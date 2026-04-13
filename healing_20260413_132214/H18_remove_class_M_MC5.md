# H18_remove_class_M_MC5 (328s)



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
session id: 019d86b7-351f-7381-b5b8-62ee73787e4b
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.

CRITICAL SESSION CONTEXT (factor this in):
This session deployed 537+ Codex agents across 7 campaigns. The following has ALREADY been done:
- Theorems A-D, H: proof architecture rectified. Verdier convention fixed (Thm A), off-locus
  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
  separated + reflexivity from perfectness (Thm C1), center-to-bar lift proved (Thm C2),
  circularity broken with routing remark (Thm D).
- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
- Topologization: split into cohomological (proved KM) + chain-level (conjectural).
- Koszul equivs (vii)/(viii): scope narrowed to match proofs.
- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
- 48 new anti-patterns catalogued (AP186-AP224).
- Wave A: broken refs, hardcoded Parts, duplicate labels, status mismatches, proof-after-conj
  all fixed across Vol I and Vol II.
- New compute engines: critical level (72 tests), Verlinde polynomial (g=0..6),
  genus-2 decomposition, chiral bialgebra, tetrahedron, and 20+ more.
- Vol I ~2,719pp (29 commits this session), Vol II ~1,681pp (15 commits), Vol III ~319pp (19 commits).

READ the current state of files on disk — they reflect ALL the above work.
Your job: HEAL remaining wounds, provide ALTERNATIVE proofs, UPGRADE strength.

Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


RESEARCH: Chain-level BV/bar for class M.

TARGET: chapters/connections/bv_brst.tex (add Research Remark)

MC5 chain-level is FALSE for class M (Virasoro). The coderived result holds.

INVESTIGATE:
1. WHY does chain-level fail for class M? The infinite shadow tower means infinitely
   many non-zero A-inf operations; the BV complex cannot capture them all at chain level.
2. Is there a SPECTRAL version of MC5 that works for class M? (A spectral sequence
   from the shadow tower filtration converging to the BV complex.)
3. What is the BEST chain-level statement? Perhaps: BV ≅ bar in a COMPLETED category
   (pro-completion by shadow tower degree)?
4. Can the coderived result be STRENGTHENED to something between coderived and chain-level?

Write a Research Remark with the spectral and completed approaches.
mcp startup: no servers
codex
Using `frontier-research` for the new class-M research remark, and `multi-path-verify` for the MC5/coderived-vs-chain-level claim surface. First step is to read the constitutional files and the live `bv_brst.tex` surface, then locate every current MC5/class-M reference before drafting.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 succeeded in 52ms:
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
**Locating research materials**

I need to read the exact file, along with the frontier-research skill instructions. I think it's important to open the right skill files and follow their content. I should inspect the target files and references, possibly using the explorer or rg for better searching. It might be a good idea to spawn an explorer agent to find the relevant sections in bv_brst.tex and related files like editorial constitution and w-algebras. I want to conduct a precise search.
codex
The live surface is large enough that I’m splitting the search: one pass for the exact `bv_brst.tex` insertion point, one pass for all MC5/class-M references that constrain the wording. After that I’ll lock the claim surface and draft the research remark against the current proofs rather than old session state.
collab spawn_agent(call_gobcTbA9G1jTEWwUi5IJcFB5, prompt="Locate the exact MC5 / class M / BV-bar discussion in chapters/connections/bv_brst.tex and nearby labels/remarks. Report…")
spawn_agent(call_gobcTbA9G1jTEWwUi5IJcFB5, prompt="Locate the exact MC5 / class M / BV-bar discussion in chapters/connections/bv_brst.tex and nearby labels/remarks. Report…") pending init:
  agent: 019d86b7-cb18-74c3-ae61-2e7ae3e09dd2
mcp startup: no servers
collab spawn_agent(call_qB5vJfDsUmeSE2A1D7f8xVsb, prompt="Search the repo for MC5, chain-level BV/bar equivalence, coderived result, class M, Virasoro, shadow tower filtration, c…")
spawn_agent(call_qB5vJfDsUmeSE2A1D7f8xVsb, prompt="Search the repo for MC5, chain-level BV/bar equivalence, coderived result, class M, Virasoro, shadow tower filtration, c…") pending init:
  agent: 019d86b7-cbfb-7ce3-b6f8-04068a449ae7
mcp startup: no servers
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/frontier-research/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
 succeeded in 51ms:
---
name: frontier-research
description: Use for new theorem architecture, research synthesis, or frontier programme design. Keep work local by default. Delegate or swarm only when the user explicitly authorizes it. This is the Codex-native equivalent of the frontier and research-swarm workflows from `CLAUDE.md`.
---

# Frontier Research

Frontier work is allowed only after the proved core, the conditional bridge, and the conjectural extension are separated sharply.

## Workflow

1. Partition the topic into:
   proved core,
   compute-backed evidence,
   conditional bridge,
   conjectural extension,
   heuristic picture.
2. Read the live theorem surface before synthesizing new structure.
3. Name the exact blocker for every missing implication.
4. Prefer the strongest narrower programme statement that survives hostile rereading.
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

exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'rg -n "MC5" -n "class M" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: class M: No such file or directory (os error 2)
chapters/connections/bv_brst.tex:2201:of MC5: construct a class~$\mathsf{M}$ filtration for which the
chapters/connections/bv_brst.tex:2500:the higher-genus MC5 comparison between the handle-gluing BRST
chapters/connections/bv_brst.tex:2532:$bc$ ghosts gives the MC5 genus-$0$ case proved in
exec
/bin/zsh -lc 'rg -n "MC5"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2002

healing_20260413_132214/H07_MC5_alt_approach.md:1:# H07_MC5_alt_approach (288s)
healing_20260413_132214/H07_MC5_alt_approach.md:3:Updated [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2029). The operadic remark now states the alternative MC5 route in the corrected two-colour form: `\Delta_{\mathrm{BV}}` is the closed-colour Swiss-cheese contraction, `d_{\bar B}` is the open-colour coderivation, the relevant `SC^{\mathrm{ch,top}}` object is the pair `\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA\bigr)` rather than `B(A)` itself, the coderived comparison is presented as the coloured Koszul bar-cobar correspondence, and the class `\mathsf{M}` chain-level gap is isolated as non-formality of the explicit transferred model rather than a failure of coderived duality.
healing_20260413_132214/H07_MC5_alt_approach.md:5:Verification: I ran `latexmk -pdf main.tex`. The build progressed past `bv_brst.tex`; it then failed on an unrelated pre-existing error at [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1890) (`\E_2` undefined control sequence), with many existing undefined refs/citations elsewhere. I also checked propagation: no live Vol II/III TeX duplicate of this operadic MC5 remark required synchronized edits.
healing_20260413_132214/H07_MC5_alt_approach.md:47:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H07_MC5_alt_approach.md:100:MC5 — ALTERNATIVE APPROACH to BV/bar identification.
healing_20260413_132214/H07_MC5_alt_approach.md:124:I need to follow instructions for codebase questions, so I’ll start with the explorer. It's important to locate relevant sections and dependencies effectively. Since this is a math manuscript intertwined with code, using the explorer over a manual search makes sense. I’ll ask the explorer to find target locations and constraints related to existing proofs like MC5. I could even consider reading files directly with exec_command, but I need to ensure I'm careful with how I proceed.
healing_20260413_132214/H07_MC5_alt_approach.md:130:I’m treating this as a local fortification pass on `chapters/connections/bv_brst.tex`. First I’m loading the required constitutional files and the live MC5 surface, then I’ll draft an alternative-proof remark that stays compatible with the repo’s corrected `SC^{ch,top}`/bar-center conventions instead of reintroducing the known forbidden conflations.
healing_20260413_132214/H07_MC5_alt_approach.md:226:I need to archive the red_team_summary due to a missing path. I’ll read the full target file and consider any relevant dependencies. I might need to use an explorer, though I’m unsure if I should opt for cross-volume skills. It could help to read the target file around the MC5 section and check for any existing remarks. I’ll also use rg for MC5 or BV/bar identification and look for the exact theorem label. Let's proceed with that!
healing_20260413_132214/H07_MC5_alt_approach.md:232:/bin/zsh -lc "rg -n \"MC5|BV|bar identification|coderived|harmonic|Swiss|Koszul dual|SC\\"'^'"\\{ch,top\\}|BV/bar\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_132214/H07_MC5_alt_approach.md:348:/bin/zsh -lc "rg -n \"thm:bv-bar-coderived|rem:bv-bar-coderived-operadic|MC5|standard-tower-mc5|harmonic decoupling|chain-level gap for class~\\\\mathsf\\{M\\}\" chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H07_MC5_alt_approach.md:351:    (?:thm:bv-bar-coderived|rem:bv-bar-coderived-operadic|MC5|standard-tower-mc5|harmonic decoupling|chain-level gap for class~\mathsf\{M\})
healing_20260413_132214/H07_MC5_alt_approach.md:479:I need to inspect the theorem thm:bv-bar-coderived and ensure I understand the full proof. It’s important to find the right context for any alternative remarks I want to make. I might also want to explore if there's a claim surface in the editorial constitution MC5. This sounds like a worthwhile search, especially to gather relevant insights. Let’s see what I can uncover to support my understanding!
healing_20260413_132214/H07_MC5_alt_approach.md:484:/bin/zsh -lc "rg -n 'MC5|mc5|BV/bar identification|coderived BV/bar|standard-tower-mc5|master-bv-brst' chapters/connections/editorial_constitution.tex chapters/connections/bv_brst.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H07_MC5_alt_approach.md:508:chapters/theory/poincare_duality_quantum.tex:1271:itself is downstream MC5.
healing_20260413_132214/H07_MC5_alt_approach.md:512:chapters/theory/en_koszul_duality.tex:3282:\textup{(}see the MC5 status in the concordance\textup{)}.
healing_20260413_132214/H07_MC5_alt_approach.md:513:chapters/theory/bar_cobar_adjunction_inversion.tex:4333:\item \textbf{MC5}: does the physical logarithm (BRST) equal the
healing_20260413_132214/H07_MC5_alt_approach.md:514:chapters/theory/nilpotent_completion.tex:1265:\item \emph{Only then return to MC5.}
healing_20260413_132214/H07_MC5_alt_approach.md:515:chapters/theory/nilpotent_completion.tex:1267: $\text{MC3} \Rightarrow \text{MC4} \Rightarrow \text{MC5}$
exec
/bin/zsh -lc "sed -n '2150,2350p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
into the differential via a Maurer--Cartan twist), and different
choices produce inequivalent chain complexes. The coderived
category avoids this choice. By
Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
curved objects are not set to zero in this localization; the
comparison map of Theorem~\ref{thm:bv-bar-coderived} becomes an
isomorphism precisely because its cone is coacyclic.

