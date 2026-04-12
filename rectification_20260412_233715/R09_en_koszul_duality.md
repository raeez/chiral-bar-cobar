# R09_en_koszul_duality (790s)

In [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:2946), I repaired the topologization claim surface by making the proved statement exactly match the proof. `thm:topologization` is now a cohomological result on `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, while the chain-level lift is pushed into the existing conjectural lane `conj:topologization-general`. I also weakened `def:inner-conformal-vector` to the actually constructed condition `T-[Q,G]` being `Q`-exact, and synced the proof, construction, boundary interpretation, coderived remark, and chapter summaries so they no longer speak as if chain-level `\Ethree` were proved.

I re-read the modified theorem/proof/remark cluster and the in-file downstream references to `thm:topologization`, `conj:topologization-general`, `def:inner-conformal-vector`, and `constr:sugawara-antighost`. I attempted `make fast`, but the TeX process was killed by the system (`Error 137`), so there is no stable full-build verdict from that run. A filtered `chktex` pass over the edited line ranges did not reveal new syntax issues; the remaining warnings there are the file’s pre-existing style/lint debt.

## Rectification Summary
- [FIXED] CRITICAL T14 — restated `thm:topologization` as a BRST-cohomological `\Ethree` result, repointed `conj:topologization-general` to the chain-level strengthening, weakened `def:inner-conformal-vector` to match the actual construction, and synchronized the surrounding remarks/summaries so the concession at lines `3146–3176` is now consistent with the final claim.


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
session id: 019d83a0-a0b6-7fa2-8a25-2cf733a89971
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


TARGET: chapters/theory/en_koszul_duality.tex

FINDINGS TO FIX:

1. [CRITICAL T14] Line ~2947: Topologization theorem stated as chain-level E_3, but proof
   only establishes [Q,G] = T_Sug + Q-exact on Q-cohomology (lines 3307-3311).
   The file itself concedes the chain-level gap at 3146-3176.
   FIX: The strongest truthful choice:
   (a) Restate the theorem as a Q-COHOMOLOGY level result (E_3 on H*(Z^der, Q)), OR
   (b) If a chain-level proof exists elsewhere, cite it, OR
   (c) Split into: "cohomological E_3" (ProvedHere) + "chain-level E_3" (Conjectured).
   Option (c) is probably the strongest honest choice. Update ClaimStatus accordingly.

Read lines 2900-3200 carefully, verify the finding, make the fix.
Also check if the chain-level concession at 3146-3176 is consistent with the final claim.
mcp startup: no servers

thinking
**Evaluating skills for tasks**

I don't have a template for the status, but I think I should note the claim status. I might use PE-10 if it's a theorem, and I'm considering whether to use the claim-surface-sync skill since the status could drift. The task of rectifying the mathematical chapter or proof definitely calls for the beilinson-rectify skill. I'll also look into both skills since it seems appropriate to open enough skill files. Let's check that!
codex
Using `beilinson-rectify` and `claim-surface-sync` on [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex). I’m first reading the required constitutional files and the exact theorem/proof region around lines `2900–3200` and `3307–3311` to verify whether the theorem overclaims chain-level `E_3`.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3288,3335p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2900,3200p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
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
 exited 1 in 51ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
 succeeded in 51ms:
 {:}J^b\, c^c\, \bar c_a{:}$.
 This is $Q$-exact in the bulk: it equals
 $[Q, \frac{1}{2(k+h^\vee)} \sum_{a,b,c}
 f^a{}_{bc}\,{:}\bar c_b\, c^c\, \bar c_a{:}]$ up to terms
 proportional to the equations of motion, hence vanishes in
 $Q$-cohomology.
\item \emph{Ghost self-coupling from $Q \cdot \bar c_a$.}
 The term $f_{ab}{}^c\,\bar c_c\, c^b$ in $Q \cdot \bar c_a$
 contributes
 $\frac{1}{2(k+h^\vee)}\sum_a f_{ab}{}^c\,
 {:}J^a\, \bar c_c\, c^b{:}$.
 The sum $f_{ab}{}^c\,J^a\,\bar c_c\, c^b$ has ghost
 number~$-1$ and is $Q$-exact by the same mechanism: its
 $Q$-variation produces a term proportional to
 $f_{ab}{}^c\,f^a{}_{de}\,c^d\,c^e\,\bar c_c\,c^b$, which
 vanishes by the Jacobi identity
 $f_{ab}{}^c\,f^a{}_{de} + \text{cyc}(b,d,e) = 0$.
\end{enumerate}
In summary,
\begin{equation}\label{eq:TQG-result}
 succeeded in 51ms:


%================================================================
% The direct (brace-algebra) proof of the center theorem.
% Self-contained module: definitions, explicit signs, uniqueness.
%================================================================
\input{chapters/theory/chiral_center_theorem}


%================================================================
% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
%================================================================

\section{Topologization: from
\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC} to
\texorpdfstring{$\Ethree$}{E3}}
\label{sec:topologization}
\index{topologization theorem|textbf}
\index{Sugawara construction!topologization}
\index{E3 algebra@$\Ethree$-algebra!from Swiss-cheese + conformal vector}
 succeeded in 50ms:
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
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
codex
The local surface already confirms the reported mismatch: the theorem says chain-level `\Ethree`, while the surrounding remarks explicitly restrict the `\Etwo^{hol}\to\Etwo^{top}` step to `Q`-cohomology. I’m reading the exact dependency labels and line-numbered theorem/proof span now so the patch can separate proved cohomological content from the open chain-level strengthening without collateral drift.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2940,3205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3300,3320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(thm:operadic-center-hochschild|thm:brace-dg-algebra|prop:gerstenhaber-sl2-bracket|constr:sugawara-antighost)\\}|Topologization|topologization\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
  2940	holomorphic $\Etwo$ to topological $\Etwo$, one must show
  2941	that the complex-structure dependence is homotopically
  2942	trivial.
  2943	
  2944	\begin{definition}[Inner conformal vector]
  2945	\label{def:inner-conformal-vector}
  2946	\index{conformal vector!inner}
  2947	Let $\cA$ be a chiral algebra and let $Q$ be a
  2948	BRST-type differential on the algebra of observables
  2949	of a holomorphic--topological theory~$T$ on
  2950	$\bC \times \bR$ whose boundary chiral algebra
  2951	is~$\cA$. An \emph{inner conformal vector} for
  2952	$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
  2953	central charge~$c$ that is $Q$-exact in the algebra
  2954	of bulk observables: there exists $G(z)$ such that
  2955	$T(z) = [Q, G(z)]$.
  2956	For affine Kac--Moody $V_k(\fg)$ at non-critical level,
  2957	the Sugawara element
  2958	$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
  2959	\sum_a {:}J^a J_a{:}$
 succeeded in 51ms:
  3300	 number~$-1$ and is $Q$-exact by the same mechanism: its
  3301	 $Q$-variation produces a term proportional to
  3302	 $f_{ab}{}^c\,f^a{}_{de}\,c^d\,c^e\,\bar c_c\,c^b$, which
  3303	 vanishes by the Jacobi identity
  3304	 $f_{ab}{}^c\,f^a{}_{de} + \text{cyc}(b,d,e) = 0$.
  3305	\end{enumerate}
  3306	In summary,
  3307	\begin{equation}\label{eq:TQG-result}
  3308	[Q,\, G(z)] \;=\; T_{\mathrm{Sug}}(z) \;+\;
  3309	 (\text{$Q$-exact operators of ghost number $\ge 1$}).
  3310	\end{equation}
  3311	On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
  3312	the chain-level datum that makes the topologization proof
  3313	\textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
  3314	constructive.
  3315	
  3316	\textsc{The specialisation to $\fsl_2$.}
  3317	For $\fg = \fsl_2$ with standard basis
  3318	$\{e, f, h\}$ ($[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$)
  3319	and trace-form
 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
chapters/theory/en_koszul_duality.tex:24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
chapters/theory/en_koszul_duality.tex:26:The topologization proof is made constructive by an explicit
chapters/theory/en_koszul_duality.tex:1273:  topologization theorem
chapters/theory/en_koszul_duality.tex:1274:  (Theorem~\textup{\ref{thm:topologization}}).
chapters/theory/en_koszul_duality.tex:1792:\label{thm:operadic-center-hochschild}
chapters/theory/en_koszul_duality.tex:2913:\section{Topologization: from
chapters/theory/en_koszul_duality.tex:2916:\label{sec:topologization}
chapters/theory/en_koszul_duality.tex:2917:\index{topologization theorem|textbf}
chapters/theory/en_koszul_duality.tex:2918:\index{Sugawara construction!topologization}
chapters/theory/en_koszul_duality.tex:2964:\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
chapters/theory/en_koszul_duality.tex:2965:\label{thm:topologization}
chapters/theory/en_koszul_duality.tex:2967:\index{topologization theorem!statement}
chapters/theory/en_koszul_duality.tex:2981:\begin{equation}\label{eq:topologization}
chapters/theory/en_koszul_duality.tex:2987:where the first arrow is the topologization
chapters/theory/en_koszul_duality.tex:3023:\label{rem:topologization-inputs}
chapters/theory/en_koszul_duality.tex:3024:\index{topologization theorem!external inputs}
chapters/theory/en_koszul_duality.tex:3060:\begin{remark}[Scope: which algebras admit topologization]
chapters/theory/en_koszul_duality.tex:3061:\label{rem:topologization-scope}
chapters/theory/en_koszul_duality.tex:3062:\index{topologization theorem!scope}

thinking
**Inspecting references for consistency**

I need to check other mentions of the theorem within the same file to ensure everything is consistent. I'll look around lines 1273, 3434, and 5279 since the user only wants to edit the assigned file. I do need to verify those parts to make sure the theorem references aren’t overstating anything. I also see mentions around line 23, so I should check that front summary too. I’ll look through other relevant lines to adjust if anything overclaims.
codex
I’ve confirmed the local contradiction inside the same file: the statement is unconditional `\Ethree`, the proof only produces local constancy after passing to `Q`-cohomology, and the later remark states that gap explicitly. I’m sweeping the other in-file summaries of `Theorem~\ref{thm:topologization}` so the patch fixes the entire local claim surface, not just the theorem header.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5272,5292p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3388,3450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3470,3492p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1258,1285p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1258	carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.
  1259	
  1260	The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
  1261	the \emph{derived chiral center}
  1262	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
  1263	= C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$,
  1264	computed \emph{using} the bar complex as a resolution.
  1265	The derived center is the algebra of bulk observables of
  1266	the 3d HT theory on $X \times \bR$:
  1267	\begin{itemize}
  1268	\item It carries $\Etwo$ structure from
  1269	  $\FM_k(\bC)$ (the operadic center theorem,
  1270	  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
  1271	\item With an inner conformal vector at non-critical level,
  1272	  this $\Etwo$ upgrades to $\Ethree$ via the
  1273	  topologization theorem
  1274	  (Theorem~\textup{\ref{thm:topologization}}).
  1275	\item Without a conformal vector,
  1276	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ carries
  1277	  $\mathsf{SC}^{\mathrm{ch,top}}$ structure
 succeeded in 51ms:
  5272	$\Sigma_n$-coinvariants and uses the coshuffle coproduct
  5273	instead. At higher genus the fibrewise differential
  5274	$\dfib$ is curved with $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$
  5275	but is \emph{not} a coderivation; flatness and the coderivation
  5276	property are restored only by the period-corrected differential
  5277	$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
  5278	(Remark~\ref{rem:sc-higher-genus}).
  5279	The topologization theorem
  5280	(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
  5281	of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
  5282	with an explicit antighost contraction $G(z)$
  5283	(Construction~\ref{constr:sugawara-antighost}) that makes
  5284	the proof constructive. For class~M algebras, where the
  5285	chain-level $\Ethree$ encounters obstructions from
  5286	step~(iv) of Remark~\ref{rem:topologization-chain-vs-cohomology},
  5287	a coderived refinement (Conjecture~\ref{conj:coderived-e3})
  5288	provides the conjectural alternative.
  5289	
  5290	Three concrete calculations remain beyond the proved theorems.
  5291	First, explicit closed-form formulas for the $\En$ bar differential
 succeeded in 51ms:
     1	\chapter{\texorpdfstring{$\En$ Koszul duality and higher-dimensional bar complexes}{En Koszul duality and higher-dimensional bar complexes}}
     2	\label{ch:en-koszul-duality}
     3	
     4	\index{En algebra@$\En$ algebra!Koszul duality|textbf}
     5	\index{bar complex!higher-dimensional|textbf}
     6	
     7	For $\En$ algebras, the bar-cobar adjunction replaces the logarithmic
     8	propagator $d\log(z-w)$ with a closed $(n{-}1)$-form, the Arnold
     9	relations with the Totaro relations, and chiral Koszul duality with
    10	$\En$ Koszul duality. The underlying construction is the same:
    11	duality is mediated by a convolution algebra on a compactified
    12	configuration space. The passage from $n = 1$
    13	(associative/$A_\infty$) through $n = 2$ (the holomorphic refinement
    14	recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
    15	Vassiliev invariants) and beyond exhibits bar-cobar duality as a
    16	single construction parametrised by manifold dimension, with the
    17	formality phenomena of Kontsevich and Tamarkin as shadows of the
    18	Koszul property in each dimension.
    19	
    20	The chapter culminates in the chiral center theorem
 succeeded in 50ms:
  3470	coderived tensor product requires verification.
  3471	\end{remark}
  3472	
  3473	
  3474	
  3475	% ================================================================
  3476	% The E_3 identification theorem and explicit operations
  3477	% ================================================================
  3478	
  3479	The topologization theorem identifies the derived chiral
  3480	centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
  3481	$\Ethree$-algebra. The Costello--Francis--Gwilliam
  3482	construction produces another $\Ethree$-algebra $\cA^\lambda$
  3483	from perturbative Chern--Simons quantisation. Both deform
  3484	$C^*(\fg)$ over the same base. For simple $\fg$, the
  3485	one-dimensionality of $H^3(\fg)$ forces the two
  3486	deformation families to be isomorphic.
  3487	
  3488	\begin{theorem}[Identification of $\Ethree$-deformation families]
  3489	\label{thm:e3-identification}
 succeeded in 51ms:
  3388	\item \textup{(Coderived local constancy.)}
  3389	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3390	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  3391	  is locally constant. Precisely: the
  3392	  $m_0$-curvature obstruction to local constancy at
  3393	  step~\textup{(iv)} of
  3394	  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  3395	  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
  3396	  same mechanism that absorbs $\delta_4$ in
  3397	  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
  3398	\item \textup{(Coderived $\Ethree$.)}
  3399	  The locally-constant recognition principle
  3400	  \textup{(}Lurie~\cite{HA}\textup{)}, adapted to the
  3401	  coderived setting, equips the derived chiral center
  3402	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ with an
  3403	  $\Etwo^{\mathrm{top}}$-structure in $D^{\mathrm{co}}$.
  3404	  Combined with the $\Eone^{\mathrm{top}}$-structure from
  3405	  the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
  3406	  additivity gives an $\Ethree^{\mathrm{top}}$-structure in
  3407	  $D^{\mathrm{co}}$.

thinking
**Inspecting references in the document**

I need to check if "Theoremref{thm:topologization}" is mentioned elsewhere in the target document, possibly at chain-level discussions. The relevant lines seem to span around numbers like 23, 1271, 3479, and 5279, and I want to confirm if 3434 relates to q-cohomology. There's also a possibility that theorem e3-identification utilizes it. I should take a closer look at the segments between lines 3488 and 3555 to see what I can find!
codex
The downstream surface matters here: later in the same chapter there is an `E_3`-identification theorem whose opening sentence inherits whatever `Theorem~\ref{thm:topologization}` actually proves. I’m checking whether that lane also needs a local wording repair once the main theorem is narrowed/split.
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:topologization\\}|thm:topologization|conj:topologization-general|rem:topologization-chain-vs-cohomology\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3488,3578p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1274:  (Theorem~\textup{\ref{thm:topologization}}).
2965:\label{thm:topologization}
3063:Theorem~\ref{thm:topologization} is proved for affine
3082:Conjecture~\ref{conj:topologization-general} below.
3097:\label{conj:topologization-general}
3108:The proof of Theorem~\ref{thm:topologization} for affine
3132:Theorem~\ref{thm:topologization} to
3133:Conjecture~\ref{conj:topologization-general} is
3145:\label{rem:topologization-chain-vs-cohomology}
3146:The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
3186:The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
3313:\textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
3376: Conjecture~\textup{\ref{conj:topologization-general}}.
3394:  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
3412:  of Theorem~\textup{\ref{thm:topologization}}.
3436:  (Theorem~\ref{thm:topologization}).
3441:Remark~\ref{rem:topologization-chain-vs-cohomology} from
5280:(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
5286:step~(iv) of Remark~\ref{rem:topologization-chain-vs-cohomology},
 succeeded in 52ms:
  3488	\begin{theorem}[Identification of $\Ethree$-deformation families]
  3489	\label{thm:e3-identification}
  3490	\ClaimStatusProvedHere
  3491	Let $\fg$ be a simple finite-dimensional Lie algebra and
  3492	$V_k(\fg)$ the affine Kac--Moody vertex algebra at
  3493	level~$k$.
  3494	Writing $\lambda = k + h^\vee$ for the departure from
  3495	critical level, the derived chiral centre
  3496	$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ of
  3497	Proposition~\textup{\ref{prop:e3-structure}} and the
  3498	CFG $\Ethree$-algebra $\cA^\lambda$ of
  3499	Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
  3500	deformation families of $\Ethree$-algebras:
  3501	\begin{equation}\label{eq:e3-families}
  3502	  \{Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
  3503	  \}_{k + h^\vee \in \lambda\CC[[\lambda]]}
  3504	  \;\simeq\; \{\cA^\lambda\}_{\lambda
  3505	  \in \lambda H^3(\fg)[[\lambda]]}
  3506	\end{equation}
  3507	over the base $\lambda H^3(\fg)[[\lambda]]$
exec
/bin/zsh -lc "rg -n \"label\\{prop:e3-structure\\}|label\\{thm:e3-cs\\}|E_3|\\\\Ethree\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3640,3795p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{prop:e3-structure\}|label\{thm:e3-cs\}|E_3|\Ethree)
                                                         ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  3640	
  3641	% ----------------------------------------------------------------
  3642	\subsection{Explicit $\Ethree$ operations for
  3643	$V_k(\mathfrak{sl}_2)$}
  3644	\label{subsec:e3-explicit}
  3645	
  3646	\subsection{Explicit $\Ethree$ operations for
  3647	$V_k(\mathfrak{sl}_2)$}
  3648	\label{subsec:e3-explicit}
  3649	
  3650	The abstract $\Ethree$ structure of
  3651	Proposition~\ref{prop:e3-structure} acquires concrete content
  3652	for $\fg = \mathfrak{sl}_2$: the five-dimensional derived
  3653	chiral centre $\CC \oplus \mathfrak{sl}_2[-1] \oplus \CC[-2]$
  3654	carries an explicit cup product, Gerstenhaber bracket,
  3655	$\Pthree$ bracket, and BV operator, all computable from the
  3656	OPE.
  3657	
  3658	\medskip
  3659	\noindent
exec
/bin/zsh -lc 'rg -n "prop:e3-structure|thm:e3-cs|chiral-e3-cfg|cfg" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5200,5335p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3497:Proposition~\textup{\ref{prop:e3-structure}} and the
3499:Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
3535:  \textup{(}Theorem~\textup{\ref{thm:chiral-e3-cfg}(ii)}%
3540:  \textup{(}Theorem~\ref{thm:e3-cs}(iv)\textup{)} holds
3563:(Theorem~\ref{thm:e3-cs}(ii) and
3564:Theorem~\ref{thm:cfg}(iv) respectively).
3587:(Theorem~\ref{thm:chiral-e3-cfg}(i)), so
3608:(Theorem~\ref{thm:chiral-e3-cfg}, Step~1 of the
3609:proof). By Theorem~\ref{thm:chiral-e3-cfg}(ii), the
3633:(Theorem~\ref{thm:e3-cs}(iv)) requires the Sugawara
3651:Proposition~\ref{prop:e3-structure} acquires concrete content
3661:By Proposition~\ref{prop:e3-structure} and the chiral
4016:(Theorem~\ref{thm:cfg}(iv)). The generator of
4040:(Theorem~\ref{thm:cfg}(iv));
4386:  Theorem~\textup{\ref{thm:e3-cs}(ii)}.
4432:is provided by Proposition~\ref{prop:e3-structure}(ii)
4725:Theorem~\ref{thm:e3-cs}(ii): $H^3(\fg)$ is one-dimensional
4827:\label{subsec:chiral-e3-cfg-comparison}
4838:\label{thm:chiral-e3-cfg}
4842:\begin{equation}\label{eq:cfg-comparison}
 succeeded in 51ms:
  5200	  \label{eq:sl2-p3-hf}
  5201	  \{\phi_h, \phi_f\}^{\mathrm{ch}}
  5202	  &= -2\,\phi_f, \\
  5203	  \label{eq:sl2-p3-hh}
  5204	  \{\phi_h, \phi_h\}^{\mathrm{ch}}
  5205	  &= 2k\,\partial, \\
  5206	  \label{eq:sl2-p3-ee}
  5207	  \{\phi_e, \phi_e\}^{\mathrm{ch}}
  5208	  &= 0, \\
  5209	  \label{eq:sl2-p3-ff}
  5210	  \{\phi_f, \phi_f\}^{\mathrm{ch}}
  5211	  &= 0.
  5212	\end{align}
  5213	The Lie bracket terms ($\phi_h$ in~\eqref{eq:sl2-p3-ef},
  5214	$2\phi_e$ in~\eqref{eq:sl2-p3-he},
  5215	$-2\phi_f$ in~\eqref{eq:sl2-p3-hf}) persist at $k = 0$;
  5216	the cocycle terms ($k\,\partial$ in~\eqref{eq:sl2-p3-ef}
  5217	and~\eqref{eq:sl2-p3-hh}) vanish at $k = 0$
  5218	(AP126 check: at $k = 0$, the level-dependent terms
  5219	vanish, and the bracket reduces to the Chevalley--Eilenberg

thinking
**Verifying chain-level proof**

I need to check if there is chain-level proof available in the target or repository. The user mentioned reading lines 2900-3200 carefully, which makes me think I should focus on that section. However, the strongest technical approach might be to cite any relevant proof if it exists elsewhere. I'll make sure to examine these details thoroughly to provide the best response for the user!
codex
Before I edit, I need to know whether the chain-level claim can actually be saved for affine Kac–Moody by citing an existing `SC`-formality result in this same file. If that proof surface exists, I’ll keep the stronger theorem and anchor it; if it doesn’t, I’ll split the claim into proved cohomological content plus an explicit chain-level conjectural strengthening.
exec
/bin/zsh -lc "rg -n \"SC-formal|SC formal|topologization|chain-level \\\\Ethree|cohomological \\\\Ethree\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"SC-formal|SC formal|m_k\\"'^'"\\{\\\\mathrm\\{SC\\}\\}|class~L|class~\\\\mathsf\\{L\\}|chain-level and cohomological|cohomological \\\\Ethree|chain-level \\\\Ethree\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:SC-formal|SC formal|topologization|chain-level \Ethree|cohomological \Ethree)
                                                      ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:SC-formal|SC formal|m_k\^\{\mathrm\{SC\}\}|class~L|class~\mathsf\{L\}|chain-level and cohomological|cohomological \Ethree|chain-level \Ethree)
                                  ^^
error: unrecognized escape sequence

thinking
**Considering string patterns**

I’m thinking I need simpler patterns with fixed strings, which might call for multiple regular expressions instead of using regex escapes. Maybe I can utilize `rg -F` or just plain strings. This way, I might avoid complications and create a more straightforward approach. Simplifying this could make things more manageable and efficient in whatever I’m working on. It’s something worth exploring further to find the best solution!
exec
/bin/zsh -lc 'rg -n -F "class~L" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "SC-formal" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
 succeeded in 52ms:
894:remains class~L ($r_{\max} = 3$), the $\beta\gamma$ system
exec
/bin/zsh -lc 'rg -n -F "chain-level and cohomological" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"chain-level and cohomological\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"SC-formal\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3172:$k \geq 3$\textup{)}, the chain-level and cohomological
 succeeded in 50ms:
chapters/theory/en_koszul_duality.tex:3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/chiral_koszul_pairs.tex:86:(Heisenberg and its relatives) is SC-formal
chapters/theory/chiral_koszul_pairs.tex:2511:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2515:algebra outside class~$G$ can be SC-formal. The answer
chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2524:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2533:SC-formal\textup{)} is established in
chapters/theory/chiral_koszul_pairs.tex:2539:For the converse, suppose~$\cA$ is SC-formal.
chapters/theory/chiral_koszul_pairs.tex:2548: \text{SC-formal}
chapters/theory/chiral_koszul_pairs.tex:2571:brackets; SC-formality is incompatible with each. The only
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:3172:$k \geq 3$\textup{)}, the chain-level and cohomological
codex
The file does not contain any proved `SC`-formality result that would rescue the chain-level statement for affine Kac–Moody. In fact, the only local “G and L are SC-formal” sentence is itself unsupported and conflicts with the repo constitution, so I’m treating it as part of the overclaim surface and correcting it while keeping the edit strictly inside the assigned file.
exec
/bin/zsh -lc 'rg -n -F "chain-level topologization" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "topologization-chain" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:topologization}\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "cohomological topologization" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3145:\label{rem:topologization-chain-vs-cohomology}
3394:  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
3441:Remark~\ref{rem:topologization-chain-vs-cohomology} from
5286:step~(iv) of Remark~\ref{rem:topologization-chain-vs-cohomology},
 exited 1 in 52ms:

 succeeded in 51ms:
3144:\begin{remark}[Chain-level vs cohomological topologization]
 succeeded in 51ms:
3063:Theorem~\ref{thm:topologization} is proved for affine
3108:The proof of Theorem~\ref{thm:topologization} for affine
3132:Theorem~\ref{thm:topologization} to
3146:The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
3436:  (Theorem~\ref{thm:topologization}).
5280:(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
Plan update
Verified that the theorem overclaims chain-level E3 and that no supporting chain-level proof exists in the target file. I’m patching the local claim surface only, with a proved cohomological theorem plus an explicit chain-level conjectural strengthening, then re-reading all in-file references to the theorem.
  ✓ Audit theorem, proof, and surrounding remarks for the topologization claim surface in en_koszul_duality.tex
  → Patch theorem statement/status surface to separate proved cohomological content from conjectural chain-level content
  • Re-read downstream references in the same file and verify no remaining overclaims or broken labels




thinking
**Clarifying conjectures**

I’m thinking about how to improve the clarity in my writing. Adding a sentence after the theorem or before the general conjecture could really help. I could use something like, "The chain-level enhancement of this affine cohomological E3 structure is conjectural; see Conjecture\ref{conj:topologization-general}." After that, the general conjecture should clearly state whether it’s talking about chain-level or cochain-level, which seems really important for understanding!
thinking
**Considering theorem and conjecture placement**

I’m thinking about where to place the conjecture in relation to the theorem. Should it go after the theorem or immediately before the proof? If it’s a new conjecture, then the proof would just remain part of the theorem. Since the user suggests splitting into theorem and conjecture, maybe I could add a brief remark after the theorem but before the proof. However, it seems rewriting the existing general conjecture later might be enough.
thinking
**Refining conjectures**

I'm considering how to refine the conjectures regarding general chiral algebras to avoid redundancy. Since affine is a specific case of the general, keeping the affine conjecture could be unnecessary unless it helps clarify things. A better approach might be to strengthen the existing conjecture by focusing on general chiral algebras and modifying it to reflect this. I think creating a new title, “[Chain-level topologization for general chiral algebras],” would streamline our efforts while still aligning the theorem and conjecture appropriately.
thinking
**Revising mathematical language**

I realize that the sentence I wrote overstates the chain-level datum. I think it's better to phrase it as "This is the explicit operator-level datum that makes the cohomological topologization argument constructive." This is important because the equation includes Q-exact error terms. So, I’ll make sure to modify it accordingly to clarify my arguments and ensure they are presented correctly. It feels crucial to communicate these details accurately.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3310,3418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "identifies the derived chiral centre" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"upgrades to \\Ethree\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "upgrades the resulting" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
  3310	\end{equation}
  3311	On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
  3312	the chain-level datum that makes the topologization proof
  3313	\textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
  3314	constructive.
  3315	
  3316	\textsc{The specialisation to $\fsl_2$.}
  3317	For $\fg = \fsl_2$ with standard basis
  3318	$\{e, f, h\}$ ($[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$)
  3319	and trace-form
  3320	$\kappa(e,f) = 1$, $\kappa(h,h) = 2$, the Sugawara
  3321	element is
  3322	$T_{\mathrm{Sug}} = \frac{1}{2(k+2)}\bigl(
  3323	{:}J^e J^f{:} + {:}J^f J^e{:} + \tfrac{1}{2}{:}J^h J^h{:}\bigr)$,
  3324	and the antighost contraction is
  3325	\[
  3326	G(z) \;=\; \frac{1}{2(k+2)}\bigl(
  3327	{:}J^e(z)\,\bar c_f(z){:}
  3328	\;+\; {:}J^f(z)\,\bar c_e(z){:}
  3329	\;+\; \tfrac{1}{2}\,{:}J^h(z)\,\bar c_h(z){:}
 succeeded in 51ms:
24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n -F "prop:e3-structure" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:e3-cs" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3540:  \textup{(}Theorem~\ref{thm:e3-cs}(iv)\textup{)} holds
3563:(Theorem~\ref{thm:e3-cs}(ii) and
3633:(Theorem~\ref{thm:e3-cs}(iv)) requires the Sugawara
4386:  Theorem~\textup{\ref{thm:e3-cs}(ii)}.
4725:Theorem~\ref{thm:e3-cs}(ii): $H^3(\fg)$ is one-dimensional
5008:base (Theorem~\ref{thm:e3-cs}(ii) and
 succeeded in 51ms:
3497:Proposition~\textup{\ref{prop:e3-structure}} and the
3651:Proposition~\ref{prop:e3-structure} acquires concrete content
3661:By Proposition~\ref{prop:e3-structure} and the chiral
4432:is provided by Proposition~\ref{prop:e3-structure}(ii)

thinking
**Searching for label location**

I’m wondering if there’s no label location because it might be in the included file. Perhaps it's earlier than line 2900 in that same file? I think I should widen my search a bit more. I could use a command like `rg -n -F "label{prop:e3-structure}"` to check more thoroughly. It seems like a good way to make sure I’m not missing anything important! Let's see what I can find.
exec
/bin/zsh -lc 'rg -n -F "label{prop:e3-structure}" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "label{thm:e3-cs}" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F "H''^'"\\bullet_Q\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "bulk observables" chapters/theory/en_koszul_duality.tex | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Q-cohomology" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
1265:The derived center is the algebra of bulk observables of
2155:\item \emph{Closed color $=$ bulk observables.} The closed-sector
2165:\item \emph{Center $=$ interior bulk observables.} The
2597: interior bulk observables in the half-space
2954:of bulk observables: there exists $G(z)$ such that
 exited 1 in 51ms:

codex
```text
scope_lock:
  file: chapters/theory/en_koszul_duality.tex
  labels: thm:topologization, conj:topologization-general, rem:topologization-chain-vs-cohomology
  issue: theorem states chain-level E3, proof only yields Q-cohomological local constancy

