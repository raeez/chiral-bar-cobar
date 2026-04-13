# F15_hidden_imports_hg_comp (711s)

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:477` — PROBLEM: C0 Step 3 jumps from the genus-$g$ flat bar family to `thm:cobar-resolution-scoped` and `thm:obstruction-quantum`, but those imported results live on different objects: the former is a genus-$0$ cobar-resolution theorem (`chapters/theory/higher_genus_foundations.tex:2061-2081`), the latter defines `\mathcal Z(\A)` as `\mathcal H^0` of an endomorphism complex (`chapters/theory/higher_genus_foundations.tex:4588-4607`), not of `R\pi_{g*}\bar B^{(g)}_{\mathrm{flat}}(\A)`. FIX: delete lines 477-481 and insert a new local lemma proving `\mathcal H^0(R\pi_{g*}\bar B^{(g)}_{\mathrm{flat}}(\A))\cong\mathcal Z_\A` directly from the degree-$0$ bar calculation; cite that lemma here.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:818` — PROBLEM: Step I defines `E_1^{p,q,g}` using `d_{\mathrm{fiber}}` and then asserts `d_{\mathrm{fiber}}^2=0`, but the same manuscript’s higher-genus differential convention says `\dfib^{\,2}=\kappa(\A)\omega_g` and only `\Dg{g}^{\,2}=0` (`chapters/theory/higher_genus_foundations.tex:229-270`). FIX: rewrite the spectral sequence with the strict flat differential `\Dg{g}` everywhere, or reformulate Step I in coderived terms and stop taking ordinary cohomology of `\dfib`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:848` — PROBLEM: the Leray argument is run on the trivial product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g`, then the proof immediately treats the fiber as the varying curve `\overline C_p(\Sigma_g)`. That silently replaces the universal family by a constant product. FIX: replace lines 848-853 with the actual universal configuration morphism `\pi_{g,n}:\overline{\mathcal C}_{g,n}\to\overline{\mathcal M}_g` and rewrite the spectral sequence in terms of `R^q\pi_{g,n*}`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:975` — PROBLEM: `Q_g(\A)` is defined as the genus-graded piece of bar cohomology before C1 is proved, then later used as input to prove the C1 eigenspace decomposition. That is circular notation, not a proof. FIX: rename the Step I object to `Q_g^{\mathrm{fil}}(\A)` in lines 964-1011 and downstream uses, and only identify it with `\ker(\sigma-\mathrm{id})` after `lem:eigenspace-decomposition-complete`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1597` — PROBLEM: the proof-local center-isomorphism lemma uses `thm:e1-module-koszul-duality`, but that source explicitly says the proved module-level package is only on the quadratic genus-$0$ complete/conilpotent `E_1` lane and warns that extending it to arbitrary chiral Koszul pairs needs extra hypotheses (`chapters/theory/chiral_koszul_pairs.tex:5579-5588,5593-5626`). C1 applies it to arbitrary chiral Koszul pairs at all genera. FIX: either restrict C1 to that `E_1` lane, or replace lines 1597-1615 with a genuinely proved center-comparison lemma on the present chiral surface.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:600` — PROBLEM: `thm:quantum-complementarity-main` closes its proof at line 610 with only a roadmap, while the actual argument is split into later standalone proof environments at lines 757-1872. The theorem is structurally unproved in the TeX source. FIX: remove the `\end{proof}` at line 610 and keep Steps I-III inside the same proof, or turn lines 600-610 into a remark and attach a single actual proof environment spanning 757-1872.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:205` — PROBLEM: `def:complementarity-complexes` asserts a cochain involution `\sigma` on `\mathbf C_g(\A)` by citing `thm:verdier-bar-cobar`, but that theorem is a genus-$0$ Ran-space Verdier statement on `\bar B^{\mathrm{ch}}(\A)` (`chapters/theory/cobar_construction.tex:1313-1327`), not an involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\A))`. FIX: move the definition after a standalone construction of `\sigma_g`, or replace lines 205-207 by a forward reference to a new lemma that actually constructs `\sigma_g` on the ambient complex.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:327` — PROBLEM: `lem:perfectness-criterion` proves bounded coherent cohomology by base change, then jumps to “perfect complex” without adding the missing regularity input on `\overline{\mathcal M}_g`. FIX: weaken the conclusion to “bounded complex with coherent cohomology”, or add the explicit theorem/citation that on the smooth DM stack `\overline{\mathcal M}_g`, `D^b_{\mathrm{coh}}=\mathrm{Perf}`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:395` — PROBLEM: C0(i) says the curved fiber model determines a well-defined coderived object, but Step 1 only cites `conv:higher-genus-differentials` and `prop:gauss-manin-uncurving-chain`; the latter explicitly says the curved and flat models are not gauge equivalent and live in different categories (`chapters/theory/higher_genus_foundations.tex:396-410`). The coderived object itself is not constructed here. FIX: cite a real coderived-existence theorem from the coderived appendix, or weaken C0(i) to the statement actually shown: the curved model has an associated strict flat model for ordinary-derived calculations.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1381` — PROBLEM: the Kodaira-Spencer theorem cites `cor:quantum-dual-complete` as if it supplied `\mathbb D:H^*(\bar B^{(g)}(\A))\to H^*(\bar B^{(g)}(\A^!))^\vee`, but that corollary only states `Q_g(\A)\cong Q_g(\A^!)^\vee`. FIX: change the citation to a repaired full bar-complex duality result, or rewrite the sentence so it refers only to the `Q_g` spaces.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1667` — PROBLEM: the proof of `lem:eigenspace-decomposition-complete` assigns the `+1/-1` signs by slogan: lines 1683-1685 invoke an uncited `(-1)^q` rule, and lines 1704-1715 simply assert `\sigma(\beta)=-\beta`. No prior lemma computes these eigenvalues. FIX: insert a separate sign lemma computing the action of `\sigma` on the `j_*` and `j_!` branches with explicit chain-level conventions, or postpone the `Q_g(\A)`/`Q_g(\A^!)` naming until that sign computation exists.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1957` — PROBLEM: `prop:lagrangian-eigenspaces` redefines `\sigma` as `\mathbb D\circ\mathrm{KS}`, while the chapter already used `\sigma=\mathbb D\circ((-)^!)^{-1}` at lines 1503-1509, and it cites “Step 7” of another proof instead of a labeled result. The involution changes definition mid-chapter and the dependency is not a stable claim surface. FIX: promote one construction of `\sigma` to a standalone labeled lemma, cite that lemma here, and delete the `\sigma=\mathbb D\circ\mathrm{KS}` sentence.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2105` — PROBLEM: C2(i) concludes that the BV adjoint map `x\mapsto\{x,-\}_{\mathrm{BV}}` is a quasi-isomorphism and uses `thm:verdier-bar-cobar` on the all-genera curved-central surface, but the assumed theorems `thm:config-space-bv` and `thm:bv-functor` do not state that adjoint-map quasi-isomorphism, and `thm:verdier-bar-cobar` is only genus-$0$ quadratic. FIX: add the adjoint quasi-isomorphism and the needed higher-genus Verdier comparison as explicit hypotheses of C2, or remove the non-degeneracy conclusion from part (i).

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2123` — PROBLEM: C2(ii) calls `L_g:=\bar B^{(g)}(\A)[1]` a dg Lie algebra and says it is a genus truncation of `\Definfmod(\A)` via `prop:modular-deformation-truncation`, but that proposition is about the genus filtration on `\Defcyc^{\mathrm{mod}}(\A)`, not on the raw bar piece. FIX: redefine `L_g` as the genus-$g$ graded piece of `\Defcyc^{\mathrm{mod}}(\A)`, or add a new identification lemma proving that `\bar B^{(g)}(\A)[1]` is closed under the bracket and matches that truncation.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1247` — PROBLEM: `cor:duality-bar-complexes-complete` assumes a direct perfect pairing `\A\otimes\A^!\to\mathcal O_X` and integrates it, but the manuscript’s proved Koszul-duality surface gives a bar-coalgebra / dual-algebra comparison, not this pointwise pairing, and the required degree and dualizing-sheaf shifts are suppressed. FIX: rewrite the corollary as a pairing between `\bar B^{\mathrm{ch}}(\A)` and `\mathbb D_{\mathrm{Ran}}(\bar B^{\mathrm{ch}}(\A))`, then identify that dual object with `\A_\infty^!` only on the regime where `thm:verdier-bar-cobar` applies.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:588` — PROBLEM: the genus-$0$ clause uses unpointed `\overline{\mathcal M}_0` as if it were the same sort of object as the later pointed space `\overline{\mathcal M}_{1,1}`. This section never states the convention that makes the genus-$0$ surface stable. FIX: replace the genus-$0$ space by the stable pointed space actually intended, most likely `\overline{\mathcal M}_{0,3}\cong \mathrm{pt}`, or add an explicit convention before C1 that genus $0$ is read after fixing the three marked points.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1090` — PROBLEM: the Heisenberg example puts `\kappa` inside `Z(\mathcal H_\kappa)`, but throughout the chapter `\kappa` is used as a scalar level/modular-characteristic parameter, not a field in the algebra. FIX: replace `\mathbb C\cdot\mathbf1\oplus\mathbb C\cdot\kappa` by the actual central subspace of the chiral algebra, or keep `\kappa` outside the center example as an external scalar parameter.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1164` — PROBLEM: `thm:verdier-duality-config-complete` is stated at the wrong categorical level: Verdier duality is written as an isomorphism on cohomology groups with a residual `[d]` shift, while the proof is ordinary Poincaré duality by integration. FIX: restate the theorem at the sheaf/complex level `\mathbb D_{\overline C_n(X)}(\mathbf C)\simeq\mathbf C[2n]` and move the cohomological pairing to a corollary.

