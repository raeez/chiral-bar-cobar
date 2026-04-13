# R13_introduction (303s)

Edited [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:368). I re-read the two modified regions in context and checked that `thm:e1-mc-element`, `thm:mc2-bar-intrinsic`, and `prop:standard-strong-filtration` all exist. I did not run a full TeX build.

## Rectification Summary
- [FIXED] finding 1 — at [introduction.tex:368](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:368), I separated the ordered and modular statements explicitly: the ordered class is now written as `\Theta_\cA^{\Eone}` and cited to `thm:e1-mc-element`, and the next sentence states that averaging produces the modular Maurer--Cartan element of `thm:mc2-bar-intrinsic`.
- [FIXED] finding 2 — at [introduction.tex:2093](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2093), I tightened the MC4 advertisement so it now says the strong-filtration mechanism applies only after passing to the weight-completed tower, and that the standard-family MC4 statements are on weight completions, not on the uncompleted direct sums.


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
session id: 019d8685-0f54-7590-9a87-bb9299ebfb07
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
codex
I’m auditing the assigned introduction surface and the required constitutional references first, then I’ll patch only `chapters/theory/introduction.tex` with the minimum truthful changes that close both findings.
exec
/bin/zsh -lc "rg -n \"beilinson-rectify|rectify|verification|propagate|status\" .agents/skills/beilinson-rectify/SKILL.md && sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2:name: beilinson-rectify
3:description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
10:It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.
31:   status drift
43:6. After every substantive theorem-surface change, sync nearby status remarks, concordance text, duplicates, and metadata.
44:7. Run the strongest local verification available and close with a proved/computational/conditional split.
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
codex
I’ve loaded the constitutional layer and the rectification skill. Next I’m locating the two exact introduction passages and the supporting theorem/proposition surfaces they should point to, so the edit stays local and truthful.
exec
/bin/zsh -lc 'rg -n "mc2-bar-intrinsic|MC4|strong filtration|standard-strong-filtration|weight-completion|V_k|Vir|W-algebras|lattice" chapters/theory/introduction.tex chapters/theory/e1_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '330,410p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 250

