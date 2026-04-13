# R01_chiral_koszul_pairs (491s)

Edited [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex). Theorem A now cleanly separates coalgebra-side unit equivalences from algebra-side post-Verdier identifications, the Koszul meta-theorem now marks `(vii)` as genus-0 equivalence plus uniform-weight all-genera refinement and states `(viii)` only at the proved Hochschild strength, and the SC-formality lane now explicitly uses the uniform operadic/Wick argument for all class-`G` families.

Local verification passed by re-reading the modified blocks and running `git diff --check`. A full `latexmk` run is currently blocked by an unrelated pre-existing error in [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978): undefined control sequence `\Rep`, so I could not use a full manuscript build to verify this file.

## Rectification Summary
- [FIXED] finding 1 — Theorem A now distinguishes the categories correctly: part `(1)` treats units as coalgebra equivalences and counits as algebra quasi-isomorphisms, while parts `(2)` and `(3)` are explicitly post-`\mathbb{D}_{\Ran}` factorization-algebra statements.
- [FIXED] finding 2 — The proof of Theorem A part `(2)` now states explicitly that the Verdier input is the algebra-level identification from Definition `\ref{def:chiral-koszul-pair}` / Theorem `\ref{thm:verdier-bar-cobar}`, not a coalgebra identification.
- [FIXED] finding 3 — Verified already resolved on the current surface: the proof cites `Lemma~\ref{lem:filtered-comparison-unit}` and no phantom “bar-degree analogue” citation remains.
- [FIXED] finding 4 — Condition `(vii)` is now named as genus-0 factorization homology concentration with a separate uniform-weight all-genera refinement, and the proof-web remarks now say explicitly that the unconditional equivalence uses only the genus-0 clause.
- [FIXED] finding 5 — Condition `(viii)` now states only the proved Hochschild package; the theorem and proof explicitly say no freeness of the underlying graded-commutative cup-product algebra is being claimed.
- [FIXED] finding 6 — The SC-formality lane now states on the theorem surface that the proof uses the operadic/tree-shadow/Wick argument and not any invariant-bilinear-form construction.
- [FIXED] finding 7 — The forward class-`G` implication is now stated explicitly as uniform across Heisenberg, lattice VOA, and free fermion on this file’s theorem surface.


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
session id: 019d87a6-51db-7123-a072-ab181a904b20
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


TARGET: chapters/theory/chiral_koszul_pairs.tex

FINDINGS TO FIX:

1. [CRITICAL T01] Line ~3616: Theorem A Verdier half flips between coalgebra and algebra.
   The setup defines A^!_inf as factorization ALGEBRA via D_Ran(bar B), but the theorem
   asserts bar COALGEBRA equivalences, and the proof concludes with "factorization algebra,
   not coalgebra." This violates four-functor discipline.
   FIX: Make the Verdier statement consistently about factorization ALGEBRAS (the D_Ran output).
   The bar B is a COALGEBRA; D_Ran(bar B) is an ALGEBRA. The theorem should state the
   equivalence at the algebra level after applying D_Ran. Check convention in bar_construction.tex:80-105.

2. [CRITICAL T01] Line ~584: Proof of part (2) imports Verdier compatibility as definition,
   not deriving it. The cited thm:verdier-bar-cobar identifies with factorization algebras
   in cobar_construction.tex:1347, not the coalgebra identification.
   FIX: Clarify that the Verdier identification is at the algebra (post-D_Ran) level.

3. [CRITICAL T01] Line ~416: Part (1) cites "bar-degree analogue of Lemma filtered-comparison"
   which does not exist anywhere in the repo.
   FIX: Either write this lemma or cite the correct existing result.

4. [CRITICAL T13] Line ~1998-2004: Koszul equiv (vii) is listed as unconditional but proof
   scopes it to g=0 only. All-genera version is strictly stronger.
   FIX: Move (vii) to the conditional equivalences, or add the all-genera proof.

5. [CRITICAL T13] Line ~2005-2008: Koszul equiv (viii) mis-stated. Cited Hochschild theorems
   prove duality and concentration, not free polynomial algebra. (viii)=>(v) uses unproved claim.
   FIX: Weaken (viii) to match what's actually proved, or prove the stronger statement.

6. [CRITICAL T15] Line ~2539: SC-formality converse proof uses bilinear form C(x,y,z)=kappa(x,[y,z])
   but kappa is scalar, not bilinear. Also not valid for betagamma (no metric).
   FIX: Restrict the proof to families with invariant bilinear form, or find a different proof.

7. [CRITICAL T15] Line ~2532: Forward implication only proved for Heisenberg, not full class G.
   Lattice VOA class assignment contradicts between tables.
   FIX: Resolve the class-G membership for lattice VOAs consistently and prove forward for all class G.

Read the file, verify each finding, make the strongest truthful fix for each.
mcp startup: no servers


thinking
**Planning file updates**

I need to start with a commentary update before diving into the substantial work. Maybe using an update_plan is the right approach since the work is substantial. I'll provide some commentary with my understanding as the first step. Then, I should utilize parallel tools for reading required files concurrently. I think an explorer agent could be used to locate findings quickly. However, I also need to read files myself, as it's a repo question. Exploring could help me reference faster, but it may be overkill.
thinking
**Utilizing explorer agents**

I should always prefer explorer agents over manual searches or file reading. It makes sense to spawn them to search the codebase for relevant lemmas and theorems. I need to be careful about this approach. I could have one explorer focus on theorem labels and references while still using shell reads for direct context. Perhaps I should use an explorer to locate the bar_construction convention and identify the missing lemma. Utilizing two explorers in parallel sounds useful!
codex
Using `beilinson-rectify` for this theorem-surface repair. I’m reading the required constitutional files plus the target theorem context, and I’m separately checking the cited dependencies for the Verdier convention, the missing filtered lemma, and the class-G/SC-formality surface before I edit.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

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

exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
codex
I have the constitutional surface loaded. Next I’m reading the exact theorem blocks around each finding, plus the cited dependency lanes in `bar_construction.tex` and `cobar_construction.tex`, to determine whether each fix can be strengthened or must be narrowed.
exec
/bin/zsh -lc 'rg -n "filtered-comparison|Verdier|Koszul equiv|SC-formality|class G|lattice" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2480,2595p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '360,700p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1880,2065p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3570,3665p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1320,1375p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '70,120p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "filtered-comparison|complete-filtered-comparison|bar-degree analogue|Lemma filtered-comparison|thm:verdier-bar-cobar|class G|SC-formal|lattice VOA|lattice vertex|Heisenberg" chapters/theory chapters/examples chapters/frame | head -n 300' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
\item \emph{Non-principal $\mathcal{W}$-algebras at wild nilpotent type.}
 Quantum Drinfeld--Sokolov reduction at a nilpotent $e$ whose
 associated Slodowy slice has wild representation type produces
 a $\mathcal{W}$-algebra whose Ext quiver has $m \geq 3$ arrows;
 the resulting bar complex inherits the wild root structure.
\end{enumerate}
The replacement for the shadow obstruction tower in
class~$\mathbf{W}$ is the motivic Donaldson--Thomas theory of
Kontsevich--Soibelman: the DT invariants $\Omega(d_0, d_1)$
grow exponentially in $\max(d_0, d_1)$ for $m \geq 3$, and
their wall-crossing structure encodes the information that the
shadow tower would carry in the Koszul world
(Remark~\ref{rem:wild-quiver-boundary}).
\end{remark}

\subsubsection{Koszulness from Sklyanin Poisson cohomology}
\label{subsubsec:sklyanin-poisson-koszulness}
\index{Koszul property!Sklyanin Poisson rigidity}
\index{Poisson cohomology!Sklyanin bracket}
 succeeded in 52ms:
\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(xi)}:
On the Koszul locus, the bar-cobar adjunction provides a free
resolution, and the complementarity splitting
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
\simeq H^*(\overline{\cM}_g, \cZ_\cA)$
(Theorem~C) identifies $\cM_\cA$ and $\cM_{\cA^!}$ as
complementary subspaces of $\cM_{\mathrm{comp}}$. The
shifted-symplectic structure
(Theorem~\ref{thm:ambient-complementarity-fmp})
makes these subspaces isotropic; the complementarity splitting
gives maximal dimension, hence Lagrangian.

\smallskip\noindent
\textup{(xi)}$\Rightarrow$\textup{(i)}:
If $\cM_\cA$ and $\cM_{\cA^!}$ are transverse Lagrangians,
their derived intersection
$\cM_\cA \times^h_{\cM_{\mathrm{comp}}} \cM_{\cA^!}$
is discrete (transverse Lagrangian intersection in a $(-1)$-shifted
symplectic space has expected dimension~$0$). This derived
 succeeded in 52ms:
with $X_{L_k(\fg)} = \overline{\mathbb{O}}_{\min}$
\textup{(}the closure of the minimal nilpotent orbit\textup{)}.
Assume in addition that the Li associated graded is reduced:
\[
R_{L_k(\fg)}=\operatorname{gr}^F L_k(\fg)
\;\cong\;
\mathcal{O}(\overline{\mathbb{O}}_{\min})
\]
as Poisson algebras, and assume that the resulting reduced
Li--bar $E_2$ page is diagonally concentrated.
Then $L_k(\fg)$ is chirally Koszul.
\end{corollary}

\begin{proof}
This is exactly the orbit-reduction criterion of
Theorem~\ref{thm:associated-variety-koszulness}(ii)
applied to the reduced Poisson algebra
$\mathcal{O}(\overline{\mathbb{O}}_{\min})$.
\end{proof}

 succeeded in 52ms:
\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
\label{lem:filtered-comparison-unit}
\index{spectral sequence!bar-side filtered comparison}
Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
whose filtration is exhaustive, complete, and bounded below.
If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
then:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ is a classical Koszul datum;
\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
 acyclic.
\end{enumerate}
\end{lemma}

\begin{proof}
This is the unit-side analogue of
Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
 succeeded in 52ms:
51:Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
57:adjunction achieves (a) but not (b) or (c); Verdier duality alone
142:locus (Theorem~A) are proved. The Verdier intertwining that
333:\label{lem:filtered-comparison}
361:\label{lem:filtered-comparison-unit}
378:Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
467:strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
475:convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
569: dual pair, applying Verdier duality to the bar coalgebra of one side
574:$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
651:equipped with Verdier-compatible factorization-algebra
666:and Verdier compatibility can all be verified without
679:algebra-level Verdier compatibility
715:coalgebra identifies its Verdier dual factorization algebra with the
1642:$W(2)$ embeds into the lattice VOA~$V_{2\mathbb{Z}}$ as the
2694:biduality of holonomic D-modules under Verdier duality. Concretely,
2779:& Heisenberg, lattice VOA, free fermion
2805:Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
2812:lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
2841:For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
 succeeded in 50ms:
\smallskip
\noindent\textit{Notation.}
Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.

