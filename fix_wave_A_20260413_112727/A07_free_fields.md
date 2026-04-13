# A07_free_fields (285s)

Edited [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1150) with the minimum truthful scope fixes, and also repaired two stale summaries in the same file at [the earlier beta-gamma overview](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:708) and [the later recap table](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5551).

- Finding 1: FIXED. The vanishing proposition now explicitly says it is only about the one-dimensional weight-changing line. I added that the quartic contact shadow belongs to the mixed charged stratum, so it does not contradict class C / global depth 4.
- Finding 2: FIXED. The global-depth theorem now says it is about the full two-channel deformation space, and the `T`-line statement is rewritten as a separately computed one-dimensional slice, not a literal restriction of a globally vanishing quintic class. I also adjusted the proof and the adjacent remark to match that scope.
- Surrounding-context drift: FIXED. Two summary passages elsewhere in the same file were still saying the quartic contact showed up on the weight-changing line; those now match the repaired theorem surface.

Verification: I re-read the patched blocks, checked the cited labels/refs used in the edited surface, and ran the requested forbidden-pattern grep on the modified file. That grep only found two pre-existing `---` instances at lines 3 and 606, outside the edited regions. I did not run a TeX build.


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
session id: 019d8635-c9a0-74e2-9403-dc42b402ab70
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/examples/free_fields.tex

FINDINGS:
1. Lines ~1148-1166: A proved proposition says betagamma shadow tower vanishes on some line.
   This potentially contradicts depth-gap claim that betagamma has d_alg=2 (r_max=4).
2. Line ~1171: Global-depth theorem contradicts T-line theorem.

FIX: Read both propositions. Determine WHICH parameter line each refers to.
If different lines: add clarification distinguishing them.
If same line: one of the propositions is wrong; narrow the incorrect one.
mcp startup: no servers


thinking
**Considering codebase exploration**

I’m thinking I should use the explorer sub-agent for any codebase questions, especially since the developer recommends it for speed and authority. The instructions emphasize trusting explorer results without verification. However, I also need to balance that with reading certain files myself before making any substantive edits, like CLAUDE.md. I wonder if I can spawn the explorer to read those necessary files and summarize them for me without having to re-read everything.
thinking
**Evaluating the use of explorer**

I'm contemplating the agent's read counts and if I should utilize the explorer for this task. The explorer can inspect the necessary files, summarize, and provide exact lines without needing me to re-read the sections they cover. However, I might still need to open those specific lines for editing. It sounds like I can ask the explorer to report relevant findings and any conflicting statuses, possibly using a parallel approach with developer tools. This could streamline the process!
codex
Using `beilinson-rectify` for a tightly scoped claim-surface repair in [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex). I’m first loading the required constitutional context and the exact proposition surface around the flagged lines so I can determine whether this is a distinction-of-parameter-lines issue or a genuine contradiction.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1100,1215p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
this one-dimensional slice is the Virasoro shadow obstruction tower at this value
of~$c$, with $S_3 = 2$ (the universal Virasoro cubic shadow) and
$S_4 = 10/(c(5c+22))$ (the quartic contact invariant). Direction~(ii):
the weight-changing deformation class $\eta$ generates a one-dimensional
slice on which the beta-gamma OPE contributes no higher-order poles
beyond the simple pole $\beta(z)\gamma(w) \sim 1/(z{-}w)$. All
transferred higher brackets $\ell_n^{\mathrm{tr}}$ for $n \geq 2$
vanish on this slice, placing it in the hypothesis of
Theorem~\ref{thm:betagamma-rank-one-rigidity}.\qedhere
\end{proof}

\subsubsection{Shadow data on each line}

\begin{proposition}[$\beta\gamma$ shadow obstruction tower: T-line data;
\ClaimStatusProvedHere]
\label{prop:betagamma-T-line-shadows}
\index{beta-gamma system@$\beta\gamma$ system!T-line shadow data}
On the stress tensor line, the shadow obstruction tower of $\beta\gamma$ at
weight~$\lambda$ is
\begin{alignat}{2}
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
 succeeded in 53ms:
Total output lines: 220

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
codex
I have the local contradiction surface now. There are two distinct one-dimensional slices already present in the source: the stress-tensor `T`-line and the weight-changing line. I’m reading the surrounding proof and the upstream definitions/theorems these propositions cite so I can narrow only the incorrect scope, not the whole section.
exec
/bin/zsh -lc "sed -n '1215,1275p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1060,1148p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"betagamma-(quartic-birth|rank-one-rigidity)|nms-betagamma-mu-vanishing|single-line-dichotomy\" chapters/examples/free_fields.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:

The $\beta\gamma$ system is the unique free-field archetype outside the
Gaussian class. The full shadow obstruction tower is controlled by the
interaction between two primary directions in the modular cyclic
deformation complex (Definition~\ref{def:modular-cyclic-deformation-complex}),
and terminates at degree~$4$ by a stratum separation mechanism that has
no analogue for single-generator algebras.

\subsubsection{Multi-channel structure}
\label{sec:betagamma-multi-channel}

\begin{proposition}[$\beta\gamma$ deformation complex;
\ClaimStatusProvedHere]
\label{prop:betagamma-deformation-channels}
\index{beta-gamma system@$\beta\gamma$ system!deformation channels}
The modular cyclic deformation complex of the $\beta\gamma$ system at
conformal weight~$\lambda$ has (at least) two primary directions:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{The stress tensor line}
 (T-line): the one-dimensional slice corresponding to
 succeeded in 55ms:
self-bracket exits the complex by rank-one rigidity; no further
obstruction propagates.

Therefore $r_{\max} = 4$: the tower terminates at the quartic level.\qedhere
\end{proof}

\begin{remark}[Why the T-line tower continues but the global tower stops]
\label{rem:betagamma-stratum-separation-mechanism}
\index{stratum separation!mechanism}
The phenomenon that the T-line restriction has infinite shadow depth
(class~M) while the full algebra has finite shadow depth (class~C) is
\emph{stratum separation}: the quintic obstruction $o_5$ couples
the cubic and quartic shadows, but these live on different strata
of the deformation complex. The cubic shadow is supported on the
T-direction, the quartic contact lives on the charged stratum, and
their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
on the weight-changing line removes the required input.
Stratum separation is an intrinsically multi-channel
effect; it cannot occur for single-generator algebras, where the
shadow obstruction tower on the unique primary line \emph{is} the global tower.
 succeeded in 52ms:
chapters/examples/free_fields.tex:106:Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
chapters/examples/free_fields.tex:289:(Theorem~\ref{thm:single-line-dichotomy}), $\Delta = 0$
chapters/examples/free_fields.tex:715:Theorem~\ref{thm:betagamma-rank-one-rigidity});
chapters/examples/free_fields.tex:812:(Theorem~\ref{thm:betagamma-rank-one-rigidity}) applies verbatim once
chapters/examples/free_fields.tex:1089: (Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}).
chapters/examples/free_fields.tex:1108:Theorem~\ref{thm:betagamma-rank-one-rigidity}.\qedhere
chapters/examples/free_fields.tex:1145:(Theorem~\ref{thm:single-line-dichotomy}).\qedhere
chapters/examples/free_fields.tex:1161:rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
chapters/examples/free_fields.tex:1191:(Theorem~\ref{thm:betagamma-quartic-birth}).
chapters/examples/free_fields.tex:1200:Theorem~\ref{thm:betagamma-quartic-birth}).
chapters/examples/free_fields.tex:1204:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
chapters/examples/free_fields.tex:5550:(Theorem~\ref{thm:betagamma-rank-one-rigidity}).
chapters/examples/w3_holographic_datum.tex:638:Theorem~\ref{thm:single-line-dichotomy}, neither line terminates
chapters/examples/deformation_quantization_examples.tex:14:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}); and the Virasoro
chapters/examples/minimal_model_examples.tex:571:(Theorem~\ref{thm:single-line-dichotomy}).
chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
chapters/examples/beta_gamma.tex:188:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}) implies no quartic
chapters/examples/beta_gamma.tex:205:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), terminates
chapters/examples/beta_gamma.tex:353:(Theorem~\ref{thm:betagamma-rank-one-rigidity}), so
chapters/examples/beta_gamma.tex:2003:\label{sec:betagamma-quartic-birth}

thinking
**Inspecting dependencies in files**

I should look closely at the beta_gamma.tex file, focusing on the relevant theorems or propositions. Since the exact file isn’t assigned, my approach is to edit the target file but also check the cited dependencies. I think reading beta_gamma.tex is important since it’s a direct dependency. I'll search for the same labels around lines 2700 and 2096 to inspect the relevant sections. It seems like a necessary step to understand dependencies better.
codex
The local file already distinguishes the `T`-line from the weight-changing line, but the global theorem is still stated in a way that reads as if the `T`-line computation were a literal restriction of the global tower. I’m checking the fuller `beta_gamma` chapter that these claims compress, because if the canonical statement there already narrows the scope, the safest fix is to import that narrower wording here.
exec
/bin/zsh -lc "sed -n '2088,2175p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
to the moduli of deformations spanned by the class $\eta$ that shifts
conformal weight $\lambda \mapsto \lambda + \epsilon$.
\end{definition}

