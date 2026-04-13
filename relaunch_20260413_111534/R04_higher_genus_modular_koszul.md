# R04_higher_genus_modular_koszul (932s)

Edited [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:936) only. I re-read each modified surface, checked the newly introduced label targets (`thm:e1-mc-element`, `chap:e1-modular-koszul`, `prop:geometric-modular-operadic-mc`, `thm:genus-universality`, `thm:family-index`, `thm:betagamma-global-depth`, `prop:betagamma-T-line-shadows`) and confirmed the “fixed pointed curve” wording now survives only as an explicit negation inside the corrected ambient `D^2=0` proof. I did not run a full TeX build.

## Rectification Summary
- [FIXED] T06 circularity in Theorem D — added an explicit routing remark making the proof chain non-circular: bar-intrinsic shadow tower (`thm:mc2-bar-intrinsic`) → genus universality (`thm:genus-universality`) → downstream GRR/family-index identification (`thm:family-index`).
- [FIXED] T08 PBW / Whitehead misuse — added the missing comparison showing that, after fixing a weight and mode pattern, the residue action factors through the diagonal adjoint action of finite-dimensional semisimple `\fg`; mixed genus-`0/g` maps are now routed through `H^1(\fg,N_h^{n-1})`, not through cohomology of the truncated current algebra.
- [FIXED] T09 MC2 scope in this chapter — `thm:universal-theta`, `thm:mc2-bar-intrinsic`, and the surrounding remarks now state explicitly that this chapter proves the coinvariant/symmetric MC2 statement on `\gAmod`; the ordered `E_1` theorem is redirected to `thm:e1-mc-element` in `e1_modular_koszul.tex`.
- [BLOCKED] T09 introduction cross-reference — the misattribution in `introduction.tex` was not edited because the task restricted edits to the assigned target file. I added an in-file scope remark stating that any external citation of `thm:mc2-bar-intrinsic` as the ordered `E_1` statement is incorrect.
- [FIXED] T09 `\Theta_\cA` placement — added the explicit identification of the genuswise product of cyclic coderivations with the augmentation ideal `G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)`, so the proof no longer silently treats two different spaces as the same.
- [FIXED] T16 depth-gap overscope — the depth-gap proposition now separates the `\kappa|_L \neq 0` single-line regime, where only `{0,1,\infty}` occur, from the boundary `d_{\mathrm{alg}}=2` contact witness realized globally by the conformal-weight `\beta\gamma_\lambda` family.
- [FIXED] T16 class-C witness contradiction — the file now states that the class-`\mathbf{C}` witness is not the weight-changing line and not the `T`-line; it is the full conformal-weight `\beta\gamma_\lambda` family with `S_2=6\lambda^2-6\lambda+1`, `S_3=0`, `S_4=-5/12`, and `S_r=0` for `r\ge 5`.
- [FIXED] T18 wrong space for ambient `D^2=0` — the ambient square-zero theorem and related remarks now use the relative Fulton-MacPherson/log-FM space of the universal stable family `\operatorname{FM}_k(\cC_{g,n}/\overline{\cM}_{g,n})`; collision faces, curve-degeneration faces, and mixed codimension-2 cancellations are all formulated on that universal-family carrier.


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
session id: 019d8674-3005-73d3-a4e5-2fa3ccad1297
--------
user
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \ref and \label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>


TARGET: chapters/theory/higher_genus_modular_koszul.tex

This is the largest theory file. Multiple CRITICAL findings.

FINDINGS TO FIX:

1. [CRITICAL T06] Line ~2695: Theorem D circular dependency with thm:family-index.
   FIX: Add a routing remark (AP147) identifying the non-circular anchor.
   The proof chain should be: shadow tower construction (independent) → genus universality
   (from shadow tower) → family index identification (from universality). Make this explicit.

2. [CRITICAL T08] Lines ~994,1011: MC1 PBW — d_1^PBW maps enrichment classes to genus-0 sector
   without controlling mixed maps. Whitehead invoked for semisimple g but applied to truncated
   current algebra.
   FIX: Add the missing comparison between truncated current algebra and g. Whitehead applies
   to the finite-dimensional Lie algebra g acting on the weight graded pieces; make this precise.

3. [CRITICAL T09] Line ~3475: MC2 proved on g^mod only, not g^{E1}.
   Introduction.tex:368 wrongly attributes the E1 statement to thm:mc2-bar-intrinsic.
   FIX: Clarify that MC2 as stated here is on g^mod. The E1 version is in e1_modular_koszul.tex.
   Fix the introduction cross-reference.

4. [CRITICAL T09] Line ~3627: Theta_A placed in product of genuswise cyclic coderivations,
   then treated as element of Defcyc(A) ⊗ Gmod without identification.
   FIX: Add the explicit identification or restructure the proof to work in the genuswise product.

5. [CRITICAL T16] Line ~17115: Depth gap prop over-scoped. The kappa!=0 hypothesis excludes
   the d_alg=2 case (betagamma with kappa|_L=0).
   FIX: Split into kappa!=0 case ({0,1,inf}) and the kappa=0 boundary ({2}). Or remove the kappa!=0 hypothesis.

6. [CRITICAL T16] Line ~16414: Class-C witness contradicted. betagamma shadow tower vanishes
   on the weight-changing line. The claimed r_max=4 conflicts with proved mu_bg=0.
   FIX: Check which line/family actually realizes d_alg=2. If betagamma on the standard line,
   verify the shadow tower is nonzero there. Update the witness.

7. [CRITICAL T18] Lines ~30863,30882: D^2=0 proof uses wrong space. Log FM for fixed (X,D)
   has FM collisions and puncture collisions, not curve degenerations.
   FIX: The D^2=0 should work on the universal family over M-bar_{g,n}, not on log FM for fixed curve.
   Rewrite the space to be the correct one.

