# R25_bar_cobar_adjunction_inversion (685s)

Edited [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex).

The repair takes the second option from the finding. I did not try to invent a curved/coderived spectral sequence that this file does not prove. Instead, I made the strict spectral-sequence lane explicitly square-zero only, routed off-locus claims to the coderived/contraderived comparison already proved in this file, and tightened the downstream Lagrangian summaries so they only use the Koszul surface where ordinary bar-cobar inversion is actually available. I also removed the corollary’s dependence on `conj:lagrangian-koszulness` by making its proof direct on that Koszul surface.

Verification: I re-read the modified theorem/proof blocks, checked the new label is unique, and checked the referenced labels used in the new text exist. I did not run a full LaTeX build.

## Rectification Summary
- [FIXED] finding — restricted `thm:bar-cobar-spectral-sequence` and `thm:spectral-sequence-collapse` to square-zero total differentials, added an explicit boundary remark that they do not apply to curved fiberwise `\dfib` with `\dfib^{2}=\kappa(\cA)\omega_g`, narrowed Theorem B’s off-locus scope to the proved completed/coderived comparison, and aligned the Lagrangian evidence/corollary with that boundary.


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
session id: 019d83b7-6679-7412-943f-2ca3d5074329
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


TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex

FINDINGS TO FIX:

1. [CRITICAL T02] Lines ~2789-2808, 3015-3041: Related to Theorem B off-locus argument.
   The strict spectral sequence at 2024-2077 is formulated for d^2=0 complexes.
   Used in the off-locus curved setting where d^2=kappa*omega_g.
   FIX: Either extend the spectral sequence to the curved/coderived setting, or restrict
   the off-locus claim to the coderived category (where the comparison IS proved).

Read the file, verify the finding, make the strongest truthful fix.
mcp startup: no servers
codex
Using `beilinson-rectify` for this theorem-lane repair. I’m first reading the required constitutional files plus the target section to verify exactly where the off-locus argument crosses from strict to curved complexes.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 52ms:
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

 succeeded in 50ms:
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
**Inspecting target file**

I need to inspect the target file, probably looking at the full file or the relevant sections. Using the explorer agent seems like a good option to locate what I need, especially the dependencies. I've already read some manually, so maybe I can focus on the target file and the lines around my previous findings. I could also use rg to find theorem labels and sections. Since the user specified a file, I’ll think about the best approach for verification later.
Plan update
Locking scope on the Theorem B off-locus lane in the assigned file, then rectifying the strict-versus-curved misuse with the strongest truthful replacement and re-reading the surrounding theorem surface.
  → Inspect the target file around the cited lines and identify the exact theorem/proof fragments using the strict spectral-sequence argument off the Koszul locus
  • Choose the strongest truthful repair: extend the argument only if the file already proves the needed curved/coderived comparison; otherwise narrow the off-locus statement to the coderived comparison actually established
  • Edit the target file minimally, then re-read the modified theorem/proof/status surface and run local label/reference/consistency checks
codex
I’ve loaded the constitutional layer and the rectification workflow. Next I’m reading the exact theorem surface and nearby dependencies inside the assigned file to see whether the strongest truthful fix is an internal extension to coderived spectral sequences or a claim restriction.
exec
/bin/zsh -lc "rg -n \"higher-genus-inversion|spectral sequence|d\\"'^2|coderived|curved|off-locus|Koszul locus|Theorem B|thm:higher-genus-inversion|thm:strictified-off-locus|curvature|comparison" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2740,3065p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1980,2095p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 269

3:%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
4:%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
6:%% proves that the adjunction inverts: Theorem B says
7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
22:answer: on the Koszul locus
27:a spectral sequence whose $E_2$~collapse, forced by the Koszul
30:bar degree. Off the Koszul locus, inversion persists in
31:progressively more structured forms: curved-central algebras
33:coderived categories
42:\label{sec:filtered-vs-curved-comprehensive}
47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
48:with central curvature), filtered-complete (requiring $I$-adic completion),
70:algebras admit direct bar-cobar inversion without completion; curved
101:\begin{example}[Heisenberg: curved quadratic]\label{ex:heisenberg-quadratic}
104:The double pole produces a \emph{curved} quadratic structure: the relation $J \otimes J \sim k \cdot \mathbf{1}$ is inhomogeneous (the right side is degree~0, not degree~2), so the bar complex has curvature $m_0 \propto k \cdot \mathbf{1} \neq 0$ for $k \neq 0$ (the curvature element is proportional to the vacuum, which is central). In the language of Definition~\ref{def:quadratic-chiral}, the Heisenberg is ``quadratic'' in the sense that the OPE involves at most two generators on the left side, but it is \emph{not} strictly quadratic (i.e., $m_0 \neq 0$).
107:\[\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*) \quad \text{(commutative chiral algebra on the dual space, with curvature)}\]
109:Since $\mathfrak{h}$ is abelian, the chiral Koszul dual is $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ with $d = 0$ and curvature $m_0 \propto -k \cdot \mathbf{1}$ (the level negates under Koszul duality; $h^\vee = 0$ for the abelian Lie algebra). This is a \emph{commutative} chiral algebra with curvature, not the Heisenberg at negated level \neq \mathcal{H}_{-k}$). The bar differential vanishes (Example~\ref{ex:ope-to-residue}), so $H^*(\bar{B}(\mathcal{H}_k)) \simeq \bar{B}(\mathcal{H}_k)$ with CE cooperad structure.
123:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 succeeded in 52ms:
\index{characteristic variety!alignment with FM stratification}
Let $\cA$ be a chiral algebra on~$X$ satisfying the standing hypotheses.
Then $\cA$ is chirally Koszul if and only if the following two conditions
hold for all $n \geq 1$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Purity)}\quad
 Each bar component $\barBch_n(\cA)$, viewed as a mixed Hodge module on
 $\overline{\Conf}_n(X)$, is \emph{pure} of weight~$n$.
\item \textup{(Characteristic variety alignment)}\quad
 The characteristic variety
 $\operatorname{Ch}(\barBch_n(\cA)) \subset T^*\overline{\Conf}_n(X)$
 is contained in the union of conormal bundles to boundary strata:
 \[
 \operatorname{Ch}\bigl(\barBch_n(\cA)\bigr) \;\subset\;
 \bigcup_{S \subset \partial \overline{\Conf}_n(X)}
 T^*_S \overline{\Conf}_n(X).
 \]
\end{enumerate}
\end{conjecture}

 succeeded in 52ms:
$\kappa(\cA) = \kappa(\cB)$ and $\kappa(\cA^!) = \kappa(\cB^!)$
simultaneously, since $K$ is an invariant of the bar coalgebra.
The non-vanishing conductor therefore provides a numerical
obstruction to derived Morita equivalence that has no counterpart
in the $K = 0$ families.
\end{remark}

\subsection{Proof strategy and filtration}

\begin{definition}[Bar-cobar filtration]\label{def:bar-cobar-filtration}
Define a decreasing filtration on $\Omega(\bar{B}(\mathcal{A}))$ by:
\[F^p\Omega(\bar{B}(\mathcal{A})) = \bigoplus_{n \geq p} \Omega^n(\bar{B}^n(\mathcal{A}))\]

This is the filtration by \emph{bar degree} (= cobar degree).

\emph{Geometric meaning.} $F^p$ consists of elements involving at least $p$ points
in configuration space. As $p \to \infty$, we are considering increasingly complicated
configurations.

\emph{Properties.}
 succeeded in 52ms:
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


thinking
**Inspecting code lines**

I need to check specific lines, particularly 2789-2808 and 3015-3041, to see if any theorem labels are truncated. It seems like the current output might be missing those exact lines, so I’ll open a narrower view around them, including lines 2024-2077 to inspect the theorem or lemma at 2024. I might use `nl -ba` and execute a command for better inspection. The developer suggests using an explorer for codebase questions, so I’ll spawn that to locate the arguments and dependency summaries more efficiently.
codex
The strict spectral-sequence theorem is indeed formulated as an ordinary filtered-complex argument, and the introduction already advertises coderived behavior off locus. I’m now isolating the exact theorem/proof paragraphs where the proof overreaches, so I can repair the off-locus statement without disturbing the proved Koszul-locus lane.
collab spawn_agent(call_aCmUp1Ze407pWgsBfWESGMQP, prompt="Inspect chapters/theory/bar_cobar_adjunction_inversion.tex only. Identify the exact theorem/proof/remark blocks around l…")
spawn_agent(call_aCmUp1Ze407pWgsBfWESGMQP, prompt="Inspect chapters/theory/bar_cobar_adjunction_inversion.tex only. Identify the exact theorem/proof/remark blocks around l…") pending init:
  agent: 019d83b8-0f62-7d03-8145-6228851c372d
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1980,2100p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\kappa(\cA) = \kappa(\cB)$ and $\kappa(\cA^!) = \kappa(\cB^!)$
simultaneously, since $K$ is an invariant of the bar coalgebra.
The non-vanishing conductor therefore provides a numerical
obstruction to derived Morita equivalence that has no counterpart
in the $K = 0$ families.
\end{remark}

\subsection{Proof strategy and filtration}

\begin{definition}[Bar-cobar filtration]\label{def:bar-cobar-filtration}
Define a decreasing filtration on $\Omega(\bar{B}(\mathcal{A}))$ by:
\[F^p\Omega(\bar{B}(\mathcal{A})) = \bigoplus_{n \geq p} \Omega^n(\bar{B}^n(\mathcal{A}))\]

This is the filtration by \emph{bar degree} (= cobar degree).

\emph{Geometric meaning.} $F^p$ consists of elements involving at least $p$ points
in configuration space. As $p \to \infty$, we are considering increasingly complicated
configurations.

\emph{Properties.}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2760,2820p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Content and implications]\label{rem:d-module-purity-content-bci}
Condition~(i) is the chiral analogue of the BGS diagonal purity:
$\operatorname{Ext}^i_A(k,k)$ carries a pure Hodge structure of
weight~$i$ if and only if $A$ is Koszul~\cite{BGS96}.
Condition~(ii) asserts that all OPE singularities are visible on the
FM boundary, with no hidden singularities in the interior of
configuration space. For regular holonomic $\mathcal{D}$-modules, this
forces $\barBch_n(\cA)$ to be a successive extension of rank-one flat
connections along boundary strata.

Together, (i) and (ii) imply FM boundary acyclicity
(Theorem~\ref{thm:fm-boundary-acyclicity}): purity forces the Leray
spectral sequence for $i_S^!\,\barBch_n$ to degenerate at~$E_1$, and
alignment puts the $E_1$ terms in degree zero.
In the representation-theoretic context, alignment translates to the
BGG resolution property: highest-weight modules have finite Verma
filtrations.
\end{remark}

\medskip
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2990,3060p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
dg~Lie algebra and follows from
$\omega([\Theta, \alpha], \beta)
= \omega(\alpha, [\Theta, \beta])$
applied to the Maurer--Cartan element~$\Theta_\cA$ that
twists the differential.

\smallskip\noindent
\emph{Step~4: perfectness.}
The pairing~$\omega$ induces a chain map
$\varphi \colon \fg|_n \to (\fg|_n)^\vee[-1]$
defined by $\varphi(\alpha)(\beta) := \omega(\alpha, \beta)$.
That $\varphi$ is a chain map follows from the
skew-adjointness in Step~3: $\varphi \circ d = d^\vee \circ \varphi$.
By Step~2, $\varphi$ is an isomorphism of graded vector spaces
at each chain degree (nondegenerate finite-dimensional bilinear
form $\Leftrightarrow$ the induced linear map is bijective).
A chain map that is an isomorphism of underlying graded vector
spaces is a chain isomorphism, hence a fortiori a
quasi-isomorphism. Therefore the pairing on~$\fg|_n$ is perfect.

exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2010,2088p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2776,2824p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3328,3388p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3000,3055p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2010	\[\text{Gr}^p\Omega(\bar{B}(\mathcal{A})) = \Omega^p(\bar{B}^p(\mathcal{A}))\]
  2011	
  2012	The induced differential on $\text{Gr}^\bullet$ is the \emph{bar complex differential} $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ (i.e., the full differential on $\bar{B}(\mathcal{A})$, lifted to each cobar tensor factor).
  2013	\end{lemma}
  2014	
  2015	\begin{proof}
  2016	By definition of associated graded:
  2017	\[\text{Gr}^p = F^p / F^{p+1} = \Omega^p(\bar{B}^p(\mathcal{A}))\]
  2018	
  2019	The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
  2020	\end{proof}
  2021	
  2022	\subsection{Spectral sequence construction}
  2023	
  2024	\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
  2025	\label{thm:koszul-spectral-sequence}
  2026	The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
  2027	sequence:
  2028	\[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
  2029	converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
 succeeded in 51ms:
  2776	filtrations.
  2777	\end{remark}
  2778	
  2779	\medskip
  2780	
  2781	\subsubsection{Lagrangian criterion in the shifted-symplectic deformation space}
  2782	
  2783	Ambient complementarity
  2784	(Conjecture~\ref{conj:ambient-complementarity},
  2785	Theorem~\ref{thm:ambient-complementarity-fmp}) equips the modular
  2786	deformation space with a $(-1)$-shifted symplectic structure.
  2787	Koszulness should be Lagrangian transversality.
  2788	
  2789	\begin{conjecture}[Conditional Lagrangian characterization of chiral Koszulness;
  2790	\ClaimStatusConjectured]%
  2791	\label{conj:lagrangian-koszulness}%
  2792	\index{Koszulness!Lagrangian characterization}
  2793	\index{Lagrangian!transversality and Koszulness}
  2794	\index{shifted-symplectic!Lagrangian criterion for Koszulness}
  2795	Suppose the ambient complementarity tangent complex $T_{\mathrm{comp}}(\cA)$
 succeeded in 51ms:
  3328	this coalgebraic memory into an algebraic one, turning
  3329	$\barB_X(\cA)$ into the dual algebra~$\cA^!_\infty$ without any
  3330	loss of information. The adjunction
  3331	$\Omegach \dashv \barBch$ and the intertwining
  3332	$\mathbb{D}_{\operatorname{Ran}} \circ \barB_X \simeq \barB_X \circ
  3333	(-)^!$ are therefore two faces of a single structure: the bar functor
  3334	translates algebraic duality (Koszul) into geometric duality
  3335	(Verdier), and the cobar functor translates back. Every other
  3336	duality in the programme, whether Poincar\'e--Koszul on manifolds,
  3337	Serre on moduli, or the $c \mapsto 26 - c$ involution on the Virasoro
  3338	line, is a specialization of this single adjunction acting on
  3339	different geometric inputs.
  3340	\end{remark}
  3341	
  3342	\begin{remark}[Curvature and coderived categories]\label{rem:curvature-coderived}
  3343	\index{coderived category!bar-cobar}
  3344	\index{curvature!coderived category}
  3345	When curvature is present, i.e., when the genus-$1$ obstruction
  3346	$m_0^{(1)} = \kappa(\cA) \cdot \lambda_1 \neq 0$ (as it is for all
  3347	Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
 succeeded in 52ms:
  3000	defined by $\varphi(\alpha)(\beta) := \omega(\alpha, \beta)$.
  3001	That $\varphi$ is a chain map follows from the
  3002	skew-adjointness in Step~3: $\varphi \circ d = d^\vee \circ \varphi$.
  3003	By Step~2, $\varphi$ is an isomorphism of graded vector spaces
  3004	at each chain degree (nondegenerate finite-dimensional bilinear
  3005	form $\Leftrightarrow$ the induced linear map is bijective).
  3006	A chain map that is an isomorphism of underlying graded vector
  3007	spaces is a chain isomorphism, hence a fortiori a
  3008	quasi-isomorphism. Therefore the pairing on~$\fg|_n$ is perfect.
  3009	
  3010	Taking the pro-complete limit over all weight levels:
  3011	$\omega$ is perfect at each~$n$, so the pro-complete
  3012	pairing on~$\fg = \varprojlim_n \fg/F_n$ is perfect.
  3013	\end{proof}
  3014	
  3015	\begin{corollary}[Unconditional Lagrangian criterion for the
  3016	standard landscape]
  3017	\label{cor:lagrangian-unconditional}
  3018	\ClaimStatusProvedHere
  3019	\index{Koszulness!Lagrangian criterion unconditional}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2700,2840p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\]
In words: the restriction of the $n$-th bar component to every boundary
stratum of the Fulton--MacPherson compactification is cohomologically
concentrated in degree zero.
\end{theorem}

\begin{proof}
Each boundary stratum $S_T \cong \prod_{v \in V(T)}
\overline{\Conf}_{|v|}(X_v)$ is indexed by a tree~$T$.
The restriction $i_{S_T}^!\,\barBch_n(\cA)$ decomposes as
the tensor product $\bigotimes_{v \in V(T)}
i_v^!\,\barBch_{|v|}(\cA)$,
where each factor is a lower-degree bar component restricted to
$\overline{\Conf}_{|v|}(X_v)$.

Forward: $E_2$-collapse
(Theorem~\ref{thm:pbw-koszulness-criterion}) concentrates each
bar component in degree~$0$; restrictions of degree-$0$ objects
remain in degree~$0$.



thinking
**Analyzing spectral sequence and curved setting references**

I'm tracing which sections mention the strict bar-cobar spectral sequence or quasi-isomorphism language beyond the Koszul locus, especially regarding curved or coderived contexts. I'll identify relevant blocks by label and locate if the file discusses curved or coderived replacements, possibly by searching for "curved" to verify. This will help clarify how the text handles these general or curved settings.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "curved" -n chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
4:%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
31:progressively more structured forms: curved-central algebras
42:\label{sec:filtered-vs-curved-comprehensive}
47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
70:algebras admit direct bar-cobar inversion without completion; curved
101:\begin{example}[Heisenberg: curved quadratic]\label{ex:heisenberg-quadratic}
104:The double pole produces a \emph{curved} quadratic structure: the relation $J \otimes J \sim k \cdot \mathbf{1}$ is inhomogeneous (the right side is degree~0, not degree~2), so the bar complex has curvature $m_0 \propto k \cdot \mathbf{1} \neq 0$ for $k \neq 0$ (the curvature element is proportional to the vacuum, which is central). In the language of Definition~\ref{def:quadratic-chiral}, the Heisenberg is ``quadratic'' in the sense that the OPE involves at most two generators on the left side, but it is \emph{not} strictly quadratic (i.e., $m_0 \neq 0$).
138:The bar complex is the curved chiral CE coalgebra at the Feigin--Frenkel shifted level:
146:\subsubsection{Class II: curved (non-quadratic) chiral algebras}
148:\begin{definition}[Curved chiral algebra]\label{def:curved-chiral-detailed}
149:A chiral algebra $\mathcal{A}$ is \emph{curved} (but not necessarily quadratic) if:
159:\begin{example}[Virasoro: curved, non-quadratic]\label{ex:virasoro-curved}
170:The algebra is curved because the central charge $c$ is a curvature
205:\begin{example}[\texorpdfstring{$W_3$}{W3}: filtered, non-curved]\label{ex:w3-filtered}
218:where $\Lambda(L \cdot L)$ is a composite operator, not a single generator. The algebra is filtered rather than curved because it is not generated by a finite-dimensional space $V$: composite operators like $(L \cdot L)$ appear at all levels, and the filtration is infinite-dimensional at each level. The Koszul dual is
343:The cobar-bar adjunction $\Omega \dashv B$ restricts to an equivalence on pro-nilpotent objects by the filtered analogue of Theorem~\ref{thm:bar-cobar-isomorphism-main}; the completion $\widehat{\bar{B}}(\mathcal{A})$ is pro-nilpotent by construction, so $\Omega(\widehat{\bar{B}}(\mathcal{A})) \simeq \widehat{\mathcal{A}}$. See Positselski~\cite{Positselski11} for the general framework of curved Koszul duality with completions.
346:\subsection{When does filtering degenerate to curved?}
348:\begin{proposition}[Filtered implies curved; \ClaimStatusProvedHere]\label{prop:filtered-to-curved}
349:A filtered chiral algebra $\mathcal{A}$ has an associated \emph{curved structure} if:
thinking
**Investigating line references**

I'm looking into the lines 2789 and 3015, which are supposed to relate to Theorem B and the off-locus argument. However, the user findings indicate different lines as relevant. I’m wondering if the line numbers shifted due to edits. It seems those lines may not be connected after all. I should check for the actual off-locus argument in lines around 2560 onwards, particularly from 2520-2660. I'll need to use more commands to refine this search.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2428,2688p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "off the Koszul locus|off-locus|coderived|strictified|ordinary derived|quasi-isomorphism|bar-cobar inversion|comparison functor|Phi|PBW spectral sequence|collapse" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2688,2768p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2428	over the complete algebra and
  2429	$\operatorname{Comod}^{\mathrm{pronil}}$ denotes pronilpotent
  2430	comodules over the completed bar coalgebra. The twisting morphism
  2431	$\widehat\tau\colon \widehat{\bar B}^{\mathrm{ch}}(\cA) \to \cA$
  2432	mediates the equivalence via completed extension of scalars.
  2433	\end{corollary}
  2434	
  2435	\begin{proof}
  2436	The completed counit and unit are quasi-isomorphisms by
  2437	Theorem~\ref{thm:completed-bar-cobar-strong}(3)--(4). The
  2438	passage to module/comodule categories follows from completed twisting
  2439	representability
  2440	(Theorem~\ref{thm:completed-twisting-representability}), which
  2441	ensures that the completed bar and cobar functors on
  2442	module categories are adjoint and that the unit/counit natural
  2443	transformations are quasi-isomorphisms quotientwise. Applying
  2444	Lemma~\ref{lem:complete-filtered-comparison} to each module/comodule
  2445	then gives the equivalence. The argument parallels
  2446	Theorem~\ref{thm:full-derived-module-equiv-proved}, with
  2447	finite-generation replaced by continuity and conilpotence replaced
 succeeded in 52ms:
7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
16:is a quasi-isomorphism, so that no information is lost. This is
24:quasi-isomorphism of chiral algebras, genus by genus and in
27:a spectral sequence whose $E_2$~collapse, forced by the Koszul
28:property (Theorem~\ref{thm:spectral-sequence-collapse}),
29:reduces the quasi-isomorphism to a finite verification at each
33:coderived categories
50:admit bar-cobar inversion by increasingly refined completions; the
70:algebras admit direct bar-cobar inversion without completion; curved
141:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
244:question: completed bar-cobar inversion holds. The remaining task is
578:quasi-isomorphism for the bar differential.
617:$\mathrm{lim}^1 = 0$ and hence the comparison quasi-isomorphism.
662:The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
676:bar-complex cohomology collapses on the higher-genus bar-object
686:\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
687:\label{rem:coderived-status}%
688:\index{coderived category!status}%
691:the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
692:$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
 succeeded in 51ms:
  2688	
  2689	\begin{theorem}[FM boundary acyclicity;
  2690	\ClaimStatusProvedHere]\label{thm:fm-boundary-acyclicity}
  2691	\index{Koszulness!FM boundary acyclicity}
  2692	\index{Fulton--MacPherson compactification!boundary acyclicity}
  2693	Let $\cA$ be a chiral algebra on~$X$ satisfying the standing hypotheses.
  2694	Then $\cA$ is chirally Koszul if and only if for all $n \geq 2$ and every
  2695	boundary stratum $S \subset \partial \overline{\Conf}_n(X)$ with inclusion
  2696	$i_S \colon S \hookrightarrow \overline{\Conf}_n(X)$:
  2697	\[
  2698	 H^k\bigl(i_S^!\, \barBch_n(\cA)\bigr) = 0
  2699	 \quad \text{for all } k \neq 0.
  2700	\]
  2701	In words: the restriction of the $n$-th bar component to every boundary
  2702	stratum of the Fulton--MacPherson compactification is cohomologically
  2703	concentrated in degree zero.
  2704	\end{theorem}
  2705	
  2706	\begin{proof}
  2707	Each boundary stratum $S_T \cong \prod_{v \in V(T)}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2120,2180p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 is a quasi-isomorphism after appropriate quantum corrections (here $\mathcal{A}_g$ denotes the genus-$g$ component of the genus-graded chiral algebra)
 
\item \emph{Genus series:}
 \[\psi = \sum_{g=0}^\infty \hbar^{2g-2} \psi_g\]
 converges in the $\hbar$-adic completion for $|\hbar| < R$ (radius determined 
 by growth of moduli spaces)
\end{enumerate}
\end{theorem}

\begin{proof}
We prove each case separately.

\emph{Case 1: Genus zero on~$\bP^1$.}

At genus zero, the chiral bar complex lives on configuration spaces of the rational curve:
\[\bar{B}_0^n(\mathcal{A}) = \Gamma\left(\overline{C}_n(\mathbb{P}^1),
\mathcal{A}^{\boxtimes n} \otimes \Omega^\bullet\right)\]
This is \emph{not} the classical bar complex over a point: the Fulton--MacPherson compactifications $\overline{C}_n(\bP^1)$, the logarithmic propagator $\eta_{ij} = d\log(z_i - z_j)$, and the Arnold relations in the cohomology of configuration spaces are all genuinely present and have no classical analogue. The classical bar over a point embeds via formal-disk restriction followed by homotopy transfer, but this comparison requires specifying the retraction $\bA^1 \to \mathrm{pt}$ and its attendant chain homotopy (see the discussion following Definition~\ref{def:chiral-koszul-pair}).

Beilinson--Drinfeld proved \cite{BD04} Theorem 3.7.11:
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2288,2428p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1568,1668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1668,1825p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1568	 and free contramodules are projective
  1569	 (Proposition~\ref{prop:chiral-inj-proj-resolutions}).
  1570	\item \emph{Conilpotency from conformal weight.}
  1571	 The conformal weight grading on $\bar{B}^{\mathrm{ch}}(\cA)$
  1572	 (inherited from $\cA$) ensures conilpotency
  1573	 (Theorem~\ref{thm:coalgebra-via-NAP}(4)), which is needed for
  1574	 the compact generation argument in Step~5 of the proof.
  1575	\item \emph{Finite-dimensionality from holonomicity.}
  1576	 The holonomicity of the bar complex on each configuration space
  1577	 stratum (Lemma~\ref{lem:bar-holonomicity}) ensures
  1578	 finite-dimensional graded pieces, which is
  1579	 needed for the duality between contramodules and complete modules
  1580	 (Remark~\ref{rem:chiral-contramodules}).
  1581	\end{enumerate}
  1582	These geometric inputs are specific to the chiral setting and have
  1583	no analogue in Positselski's ground-field framework.
  1584	\end{remark}
  1585	
  1586	%================================================================
  1587	% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
 succeeded in 51ms:
  2288	quasi-isomorphism corresponds to:
  2289	
  2290	A homology isomorphism gives only on-shell equivalence: physical states match, but scattering amplitudes and quantum corrections are inaccessible. A quasi-isomorphism gives off-shell equivalence: correlation functions, amplitudes, quantum corrections (encoded in the higher homotopies), and the path integral measure all transfer.
  2291	\end{remark}
  2292	
  2293	%================================================================
  2294	% COMPLETED BAR-COBAR INVERSION
  2295	%================================================================
  2296	
  2297	\subsection{Completed bar-cobar inversion}
  2298	\label{subsec:completed-bar-cobar-inversion}
  2299	
  2300	The finite-stage inversion theorem
  2301	(Theorem~\ref{thm:bar-cobar-inversion-qi}) establishes the
  2302	quasi-isomorphism $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on the
  2303	Koszul locus of finite-type chiral algebras. The programmatic regime
  2304	($\mathcal{W}_\infty$, affine Yangians, RTT towers) requires an
  2305	extension of inversion to separated complete inverse limits. The key
  2306	structural input is the strong completion-tower framework developed in
  2307	\S\ref{sec:curved-koszul-i-adic}
 succeeded in 50ms:
  1668	
  1669	\begin{example}[Admissible-level failure of bar-cobar inversion]
  1670	\label{ex:admissible-sl2-failure}
  1671	\index{admissible level!bar-cobar inversion failure}
  1672	\index{bar-cobar inversion!admissible-level counterexample}
  1673	Consider $L_{-1/2}(\mathfrak{sl}_2)$, the simple affine vertex algebra
  1674	at the admissible level $k = -1/2$ for $\widehat{\mathfrak{sl}}_2$
  1675	(here $h^\vee = 2$, so $k + h^\vee = 3/2$; the admissible
  1676	parametrization is $k = -h^\vee + p/q$ with $p = 3$, $q = 2$).
  1677	This algebra is excluded from the Koszul locus of
  1678	Theorem~\ref{thm:bar-cobar-inversion-qi}, and we now explain the
  1679	concrete mechanism by which bar-cobar inversion fails.
  1680	
  1681	\emph{Singular vector in the bar-relevant range.}
  1682	The vacuum Verma module $M(k\Lambda_0)$ at $k = -1/2$ has a
  1683	singular vector at conformal weight $(p-1)q = 2 \cdot 2 = 4$,
  1684	produced by the Kac--Kazhdan root $\beta_{q,-} = q\delta - \alpha$
  1685	at KK value $j = p - 1 = 2$
  1686	(Kac--Wakimoto~\cite{KW88};
  1687	cf.\ Remark~\ref{rem:sl2-admissible}).

thinking
**Evaluating spectral sequence claims and corrections**

I'll carefully examine the specified sections around 2024–2077, focusing on where bar-cobar spectral sequences and collapse theorems appear, especially noting that these results rely on Koszul assumptions. I want to clarify that outside the Koszul locus or in curved contexts, the file doesn't provide a coderived replacement, so minimal corrections would require explicitly restricting claims to Koszul cases or acknowledging missing curved generalizations. I'll also check for any mentions of coderived solutions nearby.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "coderived" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
33:coderived categories
662:The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
686:\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
687:\label{rem:coderived-status}%
688:\index{coderived category!status}%
693:(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
701:($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
708:these classes \emph{control} the coderived category at each genus requires
709:the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
717:\item Construct the coderived model structure on curved chiral
721:\item Identify the coderived shadow invariants with the proved
875:substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
969:\label{subsec:chiral-coderived-contraderived}
972:\label{def:chiral-coderived}
973:\index{coderived category!chiral|textbf}
1005:\label{eq:chiral-coderived}\\
1065: the coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
1328:the contraderived and coderived categories
1433:bar coalgebra. Its intrinsic output is a coderived/contraderived
1454:between the coderived category of conilpotent chiral
exec
/bin/zsh -lc 'rg -n "higher-genus-inversion|genus-graded-convergence|coderived/contraderived|Positselski|filtered-complete|curved-central" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2100,2290p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '940,1610p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
26:(Theorem~\ref{thm:genus-graded-convergence}). The proof uses
31:progressively more structured forms: curved-central algebras
32:via $I$-adic completion, filtered-complete algebras via
47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
48:with central curvature), filtered-complete (requiring $I$-adic completion),
343:The cobar-bar adjunction $\Omega \dashv B$ restricts to an equivalence on pro-nilpotent objects by the filtered analogue of Theorem~\ref{thm:bar-cobar-isomorphism-main}; the completion $\widehat{\bar{B}}(\mathcal{A})$ is pro-nilpotent by construction, so $\Omega(\widehat{\bar{B}}(\mathcal{A})) \simeq \widehat{\mathcal{A}}$. See Positselski~\cite{Positselski11} for the general framework of curved Koszul duality with completions.
662:The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
669:\index{Positselski!chiral lift|textbf}
681:The chiral analogues of Positselski's coalgebra homological
682:algebra~\cite{Positselski11} replace the ground field~$k$ by
693:(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
710:This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
800:This follows Positselski~\cite[\S4.1]{Positselski11}.
856:replaces Positselski's $\mathrm{Hom}_k(C, P) \to P$, where
1023:(Positselski~\cite[\S4.5]{Positselski11}). When $h \neq 0$, the standard
1100:Positselski~\cite[\S4.4, proof of Theorem]{Positselski11}).
1117:Positselski~\cite[\S4.4]{Positselski11}, using the injective
1204:\index{Positselski!functors PhiPsi@$\Phi_C$, $\Psi_C$}
1271:Positselski~\cite[\S5.1]{Positselski11}), the
1303:\index{Positselski!chiral correspondence|textbf}
 succeeded in 50ms:
  2100	\subsection{Convergence at all genera}
  2101	
  2102	\begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
  2103	\textup{[Regime: curved-central on the Koszul locus
  2104	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  2105	
  2106	Let $\mathcal{A}$ be a Koszul chiral algebra satisfying the hypotheses of
  2107	Theorem~\ref{thm:bar-cobar-inversion-qi}. The bar-cobar inversion
  2108	$\psi: \Omega(\bar{B}(\mathcal{A})) \to \mathcal{A}$
  2109	converges at each genus $g$, and the full genus-graded sum converges in the
  2110	$\hbar$-adic completion.
  2111	
  2112	More precisely:
  2113	\begin{enumerate}
  2114	\item \emph{Genus zero:} 
  2115	 \[\psi_0: \Omega_0(\bar{B}_0(\mathcal{A})) \xrightarrow{\sim} \mathcal{A}\]
  2116	 is a quasi-isomorphism (classical result, BD §3.7)
  2117	 
  2118	\item \emph{Fixed genus $g$:}
  2119	 \[\psi_g: \Omega_g(\bar{B}_g(\mathcal{A})) \to \mathcal{A}_g\]
 succeeded in 52ms:
   940	\mathrm{Hom}_{\mathcal{D}_X}(N, V)\bigr)
   941	\]
   942	for any graded $\mathcal{D}_X$-module $V$, and dually:
   943	\[
   944	\mathrm{Hom}_{\mathcal{D}_X}(C \chirtensor V,\, P)
   945	\;\cong\;
   946	\mathrm{Hom}_{\mathcal{D}_X}(V,\,
   947	\mathrm{Hom}^{\mathrm{ch}}(C, P))
   948	\]
   949	establishing $\Phi_C \dashv \Psi_C$
   950	(see Definition~\textup{\ref{def:chiral-Phi-Psi}} below).
   951	\end{lemma}
   952	
   953	\begin{proof}
   954	Both isomorphisms are instances of the tensor-hom adjunction in the
   955	chiral category. For the first: an element of the left side is a
   956	$\mathcal{D}_X$-linear map $f\colon N \square_C^{\mathrm{ch}} M \to V$.
   957	By the universal property of the equalizer, this is equivalent to a
   958	$\mathcal{D}_X$-linear map $\tilde{f}\colon N \chirtensor M \to V$
   959	that equalizes the two coaction maps. By the chiral tensor-hom

thinking
**Exploring theorems**

I need to take a closer look at the higher-genus inversion theorem. It seems like I should search for more information, possibly in other resources or papers. I'm not quite sure where to start, but I'm curious about where this theorem might be discussed further. Let me see if I can find some good references or sources that cover this topic! This could help clarify my understanding.
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|higher-genus inversion|higher-genus-open-stratum-qi|extension-across-boundary-qi|boundary-qi\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3590,3645p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1791:higher-genus inversion package (Theorem~\ref{thm:higher-genus-inversion}).
1917:higher-genus inversion is \emph{conditional} on~\ref{MK:modular}.
2163:See Lemma~\ref{lem:higher-genus-open-stratum-qi}.
2171:(Lemma~\ref{lem:higher-genus-boundary-qi}).
2178:(Lemma~\ref{lem:extension-across-boundary-qi}).
 succeeded in 51ms:
  3590	diagram~\eqref{eq:master-square} at genus~$0$:
  3591	\[
  3592	\begin{tikzcd}[row sep=large, column sep=large]
  3593	\cA \arrow[r, "\barB_X"] \arrow[d, "(\cdot)^!"']
  3594	& \barB_X(\cA) \arrow[d, "\mathbb{D}_{\mathrm{Ran}}"] \\
  3595	\cA^! \arrow[r, "\barB_X"']
  3596	& \barB_X(\cA^!)
  3597	\end{tikzcd}
  3598	\]
  3599	The top row is the bar construction of this chapter; the right
  3600	column is Verdier duality
  3601	(Theorem~\ref{thm:verdier-bar-cobar}); the commutativity
  3602	$\mathbb{D}_{\mathrm{Ran}}\barB_X(\cA) \simeq \cA^!_\infty$ (factorization \emph{algebra}, not coalgebra)
  3603	is Theorem~A. The cobar functor $\Omega_X$ is left adjoint
  3604	to~$\barB_X$, and the counit
  3605	$\Omega_X\barB_X(\cA) \xrightarrow{\sim} \cA$ is an
  3606	equivalence for Koszul algebras.
  3607	
  3608	In the nilpotence-periodicity framework
  3609	(Remark~\ref{rem:nilpotence-periodicity}), this is the

codex
**Findings**
- `lem:bar-cobar-associated-graded`, `thm:bar-cobar-spectral-sequence`, and `thm:spectral-sequence-collapse` (≈2024‑2077) currently describe the strict bar-cobar spectral sequence and its $E_2$ collapse as if the bar differential were already a quasi-isomorphism, but the convergence proof only invokes conilpotency/completion and the collapse relies on the Koszul quasi-isomorphism into $\bar{B}(\cA)$; no curved/coderived analogue is proved in this file. Minimal truthful fix inside this file is to frame these statements explicitly as “on the Koszul locus (quadratic Koszul chiral algebras)” or otherwise note that a coderived spectral sequence would be required once curvature is present, rather than implicitly claiming the general collapse/quasi-isomorphism.

- The remark and conjecture around lines 2789‑2808 (`rem:d-module-purity-content-bci`, `conj:lagrangian-koszulness`, `rem:lagrangian-ptvv`) use the bar-cobar adjunction/free-resolution language to argue Lagrangian transversality even “off the locus,” yet the evidence given is “on the Koszul locus” and there’s no curved/coderived replacement proved here. The minimal truthful rectification is to keep these statements conditional on being in the Koszul regime (e.g., purity + alignment ⇒ FM boundary acyclicity ⇒ Koszul) and to flag that the passage to curved/coderived settings needs the coderived bar-cobar adjunction (only sketched elsewhere) before one can assert the same Lagrangian picture.

- `cor:lagrangian-unconditional` plus its proof (≈3015‑3041) deploy the ordinary quasi-isomorphism machinery to conclude that standard families are transverse Lagrangians, but the proof only works because (P1)–(P3) enforce the Koszul hypotheses; there is no new curved/coderived replacement built here. The minimal truthful correction is to restate the corollary as “under (P1)–(P3), which enforce the Koszul locus,” or add a pointer that extending to curved families would require first constructing the coderived bar-cobar quasi-equivalence (not present in this section).
thinking
**Investigating label issues**

I’m noticing that the search label “higher-genus-inversion” isn't found. Maybe it’s a duplicate or missing? I wonder if the theorem was inserted in another file or if the label is unresolved. I think it could be useful to search globally for the label, but I need to be mindful not to edit other files. I can read dependencies, so maybe a global search will help me pinpoint the issue.
codex
I’ve isolated the risky surface. The file already contains a proved coderived/contraderived comparison for curved bar coalgebras, while the strict spectral-sequence theorem is explicitly ordinary `d^2=0` filtered homological algebra. I’m checking which theorem statements still overstate ordinary quasi-isomorphism off locus so I can narrow exactly those sentences.
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|label\\{lem:higher-genus-open-stratum-qi\\}|label\\{lem:higher-genus-boundary-qi\\}|label\\{lem:extension-across-boundary-qi\\}|label\\{thm:BD-extension-higher-genus\\}\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "filtered-complete off it|curved-central on the Koszul locus|quasi-isomorphism after appropriate quantum corrections|quasi-isomorphism there|off it, passage to|off the Koszul locus|completed or coderived" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "bar-cobar inversion is quasi-isomorphism|Genus-graded convergence|higher-genus inversion|coderived category|contraderived|Positselski equivalence" metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
1606:on the Koszul locus; filtered-complete off it
1660:the counit $\psi$ is a quasi-isomorphism there
1663:with the completed or coderived bar-cobar correspondence
2103:\textup{[Regime: curved-central on the Koszul locus
2120: is a quasi-isomorphism after appropriate quantum corrections (here $\mathcal{A}_g$ denotes the genus-$g$ component of the genus-graded chiral algebra)
2616:resolution converges and $\Phi$ is an equivalence; off it, passage to
4147:convergence off the Koszul locus decomposes into complementary
 succeeded in 52ms:
metadata/theorem_registry.md:251:| `thm:positselski-chiral-proved` | `theorem` | 1441 | Positselski equivalence for the chiral bar coalgebra |
metadata/theorem_registry.md:257:| `thm:genus-graded-convergence` | `theorem` | 2040 | Genus-graded convergence |
metadata/theorem_registry.md:1154:| `thm:positselski-chiral` | `theorem` | 1251 | Positselski equivalence for the chiral bar coalgebra |
metadata/theorem_registry.md:2024:| `thm:factorization-positselski` | `theorem` | 1523 | Factorization Positselski equivalence on the bar-coalgebra surface |
metadata/theorem_registry.md:2316:| `thm:bv-bar-coderived` | `theorem` | 1895 | BV$=$bar in the coderived category |
chapters/connections/concordance.tex:696: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
chapters/connections/concordance.tex:1955: BV=bar in the coderived category is proved for all four shadow
chapters/connections/concordance.tex:4174: coderived category.
chapters/connections/concordance.tex:4845:intrinsic coderived/contraderived bar-coalgebra framework of
chapters/connections/concordance.tex:4853:their coderived/contraderived invariants remain nontrivial. The
chapters/connections/concordance.tex:4857:The provisional coderived category
chapters/connections/concordance.tex:4925:and contraderived categories on~$\operatorname{Ran}(X)$: curved
chapters/connections/concordance.tex:4934:coderived category embeds fully faithfully
chapters/connections/concordance.tex:5436:between the \emph{coderived category}
chapters/connections/concordance.tex:6939: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
chapters/connections/concordance.tex:7611: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9113:the coderived category $D^{\mathrm{co}}(C)$ reduces to
chapters/connections/concordance.tex:10086: \textbf{Resolved} in the coderived category
chapters/connections/concordance.tex:10334: coderived category?}
chapters/connections/concordance.tex:10613: coderived category of analytic contramodules.

thinking
**Investigating missing matches**

I'm noticing that the rg tool isn't finding any matches, and it's exiting with an error because there are missing labels in the file. I wonder if there are unresolved references. I should take a closer look around lines 4147 to see if there's something in the summary or diagram that could provide clarity. I need to search those exact lines to figure out what's going wrong here.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '4128,4162p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{cor:bar-cobar-inverse\\}|bar-cobar-inverse\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:bar-cobar-inversion-qi\\}|thm:bar-cobar-inversion-qi\\}|thm:genus-graded-convergence\\}|cor:bar-cobar-inverse\\}|thm:positselski-chiral-proved\\}|thm:full-derived-module-equiv-proved\\}\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4128	algebras. The residual content is a geometric assertion:
  4129	that sectorwise degeneration on the bar complex lifts to
  4130	compact generation of $\mathrm{Fact}(X;\, \cA)$ on\/ $\Ran(X)$.
  4131	\end{corollary}
  4132	
  4133	\subsection{The categorical logarithm and its four properties}
  4134	\label{subsec:monograph-as-log}
  4135	\index{categorical logarithm!four properties}
  4136	
  4137	Taken at full depth, the four main theorems are the four fundamental
  4138	properties of \emph{any} logarithm:
  4139	\begin{itemize}
  4140	\item \textbf{Theorem~A} (existence): the categorical logarithm and
  4141	exponential exist, as a pair of adjoint functors between augmented
  4142	factorization algebras and conilpotent factorization coalgebras.
  4143	\item \textbf{Theorem~B} (invertibility): on the convergence domain
  4144	(the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
  4145	logarithm faithfully encodes its input.
  4146	\item \textbf{Theorem~C} (branch structure): the failure of
  4147	convergence off the Koszul locus decomposes into complementary
 succeeded in 52ms:
21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
26:(Theorem~\ref{thm:genus-graded-convergence}). The proof uses
141:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
1441:\label{thm:positselski-chiral-proved}
1498:\label{thm:full-derived-module-equiv-proved}
1512:Consequently, on that same locus, Theorem~\textup{\ref{thm:positselski-chiral-proved}}
1536:Theorem~\ref{thm:positselski-chiral-proved} gives the stated ordinary
1550:Theorem~\ref{thm:full-derived-module-equiv-proved} is precisely the
1604:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1664:(Corollary~\ref{cor:bar-cobar-inverse},
1678:Theorem~\ref{thm:bar-cobar-inversion-qi}, and we now explain the
1708:Theorem~\ref{thm:bar-cobar-inversion-qi}(4)
1726:Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
1754:(Theorem~\ref{thm:bar-cobar-inversion-qi}(4)) collapses at a finite
1790:Theorem~\ref{thm:genus-graded-convergence}, item~(2), together with the
1795:Theorem~\ref{thm:genus-graded-convergence}, item~(3), which identifies
1824:Theorem~\ref{thm:bar-cobar-inversion-qi}. Then:
1866:At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is a
1878:Theorem~\ref{thm:bar-cobar-inversion-qi} is invoked to verify
1897:quasi-isomorphism. Theorem~\ref{thm:bar-cobar-inversion-qi} is
 succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1664:(Corollary~\ref{cor:bar-cobar-inverse},
chapters/theory/bar_cobar_adjunction_inversion.tex:2470: Cor~\ref{cor:bar-cobar-inverse} \\

thinking
**Searching for cor:bar-cobar-inverse**

I need to find the cor:bar-cobar-inverse, and I think it might be in a curved file. That sounds relevant, so I should search for it. I wonder what I might discover if I dig into it further. Hopefully, that leads me to the information I need! I'm excited to explore this a bit more, just to see what I can uncover. Let's get to searching!
exec
/bin/zsh -lc "rg -n \"label\\{cor:bar-cobar-inverse\\}\" chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/cobar_construction.tex:1446:\begin{corollary}[Bar-cobar mutual inverses; \ClaimStatusProvedHere]\label{cor:bar-cobar-inverse}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"conv:higher-genus-differentials|dfib|d_fib|d\\"'^2_bar=0|d_fib'"\\"'^2|fiberwise differential|curvature" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
     1	\chapter{Bar-cobar adjunction and curved Koszul duality}
     2	\label{chap:bar-cobar-adjunction}
     3	
     4	The bar-cobar adjunction $\Omegach \dashv \barBch$ represents the
     5	space of twisting morphisms
     6	$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
     7	by a pair of functors between chiral algebras and conilpotent
     8	chiral coalgebras on $\Ran(X)$
     9	(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
    10	morphism
    11	$\tau_\cA \in \MC\bigl(\operatorname{Conv}(\barBch(\cA), \cA)\bigr)$
    12	is the genus-$0$ binary component of the MC element
    13	$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
    14	$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
    15	Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
    16	that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
    17	product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
    18	cohomology, so the counit
    19	$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
    20	is a quasi-isomorphism on the Koszul locus.
 succeeded in 52ms:
Total output lines: 164

chapters/theory/bar_cobar_adjunction_inversion.tex:47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
chapters/theory/bar_cobar_adjunction_inversion.tex:48:with central curvature), filtered-complete (requiring $I$-adic completion),
chapters/theory/bar_cobar_adjunction_inversion.tex:104:The double pole produces a \emph{curved} quadratic structure: the relation $J \otimes J \sim k \cdot \mathbf{1}$ is inhomogeneous (the right side is degree~0, not degree~2), so the bar complex has curvature $m_0 \propto k \cdot \mathbf{1} \neq 0$ for $k \neq 0$ (the curvature element is proportional to the vacuum, which is central). In the language of Definition~\ref{def:quadratic-chiral}, the Heisenberg is ``quadratic'' in the sense that the OPE involves at most two generators on the left side, but it is \emph{not} strictly quadratic (i.e., $m_0 \neq 0$).
chapters/theory/bar_cobar_adjunction_inversion.tex:107:\[\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*) \quad \text{(commutative chiral algebra on the dual space, with curvature)}\]
chapters/theory/bar_cobar_adjunction_inversion.tex:109:Since $\mathfrak{h}$ is abelian, the chiral Koszul dual is $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ with $d = 0$ and curvature $m_0 \propto -k \cdot \mathbf{1}$ (the level negates under Koszul duality; $h^\vee = 0$ for the abelian Lie algebra). This is a \emph{commutative} chiral algebra with curvature, not the Heisenberg at negated level \neq \mathcal{H}_{-k}$). The bar differential vanishes (Example~\ref{ex:ope-to-residue}), so $H^*(\bar{B}(\mathcal{H}_k)) \simeq \bar{B}(\mathcal{H}_k)$ with CE cooperad structure.
chapters/theory/bar_cobar_adjunction_inversion.tex:123:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
chapters/theory/bar_cobar_adjunction_inversion.tex:153:\item There exists a \emph{central curvature element} $\mu_0 \in Z(\mathcal{A})^2$
chapters/theory/bar_cobar_adjunction_inversion.tex:154:\item The curvature satisfies the MC equation: 
chapters/theory/bar_cobar_adjunction_inversion.tex:170:The algebra is curved because the central charge $c$ is a curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:354:\item All higher relations are \emph{consequences} of lower ones plus curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:365:The filtered algebra $\mathcal{A}$ deforms $\mathrm{gr}(\mathcal{A})$. By condition~(3), the deformation is controlled by a single curvature element: choose generators $a_1, \ldots, a_r$ lifting $\mathrm{gr}^1(\mathcal{A})$ to $F_1\mathcal{A}$. The product $\mu(a_i, a_j)$ in $\mathcal{A}$ differs from the product in $\mathrm{gr}(\mathcal{A})$ by an element in $F_2\mathcal{A}$:
chapters/theory/bar_cobar_adjunction_inversion.tex:386:\emph{Option 2 - Curved.} Generator $V = \mathbb{C} \cdot T$, curvature $\mu_0 = c \cdot \mathbf{1}$, and higher operations $m_3(T \otimes T \otimes T)$ from the Schwarzian.
chapters/theory/bar_cobar_adjunction_inversion.tex:392:The curvature $\mu_0 = c$ captures the failure of $T$ to be a quadratic generator.
chapters/theory/bar_cobar_adjunction_inversion.tex:430:Since $J_{(0)}J = 0$ (no simple pole), only the curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:431:component~$d_{\mathrm{curvature}}$ contributes
chapters/theory/bar_cobar_adjunction_inversion.tex:433:bar degrees, the output of $d_{\mathrm{curvature}}$ is the
chapters/theory/bar_cobar_adjunction_inversion.tex:473:\item Its Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is the commutative chiral algebra on $V^*$, with curvature $m_0 \propto -k \cdot \mathbf{1}$
chapters/theory/bar_cobar_adjunction_inversion.tex:507:The curvature $c$ ensures $\widehat{d}^2 = 0$ on the completed complex.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '680,724p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   680	
   681	The chiral analogues of Positselski's coalgebra homological
   682	algebra~\cite{Positselski11} replace the ground field~$k$ by
   683	$\mathcal{D}_X$ and the tensor product by $\chirtensor$; all
   684	exactness properties are inherited from configuration space geometry.
   685	
   686	\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
   687	\label{rem:coderived-status}%
   688	\index{coderived category!status}%
   689	The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
   690	bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
   691	the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
   692	$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
   694	and ordinary derived categories coincide.
   695	
   696	At genus $g \geq 1$, the situation changes: the curvature
   697	$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
   698	with $\kappa(\cA) \neq 0$. This curvature is \emph{not a failure of
   699	Koszulness}: a Koszul algebra has uncurved genus-$0$ bar

thinking
**Identifying theorem inconsistencies**

I see the remark mentions the higher-genus-inversion quasi-isomorphism and hints at an extension toward coderived Quillen equivalence as a conjecture. However, there seems to be an inconsistency here that I need to address. It might be valuable to revisit this information and wait for more clarification from the explorer. Getting this right is important, so I want to make sure it aligns correctly with established theories!
collab wait(call_mYiPzIibLGUyhN6iCVhovuYU)
  receivers: 019d83b8-0f62-7d03-8145-6228851c372d
wait(call_mYiPzIibLGUyhN6iCVhovuYU) 1 agents complete:
  019d83b8-0f62-7d03-8145-6228851c372d completed: "**Findings**
- `lem:bar-cobar-associated-graded`, `thm:bar-cobar-spectral-sequence`, and `thm:spectral-sequence-collapse…"
exec
/bin/zsh -lc "rg -n \"conv:higher-genus-differentials|D_g|\\\\Dg\\{|period-corrected differential|total corrected differential|quantum-diff-squares-zero|higher-genus-open-stratum-qi|higher-genus-boundary-qi|extension-across-boundary-qi|BD-extension-higher-genus\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:205:\begin{example}[\texorpdfstring{$W_3$}{W3}: filtered, non-curved]\label{ex:w3-filtered}
chapters/theory/bar_cobar_adjunction_inversion.tex:228:\begin{example}[\texorpdfstring{$W_\infty$}{W_infinity}: infinite-type completion]\label{ex:winfty-completion-frontier-comprehensive}
chapters/theory/bar_cobar_adjunction_inversion.tex:395:\begin{example}[\texorpdfstring{$W_3$}{W3}: truly filtered, not curved]\label{ex:w3-not-curved}
chapters/theory/bar_cobar_adjunction_inversion.tex:517:\subsubsection{\texorpdfstring{$W_3$ (filtered): always completion}{W-3 (filtered): always completion}}
chapters/theory/bar_cobar_adjunction_inversion.tex:519:\begin{example}[\texorpdfstring{$W_3$}{W3}: bar complex must be completed]\label{ex:w3-bar-completion}
chapters/theory/bar_cobar_adjunction_inversion.tex:675:($\dfib^{\,2} = \mcurv{g} \neq 0$; Convention~\ref{conv:higher-genus-differentials}). In the curved case, ordinary
chapters/theory/bar_cobar_adjunction_inversion.tex:1202:\begin{definition}[Functors \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch}]
chapters/theory/bar_cobar_adjunction_inversion.tex:1233:\begin{lemma}[Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and
chapters/theory/bar_cobar_adjunction_inversion.tex:1234:\texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch}; \ClaimStatusProvedHere]
chapters/theory/bar_cobar_adjunction_inversion.tex:1864:\begin{remark}[Relation to the fundamental theorem \texorpdfstring{$\mathrm{A}_0$}{A_0}]
chapters/theory/bar_cobar_adjunction_inversion.tex:2079:\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
chapters/theory/bar_cobar_adjunction_inversion.tex:2144:We have verified (Theorem~\ref{thm:BD-extension-higher-genus}) that all technical
chapters/theory/bar_cobar_adjunction_inversion.tex:2163:See Lemma~\ref{lem:higher-genus-open-stratum-qi}.
chapters/theory/bar_cobar_adjunction_inversion.tex:2171:(Lemma~\ref{lem:higher-genus-boundary-qi}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2178:(Lemma~\ref{lem:extension-across-boundary-qi}).
chapters/theory/bar_cobar_adjunction_inversion.tex:3203:\begin{remark}[Identifying \texorpdfstring{$\mathcal{A}^!$}{A!} in practice]\label{rem:identify-koszul-wild}
chapters/theory/bar_cobar_adjunction_inversion.tex:3350:(see Convention~\ref{conv:higher-genus-differentials} for the notation).
chapters/theory/bar_cobar_adjunction_inversion.tex:3586:\begin{remark}[The master diagram at genus~\texorpdfstring{$0$}{0}]
chapters/theory/bar_cobar_adjunction_inversion.tex:3883:Total differential $\Dg{g}^2 = 0$ after Gauss--Manin correction \\[2pt]
chapters/theory/bar_cobar_adjunction_inversion.tex:3901:\item The \emph{flat connection} is the total corrected differential
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3868,3925p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"begin\\{convention\\}.*higher-genus-differentials|label\\{conv:higher-genus-differentials\\}|higher-genus differentials\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3868	\renewcommand{\arraystretch}{1.3}
  3869	\begin{tabular}{p{5.5cm}p{5.5cm}}
  3870	\textbf{Classical complex analysis} & \textbf{Categorical logarithm} \\
  3871	\hline
  3872	Simply connected domain &
  3873	Genus~$0$: $\pi_1(C_2(\mathbb{P}^1)) = 0$ \\[2pt]
  3874	$\log$ is single-valued, holomorphic &
  3875	$\dzero^2 = 0$ (Arnold relations), no curvature \\[2pt]
  3876	Multiply connected domain ($\mathbb{C}^\times$) &
  3877	Genus~$g \geq 1$: $\pi_1(\Sigma_g) \neq 0$ \\[2pt]
  3878	$\log$ acquires monodromy $2\pi i n$ &
  3879	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ \\[2pt]
  3880	Residue at branch point: $\mathrm{Res}_{z=0}(dz/z) = 1$ &
  3881	Curvature class: $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$, \; $\kappa(\cA) \in \mathbb{C}$ \\[2pt]
  3882	Total differential $d\log z$ is exact on universal cover &
  3883	Total differential $\Dg{g}^2 = 0$ after Gauss--Manin correction \\[2pt]
  3884	Period matrix $\tau_{ij} = \oint_{B_j} \omega_i$ &
  3885	Modular package $(\kappa, \Delta, \Theta, \Pi)$ \\[2pt]
  3886	Torelli: $\tau$ determines the curve &
  3887	Categorical Torelli: monodromy of $\barB_g$ determines~$\cA$
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"label\\{conv:higher-genus-differentials\\}|higher-genus-differentials\" chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_construction.tex:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
chapters/theory/coderived_models.tex:154:(Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/coderived_models.tex:203: Convention~\textup{\ref{conv:higher-genus-differentials}});
chapters/theory/bar_cobar_adjunction_inversion.tex:675:($\dfib^{\,2} = \mcurv{g} \neq 0$; Convention~\ref{conv:higher-genus-differentials}). In the curved case, ordinary
chapters/theory/bar_cobar_adjunction_inversion.tex:3350:(see Convention~\ref{conv:higher-genus-differentials} for the notation).
chapters/theory/bar_cobar_adjunction_inversion.tex:3912:(Convention~\ref{conv:higher-genus-differentials}) are three levels of
chapters/theory/chiral_hochschild_koszul.tex:126:Convention~\ref{conv:higher-genus-differentials}), so the bar complex
chapters/theory/chiral_hochschild_koszul.tex:2900:(Convention~\ref{conv:higher-genus-differentials}(ii)), which
chapters/theory/chiral_hochschild_koszul.tex:3226: \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))}.
chapters/theory/chiral_hochschild_koszul.tex:3275:of Convention~\ref{conv:higher-genus-differentials}(ii):
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
chapters/theory/higher_genus_foundations.tex:491:(Convention~\ref{conv:higher-genus-differentials}): curvature lives in
chapters/theory/higher_genus_foundations.tex:3705:\begin{remark}[Leray decomposition and Convention~\ref{conv:higher-genus-differentials}]
chapters/theory/higher_genus_foundations.tex:4575:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}}\textup{)}.
chapters/theory/higher_genus_foundations.tex:4614:Convention~\ref{conv:higher-genus-differentials}, the corrected
chapters/theory/bar_cobar_adjunction_curved.tex:375:(Theorem~\ref{thm:genus-universality}; Convention~\ref{conv:higher-genus-differentials}). The fiberwise differential $\dfib$ is curved, but the total corrected differential $\Dg{g}$ satisfies
chapters/theory/bar_cobar_adjunction_curved.tex:5613: (Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/bar_cobar_adjunction_curved.tex:6100:Convention~\textup{\ref{conv:higher-genus-differentials}}.
chapters/theory/higher_genus_modular_koszul.tex:565:(Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_modular_koszul.tex:2612:Convention~\ref{conv:higher-genus-differentials}. Part~\textup{(ii)} is

thinking
**Evaluating theorem status**

I need to check if the status of the theorem has changed. It might still be "ProvedHere" if we narrow down our focus. I wonder if the label needs to change; it seems likely that it doesn't, but I'll double-check to be sure. It's important to keep track of these details to ensure accuracy when discussing the theorem's status. Let's dig deeper into this!
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|label\\{lem:higher-genus-open-stratum-qi\\}|label\\{lem:higher-genus-boundary-qi\\}|label\\{lem:extension-across-boundary-qi\\}|label\\{thm:BD-extension-higher-genus\\}\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/T08_MC1_PBW.md:975:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T02_thm_B.md:406:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T02_thm_B.md:422:4010:\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
audit_campaign_20260412_231034/T02_thm_B.md:423:4059:\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
audit_campaign_20260412_231034/T02_thm_B.md:424:4085:\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
audit_campaign_20260412_231034/T02_thm_B.md:425:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T02_thm_B.md:1337:  4010	\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
chapters/theory/higher_genus_complementarity.tex:3140:\label{thm:BD-extension-higher-genus}
chapters/theory/higher_genus_complementarity.tex:4039:\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
chapters/theory/higher_genus_complementarity.tex:4088:\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
chapters/theory/higher_genus_complementarity.tex:4114:\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
rectification_20260412_233715/R19_coderived_models.md:222:chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
rectification_20260412_233715/R19_coderived_models.md:353:\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
rectification_20260412_233715/R02_higher_genus_complementarity.md:200:\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
rectification_20260412_233715/R02_higher_genus_complementarity.md:286:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
rectification_20260412_233715/R02_higher_genus_complementarity.md:404:\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
rectification_20260412_233715/R02_higher_genus_complementarity.md:505:chapters/theory/higher_genus_complementarity.tex:4010:\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
rectification_20260412_233715/R02_higher_genus_complementarity.md:543:  4101	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
rectification_20260412_233715/R02_higher_genus_complementarity.md:1265:chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}

thinking
**Inspecting audit findings**

I need to read the audit finding file T02_thm_B.md, as it might be directly relevant. It’s in the audit campaign, but I'm not sure if I can use it as a dependency since the user provided the finding text. However, knowing the suggested fixes might be useful. I’ll focus on reading only the relevant portions from the audit file since it's available locally. Let's take a closer look!
exec
/bin/zsh -lc "sed -n '1,260p' audit_campaign_20260412_231034/T02_thm_B.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# T02_thm_B (517s, gpt-5.4)

[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4123 — Clause `(b)` of `thm:higher-genus-inversion` is stated as theorematic, but the proof at `4140-4172` only proves the Koszul/modular-locus quasi-isomorphism in `(a)`. Its cited support is circular: `chapters/theory/coderived_models.tex:247-270` proves `prop:coderived-adequacy(a)` by invoking `thm:higher-genus-inversion` itself, and its off-locus argument reuses the strict spectral sequence of `chapters/theory/bar_cobar_adjunction_inversion.tex:2024-2077`, which is formulated for complexes with `d^2=0`, not for the curved off-locus setting.

[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4077 — The boundary induction step silently replaces a tensor product over the nodal fiber algebra by an ordinary tensor product over the ground field. But the actual gluing statements at `chapters/theory/higher_genus_complementarity.tex:3208-3253` are over `\mathcal A(p)`, not over `\mathbb C`. Without flatness or Tor-vanishing at the node, Künneth does not justify preservation of quasi-isomorphisms, so the proof of `lem:higher-genus-boundary-qi` does not follow.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4120 — Part `(a)` of `thm:higher-genus-inversion` claims the spectral sequence collapses at `E_2`, but the proof at `4140-4172` establishes only the quasi-isomorphism of `\psi_g`. The `E_2`-collapse is only proved later in `lem:e2-collapse-higher-genus` at `4205-4218`, so the theorem statement outruns the proof attached to it.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4018 — The open-stratum proof does not pin down which genus-`g` complex is being inverted. The manuscript distinguishes the curved fiberwise differential `\dfib` with `\dfib^2=\kappa(\cA)\omega_g` on a fixed curve and the strict corrected differential `\Dg{g}` with `\Dg{g}^2=0` (`chapters/theory/higher_genus_foundations.tex:229-270`, `chapters/theory/higher_genus_modular_koszul.tex:557-572`). Yet `lem:higher-genus-open-stratum-qi` passes from PBW concentration for `(\bar B^{(g)}(\cA),\dfib)` to the strict bar-cobar counit on a fixed curve via `thm:fundamental-twisting-morphisms` (`chapters/theory/chiral_koszul_pairs.tex:357-375`) without supplying the comparison between the curved and strict models.

[MEDIUM] chapters/theory/algebraic_foundations.tex:223 — The primary definition of the Koszul locus is conclusion-based: `\cA` is “Koszul” iff the genus-0 counit `\Omega_X(\bar B_X(\cA))\to\cA` is already a quasi-isomorphism. Consequently the genus-0 clause of `thm:bar-cobar-inversion-qi` (`chapters/theory/bar_cobar_adjunction_inversion.tex:1611-1623`) is tautological on the live definition rather than a recognition theorem from independent hypotheses. The antecedent, non-tautological notion only appears later via chiral Koszul data/pairs.

[MEDIUM] chapters/frame/guide_to_main_results.tex:37 — The public theorem summaries inflate scope. `guide_to_main_results.tex:37-40` and `preface.tex:1212-1215` advertise all-genera inversion “on the Koszul locus”, while the actual theorem assumes a modular pre-Koszul datum `(MK1–MK3)`. `heisenberg_frame.tex:4583-4585` and `4611-4615` further summarize the off-locus result as living in “the coderived category”, but the theorem only names the provisional coderived category.

## Summary
Instances checked: 17 | Violations found: 6 | Verdict: FAIL


---
STDERR:



thinking
**Considering relevant fixes**

I'm wondering if we should also fix those other issues. Since the user only listed one finding, maybe it would be best to address all relevant surfaces. The remarks about Lagrangian might not be essential unless they implicitly relate to the off-locus theorem. But if they're touched upon, I should definitely consider how they tie into the overall understanding. It's crucial to ensure all aspects are properly addressed for the user!
thinking
**Examining Lagrangian corollary**

I need to take a closer look at the current text surrounding the Lagrangian corollary. It states that under conditions P1 through P3, the Lagrangian criterion is considered unconditional and applies universally to every algebra within the standard landscape at non-critical, non-degenerate levels. I wonder if certain elements are part of the Koszul locus and how that affects filtered elements. The user’s specific question might hinge on how this corollary uses quasi-isomorphism to imply that the standard families are Lagrangians.
thinking
**Evaluating proof adjustments**

It looks like I need to fix something to avoid using conjecture in proof or proving after conjecture. But the user didn't mention this directly. If I touch lines 3015-3041, I likely need to make changes. I should inspect the rest of the corollary proof beyond line 3041 to see if it truly provides a complete proof. So, let’s read through the entire corollary proof to be sure!
codex
The deeper issue is now clear: the file has one consistent safe lane and one inconsistent one. The safe lane is the intrinsic bar-coalgebra coderived/contraderived comparison already proved here; the inconsistent lane is ordinary quasi-isomorphism language and strict spectral-sequence rhetoric leaking into curved/off-locus and Lagrangian summaries. I’m patching those theorem-adjacent summaries to force the correct boundary.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3036,3126p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2808,2878p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3036	
  3037	\begin{proof}
  3038	We verify the three hypotheses of
  3039	Theorem~\ref{thm:ambient-complementarity-fmp} and then
  3040	apply the Lagrangian criterion
  3041	(Theorem~\ref{conj:lagrangian-koszulness}).
  3042	
  3043	\smallskip\noindent
  3044	\emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
  3045	structure.}
  3046	The dg~Lie algebra $\fg := \Defcyc^{\mathrm{mod}}(\cA)$ is
  3047	complete and filtered (by genus). By the Lurie--Pridham
  3048	correspondence \cite{LurieDAGX, Pridham17}, $\fg$ integrates
  3049	to a formal moduli problem $\cM_{\mathrm{comp}}(\cA)$ with
  3050	tangent complex $\fg[1]$.
  3051	Proposition~\ref{prop:lagrangian-perfectness} gives perfectness
  3052	of the degree~$-1$ invariant pairing on~$\fg$
  3053	under~(P1)--(P3).
  3054	By the PTVV/Kontsevich--Pridham principle \cite{PTVV13,Pridham17},
  3055	a perfect invariant pairing of degree~$-1$ on a dg~Lie algebra
 succeeded in 51ms:
  2808	\end{conjecture}
  2809	
  2810	\begin{remark}[Evidence]
  2811	Forward: on the Koszul locus, the bar-cobar adjunction gives a
  2812	free resolution and the complementarity splitting
  2813	$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!) \simeq
  2814	H^*(\overline{\cM}_g, \cZ_\cA)$ (Theorem~C) identifies $\cM_\cA$
  2815	and $\cM_{\cA^!}$ as complementary subspaces. The
  2816	shifted-symplectic structure
  2817	(Theorem~\ref{thm:ambient-complementarity-fmp}) makes them
  2818	isotropic; complementarity gives maximal dimension, hence
  2819	Lagrangian.
  2820	
  2821	Converse: transverse Lagrangians in a $(-1)$-shifted symplectic
  2822	space have derived intersection of expected dimension~$0$. This
  2823	derived intersection is the twisted tensor product
  2824	$K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
  2825	\end{remark}
  2826	
  2827	\begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}


thinking
**Refining proof structure**

I’m considering the corollary proof and how it uses conjecture. It seems like I could create a direct proof that makes the conjecture reference unnecessary. By possibly replacing certain lines, I could verify hypotheses and show implications directly! That's an easy fix! I need to adjust the corollary statement to focus on the Koszul locus and consider modifying some remarks, like clarifying evidence and interpretations. Let’s also revisit the theorem title or regime. Exciting!
thinking
**Editing theorem statement**

I’m thinking about making minimal edits to the theorem statement. I could include a regime reference specifying the square-zero bar/cobar differential, particularly for genus-0 or corrected models. I also want to add a note after the theorem or at the end of the proof, clarifying that this doesn't apply to curved fiberwise complexes. Plus, I should ensure the theorem references the correct regime, changing the wording in clause 4 to focus on the Koszul/modular locus instead.
codex
```text
PE-10: scope quantifier
genus: genus 0 strict spectral-sequence lane; higher-genus/off-locus comparison lane separated explicitly
degree: all bar degrees on the square-zero filtered complex; off-locus ordinary spectral-sequence use rejected
AP32 weight tag: NA
AP139 free-var audit: strict spectral-sequence claims keep only variables justified by d^2=0; coderived claims point to proved bar-coalgebra comparison
AP36: no new iff added beyond existing proved surfaces; off-locus “quasi-isomorphism” language narrowed to intrinsic coderived/contraderived comparison
verdict: ACCEPT
```
codex
I’m editing the theorem surface now. The change is narrow: make the strict spectral-sequence lane explicitly square-zero only, route off-locus claims to the already-proved coderived/contraderived comparison, and remove the corollary’s dependence on a conjecture by making its proof direct on the Koszul surface.
exec
/bin/zsh -lc "sed -n '2084,2110p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
\[E_2^{p,q} = E_\infty^{p,q}.\]
\end{theorem}

\begin{proof}
The Koszul property of $\mathcal{A}$ means that the natural inclusion $\iota: \mathcal{A}^! \hookrightarrow \bar{B}(\mathcal{A})$ of the quadratic dual into the bar complex is a quasi-isomorphism (see \cite[Theorem~3.4.1]{LV12} for the classical case and Chapter~\ref{chap:koszul-pairs} for the chiral adaptation). Since $\mathcal{A}^!$ is generated in weight~1 with quadratic relations, its image under $\iota$ lies on the diagonal $p + q = \text{const}$ in the bigrading $(p,q)$ by bar degree and internal degree.

At the $E_1$ page, we compute the cohomology of each column with respect to $d_0 = d_{\bar{B}}$, the full bar complex differential. Each column $E_0^{p,\bullet}$ with differential $d_0$ computes the bar cohomology $H^q(\bar{B}^p(\mathcal{A}), d_{\bar{B}})$ at fixed cobar degree~$p$. By the Koszul quasi-isomorphism, the bar cohomology is concentrated on the diagonal, giving $E_1^{p,q} = 0$ whenever $q \neq 0$ (after reindexing by the bar filtration degree).

At the $E_2$ page, we take cohomology with respect to $d_1$ (induced by $d_{\text{cobar}}$, the comultiplication part). The $E_2$ groups inherit the diagonal concentration.

For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
\end{proof}

\subsection{Convergence at all genera}

\begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
\textup{[Regime: curved-central on the Koszul locus
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -26,10 +26,12 @@
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..26647a4f027896a66f4a4fd573715099bb07e953
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..26647a4f027896a66f4a4fd573715099bb07e953
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -694,3 +694,4 @@
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
@@ -709,5 +710,9 @@
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
apply_patch(auto_approved=true) exited 0 in 86ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..4a271388bf54303d626240b3be401b6fe260335b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..4a271388bf54303d626240b3be401b6fe260335b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1612,3 +1612,3 @@
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
@@ -1669,5 +1669,9 @@
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
apply_patch(auto_approved=true) exited 0 in 64ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..d61677e667f97db278715761454fd299d816c6a5
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..d61677e667f97db278715761454fd299d816c6a5
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -2036,3 +2036,8 @@
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
@@ -2090,3 +2095,3 @@
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
@@ -2095,3 +2100,4 @@
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
@@ -2110,2 +2116,19 @@
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..a97c614b524a74ac098d7a7d35504afb54b24596
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..a97c614b524a74ac098d7a7d35504afb54b24596
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -2858,2 +2858,6 @@
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
@@ -2864,3 +2868,5 @@
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
@@ -2869,2 +2875,4 @@
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
@@ -2873,3 +2881,3 @@
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
@@ -2910,3 +2918,8 @@
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..b616155f13ae65818e82fcd52df51e15c44a289a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..b616155f13ae65818e82fcd52df51e15c44a289a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -3067,3 +3067,4 @@
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
@@ -3084,6 +3085,5 @@
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
@@ -3115,3 +3115,3 @@
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
@@ -3138,2 +3138,6 @@
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
apply_patch(auto_approved=true) exited 0 in 95ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Exploring theorem references**

I'm considering whether I need to patch any theorem references to conjectures or other lines. I think a search is necessary here. It seems like there could be some remarks regarding the main theorem and spectral sequences. I should maybe check line 2149 for potential updates. Let’s take a closer look at the changed sections and utilize tools like `rg` and `sed` to help with this. It’s all about making sure everything’s accurate!
exec
/bin/zsh -lc "sed -n '686,722p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14,42p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "conj:lagrangian-koszulness|square-zero boundary|filtered-complete off it|ordinary counit|strict square-zero surface|twisted tensor product on the Koszul surface|direct curved bar-cobar Quillen equivalence|strict argument stops" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1600,1670p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
exactness properties are inherited from configuration space geometry.

\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
\label{rem:coderived-status}%
\index{coderived category!status}%
The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
On the quadratic genus-$0$ bar-dual surface, the coderived
and ordinary derived categories coincide.

At genus $g \geq 1$, the situation changes: the curvature
$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
with $\kappa(\cA) \neq 0$. This curvature is \emph{not a failure of
Koszulness}: a Koszul algebra has uncurved genus-$0$ bar
($d^2 = 0$ on $\barB^{(0)}$) but curved genus-$g$ bar
($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
$D^{\mathrm{co}}(\cA)$ is therefore not an exotic generalization
 succeeded in 50ms:
30:bar degree. Off the Koszul locus this strict argument stops.
716:the direct curved bar-cobar Quillen equivalence extending the genus-$0$
1675:does not assert that the ordinary counit $\psi$ is a
2102:strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
2825:\label{conj:lagrangian-koszulness}%
2882:Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
3199:and Theorem~\ref{conj:lagrangian-koszulness}
3232: \textup{(Theorem~\ref{conj:lagrangian-koszulness};
 succeeded in 52ms:
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
answer: on the Koszul locus
(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
quasi-isomorphism of chiral algebras, genus by genus and in
the $\hbar$-adic completion
(Theorem~\ref{thm:genus-graded-convergence}). The proof uses
a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
property (Theorem~\ref{thm:spectral-sequence-collapse}),
reduces the quasi-isomorphism to a finite verification at each
bar degree. Off the Koszul locus this strict argument stops.
What survives on the proved surface is the intrinsic
completed/coderived comparison: curved-central algebras via
$I$-adic completion, filtered-complete algebras via the
 succeeded in 52ms:
The comodule-contramodule correspondence of the preceding section
provides the categorical framework in which bar-cobar inversion
lives: at genus~$0$ the coderived category reduces to the
ordinary derived category, and the inversion theorem is a
quasi-isomorphism in the classical sense; at genus~$g \geq 1$
the curvature forces passage to the coderived setting, and the
inversion theorem becomes a statement about coderived equivalences.
We now prove the central result of this chapter.

\subsection{Statement of the main result}

\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
on the Koszul locus
\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}

The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.

Let $\mathcal{A}$ be a \emph{Koszul} chiral algebra on a Riemann surface $X$
(Definition~\ref{def:koszul-chiral-algebra};
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}

exec
/bin/zsh -lc "sed -n '1670,1684p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
with the completed correspondence of
Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
coderived/contraderived bar-coalgebra comparison of
Theorems~\ref{thm:positselski-chiral-proved}
and~\ref{thm:full-derived-module-equiv-proved}; this theorem
does not assert that the ordinary counit $\psi$ is a
quasi-isomorphism there.
\end{theorem}


\begin{example}[Admissible-level failure of bar-cobar inversion]
\label{ex:admissible-sl2-failure}
\index{admissible level!bar-cobar inversion failure}
\index{bar-cobar inversion!admissible-level counterexample}
Consider $L_{-1/2}(\mathfrak{sl}_2)$, the simple affine vertex algebra
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Inspecting spectral and Lagrangian sections**

I need to take a closer look at the spectral sequence section and the Lagrangian section. It seems important to ensure I fully understand both of these areas. I should examine them in detail to gather any critical insights or information that may be helpful. I wonder what specific aspects within these sections need my attention. Let's see what I can find when I dig deeper!
exec
/bin/zsh -lc "sed -n '2810,3110p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2020,2125p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
filtrations.
\end{remark}

\medskip

\subsubsection{Lagrangian criterion in the shifted-symplectic deformation space}

Ambient complementarity
(Conjecture~\ref{conj:ambient-complementarity},
Theorem~\ref{thm:ambient-complementarity-fmp}) equips the modular
deformation space with a $(-1)$-shifted symplectic structure.
Koszulness should be Lagrangian transversality.

\begin{conjecture}[Conditional Lagrangian characterization of chiral Koszulness;
\ClaimStatusConjectured]%
\label{conj:lagrangian-koszulness}%
\index{Koszulness!Lagrangian characterization}
\index{Lagrangian!transversality and Koszulness}
\index{shifted-symplectic!Lagrangian criterion for Koszulness}
Suppose the ambient complementarity tangent complex $T_{\mathrm{comp}}(\cA)$
 succeeded in 52ms:
The associated graded of the bar-cobar filtration is:
\[\text{Gr}^p\Omega(\bar{B}(\mathcal{A})) = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The induced differential on $\text{Gr}^\bullet$ is the \emph{bar complex differential} $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ (i.e., the full differential on $\bar{B}(\mathcal{A})$, lifted to each cobar tensor factor).
\end{lemma}

\begin{proof}
By definition of associated graded:
\[\text{Gr}^p = F^p / F^{p+1} = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
\end{proof}

\subsection{Spectral sequence construction}

\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
\label{thm:koszul-spectral-sequence}
\textup{[Regime: square-zero total differential on the filtered
bar-cobar complex.]}
Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Checking sentence placement**

I need to inspect the proof to make sure that the added sentence is in the correct place. It's important that everything flows well and makes sense in context. I’ll pay close attention to how it fits with the surrounding text to ensure clarity. My goal here is to maintain a smooth reading experience for the user. Let’s see how it all comes together!
exec
/bin/zsh -lc "sed -n '3110,3148p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
The one-sided deformation maps $i_\cA$, $i_{\cA^!}$ are
isotropic embeddings: this is
Theorem~\ref{thm:ambient-complementarity-tangent}(ii), proved
unconditionally.

\smallskip\noindent
\emph{(3) Equivalence on the Koszul surface.}
\begin{itemize}
\item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
 On the Koszul locus, the twisted tensor product
 $K_\tau(\cA, \cA^!)$ is acyclic. The complementarity
 splitting (Theorem~C) gives a direct-sum decomposition
 $T_{\mathrm{comp}} \simeq T_\cA \oplus T_{\cA^!}$:
 the one-sided tangent complexes are complementary subspaces.
 By~(2) they are isotropic; by complementarity they are
 half-dimensional. Isotropic + half-dimensional = Lagrangian.
\item \emph{Converse} (Lagrangian $\Rightarrow$ Koszul).
 Transverse Lagrangians in a $(-1)$-shifted symplectic
 formal moduli problem have discrete derived
 intersection~\cite{PTVV13}. The derived intersection
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Inspecting theorem references**

It looks like I've got some work to do on patching references at certain lines in the document. I might need to check whether the user only wanted valid labels rather than focusing on the style. The search outputs point to some remaining occurrences, so I'll need to inspect those specific lines. Since it's all in the same file, it seems straightforward to make these updates. I'll double-check before proceeding!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3188,3240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3188	still requires~(P\ref{item:perf-fingen}) (finite weight spaces from
  3189	PBW) and~(P\ref{item:perf-dual}) (dual regularity via base change).
  3190	The CY exchange explains the \emph{mechanism} of perfectness at
  3191	each fiber; the \emph{uniformity} across the moduli family is a
  3192	separate input.
  3193	\end{remark}
  3194	
  3195	\begin{remark}[Synthesis: six faces of chiral Koszulness]
  3196	\label{rem:six-faces-koszulness}
  3197	Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
  3198	Conjecture~\ref{conj:d-module-purity-koszulness},
  3199	and Theorem~\ref{conj:lagrangian-koszulness}
  3200	give six characterizations of chiral Koszulness, which we summarize as
  3201	follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
  3202	The following conditions are related as indicated
  3203	\textup{(}cf.\ the meta-theorem, Theorem~\textup{\ref{thm:koszul-equivalences-meta}}\textup{)}:
  3204	\begin{enumerate}[label=\textup{(\alph*)}]
  3205	\item \textup{(Algebraic)}\quad
  3206	 $\cA$ is chirally Koszul:
  3207	 $\operatorname{Ext}^i_\cA(k,k)_j = 0$ for $i \neq j$
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Search for theorem references**

I think these should be classified as conjectures rather than theorems. There might be patches needed, too. I should also consider mentioning item f and its conditions, particularly with regard to perfectness versus an unconditional standard landscape. That sounds good! I want to make a patch for this. Additionally, it might be useful to search for "Theorem\ref{conj:" in other parts of the file using a tool like rg.
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{conj:\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..ce12c2c4386efc9db797fe8ef088e285e16a5e58
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}


thinking
**Troubleshooting code issues**

It seems it didn't find the issue, and I'm wondering if I need some escaping with a reference? I noticed two lines that might be problematic, possibly due to a double backslash. So as a next step, I think I should focus on patching those lines to see if that resolves the error. It's all about figuring out these little details! Let's see how it goes once I implement those patches.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -3198,3 +3198,3 @@
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
@@ -3231,3 +3231,3 @@
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
apply_patch(auto_approved=true) exited 0 in 60ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

codex
I’ve applied the narrow repair. I’m re-reading the modified theorem surface and running local grep checks for the exact failure mode: any remaining place in this file where the strict spectral sequence or ordinary twisted-tensor/free-resolution language bleeds into off-locus curved claims.
exec
/bin/zsh -lc "rg -n \"spectral sequence|off the Koszul locus|coderived/contraderived|twisted tensor product|free resolution|ordinary counit|quasi-isomorphism there|Conjecture~\\\\ref\\{conj:lagrangian-koszulness\\}|Theorem~\\\\ref\\{conj:lagrangian-koszulness\\}\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
27:a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
34:coderived/contraderived bar-coalgebra comparison of
125:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
595:the associated spectral sequence has
601:contributions, so the filtered spectral sequence is well-defined and converges
693:the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
1404:using the cofree resolution from Step~2. Thus
1440:bar coalgebra. Its intrinsic output is a coderived/contraderived
1475:At genus~$g \geq 1$, the coderived/contraderived categories are the
1544:derived reduction of the intrinsic coderived/contraderived
1561:The coderived/contraderived framework generalizes to genus~$g \geq 1$, where the
1656:\item There exists a spectral sequence converging to
1665:argument is unavailable, the bar spectral sequence can carry extra
1667:the counit $\psi$ is a quasi-isomorphism there
1672:coderived/contraderived bar-coalgebra comparison of
1675:does not assert that the ordinary counit $\psi$ is a
1676:quasi-isomorphism there.
1718:The bar-cobar spectral sequence of
1723:differential, so the spectral sequence does not collapse at $E_2$.
1764:the bar-cobar spectral sequence
exec
/bin/zsh -lc "sed -n '3194,3242p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2088,2148p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3016,3140p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Synthesis: six faces of chiral Koszulness]
\label{rem:six-faces-koszulness}
Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
Conjecture~\ref{conj:d-module-purity-koszulness},
and Conjecture~\ref{conj:lagrangian-koszulness}
give six characterizations of chiral Koszulness, which we summarize as
follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
The following conditions are related as indicated
\textup{(}cf.\ the meta-theorem, Theorem~\textup{\ref{thm:koszul-equivalences-meta}}\textup{)}:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \textup{(Algebraic)}\quad
 $\cA$ is chirally Koszul:
 $\operatorname{Ext}^i_\cA(k,k)_j = 0$ for $i \neq j$
 \textup{(meta-theorem item~(i))}.
\item \textup{(Descent-theoretic)}\quad
 The Barr--Beck--Lurie comparison functor for
 $B_\kappa \dashv \Omega_\kappa$ is an equivalence
 \textup{(Theorem~\ref{thm:barr-beck-lurie-koszulness};
 meta-theorem item~(vi))}.
 succeeded in 52ms:
\item The complex is bounded in each column (fixed $p$)
\end{enumerate}

By standard spectral sequence theory (Weibel \cite{Weibel94}, Chapter 5), this ensures:
\[E_\infty^{p,q} = \text{Gr}^p H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
\end{proof}

\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
\textup{[Regime: quadratic, Koszul locus, square-zero total differential
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.

For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
\[E_2^{p,q} = E_\infty^{p,q}.\]
\end{theorem}

\begin{proof}
 succeeded in 51ms:
\langle \alpha(-), \beta(-) \rangle_\cA\bigr)$.
This is nondegenerate because it is the composite of the
canonical isomorphism
$\operatorname{Hom}(V, W) \cong V^\vee \otimes W$
with the tensor-product pairing, and the tensor product of two
nondegenerate finite-dimensional bilinear forms is nondegenerate.
Because the total pairing on~$\fg|_n$ is the direct sum over
$(g,r)$ of these component pairings (different $(g,r)$-components
are $\omega$-orthogonal by the grading), the total chain-level
pairing is nondegenerate.

\smallskip\noindent
\emph{Step~3: skew-adjointness of the differential.}
The differential $d = d_{\mathrm{int}} + d_{\mathrm{sew}}$
on~$\fg$ is skew-adjoint with respect to~$\omega$:
\[
\omega(d\alpha, \beta)
\;+\; (-1)^{|\alpha|}\,\omega(\alpha, d\beta)
\;=\; 0.
\]
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.



thinking
**Considering Lagrangian concepts**

I noticed that we changed the Lagrangian section to indicate "off-locus," which isn't claimed. However, there's a remark about a metaphorical "failure of convergence off the Koszul locus" that may decompose into complementary Lagrangians. I’m contemplating if this relates to theorem C's branch structure, and whether it holds up. It's possible this refers to complementarity rather than theorem B, which could make it more conceptual.
thinking
**Inspecting log details**

I’m considering whether I can ignore a certain detail. There’s a line in the categorical log that reads, “convergence off the Koszul locus decomposes into complementary…” from line 4198. This might be inconsistent with a new boundary I’m dealing with. It feels important to inspect this further to ensure there are no discrepancies that could lead to issues later on. I’ve got to keep my attention on these details!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '4188,4204p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4188	Taken at full depth, the four main theorems are the four fundamental
  4189	properties of \emph{any} logarithm:
  4190	\begin{itemize}
  4191	\item \textbf{Theorem~A} (existence): the categorical logarithm and
  4192	exponential exist, as a pair of adjoint functors between augmented
  4193	factorization algebras and conilpotent factorization coalgebras.
  4194	\item \textbf{Theorem~B} (invertibility): on the convergence domain
  4195	(the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
  4196	logarithm faithfully encodes its input.
  4197	\item \textbf{Theorem~C} (branch structure): the failure of
  4198	convergence off the Koszul locus decomposes into complementary
  4199	Lagrangians (the two branches of the multi-valued logarithm), and the
  4200	total logarithmic data is the sum of the two branches.
  4201	\item \textbf{Theorem~D} (leading coefficient): the leading
  4202	coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
  4203	full scalar package, just as the leading coefficient of
  4204	$\log(1+z) = z + \cdots$ determines the local behavior.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

exec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{conj:|Theorem~\\ref\\{conj:' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.


thinking
**Evaluating LaTeX checks**

I need to consider running LaTeX syntax checks. I could use the command to check for specific labels, but maybe it's not necessary. A simple grep might help find any broken references introduced. I also need to make sure there are no unmatched braces in inserted lines. While running `latexmk` might not be feasible, I could check with `grep` or inspect the diff for unexpected changes. Checking the diff might be a solid plan!
codex
The edits are in place. I’m doing a hostile re-read of the exact diff now: checking that every new limitation is aligned with the proved coderived comparison, that no theorem status was silently overpromoted, and that the corollary now stands on its own proof instead of leaning on the conjecture.
exec
/bin/zsh -lc 'git diff -- chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455ac..604e423 100644
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@ answer: on the Koszul locus
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..604e42313b2aba8302482d3df3b9776c57e53e3b
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3035,10 +3083,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3113,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3136,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3196,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3229,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -3077,3 +3077,4 @@
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..d5913f52e6ee47001cd6e1a74b0ab14dd9c87c1e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..d5913f52e6ee47001cd6e1a74b0ab14dd9c87c1e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.

exec
/bin/zsh -lc "rg -n \"label\\{rem:spectral-sequence-square-zero-boundary\\}\" ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3016,3144p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "conj:lagrangian-koszulness|thm:positselski-chiral-proved|thm:full-derived-module-equiv-proved|thm:bar-cobar-spectral-sequence|thm:spectral-sequence-collapse|thm:bar-cobar-inversion-qi" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
./chapters/theory/bar_cobar_adjunction_inversion.tex:2118:\label{rem:spectral-sequence-square-zero-boundary}
 succeeded in 52ms:
\langle \alpha(-), \beta(-) \rangle_\cA\bigr)$.
This is nondegenerate because it is the composite of the
canonical isomorphism
$\operatorname{Hom}(V, W) \cong V^\vee \otimes W$
with the tensor-product pairing, and the tensor product of two
nondegenerate finite-dimensional bilinear forms is nondegenerate.
Because the total pairing on~$\fg|_n$ is the direct sum over
$(g,r)$ of these component pairings (different $(g,r)$-components
are $\omega$-orthogonal by the grading), the total chain-level
pairing is nondegenerate.

\smallskip\noindent
\emph{Step~3: skew-adjointness of the differential.}
The differential $d = d_{\mathrm{int}} + d_{\mathrm{sew}}$
on~$\fg$ is skew-adjoint with respect to~$\omega$:
\[
\omega(d\alpha, \beta)
\;+\; (-1)^{|\alpha|}\,\omega(\alpha, d\beta)
\;=\; 0.
\]
 succeeded in 51ms:
21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
28:property (Theorem~\ref{thm:spectral-sequence-collapse}),
35:Theorem~\ref{thm:positselski-chiral-proved}
143:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
695:(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
715:Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
1448:\label{thm:positselski-chiral-proved}
1505:\label{thm:full-derived-module-equiv-proved}
1519:Consequently, on that same locus, Theorem~\textup{\ref{thm:positselski-chiral-proved}}
1543:Theorem~\ref{thm:positselski-chiral-proved} gives the stated ordinary
1557:Theorem~\ref{thm:full-derived-module-equiv-proved} is precisely the
1611:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1659: by the Koszul property (Theorem~\ref{thm:spectral-sequence-collapse})
1673:Theorems~\ref{thm:positselski-chiral-proved}
1674:and~\ref{thm:full-derived-module-equiv-proved}; this theorem
1689:Theorem~\ref{thm:bar-cobar-inversion-qi}, and we now explain the
1719:Theorem~\ref{thm:bar-cobar-inversion-qi}(4)
1720:(Theorem~\ref{thm:spectral-sequence-collapse}) relies on
1737:Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
1765:(Theorem~\ref{thm:bar-cobar-inversion-qi}(4)) collapses at a finite
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..d5913f52e6ee47001cd6e1a74b0ab14dd9c87c1e
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.




thinking
**Investigating theorem findings**

I’m trying to search for results related to `Theorem\ref{conj:lagrangian-koszulness}`, but I’m not finding anything. I need to inspect specific lines, like 3199 and 2701, to see if there’s a potential issue in the output. It seems there’s still concern over the claims of convergence related to the Koszul locus, particularly around line 4198. Although the main finding appears resolved, I might need to consider the residual risks mentioned, especially regarding Theorem C.
thinking
**Patching theorem summary**

I noticed that since this is in the same file and our grep surfaced it, I might need to patch the summary to clarify, like saying, "the failure of strict convergence off the Koszul locus is recorded on the complementary Lagrangian/coderived branches." The user didn’t specifically ask for this, but it seems wise to avoid introducing inconsistencies. I want to ensure the summary aligns well with theorem C’s branch structure without conflicting with the Lagrangian criterion. I could adjust the phrasing to capture this accurately.
thinking
**Inspecting nearby lines for edits**

I think this is more of a conceptual issue, but I still want to keep things consistent. So, I should inspect the nearby lines, specifically 4188-4200, to see if I can patch just those two lines for clarity. Since it’s all in the same file and directly relates to the off-locus discussion, a minimal and truthful edit should help maintain consistency without losing the essence of the content. Let’s see what I can do!
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -4198,5 +4198,6 @@
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
apply_patch(auto_approved=true) exited 0 in 56ms:
Success. Updated the following files:
M chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..678623fd4984d579b40c94faa711b62c1bf66c7f
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
@@ -4144,9 +4196,10 @@
 (the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
 logarithm faithfully encodes its input.
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
 coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
 full scalar package, just as the leading coefficient of

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..678623fd4984d579b40c94faa711b62c1bf66c7f
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
@@ -4144,9 +4196,10 @@
 (the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
 logarithm faithfully encodes its input.
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
 coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
 full scalar package, just as the leading coefficient of


thinking
**Searching for context**

I think it might be helpful to search for broader off-locus claims, especially since I need to fix a specific aspect mentioned, like line 4198. The phrase "off the Koszul locus" could be key here, so I'll look into that. It seems like gathering additional context could clarify things. This could help me gain a better understanding of the topic and ensure I’m approaching it accurately. Let’s see what I can find!
exec
/bin/zsh -lc 'rg -n "off the Koszul locus|off it,|off-locus" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2650:resolution converges and $\Phi$ is an equivalence; off it, passage to
2876:The off-locus coderived surface is not identified here with an
2921:off-locus regime remains on the intrinsic coderived/contraderived
4199: strict convergence off the Koszul locus is recorded, on the
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..678623fd4984d579b40c94faa711b62c1bf66c7f
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
@@ -4144,9 +4196,10 @@
 (the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
 logarithm faithfully encodes its input.
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
 coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
 full scalar package, just as the leading coefficient of

Plan update
The strict spectral-sequence lane is now explicitly square-zero only, the Theorem B scope no longer advertises off-locus ordinary inversion, and the Lagrangian summaries/corollary have been narrowed to the Koszul surface with direct proof and coderived off-locus boundary notes.
  ✓ Inspect the target file around the cited lines and identify the exact theorem/proof fragments using the strict spectral-sequence argument off the Koszul locus
  ✓ Choose the strongest truthful repair: extend the argument only if the file already proves the needed curved/coderived comparison; otherwise narrow the off-locus statement to the coderived comparison actually established
  ✓ Edit the target file minimally, then re-read the modified theorem/proof/status surface and run local label/reference/consistency checks
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..678623fd4984d579b40c94faa711b62c1bf66c7f
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
@@ -4144,9 +4196,10 @@
 (the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
 logarithm faithfully encodes its input.
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
 coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
 full scalar package, just as the leading coefficient of

codex
Edited [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex).

The repair takes the second option from the finding. I did not try to invent a curved/coderived spectral sequence that this file does not prove. Instead, I made the strict spectral-sequence lane explicitly square-zero only, routed off-locus claims to the coderived/contraderived comparison already proved in this file, and tightened the downstream Lagrangian summaries so they only use the Koszul surface where ordinary bar-cobar inversion is actually available. I also removed the corollary’s dependence on `conj:lagrangian-koszulness` by making its proof direct on that Koszul surface.

Verification: I re-read the modified theorem/proof blocks, checked the new label is unique, and checked the referenced labels used in the new text exist. I did not run a full LaTeX build.

## Rectification Summary
- [FIXED] finding — restricted `thm:bar-cobar-spectral-sequence` and `thm:spectral-sequence-collapse` to square-zero total differentials, added an explicit boundary remark that they do not apply to curved fiberwise `\dfib` with `\dfib^{2}=\kappa(\cA)\omega_g`, narrowed Theorem B’s off-locus scope to the proved completed/coderived comparison, and aligned the Lagrangian evidence/corollary with that boundary.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index b5455accb55dea709f7ab8d35c6d2850d4c560c9..678623fd4984d579b40c94faa711b62c1bf66c7f
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -24,14 +24,16 @@
 quasi-isomorphism of chiral algebras, genus by genus and in
 the $\hbar$-adic completion
 (Theorem~\ref{thm:genus-graded-convergence}). The proof uses
-a spectral sequence whose $E_2$~collapse, forced by the Koszul
+a strict bar-cobar spectral sequence whose $E_2$~collapse, forced by the Koszul
 property (Theorem~\ref{thm:spectral-sequence-collapse}),
 reduces the quasi-isomorphism to a finite verification at each
-bar degree. Off the Koszul locus, inversion persists in
-progressively more structured forms: curved-central algebras
-via $I$-adic completion, filtered-complete algebras via
-coderived categories
-\textup{(}Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
+bar degree. Off the Koszul locus this strict argument stops.
+What survives on the proved surface is the intrinsic
+completed/coderived comparison: curved-central algebras via
+$I$-adic completion, filtered-complete algebras via the
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}
+\textup{(}cf.\ Gui--Li--Zeng~\cite{GLZ22}\textup{)}, and programmatic
 algebras ($\mathcal{W}_\infty$, $\mathcal{W}_{1+\infty}$) via
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}). The regime
@@ -690,7 +692,8 @@
 bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
 the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
 $\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
-(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
+(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
+On the quadratic genus-$0$ bar-dual surface, the coderived
 and ordinary derived categories coincide.
 
 At genus $g \geq 1$, the situation changes: the curvature
@@ -705,9 +708,13 @@
 
 The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
 produces genus-$g$ classes via the convolution algebra, but proving that
-these classes \emph{control} the coderived category at each genus requires
-the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
-This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
+these classes \emph{control} the coderived category at each genus via a
+direct algebra/coalgebra adjunction requires the curved bar-cobar
+adjunction to extend to a coderived Quillen equivalence. The intrinsic
+bar-coalgebra comparison already proved in this chapter is
+Theorem~\ref{thm:positselski-chiral-proved}; what remains conjectural is
+the direct curved bar-cobar Quillen equivalence extending the genus-$0$
+adjunction itself. The abstract framework (Positselski~\cite{Positselski11},
 Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
 instantiation (handling the Ran space and factorization structure
 simultaneously with curved homological algebra) has not been carried out.
@@ -1603,7 +1610,7 @@
 
 \begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
 \textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
-on the Koszul locus; filtered-complete off it
+on the Koszul locus
 \textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 
 The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
@@ -1660,9 +1667,13 @@
 the counit $\psi$ is a quasi-isomorphism there
 \textup{(}see Remark~\ref{rem:sl2-admissible}
 and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
-with the completed or coderived bar-cobar correspondence
-(Corollary~\ref{cor:bar-cobar-inverse},
-\S\ref{sec:i-adic-completion}).
+with the completed correspondence of
+Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorems~\ref{thm:positselski-chiral-proved}
+and~\ref{thm:full-derived-module-equiv-proved}; this theorem
+does not assert that the ordinary counit $\psi$ is a
+quasi-isomorphism there.
 \end{theorem}
 
 
@@ -2023,7 +2034,12 @@
 
 \begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
 \label{thm:koszul-spectral-sequence}
-The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
+\textup{[Regime: square-zero total differential on the filtered
+bar-cobar complex.]}
+Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
+satisfies $d^2 = 0$ and preserves the filtration from
+Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
+Definition~\ref{def:bar-cobar-filtration} induces a spectral
 sequence:
 \[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
 converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
@@ -2077,12 +2093,13 @@
 \end{proof}
 
 \begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
-\textup{[Regime: quadratic, Koszul locus
+\textup{[Regime: quadratic, Koszul locus, square-zero total differential
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
 For the Heisenberg algebra, the spectral sequence collapsed trivially because $d_{\mathrm{bracket}} = 0$ (no simple poles): the bar cohomology was concentrated in degrees $0$ and $2$ without further work (\S\ref{sec:frame-bar-all}). For non-abelian algebras, the collapse is a consequence of the Koszul property.
 
-For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
+For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}) on the
+strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
 Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
 \[E_2^{p,q} = E_\infty^{p,q}.\]
 \end{theorem}
@@ -2097,6 +2114,23 @@
 For $r \geq 2$, the differential $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ shifts the bidegree by $(r, 1-r)$. Since $E_2^{p,q} = 0$ for $q \neq 0$, either the source or the target of $d_r$ vanishes for every $r \geq 2$. Therefore $d_r = 0$ for all $r \geq 2$, and the spectral sequence collapses at $E_2$.
 \end{proof}
 
+\begin{remark}[Square-zero boundary of the spectral-sequence proof]
+\label{rem:spectral-sequence-square-zero-boundary}
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse} are statements about filtered
+complexes with square-zero total differential. In this chapter they
+apply to the strict genus-$0$ bar-cobar complex, and to any
+completed/corrected model whose total differential squares to zero.
+They do \emph{not} apply to the curved fiberwise higher-genus
+differential $\dfib$ with
+$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$. Off the Koszul locus, the
+proved replacement in this file is the intrinsic
+coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}, with ordinary derived
+reduction only on the flat finite-type completed-dual loci of
+Theorem~\ref{thm:full-derived-module-equiv-proved}.
+\end{remark}
+
 \subsection{Convergence at all genera}
 
 \begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
@@ -2822,22 +2856,30 @@
 space have derived intersection of expected dimension~$0$. This
 derived intersection is the twisted tensor product
 $K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
+This is a Koszul-locus argument. Off the Koszul locus, the chapter
+proves only the intrinsic coderived/contraderived bar-coalgebra
+comparison of Theorem~\ref{thm:positselski-chiral-proved}, not an
+ordinary twisted-tensor-product or free-resolution statement.
 \end{remark}
 
 \begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
 In the PTVV framework~\cite{PTVV13}, the derived intersection
 $\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
 \mathcal{M}_{\cA^!}$ computes the twisted tensor product
-$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
+$K_\tau(\cA, \cA^!)$ on the Koszul surface of
+Theorem~\ref{thm:bar-cobar-inversion-qi}; its acyclicity
+\textup{(}equivalent to Koszulness\textup{)} is
 precisely the transversality of the two Lagrangians.
 The proved linear shadow is Theorem~C:
 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
+The off-locus coderived surface is not identified here with an
+ordinary twisted tensor product.
 \end{remark}
 
 \begin{remark}[Conditional hypotheses and their verification]
 \label{rem:lagrangian-conditional}
-Theorem~\ref{conj:lagrangian-koszulness} is conditional on three
+Conjecture~\ref{conj:lagrangian-koszulness} is conditional on three
 sub-hypotheses of the ambient complementarity programme: perfectness of
 the deformation complex, non-degeneracy of the shifted-symplectic
 pairing, and finiteness of the modular envelope. The tangent-level
@@ -2874,7 +2916,12 @@
 finiteness of the modular envelope is immediate from~(P1).
 Corollary~\ref{cor:lagrangian-unconditional} upgrades the
 Lagrangian criterion to an unconditional equivalence for the
-standard landscape.
+standard-landscape Koszul cases covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}. The filtered-complete
+off-locus regime remains on the intrinsic coderived/contraderived
+bar-coalgebra surface of
+Theorem~\ref{thm:positselski-chiral-proved} and is not part of
+that upgrade.
 \end{remark}
 
 \begin{proposition}[Perfectness for the standard landscape]
@@ -3018,7 +3065,8 @@
 \ClaimStatusProvedHere
 \index{Koszulness!Lagrangian criterion unconditional}
 \index{Lagrangian!unconditional equivalence}
-Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
+Under hypotheses \textup{(P1)--(P3)}, and on the Koszul locus to
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies, the Lagrangian criterion
 \textup{(}item~\textup{(xi)} of the meta-theorem,
 Theorem~\textup{\ref{thm:koszul-equivalences-meta})} is an
 unconditional equivalence: $\cA$ is chirally Koszul if and only if
@@ -3027,7 +3075,8 @@
 space~$\mathcal{M}_{\mathrm{comp}}$.
 
 In particular, this applies unconditionally to every algebra in the
-standard landscape at non-critical, non-degenerate levels:
+standard landscape at the non-critical, non-degenerate levels for
+which Theorem~\ref{thm:bar-cobar-inversion-qi} applies:
 Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
 $k \neq -h^\vee$, Virasoro at generic~$c$, principal
 $\mathcal{W}$-algebras at non-critical level, and all free-field
@@ -3035,10 +3084,9 @@
 \end{corollary}
 
 \begin{proof}
-We verify the three hypotheses of
-Theorem~\ref{thm:ambient-complementarity-fmp} and then
-apply the Lagrangian criterion
-(Theorem~\ref{conj:lagrangian-koszulness}).
+We verify the shifted-symplectic hypotheses and then prove the two
+implications directly on the Koszul surface covered by
+Theorem~\ref{thm:bar-cobar-inversion-qi}.
 
 \smallskip\noindent
 \emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
@@ -3066,7 +3114,7 @@
 unconditionally.
 
 \smallskip\noindent
-\emph{(3) Equivalence.}
+\emph{(3) Equivalence on the Koszul surface.}
 \begin{itemize}
 \item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  On the Koszul locus, the twisted tensor product
@@ -3089,6 +3137,10 @@
  $K_\tau$, which is Koszulness
  (Definition~\ref{def:chiral-koszul-morphism}).
 \end{itemize}
+This step uses the ordinary twisted-tensor-product interpretation on
+the Koszul surface. Off that surface, the file proves only the
+intrinsic coderived/contraderived bar-coalgebra comparison of
+Theorem~\ref{thm:positselski-chiral-proved}.
 
 \smallskip\noindent
 \emph{Standard-landscape verification.}
@@ -3145,7 +3197,7 @@
 \label{rem:six-faces-koszulness}
 Theorems~\ref{thm:barr-beck-lurie-koszulness}--\ref{thm:fm-boundary-acyclicity},
 Conjecture~\ref{conj:d-module-purity-koszulness},
-and Theorem~\ref{conj:lagrangian-koszulness}
+and Conjecture~\ref{conj:lagrangian-koszulness}
 give six characterizations of chiral Koszulness, which we summarize as
 follows. Let $\cA$ be a chiral algebra satisfying the standing hypotheses.
 The following conditions are related as indicated
@@ -3178,7 +3230,7 @@
 \item \textup{(Symplectic)}\quad
  $\mathcal{M}_\cA$ and $\mathcal{M}_{\cA^!}$ are transverse
  Lagrangians in $\mathcal{M}_{\mathrm{comp}}$
- \textup{(Theorem~\ref{conj:lagrangian-koszulness};
+ \textup{(Conjecture~\ref{conj:lagrangian-koszulness};
  meta-theorem item~(xi);
  conditional on perfectness, unconditional for the standard
  landscape by Corollary~\ref{cor:lagrangian-unconditional})}.
@@ -4144,9 +4196,10 @@
 (the Koszul locus), $\exp \circ \log = \mathrm{id}$, and the
 logarithm faithfully encodes its input.
 \item \textbf{Theorem~C} (branch structure): the failure of
-convergence off the Koszul locus decomposes into complementary
-Lagrangians (the two branches of the multi-valued logarithm), and the
-total logarithmic data is the sum of the two branches.
+ strict convergence off the Koszul locus is recorded, on the
+ complementarity surface, by complementary Lagrangian branches
+ (the two branches of the multi-valued logarithm), and the total
+ logarithmic data is the sum of the two branches.
 \item \textbf{Theorem~D} (leading coefficient): the leading
 coefficient $\kappa(\cA)$ of the logarithmic expansion determines the
 full scalar package, just as the leading coefficient of

tokens used
209,449
