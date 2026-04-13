# S15_appendices_to_body (1125s)

- [CRITICAL] `main.tex:1660` — PROBLEM: `\phantomsection\label{app:coderived-models}` is only a synthetic “planned appendix” anchor, while the actual live material is `chapters/theory/coderived_models.tex:188` (`\label{sec:coderived-models}`) and the archive chapter itself is mislabeled `\label{app:coderived}` at `chapters/theory/coderived_models.tex:3`. Core theory points to that fake appendix target at `chapters/theory/higher_genus_foundations.tex:293,407,832`. FIX: rename `chapters/theory/coderived_models.tex:3` to `\label{chap:coderived-models}`, change its prose at line 12 from “This appendix” to “This chapter,” keep `\label{sec:coderived-models}` at line 188, replace those body references with `Chapter~\ref{chap:coderived-models}, \S\ref{sec:coderived-models}` (or just `\S\ref{sec:coderived-models}` where only the subsection is meant), and delete `main.tex:1643` `\label{app:coderived}` plus `main.tex:1660` `\label{app:coderived-models}`.

- [HIGH] `chapters/theory/nilpotent_completion.tex:4` — PROBLEM: this archive-only frontier chapter is included before `\appendix` (`main.tex:1559`) but still carries the appendix label `app:nilpotent-completion` and appendix prose at `chapters/theory/nilpotent_completion.tex:8,19,1277`; annals mode then fakes the same appendix label at `main.tex:1642`, while core theory cites it as `Appendix` at `chapters/theory/bar_cobar_adjunction_inversion.tex:70`, `bar_cobar_adjunction_curved.tex:1514,5980`, `introduction.tex:2624`, `algebraic_foundations.tex:2436,2499`, `poincare_duality.tex:682`, `filtered_curved.tex:131`, `chiral_koszul_pairs.tex:4859,4865,5422`. FIX: rename the live label to `chap:nilpotent-completion`, change “This appendix”/“present appendix” to “This chapter”/“present frontier chapter,” replace every `Appendix~\ref{app:nilpotent-completion}` with `Chapter~\ref{chap:nilpotent-completion}` in archive-visible text, remove `main.tex:1642`, and rewrite annals-visible mentions as plain archive-only notes instead of fake appendix references.

- [HIGH] `chapters/theory/algebraic_foundations.tex:116` — PROBLEM: the definition of a quadratic algebra sends the reader to `Definition~\ref{def:bar-complex-algebraic}`, but that label lives in the notation appendix at `appendices/notation_index.tex:342`, where the “definition” is only a back-pointer to `Theorem~\ref{thm:bar-coalgebra}`. This is source-to-index-to-source circularity on a core definition seam. FIX: replace the sentence with a real forward statement, e.g. `The bar construction is built from~\bar A via \(B(A)=T^c(s^{-1}\bar A)\); see Theorem~\ref{thm:bar-coalgebra}.` Do not cite `def:bar-complex-algebraic` from core theory.

- [HIGH] `chapters/theory/existence_criteria.tex:474` — PROBLEM: the proved classification table sends the `\mathcal W_{1+\infty}` row to `Appendix~\ref{app:koszul-reference}`, while `appendices/koszul_reference.tex:242` sends the reader straight back to `Appendix~\ref{app:existence-criteria}` for the classification table. That is a circular navigation dependency with no direct criterion at the seam. FIX: in the table row, replace `Filtered; see Appendix~\ref{app:koszul-reference}` with a concrete pointer such as `Filtered; completed dual on the essential-image locus of Theorem~\ref{thm:essential-image-koszul}`; then change `appendices/koszul_reference.tex:242` to cite that same theorem directly instead of bouncing back to the table.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1583` — PROBLEM: this proved theorem cites promoted main-body material as `Appendix~\ref{app:homotopy-transfer}`, even though `appendices/homotopy_transfer.tex` is loaded before `\appendix` at `main.tex:1010`; the citation is also too vague, since the theorem used is `appendices/homotopy_transfer.tex:455` (`thm:chiral-htt`), not the chapter as a whole. The same chapter/appendix drift appears at `chapters/theory/higher_genus_foundations.tex:1104`, `quantum_corrections.tex:360,525`, `chiral_modules.tex:2665`, and `chiral_hochschild_koszul.tex:2901,2933`. FIX: rename `appendices/homotopy_transfer.tex:2` to `\label{chap:homotopy-transfer}`, change `higher_genus_foundations.tex:1583` to `Theorem~\ref{thm:chiral-htt} produces a minimal...`, change `higher_genus_foundations.tex:1104` to `Chapter~\ref{chap:homotopy-transfer}, \S\ref{sec:ainfty-historical}`, and replace the remaining `Appendix~\ref{app:homotopy-transfer}` pointers with `Chapter~\ref{chap:homotopy-transfer}` or the exact theorem labels they use.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:4313` — PROBLEM: the proved corollary writes the quartic projection as `R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)` and cites the whole nonlinear-shadows chapter generically, but the promoted chapter `appendices/nonlinear_modular_shadows.tex` defines the actual object as `\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)` at `appendices/nonlinear_modular_shadows.tex:1733-1742` (`def:nms-modular-quartic-resonance-class`) and is loaded before `\appendix` at `main.tex:1109`. This is both notation drift and an imprecise seam citation. FIX: change the corollary to `\pi_4(\Theta_\cA)=\mathfrak R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)` and replace the generic chapter pointer with `Definition~\ref{def:nms-modular-quartic-resonance-class}`; also rename `appendices/nonlinear_modular_shadows.tex:2` to `\label{chap:nonlinear-modular-shadows}` and update the generic `Appendix~\ref{app:nonlinear-modular-shadows}` references in this chapter (`4848, 10138, 12290, 12329, 13220, 15463, 15477, 29759, 31102`) to `Chapter~\ref{chap:nonlinear-modular-shadows}`.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:5752` — PROBLEM: `branch_line_reductions` is a promoted main-body chapter (`main.tex:1113`) but the body still cites it as `Appendix~\ref{app:branch-line-reductions}` here, again at `chapters/theory/chiral_hochschild_koszul.tex:5784`, and in `chapters/theory/introduction.tex:1954`. FIX: rename `appendices/branch_line_reductions.tex:2` to `\label{chap:branch-line-reductions}` and change those references to `Chapter~\ref{chap:branch-line-reductions}`; where a specific result is intended, replace the chapter-level pointer with the exact theorem label from that chapter.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:1116` — PROBLEM: `Appendix~\ref{app:combinatorial-frontier}` points to an archive-only chapter loaded before `\appendix` in archive mode (`main.tex:1371`) and replaced by a phantom label in annals mode (`main.tex:1873`). The seam therefore misclassifies the object as an appendix and leaves annals-visible text pointing at a placeholder instead of live content. FIX: rename `appendices/combinatorial_frontier.tex:2` to `\label{chap:combinatorial-frontier}`, change archive-mode cross-references such as this one and `chapters/theory/introduction.tex:2251` to chapter refs, and replace annals-visible mentions with plain text like `the archive-only combinatorial frontier chapter`; then delete `main.tex:1873` `\label{app:combinatorial-frontier}`.

## Summary
Checked: 33 | Findings: 8 | Verdict: FAIL


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
session id: 019d87e1-7263-7b82-b5b3-cffa14f48097
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
**Auditing codebase files**

I need to act as a coding agent for the user’s request to audit specific directories, focusing on key files and reviewing transitions carefully. Since the user wants an audit rather than code edits, I'll lean on the deep-beilinson-audit skill. Considering the complexity, it might be helpful to use explorer agents, perhaps one for citations, one for circular dependencies, and another for notation consistency. I must ensure to ground claims directly from the actual file contents I read.
thinking
**Locating surfaces and reading files**

I'm considering using explorers to help locate surfaces and determine the relevant files that need reviewing. An initial commentary update seems essential, along with possibly updating the plan for the substantial work ahead. Since we're conducting a mathematical audit but not editing, reading mandatory documents like CLAUDE, the concordance, theorem registry, and the red_team_summary might still be wise. I'll need to send the user an update on my understanding and the next steps before spawning an explorer to map the seam files.
codex
Auditing the seam between `appendices/` and `chapters/theory/` now. I’m first locating the appendix/theory files that actually reference each other, then I’ll read those transition points line-by-line for citation drift, circularity, and notation mismatches.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files appendices chapters/theory | sed 's#"'^#FILE #'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
FILE appendices/general_relations.tex
FILE appendices/homotopy_transfer.tex
FILE appendices/computational_tables.tex
FILE appendices/branch_line_reductions.tex
FILE appendices/nonlinear_modular_shadows.tex
FILE appendices/_sl2_yangian_insert.tex
FILE appendices/spectral_higher_genus.tex
FILE appendices/dual_methodology.tex
FILE appendices/signs_and_shifts.tex
FILE appendices/arnold_relations.tex
FILE appendices/theta_functions.tex
FILE appendices/combinatorial_frontier.tex
FILE appendices/koszul_reference.tex
FILE appendices/ordered_associative_chiral_kd.tex
FILE appendices/notation_index.tex
FILE chapters/theory/higher_genus_modular_koszul.tex
FILE chapters/theory/quantum_corrections.tex
FILE chapters/theory/fourier_seed.tex
FILE chapters/theory/poincare_duality_quantum.tex
 succeeded in 50ms:
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


thinking
**Gathering resources for review**

I need to check the concordance and the theorem registry first, and it seems like a red team summary based on skill load is likely necessary too. I also want to locate the references between the appendices and chapters or theory. Finding citations might also be important. So, it looks like I'll be gathering cross-references as I go. I should definitely use RG to help with this process!
codex
I’ve loaded the audit protocol and canonical repo constraints. Next I’m mapping the actual seam: every `appendices/` reference from `chapters/theory/`, every back-reference, and any duplicated chapter/appendix pair that could hide circular proof structure.
exec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"appendix|appendices|App\\\\.?|Arnold|signs_and_shifts|notation_index|ordered_associative_chiral_kd|theta_functions|koszul_reference|homotopy_transfer|general_relations|spectral_higher_genus|branch_line_reductions|dual_methodology|nonlinear_modular_shadows|combinatorial_frontier|computational_tables|arnold_relations\" chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{|ref\\{|autoref\\{|nameref\\{\" appendices chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
Total output lines: 646

appendices/general_relations.tex:17:Jacobi identity & Arnold--Orlik--Solomon relations \\
appendices/general_relations.tex:67:\chapter{\texorpdfstring{Arnold relations for small $n$}{Arnold relations for small n}}
appendices/general_relations.tex:70:Arnold relations for logarithmic forms:
appendices/general_relations.tex:77:\emph{$n = 4$ (four 3-term Arnold relations, one for each triple $\{i,j,k\} \subset \{1,2,3,4\}$).}
appendices/general_relations.tex:84:These four relations (each involving forms that share an index) reduce $\binom{6}{2} = 15$ naive products to $\dim H^2(C_4(\mathbb{C})) = 11$ independent classes. Products of disjoint pairs such as $\eta_{12} \wedge \eta_{34}$ are \emph{not} constrained by Arnold relations and remain independent.
appendices/general_relations.tex:87:These are the ten three-term Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$, one for each triple $\{i,j,k\} \subset \{1,2,3,4,5\}$. All higher-degree relations (such as the degree-3 relations in $H^3(C_5(\mathbb{C}))$) are consequences of these quadratic relations, by the Orlik--Solomon theorem.
appendices/general_relations.tex:91:by the ideal generated by $\binom{n}{3}$ quadratic Arnold relations (one for each triple $i < j < k$).
appendices/homotopy_transfer.tex:269:\section{Applications to minimal models}
appendices/homotopy_transfer.tex:290:\item Apply the homotopy transfer theorem to get $\{m_n\}_{n \geq 2}$ on $M$.
appendices/homotopy_transfer.tex:450:\section{Applications to chiral algebras}
appendices/homotopy_transfer.tex:563:Applying Theorem~\ref{thm:htt} to the strict $\Eone$-chiral algebra
appendices/homotopy_transfer.tex:773:at the associated graded level. Applying HTT with the perturbed
appendices/computational_tables.tex:4:This appendix collects numerical data for the bar complexes computed in Part~\ref{part:characteristic-datum}: Kontsevich weights for the deformation quantization star product, OPE structure constants for low-rank Kac--Moody and $\mathcal{W}$-algebras, Arnold relation expansions through $n = 4$, and modular form data at genera~$1$ and~$2$.
appendices/computational_tables.tex:92:\section{Arnold relation expansions}
appendices/computational_tables.tex:100:For $n = 4$, there are four Arnold relations, one for each $3$-element subset of
appendices/computational_tables.tex:110:$\{i,j\} \cap \{k,l\} = \emptyset$ are \emph{not} constrained by Arnold relations
appendices/computational_tables.tex:115:For any three distinct indices $i, j, k$, the fundamental Arnold relation is:
appendices/computational_tables.tex:131:(cf.\ the genus-$g$ formula in Appendix~\ref{app:theta}). The $2^4 = 16$ characteristics split into $6$ odd and $10$ even.
 succeeded in 51ms:
Total output lines: 9453

appendices/general_relations.tex:2:\label{app:geometric-dictionary}
appendices/general_relations.tex:28:Each entry represents a precise functor or natural transformation between categories. For instance, the correspondence ``Chiral multiplication $\leftrightarrow$ Residues at collision divisors'' is the content of Theorem~\ref{thm:residue-formula}, establishing that the multiplication map factors through the residue homomorphism. Similarly, ``Central extensions $\leftrightarrow$ Curved $A_\infty$ structures'' reflects Theorem~\ref{thm:heisenberg-bar}, showing how the failure of strict associativity due to central charges is precisely captured by the curvature term $m_0$.
appendices/general_relations.tex:34:\label{app:sign-conventions-general}
appendices/general_relations.tex:48:\label{app:ope-tables}
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/general_relations.tex:98:\label{app:curved-ainfty-formulas}
appendices/general_relations.tex:127:That is, when the curvature element is central, $m_1$ is strictly nilpotent ($m_1^2 = 0$). This is exactly the algebraic condition ensuring $d_{\text{bar}}^2 = 0$ in the bar complex (see the nine-term proof in \S\ref{sec:bar-nilpotency}).
appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
appendices/homotopy_transfer.tex:12:(Theorem~\ref{thm:bar-ainfty-complete}).
appendices/homotopy_transfer.tex:15:\label{prop:htt-rectification}
appendices/homotopy_transfer.tex:19:(Theorem~\ref{thm:rectification-meta}): given a deformation retract
appendices/homotopy_transfer.tex:40: (Theorem~\ref{thm:htt}) endows~$H$
appendices/homotopy_transfer.tex:61:\label{sec:ainfty-historical}
appendices/homotopy_transfer.tex:63:$A_\infty$ algebras were introduced by Stasheff~\cite{Sta63} to encode the homotopy-coherent associativity of loop space multiplication. The operadic viewpoint identifies them as algebras over the homology of the little intervals operad. For the role of bar-cobar duality in the chiral setting, see Chapter~\ref{chap:higher-genus}.
appendices/homotopy_transfer.tex:66:\label{sec:htt}
appendices/homotopy_transfer.tex:69:\label{thm:htt}
appendices/homotopy_transfer.tex:104:\begin{equation}\label{eq:ainfty-relation}
appendices/homotopy_transfer.tex:130:\label{def:sdr}



thinking
**Planning systematic seam audit**

I’m facing a task to conduct a systematic seam audit between appendices and chapters, particularly focusing on theory. I need to check that appendix results are cited correctly, avoid circular dependencies, and ensure consistent notation. This involves reading all relevant files and transition points carefully. For any inconsistencies or gaps, I'll note the issues precisely with file and line references and their solutions. It might be necessary to inspect all references from theory to appendices to build a clear map.
thinking
**Ensuring notation consistency**

I need to focus on maintaining notation consistency across the seams, including labels, section references, and notational names. Reading relevant files is essential, and I could leverage scripts to list references from theory to appendices, and vice versa. Using regex might help to filter out the correct labels. Maybe parsing files and crossing directories with tools like `rg` could simplify things. I should look to build cross-reference maps, utilizing commands for accurate findings based on file contents. It's about aligning everything clearly!
thinking
**Deciding on tools for analysis**

I’m figuring out that I might not need Python for this task since the developer suggested utilizing simple shell commands or apply_patch. For analysis, I could use Perl or Awk, but Ruby might be a better choice. Shell commands seem fine too! I may consider options like `rg`, a small Perl one-liner, or even `grep` and `sort`. I need to inspect main.tex to confirm the order of appendices and ensure they are referenced correctly after the theory. It's important to clarify which appendices are actually relevant!
codex
The seam is broad enough that I need a mechanical cross-reference map before judging prose. I’m extracting every cross-directory `\ref`/`\eqref` target and then checking the highest-risk seams manually: sign conventions, Arnold relations, higher-genus/nonlinear shadow appendices, the nilpotent-completion references, and any duplicated chapter/appendix pair.
Plan update
Audit will proceed by cross-reference extraction, then manual seam checks for citation correctness, circular proof dependence, and notation drift.
  → Build a cross-directory label/ref map between appendices/ and chapters/theory/
  • Read high-risk transition points and duplicated seam files line-by-line
  • Re-verify candidate findings and assemble exact file:line fixes
exec
/bin/zsh -lc "ruby -e '
labels={}
Dir[\"appendices/**/*.tex\",\"chapters/theory/**/*.tex\"].each do |f|
  File.readlines(f, chomp:true).each_with_index do |line,i|
    line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| labels[m[0]]=[f,i+1,line.strip] }
  end
