# H02_thm_B_alt_proof (570s)

Revised the alternative-proof remark for Theorem B in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1858). The remark now states the second proof path in the requested Keller language: a filtered strong deformation retract on the tangent complex, the quadratic formal-neighborhood interpretation via `\cA^i = H^*(\barB(\cA))`, Kontsevich/Fulton--MacPherson formality feeding the transferred `A_\infty` structure, and descent to the coderived statement through the curvature/bar-degree filtration. No duplicate remark surface was found in Vol II or Vol III.

Verification: `make fast` completed without a local LaTeX error. Final pass reached `0` undefined citations and `0` undefined references; one rerun request remained from large-document page-count oscillation.

## Fortification Report
Theorem B (`thm:bar-cobar-inversion-qi`)
- PRIMARY PROOF: sound on the current local dependency surface
- SECONDARY PROOF: written
- TECHNIQUE: Keller deformation-theoretic tangent-complex retract + Kontsevich/Fulton--MacPherson `E_2` formality + coderived descent through curvature filtration
- CONDITION STATUS: genus-0 strict lane unconditional; higher-genus strict lane conditional on `MK:modular`; coderived off-locus unconditional under the theorem’s existing finite-dimensional graded-bar hypothesis
- CONFIDENCE: medium


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
session id: 019d8693-ebb4-73a1-a8f0-774e0c0dd20b
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.

CRITICAL SESSION CONTEXT (factor this in):
This session deployed 537+ Codex agents across 7 campaigns. The following has ALREADY been done:
- Theorems A-D, H: proof architecture rectified. Verdier convention fixed (Thm A), off-locus
  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
  separated + reflexivity from perfectness (Thm C1), center-to-bar lift proved (Thm C2),
  circularity broken with routing remark (Thm D).
- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
- Topologization: split into cohomological (proved KM) + chain-level (conjectural).
- Koszul equivs (vii)/(viii): scope narrowed to match proofs.
- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
- 48 new anti-patterns catalogued (AP186-AP224).
- Wave A: broken refs, hardcoded Parts, duplicate labels, status mismatches, proof-after-conj
  all fixed across Vol I and Vol II.
- New compute engines: critical level (72 tests), Verlinde polynomial (g=0..6),
  genus-2 decomposition, chiral bialgebra, tetrahedron, and 20+ more.
- Vol I ~2,719pp (29 commits this session), Vol II ~1,681pp (15 commits), Vol III ~319pp (19 commits).

READ the current state of files on disk — they reflect ALL the above work.
Your job: HEAL remaining wounds, provide ALTERNATIVE proofs, UPGRADE strength.

Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


THEOREM B — ALTERNATIVE PROOF via Keller's deformation theory.

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex (add Remark)

The primary proof uses the bar filtration spectral sequence. Write an ALTERNATIVE:

TECHNIQUE: Keller's derived deformation theory + Kontsevich formality.
1. The bar-cobar unit A -> Omega(B(A)) is a deformation-retract at the level of
   the tangent complex (Koszul locus = formal neighborhood of the quadratic closure).
2. Kontsevich formality for FM_n(C) implies the A-inf structure on H*(B(A)) is formal
   on the Koszul locus. Formality + deformation retract = qi.
3. The off-locus extension to D^co: the deformation retract descends to the coderived
   category because the retraction respects the curvature filtration.

Write as Remark[Alternative proof via formality]. This provides a SECOND proof path
independent of the spectral sequence argument.
mcp startup: no servers

thinking
**Choosing the right tool for search**

I need to search the codebase files, and I could use either the spawn_agent explorer or shell. The explorer seems to be a clear choice since it's specified for codebase questions and is described as fast and authoritative. Although using the shell might feel easier, I want to stick to the instruction of using `explorer`. It makes sense to go with what’s recommended for efficiency!
codex
I’m fortifying Theorem B in `chapters/theory/bar_cobar_adjunction_inversion.tex` by adding an alternative proof remark, and I’m starting with the required live-surface reads plus the current theorem context before I draft anything.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
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
| `ProvedHere` | 2842 |
 succeeded in 52ms:
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

thinking
**Locating codebase dependencies**

