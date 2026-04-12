# XV08_thm_status_xvol (81s, gpt-5.4)



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
session id: 019d83b2-cc7f-73a0-b1de-3b8b8c40797a
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


MISSION: Cross-volume consistency check for Theorem status vs proofs.

Do theorem status claims in concordance.tex, metadata, and README match what's actually proved in the .tex files? Check all five theorems A-D+H.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers



thinking
**Conducting an audit check**

I need to perform a cross-volume consistency check for the status vs. proofs of five theorems (A-D and H) without modifying any files. My plan is to read and report on this, possibly using the deep-beilinson-audit and claim-surface-sync skills. I should also refer to AGENTS about necessary reads before any mathematical edits, though no edits are allowed. It seems wise to check through the concordance and theorem registry as this is for an audit, not an edit. Following developer instructions, I'll prioritize explorers for quick and accurate information.
thinking
**Navigating codebase inquiries**

I need to use the spawn_agent explorer to search the codebase for the user's inquiry. The developer mentions trusting the explorer's results without needing verification, but there's a conflict since the user wants specific file contents or tool outputs. Maybe I can use the explorer to gather candidate files or specific lines, and then I'll read those exact lines myself. It seems best to balance both approaches: rely on the explorer for broad searches and then confirm the key details directly.
thinking
**Clarifying file content requests**

The user is asking for actual file contents or tool outputs that I've personally read. The explorer's output can be cited as tool output, but it doesn't provide the exact file contents. To stay within guidelines, I should use the explorer to identify relevant files and specific lines. It feels like manually opening those files might not be considered re-searching. However, I need to ensure I provide verification for the user. Maybe I can ask the explorer to read the relevant files and report the exact lines.
codex
Using `deep-beilinson-audit` and `claim-surface-sync` workflows here: I’m locking the theorem surfaces for A–D and H across concordance, metadata, README, and the live theorem/proof environments in all three volumes, then I’ll compare claimed status against what is actually present.

thinking
**Planning tool usage**

I think I need to open skill files, and I’m trying to decide whether to use `exec cat` or `rg`. I might want to use `multi_tool_use.parallel` for running commands in parallel. It feels like I should consider updating my plan since this seems substantial, but it’s not necessary unless the user asks for it. Okay, let’s go ahead and set the plan.
Plan update
Cross-volume audit of theorem-status consistency for the five theorem lanes A–D and H, with no file edits.
  → Read the relevant skill instructions and locate the canonical theorem-status surfaces in Volumes I–III
  • Extract claimed statuses for Theorems A–D and H from concordance, metadata, and README surfaces
  • Inspect the actual theorem/proof environments in the source chapters and compare against claimed status
  • Re-verify each discrepancy and produce a severity-ordered audit report

thinking
**Searching skill files**

I need to read the skill files, and I’m thinking it might be good to use parallel execution for efficiency. Before that, I'll consider using the explorer agent to check on the status of theorem A-D+H surfaces. I want to ensure I craft a precise prompt for that, so it helps me gather the right information. It feels important to get this right for exploring those surfaces effectively!
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
 succeeded in 52ms:
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

collab spawn_agent(call_KsmmGVPkKKcdl4vUky0Ysnmr, prompt="<task>Audit theorem-status consistency for the five theorem lanes A, B, C, D, H across three repos: /Users/raeez/chiral-…")
mcp startup: no servers
spawn_agent(call_KsmmGVPkKKcdl4vUky0Ysnmr, prompt="<task>Audit theorem-status consistency for the five theorem lanes A, B, C, D, H across three repos: /Users/raeez/chiral-…") pending init:
  agent: 019d83b3-2d68-7e82-a665-8535448aca79
Plan update
  • Identify canonical status sources in each repo (concordance, metadata, README) for theorems A/B/C/D/H
  • Locate live theorem/proof environments in .tex chapters across repos for these theorems
  • Compile report listing status claims and proximity of proofs per theorem lane
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem [ABC]")}' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: parse error near `)'
codex
I’ve loaded the audit workflows. Next I’m reading the canonical status surfaces and the red-team context before I compare them against the live theorem/proof environments.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
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

 succeeded in 53ms:
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

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem [ABCDH]" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,120p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
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

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem [ABC]" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Evaluating search methods**