\medskip

\begin{convention}[Set notation and ordering]\label{conv:set-notation}
Throughout this chapter: collision divisors are $D_{ij}$ with $i < j$ (indices in increasing order); the hat notation $\widehat{ij}$ denotes \emph{omission} of both factors $\phi_i$ and $\phi_j$ after applying the OPE (we write $\widehat{ij}$ for the collision pattern itself, and $\widehat{\phi_i, \phi_j}$ when listing omitted terms in a tensor product).
\end{convention}

\begin{convention}[Bar coalgebra and Koszul dual algebra]
\label{conv:bar-coalgebra-identity}
\index{bar construction!as Koszul dual coalgebra|textbf}
\index{Koszul dual!coalgebra vs.\ algebra|textbf}
The bar construction $\barB_X(\cA)$ of an augmented chiral
algebra~$\cA$ is a dg factorization \emph{coalgebra} on
$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
of~$\cA$: the bar complex is not a tool for computing the dual,
it \emph{is} the dual.

 succeeded in 50ms:
Koszul dual.

Write
\[
(\mathcal{A})^!_\infty
:=
\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
\]
for the homotopy Koszul dual factorization algebra. There is a perfect pairing:
\[\langle \cdot, \cdot \rangle: \bar{B}^{\text{ch}}_n(\mathcal{A}) \otimes 
(\mathcal{A})^!_{\infty,n} \to \mathbb{C}\]

given by:
\[\langle \omega_{\text{bar}}, K_{\text{Verdier}} \rangle = \int_{\overline{C}_n(X)} 
\omega_{\text{bar}} \wedge \iota^* K_{\text{Verdier}}\]

where:
\begin{itemize}
\item $\omega_{\text{bar}} \in \Gamma(\overline{C}_n(X), \mathcal{A}^{\boxtimes n} 
\otimes \Omega^*_{\log})$ is a bar element (logarithmic form on compactified space)
 succeeded in 50ms:
chapters/frame/preface_sections10_13_draft.tex:100:For the Heisenberg algebra $\mathcal H_k$ in Swiss-cheese coordinates:
chapters/frame/preface_sections10_13_draft.tex:244:incarnation of the BV operator. For the Heisenberg PVA:
chapters/frame/preface_sections10_13_draft.tex:349:\emph{Heisenberg} (class~$\mathbf{G}$): $\cA=\mathcal H_k$,
chapters/frame/preface_sections10_13_draft.tex:425:Theorem~\ref{thm:general-hs-sewing}), and the Heisenberg one-particle
chapters/frame/preface_sections10_13_draft.tex:445:proved: Heisenberg sewing (ind-Hilbert completion, Moriwaki 2026) and
chapters/examples/deformation_quantization.tex:53:The configuration spaces here are the same ones that defined the Heisenberg bar differential (\S\ref{sec:frame-bar-deg2}), now with marked boundary points replacing interior points.
chapters/examples/deformation_quantization.tex:442:\subsection{Example 1: Heisenberg algebra}
chapters/examples/deformation_quantization.tex:1046:\subsection{Chiral star product: explicit Heisenberg computation}
chapters/examples/deformation_quantization.tex:1048:\begin{computation}[Heisenberg chiral star product through \texorpdfstring{$\hbar^3$}{3}]
chapters/examples/deformation_quantization.tex:1050:\index{Heisenberg algebra!star product}
chapters/examples/deformation_quantization.tex:1051:\index{deformation quantization!Heisenberg}
chapters/examples/deformation_quantization.tex:1053:For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
chapters/examples/deformation_quantization.tex:1081:For $a = a_{-1}|0\rangle$ (the basic Heisenberg mode):
chapters/examples/deformation_quantization.tex:1083:$\lambda$-bracket vanishes on generators because the Heisenberg
chapters/examples/deformation_quantization.tex:1087:All terms vanish for the same reason: the Heisenberg Poisson
chapters/frame/preface_sections2_4_draft.tex:121:For the Heisenberg algebra: the only OPE datum entering the bar
chapters/frame/preface_sections2_4_draft.tex:800:the Heisenberg algebra is the vertex-algebraic analogue, with
chapters/frame/guide_to_main_results.tex:102: all genera; Heisenberg sewing via Fredholm determinant.
chapters/frame/guide_to_main_results.tex:176:class~G ($r_{\max} = 2$, Heisenberg), class~L ($r_{\max} = 3$,
chapters/examples/w_algebras_deep.tex:291:Heisenberg algebra $\mathcal{H}^{\otimes 2}$ (two free bosons $\phi_1, \phi_2$
codex
The first pass shows two separate problems on the Theorem A surface: the file already knows the Verdier output is an algebra after `\mathbb{D}_{\operatorname{Ran}}`, but the theorem statement and proof still slip back into coalgebra language; and the missing “bar-degree analogue” is not missing anymore, because this file already has `lem:filtered-comparison-unit`, so the theorem should cite that actual lemma instead of a phantom analogue.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,4175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '400,640p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1985,2065p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2520,2985p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:verdier-bar-cobar|bar-cobar-isomorphism-main|fundamental-twisting-morphisms|ambient-complementarity-fmp|lattice-postnikov-termination|lattice:koszul-morphism|class~\\\\\\\\mathbf\\{G\\}|SC-formality\" chapters/theory chapters/examples chapters/frame | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1985	\end{tabular}
  1986	\end{center}
  1987	
  1988	\smallskip\noindent
  1989	The reduced orbit geometry can still provide useful input, but
  1990	the present theorem does not identify the reduced Li--bar
  1991	$E_2$ page with ordinary Poisson cohomology or with
  1992	$H^*(\widetilde{\mathbb{O}}, \mathcal{O}_{\widetilde{\mathbb{O}}})$
  1993	for a symplectic resolution. What it does show is that any
  1994	reduced-level diagonal-concentration statement constrains only the
  1995	reduced Li--bar page and leaves nilradical contributions as a
  1996	separate obstruction.
  1997	
  1998	A conjectural type-$A$ orbit-duality principle
  1999	\textup{(}Conjecture~\textup{\ref{conj:orbit-duality}}\textup{)}
  2000	would exchange the associated varieties of $L_k$ and~$L_{k'}$:
  2001	$\overline{\mathbb{O}} \leftrightarrow
  2002	\overline{d_{\mathrm{BV}}(\mathbb{O})}$. If that principle holds,
  2003	it imposes a \emph{compatibility constraint}: the Li--bar
  2004	obstructions for~$L_k$ and~$L_{k'}$ should be
 succeeded in 51ms:
   400	$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
   401	
   402	For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
   403	$K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
   404	equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
   405	$K_\tau^L$ by $F_\bullet$; its associated graded complex is the
   406	classical left twisted tensor product for $\operatorname{gr}_F\tau$,
   407	which is acyclic by~(a). Strong convergence then lifts this
   408	acyclicity to~$K_\tau^L$.
   409	\end{proof}
   410	
   411	\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
   412	\label{thm:fundamental-twisting-morphisms}
   413	\index{twisting morphism!fundamental theorem|textbf}
   414	\textup{[Regime: quadratic
   415	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   416	
   417	\smallskip\noindent
   418	This is the chiral analogue of \cite[Theorem~2.3.1]{LV12}.
   419	For a chiral twisting datum
 succeeded in 51ms:
  2520	\quad\text{(Ext diagonal vanishing),}\qquad
  2521	\textup{(i)} \Longleftrightarrow \textup{(vii)}
  2522	\quad\text{(factorization homology at genus~$0$),}
  2523	\]
  2524	\[
  2525	\textup{(i)} \Longleftrightarrow \textup{(ix)}
  2526	\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
  2527	\textup{(i)} \Longleftrightarrow \textup{(x)}
  2528	\quad\text{(FM boundary acyclicity),}
  2529	\]
  2530	and on the monadic side
  2531	\[
  2532	\textup{(i)} \Longleftrightarrow \textup{(vi)}
  2533	\quad\text{(Barr--Beck--Lurie monadicity).}
  2534	\]
  2535	
  2536	Three direct cross-links are the load-bearing redundancy.
  2537	
  2538	\smallskip\noindent
  2539	\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
 succeeded in 51ms:
  3600	$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
  3601	$\cA = \widehat{\fg}_k$ defines a Sklyanin--Poisson bracket on
  3602	$(\fg^!)^*$ via the Semenov-Tian-Shansky
  3603	construction~\cite{STS83}. The infinitesimal rigidity of this
  3604	bracket (vanishing of its second Poisson cohomology) turns out to
  3605	be equivalent to chiral Koszulness for the affine family.
  3606	
  3607	\begin{theorem}[Koszulness from Sklyanin--Poisson rigidity;
  3608	\ClaimStatusProvedHere{} for affine KM]
  3609	\label{thm:koszulness-from-sklyanin}
  3610	\index{Koszul property!Sklyanin Poisson rigidity|textbf}
  3611	\index{Poisson cohomology!vanishing|textbf}
  3612	\index{Whitehead's second lemma!application to Poisson rigidity}
  3613	
  3614	For $\cA = \widehat{\fg}_k$ with $\fg$ semisimple, the
  3615	Sklyanin--Poisson bracket
  3616	$\{-,-\}_{\mathrm{STS}}$ on $(\fg^!)^*$ determined by the classical
  3617	$r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$ has vanishing second
  3618	Poisson cohomology:
  3619	\[
 succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:35: Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]
chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/frame/heisenberg_frame.tex:1039:(Theorem~\ref{thm:fundamental-twisting-morphisms}):
chapters/frame/heisenberg_frame.tex:1333:(Theorem~\ref{thm:bar-cobar-isomorphism-main}):
chapters/frame/heisenberg_frame.tex:1530:(Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/frame/heisenberg_frame.tex:4575:(Theorem~\ref{thm:bar-cobar-isomorphism-main}):
chapters/examples/lattice_foundations.tex:927:The bar-cobar QI follows from Theorem~\ref{thm:lattice:koszul-morphism}: the twisting morphism $\tau$ is Koszul, so $\Omega^{\mathrm{ch}}(\barBgeom(\Vlat_\Lambda)) \xrightarrow{\sim} \Vlat_\Lambda$.
chapters/examples/lattice_foundations.tex:994:\label{thm:lattice:koszul-morphism}
chapters/examples/lattice_foundations.tex:1707:(Corollary~\ref{cor:lattice-postnikov-termination}).
chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/examples/lattice_foundations.tex:3620:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is stated for any
chapters/examples/lattice_foundations.tex:3758:(Theorem~\ref{thm:lattice:koszul-morphism}) via the lattice
chapters/examples/lattice_foundations.tex:3790:Theorem~\ref{thm:lattice:koszul-morphism} applies sector by
chapters/examples/lattice_foundations.tex:4810:\label{cor:lattice-postnikov-termination}
chapters/examples/beta_gamma.tex:427:adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}), the bar
chapters/examples/landscape_census.tex:1456:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) produces the
chapters/examples/landscape_census.tex:2931:(Theorem~\ref{thm:bar-cobar-isomorphism-main}); Verdier duality
chapters/theory/higher_genus_modular_koszul.tex:516:Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}.
chapters/theory/higher_genus_modular_koszul.tex:554:\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
chapters/theory/higher_genus_modular_koszul.tex:711:MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};

thinking
**Exploring theorem conditions**

I want to dig deeper into theorem A to understand its likely minimal aspects better. I’m especially curious about conditions (vii) and (viii) since they seem important. I’ll need to read through the theorem's body, including the definitions of these conditions and the proof segments. It seems like opening the range from around 2060 to 2515 could be useful for this exploration. Let's dive into the details!
codex
I’ve isolated the remaining heavy surfaces: the Koszul meta-theorem block around items `(vii)` and `(viii)`, and the SC-formality proposition around class `G`. I’m now reading the exact statements and the proof arrows, because those are where the current status inflation sits.
exec
/bin/zsh -lc "sed -n '620,760p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1200,1295p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '360,460p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2055,2520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"main-koszul-hoch|hochschild-polynomial-growth|e2-formality-hochschild|factorization homology|uniform-weight lane|all-genera concentration|genus-0 clause of condition|class G|Gaussian locus|free fermion\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/examples/lattice_foundations.tex chapters/examples/free_fields.tex chapters/frame/preface.tex chapters/frame/heisenberg_frame.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\ChirHoch^{\bullet}(\cA)
\;\cong\;
\bigl((\cA)^!_\infty\bigr)_{\Sigma}
\;\cong\;
\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
\end{equation}
where $(-)_{\Sigma}$ denotes totalized $\Sigma_n$-coinvariants in
bar degree~$n$.
If
\[
\cA^i := H^*\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr),
\qquad
\cA^! := \mathbb{D}_X(\cA^i),
\]
then this is the corrected comparison chain
\[
\bar{B}^{\mathrm{ch}}(\cA)
\;\longrightarrow\;
\cA^i
\;\xrightarrow{\ \mathbb{D}_X\ }\;
 succeeded in 52ms:
quantum $L_\infty$-algebra forces scalar saturation, nor that
one-channelity alone implies formality. The strongest proved
input is the one-channel minimal-model statement
$\Theta_{\cA}^{\min}=\eta\otimes\Gamma_{\cA}$
\textup{(}Corollary~\textup{\ref{cor:scalar-saturation}}\textup{)};
identifying $\Gamma_{\cA}$ with
$\kappa(\cA)\Lambda$ is the open tautological-purity step outside
the proved scalar lane.

\emph{Relation to the shadow obstruction tower.}\;
The non-scalar universal classes
of~\S\ref{subsec:non-scalar-theta} measure the deviation of
$\Theta_{\cA}$ from the scalar line. The cubic shadow~$C$, quartic resonance class~$Q$,
and all higher shadows $\mathrm{Sh}_r$ are the
\emph{obstructions to formality}: the higher-order
corrections preventing $\Theta_{\cA}$ from lying on the
scalar line.

\emph{Pillar~C interaction} (Mok~\cite{Mok25}):
the planted-forest coefficient algebra $G_{\mathrm{pf}}$
 succeeded in 52ms:
cohomology sheaves
$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA))$ vanish for
$q \neq 0$ uniformly over the base, and the surviving
degree-$0$ cohomology sheaf has
finite-dimensional fibers by hypothesis~(ii). The standard
cohomology and base change theorem
(EGA~III, Th\'eor\`eme~7.7.5)
then gives that $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$ is a perfect
complex (bounded, with coherent cohomology sheaves) on
$\overline{\mathcal{M}}_g$.
\end{proof}

\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
\label{thm:fiber-center-identification}
\index{fiber--center identification|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

\smallskip\noindent
Assume $\cA$ carries a modular pre-Koszul datum
 succeeded in 52ms:
  2055	\smallskip
  2056	\noindent\textbf{Unconditional equivalences:}
  2057	\begin{enumerate}
  2058	\item[\textup{(i)}] $\cA$ is chirally Koszul
  2059	 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
  2060	\item[\textup{(ii)}] The PBW spectral sequence on
  2061	 $\barBgeom(\cA)$ collapses at $E_2$
  2062	 \textup{(}Theorem~\textup{\ref{thm:pbw-koszulness-criterion})}.
  2063	\item[\textup{(iii)}] The minimal $A_\infty$-model of
  2064	 $\barBgeom(\cA)$ is formal: $m_n = 0$ for $n \geq 3$
  2065	 \textup{(}Proposition~\textup{\ref{prop:ainfty-formality-implies-koszul}}
  2066	 and Theorem~\textup{\ref{thm:ainfty-koszul-characterization})}.
  2067	\item[\textup{(iv)}] Ext diagonal vanishing:
  2068	 $\operatorname{Ext}^{p,q}_\cA(\omega_X, \omega_X) = 0$ for
  2069	 $p \neq q$.
  2070	\item[\textup{(v)}] The bar-cobar counit
  2071	 $\Omega(\barBgeom(\cA)) \to \cA$ is a
  2072	 quasi-isomorphism
  2073	 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-inversion-qi})}.
  2074	\item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
 succeeded in 50ms:
