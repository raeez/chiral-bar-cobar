# XV06_hochschild_xvol (458s)

- [CRITICAL] Vol III [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:272) — The formal definition of “Three Hochschild theories” replaces the canonical `topological / chiral / categorical` split with `categorical / chiral / derived center`; the chapter intro already advertises the same triad at [line 4](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4). This rewrites the programme-level taxonomy: the derived center is not the third Hochschild theory in Vol I’s concordance, but the chiral cochain-level bulk.

- [HIGH] Vol III [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:20) — The opening convention says “Hochschild” in Vol III means categorical Hochschild, then says `\Phi` lifts “topological Hochschild data” to `\mathrm{ChirHoch}^*(A_\cC)` at [line 27](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:27). That collapses categorical into topological. The same categorical-as-topological wording recurs in [hochschild_calculus.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:9).

- [HIGH] Vol II [raviolo-restriction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:107) — `Z(\cA)` is glossed as “the derived center (chiral Hochschild homology)”. In Vols I–II, the derived center is computed by chiral Hochschild cochains/cochain complex; chiral Hochschild homology is a different annular theory.

- [HIGH] Vol II [anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1491) — The boundary-anomaly passage uses bare `HH^2(V_k(\mathfrak{sl}_2))` and `B \simeq HH^\bullet(V_k(\mathfrak{sl}_2))` for VOA deformations and the bulk-boundary map. In this volume’s own theory chapter, bulk is identified with chiral Hochschild cochains of the boundary algebra, not unqualified `HH`. The same drift propagates in [anomaly_completed_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1786) and [anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:1790).

- [HIGH] Vol II [3d_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2135) — The Virasoro bulk computation uses bare `\HH^i(\mathrm{Vir}_c)` and then identifies the result with the derived centre/bulk of the boundary algebra; the same notation is repeated at [line 2255](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2255). The dedicated Virasoro chapter uses the qualified chiral theory instead at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:585).

- [MEDIUM] Vol II [thqg_holographic_reconstruction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2591) — The comparison `\operatorname{ChirHoch}^n(\cA_X) \cong \HH^n(X)` leaves the right-hand side unqualified and then speaks of the “full Hochschild diamond”. Vol I’s concordance requires explicit qualifiers when two Hochschild theories are compared; here the categorical side is only implicit.

No surviving Volume I inconsistency remained in the candidate chapter surfaces I re-read against the concordance.

## Summary
Instances checked: 25 | Violations found: 6 | Verdict: FAIL


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
session id: 019d8627-1b0a-7751-9dd0-7da4c23f5acd
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


MISSION: Cross-volume consistency check for Hochschild disambiguation.

Are the three Hochschild theories correctly distinguished? Check: chiral/topological/categorical never conflated, across all 3 repos.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers


thinking
**Evaluating file search strategies**

I'm focusing on a codebase audit, so I want to prefer using the explorer tool over manual search and file reading. I need to ask explorers first and trust their results, but the user wants actual file contents and tool outputs. I could use the explorer to find candidate files and then read them manually. With three repositories, it might be useful to have parallel explorers. I’ll aim for regular commentary updates and have to keep everything within local access.
thinking
**Assessing file reading strategy**

I’m considering whether I need to read analogous files in other volumes, as the cross-volume rule states that the live surface includes all three. However, the required reads should only focus on the current repository. I should read the exact files we directly interact with for dependencies. To start the audit, I can focus on CLAUDE, concordance, theorem_registry, and red_team_summary to ground the "three Hochschild theories." The user also asked for specific checks across chapters, so I need to keep that in mind.
codex
I’m treating this as a red-team cross-volume audit, not a local wording check. First I’m loading the repo constitution and the audit skill, then I’ll sweep all three `chapters/` trees for Hochschild terminology and read every candidate hit in context before I report anything.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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

 succeeded in 50ms:
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

thinking
**Planning file retrieval**

The user wants me to access actual file contents or tool outputs. I think I’ll use the explorer tool to find candidate files or line hits. Then I can manually open the relevant files with an exec_command. It seems like a good plan, but I'll probably need to develop a clear strategy since it looks substantial. I can update the plan while keeping track of the steps along the way. Let's break it down into four steps.
codex
I’ve loaded the constitutional statement: the canonical distinction is `topological HH / chiral HH (ChirHoch) / categorical HH`, with geometry `R / curve X / CY category` and a rule that bare “Hochschild” is only allowed for historical topological remarks. Next I’m using explorer passes to locate every Hochschild mention in each volume, then I’ll read only the actual candidate contexts and test whether the qualifiers drift or the objects get conflated.
Plan update
Cross-volume audit plan for Hochschild disambiguation. I am reading all candidate chapter surfaces first and will only report re-verified discrepancies.
  → Search all three chapter trees for Hochschild terminology and identify candidate conflation sites
  • Read each candidate hit in context and test against the canonical three-theory distinction
  • Re-check downstream duplicates and second-order propagation around each surviving finding
  • Produce severity-ordered audit report with exact file:line references and counts
collab spawn_agent(call_JuaL1MEvcl1gw6zjZJ8hXE5D, prompt="Search /Users/raeez/chiral-bar-cobar/chapters for all Hochschild-related mentions and identify candidate conflations amo…")
spawn_agent(call_JuaL1MEvcl1gw6zjZJ8hXE5D, prompt="Search /Users/raeez/chiral-bar-cobar/chapters for all Hochschild-related mentions and identify candidate conflations amo…") pending init:
  agent: 019d8627-bdaf-73c2-b415-368ae82f2046
mcp startup: no servers
collab spawn_agent(call_8rykxYfOT7Pa6El3sILVHWLo, prompt="Search /Users/raeez/chiral-bar-cobar-vol2/chapters for all Hochschild-related mentions and identify candidate conflation…")
mcp startup: no servers
spawn_agent(call_8rykxYfOT7Pa6El3sILVHWLo, prompt="Search /Users/raeez/chiral-bar-cobar-vol2/chapters for all Hochschild-related mentions and identify candidate conflation…") pending init:
  agent: 019d8627-bdc5-7bc1-aaa5-b47861c4a7f7
collab spawn_agent(call_PWqhWcXTJJhXYEeKTv2rYs4J, prompt="Search /Users/raeez/calabi-yau-quantum-groups/chapters for all Hochschild-related mentions and identify candidate confla…")
mcp startup: no servers
spawn_agent(call_PWqhWcXTJJhXYEeKTv2rYs4J, prompt="Search /Users/raeez/calabi-yau-quantum-groups/chapters for all Hochschild-related mentions and identify candidate confla…") pending init:
  agent: 019d8627-bdcb-7e83-b638-1d4b78c52308
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
chapters
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild" ../chiral-bar-cobar-vol2/chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 603

../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:653:\subsubsection{Chiral Hochschild Cochains}
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:655:The chiral Hochschild complex $\CH^\bullet_{\text{ch}}(\text{Vir})$ governs deformations of the Virasoro $A_\infty$ structure.
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:657:\begin{definition}[Chiral Hochschild Cochains for Virasoro]
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:658:A chiral Hochschild $k$-cochain is a multilinear map
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:665:The differential on $\CH^\bullet_{\text{ch}}(\text{Vir})$ is the Hochschild differential:
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:672:\begin{proposition}[Virasoro Hochschild Cohomology; \ClaimStatusConditional]
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:675:The chiral Hochschild cohomology $HH^\bullet_{\text{ch}}(\text{Vir}_c)$ is isomorphic
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:690:which is infinite-dimensional. The chiral Hochschild cohomology lives on a one-dimensional
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1252:\subsubsection{Chiral Hochschild cohomology of $\mathcal{W}_N$}
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1259:\index{Hochschild cohomology!W-algebra}%
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:847:\subsubsection{Chiral Hochschild Cochains for $W_3$}
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:849:The chiral Hochschild complex $\CH^\bullet_{\text{ch}}(W_3)$ is bi-graded by the degrees coming from $T$ and $W$.
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:851:\begin{definition}[Bi-Graded Hochschild Cochains]
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:852:A chiral Hochschild $(k_T, k_W)$-cochain is a multilinear map
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:859:The Hochschild differential is:
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:864:\begin{proposition}[$W_3$ Hochschild Cohomology; \ClaimStatusConditional]
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:867:The bi-graded chiral Hochschild cohomology is:
../chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1264:\subsubsection{Chiral Hochschild cohomology of $\mathcal{W}_N$}
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 159

chapters/examples/toroidal_elliptic.tex:1700:and the descent spectral sequence for Hochschild cohomology
chapters/examples/toroidal_elliptic.tex:2414:\index{Hochschild cohomology!K3 x E}
chapters/examples/toroidal_elliptic.tex:3933: the higher Hochschild obstructions.
chapters/examples/fukaya_categories.tex:105: \item The Hochschild homology
chapters/examples/fukaya_categories.tex:143: \item The Hochschild homology
chapters/examples/fukaya_categories.tex:372: \item \emph{Lie conformal algebra}: The Hochschild cohomology
chapters/examples/fukaya_categories.tex:524: Hochschild homology of the Fukaya category to the quantum
chapters/examples/matrix_factorizations.tex:4:The third source of CY categories is the Landau--Ginzburg model. A polynomial $W \colon \C^n \to \C$ with isolated critical point produces a $\Z/2$-graded dg-category $\MF(W)$ of matrix factorizations, and Dyckerhoff's theorem (extending Orlov's singularity-category comparison) gives $\MF(W)$ the structure of a smooth proper CY category of dimension $n - 2$. The assignment $W \mapsto \MF(W)$ is the algebraic shadow of the B-model on the LG target, and composing with the Vol~III functor $\Phi$ produces the chiral algebra of that LG theory. This chapter develops three faces of the resulting story: the CY category and its Hochschild invariants; the LG/CY correspondence, which reconciles the LG bridge with the derived-category bridge of Chapter~\ref{ch:derived-cy}; and the ADE specialization, which predicts that $\Phi(\MF(W))$ recovers the principal $\cW$-algebra of the corresponding simply-laced type.
chapters/examples/matrix_factorizations.tex:19:Kapustin and Li \cite{KapustinLi2003} identified $\MF(W)$ with the category of B-type boundary conditions of the LG model with superpotential $W$; their residue formula computes the open-string pairing. Dyckerhoff \cite{Dyckerhoff2011} proved compact generation and computed the Hochschild invariants; Polishchuk and Vaintrob \cite{PolishchukVaintrob2012} constructed the CY structure as a cyclic $\Ainf$-structure and identified the trace with the Kapustin--Li residue.
chapters/examples/matrix_factorizations.tex:36:The Hochschild invariants of $\MF(W)$ are explicit. Write $\Jac(W) = S/(\partial_1 W, \ldots, \partial_n W)$ for the Jacobi ring.
chapters/examples/matrix_factorizations.tex:38:\begin{theorem}[Hochschild invariants; Dyckerhoff, Polishchuk--Vaintrob]
chapters/examples/matrix_factorizations.tex:67:a two-dimensional $\Z/2$-graded Clifford algebra on one generator. The Jacobi ring is $\Jac(x^2) = \C[x]/(2x) \cong \C$, so $\HH_\bullet(\MF(x^2)) \cong \C$ is one-dimensional; the two-dimensional endomorphism algebra counts the $\Z/2$-graded indecomposable and its parity shift. The dimension count $2$ is the rank count of the free-fermion representation: a single holomorphic fermion contributes a two-dimensional Clifford sector, and this is the smallest nonzero input to the LG-to-chiral passage at the level of Hochschild invariants. The $n = 1$ case sits outside the CY$_2$ domain of Theorem~CY-A$_2$ (Remark~\ref{rem:mf-dim-caveat}) and is used only as the building block for the stabilized four-variable model in Section~\ref{sec:ade-w-algebras}.
chapters/examples/matrix_factorizations.tex:163:a non-degenerate quadratic form. The critical locus is the origin and the Milnor number is $\mu(\widetilde{W}_{A_1}) = 1$. The Jacobi ring is $\C[x, y, z, w]/(x, y, z, w) \cong \C$, one-dimensional, so by Theorem~\ref{thm:mf-hh} the Hochschild homology is
chapters/examples/k3_times_e.tex:476:% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
chapters/examples/k3_times_e.tex:510:produces a chiral algebra with $24$ generators (one per Hochschild class, since
chapters/examples/k3_times_e.tex:514:total Hochschild dimension. Five independent verifications appear in
chapters/examples/k3_times_e.tex:542: The $24$ Hochschild generators are present, but the CY trace projects onto a
chapters/examples/k3_times_e.tex:545: sees half the Hochschild homology. The $\Z/2$-orbifolding kills exactly the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 654

chapters/examples/deformation_quantization.tex:26: $H^2(\Defcyc(\cA))$, the chiral Hochschild cohomology of
chapters/examples/deformation_quantization.tex:141:The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$. This remains open.
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:403:More precisely (via the Hochschild deformation complex):
chapters/examples/deformation_quantization.tex:583:\item Right side: Chiral Hochschild cochains (quantum)
chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
chapters/examples/deformation_quantization.tex:608:The chiral Hochschild cohomology of the classical chiral algebra controls quantization:
chapters/examples/deformation_quantization.tex:1629:of the Hochschild--Kostant--Rosenberg theorem for dg algebras.
chapters/examples/deformation_quantization.tex:1827:\index{Hochschild--Kostant--Rosenberg!for dg algebras}
chapters/examples/deformation_quantization.tex:1841:$\HH^\bullet$ denotes Hochschild cohomology,
chapters/examples/deformation_quantization.tex:1867:over~$k$). Therefore, the derived Hochschild cohomology equals the
chapters/examples/deformation_quantization.tex:1868:strict Hochschild cohomology:
chapters/examples/deformation_quantization.tex:1874:The Hochschild--Kostant--Rosenberg theorem for dg algebras
chapters/examples/deformation_quantization.tex:1940:The Hochschild cohomology of $k$ is $\HH^\bullet(k) = k$
chapters/examples/deformation_quantization.tex:2118:theory of the singularity $Z_F$. The Hochschild cohomology
chapters/examples/deformation_quantization.tex:2130:(chiral) Hochschild cohomology of the boundary algebra, which
chapters/examples/symmetric_orbifolds.tex:56:H (Hochschild) &
chapters/examples/symmetric_orbifolds.tex:226:\begin{conjecture}[Chiral Hochschild growth;

thinking
**Running manual searches**

I’m considering running a manual search using “rg” across three repositories while I wait. The user likely wants specific tool outputs, so I can execute some commands with “rg” and search for terms like Hochschild, ChirHoch, and THH. I should keep the output manageable, perhaps by separating results by repository. A command like `rg -n -i --glob '*.tex' '(ChirHoch|Hochschild)'` seems reasonable, but I might want to narrow it down further for clarity. Let's see how it goes!
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "topological Hochschild" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/frame/preface.tex:27:to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '260,330p' chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}


%% ===================================================================
%% SECTION 4: The Hochschild bridge
%% ===================================================================

\section{The Hochschild bridge}
\label{sec:hochschild-bridge}

Three Hochschild theories act on a CY category $\cC$ with chiral algebra $A_\cC = \Phi(\cC)$, and distinguishing them is essential for the bridge to Volume~I.

\begin{definition}[Three Hochschild theories]
\label{def:three-hochschild}
Let $\cC$ be a smooth proper CY$_d$ category with chiral algebra $A_\cC = \Phi(\cC)$.
\begin{enumerate}[label=(\roman*)]
 \item \emph{Categorical Hochschild.} The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ with Hochschild differential $b$ and Connes operator $B$. This is the topological invariant of $\cC$ as a dg category: it carries the Gerstenhaber bracket and the $(2-d)$-shifted Poisson structure from the Serre pairing (Chapter~\ref{ch:hochschild-calculus}).
 \item \emph{Chiral Hochschild.} The chiral Hochschild cohomology $\ChirHoch^*(A_\cC)$ of Volume~I (Theorem~H): concentrated in cohomological degrees $\{0, 1, 2\}$ with polynomial Hilbert series. This is the obstruction-theoretic invariant governing the shadow tower of $A_\cC$.
 \item \emph{Derived center.} The chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC) = \RHom(\Omega B(A_\cC), A_\cC)$: the universal bulk algebra, computed by chiral Hochschild \emph{cochains} (not cohomology). This is the target of the holographic datum (Vol~II).
