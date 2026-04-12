# R13_introduction (71s)



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
session id: 019d83b2-f1a4-7e32-b815-a72d29315bb1
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


TARGET: chapters/theory/introduction.tex

FINDINGS TO FIX:

1. [CRITICAL T09] Line ~368: Incorrectly attributes the E1 ordered MC2 statement to
   thm:mc2-bar-intrinsic, which only proves the g^mod (symmetric/modular) version.
   The E1 version is in e1_modular_koszul.tex:290.
   FIX: Correct the cross-reference. Either cite the E1 theorem separately, or qualify
   that the introduction states the stronger E1 version which is proved in e1_modular_koszul.tex.

2. Lines ~2091-2092: Advertises MC4 application to V_k(g), Vir_c, W-algebras, lattices.
   But prop:standard-strong-filtration has the wrong inequality (T11 finding).
   FIX: Add qualification that the strong filtration requires weight-completion hypothesis.

Read the file, find these specific references, fix them.
mcp startup: no servers



thinking
**Assessing file modifications**

I need to modify a specific file, chapters/theory/introduction.tex. I'm thinking about reading AGENTS and some required first reads before I dive into the mathematical edits. To do this well, I should first familiarize myself with CLAUDE.md and other relevant documents. I’m focusing on rectifying mathematical parts and possibly using `beilinson-rectify` if that's required for the findings. I'll start with commentary updates, which need to happen frequently, while inspecting the file for necessary changes.
thinking
**Using explorer agents**

I can utilize the commentary tool in parallel to run multiple commands, which sounds efficient! I don’t always need Python for reading; I could use `rg`. The instructions suggest preferring the explorer for any codebase questions. However, since this is a math manuscript, it might not be absolutely necessary. But, to follow the guidelines, I should probably spawn the explorer agent to locate references and access relevant theorem labels, as the instructions emphasize their speed and authority over manual searches.
thinking
**Gathering context for editing**

To gather context, I think it's a good idea to spawn the explorer to pinpoint exact locations and relevant references. Then, I can still inspect the target file myself for editing. I might open the skill file to refer to the instructions, which say I should open SKILL.md after deciding on a skill. I could also use `exec_command cat`, but just enough to get what I need. Since this involves substantial updates, a short plan might still be useful. I'll start with a commentary update to acknowledge this step.
codex
Using `beilinson-rectify` for a scoped manuscript correction in [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex). I’m reading the required context and locating the two cited surfaces before patching only that file.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 120ms:
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
 succeeded in 145ms:
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

 succeeded in 155ms:
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

 succeeded in 175ms:
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
**Evaluating file inspection**

I need to inspect the target file, focusing on relevant lines and dependencies. I might want to use the explorer tool since the instructions suggest preferring it. I’ve already read it manually, but using the explorer could help me locate exact findings and surrounding context. I'll spawn the explorer to identify these lines and references quickly without overdoing it. So, I’ll keep it efficient and effective!
codex
I’ve loaded the rectification workflow and constitutional sources. Next I’m checking the exact introduction passages against the proving surfaces for `thm:mc2-bar-intrinsic`, the E1 theorem in `e1_modular_koszul.tex`, and the MC4 filtration hypothesis before editing.
collab spawn_agent(call_JYz9ck0RRcTO1RsLWqa457lW, prompt="Inspect the manuscript surfaces for two findings in chapters/theory/introduction.tex. 1) Locate the line around ~368 tha…")
mcp startup: no servers
spawn_agent(call_JYz9ck0RRcTO1RsLWqa457lW, prompt="Inspect the manuscript surfaces for two findings in chapters/theory/introduction.tex. 1) Locate the line around ~368 tha…") pending init:
  agent: 019d83b3-6063-7191-adc2-8dc2d17102df
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '300,450p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 & \checkmark & & & & \\
FG~\cite{FG12}
 & \checkmark & \checkmark\textsuperscript{*} & & & \\
CG~\cite{CG17}
 & & & & & \\
GLZ~\cite{GLZ22}
 & \checkmark\textsuperscript{*} & & & & \\
MS~\cite{MS24}
 & & & & & \\
\textbf{This work}
 & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