The upshot: the BV quantisation of the worldsheet sigma model
and the algebraic bar construction of the boundary vertex algebra
live naturally in the same curved homological framework. The
chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
signal that the coderived category is unnecessary; it is the reason
the coderived category is the correct ambient. What remains open is
the filtered-completed refinement in class~$\mathsf{M}$
\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
\end{remark}

\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
exec
/bin/zsh -lc 'rg -n "coderived" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
32:all-genera coderived comparison of
33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
1853:Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
1861:curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
1862:class~$\mathsf{M}$ BV and bar models in the coderived category even
1900: & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
1909:powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
1917:\begin{theorem}[BV$=$bar in the coderived category;
1919:\label{thm:bv-bar-coderived}%
1920:\index{BV algebra!bar complex identification!coderived category|textbf}%
1921:\index{coderived category!BV/bar identification|textbf}%
1996:becomes an isomorphism in the coderived quotient
2003:of Definition~\ref{def:coderived-fact}. This is the required
2004:coderived comparison. The provisional localization is not needed
2008:\begin{remark}[Harmonic mechanism behind the coderived comparison]
2009:\label{rem:bv-bar-coderived-higher-genus}%
2010:\index{coderived category!higher-genus validity}%
2014:Theorem~\ref{thm:bv-bar-coderived}. The proof has two inputs:
2032:\label{rem:bv-bar-coderived-operadic}%
2036:Theorem~\ref{thm:bv-bar-coderived}. By
codex
I have the chapter opening. Next I’m reading the exact theorem/remark lane around `thm:bv-bar-coderived` and the surrounding class-`M` discussion, because the new remark has to agree with those statements and not accidentally re-open a closed scope decision.
exec
/bin/zsh -lc "sed -n '260,620p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,1040p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:bv-bar-coderived|MC5|class.?M|Virasoro|shadow tower|completed|coderived|chain-level|harmonic decoupling|Research Remark|remark" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Phi$ can be described concretely in low degrees:
\begin{itemize}
\item \emph{Degree~$0$}: $\Phi(|0\rangle) = 1 \in \barB^0$.
 A BRST-closed state of ghost number~$0$ maps to the unit in
 the bar complex.
\item \emph{Degree~$1$}: $\Phi(c_1 \alpha_{-1}^i |0\rangle)
 = [\alpha^i] \in \barB^1$, where $\alpha^i$ are the Heisenberg
 generators. The physical vertex operators (momentum eigenstates)
 map to bar generators.
\item \emph{Degree~$2$}: $\Phi(c_0 c_1 |0\rangle) = \eta_{12}$,
 where $\eta_{12} = d\log(z_1 - z_2)$ is the FM propagator.
 The ghost bilinear maps to the logarithmic form on the
 configuration space. This is the ghost--propagator identification.
\end{itemize}
In general, ghost insertions $c_{n_1} \cdots c_{n_k}$ map to
products of logarithmic forms $\eta_{i_1 j_1} \wedge \cdots \wedge
\eta_{i_r j_r}$ on the configuration space, with the precise
correspondence determined by the residue map of the FM propagator.
\end{remark}

 succeeded in 51ms:
\frac{\partial}{\partial \eta_{ij}}
\]
inserts a diagonal residue, contracting the logarithmic form $\eta_{ij}$ via a
delta-function along $D_{ij}$. This is the loop-insertion operator in the bar
complex, distinct from the cobar functor $\Omega$ (which recovers $\cA$ from
$B(\cA)$ by bar-cobar inversion, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
The precise algebraic version of this operator is conditional
\textup{(}Theorem~\ref{thm:config-space-bv}\textup{)}.
\end{definition}

\begin{remark}[Heuristic QME/MC comparison; \ClaimStatusHeuristic]
\label{rem:qme-bar-cobar}
\index{quantum master equation|textbf}
At genus~$0$, the classical part of the BV master equation matches the
square-zero bar differential after transporting through the external
comparison of Theorem~\ref{thm:bv-bar-geometric}. Extending this to a
full identification of the quantum master equation
\[
\hbar\,\Delta_{\mathrm{BV}}S + \tfrac{1}{2}\{S,S\}=0
\]
 succeeded in 52ms:
23:on the total Virasoro central charge of matter plus ghosts. Do
32:all-genera coderived comparison of
33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
35:$\mathsf{L}$, and~$\mathsf{C}$ admit stronger chain-level statements
39:coacyclic. The stronger chain-level statement is unconditional for
41:class~$\mathsf{C}$ on harmonic decoupling, and open for
53:chain-level identification breaks: the cross-channel term in the
55:harmonic decoupling is assumed, and class~$\mathsf{M}$ is precisely
58:\begin{remark}[BRST anomaly brackets and transferred SC operations]
73:\end{remark}
75:\begin{remark}[BV/bar dictionary; \ClaimStatusHeuristic]
92:The chain-level identifications (antifields versus
98:Theorem~\ref{thm:genus-universality} and, for Virasoro, of
101:chain-level equalities.
102:\end{remark}
104:\begin{remark}[Heuristic BV reading of the modular MC hierarchy]
117:in the completed cyclic deformation Lie algebra
154:\end{remark}
156:\begin{remark}[String field theory interpretation]
166:\end{remark}
exec
/bin/zsh -lc "sed -n '1890,2270p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\toprule
Class & Status on current record & Comment \\
\midrule
$\mathsf{G}$ \textup{(}Heisenberg\textup{)}
 & chain-level curved equivalence & no interaction vertices \\
$\mathsf{L}$ \textup{(}affine KM\textup{)}
 & chain-level curved equivalence & Jacobi kills the cubic harmonic term \\
$\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
 & chain-level under harmonic decoupling & composite free-field factorization \\
$\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
 & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
\bottomrule
\end{tabular}
\end{center}
For class~$\mathsf{M}$, the quartic discrepancy
$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
\kappa / \operatorname{Im}(\tau)$ is not a coboundary
in the ordinary chain complex. Proposition~\ref{prop:chain-level-three-obstructions}
shows that the full harmonic discrepancy is a sum of curvature
powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2160,2425p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2160	live naturally in the same curved homological framework. The
  2161	chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
  2162	signal that the coderived category is unnecessary; it is the reason
  2163	the coderived category is the correct ambient. What remains open is
  2164	the filtered-completed refinement in class~$\mathsf{M}$
  2165	\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
  2166	all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
  2167	\end{remark}
  2168	
  2169	\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
  2170	\label{rem:bv-bar-class-m-frontier}
  2171	\index{BV algebra!class M frontier|textbf}%
  2172	\index{coderived category!filtered-completed refinement}%
  2173	Theorem~\ref{thm:bv-bar-coderived} and
  2174	Proposition~\ref{prop:chain-level-three-obstructions} already isolate
  2175	the exact failure mechanism for class~$\mathsf{M}$. The quartic
  2176	harmonic discrepancy is not a coboundary in the ordinary chain
  2177	complex, and the higher discrepancies satisfy
  2178	\[
  2179	\delta_r^{\mathrm{harm}}
exec
/bin/zsh -lc 'rg -n "shadow tower" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2470,2585p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2470	Proposition~\ref{prop:km-generic-acyclicity} place $V_k(\fg)$ on the
  2471	chirally Koszul locus. On the BRST side, the associated graded
  2472	differential is the Chevalley--Eilenberg differential~$d_{\mathrm{CE}}$
  2473	of the current Lie algebra $\widehat{\fg}_{k,-}$ acting on the
  2474	vacuum module. On the bar side, the associated graded differential
  2475	is extracted from the simple-pole current OPE bracket
  2476	$J^a(z) J^b(w) \sim k\,\Omega^{ab}/(z-w) + f^{ab}{}_c J^c(w)/(z-w)$,
  2477	which is the same bracket that defines~$d_{\mathrm{CE}}$.
  2478	The filtered comparison therefore lifts the Chevalley--Eilenberg
  2479	identification to the full genus-$0$ complexes.
  2480	
  2481	\emph{Step~3: Degree propagation.}
  2482	Since $V_k(\fg)$ is chirally Koszul at generic level, the bar spectral
  2483	sequence collapses on the Koszul line and each finite-length summand of
  2484	$T^c(s^{-1}\overline{V_k(\fg)})$ is generated by the binary residue
  2485	bracket and its iterates. The genus-$0$ BRST/bar identification
  2486	propagates from the binary comparison to every finite degree $n \geq 3$.
  2487	\end{proof}
  2488	
  2489	\begin{conjecture}[All-genera WZW BRST/bar identification at generic level;
exec
/bin/zsh -lc "rg -n \"class~\\\\mathsf\\{M\\}\"" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:class~\mathsf\{M\})
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'class~\\\\mathsf\\{M\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "completed" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
117:in the completed cyclic deformation Lie algebra
1235: (MC4 closed; Vol~I Theorem~\ref{thm:completed-bar-cobar-strong}).
1864:uncompleted models.
1912:the filtered-completed refinement for class~$\mathsf{M}$
2164:the filtered-completed refinement in class~$\mathsf{M}$
2172:\index{coderived category!filtered-completed refinement}%
2188:class~$\mathsf{M}$ on the explicit uncompleted models: one is not
2207:The best chain-level statement is likely completed rather than strict.
2209:Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
2212:$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
2229:stronger filtered-completed statement. One can ask that
2238:passage. At present this filtered-completed refinement is the most
exec
/bin/zsh -lc 'rg -n "Virasoro" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
23:on the total Virasoro central charge of matter plus ghosts. Do
98:Theorem~\ref{thm:genus-universality} and, for Virasoro, of
462:where $L^{\cA}_n$ are the Virasoro modes of~$\cA$ and $b_n, c_n$ are
751:the Virasoro branch where $\kappa + \kappa' = 13$\textup{)}.
774:\emph{not} self-dual under the Virasoro self-duality locus
775:$c = 13$ \textup{(}Virasoro self-dual at
849:\emph{not} the Virasoro self-duality at $c = 13$
911:semi-infinite cohomology of the Virasoro algebra \emph{does}
1020:semi-infinite complex of the Virasoro algebra acting on~$\mathcal{H}^{26}$;
1062:duality is level-negating; it fails for Virasoro, where
1169:\begin{corollary}[Virasoro bar complex = semi-infinite complex;
1172:\index{semi-infinite cohomology!Virasoro}
1173:\index{Virasoro algebra!semi-infinite cohomology}
1174:For the Virasoro algebra $\mathrm{Vir}_c$ at central charge
1182:where $M_c$ is the vacuum Virasoro module. The Motzkin-number
1212:level-independent constant: $13$ for Virasoro and $250/3$ for
1227:\textup{(}Virasoro\textup{)}: the Virasoro at
1715: \textup{(}Virasoro, $\cW_N$\textup{)}:
1840: For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
1899:$\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
codex
**Class M/BV-bar surface**  
- `chapters/connections/bv_brst.tex:2160-2239` hosts `Remark  rem:bv-bar-class-m-frontier`: it isolates the MC5 failure for class~$\mathsf{M}$ (line 2173 onward), states that the quartic harmonic discrepancy is nontrivial and proliferates via the permanent cubic source, then proposes a spectral-bar filtration (lines 2192‑2205) whose higher differentials should capture the $c_r(\cA)$ obstruction classes and converge to a coacyclic cone, and finally argues that only a completed-weight comparison (lines 2207‑2238) can plausibly yield a chain-level statement stronger than the bare coderived equivalence.  

**MC5 mention and nearby claims**  
- `chapters/connections/bv_brst.tex:2490-2502` covers `Conjecture  rem:conj:wzw-brst-bar-all-genera`: it frames the higher-genus MC5 comparison between the handle-gluing BRST operator and the modular bar bar differential, declaring the all-genera BRST/bar identification at generic level open beyond genus 0.  

**Best insertion point for new research remark**  
- Immediately after `Remark rem:bv-bar-class-m-frontier` (before `\section{Non-Calabi--Yau local surfaces…}` at lines 2240‑2242) is the cleanest spot. The surrounding text already frames the filtered-completed/class~$\mathsf{M}$ failure and the need for spectral filtration + completion, so a new remark there could build directly on the MC5-class~$\mathsf{M}$ narrative, spell out the desired spectral shadow-tower filtration, and sketch how completed-category replacements (continuous $\widehat f_g$) would absorb the infinite obstruction tower.

thinking
**Identifying cross-volume references and key sections**

I'm gathering relevant lines on Virasoro context and shadow towers, noting key terms like completed categories and models. I'll search the repo for cross-volume duplicates related to BV constructions, focusing on mentions in other volumes to address the user's request thoroughly.
exec
/bin/zsh -lc 'rg -n "bv-bar-coderived"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1596

healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
CLAUDE.md:508:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
healing_20260413_132214/H08_topol_alt_proof.md:620:  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
healing_20260413_132214/H07_MC5_alt_approach.md:8:For `thm:bv-bar-coderived`:
healing_20260413_132214/H07_MC5_alt_approach.md:15:For `thm:bv-bar-coderived` upgrade status:
healing_20260413_132214/H07_MC5_alt_approach.md:283:33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
healing_20260413_132214/H07_MC5_alt_approach.md:345:\label{rem:bv-bar-coderived-higher-genus}%
healing_20260413_132214/H07_MC5_alt_approach.md:348:/bin/zsh -lc "rg -n \"thm:bv-bar-coderived|rem:bv-bar-coderived-operadic|MC5|standard-tower-mc5|harmonic decoupling|chain-level gap for class~\\\\mathsf\\{M\\}\" chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H07_MC5_alt_approach.md:351:    (?:thm:bv-bar-coderived|rem:bv-bar-coderived-operadic|MC5|standard-tower-mc5|harmonic decoupling|chain-level gap for class~\mathsf\{M\})
healing_20260413_132214/H07_MC5_alt_approach.md:479:I need to inspect the theorem thm:bv-bar-coderived and ensure I understand the full proof. It’s important to find the right context for any alternative remarks I want to make. I might also want to explore if there's a claim surface in the editorial constitution MC5. This sounds like a worthwhile search, especially to gather relevant insights. Let’s see what I can uncover to support my understanding!
healing_20260413_132214/H07_MC5_alt_approach.md:487:\label{thm:bv-bar-coderived}%
healing_20260413_132214/H07_MC5_alt_approach.md:520:chapters/theory/introduction.tex:2055:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
healing_20260413_132214/H07_MC5_alt_approach.md:549:scope: chapters/connections/bv_brst.tex, rem:bv-bar-coderived-operadic
healing_20260413_132214/H07_MC5_alt_approach.md:550:target theorem: thm:bv-bar-coderived
healing_20260413_132214/H07_MC5_alt_approach.md:600: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H07_MC5_alt_approach.md:652: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H07_MC5_alt_approach.md:704: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H07_MC5_alt_approach.md:719:\label{rem:bv-bar-coderived-operadic}%
exec
/bin/zsh -lc "sed -n '1620,2255p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\lambda_3^{\mathrm{FP}} = 31/967680$.
\textup{(}Verified in the compute layer:
\texttt{heisenberg\_bv\_bar\_proof.py}, $60$ tests.\textup{)}
\end{proof}

\begin{remark}[Why the Heisenberg is special]
\label{rem:heisenberg-bv-bar-scope}
\index{BV algebra!bar complex identification!scope}
Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
\textup{(}partition function\slash free energy\textup{)} for the
Heisenberg family at all genera.
The Heisenberg succeeds because it is class~G:
a single Gaussian channel, no interaction vertices, and
all moduli dependence controlled by the Quillen anomaly.
For non-free theories, the scalar identification requires
the shadow obstruction tower machinery
\textup{(}Theorem~D for uniform-weight algebras;
the multi-weight genus expansion for $W_N$\textup{)}.

collab wait(call_TEipij6nP10MFqUzcDHR2GtT)
  receivers: 019d86b7-cb18-74c3-ae61-2e7ae3e09dd2, 019d86b7-cbfb-7ce3-b6f8-04068a449ae7
wait(call_TEipij6nP10MFqUzcDHR2GtT) 1 agents complete:
  019d86b7-cb18-74c3-ae61-2e7ae3e09dd2 completed: "**Class M/BV-bar surface**  
- `chapters/connections/bv_brst.tex:2160-2239` hosts `Remark  rem:bv-bar-class-m-frontier`:…"

thinking
**Identifying cross-volume references and duplicates**

I'm focusing on locating precise file paths and line ranges in Volume I that mention key terms like MC5, chain-level BV/bar equivalence, coderived results, class M, Virasoro, shadow tower filtration, and related concepts. I’ll also check for duplicates that appear in Volume II or the concordance files, highlighting cross-volume overlaps and referencing exact line numbers instead of aggregators, making it easier to pinpoint where to align new research remarks.
exec
/bin/zsh -lc 'rg -n "rem:bv-bar-class-m-frontier" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:1913:\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
chapters/connections/bv_brst.tex:2165:\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
chapters/connections/bv_brst.tex:2170:\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1130:I need to pick a new, unique label, possibly something like `rem:bv-bar-class-m-research` or `rem:bv-bar-class-m-frontier`. I want to make sure it’s distinctive. I think using a simple command with the path `/Users` would work well, but I might need to wait for the explorer's results before finalizing anything. Let’s keep it straightforward and see what the explorer reveals!
healing_20260413_130533/H18_remove_class_M_MC5.md:1235:label: \label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1247:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1333:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1419:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1523:  2167	\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1526:/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-class-m-frontier\\}|\\\\ref\\{prop:chain-level-three-obstructions\\}|\\\\ref\\{cor:virasoro-postnikov-nontermination\\}|\\\\ref\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\ref\\{prop:standard-strong-filtration\\}|\\\\ref\\{thm:completed-bar-cobar-strong\\}|\\\\ref\\{def:curved-weak-equiv\\}|\\\\ref\\{def:provisional-coderived\\}' chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
healing_20260413_130533/H18_remove_class_M_MC5.md:1550:/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-class-m-frontier\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_130533/H18_remove_class_M_MC5.md:1551:/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2167:\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1562:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1661:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1752:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1864:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:1982:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:2003:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:2097:+\label{rem:bv-bar-class-m-frontier}
healing_20260413_130533/H18_remove_class_M_MC5.md:2213:+\label{rem:bv-bar-class-m-frontier}
exec
/bin/zsh -lc 'rg -n "bv-bar-coderived" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
721: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
1987: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
3381: (Theorem~\ref{thm:bv-bar-coderived});
7068: (Theorem~\ref{thm:bv-bar-coderived});
7745: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
9832: \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
10229: (Theorem~\ref{thm:bv-bar-coderived}):
11157: Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
11278: (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
codex
The main theorem lane is now clear. There is already a frontier remark, but it is still too coarse for your target: it says “spectral replacement” and “completed refinement” without explaining why class `M` fails or what the intermediate strengthened statement should be. I’m now tightening that specific remark rather than creating a disconnected new lane.
collab wait(call_UATkqSsOo8Eztw8B8A8mXuXe)
  receivers: 019d86b7-cbfb-7ce3-b6f8-04068a449ae7
exec
/bin/zsh -lc 'rg -n "V1-thm:bv-bar-coderived" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
relaunch_wave2_empties/S16_v1_to_v2_bridge.md:472:\phantomsection\label{V1-thm:bv-bar-coderived}%
relaunch_wave2_empties/S16_v1_to_v2_bridge.md:866:   144	W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
fix_wave_A_20260413_112727/A20_fix_broken_refs_v2.md:528:7	OK	chapters/connections/3d_gravity.tex:283	V1-thm:bv-bar-coderived
wave2_audit_20260413_001942/B06_MC_bridge.md:424:  1595	ef*{V1-thm:bv-bar-coderived}); the genuswise
wave2_audit_20260413_001942/B06_MC_bridge.md:888:   144	W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
platonic_rectification_20260413_114523/P17_concordance_sync.md:1481:wave2_audit_20260413_001942/B06_MC_bridge.md:424:  1595	ef*{V1-thm:bv-bar-coderived}); the genuswise
platonic_rectification_20260413_114523/P17_concordance_sync.md:1483:wave2_audit_20260413_001942/B06_MC_bridge.md:888:   144	W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
relaunch_20260413_111534/S16_v1_to_v2_bridge.md:331:\phantomsection\label{V1-thm:bv-bar-coderived}%
audit/vol2_chapters_unresolved_refs_report.md:278:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:283 — PROBLEM: `ref{V1-thm:bv-bar-coderived}` resolves only through the naked alias `\phantomsection\label{V1-thm:bv-bar-coderived}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:600` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:bv-bar-coderived}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:600` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
audit/vol2_chapters_unresolved_refs_report.md:335:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:950 — PROBLEM: `ref{V1-thm:bv-bar-coderived}` resolves only through the naked alias `\phantomsection\label{V1-thm:bv-bar-coderived}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:600` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:bv-bar-coderived}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:600` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
healing_20260413_130533/H07_MC5_alt_approach.md:927:/Users/raeez/chiral-bar-cobar-vol2/main.tex:600:\phantomsection\label{V1-thm:bv-bar-coderived}%
healing_20260413_130533/H07_MC5_alt_approach.md:931:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:283:(Volume~I, Theorem~\ref{V1-thm:bv-bar-coderived}).
healing_20260413_130533/H07_MC5_alt_approach.md:933:/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1595:ef*{V1-thm:bv-bar-coderived}); the genuswise
healing_20260413_130533/H07_MC5_alt_approach.md:934:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:950: \ref{V1-thm:bv-bar-coderived} \\
healing_20260413_130533/H07_MC5_alt_approach.md:936:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:144:W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
healing_20260413_130533/H07_MC5_alt_approach.md:937:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:393:The analytic lane of MC5 is therefore proved at all genera; BV=bar in the coderived category is proved for all shadow classes (Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false).
healing_20260413_130533/H07_MC5_alt_approach.md:938:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:522: (Vol~I, Theorem~\ref*{V1-thm:bv-bar-coderived});
healing_20260413_130533/H07_MC5_alt_approach.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 149395)