I need to read the full target file and its dependencies. I could use the explorer subagent, but I've already gathered some information directly. The instruction suggests preferring explorers for codebase questions, though it isn't mandatory. Maybe it's okay not to use it? I’ll ask the explorer agent to summarize theorem B and its cited dependencies for the alternative proof. I need to make sure to state I'm using the skill line and to spawn the explorer agent.
codex
I’m using `beilinson-rectify` for the theorem surface and `build-surface` for verification. Next I’m reading the full Theorem B lane and the local proof dependencies so the alternative proof can be inserted without drifting object identity or status.
collab spawn_agent(call_IG0mf5Ne5k4VmAabkxgVym0k, prompt="Inspect the Theorem B lane in /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex. I need: …")
mcp startup: no servers
spawn_agent(call_IG0mf5Ne5k4VmAabkxgVym0k, prompt="Inspect the Theorem B lane in /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex. I need: …") pending init:
  agent: 019d8694-5aab-7493-a4c3-e571937e4c29
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
exec
/bin/zsh -lc 'rg -n "thm:bar-cobar-inversion-qi" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
138:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
690:(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1713:Theorem~\ref{thm:bar-cobar-inversion-qi}; the concrete mechanism by
1761:Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
1861:Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
1938:Theorem~\ref{thm:bar-cobar-inversion-qi}. Then:
1980:At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is a
1992:Theorem~\ref{thm:bar-cobar-inversion-qi} is invoked to verify
2011:quasi-isomorphism. Theorem~\ref{thm:bar-cobar-inversion-qi} is
2018:At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is
2076:Theorem~\ref{thm:bar-cobar-inversion-qi} converts the bar coalgebra
2187:For the application to Theorem~\ref{thm:bar-cobar-inversion-qi}, the completeness statement in Definition~\ref{def:bar-cobar-filtration}(2) is supplied by its conilpotency/completion hypothesis: if $\bar{B}(\mathcal{A})$ is conilpotent in the sense of Definition~\ref{def:conilpotent-complete}, every element has finite bar degree, while in the augmentation-ideal completion regime the filtration is complete by construction.
2247:Theorem~\ref{thm:bar-cobar-inversion-qi}. The bar-cobar inversion
2441:(Theorem~\ref{thm:bar-cobar-inversion-qi}) establishes the
2550:(Theorem~\ref{thm:bar-cobar-inversion-qi}), these results close
2606: Thm~\ref{thm:bar-cobar-inversion-qi} \\
2639:The inversion theorem (Theorem~\ref{thm:bar-cobar-inversion-qi})
2672:standing hypotheses of Theorem~\textup{\ref{thm:bar-cobar-inversion-qi}}.
exec
/bin/zsh -lc "sed -n '1,280p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1580,1725p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '280,620p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
%% ===== Editorial bridge: the inversion half of the chapter =====
%%
%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
%% framework that supports it off the quadratic locus. This second half
%% proves that the adjunction inverts: Theorem B says
%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
%% Together, Theorems A and B close the algebraic engine of the monograph.

\bigskip
\noindent\textbf{From adjunction to inversion.}\enspace
An adjunction that is not an equivalence is a deficiency: it
records the information lost in the round trip. Theorem~A
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

 succeeded in 51ms:
 finite-dimensional graded pieces, which is
 needed for the duality between contramodules and complete modules
 (Remark~\ref{rem:chiral-contramodules}).
\end{enumerate}
These geometric inputs are specific to the chiral setting and have
no analogue in Positselski's ground-field framework.
\end{remark}

%================================================================
% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
%================================================================

\section{Bar-cobar inversion}
\label{sec:bar-cobar-inversion-quasi-iso}

The comodule-contramodule correspondence of the preceding section
provides the categorical framework in which bar-cobar inversion
lives: at genus~$0$ the coderived category reduces to the
ordinary derived category, and the inversion theorem is a
quasi-isomorphism in the classical sense; at genus~$g \geq 1$
 succeeded in 51ms:
YES (strong completion tower,
Thm~\ref{thm:completed-bar-cobar-strong}) &
$W_\infty$ \\
\hline
\end{tabular}
\end{center}

\subsection{Theoretical framework: filtered cooperads}

Following Gui--Li--Zeng \cite{GLZ22}, we develop the theory of filtered cooperads.

\begin{definition}[Filtered cooperad]\label{def:filtered-cooperad}
A \emph{filtered cooperad} $\mathcal{C}$ is a cooperad equipped with a filtration:
\begin{equation}
F^0\mathcal{C} \supset F^1\mathcal{C} \supset F^2\mathcal{C} \supset \cdots
\end{equation}
(decreasing) satisfying:
\begin{enumerate}
\item \emph{Coalgebra compatibility}: 
\[\Delta(F^k\mathcal{C}) \subset \sum_{i+j=k} F^i\mathcal{C} \otimes F^j\mathcal{C}\]
exec
/bin/zsh -lc "sed -n '620,1040p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1040,1520p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1520,2460p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
finite-type algebras converge without completion.
\end{proof}

\begin{remark}[Dependencies]
This proof uses:
\begin{enumerate}[label=(D\arabic*)]
\item conilpotent convergence control (Theorem~\ref{thm:conilpotency-convergence});
\item filtered-to-curved reduction inputs for non-quadratic regimes
(Theorem~\ref{thm:filtered-to-curved});
\item filtered/complete Koszul duality context \cite{GLZ22}.
\end{enumerate}
\end{remark}

\subsection{Physical interpretation}

Quadratic algebras correspond to free field theories (Heisenberg $\leftrightarrow$ free boson, Kac--Moody $\leftrightarrow$ WZW). Curved algebras correspond to interacting theories with anomalies (Virasoro, with central charge $c$ measuring quantum breaking of scale invariance). Filtered algebras correspond to theories with composite operators ($W_3$ and Toda field theory). General algebras correspond to non-local theories ($W_\infty$), where the MC4 structural package is proved (Theorem~\ref{thm:completed-bar-cobar-strong}); the residual H-level comparison is example-specific.

From Kontsevich's geometric viewpoint, the filtration level corresponds to the codimension of collision loci: quadratic algebras see only pairwise collisions, curved algebras see central terms from $n$-point collisions, and filtered algebras require higher-codimension strata. The completion $\widehat{\bar{B}}(\mathcal{A})$ is the formal neighborhood of the diagonal in configuration space.

\subsection{Summary and decision tree}
 succeeded in 51ms:
\[
J(V) := C \chirtensor V
\]
with coaction $\Delta \chirtensor \mathrm{id}_V\colon
C \chirtensor V \to C \chirtensor C \chirtensor V$.
The CDG-comodule differential is
$d_{J(V)}(c \otimes v) = d(c) \otimes v$,
and the curvature relation $d_{J(V)}^2 = h \ast (-)$ is inherited
from~$C$.
\end{definition}

\begin{proposition}[Injective and projective resolutions;
\ClaimStatusProvedHere]\label{prop:chiral-inj-proj-resolutions}
\index{injective resolution!chiral CDG-comodule}
\index{projective resolution!chiral CDG-contramodule}
Let $(C, d, h)$ be a conilpotent chiral CDG-coalgebra with
finite-dimensional graded pieces.
\begin{enumerate}[label=\textup{(\alph*)}]
\item For any left chiral CDG-comodule $M$, the cofree chiral
 comodule $J(M) = C \chirtensor M$ is \emph{injective} in the
 succeeded in 51ms:
\end{theorem}

\begin{proof}
\emph{Step~1.}
By Remark~\ref{rem:chiral-contramodules}, under the standing
finite-type hypothesis, chiral CDG-contramodules over~$C$ are
equivalent to complete modules over the graded dual algebra~$C^*$.

\emph{Step~2.}
On the additional flat finite-type locus assumed in the statement,
Positselski's comparison theorem
\cite[\S4.5, Theorem~4.5.1]{Positselski11} identifies the
contraderived category of these contramodules with the ordinary
bounded derived category of complete $C^*$-modules. This gives
\eqref{eq:full-derived-equiv-proved}.

\emph{Step~3.}
Combining \eqref{eq:full-derived-equiv-proved} with
Theorem~\ref{thm:positselski-chiral-proved} gives the stated ordinary
derived reduction of the intrinsic coderived/contraderived
exec
/bin/zsh -lc 'rg -n "begin{proof}" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:begin{proof})
             ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{proof\\}\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc 'rg -n "Proof" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
324:\begin{proof}[Proof outline (following GLZ)]
2101:\subsection{Proof strategy and filtration}
exec
/bin/zsh -lc "sed -n '2040,2200p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
functoriality of bar-cobar through the $L_\infty$-convolution
$\Convinf$
(Theorem~\ref{thm:operadic-homotopy-convolution}).
In particular, bar-cobar inversion preserves the full quantum
$L_\infty$ structure, not merely the dg~Lie shadow.
\end{remark}

\begin{remark}[Quasi-isomorphism of chain complexes vs chiral algebras]\label{rem:qi-vs-homology-iso}
The distinction is between two levels of structure:

\emph{Chain complex quasi-isomorphism.} A chain map $\psi: C^\bullet \to D^\bullet$ inducing an isomorphism $H^\bullet(\psi): H^\bullet(C) \xrightarrow{\cong} H^\bullet(D)$ on cohomology. This is the standard notion; a ``homology isomorphism'' and a ``quasi-isomorphism'' are the \emph{same thing} at the chain complex level.

\emph{Chiral algebra quasi-isomorphism.} An $A_\infty$ (or chiral algebra) morphism $\psi\colon \mathcal{A} \to \mathcal{B}$ whose linear component $\psi_1\colon \mathcal{A} \to \mathcal{B}$ is a chain complex quasi-isomorphism. Such a map preserves the full $A_\infty$ structure up to coherent homotopy. The distinction matters:
A chain complex quasi-isomorphism tells us only about $H^\bullet$ and need not respect multiplicative or $A_\infty$ structure, whereas a chiral algebra quasi-isomorphism gives a full equivalence in the derived category of chiral algebras, preserving all homotopy-theoretic information. For bar-cobar inversion to establish derived equivalences, the map $\Omega(B(\mathcal{A})) \to \mathcal{A}$ must be a quasi-isomorphism of \emph{chiral algebras}, not of chain complexes alone.

\emph{Example.}
Consider a dga $(C^\bullet, d, \mu)$ with:
\[\cdots \to 0 \to \mathbb{C} \xrightarrow{0} \mathbb{C} \to 0 \to \cdots\]

This has $H^0 = \mathbb{C}$, $H^i = 0$ for $i \neq 0$.

thinking
**Evaluating user remark**

It’s interesting that the target remark already exists. It seems the user wants to add a remark, but it might require some scrutiny to see if it aligns with their instructions or if it needs an upgrade. I need to strengthen the existing content to incorporate Keller’s deformation theory and Kontsevich formality while respecting curvature filtration. Also, I might want to search for Keller references and necessary dependencies for alternative proofs. I should ensure coherence and clarity in the remark.
thinking
**Clarifying deformation concepts**

I’m working through some concepts regarding the bar-cobar unit, which connects to the deformation retract at the tangent complex, specifically within the Koszul locus. I find that Kontsevich’s formality for FM_n(C) means the A-infinity structure on H*(B(A)) is formal here. I might need to refine my remark to emphasize the bar-cobar unit rather than the counit, and possibly include connections to the derived deformation functor. Searching the repository for Keller's deformation theory references will help clarify this further.
exec
/bin/zsh -lc "rg -n \"Proof of Theorem~\\\\ref\\{thm:bar-cobar-inversion-qi\\}\" -n chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
The theorem surface already contains an alternative-formality remark, so I’m checking whether it actually matches the Keller deformation-theory route the task asked for or only gestures at it. I’m now tightening that against the nearby deformation, formality, and coderived references before I edit.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1750,1915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Keller|ainfty-koszul-characterization|prop:en-formality|shadow-formality-low-degree|coderived-bar-degree-spectral-sequence|off-koszul-ran-inversion|higher-genus-inversion|quadratic closure|formal neighborhood|tangent complex|curvature filtration\" chapters metadata appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1750	\to L_{-1/2}(\mathfrak{sl}_2)$
  1751	fails to be a quasi-isomorphism: the surviving off-diagonal class
  1752	generates a non-trivial extension in
  1753	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$
  1754	that has no preimage in $L_{-1/2}(\mathfrak{sl}_2)$.
  1755	
  1756	\emph{Consistency with the Koszul-locus hypothesis.}
  1757	At generic level, the vacuum Verma module
  1758	$M(k\Lambda_0)$ has no singular vectors in the bar-relevant range,
  1759	$H^\bullet(\bar{B}^{\mathrm{ch}}(V_k(\mathfrak{sl}_2)))$ is
  1760	concentrated on the Koszul diagonal, and
  1761	Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
  1762	level $k = -1/2$ lies outside the Koszul locus because the
  1763	representation category
  1764	$\mathrm{KL}_{-1/2}(\mathfrak{sl}_2)$
  1765	(Arakawa~\cite{Arakawa17, Arakawa2016RationalAdmissible}) is a
  1766	non-semisimple finite tensor category whose singular vectors
  1767	obstruct the diagonal concentration.
  1768	For the critical-level analogue $k = -h^\vee = -2$, the
  1769	Feigin--Frenkel center~\cite{Feigin-Frenkel} causes an even more
 succeeded in 50ms:
chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
chapters/examples/deformation_quantization.tex:1790:where $\mathbb{T}_{A_F}$ is the tangent complex of~$A_F$.
chapters/examples/deformation_quantization.tex:1792:the cotangent complex is the free $A_F$-module
chapters/examples/deformation_quantization.tex:1883:where $\mathbb{T}_{\Spec(A)}$ is the tangent complex.
chapters/examples/deformation_quantization.tex:2058:in the tangent complex: the cusp's tangent complex has a longer
appendices/nonlinear_modular_shadows.tex:276:Proposition~\ref{prop:shadow-formality-low-degree},
appendices/nonlinear_modular_shadows.tex:512:\begin{definition}[Ambient complementarity tangent complex]
appendices/nonlinear_modular_shadows.tex:514:Given an ambient complementarity datum, define the \emph{ambient complementarity tangent complex}
appendices/nonlinear_modular_shadows.tex:532:\item the one-sided tangent complexes
appendices/nonlinear_modular_shadows.tex:539:\item if the pairing on $L_{\cA}\oplus K_{\cA}\oplus L_{\cA^!}$ is perfect and bar--cobar duality identifies the normal complex of one side with the shifted dual tangent complex of the other, then $T_{\cA}$ and $T_{\cA^!}$ are complementary Lagrangians in $T_{\mathrm{comp}}(\cA)$.
appendices/nonlinear_modular_shadows.tex:546:For the one-sided tangent complex $T_{\cA}$, the pullback of the ambient pairing reduces to the quadratic term in the differentiated Maurer--Cartan equation for the universal kernel. That quadratic term vanishes because the Maurer--Cartan equation is exactly the isotropy condition for the graph of the one-sided variation. The same argument applies to $T_{\cA^!}$.
appendices/nonlinear_modular_shadows.tex:548:If the cyclic pairing is perfect and bar--cobar duality identifies the normal complex of one side with the shifted dual tangent complex of the other, maximal isotropicity follows: the two sides are opposite polarizations of a single symplectic deformation problem.\qedhere
appendices/nonlinear_modular_shadows.tex:553:Assume the tangent complex $T_{\mathrm{comp}}(\cA)$ integrates to a filtered complete cyclic $L_\infty$-algebra presenting a formal moduli problem
appendices/nonlinear_modular_shadows.tex:575:The last item is decisive: the theorem is not only about tangent complexes at one point, but about a modular geometry stable under the basic operations of the theory.
appendices/nonlinear_modular_shadows.tex:601:In the pointed formal neighborhood this one-form is exact:
appendices/nonlinear_modular_shadows.tex:609:Because $i_+$ is Lagrangian, the normal complex of $\mathcal L_+$ in $\mathcal M$ is canonically identified with $T^*[-1]\mathcal L_+$. Formally along $\mathcal L_+$, the symplectic neighborhood theorem gives a pointed equivalence with the shifted cotangent bundle. Under this identification, $\mathcal L_+$ becomes the zero section. Since $\mathcal L_-$ is complementary to the zero section, it is the graph of a one-form $\alpha_+$. The graph of a one-form in a cotangent bundle is Lagrangian if and only if the one-form is closed, because the pullback of the canonical symplectic form is exactly $d\alpha_+$. In a pointed formal neighborhood every closed one-form is exact, which produces $S_+$.\qedhere
appendices/nonlinear_modular_shadows.tex:3061:(Proposition~\ref{prop:shadow-formality-low-degree}) is the
appendices/nonlinear_modular_shadows.tex:3781:(Proposition~\ref{prop:shadow-formality-low-degree}), the shadow obstruction tower
chapters/examples/w_algebras_deep.tex:83:where the right side is the ``thick'' flag variety with formal neighborhood structure.
chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1915,2035p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1915	This yields the coderived statement of clause~\textup{(2)} by a route
  1916	parallel to Keller's deformation-theoretic argument. It does not remove
  1917	the extra hypothesis in clause~\textup{(4)}: promotion from coderived
  1918	equivalence to an ordinary quasi-isomorphism still requires the same
  1919	collapse input, or the flat case $\kappa(\cA)=0$.
  1920	\end{remark}
  1921	
  1922	\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
  1923	\label{conj:koszul-wall-associated-variety}
  1924	\index{Koszul locus!derived wall}
  1925	\index{associated variety!Koszul wall}
  1926	Let $\mathrm{ChAlg}^{\mathrm{aug}}$ be the derived moduli stack of
  1927	augmented chiral algebras, and let
  1928	\[
  1929	\mathrm{Kos}
  1930	:=
  1931	\left\{
  1932	\cA \in \mathrm{ChAlg}^{\mathrm{aug}}
  1933	\;\middle|\;
  1934	\Omegach\bigl(\barBch(\cA)\bigr) \xrightarrow{\sim} \cA
collab wait(call_zDg43U1sqPaHzmChyTLrJJPM)
  receivers: 019d8694-5aab-7493-a4c3-e571937e4c29
exec
/bin/zsh -lc "sed -n '2400,2800p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\emph{Step 4:} At each genus, $\psi_g$ is natural in $\mathcal{A}$, so the 
genus-graded sum is also natural.
\end{proof}

\subsection{Applications to module categories}

\begin{remark}[Ordinary module Koszul duality is a separate genus-$0$ surface]
\label{rem:derived-equiv-scope}
The intrinsic higher-genus comparison proved in this chapter is the
bar-coalgebra statement of
Theorems~\ref{thm:positselski-chiral-proved} and
\ref{thm:full-derived-module-equiv-proved}: coderived/contraderived on
the bar-coalgebra surface, with ordinary derived reduction only on the
flat finite-type completed-dual loci. That does \emph{not} by itself
prove a broad ordinary-derived equivalence between general chiral
$\cA$-modules and $\cA^!$-comodules.

The ordinary module-theoretic Koszul duality used elsewhere in the
manuscript is the separate $\Eone$ complete/conilpotent theorem
exec
/bin/zsh -lc 'rg -n "prop:coderived-bar-degree-spectral-sequence" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
1913:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
2231:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
exec
/bin/zsh -lc "sed -n '1650,1880p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 For arbitrary complete augmented $\mathcal{A}$ with
 finite-dimensional graded bar pieces, the factorization counit
 \[
 \psi_X \colon \Omega_X \barB_X(\mathcal{A}) \longrightarrow \mathcal{A}
 \]
 is a coacyclic-equivalence: its cone
 \[
 K_\psi :=
 \operatorname{cone}\!\bigl(\Omega_X \barB_X(\mathcal{A}) \to \mathcal{A}\bigr)
 \]
 is coacyclic. Equivalently, $\psi_X$ is an isomorphism in
 $D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$, without any
 Koszulness hypothesis.

\item \emph{Coderived bar-degree filtration.}
 On the curved cone $K_\psi$, the bar-degree filtration yields the
 coderived spectral sequence of
 Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
 $E_1$ page is computed from the strict associated-graded differential
 $\operatorname{gr}^0 d$; the curvature relation
wait(call_zDg43U1sqPaHzmChyTLrJJPM) timed out:

thinking
**Searching for theorems**

I think I need to wait for a bit and ensure I have enough context. I should read the actual statements of the referenced propositions and theorems to avoid overclaiming anything. I'll search for specific lines and maybe look into relevant theorems, like the one about Koszul characterization. Additionally, I'll check the concordance lines referencing Theorem B and Keller classicality. It's all about inspecting the targeted contexts for clarity!
exec
/bin/zsh -lc 'rg -n "Keller" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1881:Keller's classicality theorem for formal $A_\infty$-algebras
1882:\cite{Keller01} reduces the problem to proving that the transferred
1892:Together with the Keller formality criterion of
1916:parallel to Keller's deformation-theoretic argument. It does not remove
codex
I have the live theorem surface. The existing remark is close, but it does not cleanly state the Keller tangent-complex retract, the formal-neighborhood interpretation, or the coderived descent through curvature filtration in the way this task requires. I’m verifying the referenced statements now so the revised remark stays within what the manuscript already proves.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1260,1338p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '970,1035p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1260	
  1261	If the minimal $A_\infty$-structure is \emph{formal}
  1262	($m_n = 0$ for all $n \geq 3$), then $\cA$ is chirally Koszul.
  1263	\end{proposition}
  1264	
  1265	\begin{proof}
  1266	Formality of the $A_\infty$-structure means the bar complex
  1267	$\barBgeom_X(\cA)$ is formal as a dg coalgebra: the natural map to
  1268	its cohomology $H^*(\barBgeom_X(\cA))$ is a quasi-isomorphism of
  1269	$A_\infty$-coalgebras. The higher products $m_n$ ($n \geq 3$) are
  1270	identified with the PBW spectral sequence differentials $d_{n-1}$
  1271	via the standard comparison (cf.\ \cite[Theorem~3.4.1]{LPWZ09}):
  1272	$m_n = 0$ for $n \geq 3$ is equivalent to $E_2 = E_\infty$, which
  1273	is the PBW collapse criterion of
  1274	Theorem~\ref{thm:pbw-koszulness-criterion}.
  1275	\end{proof}
  1276	
  1277	\begin{theorem}[Converse: chiral Koszulness implies formality;
  1278	\ClaimStatusProvedHere]
  1279	\label{thm:ainfty-koszul-characterization}%
 succeeded in 51ms:
   970	\end{theorem}
   971	
   972	\begin{remark}[Formality and deformation quantization]
   973	\label{rem:formality-dq}
   974	\index{deformation quantization!from $\Etwo$ formality}
   975	Kontsevich formality~\cite{Kon03} implies star products on
   976	arbitrary Poisson manifolds. In our framework
   977	(Chapter~\ref{chap:chiral-deformation}), $\Etwo$ Koszul duality
   978	exchanges the bar complex of polyvector fields with that of
   979	polydifferential operators, exchanging Poisson brackets with star products.
   980	The explicit Kontsevich star product arises from propagator integrals
   981	on $\overline{\Conf}_k(\mathcal{H})$, a specific $\Etwo$ bar complex
   982	model with boundary conditions.
   983	\end{remark}
   984	
   985	\begin{proposition}[\texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2};
   986	\ClaimStatusProvedElsewhere]
   987	\label{prop:en-formality}
   988	\index{formality!$\En$ operad}
   989	\textup{(}Fresse--Willwacher~\cite{FresseWillwacher20}, Idrissi~\cite{Idrissi22}\textup{)}\quad
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '300,390p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '917,985p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15360,15435p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:htt\\}|homotopy transfer theorem|\\\\label\\{thm:ainfty-koszul-characterization\\}|\\\\label\\{prop:en-formality\\}|\\\\label\\{prop:shadow-formality-low-degree\\}|\\\\label\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2388,2420p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   917	\label{thm:off-koszul-ran-inversion}
   918	\index{bar-cobar inversion!off-Koszul|textbf}
   919	\index{coderived category!bar-cobar inversion}
   920	Let $\cA$ be a complete augmented chiral algebra on~$X$ with
   921	$\barB_X^{\mathrm{fact}}(\cA)$ having finite-dimensional graded
   922	pieces. Then the bar-cobar counit
   923	\[
   924	\Omega_X \barB_X(\cA) \longrightarrow \cA
   925	\]
   926	is an isomorphism in
   927	$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$,
   928	without any Koszulness hypothesis on~$\cA$.
   929	Equivalently, its cone is coacyclic.
   930	\end{theorem}
   931	
   932	\begin{proof}
   933	Write $C = \barB_X^{\mathrm{fact}}(\cA)$ for the bar coalgebra
   934	(a conilpotent curved factorization coalgebra by
   935	Proposition~\ref{prop:bar-ran-well-defined}),
   936	and $\varepsilon \colon \Omega_X C \to \cA$ for the bar-cobar
 succeeded in 51ms:
   300	
   301	For (b): the PBW filtration by conformal weight is exhaustive,
   302	decreasing, preserved by all three components of the bar differential,
   303	and satisfies $m_0^{(g)} \in F^1$ because the curvature involves at
   304	least one OPE contraction. At associated graded level, the
   305	differential reduces to $\dzero$, which is strict.
   306	
   307	For (c): Verdier duality preserves the PBW filtration
   308	(it exchanges weight~$n$ generators with weight~$n$ cogenerators in
   309	the Koszul dual) and commutes with the bar differential. Hence it
   310	descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ and the
   311	eigenspace decomposition is well-defined.
   312	\end{proof}
   313	
   314	\begin{proposition}[Coderived bar-degree spectral sequence;
   315	\ClaimStatusProvedHere]
   316	\label{prop:coderived-bar-degree-spectral-sequence}
   317	\index{coderived category!bar-degree spectral sequence|textbf}
   318	\index{bar-cobar inversion!coderived filtration}
   319	Let
 succeeded in 51ms:
 15360	$m_r^{\mathrm{tr}} = 0$
 15361	$\;\Rightarrow\;$
 15362	$o_{r+1} = 0$
 15363	\textup{(}eq.~\eqref{eq:next-obstruction}\textup{)}
 15364	$\;\Rightarrow\;$
 15365	$\mathrm{Sh}_{r+1} = 0$.
 15366	In particular, $L_\infty$-formality at genus~$0$ through
 15367	degree~$r$ implies shadow termination at degree~$r$, with
 15368	no restriction on~$r$.
 15369	Proposition~\ref{prop:shadow-formality-low-degree} gives the
 15370	constructive content at $r = 2, 3, 4$; the above argument
 15371	extends to all finite degrees, completing the proof of
 15372	Theorem~\ref{thm:operadic-complexity-detailed}.
 15373	\end{remark}
 15374	
 15375	\begin{proposition}[Shadow--formality identification at low degree]
 15376	\label{prop:shadow-formality-low-degree}
 15377	\ClaimStatusProvedHere
 15378	\index{shadow obstruction tower!formality identification|textbf}
 15379	\index{Linfty@$L_\infty$-formality!shadow tower identification}
 exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{thm:htt\}|homotopy transfer theorem|\label\{thm:ainfty-koszul-characterization\}|\label\{prop:en-formality\}|\label\{prop:shadow-formality-low-degree\}|\label\{prop:coderived-bar-degree-spectral-sequence\}|\label\{thm:off-koszul-ran-inversion\})
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  2388	Chapter~\ref{chap:koszul-pairs}.
  2389	Items are listed in the meta-theorem's numbering, so that
  2390	\textup{(\ref{item:kp-def})}--\textup{(\ref{item:kp-dmod})}
  2391	in the concordance and in the chapter are identical.
  2392	
  2393	\medskip\noindent
  2394	\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
  2395	
  2396	\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
  2397	\item\label{item:kp-def}
  2398	 Chirally Koszul (Definition~\ref{def:chiral-koszul-morphism}).
  2399	 \hfill \checkmark
  2400	\item\label{item:kp-pbw}
  2401	 PBW spectral sequence on $\barBgeom(\cA)$ collapses at~$E_2$
  2402	 (Theorem~\ref{thm:pbw-koszulness-criterion}).
  2403	 \hfill \checkmark
  2404	\item\label{item:kp-ainfty}
  2405	 Minimal $A_\infty$-model has $m_n = 0$ for $n \ge 3$
  2406	 (Theorem~\ref{thm:ainfty-koszul-characterization}).
  2407	 Converse via Keller classicality.
