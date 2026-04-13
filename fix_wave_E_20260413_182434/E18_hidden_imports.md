# E18_hidden_imports (861s)

I audited the requested import sites in `higher_genus_modular_koszul.tex`; these were the surviving defects.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:710): MK1 for the free-field proposition imported `thm:km-chiral-koszul`, which is an affine Kac-Moody theorem and does not prove genus-0 Koszulity for the free fermion or the `\beta\gamma`--`bc` pair. EXACT edit applied: replaced that citation block with `thm:heisenberg-koszul-dual-early`, `thm:fermion-boson-koszul`, and `thm:betagamma-bc-koszul`, matched to the three families actually covered there.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:765) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1820): the principal `\mathcal W` proofs cited `thm:bar-cobar-spectral-sequence`, which only constructs the spectral sequence and does not supply the completed diagonal Koszul input needed for MK1. EXACT edit applied: replaced that import with `cor:w-principal-completed-koszul`, while keeping `thm:w-algebra-koszul-main` for the duality input.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:13338): item (III) of the universal modular deformation functor proof relied on chiral twisting-morphism representability “transported to the modular setting” without a theorem on the page proving that extension. EXACT edit applied: replaced the handwave with `cor:vol1-theta-log-fm-twisting-data` and `cor:strictification-comparison(i)`, which are the explicit modular and strict-model results already in this chapter.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16994): the archetype-classification proof cited a general “diagonal Ext-vanishing criterion” for Heisenberg, lattice, and `\beta\gamma`, but not the example theorems that actually establish those cases. EXACT edit applied: replaced that shortcut with exact family-level imports: `thm:heisenberg-koszul-dual-early`, `thm:lattice:koszul-morphism`, and `thm:betagamma-bar-cohomology`.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:26987): the DT-counting proof used the package shorthand “Theorem D” instead of the exact theorem surface proving the displayed formula. EXACT edit applied: replaced the shorthand with `Theorem~\ref{thm:modular-characteristic}` and wrote the imported formula explicitly as `F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g`.

Verification: I re-read the edited surfaces, confirmed the new labels exist in source, and checked that the stale defective import strings are gone from the audited sites. I did not run a full TeX build.


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
session id: 019d87db-bd9d-7412-859f-7de10fddfa07
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Find hidden imports in Vol I theory chapters.
Search for 'by Theorem', 'by Proposition', 'by Lemma', 'follows from'.
For each: does the cited result exist and prove what's needed?
Focus on higher_genus_modular_koszul.tex (the largest file).
mcp startup: no servers

thinking
**Evaluating editing options**

It seems that I need to focus on the assigned file specifically, which is named higher_genus_modular_koszul.tex. The action safety suggests that I should only edit files assigned to me, so external dependencies might be an issue, as I'm unable to edit those. I’ll need to figure out the exact file path to ensure I’m working on the correct document. It's essential to clarify these boundaries while editing!
codex
Using `deep-beilinson-audit` for a citation/proof-surface audit. I’m first loading the required constitutional files plus the target chapter, then I’ll extract every “by Theorem/Proposition/Lemma/follows from” site in `higher_genus_modular_koszul.tex` and verify each citation against the live source.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'red_team_summary.md' -g 'higher_genus_modular_koszul.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/concordance.tex
chapters/theory/higher_genus_modular_koszul.tex

thinking
**Gathering necessary files**

I need to read the required files, starting with the path for the red_team_summary, which might be in the archive. I could consider using rg locate, but maybe I don’t need to use explorer. I want to focus on reading relevant sections rather than skimming through huge documents—just enough to get the information. I'll use rg around the higher_genus file to look for target phrases and might need to update my plan after getting the context. Let’s gather what I need!
codex
I have the audit workflow and target path. Next I’m reading the constitutional sources and enumerating every import-like phrase in the chapter so I can verify them one by one against actual labels and hypotheses.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md' -g 'raeeznotes/raeeznotes100/red_team_summary.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -n "by Theorem|by Proposition|by Lemma|follows from" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
350:Involutivity $(\mathcal{A}^!)^! \cong \mathcal{A}$ follows from applying
374:hence a resolution. Minimality follows from the diagonal Ext vanishing
383:Koszulity follows from the explicit bar complex computations
656:\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
712:MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
721:\ref{MK:verdier} for the standard landscape follows from: (1)~the genus-$0$ bar-cobar Verdier pairing
766:MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
767:MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
1065:by Theorem~\ref{thm:km-chiral-koszul}.
1150:$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
1619:item~(iii) follows from~(i) and the
1769:item~(iii) follows from~(i) and the
1830:item~(iii) follows from~(i) and the
2092:\index{MK3!follows from MK1|textbf}
2649:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2705:by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
2706:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2945:The group homomorphism property follows from~(iv): additivity
3976: by Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b).
4141: because centrality follows from the locality axiom alone.
 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |




thinking
**Auditing hidden imports**

I'm diving into auditing "hidden imports" in higher_genus_modular_koszul.tex. The search results show many lines, but not all are actual citations—it seems some might just be internal proof. I should focus on explicit references like 'by Theorem/Proposition/Lemma' and anything that says 'follows from,' since that's where cited results should be. I need to ensure I'm exhaustive within the assigned scope, auditing matches in this file despite its size since finding issues is critical.
thinking
**Extracting and inspecting phrases**

I need a systematic approach to extract all matches with context in the document. Many might be internal proofs, like "follows from," which aren't issues. I'll inspect phrases around explicit citations and those suspicious uncited ones. It might be beneficial to use a script to capture contexts, focusing on problematic hidden imports. Since the document has about 33k lines, it's challenging to verify each manually. I should look for citations in theorems, propositions, and lemmas, along with "follows from" phrases. An automated approach could help list matches and check for cited labels.
thinking
**Parsing citations for audit**

I could parse citations in those lines and audit whether the cited results actually exist. Using a combination of `rg` for labels and perhaps a script with custom `awk` could work well. I'd need to rely on shell commands to inspect contexts around explicit citations. I might consider using the explorer tool to find all labels, following the instructions for codebase questions since this involves text files. But it seems there's no explicit request for parallel or delegated tasks unless the user asks for them specifically.
codex
I’ve got the candidate import sites. The file is dense enough that I’m switching to a structured pass: first isolate every explicit theorem/proposition/lemma citation in the chapter, then check unlabeled “follows from” sites for unsupported imports, and only then patch the chapter with minimum-scope edits.
Plan update
  → Load higher_genus_modular_koszul.tex contexts for all explicit import phrases and map cited labels to live definitions/status
  • Identify broken or underjustified imports in the chapter and choose minimal truthful rewrites confined to the target file
  • Apply patch, then verify no new broken references or unsupported hidden-import phrasing remain on the edited surface
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'while(/(?:Theorem|Proposition|Lemma)~\\\\(?:textup\\{)?ref\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_modular_koszul.tex | sort -u" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "by Theorem|by Proposition|by Lemma|follows from" chapters/theory/higher_genus_modular_koszul.tex -C 2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   35426 chapters/theory/higher_genus_modular_koszul.tex
 succeeded in 51ms:
lem:degree-cutoff
lem:graph-sum-truncation
lem:involution-splitting
lem:mk67-from-mc2
lem:pbw-mixed-factorization
lem:pbw-weightwise-g-module
lem:stable-graph-d-squared
prop:2d-convergence
prop:bar-verlinde-asymptotics
prop:betagamma-T-line-shadows
prop:c13-full-self-duality
prop:carleman-virasoro
prop:collision-locality
prop:critical-cubic-convergence
prop:cross-channel-growth
prop:cross-channel-no-closed-form
prop:curvature-centrality-general
prop:cyclic-ce-identification
prop:depth-gap-trichotomy
prop:dg-shifted-comparison
 succeeded in 51ms:
348-$\bar{B}^{(g)}(\mathcal{A})$ is concentrated on the diagonal in the bigrading,
349-so $(\mathcal{A}^!)^{(g)} := \bar{B}^{(g)}(\mathcal{A})$ is the correct Koszul dual.
350:Involutivity $(\mathcal{A}^!)^! \cong \mathcal{A}$ follows from applying
351-bar-cobar inversion at each genus and passing to the inverse limit using the
352-convergence hypothesis~(2).
--
372-$(\mathcal{A}^!)^{(g)}$. The bar-cobar inversion
373-(Theorem~\ref{thm:higher-genus-inversion}) shows this complex is exact,
374:hence a resolution. Minimality follows from the diagonal Ext vanishing
375-(modular Koszulity hypothesis).
376-\end{proof}
--
381-modular forms and period integrals introduce new cohomological contributions.
382-For the Heisenberg algebra and affine Kac--Moody at generic level, modular
383:Koszulity follows from the explicit bar complex computations
384-in Part~\ref{part:physics-bridges}. A general criterion remains open.
385-\end{remark}
--
654-\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
655-The definition separates \emph{hypotheses} (MK1--MK3) from


thinking
**Inspecting label contexts**

I need to verify the existence of specific labels in my repository. Running a grep command could help check if labels like `thm:heisenberg-bar-complete` and others really exist. Some may not be in the complete registry, so I should search for any suspicious labels. 

Okay, using rg to find `\label` occurrences could work too. An automated existence check for these labels will be beneficial across the repo, focusing on explicit references. I might write a shell loop or use Perl for this.
thinking
**Simplifying label check**

I need a simpler way to check for labels, using a loop like “while read label; do” with an rg command. The command should look for `\\label{$label}` specifically in .tex files. I want to ensure I get output for any missing labels. This approach seems efficient for gathering the necessary information, so I’m ready to implement it. I just need to ensure everything works as expected! Let's execute this.
codex
I’m now distinguishing two failure modes: missing labels versus real labels that do not support the sentence that cites them. The first pass is mechanical; the second is the actual adversarial read.
exec
/bin/zsh -lc 'labels=$(perl -ne '"'while(/(?:Theorem|Proposition|Lemma)~\\\\(?:textup\\{)?ref\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_modular_koszul.tex | sort -u); for label in "'$labels; do count=$(rg -n --fixed-strings "'"\\\\label{"'$label}" . -g '"'*.tex' | wc -l | tr -d ' '); if [ \""'$count" = "0" ]; then echo "MISSING $label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
MISSING lem:degree-cutoff
lem:graph-sum-truncation
lem:involution-splitting
lem:mk67-from-mc2
lem:pbw-mixed-factorization
lem:pbw-weightwise-g-module
lem:stable-graph-d-squared
prop:2d-convergence
prop:bar-verlinde-asymptotics
prop:betagamma-T-line-shadows
prop:c13-full-self-duality
prop:carleman-virasoro
prop:collision-locality
prop:critical-cubic-convergence
prop:cross-channel-growth
prop:cross-channel-no-closed-form
exec
/bin/zsh -lc 'labels=$(perl -ne '"'while(/(?:Theorem|Proposition|Lemma)~\\\\(?:textup\\{)?ref\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_modular_koszul.tex | sort -u); while IFS= read -r label; do [ -z \""'$label" ] && continue; count=$(grep -R -F "'"\\\\label{"'$label}" --include='"'*.tex' . | wc -l | tr -d ' '); if [ \""'$count" = "0" ]; then echo "MISSING $label"; fi; done <<EOF
$labels
EOF' in /Users/raeez/chiral-bar-cobar
thinking
**Considering polling strategy**

It seems like I might still be processing because of many greps running, so I'll think about polling later. Using an rg label for existence could be heavy with loops, but I still want to give it a shot eventually. So, let's plan to poll again as needed and see how things look!
codex
I’ve already hit one likely class of defects: some import sites point to labels that look stale or non-canonical. I’m checking those directly before I touch prose, because a hidden import backed by a dead label is a straight correctness failure, not just weak exposition.
exec
/bin/zsh -lc "sed -n '680,780p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2688,2720p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '13270,13345p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"heisenberg-bar-complete|w-algebra-koszul-main|bar-cobar-spectral-sequence|universal-MC|kappa-additivity|theta-twisting-morphism|linfty-obstruction-5-6|heisenberg-bar-complete\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Functorial}: $\mathcal{C}$ is natural in morphisms
 of modular Koszul objects;
\item \emph{Dualizable}: the duality $\cA \leftrightarrow \cA^!$
 acts on each component
 ($\kappa + \kappa' = K$, $\Delta_{\cA^!}$ determined by
 $\Delta_{\cA}$, etc.);
\item \emph{Modular}: compatible with clutching and
 boundary degeneration on~$\overline{\mathcal{M}}_{g,n}$;
\item \emph{Non-scalar}: $\kappa(\cA)$ is only the first shadow;
 the full package contains strictly more information
 (cf.\ the spectral data of level~(2) in
 Remark~\ref{rem:characteristic-hierarchy}).
\end{enumerate}

\smallskip\noindent
The cyclic $L_\infty$-algebra $\Defcyc(\cA)$ is constructed
by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
(Theorems~\ref{thm:universal-MC}
 succeeded in 52ms:
The scalar formula is
proved unconditionally at genus~$1$ and at all genera on the
uniform-weight lane; for multi-weight algebras at $g \geq 2$,
the scalar formula $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
\textup{(}UNIFORM-WEIGHT\textup{)}
\emph{fails} and the correct expansion includes a cross-channel
correction
(Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}).
The non-perturbative completion (summation over topologies,
instanton sectors, and phase transitions) is a separate
mathematical problem not addressed by the MC framework.
\end{theorem}

\begin{proof}
(i) follows from the bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA = D_\cA - \dzero$
is canonical, and the cyclic trace is gauge-invariant
(Theorem~\ref{thm:shadow-homotopy-invariance}).
(ii) follows from the pronilpotent weight filtration
(Theorem~\ref{thm:recursive-existence}).
 succeeded in 52ms:
$\Ainf$-Yang--Baxter data
(Proposition~\ref{prop:dg-shifted-comparison}).
\end{enumerate}
For simple Lie symmetry, MK6--MK7 follow from
Lemma~\ref{lem:mk67-from-mc2}. MK8 remains programmatic.
\end{remark}