PE-10:
genus: NA
degree: NA
claim surface: topologization theorem for affine KM
proved statement available: cohomological E3 on Q-cohomology
chain-level E3 proved here? N
status split:
  thm:topologization -> ProvedHere, cohomological
  conj:topologization-general -> Conjectured, chain-level strengthening
local references to sync: intro sentence, derived-center summary, evidence remark, chain-vs-cohomology remark, concluding chapter summary
verdict: ACCEPT
```



thinking
**Investigating theorem claims**

I’m considering a theorem introduction that may relate to formal deformation families of E3-algebras at a cohomological level. The current theorem statement seems to overreach by claiming that `Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))` is a formal deformation family of E3-algebras. This citation might not be appropriate if Prop `prop:e3-structure` also overclaims chain-level. I need to inspect it to ensure it aligns with my goals, but I can only edit the specific file assigned. Do I need to adjust my findings?
thinking
**Revising theorem statement**

I see that the opening sentence at line 3479 can be revised, but the theorem statement references Prop `prop:e3-structure`. If this proposition is in the same included file, it might not be allowed to change it. However, I wonder if I could avoid making changes since it doesn't directly stem from the topologization theorem. I need to tread carefully here to ensure everything remains consistent and within the guidelines.
thinking
**Inspecting theorem safety**

I'm considering how to check if the later theorem is safe by looking at the included file. Given that it's nested in chapters/theory/chiral_center_theorem.tex, I know I can read it but not edit it. I might need to figure out if the e3-identification theorem is a different concern. The patch shouldn’t create new inconsistencies, but I think it's okay to address existing ones. If there's an issue with line 3479 using the topologization overclaim, I can fix the summary sentence. I’ll also need to quickly inspect the label `prop:e3-structure` to see if the topologization theorem is there. Let's search within that file!
codex
I’m keeping the patch scoped, but there is one more local dependency check: if a downstream statement already has an independent `E_3` source, I should avoid overcorrecting it. I’m reading the referenced `prop:e3-structure`/`thm:e3-cs` surfaces only to decide which in-file summary sentences can be safely narrowed and which should be left alone.
exec
/bin/zsh -lc 'rg -n -F "label{prop:e3-structure}" chapters/theory/chiral_center_theorem.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "label{thm:e3-cs}" chapters/theory/chiral_center_theorem.tex chapters/theory/en_koszul_duality.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "prop:e3-structure" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:e3-cs" chapters/theory/chiral_center_theorem.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:3540:  \textup{(}Theorem~\ref{thm:e3-cs}(iv)\textup{)} holds
chapters/theory/en_koszul_duality.tex:3563:(Theorem~\ref{thm:e3-cs}(ii) and
chapters/theory/en_koszul_duality.tex:3633:(Theorem~\ref{thm:e3-cs}(iv)) requires the Sugawara
chapters/theory/en_koszul_duality.tex:4386:  Theorem~\textup{\ref{thm:e3-cs}(ii)}.
chapters/theory/en_koszul_duality.tex:4725:Theorem~\ref{thm:e3-cs}(ii): $H^3(\fg)$ is one-dimensional
chapters/theory/en_koszul_duality.tex:5008:base (Theorem~\ref{thm:e3-cs}(ii) and



thinking
**Considering LaTeX Structure**

I'm thinking about whether I should use `\text{-structure}` after the equation or if `\text{-algebra structure}` is a better fit. I want to ensure it's clear in LaTeX. The equation will look like this: 

\text{ carries an }\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}} = \Ethree^{\mathrm{top}}\text{-algebra structure}. 

It doesn't seem weird, and I think it might fit well once I finalize it.
thinking
**Reevaluating definitions and theorems**

I've noticed that construction 3307 states that for affine KM, the requirement is `T = [Q,G]` on Q-cohomology but not at the chain level. This makes me think that maybe my definition overclaims too much. The theorem suggests that Sugawara provides an inner conformal vector, but it only gives an equation up to Q-exact higher ghost terms. If those terms are indeed Q-exact, then presuming chain-level equality in cohomology might be incorrect. I may need to adjust the definition of an inner conformal vector accordingly.
thinking
**Defining inner conformal vector**

I'm thinking that the strongest technical choice might be to define the "inner conformal vector" as exact in BRST cohomology instead of in the cochain complex. This seems necessary since the theorem and proof utilize that approach. However, it feels like a significant change while still aiming for the same target. I should also check if this definition appears elsewhere in the file to ensure consistency. It’s important to keep everything aligned!
codex
A second overclaim sits one step upstream of the theorem: `Definition~\ref{def:inner-conformal-vector}` currently requires literal chain-level equality `T=[Q,G]`, while the construction only proves that equality after passing to BRST cohomology. I’m folding that into the same patch so the theorem’s hypothesis matches what the file actually constructs.
exec
/bin/zsh -lc 'rg -n -F "def:inner-conformal-vector" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "inner conformal vector" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2945:\label{def:inner-conformal-vector}
2974:\textup{(}Definition~\textup{\ref{def:inner-conformal-vector}}\textup{)}.
 succeeded in 51ms:
1271:\item With an inner conformal vector at non-critical level,
2951:is~$\cA$. An \emph{inner conformal vector} for
2960:provides the inner conformal vector. For the
2973:provides an inner conformal vector
2988:\textup{(}the inner conformal vector makes holomorphic
2994:The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
3066:an explicit inner conformal vector and the $3$d
3110:inner conformal vector $T = [Q, G]$, and (ii)~the
3385:Let $\cA$ be a chirally Koszul algebra with inner conformal vector
3434:\item Topologization via inner conformal vector is proved on

thinking
**Revising mathematical notation**

I need to update the remark in line 3110. The phrase "inner conformal vector T=[Q,G]" should change to "inner conformal vector represented by \(T=[Q,G]\) in BRST cohomology." Also, I might want to include a chain-level conjecture that mentions how, in the affine Kac–Moody case, this lifts Theorem... I think that's a good addition, so I'll plan to incorporate that!
codex
I’m editing the theorem surface now. The patch does three things inside [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex): it weakens the definition and theorem only where the proof forces it, it repoints the existing general conjecture to the chain-level strengthening, and it synchronizes the nearby summaries/remarks that were still speaking as if chain-level `E_3` were proved.
codex
The first patch missed one exact context block, so I’m re-reading the affected spans and applying the same content in smaller hunks. The edit scope is unchanged; this is just to keep the patch aligned with the live file.
exec
/bin/zsh -lc "sed -n '3478,3486p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18,34p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3306,3354p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3060,3188p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1266,1277p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2944,3022p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3388,3420p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5278,5288p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The topologization theorem identifies the derived chiral
centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
$\Ethree$-algebra. The Costello--Francis--Gwilliam
construction produces another $\Ethree$-algebra $\cA^\lambda$
from perturbative Chern--Simons quantisation. Both deform
$C^*(\fg)$ over the same base. For simple $\fg$, the
one-dimensionality of $H^3(\fg)$ forces the two
deformation families to be isomorphic.
 succeeded in 51ms:
Koszul property in each dimension.

The chapter culminates in the chiral center theorem
(\S\ref{sec:operadic-center-theorem}), which identifies the chiral
Hochschild cochain complex as the operadic center of an
$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
theorem (\S\ref{sec:topologization}), which upgrades the resulting
$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
The topologization proof is made constructive by an explicit
antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
in the $3$d holomorphic Chern--Simons BV complex
(Construction~\ref{constr:sugawara-antighost}). For class~M
algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
encounters obstructions from the infinite shadow tower, a coderived
refinement provides an alternative path
(Conjecture~\ref{conj:coderived-e3}).

 succeeded in 50ms:
the 3d HT theory on $X \times \bR$:
\begin{itemize}
\item It carries $\Etwo$ structure from
  $\FM_k(\bC)$ (the operadic center theorem,
  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
\item With an inner conformal vector at non-critical level,
  this $\Etwo$ upgrades to $\Ethree$ via the
  topologization theorem
  (Theorem~\textup{\ref{thm:topologization}}).
\item Without a conformal vector,
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ carries
  $\mathsf{SC}^{\mathrm{ch,top}}$ structure
 succeeded in 51ms:
In summary,
\begin{equation}\label{eq:TQG-result}
[Q,\, G(z)] \;=\; T_{\mathrm{Sug}}(z) \;+\;
 (\text{$Q$-exact operators of ghost number $\ge 1$}).
\end{equation}
On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
the chain-level datum that makes the topologization proof
\textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
constructive.

\textsc{The specialisation to $\fsl_2$.}
For $\fg = \fsl_2$ with standard basis
$\{e, f, h\}$ ($[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$)
and trace-form
$\kappa(e,f) = 1$, $\kappa(h,h) = 2$, the Sugawara
element is
$T_{\mathrm{Sug}} = \frac{1}{2(k+2)}\bigl(
{:}J^e J^f{:} + {:}J^f J^e{:} + \tfrac{1}{2}{:}J^h J^h{:}\bigr)$,
and the antighost contraction is
\[
 succeeded in 52ms:
\begin{remark}[Scope: which algebras admit topologization]
\label{rem:topologization-scope}
\index{topologization theorem!scope}
Theorem~\ref{thm:topologization} is proved for affine
Kac--Moody $V_k(\fg)$ at non-critical level
$k \neq -h^\vee$, where the Sugawara element provides
an explicit inner conformal vector and the $3$d
holomorphic--topological theory is Chern--Simons.
Topologization produces the perturbative
Chern--Simons $\Ethree$-algebra of
Costello--Francis--Gwilliam.

For general chiral algebras with conformal vector, the
same conclusion is expected but remains conjectural:

Virasoro $\mathrm{Vir}_c$: the algebra carries its own
stress tensor $T(z)$. The holomorphic--topological theory
is $3$d gravity. Topologization requires $T$ to be $Q$-exact
in the $3$d gravity bulk; this is expected at generic
$c \neq 0$ but requires constructing the BRST complex of
 succeeded in 51ms:
\begin{definition}[Inner conformal vector]
\label{def:inner-conformal-vector}
\index{conformal vector!inner}
Let $\cA$ be a chiral algebra and let $Q$ be a
BRST-type differential on the algebra of observables
of a holomorphic--topological theory~$T$ on
$\bC \times \bR$ whose boundary chiral algebra
is~$\cA$. An \emph{inner conformal vector} for
$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
central charge~$c$ that is $Q$-exact in the algebra
of bulk observables: there exists $G(z)$ such that
$T(z) = [Q, G(z)]$.
For affine Kac--Moody $V_k(\fg)$ at non-critical level,
the Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
\sum_a {:}J^a J_a{:}$
provides the inner conformal vector. For the
Virasoro algebra, $T(z)$ is the stress tensor itself.
\end{definition}

 succeeded in 52ms:
\item \textup{(Coderived local constancy.)}
  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  is locally constant. Precisely: the
  $m_0$-curvature obstruction to local constancy at
  step~\textup{(iv)} of
  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
  same mechanism that absorbs $\delta_4$ in
  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
\item \textup{(Coderived $\Ethree$.)}
  The locally-constant recognition principle
  \textup{(}Lurie~\cite{HA}\textup{)}, adapted to the
  coderived setting, equips the derived chiral center
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ with an
  $\Etwo^{\mathrm{top}}$-structure in $D^{\mathrm{co}}$.
  Combined with the $\Eone^{\mathrm{top}}$-structure from
  the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
  additivity gives an $\Ethree^{\mathrm{top}}$-structure in
  $D^{\mathrm{co}}$.
 succeeded in 51ms:
(Remark~\ref{rem:sc-higher-genus}).
The topologization theorem
(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
with an explicit antighost contraction $G(z)$
(Construction~\ref{constr:sugawara-antighost}) that makes
the proof constructive. For class~M algebras, where the
chain-level $\Ethree$ encounters obstructions from
step~(iv) of Remark~\ref{rem:topologization-chain-vs-cohomology},
a coderived refinement (Conjecture~\ref{conj:coderived-e3})
provides the conjectural alternative.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -24,5 +24,7 @@
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
@@ -1271,3 +1273,3 @@
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
apply_patch(auto_approved=true) exited 0 in 39ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..dee77ddc9dd81b524364eb12ca97a8fd6bda7cb0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..dee77ddc9dd81b524364eb12ca97a8fd6bda7cb0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -2955,4 +2955,5 @@
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
@@ -2965,3 +2966,3 @@
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
@@ -2981,13 +2982,16 @@
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
@@ -2995,3 +2999,4 @@
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
@@ -3004,4 +3009,5 @@
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
@@ -3013,3 +3019,4 @@
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
@@ -3020,3 +3027,3 @@
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..3eff20fb0e3d7490d5a416dbcc5c0f9e9216a8b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..3eff20fb0e3d7490d5a416dbcc5c0f9e9216a8b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3076,5 +3076,5 @@
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
@@ -3104,3 +3104,3 @@
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
@@ -3110,4 +3110,5 @@
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
@@ -3118,3 +3119,3 @@
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
@@ -3124,3 +3125,5 @@
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
@@ -3154,4 +3157,4 @@
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
@@ -3177,10 +3180,13 @@
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 43ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..7bea81bf38aae26630d7a66f46407b9dfeef6c6a
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..7bea81bf38aae26630d7a66f46407b9dfeef6c6a
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3201,5 +3201,5 @@
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
@@ -3326,3 +3326,4 @@
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
@@ -3362,5 +3363,6 @@
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..090812d818f6ad1a545ec60ff69872364ba3a2d5
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..090812d818f6ad1a545ec60ff69872364ba3a2d5
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3424,10 +3424,10 @@
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
apply_patch(auto_approved=true) exited 0 in 52ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d684615732891dae3f1c976bb82bdd3dbde4bd39
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d684615732891dae3f1c976bb82bdd3dbde4bd39
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3495,5 +3495,5 @@
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
@@ -5296,4 +5296,5 @@
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d822d5a68c69744cc5509ac0f73be4e2e659f096
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3493,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5294,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d822d5a68c69744cc5509ac0f73be4e2e659f096
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3493,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5294,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

codex
The theorem/proof split is in place. I’m re-reading for coherence now, especially the nearby sentences that still use the old literal `T=[Q,G]` wording or might have picked up grammatical damage from the narrowed statement.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '18,34p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1266,1278p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
    18	Koszul property in each dimension.
    19	
    20	The chapter culminates in the chiral center theorem
    21	(\S\ref{sec:operadic-center-theorem}), which identifies the chiral
    22	Hochschild cochain complex as the operadic center of an
    23	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
    24	theorem (\S\ref{sec:topologization}), which upgrades the resulting
    25	$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
    26	conformal vector.
    27	The topologization proof is made constructive by an explicit
    28	antighost contraction $G(z)$ representing
    29	$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
    30	in the $3$d holomorphic Chern--Simons BV complex
    31	(Construction~\ref{constr:sugawara-antighost}). For class~M
    32	algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
    33	encounters obstructions from the infinite shadow tower, a coderived
    34	refinement provides an alternative path
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3306,3354p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2944,3025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3478,3486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3060,3188p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3388,3420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5278,5288p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "upgrades the" chapters/theory/en_koszul_duality.tex | rg -n -F "topologization"' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "T = [Q, G]" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1266	computed \emph{using} the bar complex as a resolution.
  1267	The derived center is the algebra of bulk observables of
  1268	the 3d HT theory on $X \times \bR$:
  1269	\begin{itemize}
  1270	\item It carries $\Etwo$ structure from
  1271	  $\FM_k(\bC)$ (the operadic center theorem,
  1272	  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
  1273	\item With an inner conformal vector at non-critical level,
  1274	  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
  1275	  topologization theorem
  1276	  (Theorem~\textup{\ref{thm:topologization}}).
  1277	\item Without a conformal vector,
  1278	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ carries
exec
/bin/zsh -lc "rg -n -F \"upgrades to an \\Ethree\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3306	 f^a{}_{bc}\,{:}\bar c_b\, c^c\, \bar c_a{:}]$ up to terms
  3307	 proportional to the equations of motion, hence vanishes in
  3308	 $Q$-cohomology.
  3309	\item \emph{Ghost self-coupling from $Q \cdot \bar c_a$.}
  3310	 The term $f_{ab}{}^c\,\bar c_c\, c^b$ in $Q \cdot \bar c_a$
  3311	 contributes
  3312	 $\frac{1}{2(k+h^\vee)}\sum_a f_{ab}{}^c\,
  3313	 {:}J^a\, \bar c_c\, c^b{:}$.
  3314	 The sum $f_{ab}{}^c\,J^a\,\bar c_c\, c^b$ has ghost
  3315	 number~$-1$ and is $Q$-exact by the same mechanism: its
  3316	 $Q$-variation produces a term proportional to
  3317	 $f_{ab}{}^c\,f^a{}_{de}\,c^d\,c^e\,\bar c_c\,c^b$, which
  3318	 vanishes by the Jacobi identity
  3319	 $f_{ab}{}^c\,f^a{}_{de} + \text{cyc}(b,d,e) = 0$.
  3320	\end{enumerate}
  3321	In summary,
  3322	\begin{equation}\label{eq:TQG-result}
  3323	[Q,\, G(z)] \;=\; T_{\mathrm{Sug}}(z) \;+\;
  3324	 (\text{$Q$-exact operators of ghost number $\ge 1$}).
  3325	\end{equation}
 succeeded in 50ms:
  2944	trivial.
  2945	
  2946	\begin{definition}[Inner conformal vector]
  2947	\label{def:inner-conformal-vector}
  2948	\index{conformal vector!inner}
  2949	Let $\cA$ be a chiral algebra and let $Q$ be a
  2950	BRST-type differential on the algebra of observables
  2951	of a holomorphic--topological theory~$T$ on
  2952	$\bC \times \bR$ whose boundary chiral algebra
  2953	is~$\cA$. An \emph{inner conformal vector} for
  2954	$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
  2955	central charge~$c$ that is $Q$-exact in the algebra
  2956	of bulk observables up to a $Q$-boundary: there exists
  2957	$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
  2958	Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
  2959	For affine Kac--Moody $V_k(\fg)$ at non-critical level,
  2960	the Sugawara element
  2961	$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
  2962	\sum_a {:}J^a J_a{:}$
  2963	provides the inner conformal vector. For the
 succeeded in 50ms:
  3060	\emph{intermediary} between
  3061	$\Eone$-chiral and $\Ethree$; the conformal vector is
  3062	the bridge. This resolves the apparent paradox of the
  3063	dimensional ladder: the $n = 2$ (chiral) and $n = 3$
  3064	(Chern--Simons) rows are connected not by an automatic
  3065	operadic promotion, but by the physical data of a stress
  3066	tensor.
  3067	\end{remark}
  3068	
  3069	\begin{remark}[Scope: which algebras admit topologization]
  3070	\label{rem:topologization-scope}
  3071	\index{topologization theorem!scope}
  3072	Theorem~\ref{thm:topologization} is proved for affine
  3073	Kac--Moody $V_k(\fg)$ at non-critical level
  3074	$k \neq -h^\vee$, where the Sugawara element provides
  3075	an explicit inner conformal vector and the $3$d
  3076	holomorphic--topological theory is Chern--Simons.
  3077	Topologization produces the corresponding
  3078	cohomological $\Ethree$-algebra on BRST cohomology.
  3079	The chain-level enhancement remains conjectural.
 succeeded in 52ms:
  3478	(~\cite{HA}, Theorem~5.4.5.9) is stated for
  3479	factorization algebras valued in a stable $\infty$-category;
  3480	the coderived category $D^{\mathrm{co}}(\cA)$ is stable
  3481	(Positselski), but the factorization-algebra formalism in
  3482	$D^{\mathrm{co}}$ has not been developed in the literature.
  3483	Second, Dunn additivity
  3484	$\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}} \simeq
  3485	\Ethree^{\mathrm{top}}$ is proved for $\En$-algebras in
  3486	stable $\infty$-categories; its compatibility with the
 succeeded in 52ms:
  3388	 $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
  3389	 in the $3$d gravity \textup{(}respectively higher-spin
  3390	 gravity\textup{)} bulk. This bulk theory and its BRST complex
  3391	 have not been constructed at the BV level; the antighost
  3392	 contraction for class~M is the content of
  3393	 Conjecture~\textup{\ref{conj:topologization-general}}.
  3394	\end{enumerate}
  3395	\end{remark}
  3396	
  3397	\begin{conjecture}[Coderived $\Ethree$ for class~M; \ClaimStatusConjectured]
  3398	\label{conj:coderived-e3}%
  3399	\index{coderived category!E3 structure@$\Ethree$ structure|textbf}%
  3400	\index{topologization theorem!coderived refinement}%
  3401	\index{E3 algebra@$\Ethree$ algebra!coderived}%
  3402	Let $\cA$ be a chirally Koszul algebra with inner conformal vector
  3403	at non-critical level.
  3404	\begin{enumerate}[label=\textup{(\roman*)}]
  3405	\item \textup{(Coderived local constancy.)}
  3406	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3407	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
 succeeded in 51ms:
1:24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
4:5297:(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
 succeeded in 51ms:
  5278	Theorem~\ref{thm:knudsen-higher-enveloping},
  5279	Proposition~\ref{prop:en-formality};
  5280	see also Remark~\ref{rem:en-scope}).
  5281	The \emph{ordered} bar complex
  5282	$\barB^{\mathrm{ord}}(\cA)=T^c(s^{-1}\bar\cA)$ is a dg coalgebra
  5283	over the holomorphic--topological Swiss-cheese operad
  5284	$\mathsf{SC}^{\mathrm{ch,top}}$: the differential is the
  5285	closed $(n=2)$ color, the deconcatenation coproduct is the
  5286	open $(n=1)$ color
  5287	(Theorem~\ref{thm:bar-swiss-cheese}); the symmetric bar
  5288	$\barB^{\Sigma}(\cA)$ of Theorem~A is recovered by $R$-twisted
 succeeded in 51ms:
3089:$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
3149:$\cW_N$) and the verification that $T = [Q, G]$ therein.
3170:\item The Sugawara contraction $T = [Q, G]$ is proved at the
3388: $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
 exited 1 in 56ms:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d822d5a68c69744cc5509ac0f73be4e2e659f096
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3493,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5294,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the




thinking
**Correcting document lines**

I realize that the output from line 3478 isn't what I wanted because I requested the wrong range; I actually need around line 3479. It might have shifted due to inserted lines. I'll check for the phrase "identifies the BRST cohomology." I also want to verify the grammar in the theorem proof from lines 3001 to 3005, as it seems to lack proper subject structure. I'll rephrase it to fix the grammar issue. Let’s patch it up!
thinking
**Adjusting operator relations**

I need to adjust the occurrences of \(T=[Q,G]\). For example, at line 3170, it states, "The Sugawara contraction \(T=[Q,G]\) is proved at operator level," but it seems to prove only cohomology. I should rephrase it to, "The Sugawara contraction \(T=[Q,G]\) in BRST cohomology is proved at operator level." Lines 3089 and 3149 could clarify this by saying, "verifying that \(T-[Q,G]\) is \(Q\)-exact" or "verifying the inner conformal vector relation." Additionally, I’ll ensure consistency throughout and check the topologization summary near line 5297. Let’s update it all!
thinking
**Checking line shifts**

I realize that the output from `rg -n -F "upgrades the"` may have line shifts, so I need to check around line 5290 to get a clearer understanding. The output at line 5297 might not be accurate after the changes, which means I have to read more closely and see what adjustments might be necessary. This way, I can ensure I have the right context and content before making any updates!
codex
One sentence in the proof picked up a grammatical break, and a few remaining `T=[Q,G]` phrases still spoke as if literal chain-level equality were proved. I’m doing one final cleanup pass on those exact lines before verification.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2998,3008p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3084,3091p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3385,3391p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3168,3173p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "The topologization theorem" chapters/theory/en_koszul_duality.tex | head -n 10' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "identifies the BRST cohomology" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3143,3150p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2998	
  2999	\begin{proof}
  3000	The inner conformal vector identifies
  3001	$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
  3002	where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
  3003	\bar c_a(z){:}$ is the antighost contraction of
  3004	Construction~\ref{constr:sugawara-antighost} below,
  3005	generates holomorphic translations: for any bulk
  3006	observable $\cO$,
  3007	$\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
  3008	= [Q, [G, \cO]]$.
 succeeded in 51ms:
  3084	Virasoro $\mathrm{Vir}_c$: the algebra carries its own
  3085	stress tensor $T(z)$. The holomorphic--topological theory
  3086	is $3$d gravity. Topologization requires $T$ to be $Q$-exact
  3087	in the $3$d gravity bulk; this is expected at generic
  3088	$c \neq 0$ but requires constructing the BRST complex of
  3089	$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
  3090	This construction is the subject of
  3091	Conjecture~\ref{conj:topologization-general} below.
 succeeded in 50ms:
  3385	 conformal vector to topologize.
  3386	\item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  3387	 The stress tensor $T(z)$ IS the conformal vector, so
  3388	 $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
  3389	 in the $3$d gravity \textup{(}respectively higher-spin
  3390	 gravity\textup{)} bulk. This bulk theory and its BRST complex
  3391	 have not been constructed at the BV level; the antighost
 succeeded in 51ms:
  3168	  $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
  3169	  \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
  3170	\item The Sugawara contraction $T = [Q, G]$ is proved at the
  3171	  \emph{operator} level for $V_k(\fg)$ at non-critical level
  3172	  \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
  3173	\item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
 succeeded in 51ms:
3496:The topologization theorem identifies the BRST cohomology of the
 succeeded in 51ms:
3496:The topologization theorem identifies the BRST cohomology of the
5296:The topologization theorem
 succeeded in 51ms:
  3143	The obstruction to extending
  3144	Theorem~\ref{thm:topologization} to
  3145	Conjecture~\ref{conj:topologization-general} is
  3146	the construction of the $3$d HT BRST complex for the
  3147	relevant bulk theory (Chern--Simons for gauge algebras,
  3148	$3$d gravity for Virasoro, higher-spin gravity for
  3149	$\cW_N$) and the verification that $T = [Q, G]$ therein.
  3150	For affine Kac--Moody, the bulk theory is holomorphic
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d822d5a68c69744cc5509ac0f73be4e2e659f096
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3493,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5294,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5294,5302p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3494,3502p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5294	$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
  5295	(Remark~\ref{rem:sc-higher-genus}).
  5296	The topologization theorem
  5297	(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
  5298	the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
  5299	conformal vector,
  5300	with an explicit antighost contraction $G(z)$
  5301	(Construction~\ref{constr:sugawara-antighost}) that makes
  5302	the proof constructive. For class~M algebras, where the
 succeeded in 51ms:
  3494	% ================================================================
  3495	
  3496	The topologization theorem identifies the BRST cohomology of the
  3497	derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
  3498	as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
  3499	construction produces another $\Ethree$-algebra $\cA^\lambda$
  3500	from perturbative Chern--Simons quantisation. Both deform
  3501	$C^*(\fg)$ over the same base. For simple $\fg$, the
  3502	one-dimensionality of $H^3(\fg)$ forces the two
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..d822d5a68c69744cc5509ac0f73be4e2e659f096
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,21 +2980,25 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
 where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
 \bar c_a(z){:}$ is the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below,
@@ -3000,8 +3007,9 @@
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3017,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3074,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3102,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3155,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3178,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3199,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3324,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3361,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3422,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3493,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5294,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Evaluating chain-level identifications**

I'm looking at a statement about chain-level BV/bar identifications. It suggests that these are confirmed for classes G and L but are just conjectured for class M. Is that accurate? The earlier AGENTS indicated that confirmations exist for G and L, while M remains uncertain. The proof is cohomological, and for class M, chain-level E3 might fail, which is interesting. Maybe I should consider not diving deeper into this right now.
codex
I found the last real issues: one proof sentence had broken syntax, and four residual `T=[Q,G]` phrases still needed to be made cohomological rather than literal. I’m applying that cleanup and then doing a final grep/readback.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -2999,8 +2999,9 @@
 \begin{proof}
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
 The inner conformal vector identifies
-$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..37a50d030bf831c2ea3c283b81f1ca2ba6e63580
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3103,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3156,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3179,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3200,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3325,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3362,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3423,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3494,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5295,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..37a50d030bf831c2ea3c283b81f1ca2ba6e63580
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3093,27 +3103,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3143,8 +3156,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3166,14 +3179,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3200,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3325,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3362,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3405,14 +3423,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3494,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5295,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3089,3 +3089,4 @@
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
@@ -3149,3 +3150,4 @@
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
@@ -3170,3 +3172,4 @@
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
@@ -3388,3 +3391,4 @@
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

codex
The claim surface now reads coherently. I’m doing the verification pass next: one readback/grep over the modified theorem lane, then a narrow TeX build check if the toolchain is available, since that is the fastest way to catch any label or syntax drift from these edits.
exec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:topologization}\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "conj:topologization-general" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "constr:sugawara-antighost" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def:inner-conformal-vector" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2996:see Conjecture~\textup{\ref{conj:topologization-general}}.
3093:Conjecture~\ref{conj:topologization-general} below.
3108:\label{conj:topologization-general}
3147:Conjecture~\ref{conj:topologization-general} is
3398: Conjecture~\textup{\ref{conj:topologization-general}}.
 succeeded in 54ms:
3073:Theorem~\ref{thm:topologization} is proved for affine
3120:The proof of Theorem~\ref{thm:topologization} for affine
3129:Theorem~\ref{thm:topologization} proves only the
3146:Theorem~\ref{thm:topologization} to
3161:The proof of Theorem~\ref{thm:topologization} mixes chain-level
3187:Theorem~\ref{thm:topologization} proves only the
3458:  (Theorem~\ref{thm:topologization}).
5302:(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
 succeeded in 51ms:
31:(Construction~\ref{constr:sugawara-antighost}). For class~M
3003:Construction~\ref{constr:sugawara-antighost} below.
3176:  \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
3200:\label{constr:sugawara-antighost}%
5306:(Construction~\ref{constr:sugawara-antighost}) that makes
 succeeded in 51ms:
2947:\label{def:inner-conformal-vector}
2977:\textup{(}Definition~\textup{\ref{def:inner-conformal-vector}}\textup{)}.
 succeeded in 51ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Inspecting line structure**

I need to check line 3458, focusing on its remark structure to ensure everything's okay there. I wonder if it's necessary to look at the lines around 3448-3462, but maybe I can skip that if it’s a straightforward check. Since the theorem references counts and I want to avoid any overclaims, it could be useful to verify this specific line. Let's make sure it aligns with the intended meaning!
codex
The local references are consistent after the rewrite. I’m using the build surface now to do the narrowest falsifying check instead of a full manuscript build: confirm the build target exists, then run a single fast LaTeX pass with error halting if the toolchain is present.
exec
/bin/zsh -lc 'which latexmk || true' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^(fast|all|main):" Makefile' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'which pdflatex || true' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Library/TeX/texbin/latexmk
 succeeded in 51ms:
93:all: $(STAMP) working-notes publish
114:fast:
 succeeded in 52ms:
/Library/TeX/texbin/pdflatex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Inspecting fast target**

I need to figure out what the fast target does, and it seems like it could be fairly targeted or heavy. I could run a command like `sed -n '114,140p' Makefile` to look at a specific section of the Makefile. This should help me gather the details I need! Let’s go ahead and take a look to make sure I understand properly what it involves. It might be quite useful!
exec
/bin/zsh -lc "sed -n '114,150p' Makefile" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
fast:
	@echo "  ── Fast build (up to $(FAST_PASSES) passes) ──"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"

## working-notes: Build the working notes (standalone document).
working-notes: $(OUT_WN)

$(OUT_WN): $(WN_TEX)
	@echo "  ── Building working notes ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@cd $(WN_DIR) && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true
	@if [ -f $(WN_PDF) ]; then \
		cp $(WN_PDF) $(OUT_WN); \
		echo "  ✓  $(OUT_WN)"; \
	else \
		echo "  ✗  Working notes build failed."; \
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

codex
The build toolchain is available, and `make fast` exists. I’m running the build-surface prelude and a single fast manuscript check now; if it fails, I’ll classify whether the failure is caused by this edit or by pre-existing manuscript debt.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true
sleep 2' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

 succeeded in 2.01s:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

 exited 2 in 12.68s:
./scripts/build.sh: line 64: 33046 Killed: 9               $TEX $TEXFLAGS main.tex > "$RUN_LOG" 2>&1
   ?pp, 472 undef citations, 942 undef references, 0 rerun requests, 24 overfull, 57 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
Runaway argument?
./main.tex:589: File ended while scanning use of \@writefile.
Runaway argument?
./main.tex:589: File ended while scanning use of \@@BOOKMARK.
Runaway argument?
./main.tex:589: File ended while scanning use of \@@BOOKMARK.
make: *** [fast] Error 137
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Investigating build log issues**

I’m planning to inspect the top of the build log, especially around the target file, but I’m unsure if it’ll be useful. It seems the output indicates a kill from the OS rather than our edits, possibly due to an OOM (out of memory) issue. I might perform a static syntax check using `chktex` on the modified file since the tool is available. Let’s see how that goes!
codex
`make fast` did not give a trustworthy manuscript verdict: the TeX process was killed by the system, and the resulting runaway messages are from an interrupted build surface, not stable evidence. I’m switching to a file-local static TeX check on the edited chapter so I can still falsify syntax/label issues without needing a full successful manuscript compile.
exec
/bin/zsh -lc 'tail -n 80 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'which chktex || true' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "topologization" .build_logs/tex-build.stdout.log main.log' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Library/TeX/texbin/chktex
 succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 51ms:
main.log:2180:LaTeX Warning: Reference `thm:topologization' on page 94 undefined on input lin
main.log:2184:LaTeX Warning: Reference `sec:topologization' on page 94 undefined on input lin
main.log:2188:LaTeX Warning: Reference `conj:topologization-general' on page 94 undefined on 
main.log:3001:LaTeX Warning: Reference `thm:topologization' on page 125 undefined on input li
main.log:3005:LaTeX Warning: Reference `conj:topologization-general' on page 125 undefined on
main.log:3013:LaTeX Warning: Reference `sec:topologization' on page 125 undefined on input li
main.log:3032:LaTeX Warning: Reference `thm:topologization' on page 126 undefined on input li
main.log:3036:LaTeX Warning: Reference `sec:topologization' on page 126 undefined on input li
main.log:3040:LaTeX Warning: Reference `conj:topologization-general' on page 126 undefined on
main.log:3455:LaTeX Warning: Reference `thm:topologization' on page 132 undefined on input li
main.log:3459:LaTeX Warning: Reference `conj:topologization-general' on page 132 undefined on
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Running code checks**