end
Dir[\"appendices/**/*.tex\",\"chapters/theory/**/*.tex\"].sort.each do |f|
  File.readlines(f, chomp:true).each_with_index do |line,i|
    line.scan(/\\\\(?:ref|eqref|autoref|Cref|cref|nameref)\\{(["'^}]+)'"\\}/){|m|
      label=m[0]
      next unless labels[label]
      def_file,def_line,_=labels[label]
      from=f.start_with?(\"appendices/\") ? \"appendix\" : \"theory\"
      to=def_file.start_with?(\"appendices/\") ? \"appendix\" : \"theory\"
      next if from==to
      puts [from,to,f,i+1,label,def_file,def_line,line.strip].join(\"\\t\")
    }
  end
end
'" in /Users/raeez/chiral-bar-cobar succeeded in 147ms:
appendix	theory	appendices/arnold_relations.tex	169	thm:bar-nilpotency-complete	chapters/theory/bar_construction.tex	797	This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
appendix	theory	appendices/arnold_relations.tex	175	thm:arnold-higher-genus	chapters/theory/higher_genus_foundations.tex	2888	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
appendix	theory	appendices/arnold_relations.tex	175	thm:arnold-quantum	chapters/theory/higher_genus_foundations.tex	2889	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
appendix	theory	appendices/arnold_relations.tex	175	thm:arnold-genus1	chapters/theory/higher_genus_foundations.tex	4068	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
appendix	theory	appendices/arnold_relations.tex	175	sec:genus-2-complete	chapters/theory/higher_genus_foundations.tex	4216	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
appendix	theory	appendices/arnold_relations.tex	175	sec:genus-3-complete	chapters/theory/higher_genus_foundations.tex	4319	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
appendix	theory	appendices/arnold_relations.tex	515	thm:bar-nilpotency-complete	chapters/theory/bar_construction.tex	797	cancellation of Theorem~\ref{thm:bar-nilpotency-complete} is recovered
appendix	theory	appendices/arnold_relations.tex	523	thm:bar-nilpotency-complete	chapters/theory/bar_construction.tex	797	Theorem~\ref{thm:bar-nilpotency-complete} is the local manifestation of
appendix	theory	appendices/branch_line_reductions.tex	24	thm:modular-characteristic	chapters/theory/higher_genus_modular_koszul.tex	2846	(Theorem~\ref{thm:modular-characteristic}), the spectral characteristic
appendix	theory	appendices/branch_line_reductions.tex	25	thm:spectral-characteristic	chapters/theory/higher_genus_modular_koszul.tex	3541	(Theorem~\ref{thm:spectral-characteristic}), and the universal modular
appendix	theory	appendices/branch_line_reductions.tex	27	thm:universal-theta	chapters/theory/higher_genus_modular_koszul.tex	3574	(Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}).
appendix	theory	appendices/branch_line_reductions.tex	27	thm:mc2-full-resolution	chapters/theory/higher_genus_modular_koszul.tex	8167	(Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}).
appendix	theory	appendices/branch_line_reductions.tex	43	thm:universal-theta	chapters/theory/higher_genus_modular_koszul.tex	3574	Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}.
appendix	theory	appendices/branch_line_reductions.tex	43	thm:mc2-full-resolution	chapters/theory/higher_genus_modular_koszul.tex	8167	Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}.
appendix	theory	appendices/branch_line_reductions.tex	46	def:scalar-lane	chapters/theory/higher_genus_modular_koszul.tex	2712	(Definition~\ref{def:scalar-lane}) this further
appendix	theory	appendices/branch_line_reductions.tex	49	def:shadow-postnikov-tower	chapters/theory/higher_genus_modular_koszul.tex	12247	obstruction tower (Definition~\ref{def:shadow-postnikov-tower}),
appendix	theory	appendices/branch_line_reductions.tex	92	def:shadow-postnikov-tower	chapters/theory/higher_genus_modular_koszul.tex	12247	(Definition~\ref{def:shadow-postnikov-tower}).
appendix	theory	appendices/branch_line_reductions.tex	130	thm:modular-characteristic	chapters/theory/higher_genus_modular_koszul.tex	2846	(Theorem~\ref{thm:modular-characteristic}).
appendix	theory	appendices/branch_line_reductions.tex	134	thm:spectral-characteristic	chapters/theory/higher_genus_modular_koszul.tex	3541	(Theorem~\ref{thm:spectral-characteristic}).
appendix	theory	appendices/branch_line_reductions.tex	138	thm:universal-theta	chapters/theory/higher_genus_modular_koszul.tex	3574	(Theorems~\ref{thm:universal-theta}

thinking
**Considering output storage**

I should probably save the output for easier searching. Rerunning it in a file located in /tmp could help with that. It makes sense to create a cross-reference TSV in /tmp for our use, especially since the user won't see the command output. I guess I can use `exec_command` to write to /tmp, as that's allowed. Using shell redirect seems like a good idea, and then I can inspect the results later.
codex
The cross-reference graph is in hand. I’m now reading the bidirectional seams with the biggest chance of hidden failure: references that go both ways between the same appendix/theory pair, references to appendix-local theorem labels from theory, and spots where theory cites an appendix as if it were a chapter or foundational input.
exec
/bin/zsh -lc "ruby -e '
labels={}
Dir[\"appendices/**/*.tex\",\"chapters/theory/**/*.tex\"].each do |f|
  File.readlines(f, chomp:true).each_with_index do |line,i|
    line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| labels[m[0]]=[f,i+1] }
  end
end
File.open(\"/tmp/seam_refs.tsv\",\"w\") do |out|
  Dir[\"appendices/**/*.tex\",\"chapters/theory/**/*.tex\"].sort.each do |f|
    File.readlines(f, chomp:true).each_with_index do |line,i|
      line.scan(/\\\\(?:ref|eqref|autoref|Cref|cref|nameref)\\{(["'^}]+)'"\\}/){|m|
        label=m[0]
        next unless labels[label]
        def_file,def_line=labels[label]
        from=f.start_with?(\"appendices/\") ? \"appendix\" : \"theory\"
        to=def_file.start_with?(\"appendices/\") ? \"appendix\" : \"theory\"
        next if from==to
        out.puts [from,to,f,i+1,label,def_file,def_line,line.strip].join(\"\\t\")
      }
    end
  end
end
puts \"/tmp/seam_refs.tsv written\"'" in /Users/raeez/chiral-bar-cobar succeeded in 134ms:
/tmp/seam_refs.tsv written

thinking
**Analyzing cycles**

I need to analyze cycles, which means I can use a shell command to help me group bidirectional pairs by their file pairs. It seems like a straightforward approach, but I want to make sure I'm considering everything necessary for the analysis. I’ll think through how best to implement this and what specific details or commands I might need to ensure the output is accurate. Let's see how I can make this work!
exec
/bin/zsh -lc "awk -F '\\t' '"'$1=="theory" && $2=="appendix" {print $3":"$4" -> "$5" @ "$6":"$7}'"' /tmp/seam_refs.tsv | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk -F '\\t' '{print "'$3 " -> " $6}'"' /tmp/seam_refs.tsv | sort | uniq -c | sort -nr | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk -F '\\t' '{print "'$3 "'"\\t\" "'$6}'"' /tmp/seam_refs.tsv | sort | uniq > /tmp/pairs.tsv && awk -F '\\t' 'NR==FNR{a["'$1 FS $2]=1;next} {if(a[$2 FS $1]) print $1 " <-> " $2}'"' /tmp/pairs.tsv /tmp/pairs.tsv | sort -u" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/algebraic_foundations.tex:116 -> def:bar-complex-algebraic @ appendices/notation_index.tex:342
chapters/theory/algebraic_foundations.tex:1079 -> app:signs @ appendices/signs_and_shifts.tex:2
chapters/theory/algebraic_foundations.tex:1079 -> app:sign-conventions @ appendices/signs_and_shifts.tex:713
chapters/theory/bar_cobar_adjunction_inversion.tex:1876 -> thm:htt @ appendices/homotopy_transfer.tex:69
chapters/theory/bar_cobar_adjunction_inversion.tex:3506 -> thm:essential-image-koszul @ appendices/koszul_reference.tex:268
chapters/theory/bar_construction.tex:650 -> app:signs @ appendices/signs_and_shifts.tex:2
chapters/theory/bar_construction.tex:650 -> app:sign-conventions @ appendices/signs_and_shifts.tex:713
chapters/theory/bar_construction.tex:650 -> sec:sign-dictionary-complete @ appendices/signs_and_shifts.tex:1012
chapters/theory/bar_construction.tex:963 -> ver:d2-degree3 @ appendices/signs_and_shifts.tex:607
chapters/theory/bar_construction.tex:964 -> prop:master-sign @ appendices/signs_and_shifts.tex:576
chapters/theory/bar_construction.tex:964 -> app:signs @ appendices/signs_and_shifts.tex:2
chapters/theory/bar_construction.tex:1245 -> app:arnold-relations @ appendices/arnold_relations.tex:1
chapters/theory/chiral_hochschild_koszul.tex:1172 -> thm:nms-all-degree-master-equation @ appendices/nonlinear_modular_shadows.tex:2110
chapters/theory/chiral_hochschild_koszul.tex:2463 -> app:signs @ appendices/signs_and_shifts.tex:2
chapters/theory/chiral_hochschild_koszul.tex:2463 -> app:sign-conventions @ appendices/signs_and_shifts.tex:713
chapters/theory/chiral_hochschild_koszul.tex:2901 -> app:homotopy-transfer @ appendices/homotopy_transfer.tex:2
chapters/theory/chiral_hochschild_koszul.tex:2933 -> app:homotopy-transfer @ appendices/homotopy_transfer.tex:2
chapters/theory/chiral_hochschild_koszul.tex:5740 -> app:nonlinear-modular-shadows @ appendices/nonlinear_modular_shadows.tex:2
chapters/theory/chiral_hochschild_koszul.tex:5752 -> app:branch-line-reductions @ appendices/branch_line_reductions.tex:2
chapters/theory/chiral_hochschild_koszul.tex:5784 -> app:branch-line-reductions @ appendices/branch_line_reductions.tex:2
 succeeded in 51ms:
 240 appendices/ordered_associative_chiral_kd.tex -> chapters/theory/ordered_associative_chiral_kd.tex
  35 chapters/theory/higher_genus_modular_koszul.tex -> appendices/nonlinear_modular_shadows.tex
  34 appendices/nonlinear_modular_shadows.tex -> chapters/theory/higher_genus_modular_koszul.tex
  17 appendices/notation_index.tex -> chapters/theory/algebraic_foundations.tex
  17 appendices/branch_line_reductions.tex -> chapters/theory/higher_genus_modular_koszul.tex
  10 appendices/koszul_reference.tex -> chapters/theory/higher_genus_modular_koszul.tex
   8 appendices/notation_index.tex -> chapters/theory/configuration_spaces.tex
   8 appendices/homotopy_transfer.tex -> chapters/theory/higher_genus_foundations.tex
   7 chapters/theory/higher_genus_foundations.tex -> appendices/homotopy_transfer.tex
   6 chapters/theory/bar_construction.tex -> appendices/signs_and_shifts.tex
   6 appendices/koszul_reference.tex -> chapters/theory/bar_cobar_adjunction_curved.tex
   5 appendices/koszul_reference.tex -> chapters/theory/chiral_koszul_pairs.tex
   5 appendices/koszul_reference.tex -> chapters/theory/bar_cobar_adjunction_inversion.tex
   5 appendices/combinatorial_frontier.tex -> chapters/theory/chiral_koszul_pairs.tex
   5 appendices/arnold_relations.tex -> chapters/theory/higher_genus_foundations.tex
   4 chapters/theory/nilpotent_completion.tex -> appendices/homotopy_transfer.tex
   4 chapters/theory/introduction.tex -> appendices/signs_and_shifts.tex
   4 chapters/theory/higher_genus_complementarity.tex -> appendices/nonlinear_modular_shadows.tex
   4 chapters/theory/cobar_construction.tex -> appendices/signs_and_shifts.tex
   4 appendices/ordered_associative_chiral_kd.tex -> chapters/theory/configuration_spaces.tex
 succeeded in 50ms:
appendices/arnold_relations.tex <-> chapters/theory/bar_construction.tex
appendices/combinatorial_frontier.tex <-> chapters/theory/chiral_koszul_pairs.tex
appendices/combinatorial_frontier.tex <-> chapters/theory/higher_genus_modular_koszul.tex
appendices/homotopy_transfer.tex <-> chapters/theory/higher_genus_complementarity.tex
appendices/homotopy_transfer.tex <-> chapters/theory/higher_genus_foundations.tex
appendices/koszul_reference.tex <-> chapters/theory/bar_cobar_adjunction_inversion.tex
appendices/koszul_reference.tex <-> chapters/theory/existence_criteria.tex
appendices/nonlinear_modular_shadows.tex <-> chapters/theory/chiral_koszul_pairs.tex
appendices/nonlinear_modular_shadows.tex <-> chapters/theory/higher_genus_complementarity.tex
appendices/nonlinear_modular_shadows.tex <-> chapters/theory/higher_genus_foundations.tex
appendices/nonlinear_modular_shadows.tex <-> chapters/theory/higher_genus_modular_koszul.tex
appendices/notation_index.tex <-> chapters/theory/algebraic_foundations.tex
appendices/signs_and_shifts.tex <-> chapters/theory/bar_construction.tex
chapters/theory/algebraic_foundations.tex <-> appendices/notation_index.tex
chapters/theory/bar_cobar_adjunction_inversion.tex <-> appendices/koszul_reference.tex
chapters/theory/bar_construction.tex <-> appendices/arnold_relations.tex
chapters/theory/bar_construction.tex <-> appendices/signs_and_shifts.tex
chapters/theory/chiral_koszul_pairs.tex <-> appendices/combinatorial_frontier.tex
chapters/theory/chiral_koszul_pairs.tex <-> appendices/nonlinear_modular_shadows.tex
chapters/theory/existence_criteria.tex <-> appendices/koszul_reference.tex

thinking
**Considering list organization**

I see that I might need to create an appendix to include theory references too. It sounds like a good idea to keep everything organized and make sure I don't miss out on important connections. By listing the references clearly, I can ensure they are accessible for others who might want to refer to them later. Let’s make sure it’s done thoughtfully for clarity and completeness!
exec
/bin/zsh -lc "awk -F '\\t' '"'$1=="appendix" && $2=="theory" {print $3":"$4" -> "$5" @ "$6":"$7}'"' /tmp/seam_refs.tsv | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/arnold_relations.tex:169 -> thm:bar-nilpotency-complete @ chapters/theory/bar_construction.tex:797
appendices/arnold_relations.tex:175 -> thm:arnold-higher-genus @ chapters/theory/higher_genus_foundations.tex:2888
appendices/arnold_relations.tex:175 -> thm:arnold-quantum @ chapters/theory/higher_genus_foundations.tex:2889
appendices/arnold_relations.tex:175 -> thm:arnold-genus1 @ chapters/theory/higher_genus_foundations.tex:4068
appendices/arnold_relations.tex:175 -> sec:genus-2-complete @ chapters/theory/higher_genus_foundations.tex:4216
appendices/arnold_relations.tex:175 -> sec:genus-3-complete @ chapters/theory/higher_genus_foundations.tex:4319
appendices/arnold_relations.tex:515 -> thm:bar-nilpotency-complete @ chapters/theory/bar_construction.tex:797
appendices/arnold_relations.tex:523 -> thm:bar-nilpotency-complete @ chapters/theory/bar_construction.tex:797
appendices/branch_line_reductions.tex:24 -> thm:modular-characteristic @ chapters/theory/higher_genus_modular_koszul.tex:2846
appendices/branch_line_reductions.tex:25 -> thm:spectral-characteristic @ chapters/theory/higher_genus_modular_koszul.tex:3541
appendices/branch_line_reductions.tex:27 -> thm:universal-theta @ chapters/theory/higher_genus_modular_koszul.tex:3574
appendices/branch_line_reductions.tex:27 -> thm:mc2-full-resolution @ chapters/theory/higher_genus_modular_koszul.tex:8167
appendices/branch_line_reductions.tex:43 -> thm:universal-theta @ chapters/theory/higher_genus_modular_koszul.tex:3574
appendices/branch_line_reductions.tex:43 -> thm:mc2-full-resolution @ chapters/theory/higher_genus_modular_koszul.tex:8167
appendices/branch_line_reductions.tex:46 -> def:scalar-lane @ chapters/theory/higher_genus_modular_koszul.tex:2712
appendices/branch_line_reductions.tex:49 -> def:shadow-postnikov-tower @ chapters/theory/higher_genus_modular_koszul.tex:12247
appendices/branch_line_reductions.tex:92 -> def:shadow-postnikov-tower @ chapters/theory/higher_genus_modular_koszul.tex:12247
appendices/branch_line_reductions.tex:130 -> thm:modular-characteristic @ chapters/theory/higher_genus_modular_koszul.tex:2846
appendices/branch_line_reductions.tex:134 -> thm:spectral-characteristic @ chapters/theory/higher_genus_modular_koszul.tex:3541
appendices/branch_line_reductions.tex:138 -> thm:universal-theta @ chapters/theory/higher_genus_modular_koszul.tex:3574






thinking
**Clarifying appendix and chapters**

The user is asking about the relationship between appendices and chapters or theories, possibly indicating some duplicate concerns. I think I need to sort out whether those files truly duplicate content. Wait, the appendix references the theory file often, but the theory doesn’t reference the appendix as much. If that's the case, it could still be acceptable because the appendix serves as supplementary material. I should clarify this better for the user!
thinking
**Evaluating content conflicts**

I have a status conflict because there’s the same content in both the appendix and theory volumes. It might not be relevant unless there’s an inconsistency that needs addressing. I should consider inspecting the build or labels to check for undefined references. It's possible there are references to nonexistent labels within the seam. I might grep the logs or consider using `latexmk` to identify any undefined refs. Ultimately, I aim to focus on confirmed inconsistencies.
thinking
**Identifying referencing issues**

I’m facing some misclassified reference texts, like confusion between chapter and appendix labels or misnamed file labels. There could also be circular dependencies if an appendix theorem cites a theory theorem that references back to the same appendix. I need to check for cycles and see if those references are foundational or just applications. Candidates to investigate include links between bar construction and Arnold relations, particularly if they reference each other in a way that’s circular, unless they're merely historical.
thinking
**Inspecting potential circular references**

I need to take a closer look at certain references. For example, between higher genus foundations and homotopy transfer, the theory cites appendix HTT results while the appendix refers back to the theory's theorems. There might not be any circularity if those are just applications. Then there's the higher genus modular Koszul and nonlinear modular shadows pair, where the theory relies on appendix results. It could get circular if a theorem in theory depends on an appendix theorem that references back. I need to inspect these specific cases.
thinking
**Examining theorem dependencies**

I'm analyzing the relationship between a core theory and an appendix theorem. It seems the core theorem relies on appendix results, but what if the appendix also references back to the core? I’ve got to check these connections closely. It could be acyclic, which might be fine if the appendix is just supplementary. To simplify, I might look at a claim registry to see if any dependencies are unproven or depend back on prior claims. I’m considering using a CSV file for this.
thinking
**Investigating theory and appendix citations**

I'm looking into whether theory labels reference appendix conjectures. For instance, the `higher_genus_modular_koszul` might cite `conj:w3-bar-gf` in the appendix. I need to check if this is within a proved theorem or just a remark; it could be okay unless the theorem relies on the conjecture. Since the user has asked for a thorough audit, I might explore a CSV of suspicious dependencies to find any risky claims or label conflicts. I should examine the connections between appendices and chapters.
codex
I’ve narrowed the likely failure modes. Next pass is focused on places where the seam is structurally wrong rather than merely cross-referenced: theory citing a notation appendix as a source of definitions, theory referring to appendix sections as if they were appendices/chapters, and any proved theorem block whose appendix dependency points back into the same theory lane.
exec
/bin/zsh -lc "rg -n \"appendices/|chapters/theory/|appendix|theory\" suspicious_proved_claim_dependencies.csv label_status_conflicts.csv master_claim_ledger_filtered.csv 2>/dev/null | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Chapter~\\\\ref\\{app:|Ch\\\\.?~\\\\ref\\{app:|Appendix~\\\\ref\\{sec:|Appendix~\\\\ref\\{subsec:|Appendix~\\\\ref\\{thm:|Appendix~\\\\ref\\{prop:|Appendix~\\\\ref\\{lem:\" chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Definition~\\\\ref\\{def:["'^}]+'"\\}\" chapters/theory | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 exited 1 in 50ms:

 succeeded in 50ms:


thinking
**Evaluating command issues**

I’m considering if there are any files available; perhaps a CSV in the root, but I don't think it's necessary. The second command with `rg` failed, maybe due to quoting issues with regex. I need a simpler search. The third output showing no matches is odd; I might try `rg` on `Definition\ref{def:` but that's probably not right either given the backslashes. It seems like a good idea to switch to using `grep` for a simpler approach.
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\ref\\{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{subsec:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{sec:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{thm:|Appendix~\\\\ref\\{prop:|Appendix~\\\\ref\\{lem:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:5740:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/theory/introduction.tex:1952:(Chapter~\ref{app:nonlinear-modular-shadows}).
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:1104:For historical background on $A_\infty$ algebras, see Appendix~\ref{sec:ainfty-historical}.
chapters/theory/algebraic_foundations.tex:296:the coderived category (Appendix~\ref{sec:coderived-models});
chapters/theory/algebraic_foundations.tex:377:(Appendix~\ref{sec:coderived-models}).%
chapters/theory/chiral_koszul_pairs.tex:292:(Appendix~\ref{sec:coderived-models}),
 exited 1 in 51ms:

 exited 1 in 51ms:


thinking
**Investigating theory file sections**

I'm considering the section labels in the theory file. The "coderived-models" label is interesting, and I think I need to inspect it further. It might not be directly related to my current focus, but I'm curious. I definitely want to look at "higher_genus_foundations" in the appendix too. It sounds like it could give me some valuable insights. This exploration should help clarify my understanding!
exec
/bin/zsh -lc "sed -n '1944,1958p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '56,76p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5732,5746p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1088,1112p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 higher operations into the differential of~$\Omega(B(H))$.
\end{enumerate}
\end{proof}

\section{Historical origins}
\label{sec:ainfty-historical}

$A_\infty$ algebras were introduced by Stasheff~\cite{Sta63} to encode the homotopy-coherent associativity of loop space multiplication. The operadic viewpoint identifies them as algebras over the homology of the little intervals operad. For the role of bar-cobar duality in the chiral setting, see Chapter~\ref{chap:higher-genus}.

\section{The homotopy transfer theorem}
\label{sec:htt}

\begin{theorem}[Homotopy transfer theorem \cite{LV12, Kadeishvili80}; \ClaimStatusProvedElsewhere]
\label{thm:htt}
Let $(V, d_V)$ and $(W, d_W)$ be chain complexes with:
\begin{enumerate}[label=(\roman*)]
\item A chain map $p: V \to W$ (projection).
\item A chain map $\iota: W \to V$ (inclusion).
\item A chain homotopy $h: V \to V[-1]$ satisfying $\id_V - \iota p = d_V h + h d_V$.
\item The \emph{side conditions} (compatibility of $h$ with $p, \iota$): $p \iota = \id_W$, $h \iota = 0$, $p h = 0$, $h^2 = 0$.
 succeeded in 50ms:
\underbrace{\Theta_\cA}_{\text{universal class}}.
\]
The scalar characteristic $\kappa(\cA)$ is proved. The spectral
discriminant $\Delta_\cA$ is proved. The cubic and quartic shadow
classes $[\mathfrak C_\cA]$ and $[\mathfrak Q_\cA]$ are the first
genuinely nonlinear modular invariants, computable on any family
where the cyclic deformation package is available through the
relevant order
(Chapter~\ref{app:nonlinear-modular-shadows}).
The branch-line reductions
(Appendix~\ref{app:branch-line-reductions}) extract exact
finite-dimensional quotients of this layer, including genus-$2$
transparency and the universal genus-$3$ constant~$7$ on the shared
$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.
For class~$\mathbf{M}$ algebras the infinite tower has a computable
 succeeded in 51ms:
so the genus-$1$ scalar trace is
$\kappa(\cA)\lambda_1$
\textup{(}g=1 only; all-weight at g=1 is unconditional\textup{)}.
The same scalar shadow recursion and clutching laws then identify
$\Lambda_g$ with $c_g(\mathbb{E}) = \lambda_g$ at every genus on the
proved uniform-weight scalar lane. Pairing with the
Faber--Pandharipande test class produces
$\sum_{g \geq 1} \mathrm{obs}_g \cdot \hbar^{2g}
= \kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
Thus the scalar $\kappa(\cA)$ is fixed by the genus-$1$ Chern
character, while the higher obstruction classes are the Hodge Chern
classes selected by the same scalar recursion.

\section{\texorpdfstring{$A_\infty$ structures and higher operations}{A-infinity structures and higher operations}}

For historical background on $A_\infty$ algebras, see Appendix~\ref{sec:ainfty-historical}.

% ================================================================
% SECTION 4.2: THE GEOMETRIC BAR COMPLEX AND ITS A-INFINITY STRUCTURE
 succeeded in 51ms:
fake linear splitting. A natural target: compute the
cubic term of~$S_\cA$ for Heisenberg,
$\widehat{\mathfrak{sl}}_2$, and $\beta\gamma$.
\end{remark}

\begin{remark}[Nonlinear shadow calculus]
\label{rem:nonlinear-shadow-pointer}
The first nonlinear jets of~$S_\cA$ are developed systematically
in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
shadow cocycle
$\Theta_\cA^{\le 4} = H_\cA + \mathfrak C_\cA + \mathfrak Q_\cA$
is constructed, its master and clutching equations are proved,
and the three frame families are shown to realize the Gaussian,
Lie/tree, and contact/quartic archetypes respectively.
The modular quartic resonance class~$\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)$

thinking
**Fixing appendix references**

I’m encountering issues with using "Chapter" as an appendix label. I need to find the exact fix, but there may be more to explore. I could search across all files instead of just a narrow focus. I've noticed references like `Appendix\ref{sec:coderived-models}`, but some labels might be defined differently. There’s definitely a seam issue on line 1104, and I should look for patterns like `Chapter\ref{app:` and `Appendix\ref{sec:` using regex for better results.
exec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:|Chapter~\\\\ref\\{app:|Ch\\.?~\\\\ref\\{app:' chapters/theory | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{sec:["'^}]+'"' chapters/theory | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Ch\\.?~\\\\ref\\{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:2224:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2377: (Ch.~\ref{app:nonlinear-modular-shadows}).
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:1104:For historical background on $A_\infty$ algebras, see Appendix~\ref{sec:ainfty-historical}.
chapters/theory/algebraic_foundations.tex:296:the coderived category (Appendix~\ref{sec:coderived-models});
chapters/theory/algebraic_foundations.tex:377:(Appendix~\ref{sec:coderived-models}).%
chapters/theory/chiral_koszul_pairs.tex:292:(Appendix~\ref{sec:coderived-models}),
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:4846:(Appendix~\ref{app:nonlinear-modular-shadows});
chapters/theory/higher_genus_modular_koszul.tex:10136:Appendix~\ref{app:nonlinear-modular-shadows} at each finite
chapters/theory/higher_genus_modular_koszul.tex:12288: (Appendix~\ref{app:nonlinear-modular-shadows}).
chapters/theory/higher_genus_modular_koszul.tex:12327: Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:13218:and Appendix~\ref{app:nonlinear-modular-shadows}
chapters/theory/higher_genus_modular_koszul.tex:15461:Appendix~\ref{app:nonlinear-modular-shadows}:
chapters/theory/higher_genus_modular_koszul.tex:15475:Appendix~\ref{app:nonlinear-modular-shadows} enumerates
chapters/theory/higher_genus_modular_koszul.tex:29755:(Appendix~\ref{app:nonlinear-modular-shadows}) is
chapters/theory/higher_genus_modular_koszul.tex:31098:and Appendix~\ref{app:nonlinear-modular-shadows}) is the
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:525:full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
chapters/theory/filtered_curved.tex:131:Completion technology: Appendix~\ref{app:nilpotent-completion}.
chapters/theory/bar_cobar_adjunction_inversion.tex:70:(Appendix~\ref{app:nilpotent-completion}); and general algebras may
chapters/theory/introduction.tex:1952:(Chapter~\ref{app:nonlinear-modular-shadows}).
chapters/theory/introduction.tex:1954:(Appendix~\ref{app:branch-line-reductions}) extract exact
chapters/theory/introduction.tex:2224:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2377: (Ch.~\ref{app:nonlinear-modular-shadows}).
chapters/theory/introduction.tex:2615: See Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}.
chapters/theory/introduction.tex:2624: (Appendix~\ref{app:nilpotent-completion}).
chapters/theory/introduction.tex:2638:Appendix~\ref{app:signs}.

thinking
**Exploring Circular References**

I'm thinking it through: there seems to be a circular reference between a theory classification table and the appendix. The table leads to the appendix for W1+∞, and then the appendix sends readers back to the classification. This might create a confusing loop rather than proving circularity. I wonder if I need to clarify the appendix or change some references to make things clearer. It feels like there’s a connectivity gap that requires addressing.
exec
/bin/zsh -lc "sed -n '560,620p' appendices/signs_and_shifts.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,660p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '952,972p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '996,1028p' appendices/signs_and_shifts.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
d_\Omega(s^{-1}c_1 \otimes s^{-1}c_2) &= d_\Omega(s^{-1}c_1) \otimes s^{-1}c_2
 + (-1)^{|s^{-1}c_1|} s^{-1}c_1 \otimes d_\Omega(s^{-1}c_2) \\
&= \Bigl( -s^{-1}(dc_1) - \sum (-1)^{|c_1'|} s^{-1}c_1' \otimes s^{-1}c_1'' \Bigr) \otimes s^{-1}c_2 \\
&\quad + (-1)^{|c_1|-1} s^{-1}c_1 \otimes \Bigl( -s^{-1}(dc_2) - \sum (-1)^{|c_2'|} s^{-1}c_2' \otimes s^{-1}c_2'' \Bigr)
\end{align*}

Expanding:
\begin{align*}
d_\Omega(s^{-1}c_1 \otimes s^{-1}c_2) &= -s^{-1}(dc_1) \otimes s^{-1}c_2 \\
&\quad - \sum (-1)^{|c_1'|} s^{-1}c_1' \otimes s^{-1}c_1'' \otimes s^{-1}c_2 \\
&\quad + (-1)^{|c_1|} s^{-1}c_1 \otimes s^{-1}(dc_2) \\
&\quad + (-1)^{|c_1|} \sum (-1)^{|c_2'|} s^{-1}c_1 \otimes s^{-1}c_2' \otimes s^{-1}c_2''
\end{align*}
\end{computation}

\begin{proposition}[Master sign formula {\cite{LV12}}; \ClaimStatusProvedElsewhere]
\label{prop:master-sign}
For the bar complex of an $\Ainf$-algebra $(A, \{m_n\})$, the full differential 
on $[a_1|\cdots|a_n]$ is:
\[
 succeeded in 51ms:
\subsubsection{Pitfall 3: collision divisor ordering}

\emph{Convention.} We write collision divisors with $i < j$: $\colldiv{1}{3}$ rather than $\colldiv{3}{1}$. Since $\colldiv{i}{j} = \{z_i = z_j\}$ is an unordered locus, $\colldiv{3}{1} = \colldiv{1}{3}$ (no sign). Likewise, the logarithmic forms satisfy $\LogForm{j}{i} = \LogForm{i}{j}$ since $d\log(z_j - z_i) = d\log(-(z_i - z_j)) = d\log(z_i - z_j)$.

The sign convention $e_{ji} = -e_{ij}$ applies only to Orlik--Solomon algebra generators (an algebraic convention for exterior algebra presentations), not to the geometric forms or divisors.

\subsubsection{Pitfall 4: Arnold relation orientation}

\emph{Wrong.} Assuming Arnold relations hold without signs.

\emph{Right.} The cyclic sum includes signs from wedge product antisymmetry:
\[\LogForm{1}{2} \wedge \LogForm{2}{3} + \LogForm{2}{3} \wedge \LogForm{3}{1} + \LogForm{3}{1} \wedge \LogForm{1}{2} = 0\]

Note: Each term has a $+$ sign in the cyclic sum, but the individual forms anticommute.

\subsection{Sign convention dictionary}
\label{sec:sign-dictionary-complete}

\begin{table}[ht!]
\centering
 succeeded in 51ms:
$d_{\mathrm{internal}} \circ \Res_{D_{ij}}
= \Res_{D_{ij}} \circ d_{\mathrm{internal}}$ follows:
$\Res_{D_{ij}}$ is a $\cD_X$-module operation, and
$d_\cA$ is $\cD_X$-linear.

For $\{d_1, d_3\} = 0$: the operators $d_1$ and $d_3$ act on the algebra and form tensor factors respectively. The Koszul sign accompanying $d_3$ includes a factor $(-1)^{\sum_i |\phi_i|}$ from passing the de Rham differential past the algebra elements. After $d_1$ increases one algebra degree by $1$, the sign acquires an extra factor of $(-1)$. Thus $d_3 \circ d_1 = -d_1 \circ d_3$, and the anticommutator vanishes.

For $\{d_2, d_3\} = 0$: this follows from the residue exact sequence for logarithmic forms. On a normal crossing divisor $D = \bigcup D_{ij} \subset \overline{C}_{n+1}(X)$, the residue map fits into the exact sequence $0 \to \Omega^k \to \Omega^k(\log D) \xrightarrow{\text{Res}} \bigoplus_{D_{ij}} \Omega^{k-1}_{D_{ij}}(\log D') \to 0$, and the de Rham differential is compatible with the residue map: $\text{Res}_{D_{ij}} \circ d_{\text{dR}} = d_{\text{dR}}|_{D_{ij}} \circ \text{Res}_{D_{ij}}$. Since $d_2$ is a signed sum of residues and $d_3 = d_{\text{dR}}$, they anticommute (with signs from Convention~\ref{conv:orientations-enhanced}).
\end{proof}

\begin{remark}[Sign-level verification]\label{rem:sign-bridge}
For a complete sign-by-sign verification of $d^2 = 0$ at low degrees
(including the explicit computation for degree-3 elements $[a|b|c]$ in a
graded associative algebra), see Verification~\ref{ver:d2-degree3} and
Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
\end{remark}

\begin{remark}[Synthesis]\label{rem:d-squared-synthesis}\label{rem:geometric-miracle}
The three mechanisms entering the proof of $d^2 = 0$,
the Borcherds identity (algebra), Stokes' theorem (topology), and
 succeeded in 51ms:
$d_{\text{residue}}$ extracts OPE coefficients via residues
at collision divisors~$D_{ij}$;
$d_{\text{form}}$ is the de~Rham differential on configuration space,
enforcing Ward identities
(Lemma~\ref{lem:ddr-preserves-log}).

Nilpotency $d^2 = 0$ is \emph{not} automatic. Among the nine cross-terms in
$(d_1 + d_2 + d_3)^2$, the critical one is
$d_{\text{residue}}^2 = 0$: this requires the full Borcherds
identity, not merely Jacobi
(Proposition~\ref{prop:pole-decomposition}). The remaining
cross-terms vanish by Stokes
($\{d_{\text{form}}, d_{\text{residue}}\} = 0$) and the
derivation property.
\end{remark}

\begin{example}[Heisenberg degree-\texorpdfstring{$1$}{1} bar differential]\label{ex:heisenberg-d-deg1}
\label{ex:free-boson-d-deg1}
The Heisenberg algebra $\mathcal{H}_k$ with OPE $J(z)J(w) = k/(z-w)^2 + \text{regular}$ has bar differential
$d_{\mathrm{res}}(J \otimes J \otimes \eta_{12}) = J_{(1)}J = k \cdot \mathbf{1}$

thinking
**Investigating notation consistency**

I’m looking into the appendix sign proposition, which is proved elsewhere, and how it supports the theory without being circular. There's a potential issue with line 650 of bar_construction mentioning "total degree |\phi|+k". It might need to be consistent with the appendix, I think. I should inspect theory line 116 in algebraic_foundations, as it references the notation_index definition, so I’ll focus on that and the notation_index entry.
exec
/bin/zsh -lc "sed -n '104,124p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{quadratic algebra|textbf}
A graded algebra $A = T(V)/I$ is \emph{quadratic} if:
\begin{enumerate}
\item $V$ is a graded vector space (generators)
\item $I \subset V \otimes V$ is a subspace of relations in degree 2
\item The defining ideal is $(I)$ generated by $I$
\end{enumerate}
We write $A = A(V, R)$ where $R \subset V \otimes V$ are the
relations. The algebra carries a canonical \emph{augmentation}
$\varepsilon \colon A \twoheadrightarrow k$ sending all generators
to zero; the \emph{augmentation ideal} is
$\bar{A} = \ker(\varepsilon) = \bigoplus_{n \geq 1} V^{\otimes n}/(I)$.
The bar construction (Definition~\ref{def:bar-complex-algebraic})
is built from~$\bar{A}$.
\end{definition}

\begin{example}[Prototypical examples]
\label{ex:classical-quadratic-algebras}
\index{symmetric algebra}
\index{exterior algebra}
exec
/bin/zsh -lc "sed -n '334,350p' appendices/notation_index.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{definition}[A-infinity algebra]\label{def:ainf-algebra}
We use the curved/filtered \(A_\infty\) framework fixed in Definition~\ref{def:curved-ainfty}.
\end{definition}

\begin{definition}[Arnold relations]\label{def:arnold-relations}
The Arnold-relation package is the one established in Theorem~\ref{thm:arnold-relations}.
\end{definition}

\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic}
The algebraic bar complex is represented by the DG coalgebra model of Theorem~\ref{thm:bar-coalgebra}.
\end{definition}

\begin{definition}[Geometric bar complex]\label{def:geometric-bar-complex}
The geometric bar complex is Definition~\ref{def:geometric-bar}.
\end{definition}

\begin{definition}[Central charge]\label{def:central-charge}


thinking
**Inspecting theorem dependencies**

I'm looking into the theorem and its relation to a theory here, perhaps around line 12725 in the theory chapter and something in the appendix around 2110. I'll need to check if the appendix theorems depend on the core theory theorem labeled `thm:shadow-archetype-classification`. It’s crucial to identify any circular dependencies where one cites the other, so I’ll search for references in the appendix and verify if the cited theory theorem appears earlier or later. Let’s ensure there’s no circularity!
thinking
**Searching for theorem references**

I might try using a script to check if any lines in the appendix reference a theorem label and then use `\ref{...}` to point back to the theory label. It sounds a bit tricky, so I might need to do some manual checks for the major candidates. I’ll focus on references like `thm:nms-all-degree-master-equation` and `higher_genus_modular_koszul`, as well as `thm:nms-finite-termination`. I'll search the appendix around their proofs and see how they correlate with the theory.
codex
The notation-index dependency is a real seam defect, not just style: a theory definition currently points into a notation appendix whose own “definition” points back into theory. I’m checking the same kind of loop in the nonlinear-shadow and homotopy-transfer seams now, because that is where proof-level circularity is most plausible.
exec
/bin/zsh -lc "sed -n '2088,2210p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12696,12770p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
where $c_{p,q}=1$ if $p<q$ and $c_{p,p}=\frac12$, and the bracket is the single-edge sewing contraction of Construction~\ref{constr:nms-sewing-product}. The first cases are
\begin{alignat}{2}
\mathfrak o_{\cA}^{(4)}
&= \tfrac12\{\mathfrak C_{\cA},\mathfrak C_{\cA}\}_{H_{\cA}},
&\qquad&\text{(quartic)}
\label{eq:nms-quartic-obstruction-recalled}
\\
\mathfrak o_{\cA}^{(5)}
&= \{\mathfrak C_{\cA},\mathfrak Q_{\cA}\}_{H_{\cA}},
&\qquad&\text{(quintic)}
\label{eq:nms-quintic-obstruction}
\\
\mathfrak o_{\cA}^{(6)}
&= \tfrac12\{\mathfrak Q_{\cA},\mathfrak Q_{\cA}\}_{H_{\cA}}
+\{\mathfrak C_{\cA},\mathrm{Sh}_5(\cA)\}_{H_{\cA}}.
&\qquad&\text{(sextic)}
\label{eq:nms-sextic-obstruction}
\end{alignat}
\end{definition}
exec
/bin/zsh -lc "sed -n '1188,1236p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32140,32420p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proof}
Proposition~\ref{prop:mc2-functoriality}(iii) provides
$f_*^{\mathrm{sh}}$ as a bigrading-preserving map on
cohomology. It is a Lie algebra morphism because
$f_*$ is a dg~Lie morphism at the chain level
(composition with an algebra morphism preserves the
convolution bracket). For the quasi-isomorphism
assertion: when $f\colon \cA \to \cB$ is a
quasi-isomorphism, the induced map
$\operatorname{End}(f)\colon \operatorname{End}_\cA(n)
\to \operatorname{End}_\cB(n)$ is a quasi-isomorphism
of chain complexes for each~$n$. Since
$C_*(\overline{\cM}_{g,n})$ is a chain complex of
free abelian groups \textup{(}cellular chains on a
CW complex\textup{)}, the functor
$\operatorname{Hom}(C_*(\overline{\cM}_{g,n}),\, -)$
preserves quasi-isomorphisms, so
$f_*$ is a quasi-isomorphism of convolution algebras.
The descended map on cohomology is therefore an
 succeeded in 51ms:
\end{proof}

\begin{corollary}[Pure contact boundary law; \ClaimStatusProvedHere]
\label{cor:nms-betagamma-boundary-law}
On the weight/contact slice of $\beta\gamma$ one has
\[
\xi^*\mathfrak Q_{\beta\gamma}
=
H_{\beta\gamma}\star_{P_{\beta\gamma}}\mathfrak Q_{\beta\gamma}
+
\mathfrak Q_{\beta\gamma}\star_{P_{\beta\gamma}}H_{\beta\gamma}.
\]
There is no cubic tree contribution.
\end{corollary}

\begin{proof}
Apply the quartic boundary recursion with $\mathfrak C_{\beta\gamma}=0$.\qedhere
\end{proof}

\begin{theorem}[Primitive nonlinear archetype trichotomy; \ClaimStatusProvedHere]
 succeeded in 51ms:
$G$ and~$C$ share $(0)$ in the pf column at genus~$2$.
The full depth classification requires the critical discriminant
$\Delta = 8\kappa S_4$
\textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)},
which distinguishes $L$ \textup{(}$\Delta = 0$\textup{)} from~$M$
\textup{(}$\Delta \neq 0$\textup{)}, and~$G$ \textup{(}$\alpha = 0$,
$\Delta = 0$\textup{)} from~$C$
\textup{(}stratum separation\textup{)}.
\end{theorem}

\begin{proof}
From the inductive genus determination
(Corollary above),
$\Theta^{(2)} = \Theta^{(2)}_{\mathrm{loop}^2}
+ \Theta^{(2)}_{\mathrm{sep}\circ\mathrm{loop}}
+ \Theta^{(2)}_{\mathrm{pf}}$.

The loop${}^2$ shell
$\Theta^{(2)}_{\mathrm{loop}^2} =
-\tfrac{1}{2}[\Theta^{(1)}, \Theta^{(1)}]$
exec
/bin/zsh -lc "sed -n '12324,12364p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3378,3810p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5350,5370p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4684,4718p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item $S_4 = \mathfrak{Q}(\cA)$ is the quartic contact term: the
 Wilson coefficient of a four-point bulk interaction, carrying
 the clutching-law data of
 Appendix~\ref{app:nonlinear-modular-shadows}.
\item $S_r$ for $r \geq 5$ are the higher-loop corrections to
 boundary-bulk reconstruction at degree~$r$.
\end{itemize}
The holographic reading is compatible with the bar-intrinsic
definition because $\Theta_{\cA} = D_{\cA} - d_0$ is itself a
bar-local invariant
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)},
so each $S_r$ depends only on~$\cA$ and not on any auxiliary
bulk structure: the bulk is \emph{recovered} from the corrections,
not assumed before them. This reading does not change the
theorem statements; it names a physical content the combinatorial
definition already carries.
\end{remark}

\begin{remark}[Depth classification as holographic truncation]
\label{rem:depth-classification-holographic-truncation}
 succeeded in 52ms:
\label{rem:three-archetypes-lagrangian}
The fake-complementarity criterion reframes the archetype trichotomy
(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
so the dual Lagrangian bends cubically. The $\beta\gamma$ system is
quartic on the weight/contact slice. Virasoro is the first family
where the dual Lagrangian has both cubic and quartic bending,
and the complementarity potential is genuinely non-polynomial; its
shadow obstruction tower is infinite (Theorem~\ref{thm:nms-finite-termination}).
\end{remark}

\begin{remark}[Shadow obstruction tower as period correction]
\label{rem:shadow-tower-period-correction}
\index{period correction!shadow tower}
The shadow hierarchy
$\kappa \to \Delta \to \mathfrak{C}
\to \mathfrak{Q} \to \Theta$
admits a concrete interpretation as the Taylor expansion of the
 succeeded in 50ms:
$\cA$ are equivalent:
\begin{enumerate}[label=(\roman*)]
\item The bar spectral sequence
$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g\Bbar_g(\cA))$
collapses at~$E_2$ for all $g \geq 0$.
\item The filtered $\Ainf$-algebra $\Omega_g(\Bbar_g(\cA))$ is
\emph{formal}: quasi-isomorphic to its cohomology with the
transferred $\Ainf$-structure
(Theorem~\textup{\ref{thm:chiral-htt}}).
\item The transferred higher operations satisfy
$\tilde{m}_n^{(g)} = 0$ for $n \geq 3$ and all~$g$
(Koszulness at all genera).
\end{enumerate}
In the factorization homology picture, formality means that
$\int_{\Sigma_g}\cA$ is determined by $\int_{\mathbb{P}^1}\cA$
and the handle attachments, with no higher coherence obstructions.
\end{proposition}

\begin{proof}
(i) $\Rightarrow$ (ii): The spectral sequence arises from the bar
 succeeded in 52ms:
Theorem~\ref{thm:completed-bar-cobar-strong};
lattice filt.\ =
Theorem~\ref{thm:lattice:koszul-morphism};
null vect.\ = Kac--Shapovalov obstruction
(Theorem~\ref{thm:kac-shapovalov-koszulness});
Cartan~$H^2$ = abelian Cartan subalgebra classes
surviving in $H^2(\barB)$
(Remark~\ref{rem:admissible-koszul-status}).
\textit{Shadow}: archetype class $G$/$L$/$C$/$M$
(Theorem~\ref{thm:nms-archetype-trichotomy})
and shadow depth $r_{\max}$;
all four classes contain Koszul algebras
(shadow depth $\neq$ Koszulness).

\smallskip\noindent
${}^{\dagger}$\,The symplectic fermion
($\beta\gamma$ at $\lambda = \tfrac{1}{2}$,
$c = -1$) \emph{is} chirally Koszul:
the algebra is freely strongly generated, and
logarithmic phenomena appear in the module category,



thinking
**Evaluating circularity and references**

I need to think about the existence of actual circularity in my work. It seems like `bar-cobar-htt` might be referenced in the appendix, and I should check its connection to `quantum-complementarity-main`. I wonder if there are any direct navigation loops that could cause issues. I might need to search for theory references linked to appendix local labels, especially where there are only notation index stubs. Some labels are stubs, while others refer to real results. I need to analyze if any issues are severe enough.
thinking
**Inspecting appendix references**

I'm thinking about whether the label prefix for appendix sections is appropriate. For example, mentioning "Appendix 3.2" seems fine, especially if it's a section in `general_relations.tex`, which is a chapter. I wonder if using `\ref` prints the section number as A.4. I also need to look into `_sl2_yangian_insert` and its connection to the appendix theorem. There might be unresolved labels or even misnamed chapter labels. It appears that theory files incorrectly reference `nilpotent-completion` as an appendix, which seems like a serious issue.
thinking
**Inspecting document structure**

I need to verify whether the section called "nilpotent_completion" is actually included as an appendix or just labeled as one. The file path leads me to believe it's part of the theory, but the user's questions suggest I should look for discrepancies. I'll check the start of the main file for the include order and examine the references. It seems like there's some confusion between what's labeled as a chapter and what's labeled as an appendix.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/theory/nilpotent_completion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'nilpotent_completion|app:nilpotent-completion|chap:nilpotent-completion' main.tex chapters/theory/nilpotent_completion.tex chapters/theory/introduction.tex chapters/theory/existence_criteria.tex chapters/theory/algebraic_foundations.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/poincare_duality.tex chapters/theory/filtered_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\input\\{.*nilpotent_completion|\\\\include\\{.*nilpotent_completion|\\\\appendix' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\providecommand{\bk}{\mathbb{k}}
\chapter{Nilpotent-completion frontier for non-quadratic Koszul duality}
\label{app:nilpotent-completion}


The bar construction of Virasoro produces an infinite coalgebra.
Without completion, no dual algebra is accessible. This appendix
extends the finite-type geometric Koszul formalism to a larger class of
filtered chiral algebras under finite-generation and polynomial-growth
hypotheses, recording the $I$-adic framework, the finite-stage
infrastructure, and the exact missing lemmas that separate the standard
completed examples from a universal completion theorem.

\begin{remark}[Dependency warning]
\label{rem:nilpotent-completion-dependency}
The theorematic core of the monograph remains the finite-type
Koszul-locus theory of Chapters~\ref{chap:koszul-pairs}
and~\ref{chap:higher-genus}. The present appendix records the leading
extension of that core, not a replacement of it. Every result below
 succeeded in 51ms:
chapters/theory/filtered_curved.tex:131:Completion technology: Appendix~\ref{app:nilpotent-completion}.
chapters/theory/poincare_duality.tex:682:over the conilpotent filtration by bar degree (see Appendix~\ref{app:nilpotent-completion}), which organizes the bar complex by the number of collision points on~$\overline{C}_n(X)$.
chapters/theory/chiral_koszul_pairs.tex:4859:Appendix~\ref{app:nilpotent-completion}. The present chapter treats
chapters/theory/chiral_koszul_pairs.tex:4865:the extended hypotheses of Appendix~\ref{app:nilpotent-completion}.
chapters/theory/chiral_koszul_pairs.tex:5422:See Appendix~\ref{app:nilpotent-completion} for the completion
chapters/theory/existence_criteria.tex:14:Appendix~\ref{app:nilpotent-completion}, and the classical
chapters/theory/existence_criteria.tex:703: inverse-limit hypotheses; Appendix~\ref{app:nilpotent-completion}
chapters/theory/bar_cobar_adjunction_curved.tex:1514:See Appendix~\ref{app:nilpotent-completion},
chapters/theory/bar_cobar_adjunction_curved.tex:5980:(Appendix~\ref{app:nilpotent-completion}) inherits strict nilpotence.
chapters/theory/bar_cobar_adjunction_inversion.tex:70:(Appendix~\ref{app:nilpotent-completion}); and general algebras may
chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
chapters/theory/introduction.tex:2624: (Appendix~\ref{app:nilpotent-completion}).
main.tex:1559:\input{chapters/theory/nilpotent_completion}
main.tex:1626: \phantomsection\label{thm:resonance-filtered-bar-cobar}% % nilpotent_completion.tex (3 refs)
main.tex:1628: \phantomsection\label{thm:stabilized-completion-positive}% % nilpotent_completion.tex
main.tex:1642: \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
main.tex:1644: \phantomsection\label{sec:mc4-splitting}% % nilpotent_completion.tex
chapters/theory/algebraic_foundations.tex:2436: (Appendix~\ref{app:nilpotent-completion}).
chapters/theory/algebraic_foundations.tex:2499:(Appendix~\ref{app:nilpotent-completion});
 succeeded in 51ms:
1559:\input{chapters/theory/nilpotent_completion}
1585:\appendix

thinking
**Inspecting document structure**

I find it interesting that the main.tex file includes information about nilpotent completion right before the \appendix command. This seems to indicate a theory chapter that’s incorrectly labeled as an appendix, creating a significant seam inconsistency. The user mentioned a seam between appendices and theory chapters, and it looks like `chapters/theory/nilpotent_completion.tex` is being presented as an appendix. I need to carefully check the include order and look into any phantom section labels in the main.tex file, especially between lines 1550 and 1590.
exec
/bin/zsh -lc "sed -n '1548,1592p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
higher-spin geometry, entanglement, and the open problems toward which
the engine points.

\input{chapters/connections/frontier_modular_holography_platonic}
% omitted: chapters/connections/twisted_holography_quantum_gravity.tex
% thqg_open_closed_realization promoted to Part II (The Characteristic Datum)
\input{chapters/connections/entanglement_modular_koszul}
\input{chapters/connections/thqg_entanglement_programme}
\input{chapters/connections/holographic_codes_koszul}
\input{chapters/connections/semistrict_modular_higher_spin_w3}
% --- Promoted from appendices: substantial frontier chapters ---
\input{chapters/theory/nilpotent_completion}
\input{chapters/theory/coderived_models}
\input{chapters/connections/subregular_hook_frontier}
\input{chapters/connections/outlook}

% Master concordance: the trilingual dictionary connecting the seven-face
% programme across all three volumes. Placed after the constitution
% (concordance.tex) and after outlook.tex so that it serves as the final
% navigation index of Vol~I, pointing to the corresponding chapters in



thinking
**Identifying document fixes**

I see there's strong evidence indicating an issue with the nilpotent completion in the theory section. The text refers to something as an appendix, but it seems to belong in a chapter instead. To fix this accurately, I need to either move the content below the appendix command into the appendix section or relabel it completely. Since the comments suggest it's intentional to be a chapter, I'll go ahead and relabel everything from Appendix to Chapter, ensuring all references are updated accordingly.
thinking
**Clarifying document references**

I need to ensure I mention all affected references, even if they aren't exhaustive. The fix should state clearly to rename the label to `chap:nilpotent-completion`, replace every `Appendix\ref{app:nilpotent-completion}` with `Chapter\ref{chap:nilpotent-completion}`, and update the introductory text to say 'This chapter' instead. It makes sense to cite specific lines where these problems occur, like `chapters/theory/nilpotent_completion.tex:4` or `main.tex:1559/1585`. I’m considering whether to include both findings since they relate to the overall structure between appendices and theory.
thinking
**Updating references in documentation**

I’ve noticed a mislabeled appendix in the theory section that needs fixing, and I should rename the label and adjust the references. If I take care of this, it might automatically fix any inconsistencies across other references in the introduction and other sections using "Appendix." I’ll need to mention all the relevant downstream uses, even if formatting complicates things. Plus, I should check if any other sections like `coderived_models` need a similar review.
exec
/bin/zsh -lc "sed -n '1,24p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'app:coderived-models|Appendix~\\\\ref\\{app:coderived-models|Appendix~\\\\ref\\{sec:coderived-models|Chapter~\\\\ref\\{app:coderived-models' chapters/theory main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products
 succeeded in 51ms:
main.tex:1660: \phantomsection\label{app:coderived-models}% % planned appendix
chapters/theory/higher_genus_foundations.tex:293:see Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:407: $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:832: \textup{(}Appendix~\textup{\ref{app:coderived-models})}.
chapters/theory/chiral_koszul_pairs.tex:292:(Appendix~\ref{sec:coderived-models}),
chapters/theory/algebraic_foundations.tex:296:the coderived category (Appendix~\ref{sec:coderived-models});
chapters/theory/algebraic_foundations.tex:377:(Appendix~\ref{sec:coderived-models}).%

thinking
**Investigating section labels**

I’m looking at the `app:coderived` section label in my document, but it seems to reference `app:coderived-models` in the phantomsection of main.tex, which is planned for the appendix. I need to inspect main.tex around line 1660 to clear this up. I wonder if it'll be straightforward to fix, or if this leads to a bigger issue. Let's see what's going on!
exec
/bin/zsh -lc "sed -n '1654,1664p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \phantomsection\label{rem:pixton-genus2-computation}% % concordance.tex
 \phantomsection\label{rem:pixton-conjecture-status}% % concordance.tex
 \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
 \phantomsection\label{thm:sl2-genus2-curvature}% % genus_expansions.tex
 \phantomsection\label{thm:complementarity-root-datum}% % genus_expansions.tex
 \phantomsection\label{sec:conventions}% % higher_genus_foundations.tex forward ref
 \phantomsection\label{app:coderived-models}% % planned appendix
 \phantomsection\label{rem:three-models}% % Vol II remark
 % --- Archive-only chapter labels ---
 \phantomsection\label{ch:genus-expansions}% % genus_expansions.tex
 % removed: ch:derived-langlands phantom (now defined in derived_langlands.tex)

thinking
**Inspecting label issues**

It looks like there’s a problem with the label for the appendix in my main document. The phantom label `app:coderived-models` is referenced, but the actual file has a different label, `app:coderived`, and it’s just a section in the theory file. I’m wondering if that’s causing confusion when it references `Appendix\ref{app:coderived-models}`. I should check if `sec:coderived-models` exists in the document, as that might clarify things. Let's investigate!
exec
/bin/zsh -lc "rg -n 'label\\{sec:coderived-models\\}|label\\{app:coderived-models\\}|label\\{app:coderived\\}' chapters/theory/coderived_models.tex main.tex chapters/theory/algebraic_foundations.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1643: \phantomsection\label{app:coderived}% % coderived_models.tex
main.tex:1660: \phantomsection\label{app:coderived-models}% % planned appendix
main.tex:1865: \phantomsection\label{sec:coderived-models}%
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/coderived_models.tex:188:\label{sec:coderived-models}
exec
/bin/zsh -lc "sed -n '180,198p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\eqref{eq:co-contra-equivalence}.
\end{remark}

%%% =======================================================
%%% Relative curved models adequate for the present monograph
%%% =======================================================

\subsection{Relative curved models}
\label{sec:coderived-models}
\index{coderived category!relative models|textbf}

The full theory of coderived categories of factorization algebras
on $\operatorname{Ran}(X)$ is not yet available in the literature;
its development is part of the Stratum~II programme
(Remark~\ref{rem:two-strata}). Nevertheless, the off-Koszul
statements in this monograph (where the bar-cobar counit is
a curved equivalence rather than a quasi-isomorphism) require
a precise ambient homotopy category. This subsection defines the
\emph{minimal} relative homotopy theory needed to make those

thinking
**Inspecting theory references**

I'm noticing that coderived_models is actually a theory section that’s misplaced as an appendix in the references. That seems like an issue with the layout. I’ll need to check the references in the theory section where it's being used. I should look into the topics around algebraic foundations, higher genus foundations, and chiral Koszul pairs to make sure everything aligns correctly. Let's see what I find!
exec
/bin/zsh -lc "sed -n '286,304p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '284,300p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '368,384p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{Theorem layer:} For a chiral Koszul pair
 $(\mathcal{A}_1, \mathcal{A}_2)$, Theorem~A
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}) proves
 $\bar{B}^{\mathrm{ch}}(\mathcal{A}_1) \simeq \mathcal{A}_2^!$
 and $\Omega^{\mathrm{ch}}(\mathcal{A}_i^!) \simeq \mathcal{A}_i$
 as \emph{consequences} of the recognition data, not as definitions.
\end{enumerate}
Off the Koszul locus, the bar-cobar object persists only in
the completed coderived category
(Appendix~\ref{sec:coderived-models}).%

The correspondence between twisting morphisms and GLZ Maurer--Cartan
elements is Proposition~\ref{prop:comparison-our-glz}(iii).%

\subsection{Twisting morphisms: the fundamental object}
\label{subsec:twisting-morphisms-fundamental}
\index{twisting morphism|textbf}
 succeeded in 52ms:
$\bar{B}_X(\cA)$ and cobar $\Omega_X(\bar{B}_X(\cA))$ exist as
constructions. But the counit
$\Omega_X(\bar{B}_X(\cA)) \to \cA$ is a quasi-isomorphism
\emph{only when $\tau$ is a Koszul morphism}
(Theorem~\ref{thm:bar-cobar-inversion-qi}).
Off the Koszul locus, the bar-cobar object persists in the
provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
(Appendix~\ref{sec:coderived-models}),
not in the ordinary derived category.
This is the chiral/factorization analogue of the fundamental
theorem of twisting morphisms \cite[Theorem~2.3.1]{LV12}.
\end{remark}

The following lemmas make the mapping-cone identifications
explicit, as required for Theorem~\ref{thm:fundamental-twisting-morphisms}.

 succeeded in 52ms:
 $\barB_X(\cA) \otimes_\pi \cA^!$, formed with the universal
 twisting morphism~$\pi$
 \textup{(}Proposition~\textup{\ref{prop:universal-twisting-adjunction}(i)},
 Definition~\textup{\ref{def:twisted-tensor-product})}, is acyclic.
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
exec
/bin/zsh -lc "sed -n '288,304p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the \emph{derived category}. The curved differential $\dfib$
produces a curved dg coalgebra with $\dfib^{\,2} \neq 0$
(for $\kappa \neq 0$); the bar complex equipped with $\dfib$
lives in the \emph{coderived category}
$D^{\mathrm{co}}$~(Positselski;
see Appendix~\ref{app:coderived-models}).
The derived/coderived comparison, established on the manuscript's
flat-side comparison locus together with the coderived treatment of
the curved model, ensures that the flat model carries the ordinary
derived package while the curved model is its coderived counterpart.

\noindent
\textbf{Relation.}
The fiberwise differential $\dfib$ is curved; the quantum
corrections $\sum t_k d_k$ cancel the curvature via the
Lagrangian property of the $A$-cycle subspace, producing the
strict differential $\Dg{g} = \dzero + \sum t_k d_k$.

thinking
**Investigating misclassification issues**

I’ve discovered that the section on coderived_models is referred to as an appendix, possibly using phantom labels, which could cause issues with navigation and scope. This might indicate a high severity misclassification across the chapters. I need to inspect the labels in main.tex related to nilpotent_completion and coderived, checking for systemic misclassifications. It seems this drift is due to attempts to preserve old references after adjustments. I'll look for appendix references in theory files and try to systematically detect any problematic labels.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\label\\{app:' chapters/theory/*.tex chapters/theory/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/existence_criteria.tex:9:\label{app:existence-criteria}
chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
chapters/theory/spectral_sequences.tex:2:\label{app:spectral-sequences}
chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/existence_criteria.tex:9:\label{app:existence-criteria}
chapters/theory/spectral_sequences.tex:2:\label{app:spectral-sequences}

thinking
**Inspecting file structure**

Okay, I've realized that the existence_criteria and spectral_sequences theory files are both labeled with `app:`. I need to carefully check the main.tex for the inclusion order and references to see how everything is connected. This might take some digging, but it's essential to make sure everything is organized correctly. So, let’s dive in and search through those files!
exec
/bin/zsh -lc "sed -n '1,16p' chapters/theory/existence_criteria.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,16p' chapters/theory/spectral_sequences.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'app:existence-criteria|app:spectral-sequences|Appendix~\\\\ref\\{app:existence-criteria|Appendix~\\\\ref\\{app:spectral-sequences|Chapter~\\\\ref\\{app:existence-criteria|Chapter~\\\\ref\\{app:spectral-sequences' chapters/theory main.tex appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
%================================================================
% APPENDIX: EXISTENCE CRITERIA FOR KOSZUL DUALS
% The theorematic core lives in Chapters 2, 8, 9 and the
% concordance (Chapter 34). This appendix compares existence
% paradigms; it does not legislate a monograph-wide criterion.
%================================================================

\chapter{Comparison of existence paradigms for Koszul duals}
\label{app:existence-criteria}


For which chiral algebras does a Koszul dual exist? The strict
finite-type theory of the core monograph, the completion package of
Appendix~\ref{app:nilpotent-completion}, and the classical
existence/non-existence criteria in the literature each answer a
different version of this question.
 succeeded in 53ms:
\chapter{Spectral sequences}
\label{app:spectral-sequences}

\index{spectral sequence|textbf}

The bar complex carries three natural filtrations. Each isolates a different
structural invariant: the bar spectral sequence computes bar cohomology, the
Chevalley--Cousin spectral sequence relates D-module cohomology to configuration
space geometry, and the genus spectral sequence organizes quantum corrections by
loop order.

\section{Filtered complexes and spectral sequences}
\label{sec:filtered-complexes}

\begin{definition}[Filtered chain complex]
\label{def:filtered-complex}
 succeeded in 50ms:
appendices/koszul_reference.tex:242:See Proposition~\ref{prop:classification-table} in Appendix~\ref{app:existence-criteria} for the complete classification table of chiral algebras by Koszul type; see \S\ref{sec:filtered-vs-curved-comprehensive} for the underlying theory.
chapters/theory/spectral_sequences.tex:2:\label{app:spectral-sequences}
chapters/theory/existence_criteria.tex:9:\label{app:existence-criteria}
chapters/theory/algebraic_foundations.tex:2501:(Appendix~\ref{app:existence-criteria}).

thinking
**Clarifying document structure**

I'm noticing that the existence criteria and spectral sequences are listed as theory chapters, yet the app and text label them as appendices at the top. It's interesting! I need to check the main text to understand how these chapters are included in relation to the appendices. Let's search for the main inclusion order and see how everything lines up. I want to make sure I'm grasping the correct structure!
exec
/bin/zsh -lc "rg -n '\\\\input\\{chapters/theory/existence_criteria\\}|\\\\input\\{chapters/theory/spectral_sequences\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1601:\input{chapters/theory/spectral_sequences}
1602:\input{chapters/theory/existence_criteria}


thinking
**Evaluating chapter references**

I’m looking at the mislabeled theory chapters, wondering if references use the Appendix correctly. It seems only "algebraic_foundations" mentions "existence_criteria" and the "appendices/koszul_reference" as an appendix. The existence criteria file starts as an appendix, which feels inconsistent with the spectral_sequences. I’m curious if the prefix “app” is incorrect, especially since it doesn’t seem to have cross-references. A theory chapter labeled as an appendix could definitely cause confusion. I need to find solid evidence of this misunderstanding.
thinking
**Identifying label inconsistencies**

I need to make an exact fix by renaming `\label{app:spectral-sequences}` to `\label{chap:spectral-sequences}` and updating any references. I’m searching for any references to this label but haven’t found any yet. Still, there's an inconsistency that might warrant flagging—probably low to medium priority. I’ll check other labels in theory files that start with `app:`—I found four: coderived, existence_criteria, nilpotent_completion, and spectral_sequences. This could indicate that these sections are mislabeled as appendices, so I'll need to examine each file closely.
exec
/bin/zsh -lc "rg -n 'app:existence-criteria|app:spectral-sequences|app:coderived|app:nilpotent-completion' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1642: \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
1643: \phantomsection\label{app:coderived}% % coderived_models.tex
1660: \phantomsection\label{app:coderived-models}% % planned appendix
exec
/bin/zsh -lc "sed -n '2488,2506p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,20p' chapters/theory/existence_criteria.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,248p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\operatorname{KSpec}(\cA) := (c(\cA), \kappa(\cA),
\varrho(\cA))$. Additive under tensor products in $c$
and~$\kappa$.
\end{definition}

\begin{remark}[Existence regimes]\label{rem:existence-regimes}
\label{rem:existence-koszul}
Three regimes, not one universal theorem:
(i)~\emph{strict}, where $\bar{B}_X$ and inversion hold on the
Koszul locus;
(ii)~\emph{completed}, under inverse-limit hypotheses
(Appendix~\ref{app:nilpotent-completion});
(iii)~\emph{comparison}
(Appendix~\ref{app:existence-criteria}).
The essential distinction: $\bar{B}_X(\cA)$ may be constructed
beyond where $\Omega_X\bar{B}_X(\cA) \simeq \cA$ is proved.
\end{remark}

 succeeded in 52ms:
%================================================================
% APPENDIX: EXISTENCE CRITERIA FOR KOSZUL DUALS
% The theorematic core lives in Chapters 2, 8, 9 and the
% concordance (Chapter 34). This appendix compares existence
% paradigms; it does not legislate a monograph-wide criterion.
%================================================================

\chapter{Comparison of existence paradigms for Koszul duals}
\label{app:existence-criteria}


For which chiral algebras does a Koszul dual exist? The strict
finite-type theory of the core monograph, the completion package of
Appendix~\ref{app:nilpotent-completion}, and the classical
existence/non-existence criteria in the literature each answer a
different version of this question.

%================================================================
% SECTION 1: STATEMENT OF THE PROBLEM
%================================================================
 succeeded in 52ms:
This ensures that genus $g$ quantum corrections are modular-invariant.


\section{Classification of chiral algebras by Koszul type}
\label{app:koszul-classification}

See Proposition~\ref{prop:classification-table} in Appendix~\ref{app:existence-criteria} for the complete classification table of chiral algebras by Koszul type; see \S\ref{sec:filtered-vs-curved-comprehensive} for the underlying theory.

%================================================================
% SECTION: ESSENTIAL IMAGE CHARACTERIZATION
%================================================================

\section{\texorpdfstring{Essential image: when is $\widehat{\mathcal{C}} = \mathcal{A}^!$?}{Essential image: when is C = A !?}}

thinking
**Searching theory files**

I think I need to search through all the theory files for comments that start with “APPENDIX” or “This appendix” that are included before the appendices. This way, I can compile them into a list. To do this efficiently, I'm considering using a tool like `rg` (ripgrep) to quickly find those sections. It should streamline the process, and I’m curious to see what valuable insights I can extract from those comments!
exec
/bin/zsh -lc "rg -n 'This appendix|present appendix|The present appendix|APPENDIX:' chapters/theory/*.tex chapters/theory/**/*.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/existence_criteria.tex:2:% APPENDIX: EXISTENCE CRITERIA FOR KOSZUL DUALS
chapters/theory/existence_criteria.tex:4:% concordance (Chapter 34). This appendix compares existence
chapters/theory/nilpotent_completion.tex:8:Without completion, no dual algebra is accessible. This appendix
chapters/theory/nilpotent_completion.tex:19:and~\ref{chap:higher-genus}. The present appendix records the leading
chapters/theory/nilpotent_completion.tex:1277:This appendix should be read as a frontier package, not as a blanket
chapters/theory/coderived_models.tex:12:replacement. This appendix collects the definitions and key results
chapters/theory/existence_criteria.tex:2:% APPENDIX: EXISTENCE CRITERIA FOR KOSZUL DUALS
chapters/theory/existence_criteria.tex:4:% concordance (Chapter 34). This appendix compares existence
chapters/theory/nilpotent_completion.tex:8:Without completion, no dual algebra is accessible. This appendix
chapters/theory/nilpotent_completion.tex:19:and~\ref{chap:higher-genus}. The present appendix records the leading
chapters/theory/nilpotent_completion.tex:1277:This appendix should be read as a frontier package, not as a blanket
chapters/theory/spectral_sequences.tex:67:This appendix presents spectral sequences in the \emph{homological} convention (chain complexes, $d$ lowers total degree), so $d_r$ has bidegree $(-r, r-1)$. The main body of the text uses cohomological convention ($d$ raises degree), where the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ has bidegree $(r, -r+1)$. The two conventions are related by reindexing $E_r^{p,q} \leftrightarrow E_r^{-p,-q}$.
chapters/theory/spectral_sequences.tex:67:This appendix presents spectral sequences in the \emph{homological} convention (chain complexes, $d$ lowers total degree), so $d_r$ has bidegree $(-r, r-1)$. The main body of the text uses cohomological convention ($d$ raises degree), where the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ has bidegree $(r, -r+1)$. The two conventions are related by reindexing $E_r^{p,q} \leftrightarrow E_r^{-p,-q}$.
chapters/theory/coderived_models.tex:12:replacement. This appendix collects the definitions and key results

thinking
**Considering appendices and findings**

I'm noticing that there are four theory files described as appendices in spectral_sequences. The boundary between the main content and the appendices seems a bit blurred. I’m considering whether I should present one overall finding or focus on the four individual files. Grouping might simplify things, but if the user wants every inconsistency, separating them could be better. I’ll need to check line 67 in spectral_sequences and the surrounding lines for more details.
exec
/bin/zsh -lc "sed -n '60,72p' chapters/theory/spectral_sequences.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The differential $d_r: E_r^{p,q} \to E_r^{p-r, q+r-1}$ is induced by $d$:
\[
d_r([x]) := [dx] \in E_r^{p-r, q+r-1}
\]
for $[x] \in E_r^{p,q}$ represented by $x \in F_p C_{p+q}$ with $dx \in F_{p-r} C_{p+q-1}$.

\begin{remark}[Convention]
This appendix presents spectral sequences in the \emph{homological} convention (chain complexes, $d$ lowers total degree), so $d_r$ has bidegree $(-r, r-1)$. The main body of the text uses cohomological convention ($d$ raises degree), where the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ has bidegree $(r, -r+1)$. The two conventions are related by reindexing $E_r^{p,q} \leftrightarrow E_r^{-p,-q}$.
\end{remark}

\emph{Step~4.} There are canonical isomorphisms:
\[
H(E_r^{p,q}, d_r) \cong E_{r+1}^{p,q}.

thinking
**Checking for circular references**

I need to check the appendices that reference theory definitions to see if there are any circular dependencies. For instance, `appendices/arnold_relations` references `thm:bar-nilpotency-complete`, while the bar construction references `appendixref{app:arnold-relations}`. I’m considering whether this is circular; it might not be, since the bar construction theorem uses Arnold from literature, and the appendix provides extra proofs. However, I need to inspect around line 169 to verify this.
exec
/bin/zsh -lc "sed -n '156,176p' appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1252p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The Arnold relations can be verified systematically for each triple $\{i,j,k\} \subset \{1,\ldots,n\}$:
\begin{itemize}
\item $n=3$: $\binom{3}{3} = 1$ relation (verified above)
\item $n=4$: $\binom{4}{3} = 4$ relations (all follow from the $n=3$ case by restriction)
\item $n=5$: $\binom{5}{3} = 10$ relations (similarly)
\end{itemize}
\end{remark}

\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
The Arnold relations ensure $d^2 = 0$ for the geometric bar differential:
\[d^2 = \sum_{\text{cycles}} [\operatorname{Res}_{D_i}, \operatorname{Res}_{D_j}] = 0\]
because the residue commutators sum to zero by Arnold relations.
\begin{proof}
This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
\end{proof}
\end{corollary}

\subsection{Attribution}

Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
 succeeded in 52ms:

\item \emph{Position Function:} For $k \in S$, we denote by $|k|_S$ (or simply $|k|$ 
when $S$ is clear from context) the \emph{position} of $k$ in this ordering:
\[k = k_{|k|} \quad \iff \quad |k| = i \text{ where } k \text{ is the } i\text{-th smallest element of } S\]

\item \emph{Sign Convention:} Signs arising from reordering are computed via the 
Koszul rule. Moving an element $k$ past position $|k|$ introduces sign $(-1)^{|k|-1}$.

\item \emph{Multi-indices:} For multi-index sets (e.g., in partitions), we use 
lexicographic ordering.
\end{enumerate}

\emph{Example.} For $S = \{2, 5, 7\}$:
\begin{itemize}
\item $|2|_S = 1$ (first position)
\item $|5|_S = 2$ (second position) 
\item $|7|_S = 3$ (third position)
\end{itemize}

In Arnold relations, the notation $(-1)^{|k|}$ means $(-1)^{|k|_S}$ where $S$ is the 
exec
/bin/zsh -lc "sed -n '508,528p' appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The residue differential is a summand of the boundary operator $\partial$
(restricting to codimension-$1$ strata $D_S$ with $|S| = 2$, which
correspond to two-point collisions). The identity $\partial^2 = 0$
(Theorem~\ref{thm:config-boundary-relations}) implies that the
$d_{\mathrm{res}}^2$ terms cancel against the nested and disjoint
codimension-$2$ strata exactly as described above. The nine-term
cancellation of Theorem~\ref{thm:bar-nilpotency-complete} is recovered
as the special case $n = 3$, $S = \{i,j\}$, $S' = \{j,k\}$,
$S'' = \{k,i\}$.
\end{proof}

\begin{remark}[Relationship to the nine-term verification]
\label{rem:nine-term-global}
The nine-term cancellation in the proof of
Theorem~\ref{thm:bar-nilpotency-complete} is the local manifestation of
the global identity $\partial^2 = 0$. For $n = 3$ points, the
codimension-$2$ strata are triple collision loci $D_{ijk}$, and the three
codimension-$1$ divisors $D_{ij}$, $D_{jk}$, $D_{ki}$ meeting at $D_{ijk}$
produce exactly the nine terms (three squared terms and six cross terms) that

thinking
**Checking theorem references**

I'm working through some proofs, and I think I've got the relationships clear: appendix theorem proofs rely on the bar theorem, and the theory theorem uses the appendix as a supplementary proof. I'm wondering if there's a mismatch with theorem labels in the notation index, specifically with `def:arnold-relations`. I need to search to see if `thm:arnold-relations` exists in either `configuration_spaces.tex` or `bar_construction`. Let's dig in!
exec
/bin/zsh -lc "rg -n 'label\\{thm:arnold-relations\\}' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/configuration_spaces.tex:733:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-relations}
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\ref\\{app:nilpotent-completion|Chapter~\\\\ref\\{app:existence-criteria|Chapter~\\\\ref\\{app:coderived-models|Chapter~\\\\ref\\{app:coderived|Chapter~\\\\ref\\{app:spectral-sequences' appendices chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:nilpotent-completion|Appendix~\\\\ref\\{app:existence-criteria|Appendix~\\\\ref\\{app:coderived-models|Appendix~\\\\ref\\{app:coderived|Appendix~\\\\ref\\{app:spectral-sequences' appendices chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'This appendix|present appendix|This appendix presents' chapters/theory/existence_criteria.tex chapters/theory/nilpotent_completion.tex chapters/theory/coderived_models.tex chapters/theory/spectral_sequences.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
chapters/theory/spectral_sequences.tex:67:This appendix presents spectral sequences in the \emph{homological} convention (chain complexes, $d$ lowers total degree), so $d_r$ has bidegree $(-r, r-1)$. The main body of the text uses cohomological convention ($d$ raises degree), where the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ has bidegree $(r, -r+1)$. The two conventions are related by reindexing $E_r^{p,q} \leftrightarrow E_r^{-p,-q}$.
chapters/theory/coderived_models.tex:12:replacement. This appendix collects the definitions and key results
chapters/theory/nilpotent_completion.tex:8:Without completion, no dual algebra is accessible. This appendix
chapters/theory/nilpotent_completion.tex:19:and~\ref{chap:higher-genus}. The present appendix records the leading
chapters/theory/nilpotent_completion.tex:1277:This appendix should be read as a frontier package, not as a blanket
chapters/theory/existence_criteria.tex:4:% concordance (Chapter 34). This appendix compares existence
 succeeded in 52ms:
appendices/koszul_reference.tex:242:See Proposition~\ref{prop:classification-table} in Appendix~\ref{app:existence-criteria} for the complete classification table of chiral algebras by Koszul type; see \S\ref{sec:filtered-vs-curved-comprehensive} for the underlying theory.
chapters/theory/bar_cobar_adjunction_inversion.tex:70:(Appendix~\ref{app:nilpotent-completion}); and general algebras may
chapters/theory/bar_cobar_adjunction_curved.tex:1514:See Appendix~\ref{app:nilpotent-completion},
chapters/theory/bar_cobar_adjunction_curved.tex:5980:(Appendix~\ref{app:nilpotent-completion}) inherits strict nilpotence.
chapters/theory/introduction.tex:2624: (Appendix~\ref{app:nilpotent-completion}).
chapters/theory/poincare_duality.tex:682:over the conilpotent filtration by bar degree (see Appendix~\ref{app:nilpotent-completion}), which organizes the bar complex by the number of collision points on~$\overline{C}_n(X)$.
chapters/theory/filtered_curved.tex:131:Completion technology: Appendix~\ref{app:nilpotent-completion}.
chapters/theory/algebraic_foundations.tex:2436: (Appendix~\ref{app:nilpotent-completion}).
chapters/theory/algebraic_foundations.tex:2499:(Appendix~\ref{app:nilpotent-completion});
chapters/theory/algebraic_foundations.tex:2501:(Appendix~\ref{app:existence-criteria}).
chapters/theory/higher_genus_foundations.tex:293:see Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:407: $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
chapters/theory/chiral_koszul_pairs.tex:4859:Appendix~\ref{app:nilpotent-completion}. The present chapter treats
chapters/theory/chiral_koszul_pairs.tex:4865:the extended hypotheses of Appendix~\ref{app:nilpotent-completion}.
chapters/theory/chiral_koszul_pairs.tex:5422:See Appendix~\ref{app:nilpotent-completion} for the completion
chapters/theory/existence_criteria.tex:14:Appendix~\ref{app:nilpotent-completion}, and the classical
chapters/theory/existence_criteria.tex:703: inverse-limit hypotheses; Appendix~\ref{app:nilpotent-completion}
exec
/bin/zsh -lc "sed -n '286,298p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,18p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '400,412p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Rather, $\nabla^{\mathrm{GM}}$ is an independent geometric datum
 (the connection on the base $\overline{\cM}_g$), and the
 uncurving identity~\eqref{eq:chain-uncurving} expresses the
 interplay between fiber curvature and base flatness.
 The resulting flat complex $(\barB^{(g)}(\cA), \Dg{g})$ lives in
 the derived category; the curved complex
 $(\barB^{(g)}(\cA), \dfib)$ lives in the coderived category
 $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
 These categories are \emph{inequivalent} in general: the
 coderived category has strictly more objects (the coacyclic
 complexes are invisible to the derived category).
\end{enumerate}
\end{proposition}
 succeeded in 52ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

 succeeded in 52ms:
The strict differentials $\dzero$ and $\Dg{g}$ produce honest
chain complexes; the bar complex equipped with either lives in
the \emph{derived category}. The curved differential $\dfib$
produces a curved dg coalgebra with $\dfib^{\,2} \neq 0$
(for $\kappa \neq 0$); the bar complex equipped with $\dfib$
lives in the \emph{coderived category}
$D^{\mathrm{co}}$~(Positselski;
see Appendix~\ref{app:coderived-models}).
The derived/coderived comparison, established on the manuscript's
flat-side comparison locus together with the coderived treatment of
the curved model, ensures that the flat model carries the ordinary
derived package while the curved model is its coderived counterpart.



thinking
**Examining notation consistency**

I need to ensure that there's consistency in notation, especially regarding definitions and naming mismatches across different sections. For instance, references such as `bar_construction` seem to point to a notation index, which raises questions. Also, an appendix reference might label it correctly but could still lead to confusion, like calling appendices "Chapters." I'll need to verify if appendix theorems are properly cited and whether they are indeed proven or just conjectural. I might consider using a theorem registry for clarity.
thinking
**Searching for theorem references**

I need to investigate if any proven theorems in the theory reference an appendix conjecture as support, since that could be significant. I'll search for any blocks that connect the theory theorems to these appendix conjectures. I might want to look into the suspicious_proved_claim_dependencies.csv, although I'm not sure if that file is available. It could also be worth checking for generated files in the root directory. I'll need to list those out to see what I have.
codex
I’m now checking seam citations against claim status, not just label existence. The failure mode to kill here is a proved theory statement leaning on an appendix conjecture or frontier-only appendix theorem without importing that status.
exec
/bin/zsh -lc "rg -n '\\\\ClaimStatus(Conjectured|Conditional|Heuristic|Open)' appendices/nonlinear_modular_shadows.tex appendices/combinatorial_frontier.tex appendices/homotopy_transfer.tex appendices/koszul_reference.tex appendices/arnold_relations.tex appendices/signs_and_shifts.tex appendices/general_relations.tex appendices/branch_line_reductions.tex appendices/notation_index.tex appendices/computational_tables.tex appendices/theta_functions.tex appendices/spectral_higher_genus.tex appendices/dual_methodology.tex appendices/_sl2_yangian_insert.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "ruby -e '
labels={}
Dir[\"appendices/**/*.tex\"].each do |f|
  env=nil
  File.readlines(f, chomp:true).each_with_index do |line,i|
    if line =~ /\\\\begin\\{(theorem|proposition|lemma|corollary|remark|conjecture|definition|computation|verification|idea|observation)\\}/
      env="'$1
      status=line[/'"\\\\ClaimStatus([A-Za-z]+)/,1]
    end
    line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| labels[m[0]]=[f,i+1,env,status] }
    env=nil if line =~ /\\\\end\\{(theorem|proposition|lemma|corollary|remark|conjecture|definition|computation|verification|idea|observation)\\}/
  end
end
Dir[\"chapters/theory/**/*.tex\"].sort.each do |f|
  lines=File.readlines(f, chomp:true)
  lines.each_with_index do |line,i|
    line.scan(/\\\\(?:ref|eqref|autoref|Cref|cref|nameref)\\{(["'^}]+)'"\\}/){|m|
      lbl=m[0]
      next unless labels[lbl]
      def_file,def_line,env,status=labels[lbl]
      if status && status "'!~ /ProvedHere|ProvedElsewhere/
        puts [f,i+1,lbl,def_file,def_line,env,status,line.strip].join("'"\\t\")
      end
    }
  end
end
'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'ls -1 *.csv 2>/dev/null' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
appendices/spectral_higher_genus.tex:118:\begin{conjecture}[Superstring degeneration; \ClaimStatusConjectured]\label{conj:superstring-degeneration}
appendices/combinatorial_frontier.tex:469:\begin{conjecture}[\texorpdfstring{$\mathcal{W}_3$}{W3} bar cohomology generating function; \ClaimStatusConjectured]\label{conj:w3-bar-gf}
appendices/combinatorial_frontier.tex:940:\begin{conjecture}[Period-\texorpdfstring{$6$}{6} Pad\'e structure; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:1082:\begin{conjecture}[Critical-level emergence; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:1102:\begin{conjecture}[Critical self-duality as Maurer--Cartan; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2506:\begin{definition}[Modular chiral Feynman transform; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2547:\begin{conjecture}[Graph-completed Hamiltonian refinement; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2567:\begin{definition}[Complementarity Legendrian; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2730:\begin{conjecture}[Nonlinear phase of the standard families; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2755:\begin{definition}[Nonlinear spectral-branch stack; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2794:\begin{definition}[Polarized modular graph algebra; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2828:\begin{conjecture}[Polarized universal class; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2852:\begin{definition}[Resonance scattering diagram; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2873:\begin{definition}[Complementarity schober; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2891:\begin{definition}[Modular wavefunction; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2947:\begin{conjecture}[Quartic lift theorem; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2988:\begin{conjecture}[Resonance wall-crossing theorem; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2993:\begin{conjecture}[Quantization theorem; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:4387:\ClaimStatusConjectured
appendices/branch_line_reductions.tex:1183:\begin{conjecture}[Spectral shadow principle; \ClaimStatusConjectured]
 exited 1 in 51ms:
zsh:1: no matches found: *.csv
 succeeded in 378ms:
chapters/theory/higher_genus_modular_koszul.tex	34973	conj:w3-bar-gf	appendices/combinatorial_frontier.tex	469	conjecture	Conjectured	and~\ref{conj:w3-bar-gf}) is the first example where the
chapters/theory/higher_genus_modular_koszul.tex	35081	conj:w3-bar-gf	appendices/combinatorial_frontier.tex	469	conjecture	Conjectured	\textup{(}Conjecture~\textup{\ref{conj:w3-bar-gf}}).
chapters/theory/higher_genus_modular_koszul.tex	35097	conj:w3-bar-gf	appendices/combinatorial_frontier.tex	469	conjecture	Conjectured	and~\textup{\ref{conj:w3-bar-gf}}), but the shared

thinking
**Investigating conjecture references**

I’m noticing that there are only theoretical references to unproven appendix labels in higher_genus_modular_koszul, which makes me think they might be properly termed conjectures. I need to look into the context to make sure these terms aren't being misused. It's crucial to keep everything accurate and clear in these discussions, so I'll need to open lines of inquiry about this further.
exec
/bin/zsh -lc "sed -n '34960,35104p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:spectral-shadow-position}
\index{shadow tower!spectral level}
The lifted spectral cover sits at the $L_2$ level of the
characteristic hierarchy
(cf.~\S\ref{subsec:completion-kinematics-programme}): $L_1$ is the scalar
modular characteristic~$\kappa(\cA)$, while $L_2$ is the
spectral discriminant~$\Delta_\cA$ together with its module
structure. The defect calculus developed here provides the
geometric content of this level: the discriminant polynomial is
the visible shadow, but tensor transport, DS reduction, and
level-rank duality require the full lifted cover.
The $\widehat{\mathfrak{sl}}_3/\mathcal{W}_3$ orbit
(Conjectures~\ref{conj:sl3-bar-gf}
and~\ref{conj:w3-bar-gf}) is the first example where the
visible generating functions are both rational but the lifted
covers are nontrivially cubic: the algebra and its DS image
live on different sheets of a common $S_3$ cover, and the DS
functor is a sheet-crossing map.
\end{remark}



thinking
**Inspecting theorem references**

I’m looking through the conjecture references that are properly labeled. It seems I should use a theorem registry or grep to pinpoint theory refs to appendix labels marked Conditional or Conjectured. I found only three, which might not be in proved theorems.

I also want to check if there are appendix references within theory proofs that are just remarks or definitions. There could be potential confusion, particularly with details like the A∞ algebra in line 1147 referencing the appendix. Let's ensure everything is systematic and checks for circular dependencies.
thinking
**Inspecting circular references**

I can detect potential cycles at the file pair level and check if they’re truly circular. So far, it seems there aren’t direct circular references except for some notation and classification loops. However, I suspect there might be another loop between the appendices and theory references regarding criteria for existence. The theory mentions details that redirect to an appendix, which then refers back to the theory for more information. I should look closely around theory lines 460-480 to see if there's a direct missing statement.
exec
/bin/zsh -lc "sed -n '462,478p' chapters/theory/existence_criteria.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,246p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This ensures that genus $g$ quantum corrections are modular-invariant.


\section{Classification of chiral algebras by Koszul type}
\label{app:koszul-classification}

See Proposition~\ref{prop:classification-table} in Appendix~\ref{app:existence-criteria} for the complete classification table of chiral algebras by Koszul type; see \S\ref{sec:filtered-vs-curved-comprehensive} for the underlying theory.

%================================================================
% SECTION: ESSENTIAL IMAGE CHARACTERIZATION
%================================================================
 succeeded in 51ms:
\textbf{Chiral Algebra} & \textbf{Quadratic?} & \textbf{Has Dual?} & \textbf{Comments} \\
\hline
Heisenberg $\mathcal{H}$ & Yes & Yes & Primitive coalgebra \\
\hline
$\widehat{\mathfrak{g}}_k$ (Kac--Moody) & Yes & Yes (generic $k$) & See Prop.~\ref{prop:kac-moody-koszul-duals} \\
\hline
Virasoro $\text{Vir}$ & No & Yes (completion) & $I$-adic completion \\
\hline
$\mathcal{W}_3$ & No & Yes (all $c$, completed) & Strict Koszul at $c = -2$ only \\
\hline
$\mathcal{W}_N$ ($N < \infty$) & No & Sometimes & Depends on $(N, c)$ \\
\hline
$\mathcal{W}_{1+\infty}$ & No & Yes (completed) & Filtered; see Appendix~\ref{app:koszul-reference} \\
\hline
$\mathcal{W}_\infty$ & No & Yes (completion) & Weight stabilization; no strict finite-stage dual \\
\hline
Free fermion ($bc$ ghosts) & Yes & Yes & Exterior coalgebra \\

thinking
**Addressing navigation issues**

I'm noticing a circular navigation loop, which seems to be a seam issue. The fix could involve making the table row self-contained or providing an explicit classification statement in the appendix instead of redirecting. I think the exact fix might be to replace a reference in the theorem file. I need to check the appendix for the relevant theorem ‘essential-image-koszul’, probably around line 268, and search through lines 260-280 for more context.
exec
/bin/zsh -lc "sed -n '260,284p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{question}

\begin{remark}\label{rem:why-essential-image-matters}
The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
\end{remark}

\subsection{Main characterization theorem}

\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:

\begin{enumerate}
\item \emph{Conilpotency.} $\widehat{\mathcal{C}}$ is conilpotent: every element of $\ker(\epsilon)$ is annihilated by a sufficiently high iterate of the reduced coproduct $\bar{\Delta}$:
 \[\ker(\epsilon) = \bigcup_{n \geq 0} \ker(\bar{\Delta}^{(n)})\]
 
\item \emph{Connected.} The counit is surjective onto the ground field:
 \[\epsilon: \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}\]
 
\item \emph{Geometric representability.} $\widehat{\mathcal{C}}$ admits a presentation as sections of a $\mathcal{D}_X$-module coalgebra on the Ran space of~$X$; equivalently, there exists a factorization coalgebra~$\mathcal{F}$ such that $\widehat{\mathcal{C}} \simeq \Gamma(\mathrm{Ran}(X),\, \mathcal{F})$, compatible with the operadic structure of the Fulton--MacPherson compactification

thinking
**Exploring source lines in theories**

I'm considering using a script to check cross-directory references in my theory and the appendix. It's important to find if a source line is situated inside a theorem, proposition, lemma, corollary, definition, or remark, along with its status. This could help me identify any potentially problematic theorems or proved statements. It's a methodical approach, but let’s be careful to ensure everything is accurate.
exec
/bin/zsh -lc "ruby -e '
# load appendix labels
appendix_labels={}
Dir[\"appendices/**/*.tex\"].each do |f|
  File.readlines(f, chomp:true).each_with_index do |line,i|
    line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| appendix_labels[m[0]]=[f,i+1] }
  end
end
Dir[\"chapters/theory/**/*.tex\"].sort.each do |f|
  env=nil; status=nil; envline=nil; envlabel=nil
  File.readlines(f, chomp:true).each_with_index do |line,i|
    if line =~ /\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|conjecture|computation|verification|idea|observation)\\}/
      env="'$1; envline=i+1; status=line[/'"\\\\ClaimStatus([A-Za-z]+)/,1]
    end
    if env
      line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| envlabel ||= m[0] }
      line.scan(/\\\\(?:ref|eqref|autoref|Cref|cref|nameref)\\{(["'^}]+)'"\\}/){|m|
        lbl=m[0]
        next unless appendix_labels[lbl]
        af,al=appendix_labels[lbl]
        puts [f,i+1,env,envline,(envlabel||\"\"),status.to_s,lbl,af,al,line.strip].join(\"\\t\")
      }
    end
    if line =~ /\\\\end\\{(theorem|proposition|lemma|corollary|remark|definition|conjecture|computation|verification|idea|observation)\\}/
      env=nil; status=nil; envline=nil; envlabel=nil
    end
  end
end
' | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 104ms:
chapters/theory/algebraic_foundations.tex	116	definition	102	def:quadratic-algebra		def:bar-complex-algebraic	appendices/notation_index.tex	342	The bar construction (Definition~\ref{def:bar-complex-algebraic})
chapters/theory/algebraic_foundations.tex	2465	remark	2423	rem:three-koszul-mechanisms		rem:three-bar-variants	appendices/ordered_associative_chiral_kd.tex	687	(Remark~\ref{rem:three-bar-variants}).
chapters/theory/bar_cobar_adjunction_curved.tex	109	remark	99	rem:bar-ordered-primacy		ch:ordered-associative-chiral-kd	appendices/ordered_associative_chiral_kd.tex	37	Chapter~\ref{ch:ordered-associative-chiral-kd}, the cofree
chapters/theory/bar_cobar_adjunction_curved.tex	164	remark	99	rem:bar-ordered-primacy		ch:ordered-associative-chiral-kd	appendices/ordered_associative_chiral_kd.tex	37	Chapter~\ref{ch:ordered-associative-chiral-kd}, and the passage
chapters/theory/bar_cobar_adjunction_inversion.tex	1876	remark	1858	rem:bar-cobar-inversion-alt-formality		thm:htt	appendices/homotopy_transfer.tex	69	\textup{(}Theorem~\textup{\ref{thm:htt}}\textup{)} supplies maps
chapters/theory/bar_cobar_adjunction_inversion.tex	3506	remark	3486	rem:identify-koszul-wild		thm:essential-image-koszul	appendices/koszul_reference.tex	268	(Theorem~\ref{thm:essential-image-koszul}):
chapters/theory/bar_construction.tex	965	remark	962	rem:sign-bridge		ver:d2-degree3	appendices/signs_and_shifts.tex	607	graded associative algebra), see Verification~\ref{ver:d2-degree3} and
chapters/theory/bar_construction.tex	966	remark	962	rem:sign-bridge		prop:master-sign	appendices/signs_and_shifts.tex	576	Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
chapters/theory/bar_construction.tex	966	remark	962	rem:sign-bridge		app:signs	appendices/signs_and_shifts.tex	2	Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
chapters/theory/chiral_hochschild_koszul.tex	2463	definition	2422	def:graph-amplitude		app:signs	appendices/signs_and_shifts.tex	2	(Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}).
chapters/theory/chiral_hochschild_koszul.tex	2463	definition	2422	def:graph-amplitude		app:sign-conventions	appendices/signs_and_shifts.tex	713	(Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}).
chapters/theory/chiral_hochschild_koszul.tex	5740	remark	5737	rem:nonlinear-shadow-pointer		app:nonlinear-modular-shadows	appendices/nonlinear_modular_shadows.tex	2	in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/theory/chiral_hochschild_koszul.tex	5752	remark	5750	rem:branch-line-pointer		app:branch-line-reductions	appendices/branch_line_reductions.tex	2	Appendix~\ref{app:branch-line-reductions} extracts exact
chapters/theory/chiral_hochschild_koszul.tex	5784	remark	5762	rem:categorical-logarithm-jets		app:branch-line-reductions	appendices/branch_line_reductions.tex	2	(Appendix~\ref{app:branch-line-reductions}) are the spectral
chapters/theory/chiral_koszul_pairs.tex	1116	remark	1113	rem:ce-vs-exterior		app:combinatorial-frontier	appendices/combinatorial_frontier.tex	2	Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
chapters/theory/chiral_koszul_pairs.tex	3508	remark	3475	rem:koszulness-vs-shadow-depth		thm:nms-archetype-trichotomy	appendices/nonlinear_modular_shadows.tex	1208	(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
chapters/theory/chiral_modules.tex	2665	remark	2662			app:homotopy-transfer	appendices/homotopy_transfer.tex	2	(Appendix~\ref{app:homotopy-transfer}; see
chapters/theory/chiral_modules.tex	2882	computation	2872	comp:bgg-sl2-pipeline		thm:sl2-koszul-dual	appendices/_sl2_yangian_insert.tex	533	(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
chapters/theory/chiral_modules.tex	2954	computation	2872	comp:bgg-sl2-pipeline		thm:sl2-koszul-dual	appendices/_sl2_yangian_insert.tex	533	(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
chapters/theory/chiral_modules.tex	2975	computation	2872	comp:bgg-sl2-pipeline		thm:sl2-koszul-dual	appendices/_sl2_yangian_insert.tex	533	Theorem~\ref{thm:sl2-koszul-dual},


thinking
**Analyzing sources for theorem validity**

I’m checking some theorems and propositions that reference appendices. The ones marked with ProvedHere are crucial because they might rely on sources in the appendices. I need to examine if there are any circular references or foundational issues. 

For example, the algebraic_foundations definition relies on the notation index, which seems problematic. Also, the existence_criteria proposition points to an appendix, creating a potential proof loop, while other theorems seem fine.
thinking
**Examining theorem dependencies**

I need to check if the appendix theorem relies back on the main theory or just on general HTT, which might be fine. Theorem `thm:htt` could be acceptable as it supports the primary context without circularity. Also, I should verify if the appendix `homotopy_transfer` has been proved elsewhere and if it's utilized correctly in the main theory. 

There’s a potential issue in the higher_genus_modular_koszul corollary `cor:shadow-extraction`, which references Appendix `nonlinear_modular_shadows` without pinpointing a specific result, so I’ll need to dig deeper into the context for clarity.
exec
/bin/zsh -lc "sed -n '4290,4318p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
In both regimes, $\Theta_\cA$ \emph{exists} by the
bar-intrinsic construction.
\end{remark}

\begin{corollary}[Shadow extraction; \ClaimStatusProvedHere]
\label{cor:shadow-extraction}
\index{shadow extraction|textbf}
\index{universal Maurer--Cartan class!shadow extraction}
The bar-intrinsic MC element $\Theta_\cA$ of
Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
projections recovering all named modular invariants:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Scalar shadow:}
 $\pi_{\mathrm{sc}}(\Theta_\cA)
 = \sum_{g \geq 1} \kappa(\cA)\,\lambda_g$
 \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
\item \emph{Spectral shadow:}
 $\pi_{\mathrm{br}}(\Theta_\cA) = T_{\mathrm{br},\cA}$,
 so $\Delta_\cA(x) = \det(1 - x\, T_{\mathrm{br},\cA})$
 whenever the spectral branch object exists

thinking
**Clarifying definition references**

I'm noticing that the corollary references an appendix generically instead of specifying a precise definition label. Since the quartic resonance class might have a specific definition labeled as `def:nms-modular-quartic-resonance-class` at appendix line 1734, I feel it's too vague to cite the entire appendix. I need to replace that generic citation with the exact definition reference. I should verify the exact label and meaning by looking around line 1734 to confirm.
exec
/bin/zsh -lc "sed -n '1728,1742p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\in \Gamma\bigl(\overline{\mathcal M}_{g,n}\times B_{\cA}^{\circ},
\mathscr L_{4,g,n}^{\mathrm{res}}(\cA)\bigr).
\end{equation}
\end{construction}

\begin{definition}[Modular quartic resonance class]
\label{def:nms-modular-quartic-resonance-class}
The \emph{modular quartic resonance class} of $\cA$ in genus $(g,n)$ is the Cartier divisor class
\begin{equation}
\label{eq:nms-modular-resonance-class}
\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
:=
\operatorname{div}\bigl(s_{4,g,n}^{\mathrm{res}}(\cA)\bigr)
\in
\operatorname{Pic}\bigl(\overline{\mathcal M}_{g,n}\times B_{\cA}^{\circ}\bigr).
exec
/bin/zsh -lc "sed -n '1572,1590p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
\label{thm:chain-vs-homology}
Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Chain level.}
 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
 all operations are computable via configuration space integrals,
 and homotopies have geometric meaning as forms on
 $\overline{C}_n(X)$.
\item \emph{Homology level.}
 The homotopy transfer theorem
 (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
 $A_\infty$ structure $\{m_k^H\}$ on $H^*(\mathcal{A})$ with
 $m_1^H = 0$. The product $m_2^H$ descends to homology
 (it is strictly associative if $\mathcal{A}$ is formal).
 However, the transferred higher operations
 $m_k^H$ for $k \geq 3$ are in general \emph{non-trivial}:
 they are the Massey products, encoding obstructions to formality.
\item \emph{What is lost.}


thinking
**Assessing citation clarity**

I'm looking at a theorem that cites a generic appendix, which somewhat confuses things. I wonder if I should reference `Theorem\ref{thm:htt}` or `Theorem\ref{thm:chiral-htt}`. The term "The homotopy transfer theorem" makes me lean toward `Theorem\ref{thm:htt}`, but the generic appendix feels vague. This could create citation accuracy issues. I should systematically list references from the output where certain conditions apply. We might have multiple generic appendix references to clarify.
thinking
**Evaluating citation adequacy**

It seems referencing sections might still be fine. For example, the `chiral_hochschild_koszul` definition appears okay with the generic appendix. The `high_genus_modular_koszul` definitions might not be an issue with their remarks. I should probably concentrate on the proved environments. A few citations need more attention: like `algebraic_foundations`, `existence_criteria`, and others linked to generic appendices. Also, I can inspect the `higher_genus_modular_koszul corollary` better since an exact fix seems clearer there.
exec
/bin/zsh -lc "sed -n '170,220p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '448,470p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '66,92p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


\section{Applications to chiral algebras}
\label{sec:htt-chiral}


\begin{theorem}[Chiral homotopy transfer; \ClaimStatusProvedHere]
\label{thm:chiral-htt}
\index{$A_\infty$-structure!transferred}
Let $\cA$ be an $\Eone$-chiral algebra on a curve $X$ and suppose we have an 
SDR of the underlying D-module:
\[
(\cA, H, p, \iota, h) \quad \text{with } H = H^{\mathrm{ch}}_*(\cA).
\]
Then:
\begin{enumerate}[label=(\roman*)]
\item $H$ inherits an $\Ainf$-chiral algebra structure.
\item The higher operations $\{m_n^{\mathrm{ch}}\}_{n \geq 3}$ are ``Massey products'' 
for the chiral structure.
\item If $\cA$ is Koszul, then $m_n^{\mathrm{ch}} = 0$ for $n \geq 3$.
 succeeded in 51ms:
(ii) The Comparison Theorem for projective resolutions provides the maps; 
standard homological algebra constructs the homotopy.
\end{proof}


\section{Explicit formulas for transferred structures}
\label{sec:transfer-formulas}

\begin{construction}[Transferred \texorpdfstring{$\Ainf$}{A-infinity}-structure]
\label{constr:transfer-ainf}
Let $(A, \{m_n\})$ be an $\Ainf$-algebra and $(A, H, p, \iota, h)$ an SDR to 
the homology $H = H_*(A)$. The transferred $\Ainf$-structure $\{\tilde{m}_n\}$ 
on $H$ is given by:

\emph{$\tilde{m}_1 = 0$.} The differential on homology vanishes.

\emph{$\tilde{m}_2$.} The induced product:
\[
\tilde{m}_2(a, b) = p \, m_2(\iota(a), \iota(b)).
\]
 succeeded in 51ms:
\label{sec:htt}

\begin{theorem}[Homotopy transfer theorem \cite{LV12, Kadeishvili80}; \ClaimStatusProvedElsewhere]
\label{thm:htt}
Let $(V, d_V)$ and $(W, d_W)$ be chain complexes with:
\begin{enumerate}[label=(\roman*)]
\item A chain map $p: V \to W$ (projection).
\item A chain map $\iota: W \to V$ (inclusion).
\item A chain homotopy $h: V \to V[-1]$ satisfying $\id_V - \iota p = d_V h + h d_V$.
\item The \emph{side conditions} (compatibility of $h$ with $p, \iota$): $p \iota = \id_W$, $h \iota = 0$, $p h = 0$, $h^2 = 0$.
\end{enumerate}
Such data is called a \emph{strong deformation retract} (SDR).

If $V$ carries a $\cP_\infty$-algebra structure (for $\cP$ a Koszul operad), 
then $W$ inherits a $\cP_\infty$-algebra structure such that $p$ and $\iota$ 
extend to $\infty$-quasi-isomorphisms of $\cP_\infty$-algebras.
\end{theorem}

\begin{proof}
The transferred structure on $W$ is constructed via the \emph{tensor trick}
exec
/bin/zsh -lc "sed -n '292,310p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16872,16932p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The identification of the genus-$0$ shadow obstruction tower with the
$L_\infty$ formality obstruction tower is structural:
the homological perturbation lemma (HPL) produces a
transferred $L_\infty$-algebra on any retract, and the
transferred brackets $\ell_r^{\mathrm{tr}}$ always exist.
The genuinely new content of
Proposition~\ref{prop:shadow-linfty-obstruction} is the
\emph{termination} phenomenon: the transferred $L_\infty$-algebra
terminates at degree $r_{\max}(\cA)$, meaning
$\ell_r^{\mathrm{tr}} = 0$ for all $r > r_{\max}$. This
is a consequence of the shadow obstruction tower analysis
(Theorem~\ref{thm:shadow-archetype-classification}),
not the HPL itself. The HPL is agnostic about termination;
it produces infinitely many brackets in general. What
forces termination is the specific structure of the modular
convolution algebra: the vanishing of obstruction classes
$o^{(r+1)}(\cA)$ in
$H^2(F^{r+1}\gAmod/F^{r+2}\gAmod, d_2)$
for $r > r_{\max}$, which reflects the OPE complexity of~$\cA$.
 succeeded in 52ms:
\begin{theorem}[Shadow archetype classification]
\label{thm:shadow-archetype-classification}
\ClaimStatusProvedHere
\index{shadow depth!classification theorem|textbf}
\index{shadow archetype classification|textbf}
Every chirally Koszul algebra in the standard landscape has algebraic
shadow depth
\[
 d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
\]
Equivalently, it belongs to exactly one of the shadow depth classes
$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
The class is determined by the vanishing pattern of obstruction
classes at degrees~$3$, $4$, $5$, and the assignments for the
primitive archetypes are as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Gaussian \textup{(}$\mathbf{G}$,
$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.

thinking
**Evaluating file revisions**

I need to identify an exact fix, similar to what’s done for nilpotents, relabeling to "chapter" and updating references. There’s a significant finding at `chapters/theory/existence_criteria.tex:9` and potential comments in line 2. The labels in the app and intro mention the appendix; I’ll consider including those. It looks like there might be a systemic issue across multiple files, so I may need to search for `\label{app:` in theory files not included after \appendix.
exec
/bin/zsh -lc "sed -n '824,836p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\item \emph{Homotopical \textup{(}bar-cobar inversion in
 $D^{\mathrm{co}}$\textup{)}.}\;
 If $\cA$ has finite-dimensional weight spaces
 \textup{(}the positive-energy axiom\textup{)}, then the
 genus-$g$ bar-cobar adjunction
 $\barBch_g \dashv \Omegach_g$ extends to an equivalence
 in the coderived category $D^{\mathrm{co}}$
 \textup{(}Appendix~\textup{\ref{app:coderived-models})}.
 The positive-energy condition ensures the weight-by-weight
 SDR exists and the homotopy transfer theorem produces the
 transferred curved $A_\infty$ structure on the coderived
 bar object; on the strict flat comparison model
codex
I’ve found a deeper seam defect than misworded prose: some theory chapters carry appendix labels, and `main.tex` adds duplicate phantom appendix labels on top of them. That creates unstable or outright wrong hyperlink targets, not just bad wording.
exec
/bin/zsh -lc "rg -n '\\\\label\\{app:nilpotent-completion\\}|\\\\label\\{app:coderived\\}|\\\\label\\{app:coderived-models\\}' main.tex chapters/theory/nilpotent_completion.tex chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^'"\\\\label\\{app:' chapters/theory | sed -n '1,50p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
main.tex:1642: \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
main.tex:1643: \phantomsection\label{app:coderived}% % coderived_models.tex
main.tex:1660: \phantomsection\label{app:coderived-models}% % planned appendix
chapters/theory/coderived_models.tex:3:\label{app:coderived}
 succeeded in 51ms:
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/existence_criteria.tex:9:\label{app:existence-criteria}
chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
chapters/theory/spectral_sequences.tex:2:\label{app:spectral-sequences}
exec
/bin/zsh -lc "ruby -e '
counts=Hash.new{|h,k| h[k]=[]}
Dir[\"main.tex\",\"chapters/theory/**/*.tex\",\"appendices/**/*.tex\"].each do |f|
  File.readlines(f, chomp:true).each_with_index do |line,i|
    line.scan(/\\\\label\\{(["'^}]+)'"\\}/){|m| counts[m[0]] << [f,i+1] }
  end
end
counts.select{|k,v| v.size>1 && k =~ /app:(nilpotent-completion|coderived|coderived-models)/}.each do |k,v|
  puts k
  v.each{|f,l| puts \"  #{f}:#{l}\"}
end
'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
app:nilpotent-completion
  main.tex:1642
  chapters/theory/nilpotent_completion.tex:4
app:coderived
  main.tex:1643
  chapters/theory/coderived_models.tex:3
exec
/bin/zsh -lc "rg -n 'W_\\{1\\+\\\\infty\\}|W_\\{1\\+infty\\}|\\\\mathcal\\{W\\}_\\{1\\+\\\\infty\\}|W_\\infty|essential image' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:W_\{1\+\\infty\}|W_\{1\+infty\}|\\mathcal\{W\}_\{1\+\\infty\}|W_\infty|essential image)
                                                                       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'essential image|W_\\infty|1\\+\\\\infty|1\\+infty|\\\\mathcal\\{W\\}_\\{1\\+\\\\infty\\}' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:essential image|W_\infty|1\+\\infty|1\+infty|\\mathcal\{W\}_\{1\+\\infty\})
                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'essential image' appendices/koszul_reference.tex && rg -n -F '\\mathcal{W}_{1+\\infty}' appendices/koszul_reference.tex && rg -n -F '\\mathcal{W}_\\infty' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
8:tables and the essential image characterization; the core definitions
259:Equivalently: what is the \emph{essential image} of the Koszul duality functor?
263:The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).


thinking
**Revising Theorem References**

I’m thinking no direct mention of W_{1+∞} is needed, so the theorem can remain generic. It might be better not to point to the appendix if it doesn't address W_{1+∞} specifically. For clarity, I could add a remark in the appendix and cite it from the table. Since the user wants a direct fix, I’ll replace the pointer with a concise summary. I also need to check if any theories refer to the appendix beyond just the corollary.
thinking
**Searching Appendix References**

I need to check for generic references in the appendix linked to the "higher_genus_foundations theorem 1191" and its relevant sections. It seems acceptable since it cites a section. There's also a definition in line 1147 that refers to the appendix generically, which seems fine without a specific theorem label. However, I’m concerned about the `bar_cobar_adjunction_curved` remark in multiple spots, especially since it points to a label in the appendix that may also exist in the theory file. I’ll search to clarify this.
exec
/bin/zsh -lc "rg -n 'label\\{ch:ordered-associative-chiral-kd\\}' appendices/ordered_associative_chiral_kd.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:37:\label{ch:ordered-associative-chiral-kd}
chapters/theory/ordered_associative_chiral_kd.tex:37:\label{ch:ordered-associative-chiral-kd}

thinking
**Identifying duplicate labels**

I’ve noticed there’s a duplicate label across the appendix and the theory files, which might be causing a mix-up. The cross-reference mapping seems to favor the appendix, possibly due to the last label. This is a significant issue! I need to check if both files contain the same label; it’s likely in the appendix file under "ordered_associative_chiral_kd.tex" after \appendix. I'll also look at the theory version for confirmation by searching main.tex.
exec
/bin/zsh -lc "rg -n '\\\\input\\{appendices/ordered_associative_chiral_kd\\}|\\\\input\\{chapters/theory/ordered_associative_chiral_kd\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1156:\input{chapters/theory/ordered_associative_chiral_kd}


thinking
**Checking document directories**

I’m examining the theory file included, but I’m wondering if the appendix duplicate was left out. And I think there could be a labeling issue across the repository; that might not address the documentation problem if the appendix file isn't present. I need to verify whether the appendices directory includes it or if it’s just missing from the main documents. I guess I should continue searching to clarify this!
thinking
**Inspecting appendix files**

I need to check the main appendices to identify which files are currently active. I'm thinking specifically about general_relations, arnold_relations, signs_and_shifts, theta_functions, spectral_higher_genus, and koszul_reference — perhaps there are more relevant files after line 1592? It seems important to review the complete include block for all appendices. Let's clarify this to ensure I have an accurate understanding of what I need to work with!
exec
/bin/zsh -lc "sed -n '1585,1620p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\appendix

\input{appendices/general_relations}
\input{appendices/arnold_relations}
\input{appendices/signs_and_shifts}
\input{appendices/theta_functions}
\input{appendices/spectral_higher_genus}
\input{appendices/koszul_reference}
\ifannalsedition\else
 \input{appendices/dual_methodology}
\fi
\input{appendices/notation_index}
\ifannalsedition\else
 \input{appendices/computational_tables}
\fi
% --- Moved from Part IV (EXEC-17): self-identified appendices ---
\input{chapters/theory/spectral_sequences}
\input{chapters/theory/existence_criteria}

% ======================================================================

thinking
**Evaluating build modes**

I'm focusing on the duplicates only appearing when "annalsedition" is true. I need to clarify if the build mode needs to be determined, though it might not be necessary. The source has a duplicate label inside a conditional, which could lead to issues if "annalsedition" is true. It's a potential problem due to inconsistency. If the condition is false in a full build, the duplicate label won’t be present. I need to check if `\ifannalsedition` is indeed true, so I should look at the top main.
exec
/bin/zsh -lc "rg -n 'annalsedition(true|false)|newif\\\\ifannalsedition|\\\\annalsedition' main.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
138:% Set \annalseditiontrue for the public Annals of Mathematics Studies build
140:% Set \annalseditionfalse for the full archive build (everything visible).
141:\newif\ifannalsedition
142:\annalseditiontrue
145: \annalseditionfalse
exec
/bin/zsh -lc "sed -n '136,148p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

% ---- Annals / Archive edition switch ----
% Set \annalseditiontrue for the public Annals of Mathematics Studies build
% (suppresses claim-status tags, quarantines frontier material).
% Set \annalseditionfalse for the full archive build (everything visible).
\newif\ifannalsedition
\annalseditiontrue
% Override: make archive passes \def\archivebuild{1} to enable full content.
\ifdefined\archivebuild
 \annalseditionfalse
\fi

% Claim provenance tags used in theorem-like headers.
exec
/bin/zsh -lc "sed -n '1528,1588p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% Genus-1 extension of the seven-face programme. The collision residue
% on E_tau produces elliptic objects: KZB connection, Belavin r-matrix,
% elliptic Gaudin Hamiltonians, and genuinely new higher-order elliptic
% operators for class M (Virasoro, W_N).
\input{chapters/connections/genus1_seven_faces}

% ======================================================================
% PART VI: THE FRONTIER (archive-only)
%
% Conditional, open: modular holography, higher-spin geometry,
% entanglement, completion, and the open problems toward which the
% engine points.
% ======================================================================
\part{The Frontier}
\label{part:v1-frontier}

\noindent
Parts~\ref{part:bar-complex}--\ref{part:seven-faces} develop the proved core, its standard computations, its
bridges to adjacent programmes, and the centrepiece collision-residue
identification. Part~\ref{part:v1-frontier} enters the frontier: modular holography,
exec
/bin/zsh -lc "rg -n '"'^'"\\\\ifannalsedition|"'^'"\\\\else|"'^'"\\\\fi' main.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
146:\fi
150:\ifannalsedition
157:\else
164:\fi
594:\fi
849:\ifannalsedition
851:\fi
962:\ifannalsedition\else
964:\fi
1365:\ifannalsedition\else
1372:\fi
1411:\ifannalsedition
1448:\else
1452:\fi
1454:\ifannalsedition\else
1472:\fi
1507:\ifannalsedition\else
1570:\fi
1593:\ifannalsedition\else
1595:\fi
exec
/bin/zsh -lc "sed -n '1590,1618p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\input{appendices/theta_functions}
\input{appendices/spectral_higher_genus}
\input{appendices/koszul_reference}
\ifannalsedition\else
 \input{appendices/dual_methodology}
\fi
\input{appendices/notation_index}
\ifannalsedition\else
 \input{appendices/computational_tables}
\fi
% --- Moved from Part IV (EXEC-17): self-identified appendices ---
\input{chapters/theory/spectral_sequences}
\input{chapters/theory/existence_criteria}

% ======================================================================
% ANNALS-EDITION PHANTOM LABELS
%
% Labels defined in archive-only content (Part VI outlook, concordance,
% editorial constitution, nilpotent completion appendix, landscape census,
% genus_complete) that are referenced from annals-included chapters.

thinking
**Exploring label referencing issues**

It seems like `\phantomsection` might not step the counter, so the current label just sticks to whatever was last set by `\chapter`. At line 1642 in main.tex, after including the existence criteria chapter in the appendix, `\@currentlabel` probably holds onto the last appendix chapter letter, like J. This could lead to `\ref{app:nilpotent-completion}` displaying that same letter instead of a new one, which could be incorrect. I'll need to check if `\phantomsection\label{...}` without `\refstepcounter` actually reuses the previous label.
codex
I need one more verification pass on the phantom-label seam. Rather than rely on TeX folklore, I’m checking the generated `.aux` data directly to see what those archive-only labels currently resolve to.
exec
/bin/zsh -lc "rg -n 'app:nilpotent-completion|app:coderived-models|app:coderived' -g '*.aux' ." in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "find . -name '*.aux' | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 2.10s:
./standalone/survey_modular_koszul_duality_v2.aux
./standalone/genus1_seven_faces.aux
./standalone/programme_summary_sections9_14.aux
./standalone/garland_lepowsky.aux
./standalone/riccati.aux
./standalone/N4_mc4_completion.aux
./standalone/drinfeld_kohno_bridge.aux
./standalone/introduction_full_survey.aux
./standalone/survey_modular_koszul_duality.aux
./standalone/w3_holographic_datum.aux
./standalone/bp_self_duality.aux
./standalone/N2_mc3_all_types.aux
./standalone/editorial.aux
./standalone/three_dimensional_quantum_gravity.aux
./standalone/ordered_chiral_homology.aux
./standalone/gaudin_from_collision.aux
./standalone/N6_shadow_formality.aux
./standalone/analytic_sewing.aux
./standalone/computations.aux
./standalone/en_chiral_operadic_circle.aux



thinking
**Considering fix options**

I’m thinking about a better solution for the archive and annals build. For the archive, since nilpotent_completion is a frontier chapter, I should rename the label to `chap:nilpotent-completion` and change all related content references to “Chapter.” For the annals build, since the frontier chapter isn’t included, it makes sense to either replace the bare appendix-style label with a clear note or remove those references from the visible chapters. Let’s focus on implementing these changes!
thinking
**Assessing appendix issues**

I'm considering moving `coderived_models` into the appendix if it's necessary for the annals. However, comments indicate it's not a reference point. I need to take a closer look at `\ifannalsedition` in part VI and the appendices. It's concerning that the annals build omits the nilpotent_completion/coderived_models, leaving references that lead to missing content. I see two possible fixes: either include a short appendix or refactor the references. Given the user's focus on the seam between appendices and theory, I need to determine the best approach.
thinking
**Determining chapter references**

I see that we need to adjust based on the main comments suggesting these sections are now substantial frontier chapters. This means I should stop referring to them as appendices in the live content. Since the annals build omits them, I should replace the cross-references in the core with non-linking archive-only notes or inline summaries. The user is looking for findings with an exact fix, which might not be easily implementable in one simple change. I need to clarify this.
exec
/bin/zsh -lc "rg -n '\\\\input\\{appendices/(homotopy_transfer|branch_line_reductions|nonlinear_modular_shadows|combinatorial_frontier|_sl2_yangian_insert|ordered_associative_chiral_kd)\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1010:\input{appendices/homotopy_transfer}
1109:\input{appendices/nonlinear_modular_shadows}
1113:\input{appendices/branch_line_reductions}
1371: \input{appendices/combinatorial_frontier}

thinking
**Inspecting document context**

I realize that the sections I'm looking for might not be under the appendix as I initially thought. I should inspect the main body instead, probably around sections 1000, 1100, and maybe 1365. It’s a bit tedious, but I want to make sure I cover all my bases and find the relevant information in the right spots. Let’s see what I can uncover!
exec
/bin/zsh -lc "sed -n '996,1016p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1100,1118p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1364,1374p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% --------------------------------------------------
% Chapter 7: Bar-Cobar Adjunction and Curved Koszul Duality
% Curved structures, I-adic completion, coalgebra homological algebra,
% bar-cobar inversion (Theorem A), Ran-space perspective, categorical logarithm.
% --------------------------------------------------
% Stub dispatcher removed from live build; compile the substantive chapter files directly.
% \include{chapters/theory/bar_cobar_adjunction}
\clearpage
\input{chapters/theory/bar_cobar_adjunction_curved}
\input{chapters/theory/bar_cobar_adjunction_inversion}
\clearpage

% Homotopy Transfer Theorem: the mechanical heart of A∞ structure production.
% Promoted from Appendix to Part I: this is foundational, not supplementary.
\input{appendices/homotopy_transfer}

% Bar-Cobar Inversion: the quasi-isomorphism theorem, spectral sequence
% construction, E_2 collapse, functoriality, derived equivalence.
% Phase 0 canonicalization: merged into bar_cobar_construction; preserved at
% archive/legacy/bar_cobar_quasi_isomorphism_legacy.tex.
 succeeded in 51ms:
$\kappa \to \Delta \to \mathfrak{C} \to \mathfrak{Q} \to \cdots$,
each level a constructive finite-order invariant with obstruction
classes in the cyclic deformation complex; the branch-line reductions
that extract structural theorems from finite-dimensional quotients;
and the computational methods that verify every formula by at least
three independent paths. The all-degree limit is the universal
Maurer--Cartan element~$\Theta_\cA$, proved by the bar-intrinsic
construction (Theorem~\ref{thm:mc2-bar-intrinsic}).

\input{appendices/nonlinear_modular_shadows}

% Branch-line reductions: genus-2 transparency, universal genus-3 constant,
% spectral cumulant hierarchy. The computational heart of Ring 2.
\input{appendices/branch_line_reductions}

% Computational methods: three-way verification of shadow obstruction towers,
% bar cohomology, genus-2 free energies, DS-transferred towers,
% explicit MC elements, N=2 SCA, and the decisive E_8 test.
\input{chapters/theory/computational_methods}
 succeeded in 51ms:

\ifannalsedition\else
 % --- Archive-only: extended example families and census ---
 % omitted: chapters/examples/toroidal_elliptic.tex (moved to Vol III)
 \input{chapters/examples/genus_expansions}
 \input{chapters/examples/bar_complex_tables}
 \input{chapters/examples/landscape_census}
 \input{appendices/combinatorial_frontier}
\fi

% ======================================================================


thinking
**Identifying appendix references**

I realize that there are important files like homotopy_transfer, nonlinear_modular_shadows, branch_line_reductions, and combinatorial_frontier that have been mistakenly labeled as being in the appendix when they should be part of the main body. I need to identify these misreferences and their actual positions. It seems I should check all file inputs before the specified line 1585 to confirm their locations. I might consider using a script to automate this comparison. It’s crucial to ensure everything is properly aligned in the final document!
thinking
**Inspecting appendix references**

I’ve realized that calling it an Appendix is incorrect, especially in regards to `app:homotopy-transfer`. This seems to be a significant issue that’s widespread. I need to search for all occurrences in the theory and identify how prevalent this mislabeling is. It might be helpful to focus on systemic findings for each promoted file. I plan to check the file headers and labels to ensure everything is accurately represented. I really want to get this right!
codex
The seam is broader than I first thought: several files still live under `appendices/`, but `main.tex` promotes them into the main body before `\appendix`. Any body text that still calls those files “Appendix” is materially wrong, because the build places them in Part I or the main theory lane.
exec
/bin/zsh -lc "sed -n '1,20p' appendices/combinatorial_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,20p' appendices/branch_line_reductions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,20p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,20p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\chapter{Homotopy transfer}
\label{app:homotopy-transfer}

\index{homotopy transfer theorem|textbf}

The homotopy
transfer theorem is the mechanism by which classical Koszul duality
acquires quantum corrections. Passing from a chain complex to its
cohomology via a deformation retract necessarily introduces higher
operations $m_k$ for $k \geq 3$; these are precisely the genus-$0$
quantum corrections of the bar complex
(Theorem~\ref{thm:bar-ainfty-complete}).

\begin{proposition}[Homotopy transfer as rectification mechanism]
\label{prop:htt-rectification}
\ClaimStatusProvedHere
The homotopy transfer theorem is the technical engine of the
rectification meta-theorem
(Theorem~\ref{thm:rectification-meta}): given a deformation retract
$V \xrightarrow{p} H \xrightarrow{i} V$ with $pi = \mathrm{id}$
 succeeded in 51ms:
\chapter[Branch-line reductions and primitive modular characteristics]{Branch-line reductions, primitive modular characteristics, and the intrinsic invariant ladder}
\label{app:branch-line-reductions}

The full modular Maurer--Cartan element $\Theta_\cA$ lives in an
infinite-dimensional convolution algebra. A \emph{branch-line
reduction} restricts~$\Theta_\cA$ to a configuration of minimal
complexity (two-point branch lines, rank-one spectral sectors,
genus-$2$ transparency windows) and proves structural theorems
inside the resulting finite-dimensional quotient.

The \emph{primitive modular characteristics} are the irreducible
components of~$\Theta_\cA$ under the clutching maps of
$\overline{\mathcal{M}}_{g,n}$: they are to the shadow obstruction
tower what primitive elements are to a Hopf algebra. The intrinsic
invariant ladder
\[
\kappa(\cA)
\rightsquigarrow
\Delta_{\cA}(x)
\rightsquigarrow
 succeeded in 51ms:
\chapter[Combinatorial frontier]{The combinatorial frontier of chiral bar cohomology}
\label{app:combinatorial-frontier}

Combinatorics in this monograph is not incidental decoration on an
algebraic core; it is constitutive. The dimensions
$\dim H^n(\barBgeom(\cA))$ are integers, and integers have structure:
generating functions, recurrences, growth rates, OEIS identities.
The bar-cobar machine converts algebraic input (OPE data, relation
spaces, conformal weights) into integer sequences, and those sequences
carry information about the algebra that no single theorem statement
can capture. When $\dim(\mathrm{Vir}^!)_n$ grows as $3^n/n^{3/2}$
while $\dim(\beta\gamma^!)_n$ grows as $3^n/n^{1/2}$, the shared
base and differing exponent encode the fact that these algebras share
a spectral discriminant but differ in the multiplicity structure of
their Koszul duals.

The counting problem has a further layer: one wants to count not only
bar cohomology dimensions but coherent packages (shadow-compatible
families of invariants), primitive modular characteristics (the
irreducible pieces of the completed Maurer--Cartan element), and
 succeeded in 50ms:
\chapter[Ambient complementarity and nonlinear modular shadows]{Ambient complementarity, nonlinear modular shadows, and the quartic resonance class}
\label{app:nonlinear-modular-shadows}

The modular characteristic $\kappa(\cA)$ (Theorem~D) and the spectral
discriminant~$\Delta_{\cA}$ are the linear face of a single ambient
deformation problem. The ambient problem carries a $(-1)$-shifted
symplectic form, and the two dual packages $\mathcal{Q}_g(\cA)$
and~$\mathcal{Q}_g(\cA^{!})$ are complementary Lagrangians inside it.
Their interaction produces an infinite nonlinear tower
\[
\kappa \;\longrightarrow\; \Delta \;\longrightarrow\;
\mathfrak{C} \;\longrightarrow\; \mathfrak{Q}
\;\longrightarrow\; \Theta,
\]
the \emph{shadow obstruction tower}: the sequence of finite-order
projections $\Theta_\cA^{\leq r}$ of the universal MC element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
is MC because $D_\cA^2 = 0$; all-degree convergence
$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ by
exec
/bin/zsh -lc "rg -n 'label\\{app:combinatorial-frontier\\}|app:combinatorial-frontier' main.tex appendices/combinatorial_frontier.tex chapters/theory/introduction.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1873: \phantomsection\label{app:combinatorial-frontier}%
appendices/combinatorial_frontier.tex:2:\label{app:combinatorial-frontier}
chapters/theory/introduction.tex:2251:Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
chapters/theory/chiral_koszul_pairs.tex:1116:Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
exec
/bin/zsh -lc "sed -n '1868,1876p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \phantomsection\label{prop:transport-propagation}%
 \phantomsection\label{prop:hook-ghost-constant}%
 \phantomsection\label{cor:bgg-koszul-involution}%
 \phantomsection\label{cor:virasoro-mode-removal}%
 \phantomsection\label{prop:bar-bgg-sl2}%
 \phantomsection\label{app:combinatorial-frontier}%
 \phantomsection\label{app:w3-jacobi-full}%
 \phantomsection\label{def:infty-operad}%
 % --- Frontier / THQG chapter labels ---
exec
/bin/zsh -lc "rg -n 'app:nonlinear-modular-shadows|app:branch-line-reductions|app:homotopy-transfer|app:combinatorial-frontier' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1873: \phantomsection\label{app:combinatorial-frontier}%

thinking
**Evaluating document structure**

I'm looking at the structure for nonlinear_modular_shadows, which includes both a Chapter and an Appendix. The branch_line seems like it's more suited for the Appendix. I think the combinatorial content could fit as either an Appendix or potentially a Chapter. It could be helpful if I just search for simpler terms to clarify this structure better. Let’s figure out the best way to organize these sections!
exec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:homotopy-transfer|Chapter~\\\\ref\\{app:homotopy-transfer|Ch\\.?~\\\\ref\\{app:homotopy-transfer' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/combinatorial_frontier.tex:334:\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:525:full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
chapters/theory/chiral_modules.tex:2665:(Appendix~\ref{app:homotopy-transfer}; see
chapters/theory/higher_genus_foundations.tex:1583: (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
chapters/theory/chiral_hochschild_koszul.tex:2901:Appendix~\ref{app:homotopy-transfer}, the transferred higher
chapters/theory/chiral_hochschild_koszul.tex:2933:complete filtered dg~Lie algebras (Appendix~\ref{app:homotopy-transfer}).
exec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:nonlinear-modular-shadows|Chapter~\\\\ref\\{app:nonlinear-modular-shadows|Ch\\.?~\\\\ref\\{app:nonlinear-modular-shadows' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:branch-line-reductions|Chapter~\\\\ref\\{app:branch-line-reductions|Ch\\.?~\\\\ref\\{app:branch-line-reductions' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:combinatorial-frontier|Chapter~\\\\ref\\{app:combinatorial-frontier|Ch\\.?~\\\\ref\\{app:combinatorial-frontier' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:4848:(Appendix~\ref{app:nonlinear-modular-shadows});
chapters/theory/higher_genus_modular_koszul.tex:10138:Appendix~\ref{app:nonlinear-modular-shadows} at each finite
chapters/theory/higher_genus_modular_koszul.tex:12290: (Appendix~\ref{app:nonlinear-modular-shadows}).
chapters/theory/higher_genus_modular_koszul.tex:12329: Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:13220:and Appendix~\ref{app:nonlinear-modular-shadows}
chapters/theory/higher_genus_modular_koszul.tex:15463:Appendix~\ref{app:nonlinear-modular-shadows}:
chapters/theory/higher_genus_modular_koszul.tex:15477:Appendix~\ref{app:nonlinear-modular-shadows} enumerates
chapters/theory/higher_genus_modular_koszul.tex:29759:(Appendix~\ref{app:nonlinear-modular-shadows}) is
chapters/theory/higher_genus_modular_koszul.tex:31102:and Appendix~\ref{app:nonlinear-modular-shadows}) is the
chapters/theory/chiral_hochschild_koszul.tex:5740:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/theory/introduction.tex:1952:(Chapter~\ref{app:nonlinear-modular-shadows}).
chapters/theory/introduction.tex:2224:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2377: (Ch.~\ref{app:nonlinear-modular-shadows}).
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1116:Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:5752:Appendix~\ref{app:branch-line-reductions} extracts exact
chapters/theory/chiral_hochschild_koszul.tex:5784:(Appendix~\ref{app:branch-line-reductions}) are the spectral
chapters/theory/introduction.tex:1954:(Appendix~\ref{app:branch-line-reductions}) extract exact







thinking
**Considering label prefixes**

I'm observing that there might be a low issue regarding whether to use "label prefix/app" or "chapter." It seems many theory lines are incorrectly using "Appendix." I wonder if I should clarify this distinction to avoid confusion. The nuances in the terminology could definitely impact the user's understanding. Getting it right matters, so I'm focused on ensuring my explanation is clear and accurate. Let's explore this distinction further!
thinking
**Addressing file inconsistencies**

I'm focusing on updating the references in the file, particularly distinguishing between “Chapter” and “Appendix.” It looks like the term "Appendix" is misused in many places where it should refer to a chapter instead. Since the file is promoted, I'll cite the body lines where these errors occur instead of just the label. I think it makes sense to mention one representative location in the appendices for clarity, while also ensuring the label is corrected for consistency throughout the document.
thinking
**Identifying potential label issues**

I’ve noticed a problem with the citation for `cor:shadow-extraction` on line 4315, which uses a generic appendix reference instead of the exact label, especially since the file is promoted. There’s also a similar issue with `higher_genus_foundations theorem 1583`. Other potential concerns include a circular pointer for `prop:classification-table` and issues with the `notation_index` definitions. Additionally, `coderived_models` has a phantom label, which might be critical. Plus, an archive-only chapter is misclassified as an appendix. I need to inspect specific lines in the theory referencing it for further clarity.
thinking
**Clarifying reference issues**

I’ve realized that since the file is a main-body chapter, the references to "Chapter" are correct, so I don’t have an issue there. Earlier, I mistakenly thought the references to "Appendix" were wrong, but it turns out that the "Chapter" references are the ones that should stay. I need to search for lines like `Appendixref{app:nonlinear-modular-shadows}` to ensure they’re corrected since the file is a chapter, so those shouldn't reference "Appendix" at all.
thinking
**Evaluating labeling issues**

I'm figuring out the issue around the phantom label in the annals build. It seems like there's a problem because the main text includes references that the annals build omits. I see that the introduction still references it, which is curious! I might want to inspect if both the introduction and chiral_koszul_pairs are included, as that could provide clarity. The situation with nilpotent completion also seems to mirror this, and it looks like it's an intentional workaround regarding archive-only content!
thinking
**Identifying gaps in the theory**

I see a gap in core theory related to omitted archive-only material. I could either integrate the essential statement into the included chapters or maintain a condensed appendix stub. The user asked about the connection between appendices and theory, emphasizing that no circular dependencies should exist. It's crucial to cross-reference the omitted material since it impacts the manuscript's integrity. For coderived models and other aspects, I recognize that the absence of this material creates significant issues that need prioritizing based on severity.
thinking
**Verifying findings in the manuscript**

I need to pinpoint 8-12 exact findings, specifically verifying line numbers and contexts for nilpotent references. Searching those lines could be sufficient. For the core theorem, I might not need to cite each reference explicitly; instead, I can cite the defining issue file line. 

The strongest findings include a critical one at `main.tex:1660`, relating to `coderived_models.tex:188`. The issue is that the theory references a phantom appendix, misclassifying it as an appendix while indicating a section which contains the actual content.
codex
I found at least one notation drift candidate on the nonlinear-shadow seam: the theory corollary names the quartic projection with a plain `R`, while the appendix definition appears to use `\mathfrak R`. I’m checking whether that is a genuine mismatch or just font variation declared elsewhere.
exec
/bin/zsh -lc "rg -n 'R\\"'^'"\\{\\\\mathrm\\{mod\\}\\}_\\{4|\\\\mathfrak R_\\{4,|quartic resonance class' chapters/theory/higher_genus_modular_koszul.tex appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:1:\chapter[Ambient complementarity and nonlinear modular shadows]{Ambient complementarity, nonlinear modular shadows, and the quartic resonance class}
appendices/nonlinear_modular_shadows.tex:229:\item At degree~$4$: the quartic resonance class
appendices/nonlinear_modular_shadows.tex:1015:the open/closed quartic resonance class
appendices/nonlinear_modular_shadows.tex:1127:The open/closed quartic resonance class reduces to the tree correction:
appendices/nonlinear_modular_shadows.tex:1652:\section{From Gram determinants to a modular quartic resonance class}
appendices/nonlinear_modular_shadows.tex:1733:\begin{definition}[Modular quartic resonance class]
appendices/nonlinear_modular_shadows.tex:1735:The \emph{modular quartic resonance class} of $\cA$ in genus $(g,n)$ is the Cartier divisor class
appendices/nonlinear_modular_shadows.tex:1738:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1822:\begin{theorem}[Clutching law for the modular quartic resonance class; \ClaimStatusProvedHere]
appendices/nonlinear_modular_shadows.tex:1827:\xi^*\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1829:p_1^*\mathfrak R_{4,g_1,n_1+1}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1831:p_2^*\mathfrak R_{4,g_2,n_2+1}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1835:In words: the boundary restriction of the quartic resonance class is the sum of the two contact resonance classes from the components together with a new tree correction generated by the cubic shadow.
appendices/nonlinear_modular_shadows.tex:1902:The clutching law \eqref{eq:nms-resonance-clutching-law} for the modular quartic resonance class is exactly the degree-$4$ contact-plus-tree shadow of that identity.
appendices/nonlinear_modular_shadows.tex:1911:The modular quartic resonance class behaves as follows in the model families.
appendices/nonlinear_modular_shadows.tex:1915:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\mathcal H)=0,
appendices/nonlinear_modular_shadows.tex:1921:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\widehat{\mathfrak{sl}}_{2,k})=0,
appendices/nonlinear_modular_shadows.tex:1930:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\beta\gamma)
appendices/nonlinear_modular_shadows.tex:1941:\begin{remark}[Why the quartic resonance class is new]
appendices/nonlinear_modular_shadows.tex:1943:The scalar characteristic $\kappa(\cA)$ and the spectral characteristic $\Delta_{\cA}$ detect linear and spectral information. The class $\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)$ is different in kind. It records the failure of the contact quartic sector to remain nondegenerate, and its boundary correction is quadratic in the cubic shadow. It is therefore the first genuinely nonlinear Picard-valued characteristic of the theory.
exec
/bin/zsh -lc "sed -n '4302,4318p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\item \emph{Scalar shadow:}
 $\pi_{\mathrm{sc}}(\Theta_\cA)
 = \sum_{g \geq 1} \kappa(\cA)\,\lambda_g$
 \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
\item \emph{Spectral shadow:}
 $\pi_{\mathrm{br}}(\Theta_\cA) = T_{\mathrm{br},\cA}$,
 so $\Delta_\cA(x) = \det(1 - x\, T_{\mathrm{br},\cA})$
 whenever the spectral branch object exists
 \textup{(}Theorem~\textup{\ref{thm:spectral-characteristic}}\textup{)}.
\item \emph{Quartic shadow:}
 $\pi_4(\Theta_\cA)
 = R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)$
 \textup{(}the quartic resonance class of
 Appendix~\textup{\ref{app:nonlinear-modular-shadows}}\textup{)}.
\item \emph{Higher shadows:}
 $\pi_r(\Theta_\cA)
 = \operatorname{Sh}_r(\cA)
exec
/bin/zsh -lc "sed -n '1730,1746p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{equation}
\end{construction}

\begin{definition}[Modular quartic resonance class]
\label{def:nms-modular-quartic-resonance-class}
The \emph{modular quartic resonance class} of $\cA$ in genus $(g,n)$ is the Cartier divisor class
\begin{equation}
\label{eq:nms-modular-resonance-class}
\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
:=
\operatorname{div}\bigl(s_{4,g,n}^{\mathrm{res}}(\cA)\bigr)
\in
\operatorname{Pic}\bigl(\overline{\mathcal M}_{g,n}\times B_{\cA}^{\circ}\bigr).
\end{equation}
\end{definition}

\begin{proposition}[Basis independence and specialization; \ClaimStatusProvedHere]

thinking
**Searching for notation patterns**

Okay, it seems there’s a possible notation mismatch with `R^{mod}_{4}`. I want to search if this notation has been used elsewhere, maybe even look for macro synonyms. It seems like there could be an `R` without the `\mathfrak R` involved. So, let's investigate this to clarify and ensure I'm accurate in my understanding. I’ll look into relevant resources for better context!
exec
/bin/zsh -lc "rg -n 'R\\"'^'"\\{\\\\mathrm\\{mod\\}\\}_\\{4|\\\\mathfrak R_\\{4' chapters/theory/higher_genus_modular_koszul.tex appendices/nonlinear_modular_shadows.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:1738:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1827:\xi^*\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1829:p_1^*\mathfrak R_{4,g_1,n_1+1}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1831:p_2^*\mathfrak R_{4,g_2,n_2+1}^{\mathrm{mod}}(\cA)
appendices/nonlinear_modular_shadows.tex:1915:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\mathcal H)=0,
appendices/nonlinear_modular_shadows.tex:1921:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\widehat{\mathfrak{sl}}_{2,k})=0,
appendices/nonlinear_modular_shadows.tex:1930:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\beta\gamma)
appendices/nonlinear_modular_shadows.tex:1943:The scalar characteristic $\kappa(\cA)$ and the spectral characteristic $\Delta_{\cA}$ detect linear and spectral information. The class $\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)$ is different in kind. It records the failure of the contact quartic sector to remain nondegenerate, and its boundary correction is quadratic in the cubic shadow. It is therefore the first genuinely nonlinear Picard-valued characteristic of the theory.
appendices/nonlinear_modular_shadows.tex:1959:\mathfrak R_{4,\bullet}^{\mathrm{mod}}(\cA),\;
appendices/nonlinear_modular_shadows.tex:2479:\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA),
chapters/theory/higher_genus_modular_koszul.tex:4313: = R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)$
exec
/bin/zsh -lc "rg -n '\\\\input\\{appendices/_sl2_yangian_insert\\}|\\\\input\\{appendices/ordered_associative_chiral_kd\\}' main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:










thinking
**Considering explicit replacements**

I need to propose a clear fix. For "nilpotent," the solution could be to replace the cross-reference with a simple archive note. Since the user wants a precise solution, that's important to mention. The same might apply for "coderived_models." The annals build omits it, but the core propositions reference it. Including a condensed appendix could clarify things, but since these references are explanatory, plain text might suffice. The task involves determining whether to add a definition in the core chapter instead. Which route should I take?
thinking
**Evaluating appendix pointers**

I’m considering an update to say: “Replace the dangling appendix pointer with an in-text parenthetical referencing the relative coderived category \(D^{\mathrm{co}}\) in the archive build.” But if the annals build doesn’t include that section, it won’t work well. A better option might be to suggest replacing it with an inline definition of the relative coderived category \(D^{co}_{prov}(X)\) defined below. However, I wonder if higher_genus_foundations could also use \(D^{co}\) and define it locally.
thinking
**Identifying necessary corrections**

I need to clarify something about line 293 in the text. It seems it involves a remark or proposition rather than a theorem, which is good to note. However, I should mention that there are three occurrences that need to be addressed. It’s really important to make sure all parts are accurate and clear. Checking for all instances will help in ensuring everything aligns perfectly!
thinking
**Formatting severity reports**

The user wants the format to be `[SEVERITY] file:line — PROBLEM: ... FIX: ...` and prefers a plain `file:line` style instead of markdown links. I can mention multiple file:lines in the FIX text as necessary, and using monospace might be helpful. The bullet might look like `- [CRITICAL] main.tex:1660 — PROBLEM: ... FIX: ...`. I’ll also make sure to include `Checked: N | Findings: N | Verdict: FAIL`, so I’ll count findings accurately and summarize clearly. It looks like there are 9 findings and 33 files checked.
thinking
**Setting findings summary**

I think I need to present a summary format like `Checked: 33 | Findings: 9 | Verdict: FAIL`. That seems clear enough! It's important that each finding is grounded in the exact read lines. For the coderived finding, I can specifically cite `main.tex:1660` to ensure clarity. I want to be precise and make sure everything aligns with what the user requested to keep it organized and understandable. Let's make this report accessible!
thinking
**Making precise corrections**

I need to provide precise fixes for various mathematical references. For the algebraic foundations, the exact change is to replace `Definition\ref{def:bar-complex-algebraic}` with `Theorem\ref{thm:bar-coalgebra}` in a specific formula. I've decided the better fix is to clarify how the bar construction is rooted in the augmentation ideal. For the higher-genus modular Koszul, replace `R^{...}` with `\mathfrak R^{...}`. For branch line, renaming the label to `chap:branch-line-reductions` seems like a solid update. I need to ensure I’m thorough with my recommendations!
thinking
**Evaluating findings organization**

I'm considering whether to integrate the homotopy_transfer into one finding instead of keeping it separate. The line uses a section label as an appendix, and I think including all updates could streamline things. The user asked for every inconsistency, so if I say to update all homotopy transfer references, that would cover line 1104, which uses `sec:` instead of `app:`. I can mention this in the fix list, reducing findings to eight.
thinking
**Assessing label updates**

I'm wondering if there's an issue with `higher_genus_modular_koszul` having correct chapter references in the introduction. After renaming the label to `chap:nonlinear...`, those lines can update accordingly. I think the label in `appendices/nonlinear_modular_shadows.tex:2` should also be renamed. Although it still works currently, fixing those labels means many references will need updating. Additionally, I might reconsider using theory file paths like `chapters/theory/coderived_models.tex:3`, since the user prefers file:line formats. Let’s ensure everything aligns well.
thinking
**Considering exact line numbers**

I'm thinking we might want to run `nl -ba` or `sed -n` to get precise line numbers for our references. However, I noted that `rg` has already provided the exact numbers, so maybe we don’t need to do that. It's great that we have options, but I’m considering if it’s necessary to add more steps. I want to keep things efficient while making sure we have the right details!
codex
- [CRITICAL] `main.tex:1660` — PROBLEM: `\phantomsection\label{app:coderived-models}` is only a synthetic “planned appendix” anchor, while the actual live material is `chapters/theory/coderived_models.tex:188` (`\label{sec:coderived-models}`) and the archive chapter itself is mislabeled `\label{app:coderived}` at `chapters/theory/coderived_models.tex:3`. Core theory points to that fake appendix target at `chapters/theory/higher_genus_foundations.tex:293,407,832`. FIX: rename `chapters/theory/coderived_models.tex:3` to `\label{chap:coderived-models}`, change its prose at line 12 from “This appendix” to “This chapter,” keep `\label{sec:coderived-models}` at line 188, replace those body references with `Chapter~\ref{chap:coderived-models}, \S\ref{sec:coderived-models}` (or just `\S\ref{sec:coderived-models}` where only the subsection is meant), and delete `main.tex:1643` `\label{app:coderived}` plus `main.tex:1660` `\label{app:coderived-models}`.

- [HIGH] `chapters/theory/nilpotent_completion.tex:4` — PROBLEM: this archive-only frontier chapter is included before `\appendix` (`main.tex:1559`) but still carries the appendix label `app:nilpotent-completion` and appendix prose at `chapters/theory/nilpotent_completion.tex:8,19,1277`; annals mode then fakes the same appendix label at `main.tex:1642`, while core theory cites it as `Appendix` at `chapters/theory/bar_cobar_adjunction_inversion.tex:70`, `bar_cobar_adjunction_curved.tex:1514,5980`, `introduction.tex:2624`, `algebraic_foundations.tex:2436,2499`, `poincare_duality.tex:682`, `filtered_curved.tex:131`, `chiral_koszul_pairs.tex:4859,4865,5422`. FIX: rename the live label to `chap:nilpotent-completion`, change “This appendix”/“present appendix” to “This chapter”/“present frontier chapter,” replace every `Appendix~\ref{app:nilpotent-completion}` with `Chapter~\ref{chap:nilpotent-completion}` in archive-visible text, remove `main.tex:1642`, and rewrite annals-visible mentions as plain archive-only notes instead of fake appendix references.

- [HIGH] `chapters/theory/algebraic_foundations.tex:116` — PROBLEM: the definition of a quadratic algebra sends the reader to `Definition~\ref{def:bar-complex-algebraic}`, but that label lives in the notation appendix at `appendices/notation_index.tex:342`, where the “definition” is only a back-pointer to `Theorem~\ref{thm:bar-coalgebra}`. This is source-to-index-to-source circularity on a core definition seam. FIX: replace the sentence with a real forward statement, e.g. `The bar construction is built from~\bar A via \(B(A)=T^c(s^{-1}\bar A)\); see Theorem~\ref{thm:bar-coalgebra}.` Do not cite `def:bar-complex-algebraic` from core theory.

- [HIGH] `chapters/theory/existence_criteria.tex:474` — PROBLEM: the proved classification table sends the `\mathcal W_{1+\infty}` row to `Appendix~\ref{app:koszul-reference}`, while `appendices/koszul_reference.tex:242` sends the reader straight back to `Appendix~\ref{app:existence-criteria}` for the classification table. That is a circular navigation dependency with no direct criterion at the seam. FIX: in the table row, replace `Filtered; see Appendix~\ref{app:koszul-reference}` with a concrete pointer such as `Filtered; completed dual on the essential-image locus of Theorem~\ref{thm:essential-image-koszul}`; then change `appendices/koszul_reference.tex:242` to cite that same theorem directly instead of bouncing back to the table.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1583` — PROBLEM: this proved theorem cites promoted main-body material as `Appendix~\ref{app:homotopy-transfer}`, even though `appendices/homotopy_transfer.tex` is loaded before `\appendix` at `main.tex:1010`; the citation is also too vague, since the theorem used is `appendices/homotopy_transfer.tex:455` (`thm:chiral-htt`), not the chapter as a whole. The same chapter/appendix drift appears at `chapters/theory/higher_genus_foundations.tex:1104`, `quantum_corrections.tex:360,525`, `chiral_modules.tex:2665`, and `chiral_hochschild_koszul.tex:2901,2933`. FIX: rename `appendices/homotopy_transfer.tex:2` to `\label{chap:homotopy-transfer}`, change `higher_genus_foundations.tex:1583` to `Theorem~\ref{thm:chiral-htt} produces a minimal...`, change `higher_genus_foundations.tex:1104` to `Chapter~\ref{chap:homotopy-transfer}, \S\ref{sec:ainfty-historical}`, and replace the remaining `Appendix~\ref{app:homotopy-transfer}` pointers with `Chapter~\ref{chap:homotopy-transfer}` or the exact theorem labels they use.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:4313` — PROBLEM: the proved corollary writes the quartic projection as `R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)` and cites the whole nonlinear-shadows chapter generically, but the promoted chapter `appendices/nonlinear_modular_shadows.tex` defines the actual object as `\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)` at `appendices/nonlinear_modular_shadows.tex:1733-1742` (`def:nms-modular-quartic-resonance-class`) and is loaded before `\appendix` at `main.tex:1109`. This is both notation drift and an imprecise seam citation. FIX: change the corollary to `\pi_4(\Theta_\cA)=\mathfrak R^{\mathrm{mod}}_{4,\bullet,\bullet}(\cA)` and replace the generic chapter pointer with `Definition~\ref{def:nms-modular-quartic-resonance-class}`; also rename `appendices/nonlinear_modular_shadows.tex:2` to `\label{chap:nonlinear-modular-shadows}` and update the generic `Appendix~\ref{app:nonlinear-modular-shadows}` references in this chapter (`4848, 10138, 12290, 12329, 13220, 15463, 15477, 29759, 31102`) to `Chapter~\ref{chap:nonlinear-modular-shadows}`.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:5752` — PROBLEM: `branch_line_reductions` is a promoted main-body chapter (`main.tex:1113`) but the body still cites it as `Appendix~\ref{app:branch-line-reductions}` here, again at `chapters/theory/chiral_hochschild_koszul.tex:5784`, and in `chapters/theory/introduction.tex:1954`. FIX: rename `appendices/branch_line_reductions.tex:2` to `\label{chap:branch-line-reductions}` and change those references to `Chapter~\ref{chap:branch-line-reductions}`; where a specific result is intended, replace the chapter-level pointer with the exact theorem label from that chapter.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:1116` — PROBLEM: `Appendix~\ref{app:combinatorial-frontier}` points to an archive-only chapter loaded before `\appendix` in archive mode (`main.tex:1371`) and replaced by a phantom label in annals mode (`main.tex:1873`). The seam therefore misclassifies the object as an appendix and leaves annals-visible text pointing at a placeholder instead of live content. FIX: rename `appendices/combinatorial_frontier.tex:2` to `\label{chap:combinatorial-frontier}`, change archive-mode cross-references such as this one and `chapters/theory/introduction.tex:2251` to chapter refs, and replace annals-visible mentions with plain text like `the archive-only combinatorial frontier chapter`; then delete `main.tex:1873` `\label{app:combinatorial-frontier}`.

## Summary
Checked: 33 | Findings: 8 | Verdict: FAIL
tokens used
258,219
