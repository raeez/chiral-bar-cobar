# R11_thqg_symplectic_polarization (69s)



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
session id: 019d83b2-f061-7280-97c3-43ad047c6dfe
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


TARGET: chapters/connections/thqg_symplectic_polarization.tex

FINDINGS TO FIX:

1. [CRITICAL T04] Lines ~476,694: Q_g(A) ≅ Q_g(A^!)^v claimed for all g>=0, but
   Q_0(A)=Z(A) and Q_0(A^!)=0 proven in the same file. Contradiction at g=0.
   FIX: Add hypothesis g>=1, or fix the genus-0 identifications. Check if Q_0 should
   actually be nonzero for both A and A^!.

2. [CRITICAL T04] Lines ~197,220: The involution sigma uses ev: C_g(A)^{vv} -> C_g(A)
   without reflexivity hypothesis. The vv construction imports finite-dimensional fiber-cohomology.
   FIX: Add the reflexivity/perfectness hypothesis explicitly, or use a different construction.

Read the file, verify both findings, fix.
mcp startup: no servers
codex
Using `beilinson-rectify` for a local proof-surface repair. I’m reading the required constitutional files and the target section first, then I’ll patch only the assigned file with the smallest truthful fix that closes both contradictions.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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


thinking
**Inspecting target files**