chapters/frame/preface.tex:1436:uniform-weight lane, the obstruction class factors as
chapters/frame/preface.tex:2771: & Heisenberg $\cH_k$, free fermion\\
chapters/frame/preface.tex:3188:\subsection*{Lattice, free fermion, and the Gaussian shadow}
chapters/frame/preface.tex:3208:The free fermion $\psi$ (weight~$1/2$, OPE
chapters/frame/preface.tex:3534:proved on the uniform-weight lane and fails for multi-weight
chapters/frame/preface.tex:4410:uniform-weight lane; for multi-weight algebras at $g\ge 2$ the free
chapters/frame/heisenberg_frame.tex:195: through factorization homology, the Drinfeld--Kohno equivalence
chapters/frame/heisenberg_frame.tex:206:\textbf{H}~(Theorem~\ref{thm:hochschild-polynomial-growth}): $\mathrm{ChirHoch}^*(\mathcal{H}_k) = (\mathbb{C}, \mathbb{C}, \mathbb{C})$ concentrated in degrees $\{0, 1, 2\}$; Hilbert polynomial $P(t) = 1 + t + t^2$.
chapters/frame/heisenberg_frame.tex:1992:(Theorem~\ref{thm:hochschild-polynomial-growth}) this complex is
chapters/frame/heisenberg_frame.tex:2243:\emph{more complicated} algebra: free fermions and $\beta\gamma$
chapters/frame/heisenberg_frame.tex:2259:\emph{double} pole. The free fermion has a single
chapters/frame/heisenberg_frame.tex:2298:The bar complex $\barB(\mathcal{F})$ of the free fermion is acyclic:
chapters/frame/heisenberg_frame.tex:2312:The Koszul dual of the free fermion is the $\beta\gamma$ system,
chapters/frame/heisenberg_frame.tex:2365:the free fermion has $d_{\mathrm{residue}} = 0$.
chapters/examples/lattice_foundations.tex:71:level~$1$ is $V_{Q}$ for the root lattice $Q$; the free fermion
chapters/examples/lattice_foundations.tex:1672:\index{shadow tower!class G universality}%
chapters/examples/lattice_foundations.tex:4493:(Heisenberg, lattice, free fermion) where every Koszul pair is
chapters/examples/free_fields.tex:54:The free fermion $r$-matrix vanishes: the simple pole in the
chapters/examples/free_fields.tex:77:The free fermion is Gaussian with
chapters/examples/free_fields.tex:86:single-generator free fermion is class~G ($r_{\max} = 2$) by

thinking
**Reviewing algebra theorems**

I think I need to look into the theorem properties on e2-formality and Hochschild details to ensure I'm not overstating free algebra with v111. I feel like I’ve seen something about this before. I should also check out the Hilbert series for the H polynomial, which seems relevant. Let’s inspect the relevant theorem lines to clarify my understanding. It's all about ensuring accuracy in my statements!
exec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '1660,1710p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2808,2830p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '690,1075p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3188,3225p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"free polynomial|free graded|graded-commutative algebra|brace|Massey|formal as an E_2|cohomologically trivial\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2808	\]
  2809	The shadow obstruction tower \emph{is} the $L_\infty$-formality
  2810	obstruction tower at all degrees
  2811	(Theorem~\ref{thm:shadow-formality-identification}). The four
  2812	classes G/L/C/M are the four formality types:
  2813	$\mathbf{G}$ = free,
  2814	$\mathbf{L}$ = Lie,
  2815	$\mathbf{C}$ = quadratic non-Lie,
  2816	$\mathbf{M}$ = genuinely nonlinear.
  2817	
  2818	The Swiss-cheese formality condition ($m_k^{\mathrm{SC}}=0$ for
  2819	all $k\ge 3$) selects exactly class~$\mathbf{G}$:
  2820	a chiral algebra in the standard landscape is SC-formal if and
  2821	only if it is Heisenberg
  2822	(Proposition~\ref{prop:sc-formal-iff-class-g}).
  2823	The forward direction is immediate (abelian bracket kills all
  2824	nested operations); the converse uses nondegeneracy of the
  2825	invariant form to force the bracket to vanish from $S_3=0$.
  2826	
  2827	The algebraic depth $d_{\mathrm{alg}}(\cA)$ exhibits a gap:
 succeeded in 52ms:
  1660	
  1661	The twenty-four Niemeier lattices are the even unimodular lattices
  1662	in dimension~$24$. They form a finite classification: each is
  1663	determined by its root system~$R(\Lambda)$, which satisfies
  1664	Niemeier's constraint that all irreducible components have the
  1665	same Coxeter number~$h$. The twenty-fourth lattice, with
  1666	$R = \varnothing$, is the Leech lattice~$\Lambda_{\mathrm{Leech}}$.
  1667	
  1668	\begin{theorem}[Niemeier shadow universality;
  1669	\ClaimStatusProvedHere]%
  1670	\label{thm:lattice:niemeier-shadow-universality}%
  1671	\index{Niemeier lattice!shadow universality}%
  1672	\index{shadow tower!class G universality}%
  1673	Let $\Lambda$ be any of the twenty-four Niemeier lattices. Then:
  1674	\begin{enumerate}[label=\textup{(\roman*)}]
  1675	\item $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda) = 24$
  1676	for all twenty-four lattices.
  1677	\item $S_r(V_\Lambda) = 0$ for all $r \geq 3$: every Niemeier
  1678	lattice VOA is class~$\mathbf{G}$ with shadow depth~$2$.
  1679	\item The genus-$g$ scalar amplitude is
 succeeded in 51ms:
  3188	\subsection*{Lattice, free fermion, and the Gaussian shadow}
  3189	
  3190	Two further families complete the Gaussian class.
  3191	
  3192	Lattice vertex algebras
  3193	$V_\Lambda = \cH_k^{\otimes N} \otimes
  3194	\mathbb{C}[\Lambda]_\varepsilon$ for an even lattice~$\Lambda$
  3195	of rank~$N$ inherit class~G from their Heisenberg factor:
  3196	$\kappa(V_\Lambda) = \mathrm{rank}(\Lambda)$, independent of
  3197	the lattice's inner products and cocycle~$\varepsilon$. The
  3198	curvature sees only the free-boson contribution; the braiding
  3199	sees the group ring $\mathbb{C}[\Lambda]_\varepsilon$. Shadow
  3200	depth~$2$. For self-dual lattices the partition function is an
  3201	honest modular form; at rank~$24$ the bar-complex invariants
  3202	$(h, \mathrm{rank})$ discriminate between all $24$ Niemeier
  3203	lattice VOAs. The arithmetic of the lattice theta function is
  3204	invisible to the shadow obstruction tower but visible to the
  3205	genus-$2$ amplitude, a Siegel modular form for
  3206	$\mathrm{Sp}(4, \mathbb{Z})$.
  3207	
 succeeded in 52ms:
   690	
   691	\begin{theorem}[Koszul duality for Hochschild cohomology
   692	\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
   693	\label{thm:main-koszul-hoch}
   694	\index{Hochschild cohomology!Koszul duality|textbf}
   695	\textup{[Regime: quadratic on the Koszul locus
   696	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   697	
   698	For every chiral Koszul datum~$\cA$
   699	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})} with
   700	dual~$\cA^!$ on a smooth projective curve~$X$, the bigraded chiral
   701	Hochschild complex
   702	\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
   703	the \emph{derived-level} duality:
   704	\begin{equation}\label{eq:hochschild-H-derived}
   705	RHH_{\mathrm{ch}}(\cA)
   706	\;\simeq\;
   707	R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr).
   708	\end{equation}
   709	On cohomology:
 succeeded in 50ms:
chapters/theory/chiral_hochschild_koszul.tex:28:carry natural brace and $E_2$ structures. The convolution dg~Lie
chapters/theory/chiral_hochschild_koszul.tex:49: (Theorem~\ref{thm:chiral-deligne-tamarkin}). The brace dg algebra
chapters/theory/chiral_hochschild_koszul.tex:1046:\item All higher $\Etwo$-operations \textup{(}braces of
chapters/theory/chiral_hochschild_koszul.tex:1047: degree~$\geq 3$, Massey products, $A_\infty$ corrections\textup{)}
chapters/theory/chiral_hochschild_koszul.tex:1048: are cohomologically trivial.
chapters/theory/chiral_hochschild_koszul.tex:1066:The brace $b_{k-1}(a; a_1, \ldots, a_{k-1})$ for $a \in H^p$,
chapters/theory/chiral_hochschild_koszul.tex:1071:so the braces factor through a single diagonal line in the
chapters/theory/chiral_hochschild_koszul.tex:1074:model of the $\Etwo$-structure then shows that all higher braces are
chapters/theory/chiral_hochschild_koszul.tex:3421:&= \underbrace{\dzero^2}_{=\,0}
chapters/theory/chiral_hochschild_koszul.tex:5094:Definition~\ref{def:chiral-hochschild-cochain-brace}. In that
chapters/theory/chiral_hochschild_koszul.tex:5095:algebraic model, the single brace $f\{g\}$ is the pre-Lie
chapters/theory/chiral_hochschild_koszul.tex:5096:insertion of Example~\ref{ex:single-brace-chiral}, and the
chapters/theory/chiral_hochschild_koszul.tex:5109:the geometric avatar of the single brace $f\{g\}$. We therefore
chapters/theory/chiral_hochschild_koszul.tex:5138:Theorem~\ref{thm:brace-dg-algebra} shows that $\delta$ is a
chapters/theory/chiral_hochschild_koszul.tex:5139:derivation of the brace operations; hence
chapters/theory/chiral_hochschild_koszul.tex:5152:the cup product is the binary closed operation and the single brace
chapters/theory/chiral_hochschild_koszul.tex:5156:brace-cup compatibility, so on cochains one has
chapters/theory/chiral_hochschild_koszul.tex:5222:so $f \circ g$ is the geometric realization of the single brace
chapters/theory/chiral_hochschild_koszul.tex:5424:\item $F_2$ is the brace operation
chapters/theory/chiral_hochschild_koszul.tex:5427:\item $F_3$ is the Jacobiator homotopy for the brace bracket
codex
The class-`G` surface inside the target file is mostly consistent already: its table and proof lane treat `Heisenberg`, `lattice VOA`, and `free fermion` as Gaussian. The bad step is narrower than the user summary suggests: the proposition proof later refers to a nonexistent bilinear-form argument, while the file itself already contains a stronger operadic/shadow-tower route that works uniformly across the whole class.
exec
/bin/zsh -lc "rg -n \"class~\\\\mathbf\\{G\\}|class~\\"'$G'"\\"'$|lattice VOA|lattice & .*G|SC-formal|Gaussian" chapters/theory/chiral_koszul_pairs.tex | sed -n '"'1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3288,3330p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '714,730p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:class~\mathbf\{G\}|class~$G$|lattice VOA|lattice & .*G|SC-formal|Gaussian)
             ^^
error: unrecognized escape sequence
 succeeded in 51ms:
   714	Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
   715	coalgebra identifies its Verdier dual factorization algebra with the
   716	Koszul dual algebra
   717	$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
   718	the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
   719	degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
   720	producing exactly the commutative Koszul dual
   721	(\S\ref{sec:frame-koszul-dual}).
   722	Because $\mathcal{H}_k$ is abelian, the PBW spectral sequence
   723	(Theorem~\ref{thm:pbw-koszulness-criterion}) is trivial and the
   724	Koszul complex $K_\tau(\mathcal{H}_k,
   725	\mathrm{Sym}^{\mathrm{ch}}(V^*))$ is manifestly acyclic.
   726	\end{example}
   727	
   728	\begin{example}[Explicit correspondence: \texorpdfstring{$bc$}{bc} ghost system and \texorpdfstring{$\beta\gamma$}{beta-gamma} system]
   729	\label{ex:bc-betagamma-koszul}
   730	Consider the chiral Koszul pair $(\mathcal{BC}, \mathcal{BG})$ where:
 succeeded in 51ms:
  3288	\multicolumn{6}{@{}l}{\textit{Virasoro and $\cW$-algebras}} \\[2pt]
  3289	$\mathrm{Vir}_c$, generic $c$
  3290	 & universal & $1$ & Proved & PBW univ.\ & $M$, $r_{\max}=\infty$ \\
  3291	$\mathrm{Vir}$ at $c = 0$
  3292	 & universal & $1$ & Proved & PBW univ.\ & $M$, $r_{\max}=\infty$ \\
  3293	$L(c_{3,4}, 0)$ Ising${}^{\ddagger}$
  3294	 & simple quot.\ & $1$ & \textbf{Not K.}\ & null vect.\ & $M$, $r_{\max}=\infty$ \\
  3295	$\cW_3$ (universal)
  3296	 & universal & $2$ & Proved & PBW univ.\ & $M$, $r_{\max}=\infty$ \\
  3297	$\cW_{1+\infty}$
  3298	 & limit & $\infty$ & Proved & MC4 compl.\ & $M$, $r_{\max}=\infty$ \\
  3299	$N{=}2$ SCA${}^{\S}$
  3300	 & extended & $4$ & Proved & PBW univ.\ & $M$, $r_{\max}=\infty$ \\
  3301	\midrule
  3302	\multicolumn{6}{@{}l}{\textit{Lattice and logarithmic}} \\[2pt]
  3303	$V_{D_4}$ lattice VOA
  3304	 & lattice & $28$ & Proved & lattice filt.\ & $G$, $r_{\max}=2$ \\
  3305	Triplet $\cW(2)$
  3306	 & logarithmic & $4$ & Open & --- & unknown \\
  3307	\bottomrule
exec
/bin/zsh -lc "rg -n \"filtered-comparison-unit|bar-side filtered comparison|unit-side analogue|bar-degree analogue\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:361:\label{lem:filtered-comparison-unit}
chapters/theory/chiral_koszul_pairs.tex:362:\index{spectral sequence!bar-side filtered comparison}
chapters/theory/chiral_koszul_pairs.tex:377:This is the unit-side analogue of
chapters/theory/chiral_koszul_pairs.tex:475:convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}


thinking
**Examining proof details**

The regex check failed, but that’s not crucial. I might rerun it later if needed. I should read the theorem around 2520 and inspect sections around 2885 for any issues the user mentioned. There seems to be confusion over line numbers in different versions. The user refers to line 2539, which may not fully align with our current proof. I want to clarify that the proof doesn't utilize bilinear form, which is a key requirement.
thinking
**Searching for bilinear form references**

I just realized there's a mention of bilinear form in the preface, but it's not in the target file. I should check if there’s a related proposition later on, possibly around 2893. My next step is to search for "C(x,y,z)" or "kappa(x)" to see if they show up in the context I'm looking for. This might help clarify whether these concepts are used elsewhere in the document. I want to be thorough!
🌐 Searching the web...
🌐 Searched the web

thinking
**Assessing web call error**

Oops, it looks like I accidentally made a web call from the wrong tool. That can happen! I think it’s okay to ignore any issues since it’s empty anyway. Now, I need to focus on searching locally for C(x,y,z) or kappa(x). This seems like a straightforward task, and I’ll make sure to get it right this time. Let's keep going and find what I need!
exec
/bin/zsh -lc "rg -n \"C\\(x,y,z\\)|C\\(x, y, z\\)|kappa\\(x,\\[y,z\\]\\)|\\kappa\\(x,\\[y,z\\]\\)|invariant bilinear form|metric\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"theorematic|thm:nms-archetype-trichotomy|shadow-archetype-classification|nms-archetype-trichotomy|class G\" chapters/theory/chiral_koszul_pairs.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:C\(x,y,z\)|C\(x, y, z\)|kappa\(x,\[y,z\]\)|\kappa\(x,\[y,z\]\)|invariant bilinear form|metric)
                                                  ^^
error: unrecognized escape sequence
 succeeded in 52ms:
78:(Theorem~\ref{thm:shadow-archetype-classification}), record the
2811:\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
2896:\index{class G@class~$G$!characterised by SC-formality}
2927:degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
2947:\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
3329:(Theorem~\ref{thm:nms-archetype-trichotomy})
3450:(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
4798:appendix. The theorematic core of this chapter does not depend on
6515:not part of the present theorematic surface.
exec
/bin/zsh -lc "rg -n \"invariant bilinear form|metric|C\\(x|kappa\\(x|\\\\kappa\\(x\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3438,3465p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '70,95p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:invariant bilinear form|metric|C\(x|kappa\(x|\kappa\(x)
                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  3438	Heisenberg & $2$ (finite) & Gaussian \\
  3439	Affine $\widehat{\fg}_k$ & $3$ (finite) & Lie \\
  3440	$\beta\gamma$ system & $4$ (finite) & Contact \\
  3441	Virasoro $\mathrm{Vir}_c$ & $\infty$ & Mixed \\
  3442	$\mathcal{W}_N$ & $\infty$ & Mixed \\
  3443	\hline
  3444	\end{tabular}
  3445	\end{center}
  3446	All five are chirally Koszul (genus-$0$ slice is formal), yet the
  3447	Virasoro algebra has infinite shadow depth
  3448	($\mathfrak{o}^{(5)}_{\mathrm{Vir}} \neq 0$
  3449	at genus~$\geq 1$). The archetype classification
  3450	(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
  3451	Koszul locus by the all-genera termination behavior of
  3452	$\Theta_\cA$, a transverse invariant invisible to genus~$0$.
  3453	\end{remark}
  3454	
  3455	\begin{remark}[Shadow classes under direct sum]
  3456	\label{rem:shadow-class-direct-sum}
  3457	\index{shadow depth!direct sum}
 succeeded in 51ms:
    70	eigenspace decomposition) is conditional on perfectness of the
    71	bar-cobar normal complex. One (D-module purity) is a
    72	one-directional implication. The count is exact:
    73	$9 + 1 + 1 + 1$.
    74	
    75	Two distinctions require emphasis. First, the four complexity
    76	classes G/L/C/M, with shadow depths
    77	$\{2, 3, 4, \infty\}$
    78	(Theorem~\ref{thm:shadow-archetype-classification}), record the
    79	degree at which the shadow obstruction tower first becomes
    80	nontrivial; they do \emph{not} record failure of Koszulness.
    81	Every standard chiral algebra is chirally Koszul. The classes
    82	separate algebras by the complexity of their higher-genus
    83	behaviour, not by the validity of the duality. Second,
    84	Koszulness and SC formality are logically independent properties.
    85	Koszulness is the condition that bar cohomology is concentrated
    86	in degree one; SC formality is the condition
    87	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
    88	bar complex. All standard families are Koszul; only class~$G$
    89	(Heisenberg and its relatives) is SC-formal
Plan update
Context is loaded. I’ve isolated seven fixes into three edit clusters so I can keep the write surface minimal and re-verify each theorem block after patching.
  → Rectify Theorem A and surrounding Verdier/four-object language so every post-\mathbb{D}_{\Ran} statement is algebra-level and references the actual bar-side comparison lemma
  • Repair the Koszul meta-theorem status surface by separating unconditional genus-0 equivalence from the proved all-genera uniform-weight refinement and by weakening item (viii) to the strongest Hochschild consequence actually proved
  • Repair the SC-formality/class-G proposition so the proof works uniformly for Heisenberg, lattice VOA, and free fermion without any bilinear-form argument, then re-read the modified blocks and run targeted label/reference/forbidden-language checks
codex
I’ve got enough context to patch. The edits will stay inside `chapters/theory/chiral_koszul_pairs.tex`, and they’ll do three things: tighten the Theorem A Verdier lane to the algebra side after `\mathbb{D}_{\Ran}`, split the Koszul meta-theorem into what is actually equivalent versus what is proved only as a consequence or refinement, and replace the SC-formality converse with the uniform operadic/shadow-tower proof that already fits all of class `G`.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '640,705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '40,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Verdier dual.*coalgebra|bar coalgebra.*Verdier|post-Verdier|factorization algebra attached to the Verdier-dual datum|Theorem~A|A_2|dual factorization algebra|homotopy Koszul dual factorization algebras|SC-formal|class~\\"'$G'"\\"'$|class~G" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   640	
   641	\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
   642	\index{Koszul pair!chiral|textbf}
   643	A \emph{chiral Koszul pair} on a smooth projective curve~$X$
   644	is a pair of chiral Koszul data
   645	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
   646	Definition~\textup{\ref{def:chiral-koszul-morphism})}
   647	\[
   648	(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
   649	(\cA_2, \cC_2, \tau_2, F_\bullet)
   650	\]
   651	equipped with Verdier-compatible factorization-algebra
   652	identifications
   653	\[
   654	\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
   655	\qquad
   656	\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
   657	\]
   658	compatible with the twisting morphisms and filtrations.
   659	In this situation we write $\cA_2 \simeq \cA_1^!$ and
 succeeded in 52ms:
    40	Koszul: it does not see the genus corrections in the bar
    41	complex, and it does not detect the shadow obstruction tower
    42	whose depth varies from two to infinity across the standard
    43	families.
    44	
    45	The bar-cobar adjunction of Theorem~A
    46	(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
    47	functorial pair that resolves all three obstructions. It is the
    48	unique adjunction that (a)~inverts on the Koszul locus, producing
    49	$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
    50	(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
    51	Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
    52	homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
    53	$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
    54	H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    55	(Theorem~\ref{thm:quantum-complementarity-main}).
    56	No other functorial construction achieves all three: the operadic
    57	adjunction achieves (a) but not (b) or (c); Verdier duality alone
    58	achieves (b) but has no bar-cobar content; complementarity (c)
    59	requires both (a) and (b) as input.
 succeeded in 50ms:
45:The bar-cobar adjunction of Theorem~A
52:homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
89:(Heisenberg and its relatives) is SC-formal
142:locus (Theorem~A) are proved. The Verdier intertwining that
552:\begin{remark}[Theorem~A decomposition]\label{rem:theorem-A-decomposition}
569: dual pair, applying Verdier duality to the bar coalgebra of one side
570: produces the dual factorization algebra of the other.
649:(\cA_2, \cC_2, \tau_2, F_\bullet)
659:In this situation we write $\cA_2 \simeq \cA_1^!$ and
660:$\cA_1 \simeq \cA_2^!$.
688:$\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
715:coalgebra identifies its Verdier dual factorization algebra with the
1137:Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
1146:H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
1148:% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
1149:% $\cA_2 = \cA_1^!$ creates a notational double-dual. The intended meaning
1152:% The subsequent prose clarifies this: $\barBch(\cA_1) \simeq \cA_2^!$
1156:Equivalently, $\bar{B}^{\mathrm{ch}}(\cA_1) \simeq \cA_2^!$ in the
1157:derived category of graded chiral coalgebras, where $\cA_2^!$ carries
1160:$\bar{B}^{\mathrm{ch}}(\cA_1) \to \cA_2^!$ is a
codex
Before editing, I’m checking one more local dependency lane inside the same file: the bar-concentration theorem around `\barB^{\mathrm{ch}}(\cA_1) \simeq \cA_2^!` uses coalgebra language correctly, so I only need to repair the post-Verdier statements, not the bar-coalgebra concentration statements themselves.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4248,4302p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1128,1195p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4248	\index{Lagrangian self-intersection!Theorem A}
  4249	Volume~II reveals that this adjunction is the groupoid
  4250	comodule-module adjunction for the Lagrangian self-intersection
  4251	$\mathfrak{S} = \mathcal{L} \times_{\mathcal{M}} \mathcal{L}$:
  4252	the bar complex $\barB_X(\cA)$ is the structure sheaf of the
  4253	derived self-intersection of the boundary Lagrangian inside a
  4254	$(-2)$-shifted symplectic stack, and the cobar functor reconstructs
  4255	the Lagrangian from its groupoid algebra.
  4256	\end{remark}
  4257	
  4258	\begin{remark}[Twisting morphism content of Theorem~A]
  4259	\label{rem:theorem-a-tau}
  4260	\index{twisting morphism!Theorem A content}
  4261	The unit $\eta_{\tau_i} \colon \cC_i \to \barB_X(\cA_i)$ and
  4262	counit $\varepsilon_{\tau_i} \colon \Omega_X(\cC_i) \to \cA_i$
  4263	in part~(1) are induced by the Koszul morphism~$\tau_i$
  4264	of the underlying twisting datum
  4265	(Definition~\ref{def:chiral-twisting-datum}).
  4266	Part~(1) says each~$\tau_i$ is acyclic;
  4267	part~(2) says that after applying Verdier duality to the bar
 succeeded in 51ms:
  1128	chiral primary.
  1129	\end{remark}
  1130	
  1131	\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
  1132	\label{thm:bar-concentration}
  1133	\index{bar complex!concentration}
  1134	\textup{[Regime: quadratic on the Koszul locus
  1135	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1136	
  1137	Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
  1138	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
  1139	Then the augmented bar complex $\bar{B}^{\mathrm{ch}}(\cA_1)$,
  1140	equipped with its bigrading by bar degree~$p$ and bar-differential
  1141	cohomological degree~$q$, satisfies:
  1142	\[
  1143	H^{p,q}(\bar{B}^{\mathrm{ch}}(\cA_1)) = 0
  1144	\quad\text{for } q \neq 0,
  1145	\qquad
  1146	H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
  1147	\]








thinking
**Exploring theorem details**

I need to clarify what Theorem A says. It seems like item (1) should mention units and counits. A unit is getting into conilpotent complete factorization coalgebras, while a counit relates to factorization algebras. As for items (2) and (3), they're connected to the derived category of factorization algebras. I want to make sure I’m accurately understanding this and keeping everything straight as I think through the theorem.
thinking
**Reviewing theorem details**

I’m thinking about theorem A and its remark regarding Verdier duality and bar coalgebra, which suggests dual factorization algebra is produced. That seems okay since D_Ran(bar coalgebra) gives us algebra. I'm also considering providing an alternative proof for theorem A and making sure to adjust a few lines to avoid slippage. For the missing lemma, it seems our file has it, so no changes might be needed, although I’m still wondering about confirming all references.
thinking
**Clarifying needed edits**

I'm thinking about how to satisfy the user by stating in the summary that no edits are needed since the file already has the lemma: filtered-comparison-unit, and the theorem cites it. It seems that no changes may be necessary for finding 3 either. However, since the user requested a fix, if the current working copy is already fixed, I could report that as FIXED with no changes. But I guess there's an expectation for modifications since line numbers likely refer to the current file.
thinking
**Clarifying theorem proof**

I'm looking at the theorem, which presently discusses unqualified item (vii) regarding both genus-0 and uniform-weight refinement. To clear up any potential confusion, I think it might be beneficial to modify the proof by adding remarks about redundancy and adjusting the graph labels. Specifically, mentioning the "genus-0 clause of (vii)" when referring to the unconditional core would be a helpful edit. This seems like a practical approach!
thinking
**Reviewing theorem edits**

I’m checking the summary, and it seems like there might be some misstatements in sections v and viii. Lines 61-69 mention nine unconditional equivalences and one consequence related to Hochschild duality, which is okay. With the current file, it looks like the biggest edits needed are in the theorem A statement or preamble, and maybe some remarks. Also, I noticed the proof might need rephrasing since it uses "unit and counit being quasi-isomorphisms," but the fundamental theorem gives a weak equivalence for the unit. I could definitely patch that up.
thinking
**Evaluating algebra details**

I'm considering the phrase “all higher braces and Massey products are cohomologically trivial.” It might be more effective to mention that these theorems don't imply the freeness of the underlying graded-commutative algebra. I could cross-reference this with a specific remark as well. There's a remark that doesn't have a label, and creating a new one would need to ensure uniqueness. Perhaps I could simplify the last clause instead of adding more complexity. It seems manageable with grep, but maybe a minimal change will suffice.
thinking
**Clarifying theorem proofs**

I’m looking at the statement of the theorem and its proof. The statement is clear regarding the properties of $\ChirHoch^*(\cA)$ as a formal \Etwo-algebra. I think it’s important to clarify that no freeness follows, although we could strengthen the proposition statement. I might also consider adding a sentence in the proof to emphasize that the freeness of the cup-product algebra isn’t claimed, as that feels minimal and truthful. I'll make sure this all connects properly.
thinking
**Adjusting proof clarity**

I'm considering adjusting the first line of the proof to clearly state, "The forward direction (class G => SC-formal) is exactly Proposition...," highlighting that the class-G row includes Heisenberg, lattice VOAs, and free fermions. It seems like a solid modification. I should also search the target file for any mentions of "bilinear form" or "metric" to ensure they don't pop up elsewhere. I think using fixed-string patterns might work for this. Let's get started!
exec
/bin/zsh -lc "rg -n -F 'invariant bilinear form' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'metric' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'C(x,y,z)' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 50ms:
531:\index{Maurer--Cartan equation!geometric origin}
567:\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
747:\item $\mathcal{BG}$: two bosonic generators $\beta, \gamma$, with no nilpotency (symmetric algebra structure)
751:\emph{Geometric picture.}
866:weight spaces of the symmetric algebra
1650:\begin{remark}[Arithmetic shadows: Koszulness as harmonic metric]
1678:\subsection{The Li--bar spectral sequence and geometric Koszulness}
1679:\label{subsec:li-bar-geometric-koszulness}
1684:give a geometric refinement: the Li filtration on~$\cA$ induces a
1869:Any such comparison would require extra geometric input and is
2015:The Li filtration organizes these null vectors \emph{geometrically}:
2027:Li--bar page, possibly guided by geometric input from a
2252:$\int_{\mathbb{P}^1}\cA \simeq |\barBgeom(\cA)|$, the geometric
2330:Geometrically, $\delta F_g^{\mathrm{cross}}$ is the scalar trace of
2562:\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
2652:Poisson-geometric proof of Koszulness restricted to the affine
2919:symmetric closed sector applies the averaging morphism
3524:The symmetric Euler form of $K_m$ has determinant $4 - m^2$.
3595:sequences. We now record a Poisson-geometric characterization that
3625:providing a Poisson-geometric proof of $E_2$-collapse independent
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\kappa(x,[y,z])' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
Pre-edit verification for the touched theorem surfaces:

```text
FOUR OBJECTS:
1. B(A) = bar coalgebra = T^c(s^{-1}\bar A)
2. A^i = H^*(B(A)) = dual coalgebra
3. A^! = ((A^i)^v) or post-Verdier factorization algebra on Ran(X)
4. Z^der_ch(A) = derived chiral center = Hochschild cochains

target: thm:bar-cobar-isomorphism-main
pre-Verdier objects: C_i, \barB_X(A_i) = coalgebras
post-Verdier objects: D_Ran(C_i), D_Ran(\barB_X(A_i)), \Omega_X(C_i), A_i = factorization algebras
forbidden conflation avoided: "Verdier identifies bar coalgebra with dual coalgebra"
intended fix: split part (1) by natural category; keep parts (2)-(3) strictly algebra-level after D_Ran
verdict: ACCEPT
```

```text
PE-10
surface: thm:koszul-equivalences-meta and proof-web remarks
genus: (vii) = g=0 equivalence + all-genera uniform-weight refinement
degree: all bar degrees; no free variable drift
AP32 weight tag: UNIFORM tagged? Y
(viii): one-way Hochschild consequence only; no converse, no freeness claim
verdict: ACCEPT
```

thinking
**Finalizing proof details**

I'm considering whether I should emphasize in the proof's first sentence that class G row consists of Heisenberg, lattice VOA, and free fermion, ensuring no bilinear-form input is used. It feels necessary to add a line stating, “No invariant metric is invoked.” I think the argument remains consistent throughout the operadic genus-0 tree analysis across the three Gaussian families. This clarification could make the proof stronger and clearer.
codex
I’m applying the patch now. The edits are local to three theorem blocks: Theorem A’s category bookkeeping, the `(vii)/(viii)` scope in the Koszul meta-theorem and its proof web, and an explicit sentence in the SC-formality proof that the argument is the uniform operadic/Wick one, not a metric-based family-specific argument.
codex
The patch partially missed on line wrapping. I’m re-reading the exact local blocks and then applying the edits in smaller hunks so I don’t touch unrelated text.
exec
/bin/zsh -lc "sed -n '2168,2190p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2214,2268p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2070,2118p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '560,575p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4258,4296p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4013,4096p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2900,2972p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2516,2636p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Twisting morphism content of Theorem~A]
\label{rem:theorem-a-tau}
\index{twisting morphism!Theorem A content}
The unit $\eta_{\tau_i} \colon \cC_i \to \barB_X(\cA_i)$ and
counit $\varepsilon_{\tau_i} \colon \Omega_X(\cC_i) \to \cA_i$
in part~(1) are induced by the Koszul morphism~$\tau_i$
of the underlying twisting datum
(Definition~\ref{def:chiral-twisting-datum}).
Part~(1) says each~$\tau_i$ is acyclic;
part~(2) says that after applying Verdier duality to the bar
coalgebra of one side one obtains the dual factorization algebra
recovered from the other;
and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
the extra relative Verdier/base-change input needed to transport
these identifications over a base.
\end{remark}

\begin{remark}[Elementary model presentation;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-a-model}
 succeeded in 52ms:
\item[\textup{(v)}] The bar-cobar counit
 $\Omega(\barBgeom(\cA)) \to \cA$ is a
 quasi-isomorphism
 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-inversion-qi})}.
\item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
 bar-cobar adjunction is an equivalence on the fiber over
 $\barBgeom(\cA)$.
\item[\textup{(vii)}] Factorization homology concentration:
 $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
 If $\cA$ lies on the uniform-weight lane, then for every smooth
 projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
 $H^k(\int_{\Sigma_g}\cA)=0$ for $k \neq 0$, and for $g \geq 1$
 the surviving scalar obstruction class is
 \[
 \mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g
 \]
 \textup{(UNIFORM-WEIGHT; Theorem~\textup{\ref{thm:genus-universality})}.}
\item[\textup{(ix)}] The Kac--Shapovalov determinant
 $\det G_h \neq 0$ in the bar-relevant range
 \textup{(}Theorem~\textup{\ref{thm:kac-shapovalov-koszulness})}.
 succeeded in 52ms:
\medskip
\textsc{Factorization homology concentration}
\textup{(i)}$\Leftrightarrow$\textup{(vii)}
\textup{(}with the all-genera uniform-weight refinement; cf.\
Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(vii)}:
The bar complex \emph{is} factorization homology
(Proposition~\ref{prop:bar-fh}):
$\barB_n(\cA) = (\int_X \cA)_n$. At $g = 0$, $E_2$-collapse gives
$H^k(\int_{\mathbb{P}^1} \cA) = 0$ for $k \neq 0$: the Goodwillie
filtration of $\int_{\mathbb{P}^1} \cA$ has associated graded
given by $\barB_n$ contributions, each concentrated in degree~$0$
by PBW collapse. If $\cA$ lies on the uniform-weight lane, the same
identification holds for every genus. The loop-order spectral
sequence of the higher-genus bar complex collapses on the modular
Koszul locus (Theorem~\ref{thm:loop-order-collapse}), so after the
vertexwise genus-$0$ PBW collapse every loop-order stratum remains
cohomologically concentrated in degree~$0$. Theorem~\ref{thm:genus-universality}
 succeeded in 52ms:
 twisting datum, Koszulity $\Leftrightarrow$ counit qi
 $\Leftrightarrow$ unit we $\Leftrightarrow$ twisted tensor
 products acyclic.
\item \emph{$\mathrm{A}_1$}: bar concentration
 (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
 $H^i(\bar{B}^{\mathrm{ch}}(\cA)) = 0$ for $i \neq 0$ and
 $H^0 \cong \cC$.
\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
 dual pair, applying Verdier duality to the bar coalgebra of one side
 produces the dual factorization algebra of the other.
\end{itemize}
$\mathrm{A}_0$ is the Koszul recognition theorem;
$\mathrm{A}_1$ extracts the dual coalgebra;
$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
\end{remark}
 succeeded in 52ms:
\textup{(v)}$\Rightarrow$\textup{(viii)}:

\smallskip\noindent
The quasi-isomorphism
$\Omega(\barBgeom(\cA)) \xrightarrow{\sim} \cA$ identifies the
bar-cobar resolution with the chiral Hochschild complex. On the
Koszul locus, Theorem~H,
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild} give the stated
cohomological concentration, duality, polynomial Hilbert series,
and $\Etwo$-formality. The proof of
Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
braces and Massey products on $\ChirHoch^*(\cA)$ are
cohomologically trivial. No converse from
\textup{(viii)} to the bar-cobar counit is proved here.

\medskip
\textsc{$A_\infty$ formality}
 succeeded in 51ms:
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
mixed tree formulas stop at arity~$2$, so
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Then every mixed Swiss-cheese operation of arity~$r \geq 3$
vanishes in the Swiss-cheese structure with open colour~$\cA$.
The tree-shadow correspondence is operadic: the arity-$r$ mixed
tree and the degree-$r$ shadow are produced by the same genus-$0$
tree-transfer formula, with the same propagator on internal edges;
the only difference is the output colour, and passage to the
symmetric closed sector applies the averaging morphism
 succeeded in 51ms:
\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
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
 succeeded in 52ms:
\quad\text{($A_\infty$ transfer and Keller classicality),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(iv)}
\quad\text{(Ext diagonal vanishing),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(vii)}
\quad\text{(factorization homology at genus~$0$),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(ix)}
\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(x)}
\quad\text{(FM boundary acyclicity),}
\]
and on the monadic side
\[
\textup{(i)} \Longleftrightarrow \textup{(vi)}
\quad\text{(Barr--Beck--Lurie monadicity).}
\]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -569,3 +569,4 @@
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..57ce5c47ef53d3dea936068e36babf73313dee33
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..57ce5c47ef53d3dea936068e36babf73313dee33
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2077,3 +2077,4 @@
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
@@ -2109,5 +2110,6 @@
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..fd90f3a2dc9297ad4cf96c26b427f47cd229268c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..fd90f3a2dc9297ad4cf96c26b427f47cd229268c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..fd90f3a2dc9297ad4cf96c26b427f47cd229268c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2219,4 +2219,5 @@
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..5e31e29aebb4282d4f200fbc7b146394911c348f
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2214,8 +2217,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..5e31e29aebb4282d4f200fbc7b146394911c348f
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2214,8 +2217,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2185,3 +2185,6 @@
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..9cc947790cb510f5f48e8522a346725d3938bd31
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..9cc947790cb510f5f48e8522a346725d3938bd31
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2528,3 +2528,3 @@
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
@@ -2624,2 +2624,6 @@
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..d68a935ecf5a6f06ba8010e4ee32c42179f216ec
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..d68a935ecf5a6f06ba8010e4ee32c42179f216ec
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.