exec
/bin/zsh -lc "rg -n \"label\\{thm:htt\\}|Homotopy transfer theorem|homotopy transfer theorem\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:ainfty-koszul-characterization\\}|label\\{prop:en-formality\\}|label\\{prop:shadow-formality-low-degree\\}|label\\{prop:coderived-bar-degree-spectral-sequence\\}|label\\{thm:off-koszul-ran-inversion\\}\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:12600:The homotopy transfer theorem
chapters/theory/higher_genus_modular_koszul.tex:15496:homotopy transfer theorem applied to the strict model
chapters/theory/higher_genus_modular_koszul.tex:15533:The homotopy transfer theorem
chapters/theory/higher_genus_modular_koszul.tex:16217: The homotopy transfer theorem computes the bracket
chapters/theory/en_koszul_duality.tex:3007:  The homotopy transfer theorem controls the dependence on
chapters/theory/en_koszul_duality.tex:3074:original derived center. The homotopy transfer theorem for
chapters/theory/bar_cobar_adjunction_inversion.tex:1874:and the homotopy transfer theorem
chapters/theory/higher_genus_foundations.tex:833: SDR exists and the homotopy transfer theorem produces the
chapters/theory/higher_genus_foundations.tex:1581: The homotopy transfer theorem
chapters/theory/higher_genus_foundations.tex:1634:The homotopy transfer theorem
chapters/theory/chiral_modules.tex:2656:of the general homotopy transfer theorem
chapters/theory/nilpotent_completion.tex:997:By the homotopy transfer theorem
chapters/theory/chiral_hochschild_koszul.tex:2299:The homotopy transfer theorem produces a minimal $L_\infty$-algebra
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:15376:\label{prop:shadow-formality-low-degree}
chapters/theory/coderived_models.tex:316:\label{prop:coderived-bar-degree-spectral-sequence}
chapters/theory/coderived_models.tex:917:\label{thm:off-koszul-ran-inversion}
chapters/theory/en_koszul_duality.tex:987:\label{prop:en-formality}
chapters/theory/chiral_koszul_pairs.tex:1279:\label{thm:ainfty-koszul-characterization}%
exec
/bin/zsh -lc "rg -n \"label\\{thm:htt\\}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/homotopy_transfer.tex:69:\label{thm:htt}