I need to read the archive called red_team_summary since the direct path is missing. I’m considering using the full target file or just the findings. I might use a tool to locate specific lines and theorem labels. I could read in chunks and possibly use parallel processing with the archive and target file. I may also run some searches for relevant queries and inspect the context around my findings. Let's start by checking the file size and relevant lines.
codex
The red-team note lives under `archive`, so I’m loading that plus the target file around the flagged loci and theorem statements. After that I’ll decide whether the strong fix is a proof repair or a scoped hypothesis.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Q_g|Q_0|sigma|C_g\\(|ev:|\\"'^{vv}|Verdier|reflex|perfect" chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
    2104 chapters/connections/thqg_symplectic_polarization.tex
 exited 2 in 51ms:
rg: regex parse error:
    (?:Q_g|Q_0|sigma|C_g\(|ev:|\^{vv}|Verdier|reflex|perfect)
                                  ^
error: repetition quantifier expects a valid decimal

thinking
**Fixing regex patterns**

I need to fix the regex pattern escaping. I should read the relevant lines to understand the issue better. It might be helpful to use `rg -n` with simpler patterns and possibly use `sed`. Okay, so I’m wondering if using an explorer is necessary. I need to target specific chunks of the file around lines 150-260, 450-520, and 660-730, plus include the theorem labels. Let’s start reading those sections!
codex
I’ve confirmed the file is large and in a high-risk cluster, so I’m narrowing to the local theorem/proof surface around both defects before editing. The main question now is whether the genus-zero contradiction can be repaired by proof or only by scope restriction.
exec
/bin/zsh -lc "rg -n \"Q_g|Q_0|sigma|C_g\\(|C_g\\"'^|'"\\"'^'"\\{vv\\}|Verdier|reflex|perfect|dual\" chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,260p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,530p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '660,730p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 $H^0 \otimes H^0 \to \mathbb{C}$
 \textup{(}classical pairing\textup{)}.
\item At genus $g \ge 2$: degree $-(3g - 3)$,
 giving a genuine shifted-symplectic structure.
\end{enumerate}
\end{proposition}

\begin{proof}
The degree is $-(3g - 3) = -\dim_{\mathbb{C}}
\overline{\mathcal{M}}_g$, which is the Verdier shift for
Serre duality on a smooth variety of dimension $3g - 3$.
The three cases follow by substituting $g = 0, 1, \ge 2$.
\end{proof}

\begin{remark}[Genus $1$ distinguished]
\label{rem:thqg-III-genus-1-special}
\index{genus 1!holographic pairing}
At genus~$1$, $\dim \overline{\mathcal{M}}_{1,1} = 1$
but $\dim \overline{\mathcal{M}}_1 = 0$ (a point for the
coarse moduli). The relevant moduli space for marked curves
 succeeded in 53ms:
39:while the ambient Verdier and cyclic-deformation shifted-symplectic
42:The ambient complex carries a Verdier involution whose eigenspace
48:generates the dual Lagrangian as a formal graph, that its Taylor
58:complex and Verdier involution, establishing the foundational
79:\subsection{The ambient complex and Verdier involution}
82:\index{Verdier involution!on ambient complex}
102:family is perfect
103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
137:\item \emph{Verdier self-duality.}
144: \begin{equation}\label{eq:thqg-III-verdier-self-duality}
149: where $\mathbb{D}$ denotes Verdier duality on
166:Lemma~\ref{lem:perfectness-criterion}(ii)).
176:The Koszul pairing restricts to a perfect pairing on centers
178:(Corollary~\ref{cor:duality-bar-complexes-complete} and
182:By Verdier duality for constructible sheaves on smooth proper
197:\begin{construction}[Verdier involution on the ambient complex]
199:\index{Verdier involution!construction|textbf}
200:The Verdier self-duality of
204:(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
206:\begin{equation}\label{eq:thqg-III-sigma-def}
 succeeded in 53ms:
 $\overline{\mathcal{M}}_g$.

\item \emph{Functoriality.}
 The assignment $(\cA, \cA^!) \mapsto \mathbf{C}_g(\cA)$
 is functorial in morphisms of Koszul pairs.
\end{enumerate}
\end{proposition}

\begin{proof}
\emph{Part (i).}
The cohomological dimension of $\overline{\mathcal{M}}_g$ is
$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
by Artin vanishing for proper DM stacks
\cite[\S4.1]{Olsson16}. The stalks of
$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
(finite-dimensional fiber cohomology,
Lemma~\ref{lem:perfectness-criterion}(ii)).
By constructibility of $\mathcal{Z}(\cA)$
(Lemma~\ref{lem:quantum-ss-convergence}, condition (2)),
each cohomology sheaf $R^q\pi_{g*}\barB^{(g)}(\cA)$
 succeeded in 52ms:
\Phi(\cA) + \Phi(\cA^!) = \Phi_{\mathrm{total}}
\]
holds with $\Phi_{\mathrm{total}}$ independent of the choice
of $\cA$ within its Koszul pair.
\end{corollary}

\begin{proof}
Since $\Phi$ factors through
$\mathcal{H}_g(\cA) = Q_g(\cA) \oplus Q_g(\cA^!)$,
the restriction of $\Phi$ to each summand gives the
decomposition. Independence of $\Phi_{\mathrm{total}}$
from the choice of $\cA$ within $\{\cA, \cA^!\}$
follows from the symmetry $Q_g(\cA) \oplus Q_g(\cA^!)
= Q_g(\cA^!) \oplus Q_g((\cA^!)^!) = Q_g(\cA^!) \oplus Q_g(\cA)$.
\end{proof}

\begin{corollary}[Dimension parity;
\ClaimStatusProvedHere]
\label{cor:thqg-III-dimension-parity}
For a Koszul self-dual chiral algebra $\cA \cong \cA^!$ and

thinking
**Clarifying theorem context**

I need to gather more context about theorem proof in stage 4, and possibly the self-dual-halving theorem around 694. It seems like I might need to look into theorems maybe around 640 as well. I think checking lines 600 to 710 could help me find the self-dual theorem. I should also consider any contradictions around line 694 since the self-dual-halving theorem uses all g ≥ 0. So, inspecting the surrounding material will be essential!
codex
The contradiction is local and real: the file proves `Q_0(\cA)=Z(\cA)` and `Q_0(\cA^!)=0`, so any all-genus duality statement is false as written. I’m reading the downstream corollaries that advertise the false all-genus version, then I’ll patch the theorem surface consistently.
exec
/bin/zsh -lc "sed -n '720,820p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '600,700p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '900,1075p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{complementarity!genus 1}
At genus~$1$,
$H^*(\overline{\mathcal{M}}_{1,1})
= \mathbb{Q} \oplus \mathbb{Q}\lambda_1$
with $\lambda_1 = c_1(\mathbb{E})$ the Hodge class.
For the Heisenberg algebra $\mathcal{H}_\kappa$:
\begin{equation}\label{eq:thqg-III-heisenberg-genus-1}
Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa,
\qquad
Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda_1.
\end{equation}
The central extension $\kappa$ is an obstruction for
$\mathcal{H}_\kappa$ (eigenvalue $+1$); the Hodge class
$\lambda_1$ is the curvature for $\mathcal{H}_\kappa^!$
(eigenvalue $-1$).
\end{proposition}

\begin{proof}
The involution $\sigma$ acts on the
two-dimensional space $H^0 \oplus H^2$ of
 succeeded in 51ms:
the Verdier--Koszul duality, i.e., $\alpha$ comes from the
$j_*$-extension of bar cochains of $\cA$
(Lemma~\ref{lem:eigenspace-decomposition-complete}).
The genus-$g$ quantum correction space $Q_g(\cA)$ is precisely
the subspace of $H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$
arising from bar cochains of $\cA$ in the $j_*$-extension
(Lemma~\ref{lem:quantum-from-ss}).

Symmetrically, $\mathbf{C}_g^-$ consists of cochains fixed by
$-\sigma$, which come from the $j_!$-extension of bar
cochains of $\cA^!$ (equivalently, cobar cochains of $\cA$),
giving $\mathbf{C}_g^- \simeq \mathbf{Q}_g(\cA^!)$.

\emph{Stage 4: S-level decomposition and duality.}
Applying $H^*$ to the direct sum
\eqref{eq:thqg-III-direct-sum} gives:
\[
H^*(\mathbf{C}_g(\cA))
= H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
= Q_g(\cA) \oplus Q_g(\cA^!).
 succeeded in 52ms:
\ClaimStatusConditional]
\label{thm:thqg-III-bv-lagrangian}
\index{BV algebra!Lagrangian polarization}
Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}.
Let $(\cA, \cA^!)$ be a chiral Koszul pair and $g \ge 1$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The dg Lie algebra
 $L_g := \barB^{(g)}(\cA)[1]$ carries a nondegenerate
 invariant pairing of degree $-1$, making $\MC(L_g)$
 a $(-1)$-shifted symplectic formal moduli problem.

\item The $\sigma$-eigenspace decomposition
 $L_g = L_g^+ \oplus L_g^-$ provides complementary
 Lagrangian subspaces.

\item $L_g^+$ controls deformations of $\cA$ at genus $g$;
 $L_g^-$ controls deformations of $\cA^!$ at genus $g$.
\end{enumerate}
\end{theorem}

thinking
**Examining proof validity**

I need to check the construction and the proposition for proving sigma squared using expectation values, as it might be invalid without certain conditions being perfect. I'll read more about the proof, specifically around lines 238 to 290. It seems crucial to understand those sections to ensure everything is valid and meets the requirements. I’m eager to dive into this and clarify any uncertainties!
exec
/bin/zsh -lc "sed -n '238,290p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '90,190p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thqg-III-eigenspace-decomposition|self-dual-halving|quantum-dual-complete|duality-bar-complexes-complete|center-isomorphism|perfectness-criterion|quantum-from-ss|eigenspace-decomposition-complete" chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{Verdier involution!involutivity}
The endomorphism $\sigma$ of
Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
satisfies:
\begin{enumerate}[label=\textup{(\alph*)}]
\item $\sigma^2 = \id$ \textup{(}involutivity\textup{)}.
\item The Verdier pairing
 $\langle -, - \rangle_{\mathbb{D}} \colon
 \mathbf{C}_g(\cA) \otimes \mathbf{C}_g(\cA) \to
 \mathbb{C}[{-(3g{-}3)}]$
 satisfies the anti-symmetry
 \begin{equation}\label{eq:thqg-III-anti-symmetry}
 \langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
 = -\langle v, w \rangle_{\mathbb{D}}
 \end{equation}
 for all $v, w \in \mathbf{C}_g(\cA)$.
\end{enumerate}
\end{proposition}

\begin{proof}
 succeeded in 52ms:
\label{def:thqg-III-holographic-ambient}
\index{holographic ambient complex|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair and let $g \ge 0$.
The \emph{holographic ambient complex} at genus~$g$ is the cochain
complex
\begin{equation}\label{eq:thqg-III-holographic-ambient}
\mathbf{C}_g(\cA)
:= \RGamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
\end{equation}
where $\mathcal{Z}(\cA)$ is the center local system on the
Deligne--Mumford--Knudsen compactification
$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
family is perfect
(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
identification
(Theorem~\ref{thm:fiber-center-identification}) gives
\begin{equation}\label{eq:thqg-III-bar-center}
\mathbf{C}_g(\cA)
\simeq
\RGamma(\overline{\mathcal{M}}_g,
 succeeded in 52ms:
60:\S\ref{subsec:thqg-III-eigenspace-decomposition} proves the
103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
141: (Lemma~\ref{lem:center-isomorphism}) induce a
166:Lemma~\ref{lem:perfectness-criterion}(ii)).
178:(Corollary~\ref{cor:duality-bar-complexes-complete} and
179:Lemma~\ref{lem:center-isomorphism}).
227:Corollary~\ref{cor:duality-bar-complexes-complete},
230:via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
391:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
464:\label{subsec:thqg-III-eigenspace-decomposition}
474:\label{thm:thqg-III-eigenspace-decomposition}
602:(Lemma~\ref{lem:eigenspace-decomposition-complete}).
606:(Lemma~\ref{lem:quantum-from-ss}).
640:(Corollary~\ref{cor:quantum-dual-complete}).
689:(Theorem~\ref{thm:self-dual-halving}).
939: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
1016:(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}), the
1053:cohomology (Lemma~\ref{lem:perfectness-criterion}).
1689:(Theorem~\ref{thm:self-dual-halving}).
1907:\textup{(}Theorem~\textup{\ref{thm:self-dual-halving})}.

thinking
**Searching for theorems**

I need to locate the self-dual-halving theorem label, possibly in a different file. I can use `rg` for that. Also, I should check `cor:quantum-dual-complete` in another file. The instructions say I can only edit a specific file, but I can read others. I want to verify if `cor:quantum-dual-complete` is applicable for \(g \geq 1\). It’s important to look into that, and I should also check `cor:duality-bar-complexes-complete` for any reflexivity hypothesis. I’ll search quickly!
codex
I’m now checking the cited support statements outside this file, because the right fix depends on what is actually proved elsewhere. If the imported duality already carries `g \ge 1` or perfectness, I should mirror that here rather than invent a stronger local claim.
exec
/bin/zsh -lc "rg -n \"label\\{thm:self-dual-halving\\}|label\\{cor:quantum-dual-complete\\}|label\\{cor:duality-bar-complexes-complete\\}|label\\{lem:center-isomorphism\\}|label\\{lem:perfectness-criterion\\}\" chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "self-dual-halving|quantum-dual-complete|duality-bar-complexes-complete|center-isomorphism|perfectness-criterion" chapters/theory chapters/connections chapters/examples appendices' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:280:\label{lem:perfectness-criterion}
chapters/theory/higher_genus_complementarity.tex:1128:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1222:\label{cor:quantum-dual-complete}
chapters/theory/higher_genus_complementarity.tex:1482:\label{lem:center-isomorphism}
chapters/theory/higher_genus_complementarity.tex:2324:\begin{theorem}[Self-dual halving; \ClaimStatusProvedHere]\label{thm:self-dual-halving}
 succeeded in 51ms:
chapters/connections/thqg_symplectic_polarization.tex:103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
chapters/connections/thqg_symplectic_polarization.tex:141: (Lemma~\ref{lem:center-isomorphism}) induce a
chapters/connections/thqg_symplectic_polarization.tex:166:Lemma~\ref{lem:perfectness-criterion}(ii)).
chapters/connections/thqg_symplectic_polarization.tex:178:(Corollary~\ref{cor:duality-bar-complexes-complete} and
chapters/connections/thqg_symplectic_polarization.tex:179:Lemma~\ref{lem:center-isomorphism}).
chapters/connections/thqg_symplectic_polarization.tex:227:Corollary~\ref{cor:duality-bar-complexes-complete},
chapters/connections/thqg_symplectic_polarization.tex:230:via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
chapters/connections/thqg_symplectic_polarization.tex:391:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
chapters/connections/thqg_symplectic_polarization.tex:640:(Corollary~\ref{cor:quantum-dual-complete}).
chapters/connections/thqg_symplectic_polarization.tex:689:(Theorem~\ref{thm:self-dual-halving}).
chapters/connections/thqg_symplectic_polarization.tex:939: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
chapters/connections/thqg_symplectic_polarization.tex:1053:cohomology (Lemma~\ref{lem:perfectness-criterion}).
chapters/connections/thqg_symplectic_polarization.tex:1689:(Theorem~\ref{thm:self-dual-halving}).
chapters/connections/thqg_symplectic_polarization.tex:1907:\textup{(}Theorem~\textup{\ref{thm:self-dual-halving})}.
chapters/connections/thqg_symplectic_polarization.tex:1911:By Theorem~\ref{thm:self-dual-halving},
chapters/examples/genus_expansions.tex:1706:The halving theorem (Theorem~\ref{thm:self-dual-halving}) applies:
chapters/examples/genus_expansions.tex:1803:\item \emph{Algebra-dependence of $\sigma$.} Self-dual algebras give a universal $4+4$ splitting (Theorem~\ref{thm:self-dual-halving}); non-self-dual algebras have asymmetric $\sigma$-eigenspaces encoding OPE data. This is a genus-$2$ phenomenon: at genus~$1$, $\dim H^* = 2$ forces $1+1$.
chapters/connections/outlook.tex:487:(Theorem~\ref{thm:self-dual-halving}).
chapters/theory/higher_genus_complementarity.tex:76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
chapters/theory/higher_genus_complementarity.tex:92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
 succeeded in 52ms:
% Section file for Chapter: Twisted Holography and Quantum Gravity
% Result (G3): Complementarity as Shifted-Symplectic Polarization

% Local macros (providecommand only; never \newcommand in chapter files)
\providecommand{\MC}{\mathrm{MC}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
\providecommand{\Sh}{\mathrm{Sh}}
\providecommand{\gr}{\operatorname{gr}}
\providecommand{\id}{\mathrm{id}}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\Sym}{\operatorname{Sym}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\End}{\operatorname{End}}
\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\rank}{\operatorname{rank}}
\providecommand{\ad}{\operatorname{ad}}
\providecommand{\Fred}{\operatorname{Fred}}
\providecommand{\Map}{\operatorname{Map}}
exec
/bin/zsh -lc "sed -n '1110,1255p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '280,355p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2318,2355p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1470,1505p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\Omega^k_{\log}(\overline{C}_n(X)) \times \Omega^{2n-k}_{\log}(\overline{C}_n(X)) 
\to \mathbb{C}
\end{equation}
given by:
\begin{equation}
\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
\end{equation}
where $\text{Res}$ denotes the Poincaré residue map.

