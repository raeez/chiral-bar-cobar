# OA6_topol_chain (399s)

Only new proposition/proof in the recent change is `prop:sugawara-gauge-rectification`; the review below covers it completely.

**Findings**
- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3776): part (i) claims an explicit primitive `\eta_1` and exact cochain-level rectification, but the source construction only proves the ghost-current term modulo equations of motion and treats the ghost-self-coupling term by an unexpanded “same mechanism” argument ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3662), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3673)). No strict primitive is actually constructed there. FIX: either compute strict primitives for both correction terms on the stated BRST complex and then deduce `[Q,\widetilde G_1]=T_{\mathrm{Sug}}`, or weaken part (i) back to a cohomological/conditional statement.

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3794): part (ii) collapses the brace-coherence tower from shadow depth alone, but the cited support [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1658) controls the BV/bar harmonic discrepancy, not the brace deformation complex, and the same chapter already says those are different obstruction problems ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3475)). The proposition also contradicts itself: it first says only `m_2` contributes, then later uses a nonzero `m_3` without computing `[m_3,\widetilde G_1]` ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3795), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3893)). FIX: add a theorem identifying `D^{(1)}` with the cited harmonic obstruction and compute the degree-3 term explicitly, or downgrade part (ii) to conditional/heuristic.

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3818): the Dunn step is asserted, not proved. From `[m,G]=\partial_z` the text jumps to “locally constant on cochains” and then to `E_3^{top}`, but neither this proposition nor Theorem `thm:topologization` proves the recognition lemma needed to apply HA 5.4.5.9 / 5.1.2.2 on the original complex ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3109), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3924)). FIX: insert a precise lemma showing that brace-level null-homotopy of holomorphic translation yields a locally constant factorization algebra on the original cochain complex, with commuting `E_2^{top}` and `E_1^{top}` structures on the same object; otherwise keep only Theorem `thm:topologization`(ii).

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3952): class `M` non-termination is overstated. Here and at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3998) the file says the gauge procedure does not terminate, but earlier the same file only says the infinite coherence tower is expected and that MC5 gives evidence rather than proof ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3420), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3486)); the cited class-`M` result only proves curvature-divisible harmonic discrepancies, not divergence of the gauge series ([bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1786)). FIX: change the class `M` language back to conjectural/expected, or add a separate proof of non-termination in the brace deformation complex.

- PROBLEM at [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7321): claim-surface sync is stale. Concordance still presents the original-complex lift as conditional on `[m,G]=\partial_z`, and `metadata/theorem_registry.md` has no `prop:sugawara-gauge-rectification` entry. FIX: if the proposition survives, update concordance and regenerate metadata; if it is downgraded, keep the current concordance scope and remove the new `ProvedHere` surface.

**Checks**
Label/status check passed syntactically: `\label{prop:sugawara-gauge-rectification}` is unique across Vols I–III, and the environment/tag pairing is `proposition` + `\ClaimStatusProvedHere`.

No direct AP126, AP132, AP165, AP113, or AP29 hit appears in the audited proposition block. The problems are proof gaps and status drift.


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
session id: 019d889b-ab57-71d1-913d-7b33ecf39950
--------
user
<task>
You are a Beilinson rectification auditor. Read the RECENT changes to the assigned file.
These changes were written by automated mathematical research agents. Your job:
(1) Verify mathematical correctness of every new proposition and proof
(2) Check all labels are unique, environments match status tags
(3) Check no AP violations introduced (AP126, AP132, AP29, AP165, AP113)
(4) Flag any gaps, incorrect steps, or unjustified claims
For each finding: PROBLEM at file:line + FIX.
</task>
<grounding_rules>Ground every claim in the file contents you read.</grounding_rules>
<completeness_contract>Audit EVERY new proposition and proof in the file.</completeness_contract>


Audit prop:sugawara-gauge-rectification in chapters/theory/en_koszul_duality.tex. Verify: gauge transformation convergence for class G/L (finite depth), non-convergence for class M, Dunn additivity step.
mcp startup: no servers


thinking
**Auditing recent changes**

I need to audit recent changes to a file, following the user's request. First, I'll inspect the repository and the AGENTS instructions. It's important to review the relevant documents before making any edits, even if this is about auditing rather than editing. The user mentioned being a Beil rectification auditor, so I should focus on using the deep-beilinson-audit for this task. I might also look into the git diff for recent changes to the assigned file.
thinking
**Auditing gauge rectification**

I need to audit the `prop:sugawara-gauge-rectification` in the specified LaTeX file. My goal is to verify specific items and produce findings with clear indications of any problems along with suggested fixes. If I find nothing, I should explicitly state that there are no findings and outline any risks or testing gaps. I’ll focus on inspecting the propositions, proofs, and recent changes. It’s essential to review constitutional files before proceeding, and I might run grep for unique labels across volumes.
codex
Auditing the recent edits in `chapters/theory/en_koszul_duality.tex` and grounding the check in the live source first. I’m pulling the file diff, the proposition/proof context, and the required repo-wide status surfaces before I judge the new argument.
exec
/bin/zsh -lc "sed -n '1,240p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 51ms:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ea48c7..e24ea99 100644
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@ $C^*(\fg) = \Sym(\fg^\vee[-1])$.
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,240p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
 succeeded in 51ms:
\chapter{\texorpdfstring{$\En$ Koszul duality and higher-dimensional bar complexes}{En Koszul duality and higher-dimensional bar complexes}}
\label{ch:en-koszul-duality}

\index{En algebra@$\En$ algebra!Koszul duality|textbf}
\index{bar complex!higher-dimensional|textbf}

For $\En$ algebras, the bar-cobar adjunction replaces the logarithmic
propagator $d\log(z-w)$ with a closed $(n{-}1)$-form, the Arnold
relations with the Totaro relations, and chiral Koszul duality with
$\En$ Koszul duality. The underlying construction is the same:
duality is mediated by a convolution algebra on a compactified
configuration space. The passage from $n = 1$
(associative/$A_\infty$) through $n = 2$ (the holomorphic refinement
recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
Vassiliev invariants) and beyond exhibits bar-cobar duality as a
single construction parametrised by manifold dimension, with the
formality phenomena of Kontsevich and Tamarkin as shadows of the
Koszul property in each dimension.