\bottomrule
\end{tabular}
\end{center}

\noindent
{\footnotesize ${}^*$FG: inversion at genus~$0$ for Lie-type bar
complexes. GLZ: adjunction at genus~$0$, degree~$2$ only.}

\smallskip\noindent
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "mc2-bar-intrinsic" -n chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
108:(Theorem~\ref{thm:mc2-bar-intrinsic}).
374:(Theorem~\ref{thm:mc2-bar-intrinsic}); since
570: (Theorem~\ref{thm:mc2-bar-intrinsic}).
724:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
885:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
1801: proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
1997:(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
2073:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
2082:\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
2264:in Theorem~\ref{thm:mc2-bar-intrinsic}. Every chapter either

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2050,2130p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).

\subsection{Entanglement entropy from the shadow obstruction tower}

At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).

Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.

Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.

\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.

\begin{center}
\small
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '340,400p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\medskip\noindent\textbf{The boundary-bulk reconstruction thesis.}
\emph{The boundary chiral algebra~$\cA$ determines its bulk via the
chiral derived centre~$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$; the
modular characteristic~$\kappa(\cA)$ is the holographic central charge;
the shadow obstruction tower~$\{S_r(\cA)\}_{r \ge 2}$ is the holographic
correction hierarchy; and the Drinfeld double
$U_\cA = \cA \bowtie \cA^!$ is the universal boundary-bulk algebra.}
The bar complex computes the boundary $\mapsto$ bulk transform; the
cobar inverts it on the Koszul locus.
Each theorem isolates one structural property of this transform.
Theorem~A constructs the bar-cobar adjunction and its Verdier intertwining
(Definition~\ref{def:chiral-koszul-pair}).
Theorem~B inverts the transform: at genus~$0$ via chiral
Koszulity (Theorem~\ref{thm:koszul-equivalences-meta}),
at genus~$g \ge 1$ via the inductive genus step.
Theorem~C constrains the Koszul dual pair by a family-specific sum rule:
$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
Kac--Moody and free fields and $K = 13$ for Virasoro
(self-dual at $c = 13$).
Theorem~D identifies $\kappa$
thinking
**Inspecting file dependencies**

I'm considering inspecting the target file to locate specific lines and their dependencies. It seems I might not need the entire file but definitely want to focus on lines related to a certain theorem in the e1 file, particularly around line 290 and the concept of strong filtration. I should probably use parallel execution for efficiency. It’s all about finding the right balance to get the information I need without getting too bogged down!
exec
/bin/zsh -lc "sed -n '320,410p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2050,2135p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '250,340p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1040,1115p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:mc2-bar-intrinsic|standard-strong-filtration|MC4|weight-completion|weight completion|strong filtration|lattice|V_k\\(\\\\fg\\)|Vir|W-algebra\" chapters/theory/introduction.tex chapters/theory/e1_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
No existing framework proves all five.
Theorems~C and~D require the genus tower, which requires
the full modular bar complex on $\overline{\mathcal{M}}_{g,n}$
(the log FM compactifications of~\cite{Mok25}), and Theorem~H requires the chiral
Hochschild complex, which combines all degrees simultaneously.
This monograph proves all five by developing the ordered bar
complex $\barB^{\mathrm{ord}}(\cA)$ as the primitive object and
extracting the five theorems as $\Sigma_n$-coinvariant projections
of its Maurer--Cartan element~$\Theta_\cA$.


\section{The five theorems}
\label{sec:NAP-unifying}
\label{sec:main-results-complete}
\index{Koszul duality!chiral|textbf}
\index{modular Koszul duality|textbf}
\index{quantum corrections!as modular completion}

The selection principle determines which algebraic inputs are admissible. The five theorems characterize the universal output.

 succeeded in 52ms:
The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).

\subsection{Entanglement entropy from the shadow obstruction tower}

At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).

Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.

Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.

\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.

\begin{center}
\small
 succeeded in 51ms:
\prod_{\substack{g,n \\ 2g-2+n > 0}}
\operatorname{Hom}\!\bigl(
\cM_{\Ass}(g,n),\,
\operatorname{End}_{\cA}(n)
\bigr).
\end{equation}
The Hom carries no $\Sigma_n$-equivariance; this is the structural
distinction from $\gAmod =
\prod \operatorname{Hom}_{\Sigma_n}(\cM_\Com(g,n),
\operatorname{End}_\cA(n))$
(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
uses the symmetric cooperad $\mathrm{Sym}^c$ obtained from $T^c$ by external
$\Sigma_n$-coinvariants. The dg~Lie structure is inherited from
$F\!\Ass$: $D$ from $D_{F\!\Ass}$, $[-,-]$ from ribbon-graph
composition.
The \emph{averaging map}
\begin{equation}
\label{eq:e1-to-einfty-projection}
\operatorname{av}\colon
{\gAmod}^{E_1}
 succeeded in 52ms:
$b = \varprojlim_N b_N$, $\Delta = \varprojlim_N \Delta_N$,
$h = \varprojlim_N h_N$. The curved coalgebra identities hold
quotientwise and hence on the limit. The completed twisting morphism
$\widehat\tau := \varprojlim_N \tau_N$ is well-defined as a
degree-$+1$ map $\widehat{\bar B}^{\mathrm{ch}}(\cA) \to \cA$.

\emph{Continuity: the MC equation converges.}
By Lemma~\ref{lem:degree-cutoff}, modulo $F^{N+1}$ only degrees
$\le N$ contribute to the convolution product $\widehat\tau \star
\widehat\tau$. The MC equation
$\partial(\widehat\tau) + \widehat\tau \star \widehat\tau = 0$
therefore holds modulo $F^{N+1}$ (where it reduces to the
finite-stage equation for~$\tau_N$), hence on the completed
coalgebra. The bar differential $\widehat{b}$ is continuous
because the inverse-limit topology is initial for the projections.

\emph{Pronilpotence.}
The reduced coproduct on bar-length-$\le m$ elements is nilpotent on each finite
quotient (since bar length is bounded). Passing to the inverse limit
gives topological pronilpotence.
 succeeded in 50ms:
chapters/theory/e1_modular_koszul.tex:316:construction (Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/theory/e1_modular_koszul.tex:1302:(Virasoro at generic~$c$), the BBJ framework requires a
chapters/theory/e1_modular_koszul.tex:1570:\item \emph{Odd desuspended degree} ($h$ even: Virasoro $h{=}2$, $W_3$ generator $T$ at $h{=}2$):
chapters/theory/e1_modular_koszul.tex:1598:every degree, explaining how the Virasoro algebra (single generator,
chapters/theory/e1_modular_koszul.tex:1625:Virasoro
chapters/theory/e1_modular_koszul.tex:1667: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:1695: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:1718: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:2339: desuspended degree~\textup{(}$h$ even: Virasoro\textup{)},
chapters/theory/e1_modular_koszul.tex:2363: For Virasoro single generator \textup{(}$d=1$\textup{)}, the
chapters/theory/bar_cobar_adjunction_curved.tex:28:algebra is quadratic: Virasoro, $\mathcal{W}_N$, and
chapters/theory/bar_cobar_adjunction_curved.tex:70: no completion needed (Heisenberg, free fields, lattice VOAs);
chapters/theory/bar_cobar_adjunction_curved.tex:73: $d_{\mathrm{fib}}^2 = \kappa \cdot \omega_g$ (affine algebras, Virasoro);
chapters/theory/bar_cobar_adjunction_curved.tex:78: MC4 completion (proved; Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/theory/bar_cobar_adjunction_curved.tex:168:The Virasoro algebra cannot be quadratic: the Virasoro OPE
chapters/theory/bar_cobar_adjunction_curved.tex:173:$\barB(\mathrm{Vir}_c)$ is curved: its
chapters/theory/bar_cobar_adjunction_curved.tex:236:% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
chapters/theory/bar_cobar_adjunction_curved.tex:252:\item $\kappa(\mathcal{A})$ is the coefficient of the Hodge class in $d_{\mathrm{fib}}^2$, hence the strength of the genus-$g$ gravitational backreaction. In that dictionary, $\kappa(\mathcal{A})$ is the Newton coupling. It is family-specific: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$ for affine Kac--Moody, $\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro, and $\kappa(\mathcal{B}^k) = c/6$ for Bershadsky--Polyakov.
chapters/theory/bar_cobar_adjunction_curved.tex:253:\item The critical gravitational coupling is the fixed point of the duality involution on the scalar lane. When the scalar complementarity constant is written as $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = K_\kappa(\mathcal{A})$, the fixed point is $\kappa_{\mathrm{crit}} = K_\kappa(\mathcal{A})/2$. This constant is family-specific. For affine Kac--Moody, Heisenberg, and free-field families one has $K_\kappa = 0$, so $\kappa_{\mathrm{crit}} = 0$. For Virasoro one has $K_\kappa = 13$, so $\kappa_{\mathrm{crit}} = 13/2$, equivalently $c = 13$. For the Bershadsky--Polyakov family the manuscript uses $\kappa(\mathcal{B}^k) = c/6$ together with the central-charge conductor $c(\mathcal{B}^k) + c((\mathcal{B}^k)^!) = 196$; hence the self-dual central charge is $c = 98$, and the induced scalar critical coupling is $\kappa_{\mathrm{crit}} = 49/3$.
chapters/theory/bar_cobar_adjunction_curved.tex:313:For example, the Virasoro algebra and $W_\infty$ need completion, while Heisenberg and Kac--Moody (conilpotent) do not.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '250,330p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\prod_{\substack{g,n \\ 2g-2+n > 0}}
\operatorname{Hom}\!\bigl(
\cM_{\Ass}(g,n),\,
\operatorname{End}_{\cA}(n)
\bigr).
\end{equation}
The Hom carries no $\Sigma_n$-equivariance; this is the structural
distinction from $\gAmod =
\prod \operatorname{Hom}_{\Sigma_n}(\cM_\Com(g,n),
\operatorname{End}_\cA(n))$
(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
uses the symmetric cooperad $\mathrm{Sym}^c$ obtained from $T^c$ by external
$\Sigma_n$-coinvariants. The dg~Lie structure is inherited from
$F\!\Ass$: $D$ from $D_{F\!\Ass}$, $[-,-]$ from ribbon-graph
composition.
The \emph{averaging map}
\begin{equation}
\label{eq:e1-to-einfty-projection}
\operatorname{av}\colon
{\gAmod}^{E_1}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:standard-strong-filtration" -n chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1093:\label{prop:standard-strong-filtration}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1070,1110p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
finite-stage counit $\epsilon_N\colon
\Omega^{\mathrm{ch}}(\bar B^{\mathrm{ch}}(\cA_{\le N}))
\xrightarrow{\sim} \cA_{\le N}$, which is a quasi-isomorphism by the
finite-stage theorem. Now apply the complete filtered comparison lemma
(Lemma~\ref{lem:complete-filtered-comparison}; Milnor exact sequence +
surjective quotient tower):
\[
0 \to \varprojlim\nolimits^1_N H^{m-1}(\operatorname{Cone}(\epsilon_N))
\to H^m(\operatorname{Cone}(\widehat\epsilon))
\to \varprojlim_N H^m(\operatorname{Cone}(\epsilon_N)) \to 0.
\]
The right term vanishes because each $\epsilon_N$ is a quasi-isomorphism.
The left term vanishes because the surjective quotient tower is
Mittag--Leffler. Hence $\widehat\epsilon$ is a quasi-isomorphism.

\emph{Step~4: unit on the coalgebra side.}
By the same quotientwise argument: the quotient of $\widehat\eta$ modulo
$F^{N+1}$ is the finite-stage unit, which is a quasi-isomorphism.
Lemma~\ref{lem:complete-filtered-comparison} applies identically.
\end{proof}

thinking
**Investigating hypothesis issues**

I need to look more closely at the proposition regarding standard-strong filtration to better understand the actual hypothesis issue at hand. It seems like I've found something regarding the wrong inequality, T11, and I might need to qualify the weight-completion hypothesis. I should also check the theorem statement to see if it mentions weight-completion. Let's dig into the proposition a bit more to clarify things!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1110,1150p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the inverse limit of the finite weight truncations is the weight
 completion,
 \[
 \varprojlim_N \cA_{\le N} \cong \widehat{\cA}^{\mathrm{wt}},
 \]
 and the direct sum~$\cA$ embeds into $\widehat{\cA}^{\mathrm{wt}}$ as
 a dense subspace; in particular, the direct-sum algebra~$\cA$ is not
 identified with this inverse limit unless it is already weight-complete;
\item the finite truncations $\{\cA_{\le N}\}_{N \ge 0}$ form an inverse
 system of finite-type curved chiral $\Ainf$-algebras;
\item for the reduced bar complexes
 \[
 C_N := \bar B(\cA_{\le N}),
 \]
 the total conformal-weight filtration
 \[
 F_{\le w}C_N
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1150,1190p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Each family carries the standard nonnegative conformal-weight
decomposition
\[
\cA = \bigoplus_{h \ge 0} \cA_h
\]
with finite-dimensional weight spaces. For affine Kac--Moody,
Virasoro, and principal~$\mathcal{W}$-algebras this is the usual
$L_0$-grading by conformal weight; for a positive-definite even lattice
vertex algebra, finite-dimensionality of each~$\cA_h$ follows because
only finitely many lattice vectors have a given norm.

The finite truncation $\cA_{\le N}$ is therefore finite-dimensional.
The transition map $\cA_{\le N+1} \twoheadrightarrow \cA_{\le N}$ is
the quotient by the weight-$(N+1)$ summand, so the inverse system
$\{\cA_{\le N}\}_N$ is well defined. Its inverse limit is the product
\[
\varprojlim_N \cA_{\le N}
\cong \prod_{h \ge 0} \cA_h
= \widehat{\cA}^{\mathrm{wt}},
\]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1190,1230p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\]
so residue extraction never increases conformal weight. Iterating this
estimate through the $A_\infty$ terms shows that every summand of the
bar differential weakly decreases total conformal weight. Equivalently,
\begin{equation}\label{eq:bar-weight-preservation}
d_{\mathrm{bar}}(F_{\le w}C_N) \subset F_{\le w}C_N .
\end{equation}
This is the correct bar-level statement corresponding to the OPE weight
formula. It does \emph{not} imply the strong-filtration axiom
\eqref{eq:strong-filtration-condition} on~$\cA$ itself; for instance,
for affine currents one has
$\operatorname{wt}(J^a_{(0)}J^b)=1<2$.

Finally, if a homogeneous bar word has total conformal weight at most
$w$, then each letter occurring in it has weight at most~$w$. Hence for
$N \ge w$ every such word already lies in $\bar B(\cA_{\le N})$, and
the transition map $C_{N+1} \to C_N$ is an isomorphism on
$F_{\le w}$. This proves~\textup{(}iv\textup{)}, and the conclusion
about Proposition~\ref{prop:mc4-weight-cutoff} is immediate.
\end{proof}
codex
The target passages are located. I’m now pinning the exact proving surfaces so the introduction only claims what those results actually establish, with no spillover from the stronger informal summary.
exec
/bin/zsh -lc "sed -n '1115,1195p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \[
 \varprojlim_N \cA_{\le N} \cong \widehat{\cA}^{\mathrm{wt}},
 \]
 and the direct sum~$\cA$ embeds into $\widehat{\cA}^{\mathrm{wt}}$ as
 a dense subspace; in particular, the direct-sum algebra~$\cA$ is not
 identified with this inverse limit unless it is already weight-complete;
\item the finite truncations $\{\cA_{\le N}\}_{N \ge 0}$ form an inverse
 system of finite-type curved chiral $\Ainf$-algebras;
\item for the reduced bar complexes
 \[
 C_N := \bar B(\cA_{\le N}),
 \]
 the total conformal-weight filtration
 \[
 F_{\le w}C_N
 := \operatorname{span}\left\{
 s^{-1}a_1|\cdots|s^{-1}a_r \,\middle|\,
 \sum_{j=1}^r \operatorname{wt}(a_j) \le w
 \right\}
 \]
exec
/bin/zsh -lc "sed -n '540,590p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,125p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,740p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1788,1810p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1988,2004p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \to
 \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
 \]
 is intertwined with Verdier duality
 (Chapter~\ref{chap:bar-cobar}):
 $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA)
 \simeq \cA^!_\infty$
 (factorization \emph{algebra}, not coalgebra),
 functorial in families
 over~$\overline{\mathcal{M}}_{g,n}$.
 It decomposes into chiral twisting morphisms
 ($\mathrm{A}_0$,
 Theorem~\ref{thm:fundamental-twisting-morphisms}),
 bar concentration
 ($\mathrm{A}_1$, Theorem~\ref{thm:bar-concentration}), and
 Verdier-geometric duality
 ($\mathrm{A}_2$,
 Theorem~\ref{thm:bar-cobar-isomorphism-main}).
 On the proved genus-$0$ locus, the bar complex admits a BRST
 comparison; Verdier duality is the algebraic shadow of CPT.
 succeeded in 51ms:
$\Delta = 8\kappa S_4$ forces $r_{\max}$ to lie in
$\{2, 3, \infty\}$ on any one-dimensional primary slice
(Theorem~\ref{thm:single-line-dichotomy}); the
fourth class $r_{\max} = 4$ arises from stratum
separation.
The algebraic depth $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
admits no value~$3$ or any finite value $\geq 3$
(Proposition~\ref{prop:depth-gap-trichotomy}).
Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
$k \geq 3$) holds if and only if the algebra belongs to
class~$\mathbf{G}$
(Proposition~\ref{prop:sc-formal-iff-class-g}).
For free-field algebras, the scalar formula
$F_g = \kappa \cdot \lambda_g$ is exact at all genera
(all-weight): the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


Three depths measure distinct aspects of the tower.
 succeeded in 52ms:
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}): the
 Koszul dual algebra as theorem, not definition-by-analogy.