\begin{proposition}[Free-field examples are modular pre-Koszul; \ClaimStatusProvedHere]
\label{prop:standard-examples-modular-koszul}
\index{modular Koszul chiral algebra!examples}
\textup{[Regime: quadratic
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

The following chiral algebras satisfy the antecedent axioms
\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
Theorems~\textup{\ref{thm:higher-genus-inversion}}
and~\textup{\ref{thm:quantum-complementarity-main}} then supply
\textup{MK4--MK5}, so they are modular Koszul:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the Heisenberg algebra $\mathcal{H}_\kappa$
 succeeded in 50ms:
./main.tex:1743: \phantomsection\label{thm:universal-MC}%
./chapters/examples/w_algebras_deep.tex:1062:Theorem~\ref{thm:w-algebra-koszul-main}, not a BV-orbit transport to
./chapters/examples/w_algebras_deep.tex:1127:Theorem~\ref{thm:w-algebra-koszul-main}. The same three ingredients
./chapters/examples/w_algebras_deep.tex:1234:Theorem~\ref{thm:w-algebra-koszul-main}:
./chapters/examples/w_algebras_deep.tex:1904:(Theorem~\ref{thm:w-algebra-koszul-main}).
./chapters/examples/w_algebras_deep.tex:2051: Theorem~\textup{\ref{thm:w-algebra-koszul-main})}.
./chapters/examples/symmetric_orbifolds.tex:13:(Corollary~\ref{cor:kappa-additivity}) and the fact that twisted
./chapters/examples/lattice_foundations.tex:1145: and Corollary~\ref{cor:kappa-additivity}),
./chapters/examples/w3_composite_fields.tex:979: the spectral sequence from Theorem~\ref{thm:bar-cobar-spectral-sequence}
./chapters/examples/free_fields.tex:1445:See Theorem~\ref{thm:heisenberg-bar-complete} for explicit formulas
./chapters/examples/free_fields.tex:3395:(Theorem~\ref{thm:heisenberg-bar-complete}).
./chapters/examples/free_fields.tex:3722:\begin{theorem}[Heisenberg bar complex: complete calculation; \ClaimStatusProvedHere]\label{thm:heisenberg-bar-complete}
./chapters/examples/free_fields.tex:3857:The double pole prevents standard residue extraction: the literal residue $\mathrm{Res}_{z=w}[k/(z-w)^2 \cdot \eta_{zw}]$ vanishes since the integrand has a triple pole with zero residue (cf.\ the clarification at Theorem~\ref{thm:heisenberg-bar-complete}). Instead, the Borcherds identity extracts the OPE coefficient directly, giving the \emph{boundary pairing}
./chapters/examples/free_fields.tex:5792:The explicit low-degree bar complex computations for the free fermion, Heisenberg, and $\beta\gamma$ system are carried out in Theorem~\ref{thm:fermion-bar-complex-genus-0} (free fermion, \S\ref{sec:free-fermion}), Theorem~\ref{thm:heisenberg-bar} and Theorem~\ref{thm:heisenberg-bar-complete} (Heisenberg, \S\ref{sec:heisenberg-bar-complex}), and Theorem~\ref{thm:betagamma-bc-koszul} with Proposition~\ref{prop:bc-betagamma-orthogonality} ($\beta\gamma \leftrightarrow bc$, \S\ref{sec:fermion-boson-koszul}). All results match the predictions of Theorem~\ref{thm:bar-cobar-isomorphism-main}.
./chapters/examples/deformation_quantization_examples.tex:434:The non-termination reflects $m_n \neq 0$ for all $n$ in the deformation complex of $\mathcal{W}_3$ ($\mathcal{W}_3$ is Koszul as a chiral algebra by Theorem~\ref{thm:w-algebra-koszul-main}; the non-termination is in the Coisson-to-chiral deformation, not in bar-cobar duality).
./chapters/examples/deformation_quantization_examples.tex:617:For $\mathrm{Vir}_c$ via DS reduction of $\widehat{\mathfrak{sl}}_2$ at level $k$: the Koszul dual is $\mathrm{Vir}_{26-c}$ (Theorem~\ref{thm:w-algebra-koszul-main}), with curvatures $\kappa(c)=c/2$, $\kappa(c')=(26-c)/2$, summing to $13$ independently of $c$. At $c=0$ the bar complex is uncurved while the dual is maximally curved; at $c=26$ the roles reverse, giving the algebraic uncurved-shadow configuration that appears in the no-ghost discussion.
./chapters/examples/genus_expansions.tex:315:(Theorem~\ref{thm:w-algebra-koszul-main}).
./chapters/examples/genus_expansions.tex:1352:(Theorem~\ref{thm:w-algebra-koszul-main}). The genus-$2$ bar
./chapters/examples/genus_expansions.tex:2349:For a rank-$d$ even unimodular lattice $\Lambda$ (e.g., $E_8$, $E_8 \oplus E_8$, the Leech lattice), the lattice vertex algebra $V_\Lambda \cong \mathcal{H}_1^{\otimes d}$ has obstruction coefficient $\kappa(V_\Lambda) = d$ (Corollary~\ref{cor:kappa-additivity}). The genus-$g$ free energy:
./chapters/examples/genus_expansions.tex:3550:(Corollary~\ref{cor:kappa-additivity}) and the linearity of the generating

thinking
**Searching for theorems**

I'm looking for the exact results regarding free fermions and beta-gamma. I need to check the chapters on free fields and the beta-gamma approach. I wonder if the theorems `thm:fermion-bar-complex-genus-0` and `thm:betagamma-bc-koszul` are relevant here. I'll inspect those chapters carefully. Since my focus is just on editing the target file, I can replace the citations with the correct theorems to ensure accuracy!
codex
One citation is already suspect on content, not just label health: the free-field proof cites a Kac–Moody theorem for MK1. I’m checking the underlying example chapters now so I can replace that import with the theorem(s) that actually establish genus-0 Koszulity for free fermion and `βγ`.
exec
/bin/zsh -lc "sed -n '3700,3815p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:km-chiral-koszul\\}|label\\{thm:fermion-bar-complex-genus-0\\}|label\\{thm:betagamma-bc-koszul\\}|label\\{thm:heisenberg-bar-complete\\}|label\\{prop:free-field-scalar-exact\\}|label\\{thm:heisenberg-higher-genus\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1030,1105p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 specializes to the Verdier identification
 $\mathbb{D}_{\mathrm{Ran}}\, \bar{B}(\cA) \simeq \cA^!_\infty$
 of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
 realized at the chain level by propagator integrals
 \textup{(}Proposition~\textup{\ref{prop:refines-af})}.
 The holomorphic propagator $\eta_{ij} = d\log(z_i - z_j)$
 is a specific representative of the $\Etwo$ propagator class
 $[\alpha_{ij}] \in H^1(\Conf_2(X))$
 \textup{(}Corollary~\textup{\ref{cor:n2-recovery})}.
\end{enumerate}
\end{theorem}

\begin{remark}[Nonlinear Fourier interpretation]
\label{rem:fh-fourier}\label{rem:htt-fourier}\label{rem:curved-fourier}
\index{factorization homology!as Fourier integral}\index{homotopy transfer!Fourier interpretation}\index{coderived category!Fourier interpretation}
The derived Fourier transform (Theorem~\ref{thm:derived-fourier}) replaces $\int_G f\, e^{i\langle\cdot,\cdot\rangle}$ with factorization homology $\int_M A$, the $\En$ propagator serving as kernel. Homotopy transfer (Theorem~\ref{thm:htt}) yields an $\Ainf$-structure via the tree formula (Theorem~\ref{thm:tree-formula}); for Koszul algebras $\tilde{m}_k = 0$ for $k \geq 3$ (Theorem~\ref{thm:chiral-htt}). At genus $g \geq 1$, curvature forces passage to $D^{\mathrm{co}}(\barB_g(\cA))$, where the derived inversion~\eqref{eq:pk-duality-fourier} holds and complementarity (Theorem~\ref{thm:quantum-complementarity-main}) gives $\kappa(\cA) + \kappa(\cA^!) = [\omega_g]$.
\end{remark}

\subsection{Explicit bar complex calculation}

 succeeded in 52ms:
chapters/examples/free_fields.tex:885:\label{thm:fermion-bar-complex-genus-0}
chapters/examples/free_fields.tex:1633:\begin{theorem}[Higher genus Heisenberg; \ClaimStatusProvedHere]\label{thm:heisenberg-higher-genus}
chapters/examples/free_fields.tex:1706:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality; \ClaimStatusProvedHere]\label{thm:betagamma-bc-koszul}
chapters/examples/free_fields.tex:3722:\begin{theorem}[Heisenberg bar complex: complete calculation; \ClaimStatusProvedHere]\label{thm:heisenberg-bar-complete}
chapters/theory/higher_genus_modular_koszul.tex:22464:\label{prop:free-field-scalar-exact}
chapters/theory/chiral_koszul_pairs.tex:846:\label{thm:km-chiral-koszul}
 succeeded in 50ms:
so $\dim H^n$ is constant.
At a special value $\lambda_0 \in \Sigma_n \cup \Sigma_{n+1}$,
either $r_n$ or $r_{n+1}$ drops, causing $\dim H^n$
to (weakly) increase.
\end{proof}

\begin{remark}[Special values and admissible levels]
\label{rem:special-level-values}
\index{admissible level!bar cohomology jump}
The exceptional set $\Sigma_n(\mathfrak{g})$ has at most $\dim\bar{B}^n \cdot \dim\bar{B}^{n-1}$ values. For $\mathfrak{sl}_2$ at degree~$2$, $d_\lambda\colon \bar{B}^2 \to \bar{B}^1$ is a $3 \times 9$ matrix linear in $\lambda$ with generic rank~$3$ for all $\lambda \neq 0$, so $\Sigma_2 = \{0\}$ ($k = -2$), consistent with Theorem~\textup{\ref{thm:universal-kac-moody-koszul}}. Admissible levels $k = -2 + p/q$ are the natural candidates for non-generic behavior (Remark~\textup{\ref{rem:bicomplex-interpretation}}\textup{(iii)}).
\end{remark}

\begin{conjecture}[$\mathfrak{sl}_2$ bar cohomology as spin representations]
\label{conj:sl2-bar-spin-representations}
\ClaimStatusConjectured
\index{bar complex!$\widehat{\mathfrak{sl}}_2$!spin representation|textbf}
\index{Garland--Lepowsky concentration!representation-theoretic refinement}
For each $n \geq 1$, the bar cohomology
$H^n(\bar{B}^\bullet(\widehat{\mathfrak{sl}}_{2,k}))$
at generic level~$k$ carries a natural
 succeeded in 50ms:
\chapter{\texorpdfstring{The $\beta\gamma$ system}{The beta-gamma system}}\label{chap:beta-gamma}
% Regime I: quadratic (Convention~\ref{conv:regime-tags}).

A chiral algebra with a weight-zero generator violates every
positive-grading hypothesis standard in the theory of vertex
operator algebras. At $\lambda = 0$ the $\beta\gamma$ system has a
generator $\gamma$ of conformal weight zero: the mode expansion
$\gamma(z) = \sum_n \gamma_n z^{-n}$ contains a zero mode
$\gamma_0$ that acts on the vacuum without raising energy, the
character diverges as $1/(1-q)$ rather than as a $q$-series with
positive coefficients, and standard positive-energy filtrations
collapse. The algebra cannot be treated as a Heisenberg-type or
Kac--Moody-type object, where a positive grading forces the shadow
tower to terminate at degree~$2$ or~$3$.

The depth classification assigns $\beta\gamma$ to a class of its
own. Heisenberg and lattice algebras (class~$\mathsf{G}$) have
shadow towers terminating at degree~$2$; affine Kac--Moody algebras
(class~$\mathsf{L}$) terminate at degree~$3$; Virasoro and
$\mathcal{W}_N$ (class~$\mathsf{M}$) run to infinity. The

thinking
**Inspecting theorems on fermions**

I’m focusing on free fields rather than a general context. I think I should examine the specific theorems related to fermions and the betagamma function, particularly for genus 0. It might be sufficient to zero in on those areas. I'll need to search for specific labels and delve into the broader context to ensure I have a clear understanding of what's being discussed. This approach should help clarify my knowledge.
exec
/bin/zsh -lc "sed -n '840,940p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1680,1755p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,900p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1700,1765p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}
This single-generator duality should not be confused with the \emph{two-generator} duality $(\beta\gamma)^! \cong bc$ of Theorem~\ref{thm:betagamma-bc-koszul}. Here both sides have $\dim V = 1$; in the $\beta\gamma$--$bc$ duality, both sides have $\dim V = 2$.
\end{remark}

\begin{proof}[Verification of Koszul pair conditions]
\noindent\emph{Generators and weights.}
\begin{itemize}
\item $\mathcal{F}$: one fermionic generator $\psi$ with $h_\psi = 1/2$, so $V = \mathbb{C}\psi$ ($\dim V = 1$)
\item $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$: one bosonic generator $\gamma$ with $h_\gamma = 1/2$, so $V^* = \mathbb{C}\gamma$ ($\dim V^* = 1$)
\end{itemize}

\noindent\emph{Pairing.} The residue pairing $V \times V^* \to \mathbb{C}$ is:
\[\langle\psi, \gamma\rangle = \mathrm{Res}_{z=w}\left[\psi(z)\gamma(w) \cdot 1\right] = 1\]
This is a non-degenerate pairing between 1-dimensional spaces.

\noindent\emph{Relations.}
\begin{itemize}
\item $R_{\mathrm{ferm}} = \mathrm{span}\{\psi \otimes \psi + \psi \otimes \psi\} = \mathrm{Sym}^2(V)$ (antisymmetry: $\psi \otimes \psi = -\psi \otimes \psi$ in graded sense, but the relation $R$ is the symmetric part)
\item $R_{\mathrm{bos}} = 0$ (no relation in $\mathrm{Sym}^2(V^*)$, since $\gamma \otimes \gamma$ is a free generator)
 succeeded in 51ms:
\subsection{\texorpdfstring{$\beta\gamma$--$bc$}{beta-gamma--bc} orthogonality and duality}
 
\begin{proposition}[\texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality; \ClaimStatusProvedHere]\label{prop:bc-betagamma-orthogonality}
The relations $R_{bc} \perp R_{\beta\gamma}$ under the residue pairing: the Clifford relation of the $bc$ system is orthogonal to the Weyl relation of the $\beta\gamma$ system.
\end{proposition}

\begin{proof}
The generators pair via the residue pairing $\langle b, \beta \rangle = 1$, $\langle c, \gamma \rangle = 1$, $\langle b, \gamma \rangle = 0$, $\langle c, \beta \rangle = 0$ (dual bases).

The quadratic relations are $R_{bc} = b \otimes c + c \otimes b$ (Clifford/symmetric) and $R_{\beta\gamma} = \beta \otimes \gamma - \gamma \otimes \beta$ (Weyl/antisymmetric).

Computing:
\begin{align*}
\langle R_{bc}, R_{\beta\gamma} \rangle &= \langle b \otimes c + c \otimes b, \; \beta \otimes \gamma - \gamma \otimes \beta \rangle \\
&= \langle b, \beta \rangle \langle c, \gamma \rangle - \langle b, \gamma \rangle \langle c, \beta \rangle \\
&\quad + \langle c, \beta \rangle \langle b, \gamma \rangle - \langle c, \gamma \rangle \langle b, \beta \rangle \\
&= (1)(1) - (0)(0) + (0)(0) - (1)(1) = 0.
\end{align*}

The cancellation is exact: the symmetric relation $(+)$ and antisymmetric relation $(-)$ are orthogonal complements under the residue pairing. This is the quadratic data underlying the Koszul duality $(\beta\gamma)^! \cong bc$.
 succeeded in 51ms:
\end{proof}
 

\subsection{\texorpdfstring{$\beta\gamma$--$bc$}{beta-gamma--bc} Koszul duality}\label{sec:fermion-boson-koszul}
\index{free fermion!Koszul dual}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality; \ClaimStatusProvedHere]\label{thm:betagamma-bc-koszul}
The $\beta\gamma$ system (two bosonic generators with antisymmetric relation) and the $bc$ ghost system (two fermionic generators with symmetric relation) are Koszul dual:
\begin{equation}\label{eq:betagamma-bc-koszul}
(\beta\gamma)^! \cong bc \quad \text{and} \quad (bc)^! \cong \beta\gamma.
\end{equation}
At the level of bar complexes:
\[
H^*(\bar{B}_{\mathrm{geom}}(bc)) \cong \mathrm{Sym}^{\mathrm{ch}}(\beta, \gamma), \quad
H^*(\bar{B}_{\mathrm{geom}}(\beta\gamma)) \cong \Lambda^{\mathrm{ch}}(b, c).
\]
\end{theorem}

\begin{remark}
This is a \emph{two-generator} duality: $\beta\gamma$ has $\dim V = 2$ (bosonic) and $bc$ has $\dim V^* = 2$ (fermionic). It should not be confused with the \emph{single-generator} duality $\Lambda^{\mathrm{ch}}(\psi) \leftrightarrow \mathrm{Sym}^{\mathrm{ch}}(\gamma)$ between one free fermion and one free boson.
 succeeded in 51ms:
is concentrated in degree $0$:
\[
E_1^{p,q} = H^{p+q}(\operatorname{gr}^p K) =
\begin{cases}
\bC & p = q = 0, \\
0 & p + q > 0.
\end{cases}
\]
All higher differentials $d_r$ for $r \geq 1$ are therefore zero
(they map between zero groups), so the spectral sequence collapses
at $E_1$.

By completeness of the filtration and the bounded-below hypothesis,
the spectral sequence converges:
$E_\infty = \operatorname{gr} H^*(K)$.
Since $E_\infty$ is concentrated in degree~$0$,
we conclude $H^n(K) = 0$ for $n > 0$.
\end{proof}

\begin{remark}[Relation to classical Koszulness]

thinking
**Identifying issues in theorems**

I’m finding that `thm:km-chiral-koszul` clearly has an issue for the free-field scenario. I probably need to identify more content mismatches, too. I should inspect `thm:universal-MC` since the phantom section label may not reference a theorem. There is a theorem in concordance, but it's uncertain whether referencing it in the target file is okay. I’ll search near citation 450 to see what's going on there.
exec
/bin/zsh -lc "sed -n '5328,5388p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,470p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:lattice-sewing}), is \ClaimStatusProvedHere{} (promoted from conjecture).
Targets (C$_{\mathrm{an}}$) and~(D$_{\mathrm{an}}$) remain \ClaimStatusConjectured{}.
The programme is recorded here to fix definitions and their
relationship to the algebraic proved core.
On the derived-algebraic side, Nafcha proves a gluing formula for
chiral homology on families of stable curves [arXiv:2603.30037],
complementing the analytic HS-sewing criterion: Nafcha's formula
operates on derived categories of D-modules on the Ran space;
HS-sewing operates on Hilbert-space trace-class estimates.

\subsection{The universal Maurer--Cartan class}

The genus tower $\{\barB^{(g)}(\cA)\}_{g \geq 0}$
(Theorem~\ref{thm:master-tower}) is controlled by a universal
obstruction.

\begin{theorem}[Universal MC class;
\ClaimStatusProvedHere]\label{thm:universal-MC}
\index{Maurer--Cartan class!universal}
For a modular Koszul chiral algebra $\cA$ with non-degenerate
 succeeded in 51ms:
which the categorical $\exp/\log$ correspondence
(Remark~\ref{rem:nilpotence-periodicity}) holds at all genera:
bar and cobar are mutually inverse on the Koszul locus,
and curvature is controlled by a universal scalar~$\kappa(\cA)$.
All four main theorems hold for modular Koszul algebras.
Definition~\ref{def:modular-koszul-homotopy} gives the homotopy-native
version; Definition~\ref{def:modular-koszul-chiral} gives the concrete
dg model.

\begin{definition}[Modular Koszul object: homotopy form]\label{def:modular-koszul-homotopy}
\index{modular Koszul chiral algebra!homotopy form}
Let $X$ be a smooth projective curve over~$\mathbb{C}$.
A \emph{modular Koszul object} on~$X$ is an augmented factorization algebra
$\cA \in \operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$
equipped with:
\begin{enumerate}[label=\textup{(D\arabic*$_\infty$)}]
\item\label{D:bar-htpy}
A bar object
$\mathbf{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
in the homotopy category of factorization coalgebras.
exec
/bin/zsh -lc "sed -n '2230,2305p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '532,670p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of
the bar complex differential to each cobar tensor factor and preserves
cobar degree~$p$.
The comultiplication term $d_{\text{cobar}}$ raises cobar degree by~$1$,
so it sends $F^p$ into $F^{p+1}$ and vanishes on
$F^p/F^{p+1}=\text{Gr}^p$.
Therefore the induced differential on the associated graded is exactly
$d_{\bar{B}}$, which is the $d_0$ differential of the spectral
sequence.
\end{proof}

\subsection{Spectral sequence construction}

\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
\label{thm:koszul-spectral-sequence}
\textup{[Regime: square-zero total differential on the filtered
bar-cobar complex.]}
Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
satisfies $d^2 = 0$ and preserves the filtration from
Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
 succeeded in 51ms:
\;\hookrightarrow\;
\operatorname{hom}_\alpha(\cC,\, \cP)
\]
of Robert-Nicoud--Wierstra~\textup{\cite[Theorem~4.1]{RNW19}}.
The $sL_\infty$ higher brackets $\ell_k$ ($k \geq 3$) on
$\operatorname{hom}_\alpha$ arise from the homotopy transfer through
the $\operatorname{Hom}$~functor
\textup{(}Loday--Vallette~\textup{\cite[Theorem~10.3.8]{LV12})}.
In particular, the modular convolution algebra
$\mathfrak{g}_\cA^{\mathrm{mod}}$ of
Definition~\textup{\ref{def:modular-convolution-dg-lie}}
is the chiral specialization with
$\cC = \cC^{\textup{!\textasciigrave}}_{\mathrm{ch}}$,
$\cP = \cP^{\mathrm{ch}}$.
\end{theorem}

\begin{proof}[References]
The general operadic convolution identification is
\cite[Theorem~4.1]{RNW19}; the strict model comparison is
\cite[Theorem~10.3.8]{LV12}. The chiral specialization follows from
exec
/bin/zsh -lc "sed -n '560,690p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
genus-$0$ bar construction to all genera via propagators on
$\overline{C}_n(\Sigma_g)$
(Theorem~\ref{thm:prism-higher-genus}).
Each genus-$g$ piece carries a degree-$1$ \emph{fiberwise
differential}~$\dfib$ with
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
(Convention~\ref{conv:higher-genus-differentials}).
The completed total bar object
$\bar{B}^{\mathrm{full}}_X(\cA) :=
\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
carries a strict total differential $\Dg{} \colon
\bar{B}^{\mathrm{full}}_X(\cA) \to \bar{B}^{\mathrm{full}}_X(\cA)$
with $\Dg{}^2 = 0$, whose reduction modulo $\hbar^{g+1}$ restricts
to $\dfib$ at genus~$g$.

\item\label{D:center-dg}
A center local system $\mathcal{Z}_{\cA}$ on
$\overline{\mathcal{M}}_{g,\bullet}$ whose fiber at a smooth
curve~$\Sigma$ is the center $Z(\cA|_\Sigma)$.


thinking
**Checking spectral sequences**

I'm diving into the MK3 and PBW spectral sequences and their concentration at all genera. It seems like there might be an insufficient proof for free-field examples in the citation section, so I need to check if there's a theorem in the file that proves that free-field genus expansions imply PBW concentration. I should also look into a proposition that states all free-field algebras remain exact. Time to search for more details!
exec
/bin/zsh -lc "sed -n '22390,22520p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Problem~\textup{\ref{op:multi-generator-universality}} in
the negative.
\end{theorem}

\begin{proof}
(i)~\emph{Per-channel universality.}
Each edge~$e$ of a stable graph~$\Gamma$ carries a single channel
assignment $\sigma(e) \in \{1, \ldots, r\}$. The \emph{diagonal}
graph sum restricts to those assignments where every edge carries
the same channel: $\sigma(e) = i$ for all~$e$. On such a
diagonal assignment, the amplitude of~$\Gamma$ factors as
$A_\Gamma(\sigma_i, \cA) = A_\Gamma(\cA_i)$, the single-channel
amplitude for the rank-$1$ chiral algebra~$\cA_i$ with curvature
$\kappa_i$ (the $i$-th per-channel component of
Theorem~\ref{thm:shadow-channel-decomposition}). Summing over
all~$i$ and all graphs:
\[
F_g^{\mathrm{diag}}(\cA)
\;=\;
\sum_{i=1}^r F_g(\cA_i)
exec
/bin/zsh -lc "sed -n '1790,1835p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The genus-$g$ bar-cobar inversion
$\Omega^{(g)}(\bar{B}^{(g)}(\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})))
\xrightarrow{\sim} \mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$
is a quasi-isomorphism at all genera.
\item The genus-$g$ complementarity
is expressed by
\[
Q_g(\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}}))
+ Q_g(\mathcal{W}^{k'}(\mathfrak{g}, f_{\mathrm{prin}}))
= H^*(\overline{\cM}_g,\, Z_{\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})}),
\]
holds unconditionally.
\item The scalar package
$\{\kappa(\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})),
\{F_g\}_{g \geq 1}\}$ and the spectral discriminant
$\Delta_{\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})}$
are unconditionally defined.
\end{enumerate}
This upgrades

thinking
**Evaluating mathematical proofs**

