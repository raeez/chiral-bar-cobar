# H14_remove_koszul_locus (607s)

The Theorem B research surface in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1934) now states the Koszul-locus question in the four pieces you asked for: the exact genus-0 definition, the off-locus obstruction as the first off-diagonal bar class and first transferred higher \(m_r\), the conjectural derived Koszul wall versus the proved abstract collapse criterion, and the family boundary where failure is expected. It also now says explicitly that clause (4) does not remove the genus-0 Koszul hypothesis.

I checked that against [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:236) and [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:274). A cold `latexmk` pass gets past this theorem band and then fails later, outside this surface, at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677) on an undefined `\ord` macro. Full-build verification is therefore blocked elsewhere. The build attempts also refreshed tracked TeX artifacts (`main.aux`, `main.log`, `main.out`).

## Fortification Report
Theorem B (`thm:bar-cobar-inversion-qi`)

- PRIMARY PROOF: `sound`
- SECONDARY PROOF: `written`
- TECHNIQUE: dependency-closed spectral-sequence/coderived proof; independent formality plus homotopy-transfer proof on the strict Koszul lane
- CONDITION STATUS: strict quasi-isomorphism conditional on the genus-0 Koszul locus and higher-genus modular input; off-locus coderived equivalence unconditional; ordinary off-locus promotion only by the abstract collapse criterion, with the derived wall still conjectural
- CONFIDENCE: `high`


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
session id: 019d86aa-10af-7093-ab2d-2f5f51c2ed69
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


RESEARCH: Can the Koszul locus restriction be removed from Theorem B?

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex (add Research Remark)

Theorem B gives qi Omega(B(A)) -> A on the KOSZUL LOCUS. Off-locus: coderived only.

INVESTIGATE:
1. What is the Koszul locus PRECISELY? (Quadratic A-inf algebras whose bar cohomology
   is concentrated in degree 1.)
2. How far off-locus can the qi be pushed? Is there a DERIVED Koszul locus?
3. The coderived equivalence IS unconditional. Can it be upgraded to a genuine qi
   for specific non-Koszul families?
4. What families are NOT on the Koszul locus? (All standard VAs are Koszul — the
   locus is restrictive only for genuinely pathological algebras.)

Write a Research Remark characterising the Koszul locus and the off-locus obstruction.
mcp startup: no servers


thinking
**Planning commentary updates**

I’m considering how to maintain updates and clearly announce my next steps. I think I should start with "Using `beilinson-rectify` for the manuscript patch" and mention that `claim-surface-sync` will be used only if needed. I’ll also read the constitutional files and the target chapter before drafting. I’ll likely use `multi-path-verify` to explore alternative proof paths for verification while keeping the focus on one claim family, not rewriting the theorem architecture.
thinking
**Exploring file reading methods**

I’m thinking about how to work with the skills files. Maybe I can start by using the `cat` command to read the first lines. I could explore using some parallel execution commands, like `sed -n`, and look into the constitutional files too. Since I have multiple file reads to handle, I might want to use `multi_tool_use.parallel` with `exec` commands for those skills files. I’ll also need to inspect the file tree for better organization.
codex
Using `multi-path-verify` to pin down the Koszul-locus claim and `beilinson-rectify` to patch the chapter. I’m reading the constitutional files, the target theorem surface, and the relevant skill instructions before drafting the research remark.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

 succeeded in 53ms:
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
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
%% ===== Editorial bridge: the inversion half of the chapter =====
%%
%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
%% framework that supports it off the quadratic locus. This second half
%% proves that the adjunction inverts: Theorem B says
%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
%% Together, Theorems A and B close the algebraic engine of the monograph.

\bigskip
\noindent\textbf{From adjunction to inversion.}\enspace
An adjunction that is not an equivalence is a deficiency: it
records the information lost in the round trip. Theorem~A
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

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

 succeeded in 50ms:
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


thinking
**Exploring theorem details**

I need to keep reading the target file, focusing on theorem labels and possibly more relevant sections. I should locate Theorem B, the definition of Koszul-Lust, and remarks about off-locus. I could use rg to find specific details or consider using an explorer sub-agent, as it’s suggested for codebase questions. It sounds like a good idea to ask the explorer to summarize Theorem B and the Koszul locus definition to gather the necessary information. Let's go for it!
codex
I’ve loaded the constitutional surface and the target chapter. Next I’m tracing the exact theorem/definition chain for Theorem B, the Koszul-locus definition, and the existing off-locus coderived argument so the new remark lands on the right proof surface instead of floating as commentary.
collab spawn_agent(call_5yfIYLWgIyyEicm6cLRsuxx2, prompt="In /Users/raeez/chiral-bar-cobar, identify the exact theorem/definition chain relevant to Theorem B in chapters/theory/b…")
mcp startup: no servers
spawn_agent(call_5yfIYLWgIyyEicm6cLRsuxx2, prompt="In /Users/raeez/chiral-bar-cobar, identify the exact theorem/definition chain relevant to Theorem B in chapters/theory/b…") pending init:
  agent: 019d86aa-8e8a-7d13-b2c7-d81be34ba93f

Plan update
  → Survey repository for bar_cobar_adjunction_inversion.tex to locate Theorem B and context
  • Identify definition of Koszul locus and theorems for strict quasi-isomorphism on locus
  • Find unconditional coderived statements off-locus and remarks characterizing obstruction/collapse loci across Vol I/II/III
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'rg -n "Theorem B" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
6:%% proves that the adjunction inverts: Theorem B says
thinking
**Considering context for updates**

I think I might need to use an update plan since it looks substantial. But first, I should gather some context. Doing that soon would be ideal. I'll also need to search the target file for relevant terms, maybe using lines from rg. This should help me ensure that the update is well-informed and any changes I make are appropriate based on the information I find.
exec
/bin/zsh -lc 'rg -n "def:koszul-locus|thm:bar-cobar-inversion-qi|thm:higher-genus-inversion|coderived|collapse loci|collapse locus|coacyclic|Research Remark|research remark|Koszul locus|off-locus" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 333

chapters/theory/bar_cobar_adjunction_curved.tex:15:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
chapters/theory/bar_cobar_adjunction_curved.tex:20:is a quasi-isomorphism on the Koszul locus.
chapters/theory/bar_cobar_adjunction_curved.tex:32:$\Ainf$~algebras, $I$-adic completions, and coderived categories.
chapters/theory/bar_cobar_adjunction_curved.tex:75: $I$-adic completion required, work in coderived category
chapters/theory/bar_cobar_adjunction_curved.tex:389:coderived category
chapters/theory/bar_cobar_adjunction_curved.tex:392:coderived/contraderived setting.
chapters/theory/bar_cobar_adjunction_curved.tex:395:\begin{remark}[Derived--coderived reduction for chiral CDG-coalgebras]
chapters/theory/bar_cobar_adjunction_curved.tex:396:\label{rem:derived-coderived-chiral-CDG}
chapters/theory/bar_cobar_adjunction_curved.tex:397:\index{coderived category!derived reduction}
chapters/theory/bar_cobar_adjunction_curved.tex:398:\index{Positselski!derived--coderived reduction}
chapters/theory/bar_cobar_adjunction_curved.tex:401:between its coderived and ordinary derived categories:
chapters/theory/bar_cobar_adjunction_curved.tex:414: coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
chapters/theory/bar_cobar_adjunction_curved.tex:422:(H1) and $h = 0$ imply that every acyclic CDG-comodule is coacyclic, so
chapters/theory/bar_cobar_adjunction_curved.tex:428:The coderived category reduces to the ordinary derived category.
chapters/theory/bar_cobar_adjunction_curved.tex:429:This is the regime of Theorem~B (bar-cobar inversion on the Koszul locus).
chapters/theory/bar_cobar_adjunction_curved.tex:438:coderived--contraderived equivalence
chapters/theory/bar_cobar_adjunction_curved.tex:449:See Remark~\ref{rem:curvature-coderived} for the connection to
chapters/theory/bar_cobar_adjunction_curved.tex:451:\S\ref{subsec:chiral-coderived-contraderived} for the chiral
exec
/bin/zsh -lc 'rg -n "Koszul locus|derived Koszul|collapse locus|collapse loci|coderived|coacyclic-equivalence|strict quasi-isomorphism" chapters/theory chapters/examples chapters/connections /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1475