\item \emph{Genus-$1$ curvature.}
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot
 \operatorname{id}$
 (Theorem~\ref{thm:genus-universality}). The natural home is
 Positselski's coderived category: quantum corrections are a
 change of ambient category, not extra terms.
\item \emph{Clutching of stable curves.}
 The genus tower is compatible with boundary clutching via the
 modular operad (Theorem~\ref{thm:prism-higher-genus}).
 The combinatorics is stable graphs, not trees, and
 $\Theta_\cA$ (Theorem~\ref{thm:universal-MC},
 proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
 is compatible with clutching, trace, and Verdier duality.
\item \emph{Associative structure.}
 \index{ordered factorization|see{$\Eone$-chiral algebra}}
 The Yangian $Y(\mathfrak{g})$ is $\Eone$-chiral
 (Definition~\ref{def:e1-chiral}): its bar complex uses ordered
 configuration spaces, and Verdier duality acts by $R$-matrix
 succeeded in 52ms:
error.
\emph{Chiral Hochschild} $\ChirHoch^*(\cA) =
H^*(\operatorname{CoDer}(\barB(\cA)))$ is the cohomology of
coderivations of the bar coalgebra; it lives on the
curve~$X$ and has cohomological amplitude~$[0,2]$ on the
Koszul locus (Theorem~H).
\emph{Topological Hochschild} $\mathrm{HH}^*_{\mathrm{top}}$
is the factorization homology on the circle $S^1$; it lives
in dimension~$1$ higher and governs the $\Eone$-chiral bar of
Volume~II.
\emph{Categorical Hochschild} $\mathrm{HH}^*(\mathrm{Rep}(\cA))$
is the Hochschild cohomology of the module category; it governs
the Drinfeld center and the $E_2$ structure.
See Principle~\ref{princ:geometric-origin-hochschild}
(Chapter~\ref{ch:algebraic-foundations}) for the geometric
origin that distinguishes all three.
\end{warning}

\begin{principle}[Five facets of $\Theta_\cA$]
\label{princ:five-facets}
 succeeded in 52ms:
finite-order projections of~$\Theta_\cA$:
$\kappa$ (degree~$2$),
$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
a projection of the next. The weight filtration on~$\gAmod$
controls extension; each truncation
$\Theta_\cA^{\le r}$ is constructive without requiring the full
all-genera modular envelope. The all-degree master equation
$D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
is automatically Maurer--Cartan because $D_\cA^2 = 0$.

\emph{Ring~3: the physics-facing frontier.}
Three axes extend the proved core toward mathematical physics.
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{The $\mathcal W$-algebra axis.}
 Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra


thinking
**Clarifying hypothesis and references in proposition**

I’m sorting out a precise summary of the proposition’s hypothesis versus the introduction’s claim about strong filtration. The introduction states that certain families satisfy a strong filtration property on the algebra, but the proposition only guarantees finite weight truncations and bar-level filtrations, not the full strong-filtration axiom. I plan to highlight the mismatch in theorem references between the introduction and the actual E1 MC element theorem, suggest minimal wording changes for clarity, and reference specific file paths and line numbers to guide any edits. This involves explaining that the proposition ensures finite completions via bar filtration but that assuming strong filtration on the algebra remains separate and should be clearly stated.

codex
- E₁ Maurer–Cartan citation: `chapters/theory/introduction.tex:350-380` strings the ordered-bar MC element to Theorem `thm:mc2-bar-intrinsic`, but the local claim is “the ordered bar differential on `\barB^{\mathrm{ord}}(\cA)` defines an E₁ Maurer–Cartan element”; the actual theorem that establishes that is `thm:e1-mc-element` in `chapters/theory/e1_modular_koszul.tex:266-305`. To avoid confusion, link that paragraph and Theorem MC2 to `\ref{thm:e1-mc-element}` (and keep `\ref{thm:mc2-bar-intrinsic}` for the bar-intrinsic construction in the proof of `thm:e1-mc-element`).

- MC4 application scope: the introduction’s Mechanism 1 claim (`chapters/theory/introduction.tex:2040-2110`) lists `V_k(\fg)`, `\mathrm{Vir}_c`, principal `\cW` and lattice algebras as instances of Proposition `prop:standard-strong-filtration`. That proposition (`chapters/theory/bar_cobar_adjunction_curved.tex:1090-1230`) actually only guarantees the standard weight truncations and the induced total-weight filtration on the finite-stage bar complexes (items (i)–(iv)) needed for Proposition `prop:mc4-weight-cutoff`. Its closing sentence emphasizes that those families “do not supply the strong-filtration axiom \eqref{eq:strong-filtration-condition} on~$\cA$ itself.” The introduction should therefore clarify that Mechanism 1’s “strong-filtration” hypothesis is still an extra assumption (or needs independent verification) and that Proposition `prop:standard-strong-filtration` only provides the bar-level weight truncations and resulting completion criteria, not an automatic strong filtration on each chiral algebra.

These changes keep the claims precise without editing the sources.
thinking
**Reviewing references and corrections**

I'm looking at multiple references to thm:mc2-bar-intrinsic related to Theta_A in gAmod, and it seems there's an incorrect attribution of E1 in an ordered statement around line 368. The user requested fixing specific references, so I'll focus on that. There might be similar misreferences elsewhere, but the action is only related to specific files. I need to check line 2073 in the MC2 table and ensure the references align properly. The critical reference is about defining Theta in gAmod^{E1}.
thinking
**Examining introduction lines for corrections**

I’m considering whether we should correct other introduction lines that incorrectly claim E1 is associated with the wrong theorem. My search shows potential issues in lines 570, 724, 885, and 1801, which seem to attribute E1 incorrectly. Though the user only flagged line 368, it's crucial to resolve every finding. A minimal edit at line 368 might not be enough to prevent similar errors. I should search for references to `E_1` around thm:mc2-bar-intrinsic to address any broader issues. I'll inspect around lines 850-900 for further E1 mentions.
codex
I found one direct misattribution at the E1 ordered MC sentence. I’m checking nearby repeated `thm:mc2-bar-intrinsic` mentions in the introduction so I don’t leave the same error a few paragraphs later.
exec
/bin/zsh -lc "sed -n '1768,1810p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '860,900p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '95,115p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1968,2002p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The five theorems and the $\Eone$ primacy thesis rest on five
geometric ingredients, which combine into a single functorial
correspondence between geometry, algebra, and physics.

\begin{remark}[Five geometric ingredients]\label{rem:five-pieces}
\index{modular Koszul duality!five irreducible pieces}
\index{geometric synthesis|textbf}
Modular Koszul duality rests on five geometric ingredients.
The first four belong to the commutative ($\Einf$) face; the fifth
to the associative ($\Eone$) face.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Three-point collision.}
 The Arnold relation
 ($\eta_{12}\wedge\eta_{23}+\eta_{23}\wedge\eta_{31}+\eta_{31}\wedge\eta_{12}=0$)
 is factorization
 coherence: fusing three insertions does not depend on the
 order of pairwise collisions. The genus-$0$ seed.