thinking
**Considering theorems**

I think I should read the theorem statement, even if it's not strictly necessary. Having that information might help me understand the problem better. It's always good to clarify things, right? A deeper look could provide insights that make everything just click into place. I feel like I might be overthinking it a bit, but I want to make sure I’m on the right track to help the user effectively.
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '48,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    48	\item Composing: the transferred structure on~$H$ rectifies
    49	 through bar-cobar to a strict model quasi-isomorphic to~$V$,
    50	 since $H \simeq V$ by the deformation retract. The tree
    51	 formula for $m_n^{\mathrm{tr}}$ is the explicit form of the
    52	 tensor trick (\cite{LV12}~\S10.3), whose summands are indexed
    53	 by planar trees with internal vertices decorated by the
    54	 operations $m_k^V$ and internal edges decorated by the
    55	 homotopy~$h$. Bar-cobar inversion re-absorbs these
    56	 higher operations into the differential of~$\Omega(B(H))$.
    57	\end{enumerate}
    58	\end{proof}
    59	
    60	\section{Historical origins}
    61	\label{sec:ainfty-historical}
    62	
    63	$A_\infty$ algebras were introduced by Stasheff~\cite{Sta63} to encode the homotopy-coherent associativity of loop space multiplication. The operadic viewpoint identifies them as algebras over the homology of the little intervals operad. For the role of bar-cobar duality in the chiral setting, see Chapter~\ref{chap:higher-genus}.
    64	
    65	\section{The homotopy transfer theorem}
    66	\label{sec:htt}
    67	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2178,2205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '1398,1420p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2178	\textup{(i)}$\Leftrightarrow$\textup{(iii)}:
  2179	
  2180	\smallskip\noindent
  2181	\textup{(ii)}$\Rightarrow$\textup{(iii)}:
  2182	$E_2$-collapse means all PBW differentials $d_r = 0$ for $r \geq 2$.
  2183	The $A_\infty$ products $m_n$ are identified with $d_{n-1}$ under
  2184	the HPL transfer, so $m_n = 0$ for $n \geq 3$
  2185	(Proposition~\ref{prop:ainfty-formality-implies-koszul}).
  2186	
  2187	\smallskip\noindent
  2188	\textup{(iii)}$\Rightarrow$\textup{(ii)}:
  2189	If $m_n = 0$ for $n \geq 3$, the minimal $A_\infty$-model is
  2190	strictly associative: $H^*(\barBgeom(\cA))$ is a dg algebra with
  2191	$m_2$ as the product and all higher operations trivial. The
  2192	bar spectral sequence of this formal $A_\infty$-algebra collapses
  2193	at~$E_2$ by the classicality theorem for formal $A_\infty$-algebras
  2194	(Keller). The chiral $A_\infty$ structure is computed fiberwise on
  2195	each FM stratum (Proposition~\ref{prop:shadow-formality-low-degree});
  2196	on each fiber the HPL transfer is an ordinary $A_\infty$ transfer
  2197	over a field, to which Keller's theorem applies directly. The PBW
 succeeded in 51ms:
  1398	factorization objects, and the coderived/contraderived
  1399	factorization categories on~$\operatorname{Ran}(X)$. Structural
  1400	theorems: stratified conservative restriction via Positselski's
  1401	injective characterization
  1402	(Theorem~\ref{thm:stratified-conservative-restriction}),
  1403	provisional embedding
  1404	(Proposition~\ref{prop:provisional-embedding}), bar functor
  1405	well-definedness
  1406	(Proposition~\ref{prop:bar-ran-well-defined}), and factorization
  1407	co-contra correspondence for conilpotent coalgebras
  1408	(Theorem~\ref{thm:fact-co-contra-general}).
  1409	\emph{Gap closed}: off-Koszul bar-cobar inversion
  1410	(Theorem~\ref{thm:off-koszul-ran-inversion}; proved via
  1411	stratified Positselski + conservative assembly).
  1412	
  1413	\smallskip\noindent
  1414	\textbf{H2\,: $\mathcal{W}_\infty$ H-level realization (MC4).}
  1415	\textbf{Resolved} by Theorem~\ref{thm:winfty-factorization-kd}: the
  1416	factorization target~$\mathcal{W}_\infty^{\mathrm{fact}}$ is
  1417	constructed via $\Einf$-sectorwise convergence at each finite