thinking
**Considering proof adjustments**

I'm thinking of possibly changing the direct arrows from ii to vii, but it might not be necessary since the note indicates that vii refers to the genus-0 clause in the discussion. That's a good point to keep in mind. I also need to patch the SC-formality proof and make a remark on that. It's important to focus on clarity and accuracy in these updates for better understanding.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2921,2 +2921,4 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
@@ -2981,2 +2983,4 @@
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..3ec30ab91b057b1f3d3fe6b9b2e01ae58fc703e5
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..3ec30ab91b057b1f3d3fe6b9b2e01ae58fc703e5
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -4033,3 +4033,7 @@
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
@@ -4046,3 +4050,5 @@
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
@@ -4077,3 +4083,4 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
@@ -4084,3 +4091,4 @@
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..e2135b7e2f8bf74c0f8f8ecf70c83fb1dc2f1c87
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..e2135b7e2f8bf74c0f8f8ecf70c83fb1dc2f1c87
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -4290,3 +4290,3 @@
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
@@ -4315,3 +4315,3 @@
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
apply_patch(auto_approved=true) exited 0 in 27ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..79453b64003489db5b2f2a200fac112d47910f59
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..79453b64003489db5b2f2a200fac112d47910f59
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are



thinking
**Reviewing theorem proof language**