\end{enumerate}
codex
I’ve fixed the canonical test from the concordance: `topological = E1 on R -> E2`, `chiral = chiral algebra on curve -> graded vertex algebra`, `categorical = dg/A∞ category -> E2 / CY shifted Poisson`. I’m now pulling the raw chapter hits directly so the final findings rest on file contents, not on summaries.
exec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'ChirHoch|Hochschild' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'ChirHoch|Hochschild' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'ChirHoch|Hochschild' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:628:  Theorem~\ref{thm:c3-hochschild}). For general toric CY3,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1700:and the descent spectral sequence for Hochschild cohomology
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2414:\index{Hochschild cohomology!K3 x E}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3933: the higher Hochschild obstructions.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:105: \item The Hochschild homology
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:143: \item The Hochschild homology
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:372: \item \emph{Lie conformal algebra}: The Hochschild cohomology
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:375: (Chapter~\ref{ch:hochschild-calculus});
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:524: Hochschild homology of the Fukaya category to the quantum
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:4:The third source of CY categories is the Landau--Ginzburg model. A polynomial $W \colon \C^n \to \C$ with isolated critical point produces a $\Z/2$-graded dg-category $\MF(W)$ of matrix factorizations, and Dyckerhoff's theorem (extending Orlov's singularity-category comparison) gives $\MF(W)$ the structure of a smooth proper CY category of dimension $n - 2$. The assignment $W \mapsto \MF(W)$ is the algebraic shadow of the B-model on the LG target, and composing with the Vol~III functor $\Phi$ produces the chiral algebra of that LG theory. This chapter develops three faces of the resulting story: the CY category and its Hochschild invariants; the LG/CY correspondence, which reconciles the LG bridge with the derived-category bridge of Chapter~\ref{ch:derived-cy}; and the ADE specialization, which predicts that $\Phi(\MF(W))$ recovers the principal $\cW$-algebra of the corresponding simply-laced type.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:19:Kapustin and Li \cite{KapustinLi2003} identified $\MF(W)$ with the category of B-type boundary conditions of the LG model with superpotential $W$; their residue formula computes the open-string pairing. Dyckerhoff \cite{Dyckerhoff2011} proved compact generation and computed the Hochschild invariants; Polishchuk and Vaintrob \cite{PolishchukVaintrob2012} constructed the CY structure as a cyclic $\Ainf$-structure and identified the trace with the Kapustin--Li residue.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:36:The Hochschild invariants of $\MF(W)$ are explicit. Write $\Jac(W) = S/(\partial_1 W, \ldots, \partial_n W)$ for the Jacobi ring.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:38:\begin{theorem}[Hochschild invariants; Dyckerhoff, Polishchuk--Vaintrob]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:67:a two-dimensional $\Z/2$-graded Clifford algebra on one generator. The Jacobi ring is $\Jac(x^2) = \C[x]/(2x) \cong \C$, so $\HH_\bullet(\MF(x^2)) \cong \C$ is one-dimensional; the two-dimensional endomorphism algebra counts the $\Z/2$-graded indecomposable and its parity shift. The dimension count $2$ is the rank count of the free-fermion representation: a single holomorphic fermion contributes a two-dimensional Clifford sector, and this is the smallest nonzero input to the LG-to-chiral passage at the level of Hochschild invariants. The $n = 1$ case sits outside the CY$_2$ domain of Theorem~CY-A$_2$ (Remark~\ref{rem:mf-dim-caveat}) and is used only as the building block for the stabilized four-variable model in Section~\ref{sec:ade-w-algebras}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:163:a non-degenerate quadratic form. The critical locus is the origin and the Milnor number is $\mu(\widetilde{W}_{A_1}) = 1$. The Jacobi ring is $\C[x, y, z, w]/(x, y, z, w) \cong \C$, one-dimensional, so by Theorem~\ref{thm:mf-hh} the Hochschild homology is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:476:% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:510:produces a chiral algebra with $24$ generators (one per Hochschild class, since
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:514:total Hochschild dimension. Five independent verifications appear in
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:542: The $24$ Hochschild generators are present, but the CY trace projects onto a
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:545: sees half the Hochschild homology. The $\Z/2$-orbifolding kills exactly the
 succeeded in 52ms:
Total output lines: 1316

/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:26: $H^2(\Defcyc(\cA))$, the chiral Hochschild cohomology of
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:27: Theorem~\ref{thm:hochschild-bar-cobar}.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:141:The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$. This remains open.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:403:More precisely (via the Hochschild deformation complex):
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:583:\item Right side: Chiral Hochschild cochains (quantum)
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:608:The chiral Hochschild cohomology of the classical chiral algebra controls quantization:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:610:\ChirHoch^*(\mathcal{A}_{\mathrm{cl}})[\hbar]
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:643:computes $\ChirHoch^*$ via configuration space integrals.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:725:(Theorem~\ref{thm:operadic-center-hochschild}).
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1629:of the Hochschild--Kostant--Rosenberg theorem for dg algebras.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1827:\index{Hochschild--Kostant--Rosenberg!for dg algebras}
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1841:$\HH^\bullet$ denotes Hochschild cohomology,
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1867:over~$k$). Therefore, the derived Hochschild cohomology equals the
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1868:strict Hochschild cohomology:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1874:The Hochschild--Kostant--Rosenberg theorem for dg algebras
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1940:The Hochschild cohomology of $k$ is $\HH^\bullet(k) = k$
 succeeded in 52ms:
Total output lines: 787

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:653:\subsubsection{Chiral Hochschild Cochains}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:655:The chiral Hochschild complex $\CH^\bullet_{\text{ch}}(\text{Vir})$ governs deformations of the Virasoro $A_\infty$ structure.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:657:\begin{definition}[Chiral Hochschild Cochains for Virasoro]
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:658:A chiral Hochschild $k$-cochain is a multilinear map
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:665:The differential on $\CH^\bullet_{\text{ch}}(\text{Vir})$ is the Hochschild differential:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:667:% label removed: eq:hochschild-diff
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:672:\begin{proposition}[Virasoro Hochschild Cohomology; \ClaimStatusConditional]
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:673:% label removed: prop:vir-hochschild
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:675:The chiral Hochschild cohomology $HH^\bullet_{\text{ch}}(\text{Vir}_c)$ is isomorphic
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:679:is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:680:Remark~\ref*{rem:critical-level-lie-vs-chirhoch}),
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:690:which is infinite-dimensional. The chiral Hochschild cohomology lives on a one-dimensional
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1252:\subsubsection{Chiral Hochschild cohomology of $\mathcal{W}_N$}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1253:\label{subsubsec:wn-hochschild}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1259:\index{Hochschild cohomology!W-algebra}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:847:\subsubsection{Chiral Hochschild Cochains for $W_3$}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:849:The chiral Hochschild complex $\CH^\bullet_{\text{ch}}(W_3)$ is bi-graded by the degrees coming from $T$ and $W$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:851:\begin{definition}[Bi-Graded Hochschild Cochains]

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '60,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    60	The corrected global triangle \eqref{eq:global-corrected-triangle} will follow once two comparison maps are supplied:
    61	
    62	\begin{enumerate}[label=(\arabic*),leftmargin=1.8em]
    63	\item a \emph{bulk/boundary comparison}
    64	\[
    65	\beta_{\der}:\Abulk\longrightarrow \Zder(B_b)
    66	\]
    67	for a rich boundary condition $b$;
    68	\item a \emph{boundary/line comparison}
    69	\[
    70	\End_{\cC_{\mathrm{line}}}(M_b)\simeq B_b
    71	\]
    72	showing that the chosen boundary vacuum $M_b$ generates the line category.
    73	\end{enumerate}
    74	
    75	Once these exist, Proposition~\ref{prop:formal-global-triangle} finishes the job. So the theorem is not one enormous mystery. It is two comparison theorems plus Morita invariance.
    76	
    77	\subsection{Why the local exact sector matters for the global problem}
    78	
    79	The local theorem package proved above gives a template for the global attack:
thinking
**Identifying candidate Hochschild conflations**

I’m gathering specific file and line references where different Hochschild theories might be conflated, focusing on mentions of "topological Hochschild," "chiral Hochschild," "categorical Hochschild," and more general "Hochschild" terms like "derived center." I plan to verify contexts closely using line-numbered excerpts to pinpoint spots where the user might find ambiguous or overlapping descriptions across chapters.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3630,3685p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
centers are not known to coincide. Warning~\ref{warn:multiple-e1-chiral}
in Chapter~\ref{ch:algebraic-foundations} records the full
comparison table.

The monograph uses Notion~(B) throughout. Every theorem
stated for ``an $E_1$-chiral algebra $\cA$'' means a
Notion~(B) structure unless explicitly qualified.

\subsection*{10.4.\enspace Three Hochschild theories}

Three a priori distinct Hochschild-type constructions
appear in the programme:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item \emph{Chiral Hochschild cohomology}
 $\mathrm{ChirHoch}^*(\cA)$: the subject of Theorem~H,
 computed from the chiral bar complex on curves.
 Polynomial Hilbert series, concentrated in degrees
 $\{0,1,2\}$.
\item \emph{Topological Hochschild homology}
 $\mathrm{THH}(\cA)$: factorisation homology over~$S^1$,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/frame/preface.tex | sed -n '400,450p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   400	\section*{IV.\quad The Steinberg principle}
   401	
   402	The Steinberg variety
   403	$\widetilde{\cN} \times_{\fg} \widetilde{\cN}$ is one geometric
   404	object; Borel--Moore homology, $K$-theory, and equivariant derived
   405	category extract three algebraic invariants: the Hecke algebra,
   406	the Springer correspondence, and the Kazhdan--Lusztig basis. The
   407	chiral bar complex $\barBch(\cA)$ on
   408	$\FM_k(\C) \times \Conf_k^{<}(\R)$ is one coalgebra, and three
   409	functors project three objects from it: cobar
   410	$\Omega(\barBch(\cA)) \simeq \cA$ recovers the original algebra
   411	as inversion (the left adjoint of bar, not Koszul duality);
   412	Verdier duality on the Ran space,
   413	$\mathbb{D}_{\mathrm{Ran}}(\barBch(\cA)) \simeq \barBch(\cA^!)$,
   414	is Koszul duality proper; and chiral Hochschild cochains
   415	$C^\bullet_{\mathrm{ch}}(\cA,\cA)$ compute the bulk as the
   416	derived centre $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. The
   417	three functors are genuinely distinct: cobar is inversion,
   418	Verdier is Koszul duality, Hochschild is the derived centre.
   419	Three Hochschild theories coexist: chiral Hochschild
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '10,80p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Volumes~I and~II develop the bar-cobar machine that extracts
modular invariants from any chiral algebra~$A$ on a curve~$X$:
the bar complex $B(A) = T^c(s^{-1}\bar{A})$ with its
deconcatenation coproduct, the universal Maurer--Cartan element
$\Theta_A$, the modular characteristic
$\kappa_{\mathrm{ch}}(A)$, and the five theorems that control
the genus tower. Neither volume constructs a single chiral
algebra. The input is always assumed. This volume constructs
the input.

A terminological point: ``Hochschild'' in this volume means
categorical Hochschild cohomology: the cyclic bar complex
$\mathrm{CC}_*(\cC)$ of a dg or $\Ainf$-category, topological
in nature. The chiral upgrade $\mathrm{ChirHoch}^*(A)$ of
Volume~I (Theorem~H) is the holomorphic version; it is the
output of the functor $\Phi$, not the input. The two are
related by the functor itself: $\Phi$ sends $\mathrm{CC}_*(\cC)$
to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
data to holomorphic chiral data on the curve.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/examples-worked.tex | sed -n '1230,1280p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1230	 $\kappa(\cA^!) = -\kappa(\cA)$ with $V_{-k-2h^\vee}(\fg)$
  1231	 but is categorically distinct \textup{(}cf.\\textup{)}.
  1232	 On the associated graded \textup{(}PBW filtration\textup{)},
  1233	 $\operatorname{gr}\cA_\partial^! \simeq C^\bullet(\fg[t^{-1}]t^{-1})$.
  1234	 The Koszul involution exchanges Neumann~$\leftrightarrow$~Dirichlet
  1235	 boundary conditions.
  1236	
  1237	\item \textbf{Derived center \textup{(}universal bulk\textup{)}.}
  1238	 $\Zder^{\mathrm{ch}}(\cA_\partial)
  1239	 = C^\bullet_{\mathrm{ch}}(V_k(\fg),\, V_k(\fg))$.
  1240	 The bulk observables are chiral Hochschild cochains of the boundary
  1241	 algebra, not the bar complex.
  1242	
  1243	\item \textbf{Collision residue.}
  1244	 $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
  1245	 equation. The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
  1246	
  1247	\item \textbf{Modular MC element.}
  1248	 $\Theta_\cA = D_\cA - d_0 \in \MC(\gAmod)$, with modular
  1249	 characteristic $\kappa = \kappa(V_k(\fg))
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '10040,10120p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Theorem~\ref{thm:off-koszul-ran-inversion}) gives
$\Omega^{\mathrm{co}}(\barB^{\mathrm{ord}}(\cA)) \simeq \cA$
in~$\Dco$ for arbitrary shadow class; this uses the
coderived BV$=$bar identification
(Theorem~\ref{thm:bv-bar-coderived}) to absorb the
$m_0$-proportional obstructions.
On the Koszul locus the conilpotent reduction theorem
(Theorem~\ref{thm:conilpotent-reduction}) identifies
$\Dco$ with the ordinary derived category, so the coderived
bialgebra is a genuine DG-bialgebra.
\end{proof}