- [LOW] `chapters/theory/higher_genus_complementarity.tex:467` — PROBLEM: Step 3 says the `E_1`-page vanishing holds “by Step 2”, but Step 2 only defines the filtration; the associated-graded computation is in Step 3 itself. FIX: change “by Step 2” to “by Step 3” or merge the associated-graded argument into Step 2.

## Summary
Checked: 19 | Findings: 19 | Verdict: FAIL


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
session id: 019d86a1-df9d-7c52-a9e9-50097f3dc6c8
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
**Planning file audit**

I need to conduct an audit of the specified file chapters. I’ll have to make exact fixes, grounding every claim in what I find. It seems necessary to read the AGENTS required files before making any significant edits. Since the user wants just an audit, I should inspect the file for any hidden imports relevant to the proofs. Using the deep-beilinson-audit skill could be critical, so I need to remember that. Frequent commentary is important as I proceed!
thinking
**Updating audit plan**

I likely need to update the audit plan because it sounds substantial. I should follow instructions from AGENTS and use pre-edit verification, even if I'm not editing. It’s important to inspect the file, identifying all theorem labels like C0, C1, and C2, while checking for hidden imports. Exact line references will also be necessary, possibly using line numbers. It seems prudent to read the required files for a thorough audit. Starting with an update on commentary sounds like a good approach before diving into the skill files.
thinking
**Using the explorer for dependency mapping**

I could use the explorer to map out dependencies and labels in the target file. The guidance suggests preferring explorers over manual search or reading, so I plan to start with the explorer sub-agent for clarity. My goal is to identify labels like C0, C1, C2, along with any hidden imports and unresolved references. However, I still need to ground my findings in the actual contents of the file. Trusting the explorer is recommended, but I'll ensure to verify everything through careful reading.
codex
Using `deep-beilinson-audit` for a hostile review of [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex). I’m first reading the audit constitution files, the target file with line numbers, and the proof dependencies around the `C0/C1/C2` surfaces so the findings are grounded in exact text.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
 succeeded in 53ms:
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
| Total tagged claims | 3672 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 succeeded in 51ms:
     1	\section{The complementarity theorem}
     2	\label{sec:complementarity-theorem}
     3	
     4	Classical Koszul duality over a point is a discrete correspondence:
     5	$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
     6	Already at genus~$0$ on a curve, the Fulton--MacPherson
     7	compactifications $\overline{C}_n(X)$ and the Arnold forms
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
    16	algebras to interact through the moduli
    17	$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
    18	decomposes into two complementary halves via Verdier duality:
    19	\begin{equation}\label{eq:complementarity-chapter-opening}
    20	 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
codex
The file is front-loading bold claims before definitions. I’m mapping the exact theorem/proof blocks and every imported label they cite so the audit hits hidden dependencies rather than surface prose only.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '981,1340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{|begin\\{(theorem|lemma|proposition|corollary|definition|remark)\\}|ClaimStatus|ref\\{\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '261,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '621,980p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 750

2:\label{sec:complementarity-theorem}
19:\begin{equation}\label{eq:complementarity-chapter-opening}
39:(Theorem~\ref{thm:quantum-complementarity-main}).
50: \textup{(}Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}\textup{)}.
57: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
66: \begin{equation}\label{eq:complementarity-summary}
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
84: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
96: \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
100:flat fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
103:(Proposition~\ref{prop:standard-examples-modular-koszul}).
111:\begin{remark}[Calabi--Yau exchange and the perfectness hypothesis]
112:\label{rem:hr24-cy-interchange}
126:base change (Lemma~\ref{lem:perfectness-criterion}).
134:\begin{remark}[Physical origin]
145:\begin{remark}[Kodaira--Spencer action on tautological classes]
155:\begin{remark}[Algebraic structure]
164:\begin{remark}[Computational perspective: Heisenberg at genus~$1$]
 succeeded in 53ms:
   981	
   982	The genus-$g$ quantum corrections are precisely those cohomology classes that arise 
   983	from genus-$g$ contributions but not from lower genus. Thus:
   984	\begin{equation}
   985	Q_g(\mathcal{A}) := \text{gr}^g H^*(\bar{B}(\mathcal{A})) = E_\infty^{*,*,g}
   986	\end{equation}
   987	We use the same notation $Q_g(\mathcal{A})$ for this graded piece,
   988	anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
   989	which identifies it with the $+1$-eigenspace of the Verdier involution
   990	(Definition~\ref{def:complementarity-complexes}).
   991	The two characterizations coincide: the filtration graded
   992	piece captures the part of bar cohomology coming from genus~$g$,
   993	while the eigenspace captures the $\mathcal{A}$-sector under
   994	Verdier involution.
   995	The identification is proved in
   996	Lemma~\ref{lem:eigenspace-decomposition-complete}: the Verdier
   997	involution sorts contributions according to whether they arise
   998	from $j_*$-extended bar cochains of~$\mathcal{A}$ (eigenvalue~$+1$) or
   999	from $j_!$-extended bar cochains of~$\mathcal{A}^!$ (eigenvalue~$-1$),
  1000	and the genus filtration separates precisely these two sources
 succeeded in 51ms:
   621	(Theorem~\textup{\ref{thm:ambient-d-squared-zero}},
   622	which uses \textup{[}Mok25\textup{]}) or on the full
   623	bar-intrinsic MC element $\Theta_\cA$
   624	(Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}).
   625	The only curvature input is the scalar $\kappa(\cA)$,
   626	which comes from the convolution-level
   627	$D^2 = 0$ (unconditional).
   628	\end{remark}
   629	
   630	\begin{remark}[Elementary model presentation;
   631	Convention~\ref{conv:proof-architecture}]
   632	\label{rem:theorem-c-model}
   633	\label{rem:complementarity-model}% backward-compatible label
   634	\index{complementarity!model presentation}
   635	\emph{Step~B} (M-level): The homotopy eigenspace
   636	$\mathbf{Q}_g(\cA)=\operatorname{fib}(\sigma-\mathrm{id})$ is modeled by
   637	$\operatorname{im}(p^+)$ with $p^+=\tfrac{1}{2}(\mathrm{id}+\sigma)$
   638	on $C_g=R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$.
   639	The Lagrangian property is $\langle p^+x,p^+y\rangle=0$
   640	(Lemma~\ref{lem:involution-splitting}(c)).
 succeeded in 52ms:
   261	\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
   262	and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
   263	via the standard cone identification.
   264	Part~(b) follows by applying $H^*$ to~(a).
   265	Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
   266	so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
   267	= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
   268	Maximality is immediate from the direct-sum decomposition.
   269	\end{proof}
   270	
   271	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   272	\index{bar complex!relative fiber|textbf}
   273	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
   274	\[
   275	\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
   276	\overline{\mathcal{M}}_g
   277	\]
   278	be the family of genus-$g$ compactified configuration spaces
   279	carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
   280	Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the