\item \emph{Verdier duality on $\operatorname{Ran}(X)$.}
 $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA) \simeq
 \cA^!_\infty$
 succeeded in 51ms:
finite-dimensional quotients of this layer, including genus-$2$
transparency and the universal genus-$3$ constant~$7$ on the shared
$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.
For class~$\mathbf{M}$ algebras the infinite tower has a computable
exponential growth rate $\rho(\cA)$ governed by the shadow metric
$Q_L$ (Proposition~\ref{prop:shadow-tower-growth-rate}); for the
Virasoro family this gives
$\rho(\mathrm{Vir}_c) =
\sqrt{(180c{+}872)/((5c{+}22)\,c^2)}$
(Remark~\ref{rem:virasoro-shadow-growth-rate}), with the
equation $\rho = 1$ cutting out the convergence/divergence
boundary at $c_\star \approx 6.125$.
The cubic shadow coefficient $\alpha_s$ on each primary line
admits a universal gravitational form determined by the conformal
weights of the strong generators alone
(Theorem~\ref{thm:w-universal-gravitational-cubic}).

The unifying principle is the modular $L_\infty$ convolution
algebra~$\gAmod$, whose $L_\infty$ structure comes
from the Feynman transform of the modular operad; $\Convstr$ is its strict model. The shadow obstruction tower consists of
 succeeded in 52ms:
 Chapter~\ref{ch:derived-langlands}). On the Koszul locus at
 generic level the bulk carries no hidden state space beyond
 the shadow obstruction tower: holographic reconstruction is
 tight.