thinking
**Compiling research references with line numbers**

I'm gathering detailed line ranges and file references for key topics like MC5, chain-level BV/bar equivalence, coderived results, and the shadow tower filtration, focusing on chapters/connections/bv_brst.tex and related files. I plan to highlight cross-volume duplicates with Vol II aliases, noting precise lines around important propositions, remarks, and theorems, including the shadow obstruction tower's non-termination and completed category contexts. I'll format this info clearly to help the user locate relevant sections for adding a new research remark.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1870,2025p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1870	\index{BV algebra!sewing operator identification|textbf}%
  1871	\index{sewing operator!BV Laplacian identification}%
  1872	\index{Bergman kernel!sewing contraction}%
  1873	The identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ at
  1874	the chain level asserts that the BV Laplacian and the bar sewing
  1875	operator agree as $(g,n) \to (g{+}1,n{-}2)$ operations on the
  1876	modular convolution algebra~$\gAmod$: both contract a pair of
  1877	inputs through the Bergman kernel $d\log E(z,w)$ along the
  1878	non-separating boundary divisor
  1879	$\delta^{\mathrm{ns}}\colon
  1880	\overline{\mathcal{M}}_{g,n+2} \to
  1881	\overline{\mathcal{M}}_{g+1,n}$.
  1882	Four complementary descriptions of this comparison
  1883	\textup{(}operator definition, spectral sequence, Heisenberg
  1884	extraction, modular operad\textup{)} lead to the following
  1885	class-by-class obstruction profile on the current written record.
  1886	\begin{center}
  1887	\small
  1888	\renewcommand{\arraystretch}{1.15}
  1889	\begin{tabular}{lcl}
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2030,2225p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2030	
  2031	\begin{remark}[Alternative approach via operadic Koszul duality]
  2032	\label{rem:bv-bar-coderived-operadic}%
  2033	\index{BV algebra!bar complex identification!operadic route}%
  2034	\index{Koszul duality!BV/bar comparison}%
  2035	There is a second route to
  2036	Theorem~\ref{thm:bv-bar-coderived}. By
  2037	Principle~\ref{princ:sc-two-incarnations}, the ordered bar complex
  2038	$\barB^{\mathrm{ord}}(\cA)$ is the open
  2039	$\Eone$-chiral coalgebra engine, while the derived center
  2040	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
  2041	= C^{\bullet}_{\mathrm{ch}}(\cA,\cA)$ is the closed object carrying
  2042	the $\mathsf{SC}^{\mathrm{ch,top}}$ structure. In this two-coloured
  2043	package, the BV operator $\Delta_{\mathrm{BV}}$ is the closed-colour
  2044	contraction induced by the Swiss-cheese pairing, whereas the bar
  2045	differential $d_{\barB}$ is the open-colour coderivation induced by
  2046	the chiral product. The two operators therefore come from the same
  2047	operadic bar-cobar datum, but they live in different colours. What is
  2048	compared is not ``the bar complex as a Swiss-cheese algebra'': the
  2049	Swiss-cheese object is the pair
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2225,2260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2225	inverse limit is continuous. This is the strongest chain-level
  2226	statement presently visible for class~$\mathsf{M}$.
  2227	
  2228	Between ordinary chain level and bare coderived equivalence lies a
  2229	stronger filtered-completed statement. One can ask that
  2230	$\widehat f_g$ be a weak equivalence of filtered curved models in the
  2231	sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
  2232	isomorphism already in the provisional coderived category of
  2233	Definition~\ref{def:provisional-coderived}. This is stronger than
  2234	Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
  2235	filtration and every finite truncation; it is weaker than an ordinary
  2236	chain-level quasi-isomorphism, because it allows the infinite residual
  2237	class~$\mathsf{M}$ discrepancy to die only after filtered coderived
  2238	passage. At present this filtered-completed refinement is the most
  2239	plausible strengthening of the coderived theorem.
  2240	\end{remark}
  2241	
  2242	\section{Non-Calabi--Yau local surfaces and the Burns datum}
  2243	\label{sec:non-cy-local-surfaces}
  2244	\index{Burns space|textbf}