The chapter culminates in the chiral center theorem
codex
Using the `deep-beilinson-audit` workflow here because this is a local proof audit, not a rewrite. Next I’m isolating `prop:sugawara-gauge-rectification`, its proof dependencies, and the recent diff around that block to test the exact convergence and Dunn-additivity claims.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5000,5400p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:sugawara-gauge-rectification|Dunn additivity|gauge rectification|class G|class L|class M|finite depth|non-convergence|Sugawara" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff --unified=80 -- chapters/theory/en_koszul_duality.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
25:$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
33:original BRST complex is proved by gauge rectification of the
34:Sugawara contraction together with finite shadow depth
35:(Proposition~\ref{prop:sugawara-gauge-rectification}). For class~M
1082: % has higher components; sigma_5 for class L arises from Phi_2(S_2, S_3),
1083: % not directly from S_5 (which vanishes for class L). This is consistent:
1084: % class L has S_3 != 0 but S_r = 0 for r >= 4, and the wheel sigma_5
2947:\index{Sugawara construction!topologization}
2987:the Sugawara element
3001:The Sugawara element
3045:  $G_1$ equal to the Sugawara antighost contraction of
3059:with $\Ethree^{\mathrm{top}}$ is Dunn additivity. For
3086:$\mathsf{SC}^{\mathrm{ch,top}}$), Dunn additivity gives
3112:higher homotopies extending the unary Sugawara contraction.
3116:Lurie's recognition theorem and Dunn additivity therefore
3123:At $k = -h^\vee$, the Sugawara denominator
3124:$2(k + h^\vee)$ diverges: the Sugawara element is undefined,
3174:$k \neq -h^\vee$, where the Sugawara element provides
3187:\textup{(}Proposition~\ref{prop:sugawara-gauge-rectification}\textup{)}.
3188:The last step uses gauge rectification of the Sugawara
 succeeded in 51ms:

The Sugawara constraint
(Theorem~\ref{thm:e3-identification}(iv)) requires
separate analysis: the Sugawara element for
$\mathfrak{gl}_N$ at levels $(k_1, k_2)$ involves only
the $\mathfrak{sl}_N$ factor at non-critical level
$k_1 \neq -N$; the $\mathfrak{gl}_1$ factor contributes
independently to the stress tensor. The topological
enhancement holds at generic $(k_1, k_2)$ with
$k_1 \neq -N$.
\end{remark}

% ========================================================
\subsection{Explicit $\Ethree$ operations for
$V_k(\mathfrak{sl}_2)$}
\label{subsec:e3-explicit}

The abstract $\Ethree$ structure of
Theorem~\ref{thm:e3-cs} acquires concrete content
for $\fg = \mathfrak{sl}_2$: the five-dimensional derived
 succeeded in 51ms:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ea48c7..e24ea99 100644
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4383,160 +4383,235 @@ On the original complex, both routes remain cohomological:
 the Dunn route uses local constancy only after passing to
 BRST cohomology, and the HDC route uses formality to compare
 chain-level operations with their cohomological shadow. For
 affine Kac--Moody, Theorem~\ref{thm:topologization} adds the
 stronger statement that the cohomology complex itself is an
 unconditional chain-level $\Ethree^{\mathrm{top}}$ model on a
 quasi-isomorphic complex. What remains open is the lift to
 the original cochain complex, governed by the
 $A_\infty$-coherence equation
 $[m,G]=\partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}.
 For class~M algebras, even the cohomological route still
 depends on the conjectural bulk BRST construction
 (Conjecture~\ref{conj:topologization-general}), and the
 coderived alternative remains Conjecture~\ref{conj:coderived-e3}.
exec
/bin/zsh -lc 'rg -n "sugawara-gauge-rectification|topologization|constr:sugawara-antighost|rem:topologization-chain-vs-cohomology|thm:topologization|sc-two-incarnations|E_3|Ethree|Dunn" chapters/theory/en_koszul_duality.tex chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
chapters/theory/en_koszul_duality.tex:24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
chapters/theory/en_koszul_duality.tex:25:$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
chapters/theory/en_koszul_duality.tex:27:The topologization proof is made constructive by an explicit
chapters/theory/en_koszul_duality.tex:31:(Construction~\ref{constr:sugawara-antighost}). For affine
chapters/theory/en_koszul_duality.tex:32:Kac--Moody at non-critical level, the chain-level $\Ethree$ on the
chapters/theory/en_koszul_duality.tex:35:(Proposition~\ref{prop:sugawara-gauge-rectification}). For class~M
chapters/theory/en_koszul_duality.tex:36:algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
chapters/theory/en_koszul_duality.tex:1276:\label{princ:sc-two-incarnations}
chapters/theory/en_koszul_duality.tex:1301:  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
chapters/theory/en_koszul_duality.tex:1302:  topologization theorem
chapters/theory/en_koszul_duality.tex:1303:  (Theorem~\textup{\ref{thm:topologization}}).
chapters/theory/en_koszul_duality.tex:1308:  strictly weaker than $\Ethree$.
chapters/theory/en_koszul_duality.tex:1314:$\mathsf{SC}^{\mathrm{ch,top}}$ (or $\Ethree$) output.
chapters/theory/en_koszul_duality.tex:1358:\textup{(}Principle~\textup{\ref{princ:sc-two-incarnations}}\textup{)}.
chapters/theory/en_koszul_duality.tex:2101:$E_2$ to $E_3$ for $E_1$-chiral input requires the Drinfeld
chapters/theory/en_koszul_duality.tex:2939:% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
chapters/theory/en_koszul_duality.tex:2944:\texorpdfstring{$\Ethree$}{E3}}
chapters/theory/en_koszul_duality.tex:2945:\label{sec:topologization}
chapters/theory/en_koszul_duality.tex:2946:\index{topologization theorem|textbf}

thinking
**Evaluating mathematical edits**

I’m thinking about whether more edits are necessary, but the instructions say I need to fill out the Pre-Edit Verification before making any surface edits in hot zones. Since this is only an audit and not editing, maybe I don’t need to do it yet. However, if I do later edit, I’ll need to check the theorem on topologization, as well as various dependencies. I should also review the proof for related theorems and ensure mathematical correctness for various classes.
codex
I’ve isolated the relevant surface: `prop:sugawara-gauge-rectification` is a `ProvedHere` proposition that explicitly claims chain-level `E_3^{top}` on the original BRST complex, with class `G/L` convergence and class `M` failure separated inside the proof. I’m now checking whether each imported input actually gives those conclusions, or whether the proof silently upgrades a cohomological or transferred-model statement into an original-complex statement without enough control.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2990,3425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3550,3975p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2990	provides the inner conformal vector. For the
  2991	Virasoro algebra, $T(z)$ is the stress tensor itself.
  2992	\end{definition}
  2993	
  2994	\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
  2995	\label{thm:topologization}
  2996	\ClaimStatusProvedHere
  2997	\index{topologization theorem!statement}
  2998	Let $\fg$ be a finite-dimensional simple Lie algebra
  2999	and let $\cA = V_k(\fg)$ be the universal affine
  3000	vertex algebra at non-critical level $k \neq -h^\vee$.
  3001	The Sugawara element
  3002	$T_{\mathrm{Sug}} = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J_a{:}$
  3003	provides an inner conformal vector
  3004	\textup{(}Definition~\textup{\ref{def:inner-conformal-vector}}\textup{)}.
  3005	The chiral
  3006	center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, which carries
  3007	$\Etwo$ structure from the closed sector of
  3008	$\mathsf{SC}^{\mathrm{ch,top}}$
  3009	\textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
 succeeded in 52ms:
  3550	\end{remark}
  3551	
  3552	\begin{construction}[The Sugawara antighost contraction for affine
  3553	Kac--Moody]
  3554	\label{constr:sugawara-antighost}%
  3555	\index{Sugawara construction!antighost contraction $G(z)$|textbf}%
  3556	\index{topologization theorem!explicit $G(z)$}%
  3557	\index{antighost contraction|textbf}%
  3558	\ClaimStatusProvedHere
  3559	The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
  3560	existence of $G(z)$ witnessing the inner conformal vector in BRST
  3561	cohomology but does not construct it. We supply the explicit
  3562	operator and verify the cohomological identity.
  3563	
  3564	Let $\fg$ be a finite-dimensional simple Lie algebra with basis
  3565	$\{t_a\}_{a=1}^{\dim\fg}$, structure constants
  3566	$f^a{}_{bc}$ ($[t_b, t_c] = f^a{}_{bc}\,t_a$), Killing form
  3567	$\kappa_{ab} = \operatorname{tr}(t_a t_b)$, and dual Coxeter number
  3568	$h^\vee$. Fix a non-critical level $k \ne -h^\vee$.
  3569	