I need to check if the word "give" should be used instead of "gives" in the theorem proof snippet — maybe it's a grammar thing? I'll inspect the modified regions for any additional changes in the theorem's decomposition. Also, there's an alternative proof remark on line 2933 saying it doesn't use bilinear-form input. However, it seems there’s no mention of bilinear form anywhere else. To clarify, I might need to adjust the remark intro to indicate it “admits a second proof path that also stays...” to avoid confusion!
thinking
**Modifying theorem remarks**

The current remark mentions, "admits a second proof path that stays in genus-0 operadic transfer and does not use the bilinear-form input," which might suggest that there's an alternative involving bilinear form. Since we want the theorem to avoid relying on that, I think I should modify the remark intro. Maybe something like "records the same genus-0 operadic transfer argument in a self-contained way" works better. This way, we can remove any mention of bilinear form entirely and clarify the proof path instead! Let’s patch that!
codex
One more local clean-up is still warranted: the “Operadic alternative proof” remark currently phrases itself as avoiding a bilinear-form input, which still hints at the old bad proof. I’m removing that implication so the local theorem surface is internally consistent about which argument is actually being used.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2948,4 +2948,4 @@
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

codex
The write is in place. I’m re-reading the modified theorem blocks and then I’ll run the narrowest verification I can: local diff inspection plus a TeX build check if the file surface stays self-contained enough to make that worthwhile.
exec
/bin/zsh -lc "sed -n '560,575p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2070,2188p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2214,2268p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2900,2975p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2516,2640p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4013,4098p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4258,4296p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 twisting datum, Koszulity $\Leftrightarrow$ counit qi
 $\Leftrightarrow$ unit we $\Leftrightarrow$ twisted tensor
 products acyclic.
\item \emph{$\mathrm{A}_1$}: bar concentration
 (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
 $H^i(\bar{B}^{\mathrm{ch}}(\cA)) = 0$ for $i \neq 0$ and
 $H^0 \cong \cC$.
\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
 dual pair, applying Verdier duality to the bar coalgebra of one side
 and then reading the result on the post-Verdier side produces the
 dual factorization algebra of the other.
\end{itemize}
$\mathrm{A}_0$ is the Koszul recognition theorem;
$\mathrm{A}_1$ extracts the dual coalgebra;
$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
 succeeded in 51ms:
 $p \neq q$.
\item[\textup{(v)}] The bar-cobar counit
 $\Omega(\barBgeom(\cA)) \to \cA$ is a
 quasi-isomorphism
 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-inversion-qi})}.
\item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
 bar-cobar adjunction is an equivalence on the fiber over
 $\barBgeom(\cA)$.
\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
 with uniform-weight all-genera refinement:
 $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
 If $\cA$ lies on the uniform-weight lane, then for every smooth
 projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
 $H^k(\int_{\Sigma_g}\cA)=0$ for $k \neq 0$, and for $g \geq 1$
 the surviving scalar obstruction class is
 \[
 \mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g
 \]
 \textup{(UNIFORM-WEIGHT; Theorem~\textup{\ref{thm:genus-universality})}.}
\item[\textup{(ix)}] The Kac--Shapovalov determinant
 succeeded in 51ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e4256..f218b5b 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@ duality theorem:
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@ them. Condition~\textup{(xii)} implies condition~\textup{(x)}
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
 succeeded in 52ms:
mixed-sector tree formulas with the degree-by-degree shadow tower
after averaging. The criterion below packages this as an equivalence
between SC-formality and truncation of the shadow tower at degree~$2$.

\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
 succeeded in 52ms:
filtration is defined fiberwise and compatible with the FM
stratification, so fiberwise $E_2$-collapse assembles to global
$E_2$-collapse: all transferred differentials $d_r = 0$ for
$r \geq 2$. Hence the spectral sequence
on~$\barBgeom(\cA)$ also collapses at~$E_2$.

\medskip
\textsc{Factorization homology concentration}
\textup{(i)}$\Leftrightarrow$\textup{(vii)}
\textup{(}the equivalence concerns the genus-$0$ clause; the
uniform-weight all-genera statement is a proved refinement.
Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(vii)}:
The bar complex \emph{is} factorization homology
(Proposition~\ref{prop:bar-fh}):
$\barB_n(\cA) = (\int_X \cA)_n$. At $g = 0$, $E_2$-collapse gives
$H^k(\int_{\mathbb{P}^1} \cA) = 0$ for $k \neq 0$: the Goodwillie
filtration of $\int_{\mathbb{P}^1} \cA$ has associated graded
 succeeded in 51ms:
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
programme
(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
\end{remark}

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
 succeeded in 51ms:
single chain.
Its unconditional core already has several proof lanes that do not
route through the same intermediate condition:
\[
\textup{(i)} \Longleftrightarrow \textup{(v)}
\quad\text{(universal twisting morphism and bar filtration),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(iii)}
\quad\text{($A_\infty$ transfer and Keller classicality),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(iv)}
\quad\text{(Ext diagonal vanishing),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(vii)}
\quad\text{(the genus-$0$ clause of factorization homology concentration),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(ix)}
\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(x)}
\quad\text{(FM boundary acyclicity),}
 succeeded in 51ms:
\item construct the relative bar components as bounded holonomic
 $\cD$-complexes on the relative Fulton--MacPherson spaces;
\item prove the relative Verdier/base-change isomorphism on the
 relative Ran space, lift the algebra-level Verdier-compatible pair
 identifications, and check compatibility with the factorization
 gluing maps.
\end{enumerate}
The fixed-curve theorem above is the strongest unconditional result
proved in this chapter.
\end{remark}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-a-lagrangian}
\index{Lagrangian self-intersection!Theorem A}
Volume~II reveals that this adjunction is the groupoid
comodule-module adjunction for the Lagrangian self-intersection
$\mathfrak{S} = \mathcal{L} \times_{\mathcal{M}} \mathcal{L}$:
the bar complex $\barB_X(\cA)$ is the structure sheaf of the
derived self-intersection of the boundary Lagrangian inside a
$(-2)$-shifted symplectic stack, and the cobar functor reconstructs
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

codex
The edited blocks reread cleanly. I’m running one build pass now to catch any LaTeX syntax breakage from the sentence-level edits; if that’s too heavy for the full manuscript, I’ll fall back to reporting the exact limitation.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are


 exited 12 in 3.59s:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.log'
Latexmk: Index file 'main.idx' was written
Latexmk: Missing input file 'main.ind' (or dependence on it) from following:
  No file main.ind.
Latexmk: Log file says output to '/tmp/mkd-chiral-bar-cobar-20260413182155-3056/main.pdf'
Latexmk: applying rule 'makeindex main.idx'...
Rule 'makeindex main.idx':  Reasons for rerun
Category 'other':
  Rerun of 'makeindex main.idx' forced or previously required:
    Reason or flag: 'Initial set up of rule'

------------
Run number 1 of rule 'makeindex main.idx'
------------
------------
Running 'makeindex  -o "main.ind" "main.idx"'
thinking
**Monitoring processing status**

I'm keeping an eye on the status of Latexmk, which is still running. It might need a bit more time. I wonder if I should do a quick poll to see if there are updates or if I just need to be patient for a little while longer. It's always a bit uncertain when things are processing, but I'm here for it! Let's wait and see what happens next.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are



thinking
**Troubleshooting build issues**

I'm facing a build failure due to an unrelated existing issue in the preface. I wonder if there's a way to compile a partial file, but it seems like the failure is independent. I could try running `pdflatex -draftmode -interaction=nonstopmode`, but it likely won't solve anything. Running a syntax check with `chktex` could be useful if it's installed. Ultimately, the build is blocked by an unrelated error, which is quite frustrating!
thinking
**Checking for errors**

I’m thinking about running `sed -n` on the target sections to see if that helps. I could also use `rg -n` to check for specific terms like "factorization homology concentration" and others. It might be a good idea to run `git diff --check` on the file to catch any whitespace errors. I wonder if I should grep to confirm we didn’t accidentally introduce any banned words. We recently added "post-Verdier," which is fine since it has a hyphen, but I need to be careful with other punctuation!
codex
The build is blocked by a pre-existing unrelated LaTeX error in [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978): undefined control sequence `\Rep`. I’m still doing the remaining local checks on the edited file itself so I can close the theorem-surface verification cleanly.
exec
/bin/zsh -lc "rg -n -F 'bilinear-form input' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --check -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'post-Verdier dual factorization algebra' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'bar-degree analogue' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'cup-product algebra need not be free' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'genus-"'$0$ clause'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:

 exited 1 in 51ms:

 succeeded in 51ms:
4291:coalgebra of one side one obtains the post-Verdier dual factorization algebra
 succeeded in 51ms:
2043:genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
2223:\textup{(}the equivalence concerns the genus-$0$ clause; the
2256:\textup{(}this genus-$0$ clause is the only input needed for the
2272:and this genus-$0$ clause is the only input used in the converse
2529:\quad\text{(the genus-$0$ clause of factorization homology concentration),}
2626:its genus-$0$ clause. The uniform-weight all-genera statement recorded
3407:\textup{(i)--(vi)}, the genus-$0$ clause of
 succeeded in 51ms:
2114: cup-product algebra need not be free
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

Plan update
The file edits are complete. I re-read each modified theorem block, verified the local diff, and ran `git diff --check`. A full LaTeX build is currently blocked by an unrelated pre-existing `\Rep` error in `chapters/frame/preface.tex:978`, so verification on the edited surface is local plus textual rather than full-manuscript.
  ✓ Rectify Theorem A and surrounding Verdier/four-object language so every post-\mathbb{D}_{\Ran} statement is algebra-level and references the actual bar-side comparison lemma
  ✓ Repair the Koszul meta-theorem status surface by separating unconditional genus-0 equivalence from the proved all-genera uniform-weight refinement and by weakening item (viii) to the strongest Hochschild consequence actually proved
  ✓ Repair the SC-formality/class-G proposition so the proof works uniformly for Heisenberg, lattice VOA, and free fermion without any bilinear-form argument, then re-read the modified blocks and run targeted label/reference/forbidden-language checks
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are






thinking
**Organizing findings and summaries**

I should note that finding three was already resolved, so it makes sense to mark it as [FIXED] in the final summary. I need to check if the user requested a structured output with bullet points. It's important to mention that some findings require no changes since they're already addressed in the current file. I should include a concise Rectification Summary with each finding, addressing tests done and any build blockages, while ensuring clarity. I'll avoid nested bullets.
thinking
**Summarizing findings status**

For findings 4, 5, 6, and 7, we clarified and edited some related lines. No edits were needed for finding 3, which is marked as resolved. I’ll enumerate the findings: 

1. [FIXED] Theorem A now distinguishes between coalgebra and algebra-level identifications.  
2. [FIXED] Part (2) proof outlines the algebra-level identification clearly.  
3. [FIXED] Finding verified as resolved with no phantom citations.  
4. [FIXED] Genus-0 factorization homology concentration is now explicitly named.  
5. [FIXED] The Hochschild package is noted, disclaiming freeness claims.  
6. [FIXED] SC-formality proof now uses the correct argument type.
thinking
**Clarifying findings regarding class-G**

I’ve noted that finding 7 is marked [FIXED]. The forward class-G direction is now clearly applied uniformly to Heisenberg, lattice VOAs, and free fermions. This means that the local target-file class-G membership is consistent across these areas. It’s important to emphasize that this clarification solidifies how these elements interact within the framework we’re discussing. I’ll ensure this resolution is included in the final summary for clarity.
thinking
**Confirming edits and updates**

I need to verify that the command `git diff --check` passed, and that I've re-read my changes. The `latexmk` process got blocked due to an unrelated issue in preface.tex. I’ll mention there are no label changes or new references — something like "No new labels/refs were introduced." It’s also nice to note that no inconsistencies were added. I could start with a brief paragraph summarizing the edits to chiral_koszul_pairs.tex, including relevant links for reference.
thinking
**Creating clickable file links**

I need to format clickable file links with an absolute target while optionally including the line number. For example, I can use [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex). That seems fine to me. I may also want to include a link for a build failure, like [chapters/frame/preface.tex](/Users/...:978). I don't need any conversational opener here, so let’s move directly to crafting the necessary content.
codex
Edited [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex). Theorem A now cleanly separates coalgebra-side unit equivalences from algebra-side post-Verdier identifications, the Koszul meta-theorem now marks `(vii)` as genus-0 equivalence plus uniform-weight all-genera refinement and states `(viii)` only at the proved Hochschild strength, and the SC-formality lane now explicitly uses the uniform operadic/Wick argument for all class-`G` families.

Local verification passed by re-reading the modified blocks and running `git diff --check`. A full `latexmk` run is currently blocked by an unrelated pre-existing error in [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978): undefined control sequence `\Rep`, so I could not use a full manuscript build to verify this file.

## Rectification Summary
- [FIXED] finding 1 — Theorem A now distinguishes the categories correctly: part `(1)` treats units as coalgebra equivalences and counits as algebra quasi-isomorphisms, while parts `(2)` and `(3)` are explicitly post-`\mathbb{D}_{\Ran}` factorization-algebra statements.
- [FIXED] finding 2 — The proof of Theorem A part `(2)` now states explicitly that the Verdier input is the algebra-level identification from Definition `\ref{def:chiral-koszul-pair}` / Theorem `\ref{thm:verdier-bar-cobar}`, not a coalgebra identification.
- [FIXED] finding 3 — Verified already resolved on the current surface: the proof cites `Lemma~\ref{lem:filtered-comparison-unit}` and no phantom “bar-degree analogue” citation remains.
- [FIXED] finding 4 — Condition `(vii)` is now named as genus-0 factorization homology concentration with a separate uniform-weight all-genera refinement, and the proof-web remarks now say explicitly that the unconditional equivalence uses only the genus-0 clause.
- [FIXED] finding 5 — Condition `(viii)` now states only the proved Hochschild package; the theorem and proof explicitly say no freeness of the underlying graded-commutative cup-product algebra is being claimed.
- [FIXED] finding 6 — The SC-formality lane now states on the theorem surface that the proof uses the operadic/tree-shadow/Wick argument and not any invariant-bilinear-form construction.
- [FIXED] finding 7 — The forward class-`G` implication is now stated explicitly as uniform across Heisenberg, lattice VOA, and free fermion on this file’s theorem surface.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e425636ab84ed7739e227fd6f5e08abb6fb061..f218b5b54a55c61c080a0a8ac1d2082c17587942
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
+ with uniform-weight all-genera refinement:
  $H^k(\int_{\mathbb{P}^1}\cA)=0$ for $k \neq 0$.
  If $\cA$ lies on the uniform-weight lane, then for every smooth
  projective curve $\Sigma_g$ of genus $g \geq 0$ one also has
@@ -2106,9 +2108,10 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
- equivalently, all higher braces and Massey products are
- cohomologically trivial
+ and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
+ all higher braces and Massey products are
+ cohomologically trivial, but the underlying graded-commutative
+ cup-product algebra need not be free
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
@@ -2180,7 +2183,10 @@
 Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
 the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
 braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. No converse from
+cohomologically trivial. This is the full proved content of
+\textup{(viii)} at the theorem level: no freeness statement for the
+underlying graded-commutative cup-product algebra is claimed here.
+No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
 \medskip
@@ -2214,8 +2220,9 @@
 \medskip
 \textsc{Factorization homology concentration}
 \textup{(i)}$\Leftrightarrow$\textup{(vii)}
-\textup{(}with the all-genera uniform-weight refinement; cf.\
-Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
+\textup{(}the equivalence concerns the genus-$0$ clause; the
+uniform-weight all-genera statement is a proved refinement.
+Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:
 
 \smallskip\noindent
 \textup{(i)}$\Rightarrow$\textup{(vii)}:
@@ -2519,7 +2526,7 @@
 \textup{(i)} \Longleftrightarrow \textup{(iv)}
 \quad\text{(Ext diagonal vanishing),}\qquad
 \textup{(i)} \Longleftrightarrow \textup{(vii)}
-\quad\text{(factorization homology at genus~$0$),}
+\quad\text{(the genus-$0$ clause of factorization homology concentration),}
 \]
 \[
 \textup{(i)} \Longleftrightarrow \textup{(ix)}
@@ -2615,6 +2622,10 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
+Within this proof-web discussion, the node \textup{(vii)} always means
+its genus-$0$ clause. The uniform-weight all-genera statement recorded
+in Theorem~\ref{thm:koszul-equivalences-meta}\textup{(vii)} is a
+proved strengthening, not an extra unconditional equivalence.
 Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
 displayed core subweb by forgetting arrow directions and deleting the
 satellite node~\textup{(viii)}.
@@ -2908,6 +2919,8 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
 mixed tree formulas stop at arity~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+This uses the same operadic/Wick-factorization argument in all three
+families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
@@ -2933,8 +2946,8 @@
 \begin{remark}[Operadic alternative proof]
 \index{Swiss-cheese operad!operadic alternative proof}
 Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
-path that stays in genus-$0$ operadic transfer and does not use the
-bilinear-form input.
+path that stays in genus-$0$ operadic transfer and makes the
+tree-shadow mechanism explicit.
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
@@ -2968,6 +2981,8 @@
 rules out~$L$, $C$, and~$M$ by explicit first nonzero operations
 $m_3^{\mathrm{SC}}$, $m_4^{\mathrm{SC}}$, and the infinite tower,
 respectively. Only class~$G$ remains.
+This is the argument used on the theorematic surface because it applies
+uniformly to Heisenberg, lattice VOAs, and free fermions.
 \end{remark}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -4016,7 +4031,11 @@
 \index{Theorem A|textbf}
 \textup{[}Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
-The equivalences below hold in the derived category
+The unit maps in part~\textup{(1)} are equivalences in the derived
+category of conilpotent complete factorization coalgebras on
+$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
+post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
+equivalences in the derived category
 $D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
 factorization algebras on~$X$.
 
@@ -4029,7 +4048,9 @@
 the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
 Then:
 \begin{enumerate}
-\item the canonical units and counits are quasi-isomorphisms:
+\item the canonical unit maps are weak equivalences of conilpotent
+ complete factorization coalgebras, and the canonical counit maps are
+ quasi-isomorphisms of factorization algebras:
 \[
 \cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
 \Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
@@ -4060,14 +4081,16 @@
 (Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
 conditions
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
-the unit and counit being quasi-isomorphisms.
+the unit maps being weak equivalences of factorization coalgebras and
+the counit maps being quasi-isomorphisms of factorization algebras.
 For part~(2), the Verdier compatibility in
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
 indices reversed. In the standard examples, this hypothesis is
 supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
-lives on the post-Verdier factorization-algebra side. Let
+lives on the post-Verdier factorization-algebra side rather than on a
+coalgebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -4265,7 +4288,7 @@
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says that after applying Verdier duality to the bar
-coalgebra of one side one obtains the dual factorization algebra
+coalgebra of one side one obtains the post-Verdier dual factorization algebra
 recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
@@ -4290,7 +4313,7 @@
 $\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
 are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
 \simeq \cA$. Verdier duality identifies the bar coalgebra with the
-homotopy dual factorization algebra via
+homotopy dual factorization algebra via the post-Verdier equivalence
 $\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
 (\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
 theorem; what follows are

tokens used
186,273