exec
/bin/zsh -lc "sed -n '1860,1945p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The strict Koszul lane of
Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
and~\ref{thm:spectral-sequence-collapse}. One packages the counit
\[
\psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
\]
with its adjoint unit into a filtered strong deformation retract on the
tangent complex of the bar-cobar deformation problem. After passing to
the PBW-associated graded quadratic model, that is, to the formal
neighborhood of the quadratic closure, the transferred coalgebra is
\[
\cA^i = H^*(\barB(\cA)),
\]
and the homotopy transfer theorem
\textup{(}Theorem~\textup{\ref{thm:htt}}\textup{)} supplies maps
\[
\cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
\Omega(\barB(\cA))
\]
exec
/bin/zsh -lc 'rg -n "deformation retract" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 312

appendices/homotopy_transfer.tex:9:cohomology via a deformation retract necessarily introduces higher
appendices/homotopy_transfer.tex:19:(Theorem~\ref{thm:rectification-meta}): given a deformation retract
appendices/homotopy_transfer.tex:50: since $H \simeq V$ by the deformation retract. The tree
appendices/homotopy_transfer.tex:77:Such data is called a \emph{strong deformation retract} (SDR).
appendices/homotopy_transfer.tex:129:\begin{definition}[Strong deformation retract data]
appendices/homotopy_transfer.tex:131:\index{strong deformation retract|textbf}
appendices/homotopy_transfer.tex:132:\index{SDR|see{strong deformation retract}}
appendices/homotopy_transfer.tex:133:A \emph{strong deformation retract} (SDR) from $V$ to $W$ is a tuple 
appendices/homotopy_transfer.tex:441:If $V \xrightarrow{p} H_*(V) =: W$ is a deformation retract:
appendices/homotopy_transfer.tex:516:deformation retract forces higher operations $m_k$ ($k \geq 3$) on the cohomology,
standalone/computations.tex:531:\mathrm{Vir}$ is a BRST reduction with a strong deformation retract
standalone/N6_shadow_formality.tex:302:bracket $[-,-]$. A \emph{deformation retract} onto $H^*(\fg)$ is
standalone/N6_shadow_formality.tex:465:Choose a deformation retract $(\gmodzero,h,\Ash_{*,0})$ with
appendices/combinatorial_frontier.tex:334:\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.
wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:570:  1902	For the resolved conifold: $\chi_{\mathrm{top}} = 2$ (the total space deformation retracts onto $\bP^1$) gives $\chi_{\mathrm{top}}/24 = 1/12$, but the DT computation gives $\kappa_{\mathrm{ch}} = 1$ (the conifold has a single BPS state contributing at genus~$1$).
audit_campaign_20260412_231034/F01_kappa_KM.md:206:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:66:Each entry is computed independently. For $E$: the quantum chiral algebra is the Heisenberg $H_1$ with $\kappa_{\mathrm{ch}} = 1$ (the level), while $\chi_{\mathrm{top}}(E) = 0$. For $K3$: the quantum chiral algebra is the $\cN = 4$ SCA with $\kappa_{\mathrm{ch}} = 2 = \dim_\C(K3)$, while $\chi_{\mathrm{top}}/24 = 1$. For $K3 \times E$: $\chi_{\mathrm{top}}(K3 \times E) = \chi(K3) \cdot \chi(E) = 24 \cdot 0 = 0$; the chiral de Rham complex has $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$ (proved by additivity); the BKM automorphic weight is the distinct quantity $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$ (see the $\kappa_{\mathrm{ch}}$-spectrum, Example~\ref{ex:kappa-spectrum-k3xe}). For the conifold: the resolved conifold has $\chi_{\mathrm{top}} = 2$ (the total space of $\cO(-1) \oplus \cO(-1) \to \bP^1$ deformation retracts onto the zero section $\bP^1$, so $\chi_{\mathrm{top}} = \chi(\bP^1) = 2$), giving $\chi_{\mathrm{top}}/24 = 1/12$, while $\kappa_{\mathrm{ch}} = 1$.
scripts/healing_fortification_40.py:156:   on the Koszul locus. Formality + deformation retract = qi.
scripts/healing_fortification_40.py:157:3. The off-locus extension to D^co: the deformation retract descends to the coderived

thinking
**Clarifying deformation units**