\end{enumerate}
The five facets of Principle~\ref{princ:five-facets} are the five
algebraic consequences of the MC element; the five claims above are
the five boundary-bulk consequences of the same theorems.
\end{conjecture}

\begin{proposition}[Five facets of the collision residue $r(z)$;
 \ClaimStatusProvedHere]
\label{prop:five-facets-collision-residue}
\index{collision residue!five facets|textbf}%
\index{r-matrix@$r(z)$!five facets|textbf}%
\index{Seven Faces!and five facets of $r(z)$}%
The degree-$2$, genus-$0$ projection
\[
r(z)
\;:=\;
 succeeded in 51ms:
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


Three depths measure distinct aspects of the tower.
The \emph{shadow depth} $r_{\max}$ is the largest degree at which the shadow is nonzero.
The \emph{generating depth} $d_{\mathrm{gen}}$ is the smallest degree at which all higher operations are determined recursively.
The \emph{algebraic depth} $d_{\mathrm{alg}}$ records whether the tower terminates
(Definition~\ref{def:generating-depth}).
These are independent invariants: Virasoro has $d_{\mathrm{gen}} = 3$ but $d_{\mathrm{alg}} = \infty$; $m_3$ generates all higher operations, yet none vanish.

The tower is governed by three structure theorems, all projections of a single object: the Maurer--Cartan element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}).
\emph{Algebraicity}
(Theorem~\ref{thm:riccati-algebraicity}).
On each primary line~$L$, the shadow generating function satisfies
$H(t)^2 = t^4 Q_L(t)$,
where $Q_L$ is a quadratic polynomial in three invariants $(\kappa, \alpha, S_4)$. The
tower is the Taylor expansion of~$\sqrt{Q_L}$, algebraic of degree~$2$.
ERROR: exceeded retry limit, last status: 429 Too Many Requests, request id: d0a8263e-e6a0-45b4-95dc-f76001c8eb0a
tokens used
43,918
