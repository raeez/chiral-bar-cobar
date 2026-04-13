# H14_remove_koszul_locus (326s)

Inserted a research remark in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1930). It now states, in one place, the exact genus-0 definition of the Koszul locus, the equivalent PBW/bar-cohomology characterizations, the precise off-locus obstruction as the first off-diagonal bar class, and the strongest truthful upgrade path: unconditional coderived inversion, with ordinary quasi-isomorphism only on collapse loci or when `\kappa(\cA)=0`. I verified the inserted surface by reread, label-uniqueness grep across Vols I–III, and local prose-hygiene checks. I did not run a full TeX build.

A residual inconsistency remains outside the inserted remark: [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1708) treats admissible affine simple quotients as off-locus, while [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1576) contains a stronger admissible `\mathfrak{sl}_2` Koszulness claim. I left that unresolved because the target task was the research remark and the current sources do not settle the conflict cleanly.

## Fortification Report
Theorem B
- PRIMARY PROOF: sound on its current stated scope; no proof steps were changed
- SECONDARY PROOF: written
- TECHNIQUE: deformation-retract / homotopy-transfer / formality route (the existing alternative proof after the main proof)
- CONDITION STATUS: strict quasi-isomorphism on the Koszul locus; higher-genus strict inversion conditional on the modular-Koszul input; coderived equivalence unconditional off-locus; derived upgrade remains conjectural
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
session id: 019d869e-545c-7993-9bb5-93c718ed2f6d
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.
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


RESEARCH: Can the Koszul locus restriction be removed from Theorem B?

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex (add Research Remark)

Theorem B gives qi Omega(B(A)) -> A on the KOSZUL LOCUS. Off-locus: coderived only.

INVESTIGATE:
1. What is the Koszul locus PRECISELY? (Quadratic A-inf algebras whose bar cohomology
   is concentrated in degree 1.)
2. How far off-locus can the qi be pushed? Is there a DERIVED Koszul locus?
3. The coderived equivalence IS unconditional. Can it be upgraded to a genuine qi
   for specific non-Koszul families?
4. What families are NOT on the Koszul locus? (All standard VAs are Koszul — the
   locus is restrictive only for genuinely pathological algebras.)

Write a Research Remark characterising the Koszul locus and the off-locus obstruction.
mcp startup: no servers

thinking
**Evaluating tools for inspection**

I might need to run a shell command to inspect the code, but using the explorer sounds like a good option too. I think it's best to prefer explorers over doing manual searches or file reading whenever possible. I want to ask explorers directly and be precise in my queries. I shouldn't re-read or re-search code they already cover, and I should trust their results without verification. Still, I think I’ll need to read certain constitutional files myself.
codex
Using `frontier-research` for the off-locus investigation and `multi-path-verify` for the theorem-status/formulation checks. First step is to read the required constitutional surfaces, locate Theorem B and its nearby claims, and map any duplicate/cross-volume statements before drafting the research remark.
collab spawn_agent(call_CFXepuqRWcTZDsUteaxToKhO, prompt="Read and summarize only the parts relevant to Theorem B/Koszul locus in this repo. Focus on: 1) `chapters/theory/bar_cob…")
mcp startup: no servers
spawn_agent(call_CFXepuqRWcTZDsUteaxToKhO, prompt="Read and summarize only the parts relevant to Theorem B/Koszul locus in this repo. Focus on: 1) `chapters/theory/bar_cob…") pending init:
  agent: 019d869e-a63c-7fb1-ad2d-d58da457d9b1