thinking
**Summarizing cross-volume references and key sections**

I’m gathering exact line numbers and snippets to highlight cross-volume duplicates and key references like the shadow obstruction tower, completed complex, and various propositions and theorems. I’ll pinpoint where chain-level remarks appear and check for any cross-volume consistency issues around MC5 in the theory introduction section. This should give the user a clear and detailed map of the interconnected content.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2040,2090p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2040	
  2041	\subsection{Entanglement entropy from the shadow obstruction tower}
  2042	
  2043	At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
  2044	$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).
  2045	
  2046	Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.
  2047	
  2048	Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.
  2049	
  2050	\section{The MC frontier}
  2051	\label{sec:mc-frontier-intro}
  2052	\index{MC frontier|textbf}
  2053	\index{master conjectures}
  2054	
  2055	The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
  2056	
  2057	\begin{center}
  2058	\small
  2059	\begin{tabular}{llll}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '260,305p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   260	terminates by the depth formula
   261	$d' = \lfloor(p-1)/2\rfloor = 0$. For multi-generator algebras at
   262	$p = 2$, the discriminant is the \emph{centrality} of the
   263	double-pole coefficient: if the residue $c_0 = \{a_{(0)} b\}$ is
   264	central (Heisenberg, class~$\mathbf{G}$, depth~$2$) the
   265	$\lambda$-bracket is abelian; if $c_0$ is non-central (affine KM,
   266	class~$\mathbf{L}$, depth~$3$) the Lie bracket generates $m_3
   267	\ne 0$ through the Jacobi identity.
   268	Part~(2): the quartic pole $a_{(3)}a = c/2$ forces
   269	$A_3 \neq 0$ (cf.~\eqref{eq:gravity-associator} below), which
   270	forces $m_3 = -A_3 \neq 0$; the Stasheff identity then forces
   271	$m_4, m_5, \ldots$ in perpetuity.
   272	Part~(3) is the DS transfer theorem
   273	(Theorem~\ref{thm:ds-hpl-transfer}).
   274	\end{proof}
   275	
   276	\begin{remark}[BV/bar identification by shadow class]
   277	\label{rem:bv-bar-by-class}
   278	\index{BV algebra!bar complex identification!by shadow class}
   279	The BV/bar identification
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '930,980p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   930	\subsection{Concrete consequences and open problems}
   931	
   932	The following table compresses the principal results and open problems
   933	arising from the constructions of this volume combined with Volume~I's
   934	five main theorems.
   935	
   936	\begin{center}
   937	\small
   938	\renewcommand{\arraystretch}{1.3}
   939	\begin{tabular}{@{}p{5.8cm}lp{4.0cm}@{}}
   940	\textbf{Result} & \textbf{Status} & \textbf{Location} \\
   941	\hline
   942	Jones polynomial from bar complex integrals
   943	 & Proved
   944	 & Thm~\ref{thm:affine-monodromy-identification},
   945	 Cor~\ref{cor:jones-polynomial} \\
   946	MC5: BV-BRST/bar genus tower
   947	 & Analytic HS-sewing proved (all genera); genus-$0$ algebraic BRST/bar proved; $D^{\mathrm{co}}$-level BV=bar proved (all shadow classes); chain-level conjectural
   948	 & Thms~\ref*{V1-thm:general-hs-sewing},
   949	 \ref{rem:mc5-genus-zero-bridge},
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '560,620p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   560	\phantomsection\label{V1-prop:thqg-VII-genus3}%
   561	\phantomsection\label{V1-prop:thqg-VII-genus4}%
   562	\phantomsection\label{V1-prop:vir-complementarity}%
   563	\phantomsection\label{V1-prop:virasoro-c26-selfdual}%
   564	\phantomsection\label{V1-rem:bcov-mc-dictionary}%
   565	\phantomsection\label{V1-rem:bv-bar-bridge}%
   566	\phantomsection\label{V1-rem:bv-bar-class-c-proof}%
   567	\phantomsection\label{V1-rem:conj-modular-resolved}%
   568	\phantomsection\label{V1-rem:g9-mc-relation}%
   569	\phantomsection\label{V1-rem:g9-wall-crossing}%
   570	\phantomsection\label{V1-rem:lattice:monster-shadow}%
   571	\phantomsection\label{V1-rem:mc3-ordered-bar-bridge}%
   572	\phantomsection\label{V1-rem:sc-higher-genus}%
   573	\phantomsection\label{V1-rem:thqg-I-btz-saddles}%
   574	\phantomsection\label{V1-rem:thqg-I-open-directions}%
   575	\phantomsection\label{V1-rem:thqg-VI-cubic-source}%
   576	\phantomsection\label{V1-rem:thqg-VI-w-infinity}%
   577	\phantomsection\label{V1-rem:thqg-VII-hbar-topology}%
   578	\phantomsection\label{V1-rem:three-r-matrices}%
   579	\phantomsection\label{V1-rem:vir-trichotomy-genera}%
wait(call_UATkqSsOo8Eztw8B8A8mXuXe) timed out:
collab wait(call_xh6x5ilqmZEtBZa3VYhvfJT9)
  receivers: 019d86b7-cbfb-7ce3-b6f8-04068a449ae7

thinking
**Summarizing research references and cross-volume duplicates**

I'll prepare a clear, plain-text final message highlighting key sections in specified files with line references, emphasizing cross-volume duplicates and relevant propositions, including aliases like `V1-thm` in `Vol II`. I'll ensure the summary covers mentions of terms like `MC5`, `coderived result`, and `shadow tower filtration`, follows developer instructions for minimal formatting with bullet points, and states that no editing was done.
codex
- `chapters/connections/bv_brst.tex:1893‑2240` bundles the existing constraints. The obstruction table (1893‑1901) singles out class \(\mathsf{M}\) (Virasoro/\(\mathcal W_N\)) as the lone entry where BV=bar only holds in \(D^{\mathrm{co}}\). The coderived theorem \(thm:bv-bar-coderived\) at 1917‑1956 spells out the \(m_0\)-power torsion mechanism, Proposition \ref{prop:chain-level-three-obstructions}, and the fact that all higher harmonic discrepancies are absorbed only after passing to the coderived quotient. Remarks 2031‑2166 revisit the Swiss-cheese/Koszul route, explain why the curved setting forces \(D^{\mathrm{co}}\), and point to the unresolved filtered‑completed upgrade for class \(\mathsf{M}\). The research remark candidate (2169‑2240) already encodes that the “shadow obstruction tower” never stops for Virasoro/principal \(\mathcal W_N\), proposes a shadow-window/spectral filtration (via Proposition \ref{prop:coderived-bar-degree-spectral-sequence}) whose differentials should record the harmonic classes \(c_r(\cA)\), and raises the weight-completion/completed bar-cobar interplay (Proposition \ref{prop:standard-strong-filtration}, Theorem \ref{thm:completed-bar-cobar-strong}, the continuous maps \(\widehat f_g\), and definitions of filtered weak equivalence/provisional coderived). Any new remark must respect these line numbers and the existing labels \(rem:bv-bar-class-m-frontier\), \(thm:bv-bar-coderived\), and the surrounding spectral/completion references.