I'm looking at a proof that utilizes Theorems w-algebra-koszul-main and bar-cobar-spectral-sequence for MK1. It seems like that might be okay, but I need to take a closer look at the W theorem. There’s a lot to unpack and ensure everything aligns correctly. Let’s inspect the details to confirm the math holds up the way it should! It’s important to double-check these foundations, especially when they can be complex.
exec
/bin/zsh -lc "sed -n '309,420p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[\texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent; \ClaimStatusProvedHere]\label{thm:w-algebra-koszul-main}
\index{W-algebra@$\mathcal{W}$-algebra|textbf}
\textup{[Regime: filtered-complete \textup{(}DS reduction from curved-central KM;
Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\mathfrak{g}$ be a simple Lie algebra with dual Coxeter number $h^\vee$, and let $f = f_{\mathrm{prin}}$ be the principal nilpotent.
For $k \neq -h^\vee$, the W-algebra $\mathcal{W}^k(\mathfrak{g}) = \mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ admits a curved $A_\infty$ Koszul dual:
\begin{equation}\label{eq:w-koszul-main}
\mathcal{W}^k(\mathfrak{g})^! \simeq \mathcal{W}^{k'}(\mathfrak{g})
\end{equation}
where the dual level is the Feigin--Frenkel involution:
\begin{equation}\label{eq:ff-level-shift}
k' = -k - 2h^\vee
\end{equation}

The equivalence is of curved $A_\infty$ chiral algebras, and satisfies:
\begin{enumerate}
\item \emph{Involutivity.} $(k')' = -(-k-2h^\vee) - 2h^\vee = k$, so $(\mathcal{W}^!)^! \simeq \mathcal{W}$.
\item \emph{Critical fixed point.} The Feigin--Frenkel involution fixes
the critical level: if $k=-h^\vee$, then $k'=-k-2h^\vee=-h^\vee$.
exec
/bin/zsh -lc "rg -n \"label\\{def:chiral-koszul-pair\\}|chiral Koszul pair\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:600:The pair $(\cA, \cA^!)$ is a chiral Koszul pair
chapters/theory/higher_genus_modular_koszul.tex:12764:For a chiral Koszul pair $(\cA, \cA^!)$ with Verdier involution
chapters/theory/bar_cobar_adjunction_curved.tex:6695:$(\cA, \cA^\sharp)$ is a finite chiral Koszul pair. Then
chapters/theory/bar_cobar_adjunction_curved.tex:6753:\begin{theorem}[Recognition theorem for finite chiral Koszul pairs;
chapters/theory/bar_cobar_adjunction_curved.tex:6761:\item $(\cA,\cB)$ is a finite chiral Koszul pair.
chapters/theory/bar_cobar_adjunction_curved.tex:6780:required of a finite chiral Koszul pair.
chapters/theory/koszul_pair_structure.tex:94:Fix a chiral Koszul pair $(\cA, \cA^!)$ on a genus-$0$ curve and deform the curve to genus~$g \geq 1$. The bar construction
chapters/theory/koszul_pair_structure.tex:2422:Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth curve~$X$.
chapters/theory/koszul_pair_structure.tex:2508:For a chiral Koszul pair $(\cA, \cA^!)$ with $\cA = \AffKM{g}_k$,
chapters/theory/algebraic_foundations.tex:309:The full chiral Koszul pair is
chapters/theory/algebraic_foundations.tex:352:The chiral Koszul pair structure has three layers
chapters/theory/algebraic_foundations.tex:368:\item \emph{Theorem layer:} For a chiral Koszul pair
chapters/theory/existence_criteria.tex:132:Any broader module-category comparison for general chiral Koszul pairs
chapters/theory/higher_genus_foundations.tex:2572:for a chiral Koszul pair $(\cA_1, \cA_2)$
chapters/theory/higher_genus_foundations.tex:2587:\textup{For a chiral Koszul pair $(\cA_1, \cA_2)$, the bar-cobar
chapters/theory/higher_genus_foundations.tex:2590:Let $(\mathcal{A}_1, \mathcal{A}_2)$ be a chiral Koszul pair of chiral algebras on a
chapters/theory/higher_genus_foundations.tex:2673:For a chiral Koszul pair $(\mathcal{A}, \mathcal{A}^!)$ on a smooth projective curve~$X$,
chapters/theory/poincare_duality.tex:577:Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
chapters/theory/chiral_koszul_pairs.tex:103:property of a chiral Koszul pair, is checked by spectral sequence
chapters/theory/chiral_koszul_pairs.tex:634:\subsection{The concept of chiral Koszul pairs: precise formulation}
exec
/bin/zsh -lc "sed -n '642,715p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
\index{Koszul pair!chiral|textbf}
A \emph{chiral Koszul pair} on a smooth projective curve~$X$
is a pair of chiral Koszul data
\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
Definition~\textup{\ref{def:chiral-koszul-morphism})}
\[
(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
(\cA_2, \cC_2, \tau_2, F_\bullet)
\]
equipped with Verdier-compatible factorization-algebra
identifications
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
\qquad
\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
\]
compatible with the twisting morphisms and filtrations.
In this situation we write $\cA_2 \simeq \cA_1^!$ and
$\cA_1 \simeq \cA_2^!$.

thinking
**Investigating modular extension proof**

I need to verify if the modular extension is indeed proved within the same file. I’m considering searching for the modular version of the corollary, specifically `Corollary theta-twisting-morphism`, which appears to be chiral and not modular. However, the proof references an "extended to a modular setting" without citations, which feels like a hidden import that may relate to the user's question. I might need to cite `thm:convolution-master-identification` and check the context around the universal modular deformation theorem for clarity.
codex
I’m checking a second class of failures now: “extended to the modular setting” clauses that have no theorem backing them. Those are hidden imports even when every label exists.
exec
/bin/zsh -lc "rg -n \"Tw_\\\\alpha\\"'^'"\\{\\\\mathrm\\{mod\\}\\}|Tw_\\\\alpha\\"'^{mod}|modular setting|extended to the modular setting|convolution-master-identification|convolution-dg-lie-structure" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/algebraic_foundations.tex chapters/connections/concordance.tex -g '"'*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:universal-theta\\}|label\\{thm:cyclic-linf-graph\\}|label\\{thm:convolution-master-identification\\}|label\\{thm:convolution-dg-lie-structure\\}|label\\{prop:mc2-functoriality\\}|label\\{thm:mc2-bar-intrinsic\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12460,12540p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11390,11515p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Tw_\alpha\^\{\mathrm\{mod\}\}|Tw_\alpha\^{mod}|modular setting|extended to the modular setting|convolution-master-identification|convolution-dg-lie-structure)
                    ^^
error: unrecognized escape sequence
 succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:3574:\label{thm:universal-theta}
chapters/theory/higher_genus_modular_koszul.tex:3773:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:4408:\label{prop:mc2-functoriality}
chapters/theory/higher_genus_modular_koszul.tex:10247:\label{thm:convolution-dg-lie-structure}
chapters/theory/chiral_hochschild_koszul.tex:2613:complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
chapters/theory/algebraic_foundations.tex:522:\label{thm:convolution-master-identification}
 succeeded in 50ms:
\ell_\Gamma(f_1,\dots,f_k)
\;=\;
\mu_\Gamma\circ
\bigl(\alpha^{\mathrm{mod}}_\Gamma\otimes f_1\otimes\cdots\otimes f_k\bigr)
\circ
\Delta^{\log}_{\Gamma},
\end{equation}
and the Taylor coefficients of the modular $L_\infty$-structure are
\begin{equation}
\label{eq:graphwise-taylor-coefficients}
\ell_k^{(g)}
\;=\;
\sum_{\substack{
\Gamma\in \mathsf{Gr}^{\mathrm{st}}\\
|V(\Gamma)|=k,\;
b_1(\Gamma)+\sum_v g(v)=g}}
\frac{1}{|\operatorname{Aut}(\Gamma)|}\,
\ell_\Gamma.
\end{equation}
\end{construction}
 succeeded in 50ms:
$[o_{r+1}] \in H^2(F^{r+1}\gAmod/F^{r+2}\gAmod)$
controls extension to the next level. The four primitive
archetypes terminate at their respective depths: class~$\mathbf{G}$
at degree~$2$ (pure scalar), class~$\mathbf{L}$ at~$3$ (Lie bracket),
class~$\mathbf{C}$ at~$4$ (quartic contact), class~$\mathbf{M}$
at infinity (all obstructions non-vanishing).
The full element $\Theta_{\cA} = \varprojlim\Theta^{\leq r}$
is proved to exist by the bar-intrinsic construction
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.}%
\label{fig:shadow-postnikov-tower}
\end{figure}

%% FORCED TRANSITION: from tower to algebra.
%% The tower defines the MC element level by level.
%% To extract computable invariants, pass to cohomology.

The shadow obstruction tower defines $\Theta_\cA$ as an inverse limit
of truncated MC elements. Each truncation $\Theta_\cA^{\leq r}$
lives in the quotient $\gAmod / F^{r+1}$, an infinite-dimensional
dg~Lie algebra. To extract finite-dimensional invariants from this
exec
/bin/zsh -lc "sed -n '4445,4495p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathfrak{Q}, \ldots)$ are invariants of the
quasi-isomorphism class of~$\cA$.
\end{proposition}

\begin{proof}
\emph{Part~(i).} The bar-intrinsic construction defines
$\Theta_\cA := D_\cA - d_0^{(\cA)}$ and
$\Theta_\cB := D_\cB - d_0^{(\cB)}$.
By hypothesis, $f$ induces a coalgebra morphism
$\barB(f)\colon \barB(\cA) \to \barB(\cB)$ that
intertwines the genus-completed bar differentials:
$\barB(f) \circ D_\cA = D_\cB \circ \barB(f)$
(Theorem~\ref{thm:bar-functorial}).
The induced map $f_*$ on the convolution algebra is
post-composition with $\operatorname{End}(f)$, which
transports the codifferential $D_\cA$
(viewed as an element of $\gAmod$)
to $D_\cB$ (viewed in $\mathfrak{g}_\cB^{\mathrm{mod}}$).
Since $f_*$ also sends $d_0^{(\cA)}$ to $d_0^{(\cB)}$
(the genus-$0$ part is separately functorial),

thinking
**Evaluating algebra properties**

I'm thinking this proposition could relate to the homotopy invariance of shadow algebra with respect to filtered quasi-isomorphisms. I should verify if LV corollary 11.4.8 necessitates complete filtered sL∞. It seems like it might be alright if the context of the proposition already incorporates pronilpotent or completed structures. I need to inspect the preceding statement for clarity on this.
exec
/bin/zsh -lc "sed -n '4408,4455p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{prop:mc2-functoriality}
\index{MC2!functoriality|textbf}
\index{universal Maurer--Cartan class!functoriality}
The assignment $\cA \mapsto \Theta_\cA$ is functorial:
for every morphism $f\colon \cA \to \cB$ of modular Koszul
chiral algebras that is compatible with the augmentations,
invariant forms, and genus towers
\textup{(}i.e., a morphism of
$(\mathrm{D1})$--$(\mathrm{D6})$ data in
Definition~\textup{\ref{def:modular-koszul-chiral})}, the
induced map on convolution algebras
\begin{equation}\label{eq:mc2-functoriality}
f_*\colon
\mathfrak{g}_\cA^{\mathrm{mod}}
\;\longrightarrow\;
\mathfrak{g}_\cB^{\mathrm{mod}},
\qquad
\varphi \;\longmapsto\; f \circ \varphi,
\end{equation}
is a morphism of completed dg~Lie algebras satisfying:

thinking
**Evaluating potential issues**

I'm reviewing the content for potential issues. At point 15142, I see an analytic realization mentioned, which seems alright. The next reference at 15979 also looks fine regarding shadow-formality. However, at 16539, I notice a statement about verification tables that might need more clarity. Regarding point 16992, it discusses families being Koszul, but it's a bit vague. I think I should add explicit citations for free fields there. Let's check further around point 16956.
exec
/bin/zsh -lc "sed -n '16945,17005p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For lattice vertex algebras, the shadow--spectral correspondence
\textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
identifies the total shadow depth with $1$ plus the number of critical
lines of the constrained Epstein zeta. The total depth is unbounded:
every finite value $d \geq 2$ is realized by even unimodular
lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
arising from independent cusp forms in $M_{r/2}$
\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
new algebraic-shadow archetypes: for lattices one has
$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
\end{theorem}

\begin{proof}
Each case follows from the established vanishing theorems:

(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
coassociative ($m_k = 0$ for $k \geq 3$ in the transferred
$A_\infty$-structure), so all obstruction sources vanish
(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).

exec
/bin/zsh -lc "sed -n '25845,25890p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
prepotential (verified for $\cW_3$ in part~(v); expected for
general~$N$ from the free-field realization), identifies the shadow
CohFT with the $A_{N-1}$ Frobenius manifold CohFT.
The Witten conjecture~\cite{Witten93} (proved
by Faber--Shadrin--Zvonkine~\cite{FSZ10}) identifies the MC equations
with the $r$-KdV hierarchy; and
Pandharipande--Pixton--Zvonkine~\cite{PPZ19}
prove that $r$-spin relations generate the Pixton ideal.
For the semisimple upgrade: Givental--Teleman~\cite{Givental01,Teleman12}
reconstructs the unique CohFT from genus-$0$ data;
PPZ~\cite{PPZ19} proves any semisimple CohFT generates Pixton;
and the MC equations encode the full CohFT determination (the
CohFT is the unique solution of the MC system at all $(g,n)$).
\end{proof}

\begin{conjecture}[Pixton ideal from shadow obstruction towers]
\label{conj:pixton-from-shadows-hgmk}
\ClaimStatusConjectured
\index{Pixton ideal!from shadow obstruction towers|textbf}
\index{shadow obstruction tower!Pixton ideal generation}

thinking
**Inspecting theorem context**

I think there's some conjectural evidence here that might be fine, but there’s a potential issue with proof 18, starting with the integral notation and mentioning "Theorem D" without a citation. I feel like I need to inspect the context around line 26970 to clarify this. Maybe it involves the concordance theorem, but usually, they’d reference the theorem in the .tex file. There's a chance of a hidden import making it ambiguous. It seems important to examine this!
exec
/bin/zsh -lc "sed -n '26965,26990p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Shadow obstruction tower and DT curve counting;
 \ClaimStatusProvedHere]
\label{thm:shadow-dt-curve-counting}
\index{shadow tower!DT invariants}
For $\cA$ on $C \subset \operatorname{Tot}(K_C)$
\textup{(}uniform-weight; unconditional at $g = 1$\textup{):}
\begin{equation}\label{eq:shadow-dt-degree1}
F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
\textup{(}UNIFORM-WEIGHT\textup{)}.
\end{equation}
Higher-degree corrections correspond to higher curve-class
contributions: cubic shadow $\to$ degree~$2$,
quartic $\to$ degree~$3$.
\end{theorem}

\begin{proof}
$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
GV integrality gives $n_0^{d=1} = 1$.
\end{proof}
exec
/bin/zsh -lc "sed -n '30520,30542p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\tfrac{1}{2}[\Theta_\cA,\Theta_\cA]_{g,2}$
splits by clutching
(Theorem~\ref{thm:mc2-bar-intrinsic}(iii))
into separating and non-separating contributions, recovering
the complementarity sum. Verdier duality interchanges
$L^+_\cA$ and~$L^-_\cA$, giving $Q_g(\cA) + Q_g(\cA^!)
= H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
Full detail: Theorem~\ref{thm:quantum-complementarity-main}.

\smallskip\noindent
\emph{(D).}
Universality and the duality constraint are properties~(i) and~(iv)
of Theorem~\ref{thm:mc2-bar-intrinsic}; additivity is
Proposition~\ref{prop:independent-sum-factorization};
the generating function identity
$\sum_{g \geq 1} F_g\,\hbar^{2g}
= \kappa(\cA)\bigl[\widehat{A}(i\hbar)-1\bigr]$
follows from $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$.
Full detail: Theorem~\ref{thm:modular-characteristic}.


thinking
**Managing theorem attention**

I'm thinking about creating a shorter list of theorems that need my focus. First, there's the issue with theorem 710-712 regarding free fermion and the beta-gamma model. Then for 764-766, I might need to consider using theorem `thm:w-algebra-koszul-main` and `thm:bar-cobar-spectral-sequence`. I should verify the appropriate theorem for the collapse at E2 and diagonal concentration. The situation is tricky because the bar-cobar spectral sequence constructs but doesn’t collapse, so I'll need to double-check the details.
codex
I’ve isolated another likely bad import: the `\mathcal W` proof cites the spectral-sequence construction theorem, but MK1 needs collapse/diagonality, not just existence of a spectral sequence. I’m reading that lane now to see whether there is a stronger theorem already available and should replace the citation.
exec
/bin/zsh -lc "rg -n \"spectral-sequence-collapse|bar-cobar-spectral-sequence|collapse at E_2|diagonal|Koszul\" chapters/examples/w_algebras.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2270,2365p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5730,5795p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1800,1845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1186

chapters/examples/w_algebras.tex:1:\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
chapters/examples/w_algebras.tex:17:rank amplifies every feature. None of these is Koszul in any
chapters/examples/w_algebras.tex:34:at dual levels is a Koszul-type involution whose intertwining with
chapters/examples/w_algebras.tex:39:Drinfeld--Sokolov reduction is itself a Koszul functor, reducing
chapters/examples/w_algebras.tex:43:\index{W-algebra@$\mathcal{W}$-algebra!as modular Koszul family}
chapters/examples/w_algebras.tex:67:Koszul dual & $\mathrm{Vir}_{26-c}$
chapters/examples/w_algebras.tex:72:Koszul self-dual point &
chapters/examples/w_algebras.tex:75: Non-formal (all $\ell_k^{\mathrm{tr}} \neq 0$; chirally Koszul) &
chapters/examples/w_algebras.tex:76: Non-formal (chirally Koszul) \\
chapters/examples/w_algebras.tex:82:The modular Koszul triples
chapters/examples/w_algebras.tex:105:DS reduction sends the Koszul pair
chapters/examples/w_algebras.tex:112:modular Koszul triples
chapters/examples/w_algebras.tex:114:Koszul dual, and collision $r$-matrix all transfer.
chapters/examples/w_algebras.tex:231:The off-diagonal vanishing follows from conformal weight:
chapters/examples/w_algebras.tex:260:where $\rho_\cA$ is the Koszul radius, measures the rate
chapters/examples/w_algebras.tex:304:The sixth-order pole in the $W \times W$ OPE places this beyond quadratic Koszul duality.
chapters/examples/w_algebras.tex:307:\subsection{\texorpdfstring{Curved $A_\infty$ Koszul duality}{Curved A-infinity Koszul duality}}
chapters/examples/w_algebras.tex:309:\begin{theorem}[\texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent; \ClaimStatusProvedHere]\label{thm:w-algebra-koszul-main}
 succeeded in 50ms:
\subsection{The fundamental theorem for chiral Koszul pairs}

\begin{remark}[General chiral module-category duality remains frontier]
\label{rem:module-category-frontier}
The broad ordinary-derived package for a general
chiral Koszul pair $(\cA_1,\cA_2)$
\textup{(}derived equivalence, Ext exchange with derived Hom on the
bar-comodule side and finite-type Tor reformulations, simple/projective
transport, and Hochschild transport\textup{)}
is \emph{not} proved on this general surface. The earlier bar-cobar
machinery in Part~\ref{part:bar-complex} gives the intrinsic bar-coalgebra comparison, and
the manuscript's proved ordinary module-level statement is the later
$\Eone$ theorem
Theorem~\ref{thm:e1-module-koszul-duality}, restricted to the
quadratic genus-$0$ complete/conilpotent lane.

Any extension of that package to arbitrary chiral Koszul pairs would
require extra hypotheses and a module-level comparison theorem beyond
what is currently established here.
\end{remark}
 succeeded in 52ms:
\[E_0^{p,q} = F^p\Omega^{p+q}(\bar{B}(\mathcal{A})) / F^{p+1}\Omega^{p+q}(\bar{B}(\mathcal{A}))\]

By definition of the filtration, this isolates the piece in cobar degree~$p$ and total degree $p+q$.

\emph{Step 2: $d_0$ differential.} On the $E_0$ page:
\[d_0: E_0^{p,q} \to E_0^{p,q+1}\]
is the bar complex differential $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$, lifted to each cobar tensor factor. This is the filtration-preserving component of $d$: both $d_{\text{internal}}$ (from the differential on~$\mathcal{A}$) and $d_{\text{bar}}$ (from the multiplication of~$\mathcal{A}$, encoding collisions) preserve cobar degree.

Taking cohomology gives the $E_1$ page: bar cohomology at each fixed cobar degree.

\emph{Step 3: $d_1$ differential.} On the $E_1$ page:
\[d_1: E_1^{p,q} \to E_1^{p+1,q}\]
is induced by $d_{\text{cobar}}$ (the comultiplication on $\bar{B}(\mathcal{A})$, which increases cobar degree by~$1$).

Taking cohomology gives the $E_2$ page.

\emph{Step 4: Higher differentials.} For $r \geq 2$:
\[d_r: E_r^{p,q} \to E_r^{p+r,q-r+1}\]

These differentials encode higher-order interactions between bar and cobar operations.
 succeeded in 50ms:
= H^*(\overline{\cM}_g,\, Z_{\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})}),
\]
holds unconditionally.
\item The scalar package
$\{\kappa(\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})),
\{F_g\}_{g \geq 1}\}$ and the spectral discriminant
$\Delta_{\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})}$
are unconditionally defined.
\end{enumerate}
This upgrades
Proposition~\textup{\ref{prop:conditional-modular-koszul}}
for the higher $\mathcal{W}_N$ family, and more generally for
principal finite-type $\mathcal{W}$-algebras,
from conditional to unconditional.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorems~\ref{thm:w-algebra-koszul-main}
and~\ref{thm:bar-cobar-spectral-sequence}.

thinking
**Exploring concentration theorems**