thinking
**Reviewing theorem proof steps**

I think I might need to add more lines around theorem proof Step III later, but maybe it’s sufficient for now. I need to inspect lines 1330 onward later since there are a lot of outputs. I'm thinking about focusing on proofs C1/C2 and hidden imports between lines 1367-1800 and 1913, and I need to check if those definitions for imported labels are unresolved. I’ll probably need to use `texlua` or `rg` to see if those labels exist.
thinking
**Inspecting reference labels**

I need to check the statuses of referenced labels in the metadata or file definitions. I could use scripts or `rg` across the repo to locate labels and status tags. It seems I should script some analysis to list references from theorem blocks and determine if the targets exist and their statuses. The user wants an exhaustive audit, focusing on the foundation of the file, particularly hidden imports for C0/C1/C2 proofs. It’s probably best to concentrate on proof surfaces and their surroundings.
thinking
**Reviewing supporting proofs**

I need to consider potential issues within the support chain. It's probably a good idea to read around the proof for thm:quantum-complementarity-main, along with the supporting lemmas in Steps I-III and several properties, like prop:lagrangian-eigenspaces and prop:ptvv-lagrangian. I'll focus on inspecting lines 1360-2200. It seems important to examine these specific chunks thoroughly, so let's take a closer look at those line numbers.
codex
I have the theorem shells. Next I’m reading the actual proof chain for `C1` and `C2`, because the file already shows a pattern of statements that cite deep inputs instead of proving the bridge locally.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1360,1825p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1360	
  1361	\subsection{Step III: decomposition and complementarity}
  1362	
  1363	\begin{proof}[Step III: Steps 7-10]
  1364	
  1365	\emph{Step 7: Center action on moduli space cohomology.}
  1366	
  1367	\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
  1368	\label{thm:kodaira-spencer-chiral-complete}
  1369	\index{Kodaira--Spencer map|textbf}
  1370	\textup{[Regime: curved-central on the Koszul locus; positive genus
  1371	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1372	
  1373	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
  1374	$g \geq 1$, and let $\pi: \mathcal{C}_g
  1375	\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
  1376	\begin{equation}
  1377	\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
  1378	\end{equation}
  1379	constructed from the Gauss--Manin connection on the chiral homology sheaf.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1826,2335p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
path=pathlib.Path('chapters/theory/higher_genus_complementarity.tex')
text=path.read_text()
# extract refs in C0/C1/C2 region around theorem/proof chain 372-610 and 756-2335
regions=[(372,610),(756,2335)]
lines=text.splitlines()
for start,end in regions:
    sub='\\n'.join(lines[start-1:end])
    refs=sorted(set(re.findall(r'\\\\(?:ref|eqref|textup\\{\\\\ref)\\{(["'^}]+)'"\\}', sub)))
    print(f'REGION {start}-{end}: {len(refs)} refs')
    for r in refs:
        print(r)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1826	and in particular $\dim V^+ + \dim V^- = \dim V$.
  1827	
  1828	\emph{Verification at small genera.}
  1829	
  1830	\emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
  1831	$\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
  1832	giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
  1833	$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
  1834	Theorem~\ref{thm:quantum-complementarity-main}.
  1835	
  1836	\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
  1837	For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
  1838	(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
  1839	\cdot \lambda$ (curvature, eigenvalue $-1$). Dimension check: $1 + 1 = 2$.
  1840	
  1841	\emph{Genus $2$}: $\dim H^*(\overline{\mathcal{M}}_2) = 8$
  1842	(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$).
  1843	The involution $\sigma$ splits $H^*$ into $\pm 1$-eigenspaces whose
  1844	dimensions depend on the chiral algebra through the $j_*/j_!$ extension
  1845	data. For Koszul self-dual algebras (e.g., $\mathrm{Vir}_{13}$),
 exited 127 in 50ms:
zsh:1: command not found: python
codex
I’ve hit the proof bodies now. The main failure mode is becoming clear: many “proved here” steps are actually paraphrases of unstated comparison theorems, and some transitions change the object being studied without saying so.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
tex_files=list(root.rglob('*.tex'))
labels={}
for p in tex_files:
    try:
        text=p.read_text()
    except Exception:
        continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', text):
        labels.setdefault(m.group(1), []).append((str(p), text.count('\\n',0,m.start())+1))
path=pathlib.Path('chapters/theory/higher_genus_complementarity.tex')
text=path.read_text()
refs=sorted(set(re.findall(r'\\\\(?:ref|eqref|pageref|autoref|Cref|cref)\\{(["'^}]+)'"\\}', text)))
missing=[]
for r in refs:
    if r not in labels:
        missing.append(r)
print('TOTAL REFS', len(refs))
print('MISSING', len(missing))
for r in missing:
    print(r)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
tex_files=list(root.rglob('*.tex'))
labels={}
for p in tex_files:
    try:
        text=p.read_text()
    except Exception:
        continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', text):
        labels.setdefault(m.group(1), []).append((str(p), text.count('\\n',0,m.start())+1))
# refs in C0/C1/C2 main region only
path=pathlib.Path('chapters/theory/higher_genus_complementarity.tex')
lines=path.read_text().splitlines()
sub='\\n'.join(lines[371:2335])
refs=sorted(set(re.findall(r'\\\\(?:ref|eqref|pageref|autoref|Cref|cref)\\{(["'^}]+)'"\\}', sub)))
for r in refs:
    locs=labels.get(r)
    if locs:
        print(r, '=>', '; '.join(f'{p}:{ln}' for p,ln in locs[:3]))
    else:
        print(r, '=> MISSING')
PY" in /Users/raeez/chiral-bar-cobarcodex
I’m checking the reference graph mechanically now. If any cited theorem or lemma in the `C0/C1/C2` chain is missing, duplicated, or only exists under a weaker status elsewhere, it will surface here.
 succeeded in 56.09s:
TOTAL REFS 210
MISSING 0
 succeeded in 59.01s:
app:sign-conventions => appendices/signs_and_shifts.tex:713; .claude/worktrees/agent-a2a46b8f/appendices/signs_and_shifts.tex:713; .claude/worktrees/agent-a40a6cef/appendices/signs_and_shifts.tex:713
app:signs => appendices/signs_and_shifts.tex:2; .claude/worktrees/agent-a2a46b8f/appendices/signs_and_shifts.tex:2; .claude/worktrees/agent-a40a6cef/appendices/signs_and_shifts.tex:2
ch:bv-brst => .claude/worktrees/agent-a2a46b8f/chapters/connections/bv_brst.tex:2; .claude/worktrees/agent-a40a6cef/chapters/connections/bv_brst.tex:2; .claude/worktrees/agent-ab23aca7/chapters/connections/bv_brst.tex:2
conv:higher-genus-differentials => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_foundations.tex:205; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_foundations.tex:205; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_foundations.tex:205
conv:proof-architecture => standalone/introduction_full_survey.tex:5307; .claude/worktrees/agent-a2a46b8f/chapters/theory/introduction.tex:4814; .claude/worktrees/agent-a40a6cef/chapters/theory/introduction.tex:4742
conv:regime-tags => standalone/introduction_full_survey.tex:5307; .claude/worktrees/agent-a2a46b8f/chapters/theory/introduction.tex:4814; .claude/worktrees/agent-a40a6cef/chapters/theory/introduction.tex:4742
cor:duality-bar-complexes-complete => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:1034; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:1033; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:1033
cor:quantum-dual-complete => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:1128; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:1127; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:1127
cor:virasoro-quantum-dim => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:2237; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:2236; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:2236
def:chiral-koszul-pair => .claude/worktrees/agent-a2a46b8f/chapters/theory/chiral_koszul_pairs.tex:544; .claude/worktrees/agent-a40a6cef/chapters/theory/chiral_koszul_pairs.tex:542; .claude/worktrees/agent-ab23aca7/chapters/theory/chiral_koszul_pairs.tex:542
def:complementarity-complexes => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:112; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:111; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:111
def:geometric-bar => .claude/worktrees/agent-a2a46b8f/chapters/theory/bar_construction.tex:449; .claude/worktrees/agent-a40a6cef/chapters/theory/bar_construction.tex:452; .claude/worktrees/agent-ab23aca7/chapters/theory/bar_construction.tex:452
def:koszul-dual-chiral => .claude/worktrees/agent-a2a46b8f/chapters/theory/chiral_koszul_pairs.tex:2857; .claude/worktrees/agent-a40a6cef/chapters/theory/chiral_koszul_pairs.tex:2943; .claude/worktrees/agent-ab23aca7/chapters/theory/chiral_koszul_pairs.tex:2943
def:modular-koszul-chiral => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_modular_koszul.tex:455; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_modular_koszul.tex:455; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_modular_koszul.tex:455
eq:center-residue-condition => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:858; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:857; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:857
eq:complementarity-decomp => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:402; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:401; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:401
eq:fiber-bar-complex => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:832; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:831; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:831
eq:quantum-duality => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:435; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:434; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:434
eq:verdier-center-intertwine => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:1281; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:1280; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:1280
eq:verdier-ks-anticommute => .claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_complementarity.tex:1173; .claude/worktrees/agent-a40a6cef/chapters/theory/higher_genus_complementarity.tex:1172; .claude/worktrees/agent-ab23aca7/chapters/theory/higher_genus_complementarity.tex:1172
exec
/bin/zsh -lc 'for lbl in prop:gauss-manin-uncurving-chain thm:cobar-resolution-scoped thm:obstruction-quantum thm:verdier-bar-cobar lem:verdier-extension-exchange thm:e1-module-koszul-duality thm:config-space-bv thm:bv-functor prop:modular-deformation-truncation thm:modular-homotopy-convolution prop:model-independence thm:chiral-koszul-duality def:modular-koszul-chiral conv:higher-genus-differentials conv:regime-tags; do echo "=== $lbl ==="; rg -n "'"\\\\label\\{"'$lbl'"\\}|ClaimStatus|begin\\{(theorem|lemma|proposition|definition|convention|remark)\\}\" chapters appendices metadata -g '*.tex' -g '*.md' | sed -n '1,8p'; done" in /Users/raeez/chiral-bar-cobar succeeded in 96ms:
=== prop:model-independence ===
rg: regex parse error:
    (?:\label\{prop:model-independence\}|ClaimStatus|begin\{(theorem|lemma|proposition|definition|convention|remark)\})
       ^^
error: unrecognized escape sequence
=== thm:chiral-koszul-duality ===
rg: regex parse error:
    (?:\label\{thm:chiral-koszul-duality\}|ClaimStatus|begin\{(theorem|lemma|proposition|definition|convention|remark)\})
       ^^
error: unrecognized escape sequence
=== def:modular-koszul-chiral ===
rg: regex parse error:
    (?:\label\{def:modular-koszul-chiral\}|ClaimStatus|begin\{(theorem|lemma|proposition|definition|convention|remark)\})
       ^^
error: unrecognized escape sequence
=== conv:higher-genus-differentials ===
rg: regex parse error:
    (?:\label\{conv:higher-genus-differentials\}|ClaimStatus|begin\{(theorem|lemma|proposition|definition|convention|remark)\})
       ^^
error: unrecognized escape sequence

thinking
**Considering regex simplifications**