exec
/bin/zsh -lc 'git log --oneline --follow -- chapters/theory/en_koszul_duality.tex | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git blame -L 3756,3950 -- chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:sugawara-gauge-rectification|label\\{prop:sugawara-gauge-rectification\\}|ref\\{prop:sugawara-gauge-rectification\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
e37cc33 Topologization chain-level: gauge rectification proves E_3 on original BRST complex for affine KM (AP210 resolved)
02336ae Final gaps + elite rescue: 85 source files rectified across theory, examples, connections
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
4641d30 Elliptic Drinfeld coproduct (31 tests) + Jones Markov trace engine
56cd1ab Final sync: late-arriving frontier agent results
971b573 Final session sync: all late-arriving agent results
7ded6e5 Late-arriving frontier agent edits: chiral Koszul pairs scope tightening, higher-genus complementarity cross-reference update
767abfe Cross-volume: 6d hCS defect result from Vol III
fd56627 Coderived E_3 obstruction analysis: Steps 1-2 proved, Step 3 (categorical infrastructure) open. conj:coderived-e3 stays conjectural.
9bb2f07 CONJECTURE → THEOREM: Miura cross-term universality PROVED from Prochazka-Rapcak
bb6b7b4 Final sync before frontier swarm
9505674 Final session sync: all frontier agent results and build artifacts
2e5a612 Wave 2 healing swarm: verification engines, alternative proofs, formula cross-checks
a0f29d9 20-agent HEAL swarm: sign convention, cross-volume formulas, Belavin correction, E_3 formality lemma, gl_3 engine, spin-3 Miura, genus-2 factorization, P_3 Jacobi, BV vanishing, Verlinde 3-path, ker(av) basis, W_N descent, formality bridge, CFG chain-level, AP29 sweep, antipode frontier, standalone zero undef refs
ab0b09c Rectification wave 2: off-locus inversion, E_n expansion, ordered chiral KD, shadow tower deepening
7c16cec First-principles rectification of core theorem architecture (12 theory chapters)
b6cc11d Grammatical fix: 'an degree' -> 'a degree' across 16 files (article mismatch from arity->degree rename)
6c053bb Vol I: CLAUDE.md audit update, new compute engines, standalone and build sync
445a834 E_n Koszul duality expansion, chiral center Gerstenhaber bracket, and theory-wide degree normalisation (26 chapters)
5a55840 Core mathematical content: E_1 coalgebra recast, topologisation theory, ordered chiral Koszul duality
 succeeded in 50ms:
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3756) \begin{proposition}[Chain-level $\Ethree^{\mathrm{top}}$ for
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3757) affine Kac--Moody via gauge rectification]
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3758) \label{prop:sugawara-gauge-rectification}%
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3759) \index{topologization theorem!chain-level for affine KM|textbf}%
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3760) \index{Sugawara construction!gauge rectification|textbf}%
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3761) \index{E3 algebra@$\Ethree$ algebra!chain-level for affine KM|textbf}%
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3762) \ClaimStatusProvedHere
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3763) Let $\fg$ be a finite-dimensional simple Lie algebra and
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3764) $\cA = V_k(\fg)$ the universal affine vertex algebra at
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3765) non-critical level $k \neq -h^\vee$. The derived chiral
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3766) center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits a
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3767) chain-level $\Ethree^{\mathrm{top}}$-algebra structure on
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3768) the original BRST complex
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3769) \textup{(}not merely on a quasi-isomorphic
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3770) model\textup{)}.
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3771) \begin{enumerate}[label=\textup{(\roman*)}]
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3772) \item \textup{(Gauge-rectified Sugawara contraction.)}
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3773)   The antighost contraction $G_1 = G(z)$ of
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3774)   Construction~\textup{\ref{constr:sugawara-antighost}}
e37cc33b (Raeez Lorgat 2026-04-13 22:38:03 +0200 3775)   satisfies
 succeeded in 100ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:35:(Proposition~\ref{prop:sugawara-gauge-rectification}). For class~M
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3187:\textup{(}Proposition~\ref{prop:sugawara-gauge-rectification}\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3435:Proposition~\ref{prop:sugawara-gauge-rectification}; for class~$M$,
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3547:  Proposition~\ref{prop:sugawara-gauge-rectification}
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3758:\label{prop:sugawara-gauge-rectification}%
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3964:Proposition~\ref{prop:sugawara-gauge-rectification}
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3994:  Proposition~\ref{prop:sugawara-gauge-rectification}
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:6679:(Proposition~\ref{prop:sugawara-gauge-rectification}). For class~M

thinking
**Examining obstruction properties**

I think I need to dive into examining something called chain-level three obstructions and the related theorem or class depth. It sounds like I should search through the lines around that relevant proposition. I might also need to verify the finite depth of class G/L and something about class M not converging. Let’s see! I’ll go ahead and search for those details to clarify my understanding.
codex
The proof’s weak point is already visible: it cites finite shadow depth to collapse the whole `A_\infty` coherence tower, but I haven’t yet seen a source that identifies that tower with the shadow tower strongly enough to justify `G_k=0` for `k≥2`. I’m checking the exact supporting proposition it invokes and whether class `M` non-convergence is actually proved anywhere or just heuristic prose.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '7000,7155p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4040,4235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"chain-level-three-obstructions|cubic harmonic obstruction|shadow depth|r_max = 3|class~\\\\"'$L|class~'"\\\\"'$M|infinite shadow|coherence tower|brace deformation complex" chapters/theory/en_koszul_duality.tex chapters/connections/concordance.tex chapters/theory/*.tex chapters/examples/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7000	
  7001	%================================================================
  7002	% SECTION: E_3 BAR ALGEBRA STRUCTURE
  7003	%================================================================
  7004	
  7005	\section{\texorpdfstring{$\Etwo$ structure on the symmetric bar and the $\mathsf{E}_3$ obstruction}{E2 structure on the symmetric bar and the E3 obstruction}}
  7006	\label{sec:e3-bar-structure}
  7007	\index{bar complex!E2 structure@$\Etwo$ structure|textbf}
  7008	\index{E3 obstruction@$\mathsf{E}_3$ obstruction|textbf}
  7009	
  7010	The symmetric chiral bar complex $\barB^{\Sigma}(\cA)$ of a chiral
  7011	algebra on a curve carries a natural $\Etwo$ structure from the local
  7012	configuration spaces $\Conf_k(\bC)$. It is obtained from the
  7013	ordered primitive $\barB^{\mathrm{ord}}(\cA)$ by the lossy
  7014	$R$-twisted $\Sigma_n$-coinvariant passage. It does \emph{not}
  7015	carry an $\mathsf{E}_3$ structure: a curve provides only~$\bR^2$,
  7016	and the passage to $\mathsf{E}_3$ requires $\bR^3$ geometry. The
  7017	correct statement is that, for $\Einf$-chiral algebras
  7018	(where $\barB^{\Sigma}(\cA)$ exists), the \emph{derived center}
  7019	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 succeeded in 52ms:
  4040	  chain-level lift, and it is compatible with the coderived
  4041	  BV$=$bar identification of
  4042	  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
  4043	\end{enumerate}
  4044	\end{conjecture}
  4045	
  4046	\begin{remark}[Structure of the coderived $\Ethree$ conjecture]
  4047	\label{rem:coderived-e3-structure}%
  4048	\index{coderived category!E3 structure@$\Ethree$ structure!mechanism}%
  4049	The conjecture synthesises three proved results with one new
  4050	principle.
  4051	The three proved results are:
  4052	\begin{enumerate}[label=\textup{(\alph*)}]
  4053	\item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the
  4054	  pair $(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\, \cA)$ is
  4055	  chain-level
  4056	  (Theorem~\ref{thm:operadic-center-hochschild}).
  4057	\item The coderived BV$=$bar identification absorbs all
  4058	  $m_0$-proportional obstructions for every shadow class
  4059	  (Theorem~\ref{thm:bv-bar-coderived}).
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:34:Sugawara contraction together with finite shadow depth
chapters/theory/en_koszul_duality.tex:892:\index{shadow depth!$\En$ independence}
chapters/theory/en_koszul_duality.tex:893:For a formal $\En$-algebra, the shadow depth class (G/L/C/M
chapters/theory/en_koszul_duality.tex:2841:\index{shadow depth!truncation produces deficient pair}
chapters/theory/en_koszul_duality.tex:3051:  in the brace deformation complex, then
chapters/theory/en_koszul_duality.tex:3111:brace deformation complex by an $A_\infty$-coherent family of
chapters/theory/en_koszul_duality.tex:3189:contraction together with the finite shadow depth of
chapters/theory/en_koszul_duality.tex:3192:$A_\infty$-coherence tower of
chapters/theory/en_koszul_duality.tex:3289:  the corresponding $A_\infty$-coherence tower trivializing
chapters/theory/en_koszul_duality.tex:3395:in the brace deformation complex. In degree~$n$, this means
chapters/theory/en_koszul_duality.tex:3422:nontrivial, this coherence tower is expected to be genuinely
chapters/theory/en_koszul_duality.tex:3454:  bypasses the brace deformation complex and recovers the same
chapters/theory/en_koszul_duality.tex:3478:  cocycle $\partial_z$ in the brace deformation complex. The ambient
chapters/theory/en_koszul_duality.tex:3518:  brace deformation complex with its controlling dg Lie algebra,
chapters/theory/en_koszul_duality.tex:3540:  class~$L$ has finite shadow depth $r_{\max} = 3$,
chapters/theory/en_koszul_duality.tex:3541:  the cubic harmonic obstruction vanishes by Jacobi
chapters/theory/en_koszul_duality.tex:3542:  \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)},
chapters/theory/en_koszul_duality.tex:3786:\item \textup{(Termination of the coherence tower.)}
chapters/theory/en_koszul_duality.tex:3791:  lands in the brace deformation complex.
chapters/theory/en_koszul_duality.tex:3794:  For $V_k(\fg)$, class~$L$ has shadow depth
exec
/bin/zsh -lc 'rg -n -i "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate|perhaps|seems to|appears to|---|—" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:chain-level-three-obstructions\\}|label\\{thm:topologization\\}|label\\{conj:coderived-e3\\}|label\\{princ:sc-two-incarnations\\}|label\\{thm:operadic-center-hochschild\\}|label\\{thm:brace-dg-algebra\\}|label\\{thm:htt-operadic\\}\" chapters/theory/en_koszul_duality.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 66ms:
chapters/theory/en_koszul_duality.tex:1276:\label{princ:sc-two-incarnations}
chapters/theory/en_koszul_duality.tex:1821:\label{thm:operadic-center-hochschild}
chapters/theory/en_koszul_duality.tex:2995:\label{thm:topologization}
chapters/theory/en_koszul_duality.tex:4007:\label{conj:coderived-e3}%
chapters/theory/chiral_center_theorem.tex:610:\label{thm:brace-dg-algebra}
chapters/theory/en_koszul_duality.tex:1276:\label{princ:sc-two-incarnations}
chapters/theory/en_koszul_duality.tex:1821:\label{thm:operadic-center-hochschild}
chapters/theory/en_koszul_duality.tex:2995:\label{thm:topologization}
chapters/theory/en_koszul_duality.tex:4007:\label{conj:coderived-e3}%
 succeeded in 73ms:
