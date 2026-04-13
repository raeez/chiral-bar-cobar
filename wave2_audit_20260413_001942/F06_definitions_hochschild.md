# F06_definitions_hochschild (673s)

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:324 — PROBLEM: The chapter replaces the canonical chiral Hochschild complex by `\text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\A)),\A)` and then upgrades that to `\Ext_{\mathrm{ChirAlg}}` / `\RHom_{\mathrm{ChirAlg}}` “by definition” at lines 355-357, 572-573, and 754-756. The canonical definition actually read in [chiral_center_theorem.tex:298-343] is `C^\bullet_{\mathrm{ch}}(A,A)=\prod_{k\ge0}\End^{\mathrm{ch}}_A(k)[1-k]` with differential `\delta=[m,-]`. No comparison theorem is stated before the substitution. FIX: Insert the canonical definition at the start of this chapter:
  `\ChirHoch^\bullet(\A):=H^\bullet(C^\bullet_{\mathrm{ch}}(\A,\A)),\quad C^\bullet_{\mathrm{ch}}(\A,\A)=\prod_{k\ge0}\End^{\mathrm{ch}}_\A(k)[1-k].`
  Then restate Theorem~324 as a comparison theorem, e.g.
  `C^\bullet_{\mathrm{ch}}(\A,\A)\simeq \Conv(\bar B^{\mathrm{ch}}(\A),\A)` (or the precise dg Hom-complex you intend), and replace every “by definition” equality with “via the quasi-isomorphism of Theorem~\ref{thm:hochschild-bar-cobar}”.

- [CRITICAL] chapters/theory/higher_genus_foundations.tex:2672 — PROBLEM: `def:bigraded-hochschild` names a new object “the bigraded chiral Hochschild complex” but defines it as `R\mathrm{Hom}_{\mathcal D_{\overline C_{p+2}(X)}}(\A^{\boxtimes(p+2)},\omega_{\overline C_{p+2}(X)})`. That is a Verdier/derived-Hom model, not the canonical `End^{\mathrm{ch}}_A` cochain complex, and no comparison theorem identifies the two before `chiral_hochschild_koszul.tex` uses this definition as Theorem H’s input. FIX: Rename this definition to “Verdier-dual bar model for chiral Hochschild,” then add an explicit proposition immediately after it proving/citing
  `CH^{p,\bullet}_{\mathrm{Verd}}(\A)\simeq \operatorname{gr}_p C^\bullet_{\mathrm{ch}}(\A,\A)`,
  and only after that define `RHH_{\mathrm{ch}}(\A)` as the same object.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145 — PROBLEM: The local “geometric realization” defines a degree-`n` cochain using only `\overline C_{n+2}(X)` and fixed `n`-forms. That collapses arity/bar degree and cochain degree into one index, contradicting both the canonical bigrading in [chiral_center_theorem.tex:298-333] and the later imported bigraded model [higher_genus_foundations.tex:2672-2688]. FIX: Replace lines 143-157 by a genuinely bigraded definition, e.g.
  `\mathcal F^{p,q}_{\mathrm{ch}}(\A):=R\Gamma(\overline C_{p+2}(X), j_*j^*\A^{\boxtimes(p+2)}\otimes \Omega^q_{\overline C_{p+2}(X)}(\log D))`,
  and then set
  `\ChirHoch^\bullet(\A)=\Tot(\bigoplus_{p\ge0}\mathcal F^{p,\bullet}_{\mathrm{ch}}[-p])`.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:282 — PROBLEM: The proof of `thm:chiral-hochschild-differential` asserts that `d_{\mathrm{dR}}\eta_{12}` is “supported on the boundary divisor” and decomposes into boundary residues. Two paragraphs earlier `d_{\text{config}}` was defined as the ordinary de Rham differential, and `\eta_{12}=d\log(z_1-z_2)` is closed on configuration space. As written, the key cancellation step is false. FIX: Delete lines 282-289 and replace them with a correct boundary argument: either work in the logarithmic de Rham complex with explicit residue maps, or cite `thm:arnold-relations` to state that the codimension-2 boundary contributions from the three collision strata cancel in the Stokes formula. Do not write `d_{\mathrm{dR}}\eta_{12}` as a boundary current unless that extension is defined first.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:123 — PROBLEM: The file states `d_{\mathrm{fib}}^{\,2}=\kappa(\A)\omega_g`, then concludes “the bar complex is a curved `A_\infty`-algebra.” That is the wrong object. In this repo the bar complex is a coalgebra; curvature belongs to the fiberwise/dual curved structure, not to “the bar complex as an `A_\infty`-algebra.” FIX: Replace lines 123-127 with: “At genus `g\ge1`, the fiberwise differential satisfies `d_{\mathrm{fib}}^{\,2}=\kappa(\A)\omega_g`. This is the curved gauge on the genus-`g` fibre; the bar differential on `B(\A)` remains square-zero as a coalgebra differential, while the dual/Koszul-dual algebra acquires the corresponding curved `A_\infty` structure.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:362 — PROBLEM: The spectral-sequence theorem is not built on the object actually defined above. `E_0^{n,q}` is written as plain global sections, `d_0` is called “sheaf cohomology,” `\ChirHoch^{m,*}` appears without prior definition, and the proof never constructs a double complex whose vertical differential is sheaf cohomology. FIX: Restate this as the hypercohomology spectral sequence of the corrected sheaf complex:
  `E_1^{p,q}=H^q(\overline C_{p+2}(X),\mathcal F_p^\bullet)\Rightarrow \mathbb H^{p+q}(\Tot\mathcal F_\bullet^\bullet)`,
  define `\mathcal F_p^\bullet` explicitly, and remove `d_{\mathrm{sheaf}}` as if it were an honest differential on `\Gamma`.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:864 — PROBLEM: The proof of `prop:e2-formality-hochschild` does not prove the claim it states. The degree count at lines 886-896 does not kill ternary operations, and “collapse at `E_2` forces higher `E_2`-operations to be coboundaries” is asserted without mechanism. The statement also mislabels the Gerstenhaber bracket as “degree-`1`” at line 875. FIX: Replace the proof with a direct citation to [en_koszul_duality.tex:955-969] plus [chiral_center_theorem.tex:1714-1723]: operad formality identifies `E_2`-algebras up to quasi-isomorphism by their induced Gerstenhaber structure on cohomology. Then change line 875 to “degree-`(-1)` bracket” or “degree-`0` bracket on `H^*(\ChirHoch(\A))[1]`.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4881 — PROBLEM: The bracket theorem gets the structure wrong twice. A degree `-1` bracket does not make `\ChirHoch^\bullet(\A)` itself a graded Lie algebra; it makes `\ChirHoch^\bullet(\A)[1]` a graded Lie algebra, or `\ChirHoch^\bullet(\A)` a Gerstenhaber algebra. The sentence “not by algebraic composition” at line 4889 also contradicts the proof and the imported definition [chiral_center_theorem.tex:501-516], where the bracket is the antisymmetrized single-brace operadic composition. FIX: Replace lines 4881-4889 with: “The chiral Hochschild cohomology carries a degree `-1` Gerstenhaber bracket; equivalently `\ChirHoch^\bullet(\A)[1]` is a graded Lie algebra. Geometrically, this bracket is realized by OPE residues on configuration spaces, which coincide with the antisymmetrized single-brace operadic compositions.”

- [HIGH] chapters/theory/chiral_center_theorem.tex:544 — PROBLEM: The imported degree conventions are plainly wrong: the cup product and the Gerstenhaber bracket are both described as “degree~`2`.” That conflicts with the local bracket definition [chiral_center_theorem.tex:501-516] and the cohomology statement [chiral_center_theorem.tex:1714-1723]. FIX: Replace lines 544-546 with: “the cup product (associative, cohomological degree `0`), the Gerstenhaber bracket (degree `-1` on `C^\bullet_{\mathrm{ch}}`, degree `0` on `C^\bullet_{\mathrm{ch}}[1]`), and the full brace system.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4797 — PROBLEM: The Heisenberg example uses the wrong family reference and the wrong model. It cites `thm:km-chiral-koszul`, whose registry entry is “Affine Kac--Moody algebras are chiral Koszul,” to justify a Heisenberg claim; the same miscitation recurs at line 1351. Then line 4799 computes `\ChirHoch` by applying `\Hom_{\mathcal B-\mathcal B}(-,\mathcal B)` to a bimodule resolution, which is exactly the classical `A^e`-style move this chapter was supposed to avoid. FIX: Replace both Heisenberg citations by `thm:heisenberg-koszul-dual-early` or `thm:frame-heisenberg-koszul-dual`, and rewrite the computation in the canonical chiral model `C^\bullet_{\mathrm{ch}}(\mathcal B,\mathcal B)`; if you insist on the bimodule resolution, add an explicit comparison proposition from the chiral complex to that classical model before using it.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:12 — PROBLEM: The opening paragraph identifies `\ChirHoch^\bullet(\A)` with “the tangent complex to `\MC(\gAmod)/\mathrm{gauge}`” and immediately converts degree concentration into moduli amplitude `[0,2]`, but no shift convention for tangent complexes of MC moduli problems is stated here. Later tangent-complex definitions in the same file use shifted fibers [chiral_hochschild_koszul.tex:5255-5265]. FIX: Replace lines 11-16 with a shift-free statement: “`\ChirHoch^\bullet(\A)` is the deformation complex controlling bulk deformations; Theorem H gives vanishing outside degrees `0,1,2` on the Koszul locus.” Only discuss the tangent complex of the MC stack after the chapter states its shift convention.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:136 — PROBLEM: The duality formula is cited to `rem:nc-hodge-degeneration`, but that remark only discusses pole-order filtration and Hodge-type language; it does not state `\ChirHoch^n(\A)\cong \ChirHoch^{2-n}(\A^!)^\vee\otimes\omega_X`. FIX: Change the citation at line 137 to a forward reference to `Theorem~\ref{thm:main-koszul-hoch}` or to `Lemma~\ref{lem:hochschild-shift-computation}` plus `Theorem~\ref{thm:main-koszul-hoch}`.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:109 — PROBLEM: The file says the chiral Hochschild complex is “constructed in `\S\ref{subsec:hochschild-duality}`,” but that label is attached to the later main-duality subsection, not to the local construction at lines 139-318 or the algebraic definition in `chiral_center_theorem.tex`. FIX: Change the reference to “constructed in the present section” or “defined algebraically in Definition~\ref{def:chiral-hochschild-cochain-brace} and realized geometrically below.”

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:4867 — PROBLEM: The comparison with classical Hochschild cohomology ends with “For constant fields: `\ChirHoch^n(\A)|_{\text{constant}}\cong HH^n_{\text{classical}}(H^0(\A))`,” but “constant fields” is undefined and no comparison theorem or citation is supplied. FIX: Delete lines 4871-4873, or replace them with a qualified sentence: “After choosing a constant-field truncation functor and proving compatibility of the chiral and classical brace structures, one expects a comparison with classical Hochschild cohomology; this is not proved here.”

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:4539 — PROBLEM: The CFT aside leaks out of the chapter’s proved scope twice. Line 4541 treats `\ChirHoch^3` as the obstruction space without saying this is the pre-Theorem-H general pattern; on the Koszul locus the chapter itself later proves `\ChirHoch^n=0` for `n>2`. Line 4544 then jumps to `\mathcal N=4` SYM and a `\mathbb C^{3(g-1)}` deformation space inside Volume I with no setup, citation, or chiral-algebra-on-a-curve model. FIX: Rewrite the paragraph as: “For a general deformation complex, degree `2` classes are first-order deformations and degree `3` classes are potential obstructions; on the Koszul locus Theorem~\ref{thm:hochschild-polynomial-growth} kills the latter.” Then delete the `\mathcal N=4` SYM example or move it to Volume II with a precise citation.

- [LOW] chapters/theory/chiral_hochschild_koszul.tex:4976 — PROBLEM: The Heisenberg bracket example proves only `[[k],[k]]=0`, then overstates this as “the level is a central element … (it commutes with everything).” Self-bracket zero does not imply centrality. FIX: Replace the last sentence with: “This shows only that the self-bracket of the level class vanishes. Centrality would require a separate computation of `[[k],x]` for every `x\in\ChirHoch^\bullet(\mathcal B)`.”

## Summary
Checked: 8 | Findings: 16 | Verdict: FAIL


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
session id: 019d83e2-7e7b-7f73-b015-bf2638e436d1
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


MISSION: FOUNDATION AUDIT of chapters/theory/chiral_hochschild_koszul.tex

Check: is chiral Hochschild ChirHoch defined via End^{ch}_A (NOT via RHom_{A^e})? Is the Gerstenhaber bracket defined (both insertions, not just one)? Is the concentration claim in {0,1,2} precise (amplitude vs dimension)?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Preparing for code audit**