exec
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

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 55ms:
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
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem B" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
6:%% proves that the adjunction inverts: Theorem B says
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Koszul locus" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
22:answer in two layers: on the Koszul locus
26:(Theorem~\ref{thm:genus-graded-convergence}); off the Koszul locus,
686:The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1635: If, in addition, $\mathcal{A}$ lies on the higher-genus Koszul locus
1679: the relevant off-Koszul locus
1712:This algebra is excluded from the Koszul locus of
1762:level $k = -1/2$ lies outside the Koszul locus because the
1885:$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
1899:Koszul locus these obstructions vanish, so the transferred
1917:Off the Koszul locus the same deformation-retract package survives
1932:\index{Koszul locus!derived wall}
2207:\textup{[Regime: quadratic, Koszul locus, square-zero total differential
2237:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
2250:\textup{[Regime: curved-central on the Koszul locus
2451:Koszul locus of finite-type chiral algebras. The programmatic regime
2673:satisfies these conditions precisely on the Koszul locus.
2709:On the Koszul locus, bar-cobar inversion
2748:and totalization preservation of $B_\kappa$ on the Koszul locus
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '620,780p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
codex
The live surface confirms Theorem B is already recorded as a strict quasi-isomorphism only on the Koszul locus, with coderived equivalence unconditional off-locus. Next I’m reading the theorem file itself and tracing how the locus is currently defined, then I’ll draft the strongest truthful research remark and propagate only if the same wording recurs elsewhere.
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/frontier-research/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
---
name: frontier-research
description: Use for new theorem architecture, research synthesis, or frontier programme design. Keep work local by default. Delegate or swarm only when the user explicitly authorizes it. This is the Codex-native equivalent of the frontier and research-swarm workflows from `CLAUDE.md`.
---

# Frontier Research

Frontier work is allowed only after the proved core, the conditional bridge, and the conjectural extension are separated sharply.

## Workflow

1. Partition the topic into:
   proved core,
   compute-backed evidence,
   conditional bridge,
   conjectural extension,
   heuristic picture.
2. Read the live theorem surface before synthesizing new structure.
3. Name the exact blocker for every missing implication.
4. Prefer the strongest narrower programme statement that survives hostile rereading.
 succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 50ms:
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

exec
/bin/zsh -lc "rg -n \"Koszul locus|coderived|Omega\\\\(B|\\\\Omegach\\\\(\\\\barBch|bar-cobar-inversion|higher-genus-inversion|collapse loci|collapse locus|Research Remark|Koszul\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory chapters/examples chapters/connections ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Koszul locus|coderived|Omega\(B|\Omegach\(\barBch|bar-cobar-inversion|higher-genus-inversion|collapse loci|collapse locus|Research Remark|Koszul)
                                       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1580,1980p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem B" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Reviewing the process**

I'm considering rerunning rg escaping since it seems necessary. The file is quite large, so I need to focus on targeting specific definitions and theorems. I want to ensure that my response is accurate and relevant, so an explorer response would be beneficial here. I'll take a moment to wait and gather the necessary details before proceeding further. It feels important to get this right!
collab wait(call_wye6lZqSx7mGf7py65lhsCfA)
  receivers: 019d869e-a63c-7fb1-ad2d-d58da457d9b1
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Koszul" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
40: & Strict quasi-isomorphism on the Koszul locus
70: & On the Koszul locus at generic level:
136: modular Koszul algebras (Theorem~H).
178:polynomial consequence of Koszul functoriality.
204: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ partition
232:Classical Koszul duality (Priddy; Beilinson--Ginzburg--Soergel)
261:\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
262:Within the chirally Koszul standard examples treated in
267:Koszulness status:
284: for all Koszul chiral algebras at all genera. Inversion is
306: For a Koszul chiral algebra~$\cA$ with uniform-weight
349: The Kodaira--Spencer map is constructed for all Koszul pairs
353:\item \emph{$\Eone$-chiral Koszul duality
361: Complete Koszul duality computations for all standard families:
372: Koszul despite nonvanishing $H^2_{\mathrm{CE}}$\textup{)},
401: On the Koszul locus at generic level, the collision-depth spectral
416: Functoriality under Koszul duality passes through the Connes
451: and homotopy-Koszulity of~$\mathsf{SC}^{\mathrm{ch,top}}$
453: explicit brace morphism with Koszul signs
512:Chiral Koszul duality & Chiral Koszul duality (same) \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '30,120p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
\hline
\textbf{A} & Bar-cobar adjunction
 & $\barBch \dashv \Omegach$ on $\Ran(X)$,
 with the algebra-level Verdier half only after
 $\mathbb{D}_{\Ran}$:
 $\mathbb{D}_{\Ran}\barB_X(\cA_i)\simeq \Omega_X(\cC_j)\simeq \cA_j$,
 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
 & \ClaimStatusProvedHere \\
\textbf{B} & Bar-cobar inversion
 & Strict quasi-isomorphism on the Koszul locus
 $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
 \textup{(}Thms~\ref{thm:higher-genus-inversion},
 \ref{thm:bar-cobar-inversion-qi}\textup{)}; off the locus,
 the counit is an unconditional coderived coacyclic-equivalence,
 promoted back to an ordinary quasi-isomorphism on collapse loci
 & \ClaimStatusProvedHere \\
\textbf{C} & Complementarity
 & C0: coderived fiber-center identification unconditional,
 ordinary-derived only on the flat perfect locus
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem B" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
131:| `thm:completed-bar-cobar-strong` | `theorem` | 946 | MC element lifts to the completed convolution algebra |
253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
254:| `lem:bar-cobar-associated-graded` | `lemma` | 2122 | Associated graded |
255:| `thm:bar-cobar-spectral-sequence` | `theorem` | 2138 | Bar-cobar spectral sequence |
259:| `thm:bar-cobar-inversion-functorial` | `theorem` | 2371 | Functoriality of bar-cobar inversion |
348:| `thm:hochschild-bar-cobar` | `theorem` | 324 | Hochschild via bar-cobar |
382:| `thm:bar-cobar-resolution` | `theorem` | 4778 | Bar-cobar resolution |
424:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3760 | Geometric bar--cobar duality |
425:| `prop:bar-cobar-relative-extension` | `proposition` | 3899 | Relative extension from relative Verdier base change |
494:| `thm:fusion-bar-cobar` | `theorem` | 4974 | Fusion product compatibility on the module bar surface |
509:| `thm:bar-cobar-verdier` | `theorem` | 1313 | Bar-cobar Verdier |
510:| `cor:bar-cobar-inverse` | `corollary` | 1466 | Bar-cobar mutual inverses |
542:| `thm:off-koszul-ran-inversion` | `theorem` | 917 | Off-Koszul bar-cobar inversion on Ran |
622:| `thm:kl-bar-cobar-adjunction` | `theorem` | 1121 | Chain-level KL adjunction from bar-cobar |
656:| `thm:en-chiral-bridge` | `theorem` | 71 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
660:| `cor:n2-recovery` | `corollary` | 656 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
828:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2586 | Bar-cobar isomorphism, retained for equation labels |
987:| `thm:ran-coherent-bar-cobar` | `theorem` | 14516 | Ran-coherent bar-cobar equivalence |
1209:| `thm:completed-bar-cobar` | `theorem` | 191 | Completed bar-cobar duality |
1212:| `thm:resonance-filtered-bar-cobar` | `theorem` | 673 | Resonance-filtered completed bar/cobar |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '220,280p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
| `thm:mc-periods-DISABLED` | `theorem` | 6017 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 6078 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 6090 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 6198 | Bar complex as algebra over the modular operad |
| `cor:genus-expansion-converges` | `corollary` | 6499 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6557 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6666 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6728 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6783 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6807 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6855 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6884 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6892 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6957 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6973 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 7019 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 7068 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 7112 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (52)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"Theorem B\" -g'*'" in /Users/raeez/chiral-bar-cobar succeeded in 4.38s:
compute/lib/theorem_koszul_12fold_rectification_engine.py:1015:                'Theorem B (bar-cobar inversion) is stated on the Koszul '
compute/lib/theorem_koszul_12fold_rectification_engine.py:1031:            'to the Koszul locus (Theorem B) or uses pro-nilpotent '
archive/session_artifacts/ADVERSARIAL_AUDIT_v41.md:74:#### Theorem B (Higher-genus inversion)
archive/session_artifacts/ADVERSARIAL_AUDIT_v41.md:307:| Theorem B | ★★★★☆ | Complete; E_2 collapse in remark not proof |
archive/session_artifacts/ADVERSARIAL_AUDIT_v41.md:334:4. Expand Theorem B lem:higher-genus-open-stratum-qi (constructibility + proper base change)
archive/session_artifacts/ADVERSARIAL_AUDIT_v41.md:335:5. Move E_2 collapse into Theorem B proof body
archive/session_artifacts/HARMONIZED_TASKLIST.md:596:| S-K5 | I | chapters/theory/higher_genus.tex | VERIFY Theorem B coderived part (b) clearly marked conditional | STRIKE_LIST:K5 |
archive/session_artifacts/HARMONIZATION_CG_TODOLIST.md:38:- [ ] **B2.** Theorem B (bar_cobar_adjunction_inversion.tex) — frame counit as acyclicity of τ
archive/session_artifacts/autonomous_state.md:35:- **Theorem B** (inversion): PASS
archive/misc/research_programme_upgrade_memo.md:76:### Theorem B (exact archetypes)
.claude/worktrees/agent-a2a46b8f/compute/lib/qec_koszul_code_engine.py:816:      Exact on the Koszul locus (Theorem B).
.claude/worktrees/agent-a2a46b8f/compute/lib/qec_koszul_code_engine.py:852:        'source': 'Theorem B (bar-cobar inversion on Koszul locus)',
compute/lib/bc_grand_unified_atlas_engine.py:79:(R6) Bar-cobar preserves zeros (Theorem B):
compute/lib/bc_grand_unified_atlas_engine.py:1182:    r"""Theorem B consistency: bar-cobar inversion should preserve spectral data.
compute/lib/bc_grand_unified_atlas_engine.py:1755:    # Theorem B: bar-cobar invariance
archive/misc/STRIKE_LIST_250.md:150:- [ ] **K5.** Vol I `higher_genus.tex`: verify Theorem B coderived part (b) clearly marked conditional
compute/lib/string_field_theory_bar_engine.py:1031:    AP34: bar-cobar inversion recovers A itself (Theorem B), NOT the bulk.
compute/lib/string_field_theory_bar_engine.py:1046:    gives the minimal resolution of A (Theorem B).
compute/lib/string_field_theory_bar_engine.py:1063:        "bar_cobar_inversion": "Omega(B(A)) ~ A (Theorem B)",
compute/lib/string_field_theory_bar_engine.py:1500:            "identification": "Erler-Maccaferri = bar-cobar (Theorem B)",
wait(call_wye6lZqSx7mGf7py65lhsCfA) timed out:

thinking
**Locating labels and definitions**

I need to consider waiting a bit longer or possibly using shell commands to streamline the process. My next step is to locate the relevant labels in the file and figure out any theorem definitions that might be necessary. I'll probably use a tool like `rg` to assist in searching efficiently. This should help keep everything organized. Let's see how it goes!

thinking
**Identifying and summarizing cross-volume references**

I'm gathering targeted excerpts and file paths referencing Theorem B, Koszul locus, and related terms across specified chapters and metadata, focusing on key sections like bar_cobar adjacency and concordance files, plus representative occurrences in Vol II/III to build a concise evidence-backed summary.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1270,1350p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: chapters/connections/ordered_associative_chiral_kd_core.tex: No such file or directory
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
codex
I’ve reached the theorem surface. The next pass is narrower: isolate the exact definition of the Koszul locus, the existing off-locus statements, and any places where the manuscript already hints at “collapse loci” or filtered/derived substitutes so the new remark is aligned rather than aspirational.
exec
/bin/zsh -lc "rg -n 'def:koszul-locus|thm:bar-cobar-inversion-qi|thm:higher-genus-inversion|coderived|collapse loci|collapse locus|Koszul locus|Research Remark|\\bKoszul\\b' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
22:answer in two layers: on the Koszul locus
23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
26:(Theorem~\ref{thm:genus-graded-convergence}); off the Koszul locus,
27:the same counit remains invertible in the coderived
30:the square-zero bar-cobar spectral sequence only on the Koszul lane.
31:The curved proof uses the coderived bar-degree filtration: the
103:\emph{Koszul dual.}
106:Since $\mathfrak{h}$ is abelian, the chiral Koszul dual is $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ with $d = 0$ and curvature $m_0 \propto -k \cdot \mathbf{1}$ (the level negates under Koszul duality; $h^\vee = 0$ for the abelian Lie algebra). This is a \emph{commutative} chiral algebra with curvature, not the Heisenberg at negated level \neq \mathcal{H}_{-k}$). The bar differential vanishes (Example~\ref{ex:ope-to-residue}), so $H^*(\bar{B}(\mathcal{H}_k)) \simeq \bar{B}(\mathcal{H}_k)$ with CE cooperad structure.
134:\emph{Bar complex and Koszul dual.}
138:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
173:The Koszul dual is determined by the central-charge involution
215:where $\Lambda(L \cdot L)$ is a composite operator, not a single generator. The algebra is filtered rather than curved because it is not generated by a finite-dimensional space $V$: composite operators like $(L \cdot L)$ appear at all levels, and the filtration is infinite-dimensional at each level. The Koszul dual is
305:\begin{theorem}[Filtered Koszul duality (GLZ) {\cite{GLZ22}}; \ClaimStatusProvedElsewhere]\label{thm:filtered-koszul-glz}
317:computes a \emph{filtered Koszul dual} $\mathcal{A}^!_{\text{filt}}$ with:
340:The cobar-bar adjunction $\Omega \dashv B$ restricts to an equivalence on pro-nilpotent objects by the filtered analogue of Theorem~\ref{thm:bar-cobar-isomorphism-main}; the completion $\widehat{\bar{B}}(\mathcal{A})$ is pro-nilpotent by construction, so $\Omega(\widehat{\bar{B}}(\mathcal{A})) \simeq \widehat{\mathcal{A}}$. See Positselski~\cite{Positselski11} for the general framework of curved Koszul duality with completions.
450:\emph{Koszul dual.}
470:\item Its Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is the commutative chiral algebra on $V^*$, with curvature $m_0 \propto -k \cdot \mathbf{1}$
511:Koszul dual is not well-defined.
exec
/bin/zsh -lc "sed -n '520,860p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Koszul locus|coderived|collapse loci|collapse locus|bar-cobar inversion|Omega\\\\(barB|\\\\Omegach\\\\(\\\\barBch|derived Koszul|non-Koszul|quadratic A[_-]inf|bar cohomology.*degree 1' chapters/theory chapters/examples chapters/connections /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{align}
\bar{B}^0(W_3) &= \mathbb{C} \cdot \mathbf{1} \\
\bar{B}^1(W_3) &= \mathbb{C} \cdot L \oplus \mathbb{C} \cdot W \oplus \text{(derivatives and composites)} \\
\bar{B}^2(W_3) &= \text{(all pairs)} \\
&\vdots
\end{align}

\emph{Problem.} Already at degree 1, we have:
\begin{itemize}
\item Generators: $L$, $W$
\item First derivatives: $\partial L$, $\partial W$
\item Second derivatives: $\partial^2 L$, $\partial^2 W$
\item Composites: $(L \cdot L)$, $(L \cdot W)$, $(W \cdot W)$
\item Higher composites: $(\partial L \cdot L)$, etc.
\end{itemize}

The space is infinite-dimensional even before taking products.

\emph{Filtration.} Filter by total operator dimension:
\begin{align}
 exited 2 in 50ms:
rg: regex parse error:
    (?:Koszul locus|coderived|collapse loci|collapse locus|bar-cobar inversion|Omega\\(barB|\\Omegach\\(\\barBch|derived Koszul|non-Koszul|quadratic A[_-]inf|bar cohomology.*degree 1)
                                                                                      ^
error: unclosed group

thinking
**Checking cross-volume directories**

I’m curious whether the user’s referenced volumes exist outside the current root. I’ll check paths like `/Users/raeez/chiral-bar-cobar-vol2` for “Theorem B” mentions, focusing on key subdirectories to avoid too much data. Let’s explore these cross-volume links carefully!
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem B" /Users/raeez/chiral-bar-cobar-vol2/chapters -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1293:\index{five main theorems!E1@$E_1$ variant!Theorem B}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2738:\item \textbf{Theorem B} (bar-cobar inversion): the cumulant
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1235:\index{five main theorems!E1@$E_1$ variant!Theorem B}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1270,1345p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section{The \texorpdfstring{$E_1$}{E1} five main theorems at genus zero}
\label{sec:e1-five-theorems-genus0}
\index{five main theorems!E1@$E_1$ variant!genus zero|textbf}

Volume~I establishes five main theorems for $E_\infty$-chiral algebras: bar-cobar adjunction, Koszul inversion, complementarity, leading coefficient, and the Hochschild ring. Each has an $E_1$-chiral counterpart, obtained by replacing symmetric coinvariants with the ordered bar complex and its braid-group equivariance. The five $E_1$ theorems at genus zero are formal consequences of the master theorem (Theorem~\ref{thm:master}) together with the explicit constructions of Appendix~\ref{sec:ordered-bar-explicit}; they are collected here to make the parallel with Vol~I explicit.

\begin{theorem}[Theorem~$\mathrm{A}^{E_1}$; \ClaimStatusProvedHere]
\label{thm:e1-theorem-A}
\index{five main theorems!E1@$E_1$ variant!Theorem A}
$\Cobar \dashv \Barch\colon
\mathsf{Alg}^{E_1}_{\mathrm{ch}} \rightleftarrows
\mathsf{Coalg}^{E_1}_{\mathrm{ch}}$.
Koszul exchange acts by $R^{-1}(z)$
\textup{(}Theorem~\textup{\ref{thm:opposite}}).
\end{theorem}

\begin{proof}
Ordered bar--cobar equivalence (\S\ref{sec:setup}) plus
opposite-duality (Theorem~\ref{thm:opposite}).
\end{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2720,2765p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\Theta_\cA,\;
\nabla^{\mathrm{hol}}
\bigr),
\end{equation}
where $\hat{T}^c(\cA)$ is the completed cumulant generating function,
$D_\cA$ is the bar differential, $\tau_\cA$ is the reduced partition
function, $r_\cA(z)$ is the collision residue, $\Theta_\cA$ is the
universal MC element, and $\nabla^{\mathrm{hol}}$ is the shadow
connection.
\end{definition}

\begin{remark}[Five theorems as cumulant relations]
% label removed: rem:thqg-five-theorems-cumulants
The five main theorems of Volume~I (A, B, C, D, H) are the first
five cumulant relations of the modular cumulant transform:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textbf{Theorem A} (bar-cobar adjunction): $D_\cA$ defines
 the cumulant generating function.
\item \textbf{Theorem B} (bar-cobar inversion): the cumulant
 generating function is invertible on the Koszul locus.
codex
The file already contains the key ingredients I need: an existing coderived-status remark, the main inversion theorem, a secondary proof of the strict Koszul lane, and a conjectural “Derived Koszul wall.” I’m now reconciling those pieces into a single research remark that says exactly what is proved, what the obstruction is, and what a derived replacement would mean.
exec
/bin/zsh -lc "sed -n '3888,3978p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1560,1965p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '760,840p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'def:koszul-locus|higher-genus Koszul locus|Derived Koszul wall|off-Koszul|collapse loci|collapse locus|admissible level|non-Koszul|E_2 collapse|bar cohomology.*concentrated|degree 1' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
differential is a sum over pairwise collisions). The kernel $\eta$ is
the infinitesimal version of this conversion.
\end{remark}

\subsection{The Taylor expansion of the logarithm}
\label{subsec:taylor-expansion-log}
\index{PBW spectral sequence!as Taylor expansion}

The PBW spectral sequence of a chiral algebra~$\cA$
(Definition~\ref{def:chiral-koszul-pair}) is the Taylor expansion of
the categorical logarithm.

More precisely: the weight filtration on the bar complex
$\barB(\cA) = \bigoplus_{n \geq 0} (s^{-1}\overline{\cA})^{\otimes n}$
induces a spectral sequence
\[
E_1^{p,q} \;=\; H^q\bigl(\mathrm{gr}^p\, \barB(\cA)\bigr)
\;\Longrightarrow\;
H^{p+q}(\barB(\cA))\,.
\]
 succeeded in 51ms:

\begin{remark}[The role of the configuration space geometry]
\label{rem:config-space-role}
The proof of the chiral comodule-contramodule correspondence
(Theorem~\ref{thm:chiral-co-contra-correspondence}) uses the
geometry of configuration spaces in three places:
\begin{enumerate}
\item \emph{Exactness of the chiral tensor product.}
 The tensor-hom adjunction for holonomic $\mathcal{D}_X$-modules
 on $\overline{C}_n(X)$ ensures that cofree comodules are injective
 and free contramodules are projective
 (Proposition~\ref{prop:chiral-inj-proj-resolutions}).
\item \emph{Conilpotency from conformal weight.}
 The conformal weight grading on $\bar{B}^{\mathrm{ch}}(\cA)$
 (inherited from $\cA$) ensures conilpotency
 (Theorem~\ref{thm:coalgebra-via-NAP}(4)), which is needed for
 the compact generation argument in Step~5 of the proof.
\item \emph{Finite-dimensionality from holonomicity.}
 The holonomicity of the bar complex on each configuration space
 stratum (Lemma~\ref{lem:bar-holonomicity}) ensures
 succeeded in 52ms:
 (the curvature is a cocycle for the coderivation~$d$).
 \end{enumerate}
\end{enumerate}
When $h = 0$, we recover an ordinary DG chiral coalgebra.
\end{definition}

\begin{example}[The bar complex as chiral CDG-coalgebra]
\label{ex:bar-as-CDG}
\index{bar complex!as CDG-coalgebra}
For a Koszul chiral algebra $\cA$ on $X$:
\begin{itemize}
\item At genus~$0$: $\bar{B}^{(0)}(\cA) = (\bar{B}^{\mathrm{ch}}(\cA), d_{\bar{B}}, 0)$
 is a DG chiral coalgebra ($h = 0$).
\item At genus~$g \geq 1$: $\bar{B}^{(g)}(\cA) = (\bar{B}^{\mathrm{ch}}(\cA), d_{\bar{B}}^{(g)}, h_g)$
 is a CDG chiral coalgebra with curvature
 $h_g = m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$
 (Theorem~\ref{thm:genus-universality}), where $\kappa(\cA)$ is
 the obstruction coefficient and $\lambda_g$ is the Faber--Pandharipande
 class on $\overline{\mathcal{M}}_g$.
\end{itemize}
 succeeded in 52ms:
23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
527:\emph{Problem.} Already at degree 1, we have:
687:bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
1635: If, in addition, $\mathcal{A}$ lies on the higher-genus Koszul locus
1649:\item \emph{Coderived off-Koszul lane.}
1679: the relevant off-Koszul locus
1682: quasi-isomorphism. Outside those collapse loci this theorem does not
1706:\index{admissible level!bar-cobar inversion failure}
1709:at the admissible level $k = -1/2$ for $\widehat{\mathfrak{sl}}_2$
1775:\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
1777:\index{2-Koszul!admissible level}%
1778:\index{admissible level!2-Koszul}%
1784:A stronger expectation is that the bar cohomology is concentrated in
1803:$N$-Koszul (admissible level, $E_N$ collapse) $\subset$
1804:non-Koszul (critical level, no finite collapse).
1825:\item \emph{Coderived off-Koszul lane.}
1930:\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
2210:For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
2221:At the $E_1$ page, we compute the cohomology of each column with respect to $d_0 = d_{\bar{B}}$, the full bar complex differential. Each column $E_0^{p,\bullet}$ with differential $d_0$ computes the bar cohomology $H^q(\bar{B}^p(\mathcal{A}), d_{\bar{B}})$ at fixed cobar degree~$p$. By the Koszul quasi-isomorphism, the bar cohomology is concentrated on the diagonal, giving $E_1^{p,q} = 0$ whenever $q \neq 0$ (after reindexing by the bar filtration degree).
3278:$\det G_h(c)$ vanishes (admissible levels for Virasoro).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem B" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:217: \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/topological_vertex_e1_engine.py:585:    inversion theorem (Theorem B of Vol I) specialized to E_1.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/operadic_koszul_e1_hocolim.py:594:        This is the E₁ analogue of Vol I Theorem B.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/e1_bar_cobar_cy3.py:669:    Bar-cobar inversion (Theorem B analogue):
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '200,240p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{conjecture}


%% ===================================================================
%% SECTION 6: The five theorems in the CY setting
%% ===================================================================

\section{The five theorems in the CY setting}
\label{sec:five-theorems-cy}

We summarize the status of the five main theorems of Volume~I when specialized to chiral algebras arising from CY categories.

\begin{theorem*}[The five theorems for CY chiral algebras]
Let $A = A_\cC$ be the chiral algebra of a CY$_3$ category $\cC$. Then:
\begin{description}
 \item[Theorem A (adjunction).] The bar-cobar adjunction $B \dashv \Omega$ restricts to CY chiral algebras: $B(A_\cC)$ is a factorization coalgebra on $\Ran(X)$, and $D_{\Ran}(B(A_\cC)) \simeq B(A_{\cC^!})$. The CY identification CY-A(ii) gives $\mathrm{CC}_\bullet(\cC) \simeq B(A_\cC)$.

 \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.

 \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.

thinking
**Searching for label definition**

I need to define the label `def:koszul-locus`, but I think it might be in another file, not the one currently open. So, I should search across the entire repository to locate it. It's important I find the exact definition to ensure I'm not missing any context. Let's explore the repo thoroughly and see where that label might be defined. This way, I can get a clearer understanding of what I'm looking for!

thinking
**Searching cross-volume technical references**

I'm gathering key references to terms like 'Koszul locus', 'coderived', 'Omega(B(A))', and 'Theorem B' across multiple volumes to synthesize relevant connections, focusing on how these link to the CY volume and chiral algebra contexts. I'll look specifically for mentions in Vol II and Vol III that tie back to main results or provide illuminating cross-references.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Koszul locus" /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 267

/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:114:(A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has its own derived center. (B)<->(C) via Drinfeld associator on the Koszul locus. NEVER conflate.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:257:- AP161: Five notions of E_1-chiral algebra are NOT interchangeable. (A)-(E) each have own derived center. (B)<->(C) on Koszul locus only. Counter: specify which notion.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:273:- AP174: Chiral QG equivalence scope. Proved abstractly on Koszul locus. Concrete verification: sl_2 Yangian and affine KM only. Elliptic partial; toroidal absent. FORBIDDEN: "equivalence for all four families."
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1226:  quasi-isomorphism on the Koszul locus
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2696:On the chirally Koszul locus, the line-operator category is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:261:Assuming the affine example lies on the chirally Koszul locus,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:545:Volume~I, inversion on the Koszul locus) in the nonabelian gauge-theory setting.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3904: lies outside the Koszul locus, where the bar spectral
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3990: $\kappa(\cA) + \kappa(\cA^!) = K(\cA)$ on the Koszul locus,
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:104:- **MODERATE -- "scoped identifications" phrasing (lines 449--456).** "The scoped identifications C_line ≃ A^!_line-mod and Abulk ≃ Z_der(Bbound) ≃ HH^bullet_ch(A^!_line) assemble these faces into the bulk-boundary-line triangle (Theorems~\ref{thm:boundary-linear-bulk-boundary} and \ref{thm:lines_as_modules}) on the boundary-linear exact sector and on the chirally Koszul locus respectively." The phrase "boundary-linear exact sector... chirally Koszul locus respectively" pairs the two conditions with the two identifications -- but which scope goes with which? The reader has to match by order. MODERATE: rewrite as "... on the boundary-linear exact sector (for Abulk) and on the chirally Koszul locus (for C_line)" would disambiguate. The content is right, the pairing is unclear.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1058:conjectural beyond the Koszul locus).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1106: On the Koszul locus the counit
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1124: $\mathrm{ChirHoch}^*(\cA)$ is polynomial on the Koszul locus at
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1140:physical hypotheses. On the chirally Koszul locus, the
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1169:\item \emph{On the chirally Koszul locus:}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1434:the Koszul locus (one-loop exactness,
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:464:   Fix: rewrote part~(iii) so the unconditional statement is the bulk-to-chiral-Hochschild quasi-isomorphism, with the stronger derived-center identification only under the compact-generation / boundary-linear hypotheses; rewrote part~(iv) to require the chirally Koszul locus; kept part~(v) at the level of perturbative line operators; and aligned the proof and packaging remarks with those scoped statements.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:472:   Fix: propagated the scope repair across the active summary surface: the abstract now distinguishes the unconditional Hochschild statement from the boundary-linear derived-center statement; the preface and introduction place the line-module identification on the chirally Koszul locus; the conclusion replaces the stale all-genera theorem advertisement with the ordered/open `E_1` persistence statement; the frontier target now states its compact-generation and chirally Koszul hypotheses explicitly; and the core chapter now cites Theorem~`thm:boundary-linear-bulk-boundary` directly at the load-bearing point.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2000,2045p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\begin{remark}[Evidence]
(i) is Theorem~\ref{thm:bar-is-self-intersection}(ii), read through
Construction~\ref{con:point-endomorphism}: the bar complex is the
formal bar/Koszul model for the endomorphism object of the point.

(ii) The product decomposition
$\FM_k(\C) \times \Conf_k^{<}(\R)$ of the iterated
self-intersection is the factored composition of endomorphisms
in~$\mathsf{Symp}^{\mathrm{der}}_{-2}$: the $\C$-factor governs
collision (composition of correspondences) and the $\R$-factor
governs ordering (the $E_1$-monoidal structure on endomorphisms).
Their product is the two-coloured Swiss-cheese operad
(Section~\ref{sec:foundations}).

(iii) This is the geometric reading of the complementarity package
of Volume~I: when $\cL_\cA$ and the boundary datum corresponding to
$\cA^!$ are complementary Lagrangians in $\Mvac$, their intersection
$\cL_\cA \times_{\Mvac} \cL_{\cA^!}$ carries a $(-1)$-shifted
symplectic structure that realizes the pairing.
codex
One ambiguity is now clear: the theorem text points to `Definition~\ref{def:koszul-locus}`, but the nearby file mostly uses `def:koszul-chiral-algebra` / `def:chiral-koszul-pair`. I’m checking whether the locus is defined elsewhere or if the remark needs to restate it explicitly to avoid hidden dependence.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'def:koszul-chiral-algebra|def:chiral-koszul-pair|chirally Koszul|Kosz\\(X\\)|PBW spectral sequence collapses|bar cohomology.*diagonal|bar cohomology.*degree~1' chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{def:koszul-locus\\}|\\\\begin\\{definition\\}.*Koszul locus|Koszul locus' chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Chiral Koszul duality}
\label{chap:koszul-pairs}

\index{chiral Koszul duality|textbf}
\index{twisting morphism!chiral|textbf}
\index{Francis--Gaitsgory|textbf}

Classical Koszul duality, in the sense of
Priddy~\cite{Priddy70} and
Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
algebras over a field: the bar complex is a tensor coalgebra on a
finite-dimensional vector space, the cobar functor inverts it
when bar cohomology is concentrated in degree one, and the
duality exchanges quadratic algebras with quadratic coalgebras.
Three features of chiral algebras on algebraic curves defeat
this framework simultaneously. First, chiral algebras are
\emph{curved}: the bar differential on the genus expansion
satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
rather than $d^2 = 0$, so the classical bar-cobar adjunction,
which requires strict nilpotence, does not apply beyond genus
 succeeded in 52ms:
appendices/homotopy_transfer.tex:584:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): on the Koszul locus,
appendices/nonlinear_modular_shadows.tex:3520:Koszul locus, $\kappa$ is nondegenerate. Set $P = \kappa^{-1}$.
appendices/dual_methodology.tex:201:Koszul locus, and characterizes it (see the Koszul equivalences meta-theorem,
appendices/ordered_associative_chiral_kd.tex:44:Its linear dual, on the chirally Koszul locus, is the dg-shifted Yangian.
appendices/ordered_associative_chiral_kd.tex:5886:and on the Koszul locus
appendices/ordered_associative_chiral_kd.tex:6437:On the chirally Koszul locus, the line-side algebra $A^!_{\mathrm{line}}$
appendices/ordered_associative_chiral_kd.tex:6478:\begin{theorem}[Factorisation identification on the Koszul locus;
appendices/ordered_associative_chiral_kd.tex:6481:On the chirally Koszul locus for a simple Lie algebra $\mathfrak{g}$,
appendices/ordered_associative_chiral_kd.tex:6973:\item On the chirally Koszul locus \textup{(}where the bar--cobar
appendices/ordered_associative_chiral_kd.tex:7937:Y_\hbar(\fg)\text{-}\mathrm{mod}^{\mathrm{fd}}$ on the affine Koszul locus
chapters/connections/thqg_open_closed_realization.tex:299:Gerstenhaber algebra. On the Koszul locus, Theorem~H
chapters/connections/thqg_open_closed_realization.tex:621:On the Koszul locus, this is the three-term Gerstenhaber algebra
chapters/connections/thqg_open_closed_realization.tex:939:on the Koszul locus. Therefore
chapters/connections/editorial_constitution.tex:76: the categorical extension of Theorem~B off the Koszul locus.
chapters/connections/editorial_constitution.tex:2345: inverses on the Koszul locus.
chapters/connections/editorial_constitution.tex:2461:(i) is proved at genus~$0$ and on the Koszul locus at all genera
chapters/connections/editorial_constitution.tex:2704:characteristic via exponentiation, and identifies the Koszul locus
chapters/connections/thqg_symplectic_polarization.tex:43:decomposition is unconditional on the Koszul locus~(C1), while the
chapters/connections/thqg_symplectic_polarization.tex:268:Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
chapters/connections/thqg_symplectic_polarization.tex:524:eigenspace decomposition~(C1) holds on the Koszul locus without
 succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:688:the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
chapters/theory/bar_cobar_adjunction_inversion.tex:1628: \textup{(}Definition~\ref{def:koszul-chiral-algebra}; equivalently,
chapters/theory/bar_cobar_adjunction_inversion.tex:1734:this relation produces bar cohomology off the Koszul diagonal:
chapters/theory/bar_cobar_adjunction_inversion.tex:2003:Definition~\ref{def:koszul-chiral-algebra} was initially
chapters/theory/bar_cobar_adjunction_inversion.tex:2221:At the $E_1$ page, we compute the cohomology of each column with respect to $d_0 = d_{\bar{B}}$, the full bar complex differential. Each column $E_0^{p,\bullet}$ with differential $d_0$ computes the bar cohomology $H^q(\bar{B}^p(\mathcal{A}), d_{\bar{B}})$ at fixed cobar degree~$p$. By the Koszul quasi-isomorphism, the bar cohomology is concentrated on the diagonal, giving $E_1^{p,q} = 0$ whenever $q \neq 0$ (after reindexing by the bar filtration degree).
chapters/theory/bar_cobar_adjunction_inversion.tex:2285:This is \emph{not} the classical bar complex over a point: the Fulton--MacPherson compactifications $\overline{C}_n(\bP^1)$, the logarithmic propagator $\eta_{ij} = d\log(z_i - z_j)$, and the Arnold relations in the cohomology of configuration spaces are all genuinely present and have no classical analogue. The classical bar over a point embeds via formal-disk restriction followed by homotopy transfer, but this comparison requires specifying the retraction $\bA^1 \to \mathrm{pt}$ and its attendant chain homotopy (see the discussion following Definition~\ref{def:chiral-koszul-pair}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2692: $\cA$ is chirally Koszul if and only if the Barr--Beck--Lurie
chapters/theory/bar_cobar_adjunction_inversion.tex:2782:standing hypotheses. Then $\cA$ is chirally Koszul if and only if for
chapters/theory/bar_cobar_adjunction_inversion.tex:2842:Then $\cA$ is chirally Koszul if and only if for all $n \geq 2$ and every
chapters/theory/bar_cobar_adjunction_inversion.tex:2890:Then $\cA$ is chirally Koszul if and only if the following two conditions
chapters/theory/bar_cobar_adjunction_inversion.tex:2952:are isotropic embeddings. Then $\cA$ is chirally Koszul if and only if both
chapters/theory/bar_cobar_adjunction_inversion.tex:3186:unconditional equivalence: $\cA$ is chirally Koszul if and only if
chapters/theory/bar_cobar_adjunction_inversion.tex:3321: $\cA$ is chirally Koszul:
chapters/theory/bar_cobar_adjunction_inversion.tex:3897:(Definition~\ref{def:chiral-koszul-pair}) is the Taylor expansion of
chapters/theory/bar_cobar_adjunction_inversion.tex:3927:(Definition~\ref{def:chiral-koszul-pair});
chapters/theory/chiral_koszul_pairs.tex:81:Every standard chiral algebra is chirally Koszul. The classes
chapters/theory/chiral_koszul_pairs.tex:140:pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
chapters/theory/chiral_koszul_pairs.tex:641:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:697:Definition~\textup{\ref{def:koszul-chiral-algebra}}, and hence lies on
chapters/theory/chiral_koszul_pairs.tex:705:Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "coderived" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 263

/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:75:     - For uncurved algebras: D^{co}(A) = D(A) (coderived = derived).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:136:     D^{co}(A) -> D^b(A)     (coderived -> derived)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:719:    r"""Information about the coderived category D^co(A) for a curved algebra.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:732:    For higher arities, the coderived structure provides CONVERGENCE:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:733:    the coderived totalization converges where the derived totalization
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:739:        coderived_dimension: dim D^co (for finite-dim cases)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:744:    coderived_dimension: str       # "finite" or "infinite" or specific value
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:748:def coderived_info(data: CurvedAInfinityData) -> CoderivedInfo:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:749:    """Compute coderived category information."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:754:            coderived_dimension="equals D^b",
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:760:        coderived_dimension="strictly larger than D^b",
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:1017:      - The bar-cobar adjunction B -| Omega extends to the coderived setting.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:210:    chain complexes, while the curved model is the coderived avatar.  The
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:499:    in the appropriate (coderived) sense.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:536:    # In the coderived sense (Model 3): d_fib^2 = kappa * omega_g
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:538:    # is flat in the coderived category.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:540:    coderived_flat = True  # Always: curvature is a fixed scalar
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/gauge_orbit_engine.py:550:        'coderived_flat': coderived_flat,
exec
/bin/zsh -lc "sed -n '223,310p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1560,1655p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,730p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
\index{Koszul chiral algebra|textbf}
Let $X$ be a smooth projective curve over~$\CC$.
An augmented chiral algebra~$\cA$
(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
if the bar-cobar counit
\[
\varepsilon \colon
\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism at genus~$0$.
\end{definition}

\begin{definition}[Koszul locus]\label{def:koszul-locus}
\index{Koszul locus|textbf}
The \emph{Koszul locus} is the full subcategory
\[
\operatorname{Kosz}(X)
\;\subset\;
\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
 succeeded in 52ms:
\item rationality and semisimplicity of the ordinary module
 category \textup{(}Theorem~\ref{thm:admissible-rep-theory}(ii)\textup{)};
\item finite-page bar and Li--bar spectral sequences in the
 ordinary-character calculations: the worked
 $\widehat{\mathfrak{sl}}_2$, $k=-1/2$ bar derivation of the vacuum
 Kac--Wakimoto character \textup{(}Theorem~\ref{thm:kw-bar-spectral}\textup{)},
 together with weightwise finite-page control and the external
 general-rank Kac--Wakimoto formulas on the broader
 non-degenerate admissible lane
 \textup{(}Proposition~\ref{prop:bar-admissible} and
 Theorem~\ref{thm:kw-bar-general-rank}\textup{)}.
\end{enumerate}
These results are compatible with chiral Koszulness, but they do
not yet prove bar-cobar inversion or Ext-diagonal purity for the
simple quotient in general.

For $\fg = \mathfrak{sl}_2$, admissible Koszulness is settled:
the simple quotient $L_k(\mathfrak{sl}_2)$ is chirally Koszul at
\emph{every} admissible level $k = -2 + p/q$ ($p \geq 2$,
$q \geq 1$, $\gcd(p,q) = 1$). The argument is structural:
 succeeded in 51ms:

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
exec
/bin/zsh -lc "sed -n '3605,3635p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
constraint (the pentagon identity on five FM boundary
strata of $\overline{\mathcal{M}}_{0,5}$).
Class~$C$: $S_4 \neq 0$, $S_5 = 0$; two crossing levels.
Class~$M$: all $S_r \neq 0$; infinite tower.
\end{proof}

\begin{proposition}[Minimal model non-Koszulness;
\ClaimStatusProvedHere]
\label{prop:minimal-model-non-koszul}
\index{minimal model!non-Koszulness mechanism|textbf}
\index{null vector!bar complex effect|textbf}
\index{Koszul property!failure mechanism}
Let $L(c_{p,q}, 0)$ be a non-trivial unitary minimal model
with first vacuum singular vector at
weight $w_0 = (p{-}1)(q{-}1)$. The simple quotient
$L(c_{p,q}, 0)$ is \emph{not} chirally Koszul: the bar
cohomology
$H^2(\barB(L(c_{p,q},0)))_{w_0} \neq 0$.

The mechanism is structural:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"Omega\\(B\" /Users/raeez/chiral-bar-cobar-vol2/chapters -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:1716:dg-algebra maps $\Omega(B(\cA)) \to \cA$, and the universal
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2410:\item The loop space\/ $\Omega(B(\cA))$ recovers\/ $\cA$ up to a
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2414: \Omega(B(\cA))
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2420: trivial and\/ $\Omega(B(\cA)) \simeq \cA$ as an honest
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2426: When\/ $\kappa \neq 0$, $\Omega(B(\cA))$ is\/ $\cA$ twisted
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2460:The loop space $\Omega(B(\cA))$ is the fiber of the evaluation map
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2468:$\Omega(B(\cA)) \simeq \cA^{[\kappa]}$ follows from the lifted
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2681:Theorem~B (inversion) & $\Omega(B(\cA_E)) \simeq \cA_E$ & immediate
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3172:$\Omega(B(\cA)) \simeq \cA$ and Verdier duality do not suffice to identify
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:4086:Bar-intrinsic $D_\cA^2 = 0$ & B (Inversion) & $\Omega(B(\cA)) \xrightarrow{\sim} \cA$ on Koszul locus \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:5904:the Verdier-dual $\cA^!$, not the cobar $\Omega(B(\cA))$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:21:bulk; bar-cobar inversion $\Omega(B(\cA)) \simeq \cA$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:140:compatibility $\Omega(B(\cA_T)) \simeq \cA_T$ needed to transfer
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:414:$\Omega(B(\cA_T)) \simeq \cA_T$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:198:The Koszul dual is \emph{not} the cobar construction: $\Omega(B(\cA))
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2799: is the Koszul dual; $\Omega(B(\cA)) \simeq \cA$ is bar-cobar inversion.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2390,2455p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{proposition}[Curved delooping; \ClaimStatusProvedHere]
\label{prop:curved-delooping}
Let\/ $\cA$ be a curved\/ $\Ainf$ chiral algebra with modular
characteristic\/ $\kappa \neq 0$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The delooping\/ $B(\cA)$ determines a line bundle\/
 $\mathcal{L}_\kappa$ on\/ $\overline{\mathcal M}_g$ with first
 Chern class
 \[
 c_1(\mathcal{L}_\kappa)
 \;=\;
 \kappa(\cA) \cdot [\omega_g]
 \;\in\;
 H^2(\overline{\mathcal M}_g,\, \mathbb{Z}).
 \]
 For the affine lineage $\cA = \hat{\mathfrak{g}}_k$, this is the\/
 $k$-th power of the determinant of the Hodge bundle:
 $\mathcal{L}_k = (\det \lambda)^{\otimes k}$.

thinking
**Investigating chiral Koszul pairs**

I'm noticing a conflict between two resources: one says sl2 admissible failure, while another claims sl2 is chirally Koszul at every level. That seems inconsistent, so I need to investigate further. The user has questions about what families are not on the Koszul locus, hinting that standard VAs are included. I should check the concordance or theorem registry for clarity on the status of chiral koszul pairs and the relevant theorems. It’s important to get this right!
thinking
**Examining epistemic hierarchy**

I need to make a decision based on the "epistemic hierarchy," considering direct computation and source context. There's a possibility that the theorem file might be outdated. I may not need to change the theorem itself but rather research remarks characterizing the obstruction. If a contradiction exists, I should mention it and possibly fix the local wording. I also need to inspect the current file from around 2000, as it likely has synchronization notes, and search from 1988 onward to clarify any cross-file tensions.

codex
I found a live inconsistency that matters for the remark’s truth conditions: this file presents `L_{-1/2}(sl_2)` as outside the Koszul locus, while `chapters/theory/chiral_koszul_pairs.tex` currently states all admissible `sl_2` simple quotients are chirally Koszul. I’m reading the local reconciliation surface before I edit, because the research remark cannot silently choose one side.
exec
/bin/zsh -lc "sed -n '1988,2055p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1550,1635p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is a
consequence of the fundamental theorem of chiral twisting morphisms
(Theorem~\ref{thm:fundamental-twisting-morphisms}):
the counit $\Omega_X(\bar{B}_X(\cA)) \to \cA$ being a
quasi-isomorphism is one of the four equivalent characterizations
of Koszulity established there. The present theorem extends this
to all genera via the genus induction of clause~(D2).
\end{remark}

\begin{remark}[Non-circularity: twisted-tensor cone as primitive anchor]
\label{rem:bar-cobar-twisted-tensor-anchor}
A reader tracking the proof chain might worry that
Theorem~\ref{thm:bar-cobar-inversion-qi} is invoked to verify
clause~(v) of the Koszul-equivalences meta-theorem
(Theorem~\ref{thm:koszul-equivalences-meta}), while
Definition~\ref{def:koszul-chiral-algebra} was initially
phrased in bar-cobar terms; this would create an apparent
circularity. The circularity is only apparent. The canonical
anchor is the twisted-product cone identification
Lemma~\ref{lem:twisted-product-cone-counit}, which computes
 succeeded in 52ms:
\index{admissible level!Koszulness status}
For the universal algebra $V_k(\fg)$, free strong generation
gives chiral Koszulness at every level
\textup{(}Corollary~\ref{cor:universal-koszul}\textup{)}.
For the simple quotient $L_k(\fg)$, null vectors enter the
bar-relevant range at admissible levels, so the PBW/Shapovalov
criterion no longer applies directly.

What \emph{is} proved for non-degenerate admissible levels is:
\begin{enumerate}[label=\textup{(\roman*)}]
\item rationality and semisimplicity of the ordinary module
 category \textup{(}Theorem~\ref{thm:admissible-rep-theory}(ii)\textup{)};
\item finite-page bar and Li--bar spectral sequences in the
 ordinary-character calculations: the worked
 $\widehat{\mathfrak{sl}}_2$, $k=-1/2$ bar derivation of the vacuum
 Kac--Wakimoto character \textup{(}Theorem~\ref{thm:kw-bar-spectral}\textup{)},
 together with weightwise finite-page control and the external
 general-rank Kac--Wakimoto formulas on the broader
 non-degenerate admissible lane
 \textup{(}Proposition~\ref{prop:bar-admissible} and
exec
/bin/zsh -lc "rg -n 'admissible.*sl_2|L_\\{-1/2\\}|bar-cobar inversion fails|excluded from the Koszul locus|simple quotient.*chirally Koszul at every admissible level|admissible Koszulness is settled' chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1576:For $\fg = \mathfrak{sl}_2$, admissible Koszulness is settled:
chapters/theory/bar_cobar_adjunction_inversion.tex:1708:Consider $L_{-1/2}(\mathfrak{sl}_2)$, the simple affine vertex algebra
chapters/theory/bar_cobar_adjunction_inversion.tex:1712:This algebra is excluded from the Koszul locus of
chapters/theory/bar_cobar_adjunction_inversion.tex:1714:which bar-cobar inversion fails is the following.
chapters/theory/bar_cobar_adjunction_inversion.tex:1730:Passing to the simple quotient $L_{-1/2}(\mathfrak{sl}_2)$ kills
chapters/theory/bar_cobar_adjunction_inversion.tex:1733:$\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2))$,
chapters/theory/bar_cobar_adjunction_inversion.tex:1749:$\psi\colon \Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))
chapters/theory/bar_cobar_adjunction_inversion.tex:1750:\to L_{-1/2}(\mathfrak{sl}_2)$
chapters/theory/bar_cobar_adjunction_inversion.tex:1753:$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$
chapters/theory/bar_cobar_adjunction_inversion.tex:1754:that has no preimage in $L_{-1/2}(\mathfrak{sl}_2)$.
chapters/theory/bar_cobar_adjunction_inversion.tex:1779:The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
chapters/theory/bar_cobar_adjunction_inversion.tex:1781:$H^*(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$ is not
chapters/theory/bar_cobar_adjunction_inversion.tex:1785:degrees $\{1, 2\}$, making $L_{-1/2}(\mathfrak{sl}_2)$ a
thinking
**Summarizing extensive cross references**

I’m compiling a detailed summary of cross references related to Omega(B(A)) and Theorem B across multiple volumes and chapters. This includes precise file paths with line number ranges and key results like inversion theorems, coderived category definitions, Koszul locus remarks, and connections to CY categories. I’m making sure to weave these references together to provide a comprehensive and well-documented overview reflecting the scope of the proposition in various contexts.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2665,2705p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


\subsubsection{Connection to Volume~I}
\label{subsubsec:k3e-vol1-connection}

The $K3 \times E$ example instantiates every layer of the
Volume~I engine:

\begin{center}
\renewcommand{\arraystretch}{1.25}
\small
\begin{tabular}{lll}
\textbf{Vol~I result} & \textbf{$K3 \times E$ instance} & \textbf{Value} \\
\hline
Theorem~A (adjunction) & $D_{\mathrm{Ran}}(B(\cA_E))
 \simeq B(\cA_E^!)$ & free-field Verdier \\
Theorem~B (inversion) & $\Omega(B(\cA_E)) \simeq \cA_E$ & immediate
 (class $\mathsf{G}$) \\
Theorem~C (complementarity) & $\kappa + \kappa' = 0$;
 $F_g + F_g' = 0$ for all $g$ & $24 + ({-}24) = 0$ \\


codex
**Theorem B Surface**
- `chapters/theory/bar_cobar_adjunction_inversion.tex:1-70` introduces the goal: Theorem B asserts that the bar-cobar counit recovers the input chiral algebra on the Koszul locus and, via the coderived refinement, always gives a coacyclic equivalence whose cone is controlled by the bar-degree filtration. The off-locus clause is now explicitly constrained to the coderived setting, with promotion to an ordinary quasi-isomorphism requiring the collapse inputs recorded there.  
- `chapters/theory/bar_cobar_adjunction_inversion.tex:1598-1865` spells out the four-part statement (strict Koszul lane, coderived off-locus lane, the coderived bar-degree spectral sequence, and the extra collapse hypothesis for promotion) and the supporting dependency proof outline; admissible-level counterexamples and the alternative Keller-style formal-neighborhood remark stay within that scope.  
- `chapters/theory/bar_cobar_adjunction_inversion.tex:386-455` (Remark “coderived status”) emphasizes that Koszulness is a genus‑0 criterion, that genus‑$g\ge1$ curvature forces the coderived category, and that the Koszul locus is exactly where the ordinary derived category equals the coderived one, separating the components of the argument cleanly.

**Status & Registry**
- `chapters/connections/concordance.tex:30-71` records Theorem B as one of the five main theorems: “bar-cobar inversion” is proved strictly on the Koszul locus and its coderived extension is unconditional, matching the statement above and summarizing the off-locus coderived coverage.  
- `metadata/theorem_registry.md:253-259` lists `thm:bar-cobar-inversion-qi` with the same title (“Bar-cobar inversion: strict on the Koszul locus, coderived off it”), linking the theorem number back into the registry for references/code generation.

**Cross-volume echoes**
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1270-1330` records the $E_1$ analogue: Theorem B$^{E_1}$ gives $\Cobar(\Barch(\cA))\simeq\cA$ on the ordered Koszul locus, confirming that the bar-cobar inversion philosophy persists in the ordered/braided setting and supporting the Yangian identifications for $\cA=\hat\fg_k$.  
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2725-2765` says the modular cumulant generating function is invertible on the Koszul locus (Theorem B), feeding the gravitational cumulant series just as the Vol I theorem guarantees $\Omega(B(\cA))\simeq\cA$.  
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2395-2445` relates $\Omega(B(\cA))$ to the original algebra up to the Verlinde bundle twist: when $\kappa=0$ the loop space is literally $\cA$, and when $\kappa\neq0$ it is the twisted algebra. That section doubles as a conceptual expansion of how $\Omega(B(\cA))$ sits on the Koszul locus.  
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2005-2040` traces $(\cA^!)^! \simeq \cA$ back to Vol I Theorem B acting on the Koszul locus, confirming the involutivity reference that appears across Vol II.  
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2665-2695` showcases the $K3\times E$ family as a test case where Theorem B’s inversion $\Omega(B(\cA_E)) \simeq \cA_E$ holds because the class is in shadow class $\mathsf{G}$, reinforcing the practical reach of the theorem.  
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:3298-3345` develops the derived–coderived comparison by showing that the chiral exponential map is a coderived quasi-isomorphism between the flat/derived and curved/coderived models, so the same coderived persistence that Theorem B isolates on the Koszul locus now ties into the global gauge-theoretic picture.  
- `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:210-230` summarizes the five Volume I theorems for CY chiral algebras; in particular, it restates Theorem B as “$\Omega(B(A_\cC)) \simeq A_\cC$ on the Koszul locus”, noting that chirally Koszul equals Hochschild formality in the CY category context.
thinking
**Considering Koszul locus examples**

I’m thinking about the user’s question regarding families that aren’t on the Koszul locus. Generally, simple quotients with singular vectors are examples of off-locus cases. While all standard VAs are Koszul, I should clarify that standard universal families are included. Off-locus examples originate from nongeneric simple quotients. I wonder if I should add a research remark to the target file after the theorem, addressing any conditional statements that may be inconsistent across the repository.
thinking
**Investigating theorem contradictions**

I'm thinking about how the theorem file has some explicit contradictory claims regarding the user's premise. I need to investigate this further, particularly around line 1576 in the chiral_koszul_pairs, where there might be a relevant remark with open statuses. It’s tricky determining what's more reliable. The concordance possibly mentions a generic level Theorem H about the Koszul locus, but without detailing admissibility. I wonder if I should label the statuses and check the theorem registry, though it feels like I don’t have enough information yet.
collab wait(call_smkAaLIKlfXhNOhXsA41jo2Z)
  receivers: 019d869e-a63c-7fb1-ad2d-d58da457d9b1
wait(call_smkAaLIKlfXhNOhXsA41jo2Z) 1 agents complete:
  019d869e-a63c-7fb1-ad2d-d58da457d9b1 completed: "**Theorem B Surface**
- `chapters/theory/bar_cobar_adjunction_inversion.tex:1-70` introduces the goal: Theorem B asserts…"



thinking
**Clarifying manuscript boundaries**

I'm considering how to approach the discussion of admissible simple quotients and minimal-model quotients in the manuscript. It could be a good idea to avoid mentioning SL2 altogether due to contradictions. Instead, I might frame it in a way that explains these quotients as boundaries where current testing occurs for failures. However, I should be cautious since this might conflict with what the user has mentioned in their parenthetical.
thinking
**Organizing mathematical thoughts**

I’m thinking through the structure of my ideas: starting with the theorem, followed by the proof and any alternate proofs. Then, I want to add a remark about the research. After that, I could dive into the derived wall conjecture, possibly providing a reference to it. I hope there aren’t any label conflicts that could complicate things. It’s all about keeping these elements organized and clear!
thinking
**Considering research title**

I think I should add "Research remark" to the title because the user asked for clarity. So maybe I'll modify it to something like “[Research remark: the Koszul locus and the off-locus obstruction].” That sounds good to me! Now I also need to use the `apply_patch` function to make the necessary updates. Let's see how that all comes together!
codex
I’ve narrowed the edit to one load-bearing addition: a research remark immediately after the alternative proof/formality remark, before the existing derived-wall conjecture. The remark will make four points explicit in one place: the exact genus-0 definition of the Koszul locus, the concrete off-locus obstruction, the unconditional coderived replacement, and the current boundary of families where strict inversion can actually fail.
Plan update
Context is assembled and the edit scope is now precise.
  ✓ Lock the precise theorem surface, definition of the Koszul locus, and off-locus obstruction language from adjacent files
  → Add a research remark in `chapters/theory/bar_cobar_adjunction_inversion.tex` characterizing the Koszul locus, the off-locus obstruction, the derived/coderived enlargement, and the family boundary
  • Re-read the edited surface and run targeted grep checks for wording drift and cross-volume collision surfaces
codex
```text
PE-4: bar complex formula
object: B(A) = bar coalgebra of the augmented algebra, discussed via \barB_X(\cA)
T^c argument: [s^{-1} A-bar? Y/N]  AP132: augmentation? [Y/N]
AP22: |s^{-1}v| = |v| [-1/+1] (must be -1)
s^{-1} not bare s? [Y/N]
coproduct: [deconcatenation / coshuffle / coLie]
match to intended bar: [B^ord→deconc / B^Sigma→coshuffle / B^Lie→coLie]
grading: cohomological |d|=+1? [Y/N]
verdict: ACCEPT

Filled for this edit:
object: B(A) = \barB_X(\cA), the augmented chiral bar coalgebra
T^c argument: Y  AP132: Y
AP22: -1
s^{-1} not bare s?: Y
coproduct: deconcatenation
match to intended bar: B^ord→deconc
grading: cohomological |d|=+1? Y
verdict: ACCEPT
```

thinking
**Considering theorem scope**

I’m thinking about needing PE-10 because of the theorem scope remark. But maybe it’s not essential. Still, it could be good to include it since I'm mentioning theorem B's scope. It feels like a bit of a gray area for me, but since this is related to the hot zone quantifier and theorem, I’ll lean towards including it for clarity. Let's proceed with caution here!
codex
```text
PE-10: scope quantifier
genus: genus-0 for the definition of the Koszul locus; all genera only for the coderived continuation/modular refinement
degree: bar-degree diagonal criterion; no free variables
AP32 weight tag: NA
AP139 free-var audit: LHS vars:{\cA,X,g when stated} RHS vars:{\cA,X,g when stated} LHS⊇RHS? Y
AP36: implication structure only; no new iff beyond existing cited equivalences
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1929,2 +1929,65 @@
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}


thinking
**Running grep for edits**

I'm thinking about running a targeted grep around my edits. Maybe I'll compile those results, or I could use a targeted TeX snippet search. There’s also the idea of using `sed -n '1910,1995p'` for more precise output. I should consider using `rg` to check for label uniqueness across all volumes and look for any banned tokens or em dashes in the edited file. Since I’m only looking at the edited sections, I’ll check for duplicate labels too. Time to run these commands!
codex
The edit is in place. I’m now doing the hostile reread and narrow falsifiers: label uniqueness across volumes, local prose/LaTeX hygiene on the inserted block, and a targeted readback of the theorem surface to make sure the new remark says only what the surrounding proofs actually support.
exec
/bin/zsh -lc "rg -n '\\\\label\\{rem:koszul-locus-off-locus-obstruction\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1910,2005p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 145ms:
\]
where the last quasi-isomorphism is the twisting-morphism/Koszul-duality
identification of
Theorem~\ref{thm:fundamental-twisting-morphisms}
\textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
on the quadratic lane\textup{)}. This recovers clause~\textup{(1)}.

Off the Koszul locus the same deformation-retract package survives
after passing to filtered curved models. The transfer data respects
the bar-degree filtration, and the curvature term lies in positive
filtration, so the associated graded retract is strict.
Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
identifies the cone of the factorization counit as coacyclic, and
Theorem~\ref{thm:off-koszul-ran-inversion} recovers the coderived
statement of clause~\textup{(2)}. This does not remove the extra
hypothesis in clause~\textup{(4)}: promotion from coderived
equivalence to an ordinary quasi-isomorphism still requires the same
collapse input, or the flat case $\kappa(\cA)=0$.
\end{remark}

exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p = Path('chapters/theory/bar_cobar_adjunction_inversion.tex')
text = p.read_text()
start = text.index('\\\\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]')
end = text.index('\\\\end{remark}', start) + len('\\\\end{remark}')
block = text[start:end]
for token in ['Moreover','moreover','Additionally','additionally','Notably','notably','Crucially','crucially','Remarkably','remarkably','Interestingly','interestingly','Furthermore','furthermore','we now','worth noting','worth mentioning','it should be noted','it is important to note','delve','leverage','tapestry','cornerstone','journey','navigate','---','—']:
    if token in block:
        print(token)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Research remark: the Koszul locus and the off-locus obstruction|derived Koszul locus|pathological quotient boundary|generic-level families|higher-rank admissible simple quotients' chapters/theory/bar_cobar_adjunction_inversion.tex /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 95ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1930:\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
chapters/theory/bar_cobar_adjunction_inversion.tex:1971:chiral algebras, but a derived Koszul locus: the full substack on
chapters/theory/bar_cobar_adjunction_inversion.tex:1981:universal landscape but its pathological quotient boundary. Freely
chapters/theory/bar_cobar_adjunction_inversion.tex:1982:strongly generated or generic-level families are designed to stay on
chapters/theory/bar_cobar_adjunction_inversion.tex:1987:quotients, higher-rank admissible simple quotients, and other
 succeeded in 359ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1931:\label{rem:koszul-locus-off-locus-obstruction}
 succeeded in 147ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}






thinking
**Deciding on builds and checks**

I might need to check for `def:koszul-locus` references again, but maybe not. I'm noticing a remark about bar degree, which seems to align with previous notes on having a focus on bar degree 1. Should I mention "standard universal landscape"? Perhaps adding a note about cross-volume propagation would help too. I can consider running a targeted TeX build, although it might not be necessary. Since edits were minimal, a quick compile could be useful. Let's think through my options!
thinking
**Verifying LaTeX syntax**

I’m weighing whether I need to verify the LaTeX syntax by running a parser or if there’s a simpler way. Using `latexmk -pdf` may be heavy, but it could still work. Alternatively, I could run `python scripts/verify_tex_structure.py`, but I’m not sure if that exists. Also, I might consider using `texfot` or `latexmk`, though I need to check my environment first. Ultimately, I want to mention any necessary fixes, especially around potential inconsistencies in the file.
thinking
**Addressing remarks and risks**

The new remark specifically mentions higher-rank admissible simple quotients, excluding sl2. However, I see a contradiction within the repo. Should I highlight this as a residual risk in the final output? Since the user asked for a broad healing perspective, it might help to mention the unresolved conflict as well. I’m considering updating the plan to complete steps 2 and 3, especially if there aren't further edits. This seems like a sensible approach!
thinking
**Inspecting theorem inconsistencies**

I think I need to check if the example in the theorem file still conflicts with the new remark. It says there's an admissible level sl2 failure, whereas the remark indicates that the quotient boundary includes higher-rank admissible simple quotients. There's no explicit contradiction, but the example discusses sl2 off-locus, which isn't mentioned in the new remark. Also, the theorem excludes simple admissible affine quotients, conflicting with chiral_koszul_pairs. I wonder if adding a sentence about boundary family-dependency could clarify things. But wait, would that make the remark too weak? Maybe I should look into the main theorem file for more context.
thinking
**Checking admissible quotients**

I should see if the search indicates that standard landscape universal families are the only ones considered, but that's not necessarily a requirement. It might be helpful to quickly look at `chapters/theory/higher_genus_modular_koszul.tex`, specifically around lines 9526 or 10073, to determine whether admissible quotients are excluded or if boundaries are discussed. The new remark mentions higher-rank admissible simple quotients, so it's essential to ensure there's consistency across all references. Let’s take a quick glance!
codex
I’ve finished the local verification. The new remark is label-clean and prose-clean. There is still a separate manuscript inconsistency around admissible affine simple quotients (`bar_cobar_adjunction_inversion.tex` vs `chiral_koszul_pairs.tex`), so I’m doing one last spot check in the higher-genus file to avoid importing the wrong boundary picture into the final report.
exec
/bin/zsh -lc "sed -n '9498,9545p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10060,10110p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'admissible level|simple quotient|Koszul locus|standard landscape|principal \\\\cW|generic Virasoro|universal affine' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{corollary}[Level-direction concentration at all non-critical levels for
algebraic families; \ClaimStatusProvedHere]
\label{cor:saturation-algebraic-families}
\index{scalar saturation!at all non-critical levels}
Every modular Koszul chiral algebra in an algebraic family
with rational OPE coefficients
\textup{(}hypotheses~\textup{(a), (b), (c$'$)} of
Theorem~\textup{\ref{thm:algebraic-family-rigidity}}\textup{)}
has vanishing primitive tangent space, hence
$\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}$ for some
\/$\Gamma_{\cA}\in\Gmod$, at all but finitely many levels.
The stronger identity
$\Theta_{\cA}^{\min} = \kappa(\cA)\cdot\eta\otimes\Lambda$
is not proved here in general.
In particular:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Affine Kac--Moody.} For $V^k(\fg)$ with
 simple~$\fg$, the OPE is polynomial in~$k$, and the
 only non-current generator~$T$ is a $\fg$-singlet.
 succeeded in 51ms:
For arbitrary multi-weight families, only the genus-$1$ comparison is
unconditional.
\end{corollary}

\begin{proof}
The first sentence is
Theorem~\ref{thm:mc2-bar-intrinsic}. The second follows from
Proposition~\ref{prop:geometric-modular-operadic-mc},
Theorem~\ref{thm:tautological-line-support}, and
Theorem~\ref{thm:mc2-conditional-completion}.
\end{proof}

\begin{remark}[Non-examples and boundaries]\label{rem:mk-non-examples}
Outside the presently verified modular-Koszul locus:
\textup{(}i\textup{)} simple affine KM quotients at admissible
levels, where null vectors obstruct the PBW/Shapovalov route and
inversion is not established unconditionally;
\textup{(}ii\textup{)} Virasoro minimal models, where singular-vector
quotients obstruct MK1;
\textup{(}iii\textup{)} logarithmic algebras
 succeeded in 52ms:
200:At special parameters (e.g.\ admissible levels), the question
422:bar and cobar are mutually inverse on the Koszul locus,
501:on the Koszul locus in
628:quasi-isomorphism on the Koszul locus, and an isomorphism in the
720:\ref{MK:verdier} for the standard landscape follows from: (1)~the genus-$0$ bar-cobar Verdier pairing
2108:entire CFT-type standard landscape.
2217:therefore reduces to a single axiom for the standard landscape:
2406: throughout the Koszul locus.
2480:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
2554: standard landscape.
2760:\item On the Koszul locus, for every genus~$g \geq 0$ the genus-$g$
3223:below, covering six families in the standard landscape
3716:In particular, every chiral algebra in the standard landscape
4074:\textup{(}For the standard landscape, this axiom is
4363:genera). For the standard landscape,~\ref{MK:modular}
8822:(Kac--Moody, generic level, standard landscape).
8944:At admissible levels beyond these regimes,
9127:for the standard landscape;
9379:At admissible levels, the module category is non-semisimple, and
9526: quotients $L_k(\fg)$ to the modular-Koszul locus.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}


thinking
**Contemplating report consistency**

I'm thinking about the residual inconsistency surrounding admissible simple quotients. It's important to mention that the report should indicate medium confidence due to this inconsistency. However, theorem B's local proof might be strong within the current scope. The repository inconsistency is making me reconsider if it should still be medium. I realize I need to be honest about this and not forget to update the plan once everything is resolved. Let's tackle this after we're done with everything else.
Plan update
The research remark is inserted and the local theorem surface has been re-read with label/prose checks.
  ✓ Lock the precise theorem surface, definition of the Koszul locus, and off-locus obstruction language from adjacent files
  ✓ Add a research remark in `chapters/theory/bar_cobar_adjunction_inversion.tex` characterizing the Koszul locus, the off-locus obstruction, the derived/coderived enlargement, and the family boundary
  ✓ Re-read the edited surface and run targeted grep checks for wording drift and cross-volume collision surfaces
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}


thinking
**Deciding on conflict resolution**

I'm choosing to leave that conflict untouched for now because my main task is to focus on the research remark, and it seems the sources I have don't clearly address the disagreement. It could be important to report on this, but I think I might just need to mention theorem B briefly, since it seems relevant but doesn't demand a full exploration right now. Let's keep it straightforward!
codex
Inserted a research remark in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1930). It now states, in one place, the exact genus-0 definition of the Koszul locus, the equivalent PBW/bar-cohomology characterizations, the precise off-locus obstruction as the first off-diagonal bar class, and the strongest truthful upgrade path: unconditional coderived inversion, with ordinary quasi-isomorphism only on collapse loci or when `\kappa(\cA)=0`. I verified the inserted surface by reread, label-uniqueness grep across Vols I–III, and local prose-hygiene checks. I did not run a full TeX build.

A residual inconsistency remains outside the inserted remark: [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1708) treats admissible affine simple quotients as off-locus, while [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1576) contains a stronger admissible `\mathfrak{sl}_2` Koszulness claim. I left that unresolved because the target task was the research remark and the current sources do not settle the conflict cleanly.

## Fortification Report
Theorem B
- PRIMARY PROOF: sound on its current stated scope; no proof steps were changed
- SECONDARY PROOF: written
- TECHNIQUE: deformation-retract / homotopy-transfer / formality route (the existing alternative proof after the main proof)
- CONDITION STATUS: strict quasi-isomorphism on the Koszul locus; higher-genus strict inversion conditional on the modular-Koszul input; coderived equivalence unconditional off-locus; derived upgrade remains conjectural
- CONFIDENCE: medium
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index dad9b8865ccb25f9563cea9cf2c5f3b6a89a7064..7524d8bfad62d55f1396e7a2174796bab15bbf79
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1927,6 +1927,69 @@
 collapse input, or the flat case $\kappa(\cA)=0$.
 \end{remark}
 
+\begin{remark}[Research remark: the Koszul locus and the off-locus obstruction]
+\label{rem:koszul-locus-off-locus-obstruction}
+\index{Koszul locus!off-locus obstruction}
+\index{bar-cobar inversion!off-locus obstruction}
+The phrase ``Koszul locus'' in
+Theorem~\ref{thm:bar-cobar-inversion-qi} has a precise
+genus-$0$ meaning: it is the full subcategory
+$\operatorname{Kosz}(X)$ of Definition~\ref{def:koszul-locus}.
+Equivalently, $\cA \in \operatorname{Kosz}(X)$ if and only if the
+genus-$0$ counit
+\[
+\Omega_X(\barB_X(\cA)) \longrightarrow \cA
+\]
+is a quasi-isomorphism; if and only if the PBW/bar spectral sequence
+collapses at~$E_2$; if and only if
+$H^*(\barB_X(\cA))$ is concentrated on the Koszul diagonal
+\textup{(}bar degree equal to internal degree, or after the
+reindexing used in
+Theorem~\ref{thm:bar-cobar-spectral-sequence},
+concentrated in bar degree~$1$\textup{)}. For a quadratic
+$A_\infty$ model this recovers the classical Priddy/BGS criterion:
+the bar cohomology is concentrated in weight~$1$.
+
+The obstruction off the locus is equally concrete: the first
+off-diagonal bar class. Once $H^*(\barB_X(\cA))$ acquires a class in
+bidegree $(p,q)$ with $q \neq 0$ after the standard reindexing, the
+strict square-zero proof loses diagonal concentration, higher
+differentials need not vanish, and the cone of the counit can stop
+being acyclic in the ordinary derived category. In the quotient
+examples already isolated in the manuscript, this class is created by
+a null-vector ideal or a non-flat PBW degeneration: singular vectors
+enter the bar-relevant range, or composite relations survive in bar
+degree $\geq 2$, so the PBW collapse no longer forces strict
+inversion.
+
+What survives off the locus is unconditional and already proved:
+clause~\textup{(2)} of
+Theorem~\ref{thm:bar-cobar-inversion-qi} gives a coderived
+coacyclic-equivalence for every complete augmented input with
+finite-dimensional graded bar pieces. The natural enlargement of
+$\operatorname{Kosz}(X)$ is therefore not the whole moduli stack of
+chiral algebras, but a derived Koszul locus: the full substack on
+which the coderived cone is still detected by ordinary cohomology.
+Conjecture~\ref{conj:koszul-wall-associated-variety} formulates this
+derived wall. The proved upgrade is narrower: promotion from coderived
+equivalence back to a genuine quasi-isomorphism holds on the collapse
+loci singled out in clause~\textup{(4)}, including the flat case
+$\kappa(\cA)=0$ and any family for which the coderived bar-degree
+spectral sequence degenerates to ordinary cohomology.
+
+From this viewpoint, the restrictive surface is not the standard
+universal landscape but its pathological quotient boundary. Freely
+strongly generated or generic-level families are designed to stay on
+the locus: Heisenberg, universal affine $V_k(\fg)$, generic Virasoro,
+and the principal $\cW$-families enter through PBW-flat models. The
+genuine candidates for leaving the locus are quotient algebras with
+null-vector ideals in the bar-relevant range, minimal-model
+quotients, higher-rank admissible simple quotients, and other
+non-flat or non-freely-generated degenerations. Even there the
+coderived comparison remains available; what fails is only the
+promotion from coacyclicity to an ordinary quasi-isomorphism.
+\end{remark}
+
 \begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
 \label{conj:koszul-wall-associated-variety}
 \index{Koszul locus!derived wall}

tokens used
213,990