I think my regex approach isn't quite right. Instead, I could use simpler methods with `rg` for fixed strings, maybe utilizing the `-F` option. There’s also the idea of just using `rg` with a specific label, which might help make things clearer. I might want to work in a loop while applying `rg -n -F` to streamline the process better. It feels like there’s a more efficient path here!
exec
/bin/zsh -lc 'for lbl in prop:gauss-manin-uncurving-chain thm:cobar-resolution-scoped thm:obstruction-quantum thm:verdier-bar-cobar lem:verdier-extension-exchange thm:e1-module-koszul-duality thm:config-space-bv thm:bv-functor prop:modular-deformation-truncation thm:modular-homotopy-convolution prop:model-independence thm:chiral-koszul-duality def:modular-koszul-chiral conv:higher-genus-differentials conv:regime-tags; do echo "=== $lbl ==="; rg -n -F "'"\\\\label{"'$lbl}" chapters appendices metadata CLAUDE.md; done' in /Users/raeez/chiral-bar-cobar succeeded in 187ms:
chapters/theory/chiral_koszul_pairs.tex:5595:\label{thm:e1-module-koszul-duality}
=== thm:config-space-bv ===
chapters/connections/bv_brst.tex:1307:\label{thm:config-space-bv}
=== thm:bv-functor ===
chapters/connections/bv_brst.tex:1363:\label{thm:bv-functor}
=== prop:modular-deformation-truncation ===
chapters/theory/chiral_hochschild_koszul.tex:2060:\label{prop:modular-deformation-truncation}
=== thm:modular-homotopy-convolution ===
chapters/theory/higher_genus_modular_koszul.tex:10934:\label{thm:modular-homotopy-convolution}
=== prop:model-independence ===
chapters/theory/bar_construction.tex:1473:\label{prop:model-independence}
=== thm:chiral-koszul-duality ===
chapters/theory/chiral_koszul_pairs.tex:4557:\label{thm:chiral-koszul-duality}
=== def:modular-koszul-chiral ===
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
=== conv:higher-genus-differentials ===
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
=== conv:regime-tags ===
chapters/theory/introduction.tex:2580:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
chapters/theory/introduction.tex.bak:1860:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '330,410p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '330,390p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2048,2105p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4568,4628p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   340	comparison of the three chain-level models and their relationship
   341	to the modular bar complex.
   342	\end{remark}
   343	
   344	\begin{proposition}[Gauss--Manin uncurving at chain level; \ClaimStatusProvedHere]
   345	\label{prop:gauss-manin-uncurving-chain}
   346	\index{Gauss--Manin connection!chain-level uncurving|textbf}
   347	\index{uncurving!Gauss--Manin|textbf}
   348	Let $\cA$ be a cyclic chiral algebra on $\Sigma_g$ with
   349	$g \geq 1$. The passage from the curved differential $\dfib$
 succeeded in 51ms:
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
   340	The internal differential $d_{\mathrm{internal}}$ is induced by the
   341	chiral algebra structure, which is a $\mathcal{D}_X$-module morphism
   342	by definition.
   343	The form differential $d_{\mathrm{form}}$ is the de~Rham differential
   344	on $\Omega^*_{\log}(D)$, which is a $\mathcal{D}$-module morphism.
   345	The residue differential $d_{\mathrm{residue}} = \sum_D \operatorname{Res}_D$
   346	is the composition of restriction to a boundary divisor~$D$ followed
   347	by the trace map, both of which are morphisms of
   348	$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
   349	Hence $d_{\mathrm{bar}}$ is a morphism of holonomic
 succeeded in 51ms:
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
  2060	
  2061	\begin{theorem}[Cobar resolution on the Koszul locus {\cite{LV12}}; \ClaimStatusProvedElsewhere]
  2062	\label{thm:cobar-resolution-scoped}
  2063	For any augmented chiral algebra $\mathcal{A}$, the bar construction
  2064	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ and cobar construction
  2065	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ exist as objects.
  2066	When the canonical twisting morphism is Koszul
  2067	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})},
 succeeded in 50ms:
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
  4580	\end{enumerate}
  4581	\emph{Provenance note.}
  4582	This claim is used in this manuscript as an external theorem, proved in
  4583	\cite{Mumford83}. It is not reproved internally here.
  4584	\end{remark}
  4585	
  4586	\subsection{Quantum obstructions as cohomology classes}
  4587	
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1296,1348p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1290,1398p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5578,5638p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2040,2088p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '220,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '520,565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2580,2618p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10912,10970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4538,4615p'" in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
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
  1310	\subsection{Verdier duality on bar and cobar}
  1311	
  1312	
  1313	\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
  1314	\label{thm:verdier-bar-cobar}
  1315	\index{Verdier duality!bar-cobar|textbf}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1456,1495p'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
  2040	\end{definition}
  2041	
  2042	\begin{remark}[Strictification of the modular deformation object]
  2043	\label{rem:modular-cyc-strictification}
  2044	The modular cyclic deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$
  2045	is the strict model of the homotopy-invariant modular deformation
  2046	object $\Definfmod(\cA)$
  2047	\textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution})}.
  2048	The cyclic coderivation description is one model, obtained from the
  2049	cofree resolution of~$\barB(\cA)$; a different choice of
  2050	contracting homotopy produces an $L_\infty$-quasi-isomorphic
  2051	deformation complex. For affine Kac--Moody algebras, the
  2052	strict model is already formal: the universal class
  2053	$\Theta^{\mathrm{str}}_{\widehat{\mathfrak{g}}_k}$ satisfies the strict
  2054	MC equation with all higher $L_\infty$-brackets vanishing
  2055	\textup{(}Theorem~\textup{\ref{thm:km-strictification})}.
  2056	\end{remark}
  2057	
  2058	\begin{proposition}[Genus truncation;
  2059	\ClaimStatusProvedHere]
 succeeded in 76ms:
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
  1308	Assume that the diagonal-residue operator on the logarithmic bar
  1309	complex extends to a degree-$+1$ second-order operator
 succeeded in 55ms:
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
 succeeded in 85ms:
  5578	transport, and Hochschild transport\textup{)}
  5579	is \emph{not} proved on this general surface. The earlier bar-cobar
  5580	machinery in Part~\ref{part:bar-complex} gives the intrinsic bar-coalgebra comparison, and
  5581	the manuscript's proved ordinary module-level statement is the later
  5582	$\Eone$ theorem
  5583	Theorem~\ref{thm:e1-module-koszul-duality}, restricted to the
  5584	quadratic genus-$0$ complete/conilpotent lane.
  5585	
  5586	Any extension of that package to arbitrary chiral Koszul pairs would
  5587	require extra hypotheses and a module-level comparison theorem beyond
  5588	what is currently established here.
  5589	\end{remark}
  5590	
  5591	\subsection{\texorpdfstring{$\Eone$-chiral module category Koszul duality}{E1-chiral module category Koszul duality}}
  5592	
  5593	\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-module category Koszul duality;
  5594	\ClaimStatusProvedHere]
  5595	\label{thm:e1-module-koszul-duality}
  5596	\index{module Koszul duality|textbf}
  5597	Let $\mathcal{A}$ be a Koszul $\Eone$-chiral algebra with Koszul
 succeeded in 54ms:
  4538	\[\sum_{j,m,n} C_{ij}^{\gamma,m} C_{j\alpha}^{\beta,n} + \sum_{k,m,s} C_{i\alpha}^{k,m} C_{k\beta}^{\gamma,s} = 0 \qquad \forall\, i, \alpha, \beta, \gamma\]
  4539	
  4540	But this is \emph{precisely the associativity constraint} for the chiral product in $\mathcal{A}_2$: the second sum encodes $(\phi_i \cdot \phi_\alpha) \cdot \phi_\beta$ evaluated at $\phi_\gamma$, while the first sum encodes the rearrangement through $\phi_i \cdot (\phi_\alpha \cdot \phi_\beta)$.
  4541	
  4542	Geometrically: $d_!^2 = 0$ encodes $\partial^2 = 0$ in configuration space; boundaries of boundaries vanish (Arnold--Orlik--Solomon relations).
  4543	\end{proof}
  4544	
  4545	\begin{remark}
  4546	Theorem~\ref{thm:coalgebra-axioms-verified} exhibits the characteristic feature of Koszul duality: associativity of the algebra $\mathcal{A}_2$ is equivalent to nilpotence of the coalgebra differential $d_!$. Algebraic structure on one side translates to cohomological structure on the dual side.
  4547	\end{remark}
  4548	
  4549	%----------------------------------------------------------------
  4550	% STAGE 3: BAR COMPUTES THE DUAL
  4551	%----------------------------------------------------------------
  4552	
  4553	\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}
  4554	
  4555	\begin{theorem}[Bar computes Koszul dual, complete statement; \ClaimStatusProvedHere]
  4556	\label{thm:bar-computes-koszul-dual-complete}
  4557	\label{thm:chiral-koszul-duality}
 succeeded in 61ms:
 10912	well-defined up to $L_\infty$-quasi-isomorphism, whose
 10913	Maurer--Cartan elements are $\infty$-twisting morphisms.
 10914	For strict $C$, $P$, the convolution dg~Lie algebra
 10915	$\Convstr(C,P) := \operatorname{Hom}_{\mathbb{S}}(C,P)$ is a
 10916	strict model: $\ell_1 = D$, $\ell_2 = [-,-]$,
 10917	$\ell_n = 0$ for $n \geq 3$.
 10918	The full chiral operadic identification, including
 10919	functoriality with respect to $\infty$-morphisms
 10920	and the one-slot obstruction, is
 10921	Theorem~\textup{\ref{thm:operadic-homotopy-convolution}}.
 10922	\end{theorem}
 10923	
 10924	\begin{proof}[References]
 10925	The operadic $L_\infty$ structure is constructed via homotopy
 10926	transfer through the $\operatorname{Hom}$~functor
 10927	(Loday--Vallette~\cite[Thm~10.3.8]{LV12}; Robert-Nicoud--Wierstra~\cite[Thm~4.1]{RNW19}); the explicit
 10928	transferred brackets are given by van~der~Laan~\cite{vdL03}.
 10929	The strict dg~Lie algebra is the binary truncation.
 10930	\end{proof}
 10931	
 succeeded in 64ms:
  2580	\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
  2581	\index{regime tag}
  2582	Four regimes, in order of increasing generality.
  2583	The three bar differentials are:
  2584	$\dzero$ (the genus-$0$ bar differential),
  2585	$\dfib$ (the fibered bar differential, genus-$g$ but
  2586	uncorrected for period monodromy), and
  2587	$\Dg{g}$ (the full genus-$g$ corrected bar differential,
  2588	incorporating period corrections via the Hodge bundle).
  2589	\begin{enumerate}
  2590	\item \textbf{Quadratic.} $\dzero^2 = 0$;
  2591	 Theorems~A--D hold without qualification.
  2592	 Heisenberg, free fermions, lattice VOAs.
  2593	\item \textbf{Curved-central.}
  2594	 $\dfib^{\,2} = \kappa \cdot \omega_g$; $\Dg{g}^{\,2} = 0$.
  2595	 $\widehat{\mathfrak{g}}_k$ at non-critical level, Virasoro
  2596	 with $c \neq 0$.
  2597	\item \textbf{Filtered-complete.} Complete filtration with
  2598	 $\operatorname{gr}^F \cA$ quadratic Koszul.
  2599	 $\mathcal{W}$-algebras via DS reduction, deformation
 succeeded in 68ms:
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
  1470	\end{corollary}
  1471	
  1472	\begin{proposition}[Model independence; \ClaimStatusProvedHere]
  1473	\label{prop:model-independence}
  1474	\index{model independence}
  1475	Let $\cA$ be a chiral algebra on~$X$.