2782:\item \emph{Standard landscape.}
2783: For every family in the standard landscape (Heisenberg, affine
codex
I’ve found a second structural issue: the file itself still says at [chapters/theory/en_koszul_duality.tex]( /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3420 ) that for class `M` the coherence tower is only “expected” to be infinite, but the new proposition later upgrades that to a definitive non-termination claim. I’m checking whether there is an actual proved proposition in this file or elsewhere that bridges that gap.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3420,3555p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3420	For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
  3421	where SC non-formality means all $m_k^{\mathrm{SC}}$ are
  3422	nontrivial, this coherence tower is expected to be genuinely
  3423	infinite. That is why the original-complex
  3424	$\Ethree$ remains open even when the cohomological statement
  3425	is the expected endpoint.
  3426	\end{remark}
  3427	
  3428	\begin{remark}[Research direction: chain-level topologization]
  3429	\label{rem:research-chain-level-topologization}
  3430	\index{topologization theorem!chain-level research direction}%
  3431	\index{Sugawara construction!gauge rectification programme}%
  3432	Theorem~\ref{thm:topologization} separates the problem into a proved
  3433	homotopy-invariant lane and an original-complex lane. For affine
  3434	Kac--Moody, the original-complex lane is resolved by
  3435	Proposition~\ref{prop:sugawara-gauge-rectification}; for class~$M$,
  3436	the original-complex $\Ethree$ remains open on the ordinary complex
  3437	and requires the coderived approach
  3438	(Conjecture~\ref{conj:coderived-e3}). The status sharpens as follows.
  3439	\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "rg -n \"class~\\\\\\"'$M.*(infinite|does not terminate|fails)|coherence tower.*class~'"\\\\\\"'$M|ordinary chain-level '"\\\\Ethree fails|quartic discrepancy|delta_4\" chapters/theory/en_koszul_duality.tex chapters/theory/*.tex chapters/examples/*.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bv-bar-coderived\\}|label\\{prop:coderived-adequacy\\}|label\\{thm:htt-operadic\\}|label\\{thm:operadic-center-hochschild\\}\" /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:chain-level-three-obstructions\\}|begin\\{proposition\\}.*chain-level three obstructions|chain-level three obstructions|cubic harmonic obstruction\" /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar exited 2 in 65ms:
rg: regex parse error:
    (?:class~\$M.*(infinite|does not terminate|fails)|coherence tower.*class~\$M|ordinary chain-level \Ethree fails|quartic discrepancy|delta_4)
                                                                                                      ^^
error: unrecognized escape sequence
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2289:\label{thm:bv-bar-coderived}%
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1821:\label{thm:operadic-center-hochschild}
/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:251:\label{prop:coderived-adequacy}
 succeeded in 153ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:10306:\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:21472:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:32636:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:43801:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:54966:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:66129:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:77292:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:88430:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:99613:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:110786:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:121980:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:133187:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:144380:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:155556:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:166733:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:177915:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:189017:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:200753:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:212489:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H11_SC_formal_alt.md:224226:-\newlabel{prop:chain-level-three-obstructions}{{T.7.3}{2453}{Three chain-level obstructions and harmonic factorization; \ClaimStatusProvedHere }{proposition.T.7.3}{}}

thinking
**Inspecting proposition connections**

I need to look closely at the chapters and connections in the `bv_brst.tex` file, particularly around the proposition dealing with the chain-level-three obstructions and possibly a theorem regarding class M failure. It seems like I might also need to consider using a simpler pattern with rg. I’ll dive into this context to see what insights I can find relevant to those areas. Let's see how they all connect!
codex
The proposition it cites lives in `chapters/connections/bv_brst.tex`, so I’m checking whether that result actually identifies the relevant brace-defect terms, or only a different BV/bar obstruction cone. If it’s the latter, the new proof is importing the wrong obstruction theory.
exec
/bin/zsh -lc "rg -n \"ordinary chain-level E_3 fails|ordinary chain-level \\\\Ethree fails|quartic discrepancy|delta_4|coherence tower is expected|expected to be genuinely infinite|original-complex \\\\Ethree remains open|class M\" chapters/theory/en_koszul_duality.tex chapters/connections/bv_brst.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1600,1765p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:ordinary chain-level E_3 fails|ordinary chain-level \Ethree fails|quartic discrepancy|delta_4|coherence tower is expected|expected to be genuinely infinite|original-complex \Ethree remains open|class M)
                                                           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1600	
  1601	\medskip
  1602	\noindent\textbf{Path \textup{(d)}: numerical verification.}
  1603	\index{multi-path verification!Heisenberg BV/bar}
  1604	At each genus $g = 1, \ldots, 15$, three independent
  1605	implementations produce the same rational number $\lambda_g^{\mathrm{FP}}$:
  1606	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  1607	\item the Bernoulli formula
  1608	 $\lambda_g^{\mathrm{FP}}
  1609	 = \frac{(2^{2g-1}-1)\,|B_{2g}|}{2^{2g-1}\,(2g)!}$;
  1610	\item the Taylor extraction of the $\hat{A}$-series
  1611	 $(\hbar/2)/\sin(\hbar/2) - 1
  1612	 = \sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\,\hbar^{2g}$;
  1613	\item a direct computation of the Faber--Pandharipande
  1614	 intersection integral on $\overline{\mathcal{M}}_{g,1}$
  1615	 via the string/dilaton equation and Witten's conjecture.
  1616	\end{enumerate}
  1617	All three agree at every genus tested. Sample values:
  1618	$\lambda_1^{\mathrm{FP}} = 1/24$,
  1619	$\lambda_2^{\mathrm{FP}} = 7/5760$,
exec
/bin/zsh -lc "rg -n \"Theorem~5\\.4\\.5\\.9|5\\.1\\.2\\.2|locally constant factorization algebras on \\\\bC|Dunn additivity|Etwo\\"'^'"\\{\\\\mathrm\\{top\\}\\} \\\\otimes \\\\Eone\\"'^'"\\{\\\\mathrm\\{top\\}\\}\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '560,700p'" in /Users/raeez/chiral-bar-cobar exited 2 in 149ms:
rg: regex parse error:
    (?:Theorem~5\.4\.5\.9|5\.1\.2\.2|locally constant factorization algebras on \bC|Dunn additivity|Etwo\^\{\mathrm\{top\}\} \otimes \Eone\^\{\mathrm\{top\}\})
                                                                                                            ^^
error: unrecognized escape sequence
 succeeded in 133ms:
   560	\begin{proposition}[Pre-Lie relation for the single brace; \ClaimStatusProvedHere]
   561	\label{prop:pre-lie-chiral}
   562	\index{pre-Lie!chiral braces}
   563	The single-brace operation on $C^\bullet_{\mathrm{ch}}(A, A)$
   564	satisfies the pre-Lie identity: for all $a, b, c$,
   565	\[
   566	a\{b\}\{c\} - a\{b\{c\}\}
   567	= (-1)^{\|b\| \cdot \|c\|}
   568	\bigl(a\{c\}\{b\} - a\{c\{b\}\}\bigr).
   569	\]
   570	\end{proposition}
   571	
   572	\begin{proof}
   573	Both sides are double insertions into~$a$. On the
   574	left, $a\{b\}\{c\}$ inserts $b$ first (at position~$i$)
   575	then $c$ (at position~$j$), while $a\{b\{c\}\}$
   576	inserts $c$ into~$b$ first and then the composite
   577	into~$a$. The non-nested terms ($i \ne j$ and $c$ not
   578	inside~$b$) on the left are paired with the corresponding
   579	non-nested terms on the right (with~$b$ and $c$ exchanged)
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1764,1828p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1764	\delta_r^{\mathrm{harm}}
  1765	\;=\;
  1766	c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
  1767	\qquad\text{for every } r \geq 4.
  1768	\]
  1769	For class~G, there are no interaction vertices, so every
  1770	$c_r(\cA)$ vanishes. For class~L
  1771	\textup{(}affine Kac--Moody at non-critical level
  1772	$k \neq -h^\vee$\textup{)}, the interaction vertex is the
  1773	structure-constant tensor $f^{abc}$. The cubic harmonic
  1774	correction has the form
  1775	$\sum_c f^{abc}\cdot I_{\mathrm{harm}}(z_1,z_2)\cdot f^{cde}$,
  1776	where $I_{\mathrm{harm}}$ is the integral of the harmonic
  1777	propagator against the cubic vertex measure. Antisymmetry of
  1778	$f^{abc}$ and the Jacobi identity
  1779	$f^{abc}f^{cde} + \text{cyclic} = 0$ force this coefficient to
  1780	vanish, and shadow depth $r_{\max} = 3$ excludes quartic and
  1781	higher terms. For class~C
  1782	\textup{(}$\beta\gamma$\textup{)}, the quartic correction is the
  1783	first possible harmonic term; when the harmonic insertion factors