I'm considering how to express that the relevant unit in the deformation problem is the tangent-level inclusion from homotopy transfer, rather than the unit related to algebra-side adjunction. But then, I wonder if that might be a bit too technical or complex. Making sure to communicate clearly is key, so I'll think about how to explain that more simply or whether I should emphasize one part over the other.
exec
/bin/zsh -lc "rg -n \"Keller0|keller-icm|Keller06|Keller01\" -g '*.bib' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
bibliography/references.tex:796:\bibitem{Keller01}
bibliography/references.tex:799:\bibitem{Keller06}
chapters/connections/thqg_open_closed_realization.tex:854:(\cite[Theorem~1.2]{Keller06}).
chapters/theory/koszul_pair_structure.tex:742:Keller's theorem~\cite{Keller01}, an isomorphism on Hochschild
chapters/theory/en_koszul_duality.tex:2767: Keller~\cite{Keller06} shows that for derived-simple algebras
chapters/theory/chiral_modules.tex:2658:Keller~\cite{Keller01} and Merkulov~\cite{Merkulov99} for the
chapters/theory/bar_cobar_adjunction_inversion.tex:1882:\cite{Keller01} reduces the problem to proving that the transferred
chapters/theory/chiral_center_theorem.tex:2172:(Keller~\cite{keller-icm}, Theorem~3.4: for Koszul algebras,
chapters/theory/hochschild_cohomology.tex:929:\begin{proposition}[Morita equivalence {\cite{Keller06,Toen07}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:972:The result is standard: see Keller~\cite{Keller06},
chapters/theory/hochschild_cohomology.tex:1121:\mathrm{HH}^\bullet(A)$ is implicit in Keller~\cite{Keller06} and

thinking
**Referencing discussions on Keller and related topics**

I'm gathering precise file paths and line numbers from the repository, especially from `chapters/theory/bar_cobar_adjunction_inversion.tex`, to point out where Keller, deformation retracts, formality, Koszul locus, tangent complexes, and curvature filtration are discussed. I'll highlight theorem statements near line 1606, remarks around 1860-1925 that mention "Keller's classicality theorem" and deformation retracts, plus related propositions and definitions such as `prop:coderived-bar-degree-spectral-sequence`, `Definition\ref{def:bar-cobar-filtration}`, and `Theorem\ref{thm:bar-cobar-spectral-sequence}`. I’ll also check other files like `appendices/homotopy_transfer.tex` and `standalone/introduction_full_survey.tex` for supporting references while sticking to exact file and line citations without ranges. This way, I can confirm whether the repo already contains textual evidence to support alternative remarks on these topics.
exec
/bin/zsh -lc 'rg -n "def:bar-cobar-filtration" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2103:\begin{definition}[Bar-cobar filtration]\label{def:bar-cobar-filtration}
2144:Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
2145:Definition~\ref{def:bar-cobar-filtration} induces a spectral
2187:For the application to Theorem~\ref{thm:bar-cobar-inversion-qi}, the completeness statement in Definition~\ref{def:bar-cobar-filtration}(2) is supplied by its conilpotency/completion hypothesis: if $\bar{B}(\mathcal{A})$ is conilpotent in the sense of Definition~\ref{def:conilpotent-complete}, every element has finite bar degree, while in the augmentation-ideal completion regime the filtration is complete by construction.

exec
/bin/zsh -lc 'rg -n "thm:bar-cobar-spectral-sequence" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1673: Theorems~\ref{thm:bar-cobar-spectral-sequence}
1743:Theorems~\ref{thm:bar-cobar-spectral-sequence}
1789:\textup{(}Theorems~\ref{thm:bar-cobar-spectral-sequence}
1837:Theorems~\ref{thm:bar-cobar-spectral-sequence}
1862:bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
2133:The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
2138:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
2205:strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
2206:Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
2222:Theorems~\ref{thm:bar-cobar-spectral-sequence}
thinking
**Considering sources for citations**

I'm thinking about whether I should use Keller06, which is related to derived deformation theory, or just stick with Keller01 since it's been mentioned. The user specifically refers to Keller's derived deformation theory and Kontsevich formality. It might make sense to check both Keller01 and Keller06 to see if I can cite them together. I’ll need to investigate the bibliographic entries and references to make sure I’m including the right sources.
exec
/bin/zsh -lc "sed -n '790,806p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '806,812p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\bibitem{KL93}
D. Kazhdan and G. Lusztig, \emph{Tensor structures arising from affine Lie algebras, I--IV}, J. Amer. Math. Soc. \textbf{6} (1993), 905--947, 949--1011; \textbf{7} (1994), 335--381, 383--453.

\bibitem{Kee92}
S. Keel, \emph{Intersection theory of moduli space of stable $n$-pointed curves of genus zero}, Trans. Amer. Math. Soc. \textbf{330} (1992), no.~2, 545--574.

\bibitem{Keller01}
B. Keller, \emph{Introduction to $A$-infinity algebras and modules}, Homology, Homotopy and Applications \textbf{3} (2001), no.~1, 1--35, arXiv:math/9910179.

\bibitem{Keller06}
B. Keller, \emph{On differential graded categories}, International Congress of Mathematicians, Vol.~II, Eur. Math. Soc., Z\"urich, 2006, pp.~151--190, arXiv:math/0601185.

\bibitem{Terras1973}
A. Terras, \emph{Bessel series expansions of the Epstein zeta function and the functional equation}, Trans. Amer. Math. Soc. \textbf{183} (1973), 477--486.

\bibitem{Titchmarsh-zeta}
E. C. Titchmarsh, \emph{The Theory of the Riemann Zeta-function}, 2nd ed. (revised by D.~R. Heath-Brown), Oxford University Press, 1986.
 succeeded in 51ms:
E. C. Titchmarsh, \emph{The Theory of the Riemann Zeta-function}, 2nd ed. (revised by D.~R. Heath-Brown), Oxford University Press, 1986.

\bibitem{Toen07}
B. To\"en, \emph{The homotopy theory of dg-categories and derived Morita theory}, Invent. Math. \textbf{167} (2007), no.~3, 615--667, arXiv:math/0408337.

\bibitem{KhanZeng25}
A. Z. Khan and K. Zeng, \emph{Poisson vertex algebras and three dimensional gauge theory}, arXiv:2502.13227, 2025.
exec
/bin/zsh -lc 'rg -n "thm:spectral-sequence-collapse" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1674: and~\ref{thm:spectral-sequence-collapse}.
1744:and~\ref{thm:spectral-sequence-collapse} relies on
1790:and~\ref{thm:spectral-sequence-collapse}\textup{)} collapses at a
1838:and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
1863:and~\ref{thm:spectral-sequence-collapse}. One packages the counit
2198:\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
2223:and~\ref{thm:spectral-sequence-collapse} are statements about filtered
3850:(Theorem~\ref{thm:spectral-sequence-collapse}) \\[2pt]
3910:Theorems~\ref{thm:spectral-sequence-collapse}
exec
/bin/zsh -lc 'rg -n "coderived-bar-degree" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
1913:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
2231:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},

exec
/bin/zsh -lc 'rg -n "coderived.*spectral" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1666: coderived spectral sequence of
1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
1849:any class~$G/L$ collapse input for the coderived bar-degree spectral
1913:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
2231:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
exec
/bin/zsh -lc "rg -n \"label\\{prop:coderived-bar-degree-spectral-sequence\" -n chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc 'rg -n "prop:coderived-bar-degree-spectral-sequence" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 361

platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:24:`prop:coderived-bar-degree-spectral-sequence` in [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:304)
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1321:I should prepare for creating a new label that’s unique across volumes. First, I need to search to see if a similar label already exists. I’m considering using `prop:coderived-bar-degree-spectral-sequence` as a candidate for a theorem label. It’s crucial to ensure its uniqueness across the three volumes. I might use grep to help with that, and I’ll verify if any existing labels can be repurposed before proceeding with any edits.
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1334:label: \label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1413:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1554:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1631:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1804:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:1881:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2054:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2137:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2310:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2405:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2578:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2772:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:2945:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:3049:+\label{prop:coderived-bar-degree-spectral-sequence}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:3222:+ \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
platonic_rectification_20260413_114523/P02_thm_B_offlocus_upgrade.md:3378:+\label{prop:coderived-bar-degree-spectral-sequence}
thinking
**Rephrasing technical language**

I need to be careful with my phrasing around "PBW concentration" and "formal neighborhood." Instead of saying they are equal, I could express it like: "the PBW associated graded identifies the tangent complex with that of the quadratic closure." That makes it safer. I could also say, "the relevant formal neighborhood is governed by the quadratic closure." Since the user mentioned "Koszul locus," I should clarify it by saying, "in the sense that the tangent complex is controlled by the quadratic closure."
thinking
**Evaluating theorem proof**

I think I need to mention whether theorem B has a primary proof that’s sound. That might be important for the final evaluation. I should also consider exploring the results to compare, but maybe it isn't strictly necessary right now. I’ll definitely check if the agent has completed its task, as that could provide further insights. So, lots to consider, but I’m keeping track of it!
collab wait(call_7wYmnedIFI9uKvzFp0CQ3R4C)
  receivers: 019d8694-5aab-7493-a4c3-e571937e4c29
exec
/bin/zsh -lc "sed -n '280,360p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Omega_X \barB_X(\cA)$ and~$\cA$ is bounded below, exhaustive, and
preserved by~$\varepsilon$. Hence $K$ inherits a bounded-below
filtration. Its filtration-preserving differential is the strict
Chevalley--Cousin differential: the curved correction inserts at
least one diagonal contraction, so it lands in $F^1$ and disappears
from $\operatorname{gr}^0 K$. Thus each graded piece of
$\operatorname{gr} K$ is the cone of the strict
Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
Cousin-filtration argument gives that strict counit as a
quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
the filtered cone vanishes. This proof is independent of
Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
curvature-zero Cousin model together with Positselski's filtered
coacyclicity criterion. By
\cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
curved object with acyclic associated graded is coacyclic.
Therefore $K$ lies in the thick subcategory generated by
totalizations of short exact sequences and infinite direct sums, so
$\varepsilon$ is a coacyclic-equivalence and hence an isomorphism in
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
wait(call_7wYmnedIFI9uKvzFp0CQ3R4C) timed out:

thinking
**Updating Plans**

I’m thinking that maybe I don’t need to keep the explorer open. Perhaps I should consider closing it later. Should I make an update to my plan? It seems like substantial work isn’t necessary, but maybe it could be done. I haven’t been asked about it, though. Also, I really need to fill in PE-10 in the commentary before making any edits. That’s definitely a priority!
codex
```text
PE-10
genus: clause (1) on the Koszul locus; clause (2) on the coderived off-Koszul lane
degree: all bar degrees; no free bar-degree variable introduced
AP32 weight tag: NA
AP139 free-var audit: LHS vars {A} / {A,g} match RHS vars {A} / {A,g}
AP36: implication only; no new converse or iff claim
verdict: ACCEPT
```

I’m replacing the existing alternative-formality remark, not adding a new claim surface. The edit will make the second proof path explicitly Keller-style at the tangent-complex level and make the coderived descent go through the curvature filtration rather than by informal analogy.

thinking
**Summarizing precise file and line references for spectral-sequence proof dependencies**

I'm gathering exact file and line locations for key definitions, theorems, propositions, examples, and remarks that the spectral-sequence proof relies on. This includes citing the main proposition at `chapters/theory/coderived_models.tex:316`, related filtration and convergence theorems around lines 2103-2198 in `bar_cobar_adjunction_inversion.tex`, and supporting examples and alternative proofs with their locations. I'm carefully including references to remarks on formality and deformation retracts with line numbers to fully ground the spectral-sequence proof context.
exec
/bin/zsh -lc 'rg -n "Alternative proof via formality" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1858:\begin{remark}[Alternative proof via formality]
exec
/bin/zsh -lc 'rg -n "Proof strategy and filtration" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2101:\subsection{Proof strategy and filtration}
exec
/bin/zsh -lc 'rg -n "Spectral sequence construction" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2136:\subsection{Spectral sequence construction}
exec
/bin/zsh -lc "rg -n \"Example\\[Admissible-level failure\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -n "Admissible-level failure of bar-cobar inversion" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1704:\begin{example}[Admissible-level failure of bar-cobar inversion]
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1862,3 +1862,5 @@
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
@@ -1866,6 +1868,5 @@
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
@@ -1879,19 +1880,25 @@
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
@@ -1909,10 +1916,11 @@
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}


thinking
**Verifying edits and duplicates**

I need to re-read the edited section and verify everything. Maybe I should grep for banned words and compile the results. Cross-checking for duplicates could be useful, too—just in case any genuine duplicates surface during the search. I might use a command like `rg -n "Alternative proof via formality|bar-cobar deformation problem|FM formality obstructions"` for this. Additionally, using `sed` or `nl` could help inspect the patch. I'll check for line overflows as well. Let's take the time to read through!
codex
The remark is edited. I’m re-reading the touched surface now to make sure the new proof path is actually independent of the spectral-sequence lane and that the coderived extension is tied to the filtered-curved machinery already proved elsewhere.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1858,1924p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -i "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate|---|—" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "rem:bar-cobar-inversion-alt-formality|Alternative proof via formality|Keller01|prop:en-formality|prop:shadow-formality-low-degree|thm:ainfty-koszul-characterization|prop:coderived-bar-degree-spectral-sequence|thm:off-koszul-ran-inversion" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
1826:Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
1858:\begin{remark}[Alternative proof via formality]
1859:\label{rem:bar-cobar-inversion-alt-formality}
1893:\textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
1896:\textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
1898:Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
1901:theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
1921:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
1923:Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
2239:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
 succeeded in 52ms:
  1858	\begin{remark}[Alternative proof via formality]
  1859	\label{rem:bar-cobar-inversion-alt-formality}
  1860	The strict Koszul lane of
  1861	Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
  1862	bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
  1863	and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
  1864	spectral-sequence argument by the deformation problem controlled by the
  1865	bar coalgebra. Write
  1866	\[
  1867	\psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
  1868	\]
  1869	for the counit. After passing to the PBW-associated graded quadratic
  1870	model, one is working in the formal neighborhood governed by the
  1871	quadratic closure
  1872	\[
  1873	\cA^i = H^*(\barB(\cA)),
  1874	\]
  1875	and the homotopy transfer theorem
  1876	\textup{(}Theorem~\textup{\ref{thm:htt}}\textup{)} supplies maps
  1877	\[
 succeeded in 52ms:
1637: \textup{(}for the standard landscape, by
3009:\emph{Verification for the standard landscape.}
3011:perfectness for the standard landscape at non-critical,
3033:standard-landscape Koszul cases covered by
3041:\begin{proposition}[Perfectness for the standard landscape]
3177:standard landscape]
3192:standard landscape at the non-critical, non-degenerate levels for
3260:\emph{Standard-landscape verification.}
3350: landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
3356:standard landscape, Corollary~\ref{cor:lagrangian-unconditional}).
3572:object on $\operatorname{Ran}(X)$. We now show that this
4416:We now consider what happens when
5955:We now connect the abstract divisor-core theory to bar
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

codex
- **Bar-cobar inversion lane.** Theorem B is presented immediately after the “Bar-cobar inversion” section heading (`chapters/theory/bar_cobar_adjunction_inversion.tex:1606`); it is followed by Example 3.1.1 on admissible-level failure (`…:1704`) and the alternative-proof remark discussed below (`…:1858`). The proof narrative begins in the “Proof strategy and filtration” subsection (`…:2101`) and continues through the “Spectral sequence construction” subsection (`…:2136`), so those are the neighborhoods where the affirmation of Theorem B and its corollaries are worked out.

- **Spectral-sequence infrastructure.** Clause (3) of the theorem cites the bar-degree filtration of Definition \ref{def:bar-cobar-filtration} (`chapters/theory/bar_cobar_adjunction_inversion.tex:2103`), the square-zero spectral sequence of Theorem \ref{thm:bar-cobar-spectral-sequence} (`…:2138`), and its $E_2$ collapse on the Koszul diagonal from Theorem \ref{thm:spectral-sequence-collapse} (`…:2198`). The off-Koszul, curved case appeals to Proposition \ref{prop:coderived-bar-degree-spectral-sequence} (`chapters/theory/coderived_models.tex:316`), which produces a filtered cone whose curvature lives in $F^1$ and whose vanishing $E_1$ implies coacyclicity and hence the coderived equivalence mentioned in (2).

- **Existing Keller/deformation-formality discussion.** Remark “Alternative proof via formality” (`chapters/theory/bar_cobar_adjunction_inversion.tex:1858`) already packages the counit/unit into a filtered strong deformation retract on the tangent complex of the bar-cobar deformation problem, cites Keller’s classicality/formality criterion, references the Koszul locus, and observes that the curvature term sits in positive bar-degree filtration so the associated-graded retract is strict. That remark therefore already provides the Keller/deformation-retract/formality/tangent-complex discussion you mention; the standard SDR definitions in `appendices/homotopy_transfer.tex:129` can be cited if you want to expand those notions further.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1924,1932p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1924	statement of clause~\textup{(2)}. This does not remove the extra
  1925	hypothesis in clause~\textup{(4)}: promotion from coderived
  1926	equivalence to an ordinary quasi-isomorphism still requires the same
  1927	collapse input, or the flat case $\kappa(\cA)=0$.
  1928	\end{remark}
  1929	
  1930	\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
  1931	\label{conj:koszul-wall-associated-variety}
  1932	\index{Koszul locus!derived wall}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

codex
The write is stable on reread. I’m running the narrowest build check now so the remark is verified against the live TeX surface rather than only syntactically inspected.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

exec
/bin/zsh -lc 'sleep 2' in /Users/raeez/chiral-bar-cobar succeeded in 1.95s:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

codex
The fast build is running. I’m watching for a local LaTeX failure on the touched theorem lane rather than relying on prior aux state.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

codex
Pass 2 reduced the aux noise sharply, which is what I needed to see. I’m waiting for the build to settle so I can distinguish a real theorem-surface error from pass-dependent reference churn.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

 succeeded in 2m 43s:
   2634pp, 2005 undef citations, 7770 undef references, 2 rerun requests, 142 overfull, 271 underfull
── Pass 2 / 4 ──
   2774pp, 20 undef citations, 128 undef references, 1 rerun requests, 167 overfull, 359 underfull
── Pass 3 / 4 ──
   2774pp, 1 undef citations, 17 undef references, 0 rerun requests, 17 overfull, 53 underfull
── Pass 4 / 4 ──
   2776pp, 0 undef citations, 0 undef references, 1 rerun requests, 5 overfull, 33 underfull
⚠ Did not fully converge after 4 passes (Cit=0, Ref=0, Rerun=1).
  This is normal for page-count oscillation on large documents.
     Logs: .build_logs/tex-build.stdout.log and main.log

thinking
**Considering build and inspection**

I'm reflecting on the build status. It seems fine, but I might need to inspect the git diff to confirm. There's a possibility that the explorer agent timed out, so I should consider closing it. Overall, I'm thinking about keeping everything on track to ensure everything is working smoothly. Let's go ahead and check things out to avoid potential hiccups. I want to make sure everything is clear!
codex
The build completed without a local LaTeX error. It still reports one rerun request from page-count oscillation on the large document, but citations and references are clean, so the edited theorem surface is stable.

thinking
**Inspecting changes**

I need to inspect the differences in the summary, ensuring that only one file has changed. I could run commands like `git diff --stat` or check a relevant snippet. I'm also considering checking for cross-volume duplicates, but maybe that's not necessary. Using `git diff -- chapters/...` and possibly `rg` for label duplicates seems like a plan, or maybe I’ll just close the explorer since it's not useful right now.
exec
/bin/zsh -lc 'git diff -- chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Alternative proof via formality|bar-cobar-inversion-alt-formality\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1858:\begin{remark}[Alternative proof via formality]
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1859:\label{rem:bar-cobar-inversion-alt-formality}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}