I need to audit a file in coding agent mode. It seems I should consider using the skill deep-beilinson-audit, maybe even multi-path-verify, since the user explicitly asked for an audit of the foundation file. First, I have to read the required AGENTS, then delve into related documentation like CLAUDE.md and the theorem registry. I want to focus solely on identifying bugs, risks, and suggesting exact fixes without making edits unless asked. I’ll ensure to back my claims with the contents read.
thinking
**Planning a code review**

I should start by using the explorer agent for codebase questions, especially for file reviews. It seems that this agent can help locate relevant files and dependencies quickly. Since I want grounded findings, I’ll combine manual reading with explorer insights, focusing on documents like CLAUDE.md and the theorem registry. While I need to be respectful of approval processes, I might not need a detailed plan since the user asked for a review. However, I should still provide a short commentary update.
thinking
**Examining unresolved references**

I need to probably use a command like `rg -n "ChirHoch|Gerstenhaber|End\^{ch}|RHom|0,1,2|amplitude|dimension|Hochschild"` to search the target file and maybe the whole repo. I should also check for unresolved references using LaTeX commands, looking for `\ref{` in case any are missing. Since the user has requested a focus on the foundation audit of the chapter, I’ll consider any hidden imports or unresolved references as findings and possibly inspect for `\Cref` label existence too.
codex
I’m auditing `chapters/theory/chiral_hochschild_koszul.tex` as a hostile reviewer. First I’m reading the mandatory repo context and the exact chapter surface, then I’ll cross-check every claim about `\mathrm{ChirHoch}`, the bracket, and the `{0,1,2}` concentration claim against the live source.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 366ms:
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
 succeeded in 407ms:
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

 succeeded in 400ms:
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
 succeeded in 367ms:
\chapter{Chiral Hochschild cohomology and Koszul duality}
\label{chap:deformation-theory}

\index{deformation theory!chiral|textbf}
\index{Hochschild cohomology!chiral|textbf}

The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
Koszul duality, but how rigid is the moduli it lives in? Without
knowing the tangent complex to
$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
bulk-field coupling remains inaccessible. The chiral Hochschild
complex $\ChirHoch^*(\cA)$ is that tangent complex;
Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
Koszul locus, so the MC moduli has cohomological
amplitude~$[0,2]$, and the Koszul duality
$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
is Verdier duality on this tangent space.

The cyclic deformation complex $\Defcyc(\cA)$
(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
 succeeded in 451ms:
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

codex
I have the chapter surface loaded. Next I’m reading the rest of the file and then I’ll cross-check every referenced definition/label that the chapter leans on for the `ChirHoch` construction, the Gerstenhaber bracket, and the `{0,1,2}` claim.
exec
/bin/zsh -lc "sed -n '261,520p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '521,820p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 78ms:
bar degree~$p$ is $(p+2) - p = 2$.

It remains to see that this uniform value persists after passing to
cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
cohomology $H^{p,q}(\barB^{\mathrm{ch}}(\cA))$ vanishes for
$q \neq 0$; only the $q = 0$ diagonal contributes. On this
diagonal, bar degree~$p$ and cohomological degree~$q = 0$ give
total degree~$p + 0 = p$ in the source and $p + 2$ in the target
(after the Verdier shift). The difference $2$ is independent of~$p$,
confirming the uniform shift.

The $\omega_X$ factor: Serre duality on the one-dimensional base
curve~$X$ contributes $\omega_X = \Omega^1_X$ as the dualizing sheaf.
This twist is intrinsic to $\mathcal{D}$-module duality on~$X$ and
independent of the configuration-space geometry.
\end{proof}

\begin{lemma}[Chiral Hochschild descent; \ClaimStatusProvedHere]
\label{lem:chirhoch-descent}
\index{chiral Hochschild!descent from bar}
exec
/bin/zsh -lc "rg -n \"ChirHoch|chiral Hochschild|Gerstenhaber|brace|RHom|A\\"'^e|End'"\\"'^'"\\{ch\\}_A|End\\"'^'"\\{ch\\}|0,1,2|amplitude|dimension|cohomological degrees|concentrated\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 1.00s:
with three points $z_1, z_2, z_3$), the two compositions act
as:
\begin{align*}
(d_{\text{config}} \circ d_{\text{fact}})(\phi)
&= d_{\mathrm{dR}}\Bigl(
 \mathrm{Res}_{z_1 = z_2}\bigl[a_1 a_2 \otimes a_3
 \otimes \eta_{12}\bigr] \Bigr), \\
(d_{\text{fact}} \circ d_{\text{config}})(\phi)
&= \sum_{i<j}
 \mathrm{Res}_{z_i = z_j}\bigl[a_1 \otimes a_2 \otimes a_3
 \otimes d_{\mathrm{dR}}\eta_{12}\bigr].
\end{align*}

The key identity is Arnold's relation
\cite{Arnold69}: for the logarithmic 1-forms
$\eta_{ij} = d\log(z_i - z_j)$ on $C_3(X)$,
\begin{equation}\label{eq:arnold-three-point}
\eta_{12} \wedge \eta_{23}
+ \eta_{23} \wedge \eta_{31}
+ \eta_{31} \wedge \eta_{12} = 0.
 succeeded in 747ms:
11:bulk-field coupling remains inaccessible. The chiral Hochschild
12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
13:Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
15:amplitude~$[0,2]$, and the Koszul duality
16:$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
21:refinement of $\ChirHoch^*(\cA)$.
28:carry natural brace and $E_2$ structures. The convolution dg~Lie
49: (Theorem~\ref{thm:chiral-deligne-tamarkin}). The brace dg algebra
108:That complex is the \emph{chiral Hochschild complex}
114:in the chiral Hochschild complex involves $(n+2)$ points on~$X$;
136:$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
139:\section{Construction of the chiral Hochschild complex}
172:\begin{theorem}[The chiral Hochschild differential; \ClaimStatusProvedHere]
357:The left side is precisely $\ChirHoch^n(\mathcal{A})$ by definition.
365:E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log}) \Rightarrow \ChirHoch^{n+q}(\mathcal{A})
371:The chiral Hochschild complex $\ChirHoch^*(\mathcal{A})$ is a double complex with horizontal differential $d_{\mathrm{bar}}$ (the bar differential of Definition~\ref{def:bar-differential-complete}) and vertical differential $d_{\mathrm{sheaf}}$ (sheaf cohomology on configuration spaces). Filter by bar degree: $F^n = \bigoplus_{m \geq n} \ChirHoch^{m,*}$. The resulting spectral sequence has $E_0^{n,q} = \Gamma(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$ with $d_0 = d_{\mathrm{sheaf}}$, so $E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$. Convergence follows from the bounded-below hypothesis on $\mathcal{A}$ and the finite cohomological dimension of configuration spaces.
376:\ChirHoch^k(\mathcal{A}) \cong \bigoplus_{n+q=k} H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log})
483:chiral Hochschild complex
491: has complex dimension $p+2$\textup{)};
509:variety $Y_p := \overline{C}_{p+2}(X)$ of complex dimension
 succeeded in 862ms:
     1	\chapter{Chiral Hochschild cohomology and Koszul duality}
     2	\label{chap:deformation-theory}
     3	
     4	\index{deformation theory!chiral|textbf}
     5	\index{Hochschild cohomology!chiral|textbf}
     6	
     7	The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
     8	Koszul duality, but how rigid is the moduli it lives in? Without
     9	knowing the tangent complex to
    10	$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
    11	bulk-field coupling remains inaccessible. The chiral Hochschild
    12	complex $\ChirHoch^*(\cA)$ is that tangent complex;
    13	Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
    14	Koszul locus, so the MC moduli has cohomological
    15	amplitude~$[0,2]$, and the Koszul duality
    16	$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
    17	is Verdier duality on this tangent space.
    18	
    19	The cyclic deformation complex $\Defcyc(\cA)$
    20	(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic


thinking
**Planning an exhaustive audit**

I need to prepare for an extensive audit of the file, focusing on specific segments and theorems like theorem H. I want to check for labels, definitions, and references to ensure everything is in order. The task emphasizes identifying every weakness, even subtle ones, which might lead to numerous findings. However, time is limited, so I’ll focus mainly on the foundational sections and line numbers related to the references, confirming their existence. I might consider using an explorer agent to assist with locating any missing definitions.
thinking
**Utilizing deep-beilinson-audit skill**

I might need to use the deep-beilinson-audit skill for this task. First, I have to announce that I’m using this skill in the commentary section. After that, I’ll open the skill file to ensure everything’s ready to go. It’s important to take these steps to make sure I’m prepared and organized. Alright, let’s get started with that process now!
codex
I’m using `deep-beilinson-audit` for this pass because this is a theorem-surface falsification job, not a local wording check. I’m now checking whether the chapter’s claimed definitions and proof infrastructure actually exist at the cited labels, or whether this chapter is leaning on ghosts and category slips.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4840,5025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "def:chiral-hochschild-cochain-brace|cor:gerstenhaber-cohomology|thm:chiral-deligne-tamarkin|def:bigraded-hochschild|thm:bar-concentration|thm:operadic-homotopy-convolution|def:cyclic-deformation-elementary|def:modular-cyclic-deformation-complex|rem:modular-cyc-strictification|thm:arnold-relations|thm:HC-spectral-sequence|rem:nc-hodge-degeneration|thm:e1-module-koszul-duality|thm:kodaira-spencer-chiral-complete|lem:verdier-involution-moduli|def:thqg-chiral-derived-center|sec:thqg-open-closed-realization|thm:thqg-annulus-trace|chap:bar-cobar|ch:algebraic-foundations|chap:e1-modular-koszul|conv:regime-tags" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4840	\mathbb{C} & n = 0\\
  4841	0 & n = 1\\
  4842	\mathbb{C} & n = 2\\
  4843	0 & n \geq 3
  4844	\end{cases}\]
  4845	
  4846	As a graded algebra:
  4847	\[\ChirHoch^*(\mathcal{F}) \cong \Lambda(c)\]
  4848	(exterior algebra on one generator of degree 2)
  4849	\end{example}
  4850	
  4851	\subsection{Koszul duality and HH* pairing}
  4852	
  4853	The Koszul duality for Hochschild cohomology (Theorem~\ref{thm:main-koszul-hoch}) is now verified on examples.
  4854	
  4855	\begin{verification}[$bc$/$\beta\gamma$ Koszul duality; \ClaimStatusProvedHere]\label{ver:boson-fermion-HH}
  4856	The Koszul pair ($bc$ ghost system $\mathcal{F}_{bc}$, $\beta\gamma$ system $\mathcal{BG}$) satisfies:
  4857	\begin{align*}
  4858	\ChirHoch^0(\mathcal{F}_{bc}) = \mathbb{C} &\xleftrightarrow{\text{dual}} \ChirHoch^2(\mathcal{BG})^* = \mathbb{C}\\
  4859	\ChirHoch^1(\mathcal{F}_{bc}) = 0 &\xleftrightarrow{\text{dual}} \ChirHoch^1(\mathcal{BG})^* = 0\\
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

 succeeded in 51ms:
Total output lines: 542

