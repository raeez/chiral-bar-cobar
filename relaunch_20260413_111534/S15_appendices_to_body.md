# S15_appendices_to_body (1377s)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16576 — PROBLEM: the proof of `thm:shadow-archetype-classification` cites `thm:nms-heisenberg-exact-linearity` for “Heisenberg and lattice VOAs” and for `m_k=0` for all `k\ge3`, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:953-966` is only the Heisenberg line and only states `\Theta_{\mathcal H}^{\le4}=H_{\mathcal H}` through quartic order. It does not cover lattices. FIX: replace this step with `For Heisenberg, Theorem~\ref{thm:heisenberg-formality} gives \(m_k=0\) for all \(k\ge3\).` Delete `and lattice VOAs` here; add a separate lattice-specific citation before retaining lattices in item `(i)` of `thm:shadow-archetype-classification`.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16581 — PROBLEM: the same proof upgrades `thm:nms-affine-cubic-normal-form` to all affine algebras, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1037-1050` is only for the strict current-level sector of `\widehat{\mathfrak{sl}}_{2,k}`. The same scope leak already appears expositionally at `chapters/theory/higher_genus_modular_koszul.tex:12609`. FIX: replace `For affine algebras` with `For the strict current-level sector of \widehat{\mathfrak{sl}}_{2,k}` at both locations, or supply a genuinely general affine theorem before keeping the broader quantifier in `thm:shadow-archetype-classification(ii)`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:31342 — PROBLEM: this cites `thm:nms-archetype-trichotomy` as a full `G/L/C/M` all-genera classification, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1207-1226` only treats three primitive families through quartic order. The same miscitation recurs at `chapters/theory/higher_genus_modular_koszul.tex:31574`, `chapters/theory/chiral_koszul_pairs.tex:2960`, `chapters/theory/chiral_koszul_pairs.tex:3079`, and `chapters/theory/higher_genus_complementarity.tex:5781`. FIX: replace each of those citations with `Theorem~\ref{thm:shadow-archetype-classification}`; when infinite Virasoro/`\mathcal W_N` behavior is used explicitly, add `Theorem~\ref{thm:nms-finite-termination}` or `Theorem~\ref{thm:nms-virasoro-quintic-forced}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:17872 — PROBLEM: the body says `thm:nms-clutching-law-modular-resonance` gives the quartic factorization constraint “at every boundary stratum,” but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1822-1835` is only a separating clutching law. FIX: change `every boundary stratum` to `every separating boundary stratum`; if non-separating strata are intended too, cite `Theorem~\ref{thm:nms-nonseparating-clutching-law}` alongside it.

- [HIGH] chapters/theory/chiral_modules.tex:2945 — PROBLEM: the level involution `k\mapsto -k-4` is attributed to `thm:sl2-koszul-dual`, but the cited theorem in `appendices/_sl2_yangian_insert.tex:531-553` only identifies the open-colour dual with `Y_\hbar(\mathfrak{sl}_2)` and `\hbar=1/(k+2)`. The closed-colour affine level shift appears only in `appendices/_sl2_yangian_insert.tex:596-602` as `rem:closed-vs-open-sl2`. The same wrong theorem citation is repeated at `chapters/theory/chiral_modules.tex:2967`. FIX: change those citations to `Remark~\ref{rem:closed-vs-open-sl2}` for the closed-colour shift; keep `Theorem~\ref{thm:sl2-koszul-dual}` only for the Yangian/open-colour identification.

- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:3275 — PROBLEM: the checklist says conilpotent means `\bigcap_n \mathrm{coker}(\Delta^n)=0`, but the cited appendix theorem in `appendices/koszul_reference.tex:268-286` uses the standard criterion `\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar\Delta^{(n)})`. The body is not citing the appendix correctly. FIX: replace the parenthetical at line 3277 with `every element of \(\ker(\epsilon)\) is killed by some iterated reduced coproduct, i.e. \(\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar\Delta^{(n)})\)`.

- [HIGH] chapters/theory/algebraic_foundations.tex:116 — PROBLEM: the foundational chapter points to `Definition~\ref{def:bar-complex-algebraic}`, but the target in `appendices/notation_index.tex:342-344` is only a glossary stub pointing forward to `Theorem~\ref{thm:bar-coalgebra}`. That reverses the dependency direction and leaves the classical bar construction undefined on the theory surface. FIX: replace the sentence with a local definition, e.g. `The bar construction is \(\barB(A)=T^c(s^{-1}\bar A)\)` with deconcatenation coproduct; cite `Theorem~\ref{thm:bar-coalgebra}` only for the later chiral dg-coalgebra model, not as the source definition.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:1123 — PROBLEM: the body defines an uncurved `A_\infty` algebra with `k\ge1` but cites `Appendix~\ref{app:curved-ainfty-formulas}`, whose heading and displayed formulas in `appendices/general_relations.tex:97-107` are for the curved theory with `m_0=\mu_0`. The notation seam is off by exactly the curvature term. FIX: rename the body definition to `uncurved \(A_\infty\) algebra` and change the citation sentence to `This is the specialization \(\mu_0=0\) of the curved formulas in Appendix~\ref{app:curved-ainfty-formulas}.`

## Summary
Checked: 17 | Findings: 8 | Verdict: FAIL


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
session id: 019d8633-220e-7b33-a9dc-ea5288f79c8f
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


MISSION: SEAM AUDIT between appendices/ and chapters/theory/.

Appendices→Theory. Check: (a) appendix results cited correctly in body, (b) no circular dependencies, (c) notation consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers


thinking
**Planning the code audit**

I need to conduct a thorough code review on the specified repo sections while following the AGENTS instructions. The user has requested an audit with findings and exact fixes, but we’re not supposed to make edits unless necessary. Before diving into any mathematical edits, I need to gather context from essential files like CLAUDE and others. Using skills like deep-beilinson-audit and claim-surface-sync could be effective, and I should prioritize explorer subagents for scanning those sections. Frequent updates seem important!
thinking
**Preparing for claims verification**

The user is insisting that every claim should be grounded in the actual file contents I read. It seems I need to read those files myself, although I might rely on the explorer for some guidance. Using the explorer can help identify candidate files, but I’ll need to manually verify them. I should also consider an update plan for commentary updates before exploration and after gathering sufficient context. Starting with a commentary update seems like the best first step!
codex
I’m auditing the appendix-to-theory seam, with focus on citations, dependency direction, and notation drift. I’ll identify the actual transition files first, then read the cited seams in context and only report findings I can pin to exact lines.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files appendices chapters/theory | sed 's#"'^#/#'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/Users/raeez/chiral-bar-cobar
/chapters/theory/higher_genus_modular_koszul.tex
/chapters/theory/quantum_corrections.tex
/chapters/theory/fourier_seed.tex
/chapters/theory/poincare_duality_quantum.tex
/chapters/theory/en_koszul_duality.tex
/chapters/theory/bar_cobar_adjunction_inversion.tex
/chapters/theory/bar_cobar_adjunction_curved.tex
/chapters/theory/poincare_duality.tex
/chapters/theory/filtered_curved.tex
/chapters/theory/higher_genus_foundations.tex
/chapters/theory/computational_methods.tex
/chapters/theory/chiral_koszul_pairs.tex
/chapters/theory/bar_cobar_adjunction.tex
/chapters/theory/introduction.tex
/chapters/theory/nilpotent_completion.tex
/chapters/theory/cobar_construction.tex
/chapters/theory/hochschild_cohomology.tex
/chapters/theory/three_invariants.tex
/chapters/theory/bar_construction.tex
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

codex
I’ve loaded the constitutional files and the audit skill. Next I’m mapping the actual seam: labels defined in `appendices/` and cited in `chapters/theory/`, plus reverse references that could create circular dependence.
Plan update
Seam audit between `appendices/` and `chapters/theory/` will be evidence-first: map cross-references, read each transition in context, then attack dependency direction and notation consistency before writing findings.
  → Map appendix-defined labels referenced by theory and theory-defined labels referenced by appendices
  • Read each seam location in context and test citation correctness, scope, and dependency direction
  • Hunt second-order seam issues: circularity, notation drift, duplicate theorem surfaces, inconsistent imported hypotheses
  • Re-verify surviving findings and deliver exact file:line fixes

thinking
**Exploring mapping methods**