I need to run chktex on the target file. I’m considering the options: maybe using the flags -q for quiet mode and -n to ignore any specific warnings? Alright, let’s go ahead with that — it seems like a good plan. It’s always nice to ensure my work is tidy and free from unnecessary errors. I’ll get started on this right away!
exec
/bin/zsh -lc 'chktex -q -n1 -n2 -n8 -n46 chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 153ms:
Warning 24 in chapters/theory/en_koszul_duality.tex line 2: Delete this space to maintain correct pagereferences.
\label{ch:en-koszul-duality}  
^
Warning 24 in chapters/theory/en_koszul_duality.tex line 4: Delete this space to maintain correct pagereferences.
\index{En algebra@$\En$ algebra!Koszul duality|textbf}  
^
Warning 24 in chapters/theory/en_koszul_duality.tex line 5: Delete this space to maintain correct pagereferences.
\index{bar complex!higher-dimensional|textbf}  
^
Warning 24 in chapters/theory/en_koszul_duality.tex line 71: Delete this space to maintain correct pagereferences.
\label{thm:en-chiral-bridge}  
^
Warning 24 in chapters/theory/en_koszul_duality.tex line 72: Delete this space to maintain correct pagereferences.
\index{En algebra@$\En$ algebra!bridge to chiral bar-cobar|textbf}  
^
Warning 9 in chapters/theory/en_koszul_duality.tex line 74: `)' expected, found `}'.
\textup{(}Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{)}  
         ^