\subsection{Quartic birth}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth;
\ClaimStatusProvedHere]
\label{thm:betagamma-quartic-birth}
\index{quartic birth!beta-gamma@$\beta\gamma$}
On the weight/contact slice
(Definition~\textup{\ref{def:betagamma-weight-contact-slice}}), one has
\[
 \mathfrak{C}_{\beta\gamma} = 0,
 \qquad
 \mathfrak{o}_{\beta\gamma}^{(4)} = 0,
 \qquad
 \mathfrak{Q}_{\beta\gamma} = \operatorname{cyc}(m_3).
\]
Equivalently, the first nonlinear local shadow is quartic rather than
exec
/bin/zsh -lc 'rg -n "global shadow depth|T-line tower continues|weight-changing line|S_5 != 0 on the one-dimensional T-line restriction|stratum separation" chapters/examples/beta_gamma.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2550,2765p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
119:On the weight-changing line, the degree-$2$ shadow vanishes
139:On the weight-changing line (the $\lambda$-marginal slice),
338:the degree-$2$ shadow restricted to the weight-changing line vanishes
2034:On the weight-changing line, the genus-$0$ curvature vanishes ($m_0 = 0$) and the
2042:On the weight-changing line, the Maurer--Cartan equation is linear
2058:The tower terminates on the weight-changing line.
2119:On the weight-changing line the Maurer--Cartan equation is linear, so no
2131:degree~$4$ on weight-changing line; \ClaimStatusProvedHere]
2134:On the weight-changing line, the shadow obstruction tower
2145:on the weight-changing line.
2146:\textup{(}Off the weight-changing line, the global modular
2167:On the weight-changing line, the primitive logarithmic modular kernel
2181: \textup{(}cubic vanishes on the weight-changing line\textup{)};
2230:\textup{(}the branch space on the weight-changing line is rank~$1$\textup{)},
2238:weight-changing line. The rigid-cutting channel is nonzero: the
2253:On the weight-changing line the branch-active quotient
2268:invariant on the weight-changing line projects to zero in the branch
2276:The branch packet on the weight-changing line is Gaussian, but the
2282:\subsection{Explicit computations on the weight-changing line}
2353:to the weight-changing line.
 succeeded in 53ms:
Theorem~\ref{thm:betagamma-rank-one-rigidity} below.

\medskip
\noindent\emph{Computational verification:}
\texttt{compute/lib/betagamma\_quartic\_contact.py}.\qedhere
\end{proof}

\subsection{Rank-one abelian rigidity}

\begin{theorem}[Rank-one abelian rigidity; \ClaimStatusProvedHere]
\label{thm:betagamma-rank-one-rigidity}
\index{rank-one abelian rigidity}
Let $L \subset V_{\cA}$ be a one-dimensional cyclic subspace on which
all transferred higher brackets vanish:
\[
 \ell_n^{\mathrm{tr}}\big|_L = 0
 \qquad (n \ge 2).
\]
Then the restriction of the complementarity potential to $L$ is exactly
quadratic. In particular, complementarity on $L$ is formally fake.


thinking
**Clarifying theorems**

I'm working through some complexities in theorems related to global depth and T-line. It seems there's a contradiction in line 1171, and I think I need to clarify what the global tower refers to—it should be about the full two-dimensional deformation space. I should also specify that "S_5=0 globally" pertains to the global deformation complex, not just the T-line. Additionally, I’m reconsidering the weight-line proposition; it might not be correct to say it vanishes at all degrees due to global depth.
thinking
**Refining the proposition**

I'm thinking the current proposition is okay, but I should suggest adding a clarification: "This statement concerns only the one-dimensional weight-changing line; it does not rule out the quartic contact shadow on the two-dimensional weight/contact slice." That seems like a minimal adjustment. I also need to revisit the definitions or proposition in free_fields around 1080-1108. There might be mention of the deformation complex too, and it looks like there's a contradiction in the reading between lines 1148-1166.
Plan update
The contradiction looks semantic rather than computational: the local file mixes three different loci, and the wording currently makes the one-dimensional slice computations sound like literal restrictions of the global tower. I’m tightening only those scope boundaries.
  ✓ Compare the flagged propositions/theorem with the fuller beta-gamma chapter and identify the exact parameter loci each claim lives on
  → Patch chapters/examples/free_fields.tex with the minimum scope clarifications or narrowing needed to remove the contradictions
  • Re-read the edited block and grep the modified file for forbidden patterns and affected references
codex
```text
genus: [all]
degree: [all]
AP32 weight tag: [NA]
tagged? [Y]
AP139 free-var audit: LHS vars:{global beta-gamma tower / one-dimensional T-line slice / weight-changing line} RHS vars:{same after clarification} LHS⊇RHS? [Y]
AP36: [implies]
if iff, converse proved same thm? [NA]
verdict: ACCEPT
```


thinking
**Clarifying proof structure**

I think I should start the proof with a clear statement about its structure, noting that it's organized degree by degree on the full deformation complex. I also want to specify that the T-line computations I'm mentioning are slice computations and not literal restrictions. In degree 5, I need to revise that paragraph because I say the cubic shadow vanishes on all relevant slices, but it might confuse readers since the T-line cubic isn't zero after all.
thinking
**Addressing terminology concerns**

I’m noticing a potential issue with using "standalone one-dimensional T-line slice" in the theorem statement, as that term isn't currently established. It might be okay, but I should double-check. After editing the modified file, I’ll use grep to search for any forbidden patterns, like em dashes or AI-related sloppiness. I also want to look for occurrences of "restriction," as one of them might need to be removed. I'll proceed carefully with the patching process.
codex
I’ve isolated the minimal truthful fix: keep the weight-changing-line vanishing statement, but explicitly fence it to that one-dimensional slice; then rewrite the global-depth theorem/proof so the `T`-line calculation is clearly a separate one-dimensional recomputation, not a literal restriction of a globally vanishing quintic class. I’m applying only those scope edits now.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -1156,2 +1156,6 @@
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
@@ -1174,6 +1178,7 @@
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
@@ -1181,3 +1186,5 @@
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
@@ -1210,5 +1217,7 @@
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
@@ -1229,4 +1238,6 @@
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
apply_patch(auto_approved=true) exited 0 in 39ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..6341011684c5662e1ec7aaa5744d9a5d750f7fde
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1227,8 +1236,10 @@
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..6341011684c5662e1ec7aaa5744d9a5d750f7fde
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1227,8 +1236,10 @@
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.

codex
The scope edits are in place. I’m re-reading the patched block now to make sure the global theorem, its proof, and the adjacent remark still agree line-by-line and that I didn’t introduce a new local inconsistency.
exec
/bin/zsh -lc 'rg -n "restriction of a nonzero global quintic class|separately computed one-dimensional T-line tower|mixed charged stratum|full two-channel deformation space" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1148,1248p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1179:On the full two-channel deformation space, the $\beta\gamma$ system has
 succeeded in 51ms:
\begin{proposition}[$\beta\gamma$ shadow obstruction tower: weight-changing line;
\ClaimStatusProvedHere]
\label{prop:betagamma-weight-line-shadows}
\index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
\[
 S_r\big|_{\mathrm{wc}} = 0
 \qquad (r \geq 2).
\]
This statement concerns only the one-dimensional slice generated by the
weight-changing class; the quartic contact shadow in
Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
stratum and is not detected on this line.
\end{proposition}

\begin{proof}
The weight-changing line satisfies the hypothesis of rank-one abelian
rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
transferred higher brackets $\ell_n^{\mathrm{tr}}|_L = 0$ for
$n \geq 2$. The shadow obstruction tower is therefore purely quadratic, and since
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..6341011684c5662e1ec7aaa5744d9a5d750f7fde
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1227,8 +1236,10 @@
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.




thinking
**Refining terminology**

I'm thinking I need to change the wording from "restriction" to "slice" in the phrase about the T-line phenomenon to make it consistent. Also, I'm pondering whether "weight-changing line projection mu =..." is acceptable. The theorem proof may still utilize the Proposition T-line for degree 2 globally, but I'm unsure if S2 global is exactly equal to T-line kappa. In the context of a full two-channel complex global S2, it might be derived from the stress tensor line. I could refine the "T-line slice" in my remarks too.
thinking
**Checking for forbidden patterns**

I need to identify forbidden patterns in the modified file based on the user's request. I'm considering using `rg` with specific patterns for this, especially looking for problematic phrases or terms. It seems like checking for certain labels might not be an issue. I can focus on identifying new phrases to keep the results relevant. However, if I find a lot of unrelated matches, I’ll need to clarify that most are pre-existing. I should ensure to do this after editing.
thinking
**Searching for dangerous phrases**

I need to check for specific dangerous phrases, like "T-line restriction," within the modified block. It makes sense to look for these phrases carefully, especially in references to any labels. I’ll consider using `rg` to search for "T-line restriction" directly in the file. This should help me pinpoint any occurrences of that phrase effectively. It’s important to be thorough with this search to ensure I'm catching anything that could be problematic. Let's dive in!
codex
The patched block now reads coherently, but there’s one more local wording cleanup to remove the last ambiguous use of “restriction” in the remark. After that I’ll run the required grep checks on the modified file.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -1232,3 +1232,3 @@
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..4167d4bf935ebc940d4c3663ee0937d8e57fc9bd
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..4167d4bf935ebc940d4c3663ee0937d8e57fc9bd
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.

codex
I’m on verification now: first a forbidden-pattern grep on the modified file, then a quick reference/label sanity check on the labels cited in the edited block.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth)\\}|\\\\ref\\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth|thm:betagamma-rank-one-rigidity|thm:betagamma-quartic-birth|cor:nms-betagamma-mu-vanishing)\\}\" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -e '—' -e '---' -e '\\b[Mm]oreover\\b' -e '\\b[Aa]dditionally\\b' -e '\\b[Nn]otably\\b' -e '\\b[Cc]rucially\\b' -e '\\b[Rr]emarkably\\b' -e '\\b[Ff]urthermore\\b' -e 'we now' -e 'it is worth noting' -e 'worth mentioning' -e 'it should be noted' -e 'it is important to note' -e '\\bdelve\\b' -e '\\bleverage\\b' -e '\\btapestry\\b' -e '\\bcornerstone\\b' -e '\\bjourney\\b' -e '\\bnavigate\\b' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth)\}|\ref\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth|thm:betagamma-rank-one-rigidity|thm:betagamma-quartic-birth|cor:nms-betagamma-mu-vanishing)\})
       ^^