codex
I’ve confirmed the label and environment surface: `prop:sugawara-gauge-rectification` is unique across the three volumes and the `prop:` / `\ClaimStatusProvedHere` pairing is internally consistent. The remaining question is truth, and the imported support currently looks weaker than the proposition advertises.
exec
/bin/zsh -lc "git show --stat --summary e37cc33 -- chapters/theory/en_koszul_duality.tex && git show --unified=40 e37cc33 -- chapters/theory/en_koszul_duality.tex | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
commit e37cc33be05621cd80e3e48dcfa1b012375d0096
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:38:03 2026 +0200

    Topologization chain-level: gauge rectification proves E_3 on original BRST complex for affine KM (AP210 resolved)
    
    prop:sugawara-gauge-rectification proves chain-level E_3 on the ORIGINAL BRST
    complex (not just a qi-equivalent model) for affine Kac-Moody V_k(g) at non-critical
    level k != -h^v. This resolves the chain-level gap identified in the 832-agent audit.
    
    The proof constructs an explicit gauge transformation that rectifies the Sugawara
    antighost contraction G(z) so that [Q, G'] = T_Sug EXACTLY at the cochain level
    (not just up to Q-exact corrections). The key ingredients:
    
    (1) The Q-exact correction [Q, eta] from the original Sugawara construction is
        explicit for affine KM: it comes from the OPE of G with itself via the
        current algebra structure.
    
    (2) The gauge transformation exp(ad_eta) converges because the shadow depth for
        class L (affine KM) is FINITE (d_alg = 1): the correction terms terminate
exec
/bin/zsh -lc 'rg -n "sugawara-gauge-rectification" metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 78ms:



thinking
**Considering metadata issues**

I'm looking at a proposition that's not in the theorem registry or concordance, which could be due to outdated metadata. The user wants to ensure all labels match unique environment status tags. I can confirm that the labels are unique, but I'm not sure about the claim-surface sync because the registry isn't updated. The user didn't directly ask about syncing but mentioning the metadata drift as a finding seems reasonable. Still, it's a sync issue, and I wonder how this ties to environment status.
thinking
**Inspecting theorem updates**

I need to check if the theorem registry isn't updated because it hasn't auto-regenerated from the current HEAD. It might be stale since the proposition is absent—possibly generated earlier. The user asked for unique labels and matching environment status tags, which I can confirm. However, the registry lacks the new, proved claim, indicating metadata drift. This might be a finding, but only if the user requested "claim-surface sync." I might also need to inspect concordance for relevant details around 7321.
codex
I checked the metadata surfaces too. `prop:sugawara-gauge-rectification` is not present in `metadata/theorem_registry.md` or `chapters/connections/concordance.tex`, so even before judging the proof there is claim-surface drift: the file now advertises a new `ProvedHere` result that the central status surfaces do not record.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7308,7345p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"topologization|original complex|quasi-isomorphic model|gauge rectification|Sugawara\" chapters/connections/concordance.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7308	 See Vol~II CLAUDE.md, AP165/B54--B56.} \\
  7309	\hline
  7310	\multicolumn{3}{p{13cm}}{%
  7311	 \textbf{SC self-duality retracted.}
  7312	 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
  7313	 \text{shuffle-mixed})$: the closed dimensions are
  7314	 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
  7315	 Koszul self-dual. The duality \emph{functor} is an
  7316	 involution; the \emph{operad} is not self-dual.
  7317	 See AP166/B57.} \\
  7318	\hline
  7319	\multicolumn{3}{p{13cm}}{%
  7320	 \textbf{Topologization scoped.}
  7321	 The cohomological topologization theorem
  7322	 (Theorem~\ref{thm:topologization}:
  7323	 $\SCchtop + \text{inner conformal vector}
  7324	 \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  7325	 is proved for affine Kac--Moody at non-critical level.
  7326	 The same theorem gives an unconditional chain-level
  7327	 $E_3^{\mathrm{top}}$ model on the zero-differential
 succeeded in 52ms:
7290: & Sugawara antighost construction:
7292: antighost field for topologization
7321: The cohomological topologization theorem
7322: (Theorem~\ref{thm:topologization}:
7334: (Conjecture~\ref{conj:topologization-general}).} \\
9688:SC self-duality retraction, topologization scoping, critical-level
9701:\item \textbf{FT-5} (topologization scope):
9702: \emph{passed}. Cohomological topologization
exec
/bin/zsh -lc 'rg -n "sugawara-gauge-rectification|topologization|gauge rectification" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3960,4015p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
673:| `thm:topologization` | `theorem` | 2991 | Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}} |
 succeeded in 51ms:
  3960	
  3961	\begin{remark}[Three approaches to chain-level topologization]
  3962	\label{rem:three-approaches-chain-level}%
  3963	\index{topologization theorem!three approaches to chain-level}%
  3964	Proposition~\ref{prop:sugawara-gauge-rectification}
  3965	resolves the chain-level topologization for affine Kac--Moody
  3966	by combining three independent strategies.
  3967	\begin{enumerate}[label=\textup{(\alph*)}]
  3968	\item \emph{Gauge transformation
  3969	  \textup{(}Approach~A\textup{)}.}
  3970	  The $Q$-exact correction in
  3971	  $[Q, G_1] - T_{\mathrm{Sug}} = [Q, \eta_1]$
  3972	  is killed by replacing $G_1$ with
  3973	  $\widetilde G_1 = G_1 - \eta_1$:
  3974	  a gauge transformation in the dg Lie algebra controlling
  3975	  the brace deformation complex. This works at degree~$1$
  3976	  for any algebra with an explicit antighost contraction.
  3977	\item \emph{Shadow-depth truncation
  3978	  \textup{(}Approach~C\textup{)}.}
  3979	  For class~$L$, the coherence tower has only three