thinking
**Investigating git diff issue**

I'm noticing that the output from git diff is empty, which seems odd. Maybe the diff is too large, or the file in question is untracked. It's also possible that the output is suppressed due to size limits. I wonder if git thinks there are no changes compared to HEAD, or if there are uncommitted modifications already in the repository. It might be a good idea to run git status for that file to confirm.
exec
/bin/zsh -lc 'git status --short -- chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

exec
/bin/zsh -lc 'git rev-parse --is-inside-work-tree' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
true
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

exec
/bin/zsh -lc "git show HEAD:chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1858,1928p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Alternative proof via formality]
\label{rem:bar-cobar-inversion-alt-formality}
The strict Koszul lane of
Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
spectral-sequence argument by the deformation problem controlled by the
bar coalgebra. Write
\[
\psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
\]
for the counit. After passing to the PBW-associated graded quadratic
model, one is working in the formal neighborhood governed by the
quadratic closure
\[
\cA^i = H^*(\barB(\cA)),
\]
and the homotopy transfer theorem
\textup{(}Theorem~\textup{\ref{thm:htt}}\textup{)} supplies maps
\[
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

collab close_agent(call_vnihDQdQiW749bGkXkigHvUo)
  receiver: 019d8694-5aab-7493-a4c3-e571937e4c29
close_agent(call_vnihDQdQiW749bGkXkigHvUo) completed: "- **Bar-cobar inversion lane.** Theorem B is presented immediately after the “Bar-cobar inversion” section heading (`cha…":
  receiver: 019d8694-5aab-7493-a4c3-e571937e4c29
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

codex
Revised the alternative-proof remark for Theorem B in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1858). The remark now states the second proof path in the requested Keller language: a filtered strong deformation retract on the tangent complex, the quadratic formal-neighborhood interpretation via `\cA^i = H^*(\barB(\cA))`, Kontsevich/Fulton--MacPherson formality feeding the transferred `A_\infty` structure, and descent to the coderived statement through the curvature/bar-degree filtration. No duplicate remark surface was found in Vol II or Vol III.