chapters/theory/e1_modular_koszul.tex:345:element in Theorem~\ref{thm:mc2-bar-intrinsic}.
chapters/theory/e1_modular_koszul.tex:1000:% AP1: kappa(V_k(sl_2)) = dim(sl_2)(k+h^v)/(2h^v) = 3(k+2)/4.
chapters/theory/e1_modular_koszul.tex:1059:the affine algebra $V_k(\mathfrak{sl}_2)$ (class~$L$,
chapters/theory/e1_modular_koszul.tex:1106:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4. From C3.
chapters/theory/e1_modular_koszul.tex:1322:\int_X^{\mathrm{ord}} V_k(\fg),
chapters/theory/e1_modular_koszul.tex:1327:(Virasoro at generic~$c$), the BBJ framework requires a
chapters/theory/e1_modular_koszul.tex:1595:\item \emph{Odd desuspended degree} ($h$ even: Virasoro $h{=}2$, $W_3$ generator $T$ at $h{=}2$):
chapters/theory/e1_modular_koszul.tex:1623:every degree, explaining how the Virasoro algebra (single generator,
chapters/theory/e1_modular_koszul.tex:1650:Virasoro
chapters/theory/e1_modular_koszul.tex:1692: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:1720: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:1743: Virasoro\textup: &
chapters/theory/e1_modular_koszul.tex:2364: desuspended degree~\textup{(}$h$ even: Virasoro\textup{)},
chapters/theory/e1_modular_koszul.tex:2388: For Virasoro single generator \textup{(}$d=1$\textup{)}, the
chapters/theory/introduction.tex:45:Every standard family (Kac--Moody, Virasoro, $\mathcal{W}$-algebras, lattice vertex algebras) sits between the CG opening and the $\Eone$ atom, and the bar complex on higher-genus curves classifies them.
chapters/theory/introduction.tex:78:$r_{\max} = 4$; Virasoro and $\mathcal{W}$-algebras
chapters/theory/introduction.tex:104:These are independent invariants: Virasoro has $d_{\mathrm{gen}} = 3$ but $d_{\mathrm{alg}} = \infty$; $m_3$ generates all higher operations, yet none vanish.
chapters/theory/introduction.tex:108:(Theorem~\ref{thm:mc2-bar-intrinsic}).
 succeeded in 51ms:

\section{The five theorems}
\label{sec:NAP-unifying}
\label{sec:main-results-complete}
\index{Koszul duality!chiral|textbf}
\index{modular Koszul duality|textbf}
\index{quantum corrections!as modular completion}

The selection principle determines which algebraic inputs are admissible. The five theorems characterize the universal output.

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
exec
/bin/zsh -lc "sed -n '2060,2115p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1070,1145p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '250,330p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1465p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.

\begin{center}
\small
\begin{tabular}{llll}
\textbf{MC} & \textbf{Statement} & \textbf{Status} & \textbf{Key input} \\ \hline
MC1 & PBW concentration & \textbf{proved} & all standard families \\[2pt]
MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
MC3 & Thick generation & \textbf{proved} & CG all types + eval-core DK (Cor.~\ref{cor:mc3-all-types}); DK-4/5 downstream \\[2pt]
MC4 & $\mathcal{W}_\infty$ closure & \textbf{proved} & completion towers + weight cutoff \\[2pt]
MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}
\end{tabular}
\end{center}

 succeeded in 52ms:
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
 succeeded in 50ms:
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

\begin{proposition}[Reduction of MC4 to finite-stage compatibility;
\ClaimStatusProvedHere]
\label{prop:mc4-reduction-principle}
Let $\{C_N\}_{N \ge 0}$ be the inverse system of finite-stage bar
complexes
\[
C_N := \bar B(\cA_{\le N}),
\qquad
\widehat{C} := \varprojlim_N C_N,
\]
for a tower whose finite stages $\cA_{\le N}$ lie in the proved
bar-cobar regime. Assume:
\begin{enumerate}
\item each transition map $C_{N+1} \to C_N$ is a morphism of complexes;
\item for every cohomological degree~$m$, the inverse system
 $\{H^m(C_N)\}_N$ satisfies the Mittag--Leffler condition; and
\item the finite-stage bar-cobar quasi-isomorphisms
 $\epsilon_N \colon \Omega(C_N) \xrightarrow{\sim} \cA_{\le N}$ are
 compatible with the tower maps.

thinking
**Reviewing theorem qualifications**

I’m noticing that the current version seems fixed, but it's possible there are two instances I need to consider. I should ensure there's proper qualification on the filtration referencing the wrong inequality. I’ll search for `prop:standard-strong-filtration` in the intro and check out mentions of `thm:mc2-bar-intrinsic`, particularly around line 368. It looks like the theorem e1-mc-element already uses the correct E1 theorem, so I need to inspect this further and identify necessary changes.
codex
The dependency surfaces are clear now. `thm:e1-mc-element` is the ordered `E_1` MC theorem; `thm:mc2-bar-intrinsic` is the averaged modular version. I’m auditing every introduction sentence that cites `thm:mc2-bar-intrinsic` so I only change the mismatched ones.
exec
/bin/zsh -lc 'rg -n "thm:mc2-bar-intrinsic|thm:e1-mc-element|prop:standard-strong-filtration" chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '96,116p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    96	(Proposition~\ref{prop:free-field-scalar-exact}).
    97	
    98	
    99	Three depths measure distinct aspects of the tower.
   100	The \emph{shadow depth} $r_{\max}$ is the largest degree at which the shadow is nonzero.
   101	The \emph{generating depth} $d_{\mathrm{gen}}$ is the smallest degree at which all higher operations are determined recursively.
   102	The \emph{algebraic depth} $d_{\mathrm{alg}}$ records whether the tower terminates
   103	(Definition~\ref{def:generating-depth}).
   104	These are independent invariants: Virasoro has $d_{\mathrm{gen}} = 3$ but $d_{\mathrm{alg}} = \infty$; $m_3$ generates all higher operations, yet none vanish.
   105	
   106	The tower is governed by three structure theorems, all projections of a single object: the Maurer--Cartan element
   107	$\Theta_\cA \in \MC(\gAmod)$
   108	(Theorem~\ref{thm:mc2-bar-intrinsic}).
   109	\emph{Algebraicity}
   110	(Theorem~\ref{thm:riccati-algebraicity}).
   111	On each primary line~$L$, the shadow generating function satisfies
   112	$H(t)^2 = t^4 Q_L(t)$,
   113	where $Q_L$ is a quadratic polynomial in three invariants $(\kappa, \alpha, S_4)$. The
   114	tower is the Taylor expansion of~$\sqrt{Q_L}$, algebraic of degree~$2$.
   115	The discriminant
 succeeded in 51ms:
108:(Theorem~\ref{thm:mc2-bar-intrinsic}).
374:(Theorem~\ref{thm:e1-mc-element}); since
570: (Theorem~\ref{thm:mc2-bar-intrinsic}).
724:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
885:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
1269:(Theorem~\ref{thm:e1-mc-element}):
1372:(Theorem~\ref{thm:e1-mc-element}).
1801: proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
1997:(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
2073:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
2082:\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
2092:If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
2264:in Theorem~\ref{thm:mc2-bar-intrinsic}. Every chapter either
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '878,892p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '560,578p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '716,732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1794,1806p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1992,2100p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   878	r(z)
   879	\;:=\;
   880	\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)
   881	\;\in\;
   882	\End(V^{\otimes 2}) \otimes \cO(*\Delta)
   883	\]
   884	of the universal Maurer--Cartan element
   885	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
   886	admits five equivalent characterizations. Each is proved in the
   887	indicated chapter; all five describe the same object up to convention.
   888	\begin{enumerate}[label=\textup{(F\arabic*)}]
   889	\item \emph{Classical $r$-matrix.}
   890	 $r(z)$ is the classical limit of the quantum $R$-matrix
   891	 $R(z;\hbar) = 1 + \hbar\,r(z) + O(\hbar^2)$ of the Yangian
   892	 $Y(\cA)$; it satisfies the classical Yang--Baxter equation and
 succeeded in 50ms:
   716	\end{warning}
   717	
   718	\begin{principle}[Five facets of $\Theta_\cA$]
   719	\label{princ:five-facets}
   720	\index{MC element!five facets|textbf}%
   721	Let\/ $\cA$ be a modular Koszul chiral algebra on a smooth projective
   722	curve~$X$, and let\/ $\Theta_\cA := D_\cA - d_\cA^{(0)} \in \gAmod$
   723	be the bar-intrinsic Maurer--Cartan element
   724	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
   725	The five main theorems characterize five
   726	\emph{facets} of~$\Theta_\cA$: existence, faithfulness,
   727	decomposition, leading coefficient, and coefficient ring.
   728	\begin{enumerate}[label=\textup{(\Alph*)}]
   729	\item \emph{Arena}
   730	 \textup{(}Theorem~A\textup{)}.
   731	 $\Theta_\cA$ \textbf{exists}.
   732	 The bar--cobar adjunction constructs the modular convolution
 succeeded in 51ms:
   560	 The non-circular anchor for the $(\mathrm{ii}) \Rightarrow (\mathrm{v})$ routing in Theorem~\ref{thm:koszul-equivalences-meta} is the twisted-tensor identification (Remark~\ref{rem:bar-cobar-twisted-tensor-anchor}): the chain runs through Lemma~\ref{lem:twisted-product-cone-counit}, not through bar-cobar inversion.
   561	
   562	\item \emph{Theorem~B} (Bar-cobar inversion,
   563	 Theorem~\ref{thm:higher-genus-inversion}).
   564	 On the Koszul locus, the counit
   565	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$
   566	 is an equivalence; the spectral sequence collapses at~$E_2$.
   567	 Off the locus, the bar-cobar object persists but becomes curved;
   568	 the failure is measured by
   569	 $\Theta_\cA := D_\cA - d_\cA^{(0)}$
   570	 (Theorem~\ref{thm:mc2-bar-intrinsic}).
   571	 The BRST resolution is complete.
   572	
   573	 More precisely, there is a spectral sequence with $E_1$ page
   574	 $E_1^{p,q} = H^q(\barB^p_X(\cA))$ converging to $H^{p+q}(\Omega_X \barB_X(\cA))$.
   575	 On the Koszul locus, $E_1^{p,q} = 0$ for $p \neq 1$, so
   576	 $E_2 = E_\infty$, and the comparison map
   577	 $\varepsilon \colon \Omega_X \barB_X(\cA) \to \cA$
   578	 induces an isomorphism on cohomology. This is the categorical
 succeeded in 51ms:
  1794	 Positselski's coderived category: quantum corrections are a
  1795	 change of ambient category, not extra terms.
  1796	\item \emph{Clutching of stable curves.}
  1797	 The genus tower is compatible with boundary clutching via the
  1798	 modular operad (Theorem~\ref{thm:prism-higher-genus}).
  1799	 The combinatorics is stable graphs, not trees, and
  1800	 $\Theta_\cA$ (Theorem~\ref{thm:universal-MC},
  1801	 proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
  1802	 is compatible with clutching, trace, and Verdier duality.
  1803	\item \emph{Associative structure.}
  1804	 \index{ordered factorization|see{$\Eone$-chiral algebra}}
  1805	 The Yangian $Y(\mathfrak{g})$ is $\Eone$-chiral
  1806	 (Definition~\ref{def:e1-chiral}): its bar complex uses ordered
 succeeded in 51ms:
  1992	controls extension; each truncation
  1993	$\Theta_\cA^{\le r}$ is constructive without requiring the full
  1994	all-genera modular envelope. The all-degree master equation
  1995	$D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
  1996	bar-intrinsic construction
  1997	(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
  1998	is automatically Maurer--Cartan because $D_\cA^2 = 0$.
  1999	
  2000	\emph{Ring~3: the physics-facing frontier.}
  2001	Three axes extend the proved core toward mathematical physics.
  2002	\begin{enumerate}[label=\textup{(\alph*)}]
  2003	\item \emph{The $\mathcal W$-algebra axis.}
  2004	 Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
  2005	 at generic level is completed Koszul. Strict Koszulity is
  2006	 exceptional: the subregular family $\mathcal W_n^{(2)}$ has
  2007	 unbounded canonical homotopy degree, and the classical $W_3$ sector
  2008	 defines the first finite-degree modular higher-spin package.
  2009	 MC4 is proved: the strong completion-tower theorem
  2010	 (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
  2011	 completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,

thinking
**Inspecting for mismatches**

I want to ensure there's no mismatch elsewhere in the code. I think it would help to inspect the lines around 330-380, especially near line 368, and check for any discrepancies after the insertion. It's crucial to identify where things might not correspond to what I'm expecting. Let's look closely at those line numbers to figure this out!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '350,382p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   350	Theorem~A constructs the bar-cobar adjunction and its Verdier intertwining
   351	(Definition~\ref{def:chiral-koszul-pair}).
   352	Theorem~B inverts the transform: at genus~$0$ via chiral
   353	Koszulity (Theorem~\ref{thm:koszul-equivalences-meta}),
   354	at genus~$g \ge 1$ via the inductive genus step.
   355	Theorem~C constrains the Koszul dual pair by a family-specific sum rule:
   356	$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
   357	Kac--Moody and free fields and $K = 13$ for Virasoro
   358	(self-dual at $c = 13$).
   359	Theorem~D identifies $\kappa$
   360	as the one-loop coefficient of the bulk partition
   361	function on the uniform-weight lane; the multi-weight
   362	correction $\delta F_g^{\mathrm{cross}}$ at $g \ge 2$ is a
   363	separate higher-loop contribution.
   364	Theorem~H bounds the bulk state space: at generic level on the
   365	Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
   366	
   367	\medskip\noindent
   368	All five theorems are $\Sigma_n$-coinvariant projections of a single
   369	$E_1$ object.



thinking
**Investigating corrections in the document**

I've already fixed line 368, but there's a thought that another statement in the introduction might incorrectly cite the E1 object or a theorem. I should search for terms like "ordered bar differential" or "E_1 object." While I believe I've identified the fixes, the user wants to ensure all references are correct. 

I also might need to check lines 1801 and 1997 for a stronger version relating to the all-degree master equation with Theta in a modular context. I'll inspect those lines for necessary edits.
thinking
**Clarifying references in the document**

It seems there might be another incorrect reference that isn't caught by a simple label search, especially with Theorem universal-MC. I should search for terms like "single E1 object," "ordered," and "coinvariant projections." 

The user has asked me to read the file and fix specific references, so if one has already been addressed, I can mention that. However, it's best to clarify the E1 sentence by separately naming the modular theorem. 

Updating line 374 could strengthen the citation by referencing both `thm:e1-mc-element` and mentioning that averaging yields `thm:mc2-bar-intrinsic`. Currently, it only cites the E1 theorem, which might not be sufficient.
thinking
**Improving clarity and robustness**

To enhance clarity and avoid future confusion, I think I should add "its averaging is Theorem\ref{thm:mc2-bar-intrinsic}" in the next sentence. This would directly connect the E1 strong theorem to the modular version, creating a clear reference.

Once I add this statement, the finding will be addressed. Next, I should check if the qualification on line 2092 is sufficient. The finding mentions a wrong inequality in the proposition, which I can fix by including that the strong filtration requires a weight-completion hypothesis.
codex
The second finding is subtler: the intro already mentions weight completion, but I’m tightening that sentence so it states the actual logical dependency, namely that the strong-filtration mechanism applies only after passing to the completed tower, not to the direct sum.
exec
/bin/zsh -lc "sed -n '1145,1188p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
strong-filtration axiom~\eqref{eq:strong-filtration-condition} on
$\cA$ itself for the descending conformal-weight filtration.
\end{proposition}

\begin{proof}
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

thinking
**Considering planning steps**

I'm thinking about whether to use the PE-4 bar complex formula, but I'm not editing the formula now. The PE-11 differential form doesn't seem necessary either. Hmm, should I maybe update the plan instead since it feels substantial enough? I could probably organize an update plan with three steps. So, I'll go ahead and set that up now; it seems like the best route to take!
Plan update
The target is local to the introduction, but both findings depend on nearby theorem/proposition surfaces. I’ve located the exact passages and their supporting dependencies; next is a scoped patch and then a reread/consistency check.
  ✓ Audit the targeted introduction passages against the cited theorem/proposition surfaces
  → Patch `chapters/theory/introduction.tex` to separate the ordered `E_1` citation from the averaged modular citation and to make the MC4 weight-completion hypothesis explicit
  • Re-read the modified sections and verify labels/status coherence on the touched surface
codex
I have the exact patch. I’m changing one theorem-reference sentence to distinguish the ordered `E_1` MC class from its averaged modular shadow, and one MC4 sentence to state explicitly that the strong-filtration route applies only on the weight-completed tower.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -371,3 +371,3 @@
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
@@ -375,5 +375,6 @@
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
@@ -2092,2 +2093,3 @@
 If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..56cc53981f3e4934c3a733353d3bc5aa2018b549
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2090,6 +2091,7 @@
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
 If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..56cc53981f3e4934c3a733353d3bc5aa2018b549
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2090,6 +2091,7 @@
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
 If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}


thinking
**Inspecting for duplicates**

I need to carefully reread the surrounding context to make sure there aren’t any duplicate sentences. It seems we replaced one line but ended up inserting a duplicate instead? I should check the second patch that used the entire line context; maybe that caused the duplicate since it didn’t remove the old one properly. I’ll focus on inspecting the sections around lines 2088-2094 and 368-377 to get a clearer picture.
codex
The file is patched. I’m re-reading both modified regions now to catch any local coherence issue, especially accidental duplication or notation drift from the `\Theta_\cA^{\Eone}` introduction.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2088,2096p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '366,381p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   366	
   367	\medskip\noindent
   368	All five theorems are $\Sigma_n$-coinvariant projections of a single
   369	$E_1$ object.
   370	The ordered bar differential $D_\cA^{\Eone}$ on
   371	$\barB^{\mathrm{ord}}(\cA)$ defines
   372	$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
   373	\in \MC({\gAmod}^{\Eone})$
   374	(Theorem~\ref{thm:e1-mc-element}); since
   375	$(D_\cA^{\Eone})^2 = 0$, the MC equation
   376	$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
   377	is automatic. Averaging into~$\gAmod$ produces the modular
   378	Maurer--Cartan element $\Theta_\cA$ of
   379	Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
   380	structural properties of this projection.
   381	\emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 succeeded in 52ms:
  2088	
  2089	\noindent\textbf{MC4} ($\mathcal{W}_\infty$ closure and completed bar-cobar): The completed bar-cobar problem asks whether finite-stage Koszul duality passes to inverse limits. Two complementary mechanisms cover the entire standard landscape:
  2090	
  2091	\smallskip
  2092	\noindent\emph{Mechanism~1: strong filtration.}
  2093	If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
  2094	If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
  2095	
  2096	\smallskip
exec
/bin/zsh -lc "rg -n \"Theta_\\\\cA\\"'^'"\\{\\\\Eone\\}|Theorem~\\\\ref\\{thm:e1-mc-element\\}|not on the uncompleted direct sums|weight-completed tower\" chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Theta_\cA\^\{\Eone\}|Theorem~\ref\{thm:e1-mc-element\}|not on the uncompleted direct sums|weight-completed tower)
             ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..56cc53981f3e4934c3a733353d3bc5aa2018b549
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2090,6 +2091,7 @@
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
 If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}


thinking
**Fixing duplicates and errors**

I see there's duplication between lines 2093 and 2094, so I need to remove that old duplicate sentence. The "rg error" seems harmless, but I still need to patch it by removing line 2093, which is the old version. I plan to patch the second hunk to eliminate the duplicate long sentence. I’m considering running a search with a fixed string, but maybe that’s not necessary. Anyway, I’ll just proceed with the patch!
codex
I hit a local duplication in the MC4 paragraph from the patch context. I’m removing the stale pre-edit sentence and then re-running a tight reread of both regions.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2092,3 +2092,2 @@
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
 If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '368,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2090,2096p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   368	All five theorems are $\Sigma_n$-coinvariant projections of a single
   369	$E_1$ object.
   370	The ordered bar differential $D_\cA^{\Eone}$ on
   371	$\barB^{\mathrm{ord}}(\cA)$ defines
   372	$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
   373	\in \MC({\gAmod}^{\Eone})$
   374	(Theorem~\ref{thm:e1-mc-element}); since
   375	$(D_\cA^{\Eone})^2 = 0$, the MC equation
   376	$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
   377	is automatic. Averaging into~$\gAmod$ produces the modular
   378	Maurer--Cartan element $\Theta_\cA$ of
   379	Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
   380	structural properties of this projection.
 succeeded in 52ms:
  2090	
  2091	\smallskip
  2092	\noindent\emph{Mechanism~1: strong filtration.}
  2093	If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
  2094	
  2095	\smallskip
  2096	\noindent\emph{Mechanism~2: weight cutoff.}
exec
/bin/zsh -lc "grep -nF \"Theorem~\\\\ref{thm:e1-mc-element}\" chapters/theory/introduction.tex && grep -nF \"Theorem~\\\\ref{thm:mc2-bar-intrinsic}\" chapters/theory/introduction.tex | head -n 20 && grep -nF \"not on the uncompleted direct sums\" chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
374:(Theorem~\ref{thm:e1-mc-element}); since
1270:(Theorem~\ref{thm:e1-mc-element}):
1373:(Theorem~\ref{thm:e1-mc-element}).
108:(Theorem~\ref{thm:mc2-bar-intrinsic}).
379:Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
571: (Theorem~\ref{thm:mc2-bar-intrinsic}).
1802: proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
1998:(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
2083:\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
2265:in Theorem~\ref{thm:mc2-bar-intrinsic}. Every chapter either
2093:If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

codex
The two target paragraphs now read correctly. I’m doing one last dependency check on the referenced labels and a diff pass so the close-out is based on the actual post-edit surface.
exec
/bin/zsh -lc 'git diff -- chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba..09d52f0 100644
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@ All five theorems are $\Sigma_n$-coinvariant projections of a single
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
exec
/bin/zsh -lc "grep -nF '\\label{thm:e1-mc-element}' chapters/theory/e1_modular_koszul.tex && grep -nF '\\label{thm:mc2-bar-intrinsic}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/* chapters/theory/*.tex | head -n 20 && grep -nF '\\label{prop:standard-strong-filtration}' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
chapters/theory/higher_genus_modular_koszul.tex:3707:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:3707:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:3707:\label{thm:mc2-bar-intrinsic}
1093:\label{prop:standard-strong-filtration}
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}




thinking
**Considering LaTeX compilation options**

I'm thinking about running `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, although it might be heavy. Alternatively, I'm wondering if I can compile just the introduction, but that seems impossible. I could check for unmatched braces using `python`, but I'm not sure that's allowed. Maybe using `grep` or `rg` might help too, but I have to consider the complexity. It might be wise to run `latexmk` quietly and test thoroughly, even if it takes time.
thinking
**Evaluating the need for build verification**

I'm considering whether a build is necessary. If we decide to go ahead with it, then the skill would clearly apply. However, since the user hasn't mentioned the skill and the task doesn't necessitate a build, I'm pondering if we really need to run it. The phrase "strongest local verification available" indicates it might be useful. Still, I need to decide if it's worth it, and maybe we can manage without it after all.
thinking
**Updating and searching for issues**

I'm thinking I should search for syntax errors first since it might be easier. Actually, since the patches are simple and don’t use labels, compiling might be unnecessary. However, confirming that "all \ref and \label are valid" could be done with grep, which is good to know. Hmm, it seems I need to update my plan now that this step is completed. Let’s proceed with updating the plan!
Plan update
The introduction patch is in place and the touched references were re-checked against their defining labels. I verified the two modified regions in context and confirmed the cited labels exist.
  ✓ Audit the targeted introduction passages against the cited theorem/proposition surfaces
  ✓ Patch `chapters/theory/introduction.tex` to separate the ordered `E_1` citation from the averaged modular citation and to make the MC4 weight-completion hypothesis explicit
  ✓ Re-read the modified sections and verify labels/status coherence on the touched surface
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

codex
Edited [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:368). I re-read the two modified regions in context and checked that `thm:e1-mc-element`, `thm:mc2-bar-intrinsic`, and `prop:standard-strong-filtration` all exist. I did not run a full TeX build.

## Rectification Summary
- [FIXED] finding 1 — at [introduction.tex:368](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:368), I separated the ordered and modular statements explicitly: the ordered class is now written as `\Theta_\cA^{\Eone}` and cited to `thm:e1-mc-element`, and the next sentence states that averaging produces the modular Maurer--Cartan element of `thm:mc2-bar-intrinsic`.
- [FIXED] finding 2 — at [introduction.tex:2093](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2093), I tightened the MC4 advertisement so it now says the strong-filtration mechanism applies only after passing to the weight-completed tower, and that the standard-family MC4 statements are on weight completions, not on the uncompleted direct sums.
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 7ed99ba50885c00465bac7088d23b6ae5bc9e0a7..09d52f098f37ba5985a0c5054d2f4138c72031dc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -369,13 +369,14 @@
 $E_1$ object.
 The ordered bar differential $D_\cA^{\Eone}$ on
 $\barB^{\mathrm{ord}}(\cA)$ defines
-$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
+$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
 \in \MC({\gAmod}^{\Eone})$
 (Theorem~\ref{thm:e1-mc-element}); since
 $(D_\cA^{\Eone})^2 = 0$, the MC equation
-$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
-is automatic. Averaging into~$\gAmod$ produces the
-$\Sigma_n$-invariant content: the five theorems characterize five
+$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
+is automatic. Averaging into~$\gAmod$ produces the modular
+Maurer--Cartan element $\Theta_\cA$ of
+Theorem~\ref{thm:mc2-bar-intrinsic}; the five theorems characterize five
 structural properties of this projection.
 \emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
 \emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
@@ -2089,7 +2090,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$; accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions.
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). For the standard graded families of Proposition~\ref{prop:standard-strong-filtration}, this strong-filtration mechanism applies only after passage to the weight-completed tower: the inverse-limit object is the weight completion $\widehat{\cA}^{\mathrm{wt}}$ rather than the direct sum~$\cA$. Accordingly, the MC4 statement for $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), and lattice algebras is formulated on their weight completions, not on the uncompleted direct sums.
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}

tokens used
139,012