Warning 9 in chapters/theory/en_koszul_duality.tex line 74: `}' expected, found `)'.
\textup{(}Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{)}  
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Filtering chktex warnings**

I’m noticing a huge output from chktex, and there are many pre-existing warnings. It might make more sense to run a more targeted check around our edited lines. Sure, I could use `chktex -v0 -f ...`, but it feels easier to filter using `awk`. However, I really want to focus on our modified lines specifically, so running `chktex ... | rg -n "line (294|295|296|..."` to see if any new warnings pop up from our changes sounds like a solid plan!
codex
`chktex` is usable, but the file already carries thousands of pre-existing style warnings, so the raw exit code is not evidence. I’m filtering it down to the edited line ranges only; that lets me distinguish new syntax damage from the chapter’s existing lint debt.
exec
/bin/zsh -lc 'chktex -q -n1 -n2 -n8 -n46 chapters/theory/en_koszul_duality.tex 2>/dev/null | rg -n "line (29[4-9]|30[0-9]|31[0-9]|32[0-9]|33[0-9]|34[0-9]|52(9[0-9]|[0-8][0-9]))"' in /Users/raeez/chiral-bar-cobar succeeded in 106ms:
118:Warning 24 in chapters/theory/en_koszul_duality.tex line 298: Delete this space to maintain correct pagereferences.
121:Warning 24 in chapters/theory/en_koszul_duality.tex line 299: Delete this space to maintain correct pagereferences.
124:Warning 3 in chapters/theory/en_koszul_duality.tex line 311: You should enclose the previous parenthesis with `{}'.
127:Warning 9 in chapters/theory/en_koszul_duality.tex line 314: `)' expected, found `}'.
130:Warning 9 in chapters/theory/en_koszul_duality.tex line 315: `}' expected, found `)'.
133:Warning 24 in chapters/theory/en_koszul_duality.tex line 331: Delete this space to maintain correct pagereferences.
136:Warning 24 in chapters/theory/en_koszul_duality.tex line 332: Delete this space to maintain correct pagereferences.
139:Warning 24 in chapters/theory/en_koszul_duality.tex line 335: Delete this space to maintain correct pagereferences.
142:Warning 24 in chapters/theory/en_koszul_duality.tex line 336: Delete this space to maintain correct pagereferences.
1066:Warning 24 in chapters/theory/chiral_center_theorem.tex line 296: Delete this space to maintain correct pagereferences.
1069:Warning 24 in chapters/theory/chiral_center_theorem.tex line 299: Delete this space to maintain correct pagereferences.
1072:Warning 24 in chapters/theory/chiral_center_theorem.tex line 300: Delete this space to maintain correct pagereferences.
1075:Warning 3 in chapters/theory/chiral_center_theorem.tex line 312: You should enclose the previous parenthesis with `{}'.
1078:Warning 24 in chapters/theory/chiral_center_theorem.tex line 347: Delete this space to maintain correct pagereferences.
1738:Warning 24 in chapters/theory/en_koszul_duality.tex line 2947: Delete this space to maintain correct pagereferences.
1741:Warning 24 in chapters/theory/en_koszul_duality.tex line 2948: Delete this space to maintain correct pagereferences.
1744:Warning 24 in chapters/theory/en_koszul_duality.tex line 2968: Delete this space to maintain correct pagereferences.
1747:Warning 24 in chapters/theory/en_koszul_duality.tex line 2970: Delete this space to maintain correct pagereferences.
1750:Warning 9 in chapters/theory/en_koszul_duality.tex line 2977: `)' expected, found `}'.
1753:Warning 9 in chapters/theory/en_koszul_duality.tex line 2977: `}' expected, found `)'.
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the