Verification: `make fast` completed without a local LaTeX error. Final pass reached `0` undefined citations and `0` undefined references; one rerun request remained from large-document page-count oscillation.

## Fortification Report
Theorem B (`thm:bar-cobar-inversion-qi`)
- PRIMARY PROOF: sound on the current local dependency surface
- SECONDARY PROOF: written
- TECHNIQUE: Keller deformation-theoretic tangent-complex retract + Kontsevich/Fulton--MacPherson `E_2` formality + coderived descent through curvature filtration
- CONDITION STATUS: genus-0 strict lane unconditional; higher-genus strict lane conditional on `MK:modular`; coderived off-locus unconditional under the theorem’s existing finite-dimensional graded-bar hypothesis
- CONFIDENCE: medium
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 102e2f2cd54bd7ca28311622ec080ec7ad70dfdf..dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1860,14 +1860,15 @@
 The strict Koszul lane of
 Theorem~\ref{thm:bar-cobar-inversion-qi} admits a second proof that
 bypasses Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. One packages the counit
+and~\ref{thm:spectral-sequence-collapse}. The point is to replace the
+spectral-sequence argument by the deformation problem controlled by the
+bar coalgebra. Write
 \[
 \psi \colon \Omega(\barB(\cA)) \longrightarrow \cA
 \]
-with its adjoint unit into a filtered strong deformation retract on the
-tangent complex of the bar-cobar deformation problem. After passing to
-the PBW-associated graded quadratic model, that is, to the formal
-neighborhood of the quadratic closure, the transferred coalgebra is
+for the counit. After passing to the PBW-associated graded quadratic
+model, one is working in the formal neighborhood governed by the
+quadratic closure
 \[
 \cA^i = H^*(\barB(\cA)),
 \]
@@ -1877,23 +1878,29 @@
 \cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
 \Omega(\barB(\cA))
 \]
-with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex.
-Keller's classicality theorem for formal $A_\infty$-algebras
-\cite{Keller01} reduces the problem to proving that the transferred
-$A_\infty$-structure on~$\cA^i$ is formal.
+with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
+bar-cobar deformation problem. In Keller's deformation-theoretic
+language, this identifies the formal moduli problem of
+$\Omega(\barB(\cA))$ with the one controlled by the transferred
+$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
+concentration says that this tangent complex is already governed by the
+quadratic closure.
 
-On the Koszul locus, that formality comes from configuration-space
-formality. The local fibers $\FM_m(\bC)$ are formal by the
-$\En$-formality package
+The remaining step is formality of the transferred
+$A_\infty$-structure on~$\cA^i$. The $\E_2$-formality map realized by
+Kontsevich-type configuration-space integrals on
+Fulton--MacPherson models
 \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
-and the transferred higher operations are computed fiberwise on the
-Fulton--MacPherson strata
+and the fiberwise identification of transferred higher operations with
+the corresponding FM-stratum operations
 \textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}}\textup{)}.
-Together with the Keller formality criterion of
-Theorem~\ref{thm:ainfty-koszul-characterization}, this implies that the
-higher $m_n$ vanish after transfer, so
-$\barB(\cA)$ is $A_\infty$-quasi-isomorphic to~$\cA^i$ with no higher
-corrections. Applying~$\Omega$ gives
+identify the higher $m_n$ with the FM formality obstructions.
+Theorem~\ref{thm:ainfty-koszul-characterization} then says that on the
+Koszul locus these obstructions vanish, so the transferred
+$A_\infty$-structure on~$\cA^i$ is formal. Keller's classicality
+theorem for formal $A_\infty$-algebras \cite{Keller01} upgrades the
+tangent-level retract to an $A_\infty$ quasi-isomorphism. Applying
+$\Omega$ gives
 \[
 \Omega(\barB(\cA))
 \;\simeq\;
@@ -1907,14 +1914,15 @@
 \textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
 on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.
 
-Off the Koszul locus the same deformation-retract package remains
-filtered by bar degree and curvature. Because the curvature term lies
-in positive filtration, the associated graded retraction is strict, so
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-identifies the cone of the factorization counit with a coacyclic object.
-This yields the coderived statement of clause~\textup{(2)} by a route
-parallel to Keller's deformation-theoretic argument. It does not remove
-the extra hypothesis in clause~\textup{(4)}: promotion from coderived
+Off the Koszul locus the same deformation-retract package survives
+after passing to filtered curved models. The transfer data respects
+the bar-degree filtration, and the curvature term lies in positive
+filtration, so the associated graded retract is strict.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+identifies the cone of the factorization counit as coacyclic, and
+Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
+statement of clause~\textup{(2)}. This does not remove the extra
+hypothesis in clause~\textup{(4)}: promotion from coderived
 equivalence to an ordinary quasi-isomorphism still requires the same
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}

tokens used
223,086