codex
I’m checking the Dunn step against the repo’s own constitutional distinction `SC^{ch,top} ≠ E_3`. If the proof is only combining the closed color with the open color abstractly, that is not enough; it needs an actual single-object locally constant factorization algebra on `R^3`, not just a two-colored Swiss-cheese action.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4230,4338p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4230	\index{E3 algebra@$\Ethree$ algebra!via Dunn additivity|textbf}%
  4231	\index{Dunn additivity!alternative $\Ethree$ construction|textbf}%
  4232	\index{topologization theorem!Dunn route to $\Ethree$}%
  4233	\ClaimStatusProvedHere
  4234	Let $\fg$ be a finite-dimensional simple Lie algebra and
  4235	$\cA = V_k(\fg)$ the universal affine vertex algebra at
  4236	non-critical level $k \neq -h^\vee$.  The BRST cohomology of
  4237	the derived chiral centre
  4238	$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$
  4239	carries an $\Ethree^{\mathrm{top}}$-algebra structure by a route
  4240	that does not invoke the Higher Deligne Conjecture.
  4241	
  4242	The three inputs are:
  4243	\begin{enumerate}[label=\textup{(\roman*)}]
  4244	\item \textup{(Costello--Gwilliam factorisation algebra.)}
  4245	  The $3$d holomorphic--topological Chern--Simons theory on
  4246	  $\bR_t \times \bC_z$ produces a factorisation algebra
  4247	  $\cF^{\mathrm{CS}}_k$ on $\bR \times \bC$ whose
  4248	  algebraic structure decomposes as
  4249	  $\Eone^{\mathrm{top}}$ along the $\bR$-direction and


thinking
**Considering theorem implications**