chapters/examples/lattice_foundations.tex:4489:\subsection{Bridge to Yangian derived Koszul duality}
chapters/examples/landscape_census.tex:799:extension to the ordinary-derived/completed/coderived enlargement and
chapters/examples/landscape_census.tex:1435: ordinary-derived/completed/coderived enlargement, and then the
chapters/examples/free_fields.tex:1864:The derived Koszul duality becomes the field-antifield correspondence in the BV formalism.
chapters/examples/free_fields.tex:1989:derived Koszul dual module.
chapters/examples/free_fields.tex:3673: $\En$-Koszul locus (where the bar spectral sequence
chapters/examples/free_fields.tex:3710:\index{factorization homology!as Fourier integral}\index{homotopy transfer!Fourier interpretation}\index{coderived category!Fourier interpretation}
chapters/examples/yangians_foundations.tex:8:theory. Its linear dual, on the chirally Koszul locus, is the Yangian.
chapters/examples/yangians_drinfeld_kohno.tex:750: \textup{(}Theorem~B on the Koszul locus\textup{)};
chapters/examples/yangians_drinfeld_kohno.tex:1017:infinite-dimensional modules via a completed or coderived
chapters/examples/yangians_drinfeld_kohno.tex:1511:\subsubsection*{Coderived factorization duality off the Koszul locus}
chapters/examples/yangians_drinfeld_kohno.tex:1513:On the Koszul locus (generic levels, evaluation-generated core),
chapters/examples/yangians_drinfeld_kohno.tex:1515:in the ordinary derived sense. Off the Koszul locus (at admissible
chapters/examples/yangians_drinfeld_kohno.tex:1519:coderived/contraderived category of
chapters/examples/yangians_drinfeld_kohno.tex:1525:\index{coderived category!factorization|textbf}
chapters/examples/yangians_drinfeld_kohno.tex:1526:\index{factorization co-contra comparison!off the Koszul locus}
chapters/examples/yangians_drinfeld_kohno.tex:1536:\item The factorization coderived category
chapters/examples/yangians_drinfeld_kohno.tex:1553: where the left side is the coderived category of conilpotent
exec
/bin/zsh -lc "sed -n '1,200p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 71ms:
%% ===== Editorial bridge: the inversion half of the chapter =====
%%
%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
%% framework that supports it off the quadratic locus. This second half
%% proves that the adjunction inverts: Theorem B says
%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
%% Together, Theorems A and B close the algebraic engine of the monograph.

\bigskip
\noindent\textbf{From adjunction to inversion.}\enspace
An adjunction that is not an equivalence is a deficiency: it
records the information lost in the round trip. Theorem~A
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

exec
/bin/zsh -lc 'rg -n "koszul-locus" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/dependency_graph.dot:3357:  cor_ordered_FG_koszul_locus [label="cor:ordered-FG-koszul-locus\ncorollary [Pr]\nKoszul dual on the associated graded", style=filled, fillcolor="#bbdefb"];
metadata/label_index.json:4678:  "cor:ordered-FG-koszul-locus": {
metadata/label_index.json:7110:  "def:koszul-locus": {
metadata/label_index.json:34482:  "rem:koszul-locus-off-locus-obstruction": {
metadata/claims.jsonl:3229:{"label": "cor:ordered-FG-koszul-locus", "env_type": "corollary", "status": "ProvedElsewhere", "file": "chapters/theory/koszul_pair_structure.tex", "line": 2322, "title": "Koszul dual on the associated graded"}
metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
standalone/ordered_chiral_homology.tex:1578:\label{def:koszul-locus}
standalone/ordered_chiral_homology.tex:3885:\textup{(}Definition~\textup{\ref{def:koszul-locus}}:
standalone/ordered_chiral_homology.tex:4930:  \textup{(}Definition~\textup{\ref{def:koszul-locus}}\textup{)}.
fix_wave_A_20260413_112727/A09_coderived_models.md:336:chapters/theory/bar_cobar_adjunction_inversion.tex:23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
fix_wave_A_20260413_112727/A08_cobar_construction.md:338:(Definition~\textup{\ref{def:koszul-locus}}).
audit_campaign_20260412_231034/T02_thm_B.md:651:I need to inspect theorem/reference `thm:bar-cobar-isomorphism-main`, especially since the base case or structural reason might be misnamed. My primary question here is about falsifying the proof of Theorem B, so I'll have to analyze it step by step. Additionally, I should look into the definition of the Koszul locus `def:koszul-locus` and see if it’s correctly used in the introduction and theorem. I'll do a search to gather more information.
audit_campaign_20260412_231034/T02_thm_B.md:653:/bin/zsh -lc "rg -n \"label\\{def:koszul-locus\\}|Koszul locus\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/frame/preface.tex chapters/frame/heisenberg_frame.tex chapters/theory/algebraic_foundations.tex chapters/theory/chiral_koszul_pairs.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/T02_thm_B.md:673:chapters/theory/algebraic_foundations.tex:236:\begin{definition}[Koszul locus]\label{def:koszul-locus}
audit_campaign_20260412_231034/T02_thm_B.md:694:\begin{definition}[Koszul locus]\label{def:koszul-locus}
audit_campaign_20260412_231034/T02_thm_B.md:1480:   236	\begin{definition}[Koszul locus]\label{def:koszul-locus}
wave2_audit_20260413_001942/F02_definitions_koszul.md:27:- [LOW] `chapters/theory/chiral_koszul_pairs.tex:48` — PROBLEM: the chapter uses `Koszul locus` before giving any local recall; the actual definition is hidden in `chapters/theory/algebraic_foundations.tex:236-245`. FIX: at the first occurrence, add `the Koszul locus \operatorname{Kosz}(X) of Definition~\ref{def:koszul-locus}, i.e. the full subcategory of augmented chiral algebras for which the genus-0 counit \Omega_X\barB_X(\cA)\to\cA is a quasi-isomorphism`.
wave2_audit_20260413_001942/F02_definitions_koszul.md:565:I need to focus on relevant portions of the file, especially around definitions and the equivalence theorem. I probably won't need all 6000 lines, just the core definitions and theorems. I should identify the exact theorem `thm:koszul-equivalences-meta` along with related definitions like `def:koszul-chiral-algebra` and `def:koszul-locus`. Let's also look into intrinsic characterizations and use exact labels for better clarity. Finally, I’ll check if the file builds correctly or references any unresolved issues.
wave2_audit_20260413_001942/F02_definitions_koszul.md:569:/bin/zsh -lc "rg -n \"thm:koszul-equivalences-meta|def:koszul-chiral-algebra|def:koszul-locus|10\\+1\\+1|twelve|eleven|thirteen|eigen|purity|D-module purity|Lagrangian eigenspace|Hochschild duality\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/F02_definitions_koszul.md:575:681:(Definition~\textup{\ref{def:koszul-locus}}).

exec
/bin/zsh -lc "sed -n '220,280p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{definition}

\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
\index{Koszul chiral algebra|textbf}
Let $X$ be a smooth projective curve over~$\CC$.
An augmented chiral algebra~$\cA$
(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
if the bar-cobar counit
\[
\varepsilon \colon
\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism at genus~$0$.
\end{definition}

\begin{definition}[Koszul locus]\label{def:koszul-locus}
\index{Koszul locus|textbf}
The \emph{Koszul locus} is the full subcategory
\[
thinking
**Inspecting existing research remarks**

I'm noticing there's already a Research Remark at lines 1930 and above. The user wants to add one, but maybe it's already there? I'll need to look at the section from around 1830 to 1995 closely. There's a chance that Theorem B has a secondary proof around 1861 too, so I should check its current state. Okay, I think I can use sed for this inspection.
exec
/bin/zsh -lc 'rg -n "thm:bar-cobar-inversion-qi" -n' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 1546

healing_20260413_132214/H02_thm_B_alt_proof.md:8:Theorem B (`thm:bar-cobar-inversion-qi`)
healing_20260413_132214/H02_thm_B_alt_proof.md:286:/bin/zsh -lc 'rg -n "thm:bar-cobar-inversion-qi" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H02_thm_B_alt_proof.md:287:21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
healing_20260413_132214/H02_thm_B_alt_proof.md:288:138:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
healing_20260413_132214/H02_thm_B_alt_proof.md:289:690:(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
healing_20260413_132214/H02_thm_B_alt_proof.md:290:1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
healing_20260413_132214/H02_thm_B_alt_proof.md:291:1713:Theorem~\ref{thm:bar-cobar-inversion-qi}; the concrete mechanism by
healing_20260413_132214/H02_thm_B_alt_proof.md:292:1761:Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
healing_20260413_132214/H02_thm_B_alt_proof.md:293:1861:Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
healing_20260413_132214/H02_thm_B_alt_proof.md:294:1938:Theorem~\ref{thm:bar-cobar-inversion-qi}. Then:
healing_20260413_132214/H02_thm_B_alt_proof.md:295:1980:At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is a
healing_20260413_132214/H02_thm_B_alt_proof.md:296:1992:Theorem~\ref{thm:bar-cobar-inversion-qi} is invoked to verify
healing_20260413_132214/H02_thm_B_alt_proof.md:297:2011:quasi-isomorphism. Theorem~\ref{thm:bar-cobar-inversion-qi} is
healing_20260413_132214/H02_thm_B_alt_proof.md:298:2018:At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is
healing_20260413_132214/H02_thm_B_alt_proof.md:299:2076:Theorem~\ref{thm:bar-cobar-inversion-qi} converts the bar coalgebra
healing_20260413_132214/H02_thm_B_alt_proof.md:300:2187:For the application to Theorem~\ref{thm:bar-cobar-inversion-qi}, the completeness statement in Definition~\ref{def:bar-cobar-filtration}(2) is supplied by its conilpotency/completion hypothesis: if $\bar{B}(\mathcal{A})$ is conilpotent in the sense of Definition~\ref{def:conilpotent-complete}, every element has finite bar degree, while in the augmentation-ideal completion regime the filtration is complete by construction.
healing_20260413_132214/H02_thm_B_alt_proof.md:301:2247:Theorem~\ref{thm:bar-cobar-inversion-qi}. The bar-cobar inversion
healing_20260413_132214/H02_thm_B_alt_proof.md:302:2441:(Theorem~\ref{thm:bar-cobar-inversion-qi}) establishes the
codex
The grep surfaced that the target file already contains a `Research remark: the Koszul locus and the off-locus obstruction` block. I’m reading that local band now to decide whether it already answers the research question or whether it needs tightening and better characterization.
exec
/bin/zsh -lc "sed -n '395,470p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1760,2015p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
concentrated on the Koszul diagonal, and
Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
level $k = -1/2$ lies outside the Koszul locus because the
representation category
$\mathrm{KL}_{-1/2}(\mathfrak{sl}_2)$
(Arakawa~\cite{Arakawa17, Arakawa2016RationalAdmissible}) is a
non-semisimple finite tensor category whose singular vectors
obstruct the diagonal concentration.
For the critical-level analogue $k = -h^\vee = -2$, the
Feigin--Frenkel center~\cite{Feigin-Frenkel} causes an even more
dramatic failure: the center of
$V_{-2}(\mathfrak{sl}_2)$ jumps in dimension and the bar complex
acquires infinitely many off-diagonal classes.
\end{example}

\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
\label{rem:admissible-2-koszul}%
\index{2-Koszul!admissible level}%
\index{admissible level!2-Koszul}%
The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
 succeeded in 52ms:
\begin{remark}[Derived--coderived reduction for chiral CDG-coalgebras]
\label{rem:derived-coderived-chiral-CDG}
\index{coderived category!derived reduction}
\index{Positselski!derived--coderived reduction}
The chiral bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$ is a CDG-coalgebra
with curvature $h = m_0^{(g)}$. Three hypotheses govern the relationship
between its coderived and ordinary derived categories:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item \emph{Conilpotency}: $C$ is conilpotent, i.e., the coaugmentation
 filtration is exhaustive. This holds by
 Theorem~\ref{thm:coalgebra-via-NAP}(4): the conformal weight grading
 on $\bar{B}^{\mathrm{ch}}(\cA)$ provides an exhaustive
 $\mathbb{N}$-filtration with $C = \bigcup_n F^n C$.
\item \emph{Finite-type weight spaces}: each graded piece of $C$ is
 finite-dimensional. This holds because $\cA$ is finitely generated
 with finite-dimensional conformal weight spaces (the positive-energy
 axiom), so $\bar{B}^n(\cA)$ in each weight is a finite-dimensional
 vector space.
\item \emph{Compact generation}: (H1) and (H2) together imply that the
 coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
exec
/bin/zsh -lc "sed -n '680,740p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4924,4995p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1)
\simeq \Omega_X(\cC_2)
\]
is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
a statement about the factorization algebra obtained after applying
$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
the counit quasi-isomorphism
$\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
Theorem~\ref{thm:fundamental-twisting-morphisms}.
The Heisenberg pair
$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$ is the
prototype (\S\ref{sec:frame-koszul-dual}).

\smallskip\noindent
In particular, each algebra~$\cA_i$ in a chiral Koszul pair is a
Koszul chiral algebra in the sense of
Definition~\textup{\ref{def:koszul-chiral-algebra}}, and hence lies on
the Koszul locus~$\operatorname{Kosz}(X)$
(Definition~\textup{\ref{def:koszul-locus}}).
 succeeded in 53ms:
\subsection{The coderived Ran-space formalism}
\label{subsec:coderived-ran}

The bar-cobar adjunction is an equivalence of
$\infty$-categories, the categorical $\exp/\log$ correspondence
(Remark~\ref{rem:nilpotence-periodicity}):
\[
\bar{B}_X \colon
\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
\;\rightleftarrows\;
\operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
\,:\!\Omega_X,
\]
where $\operatorname{Fact}(X)$ denotes factorization algebras on
$\operatorname{Ran}(X)$ (cf.\ Appendix~\ref{app:existence-criteria}).

On the Koszul locus this is an equivalence: $\exp \circ \log = \mathrm{id}$
on the convergence domain. When curvature is present (that is,
when the categorical logarithm acquires non-trivial monodromy), the
theorem-level statement moves from ordinary derived categories to the
exec
/bin/zsh -lc "sed -n '1580,1750p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 finite-dimensional graded pieces, which is
 needed for the duality between contramodules and complete modules
 (Remark~\ref{rem:chiral-contramodules}).
\end{enumerate}
These geometric inputs are specific to the chiral setting and have
no analogue in Positselski's ground-field framework.
\end{remark}

%================================================================
% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
%================================================================

\section{Bar-cobar inversion}
\label{sec:bar-cobar-inversion-quasi-iso}

The comodule-contramodule correspondence of the preceding section
provides the categorical framework in which bar-cobar inversion
lives: at genus~$0$ the coderived category reduces to the
ordinary derived category, and the inversion theorem is a
quasi-isomorphism in the classical sense; at genus~$g \geq 1$
exec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '220,280p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   220	\end{enumerate}
   221	\end{definition}
   222	
   223	\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
   224	\index{Koszul chiral algebra|textbf}
   225	Let $X$ be a smooth projective curve over~$\CC$.
   226	An augmented chiral algebra~$\cA$
   227	(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
   228	if the bar-cobar counit
   229	\[
   230	\varepsilon \colon
   231	\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
   232	\]
   233	is a quasi-isomorphism at genus~$0$.
   234	\end{definition}
   235	
   236	\begin{definition}[Koszul locus]\label{def:koszul-locus}
   237	\index{Koszul locus|textbf}
   238	The \emph{Koszul locus} is the full subcategory
   239	\[


thinking
**Identifying theorem and definition references**

I’m gathering the relevant theorem labels related to Theorem B on strict quasi-isomorphisms in the bar-cobar inversion theory, focusing on referencing definitions of the Koszul locus and related theorems like `thm:bar-cobar-inversion-qi`, `thm:bar-cobar-spectral-sequence`, and `thm:spectral-sequence-collapse`. I plan to use search tools to find exact file locations and line numbers to document these connections clearly.
exec
/bin/zsh -lc 'rg -n "bar-cobar-spectral-sequence" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1673: Theorems~\ref{thm:bar-cobar-spectral-sequence}
1743:Theorems~\ref{thm:bar-cobar-spectral-sequence}
1789:\textup{(}Theorems~\ref{thm:bar-cobar-spectral-sequence}
1837:Theorems~\ref{thm:bar-cobar-spectral-sequence}
1862:bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
1948:Theorem~\ref{thm:bar-cobar-spectral-sequence},
2204:The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
2209:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
2276:strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
2277:Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
2293:Theorems~\ref{thm:bar-cobar-spectral-sequence}
thinking
**Clarifying algebraic concepts**

I'm thinking about how to strengthen my response by naming specific examples or families. I need to verify which families are actually not on the locus. The user mentioned that all standard VAs are Koszul, but I want to check whether that's right, especially regarding pathological algebras. There's a note that generic Virasoro might be on the locus, particularly for principal W-families. I need to confirm if "Koszul" applies broadly or if it’s more restricted, so I'll search for the definition of Koszul locus and the relevant theorem.
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{definition\\}\\[.*Koszul locus|\\\\label\\{def:koszul-locus\\}|\\\\begin\\{theorem\\}\\[.*bar-cobar inversion|\\\\label\\{thm:bar-cobar-inversion-qi\\}|\\\\label\\{thm:off-koszul-ran-inversion\\}|\\\\label\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\label\\{thm:conilpotent-reduction\\}\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\begin\{definition\}\[.*Koszul locus|\label\{def:koszul-locus\}|\begin\{theorem\}\[.*bar-cobar inversion|\label\{thm:bar-cobar-inversion-qi\}|\label\{thm:off-koszul-ran-inversion\}|\label\{prop:coderived-bar-degree-spectral-sequence\}|\label\{thm:conilpotent-reduction\})
                                            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '1540,1875p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '870,980p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[No cohomology for CDG-comodules]
\label{rem:no-CDG-cohomology}
Since $d^2 \neq 0$ in a CDG-comodule (when $h \neq 0$), there is no
notion of cohomology, so the ordinary
derived category is inadequate at higher genus: one cannot define
acyclic objects via vanishing cohomology. The correct
substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
\end{remark}

\subsection{Chiral cotensor and cohomomorphism complexes}
\label{subsec:chiral-cotensor}

\begin{definition}[Chiral cotensor product]\label{def:chiral-cotensor}
\index{cotensor product!chiral}
Let $(C, d, h)$ be a chiral CDG-coalgebra, $N$ a right chiral
CDG-comodule, and $M$ a left chiral CDG-comodule. The
\emph{chiral cotensor product} $N \square_C^{\mathrm{ch}} M$ is
the equalizer:
\[
 succeeded in 51ms:
equivalence. On the quadratic genus-$0$ bar-dual surface, the
identification $C^*\cong \cA^!$ is supplied by
Theorem~\ref{thm:bar-computes-dual}, recovering
Theorem~\ref{thm:e1-module-koszul-duality}.
\end{proof}

\begin{remark}[Relation to genus-0 module Koszul duality]
\label{rem:genus-0-recovery}
At genus~$0$, the curvature $h = 0$, so CDG-comodules reduce to
DG-comodules, the coderived category reduces to the ordinary derived
category, and on the quadratic bar-dual surface the completed-dual
algebra $C^*=\barB^{\mathrm{ch}}(\cA)^*$ identifies with~$\cA^!$.
Theorem~\ref{thm:full-derived-module-equiv-proved} is precisely the
flat finite-type reduction that then recovers the ordinary
genus-$0$ module Koszul duality of
Theorem~\ref{thm:e1-module-koszul-duality}.
The coderived/contraderived framework generalizes to genus~$g \geq 1$, where the
curvature $m_0^{(g)} \neq 0$ prevents replacing the exotic
categories by ordinary derived categories without extra flatness input.
\end{remark}
exec
/bin/zsh -lc 'rg -n "coderived" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
27:the same counit remains invertible in the coderived
31:The curved proof uses the coderived bar-degree filtration: the
659:The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
683:\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
684:\label{rem:coderived-status}%
685:\index{coderived category!status}%
691:On the quadratic genus-$0$ bar-dual surface, the coderived
699:($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
706:these classes \emph{control} the coderived category at each genus via a
708:adjunction to extend to a coderived Quillen equivalence. The intrinsic
719:\item Construct the coderived model structure on curved chiral
723:\item Identify the coderived shadow invariants with the proved
877:substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
971:\label{subsec:chiral-coderived-contraderived}
974:\label{def:chiral-coderived}
975:\index{coderived category!chiral|textbf}
1007:\label{eq:chiral-coderived}\\
1067: the coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
1330:the contraderived and coderived categories
1435:bar coalgebra. Its intrinsic output is a coderived/contraderived
exec
/bin/zsh -lc 'rg -n "off-koszul" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1826:Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
1923:Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
exec
/bin/zsh -lc "rg -n \"def:koszul-locus|begin\\{definition\\}\\[Koszul locus|Koszul locus of\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1295p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:699:(Definition~\textup{\ref{def:koszul-locus}}).
chapters/theory/chiral_koszul_pairs.tex:4049:In this $\infty$-categorical formulation, the Koszul locus of the
chapters/theory/bar_cobar_adjunction_inversion.tex:23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
chapters/theory/bar_cobar_adjunction_inversion.tex:1712:This algebra is excluded from the Koszul locus of
chapters/theory/bar_cobar_adjunction_inversion.tex:1937:$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
chapters/theory/bar_cobar_adjunction_inversion.tex:2514:Koszul locus of finite-type chiral algebras. The programmatic regime
chapters/theory/higher_genus_modular_koszul.tex:35049:denotes the local Koszul locus of
 succeeded in 52ms:
 $\Phi_C^{\mathrm{ch}}(P)$ to be the left chiral CDG-comodule
 whose underlying graded $\mathcal{D}_X$-module is the
 chiral contratensor product $C \odot_C^{\mathrm{ch}} P$.
 Concretely, $\Phi_C^{\mathrm{ch}}(P)$ is a quotient of
 $C \chirtensor P$; the comodule structure comes from the
 comultiplication on the left factor~$C$, and the differential is
 induced by the differentials on $C$ and $P$ via the standard
 formula for the tensor product of graded $\mathcal{D}_X$-modules
 with differentials.
\item For a left chiral CDG-comodule $M$, define
 $\Psi_C^{\mathrm{ch}}(M)$ to be the left chiral CDG-contramodule
 whose underlying graded $\mathcal{D}_X$-module is
 $\mathrm{Hom}_C^{\mathrm{ch}}(C, M) = \mathrm{Cohom}_C^{\mathrm{ch}}(C, M)$.
 The contramodule structure comes from the comultiplication
 on $C$, and the differential is induced from $d_C$ and $d_M$.
\end{itemize}
These define DG-functors:
\begin{align*}
\Phi_C^{\mathrm{ch}}\colon \mathrm{DG}(C\text{-}\mathrm{contra}^{\mathrm{ch}})
&\longrightarrow \mathrm{DG}(C\text{-}\mathrm{comod}^{\mathrm{ch}}), \\
exec
/bin/zsh -lc 'rg -n "off-koszul-ran-inversion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 442

audit_campaign_20260412_231034/T04_thm_C1.md:1228:  4940	(Theorem~\ref{thm:off-koszul-ran-inversion}): the counit
healing_20260413_130533/H02_thm_B_alt_proof.md:847:I’ve noticed that there are some existing theorems I could cite. For instance, there's a theorem in chiral_koszul_pairs regarding the equivalence between E_2 collapse and A_infinity formality using Keller. I could definitely reference that. Additionally, there's the Kontsevich formality in the cobar construction. I should also check results related to curvature filtration and coderived spectral sequences. I need to look up specific labels and propositions like coderived-bar-degree-spectral-sequence and theorem off-koszul-ran-inversion to support my work.
healing_20260413_130533/H02_thm_B_alt_proof.md:852:/bin/zsh -lc 'rg -n "off-koszul-ran-inversion|coderived-bar-degree-spectral-sequence|conilpotent-reduction|full-derived-module-equiv-proved|positselski-chiral-proved|fundamental-twisting-morphisms|bar-nilpotency-complete|chiral-koszul-duality|ainfty-formality-implies-koszul|e2-formality-hochschild|shadow-formality-low-degree|bar concentration|PBW spectral sequence" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/coderived_models.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
healing_20260413_130533/H02_thm_B_alt_proof.md:879:chapters/theory/coderived_models.tex:367:\textup{(}Theorem~\ref{thm:off-koszul-ran-inversion}\textup{)}
healing_20260413_130533/H02_thm_B_alt_proof.md:880:chapters/theory/coderived_models.tex:423:and~\ref{thm:off-koszul-ran-inversion}\textup{)}. The full
healing_20260413_130533/H02_thm_B_alt_proof.md:882:chapters/theory/coderived_models.tex:901:\label{thm:off-koszul-ran-inversion}
healing_20260413_130533/H02_thm_B_alt_proof.md:883:chapters/theory/coderived_models.tex:983:Theorem~\ref{thm:off-koszul-ran-inversion} resolves
healing_20260413_130533/H02_thm_B_alt_proof.md:995:\label{thm:off-koszul-ran-inversion}
healing_20260413_130533/H02_thm_B_alt_proof.md:1015:Theorem~\ref{thm:off-koszul-ran-inversion} resolves
metadata/dependency_graph.dot:2580:  thm_off_koszul_ran_inversion [label="thm:off-koszul-ran-inversion\ntheorem [Pr]\nOff-Koszul bar-cobar inversion on Ran", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:542:| `thm:off-koszul-ran-inversion` | `theorem` | 917 | Off-Koszul bar-cobar inversion on Ran |
metadata/label_index.json:50414:  "thm:off-koszul-ran-inversion": {
healing_20260413_132214/H02_thm_B_alt_proof.md:491:/bin/zsh -lc "rg -n \"Keller|ainfty-koszul-characterization|prop:en-formality|shadow-formality-low-degree|coderived-bar-degree-spectral-sequence|off-koszul-ran-inversion|higher-genus-inversion|quadratic closure|formal neighborhood|tangent complex|curvature filtration\" chapters metadata appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_132214/H02_thm_B_alt_proof.md:669:/bin/zsh -lc "rg -n \"\\\\label\\{thm:htt\\}|homotopy transfer theorem|\\\\label\\{thm:ainfty-koszul-characterization\\}|\\\\label\\{prop:en-formality\\}|\\\\label\\{prop:shadow-formality-low-degree\\}|\\\\label\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H02_thm_B_alt_proof.md:671:   917	\label{thm:off-koszul-ran-inversion}
healing_20260413_132214/H02_thm_B_alt_proof.md:735:    (?:\label\{thm:htt\}|homotopy transfer theorem|\label\{thm:ainfty-koszul-characterization\}|\label\{prop:en-formality\}|\label\{prop:shadow-formality-low-degree\}|\label\{prop:coderived-bar-degree-spectral-sequence\}|\label\{thm:off-koszul-ran-inversion\})
healing_20260413_132214/H02_thm_B_alt_proof.md:761:/bin/zsh -lc "rg -n \"label\\{thm:ainfty-koszul-characterization\\}|label\\{prop:en-formality\\}|label\\{prop:shadow-formality-low-degree\\}|label\\{prop:coderived-bar-degree-spectral-sequence\\}|label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H02_thm_B_alt_proof.md:778:chapters/theory/coderived_models.tex:917:\label{thm:off-koszul-ran-inversion}

thinking
**Searching for definitions**

I think I might have used the wrong region, so I need to correctly define the line. I could use `rg` to search through the file to find the exact line of interest, maybe around line 1300. It seems I've identified a target that might actually be beyond 1340. Let's specifically search for "Koszul locus" in that file to gather more information. That should help narrow things down!
exec
/bin/zsh -lc 'rg -n "prop:coderived-bar-degree-spectral-sequence" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 475

relaunch_20260413_111534/R19_coderived_models.md:359:metadata/claims.jsonl:2147:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1606, "title": "Bar-cobar inversion: strict on the Koszul locus, coderived off it", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "sec:i-adic-completion", "def:koszul-chiral-algebra", "thm:higher-genus-inversion", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "prop:coderived-bar-degree-spectral-sequence", "thm:bar-cobar-spectral-sequence", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse", "thm:positselski-chiral-proved", "thm:full-derived-module-equiv-proved"]}
relaunch_20260413_111534/R19_coderived_models.md:371:537:| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 306 | Coderived bar-degree spectral sequence |
relaunch_20260413_111534/R19_coderived_models.md:795:| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 306 | Coderived bar-degree spectral sequence |
healing_20260413_132214/H02_thm_B_alt_proof.md:580:/bin/zsh -lc 'rg -n "prop:coderived-bar-degree-spectral-sequence" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_132214/H02_thm_B_alt_proof.md:581:1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
healing_20260413_132214/H02_thm_B_alt_proof.md:582:1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
healing_20260413_132214/H02_thm_B_alt_proof.md:583:1913:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
healing_20260413_132214/H02_thm_B_alt_proof.md:584:2231:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
healing_20260413_132214/H02_thm_B_alt_proof.md:604: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
healing_20260413_132214/H02_thm_B_alt_proof.md:669:/bin/zsh -lc "rg -n \"\\\\label\\{thm:htt\\}|homotopy transfer theorem|\\\\label\\{thm:ainfty-koszul-characterization\\}|\\\\label\\{prop:en-formality\\}|\\\\label\\{prop:shadow-formality-low-degree\\}|\\\\label\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H02_thm_B_alt_proof.md:708:   316	\label{prop:coderived-bar-degree-spectral-sequence}
healing_20260413_132214/H02_thm_B_alt_proof.md:735:    (?:\label\{thm:htt\}|homotopy transfer theorem|\label\{thm:ainfty-koszul-characterization\}|\label\{prop:en-formality\}|\label\{prop:shadow-formality-low-degree\}|\label\{prop:coderived-bar-degree-spectral-sequence\}|\label\{thm:off-koszul-ran-inversion\})
healing_20260413_132214/H02_thm_B_alt_proof.md:761:/bin/zsh -lc "rg -n \"label\\{thm:ainfty-koszul-characterization\\}|label\\{prop:en-formality\\}|label\\{prop:shadow-formality-low-degree\\}|label\\{prop:coderived-bar-degree-spectral-sequence\\}|label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H02_thm_B_alt_proof.md:777:chapters/theory/coderived_models.tex:316:\label{prop:coderived-bar-degree-spectral-sequence}
healing_20260413_132214/H02_thm_B_alt_proof.md:921:I'm gathering precise file paths and line numbers from the repository, especially from `chapters/theory/bar_cobar_adjunction_inversion.tex`, to point out where Keller, deformation retracts, formality, Koszul locus, tangent complexes, and curvature filtration are discussed. I'll highlight theorem statements near line 1606, remarks around 1860-1925 that mention "Keller's classicality theorem" and deformation retracts, plus related propositions and definitions such as `prop:coderived-bar-degree-spectral-sequence`, `Definition\ref{def:bar-cobar-filtration}`, and `Theorem\ref{thm:bar-cobar-spectral-sequence}`. I’ll also check other files like `appendices/homotopy_transfer.tex` and `standalone/introduction_full_survey.tex` for supporting references while sticking to exact file and line citations without ranges. This way, I can confirm whether the repo already contains textual evidence to support alternative remarks on these topics.
healing_20260413_132214/H02_thm_B_alt_proof.md:986:1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
healing_20260413_132214/H02_thm_B_alt_proof.md:987:1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
healing_20260413_132214/H02_thm_B_alt_proof.md:988:1913:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
exec
/bin/zsh -lc 'rg -n "Koszul locus|def:koszul-locus|Koszul diagonal|bar degree equal to internal degree" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
22:answer in two layers: on the Koszul locus
23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
26:(Theorem~\ref{thm:genus-graded-convergence}); off the Koszul locus,
686:The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1635: If, in addition, $\mathcal{A}$ lies on the higher-genus Koszul locus
1679: the relevant off-Koszul locus
1712:This algebra is excluded from the Koszul locus of
1734:this relation produces bar cohomology off the Koszul diagonal:
1737:degree~$n$ (the ``Koszul diagonal''), whereas at $k = -1/2$ the
1760:concentrated on the Koszul diagonal, and
1762:level $k = -1/2$ lies outside the Koszul locus because the
1885:$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
1899:Koszul locus these obstructions vanish, so the transferred
1917:Off the Koszul locus the same deformation-retract package survives
1930:\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
1932:\index{Koszul locus!off-locus obstruction}
1934:The phrase ``Koszul locus'' in
1937:$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
exec
/bin/zsh -lc "sed -n '650,735p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '280,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   280	$\Omega_X \barB_X(\cA)$ and~$\cA$ is bounded below, exhaustive, and
   281	preserved by~$\varepsilon$. Hence $K$ inherits a bounded-below
   282	filtration. Its filtration-preserving differential is the strict
   283	Chevalley--Cousin differential: the curved correction inserts at
   284	least one diagonal contraction, so it lands in $F^1$ and disappears
   285	from $\operatorname{gr}^0 K$. Thus each graded piece of
   286	$\operatorname{gr} K$ is the cone of the strict
   287	Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
   288	Cousin-filtration argument gives that strict counit as a
   289	quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
   290	the filtered cone vanishes. This proof is independent of
   291	Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
   292	curvature-zero Cousin model together with Positselski's filtered
   293	coacyclicity criterion. By
   294	\cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
   295	curved object with acyclic associated graded is coacyclic.
   296	Therefore $K$ lies in the thick subcategory generated by
   297	totalizations of short exact sequences and infinite direct sums, so
   298	$\varepsilon$ is a coacyclic-equivalence and hence an isomorphism in
   299	$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
 succeeded in 52ms:
\item Does it have composite operators? $\Rightarrow$ Must complete
\item Is the generating space infinite-dimensional? $\Rightarrow$ handled by the MC4 completion theorem (Theorem~\ref{thm:completed-bar-cobar-strong}); residual task is to identify the filtered H-level target and its finite quotients by explicit coefficient identities and finite detection
\end{enumerate}

Most vertex algebras from CFT are either quadratic or curved with finite-dimensional
$\bar{B}^1$, so Koszul duality applies.
\end{remark}

\iffalse
The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
\fi
%%% END COMMENTED-OUT: Four-class exposition

\section{Chiral coalgebra homological algebra}
\label{sec:chiral-coalgebra-homalg}
\index{chiral coalgebra!homological algebra|textbf}
\index{Positselski!chiral lift|textbf}

The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra
(Theorem~\ref{thm:bar-chiral}). At genus~$0$, it is a

exec
/bin/zsh -lc "sed -n '1910,1945p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Searching for definitions**

I see there's a remark, but it doesn't provide a definition. I think I really need to locate the actual definition, which might be in another file. I should search for the label, making sure to use "rg" for the label exactly across the entire repository. That should help me find the information I’m looking for. I just want to ensure I get it right!
exec
/bin/zsh -lc "rg -n \"label\\{def:koszul-locus\\}\" chapters/theory /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/algebraic_foundations.tex:236:\begin{definition}[Koszul locus]\label{def:koszul-locus}
exec
/bin/zsh -lc "sed -n '1945,2005p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
\textup{(}bar degree equal to internal degree, or after the
reindexing used in
Theorem~\ref{thm:bar-cobar-spectral-sequence},
concentrated in bar degree~$1$\textup{)}. For a quadratic
$A_\infty$ model this recovers the classical Priddy/BGS criterion:
the bar cohomology is concentrated in weight~$1$.

The obstruction off the locus is equally concrete: the first
off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
strict square-zero proof loses diagonal concentration, higher
differentials need not vanish, and the cone of the counit can stop
being acyclic in the ordinary derived category. In the quotient
examples already isolated in the manuscript, this class is created by
a null-vector ideal or a non-flat PBW degeneration: singular vectors
enter the bar-relevant range, or composite relations survive in bar
degree $\geq 2$, so the PBW collapse no longer forces strict
inversion.

exec
/bin/zsh -lc 'rg -n "rem:koszul-locus-off-locus-obstruction" -n' in /Users/raeez/chiral-bar-cobar succeeded in 87ms:
healing_20260413_130533/H14_remove_koszul_locus.md:1224:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1300:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1376:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1450:/bin/zsh -lc "rg -n '\\\\label\\{rem:koszul-locus-off-locus-obstruction\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_130533/H14_remove_koszul_locus.md:1491:/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1931:\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1504:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1673:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1759:+\label{rem:koszul-locus-off-locus-obstruction}
healing_20260413_130533/H14_remove_koszul_locus.md:1852:+\label{rem:koszul-locus-off-locus-obstruction}
chapters/theory/bar_cobar_adjunction_inversion.tex:1931:\label{rem:koszul-locus-off-locus-obstruction}
exec
/bin/zsh -lc "sed -n '220,290p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{definition}

\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
\index{Koszul chiral algebra|textbf}
Let $X$ be a smooth projective curve over~$\CC$.
An augmented chiral algebra~$\cA$
(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
if the bar-cobar counit
\[
\varepsilon \colon
\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism at genus~$0$.
\end{definition}

\begin{definition}[Koszul locus]\label{def:koszul-locus}
\index{Koszul locus|textbf}
The \emph{Koszul locus} is the full subcategory
\[
exec
/bin/zsh -lc 'rg -n "Koszul locus" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 304

/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:149:**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)<->(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/kodaira_spencer_e1_engine.py:472:    The bar-cobar adjunction: Omega(B(A_{KS})) ~= A_{KS} (on Koszul locus).
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:114:(A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has its own derived center. (B)<->(C) via Drinfeld associator on the Koszul locus. NEVER conflate.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:257:- AP161: Five notions of E_1-chiral algebra are NOT interchangeable. (A)-(E) each have own derived center. (B)<->(C) on Koszul locus only. Counter: specify which notion.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:273:- AP174: Chiral QG equivalence scope. Proved abstractly on Koszul locus. Concrete verification: sl_2 Yangian and affine KM only. Elliptic partial; toroidal absent. FORBIDDEN: "equivalence for all four families."
/Users/raeez/calabi-yau-quantum-groups/compute/lib/e1_bar_cobar_cy3.py:50:   Bar-cobar inversion holds on the Koszul locus: the counit
/Users/raeez/calabi-yau-quantum-groups/compute/lib/e1_bar_cobar_cy3.py:671:    on the Koszul locus.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/e1_bar_cobar_cy3.py:694:        The Koszul locus for E₁ is BROADER than for E_∞: an algebra
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1058:conjectural beyond the Koszul locus).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1106: On the Koszul locus the counit
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1124: $\mathrm{ChirHoch}^*(\cA)$ is polynomial on the Koszul locus at
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1140:physical hypotheses. On the chirally Koszul locus, the
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1169:\item \emph{On the chirally Koszul locus:}
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:104:- **MODERATE -- "scoped identifications" phrasing (lines 449--456).** "The scoped identifications C_line ≃ A^!_line-mod and Abulk ≃ Z_der(Bbound) ≃ HH^bullet_ch(A^!_line) assemble these faces into the bulk-boundary-line triangle (Theorems~\ref{thm:boundary-linear-bulk-boundary} and \ref{thm:lines_as_modules}) on the boundary-linear exact sector and on the chirally Koszul locus respectively." The phrase "boundary-linear exact sector... chirally Koszul locus respectively" pairs the two conditions with the two identifications -- but which scope goes with which? The reader has to match by order. MODERATE: rewrite as "... on the boundary-linear exact sector (for Abulk) and on the chirally Koszul locus (for C_line)" would disambiguate. The content is right, the pairing is unclear.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:464:   Fix: rewrote part~(iii) so the unconditional statement is the bulk-to-chiral-Hochschild quasi-isomorphism, with the stronger derived-center identification only under the compact-generation / boundary-linear hypotheses; rewrote part~(iv) to require the chirally Koszul locus; kept part~(v) at the level of perturbative line operators; and aligned the proof and packaging remarks with those scoped statements.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:472:   Fix: propagated the scope repair across the active summary surface: the abstract now distinguishes the unconditional Hochschild statement from the boundary-linear derived-center statement; the preface and introduction place the line-module identification on the chirally Koszul locus; the conclusion replaces the stale all-genera theorem advertisement with the ordered/open `E_1` persistence statement; the frontier target now states its compact-generation and chirally Koszul hypotheses explicitly; and the core chapter now cites Theorem~`thm:boundary-linear-bulk-boundary` directly at the load-bearing point.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:502:   Fix: rewrote those summary passages so the unconditional statement is the bulk-to-chiral-Hochschild identification, the derived-center comparison is tied to the boundary-linear exact sector, and the line-module identification is explicitly confined to the chirally Koszul locus. The introduction now names the theorem package itself as scoped.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:510:   Fix: replaced the closed-colour clause by `$A_{\mathrm{bulk}} \simeq C^\bullet_{\mathrm{ch}}(\Bbound,\Bbound)$` and kept the open-colour `\cA^!`-module identification only on the chirally Koszul locus.
exec
/bin/zsh -lc "sed -n '290,345p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
These equivalences are special cases of the ten unconditional
equivalences~\textup{(i)--(x)} proved in
Theorem~\textup{\ref{thm:koszul-equivalences-meta}}
(Chapter~\textup{\ref{chap:koszul-pairs}}).
Off the Koszul locus, the bar complex is curved and lives in
the coderived category (Appendix~\ref{sec:coderived-models});
the categorical logarithm has monodromy.
\end{remark}

\noindent
The definition above identifies Koszulness with the bar-cobar
counit being a quasi-isomorphism.
Chapter~\ref{chap:koszul-pairs} introduces the antecedent
recognition data: a chiral twisting datum
(Definition~\ref{def:chiral-twisting-datum}) and a Koszul twisting
morphism (Definition~\ref{def:chiral-koszul-morphism},
Theorem~\ref{thm:fundamental-twisting-morphisms}); bar-cobar
identifications are then proved as consequences on the Koszul locus.
The full chiral Koszul pair is
collab wait(call_4gSrM8W8zxOc6bzVZK8O8Kh0)
  receivers: 019d86aa-8e8a-7d13-b2c7-d81be34ba93f
exec
/bin/zsh -lc "sed -n '2180,2225p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}
The deconcatenation coproduct
$\Delta\colon s^{-1}\bar\cA^{\otimes n} \to
\bigoplus_{p+q=n} s^{-1}\bar\cA^{\otimes p}
\otimes s^{-1}\bar\cA^{\otimes q}$
is a purely combinatorial operation on ordered tensor products:
it splits a word into a left factor and a right factor along each
position. This splitting depends only on the linear ordering of
the inputs (the $\Conf_k^{<}(\R)$ factor), not on the holomorphic
collision data (the $\FM_k(\C)$ factor) or on the genus of the
underlying curve. The genus-$g$ deformation
$\dfib^{\,2} = \kappa \cdot \omega_g$
(Construction~\ref{constr:tautological-bundle}) acts entirely on the
closed-colour differential; the open-colour coproduct is blind to it.
\end{proof}

\begin{remark}[Perturbative/non-perturbative as clean/excess intersection]
\label{rem:steinberg-perturbative}
\index{perturbative!clean Steinberg intersection}
The Steinberg presentation sharpens the perturbative/non-perturbative
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex | sed -n '2184,2230p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2184	\otimes s^{-1}\bar\cA^{\otimes q}$
  2185	is a purely combinatorial operation on ordered tensor products:
  2186	it splits a word into a left factor and a right factor along each
  2187	position. This splitting depends only on the linear ordering of
  2188	the inputs (the $\Conf_k^{<}(\R)$ factor), not on the holomorphic
  2189	collision data (the $\FM_k(\C)$ factor) or on the genus of the
  2190	underlying curve. The genus-$g$ deformation
  2191	$\dfib^{\,2} = \kappa \cdot \omega_g$
  2192	(Construction~\ref{constr:tautological-bundle}) acts entirely on the
  2193	closed-colour differential; the open-colour coproduct is blind to it.
  2194	\end{proof}
  2195	
  2196	\begin{remark}[Perturbative/non-perturbative as clean/excess intersection]
  2197	\label{rem:steinberg-perturbative}
  2198	\index{perturbative!clean Steinberg intersection}
  2199	The Steinberg presentation sharpens the perturbative/non-perturbative
  2200	divide. On the Koszul locus the self-intersection is \emph{clean}:
  2201	the derived fibers $\operatorname{Tor}^{\cO(\mathscr{M})}_i$
  2202	vanish for $i > 0$, the groupoid $\Steinb_b \rightrightarrows
  2203	\mathscr{L}$ is \'etale
exec
/bin/zsh -lc "rg -n \"Koszul\" /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 607

/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:850:Koszul locus} (Theorem CY-B(ii)): the bar complex (product side) and the
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:74:We recall the essential structures from Vol~I (Modular Koszul Duality)
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:81:For a modular Koszul chiral algebra $\mathcal{A}$, the universal
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:158:Koszul duality pairs $\mathcal{A}$ with $\mathcal{A}^!$. The sum
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:232:chiral algebra and its Koszul dual contribute, each with weight~5).
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:247:$G(S \times E)$ is modular Koszul with $\kappa_{\mathrm{BKM}} = 5$, then the genus tower
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:443:For a Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, the complementarity
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:456:For the quantum vertex chiral group $G(X)$ of a CY3 $X$, the Koszul
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:467:\item The Koszul dual $G(X)^!$ is a BKM superalgebra
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:507:determined by the Koszul duality of the underlying lattice VOA. Since
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:51: and Koszul Duality \\[8pt]
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:65:These notes spell out the physical picture behind $G(X)$ for a CY3 $X$. Four ingredients are developed: M-theory holography, open string field theory from CY categories, closed strings from cyclic homology, and their packaging via Koszul duality. Throughout, we connect to the CY-to-chiral functor $\Phi$ (Theorem CY-A), the bar-cobar machine of Volume~I, and the $E_1/E_2$ chiral hierarchy of Volume~III.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:169:\subsection{Holography as Koszul duality}
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:174:\begin{conjecture}[Holographic Koszul duality]
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:177:related by Koszul duality:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:181:where $\cB^!$ denotes the Koszul dual of $\cB$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:189:z_2][1])$. The Koszul dual of the latter is $\mathbf{U}(\Hom(\mathbb{C}^2)
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:191:is the former. Koszul duality thus interchanges:
exec
/bin/zsh -lc "rg -n \"collapse\" /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_sduality_langlands.tex:913:collapse to a single point (the self-dual level, the self-dual coupling, the
/Users/raeez/calabi-yau-quantum-groups/notes/theory_e2_chiral_formalism.tex:583:(Section~4) asks when these spectral sequences collapse at $E_1$
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:312:symmetric monoidal ($E_\infty$), reflecting the collapse of $E_2$
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1078:Without the $\Omega$-deformation, the CY3 functor chain for $\C^3$ collapses: the Lie conformal algebra is abelian (Theorem~\ref{wn:thm:c3-abelian-bracket}), the envelope produces the free Heisenberg, and the $\Etwo$ structure is trivially $\Einf$ (symmetric monoidal). Noncompactness forces the introduction of external data: $T^3$-equivariant structure plus $\bS^3$-framing. For compact CY3, neither should be needed: the nontrivial global geometry plays the role of the $\Omega$-deformation.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3356:derived category collapse (Positselski acyclicity), so the comparison
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3684:\subsection{The $\kappa_{\mathrm{ch}}$-collapse}
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3685:\label{subsec:kappa-collapse}
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3687:\begin{observation}[$\kappa_{\mathrm{ch}}$-collapse: rank $\to$ $\dim_\C$]
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3688:\label{obs:kappa-collapse}
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3689:The passage from the abelian $(2,0)$ pushforward to the K3 sigma model exhibits a \emph{non-perturbative collapse of the modular characteristic}:
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3821:In the M-theory picture, the abelian $(2,0)$ theory is the worldvolume theory of a single M5-brane. The pushforward along $K3$ gives the effective theory of the M5-brane wrapping $K3$: a $2$-dimensional theory on $E$ with content determined by the $K3$ zero modes (harmonic forms). The sigma model VOA arises only at the level of the \emph{string worldsheet} --- the non-perturbative type~IIA / heterotic duality relates the M5-brane picture to the string sigma model on $K3$. The $\kappa_{\mathrm{ch}}$-collapse from $\mathrm{rank}$ to $\dim_\C$ is the algebraic shadow of this duality: the M5-brane sees $\mathrm{rank}(H^2)$ zero modes, while the string worldsheet sees $\dim_\C(K3)$ as the effective target dimension.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3837: \item \textbf{Question 5} ($\kappa_{\mathrm{ch}} = h^{1,1}/4$ universality): the $\kappa_{\mathrm{ch}}$-collapse shows that the relevant quantity is $\dim_\C$, not $h^{1,1}$ or $\mathrm{rank}$. For $K3$: $\dim_\C = 2$, $h^{1,1}/4 = 5$, and neither equals $\mathrm{rank}/12 \approx 1.83$. The question should be reframed: what determines $\kappa_\BPS$ (the BKM weight) in terms of Hodge data, and how does the second-quantization factor $\kappa_\BPS / \kappa_{\mathrm{ch}}$ depend on the geometry?
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:613:  \item The $E_3$-chiral structure on $\C^3$ requires all three complex directions on equal footing. In the rational limit, the geometry degenerates to $\C^2 \times \R$ (the 5d holomorphic CS of row~2 in the table of \S\ref{subsec:en-theory-dimension}), which carries only $\Etwo$-chiral structure. The third direction collapses from $\C^*$ to $\R$, breaking the three-fold symmetry.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:699:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations applies:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:131:When $D^b(\Coh(X))$ admits a full exceptional collection, the category collapses to modules over a finite-dimensional quiver algebra. This is the tightest combinatorial description of $D^b(\Coh(X))$ and provides the simplest non-trivial inputs to the CY-to-chiral functor (restricted to \emph{local} CY geometries, since a compact variety with a full exceptional collection is Fano, hence NOT Calabi--Yau).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:354:  limit, the three parameters collapse to two ($\epsilon_1, \epsilon_2$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1454:As $\tau \to i\infty$, $\theta_1(z|\tau) \to 2\sin(\pi z)$ and the Eisenstein corrections collapse to constants; as $q \to 1$, the trigonometric propagator becomes $dz/z$ and $R_q(u) \to 1 - \hbar P/u$. The bar complex degenerates accordingly: $\B^{\mathrm{ell}}(\cA) \to \B^{\mathrm{trig}}(\cA) \to \B^{\mathrm{rat}}(\cA)$, consistent with the spectral sequence of Theorem~\ref{thm:elliptic-vs-rational}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2307:\begin{remark}[The $\kappa_{\mathrm{ch}}$-collapse: rank $\to$ $\dim_\bC$]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2308:\label{rem:kappa-collapse}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2309:\index{kappa-collapse@$\kappa_{\mathrm{ch}}$-collapse}
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex | sed -n '2295,2335p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2295	 \item No poles of order $\geq 3$ appear: the $6$-dimensional
  2296	 theory is free with at most quadratic action.
  2297	\end{enumerate}
  2298	In particular, $\cA_{\mathrm{free}}$ is a lattice vertex algebra
  2299	$V_\Lambda$ with $\Lambda$ determined by the fiber cohomology
  2300	surviving the closure constraint. By the Vol~I lattice curvature
  2301	theorem, $\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for any
  2302	lattice VA, shadow class~$\mathbf{G}$
  2303	\textup{(}Gaussian, $r_{\max} = 2$\textup{)}, and the shadow
  2304	obstruction tower terminates:
  2305	$\Theta_{\cA_{\mathrm{free}}} = \kappa_{\mathrm{ch}} \cdot \omega_g$ at all genera \end{proposition}
  2306	
  2307	\begin{remark}[The $\kappa_{\mathrm{ch}}$-collapse: rank $\to$ $\dim_\bC$]
  2308	\label{rem:kappa-collapse}
  2309	\index{kappa-collapse@$\kappa_{\mathrm{ch}}$-collapse}
  2310	The passage from the abelian $(2,0)$ pushforward to the K3 sigma
  2311	model exhibits a non-perturbative collapse of the modular
  2312	characteristic:
  2313	\[
  2314	 \kappa_{\mathrm{ch}}(\cA_{\mathrm{free}}) \;=\; \mathrm{rank}(\Lambda)
Plan update
  ✓ Survey repository for bar_cobar_adjunction_inversion.tex to locate Theorem B and context
  ✓ Identify definition of the Koszul locus and theorems for strict quasi-isomorphism on locus
  ✓ Find unconditional coderived statements off-locus and remarks characterizing obstruction/collapse loci across volumes
exec
/bin/zsh -lc "rg -n \"label\\{thm:spectral-sequence-collapse\\}\" -n chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2269:\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}\" -n chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

wait(call_4gSrM8W8zxOc6bzVZK8O8Kh0) timed out:
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
audit_campaign_20260412_231034/T08_MC1_PBW.md:975:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/S05_foundations_to_complementarity.md:984:  4130	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
healing_20260413_130533/H02_thm_B_alt_proof.md:444:chapters/theory/higher_genus_complementarity.tex:4316:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
healing_20260413_130533/H02_thm_B_alt_proof.md:458:wave2_audit_20260413_001942/U09_missing_examples.md:255:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
healing_20260413_130533/H02_thm_B_alt_proof.md:517:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/F09_prerequisites_thm_H.md:328:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/F09_prerequisites_thm_H.md:343:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:772:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/S20_readme_to_manuscript.md:887:  4130	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
platonic_rectification_20260413_114523/P03_thm_C0_curved_upgrade.md:1585:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
platonic_rectification_20260413_114523/P17_concordance_sync.md:3992:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/U09_missing_examples.md:255:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
relaunch_20260413_111534/R19_coderived_models.md:579:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
relaunch_20260413_111534/R19_coderived_models.md:1569:/bin/zsh -lc "rg -n -F -e '\\label{thm:higher-genus-inversion}' -e '\\label{def:coacyclic-fact}' -e '\\label{def:coderived-contraderived-abstract}' -e '\\label{def:coderived-fact}' -e '\\label{prop:coderived-adequacy}' chapters/theory/coderived_models.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
relaunch_20260413_111534/R19_coderived_models.md:1574:chapters/theory/higher_genus_complementarity.tex:4355:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T02_thm_B.md:406:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T02_thm_B.md:425:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:999:/bin/zsh -lc "grep -nF '\\label{thm:higher-genus-inversion}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
rectification_20260412_233715/R19_coderived_models.md:222:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1048:audit_campaign_20260412_231034/T08_MC1_PBW.md:975:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}

thinking
**Considering polling options**

I think I might need to conduct a poll later on. It feels like gathering opinions could be helpful. However, for now, it seems more efficient to use an update plan instead. I want to stay organized and on top of things. I hope that approach will streamline my efforts without overwhelming anyone. Let’s see how that goes! I'll keep the user's needs in mind while working through this.
codex
Context is clear enough to lock scope. I’m treating this as a local fortification of Theorem B’s theorem-band: verify the existing research remark against the live definitions and off-locus theorems, then tighten it so it answers the four questions explicitly and does not outclaim the proved promotion lane.
Plan update
Scope locked to the Theorem B surface in chapters/theory/bar_cobar_adjunction_inversion.tex, with live dependencies in algebraic_foundations.tex and the coderived comparison lane.
  ✓ Read constitutional files, target file, and direct dependencies for Theorem B and the Koszul-locus definitions.
  → Verify the existing Research Remark against the live theorem surface and identify any under-specified or over-strong claims.
  • Edit the Research Remark to characterize the Koszul locus, derived wall, off-locus obstruction, and honest upgrade lanes.
  • Run targeted verification: re-read the edited band, grep for local consistency issues, and summarize proof-strength/confidence for Theorem B.

thinking
**Inspecting the theorem**

I need to look into the off-Koszul theorem and coderived spectral sequence to ensure everything is accurate. Right now, I have a remark, but I want to check if there's any existing statement about the "derived Koszul locus" in conjectures, just in case my remark is already sufficient. The user wants to add a research remark, so I think it might be good to see if it's already been included by others. I'll check the off-Koszul theorem and find the right proposition to quote.
exec
/bin/zsh -lc "sed -n '1440,1535p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{theorem}[Positselski equivalence for the chiral bar coalgebra;
\ClaimStatusProvedHere]
\label{thm:positselski-chiral-proved}
\index{Positselski!chiral equivalence|textbf}
\index{comodule-contramodule correspondence!chiral Koszul|textbf}
For a Koszul chiral algebra $\cA$ on a smooth curve $X$ with
curved bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$
(a conilpotent chiral CDG-coalgebra by
Example~\textup{\ref{ex:bar-as-CDG}}), there is an equivalence of
triangulated categories:
\begin{equation}\label{eq:positselski-chiral-proved}
D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{conil,\,ch}})
\;\simeq\;
D^{\mathrm{ctr}}(C\text{-}\mathrm{contra}^{\mathrm{ch}})
\end{equation}
between the coderived category of conilpotent chiral
CDG-comodules over the bar coalgebra~$C$ and the contraderived
category of chiral CDG-contramodules over the same
CDG-coalgebra~$C$.
exec
/bin/zsh -lc "sed -n '1020,1105p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1360,1445p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
&\subset \mathrm{Hot}(C\text{-}\mathrm{contra}^{\mathrm{ch}}), \\
\mathrm{Hot}(C\text{-}\mathrm{comod}^{\mathrm{ch}}_{\mathrm{inj}})
&\subset \mathrm{Hot}(C\text{-}\mathrm{comod}^{\mathrm{ch}})
\end{align*}
are mutually inverse equivalences.

To see this, observe that the unit and counit natural transformations
\[
\eta\colon \mathrm{id} \to \Psi_C^{\mathrm{ch}} \circ \Phi_C^{\mathrm{ch}},
\qquad
\varepsilon\colon \Phi_C^{\mathrm{ch}} \circ \Psi_C^{\mathrm{ch}} \to \mathrm{id}
\]
are isomorphisms on free contramodules and cofree comodules
(Step~2). Since these objects generate the respective
homotopy categories (every object is built from generators by
shifts, cones, and countable (co)products),
and both $\Phi_C^{\mathrm{ch}}$ and $\Psi_C^{\mathrm{ch}}$ preserve
exact triangles and countable (co)products, the natural
transformations $\eta$ and $\varepsilon$ are isomorphisms
on all objects with projective (resp.\ injective) underlying graded
 succeeded in 50ms:
by localizing at acyclic objects (those with $H^*(M) = 0$). In general,
$\mathrm{Acycl}^{\mathrm{co}} \supset \mathrm{Acycl}$,
so $D^{\mathrm{co}}$ is a quotient of $D$. When $C$ has
finite homological dimension (e.g., when $\cA$ is Koszul with finite
global dimension), the two categories coincide
(Positselski~\cite[\S4.5]{Positselski11}). When $h \neq 0$, the standard
cohomological derived category is no longer the right invariant
for the curved theory; on the higher-genus bar-complex surfaces
treated here the underlying complexes are acyclic, while
$D^{\mathrm{co}}$ is nontrivial.
\end{remark}

\subsection{Injective comodules and projective contramodules}
\label{subsec:chiral-inj-proj}

\begin{definition}[Cofree chiral CDG-comodule]
\label{def:cofree-chiral-comod}
\index{cofree comodule!chiral}
For a graded $\mathcal{D}_X$-module $V$, the \emph{cofree graded
chiral $C$-comodule} on $V$ is:
codex
- **Definition** Koszul locus — “Kosz(X)” is the full subcategory of augmented chiral algebras whose genus‑0 bar‑cobar counit is a quasi‑isomorphism; see `chapters/theory/algebraic_foundations.tex:236` (Definition \ref{def:koszul-locus}).

- **Strict inversion theorems** Theorem B (`thm:bar-cobar-inversion-qi`, `chapters/theory/bar_cobar_adjunction_inversion.tex:1606`) states that on the Koszul locus the genus‑0 and higher‑genus counits are quasi‑isomorphisms, relying on the square‑zero spectral sequence (`thm:bar-cobar-spectral-sequence`, `:2209`), its collapse at \(E_2\) (`thm:spectral-sequence-collapse`, `:2269`), and the higher‑genus inversion package (`thm:higher-genus-inversion`, `chapters/theory/higher_genus_complementarity.tex:4424`).

- **Coderived lane** Clause (2) of `thm:bar-cobar-inversion-qi` upgrades the counit to a coacyclic equivalence for every complete augmented algebra with finite graded bar pieces, while the bar‑degree filtration proposition (`prop:coderived-bar-degree-spectral-sequence`, `chapters/theory/coderived_models.tex:314`) and the Ran‑version theorem (`thm:off-koszul-ran-inversion`, `chapters/theory/coderived_models.tex:917`) guarantee the unconditional coderived statement off the locus.

- **Off-locus remarks** Vol I’s `rem:koszul-locus-off-locus-obstruction` (`chapters/theory/bar_cobar_adjunction_inversion.tex:1931`) narrates the first non‑Koszul bar class as the obstruction, the collapse hypothesis needed for promotion, and the derived wall conjecture; Vol II’s `rem:steinberg-perturbative` (`chapters/connections/bar-cobar-review.tex:2196`) interprets failure as excess intersection/unanished higher Tor class; Vol III’s `rem:kappa-collapse` (`chapters/examples/toroidal_elliptic.tex:2307`) records the non‑perturbative collapse of the modular characteristic as the geometry leaves the Koszul locus.


thinking
**Considering higher-genus modular loci**

I might need to mention the higher-genus modular locus, separate from the genus-0 Koszul locus. There’s a point about off-locus obstruction being the first non-zero higher bar cohomology past degree 1. It could serve as an alternative proof path. Also, I should consider describing it through transferred A∞ operations and Ext algebra. This could provide two equivalent descriptions of obstruction, linking it to higher multiplications. Additionally, I could touch on upgrades for specific non-Koszul families, like the flat case where kappa equals zero.
thinking
**Clarifying spectral sequences and candidates**

I need to mention that the statement includes flat cases and any family where the coderived bar-degree spectral sequence degenerates to ordinary cohomology. To add specificity, I could propose a concrete candidate, like admissible \(L_{-1/2}(sl_2)\), especially if the related remark about its 2-Koszulness is proven. I might also point out non-Koszul families that are derived-positive, where the \(E_N\) collapse still yields qi, even when it's not proven via \(E_2\).
exec
/bin/zsh -lc "sed -n '4032,4075p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\varepsilon\colon\cA\to\omega_X$, the associated simplicial bar object
$\operatorname{Bar}_\bullet(\omega_X,\cA,\omega_X)$ is the
\v{C}ech nerve of~$\varepsilon$, and its geometric realization is the
bar coalgebra~$\barB_X(\cA)$~\cite[Chapter~5, especially
\S\S5.2.2--5.2.4]{HA}. Dually, a coaugmented conilpotent
coalgebra~$\cC$ has a cosimplicial cobar object obtained from the dual
\v{C}ech nerve, and its totalization is~$\Omega_X(\cC)$ by the same
bar\slash cobar formalism~\cite[Chapter~5, especially
\S\S5.2.3--5.2.4]{HA}. The general realization\slash totalization
adjunction therefore produces the functor pair
\[
\barB_X \colon
\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
\rightleftarrows
\operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
\,:\!\Omega_X.
\]
In this $\infty$-categorical formulation, the Koszul locus of the
chapter is the locus where these \v{C}ech and co-\v{C}ech resolutions
are effective, so the unit and counit are equivalences there. This





thinking
**Evaluating research remarks**

I’m thinking about whether I could use this as alternative proof, but the user is focusing on research. I might not need additional edits here. Since my goal is to fortify, perhaps I should still add another research remark. It’s important to ensure the existing one aligns well with the user’s instructions. Comparing the current remark might help identify any necessary refinements. So, I’ll take a closer look at the details and how they fit together.
thinking
**Analyzing remarks on derived Koszul locus**

I've reviewed the existing remark about the natural enlargement not capturing the whole moduli, but focusing on the derived Koszul locus. It mentions some intriguing conjectures and proves regarding codderived cones and their conditions. I think I need to explore if I can talk about upgrading qi for specific non-Koszul families, but I need to be cautious since it's generally about collapse loci. The mention of specific non-Koszul families like class G/L could provide clarity, especially since class G includes elements that might be more complex.
thinking
**Exploring off-Koszul families**

I'm thinking about off-Koszul families with κ=0. The critical-level affine might have κ=0, but is it completely augmented? It seems there are complexities since the bar complex picks up infinitely many off-diagonal classes. However, according to clause (4), if κ=0, there’s a potential upgrade to chain-level qi through coderived equivalence. I need to be cautious here and confirm if critical-level affine truly qualifies as a non-Koszul family where qi can be upgraded, as Theorem B states.
thinking
**Evaluating VOA properties**

I'm considering the Feigin-Frenkel center and its implications on the universal affine VOA. It seems like it's not C_2-cofinite and also not finitely strongly generated because the center is polynomial with infinitely many generators. For simple g, the center is generated by fields related to exponents and derivatives. However, for sl2, the center is generated by one field and its derivatives, which means it is indeed finitely strongly generated. So, I think strong generation is confirmed!
thinking
**Considering cross-volume remarks**

I think I need to check for other comments in Volume II that might characterize off-locus. The user is asking if any changes across volumes could affect them, but since the target file is the main concern, cross-volume checks might not be necessary unless there are duplicates. I wonder if I should use a grep search for exact remark text in other volumes. The rules state that shared content like formulas and definitions include all three volumes, but maybe we can limit it to just local remarks. I'll wait to see if the explorer provides any line references.
collab wait(call_ZcZ7CY0U38U0uqop80zROBdI)
  receivers: 019d86aa-8e8a-7d13-b2c7-d81be34ba93f
wait(call_ZcZ7CY0U38U0uqop80zROBdI) 1 agents complete:
  019d86aa-8e8a-7d13-b2c7-d81be34ba93f completed: "- **Definition** Koszul locus — “Kosz(X)” is the full subcategory of augmented chiral algebras whose genus‑0 bar‑cobar c…"





thinking
**Considering research remarks**

I need to check the bar-cobar-review vol II remarks to see if my terms are aligned, but it might not be necessary. I should look at the target research remark at line 1930 since it might already be okay. I want to identify any under-specified claims or those that are too strong. I have ideas for improvements, like separating the "higher-genus modular locus" in relation to Theorem B and clarifying the derived Koszul locus. I might also consider alternative descriptions of obstructions through higher multiplications.
thinking
**Refining research remarks**

I’m thinking about enhancing my research remarks to link with an alternative proof. It could clarify that obstructions can be understood through the first off-diagonal bar class or the first nonzero transferred higher multiplication on \(A^i\). That sounds nice! 

I also want to add a more precise classification of families, like universal and freely strongly generated ones, and mention simple admissible affine quotients and minimal models. The current remarks could clarify that all standard VOAs in the manuscript are connected through PBW-flat models while ensuring not to overreach any unverified claims.
thinking
**Clarifying terminology**

I'm refining my terminology to be more precise. I think I should avoid using "pathological" unless it has been introduced previously. Instead, I can stick with "singular quotient boundary," as the current text does. 

Also, there's a mention of "Quadratic A_infty models," which have their bar cohomology concentrated in degree 1. I realize I need to make this explicit because the user has requested exactly that detail. So, it’s important to ensure clarity and accuracy in my description.
thinking
**Mentioning critical-level adjustments**

I need to pay attention to how critical-level κ=0 is being interpreted, as it's essential not to misread it as genus0 qi. That’s a good point! I think I should add this clarification. I could also mention that the user is inquiring about the derived Koszul locus off locus, which seems relevant to our current discussion. It looks like there’s some important context here that can help clear up any confusion.
thinking
**Refining research remark**

The user asked me to write a research remark, but since there’s already one, it feels like the simplest approach is to refine it. I think I should replace it with a clearer 4-part structure. I need to inspect the total lines to see how it’s organized and maybe update the commentary with the planned edits. It seems like a good way to improve clarity!
codex
I found one real fortification target: the current remark is directionally right, but it leaves two things too implicit. I’m rewriting it so it answers the four research questions in order and explicitly separates the genus‑0 Koszul hypothesis from the higher‑genus coderived promotion lane, which is the point most likely to be misread.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1934,58 +1934,82 @@
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Verifying token bans**

I need to read through the block and use a grep tool to find any banned tokens—could be a bit messy with AI slop. Maybe I'll also check if there's a line wrap issue using sed. It might be useful to run a search for "derived wall" as well, just to be thorough. Additionally, I should look for em dashes and inspect remark lines for any suspicious words. Let's keep this process organized!
codex
The edit is in. I’m re-reading the theorem band and running a narrow hygiene pass now: local theorem-surface consistency, no status drift, and no accidental overclaim in the new promotion language.
exec
/bin/zsh -lc "sed -n '1928,2015p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -i "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "rem:koszul-locus-off-locus-obstruction|def:koszul-locus|rem:equivalent-formulations-koszul|conj:koszul-wall-associated-variety|rem:admissible-2-koszul|thm:bar-cobar-inversion-qi" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/algebraic_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
\label{rem:koszul-locus-off-locus-obstruction}
\index{Koszul locus!off-locus obstruction}
\index{bar-cobar inversion!off-locus obstruction}
The phrase ``Koszul locus'' in
Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
kept separate: the genus-$0$ Koszul condition of
Definition~\ref{def:koszul-locus}, and the higher-genus coderived
continuation of the same bar-cobar comparison. The research picture is
therefore:
\begin{enumerate}[label=\textup{(\arabic*)}]
\item \emph{Precise genus-$0$ locus.}
 The Koszul locus is the full subcategory
 $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
 counit
 \[
 \Omega_X(\barB_X(\cA)) \longrightarrow \cA
 \]
 succeeded in 52ms:
3659:object on $\operatorname{Ran}(X)$. We now show that this
4503:We now consider what happens when
6042:We now connect the abstract divisor-core theory to bar
 succeeded in 50ms:
chapters/theory/algebraic_foundations.tex:59:(Definition~\ref{def:koszul-locus}). The central algebraic
chapters/theory/algebraic_foundations.tex:236:\begin{definition}[Koszul locus]\label{def:koszul-locus}
chapters/theory/algebraic_foundations.tex:274:\label{rem:equivalent-formulations-koszul}
chapters/theory/algebraic_foundations.tex:625:(Definition~\ref{def:koszul-locus}), the bar spectral sequence
chapters/theory/algebraic_foundations.tex:1552:(Definition~\ref{def:koszul-locus}).
chapters/theory/bar_cobar_adjunction_inversion.tex:21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
chapters/theory/bar_cobar_adjunction_inversion.tex:23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
chapters/theory/bar_cobar_adjunction_inversion.tex:138:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
chapters/theory/bar_cobar_adjunction_inversion.tex:690:(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
chapters/theory/bar_cobar_adjunction_inversion.tex:1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
chapters/theory/bar_cobar_adjunction_inversion.tex:1713:Theorem~\ref{thm:bar-cobar-inversion-qi}; the concrete mechanism by
chapters/theory/bar_cobar_adjunction_inversion.tex:1761:Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
chapters/theory/bar_cobar_adjunction_inversion.tex:1776:\label{rem:admissible-2-koszul}%
chapters/theory/bar_cobar_adjunction_inversion.tex:1861:Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
chapters/theory/bar_cobar_adjunction_inversion.tex:1931:\label{rem:koszul-locus-off-locus-obstruction}
chapters/theory/bar_cobar_adjunction_inversion.tex:1935:Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
chapters/theory/bar_cobar_adjunction_inversion.tex:1937:Definition~\ref{def:koszul-locus}, and the higher-genus coderived
chapters/theory/bar_cobar_adjunction_inversion.tex:1949: \textup{(}Definition~\ref{def:koszul-locus},
chapters/theory/bar_cobar_adjunction_inversion.tex:1950: Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1977: Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Considering timing and updates**

I'm thinking it may take about 2 minutes for the large monograph, which could mean several minutes of processing. That's alright, but I should aim to provide updates every 30 seconds if it takes longer. I can try this approach, but the sandbox might generate many tokens. Maybe I could set `yield_time_ms` to 1000 and check back if it's still running. I should also note this in the commentary before starting the build.
codex
The text re-read is clean and the local references resolve. I’m doing one stronger verification pass now by asking TeX to parse the live tree; if the full monograph build is too heavy, I’ll report that rather than pretend the edit was compile-checked.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

 exited 12 in 2.17s:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  main.aux
  main.ind

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2

thinking
**Monitoring build progress**

The build is still running, and I realize it could take a while. I think it might be a good idea to implement a polling mechanism to check on its status. I’m considering setting the polling interval to about 30 seconds to balance between waiting too long and being too frequent. It feels important to stay updated without overwhelming the system. Let’s see how this approach works out!
codex
The full tree is parsing, so I’m letting it run long enough to catch a real TeX failure instead of stopping at the first screen of package loads. If it dies elsewhere in the manuscript, I’ll separate that from the local edit.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Investigating build failure**

It looks like the build failed due to a preexisting issue, possibly a missing \begin{document} near line 11073 of an auxiliary file. I need to check if this relates to our current edits. I think I'll inspect the main.log around that error and see if line 11073 in the generated .aux file is corrupt from a previous build, but it's likely not caused by our edits. I'll grep the context to clarify what's happening.
codex
The TeX pass reached the existing global build surface and then died in a preexisting manuscript error, not at the new remark. I’m checking the exact failing location once so I can tell you whether this edit is clean but the tree is already broken, or whether the failure routes through my touched file.
exec
/bin/zsh -lc "rg -n \"Missing \\\\begin\\{document\\}|l\\.11073|bar_cobar_adjunction_inversion|rem:koszul-locus-off-locus-obstruction\" main.log" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '11040,11085p' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^eorem'"\\}\\}\\{2694\\}|eorem\\}\\}\\{2694\\}|Missing \\\\begin\\{document\\}\" main.aux chapters -g '*.aux'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 exited 1 in 50ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Inspecting output issues**

It looks like there might be an issue because I’m not getting any output, which makes me think the maximum output limit could be causing a problem. I should check the commands to see if they are working properly. It might be helpful to use `tail -n 50 main.log` to inspect what’s happening in the logs. That could give me more clarity on why I’m not seeing any matches!
exec
/bin/zsh -lc 'tail -n 80 main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

LaTeX Warning: Reference `ch:holographic-datum-master' on page 401 undefined on
 input line 2065.



[401]

LaTeX Warning: Reference `ex:fermion-betagamma-bar-cobar' on page 402 undefined
 on input line 2108.


LaTeX Warning: Reference `thm:fermion-boson-koszul' on page 402 undefined on in
put line 2108.


LaTeX Warning: Citation `LV12' on page 402 undefined on input line 2115.


LaTeX Warning: Citation `LV12' on page 402 undefined on input line 2128.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Troubleshooting log errors**

I suspect the tail command isn't displaying errors because the log file is over 80 lines long. There might be too much data to process effectively. I think I should use `grep -n "Missing \\\\begin{document}" main.log` to pinpoint where the missing document error is within the log. This could help me find the exact location and understand why it’s not showing up properly. Let’s see if that helps!
exec
/bin/zsh -lc "grep -n \"Missing \\\\begin{document}\" main.log" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

exec
/bin/zsh -lc 'grep -n "LaTeX Error: Missing" main.log' in /Users/raeez/chiral-bar-cobar exited 1 in 54ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Investigating log issues**

I’m wondering if the log wasn’t saved due to a build failure, but the tail is still available. It might be that an error was captured in stdout, but the log didn’t flush properly. I guess I should check the size of main.log to see if it’s from a previous session. Maybe I'll use wc and grep to search for any odd lines. There seems to be quite a bit to unravel here!
exec
/bin/zsh -lc "wc -l main.log && rg -n \"Fatal error|Missing|multiply defined|eorem\\}\\}\\{2694\\}\" main.log" in /Users/raeez/chiral-bar-cobar succeeded in 162ms:
   13234 main.log
13233:./chapters/theory/bar_cobar_adjunction_inversion.tex:1890:  ==> Fatal error occ
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Inspecting fatal error**

I see there's a fatal error logged at line 1890 in the file, and I need to check what's happening around that line. I wonder if it's related to our new remark or something else entirely. Just to be thorough, I should look at the lines between 1880 and 1895. Let’s see what’s going on in that section of the file to figure out the issue!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1882,1896p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1882	bar-cobar deformation problem. In Keller's deformation-theoretic
  1883	language, this identifies the formal moduli problem of
  1884	$\Omega(\barB(\cA))$ with the one controlled by the transferred
  1885	$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
  1886	concentration says that this tangent complex is already governed by the
  1887	quadratic closure.
  1888	
  1889	The remaining step is formality of the transferred
  1890	$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
  1891	Kontsevich-type configuration-space integrals on
  1892	Fulton--MacPherson models
  1893	\textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
  1894	and the fiberwise identification of transferred higher operations with
  1895	the corresponding FM-stratum operations
  1896	\textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
exec
/bin/zsh -lc "sed -n '13220,13236p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
misspelled it (e.g., `\hobx'), type `I' and the correct
spelling (e.g., `I\hbox'). Otherwise just continue,
and I'll forget about whatever was undefined.

 
Here is how much of TeX's memory you used:
 48942 strings out of 473190
 947179 string characters out of 5715801
 1162885 words of memory out of 5000000
 65495 multiletter control sequences out of 15000+600000
 1109044 words of font info for 793 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 116i,21n,121p,1797b,2563s stack positions out of 10000i,1000n,20000p,200000b,200000s
./chapters/theory/bar_cobar_adjunction_inversion.tex:1890:  ==> Fatal error occ
urred, no output PDF file produced!
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Searching for log details**

I need to look back at the earlier log lines to identify any undefined control sequences, potentially around \E_2. It seems the clues might be hidden near line 13200 or even earlier. I'll search through the logs to gather more context and see if I can pinpoint where the issues might be stemming from. I know digging into these lines could lead me to the answers I need!
exec
/bin/zsh -lc "sed -n '13190,13225p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


[515]

LaTeX Warning: Reference `thm:conilpotent-reduction' on page 516 undefined on i
nput line 1846.


LaTeX Warning: Reference `thm:bar-cobar-inversion-qi' on page 516 undefined on 
input line 1861.


LaTeX Warning: Reference `thm:bar-cobar-spectral-sequence' on page 516 undefine
d on input line 1862.


LaTeX Warning: Reference `thm:spectral-sequence-collapse' on page 516 undefined
 on input line 1863.


file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Assessing build issues**

I see that our edit didn't cause the build failure; it was already broken due to a preexisting issue in the same file. However, since the user wants to heal the remaining wounds, fixing this seems low-risk and might just involve correcting a typo. They likely meant \(E_2\) or \(\En\), which I can repair since it’s in a touched file. I need to check if \E_2 is used elsewhere and confirm the correct macro conventions.
codex
The full build failure turned out not to come from the new remark at all. It exposed a preexisting typo two paragraphs earlier in the same theorem band: `\E_2` is undefined at [chapters/theory/bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1890). I’m fixing that now and then rerunning the local verification.
exec
/bin/zsh -lc "rg -n \"\\\\E_2|\\\\mathbb\\{E\\}_2|\\\\mathrm\\{E\\}_2|E_2-formality|\\\\En-formality\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory chapters/connections /Users/raeez/chiral-bar-cobar-vol2 | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:\E_2|\mathbb\{E\}_2|\mathrm\{E\}_2|E_2-formality|\En-formality)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"\\\\newcommand\\\\E|\\\\def\\\\E|\\\\DeclareMathOperator\\{\\\\E|\\\\newcommand\\{\\\\En\\}|\\\\newcommand\\{\\\\Eone\\}\" preamble.tex main.tex macros.tex styles -g '*.tex' -g '*.sty'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\newcommand\E|\def\E|\DeclareMathOperator\{\E|\newcommand\{\En\}|\newcommand\{\Eone\})
                  ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

exec
/bin/zsh -lc "rg -n -F '\\E_2' chapters/theory bar_cobar_adjunction_inversion.tex /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbb{E}_2' chapters/theory chapters/connections /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: bar_cobar_adjunction_inversion.tex: No such file or directory (os error 2)
chapters/theory/bar_cobar_adjunction_inversion.tex:1890:$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:25614:\mathbb{E}_1 \oplus \mathbb{E}_2$,
chapters/theory/poincare_duality_quantum.tex:319:These are \emph{dual} constructions: factorization homology computes the derived tensor product (the \emph{homological} side), while the derived Hom (the \emph{cohomological} side) is computed via the bar complex. They are related by $\mathbb{E}_2$-Koszul duality as developed by Francis \cite{Francis2013}, building on Lurie's operadic bar-cobar framework~\cite[§5.2]{HA}.
chapters/theory/poincare_duality_quantum.tex:323:By Francis \cite{Francis2013}, both constructions are derived functors of the forgetful functor from $\mathcal{A}$-modules to chain complexes, evaluated on the trivial module $k$. The factorization homology $\int_X \mathcal{A} \simeq \mathcal{A} \otimes^{\mathbb{L}}_{\mathrm{Disk}(X)} \mathrm{pt}$ is the derived tensor product (left adjoint, homological), while the bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{A}) \simeq \mathrm{RHom}_{\mathcal{A}\text{-mod}}(k, k)$ is the derived Hom (right adjoint, cohomological). These are related by $\mathbb{E}_2$-Koszul duality: the $\mathbb{E}_2$-operad is Koszul self-dual up to shift \cite[Theorem~5.2]{Francis2013}, which induces the duality between the two functors.
exec
/bin/zsh -lc "rg -n -F '\\En' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\Eone' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 977

./healing_20260413_132214/H02_thm_B_alt_proof.md:660:   985	\begin{proposition}[\texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2};
./healing_20260413_132214/H02_thm_B_alt_proof.md:663:   988	\index{formality!$\En$ operad}
./healing_20260413_132214/H02_thm_B_alt_proof.md:1130:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1221:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1316:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1469:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1581:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1681:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1779:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1875:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:1972:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2067:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2162:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2257:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2352:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2447:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2542:-$\En$-formality package
./healing_20260413_132214/H02_thm_B_alt_proof.md:2637:-$\En$-formality package
 succeeded in 52ms:
Total output lines: 3660

./healing_20260413_132214/H12_complementarity_alt.md:496:chapters/examples/toroidal_elliptic.tex:266:\item \emph{RTT presentation.} By $\Eone$-chiral Koszul duality (Theorem~\ref{thm:e1-chiral-koszul-duality}), the dual has $R$-matrix $R(u;q,t)^{-1} = R(u;q^{-1},t^{-1})$ (Ding--Iohara inversion; cf.\ Theorem~\ref{thm:yangian-koszul-dual}).
./healing_20260413_132214/H07_MC5_alt_approach.md:397:\begin{principle}[The bar complex is $\Eone$-chiral coassociative;
./healing_20260413_132214/H07_MC5_alt_approach.md:404:is an $\Eone$-chiral coassociative coalgebra: a coalgebra
./healing_20260413_132214/H07_MC5_alt_approach.md:726:$\Eone$-chiral coalgebra engine, while the derived center
./healing_20260413_132214/H07_MC5_alt_approach.md:1115:$\Eone$-chiral coalgebra engine, while the derived center
./healing_20260413_132214/H07_MC5_alt_approach.md:1311:  2037	$\Eone$-chiral coalgebra engine, while the derived center
./healing_20260413_132214/H02_thm_B_alt_proof.md:578:manuscript is the separate $\Eone$ complete/conilpotent theorem
./healing_20260413_132214/H01_thm_A_alt_proof.md:386:chapters/examples/yangians_foundations.tex:364:In the RTT presentation, the Yangian $Y(\mathfrak{g})^{\mathrm{ch}}$ carries the structure of a quadratic $\Eone$-chiral algebra (Definition~\ref{def:e1-chiral}; cf.\ \cite[§4.1]{HA}). The $\Eone$-locality axiom is $R$-twisted commutativity:
./appendices/homotopy_transfer.tex:457:Let $\cA$ be an $\Eone$-chiral algebra on a curve $X$ and suppose we have an 
./appendices/homotopy_transfer.tex:472:We apply the general homotopy transfer theorem (Theorem~\ref{thm:htt}) to the $\Eone$-chiral operad.
./appendices/homotopy_transfer.tex:480:\emph{Step~4} ($\Ainf$-relations). The transferred operations $\{\tilde{m}_n^{\mathrm{ch}}\}$ satisfy the $\Ainf$-relations by the same algebraic argument as in the general theorem: the identity $\sum_{r+s+t=n}(-1)^{rs+t}\tilde{m}_{r+1+t}(\mathrm{id}^{\otimes r} \otimes \tilde{m}_s \otimes \mathrm{id}^{\otimes t}) = 0$ follows from substituting the tree formulas and using the $\Eone$-relations on $\cA$ together with the SDR identities $p\iota = \mathrm{id}$, $\mathrm{id} - \iota p = dh + hd$, $h^2 = 0$.
./appendices/homotopy_transfer.tex:563:Applying Theorem~\ref{thm:htt} to the strict $\Eone$-chiral algebra
./appendices/dual_methodology.tex:30:\Bbar: \Eone\text{-}\Alg \rightleftarrows \Eone\text{-}\CoAlg : \Cobar
./appendices/dual_methodology.tex:49:For an $\Eone$-chiral algebra $\cA$, the counit:
./appendices/dual_methodology.tex:193:For any augmented $\Eone$-chiral algebra $\cA$, the counit of the bar-cobar
./appendices/dual_methodology.tex:198:is an equivalence in the $\infty$-category of $\Eone$-chiral algebras. This
./appendices/signs_and_shifts.tex:471:determinant lines. For an $\Eone$-chiral algebra $\cA$:
./appendices/koszul_reference.tex:89:\S\ref{app:koszul_higher_genus}, proved by applying the $\Eone$-chiral Koszul
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Exploring macro and formality**

I'm noticing that while the \En macro exists, the \E_2 one doesn't seem to. It makes me think we likely want to look into `$\En$-formality`. The context mentions "The \E_2-formality map realized by Kontsevich-type configuration-space integrals," which could be pointing toward the Proposition prop:en-formality. It seems like it might be discussing a generic \En formality for n >= 2. I should search for the exact title of that proposition to clarify.
exec
/bin/zsh -lc "rg -n \"label\\{prop:en-formality\\}|En formality|formality for n >= 2|formality for \\\\En\" chapters/theory appendices" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{prop:en-formality\}|En formality|formality for n >= 2|formality for \En)
                                                                                  ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

exec
/bin/zsh -lc "rg -n -F '\\label{prop:en-formality}' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:987:\label{prop:en-formality}
exec
/bin/zsh -lc "rg -n -F '\\En-formality' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'En formality' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..b62e28c97e23f54470dba374f906a91d2dc7be7e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

exec
/bin/zsh -lc "sed -n '980,1015p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The explicit Kontsevich star product arises from propagator integrals
on $\overline{\Conf}_k(\mathcal{H})$, a specific $\Etwo$ bar complex
model with boundary conditions.
\end{remark}

\begin{proposition}[\texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2};
\ClaimStatusProvedElsewhere]
\label{prop:en-formality}
\index{formality!$\En$ operad}
\textup{(}Fresse--Willwacher~\cite{FresseWillwacher20}, Idrissi~\cite{Idrissi22}\textup{)}\quad
The $\En$ operad is formal over $\bR$ for all $n \geq 2$.
The formality map is constructed explicitly via configuration
space integrals on $\overline{\Conf}_k(\bR^n)$ using the propagator
of Definition~\textup{\ref{def:en-propagator}}, with the Kontsevich
graph expansion providing the explicit formulas.
\end{proposition}


%================================================================
% SECTION: THE KONTSEVICH GRAPH COMPLEX AND SHADOW TOWER
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Considering formal properties**

I'm trying to decide whether to use `$\En$` or `$\Etwo$`. The proposition concerns \En formal for n>=2, but it seems the alternative proof might require an E2-formality map. Maybe that’s because the chiral on the curve is specifically for n=2? I should search for phrases that relate to this. There’s definitely something interesting about how these different notations interact, and it’s crucial to get it right for clarity!
exec
/bin/zsh -lc "rg -n -F 'formality map realized by' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1890:$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Investigating build error**

I noticed the output mentions \Etwo already, which is interesting. I'm wondering if this happened after a build failure or if something changed. It says there's a `$\Etwo$-formality map` in line 1890, suggesting our current file is \Etwo, but earlier it showed \E_2. Perhaps there's been a change in the current file. Wait, could the build error still stem from an old file? I should check around that line.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1888,1892p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1888	
  1889	The remaining step is formality of the transferred
  1890	$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
  1891	Kontsevich-type configuration-space integrals on
  1892	Fulton--MacPherson models
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Verifying changes carefully**

I think I have to consider whether this is a user edit or an auto-generated tool change. The developer indicated that if unexpected changes occur, it’s likely user-generated or auto-generated. If there's a direct conflict, I should definitely ask the user for clarification. Here, I've fixed an error. I need to check the git diff to see if this is just a remark change or if it’s already tracked. Let's use git diff to verify that!
codex
A local inconsistency just surfaced: the build log shows the old undefined `\E_2`, but the live file on disk now reads `\Etwo` at that line. I’m checking the diff once so I don’t overwrite someone else’s concurrent fix or misreport the verification state.
exec
/bin/zsh -lc "rg -n -F '\\E_2' chapters/theory/bar_cobar_adjunction_inversion.tex main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 exited 1 in 52ms:

 succeeded in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Troubleshooting Git Output**

I'm looking into why there's no output from the diff/status commands. It seems odd; could it be related to max_output_tokens? I wonder if it has to do with the commands not producing output due to cleanliness, but that shouldn't be the case. Maybe I need to try a plain exec without tty. I’m thinking of running `git diff -- chapters... | sed -n '1,120p'` separately to see if that changes anything.
exec
/bin/zsh -lc "git status --short | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M main.log
 D main.out
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]



thinking
**Analyzing git status**

I noticed that the git status shows only main.log and main.out changed. That makes me consider whether the edited file isn't shown because the working tree is clean. This might mean our remark was automatically committed, but that's impossible. Maybe the repository has `assume unchanged`? I should check with `git diff -- chapters/...`, as it's possible that our changes reverted to what was already in HEAD. It seems like someone may have already applied the same remark, even though `apply_patch` said it was a success. Strange situation!
thinking
**Inspecting file changes**

The user asked for edits, so I’m thinking if the file already had those changes, there might not actually be any updates. However, `apply_patch` should indicate no changes if that's the case, yet it applied anyway. It could be that the index isn't refreshed. Hmm, maybe I should inspect the differences between HEAD and the modified file. I think using `git show HEAD:chapters/... | sed -n '1928,2015p'` would help me compare them effectively.
exec
/bin/zsh -lc "git show HEAD:chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1928,2015p'" in /Users/raeez/chiral-bar-cobar succeeded in 126ms:
\end{remark}

\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
\label{rem:koszul-locus-off-locus-obstruction}
\index{Koszul locus!off-locus obstruction}
\index{bar-cobar inversion!off-locus obstruction}
The phrase ``Koszul locus'' in
Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
kept separate: the genus-$0$ Koszul condition of
Definition~\ref{def:koszul-locus}, and the higher-genus coderived
continuation of the same bar-cobar comparison. The research picture is
therefore:
\begin{enumerate}[label=\textup{(\arabic*)}]
\item \emph{Precise genus-$0$ locus.}
 The Koszul locus is the full subcategory
 $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
 counit
 \[
 \Omega_X(\barB_X(\cA)) \longrightarrow \cA
 \]
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]



thinking
**Analyzing patch changes**

Alright, I see that the HEAD already contained our final text, so the patch we made didn't change anything. It seems the live repo had the remark before we started, which is curious since a previous command showed an older version. This implies that both HEAD and the working tree might have been updated before our changes, which makes sense since after applying the patch, everything aligned to HEAD. I think the working copy may have been modified but unstaged initially. So, in a way, we did make an edit but ended up clean relative to HEAD. That's interesting!
thinking
**Preparing for build**

It sounds like I need to focus on building with the current \Etwo to progress further. I should rerun latexmk, as there was no failure at the last check, but I need to be aware that the build might still fail elsewhere. I'll do a second run since the main.log and output are dirty. Alright, let’s go ahead and rerun the build to see how it goes!
codex
The live file and `HEAD` now agree on the fortified remark, so there is no unresolved local drift. I’m rerunning the TeX pass once against the current tree to see whether the earlier undefined control sequence is gone and whether any remaining failure is elsewhere.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

 exited 12 in 2.08s:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  chapters/theory/algebraic_foundations.aux
  chapters/theory/bar_cobar_adjunction.aux
  chapters/theory/chiral_hochschild_koszul.aux
  chapters/theory/chiral_koszul_pairs.aux
  chapters/theory/chiral_modules.aux
  chapters/theory/configuration_spaces.aux
  chapters/theory/higher_genus.aux
  chapters/theory/introduction.aux
  chapters/theory/koszul_pair_structure.aux
  chapters/theory/poincare_duality.aux
  chapters/theory/poincare_duality_quantum.aux
  chapters/theory/quantum_corrections.aux
  main.aux
Category 'changed_user':

thinking
**Considering timing for poll**

I'm thinking that maybe I should wait about 30 seconds before launching the poll. That seems like a reasonable time frame to let the initial responses settle. It’s important not to rush, as I want to ensure everyone has a chance to participate! I'll make sure I keep track of the timing so I can execute it smoothly.
codex
The rerun passed the earlier undefined-control-sequence point. I’m waiting for the first actual hard stop; if one appears later, that gives us a clean separation between the Theorem B band and the next broken surface in the tree.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]



thinking
**Considering aux files deletion**

I’m noticing there are many aux files that could be deleted. I think a command like `find . -name '*.aux' -delete` might help here, but I'm uncertain about its impact on the repository. The user desires healing, so it seems worth a shot. 

I need to verify if these aux files are tracked by Git since the status only showed main.log and main.out. Cleaning them up could help, but I should check if using `latexmk -C` would also remove necessary files. Rerunning the build could give a clearer outcome.
thinking
**Cleaning auxiliary files**

I noticed the build failed due to a runaway in main.aux, probably from bad label syntax. If I clean the aux files, that might resolve the issue. I’m considering using `latexmk -C` to clean everything or removing just `main.aux` and its included aux files. It could be safer to target `latexmk -C main.tex`, but I worry it might remove the PDF too. Still, I think running `latexmk -C main.tex` could be the best option to start fresh.
codex
The second failure is now clearly global build-state corruption in the generated `.aux` layer, not the theorem band: `Runaway argument ... \@newl@bel` at `main.aux` load time. I’m cleaning the generated LaTeX artifacts and rerunning once from a cold state, which is the only honest way to tell whether the source tree itself parses.
exec
/bin/zsh -lc 'latexmk -C main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
No specific requests made, so using default for latexmk.
Latexmk: Doing main (small) clean up for 'main.tex'

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

codex
The cold build is still in early parsing, but the previous `.aux` corruption is gone. I’m polling for the next hard stop so the verification result is actually meaningful.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Considering output status**

I'm monitoring the output, and so far, there haven't been any errors. It seems like it's still running, and the output is quite large! I should think about how we can eventually get an exit feedback if needed. Polling with a lower max output might be a good strategy to help manage this and keep things moving smoothly. I'm curious how we can optimize this process!
 exited 12 in 15.63s:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/memoir.cls
Document Class: memoir 2025/03/06 v3.8.3 configurable book, report, article doc
ument class
(/usr/local/texlive/2025/texmf-dist/tex/latex/xpatch/xpatch.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3kernel/expl3.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def))
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty))
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/mem11.clo)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/dcolumn.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/delarray.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/tabularx.sty)
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Cleaning build artifacts**

I’ve encountered a build failure due to an undefined control sequence, `\ord`. I verified that the local edit is fine, but the build logs have become huge, and there are changes in the generated artifacts. I’m considering whether we should keep the changes in main.log since it comes from our build. It might be best to revert or clean up, so I think I’ll run `latexmk -C main.tex` to avoid any dirty artifacts. Cleaning seems safe now!
codex
The source tree got far enough to show that the Theorem B band is no longer the blocker. The current hard stop is a different file, [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677), with an undefined `\ord` macro. I’m cleaning the generated build artifacts now so I don’t leave verification noise behind.
exec
/bin/zsh -lc 'latexmk -C main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
No specific requests made, so using default for latexmk.
Latexmk: Doing main (small) clean up for 'main.tex'

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]


thinking
**Checking git status**

Let me check the current status of my Git repository. I want to see if there are any changes that are staged for commit or untracked files that I need to address. It's always a good practice to make sure everything is in order before I proceed with any other operations. I’ll run the command and review the output to get a clear picture of my project's current state.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1931,2015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git status --short | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1931	\label{rem:koszul-locus-off-locus-obstruction}
  1932	\index{Koszul locus!off-locus obstruction}
  1933	\index{bar-cobar inversion!off-locus obstruction}
  1934	The phrase ``Koszul locus'' in
  1935	Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
  1936	kept separate: the genus-$0$ Koszul condition of
  1937	Definition~\ref{def:koszul-locus}, and the higher-genus coderived
  1938	continuation of the same bar-cobar comparison. The research picture is
  1939	therefore:
  1940	\begin{enumerate}[label=\textup{(\arabic*)}]
  1941	\item \emph{Precise genus-$0$ locus.}
  1942	 The Koszul locus is the full subcategory
  1943	 $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
  1944	 counit
  1945	 \[
  1946	 \Omega_X(\barB_X(\cA)) \longrightarrow \cA
  1947	 \]
  1948	 is a quasi-isomorphism at genus~$0$
  1949	 \textup{(}Definition~\ref{def:koszul-locus},
  1950	 Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
 succeeded in 51ms:
 M chapters/connections/bv_brst.tex
 M chapters/connections/thqg_symplectic_polarization.tex
 M chapters/examples/yangians_computations.tex
 M compute/lib/elliptic_drinfeld_coproduct_engine.py
 M main.aux
 M main.log
 M main.out
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]



thinking
**Evaluating git commands**

I must remember that using destructive commands like `git checkout --` is a no-go unless the user explicitly permits it. I could use `git show HEAD:main.aux > main.aux`, but editing directly in the shell isn't allowed. The developer suggests using `apply_patch` for manual edits instead. Leaving build artifacts dirty might not be ideal, though. I could also consider restoring files with `git restore`, but that seems risky. Overall, I need to be careful with commands when handling generated files like `main.aux`.
thinking
**Considering build artifacts**

The user hasn't asked for a commit, so I think it’s acceptable to address the artifacts later. I might consider removing them from the working tree non-destructively, but previous attempts with `latexmk -C` didn't revert to the HEAD state. I could check the changes with `git diff --stat` for those files, but it might not be necessary. It could be good to mention that my full-build attempts modified the tracked TeX artifacts, and I may ask if the user wants me to clean them up. I aim to keep my response concise.
Plan update
The Research Remark now answers the four requested questions explicitly. Verification showed the Theorem B band parses past the touched surface; the full build is blocked later by an unrelated undefined macro in higher_genus_complementarity.tex.
  ✓ Read constitutional files, target file, and direct dependencies for Theorem B and the Koszul-locus definitions.
  ✓ Verify the existing Research Remark against the live theorem surface and identify any under-specified or over-strong claims.
  ✓ Edit the Research Remark to characterize the Koszul locus, derived wall, off-locus obstruction, and honest upgrade lanes.
  ✓ Run targeted verification: re-read the edited band, grep for local consistency issues, and summarize proof-strength/confidence for Theorem B.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

codex
The Theorem B research surface in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1934) now states the Koszul-locus question in the four pieces you asked for: the exact genus-0 definition, the off-locus obstruction as the first off-diagonal bar class and first transferred higher \(m_r\), the conjectural derived Koszul wall versus the proved abstract collapse criterion, and the family boundary where failure is expected. It also now says explicitly that clause (4) does not remove the genus-0 Koszul hypothesis.

I checked that against [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:236) and [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:274). A cold `latexmk` pass gets past this theorem band and then fails later, outside this surface, at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677) on an undefined `\ord` macro. Full-build verification is therefore blocked elsewhere. The build attempts also refreshed tracked TeX artifacts (`main.aux`, `main.log`, `main.out`).

## Fortification Report
Theorem B (`thm:bar-cobar-inversion-qi`)

- PRIMARY PROOF: `sound`
- SECONDARY PROOF: `written`
- TECHNIQUE: dependency-closed spectral-sequence/coderived proof; independent formality plus homotopy-transfer proof on the strict Koszul lane
- CONDITION STATUS: strict quasi-isomorphism conditional on the genus-0 Koszul locus and higher-genus modular input; off-locus coderived equivalence unconditional; ordinary off-locus promotion only by the abstract collapse criterion, with the derived wall still conjectural
- CONFIDENCE: `high`
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 7524d8bfad62d55f1396e7a2174796bab15bbf79..5c48ad5175d818d9826fbf6860d17c95dd7338c3
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1887,7 +1887,7 @@
 quadratic closure.
 
 The remaining step is formality of the transferred
-$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+$A_\infty$-structure on~$\cA^i$. The $\Etwo$-formality map realized by
 Kontsevich-type configuration-space integrals on
 Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
@@ -1932,62 +1932,86 @@
 \index{Koszul locus!off-locus obstruction}
 \index{bar-cobar inversion!off-locus obstruction}
 The phrase ``Koszul locus'' in
-Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
-genus-$0$ meaning: it is the full subcategory
-$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
-Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
-genus-$0$ counit
-\[
-\Omega_X(\barB_X(\cA)) \longrightarrow \cA
-\]
-is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
-collapses at~$E_2$; if and only if
-$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
-\textup{(}bar degree equal to internal degree, or after the
-reindexing used in
-Theorem~\ref{thm:bar-cobar-spectral-sequence},
-concentrated in bar degree~$1$\textup{)}. For a quadratic
-$A_\infty$ model this recovers the classical Priddy/BGS criterion:
-the bar cohomology is concentrated in weight~$1$.
+Theorem~\ref{thm:bar-cobar-inversion-qi} has two layers that should be
+kept separate: the genus-$0$ Koszul condition of
+Definition~\ref{def:koszul-locus}, and the higher-genus coderived
+continuation of the same bar-cobar comparison. The research picture is
+therefore:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item \emph{Precise genus-$0$ locus.}
+ The Koszul locus is the full subcategory
+ $\operatorname{Kosz}(X)$ of augmented chiral algebras for which the
+ counit
+ \[
+ \Omega_X(\barB_X(\cA)) \longrightarrow \cA
+ \]
+ is a quasi-isomorphism at genus~$0$
+ \textup{(}Definition~\ref{def:koszul-locus},
+ Remark~\ref{rem:equivalent-formulations-koszul}\textup{)}.
+ Equivalently, the PBW/bar spectral sequence collapses at~$E_2$; and
+ equivalently, $H^*(\barB_X(\cA))$ is concentrated on the Koszul
+ diagonal
+ \textup{(}bar degree equal to internal degree, or after the
+ reindexing of Theorem~\ref{thm:bar-cobar-spectral-sequence},
+ concentrated in bar degree~$1$\textup{)}. For a quadratic
+ $A_\infty$ model this is exactly the classical Priddy/BGS criterion:
+ bar cohomology concentrated in degree~$1$.
 
-The obstruction off the locus is equally concrete: the first
-off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
-bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
-strict square-zero proof loses diagonal concentration, higher
-differentials need not vanish, and the cone of the counit can stop
-being acyclic in the ordinary derived category. In the quotient
-examples already isolated in the manuscript, this class is created by
-a null-vector ideal or a non-flat PBW degeneration: singular vectors
-enter the bar-relevant range, or composite relations survive in bar
-degree $\geq 2$, so the PBW collapse no longer forces strict
-inversion.
+\item \emph{Off-locus obstruction.}
+ The first obstruction is the first bar class off the Koszul
+ diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
+ $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
+ concentration is lost, the square-zero $E_2$-collapse proof breaks,
+ and the genus-$0$ counit need not be a quasi-isomorphism. After
+ homotopy transfer, the same obstruction appears as the first
+ non-vanishing higher multiplication
+ $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
+ This is distinct from the higher-genus curvature
+ $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
+ even on the Koszul locus, while the off-diagonal bar class is what
+ removes strict genus-$0$ inversion.
 
-What survives off the locus is unconditional and already proved:
-clause~\textup{(2)} of
-Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
-coacyclic-equivalence for every complete augmented input with
-finite-dimensional graded bar pieces. The natural enlargement of
-$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
-chiral algebras, but a derived Koszul locus: the full substack on
-which the coderived cone is still detected by ordinary cohomology.
-Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
-derived wall. The proved upgrade is narrower: promotion from coderived
-equivalence back to a genuine quasi-isomorphism holds on the collapse
-loci singled out in clause~\textup{(4)}, including the flat case
-$\kappa(\cA)=0$ and any family for which the coderived bar-degree
-spectral sequence degenerates to ordinary cohomology.
+\item \emph{How far the quasi-isomorphism extends.}
+ Off the locus, the strongest unconditional statement is already
+ clause~\textup{(2)} of
+ Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
+ augmented input with finite-dimensional graded bar pieces, the cone
+ of the factorization counit is coacyclic, hence the counit is an
+ isomorphism in the coderived category. The natural enlargement of
+ $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
+ Koszul locus}: the full derived substack on which this coacyclic cone
+ is still detected by ordinary cohomology.
+ Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
+ derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
+ upgrades the coderived equivalence only on collapse loci where the
+ coderived bar-degree filtration degenerates to ordinary cohomology.
+ No specific non-Koszul family is presently proved by a separate
+ family-level argument to satisfy that promotion hypothesis. The live
+ theorem is the abstract collapse criterion of clause~\textup{(4)}.
+ In particular, this does \emph{not} remove the genus-$0$ Koszul
+ hypothesis of Definition~\ref{def:koszul-locus}; it only says that
+ after one passes to the curved or completed factorization surface,
+ some off-locus families may still lie on the derived side of the
+ wall.
 
-From this viewpoint, the restrictive surface is not the standard
-universal landscape but its pathological quotient boundary. Freely
-strongly generated or generic-level families are designed to stay on
-the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
-and the principal $\cW$-families enter through PBW-flat models. The
-genuine candidates for leaving the locus are quotient algebras with
-null-vector ideals in the bar-relevant range, minimal-model
-quotients, higher-rank admissible simple quotients, and other
-non-flat or non-freely-generated degenerations. Even there the
-coderived comparison remains available; what fails is only the
-promotion from coacyclicity to an ordinary quasi-isomorphism.
+\item \emph{Which families are expected to leave the locus.}
+ On the live proved surface, the restrictive boundary is not the
+ universal or freely strongly generated landscape but its singular
+ quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
+ Virasoro, and the principal $\cW$-families enter through PBW-flat
+ models and are treated as on-locus. The genuine off-locus candidates
+ are quotient algebras with null-vector ideals in the bar-relevant
+ range: simple admissible affine quotients, minimal-model Virasoro and
+ $\cW$-quotients, critical-level enlargements with extra center, and
+ other non-flat PBW degenerations. For such families the coderived
+ comparison remains available; what is missing is ordinary
+ cohomological detectability of the coacyclic cone. The admissible
+ $\widehat{\mathfrak{sl}}_2$ example of
+ Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ conjectural $2$-Koszul behavior would move it closer to the derived
+ wall, but by itself would not yet supply the promotion required in
+ clause~\textup{(4)}.
+\end{enumerate}
 \end{remark}
 
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]

tokens used
180,469