- The “MC5 frontier” is cross‑referenced elsewhere in Volume I: see `chapters/theory/introduction.tex:2055‑2067` (MC1–MC5 status table, analytic HS‑sewing proven and coderived BV=bar but the chain-level MC5 remains conjectural) and `chapters/connections/concordance.tex:7745‑7755` (the MC5 column explicitly pointing to \(thm:bv-bar-coderived\), the class \(\mathsf{M}\) failure, and the need for filtered completion). Any remark in `bv_brst.tex` should stay consistent with those higher‑level status statements.

- Cross‑volume touchpoints: Volume II still points readers back to the Volume I result via the alias `V1-thm:bv-bar-coderived` (see `vol2/chapters/connections/3d_gravity.tex:276‑299` and `vol2/chapters/connections/conclusion.tex:936‑955`). The alias itself is defined near `vol2/main.tex:560‑601`. No other volume carries its own version of the `rem:bv-bar-class-m-frontier` research goal, but the forthcoming remark should not contradict these citations—Volume II assumes the coderived statement and class \(\mathsf{M}\) chain‑level failure exactly as stated here.

No files were edited.
wait(call_xh6x5ilqmZEtBZa3VYhvfJT9) 1 agents complete:
  019d86b7-cbfb-7ce3-b6f8-04068a449ae7 completed: "- `chapters/connections/bv_brst.tex:1893‑2240` bundles the existing constraints. The obstruction table (1893‑1901) singl…"
Plan update
Claim surface locked: `chapters/connections/bv_brst.tex`, theorem lane `prop:chain-level-three-obstructions` -> `thm:bv-bar-coderived` -> `rem:bv-bar-class-m-frontier`, with cross-checks in `chapters/theory/introduction.tex` and `chapters/connections/concordance.tex`. I’m tightening the existing class-M frontier remark into a sharper research remark grounded in the current proofs and completion machinery.
  → Read the exact supporting results and status summaries that constrain the class-M MC5 wording
  • Draft a stronger research remark explaining why strict chain level fails for class M and what spectral/completed replacements remain viable
  • Patch `chapters/connections/bv_brst.tex` and sync any necessary status wording in nearby summary surfaces
  • Verify by reread and targeted grep for consistency, labels, and banned prose

thinking
**Searching for supporting results**

I need to find and read the supporting results for my task. It looks like using parallel execution could be helpful here, and I might want to look at the introduction and concordance around the MC5 lines. I think I should also search for exact references. There's quite a bit to keep track of, but gathering all this information will help clarify things. I'll make sure to stay organized while I do this!
exec
/bin/zsh -lc "rg -n \"prop:coderived-bar-degree-spectral-sequence|cor:virasoro-postnikov-nontermination|prop:standard-strong-filtration|thm:completed-bar-cobar-strong|def:provisional-coderived|def:curved-weak-equiv|MC5|bv-bar-coderived|class.\\\\mathsf\\{M\\}|shadow obstruction tower\" chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:prop:coderived-bar-degree-spectral-sequence|cor:virasoro-postnikov-nontermination|prop:standard-strong-filtration|thm:completed-bar-cobar-strong|def:provisional-coderived|def:curved-weak-equiv|MC5|bv-bar-coderived|class.\mathsf\{M\}|shadow obstruction tower)
                                                                                                                                                                                                                                   ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '2038,2088p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7728,7775p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).

\subsection{Entanglement entropy from the shadow obstruction tower}

At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).

Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.

Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.

\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.

\begin{center}
 succeeded in 52ms:
$\dim\operatorname{grt}_1(\text{weight }8) = 1$
\textup{(}from $[\sigma_3, \sigma_5]$\textup{)},
$\dim\operatorname{grt}_1(\text{weight }10) = 1$
\textup{(}from $[\sigma_3, \sigma_7]$\textup{)}, and
$\dim\operatorname{grt}_1(\text{weight }12) = 2$
\textup{(}one Ihara-reduced bracket $+$ the cusp
form~$\Delta_{12}$\textup{)}.
The spectral Drinfeld class must be analysed
case by case at weights $\geq 8$.
\end{remark}

\begin{remark}[Frontier status of the ten load-bearing conjectures, as of 2026]
\label{rem:concordance-frontier-status-2026}
\index{open conjectures!frontier status 2026}
The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
\begin{enumerate}
\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
 \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
\item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
 Restricted DK-4 on the evaluation-generated core is the next step.
exec
/bin/zsh -lc "sed -n '900,980p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
\cA = F^0\cA \supset F^1\cA \supset F^2\cA \supset \cdots,
\qquad
\textstyle\bigcap_{N \ge 0} F^{N+1}\cA = 0,
\]
such that:
\begin{enumerate}
\item $\cA$ is separated and complete:
 $\cA \cong \varprojlim_N \cA_{\le N}$, where
 $\cA_{\le N} := \cA/F^{N+1}\cA$;
\item every quotient $\cA_{\le N}$ is finite type and lies in the proved
 bar-cobar regime;
\item $\bar\cA = F^1\cA$ (the augmentation ideal is the first filtration
 piece); and
\item all chiral $\Ainf$-operations are filtration-nondecreasing:
 \begin{equation}\label{eq:strong-filtration-condition}
 \mu_r(F^{i_1}\cA, \dots, F^{i_r}\cA)
 \subset F^{i_1+\cdots+i_r}\cA.
 \end{equation}
\end{enumerate}
exec
/bin/zsh -lc "sed -n '1080,1115p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
The right term vanishes because each $\epsilon_N$ is a quasi-isomorphism.
The left term vanishes because the surjective quotient tower is
Mittag--Leffler. Hence $\widehat\epsilon$ is a quasi-isomorphism.

\emph{Step~4: unit on the coalgebra side.}
By the same quotientwise argument: the quotient of $\widehat\eta$ modulo
$F^{N+1}$ is the finite-stage unit, which is a quasi-isomorphism.
Lemma~\ref{lem:complete-filtered-comparison} applies identically.
\end{proof}

\begin{proposition}[Standard weight truncations and the induced bar filtration;
\ClaimStatusProvedHere]
\label{prop:standard-strong-filtration}
\index{bar complex!weight truncations for standard families|textbf}
Let $\cA$ be one of the following chiral algebras:
\begin{enumerate}[label=\textup{(\alph*)}]
\item $V_k(\fg)$ for any simple~$\fg$ and $k \neq -h^\vee$;
\item $\mathrm{Vir}_c$ for any~$c$;
\item $\cW^k(\fg, f_{\mathrm{prin}})$ for any simple~$\fg$,
exec
/bin/zsh -lc "sed -n '2185,2235p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{prop:winfty-ds-local-coefficient-criterion}
Fix $N \ge 2$ and let
$\mathcal{F}_{\le N}:=\mathcal{F}_\infty/I_{>N}\mathcal{F}_\infty$
be as in
Proposition~\ref{prop:winfty-spin-triangular-ideals}. If the local
OPE coefficients $C_{s,t}^{u;m,n}(N)$ agree with the principal DS data,
translation descendants generate all local relations, and bar operations
match, then Proposition~\ref{prop:winfty-ds-coefficient-criterion}
applies and the quotient identifies with $W_N$.
\end{proposition}

\begin{proof}
Immediate from Proposition~\ref{prop:winfty-ds-coefficient-criterion}.
\end{proof}

\begin{proposition}[Residue-coefficient identity criterion for
principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients;
\ClaimStatusProvedHere]
\label{prop:winfty-ds-residue-identity-criterion}
Fix $N \ge 2$ and let

thinking
**Locating missing information**

I need to look for the missing RG search while ensuring I properly escape any necessary elements. I'm also aiming to gather definitions for terms like "provisional coderived" and possibly "spectral sequence prop." To tackle this, I think using a simple string list format for RG could be helpful, and I might want to separate the different elements as needed. This way, I can organize the information better as I search.
codex
The support surface is consistent: the introduction and concordance already state “coderived proved, class-`M` strict chain level false.” I’m now reading the exact filtration/spectral definitions so the new remark can make a stronger statement without inventing unsupported terminology.
exec
/bin/zsh -lc "sed -n '2440,2535p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:coderived-bar-degree-spectral-sequence|def:provisional-coderived|def:curved-weak-equiv|cor:virasoro-postnikov-nontermination|shadow obstruction tower|permanent cubic source\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \barB^{\mathrm{ch}}_0\bigl(V_k(\fg)\bigr),\,
 d_{\mathrm{bar}}
 \bigr).
\end{equation}
On the PBW-associated graded, the BRST differential
$Q_{\mathrm{BRST}}^{\mathrm{WZW}}$ equals the bar differential
$d_{\mathrm{bar}}$; both reduce to the Chevalley--Eilenberg
differential $d_{\mathrm{CE}}$ of the loop algebra subalgebra
$\widehat{\fg}_{k,-} := \fg \otimes t^{-1}\mathbb{C}[t^{-1}]$
acting on the vacuum module~$V_k(\fg)$.
\end{proposition}

\begin{proof}
The argument extends
Theorem~\ref{thm:brst-bar-genus0} \textup{(}the $c = 26$ string
case\textup{)} by replacing the Virasoro BRST complex with the
affine semi-infinite complex, and invokes
Theorem~\ref{thm:bar-semi-infinite-km} for the comparison.

\emph{Step~1: Bar--semi-infinite comparison.}
 succeeded in 52ms:
Total output lines: 989

