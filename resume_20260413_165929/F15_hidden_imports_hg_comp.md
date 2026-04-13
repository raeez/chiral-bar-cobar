# F15_hidden_imports_hg_comp (676s)

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:356` — PROBLEM: Lemma `lem:perfectness-criterion` concludes perfectness from finite-dimensional fiber cohomology plus base change, but the proof never proves pseudo-coherence/coherence of the infinite bar complex, and the cited base-change step only gets you as far as bounded/coherent direct images, not perfection. FIX: Strengthen the lemma to assume bounded pseudo-coherent/coherent filtered pieces and use regularity of `\overline{\mathcal M}_g` to pass from bounded coherent to perfect; otherwise weaken the conclusion to bounded coherent and stop using this lemma as a perfection criterion.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:477` — PROBLEM: C0 Step 3 cites `thm:cobar-resolution-scoped` to identify the genus-`g` strict flat bar family as a bar resolution, but `chapters/theory/higher_genus_foundations.tex:2061` is a genus-0 bar-cobar resolution statement and does not prove a relative genus-`g` resolution over moduli. FIX: Insert a new relative higher-genus resolution lemma for `R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)` and cite that here; if you do not have that lemma, delete the resolution-based center identification from C0(ii).

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:480` — PROBLEM: C0 Step 3 cites `thm:obstruction-quantum` to identify `\mathcal H^0(R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA))` with `\mathcal Z_{\cA}`, but `chapters/theory/higher_genus_foundations.tex:4601-4607,4649-4654` only identifies `\mathcal H^0` of the endomorphism complex `\mathcal E^\bullet_{g,\mathrm{flat}}(\cA)` with the center. That is the wrong object. FIX: Replace this citation with a lemma computing `H^0` of the flat fiber bar complex itself, or weaken C0(ii) to the vanishing statement until the pushforward-to-center identification is actually proved.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:532` — PROBLEM: Theorem C1 is quantified over every “chiral Koszul pair”, but its statement and proof use the center local system, genus-`g` bar families, Verdier-in-families, and higher-genus differentials from the modular pre-Koszul package, not bare genus-0 Koszulity. FIX: Change the opening hypothesis to “Let `(\cA,\cA^!)` be a chiral Koszul pair carrying the modular pre-Koszul datum/MK1–MK3 of Definition `def:modular-koszul-chiral`,” and propagate that scope to Definition `def:complementarity-complexes` and Steps I–III.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:848` — PROBLEM: Step I builds the Leray spectral sequence from `\overline{C}_n(X)\times \overline{\mathcal M}_g \to \overline{\mathcal M}_g`, which is the wrong geometry for varying curves. The proof needs the universal compactified configuration family, not a product with a fixed `X`. FIX: Replace the displayed fibration by the universal relative configuration map already implicit at lines 785-793, rewrite `E_1/E_2` using its pushforwards, and remove the fixed-product language.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1597` — PROBLEM: The sublemma `Z(\cA)\cong Z(\cA^!)` is proved by invoking `thm:e1-module-koszul-duality`, but `chapters/theory/chiral_koszul_pairs.tex:5682-5698` explicitly says the general chiral module-category duality surface is not proved, and `5703-5716` only covers the complete/conilpotent `\Eone`, quadratic, genus-0 lane. FIX: Delete this proof and either prove a direct center-comparison theorem under the current higher-genus hypotheses or restate Step 8 as a duality between `Z(\cA)` and `Z(\cA^!)` without identifying them.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1556` — PROBLEM: Step 8 turns Verdier duality between the `\cA` and `\cA^!` spectral sequences into an involution `\sigma` on `H^*(\overline{\mathcal M}_g,Z(\cA))` itself, then into `\pm1` eigenspaces at lines 1643-1742. That self-identification is exactly the unproved point. FIX: Restate Lemmas `lem:verdier-involution-moduli` and `lem:eigenspace-decomposition-complete` as an isomorphism/pairing between the `\cA` and `\cA^!` coefficient systems; only reintroduce a single-space involution after proving an honest self-identification of centers.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:495` — PROBLEM: C0(iii) claims that `\kappa(\cA)=0` lets the conclusion of C0(ii) be read directly on the curved model, but `\dfib^2=0` only makes the curved model an ordinary complex; it does not identify `(\barB^{(g)},\dfib)` with `(\barB^{(g)},\Dg{g})`. FIX: Either prove a comparison quasi-isomorphism at `\kappa=0`, or weaken C0(iii) to “the curved model becomes an ordinary complex” and stop there.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:828` — PROBLEM: Step I calls `d_{\mathrm{fiber}}` the fiber differential and then proves `d_{\mathrm{fiber}}^2=0` from Arnold at line 871, contradicting `chapters/theory/higher_genus_foundations.tex:238-271`, where the genus-`g` fiber differential satisfies `\dfib^2=\kappa(\cA)\omega_g`. FIX: Rename the `E_1`-page differential to the genus-0 collision part `\dzero`/`d_{\mathrm{coll}}`, and state explicitly that the spectral sequence filters the strict flat differential `\Dg{g}`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:600` — PROBLEM: The printed proof of Theorem C1 closes at line 1870 after proving the S-level splitting, but the theorem statement also claims an H-level cochain pairing and functorial/graded compatibility. The post-proof remark at 1874-1900 is not part of the proof and still does not establish the pairing or grading clause. FIX: Move the H-level argument into the theorem proof before `\qedhere`, add a separate cochain-level Verdier pairing lemma, and either prove functoriality/weight compatibility there or delete those clauses from the theorem statement.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1445` — PROBLEM: Step 7 specializes to `H^*(\overline{\mathcal M}_g,Z(\cA))` using `lem:fiber-cohomology-center`, but that lemma only proves the center identification on the smooth locus at `chapters/theory/higher_genus_complementarity.tex:1018-1026`. The boundary extension is missing. FIX: Insert a boundary-extension lemma before line 1445 and cite it; otherwise replace the compactified-moduli cohomology in Step 7-10 by the smooth locus.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2123` — PROBLEM: C2 defines `L_g:=\barB^{(g)}(\cA)[1]` as a dg Lie algebra, but in this chapter the genus-`g` bar complex is ambiguous and the fiberwise model is curved. The proof never proves that the conditional BV bracket on `\barB^{\mathrm{ch}}(\cA)` descends to the strict flat genus-`g` chart. FIX: Replace `L_g` by `L_g:=\barB^{(g)}_{\mathrm{flat}}(\cA)[1]` everywhere in C2, and add a lemma that the BV bracket is compatible with the genus filtration and restricts to each fixed-genus strict flat chart.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2105` — PROBLEM: C2 uses `thm:verdier-bar-cobar` as a generic all-genus input, but `chapters/theory/cobar_construction.tex:1316-1320` tags that theorem as `[Regime: quadratic, genus-0]`. The same proof then invokes Kontsevich-Pridham at lines 2186-2190 without importing completeness/pronilpotence for the dg Lie algebra. FIX: Restrict C2 to the quadratic genus-0 lane or replace the citation with a family/genus-`g` Verdier comparison theorem, and add an explicit hypothesis that the completed `L_g` is pronilpotent/complete before applying Kontsevich-Pridham.

## Summary
Checked: 13 | Findings: 13 | Verdict: FAIL


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
session id: 019d8774-0777-7530-9d69-3f3a5d1ad352
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_complementarity.tex

Same: hidden imports for C0/C1/C2 proofs.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Optimizing tool usage**

I need to consider using multi_tool_use.parallel to handle file reads effectively. Since I can’t browse the internet due to network restrictions, using tools like rg might be crucial. It feels like I might not need to update my plan much. However, because this task is substantial, it might help to provide a longer plan after gathering enough context. I'll start with sending a brief update in commentary.
codex
Auditing `chapters/theory/higher_genus_complementarity.tex` as a hostile proof surface. I’m loading the required constitutional files, the audit skill, and the target chapter plus its immediate dependencies before I enumerate findings.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
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
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
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
**Evaluating map options**

I'm considering using an explorer tool to get a map, which sounds like a straightforward approach. After that, we could read the files ourselves—it might work out well. I should probably keep the user updated with our progress too, just to make sure they're in the loop. It's always nice to communicate what we’re doing. So let's see how this goes!
codex
I’ve loaded the constitutional surface and the target chapter opening. Next I’m tracing the exact proof blocks for `C0/C1/C2`, then reading every referenced theorem/lemma those proofs import so the findings are grounded in the actual dependency chain, not the summary prose.
collab spawn_agent(call_STtfHTQnQHBxTrn3i1Ybs1mG, prompt="Map the audit surface for chapters/theory/higher_genus_complementarity.tex. I need the exact line ranges for: the statem…")
mcp startup: no servers
spawn_agent(call_STtfHTQnQHBxTrn3i1Ybs1mG, prompt="Map the audit surface for chapters/theory/higher_genus_complementarity.tex. I need the exact line ranges for: the statem…") pending init:
  agent: 019d8774-8416-7b61-b792-15ed9c3b7dac

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
thinking
**Updating the plan**

I think I need to consider creating a structured plan or updating my current one. Maybe I should outline my main objectives, steps, and any resources I might need to make sure everything is clear. Taking my time with this could really help ensure that I'm covering all the bases. I'm curious to see how this updated plan might improve my process — let's see where it takes me!
Plan update
Hostile audit of the complementarity chapter requires reading the live proof surface, tracing direct imports, then checking second-order dependency failures before reporting only re-verified findings.
  → Locate the C0/C1/C2 theorem blocks and extract their proof-local dependency graph from the target chapter.
  • Read the cited dependency surfaces in context and test each import for missing hypotheses, hidden definitional dependencies, unresolved references, or status drift.
  • Re-verify surviving findings against exact lines and produce the audit report in the requested severity format.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C0" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
104:The fiber--center identification~(C0) holds unconditionally in
372:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '300,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\bigl(\barB^{(g)}(\cA), \Dg{g}\bigr)
\]
for the strict flat comparison family of
Convention~\textup{\ref{conv:higher-genus-differentials}}.
Suppose the following two conditions hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{PBW filterability.}
 The genus-$g$ bar complex $\bar{B}^{(g)}(\cA)$ admits an
 exhaustive multiplicative filtration~$F_\bullet$ such that the
 associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
 sees only the genus-$0$ collision differential~$\dzero$ and is
 Koszul-acyclic \textup{(}axioms \textup{MK1} and
 \textup{MK3} of
 Definition~\textup{\ref{def:modular-koszul-chiral})}.

\item \emph{Finite-dimensional flat fiber cohomology.}
 For each closed point
 $[\Sigma] \in \overline{\mathcal{M}}_g$,
 $\dim_\mathbb{C} H^n\bigl(
 \bar{B}^{(g)}_{\mathrm{flat}}(\cA)\big|_\Sigma\bigr)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "quantum-complementarity" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
504:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
525:\label{thm:quantum-complementarity-main}
526:\label{thm:quantum-complementarity}
670:The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
988:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
1342:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
1358:Theorem~\ref{thm:quantum-complementarity-main}.
1834:Theorem~\ref{thm:quantum-complementarity-main}.
1870:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
1879:Theorem~\ref{thm:quantum-complementarity-main} via three steps.
1951:Theorem~\ref{thm:quantum-complementarity-main}, Step~7), so the
1967:Theorem~\ref{thm:quantum-complementarity-main}), the involution
1988:Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
2306: (Theorem~\ref{thm:quantum-complementarity-main}), we have
2441:The conjecture asserts that quantum complementarity (Theorem~\ref{thm:quantum-complementarity-main}) reproduces established physics identifications (central charge duality, marginal-obstruction exchange, electric-magnetic splitting) when applied to specific CFT Koszul pairs.
2461:complementarity decomposition is functorial (property 3 of Theorem~\ref{thm:quantum-complementarity-main}), it commutes with the modular action.
2580:(Theorem~\ref{thm:quantum-complementarity-main}):
2649:(Theorem~\ref{thm:quantum-complementarity-main}) with
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '520,900p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

thinking
**Running file analysis**

I need to read the target file more closely. It seems like using the `rg` tool for theorem labels might be helpful. I also want to gather line counts and direct references, which could offer useful insights. I'll consider utilizing parallel execution commands to optimize the process. This way, I can efficiently gather the necessary data without wasting too much time. Let's see how this goes!
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,620p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|lem:perfectness-criterion|prop:gauss-manin-uncurving-chain|prop:standard-examples-modular-koszul|thm:verdier-bar-cobar|lem:involution-splitting|ClaimStatus|begin\\{theorem\\}|begin\\{lemma\\}|begin\\{proposition\\}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,980p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1340p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    6420 chapters/theory/higher_genus_complementarity.tex
 succeeded in 51ms:
Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
via the standard cone identification.
Part~(b) follows by applying $H^*$ to~(a).
Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
Maximality is immediate from the direct-sum decomposition.
\end{proof}

\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
\index{bar complex!relative fiber|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
\[
\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
\overline{\mathcal{M}}_g
\]
be the family of genus-$g$ compactified configuration spaces
carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
 succeeded in 51ms:
ambient-level $D^2 = 0$
(Theorem~\textup{\ref{thm:ambient-d-squared-zero}},
which uses \textup{[}Mok25\textup{]}) or on the full
bar-intrinsic MC element $\Theta_\cA$
(Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}).
The only curvature input is the scalar $\kappa(\cA)$,
which comes from the convolution-level
$D^2 = 0$ (unconditional).
\end{remark}

\begin{remark}[Elementary model presentation;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-c-model}
\label{rem:complementarity-model}% backward-compatible label
\index{complementarity!model presentation}
\emph{Step~B} (M-level): The homotopy eigenspace
$\mathbf{Q}_g(\cA)=\operatorname{fib}(\sigma-\mathrm{id})$ is modeled by
$\operatorname{im}(p^+)$ with $p^+=\tfrac{1}{2}(\mathrm{id}+\sigma)$
on $C_g=R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$.
The Lagrangian property is $\langle p^+x,p^+y\rangle=0$
 succeeded in 51ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
50: \textup{(}Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}\textup{)}.
57: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
84: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
100:flat fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
103:(Proposition~\ref{prop:standard-examples-modular-koszul}).
126:base change (Lemma~\ref{lem:perfectness-criterion}).
207:(Theorem~\ref{thm:verdier-bar-cobar}).
230:(Lemma~\ref{lem:involution-splitting}) makes the passage automatic
234:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
235:\label{lem:involution-splitting}
288:\begin{lemma}[Perfectness criterion for the strict flat relative bar family;
289:\ClaimStatusProvedHere]
290:\label{lem:perfectness-criterion}
372:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
373:\label{thm:fiber-center-identification}
397: coderived object. Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}
404: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
439:Proposition~\ref{prop:gauss-manin-uncurving-chain} supplies the strict
 succeeded in 51ms:
\end{equation}

The genus-$g$ quantum corrections are precisely those cohomology classes that arise 
from genus-$g$ contributions but not from lower genus. Thus:
\begin{equation}
Q_g(\mathcal{A}) := \text{gr}^g H^*(\bar{B}(\mathcal{A})) = E_\infty^{*,*,g}
\end{equation}
We use the same notation $Q_g(\mathcal{A})$ for this graded piece,
anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
which identifies it with the $+1$-eigenspace of the Verdier involution
(Definition~\ref{def:complementarity-complexes}).
The two characterizations coincide: the filtration graded
piece captures the part of bar cohomology coming from genus~$g$,
while the eigenspace captures the $\mathcal{A}$-sector under
Verdier involution.
The identification is proved in
Lemma~\ref{lem:eigenspace-decomposition-complete}: the Verdier
involution sorts contributions according to whether they arise
from $j_*$-extended bar cochains of~$\mathcal{A}$ (eigenvalue~$+1$) or
from $j_!$-extended bar cochains of~$\mathcal{A}^!$ (eigenvalue~$-1$),
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '330,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   330	\emph{Step~1: Uniform cohomological bound from the associated graded.}
   331	The PBW filtration~$F_\bullet$ is flat over the base
   332	$\overline{\mathcal{M}}_g$ (it is a bar-degree filtration,
   333	hence defined fiber-by-fiber by the combinatorial bar grading).
   334	At the associated graded level the quantum correction terms in
   335	$\Dg{g}$ sit in positive filtration degree, so
   336	$\operatorname{gr}_F$ carries only the genus-$0$
   337	differential~$\dzero$. By Koszul acyclicity~(i), the
   338	cohomology of $\operatorname{gr}_F$ is concentrated in total
   339	degree~$0$, giving a uniform vanishing range
   340	$H^q(\operatorname{gr}_F\bar{B}^{(g)}_{\mathrm{flat}}(\cA)\big|_\Sigma) = 0$
   341	for $q \neq 0$ at every point of the base.
   342	
   343	\emph{Step~2: Transfer to the filtered complex.}
   344	The bar-degree filtration spectral sequence
   345	$E_1^{p,q} =
   346	H^q(\operatorname{gr}_p\bar{B}^{(g)}_{\mathrm{flat}}(\cA)\big|_\Sigma)$
   347	has $E_1^{p,q} = 0$ for $q \neq 0$ by Step~1. All higher
   348	differentials $d_r$ ($r \geq 2$) therefore vanish (they map into
   349	or out of the zero row), and the spectral sequence collapses at
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '520,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   520	The Heisenberg complementarity
   521	of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
   522	polarization:
   523	
   524	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   525	\label{thm:quantum-complementarity-main}
   526	\label{thm:quantum-complementarity}
   527	\index{deformation-obstruction complementarity|textbf}
   528	\index{Lagrangian!complementarity|textbf}
   529	\textup{[}Regime: curved-central
   530	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   531	
   532	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
   533	curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
   534	the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
   535	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
   536	Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
   537	for the ambient complex and homotopy eigenspaces of
   538	Definition~\textup{\ref{def:complementarity-complexes}}.
   539	

thinking
**Planning theorem analysis**

I have enough information to inspect theorems C0, C1, and C2, particularly focusing on their statements and proofs. I need to read the C2 theorem block and check the detailed proof for C1 in the file around line 1556. 

There's a theorem regarding the shift symplectic and supporting propositions I should consider. I also need to look at the theorem on quantum complementarity, which may have a placeholder proof earlier in Step III. 

I’ll check lines 1550-2085 for more context on the C2 theorem and identify relevant dependencies and citations in the repo. This involves using fitting commands across the repo for the cited labels.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "conv:higher-genus-differentials" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 550

wave2_audit_20260413_001942/C04_bar_construction.md:606:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:898:/bin/zsh -lc "rg -n \"conv:higher-genus-differentials|dfib|d_fib|d\\"'^2_bar=0|d_fib'"\\"'^2|fiberwise differential|curvature" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:973:/bin/zsh -lc "rg -n \"conv:higher-genus-differentials|D_g|\\\\Dg\\{|period-corrected differential|total corrected differential|quantum-diff-squares-zero|higher-genus-open-stratum-qi|higher-genus-boundary-qi|extension-across-boundary-qi|BD-extension-higher-genus\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:979:chapters/theory/bar_cobar_adjunction_inversion.tex:675:($\dfib^{\,2} = \mcurv{g} \neq 0$; Convention~\ref{conv:higher-genus-differentials}). In the curved case, ordinary
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:990:chapters/theory/bar_cobar_adjunction_inversion.tex:3350:(see Convention~\ref{conv:higher-genus-differentials} for the notation).
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:996:/bin/zsh -lc "rg -n \"begin\\{convention\\}.*higher-genus-differentials|label\\{conv:higher-genus-differentials\\}|higher-genus differentials\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1020:/bin/zsh -lc "rg -n \"label\\{conv:higher-genus-differentials\\}|higher-genus-differentials\" chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1021:chapters/theory/bar_construction.tex:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1022:chapters/theory/coderived_models.tex:154:(Convention~\ref{conv:higher-genus-differentials}).
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1023:chapters/theory/coderived_models.tex:203: Convention~\textup{\ref{conv:higher-genus-differentials}});
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1024:chapters/theory/bar_cobar_adjunction_inversion.tex:675:($\dfib^{\,2} = \mcurv{g} \neq 0$; Convention~\ref{conv:higher-genus-differentials}). In the curved case, ordinary
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1025:chapters/theory/bar_cobar_adjunction_inversion.tex:3350:(see Convention~\ref{conv:higher-genus-differentials} for the notation).
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1026:chapters/theory/bar_cobar_adjunction_inversion.tex:3912:(Convention~\ref{conv:higher-genus-differentials}) are three levels of
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1027:chapters/theory/chiral_hochschild_koszul.tex:126:Convention~\ref{conv:higher-genus-differentials}), so the bar complex
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1028:chapters/theory/chiral_hochschild_koszul.tex:2900:(Convention~\ref{conv:higher-genus-differentials}(ii)), which
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1029:chapters/theory/chiral_hochschild_koszul.tex:3226: \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))}.
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1030:chapters/theory/chiral_hochschild_koszul.tex:3275:of Convention~\ref{conv:higher-genus-differentials}(ii):
rectification_20260412_233715/R25_bar_cobar_adjunction_inversion.md:1031:chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '210,280p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   210	$L_\infty$ structure and the modular envelope appear in
   211	\S\ref{sec:koszul-across-genera}.
   212	
   213	\begin{remark}[Parallel track: the anomaly]\label{rem:anomaly-parallel-track}
   214	\index{conformal anomaly!parallel track}
   215	\begin{center}
   216	\small
   217	\begin{tabular}{ll}
   218	\textbf{This chapter} & \textbf{Physics reading} \\ \hline
   219	Fiberwise curvature $\dfib^{\,2} = \kappa \cdot \omega_1$ & Conformal anomaly \\
   220	$\kappa(\cA) = 0$ (flatness) & $\kappa_{\mathrm{eff}} = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$ \\
   221	Coderived category & Off-shell (curved background) \\
   222	Obstruction class $\mathrm{obs}_g$ & One-loop determinant on $\Sigma_g$ \\
   223	Complementarity $Q_g + Q_g' = H^*$ & Matter--ghost pairing
   224	\end{tabular}
   225	\end{center}
   226	These are theorems (Theorem~\ref{thm:brst-bar-genus0}), not analogies.
   227	\end{remark}
   228	
   229	\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
codex
I’ve reached the actual theorem blocks. The next pass is narrower: line-numbered reads around `C0`, the deferred `C1` proof steps, `C2`, and every imported label those proofs cite, so I can separate genuine dependency failures from presentational noise.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1900,2145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1540,1895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '280,610p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(prop:ptvv-lagrangian|thm:shifted-symplectic-complementarity|lem:eigenspace-decomposition-complete|thm:verdier-duality-config-complete|thm:kodaira-spencer-chiral-complete)\\}\" chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(prop:gauss-manin-uncurving-chain|thm:cobar-resolution-scoped|thm:obstruction-quantum|thm:verdier-bar-cobar|prop:standard-examples-modular-koszul|thm:chiral-koszul-duality|thm:kodaira-spencer-chiral-complete|prop:model-independence|thm:ambient-d-squared-zero|thm:mc2-bar-intrinsic|conv:higher-genus-differentials|def:modular-koszul-chiral|conv:regime-tags)\\}\" -n chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1900	\end{remark}
  1901	
  1902	\begin{remark}[Geometric substrate (Volume~II)]
  1903	\label{rem:theorem-c-lagrangian}
  1904	\index{Lagrangian self-intersection!Theorem C}
  1905	Volume~II interprets the complementary decomposition as two
  1906	Lagrangians $\mathcal{L}$ and $\mathcal{L}^!$ inside a
  1907	$(-2)$-shifted symplectic stack $\mathcal{M}$, whose derived
  1908	intersection $\mathcal{L} \times_{\mathcal{M}} \mathcal{L}^!$
  1909	carries the $(-1)$-shifted symplectic structure that governs the
  1910	Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
  1911	\end{remark}
  1912	
  1913	\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
  1914	\label{prop:lagrangian-eigenspaces}
  1915	\index{Lagrangian!eigenspaces|textbf}
  1916	\index{Verdier duality!pairing on moduli}
  1917	Let $(\cA, \cA^!)$ be a chiral Koszul pair and let
  1918	$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
  1919	\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
  1540	$H^*(\overline{\mathcal{M}}_{1,1})$ is:
  1541	\begin{equation}
  1542	\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
  1543	\end{equation}
  1544	where $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle.
  1545	This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
  1546	the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
  1547	\end{proof}
  1548	
  1549	\emph{Step 8: Verdier involution and eigenspace decomposition.}
  1550	
  1551	The anti-commutativity~\eqref{eq:verdier-ks-anticommute} is the key to the
  1552	eigenspace decomposition. We construct a canonical involution on $H^*(\overline{
  1553	\mathcal{M}}_g, Z(\mathcal{A}))$ whose $\pm 1$ eigenspaces give $Q_g(\mathcal{A})$
  1554	and $Q_g(\mathcal{A}^!)$.
  1555	
  1556	\begin{lemma}[Verdier involution on moduli cohomology; \ClaimStatusProvedHere]
  1557	\label{lem:verdier-involution-moduli}
  1558	For a chiral Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, Verdier duality on
  1559	$\overline{C}_n(X)$ together with the Koszul pairing $\mathcal{A} \otimes
 succeeded in 51ms:
   280	Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
   281	\emph{genus-$g$ fiber bar complex}
   282	$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
   283	on the fixed curve~$\Sigma$ with the fiberwise curved
   284	differential~$\dfib$
   285	\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
   286	\end{definition}
   287	
   288	\begin{lemma}[Perfectness criterion for the strict flat relative bar family;
   289	\ClaimStatusProvedHere]
   290	\label{lem:perfectness-criterion}
   291	\index{perfectness criterion|textbf}
   292	\index{bar complex!relative perfectness|textbf}
   293	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
   294	curve~$X$, carrying a modular pre-Koszul datum
   295	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
   296	Write
   297	\[
   298	\barB^{(g)}_{\mathrm{flat}}(\cA)
   299	\;:=\;
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:1165:\label{thm:verdier-duality-config-complete}
chapters/theory/higher_genus_complementarity.tex:1368:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1644:\label{lem:eigenspace-decomposition-complete}
chapters/theory/higher_genus_complementarity.tex:2083:\label{thm:shifted-symplectic-complementarity}
chapters/theory/higher_genus_complementarity.tex:2260:\label{prop:ptvv-lagrangian}
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:1368:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/cobar_construction.tex:1314:\label{thm:verdier-bar-cobar}
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:687:\label{prop:standard-examples-modular-koszul}
chapters/theory/higher_genus_modular_koszul.tex:3770:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:31649:\label{thm:ambient-d-squared-zero}
chapters/theory/bar_construction.tex:1473:\label{prop:model-independence}
chapters/theory/chiral_koszul_pairs.tex:4667:\label{thm:chiral-koszul-duality}
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
chapters/theory/higher_genus_foundations.tex:2062:\label{thm:cobar-resolution-scoped}
chapters/theory/higher_genus_foundations.tex:4589:\label{thm:obstruction-quantum}
chapters/theory/introduction.tex:2580:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
chapters/theory/introduction.tex.bak:1860:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{prop:gauss-manin-uncurving-chain\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
rectification_20260412_233715/R03_higher_genus_foundations.md:867:   345	\label{prop:gauss-manin-uncurving-chain}
chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:514:chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:518:chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:610:   345	\label{prop:gauss-manin-uncurving-chain}
platonic_rectification_20260413_114523/P03_thm_C0_curved_upgrade.md:521:345:\label{prop:gauss-manin-uncurving-chain}
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:616:   345	\label{prop:gauss-manin-uncurving-chain}
relaunch_wave2_empties/F15_hidden_imports_hg_comp.md:560:   345	\label{prop:gauss-manin-uncurving-chain}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '320,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   320	$d$ for the genus-$0$ bar differential are using $\dzero$.
   321	\end{convention}
   322	
   323	\begin{remark}[Curvature as infinitesimal monodromy: the chiral Riemann--Hilbert correspondence]
   324	\label{rem:curvature-riemann-hilbert}
   325	\index{Riemann--Hilbert correspondence!chiral|textbf}
   326	\index{curvature!as infinitesimal monodromy}
   327	The genus-$g$ propagator $\eta_{ij}^{(g)}=d\log E(z_i,z_j)+\cdots$
   328	acquires monodromy $2\pi i$ around $B$-cycles; the Arakelov
   329	normalization transfers this into the Arnold defect, giving
   330	$\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$.
   331	Thus $\kappa(\cA)$ is the infinitesimal monodromy of the logarithmic
   332	propagator. The corrected differential $\Dg{g}$ absorbs the curvature
   333	into quantum corrections, restoring $\Dg{g}^{\,2}=0$; this is the chiral
   334	analogue of the Riemann--Hilbert correspondence ($\dfib$ is the curved
   335	connection, $\Dg{g}$ the flat one).
   336	The three differentials $\dzero$, $\dfib$, $\Dg{g}$ correspond to:
   337	genus-$0$ (single-valued), genus-$g$ with monodromy (curved),
   338	and the full logarithm on the universal cover (flat).
   339	See Volume~II, Remark~\ref*{rem:three-models} for the full
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{lem:perfectness-criterion\\}\" -n chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
290:\label{lem:perfectness-criterion}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '250,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   250	 \textup{(}anti-symmetric under $\sigma$\textup{)}, then $V^+$ and
   251	 $V^-$ are isotropic for $\langle -,- \rangle$; if the pairing is
   252	 non-degenerate, they are Lagrangian.
   253	\end{enumerate}
   254	\end{lemma}
   255	
   256	\begin{proof}
   257	The projectors $p^\pm := \tfrac{1}{2}(\mathrm{id} \pm \sigma)$
   258	are cochain maps with $p^+ + p^- = \mathrm{id}$,
   259	$(p^\pm)^2 = p^\pm$, and $p^+ \circ p^- = 0$.
   260	Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
   261	\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
   262	and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
   263	via the standard cone identification.
   264	Part~(b) follows by applying $H^*$ to~(a).
   265	Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
   266	so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
   267	= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
   268	Maximality is immediate from the direct-sum decomposition.
   269	\end{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:cobar-resolution-scoped\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rectification_20260412_233715/R03_higher_genus_foundations.md:1568:  2048	\label{thm:cobar-resolution-scoped}
chapters/theory/higher_genus_foundations.tex:2062:\label{thm:cobar-resolution-scoped}
wave2_audit_20260413_001942/F09_prerequisites_thm_H.md:932:  2039	\label{thm:cobar-resolution-scoped}
audit_campaign_20260412_231034/T03_thm_C0.md:1778:  2048	\label{thm:cobar-resolution-scoped}
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:988:  2039	\label{thm:cobar-resolution-scoped}
relaunch_wave2_empties/F15_hidden_imports_hg_comp.md:601:  2062	\label{thm:cobar-resolution-scoped}
platonic_rectification_20260413_114523/P03_thm_C0_curved_upgrade.md:1491:chapters/theory/higher_genus_foundations.tex:2039:\label{thm:cobar-resolution-scoped}
platonic_rectification_20260413_114523/P03_thm_C0_curved_upgrade.md:1702:\label{thm:cobar-resolution-scoped}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2000,2105p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2000	\emph{Step 3: Koszul hypothesis gives $\mathrm{gr}$ convergence.}
  2001	Since $\mathrm{gr}\,\mathcal{A}$ is Koszul, Theorem~\ref{thm:bar-cobar-inversion-qi} gives:
  2002	\[\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathrm{gr}\,\mathcal{A}))
  2003	\xrightarrow{\sim} \mathrm{gr}\,\mathcal{A}\]
  2004	The spectral sequence collapses at $E_2$ for $\mathrm{gr}\,\mathcal{A}$, and
  2005	each cohomology class of $\bar{B}(\mathrm{gr}\,\mathcal{A})$ has a unique harmonic
  2006	representative.
  2007	
  2008	\emph{Step 4: Filtered quasi-isomorphism.}
  2009	The filtration spectral sequence for $\bar{B}(\mathcal{A})$ has:
  2010	\[E_1^{p,q} = H^q(\mathrm{gr}_p\,\bar{B}(\mathcal{A})) =
  2011	H^q(\bar{B}(\mathrm{gr}\,\mathcal{A})_p) \Longrightarrow
  2012	H^{p+q}(\bar{B}(\mathcal{A}))\]
  2013	Since $E_1 = H^*(\bar{B}(\mathrm{gr}\,\mathcal{A}))$ and the spectral sequence for
  2014	$\mathrm{gr}\,\mathcal{A}$ collapses at $E_2$, this spectral sequence also collapses
  2015	at $E_2$. Boardman's Comparison Theorem \cite{Boardman-conditional}
  2016	requires completeness ($\cA = \varprojlim \cA/F_k$, $\bigcap F_k = 0$)
  2017	and exhaustiveness ($\bigcup F_k = \cA$), both of which hold by
  2018	hypothesis. The convergence of the $\mathrm{gr}$ spectral sequence
  2019	therefore implies convergence of the filtered one, and the cobar-bar
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:obstruction-quantum\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rectification_20260412_233715/R03_higher_genus_foundations.md:635:chapters/theory/higher_genus_foundations.tex:4575:\label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:636:chapters/theory/higher_genus_foundations.tex:4575:\label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:965:  4575	\label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:2317: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:2529: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:2749: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:3045: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:3287: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:3529: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:3719:  4569	\label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:3771: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:4034: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:4278: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:4525: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:4822: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:5068: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:5333: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:5589: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:5843: \label{thm:obstruction-quantum}
rectification_20260412_233715/R03_higher_genus_foundations.md:6108: \label{thm:obstruction-quantum}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4540,4605p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4540	descriptions of tautological generators and low-genus cohomology structure for
  4541	$\overline{\mathcal{M}}_{g,n}$ are classical in the moduli-space literature;
  4542	see~\cite{Mumford83}.
  4543	\end{remark}
  4544	
  4545	\begin{definition}[Hodge bundle]
  4546	\label{def:hodge-bundle}
  4547	\index{Hodge bundle|textbf}
  4548	The \emph{Hodge bundle} $\mathbb{E} \to \overline{\mathcal{M}}_{g,n}$ is the rank-$g$ vector bundle whose fiber over $[(\Sigma_g; p_1, \ldots, p_n)]$ is:
  4549	\begin{equation}
  4550	\mathbb{E}_{[\Sigma_g]} = H^0(\Sigma_g, \Omega^1_{\Sigma_g})
  4551	\end{equation}
  4552	the space of holomorphic differentials.
  4553	
  4554	The Chern classes:
  4555	\begin{equation}
  4556	\lambda_i = c_i(\mathbb{E}) \in H^{2i}(\overline{\mathcal{M}}_{g,n}, \mathbb{Q})
  4557	\end{equation}
  4558	are the \emph{$\lambda$-classes}. (The \emph{Mumford--Morita--Miller classes} $\kappa_i = \pi_*(\psi_{n+1}^{i+1}) \in H^{2i}(\overline{\mathcal{M}}_{g,n})$ are related but distinct: they are pushforwards of powers of the universal cotangent class.)
  4559	\end{definition}

thinking
**Preparing to extract proof references**

I’m focusing on identifying all label references inside the C1 proof section, which spans roughly lines 600 to 1870. Since there are a lot of `\ref{}` commands throughout the file, I plan to narrow down to this range and consider scripting a Python tool to parse and list unique references within the proof block for clarity. This should help map the direct citations used in the C1 proof steps.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python - <<'PY'
import re
text=open('chapters/theory/higher_genus_complementarity.tex').read().splitlines()
pattern=re.compile(r\"\\\\ref\\{(["'^}]+)'"\\}\")
for i,line in enumerate(text,1):
    if 600 <= i <= 1870:
        for match in pattern.finditer(line):
            print(i, match.group(1))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re
text=open('chapters/theory/higher_genus_complementarity.tex').read().splitlines()
pattern=re.compile(r\"\\\\ref\\{(["'^}]+)'"\\}\")
for i,line in enumerate(text,1):
    if 600 <= i <= 1870:
        for match in pattern.finditer(line):
            print(i, match.group(1))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
603 lem:genus-filtration
605 thm:verdier-duality-config-complete
607 thm:kodaira-spencer-chiral-complete
621 thm:ambient-d-squared-zero
624 thm:mc2-bar-intrinsic
631 conv:proof-architecture
640 lem:involution-splitting
643 prop:model-independence
661 prop:ptvv-lagrangian
670 thm:quantum-complementarity-main
675 thm:ambient-complementarity-fmp
676 prop:ptvv-lagrangian
695 prop:ptvv-lagrangian
775 lem:genus-filtration
776 def:geometric-bar
840 thm:ss-quantum
871 thm:arnold-three
905 thm:ss-quantum
930 lem:fiber-cohomology-center
945 thm:conilpotency-bar
codex
The C1 surface already shows a structural risk: the theorem is declared proved at line `524`, but its front proof block ends at line `610` and the deferred proof closes at line `1870`. I’m now checking whether every clause of the theorem statement is actually discharged in that deferred chain or only advertised and proved later in separate propositions.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1320,1565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2145,2325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '220,430p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(thm:e1-module-koszul-duality|lem:verdier-extension-exchange|thm:geometric-equals-operadic-bar|thm:bar-concentration|thm:arnold-three|thm:conilpotency-bar|thm:config-space-bv|thm:bv-functor|prop:modular-deformation-truncation|thm:modular-homotopy-convolution|thm:lagrangian-complementarity)\\}\" chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2040,2125p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4560,4635p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   220	$\kappa(\cA) = 0$ (flatness) & $\kappa_{\mathrm{eff}} = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$ \\
   221	Coderived category & Off-shell (curved background) \\
   222	Obstruction class $\mathrm{obs}_g$ & One-loop determinant on $\Sigma_g$ \\
   223	Complementarity $Q_g + Q_g' = H^*$ & Matter--ghost pairing
   224	\end{tabular}
   225	\end{center}
   226	These are theorems (Theorem~\ref{thm:brst-bar-genus0}), not analogies.
   227	\end{remark}
   228	
   229	\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
   230	\index{bar differential!higher-genus notation|textbf}
   231	The Feynman transform differential
   232	$d_{\mathrm{FT}} = d_{\mathrm{tree}} + d_{\mathrm{loop}}$
   233	\textup{(}Proposition~\textup{\ref{prop:loop-filtration-compatible})} is
   234	the single canonical differential on the genus-$g$ bar complex. For
   235	computational purposes, three projections of this differential are
   236	used throughout the manuscript.
   237	\begin{enumerate}
   238	\item[\textup{(i)}] \textbf{Fiberwise curved differential} $\dfib$.
   239	 On a fixed curve $\Sigma_g$, the collision-residue differential built
 succeeded in 51ms:
  2145	
  2146	\begin{proof}
  2147	\emph{Part (i).}
  2148	The BV bracket $\{-,-\}_{\mathrm{BV}}$ on $\barB^{\mathrm{ch}}(\cA)$
  2149	has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
  2150	Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
  2151	associated bivector field on the formal moduli problem has degree~$-1$.
  2152	Theorem~\ref{thm:config-space-bv} identifies this bracket with the
  2153	configuration-space residue pairing. Theorem~\ref{thm:bv-functor}
  2154	supplies a bracket-compatible Verdier comparison, and
  2155	Theorem~\ref{thm:verdier-bar-cobar} identifies that comparison with
  2156	\[
  2157	\mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))
  2158	\xrightarrow{\;\sim\;}
  2159	\cA^!_\infty
  2160	\]
  2161	on the Koszul locus. By the compatibility clause in
  2162	Theorem~\ref{thm:bv-functor}, the adjoint map
  2163	$x \mapsto \{x,-\}_{\mathrm{BV}}$ is exactly this Verdier comparison,
  2164	shifted by~$[1]$. Since the comparison is a quasi-isomorphism, the
 succeeded in 52ms:
  1320	\begin{equation}
  1321	(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
  1322	\end{equation}
  1323	
  1324	But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
  1325	\begin{equation}
  1326	\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
  1327	\mathcal{A}^!)))^\vee
  1328	\end{equation}
  1329	\end{proof}
  1330	
  1331	\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
  1332	\label{cor:quantum-dual-complete}
  1333	For each genus $g \geq 1$ and every Koszul dual chiral pair
  1334	$(\mathcal{A}, \mathcal{A}^!)$:
  1335	\begin{equation}
  1336	Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
  1337	\end{equation}
  1338	with respect to the Verdier pairing. At genus $0$, the
  1339	cohomological-shadow eigenspaces are instead
 succeeded in 51ms:
chapters/connections/outlook.tex:666:\phantomsection\label{thm:lagrangian-complementarity}
chapters/connections/bv_brst.tex:1307:\label{thm:config-space-bv}
chapters/connections/bv_brst.tex:1363:\label{thm:bv-functor}
chapters/theory/higher_genus_modular_koszul.tex:10934:\label{thm:modular-homotopy-convolution}
chapters/theory/chiral_koszul_pairs.tex:1132:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:5705:\label{thm:e1-module-koszul-duality}
chapters/theory/chiral_hochschild_koszul.tex:2060:\label{prop:modular-deformation-truncation}
chapters/theory/cobar_construction.tex:354:\label{lem:verdier-extension-exchange}
chapters/theory/bar_construction.tex:1189:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-three}
chapters/theory/bar_construction.tex:2065:\label{thm:geometric-equals-operadic-bar}
chapters/theory/bar_cobar_adjunction_curved.tex:581:\label{thm:conilpotency-bar}
chapters/connections/concordance.tex:5062:C1 \ClaimStatusProvedHere, C2 \ClaimStatusConditional]\label{thm:lagrangian-complementarity}
 succeeded in 51ms:
  2040	= (\mathrm{gr}\,\cA)^!$.
  2041	Completeness of $\cA^!$ follows from completeness of
  2042	$\bar{B}(\cA)$ (Positselski~\cite[\S A.1]{Positselski11}).
  2043	This proves (4).
  2044	\end{proof}
  2045	
  2046	\begin{example}[W-algebras are filtered]
  2047	The $W_N$ algebra has filtration by conformal weight:
  2048	\[F_k = \mathrm{span}\{W^{(s)} : s \leq k\}\]
  2049	
  2050	This filtration satisfies the hypotheses of Theorem~\ref{thm:convergence-filtered}: it is complete and separated (conformal weight is bounded below), compatible with chiral operations ($\mu(F_i \otimes F_j) \subset F_{i+j}$), and has associated graded $\mathrm{gr}\,W_N \cong$ free field algebra (Koszul by Theorem~\ref{thm:chiral-koszul-duality}).
  2051	\end{example}
  2052	
  2053	% ================================================================
  2054	% SECTION 4.7: THE COBAR RESOLUTION
  2055	% ================================================================
  2056	
  2057	\subsection{The cobar resolution and Ext groups}
  2058	
  2059	\subsubsection{Resolution at chain level}
 succeeded in 51ms:
  4560	
  4561	\begin{theorem}[Faber--Pandharipande $\lambda_g$ formula {\cite{FP03}}; \ClaimStatusProvedElsewhere]
  4562	\label{thm:mumford-formula}
  4563	\index{Faber--Pandharipande formula}
  4564	The top $\lambda$-class, paired with the appropriate $\psi$-class, evaluates to \textup{(LOCAL)}:
  4565	\begin{equation}\label{eq:faber-pandharipande}
  4566	\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
  4567	\end{equation}
  4568	where $B_{2g}$ are Bernoulli numbers~\cite{FP03}. The integrand has degree $(2g-2)+g = 3g-2 = \dim\overline{\mathcal{M}}_{g,1}$. At $g = 1$: $\frac{1}{2} \cdot \frac{1/6}{2} = \frac{1}{24}$; at $g = 2$: $\frac{7}{8} \cdot \frac{1/30}{24} = \frac{7}{5760}$ \textup{(LOCAL)}.
  4569	\end{theorem}
  4570	
  4571	\begin{remark}[Imported-proof dependency tags]
  4572	\emph{Dependency tags.}
  4573	\begin{enumerate}[label=(D\arabic*)]
  4574	\item The class-theoretic setup is provided by
  4575	Theorem~\ref{thm:mmm-classes} and Definition~\ref{def:hodge-bundle}.
  4576	\item The closed-form Bernoulli expression is imported from the external
  4577	tautological-ring literature (see~\cite{Mumford83}).
  4578	\item In this manuscript, the formula is used as input to obstruction and
  4579	quantum-correction bookkeeping (e.g. Theorem~\ref{thm:obstruction-general}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shifted-symplectic" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
189:boundaries meet in a shifted-symplectic ambient space at
507:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
508:conditional bar-side BV / shifted-symplectic upgrade.
1996:\label{sec:shifted-symplectic-complementarity}
2002:proved shifted-symplectic statement on the ambient complex~$C_g$. The
2083:\label{thm:shifted-symplectic-complementarity}
2224:A multi-weight upgrade of Theorem~\ref{thm:shifted-symplectic-complementarity}
2247:Theorem~\ref{thm:shifted-symplectic-complementarity} is a genus-$g$
2325:Conditional on Theorem~\ref{thm:shifted-symplectic-complementarity},
5495:shifted-symplectic phase space in the sense of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1970,2350p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1970	= \langle \mathbb{D}v, \mathbb{D}w \rangle_{\mathbb{D}}
  1971	= -\langle v, w \rangle_{\mathbb{D}}$,
  1972	where the last step uses the anti-commutativity property.
  1973	
  1974	\emph{Part (iii).}
  1975	For $v, w \in V^+$ (eigenvalue $+1$):
  1976	$\langle v, w \rangle_{\mathbb{D}}
  1977	= \langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
  1978	= -\langle v, w \rangle_{\mathbb{D}}$,
  1979	so $\langle v, w \rangle_{\mathbb{D}} = 0$. The same argument
  1980	applies to $V^-$. Since $V = V^+ \oplus V^-$ and the pairing is
  1981	non-degenerate on $V$, the subspaces $V^+$ and $V^-$ are maximal
  1982	isotropic, i.e., Lagrangian.
  1983	\end{proof}
  1984	
  1985	\begin{remark}[Lagrangian interpretation of complementarity]\label{rem:lagrangian-complementarity}
  1986	\index{Lagrangian!complementarity}
  1987	The decomposition of
  1988	Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
  1989	polarization: $Q_g(\cA)$ and $Q_g(\cA^!)$ are complementary

thinking
**Exploring quantum proofs**

I find myself wondering if I need more proof regarding quantum obstruction. It seems like there could be some theorems that might help in identifying H^0 through a center local system. I think it would be beneficial to inspect this further and gather more understanding. There's a complexity to this topic that piques my curiosity, and I want to make sure I'm on the right track. Let’s dig deeper!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4635,4725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4640,4705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '320,390p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5680,5735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1290,1335p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '520,715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4640	\begin{align*}
  4641	d_!^2(\phi_i^*) &= d_!\left(-\sum_{j,k,m} C_{ij}^{k,m} \phi_j^* \boxtimes \phi_k^*\right) \\
  4642	&= -\sum_{j,k,m} C_{ij}^{k,m} [d_!(\phi_j^*) \boxtimes \phi_k^* + \phi_j^* \boxtimes d_!(\phi_k^*)] \\
  4643	&= -\sum_{j,k,m} C_{ij}^{k,m} \left[\left(-\sum_{\ell,p} C_{j\ell}^{p,n} \phi_\ell^* \boxtimes \phi_p^*\right) \boxtimes \phi_k^* + \phi_j^* \boxtimes \left(-\sum_{q,r} C_{kq}^{r,s} \phi_q^* \boxtimes \phi_r^*\right)\right] \\
  4644	&= \sum_{j,k,\ell,m,n,p} C_{ij}^{k,m} C_{j\ell}^{p,n} \,(\phi_\ell^* \boxtimes \phi_p^* \boxtimes \phi_k^*) + \sum_{j,k,q,m,r,s} C_{ij}^{k,m} C_{kq}^{r,s} \,(\phi_j^* \boxtimes \phi_q^* \boxtimes \phi_r^*)
  4645	\end{align*}
  4646	
  4647	For this to vanish, the coefficient of each $\phi_\alpha^* \boxtimes \phi_\beta^* \boxtimes \phi_\gamma^*$ must be zero:
  4648	\[\sum_{j,m,n} C_{ij}^{\gamma,m} C_{j\alpha}^{\beta,n} + \sum_{k,m,s} C_{i\alpha}^{k,m} C_{k\beta}^{\gamma,s} = 0 \qquad \forall\, i, \alpha, \beta, \gamma\]
  4649	
  4650	But this is \emph{precisely the associativity constraint} for the chiral product in $\mathcal{A}_2$: the second sum encodes $(\phi_i \cdot \phi_\alpha) \cdot \phi_\beta$ evaluated at $\phi_\gamma$, while the first sum encodes the rearrangement through $\phi_i \cdot (\phi_\alpha \cdot \phi_\beta)$.
  4651	
  4652	Geometrically: $d_!^2 = 0$ encodes $\partial^2 = 0$ in configuration space; boundaries of boundaries vanish (Arnold--Orlik--Solomon relations).
  4653	\end{proof}
  4654	
  4655	\begin{remark}
  4656	Theorem~\ref{thm:coalgebra-axioms-verified} exhibits the characteristic feature of Koszul duality: associativity of the algebra $\mathcal{A}_2$ is equivalent to nilpotence of the coalgebra differential $d_!$. Algebraic structure on one side translates to cohomological structure on the dual side.
  4657	\end{remark}
  4658	
  4659	%----------------------------------------------------------------
 succeeded in 52ms:
  4635	\begin{proof}
  4636	By Proposition~\ref{prop:gauss-manin-uncurving-chain} and
  4637	Convention~\ref{conv:higher-genus-differentials}, the corrected
  4638	differential satisfies $\Dg{g}^{\,2} = 0$, so
  4639	$\bar{B}^{(g)}_{\mathrm{flat}}(\mathcal{A})$ is an honest cochain
  4640	complex of sheaves on $\overline{\mathcal{M}}_g$.
  4641	Its endomorphism sheaf
  4642	$\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})$
  4643	is therefore also a strict complex, and ordinary hypercohomology
  4644	applies on the flat side.
  4645	
  4646	On the Koszul locus, Theorem~\ref{thm:cobar-resolution-scoped}
  4647	identifies the strict bar complex as a bar resolution of
  4648	$\mathcal{A}$. Hence
  4649	$\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})$
  4650	computes the derived endomorphism complex of~$\mathcal{A}$, and
  4651	its degree-$0$ cocycles are precisely the endomorphisms commuting
  4652	with the chiral product. Their sheaf is the center local system
  4653	$\mathcal{Z}(\mathcal{A})
  4654	= \mathcal{H}^0(\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A}))$.
 succeeded in 51ms:
  5680	\subsection{The fundamental theorem for chiral Koszul pairs}
  5681	
  5682	\begin{remark}[General chiral module-category duality remains frontier]
  5683	\label{rem:module-category-frontier}
  5684	The broad ordinary-derived package for a general
  5685	chiral Koszul pair $(\cA_1,\cA_2)$
  5686	\textup{(}derived equivalence, Ext exchange with derived Hom on the
  5687	bar-comodule side and finite-type Tor reformulations, simple/projective
  5688	transport, and Hochschild transport\textup{)}
  5689	is \emph{not} proved on this general surface. The earlier bar-cobar
  5690	machinery in Part~\ref{part:bar-complex} gives the intrinsic bar-coalgebra comparison, and
  5691	the manuscript's proved ordinary module-level statement is the later
  5692	$\Eone$ theorem
  5693	Theorem~\ref{thm:e1-module-koszul-duality}, restricted to the
  5694	quadratic genus-$0$ complete/conilpotent lane.
  5695	
  5696	Any extension of that package to arbitrary chiral Koszul pairs would
  5697	require extra hypotheses and a module-level comparison theorem beyond
  5698	what is currently established here.
  5699	\end{remark}
 succeeded in 51ms:
   320	\cite[Theorem~3.2.3]{HTT08}.
   321	
   322	\emph{Step~3: Logarithmic extension.}
   323	The bar sheaf on the open configuration space $C_n(X)$ is
   324	$j^*\pi^!\cA^{\boxtimes n} \otimes \Omega^*_{\log}(D)$,
   325	where $j \colon C_n(X) \hookrightarrow \overline{C}_n(X)$ is the
   326	inclusion and $D = \overline{C}_n(X) \setminus C_n(X)$ is a normal
   327	crossings divisor (Theorem~\ref{thm:FM}).
   328	The logarithmic differential forms $\Omega^*_{\log}(D)$ define a
   329	regular integrable connection on the NCD complement, so
   330	$j_*$ of the resulting regular holonomic module on~$C_n(X)$ is
   331	regular holonomic on~$\overline{C}_n(X)$ by Deligne's regularity
   332	theorem \cite[Theorem~5.2.17]{HTT08}.
   333	This identifies $\bar{B}^{\mathrm{ch}}_n(\cA)$ as a regular
   334	holonomic $\mathcal{D}_{\overline{C}_n(X)}$-module.
   335	
   336	\emph{Step~4: Bar differential.}
   337	The bar differential $d_{\mathrm{bar}} = d_{\mathrm{internal}}
   338	+ d_{\mathrm{residue}} + d_{\mathrm{form}}$
   339	(Definition~\ref{def:bar-differential-complete}).
 succeeded in 51ms:
  1290	\end{example}
  1291	
  1292	\begin{remark}[CFT vertex operators from cobar]\label{rem:vertex-operators-cobar}
  1293	In conformal field theory, vertex operators $V_\alpha(z)$ create states $|\alpha\rangle$ 
  1294	at position $z$. These correspond to cobar elements:
  1295	\[V_\alpha \leftrightarrow K_\alpha \in \Omega^1(\mathcal{C})\]
  1296	
  1297	The OPE of vertex operators:
  1298	\[V_\alpha(z) V_\beta(w) \sim \sum_\gamma \frac{C_{\alpha\beta}^\gamma}{(z-w)^{h_\gamma - h_\alpha - h_\beta}} V_\gamma(w)\]
  1299	
  1300	corresponds to the cobar product:
  1301	\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]
  1302	
  1303	The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
  1304	structure constants.
  1305	
  1306	The cobar construction thus provides a geometric derivation
  1307	of the OPE algebra in CFT.
  1308	\end{remark}
  1309	
 succeeded in 51ms:
   520	$Q_g(\cA^!) := H^*(\mathbf{Q}_g(\cA^!))$ recover the
   521	deformation and obstruction spaces of
   522	Theorem~\ref{thm:quantum-complementarity-main}.
   523	\end{definition}
   524	
   525	\begin{remark}[Model independence]\label{rem:model-independence}
   526	Any two admissible dg presentations of the same factorization
   527	object are connected by a contractible space of quasi-isomorphisms,
   528	so the homotopy axioms \ref{MK:koszul-htpy}--\ref{MK:modular-htpy}
   529	are invariants of the factorization algebra, not of a
   530	chosen model. Definition~\ref{def:modular-koszul-chiral} provides
   531	the dg model used throughout.
   532	\end{remark}
   533	
   534	\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
   535	 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
   536	Let $X$ be a smooth projective curve over $\mathbb{C}$.
   537	A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
   538	algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
   539	the following data and satisfying the following axioms.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{subsec:genus2-complementarity-verification\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/genus_expansions.tex:1676:\subsection{Genus-2 complementarity verification}\label{subsec:genus2-complementarity-verification}
main.tex:1580: \phantomsection\label{subsec:genus2-complementarity-verification}% % genus_expansions.tex
healing_20260413_132214/H11_SC_formal_alt.md:13133:\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:24299:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:35463:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:46628:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:57793:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:68956:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:80119:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:91257:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:102440:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:113613:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:124807:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:136014:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:147207:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:158383:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:169560:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:180742:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:191844:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
healing_20260413_132214/H11_SC_formal_alt.md:203580:-\newlabel{subsec:genus2-complementarity-verification}{{K.7.1}{2704}{Practical recommendations}{section*.232}{}}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{part:characteristic-datum\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
wave2_audit_20260413_001942/D15_hardcoded_parts.md:311:/Users/raeez/chiral-bar-cobar/main.tex:1073:\label{part:characteristic-datum}
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1360:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1363:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
audit_campaign_20260412_231034/XV12_part_refs.md:320:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
audit_campaign_20260412_231034/XV12_part_refs.md:322:/Users/raeez/chiral-bar-cobar/main.tex:1045:\label{part:characteristic-datum}
main.tex:1073:\label{part:characteristic-datum}
wave2_audit_20260413_001942/U13_dead_labels.md:279:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:954:./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:955:./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:956:./wave2_audit_20260413_001942/D15_hardcoded_parts.md:311:/Users/raeez/chiral-bar-cobar/main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:957:./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1360:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:958:./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1363:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:959:./wave2_audit_20260413_001942/F04_definitions_complementarity.md:1089:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:960:./wave2_audit_20260413_001942/U13_dead_labels.md:279:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:961:./wave2_audit_20260413_001942/C19_chiral_hochschild_koszul.md:1033:main.tex:1073:\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:962:./audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:963:./main.tex:1073:\label{part:characteristic-datum}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{app:signs\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1235:/bin/zsh -lc "rg -n -F '\\label{app:signs}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1238:./appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:682:appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:745:appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2044:appendices/signs_and_shifts.tex:2:\label{app:signs}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:968:./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
appendices/signs_and_shifts.tex:2:\label{app:signs}
healing_20260413_132214/H11_SC_formal_alt.md:12478:\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:23644:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:34808:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:45973:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:57138:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:68301:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:79464:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:90602:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:101785:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:112958:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:124152:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:135359:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{app:sign-conventions\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:683:appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:746:appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2045:appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:968:./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H11_SC_formal_alt.md:12594:\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:23760:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:34924:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:46089:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:57254:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:68417:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:79580:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:90718:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:101901:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:113074:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:124268:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:135475:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:146668:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
healing_20260413_132214/H11_SC_formal_alt.md:157844:-\newlabel{app:sign-conventions}{{G.7}{2637}{Dictionary of sign conventions}{section.G.7}{}}
codex
The dependency graph is now populated. I’m checking three kinds of failure in order: circular imports back into Theorem C, stronger hypotheses silently imported from other chapters, and proof clauses that are declared proved here but only become true after later propositions or conditionals.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1288,1395p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:quantum-complementarity-main|thm:fiber-center-identification|thm:shifted-symplectic-complementarity|lem:perfectness-criterion|thm:kodaira-spencer-chiral-complete|prop:lagrangian-eigenspaces|prop:ptvv-lagrangian" chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:quantum-complementarity-main|lem:involution-splitting|lem:perfectness-criterion|thm:fiber-center-identification|thm:shifted-symplectic-complementarity" master_claim_ledger_filtered.csv suspicious_proved_claim_dependencies.csv label_status_conflicts.csv 2>/dev/null' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"theorematic|\\\\S\\\\ref\\{lem:genus-filtration\\}|Step~I|Step~II|Step~III|q = 0 row|j_"'!|j_'"\\*|Picard--Lefschetz|Riemann--Roch\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1288	\item \emph{Second-order}: $\Delta$ is a second-order operator, meaning the
  1289	 \emph{BV bracket}
  1290	 \[
  1291	 \{a, b\} := (-1)^{|a|}\bigl[\Delta(ab) - \Delta(a)\,b
  1292	 - (-1)^{|a|} a\,\Delta(b)\bigr]
  1293	 \]
  1294	 (the failure of $\Delta$ to be a graded derivation) satisfies the
  1295	 graded Leibniz rule in each slot:
  1296	 \begin{gather*}
  1297	 \{a, bc\} = \{a, b\}\,c + (-1)^{(|a|+1)|b|} b\,\{a, c\},\\
  1298	 \{a, b\} = -(-1)^{(|a|+1)(|b|+1)}\{b, a\}.
  1299	 \end{gather*}
  1300	\end{enumerate}
  1301	The bracket automatically satisfies the graded Jacobi identity.
  1302	\end{definition}
  1303	
  1304	\subsection{BV structure from configuration spaces}
  1305	
  1306	\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
  1307	\label{thm:config-space-bv}
exec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
text=pathlib.Path('chapters/theory/higher_genus_complementarity.tex').read_text()
# collect refs in C0 proof block 430-498 etc and theorem proof blocks 600-610 + 1363-2200
lines=text.splitlines()
regions=[(430,498),(600,610),(761,2200)]
refs=[]
for a,b in regions:
    for i in range(a-1,b):
        for m in re.finditer(r'\\\\ref\\{(["'^}]+)'"\\}', lines[i]):
            refs.append((i+1,m.group(1)))
for item in refs:
    print(f\"{item[0]}:{item[1]}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/theorem_registry.md:726:| `lem:perfectness-criterion` | `lemma` | 290 | Perfectness criterion for the strict flat relative bar family |
metadata/theorem_registry.md:727:| `thm:fiber-center-identification` | `theorem` | 373 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
metadata/theorem_registry.md:728:| `thm:quantum-complementarity-main` | `theorem` | 525 | Quantum complementarity as Lagrangian polarization |
metadata/theorem_registry.md:738:| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1368 | Kodaira--Spencer map for chiral algebras |
metadata/theorem_registry.md:745:| `prop:lagrangian-eigenspaces` | `proposition` | 1914 | Verdier pairing and Lagrangian eigenspaces |
metadata/theorem_registry.md:747:| `prop:ptvv-lagrangian` | `proposition` | 2260 | PTVV Lagrangian embedding |
chapters/connections/concordance.tex:50: \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
chapters/connections/concordance.tex:54: \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
chapters/connections/concordance.tex:57: \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
chapters/connections/concordance.tex:203: (Theorem~\ref{thm:quantum-complementarity-main}).
chapters/connections/concordance.tex:337: (Theorem~\ref{thm:quantum-complementarity-main}).}
chapters/connections/concordance.tex:341: \textup{(}Theorem~\ref{thm:fiber-center-identification}\textup{)}.
chapters/connections/concordance.tex:345: \textup{(}Theorem~\ref{thm:quantum-complementarity-main}\textup{)}.
chapters/connections/concordance.tex:348: \textup{(}Theorem~\ref{thm:shifted-symplectic-complementarity}\textup{)}.
chapters/connections/concordance.tex:351: \textup{(}Theorem~\ref{thm:kodaira-spencer-chiral-complete}\textup{)}.
chapters/connections/concordance.tex:3984:Theorem~\ref{thm:shifted-symplectic-complementarity} and therefore
chapters/connections/concordance.tex:4596: (Theorem~\ref{thm:quantum-complementarity-main}).
chapters/connections/concordance.tex:4807:$C_{\mathrm{mod}}$ & C0 fiber-center identification; C1 duality / & C0/C1: \textbf{Proved}; & Thms~\ref{thm:fiber-center-identification}, \\
chapters/connections/concordance.tex:4808: & Lagrangian complementarity; C2 shifted-symplectic upgrade & C2: \textbf{Conditional} & \ref{thm:quantum-complementarity-main}, \\
chapters/connections/concordance.tex:4809: & on the uniform-weight BV lane & & \ref{thm:shifted-symplectic-complementarity} \\[2pt]
 exited 2 in 51ms:

 succeeded in 51ms:
603:Step~I (\S\ref{lem:genus-filtration}ff.) constructs the spectral
605:Step~II (from Theorem~\ref{thm:verdier-duality-config-complete})
607:Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
746:\item Riemann--Roch theorem for Hodge bundle on $\overline{\mathcal{M}}_g$
897:\emph{Picard--Lefschetz formula}.
934:is quasi-unipotent: the Picard--Lefschetz formula gives
998:from $j_*$-extended bar cochains of~$\mathcal{A}$ (eigenvalue~$+1$) or
999:from $j_!$-extended bar cochains of~$\mathcal{A}^!$ (eigenvalue~$-1$),
1153:This completes Step~I: the genus filtration, the associated spectral
1354:This completes Step~II: Verdier duality on configuration spaces
1459:exchanges $j_*$ and $j_!$ extensions (Lemma~\ref{lem:verdier-extension-exchange}):
1460:$\mathbb{D}(j_* \mathcal{F}) \cong j_!(\mathbb{D}\mathcal{F})$.
1462:The KS class $\kappa(v)$ acts on $H^*(\overline{C}_n(\Sigma_g), j_*\mathcal{A}^{\boxtimes n})$
1634:The key sign is: $j_*$ and $j_!$ differ by a shift of $2\dim(\partial)$ in the
1673:\item The bar complex of $\mathcal{A}$ uses $j_*$-extension.
1675:uses $j_!$-extension.
1676:\item Verdier duality exchanges $j_*$ and $j_!$
1690:$j_!$-extension (compact support), dual to the $j_*$-extension used
1699:through its own spectral sequence but through the $j_! \leftrightarrow j_*$
1701:$j_!$-extended classes to $j_*$-extended classes.
 exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re
labels=set()
for i,line in enumerate(open('chapters/theory/higher_genus_complementarity.tex').read().splitlines(),1):
    if 600 <= i <= 1870:
        for match in re.finditer(r\"\\\\ref\\{(["'^}]+)'"\\}\", line):
            labels.add(match.group(1))
for lbl in sorted(labels):
    print(lbl)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
app:sign-conventions
app:signs
conv:proof-architecture
conv:regime-tags
cor:duality-bar-complexes-complete
cor:quantum-dual-complete
cor:virasoro-quantum-dim
def:chiral-koszul-pair
def:complementarity-complexes
def:geometric-bar
def:koszul-dual-chiral
lem:center-isomorphism
lem:eigenspace-decomposition-complete
lem:exhaustion-complete
lem:fiber-cohomology-center
lem:genus-filtration
lem:involution-splitting
lem:obs-def-split-complete
lem:quantum-from-ss
lem:ss-duality-complete
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    res=subprocess.run([\"rg\",\"-n\",\"\\\\label\\{\"+label+\"\\}\"], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 113ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern=f\"\\\\\\\\label\\{{{label}\\}}\"
    res=subprocess.run([\"rg\",\"-n\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 129ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern = r\"\\\\label\\{\" + label + r\"\\}\"
    res=subprocess.run([\"rg\",\"-n\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 128ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND
thinking
**Verifying mathematical proof**

I’m trying to clarify a fix in a proof regarding bounded coherent complexes and perfectness from a regularity standpoint. I need to ensure that \(\overline{\mathcal M}_g\) is indeed smooth over C and check if the DM stack is stable. I've noted that the smooth Deligne-Mumford stack and its dimension confirm part of it, but it seems there’s a crucial argument missing, which needs addressing. I'll see if this proof gap is manageable despite its importance!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1874,1905p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1874	\begin{remark}[Proof architecture summary for Theorem~C]
  1875	\label{rem:h-level-proof-summary}
  1876	\index{Theorem C!proof architecture summary}
  1877	The distributed proof above establishes both the
  1878	S-level (cohomological) and H-level (homotopy) claims of
  1879	Theorem~\ref{thm:quantum-complementarity-main} via three steps.
  1880	\emph{First}, the Verdier involution~$\sigma$ is a
  1881	\emph{cochain-level} involution on
  1882	$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
  1883	it is induced by the composition of Verdier duality~$\mathbb{D}$
  1884	(an exact functor on $D^b_{\mathrm{hol}}(\mathcal{D})$) with the
  1885	Koszul identification
  1886	$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
  1887	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
  1888	Since~$\sigma$ is induced by exact functors, it commutes with
  1889	differentials at every page of the spectral sequence
  1890	(Lemma~\ref{lem:verdier-involution-moduli}).
  1891	\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
  1892	the cochain-level splitting: the projectors
  1893	$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern = \"\\\\label{\" + label + \"}\"
    res=subprocess.run([\"rg\",\"-n\",\"-F\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 141ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern = \"\\\\\\\\label{\" + label + \"}\"
    res=subprocess.run([\"rg\",\"-n\",\"-F\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 126ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label{app:signs}'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\label{app:signs})
               ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -F '\\\\label{app:signs}'" in /Users/raeez/chiral-bar-cobar succeeded in 80ms:
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1235:/bin/zsh -lc "rg -n -F '\\label{app:signs}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

thinking
**Refining search scope for label patterns**

I’m narrowing down the ripgrep search to only `.tex` files and specific directories to avoid false matches in logs or unrelated files. This way, I can more reliably locate label definitions by targeting directories like `chapters` and `appendices` instead of scanning the entire repo indiscriminately. I'll verify this approach by testing `rg` on a specific label pattern within limited paths.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -F '\\\\label{lem:genus-filtration}' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -F '\\\\label{lem:genus-filtration}' chapters/theory" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && printf '%s\\n' '\\\\label'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\\label
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && printf '%s\\n' '\\label'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'label\\{lem:genus-filtration\\}'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
chapters/theory/higher_genus_complementarity.tex:762:\label{lem:genus-filtration}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern = \"\\\\\\\\label\\\\{\" + label + \"\\\\}\"
    res=subprocess.run([\"rg\",\"-n\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 123ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
label='lem:genus-filtration'
pattern = \"\\\\\\\\label\\\\{\" + label + \"\\\\}\"
print(repr(pattern))
res = __import__('subprocess').run(['rg','-n',pattern], capture_output=True, text=True)
print('returncode', res.returncode)
print('output', res.stdout)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
'\\\\label\\{lem:genus-filtration\\}'
returncode 1
output 
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
label='lem:genus-filtration'
pattern = \"\\\\label{\" + label + \"\\\\}\"
print(repr(pattern))
res = __import__('subprocess').run(['rg','-n',pattern], capture_output=True, text=True)
print('returncode', res.returncode)
print('output', res.stdout)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
'\\label{lem:genus-filtration\\}'
returncode 2
output 
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
label='lem:genus-filtration'
pattern = \"\\\\label\\\\{\" + label + \"\\\\}\"
print(repr(pattern))
res = __import__('subprocess').run(['rg','-n',pattern], capture_output=True, text=True)
print('returncode', res.returncode)
print('output', res.stdout)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
'\\label\\{lem:genus-filtration\\}'
returncode 2
output 
thinking
**Clarifying theorem proof details**

I'm examining the theorem statement and proof, particularly the corollary quantum-dual-complete found later in the file at step II before the proof concludes. The roadmap points to this corollary being at 1331 within Step II, while the proof itself finishes after Step III. I’m wondering if the proof explicitly cites it. Step II establishes a perfect pairing for genus ≥ 1, but doesn't clarify which steps link to each assertion. The corollary mentions a genus-0 exception, raising questions about circular reasoning.
thinking
**Evaluating theorem structure**

I'm considering if the main theorem relies on step II specifically for g ≥ 1 duality, while treating genus 0 separately. This could clarify the situation and avoid any circular reasoning issues. It's interesting how the distinctions are made, and I'm just trying to ensure I understand how each step contributes to the overall framework. It feels like there’s a lot of nuance here to unravel!
thinking
**Exploring theorems and principles**

I’m thinking about the theorem that applies to the genus-0 quadratic regime and how it's noted in lines 1316-1319. There's the C2 theorem that is more general, relating to chiral Koszul pairs across all genera. The bv-functor references verdier-bar-cobar and mentions the Koszul locus A^!∞ ≃ A^! But I'm wondering about the assumptions connected to this generalization. I feel like I need to explore this more deeply!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2025,2088p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2025	 \overline{\mathcal{M}}_{g_1,|S_1|+1} \times
  2026	 \overline{\mathcal{M}}_{g_2,|S_2|+1}$.
  2027	\end{itemize}
  2028	
  2029	The Lie bracket is \emph{graph composition}: for
  2030	$\xi \in \operatorname{CoDer}^{\mathrm{cyc}}(\barB^{(g_1,n_1)}(\cA))$
  2031	and
  2032	$\eta \in \operatorname{CoDer}^{\mathrm{cyc}}(\barB^{(g_2,n_2)}(\cA))$,
  2033	\begin{equation}\label{eq:modular-cyc-graph-bracket}
  2034	[\xi,\eta]
  2035	\;:=\;
  2036	\sum_{\Gamma}\xi \circ_\Gamma \eta,
  2037	\end{equation}
  2038	summed over stable graphs~$\Gamma$ connecting an output of~$\xi$ to an
  2039	input of~$\eta$ with cross-polarization on internal edges.
  2040	\end{definition}
  2041	
  2042	\begin{remark}[Strictification of the modular deformation object]
  2043	\label{rem:modular-cyc-strictification}
  2044	The modular cyclic deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
labels=[
\"app:sign-conventions\",\"app:signs\",\"conv:proof-architecture\",\"conv:regime-tags\",\"cor:duality-bar-complexes-complete\",\"cor:quantum-dual-complete\",\"cor:virasoro-quantum-dim\",
\"def:chiral-koszul-pair\",\"def:complementarity-complexes\",\"def:geometric-bar\",\"def:koszul-dual-chiral\",\"lem:center-isomorphism\",\"lem:eigenspace-decomposition-complete\",
\"lem:exhaustion-complete\",\"lem:fiber-cohomology-center\",\"lem:genus-filtration\",\"lem:involution-splitting\",\"lem:obs-def-split-complete\",\"lem:quantum-from-ss\",\"lem:ss-duality-complete\",
\"lem:trivial-intersection-complete\",\"lem:verdier-extension-exchange\",\"lem:verdier-involution-moduli\",\"part:characteristic-datum\",\"prop:model-independence\",\"prop:ptvv-lagrangian\",\"sec:FM-compactification\",
\"subsec:genus2-complementarity-verification\",\"thm:ambient-complementarity-fmp\",\"thm:ambient-d-squared-zero\",\"thm:arnold-three\",\"thm:bar-concentration\",\"thm:chiral-koszul-duality\",\"thm:conilpotency-bar\",
\"thm:e1-module-koszul-duality\",\"thm:geometric-equals-operadic-bar\",\"thm:kodaira-spencer-chiral-complete\",\"thm:mc2-bar-intrinsic\",\"thm:quantum-complementarity-main\",\"thm:ss-quantum\",\"thm:verdier-bar-cobar\",\"thm:verdier-duality-config-complete\"]
for label in labels:
    pattern = \"label\\\\{\" + label + \"\\\\}\"
    res=subprocess.run([\"rg\",\"-n\",pattern], capture_output=True, text=True)
    if res.returncode"'!=0:
        print(label, "NOT FOUND")
    else:
        first=res.stdout.strip().splitlines()[0]
        print(label, first)
PY' in /Users/raeez/chiral-bar-cobar succeeded in 112ms:
app:sign-conventions NOT FOUND
app:signs NOT FOUND
conv:proof-architecture NOT FOUND
conv:regime-tags NOT FOUND
cor:duality-bar-complexes-complete NOT FOUND
cor:quantum-dual-complete NOT FOUND
cor:virasoro-quantum-dim NOT FOUND
def:chiral-koszul-pair NOT FOUND
def:complementarity-complexes NOT FOUND
def:geometric-bar NOT FOUND
def:koszul-dual-chiral NOT FOUND
lem:center-isomorphism NOT FOUND
lem:eigenspace-decomposition-complete NOT FOUND
lem:exhaustion-complete NOT FOUND
lem:fiber-cohomology-center NOT FOUND
lem:genus-filtration NOT FOUND
lem:involution-splitting NOT FOUND
lem:obs-def-split-complete NOT FOUND
lem:quantum-from-ss NOT FOUND
lem:ss-duality-complete NOT FOUND
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '780,900p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   780	\end{equation}
   781	
   782	When $X$ has genus $g$, the configuration space $\overline{C}_n(X)$ fibers over $X$. 
   783	To stratify by genus, we consider:
   784	\begin{equation}
   785	\mathcal{C}_n := \overline{C}_n(\mathcal{M}_g) \to \overline{\mathcal{M}}_g
   786	\end{equation}
   787	the universal configuration space over the moduli stack.
   788	
   789	The fiber over $[(\Sigma_h; p_1, \ldots, p_n)]$ is $\overline{C}_n(\Sigma_h)$. Thus:
   790	\begin{equation}
   791	\bar{B}^{(h)}(\mathcal{A}) = R\Gamma(\overline{\mathcal{M}}_h, \mathcal{H}^*(\mathcal{
   792	C}_n, \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}))
   793	\end{equation}
   794	
   795	The genus filtration $F^{\leq g}$ consists of contributions from curves of genus 
   796	$\leq g$. This is well-defined because:
   797	\begin{enumerate}
   798	\item The differential $d = \sum_{D} \text{Res}_D$ respects the genus filtration 
   799	(residues at divisors do not change genus)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
label='lem:genus-filtration'
pattern = \"label\\\\{\" + label + \"\\\\}\"
res=subprocess.run(['rg','-n',pattern], capture_output=True, text=True)
print('cmd', ['rg','-n',pattern])
print('stdout', repr(res.stdout))
print('stderr', repr(res.stderr))
print('rc', res.returncode)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
cmd ['rg', '-n', 'label\\{lem:genus-filtration\\}']
stdout ''
stderr ''
rc 1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import subprocess
label='lem:genus-filtration'
pattern=\"label\\\\{\"+label+\"\\\\}\"
cmd=f\"rg -n '{pattern}'\"
res=subprocess.run(cmd, shell=True, capture_output=True, text=True)
print('cmd', cmd)
print('stdout', res.stdout)
print('stderr', res.stderr)
print('rc', res.returncode)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
cmd rg -n 'label\{lem:genus-filtration\}'
stdout 
stderr 
rc 1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'label\\{lem:genus-filtration\\}'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:762:\label{lem:genus-filtration}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && for label in app:sign-conventions app:signs conv:proof-architecture conv:regime-tags cor:duality-bar-complexes-complete cor:quantum-dual-complete cor:virasoro-quantum-dim def:chiral-koszul-pair def:complementarity-complexes def:geometric-bar def:koszul-dual-chiral lem:center-isomorphism lem:eigenspace-decomposition-complete lem:exhaustion-complete lem:fiber-cohomology-center lem:genus-filtration lem:involution-splitting lem:obs-def-split-complete lem:quantum-from-ss lem:ss-duality-complete lem:trivial-intersection-complete lem:verdier-extension-exchange lem:verdier-involution-moduli part:characteristic-datum prop:model-independence prop:ptvv-lagrangian sec:FM-compactification subsec:genus2-complementarity-verification thm:ambient-complementarity-fmp thm:ambient-d-squared-zero thm:arnold-three thm:bar-concentration thm:chiral-koszul-duality thm:conilpotency-bar thm:e1-module-koszul-duality thm:geometric-equals-operadic-bar thm:kodaira-spencer-chiral-complete thm:mc2-bar-intrinsic thm:quantum-complementarity-main thm:ss-quantum thm:verdier-bar-cobar thm:verdier-duality-config-complete; do echo "-- $label --"; rg -n "label'"\\{"'$label'"\\}\"; done" in /Users/raeez/chiral-bar-cobar succeeded in 1.41s:
-- app:signs --
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1235:/bin/zsh -lc "rg -n -F '\\label{app:signs}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1238:./appendices/signs_and_shifts.tex:2:\label{app:signs}
relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:968:./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/F11_hidden_imports_bar.md:1055:app:signs	./appendices/signs_and_shifts.tex:2:\label{app:signs}
wave2_audit_20260413_001942/F11_hidden_imports_bar.md:1133:app:signs	appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:682:appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:745:appendices/signs_and_shifts.tex:2:\label{app:signs}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2044:appendices/signs_and_shifts.tex:2:\label{app:signs}
appendices/signs_and_shifts.tex:2:\label{app:signs}
healing_20260413_132214/H11_SC_formal_alt.md:12478:\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:23644:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:34808:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:45973:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:57138:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:68301:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:79464:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:90602:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}
healing_20260413_132214/H11_SC_formal_alt.md:101785:-\newlabel{app:signs}{{G}{2627}{Sign conventions and shifts}{appendix.G}{}}

thinking
**Filtering label definitions to .tex files**

I'm refining the search to exclude noisy log entries by limiting ripgrep to directories and files ending with `.tex`, focusing on source files rather than markdown or log references. Running a loop per label within these specific folders should produce clearer, manageable output.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && for label in app:sign-conventions app:signs conv:proof-architecture conv:regime-tags cor:duality-bar-complexes-complete cor:quantum-dual-complete cor:virasoro-quantum-dim def:chiral-koszul-pair def:complementarity-complexes def:geometric-bar def:koszul-dual-chiral lem:center-isomorphism lem:eigenspace-decomposition-complete lem:exhaustion-complete lem:fiber-cohomology-center lem:genus-filtration lem:involution-splitting lem:obs-def-split-complete lem:quantum-from-ss lem:ss-duality-complete lem:trivial-intersection-complete lem:verdier-extension-exchange lem:verdier-involution-moduli part:characteristic-datum prop:model-independence prop:ptvv-lagrangian sec:FM-compactification subsec:genus2-complementarity-verification thm:ambient-complementarity-fmp thm:ambient-d-squared-zero thm:arnold-three thm:bar-concentration thm:chiral-koszul-duality thm:conilpotency-bar thm:e1-module-koszul-duality thm:geometric-equals-operadic-bar thm:kodaira-spencer-chiral-complete thm:mc2-bar-intrinsic thm:quantum-complementarity-main thm:ss-quantum thm:verdier-bar-cobar thm:verdier-duality-config-complete; do printf '%s
' \"-- "'$label --"; rg -n "label'"\\\\{"'$label'"\\\\}\" chapters examples connections appendices main.tex; done" in /Users/raeez/chiral-bar-cobar exited 2 in 251ms:
-- lem:genus-filtration --
rg: examples: No such file or directory (os error 2)
rg: connections: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:762:\label{lem:genus-filtration}
-- lem:involution-splitting --
rg: examples: No such file or directory (os error 2)
rg: connections: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:235:\label{lem:involution-splitting}
-- lem:obs-def-split-complete --
rg: examples: No such file or directory (os error 2)
rg: connections: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:1757:\label{lem:obs-def-split-complete}
-- lem:quantum-from-ss --
rg: examples: No such file or directory (os error 2)
rg: connections: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:965:\label{lem:quantum-from-ss}
-- lem:ss-duality-complete --
rg: examples: No such file or directory (os error 2)
rg: connections: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:1278:\label{lem:ss-duality-complete}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && for label in app:sign-conventions app:signs conv:proof-architecture conv:regime-tags cor:duality-bar-complexes-complete cor:quantum-dual-complete cor:virasoro-quantum-dim def:chiral-koszul-pair def:complementarity-complexes def:geometric-bar def:koszul-dual-chiral lem:center-isomorphism lem:eigenspace-decomposition-complete lem:exhaustion-complete lem:fiber-cohomology-center lem:genus-filtration lem:involution-splitting lem:obs-def-split-complete lem:quantum-from-ss lem:ss-duality-complete lem:trivial-intersection-complete lem:verdier-extension-exchange lem:verdier-involution-moduli part:characteristic-datum prop:model-independence prop:ptvv-lagrangian sec:FM-compactification subsec:genus2-complementarity-verification thm:ambient-complementarity-fmp thm:ambient-d-squared-zero thm:arnold-three thm:bar-concentration thm:chiral-koszul-duality thm:conilpotency-bar thm:e1-module-koszul-duality thm:geometric-equals-operadic-bar thm:kodaira-spencer-chiral-complete thm:mc2-bar-intrinsic thm:quantum-complementarity-main thm:ss-quantum thm:verdier-bar-cobar thm:verdier-duality-config-complete; do printf '%s
' \"-- "'$label --"; rg -n "label'"\\\\{"'$label'"\\\\}\" chapters appendices main.tex; done" in /Users/raeez/chiral-bar-cobar succeeded in 248ms:
chapters/theory/higher_genus_complementarity.tex:235:\label{lem:involution-splitting}
-- lem:obs-def-split-complete --
chapters/theory/higher_genus_complementarity.tex:1757:\label{lem:obs-def-split-complete}
-- lem:quantum-from-ss --
chapters/theory/higher_genus_complementarity.tex:965:\label{lem:quantum-from-ss}
-- lem:ss-duality-complete --
chapters/theory/higher_genus_complementarity.tex:1278:\label{lem:ss-duality-complete}
-- lem:trivial-intersection-complete --
chapters/theory/higher_genus_complementarity.tex:1788:\label{lem:trivial-intersection-complete}
-- lem:verdier-extension-exchange --
chapters/theory/cobar_construction.tex:354:\label{lem:verdier-extension-exchange}
-- lem:verdier-involution-moduli --
chapters/theory/higher_genus_complementarity.tex:1557:\label{lem:verdier-involution-moduli}
-- part:characteristic-datum --
main.tex:1073:\label{part:characteristic-datum}
-- prop:model-independence --
chapters/theory/bar_construction.tex:1473:\label{prop:model-independence}
-- prop:ptvv-lagrangian --
chapters/theory/higher_genus_complementarity.tex:2260:\label{prop:ptvv-lagrangian}
-- sec:FM-compactification --
thinking
**Clarifying mathematical concepts**

I’m thinking about a theorem that was only proved for S-level direct sums in 1866, but it seems it didn’t discharge the H-level quasi-isomorphism in the specified pages. It’s interesting that a remark from 1874 provides a way to deduce H-level using exact functors and involution splitting. I wonder how this relates to other findings in the field! There's a lot to unpack here in the realm of abstract mathematics.
collab wait(call_kKcScqNPulE4GG4kzgifOqqP)
  receivers: 019d8774-8416-7b61-b792-15ed9c3b7dac
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re
file='chapters/theory/higher_genus_complementarity.tex'
lines=open(file).read().splitlines()
for i,line in enumerate(lines,1):
    if 2082 <= i <= 2205:
        for match in re.finditer(r\"\\\\ref\\{(["'^}]+)'"\\}\", line):
            print(i, match.group(1))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2087 conv:regime-tags
2090 thm:config-space-bv
2090 thm:bv-functor
2094 sec:frame-complementarity
2103 thm:config-space-bv
2106 thm:bv-functor
2107 thm:verdier-bar-cobar
2132 prop:modular-deformation-truncation
2134 thm:modular-homotopy-convolution
2138 lem:bar-chart-lagrangian-lift
2149 thm:config-space-bv
2152 thm:config-space-bv
2153 thm:bv-functor
2155 thm:verdier-bar-cobar
2162 thm:bv-functor
2185 thm:bv-functor
2194 lem:bar-chart-lagrangian-lift
2194 prop:lagrangian-eigenspaces
2197 lem:bar-chart-lagrangian-lift
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && for label in conv:regime-tags thm:config-space-bv thm:bv-functor sec:frame-complementarity thm:verdier-bar-cobar prop:modular-deformation-truncation thm:modular-homotopy-convolution lem:bar-chart-lagrangian-lift prop:lagrangian-eigenspaces; do printf '-- %s --\\n' "'$label; rg -n "label'"\\\\{"'$label'"\\\\}\" chapters appendices main.tex; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
-- conv:regime-tags --
chapters/theory/introduction.tex.bak:1860:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
chapters/theory/introduction.tex:2580:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
-- thm:config-space-bv --
chapters/connections/bv_brst.tex:1307:\label{thm:config-space-bv}
-- thm:bv-functor --
chapters/connections/bv_brst.tex:1363:\label{thm:bv-functor}
-- sec:frame-complementarity --
chapters/frame/heisenberg_frame.tex:1761:\label{sec:frame-complementarity}
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1702:\label{sec:frame-complementarity}
-- thm:verdier-bar-cobar --
chapters/theory/cobar_construction.tex:1314:\label{thm:verdier-bar-cobar}
-- prop:modular-deformation-truncation --
chapters/theory/chiral_hochschild_koszul.tex:2060:\label{prop:modular-deformation-truncation}
-- thm:modular-homotopy-convolution --
chapters/theory/higher_genus_modular_koszul.tex:10934:\label{thm:modular-homotopy-convolution}
-- lem:bar-chart-lagrangian-lift --
chapters/theory/higher_genus_complementarity.tex:2012:\label{lem:bar-chart-lagrangian-lift}
-- prop:lagrangian-eigenspaces --
chapters/theory/higher_genus_complementarity.tex:1914:\label{prop:lagrangian-eigenspaces}

thinking
**Reviewing theorem statuses and proof line ranges**

I'm examining the statuses of referenced theorems like `thm:config-space-bv` and how they align with claims such as `ClaimStatusProvedHere` or `ClaimStatusConditional`. I'll also gather line ranges for statement and proof sections C0, C1, and C2, including detailed proof steps like Step I and Step II by searching subsections to outline the full proof structure comprehensively.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Step II" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1158:\subsection{Step II: Verdier duality on fibers}
1160:\begin{proof}[Step II: Steps 5-6]
1361:\subsection{Step III: decomposition and complementarity}
1363:\begin{proof}[Step III: Steps 7-10]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re
lines=open('chapters/theory/higher_genus_complementarity.tex').read().splitlines()
for i,line in enumerate(lines,1):
    if 757 <= i <= 1155 and '\\\\end{proof}' in line:
        print('end', i)
        break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
end 803
wait(call_kKcScqNPulE4GG4kzgifOqqP) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1290,1390p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \[
 \{a, b\} := (-1)^{|a|}\bigl[\Delta(ab) - \Delta(a)\,b
 - (-1)^{|a|} a\,\Delta(b)\bigr]
 \]
 (the failure of $\Delta$ to be a graded derivation) satisfies the
 graded Leibniz rule in each slot:
 \begin{gather*}
 \{a, bc\} = \{a, b\}\,c + (-1)^{(|a|+1)|b|} b\,\{a, c\},\\
 \{a, b\} = -(-1)^{(|a|+1)(|b|+1)}\{b, a\}.
 \end{gather*}
\end{enumerate}
The bracket automatically satisfies the graded Jacobi identity.
\end{definition}

\subsection{BV structure from configuration spaces}

\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
\label{thm:config-space-bv}
Assume that the diagonal-residue operator on the logarithmic bar
complex extends to a degree-$+1$ second-order operator


thinking
**Composing detailed final remarks**

I'm organizing the final response into sections C0, C1, and C2 with bullet points for statements, proofs, and references including file paths and line numbers inline. I'll highlight the conditional status of C2 and emphasize that no unresolved references remain, carefully listing the many references while adhering to the formatting instructions and ensuring clarity and completeness in the final message.


codex
**C0 (Fiber–center identification, lines 372‑428)**  
- Statement: `chapters/theory/higher_genus_complementarity.tex:372‑428` describes the coderived/flat comparison, perfectness locus, and the $\kappa=0$ recovery for the genus‑$g$ bar family.  
- Proof: `lines 430‑498` filter the strict flat model, collapse the bar filtration, apply base change, and tie the surviving $\mathcal{H}^0$ to $\mathcal{Z}_{\mathcal{A}}$.  
- References: `conv:higher-genus-differentials` (chapters/theory/higher_genus_foundations.tex:229‑279); `prop:gauss-manin-uncurving-chain` (chapters/theory/higher_genus_foundations.tex:345‑380); `lem:perfectness-criterion` (chapters/theory/higher_genus_complementarity.tex:288‑325); `thm:cobar-resolution-scoped` (chapters/theory/higher_genus_foundations.tex:2061‑2079); `thm:obstruction-quantum` (chapters/theory/higher_genus_foundations.tex:4589‑4605). No anomalous refs or status tags appear inside this proof.

**C1 (Quantum complementarity, lines 524‑594)**  
- Statement: `chapters/theory/higher_genus_complementarity.tex:524‑594` spells out the H‑level homotopy decomposition plus Verdier duality, the S‑level cohomological shadow, and the genus‑0 fixed classes.  
- Proof: The sketch at `lines 600‑610` points to Steps I‑III; the detailed work runs through Step I (genus filtration and spectral sequence construction, roughly `lines 755‑1149`), Step II (Verdier duality on fibers, `lines 1158‑1344`), and Step III (decomposition/exhaustion, `lines 1361‑1870`).  
- References:  
  `lem:genus-filtration` (chapters/theory/higher_genus_complementarity.tex:762); `def:geometric-bar` (chapters/theory/bar_construction.tex:502); `thm:ss-quantum` (chapters/theory/higher_genus_complementarity.tex:817); `thm:arnold-three` (chapters/theory/bar_construction.tex:1189); `prop:lagrangian-eigenspaces` (chapters/theory/higher_genus_complementarity.tex:1914); `lem:bar-chart-lagrangian-lift` (chapters/theory/higher_genus_complementarity.tex:2012); `prop:ptvv-lagrangian` (chapters/theory/higher_genus_complementarity.tex:2260); `thm:verdier-bar-cobar` (chapters/theory/cobar_construction.tex:1314); `thm:verdier-duality-config-complete` (chapters/theory/higher_genus_complementarity.tex:1165); `lem:verdier-extension-exchange` (chapters/theory/cobar_construction.tex:354); `lem:verdier-involution-moduli` (chapters/theory/higher_genus_complementarity.tex:1557); `thm:chiral-koszul-duality` (chapters/theory/chiral_koszul_pairs.tex:4667); `def:chiral-koszul-pair` (chapters/theory/chiral_koszul_pairs.tex:641); `thm:bar-concentration` (chapters/theory/chiral_koszul_pairs.tex:1132); `thm:conilpotency-bar` (chapters/theory/bar_cobar_adjunction_curved.tex:581); `thm:e1-module-koszul-duality` (chapters/theory/chiral_koszul_pairs.tex:5705); `thm:geometric-equals-operadic-bar` (chapters/theory/bar_construction.tex:2065); `prop:model-independence` (chapters/theory/bar_construction.tex:1473); `cor:duality-bar-complexes-complete` (chapters/theory/higher_genus_complementarity.tex:1238); `cor:quantum-dual-complete` (chapters/theory/higher_genus_complementarity.tex:1332); `lem:ss-duality-complete` (chapters/theory/higher_genus_complementarity.tex:1278); `lem:quantum-from-ss` (chapters/theory/higher_genus_complementarity.tex:965); `lem:fiber-cohomology-center` (chapters/theory/higher_genus_complementarity.tex:1017); `lem:involution-splitting` (chapters/theory/higher_genus_complementarity.tex:235); `lem:center-isomorphism` (chapters/theory/higher_genus_complementarity.tex:1592); `lem:eigenspace-decomposition-complete` (chapters/theory/higher_genus_complementarity.tex:1644); `lem:obs-def-split-complete` (chapters/theory/higher_genus_complementarity.tex:1757); `lem:trivial-intersection-complete` (chapters/theory/higher_genus_complementarity.tex:1788); `lem:exhaustion-complete` (chapters/theory/higher_genus_complementarity.tex:1808); `prop:ptvv-lagrangian` (chapters/theory/higher_genus_complementarity.tex:2260); `thm:kodaira-spencer-chiral-complete` (chapters/theory/higher_genus_complementarity.tex:1368); `thm:mc2-bar-intrinsic` (chapters/theory/higher_genus_modular_koszul.tex:3770); `thm:ambient-d-squared-zero` (chapters/theory/higher_genus_modular_koszul.tex:31649); `thm:ambient-complementarity-fmp` (chapters/theory/higher_genus_complementarity.tex:4983); `cor:virasoro-quantum-dim` (chapters/theory/higher_genus_complementarity.tex:2590); `sec:FM-compactification` (chapters/theory/configuration_spaces.tex:93); `def:koszul-dual-chiral` (chapters/theory/chiral_koszul_pairs.tex:4493); `thm:quantum-complementarity-main` itself (chapters/theory/higher_genus_complementarity.tex:525); `app:signs` (appendices/signs_and_shifts.tex:2); `app:sign-conventions` (appendices/signs_and_shifts.tex:713); `conv:regime-tags` & `conv:proof-architecture` (chapters/theory/introduction.tex:2580); `part:characteristic-datum` (main.tex:1073); `subsec:genus2-complementarity-verification` (chapters/examples/genus_expansions.tex:1676).  
No unresolved references appear inside this proof, and every cited theorem/lemma is defined with a matching `ClaimStatus` in the referenced file.

**C2 (Shifted-symplectic complementarity, lines 2082‑2144)**  
- Statement: `chapters/theory/higher_genus_complementarity.tex:2082‑2144` records the conditional BV upgrade, noting the `ClaimStatusConditional` tag and the need for the BV package plus Verdier comparisons.  
- Proof: `chapters/theory/higher_genus_complementarity.tex:2147‑2201` spells out the BV bracket, the Kontsevich–Pridham formalism, and how the eigenspaces lift via the bar chart transport.  
- References: `conv:regime-tags` (chapters/theory/introduction.tex:2580); `thm:config-space-bv` (chapters/connections/bv_brst.tex:1307); `thm:bv-functor` (chapters/connections/bv_brst.tex:1363); `sec:frame-complementarity` (chapters/frame/heisenberg_frame.tex:1761); `thm:verdier-bar-cobar` (chapters/theory/cobar_construction.tex:1314); `prop:modular-deformation-truncation` (chapters/theory/chiral_hochschild_koszul.tex:2060); `thm:modular-homotopy-convolution` (chapters/theory/higher_genus_modular_koszul.tex:10934); `lem:bar-chart-lagrangian-lift` (chapters/theory/higher_genus_complementarity.tex:2012); `prop:lagrangian-eigenspaces` (chapters/theory/higher_genus_complementarity.tex:1914). Because the two BV theorems themselves carry `ClaimStatusConditional`, the conditional tag on C2 lines up with the dependency graph; no unresolved labels remain.



thinking
**Evaluating the C0 theorem**

I'm noticing a potential issue in part (iii) regarding zero-curvature recovery: if κ(A)=0, then it suggests d_fib^2=0. However, the conclusion in part (ii) about the curved model still hinges on the identification with the center local system. The proof indicates that the same conclusion can be interpreted directly from this, so I need to double-check the logic and ensure that all assumptions are valid. Let's explore the implications further!
thinking
**Evaluating mathematical statements**

I need to address a few mathematical adjustments. First, I could replace part (iii) with a weaker statement: "if κ(A)=0, the curved model lies in the ordinary derived category." Alternatively, I might need to show that when κ=0, the Gauss-Manin correction is null-homotopic or quasi-isomorphic so curved and flat models are equivalent. 

I need to check a potential issue in the C1 theorem statement regarding definitions of Q_g(A) and how it relates to involution splitting lemma. There’s also another point in Step 8 about the Verdier involution that needs careful consideration because it may not hold for the cohomology I'm dealing with.
thinking
**Considering cohomology composition**

I'm thinking that the composition on bar cohomology might be the identity if both pairings are perfect. However, they only reference a theorem on configuration spaces, so this could be seen as overreaching. It raises some concerns for me because the center-isomorphism issue seems more fundamental. I may need to explore this further to clarify whether the assumptions hold or if I'm missing something crucial in the reasoning. Let's keep digging into these concepts!
thinking
**Assessing citation accuracy**

I noticed that the opening paragraph from lines 100-103 claims “nondegeneracy … verified family by family (Proposition...)”, but it seems to be a false citation since it doesn’t mention nondegeneracy of the Verdier pairing. This statement is found in the file targeted for C2, but it's not related to theorem proof, which makes me question its accuracy. I need to clarify this point further for better understanding.
thinking
**Reflecting on theorem challenges**

I'm noticing a potential issue in theorem C1, particularly in Step 8 line 1634 where j_* and j_! differ by a shift related to the dualizing complex, which creates a factor in eigenvalue identification. There seems to be a lack of proof and uncertainty around the boundary's dimension. I should search for some references and ensure I identify around 8-12 findings to present to the user, especially since they asked about exhaust surfaces.
thinking
**Identifying findings for discussion**

I’m thinking about a range of findings I can cover related to several theorems and lemmas. There's the C0 theorem, perfectness lemma, spectral sequence geometry in C1, and issues with the invalid center isomorphism in C1. I also need to consider the missing proof elements in the C1 theorem. There are about 10-11 findings in total, including C2 issues like genus-zero misuse. I should organize these topics for clarity before sharing with the user.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
text=pathlib.Path('chapters/theory/higher_genus_complementarity.tex').read_text()
lines=text.splitlines()
regions=[(430,498),(600,610),(761,2200)]
refs=[]
for a,b in regions:
    for i in range(a-1,b):
        for m in re.finditer(r'\\\\ref\\{(["'^}]+)'"\\}', lines[i]):
            refs.append((i+1,m.group(1)))
seen=[]
for item in refs:
    if item[1] not in [x[1] for x in seen]:
        seen.append(item)
for line,label in seen:
    print(f\"{line}:{label}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
434:conv:higher-genus-differentials
439:prop:gauss-manin-uncurving-chain
477:thm:cobar-resolution-scoped
480:thm:obstruction-quantum
490:lem:perfectness-criterion
603:lem:genus-filtration
605:thm:verdier-duality-config-complete
607:thm:kodaira-spencer-chiral-complete
776:def:geometric-bar
840:thm:ss-quantum
871:thm:arnold-three
930:lem:fiber-cohomology-center
945:thm:conilpotency-bar
974:lem:quantum-from-ss
988:thm:quantum-complementarity-main
990:def:complementarity-complexes
996:lem:eigenspace-decomposition-complete
1019:def:chiral-koszul-pair
1116:thm:geometric-equals-operadic-bar
1122:thm:bar-concentration

thinking
**Considering geometric bar definition**

I’m thinking about whether I should read about the definition of the geometric bar. It might not be necessary, but if I find that spectral sequences are using the wrong object, it could be helpful. Maybe it's okay to move forward without it for now, but I could always read it later if I need more clarification. Let’s just keep an eye on that label.
exec
/bin/zsh -lc "rg -n \"label\\{def:geometric-bar\\}\" chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_construction.tex:502:\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%

thinking
**Evaluating theorem requirements**

I’m considering whether it’s necessary to read the continuation of the theorem C2 proof. I might inspect the `prop:model-independence` to see if it supports functoriality, but it probably won’t be critical. The theorem proof doesn’t cite it. Still, mentioning that moving a remark into the proof could suffice with the model independence theorem. However, I need to check that it addresses gradings since part (iii) of the theorem references compatibility with conformal weight and cohomological degree gradings.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1450,1495p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1450	
  1451	\emph{Chain map property.}\label{thm:bar-induced-chain-map}
  1452	Since $f$ commutes with the internal differential ($f$ is a
  1453	$\mathcal{D}$-module map), with the residue differential ($f$
  1454	preserves the chiral product), and does not affect the de~Rham
  1455	component, $\bar{B}^{\mathrm{geom}}(f)$ commutes with
  1456	$d = d_{\mathrm{int}} + d_{\mathrm{res}} + d_{\mathrm{dR}}$.
  1457	
  1458	\emph{Coalgebra morphism.}\label{lem:bar-induced-coalgebra}
  1459	The coproduct $\Delta$ is defined by restricting to collision
  1460	divisors; since $f$ acts on algebra factors and $\Delta$ acts
  1461	on the indexing set,
  1462	$\Delta \circ \bar{B}(f) = (\bar{B}(f) \otimes \bar{B}(f))
  1463	\circ \Delta$. The counit compatibility and preservation of
  1464	identities and composition are immediate from the definition.
  1465	\end{proof}
  1466	
  1467	\begin{corollary}[Natural transformation property; \ClaimStatusProvedHere]\label{cor:bar-natural}
  1468	\label{cor:why-functoriality}
  1469	A commutative diagram of chiral algebras induces a commutative diagram of bar complexes: if $k \circ f = g \circ h$ in $\mathsf{ChirAlg}_X$, then $\bar{B}(k) \circ \bar{B}(f) = \bar{B}(g) \circ \bar{B}(h)$ in $\mathsf{dgCoalg}_X$. This is immediate from functoriality.

thinking
**Refining findings list**

I'm thinking that my answer should be concise, possibly limiting the findings to about 10-12 items. I don't want to overwhelm the user, but I need to ensure there's enough information. Including a low severity citation to standard-examples-modular-koszul might be useful for clarity, especially since the user wants every missing definition. However, if I go over 12 items, it might not be necessary. I want to verify everything and close any unused agents before finalizing my response.
collab close_agent(call_bpxhyt95nnRU9YE4xHRXKCIy)
  receiver: 019d8774-8416-7b61-b792-15ed9c3b7dac
close_agent(call_bpxhyt95nnRU9YE4xHRXKCIy) completed: "**C0 (Fiber–center identification, lines 372‑428)**  
- Statement: `chapters/theory/higher_genus_complementarity.tex:372…":
  receiver: 019d8774-8416-7b61-b792-15ed9c3b7dac
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1012,1038p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1012	\end{proof}
  1013	
  1014	\emph{Step 4: Identify fiber cohomology with center.}
  1015	
  1016	\begin{lemma}[Fiber cohomology and center; \ClaimStatusProvedHere]
  1017	\label{lem:fiber-cohomology-center}
  1018	For a Koszul chiral algebra~$\mathcal{A}$
  1019	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
  1020	the fiber cohomology sheaf over the smooth
  1021	locus~$\overline{\mathcal{M}}_g^{\mathrm{sm}}$ satisfies:
  1022	\begin{equation}
  1023	\mathcal{H}^*_{\mathrm{fiber}}(\mathcal{A})
  1024	\big|_{\overline{\mathcal{M}}_g^{\mathrm{sm}}}
  1025	\cong Z(\mathcal{A}) \otimes \underline{\mathbb{C}}
  1026	\end{equation}
  1027	where $\underline{\mathbb{C}}$ is the constant sheaf.
  1028	\end{lemma}
  1029	
  1030	\begin{proof}[Proof of Lemma~\ref{lem:fiber-cohomology-center}]
  1031	Fix a smooth curve $\Sigma_g$ of genus~$g$. The fiber of the bar