\begin{remark}[The projection disease]
\label{rem:projection-disease}%
\index{projection disease|textbf}%
\index{coderived chiral bialgebra!projection disease}%
The coderived chiral bialgebra $\barB^{\mathrm{ord}}(\cA)$ is
the single primitive object from which
the apparently heterogeneous landscape of products, coproducts,
and intertwining maps is recovered by applying different functors.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "topological Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/preface.tex:421:$\cZ^{\mathrm{der}}_{\mathrm{ch}}$), topological Hochschild
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "derived center.*Hochschild" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/hochschild_cohomology.tex:1000:The bridge between the derived center and Hochschild cochains is the
chapters/theory/hochschild_cohomology.tex:1053:\index{derived center!Hochschild identification}
chapters/connections/genus_complete.tex:776:where $Z_{\mathrm{der}}$ denotes the derived center (Hochschild
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1,200p' chapters/theory/hochschild_calculus.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Hochschild Calculus for CY Categories}
\label{ch:hochschild-calculus}

%%: kappa always subscripted in Vol III.
%%: E_1/ordered is primitive; unordered is derived quotient.

\begin{remark}[Convention: categorical Hochschild]
\label{rem:hochschild-convention-categorical}
In this chapter, ``Hochschild'' refers to the categorical Hochschild
invariants of a dg category (the cyclic bar complex
$\mathrm{CC}_*(\cC)$), which are topological in nature.
The chiral Hochschild cohomology $\ChirHoch^*$ of Volume~I
(Theorem~H) is the chiral upgrade incorporating OPE data and curve
geometry.  The CY-to-chiral functor $\Phi$ of
Chapter~\ref{ch:cy-to-chiral} maps the categorical Gerstenhaber
bracket to the chiral convolution bracket.
\end{remark}

A Calabi--Yau $d$-category has a non-degenerate Serre pairing. What does this pairing force on the Hochschild invariants? For a general dg category, Hochschild homology $\HH_\bullet(\cC)$ carries only a Connes $B$-operator and Hochschild cohomology $\HH^\bullet(\cC)$ carries only a Gerstenhaber bracket; the two are linked by a cap product, but no pairing relates them. The CY structure removes this deficiency.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2080,2110p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2080	$K^{\ex}_{F,p}$ & exact pointed line algebra \\
  2081	\hline
  2082	$\kappa$ & reduced Kuranishi map after eliminating linearly massive directions \\
  2083	\hline
  2084	$K_\kappa$ & minimal pointed line algebra \\
  2085	\hline
  2086	$A^!_{\mathrm{line}}$ & absolute open-colour Koszul-dual algebra conjecturally controlling all lines in the global theory \\
  2087	\hline
  2088	$\Zder$ & derived center \\
  2089	\hline
  2090	$\HH^\bullet$ & Hochschild cochains/cohomology \\
  2091	\hline
  2092	\end{longtable}
  2093	\end{center}
  2094	
  2095	% Bibliography entries consolidated into main.tex.
  2096	
  2097	
  2098	%================================================================
  2099	% THE GENUS-ZERO HOLOGRAPHIC SPINE AND AMBIENT COMPLEMENTARITY
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '980,1010p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{def:derived-center}
\index{derived center|textbf}
For a $k$-linear dg-category $\mathcal{C}$, the \emph{derived center}
is the dg-algebra of derived endomorphisms of the identity functor:
\[
Z_{\mathrm{der}}(\mathcal{C})
:= \RHom_{\mathrm{Fun}(\mathcal{C}, \mathcal{C})}
 (\mathrm{Id}_{\mathcal{C}},\, \mathrm{Id}_{\mathcal{C}}).
\]
A degree-$n$ cocycle in $Z_{\mathrm{der}}(\mathcal{C})$ is a
natural transformation $\mathrm{Id}_{\mathcal{C}} \Rightarrow
\mathrm{Id}_{\mathcal{C}}[n]$; its cohomology class is a derived
natural transformation. The product on $Z_{\mathrm{der}}(\mathcal{C})$
is composition of natural transformations; in particular,
$H^0(Z_{\mathrm{der}}(\mathcal{C}))$ is the ordinary center of the
homotopy category $[\mathcal{C}]$.
\end{definition}

\subsection{Endofunctors as bimodules}


exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "bulk.*Hochschild" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/examples-worked.tex:87:For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
chapters/examples/examples-worked.tex:1240: The bulk observables are chiral Hochschild cochains of the boundary
chapters/examples/examples-computing.tex:464:The bulk--boundary correspondence (Theorem~\ref{thm:bulk_hochschild}) identifies bulk observables with chiral Hochschild cochains of $\widehat{\mathfrak{u}(1)}_k$, realizing concretely the framework of Sections~\ref{sec:chiral_hochschild_expanded}--\ref{sec:bar_cobar}.
chapters/connections/ht_bulk_boundary_line.tex:622:The first identity is the boundary dg algebra with $F=0$. The second is ordinary completed Koszul duality. The final statement follows from Theorem~\ref{thm:boundary-linear-bulk-boundary} and the Morita invariance of Hochschild cohomology.
chapters/connections/ht_bulk_boundary_line.tex:1073:\item the local bulk algebra is recovered from $K_\kappa$ by Hochschild cochains;
chapters/connections/ht_bulk_boundary_line.tex:1272:\item \textbf{derived center}: bulk should be recovered from lines by Hochschild cochains;
chapters/connections/celestial_holography_frontier.tex:1182:the bulk twisting morphism and the line-side chiral Hochschild
chapters/connections/hochschild.tex:345:The relationship between bulk local operators and chiral Hochschild cochains is as follows.
chapters/connections/hochschild.tex:389:Let\/ $\mathsf{Obs}$ be a holomorphic--topological prefactorization algebra on\/ $\C\times\R$ arising from a physical realization in the scope of Theorem~\ref{thm:physics-bridge}, and let $A_{\partial}$ be the boundary chiral algebra obtained by restricting\/ $\mathsf{Obs}$ to the boundary\/ $\C\times\{0\}$. Then bulk local operators are quasi-isomorphic to chiral Hochschild cochains:
chapters/connections/hochschild.tex:399:the global case is conjectural, and an abstract bulk/Hochschild comparison for an arbitrary logarithmic\/ $\SCchtop$-algebra without a chosen HT prefactorization realization is not established here
chapters/connections/hochschild.tex:414:\begin{remark}[Scope of the bulk--Hochschild identification]
chapters/connections/hochschild.tex:416:The quasi-isomorphism $\mathcal{O}_{\mathrm{bulk}} \simeq C^\bullet_{\mathrm{ch}}(A_{\partial}, A_{\partial})$ is proved here for HT prefactorization algebras in the scope of Theorem~\ref{thm:physics-bridge}; the proof uses reduction along $\R$ and factorization homology of the chosen prefactorization model $\mathsf{Obs}$. The stronger triangle composition (that bulk $\simeq$ derived center of boundary) further requires compact generation and the derived center quasi-isomorphism. These are verified rigorously only in the boundary-linear exact sector (Theorem~\ref{thm:boundary-linear-bulk-boundary}). The global triangle for all HT theories remains conjectural, and the manuscript does not currently prove an abstract bulk/Hochschild comparison for an arbitrary logarithmic $\SCchtop$-algebra without a physical realization.
chapters/connections/hochschild.tex:430:differential $d_{\mathrm{bulk}}$ with the chiral Hochschild
chapters/connections/hochschild.tex:474:The holomorphic weight filtration on the bulk side matches the \emph{Hochschild filtration} on $C^\bullet_{\mathrm{ch}}(A_{\partial}, A_{\partial})$: filtration degree $p$ on the bulk corresponds to cochains supported on $\Ran_{\leq p}(\C)$, i.e., cochains of at most $p$ inputs. This is because each additional insertion point introduces a new collision divisor contributing to the pole order.
chapters/connections/hochschild.tex:479:The total differential $d_{\mathrm{bulk}}$ on $\int_{\C} \mathsf{Obs}^{\R}$ has two components, which we identify with the two components of the chiral Hochschild differential $d_{\mathrm{ch}} = \delta_Q + \delta_{\mathrm{Hoch}}$.
chapters/connections/hochschild.tex:488:\item \emph{Hochschild differential $\delta_{\mathrm{Hoch}}$:} The factorization product (gluing bulk operators as insertion points collide) is controlled by the codimension-1 boundary faces of $\FM_k(\C)$. For an $n$--cochain $f_n$, the Hochschild differential inserts $m_2$ at adjacent positions:
chapters/connections/hochschild.tex:574:Parts (i) and (ii) are established in \cite{CDG20}, Section 4. Part (iii) follows from our bulk--Hochschild identification (Theorem \ref{thm:bulk_hochschild}): the center $Z(A_{\partial})$ corresponds to $HH^0(A_{\partial}, A_{\partial})$, which is the degree-0 component of chiral Hochschild cohomology. Part (iv) is the module structure induced by the bulk-to-boundary restriction map.
chapters/connections/hochschild.tex:673:between chiral Hochschild cochains of the local algebra $A$ and the complex of bulk local observables supported in a small $3$--ball, with filtration by holomorphic weight. On associated graded, this identification reduces to the BD--chiral Hochschild complex on the closed color tensored with the $E_1$ Hochschild complex on the open color.
chapters/connections/hochschild.tex:1177:The bulk algebra of a 3d HT theory is the chiral Hochschild cochain
chapters/connections/hochschild.tex:1230:The bulk algebra at the Hochschild level is
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Topological Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:3648:\item \emph{Topological Hochschild homology}
chapters/theory/e1_modular_koszul.tex:1156:\begin{remark}[Topological Hochschild homology and the stratified comparison]
chapters/theory/introduction.tex:706:\emph{Topological Hochschild} $\mathrm{HH}^*_{\mathrm{top}}$
chapters/connections/concordance.tex:108:\item \emph{Topological Hochschild cohomology} $\HH^*(A, A)$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/ht_bulk_boundary_line.tex | sed -n '1060,1095p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1060	K_\kappa\simeq \Lambda(T_pF^{-1}(0)).
  1061	\]
  1062	\end{corollary}
  1063	
  1064	\begin{proof}
  1065	Smoothness is equivalent to surjectivity of $dF_p$, hence $C=\coker(dF_p)=0$. Therefore $\kappa=0$ and only the free exterior algebra on $T=\ker(dF_p)$ remains.
  1066	\end{proof}
  1067	
  1068	
  1069	\section{Local bulk from local lines, and the boundary-linear line Mather--Yau theorem}% label removed: sec:classification
  1070	
  1071	The previous section produces the minimal pointed line algebra $K_\kappa$ attached to a boundary vacuum. The proof of two culmination theorems:
  1072	\begin{enumerate}[label=(\arabic*),leftmargin=1.8em]
  1073	\item the local bulk algebra is recovered from $K_\kappa$ by Hochschild cochains;
  1074	\item the polarized quasi-isomorphism class of $K_\kappa$ classifies the reduced microlocal formal germ.
  1075	\end{enumerate}
  1076	
  1077	\subsection{Local bulk from local lines}
  1078	
  1079	Let $\gamma$ denote the coordinate on $C^\vee$. The effective boundary-linear potential determined by the Kuranishi map is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1140,1175p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

%% ════════════════════════════════════════════════════════════════════════
%% FORMALITY BRIDGE AND FAILURE
%% ════════════════════════════════════════════════════════════════════════

\subsection{Formality: when ordered equals symmetric}
\label{subsec:formality-bridge}
\index{formality!ordered vs symmetric|textbf}
\index{Kontsevich--Tamarkin!operad formality}

Four formality conditions control the relationship between
ordered chiral homology and its symmetric shadow.
Condition (a) is unconditional; conditions (b)--(d) are
logically ordered implications that, on the standard
landscape, are all equivalent to class~$\mathbf{G}$.

\begin{remark}[Topological Hochschild homology and the stratified comparison]
\label{rem:thh-vs-ord-ch}
\index{topological Hochschild homology!definition}
\index{factorisation homology!over $S^1$}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/ht_bulk_boundary_line_core.tex | sed -n '1720,1755p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1720	\subsection{Smooth vacua}
  1721	
  1722	\begin{corollary}[Smooth-point formality; \ClaimStatusProvedHere]\label{cor:smooth-formality}
  1723	If $p$ is a smooth point of the classical zero locus $F^{-1}(0)$, then $C=0$ and the minimal pointed line algebra is the exterior algebra
  1724	\[
  1725	K_\kappa\simeq \Lambda(T_pF^{-1}(0)).
  1726	\]
  1727	\end{corollary}
  1728	
  1729	\begin{proof}
  1730	Smoothness is equivalent to surjectivity of $dF_p$, hence $C=\coker(dF_p)=0$. Therefore $\kappa=0$ and only the free exterior algebra on $T=\ker(dF_p)$ remains.
  1731	\end{proof}
  1732	
  1733	
  1734	\section{Local bulk from local lines, and the boundary-linear line Mather--Yau theorem}\label{sec:classification}
  1735	
  1736	The previous section produces the minimal pointed line algebra $K_\kappa$ attached to a boundary vacuum. The proof of two culmination theorems:
  1737	\begin{enumerate}[label=(\arabic*),leftmargin=1.8em]
  1738	\item the local bulk algebra is recovered from $K_\kappa$ by Hochschild cochains;
  1739	\item the polarized quasi-isomorphism class of $K_\kappa$ classifies the reduced microlocal formal germ.
thinking
**Inspecting chiral count**

I’m thinking about whether the count conflates chiral HH with a derived center; it's something I need to inspect further. It might be marked as [HIGH]. Also, there's a reference in `examples-worked.tex` about the annulus trace being linked to the standard Hochschild homology. This could relate to Vol II, likely involving topological or categorical aspects. I need to gather more context to clarify everything properly!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3725,3755p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
center, and the derived center, each recovering the next.
The passage from the ordered bar to the symmetric bar is the
operadic shadow of the passage from the boundary to the bulk.

\bigskip

\noindent\textbf{The open/closed world (Volume~II).}
Volume~II lifts the bar complex to three dimensions. On the product
$\mathbb C_z \times \mathbb R_t$, the bar complex $\barB(\cA)$ is a
single-coloured $\Eone$-chiral dg coalgebra over
$(\mathrm{ChirAss})^!$: its differential extracts OPE residues from
collisions in the holomorphic plane, and its deconcatenation coproduct
is the cofree coassociative structure on the desuspended augmentation
ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$, not the bar
complex itself: the two-colour open/closed structure emerges when the
bar complex is fed into the Hochschild construction.

The primitive object of three-dimensional holomorphic-topological
quantum field theory on $\mathbb C_z \times \mathbb R_t$ is the
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "Hochschild.*BKM" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/modular_koszul_bridge.tex:94:The categorical modular characteristic $\kappa_{\mathrm{cat}}(\cC)$ is a topological invariant of the CY category $\cC$ (it depends only on the Hochschild homology dimensions). The chiral modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$ is an analytic invariant of the chiral algebra $A_\cC$ (it depends on the OPE structure and the generating field content). Proposition~\ref{prop:kappa-cat-chi-cy} identifies them at $d = 2$; at $d = 3$ the identification is Conjecture~\ref{conj:cy-kappa-identification} and is verified for $\C^3$ (\S\ref{subsec:c3-bridge-example}). Both are distinct from $\kappa_{\mathrm{BKM}}$ (the BKM algebra weight) and $\kappa_{\mathrm{fiber}}$ (the lattice rank); the four values constitute the $\kappa_\bullet$-spectrum (Remark~\ref{rem:cy3-kappa-polysemy}).
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/connections/bar_cobar_bridge.tex:235:The following compact CY$_3$ families illustrate the range of shadow tower behaviour. In each case, the predicted modular characteristic is $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$ (BCOV prediction); the shadow depth class, Hochschild data, and BKM structure vary.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:4917:cycles in the bar complex (which control Hochschild via bar-cobar)
chapters/frame/preface.tex:3741:bar complex is fed into the Hochschild construction.
chapters/theory/ordered_associative_chiral_kd.tex:4768:close the two-sided cobar complex into the coHochschild
chapters/theory/ordered_associative_chiral_kd.tex:4779:\begin{theorem}[Annular bar complex computes chiral Hochschild homology;
chapters/theory/ordered_associative_chiral_kd.tex:4782:\index{annular bar complex!Hochschild homology|textbf}%
chapters/theory/ordered_associative_chiral_kd.tex:10867:\item Annular bar complex computes chiral Hochschild homology:
chapters/theory/hochschild_cohomology.tex:74:What replaces the bimodule $A \otimes A^{\mathrm{op}}$ when the algebra lives on a curve rather than a point? For chiral algebras, each ingredient of the classical theory acquires a geometric upgrade: the bimodule structure is replaced by the factorization structure on~$\operatorname{Ran}(X)$, the bar resolution becomes the geometric bar complex on Fulton--MacPherson configuration spaces, and the Gerstenhaber bracket lifts to a chiral bracket governed by the OPE. The result is a chiral Hochschild complex whose cohomology computes chiral deformations, obstructions, and the center of the chiral algebra simultaneously.
chapters/theory/chiral_hochschild_koszul.tex:1983:cyclic coderivations of the bar complex, which is the Hochschild
codex
- `chapters/connections/ht_bulk_boundary_line_frontier.tex:84` — the derived-center bullet simply says “bulk should be recovered from lines by Hochschild cochains,” leaving it unclear whether this is the chiral bulk identification, the categorical derived center, or a topological $\Etwo$ comparison and so inviting conflation.  
- `chapters/connections/ht_bulk_boundary_line_frontier.tex:2090` — the glossary row for `HH^\bullet` only calls it “Hochschild cochains/cohomology” without noting which of the three flavours (chiral bulk, topological line, or categorical slab) controls each corner of the bulk–boundary–line triangle.  
- `chapters/connections/ht_bulk_boundary_line.tex:1073` — the local-bulk theorem claims “the local bulk algebra is recovered … by Hochschild cochains” while simultaneously invoking the boundary/line data, so it reads as if any Hochschild theory (topological, chiral, or categorical) would do and could easily be misinterpreted as a different flavour than intended.
codex
The broad sweep is noisy, but one strong candidate already emerged: Vol III has a section that explicitly redefines the “three Hochschild theories” as `categorical / chiral / derived center`, which conflicts with the concordance’s `topological / chiral / categorical`. I’m verifying that in file context now, then I’ll check whether Vol II repeats the same substitution or keeps the canonical split.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '1,340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '410,435p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'three Hochschild|topological Hochschild|categorical Hochschild|derived center|chiral Hochschild homology|chiral Hochschild cochains|Bare "'``Hochschild'"''|bare \"Hochschild\"|historical remarks' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   410	$\Omega(\barBch(\cA)) \simeq \cA$ recovers the original algebra
   411	as inversion (the left adjoint of bar, not Koszul duality);
   412	Verdier duality on the Ran space,
   413	$\mathbb{D}_{\mathrm{Ran}}(\barBch(\cA)) \simeq \barBch(\cA^!)$,
   414	is Koszul duality proper; and chiral Hochschild cochains
   415	$C^\bullet_{\mathrm{ch}}(\cA,\cA)$ compute the bulk as the
   416	derived centre $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. The
   417	three functors are genuinely distinct: cobar is inversion,
   418	Verdier is Koszul duality, Hochschild is the derived centre.
   419	Three Hochschild theories coexist: chiral Hochschild
   420	(OPE composition on $\Ran(\C)$, producing
   421	$\cZ^{\mathrm{der}}_{\mathrm{ch}}$), topological Hochschild
   422	($E_1$-bar composition on $\R$, producing the line category),
   423	and categorical Hochschild (Morita composition on
   424	$\C \times \R$, producing the slab bimodule;
   425	see~\cite{BZFN10} for the categorical framework). The derived centre
   426	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the first.
   427	Identifying any two collapses the architecture. Every chapter of
   428	this volume is a projection of the single coalgebra through one
   429	of the three.
 succeeded in 51ms:
     1	\chapter{Modular Koszul Duality and CY Geometry}
     2	\label{ch:modular-koszul-bridge}
     3	
     4	A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
     5	
     6	
     7	%% ===================================================================
     8	%% SECTION 1: CY modular convolution algebra
     9	%% ===================================================================
    10	
    11	\section{The modular convolution algebra for CY categories}
    12	\label{sec:modular-conv-cy}
    13	
    14	Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.
    15	
    16	\begin{definition}[CY modular convolution algebra]
    17	\label{def:cy-modular-convolution}
    18	The \emph{CY modular convolution algebra} of the pair $(B(A_\cC), A_\cC)$ is the graded vector space
    19	\[
    20	 \mathrm{Conv}_{\mathrm{str}}\bigl(B(A_\cC), A_\cC\bigr)
 succeeded in 52ms:
Total output lines: 504

/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:173:or bulk side is the chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:938:brace algebra, derived center, twisted holography boundary, line
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:61:The convolution dg Lie algebra $\mathrm{Conv}_{\mathrm{str}}(B(A_\cC), A_\cC)$ is the ambient home of $\Theta_{A_\cC}$; it is distinct from the chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC) = \RHom(\Omega B(A_\cC), A_\cC)$, which computes the bulk observables (Theorem~H). The three functors $\Omega$, $D_\Ran$, $C^\bullet_{\mathrm{ch}}(A, A)$ produce three distinct outputs from $B(A_\cC)$, and the convolution algebra is none of them: it is the \emph{working surface} on which $\Theta_{A_\cC}$ solves the master equation.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:278: \item \emph{Derived center.} The chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC) = \RHom(\Omega B(A_\cC), A_\cC)$: the universal bulk algebra, computed by chiral Hochschild \emph{cochains} (not cohomology). This is the target of the holographic datum (Vol~II).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:280:These are distinct invariants. The categorical Hochschild lives on $\cC$ (no curve geometry); the chiral Hochschild lives on $A_\cC$ (curve geometry through the OPE); the derived center is the endomorphism algebra of the identity functor in the factorization category (curve geometry through $\Ran(X)$).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:292: \item A map $\HH^\bullet(\cC, \cC) \to \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ from the categorical Hochschild cochains (the endomorphism algebra of the identity bimodule) to the chiral derived center, compatible with the Gerstenhaber product on the source and the chiral bracket on the target.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:297:Part (i) is Proposition~\ref{prop:bar-dictionary}. For (ii): the Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a Lie bracket of degree $-1$. Under $\Phi$, this bracket becomes the convolution bracket of Vol~I by functoriality of the bar construction: the deconcatenation coproduct on $B(A_\cC)$ and the binary product of $A_\cC$ assemble into a bracket on $\Hom_{\Ran}(B(A_\cC), A_\cC)$, which restricts to $\ChirHoch^*(A_\cC)$ on the cohomology. The Connes operator $B$ on $\mathrm{CC}_\bullet(\cC)$ corresponds, under the bar dictionary, to the degree-preserving component of the bar differential (Proposition~\ref{prop:bar-dictionary}(ii)), which is the modular differential on the chiral side. For (iii): the categorical Hochschild cochains $\mathrm{CC}^\bullet(\cC, \cC)$ map to $\RHom(\Omega B(A_\cC), A_\cC)$ by applying $\Phi$ to each hom-space and using the bar-cobar quasi-isomorphism $\Omega B(A_\cC) \simeq A_\cC$ (Vol~I Theorem~B on the Koszul locus).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:302:The categorical Hochschild $\HH_\bullet(\cC)$ controls the deformation theory of $\cC$ as a CY category: $\HH^2(\cC)$ parametrizes first-order deformations, $\HH^1(\cC)$ the infinitesimal automorphisms. The chiral Hochschild $\ChirHoch^*(A_\cC)$ controls the shadow tower of $A_\cC$: the obstruction classes $\mathrm{obs}_g$ live in $\ChirHoch^2(A_\cC) \otimes H^\bullet(\overline{\cM}_{g,n})$. The derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ is the bulk algebra of the holographic datum: its elements are the operators that commute with all boundary insertions. Theorem~\ref{thm:hochschild-bridge} guarantees that the categorical deformation data of $\cC$ is faithfully transmitted, through $\Phi$, to the chiral obstruction data of $A_\cC$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:9:% (3) Z^{der}_{ch}(A) = RHom(Omega(B(A)), A) (derived center, BULK)
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:11:% It is NOT the derived center (which would be Hochschild cochains).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:48: \item $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A) = \RHom(\Omega(B(A)), A)$ is the chiral derived center, computing the universal bulk (Theorem~H).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:50:These are not the same operation, and the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ corresponds to $B(A)$ itself, not to the derived center and not to the cobar.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:193: where $\cZ(A_\cC) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ is the chiral derived center.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:4:The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:34: \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:36:Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:21:categorical Hochschild cohomology: the cyclic bar complex
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/frame/preface.tex | sed -n '10,70p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '130,180p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    10	Volumes~I and~II develop the bar-cobar machine that extracts
    11	modular invariants from any chiral algebra~$A$ on a curve~$X$:
    12	the bar complex $B(A) = T^c(s^{-1}\bar{A})$ with its
    13	deconcatenation coproduct, the universal Maurer--Cartan element
    14	$\Theta_A$, the modular characteristic
    15	$\kappa_{\mathrm{ch}}(A)$, and the five theorems that control
    16	the genus tower. Neither volume constructs a single chiral
    17	algebra. The input is always assumed. This volume constructs
    18	the input.
    19	
    20	A terminological point: ``Hochschild'' in this volume means
    21	categorical Hochschild cohomology: the cyclic bar complex
    22	$\mathrm{CC}_*(\cC)$ of a dg or $\Ainf$-category, topological
    23	in nature. The chiral upgrade $\mathrm{ChirHoch}^*(A)$ of
    24	Volume~I (Theorem~H) is the holomorphic version; it is the
    25	output of the functor $\Phi$, not the input. The two are
    26	related by the functor itself: $\Phi$ sends $\mathrm{CC}_*(\cC)$
    27	to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
    28	data to holomorphic chiral data on the curve.
    29	
 succeeded in 50ms:
 Output: a chain complex carrying an $E_2$-structure
 with Calabi--Yau shifted Poisson structure when~$\cC$
 is proper Calabi--Yau.
 Geometric origin: the circle~$S^1$ and its
 cyclic bar construction.