I need to refine my conclusion to reflect a conditional statement regarding the theorem that `[m,G]=∂_z` implies local constancy or relies on Dunn's application. I should also consider mentioning the theorem registry and concordance drift as moderate. There's a missing proposition from the theorem registry that affects the scope of concordance topologization, and I need to ensure the sync surfaces are adjusted if I keep or downgrade the proposition.
thinking
**Identifying commit changes**

I need to draft a commit message noting 332 insertions and 125 deletions. It seems important to pinpoint all the new propositions or proofs included in this commit. I could search using the command `git show e37cc33` and look for additions marked by `\begin{proposition}`. It feels necessary to examine these added propositions; it could clarify the changes made in the commit. Let’s get started on that search!
codex
I’m checking the commit surface now, not just the live file, to make sure I’m not missing another newly added proposition/proof from the same change. If there are multiple new `ProvedHere` blocks in that commit, they need to be audited too.
exec
/bin/zsh -lc 'git show --unified=0 e37cc33 -- chapters/theory/en_koszul_duality.tex | rg -n "''^'"\\+\\\\begin\\{(proposition|theorem|lemma|construction|remark)\\}|"'^'"\\+\\\\ClaimStatus|"'^'"\\+\\\\label\\{\"" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:^\+\begin\{(proposition|theorem|lemma|construction|remark)\}|^\+\ClaimStatus|^\+\label\{)
                                                                       ^^
error: unrecognized escape sequence

thinking
**Considering shell syntax**