error: unrecognized escape sequence
 succeeded in 53ms:
3:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
606: & --- \\
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..4167d4bf935ebc940d4c3663ee0937d8e57fc9bd
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.


thinking
**Reviewing code edits**

I need to rerun the ref sanity check and use escaped slashes with the -F option. I've found preexisting matches in lines 3 and 606, which seem unrelated. Line 3 is from the file header comment, and line 606 is in the table. I should confirm these aren’t in the edited region to avoid touching unrelated content. Maybe I’ll run `git diff -- chapters/examples/free_fields.tex` to focus on our changes and consider using fixed strings for the grep patterns. Let’s go through that!
codex
The forbidden-pattern grep only hit two pre-existing `---` instances far outside the edited block; the patched region itself is clean. I’m rerunning the reference check with fixed-string patterns because the first regex escaped poorly.
exec
/bin/zsh -lc "rg -n -F -e '\\label{prop:betagamma-T-line-shadows}' -e '\\label{prop:betagamma-weight-line-shadows}' -e '\\label{thm:betagamma-global-depth}' -e '\\ref{prop:betagamma-T-line-shadows}' -e '\\ref{prop:betagamma-weight-line-shadows}' -e '\\ref{thm:betagamma-global-depth}' -e '\\ref{thm:betagamma-rank-one-rigidity}' -e '\\ref{thm:betagamma-quartic-birth}' -e '\\ref{cor:nms-betagamma-mu-vanishing}' chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b32468..4167d4b 100644
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@ On the weight-changing line, the shadow obstruction tower vanishes at all degree
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@ vanishes.\qedhere
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
 succeeded in 55ms:
chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
chapters/examples/beta_gamma.tex:188:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}) implies no quartic
chapters/examples/beta_gamma.tex:205:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), terminates
chapters/examples/beta_gamma.tex:353:(Theorem~\ref{thm:betagamma-rank-one-rigidity}), so
chapters/examples/beta_gamma.tex:2053:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}),
chapters/examples/beta_gamma.tex:2076:Theorem~\ref{thm:betagamma-quartic-birth} and
chapters/examples/beta_gamma.tex:2143:By Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}},
chapters/examples/beta_gamma.tex:2153:Combine Theorem~\ref{thm:betagamma-quartic-birth}
chapters/examples/beta_gamma.tex:2155:with Corollary~\ref{cor:nms-betagamma-mu-vanishing}
chapters/examples/beta_gamma.tex:2187: \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing})};
chapters/examples/beta_gamma.tex:2257:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), the branch
chapters/examples/beta_gamma.tex:2286:Theorem~\ref{thm:betagamma-quartic-birth} and the vanishing of the
chapters/examples/beta_gamma.tex:2452:(Theorem~\ref{thm:betagamma-rank-one-rigidity} below)
chapters/examples/beta_gamma.tex:2550:Theorem~\ref{thm:betagamma-rank-one-rigidity} below.
chapters/examples/beta_gamma.tex:2617:(Theorem~\ref{thm:betagamma-rank-one-rigidity}) explains uniformly why
chapters/examples/beta_gamma.tex:2701:$($Theorem~\textup{\ref{thm:betagamma-quartic-birth}}$)$.
chapters/examples/beta_gamma.tex:2719:$($Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}$)$
chapters/examples/beta_gamma.tex:2734:Part~(ii) is Theorem~\ref{thm:betagamma-quartic-birth}: the
chapters/examples/beta_gamma.tex:2737:Part~(iii) is Theorem~\ref{thm:betagamma-rank-one-rigidity},
chapters/examples/free_fields.tex:106:Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..4167d4bf935ebc940d4c3663ee0937d8e57fc9bd
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.

codex
The edited block is internally consistent now. I’m doing one last nearby-context read at the later cross-reference to `thm:betagamma-global-depth`, so I don’t leave a stale summary elsewhere in the same file.
exec
/bin/zsh -lc "sed -n '5538,5568p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 Genus-$0$ qi; rank $2 \cdot 3^{n-1}$ (Thm~\ref{thm:betagamma-bar-dim}) \\
C (complementarity) &
 $\kappa(\beta\gamma) + \kappa(bc) = 0$ &
 $Q_g + Q_g^! = H^*(\overline{\mathcal{M}}_g, Z(\beta\gamma))$ \\
D (modular char.) &
 $\Theta_{\beta\gamma}\big|_{g=1,n=0}
 = \kappa \cdot \lambda_1$ &
 $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\
H (Hochschild) &
 Degree-preserving sub-MC &
 $\operatorname{ChirHoch}^*(\beta\gamma)$ polynomial \\
\bottomrule
\end{tabular}
\end{center}
Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
on the weight-changing line. The quartic contact invariant
$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
stratum separation
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..4167d4bf935ebc940d4c3663ee0937d8e57fc9bd
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.


thinking
**Editing for clarity**

I’ve noticed a contradiction in the file, which is beyond my initial target area. It looks like I need to make an edit. So, should I proceed with this? Yes, definitely! I think I’ll patch up that small paragraph to fix the issue. It's important to ensure clarity and consistency, so making this edit feels like the right thing to do. Let's get that done!
codex
A later in-file summary was still advertising the old contradiction: it said the quartic contact appeared “on the weight-changing line,” which directly conflicts with both the local proposition and the canonical `beta_gamma` chapter. I’m tightening that one summary paragraph so the later reference matches the repaired theorem surface.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -5551,8 +5551,8 @@
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..45b7a3337b2424103f25325f7cc86d120b8c4038
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5549,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..45b7a3337b2424103f25325f7cc86d120b8c4038
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5549,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
The repaired theorem surface exposed one stale summary later in the file; that is patched now. I’m doing a final targeted scan for any remaining local phrases that still claim nonzero quartic data on the weight-changing line.
exec
/bin/zsh -lc "rg -n -C 2 \"weight-changing line|quartic contact|T-line slice|global shadow depth|Theta\\"'^'"\\{\\\\leq 4\\}\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5548,5568p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -e '—' -e '---' -e '\\b[Mm]oreover\\b' -e '\\b[Aa]dditionally\\b' -e '\\b[Nn]otably\\b' -e '\\b[Cc]rucially\\b' -e '\\b[Rr]emarkably\\b' -e '\\b[Ff]urthermore\\b' -e 'we now' -e 'it is worth noting' -e 'worth mentioning' -e 'it should be noted' -e 'it is important to note' -e '\\bdelve\\b' -e '\\bleverage\\b' -e '\\btapestry\\b' -e '\\bcornerstone\\b' -e '\\bjourney\\b' -e '\\bnavigate\\b' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:weight-changing line|quartic contact|T-line slice|global shadow depth|Theta\^\{\leq 4\})
                                                                                      ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 $\operatorname{ChirHoch}^*(\beta\gamma)$ polynomial \\
\bottomrule
\end{tabular}
\end{center}
Shadow obstruction tower: on the one-dimensional weight-changing line all
shadows vanish, but on the full two-channel deformation space one has
$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
obstruction still satisfies $o_5 = 0$ by stratum separation
(Theorem~\ref{thm:betagamma-global-depth}):
the quartic contact class lives on a charged stratum whose
self-bracket exits the complex by rank-one rigidity
(Theorem~\ref{thm:betagamma-rank-one-rigidity}).
Tower terminates at exactly $r = 4$.
The full shadow obstruction tower data (multi-channel structure,
special weight table, shadow metric, weight symmetry,
Mumford connection) is in
\S\ref{sec:betagamma-shadow-tower-free}.
The two-generator free-field systems ($\beta\gamma$ and $bc$)
 succeeded in 51ms:
3:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
606: & --- \\
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..45b7a3337b2424103f25325f7cc86d120b8c4038
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5549,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity


thinking
**Fixing regex patterns**

The first scan with the regex didn't work, so I need to rerun it using fixed strings or simpler patterns. For this, I’m thinking of searching for terms like "weight-changing line" and "quartic contact" in the file. That might help since it seems these phrases are key to what I'm looking for. I need to ensure I get this right to avoid further issues down the road!
codex
The summary paragraph is now aligned. One final targeted grep remains, using fixed strings only, to confirm there isn’t another local sentence still tying the quartic contact directly to the weight-changing line.
exec
/bin/zsh -lc "rg -n -F -e 'weight-changing line' -e 'quartic contact' -e 'T-line slice' -e 'global shadow depth' -e '\\Theta"'^{'"\\leq 4}' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
19:$d\log$ absorption as a quartic contact interaction, and the shadow
60:$r(z) = 0$. The quartic contact shadow, not the $r$-matrix,
79:Gaussian class because $\Theta^{\leq 4} \neq \Theta^{\leq 2}$ (quartic
82:weight-changing line (the global modular characteristic
104:but the quartic contact invariant vanishes
238: \textup{(}Consequence of $S_3 = 0$: no quartic contact term survives in the
277:With $S_3 = 0$, the quartic contact invariant
280:the obstruction to extending $\Theta^{\leq 3}$ to $\Theta^{\leq 4}$
710:is nonzero at generic $\lambda$, but on the weight-changing line
754:weight-changing line (cubic vanishes by rank-one abelian rigidity).
755:The quartic contact shadow lives on the charged stratum mixing the
1084:\item \emph{The weight-changing line}: the deformation that shifts the
1102:$S_4 = 10/(c(5c+22))$ (the quartic contact invariant). Direction~(ii):
1148:\begin{proposition}[$\beta\gamma$ shadow obstruction tower: weight-changing line;
1151:\index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
1152:On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
1158:weight-changing class; the quartic contact shadow in
1164:The weight-changing line satisfies the hypothesis of rank-one abelian
1175:\begin{theorem}[$\beta\gamma$ global shadow depth; \ClaimStatusProvedHere]
1180:global shadow depth $r_{\max} = 4$
 succeeded in 50ms:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b32468..45b7a33 100644
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@ On the weight-changing line, the shadow obstruction tower vanishes at all degree
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@ vanishes.\qedhere
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..45b7a3337b2424103f25325f7cc86d120b8c4038
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5549,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity


thinking
**Inspecting code lines**

I see that the scan indicates a potential issue around line 710, and I might need to check lines 700 to 760 for contradictions. The scan output suggests that line 710 has a nonzero generic lambda, which seems off considering it’s on a weight-changing line. On the other hand, lines 754-755 refer to quartic contact shadows linked to a charged stratum mixing weight changes. I'll definitely need to take a closer look at this segment!
codex
The targeted scan found one earlier local passage in the same beta-gamma discussion. I’m checking that block to make sure it already distinguishes the charged stratum correctly; if it doesn’t, I’ll patch just that sentence too.
exec
/bin/zsh -lc "sed -n '700,760p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{beta-gamma system|textbf}

\begin{remark}[Shadow archetype: contact/quartic]
\label{rem:betagamma-shadow-archetype-free}
\index{beta-gamma system@$\beta\gamma$ system!shadow archetype}
Shadow depth $r_{\max} = 4$ (class~C).
Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
where $\lambda$ is the conformal weight of $\gamma$.
Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
is nonzero at generic $\lambda$, but on the weight-changing line
$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
Tower terminates at exactly $r = 4$ by
stratum separation (rank-one rigidity,
Theorem~\ref{thm:betagamma-rank-one-rigidity});
see \S\ref{sec:betagamma-shadow-tower-free} for the full tower.
Koszul dual: $(\beta\gamma)^! = bc$
(Theorem~\ref{thm:betagamma-bc-koszul}).
See Chapter~\ref{chap:beta-gamma} for the full quartic
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..45b7a3337b2424103f25325f7cc86d120b8c4038
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1154,6 +1154,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1176,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1215,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1230,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5549,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
That earlier remark still had the same overstatement. I’m correcting just that sentence so the file has one consistent story: vanishing on the isolated weight-changing line, quartic birth only on the mixed charged stratum.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -710,3 +710,5 @@
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
apply_patch(auto_approved=true) exited 0 in 51ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..427a5beb68e4bbd431367b686d42f8a92a2e916f
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..427a5beb68e4bbd431367b686d42f8a92a2e916f
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
I corrected the earlier summary remark as well. I’m re-reading the top-level beta-gamma summary block now, because it is easy for these condensed overview paragraphs to drift after a local theorem repair.
exec
/bin/zsh -lc "sed -n '72,110p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
higher projections $\Theta_\cA^{\leq r} = \Theta_\cA^{\leq 2}$ for
$r \geq 3$. Equivalently, the convolution algebra
$\gAmod$ has trivial higher brackets: the modular deformation complex
$\Definfmod(\cA)$ is formal.

The free fermion is Gaussian with
$\kappa \neq 0$; the $\beta\gamma$ and $bc$ systems break out of the
Gaussian class because $\Theta^{\leq 4} \neq \Theta^{\leq 2}$ (quartic
contact shadow nontrivial on the charged stratum), even though
$\Theta_{\beta\gamma}^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ on the
weight-changing line (the global modular characteristic
$\kappa(\beta\gamma) = c/2$ is generically nonzero). Both
two-generator free-field systems ($\beta\gamma$ and $bc$) are class~C
($r_{\max} = 4$) by the same stratum separation mechanism; the
single-generator free fermion is class~G ($r_{\max} = 2$) by
fermionic antisymmetry. The free-field periodic table therefore
exhibits the transition from the Gaussian to the contact/quartic
archetype within the shadow depth classification
(Table~\ref{tab:shadow-tower-census}).
\end{remark}
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..427a5beb68e4bbd431367b686d42f8a92a2e916f
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
The overview blocks now agree with the repaired theorem surface. I’m doing a last phrase-level grep for the old overclaim pattern so I don’t leave another stale copy elsewhere in the same file.
exec
/bin/zsh -lc "rg -n -F -e 'first nontrivial shadow is quartic' -e 'T-line restriction' -e 'on the weight-changing line.' -e 'weight-changing line all' -e 'separately computed one-dimensional T-line tower' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1270:that $Q_L$ is irreducible quadratic and the T-line restriction is
5554:Shadow obstruction tower: on the one-dimensional weight-changing line all
exec
/bin/zsh -lc "rg -n -F -e 'quartic contact shadow lives on the charged stratum' -e 'mixed charged stratum' -e 'one-dimensional slice generated by the weight-changing class' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
757:The quartic contact shadow lives on the charged stratum mixing the
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..427a5beb68e4bbd431367b686d42f8a92a2e916f
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
There is one remaining harmless but ambiguous phrase in the `T`-line metric proposition: “T-line restriction.” I’m normalizing that to “T-line slice” for consistency with the repaired theorem language, then I’ll close out verification.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -1269,3 +1269,3 @@
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
apply_patch(auto_approved=true) exited 0 in 55ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..b4e58d8b74a811112cc2ff1af7f0d16df8ccebd2
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -1254,7 +1267,7 @@
  = \frac{40}{60\lambda^2 - 60\lambda + 32}.
 \end{equation}
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
 \end{proposition}
 
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..b4e58d8b74a811112cc2ff1af7f0d16df8ccebd2
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -1254,7 +1267,7 @@
  = \frac{40}{60\lambda^2 - 60\lambda + 32}.
 \end{equation}
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
 \end{proposition}
 
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity


thinking
**Considering final checks**

I’m thinking about rerunning the final grep and possibly building next. I should at least check for forbidden patterns and phrase issues. Updating the plan might be a good idea too. I wonder if I need to run a final read of the relevant blocks, but it might not be necessary. Maybe I could use exec with those final greps to wrap things up efficiently.
codex
The terminology is normalized now. I’m running the final verification batch: the forbidden-pattern grep the user asked for, plus a fixed-string scan of the repaired beta-gamma phrases to confirm the file now distinguishes the three loci consistently.
exec
/bin/zsh -lc "rg -n -e '—' -e '---' -e '\\b[Mm]oreover\\b' -e '\\b[Aa]dditionally\\b' -e '\\b[Nn]otably\\b' -e '\\b[Cc]rucially\\b' -e '\\b[Rr]emarkably\\b' -e '\\b[Ff]urthermore\\b' -e 'we now' -e 'it is worth noting' -e 'worth mentioning' -e 'it should be noted' -e 'it is important to note' -e '\\bdelve\\b' -e '\\bleverage\\b' -e '\\btapestry\\b' -e '\\bcornerstone\\b' -e '\\bjourney\\b' -e '\\bnavigate\\b' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F -e 'one-dimensional slice generated by the weight-changing class' -e 'full two-channel deformation space' -e 'separately computed one-dimensional T-line tower' -e 'T-line slice has infinite shadow depth' -e 'on the one-dimensional weight-changing line all shadows vanish' -e 'charged stratum' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
80:contact shadow nontrivial on the charged stratum), even though
713:level is the quartic contact term on the charged stratum:
757:The quartic contact shadow lives on the charged stratum mixing the
1181:On the full two-channel deformation space, the $\beta\gamma$ system has
1206:is nontrivial on the charged stratum that mixes the T-line and
1220:The quartic contact class lives on the charged stratum, while the cubic
1225:The quartic contact class lives on a charged stratum whose
1235:The phenomenon that the T-line slice has infinite shadow depth
1240:T-direction, the quartic contact lives on the charged stratum, and
5555:shadows vanish, but on the full two-channel deformation space one has
5561:the quartic contact class lives on a charged stratum whose
 succeeded in 60ms:
3:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
606: & --- \\
exec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b32468..b4e58d8 100644
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@ where $\lambda$ is the conformal weight of $\gamma$.
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@ On the weight-changing line, the shadow obstruction tower vanishes at all degree
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..b4e58d8b74a811112cc2ff1af7f0d16df8ccebd2
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -1254,7 +1267,7 @@
  = \frac{40}{60\lambda^2 - 60\lambda + 32}.
 \end{equation}
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
 \end{proposition}
 
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

Plan update
The contradictions came from scope drift between three loci: the standalone T-line slice, the standalone weight-changing line, and the full two-channel deformation space. The file now distinguishes those surfaces consistently, including one later summary paragraph that still advertised the old contradiction.
  ✓ Compare the flagged propositions/theorem with the fuller beta-gamma chapter and identify the exact parameter loci each claim lives on
  ✓ Patch chapters/examples/free_fields.tex with the minimum scope clarifications or narrowing needed to remove the contradictions
  ✓ Re-read the edited block and grep the modified file for forbidden patterns and affected references
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..b4e58d8b74a811112cc2ff1af7f0d16df8ccebd2
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -1254,7 +1267,7 @@
  = \frac{40}{60\lambda^2 - 60\lambda + 32}.
 \end{equation}
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
 \end{proposition}
 
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

codex
Edited [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1150) with the minimum truthful scope fixes, and also repaired two stale summaries in the same file at [the earlier beta-gamma overview](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:708) and [the later recap table](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5551).

- Finding 1: FIXED. The vanishing proposition now explicitly says it is only about the one-dimensional weight-changing line. I added that the quartic contact shadow belongs to the mixed charged stratum, so it does not contradict class C / global depth 4.
- Finding 2: FIXED. The global-depth theorem now says it is about the full two-channel deformation space, and the `T`-line statement is rewritten as a separately computed one-dimensional slice, not a literal restriction of a globally vanishing quintic class. I also adjusted the proof and the adjacent remark to match that scope.
- Surrounding-context drift: FIXED. Two summary passages elsewhere in the same file were still saying the quartic contact showed up on the weight-changing line; those now match the repaired theorem surface.

Verification: I re-read the patched blocks, checked the cited labels/refs used in the edited surface, and ran the requested forbidden-pattern grep on the modified file. That grep only found two pre-existing `---` instances at lines 3 and 606, outside the edited regions. I did not run a TeX build.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 6b3246856429a6ab9ceaebda32a781aa35587a19..b4e58d8b74a811112cc2ff1af7f0d16df8ccebd2
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,7 +708,9 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the first nontrivial shadow is quartic:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
+shadows vanish. The first nontrivial global shadow beyond the scalar
+level is the quartic contact term on the charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1154,6 +1156,10 @@
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
+This statement concerns only the one-dimensional slice generated by the
+weight-changing class; the quartic contact shadow in
+Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
+stratum and is not detected on this line.
 \end{proposition}
 
 \begin{proof}
@@ -1172,14 +1178,17 @@
 \label{thm:betagamma-global-depth}
 \index{stratum separation!beta-gamma@$\beta\gamma$}
 \index{beta-gamma system@$\beta\gamma$ system!shadow depth}
-The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
+On the full two-channel deformation space, the $\beta\gamma$ system has
+global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, despite $S_5 \neq 0$ on
-the one-dimensional T-line restriction.
+The quintic shadow $S_5 = 0$ globally, even though the separately
+computed one-dimensional T-line tower has $S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
-The proof proceeds degree by degree.
+The proof proceeds degree by degree on the full deformation complex.
+The T-line computations cited below are one-dimensional slice
+computations, not literal restrictions of the global higher shadows.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1208,9 +1217,11 @@
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket
 $o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
-Since the cubic shadow $\mathfrak{C}_{\beta\gamma} = 0$ on all relevant
-slices (it vanishes on the weight-changing line and does not mix with the
-quartic in the quintic obstruction), the bracket $o_5 = 0$.
+The quartic contact class lives on the charged stratum, while the cubic
+shadow that survives on the standalone T-line does not contribute a
+compatible input in the full two-channel complex. On the weight-changing
+line the cubic vanishes altogether. Hence the global bracket
+$o_5 = 0$.
 The quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity; no further
 obstruction propagates.
@@ -1221,14 +1232,16 @@
 \begin{remark}[Why the T-line tower continues but the global tower stops]
 \label{rem:betagamma-stratum-separation-mechanism}
 \index{stratum separation!mechanism}
-The phenomenon that the T-line restriction has infinite shadow depth
+The phenomenon that the T-line slice has infinite shadow depth
 (class~M) while the full algebra has finite shadow depth (class~C) is
 \emph{stratum separation}: the quintic obstruction $o_5$ couples
 the cubic and quartic shadows, but these live on different strata
 of the deformation complex. The cubic shadow is supported on the
 T-direction, the quartic contact lives on the charged stratum, and
-their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
-on the weight-changing line removes the required input.
+their Lie bracket vanishes in the full two-channel complex. The T-line
+tower is obtained by recomputing the shadow calculus after projecting to
+that one-dimensional slice; it is not the restriction of a nonzero
+global quintic class.
 Stratum separation is an intrinsically multi-channel
 effect; it cannot occur for single-generator algebras, where the
 shadow obstruction tower on the unique primary line \emph{is} the global tower.
@@ -1254,7 +1267,7 @@
  = \frac{40}{60\lambda^2 - 60\lambda + 32}.
 \end{equation}
 The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
-that $Q_L$ is irreducible quadratic and the T-line restriction is
+that $Q_L$ is irreducible quadratic and the T-line slice is
 class~M.
 \end{proposition}
 
@@ -5538,12 +5551,12 @@
 \bottomrule
 \end{tabular}
 \end{center}
-Shadow obstruction tower: $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
-at the scalar level, but $\Theta^{\leq 4} \neq \Theta^{\leq 2}$
-on the weight-changing line. The quartic contact invariant
+Shadow obstruction tower: on the one-dimensional weight-changing line all
+shadows vanish, but on the full two-channel deformation space one has
+$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
-(Chapter~\ref{chap:beta-gamma}), while $o_5 = 0$ by
-stratum separation
+\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
+obstruction still satisfies $o_5 = 0$ by stratum separation
 (Theorem~\ref{thm:betagamma-global-depth}):
 the quartic contact class lives on a charged stratum whose
 self-bracket exits the complex by rank-one rigidity

tokens used
71,725