thinking
**Checking theorem references**

I need to check the status of some imported references: thm:config-space-bv and thm:bv-functor, which are conditional. Since the C2 theorem is conditional, it seems okay for imports. However, there's a local lemma, `bar-chart-lagrangian-lift`, that relies on theorem C0, which might not be sufficient. I should scrutinize this. Maybe using a smaller script to extract missing references could be easier, perhaps with Python3 or ripgrep, using a simple shell pipeline.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess, pathlib
# get all labels fast via rg
proc = subprocess.run(['rg','-n','\\\\label\\\\{["'^}]+'"\\\\}','-g','*.tex','.'],capture_output=True,text=True,check=True)
labels=set()
for line in proc.stdout.splitlines():
    m=re.search(r'\\\\label\\{(["'^}]+)'"\\}',line)
    if m: labels.add(m.group(1))
text=pathlib.Path('chapters/theory/higher_genus_complementarity.tex').read_text()
refs=sorted(set(re.findall(r'\\\\(?:ref|eqref|pageref|autoref|Cref|cref)\\{(["'^}]+)'"\\}',text)))
missing=[r for r in refs if r not in labels]
print('refs',len(refs))
print('missing',len(missing))
for r in missing:
    print(r)
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 577, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['rg', '-n', '\\label\\{[^}]+\\}', '-g', '*.tex', '.']' returned non-zero exit status 2.

thinking
**Considering a script approach**

I’m thinking about needing a simpler escape for my command, maybe using `rg -N` could help. Instead, I’m leaning towards a shell script because it feels more straightforward than Python. I can use a command like `rg -o --no-filename '\\label\{[^}]+' -g '*.tex'`. But I need to pay attention to proper quoting to make sure it works right. Let’s keep refining this!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess, pathlib
cmd=\"rg -n -o '\\\\\\\\label\\\\{["'^}]+'"\\\\}' -g '*.tex' .\"
proc=subprocess.run(cmd,shell=True,capture_output=True,text=True)
print('rg status',proc.returncode)
print(proc.stderr[:500])
text=pathlib.Path('chapters/theory/higher_genus_complementarity.tex').read_text()
refs=sorted(set(re.findall(r'\\\\(?:ref|eqref|pageref|autoref|Cref|cref)\\{(["'^}]+)'"\\}',text)))
labels=set()
for line in proc.stdout.splitlines():
    m=re.search(r'\\\\label\\{(["'^}]+)'"\\}',line)
    if m: labels.add(m.group(1))
missing=[r for r in refs if r not in labels]
print('refs',len(refs),'labels',len(labels),'missing',len(missing))
for r in missing[:200]:
    print(r)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg status 0

refs 210 labels 14612 missing 0

thinking
**Exploring repository statuses**

I’m looking to get the statuses for my repositories. It seems logical to use Python to scan the repo for a label map to the environment and status. I think I might want to read the nearby lines as well to gather more context, which could be helpful. Let’s see how that works out as I go through this! It’s a bit process-heavy, but I want to ensure I capture everything accurately.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
# collect label metadata from tex files
label_meta={}
for p in root.rglob('*.tex'):
    try: lines=p.read_text().splitlines()
    except Exception: continue
    for i,l in enumerate(lines):
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', l):
            label=m.group(1)
            # search up to 4 lines backwards for begin{env}; 6 forward/back for ClaimStatus
            env=None; status=[]; title=None
            for j in range(max(0,i-4), min(len(lines), i+1)):
                mb=re.search(r'\\\\begin\\{(theorem|lemma|proposition|corollary|definition|remark|convention|example|computation|calculation|conjecture)\\}(?:\\[(.*)\\])?', lines[j])
                if mb:
                    env=mb.group(1)
                    title=mb.group(2)
            for j in range(max(0,i-4), min(len(lines), i+5)):
                status.extend(re.findall(r'\\\\ClaimStatus([A-Za-z]+)', lines[j]))
            label_meta[label]=(str(p), i+1, env, ','.join(status) if status else '-')