This pairing is also perfect, by the logarithmic Poincar\'e lemma
(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
\cong H^*(C_n(X))$; the perfectness then follows from
Poincar\'e--Lefschetz duality for the smooth quasi-projective
variety~$C_n(X)$.
\end{proof}

\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
\label{cor:duality-bar-complexes-complete}
The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
 succeeded in 52ms:
\label{lem:perfectness-criterion}
\index{perfectness criterion|textbf}
\index{bar complex!relative perfectness|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve~$X$, carrying a modular pre-Koszul datum
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
Suppose the following two conditions hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{PBW filterability.}
 The genus-$g$ bar complex $\bar{B}^{(g)}(\cA)$ admits an
 exhaustive multiplicative filtration~$F_\bullet$ such that the
 associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
 sees only the genus-$0$ collision differential~$\dzero$ and is
 Koszul-acyclic \textup{(}axioms \textup{MK1} and
 \textup{MK3} of
 Definition~\textup{\ref{def:modular-koszul-chiral})}.

\item \emph{Finite-dimensional fiber cohomology.}
 For each closed point
 $[\Sigma] \in \overline{\mathcal{M}}_g$,
 succeeded in 50ms:
complementarity sum (Theorem~\ref{thm:fermion-all-genera}), but
individual $Q_g$ need not vanish.
\end{remark}

\subsection{Self-dual algebras and critical level}

\begin{theorem}[Self-dual halving; \ClaimStatusProvedHere]\label{thm:self-dual-halving}
\index{quantum corrections!self-dual halving}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $(\cA, \cA^!)$ be a Koszul chiral pair
(Definition~\ref{def:chiral-koszul-pair}) with $\cA \cong \cA^!$
as chiral algebras. Then for all $g \geq 1$:
\begin{equation}\label{eq:self-dual-halving}
\dim Q_g(\cA) \;=\; \dim Q_g(\cA^!)
\;=\; \tfrac{1}{2}\,\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))
\end{equation}
In particular, $\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))$ is even
for every $g \geq 1$.
 succeeded in 51ms:
H^*(\bar{B}^{(g)}(\mathcal{A}))^\vee
\end{equation}
The composition $(\mathbb{D}')^\vee \circ \mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A}))
\to H^*(\bar{B}^{(g)}(\mathcal{A}))$ is the identity (by involutivity of Verdier
duality on compact smooth varieties, see Theorem~\ref{thm:verdier-duality-config-complete}).

Now, the $E_2$ page of the Leray spectral sequence
(Theorem~\ref{thm:ss-quantum}) identifies both $Q_g(\mathcal{A})$ and
$Q_g(\mathcal{A}^!)$ as subquotients of $H^*(\overline{\mathcal{M}}_g,
Z(\mathcal{A}))$, using the following canonical identification of centers.

\begin{lemma}[Center isomorphism via module Koszul duality; \ClaimStatusProvedHere]
\label{lem:center-isomorphism}
For a Koszul chiral pair $(\mathcal{A}, \mathcal{A}^!)$, there is a canonical
isomorphism $Z(\mathcal{A}) \cong Z(\mathcal{A}^!)$.
\end{lemma}

\begin{proof}[Proof of Sublemma]
Since every $E_\infty$-chiral algebra is in particular an $E_1$-chiral algebra, and the Koszul property at the $E_\infty$ level implies Koszulity at the $E_1$ level (the forgetful functor is exact on bar complexes), we may apply the module Koszul duality equivalence
(Theorem~\ref{thm:e1-module-koszul-duality}), which gives:
ERROR: exceeded retry limit, last status: 429 Too Many Requests, request id: 24431cd4-f6a0-4ada-8a01-c6d6d3d2337b
tokens used
58,540