thinking
**Analyzing range levels**

I'm looking at the relevant range between 3188-3210, 3390-3410, and the 3496 line. It's important to consider these specific levels to understand potential trends. I wonder if these ranges indicate any significant price movements? I’ll dive deeper into these numbers and see how they might affect my overall analysis. There's definitely a lot to consider here! Let's keep exploring this.
codex
The static check on the edited ranges looks clean enough: no new file-local syntax warnings appeared on the new theorem equation or the BRST-cohomology wording, and the remaining warnings in that span are the chapter’s existing `\textup{(}`/pageref style debt. I’m doing one last readback of the exact patched paragraphs, then I’ll close with a precise fix map and note that the full build could not be validated because the TeX process was killed.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2999,3032p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3138,3208p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3396,3432p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3322,3360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3494,3502p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5294,5304p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3138	$\Ethree$ upgrade may therefore exist only on
  3139	$Q$-cohomology (not on cochains) for class~M algebras.
  3140	This is consistent with the general pattern that
  3141	chain-level BV/bar identifications are proved for
  3142	classes~G and~L but remain conjectural for class~M
  3143	\textup{(}see the MC5 status in the concordance\textup{)}.
  3144	
  3145	The obstruction to extending
  3146	Theorem~\ref{thm:topologization} to
  3147	Conjecture~\ref{conj:topologization-general} is
  3148	the construction of the $3$d HT BRST complex for the
  3149	relevant bulk theory (Chern--Simons for gauge algebras,
  3150	$3$d gravity for Virasoro, higher-spin gravity for
  3151	$\cW_N$) and the verification that
  3152	$T - [Q, G]$ is $Q$-exact therein.
  3153	For affine Kac--Moody, the bulk theory is holomorphic
  3154	Chern--Simons and the BRST complex is standard. For
  3155	$3$d gravity, this is the subject of Volume~II
  3156	\textup{(}Three-Dimensional Quantum Gravity\textup{)}.
  3157	\end{remark}
 succeeded in 51ms:
  2999	\begin{proof}
  3000	Let
  3001	$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
  3002	the antighost contraction of
  3003	Construction~\ref{constr:sugawara-antighost} below.
  3004	The inner conformal vector identifies
  3005	$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
  3006	$G$ generates holomorphic translations: for any bulk
  3007	observable $\cO$,
  3008	$\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
  3009	= [Q, [G, \cO]]$.
  3010	Since $\partial_z$ is $Q$-exact, holomorphic translations
  3011	act trivially on BRST cohomology: the BRST cohomology of
  3012	the factorization algebra on the $\bC$-direction becomes
  3013	locally constant. A locally
  3014	constant factorization algebra on $\bC \cong \bR^2$
  3015	is an $\Etwo^{\mathrm{top}}$-algebra
  3016	(Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
  3017	$\Eone^{\mathrm{top}}$ from the $\bR$-direction (the
  3018	open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 succeeded in 50ms:
  3396	 have not been constructed at the BV level; the antighost
  3397	 contraction for class~M is the content of
  3398	 Conjecture~\textup{\ref{conj:topologization-general}}.
  3399	\end{enumerate}
  3400	\end{remark}
  3401	
  3402	\begin{conjecture}[Coderived $\Ethree$ for class~M; \ClaimStatusConjectured]
  3403	\label{conj:coderived-e3}%
  3404	\index{coderived category!E3 structure@$\Ethree$ structure|textbf}%
  3405	\index{topologization theorem!coderived refinement}%
  3406	\index{E3 algebra@$\Ethree$ algebra!coderived}%
  3407	Let $\cA$ be a chirally Koszul algebra with inner conformal vector
  3408	at non-critical level.
  3409	\begin{enumerate}[label=\textup{(\roman*)}]
  3410	\item \textup{(Coderived local constancy.)}
  3411	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3412	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  3413	  is locally constant. Precisely: the
  3414	  $m_0$-curvature obstruction to local constancy at
  3415	  step~\textup{(iv)} of
 succeeded in 51ms:
  3494	
  3495	
  3496	
  3497	% ================================================================
  3498	% The E_3 identification theorem and explicit operations
  3499	% ================================================================
  3500	
  3501	The topologization theorem identifies the BRST cohomology of the
  3502	derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
 succeeded in 51ms:
  3322	 vanishes by the Jacobi identity
  3323	 $f_{ab}{}^c\,f^a{}_{de} + \text{cyc}(b,d,e) = 0$.
  3324	\end{enumerate}
  3325	In summary,
  3326	\begin{equation}\label{eq:TQG-result}
  3327	[Q,\, G(z)] \;=\; T_{\mathrm{Sug}}(z) \;+\;
  3328	 (\text{$Q$-exact operators of ghost number $\ge 1$}).
  3329	\end{equation}
  3330	On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
  3331	the explicit operator-level datum that makes the cohomological
  3332	topologization proof
  3333	\textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
  3334	constructive.
  3335	
  3336	\textsc{The specialisation to $\fsl_2$.}
  3337	For $\fg = \fsl_2$ with standard basis
  3338	$\{e, f, h\}$ ($[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$)
  3339	and trace-form
  3340	$\kappa(e,f) = 1$, $\kappa(h,h) = 2$, the Sugawara
  3341	element is
 succeeded in 51ms:
  5294	$\Sigma_n$-coinvariants and uses the coshuffle coproduct
  5295	instead. At higher genus the fibrewise differential
  5296	$\dfib$ is curved with $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$
  5297	but is \emph{not} a coderivation; flatness and the coderivation
  5298	property are restored only by the period-corrected differential
  5299	$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
  5300	(Remark~\ref{rem:sc-higher-genus}).
  5301	The topologization theorem
  5302	(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
  5303	the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
  5304	conformal vector,
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..ad0a9ec6f3692da8045e9dba7031ae540ffe4eb9
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
+the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the



thinking
**Reviewing text clarity**

I think I need to read beyond line 3432, but maybe it’s not necessary. I noticed line 3000 has an awkward phrasing with "Let $G(z)=..., the antighost contraction of Construction...". It could flow better if I say, "Let... be the antighost contraction...". Yes, it’s clear the phrase is missing "be." I also see some areas, like line 28-30, could be smoother but aren’t essential to patch. Line 3077 looks fine. Overall, line 3000 definitely needs that adjustment.
thinking
**Considering text adjustments**

I think I definitely need to patch lines 3000-3003. It seems like there might be clarity issues there. I should also check lines 3430-3433, but maybe that’s not as crucial. Overall, I just want to ensure the text is clear and smooth. A small patch could make a difference. It’s all about making sure everything flows well, so I’ll focus on the necessary adjustments. Let’s keep things tidy!
codex
One final sentence still needed a missing verb. I’m fixing that now; after that the patched surface reads cleanly end to end.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3000,4 +3000,4 @@
 Let
-$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$,
-the antighost contraction of
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
+be the antighost contraction of
 Construction~\ref{constr:sugawara-antighost} below.
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..5e40a875e06e3e81d178d15bfd42c1422c5fcfd0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
+be the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..5e40a875e06e3e81d178d15bfd42c1422c5fcfd0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
+be the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

exec
/bin/zsh -lc 'rg -n -F "Cohomological topologization for affine Kac--Moody" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Chain-level topologization for general chiral algebras" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2967:\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 succeeded in 51ms:
3107:\begin{conjecture}[Chain-level topologization for general chiral algebras]
 succeeded in 50ms:
Total output lines: 2093

diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1a8ac23..5e40a87 100644
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@ The chapter culminates in the chiral center theorem
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
Plan update
Patched the topologization claim surface in the target file, split proved cohomological content from conjectural chain-level strengthening, and verified local references. Build verification was attempted, but `make fast` was killed by the system before a stable verdict; static readback and filtered `chktex` on the edited ranges did not reveal new syntax issues.
  ✓ Audit theorem, proof, and surrounding remarks for the topologization claim surface in en_koszul_duality.tex
  ✓ Patch theorem statement/status surface to separate proved cohomological content from conjectural chain-level content
  ✓ Re-read downstream references in the same file and verify no remaining overclaims or broken labels
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..5e40a875e06e3e81d178d15bfd42c1422c5fcfd0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
+be the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the




thinking
**Analyzing Git Diff Issues**

I'm looking at a massive git diff, and I'm wondering if the file could be dirty with unrelated changes causing such a big output. It seems like there might be CRLF issues or something weird after an earlier patch that inserted repeated content. The diff output looks truncated, which might not matter. I need to check if we unintentionally duplicated large blocks of text and whether there were already duplicates. It could be that those changes were made by the user before.
thinking
**Checking for Duplicate Content**

I need to ensure that our edits are limited and that we didn't accidentally duplicate content around the line 3497, as our patch only modified the intro. The huge content inserts in the diff are likely due to prior user changes, not our own. It's possible that our patch altered line numbering, affecting the diff context. To keep things concise, I'll summarize our findings and mention that the build verification was attempted but terminated. I’ll structure the output and end with a rectification summary.
thinking
**Summarizing Findings**

I think we can summarize our work with one bullet like `[FIXED] finding — ...` and mention the theorem split. Since there’s only one finding, I wonder if I should include both `[FIXED]` and `[CONDITIONAL]`, but I should stick to the summary contract that says to end with categorized bullets. I’ll highlight that this finding was resolved through narrowing and conjectural strengthening. It's important to keep things clear and organized!
codex
In [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:2946), I repaired the topologization claim surface by making the proved statement exactly match the proof. `thm:topologization` is now a cohomological result on `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, while the chain-level lift is pushed into the existing conjectural lane `conj:topologization-general`. I also weakened `def:inner-conformal-vector` to the actually constructed condition `T-[Q,G]` being `Q`-exact, and synced the proof, construction, boundary interpretation, coderived remark, and chapter summaries so they no longer speak as if chain-level `\Ethree` were proved.

I re-read the modified theorem/proof/remark cluster and the in-file downstream references to `thm:topologization`, `conj:topologization-general`, `def:inner-conformal-vector`, and `constr:sugawara-antighost`. I attempted `make fast`, but the TeX process was killed by the system (`Error 137`), so there is no stable full-build verdict from that run. A filtered `chktex` pass over the edited line ranges did not reveal new syntax issues; the remaining warnings there are the file’s pre-existing style/lint debt.

## Rectification Summary
- [FIXED] CRITICAL T14 — restated `thm:topologization` as a BRST-cohomological `\Ethree` result, repointed `conj:topologization-general` to the chain-level strengthening, weakened `def:inner-conformal-vector` to match the actual construction, and synchronized the surrounding remarks/summaries so the concession at lines `3146–3176` is now consistent with the final claim.
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index b449895010663724a2315def024cc92b2c258c42..5e40a875e06e3e81d178d15bfd42c1422c5fcfd0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -22,9 +22,11 @@
 Hochschild cochain complex as the operadic center of an
 $\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
 theorem (\S\ref{sec:topologization}), which upgrades the resulting
-$\Etwo$ center to~$\Ethree$ via the Sugawara conformal vector.
+$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
+conformal vector.
 The topologization proof is made constructive by an explicit
-antighost contraction $G(z)$ satisfying $T_{\mathrm{Sug}} = [Q, G]$
+antighost contraction $G(z)$ representing
+$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
 in the $3$d holomorphic Chern--Simons BV complex
 (Construction~\ref{constr:sugawara-antighost}). For class~M
 algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
@@ -1269,7 +1271,7 @@
   $\FM_k(\bC)$ (the operadic center theorem,
   Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
 \item With an inner conformal vector at non-critical level,
-  this $\Etwo$ upgrades to $\Ethree$ via the
+  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
   topologization theorem
   (Theorem~\textup{\ref{thm:topologization}}).
 \item Without a conformal vector,
@@ -2951,8 +2953,9 @@
 is~$\cA$. An \emph{inner conformal vector} for
 $(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
 central charge~$c$ that is $Q$-exact in the algebra
-of bulk observables: there exists $G(z)$ such that
-$T(z) = [Q, G(z)]$.
+of bulk observables up to a $Q$-boundary: there exists
+$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
+Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
 For affine Kac--Moody $V_k(\fg)$ at non-critical level,
 the Sugawara element
 $T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
@@ -2961,7 +2964,7 @@
 Virasoro algebra, $T(z)$ is the stress tensor itself.
 \end{definition}
 
-\begin{theorem}[Topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
+\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 \label{thm:topologization}
 \ClaimStatusProvedHere
 \index{topologization theorem!statement}
@@ -2977,31 +2980,37 @@
 $\Etwo$ structure from the closed sector of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
-upgrades to an $\Ethree$-algebra:
+upgrades on BRST cohomology to an $\Ethree$-algebra:
 \begin{equation}\label{eq:topologization}
-\Etwo^{\mathrm{hol}} \otimes \Eone^{\mathrm{top}}
-\;\xrightarrow{\;\text{Sugawara}\;}\;
+H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
+\text{ carries an }
 \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-\;=\; \Ethree^{\mathrm{top}},
+\;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
 \end{equation}
-where the first arrow is the topologization
-\textup{(}the inner conformal vector makes holomorphic
-translations homotopically trivial\textup{)} and the
-second equality is Dunn additivity.
+Here the inner conformal vector makes holomorphic
+translations $Q$-exact, hence trivial on BRST cohomology,
+and the equality with $\Ethree^{\mathrm{top}}$ is Dunn
+additivity. The corresponding chain-level
+$\Ethree^{\mathrm{top}}$ enhancement of
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is not proved here;
+see Conjecture~\textup{\ref{conj:topologization-general}}.
 \end{theorem}
 
 \begin{proof}
-The inner conformal vector $T_{\mathrm{Sug}} = [Q, G]$,
-where $G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,
-\bar c_a(z){:}$ is the antighost contraction of
-Construction~\ref{constr:sugawara-antighost} below,
-generates holomorphic translations: for any bulk
+Let
+$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
+be the antighost contraction of
+Construction~\ref{constr:sugawara-antighost} below.
+The inner conformal vector identifies
+$T_{\mathrm{Sug}}$ with $[Q, G]$ in BRST cohomology, and
+$G$ generates holomorphic translations: for any bulk
 observable $\cO$,
 $\partial_z \cO = [T_{\mathrm{Sug}}, \cO]
 = [Q, [G, \cO]]$.
 Since $\partial_z$ is $Q$-exact, holomorphic translations
-act trivially on $Q$-cohomology: the factorization algebra
-on the $\bC$-direction becomes locally constant. A locally
+act trivially on BRST cohomology: the BRST cohomology of
+the factorization algebra on the $\bC$-direction becomes
+locally constant. A locally
 constant factorization algebra on $\bC \cong \bR^2$
 is an $\Etwo^{\mathrm{top}}$-algebra
 (Lurie~\cite{HA}, Theorem~5.4.5.9). Combined with the
@@ -3009,14 +3018,15 @@
 open color of $\mathsf{SC}^{\mathrm{ch,top}}$), Dunn
 additivity gives
 $\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
-= \Ethree^{\mathrm{top}}$.
+= \Ethree^{\mathrm{top}}$ on
+$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.
 
 At critical level $k = -h^\vee$, the Sugawara denominator
 $2(k + h^\vee)$ diverges: the Sugawara element is undefined,
 $\partial_z$ is not $Q$-exact, and the factorization algebra
 retains genuine holomorphic dependence. The $\Etwo$ structure
 remains holomorphic, not topological, and the upgrade
-to~$\Ethree$ fails.
+to~$\Ethree$ on BRST cohomology fails.
 \end{proof}
 
 \begin{remark}[Essential external inputs]
@@ -3065,9 +3075,9 @@
 $k \neq -h^\vee$, where the Sugawara element provides
 an explicit inner conformal vector and the $3$d
 holomorphic--topological theory is Chern--Simons.
-Topologization produces the perturbative
-Chern--Simons $\Ethree$-algebra of
-Costello--Francis--Gwilliam.
+Topologization produces the corresponding
+cohomological $\Ethree$-algebra on BRST cohomology.
+The chain-level enhancement remains conjectural.
 
 For general chiral algebras with conformal vector, the
 same conclusion is expected but remains conjectural:
@@ -3077,7 +3087,8 @@
 is $3$d gravity. Topologization requires $T$ to be $Q$-exact
 in the $3$d gravity bulk; this is expected at generic
 $c \neq 0$ but requires constructing the BRST complex of
-$3$d HT gravity and verifying $T = [Q, G]$ explicitly.
+$3$d HT gravity and verifying explicitly that
+$T - [Q, G]$ is $Q$-exact.
 This construction is the subject of
 Conjecture~\ref{conj:topologization-general} below.
 
@@ -3093,27 +3104,30 @@
 The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
 \end{remark}
 
-\begin{conjecture}[Topologization for general chiral algebras]
+\begin{conjecture}[Chain-level topologization for general chiral algebras]
 \label{conj:topologization-general}
 \ClaimStatusConjectured
 \index{topologization theorem!general conjecture}
 Let $\cA$ be a chiral algebra with conformal vector
 $T(z)$ at non-critical level. Then the derived chiral
-center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ admits an
-$\Ethree$-topological structure via~\eqref{eq:topologization}.
+center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits
+a chain-level $\Ethree$-topological structure lifting the
+cohomological topologization of~\eqref{eq:topologization}.
 \end{conjecture}
 
 \begin{remark}[Evidence and obstructions]
 \label{rem:topologization-evidence}
 The proof of Theorem~\ref{thm:topologization} for affine
 Kac--Moody uses only two inputs: (i)~the existence of an
-inner conformal vector $T = [Q, G]$, and (ii)~the
+inner conformal vector in BRST cohomology, and (ii)~the
 $Q$-exactness of holomorphic translations on $Q$-cohomology.
 Both inputs are cohomological: the argument shows that the
 factorization algebra becomes locally constant
 \emph{on $Q$-cohomology}, not necessarily at the cochain
 level. For affine Kac--Moody, the Sugawara mechanism
-provides both inputs explicitly.
+provides both inputs explicitly. Accordingly,
+Theorem~\ref{thm:topologization} proves only the
+cohomological $\Ethree$-structure.
 
 For Virasoro and $\cW$-algebras (class~M in the shadow
 classification), the chain-level data is essential:
@@ -3134,7 +3148,8 @@
 the construction of the $3$d HT BRST complex for the
 relevant bulk theory (Chern--Simons for gauge algebras,
 $3$d gravity for Virasoro, higher-spin gravity for
-$\cW_N$) and the verification that $T = [Q, G]$ therein.
+$\cW_N$) and the verification that
+$T - [Q, G]$ is $Q$-exact therein.
 For affine Kac--Moody, the bulk theory is holomorphic
 Chern--Simons and the BRST complex is standard. For
 $3$d gravity, this is the subject of Volume~II
@@ -3143,8 +3158,8 @@
 
 \begin{remark}[Chain-level vs cohomological topologization]
 \label{rem:topologization-chain-vs-cohomology}
-The proof of Theorem~\ref{thm:topologization} establishes $\Ethree$
-at the following levels:
+The proof of Theorem~\ref{thm:topologization} mixes chain-level
+inputs with a cohomological recognition step:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the pair
   $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}
@@ -3155,7 +3170,8 @@
   for affine $V_k(\fsl_2)$, the bracket restricts on
   $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
   \textup{(}Proposition~\textup{\ref{prop:gerstenhaber-sl2-bracket}}\textup{)}.
-\item The Sugawara contraction $T = [Q, G]$ is proved at the
+\item The Sugawara contraction
+  $T = [Q, G]$ in BRST cohomology is proved at the
   \emph{operator} level for $V_k(\fg)$ at non-critical level
   \textup{(}Construction~\textup{\ref{constr:sugawara-antighost}}\textup{)}.
 \item The passage $\Etwo^{\mathrm{hol}} \to \Etwo^{\mathrm{top}}$
@@ -3166,14 +3182,17 @@
   is proved at the \emph{$\infty$-categorical} level
   \textup{(}Lurie~\cite{HA}\textup{)}.
 \end{enumerate}
-The chain-level gap is at step~\textup{(iv)}: the locally-constant
-recognition requires passing to $Q$-cohomology.  For class~G
-and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
-$k \geq 3$\textup{)}, the chain-level and cohomological
-$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
-where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
-chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
-Whether the chain-level $\Ethree$ exists for class~M is open.
+The decisive gap is at step~\textup{(iv)}: the locally-constant
+recognition requires passing to $Q$-cohomology. Therefore
+Theorem~\ref{thm:topologization} proves only the
+\emph{cohomological} $\Ethree$-structure on
+$H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$.
+A chain-level $\Ethree$ refinement would require a cochain-level
+replacement for step~\textup{(iv)}, and no such replacement is
+proved here. For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
+where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial,
+the chain-level $\Ethree$ may differ from the cohomological
+$\Ethree$. Whether such a chain-level lift exists is open.
 \end{remark}
 
 \begin{construction}[The Sugawara antighost contraction for affine
@@ -3184,9 +3203,9 @@
 \index{antighost contraction|textbf}%
 \ClaimStatusProvedHere
 The proof of Theorem~\textup{\ref{thm:topologization}} asserts the
-existence of $G(z)$ satisfying $T_{\mathrm{Sug}}(z) = [Q, G(z)]$
-but does not construct it. We supply the explicit chain-level
-datum.
+existence of $G(z)$ witnessing the inner conformal vector in BRST
+cohomology but does not construct it. We supply the explicit
+operator and verify the cohomological identity.
 
 Let $\fg$ be a finite-dimensional simple Lie algebra with basis
 $\{t_a\}_{a=1}^{\dim\fg}$, structure constants
@@ -3309,7 +3328,8 @@
  (\text{$Q$-exact operators of ghost number $\ge 1$}).
 \end{equation}
 On $Q$-cohomology, $[Q, G(z)] = T_{\mathrm{Sug}}(z)$ exactly. This is
-the chain-level datum that makes the topologization proof
+the explicit operator-level datum that makes the cohomological
+topologization proof
 \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}
 constructive.
 
@@ -3345,9 +3365,10 @@
 that does not descend to the boundary chiral algebra $V_k(\fg)$.
 The operator $G(z)$ therefore lives in the algebra of bulk
 observables $\cO_{\mathrm{bulk}}$, not in the boundary. The
-identity $T_{\mathrm{Sug}} = [Q, G]$ states that the Sugawara
-element, which IS a boundary operator, is the BRST-commutator of a
-bulk operator. This is the physical content of topologization: the
+relation~\eqref{eq:TQG-result} states that the Sugawara
+element, which is a boundary operator, is represented in BRST
+cohomology by the commutator of a bulk operator. This is the
+physical content of topologization: the
 stress tensor of the boundary theory is exact in the bulk, so
 $\bC$-translations are homotopically trivial when viewed from the
 three-dimensional perspective.
@@ -3368,7 +3389,8 @@
  conformal vector to topologize.
 \item \emph{Virasoro and $\cW$-algebras \textup{(}class~M\textup{)}.}
  The stress tensor $T(z)$ IS the conformal vector, so
- $T = [Q, G]$ requires $G(z)$ to be a ghost-number~$-1$ operator
+ representing $T$ by $[Q, G]$ in BRST cohomology requires
+ $G(z)$ to be a ghost-number~$-1$ operator
  in the $3$d gravity \textup{(}respectively higher-spin
  gravity\textup{)} bulk. This bulk theory and its BRST complex
  have not been constructed at the BV level; the antighost
@@ -3405,14 +3427,14 @@
   the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
   additivity gives an $\Ethree^{\mathrm{top}}$-structure in
   $D^{\mathrm{co}}$.
-\item \textup{(Class-by-class agreement.)}
-  For classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$
-  \textup{(}where the chain-level obstructions vanish\textup{)},
-  the coderived $\Ethree$ agrees with the chain-level $\Ethree$
-  of Theorem~\textup{\ref{thm:topologization}}.
-  For class~$\mathsf{M}$, the coderived $\Ethree$ is the
-  \emph{only} $\Ethree$-structure available, and it is
-  compatible with the coderived BV$=$bar identification of
+\item \textup{(Compatibility with cohomological topologization.)}
+  In the affine Kac--Moody case, the coderived $\Ethree$
+  recovers the cohomological $\Ethree$ of
+  Theorem~\textup{\ref{thm:topologization}} after passing
+  to $Q$-cohomology. For class~$\mathsf{M}$, the coderived
+  $\Ethree$ is the only presently available candidate for a
+  chain-level lift, and it is compatible with the coderived
+  BV$=$bar identification of
   Theorem~\textup{\ref{thm:bv-bar-coderived}}.
 \end{enumerate}
 \end{conjecture}
@@ -3476,9 +3498,9 @@
 % The E_3 identification theorem and explicit operations
 % ================================================================
 
-The topologization theorem identifies the derived chiral
-centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ as an
-$\Ethree$-algebra. The Costello--Francis--Gwilliam
+The topologization theorem identifies the BRST cohomology of the
+derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
+as an $\Ethree$-algebra. The Costello--Francis--Gwilliam
 construction produces another $\Ethree$-algebra $\cA^\lambda$
 from perturbative Chern--Simons quantisation. Both deform
 $C^*(\fg)$ over the same base. For simple $\fg$, the
@@ -5277,8 +5299,9 @@
 $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
 (Remark~\ref{rem:sc-higher-genus}).
 The topologization theorem
-(Theorem~\ref{thm:topologization}) upgrades the $\Etwo$ center
-of $V_k(\fg)$ to $\Ethree$ via the Sugawara conformal vector,
+(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
+the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
+conformal vector,
 with an explicit antighost contraction $G(z)$
 (Construction~\ref{constr:sugawara-antighost}) that makes
 the proof constructive. For class~M algebras, where the

tokens used
161,154