metadata/dependency_graph.dot:853:  thm_thqg_annulus_trace [label="thm:thqg-annulus-trace\ntheorem [Pr]\nAnnulus trace theorem", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2037:  thm_operadic_homotopy_convolution [label="thm:operadic-homotopy-convolution\ntheorem [Pr]\nOperadic identification of the convoluti...", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:2319:  thm_chiral_deligne_tamarkin [label="thm:chiral-deligne-tamarkin\ntheorem [Pr]\nChiral Deligne--Tamarkin", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2394:  thm_bar_concentration [label="thm:bar-concentration\ntheorem [Pr]\nBar concentration for Koszul pairs", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2432:  thm_e1_module_koszul_duality [label="thm:e1-module-koszul-duality\ntheorem [Pr]\n\texorpdfstring{$\Eone$}{E1}-module cate...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2586:  thm_arnold_relations [label="thm:arnold-relations\ntheorem [Pr]\nArnold relations", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2759:  thm_kodaira_spencer_chiral_complete [label="thm:kodaira-spencer-chiral-complete\ntheorem [Pr]\nKodaira--Spencer map for chiral algebras", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2760:  lem_verdier_involution_moduli [label="lem:verdier-involution-moduli\nlemma [Pr]\nVerdier involution on moduli cohomology", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3008:  thm_operadic_homotopy_convolution_modular [label="thm:operadic-homotopy-convolution-modular\ntheorem [Pr]\nOperadic homotopy convolution {\cite[The...", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:3220:  thm_HC_spectral_sequence [label="thm:HC-spectral-sequence\ntheorem [Pr]\nHochschild-cyclic spectral sequence {\ci...", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:3473:  thm_arnold_relations_appendix [label="thm:arnold-relations-appendix\ntheorem [Pr]\nArnold relations \cite{Arnold69}", style=filled, fillcolor="#bbdefb"];
metadata/theorem_registry.md:335:| `thm:chiral-deligne-tamarkin` | `theorem` | 1232 | Chiral Deligne--Tamarkin |
metadata/theorem_registry.md:399:| `thm:bar-concentration` | `theorem` | 1047 | Bar concentration for Koszul pairs |
metadata/theorem_registry.md:429:| `thm:e1-module-koszul-duality` | `theorem` | 4881 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
metadata/theorem_registry.md:568:| `thm:arnold-relations` | `theorem` | 733 | Arnold relations |
metadata/theorem_registry.md:718:| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1219 | Kodaira--Spencer map for chiral algebras |
metadata/theorem_registry.md:719:| `lem:verdier-involution-moduli` | `lemma` | 1407 | Verdier involution on moduli cohomology |
metadata/theorem_registry.md:2978:| `thm:thqg-annulus-trace` | `theorem` | 576 | Annulus trace theorem |
codex
The dependency surface is active now. I’ve already hit one obvious structural risk: this chapter repeatedly cites external definitions for the algebraic Hochschild complex and bracket, so I’m reading those exact source blocks instead of trusting the local paraphrase.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '280,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1288,1735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"RHom_\\{|RHom|A\\"'^e|End'"\\"'^'"\\{ch\\}_A|End\\"'^'"\\{ch\\}|derived center|ChirHoch\\"'^'"\\*|brace|Gerstenhaber bracket|single-brace|f\\{g\\}|g\\{f\\}\" chapters/theory/chiral_center_theorem.tex chapters/theory/higher_genus_foundations.tex chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2660,2725p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   280	and $h$ are commuted past the inputs of~$f$.
   281	\end{proof}
   282	
   283	The chiral endomorphism operad encodes multilinear operations
   284	with spectral parameters; partial composition encodes nested
   285	collisions. But an operad is not yet a cochain complex.
   286	To extract the deformation theory of a specific algebra
   287	$(A, \{m_k\})$, we must assemble these operation spaces into
   288	a single bigraded complex with a differential determined
   289	by~$m$.
   290	
   291	%% ===========================================================
   292	%% 2. CHIRAL HOCHSCHILD COCHAIN COMPLEX
   293	%% ===========================================================
   294	
   295	\subsection{The chiral Hochschild cochain complex}
   296	\label{subsec:chiral-hoch-cochain}
   297	
   298	\begin{definition}[Chiral Hochschild cochain complex]
   299	\label{def:chiral-hochschild-cochain-brace}
 succeeded in 52ms:
  1288	 cochain~$f$ on the open inputs.
  1289	\end{enumerate}
  1290	\end{construction}
  1291	
  1292	%% ===========================================================
  1293	%% 7. CHIRAL DELIGNE--TAMARKIN THEOREM
  1294	%% ===========================================================
  1295	
  1296	\subsection{The chiral Deligne--Tamarkin theorem}
  1297	\label{subsec:chiral-deligne-tamarkin}
  1298	
  1299	\begin{theorem}[Chiral Deligne--Tamarkin; \ClaimStatusProvedHere]
  1300	\label{thm:chiral-deligne-tamarkin}
  1301	\index{Deligne--Tamarkin theorem!chiral}
  1302	\index{chiral center theorem|see{Deligne--Tamarkin}}
  1303	Let $(A, \{m_k\})$ be a curved $\Ainf$-chiral algebra.
  1304	The universal local chiral Swiss-cheese pair
  1305	\[
  1306	U(\cA) = \bigl(C^\bullet_{\mathrm{ch}}(A, A),\, A,\,
  1307	\{\mu^{\mathrm{univ}}_{p;q}\}\bigr)
 succeeded in 51ms:
  2660	\ChirHoch^n(\mathcal{A})
  2661	\;\cong\; \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee}
  2662	\otimes \omega_X.
  2663	\end{equation}
  2664	\end{corollary}
  2665	
  2666	\begin{proof}
  2667	This is Theorem~\ref{thm:main-koszul-hoch} (Theorem~H), proved
  2668	independently in \S\ref{subsec:hochschild-duality} via
  2669	the bar-cobar quasi-isomorphism and Verdier duality on the Ran space.
  2670	\end{proof}
  2671	
  2672	\begin{definition}[Bigraded chiral Hochschild complex]
  2673	\label{def:bigraded-hochschild}
  2674	\index{Hochschild cohomology!bigraded|textbf}
  2675	The \emph{bigraded chiral Hochschild complex} of a chiral
  2676	algebra~$\cA$ on a smooth curve~$X$ is the double complex
  2677	\[
  2678	CH^{p,\bullet}_{\mathrm{ch}}(\cA) :=
  2679	R\mathrm{Hom}_{\mathcal{D}_{\overline{C}_{p+2}(X)}}
 succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:1413:\[\mathbb{D}(\mathcal{F}) = \mathcal{RHom}(\mathcal{F}, \omega_{\overline{C}_n(X)}[d])\]
chapters/theory/higher_genus_foundations.tex:5595:\underbrace{\frac{3}{c}}_{\text{banana}}
chapters/theory/higher_genus_foundations.tex:5597:\underbrace{\frac{9}{2c}}_{\text{theta}}
chapters/theory/higher_genus_foundations.tex:5599:\underbrace{\frac{1}{16}}_{\text{lollipop}}
chapters/theory/higher_genus_foundations.tex:5601:\underbrace{\frac{21}{4c}}_{\text{barbell}}
chapters/theory/higher_genus_foundations.tex:6474:\underbrace{g}_{\text{total genus}}
chapters/theory/higher_genus_foundations.tex:6476:\underbrace{\textstyle\sum_v g_v}_{\text{vertex genus}}
chapters/theory/higher_genus_foundations.tex:6478:\underbrace{b_1(\Gamma)}_{\text{loop order}}
chapters/theory/higher_genus_foundations.tex:6777: \underbrace{\Delta(S_0)}_{\text{one-loop anomaly}}
chapters/theory/higher_genus_foundations.tex:6779: \underbrace{\{S_0, S_1\}}_{\text{tree $\times$ genus-$1$}}
chapters/theory/chiral_hochschild_koszul.tex:12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
chapters/theory/chiral_hochschild_koszul.tex:21:refinement of $\ChirHoch^*(\cA)$.
chapters/theory/chiral_hochschild_koszul.tex:28:carry natural brace and $E_2$ structures. The convolution dg~Lie
chapters/theory/chiral_hochschild_koszul.tex:49: (Theorem~\ref{thm:chiral-deligne-tamarkin}). The brace dg algebra
chapters/theory/chiral_hochschild_koszul.tex:53: \delta)$ is the chiral derived center
chapters/theory/chiral_hochschild_koszul.tex:371:The chiral Hochschild complex $\ChirHoch^*(\mathcal{A})$ is a double complex with horizontal differential $d_{\mathrm{bar}}$ (the bar differential of Definition~\ref{def:bar-differential-complete}) and vertical differential $d_{\mathrm{sheaf}}$ (sheaf cohomology on configuration spaces). Filter by bar degree: $F^n = \bigoplus_{m \geq n} \ChirHoch^{m,*}$. The resulting spectral sequence has $E_0^{n,q} = \Gamma(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$ with $d_0 = d_{\mathrm{sheaf}}$, so $E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$. Convergence follows from the bounded-below hypothesis on $\mathcal{A}$ and the finite cohomological dimension of configuration spaces.
chapters/theory/chiral_hochschild_koszul.tex:572:this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
chapters/theory/chiral_hochschild_koszul.tex:872:\item $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
chapters/theory/chiral_hochschild_koszul.tex:873: the $\Etwo$ quasi-isomorphism type of $\ChirHoch^*(\cA)$ is
chapters/theory/chiral_hochschild_koszul.tex:877:\item All higher $\Etwo$-operations \textup{(}braces of
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '378,540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '540,740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "local-swiss-cheese-pair|eq:mixed-ops|eq:swiss-cheese-identity|eq:mixed-p1|const:universal-pair" chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/connections/thqg_open_closed_realization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   378	\begin{definition}[Brace operations]
   379	\label{def:brace-operations-chiral}
   380	\index{brace operations!chiral Hochschild}
   381	For cochains $f \in C^\bullet_{\mathrm{ch}}(A, A)$
   382	of degree~$p$ (i.e., $f \in \End^{\mathrm{ch}}_A(p)$)
   383	and $g_1, \ldots, g_r$ of degrees $q_1, \ldots, q_r$
   384	respectively, the \emph{brace operation}
   385	\begin{equation}\label{eq:brace-def}
   386	f\{g_1, \ldots, g_r\}
   387	\;\in\;
   388	\End^{\mathrm{ch}}_A\!\bigl(p + q_1 + \cdots + q_r - r\bigr)
   389	\end{equation}
   390	is defined by the following explicit formula.
   391	Set $Q := q_1 + \cdots + q_r - r$ (the total number
   392	of ``extra'' inputs contributed by the $g_j$).
   393	Then
   394	\begin{equation}\label{eq:brace-explicit}
   395	\boxed{
   396	\begin{aligned}
   397	&f\{g_1, \ldots, g_r\}
 succeeded in 51ms:
   540	\end{remark}
   541	
   542	Three algebraic structures now coexist on
   543	$C^\bullet_{\mathrm{ch}}(A, A)$:
   544	the cup product (associative, degree~$2$),
   545	the Gerstenhaber bracket (Lie on the desuspension, degree~$2$),
   546	and the full brace system (all degrees).
   547	The question is whether these structures are compatible
   548	with the differential $\delta = [m, -]$.
   549	They are: the chiral Hochschild cochains form a brace dg algebra.
   550	The proof of this fact occupies the next subsection and is the
   551	technical core of the chapter.
   552	
   553	%% ===========================================================
   554	%% 4. BRACE DG ALGEBRA THEOREM
   555	%% ===========================================================
   556	
   557	\subsection{The brace dg algebra structure}
   558	\label{subsec:brace-dg-algebra}
   559	
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:1111:\label{def:local-swiss-cheese-pair}
chapters/theory/chiral_center_theorem.tex:1125: \begin{equation}\label{eq:mixed-ops}
chapters/theory/chiral_center_theorem.tex:1138: \begin{equation}\label{eq:swiss-cheese-identity}
chapters/theory/chiral_center_theorem.tex:1228:\label{const:universal-pair}
chapters/theory/chiral_center_theorem.tex:1280: \begin{equation}\label{eq:mixed-p1}
chapters/theory/chiral_center_theorem.tex:1309:of Construction~\textup{\ref{const:universal-pair}} is
chapters/theory/chiral_center_theorem.tex:1406:definition~\eqref{eq:mixed-ops}, and has the correct
chapters/theory/chiral_center_theorem.tex:1415:Definition~\ref{def:local-swiss-cheese-pair}: the mixed
chapters/theory/chiral_center_theorem.tex:1435:identity~\eqref{eq:swiss-cheese-identity} with
chapters/theory/chiral_center_theorem.tex:1518:identity~\eqref{eq:swiss-cheese-identity} with
chapters/theory/chiral_center_theorem.tex:1525:in~\eqref{eq:swiss-cheese-identity}).
chapters/theory/chiral_center_theorem.tex:1611:(by definition~\eqref{eq:mixed-p1} of the universal
 succeeded in 54ms:
     1	%% ============================================================
     2	%% CHIRAL CENTER THEOREM
     3	%% Object M3 in the programme
     4	%% Self-contained module: definitions, brace algebra, Deligne--Tamarkin
     5	%% ============================================================
     6	
     7	\section{The chiral endomorphism operad and the chiral center theorem}
     8	\label{sec:chiral-center-theorem}
     9	
    10	\index{chiral center theorem|textbf}
    11	\index{brace algebra!chiral|textbf}
    12	\index{Deligne--Tamarkin!chiral|textbf}
    13	
    14	The center of a chiral algebra is too small. For the
    15	Virasoro algebra $\mathrm{Vir}_c$ at generic central charge,
    16	the ordinary center $Z(\mathrm{Vir}_c)$ is one-dimensional:
    17	it contains only the vacuum. Yet the algebra \emph{has}
    18	deformations: the central charge itself can be varied,
    19	$c \mapsto c + \epsilon$. This deformation is invisible
    20	to the center because the center sees only degree-$0$






thinking
**Examining labeling issues**

I’m noticing that if there's an issue here, it might undermine this file. First, I need to determine if the dependency is problematic. The audit surface includes both the chapter and dependencies, so it matters. 

I'm looking closely at lines 109-110. They reference a section that doesn't start where indicated, which feels off. Also, the actual construction I need to reference is in a different section altogether, which is misleading. I need to check those line labels carefully!
thinking
**Identifying foundational inconsistencies**

I need to fix the cross-reference to the current section or the `chiral_center_theorem` definition. The user wants a thorough assessment of weaknesses, so I need to be direct. 

Lines 145-156 provide a geometric definition that lacks proper derivation regarding global sections. Later, there's a mention of the spectral sequence theorem that introduces a mismatch with sheaf cohomology. Essentially, using ordinary global sections doesn't appropriately address sheaf cohomology. This could indicate a foundational inconsistency that needs correction, possibly suggesting the use of `R\Gamma` or a sheaf-level double complex instead.
thinking
**Clarifying definitions**

I could mention that lines 203-205 define `d_config` as the ordinary de Rham differential on the compactified configuration space. Then, the theorem states that `d_Hoch` equals the sum of `d_int`, `d_fact`, and `d_config`. This is a key relationship, and understanding how these differentials interact is important for grasping the broader context of the theorem. I might explore how each part contributes to the overall structure.
thinking
**Clarifying a mathematical statement**

I'm considering a clearer way to express the deformation complex controlling the MC moduli. I think I can say, "Replace lines 11-15 with: `The deformation complex controlling the MC moduli is \ChirHoch^\bullet(\cA); Theorem H gives vanishing outside degrees 0,1,2. In the convention used below, this means the deformation complex has amplitude [0,2].`" This way, I avoid making a possibly incorrect claim about the moduli stack tangent complex, which feels like a smart move!
thinking
**Evaluating theorem proof**

I’m analyzing a theorem that’s claimed to be proved, but the proof seems more like handwaving. It doesn’t properly establish that the bar is a cofree resolution or that Hom computes the derived deformation complex. The user wants a thorough audit, so I shouldn’t just focus on brevity. We could consider separating key findings: one is that the statement involves a wrong object, and the other is that the proof is incomplete and uses an undefined Ext category.
thinking
**Inspecting the conclusion**

I’m wondering if there’s an unsupported conclusion since braces vanish. But the user seems focused on concentration, though it might not be necessary unless it’s foundational. The output can include findings from later sections too. Since the user mentions exhausting the audit surface, we may need more than just a few examples. I think I should check the etwo-formality theorem around line 864, as it might contain subtle errors related to killing higher braces.
codex
I’ve isolated the main object-identity problems. I’m doing one more pass over the later uses of the `{0,1,2}` concentration claim to see whether the chapter consistently treats it as vanishing range, or whether it silently upgrades it into stronger formality or moduli statements without enough support.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '840,930p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '930,1015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"tangent complex|cohomological amplitude|amplitude\\[|amplitude~|concentrated in degrees|bounded in degrees|total dimension|dimension~2|1\\+t\\"'^2|Hilbert polynomial|P'"\\(t\\)=1\\+t\\"'^2|E_2-formality|Etwo-formality" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   840	\end{remark}
   841	
   842	\begin{example}[Heisenberg specialization]\label{ex:heisenberg-curved-specialization}
   843	For the Heisenberg algebra $\mathcal{H}_k$, the curved $A_\infty$ structure on the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ has $m_0 = -k \cdot \omega$ and $m_n = 0$ for $n \geq 3$: the curvature is the entire obstruction, with no higher operations (\S\ref{sec:frame-genus1}). This is the simplest nontrivial instance of the deformation-obstruction exchange above: $\ChirHoch^2(\mathcal{H}_k) = \mathbb{C}$ (the level deformation) is dual to $\ChirHoch^0(\mathrm{Sym}^{\mathrm{ch}}(V^*))^\vee \otimes \omega_X = \mathbb{C}$ (the center of the dual).
   844	\end{example}
   845	
   846	
   847	%================================================================
   848	% FORMALITY, MODULI, AND OPERADIC PERSPECTIVES ON KOSZULNESS
   849	%================================================================
   850	
   851	\subsection{Formality, moduli, and operadic perspectives on Koszulness}
   852	\label{subsec:formality-moduli-operadic}
   853	
   854	The modular
   855	convolution algebra $\gAmod$ carries the universal Maurer--Cartan
   856	element $\Theta_{\cA}$
   857	(Theorem~\ref{thm:mc2-bar-intrinsic}); every structural property
   858	of~$\cA$ is a property of~$\Theta_{\cA}$. Four
   859	formality-type conditions on~$\gAmod$ and their consequences for
exec
/bin/zsh -lc "rg -n \"\\[m,m\\]|m\\{m\\}|Gerstenhaber bracket gives|brace dg algebra|delta\\(\\Phi\\)|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|ChirHoch\\"'^'"\\*\\(\\\\cA\\) is that tangent complex\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   930	(Theorem~\ref{thm:cech-hca}, Pillar~A) are exact for
   931	$n \geq 3$, and $\Etwo$-formality is automatic from
   932	PBW concentration, not an additional hypothesis.
   933	
   934	The converse ($\Etwo$-formality implies Koszulness) is false.
   935	A non-Koszul algebra whose Hochschild cohomology happens
   936	to concentrate in three degrees would also be $\Etwo$-formal
   937	by the same argument. A stronger converse would require
   938	the scalar-orbit formality problem discussed
   939	below, for which no converse is proved here
   940	\textup{(}Theorem~\textup{\ref{thm:convolution-formality-one-channel}}\textup{)}.
   941	\end{remark}
   942	
   943	\begin{theorem}[Scalar universal class implies convolution
   944	formality along its distinguished orbit;
   945	\ClaimStatusProvedHere]
   946	\label{thm:convolution-formality-one-channel}
   947	\index{formality!convolution algebra}
   948	\index{one-channel!scalar-orbit formality problem}
   949	\index{scalar saturation|see{one-channel}}
 succeeded in 53ms:
chapters/theory/chiral_center_theorem.tex:28:algebra, and neither the center nor the tangent complex
chapters/theory/chiral_center_theorem.tex:50:$\ChirHoch^*(\mathrm{Vir}_c)$ is concentrated in degrees
chapters/theory/chiral_center_theorem.tex:51:$\{0, 2\}$, with total dimension~$2$ and Hilbert series
chapters/theory/chiral_center_theorem.tex:58:cohomological amplitude.
chapters/theory/chiral_center_theorem.tex:60:graded vector space, bounded in degrees $\{0,1,2\}$
chapters/theory/chiral_center_theorem.tex:1881: Thus the total dimension is~$5$. In particular, the older
chapters/theory/chiral_center_theorem.tex:1918: which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
chapters/theory/chiral_center_theorem.tex:1979:Hilbert series and is concentrated in degrees $\{0, 1, 2\}$.
chapters/theory/chiral_center_theorem.tex:1982:$P(t) = 1 + t^2$, giving total dimension~$2$:
chapters/theory/chiral_center_theorem.tex:2088:on the total dimension. The dimension of $\ChirHoch^1$ grows with
chapters/theory/chiral_hochschild_koszul.tex:9:knowing the tangent complex to
chapters/theory/chiral_hochschild_koszul.tex:12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
chapters/theory/chiral_hochschild_koszul.tex:13:Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
chapters/theory/chiral_hochschild_koszul.tex:15:amplitude~$[0,2]$, and the Koszul duality
chapters/theory/chiral_hochschild_koszul.tex:739: (\dim Z(\cA) + \dim Z(\cA^!))(1+t^2)
chapters/theory/chiral_hochschild_koszul.tex:4799:with $\mathcal{B}^! = \mathrm{CE}(\mathfrak{h}_{-k})$ generated by a single element $s\alpha$ in bar degree~1 and its square in bar degree~2. Applying $\mathrm{Hom}_{\mathcal{B}\text{-}\mathcal{B}}(-, \mathcal{B})$ to this length-2 resolution yields a cochain complex concentrated in degrees $0, 1, 2$. Hence $\ChirHoch^n(\mathcal{B}) = 0$ for $n \geq 3$.
chapters/theory/chiral_hochschild_koszul.tex:5255:\begin{definition}[Ambient complementarity tangent complex]
chapters/theory/chiral_hochschild_koszul.tex:5360:dual tangent complex of the other. A cyclic minimal-model
chapters/theory/chiral_hochschild_koszul.tex:5361:transfer upgrades the tangent complex to a $(-1)$-shifted
 exited 2 in 52ms:
rg: regex parse error:
    (?:\[m,m\]|m\{m\}|Gerstenhaber bracket gives|brace dg algebra|delta\(\Phi\)|RHom_\{\mathrm\{ChirAlg\}\}|Ext\^n_\{\mathrm\{ChirAlg\}\}|ChirHoch\^\*\(\cA\) is that tangent complex)
                                                                                       ^^
error: unrecognized escape sequence

thinking
**Considering the definition complexity**

I'm thinking that while the need to inspect something isn't mandatory, it could be interesting to look into the complex definition around 5255. It might relate to shifting conventions, which sounds intriguing. I'll hold off on jumping into it immediately, but it feels worth fetching information on later. There’s certainly a lot to unpack there!
codex
The amplitude issue is real enough that I’m checking the chapter’s own later “tangent complex” definitions, not just the opening paragraph. If the shift convention only appears 5,000 lines later, the opening claim is still ungrounded at the point of use.
exec
/bin/zsh -lc "rg -n \"by definition\\.|precisely \\\\ChirHoch|is precisely \\\\ChirHoch|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|Hom_\\{\\\\text\\{ChirAlg\\}\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '5238,5375p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "ambient complementarity tangent complex|tangent complex|shifted tangent|MC moduli|gauge" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"is that tangent complex|amplitude~\\"'$'"\\[0,2\\]|concentrated in degrees \\\\{0,1,2\\\\}|bounded in degrees \\\\{0,1,2\\\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:by definition\.|precisely \ChirHoch|is precisely \ChirHoch|RHom_\{\mathrm\{ChirAlg\}\}|Ext\^n_\{\mathrm\{ChirAlg\}\}|Hom_\{\text\{ChirAlg\}\})
                                 ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  5238	$\tau_\cA \in \mathrm{MC}(\cA^! \,\widehat{\otimes}\, \cA)$
  5239	be the universal twisting kernel
  5240	(Convention~\ref{conv:bar-coalgebra-identity}). Define
  5241	\[
  5242	K_\cA := (\cA^! \,\widehat{\otimes}\, \cA)[1],
  5243	\]
  5244	with differential twisted by~$\tau_\cA$. The linearizations
  5245	of~$\tau_\cA$ in the $\cA$- and $\cA^!$-directions give maps
  5246	\[
  5247	\nabla_\cA \colon \mathrm{Def}_{\mathrm{cyc}}(\cA)
  5248	\to K_\cA,
  5249	\qquad
  5250	\nabla_{\cA^!} \colon \mathrm{Def}_{\mathrm{cyc}}(\cA^!)
  5251	\to K_\cA.
  5252	\]
  5253	\end{definition}
  5254	
  5255	\begin{definition}[Ambient complementarity tangent complex]
  5256	\label{def:ambient-tangent-complex}
  5257	Define
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:3461:differential $\Dg{g}$ lives in the flat gauge; the
chapters/theory/higher_genus_complementarity.tex:3462:fiberwise differential $\dfib$ lives in the curved gauge.
chapters/theory/higher_genus_complementarity.tex:4610:\begin{definition}[Ambient complementarity tangent complex]
chapters/theory/higher_genus_complementarity.tex:4613:\emph{ambient complementarity tangent complex} is
chapters/theory/higher_genus_complementarity.tex:4636:\item the one-sided tangent complexes
chapters/theory/higher_genus_complementarity.tex:4645:one side with the shifted dual tangent complex of the other, then
chapters/theory/higher_genus_complementarity.tex:4657:For the one-sided tangent complex $T_{\cA}$, the pullback of the ambient
chapters/theory/higher_genus_complementarity.tex:4665:normal complex to one side with the shifted dual tangent complex of the
chapters/theory/higher_genus_complementarity.tex:4677:the tangent complex $T_{\mathrm{comp}}(\cA)$ integrates to a
chapters/theory/higher_genus_complementarity.tex:4705:whose tangent complex is $\fg[1]$.
chapters/theory/higher_genus_complementarity.tex:4720:the one-sided tangent complexes $T_\cA$ and $T_{\cA^!}$ are
chapters/theory/higher_genus_complementarity.tex:4724:algebras whose tangent complexes are Lagrangian
chapters/theory/higher_genus_foundations.tex:396:\item \emph{The uncurving is not a gauge equivalence.}\;
chapters/theory/higher_genus_foundations.tex:397: The passage $\dfib \leadsto \Dg{g}$ is \emph{not} a gauge
chapters/theory/higher_genus_foundations.tex:444:(iii)~A gauge transformation $\dfib \mapsto
chapters/theory/higher_genus_foundations.tex:451:distinction is visible at chain level: gauge-equivalent
chapters/theory/higher_genus_foundations.tex:760:The gauge transformation
chapters/theory/chiral_hochschild_koszul.tex:9:knowing the tangent complex to
chapters/theory/chiral_hochschild_koszul.tex:10:$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
chapters/theory/chiral_hochschild_koszul.tex:12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:12:complex $\ChirHoch^*(\cA)$ is that tangent complex;


thinking
**Inspecting theorem inconsistencies**

I need to take a closer look around line 4544 because something seems off. In the same chapter, theorem H states that \(\ChirHoch^2\) is bounded and not family-specific with huge dimensions. However, at line 4544, there’s a claim regarding \(\mathcal N=4\) SYM, stating \(\ChirHoch^2 = \mathbb{C}^{3(g-1)}\). I’m wondering if \(g\) refers to curvature or spacetime instead of curve genus. While an explorer agent could help find missing definitions or object mismatches, I think I’m good to proceed with the existing evidence for the audit.
thinking
**Inspecting chiral center theorem**

I need to consider inspecting line 1125 in the chiral center theorem, but it may not be necessary. I noticed a potential issue: `thm:operadic-homotopy-convolution` has a status of ProvedElsewhere, not ProvedHere, yet its use in lines 28-32 seems unproblematic. That’s acceptable because the theorem states it's a "strict model of the L_infty deformation object." Everything seems to line up, so I’ll keep that in mind while reviewing the theorem.
codex
I’ve got enough core structural failures to fail the chapter already. I’m doing a final grep-based sweep for unsupported “by definition” moves and degree-convention drift so I can separate genuine mathematical failures from mere stylistic sloppiness.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4536,4548p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '542,548p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4788,4812p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"by definition|is precisely|precisely \\\\ChirHoch|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|Hom_\\{\\\\text\\{ChirAlg\\}\\}|degree-\\"'$1'"\\"'$ bracket|degree '"\\\\"'$-1'"\\\\"'$|degree~'"\\\\\\"'$2'"\\\\\\"'$|concentrated in degrees '"\\\\{0,1,2\\\\}|bounded in degrees \\\\{0,1,2\\\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4536	
  4537	\subsection{Marginal deformations in CFT}
  4538	
  4539	In 2D conformal field theory, $\ChirHoch^2(\mathcal{A})$ classifies marginal deformations
  4540	$S \to S + \lambda \int_{\Sigma} \phi(z,\bar{z}) d^2z$.
  4541	Conformal invariance is preserved when $\phi$ has weight $(1,1)$ (marginality), $[\phi] \in \ChirHoch^2$ is a cocycle (preserving the OPE algebra), and the obstruction in $\ChirHoch^3$ vanishes (extending to all orders).
  4542	
  4543	\begin{example}[Exactly marginal deformations]
  4544	For the free boson, $\ChirHoch^2 = \mathbb{C}$ gives the radius deformation; for $\mathcal{N}=4$ SYM, $\ChirHoch^2 = \mathbb{C}^{3(g-1)}$ gives gauge coupling and theta angles; for minimal models, $\ChirHoch^2 = 0$ (isolated in moduli space).
  4545	\end{example}
  4546	
  4547	\subsection{String field theory}
  4548	
 succeeded in 52ms:
   542	Three algebraic structures now coexist on
   543	$C^\bullet_{\mathrm{ch}}(A, A)$:
   544	the cup product (associative, degree~$2$),
   545	the Gerstenhaber bracket (Lie on the desuspension, degree~$2$),
   546	and the full brace system (all degrees).
   547	The question is whether these structures are compatible
   548	with the differential $\delta = [m, -]$.
 succeeded in 52ms:
  4788	\[\ChirHoch^2(\mathcal{B}) = \mathbb{C} \cdot [k].\]
  4789	
  4790	Here $[k]$ is the cohomology class of the level.
  4791	
  4792	\subsubsection{\texorpdfstring{Higher degrees: $\ChirHoch^n(\mathcal{B})$ for $n \geq 3$}{Higher degrees: HH n(B) for n >= 3}}
  4793	
  4794	For the Heisenberg algebra (free boson), all higher Hochschild cohomology vanishes:
  4795	\[\ChirHoch^n(\mathcal{B}) = 0 \quad \text{for } n \geq 3\]
  4796	
  4797	\emph{Proof.} The Heisenberg algebra $\mathcal{B}$ is chiral Koszul (Theorem~\ref{thm:km-chiral-koszul}): its bar construction $\bar{B}(\mathcal{B})$ is quasi-isomorphic to $\mathrm{CE}(\mathfrak{h}_{-k})$, which is concentrated in bar degrees $\leq 2$ (the only generating relation is the quadratic OPE $\alpha(z)\alpha(w) \sim k/(z-w)^2$, involving exactly two fields). The Koszul resolution therefore has the form:
  4798	\[\mathcal{B} \otimes \mathcal{B}^! \otimes \mathcal{B} \;\xrightarrow{d_2}\; \mathcal{B} \otimes (s\alpha) \otimes \mathcal{B} \;\xrightarrow{d_1}\; \mathcal{B} \otimes \mathcal{B}\]
  4799	with $\mathcal{B}^! = \mathrm{CE}(\mathfrak{h}_{-k})$ generated by a single element $s\alpha$ in bar degree~1 and its square in bar degree~2. Applying $\mathrm{Hom}_{\mathcal{B}\text{-}\mathcal{B}}(-, \mathcal{B})$ to this length-2 resolution yields a cochain complex concentrated in degrees $0, 1, 2$. Hence $\ChirHoch^n(\mathcal{B}) = 0$ for $n \geq 3$.
  4800	
  4801	\subsubsection{Summary for Heisenberg}
  4802	
  4803	\[\ChirHoch^*(\mathcal{B}) = \begin{cases}
  4804	\mathbb{C} & n = 0 \text{ (center = scalars)}\\
  4805	\mathbb{C} & n = 1 \text{ (outer derivation } D(\alpha) = \mathbf{1}\text{)}\\
  4806	\mathbb{C} & n = 2 \text{ (level deformation)}\\
  4807	0 & n \geq 3 \text{ (Koszul resolution length 2)}
 exited 2 in 51ms:
rg: regex parse error:
    (?:by definition|is precisely|precisely \ChirHoch|RHom_\{\mathrm\{ChirAlg\}\}|Ext\^n_\{\mathrm\{ChirAlg\}\}|Hom_\{\text\{ChirAlg\}\}|degree-$1$ bracket|degree \569X1\$|degree~\$2\$|concentrated in degrees \{0,1,2\}|bounded in degrees \{0,1,2\})
                                            ^^
error: unrecognized escape sequence

thinking
**Searching for errors**

I’ve spotted a clear error on lines 544-545, and I think it’d be helpful to search manually instead. Grepping for specific phrases might be simpler. I should consider using separate commands rather than relying on regex, which can be complex and heavy. I want to ensure I'm tracking down issues effectively, so keeping things straightforward definitely seems like the right way to go! Let's simplify this process!
exec
/bin/zsh -lc 'rg -n "by definition" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"degree-\\"'$1'"\\"'$ bracket|degree~'"\\"'$2'"\\"'$|degree '"\\\\"'$-1'"\\\\"'$ bracket|degree'"\\-\\(\\-1\\) Lie bracket|concentrated in degrees \\\\{0,1,2\\\\}|bounded in degrees \\\\{0,1,2\\\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"not by algebraic composition|constant fields|free boson|N=4|\\ChirHoch\\"'^3|curved A_'"\\\\infty-algebra|tangent complex\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"is precisely \\\\ChirHoch|precisely \\\\ChirHoch|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|Hom_\\{\\\\text\\{ChirAlg\\}\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_center_theorem.tex:1611:(by definition~\eqref{eq:mixed-p1} of the universal
chapters/theory/chiral_hochschild_koszul.tex:357:The left side is precisely $\ChirHoch^n(\mathcal{A})$ by definition.
chapters/theory/chiral_hochschild_koszul.tex:3566:$H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ is by definition
chapters/theory/chiral_hochschild_koszul.tex:3590:by definition.
 exited 2 in 53ms:
rg: regex parse error:
    (?:degree-$1$ bracket|degree~$2$|degree \569X1\$ bracket|degree\-\(\-1\) Lie bracket|concentrated in degrees \{0,1,2\}|bounded in degrees \{0,1,2\})
                                            ^^
error: backreferences are not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 exited 2 in 53ms:
rg: regex parse error:
    (?:not by algebraic composition|constant fields|free boson|N=4|\ChirHoch\^3|curved A_\infty-algebra|tangent complex)
                                                                   ^^
error: unrecognized escape sequence
 exited 2 in 53ms:
rg: regex parse error:
    (?:is precisely \ChirHoch|precisely \ChirHoch|RHom_\{\mathrm\{ChirAlg\}\}|Ext\^n_\{\mathrm\{ChirAlg\}\}|Hom_\{\text\{ChirAlg\}\})
                    ^^
error: unrecognized escape sequence

thinking
**Considering command simplification**

I’m thinking about the need for simpler commands. Sometimes, it can be helpful to break things down into more straightforward instructions. It seems that making things less complicated could help users navigate better. I wonder what specific commands could be streamlined for clarity or efficiency. Simplifying could enhance user experience overall. I’ll keep this in mind as I look for ways to improve interactions!
exec
/bin/zsh -lc "grep -n \"RHom_{\\\\mathrm{ChirAlg}}\" -n chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "Ext''^n_{'"\\\\mathrm{ChirAlg}}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "constant fields" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "not by algebraic composition" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 exited 1 in 53ms:

 succeeded in 52ms:
4889:not by algebraic composition.
 succeeded in 52ms:
4871:spatial direction from~$X$. For constant fields:
exec
/bin/zsh -lc "grep -n \"degree-\\"'$1'"\\"'$ bracket" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "ChirAlg" chapters/theory/chiral_hochschild_koszul.tex | head -20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n \"degree~\\"'$2'"\\"'$" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "RHom" chapters/theory/chiral_hochschild_koszul.tex | head -20' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
572:this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
 succeeded in 52ms:
332:C^{\bullet}_{\text{chiral}}(\mathcal{A}) \simeq \text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A})
355:\text{Ext}^n_{\text{ChirAlg}}(\mathcal{A}, \mathcal{A}) = H^n(\text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A}))
572:this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
756:\mathrm{Ext}^n_{\mathrm{ChirAlg}(X)}(\cA, \cA),
 succeeded in 52ms:
875: cup product and degree-$1$ bracket.
 exited 1 in 52ms:


thinking
**Troubleshooting grep command**

I'm trying to manually find `degree2` in the `chiral_center_theorem` using a `grep` command. I attempted `grep -n "degree\\$2\\$"` but it didn't work—might be a formatting issue. I think I should refine my search. Maybe using a command like `grep -n "degree" ... | head` would give me better results. I'm curious if that will help clarify things!
exec
/bin/zsh -lc "grep -n \"curved A_\\\\infty-algebra\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "degree~" chapters/theory/chiral_center_theorem.tex | head -20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "tangent complex" chapters/theory/chiral_hochschild_koszul.tex | head -20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'grep -n "ChirHoch''^3" chapters/theory/chiral_hochschild_koszul.tex | head -20' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 53ms:
4541:Conformal invariance is preserved when $\phi$ has weight $(1,1)$ (marginality), $[\phi] \in \ChirHoch^2$ is a cocycle (preserving the OPE algebra), and the obstruction in $\ChirHoch^3$ vanishes (extending to all orders).
4982:must have degree $2 + 2 - 1 = 3$. But $\ChirHoch^3(\mathcal{B}) = 0$, so:
5028:($\ChirHoch^2$ controls deformations, obstructions in $\ChirHoch^3$).
 succeeded in 53ms:
22:degree~$2$. The naive deformation complex (infinitesimal
95: A multilinear operation of degree~$n$ depends on
135: degree~$|f|$ is a graded-linear map
221: arises from commuting~$g$ (of suspended degree~$\|g\|$)
319:\item The \emph{internal degree} is the degree~$k$
341:(degree $|m_k| = 2 - k$ gives total degree~$1$),
382:of degree~$p$ (i.e., $f \in \End^{\mathrm{ch}}_A(p)$)
469: degree~$\|g_j\|$) past:
523:simply $f$ itself). Precisely, for $f$ of degree~$p$ and
524:$g$ of degree~$q$:
544:the cup product (associative, degree~$2$),
545:the Gerstenhaber bracket (Lie on the desuspension, degree~$2$),
915:C^1_{\mathrm{ch}}(A, A)$ has total degree~$1$, hence
1061:arises from commuting $m$ (of suspended degree~$0$) past
1181: operation: an element $b_j \in B$ of degree~$k_j$
1372:For $b \in B$ of degree~$n$ (meaning $b$ participates in
1707:$f$ and $g$ are $\delta$-closed and of suspended degree~$-1$
1892: bar degree~$1$ \textup{(}chiral Koszulness\textup{)}, so the
1935:concentrated in bar degree~$1$.
1983:one copy of~$\bC$ in degree~$0$ (the vacuum) and one copy
 succeeded in 53ms:
9:knowing the tangent complex to
12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
5255:\begin{definition}[Ambient complementarity tangent complex]
5360:dual tangent complex of the other. A cyclic minimal-model
5361:transfer upgrades the tangent complex to a $(-1)$-shifted



thinking
**Analyzing algebraic theorems**

I’m looking at lines 4541 and 5028, which mention \(\ChirHoch^3\) as an obstruction. Given Theorem H states it vanishes on the Koszul locus, perhaps the context needs clarification, especially regarding modular Koszul algebras. It seems contradictory if that obstruction is mentioned without qualification. The statement in line 4544 introduces unsupported claims about 4d gauge theory in volume I, making it necessary to clarify these aspects. I should include a note on medium to address these subtle issues.
thinking
**Correcting references in content**

I need to fix the example in line 4544, either by deleting it or moving it to Volume II with proper context, since AGENTS architecture indicates all physics should be there. This connects to the cross-volume scope rule, so I'm focused on what's actually read. Additionally, the usage of `Theorem\ref{thm:km-chiral-koszul}` in line 4797 incorrectly references the Heisenberg algebra, which shouldn't cite an affine Kac-Moody theorem. I need to clarify this false reference to ensure accuracy.
thinking
**Updating theorems for accuracy**

I need to correct the reference in the content to the appropriate Heisenberg Koszul theorem. It looks like it should be `thm:frame-heisenberg-koszul-dual` or something from the free_fields section. It's crucial to ensure that the citation matches the relevant theorem accurately so that everything is consistent and reliable. Making this change will help improve the clarity and integrity of the work!
codex
I’ve found a few second-order leaks now: wrong degree conventions, a false “concentration implies formality” upgrade, and at least one citation that points to the wrong family entirely. I’m checking the exact Heisenberg/Koszul label before I lock the final finding list.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '5000,5032p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Heisenberg.*Koszul|Koszul dual.*Heisenberg|chiral Koszul.*Heisenberg|Heisenberg.*chiral Koszul|thm:.*heisenberg.*koszul|prop:.*heisenberg.*koszul" chapters metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4538,4546p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1080,1115p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
metadata/theorem_registry.md:94:| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1156 | Heisenberg Koszul dual |
metadata/theorem_registry.md:1460:| `thm:heisenberg-koszul-dual-early` | `theorem` | 1970 | Heisenberg Koszul dual |
metadata/theorem_registry.md:2238:| `prop:heisenberg-koszul-epstein` | `proposition` | 5462 | Degenerate case: Heisenberg |
chapters/examples/heisenberg_eisenstein.tex:290:The Heisenberg algebra and its Koszul dual satisfy exact
chapters/examples/heisenberg_eisenstein.tex:306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
chapters/examples/yangians_computations.tex:199:reduces to the Heisenberg Koszul duality
chapters/examples/yangians_computations.tex:2063:(Theorem~\ref{thm:heisenberg-koszul-dual-early}).
chapters/examples/landscape_census.tex:1373:\item \emph{Heisenberg}: Koszul dual is the commutative chiral algebra
chapters/examples/landscape_census.tex:1376:(Theorem~\ref{thm:heisenberg-koszul-dual-early}).
chapters/examples/landscape_census.tex:1997: The Heisenberg and free fermion Koszul duals grow
chapters/examples/landscape_census.tex:2080:Among the Koszul chiral algebras in Table~\textup{\ref{tab:bar-dimensions}}, the Koszul dual Hilbert function $\dim (\cA^!)_n$ grows sub-exponentially if and only if $\cA$ is a free field (Heisenberg or free fermion) or affine $\widehat{\mathfrak{sl}}_2$ (which has linear growth $2n{+}1$). All other interacting algebras (higher-rank Kac--Moody, Virasoro, $\mathcal{W}_3$, $bc$, $\beta\gamma$, Yangian) have exponential growth.
chapters/examples/landscape_census.tex:2090:For every interacting algebra in Table~\textup{\ref{tab:bar-dimensions}} with a known closed-form generating function, that function is algebraic over $\mathbb{Q}(x)$. (The free-field algebras, Heisenberg and free fermion, have transcendental partition-graded generating functions $\prod(1-x^k)^{-1}$, though their conformal-weight-graded series are rational.) For interacting algebras, this algebraicity is a consequence of the Koszul property: the bar spectral sequence collapse at $E_2$ (Theorem~\ref{thm:spectral-sequence-collapse}) constrains the generating function to satisfy a polynomial equation.
chapters/examples/landscape_census.tex:3988: Koszul dual (Theorem~\ref{thm:heisenberg-koszul-dual-early}),
chapters/examples/genus_expansions.tex:3481:The Heisenberg generating function $\sum_g F_g x^{2g} = k \cdot ((x/2)/\sin(x/2) - 1)$ from \S\ref{sec:frame-genus-tower} was a product of two factors: the curvature $\kappa = k$ and a universal series in~$x$. This factorization holds for uniform-weight modular Koszul algebras at all genera, and unconditionally at genus~$1$; the universal factor is the modified Todd class.
chapters/examples/lattice_foundations.tex:903:by Theorem~\ref{thm:heisenberg-koszul-dual-early}).
chapters/examples/lattice_foundations.tex:1016:By the Heisenberg bar-cobar quasi-isomorphism (Theorem~\ref{thm:heisenberg-koszul-dual-early}, applied to $\cH_d$), the twisted complex for the Heisenberg algebra is acyclic: $H^*(\barBgeom(\cH_d) \otimes_\tau \cH_d) = 0$ in positive degree. Hence $E_1^{p,q} = 0$ for $p+q > 0$, and the spectral sequence collapses at $E_1$.
chapters/examples/lattice_foundations.tex:1034:by Theorem~\ref{thm:heisenberg-koszul-dual-early}. Self-duality is a special
chapters/examples/lattice_foundations.tex:1063:(Theorem~\ref{thm:heisenberg-koszul-dual-early}).
chapters/examples/lattice_foundations.tex:1098:Theorem~\ref{thm:heisenberg-koszul-dual-early},
chapters/examples/lattice_foundations.tex:1121: (Theorem~\ref{thm:heisenberg-koszul-dual-early}):
 succeeded in 53ms:
  5000	bracket). Formal deformations are MC elements
  5001	$\gamma \in \ChirHoch^2(\cA)[[\hbar]]$ satisfying
  5002	$\sum_{n \geq 1} \frac{1}{n!}\ell_n(\gamma, \ldots, \gamma) = 0$.
  5003	\end{remark}
  5004	
  5005	\subsection{Computational strategy}
  5006	
  5007	\begin{remark}[Computing \texorpdfstring{$\ChirHoch^*$}{CH^*} in practice]\label{rem:compute-HH}
  5008	To compute $\ChirHoch^n(\mathcal{A})$ for a chiral algebra given by generators and OPE data, one proceeds as follows: (1) construct the bar complex $\bar{B}^n(\mathcal{A})$ using configuration space integrals; (2) build the cobar complex $\Omega(\bar{B}(\mathcal{A}))$ by inserting distributional duals; (3) form the Hom complex $\operatorname{Hom}(\Omega(\bar{B}(\mathcal{A})), \mathcal{A})$; (4) compute cohomology $\ker(d)/\operatorname{im}(d)$ at each degree. For Koszul algebras, the concentration of the bar coalgebra $\bar{B}(\mathcal{A})$ (whose dual is~$\mathcal{A}^!$) reduces the computation to lower-dimensional complexes.
  5009	\end{remark}
  5010	
  5011	\begin{remark}[Noncommutative Hodge degeneration]\label{rem:nc-hodge-degeneration}
  5012	\index{noncommutative Hodge theory}
  5013	The pole-order filtration on the chiral Hochschild complex degenerates
  5014	at $E_1$ for Koszul algebras
  5015	(Theorem~\ref{thm:spectral-sequence-collapse}), giving a mixed
  5016	structure analogous to Kaledin's noncommutative Hodge
  5017	theory~\cite{Kal08}. Theorem~C (complementarity) is Verdier duality in
  5018	this setting, exchanging the Hodge filtrations of $\cA$ and~$\cA^!$.
  5019	\end{remark}
 succeeded in 51ms:
  4538	
  4539	In 2D conformal field theory, $\ChirHoch^2(\mathcal{A})$ classifies marginal deformations
  4540	$S \to S + \lambda \int_{\Sigma} \phi(z,\bar{z}) d^2z$.
  4541	Conformal invariance is preserved when $\phi$ has weight $(1,1)$ (marginality), $[\phi] \in \ChirHoch^2$ is a cocycle (preserving the OPE algebra), and the obstruction in $\ChirHoch^3$ vanishes (extending to all orders).
  4542	
  4543	\begin{example}[Exactly marginal deformations]
  4544	For the free boson, $\ChirHoch^2 = \mathbb{C}$ gives the radius deformation; for $\mathcal{N}=4$ SYM, $\ChirHoch^2 = \mathbb{C}^{3(g-1)}$ gives gauge coupling and theta angles; for minimal models, $\ChirHoch^2 = 0$ (isolated in moduli space).
  4545	\end{example}
  4546	
 succeeded in 52ms:
  1080	exactly the non-scalar shadow obstruction tower
  1081	(\S\ref{subsec:non-scalar-theta}); the second is the
  1082	higher-genus curvature.
  1083	\end{remark}
  1084	
  1085	\begin{conjecture}[MC moduli smoothness at the Koszul locus;
  1086	\ClaimStatusConjectured]
  1087	\label{conj:mc-moduli-smoothness}
  1088	\index{Maurer--Cartan!moduli smoothness}
  1089	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  1090	with universal MC element $\Theta_{\cA} \in \MC(\gAmod)$
  1091	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
  1092	Then $\cA$ is chirally Koszul if and only if
  1093	\begin{equation}\label{eq:mc-smoothness}
  1094	H^2\!\bigl(\gAmod,\,
  1095	 \operatorname{ad}(\Theta_{\cA})\bigr)
  1096	\;=\; 0,
  1097	\end{equation}
  1098	i.e.\ the MC moduli stack $\MC(\gAmod)$ is smooth
  1099	at~$\Theta_{\cA}$.

thinking
**Analyzing differential title issues**

I’m considering the title “[The chiral Hochschild differential; \ClaimStatusProvedHere]” which seems a bit off for a proper macro. Maybe extracting metadata isn't necessary here. There could be unresolved references like `Construction\ref{const:gerstenhaber-bracket}`. Oh, and there's a potential issue with line 4917 concerning the `gerstenhaber-cohomology` in the chiral center theorem, which seems fine. However, there's a theorem statement that calls for degree -1, making `ChirHoch^*` a Lie algebra, but that phrasing could be clearer.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4878,4890p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '748,762p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '132,138p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '104,112p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   132	shifted-symplectic space built from
   133	$H^*(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$. At the
   134	Hochschild level, Koszul duality exchanges deformations and
   135	obstructions:
   136	$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
   137	(Remark~\ref{rem:nc-hodge-degeneration}).
   138	
 succeeded in 53ms:
  4878	\begin{theorem}[Chiral Gerstenhaber structure on $\ChirHoch^*$;
  4879	\ClaimStatusProvedHere]\label{thm:gerstenhaber-structure}
  4880	\index{Gerstenhaber bracket!chiral|textbf}
  4881	The chiral Hochschild cohomology carries a degree $-1$
  4882	bracket (the \emph{chiral Gerstenhaber bracket}):
  4883	\[[\cdot, \cdot]: \ChirHoch^p(\mathcal{A}) \otimes \ChirHoch^q(\mathcal{A}) \to \ChirHoch^{p+q-1}(\mathcal{A}),\]
  4884	making $\ChirHoch^*(\mathcal{A})$ into a graded Lie algebra.
  4885	This is the chiral analogue of Gerstenhaber's classical
  4886	bracket~\cite{Ger63} on associative Hochschild cochains;
  4887	it is computed by OPE residues on configuration spaces
  4888	\textup{(}Construction~\textup{\ref{const:gerstenhaber-bracket}}\textup{)},
  4889	not by algebraic composition.
  4890	\end{theorem}
 succeeded in 53ms:
   748	\end{enumerate}
   749	\end{theorem}
   750	
   751	\begin{proof}
   752	Part~(a): by Theorem~\ref{thm:hochschild-bar-cobar},
   753	\[
   754	\ChirHoch^n(\cA)
   755	\;=\;
   756	\mathrm{Ext}^n_{\mathrm{ChirAlg}(X)}(\cA, \cA),
   757	\]
   758	so $\ChirHoch^n(\cA)=0$ for $n<0$. For $n>2$,
   759	Theorem~\ref{thm:main-koszul-hoch} gives
   760	\[
   761	\ChirHoch^n(\cA)
   762	\;\cong\;
 succeeded in 52ms:
   104	\end{split}
   105	\end{equation}
   106	This is a cocycle condition: $\phi$ is closed in a complex whose
   107	differential is built from~$\mu$ via the residue operations above.
   108	That complex is the \emph{chiral Hochschild complex}
   109	$C^{\bullet}_{\mathrm{chiral}}(\mathcal{A})$, constructed in
   110	\S\ref{subsec:hochschild-duality}.
   111	
   112	The cocycle condition~\eqref{eq:deformation-cocycle} involves three
exec
/bin/zsh -lc "rg -n \"label\\{thm:e2-formality\\}|thm:e2-formality\" chapters metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "sec:frame-genus1|sec:frame-koszul-dual" chapters metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:km-chiral-koszul" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1346,1354p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/chiral_hochschild_koszul.tex:904:(Theorem~\ref{thm:e2-formality}) applied to the configuration-space
chapters/theory/en_koszul_duality.tex:956:\label{thm:e2-formality}
 succeeded in 53ms:
396:| `thm:km-chiral-koszul` | `theorem` | 760 | Affine Kac--Moody algebras are chiral Koszul |
 succeeded in 53ms:
chapters/examples/yangians_foundations.tex:500:For the Heisenberg algebra, Koszul duality exchanged Lie-type and Com-type: $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (\S\ref{sec:frame-koszul-dual}). In the Yangian setting, both sides are associative ($\Eone$), and Verdier duality inverts the $R$-matrix instead of exchanging operadic types.
chapters/examples/kac_moody.tex:501:For the Heisenberg algebra, Koszul duality sends the Lie-type $\mathcal{H}_k$ to the Com-type $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (\S\ref{sec:frame-koszul-dual}): the dual algebra changes type. For non-abelian Kac--Moody algebras, Koszul duality shifts the level: the Koszul dual is $(\widehat{\mathfrak{g}}_k)^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$, the chiral Chevalley--Eilenberg algebra at level $k' = -k - 2h^\vee$, sharing the same modular characteristic as $\widehat{\mathfrak{g}}_{k'}$ but distinct from it as a chiral algebra.
chapters/examples/genus_expansions.tex:128:\S\ref{sec:frame-genus1} and the genus tower of \S\ref{sec:frame-genus-tower}.
chapters/frame/heisenberg_frame.tex:202:\textbf{A}~(\S\ref{sec:frame-koszul-dual}): $\mathcal{H}_k^! = (\mathrm{Sym}^{\mathrm{ch}}(V^*), m_0 = -k\omega)$.
chapters/frame/heisenberg_frame.tex:1074:\section{Reading off the Koszul dual}\label{sec:frame-koszul-dual}
chapters/frame/heisenberg_frame.tex:1351:\label{sec:frame-genus1}
chapters/frame/heisenberg_frame.tex:4541: (\S\ref{sec:frame-koszul-dual},
chapters/frame/heisenberg_frame.tex:4551: (\S\ref{sec:frame-genus1}).
chapters/frame/heisenberg_frame.tex:4697:(\S\ref{sec:frame-genus1}). Operadically,
chapters/theory/higher_genus_foundations.tex:2867:At genus~$0$, the Arnold relation $\mathcal{A}_3^{(0)} = 0$ was the mechanism ensuring $\dzero^2 = 0$ in the Heisenberg bar complex (\S\ref{sec:frame-bar-deg2}). At genus~$1$, the Arnold $3$-form acquires a correction proportional to the volume form; this is the geometric origin of the fiberwise curvature $\dfib^{\,2} = \kappa \cdot \omega_1$ that we computed in~\S\ref{sec:frame-genus1}.
chapters/theory/higher_genus_foundations.tex:4080:For the Heisenberg algebra on $E_\tau$, we saw in~\S\ref{sec:frame-genus1} that the
chapters/theory/chiral_hochschild_koszul.tex:843:For the Heisenberg algebra $\mathcal{H}_k$, the curved $A_\infty$ structure on the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ has $m_0 = -k \cdot \omega$ and $m_n = 0$ for $n \geq 3$: the curvature is the entire obstruction, with no higher operations (\S\ref{sec:frame-genus1}). This is the simplest nontrivial instance of the deformation-obstruction exchange above: $\ChirHoch^2(\mathcal{H}_k) = \mathbb{C}$ (the level deformation) is dual to $\ChirHoch^0(\mathrm{Sym}^{\mathrm{ch}}(V^*))^\vee \otimes \omega_X = \mathbb{C}$ (the center of the dual).
chapters/theory/chiral_koszul_pairs.tex:674:prototype (\S\ref{sec:frame-koszul-dual}).
chapters/theory/chiral_koszul_pairs.tex:702:(\S\ref{sec:frame-koszul-dual}).
chapters/theory/chiral_koszul_pairs.tex:3966:For the Heisenberg algebra, reading off the Koszul dual from the bar coalgebra was immediate: the bar was $\mathrm{coLie}^{\mathrm{ch}}(V^*)$, so the dual was $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (\S\ref{sec:frame-koszul-dual}). The following definition extends this to algebras with multiple generators and non-trivial relations.
chapters/theory/introduction.tex:439:(\S\ref{sec:frame-koszul-dual}).
chapters/theory/introduction.tex:452:see~\S\ref{sec:frame-koszul-dual}).
chapters/theory/bar_cobar_adjunction_curved.tex:5667:For the Heisenberg algebra on an elliptic curve (\S\ref{sec:frame-genus1}), the curvature element $\mu_0 = k \cdot \mathbf{1}$ is scalar, hence central. Centrality of the curvature element is the general mechanism ensuring $d_{\mathrm{bar}}^2 = 0$ strictly in the curved setting.
chapters/theory/cobar_construction.tex:504:The bar complex used logarithmic forms on \emph{compactified} configuration spaces; the cobar uses distributions on \emph{open} configuration spaces. For the Heisenberg algebra (\S\ref{sec:frame-koszul-dual}), the cobar of $\mathrm{coLie}^{\mathrm{ch}}(V^*)$ produced $\mathrm{Sym}^{\mathrm{ch}}(V^*)$; the following definition gives the general construction.
chapters/theory/poincare_duality.tex:300:in \S\ref{sec:frame-koszul-dual}.
 succeeded in 52ms:
  1346	with coproduct:
  1347	\[
  1348	\Delta([\alpha^n]) = \sum_{i+j=n} [\alpha^i] \otimes [\alpha^j]
  1349	\]
  1350	
  1351	This is the divided power coalgebra $\Gamma(V^*)$, which is the Koszul dual \emph{coalgebra}. Its linear dual is the symmetric algebra $\mathrm{Sym}(V)$, and the Koszul dual \emph{algebra} is $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (Part~\ref{part:characteristic-datum}, the characteristic datum), confirming that the Heisenberg algebra is Koszul (Theorem~\ref{thm:km-chiral-koszul}) but \emph{not} Koszul self-dual. (The cobar $\Omega(\bar{B}(\mathcal{H}_\kappa))$ recovers $\mathcal{H}_\kappa$ itself.)
  1352	\end{proof}
  1353	
  1354	\subsection{Computing Hochschild cohomology}
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '944,968p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1690,1735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4808,4811p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4867,4874p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   944	This result is the higher-dimensional analogue of the PBW theorem
   945	and the classical bar-CE comparison. At $n = 2$, the $\Etwo$
   946	enveloping algebra $U_2(\fg)$ is the topological shadow of the
   947	chiral universal enveloping algebra
   948	$\widehat{U}(\fg_k) = V_k(\fg)$ (the vacuum module). Knudsen's
   949	Koszul duality at $n = 2$ is the topological shadow of our chiral
   950	Koszul duality.
   951	
   952	
   953	\subsection{Kontsevich formality and deformation quantization}
   954	
   955	\begin{theorem}[Formality of \texorpdfstring{$\Etwo$}{E2}; \ClaimStatusProvedElsewhere]
   956	\label{thm:e2-formality}
   957	\index{formality!$\Etwo$ operad}
   958	\textup{(}Kontsevich~\cite{Kon03},
   959	Tamarkin~\cite{Tamarkin00}\textup{)}\quad
   960	The $\Etwo$ operad is formal over $\bQ$: there is a
   961	quasi-isomorphism of operads
   962	\[
   963	C_*(\Etwo;\, \bQ)
 succeeded in 50ms:
  1690	\end{corollary}
  1691	
  1692	\begin{proof}
  1693	The identification $Z_{\mathrm{ch}}(A) = H^0(C^\bullet_{\mathrm{ch}})$
  1694	is tautological. The commutativity of the cup product
  1695	on $H^0$ follows from the Gerstenhaber bracket identity:
  1696	for $f, g \in C^0_{\mathrm{ch}}$ with $\delta f = \delta g = 0$,
  1697	\[
  1698	f \smile g - (-1)^{|f||g|} g \smile f
  1699	= [f, g]
  1700	= \delta h
  1701	\]
  1702	for some $h \in C^{-1}_{\mathrm{ch}}$ (the bracket of
  1703	two cocycles is a coboundary by the standard Gerstenhaber
  1704	algebra identity), so the cup product is commutative on
  1705	cohomology. More precisely, $[f,g] = f\{g\} - (-1)^{\|f\|\|g\|}g\{f\}$
  1706	and the pre-Lie relation shows this is $\delta$-exact when
  1707	$f$ and $g$ are $\delta$-closed and of suspended degree~$-1$
  1708	(i.e., $|f| = |g| = 0$).
  1709	\end{proof}
 succeeded in 51ms:
  4808	\end{cases}\]
  4809	
  4810	The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
  4811	\end{example}
 succeeded in 52ms:
  4867	\begin{remark}[Chiral vs.\ classical]\label{rem:chiral-vs-classical-hochschild}
  4868	Chiral $\ChirHoch^*$ differs from classical
  4869	$HH^n_{\text{classical}}(A) = \mathrm{Ext}^n_{A^e}(A,A)$ by locality,
  4870	configuration-space integrals, differential-form coefficients, and the
  4871	spatial direction from~$X$. For constant fields:
  4872	$\ChirHoch^n(\mathcal{A})|_{\text{constant}} \cong
  4873	HH^n_{\text{classical}}(H^0(\mathcal{A}))$.
  4874	\end{remark}
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '955,975p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   955	\begin{theorem}[Formality of \texorpdfstring{$\Etwo$}{E2}; \ClaimStatusProvedElsewhere]
   956	\label{thm:e2-formality}
   957	\index{formality!$\Etwo$ operad}
   958	\textup{(}Kontsevich~\cite{Kon03},
   959	Tamarkin~\cite{Tamarkin00}\textup{)}\quad
   960	The $\Etwo$ operad is formal over $\bQ$: there is a
   961	quasi-isomorphism of operads
   962	\[
   963	C_*(\Etwo;\, \bQ)
   964	\;\simeq\;
   965	H_*(\Etwo;\, \bQ).
   966	\]
   967	Consequently, every $\Etwo$-algebra structure on a
   968	cochain complex $A$ is determined up to quasi-isomorphism by the
   969	induced $H_*(\Etwo)$-algebra structure on cohomology.
   970	\end{theorem}
   971	
   972	\begin{remark}[Formality and deformation quantization]
   973	\label{rem:formality-dq}
   974	\index{deformation quantization!from $\Etwo$ formality}







thinking
**Considering finding issues**

I'm thinking about pairing with a specific line regarding "degree convention drift" across different files. It seems like severity could be medium. The user wants the exact format, which complicates things since it demands a single file:line format. There are some potential issues with different concepts being used, like the quasi-isomorphism. I'm also recognizing that some theorems may need to be properly labeled, possibly as propositions or remarks. I might mention overlaps in findings for clarity.
thinking
**Identifying a problem**

I see that there's an issue with the chapter redefining Chirhoch as Hom/Ext/RHom within the category of chiral algebras. This contradicts the established End^{ch}_A-based definition mentioned earlier at [chiral_center_theorem:298-343]. Notably, there's also no comparison theorem stated to bridge this gap. It's essential to address this contradiction to ensure clarity in the definitions used throughout the work and maintain consistency in the theoretical framework.
thinking
**Addressing physics inconsistencies**

I see a problem with the unscoped 4D physics example and the gauge-coupling dimension formula—they're in a volume-I chapter, but they lack the necessary supporting setup or citation. To fix this, I think it's best to either delete this example or move it to Volume II, where it can be better contextualized with an appropriate citation. Let’s consider how this change could improve clarity for readers!
thinking
**Considering findings and summaries**

I'm thinking about the findings on line 4810 regarding algebras and outer derivations. It seems broad. I wonder if I could simplify. The user asked about both insertions, and it turns out the bracket formula is correct. Should I include that in the summary or mention its absence as a finding? The structured contract states the summary should contain findings only, but I want to reassure the user about its completeness. I need to balance formatting with clarity.
thinking
**Summarizing findings clearly**

I'm considering a concise summary: "There is no surviving finding indicating that the formula `[f,g]=f\{g\}-(-1)^{...}g\{f\}` omits the second insertion; that aspect exists in the imported definition." But since the contract specifies that only summary counts matter, I might want to stick to essentials without extra details. The instructions seem to emphasize presenting findings first and then offering a summary, which makes me think clearly structuring this will benefit the user.
thinking
**Providing exact fixes**

The user wants clear, precise instructions—like inserting definitions or making specific changes. I realized I could suggest replacing lines with direct formulas rather than giving general guidance. For example, I could say, "Replace theorem statement lines 328-333 with `C^\bullet_{ch}(\A,\A) \xrightarrow{\sim} \Conv(\bar B^{ch}(\A),\A)`." It seems beneficial to provide exact replacement formulas for clarity and accuracy. This way, the user gets exactly what they need!
thinking
**Refining findings and summaries**

I’m moving N=4 to Volume II, which feels like a good decision. Next, I need to fix the centrality for 16 and summarize: "Checked: 8 | Findings: 16 | Verdict: FAIL," which seems appropriate. I want to be cautious not to overstate how it "redefines Chirhoch"—it might just introduce models. I’m also considering whether there's a potential issue with `\text{Hom}_{\text{ChirAlg}}` lacking an underline. Maybe this could strengthen our findings. Lastly, I'll mention the theorem in line 332 should use `\Conv` instead of `Hom_{ChirAlg}`.
codex
- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:324 — PROBLEM: The chapter replaces the canonical chiral Hochschild complex by `\text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\A)),\A)` and then upgrades that to `\Ext_{\mathrm{ChirAlg}}` / `\RHom_{\mathrm{ChirAlg}}` “by definition” at lines 355-357, 572-573, and 754-756. The canonical definition actually read in [chiral_center_theorem.tex:298-343] is `C^\bullet_{\mathrm{ch}}(A,A)=\prod_{k\ge0}\End^{\mathrm{ch}}_A(k)[1-k]` with differential `\delta=[m,-]`. No comparison theorem is stated before the substitution. FIX: Insert the canonical definition at the start of this chapter:
  `\ChirHoch^\bullet(\A):=H^\bullet(C^\bullet_{\mathrm{ch}}(\A,\A)),\quad C^\bullet_{\mathrm{ch}}(\A,\A)=\prod_{k\ge0}\End^{\mathrm{ch}}_\A(k)[1-k].`
  Then restate Theorem~324 as a comparison theorem, e.g.
  `C^\bullet_{\mathrm{ch}}(\A,\A)\simeq \Conv(\bar B^{\mathrm{ch}}(\A),\A)` (or the precise dg Hom-complex you intend), and replace every “by definition” equality with “via the quasi-isomorphism of Theorem~\ref{thm:hochschild-bar-cobar}”.

- [CRITICAL] chapters/theory/higher_genus_foundations.tex:2672 — PROBLEM: `def:bigraded-hochschild` names a new object “the bigraded chiral Hochschild complex” but defines it as `R\mathrm{Hom}_{\mathcal D_{\overline C_{p+2}(X)}}(\A^{\boxtimes(p+2)},\omega_{\overline C_{p+2}(X)})`. That is a Verdier/derived-Hom model, not the canonical `End^{\mathrm{ch}}_A` cochain complex, and no comparison theorem identifies the two before `chiral_hochschild_koszul.tex` uses this definition as Theorem H’s input. FIX: Rename this definition to “Verdier-dual bar model for chiral Hochschild,” then add an explicit proposition immediately after it proving/citing
  `CH^{p,\bullet}_{\mathrm{Verd}}(\A)\simeq \operatorname{gr}_p C^\bullet_{\mathrm{ch}}(\A,\A)`,
  and only after that define `RHH_{\mathrm{ch}}(\A)` as the same object.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145 — PROBLEM: The local “geometric realization” defines a degree-`n` cochain using only `\overline C_{n+2}(X)` and fixed `n`-forms. That collapses arity/bar degree and cochain degree into one index, contradicting both the canonical bigrading in [chiral_center_theorem.tex:298-333] and the later imported bigraded model [higher_genus_foundations.tex:2672-2688]. FIX: Replace lines 143-157 by a genuinely bigraded definition, e.g.
  `\mathcal F^{p,q}_{\mathrm{ch}}(\A):=R\Gamma(\overline C_{p+2}(X), j_*j^*\A^{\boxtimes(p+2)}\otimes \Omega^q_{\overline C_{p+2}(X)}(\log D))`,
  and then set
  `\ChirHoch^\bullet(\A)=\Tot(\bigoplus_{p\ge0}\mathcal F^{p,\bullet}_{\mathrm{ch}}[-p])`.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:282 — PROBLEM: The proof of `thm:chiral-hochschild-differential` asserts that `d_{\mathrm{dR}}\eta_{12}` is “supported on the boundary divisor” and decomposes into boundary residues. Two paragraphs earlier `d_{\text{config}}` was defined as the ordinary de Rham differential, and `\eta_{12}=d\log(z_1-z_2)` is closed on configuration space. As written, the key cancellation step is false. FIX: Delete lines 282-289 and replace them with a correct boundary argument: either work in the logarithmic de Rham complex with explicit residue maps, or cite `thm:arnold-relations` to state that the codimension-2 boundary contributions from the three collision strata cancel in the Stokes formula. Do not write `d_{\mathrm{dR}}\eta_{12}` as a boundary current unless that extension is defined first.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:123 — PROBLEM: The file states `d_{\mathrm{fib}}^{\,2}=\kappa(\A)\omega_g`, then concludes “the bar complex is a curved `A_\infty`-algebra.” That is the wrong object. In this repo the bar complex is a coalgebra; curvature belongs to the fiberwise/dual curved structure, not to “the bar complex as an `A_\infty`-algebra.” FIX: Replace lines 123-127 with: “At genus `g\ge1`, the fiberwise differential satisfies `d_{\mathrm{fib}}^{\,2}=\kappa(\A)\omega_g`. This is the curved gauge on the genus-`g` fibre; the bar differential on `B(\A)` remains square-zero as a coalgebra differential, while the dual/Koszul-dual algebra acquires the corresponding curved `A_\infty` structure.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:362 — PROBLEM: The spectral-sequence theorem is not built on the object actually defined above. `E_0^{n,q}` is written as plain global sections, `d_0` is called “sheaf cohomology,” `\ChirHoch^{m,*}` appears without prior definition, and the proof never constructs a double complex whose vertical differential is sheaf cohomology. FIX: Restate this as the hypercohomology spectral sequence of the corrected sheaf complex:
  `E_1^{p,q}=H^q(\overline C_{p+2}(X),\mathcal F_p^\bullet)\Rightarrow \mathbb H^{p+q}(\Tot\mathcal F_\bullet^\bullet)`,
  define `\mathcal F_p^\bullet` explicitly, and remove `d_{\mathrm{sheaf}}` as if it were an honest differential on `\Gamma`.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:864 — PROBLEM: The proof of `prop:e2-formality-hochschild` does not prove the claim it states. The degree count at lines 886-896 does not kill ternary operations, and “collapse at `E_2` forces higher `E_2`-operations to be coboundaries” is asserted without mechanism. The statement also mislabels the Gerstenhaber bracket as “degree-`1`” at line 875. FIX: Replace the proof with a direct citation to [en_koszul_duality.tex:955-969] plus [chiral_center_theorem.tex:1714-1723]: operad formality identifies `E_2`-algebras up to quasi-isomorphism by their induced Gerstenhaber structure on cohomology. Then change line 875 to “degree-`(-1)` bracket” or “degree-`0` bracket on `H^*(\ChirHoch(\A))[1]`.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4881 — PROBLEM: The bracket theorem gets the structure wrong twice. A degree `-1` bracket does not make `\ChirHoch^\bullet(\A)` itself a graded Lie algebra; it makes `\ChirHoch^\bullet(\A)[1]` a graded Lie algebra, or `\ChirHoch^\bullet(\A)` a Gerstenhaber algebra. The sentence “not by algebraic composition” at line 4889 also contradicts the proof and the imported definition [chiral_center_theorem.tex:501-516], where the bracket is the antisymmetrized single-brace operadic composition. FIX: Replace lines 4881-4889 with: “The chiral Hochschild cohomology carries a degree `-1` Gerstenhaber bracket; equivalently `\ChirHoch^\bullet(\A)[1]` is a graded Lie algebra. Geometrically, this bracket is realized by OPE residues on configuration spaces, which coincide with the antisymmetrized single-brace operadic compositions.”

- [HIGH] chapters/theory/chiral_center_theorem.tex:544 — PROBLEM: The imported degree conventions are plainly wrong: the cup product and the Gerstenhaber bracket are both described as “degree~`2`.” That conflicts with the local bracket definition [chiral_center_theorem.tex:501-516] and the cohomology statement [chiral_center_theorem.tex:1714-1723]. FIX: Replace lines 544-546 with: “the cup product (associative, cohomological degree `0`), the Gerstenhaber bracket (degree `-1` on `C^\bullet_{\mathrm{ch}}`, degree `0` on `C^\bullet_{\mathrm{ch}}[1]`), and the full brace system.”

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4797 — PROBLEM: The Heisenberg example uses the wrong family reference and the wrong model. It cites `thm:km-chiral-koszul`, whose registry entry is “Affine Kac--Moody algebras are chiral Koszul,” to justify a Heisenberg claim; the same miscitation recurs at line 1351. Then line 4799 computes `\ChirHoch` by applying `\Hom_{\mathcal B-\mathcal B}(-,\mathcal B)` to a bimodule resolution, which is exactly the classical `A^e`-style move this chapter was supposed to avoid. FIX: Replace both Heisenberg citations by `thm:heisenberg-koszul-dual-early` or `thm:frame-heisenberg-koszul-dual`, and rewrite the computation in the canonical chiral model `C^\bullet_{\mathrm{ch}}(\mathcal B,\mathcal B)`; if you insist on the bimodule resolution, add an explicit comparison proposition from the chiral complex to that classical model before using it.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:12 — PROBLEM: The opening paragraph identifies `\ChirHoch^\bullet(\A)` with “the tangent complex to `\MC(\gAmod)/\mathrm{gauge}`” and immediately converts degree concentration into moduli amplitude `[0,2]`, but no shift convention for tangent complexes of MC moduli problems is stated here. Later tangent-complex definitions in the same file use shifted fibers [chiral_hochschild_koszul.tex:5255-5265]. FIX: Replace lines 11-16 with a shift-free statement: “`\ChirHoch^\bullet(\A)` is the deformation complex controlling bulk deformations; Theorem H gives vanishing outside degrees `0,1,2` on the Koszul locus.” Only discuss the tangent complex of the MC stack after the chapter states its shift convention.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:136 — PROBLEM: The duality formula is cited to `rem:nc-hodge-degeneration`, but that remark only discusses pole-order filtration and Hodge-type language; it does not state `\ChirHoch^n(\A)\cong \ChirHoch^{2-n}(\A^!)^\vee\otimes\omega_X`. FIX: Change the citation at line 137 to a forward reference to `Theorem~\ref{thm:main-koszul-hoch}` or to `Lemma~\ref{lem:hochschild-shift-computation}` plus `Theorem~\ref{thm:main-koszul-hoch}`.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:109 — PROBLEM: The file says the chiral Hochschild complex is “constructed in `\S\ref{subsec:hochschild-duality}`,” but that label is attached to the later main-duality subsection, not to the local construction at lines 139-318 or the algebraic definition in `chiral_center_theorem.tex`. FIX: Change the reference to “constructed in the present section” or “defined algebraically in Definition~\ref{def:chiral-hochschild-cochain-brace} and realized geometrically below.”

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:4867 — PROBLEM: The comparison with classical Hochschild cohomology ends with “For constant fields: `\ChirHoch^n(\A)|_{\text{constant}}\cong HH^n_{\text{classical}}(H^0(\A))`,” but “constant fields” is undefined and no comparison theorem or citation is supplied. FIX: Delete lines 4871-4873, or replace them with a qualified sentence: “After choosing a constant-field truncation functor and proving compatibility of the chiral and classical brace structures, one expects a comparison with classical Hochschild cohomology; this is not proved here.”

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:4539 — PROBLEM: The CFT aside leaks out of the chapter’s proved scope twice. Line 4541 treats `\ChirHoch^3` as the obstruction space without saying this is the pre-Theorem-H general pattern; on the Koszul locus the chapter itself later proves `\ChirHoch^n=0` for `n>2`. Line 4544 then jumps to `\mathcal N=4` SYM and a `\mathbb C^{3(g-1)}` deformation space inside Volume I with no setup, citation, or chiral-algebra-on-a-curve model. FIX: Rewrite the paragraph as: “For a general deformation complex, degree `2` classes are first-order deformations and degree `3` classes are potential obstructions; on the Koszul locus Theorem~\ref{thm:hochschild-polynomial-growth} kills the latter.” Then delete the `\mathcal N=4` SYM example or move it to Volume II with a precise citation.

- [LOW] chapters/theory/chiral_hochschild_koszul.tex:4976 — PROBLEM: The Heisenberg bracket example proves only `[[k],[k]]=0`, then overstates this as “the level is a central element … (it commutes with everything).” Self-bracket zero does not imply centrality. FIX: Replace the last sentence with: “This shows only that the self-bracket of the level class vanishes. Centrality would require a separate computation of `[[k],x]` for every `x\in\ChirHoch^\bullet(\mathcal B)`.”

## Summary
Checked: 8 | Findings: 16 | Verdict: FAIL
tokens used
176,154