I'm thinking about how to escape characters in shell commands. I might need to approach it differently if I'm using double quotes. Single quotes could be a solution, but I need to clarify how they're used compared to double quotes. This is interesting because not escaping properly can lead to issues in executing commands. I think I'll explore examples to gain a better understanding of how to apply it.
exec
/bin/zsh -lc "git show --unified=0 e37cc33 -- chapters/theory/en_koszul_duality.tex | rg -n '"'^'"\\+\\\\begin\\{(proposition|theorem|lemma|construction|remark)\\}|"'^'"\\+\\\\ClaimStatus|"'^'"\\+\\\\label\\{'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
173:+\begin{proposition}[Chain-level $\Ethree^{\mathrm{top}}$ for
175:+\label{prop:sugawara-gauge-rectification}%
179:+\ClaimStatusProvedHere
378:+\begin{remark}[Three approaches to chain-level topologization]
379:+\label{rem:three-approaches-chain-level}%



thinking
**Clarifying argument logic**

I'm noticing that this argument doesn’t quite follow logically. Just because the translation-invariance of structure constants is established, it doesn't mean that the brace compositions necessarily vanish. For example, even if m_3 is translation-invariant, it’s still possible for the term [m_3, G̃_1] to be nonzero. So, I need to rethink that connection to see where the reasoning might be going astray.
thinking
**Evaluating theorem proof**

I’m thinking Dunn’s step might be okay if we accept theorem (iii). But since theorem (iii) is marked as `ProvedHere`, I wonder if we need to verify its proof. This might go beyond what the user asked, which is just to verify Dunn’s additivity step. If we find that part (ii) of the proposition fails, that could reject the result outright. Still, I should flag Dunn’s step as unsupported by the cited theorem. Let’s assess this carefully!
thinking
**Exploring class G/L in audit**

I'm considering the user's expectations about the commit message, particularly regarding class G/L and gauge rectification. I want to search the current file for references to class L, as there's speculation about its association with gauge transformation convergence. There’s mention of class G too, but maybe it's only relevant if the user insists. The commit message mentioned a property proved for class G/L, so I’ll look for that reference, possibly around line 6677.
exec
/bin/zsh -lc "rg -n \"class~\\"'$G|class G|class~'"\\"'$L|finite depth|chain-level.*class|original-complex.*class" chapters/theory/en_koszul_duality.tex | sed -n '"'1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "rg -n -F 'class~"'$L$'"' chapters/theory/en_koszul_duality.tex && rg -n -F 'class~"'$M$'"' chapters/theory/en_koszul_duality.tex && rg -n -F 'class~"'$G$'"' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2923:nothing to truncate. For class~$L$ (affine Kac--Moody),
3190:class~$L$
3540:  class~$L$ has finite shadow depth $r_{\max} = 3$,
3794:  For $V_k(\fg)$, class~$L$ has shadow depth
3801:  class~$L$\textup{)}.
3888:class~$L$. The structure constants
3894:$m_r$ for $r \geq 3$. Affine Kac--Moody is class~$L$ with
3947:class~$L$: the explicit Sugawara antighost contraction
3951:finite shadow depth $r_{\max} = 3$ (requires class~$L$,
3979:  For class~$L$, the coherence tower has only three
2846:Fix $c$ generic and let $\cA = \mathrm{Vir}_c$ (class~$M$,
2861:establishes that for class~$M$, the associated
2893:(Proposition~\ref{prop:swiss-cheese-nonformality-by-class}, class~$M$),
2927:SC-pairs from shadow truncation exist \emph{only} for class~$M$.
3435:Proposition~\ref{prop:sugawara-gauge-rectification}; for class~$M$,
3952:which is affine Kac--Moody). For class~$M$
3998:For class~$M$, Approach~A succeeds at degree~$1$ but the
2918:The construction fails for class~$G$ (Heisenberg): all
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2908,2930p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2908	  shadow tower. The closed sector acts on the open sector
  2909	  only through the cup product and identity.
  2910	  This is the maximally deficient case.
  2911	\item As $r \to \infty$ the truncation exhausts the tower,
  2912	  and the pair converges to the full $U(\cA)$. The deficiency
  2913	  vanishes in the inverse limit.
  2914	\end{enumerate}
  2915	
  2916	\smallskip
  2917	\noindent\emph{Class dependence.}
  2918	The construction fails for class~$G$ (Heisenberg): all
  2919	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$
  2920	(Proposition~\ref{prop:sc-formal-iff-class-g}), so
  2921	$(Z_{\mathsf{SC}}(\cA), \cA)_{\leq r}
  2922	= (Z_{\mathsf{SC}}(\cA), \cA)$ for every $r \geq 2$; there is
  2923	nothing to truncate. For class~$L$ (affine Kac--Moody),
  2924	truncation at $r \geq 3$ produces no deficiency because the tower
  2925	terminates at depth~$3$. For class~$C$ ($\beta\gamma$),
  2926	truncation at $r \geq 4$ produces no deficiency. Deficient
  2927	SC-pairs from shadow truncation exist \emph{only} for class~$M$.











thinking
**Evaluating finding consistency**

I'm considering whether to include a moderate finding about the internal inconsistency between lines 3795 and 3893. It could be beneficial since it’s clear and explicit. However, if we’ve already mentioned unsupported transfer, that might suffice. Still, citing the inconsistency could strengthen the argument. I might also need to mention the exact line for AP29. If none, I’ll note no AP violation detected. In terms of formatting the final answer, I’ll layout specifics clearly.
thinking
**Considering file inclusion**

I’m thinking about whether to include file links in the final output. It seems important to keep the final result concise yet impactful. Using bullet points might help to present the information more clearly and efficiently. I want to make sure that everything is streamlined and focused on delivering high-signal content that the user can easily digest. I’ll aim for clarity, balancing conciseness with the richness of information.
thinking
**Evaluating audit findings**

I’m looking at the audit and noting that there are no hits for several specific codes. The main issues I see are proof gaps and status drift. I’m considering how to classify the severity of findings, possibly categorizing them as critical, serious, or moderate. 

I think I should list Findings 1 and 2 as critical, Finding 3 as serious, and Finding 4 as moderate, with a potential fifth finding also being moderate. It might be useful to mention the new proposition introduced in the recent commit for clarity.
thinking
**Detailing Finding 1**

For Finding 1, I see that the file spanning lines 3776 to 3785 mentions an explicit primitive and a corrected contraction. I also notice that the source construction lines 3662 to 3666 refer to a ghost-current term equating to [Q,candidate] in relation to the equations of motion. Additionally, lines 3673 to 3677 state that the ghost-self-coupling is "Q-exact by the same mechanism," but it lacks an explicit primitive. I’ll need to downgrade this to a cohomological statement or supplement it with a precise cochain computation.
thinking
**Analyzing gauge procedure details**

I’m looking at four key details regarding the gauge procedure for class M. Lines 3952-3957 and 3998-4003 claim it might not terminate and could require infinite corrections. Meanwhile, earlier lines 3420-3424 state it’s "expected to be genuinely infinite," while lines 3483-3488 suggest that MC5 provides evidence but doesn’t confirm failure. Lastly, `bv_brst.tex:1786-1788` only mentions that no cancellation identity forces coefficients to vanish, needing a rewrite as conjectural or expected, or I could prove divergence separately.
thinking
**Evaluating status and propositions**

I'm looking at the metadata status drift and noticing that the concordance notes an original complex lift being conditional on some variables, yet the theorem registry doesn’t have a property entry. If the proposition stands, I might sync it; if not, I'll consider downgrading. Since the user inquired about gauge transformation convergence, I should clarify that the current file does not prove the class G case but addresses an affine KM/class L situation. It seems there might be a gap in expectations.
thinking
**Verifying gauge transformation convergence**

The user mentioned checking gauge transformation convergence for a class G/L with finite depth. Since class G isn’t explicitly stated, I should note that as a finding in the summary. I noticed that lines 3967-3983 say that approach A works for any explicit antighost, and approach C for L, but no mention of G, which may not be necessary. I should also check if the proposition or proof involves any banned vocabulary like AP29. It seems none was detected, so I'll mention that as well.
thinking
**Reviewing propositions and labels**

I'm checking a proposition about the derived center, and it looks fine regarding AP165. I should explore `chapters/connections/bv_brst.tex`, where it references the conjecture as `Conjectureref{conj:master-bv-brst}`. It seems that’s okay since the proposition addresses obstructions to the conjecture. I also ran a search for the duplicate label prop:sugawara-gauge-rectification across volumes and found only one hit. That's good! Building a status or tests might not be necessary; logs seem fine as they are.
thinking
**Considering LaTeX Options**

I’m thinking about whether to run a targeted LaTeX build, but that might be overkill since the user only asked for audit file contents. A minimal `latexmk` might be too heavy as well. I don’t think it’s necessary to run tests, especially since showing line numbers and cross-references could just use grep. If there are no edits, a quick compile might not be needed, but I could mention any unresolved references. It's probably best to tell the user a build isn't necessary.
thinking
**Structuring Findings**

I’m drafting a potential final text for the findings section. I’ve identified a problem in the material: it asserts an explicit primitive `\eta_1` and an exact cochain-level rectification, but the source only shows that the ghost-current term is exact up to equations of motion terms. I need to decide whether to provide a strict primitive for both corrections or adjust the statement to a weaker one. 

I also want to remember to use one file link per bullet and keep bullets flat, avoiding any nesting.
thinking
**Drafting findings and checks**

I might say, “The only new proposition in the recent commit is this one.” This could demonstrate the completeness of the contract. I’m considering starting with that, but I'm not completely sure. Then, I'll aim to craft a final, concise, yet comprehensive summary, possibly using bullet points. Maybe I'll label sections like **Findings** and **Checks**. I want to ensure I keep it under 70 lines as I draft!
codex
Only new proposition/proof in the recent change is `prop:sugawara-gauge-rectification`; the review below covers it completely.

**Findings**
- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3776): part (i) claims an explicit primitive `\eta_1` and exact cochain-level rectification, but the source construction only proves the ghost-current term modulo equations of motion and treats the ghost-self-coupling term by an unexpanded “same mechanism” argument ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3662), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3673)). No strict primitive is actually constructed there. FIX: either compute strict primitives for both correction terms on the stated BRST complex and then deduce `[Q,\widetilde G_1]=T_{\mathrm{Sug}}`, or weaken part (i) back to a cohomological/conditional statement.

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3794): part (ii) collapses the brace-coherence tower from shadow depth alone, but the cited support [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1658) controls the BV/bar harmonic discrepancy, not the brace deformation complex, and the same chapter already says those are different obstruction problems ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3475)). The proposition also contradicts itself: it first says only `m_2` contributes, then later uses a nonzero `m_3` without computing `[m_3,\widetilde G_1]` ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3795), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3893)). FIX: add a theorem identifying `D^{(1)}` with the cited harmonic obstruction and compute the degree-3 term explicitly, or downgrade part (ii) to conditional/heuristic.

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3818): the Dunn step is asserted, not proved. From `[m,G]=\partial_z` the text jumps to “locally constant on cochains” and then to `E_3^{top}`, but neither this proposition nor Theorem `thm:topologization` proves the recognition lemma needed to apply HA 5.4.5.9 / 5.1.2.2 on the original complex ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3109), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3924)). FIX: insert a precise lemma showing that brace-level null-homotopy of holomorphic translation yields a locally constant factorization algebra on the original cochain complex, with commuting `E_2^{top}` and `E_1^{top}` structures on the same object; otherwise keep only Theorem `thm:topologization`(ii).

- PROBLEM at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3952): class `M` non-termination is overstated. Here and at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3998) the file says the gauge procedure does not terminate, but earlier the same file only says the infinite coherence tower is expected and that MC5 gives evidence rather than proof ([en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3420), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3486)); the cited class-`M` result only proves curvature-divisible harmonic discrepancies, not divergence of the gauge series ([bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1786)). FIX: change the class `M` language back to conjectural/expected, or add a separate proof of non-termination in the brace deformation complex.

- PROBLEM at [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7321): claim-surface sync is stale. Concordance still presents the original-complex lift as conditional on `[m,G]=\partial_z`, and `metadata/theorem_registry.md` has no `prop:sugawara-gauge-rectification` entry. FIX: if the proposition survives, update concordance and regenerate metadata; if it is downgraded, keep the current concordance scope and remove the new `ProvedHere` surface.

**Checks**
Label/status check passed syntactically: `\label{prop:sugawara-gauge-rectification}` is unique across Vols I–III, and the environment/tag pairing is `proposition` + `\ClaimStatusProvedHere`.

No direct AP126, AP132, AP165, AP113, or AP29 hit appears in the audited proposition block. The problems are proof gaps and status drift.
tokens used
165,643