thinking
**Evaluating geometry steps**

I'm identifying a problem with my findings on step I regarding wrong fibration products and filtration geometry. I think I spotted an issue around line 848. The problem comes from using a fixed-curve product to derive the moduli spectral sequence instead of utilizing the universal family, which undermines step I. To fix this, I should replace it with the universal configuration family. This seems critical to address!
thinking
**Deciding on findings count**

I'm thinking about how many findings to include. Maybe I should aim for 10 to keep it concise. The user mentioned digging deeper for second-order insights, which sounds good too. I guess 10 solid findings should be plenty to provide valuable information without overwhelming the user. It’s a balance between depth and keeping it digestible, so I want to make sure I hit that sweet spot!
thinking
**Clarifying fixes**

I need to explain the exact fix instead of just giving generalities. It seems important to mention specific hypotheses or names when discussing a solution. This clarity should help in finding the exact fix I’m looking for. I'm considering how being specific can make things easier to understand for anyone following along. Let me refine how I communicate this so it's precise and clear. It's all about getting to that exact point!
codex
- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:356` — PROBLEM: Lemma `lem:perfectness-criterion` concludes perfectness from finite-dimensional fiber cohomology plus base change, but the proof never proves pseudo-coherence/coherence of the infinite bar complex, and the cited base-change step only gets you as far as bounded/coherent direct images, not perfection. FIX: Strengthen the lemma to assume bounded pseudo-coherent/coherent filtered pieces and use regularity of `\overline{\mathcal M}_g` to pass from bounded coherent to perfect; otherwise weaken the conclusion to bounded coherent and stop using this lemma as a perfection criterion.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:477` — PROBLEM: C0 Step 3 cites `thm:cobar-resolution-scoped` to identify the genus-`g` strict flat bar family as a bar resolution, but `chapters/theory/higher_genus_foundations.tex:2061` is a genus-0 bar-cobar resolution statement and does not prove a relative genus-`g` resolution over moduli. FIX: Insert a new relative higher-genus resolution lemma for `R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)` and cite that here; if you do not have that lemma, delete the resolution-based center identification from C0(ii).

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:480` — PROBLEM: C0 Step 3 cites `thm:obstruction-quantum` to identify `\mathcal H^0(R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA))` with `\mathcal Z_{\cA}`, but `chapters/theory/higher_genus_foundations.tex:4601-4607,4649-4654` only identifies `\mathcal H^0` of the endomorphism complex `\mathcal E^\bullet_{g,\mathrm{flat}}(\cA)` with the center. That is the wrong object. FIX: Replace this citation with a lemma computing `H^0` of the flat fiber bar complex itself, or weaken C0(ii) to the vanishing statement until the pushforward-to-center identification is actually proved.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:532` — PROBLEM: Theorem C1 is quantified over every “chiral Koszul pair”, but its statement and proof use the center local system, genus-`g` bar families, Verdier-in-families, and higher-genus differentials from the modular pre-Koszul package, not bare genus-0 Koszulity. FIX: Change the opening hypothesis to “Let `(\cA,\cA^!)` be a chiral Koszul pair carrying the modular pre-Koszul datum/MK1–MK3 of Definition `def:modular-koszul-chiral`,” and propagate that scope to Definition `def:complementarity-complexes` and Steps I–III.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:848` — PROBLEM: Step I builds the Leray spectral sequence from `\overline{C}_n(X)\times \overline{\mathcal M}_g \to \overline{\mathcal M}_g`, which is the wrong geometry for varying curves. The proof needs the universal compactified configuration family, not a product with a fixed `X`. FIX: Replace the displayed fibration by the universal relative configuration map already implicit at lines 785-793, rewrite `E_1/E_2` using its pushforwards, and remove the fixed-product language.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1597` — PROBLEM: The sublemma `Z(\cA)\cong Z(\cA^!)` is proved by invoking `thm:e1-module-koszul-duality`, but `chapters/theory/chiral_koszul_pairs.tex:5682-5698` explicitly says the general chiral module-category duality surface is not proved, and `5703-5716` only covers the complete/conilpotent `\Eone`, quadratic, genus-0 lane. FIX: Delete this proof and either prove a direct center-comparison theorem under the current higher-genus hypotheses or restate Step 8 as a duality between `Z(\cA)` and `Z(\cA^!)` without identifying them.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1556` — PROBLEM: Step 8 turns Verdier duality between the `\cA` and `\cA^!` spectral sequences into an involution `\sigma` on `H^*(\overline{\mathcal M}_g,Z(\cA))` itself, then into `\pm1` eigenspaces at lines 1643-1742. That self-identification is exactly the unproved point. FIX: Restate Lemmas `lem:verdier-involution-moduli` and `lem:eigenspace-decomposition-complete` as an isomorphism/pairing between the `\cA` and `\cA^!` coefficient systems; only reintroduce a single-space involution after proving an honest self-identification of centers.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:495` — PROBLEM: C0(iii) claims that `\kappa(\cA)=0` lets the conclusion of C0(ii) be read directly on the curved model, but `\dfib^2=0` only makes the curved model an ordinary complex; it does not identify `(\barB^{(g)},\dfib)` with `(\barB^{(g)},\Dg{g})`. FIX: Either prove a comparison quasi-isomorphism at `\kappa=0`, or weaken C0(iii) to “the curved model becomes an ordinary complex” and stop there.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:828` — PROBLEM: Step I calls `d_{\mathrm{fiber}}` the fiber differential and then proves `d_{\mathrm{fiber}}^2=0` from Arnold at line 871, contradicting `chapters/theory/higher_genus_foundations.tex:238-271`, where the genus-`g` fiber differential satisfies `\dfib^2=\kappa(\cA)\omega_g`. FIX: Rename the `E_1`-page differential to the genus-0 collision part `\dzero`/`d_{\mathrm{coll}}`, and state explicitly that the spectral sequence filters the strict flat differential `\Dg{g}`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:600` — PROBLEM: The printed proof of Theorem C1 closes at line 1870 after proving the S-level splitting, but the theorem statement also claims an H-level cochain pairing and functorial/graded compatibility. The post-proof remark at 1874-1900 is not part of the proof and still does not establish the pairing or grading clause. FIX: Move the H-level argument into the theorem proof before `\qedhere`, add a separate cochain-level Verdier pairing lemma, and either prove functoriality/weight compatibility there or delete those clauses from the theorem statement.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1445` — PROBLEM: Step 7 specializes to `H^*(\overline{\mathcal M}_g,Z(\cA))` using `lem:fiber-cohomology-center`, but that lemma only proves the center identification on the smooth locus at `chapters/theory/higher_genus_complementarity.tex:1018-1026`. The boundary extension is missing. FIX: Insert a boundary-extension lemma before line 1445 and cite it; otherwise replace the compactified-moduli cohomology in Step 7-10 by the smooth locus.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2123` — PROBLEM: C2 defines `L_g:=\barB^{(g)}(\cA)[1]` as a dg Lie algebra, but in this chapter the genus-`g` bar complex is ambiguous and the fiberwise model is curved. The proof never proves that the conditional BV bracket on `\barB^{\mathrm{ch}}(\cA)` descends to the strict flat genus-`g` chart. FIX: Replace `L_g` by `L_g:=\barB^{(g)}_{\mathrm{flat}}(\cA)[1]` everywhere in C2, and add a lemma that the BV bracket is compatible with the genus filtration and restricts to each fixed-genus strict flat chart.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2105` — PROBLEM: C2 uses `thm:verdier-bar-cobar` as a generic all-genus input, but `chapters/theory/cobar_construction.tex:1316-1320` tags that theorem as `[Regime: quadratic, genus-0]`. The same proof then invokes Kontsevich-Pridham at lines 2186-2190 without importing completeness/pronilpotence for the dg Lie algebra. FIX: Restrict C2 to the quadratic genus-0 lane or replace the citation with a family/genus-`g` Verdier comparison theorem, and add an explicit hypothesis that the completed `L_g` is pronilpotent/complete before applying Kontsevich-Pridham.

## Summary
Checked: 13 | Findings: 13 | Verdict: FAIL
tokens used
158,541