I'm thinking about possibly using the explorer tool soon, but maybe I should do a manual search for now. I want to consider using a parallel approach with a tool like 'rg' across repositories to find theorem labels, names, or the main theorem in README files. I don't necessarily need to use bash separators here, so I might run a combined search using 'rg -n' with alternation across directories. Let's see how that goes!
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem [ABCDH]" README.md' in /Users/raeez/chiral-bar-cobar exited 1 in 54ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Bar-cobar adjunction" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
31:\textbf{A} & Bar-cobar adjunction
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Bar-cobar inversion" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
36:\textbf{B} & Bar-cobar inversion
4864:Bar-cobar inversion there is genus~$0$ unconditional and, at higher
codex
The canonical concordance says all five theorem lanes are proved, but Theorem B and parts of H already look like mixed-status summaries rather than clean unconditional proved-here claims. I’m now locating the exact theorem environments and the README/metadata mirrors to see whether that summary outruns the live source.
exec
/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:bar-cobar-isomorphism-main|Bar-cobar adjunction|Theorem A|five main theorems' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:quantum-complementarity-main|Complementarity|Theorem C' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:genus-universality|Modular characteristic|Theorem D|obs_g\\(\\\\cA\\)=\\\\kappa\\(\\\\cA\\)\\\\lambda_g' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:higher-genus-inversion|Bar-cobar inversion|Theorem B' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|Chiral Hochschild|Theorem H' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 621