I need to consider diagonal concentration as well, and I think the spectral-sequence-collapse theorem could be useful once I establish that A is Koszul via the w theorem. It makes sense to fix the citation to the w theorem, as combining it with spectral-sequence-collapse might provide a stronger argument. I should also look into the bar concentration theorem, referred to as `thm:bar-concentration`, to help with diagonal bigrading concentration. I'll search for the statement of that theorem.
exec
/bin/zsh -lc "sed -n '1132,1175p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
\label{thm:bar-concentration}
\index{bar complex!concentration}
\textup{[Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
Then the augmented bar complex $\bar{B}^{\mathrm{ch}}(\cA_1)$,
equipped with its bigrading by bar degree~$p$ and bar-differential
cohomological degree~$q$, satisfies:
\[
H^{p,q}(\bar{B}^{\mathrm{ch}}(\cA_1)) = 0
\quad\text{for } q \neq 0,
\qquad
H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
\]
% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
% $\cA_2 = \cA_1^!$ creates a notational double-dual. The intended meaning
% is the bar cohomology of $\cA_1$, i.e.\ $\cA_1^i = H^*(\barBch(\cA_1))$

thinking
**Exploring mathematical concepts**

I’m realizing that nonquadratic aspects might not apply, which could be an issue. The spectral-sequence-collapse theorem deals with quadratic conditions. The W theorem discusses curved A∞ duality but isn't strictly about bar concentration. I think I should check for a completed Koszul corollary in the w_algebras chapter related to explicit completed Koszulity. There might be something useful in the target file regarding MK1 and its genus-0 Koszulity of the chiral pair, even if it’s not strictly quadratic. Let’s search that label!
exec
/bin/zsh -lc "sed -n '6470,6565p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
that is multiplicative and compatible with~$\partial$ is
\emph{filtered-complete}. Its \emph{completed reduced bar complex}
$\widehat{\overline{B}}(A)$ is the completion of the usual reduced
bar complex with respect to the induced filtration by total
$F$-degree.
\end{definition}

\begin{definition}[Completed Koszulity]
\label{def:w-completed-koszulity}
\index{completed Koszulity!definition}
A filtered-complete chiral algebra~$A$ is \emph{completed Koszul} if
the homology of $\widehat{\overline{B}}(A)$ is concentrated on the
diagonal with respect to bar grading and induced filtration grading,
equivalently if the completed cobar of this homology reconstructs $A$
up to filtered quasi-isomorphism.
\end{definition}

\begin{theorem}[PBW--Slodowy collapse; \ClaimStatusProvedHere]
\label{thm:w-pbw-slodowy-collapse}
\index{PBW--Slodowy collapse}
exec
/bin/zsh -lc "sed -n '6565,6605p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
The Kostant slice $\mathcal{S}_{\mathrm{prin}}
= f_{\mathrm{prin}} + \mathfrak{g}^e$ is affine, hence
\[
\mathbb{C}[J\mathcal{S}_{\mathrm{prin}}]
\cong \operatorname{Sym}_\partial\bigl((\mathfrak{g}^e)^*\bigr).
\]
Apply Theorem~\ref{thm:w-pbw-slodowy-collapse} with
$V = (\mathfrak{g}^e)^*$.
\end{proof}

\begin{remark}[Extension to arbitrary nilpotent data]
\label{rem:w-arbitrary-nilpotent-completed-koszul}
\index{completed Koszulity!arbitrary nilpotent}
The same argument applies to
$\mathcal{W}^k(\mathfrak{g}, f)$ whenever
$\operatorname{gr}_{\mathrm{Li}} \mathcal{W}^k(\mathfrak{g}, f)
\cong \mathbb{C}[J\mathcal{S}_f]$
with $\mathcal{S}_f = f + \mathfrak{g}^e$ affine. Since every
Slodowy slice is affine, the completed-Koszul problem for general

thinking
**Inspecting chiral Koszulness**

I need to inspect the context around this theorem and see if it relates to chiral Koszulness. Could it really be that this theorem gives insight here? I think I’ll focus on the years 1045 to 1070 to gather more information. I want to make sure I'm thorough in understanding the implications of this theorem and its surrounding context. There's a lot to consider, and I’m curious about how it all fits together!
exec
/bin/zsh -lc "sed -n '1038,1072p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
axiom~\textup{MK3}
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
unconditionally at genus~$1$:
they are modular pre-Koszul at~$g = 1$.
\end{theorem}

\begin{proof}
We carry out the genus-$1$ Kac--Moody argument directly, using
enrichment factorization, Whitehead acyclicity, and the
level-$k$ Killing contraction.

\medskip
\emph{Step~1: Decomposition of the $E_1$ page.}

Equip $\bar{B}^{(1)}(\widehat{\fg}_k)$ with the PBW filtration
by conformal weight, as in
Theorem~\ref{thm:pbw-koszulness-criterion}.
The leading PBW differential $d_0^{\mathrm{PBW}}$ is the
commutative bar differential of the associated graded
$\operatorname{Sym}^{\mathrm{ch}}(V)$, $V = \fg \otimes
exec
/bin/zsh -lc "sed -n '2088,2148p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{theorem}[PBW propagation: MK1 implies MK3;
 \ClaimStatusProvedHere]\label{thm:pbw-propagation}
\index{PBW spectral sequence!propagation theorem|textbf}
\index{MK3!follows from MK1|textbf}
\index{modular Koszul chiral algebra!MK3 redundancy|textbf}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra satisfying \textup{MK1}
\textup{(}genus-$0$ Koszulity,
Definition~\textup{\ref{def:modular-koszul-chiral})} and
hypotheses~\textup{(a)--(b)} of
Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
\textup{(}positive conformal grading with unique
weight-$2$ stress tensor\textup{)}.
Then axiom~\textup{MK3} holds: for every genus~$g \geq 1$,
\[
E_\infty(g) = E_\infty(0).
\]
exec
/bin/zsh -lc "sed -n '10052,10090p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Proposition~\ref{prop:tautological-line-support-criterion}
would recover $o_g=\kappa\lambda_g$.
At present this remains a route, not a completed independent proof,
for arbitrary multi-weight families.
\end{remark}

\begin{corollary}[MC2 comparison gauntlet collapses on the proved
scalar lane; \ClaimStatusProvedHere]
\label{cor:mc2-single-hypothesis}
\index{MC2!single-hypothesis reduction}
Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
for a modular Koszul chiral algebra $\cA$ with simple Lie
symmetry~$\mathfrak{g}$ by the bar-intrinsic construction.
On the proved uniform-weight lane, the explicit comparison route of
Theorem~\textup{\ref{thm:mc2-conditional-completion}} reduces to the
single remaining input
\textup{(}Hypothesis~\textup{\ref{mc2-hyp:cyclic}}\textup{)},
because MC2-2 is supplied by
Proposition~\textup{\ref{prop:geometric-modular-operadic-mc}} and
MC2-3 by Theorem~\textup{\ref{thm:tautological-line-support}}.
exec
/bin/zsh -lc "sed -n '13498,13525p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 modular cooperad structure on
 $\{C_\bullet(\operatorname{FM}_{g,n}^{\log})\}_{g,n}$,
 with higher cocomposition homotopies controlled by the
 codimension-$2$ strata of Mok's snc boundary
 \textup{(}\cite[Theorem~3.3.1]{Mok25}\textup{)}.
\end{enumerate}
\end{theorem}

\begin{proof}
Part~(i): the cutting correspondences are compositions of Mok's
proper birational modifications
$\operatorname{FM}_n(W/B)(\rho) \to
\prod_{v \in V(S_\rho)} \operatorname{FM}_{I_v}(Y_v | D_v)$
(\cite[Corollary~5.3.4]{Mok25}).
Coassociativity follows from the compatibility of rigid types under
iterated degeneration: the transversality of Mok's snc boundary
ensures that composing two cutting correspondences along compatible
edges gives the cutting correspondence for the combined rigid type.
Part~(ii) follows from the general principle that chains on a
manifold-with-corners stratification carry a homotopy cooperad
exec
/bin/zsh -lc 'rg -n "by Theorem|by Proposition|by Lemma" chapters/theory/higher_genus_modular_koszul.tex -C 2' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
654-\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
655-The definition separates \emph{hypotheses} (MK1--MK3) from
656:\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
657-There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
658-\ref{MK:koszul-htpy}, \ref{MK:verdier-htpy},
--
710-MK1 (genus-0 Koszulity) by
711-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
712:MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
713-MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
714-only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
--
764-Theorems~\ref{thm:w-algebra-koszul-main}
765-and~\ref{thm:bar-cobar-spectral-sequence};
766:MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
767:MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
768-Inversion and complementarity follow as consequences.
769-\end{proof}
--
1063-$d_0^{\mathrm{PBW}}$ extracts Poincar\'{e} residues at
codex
I’m now on the uncited “follows from” sites that compress several prerequisites into one sentence. Those are the easiest places for hidden imports to survive, so I’m checking whether they can be replaced by exact theorem names instead of family-level handwaving.
exec
/bin/zsh -lc "rg -n \"lattice.*Koszul|label\\{thm:lattice|label\\{thm:fermion|label\\{thm:betagamma|label\\{thm:free-field|label\\{thm:heisenberg-bar\\}|label\\{thm:heisenberg-bar-complete\\}|label\\{thm:betagamma-global-depth\\}|label\\{prop:pbw-universality\\}\" chapters/examples chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16984,17002p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

(iv)~For Virasoro, the cubic and quartic shadows coexist, and their
Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
generic $c$
(Theorem~\ref{thm:w-virasoro-quintic-forced}); the all-degree master
equation (Theorem~\ref{thm:nms-all-degree-master-equation}) then
forces all higher obstructions to be non-zero by induction.

That all four families are Koszul follows from
Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
for affine and W-algebras, and from the diagonal
Ext-vanishing criterion
(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
Heisenberg, lattice, and $\beta\gamma$.
\end{proof}

% ========================================================
% SHADOW ARCHETYPE CLASSIFICATION DIAGRAM
% ========================================================
 succeeded in 52ms:
chapters/examples/lattice_foundations.tex:107:\ClaimStatusProvedHere]\label{thm:lattice-sewing}%
chapters/examples/lattice_foundations.tex:542:\label{thm:lattice:e1-vs-einf}
chapters/examples/lattice_foundations.tex:607:\begin{theorem}[Frenkel--Kac--Segal; \ClaimStatusProvedElsewhere{} \cite{FK80,Se81}]\label{thm:lattice:frenkel-kac}
chapters/examples/lattice_foundations.tex:761:\label{thm:lattice:bar-structure}
chapters/examples/lattice_foundations.tex:916:\begin{theorem}[Unimodular lattice self-duality; \ClaimStatusProvedHere]\label{thm:lattice:unimodular-self-dual}
chapters/examples/lattice_foundations.tex:918:Let $\Lambda$ be an even unimodular lattice. Then $\Vlat_\Lambda$ is Koszul self-dual:
chapters/examples/lattice_foundations.tex:928:The bar-cobar QI follows from Theorem~\ref{thm:lattice:koszul-morphism}: the twisting morphism $\tau$ is Koszul, so $\Omega^{\mathrm{ch}}(\barBgeom(\Vlat_\Lambda)) \xrightarrow{\sim} \Vlat_\Lambda$.
chapters/examples/lattice_foundations.tex:950:\label{thm:lattice:koszul-dual}
chapters/examples/lattice_foundations.tex:1001:\label{thm:lattice:koszul-morphism}
chapters/examples/lattice_foundations.tex:1109:\begin{remark}[Structural form of the lattice Koszul dual]
chapters/examples/lattice_foundations.tex:1243:\label{thm:lattice:direct-sum}
chapters/examples/lattice_foundations.tex:1342:\begin{theorem}[Overlattice vertex algebra \cite{FLM88}; \ClaimStatusProvedElsewhere]\label{thm:lattice:overlattice}
chapters/examples/lattice_foundations.tex:1481:and~\ref{thm:lattice:koszul-dual}), so the Koszul duality theory
chapters/examples/lattice_foundations.tex:1493:\begin{theorem}[Lattice chiral Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:lattice:hochschild}
chapters/examples/lattice_foundations.tex:1603:\begin{theorem}[Modular invariance; \ClaimStatusProvedHere]\label{thm:lattice:modular-invariance}
chapters/examples/lattice_foundations.tex:1677:\label{thm:lattice:niemeier-shadow-universality}%
chapters/examples/lattice_foundations.tex:1783:\label{thm:lattice:niemeier-siegel-genus2}%
chapters/examples/lattice_foundations.tex:1953: (Theorem~\ref{thm:lattice:bar-structure}). The Koszul dual is
chapters/examples/lattice_foundations.tex:1977:\section{Catalog of lattice Koszul dual pairs}\label{sec:lattice:catalog}
chapters/examples/lattice_foundations.tex:1979:The lattice engine produces Koszul dual pairs for every even lattice.
exec
/bin/zsh -lc "rg -n \"label\\{thm:shadow-spectral-correspondence\\}|label\\{thm:fermion-bar-complex-genus-0\\}|label\\{thm:betagamma-bc-koszul\\}|label\\{cor:w-principal-completed-koszul\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11105,11140p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/free_fields.tex:885:\label{thm:fermion-bar-complex-genus-0}
chapters/examples/free_fields.tex:1706:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality; \ClaimStatusProvedHere]\label{thm:betagamma-bc-koszul}
chapters/examples/w_algebras.tex:6549:\label{cor:w-principal-completed-koszul}
chapters/connections/arithmetic_shadows.tex:197:\label{thm:shadow-spectral-correspondence}
 succeeded in 51ms:
 $\varphi_1 = \operatorname{id}$,
 $\varphi_2 = 0$ (the strict model has trivial ternary bracket),
 $\varphi_3 = h_*$ (determined by the contracting homotopy $h$ on
 $C_*(\overline{\cM}_{0,4})$ through the homotopy transfer
 theorem). The general component $\varphi_n$ is determined by the
 contracting homotopy on $C_*(\overline{\cM}_{0,n+1})$ through the
 sum over trivalent trees with $n$ leaves
 \textup{(}Construction~\textup{\ref{constr:explicit-convolution-linfty})}.