\end{enumerate}

\noindent
The geometry determines which theory applies:
curve~$X$ $\to$ chiral,
real line~$\bR$ $\to$ topological,
Calabi--Yau category $\to$ categorical.
When a comparison relates two theories
(e.g.\ equation~\eqref{eq:bbj-comparison} in
Chapter~\ref{chap:e1-modular-koszul}),
the qualifier on each side is mandatory.
Bare ``Hochschild'' without qualifier is
permitted only in historical remarks about the
classical (topological) theory; in all other
contexts, one of the three adjectives
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/connections/bar_cobar_bridge.tex | sed -n '210,250p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   210	We summarize the status of the five main theorems of Volume~I when specialized to chiral algebras arising from CY categories.
   211	
   212	\begin{theorem*}[The five theorems for CY chiral algebras]
   213	Let $A = A_\cC$ be the chiral algebra of a CY$_3$ category $\cC$. Then:
   214	\begin{description}
   215	 \item[Theorem A (adjunction).] The bar-cobar adjunction $B \dashv \Omega$ restricts to CY chiral algebras: $B(A_\cC)$ is a factorization coalgebra on $\Ran(X)$, and $D_{\Ran}(B(A_\cC)) \simeq B(A_{\cC^!})$. The CY identification CY-A(ii) gives $\mathrm{CC}_\bullet(\cC) \simeq B(A_\cC)$.
   216	
   217	 \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.
   218	
   219	 \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
   220	
   221	 \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
   222	
   223	 \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
   224	\end{description}
   225	\end{theorem*}
   226	
   227	
   228	%% ===================================================================
   229	%% SECTION 7: Compact CY3 examples

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bbj" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:1308:\label{rem:bbj-latyntsev-comparison}
chapters/theory/e1_modular_koszul.tex:1319:\begin{equation}\label{eq:bbj-comparison}
chapters/connections/concordance.tex:143:(e.g.\ equation~\eqref{eq:bbj-comparison} in
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1290,1335p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
ordered theory that the symmetric quotient discards.
\end{theorem}

\begin{proof}
Arnold's Poincar\'e polynomial for
$H^*(\Conf_n(\bC))$ is
$P_n(t) = \prod_{j=0}^{n-1}(1 + jt)$; setting $t=1$
gives $P_n(1) = n!$. The ordered chiral complex is
$\Omega^*_{\log}(\overline{\operatorname{FM}}_n^{\mathrm{ord}})
\otimes (s^{-1}\bar\cA)^{\otimes n}$; at the
cohomological level the $\Omega^*_{\log}$ factor
contributes the Arnold algebra of total dimension~$n!$.
The $\Sigma_n$-non-equivariance of the bar differential
(from $S(z) \neq \tau$) obstructs the descent to the
symmetric quotient that the formality bridge requires.
\end{proof}

\begin{remark}[Comparison with Ben-Zvi--Brochier--Jordan and Latyntsev]
\label{rem:bbj-latyntsev-comparison}
\index{Ben-Zvi--Brochier--Jordan!comparison with ordered chiral homology}
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '70,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    70	This is the holomorphic Euler characteristic of $\cC$ as a CY category (equivalently, for $\cC = D^b(\Coh(X))$ with $X$ a smooth projective CY$_d$ manifold, $\kappa_{\mathrm{cat}}(\cC) = \chi(\cO_X) = \sum_i (-1)^i h^{0,i}(X)$). It is distinct from the chiral modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$ of the chiral algebra $A_\cC = \Phi(\cC)$ (Conjecture~\ref{conj:cy-kappa-identification}; see Remark~\ref{rem:kappa-cat-vs-kappa-ch} below).
    71	\end{definition}
    72	
    73	\begin{proposition}[$\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$ under $\Phi$ at $d = 2$]
    74	\label{prop:kappa-cat-chi-cy}
    75	\ClaimStatusProvedHere
    76	For $\cC$ a smooth proper CY$_2$ category with chiral algebra $A_\cC = \Phi(\cC)$ (CY-A at $d = 2$, PROVED),
    77	\[
    78	 \kappa_{\mathrm{ch}}(A_\cC) \;=\; \kappa_{\mathrm{cat}}(\cC) \;=\; \chi^{\CY}(\cC).
    79	\]
    80	Consequently, for every genus $g \geq 1$ and on the uniform-weight lane,
    81	\[
    82	 \mathrm{obs}_g(A_\cC) \;=\; \kappa_{\mathrm{cat}}(\cC) \cdot \lambda_g
    83	 \qquad (g \geq 1,\;\textup{UNIFORM-WEIGHT});
    84	\]
    85	at genus $g \geq 2$ for multi-weight algebras the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (ALL-WEIGHT, with cross-channel correction $\delta F_g^{\mathrm{cross}}$).
    86	\end{proposition}
    87	
    88	\begin{proof}
    89	The free-field argument: the generating space of $A_\cC$ is $\HH^{\bullet+1}(\cC)$, and $\kappa_{\mathrm{ch}}$ equals the supertrace of the identity on this generating space, which is $\chi^{\CY}(\cC) = \kappa_{\mathrm{cat}}(\cC)$. The quantization step in the construction of $\Phi$ (CY-A, Step~4) preserves $\kappa_{\mathrm{ch}}$ at $d = 2$: the holomorphic anomaly cancellation at $d = 2$ (Serre duality $\mathbb{S}_\cC \simeq [2]$) guarantees that no quantum correction shifts the supertrace. The genus-$g$ obstruction formula is Vol~I Theorem~D applied to $A_\cC$; the substitution $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{cat}}$ follows from the first part.
thinking
**Inspecting inconsistencies**

