# R22_bar_construction (185s)

In [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:84) I made the local convention explicit: throughout this chapter, `\barB_X(\cA)` now means the symmetric factorization bar on unordered `\operatorname{Ran}(X)`, while the ordered bar is always written `B^{\mathrm{ord}}_X(\cA)`.

I also added a remark immediately after the Verdier formula in [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:106) stating that Theorem A is only the symmetric-bar statement on `\operatorname{Ran}(X)`, that `\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)` is not part of the theorem, and that one must first pass to the `\Sigma_n`-coinvariant quotient `\barB_X(\cA)`. I re-read the modified block for coherence; no theorem-status tags changed, and no new `\label` or `\ref` were introduced. I did not run a full TeX build.

## Rectification Summary
- [FIXED] T01 — strengthened the convention so the file explicitly reserves unqualified `\barB_X(\cA)` for the symmetric bar on unordered `\operatorname{Ran}(X)`, with `B^{\mathrm{ord}}_X(\cA)` kept distinct for the ordered bar.
- [FIXED] T01 — added a new remark fencing Theorem A’s Verdier statement to the symmetric Ran-space bar and explicitly ruling out reading it as a Verdier statement for the ordered bar.


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
session id: 019d83b7-6678-7e63-b435-9f678b40e1e8
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


TARGET: chapters/theory/bar_construction.tex

FINDINGS TO FIX:

1. [MEDIUM T01] Lines ~80-105: Convention that unqualified bar B means symmetric B^Sigma.
   This convention is load-bearing for Theorem A (which only works on symmetric bar).
   FIX: Verify this convention is clearly stated and consistent. Add a remark that
   Theorem A's Verdier statement requires the symmetric bar on unordered Ran(X),
   and that bar B^ord on the ordered surface does not support D_Ran.

Read the file, verify the convention, strengthen the clarity.
mcp startup: no servers


thinking
**Considering codebase exploration**

The guidelines indicate that explorers are the go-to for codebase questions, and I should trust their results without needing verification. So, I’m thinking I should definitely use explorers for these queries, but I still have the capability to read specific files and summarize things myself. It might be best to spawn an explorer agent to check out the relevant files. I wonder if it’s acceptable to delegate reading to the explorer alongside my own readings.
thinking
**Reviewing editing procedures**

I need to open the SKILL.md file, perhaps using tools like shell cat or sed. If there isn't a build, maybe I won't need build-surface. I should think about using update_plan after gathering enough context and provide regular commentary updates. When editing, I'll focus on specific files using apply_patch and remember to check surrounding context after each edit. It's essential to include a Rectification Summary with statuses and address the Pre-Edit Verification Protocol as well. I also need to mention skill usage concisely.
codex
Using `beilinson-rectify` because this is a local mathematical rectification in [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex). I’m reading the required constitutional surfaces plus the target section now, then I’ll tighten the bar-convention statement with the minimum truthful edit.
exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
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

 succeeded in 53ms:
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
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.

thinking
**Clarifying theorem applicability**

I need to make a remark after the Verdier statement, specifying that D_Ran is defined on Ran and applies to \barB_X. It’s important to clarify that this doesn’t pertain to B^{ord}, which operates on ordered FM/configuration. This is managed through linear dual/coinvariants prior to Verdier. I might also consider strengthening the clarity of theorem A to make everything easier to follow.
codex
I’ve got the local surface. The file already distinguishes `B^{\mathrm{ord}}_X(\cA)` from `\barB_X(\cA)`, but the Verdier sentence is too compressed: it doesn’t explicitly say that Theorem A is a statement on unordered `\operatorname{Ran}(X)` and therefore cannot be read as a statement about the ordered bar.
exec
/bin/zsh -lc "rg -n \"thm:bar-cobar-isomorphism-main|Verdier|barB_X|B\\"'^'"\\{\\\\mathrm\\{ord\\}\\}|B\\\\"'^'"\\{ord\\}\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:bar-cobar-isomorphism-main|Verdier intertwining|bar-cobar adjunction|unordered Ran|Ran\\(X\\)\" chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:thm:bar-cobar-isomorphism-main|Verdier|barB_X|B\^\{\mathrm\{ord\}\}|B\^\{ord\})
                                                          ^^
error: unrecognized escape sequence
 succeeded in 94ms:
chapters/theory/bar_construction.tex:34:on $\Ran(X)$ is its $\Sigma_n$-coinvariant quotient, the
chapters/theory/bar_construction.tex:99:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
chapters/theory/bar_construction.tex:142:and the bar-cobar adjunction is the pair
chapters/theory/bar_construction.tex:1401:Bar degree~$n$ uses sections over $C_{n+1}(X)$; the bar differential lowers bar degree. The \emph{reduced} bar complex, used from \S\ref{subsec:bar-functoriality} onward and throughout the monograph, replaces $\mathcal{A}$ by its augmentation ideal $\bar{\mathcal{A}} = \ker(\varepsilon \colon \mathcal{A} \to \omega_X)$ and starts at $\bar{B}^0 = \mathbb{C}$. Augmentation separates generators from scalars: the map~$\varepsilon$ extracts the component of each operator proportional to the identity (the vacuum expectation value), and the reduced complex $T^c(s^{-1}\bar{\mathcal{A}})$ tensors together only the non-scalar modes. Without this splitting, the reduced coproduct on the bar coalgebra would fail conilpotence, and the cofree coalgebra structure that drives the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}) would be unavailable. Every theorem stated later in this chapter refers to the reduced complex $T^c(s^{-1}\bar{\mathcal{A}})$; the unreduced display above has no independent content.
chapters/theory/coderived_models.tex:7:The bar-cobar adjunction at higher genus produces curved complexes
chapters/theory/coderived_models.tex:150:\index{bar-cobar adjunction!coderived formulation}
chapters/theory/koszul_pair_structure.tex:29:convolution algebra on $\Ran(X)$
chapters/theory/koszul_pair_structure.tex:80:(Theorem~A, Theorem~\ref{thm:bar-cobar-isomorphism-main}). The genus-$0$ collision differential $\dzero$ still satisfies
chapters/theory/koszul_pair_structure.tex:116: (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/theory/koszul_pair_structure.tex:396:The Jacobi identity follows from the identification of $\{-,-\}_c$ with the commutator of coderivations on the bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{A})$: coderivations form a Lie algebra under the commutator bracket, and the identification $\ChirHoch^*(\mathcal{A}) \cong \mathrm{Coder}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ is a standard consequence of the bar-cobar adjunction (see~\cite{LV12}, Theorem~9.3.2 for the classical case).
chapters/theory/koszul_pair_structure.tex:1844:Verdier intertwining (Theorem~A) is the statement that the
chapters/theory/chiral_modules.tex:28:Verdier intertwining (Theorem~\ref{thm:module-bar-verdier}) exchanges
chapters/theory/chiral_modules.tex:594:The Verdier intertwining
chapters/theory/chiral_modules.tex:596:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) acts at the
chapters/theory/chiral_modules.tex:603:one needs the \emph{module-level} Verdier intertwining: the functor
chapters/theory/chiral_modules.tex:617:full module-level Verdier intertwining is
chapters/theory/chiral_modules.tex:644:\begin{theorem}[Module-level Verdier intertwining; \ClaimStatusProvedHere]
chapters/theory/chiral_modules.tex:647:\index{conformal blocks!Verdier intertwining}
chapters/theory/chiral_modules.tex:2821:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/theory/chiral_modules.tex:4189:The level shift $k \leftrightarrow -k - 2h^\vee$ acts on D-modules on $G/B$ via the Feigin--Frenkel involution, exchanging $G/B$ with the Langlands dual $G^\vee/B^\vee$ at the level of opers: $\mathrm{Op}_{G^\vee}(X) \xleftrightarrow{\mathrm{FF}} Z(\widehat{\mathfrak{g}}_{-h^\vee})$. The bar-cobar adjunction mediates: $\bar{B}(\Delta_k(M)) \simeq \Delta_{k'}(M^!)$. This is the D-module incarnation of Theorem~\ref{thm:universal-kac-moody-koszul}.

thinking
**Inspecting relevant section**

I need to take a closer look at the related section in the ordered_associative_chiral_kd. It seems that there's an explicit point made around lines 855, which might be useful to mirror the language used. I’m curious about the connections that might clarify things further. I'll go ahead and check that specific part to see how it all comes together!
codex
I found an existing repository-local formulation of the exact point we need: [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex) already states that Verdier intertwining lives on `\Ran(X)` and that the naive ordered analogue is undefined. I’m pulling that wording pattern so the fix in the target file matches the live convention instead of inventing a new one.
exec
/bin/zsh -lc "sed -n '845,875p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '80,145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
If $\iota^2=\id$, then $(\iota^!)^2=\id$.
\end{corollary}

\begin{proof}
Apply Theorem~\ref{thm:opposite} functorially.
\end{proof}

\begin{remark}[Ordered Verdier duality does not exist]
\label{rem:ordered-verdier-nonexistence-opposite}
\index{Verdier duality!ordered bar|textbf}
The Verdier intertwining
$\mathbb{D}_{\Ran}\,\barBch(\cA) \simeq \barBch(\cA^!)$
\textup{(}Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}\textup{)}
is a statement about the \emph{symmetric} bar on unordered
$\Ran(X)$. The naive ordered analogue
$\mathbb{D}_{\Ran}\,\barB^{\mathrm{ord}}(\cA)$ is
\emph{undefined}: Verdier duality on $\Ran(X)$ requires
the cosheaf/factorization property, which uses the
\emph{symmetric} monoidal structure on disjoint-open covers.
The ordered bar lives on $\mathrm{Conf}^<_n(X)$ (ordered
 succeeded in 51ms:
    80	\begin{convention}[Bar coalgebra and Koszul dual algebra]
    81	\label{conv:bar-coalgebra-identity}
    82	\index{bar construction!as Koszul dual coalgebra|textbf}
    83	\index{Koszul dual!coalgebra vs.\ algebra|textbf}
    84	The bar construction $\barB_X(\cA)$ of an augmented chiral
    85	algebra~$\cA$ is a dg factorization \emph{coalgebra} on
    86	$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
    87	of~$\cA$: the bar complex is not a tool for computing the dual,
    88	it \emph{is} the dual.
    89	
    90	When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
    91	in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
    92	separate object: it has generators $\mathcal{V}^\vee =
    93	\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
    94	($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
    95	relations~$R^\perp$ (orthogonal complement under the residue
    96	pairing). In the classical setting (algebras on a point),
    97	$\cA^!$ is the graded linear dual of the concentrated bar
    98	coalgebra. In the chiral setting, $\cA^!$ is characterized by
    99	Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):

thinking
**Inspecting theorem statements**

I think I need to look closely at Theorem A within chiral_koszul_pairs or higher_genus_foundations to check the exact wording. The user has targeted a specific file, but it sounds like they can still read it. By inspecting the theorem statement, I might be able to confirm its symmetry. It seems like an important step to make sure everything is aligned properly!
codex
The local fix should explicitly line up with the actual theorem statement, not just with nearby prose. I’m checking the proved Theorem A surface so the remark says exactly what that theorem proves and nothing stronger.
exec
/bin/zsh -lc "sed -n '2544,2588p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3639,3715p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Summary of Theorem~A; see Theorem~\ref{thm:bar-cobar-isomorphism-main}]
\label{rem:theorem-a-summary}
The genus-zero bar-cobar duality
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Chapter~\ref{chap:koszul-pairs}) establishes:
for a chiral Koszul pair $(\cA_1, \cA_2)$
(Definition~\ref{def:chiral-koszul-pair}),
the unit and counit of the bar-cobar adjunction are
quasi-isomorphisms, and the bar functor is intertwined
with Verdier duality on $\operatorname{Ran}(X)$.
The counit is a quasi-isomorphism \emph{only on the
Koszul locus}; off this locus it persists in the completed
coderived category.
\end{remark}