\item \emph{One-slot constraint.}
 The functoriality of~(v) operates on one slot at a time
 \cite[Theorem~6.6]{RNW19}.
 Simultaneous replacement of both the coalgebra and algebra
 inputs requires sequential application: first the coalgebra
 replacement $C \leadsto C'$ \textup{(}holding $\operatorname{End}_\cA$
 fixed\textup{)}, then the algebra replacement
 $\operatorname{End}_\cA \leadsto \operatorname{End}_{\cA'}$
 \textup{(}holding $C'$ fixed\textup{)}.
 This suffices for all constructions in the monograph, since
 the Koszul duality functor $\cA \mapsto \cA^!$ acts only on the
 algebra slot while the moduli coalgebra is held fixed.

thinking
**Searching for examples in theorem**

I think replacing vague criteria with explicit examples in Issue 16992 could be really helpful. I'm considering looking for a lattice theorem that proves Koszulness. It might be best to search using "lattice:koszul-morphism" to see what I can find. Let's inspect and see if I can discover something useful for clarity on this topic!
exec
/bin/zsh -lc "sed -n '980,1035p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
has structure constants $\varepsilon(\alpha,\beta)$ from the group
algebra multiplication $e^\alpha \cdot e^\beta =
\varepsilon(\alpha,\beta)\,e^{\alpha+\beta}$.
The dual coalgebra is extracted from the bar complex
$\bar{B}^{\mathrm{ch}}(\Vlat_\Lambda^\varepsilon)$. In the bar construction,
each tensor factor is desuspended by $s^{-1}$, and the bar differential
involves the product $\mu$ composed with Koszul signs from the
desuspension. For the lattice algebra, where $\mu(e^\alpha \otimes
e^\beta) = \varepsilon(\alpha,\beta)\,e^{\alpha+\beta}$ with
$|\varepsilon(\alpha,\beta)| = \pm 1$, the desuspension introduces a
sign $(-1)^{|\alpha||\beta|}$ that, combined with the bilinearity of
$\varepsilon$, produces the cocycle inversion:
the bar-complex coproduct has structure constants
$\varepsilon(\alpha,\beta)^{-1}$.
Since $\varepsilon^{-1}$ is again a valid cocycle,
$(\Vlat_\Lambda^{\varepsilon^{-1}})^c$ is a valid coalgebra, and the
dual coalgebra is identified with it; the dual algebra is then obtained
by linear/Verdier duality.
\end{proof}


thinking
**Evaluating theorem references**

I notice that Theorem D isn't labeled in the file, but there’s a concordance summary for it. I should probably replace it with `Theorem\ref{thm:modular-characteristic}`. Also, the statement about all four families being Koszul could use some precision. I think I need to look into the statement of theorem `pbw-universality` to determine if it applies to W and affine. It seems like a good idea to do a search on that.
exec
/bin/zsh -lc "sed -n '1380,1415p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$d_r$ ($r \geq 2$) to vanish, since a $d_r$-differential shifts
the bigrading by $(r, 1-r)$, producing off-diagonal classes
that contradict~$\operatorname{Ext}^{p,q} = 0$ for $p \neq q$.
Hence $E_2$-collapse, hence Koszulness.
\end{proof}

\begin{proposition}[PBW universality; \ClaimStatusProvedHere]
\label{prop:pbw-universality}
\index{Koszul property!PBW universality}
\index{vertex algebra!freely strongly generated}

A vertex algebra~$\cA$ is \emph{freely strongly generated} if it
admits strong generators $\{a^i\}_{i \in I}$ whose normally ordered
monomials
$:\!\partial^{n_1} a^{i_1} \cdots \partial^{n_r} a^{i_r}\!:$
form a PBW basis; equivalently,
$\operatorname{gr}_F \cA \cong \operatorname{Sym}^{\mathrm{ch}}(V)$
where $V$ is the $\cD_X$-module spanned by the generators.

Every freely strongly generated vertex algebra is chirally Koszul.
exec
/bin/zsh -lc "sed -n '16895,16960p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
 Affine Kac--Moody $V_k(\fg)$ at generic level.
 The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
 \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
 quartic obstruction $o_4 = 0$ by the Jacobi identity.

\item \emph{Contact \textup{(}$\mathbf{C}$,
$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
 the conformal-weight family $\beta\gamma_\lambda$
 \textup{(}and its $bc$ dual\textup{)}.
 The class-$\mathbf{C}$ witness is not the weight-changing line and
 not the $T$-line: on the full family one has
 \[
  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
  S_3 = 0,\qquad
  S_4 = -5/12,\qquad
  S_r = 0 \quad (r \geq 5).
 \]
 Thus the charged quartic contact class is nonzero and is the last
 non-vanishing shadow component; the quintic obstruction vanishes by
exec
/bin/zsh -lc "sed -n '10235,10330p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The strict model suffices for all Maurer--Cartan computations in
this monograph
\textup{(}Remark~\textup{\ref{rem:full-homotopy-why})}.
The homotopy-invariant object $\Definfmod(\cA)$ is needed when
passing to quasi-isomorphic replacements, minimal models, or
different choices of contracting homotopy
\textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution}},
Corollary~\textup{\ref{cor:strictification-comparison})}.
\end{remark}

\begin{theorem}[dg~Lie structure from the modular operad;
\ClaimStatusProvedHere]
\label{thm:convolution-dg-lie-structure}
\index{modular convolution dg Lie algebra!structure}
The strict dg~Lie structure on the modular convolution algebra
$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Differential.}
 The differential $D$ has five components
 \textup{(}matching Remark~\textup{\ref{rem:five-pieces}};
exec
/bin/zsh -lc "sed -n '11070,11135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the shadow obstruction tower ($o^{(r)}_{\mathrm{Vir}}\neq 0$ for all
$r\geq 5$).
\end{proof}

\begin{corollary}[Strictification comparison;
\ClaimStatusProvedHere]
\label{cor:strictification-comparison}
\index{strictification comparison}
All dg~Lie algebras in this monograph are functorial strict models
of the corresponding homotopy-invariant $L_\infty$-algebras, and
all bar-complex constructions are computations in a chosen
strictification. In particular:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\mathfrak{g}_{\cA}^{\mathrm{mod}} =
 \Convstr\!\bigl(\{C_*(\overline{\cM}_{g,n})\},
 \operatorname{End}_{\cA}\bigr)$ is a strict model of
 $\Definfmod(\cA)$.
\item $\Defcyc^{\mathrm{mod}}(\cA)$ is a strict model via the
 coderivation identification.
\item For affine Kac--Moody algebras at non-critical level, the
exec
/bin/zsh -lc "sed -n '14034,14050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
from $\mathfrak{K}_\cA$ by the Feynman transform and its
successive projections.
\end{remark}

\begin{remark}[Homotopy invariance of primitive data]
\label{rem:primitive-kernel-homotopy-invariance}
The primitive kernel $\mathfrak{K}_\cA$ is invariant up to gauge
equivalence under $\infty_\alpha$-quasi-isomorphisms of chiral
algebras: this follows from
Theorem~\ref{thm:shadow-homotopy-invariance} (homotopy invariance
of the shadow algebra) and
Corollary~\ref{cor:deformation-functoriality} (deformation
functoriality), since the primitive kernel is the restriction of
the MC element to the primitive subspace, and MC moduli are
invariant under one-slot $\infty$-morphisms
by~\cite[\S8]{RNW19}.
\end{remark}

thinking
**Checking theorem labeling**

I'm considering whether theorem labels or statuses might be necessary. Since I’m not creating new labels but citing existing ones, they might not be needed. However, I could mention verification reasoning in my commentary. I’m also thinking about running a more comprehensive automated search for any suspicious generic phrases like "Theorem D," "proved above," or "extended to modular setting," as well as any improper theorems within the file. Let’s see where that leads!
exec
/bin/zsh -lc "rg -n \"Theorem~D|proved above|extended to the modular setting|for Heisenberg, lattice, and \\\\beta\\\\gamma|heisenberg-bar-complete|bar-cobar-spectral-sequence\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Theorem~D|proved above|extended to the modular setting|for Heisenberg, lattice, and \beta\gamma|heisenberg-bar-complete|bar-cobar-spectral-sequence)
                                                                                                ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "Theorem~D" chapters/theory/higher_genus_modular_koszul.tex && rg -n -F "proved above" chapters/theory/higher_genus_modular_koszul.tex && rg -n -F "extended to the modular setting" chapters/theory/higher_genus_modular_koszul.tex && rg -n -F "for Heisenberg, lattice, and $'"\\\\beta\\\\gamma"'$" chapters/theory/higher_genus_modular_koszul.tex && rg -n -F "heisenberg-bar-complete" chapters/theory/higher_genus_modular_koszul.tex && rg -n -F "bar-cobar-spectral-sequence" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
2364:\item Theorem~D \textup{(}modular characteristic
2993:\begin{remark}[Proof routing for Theorem~D;
3036:Theorem~D which does not use the shadow tower, the
3087:Theorem~D, using only the family of fiber bar complexes and Hodge
4303: \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
4357:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
5511:of Theorem~D$_{\mathrm{scal}}$
9854:Theorem~D establishes that $\kappa$ exists as a universal
9874:Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
10118:Theorem~D$_{\mathrm{scal}}$
10125:Theorem~D$_\Delta$
10166:Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
12283: \quad(the modular characteristic, Theorem~D);
12538: \quad(the modular characteristic, Theorem~D);
14315:Theorem~D
14876:Theorem~D extracts the scalar $\kappa$ from the spectral $r$-matrix;
14997:modular characteristic (Theorem~D).
15421: Theorem~D\textup{)}.
15442:curvature $\kappa(\cA)$ by definition (Theorem~D).
22663:hypothesis from Theorem~D and C2]



thinking
**Evaluating theorem references**

I’m noticing that many references to Theorem D are present. Not all of them seem problematic, but if a theorem lane is labeled as Theorem D, it might be okay. However, the specific proof at line 26984 uses Theorem D, and maybe that should remain. There are many "proved above" mentions, but only one seems relevant within conjecture. Also, I should check that search command since it might have not run properly due to how it’s structured. I might need to inspect line 2364, too.
thinking
**Inspecting theorem routing**

I’m considering if there could be a local reference for "Proof routing for Theorem D." It might be an issue if some singular lines are referencing Theorem D. The user likely prefers hidden imports rather than explicitly naming theorem packages. Line 26984 in the proof seems a bit shorthand, so maybe I could run a script to check references in lines containing `Theorem\ref`, `Proposition\ref`, and `Lemma\ref`. We've identified some semantic mismatches, and I still need to find one more reference regarding `Theorems\ref{heisenberg-bar-complete}` and `\ref{km-chiral-koszul}`.
thinking
**Considering theorem citations**

I think I need to cite the theorem for free fermion genus expansions, not just MK1. It seems like MK3 mentions that "for (b) the free-field genus expansion is explicit" in section free-field-genera. But I’m wondering if that’s an insufficient hidden import since it’s in a section rather than a formal theorem. It could be important to clarify this to ensure everything is properly referenced and accounted for.
exec
/bin/zsh -lc "sed -n '200,255p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{proposition}

\begin{proof}
Part~(i) is a direct application of genus universality
(Theorem~\ref{thm:genus-universality}).
Part~(ii) is the standard result from the
Quillen determinant line bundle computation \cite{Quillen85}
(\ClaimStatusProvedElsewhere).
Part~(iii) follows from the triviality of the
canonical bundle on an elliptic curve.
\end{proof}

\section{Lattice VOAs at all genera}\label{sec:lattice-genera}
\index{lattice VOA!genus expansion}

The Heisenberg genus expansion (\S\ref{sec:frame-genus-tower}) treats a single free boson. A lattice VOA $V_\Lambda$ tensors $d$ copies of $\mathcal{H}_1$ with $\mathbb{C}[\Lambda]$; lattice shifts leave $\kappa$ unchanged, so the genus expansion follows immediately.

\begin{theorem}[Lattice VOA free energy;
\ClaimStatusProvedHere]\label{thm:lattice-all-genera}

thinking
**Searching genus expansion theorem**

I'm considering searching for the genus expansion theorem related to fermions. It seems like an intricate topic, and I want to dig into it further. I need to clarify my approach and ensure I'm looking at the right materials to understand this better. It might also help to see examples or applications related to this theorem. Okay, let's go ahead and look for more information on this!
exec
/bin/zsh -lc "sed -n '2380,2425p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is a fermionic chiral algebra with central charge
$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
(Computation~\ref{comp:beta-gamma-central-charges}).
Its Koszul dual is the bosonic $\beta\gamma$-system at the same
weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)
= -c_{bc}$, and the underlying operadic duality is
$\mathrm{Ext} \leftrightarrow \mathrm{Sym}$
(Theorem~\ref{thm:fermion-boson-koszul}).

\begin{theorem}[Free fermion free energy at all genera;
\ClaimStatusProvedHere]\label{thm:fermion-all-genera}
\index{free fermion!obstruction coefficient}
For the $bc$ system at conformal weights $(\lambda, 1-\lambda)$,
the genus-$g$ free energy is
\begin{equation}\label{eq:fermion-Fg-bc}
F_g(bc_\lambda) = \kappa(bc_\lambda) \cdot
\frac{2^{2g-1}-1}{2^{2g-1}} \cdot
\frac{|B_{2g}|}{(2g)!}
\end{equation}
for all $g \geq 1$, where the obstruction coefficient is
exec
/bin/zsh -lc "sed -n '4180,4225p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{tabular}
\end{center}
The ratio to the Heisenberg values
\textup{(}Table~\textup{\ref{tab:free-energy-values})} is
$F_g(\cF)/F_g(\cH_1) = 1/4$ at every genus, confirming
$\kappa(\cF)/\kappa(\cH_1) = (1/4)/1 = 1/4$.
The generating function is:
\begin{equation}\label{eq:fermion-GF}
\sum_{g=1}^\infty F_g(\cF)\,\hbar^{2g}
= \frac{1}{4\hbar^2}\bigl(\hat{A}(i\hbar) - 1\bigr)
= \frac{1}{4}\Bigl(\frac{1}{24}
+ \frac{7}{5760}\hbar^2
+ \frac{31}{967680}\hbar^4 + \cdots\Bigr).
\end{equation}
\end{computation}

\subsection{Higher genus: Pfaffians and theta constants}
\label{subsec:fermion-higher-genus}
\index{free fermion!higher genus}
\index{Pfaffian!genus-$g$ partition function}


thinking
**Considering theorem references**

I see that there's a potential issue with using “TheoremD” shorthand in the shadow-dt-curve-counting proof instead of the exact theorem reference. This might be a moderate concern, as it can lead to confusion. Since the user asked for exact results, it'd be better to explicitly reference the theorem. I could fix this by using `Theorem\ref{thm:modular-characteristic}`. I wonder if it’s worth adjusting other references of Theorem D similarly, but I’ll prioritize the most straightforward fixes first.
thinking
**Clarifying theorem usage**

I realize that the theorem `koszul-equivalences-meta(iv)` is being used as a criterion rather than providing a proof for those families that satisfy it. This definitely needs a fix to ensure it references exact examples of theorems. I think being precise will enhance clarity and ensure the user understands the intention behind the theorem. It’s important for me to make these corrections to maintain accurate communication.
exec
/bin/zsh -lc "sed -n '330,430p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{computation}

\section{Bar complex computation}

The bar complex of $\beta\gamma$ computes the degree-by-degree
projections of the universal MC element
$\Theta_{\beta\gamma} := D_{\beta\gamma} - d_0 \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}). At degree~$2$,
the degree-$2$ shadow restricted to the weight-changing line vanishes
($\Theta_{\beta\gamma}^{\leq 2}\big|_{\mathrm{w.c.}} = 0$:
the $\beta\gamma$ OPE has no double pole, so
the bar complex is uncurved on this slice).
The global modular characteristic
$\kappa(\beta\gamma) = c/2 \neq 0$
(Proposition~\ref{prop:betagamma-obstruction-coefficient})
is nonzero; the vanishing is specific to the weight-changing
direction. At degree~$3$,
the cubic shadow $C$ is nonzero (the mixed OPE $\beta\gamma \sim 1/(z{-}w)$
contributes a nontrivial residue). At degree~$4$, the quartic contact
shadow $Q^{\mathrm{contact}}_{\beta\gamma}$ is the first genuinely


thinking
**Analyzing cohomology theorems**

I'm considering the theorem around betagamma-bar-cohomology, which proves the Koszul property at genus zero. I think citing this might be better than focusing solely on betagamma-bc-koszul. The proposition statement talks about beta-gamma-bc ghost systems, but I’m looking at the bar cohomology of βγ, which shows acyclicity above degree zero. For the user's exact request, I wonder if citing bar cohomology or duality will work, especially since the theorem provides a dual algebra relevant to Koszul pairs.
thinking
**Reviewing fermion theorems**

For the free fermion, the free_fields theorem corresponds to the genus zero bar complex. I think it might be better to cite `thm:betagamma-bar-cohomology` instead of the βγ duality theorem for line 16992. There’s a potential issue with the conditional-modular-koszul proof's MK1 needing a citation to `cor:w-principal-completed-koszul`, and the same for line 1818. 