/Users/raeez/chiral-bar-cobar/CLAUDE.md:486:| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
/Users/raeez/chiral-bar-cobar/AGENTS.md:547:| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:307:| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:55:organising structure. The five main theorems (A--H) are proved,
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:54:- `B(A)` is an E_1 coassociative coalgebra classifying twisting morphisms (Theorem A);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:210:We summarize the status of the five main theorems of Volume~I when specialized to chiral algebras arising from CY categories.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:215: \item[Theorem A (adjunction).] The bar-cobar adjunction $B \dashv \Omega$ restricts to CY chiral algebras: $B(A_\cC)$ is a factorization coalgebra on $\Ran(X)$, and $D_{\Ran}(B(A_\cC)) \simeq B(A_{\cC^!})$. The CY identification CY-A(ii) gives $\mathrm{CC}_\bullet(\cC) \simeq B(A_\cC)$.
/Users/raeez/chiral-bar-cobar-vol2/README.md:22:| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/fg_shadow_conjecture_audit.md:215:> "the bar-cobar equivalence (Vol I, Theorem A) gives $A^!\simeq\overline{B}(A)^\vee$, and the associated graded of the dual is the dual of the associated graded (the filtration is exhaustive and separated by hypothesis (c)), so... $\gr_{\mathrm{com}}(A^!)\simeq ... =(\gr_{\mathrm{com}}A)^!_{FG}$."
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/real_complex/noncommutative_geometry.md:225:  algebras, bar cohomology is concentrated in bar degree 1 (Theorem A).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:773:\phantomsection\label{thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:928:\phantomsection\label{V1-thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1273:the five main theorems of Volume~I are the invariants that survive
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/universal_modular_deformation_theorem.md:41:(cor:theta-twisting-morphism, thm:convolution-master-identification). The element Theta_A is the universal twisting morphism. Every natural derived invariant of the formal genus expansion is a natural transformation from Theta to a target functor on ChAlg_X^mk. The five main theorems are instances:
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:85:Volume~I is Koszul duality on a curve: the bar construction for chiral algebras on an algebraic curve~$X$, five main theorems proved at all genera. Three structure theorems organise the representation-theoretic content. \emph{Algebraicity}: $H(t)^2 = t^4 Q_L(t)$ for a computable quadratic~$Q_L$, so the shadow generating function is algebraic of degree~$2$. \emph{Formality identification}: the shadow obstruction tower agrees with the $L_\infty$ formality obstruction tower at all degrees (Theorem~\ref{V1-thm:shadow-formality-identification}), and the discriminant $\Delta = 8\kappa S_4$ classifies algebras into four depth classes~(G/L/C/M). \emph{Complementarity}: under perfectness and chain-level nondegeneracy (satisfied for all standard families; conditional in general), factorisation homology decomposes as $H^*(\overline{\mathcal{M}}_g, Z(A)) \simeq Q_g(A) \oplus Q_g(A^!)$, a Lagrangian splitting.
 succeeded in 52ms:
Total output lines: 1205

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:515:\begin{proposition}[Complementarity for $\kappa_{\mathrm{cat}}$]
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:57:We prove (in rigorous sketch) the identification of Theorem CY-B: for a quantum vertex chiral group $G(X)$ attached to a CY3 $X$, the Weyl--Kac--Borcherds denominator function $\Phi_X(z)$ equals the bar-complex Euler product of $B(A_X)$. Four steps: (1)~define the bar-complex Euler product on the root lattice, (2)~identify root-graded pieces of $B(A_X)$ with root spaces of $\frakg_X$, (3)~show $\dim B(A_X)_\alpha = \mult(\alpha)$, (4)~identify the Weyl vector $\rho$ as the regularization shift ensuring convergence.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:107:(Theorem CY-A of Vol.~III). Its bar complex
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:668:Theorem CY-B: the automorphic correction IS the shadow obstruction tower.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:850:Koszul locus} (Theorem CY-B(ii)): the bar complex (product side) and the
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:898:\item \textbf{CY-to-chiral functor} (Theorem CY-A): the existence
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:910:\item \textbf{Shadow obstruction tower = automorphic correction} (Theorem CY-B):
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:978:The result is the content of Theorem CY-B of Volume~III: the denominator
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:6:% Theorem D (modular characteristic), Theorem C (complementarity),
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:156:\subsection{Complementarity}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1815:\item \emph{Complementarity.} $\kappa_{\mathrm{ch}}(\cA) + \kappa_{\mathrm{ch}}(\cA^!)
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:65:These notes spell out the physical picture behind $G(X)$ for a CY3 $X$. Four ingredients are developed: M-theory holography, open string field theory from CY categories, closed strings from cyclic homology, and their packaging via Koszul duality. Throughout, we connect to the CY-to-chiral functor $\Phi$ (Theorem CY-A), the bar-cobar machine of Volume~I, and the $E_1/E_2$ chiral hierarchy of Volume~III.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:292:\begin{remark}[Relation to Theorem CY-A]
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:300:of Theorem CY-A is \emph{precisely} the open string field theory construction
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:759: open string fields $\RHom(\cF, \cF)[1]$ with action from the $\Ainf$-structure. This is Theorem CY-A: the cyclic $\Ainf$-structure is promoted to a chiral algebra $\Phi(\cC)$.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_cy_to_chiral_wave13.md:36:2. **Theorem CY-A_2** (line 32, `thm:cy-to-chiral`): scoped to d=2 in title + signature; uses S^2-framing. **PASS.**
/Users/raeez/calabi-yau-quantum-groups/compute/audit/cross_consistency_audit_2026_04_04.md:148:**Complementarity sum:** KM = 0 (all families), Virasoro = 13, betagamma = 0, W_3 = 250/3, N=2 SCA = 1. All correct. No cross-module contradictions.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:1074:\item \textbf{Theorem CY-A} (CY-to-chiral functor): The functor
 succeeded in 52ms:
Total output lines: 772

/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1122:\begin{theorem}[Modular characteristic of $\C^3$: five-path verification]
/Users/raeez/calabi-yau-quantum-groups/README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
/Users/raeez/calabi-yau-quantum-groups/README.md:42:| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:530:% For W-algebras: kappa + kappa' = rho*K (Theorem D).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:503: \item \textbf{Modular characteristic and shadow tower.}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:757:\item Modular characteristic: $\kappa_{\mathrm{BKM}}(K3 \times E) = 5$ (the weight of $\Delta_5$; the single-copy chiral value is $\kappa_{\mathrm{ch}} = 3$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:33:\phantomsection\label{thm:genus-universality}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1800:\begin{proposition}[Modular characteristic of the K3 sigma model;
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4168: (Theorem~\ref{thm:genus-universality}),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4469:\item \textbf{Modular characteristic.}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4622:$\kappa_{\mathrm{ch}}(\cA)$ & $3$ & Modular characteristic (Vol~I, Theorem~D) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4965:\begin{theorem}[Modular characteristic of the K3 sigma model]
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:6:% Theorem D (modular characteristic), Theorem C (complementarity),
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:7:% thm:anomaly-koszul, cor:kappa-additivity, thm:genus-universality,
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:182:\item Modular characteristic $\kappa_{\mathrm{ch}}(A_X) = \chi^{\mathrm{CY}}(\cC)$;
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:315:\begin{theorem}[Modular characteristic of the K3 sigma model]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1084: \item \emph{Modular characteristic} $\kappa_{\mathrm{ch}}(K3 \times E) = 3$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
 succeeded in 52ms:
Total output lines: 600

/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:109:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:277: \item \emph{Chiral Hochschild.} The chiral Hochschild cohomology $\ChirHoch^*(A_\cC)$ of Volume~I (Theorem~H): concentrated in cohomological degrees $\{0, 1, 2\}$ with polynomial Hilbert series. This is the obstruction-theoretic invariant governing the shadow tower of $A_\cC$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:312:\section{Categorical Theorem H}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:320:\begin{theorem}[Categorical Theorem H]
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:223: \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
/Users/raeez/chiral-bar-cobar/main.tex:488:\newcommand{\ChirHoch}{CH} % Chiral Hochschild
/Users/raeez/chiral-bar-cobar/main.tex:1027:% Chiral Hochschild cohomology, cyclic structure, Connes operator,
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:583:\item Right side: Chiral Hochschild cochains (quantum)
/Users/raeez/chiral-bar-cobar/CLAUDE.md:19:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:273:**C27. Chiral Hochschild of Vir.** `ChirHoch^*(Vir_c)` concentrated in degrees {0,1,2}; polynomial Hilbert series. This is AMPLITUDE (topological), NOT virtual dimension (arithmetic) (AP134). NOT C[Theta] (AP94). NOT Gelfand-Fuchs (GF infinite, AP95).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:840:AP160: Three Hochschild theories -- geometry determines which. (i) Topological HH: E_1 input -> E_2 (Deligne). (ii) Chiral ChirHoch: E_inf-chiral input -> {0,1,2} (Theorem H). (iii) Categorical HH: dg category -> E_2 with CY shifted Poisson. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts. Conv:three-hochschild in concordance.tex is constitutional.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
/Users/raeez/chiral-bar-cobar/compute/audit/swarm_2026_04_09_batch1_synthesis.md:30:## Segment B — Theorem H proof gap + critical level
/Users/raeez/chiral-bar-cobar/compute/audit/swarm_2026_04_09_batch1_synthesis.md:43:**Defense verdict (RESCUABLE-WITH-EXTRA-HYPOTHESIS).** The proof actually goes through bar-cobar replacement → Hom complex of D_X-modules on X → Brylinski [0,2] amplitude (configuration spaces are integrated out by bar-cobar, NOT bounded pointwise). Real log de Rham amplitude of (C̄_{n+2}(X), D) via Deligne logarithmic Poincaré + Kriz-Totaro collapse is more nuanced than the strawman SS suggests. Add "generic level" + Mok25 snc hypothesis. Already invoked piecewise in family-specific theorems but not hoisted to Theorem H.
/Users/raeez/chiral-bar-cobar/compute/audit/swarm_2026_04_09_batch1_synthesis.md:45:**Convergence.** Both agree: (a) the spectral-sequence route is a strawman, (b) the real route is bar-cobar reduction, (c) "generic level" hypothesis must be added explicitly. Detailed deep dive in **Batch 2** (10 angles on Theorem H specifically).
/Users/raeez/chiral-bar-cobar/compute/audit/swarm_2026_04_09_batch1_synthesis.md:152:8. **Theorem H** — see Batch 2 synthesis for full reformulation
 succeeded in 52ms:
Total output lines: 542

/Users/raeez/chiral-bar-cobar/CLAUDE.md:487:| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:826:AP147: Circular proof routing. Theorem B and def:koszul-chiral-algebra appeared mutually circular until the routing was made explicit: twisted-tensor → cone identification → bar-cobar (commit 65262ee). When a proof chain involves multiple theorems that reference each other, insert a ROUTING REMARK citing the primitive non-circular anchor. If no such anchor exists, the proof is genuinely circular and must be restructured.
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1604 | Bar-cobar inversion is quasi-isomorphism |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:761:| `thm:higher-genus-inversion` | `theorem` | 4082 | Higher genus inversion |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:3253:| `thm:bar-cobar-htt` | `theorem` | 524 | Bar-cobar inversion via homotopy transfer |
/Users/raeez/chiral-bar-cobar/AGENTS.md:548:| B | PROVED | Bar-cobar inversion: Omega(B(A)) → A qi on Koszul locus |
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5763:bulk respectively. Bar-cobar inversion
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:166:\begin{remark}[Bar-cobar inversion is not the seven-face master move]
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:217: \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:129: \item \emph{Bar-cobar inversion}:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:143:Bar-cobar inversion recovers the boundary; the Drinfeld center
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:365: \item \emph{Bar-cobar inversion}: $\Omega(B(A)) \simeq A$ recovers the original algebra (Vol~I Theorem~B on the Koszul locus). This is $A$, not $A^!$.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
/Users/raeez/chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:206:\begin{conjecture}[Bar-cobar inversion;
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:433:(Theorem~\ref{thm:higher-genus-inversion}).
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:543:(Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{F})) \cong \mathcal{F}$, recovering the fermion itself.)
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:592:(Bar-cobar inversion gives $\Omega(\bar{B}(\beta\gamma)) \cong \beta\gamma$, recovering $\beta\gamma$ itself.)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Complementarity" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
47:\textbf{C} & Complementarity
187:\item \textbf{Complementarity}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Modular characteristic" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
54:\textbf{D} & Modular characteristic
4424: & Modular characteristic~$\kappa(\cA)$
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Chiral Hochschild" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
64:\textbf{H} & Chiral Hochschild
115:\item \emph{Chiral Hochschild cohomology}
373:\item \emph{Chiral Hochschild cohomology
4305:\paragraph{Chiral Hochschild descent lemma.}
4716:$H$ & Chiral Hochschild: $\ChirHoch^n = 0$ for $n > 2$, $P(t) = 1+t^2$; & \textbf{Proved} (generic level, & Thms~\ref{thm:w-algebra-hochschild}, \\
7042: & Chiral Hochschild descent:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
131:| `thm:completed-bar-cobar-strong` | `theorem` | 924 | MC element lifts to the completed convolution algebra |
253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1604 | Bar-cobar inversion is quasi-isomorphism |
254:| `lem:bar-cobar-associated-graded` | `lemma` | 1946 | Associated graded |
255:| `thm:bar-cobar-spectral-sequence` | `theorem` | 1962 | Bar-cobar spectral sequence |
259:| `thm:bar-cobar-inversion-functorial` | `theorem` | 2173 | Functoriality of bar-cobar inversion |
346:| `thm:hochschild-bar-cobar` | `theorem` | 324 | Hochschild via bar-cobar |
380:| `thm:bar-cobar-resolution` | `theorem` | 4572 | Bar-cobar resolution |
420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
489:| `thm:fusion-bar-cobar` | `theorem` | 4974 | Fusion product compatibility on the module bar surface |
504:| `thm:bar-cobar-verdier` | `theorem` | 1313 | Bar-cobar Verdier |
505:| `cor:bar-cobar-inverse` | `corollary` | 1447 | Bar-cobar mutual inverses |
536:| `thm:off-koszul-ran-inversion` | `theorem` | 825 | Off-Koszul bar-cobar inversion on Ran |
616:| `thm:kl-bar-cobar-adjunction` | `theorem` | 1001 | Chain-level KL adjunction from bar-cobar |
647:| `thm:en-chiral-bridge` | `theorem` | 54 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
651:| `cor:n2-recovery` | `corollary` | 639 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
964:| `thm:ran-coherent-bar-cobar` | `theorem` | 13796 | Ran-coherent bar-cobar equivalence |
1175:| `thm:completed-bar-cobar` | `theorem` | 191 | Completed bar-cobar duality |
1178:| `thm:resonance-filtered-bar-cobar` | `theorem` | 673 | Resonance-filtered completed bar/cobar |
1599:| `thm:sl2-genus1-inversion` | `theorem` | 3686 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:bar-cobar-isomorphism-main" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 298

appendices/homotopy_transfer.tex:531:of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} is the
appendices/homotopy_transfer.tex:584:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): on the Koszul locus,
audit_campaign_20260412_231034/T20_gerstenhaber.md:1561:chapters/theory/cobar_construction.tex:1803:The bar-intrinsic MC element $\Theta_\cA := D_\cA - d_0$ (Theorem~\ref{thm:mc2-bar-intrinsic}) lives in the modular convolution algebra $\gAmod$, and the cobar complex reconstructs $\cA$ from $\barB(\cA)$ by the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
audit_campaign_20260412_231034/F12_MC_equation.md:445:(Theorem~\ref{thm:bar-cobar-isomorphism-main}); Verdier duality
metadata/dependency_graph.dot:2422:  thm_bar_cobar_isomorphism_main [label="thm:bar-cobar-isomorphism-main\ntheorem [Pr]\nGeometric bar--cobar duality", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2858:  thm_bar_cobar_isomorphism_main_equations [label="thm:bar-cobar-isomorphism-main-equations\ntheorem [Pr]\nBar-cobar isomorphism, retained for equa...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
metadata/theorem_registry.md:807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
audit_campaign_20260412_231034/T04_thm_C1.md:287:$\operatorname{Ran}(X)$. Theorem~\ref{thm:bar-cobar-isomorphism-main}
audit_campaign_20260412_231034/T01_thm_A.md:204:The theorem is indexed in the concordance as `thm:bar-cobar-isomorphism-main`, but the proof surface looks spread across the core bar-cobar chapters. I’m pulling the skill instructions and then reading the exact theorem block plus its dependency chain before auditing the proof.
audit_campaign_20260412_231034/T01_thm_A.md:208:/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-isomorphism-main\\}|bar-cobar-isomorphism-main|Verdier intertwining|thm:bar-cobar-verdier|thm:verdier-bar-cobar|Theorem~A|bar-cobar adjunction and Verdier\" chapters/theory chapters/frame chapters/connections | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/T01_thm_A.md:230:metadata/theorem_registry.md:420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
audit_campaign_20260412_231034/T01_thm_A.md:235:metadata/theorem_registry.md:807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
audit_campaign_20260412_231034/T01_thm_A.md:242:metadata/dependency_graph.dot:2422:  thm_bar_cobar_isomorphism_main [label="thm:bar-cobar-isomorphism-main\ntheorem [Pr]\nGeometric bar--cobar duality", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T01_thm_A.md:246:metadata/dependency_graph.dot:2858:  thm_bar_cobar_isomorphism_main_equations [label="thm:bar-cobar-isomorphism-main-equations\ntheorem [Pr]\nBar-cobar isomorphism, retained for equa...", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T01_thm_A.md:253:chapters/frame/guide_to_main_results.tex:35: Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]
audit_campaign_20260412_231034/T01_thm_A.md:263:chapters/frame/heisenberg_frame.tex:1333:(Theorem~\ref{thm:bar-cobar-isomorphism-main}):
audit_campaign_20260412_231034/T01_thm_A.md:264:chapters/frame/heisenberg_frame.tex:1530:(Theorem~\ref{thm:bar-cobar-isomorphism-main}).



thinking
**Analyzing canonical files and theorem environments**

I’m focusing on extracting key canonical statuses from each canonical file, including concordance, metadata, and README, noting any missing mentions. I plan to check similar files across volumes 2 and 3 to compare. Also, I want to locate the actual live theorem/proof environments in the source .tex files by verifying line numbers, starting with a specific theorem label in a large file, to understand where proofs reside.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3320,3445p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:


\subsection{Koszulness and the conformal bootstrap}
\label{subsec:koszulness-bootstrap}

\begin{theorem}[Koszulness implies bootstrap closure;
\ClaimStatusProvedHere]
\label{thm:koszulness-bootstrap}
\index{conformal bootstrap!from Koszulness|textbf}
\index{Koszul property!bootstrap closure|textbf}
Let $\cA$ be a chirally Koszul chiral algebra. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The Maurer--Cartan moduli $\MC(\gAmod)$ is discrete
 \textup{(}zero-dimensional\textup{)}: the MC element
 $\Theta_\cA$ is the unique solution, determined by the
 genus-$0$ OPE data.
\item The shadow depth $r_{\max}(\cA)$ equals the bootstrap
 closure order: the number of OPE channels at which the
 crossing equation
 $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at degree
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:bar-cobar-isomorphism-main\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3639:\label{thm:bar-cobar-isomorphism-main}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3580,3705p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{proposition}[Cumulant-to-window inversion; \ClaimStatusProvedHere]
\label{prop:cumulant-window-inversion}
\index{cumulant-to-window inversion|textbf}
\index{primitive cumulant spectrum!recovery from windows}

The cumulant law is invertible: from the window counts
$(h_1, h_2, \ldots)$ one recovers the hidden primitive spectrum
$(g_1, g_2, \ldots)$ by the recursion
\begin{equation}
\label{eq:cumulant-window-inversion}
g_1 = h_1, \qquad
g_q \;=\; h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r}
\qquad (q \geq 2).
\end{equation}
\end{proposition}

\begin{proof}
The identity $H_\cA = G_\cA/(1 - G_\cA)$ is equivalent to
thinking
**Organizing theorem searches**

I'm realizing that my search outputs are quite vast, so I need to focus on the theorem statements and proofs. I think I might need exact line numbers for clarity. Using commands like sed or rg should help navigate through the details more effectively. I see I need to manually identify theorem labels and proof environments for the entries A-D+H. I suspect that both higher_genus_complementarity and bar_cobar_adjunction_inversion might require close inspection, especially since they seem interconnected.
thinking
**Evaluating theorem conditions**

I'm questioning whether inconsistency might relate to the ClaimStatusProvedHere since the theorem has a conditional aspect tied to axiom MK:modular. I need to check the actual statement and proof for thm:higher-genus-inversion as well as the referenced axiom. It's important to determine if the theorem is marked as proved, conditional, or indicated elsewhere. For the files, I’ll be looking around 3400 for higher_genus_complementarity and 5298 for higher_genus_foundations to see if proofs are circular and align with status claims in the metadata. I'm ready to dig in!
thinking
**Assessing proof limitations**

I'm realizing we can't entirely prove or disprove all large theorems, even though the mission leans towards falsification. It might be helpful to leverage existing audit notes, but the user emphasized grounding in the actual file contents and tool outputs that I personally reviewed. While those audit notes are indeed based on file contents, I probably should prioritize using live sources over just relying on past notes. It's crucial to provide the most accurate information possible!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,3730p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3600	$G_\cA = H_\cA/(1 + H_\cA)$, or at the level of formal power
  3601	series,
  3602	\[
  3603	G_\cA(t) \;=\; H_\cA(t) - G_\cA(t)\,H_\cA(t).
  3604	\]
  3605	Extracting the coefficient of $t^q$ gives
  3606	$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
  3607	since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
  3608	follows by induction on~$q$.
  3609	\end{proof}
  3610	
  3611	\begin{remark}[The primitive defect as a Koszulness probe]
  3612	\label{rem:primitive-defect-probe}
  3613	\index{primitive defect series!Koszulness probe}
  3614	
  3615	For a quadratic chiral algebra $\cA$ with generators of
  3616	weights $d_1, \ldots, d_s$, the PBW basis ensures that all
  3617	quasi-primaries are generated by the declared strong generators,
  3618	so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
  3619	Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
ERROR: exceeded retry limit, last status: 429 Too Many Requests, request id: 282a0f61-9b54-4c0f-bf41-6a67a19aadd6
codex
I have the main theorem labels. Next I’m reading the live theorem blocks and the cross-volume summary surfaces line-for-line so I can separate real status drift from mere paraphrase.
exec
/bin/zsh -lc "rg -n --files /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '/(README["'^/]*|metadata/.+|chapters/connections/concordance'"\\.tex)"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/README.md
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
/Users/raeez/calabi-yau-quantum-groups/README.md
/Users/raeez/chiral-bar-cobar/metadata/verified_formulas.jsonl
/Users/raeez/chiral-bar-cobar/metadata/census.json
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md
/Users/raeez/chiral-bar-cobar/metadata/label_index.json
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
/Users/raeez/chiral-bar-cobar/README.md
collab wait(call_CW4faq4o3XgoDCpz8kXlqhZU)
  receivers: 019d83b3-2d68-7e82-a665-8535448aca79
wait(call_CW4faq4o3XgoDCpz8kXlqhZU) 1 agents complete:
  019d83b3-2d68-7e82-a665-8535448aca79 completed
ERROR: exceeded retry limit, last status: 429 Too Many Requests, request id: cae5e2ea-4178-4da5-8e64-a88b422055b5
tokens used
98,053