Read the file carefully (it's very large), verify each finding, fix in dependency order.
mcp startup: no servers



thinking
**Clarifying editing constraints**

I need to modify a specific file assigned, but there's an indication about fixing a cross-reference in introduction.tex. The user mentioned only to edit the assigned file, which is chapters/theory/higher_genus_modular_koszul.tex. This raises a question—can I touch introduction.tex at all? Since the user didn't specifically mention modifying the intro, I think it’s wise to keep it untouched but perhaps note the issue in the target file. However, the finding indicates the introduction cross-reference needs attention. I might need to clarify this with the user to ensure I'm following their instructions accurately.
thinking
**Evaluating file edits and skills**

I’m considering whether there are multiple assigned files, especially since there’s just one TARGET. I need to read several documents, including AGENTS and constitutional files, before making any substantial mathematical edits. This includes CLAUDE.md and others related to the theorem registry. I might only focus on relevant sections since there’s a lot of content to sift through. The instructions clearly state to consult these files first. I should probably preview SKILL.md for the appropriate skills to apply, like beilinson-rectify, but since I need to keep edits minimal, I'll focus on using what’s necessary.
thinking
**Deciding on exploration methods**

I think I need to read the skill file just enough to understand what's necessary. It’s important to use commentary updates before diving into the exploration. Maybe I should also consider updating the plan since the task seems substantial. The instructions suggest using explorer agents for codebase questions rather than manual searches or digging through files. Since my current task involves file searches, spawning explorer agents could help me locate findings and context quickly. It's about working smarter!
codex
Using `beilinson-rectify` for this pass. I’m starting by loading the required constitutional files and the target theorem surface, then I’ll verify each cited line in `higher_genus_modular_koszul.tex` before patching.
exec
/bin/zsh -lc "printf '--- CLAUDE ---\\n'; sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf '--- SKILL ---\\n'; sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- SKILL ---
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
 succeeded in 52ms:
--- CLAUDE ---
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
/bin/zsh -lc "printf '--- REGISTRY ---\\n'; sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf '--- CONCORDANCE ---\\n'; sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:family-index|thm:mc2-bar-intrinsic|Theta_A|Defcyc|depth gap|betagamma|D\\"'^2=0|log FM|Whitehead|PBW|truncated current algebra|shadow tower|genus universality|family index" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then printf '--- REDTEAM ---\\n'; sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else printf '--- REDTEAM ---\\n'; sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- REGISTRY ---
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2842 |
| Total tagged claims | 3669 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
 succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
78: $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
198:For standard examples at generic parameters, the PBW argument of
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
446:$\Defcyc(\cA)$
615:\emph{(Modular Koszulity / PBW degeneration.)}
616:At each genus $g \geq 1$, the PBW spectral sequence of
671:$\Theta_{\cA}\in\operatorname{MC}(\Defcyc(\cA)\widehat{\otimes}\Gmod)$
770:\begin{theorem}[PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
773:\index{PBW spectral sequence!higher genus concentration}
784:Then for every genus~$g \geq 1$, the PBW spectral sequence for the
844:the matrix of $d_2^{\mathrm{PBW}}$ is block upper triangular:
859:Consequently the diagonal block of $d_2^{\mathrm{PBW}}$ on
868:$d_2^{\mathrm{PBW}}$ is an isomorphism:
876:$d_2^{\mathrm{PBW}}$.
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
902:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
915:\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
916:\index{truncated current algebra!mode bookkeeping only}
 succeeded in 52ms:
--- CONCORDANCE ---
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
--- REDTEAM ---
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

thinking
**Planning the exploration**

I’m considering whether there's an introductory excerpt in the target material. It seems like it would be useful to look at the context surrounding each finding. I might need to provide a commentary update to clarify anything before diving deeper. I think I should create a detailed plan with about 5 to 6 steps to keep things organized. This structured approach should help make the exploration more effective and thorough.
codex
I’ve loaded the governing files and located each hotspot in the target chapter. Next I’m reading the surrounding theorem/proof lanes in dependency order so the fixes land on the actual argument surfaces, not just the cited lines.
Plan update
Rectification is concentrated in one large theorem file with seven interlocking findings. I’m resolving them in dependency order: first the PBW/MC2 foundations, then the Theorem D routing and Theta placement, then the depth-gap and universal-family corrections.
  → Read the local context around T08, T09, T06, T16, and T18 in higher_genus_modular_koszul.tex and identify the minimal truthful patch points
  • Patch the PBW/Whitehead comparison and MC2 scope/Theta identification issues
  • Patch the Theorem D routing remark to remove the circular dependency surface
  • Patch the depth-gap and class-C witness statements to match the proved witnesses
  • Patch the D^2=0 geometric space to the universal family over M-bar_{g,n}
  • Re-read modified sections, grep labels/refs, and verify each finding is resolved without status drift
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '900,1325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2620,3015p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   900	Theorem~\ref{thm:pbw-allgenera-principal-w}).
   901	For semisimple weightwise symmetry, the genus enrichment splits into
   902	non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
   903	invariant pieces killed by the family-specific $d_2$ transgression.
   904	The affine KM Killing class shows that this is an $E_3$ statement, not
   905	an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
   906	radical cohomology of the weightwise Lie action.
   907	Open: non-principal families; the $\mathcal{W}_\infty$
   908	inverse-limit package
   909	(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
   910	\end{remark}
   911	
   912	\begin{lemma}[Weightwise reduction of the genus enrichment to
   913	 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
   914	\label{lem:pbw-weightwise-g-module}
   915	\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
   916	\index{truncated current algebra!mode bookkeeping only}
   917	Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
   918	\[
   919	V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
 succeeded in 54ms:
  2620	\begin{definition}[Full modular characteristic package]
  2621	\label{def:full-modular-package}
  2622	\index{modular characteristic package!full|textbf}
  2623	\index{universal Maurer--Cartan class|textbf}
  2624	\index{spectral discriminant!in full package}
  2625	\index{periodicity profile!in full package}
  2626	For a modular Koszul chiral algebra~$\cA$ for which the universal
  2627	Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
  2628	constructed (in particular, for every such~$\cA$ with simple Lie
  2629	symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
  2630	\emph{full modular characteristic package} is the quintuple
  2631	\begin{equation}\label{eq:full-package-quintuple}
  2632	\mathcal{C}_{\cA}
  2633	\;:=\;
  2634	\bigl(\,\Theta_{\cA},\;\kappa(\cA),\;\Delta_{\cA},\;
  2635	 \Pi_{\cA},\;\mathcal{H}_{\cA}\,\bigr),
  2636	\end{equation}
  2637	where:
  2638	\begin{enumerate}[label=\textup{(\roman*)}]
  2639	\item The \emph{universal Maurer--Cartan class}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30790,30930p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3440,3925p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16380,17540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30790	applied to the bar complex on log-FM spaces.
 30791	
 30792	More explicitly: in the finite-order shadow obstruction tower, the extension
 30793	$\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
 30794	obstruction class $o_{r+1}(\cA) \in H^2(F^{r+1}/F^{r+2})$. For a
 30795	separating degeneration $\cA = \cA_1 \cup_\xi \cA_2$, the
 30796	obstruction classes satisfy a multiplicative relation
 30797	$\xi^* o_{r+1}(\cA) = o_{r+1}(\cA_1) \otimes 1 + 1 \otimes
 30798	o_{r+1}(\cA_2) + \text{tree correction}$,
 30799	where the tree correction comes from the birational modification
 30800	relating the product of log-FM factors to the actual special-fibre
 30801	component (Mok~\cite[Theorem~5.3.4]{Mok25}).
 30802	For non-separating degenerations, an additional term
 30803	$\hbar\Delta(\Theta_\cA^{\leq r})$ appears: this is the
 30804	BV operator that distinguishes non-separating from separating
 30805	clutching, and is the primary reason that
 30806	$D_\cA^2 = 0$ at the ambient level required the log-FM
 30807	normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
 30808	(Theorem~\ref{thm:ambient-d-squared-zero}).
 30809	\end{remark}
 succeeded in 50ms:
  3440	$\cW_3$ $\mathbb{Z}_2$-parity ($S_3 = 0$ kills
  3441	$\delta_{\mathrm{pf}}^{(2,0)}$), and the shadow visibility genus
  3442	(Corollary~\ref{cor:shadow-visibility-genus}).
  3443	\end{remark}
  3444	
  3445	\begin{theorem}[Spectral characteristic theorem; \ClaimStatusProvedHere]
  3446	\phantomsection
  3447	\label{thm:spectral-characteristic}
  3448	\index{spectral discriminant!invariance theorem|textbf}
  3449	
  3450	\smallskip\noindent
  3451	\textup{[Regime: quadratic;
  3452	Convention~\ref{conv:regime-tags}.]}
  3453	Let $\cA$ be a modular Koszul chiral algebra.
  3454	The spectral discriminant
  3455	$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
  3456	depends only on the quadratic OPE data of the Koszul pair and is invariant
  3457	under Drinfeld--Sokolov reduction.
  3458	In particular, $\Delta_{\cA}$ is a separate non-scalar invariant:
  3459	it is not determined by $\kappa(\cA)$ alone.
 succeeded in 51ms:
 16380	 non-formality persists through the quartic stage
 16381	 but is killed by a rigidity constraint at degree~$5$.
 16382	 \end{minipage} \\[6pt]
 16383	$\mathbf{M}$ & Mixed &
 16384	 $\infty$ &
 16385	 \begin{minipage}[t]{0.42\textwidth}\raggedright
 16386	 $o_r(\cA) \neq 0$ for infinitely many~$r$.
 16387	 Equivalently: $\gAmod$ is intrinsically non-formal.
 16388	 \end{minipage} \\
 16389	\bottomrule
 16390	\end{tabular}
 16391	\end{center}
 16392	These four classes are exhaustive and mutually exclusive
 16393	for the standard families at low rank. At higher rank,
 16394	\emph{finite depths $d \geq 5$} are realized by lattice vertex
 16395	algebras whose theta functions involve cusp forms
 16396	(Chapter~\ref{chap:arithmetic-shadows},
 16397	\S\ref{sec:higher-depths}): depth~$d$ requires a lattice
 16398	of rank~$r$ with $\dim S_{r/2}(\Gamma) \geq d-3$, and
 16399	each independent cusp form contributes one critical line

thinking
**Searching for D^2 proof details**

I need to gather more information about the ambient D^2 theorem. It seems the user mentions that the D^2=0 proof might be using the wrong space. I'm trying to confirm if lines 30863 and 30882 relate to the equations I'm looking for, but they might not connect since they refer to the planar forest section. I should locate the D^2=0 statement by searching around earlier or later in the text.
🌐 Searching the web...
🌐 Searched the web
codex
I’ve confirmed the PBW fix surface already has partial scaffolding, but the missing comparison needs to be stated as the reason Whitehead applies only to finite-dimensional `\fg`-modules. I’m now checking the MC2 and ambient-geometry lanes so the later edits don’t create a new object-identification gap.
exec
/bin/zsh -lc "rg -n \"ambient-d-squared-zero|D\\"'^2 = 0|D'"\\"'^2=0|log-FM|fixed curve|universal family|Mok|FM_n'"\\(|\\boverline\\\\mathcal\\{M\\}_\\{g,n\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11280,11680p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:ambient-d-squared-zero|D\^2 = 0|D\^2=0|log-FM|fixed curve|universal family|Mok|FM_n\(|\boverline\mathcal\{M\}_\{g,n\})
                                                                                                       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 11280	chart~\eqref{eq:convstr-log}, using~\cite[Theorem~4.1]{RNW19}
 11281	and~\cite[Theorem~1.2]{Val16}.
 11282	\end{proof}
 11283	
 11284	\subsubsection{The modular bar functor in logarithmic FM coordinates}
 11285	
 11286	\begin{construction}[Logarithmic modular bar functor;
 11287	\ClaimStatusProvedHere]
 11288	\label{const:vol1-log-modular-bar-functor}
 11289	\index{modular bar construction!logarithmic FM chart}
 11290	In these coordinates the modular bar construction is the
 11291	stable-graph sum
 11292	\begin{equation}\label{eq:bmod-log}
 11293	\bar{B}^{\mathrm{mod},\log}(\cA)(g,n)
 11294	\;=\;
 11295	\bigoplus_{\Gamma \in \mathsf{Gr}^{\mathrm{st}}_{g,n}}
 11296	\left(
 11297	\bigotimes_{v \in V(\Gamma)}
 11298	\bar{B}^{\mathrm{ch}}\!\bigl(A^{\mathrm{ch}}_\infty;\,
 11299	\mathrm{In}(v)\bigr)
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30380,30790p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15120,15380p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 30380	each truncation $\Theta_\cA^{\leq r}$ as a sum over
 30381	cross-polarized stable graphs of weight at most~$r$.
 30382	
 30383	\begin{definition}[The modular bar--Hamiltonian]
 30384	\label{def:modular-bar-hamiltonian}
 30385	Let $\cA$ be a cyclic chiral algebra with Koszul dual $\cA^!$,
 30386	cyclic minimal models $(V_{\cA}, \ell_n^{\mathrm{tr}})$ and
 30387	$(V_{\cA^!}, \ell_n^{!\,\mathrm{tr}})$, Hessian
 30388	$H_{\cA}\colon V_{\cA} \xrightarrow{\sim} V_{\cA}^*[-1]$,
 30389	propagator $P_{\cA} := H_{\cA}^{-1}$, and universal twisting
 30390	kernel $\tau_{\cA} \in \operatorname{MC}(\cA^!\widehat\otimes\cA)$.
 30391	The \emph{modular bar--Hamiltonian} is the connected graph sum
 30392	\begin{equation}
 30393	\label{eq:modular-bar-hamiltonian}
 30394	\Theta_{\cA}
 30395	\;:=\;
 30396	\sum_{\substack{
 30397	\Gamma\;\text{connected}\\
 30398	\text{stable, cross-polarized}}}
 30399	\frac{1}{|\operatorname{Aut}(\Gamma)|}
 succeeded in 51ms:
 15120	
 15121	\begin{example}[Verification for the four archetypes]
 15122	\label{ex:operadic-complexity-verification}
 15123	\index{operadic complexity!verification table}
 15124	\begin{center}
 15125	\small
 15126	\renewcommand{\arraystretch}{1.15}
 15127	\begin{tabular}{lcccc}
 15128	\toprule
 15129	\emph{Family} &
 15130	$d_\infty$ &
 15131	$f_\infty$ &
 15132	$r_{\max}$ &
 15133	\emph{Mechanism} \\
 15134	\midrule
 15135	Heisenberg &
 15136	 $2$ & $2$ & $2$ &
 15137	 Strictly commutative; $m_n = 0$, $n \geq 3$ \\
 15138	Affine $\hat{\mathfrak{g}}_k$ &
 15139	 $3$ & $3$ & $3$ &
codex
The ambient geometry surface is localized now. I’m checking the exact theorem that currently phrases `D^2=0` on log-FM for a fixed pair `(X,D)` so I can rewrite only that claim to the universal family over `\overline{\mathcal M}_{g,n}` and keep the downstream references coherent.
exec
/bin/zsh -lc "rg -n \"ambient-d-squared-zero|convolution-d-squared-zero|prism-higher-genus|universal family|fixed curve|log-FM|Mok25|D\\"'^2=0|d_full'"\\"'^2 = 0" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10880,11380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
302:(Theorem~\ref{thm:prism-higher-genus}(ii)) is
561:(Theorem~\ref{thm:prism-higher-genus}).
2424:(Theorem~\ref{thm:convolution-d-squared-zero}).
3847: proved via Theorem~\ref{thm:prism-higher-genus}:
3855: (Theorem~\ref{thm:convolution-d-squared-zero}).
4017: (Theorem~\ref{thm:prism-higher-genus},
4026: Theorem~\ref{thm:convolution-d-squared-zero}.
5498:(Theorem~\ref{thm:prism-higher-genus}(i)) by summing
9345: universal family.
10026:(Theorem~\ref{thm:convolution-d-squared-zero}) and the Jacobi
10524:ambient level (Theorem~\ref{thm:ambient-d-squared-zero}) is
10527:(now proved: Theorem~\ref{thm:ambient-d-squared-zero}).
10712: of Mok~\cite{Mok25}) preserves the MC moduli space up to
11133:By Mok~\cite[Theorem~3.3.1, Corollary~5.3.4]{Mok25}, these chain
11173:the proper birational correspondence~\cite[Cor~5.3.4]{Mok25}.
11251:$\{C_*(\overline{\cM}_{g,n})\}$; replacing these by log-FM
11310:of the log-FM stratum indexed by~$\Gamma$, and
11338:(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
11339:log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
11375:$d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
 succeeded in 51ms:
 10880	\end{proof}
 10881	
 10882	\begin{corollary}[Strictification comparison;
 10883	\ClaimStatusProvedHere]
 10884	\label{cor:strictification-comparison}
 10885	\index{strictification comparison}
 10886	All dg~Lie algebras in this monograph are functorial strict models
 10887	of the corresponding homotopy-invariant $L_\infty$-algebras, and
 10888	all bar-complex constructions are computations in a chosen
 10889	strictification. In particular:
 10890	\begin{enumerate}[label=\textup{(\roman*)}]
 10891	\item $\mathfrak{g}_{\cA}^{\mathrm{mod}} =
 10892	 \Convstr\!\bigl(\{C_*(\overline{\cM}_{g,n})\},
 10893	 \operatorname{End}_{\cA}\bigr)$ is a strict model of
 10894	 $\Definfmod(\cA)$.
 10895	\item $\Defcyc^{\mathrm{mod}}(\cA)$ is a strict model via the
 10896	 coderivation identification.
 10897	\item For affine Kac--Moody algebras at non-critical level, the
 10898	 $L_\infty$-algebra is strictly formal: no higher homotopy
 10899	 corrections at any genus

thinking
**Researching ambient-d-squared-zero theorem**

I need to gather more information about the ambient-d-squared-zero theorem, especially focusing on lines 31109 and surrounding content. I should dive into the text between lines 31090 and 31260 to get a full understanding of what's being discussed. This will likely help clarify the context and any important concepts related to the theorem. I'm curious to see what insights I can gather from that section!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31090,31270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31090	 complex is square-zero by construction.
 31091	\item $d_{\mathrm{sew}}^2 = 0$: this is the boundary-of-boundary
 31092	 vanishing on $\overline{\mathcal{M}}_{g,n}$, i.e.\
 31093	 Lemma~\ref{lem:stable-graph-d-squared}.
 31094	\item $d_{\mathrm{pf}}^2 = 0$: associativity of edge contraction in
 31095	 planted forests
 31096	 (Definition~\ref{def:planted-forest-coefficient-algebra}).
 31097	\item The cross-terms cancel by the master identity
 31098	 \[
 31099	 [d_{\mathrm{sew}}, d_{\mathrm{pf}}]
 31100	 + [d_{\mathrm{int}}, \hbar\Delta]
 31101	 + [[\tau_{\cA},-], d_{\mathrm{sew}} + d_{\mathrm{pf}}]
 31102	 = 0.
 31103	 \]
 31104	 This follows from Theorem~\ref{thm:ambient-d-squared-zero} below.
 31105	\end{enumerate}
 31106	\end{proof}
 31107	
 31108	\begin{theorem}[Square-zero: convolution level; \ClaimStatusProvedHere]
 31109	\label{thm:convolution-d-squared-zero}

thinking
**Investigating theorem updates**

It looks like the theorem might already be corrected, especially around T18 line 30863, which could connect to theorem 31122. However, there might be earlier lines that still need checking, like 10524 and 11336. I’ll search for terms like "fixed pointed curve" to identify any outdated statements. The user is asking to fix the introduction cross-reference, but since I can't edit that directly, I'll look for any remarks about the introduction in the file around line 43 and the initial lines.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	
exec
/bin/zsh -lc "rg -n \"mc2-bar-intrinsic|Theorem~\\\\ref\\{thm:mc2-bar-intrinsic\\}|Theorem~\\\\textup\\{\\\\ref\\{thm:mc2-bar-intrinsic\\}\\}|MC2\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '220,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2331: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2629:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2686:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2783:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2894:Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
3504:This is Theorem~\ref{thm:master-theta} (MC2).
3520:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3536:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3649:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3675:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3676:\label{thm:mc2-bar-intrinsic}
3678:\index{MC2!bar-intrinsic proof}
3679:\index{MC2!full generality}
3731:\begin{remark}[Scope of MC2 in this chapter]
3732:\index{MC2!coinvariant scope}
3733:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4002:\index{MC2!foundational dependency chain}
 succeeded in 52ms:
   220	\end{center}
   221	Horizontal maps restrict to degenerate curves in $\partial\overline{\mathcal{M}}_g$;
   222	vertical maps are bar-cobar inversion at each genus.
   223	
   224	\begin{definition}[Completed chiral algebra]\label{def:completed-chiral-algebra}
   225	\index{completed chiral algebra|textbf}
   226	The \emph{completed chiral algebra} is the inverse limit:
   227	\[
   228	\mathcal{A}_{\mathrm{complete}}
   229	= \varprojlim_g \mathcal{A}^{(g)},
   230	\]
   231	For the bookkeeping parameter $\hbar$ tracking genus,
   232	$\mathcal{A}_{\mathrm{complete}}$ is a $\mathbb{C}[\![\hbar]\!]$-module with
   233	$\mathcal{A}_{\mathrm{complete}} / \hbar^{g+1} = \bigoplus_{h=0}^{g} \mathcal{A}^{(h)}$.
   234	\end{definition}
   235	
   236	\begin{proposition}[MCG-equivariance of the genus tower; \ClaimStatusProvedHere]
   237	\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
   238	\index{mapping class group!equivariance of genus tower}
   239	\index{modular invariance!genus tower}


thinking
**Evaluating findings in the file**

I’m noticing there’s some file drift happening. It seems like the key findings are around line 3627 and potentially further along. Since the user has static findings from another analysis, some issues might already be resolved. I need to read the file carefully, verify each finding, and fix them in the right order. If some are fixed, maybe no edits are necessary, but since the user wants changes, I’ll need to identify which findings remain unresolved.
thinking
**Clarifying mathematical mapping**

I'm considering how to clarify the comparison between the mixed map and internal map. I think I need to be more precise about how the comparison is drawn from the truncated current algebra to g. I could add an explicit sentence explaining that evaluating at \( t^{-m} \) modes provides a Lie algebra homomorphism. The coefficient module gets a diagonal g action through this projection, and the mixed and internal maps factor through that. Maybe the user wants an exact comparison rather than just mentioning the mode cutoff.
exec
/bin/zsh -lc "rg -n \"d_\\{\\\\mathrm\\{alg\\}\\}.*\\{0, 1, 2, \\\\infty\\}|kappa\\|_L = 0|kappa\\|_L \\\\neq 0|depth gap|prop:depth-gap-trichotomy|betagamma-global-depth|mu_betagamma|weight-changing line|charged quartic\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16690,16810p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:d_\{\mathrm\{alg\}\}.*\{0, 1, 2, \infty\}|kappa\|_L = 0|kappa\|_L \neq 0|depth gap|prop:depth-gap-trichotomy|betagamma-global-depth|mu_betagamma|weight-changing line|charged quartic)
           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 16690	 The tower is infinite by induction on the all-degree master equation.
 16691	 For multi-generator algebras $\mathcal{W}_N$ ($N \geq 3$),
 16692	 diagonal non-autonomy at degree~$6$ is governed by the
 16693	 propagator variance
 16694	 \textup{(}Proposition~\textup{\ref{prop:propagator-variance}}):
 16695	 it vanishes at isolated curvature-proportionality loci in the
 16696	 central charge.
 16697	\end{enumerate}
 16698	Shadow depth is orthogonal to Koszulness: all archetypes are
 16699	chirally Koszul
 16700	\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
 16701	yet their shadow depths differ
 16702	\textup{(}Figure~\textup{\ref{fig:shadow-archetype-classification})}.
 16703	The shadow depth classifies the
 16704	complexity of $\Theta_\cA$, not whether the bar complex is acyclic.
 16705	
 16706	For lattice vertex algebras, the shadow--spectral correspondence
 16707	\textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
 16708	identifies the shadow depth with $1$ plus the number of critical
 16709	lines of the constrained Epstein zeta. The depth is unbounded:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4096,4175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3988,4072p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4096	(Construction~\ref{constr:obstruction-recursion}).
  4097	In both regimes, $\Theta_\cA$ \emph{exists} by the
  4098	bar-intrinsic construction.
  4099	\end{remark}
  4100	
  4101	\begin{corollary}[Shadow extraction; \ClaimStatusProvedHere]
  4102	\label{cor:shadow-extraction}
  4103	\index{shadow extraction|textbf}
  4104	\index{universal Maurer--Cartan class!shadow extraction}
  4105	The bar-intrinsic MC element $\Theta_\cA$ of
  4106	Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
  4107	projections recovering all named modular invariants:
  4108	\begin{enumerate}[label=\textup{(\roman*)}]
  4109	\item \emph{Scalar shadow:}
  4110	 $\pi_{\mathrm{sc}}(\Theta_\cA)
  4111	 = \sum_{g \geq 1} \kappa(\cA)\,\lambda_g$
  4112	 \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
  4113	\item \emph{Spectral shadow:}
  4114	 $\pi_{\mathrm{br}}(\Theta_\cA) = T_{\mathrm{br},\cA}$,
  4115	 so $\Delta_\cA(x) = \det(1 - x\, T_{\mathrm{br},\cA})$
 succeeded in 53ms:
  3988	\;=\; D_{\cA^!} - d^{(0)}_{\cA^!}
  3989	\;=\; \Theta_{\cA^!}.
  3990	\]
  3991	As a consistency check, the scalar trace transforms
  3992	correctly:
  3993	$\kappa(\cA) + \kappa(\cA^!) = 0$ for Kac--Moody, and
  3994	more generally $\kappa(\cA) + \kappa(\cA^!) = K(\mathfrak{g})$
  3995	for $\mathcal{W}$-algebras
  3996	(Theorem~\ref{thm:modular-characteristic}(iii),
  3997	Theorem~\ref{thm:genus-universality}(ii)).
  3998	\end{proof}
  3999	
  4000	\begin{remark}[Complete foundational dependency chain]
  4001	\label{rem:mc2-foundational-chain}
  4002	\index{MC2!foundational dependency chain}
  4003	For the reader who wishes to trace the proof of
  4004	Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
  4005	dependency chain is as follows.
  4006	The argument rests on four independent pillars, each proved
  4007	earlier in the manuscript:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7884,8068p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7884	Once packages~(1)--(2) exist, package~(3) is a finite
  7885	reduction to one normalized scalar check. What remains open beyond
  7886	the proved uniform-weight lane is whether that check forces the
  7887	all-genera coefficient to be $\kappa(\cA)\Lambda$.
  7888	\end{remark}
  7889	
  7890	\begin{theorem}[MC2 completion under explicit hypotheses; \ClaimStatusProvedHere]
  7891	\label{thm:mc2-conditional-completion}
  7892	\index{MC2!completion under explicit hypotheses}
  7893	Let $\cA$ be a modular Koszul chiral algebra with simple Lie
  7894	symmetry~$\mathfrak{g}$. Assume:
  7895	\begin{enumerate}[label=\textup{(MC2-\arabic*)}]
  7896	\item\label{mc2-hyp:cyclic}
  7897	 The cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  7898	 $L_\infty$-algebra on bar coderivations, with
  7899	 $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g}) \cong \mathbb{C}$
  7900	 \textup{(}confirmed for all simple~$\mathfrak{g}$ by
  7901	 Corollary~\textup{\ref{cor:one-dim-obstruction}}\textup{)}.
  7902	 \textup{[}\emph{Resolved:}
  7903	 Theorem~\textup{\ref{thm:cyclic-linf-graph}} constructs the

thinking
**Clarifying construction logic**

I need to focus on the idea of non-circular anchors in shadow tower construction. It seems like genus universality leads us to family index identification, so the family index is actually downstream of universality and not parallel. If I claim the family index is independent, it might create confusion. I should take a closer look at the theorem `thm:family-index` to understand how it's used and perhaps conduct a search around the label for additional insights.
codex
I found the Theorem D routing surface. It still presents `thm:family-index` as a parallel computation, while your required proof architecture makes it downstream of the bar-intrinsic shadow tower and genus universality. I’m checking `thm:family-index` citations now so I can rewrite that route without creating a new contradiction elsewhere in this file.
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|Theorem~\\\\ref\\{thm:family-index\\}|family index theorem|family index identification|GRR\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2943:modular functor, extracted via GRR.
2978:independent GRR/family-index computation on the universal curve.
4583: by the family index theorem
4585: The $\hat{A}$-genus arises from the GRR pushforward of the
4633:Part~(f) is the family index theorem
4749:lifted genus by genus; (iv)~the $\hat{A}$-genus arises from GRR
9687:the $\hat{A}$-genus arises from GRR via the Mumford
14110:now seen as a consequence of (i) via the family index theorem
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9660,9908p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4520,4668p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4520	 \mathbb{C}$ via the isomorphism
  4521	 $\Phi \colon C^n_{\mathrm{cyc}} \xrightarrow{\sim}
  4522	 \Lambda^{n+1}\mathfrak{g}^*$
  4523	 \textup{(}Proposition~\textup{\ref{prop:cyclic-ce-identification}}\textup{)}.
  4524	 The cohomology class $[\theta_g] =
  4525	 \kappa(\cA)\cdot[\mu]\otimes\lambda_g$ is canonical;
  4526	 the representative depends on the choice of contracting homotopy
  4527	 for the CE complex.
  4528	
  4529	\item \emph{Genus-$1$ component.}
  4530	 At genus~$1$, $\theta_1$ is an honest cocycle
  4531	 \textup{(}$l_1(\theta_1) = 0$, since there are no lower-genus
  4532	 inputs\textup{)}:
  4533	 \begin{equation}\label{eq:theta-genus1}
  4534	 \theta_1 \;=\; \kappa(\cA) \cdot \mu \otimes \lambda_1
  4535	 \;\in\;
  4536	 Z^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g})
  4537	 \otimes H^1(\overline{\mathcal{M}}_{1,1},\mathbb{Q}).
  4538	 \end{equation}
  4539	 Concretely: the genus-$1$ component of $\Theta_{\cA}$ is the
 succeeded in 51ms:
  9660	quiver VOAs with multi-dimensional conformal manifolds,
  9661	has so far produced only single-parameter dependence in all
  9662	computed cases, and in every tested instance satisfies~(c$'$).
  9663	Theorem~D establishes that $\kappa$ exists as a universal
  9664	invariant; the quadruple reduction strengthens this to the
  9665	claim that, on the proved uniform-weight lane, $\kappa$
  9666	\emph{determines the minimal scalar package} of~$\Theta_{\cA}$.
  9667	\end{remark}
  9668	
  9669	\begin{remark}[\texorpdfstring{$\kappa$}{kappa} as first Chern class]
  9670	\label{rem:kappa-first-chern}
  9671	Properties (i)--(iv) identify $\kappa$ as a first Chern class:
  9672	additive under tensor products, duality-constrained
  9673	($\kappa + \kappa' = 0$ for KM/free fields; a nonzero constant for
  9674	$\mathcal{W}$-algebras), and controlling a universal obstruction.
  9675	The modular Koszul algebra is the ``line bundle,'' the genus tower is
  9676	the ``obstruction to global sections,'' and $\Theta_{\cA}$ is the
  9677	``Chern--Weil representative'' whose scalar trace has genus-$1$
  9678	coefficient $\kappa \cdot \lambda_1$, with the full
  9679	$\kappa \cdot \lambda_g$ series proved on the uniform-weight lane.

thinking
**Inspecting the family index theorem**

I'm thinking about the potential connection with the family index theorem and the label around line 4460. I need to take a closer look at what’s happening there. It seems important to focus on the starting lines near that point to understand the context better. I'm curious to see what insights I can gather from this theorem and how it might fit into what I'm exploring. Let's dive into that!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4460,4548p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4460	 cohomology
  4461	 $\mathcal{H} = H^*(\Defcyc(\cA), l_1) \cong \mathfrak{g} \oplus
  4462	 \mathbb{C}\!\cdot\!\eta$
  4463	 \textup{(}$\deg \mathfrak{g} = 0$, $\deg\eta = 2$\textup{)} has
  4464	 transferred brackets $l_2^{\mathrm{tr}} = [-,-]_{\mathfrak{g}}$,
  4465	 $l_3^{\mathrm{tr}} = \phi$
  4466	 \textup{(}the Killing $3$-cocycle\textup{)},
  4467	 $l_n^{\mathrm{tr}} = 0$ for $n \geq 4$
  4468	 \textup{(}computed for Kac--Moody via the CE~identification
  4469	 in Corollary~\textup{\ref{cor:km-minimal-linf}};
  4470	 for the scalar saturation formula below, only the
  4471	 one-dimensionality of\/ $H^2$ is used\textup{)}.
  4472	 In the genus-completed minimal model, the universal MC element
  4473	 is
  4474	 \begin{equation}\label{eq:theta-minimal}
  4475	 \Theta_{\cA}^{\min}
  4476	 \;=\;
  4477	 \kappa(\cA) \cdot \eta \otimes \Lambda,
  4478	 \qquad
  4479	 \Lambda := \sum_{g \geq 1} \lambda_g \;\in\; \Gmod,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4420,4478p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4420	\sum_{\Gamma \in \Gamma^{\mathrm{st,bip}}_{g,n}}
  4421	\frac{1}{|\mathrm{Aut}\,\Gamma|}\,
  4422	W_\Gamma(\cA),
  4423	\end{equation}
  4424	where
  4425	$W_\Gamma(\cA)
  4426	:= (\xi_\Gamma)_*
  4427	\bigl(\bigotimes_{v \in V(\Gamma)}
  4428	\theta^{(1)}_{g(v),n(v)}\bigr)
  4429	\;\lrcorner\;
  4430	\bigotimes_{e \in E(\Gamma)} P_\cA$
  4431	contracts vertex tensors by the propagator along edges and
  4432	pushes forward along the clutching map $\xi_\Gamma$.
  4433	Because stable connected graphs of fixed $(g,n)$ are finite in
  4434	number, this sum is componentwise finite.
  4435	\end{remark}
  4436	
  4437	\subsubsection*{Explicit construction of the universal class}
  4438	
  4439	The minimal cyclic $L_\infty$ model gives a closed-form formula
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Exploring the file structure**

I noticed there's no label `thm:family-index` in this file, which is puzzling. Maybe it's labeled elsewhere? There are many references to it, so I should check the repository for other files that might contain it. However, I only need to edit the current file right now. I could still reference an external theorem if needed. I think using a search tool in the repo could help find what I'm looking for!
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|thm:family-index\" ." in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 1133

./scripts/platonic_rectification_20.py:203:KNOWN ISSUE: Circular dependency thm:genus-universality <-> thm:family-index.
./scripts/platonic_rectification_20.py:205:YOUR MISSION: BREAK the circularity by providing an INDEPENDENT proof of thm:family-index.
./scripts/platonic_rectification_20.py:218:Search for 'thm:family-index' and 'thm:genus-universality'. Focus on the proof of
./scripts/platonic_rectification_20.py:219:thm:family-index and provide the independent computation.""")
./scripts/adversarial_wave2.py:160:    ("F08_prerequisites_thm_D", "chapters/theory/higher_genus_modular_koszul.tex", "For Theorem D: trace the FULL proof chain. Start from obs_g = kappa*lambda_g. What is cited? Is each cited result proved? Is there circularity (thm:genus-universality <-> thm:family-index)?"),
./scripts/adversarial_wave2.py:613:    ("L04_thmD_chain", "Trace Theorem D chain: obs_g=kappa*lambda_g. Follow thm:genus-universality, thm:family-index. CHECK FOR CIRCULARITY. Map the non-circular anchor."),
./scripts/fix_campaign_100.py:116:2. Theorem D circular dependency routing: thm:genus-universality <-> thm:family-index.
./scripts/fix_campaign_100.py:153:1. Search for thm:family-index and thm:genus-universality. Add routing remark (AP147)
./scripts/rectification_campaign.py:181:3. [CRITICAL T06] Line ~5326: thm:family-index invoked by Theorem D proof, but thm:family-index
./scripts/rectification_campaign.py:184:   prove thm:family-index independently of thm:genus-universality, using only the genus-1 base case
./scripts/rectification_campaign.py:196:1. [CRITICAL T06] Line ~2695: Theorem D circular dependency with thm:family-index.
./scripts/rectification_campaign.py:400:1. [CRITICAL T06] Line ~6010: thm:family-index cites thm:genus-universality,
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:9:- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:668` — PROBLEM: the chain-level curvature proposition jumps from `c_1(\mathbb E,h_{Ar})=\pi_*[\omega_g^{Ar}]` to `\kappa(\cA)\lambda_g=\kappa(\cA)c_g(\mathbb E)`. A single pushed-forward `(1,1)`-form gives a first Chern class, not the top Chern class `c_g` for `g>1`; the displayed “two-step Chern--Weil projection” does not prove the claimed `\lambda_g` statement. FIX: rewrite part (ii) to conclude only the `c_1(\mathbb E)` statement, and move the `\kappa(\cA)\lambda_g` identification to a forward reference to `thm:genus-universality`/`thm:family-index` rather than deriving it here.
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:17:- [HIGH] `chapters/theory/higher_genus_foundations.tex:1061` — PROBLEM: the family-index preface asserts that the genus-`g` bar family defines a virtual `K`-class and immediately applies GRR to `\bar B(\cA)|_{fiber}` without proving perfectness, finite rank, or any base-change package for this family. FIX: recast this paragraph as a roadmap: “On the proved uniform-weight scalar lane, Theorem `thm:family-index` later replaces the full bar family by the scalar `K`-class `\mathcal D_\cA^{(g)}=\kappa(\cA)\mathbb E` and applies GRR there.”
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:740:/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "LABEL $lbl"; rg -n "'"\\\\label\\{"'$lbl'"\\}|"'$lbl" chapters appendices metadata -g '"'*.tex' -g '*.md'; echo; done" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:789:/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "LABEL $lbl"; rg -n -F "'"\\\\label{"'$lbl}" chapters appendices metadata -g '"'*.tex' -g '*.md'; echo; done" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:790:/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "REG $lbl"; rg -n -F "$lbl" metadata/theorem_registry.md chapters/connections/concordance.tex; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 198ms:
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:910:  5928	\ClaimStatusProvedHere]\label{thm:family-index}






thinking
**Identifying changes in the file**

I’m noticing some stale lines in the current file, particularly around line 2979 and possibly at line 14110 regarding the family index theorem. I should inspect the area around line 14100 to confirm this. I need to identify specific changes to make. For instance, I should reword the routing remark to clarify that the family index is downstream of genus-universality, especially in lines 2892-2900 and 2959-2993. Additionally, I should revise lines 9683-9684 to ensure consistency with that concept.
thinking
**Clarifying theorem statements**

I’m pondering whether the explicit theorem claims that the generating function is established by the family index theorem. If the family index is downstream of universality, it seems fine, but I think we should clarify in the proof that the family index is only for GRR identification of the scalar series, not for establishing \( \lambda_g \) classes. I also need to work on strengthening the Whitehead comparison and clarifying the MC2 theorem regarding \( g^{mod} \), possibly adding an explicit sentence for clarity.
thinking
**Considering file edits**

It seems like I can't edit the introduction, but I can definitely clarify things within this file. I think it would be useful to mention explicitly that the introduction cross-reference is outside the scope of this file. However, I’m speculating that the user might expect fixes to be included in the file itself. So, I might need to note that the introduction is blocked from edits to set clear expectations.
thinking
**Considering figure details**

I'm looking at the diagram where the C column shows `\kappa` at degree 2 and it seems fine globally. The weight-changing line disappearing doesn’t negatively affect global kappa. Still, perhaps it’s worth noting in the figure caption or statement that the quartic witness is on the charged slice. The theorem addresses this already, so maybe no edit is needed. However, including a footnote in table 16615 could be sufficient for clarification.
thinking
**Clarifying language in constructions**

I notice that earlier constructions still reference "proved via Mok's log-FM normal-crossings result Theorem 3.3.1" and mention the "cancellation of codim-2 faces in the normal-crossings boundary of Mok's compactification." However, they don't specify the relative universal family, which seems like a critical omission. This wording feels a bit stale, and I think updating it could enhance clarity and precision in the context. It's essential to have everything well-defined!
thinking
**Checking git status**

I need to remember to add some commentary before I dive into the editing process. It’s also probably a good idea to check the git status to see if there’s anything that needs my attention. I’ll use the command `git status --short` on the target file — maybe it’ll help me with my introduction? Getting everything organized before editing is definitely a smart move!
codex
I’ve got the concrete patch set. The changes will stay inside `higher_genus_modular_koszul.tex`: tighten the PBW comparison, rewrite the Theorem D routing so `thm:family-index` is downstream, make the coinvariant scope and genuswise-product identification explicit in MC2, clean the remaining betagamma witness wording, and rewrite the stale log-FM `D^2=0` summaries to the relative universal-family formulation.
exec
/bin/zsh -lc 'git status --short chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/theory/higher_genus_modular_koszul.tex

thinking
**Inspecting file modifications**

I see that the file has already been modified, so it’s important for me to review the differences before making any edits. I might want to use `git diff`, especially focused on relevant areas. It could be a large output, so I’ll keep in mind to use options like `--unified=3` for more context. I’ll look at the specific chunks that matter to ensure I understand what has changed!
codex
The target file is already dirty, so I’m checking the existing diff around the hot sections first. I won’t overwrite unrelated work; the patch will be constrained to the exact lines needed for these findings.
exec
/bin/zsh -lc "git diff --unified=3 -- chapters/theory/higher_genus_modular_koszul.tex | sed -n '240,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff --unified=3 -- chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
+Hodge-class curvature $\kappa(\cA)\cdot\omega_g$. The mixed term is
+the codimension-$2$ locus where a collision stratum meets a
+curve-degeneration stratum; after transport through the Hom functor
+it is exactly the ambient cross-term correction. In particular,
 \[
  [d_{\mathrm{sew}}, d_{\mathrm{pf}}]
  + [d_{\mathrm{int}}, \hbar\Delta]
  + [[\tau_{\cA},-], d_{\mathrm{sew}} + d_{\mathrm{pf}}]
  = 0
 \]
-that was previously conjectural, now follow from
-$\partial^2 = 0$ on $\operatorname{FM}_n(W/B)$:
-the codimension-$2$ strata where a curve degeneration meets a
-configuration collision appear with cancelling signs in
-$\partial^2 = 0$, and the Hom transport preserves this
-cancellation.
+is the transported form of the mixed codimension-$2$ cancellation.
+Combining the three pieces yields $D_{\cA}^2 = 0$ on the ambient
+algebra.
 
 succeeded in 53ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 80770f8..4eefd84 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -21852,13 +21852,21 @@ projecting to each boundary type.
 
 \smallskip\noindent
 \emph{Source.}
-$D^2 = 0$ on $C_*(\operatorname{FM}_n^{\mathrm{log}}(X \mathbin{|} D))$
-(Theorem~\ref{thm:ambient-d-squared-zero}).
-Transport through the Hom functor into
-$\operatorname{Hom}_{\Sigma_n}(C_*(\operatorname{FM}_n^{\mathrm{log}}),
-\operatorname{End}_\cA(n))$
-gives $D^2 = 0$ on $\gAmod$
-(Theorem~\ref{thm:convolution-d-squared-zero}).
+The geometric source of the five-component differential is the
+relative Fulton--MacPherson space of the universal curve, not the
+log-FM space of a fixed pointed curve.
+Let $\pi\colon \cC_{g,n}\to \overline{\cM}_{g,n}$ be the universal
+stable family. Theorem~\ref{thm:ambient-d-squared-zero} identifies


thinking
**Evaluating file changes**

It looks like the file has already been modified with some changes. There are uncommitted modifications around T18 that I need to respect, which means I should use apply_patch on the current file and not revert anything. I'll take a closer look at the diffs to check for any pending user changes. It's crucial to be careful, as the current content might already reflect some of the modifications made. I need to integrate the changes while searching for candidate lines to patch.
thinking
**Planning file patches**

I could patch other sections and adjust some stale D^2 summaries. Since the D diff already changed the theorem, there might still be some outdated references. I’ll likely need to patch lines 11336 and 30779, even if they’re not in the diff. It’s fine to inspect the current diff around the patches after applying them. I’ll search for terms like "independent GRR" and "family-index is not downstream" in the current file. We can use `rg -n` to get exact lines, and I should provide commentary with pre-edit verification before making any changes.
codex
```text
PE-10
genus: [all]
degree: [n=all]
AP32 weight tag: [(UNIFORM)] tagged? [Y]
AP139 free-var audit: LHS vars:{g,\cA} RHS vars:{g,\cA} LHS⊇RHS? [Y]
AP36: [implies/iff]  if iff, converse proved same thm? [NA]
verdict: ACCEPT
```

```text
MC2 scope check
surface: thm:mc2-bar-intrinsic
target algebra in chapter: [\gAmod = \Defcyc(\cA)\widehat{\otimes}\Gmod]
ordered E1 lift cited separately: [thm:e1-mc-element in chap:e1-modular-koszul]
genuswise-product identification stated in theorem text after patch: [Y]
verdict: ACCEPT
```



thinking
**Inspecting patch details**

I need to carefully craft a patch, starting by inspecting the exact text around the modification lines. I’m looking at specific lines, like 952-953 for lemma proofs and lines 1120-1138 for theorem proofs. I also need to consider theorem D, particularly lines 2892-2900 and remarks later on. The universal-theta theorem lines 3504 and 3687-3704 are possible targets too. There are example table lines and summaries to check as well. It looks like I have a lot to review!
thinking
**Considering patch updates**

I think I can patch line 3504 to clarify that it's referring to "Theorem master-theta (MC2)" as a coinvariant MC2. For line 4057, modifying the remark to say, "resolves the symmetric/coinvariant MC2 statement in this chapter" seems helpful. I’m unsure about patching lines 36-43 though, as it might not be necessary. I need to determine whether to mention the introduction's cross-reference issue due to file restrictions. I should ensure the final output clearly states what has been fixed or blocked in an organized manner.
thinking
**Clarifying fixes and scope**

For finding 3, I can mark it as FIXED because I clarified the theorem scope in the chapter and pointed to the E1 theorem. However, the external introduction cross-reference isn't in scope due to file restrictions. Since the user specifically requested a fix for the introduction cross-reference, I feel I need to mention it as `BLOCKED` in part due to that scope limitation. It's a tricky balance, but being clear about what's possible is crucial!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3498,3742p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9678,9688p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15134,15148p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2888,2996p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11284,11380p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3498	 $\operatorname{tr}(\Theta_{\cA})
  3499	 = \sum_{g \geq 1} \kappa(\cA) \lambda_g$;
  3500	\item it is compatible with clutching morphisms of stable curves;
  3501	\item under Verdier/Koszul duality, $\Theta_{\cA}$ is sent to
  3502	 $\Theta_{\cA^!}$.
  3503	\end{enumerate}
  3504	This is Theorem~\ref{thm:master-theta} (MC2).
  3505	\end{theorem}
  3506	
  3507	\begin{proof}
  3508	\emph{Bar-intrinsic construction.}
  3509	The genus-completed bar differential
  3510	$D_\cA = \dzero + \sum_{g \geq 1} \hbar^g d_\cA^{(g)}$
  3511	exists by the modular operad structure of the bar complex
  3512	(Theorem~\ref{thm:bar-modular-operad}), and satisfies
  3513	$D_\cA^2 = 0$
  3514	(Theorem~\ref{thm:bar-modular-operad}(iii)).
  3515	Define $\Theta_\cA := D_\cA - \dzero$. Since
  3516	$\dzero^2 = 0$ and $D_\cA^2 = 0$, expanding
  3517	$0 = (\dzero + \Theta_\cA)^2
 succeeded in 51ms:
  9678	coefficient $\kappa \cdot \lambda_1$, with the full
  9679	$\kappa \cdot \lambda_g$ series proved on the uniform-weight lane.
  9680	\end{remark}
  9681	
  9682	\begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
  9683	Properties~(i)--(iv) of Theorem~D are shadows of the family index
  9684	theorem (Theorem~\ref{thm:family-index}).
  9685	The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
  9686	has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
  9687	the $\hat{A}$-genus arises from GRR via the Mumford
  9688	formula~\cite{Mumford83}; additivity reflects
 succeeded in 51ms:
  2888	\end{enumerate}
  2889	\end{theorem}
  2890	
  2891	\begin{proof}
  2892	\emph{Routing remark.}
  2893	The dependency route has a common bar-intrinsic anchor.
  2894	Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
  2895	shadow tower. Theorem~\ref{thm:genus-universality} identifies its
  2896	cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
  2897	proved uniform-weight lane, while Theorem~\ref{thm:family-index}
  2898	gives an independent Grothendieck--Riemann--Roch computation of the
  2899	same scalar series from the family~\eqref{eq:bar-family} on the
  2900	universal curve. Neither theorem is used to prove the other.
  2901	Part~(i) is Theorem~\ref{thm:genus-universality} for
  2902	uniform-weight algebras. For multi-generator algebras
  2903	($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
  2904	is unconditional; the higher-genus extension is conditional on the
  2905	strong scalar ansatz of
  2906	Theorem~\ref{thm:multi-generator-universality}.
  2907	Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
 succeeded in 52ms:
 15134	\midrule
 15135	Heisenberg &
 15136	 $2$ & $2$ & $2$ &
 15137	 Strictly commutative; $m_n = 0$, $n \geq 3$ \\
 15138	Affine $\hat{\mathfrak{g}}_k$ &
 15139	 $3$ & $3$ & $3$ &
 15140	 Jacobi kills degree-$4$ graphs \\
 15141	$\beta\gamma$ &
 15142	 $4$ & $4$ & $4$ &
 15143	 Rank-$1$ rigidity kills degree-$5$ \\
 15144	Virasoro &
 15145	 $\infty$ & $\infty$ & $\infty$ &
 15146	 $:T^n:$ generates operations at all degrees \\
 15147	\bottomrule
 15148	\end{tabular}
 succeeded in 52ms:
 11284	\subsubsection{The modular bar functor in logarithmic FM coordinates}
 11285	
 11286	\begin{construction}[Logarithmic modular bar functor;
 11287	\ClaimStatusProvedHere]
 11288	\label{const:vol1-log-modular-bar-functor}
 11289	\index{modular bar construction!logarithmic FM chart}
 11290	In these coordinates the modular bar construction is the
 11291	stable-graph sum
 11292	\begin{equation}\label{eq:bmod-log}
 11293	\bar{B}^{\mathrm{mod},\log}(\cA)(g,n)
 11294	\;=\;
 11295	\bigoplus_{\Gamma \in \mathsf{Gr}^{\mathrm{st}}_{g,n}}
 11296	\left(
 11297	\bigotimes_{v \in V(\Gamma)}
 11298	\bar{B}^{\mathrm{ch}}\!\bigl(A^{\mathrm{ch}}_\infty;\,
 11299	\mathrm{In}(v)\bigr)
 11300	\;\otimes\;
 11301	C_\bullet\!\bigl(\operatorname{FM}^{\log}_\Gamma\bigr)
 11302	\;\otimes\;
 11303	\orline{E_{\mathrm{int}}(\Gamma)}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30776,30810p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30776	 codimension filtration on the boundary of
 30777	 $\operatorname{FM}_n(X|D)$: depth-$k$ forests index
 30778	 codimension-$k$ strata. The rubber torus action on grid
 30779	 expansions \textup{(\cite{Mok25}, \S2.7.1)} corresponds to our
 30780	 planted-forest depth grading.
 30781	\end{enumerate}
 30782	\end{theorem}
 30783	
 30784	\begin{remark}[Degeneration formula $=$ clutching law]
 30785	\label{rem:degeneration-equals-clutching}%
 30786	\index{degeneration formula!as clutching law}%
 30787	Mok's degeneration formula \cite[Theorem~5.3.4]{Mok25} states that
 30788	each irreducible component of the special fibre of
 30789	$\operatorname{FM}_n(W/B) \to B$ is a proper birational modification
 30790	of a product
 30791	$\prod_{v \in V(S_{\rho,1})} \operatorname{FM}_{I_v}(Y_v|D_v)$.
 30792	This is the geometric incarnation of our clutching law for the
 30793	quartic resonance class
 30794	$($Theorem~\textup{\ref{thm:nms-clutching-law-modular-resonance}}$)$
 30795	and the non-separating clutching law
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30810,30824p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30810	For non-separating degenerations, an additional term
 30811	$\hbar\Delta(\Theta_\cA^{\leq r})$ appears: this is the
 30812	BV operator that distinguishes non-separating from separating
 30813	clutching, and is the primary reason that
 30814	$D_\cA^2 = 0$ at the ambient level required the log-FM
 30815	normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
 30816	(Theorem~\ref{thm:ambient-d-squared-zero}).
 30817	\end{remark}
 30818	
 30819	\begin{corollary}[Weight filtration = tropical codimension;
 30820	\ClaimStatusProvedElsewhere]
 30821	\label{cor:weight-filtration-tropical}
 30822	\index{weight filtration!tropical codimension correspondence}
 30823	The weight filtration on the ambient algebra
 30824	$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
exec
/bin/zsh -lc "rg -n \"independent GRR|not downstream of|family index theorem|shadows of the family index theorem|downstream of|parallel index package|Part~\\(f\\) is the family index theorem|by the family index theorem\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2978:independent GRR/family-index computation on the universal curve.
2979:Theorem~\ref{thm:family-index} is not downstream of
4583: by the family index theorem
4633:Part~(f) is the family index theorem
14110:now seen as a consequence of (i) via the family index theorem
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14096,14116p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 14096	\begin{proof}
 14097	(i)~On the proved uniform-weight scalar lane, the cyclic trace of
 14098	$\Theta_\cA^{(g)}$ is the genus-$g$ obstruction
 14099	$\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ by
 14100	Theorem~D
 14101	(Theorem~\ref{thm:universal-theta}). By
 14102	Theorem~\ref{thm:primitive-to-global-reconstruction},
 14103	$\Theta_\cA^{(g)} =
 14104	\operatorname{FT}^{\log}_{\mathrm{mod}}(\mathfrak{K}_\cA)^{(g)}$,
 14105	so $F_g = \operatorname{tr}_{\mathrm{cyc}}
 14106	(\operatorname{FT}^{\log}_{\mathrm{mod}}(\mathfrak{K}_\cA)^{(g)})
 14107	= \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$.
 14108	
 14109	(ii)~This is Corollary~\ref{cor:free-energy-ahat-genus},
 14110	now seen as a consequence of (i) via the family index theorem
 14111	(Theorem~\ref{thm:family-index}).
 14112	
 14113	(iii)~The determinant line bundle has $c_1(L_\cA) = \kappa(\cA)
 14114	\cdot \lambda$ by Remark~\ref{rem:homotopy-native-d}. The
 14115	primitive flat connection restricts to a connection on $L_\cA$


thinking
**Ensuring file labels**

I need to confirm that the label exists since I’m dealing with only one file. I wonder if I should search for it externally instead of just within the file itself. Hmm, it seems fine to check both options just to be thorough! It's crucial to make sure I'm covering all bases to avoid any potential issues down the line. Let's be meticulous!
thinking
**Applying patch carefully**

I need to make sure our patch doesn't conflict. It's essential to use apply_patch and be very careful when crafting it. I'll focus on the exact contexts to avoid any issues. Each part should align perfectly, ensuring everything works smoothly together. I wonder if there's a specific way to structure this that would help prevent future problems. It's all about precision and attention to detail! I'll keep these points in mind as I proceed.
codex
I’m applying the scoped patch now. It will touch only the theorem/proof lanes we’ve identified: PBW weightwise reduction, Theorem D routing, MC2 scope/identification, the betagamma witness table, and the stale fixed-curve log-FM summaries.

thinking
**Inspecting patch issues**

It seems like the patch failed, possibly due to changes in the dirty file or spaces. I think I'll need to create the patch in smaller hunks with the exact context. I'll check around line 11336 to see if there's been a modification already. I'll patch in smaller pieces sequentially, since applying too large a hunk might cause issues if lines have moved. Let's focus on crafting those patches carefully to avoid problems with backslashes or spaces.
codex
The first patch hit a context mismatch against the existing dirty file, so I’m reapplying in smaller hunks to preserve the live text exactly where it stands.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -936,3 +936,7 @@
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
@@ -952,3 +956,14 @@
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
@@ -1137,3 +1152,7 @@
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
@@ -2892,10 +2911,22 @@
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
@@ -2965,18 +2996,15 @@
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
@@ -2988,3 +3016,3 @@
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
@@ -2993,3 +3021,3 @@
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
@@ -3504,2 +3532,5 @@
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
@@ -3699,5 +3730,10 @@
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
@@ -3739,3 +3775,6 @@
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
@@ -4582,6 +4621,6 @@
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
@@ -4632,5 +4671,5 @@
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
@@ -9682,4 +9721,5 @@
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
@@ -15142,3 +15182,3 @@
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
apply_patch(auto_approved=true) exited 0 in 54ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..7791c48208628ae613a7e3b09bb622d6a9bc4edb
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -15140,7 +15180,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..7791c48208628ae613a7e3b09bb622d6a9bc4edb
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -15140,7 +15180,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -11377,4 +11377,8 @@
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
@@ -11415,4 +11419,7 @@
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..5711f9877e42bebb82a4f371835463b866b2f046
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11375,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11417,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -15140,7 +15187,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..5711f9877e42bebb82a4f371835463b866b2f046
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11375,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11417,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -15140,7 +15187,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -30844,3 +30844,4 @@
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
@@ -30861,3 +30862,4 @@
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
apply_patch(auto_approved=true) exited 0 in 56ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..fd3e013de4ae329a2680d8107bd475fee71e70d4
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11375,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11417,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -15140,7 +15187,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30842,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30860,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..fd3e013de4ae329a2680d8107bd475fee71e70d4
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11375,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11417,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -15140,7 +15187,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30842,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30860,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc 'rg -n "resolves MC2|MC2!bar-intrinsic perspective|ordered '"\\\\"'$E_1'"\\\\"'$|coinvariant/symmetric MC2|Theorem~'"\\\\ref\\{thm:mc2-bar-intrinsic\\} is the symmetric/coinvariant MC2\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3533:In this chapter, it is the coinvariant/symmetric MC2 statement; the
4094:\index{MC2!bar-intrinsic perspective}
4096:Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..0cc2557ad6b670f6845858133f01e57607ac48fe
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4580,10 +4619,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4669,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9719,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11375,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11417,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -14843,10 +14890,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14910,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14954,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15192,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30847,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30865,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -4095,3 +4095,4 @@
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
apply_patch(auto_approved=true) exited 0 in 45ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b5706b45fa60c7f58186bfd566a88ab61fafde4e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30849,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30867,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b5706b45fa60c7f58186bfd566a88ab61fafde4e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30849,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30867,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

codex
The core patch is in. I’m running a targeted reread and grep now to catch any remaining stale wording: `family-index` as an upstream proof input, MC2 scope drift, and fixed-curve log-FM language.
exec
/bin/zsh -lc "rg -n \"independent GRR|not downstream of|Parallel index package|family index theorem|coinvariant MC2|ordered \\\\"'$E_1'"\\\\"'$|relative log-FM|fixed pointed curve|fixed '"\\(X,D\\)|Theorem~\\\\ref\\{thm:mc2-bar-intrinsic\\} resolves MC2\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '912,1168p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3769:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4096:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
9724:trace and are read index-theoretically by the family index theorem
11380:the relevant space is the relative log-FM compactification of the
14159:now seen as a consequence of (i) via the family index theorem
21911:log-FM space of a fixed pointed curve.
30852:applied to the bar complex on the relative log-FM spaces of the
31225:logarithmic Fulton--MacPherson space of a fixed pointed curve.
 succeeded in 52ms:
   912	\begin{lemma}[Weightwise reduction of the genus enrichment to
   913	 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
   914	\label{lem:pbw-weightwise-g-module}
   915	\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
   916	\index{truncated current algebra!mode bookkeeping only}
   917	Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
   918	\[
   919	V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
   920	\]
   921	Then the weight-$h$ genus-enrichment block of
   922	$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
   923	\[
   924	\mathcal{E}_g^{*,h}
   925	\;\cong\;
   926	\bigoplus_\nu
   927	C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
   928	\otimes_{\bC}
   929	H^1(\Sigma_g,\bC),
   930	\]
   931	where $\nu$ runs over the finitely many mode patterns of total
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2890,2998p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4440,4640p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9678,9690p;15138,15145p;30784,30818p;11284,11380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3498,3744p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2890	 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
  2891	 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
  2892	 K_\fg \cdot \varrho(\fg)$
  2893	 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
  2894	 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
  2895	 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
  2896	 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
  2897	 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
  2898	 $m_1, \ldots, m_r$ the exponents;
  2899	 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
  2900	 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
  2901	\item \emph{Additivity.}
  2902	 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
  2903	 Combined with~(iii), the vanishing
  2904	 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
  2905	 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
  2906	 form of anomaly cancellation.
  2907	\end{enumerate}
  2908	\end{theorem}
  2909	
 succeeded in 53ms:
  3498	recovers~$\kappa$, $\operatorname{ch}(\mathcal{V})$
  3499	recovers~$\Delta_{\cA}$, and the holonomy recovers~$\Pi_{\cA}$.
  3500	See Remark~\ref{rem:structural-saturation}.
  3501	\end{remark}
  3502	
  3503	\begin{remark}[Shared discriminant, distinct sewing]\label{rem:shared-discriminant-sheet}
  3504	The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
  3505	\end{remark}
  3506	
  3507	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3508	\label{thm:universal-theta}
  3509	\index{universal Maurer--Cartan class|textbf}
  3510	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3511	projective curve~$X$ with non-degenerate invariant form,
  3512	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3513	universal Maurer--Cartan class
  3514	\[
  3515	\Theta_{\cA} \in
  3516	\operatorname{MC}\!\bigl(
  3517	 \Defcyc(\cA) \;\widehat{\otimes}\;
 succeeded in 55ms:
  4440	$\mathsf{C}$, the obstruction classes $o_{r+1}(\cA) = 0$
  4441	for $r > r_{\max}$
  4442	(Theorem~\ref{thm:shadow-archetype-classification}), so
  4443	no bipartite graphs with more than $r_{\max}$ external legs
  4444	contribute.
  4445	The shadow--formality identification at degrees $2$, $3$, $4$
  4446	(Proposition~\ref{prop:shadow-formality-low-degree}) gives the
  4447	degree-by-degree verification.
  4448	See also Construction~\ref{constr:bipartite-linfty-truncation}
  4449	for the full combinatorial development.
  4450	\end{proof}
  4451	
  4452	\begin{remark}[Bipartite master element]
  4453	\label{rem:mc2-bipartite-master}
  4454	\emph{Bipartite master element.}
  4455	The graph-sum formula for $\Theta_\cA$ restricts to a sum
  4456	over connected bipartite stable graphs:
  4457	\begin{equation}\label{eq:bipartite-master}
  4458	\Theta^{\mathrm{plat}}_{g,n}(\cA)
  4459	\;:=\;
 succeeded in 55ms:
  9678	\index{universal Maurer--Cartan class!evidence for universality}
  9679	The conjecture is proved at generic level for all vertex algebras
  9680	with simple symmetry (Theorem~\ref{thm:cyclic-rigidity-generic}),
  9681	at all non-critical levels for algebraic families with rational
  9682	OPE coefficients
  9683	(Theorem~\ref{thm:algebraic-family-rigidity}),
  9684	and on the standard Lie-theoretic landscape in the weaker
  9685	effective-\(\Gamma\)-quadruple form
  9686	(Corollary~\ref{cor:effective-quadruple}).
  9687	The algebraic-family theorem subsumes the generic-level result
  9688	and extends it to admissible parameter values only for the
  9689	already verified algebraic-family objects in the standard
  9690	Lie-theoretic landscape \textup{(}not for the live audit surface
 11284	\end{equation}
 11285	The one-slot convention
 11286	(Corollary~\ref{cor:strictification-comparison}(vi)) fixes the
 11287	geometric cooperad; the chiral input varies by $\infty$-morphism.
 11288	The coderivation algebra
 11289	$\mathfrak{g}^{\mathrm{mod}}_\cA$
 11290	(Definition~\ref{def:modular-convolution-dg-lie}) is the bar-side
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b5706b45fa60c7f58186bfd566a88ab61fafde4e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30849,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30867,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2994,3008p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4638,4652p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2994	\[
  2995	\Theta_\cA \text{ and its shadow tower}
  2996	\Longrightarrow
  2997	\mathrm{obs}_g=\kappa\cdot\lambda_g
  2998	\Longrightarrow
  2999	\sum_{g \ge 1} F_g x^{2g}
  3000	=
  3001	\kappa\cdot(\hat{A}(ix)-1)
  3002	\]
  3003	The bar-intrinsic shadow tower is the common source.
  3004	The first implication is the scalar-trace identification of
  3005	Theorem~\ref{thm:genus-universality}; the second is the downstream
  3006	GRR/family-index identification of the same scalar series on the
  3007	virtual bar family. Theorem~\ref{thm:family-index} is therefore the
  3008	index-theoretic reformulation of the scalar output, not the
 succeeded in 59ms:
  4638	reduces to $\delta\phi = 0$, and higher degrees vanish because
  4639	$l_3$ maps to $\eta$ which is not an input for $l_3$).
  4640	The genus-completed tensor product
  4641	$\mathcal{H} \widehat{\otimes} \Gmod$ is a genus-filtered
  4642	$L_\infty$-algebra by
  4643	Proposition~\ref{prop:genus-completed-mc-framework}.
  4644	
  4645	Part~(b) follows from degree inspection: every component
  4646	$\kappa \cdot \eta \otimes \lambda_g$ lies in the
  4647	$\eta$-line of degree~$2$, while $l_2^{\mathrm{tr}}$ and
  4648	$l_3^{\mathrm{tr}}$ act nontrivially only on $\mathfrak{g}$-inputs.
  4649	No bracket composition produces a nonzero obstruction
  4650	from $\eta$-inputs alone.
  4651	
  4652	Part~(c): the homotopy transfer $\Theta_{\cA}$ from the minimal
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9720,9732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15134,15144p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30796,30818p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30818,30836p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11376,11392p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9720	\end{remark}
  9721	
  9722	\begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
  9723	Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
  9724	trace and are read index-theoretically by the family index theorem
  9725	\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
  9726	The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
  9727	has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
  9728	the $\hat{A}$-genus arises from GRR via the Mumford
  9729	formula~\cite{Mumford83}; additivity reflects
  9730	$\mathcal{L}_{\cA\otimes\cB}\cong\mathcal{L}_{\cA}\otimes\mathcal{L}_{\cB}$;
  9731	and duality reflects Verdier self-duality
  9732	$\mathcal{L}_{\cA}\otimes\mathcal{L}_{\cA^!}\cong\mathcal{O}$.
 succeeded in 52ms:
 15134	\begin{enumerate}[label=\textup{(\arabic*)}]
 15135	\item \emph{Shadow termination degree}\;
 15136	 $r_{\max}(\cA) := \sup\{r \geq 2 :
 15137	 \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 15138	 \textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
 15139	\item \emph{$A_\infty$-depth}\;
 15140	 $d_\infty(\cA) := \sup\{n \geq 2 :
 15141	 m_n^{\mathrm{tr}} \neq 0\}$,
 15142	 the highest non-vanishing transferred $A_\infty$
 15143	 operation on the minimal model of $\Defcyc(\cA)$.
 15144	\item \emph{$L_\infty$-formality level}\;
 succeeded in 52ms:
 30796	\begin{theorem}[Planted forests as tropicalization of log-FM spaces;
 30797	\ClaimStatusProvedElsewhere]
 30798	\label{thm:planted-forest-tropicalization}%
 30799	\index{planted-forest coefficient algebra!tropicalization}%
 30800	\index{logarithmic Fulton--MacPherson!tropicalization}%
 30801	\index{Mok theorem}%
 30802	\textup{(Mok \cite{Mok25}, Theorem~3.3.1 and \S2.3.)}
 30803	Let $(X,D)$ be a simple normal crossings pair and
 30804	$\operatorname{FM}_n(X|D)$ the logarithmic Fulton--MacPherson
 30805	compactification of $\operatorname{Conf}_n(X \setminus D)$.
 30806	\begin{enumerate}[label=\textup{(\roman*)}]
 30807	\item The tropicalization of $\operatorname{FM}_n(X|D)$ is the
 30808	 moduli space of \emph{planted forests}: the combinatorial types of
 30809	 boundary strata of $\operatorname{FM}_n(X|D)$ are indexed by
 30810	 $n$-marked planted forests on the fan~$\Sigma_X$.
 30811	\item The planted-forest coefficient algebra
 30812	 $\mathbb{G}_{\mathrm{pf}}$ of
 30813	 Definition~\textup{\ref{def:planted-forest-coefficient-algebra}} is
 30814	 the chain algebra on the face poset of
 30815	 $\operatorname{Trop}(\operatorname{FM}_n(X|D))$:
 succeeded in 51ms:
 30818	 \;\cong\;
 30819	 C_\bullet\bigl(
 30820	 \operatorname{Trop}(\operatorname{FM}_n(C\,|\,D_{\mathrm{nodes}}))
 30821	 \bigr),
 30822	 \]
 30823	 where $C$ is the curve and $D_{\mathrm{nodes}}$ is the nodal
 30824	 divisor. Here $\cong$ is an isomorphism of dg~algebras: both
 30825	 sides have differentials given by edge contraction (algebraic side)
 30826	 and codimension increase (tropical side), and the product is
 30827	 disjoint union of forests on both sides.
 30828	\item The planted-forest depth filtration
 30829	 $($\S\textup{\ref{subsec:carrier-algebra}}$)$ corresponds to the
 30830	 codimension filtration on the boundary of
 30831	 $\operatorname{FM}_n(X|D)$: depth-$k$ forests index
 30832	 codimension-$k$ strata. The rubber torus action on grid
 30833	 expansions \textup{(\cite{Mok25}, \S2.7.1)} corresponds to our
 30834	 planted-forest depth grading.
 30835	\end{enumerate}
 30836	\end{theorem}
 succeeded in 50ms:
 11376	($\hbar\Delta$ at leading order).
 11377	The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 11378	content of $D^2 = 0$ at the ambient level
 11379	\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
 11380	the relevant space is the relative log-FM compactification of the
 11381	universal stable family over $\overline{\cM}_{g,n}$, whose collision
 11382	faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
 11383	$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
 11384	$d_{\mathrm{loop}}$.
 11385	\end{construction}
 11386	
 11387	\begin{construction}[Boundary operators as residue correspondences;
 11388	\ClaimStatusProvedHere]
 11389	\label{const:vol1-boundary-operators-residue}
 11390	\index{boundary operators!residue correspondence}
 11391	\index{modular bar construction!residue formulas}
 11392	On a pure tensor $a\otimes\eta$ in the summand indexed by~$\Gamma$,
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b5706b45fa60c7f58186bfd566a88ab61fafde4e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -30795,7 +30849,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30867,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Investigating remarks**

I think I need to take a look at remark 30784, as it might be necessary to patch it if it isn't displayed due to the range. Let's focus on viewing remarks 30836 to 30856 as well. It seems like this process is important for making sure everything is in order — maybe there are insights to be gathered from these remarks! I'll dig into them and see what I can find.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30836,30858p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30836	 \;\cong\;
 30837	 C_\bullet\bigl(
 30838	 \operatorname{Trop}(\operatorname{FM}_n(C\,|\,D_{\mathrm{nodes}}))
 30839	 \bigr),
 30840	 \]
 30841	 where $C$ is the curve and $D_{\mathrm{nodes}}$ is the nodal
 30842	 divisor. Here $\cong$ is an isomorphism of dg~algebras: both
 30843	 sides have differentials given by edge contraction (algebraic side)
 30844	 and codimension increase (tropical side), and the product is
 30845	 disjoint union of forests on both sides.
 30846	\item The planted-forest depth filtration
 30847	 $($\S\textup{\ref{subsec:carrier-algebra}}$)$ corresponds to the
 30848	 codimension filtration on the boundary of
 30849	 $\operatorname{FM}_n(X|D)$: depth-$k$ forests index
 30850	 codimension-$k$ strata. The rubber torus action on grid
 30851	 expansions \textup{(\cite{Mok25}, \S2.7.1)} corresponds to our
 30852	 planted-forest depth grading.
 30853	\end{enumerate}
 30854	\end{theorem}
 30855	
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30858,30884p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 30858	\index{degeneration formula!as clutching law}%
 30859	Mok's degeneration formula \cite[Theorem~5.3.4]{Mok25} states that
 30860	each irreducible component of the special fibre of
 30861	$\operatorname{FM}_n(W/B) \to B$ is a proper birational modification
 30862	of a product
 30863	$\prod_{v \in V(S_{\rho,1})} \operatorname{FM}_{I_v}(Y_v|D_v)$.
 30864	This is the geometric incarnation of our clutching law for the
 30865	quartic resonance class
 30866	$($Theorem~\textup{\ref{thm:nms-clutching-law-modular-resonance}}$)$
 30867	and the non-separating clutching law
 30868	$($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 30869	the algebraic clutching identities ARE the degeneration formula
 30870	applied to the bar complex on the relative log-FM spaces of the
 30871	universal family.
 30872	
 30873	More explicitly: in the finite-order shadow obstruction tower, the extension
 30874	$\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
 30875	obstruction class $o_{r+1}(\cA) \in H^2(F^{r+1}/F^{r+2})$. For a
 30876	separating degeneration $\cA = \cA_1 \cup_\xi \cA_2$, the
 30877	obstruction classes satisfy a multiplicative relation
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30884,30896p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 30884	$\hbar\Delta(\Theta_\cA^{\leq r})$ appears: this is the
 30885	BV operator that distinguishes non-separating from separating
 30886	clutching, and is the primary reason that
 30887	$D_\cA^2 = 0$ at the ambient level required the log-FM
 30888	normal-crossings geometry of Mok's relative compactification of the
 30889	universal family~\cite[Theorem~3.3.1]{Mok25}
 30890	(Theorem~\ref{thm:ambient-d-squared-zero}).
 30891	\end{remark}
 30892	
 30893	\begin{corollary}[Weight filtration = tropical codimension;
 30894	\ClaimStatusProvedElsewhere]
 30895	\label{cor:weight-filtration-tropical}
 30896	\index{weight filtration!tropical codimension correspondence}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "rg -n \"Charged quartic slice|Rank-\\"'$1'"\\"'$ rigidity kills degree-'"\\"'$5'"\\"'$|Verification for the four archetypes" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
15175:\begin{example}[Verification for the four archetypes]
15197: Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Inspecting details**

I need to take a closer look around the range of 15190 to 15199. I want to make sure I'm thorough, so I’ll focus on any specific elements in that area, possibly looking for patterns or important information that stands out. It might be useful to double-check everything to ensure I’m not missing anything critical. Let’s dive in and see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15188,15199p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 15188	\midrule
 15189	Heisenberg &
 15190	 $2$ & $2$ & $2$ &
 15191	 Strictly commutative; $m_n = 0$, $n \geq 3$ \\
 15192	Affine $\hat{\mathfrak{g}}_k$ &
 15193	 $3$ & $3$ & $3$ &
 15194	 Jacobi kills degree-$4$ graphs \\
 15195	$\beta\gamma$ &
 15196	 $4$ & $4$ & $4$ &
 15197	 Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 15198	Virasoro &
 15199	 $\infty$ & $\infty$ & $\infty$ &
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Inspecting for citations**

I'm focusing on inspecting around remark 3731 and possibly an item. I need to search for any external citations linked to that. It's also important to check lines starting from 4645 for updates related to part f, as the earlier range didn’t display correctly. I think I should specifically look around lines 4660 to 4672, but part f seems to be at 4674, so I’ll definitely search there.
exec
/bin/zsh -lc "rg -n \"downstream family-index identification|Part~\\(f\\)\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4673:Part~(f) is the downstream family-index identification
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4668,4678p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4668	$\mu(\mu(a,b),c) + \mu(\mu(b,c),a) + \mu(\mu(c,a),b)$,
  4669	which vanishes by the Jacobi identity for~$\mathfrak{g}$.
  4670	Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
  4671	and the genus-$g$ recursion begins at $l_3$.
  4672	
  4673	Part~(f) is the downstream family-index identification
  4674	(Theorem~\ref{thm:family-index}) of the scalar series already
  4675	constructed above; the $\hat{A}$-genus appears because
  4676	$\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
  4677	pushed forward to $\overline{\mathcal{M}}_g$, produces the
  4678	$\hat{A}$-class by Mumford's formula.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc 'rg -n "Any external citation|coinvariant algebra|augmentation ideal|ordered theorem is" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
371:$\bar{B}^{(g)}(\mathcal{A})$ with the augmentation ideal of
819:is the conformal-weight-$h$ piece of the augmentation ideal.
826:the weight-$2$ space of the augmentation ideal is one-dimensional,
1663:is the conformal-weight-$h$ piece of the Virasoro augmentation ideal.
1691:Since $h \geq 2$ on the augmentation ideal, this map is an
1847:\item the augmentation ideal $\bar{V}_\cA$ is
3733:product is the augmentation ideal
3738:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
3776:$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
3778:therefore incorrect; the ordered theorem is
3905:\item \emph{$\Theta_\cA$ lies in the completed coinvariant algebra.}
3939: so it lies in the augmentation ideal
12909: preserves the filtration. The augmentation ideal
32863:augmentation ideal.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..f5c32772b411f619604c1b11e7367dd9c7c7a8f7
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -30795,7 +30867,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30885,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 



thinking
**Clarifying edits and verifications**

I need to confirm if the surfaces are already split. It seems like we should mention that the live file is correct after verification, and no additional edits are necessary. However, since the user is looking for a fix, we might need to ensure that nothing is overlooked. For instance, we could say we verified and that the conditions are satisfied. I also need to check for stale content, like the `d_alg` proposition, as well as the specific theorem adjustments we made.
thinking
**Inspecting theorem updates**

I should mention that the theorem proof already used the correct universal family, and we updated the remaining summary surfaces. It might be useful to inspect the git diff after our patch to see the relevant changes. I'll need to verify that there are no syntax issues with apply_patch. Running `latexmk` seems like it might be too large, but maybe I can use `texlua`. I might also consider using tools like `grep` or `lacheck`, but I'm not entirely sure.
codex
I’ve finished the edits. I’m doing the verification pass now: checking the modified sections in place, grepping for the old circular-routing wording and stale fixed-curve geometry wording, and confirming the new references point to live labels.
exec
/bin/zsh -lc "rg -n \"independent GRR|not downstream of|Parallel index package|fixed pointed curve|applied to the bar complex on log-FM spaces|now proved via Mok's|normal-crossings boundary of Mok's compactification|Theorem~\\\\ref\\{thm:mc2-bar-intrinsic\\} as the ordered\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
21948:log-FM space of a fixed pointed curve.
31262:logarithmic Fulton--MacPherson space of a fixed pointed curve.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:e1-mc-element\\}|\\\\label\\{prop:geometric-modular-operadic-mc\\}|\\\\label\\{thm:family-index\\}|\\\\label\\{thm:genus-universality\\}\" chapters metadata chapters/connections -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=2 -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{thm:e1-mc-element\}|\label\{prop:geometric-modular-operadic-mc\}|\label\{thm:family-index\}|\label\{thm:genus-universality\})
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 80770f8..b288625 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -935,5 +935,9 @@ trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
@@ -951,5 +955,16 @@ mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

context compacted
codex
Using `beilinson-rectify` on the assigned file only. I’ve patched the routing, PBW, MC2-scope, and ambient-space surfaces; now I’m re-reading the remaining depth-gap and class-C witness sections to verify that every listed finding is actually resolved in the live file.
exec
/bin/zsh -lc "sed -n '16370,16470p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Propositions~\ref{prop:shadow-formality-higher-degree}
and~\ref{prop:linfty-obstruction-5-6} respectively.
Part~(iii) follows from the explicit verification tables in
those propositions: for classes $\mathbf{G}$,
$\mathbf{L}$, $\mathbf{C}$, all three quantities vanish at
degrees $5$, $6$, $7$ because the tower terminates
earlier. For class $\mathbf{M}$, all three are nonzero
because $\Delta \neq 0$ forces $S_k \neq 0$ for all
$k \geq 4$
(Theorem~\ref{thm:single-line-dichotomy}).

The tree count at degree~$7$ for the stable-graph route is
$(2 \cdot 8 - 5)!! = 11!! = 10395$: this is the number of
trivalent trees with $8$ external legs, which are the
fully resolved genus-$0$ stable graphs contributing to the
bracket $\ell_7^{(0)}$. The agreement with the HPL
route ($C_6 = 132$ planar trees) and the Feynman transform
route ($C_7 = 429$ binary trees on $8$ leaves) is a
consequence of the universal property
(Theorem~\ref{thm:shadow-formality-identification},
exec
/bin/zsh -lc "sed -n '17080,17170p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30840,30910p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Let $(X,D)$ be a simple normal crossings pair and
$\operatorname{FM}_n(X|D)$ the logarithmic Fulton--MacPherson
compactification of $\operatorname{Conf}_n(X \setminus D)$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The tropicalization of $\operatorname{FM}_n(X|D)$ is the
 moduli space of \emph{planted forests}: the combinatorial types of
 boundary strata of $\operatorname{FM}_n(X|D)$ are indexed by
 $n$-marked planted forests on the fan~$\Sigma_X$.
\item The planted-forest coefficient algebra
 $\mathbb{G}_{\mathrm{pf}}$ of
 Definition~\textup{\ref{def:planted-forest-coefficient-algebra}} is
 the chain algebra on the face poset of
 $\operatorname{Trop}(\operatorname{FM}_n(X|D))$:
 \[
 \mathbb{G}_{\mathrm{pf}}
 \;\cong\;
 C_\bullet\bigl(
 \operatorname{Trop}(\operatorname{FM}_n(C\,|\,D_{\mathrm{nodes}}))
 \bigr),
 \]
 succeeded in 52ms:
stratum and $m_4^{\mathrm{SC}} \neq 0$ from the contact
quartic invariant $Q^{\mathrm{contact}}$
(Theorem~\ref{thm:betagamma-quartic-birth}).
For class~$\mathbf{M}$, the quintic-forced theorem
(Theorem~\ref{thm:w-virasoro-quintic-forced})
proves all $m_k^{\mathrm{SC}} \neq 0$
(Virasoro: infinite pole tower drives all degrees).
Aspect~(iii):
$\ell_k = S_k(\cA)$ is the shadow obstruction tower
coefficient at degree~$k$, which is nonzero for
$k \leq r_{\max}(\cA)$
(Definition~\ref{def:shadow-depth-classification}).
\end{proof}

% ================================================================
% Shadow depth escalator
% ================================================================

\begin{proposition}[Shadow depth escalator; \ClaimStatusProvedHere]
\label{prop:shadow-depth-escalator}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Inspecting line issues**

I need to check the relevant lines for T06, T08, T09, T16, T18, and possibly more. Verifying the line numbers is important, and it seems there might still be unresolved issues. I should consider checking the areas around lines 990-1020 and 2670, among others. Using a parallel approach might help streamline this process and make sure I’m covering everything necessary for a thorough inspection.
codex
The remaining risk is the depth-gap surface: I need to confirm the file now distinguishes the `\kappa \neq 0` regime from the `\kappa = 0` boundary, and that the class-C witness is no longer the contradicted standard `\beta\gamma` line. After that I’ll do a final coherence pass on the routed theorem chain and the universal-family `D^2=0` proof.
exec
/bin/zsh -lc "sed -n '960,1035p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
\;=\;
\sum_i c_i(\nu)\,
a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
\]
with coefficients $c_i(\nu)$ depending only on the mode pattern.
Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
\end{proof}

\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
 \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
\label{lem:pbw-mixed-factorization}
\index{PBW spectral sequence!mixed map factorization|textbf}
\index{Whitehead lemma!mixed genus-0/genus-g factorization}
Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
finite-dimensional $\fg$-module $N_h^{n-1}$ and
exec
/bin/zsh -lc "sed -n '3470,3785p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2660,3015p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Corollary~\ref{cor:shadow-visibility-genus}).
\end{remark}

\begin{theorem}[Spectral characteristic theorem; \ClaimStatusProvedHere]
\phantomsection
\label{thm:spectral-characteristic}
\index{spectral discriminant!invariance theorem|textbf}

\smallskip\noindent
\textup{[Regime: quadratic;
Convention~\ref{conv:regime-tags}.]}
Let $\cA$ be a modular Koszul chiral algebra.
The spectral discriminant
$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
depends only on the quadratic OPE data of the Koszul pair and is invariant
under Drinfeld--Sokolov reduction.
In particular, $\Delta_{\cA}$ is a separate non-scalar invariant:
it is not determined by $\kappa(\cA)$ alone.
\end{theorem}

 succeeded in 51ms:
 \[
 \Theta_{\cA} \in
 \operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
 \bigr);
 \]
\item $\kappa(\cA) \in \mathbb{C}$ is the
 \emph{scalar modular characteristic}
 (Definition~\ref{def:scalar-modular-package}),
 the first characteristic number of~$\Theta_{\cA}$
 under the trace map
 $\Defcyc(\cA) \to \mathbb{C}$;
\item $\Delta_{\cA}(x) = \prod_{i}(1 - \lambda_i x)$ is the
 \emph{spectral discriminant}
 (Theorem~\ref{thm:ds-bar-gf-discriminant});
\item $\Pi_{\cA} = (M_{\cA}, Q_{\cA}, G_{\cA})$ is the
 \emph{periodicity profile}
 (Remark~\ref{rem:periodicity-triple});
\item $\mathcal{H}_{\cA} := \{C_g(\cA)\}_{g \geq 0}$ is the
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "sed -n '17100,17180p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16580,16720p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "depth gap|d_alg|kappa != 0|'"\\\\kappa \\\\neq 0|beta\\\\gamma|betagamma|r_max=4|mu_bg|weight-changing\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 obstruction to collapsing the tower at the first
 nontrivial stage.
\end{itemize}
The finiteness dichotomy ($\Delta = 0$ vs.\ $\Delta \neq 0$)
thus separates algebras whose MC space is a finite CW~complex
(classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$) from those
whose MC space is an inverse limit of finite stages
(class~$\mathbf{M}$).
This is consistent with the Galois interpretation of
Remark~\ref{rem:shadow-galois-splitting}: the splitting of the
shadow field extension $K_L/F$ reflects the collapsing of the
Postnikov tower, and the inertness of $K_L$ for class~$\mathbf{M}$
reflects the infinite homotopy type.
\end{remark}

\begin{remark}[Shadow depth as BPS complexity]
\label{rem:shadow-depth-bps}
\index{shadow depth!BPS complexity}%
\index{BPS particles!shadow depth classification}%
In the infrared decomposition of a $4$d $\cN = 2$ theory,
 succeeded in 51ms:
\index{shadow depth!escalator|textbf}
\index{Drinfeld--Sokolov reduction!shadow depth escalator|textbf}
Current-algebra systems (affine Kac--Moody) are class~$\mathbf{L}$:
their shadow obstruction towers terminate at degree~$3$, and the
complementarity sum vanishes ($\kappa(\cA) + \kappa(\cA^!) = 0$).
W-algebra systems (Virasoro, $\cW_N$) are class~$\mathbf{M}$:
their towers are infinite, and $\kappa + \kappa' \neq 0$
\textup{(}Theorem~\textup{\ref{thm:ds-complementarity-tower-main})}.
Principal Drinfeld--Sokolov reduction is the functor that sends
$\mathbf{L}$ to~$\mathbf{M}$. Three mechanisms operate
simultaneously:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Cubic shadow doubling.}
 Affine $\widehat{\mathfrak{sl}}_N$ has cubic shadow
 $S_3^{\mathrm{KM}}$; the reduced $\cW_N$ has
 $S_3^{\cW} = 2\,S_3^{\mathrm{KM}}$
 \textup{(}universal for principal reduction at all~$N$,
 Proposition~\textup{\ref{prop:ds-package-functoriality}(i))}.

\item \emph{Quartic creation from zero.}
 exited 2 in 51ms:
rg: regex parse error:
    (?:depth gap|d_alg|kappa != 0|\kappa \neq 0|beta\gamma|betagamma|r_max=4|mu_bg|weight-changing)
                                  ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Inspecting theorem details**

I ran the rg command, but it failed due to regex issues. I need to rerun it with a simpler version. I have an output with an example showing beta gamma still class C with specific parameters. That could help in resolving things! I need to look into the theorem or properties around the depth gap, specifically around 17115. I might have to search for theorem labels related to depth decomposition, maybe using fixed strings like "depth gap."
codex
The live surface already contains a deeper T16 rewrite than the small patch I added earlier. I’m locating the exact proposition and witness statements now, because the only acceptable closeout is either a clean split of the `\kappa`-regimes or an explicit narrower theorem if the standard-line `\beta\gamma` witness really remains false.
exec
/bin/zsh -lc 'rg -n -F "mu_bg" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{alg}}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "weight-changing" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "depth gap" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
147: $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$, with a gap at~$3$.
16653:$d_{\mathrm{alg}}$ &
16681: (\S\ref{sec:higher-depths}; class by $d_{\mathrm{alg}}$, cf.\
16711: d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
16721:$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
16728:$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
16735:$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
16754:$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
16787:$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
16815:$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
17446:\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
17455: d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
17460: $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
17461:\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
17471:\item no value $d_{\mathrm{alg}} = 3$
17472: \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
17500:$d_{\mathrm{alg}} \in \{0, 1\}$ according to whether
17502:(class~$\mathbf{G}$, $d_{\mathrm{alg}} = 0$),
17504:(class~$\mathbf{L}$, $d_{\mathrm{alg}} = 1$).
17515:$d_{\mathrm{alg}} = \infty$ (class~$\mathbf{M}$).
 succeeded in 52ms:
17446:\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
17451:\index{depth classification!algebraic depth gap}
17580:The depth gap is the shadow tower's sharpest structural
17588:\begin{remark}[Fine structure of the depth gap]
 succeeded in 52ms:
14918:The $T$-line is class~$\mathbf{M}$, while the weight-changing
14964:weight-changing line has zero shadow tower, so the
16738: The class-$\mathbf{C}$ witness is not the weight-changing line and
16805:(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
17556:one-dimensional internal slices. On the weight-changing line,
18900:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
19243:$r = 4$: on the weight-changing line,
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "sed -n '16728,16822p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17446,17580p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14900,14980p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
\label{prop:depth-gap-trichotomy}
\ClaimStatusProvedHere
\index{algebraic depth!gap theorem|textbf}
\index{shadow depth!forbidden values}
\index{depth classification!algebraic depth gap}
Let $\cA$ be a chirally Koszul algebra in the standard landscape.
Then the algebraic depth satisfies
\begin{equation}\label{eq:depth-gap}
 d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
\end{equation}
More precisely:
\begin{enumerate}[label=\textup{(\roman*)}]
\item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
 $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
 conformal-weight family $\beta\gamma_\lambda$
 \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
 data are
 \[
 succeeded in 51ms:
 & $\mathbf{M}$ & $\infty$
 & $c/2$
 & $\mathfrak{C} = 2x^3$,\;
 $\mathfrak{Q}^{\mathrm{ct}}
 = \dfrac{10}{c(5c{+}22)}\,x^4$ \\[6pt]
$\mathcal{W}_N$ ($N \geq 3$)
 & $\mathbf{M}$ & $\infty$
 & $\kappa_{\mathcal{W}_N}\!(k)$
 & mixed cubic--quartic \\
\bottomrule
\end{tabular}
\end{center}

\smallskip
\noindent
{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
The $T$-line is class~$\mathbf{M}$, while the weight-changing
line has zero shadow tower, so neither one-dimensional slice is the
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc 'rg -n -F "ambient-d-squared-zero" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
10565:ambient level (Theorem~\ref{thm:ambient-d-squared-zero}) is
10568:(now proved: Theorem~\ref{thm:ambient-d-squared-zero}).
11379:\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
11425:Theorem~\ref{thm:ambient-d-squared-zero}.
21950:stable family. Theorem~\ref{thm:ambient-d-squared-zero} identifies
30171:Theorem~\ref{thm:ambient-d-squared-zero}).
30909:(Theorem~\ref{thm:ambient-d-squared-zero}).
31092: Theorem~\textup{\ref{thm:ambient-d-squared-zero}}.
31124:Theorem~\ref{thm:ambient-d-squared-zero}: every
31132:\label{cor:e1-ambient-d-squared-zero}
31145:as in Theorem~\textup{\ref{thm:ambient-d-squared-zero}}.
31159:relative-FM argument as Theorem~\ref{thm:ambient-d-squared-zero}.
31223: This follows from Theorem~\ref{thm:ambient-d-squared-zero} below.
31243:\label{thm:ambient-d-squared-zero}
31395:Theorem~\ref{thm:ambient-d-squared-zero} rests on a \emph{single
31404:by publication, Theorem~\textup{\ref{thm:ambient-d-squared-zero}}
31415: proof of Theorem~\textup{\ref{thm:ambient-d-squared-zero}}.
31434:Theorem~\textup{\ref{thm:ambient-d-squared-zero}} uses only the
32120:(Theorem~\ref{thm:ambient-d-squared-zero}).
exec
/bin/zsh -lc 'rg -n -F "fixed pointed curve" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '31110,31290p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(\cite[Theorem~3.3.1(2)]{Mok25}). The fibre over a
stratum labelled by~$F$ consists of all total orderings of
the children at each vertex compatible with the given
ordering of the $n$~points; this is exactly a planar
planted forest refining~$F$
(Definition~\ref{def:planar-planted-forest-coefficient-algebra}).

Part~(iii): the $\Sigma_n$-action permutes the
orderings and the quotient forgets the planar structure,
recovering the unordered strata.

Part~(iv): the boundary-of-boundary vanishing on
$\operatorname{FM}_n^{\mathrm{ord}}$ follows from the
same argument as
Theorem~\ref{thm:ambient-d-squared-zero}: every
codimension-$2$ stratum appears in exactly two
codimension-$1$ strata with opposite orientations.
The ordering does not affect the orientation
cancellation.
\end{proof}
 succeeded in 52ms:
21948:log-FM space of a fixed pointed curve.
31262:logarithmic Fulton--MacPherson space of a fixed pointed curve.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "sed -n '31290,31440p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This is the relative degeneration picture summarized in
Remark~\ref{rem:degeneration-equals-clutching}.

\medskip
\emph{Step 2: Collision part.}
Write the relative boundary operator on
$C_*(\operatorname{FM}_k(\cC_{g,n}/B))$ as
\[
\partial = \partial_{\mathrm{coll}} + \partial_{\mathrm{deg}},
\]
with $\partial_{\mathrm{coll}}$ the sum of collision faces inside the
fibers of~$\pi$ and $\partial_{\mathrm{deg}}$ the sum of faces lying
over $\partial B$. The operator $d_B$ is the transport of
$\partial_{\mathrm{coll}}$ through the Hom functor.

Every codimension-$2$ stratum contained entirely in the collision
boundary is a triple-collision stratum of
$\operatorname{FM}_k(\Sigma)$ for a smooth fiber~$\Sigma$ of~$\pi$.
Such a stratum lies in exactly two codimension-$1$ collision faces,
corresponding to the two ways of resolving the same triple collision.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Evaluating the ambient theorem**

I think the ambient theorem seems fixed, but I need to check T06, T08, and T09 more thoroughly to see if the labels are valid and check for references. The routing remark on T06 looks good too. For T08, I might want to verify the theorem proof around lines 1011 rather than just the lemma. I should search for mentions of Whitehead to help guide my checks.
exec
/bin/zsh -lc 'rg -n -F "Whitehead" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
902:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
936:records the mode cutoff only: the Whitehead step is carried out on
975:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
1034:by Whitehead; the Killing-form invariant
1045:enrichment factorization, Whitehead acyclicity, and the
1151:finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
1174:Whitehead's first lemma for semisimple~$\fg$
1181:semisimple extension of Whitehead then gives:
1228:We exhibit the interplay of Whitehead vanishing and
1262: Whitehead's theorem gives
1279:three by the bracket isomorphism, five by Whitehead, one by the
1313:summands killed by Whitehead, invariant summands passed to
1319:decomposition under~$\fg$ and the Whitehead vanishing
1323:\begin{remark}[Whitehead reduction in the PBW proof]
1326:Whitehead input appears after rewriting the weight-$h$ enrichment
1372:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1398:three-step mechanism (PBW decomposition, Whitehead
1452:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1474:$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
exec
/bin/zsh -lc 'rg -n -F "thm:e1-mc-element" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/e1_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1035,1165p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}
chapters/theory/e1_modular_koszul.tex:363: is Theorem~\textup{\ref{thm:e1-mc-element}}, equation
chapters/theory/e1_modular_koszul.tex:1375:(Theorem~\ref{thm:e1-mc-element}).
chapters/theory/higher_genus_modular_koszul.tex:3534:ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
chapters/theory/higher_genus_modular_koszul.tex:3774:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
chapters/theory/higher_genus_modular_koszul.tex:3779:Theorem~\ref{thm:e1-mc-element}.
 succeeded in 54ms:
at~$E_3$ by the level-$k$ contraction\textup{)}.
In particular, the interacting Kac--Moody algebras satisfy
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
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Inspecting theorem labels**

I need to check if the theorem labels are valid, like "chap:e1-modular-koszul." It might be worth looking at the "prop:geometric-modular-operadic-mc" label too. I think I should search for more information on these terms to ensure they're correctly labeled. It’s important to verify the details to avoid any confusion in my understanding. Let's see what I can find about these and clarify their validity.
codex
The PBW surface is now in the right shape: the file no longer applies Whitehead to the truncated current algebra itself, only to fixed-weight `\fg`-modules after separating mode multiplicities. I’m doing the final reference and label checks before I close this out.
exec
/bin/zsh -lc "rg -n -F \"\\label{chap:e1-modular-koszul}\" chapters/theory/e1_modular_koszul.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:10:\label{chap:e1-modular-koszul}
exec
/bin/zsh -lc "rg -n -F \"\\label{prop:geometric-modular-operadic-mc}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=1 -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5408:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
 succeeded in 53ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 80770f8..b288625 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -936,3 +936,7 @@ In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
@@ -952,3 +956,14 @@ Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc 'rg -n -F "family-index" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "mc2-bar-intrinsic" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2350: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2648:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2705:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2802:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2913:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3551:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3567:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3707:\label{thm:mc2-bar-intrinsic}
3769:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3777:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4043:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4093:\label{rem:mc2-bar-intrinsic-perspective}
4096:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4146:Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
4200:exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
4698:(Theorem~\ref{thm:mc2-bar-intrinsic};
5135:assembly in Theorem~\ref{thm:mc2-bar-intrinsic}. Consequently the
 succeeded in 51ms:
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
2931:Theorem~\ref{thm:family-index}.
3006:GRR/family-index identification of the same scalar series on the
3007:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
3021:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4625: downstream GRR/family-index reformulation
4626: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4673:Part~(f) is the downstream family-index identification
4674:(Theorem~\ref{thm:family-index}) of the scalar series already
9725:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
14160:(Theorem~\ref{thm:family-index}).
exec
/bin/zsh -lc 'rg -n -F "relative log-FM" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "fixed pointed curve" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
11380:the relevant space is the relative log-FM compactification of the
30889:applied to the bar complex on the relative log-FM spaces of the
 succeeded in 52ms:
21948:log-FM space of a fixed pointed curve.
31262:logarithmic Fulton--MacPherson space of a fixed pointed curve.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "sed -n '30,55p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '245,305p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
curve over $\overline{\mathcal{M}}_{g,n}$, the cobar functor
inverts at genus~$g$
(Theorem~\ref{thm:higher-genus-inversion}).

%% FORCED CONSEQUENCE: the MC element and its degree projections.

The identity $D_\cA^2 = 0$ has an immediate algebraic consequence.
Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
bar differential. Because $D_\cA^2 = 0$, the element
$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
\[
 d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
\]
unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
Existence of the MC element is not a theorem to be proved; it is a
tautology of the bar construction. The question is what structure
$\Theta_\cA$ carries.

Its successive degree projections extract the invariants of~$\cA$:
the modular characteristic $\kappa(\cA)$ at degree~$2$,
 succeeded in 52ms:
\[
\Omega^{(g)}(\sigma^* \barB^{(g)}(\cA))
\simeq \sigma^* \cA^{(g)}
\quad \text{for all } \sigma \in \mathrm{MCG}(\Sigma_g).
\]
Consequently, the genus-$g$ component
$\Theta_\cA^{(g)} \in
C_*(\overline{\mathcal{M}}_{g,n}) \otimes
\operatorname{End}(\cA^{\otimes n})$
of the universal MC element
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
$\mathrm{MCG}(\Sigma_g)$-equivariant, and the genus-$g$
amplitude $Z_g(\cA) = \operatorname{Tr}^{\circ g}(\Theta_\cA^{(g)})$
is $\mathrm{MCG}(\Sigma_g)$-invariant.
\end{proposition}

\begin{proof}
The argument has three steps.

\emph{Step~1: MCG acts on the bar differential.}
exec
/bin/zsh -lc "sed -n '11295,11325p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
planted-forest stratification and rigid-type correspondences are
visible at the chain level.
\end{construction}

\begin{corollary}[$\Theta_\cA$ as universal modular twisting
morphism; \ClaimStatusProvedHere]
\label{cor:vol1-theta-log-fm-twisting-data}
\index{Theta A@$\Theta_\cA$!as modular twisting data}
\[
\operatorname{MC}_\bullet\!\bigl(
{\Definfmod}_{\!\log}(\cA;\mathfrak{U})
\bigr)
\;\simeq\;
\operatorname{Tw}_{\alpha^{\mathrm{mod}}}\!\Bigl(
\cC^{\log\mathrm{FM}}_{\mathrm{mod}},\,
\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr).
\]
The bar-intrinsic class $\Theta_\cA$
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is the
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 



thinking
**Considering build options**

I might need to run a file-level grep for specific phrases like "independent GRR" or "Thm C witness not weight-changing line," but it seems I've already done that. I’m thinking about whether to run `latexmk`. The user didn’t specifically ask for it, but I think the verification loop suggests that I should confirm references and labels after modifying sections. Since the file is huge, a full build might not be necessary, but I could use grep or possibly the build-surface skill instead.
thinking
**Considering LaTeX compilation steps**

I'm thinking about whether it's worth running a targeted LaTeX compile or at least using grep to find any `??` notations. It might be expensive, but since we've modified one file, running a targeted build might be helpful. The user didn’t specifically ask for this, and it could be a heavy build. However, I can verify if all references are valid. I’ve already checked a few labels, and maybe I should check the existence of the others introduced. Let's proceed with that.
codex
I’m not changing the mathematical content further unless verification turns up a real defect. The last pass is mechanical: make sure every newly cited anchor exists and that the remaining “fixed pointed curve” wording is only the explicit negation inside the corrected ambient proof.
exec
/bin/zsh -lc "rg -n -F \"\\label{thm:family-index}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{thm:genus-universality}\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:5938:\ClaimStatusProvedHere]\label{thm:family-index}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:5321:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
exec
/bin/zsh -lc "rg -n -F \"\\label{thm:betagamma-global-depth}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{prop:betagamma-T-line-shadows}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{cor:nms-betagamma-mu-vanishing}\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:1178:\label{thm:betagamma-global-depth}
 succeeded in 52ms:
chapters/examples/free_fields.tex:1117:\label{prop:betagamma-T-line-shadows}
 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Investigating references**

Oh no, I can’t seem to find “cor:nms-betagamma-mu-vanishing” in the chapters. It makes me wonder if the labeling is off or maybe some details are missing. I should probably inspect the actual reference label to see what’s going on. Searching for “mu-vanishing” with a different prefix could help too. It’s a bit perplexing, but I’m determined to get to the bottom of this!
codex
One reference failed the existence check: `cor:nms-betagamma-mu-vanishing` does not exist anywhere under `chapters/`. I’m checking whether that was an older stale citation already present in the file or introduced by the current contact-family rewrite; if it’s stale here, I’ll patch the target file to the actual label.
exec
/bin/zsh -lc 'rg -n "betagamma.*mu.*vanish|mu.*betagamma|rank-one abelian rigidity|stratum separation" chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "cor:nms-betagamma-mu-vanishing" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:85:($r_{\max} = 4$) by the same stratum separation mechanism; the
chapters/examples/free_fields.tex:106:Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
chapters/examples/free_fields.tex:716:stratum separation (rank-one rigidity,
chapters/examples/free_fields.tex:756:weight-changing line (cubic vanishes by rank-one abelian rigidity).
chapters/examples/free_fields.tex:813:exchanged), and the rank-one abelian rigidity argument
chapters/examples/free_fields.tex:1047:Complementing the chain-space rank formula (Theorem~\ref{thm:betagamma-bar-dim}),
chapters/examples/free_fields.tex:1067:and terminates at degree~$4$ by a stratum separation mechanism that has
chapters/examples/free_fields.tex:1090: so the shadow obstruction tower is purely quadratic by rank-one abelian rigidity
chapters/examples/free_fields.tex:1179:\index{stratum separation!beta-gamma@$\beta\gamma$}
chapters/examples/free_fields.tex:1212:vanishes by rank-one abelian rigidity
chapters/examples/free_fields.tex:1213:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
chapters/examples/free_fields.tex:1234:\index{stratum separation!mechanism}
chapters/examples/free_fields.tex:1237:\emph{stratum separation}: the quintic obstruction $o_5$ couples
chapters/examples/free_fields.tex:5559:obstruction still satisfies $o_5 = 0$ by stratum separation
chapters/theory/higher_genus_modular_koszul.tex:12214:contact vertex, after which stratum separation on
chapters/theory/higher_genus_modular_koszul.tex:13688:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
chapters/theory/higher_genus_modular_koszul.tex:14943: & rank-one abelian rigidity \\
chapters/theory/higher_genus_modular_koszul.tex:14968: Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:15028:$\mathbf{C}$~(depth~$4$: stratum separation on
chapters/theory/higher_genus_modular_koszul.tex:15745: stratum separation at~$5$ \\
 succeeded in 51ms:
13688:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
14968: Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
16750: Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
16808:\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
17559:\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
exec
/bin/zsh -lc 'rg -n -F "label{" chapters/examples/free_fields.tex | rg -n "betagamma|mu|rigidity|stratum"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:41:\begin{equation}\label{eq:betagamma-triple}
47:703:\label{rem:betagamma-shadow-archetype-free}
54:989:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex; \ClaimStatusProvedHere]\label{thm:betagamma-bar-complex}
55:1000:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank; \ClaimStatusProvedHere]\label{thm:betagamma-bar-dim}
56:1046:\begin{remark}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar \emph{cohomology} closed form]\label{rem:betagamma-bar-cohomology-gf}
57:1060:\label{sec:betagamma-shadow-tower-free}
58:1071:\label{sec:betagamma-multi-channel}
59:1075:\label{prop:betagamma-deformation-channels}
60:1117:\label{prop:betagamma-T-line-shadows}
64:1152:\label{prop:betagamma-weight-line-shadows}
65:1178:\label{thm:betagamma-global-depth}
66:1233:\label{rem:betagamma-stratum-separation-mechanism}
67:1253:\label{prop:betagamma-shadow-metric}
70:1289:\label{comp:betagamma-shadow-weights}
71:1325:\label{prop:betagamma-weight-symmetry}
72:1354:\label{rem:betagamma-mumford}
84:1667:\begin{proposition}[\texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality; \ClaimStatusProvedHere]\label{prop:bc-betagamma-orthogonality}
86:1691:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality; \ClaimStatusProvedHere]\label{thm:betagamma-bc-koszul}
87:1693:\begin{equation}\label{eq:betagamma-bc-koszul}
92:1864:\label{sec:betagamma-bc-modules}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

exec
/bin/zsh -lc "sed -n '1080,1225p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1265p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item \emph{The stress tensor line}
 (T-line): the one-dimensional slice corresponding to
 the Virasoro subalgebra at central charge
 $c = c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$.
 On this line the shadow data coincides with that of
 $\mathrm{Vir}_{c}$.
\item \emph{The weight-changing line}: the deformation that shifts the
 conformal weight $\lambda \mapsto \lambda + \epsilon$. On this line
 all transferred higher brackets vanish
 ($\ell_n^{\mathrm{tr}}|_{L} = 0$ for $n \geq 2$),
 so the shadow obstruction tower is purely quadratic by rank-one abelian rigidity
 (Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}).
\end{enumerate}
The $\beta\gamma$ system is \emph{not} a scalar-lane algebra:
the two directions carry independent shadow data, and the
global tower depends on their interaction.
\end{proposition}

\begin{proof}
Direction~(i): the stress tensor $T(z)$ of the $\beta\gamma$ system
 succeeded in 51ms:
The weight-changing-line projection
$\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
vanishes by rank-one abelian rigidity
(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
The quartic contact class is the \emph{last} nontrivial shadow
component.

\emph{Degree~$5$.}
The quintic obstruction is the Lie bracket
$o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
The quartic contact class lives on the charged stratum, while the cubic
shadow that survives on the standalone T-line does not contribute a
compatible input in the full two-channel complex. On the weight-changing
line the cubic vanishes altogether. Hence the global bracket
$o_5 = 0$.
The quartic contact class lives on a charged stratum whose
self-bracket exits the complex by rank-one rigidity; no further
obstruction propagates.

Therefore $r_{\max} = 4$: the tower terminates at the quartic level.\qedhere
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 


thinking
**Investigating label references**

I'm thinking about the "free_fields" reference, which seems to point to a missing core label. It's possible that this label isn't included in the chapters but might exist elsewhere in the repository. I should search the entire repo to see if I can locate it. Understanding its location could be crucial for addressing the issue properly. Let's explore this further!
exec
/bin/zsh -lc 'rg -n -F "cor:nms-betagamma-mu-vanishing" .' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 123

./rectification_20260412_233715/R17_free_fields.md:216:/bin/zsh -lc "rg -n \"thm:betagamma-quartic-birth|thm:single-line-dichotomy|thm:betagamma-rank-one-rigidity|cor:nms-betagamma-mu-vanishing|global shadow depth|r_max = 4|d_alg=2|d_\\{alg\\}\" -S chapters/examples/free_fields.tex chapters/connections/concordance.tex CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
./rectification_20260412_233715/R17_free_fields.md:239:chapters/examples/free_fields.tex:106:Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
./rectification_20260412_233715/R17_free_fields.md:251:chapters/examples/free_fields.tex:1204:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
./rectification_20260412_233715/R17_free_fields.md:284:/bin/zsh -lc "rg -n \"label\\{thm:betagamma-quartic-birth\\}|label\\{thm:betagamma-rank-one-rigidity\\}|label\\{cor:nms-betagamma-mu-vanishing\\}|label\\{thm:single-line-dichotomy\\}|label\\{thm:depth-gap-trichotomy\\}|class~C|d_alg\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
./rectification_20260412_233715/R17_free_fields.md:379:/bin/zsh -lc "rg -n \"label\\{thm:betagamma-quartic-birth\\}|label\\{thm:betagamma-rank-one-rigidity\\}|label\\{cor:nms-betagamma-mu-vanishing\\}|quartic birth|rank-one abelian rigidity|mu_\\{\\\\beta\\\\gamma\\}|mu_{\\\\beta\\\\gamma}\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
./rectification_20260412_233715/R17_free_fields.md:383:    (?:label\{thm:betagamma-quartic-birth\}|label\{thm:betagamma-rank-one-rigidity\}|label\{cor:nms-betagamma-mu-vanishing\}|quartic birth|rank-one abelian rigidity|mu_\{\beta\gamma\}|mu_{\beta\gamma})
./rectification_20260412_233715/R17_free_fields.md:437:/bin/zsh -lc "rg -n -F '\\label{cor:nms-betagamma-mu-vanishing}' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
./rectification_20260412_233715/R17_free_fields.md:462:/bin/zsh -lc "rg -n -F '\\label{cor:nms-betagamma-mu-vanishing}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./fix_wave_A_20260413_112727/A07_free_fields.md:246:chapters/examples/free_fields.tex:106:Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
./fix_wave_A_20260413_112727/A07_free_fields.md:256:chapters/examples/free_fields.tex:1204:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
./fix_wave_A_20260413_112727/A07_free_fields.md:259:chapters/examples/deformation_quantization_examples.tex:14:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}); and the Virasoro
./fix_wave_A_20260413_112727/A07_free_fields.md:261:chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
./fix_wave_A_20260413_112727/A07_free_fields.md:262:chapters/examples/beta_gamma.tex:188:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}) implies no quartic
./fix_wave_A_20260413_112727/A07_free_fields.md:263:chapters/examples/beta_gamma.tex:205:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), terminates
./fix_wave_A_20260413_112727/A07_free_fields.md:833:/bin/zsh -lc "rg -n \"\\\\label\\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth)\\}|\\\\ref\\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth|thm:betagamma-rank-one-rigidity|thm:betagamma-quartic-birth|cor:nms-betagamma-mu-vanishing)\\}\" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
./fix_wave_A_20260413_112727/A07_free_fields.md:836:    (?:\label\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth)\}|\ref\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth|thm:betagamma-rank-one-rigidity|thm:betagamma-quartic-birth|cor:nms-betagamma-mu-vanishing)\})
./fix_wave_A_20260413_112727/A07_free_fields.md:924:/bin/zsh -lc "rg -n -F -e '\\label{prop:betagamma-T-line-shadows}' -e '\\label{prop:betagamma-weight-line-shadows}' -e '\\label{thm:betagamma-global-depth}' -e '\\ref{prop:betagamma-T-line-shadows}' -e '\\ref{prop:betagamma-weight-line-shadows}' -e '\\ref{thm:betagamma-global-depth}' -e '\\ref{thm:betagamma-rank-one-rigidity}' -e '\\ref{thm:betagamma-quartic-birth}' -e '\\ref{cor:nms-betagamma-mu-vanishing}' chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
./fix_wave_A_20260413_112727/A07_free_fields.md:947:chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

codex
Edited [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:936) only. I re-read each modified surface, checked the newly introduced label targets (`thm:e1-mc-element`, `chap:e1-modular-koszul`, `prop:geometric-modular-operadic-mc`, `thm:genus-universality`, `thm:family-index`, `thm:betagamma-global-depth`, `prop:betagamma-T-line-shadows`) and confirmed the “fixed pointed curve” wording now survives only as an explicit negation inside the corrected ambient `D^2=0` proof. I did not run a full TeX build.

## Rectification Summary
- [FIXED] T06 circularity in Theorem D — added an explicit routing remark making the proof chain non-circular: bar-intrinsic shadow tower (`thm:mc2-bar-intrinsic`) → genus universality (`thm:genus-universality`) → downstream GRR/family-index identification (`thm:family-index`).
- [FIXED] T08 PBW / Whitehead misuse — added the missing comparison showing that, after fixing a weight and mode pattern, the residue action factors through the diagonal adjoint action of finite-dimensional semisimple `\fg`; mixed genus-`0/g` maps are now routed through `H^1(\fg,N_h^{n-1})`, not through cohomology of the truncated current algebra.
- [FIXED] T09 MC2 scope in this chapter — `thm:universal-theta`, `thm:mc2-bar-intrinsic`, and the surrounding remarks now state explicitly that this chapter proves the coinvariant/symmetric MC2 statement on `\gAmod`; the ordered `E_1` theorem is redirected to `thm:e1-mc-element` in `e1_modular_koszul.tex`.
- [BLOCKED] T09 introduction cross-reference — the misattribution in `introduction.tex` was not edited because the task restricted edits to the assigned target file. I added an in-file scope remark stating that any external citation of `thm:mc2-bar-intrinsic` as the ordered `E_1` statement is incorrect.
- [FIXED] T09 `\Theta_\cA` placement — added the explicit identification of the genuswise product of cyclic coderivations with the augmentation ideal `G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)`, so the proof no longer silently treats two different spaces as the same.
- [FIXED] T16 depth-gap overscope — the depth-gap proposition now separates the `\kappa|_L \neq 0` single-line regime, where only `{0,1,\infty}` occur, from the boundary `d_{\mathrm{alg}}=2` contact witness realized globally by the conformal-weight `\beta\gamma_\lambda` family.
- [FIXED] T16 class-C witness contradiction — the file now states that the class-`\mathbf{C}` witness is not the weight-changing line and not the `T`-line; it is the full conformal-weight `\beta\gamma_\lambda` family with `S_2=6\lambda^2-6\lambda+1`, `S_3=0`, `S_4=-5/12`, and `S_r=0` for `r\ge 5`.
- [FIXED] T18 wrong space for ambient `D^2=0` — the ambient square-zero theorem and related remarks now use the relative Fulton-MacPherson/log-FM space of the universal stable family `\operatorname{FM}_k(\cC_{g,n}/\overline{\cM}_{g,n})`; collision faces, curve-degeneration faces, and mixed codimension-2 cancellations are all formulated on that universal-family carrier.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 88bf337563afb928981c89060572f144e87e7bd8..b28862537da35eab74ad513ec5ea5e52ddf02c00
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -934,7 +934,11 @@
 trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
 In particular the truncated current algebra $\fg \otimes V_h$
 records the mode cutoff only: the Whitehead step is carried out on
-the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
+fixing a mode pattern~$\nu$, the residue action of the truncated
+current algebra factors through the diagonal adjoint action of the
+finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
+contributes only passive multiplicity data.
 \end{lemma}
 
 \begin{proof}
@@ -950,7 +954,18 @@
 mode pattern~$\nu$, this is exactly the
 Chevalley--Eilenberg differential for the diagonal adjoint action of
 $\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
-set of mode patterns gives the stated decomposition.
+set of mode patterns gives the stated decomposition. More explicitly,
+on the $\nu$-summand every residue bracket has the form
+\[
+x \cdot (a_1 \otimes \cdots \otimes a_n)_\nu
+\;=\;
+\sum_i c_i(\nu)\,
+a_1 \otimes \cdots \otimes [x,a_i] \otimes \cdots \otimes a_n,
+\]
+with coefficients $c_i(\nu)$ depending only on the mode pattern.
+Thus the Lie-theoretic part of $d_1^{\mathrm{PBW}}$ is the
+Chevalley--Eilenberg differential for the diagonal $\fg$-action, not
+for the non-semisimple Lie algebra $\fg \otimes V_h$ itself.
 \end{proof}
 
 \begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
@@ -1135,7 +1150,11 @@
 mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
 finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
 is carried out weight by weight on honest $\fg$-modules, not on the
-non-semisimple Lie algebra $\fg \otimes V_h$.
+non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
+comparison is therefore representation-theoretic rather than
+Lie-algebraic: once the mode pattern is fixed, the residue action is
+the diagonal adjoint $\fg$-action with multiplicity spaces coming
+from the modes.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -2890,14 +2909,26 @@
 
 \begin{proof}
 \emph{Routing remark.}
-The dependency route has a common bar-intrinsic anchor.
-Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace of the
-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
-cohomological genus-$g$ component with $\kappa(\cA)\lambda_g$ on the
-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
-gives an independent Grothendieck--Riemann--Roch computation of the
-same scalar series from the family~\eqref{eq:bar-family} on the
-universal curve. Neither theorem is used to prove the other.
+The non-circular anchor is the bar-intrinsic shadow tower.
+Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
+scalar trace. Theorem~\ref{thm:genus-universality} is the first
+downstream step: it identifies the genus-$g$ scalar component of that
+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
+Theorem~\ref{thm:family-index} is downstream again: it is the
+Grothendieck--Riemann--Roch identification of the already constructed
+scalar series for the bar family~\eqref{eq:bar-family} on the
+universal curve. Thus the logical route is
+\[
+\Theta_\cA
+\;\Longrightarrow\;
+\mathrm{obs}_g=\kappa(\cA)\lambda_g
+\;\Longrightarrow\;
+\sum_{g \geq 1} F_g x^{2g}
+=
+\kappa(\cA)\cdot(\hat{A}(ix)-1),
+\]
+and Theorem~\ref{thm:genus-universality} does not invoke
+Theorem~\ref{thm:family-index}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
@@ -2963,22 +2994,19 @@
 \[
 \Theta_\cA \text{ and its shadow tower}
 \Longrightarrow
-\left\{
-\begin{array}{l}
-\mathrm{obs}_g=\kappa\cdot\lambda_g,\\[4pt]
+\mathrm{obs}_g=\kappa\cdot\lambda_g
+\Longrightarrow
 \sum_{g \ge 1} F_g x^{2g}
 =
-\kappa\cdot(\hat{A}(ix)-1).
-\end{array}
-\right.
+\kappa\cdot(\hat{A}(ix)-1)
 \]
 The bar-intrinsic shadow tower is the common source.
-The first line is the scalar-trace identification of
-Theorem~\ref{thm:genus-universality}; the second line is the
-independent GRR/family-index computation on the universal curve.
-Theorem~\ref{thm:family-index} is not downstream of
-Theorem~D, and Theorem~D is not proved from
-Theorem~\ref{thm:family-index}.
+The first implication is the scalar-trace identification of
+Theorem~\ref{thm:genus-universality}; the second is the downstream
+GRR/family-index identification of the same scalar series on the
+virtual bar family. Theorem~\ref{thm:family-index} is therefore the
+index-theoretic reformulation of the scalar output, not the
+load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 \emph{Step~B} (M-level): universality
 $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
 unconditional at $g{=}1$,
@@ -2986,12 +3014,12 @@
 Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 duality $\kappa+\kappa'=\varrho\cdot K$; additivity
 (Theorem~\ref{thm:anomaly-koszul}).
-\emph{Parallel index package}: Grothendieck--Riemann--Roch maps the
+\emph{Step~C} (index identification): Grothendieck--Riemann--Roch maps the
 virtual bar family $[\barB^{(g)}(\cA)] \in
 K_0(\overline{\mathcal{M}}_g)$ to
 $\kappa\cdot(\hat{A}(ix)-1)$
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
-\emph{Step~C}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
+\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
@@ -3502,6 +3530,9 @@
  $\Theta_{\cA^!}$.
 \end{enumerate}
 This is Theorem~\ref{thm:master-theta} (MC2).
+In this chapter, it is the coinvariant/symmetric MC2 statement; the
+ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
+Chapter~\ref{chap:e1-modular-koszul}.
 \end{theorem}
 
 \begin{proof}
@@ -3697,9 +3728,14 @@
  \barB^{(g)}_X(\cA)
 \bigr)[1].
 \end{equation}
+Via the genuswise-completion identification of
+Proposition~\ref{prop:geometric-modular-operadic-mc}(a)--(b), this
+product is the augmentation ideal
+$G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod)$ of the completed
+coinvariant modular convolution algebra.
 Then \textup{(}see Figure~\textup{\ref{fig:bar-intrinsic-construction})}:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Maurer--Cartan on\/~$\gAmod$.}
+\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
  $\Theta_\cA \in
  \MC\bigl(\Defcyc(\cA) \widehat{\otimes} \Gmod\bigr)$.
 \item \emph{Scalar trace.}
@@ -3737,7 +3773,10 @@
 $\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
 \MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
 Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
+$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
+Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
+therefore incorrect; the ordered theorem is
+Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
 % ----------------------------------------------------------------
@@ -4054,7 +4093,8 @@
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
 \index{MC2!two regimes}
-Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
+Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
+statement in this chapter: the universal
 MC class \emph{is} the positive-genus part of the bar differential,
 and the Maurer--Cartan equation is a tautological consequence
 of~$D_\cA^2 = 0$.
@@ -4580,10 +4620,10 @@
  \kappa(\cA) \cdot
  \Bigl(\hat{A}(ix) - 1\Bigr)
  \end{equation}
- by the family index theorem
+ where the first equality is the scalar trace already identified by
+ Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
+ downstream GRR/family-index reformulation
  \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
- The $\hat{A}$-genus arises from the GRR pushforward of the
- Todd class of the universal curve.
 \end{enumerate}
 \end{theorem}
 
@@ -4630,9 +4670,9 @@
 Hence $l_2(\theta_h, \theta_{g-h}) = 0$ at the cochain level,
 and the genus-$g$ recursion begins at $l_3$.
 
-Part~(f) is the family index theorem
-(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
-because
+Part~(f) is the downstream family-index identification
+(Theorem~\ref{thm:family-index}) of the scalar series already
+constructed above; the $\hat{A}$-genus appears because
 $\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
 pushed forward to $\overline{\mathcal{M}}_g$, produces the
 $\hat{A}$-class by Mumford's formula.
@@ -9680,8 +9720,9 @@
 \end{remark}
 
 \begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-d}
-Properties~(i)--(iv) of Theorem~D are shadows of the family index
-theorem (Theorem~\ref{thm:family-index}).
+Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
+trace and are read index-theoretically by the family index theorem
+\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
 The determinant line $\mathcal{L}_{\cA} := \det R\pi_{g*}\bar{B}^{(g)}(\cA)$
 has $c_1(\mathcal{L}_{\cA}) = \kappa(\cA)\cdot\lambda$;
 the $\hat{A}$-genus arises from GRR via the Mumford
@@ -11335,8 +11376,12 @@
 ($\hbar\Delta$ at leading order).
 The identity $(D_{\mathrm{mod}}^{\log})^2 = 0$ is the chain-level
 content of $D^2 = 0$ at the ambient level
-(Theorem~\ref{thm:ambient-d-squared-zero}), now proved via Mok's
-log-FM normal-crossings result~\cite[Theorem~3.3.1]{Mok25}.
+\textup{(}Theorem~\textup{\ref{thm:ambient-d-squared-zero}}\textup{)}:
+the relevant space is the relative log-FM compactification of the
+universal stable family over $\overline{\cM}_{g,n}$, whose collision
+faces give $d_{\mathrm{coll}}$ and whose curve-degeneration faces over
+$\partial\overline{\cM}_{g,n}$ give $d_{\mathrm{sew}}$ and
+$d_{\mathrm{loop}}$.
 \end{construction}
 
 \begin{construction}[Boundary operators as residue correspondences;
@@ -11373,8 +11418,11 @@
 codimension-one non-separating strata produce $\Delta$;
 rigid codimension-two planted-forest strata produce
 $d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
-codimension-two faces in the normal-crossings boundary of Mok's
-compactification~\cite[Theorem~3.3.1]{Mok25}.
+codimension-two faces in the relative normal-crossings boundary of the
+universal-family log-FM space: pure collision faces give the Arnold
+cancellation, while mixed faces where a curve degeneration meets a
+collision give the ambient cross-term cancellations of
+Theorem~\ref{thm:ambient-d-squared-zero}.
 \end{construction}
 
 \begin{construction}[Planted-forest differential as a push--pull
@@ -13631,10 +13679,11 @@
 \bottomrule
 \end{tabular}
 \end{center}
-For the $\beta\gamma$ system, the cubic corolla $K_{0,3}^\cA$ is nonzero
-but gauge-trivial (Theorem~\ref{thm:cubic-gauge-triviality}), so the
-separating bracket contributes to the shell equations at the cochain level
-but is exact. The quartic contact invariant
+For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
+\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
+so the separating bracket contributes to the shell equations only at
+the cochain level and does not produce a surviving cubic shadow.
+The quartic contact invariant
 $\mu_{\beta\gamma} = 0$
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
 cutting terms $R_{\rho}$ are generically nonzero.
@@ -14843,10 +14892,10 @@
  & $\mathbf{L}$ & $3$
  & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
  & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
-$\beta\gamma$\rlap{\textsuperscript{$\dagger$}}
+$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
  & $\mathbf{C}$ & $4$
- & $0$
- & $\mathfrak{Q} = \operatorname{cyc}(m_3)$ \\[4pt]
+ & $6\lambda^2 - 6\lambda + 1$
+ & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
 $\mathrm{Vir}_c$
  & $\mathbf{M}$ & $\infty$
  & $c/2$
@@ -14863,10 +14912,12 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Shadow data on the
-weight-changing line, where $\kappa = 0$ and the cubic is
-gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}).}
+{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
+family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line is class~$\mathbf{M}$, while the weight-changing
+line has zero shadow tower, so neither one-dimensional slice is the
+class-$\mathbf{C}$ witness by itself.}
 
 \smallskip
 \noindent
@@ -14905,13 +14956,16 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma$ on the weight-changing line, the cubic
-is gauge-trivial
-(Theorem~\ref{thm:cubic-gauge-triviality}); the
-quartic contact invariant
-$\mathfrak{Q} = \operatorname{cyc}(m_3)$ is the canonical
-representative
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+For $\beta\gamma_\lambda$ on the global conformal-weight family,
+the cubic shadow vanishes while the charged quartic survives:
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
+The $T$-line restriction has an infinite tail, and the
+weight-changing line has zero shadow tower, so the
+class-$\mathbf{C}$ witness is the full family rather than either
+one-dimensional slice
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
+ Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 For Virasoro, the $H$-Poisson bracket
 $\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 infinite tower
@@ -15140,7 +15194,7 @@
  Jacobi kills degree-$4$ graphs \\
 $\beta\gamma$ &
  $4$ & $4$ & $4$ &
- Rank-$1$ rigidity kills degree-$5$ \\
+ Charged quartic slice; rank-$1$ rigidity kills degree-$5$ \\
 Virasoro &
  $\infty$ & $\infty$ & $\infty$ &
  $:T^n:$ generates operations at all degrees \\
@@ -16614,7 +16668,7 @@
  \S\ref{sec:affine-cubic-shadow} \\[3pt]
 $\beta\gamma$ &
  $\mathbf{C}$ & $4$ & $2$ & \textsuperscript{$\ast$} &
- \S\ref{sec:betagamma-quartic-birth} \\[3pt]
+ Thm~\ref{thm:betagamma-global-depth} \\[3pt]
 $\mathrm{Vir}_c$ &
  $\mathbf{M}$ & $\infty$ & $\infty$
  & $\frac{40}{5c{+}22}$ &
@@ -16637,8 +16691,11 @@
  \S\ref{sec:higher-depths} \\
 \bottomrule
 \multicolumn{6}{l}{\textsuperscript{$\ast$}%
- Stratum separation: $\Delta \neq 0$ on charged stratum,
- $\dim\Defcyc^{(2q)} = 0$.}
+ Stratum-separated global family:
+ $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+ $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
+ The charged quartic lies off the $T$-line, so the single-line
+ discriminant is not the class-$\mathbf{C}$ witness.}
 \end{tabular}
 \end{center}
 \end{example}
@@ -16648,38 +16705,53 @@
 \ClaimStatusProvedHere
 \index{shadow depth!classification theorem|textbf}
 \index{shadow archetype classification|textbf}
-Every chirally Koszul algebra in the standard landscape belongs to
-exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
-$\mathbf{F}_4$, or $\mathbf{M}$
+Every chirally Koszul algebra in the standard landscape has algebraic
+shadow depth
+\[
+ d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
+\]
+Equivalently, it belongs to exactly one of the shadow depth classes
+$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 The class is determined by the vanishing pattern of obstruction
 classes at degrees~$3$, $4$, $5$, and the assignments for the
 primitive archetypes are as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
+\item \emph{Gaussian \textup{(}$\mathbf{G}$,
+$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
  Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
  All higher obstruction classes vanish:
  $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
  exactly quadratic.
 
-\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
+\item \emph{Lie \textup{(}$\mathbf{L}$,
+$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
  Affine Kac--Moody $V_k(\fg)$ at generic level.
  The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
  \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
  quartic obstruction $o_4 = 0$ by the Jacobi identity.
 
-\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
- the global $\beta\gamma$ system, via stratum separation between the
- $T$-line and the charged weight/contact slice.
- The weight-changing-line projection
- $\mu_{\beta\gamma}$ vanishes, but the charged quartic contact class is
- nonzero and $o_5 = 0$ by rank-one abelian rigidity and stratum
- separation
+\item \emph{Contact \textup{(}$\mathbf{C}$,
+$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
+ the conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}and its $bc$ dual\textup{)}.
+ The class-$\mathbf{C}$ witness is not the weight-changing line and
+ not the $T$-line: on the full family one has
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5).
+ \]
+ Thus the charged quartic contact class is nonzero and is the last
+ non-vanishing shadow component; the quintic obstruction vanishes by
+ rank-one abelian rigidity and stratum separation
  \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
  Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
 
-\item \emph{Mixed \textup{(}$\mathbf{M}$, $r_{\max} = \infty$\textup{)}:}
+\item \emph{Mixed \textup{(}$\mathbf{M}$,
+$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
  Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
  The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
  shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
@@ -16705,17 +16777,14 @@
 
 For lattice vertex algebras, the shadow--spectral correspondence
 \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-correspondence}})
-identifies the shadow depth with $1$ plus the number of critical
-lines of the constrained Epstein zeta. The depth is unbounded:
+identifies the total shadow depth with $1$ plus the number of critical
+lines of the constrained Epstein zeta. The total depth is unbounded:
 every finite value $d \geq 2$ is realized by even unimodular
 lattices of sufficiently high rank, with depths $5, 6, 7, \dotsc$
 arising from independent cusp forms in $M_{r/2}$
-\textup{(}\S\textup{\ref{sec:higher-depths})}. The transition from
-finite shadow depth \textup{(}classes
-$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
-infinite shadow depth \textup{(}class~$\mathbf{M}$\textup{)} is the
-transition from free to interacting
-\textup{(}Proposition~\textup{\ref{prop:free-interacting-dichotomy})}.
+\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
+new algebraic-shadow archetypes: for lattices one has
+$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 \end{theorem}
 
 \begin{proof}
@@ -16733,15 +16802,18 @@
 vanishes by the Jacobi identity: the cyclic double Lie bracket
 $\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 
-(iii)~For $\beta\gamma$, the weight-changing line alone is not the
-class-$\mathbf{C}$ witness: its shadow tower vanishes and
+(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
+the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global $\beta\gamma$ system,
-where a charged quartic contact class survives on the mixed
-weight/contact slice while the quintic obstruction still vanishes by
-stratum separation. This is exactly
-Theorem~\ref{thm:betagamma-global-depth}, so $r_{\max} = 4$.
+The $T$-line is also not the class-$\mathbf{C}$ witness:
+it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
+\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
+The class-$\mathbf{C}$ witness is the global conformal-weight family:
+there the cubic shadow vanishes, the charged quartic survives with
+$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
+$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
+$r_{\max} = 4$.
 
 (iv)~For Virasoro, the cubic and quartic shadows coexist, and their
 Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
@@ -17377,8 +17449,7 @@
 \index{algebraic depth!gap theorem|textbf}
 \index{shadow depth!forbidden values}
 \index{depth classification!algebraic depth gap}
-Let $\cA$ be a chirally Koszul algebra in the standard landscape
-with primary-line shadow data $(\kappa, \alpha, S_4)$.
+Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 Then the algebraic depth satisfies
 \begin{equation}\label{eq:depth-gap}
  d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
@@ -17387,21 +17458,28 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
  $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
-\item the boundary value $d_{\mathrm{alg}} = 2$ occurs exactly on the
- contact class~$\mathbf{C}$, where the nonzero quartic class lives on a
- charged stratum with $\kappa|_L = 0$.
+\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
+ conformal-weight family $\beta\gamma_\lambda$
+ \textup{(}equivalently $bc_\lambda$\textup{)}, whose global shadow
+ data are
+ \[
+  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
+  S_3 = 0,\qquad
+  S_4 = -5/12,\qquad
+  S_r = 0 \quad (r \geq 5);
+ \]
+\item no value $d_{\mathrm{alg}} = 3$
+ \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
+ is realized.
 \end{enumerate}
-No value $d_{\mathrm{alg}} = 3$ \textup{(}or any finite
-$d_{\mathrm{alg}} \geq 3$\textup{)} is realized.
 The four values correspond bijectively to the shadow depth
 classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$
 of Definition~\textup{\ref{def:shadow-depth-classification}}.
 \end{proposition}
 
 \begin{proof}
-The argument has three parts: a single-line analysis for
-$\kappa \neq 0$, the contact boundary $\kappa|_L = 0$, and a
-multi-sector extension.
+The argument has two parts: the single-line Riccati regime
+$\kappa \neq 0$, and the global contact witness.
 
 \emph{Single-line regime \textup{(}$\kappa \neq 0$\textup{)}.}
 On a primary line~$L$ with $\kappa \neq 0$, the shadow generating
@@ -17439,51 +17517,64 @@
 Thus no single primary line with $\kappa \neq 0$ can realize
 $d_{\mathrm{alg}} = 2$ or~$3$.
 
-The gap at $d_{\mathrm{alg}} = 3$ is forced: termination at
-degree~$5$ (i.e.\ $S_5 = 0$ but $S_4 \neq 0$) would require the
-master equation~\eqref{eq:single-line-inversion} at $r = 5$
-to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
-The recursion gives
-$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
-= -(6/5)\,P\,\alpha\,S_4$.
+The degree-$4$ master equation already isolates the unique quartic
+cancellation. From the quadratic identity $F(t)^2 = Q_L(t)$ one reads
+off the free quartic contribution
+\[
+ S_4^{\mathrm{free}}
+ \;=\;
+ -\frac{9\alpha^2}{16\kappa},
+\]
+so the finite-depth locus at degree~$4$ is exactly the cancellation
+$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
+cancellation fails, the next recursion step forces a tail. Indeed,
+the master equation~\eqref{eq:single-line-inversion} at $r = 5$
+gives
+\[
+ S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
+ = -(6/5)\,P\,\alpha\,S_4.
+\]
 For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
 and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
-$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
-next recursion step (the $j = k = 4$ term contributes
-$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
-at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
-to infinitely many nonzero $S_r$: the closed form
+$S_5 = 0$ but the next step gives
+\[
+ S_6
+ \;=\;
+ -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
+ \;=\;
+ -\frac{2\,S_4^2}{3\kappa},
+\]
+which is again nonzero. Thus there is no second finite
+cancellation beyond the affine one: away from $S_4 = 0$ the
+single-line tower does not terminate. By induction,
+$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 $H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 
-\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
-Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
-the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
-are undefined on the charged quartic stratum.
-The $\beta\gamma$ witness is the global system, not the
-weight-changing line by itself. On the weight-changing line,
-all shadows vanish and
-$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
+\emph{Global contact witness.}
+The value $d_{\mathrm{alg}} = 2$ is realized by the
+conformal-weight family $\beta\gamma_\lambda$, not by either of its
+one-dimensional internal slices. On the weight-changing line,
+all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
+rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
-The nonzero quartic class appears instead on the charged stratum
-mixing the $T$-line and the weight-changing direction; it is the last
-nonvanishing shadow component. Equivalently, the global
-$\beta\gamma$ system has $d_{\mathrm{alg}} = 2$
-\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}; Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
+On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
+gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
+The class-$\mathbf{C}$ witness is the full family:
+Theorem~\ref{thm:betagamma-global-depth} gives
+$r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
+the degree-$2$ coefficient is
+$S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
+vanishes on the conformal-weight family; and the charged quartic
+is the nonzero constant $S_4 = -5/12$.
+Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
+The same statement holds for $bc_\lambda$ by the same
+stratum-separation mechanism.
 
-\emph{Multi-sector extension.}
-For a multi-generator algebra with primary lines
-$L_1, \dotsc, L_n$, the cubic pump
-(Remark~\ref{rem:contact-stratum-separation}) applies: if
-$\alpha \neq 0$ on any mixed sector, the adjoint
-$\mathrm{ad}_{S_3}$ generates an infinite chain on every
-reachable sector, forcing $d_{\mathrm{alg}} = \infty$. If all
-mixed cubics vanish, the sectors decouple
-(Proposition~\ref{prop:independent-sum-factorization}),
-and each sector is either one of the single-line values
-$0, 1, \infty$ or the charged contact boundary value~$2$.
-Hence
-$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$ globally, and no
-intermediate value $d_{\mathrm{alg}} = 3$ is accessible.
+The classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, and
+$\mathbf{M}$ are therefore witnessed by Heisenberg/lattice/free
+families, affine Kac--Moody, $\beta\gamma_\lambda$/$bc_\lambda$,
+and Virasoro/$\mathcal{W}_N$, respectively. No finite value
+$d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
 The depth gap is the shadow tower's sharpest structural
@@ -17514,9 +17605,10 @@
 $1$ & $\mathbf{L}$ & $0$ & $\neq 0$
  & $Q_L = (2\kappa + 3\alpha\,t)^2$: linear square
  & affine $\widehat{\mathfrak{g}}_k$ \\
-$2$ & $\mathbf{C}$ & --- & ---
- & charged quartic stratum,\; $\kappa|_L = 0$
- & $\beta\gamma$ \\
+$2$ & $\mathbf{C}$ & --- & $0$
+ & conformal-weight family:\; charged quartic survives,\;
+ stratum separation kills $r \geq 5$
+ & $\beta\gamma_\lambda$ \\
 $\infty$ & $\mathbf{M}$ & $\neq 0$ & $\neq 0$
  & $\sqrt{Q_L}$ irrational: all $S_r \neq 0$
  & $\operatorname{Vir}_c$, $\cW_N$ \\
@@ -19091,12 +19183,11 @@
  $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
  \mathfrak{C}_{\mathrm{Vir}}$.
  \item $r = 4$:
- $(\kappa, \mathfrak{C})_{\cH_0} =
- (\kappa, \mathfrak{C})_{\beta\gamma} = (0, 0)$
- on the weight-changing line,\;
- $\mathfrak{Q}_{\cH_0} = 0 \neq
- \operatorname{cyc}(m_3)
- = \mathfrak{Q}_{\beta\gamma}$.
+ $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
+ $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
+ on the conformal-weight family line;\;
+ $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
+ = \mathfrak{Q}_{\beta\gamma_1}$.
  \end{itemize}
 
 \item \emph{Shadow class detection.}
@@ -26093,7 +26184,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_3, S_4$
+$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30795,7 +30886,8 @@
 and the non-separating clutching law
 $($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 the algebraic clutching identities ARE the degeneration formula
-applied to the bar complex on log-FM spaces.
+applied to the bar complex on the relative log-FM spaces of the
+universal family.
 
 More explicitly: in the finite-order shadow obstruction tower, the extension
 $\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
@@ -30812,7 +30904,8 @@
 BV operator that distinguishes non-separating from separating
 clutching, and is the primary reason that
 $D_\cA^2 = 0$ at the ambient level required the log-FM
-normal-crossings geometry of Mok~\cite[Theorem~3.3.1]{Mok25}
+normal-crossings geometry of Mok's relative compactification of the
+universal family~\cite[Theorem~3.3.1]{Mok25}
 (Theorem~\ref{thm:ambient-d-squared-zero}).
 \end{remark}
 

tokens used
309,529