I noticed some search outputs like "Theorem D_scal" may not be relevant. I wonder if there are broken label references due to multiple theorems not appearing. It could be worth verifying by running targeted searches in the file. I might also use `rg` to check for modified phrases and ensure no stale imports remain.
exec
/bin/zsh -lc "rg -n \"fermion-boson-koszul|single-generator duality|Sym\\\\"'^'"\\\\{\\\\mathrm\\\\{ch\\\\}\\}\\\\(\\\\gamma\\\\)|free fermion.*Koszul\" chapters/examples/free_fields.tex chapters/theory/cobar_construction.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:fermion-boson-koszul|single-generator duality|Sym\^\{\mathrm\{ch\}\}\(\gamma\)|free fermion.*Koszul)
                                                            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"fermion-boson-koszul\" chapters/examples/free_fields.tex chapters/theory/cobar_construction.tex -g '*.tex'; rg -n -F \"single-generator duality\" chapters/examples/free_fields.tex chapters/theory/cobar_construction.tex -g '*.tex'; rg -n -F \"free fermion\" chapters/examples/free_fields.tex chapters/theory/cobar_construction.tex -g '*.tex' | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/cobar_construction.tex:1107:\begin{theorem}[Fermion-boson Koszul duality; \ClaimStatusProvedHere]\label{thm:fermion-boson-koszul}
chapters/theory/cobar_construction.tex:2120:recovering the free fermion algebra itself (not the $\beta\gamma$ system). The Koszul dual $\mathcal{F}^! \cong \beta\gamma$ is obtained instead by linear duality of the bar coalgebra: $\mathcal{F}^! = \bar{B}^{\text{ch}}(\mathcal{F})^\vee$ (see Example~\ref{ex:fermion-betagamma-bar-cobar} and Theorem~\ref{thm:fermion-boson-koszul}). This distinction is the chiral analog of the classical fact that $\Omega(\bar{B}({\Lambda}(V))) \simeq {\Lambda}(V)$ (bar-cobar inversion), while ${\Lambda}(V)^! = \mathrm{Sym}(V^*)$ (Koszul dual algebra via linear duality).
chapters/examples/free_fields.tex:728:The $\beta\gamma$ system combines a bosonic weight-$1$ field $\beta$ and a bosonic weight-$0$ field $\gamma$. Its bar complex shares the discriminant $\Delta(x) = (1-3x)(1+x)$ with $\widehat{\mathfrak{sl}}_2$ and the Virasoro algebra. The Koszul dual is the $bc$ ghost system (\S\ref{sec:fermion-boson-koszul}).
chapters/examples/free_fields.tex:1703:\subsection{\texorpdfstring{$\beta\gamma$--$bc$}{beta-gamma--bc} Koszul duality}\label{sec:fermion-boson-koszul}
chapters/examples/free_fields.tex:2763:This calculation is carried out in detail in Theorem~\ref{thm:betagamma-bc-koszul} above (see \S\ref{sec:fermion-boson-koszul}): the antisymmetric relation $\beta\gamma - \gamma\beta$ dualizes under the residue pairing to the Clifford relation $bc + cb$, establishing $(\beta\gamma)^! \cong bc$.
chapters/examples/free_fields.tex:5792:The explicit low-degree bar complex computations for the free fermion, Heisenberg, and $\beta\gamma$ system are carried out in Theorem~\ref{thm:fermion-bar-complex-genus-0} (free fermion, \S\ref{sec:free-fermion}), Theorem~\ref{thm:heisenberg-bar} and Theorem~\ref{thm:heisenberg-bar-complete} (Heisenberg, \S\ref{sec:heisenberg-bar-complex}), and Theorem~\ref{thm:betagamma-bc-koszul} with Proposition~\ref{prop:bc-betagamma-orthogonality} ($\beta\gamma \leftrightarrow bc$, \S\ref{sec:fermion-boson-koszul}). All results match the predictions of Theorem~\ref{thm:bar-cobar-isomorphism-main}.
chapters/examples/free_fields.tex:842:This single-generator duality should not be confused with the \emph{two-generator} duality $(\beta\gamma)^! \cong bc$ of Theorem~\ref{thm:betagamma-bc-koszul}. Here both sides have $\dim V = 1$; in the $\beta\gamma$--$bc$ duality, both sides have $\dim V = 2$.
chapters/theory/cobar_construction.tex:1066:\begin{example}[Cobar of exterior coalgebra: free fermions]\label{ex:cobar-fermion-complete}
chapters/theory/cobar_construction.tex:1093:\emph{Physical interpretation.} This is the \emph{Koszul duality} of free fermions (not to be confused with the boson-fermion correspondence/bosonization, which identifies $\mathcal{F} \cong V_{\mathbb{Z}}$ as a lattice vertex algebra).
chapters/theory/cobar_construction.tex:1112:The $\beta\gamma$ system is the \emph{Koszul dual} of free fermions.
chapters/theory/cobar_construction.tex:1128:The free fermion algebra $\mathcal{F} = \Lambda^{\mathrm{ch}}(V)$ is generated by $V$ with the exterior (anticommutative) chiral product. By the classical Koszul duality $\Lambda(V)^! = \mathrm{Sym}(V^*)$ (Loday--Vallette~\cite{LV12}, Theorem~3.2.1), the chiral Koszul dual is $\mathcal{F}^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$, the commutative chiral algebra on $V^*$, which is the $\beta\gamma$ system with $\beta \in V^*$, $\gamma \in V$. The complete bar-cobar computation verifying the Koszul property (acyclicity of $B(\mathcal{F}) \otimes_\tau \mathcal{F}^!$) is carried out in Part~\ref{part:characteristic-datum}.
chapters/theory/cobar_construction.tex:2115:\begin{example}[Cobar of bar of free fermions]\label{ex:cobar-bar-fermion}
chapters/theory/cobar_construction.tex:2116:For the free fermion algebra $\mathcal{F}$, bar-cobar inversion gives:
chapters/theory/cobar_construction.tex:2120:recovering the free fermion algebra itself (not the $\beta\gamma$ system). The Koszul dual $\mathcal{F}^! \cong \beta\gamma$ is obtained instead by linear duality of the bar coalgebra: $\mathcal{F}^! = \bar{B}^{\text{ch}}(\mathcal{F})^\vee$ (see Example~\ref{ex:fermion-betagamma-bar-cobar} and Theorem~\ref{thm:fermion-boson-koszul}). This distinction is the chiral analog of the classical fact that $\Omega(\bar{B}({\Lambda}(V))) \simeq {\Lambda}(V)$ (bar-cobar inversion), while ${\Lambda}(V)^! = \mathrm{Sym}(V^*)$ (Koszul dual algebra via linear duality).
chapters/theory/cobar_construction.tex:2640:\item Free theories (Heisenberg at any level, free fermions with spin structure) extend to all genera without central charge restrictions, as the curvature $m_0$ is central and the obstruction class is scalar (Proposition~\ref{prop:km-bar-curvature}).
chapters/theory/cobar_construction.tex:2645:The free fermion extends to all genera with spin structure:
chapters/examples/free_fields.tex:54:The free fermion $r$-matrix vanishes: the simple pole in the
chapters/examples/free_fields.tex:77:The free fermion is Gaussian with
chapters/examples/free_fields.tex:86:single-generator free fermion is class~G ($r_{\max} = 2$) by
chapters/examples/free_fields.tex:149:The free fermion and Heisenberg bar complexes are

thinking
**Looking into the theorem**

I'm considering searching for the theorem related to the free fermion genus expansion, possibly around line 336 in the free_fields section. I need to inspect the content there to get more context and clarity on the topics at hand. It seems like there’s something valuable to uncover in that specific area, so diving into it might yield some interesting insights! Let’s see what I can find!
exec
/bin/zsh -lc "sed -n '330,380p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\subsubsection{Genus expansion of the free fermion}
\label{sec:fermion-genus-expansion}%
\index{free fermion!genus expansion}%

\begin{theorem}[Free fermion genus expansion; \ClaimStatusProvedHere]
\label{thm:fermion-genus-expansion}
For all $g \geq 1$, the genus-$g$ free energy of the free fermion is:
\begin{equation}\label{eq:fermion-Fg}
F_g(\mathcal{F})
= \frac{1}{4} \cdot \frac{2^{2g-1}-1}{2^{2g-1}}
 \cdot \frac{|B_{2g}|}{(2g)!}
\end{equation}
where $B_{2g}$ denotes the $2g$-th Bernoulli number.
The first values are:
\begin{align}
F_1(\mathcal{F}) &= \frac{1}{96},
 \label{eq:fermion-F1} \\
F_2(\mathcal{F}) &= \frac{7}{23040},
 \label{eq:fermion-F2} \\

thinking
**Considering potential issues**

I’m noticing a potential issue on line 16992 that seems okay but might be hidden. I think we’ll need to decide whether to patch it. Then, there’s another hidden import on line 31121 that references “Functoriality follows from naturality of the transferred operations...” which sounds a bit vague. I really need to inspect that statement closely to clarify things. Let’s make sure we address these concerns thoroughly!
exec
/bin/zsh -lc "sed -n '31100,31135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
structure on $\mathfrak{g}_{\cA}^{\mathrm{mod}}$.
\end{remark}

\begin{proposition}[MC structure principle; \ClaimStatusProvedHere]
\label{prop:chriss-ginzburg-structure}
\index{Chriss--Ginzburg structure principle|textbf}
\index{modular bar--Hamiltonian!as structure map}
The assignment $\cA \mapsto \Theta_{\cA}
\in \operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA})$
is a functor from chiral algebras to Maurer--Cartan moduli of the
ambient algebra:
\begin{equation}
\label{eq:chriss-ginzburg-functor}
\Theta\colon
\{\text{chiral algebras}\}
\longrightarrow
\coprod_{\cA}\,
\operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA}).
\end{equation}
The algebra structure on $\cA$ \emph{is} the Maurer--Cartan element


thinking
**Crafting the patch carefully**

I want to make sure I'm using ASCII only for this patch. While it's okay if there's an em dash already, I won't be adding any new ones. I’ll check if the macros for beta and gamma, like `\beta\gamma`, are in the file — which they are! It’s important to ensure I’m not quoting from another file while I’m doing this. Let's keep it focused and precise.
thinking
**Evaluating theorem citations**

I’m considering whether the target file has already referenced the theorem. I could cite `Theorem\ref{thm:fermion-boson-koszul}`, which proves fermion-boson Koszul duality in cobar construction. Given that the proposition covers free fermion modular pre-Koszul, it might make more sense to reference `thm:fermion-boson-koszul` for that pair and possibly `thm:fermion-bar-complex-genus-0` for bar concentration. I’m thinking maybe less is more, but I'm not entirely sure.
exec
/bin/zsh -lc "sed -n '1107,1148p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Fermion-boson Koszul duality; \ClaimStatusProvedHere]\label{thm:fermion-boson-koszul}

\smallskip\noindent
\textup{[Regime: quadratic
\textup{(}Convention~\textup{\ref{conv:regime-tags}}\textup{)}.]}
The $\beta\gamma$ system is the \emph{Koszul dual} of free fermions.
This is the chiral analog of classical
$\mathrm{Sym}(V) \leftrightarrow \Lambda(V^*)$ Koszul duality
(see Part~\ref{part:characteristic-datum} for the complete bar-cobar computation).

The Koszul duality correspondence exchanges:
\begin{enumerate}
\item \emph{Relations}: anticommuting fields $\{\psi, \psi\} = 0$ $\leftrightarrow$ symplectic bosons $[\beta,\gamma] = 1$; exterior relation $\psi \boxtimes \psi = 0$ $\leftrightarrow$ symplectic pairing $\langle \beta, \gamma \rangle = \frac{1}{z_1-z_2}$.

\item \emph{Algebra structure}: exterior algebra $\Lambda^*(\psi)$ $\leftrightarrow$ polynomial-type algebra; bar complex $\bar{B}(\mathcal{F}) = \Lambda^*(\psi, \partial\psi, \ldots)$ $\leftrightarrow$ $\bar{B}(\beta\gamma)$ with symplectic differential.

\item \emph{Statistics}: fermionic $\leftrightarrow$ bosonic.
\end{enumerate}
\end{theorem}

exec
/bin/zsh -lc "rg -n \"label\\{thm:heisenberg-koszul-dual|label\\{thm:frame-heisenberg-koszul-dual|label\\{thm:heisenberg-bar\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:1425:\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}
chapters/examples/free_fields.tex:1997:\begin{theorem}[Heisenberg Koszul dual; \ClaimStatusProvedHere]\label{thm:heisenberg-koszul-dual-early}
chapters/frame/heisenberg_frame.tex:1184:\label{thm:frame-heisenberg-koszul-dual}

thinking
**Considering theorem choices**

I’m weighing whether to use `thm:heisenberg-koszul-dual-early` or `frame-heisenberg-koszul-dual`. It seems like the Heisenberg Koszul dual theorem directly provides the pair I need. I should take a closer look to see which option may fit better for my purposes, ensuring I make the most informed choice possible. Let's dive into the details and figure out which one will work best!
exec
/bin/zsh -lc "sed -n '1988,2028p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
perspective, the BRST differential is precisely the bar complex
differential for the module Koszul duality: it resolves the
matter module via $bc$ ghosts, and the BRST cohomology is the
derived Koszul dual module.
\end{remark}


\subsection{Heisenberg Koszul dual: symmetric algebra}

\begin{theorem}[Heisenberg Koszul dual; \ClaimStatusProvedHere]\label{thm:heisenberg-koszul-dual-early}
\index{Heisenberg algebra!Koszul dual}
The Heisenberg chiral algebra $\mathcal{H}_k$ at level $k$ has Koszul dual:
\[\mathcal{H}_k^! \simeq \bigl(\mathrm{Sym}^{\mathrm{ch}}(V^*),\, d = 0,\, m_0 = -k \cdot \omega\bigr)\]
where $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is the chiral symmetric (commutative) algebra on the dual generator space, and $\omega \in \mathrm{Sym}^2(V^*)$ is the element dual to the pairing $\langle \alpha, \alpha \rangle = k$. This is a \emph{curved} commutative chiral algebra in the sense of Positselski: the curvature $m_0 = -k \cdot \omega$ encodes the level, and $m_0 = 0$ only at level $k = 0$.

More explicitly, the bar complex decomposes as:
\begin{align}
\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) &\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*) \quad \text{(conilpotent chiral coalgebra)} \\
\Omega^{\mathrm{ch}}(\mathrm{coLie}^{\mathrm{ch}}(V^*)) &\simeq \bigl(\mathrm{Sym}^{\mathrm{ch}}(V^*),\, m_0 = -k \cdot \omega\bigr) \quad \text{(curved cobar)}
\end{align}

thinking
**Evaluating Koszulity Issues**

I'm considering a potential issue with completed Koszulity found in examples/w_algebras.tex. It may not perfectly match the requirements of the MK1 proposition regarding bar spectral sequence collapsing at E2 along the diagonal. However, the completed Koszulity indicates that homology is concentrated along the diagonal in the completed bar complex, which might actually be better than the bare spectral sequence. I want to highlight this as the genus-0 Koszul input. I'll also think about whether MK1 uses `cor:w-principal-completed-koszul` alone, but a dual partner may be necessary too.
exec
/bin/zsh -lc "rg -n \"modular pre-Koszul|MK3|PBW spectral sequence|genus-\\"'$g'"\\"'$ computation|only double-pole contributions|free-field genus expansion" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F "extended to the modular setting" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n -F "modular setting" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
13339:modular setting.
codex
I’ve isolated five surviving citation/import defects in `higher_genus_modular_koszul.tex`. I’m patching only that file: replacing one wrong theorem import, two underpowered W-algebra imports, one modular-extension handwave, one family-level “criterion” shortcut, and one shorthand `Theorem D` proof reference with exact theorem labels.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -710,3 +710,5 @@
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
@@ -763,4 +765,4 @@
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
@@ -1817,4 +1819,4 @@
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
@@ -13335,6 +13337,6 @@
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
@@ -16993,6 +16995,5 @@
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
@@ -26985,3 +26986,6 @@
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