% The following theorem block is retained only to preserve the local
% equation labels used in this chapter. The canonical statement and proof
% are in chiral_koszul_pairs.tex.
\begin{theorem}[Bar-cobar isomorphism, retained for equation labels; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main-equations}
 succeeded in 50ms:
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
The equivalences below hold in the derived category
$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
factorization algebras on~$X$.

\smallskip\noindent
The Heisenberg instance was verified in~\S\ref{sec:frame-inversion}.
In general:

Let $(\cA_1, \cC_1, \tau_1, F_\bullet)$ and
$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
Then:
\begin{enumerate}
\item the canonical units and counits are quasi-isomorphisms:
\[

thinking
**Considering ordered analogues**

I could mention that the correct ordered analogue is something like linear duality or perhaps the passage to coinvariants. I wonder how these concepts interrelate and if they have more implications beyond the basic definitions. Additionally, I’ll think about how these ideas might apply in different contexts. It seems like there’s a lot to unpack, and I'd like to make sure I'm fully grasping the nuances to provide the best response!
codex
I’m doing one more consistency pass through the target file before patching. The aim is to make the local notation explicit without fighting the rest of the chapter’s `B^{\mathrm{ord}}` versus `\barB_X` usage.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"D_\\\\operatorname\\{Ran\\}|\\\\mathbb\\{D\\}_\\\\operatorname\\{Ran\\}|Verdier|bar complex|ordered bar|Ran\\"'^'"\\{ord\\}|Conf\\"'^<|'"\\\\barB_X|B\\"'^'"\\{\\\\mathrm\\{ord\\}\\}_X\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.
 exited 2 in 51ms:
rg: regex parse error:
    (?:D_\operatorname\{Ran\}|\mathbb\{D\}_\operatorname\{Ran\}|Verdier|bar complex|ordered bar|Ran\^\{ord\}|Conf\^<|\barB_X|B\^\{\mathrm\{ord\}\}_X)
         ^^
error: unrecognized escape sequence

thinking
**Considering a plan update**

I’m thinking about how to respond more clearly by adding a remark about the abstract operadic level. It might help to mention the universal coalgebra and the notation involved. However, the user only asked for specific findings, which makes me wonder if I even need to change my approach. Maybe using the update_plan tool to track my steps could help, so I’ll create a brief plan with three steps for clarity.
Plan update
Local rectification in a single theorem-preparatory convention block. I’ve read the required constitutional surfaces and the nearby theorem statements; next is a narrow patch plus re-read/verification.
  ✓ Audit the target convention block against Theorem A and existing ordered/symmetric bar usage
  → Patch chapters/theory/bar_construction.tex to state the local bar convention and exclude ordered Verdier duality
  • Re-read the modified section and verify the finding is resolved with no label/reference drift
codex
```text
PE-4: bar complex formula
object: B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA), with \barB_X(\cA) its \Sigma_n-coinvariant factorization quotient on \operatorname{Ran}(X)
T^c argument: [s^{-1} \bar\cA? Y]  AP132: augmentation? [Y]
AP22: |s^{-1}v| = |v| [-1] (must be -1)
s^{-1} not bare s? [Y]
coproduct: [deconcatenation / symmetric coinvariant quotient]
match to intended bar: [B^ord→deconc / \barB_X→factorization quotient on \operatorname{Ran}(X)]
grading: cohomological |d|=+1? [Y]
verdict: ACCEPT
```



thinking
**Editing patch carefully**

I need to edit the file thoughtfully. I'm thinking of inserting a paragraph after the equation and before the remark about Volume II. It might also help to modify the initial sentence a bit. The goal is to create a minimal yet truthful edit. 

I'll include a detailed clarification about the bar construction and how it relates to both unordered and ordered structures, while making it clear how theorem applications differ between the two. This way, I ensure precision in the context.
thinking
**Clarifying notation in comparisons**

To compare the ordered bar with Theorem A, I first need to reference the \(\Sigma_n\)-coinvariant quotient \(\barB_X(\cA)\). The ordered bar is usually treated separately through linear duality or the \(\Eone\) opposite-coalgebra formalism.

I should check if \(\operatorname{Ran}^{\mathrm{ord}}(X)\) is defined. To keep things simple, using "ordered configuration spaces" might be a better choice to avoid introducing new notation. Referring to "ordered configuration surfaces" could work, but I need to ensure clarity regarding the factors involved. I’d like to keep this minimal and accurate.
thinking
**Patching document remarks**

It looks like I can add another remark within the convention of the file, which seems accepted. I could structure it as `\begin{remark}[Verdier side of TheoremA]`. I want to avoid any labels for cross-volume uniqueness, and I'll make sure to use the `apply_patch` method only. Let's get started on patching this! It’s good to confirm the format before proceeding.
codex
I’m patching only the convention block in [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex). The edit will do two things: make the local `\barB_X` convention explicit, and insert a remark that fences Theorem A’s Verdier statement to the symmetric bar on unordered `\operatorname{Ran}(X)`.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -85,3 +85,3 @@
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
@@ -105,2 +105,15 @@
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..5c230937a8b8e25bad53aa7d1ad447253587de86
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,19 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..5c230937a8b8e25bad53aa7d1ad447253587de86
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,19 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

codex
The patch is in. I’m re-reading the modified block now to verify the convention is explicit, the Verdier restriction is fenced to the symmetric bar, and I haven’t introduced any local LaTeX or reference drift.
exec
/bin/zsh -lc "rg -n \"unqualified notation \\\\barB_X|Verdier side of Theorem~A|mathbb\\{D\\}_\\{\\\\operatorname\\{Ran\\}\\}.*B\\"'^'"\\{\\\\mathrm\\{ord\\}\\}\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '80,132p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:unqualified notation \barB_X|Verdier side of Theorem~A|mathbb\{D\}_\{\operatorname\{Ran\}\}.*B\^\{\mathrm\{ord\}\})
                                                                            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
    80	\begin{convention}[Bar coalgebra and Koszul dual algebra]
    81	\label{conv:bar-coalgebra-identity}
    82	\index{bar construction!as Koszul dual coalgebra|textbf}
    83	\index{Koszul dual!coalgebra vs.\ algebra|textbf}
    84	The bar construction $\barB_X(\cA)$ of an augmented chiral
    85	algebra~$\cA$ is a dg factorization \emph{coalgebra} on
    86	$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
    87	of~$\cA$: the bar complex is not a tool for computing the dual,
    88	it \emph{is} the dual.
    89	
    90	When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
    91	in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
    92	separate object: it has generators $\mathcal{V}^\vee =
    93	\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
    94	($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
    95	relations~$R^\perp$ (orthogonal complement under the residue
    96	pairing). In the classical setting (algebras on a point),
    97	$\cA^!$ is the graded linear dual of the concentrated bar
    98	coalgebra. In the chiral setting, $\cA^!$ is characterized by
    99	Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..5c230937a8b8e25bad53aa7d1ad447253587de86
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,19 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on



thinking
**Considering code readability**

I'm thinking about whether I really need fixed strings or not. I might want to do a quick search for references to see if anything's missing. I could run some commands to check the text. Also, it seems like line 86 is quite long, which isn't ideal for readability. I could consider breaking it into smaller parts, although it might not be necessary. It's essential to verify that there are no new inconsistencies in the remarks.
thinking
**Clarifying the expression**

I see that the current line indicates that it doesn't carry the required datum for the Verdier intertwining, which is good. It might be more powerful to say that "the expression \(\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)\) is not part of the theory." Including a direct reference to "does not support \(\mathbb{D}_{\operatorname{Ran}}\)" could enhance clarity. I could adjust the remark to make that explicit, especially between lines 109-112. This change would help address the user's request effectively.
codex
One sentence is still worth tightening: I want the file to say outright that `\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)` is not a valid theorem-level expression here, rather than leaving that as an implication.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -112,2 +112,4 @@
 factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
 the ordered bar lives on ordered configuration spaces and does not
apply_patch(auto_approved=true) exited 0 in 53ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..df0d23faf96ba6ed9239ab6996b20ea5ac0b33f3
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..df0d23faf96ba6ed9239ab6996b20ea5ac0b33f3
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

exec
/bin/zsh -lc "rg -n --fixed-strings \"\\begin{remark}[Verdier side of Theorem~A]\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '84,121p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
106:\begin{remark}[Verdier side of Theorem~A]
 succeeded in 51ms:
    84	The bar construction $\barB_X(\cA)$ of an augmented chiral
    85	algebra~$\cA$ is a dg factorization \emph{coalgebra} on
    86	$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
    87	of~$\cA$: the bar complex is not a tool for computing the dual,
    88	it \emph{is} the dual.
    89	
    90	When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
    91	in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
    92	separate object: it has generators $\mathcal{V}^\vee =
    93	\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
    94	($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
    95	relations~$R^\perp$ (orthogonal complement under the residue
    96	pairing). In the classical setting (algebras on a point),
    97	$\cA^!$ is the graded linear dual of the concentrated bar
    98	coalgebra. In the chiral setting, $\cA^!$ is characterized by
    99	Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
   100	Verdier duality on $\operatorname{Ran}(X)$ sends the bar
   101	\emph{coalgebra} to the homotopy Koszul dual \emph{algebra},
   102	\[
   103	\mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..df0d23faf96ba6ed9239ab6996b20ea5ac0b33f3
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+the ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on


thinking
**Fixing formatting issues**

I noticed a little mistake: the text starting with "the ordered bar lives..." should begin with a capital letter since it follows a period. It looks like the previous sentence ended with a full stop, so that needs fixing to "The ordered bar..." I'm also contemplating if the long line is still okay, but it seems like I should just proceed with the patch to make everything right. Let's get that sorted out!
codex
A small coherence fix is still needed in the new remark: one sentence boundary became a lowercase start after the insertion. I’m cleaning that and then closing verification.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -114,3 +114,3 @@
 is therefore not part of the theorem.
-the ordered bar lives on ordered configuration spaces and does not
+The ordered bar lives on ordered configuration spaces and does not
 itself carry the symmetric factorization datum required for this
apply_patch(auto_approved=true) exited 0 in 54ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..4380d797f695cc4da62f2bbe7678b65931aa2d63
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+The ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..4380d797f695cc4da62f2bbe7678b65931aa2d63
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+The ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '84,121p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    84	The bar construction $\barB_X(\cA)$ of an augmented chiral
    85	algebra~$\cA$ is a dg factorization \emph{coalgebra} on
    86	$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
    87	of~$\cA$: the bar complex is not a tool for computing the dual,
    88	it \emph{is} the dual.
    89	
    90	When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
    91	in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
    92	separate object: it has generators $\mathcal{V}^\vee =
    93	\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
    94	($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
    95	relations~$R^\perp$ (orthogonal complement under the residue
    96	pairing). In the classical setting (algebras on a point),
    97	$\cA^!$ is the graded linear dual of the concentrated bar
    98	coalgebra. In the chiral setting, $\cA^!$ is characterized by
    99	Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
   100	Verdier duality on $\operatorname{Ran}(X)$ sends the bar
   101	\emph{coalgebra} to the homotopy Koszul dual \emph{algebra},
   102	\[
   103	\mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 succeeded in 51ms:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a773..4380d79 100644
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@ Throughout this chapter: collision divisors are $D_{ij}$ with $i < j$ (indices i
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@ Verdier duality on $\operatorname{Ran}(X)$ sends the bar
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..4380d797f695cc4da62f2bbe7678b65931aa2d63
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+The ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

Plan update
The convention block now explicitly fixes the local meaning of \barB_X and fences Theorem A’s Verdier statement to the symmetric Ran-space bar. I re-read the modified lines and confirmed there are no new labels or changed references.
  ✓ Audit the target convention block against Theorem A and existing ordered/symmetric bar usage
  ✓ Patch chapters/theory/bar_construction.tex to state the local bar convention and exclude ordered Verdier duality
  ✓ Re-read the modified section and verify the finding is resolved with no label/reference drift
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..4380d797f695cc4da62f2bbe7678b65931aa2d63
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+The ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

codex
In [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:84) I made the local convention explicit: throughout this chapter, `\barB_X(\cA)` now means the symmetric factorization bar on unordered `\operatorname{Ran}(X)`, while the ordered bar is always written `B^{\mathrm{ord}}_X(\cA)`.

I also added a remark immediately after the Verdier formula in [chapters/theory/bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:106) stating that Theorem A is only the symmetric-bar statement on `\operatorname{Ran}(X)`, that `\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)` is not part of the theorem, and that one must first pass to the `\Sigma_n`-coinvariant quotient `\barB_X(\cA)`. I re-read the modified block for coherence; no theorem-status tags changed, and no new `\label` or `\ref` were introduced. I did not run a full TeX build.

## Rectification Summary
- [FIXED] T01 — strengthened the convention so the file explicitly reserves unqualified `\barB_X(\cA)` for the symmetric bar on unordered `\operatorname{Ran}(X)`, with `B^{\mathrm{ord}}_X(\cA)` kept distinct for the ordered bar.
- [FIXED] T01 — added a new remark fencing Theorem A’s Verdier statement to the symmetric Ran-space bar and explicitly ruling out reading it as a Verdier statement for the ordered bar.
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index a55a77331d3eabf3af374f193c52a5139568083d..4380d797f695cc4da62f2bbe7678b65931aa2d63
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -83,7 +83,7 @@
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. It is the Koszul dual \emph{coalgebra}
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
 of~$\cA$: the bar complex is not a tool for computing the dual,
 it \emph{is} the dual.
 
@@ -103,6 +103,21 @@
 \mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
 \;\simeq\; \cA^!_\infty,
 \]
+\begin{remark}[Verdier side of Theorem~A]
+Theorem~A is a statement about the symmetric bar
+$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
+It is not a statement about the ordered bar
+$B^{\mathrm{ord}}_X(\cA)$.
+The functor $\mathbb{D}_{\operatorname{Ran}}$ is defined on
+factorization $\mathcal{D}$-modules on $\operatorname{Ran}(X)$;
+the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
+is therefore not part of the theorem.
+The ordered bar lives on ordered configuration spaces and does not
+itself carry the symmetric factorization datum required for this
+Verdier intertwining.
+To compare the ordered bar with Theorem~A, one must first pass to
+its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
+\end{remark}
 \begin{remark}[Volume~II notation]
 In Volume~II, the Koszul dual splits into two components:
 $\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on

tokens used
69,268