# refs in theorem region
path=pathlib.Path('chapters/theory/higher_genus_complementarity.tex')
lines=path.read_text().splitlines()
sub='\\n'.join(lines[371:2335])
refs=sorted(set(re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}', sub)))
for r in refs:
    if r in label_meta:
        p,ln,env,status=label_meta[r]
        print(f'{r}\\t{p}:{ln}\\t{env}\\t{status}')
    else:
        print(f'{r}\\tMISSING')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 26.79s:
app:sign-conventions	archive/orphaned_stubs/sign_conventions.tex:2	None	-
app:signs	.claude/worktrees/agent-a074cd40/appendices/signs_and_shifts.tex:2	None	-
ch:bv-brst	chapters/connections/bv_brst.tex:2	None	-
conv:higher-genus-differentials	chapters/theory/higher_genus_foundations.tex:229	convention	-
conv:proof-architecture	chapters/theory/introduction.tex:2580	convention	-
conv:regime-tags	chapters/theory/introduction.tex:2580	convention	-
cor:duality-bar-complexes-complete	chapters/theory/higher_genus_complementarity.tex:1238	corollary	ProvedHere
cor:quantum-dual-complete	chapters/theory/higher_genus_complementarity.tex:1332	corollary	ProvedHere
cor:virasoro-quantum-dim	chapters/theory/higher_genus_complementarity.tex:2590	corollary	ProvedHere
def:chiral-koszul-pair	chapters/theory/chiral_koszul_pairs.tex:641	definition	-
def:complementarity-complexes	chapters/theory/higher_genus_complementarity.tex:197	definition	-
def:geometric-bar	archive/split_originals/bar_cobar_construction.tex:421	definition	-
def:koszul-dual-chiral	chapters/theory/chiral_koszul_pairs.tex:4420	definition	-
def:modular-koszul-chiral	archive/raeeznotes/raeeznotes97/higher_genus_modular_koszul (1).tex:328	definition	-
eq:center-residue-condition	chapters/theory/higher_genus_complementarity.tex:1059	None	-
eq:complementarity-decomp	chapters/theory/higher_genus_complementarity.tex:546	None	-
eq:fiber-bar-complex	chapters/theory/higher_genus_complementarity.tex:1033	None	-
eq:quantum-duality	chapters/theory/higher_genus_complementarity.tex:585	None	-
eq:verdier-center-intertwine	chapters/theory/higher_genus_complementarity.tex:1493	None	-
eq:verdier-ks-anticommute	chapters/theory/higher_genus_complementarity.tex:1385	None	-








thinking
**Identifying structural issues**

I notice that later step proofs exist in separate environments and aren’t linked to any theorem. However, there's this line stating, "This completes the proof of Theorem..." within Step III proof, which is confusing because it suggests the theorem has two proof environments, one of which closes early. This feels like a logical inconsistency or a bug that I need to address. It seems important to clarify the relationship between these proofs!
thinking
**Reviewing proof corrections**

I need to fix a couple of things in the theorem proof. First, I should delete `\end{proof}` at line 610 and either insert lines 601-609 as a roadmap paragraph or rework lines 600-610 into a remark with the actual Steps I-III. That’s essential for clarity. Additionally, there's a reference issue with the proposition about Lagrangian eigenspaces — it incorrectly mentions an isomorphism not stated in Theorem quantum-complementarity-main. I’ll need to clarify these references properly!
thinking
**Addressing definition issues**

I see that lines 1957-1960 define `\sigma = \mathbb D \circ \mathrm{KS}`, which refers to the Kodaira–Spencer isomorphism. However, Theorem kodaira-spencer-chiral-complete actually establishes an action through Gauss–Manin and anti-commutativity, rather than providing an isomorphism \(V \to V\) for Verdier duality. That means the definition of sigma isn’t valid. I’ll need to fix this by either using the previously constructed involution from Lemma verdier-involution-moduli or defining sigma clearly with Verdier duality and center identification. As for the C2 theorem statement, its scope appears misleading and might require a lower severity classification.
thinking
**Refining the theorem explanation**

Alright, I need to either cite a specific coderived existence theorem from the appendix and mention the functor, or I should modify item (i) to reflect the statement that's actually been proved. The proof essentially says that the curved fiber model has an associated strict flat model \((\bar B^{(g)}(\cA),\Dg{g})\) for ordinary-derived calculations. That sounds great and should clarify things!
thinking
**Considering findings**

I’m thinking that each finding can be concise, perhaps sticking to one line each. It sounds like I could aim for about 14 different findings—nice and clear! That should keep things organized and easy to digest. I’m curious about what specific topics or themes might come up in these findings. Let's explore how to structure them so that they’re informative but also engaging and straightforward!
thinking
**Refining findings layout**

I'm considering how to count my theorem/proof blocks accurately. Maybe "Checked" should reflect the count of those blocks and not just findings. If I set Checked: 20, it means I have 20 findings to present. However, I need to ensure the total doesn’t exceed 70 lines. If each finding is one concise line, I can keep it manageable. I’ll also think about how to incorporate imported source lines without making it too lengthy, focusing on crucial mismatches.
thinking
**Clarifying references**

I think I should keep the mention of references concise in the PROBLEM section. I might say something like, "the cited theorem is `higher_genus_foundations.tex:2061-2081`," since the user wants grounded content. However, I worry there might not be enough direct line references for some findings. Including plain references like `[HIGH] chapters/theory/higher_genus_complementarity.tex:1957` could work well. I’m also considering whether to note any unresolved references, maybe doing that after the summary.
thinking
**Preparing final summary**

I’m thinking about writing my final summary and aiming for 19 bullet points. It seems like I should check back and confirm that everything is in place, like those 19 load-bearing blocks. I want the draft to be succinct yet clear. It feels good to have a clear plan in mind, so I’ll focus on keeping it organized and precise! Let's get started!
codex
- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:477` — PROBLEM: C0 Step 3 jumps from the genus-$g$ flat bar family to `thm:cobar-resolution-scoped` and `thm:obstruction-quantum`, but those imported results live on different objects: the former is a genus-$0$ cobar-resolution theorem (`chapters/theory/higher_genus_foundations.tex:2061-2081`), the latter defines `\mathcal Z(\A)` as `\mathcal H^0` of an endomorphism complex (`chapters/theory/higher_genus_foundations.tex:4588-4607`), not of `R\pi_{g*}\bar B^{(g)}_{\mathrm{flat}}(\A)`. FIX: delete lines 477-481 and insert a new local lemma proving `\mathcal H^0(R\pi_{g*}\bar B^{(g)}_{\mathrm{flat}}(\A))\cong\mathcal Z_\A` directly from the degree-$0$ bar calculation; cite that lemma here.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:818` — PROBLEM: Step I defines `E_1^{p,q,g}` using `d_{\mathrm{fiber}}` and then asserts `d_{\mathrm{fiber}}^2=0`, but the same manuscript’s higher-genus differential convention says `\dfib^{\,2}=\kappa(\A)\omega_g` and only `\Dg{g}^{\,2}=0` (`chapters/theory/higher_genus_foundations.tex:229-270`). FIX: rewrite the spectral sequence with the strict flat differential `\Dg{g}` everywhere, or reformulate Step I in coderived terms and stop taking ordinary cohomology of `\dfib`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:848` — PROBLEM: the Leray argument is run on the trivial product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g`, then the proof immediately treats the fiber as the varying curve `\overline C_p(\Sigma_g)`. That silently replaces the universal family by a constant product. FIX: replace lines 848-853 with the actual universal configuration morphism `\pi_{g,n}:\overline{\mathcal C}_{g,n}\to\overline{\mathcal M}_g` and rewrite the spectral sequence in terms of `R^q\pi_{g,n*}`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:975` — PROBLEM: `Q_g(\A)` is defined as the genus-graded piece of bar cohomology before C1 is proved, then later used as input to prove the C1 eigenspace decomposition. That is circular notation, not a proof. FIX: rename the Step I object to `Q_g^{\mathrm{fil}}(\A)` in lines 964-1011 and downstream uses, and only identify it with `\ker(\sigma-\mathrm{id})` after `lem:eigenspace-decomposition-complete`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:1597` — PROBLEM: the proof-local center-isomorphism lemma uses `thm:e1-module-koszul-duality`, but that source explicitly says the proved module-level package is only on the quadratic genus-$0$ complete/conilpotent `E_1` lane and warns that extending it to arbitrary chiral Koszul pairs needs extra hypotheses (`chapters/theory/chiral_koszul_pairs.tex:5579-5588,5593-5626`). C1 applies it to arbitrary chiral Koszul pairs at all genera. FIX: either restrict C1 to that `E_1` lane, or replace lines 1597-1615 with a genuinely proved center-comparison lemma on the present chiral surface.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:600` — PROBLEM: `thm:quantum-complementarity-main` closes its proof at line 610 with only a roadmap, while the actual argument is split into later standalone proof environments at lines 757-1872. The theorem is structurally unproved in the TeX source. FIX: remove the `\end{proof}` at line 610 and keep Steps I-III inside the same proof, or turn lines 600-610 into a remark and attach a single actual proof environment spanning 757-1872.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:205` — PROBLEM: `def:complementarity-complexes` asserts a cochain involution `\sigma` on `\mathbf C_g(\A)` by citing `thm:verdier-bar-cobar`, but that theorem is a genus-$0$ Ran-space Verdier statement on `\bar B^{\mathrm{ch}}(\A)` (`chapters/theory/cobar_construction.tex:1313-1327`), not an involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\A))`. FIX: move the definition after a standalone construction of `\sigma_g`, or replace lines 205-207 by a forward reference to a new lemma that actually constructs `\sigma_g` on the ambient complex.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:327` — PROBLEM: `lem:perfectness-criterion` proves bounded coherent cohomology by base change, then jumps to “perfect complex” without adding the missing regularity input on `\overline{\mathcal M}_g`. FIX: weaken the conclusion to “bounded complex with coherent cohomology”, or add the explicit theorem/citation that on the smooth DM stack `\overline{\mathcal M}_g`, `D^b_{\mathrm{coh}}=\mathrm{Perf}`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:395` — PROBLEM: C0(i) says the curved fiber model determines a well-defined coderived object, but Step 1 only cites `conv:higher-genus-differentials` and `prop:gauss-manin-uncurving-chain`; the latter explicitly says the curved and flat models are not gauge equivalent and live in different categories (`chapters/theory/higher_genus_foundations.tex:396-410`). The coderived object itself is not constructed here. FIX: cite a real coderived-existence theorem from the coderived appendix, or weaken C0(i) to the statement actually shown: the curved model has an associated strict flat model for ordinary-derived calculations.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1381` — PROBLEM: the Kodaira-Spencer theorem cites `cor:quantum-dual-complete` as if it supplied `\mathbb D:H^*(\bar B^{(g)}(\A))\to H^*(\bar B^{(g)}(\A^!))^\vee`, but that corollary only states `Q_g(\A)\cong Q_g(\A^!)^\vee`. FIX: change the citation to a repaired full bar-complex duality result, or rewrite the sentence so it refers only to the `Q_g` spaces.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1667` — PROBLEM: the proof of `lem:eigenspace-decomposition-complete` assigns the `+1/-1` signs by slogan: lines 1683-1685 invoke an uncited `(-1)^q` rule, and lines 1704-1715 simply assert `\sigma(\beta)=-\beta`. No prior lemma computes these eigenvalues. FIX: insert a separate sign lemma computing the action of `\sigma` on the `j_*` and `j_!` branches with explicit chain-level conventions, or postpone the `Q_g(\A)`/`Q_g(\A^!)` naming until that sign computation exists.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1957` — PROBLEM: `prop:lagrangian-eigenspaces` redefines `\sigma` as `\mathbb D\circ\mathrm{KS}`, while the chapter already used `\sigma=\mathbb D\circ((-)^!)^{-1}` at lines 1503-1509, and it cites “Step 7” of another proof instead of a labeled result. The involution changes definition mid-chapter and the dependency is not a stable claim surface. FIX: promote one construction of `\sigma` to a standalone labeled lemma, cite that lemma here, and delete the `\sigma=\mathbb D\circ\mathrm{KS}` sentence.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2105` — PROBLEM: C2(i) concludes that the BV adjoint map `x\mapsto\{x,-\}_{\mathrm{BV}}` is a quasi-isomorphism and uses `thm:verdier-bar-cobar` on the all-genera curved-central surface, but the assumed theorems `thm:config-space-bv` and `thm:bv-functor` do not state that adjoint-map quasi-isomorphism, and `thm:verdier-bar-cobar` is only genus-$0$ quadratic. FIX: add the adjoint quasi-isomorphism and the needed higher-genus Verdier comparison as explicit hypotheses of C2, or remove the non-degeneracy conclusion from part (i).

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2123` — PROBLEM: C2(ii) calls `L_g:=\bar B^{(g)}(\A)[1]` a dg Lie algebra and says it is a genus truncation of `\Definfmod(\A)` via `prop:modular-deformation-truncation`, but that proposition is about the genus filtration on `\Defcyc^{\mathrm{mod}}(\A)`, not on the raw bar piece. FIX: redefine `L_g` as the genus-$g$ graded piece of `\Defcyc^{\mathrm{mod}}(\A)`, or add a new identification lemma proving that `\bar B^{(g)}(\A)[1]` is closed under the bracket and matches that truncation.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1247` — PROBLEM: `cor:duality-bar-complexes-complete` assumes a direct perfect pairing `\A\otimes\A^!\to\mathcal O_X` and integrates it, but the manuscript’s proved Koszul-duality surface gives a bar-coalgebra / dual-algebra comparison, not this pointwise pairing, and the required degree and dualizing-sheaf shifts are suppressed. FIX: rewrite the corollary as a pairing between `\bar B^{\mathrm{ch}}(\A)` and `\mathbb D_{\mathrm{Ran}}(\bar B^{\mathrm{ch}}(\A))`, then identify that dual object with `\A_\infty^!` only on the regime where `thm:verdier-bar-cobar` applies.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:588` — PROBLEM: the genus-$0$ clause uses unpointed `\overline{\mathcal M}_0` as if it were the same sort of object as the later pointed space `\overline{\mathcal M}_{1,1}`. This section never states the convention that makes the genus-$0$ surface stable. FIX: replace the genus-$0$ space by the stable pointed space actually intended, most likely `\overline{\mathcal M}_{0,3}\cong \mathrm{pt}`, or add an explicit convention before C1 that genus $0$ is read after fixing the three marked points.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1090` — PROBLEM: the Heisenberg example puts `\kappa` inside `Z(\mathcal H_\kappa)`, but throughout the chapter `\kappa` is used as a scalar level/modular-characteristic parameter, not a field in the algebra. FIX: replace `\mathbb C\cdot\mathbf1\oplus\mathbb C\cdot\kappa` by the actual central subspace of the chiral algebra, or keep `\kappa` outside the center example as an external scalar parameter.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1164` — PROBLEM: `thm:verdier-duality-config-complete` is stated at the wrong categorical level: Verdier duality is written as an isomorphism on cohomology groups with a residual `[d]` shift, while the proof is ordinary Poincaré duality by integration. FIX: restate the theorem at the sheaf/complex level `\mathbb D_{\overline C_n(X)}(\mathbf C)\simeq\mathbf C[2n]` and move the cohomological pairing to a corollary.

- [LOW] `chapters/theory/higher_genus_complementarity.tex:467` — PROBLEM: Step 3 says the `E_1`-page vanishing holds “by Step 2”, but Step 2 only defines the filtration; the associated-graded computation is in Step 3 itself. FIX: change “by Step 2” to “by Step 3” or merge the associated-graded argument into Step 2.

## Summary
Checked: 19 | Findings: 19 | Verdict: FAIL
tokens used
149,203