codex
The patch is in. I’m doing a narrow verification pass now: checking the edited lines, confirming every new label exists, and confirming the stale underpowered imports are gone from the audited sites.
exec
/bin/zsh -lc "sed -n '704,718p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{enumerate}
\end{proposition}

\begin{proof}
For (a)--(b), the bar complex is explicit
(Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
MK1 (genus-0 Koszulity) by
Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
for~(b) the free-field genus expansion is explicit
(\S\ref{sec:free-field-genera}).
exec
/bin/zsh -lc "sed -n '760,770p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Theorems~\ref{thm:pbw-allgenera-km}
and~\ref{thm:pbw-allgenera-virasoro}.

For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
unconditionally:
MK1 by
Theorem~\ref{thm:w-algebra-koszul-main} together with
Corollary~\ref{cor:w-principal-completed-koszul};
MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
Inversion and complementarity follow as consequences.
exec
/bin/zsh -lc "sed -n '1814,1826p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '13332,13342p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{proof}
(I) follows from functoriality of the bar construction
(Proposition~\ref{prop:mc2-functoriality}).
(II) is the definition of the modular convolution algebra
(Definition~\ref{def:modular-convolution-dg-lie}).
(III) follows from the modular twisting-morphism identification
(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
to the strict model by
Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
(IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 succeeded in 52ms:
principal finite-type $\mathcal{W}$-algebras,
from conditional to unconditional.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorem~\ref{thm:w-algebra-koszul-main}
together with Corollary~\ref{cor:w-principal-completed-koszul}.
MK2 (Verdier):
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (PBW concentration at all genera):
Theorem~\ref{thm:pbw-allgenera-principal-w}.
MK4 and MK5 follow from MK1--MK3 by
exec
/bin/zsh -lc "sed -n '16988,16998p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
generic $c$
(Theorem~\ref{thm:w-virasoro-quintic-forced}); the all-degree master
equation (Theorem~\ref{thm:nms-all-degree-master-equation}) then
forces all higher obstructions to be non-zero by induction.

That all four families are Koszul follows from
Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
exec
/bin/zsh -lc "sed -n '26978,26986p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorems~\\ref{thm:heisenberg-bar-complete} and~\\ref{thm:km-chiral-koszul}\" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F \"and~\\ref{thm:bar-cobar-spectral-sequence}\" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F \"extended to the modular setting\" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F \""'$'"\\int_{\\overline{\\cM}_g}\\lambda_g\\cdot\\kappa"'$ by Theorem~D." chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
\textup{(}UNIFORM-WEIGHT\textup{)}.
\end{equation}
Higher-degree corrections correspond to higher curve-class
contributions: cubic shadow $\to$ degree~$2$,
quartic $\to$ degree~$3$.
\end{theorem}

\begin{proof}
 exited 1 in 51ms:

exec
/bin/zsh -lc 'for label in thm:heisenberg-koszul-dual-early thm:fermion-boson-koszul thm:betagamma-bc-koszul cor:w-principal-completed-koszul cor:vol1-theta-log-fm-twisting-data cor:strictification-comparison thm:lattice:koszul-morphism thm:betagamma-bar-cohomology thm:modular-characteristic; do if ! grep -R -F "'"\\\\label{"'$label}" --include='"'*.tex' . >/dev/null; then echo \"MISSING "'$label"; fi; done' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

codex
The edited surfaces are consistent so far. I’m doing one last pass for exact line numbers and the final proof snippet, then I’ll report findings in the requested `PROBLEM ... / EXACT edit applied ...` format.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '706,718p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '760,769p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1816,1825p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13333,13341p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '26980,26990p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16992,17000p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '26982,26992p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   706	
   707	\begin{proof}
   708	For (a)--(b), the bar complex is explicit
   709	(Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
   710	MK1 (genus-0 Koszulity) by
   711	Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
   712	Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
   713	Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
   714	MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
   715	MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
   716	only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
   717	for~(b) the free-field genus expansion is explicit
   718	(\S\ref{sec:free-field-genera}).
 succeeded in 51ms:
   760	Theorems~\ref{thm:pbw-allgenera-km}
   761	and~\ref{thm:pbw-allgenera-virasoro}.
   762	
   763	For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
   764	unconditionally:
   765	MK1 by
   766	Theorem~\ref{thm:w-algebra-koszul-main} together with
   767	Corollary~\ref{cor:w-principal-completed-koszul};
   768	MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
   769	MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 succeeded in 52ms:
 13333	\begin{proof}
 13334	(I) follows from functoriality of the bar construction
 13335	(Proposition~\ref{prop:mc2-functoriality}).
 13336	(II) is the definition of the modular convolution algebra
 13337	(Definition~\ref{def:modular-convolution-dg-lie}).
 13338	(III) follows from the modular twisting-morphism identification
 13339	(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
 13340	to the strict model by
 13341	Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 succeeded in 52ms:
  1816	\end{corollary}
  1817	
  1818	\begin{proof}
  1819	MK1 (genus-$0$ Koszulity):
  1820	Theorem~\ref{thm:w-algebra-koszul-main}
  1821	together with Corollary~\ref{cor:w-principal-completed-koszul}.
  1822	MK2 (Verdier):
  1823	Theorem~\ref{thm:verdier-bar-cobar}.
  1824	MK3 (PBW concentration at all genera):
  1825	Theorem~\ref{thm:pbw-allgenera-principal-w}.
 succeeded in 52ms:
\end{equation}
Higher-degree corrections correspond to higher curve-class
contributions: cubic shadow $\to$ degree~$2$,
quartic $\to$ degree~$3$.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:modular-characteristic},
\[
F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
\]
 succeeded in 51ms:
 16992	forces all higher obstructions to be non-zero by induction.
 16993	
 16994	That all four families are Koszul follows from
 16995	Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
 16996	for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
 16997	for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
 16998	VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 16999	\end{proof}
 17000	
 succeeded in 50ms:
 26982	contributions: cubic shadow $\to$ degree~$2$,
 26983	quartic $\to$ degree~$3$.
 26984	\end{theorem}
 26985	
 26986	\begin{proof}
 26987	By Theorem~\ref{thm:modular-characteristic},
 26988	\[
 26989	F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
 26990	\]
 26991	For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 26992	GV integrality gives $n_0^{d=1} = 1$.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

exec
/bin/zsh -lc "grep -R -n -E '\\\\label\\{(thm:heisenberg-koszul-dual-early|thm:fermion-boson-koszul|thm:betagamma-bc-koszul|cor:w-principal-completed-koszul|cor:vol1-theta-log-fm-twisting-data|cor:strictification-comparison|thm:lattice:koszul-morphism|thm:betagamma-bar-cohomology|thm:modular-characteristic)\\}' chapters | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 255ms:
chapters/theory/cobar_construction.tex:1101:\begin{theorem}[Fermion-boson Koszul duality; \ClaimStatusProvedHere]\label{thm:fermion-boson-koszul}
chapters/theory/higher_genus_modular_koszul.tex:2848:\label{thm:modular-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:11078:\label{cor:strictification-comparison}
chapters/theory/higher_genus_modular_koszul.tex:11454:\label{cor:vol1-theta-log-fm-twisting-data}
chapters/examples/w_algebras.tex:6548:\label{cor:w-principal-completed-koszul}
chapters/examples/free_fields.tex:1706:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality; \ClaimStatusProvedHere]\label{thm:betagamma-bc-koszul}
chapters/examples/free_fields.tex:1997:\begin{theorem}[Heisenberg Koszul dual; \ClaimStatusProvedHere]\label{thm:heisenberg-koszul-dual-early}
chapters/examples/beta_gamma.tex:414:\label{thm:betagamma-bar-cohomology}
chapters/examples/lattice_foundations.tex:1001:\label{thm:lattice:koszul-morphism}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}


thinking
**Updating plan details**

I think I need to check line 1107 for the `thm:fermion-boson-koszul` instead of 1101. That seems like a good direction! I also want to verify that there are no stale patterns present since we didn’t see any outputs. It’s fine for now, but I should definitely consider updating the plan to mark it as completed. I want to ensure everything is in order before moving forward!
Plan update
Audited the explicit theorem/proposition/lemma imports and the surviving hidden-import shortcuts in the target chapter, patched the defective ones in place, and ran narrow verification on the edited surfaces and new labels.
  ✓ Load higher_genus_modular_koszul.tex contexts for all explicit import phrases and map cited labels to live definitions/status
  ✓ Identify broken or underjustified imports in the chapter and choose minimal truthful rewrites confined to the target file
  ✓ Apply patch, then verify no new broken references or unsupported hidden-import phrasing remain on the edited surface
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}



thinking
**Structuring findings and verifications**

I need to mention that the tests weren't run, focusing only on narrow grep verification. My final answer should be concise, ordered by severity, and include findings first. Including clickable file links is necessary since there's just one file, like [higher_genus_modular_koszul.tex](...:710). 

For each finding, I’ll use a bullet format: `PROBLEM at [file](...:line)` and `EXACT edit applied:`. I plan to list around five findings while ensuring to maintain a flat bullet structure without nesting. This needs to be meticulous to ensure clarity!
thinking
**Organizing findings and edits**

I applied an exact edit by replacing the citation block with `thm:heisenberg-koszul-dual-early`, `thm:fermion-boson-koszul`, and `thm:betagamma-bc-koszul`, each corresponding to the family it proves. For the second bullet, I might combine lines 765 and 1820 since they show the same defect. I could mention both file:line references like "PROBLEM at ...:765 and ...:1820," using the same file link.

For verification, I'll mention that I verified new labels exist via repo grep, checked edited surfaces, and did not run full TeX build.
 succeeded in 1m 12s:

codex
I audited the requested import sites in `higher_genus_modular_koszul.tex`; these were the surviving defects.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:710): MK1 for the free-field proposition imported `thm:km-chiral-koszul`, which is an affine Kac-Moody theorem and does not prove genus-0 Koszulity for the free fermion or the `\beta\gamma`--`bc` pair. EXACT edit applied: replaced that citation block with `thm:heisenberg-koszul-dual-early`, `thm:fermion-boson-koszul`, and `thm:betagamma-bc-koszul`, matched to the three families actually covered there.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:765) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1820): the principal `\mathcal W` proofs cited `thm:bar-cobar-spectral-sequence`, which only constructs the spectral sequence and does not supply the completed diagonal Koszul input needed for MK1. EXACT edit applied: replaced that import with `cor:w-principal-completed-koszul`, while keeping `thm:w-algebra-koszul-main` for the duality input.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:13338): item (III) of the universal modular deformation functor proof relied on chiral twisting-morphism representability “transported to the modular setting” without a theorem on the page proving that extension. EXACT edit applied: replaced the handwave with `cor:vol1-theta-log-fm-twisting-data` and `cor:strictification-comparison(i)`, which are the explicit modular and strict-model results already in this chapter.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16994): the archetype-classification proof cited a general “diagonal Ext-vanishing criterion” for Heisenberg, lattice, and `\beta\gamma`, but not the example theorems that actually establish those cases. EXACT edit applied: replaced that shortcut with exact family-level imports: `thm:heisenberg-koszul-dual-early`, `thm:lattice:koszul-morphism`, and `thm:betagamma-bar-cohomology`.

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:26987): the DT-counting proof used the package shorthand “Theorem D” instead of the exact theorem surface proving the displayed formula. EXACT edit applied: replaced the shorthand with `Theorem~\ref{thm:modular-characteristic}` and wrote the imported formula explicitly as `F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g`.

Verification: I re-read the edited surfaces, confirmed the new labels exist in source, and checked that the stale defective import strings are gone from the audited sites. I did not run a full TeX build.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 41d8127dd1a96224c8de73856e4f1193e41f9094..1949727da7ec7c3406865eb5f4fe0acf531b871c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -708,7 +708,9 @@
 For (a)--(b), the bar complex is explicit
 (Chapters~\ref{chap:free-fields}--\ref{chap:beta-gamma}):
 MK1 (genus-0 Koszulity) by
-Theorems~\ref{thm:heisenberg-bar-complete} and~\ref{thm:km-chiral-koszul};
+Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
+Theorem~\ref{thm:fermion-boson-koszul} for the free fermion, and
+Theorem~\ref{thm:betagamma-bc-koszul} for the $\beta\gamma$--$bc$ pair;
 MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
 MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
 only double-pole contributions appear (Theorem~\ref{thm:heisenberg-higher-genus}),
@@ -761,8 +763,8 @@
 For principal finite-type $\mathcal{W}$-algebras, axioms MK1 and MK2 hold
 unconditionally:
 MK1 by
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence};
+Theorem~\ref{thm:w-algebra-koszul-main} together with
+Corollary~\ref{cor:w-principal-completed-koszul};
 MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
 Inversion and complementarity follow as consequences.
@@ -1815,8 +1817,8 @@
 
 \begin{proof}
 MK1 (genus-$0$ Koszulity):
-Theorems~\ref{thm:w-algebra-koszul-main}
-and~\ref{thm:bar-cobar-spectral-sequence}.
+Theorem~\ref{thm:w-algebra-koszul-main}
+together with Corollary~\ref{cor:w-principal-completed-koszul}.
 MK2 (Verdier):
 Theorem~\ref{thm:verdier-bar-cobar}.
 MK3 (PBW concentration at all genera):
@@ -13333,10 +13335,10 @@
 (Proposition~\ref{prop:mc2-functoriality}).
 (II) is the definition of the modular convolution algebra
 (Definition~\ref{def:modular-convolution-dg-lie}).
-(III) follows from the twisting morphism representability
-(Theorem~\ref{thm:convolution-master-identification},
-Corollary~\ref{cor:theta-twisting-morphism}) extended to the
-modular setting.
+(III) follows from the modular twisting-morphism identification
+(Corollary~\ref{cor:vol1-theta-log-fm-twisting-data}), transported
+to the strict model by
+Corollary~\ref{cor:strictification-comparison}\textup{(}i\textup{)}.
 (IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
 invariance theorem
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
@@ -16991,10 +16993,9 @@
 
 That all four families are Koszul follows from
 Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
-for affine and W-algebras, and from the diagonal
-Ext-vanishing criterion
-(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
-Heisenberg, lattice, and $\beta\gamma$.
+for affine and W-algebras, Theorem~\ref{thm:heisenberg-koszul-dual-early}
+for Heisenberg, Theorem~\ref{thm:lattice:koszul-morphism} for lattice
+VOAs, and Theorem~\ref{thm:betagamma-bar-cohomology} for $\beta\gamma$.
 \end{proof}
 
 % ========================================================
@@ -26983,7 +26984,10 @@
 \end{theorem}
 
 \begin{proof}
-$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.
+By Theorem~\ref{thm:modular-characteristic},
+\[
+F_g(\cA)=\kappa(\cA)\int_{\overline{\cM}_g}\lambda_g.
+\]
 For rigid $C = \bP^1$, this is the degree-$1$ GW invariant;
 GV integrality gives $n_0^{d=1} = 1$.
 \end{proof}

tokens used
263,560