chapters/examples/deformation_quantization.tex:117:\item The Jacobi identity of the PVA ensures vanishing of $o_3$ (the cubic quantization obstruction). Higher obstructions $o_r$ for $r \geq 4$ are governed by the shadow obstruction tower of the quantized algebra and do not automatically vanish. (Koszulness of the quantized algebra is a separate property from shadow obstruction tower termination; both finite and infinite shadow depth algebras can be Koszul.)
chapters/examples/w_algebras_deep.tex:647:The shadow obstruction tower reduces to the Virasoro tower:
chapters/examples/w_algebras_deep.tex:694:with the full Virasoro shadow obstruction tower, reflecting the fact that the
chapters/examples/w_algebras_deep.tex:2566:In particular, the shadow obstruction tower intertwines:
chapters/examples/w_algebras_deep.tex:2691:after. The shadow obstruction tower of $\mathcal{W}^k(\fg,f)$ is
chapters/examples/w_algebras_deep.tex:2879: The ghost contribution to the shadow obstruction tower is absorbed
chapters/examples/w_algebras_deep.tex:2982:We tabulate the transformation of shadow obstruction tower data under principal
chapters/examples/w_algebras_deep.tex:3076:quantitatively smaller, confirming that the shadow obstruction tower
chapters/examples/w_algebras_deep.tex:3760:\index{shadow obstruction tower!W-algebra position@$\mathcal{W}$-algebra position}
chapters/examples/w_algebras_deep.tex:3762:$\mathcal{W}_\infty$ in a precise position within the shadow obstruction tower
chapters/examples/w_algebras_deep.tex:4009:\index{W4@$\mathcal{W}_4$!shadow obstruction tower}
chapters/examples/w_algebras_deep.tex:4010:\index{W5@$\mathcal{W}_5$!shadow obstruction tower}
chapters/examples/w_algebras_deep.tex:4014:The $\Walg_3$ shadow obstruction tower
chapters/examples/w_algebras_deep.tex:4134:\index{Z2 parity@$\mathbb{Z}_2$ parity!shadow obstruction tower}
chapters/examples/w_algebras_deep.tex:5141:\section{The $N\!=\!2$ superconformal shadow obstruction tower}%
chapters/examples/w_algebras_deep.tex:5144:\index{shadow obstruction tower!N=2 superconformal@$N=2$ superconformal}
chapters/examples/w_algebras_deep.tex:5152:The shadow obstruction tower data of the $N=2$ SCA provides the first worked
chapters/examples/w_algebras_deep.tex:5153:example of a \emph{multi-channel} shadow obstruction tower with a $2 \times 2$
exec
/bin/zsh -lc "sed -n '140,240p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_modular_koszul.tex | rg -n \"cor:virasoro-postnikov-nontermination|shadow obstruction tower|nontermination|Postnikov|Virasoro\" -n" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{cor:virasoro-postnikov-nontermination\\}|label\\{prop:coderived-bar-degree-spectral-sequence\\}|label\\{def:provisional-coderived\\}|label\\{def:curved-weak-equiv\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
role.
\begin{enumerate}[label=(\roman*)]
\item $\mathrm{Mod}_{\mathcal{A}}$: the dg category of chiral
 $\mathcal{A}$-modules (Definition~\ref{def:chiral-module}),
 with morphisms the $\mathcal{D}_X$-module maps compatible with
 the chiral action. This is the \emph{symmetric} (i.e.\ $\Sigma_n$-equivariant) module category, indexed by
 unordered configuration spaces, and is a stable $\infty$-category
 when $\mathcal{V} = \mathrm{Ch}(\mathbb{C})$.
\item $\mathrm{Mod}^{\Eone}_{\mathcal{A}}$: the dg category of
 $\Eone$-chiral $\mathcal{A}$-modules
 (Definition~\ref{def:e1-chiral-module}), when $\mathcal{A}$ is
 $\Eone$-chiral. This is the \emph{line-operator} module category,
 indexed by ordered configuration spaces with no
 $\Sigma_n$-equivariance, and carries the braid group action
 underlying the Drinfeld--Kohno theorem. There is a forgetful
 functor $\mathrm{Mod}_{\mathcal{A}} \to
 \mathrm{Mod}^{\Eone}_{\mathcal{A}}$ when $\mathcal{A}$ is
 $\Einf$-chiral; this functor is generally NOT an equivalence,
 reflecting the genuine difference between symmetric and ordered
 factorization data.
 succeeded in 50ms:
151: genus-$0$ shadow obstruction tower coincides with the
 succeeded in 51ms:
chapters/examples/w_algebras.tex:5274:\label{cor:virasoro-postnikov-nontermination}
chapters/theory/coderived_models.tex:222:\label{def:curved-weak-equiv}
chapters/theory/coderived_models.tex:242:\label{def:provisional-coderived}
chapters/theory/coderived_models.tex:316:\label{prop:coderived-bar-degree-spectral-sequence}
exec
/bin/zsh -lc "sed -n '640,740p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Summary for practitioners]\label{rem:practitioner-takeaway}
\emph{Before computing the Koszul dual, one should determine:}
\begin{enumerate}
\item Is the algebra quadratic? $\Rightarrow$ Proceed directly
\item Is it curved with central curvature? $\Rightarrow$ Check if $\dim(\bar{B}^1) < \infty$
 \begin{itemize}
 \item If yes: No completion
 \item If no: Completion is required
 \end{itemize}
\item Does it have composite operators? $\Rightarrow$ Must complete
\item Is the generating space infinite-dimensional? $\Rightarrow$ handled by the MC4 completion theorem (Theorem~\ref{thm:completed-bar-cobar-strong}); residual task is to identify the filtered H-level target and its finite quotients by explicit coefficient identities and finite detection
\end{enumerate}

Most vertex algebras from CFT are either quadratic or curved with finite-dimensional
$\bar{B}^1$, so Koszul duality applies.
\end{remark}

\iffalse
The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
exec
/bin/zsh -lc "sed -n '210,340p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1660,1705p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5258,5295p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (cf.\ the fiberwise differential $\dfib$ with $\dfib^{\,2} = \mcurv{g}$,
 Convention~\textup{\ref{conv:higher-genus-differentials}});
\item $\mathcal{F} = \{F^p M\}_{p \geq 0}$ is an exhaustive
 decreasing filtration with $d(F^p) \subset F^p$,
 $m_0 \in F^1$, and $\operatorname{gr}^0_{\mathcal{F}} d$ strict
 ($(\operatorname{gr}^0 d)^2 = 0$).
\end{enumerate}
A morphism $f \colon (M, d, \mathcal{F}) \to (N, d', \mathcal{F}')$ is a
filtration-preserving coalgebra map compatible with differentials and curvatures.
\end{definition}

\begin{definition}[Weak equivalence of curved models]
\label{def:curved-weak-equiv}
A morphism $f \colon M \to N$ of filtered curved factorization models
is a \emph{weak equivalence} if it satisfies either of the following
equivalent conditions:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The associated graded map
 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
 succeeded in 50ms:
 is coacyclic. Equivalently, $\psi_X$ is an isomorphism in
 $D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$, without any
 Koszulness hypothesis.

\item \emph{Coderived bar-degree filtration.}
 On the curved cone $K_\psi$, the bar-degree filtration yields the
 coderived spectral sequence of
 Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
 $E_1$ page is computed from the strict associated-graded differential
 $\operatorname{gr}^0 d$; the curvature relation
 $\dfib^{\,2} = \kappa(\mathcal{A}) \cdot \omega_g$ is absorbed into
 positive filtration and does not obstruct the $E_1$ page.
 On the square-zero Koszul lane this reduces to
 Theorems~\ref{thm:bar-cobar-spectral-sequence}
 and~\ref{thm:spectral-sequence-collapse}.

\item \emph{Promotion back to ordinary quasi-isomorphism.}
 If $\kappa(\mathcal{A}) = 0$, or more generally if the coderived
 bar-degree spectral sequence degenerates to ordinary cohomology on
 the relevant off-Koszul locus
 succeeded in 52ms:
quadratic + cubic \\
$\beta\gamma$ & $4$ (contact) & rank-one rigidity &
quartic on weight line \\
Virasoro/$\mathcal{W}_N$ & $\infty$ & permanent cubic source &
non-polynomial \\
\bottomrule
\end{tabular}
\end{center}
For the infinite-tower families, $\Theta_\cA = \varprojlim_r
\Theta_\cA^{\leq r}$
(Theorem~\ref{thm:recursive-existence}) is genuinely
infinite-order: the complementarity potential is non-polynomial.
\end{remark}

\begin{corollary}[Virasoro/$\mathcal{W}_N$ shadow obstruction tower:
infinite; \ClaimStatusProvedHere]
\label{cor:virasoro-postnikov-nontermination}
\index{shadow obstruction tower!Virasoro non-termination}
The shadow obstruction tower
\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}
exec
/bin/zsh -lc "sed -n '1828,1855p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1910,1935p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2318,2342p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
where the last quasi-isomorphism is the twisting-morphism/Koszul-duality
identification of
Theorem~\ref{thm:fundamental-twisting-morphisms}
\textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.

Off the Koszul locus the same deformation-retract package survives
after passing to filtered curved models. The transfer data respects
the bar-degree filtration, and the curvature term lies in positive
filtration, so the associated graded retract is strict.
Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
identifies the cone of the factorization counit as coacyclic, and
Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
statement of clause~\textup{(2)}. This does not remove the extra
hypothesis in clause~\textup{(4)}: promotion from coderived
equivalence to an ordinary quasi-isomorphism still requires the same
collapse input, or the flat case $\kappa(\cA)=0$.
\end{remark}

 succeeded in 51ms:
category for every complete augmented input with finite-dimensional
graded bar pieces. Its proof is independent of
Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
$\psi_X$ as coacyclic by stratified Positselski inversion and the
Verdier-quotient criterion for
$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.

\item \emph{Coderived bar-degree filtration.}
On the strict square-zero surface, existence and collapse are exactly
Theorems~\ref{thm:bar-cobar-spectral-sequence}
and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
replaces ordinary abutment by coacyclicity of the cone: the
associated-graded $E_1$ page is strict because the curvature term lies
in positive filtration.

\item \emph{Promotion lane.}
If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
coderived and ordinary derived categories and the coderived
 succeeded in 51ms:
and~\ref{thm:spectral-sequence-collapse} are statements about filtered
complexes with square-zero total differential. In this chapter they
apply to the strict genus-$0$ bar-cobar complex, and to any
completed/corrected model whose total differential squares to zero.
They do \emph{not} apply to the curved fiberwise higher-genus
differential $\dfib$ with
$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
proved replacement is the coderived bar-degree filtration of
Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
together with the intrinsic coderived/contraderived bar-coalgebra
comparison of Theorem~\ref{thm:positselski-chiral-proved}. Ordinary
derived reduction remains available only on the flat finite-type
completed-dual loci of Theorem~\ref{thm:full-derived-module-equiv-proved}
or when the curvature collapses.
\end{remark}

\subsection{Convergence at all genera}

\begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
\textup{[Regime: curved-central on the Koszul locus







thinking
**Refining mathematical proposals**

I’m thinking about the clean candidate being defined as the shadow-window filtration \(F^R K_g\) by forgetting operations of shadow degree \(<R\). If this isn’t already formalized, it might be better as a research target rather than an assertion. I could suggest a natural candidate as the decreasing shadow-window filtration \(F^R K_g := \langle \delta_r^{harm} \mid r\ge R \rangle\), but I wonder if that's overly innovative. I need to ensure mathematical coherence while considering how to refine this proposal effectively.
thinking
**Exploring refinements in filtration**

I’m considering adding that the natural refinement is the shadow-window filtration, which retains contributions from shadow degree \(\ge R\). This seems important because the corollary indicates there are nonzero contributions at every degree, making the filtration infinite. Yet, each quotient only captures finitely many \(\delta_r^{harm}\). I want to ensure that this progression of ideas is clear and makes sense in the context. This could enhance the proposal, but I need to think carefully about its implications.
thinking
**Updating remarks on theorem**

I'm thinking about how to improve my remarks by including numbered items like failure mechanism, spectral MC5, completed chain-level statement, and intermediate strengthening. I should mention that each finite shadow window comparison should be strict quasi-iso, but I'm not sure if that's proven yet. Maybe I should label it as a candidate theorem. The spectral form of MC5 could assert that for every finite shadow window, the comparison map should be a filtered quasi-isomorphism, though justification is lacking for now.
thinking
**Revising assertions on quasi-isomorphism**

I'm realizing I shouldn't assert that each finite window is a strict quasi-isomorphism. Instead, my first goal should be proving the truncated comparison on each finite window and then moving to the inverse limit. I mentioned earlier that every finite quotient of \(\hat f_g\) is a strict quasi-isomorphism, but that's conjectural. I could refine this by noting the quotient by \(F^{R+1}\) remembers only degrees \(\le R\), making it a finite problem. I also need to mention "infinite A∞ operations" since the user's interested in it.
thinking
**Addressing strict maps in complexes**

I’m thinking about a strict map of raw complexes that needs to identify a finite-order BV differential along with an explicit model that includes infinitely many higher corrections. This complexity is precisely why the direct-sum chain-level statement isn't successful in this context. It highlights the intricacies at play in these mappings and helps ground my understanding of where complications arise in the application of these theories.
thinking
**Updating remark body and title**

I’m thinking about updating both the remark body and its title. It seems like applying a patch would be the way to go. So, I need to create a complete replacement for everything from `\begin{remark}[Research direction...` to `\end{remark}`. I must remember to preserve the label while ensuring that the new content is concise yet precise. I really want to get this right!
thinking
**Considering harmonic defect notation**

I’m thinking about possibly adding “with \(d_r\) detecting the degree-\(r\) harmonic defect,” but I’m not completely sure. It might also be okay to phrase it as “with differential \(d_r\) detecting the degree-\(r\) harmonic defect” to clarify the target. I should consider whether I need to mention the \(R\) quotient notation too, since it might tie into the explanation. There’s a lot to weigh in this!
codex
I’m editing only the existing `rem:bv-bar-class-m-frontier` block. The rewrite will make the failure mechanism explicit, then separate the two viable upgrades: a spectral MC5 via shadow-window filtration, and a bi-completed chain-level comparison stronger than bare coderived equivalence.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -2168,3 +2168,3 @@
 
-\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\begin{remark}[Research remark: class~$\mathsf{M}$ spectral and completed MC5]
 \label{rem:bv-bar-class-m-frontier}
@@ -2173,6 +2173,7 @@
 Theorem~\ref{thm:bv-bar-coderived} and
-Proposition~\ref{prop:chain-level-three-obstructions} already isolate
-the exact failure mechanism for class~$\mathsf{M}$. The quartic
-harmonic discrepancy is not a coboundary in the ordinary chain
-complex, and the higher discrepancies satisfy
+Proposition~\ref{prop:chain-level-three-obstructions} isolate not
+only the surviving coderived statement but also the exact reason the
+strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
+Virasoro and principal $\cW_N$, the higher harmonic discrepancies
+satisfy
 \[
@@ -2183,33 +2184,41 @@
 \]
-For Virasoro and principal $\cW_N$,
 Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
-shadow obstruction tower does not terminate. The naive chain-level
-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
-class~$\mathsf{M}$ on the explicit uncompleted models: one is not
-facing a single quartic defect, but an infinite family of nonvanishing
-higher corrections regenerated by the permanent cubic source.
+shadow obstruction tower does not terminate: the permanent cubic
+source regenerates nonzero higher obstructions at every stage. In the
+operadic language of
+Remark~\ref{rem:bv-bar-coderived-operadic}, the transferred
+class~$\mathsf{M}$ $A_\infty$-operations do not truncate. A strict
+comparison on the raw direct-sum models would have to absorb
+infinitely many nonvanishing higher corrections by a single ordinary
+chain-homotopy package. This is what fails. The coderived theorem
+survives because every defect is still divisible by the central
+curvature.
 
-A spectral replacement is still plausible. Filter the comparison cone
-$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
-weight, or any compatible shadow-window filtration.
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
-supplies a coderived spectral sequence whose $E_1$ page is computed
-from the strict associated-graded differential, because the curvature
-lies in positive filtration. For class~$\mathsf{M}$, each finite
-window sees only finitely many operations, so the associated-graded
-comparison is a finite problem. The research target is a spectral form
-of MC5: construct a class~$\mathsf{M}$ filtration for which the
-higher differentials record exactly the harmonic classes
-$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
-This would replace a false strict chain identity by a filtered
-comparison that measures the failure page by page.
+A spectral replacement remains viable. Let
+$K_g = \operatorname{cone}(f_g)$ and filter it by bar degree, total
+conformal weight, or, more sharply for class~$\mathsf{M}$, by a
+shadow-window filtration in which the quotient by $F^{R+1}$ keeps only
+the discrepancy classes of shadow degree at most~$R$. Each finite
+window then sees only finitely many nonzero operations, so the
+associated-graded comparison becomes a finite problem.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+supplies the corresponding coderived spectral sequence, with strict
+$E_1$ page because the curvature lies in positive filtration. The
+research target is a spectral form of MC5 whose higher differentials
+record the harmonic classes $c_r(\cA)$ and whose abutment is a
+coacyclic cone. This replaces a false strict chain identity by a
+filtered comparison that measures the class~$\mathsf{M}$ defect page
+by page.
 
-The best chain-level statement is likely completed rather than strict.
-Proposition~\ref{prop:standard-strong-filtration} and
-Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
-class~$\mathsf{M}$ families already carry the weight-completion
-package on the bar side. Since the full Maurer--Cartan class satisfies
+The strongest chain-level statement presently visible is completed
+rather than strict. Proposition~\ref{prop:standard-strong-filtration}
+and Theorem~\ref{thm:completed-bar-cobar-strong} already provide the
+weight-completed bar side, and
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows why
+class~$\mathsf{M}$ also needs completion in shadow degree. Since the
+full Maurer--Cartan class satisfies
 $\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
-convolution algebra, the correct BV analogue should also live in a
-completion. One should therefore seek a continuous comparison
+convolution algebra, the correct BV analogue should live in the same
+completed regime. One should therefore seek a continuous comparison of
+bi-completed models
 \[
@@ -2220,21 +2229,23 @@
 \]
-where the hats denote compatible inverse limits of finite shadow or
-weight truncations. The conjectural assertion is not that the raw
-direct-sum complexes are quasi-isomorphic, but that every finite
+where the hats denote inverse limits over finite weight truncations
+and finite shadow windows, equivalently a pro-object built from those
+finite quotients. The conjectural statement is not that the raw
+direct-sum complexes are quasi-isomorphic, but that each finite
 quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
-inverse limit is continuous. This is the strongest chain-level
-statement presently visible for class~$\mathsf{M}$.
+inverse-limit comparison is continuous and filtration-compatible. This
+is stronger than Theorem~\ref{thm:bv-bar-coderived}, because it
+remembers every finite stage, and weaker than a raw chain-level
+quasi-isomorphism, because it allows the infinite class~$\mathsf{M}$
+defect to die only after completion.
 
-Between ordinary chain level and bare coderived equivalence lies a
-stronger filtered-completed statement. One can ask that
-$\widehat f_g$ be a weak equivalence of filtered curved models in the
-sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
-isomorphism already in the provisional coderived category of
-Definition~\ref{def:provisional-coderived}. This is stronger than
-Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
-filtration and every finite truncation; it is weaker than an ordinary
-chain-level quasi-isomorphism, because it allows the infinite residual
-class~$\mathsf{M}$ discrepancy to die only after filtered coderived
-passage. At present this filtered-completed refinement is the most
-plausible strengthening of the coderived theorem.
+Between ordinary chain level and bare coderived equivalence lies an
+intermediate strengthening. One may ask that $\widehat f_g$ be a weak
+equivalence of filtered curved models in the sense of
+Definition~\ref{def:curved-weak-equiv}, equivalently an isomorphism
+already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This retains the full
+filtered-completed class~$\mathsf{M}$ tower while remaining compatible
+with the proved coderived theorem. On the current record, this
+filtered-completed spectral statement is the sharpest plausible
+upgrade of MC5 for class~$\mathsf{M}$.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 27ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index e4df175dbf71b9839f605a72128879eb8a36ec78..fa2749149ab05703e3a00e13e3f1eb6b7807d89c
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2166,77 +2166,88 @@
 all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
-\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\begin{remark}[Research remark: class~$\mathsf{M}$ spectral and completed MC5]
 \label{rem:bv-bar-class-m-frontier}
 \index{BV algebra!class M frontier|textbf}%
 \index{coderived category!filtered-completed refinement}%
 Theorem~\ref{thm:bv-bar-coderived} and
-Proposition~\ref{prop:chain-level-three-obstructions} already isolate
-the exact failure mechanism for class~$\mathsf{M}$. The quartic
-harmonic discrepancy is not a coboundary in the ordinary chain
-complex, and the higher discrepancies satisfy
+Proposition~\ref{prop:chain-level-three-obstructions} isolate not
+only the surviving coderived statement but also the exact reason the
+strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
+Virasoro and principal $\cW_N$, the higher harmonic discrepancies
+satisfy
 \[
 \delta_r^{\mathrm{harm}}
 \;=\;
 c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
 \qquad (r \geq 4).
 \]
-For Virasoro and principal $\cW_N$,
 Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
-shadow obstruction tower does not terminate. The naive chain-level
-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
-class~$\mathsf{M}$ on the explicit uncompleted models: one is not
-facing a single quartic defect, but an infinite family of nonvanishing
-higher corrections regenerated by the permanent cubic source.
+shadow obstruction tower does not terminate: the permanent cubic
+source regenerates nonzero higher obstructions at every stage. In the
+operadic language of
+Remark~\ref{rem:bv-bar-coderived-operadic}, the transferred
+class~$\mathsf{M}$ $A_\infty$-operations do not truncate. A strict
+comparison on the raw direct-sum models would have to absorb
+infinitely many nonvanishing higher corrections by a single ordinary
+chain-homotopy package. This is what fails. The coderived theorem
+survives because every defect is still divisible by the central
+curvature.
 
-A spectral replacement is still plausible. Filter the comparison cone
-$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
-weight, or any compatible shadow-window filtration.
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
-supplies a coderived spectral sequence whose $E_1$ page is computed
-from the strict associated-graded differential, because the curvature
-lies in positive filtration. For class~$\mathsf{M}$, each finite
-window sees only finitely many operations, so the associated-graded
-comparison is a finite problem. The research target is a spectral form
-of MC5: construct a class~$\mathsf{M}$ filtration for which the
-higher differentials record exactly the harmonic classes
-$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
-This would replace a false strict chain identity by a filtered
-comparison that measures the failure page by page.
+A spectral replacement remains viable. Let
+$K_g = \operatorname{cone}(f_g)$ and filter it by bar degree, total
+conformal weight, or, more sharply for class~$\mathsf{M}$, by a
+shadow-window filtration in which the quotient by $F^{R+1}$ keeps only
+the discrepancy classes of shadow degree at most~$R$. Each finite
+window then sees only finitely many nonzero operations, so the
+associated-graded comparison becomes a finite problem.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+supplies the corresponding coderived spectral sequence, with strict
+$E_1$ page because the curvature lies in positive filtration. The
+research target is a spectral form of MC5 whose higher differentials
+record the harmonic classes $c_r(\cA)$ and whose abutment is a
+coacyclic cone. This replaces a false strict chain identity by a
+filtered comparison that measures the class~$\mathsf{M}$ defect page
+by page.
 
-The best chain-level statement is likely completed rather than strict.
-Proposition~\ref{prop:standard-strong-filtration} and
-Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
-class~$\mathsf{M}$ families already carry the weight-completion
-package on the bar side. Since the full Maurer--Cartan class satisfies
+The strongest chain-level statement presently visible is completed
+rather than strict. Proposition~\ref{prop:standard-strong-filtration}
+and Theorem~\ref{thm:completed-bar-cobar-strong} already provide the
+weight-completed bar side, and
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows why
+class~$\mathsf{M}$ also needs completion in shadow degree. Since the
+full Maurer--Cartan class satisfies
 $\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
-convolution algebra, the correct BV analogue should also live in a
-completion. One should therefore seek a continuous comparison
+convolution algebra, the correct BV analogue should live in the same
+completed regime. One should therefore seek a continuous comparison of
+bi-completed models
 \[
 \widehat f_g \colon
 \widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
 \longrightarrow
 \widehat B^{(g)}(\cA),
 \]
-where the hats denote compatible inverse limits of finite shadow or
-weight truncations. The conjectural assertion is not that the raw
-direct-sum complexes are quasi-isomorphic, but that every finite
+where the hats denote inverse limits over finite weight truncations
+and finite shadow windows, equivalently a pro-object built from those
+finite quotients. The conjectural statement is not that the raw
+direct-sum complexes are quasi-isomorphic, but that each finite
 quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
-inverse limit is continuous. This is the strongest chain-level
-statement presently visible for class~$\mathsf{M}$.
+inverse-limit comparison is continuous and filtration-compatible. This
+is stronger than Theorem~\ref{thm:bv-bar-coderived}, because it
+remembers every finite stage, and weaker than a raw chain-level
+quasi-isomorphism, because it allows the infinite class~$\mathsf{M}$
+defect to die only after completion.
 
-Between ordinary chain level and bare coderived equivalence lies a
-stronger filtered-completed statement. One can ask that
-$\widehat f_g$ be a weak equivalence of filtered curved models in the
-sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
-isomorphism already in the provisional coderived category of
-Definition~\ref{def:provisional-coderived}. This is stronger than
-Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
-filtration and every finite truncation; it is weaker than an ordinary
-chain-level quasi-isomorphism, because it allows the infinite residual
-class~$\mathsf{M}$ discrepancy to die only after filtered coderived
-passage. At present this filtered-completed refinement is the most
-plausible strengthening of the coderived theorem.
+Between ordinary chain level and bare coderived equivalence lies an
+intermediate strengthening. One may ask that $\widehat f_g$ be a weak
+equivalence of filtered curved models in the sense of
+Definition~\ref{def:curved-weak-equiv}, equivalently an isomorphism
+already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This retains the full
+filtered-completed class~$\mathsf{M}$ tower while remaining compatible
+with the proved coderived theorem. On the current record, this
+filtered-completed spectral statement is the sharpest plausible
+upgrade of MC5 for class~$\mathsf{M}$.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index e4df175dbf71b9839f605a72128879eb8a36ec78..fa2749149ab05703e3a00e13e3f1eb6b7807d89c
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2166,77 +2166,88 @@
 all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
-\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\begin{remark}[Research remark: class~$\mathsf{M}$ spectral and completed MC5]
 \label{rem:bv-bar-class-m-frontier}
 \index{BV algebra!class M frontier|textbf}%
 \index{coderived category!filtered-completed refinement}%
 Theorem~\ref{thm:bv-bar-coderived} and
-Proposition~\ref{prop:chain-level-three-obstructions} already isolate
-the exact failure mechanism for class~$\mathsf{M}$. The quartic
-harmonic discrepancy is not a coboundary in the ordinary chain
-complex, and the higher discrepancies satisfy
+Proposition~\ref{prop:chain-level-three-obstructions} isolate not
+only the surviving coderived statement but also the exact reason the
+strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
+Virasoro and principal $\cW_N$, the higher harmonic discrepancies
+satisfy
 \[
 \delta_r^{\mathrm{harm}}
 \;=\;
 c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
 \qquad (r \geq 4).
 \]
-For Virasoro and principal $\cW_N$,
 Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
-shadow obstruction tower does not terminate. The naive chain-level
-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
-class~$\mathsf{M}$ on the explicit uncompleted models: one is not
-facing a single quartic defect, but an infinite family of nonvanishing
-higher corrections regenerated by the permanent cubic source.
+shadow obstruction tower does not terminate: the permanent cubic
+source regenerates nonzero higher obstructions at every stage. In the
+operadic language of
+Remark~\ref{rem:bv-bar-coderived-operadic}, the transferred
+class~$\mathsf{M}$ $A_\infty$-operations do not truncate. A strict
+comparison on the raw direct-sum models would have to absorb
+infinitely many nonvanishing higher corrections by a single ordinary
+chain-homotopy package. This is what fails. The coderived theorem
+survives because every defect is still divisible by the central
+curvature.
 
-A spectral replacement is still plausible. Filter the comparison cone
-$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
-weight, or any compatible shadow-window filtration.
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
-supplies a coderived spectral sequence whose $E_1$ page is computed
-from the strict associated-graded differential, because the curvature
-lies in positive filtration. For class~$\mathsf{M}$, each finite
-window sees only finitely many operations, so the associated-graded
-comparison is a finite problem. The research target is a spectral form
-of MC5: construct a class~$\mathsf{M}$ filtration for which the
-higher differentials record exactly the harmonic classes
-$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
-This would replace a false strict chain identity by a filtered
-comparison that measures the failure page by page.
+A spectral replacement remains viable. Let
+$K_g = \operatorname{cone}(f_g)$ and filter it by bar degree, total
+conformal weight, or, more sharply for class~$\mathsf{M}$, by a
+shadow-window filtration in which the quotient by $F^{R+1}$ keeps only
+the discrepancy classes of shadow degree at most~$R$. Each finite
+window then sees only finitely many nonzero operations, so the
+associated-graded comparison becomes a finite problem.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+supplies the corresponding coderived spectral sequence, with strict
+$E_1$ page because the curvature lies in positive filtration. The
+research target is a spectral form of MC5 whose higher differentials
+record the harmonic classes $c_r(\cA)$ and whose abutment is a
+coacyclic cone. This replaces a false strict chain identity by a
+filtered comparison that measures the class~$\mathsf{M}$ defect page
+by page.
 
-The best chain-level statement is likely completed rather than strict.
-Proposition~\ref{prop:standard-strong-filtration} and
-Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
-class~$\mathsf{M}$ families already carry the weight-completion
-package on the bar side. Since the full Maurer--Cartan class satisfies
+The strongest chain-level statement presently visible is completed
+rather than strict. Proposition~\ref{prop:standard-strong-filtration}
+and Theorem~\ref{thm:completed-bar-cobar-strong} already provide the
+weight-completed bar side, and
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows why
+class~$\mathsf{M}$ also needs completion in shadow degree. Since the
+full Maurer--Cartan class satisfies
 $\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
-convolution algebra, the correct BV analogue should also live in a
-completion. One should therefore seek a continuous comparison
+convolution algebra, the correct BV analogue should live in the same
+completed regime. One should therefore seek a continuous comparison of
+bi-completed models
 \[
 \widehat f_g \colon
 \widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
 \longrightarrow
 \widehat B^{(g)}(\cA),
 \]
-where the hats denote compatible inverse limits of finite shadow or
-weight truncations. The conjectural assertion is not that the raw
-direct-sum complexes are quasi-isomorphic, but that every finite
+where the hats denote inverse limits over finite weight truncations
+and finite shadow windows, equivalently a pro-object built from those
+finite quotients. The conjectural statement is not that the raw
+direct-sum complexes are quasi-isomorphic, but that each finite
 quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
-inverse limit is continuous. This is the strongest chain-level
-statement presently visible for class~$\mathsf{M}$.
+inverse-limit comparison is continuous and filtration-compatible. This
+is stronger than Theorem~\ref{thm:bv-bar-coderived}, because it
+remembers every finite stage, and weaker than a raw chain-level
+quasi-isomorphism, because it allows the infinite class~$\mathsf{M}$
+defect to die only after completion.
 
-Between ordinary chain level and bare coderived equivalence lies a
-stronger filtered-completed statement. One can ask that
-$\widehat f_g$ be a weak equivalence of filtered curved models in the
-sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
-isomorphism already in the provisional coderived category of
-Definition~\ref{def:provisional-coderived}. This is stronger than
-Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
-filtration and every finite truncation; it is weaker than an ordinary
-chain-level quasi-isomorphism, because it allows the infinite residual
-class~$\mathsf{M}$ discrepancy to die only after filtered coderived
-passage. At present this filtered-completed refinement is the most
-plausible strengthening of the coderived theorem.
+Between ordinary chain level and bare coderived equivalence lies an
+intermediate strengthening. One may ask that $\widehat f_g$ be a weak
+equivalence of filtered curved models in the sense of
+Definition~\ref{def:curved-weak-equiv}, equivalently an isomorphism
+already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This retains the full
+filtered-completed class~$\mathsf{M}$ tower while remaining compatible
+with the proved coderived theorem. On the current record, this
+filtered-completed spectral statement is the sharpest plausible
+upgrade of MC5 for class~$\mathsf{M}$.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:15 PM.
tokens used
107,376