I’m noticing that the preface of Volume II matches the canonical text, which is good! Now I need to find any inconsistencies in other parts. I see that a potential candidate could be in Volume III, specifically around line 20 of the frame or preface. I’ll have to inspect that closely to ensure everything aligns properly. It’s important to maintain consistency throughout!
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex | sed -n '18,32p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '101,151p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex | sed -n '96,116p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    18	the input.
    19	
    20	A terminological point: ``Hochschild'' in this volume means
    21	categorical Hochschild cohomology: the cyclic bar complex
    22	$\mathrm{CC}_*(\cC)$ of a dg or $\Ainf$-category, topological
    23	in nature. The chiral upgrade $\mathrm{ChirHoch}^*(A)$ of
    24	Volume~I (Theorem~H) is the holomorphic version; it is the
    25	output of the functor $\Phi$, not the input. The two are
    26	related by the functor itself: $\Phi$ sends $\mathrm{CC}_*(\cC)$
    27	to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
    28	data to holomorphic chiral data on the curve.
    29	
    30	The construction is a functor
    31	\[
    32	 \Phi \colon \CY_d\text{-}\Cat \longrightarrow
 succeeded in 51ms:
   101	\index{Hochschild cohomology!three theories}%
   102	\index{chiral Hochschild cohomology!distinguished from topological and categorical}%
   103	Three distinct Hochschild theories appear in this programme.
   104	They differ in input, output, and geometric origin;
   105	conflating them is a category error.
   106	
   107	\begin{enumerate}[label=\textup{(\roman*)}]
   108	\item \emph{Topological Hochschild cohomology} $\HH^*(A, A)$.
   109	 Input: an $E_1$-algebra~$A$ (associative up to homotopy).
   110	 Output: an $E_2$-algebra (Deligne conjecture, proved by
   111	 many authors). Geometric origin: the real line~$\bR$
   112	 and its interval compactifications.
   113	 This is the classical theory of deformation complexes.
   114	
   115	\item \emph{Chiral Hochschild cohomology}
   116	 $\ChirHoch^*(\cA) = \ChirHoch^*(\cA, \cA)$.
   117	 Input: a chiral algebra~$\cA$ on a smooth curve~$X$
   118	 (equivalently, a vertex algebra on the formal disk~$D$).
   119	 Output: a graded vertex algebra, concentrated in
   120	 cohomological degrees $\{0, 1, 2\}$ for
 succeeded in 51ms:
    96	    C^{\mathrm{top}}(S^1,\cA)
    97	  \end{equation}
    98	  that is a quasi-isomorphism of chain complexes.
    99	  In particular, both models compute the same homology:
   100	  \[
   101	    H_\bullet\bigl(C^{\mathrm{ch}}(D^\times,\cA)\bigr)
   102	    \;\cong\;
   103	    H_\bullet\bigl(C^{\mathrm{top}}(S^1,\cA)\bigr)
   104	    \;\cong\;
   105	    Z(\cA),
   106	  \]
   107	  the derived center (chiral Hochschild homology)
   108	  of~$\cA$. This is the chain-level content of the
   109	  state--field correspondence.
   110	
   111	\item \textbf{$E_1$-compatibility, $E_2$-incompatibility.}
   112	  The map~$\rho$ is an $E_1$-algebra map but \emph{not}
   113	  an $E_2$-algebra map: the target carries only an
   114	  $E_1$-structure.
   115	  The discrepancy---the fiber of the forgetful functor
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4900,4925p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item In the Cartan sector ($\alpha = 0$), the $\Eone$ and $\Einf$
 Hochschild cohomologies are isomorphic
 (the Cartan generators are $\Einf$ regardless of the cocycle).
\item In non-zero sectors ($\alpha \neq 0$), the cocycle braiding
 $c_{N,q}(\alpha_i, \alpha_j) =
 (-1)^{\langle\alpha_i,\alpha_j\rangle} \zeta_N^{2q(\alpha_i,\alpha_j)}$
 introduces phase twists in the Hochschild differential, changing
 cohomology dimensions relative to the $\Einf$ case.
\item The $N$-torsion of the braiding creates $\bZ/N\bZ$ periodicity
 in the sector-by-sector Hochschild computation: sectors
 $\alpha$ and $\alpha + N\beta$ have isomorphic Hochschild
 contributions.
\end{enumerate}
\emph{Evidence.}
Part (i) follows from the lattice grading. Part (ii) follows from
Theorem~\ref{thm:lattice:curvature-braiding-orthogonal}: the Cartan
sector is $\Einf$. Part (iii) is the $\Eone$ content: the ordering
cycles in the bar complex (which control Hochschild via bar-cobar)
carry the cocycle phases. Part (iv) is structural (the braiding
matrix has $N$-torsion by Theorem~\ref{thm:quantum-lattice-structure}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild polynomial" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface_sections10_13_draft.tex:137:Lagrangian family over the Hodge bundle; and the Hochschild polynomial
chapters/frame/preface_sections5_9_draft.tex:919:Hochschild polynomial growth $\to$ Koszul-complex acyclicity,
chapters/frame/preface_section1_v2.tex:518:the chiral Hochschild polynomial growth (Theorem~H) are all
chapters/connections/concordance.tex:3217:bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
chapters/frame/preface.tex:3397:Hochschild polynomial growth $\to$ Koszul-complex acyclicity,
chapters/frame/preface.tex:3870:Lagrangian family over the Hodge bundle; and the Hochschild polynomial
chapters/theory/fourier_seed.tex:973:(\S\ref{sec:fourier-specialization}), and the Hochschild polynomial
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3385,3405p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
algebras: the Virasoro algebra has $r_{\max}=\infty$ yet
satisfies item~(iii). Shadow depth classifies complexity
\emph{within} the Koszul world, not Koszulness itself.

\medskip
\noindent\textbf{The proof circuit.}\enspace
The core equivalence chain is
$\textup{(i)} \Leftrightarrow \textup{(ii)}
\Leftrightarrow \textup{(iii)}
\Leftrightarrow \textup{(v)}
\Leftrightarrow \textup{(viii)}$,
proved by PBW concentration $\to$ bar-cobar inversion $\to$
Hochschild polynomial growth $\to$ Koszul-complex acyclicity,
with the $A_\infty$-formality branch via HPL transfer and Keller
classicality. From this core: (iv) by Ext spectral sequence,
(vi) by conservativity + log-FM totalization,
(vii) by the identification $\barB = \int_X$,
(ix) by non-degeneracy forcing PBW injectivity,
(x) by stratum-by-stratum PBW concentration.
The Lagrangian criterion~(xi) uses PTVV derived intersection

thinking
**Identifying candidate conflations in Hochschild references**

I’m gathering specific file and line references where the mention of Hochschild invariants might blur the distinctions among topological Hochschild cohomology, chiral Hochschild cohomology, and categorical Hochschild homology/cohomology. These examples highlight potential confusion due to general terms or bridging statements that don’t clearly separate the concepts, aiming to provide the user with precise candidates and succinct reasons for possible conflations.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3205,3235p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Two further characterizations, tropical Koszulness
(Theorem~\ref{thm:tropical-koszulness}) and
bifunctor obstruction decomposition
(Theorem~\ref{thm:bifunctor-obstruction-decomposition}),
are proved separately but are not among the twelve numbered
conditions.

\smallskip\noindent
\emph{Proof circuit.}
The core cycle
(\ref{item:kp-def})$\Leftrightarrow$(\ref{item:kp-pbw})$\Leftrightarrow$(\ref{item:kp-ainfty})$\Leftrightarrow$(\ref{item:kp-barcobar})$\Leftrightarrow$(\ref{item:kp-hochschild})
is proved by PBW concentration~$\to$
bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
Koszul-complex acyclicity, with $A_\infty$ formality equivalent
to PBW via Keller classicality. From this core,
Ext diagonal vanishing~(\ref{item:kp-ext}) follows by bigrading
constraints,
Barr--Beck--Lurie~(\ref{item:kp-barrbeck}) by conservativity +
monadic descent (\cite[Prop.~4.7.3.16]{HA}),
FH concentration~(\ref{item:kp-facthom}) via bar = FH,
codex
- `chapters/frame/preface.tex:20-28` – “Hochschild” is introduced as the categorical/topological invariant and immediately described as “lifting topological Hochschild data to holomorphic chiral data,” which could leave readers unsure whether the categorical Hochschild cohomology and the chiral output are distinct invariants or just rebranded versions of the same thing.  
- `chapters/frame/preface.tex:45-48` – the sentence that “the $\mathbb{S}^2$-action on Hochschild homology gives an $\Etwo$-chiral algebra” arguably treats categorical Hochschild homology as if it already is the chiral algebra, potentially conflating the topological and chiral Hochschild stories.  
- `chapters/connections/bar_cobar_bridge.tex:219-224` – Theorem H says the “CY Hochschild calculus” is “faithfully reflected in $\ChirHoch^*(A_\cC)$,” which reads like an identification of categorical Hochschild cohomology with chiral Hochschild cohomology rather than a functorial relationship, blurring the distinction between the two.  
- `chapters/connections/bar_cobar_bridge.tex:235-236` – the claim that “the shadow depth class, Hochschild data, and BKM structure vary” bundles an unspecified “Hochschild data” together with BKM structure, leaving unclear whether one means categorical/cohomology data, chiral Hochschild invariants, or some averaged/topological hybrid, so it’s a natural spot to re-check for conflation.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '760,790p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
genus-refined specialization of the binary collision residue
$\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = r(z)$
(equation~\eqref{eq:collision-residue-identification}).

\subsubsection{The holographic/Koszul dictionary}

\begin{proposition}[Bulk from boundary; \ClaimStatusProvedElsewhere{} \cite{BD04,FG12,CG17}]
\label{prop:bulk-from-boundary}
\index{bulk-boundary correspondence!derived center}
Let $\cA_\partial$ be a boundary chiral algebra and $\cA_{\mathrm{bulk}}$
the associated bulk theory. Then
\begin{equation}\label{eq:bulk-derived-center}
 \cA_{\mathrm{bulk}}
 \;\simeq\;
 Z_{\mathrm{der}}(\cA_\partial),
\end{equation}
where $Z_{\mathrm{der}}$ denotes the derived center (Hochschild
cohomology of the chiral category). The bulk is the derived center
of the boundary.
\end{proposition}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar.*Hochschild" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/hochschild_cohomology.tex:1709:The theoretical arc of Part~\ref{part:bar-complex} is now complete. Algebraic foundations (\S\ref{ch:algebraic-foundations}) supplied the operadic language; configuration spaces (\S\ref{chap:config-spaces}) gave it geometric content; the bar-cobar adjunction (Theorem~A) and the Verdier intertwining $D_{\mathrm{Ran}}(B(\cA)) \simeq B(\cA^!)$ established duality on the Ran space; and the higher-genus theory assembled the proved scalar package~$\kappa(\cA)$, the proved spectral package~$(\Delta_{\cA},\Pi_{\cA})$, and the bar-intrinsic Maurer--Cartan element~$\Theta_{\cA}$. The three main theorems (adjunction~(A), inversion on the Koszul locus~(B), and Lagrangian complementarity~(C)) are projections of a single structure: the modular Koszul object associated to a factorization algebra on curves. Chiral Hochschild cohomology, developed in this chapter, is the infinitesimal invariant of that structure: concentrated in degrees $\{0,1,2\}$ for Koszul algebras (Theorem~H), it classifies deformations, detects obstructions, and exchanges under Koszul duality via the Connes operator.
chapters/theory/chiral_hochschild_koszul.tex:4603:The bar-cobar approach computes Hochschild cohomology via the quasi-isomorphism
chapters/theory/chiral_hochschild_koszul.tex:5023:The bar-cobar approach to Hochschild cohomology provides explicit formulas
chapters/theory/chiral_koszul_pairs.tex:2119:bar-cobar resolution with the chiral Hochschild complex. On the
chapters/connections/concordance.tex:3217:bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4585,4625p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This conjecture lies outside the present monograph: it is a physical
interpretation, not a theorem. A precise formulation would require
specifying the bulk as a factorization algebra on a $3$-manifold with
boundary (Costello--Li). The relation $c_{\text{bulk}} +
c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
\end{remark}

Three pieces of evidence: the central charges satisfy
$c_{\mathrm{bulk}} + c_{\mathrm{boundary}} = 26$, the Hochschild
cohomologies are Koszul dual, and the twisting morphism exhibits
the formal pattern of the conjectural holographic dictionary.

\section{Computing Hochschild cohomology via bar-cobar resolution}
\label{sec:hochschild-via-bar-cobar-complete}

\subsection{The bar-cobar resolution strategy}

The bar-cobar approach computes Hochschild cohomology via the quasi-isomorphism
$\ChirHoch^n(\mathcal{A}) = H^n\bigl(\mathrm{Hom}_{\mathsf{Alg}}(\Omega(\bar{B}(\mathcal{A})),

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Categorical Hochschild" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:126:\item \emph{Categorical Hochschild homology}
chapters/theory/introduction.tex:710:\emph{Categorical Hochschild} $\mathrm{HH}^*(\mathrm{Rep}(\cA))$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '690,730p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 of quantizations and the passage from Poisson to chiral
 (Chapter~\ref{chap:deformation-theory}).
 The primitive step is a descent lemma (Lemma~\ref{lem:chirhoch-descent}): on the Koszul locus, $\ChirHoch^*(\cA) \cong (\mathbb{D}_{\operatorname{Ran}} \barB(\cA))_{\Sigma}$, reducing Theorem~H to Theorem~A's Verdier intertwining.
\end{itemize}

\begin{warning}[Three Hochschild theories]
\label{warn:three-hochschild-intro}
\index{Hochschild cohomology!three variants}%
Three inequivalent notions of ``Hochschild cohomology'' coexist
in this programme; conflating them is a persistent source of
error.
\emph{Chiral Hochschild} $\ChirHoch^*(\cA) =
H^*(\operatorname{CoDer}(\barB(\cA)))$ is the cohomology of
coderivations of the bar coalgebra; it lives on the
curve~$X$ and has cohomological amplitude~$[0,2]$ on the
Koszul locus (Theorem~H).
\emph{Topological Hochschild} $\mathrm{HH}^*_{\mathrm{top}}$
is the factorization homology on the circle $S^1$; it lives
in dimension~$1$ higher and governs the $\Eone$-chiral bar of
Volume~II.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '60,90p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \ref{thm:virasoro-hochschild},
 \ref{thm:critical-level-cohomology}\textup{)}
 & \ClaimStatusProvedHere
\end{tabular}
\end{center}

\noindent
The unifying principle: the modular $L_\infty$ convolution algebra
$\mathfrak{g}^{\mathrm{mod}}_\cA$ carries a natural modular $L_\infty$
structure from the Feynman transform of the modular operad. The dg~Lie
algebra of Definition~\ref{def:modular-convolution-dg-lie} is its strict
model $\Convstr$; the homotopy-invariant object is $\Definfmod(\cA)$
(Theorem~\ref{thm:modular-homotopy-convolution}). The universal MC element
$\Theta_\cA \in \MC(\gAmod)$ exists unconditionally by the bar-intrinsic
construction (Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
is MC because $D_\cA^2 = 0$). The shadow obstruction tower
$\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
\to \cdots$ consists of its finite-order projections.
Theorems~A--C read off theorem-level consequences of the full MC
package carried by $\Theta_\cA$; Theorems~D and~H are scalar and

thinking
**Evaluating categorical invariants**

I'm wrestling with how to describe categorical HH as "the topological invariant of C as a dg category." It feels a bit sloppy, but perhaps it's adequate. Since I'm reporting the whole section, maybe I shouldn't break it up. I want to pinpoint other files in volumes I and II that genuinely conflate concepts. I should search `genus_complete.tex:776`, where Z_der indicates the derived center. It's essential to consider all findings without forcing each one into a specific volume.
thinking
**Inspecting categorical concepts**

Okay, line 816 mentions that the derived center of the module category is about chiral Hochschild cochains of A^!_line. I’m thinking that this might mix up the ideas of categorical center and chiral cochains without proper distinction. I really need to look more closely at this. Since we're dealing with a module category over line algebra, it could have topological or categorical implications. Let's dig deeper into those concepts!
codex
I’ve confirmed one hard failure in Vol III and one candidate in Vol II. The Vol III bridge section really does replace the canonical `topological / chiral / categorical` split with `categorical / chiral / derived center`, and Vol II has at least one sentence equating the derived center with “chiral Hochschild homology,” which is a different object again.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex | sed -n '808,876p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex | sed -n '2320,2376p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/brace.tex | sed -n '131,178p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   808	\;\simeq\;
   809	\Zder(\cC_{\mathrm{line}})
   810	\;\simeq\;
   811	\HH^\bullet_{\mathrm{ch}}(\cA^!_{\mathrm{line}}).
   812	\]
   813	\end{proposition}
   814	
   815	\begin{proof}
   816	The first equivalence is hypothesis (iii). Since $M_b$ is a compact generator, $\cC_{\mathrm{line}}$ is derived Morita equivalent to $B_b\text{-mod}$. Derived centers are Morita invariant, giving $\Zder(B_b)\simeq \Zder(\cC_{\mathrm{line}})$. Hypothesis (iv) identifies $\cC_{\mathrm{line}}$ with $\cA^!_{\mathrm{line}}\text{-mod}$, and the derived center of the module category is chiral Hochschild cochains of $\cA^!_{\mathrm{line}}$.
   817	\end{proof}
   818	
   819	\subsection{What is new in this manuscript}
   820	
   821	The novelty of this note lies elsewhere: it strengthens the microlocal algebraic core. We prove, inside a large but exact local sector, that the boundary, line, and bulk vertices can each be constructed explicitly and compared by theorems rather than analogies.
   822	
   823	\begin{center}
   824	\renewcommand{\arraystretch}{1.2}
   825	\begin{longtable}{|p{0.24\textwidth}|p{0.23\textwidth}|p{0.43\textwidth}|}
   826	\hline
   827	\textbf{Layer} & \textbf{Status} & \textbf{Content} \\
 succeeded in 51ms:
   131	\subsection{Bulk observables \texorpdfstring{$\simeq$}{≃} chiral Hochschild cochains}
   132	\label{subsec:bulk-equals-CHC-brace}
   133	Let $\mathsf{Obs}$ be the BV observable prefactorization algebra of the HT theory, and $A=\mathsf{Obs}(D\times I)$ the local complex on a small rectangle.
   134	
   135	\begin{theorem}[Bulk–cochains identification; \ClaimStatusProvedHere]
   136	\label{thm:bulk-CHC-brace}
   137	Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra.
   138	There is a canonical filtered quasi‑isomorphism
   139	\[
   140	\mathrm{C}^\bullet_{\mathrm{ch,top}}(A)\;\simeq\;\mathsf{Obs}_{\mathrm{bulk}}(\mathbb{B}^3)
   141	\]
   142	between chiral Hochschild cochains of the local algebra $A$ and the complex of bulk local observables supported in a small $3$–ball, with filtration by holomorphic weight. On associated graded, this identification reduces to the BD‑chiral Hochschild complex on the closed color tensored with the $E_1$ Hochschild complex on the open color.
   143	\end{theorem}
   144	
   145	\begin{proof}
   146	The argument has three steps: operad-of-shapes recognition providing a common model, filtration analysis via holomorphic weight, and integrability from the logarithmic $\SCchtop$ structure.
   147	
   148	\medskip
   149	\textbf{Step 1: Operad-of-shapes recognition.}
   150	
 succeeded in 51ms:
  2320	\textup{(E)} is the $\cD$-module realization of~\textup{(B)}.
  2321	The relationship of~\textup{(D)} to the others is an open
  2322	problem connected to the higher-categorical structure of the
  2323	$\Eone$-chiral world.
  2324	
  2325	Each notion admits its own derived center construction, and the
  2326	output operad depends on which construction is used
  2327	(Remark~\ref{rem:ordered-ch-hom-bar}).
  2328	\end{warning}
  2329	
  2330	\begin{principle}[Geometric origin of Hochschild variants]
  2331	\label{princ:geometric-origin-hochschild}
  2332	\index{Hochschild theory!geometric origin}
  2333	The geometry of the base space determines the Hochschild theory.
  2334	Five cases exhaust the standard constructions:
  2335	\begin{enumerate}[label=\textup{(\roman*)}]
  2336	\item \emph{Factorisation algebra on a curve~$X$.}
  2337	  Input: chiral algebra~$\cA$ on~$X$.
  2338	  Configuration complex: $\operatorname{FM}_k(X)$
  2339	  (Fulton--MacPherson compactification, holomorphic).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/frame/preface.tex | sed -n '3735,3745p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3735	$(\mathrm{ChirAss})^!$: its differential extracts OPE residues from
  3736	collisions in the holomorphic plane, and its deconcatenation coproduct
  3737	is the cofree coassociative structure on the desuspended augmentation
  3738	ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
  3739	pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$, not the bar
  3740	complex itself: the two-colour open/closed structure emerges when the
  3741	bar complex is fed into the Hochschild construction.
  3742	
  3743	The primitive object of three-dimensional holomorphic-topological
  3744	quantum field theory on $\mathbb C_z \times \mathbb R_t$ is the
  3745	open/closed factorization dg-category~$\mathcal C$ on the bordified
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/lattice_foundations.tex | sed -n '4905,4925p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4905	 (-1)^{\langle\alpha_i,\alpha_j\rangle} \zeta_N^{2q(\alpha_i,\alpha_j)}$
  4906	 introduces phase twists in the Hochschild differential, changing
  4907	 cohomology dimensions relative to the $\Einf$ case.
  4908	\item The $N$-torsion of the braiding creates $\bZ/N\bZ$ periodicity
  4909	 in the sector-by-sector Hochschild computation: sectors
  4910	 $\alpha$ and $\alpha + N\beta$ have isomorphic Hochschild
  4911	 contributions.
  4912	\end{enumerate}
  4913	\emph{Evidence.}
  4914	Part (i) follows from the lattice grading. Part (ii) follows from
  4915	Theorem~\ref{thm:lattice:curvature-braiding-orthogonal}: the Cartan
  4916	sector is $\Einf$. Part (iii) is the $\Eone$ content: the ordering
  4917	cycles in the bar complex (which control Hochschild via bar-cobar)
  4918	carry the cocycle phases. Part (iv) is structural (the braiding
  4919	matrix has $N$-torsion by Theorem~\ref{thm:quantum-lattice-structure}).
  4920	\end{conjecture}
  4921	
  4922	
  4923	%% ================================================================
  4924	\section{Lattice shadow obstruction tower: integrable spin chains and the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/concordance.tex | sed -n '3208,3225p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3208	(Theorem~\ref{thm:bifunctor-obstruction-decomposition}),
  3209	are proved separately but are not among the twelve numbered
  3210	conditions.
  3211	
  3212	\smallskip\noindent
  3213	\emph{Proof circuit.}
  3214	The core cycle
  3215	(\ref{item:kp-def})$\Leftrightarrow$(\ref{item:kp-pbw})$\Leftrightarrow$(\ref{item:kp-ainfty})$\Leftrightarrow$(\ref{item:kp-barcobar})$\Leftrightarrow$(\ref{item:kp-hochschild})
  3216	is proved by PBW concentration~$\to$
  3217	bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
  3218	Koszul-complex acyclicity, with $A_\infty$ formality equivalent
  3219	to PBW via Keller classicality. From this core,
  3220	Ext diagonal vanishing~(\ref{item:kp-ext}) follows by bigrading
  3221	constraints,
  3222	Barr--Beck--Lurie~(\ref{item:kp-barrbeck}) by conservativity +
  3223	monadic descent (\cite[Prop.~4.7.3.16]{HA}),
  3224	FH concentration~(\ref{item:kp-facthom}) via bar = FH,
  3225	Kac--Shapovalov~(\ref{item:kp-nullvec}) via Shapovalov
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/outlook.tex | sed -n '70,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    70	algebra of Definition~\ref{def:modular-convolution-dg-lie} is its strict
    71	model $\Convstr$; the homotopy-invariant object is $\Definfmod(\cA)$
    72	(Theorem~\ref{thm:modular-homotopy-convolution}). The universal MC element
    73	$\Theta_\cA \in \MC(\gAmod)$ exists unconditionally by the bar-intrinsic
    74	construction (Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
    75	is MC because $D_\cA^2 = 0$). The shadow obstruction tower
    76	$\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
    77	\to \cdots$ consists of its finite-order projections.
    78	Theorems~A--C read off theorem-level consequences of the full MC
    79	package carried by $\Theta_\cA$; Theorems~D and~H are scalar and
    80	Hochschild outputs.
    81	
    82	% ======================================================================
    83	
    84	\section{Three-pillar foundational architecture}
    85	\label{sec:outlook-three-pillars}
    86	\index{three-pillar architecture|textbf}
    87	\index{homotopy chiral algebra!foundational role}
    88	\index{convolution!sL-infinity@$sL_\infty$-algebra!foundational role}
    89	\index{logarithmic Fulton--MacPherson!foundational role}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/frame/preface.tex | sed -n '3860,3885p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3860	Volume~II identifies the geometric substrate of the bar construction:
  3861	the bar complex is the structure sheaf of the Lagrangian
  3862	self-intersection
  3863	$\mathfrak{S}=\mathcal{L}\times_{\mathcal{M}}\mathcal{L}$
  3864	in a $(-2)$-shifted symplectic stack. The bar-cobar adjunction
  3865	(Theorem~A) is the groupoid comodule-module adjunction for~$\mathfrak{S}$;
  3866	Koszul inversion (Theorem~B) reconstructs the Lagrangian from its clean
  3867	self-intersection; complementarity (Theorem~C) is two Lagrangians whose
  3868	intersection carries a $(-1)$-shifted symplectic structure; the modular
  3869	characteristic (Theorem~D) is the Kodaira--Spencer class of the
  3870	Lagrangian family over the Hodge bundle; and the Hochschild polynomial
  3871	growth (Theorem~H) is the HKR theorem for the Lagrangian embedding.
  3872	
  3873	At genus $g\ge 1$ the bar complex acquires curvature:
  3874	$d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g$. The curvature lives
  3875	entirely in the holomorphic direction; the topological $E_1$-structure
  3876	on~$\mathbb R$ sees no curvature (the interval has no nontrivial
  3877	topology). The total corrected differential
  3878	$D_g=d_{\mathrm{fib}}+\nabla^{\mathrm{GM}}_g$ restores flatness over
  3879	$\overline{\cM}_g$: the Gauss--Manin connection absorbs the

thinking
**Summarizing candidate references for Hochschild usage**

I'm putting together a clear bullet list of lines where “Hochschild” is mentioned without clarifying whether it’s chiral, topological, or categorical, emphasizing the risk of confusion and including precise reasons referencing bar complexes, derived centers, and Koszul duality when relevant. I want to ensure each candidate includes a brief explanation of why the missing qualifier could lead to ambiguity about the Hochschild type involved.
codex
- `chapters/frame/preface.tex:3741` — in the Swiss-cheese/derived-center discussion the “bar complex is fed into the Hochschild construction” with no adjective, which readers could easily misread as referring to the topological or categorical Hochschild theory rather than the chiral Hochschild complex tied to the derived center pair.  
- `chapters/examples/lattice_foundations.tex:4917` — the argument that “cycles in the bar complex … control Hochschild via bar-cobar” uses bare “Hochschild,” so it’s unclear whether this is the chiral Hochschild theory on the curve or the topological/categorical version, risking conflation of different Hochschild avatars in the lattice-sector analysis.  
- `chapters/connections/concordance.tex:3217` — the proof circuit steps note “Hochschild polynomial growth” without specifying which Hochschild theory is meant, yet that growth behaves very differently for the chiral versus topological or categorical variants, so the current wording invites misinterpretation of which theory powers the Koszul argument.  
- `chapters/connections/outlook.tex:80` — stating that “Theorems D and H are scalar and Hochschild outputs” without qualifying “Hochschild” leaves open whether the reference is to the chiral Hochschild complex (Theorem H) or some other Hochschild theory, obscuring the intended distinction between the three Hochschild flavours.  
- `chapters/frame/preface.tex:3870` — the description “the Hochschild polynomial growth (Theorem H) is the HKR theorem for the Lagrangian embedding” names Hochschild without tagging it as chiral, so readers might mistake it for the topological or categorical Hochschild growth statements discussed elsewhere in the programme.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '1234,1316p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '4386,4510p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'derived center.*Hochschild homology|Hochschild homology.*derived center|chiral Hochschild homology' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1234	 The Koszul involution exchanges Neumann~$\leftrightarrow$~Dirichlet
  1235	 boundary conditions.
  1236	
  1237	\item \textbf{Derived center \textup{(}universal bulk\textup{)}.}
  1238	 $\Zder^{\mathrm{ch}}(\cA_\partial)
  1239	 = C^\bullet_{\mathrm{ch}}(V_k(\fg),\, V_k(\fg))$.
  1240	 The bulk observables are chiral Hochschild cochains of the boundary
  1241	 algebra, not the bar complex.
  1242	
  1243	\item \textbf{Collision residue.}
  1244	 $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
  1245	 equation. The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
  1246	
  1247	\item \textbf{Modular MC element.}
  1248	 $\Theta_\cA = D_\cA - d_0 \in \MC(\gAmod)$, with modular
  1249	 characteristic $\kappa = \kappa(V_k(\fg))
  1250	 = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$ and complementarity
  1251	 $\kappa(\cA_\partial) + \kappa(\cA_\partial^!) = 0$
  1252	 \textup{(}since $\cA^! = V_{-k-2h^\vee}(\fg)$ has
  1253	 $\kappa(\cA^!) = -\dim(\fg)\cdot(k+h^\vee)/(2h^\vee)$, by the
 succeeded in 51ms:
  4386	points.
  4387	
  4388	\smallskip
  4389	\noindent
  4390	\emph{(5) Hochschild homology $\HH_0^{\mathrm{ch}}(\cH_k)$:
  4391	the character space.}
  4392	The zeroth Hochschild homology is
  4393	\begin{equation}\label{eq:heisenberg-HH0}
  4394	\HH_0^{\mathrm{ch}}(\cH_k)
  4395	\;=\;
  4396	H_0\bigl(B^{\mathrm{ann}}_\bullet(\cH_k)\bigr)
  4397	\;\cong\;
  4398	\cH_k / [\cH_k, \cH_k]_{\mathrm{ch}},
  4399	\end{equation}
  4400	the quotient of $\cH_k$ by chiral commutators.
  4401	For the Heisenberg algebra, the chiral commutator
  4402	$[J,J]_{\mathrm{ch}} = J_{(0)}J = 0$ vanishes
  4403	(no simple pole), so every element is a class:
  4404	\[
  4405	\HH_0^{\mathrm{ch}}(\cH_k)
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5196:The zeroth chiral Hochschild homology is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1213:chiral Hochschild homology, realising the genus-$1$ ordered sector
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:107:  the derived center (chiral Hochschild homology)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:2395:\begin{theorem}[Annular bar computes chiral Hochschild homology;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:4895:computes chiral Hochschild homology
/Users/raeez/chiral-bar-cobar/chapters/theory/spectral_sequences.tex:391:\item $E_1^{0,n}$ is the genus-0 bar homology (classical chiral Hochschild homology).
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:553:\begin{definition}[Chiral Hochschild homology]
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:555:The \emph{chiral Hochschild homology} of $\mathcal{A}$ is:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4779:\begin{theorem}[Annular bar complex computes chiral Hochschild homology;
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4848: sector, computing chiral Hochschild homology.
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:9711:Item~(4), annular closure computing chiral Hochschild homology,
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:10867:\item Annular bar complex computes chiral Hochschild homology:
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex | sed -n '2584,2600p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '1488,1505p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex | sed -n '20,29p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2584	because $h^{0,1}(K3) = 0$. For algebraic K3 with Picard rank
  2585	$\rho \geq 1$, the transcendental Brauer rank drops to $22 - \rho$.
  2586	
  2587	\begin{remark}[Chiral Hochschild comparison]
  2588	\label{rem:k3e-chiral-hochschild}
  2589	\index{chiral Hochschild cohomology!K3 x E@$K3 \times E$}
  2590	By the Costello--Gwilliam theorem for holomorphic field theories,
  2591	$\operatorname{ChirHoch}^n(\cA_X) \cong \HH^n(X)$ for the
  2592	chiral de Rham complex $\cA_X = \Omega^{\mathrm{ch}}(X)$
  2593	of a CY manifold $X$. In particular,
  2594	$\dim \operatorname{ChirHoch}^2(\Omega^{\mathrm{ch}}(K3 \times E)) = 23$:
  2595	the chiral algebra \emph{sees} the full CY$_3$ deformation space,
  2596	including the noncommutative directions. The full Hochschild
  2597	diamond is
  2598	\begin{equation}\label{eq:k3e-hh-full}
  2599	(\HH^0, \HH^1, \HH^2, \HH^3, \HH^4, \HH^5, \HH^6)
  2600	= (1, 2, 23, 44, 23, 2, 1),
 succeeded in 51ms:
    20	A terminological point: ``Hochschild'' in this volume means
    21	categorical Hochschild cohomology: the cyclic bar complex
    22	$\mathrm{CC}_*(\cC)$ of a dg or $\Ainf$-category, topological
    23	in nature. The chiral upgrade $\mathrm{ChirHoch}^*(A)$ of
    24	Volume~I (Theorem~H) is the holomorphic version; it is the
    25	output of the functor $\Phi$, not the input. The two are
    26	related by the functor itself: $\Phi$ sends $\mathrm{CC}_*(\cC)$
    27	to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
    28	data to holomorphic chiral data on the curve.
    29	
 succeeded in 51ms:
  1488	The anomaly class $\Theta$ lives in $Z^2(B)\cap Z(B)$ and descends,
  1489	under the boundary reconstruction
  1490	(Proposition~\ref{prop:tholog-boundary-reconstruction}), to a
  1491	Hochschild class
  1492	\[
  1493	\Theta_\partial
  1494	\;=\;
  1495	\beta_{\mathrm{der}}(\Theta)
  1496	\;\in\;
  1497	HH^2(V_k(\mathfrak{sl}_2)).
  1498	\]
  1499	The Hochschild cohomology $HH^2(V_k(\mathfrak{sl}_2))$ controls
  1500	deformations of the VOA structure. The class $\Theta_\partial$ is
  1501	the genus-$1$ curvature obstruction, and its image under the
  1502	bulk--boundary quasi-isomorphism
  1503	$B\simeq HH^\bullet(V_k(\mathfrak{sl}_2))$ recovers~$\Theta$.
  1504	
  1505	The key identification is that $\Theta_\partial$ is \emph{not}

thinking
**Evaluating anomalies in Vol II**

I'm looking at an interesting anomaly in Vol II regarding `HH^2(V_k(sl2))` and `B\simeq HH^\bullet(V_k(sl2))`, which seems to lack qualifiers. The concordance states "Hochschild" only in a historical sense, hinting at some topological remarks. I suspect that the boundary VOA structure on V_k(sl2) relates to the chiral Hochschild cohomology of chiral algebra. This inconsistency caught my attention, and I need more context to see if it's related to a classical framework, possibly the bulk.
codex
A second Vol II failure surfaced: `anomaly_completed_frontier.tex` uses bare `HH^2(V_k(sl_2))` for VOA deformations and then writes a bulk-boundary quasi-isomorphism `B ≃ HH^\bullet(V_k(sl_2))` with no qualifier. In this repo’s own concordance, that surface must be qualified, and in this context it should be chiral Hochschild cochains/cohomology, not an untagged `HH`.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '1480,1508p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex | sed -n '1238,1252p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'HH\\"'^2'"\\(|HH\\\\bullet\\(|HH\\"'^'"\\\\bullet\\(|\\\\HH\\"'^'"\\{?2\\}?\\(' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1480	(\Bbbk\oplus\Bbbk\cdot\omega_3)[u]\big/([\Theta])
  1481	\]
  1482	when multiplication by $[\Theta]$ is injective on $H^\bullet(B)[u]$
  1483	(which holds for $k\neq -2$, since $\kappa = 3(k+2)/4\neq 0$).
  1484	
  1485	\medskip
  1486	\noindent\textbf{Step 5: the anomaly $2$-cocycle as a Hochschild
  1487	class.}
  1488	The anomaly class $\Theta$ lives in $Z^2(B)\cap Z(B)$ and descends,
  1489	under the boundary reconstruction
  1490	(Proposition~\ref{prop:tholog-boundary-reconstruction}), to a
  1491	Hochschild class
  1492	\[
  1493	\Theta_\partial
  1494	\;=\;
  1495	\beta_{\mathrm{der}}(\Theta)
  1496	\;\in\;
  1497	HH^2(V_k(\mathfrak{sl}_2)).
  1498	\]
  1499	The Hochschild cohomology $HH^2(V_k(\mathfrak{sl}_2))$ controls
 succeeded in 50ms:
  1238	\HH^\bullet(B_{L,W})
  1239	\simeq
  1240	\cO\bigl(T^*[-1]Z_F^{\der}\bigr)
  1241	\simeq
  1242	\cO\bigl(\dCrit(W)\bigr).
  1243	\]
  1244	In particular the derived center of the boundary algebra equals the bulk algebra in the boundary-linear sector.
  1245	\end{theorem}
  1246	
  1247	\begin{proof}
  1248	Because $B_{L,W}$ is a cofibrant completed commutative dg algebra, its derived center is modeled by Hochschild cochains. The algebra $B_{L,W} = (\widehat{\cO}(L) \otimes \Lambda(N), d\eta_a = F_a(x))$ is quasi-smooth: its cotangent complex $\mathbb{L}_{B/\kk}$ is concentrated in degrees $[0,1]$, where the degree-$0$ part is $\Omega^1_{B/\kk}$ (K\"ahler differentials of the underlying commutative algebra) and the degree-$1$ part is the normal bundle $N$. This two-term structure arises because $L$ is a smooth submanifold of the smooth ambient space $V = L \oplus N$, so the conormal sequence $0 \to N^\vee \to \Omega^1_V|_L \to \Omega^1_L \to 0$ yields a two-term cotangent complex; since both $L$ and $N$ are finitely generated free modules over the formal power series ring, this complex is perfect. The derived HKR isomorphism therefore applies (see Calaque--Van den Bergh \cite{CVdB10} for the dg setting, or \cite[Theorem~7.8.3.3]{Lur18} for the derived algebraic geometry framework), identifying Hochschild cochains with polyvector fields on the derived affine dg scheme $Z_F^{\der}$. Theorem~\ref{thm:dcrit-shiftedcot} identifies those polyvectors with functions on the bulk critical locus.
  1249	\end{proof}
  1250	
  1251	\subsection{The free polarization theorem as the zero superpotential case}
  1252	
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:373: $\HH^\bullet(\Fuk(X))$ with Gerstenhaber bracket produces a Lie
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:33:a non-degenerate pairing without any twist by $\omega_X$ (since $\omega_X \simeq \cO_X$). At the level of Hochschild cohomology, this induces a degree $(-d)$ symplectic pairing on $\HH^\bullet(\cC)$, the Mukai pairing (Caldararu 2003; Shklyarov 2013 for the dg-enhancement). The Mukai pairing is the B-side origin of the Ext-residue $R$-matrix: the classical $r$-matrix of the chiral algebra $\Phi(\cC)$ arises from the composition of Serre duality with the Grothendieck residue on $X$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:41: \HH^\bullet(D^b(\Coh(X))) \;\simeq\; \bigoplus_{p+q = \bullet} H^q\bigl(X, \Lambda^p T_X\bigr),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:48: \HH^\bullet(D^b(\Coh(X))) \;\simeq\; \bigoplus_{p+q = \bullet} H^q(X, \Omega^{d-p}_X).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:291: \item A map on cohomology $\HH^\bullet(\cC) \to \ChirHoch^*(A_\cC)$ that sends the Gerstenhaber bracket on $\HH^\bullet(\cC)$ to the convolution bracket on $\ChirHoch^*(A_\cC)$, and sends the Connes $B$-operator to the modular differential.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:292: \item A map $\HH^\bullet(\cC, \cC) \to \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ from the categorical Hochschild cochains (the endomorphism algebra of the identity bimodule) to the chiral derived center, compatible with the Gerstenhaber product on the source and the chiral bracket on the target.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:297:Part (i) is Proposition~\ref{prop:bar-dictionary}. For (ii): the Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a Lie bracket of degree $-1$. Under $\Phi$, this bracket becomes the convolution bracket of Vol~I by functoriality of the bar construction: the deconcatenation coproduct on $B(A_\cC)$ and the binary product of $A_\cC$ assemble into a bracket on $\Hom_{\Ran}(B(A_\cC), A_\cC)$, which restricts to $\ChirHoch^*(A_\cC)$ on the cohomology. The Connes operator $B$ on $\mathrm{CC}_\bullet(\cC)$ corresponds, under the bar dictionary, to the degree-preserving component of the bar differential (Proposition~\ref{prop:bar-dictionary}(ii)), which is the modular differential on the chiral side. For (iii): the categorical Hochschild cochains $\mathrm{CC}^\bullet(\cC, \cC)$ map to $\RHom(\Omega B(A_\cC), A_\cC)$ by applying $\Phi$ to each hom-space and using the bar-cobar quasi-isomorphism $\Omega B(A_\cC) \simeq A_\cC$ (Vol~I Theorem~B on the Koszul locus).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:302:The categorical Hochschild $\HH_\bullet(\cC)$ controls the deformation theory of $\cC$ as a CY category: $\HH^2(\cC)$ parametrizes first-order deformations, $\HH^1(\cC)$ the infinitesimal automorphisms. The chiral Hochschild $\ChirHoch^*(A_\cC)$ controls the shadow tower of $A_\cC$: the obstruction classes $\mathrm{obs}_g$ live in $\ChirHoch^2(A_\cC) \otimes H^\bullet(\overline{\cM}_{g,n})$. The derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ is the bulk algebra of the holographic datum: its elements are the operators that commute with all boundary insertions. Theorem~\ref{thm:hochschild-bridge} guarantees that the categorical deformation data of $\cC$ is faithfully transmitted, through $\Phi$, to the chiral obstruction data of $A_\cC$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:308:For $\cC$ a smooth proper CY$_3$ category, conditional on CY-A$_3$ (the conditionality propagates, AP-CY11), the maps (i)--(iii) of Theorem~\ref{thm:hochschild-bridge} extend to $d = 3$. The $(-1)$-shifted Poisson structure on $\HH^\bullet(\cC)$ (Pantev--To\"en--Vaqui\'e--Vezzosi) maps to the genus-$0$ contribution of the convolution bracket on $\ChirHoch^*(A_\cC)$; the genus-$g \geq 1$ components of the convolution bracket have no direct categorical-Hochschild source and arise from the curve geometry of $\Ran(X)$ through $\Phi$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:349:The boundary chiral algebra $A = V_k(\frakg)$ of 3d holomorphic CS on $C \times \R$ is $E_\infty$-chiral (commutative vertex algebra). By the higher Deligne conjecture (Lurie \cite{LurieHA}, Theorem~5.3.1.30), the Hochschild cochains $\HH^\bullet(A, A)$ of an $E_n$-algebra carry $E_{n+1}$ structure. For $A$ an $E_\infty$-algebra, $\HH^\bullet(A, A)$ carries $E_\infty$ structure; the specific $E_3$ subalgebra generated by the cup product, the Gerstenhaber bracket, and the BV operator (from the $S^1$-action on the cyclic bar complex) is the relevant one for the comparison with the topological $E_3$ below.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:119:= \HH^\bullet(A)$. The Ben-Zvi--Francis--Nadler theorem
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:259:duality $\HH^\bullet(\cC) \simeq \HH_{\bullet+d}(\cC)$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:261:$\HH^\bullet(\cC) \simeq \Zder(A)$ (Corollary~\ref{cor:zder-drinfeld})
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:318:categorical analogue replaces $\ChirHoch^*$ with $\HH^\bullet(\cC)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:331: \item $\HH^2(\cC)$ is the obstruction space for deformations.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:334:\HH^{p+q-1}$ on $\HH^\bullet(\cC)$ maps, under $\Phi$, to the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:133: \HH^\bullet(D^b(\mathrm{Coh}(X))) \;\cong\; H^\bullet(X, \wedge^\bullet T_X) \;\cong\; H^\bullet(X, \C),
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:137: \dim \HH^\bullet(K3) = 1 + 20 + 1 + 20 + 1 \;=\; \text{(degree-$0$: $1$, degree-$1$: $0$, degree-$2$: $22$, etc.)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:154: \HH^\bullet(Q) \cong H^\bullet(Q, \wedge^\bullet T_Q)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:180:The cyclic pairing of dimension $d = 2$ produces a degree-$(-2)$ symmetric form on the Hochschild complex; its top-degree component is a linear map $\HH^2(\cC) \to k$ whose dimension (as a quotient of $\HH^\bullet$) is $\chi(\cO_X)$ in the geometric case. The CY-to-chiral functor sends this trace to the invariant form on $A_\cC$, and the resulting $\kappa_{\mathrm{cat}}$ coincides (up to $\bS^2$-framing) with the coefficient of the $E_2$-algebra central extension. For K3 the computation reduces to $\chi(\cO_{\mathrm{K3}}) = 2$; see Chapter~\ref{ch:cy-to-chiral} Section~\ref{sec:cy-chiral-functor} and the compute module \texttt{cy\_to\_chiral\_functor.py} for the full verification.

thinking
**Exploring duplicates in findings**

I’m thinking about how to handle the same issue appearing across multiple files. I should check for duplicates or separate findings, especially between anomaly_completed_core and topological_holography. If they show the same lines, it might be a second-order propagation of the same bug. I need to report at least one and maybe mention both duplicates, listing two separate [HIGH] entries if they exist. I should verify the exact lines to be sure. Let's inspect!
codex
The Vol II ambiguity propagates: the same boundary-anomaly surface appears in multiple files, and some copies use raw `HH^\bullet(A_\partial)` exactly where the volume’s bulk theorem elsewhere uses chiral Hochschild cochains. I’m checking those duplicates now so I can separate one-off wording from repeated drift.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex | sed -n '1782,1801p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1782	\begin{remark}[Heuristic justification]
  1783	Part~(i): the chain of identifications is
  1784	\[
  1785	\kappa(\cA) \cdot \omega_g
  1786	\;\xmapsto{\text{Hochschild bridge}}\;
  1787	\Theta_{g,\partial} \in HH^2(A_\partial)
  1788	\;\xmapsto{A_\partial^! \simeq HH^\bullet(A_\partial)}\;
  1789	\Theta_g \in Z^2(A_\partial^!) \cap Z(A_\partial^!).
  1790	\]
  1791	The first arrow is
  1792	Theorem~\ref{thm:hochschild-bridge-higher-genus}(iii) (curvature
  1793	maps to cyclic obstruction). The second arrow is the
  1794	Koszul-locus identification of \(A_\partial^!\) with
  1795	\(HH^\bullet(A_\partial)\) (this is exactly
  1796	Proposition~\ref{prop:tholog-boundary-reconstruction},
  1797	transported across the quasi-isomorphism). Together, the
  1798	genus anomaly is determined entirely by boundary data.
  1799	
  1800	Part~(ii): the transgression algebra
  1801	\((A_\partial^!)_{\Theta_g}\) controls deformations of
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex | sed -n '1786,1803p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1786	\begin{remark}[Heuristic justification]
  1787	Part~(i): the chain of identifications is
  1788	\[
  1789	\kappa(\cA) \cdot \omega_g
  1790	\;\xmapsto{\text{Hochschild bridge}}\;
  1791	\Theta_{g,\partial} \in HH^2(A_\partial)
  1792	\;\xmapsto{A_\partial^! \simeq HH^\bullet(A_\partial)}\;
  1793	\Theta_g \in Z^2(A_\partial^!) \cap Z(A_\partial^!).
  1794	\]
  1795	The first arrow is
  1796	Theorem~\ref{thm:hochschild-bridge-higher-genus}(iii) (curvature
  1797	maps to cyclic obstruction). The second arrow is the
  1798	Koszul-locus identification of \(A_\partial^!\) with
  1799	\(HH^\bullet(A_\partial)\) (this is exactly
  1800	Proposition~\ref{prop:tholog-boundary-reconstruction},
  1801	transported across the quasi-isomorphism). Together, the
  1802	genus anomaly is determined entirely by boundary data.
  1803	
collab wait(call_RhOfdqQEA5QX39o1yjrX0t7X)
  receivers: 019d8627-bdaf-73c2-b415-368ae82f2046, 019d8627-bdc5-7bc1-aaa5-b47861c4a7f7, 019d8627-bdcb-7e83-b638-1d4b78c52308
wait(call_RhOfdqQEA5QX39o1yjrX0t7X) 3 agents complete:
  019d8627-bdaf-73c2-b415-368ae82f2046 completed: "- `chapters/frame/preface.tex:3741` — in the Swiss-cheese/derived-center discussion the “bar complex is fed into the Hoc…"
  019d8627-bdc5-7bc1-aaa5-b47861c4a7f7 completed: "- `chapters/connections/ht_bulk_boundary_line_frontier.tex:84` — the derived-center bullet simply says “bulk should be r…"
  019d8627-bdcb-7e83-b638-1d4b78c52308 completed: "- `chapters/frame/preface.tex:20-28` – “Hochschild” is introduced as the categorical/topological invariant and immediate…"

thinking
**Examining findings**

The explorer results show some ambiguous spots, but I'm not sure if they’re genuine discrepancies. I think it’s best to focus only on verified findings after looking at the context. Maybe I can ignore the ambiguous results unless I double-check. I should inspect lines 45-48 of Volume III, as they might say something like "Hochschild homology gives E2-chiral algebra." It seems there might be some conceptual confusion to unravel, so I’ll proceed to open it.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex | sed -n '216,226p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex | sed -n '42,50p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex | sed -n '314,318p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   216	
   217	 \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.
   218	
   219	 \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
   220	
   221	 \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
   222	
   223	 \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
   224	\end{description}
   225	\end{theorem*}
   226	
 succeeded in 51ms:
    42	conformal algebra~$L_\cC$; the factorization envelope
    43	$U_X^{\mathrm{fact}}(L_\cC)$ produces a chiral algebra
    44	$A_\cC$; the $\Sd$-framing enhances the factorization
    45	structure. For $d = 2$, the $\mathbb{S}^2$-action on
    46	Hochschild homology gives an $\Etwo$-chiral algebra with
    47	braided monoidal representation category, and all three steps
    48	are proved (Theorem~CY-A). For $d = 3$, holomorphic
    49	Chern--Simons breaks $\Etwo$ to~$\Eone$; the braiding is
    50	recovered via the Drinfeld center of the $\Eone$-monoidal
 succeeded in 51ms:
   314	self-$\operatorname{Hom}$ of~$\cA$ as a chiral bimodule, computed
   315	via OPE residues on Fulton--MacPherson configuration spaces of
   316	algebraic curves. It is distinct from \emph{topological Hochschild
   317	homology} $\mathrm{THH}(\cA)$, which is factorisation homology
   318	over~$S^1$ using only the $E_1$-structure. For $E_\infty$-algebras


thinking
**Searching for Hochschild theories**

I think I should look for the explicit phrase "three Hochschild theories" across various repositories, along with "categorical Hochschild" and similar terms. There's a chance that my search will yield some useful results. I wonder if I might find only a few good sources that provide relevant information. Let's see what I can discover through this targeted approach!
thinking
**Exploring chapter inconsistencies**

I’m thinking about the potential conflicts in a large repo. The user mentioned searching across all chapters, but there may be legacy files outside of the main flow that have inconsistent definitions. It's possible to find many of these. I can search for specific terms like "derived center" or "three theories" in Volume I, where I've already seen some consistency. I'll also look for different considerations like "topological Hochschild" and "categorical Hochschild" to identify comparisons or ambiguities.
exec
/bin/zsh -lc "rg -n 'three Hochschild|topological Hochschild|categorical Hochschild|Bare "'``Hochschild'"''|bare \"Hochschild\"|historical remarks|lifting topological Hochschild|derived center \\(chiral Hochschild homology\\)|Hochschild class|HH\\"'^2'"\\(V_k|HH\\\\bullet\\(V_k' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'three Hochschild|topological Hochschild|categorical Hochschild|lifting topological Hochschild|derived center \\(chiral Hochschild homology\\)|HH\\"'^2'"\\(V_k|HH\\\\bullet\\(V_k' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:316:algebraic curves. It is distinct from \emph{topological Hochschild
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3659:$\Einf$-factorisation structure; topological Hochschild
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1158:\index{topological Hochschild homology!definition}
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1165:The \emph{topological Hochschild homology} is the
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1237:punctured disk to topological Hochschild chains:
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1324:where $q = e^{2\pi i/(k+h^\vee)}$: the categorical Hochschild homology
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:2348:  Output: topological Hochschild cohomology
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:2373:  (half-braiding data, categorical Hochschild cohomology).
/Users/raeez/chiral-bar-cobar/chapters/connections/ym_boundary_theory.tex:435:When infinitesimal automorphisms and dual negative-degree Hochschild classes vanish, the formal boundary moduli problem linearizes. The Koszul dual center provides formal coordinates on the deformation space.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:146:Bare ``Hochschild'' without qualifier is
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:147:permitted only in historical remarks about the
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:762:contribute additional Hochschild classes (they are inner automorphisms of the
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:280:These are distinct invariants. The categorical Hochschild lives on $\cC$ (no curve geometry); the chiral Hochschild lives on $A_\cC$ (curve geometry through the OPE); the derived center is the endomorphism algebra of the identity functor in the factorization category (curve geometry through $\Ran(X)$).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:292: \item A map $\HH^\bullet(\cC, \cC) \to \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ from the categorical Hochschild cochains (the endomorphism algebra of the identity bimodule) to the chiral derived center, compatible with the Gerstenhaber product on the source and the chiral bracket on the target.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:297:Part (i) is Proposition~\ref{prop:bar-dictionary}. For (ii): the Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a Lie bracket of degree $-1$. Under $\Phi$, this bracket becomes the convolution bracket of Vol~I by functoriality of the bar construction: the deconcatenation coproduct on $B(A_\cC)$ and the binary product of $A_\cC$ assemble into a bracket on $\Hom_{\Ran}(B(A_\cC), A_\cC)$, which restricts to $\ChirHoch^*(A_\cC)$ on the cohomology. The Connes operator $B$ on $\mathrm{CC}_\bullet(\cC)$ corresponds, under the bar dictionary, to the degree-preserving component of the bar differential (Proposition~\ref{prop:bar-dictionary}(ii)), which is the modular differential on the chiral side. For (iii): the categorical Hochschild cochains $\mathrm{CC}^\bullet(\cC, \cC)$ map to $\RHom(\Omega B(A_\cC), A_\cC)$ by applying $\Phi$ to each hom-space and using the bar-cobar quasi-isomorphism $\Omega B(A_\cC) \simeq A_\cC$ (Vol~I Theorem~B on the Koszul locus).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:302:The categorical Hochschild $\HH_\bullet(\cC)$ controls the deformation theory of $\cC$ as a CY category: $\HH^2(\cC)$ parametrizes first-order deformations, $\HH^1(\cC)$ the infinitesimal automorphisms. The chiral Hochschild $\ChirHoch^*(A_\cC)$ controls the shadow tower of $A_\cC$: the obstruction classes $\mathrm{obs}_g$ live in $\ChirHoch^2(A_\cC) \otimes H^\bullet(\overline{\cM}_{g,n})$. The derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)$ is the bulk algebra of the holographic datum: its elements are the operators that commute with all boundary insertions. Theorem~\ref{thm:hochschild-bridge} guarantees that the categorical deformation data of $\cC$ is faithfully transmitted, through $\Phi$, to the chiral obstruction data of $A_\cC$.
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:21:categorical Hochschild cohomology: the cyclic bar complex
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:27:to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:7:\begin{remark}[Convention: categorical Hochschild]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:9:In this chapter, ``Hochschild'' refers to the categorical Hochschild
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1497:HH^2(V_k(\mathfrak{sl}_2)).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1499:The Hochschild cohomology $HH^2(V_k(\mathfrak{sl}_2))$ controls
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1510:$HH^2(V_k(\mathfrak{sl}_2))$ and controls deformations of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:421:$\cZ^{\mathrm{der}}_{\mathrm{ch}}$), topological Hochschild
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:423:and categorical Hochschild (Morita composition on
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:107:  the derived center (chiral Hochschild homology)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:411:where $\cC_\partial$ is the dg-category of boundary conditions (Definition~\ref{def:oc-factorization-category}). This identification is \emph{Morita invariant}: it depends only on the category $\cC_\partial$, not on the choice of vacuum object $b$ used to present the boundary algebra $A_\partial = \End(b)$. The passage from $Z_{\mathrm{der}}(\cC_\partial)$ to $C^\bullet_{\mathrm{ch}}(A_\partial, A_\partial)$ is via the standard identification of the derived center of a compactly generated dg-category with the Hochschild cochain complex of any compact generator's endomorphism algebra \cite{Kel06}; the integral-transform formalism of Ben-Zvi--Francis--Nadler~\cite{BZFN10} provides the derived-algebraic-geometric framework for this identification and for the categorical Hochschild theory more broadly.


thinking
**Analyzing findings format**

The user is asking for a detailed report on each finding, including volume, file:line, inconsistency, and severity. Duplicates should be noted as separate findings. I’m considering whether to report core and topological_holography as distinct entries since they may belong to different files or chapters in the same repository. For consistency, I think it might make sense to separate duplicates while counting them separately too. I should keep track of instances checked and violations found, including duplicates in the final count.
thinking
**Inspecting potential findings**

I need to inspect `anomaly_completed_core` and `anomaly_completed_topological_holography` for similarities in heuristics or remarks. If the same issue is repeated, it could be acceptable to separate those findings. There’s a potential unique issue at `raviolo-restriction.tex:107`, so I should search to see if that same phrase is duplicated elsewhere in the documents. This could help clarify whether to categorize them as distinct findings or not. Let's keep the organization clear!
exec
/bin/zsh -lc "rg -n 'lifting topological Hochschild|topological in nature' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'three Hochschild theories \\(categorical, chiral, derived-center\\)|Three Hochschild theories act on a CY category|\\\\begin\\{definition\\}\\[Three Hochschild theories\\]' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'derived center \\(chiral Hochschild homology\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:27:to $\mathrm{ChirHoch}^*(A_\cC)$, lifting topological Hochschild
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:11:$\mathrm{CC}_*(\cC)$), which are topological in nature.
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:270:Three Hochschild theories act on a CY category $\cC$ with chiral algebra $A_\cC = \Phi(\cC)$, and distinguishing them is essential for the bridge to Volume~I.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:272:\begin{definition}[Three Hochschild theories]
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:107:  the derived center (chiral Hochschild homology)
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '2132,2144p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '1374,1384p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '2255,2266p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2132	standard AdS$_3$/CFT$_2$ dictionary.
  2133	
  2134	\emph{Bulk.}
  2135	The Hochschild--Serre spectral sequence computation at the start of
  2136	this subsection gives $\HH^0(\mathrm{Vir}_c) = \C$,
  2137	$\HH^1(\mathrm{Vir}_c) = 0$ (all derivations inner),
  2138	$\HH^2(\mathrm{Vir}_c) = \C \cdot \Theta_c$ (the Gel'fand--Fuchs
  2139	$2$-cocycle), and
  2140	$\HH^{n \ge 3}(\mathrm{Vir}_c) = 0$ for generic~$c$, so the derived
  2141	centre is $\Zder(\mathrm{Vir}_c) \simeq \C[\![c]\!]$. This identifies
  2142	the unique bulk observable with the central charge parameter.
  2143	
  2144	\emph{Lines (abstract).}
 succeeded in 51ms:
  1374	 The $A_\infty$ structure on $\mathrm{Vir}_c$ has
  1375	 $m_k \ne 0$ for all $k \ge 3$
  1376	 (Remark~\ref{rem:yangian-virasoro-nonformality}). For
  1377	 a Yangian $Y(\mathfrak{g})$, the associated graded
  1378	 $U(\mathfrak{g}{[t]})$ is formal ($m_k = 0$ for $k \ge 3$)
  1379	 and the deformation lives in $\HH^2(U(\mathfrak{g}{[t]}))$
  1380	 (Proposition~\ref{prop:yangian-deformation-obstruction}).
  1381	 The non-vanishing of the Virasoro higher $A_\infty$
  1382	 operations means the deformation problem does not
  1383	 split into a Yangian direction and a Lie-algebra
  1384	 direction.
 succeeded in 51ms:
  2255	The Hochschild--Serre spectral sequence gives:
  2256	\[
  2257	\HH^0(\mathrm{Vir}_c) = \C,
  2258	\qquad
  2259	\HH^1(\mathrm{Vir}_c) = 0,
  2260	\qquad
  2261	\HH^2(\mathrm{Vir}_c) = \C \cdot \Theta_c,
  2262	\qquad
  2263	\HH^{n \ge 3}(\mathrm{Vir}_c) = 0
  2264	\quad\text{(generic~$c$)},
  2265	\]
  2266	where $\Theta_c$ is the Gel'fand--Fuchs $2$-cocycle recording
codex
Another propagated Vol II drift shows up in `3d_gravity.tex`: it computes `\HH^i(\mathrm{Vir}_c)` and immediately identifies the result with the derived center of the Virasoro boundary algebra. In this repo’s own terminology that should be chiral Hochschild, not an unqualified `\HH`, so I’m checking whether the same notation leak appears in the dedicated Hochschild chapter or only in the physics-facing connections.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex | sed -n '579,588p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '520,536p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '404,416p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   579	where $\circ_i$ denotes operadic composition at the $i$-th input.
   580	
   581	\begin{proposition}[Virasoro Hochschild Cohomology; \ClaimStatusConditional]
   582	\label{prop:vir-hochschild}
   583	Assume the Khan--Zeng Virasoro realization satisfies
   584	Theorem~\ref{thm:physics-bridge}.
   585	The chiral Hochschild cohomology $HH^\bullet_{\text{ch}}(\text{Vir}_c)$ is isomorphic
   586	to the space of infinitesimal deformations of the Virasoro $A_\infty$ structure on a
   587	smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
   588	at generic level/charge; the critical locus $c_{\mathrm{crit}}$ analogous to $k = -h^\vee$
 succeeded in 52ms:
   520	restatement. Write $\cL_b \subset \cM_{\mathrm{vac}}$ for the
   521	Lagrangian in the $(-2)$-shifted symplectic stack of vacua
   522	determined by the boundary condition~$b$
   523	(by the corrected bulk--boundary--line triangle of
   524	Section~\ref{sec:ht-bulk-boundary-line}).
   525	The Hochschild--Kostant--Rosenberg theorem for the derived
   526	self-intersection gives
   527	\[
   528	 \HH^\bullet(\cA_\partial,\cA_\partial)
   529	 \;\simeq\;
   530	 \cO\bigl(T^*[-1]\cL_b\bigr)
   531	 \;\simeq\;
   532	 \cO(\cM_{\mathrm{vac}})\big|_{\cL_b}\,,
   533	\]
   534	where the second identification uses the Lagrangian condition:
   535	$T^*[-1]\cL_b$ is the formal neighbourhood of $\cL_b$ inside
   536	$\cM_{\mathrm{vac}}$. The bulk algebra is therefore the
 succeeded in 52ms:
   404	\label{rem:bulk-categorical}
   405	Under the compact-generation hypotheses relevant to the
   406	boundary-linear exact sector, the bulk algebra is equivalently the
   407	derived center of the open-sector category:
   408	\[
   409	\cO_{\mathrm{bulk}} \;\simeq\; Z_{\mathrm{der}}(\cC_\partial) \;:=\; \RHom_{\mathrm{Fun}(\cC_\partial, \cC_\partial)}(\id, \id),
   410	\]
   411	where $\cC_\partial$ is the dg-category of boundary conditions (Definition~\ref{def:oc-factorization-category}). This identification is \emph{Morita invariant}: it depends only on the category $\cC_\partial$, not on the choice of vacuum object $b$ used to present the boundary algebra $A_\partial = \End(b)$. The passage from $Z_{\mathrm{der}}(\cC_\partial)$ to $C^\bullet_{\mathrm{ch}}(A_\partial, A_\partial)$ is via the standard identification of the derived center of a compactly generated dg-category with the Hochschild cochain complex of any compact generator's endomorphism algebra \cite{Kel06}; the integral-transform formalism of Ben-Zvi--Francis--Nadler~\cite{BZFN10} provides the derived-algebraic-geometric framework for this identification and for the categorical Hochschild theory more broadly.
   412	\end{remark}
   413	
   414	\begin{remark}[Scope of the bulk--Hochschild identification]
   415	\label{rem:bulk-hochschild-scope}
   416	The quasi-isomorphism $\mathcal{O}_{\mathrm{bulk}} \simeq C^\bullet_{\mathrm{ch}}(A_{\partial}, A_{\partial})$ is proved here for HT prefactorization algebras in the scope of Theorem~\ref{thm:physics-bridge}; the proof uses reduction along $\R$ and factorization homology of the chosen prefactorization model $\mathsf{Obs}$. The stronger triangle composition (that bulk $\simeq$ derived center of boundary) further requires compact generation and the derived center quasi-isomorphism. These are verified rigorously only in the boundary-linear exact sector (Theorem~\ref{thm:boundary-linear-bulk-boundary}). The global triangle for all HT theories remains conjectural, and the manuscript does not currently prove an abstract bulk/Hochschild comparison for an arbitrary logarithmic $\SCchtop$-algebra without a physical realization.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex | sed -n '7,13p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '1208,1215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '2390,2400p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     7	\begin{remark}[Convention: categorical Hochschild]
     8	\label{rem:hochschild-convention-categorical}
     9	In this chapter, ``Hochschild'' refers to the categorical Hochschild
    10	invariants of a dg category (the cyclic bar complex
    11	$\mathrm{CC}_*(\cC)$), which are topological in nature.
    12	The chiral Hochschild cohomology $\ChirHoch^*$ of Volume~I
    13	(Theorem~H) is the chiral upgrade incorporating OPE data and curve
 succeeded in 50ms:
  2390	$(d^{\mathrm{ann}})^2=0$ is the algebraic manifestation of
  2391	$\partial^2=0$ on the manifold with corners
  2392	$\overline{\FM}{}^{\,\mathrm{ann}}_{r,s}$.
  2393	\end{construction}
  2394	
  2395	\begin{theorem}[Annular bar computes chiral Hochschild homology;
  2396	\ClaimStatusProvedHere]%
  2397	\label{thm:annular-HH-vol2}%
  2398	\index{annular bar complex!Hochschild identification|textbf}%
  2399	\index{Hochschild homology!annular bar model}%
  2400	Let $\cA$ be a strongly admissible $E_1$-chiral algebra. There
 succeeded in 50ms:
  1208	\textbf{The annular sector.}\enspace
  1209	The annular bar differential
  1210	(Theorem~\ref{thm:annular-bar-differential}) connects the
  1211	open-sector $E_1$ structure to the closed-sector trace: the
  1212	ordered bar complex on the annulus $S^1 \times \R$ computes
  1213	chiral Hochschild homology, realising the genus-$1$ ordered sector
  1214	as the categorical trace of the open-sector category.
  1215	






thinking
**Evaluating potential issues**

I'm noticing a possible issue in Volume II when it comes to line 107 regarding `raviolo-restriction`. It seems there's a mix-up with the objects here; derived centers refer to cochains instead of homology. I wonder if this is more about object conflation than just three-theory conflation. The user requested an audit for cross-volume consistency related to Hochschild disambiguation, so this does seem significant to address. Time to consider this as potentially high priority.
thinking
**Searching for findings**

I'm wondering if there could be anything significant in Volume I. It seems uncertain, but I might search for "Hochschild" in the noncanonical older file called `theory/hochschild_cohomology.tex`, especially regarding the derived center. The search results aren't very straightforward, and there might be older chapters that aren't included. I guess I'll take a closer look to see if I can uncover something useful there!
thinking
**Evaluating audit details**

I've gone through a lot of files and contexts, like CLAUDE, concordance, and others—maybe around 16 snippets. It sounds like I need to summarize and clarify things, possibly counting instances checked among the candidate surfaces. I should probably track this better: "Instances checked: 16 | Violations found: 6 | Verdict: FAIL." I’m thinking "instances checked" might refer to the actual candidate surfaces I’ve read for the audit. Let's make sure to keep that in mind!
thinking
**Considering findings for audit**

I'm pondering how many findings to include in the audit. Seven or eight might be a good number, but I want to make sure they're substantial enough to be meaningful. The user asked for a full audit, so it’s important that I capture the essential points without overwhelming them. Balancing quality and quantity is key here! I’ll focus on making sure everything I include is strong and relevant.
thinking
**Considering file descriptions**

I think it's okay to mention another file path in the description. I also want to reference the anomaly surface and the main file frontier. It seems like including `anomaly_completed_core` and `...topological_holography` duplicates in the description will help keep the list shorter. This keeps things clean and concise, and I’m focused on ensuring the information is organized! Let's proceed with this approach.
thinking
**Inspecting theoretical inconsistencies**

I see that there's an explicit comparison of theories. The missing qualifier on the right-hand side seems to break the rule about mandatory qualifiers. I need to look closely at the context around lines 2587-2600. The right side `\HH^n(X)` isn't labeled properly as categorical — maybe it should be [MEDIUM]. Since the user pointed out a direct inconsistency, I should clarify that the comparison indeed requires those qualifiers. I’m also thinking about checking more context past line 2600 for further clarity.
codex
I’ve finished the re-check loop. The remaining issues aren’t just vague wording: they are repeated object/qualifier drifts concentrated in Vol II connection chapters and a formal redefinition in Vol III that replaces topological Hochschild by derived center.
Plan update
Search, context reads, and duplicate checks are complete. I have re-verified the surviving discrepancies against the actual chapter text and removed weaker candidates.
  ✓ Search all three chapter trees for Hochschild terminology and identify candidate conflation sites
  ✓ Read each candidate hit in context and test against the canonical three-theory distinction
  ✓ Re-check downstream duplicates and second-order propagation around each surviving finding
  → Produce severity-ordered audit report with exact file:line references and counts
codex
- [CRITICAL] Vol III [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:272) — The formal definition of “Three Hochschild theories” replaces the canonical `topological / chiral / categorical` split with `categorical / chiral / derived center`; the chapter intro already advertises the same triad at [line 4](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4). This rewrites the programme-level taxonomy: the derived center is not the third Hochschild theory in Vol I’s concordance, but the chiral cochain-level bulk.

- [HIGH] Vol III [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:20) — The opening convention says “Hochschild” in Vol III means categorical Hochschild, then says `\Phi` lifts “topological Hochschild data” to `\mathrm{ChirHoch}^*(A_\cC)` at [line 27](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:27). That collapses categorical into topological. The same categorical-as-topological wording recurs in [hochschild_calculus.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:9).

- [HIGH] Vol II [raviolo-restriction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:107) — `Z(\cA)` is glossed as “the derived center (chiral Hochschild homology)”. In Vols I–II, the derived center is computed by chiral Hochschild cochains/cochain complex; chiral Hochschild homology is a different annular theory.

- [HIGH] Vol II [anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1491) — The boundary-anomaly passage uses bare `HH^2(V_k(\mathfrak{sl}_2))` and `B \simeq HH^\bullet(V_k(\mathfrak{sl}_2))` for VOA deformations and the bulk-boundary map. In this volume’s own theory chapter, bulk is identified with chiral Hochschild cochains of the boundary algebra, not unqualified `HH`. The same drift propagates in [anomaly_completed_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1786) and [anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:1790).

- [HIGH] Vol II [3d_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2135) — The Virasoro bulk computation uses bare `\HH^i(\mathrm{Vir}_c)` and then identifies the result with the derived centre/bulk of the boundary algebra; the same notation is repeated at [line 2255](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2255). The dedicated Virasoro chapter uses the qualified chiral theory instead at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:585).

- [MEDIUM] Vol II [thqg_holographic_reconstruction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2591) — The comparison `\operatorname{ChirHoch}^n(\cA_X) \cong \HH^n(X)` leaves the right-hand side unqualified and then speaks of the “full Hochschild diamond”. Vol I’s concordance requires explicit qualifiers when two Hochschild theories are compared; here the categorical side is only implicit.

No surviving Volume I inconsistency remained in the candidate chapter surfaces I re-read against the concordance.

## Summary
Instances checked: 25 | Violations found: 6 | Verdict: FAIL
tokens used
298,909