I need to think about cross-referencing maps. It looks like I can use commands like "rg" for labels in appendices and references in theory. I’m considering parsing those labels and employing a shell pipeline with "rg". Maybe a bash loop would help here. Let's figure out the relevant commands I need to effectively organize this! This feels like it could lead to clarity.
exec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|Cref|cref)\\{' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix|appendix' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 7877

appendices/general_relations.tex:28:Each entry represents a precise functor or natural transformation between categories. For instance, the correspondence ``Chiral multiplication $\leftrightarrow$ Residues at collision divisors'' is the content of Theorem~\ref{thm:residue-formula}, establishing that the multiplication map factors through the residue homomorphism. Similarly, ``Central extensions $\leftrightarrow$ Curved $A_\infty$ structures'' reflects Theorem~\ref{thm:heisenberg-bar}, showing how the failure of strict associativity due to central charges is precisely captured by the curvature term $m_0$.
appendices/general_relations.tex:127:That is, when the curvature element is central, $m_1$ is strictly nilpotent ($m_1^2 = 0$). This is exactly the algebraic condition ensuring $d_{\text{bar}}^2 = 0$ in the bar complex (see the nine-term proof in \S\ref{sec:bar-nilpotency}).
appendices/computational_tables.tex:4:This appendix collects numerical data for the bar complexes computed in Part~\ref{part:characteristic-datum}: Kontsevich weights for the deformation quantization star product, OPE structure constants for low-rank Kac--Moody and $\mathcal{W}$-algebras, Arnold relation expansions through $n = 4$, and modular form data at genera~$1$ and~$2$.
appendices/computational_tables.tex:131:(cf.\ the genus-$g$ formula in Appendix~\ref{app:theta}). The $2^4 = 16$ characteristics split into $6$ odd and $10$ even.
appendices/computational_tables.tex:142:the normal-ordered product. The quasi-primary composite appearing in the OPE (cf.\ Example~\ref{ex:w3-completion-full}) is $\Lambda_{\mathrm{qp}} = {:}TT{:} - \tfrac{3}{10}\partial^2 T$; in the mode commutator below we use the \emph{non-quasi-primary} convention $\Lambda_n = \sum_m {:}L_m L_{n-m}{:}$ (without derivative correction), which differs from the quasi-primary normalization used in~\cite{Bouwknegt-Schoutens} by the $-\tfrac{3}{10}\partial^2 T$ term.
appendices/computational_tables.tex:187:\emph{Convention note.} Much of the literature (Zamolodchikov 1985, Bouwknegt--Schoutens 1993, Arakawa 2017) defines a ``full composite'' $\widetilde{\Lambda} = \frac{16}{22+5c}\bigl({:}TT{:} - \frac{3}{10}\partial^2 T\bigr)$, absorbing the coefficient $\alpha = 16/(22+5c)$ into the quasi-primary field. With that convention the commutator reads $(m-n)\widetilde{\Lambda}_{m+n}$ (no extra factor of $\alpha$). We use $\Lambda = {:}TT{:}$ as above, so our commutator carries the explicit factor $\frac{16(m-n)}{22+5c}\Lambda_{m+n}$. Both conventions yield the same mode algebra; the quasi-primary version $\Lambda_{\mathrm{qp}} = {:}TT{:} - \frac{3}{10}\partial^2 T$ (cf.\ Example~\ref{ex:w3-completion-full}) is the field-theoretic standard for the OPE.
appendices/signs_and_shifts.tex:158:\item \emph{Operadic bar/cobar.} Cohomological convention (translated from the homological convention of Loday--Vallette~\cite{LV12} via $C^n = C_{-n}$; see Definition~\ref{def:grading-conventions}).
appendices/signs_and_shifts.tex:231:\item The \emph{suspension} $sV$ (also denoted $V[-1]$ in the cohomological convention or $V[1]$ in the homological convention; see Remark~\ref{rem:shift-notation}) is
appendices/signs_and_shifts.tex:250:\item \emph{Koszul dual coalgebra} (suspension): $\cA^! \hookrightarrow \mathrm{Cofree}(sV^*)$ (Appendix~\ref{app:koszul-reference}). Suspension raises the dual generators $V^*$ by one degree because dualizing reverses the grading, and the shift restores it.
appendices/signs_and_shifts.tex:548:$d_{\mathrm{bar}}[a|b] = (-1)^{|a|}[ab]$ (desuspension, Computation~\ref{comp:bar-signs-2-1}):
appendices/signs_and_shifts.tex:597:The explicit computations in \S\ref{comp:bar-signs-2-1}--\ref{comp:bar-signs-3-2}
appendices/signs_and_shifts.tex:599:$d[a|b] = (-1)^{|a|}[ab]$ and $d[a|b|c] = (-1)^{|a|}[ab|c] - (-1)^{|a|+|b|}[a|bc]$; see the verification in \S\ref{ver:d2-degree3}.
appendices/signs_and_shifts.tex:604:\noindent\textbf{Convention shift.} The computations above (\S\ref{comp:bar-signs-2-1}--\ref{comp:bar-signs-3-2}) use the unsuspended bar notation $[a|b] = a \otimes b$. From this point onward, we work in the \emph{desuspended} convention $[a|b] = s^{-1}a \otimes s^{-1}b$, which is the convention used in the body of the monograph.
appendices/signs_and_shifts.tex:634:Computations~\ref{comp:bar-signs-2-1}--\ref{comp:bar-signs-3-2}.
appendices/signs_and_shifts.tex:888:See Table~\ref{tab:master-comparison-signs} in \S\ref{sec:master-comparison-signs} for the complete comparison across all four sources. The one essential difference: Loday--Vallette use $|d|=-1$; all other sources (BD, CG, this manuscript) use $|d|=+1$.
appendices/signs_and_shifts.tex:978:For the explicit sign computations relevant to the bar differential, see the proof of $d^2 = 0$ in \S\ref{sec:bar-nilpotency}.
appendices/signs_and_shifts.tex:1143:All four sources agree on the Koszul sign rule (Convention~\ref{conv:koszul}):
appendices/signs_and_shifts.tex:1208:The dictionary in \S\ref{app:sign-conventions} records which conventions differ.
 succeeded in 51ms:
appendices/computational_tables.tex:4:This appendix collects numerical data for the bar complexes computed in Part~\ref{part:characteristic-datum}: Kontsevich weights for the deformation quantization star product, OPE structure constants for low-rank Kac--Moody and $\mathcal{W}$-algebras, Arnold relation expansions through $n = 4$, and modular form data at genera~$1$ and~$2$.
appendices/computational_tables.tex:131:(cf.\ the genus-$g$ formula in Appendix~\ref{app:theta}). The $2^4 = 16$ characteristics split into $6$ odd and $10$ even.
appendices/branch_line_reductions.tex:28:The purpose of the appendix is not to replace the full MC2 package by a
appendices/branch_line_reductions.tex:57:The appendix proves five families of results.
appendices/branch_line_reductions.tex:141:The point of view of this appendix is that the scalar and spectral levels
appendices/arnold_relations.tex:21:\label{thm:arnold-relations-appendix}
appendices/arnold_relations.tex:39:\begin{proof}[Proof of Theorem~\ref{thm:arnold-relations-appendix}]
appendices/arnold_relations.tex:41:\begin{equation}\label{eq:arnold-cyclic-appendix}
appendices/arnold_relations.tex:59:by~\eqref{eq:arnold-cyclic-appendix}. This holds for any triple $i,j,k$ and any $n \geq 3$. Completeness: the quotient algebra has Poincar\'{e} polynomial $\prod_{j=0}^{n-1}(1+jt)$, matching Arnold's computation~\cite{Arnold69}.
appendices/nonlinear_modular_shadows.tex:207:of Appendix~\ref{app:signs}.
appendices/nonlinear_modular_shadows.tex:2495:The universal class $\Theta_{\cA}$ is constructed by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}); the remaining task is to verify clutching and Verdier compatibilities in complete generality and to identify the resulting Hamiltonian modular master action. What this appendix does show is that the nonlinear layer is rigid enough to be organized theorematically, and that it carries genuinely new modular content. The genus loop operator converts quartic contact data into genus-$1$ Hessian corrections that no scalar invariant can see. The quartic resonance class is not an afterthought: it is the first modular characteristic that remembers that complementarity is nonlinear.
appendices/nonlinear_modular_shadows.tex:3136:The full hierarchy, extended by the constructions of this appendix, is
appendices/nonlinear_modular_shadows.tex:3162:appendix supplies the higher-genus completion. That is, the
appendices/nonlinear_modular_shadows.tex:3175:For the archetype families computed in this appendix:
appendices/combinatorial_frontier.tex:334:\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.
appendices/combinatorial_frontier.tex:1067:\begin{equation}\label{eq:yangian-gf-appendix}
appendices/koszul_reference.tex:7:\S\ref{app:koszul_higher_genus}. This appendix provides reference
appendices/koszul_reference.tex:17:\label{thm:extended-koszul-appendix}
appendices/koszul_reference.tex:73:\label{thm:genus-graded-koszul-duality-appendix}
appendices/koszul_reference.tex:117:\label{lem:genus-graded-koszul-resolution-appendix}
exec
/bin/zsh -lc "for f in appendices/*.tex; do rg -n '\\\\label\\{' \""'$f"; done' in /Users/raeez/chiral-bar-cobar succeeded in 86ms:
2:\label{app:notation}
16:\label{sec:notation-categories}
62:\label{sec:notation-operads}
120:\label{sec:notation-config}
164:\label{sec:notation-chiral}
223:\label{sec:notation-misc}
328:\label{sec:index-definitions}
334:\begin{definition}[A-infinity algebra]\label{def:ainf-algebra}
338:\begin{definition}[Arnold relations]\label{def:arnold-relations}
342:\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic}
346:\begin{definition}[Geometric bar complex]\label{def:geometric-bar-complex}
350:\begin{definition}[Central charge]\label{def:central-charge}
354:\begin{definition}[Chiral algebra (BD)]\label{def:chiral-algebra-bd}
358:\begin{construction}[Chiral bracket]\label{constr:chiral-bracket}
362:\begin{definition}[Topological chiral homology]\label{def:topological-chiral-homology}
366:\begin{definition}[Chiral pseudo-tensor structure]\label{def:chiral-pseudo-tensor}
370:\begin{definition}[Cobar complex]\label{def:cobar-coalgebra}
376:\begin{definition}[Configuration space]\label{def:config-space}
380:\begin{definition}[Classical D-module input]\label{def:dmod-classical}
384:\begin{definition}[E1-chiral algebra]\label{def:e1-chiral-algebra}
codex
I’ve got the broad cross-reference surface. Now I’m collapsing it to the actual seam labels so I can inspect only the appendix results the theory chapters really import, plus any reverse imports that could create circularity.
exec
/bin/zsh -lc 'while IFS=$'"'\\t' read -r file line label; do refs="'$(rg -n "'"\\\\\\\\(ref|eqref|autoref|Cref|cref)\\\\\\{"'$label'"\\\\\\}\" chapters/theory || true); if [ -n \""'$refs" ]; then printf '"'DEF %s:%s %s\\n%s\\n' \""'$file" "$line" "$label" "$refs"; fi; done < <(perl -ne '"'while(/\\\\label\\{(["'^}]+)'"\\}/g){ print \""'$ARGV'"\\t"'$.'"\\t"'$1'"\\n\" }' appendices/*.tex)" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'while IFS=$'"'\\t' read -r file line label; do refs="'$(rg -n "'"\\\\\\\\(ref|eqref|autoref|Cref|cref)\\\\\\{"'$label'"\\\\\\}\" appendices || true); if [ -n \""'$refs" ]; then printf '"'DEF %s:%s %s\\n%s\\n' \""'$file" "$line" "$label" "$refs"; fi; done < <(perl -ne '"'while(/\\\\label\\{(["'^}]+)'"\\}/g){ print \""'$ARGV'"\\t"'$.'"\\t"'$1'"\\n\" }' chapters/theory/*.tex)" in /Users/raeez/chiral-bar-cobar succeeded in 9.04s:
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{eq:d-hf\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{eq:d-fh\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{eq:d-ee\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{eq:d-ff\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{eq:d-hh\\})
                                         ^
error: repetition quantifier expects a valid decimal
codex
The first automated join failed because `rg` treated label braces as regex. I’m rerunning it with fixed-string matching so I can get a clean appendix↔theory dependency map instead of a noisy superset.
exec
/bin/zsh -lc 'while IFS=$'"'\\t' read -r file line label; do refs="'$( { rg -F -n "'"\\\\ref{"'$label}" appendices; rg -F -n "'"\\\\eqref{"'$label}" appendices; rg -F -n "'"\\\\autoref{"'$label}" appendices; rg -F -n "'"\\\\Cref{"'$label}" appendices; rg -F -n "'"\\\\cref{"'$label}" appendices; } 2>/dev/null ); if [ -n "$refs" ]; then printf '"'DEF %s:%s %s\\n%s\\n' \""'$file" "$line" "$label" "$refs"; fi; done < <(perl -ne '"'while(/\\\\label\\{(["'^}]+)'"\\}/g){ print \""'$ARGV'"\\t"'$.'"\\t"'$1'"\\n\" }' chapters/theory/*.tex)" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'while IFS=$'"'\\t' read -r file line label; do refs="'$( { rg -F -n "'"\\\\ref{"'$label}" chapters/theory; rg -F -n "'"\\\\eqref{"'$label}" chapters/theory; rg -F -n "'"\\\\autoref{"'$label}" chapters/theory; rg -F -n "'"\\\\Cref{"'$label}" chapters/theory; rg -F -n "'"\\\\cref{"'$label}" chapters/theory; } 2>/dev/null ); if [ -n "$refs" ]; then printf '"'DEF %s:%s %s\\n%s\\n' \""'$file" "$line" "$label" "$refs"; fi; done < <(perl -ne '"'while(/\\\\label\\{(["'^}]+)'"\\}/g){ print \""'$ARGV'"\\t"'$.'"\\t"'$1'"\\n\" }' appendices/*.tex)" in /Users/raeez/chiral-bar-cobar succeeded in 49.11s:
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{def:modular-koszul-preview\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{rem:equivalent-formulations-koszul\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{rem:two-phenomena\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{thm:quadratic-koszul\\})
                                         ^
error: repetition quantifier expects a valid decimal
rg: regex parse error:
    (?:\\(ref|eqref|autoref|Cref|cref)\\{def:spectral-cybe\\})
                                         ^
error: repetition quantifier expects a valid decimal
 succeeded in 1m 07s:
DEF appendices/_sl2_yangian_insert.tex:533 thm:sl2-koszul-dual
chapters/theory/chiral_modules.tex:2874:(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
chapters/theory/chiral_modules.tex:2946:(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
chapters/theory/chiral_modules.tex:2967:Theorem~\ref{thm:sl2-koszul-dual},
DEF appendices/arnold_relations.tex:647 app:arnold-relations
chapters/theory/bar_construction.tex:1225:By Arnol'd~\cite{Arnold69}, the 1-forms $\eta_{ij} = d\log(z_i - z_j)$ generate $H^*(C_n(\mathbb{C}); \mathbb{Q})$ and satisfy the Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$. That these generate \emph{all} relations follows from Cohen's computation of $H^*(C_n(\mathbb{C}))$ as the cohomology of the Arnol'd--Brieskorn braid arrangement complement~\cite{Coh76}. See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph.
DEF appendices/arnold_relations.tex:810 cor:bar-d-squared-zero-arnold
chapters/theory/en_koszul_duality.tex:505:(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
DEF appendices/arnold_relations.tex:826 thm:arnold-iff-nilpotent
chapters/theory/configuration_spaces.tex:83:Theorem~\ref{thm:arnold-iff-nilpotent}; at genus~$0$ the
chapters/theory/configuration_spaces.tex:3804:and Theorem~\ref{thm:arnold-iff-nilpotent} shows that the Arnold
DEF appendices/branch_line_reductions.tex:1179 app:branch-line-reductions
chapters/theory/introduction.tex:1967:(Appendix~\ref{app:branch-line-reductions}) extract exact
chapters/theory/chiral_hochschild_koszul.tex:5494:Appendix~\ref{app:branch-line-reductions} extracts exact
chapters/theory/chiral_hochschild_koszul.tex:5526:(Appendix~\ref{app:branch-line-reductions}) are the spectral
DEF appendices/combinatorial_frontier.tex:2441 app:combinatorial-frontier
chapters/theory/chiral_koszul_pairs.tex:1080:Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
chapters/theory/introduction.tex:2224:Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
DEF appendices/combinatorial_frontier.tex:2908 conj:w3-bar-gf
chapters/theory/higher_genus_modular_koszul.tex:33770:and~\ref{conj:w3-bar-gf}) is the first example where the
 succeeded in 4m 23s:
DEF chapters/theory/algebraic_foundations.tex:212 def:koszul-pair-classical
appendices/notation_index.tex:485:\item Koszul pair, Definition~\ref{def:chiral-koszul-pair} (chiral), Definition~\ref{def:koszul-pair-classical} (classical)
DEF chapters/theory/algebraic_foundations.tex:405 def:convolution-dg-lie
appendices/notation_index.tex:449:(Definition~\ref{def:convolution-dg-lie}). The set $\mathrm{Tw}(C, A)$
DEF chapters/theory/algebraic_foundations.tex:670 def:twisting-morphism
appendices/notation_index.tex:445:See Definition~\ref{def:twisting-morphism} for the full treatment.
appendices/notation_index.tex:501:\item Twisting morphism, Definition~\ref{def:twisting-morphism}
DEF chapters/theory/algebraic_foundations.tex:713 prop:universal-twisting-adjunction
appendices/notation_index.tex:451:(Proposition~\ref{prop:universal-twisting-adjunction}).
DEF chapters/theory/algebraic_foundations.tex:882 thm:operadic-homotopy-convolution
appendices/nonlinear_modular_shadows.tex:151:By Theorem~\ref{thm:operadic-homotopy-convolution}, $\gAmod$ is the
appendices/nonlinear_modular_shadows.tex:373:(Theorem~\ref{thm:operadic-homotopy-convolution}); piece~(3) is the
DEF chapters/theory/algebraic_foundations.tex:1165 rem:factorization-locality
appendices/notation_index.tex:459:Locality is encoded by the factorization-locality principle~\ref{rem:factorization-locality}.
DEF chapters/theory/algebraic_foundations.tex:1172 def:ran-space
appendices/notation_index.tex:495:\item Ran space, Definition~\ref{def:ran-space}
DEF chapters/theory/algebraic_foundations.tex:1292 thm:chiral-ran
appendices/notation_index.tex:381:The \(\mathcal{D}\)-module realization used throughout is the one in Theorem~\ref{thm:chiral-ran}.
appendices/notation_index.tex:404:The holonomic regime for chiral/\(\mathcal{D}\)-module objects is used through the Ran-space formalism of Theorem~\ref{thm:chiral-ran}.
DEF chapters/theory/algebraic_foundations.tex:1605 thm:operadic-bar
Reconnecting... 1/5 (stream disconnected before completion: idle timeout waiting for SSE)

thinking
**Managing sessions**

I'm considering whether I should stop some sessions now. One has already finished, but I think 71155 might still be running. Maybe I should continue with it, as it could have more data. I could poll to check the status and close it if it's done. There’s definitely a process here that I'm navigating, and I want to ensure everything wraps up smoothly!







thinking
**Identifying findings in mapping**

I need to look at the mapping and identify candidate findings. It’s important to carefully review the seam points for any miscitations, circular dependencies, or notation inconsistencies. The mapping can help me understand the corresponding contexts, and I should focus on the actual issues at hand. Since the audit surface is large, I’ll need to systematically search for any obvious broken references and ensure cited labels exist. The user wants the file content reviewed, so inspecting transition paragraphs and appendix statements will be essential to find any inconsistencies or gaps.
thinking
**Exploring potential strategies**

I’m considering a few strategies to tackle the task at hand. First, I could search for cross-references where the theory cites appendix results that rely on the same theoretical results, creating circular dependencies. I'll also look for notation inconsistencies between the appendix and the theory on the same concepts, like specific symbols and conventions. Additionally, checking for mismatched wording, where the theory claims the appendix proves something but it only conjectures, is crucial. Lastly, I need to inspect any appendix that summarizes theory results instead of proving them, as that might lead to circular references when cited.
thinking
**Prioritizing theorem-level dependencies**

I think I should prioritize imported results that resemble theorem-level dependencies. For example, there's `cor:bar-d-squared-zero-arnold` and `thm:arnold-iff-nilpotent` which are pulled into the theory. Also, `thm:sl2-koszul-dual` is imported into `chiral_modules.tex`, and several appendices like `app:branch-line-reductions` and `app:combinatorial-frontier` are referenced in critical areas. There are numerous results, like homotopy transfer results and signs, that are cited extensively. However, I noticed a potential issue where the theory cites a definition from the `notation_index`, which might hint at circular referencing, so that needs further inspection in context.
thinking
**Evaluating circular dependency in theory**

I need to determine if there’s a circular dependency in the theory or if it’s acceptable since the appendix results extend the main theory. If the theory cites appendix theorems before they’re established, that could be circular. I’ll inspect transition points carefully and check how the appendix results are cited in relation to the main theory. If they’re just examples or pointers and not used in proofs, it could be okay. I might also automate cross-label dependencies to find any cycles.
thinking
**Inspecting theorem citations**

I'm considering whether the appendix gathers formulas correctly and if the label `app:curved-ainfty-formulas` is in the right place. I should check if the reference text prints strangely or points to the wrong appendix. There's also a theorem cited from `configuration_spaces.tex` that needs verification, especially concerning its local conditions. I want to ensure that citations from other sections properly reference the appendix, particularly if they are standalone or included in a unique context.
thinking
**Assessing theorem dependencies**

I’m considering how the appendix might extend the theory, which could be acceptable if the body references it properly. The user is asking about a seam audit. If a theorem in the body cites the appendix to support a claim, I need to check for potential cycles—like if an appendix theorem depends on the same body theorem it’s supporting. I might look into references around transition points where theory mentions the appendix for clarity.
thinking
**Searching for inconsistencies**

I need to find mismatched descriptions by searching for all phrases related to "Appendix" in the theory. It looks like there might be around 20 references to check. I plan to compare those references with the appendices themselves. I expect to uncover about 5 to 10 issues, but I want to be thorough in my review. So, I should be exhaustive in my inspection to ensure I don't miss anything important!
codex
I’ve reduced the seam to a finite set of imports. I’m now reading the high-risk transitions first: appendix-sourced definitions used in theory, appendix theorems imported back into core theory chapters, and appendix chapters that themselves lean on the same theory surface.
exec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '90,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/notation_index.tex | sed -n '340,360p;470,500p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    90	projections of a single incidence correspondence on the
    91	Fulton--MacPherson compactification~$\ConfigSpace{n}$.
    92	The geometry is developed in
    93	\S\ref{subsec:ran-universal} and
    94	Chapter~\ref{chap:bar-cobar-adjunction}; here we focus on the
    95	algebraic avatar: \emph{classical Koszul duality}.
    96	
    97	\section{Classical Koszul duality}
    98	\label{sec:classical-koszul-foundation}
    99	
   100	\subsection{Quadratic algebras and Koszul duality}
   101	
   102	\begin{definition}[Quadratic algebra]
   103	\label{def:quadratic-algebra}
   104	\index{quadratic algebra|textbf}
   105	A graded algebra $A = T(V)/I$ is \emph{quadratic} if:
   106	\begin{enumerate}
   107	\item $V$ is a graded vector space (generators)
   108	\item $I \subset V \otimes V$ is a subspace of relations in degree 2
   109	\item The defining ideal is $(I)$ generated by $I$
 succeeded in 52ms:
   340	\end{definition}
   341	
   342	\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic}
   343	The algebraic bar complex is represented by the DG coalgebra model of Theorem~\ref{thm:bar-coalgebra}.
   344	\end{definition}
   345	
   346	\begin{definition}[Geometric bar complex]\label{def:geometric-bar-complex}
   347	The geometric bar complex is Definition~\ref{def:geometric-bar}.
   348	\end{definition}
   349	
   350	\begin{definition}[Central charge]\label{def:central-charge}
   351	Central charge is the anomaly/curvature parameter appearing in the genus-corrected chiral package; see Example~\ref{ex:virasoro-central-charge-curvature}.
   352	\end{definition}
   353	
   354	\begin{definition}[Chiral algebra (BD)]\label{def:chiral-algebra-bd}
   355	We use Beilinson--Drinfeld chiral algebras as implemented in Theorem~\ref{thm:chiral-factorization}.
   356	\end{definition}
   357	
   358	\begin{construction}[Chiral bracket]\label{constr:chiral-bracket}
   359	The chiral bracket is encoded by residue/locality operations as in Theorem~\ref{thm:residue-operations}.
exec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '60,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1100,1145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2860,2985p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '520,550p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1100	\begin{example}[Ternary operation and associativity]
  1101	For three operators at $z_1, z_2, z_3$:
  1102	\begin{itemize}
  1103	\item The 2-form: $\eta_{12} \wedge \eta_{23} = d\log(z_1-z_2) \wedge d\log(z_2-z_3)$
  1104	\item Has poles along three divisors:
  1105	 \begin{itemize}
  1106	 \item[$D_{12}$:] where $z_1 = z_2$ first
  1107	 \item[$D_{23}$:] where $z_2 = z_3$ first
  1108	 \item[$D_{123}$:] where all three collide
  1109	 \end{itemize}
  1110	\item The residues give:
  1111	\[\text{Res}_{D_{12}}[\eta_{12} \wedge \eta_{23}] = m_2(m_2(a,b),c)\]
  1112	\[\text{Res}_{D_{23}}[\eta_{12} \wedge \eta_{23}] = m_2(a,m_2(b,c))\]
  1113	\[\text{Res}_{D_{123}}[\eta_{12} \wedge \eta_{23}] = m_3(a,b,c)\]
  1114	\item The difference of boundary residues equals an exact form:
  1115	\[m_2(m_2 \otimes \text{id}) - m_2(\text{id} \otimes m_2) = d(h_3)\]
  1116	where $h_3$ is the homotopy between associations
  1117	\end{itemize}
  1118	\end{example}
  1119	
 succeeded in 53ms:
    60	$T(z)$ & $T(w)$ & $\frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}$ \\
    61	$W^{(s)}(z)$ & $W^{(t)}(w)$ & $\sum_u \frac{C^u_{st} W^{(u)}(w)}{(z-w)^{s+t-u}}$ \\
    62	$e^\alpha(z)$ & $e^\beta(w)$ & $(z-w)^{(\alpha,\beta)} e^{\alpha+\beta}(w)$ \\
    63	\hline
    64	\end{tabular}
    65	\end{center}
    66	 
    67	\chapter{\texorpdfstring{Arnold relations for small $n$}{Arnold relations for small n}}
    68	\label{app:arnold-relations-small-n}
    69	
    70	Arnold relations for logarithmic forms:
    71	 
    72	\emph{$n = 3$.}
    73	\[
    74	\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0
    75	\]
    76	
    77	\emph{$n = 4$ (four 3-term Arnold relations, one for each triple $\{i,j,k\} \subset \{1,2,3,4\}$).}
    78	\begin{align*}
    79	\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} &= 0 \\
 succeeded in 51ms:
  2860	due to the vanishing of the Verma modules beyond the
  2861	affine Weyl chamber.
  2862	\end{remark}
  2863	
  2864	\begin{computation}[BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat}
  2865	at generic level; \ClaimStatusProvedHere]
  2866	\label{comp:bgg-sl2-pipeline}
  2867	\index{BGG resolution!explicit pipeline}
  2868	\index{bar complex!BGG pipeline}
  2869	We trace the bar complex of $\widehat{\mathfrak{sl}}_{2,k}$ through
  2870	the BGG spectral sequence (Theorem~\ref{thm:bgg-from-bar}) step by
  2871	step, connecting the explicit bar differential matrix
  2872	(Computation~\ref{comp:sl2-bar-matrix}) to the classical BGG
  2873	resolution, and verifying compatibility with Koszul duality
  2874	(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
  2875	(Theorem~\ref{thm:screening-bar}). \emph{Step~1: Weight decomposition of the bar complex.}
  2876	The bar differential $d\colon \bar{B}^2 \to \bar{B}^1$
  2877	(eq.~\eqref{eq:sl2-bar-matrix}) decomposes under the adjoint
  2878	$\mathfrak{h}$-action into weight sectors:
  2879	\begin{center}
 succeeded in 51ms:
   520	The representation $V_a\otimes V_b$ is defined by the coproduct
   521	$\Delta(T(u))=T(u)\dot\otimes T(u)$ applied to the evaluation
   522	homomorphisms at $a$ and~$b$ respectively. The $R$-matrix
   523	intertwiner is the Yang $R$-matrix evaluated at $u=a-b$, which is
   524	invertible for $a\neq b$ (and has rank-$1$ kernel $\bigwedge^2 V$ at
   525	$a-b=\hbar$). Irreducibility for generic $a-b$ follows from the
   526	standard Drinfeld criterion.
   527	\end{proof}
   528	
   529	\subsubsection*{The open-colour Koszul dual identification}
   530	
   531	\begin{theorem}[Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$
   532	is $Y_\hbar(\mathfrak{sl}_2)$; \ClaimStatusProvedHere]
   533	\label{thm:sl2-koszul-dual}
   534	Let $\mathcal A=\widehat{\mathfrak{sl}}_2$ at level~$k\neq -2$. The
   535	open-colour Koszul dual
   536	\[
   537	\mathcal A^!_{\mathrm{line}}
   538	\;=\;
   539	H^*\bigl(\Barch^{\mathrm{ord}}(\mathcal A)\bigr)^\vee
codex
The first concrete risk surfaced immediately: `algebraic_foundations` is importing a definition from the notation appendix, which is exactly the wrong dependency direction for a foundational chapter. I’m checking whether that’s isolated or part of a broader circular seam.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '16520,16545p;17528,17544p;18088,18105p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1548,1648p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/koszul_reference.tex | sed -n '260,290p;430,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '1,40p;450,540p;560,610p;720,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '70,95p;3790,3815p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3258,3290p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1548	\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
  1549	\label{thm:chain-vs-homology}
  1550	Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
  1551	\begin{enumerate}[label=\textup{(\roman*)}]
  1552	\item \emph{Chain level.}
  1553	 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
  1554	 all operations are computable via configuration space integrals,
  1555	 and homotopies have geometric meaning as forms on
  1556	 $\overline{C}_n(X)$.
  1557	\item \emph{Homology level.}
  1558	 The homotopy transfer theorem
  1559	 (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
  1560	 $A_\infty$ structure $\{m_k^H\}$ on $H^*(\mathcal{A})$ with
  1561	 $m_1^H = 0$. The product $m_2^H$ descends to homology
  1562	 (it is strictly associative if $\mathcal{A}$ is formal).
  1563	 However, the transferred higher operations
  1564	 $m_k^H$ for $k \geq 3$ are in general \emph{non-trivial}:
  1565	 they are the Massey products, encoding obstructions to formality.
  1566	\item \emph{What is lost.}
  1567	 The explicit chain-level homotopies $\{h_n\}$ (the contracting
 succeeded in 53ms:
   260	\end{question}
   261	
   262	\begin{remark}\label{rem:why-essential-image-matters}
   263	The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
   264	\end{remark}
   265	
   266	\subsection{Main characterization theorem}
   267	
   268	\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
   269	A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
   270	$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:
   271	
   272	\begin{enumerate}
   273	\item \emph{Conilpotency.} $\widehat{\mathcal{C}}$ is conilpotent: every element of $\ker(\epsilon)$ is annihilated by a sufficiently high iterate of the reduced coproduct $\bar{\Delta}$:
   274	 \[\ker(\epsilon) = \bigcup_{n \geq 0} \ker(\bar{\Delta}^{(n)})\]
   275	 
   276	\item \emph{Connected.} The counit is surjective onto the ground field:
   277	 \[\epsilon: \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}\]
   278	 
   279	\item \emph{Geometric representability.} $\widehat{\mathcal{C}}$ admits a presentation as sections of a $\mathcal{D}_X$-module coalgebra on the Ran space of~$X$; equivalently, there exists a factorization coalgebra~$\mathcal{F}$ such that $\widehat{\mathcal{C}} \simeq \Gamma(\mathrm{Ran}(X),\, \mathcal{F})$, compatible with the operadic structure of the Fulton--MacPherson compactification
 succeeded in 51ms:
    70	\eta_{ij} \wedge \eta_{jk}
    71	+ \eta_{jk} \wedge \eta_{ki}
    72	+ \eta_{ki} \wedge \eta_{ij} = 0
    73	\qquad (i,j,k \text{ distinct}).
    74	\end{equation}
    75	Third, this relation forces $d_{\mathrm{residue}}^2 = 0$
    76	(Theorem~\ref{thm:bar-nilpotency-complete}): the
    77	bar differential at degree~$2$ is a sum of double residues
    78	at pairs of collision divisors $D_{ij} \cap D_{jk}$, and
    79	the Arnold relation is the precise cancellation identity
    80	ensuring that these contributions sum to zero. The
    81	equivalence between the Arnold relation and nilpotency of
    82	the bar differential is
    83	Theorem~\ref{thm:arnold-iff-nilpotent}; at genus~$0$ the
    84	Arnold relation is the \emph{only} obstruction, and its
    85	vanishing gives $d^2 = 0$ unconditionally. At
    86	genus~$g \geq 1$, the Arnold relation is modified by
    87	elliptic corrections
    88	(Proposition~\ref{prop:elliptic-arnold-relations}), and
    89	the failure of strict nilpotency is measured by the
 succeeded in 52ms:
     1	\chapter{Homotopy transfer}
     2	\label{app:homotopy-transfer}
     3	
     4	\index{homotopy transfer theorem|textbf}
     5	
     6	The homotopy
     7	transfer theorem is the mechanism by which classical Koszul duality
     8	acquires quantum corrections. Passing from a chain complex to its
     9	cohomology via a deformation retract necessarily introduces higher
    10	operations $m_k$ for $k \geq 3$; these are precisely the genus-$0$
    11	quantum corrections of the bar complex
    12	(Theorem~\ref{thm:bar-ainfty-complete}).
    13	
    14	\begin{proposition}[Homotopy transfer as rectification mechanism]
    15	\label{prop:htt-rectification}
    16	\ClaimStatusProvedHere
    17	The homotopy transfer theorem is the technical engine of the
    18	rectification meta-theorem
    19	(Theorem~\ref{thm:rectification-meta}): given a deformation retract
    20	$V \xrightarrow{p} H \xrightarrow{i} V$ with $pi = \mathrm{id}$
 succeeded in 51ms:
  3258	complex it is, and thence the Koszul dual. Three functors act on
  3259	$\widehat{\mathcal{C}}$, producing three distinct objects \begin{itemize}
  3260	\item \textbf{Cobar}: $\Omega(\widehat{\mathcal{C}})$ recovers the
  3261	 \emph{original} algebra $\cA$ when
  3262	 $\widehat{\mathcal{C}} = \barB(\cA)$.
  3263	\item \textbf{Verdier dual}:
  3264	 $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \cA^!_\infty$
  3265	 produces the homotopy Koszul dual \emph{algebra}; equivalently,
  3266	 $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \barB(\cA^!)$
  3267	 as factorization coalgebras
  3268	 \textup{(}Convention~\ref{conv:bar-coalgebra-identity}\textup{)}.
  3269	 These are two descriptions of the same object: the
  3270	 identification of $\cA^!_\infty$ with $\barB(\cA^!)$ is the content
  3271	 of Theorem~A.
  3272	\end{itemize}
  3273	
  3274	\emph{Step 1: Check necessary conditions}
  3275	(Theorem~\ref{thm:essential-image-koszul}):
  3276	\begin{itemize}
  3277	\item[$\square$] Conilpotent? ($\bigcap_n \text{coker}(\Delta^n) = 0$)

thinking
**Inspecting relevant definitions**

I need to look into definitions related to bar construction. It seems there may be specific terms and guidelines I should be aware of. I'll gather information to ensure I'm considering all necessary aspects. I wonder if there are codes or standards that I'm missing. It feels important to make sure I cover everything related to bar construction thoroughly. Let’s point out any critical definitions I come across and keep those in mind moving forward.
codex
I’m checking the imported theorem bodies now. The next question is whether the appendix actually proves what the theory chapter says it proves, or whether the theory is leaning on a summary/result that itself depends back on the same chapter.
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '130,190p;760,790p;1788,1832p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '160,188p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '16526,16542p;17532,17542p;18092,18104p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   160	\item $n=5$: $\binom{5}{3} = 10$ relations (similarly)
   161	\end{itemize}
   162	\end{remark}
   163	
   164	\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
   165	The Arnold relations ensure $d^2 = 0$ for the geometric bar differential:
   166	\[d^2 = \sum_{\text{cycles}} [\operatorname{Res}_{D_i}, \operatorname{Res}_{D_j}] = 0\]
   167	because the residue commutators sum to zero by Arnold relations.
   168	\begin{proof}
   169	This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
   170	\end{proof}
   171	\end{corollary}
   172	
   173	\subsection{Attribution}
   174	
   175	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
   176	
   177	\section{Arnold relations in bar differential nilpotency}
   178	\label{sec:arnold-in-bar-nilpotency}
   179	
 succeeded in 51ms:
   130	graded by genus~$g$ (homological weight) and degree~$n$, with
   131	\begin{enumerate}[label=\textup{(\roman*)}]
   132	\item \textbf{Differential}
   133	 $d_{\partial}\colon \gAmod \to \gAmod$
   134	 induced by the boundary stratification
   135	 $\partial\overline{\mathcal{M}}_{g,n} \hookrightarrow
   136	 \overline{\mathcal{M}}_{g,n}$, i.e.\ by pullback along the
   137	 clutching morphisms of the Deligne--Mumford modular operad;
   138	\item \textbf{Bracket}
   139	 $[\,\cdot\,,\,\cdot\,]\colon
   140	 \gAmod \otimes \gAmod \to \gAmod$
   141	 given by operadic composition via stable-graph gluing:
   142	 for $f$ in the $(g_1,n_1)$-component and
   143	 $g$ in the $(g_2,n_2)$-component of~$\gAmod$, the bracket
   144	 $[f,g]_{g,n}$ is the signed sum over all stable graphs of
   145	 genus~$g = g_1 + g_2$ (or $g = g_1 + g_2 + 1$ for
   146	 self-gluing) obtained by inserting the output of~$g$
   147	 into an input of~$f$ and composing with the
   148	 Deligne--Mumford clutching map.
   149	\end{enumerate}
 succeeded in 52ms:

exec
/bin/zsh -lc "nl -ba appendices/koszul_reference.tex | sed -n '80,100p;120,132p;166,186p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1068,1088p;2948,2972p;3068,3092p;3360,3380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12590,12620p;16570,16610p;17860,17955p;30330,30650p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    80	The formula $\mathcal{A}^! = \bigoplus_g \operatorname{Ext}^*_{\mathcal{A}^{(g)}}(\mathbb{k},\mathbb{k})$
    81	is the \emph{classical} (BGS) Koszul dual, valid when each $\mathcal{A}^{(g)}$ is a
    82	classical quadratic algebra. For the chiral Koszul dual (Definition~\ref{def:chiral-koszul-pair}),
    83	the bar construction replaces $\operatorname{Ext}$; the two coincide on the classical locus but
    84	diverge for general vertex algebras (see Remark~\ref{rem:classical-vs-chiral-koszulness}).
    85	\end{theorem}
    86	
    87	\begin{proof}
    88	This is Theorem~\ref{thm:genus-graded-koszul-duality} in
    89	\S\ref{app:koszul_higher_genus}, proved by applying the $\Eone$-chiral Koszul
    90	duality (Theorem~\ref{thm:e1-chiral-koszul-duality}) genus by genus, with
    91	nilpotence ensured by Theorem~\ref{thm:genus-induction-strict} and
    92	involutivity by bar-cobar inversion
    93	(Theorem~\ref{thm:bar-cobar-inversion-qi}).
    94	\end{proof}
    95	
    96	\subsection{Genus-graded chiral Koszul duality}
    97	
    98	For chiral algebras across all genera, a modified definition is needed:
    99	
 succeeded in 51ms:
 12590	\index{soft graviton!cubic shadow}
 12591	\index{Lie bracket!determines cubic shadow}
 12592	On the Virasoro $T$-line, the cubic shadow coefficient is
 12593	$\operatorname{Sh}_3\big|_T = 2$ (the Sugawara normal-ordering
 12594	constant, independent of~$c$).
 12595	Therefore $\Delta^{(3,0)}\big|_T = 2 + 2 = 4$ for every
 12596	chirally Koszul algebra with a Virasoro subalgebra, including
 12597	all principal $\mathcal{W}_N$ ($N = 2, \ldots, 6$ verified) and the
 12598	non-principal Bershadsky--Polyakov algebra
 12599	(Computation~\ref{comp:bp-shadow-tower}).
 12600	This value $4$ is the second universal invariant of the
 12601	$\sigma$-invariant shadow ring, after
 12602	$\Delta^{(2)} = K_\fg / 2$.
 12603	
 12604	The universality has a structural explanation.
 12605	The degree-$3$ shadow $\operatorname{Sh}_3$ is the projection of
 12606	the transferred cubic $A_\infty$-operation $m_3$ through
 12607	the shadow functor. For affine algebras, $m_3$ \emph{is} the Lie
 12608	bracket transported through the bar complex
 12609	(Theorem~\ref{thm:nms-affine-cubic-normal-form}): the only ternary
 succeeded in 51ms:
  1068	chain groups $\dim\Lambda^1_3 = 3$,
  1069	$\dim\Lambda^2_3 = 9$,
  1070	$\dim\Lambda^3_3 = 1$; differential ranks
  1071	$3$ and $1$; cohomology
  1072	$(9 - 1) - 3 = 5$).
  1073	The computation is verified by checking $d_1^2 = 0$
  1074	at each weight (Computation~\ref{comp:sl2-ce-verification}).
  1075	\end{proof}
  1076	
  1077	\begin{remark}[CE cohomology vs exterior algebra dimensions]
  1078	\label{rem:ce-vs-exterior}
  1079	\index{bar complex!CE vs exterior algebra}
  1080	Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
  1081	\end{remark}
  1082	
  1083	\begin{remark}[Chevalley--Eilenberg cohomology vs chiral bar cohomology]%
  1084	\label{rem:ce-vs-chiral-bar}%
  1085	\index{Chevalley--Eilenberg cohomology!vs chiral bar}%
  1086	\index{bar complex!vs CE cohomology}%
  1087	\index{Witt algebra!CE vs bar}%
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '16526,16542p;17532,17542p;18092,18104p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30404,30412p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 51ms:
 30404	\item \emph{Shadow obstruction tower}: projecting onto the degree-$r$ component of $\Defcyc^{\mathrm{mod}}(\cA)$ gives the shadow $\mathrm{Sh}_r(\cA)$, and the MC equation projected to degree $r$ gives the all-degree master equation $\nabla_H(\mathrm{Sh}_r) + o^{(r)} = 0$ (Proposition~\ref{prop:master-equation-from-mc});
 30405	\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
 30406	\item \emph{Complementarity}: the Lagrangian decomposition of Theorem~C is the polarization into $\cA$-side and $\cA^!$-side components (under perfectness hypotheses).
 30407	\end{enumerate}
 30408	At the full all-degree level, these structures are
 30409	proved consequences of the bar-intrinsic construction
 30410	(Theorem~\ref{thm:mc2-bar-intrinsic}): the limit
 30411	$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ exists
 30412	and is Maurer--Cartan.

thinking
**Troubleshooting command issues**

It seems my first command isn't outputting anything, possibly due to a large file size or something with the "sed" command. That’s a bit odd. Maybe there’s an issue with how I quoted the command? I should try running a simpler version instead to see if I can narrow down the problem. Let’s explore that and see if it helps clarify things!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '16526,16542p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


thinking
**Checking file structure**

I’m wondering if I should use a shorter file to avoid high line numbers. If I run `nl -ba`, it could output zero if the file is too long. There might also be an issue with carriage return (CR) characters. I should check if the file has any actual lines by using `wc -l` to confirm whether any lines exist or if the count is zero.
exec
/bin/zsh -lc 'wc -l chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    2359 chapters/theory/bar_construction.tex


thinking
**Clarifying line numbers**

I'm working through how the cross-reference parser uses cumulative line numbers across multiple files with Perl, and I realize that line numbers for definitions and labels are cumulative, not per file. I need the actual line numbers, so I should use commands like `rg -n` or `nl -ba` for accuracy. I'll ensure that when mapping appendix to theory, I'm referencing the correct lines from the right files. It's important to inspect these actual line numbers closely!
thinking
**Finding actual line numbers**

I've confirmed that the definition for `def:bar-complex-algebraic` is at line 342 in the notation index, which is great. I also need to check that the line for `theorem:sl2-koszul-dual` in the appendix is indeed at line 533, as noted in earlier output. Now, I should inspect the actual lines for `bar_construction` and the relevant labels. I'll use `rg -n` to find the actual line numbers for `def:geometric-bar`, `thm:bar-coalgebra`, and `thm:geometric-equals-operadic-bar`.
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:geometric-bar\\}|\\\\label\\{thm:bar-coalgebra\\}|\\\\label\\{thm:geometric-equals-operadic-bar\\}|\\\\label\\{sec:bar-nilpotency\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
502:\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%
786:\subsection{\texorpdfstring{Proof that $d^2 = 0$: nine-term verification}{Proof that d2 = 0: nine-term verification}}\label{sec:bar-nilpotency-nine-terms-complete}\label{sec:bar-nilpotency}
1505:\begin{theorem}[Bar coalgebra; \ClaimStatusProvedHere]\label{thm:bar-coalgebra}
2065:\label{thm:geometric-equals-operadic-bar}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:mc2-bar-intrinsic\\}|\\\\label\\{prop:master-equation-from-mc\\}|\\\\label\\{thm:nms-affine-cubic-normal-form\\}|\\\\label\\{thm:nms-clutching-law-modular-resonance\\}|\\\\label\\{thm:nms-all-degree-master-equation\\}' appendices/nonlinear_modular_shadows.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:genus-graded-koszul-duality\\}|\\\\label\\{lem:genus-graded-koszul-resolution\\}|\\\\label\\{thm:genus-graded-mc\\}|\\\\label\\{thm:bar-cobar-inversion-qi\\}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 67ms:
chapters/theory/higher_genus_modular_koszul.tex:3528:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:12359:\label{prop:master-equation-from-mc}
appendices/nonlinear_modular_shadows.tex:1038:\label{thm:nms-affine-cubic-normal-form}
appendices/nonlinear_modular_shadows.tex:1823:\label{thm:nms-clutching-law-modular-resonance}
appendices/nonlinear_modular_shadows.tex:2110:\label{thm:nms-all-degree-master-equation}
 succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1611:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
chapters/theory/higher_genus_modular_koszul.tex:325:\label{thm:genus-graded-koszul}\label{thm:genus-graded-koszul-duality}\label{thm:extended-koszul}
chapters/theory/higher_genus_modular_koszul.tex:356:\label{lem:genus-graded-koszul-resolution}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:genus-graded-mc\\}' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:2099:\begin{theorem}[Maurer--Cartan = deformations {\cite{Kon03,Ger63}}; \ClaimStatusProvedElsewhere]\label{thm:genus-graded-mc}

thinking
**Clarifying mathematical definitions**

I need to find an exact fix for the definition and theory section. I think I should either move the actual definition into the theory or replace the appendix reference with theorem `thm:bar-coalgebra` or a formula like `\bar{B}(A)=T^c(s^{-1}\bar A)`. 

Also, I should rephrase the line about the bar construction for clarity, and stop relying on `def:bar-complex-algebraic` as a source in the theory, leaving it as a cross-reference in the appendix.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:sl2-koszul-dual\\}|-k-4|k\\+2|1/\\(k\\+2\\)' appendices/_sl2_yangian_insert.tex chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '531,590p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
appendices/_sl2_yangian_insert.tex:49:\hbar\;=\;\frac{1}{k+h^\vee}\;=\;\frac{1}{k+2}\,.
appendices/_sl2_yangian_insert.tex:240:points\textup{)}, and $\hbar=1/(k+2)$.
appendices/_sl2_yangian_insert.tex:533:\label{thm:sl2-koszul-dual}
appendices/_sl2_yangian_insert.tex:543:$\hbar=1/(k+2)$:
appendices/_sl2_yangian_insert.tex:550:\hbar=\frac{1}{k+2}.
appendices/_sl2_yangian_insert.tex:587:The parameter $\hbar=1/(k+2)$ arises from
appendices/_sl2_yangian_insert.tex:601:$-k-2h^\vee=-k-4$ (Verdier-level duality). The open-colour
chapters/theory/chiral_modules.tex:1145:at $c = 1 - 6(k+1)^2/(k+2)$; for $\fg = \mathfrak{sl}_N$, it
chapters/theory/chiral_modules.tex:1183:model $\mathcal{M}(k+2, k+3)$ at $c = 1 - 6/((k+2)(k+3))$.
chapters/theory/chiral_modules.tex:1903: produces a Virasoro algebra with $c = 1 - 6(k+1)^2/(k+2)$.
chapters/theory/chiral_modules.tex:2945:Under $k \mapsto -k - 2h^\vee = -k-4$
chapters/theory/chiral_modules.tex:2952:\simeq \mathcal{M}(w \cdot \Lambda_0)_{-k-4},
chapters/theory/chiral_modules.tex:2956:level~$-k-4$ with identical Weyl group combinatorics.
chapters/theory/chiral_modules.tex:2958:$\det S_1(-k-4) = -\det S_1(k)$
chapters/theory/chiral_modules.tex:3387:\cong \widehat{\mathfrak{sl}}_{2,-k-4}$, becomes the vacuum Verma at
chapters/theory/chiral_modules.tex:3390:\Phi(\mathcal{M}(0)_k) \simeq \mathcal{M}(0)_{-k-4}
chapters/theory/chiral_modules.tex:3393:$\mathrm{Mod}^{\mathrm{compl}}_{\widehat{\mathfrak{sl}}_{2,-k-4}}$
chapters/theory/chiral_modules.tex:3406:\cong \widehat{\mathfrak{sl}}_{2,-k-4}$ is justified; off this lane the
chapters/theory/chiral_modules.tex:3446:\cong \widehat{\mathfrak{sl}}_{2,-k-4}$
chapters/theory/chiral_modules.tex:3448:cofree comodule into the complete $\widehat{\mathfrak{sl}}_{2,-k-4}$-module
 succeeded in 57ms:
   531	\begin{theorem}[Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$
   532	is $Y_\hbar(\mathfrak{sl}_2)$; \ClaimStatusProvedHere]
   533	\label{thm:sl2-koszul-dual}
   534	Let $\mathcal A=\widehat{\mathfrak{sl}}_2$ at level~$k\neq -2$. The
   535	open-colour Koszul dual
   536	\[
   537	\mathcal A^!_{\mathrm{line}}
   538	\;=\;
   539	H^*\bigl(\Barch^{\mathrm{ord}}(\mathcal A)\bigr)^\vee
   540	\]
   541	is isomorphic, as a filtered associative algebra with spectral parameter,
   542	to the Yangian $Y_\hbar(\mathfrak{sl}_2)$ at deformation parameter
   543	$\hbar=1/(k+2)$:
   544	\begin{equation}\label{eq:koszul-dual-id-sl2}
   545	\boxed{
   546	\mathcal A^!_{\mathrm{line}}
   547	\;\cong\;
   548	Y_\hbar(\mathfrak{sl}_2),
   549	\qquad
   550	\hbar=\frac{1}{k+2}.

thinking
**Inspecting theorem proof lines**

I'm noticing something about line 601 of the theorem proof that mentions `-k-4`, which could relate to Verdier-level duality. I think I should examine the lines around 596 to 604 to get a better understanding. It's interesting to see how different concepts might come together in this context, so I'll dig into those lines to clarify what this proof is indicating. It could lead to some exciting insights!
exec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '594,606p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   594	\end{proof}
   595	
   596	\begin{remark}[Comparison with the closed-colour dual]
   597	\label{rem:closed-vs-open-sl2}
   598	The closed-colour (symmetric, Francis--Gaitsgory) Koszul dual of
   599	$\widehat{\mathfrak{sl}}_2$ at level~$k$ is
   600	$\mathcal A^!_{\mathrm{ch}}=\widehat{\mathfrak{sl}}_2$ at level
   601	$-k-2h^\vee=-k-4$ (Verdier-level duality). The open-colour
   602	Koszul dual is the \emph{finite-type} Yangian $Y_\hbar(\mathfrak{sl}_2)$.
   603	The input is the affine algebra; the closed output is another
   604	affine algebra (at dual level); the open output is a finite-type
   605	quantum group with spectral parameter. The cross-colour datum is the
   606	$R$-matrix: $\Barch(\mathcal A)_n\simeq
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3238,3295p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3238	The equivalences (a)$\Leftrightarrow$(b)$\Leftrightarrow$(c)$\Leftrightarrow$(d)
  3239	are proved (Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity}).
  3240	The implication (e)$\Rightarrow$(d) is proved; the converse is open.
  3241	Item~(f) is conditional on perfectness (proved unconditionally for the
  3242	standard landscape, Corollary~\ref{cor:lagrangian-unconditional}).
  3243	The full equivalence of all six would parallel the classical theorem
  3244	that Koszulness, purity, formality, and derived equivalence coincide
  3245	for graded algebras arising from geometry~\cite{BGS96}.
  3246	\end{remark}
  3247	
  3248	%================================================================
  3249	% RECOGNIZING KOSZUL DUALS IN PRACTICE
  3250	%================================================================
  3251	
  3252	\section{Recognizing Koszul duals in practice}
  3253	\label{sec:recognizing-koszul-duals}
  3254	
  3255	\begin{remark}[Identifying \texorpdfstring{$\mathcal{A}^!$}{A!} in practice]\label{rem:identify-koszul-wild}
  3256	When encountering a coalgebra $\widehat{\mathcal{C}}$ in geometry or
  3257	physics, the following procedure identifies the algebra whose bar



thinking
**Evaluating theorem citation**

I’m thinking about the remark and its relationship with the appendix theorem. The user wants to avoid circular dependencies. I can cite the appendix theorem without it being circular since it’s mentioned after the inversion theorem. 

However, there’s a potential local cycle since the appendix theorem’s proof refers back to something in the chapter. It seems tricky because it’s not truly independent support. The user is asking me to check if appendix results are cited correctly in the body.
thinking
**Checking citation accuracy**

I’m analyzing how the body cites a theorem as a checklist, but it’s actually a corollary of a body theorem, so it should be referred to differently. It seems to be more like a checklist/reformulation instead of a supporting theorem. 

Now, there’s this concern about the `koszul_reference` theorem claiming "iff" conditions, which relies on another theorem that offers conditions. Since both rely on the inversion theorem, they aren't independently justified, although that doesn't make them false. I need to dive into stronger findings to clarify this. There's also a statement in `configuration_spaces.tex` regarding the nilpotency condition, which feels incomplete.
thinking
**Inspecting theory references**

I’m looking at the theory sentence that states "its vanishing gives d^2=0 unconditionally," possibly through bar_nilpotency_complete. That seems okay for now. There’s a mention at line 3804 that I’ll need to inspect later for clarity. It was referenced in the `construction` section, so it might not be an issue after all. I’ll keep this in mind as I move forward to ensure everything aligns correctly.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '490,515p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   490	 corresponding to the stratum~$\partial_S$.
   491	\end{itemize}
   492	\end{definition}
   493	
   494	\begin{theorem}[\texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations;
   495	\ClaimStatusProvedHere]
   496	\label{thm:e2-d-squared}
   497	\index{Totaro relations!and $d^2 = 0$}
   498	The differential $d_{\Etwo}$ of
   499	Definition~\textup{\ref{def:e2-bar-complex}} satisfies
   500	$d_{\Etwo}^2 = 0$.
   501	\end{theorem}
   502	
   503	\begin{proof}
   504	The proof follows the same structure as the chiral case
   505	(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
   506	relations replaced by Totaro relations.
   507	
   508	We compute $d_{\Etwo}^2$ on a bar element
   509	$\alpha \in \Omega^*(\overline{\Conf}_k(\bR^2))
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1128,1168p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '946,976p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1026,1072p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1026	\label{subsec:nms-affine-sl2}
  1027	
  1028	\begin{definition}[Strict current-level sector]
  1029	\label{def:nms-affine-sector}
  1030	For the affine current algebra $\widehat{\mathfrak{sl}}_{2,k}$, let
  1031	\[
  1032	V_{\mathrm{aff}}:=\mathfrak{sl}_2[1]\oplus \mathbb C\,K[1]
  1033	\]
  1034	be the strict current-level sector generated by the current algebra and the level direction.
  1035	\end{definition}
  1036	
  1037	\begin{theorem}[Affine cubic normal form; \ClaimStatusProvedHere]
  1038	\label{thm:nms-affine-cubic-normal-form}
  1039	On the strict current-level sector one has
  1040	\[
  1041	\mathfrak C_{\mathrm{aff}}(x,y,z)=\kappa(x,[y,z]),
  1042	\qquad
  1043	\mathfrak o_{\mathrm{aff}}^{(4)}=0.
  1044	\]
  1045	Consequently there exists a quartic gauge in which
 succeeded in 52ms:
   946	(Proposition~\ref{prop:self-referentiality-criterion}).
   947	At higher rank, lattice vertex algebras achieve finite depths $5, 6, 7, \dotsc$ through independent cusp forms in $M_{r/2}$ (Theorem~\ref{thm:shadow-spectral-correspondence}).
   948	We now compute the three low-rank patterns in the frame families.
   949	
   950	\subsection{Heisenberg}
   951	\label{subsec:nms-heisenberg}
   952	
   953	\begin{theorem}[Heisenberg exact linearity; \ClaimStatusProvedHere]
   954	\label{thm:nms-heisenberg-exact-linearity}
   955	On the Heisenberg deformation line one has
   956	\[
   957	\mathfrak C_{\mathcal H}=0,
   958	\qquad
   959	\mathfrak o_{\mathcal H}^{(4)}=0,
   960	\qquad
   961	\mathfrak Q_{\mathcal H}=0.
   962	\]
   963	Equivalently,
   964	\[
   965	\Theta_{\mathcal H}^{\le 4}=H_{\mathcal H}.
 succeeded in 53ms:
  1128	$\mathfrak{R}^{\mathrm{oc}}_4(\widehat{\mathfrak{g}}_k)
  1129	= [\mathfrak{C} \star_{P} \mathfrak{C}] \in \cZ^2$
  1130	(Theorem~\ref{thm:thqg-oc-quartic-vanishing}(ii)).
  1131	This is the trace of cubic graviton exchange across a boundary node.
  1132	\end{remark}
  1133	
  1134	\subsection{The \texorpdfstring{$\beta\gamma$}{betagamma} system}
  1135	\label{subsec:nms-betagamma}
  1136	
  1137	\begin{definition}[Weight/contact slice]
  1138	\label{def:nms-betagamma-slice}
  1139	Let $V_{\beta\gamma}$ be the minimal cyclic slice generated by the explicit weight-changing deformation class and the first contact class detected by the first nontrivial higher operation $m_3$.
  1140	\end{definition}
  1141	
  1142	\begin{theorem}[\texorpdfstring{$\beta\gamma$}{betagamma} quartic birth; \ClaimStatusProvedHere]
  1143	\label{thm:nms-betagamma-quartic-birth}
  1144	On the weight/contact slice one has
  1145	\[
  1146	\mathfrak C_{\beta\gamma}=0,
  1147	\qquad
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1800,1845p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1800	On a separating boundary stratum there is a natural increasing filtration
  1801	\[
  1802	0\subset F^0\subset F^1=\xi^*\mathscr E_{g,n}^{[4]}(\cA)
  1803	\]
  1804	by internal-edge number such that the associated graded object splits canonically as
  1805	\begin{equation}
  1806	\label{eq:nms-associated-graded-boundary}
  1807	\operatorname{gr}\,\xi^*\mathscr E_{g,n}^{[4]}(\cA)
  1808	\cong
  1809	p_1^*\mathscr C_{g_1,n_1+1}^{\mathrm{ct}}(\cA)
  1810	\oplus
  1811	p_2^*\mathscr C_{g_2,n_2+1}^{\mathrm{ct}}(\cA)
  1812	\oplus
  1813	\mathscr T_{3,\xi}(\cA),
  1814	\end{equation}
  1815	where $p_1$ and $p_2$ are the two projections.
  1816	\end{theorem}
  1817	
  1818	\begin{proof}
  1819	At quartic order a vertex on the boundary can have either zero internal edges or one internal edge. Zero internal edges give the contact quartic sectors transported from the two components. One internal edge joining two cubic vertices gives the tree sector. No higher-edge contribution appears before quintic order. This yields the stated filtration and splitting on the associated graded.\qedhere

thinking
**Continuing to proofread**

I think I might need to continue working on the proof and possibly cite the main chapter or theorem to strengthen my argument. There's a sense that I need to add more lines to fully develop the thought process. It's like, how can I ensure everything is clear and well-supported? I guess I just need to take my time and ensure it's all well-organized before finalizing anything. Being thorough is key!
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1838,1868p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1838	\begin{proof}
  1839	By Theorem~\ref{thm:nms-boundary-filtration-quartic-envelope}, the associated graded of the pulled-back quartic envelope splits into the two contact bundles and the cubic tree bundle. The quartic clutching formula
  1840	\[
  1841	\xi^*\mathfrak Q_{\cA}
  1842	=
  1843	H_{\cA}\star\mathfrak Q_{\cA}
  1844	+
  1845	\mathfrak C_{\cA}\star\mathfrak C_{\cA}
  1846	+
  1847	\mathfrak Q_{\cA}\star H_{\cA}
  1848	\]
  1849	shows that, on the associated graded, the Gram pairing is block-upper-triangular with diagonal blocks given by the two contact pairings and the tree pairing. The determinant section therefore factors:
  1850	\[
  1851	\operatorname{gr}\,\xi^*s_{4,g,n}^{\mathrm{res}}(\cA)
  1852	=
  1853	p_1^*s_{4,g_1,n_1+1}^{\mathrm{res}}(\cA)
  1854	\otimes
  1855	p_2^*s_{4,g_2,n_2+1}^{\mathrm{res}}(\cA)
  1856	\otimes
  1857	s_{3,\xi}^{\mathrm{tree}}(\cA).
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1204,1228p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1204	Apply the quartic boundary recursion with $\mathfrak C_{\beta\gamma}=0$.\qedhere
  1205	\end{proof}
  1206	
  1207	\begin{theorem}[Primitive nonlinear archetype trichotomy; \ClaimStatusProvedHere]
  1208	\label{thm:nms-archetype-trichotomy}
  1209	Through quartic order, the three frame families realize the three primitive nonlinear archetypes:
  1210	\begin{enumerate}[label=\textup{(\roman*)}]
  1211	\item Heisenberg is Gaussian:
  1212	\[
  1213	\Theta_{\mathcal H}^{\le 4}=H_{\mathcal H}.
  1214	\]
  1215	\item Affine $\widehat{\mathfrak{sl}}_2$ is of Lie/tree type:
  1216	\[
  1217	\Theta_{\mathrm{aff}}^{\le 4}=H_{\mathrm{aff}}+\mathfrak C_{\mathrm{aff}},
  1218	\]
  1219	with quartic boundary term generated by $\mathfrak C_{\mathrm{aff}}\star \mathfrak C_{\mathrm{aff}}$.
  1220	\item The $\beta\gamma$ system is of contact/quartic type:
  1221	\[
  1222	\Theta_{\beta\gamma}^{\le 4}=H_{\beta\gamma}+\mathfrak Q_{\beta\gamma},
  1223	\]
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5118,5138p;5774,5790p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5118	$\ell_3^{\mathrm{tr}} \neq 0$ (Virasoro, $\mathcal{W}_N$).
  5119	\end{itemize}
  5120	The shadow obstruction tower is the homotopy structure made visible.
  5121	\end{remark}
  5122	
  5123	\begin{remark}[The three archetypes from the Lagrangian perspective]
  5124	\label{rem:three-archetypes-lagrangian}
  5125	The fake-complementarity criterion reframes the archetype trichotomy
  5126	(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
  5127	The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
  5128	Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
  5129	$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
  5130	so the dual Lagrangian bends cubically. The $\beta\gamma$ system is
  5131	quartic on the weight/contact slice. Virasoro is the first family
  5132	where the dual Lagrangian has both cubic and quartic bending,
  5133	and the complementarity potential is genuinely non-polynomial; its
  5134	shadow obstruction tower is infinite (Theorem~\ref{thm:nms-finite-termination}).
  5135	\end{remark}
  5136	
  5137	\begin{remark}[Shadow obstruction tower as period correction]
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '2170,2204p'" in /Users/raeez/chiral-bar-cobar succeeded in 70ms:
  2170	
  2171	\begin{theorem}[The Virasoro quintic is forced; \ClaimStatusProvedHere]
  2172	\label{thm:nms-virasoro-quintic-forced}
  2173	On the Virasoro quartic shadow envelope $E^{[4]}_{\mathrm{Vir}}$, the quintic obstruction is generically nonzero:
  2174	\begin{equation}
  2175	\label{eq:nms-virasoro-quintic-obstruction}
  2176	\mathfrak o_{\mathrm{Vir}}^{(5)}
  2177	=
  2178	\{\mathfrak C_{\mathrm{Vir}},\mathfrak Q^{\mathrm{contact}}_{\mathrm{Vir}}\}_{H_{\mathrm{Vir}}}
  2179	\neq 0
  2180	\qquad
  2181	\text{for generic $c$}.
  2182	\end{equation}
  2183	Consequently $\mathrm{Sh}_5(\mathrm{Vir})\neq 0$ generically: the Virasoro shadow obstruction tower does not terminate at quartic order.
  2184	\end{theorem}
  2185	
  2186	\begin{proof}
  2187	The gravitational cubic is $\mathfrak C_{\mathrm{Vir}}=2x^3$ and the contact quartic is $\mathfrak Q^{\mathrm{contact}}_{\mathrm{Vir}}=Q_0\,x^4$ with $Q_0=10/[c(5c+22)]\neq 0$ for generic~$c$. Their single-edge sewing contraction on the one-generator primary line with propagator $P=2/c$ produces a nonzero rank-$5$ tensor proportional to $Q_0/c$.\qedhere
  2188	\end{proof}
  2189	
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1498,1522p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1498	filtration (Theorem~\ref{thm:chevalley-cousin}). Any other admissible
  1499	model shares these properties by the same arguments, whence the
  1500	mapping space between them is contractible.
  1501	\end{proof}
  1502	
  1503	\subsection{Coalgebra structure}
  1504	
  1505	\begin{theorem}[Bar coalgebra; \ClaimStatusProvedHere]\label{thm:bar-coalgebra}
  1506	The bar complex carries a natural coalgebra structure:
  1507	\[\Delta: \bar{B}^{\text{geom}}(\mathcal{A}) \to \bar{B}^{\text{geom}}(\mathcal{A}) \otimes \bar{B}^{\text{geom}}(\mathcal{A})\]
  1508	induced by the diagonal map $X \to X \times X$.
  1509	This is the coshuffle coproduct on the symmetric bar $\mathrm{Sym}^c(s^{-1}\bar{\mathcal{A}})$, summing over all $2^n$ unordered bipartitions (Theorem~\textup{\ref{thm:three-bar-complexes}}\textup{(ii)}). The ordered bar $T^c(s^{-1}\bar{\mathcal{A}})$ carries a distinct deconcatenation coproduct with $n+1$ terms (Theorem~\textup{\ref{thm:three-bar-complexes}}\textup{(iii)}); the coshuffle is its $\Sigma_n$-symmetrization.
  1510	\end{theorem}
  1511	
  1512	\begin{proof}
  1513	Define $\Delta$ on tensors by summing over ordered bipartitions of the input
  1514	index set and restricting the logarithmic form to the corresponding boundary
  1515	factorization stratum, as in the explicit formula used in
  1516	Theorem~\ref{thm:coassociativity-complete}. This defines a morphism
  1517	$\bar{B}^{\mathrm{geom}}(\mathcal{A})\to
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:shadow-depth-classification\\}|\\\\label\\{thm:shadow-archetype-classification\\}|\\\\label\\{thm:betagamma-global-depth\\}|\\\\label\\{thm:w-virasoro-quintic-forced\\}|\\\\label\\{thm:heisenberg-formality\\}|\\\\label\\{thm:lattice-symmetric-ordered-bar\\}|\\\\label\\{thm:lattice-ordered-koszul-dual\\}' chapters/theory/higher_genus_modular_koszul.tex appendices/ordered_associative_chiral_kd.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:2343:\label{thm:heisenberg-formality}
chapters/theory/ordered_associative_chiral_kd.tex:6706:\label{thm:lattice-symmetric-ordered-bar}
chapters/theory/ordered_associative_chiral_kd.tex:6832:\label{thm:lattice-ordered-koszul-dual}
appendices/ordered_associative_chiral_kd.tex:2290:\label{thm:heisenberg-formality}
appendices/ordered_associative_chiral_kd.tex:2574:\label{thm:lattice-symmetric-ordered-bar}
appendices/ordered_associative_chiral_kd.tex:2700:\label{thm:lattice-ordered-koszul-dual}
chapters/theory/higher_genus_modular_koszul.tex:16192:\label{def:shadow-depth-classification}
chapters/theory/higher_genus_modular_koszul.tex:16499:\label{thm:shadow-archetype-classification}

thinking
**Inspecting shadow archetype theorem**

I'm thinking it's important to take a closer look at the theorem called "shadow-archetype-classification" to understand its actual statement. I want to figure out what's going wrong and how to fix it. By analyzing the details of the theorem, I can hopefully clarify things and address any issues. It's all about getting it right! Let's dive into it and see what I can discover.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16192,16540p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16192	\label{def:shadow-depth-classification}
 16193	\ClaimStatusProvedHere
 16194	\index{shadow depth|textbf}
 16195	\index{shadow depth!classification}
 16196	\index{shadow obstruction tower!depth classification}
 16197	Let $\cA$ be a modular Koszul chiral algebra with
 16198	obstruction classes $o_r(\cA)$ from
 16199	Construction~\ref{constr:obstruction-recursion}.
 16200	Define the \emph{shadow depth}
 16201	$\kappa_d(\cA) := r_{\max}(\cA) =
 16202	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16203	(with the convention $\kappa_d = \infty$ if the tower
 16204	does not terminate).
 16205	The \emph{shadow depth class} of~$\cA$ is determined
 16206	by the vanishing pattern of obstruction classes:
 16207	\begin{center}
 16208	\small
 16209	\renewcommand{\arraystretch}{1.15}
 16210	\begin{tabular}{clll}
 16211	\toprule
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4470,4490p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4470	\end{enumerate}
  4471	In the factorization homology picture, formality means that
  4472	$\int_{\Sigma_g}\cA$ is determined by $\int_{\mathbb{P}^1}\cA$
  4473	and the handle attachments, with no higher coherence obstructions.
  4474	\end{proposition}
  4475	
  4476	\begin{proof}
  4477	(i) $\Rightarrow$ (ii): The spectral sequence arises from the bar
  4478	filtration on $\Omega_g(\Bbar_g(\cA))$. Collapse at~$E_2$ means
  4479	that $E_2 \cong E_\infty \cong H^*(\Omega_g(\Bbar_g(\cA)))$,
  4480	and the filtration on cohomology is split. This splitting produces
  4481	the SDR $(\Omega_g(\Bbar_g(\cA)),\, H^*,\, p,\, \iota,\, h)$
  4482	of Theorem~\ref{thm:bar-cobar-htt}, and the transferred structure
  4483	on $H^*$ has $\tilde{m}_n = 0$ for $n \geq 3$ by the argument of
  4484	Step~3 in that proof (Koszul-line concentration forces vanishing).
  4485	Hence $\Omega_g(\Bbar_g(\cA))$ is formal.
  4486	
  4487	(ii) $\Rightarrow$ (iii): If $\Omega_g(\Bbar_g(\cA))$ is formal,
  4488	the transferred operations $\tilde{m}_n$ are the operations on the
  4489	formal model, which has $\tilde{m}_n = 0$ for $n \geq 3$ by


thinking
**Researching theorem references**

I’m considering whether a particular theory can be cited as a theorem in the body of work. Since the appendix proof uses a specific theorem (`thm:bar-cobar-inversion-qi`), it shouldn't be an issue. I wonder if I need to check for theory references related to appendix theorem labels that may be too strong or mis-scoped. It might be useful to compare these labels systematically, particularly some specific ones I’ve mentioned, which could lead to finding more insights.
thinking
**Evaluating theorem proof details**

I can report both occurrences since the second seems to be part of the theorem proof, indicating higher severity, while the first appears more like exposition, maybe medium severity. The user wants all inconsistencies, so after the first, I should dig deeper. I think listing findings individually would be best, avoiding nested bullets. I need to inspect the actual theorem being proved around line 16573 to assess the severity more accurately. Let’s check lines 16540-16572.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16540,16572p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16540	 for generic~$c$
 16541	 \textup{(}Theorem~\textup{\ref{thm:w-virasoro-quintic-forced}}).
 16542	 The tower is infinite by induction on the all-degree master equation.
 16543	 For multi-generator algebras $\mathcal{W}_N$ ($N \geq 3$),
 16544	 diagonal non-autonomy at degree~$6$ is governed by the
 16545	 propagator variance
 16546	 \textup{(}Proposition~\textup{\ref{prop:propagator-variance}}):
 16547	 it vanishes at isolated curvature-proportionality loci in the
 16548	 central charge.
 16549	\end{enumerate}
 16550	Shadow depth is orthogonal to Koszulness: all archetypes are
 16551	chirally Koszul
 16552	\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
 16553	yet their shadow depths differ
 16554	\textup{(}Figure~\textup{\ref{fig:shadow-archetype-classification})}.
 16555	The shadow depth classifies the
 16556	complexity of $\Theta_\cA$, not whether the bar complex is acyclic.
 16557	
 16558	For lattice vertex algebras, the shadow--spectral correspondence
 16559	\textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})

thinking
**Identifying potential issues**

I'm noticing a potential problem where the proof line cites the affine sl2 theorem for all affine cases, which seems unsupported. Then, there's also a concern regarding item (iv) of the theorem statement. It uses `w-virasoro-quintic-forced`, and I'm wondering if that might be acceptable. There’s also the possibility of using an all-degree master theorem along with the proposition about `propagator-variance`. There's quite a bit to consider here!
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:lattice:curvature-braiding-orthogonal\\}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'lattice:curvature-braiding-orthogonal' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:16460: Thm~\ref{thm:lattice:curvature-braiding-orthogonal} \\

thinking
**Investigating label issues**

I'm noticing a potential problem with missing labels, which could lead to broken references. It might be beneficial to inspect and grep all references to check for any undefined labels. The user is asking about the seam between appendices and chapters or theory. While this isn't the same issue, it's worth noting that line 16460 actually uses an undefined label. However, to better assist the user, I should focus on finding the independent lattice theorem or search for "curvature-braiding."
exec
/bin/zsh -lc "rg -n 'curvature-braiding' chapters/theory appendices | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/ordered_associative_chiral_kd.tex:7233:\label{thm:curvature-braiding-dichotomy}
appendices/ordered_associative_chiral_kd.tex:7382:\label{sec:curvature-braiding-entanglement}
appendices/ordered_associative_chiral_kd.tex:7430:By Theorem~\ref{thm:curvature-braiding-dichotomy}, the
appendices/ordered_associative_chiral_kd.tex:7837:(Theorem~\ref{thm:curvature-braiding-dichotomy}).
chapters/theory/higher_genus_modular_koszul.tex:16460: Thm~\ref{thm:lattice:curvature-braiding-orthogonal} \\
chapters/theory/ordered_associative_chiral_kd.tex:4904:\label{thm:curvature-braiding-dichotomy}
chapters/theory/ordered_associative_chiral_kd.tex:6305:\label{sec:curvature-braiding-entanglement}
chapters/theory/ordered_associative_chiral_kd.tex:6357:By Theorem~\ref{thm:curvature-braiding-dichotomy}, the
chapters/theory/ordered_associative_chiral_kd.tex:10874:(Theorem~\ref{thm:curvature-braiding-dichotomy}).
chapters/theory/introduction.tex:2208: $\kappa(V_\Lambda)=\operatorname{rank}(\Lambda)$; curvature-braiding orthogonality; screening operators \\
chapters/theory/introduction.tex:2379: operators; curvature-braiding orthogonality. Depth class G

thinking
**Evaluating classification theorems**

I'm considering a potential issue with undefined labels, although it might not be seam-related. For the lattice in the classification proof, maybe I could cite the ordered associative theorem or the Heisenberg formalism. The classification theorem item about Gaussian/lattice might not need bar complex strict coassociativity since all higher shadows vanish for Gaussian. I think it's worth inspecting whether the lattice theorem states that the bar differential has only deconcatenation. Let's dive into that!
exec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '2568,2592p;6688,6714p;6824,6842p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2568	\begin{proposition}[Gauss decomposition]
  2569	\ClaimStatusProvedHere
  2570	\label{prop:gauss-decomposition-sl2}
  2571	The transfer matrix $T(u) = \bigl(\begin{smallmatrix}
  2572	A(u) & B(u) \\ C(u) & D(u) \end{smallmatrix}\bigr)$
  2573	factors uniquely as
  2574	\[
  2575	T(u) \;=\;
  2576	\underbrace{\begin{pmatrix} 1 & 0 \\ F(u) & 1 \end{pmatrix}}_{F(u)}
  2577	\;\cdot\;
  2578	\underbrace{\begin{pmatrix} k_1(u) & 0 \\ 0 & k_2(u) \end{pmatrix}}_{K(u)}
  2579	\;\cdot\;
  2580	\underbrace{\begin{pmatrix} 1 & E(u) \\ 0 & 1 \end{pmatrix}}_{E(u)},
  2581	\]
  2582	with
  2583	$A(u) = k_1(u) + F(u)\,k_2(u)\,E(u)$,
  2584	$B(u) = k_1(u)\,E(u)$,
  2585	$C(u) = F(u)\,k_2(u)$,
  2586	$D(u) = k_2(u)(1 + F(u)\,E(u))$.
  2587	The Drinfeld Cartan current is the ratio

thinking
**Considering theorem clarity**

I'm thinking this isn't entirely about formality. It seems that I could address `thm:heisenberg-formality` specifically for Heisenberg. Perhaps I could simplify the proof by removing the lattice from the citation and referencing the lattice results separately later. However, item (i) of the theorem statement does include lattice considerations. I should look into whether there's a `shadow-spectral-correspondence` or a lattice-specific theorem in higher genus modular Koszul. I'll have to search for labels related to `shadow-spectral-correspondence`.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:shadow-spectral-correspondence\\}|\\\\label\\{thm:betagamma-global-depth\\}|\\\\label\\{rem:contact-stratum-separation\\}|\\\\label\\{thm:w-virasoro-quintic-forced\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
18764:\label{rem:contact-stratum-separation}

thinking
**Considering lattice theory connections**

I'm thinking about the concept of `shadow-spectral-correspondence` and whether it truly applies to connections rather than just theory. I’m not sure it's necessary to include that. Perhaps it would be better to cite a theorem related to ordered associative structures if it fits. What I really need is to identify the specific theorem that proves lattice Gaussianity in a theoretical context. It might be worthwhile to search for terms like `lattice` and `formality`.
exec
/bin/zsh -lc "rg -n 'lattice.*(Gaussian|formality|all higher|m_k = 0|Theta_.*=H|shadow depth.*2|class.*G)' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex | head -n 50" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:


thinking
**Evaluating theorem adjustments**

I’m considering whether to change the theorem statement about chirally Koszul algebras to exclude lattice and free fermion elements. However, doing so might weaken the theorem significantly. The user wants an audit, so maybe smaller claims from AGENTS would be better. If I narrow the theorem item (i) to just "Heisenberg," that could work, but I need to check if the proof later includes lattice references. I should look beyond line 16558 to see what’s included.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16572,16640p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
 16572	
 16573	\begin{proof}
 16574	Each case follows from the established vanishing theorems:
 16575	
 16576	(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
 16577	coassociative ($m_k = 0$ for $k \geq 3$ in the transferred
 16578	$A_\infty$-structure), so all obstruction sources vanish
 16579	(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).
 16580	
 16581	(ii)~For affine algebras, the cubic shadow is the Lie bracket
 16582	transported through the bar complex
 16583	(Theorem~\ref{thm:nms-affine-cubic-normal-form}). The quartic
 16584	obstruction $o_4 = \tfrac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$
 16585	vanishes by the Jacobi identity: the cyclic double Lie bracket
 16586	$\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 16587	
 16588	(iii)~For $\beta\gamma$, the weight-changing line alone is not the
 16589	class-$\mathbf{C}$ witness: its shadow tower vanishes and
 16590	$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 16591	\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.

thinking
**Fixing theorem citations**

I think I need to adjust the citations by separating them. For Heisenberg, I can use `thm:nms-heisenberg-exact-linearity`, and then for the lattice, I should use the correct theorem `thm:lattice-symmetric-ordered-bar`, or I could introduce a new local proposition instead. This will help clarify things and ensure the citations are accurate. It's important to have everything correctly referenced!
exec
/bin/zsh -lc "rg -n 'curvature-braiding orthogonality|orthogonal|lattice.*Gaussian|lattice.*quadratic|V_\\\\Lambda.*rank' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex chapters/theory/introduction.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:7655:The orthogonal and symplectic $R$-matrices for $B_2$ and
chapters/theory/introduction.tex:123:at all degrees. Genus~$g \geq 1$ corrections form a separate layer; the genus and degree directions are orthogonal
chapters/theory/introduction.tex:124:(Remark~\ref{rem:two-orthogonal-axes}).
chapters/theory/introduction.tex:2025: quotient whose dual is an orthogonal coideal. For the Yangian MC3
chapters/theory/introduction.tex:2050:The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).
chapters/theory/introduction.tex:2208: $\kappa(V_\Lambda)=\operatorname{rank}(\Lambda)$; curvature-braiding orthogonality; screening operators \\
chapters/theory/introduction.tex:2378: $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda)$; screening
chapters/theory/introduction.tex:2379: operators; curvature-braiding orthogonality. Depth class G
chapters/theory/ordered_associative_chiral_kd.tex:7502:The orthogonal and symplectic $R$-matrices for $B_2$ and
chapters/theory/ordered_associative_chiral_kd.tex:8679:orthogonal to the bar-cobar adjunction above: rather than
chapters/theory/higher_genus_modular_koszul.tex:191:\mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))$ occupies the orthogonal
chapters/theory/higher_genus_modular_koszul.tex:4557:$V_\Lambda$ \emph{(lattice, rank~$d$)} &
chapters/theory/higher_genus_modular_koszul.tex:4958:remains orthogonal to that chain.
chapters/theory/higher_genus_modular_koszul.tex:16460: Thm~\ref{thm:lattice:curvature-braiding-orthogonal} \\
chapters/theory/higher_genus_modular_koszul.tex:16550:Shadow depth is orthogonal to Koszulness: all archetypes are
chapters/theory/higher_genus_modular_koszul.tex:18635:$V_\Lambda$ & $\operatorname{rank}(\Lambda)$ & $0$ & $0$ & $0$
chapters/theory/higher_genus_modular_koszul.tex:22017:(factorization structure, metric orthogonality, ghost-number
chapters/theory/higher_genus_modular_koszul.tex:24809:\begin{remark}[Two orthogonal axes of the modular MC problem]
chapters/theory/higher_genus_modular_koszul.tex:24810:\label{rem:two-orthogonal-axes}
chapters/theory/higher_genus_modular_koszul.tex:24839:These axes are \emph{orthogonal}.


thinking
**Addressing theorem clarity**

Okay, I’m tackling the labeling issue in this theorem. The potential fix involves clarifying the scope of `higher_genus_modular_koszul:16581-16583`, which cites a theorem related to affine algebras. I think I can suggest changing “For affine algebras” to specify “For the strict current-level sector of \widehat{\mathfrak{sl}}_2.” Since the proof consistency matters, I want to include both occurrences for completeness despite some repetition. It's tricky but doable!
thinking
**Identifying citation issues**

I’ve spotted potential problems with several citations. For `higher_genus_complementarity:5781-5782`, there's a holographic restatement that goes beyond the theorem's scope by discussing Virasoro/WN infinite terms. I should suggest citing `thm:shadow-archetype-classification` or `thm:nms-finite-termination` instead. 

Similarly, `chiral_koszul_pairs:2960-2962` and `3078-3080` have classification miscitation issues too. I'm noticing these patterns consistently, so I'll need to analyze the other references like `higher_genus_modular_koszul:17872-17876` for possible boundary distinctions. The specifics matter!
exec
/bin/zsh -lc "rg -n 'thm:nms-archetype-trichotomy|thm:nms-affine-cubic-normal-form|thm:nms-heisenberg-exact-linearity|thm:nms-clutching-law-modular-resonance|thm:sl2-koszul-dual|app:curved-ainfty-formulas|def:bar-complex-algebraic|thm:essential-image-koszul' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:12609:(Theorem~\ref{thm:nms-affine-cubic-normal-form}): the only ternary
chapters/theory/higher_genus_modular_koszul.tex:16579:(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).
chapters/theory/higher_genus_modular_koszul.tex:16583:(Theorem~\ref{thm:nms-affine-cubic-normal-form}). The quartic
chapters/theory/higher_genus_modular_koszul.tex:17872:(Theorem~\ref{thm:nms-clutching-law-modular-resonance})
chapters/theory/higher_genus_modular_koszul.tex:17944:(Theorem~\ref{thm:nms-clutching-law-modular-resonance}),
chapters/theory/higher_genus_modular_koszul.tex:30638:$($Theorem~\textup{\ref{thm:nms-clutching-law-modular-resonance}}$)$
chapters/theory/higher_genus_modular_koszul.tex:31343:(Theorem~\ref{thm:nms-archetype-trichotomy}):
chapters/theory/higher_genus_modular_koszul.tex:31575:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/bar_cobar_adjunction_inversion.tex:3275:(Theorem~\ref{thm:essential-image-koszul}):
chapters/theory/chiral_koszul_pairs.tex:2961:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/chiral_koszul_pairs.tex:3080:(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
chapters/theory/higher_genus_foundations.tex:1123:An $A_\infty$ algebra consists of a graded vector space $A$ with operations $m_k: A^{\otimes k} \to A[2-k]$ for $k \geq 1$ satisfying (cf.\ Appendix~\ref{app:curved-ainfty-formulas}):
chapters/theory/higher_genus_foundations.tex:7302:(Theorem~\ref{thm:nms-clutching-law-modular-resonance}).
chapters/theory/chiral_modules.tex:2874:(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
chapters/theory/chiral_modules.tex:2946:(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
chapters/theory/chiral_modules.tex:2967:Theorem~\ref{thm:sl2-koszul-dual},
chapters/theory/higher_genus_complementarity.tex:5126:(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
chapters/theory/higher_genus_complementarity.tex:5782:(Theorem~\ref{thm:nms-archetype-trichotomy}).
chapters/theory/algebraic_foundations.tex:116:The bar construction (Definition~\ref{def:bar-complex-algebraic})

thinking
**Inspecting modular structures**

I need to take a closer look at `higher_genus_modular_koszul` with respect to items 31343 and 31575. I wonder if the archetype theorem has been misused in this context, so it seems like a thorough investigation is warranted. It feels like digging into these elements may reveal some important insights about their properties. I’ll proceed by examining whether these modular structures align with the principles of the theorem.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31336,31352p;31568,31582p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 31336	-\Delta(\Theta^{(1)}) - d_{\mathrm{sew}}^{(2)}$
 31337	is nonzero iff $\Theta^{(1)}$ has nontrivial
 31338	separating-node data, which occurs iff the cubic
 31339	shadow $\mathfrak{C}(\cA) \neq 0$, i.e.,
 31340	$\ell_3^{(0),\mathrm{tr}}|_{H^*} \neq 0$
 31341	(Proposition~\ref{prop:shadow-formality-low-degree}(ii)).
 31342	By the archetype classification
 31343	(Theorem~\ref{thm:nms-archetype-trichotomy}):
 31344	$\mathfrak{C} = 0$ for classes $G$ and $C$ (Heisenberg
 31345	and $\beta\gamma$); $\mathfrak{C} \neq 0$ for classes
 31346	$L$ and $M$ (affine and Virasoro).
 31347	
 31348	The planted-forest shell
 31349	$\Theta^{(2)}_{\mathrm{pf}} = -d_{\mathrm{pf}}^{(2)}$
 31350	depends on all shadow data through the genus-$2$
 31351	planted-forest graph sum. The scalar trace is
 31352	$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$
 31568	genus-$3$ data; $d_2\colon E_1^{0,*} \to E_1^{2,*}$ encodes
 31569	$\operatorname{Ob}_2$; $d_3\colon E_1^{0,*} \to E_1^{3,*}$
 31570	encodes the deepest obstruction at genus~$3$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31580,31606p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31580	\text{class}
 31581	& r_{\max}
 31582	& \text{vertex constraint}
 31583	& \text{active/scalar} \\\hline
 31584	G\;\text{(Gaussian)}
 31585	 & 2 & \text{all vertices binary}
 31586	 & 42/42\text{ scalar (}\kappa\text{-only)} \\
 31587	L\;\text{(Lie/tree)}
 31588	 & 3 & \operatorname{val}(v) \geq 3\text{ activates cubic}
 31589	 & \text{cubic corrections at graphs with 3-valent vertices} \\
 31590	C\;\text{(contact)}
 31591	 & 4 & \operatorname{val}(v) \geq 4\text{ activates quartic}
 31592	 & \text{quartic at 4-valent vertices; cubic absent} \\
 31593	M\;\text{(mixed)}
 31594	 & \infty & \text{all degrees active}
 31595	 & \text{all 42 graphs carry higher-degree corrections}
 31596	\end{array}
 31597	\]
 31598	For class~$G$ (Heisenberg), every graph contributes
 31599	$\kappa^{|E|}/|\operatorname{Aut}|$ and the sum recovers
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '7290,7310p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7290	$K^{\mathrm{log}}$ is designed to make them interact
  7291	functorially. Together with the genus-universality theorem
  7292	(Theorem~\ref{thm:genus-universality}) and the stable-graph bar
  7293	differential (Lemma~\ref{lem:stable-graph-d-squared}), the
  7294	logarithmic clutching kernels would provide the geometric
  7295	foundation for the modular completion of the bar complex.
  7296	Note that Theorem~\ref{thm:planted-forest-tropicalization}
  7297	identifies the planted-forest coefficient algebra
  7298	$\mathbb{G}_{\mathrm{pf}}$ with the chain algebra on
  7299	$\operatorname{Trop}(\FM_n(C|D))$; the degeneration formula
  7300	\cite[Theorem~5.3.4]{Mok25} is the geometric incarnation of
  7301	the clutching law for the quartic resonance class
  7302	(Theorem~\ref{thm:nms-clutching-law-modular-resonance}).
  7303	\end{remark}
  7304	
  7305	\begin{construction}[Log FM forgetful chain map; \ClaimStatusProvedElsewhere]
  7306	\label{constr:log-fm-chain-map}
  7307	\index{logarithmic FM!forgetful chain map}
  7308	The logarithmic Fulton--MacPherson space
  7309	$\operatorname{FM}_n(X \mathbin{|} D)$ of
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30630,30644p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30630	\index{degeneration formula!as clutching law}%
 30631	Mok's degeneration formula \cite[Theorem~5.3.4]{Mok25} states that
 30632	each irreducible component of the special fibre of
 30633	$\operatorname{FM}_n(W/B) \to B$ is a proper birational modification
 30634	of a product
 30635	$\prod_{v \in V(S_{\rho,1})} \operatorname{FM}_{I_v}(Y_v|D_v)$.
 30636	This is the geometric incarnation of our clutching law for the
 30637	quartic resonance class
 30638	$($Theorem~\textup{\ref{thm:nms-clutching-law-modular-resonance}}$)$
 30639	and the non-separating clutching law
 30640	$($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 30641	the algebraic clutching identities ARE the degeneration formula
 30642	applied to the bar complex on log-FM spaces.
 30643	
 30644	More explicitly: in the finite-order shadow obstruction tower, the extension
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2956,2964p;3074,3082p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2956	(Theorem~\ref{thm:kac-shapovalov-koszulness});
  2957	Cartan~$H^2$ = abelian Cartan subalgebra classes
  2958	surviving in $H^2(\barB)$
  2959	(Remark~\ref{rem:admissible-koszul-status}).
  2960	\textit{Shadow}: archetype class $G$/$L$/$C$/$M$
  2961	(Theorem~\ref{thm:nms-archetype-trichotomy})
  2962	and shadow depth $r_{\max}$;
  2963	all four classes contain Koszul algebras
  2964	(shadow depth $\neq$ Koszulness).
  3074	\end{tabular}
  3075	\end{center}
  3076	All five are chirally Koszul (genus-$0$ slice is formal), yet the
  3077	Virasoro algebra has infinite shadow depth
  3078	($\mathfrak{o}^{(5)}_{\mathrm{Vir}} \neq 0$
  3079	at genus~$\geq 1$). The archetype classification
  3080	(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
  3081	Koszul locus by the all-genera termination behavior of
  3082	$\Theta_\cA$, a transverse invariant invisible to genus~$0$.


thinking
**Analyzing theorem proof**

I need to check the proof details for theorem `thm:nms-heisenberg-exact-linearity`, specifically lines 969-970. It mentions that "no higher operations `m_n` with n>=3 appear," which is interesting because the theorem only claims validity up to quartic order. Line 970 states that higher operations vanish, but the theorem citation should stick to its original statement. While the proof is stronger, leaning on it for support may be precarious, as grounding rules caution against treating inferences as facts.
thinking
**Evaluating proof assumptions**

I can't just assume that the first sentence of the proof rigorously proves that all higher operations vanish. However, upon reading the proof, it does claim that clearly. So, I'm wondering how the status of the theorem plays into this situation. Does the theorem's standing provide additional support for these claims? It feels important to clarify this distinction before drawing any conclusions, as I want to ensure I'm accurately interpreting the proof and its implications.
exec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '2338,2352p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2338	same modular characteristic $\kappa = -k$ but differ as algebras).
  2339	\end{proof}
  2340	
  2341	\begin{theorem}[Formality: class~G, shadow depth~$2$;
  2342	\ClaimStatusProvedHere]
  2343	\label{thm:heisenberg-formality}
  2344	The Heisenberg ordered bar complex is formal:
  2345	the $\Ainf$-structure on $H^\bullet(\Barch(\cH_k))$
  2346	has $m_k = 0$ for all $k\ge 3$. The Heisenberg
  2347	belongs to class~G \textup{(}shadow depth $r_{\max} = 2$,
  2348	the minimum for a nontrivial chiral algebra\textup{)}.
  2349	\end{theorem}
  2350	
  2351	\begin{proof}
  2352	Since $d_{\Barch} = 0$, the bar complex \emph{is} its own

thinking
**Clarifying theorem citations**

I think I need to fix the citation for Heisenberg to refer to `thm:heisenberg-formality` instead of the appendix theorem. For lattices, I’m considering if there might be a lattice theorem that applies. Maybe I should search for something related to `class G` about lattices. There seems to be several directions to explore, and I'm curious about how this all connects! Let's see what I find out.
exec
/bin/zsh -lc "rg -n 'lattice.*class~G|lattice.*shadow depth~\\"'$2'"\\"'$|lattice.*m_k = 0|lattice.*formal'"' chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/higher_genus_modular_koszul.tex appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n 'V_\\\\Lambda|lattice vertex algebra|shadow depth.*2|class.*G' chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/higher_genus_modular_koszul.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:2341:\begin{theorem}[Formality: class~G, shadow depth~$2$;
chapters/theory/ordered_associative_chiral_kd.tex:2347:belongs to class~G \textup{(}shadow depth $r_{\max} = 2$,
chapters/theory/ordered_associative_chiral_kd.tex:2359:simple pole, which falls in class~G.
chapters/theory/ordered_associative_chiral_kd.tex:2432:In summary: the Heisenberg is class~G (shadow depth~$2$, formal,
chapters/theory/ordered_associative_chiral_kd.tex:6405:Lattice $V_\Lambda$ (abelian) & $0$ & Decoupled &
chapters/theory/ordered_associative_chiral_kd.tex:6597:double pole with scalar residue (class~G) vs.\ simple pole
chapters/theory/ordered_associative_chiral_kd.tex:6691:The lattice vertex algebra $\Vlat_\Lambda^\varepsilon$ has vertex operators
chapters/theory/ordered_associative_chiral_kd.tex:6838: $(\Vlat_\Lambda^\varepsilon)^!$ is again a lattice vertex algebra
chapters/theory/ordered_associative_chiral_kd.tex:7594:$V_\Lambda$ \textup{(even)}
chapters/theory/ordered_associative_chiral_kd.tex:7669:is equivalent. Similarly, $V_\Lambda^!$ and $V_{\Lambda^*}$ share
chapters/theory/ordered_associative_chiral_kd.tex:7712:For abelian algebras ($\mathcal{H}_k$, $V_\Lambda$):
chapters/theory/ordered_associative_chiral_kd.tex:8227:For the Heisenberg algebra $\cH_k$ (class $G$), all three
chapters/theory/ordered_associative_chiral_kd.tex:8261:  $r(z) = \Psi/z$ \textup{(}class~$G$, level prefix
chapters/theory/ordered_associative_chiral_kd.tex:8438:$r(z) = \Psi/z$ (class~$G$, level prefix $\Psi$).
chapters/theory/ordered_associative_chiral_kd.tex:8632:  confirming class~$G$).
chapters/theory/ordered_associative_chiral_kd.tex:9287:  recovering the class-$G$ case of
chapters/theory/ordered_associative_chiral_kd.tex:9876:  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
chapters/theory/ordered_associative_chiral_kd.tex:10019:On the Koszul locus \textup{(}classes~$\mathsf{G}$, $\mathsf{L}$,
chapters/theory/ordered_associative_chiral_kd.tex:10776:\item Formality of $\Barch(\cH_k)$: class~G, shadow depth~$2$,
chapters/theory/higher_genus_modular_koszul.tex:136: (class~$\mathsf{G}$, Gaussian).




thinking
**Analyzing citation fixes**

I’m searching lines around 22027 to possibly mention class G factorization with Heisenberg and lattice aspects. It seems I don't need the exact theorem label since the user just requested a correction to cite `thm:heisenberg-formality` correctly. The user noted an exact fix might be to "Delete `and lattice VOAs`." That sounds acceptable since they didn't ask for the theorem statement to be maintained. I’ll need to clarify that any further theorem statements must also be narrowed down if no lattice proof is added.
thinking
**Identifying theorem issues**

I’m noticing potential issues with `thm:nms-affine-cubic-normal-form` as it only applies to the strict current-level sector of `\widehat{\mathfrak{sl}}_2`, so I need to adjust occurrences to reflect this restriction or cite a general affine theorem. 

For `thm:nms-archetype-trichotomy`, it pertains specifically to "three primitive nonlinear archetypes." I should replace the citation with `Theorem\ref{thm:shadow-archetype-classification}`, and include deeper Virasoro conditions if necessary. Lastly, I’ll verify the conilpotency condition in `bar_cobar_adjunction_inversion` and refine wording in `higher_genus_foundations`.
thinking
**Analyzing potential issues**

I could list all five occurrences separately, but that might be excessive. There are about ten findings to consider. One concern is `higher_genus_modular_koszul:17872`, which could be rated High since it may overstate the theorem's scope. I should verify if line 17860 mentions the separating boundary because the issue is with the phrase "every boundary stratum." Then, there's `higher_genus_foundations:1123`, possibly Medium. Finally, for `chiral_modules`, I may need to cite only the strongest occurrence, 2946.
thinking
**Investigating theorem references**

I need to check if the "appendices/koszul_reference.tex" imported theorem is solely a reference version of the core theorem and not independent. The theory uses it in a remark, but it doesn't seem too severe. I suppose I could look into compile warnings, although it might not be necessary. Perhaps I should also consider updating the plan. Now that I have some context, I might need to update the statuses accordingly.
codex
I’ve moved from mapping to verified mismatches. The pattern is consistent: several theory chapters cite appendix results at a stronger scope than the appendix actually proves, and one foundational theory definition points backward into the glossary appendix.
Plan update
Cross-reference mapping is complete. I’m now in verification mode: checking each surviving mismatch against the exact theorem/definition text to eliminate false positives and pin down a concrete local fix.
  ✓ Map appendix-defined labels referenced by theory and theory-defined labels referenced by appendices
  ✓ Read each seam location in context and test citation correctness, scope, and dependency direction
  → Hunt second-order seam issues: circularity, notation drift, duplicate theorem surfaces, inconsistent imported hypotheses
  • Re-verify surviving findings and deliver exact file:line fixes

thinking
**Reviewing theorem applications**

I need to inspect the `higher_genus_modular_koszul` at lines 12609 and 16581 in relation to the `m_3` language. The appendix theorem uses `\mathfrak C`, which might be a cyclic shadow of `m_3`, but that’s not entirely clear since the statement doesn't match up. There's also a potential issue with the mention of "every boundary stratum" at line 17872, as the theorem only deals with separating aspects. I should search for the actual label in the appendix.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:nms-nonseparating-clutching-law\\}' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2295:\label{thm:nms-nonseparating-clutching-law}

thinking
**Considering classification adjustments**

I see that the `shadow-archetype-classification` is already an all-genera classification within the main theory, and it covers vir/w_n. So, I think that simply replacing the citation could suffice. As for `higher_genus_complementarity:5782`, it looks like that might be fine too. I want to make sure I'm making the right changes while keeping everything aligned with the established framework!
exec
/bin/zsh -lc "rg -n 'affine-cubic-shadow|generic affine|quartic obstruction.*Jacobi|shadow.*affine.*generic|Lie/tree' chapters/theory/higher_genus_modular_koszul.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
10331: at degree~$3$ (Lie/tree archetype).
11467:$\ell_3^{(0)}\neq0$ with $\ell_4^{(0)}=0$ the Lie/tree class
11648:\textbf{Affine} (Lie/tree)
14578:Heisenberg and generic affine Kac--Moody\textup{)}. In that
16466: \S\ref{sec:affine-cubic-shadow} \\[3pt]
16521: quartic obstruction $o_4 = 0$ by the Jacobi identity.
18760:For affine Kac--Moody $\hat{\fg}_k$: the quartic obstruction $o_4 = \frac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$ vanishes by the Jacobi identity (Theorem~\ref{thm:shadow-archetype-classification}(ii)), giving $S_4 = 0$ and $\Delta = 0$. The shadow metric $Q_L = (2\kappa + 3\alpha t)^2$ is a \emph{perfect square}: $\sqrt{Q_L}$ is polynomial and the tower terminates at $r_{\max} = 3$. The shadow connection is trivial ($\omega = Q'/(2Q) = 3\alpha/(2\kappa+3\alpha t)$, regular everywhere), consistent with the finite depth.
29978: $\mathsf{L}$ (Lie/tree) & $3$
30014:(\S\ref{sec:affine-cubic-shadow});
31587:L\;\text{(Lie/tree)}

thinking
**Searching for theorems**

I’m looking into the section on `sec:affine-cubic-shadow`. I wonder if there’s a relevant general theorem in the main content rather than just the appendix. I should inspect the details in and around the numbers 11640 or 14578 to see if there’s something that could help clarify my understanding. It seems like a good place to start digging!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11640,11680p;14568,14592p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 11640	\renewcommand{\arraystretch}{1.3}
 11641	\begin{tabular}{lccc}
 11642	& $\Theta^{(2)}_{\mathrm{loop}^2}$
 11643	& $\Theta^{(2)}_{\mathrm{sep} \circ \mathrm{loop}}$
 11644	& $\Theta^{(2)}_{\mathrm{pf}}$ \\
 11645	\hline
 11646	\textbf{Heisenberg} (Gaussian)
 11647	 & $\checkmark$ & --- & --- \\
 11648	\textbf{Affine} (Lie/tree)
 11649	 & $\checkmark$ & $\checkmark$ & --- \\
 11650	\textbf{Virasoro}/\textbf{$\mathcal{W}_N$} (Mixed)
 11651	 & $\checkmark$ & $\checkmark$ & $\checkmark$ \\
 11652	\end{tabular}
 11653	\end{center}
 11654	Heisenberg sees only iterated BV\@. Affine algebras acquire
 11655	the separating/loop interaction. Virasoro/$\mathcal{W}_N$
 11656	exhibit all three shells.
 11657	\end{construction}
 11658	
 11659	\begin{remark}[Modular Chern--Weil theory]
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:affine-cubic-shadow\\}|affine cubic shadow|Lie/tree class' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
11467:$\ell_3^{(0)}\neq0$ with $\ell_4^{(0)}=0$ the Lie/tree class


thinking
**Making a clarification**

I need to fix the phrase by changing "every boundary stratum" to "every separating boundary stratum." If I'm intending to include non-separating strata as well, it’s important to reference "Theorem\ref{thm:nms-nonseparating-clutching-law}" next to that. This adjustment will help ensure clarity and comprehensiveness in the explanation. It's essential not to overlook these nuances when discussing such intricate topics!
thinking
**Reflecting on theories**

I'm thinking about the circular appendix and how it relates to theory dependency. It seems like it doesn't really provide a concrete classical bar formula for what I'm exploring on this surface. There’s a sense of frustration here since I'm looking for clear explanations and definitions. I just want to understand how these concepts connect better, and I wonder if there's a more straightforward way to address this matter.
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16576 — PROBLEM: the proof of `thm:shadow-archetype-classification` cites `thm:nms-heisenberg-exact-linearity` for “Heisenberg and lattice VOAs” and for `m_k=0` for all `k\ge3`, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:953-966` is only the Heisenberg line and only states `\Theta_{\mathcal H}^{\le4}=H_{\mathcal H}` through quartic order. It does not cover lattices. FIX: replace this step with `For Heisenberg, Theorem~\ref{thm:heisenberg-formality} gives \(m_k=0\) for all \(k\ge3\).` Delete `and lattice VOAs` here; add a separate lattice-specific citation before retaining lattices in item `(i)` of `thm:shadow-archetype-classification`.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16581 — PROBLEM: the same proof upgrades `thm:nms-affine-cubic-normal-form` to all affine algebras, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1037-1050` is only for the strict current-level sector of `\widehat{\mathfrak{sl}}_{2,k}`. The same scope leak already appears expositionally at `chapters/theory/higher_genus_modular_koszul.tex:12609`. FIX: replace `For affine algebras` with `For the strict current-level sector of \widehat{\mathfrak{sl}}_{2,k}` at both locations, or supply a genuinely general affine theorem before keeping the broader quantifier in `thm:shadow-archetype-classification(ii)`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:31342 — PROBLEM: this cites `thm:nms-archetype-trichotomy` as a full `G/L/C/M` all-genera classification, but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1207-1226` only treats three primitive families through quartic order. The same miscitation recurs at `chapters/theory/higher_genus_modular_koszul.tex:31574`, `chapters/theory/chiral_koszul_pairs.tex:2960`, `chapters/theory/chiral_koszul_pairs.tex:3079`, and `chapters/theory/higher_genus_complementarity.tex:5781`. FIX: replace each of those citations with `Theorem~\ref{thm:shadow-archetype-classification}`; when infinite Virasoro/`\mathcal W_N` behavior is used explicitly, add `Theorem~\ref{thm:nms-finite-termination}` or `Theorem~\ref{thm:nms-virasoro-quintic-forced}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:17872 — PROBLEM: the body says `thm:nms-clutching-law-modular-resonance` gives the quartic factorization constraint “at every boundary stratum,” but the cited appendix theorem in `appendices/nonlinear_modular_shadows.tex:1822-1835` is only a separating clutching law. FIX: change `every boundary stratum` to `every separating boundary stratum`; if non-separating strata are intended too, cite `Theorem~\ref{thm:nms-nonseparating-clutching-law}` alongside it.

- [HIGH] chapters/theory/chiral_modules.tex:2945 — PROBLEM: the level involution `k\mapsto -k-4` is attributed to `thm:sl2-koszul-dual`, but the cited theorem in `appendices/_sl2_yangian_insert.tex:531-553` only identifies the open-colour dual with `Y_\hbar(\mathfrak{sl}_2)` and `\hbar=1/(k+2)`. The closed-colour affine level shift appears only in `appendices/_sl2_yangian_insert.tex:596-602` as `rem:closed-vs-open-sl2`. The same wrong theorem citation is repeated at `chapters/theory/chiral_modules.tex:2967`. FIX: change those citations to `Remark~\ref{rem:closed-vs-open-sl2}` for the closed-colour shift; keep `Theorem~\ref{thm:sl2-koszul-dual}` only for the Yangian/open-colour identification.

- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:3275 — PROBLEM: the checklist says conilpotent means `\bigcap_n \mathrm{coker}(\Delta^n)=0`, but the cited appendix theorem in `appendices/koszul_reference.tex:268-286` uses the standard criterion `\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar\Delta^{(n)})`. The body is not citing the appendix correctly. FIX: replace the parenthetical at line 3277 with `every element of \(\ker(\epsilon)\) is killed by some iterated reduced coproduct, i.e. \(\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar\Delta^{(n)})\)`.

- [HIGH] chapters/theory/algebraic_foundations.tex:116 — PROBLEM: the foundational chapter points to `Definition~\ref{def:bar-complex-algebraic}`, but the target in `appendices/notation_index.tex:342-344` is only a glossary stub pointing forward to `Theorem~\ref{thm:bar-coalgebra}`. That reverses the dependency direction and leaves the classical bar construction undefined on the theory surface. FIX: replace the sentence with a local definition, e.g. `The bar construction is \(\barB(A)=T^c(s^{-1}\bar A)\)` with deconcatenation coproduct; cite `Theorem~\ref{thm:bar-coalgebra}` only for the later chiral dg-coalgebra model, not as the source definition.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:1123 — PROBLEM: the body defines an uncurved `A_\infty` algebra with `k\ge1` but cites `Appendix~\ref{app:curved-ainfty-formulas}`, whose heading and displayed formulas in `appendices/general_relations.tex:97-107` are for the curved theory with `m_0=\mu_0`. The notation seam is off by exactly the curvature term. FIX: rename the body definition to `uncurved \(A_\infty\) algebra` and change the citation sentence to `This is the specialization \(\mu_0=0\) of the curved formulas in Appendix~\ref{app:curved-ainfty-formulas}.`

## Summary
Checked: 17 | Findings: 8 | Verdict: FAIL
tokens used
437,628
