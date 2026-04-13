# R01_chiral_koszul_pairs (463s)

Edited [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:567) to make the Theorem A Verdier lane uniformly algebra-level after `\mathbb{D}_{\operatorname{Ran}}`: the decomposition remark, the standard-construction paragraph, the Heisenberg example, the main proof, and the theorem-A content remark now all distinguish `\barB_X(\cA)` as the bar coalgebra from `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` as the resulting factorization algebra.

I then re-read the other flagged surfaces in the same file and verified they are already repaired on the live surface: the bar-side filtered comparison lemma exists and is cited, `(vii)` is only genus-`0` unconditionally with the all-genera version restricted to the uniform-weight lane, `(viii)` is only a one-way Hochschild consequence, and the SC-formality/class-`G` discussion now covers Heisenberg, lattice VOA, and free fermion without the invalid `\kappa`-trilinear argument. I did not run a full TeX build; verification was by local reread and grep, and I did not change any labels.

## Rectification Summary
- [FIXED] finding 1 — harmonized Theorem A’s Verdier wording so the bar object stays a coalgebra and the post-`\mathbb{D}_{\operatorname{Ran}}` object is always a factorization algebra.
- [FIXED] finding 2 — clarified that the standard-example Verdier input comes from `thm:verdier-bar-cobar` on the algebra side after applying `\mathbb{D}_{\operatorname{Ran}}`, not from a coalgebra identification.
- [FIXED] finding 3 — verified the missing “bar-side filtered comparison” is already present as `lem:filtered-comparison-unit`, and the theorem proof uses that correct local result.
- [NARROWED] finding 4 — verified `(vii)` is already narrowed to the genus-`0` clause unconditionally, with the all-genera strengthening kept only on the uniform-weight lane.
- [NARROWED] finding 5 — verified `(viii)` is already weakened to the proved one-way consequence: Hochschild duality, polynomial Hilbert series, and `\Etwo`-formality, without any free-polynomial claim.
- [FIXED] finding 6 — verified the converse SC-formality proof no longer uses the invalid `\kappa(x,[y,z])` construction and instead runs through shadow-tower truncation/classification.
- [FIXED] finding 7 — verified class `G` is now treated consistently and the forward implication covers the full class-`G` family listed there, including lattice VOA and free fermion.


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
session id: 019d8674-3026-7db3-8ad7-e16513c96173
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
**Considering theorem alterations**

I’m thinking about the guidelines around edits in hot zones, and it seems there’s a specific protocol to follow. It looks like we might be dealing with some findings related to kappa, potentially class G and SC-formality. I need to check whether we should provide PE-10 for scope quantifier modification when changing theorem statements and maybe PE-4 for writing adjustments to bar complex formulas under theorem A. There's a lot to navigate!
codex
Using `beilinson-rectify` for this pass because the task is to repair theorem/proof surfaces in one manuscript file with the strongest truthful fix. I’m first reading the required constitutional files and the cited local dependencies, then I’ll lock the exact theorem surfaces before editing `chapters/theory/chiral_koszul_pairs.tex`.
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 53ms:
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
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

codex
I have the repo-wide constraints loaded. Next I’m mapping the exact theorem and proof blocks in `chiral_koszul_pairs.tex`, plus the cited dependency statements in `bar_construction.tex` and `cobar_construction.tex`, so the edits stay local and truthful.
collab spawn_agent(call_0HthjzpBvCASbpwN3oMfJkLS, prompt="Inspect /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex for the seven findings below. Also read th…")
mcp startup: no servers
spawn_agent(call_0HthjzpBvCASbpwN3oMfJkLS, prompt="Inspect /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex for the seven findings below. Also read th…") pending init:
  agent: 019d8674-a520-7521-b075-690f36a93455
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc "sed -n '1,200p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc 'rg -n "finding" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "seven findings" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/D07_augmentation_ideal.md:1135:I’m considering how many findings to count, possibly seven if I include the bar_construction low. I checked and found 236 overall, but should I summarize the seven findings? The user asked if certain examples use A-bar, rather than bare A, and the orientation example doesn't. Even though it's noted, having an unreduced example in core theory may pose risks. So, I think it should be included as a low issue for clarity. I'll also check the derived_langlands for similar cases but may not find anything significant.
audit_campaign_20260412_231034/AP17_E3_chiral.md:1122:This approach could yield a total of seven findings. However, I'm wondering if having too many findings from the same file might be excessive, but it seems okay for now.
relaunch_20260413_111534/AP22_S2_c12.md:683:I'm looking at the same mathematical table again. I still think the issue is CRITICAL because a reader using the table could get the wrong invariant. However, if there's only one critical mistake, that might be enough. I'm considering combining the findings from lines 8032 and 8044 into one CRITICAL finding, noting that "the degree-2 row at 8044 repeats \dfrac{c}{12}." This approach could reduce our list length while still keeping a total of seven findings.
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:628:Vol I doesn’t currently have any live chapter-level cross-volume part refs in the compliant style, so this patch will set that pattern for the seven findings. I’m applying the minimal replacements now.
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:2217:The user is asking me to address every finding from a completed contract, stating whether each is FIXED with details on how it was fixed or BLOCKED with reasons why. I’ll need to ensure the final answer enumerates each finding clearly. The user mentions needing to include eight items; however, I see there are only seven findings from a live search plus one sibling range. I should confirm what they meant about the eight findings!
exec
/bin/zsh -lc 'rg -n "finding" chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_curved.tex:1172:finding: bounded-below grading gives an inverse limit only after
thinking
**Extracting relevant lines**

I’m reading the target file to extract specific lines that are relevant. I think I’ll use the `rg` tool for labels and perhaps `sed` for processing around the ranges. There’s an idea of using parallel execution to speed things up, which is great! The specific lines I need are around 416, 584, 1998, 2532, 2539, and 3616. So, let’s go ahead and get those chunks; it sounds efficient!
exec
/bin/zsh -lc "sed -n '1900,2065p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '340,660p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2460,2605p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{associated variety!nilradical obstruction}
\index{nilpotent cone!Koszulness obstruction}

Let $k$ be a degenerate admissible level for~$\widehat{\fg}$
with $X_{L_k(\fg)} = \overline{\mathbb{O}} \neq \{0\}$.
The associated graded $R_{L_k} = \operatorname{gr}^F L_k$
is a Poisson algebra whose reduced quotient gives
$\mathcal{O}(\overline{\mathbb{O}})$. The Koszulness
obstruction at degenerate levels comes from two sources:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Reduced Li--bar surface.}
 The reduced quotient
 $\mathcal{O}(\overline{\mathbb{O}})=R_{L_k}^{\mathrm{red}}$
 controls only the reduced Li--bar $E_2$ page furnished by
 Theorem~\ref{thm:associated-variety-koszulness}(ii). Any
 diagonal-concentration statement established on that reduced
 surface is therefore evidence only for the reduced quotient,
 not for the full non-reduced algebra~$R_{L_k}$.
\item \emph{Nilradical obstruction.}
 The nilradical $\mathcal{I} = \sqrt{0} \subset R_{L_k}$
 succeeded in 51ms:
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ is a classical Koszul datum;
\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
 acyclic.
\end{enumerate}
\end{lemma}

\begin{proof}
Filter $\varepsilon_\tau$ by $F_\bullet$. Since the filtration
is bounded below and complete, the spectral sequence converges
strongly (Eilenberg--Moore). The associated graded
$\operatorname{gr} \varepsilon_\tau$ is a quasi-isomorphism
between graded objects, which by \cite[Theorem~3.2.1]{LV12}
identifies $\operatorname{gr} \tau$ as a classical Koszul
morphism. Classical Koszulity gives acyclicity of the
associated graded twisted tensor products. Strong convergence
then lifts this to acyclicity of $K_\tau^L$ and $K_\tau^R$
themselves.
\end{proof}

 succeeded in 51ms:
 $\cA$ is chirally Koszul on $X$, then $f^*\cA$ is chirally
 Koszul on $Y$, and $(f^*\cA)^! \simeq f^*(\cA^!)$.
\end{enumerate}
\end{proposition}

\begin{proof}
\textup{(a)}: Tensor product closure is
Proposition~\ref{prop:koszul-dual-tensor-product}, which
constructs the quadratic-tensor witnessing datum and verifies
strong convergence under $\boxtimes$. The duality identification
$(\cA \boxtimes \cB)^! \simeq \cA^! \boxtimes \cB^!$ follows from
the K\"unneth formula on the bar complex
$\barB(\cA \boxtimes \cB) \simeq \barB(\cA) \boxtimes \barB(\cB)$,
combined with the fact that linear duality commutes with tensor
product over a field.

\textup{(b)}: Involutivity is a consequence of
Theorem~\ref{thm:fundamental-twisting-morphisms} (the bar-cobar
adjunction is a Quillen equivalence on the Koszul locus) and the
biduality of holonomic D-modules under Verdier duality. Concretely,
exec
/bin/zsh -lc "sed -n '3560,3685p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "filtered-comparison|Verdier|SC-formality|class G|lattice|Koszul equiv|Theorem A|bar-cobar-isomorphism-main|thm:verdier-bar-cobar|thm:shadow-formality-identification" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\smallskip\noindent\textbf{Canonical extraction.}
The primitive spectrum is read off directly from the vacuum
character: $G_\cA$ depends only on the sequence $(a_1, a_2,
a_3, \ldots)$ and no further algebraic data.
\end{definition}

\begin{definition}[Completion Hilbert series; \ClaimStatusProvedHere]
\label{def:completion-hilbert-series}
\index{completion Hilbert series|textbf}
\index{bar coalgebra!reduced-weight window}

The \emph{completion Hilbert series} of $\cA$ is the
associated-graded window series of the completed cumulant bar
coalgebra:
\begin{equation}
\label{eq:completion-hilbert-series}
H_\cA(t) \;:=\; \frac{G_\cA(t)}{1 - G_\cA(t)}
\;=\; \sum_{q \geq 1} h_q\, t^q,
\end{equation}
 succeeded in 52ms:
chapters/theory/bar_construction.tex:99:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
chapters/theory/bar_construction.tex:100:Verdier duality on $\operatorname{Ran}(X)$ sends the bar
chapters/theory/bar_construction.tex:106:\begin{remark}[Verdier side of Theorem~A]
chapters/theory/bar_construction.tex:117:Verdier intertwining.
chapters/theory/bar_construction.tex:123:$\cA^!_{\mathrm{ch}}$ (the chiral dual, arising from Verdier duality on
chapters/theory/chiral_koszul_pairs.tex:46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
chapters/theory/chiral_koszul_pairs.tex:51:Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
chapters/theory/chiral_koszul_pairs.tex:57:adjunction achieves (a) but not (b) or (c); Verdier duality alone
chapters/theory/chiral_koszul_pairs.tex:142:locus (Theorem~A) are proved. The Verdier intertwining that
chapters/theory/chiral_koszul_pairs.tex:333:\label{lem:filtered-comparison}
chapters/theory/chiral_koszul_pairs.tex:361:\label{lem:filtered-comparison-unit}
chapters/theory/chiral_koszul_pairs.tex:378:Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
chapters/theory/chiral_koszul_pairs.tex:467:strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
chapters/theory/chiral_koszul_pairs.tex:475:convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
chapters/theory/chiral_koszul_pairs.tex:553:\index{Theorem A!decomposition}
chapters/theory/chiral_koszul_pairs.tex:568: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
chapters/theory/chiral_koszul_pairs.tex:569: dual pair, Verdier duality sends the bar coalgebra of one side
chapters/theory/chiral_koszul_pairs.tex:574:$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
chapters/theory/chiral_koszul_pairs.tex:651:equipped with Verdier-compatible factorization-algebra
chapters/theory/chiral_koszul_pairs.tex:666:and Verdier compatibility can all be verified without
exec
/bin/zsh -lc 'rg -n "Finding [0-9]" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/C02_introduction.md:641:./wave2_audit_20260413_001942/S06_intro_to_body.md:1186:Then there's Potential Finding 45: it might be necessary to check the theorem registry to see if `thm:modular-koszul-duality-main` is missing. I should perform a search for that.
wave2_audit_20260413_001942/S06_intro_to_body.md:1186:Then there's Potential Finding 45: it might be necessary to check the theorem registry to see if `thm:modular-koszul-duality-main` is missing. I should perform a search for that.
audit_campaign_20260412_231034/XV13_biblio_xvol.md:1296:/Users/raeez/chiral-bar-cobar/compute/audit/dnp_kz_gz_deep_beilinson_audit_2026_04_07.md:210:## Finding 12 (MODERATE): thm:frontier-twisted-holography cites GZ26 but is tagged ProvedHere
audit_campaign_20260412_231034/BC07_genus_1.md:1302:In Finding 1, I should reference "the same zero-mode/oscillator truncation reappears in [genus_expansions.tex:159]." I also noticed duplicates in Finding 3 at specific lines in various files. 
fix_wave_A_20260413_112727/A07_free_fields.md:5:- Finding 1: FIXED. The vanishing proposition now explicitly says it is only about the one-dimensional weight-changing line. I added that the quartic contact shadow belongs to the mixed charged stratum, so it does not contradict class C / global depth 4.
fix_wave_A_20260413_112727/A07_free_fields.md:6:- Finding 2: FIXED. The global-depth theorem now says it is about the full two-channel deformation space, and the `T`-line statement is rewritten as a separately computed one-dimensional slice, not a literal restriction of a globally vanishing quintic class. I also adjusted the proof and the adjacent remark to match that scope.
fix_wave_A_20260413_112727/A07_free_fields.md:2712:- Finding 1: FIXED. The vanishing proposition now explicitly says it is only about the one-dimensional weight-changing line. I added that the quartic contact shadow belongs to the mixed charged stratum, so it does not contradict class C / global depth 4.
fix_wave_A_20260413_112727/A07_free_fields.md:2713:- Finding 2: FIXED. The global-depth theorem now says it is about the full two-channel deformation space, and the `T`-line statement is rewritten as a separately computed one-dimensional slice, not a literal restriction of a globally vanishing quintic class. I also adjusted the proof and the adjacent remark to match that scope.
fix_wave_A_20260413_112727/A04_introduction.md:5:`FIXED` Finding 1: the ordered `E_1` Maurer-Cartan sentence now cites `Theorem~\ref{thm:e1-mc-element}` instead of `thm:mc2-bar-intrinsic`, matching the ordered-bar theorem in [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:291).
fix_wave_A_20260413_112727/A04_introduction.md:7:`FIXED` Finding 2: the MC4 paragraph now states that for `V_k(\mathfrak g)`, `\mathrm{Vir}_c`, principal `\mathcal W`-algebras, and lattice algebras, the relevant inverse-limit object is the weight completion `\widehat{\cA}^{\mathrm{wt}}`, so the MC4 statement is formulated on their weight completions rather than the direct-sum algebras.
fix_wave_A_20260413_112727/A04_introduction.md:1258:`FIXED` Finding 1: the ordered `E_1` Maurer-Cartan sentence now cites `Theorem~\ref{thm:e1-mc-element}` instead of `thm:mc2-bar-intrinsic`, matching the ordered-bar theorem in [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:291).
fix_wave_A_20260413_112727/A04_introduction.md:1260:`FIXED` Finding 2: the MC4 paragraph now states that for `V_k(\mathfrak g)`, `\mathrm{Vir}_c`, principal `\mathcal W`-algebras, and lattice algebras, the relevant inverse-limit object is the weight completion `\widehat{\cA}^{\mathrm{wt}}`, so the MC4 statement is formulated on their weight completions rather than the direct-sum algebras.
compute/audit/raeeznotes114_beilinson_audit.md:9:### Finding 3: Theorem 2 associativity proof is a sketch, not a proof
compute/audit/raeeznotes114_beilinson_audit.md:12:### Finding 8: Three-way bar/center/Θ_A distinction collapsed (AP25/AP9)
compute/audit/raeeznotes114_beilinson_audit.md:15:### Finding 12: Compact generator existence is a hidden hypothesis (AP7)
compute/audit/raeeznotes114_beilinson_audit.md:36:- S2: Meromorphic tensor product on modules (fills Costello Finding 6)
compute/audit/representation_theory_thread_2026_03_31.md:307:**Finding 1**: (C1) unconditional on Koszul locus (line 73 explicit). (C2) conditional on perfectness + nondegeneracy (line 50). CORRECT.
compute/audit/representation_theory_thread_2026_03_31.md:309:**Finding 2 (MODERATE, AP7)**: rem:homotopy-native-c (line 512) cites prop:ptvv-lagrangian without the g>=2 restriction the proposition carries. Shifted-symplectic proved for g>=2 only.
compute/audit/representation_theory_thread_2026_03_31.md:311:**Finding 3 (SERIOUS, AP2)**: CLAUDE.md lists:
compute/audit/representation_theory_thread_2026_03_31.md:321:**Finding 4**: Involution-splitting lemma requires char != 2 (line 161). Satisfied over C. Key step for (C1).
exec
/bin/zsh -lc 'rg -l "seven findings"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/D07_augmentation_ideal.md
audit_campaign_20260412_231034/AP17_E3_chiral.md
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md
relaunch_20260413_111534/AP22_S2_c12.md
exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs" -n' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 2586

foundation_audit_chapters_report.md:252:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1390 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1412, before the next claim at line 1414.
foundation_audit_chapters_report.md:253:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2663 — PROBLEM: `\ClaimStatusProvedHere` proposition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2674, before the next claim at line 2683.
foundation_audit_chapters_report.md:254:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3438 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3458, before the next claim at line 3460.
foundation_audit_chapters_report.md:255:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3460 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3480, before the next claim at line 3482.
foundation_audit_chapters_report.md:256:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3482 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3500, before the next claim at line 3502.
foundation_audit_chapters_report.md:257:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3502 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3520, before the next claim at line 3522.
foundation_audit_chapters_report.md:258:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3522 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3545, before the next claim at line 3547.
wave2_audit_20260413_001942/C01_preface.md:701:1020:\include{chapters/theory/chiral_koszul_pairs}
wave2_audit_20260413_001942/S06_intro_to_body.md:15:- [MEDIUM] chapters/theory/introduction.tex:380 — PROBLEM: the intro assigns the wrong job to Theorem A: “Theorem A constructs the arena `\gAmod`.” The actual theorem A at `chapters/theory/chiral_koszul_pairs.tex:3638-3685` is geometric bar-cobar duality. The existence of `\Theta_\cA` in the convolution algebra is handled by `thm:mc2-bar-intrinsic` at `chapters/theory/higher_genus_modular_koszul.tex:3498-3528`, not by Theorem A. The same misassignment repeats at `chapters/theory/introduction.tex:732-734`. FIX: rewrite both passages so Theorem A supplies the bar-cobar/Verdier apparatus, while the convolution/MC existence claims are attributed to the convolution definition and `Theorem~\ref{thm:mc2-bar-intrinsic}`.
wave2_audit_20260413_001942/S06_intro_to_body.md:458:./chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
wave2_audit_20260413_001942/S06_intro_to_body.md:462:./rectification_20260412_233715/R02_higher_genus_complementarity.md:506:chapters/theory/chiral_koszul_pairs.tex:3611:\label{thm:bar-cobar-isomorphism-main}
wave2_audit_20260413_001942/S06_intro_to_body.md:464:./rectification_20260412_233715/R18_cobar_construction.md:448:chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
wave2_audit_20260413_001942/S06_intro_to_body.md:487:/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,3695p'" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/S06_intro_to_body.md:1479:- [MEDIUM] chapters/theory/introduction.tex:380 — PROBLEM: the intro assigns the wrong job to Theorem A: “Theorem A constructs the arena `\gAmod`.” The actual theorem A at `chapters/theory/chiral_koszul_pairs.tex:3638-3685` is geometric bar-cobar duality. The existence of `\Theta_\cA` in the convolution algebra is handled by `thm:mc2-bar-intrinsic` at `chapters/theory/higher_genus_modular_koszul.tex:3498-3528`, not by Theorem A. The same misassignment repeats at `chapters/theory/introduction.tex:732-734`. FIX: rewrite both passages so Theorem A supplies the bar-cobar/Verdier apparatus, while the convolution/MC existence claims are attributed to the convolution definition and `Theorem~\ref{thm:mc2-bar-intrinsic}`.
audit_campaign_20260412_231034/BC04_c_13.md:1250:chapters/theory/chiral_koszul_pairs.tex:4405:The non-quadratic case (Virasoro, $W_N$, Yangian) is handled uniformly via $I$-adic completion; the uncompleted statement $\bar{B}^{\mathrm{ch}}(\mathcal{A})^{\vee} \simeq \mathcal{A}^!$ (bar coalgebra dualizes to the Koszul dual algebra) holds only in the quadratic case, where $I$-adic and discrete topologies coincide.
audit_campaign_20260412_231034/T20_gerstenhaber.md:1440:992:\include{chapters/theory/chiral_koszul_pairs}
audit_campaign_20260412_231034/F12_MC_equation.md:1070:/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:236:coproduct. The MC equation $d\tau + \tau \star \tau = 0$ is
audit_campaign_20260412_231034/F12_MC_equation.md:1071:/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:447:Maurer--Cartan equation $d\tau + \tau \star \tau = 0$.

thinking
**Examining audit report references**

I see a set of seven critical problems mentioned around lines 252-258 in the `foundation_audit_chapters_report.md` file, likely linked to missing proofs for ClaimStatus. I'm curious to check the context between lines 230 and 260 to understand the "seven findings" more clearly and how they relate to the foundation audit. I'll pull that section next to explore further!
exec
/bin/zsh -lc "sed -n '220,280p' foundation_audit_chapters_report.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
- [CRITICAL] chapters/examples/yangians_drinfeld_kohno.tex:263 — PROBLEM: `\ClaimStatusProvedHere` computation has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 273, before the next claim at line 275.
- [CRITICAL] chapters/examples/yangians_foundations.tex:2867 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2885, before the next claim at line 2887.
- [CRITICAL] chapters/examples/yangians_foundations.tex:2967 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2980, before the next claim at line 2982.
- [CRITICAL] chapters/examples/yangians_foundations.tex:3194 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3204, before the next claim at line 3224.
- [CRITICAL] chapters/examples/yangians_foundations.tex:3257 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3265, before the next claim at line 3271.
- [CRITICAL] chapters/frame/guide_to_main_results.tex:240 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 281, before the next claim at line 285.
- [CRITICAL] chapters/frame/guide_to_main_results.tex:298 — PROBLEM: `\ClaimStatusProvedHere` remark has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 318; the file currently leaves this claim surface proofless.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:1183 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1193, before the next claim at line 1222.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:1407 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1419, before the next claim at line 1429.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:1429 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1437, before the next claim at line 1454.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:1577 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1583, before the next claim at line 1715.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:1773 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1786, before the next claim at line 1813.
- [CRITICAL] chapters/frame/heisenberg_frame.tex:4820 — PROBLEM: `\ClaimStatusProvedHere` computation has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 4902; the file currently leaves this claim surface proofless.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_curved.tex:4408 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 4416, before the next claim at line 4418.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_curved.tex:4418 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 4432, before the next claim at line 4434.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_curved.tex:6651 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 6663, before the next claim at line 6665.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_curved.tex:6883 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 6888, before the next claim at line 6890.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_curved.tex:6941 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 6954, before the next claim at line 6956.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_inversion.tex:1611 — PROBLEM: `\ClaimStatusProvedHere` theorem has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1677, before the next claim at line 1680.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_inversion.tex:6046 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 6054, before the next claim at line 6069.
codex
I’ve located the main pressure points. The file already contains one local repair relevant to finding 3 (`lem:filtered-comparison-unit`), so now I’m checking whether the theorem statements and proofs later in the file still advertise the older, incorrect coalgebra-level Verdier claim or overstate scope.
exec
/bin/zsh -lc "sed -n '3688,3810p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
G_\cA(t) \;=\; H_\cA(t) - G_\cA(t)\,H_\cA(t).
\]
Extracting the coefficient of $t^q$ gives
$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
follows by induction on~$q$.
\end{proof}

\begin{remark}[The primitive defect as a Koszulness probe]
\label{rem:primitive-defect-probe}
\index{primitive defect series!Koszulness probe}

For a quadratic chiral algebra $\cA$ with generators of
weights $d_1, \ldots, d_s$, the PBW basis ensures that all
quasi-primaries are generated by the declared strong generators,
so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
exec
/bin/zsh -lc "sed -n '80,130p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1310,1395p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2598,2635p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2638,2695p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{convention}[Bar coalgebra and Koszul dual algebra]
\label{conv:bar-coalgebra-identity}
\index{bar construction!as Koszul dual coalgebra|textbf}
\index{Koszul dual!coalgebra vs.\ algebra|textbf}
The bar construction $\barB_X(\cA)$ of an augmented chiral
algebra~$\cA$ is a dg factorization \emph{coalgebra} on
$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
of~$\cA$: the bar complex is not a tool for computing the dual,
it \emph{is} the dual.

When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
separate object: it has generators $\mathcal{V}^\vee =
\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
relations~$R^\perp$ (orthogonal complement under the residue
pairing). In the classical setting (algebras on a point),
$\cA^!$ is the graded linear dual of the concentrated bar
coalgebra. In the chiral setting, $\cA^!$ is characterized by
Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
 succeeded in 51ms:
\subsection{Verdier duality on bar and cobar}


\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
\label{thm:verdier-bar-cobar}
\index{Verdier duality!bar-cobar|textbf}
\textup{[Regime: quadratic, genus-$0$
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
Koszul dual.

There is a perfect pairing:
\[\langle \cdot, \cdot \rangle: \bar{B}^{\text{ch}}_n(\mathcal{A}) \otimes 
\Omega^{\text{ch}}_n(\mathcal{A}^!) \to \mathbb{C}\]

given by:
\[\langle \omega_{\text{bar}}, K_{\text{cobar}} \rangle = \int_{\overline{C}_n(X)} 
\omega_{\text{bar}} \wedge \iota^* K_{\text{cobar}}\]

 succeeded in 52ms:
tower terminates at depth~$3$ because $S_r = 0$ for $r \geq 4$.
For class~$C$\textup{:}
the cubic shadow vanishes by weight parity of the $\gamma$
generator \textup{(}conformal weight~$0$\textup{)}, while the
quartic contact invariant
$Q^{\mathrm{contact}} \neq 0$ from the
$\beta\gamma\beta\gamma$ self-contraction; rank-one rigidity of
the contact stratum kills all $m_k^{\mathrm{SC}}$ for $k \geq 5$.
For class~$M$\textup{:}
the quartic pole in the Virasoro OPE
\textup{(}$T_{(3)}T = c/2$\textup{)} produces $S_3 = 2$
\textup{(}$c$-independent\textup{)} and the critical discriminant
$\Delta = 8\kappa S_4 \neq 0$ forces all higher operations to be
nonzero.
\end{proposition}

\begin{proof}
Class~$G$: for Heisenberg, centrality of the bracket kills all nested
compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
 succeeded in 51ms:
Computational verification:
\texttt{theorem\_ainfty\_nonformality\_class\_m\_engine.py}
(three independent methods for $S_3$,
quartic shadow $S_4$ and $Q^{\mathrm{contact}}$, quintic
shadow $S_5 = -48/(c^2(5c+22))$, all four classes verified).
\end{proof}

The four classes exhaust the standard landscape, but the
relationship between SC-formality and the classification is
sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
already isolates the first nonzero Swiss-cheese operation in each
non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
formality criterion to a classification check.

\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1370,1420p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1370	\begin{proof}
  1371	Forward: $E_2$-collapse concentrates $H^*(\barBgeom(\cA))$ on
  1372	the diagonal $p = q$; since the bar resolution computes Ext,
  1373	$\operatorname{Ext}^{p,q}(\omega_X, \omega_X) = 0$ for
  1374	$p \neq q$.
  1375	Converse: diagonal concentration forces all PBW differentials
  1376	$d_r$ ($r \geq 2$) to vanish, since a $d_r$-differential shifts
  1377	the bigrading by $(r, 1-r)$, producing off-diagonal classes
  1378	that contradict~$\operatorname{Ext}^{p,q} = 0$ for $p \neq q$.
  1379	Hence $E_2$-collapse, hence Koszulness.
  1380	\end{proof}
  1381	
  1382	\begin{proposition}[PBW universality; \ClaimStatusProvedHere]
  1383	\label{prop:pbw-universality}
  1384	\index{Koszul property!PBW universality}
  1385	\index{vertex algebra!freely strongly generated}
  1386	
  1387	A vertex algebra~$\cA$ is \emph{freely strongly generated} if it
  1388	admits strong generators $\{a^i\}_{i \in I}$ whose normally ordered
  1389	monomials


thinking
**Verifying proof presence near flagged claims**

I'm checking line 1390 which the audit flagged as missing proof, but I see proof starting at line 1398, so numbering shifts might explain the confusion. I notice a corollary right after with no proof, likely the first issue. Next, I plan to inspect claims around line 2663 and others to pinpoint the 7 audit-flagged problems in the chiral_koszul_pairs file, aiming to list exact labels and line numbers for each.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2645,2695p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2645	The four classes exhaust the standard landscape, but the
  2646	relationship between SC-formality and the classification is
  2647	sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
  2648	already isolates the first nonzero Swiss-cheese operation in each
  2649	non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
  2650	class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
  2651	nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
  2652	formality criterion to a classification check.
  2653	
  2654	\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
  2655	\label{prop:sc-formal-iff-class-g}
  2656	\index{Swiss-cheese operad!formality characterisation}
  2657	\index{class G@class~$G$!characterised by SC-formality}
  2658	Let~$\cA$ be a chiral algebra in the standard landscape.
  2659	Then~$\cA$ is Swiss-cheese formal
  2660	\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
  2661	if and only if~$\cA$ belongs to class~$G$.
  2662	\end{proposition}
  2663	
  2664	\begin{proof}

thinking
**Exploring theorem conditions**

I need to dig deeper into the equivalences and conditions of the theorem, particularly focused on points (vii) and (viii). It seems like there's more to explore after 2005. I might want to look for relevant lines or references, maybe around line 2065 or so, to open things up for a better understanding. Let’s see where this leads and what new insights I can find!
exec
/bin/zsh -lc "sed -n '2065,2145p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\operatorname{Ext}^{p,q}_\cA(\omega_X, \omega_X) = 0$ for
 $p \neq q$.
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
exec
/bin/zsh -lc "rg -n \"lattice-postnikov-termination|lattice:koszul-morphism|class~\\\\"'$G'"\\\\"'$|Heisenberg, lattice VOA|Gaussian" chapters/theory/chiral_koszul_pairs.tex chapters/examples -g '"'*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"condition~\\\\textup\\{\\(vii\\)\\}|condition~\\\\textup\\{\\(viii\\)\\}|Hochschild|free polynomial|Etwo-formality|polynomial Hilbert|uniform-weight lane|all-genera concentration\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
67:$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
1216:Hochschild consequence on the Koszul locus, one conditional on
2040:On the uniform-weight lane, condition~\textup{(vii)} strengthens to
2041:the all-genera concentration statement recorded there and remains
2044:them on the Koszul locus: it yields Hochschild duality,
2045:polynomial Hilbert series, and $\Etwo$-formality, but it does not
2076: If $\cA$ lies on the uniform-weight lane, then for every smooth
2093:\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
2101: with Hochschild--Hilbert series
2154:\textsc{Hochschild consequence}
2160:bar-cobar resolution with the chiral Hochschild complex. On the
2165:cohomological concentration, duality, polynomial Hilbert series,
2215:by PBW collapse. If $\cA$ lies on the uniform-weight lane, the same
2231:the uniform-weight lane.
2248:On the uniform-weight lane, Theorem~\ref{thm:loop-order-collapse}
2264:\begin{remark}[The strongest proved Hochschild consequence]
2266:polynomial Hilbert series, and $\Etwo$-formality. It does not imply
2933:The nine unconditional equivalences and the Hochschild
3229:and the Hochschild consequence~\textup{(viii)} no longer follows.
4425:\item Formal smoothness $\Rightarrow$ Hochschild cohomology controls deformations
 succeeded in 53ms:
chapters/theory/chiral_koszul_pairs.tex:2535:\item Class~$G$ (Gaussian, $r_{\max}=2$): tree-level exact.
chapters/theory/chiral_koszul_pairs.tex:2564:& Heisenberg, lattice VOA
chapters/theory/chiral_koszul_pairs.tex:2590:Gaussian: the Heisenberg bracket
chapters/theory/chiral_koszul_pairs.tex:2593:Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
chapters/theory/chiral_koszul_pairs.tex:2617:VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
chapters/theory/chiral_koszul_pairs.tex:2649:non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
chapters/theory/chiral_koszul_pairs.tex:2674:non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
chapters/theory/chiral_koszul_pairs.tex:2953:(Theorem~\textup{\ref{thm:lattice:koszul-morphism}}) for
chapters/theory/chiral_koszul_pairs.tex:3034:Theorem~\ref{thm:lattice:koszul-morphism};
chapters/theory/chiral_koszul_pairs.tex:3148:Heisenberg & $2$ (finite) & Gaussian \\
chapters/examples/w_algebras_deep.tex:3766:\item \emph{Gaussian} (Heisenberg, lattice VOA, free fermion):
chapters/examples/w_algebras_deep.tex:5123:G & $2$ & $Y_{0,0,0}$, $Y_{0,0,1}$, $Y_{1,1,1}$ & free/Gaussian \\
chapters/examples/w_algebras_deep.tex:5133:Gaussian. This confirms that shadow depth classifies complexity
chapters/examples/w_algebras_deep.tex:5404:$c = 9$, while the Heisenberg channels remain Gaussian.
chapters/examples/symmetric_orbifolds.tex:507:leading non-Gaussian correction to the saddle-point
chapters/examples/lattice_foundations.tex:225:the Heisenberg Fredholm determinant is the Gaussian
chapters/examples/lattice_foundations.tex:228:$V_\Lambda$ has depth~$r_{\max} = 2$ (Gaussian archetype) and
chapters/examples/lattice_foundations.tex:927:The bar-cobar QI follows from Theorem~\ref{thm:lattice:koszul-morphism}: the twisting morphism $\tau$ is Koszul, so $\Omega^{\mathrm{ch}}(\barBgeom(\Vlat_\Lambda)) \xrightarrow{\sim} \Vlat_\Lambda$.
chapters/examples/lattice_foundations.tex:994:\label{thm:lattice:koszul-morphism}
chapters/examples/lattice_foundations.tex:1702:Part~(ii) follows from the Gaussian class characterization:
thinking
**Verifying proof presence across flagged lines**

I’m reviewing flagged lines where missing proofs were reported to see if the audit is outdated or still accurate. I already found proof at line 2663, so I'm turning to check near lines 3438 and onwards to confirm which claims really lack proof. This careful line inspection will clarify the real status of all flagged sections.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3420,3560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3420	 genus-$0$ OPE data.
  3421	\item The shadow depth $r_{\max}(\cA)$ equals the bootstrap
  3422	 closure order: the number of OPE channels at which the
  3423	 crossing equation
  3424	 $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at degree
  3425	 $n = 4$ is satisfied.
  3426	\item The shadow depth classification corresponds to bootstrap
  3427	 complexity:
  3428	 class~$G$ has no OPE corrections beyond leading order,
  3429	 class~$L$ has one cubic correction
  3430	 \textup{(}the pentagon identity\textup{)},
  3431	 class~$C$ terminates at the quartic,
  3432	 class~$M$ requires the infinite tower.
  3433	\end{enumerate}
  3434	The MC equation at $(g{=}0, n{=}4)$ is the crossing equation
  3435	for the four-point function.
  3436	\end{theorem}
  3437	
  3438	\begin{proof}
  3439	(i) By $A_\infty$~formality

thinking
**Exploring proof justification**

I need to continue the proof section starting around 2145 to better understand how (vii) and (viii) are justified. I'm curious about the details and whether there are clear explanations for these sections. It feels important that I clarify any uncertainties I might have. I want to ensure that the reasoning is solid and that I'm not missing anything crucial! So, let’s dive into those next parts to gain clarity.
exec
/bin/zsh -lc "sed -n '2145,2275p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\smallskip\noindent
\textup{(v)}$\Rightarrow$\textup{(i)}:
The bar-cobar counit being a quasi-isomorphism means the
twisted tensor product $K_\tau^L$ is acyclic
(Lemma~\ref{lem:twisted-product-cone-counit}), which is
condition~(1) of
Definition~\ref{def:chiral-koszul-morphism}.

\medskip
\textsc{Hochschild consequence}
\textup{(v)}$\Rightarrow$\textup{(viii)}:

\smallskip\noindent
The quasi-isomorphism
$\Omega(\barBgeom(\cA)) \xrightarrow{\sim} \cA$ identifies the
bar-cobar resolution with the chiral Hochschild complex. On the
Koszul locus, Theorem~H,
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild} give the stated
exec
/bin/zsh -lc "sed -n '2260,2295p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2920,3045p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
strengthening of \textup{(vii)} fails. The sharpened statement is
therefore optimal.
\end{remark}

\begin{remark}[The strongest proved Hochschild consequence]
The strengthened form of \textup{(viii)} stops at duality,
polynomial Hilbert series, and $\Etwo$-formality. It does not imply
that the underlying graded-commutative algebra
$\ChirHoch^*(\cA)$ is free. At generic central charge,
Theorem~\ref{thm:virasoro-hochschild} gives
\[
\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
\]
The degree-$2$ class squares to zero because
$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
graded-commutative algebra on a degree-$2$ generator would have
nonzero degree~$4$. Thus vanishing of higher braces and Massey
products is the strongest proved consequence; ordinary cup-product
relations may remain.
\end{remark}
 succeeded in 52ms:
incompatible with purity of the associated $\cD$-module.
As for Virasoro, condition~(ii) holds but
condition~(xii) is strictly stronger.

\emph{$\cW_N$ at principal nilpotent, generic central
charge} \textup{(}class~$\mathbf{M}$\textup{):}
\begin{conjecture}[Principal $\cW_N$ equivalence on the
generic locus; \ClaimStatusConjectured]
\label{conj:d-module-purity-wn-principal}
Let $\cW_N^k$ be the universal principal $\cW$-algebra
obtained from $V_k(\mathfrak{sl}_N)$ by principal
Drinfeld--Sokolov reduction, at generic central charge.
On the generic locus of the FM configuration space,
condition~(ii) of
Theorem~\ref{thm:koszul-equivalences-meta} is equivalent
to condition~(xii), conditional on the preservation of
Saito weights under principal Drinfeld--Sokolov reduction.
\end{conjecture}
The conditional hypothesis is the conjectured compatibility
of the principal nilpotent BRST differential with the


thinking
**Analyzing claim proofs and dependencies**

I'm carefully reviewing flagged claims that lack proofs or have questionable proof status, focusing on their labels and line ranges. I'll check if the best fix is adding a proof, removing a claim status, or adjusting theorem statuses, especially for definitions that might not require proof. Since dependencies like bar and cobar constructions might hold relevant lemmas or references, I'll look into those files and lines to identify how they could support fixes in chiral_koszul_pairs.tex.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '60,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    60	\end{tabular}
    61	\end{center}
    62	
    63	\noindent
    64	Theorem~\ref{thm:bar-nilpotency-complete} assembles these three
    65	components into the full genus-$0$ differential $\dzero$
    66	and proves $\dzero^2 = 0$; the key input is the Arnold relation
    67	(Theorem~\ref{thm:arnold-three},
    68	Remark~\ref{rem:costello-gwilliam-factorization}).
    69	
    70	\smallskip
    71	\noindent\textit{Notation.}
    72	Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
    73	
    74	\medskip
    75	
    76	\begin{convention}[Set notation and ordering]\label{conv:set-notation}
    77	Throughout this chapter: collision divisors are $D_{ij}$ with $i < j$ (indices in increasing order); the hat notation $\widehat{ij}$ denotes \emph{omission} of both factors $\phi_i$ and $\phi_j$ after applying the OPE (we write $\widehat{ij}$ for the collision pattern itself, and $\widehat{\phi_i, \phi_j}$ when listing omitted terms in a tensor product).
    78	\end{convention}
    79	
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1320,1385p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1320	$d_{\mathrm{curvature}}$
  1321	(Proposition~\ref{prop:pole-decomposition});
  1322	at genus~$\geq 1$ it acquires a topological component
  1323	$m_0 = \kappa \cdot \omega_g$
  1324	(Chapter~\ref{chap:higher-genus}).
  1325	\end{example}
  1326	
  1327	\begin{example}[\texorpdfstring{$\beta\gamma$}{beta-gamma} system at degree 1]\label{ex:betagamma-deg1}
  1328	For the $\beta\gamma$ system with generators $\beta(z), \gamma(z)$ and OPE:
  1329	\[\beta(z)\gamma(w) = \frac{1}{z-w} + \text{regular}, \quad \beta(z)\beta(w) = 0, \quad \gamma(z)\gamma(w) = 0\]
  1330	
  1331	\emph{Bar degree 1.}
  1332	\[\bar{B}^1(\mathcal{FG}) = \text{span}\{\beta \otimes \beta \otimes \eta, \beta \otimes \gamma \otimes \eta, \gamma \otimes \beta \otimes \eta, \gamma \otimes \gamma \otimes \eta\}\]
  1333	
  1334	\emph{Differential.} Only the $\beta \otimes \gamma$ term contributes:
  1335	\begin{align*}
  1336	d(\beta \otimes \gamma \otimes \eta_{12}) &= \text{Res}_{D_{12}}\bigl[\mu(\beta, \gamma) \otimes \eta_{12}\bigr] \\
  1337	&= \bigl[\text{Res}_{\epsilon=0}\,\eta_{12}\bigr] \cdot \mu(\beta, \gamma)\big|_{z_1=z_2}
  1338	\end{align*}
  1339	Setting $\epsilon = z_1 - z_2$, the propagator is $\eta_{12} = d\epsilon/\epsilon$, which has $\text{Res}_{\epsilon=0}[d\epsilon/\epsilon] = 1$. The chiral product $\mu(\beta, \gamma)$ extracts the simple-pole OPE coefficient $\beta(z)\gamma(w) \sim 1/(z-w)$, giving $\mathbb{1}$ (the unit element). Hence $d(\beta \otimes \gamma \otimes \eta_{12}) = \mathbb{1}$.
thinking
**Investigating class G contradictions**

I'm finding an interesting table related to the free fermion class G, but it seems it's not in the proposition. The user has noted that there are 7 mentions of lattice VOA class assignments that contradict each other in the tables. I think I should inspect the tables closely, particularly around the ones noted, like 3015 or 3148. I'll need to search for class G and see what I can find, maybe opening around 3138.
exec
/bin/zsh -lc "sed -n '3128,3160p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\cA^{\mathrm{sh}}_{r,g} = 0$ for $r \geq 3$, $g = 0$.
\item The bar spectral sequence
 $E_1^{p,q} = H^q(F^p\gAmod/F^{p+1}\gAmod)$ degenerates
 at~$E_2$.
\item The genus-$0$ convolution algebra
 $\mathfrak{g}^{(0)}_\cA$ is formal as a dg Lie algebra.
\end{enumerate}
These three conditions are equivalent to each other and to the ten
unconditional equivalences~\textup{(i)--(x)} in
Theorem~\textup{\ref{thm:koszul-equivalences-meta}}.
\end{proposition}

\begin{proof}
Condition~(i) states $\cA^{\mathrm{sh}}_{r,0} = 0$ for $r \geq 3$,
i.e.\ all genus-$0$ obstruction classes
$o_{r+1}^{(0)}(\cA) = 0$ for $r \geq 2$. This is the PBW
concentration condition~(ii) of
Theorem~\ref{thm:koszul-equivalences-meta}, establishing
(i)$\Leftrightarrow$(ii).
Condition~(ii) (bar spectral sequence $E_2$-collapse) is the same
exec
/bin/zsh -lc "rg -n \"Free fermion|free fermion|lattice VOA|lattice &|Class~\\\\"'$G'"\\\\"'$|class~'"\\\\"'$G'"\\\\"'$ row" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2998,3040p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1639:$W(2)$ embeds into the lattice VOA~$V_{2\mathbb{Z}}$ as the
2564:& Heisenberg, lattice VOA, free fermion
2590:Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
2626:For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
2629:shadow tower with its weight-$2$ truncation. For the free fermion,
2693:lattice VOA, and free fermion, and in each case the genus-$0$
2983:free fermion, and the symplectic fermion
2987:lattice VOAs, MC4 completion tower
3016:Free fermion $\psi$
3048:$V_{D_4}$ lattice VOA
3049: & lattice & $28$ & Proved & lattice filt.\ & $G$, $r_{\max}=2$ \\
5600:For free-field algebras (Heisenberg, free fermion), the
5887:free fermion chiral algebra on two generators. The direct sum
5932:to DG chiral algebras, with the free fermion and $(\beta\gamma \oplus bc,
 succeeded in 52ms:
\centering
\caption{Koszulness landscape: 17 algebras}
\label{tab:koszulness-landscape}
\index{Koszul property!landscape table}
\index{Koszul property!universal vs.\ simple quotient}
\smallskip
{\small
\begin{tabular}{@{}llccll@{}}
\toprule
\textbf{Algebra} & \textbf{Type}
 & \textbf{Gens} & \textbf{Status}
 & \textbf{Mechanism} & \textbf{Shadow} \\
\midrule
\multicolumn{6}{@{}l}{\textit{Free fields}} \\[2pt]
Heisenberg $\cH_k$
 & free field & $1$ & Proved & PBW univ.\ & $G$, $r_{\max}=2$ \\
$\beta\gamma$ ($\lambda{=}1$)
 & free field & $2$ & Proved & PBW univ.\ & $C$, $r_{\max}=4$ \\
Free fermion $\psi$
 & free field & $1$ & Proved & PBW univ.\ & $G$, $r_{\max}=2$ \\
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '60,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    60	
    61	\begin{remark}[Three functors on the bar coalgebra: cobar is NOT the Koszul dual]
    62	\label{rem:cobar-three-functors}
    63	Before entering the construction, we fix a critical distinction that
    64	pervades the chapter. Three functors act on the bar coalgebra
    65	$\barB(\cA)$, producing three different objects; confusing any two
    66	produces false statements.
    67	\begin{enumerate}[label=\textup{(\roman*)}]
    68	\item \emph{Cobar / bar-cobar inversion}
    69	 (Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}):
    70	 \[\Omegach(\barB(\cA)) \;\xrightarrow{\sim}\; \cA\qquad
    71	 \text{(recovers $\cA$ itself: a round-trip, not a duality)}.\]
    72	\item \emph{Verdier duality on $\operatorname{Ran}(X)$}
    73	 (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
    74	 \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
    75	 (\cA)^!_\infty\qquad
    76	 \text{(gives the homotopy Koszul dual factorization algebra)}.\]
    77	\item \emph{Chiral derived centre / Hochschild cochains}
    78	 (Theorem~H):
    79	 \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
exec
/bin/zsh -lc 'rg -n "filtered-comparison" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 347

metadata/dependency_graph.dot:2249:  lem_complete_filtered_comparison [label="lem:complete-filtered-comparison\nlemma [Pr]\nComplete filtered comparison lemma", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2399:  lem_filtered_comparison [label="lem:filtered-comparison\nlemma [Pr]\nFiltered comparison", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2400:  lem_filtered_comparison_unit [label="lem:filtered-comparison-unit\nlemma [Pr]\nBar-side filtered comparison", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:260:| `lem:complete-filtered-comparison` | `lemma` | 2391 | Complete filtered comparison lemma |
metadata/theorem_registry.md:395:| `lem:filtered-comparison` | `lemma` | 333 | Filtered comparison |
metadata/theorem_registry.md:396:| `lem:filtered-comparison-unit` | `lemma` | 361 | Bar-side filtered comparison |
metadata/label_index.json:24554:  "lem:complete-filtered-comparison": {
metadata/label_index.json:24654:  "lem:filtered-comparison": {
metadata/label_index.json:24658:  "lem:filtered-comparison-unit": {
metadata/label_index.json:31334:  "rem:complete-filtered-comparison-role": {
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:3:- [CRITICAL] `chapters/theory/chiral_koszul_pairs.tex:451` — PROBLEM: The implication `(\ref{ftm:counit})\Rightarrow(\ref{ftm:koszul})` in `thm:fundamental-twisting-morphisms` uses `lem:filtered-comparison` and `lem:filtered-comparison-unit`, but those lemmas require an exhaustive, complete, bounded-below filtration (`:335-336`, `:363-365`). A “chiral twisting datum” only gives an exhaustive bounded-below filtration (`:212-214`), and the proof then invokes Definition `def:chiral-koszul-morphism` condition 3 (`:456-457`) while trying to prove that very condition. FIX: strengthen the theorem hypothesis at `:407-410` to require the filtrations on `\cA,\cC,\bar B_X(\cA),\Omega_X(\cC)` to be exhaustive, complete, bounded below, and strongly convergent, then delete the circular appeal at `:456-457`.
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:857:chapters/theory/chiral_koszul_pairs.tex:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:870:chapters/theory/chiral_koszul_pairs.tex:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:1025:The mapping-cone lemmas don’t define their maps and depend on "bar-type resolution" without verifying the chiral differential decomposition. Plus, the filtered-comparison theorems claim a equivalence without proving it previously in the document. I need to investigate if there's a theorem confirming that bar commutes with the associated graded.
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:1081:I noticed that the only instance of the bar commuting with the associated graded appears in the lemma of the filtered-comparison-unit proof. It seems like this hasn't been proven in other contexts, which could mean it’s an unsupported assertion. I think I should search in other files to see if there's a relevant theorem that might help clarify or support this observation. Let's explore this more thoroughly!
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:1202:- [CRITICAL] `chapters/theory/chiral_koszul_pairs.tex:451` — PROBLEM: The implication `(\ref{ftm:counit})\Rightarrow(\ref{ftm:koszul})` in `thm:fundamental-twisting-morphisms` uses `lem:filtered-comparison` and `lem:filtered-comparison-unit`, but those lemmas require an exhaustive, complete, bounded-below filtration (`:335-336`, `:363-365`). A “chiral twisting datum” only gives an exhaustive bounded-below filtration (`:212-214`), and the proof then invokes Definition `def:chiral-koszul-morphism` condition 3 (`:456-457`) while trying to prove that very condition. FIX: strengthen the theorem hypothesis at `:407-410` to require the filtrations on `\cA,\cC,\bar B_X(\cA),\Omega_X(\cC)` to be exhaustive, complete, bounded below, and strongly convergent, then delete the circular appeal at `:456-457`.
wave2_audit_20260413_001942/C06_chiral_koszul_pairs.md:258:| `lem:filtered-comparison` | `lemma` | 314 | Filtered comparison |
wave2_audit_20260413_001942/C06_chiral_koszul_pairs.md:674:452:By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$

thinking
**Examining the code snippet**

I’m looking at the interesting lines, especially around line 2564, which already include the free fermion concept. I wonder if the earlier proposition snippet only showcased the Heisenberg model and lattice VOA. I think I need to check lines 2558-2632 since it might include additional information after edits. I did notice that table line at 2564 could be part of the output snippet but may be cut off due to token count limitations. Let's investigate that section!
exec
/bin/zsh -lc "sed -n '2558,2632p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
& \textbf{Families}
& $m_3^{\mathrm{SC}}$
& $m_4^{\mathrm{SC}}$
& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
\midrule
$G$ \textup{(}$r_{\max}=2$\textup{)}
& Heisenberg, lattice VOA, free fermion
& $= 0$
& $= 0$
& $= 0$ \\
$L$ \textup{(}$r_{\max}=3$\textup{)}
& affine KM
& $\neq 0$
& $= 0$
& $= 0$ \\
$C$ \textup{(}$r_{\max}=4$\textup{)}
& $\beta\gamma$
& $= 0$
& $\neq 0$
& $= 0$ \\
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '300,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   300	as $d_\cA + d_\cC + d_\tau^L$. The $d_\tau^L$ component acts as
   301	the cobar differential on the $\cC$-factor and as the
   302	$\varepsilon_\tau$-induced augmentation on the $\cA$-factor.
   303	The resulting complex is exactly the mapping cone of
   304	$\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ shifted by~$[-1]$:
   305	the rows of the double complex are
   306	$\cA \leftarrow \cA \otimes \cC \leftarrow \cA \otimes \cC^{\otimes 2}
   307	\leftarrow \cdots$, which is the bar-type resolution of the
   308	augmentation map. This is the chiral analogue of
   309	\cite[Lemma~2.2.5]{LV12}.
   310	\end{proof}
   311	
   312	\begin{lemma}[Right twisted tensor product as mapping cone; \ClaimStatusProvedHere]
   313	\label{lem:twisted-product-cone-unit}
   314	\index{twisted tensor product!mapping cone}
   315	Under the same hypotheses, there is a natural identification
   316	\[
   317	K_\tau^R(\cC,\cA) \;\simeq\; \operatorname{Cone}(\eta_\tau)[-1]
   318	\]
   319	where $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is the canonical
exec
/bin/zsh -lc "sed -n '2632,2698p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$r \geq 3$ survives after extracting the binary pairings. In all three
cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
lift of the same genus-$0$ tree sum whose closed projection is
$S_r(\cA)$; equivalently,
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
the mixed-sector operations vanish:
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
The weaker condition $\Delta = 0$ is not sufficient:
affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
$m_3^{\mathrm{SC}} \neq 0$.
Class~$L$: the cubic shadow
$S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
ratio (the structure constant divided by the level); the quartic
and higher shadows vanish because the Jacobi identity and rank
constraints eliminate all $\overline{\cM}_{0,r+1}$ tree sums for
$r \geq 4$ when the OPE has at most double poles.
Class~$C$: the cubic shadow vanishes by the parity obstruction on
the weight-$0$ generator~$\gamma$; the quartic contact invariant
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '420,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   420	$(\cA, \cC, \tau, F_\bullet)$
   421	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum})},
   422	the following are equivalent:
   423	\begin{enumerate}[label=\textup{(\roman*)}]
   424	\item\label{ftm:koszul}
   425	 $\tau$ is a chiral Koszul morphism
   426	 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
   427	\item\label{ftm:counit}
   428	 The canonical counit
   429	 $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$
   430	 is a quasi-isomorphism.
   431	\item\label{ftm:unit}
   432	 The canonical unit
   433	 $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$
   434	 is a weak equivalence of conilpotent complete factorization
   435	 coalgebras.
   436	\item\label{ftm:acyclic}
   437	 Both twisted tensor products $K_\tau^L(\cA,\cC)$ and
   438	 $K_\tau^R(\cC,\cA)$ are acyclic.
   439	\end{enumerate}
exec
/bin/zsh -lc "sed -n '2698,2728p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Then the mixed sector of the Swiss-cheese bar complex is formal:
every higher arity tree operation vanishes. The tower-bar
correspondence is operadic: the arity-$r$ mixed tree and the
degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
formula, with the same propagator on internal edges; the only
difference is the output colour, and passage to the symmetric
closed sector applies the averaging morphism
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
there is no higher mixed tree whose closed projection could survive.
By Theorem~\ref{thm:shadow-formality-identification} and
Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
the statement that the shadow/formality tower truncates at
degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
identifies the standard-landscape locus with this property as
precisely class~$G$. Hence an SC-formal algebra must belong
to class~$G$.
\end{proof}

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '190,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   190	\subsection{Construction layer: twisting data}
   191	
   192	To recognize Koszulness, we need to compare a chiral algebra with
   193	its bar coalgebra. The bridge between them is a \emph{twisting morphism},
   194	a degree-$+1$ map satisfying a Maurer--Cartan equation, and
   195	to ensure convergence of the resulting spectral sequences, we need a
   196	compatible filtration. The Koszul property is then a
   197	\emph{recognition criterion} on these data, not a prerequisite for
   198	their existence.
   199	
   200	\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
   201	\index{twisting datum!chiral|textbf}
   202	A \emph{chiral twisting datum} on a smooth curve $X$ is a quadruple
   203	$(\cA, \cC, \tau, F_\bullet)$ consisting of:
   204	\begin{enumerate}
   205	\item an augmented chiral algebra
   206	 $\cA \in \operatorname{Fact}^{\mathrm{aug}}(X)$;
   207	\item a conilpotent complete factorization coalgebra
   208	 $\cC \in \operatorname{CoFact}^{\mathrm{conil,comp}}(X)$;
   209	\item a degree $+1$ morphism


thinking
**Verifying seven specific findings in foundation**

I'm double-checking the exact seven findings the user wants investigated by closely examining line references in the foundation file around the noted section, confirming whether all related claims and proofs are present or if some remain unproven or outdated. I'll also search for mentions of the chiral_koszul_pairs.tex to ensure I have the complete set of findings to review.
exec
/bin/zsh -lc 'rg -n "chapters/theory/chiral_koszul_pairs.tex" foundation_audit_chapters_report.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
252:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1390 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1412, before the next claim at line 1414.
253:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2663 — PROBLEM: `\ClaimStatusProvedHere` proposition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2674, before the next claim at line 2683.
254:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3438 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3458, before the next claim at line 3460.
255:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3460 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3480, before the next claim at line 3482.
256:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3482 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3500, before the next claim at line 3502.
257:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3502 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3520, before the next claim at line 3522.
258:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:3522 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3545, before the next claim at line 3547.


thinking
**Verifying modifications**

I’m noticing that the file may already have some fixes, but I need to check what modifications are still necessary. The user mentioned that line numbering might be shifted, so I’ll have to verify each one. It looks like theorem A is consistent at the algebra level, and I’ll need to find proof around line 584. There’s a mention of chiral koszul pairs that needs clarification on Verdier compatibility at the algebra level. I'll carefully analyze the proof and definitions.
thinking
**Inspecting theorem proofs**

I’m considering whether the definition and surrounding remarks are already sufficient, but I want to inspect lines 651 and 679 as they could potentially be consistent. The user asked for strong, truthful fixes, so if the current file is already corrected from previous changes, we might not need edits. However, I need to systematically review all references. There may be some residual inconsistencies that I need to resolve, particularly in the remarks about Verdier duality and the theorem statement at line 3724, which appears to be correct.
thinking
**Verifying findings and adjustments**

I think the file may already have some fixes, but since the user wants to verify each finding, I won't skip any checks. I need to ensure any inconsistent text in the assigned file is addressed, especially if it's related to the findings. A careful audit is essential to get everything right, so I'll wait for the explorer results to help guide my adjustments and ensure that nothing slips through the cracks.
collab wait(call_sxDR9DqtZwSIykIQFn59dexA)
  receivers: 019d8674-a520-7521-b075-690f36a93455
exec
/bin/zsh -lc "rg -n \"label\\{thm\" -n chapters/theory/chiral_koszul_pairs.tex | sed -n '330,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

wait(call_sxDR9DqtZwSIykIQFn59dexA) timed out:
exec
/bin/zsh -lc "rg -n \"label\\{thm\" chapters/theory/chiral_koszul_pairs.tex | grep -n 'shadow'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc 'rg -n "shadow" chapters/theory/chiral_koszul_pairs.tex | head' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
41:complex, and it does not detect the shadow obstruction tower
66:$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
76:classes G/L/C/M, with shadow depths
78:(Theorem~\ref{thm:shadow-archetype-classification}), record the
79:degree at which the shadow obstruction tower first becomes
91:Confusing the two misidentifies what the shadow tower measures.
115:vanishing controls termination of the shadow obstruction tower
1213:The shadow obstruction tower probes all genera; Koszulness constrains only
1288:(Proposition~\ref{prop:shadow-formality-low-degree}). On each fiber,
1297:\begin{remark}[$A_\infty$ products as genus-$0$ shadows]
thinking
**Searching for theorem relations**

I’m still running the agent, so let’s continue. I need to search for the exact relationship in the dependency theorem and consider using `rg` for the nonexistent lemma. We’ve already found the local lemma exists. The user asked whether to write or cite the correct existing result. It seems I might have already written the lemma, but maybe the theorem proof will still cite "bar-degree analogue of Lemma filtered-comparison" somewhere. So I need to search for that exact phrase.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3340,3445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3340	the PBW spectral sequence.
  3341	
  3342	The classical $r$-matrix
  3343	$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
  3344	$\cA = \widehat{\fg}_k$ defines a Sklyanin--Poisson bracket on
  3345	$(\fg^!)^*$ via the Semenov-Tian-Shansky
  3346	construction~\cite{STS83}. The infinitesimal rigidity of this
  3347	bracket (vanishing of its second Poisson cohomology) turns out to
  3348	be equivalent to chiral Koszulness for the affine family.
  3349	
  3350	\begin{theorem}[Koszulness from Sklyanin--Poisson rigidity;
  3351	\ClaimStatusProvedHere{} for affine KM]
  3352	\label{thm:koszulness-from-sklyanin}
  3353	\index{Koszul property!Sklyanin Poisson rigidity|textbf}
  3354	\index{Poisson cohomology!vanishing|textbf}
  3355	\index{Whitehead's second lemma!application to Poisson rigidity}
  3356	
  3357	For $\cA = \widehat{\fg}_k$ with $\fg$ semisimple, the
  3358	Sklyanin--Poisson bracket
  3359	$\{-,-\}_{\mathrm{STS}}$ on $(\fg^!)^*$ determined by the classical
codex
The target file has already absorbed part of the needed repair: the missing bar-side comparison lemma exists locally now, and the class-`G` discussion already names free fermions in the main classification block. I’m now checking for older residual wording elsewhere in the same file so the theorem surface, remarks, and proof lanes all agree.
exec
/bin/zsh -lc "rg -n \"bar-degree analogue|analogue of Lemma filtered-comparison|factorization algebra, not a coalgebra|bar coalgebra of one side|dual factorization algebra|D_Ran\\(|\\\\mathbb\\{D\\}_\\{\\\\operatorname\\{Ran\\}\\}\\\\(\\\\cC_\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,725p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:bar-degree analogue|analogue of Lemma filtered-comparison|factorization algebra, not a coalgebra|bar coalgebra of one side|dual factorization algebra|D_Ran\(|\mathbb\{D\}_\{\operatorname\{Ran\}\}\(\cC_)
                                                                                                                                                                     ^^
error: unrecognized escape sequence
 succeeded in 53ms:

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
/bin/zsh -lc "sed -n '3890,3950p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"class-\\"'$G'"\\"'$ row consists exactly|trilinear form built from'"\\\\~\\\\kappa|C\\(x,y,z\\)|free fermion\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proposition}

\begin{proof}
Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
statement to a compatible relative unit/counit package. Applying
$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
map and then pulling back to a geometric fiber $X_s$ gives, by
hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
fiber. The displayed relative Verdier identifications provide the
algebra target on the total space, and hypothesis~\textup{(a)} is the
exact condition needed to take Verdier duals degreewise in the
relative holonomic category. These ingredients glue the fiberwise
identifications over~$S$. The specialization
$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
argument to the universal curve.
\end{proof}

\begin{remark}[Programme for the modular-family extension]
 exited 2 in 53ms:
rg: regex parse error:
    (?:class-$G$ row consists exactly|trilinear form built from\~\kappa|C\(x,y,z\)|free fermion)
                                                                 ^^
error: unrecognized escape sequence
codex
The theorem statement itself is already algebra-level, but there are still nearby explanatory blocks that need harmonization with it. I’m now patching those residual places rather than broadening the edit surface.
exec
/bin/zsh -lc 'rg -n -F "class-$G$ row consists" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n -F "trilinear form built from" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "bar coalgebra of one side" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "free fermion" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 50ms:
569: dual pair, Verdier duality sends the bar coalgebra of one side
3949:part~(2) says Verdier duality sends the bar coalgebra of one side
 succeeded in 51ms:
2564:& Heisenberg, lattice VOA, free fermion
2590:Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
2629:shadow tower with its weight-$2$ truncation. For the free fermion,
2693:lattice VOA, and free fermion, and in each case the genus-$0$
2983:free fermion, and the symplectic fermion
5600:For free-field algebras (Heisenberg, free fermion), the
5887:free fermion chiral algebra on two generators. The direct sum
5932:to DG chiral algebras, with the free fermion and $(\beta\gamma \oplus bc,
exec
/bin/zsh -lc "sed -n '3940,3965p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Twisting morphism content of Theorem~A]
\label{rem:theorem-a-tau}
\index{twisting morphism!Theorem A content}
The unit $\eta_{\tau_i} \colon \cC_i \to \barB_X(\cA_i)$ and
counit $\varepsilon_{\tau_i} \colon \Omega_X(\cC_i) \to \cA_i$
in part~(1) are induced by the Koszul morphism~$\tau_i$
of the underlying twisting datum
(Definition~\ref{def:chiral-twisting-datum}).
Part~(1) says each~$\tau_i$ is acyclic;
part~(2) says Verdier duality sends the bar coalgebra of one side
to the dual factorization algebra recovered from the other;
and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
the extra relative Verdier/base-change input needed to transport
these identifications over a base.
\end{remark}

\begin{remark}[Elementary model presentation;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-a-model}
\index{bar-cobar duality!model presentation}


thinking
**Verifying file consistency**

Okay, the current file looks to be fixed, which is great! Now, I need to verify whether the status tags and the introduction to the theorem are consistent. I'm thinking I should check some lines around 1216 and 2933, where it mentions "nine unconditional equivalences" and similar details. It's important that everything aligns nicely, so I'll take a closer look to ensure accuracy. Can't overlook those bits!
exec
/bin/zsh -lc "sed -n '1188,1238p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"all-genera concentration|nine unconditional equivalences|Hochschild consequence|free polynomial|underlying graded-commutative algebra.*free|condition~\\\\textup\\{\\(viii\\)\\}|genus-0 clause of condition~\\\\textup\\{\\(vii\\)\\}\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"free polynomial algebra|polynomial algebra|\\bfree\\b.*Hochschild|ChirHoch\\"'^'"\\*.*free\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Acyclicity of $K_\tau^L$ and $K_\tau^R$ upgrades this map from a
graded comparison to a coalgebra isomorphism
(the chiral analogue of \cite[Theorem~2.3.1]{LV12}; the
identical argument applies because acyclicity of the Koszul
complexes is the only input beyond the MC equation, and both
hold in the chiral setting by
Lemma~\ref{lem:bar-holonomicity} and
Theorem~\ref{thm:fundamental-twisting-morphisms}).
\end{proof}

%%% ---------------------------------------------------------------
%%% INTRINSIC CHARACTERIZATIONS OF CHIRAL KOSZULNESS
%%% ---------------------------------------------------------------

\subsection{Intrinsic characterizations of chiral Koszulness}
\label{sec:intrinsic-characterizations-koszulness}
\index{Koszul property!intrinsic characterizations}
\index{MC element!genus-0 formality}

The MC element $\Theta_\cA \in \MC(\mathfrak{g}_\cA^{\mathrm{mod}})$
 succeeded in 52ms:
1216:Hochschild consequence on the Koszul locus, one conditional on
2041:the all-genera concentration statement recorded there and remains
2046:force the underlying graded-commutative algebra to be free.
2093:\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
2154:\textsc{Hochschild consequence}
2264:\begin{remark}[The strongest proved Hochschild consequence]
2966:The nine unconditional equivalences and the Hochschild
3262:and the Hochschild consequence~\textup{(viii)} no longer follows.
3288:Each of the nine unconditional equivalences
 succeeded in 53ms:
838:For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
873:This is a polynomial algebra on the generators
876:polynomial algebras are Koszul, with Koszul dual the
923:is a polynomial algebra (the OPE reduces to a commutative
1309:\index{truncated polynomial algebra!$A_\infty$ dual}
2268:$\ChirHoch^*(\cA)$ is free. At generic central charge,
4117: graded is the polynomial algebra $\mathrm{Sym}(V)$ with

thinking
**Clarifying theorem status**

I think a local high-level summary would be sufficient. The theorem's status is still ClaimStatusProvedHere, which is fine because it includes a stronger claim with lane and equivalence, as well as a one-way consequence. So there’s no issue with the status. I need to check if the labels are valid, likely yes. Also, I want to inspect finding 6, since the user mentions a converse proof that uses a bilinear form. I should search for C(x,y,z) in the file.
exec
/bin/zsh -lc 'rg -n -F "C(x,y,z)" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Searching for theorem references**

I’m considering if the user is discussing theorem A relating to algebra after D_Ran. It seems I might need to reference theorem A to confirm the identification of the bar coalgebra. But I wonder if that connection is valid. To clarify, I'll search for all mentions of "Theorem\ref{thm:bar-cobar-isomorphism-main} identifies the bar coalgebra" in the file to see what comes up. That's definitely a good next step!
exec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:bar-cobar-isomorphism-main} identifies the bar coalgebra\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc 'rg -n -F "identifies the bar coalgebra" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3973:\simeq \cA$. Verdier duality identifies the bar coalgebra with the

thinking
**Reviewing flagged theorem and definition claims**

I'll inspect each of the seven flagged entries one by one, verifying if proofs exist or if the flagged issues are outdated. For those definitions incorrectly marked as proved claims, I'll consider recommending removing or reclassifying their statuses. I'll also check relevant dependencies like bar/cobar constructions and filtered comparison lemmas to provide context and propose precise fixes or status updates for each finding.
thinking
**Preparing detailed bullet list for each flagged finding**

I’m organizing the final response as a clear bullet list covering each of the seven flagged lines with exact labels, line ranges, dependency summaries, proposed fixes, and status updates, carefully referencing relevant lemmas and remarks as context. This will ensure clarity and meet all the user’s formatting and detail instructions.
thinking
**Summarizing dependencies and proposing status updates**

I’m wrapping up the detailed notes on each flagged item by tying in the relevant dependencies like bar/cobar constructions and the filtered comparison lemmas, explaining exactly what those dependencies prove and why status changes or fixes should be applied—especially reclassifying definitions and confirming proofs for theorems and propositions where appropriate.
exec
/bin/zsh -lc "sed -n '3968,3982p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
\,:\! \boldsymbol{\Omega}_X
\]
on the stable $\infty$-category of factorization (co)algebras on
$\operatorname{Ran}(X)$. On the Koszul locus, the unit and counit
are equivalences: $\boldsymbol{\Omega}_X \mathbf{B}_X(\cA)
\simeq \cA$. Verdier duality identifies the bar coalgebra with the
homotopy dual factorization algebra via
$\mathbb{D}_{\operatorname{Ran}} \mathbf{B}_X(\cA) \simeq
(\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
theorem; what follows are
presentations.

\emph{Step~B} (M-level):
The explicit dg model uses the reduced bar complex
$\bar{B}_X(\cA) = (T^c(s^{-1}\bar{\cA}),\, d_{\mathrm{bar}})$,
codex
Checked each of the seven “missing-proof” findings from `foundation_audit_chapters_report.md` against the live `chapters/theory/chiral_koszul_pairs.tex` surface, after reading the requested dependency sections (`chapters/theory/bar_construction.tex#L80-L105`, `chapters/theory/bar_construction.tex#L1347-L1369`, `chapters/theory/cobar_construction.tex#L61-L125`) and the filtered comparison lemmas (`chapters/theory/chiral_koszul_pairs.tex#L332-L409`). Here is the per‑finding report you asked for:

- **Finding 1 — `cor:universal-koszul` (lines 1407‑1419 aka `chapters/theory/chiral_koszul_pairs.tex#L1407-L1419`).**  
  *Dependency:* Proposition `prop:pbw-universality` (lines 1382‑1405) immediately covers any algebra that is freely strongly generated, and `bar_construction.tex#L80-L105` fixes the meaning of the symmetric bar coalgebra we use in that Proposition (so there is no conflation between ordered vs. factorization bar).  
  *Fix:* Add a short proof invoking `prop:pbw-universality`: each universal algebra is freely strongly generated (affine KM via the Chevalley generators, Virasoro via the Virasoro field plus descendants, `\mathcal{W}^k(\fg)` via the Feigin–Frenkel/Miura argument stated in the corollary) and thus chirally Koszul. Mention the quoted external results and the fact that the bar in scope is the Koszul dual coalgebra (per the bar construction reminder).  
  *Status change:* Keep `\ClaimStatusProvedHere`; the new proof will close the audit comment.

- **Finding 2 — `prop:sc-formal-iff-class-g` (lines 2654‑2683 / `chapters/theory/chiral_koszul_pairs.tex#L2654-L2683`).**  
  *Dependency:* `prop:swiss-cheese-nonformality-by-class` (earlier in the chapter) identifies the first non‑zero Swiss‑cheese operation in each class, so the converse (SC‑formal ⇒ class G) follows immediately by elimination.  
  *Fix:* None needed—the proof already begins at line 2664 and explicitly cites `prop:swiss-cheese-nonformality-by-class` to rule out classes L, C, M. The audit entry is out of date.  
  *Status change:* None.

- **Finding 3 — `thm:koszulness-bootstrap` (line 3443 with adjacent proof lines 3438‑3466 / `chapters/theory/chiral_koszul_pairs.tex#L3438-L3466`).**  
  *Dependency:* Item (iii) of `thm:koszul-equivalences-meta` grants $m_k=0$ for $k\geq3$ on the Koszul locus; Lemma `lem:nms-euler-inversion` (used at lines 3449‑3451) translates the shadow obstruction to the MC equation; the class table (after line 3458) ties the vanishing pattern of the $S_r$’s to G/L/C/M.  
  *Fix:* Already proved in lines 3438‑3466, so the “missing proof” flag is obsolete.  
  *Status change:* None.

- **Finding 4 — `thm:koszulness-bootstrap` (same theorem, lines 3458‑3466, flagged again at line 3460).**  
  *Dependency & fix:* Same as Finding 3; the proof shows all three bullet points and the classification argument there, so no new correction is necessary.  
  *Status change:* None.

- **Finding 5 — `prop:minimal-model-non-koszul` (lines 3468‑3505 / `chapters/theory/chiral_koszul_pairs.tex#L3468-L3505`).**  
  *Dependency:* The counting argument relies on standard partition counts for Virasoro Verma modules (see the bar‑cohomology example in `bar_construction.tex#L1347-L1369`, which explains why $\dim H^2$ counts quadratic relations).  
  *Fix:* Proof already present (lines 3491‑3504) and shows the null vector removes one generator from $\barB^1$ while leaving $\barB^2$ unchanged, forcing $H^2\neq0$.  
  *Status change:* None.

- **Finding 6 — same proposition’s numeric illustration (line 3502).**  
  *Dependency & fix:* The same Euler‑characteristic argument proves the “gap” exposed at line 3502 (Ising example) and closes the audit; nothing additional needs to change.  
  *Status change:* None.

- **Finding 7 — definitions of the primitive cumulant quotient and generating series (lines 3523‑3559 / `chapters/theory/chiral_koszul_pairs.tex#L3523-L3559`).**  
  *Dependency:* These definitions rely on the injectivity of $\partial$ at positive weights (invoked via `thm:kac-shapovalov-koszulness` and on the Kac–Shapovalov determinant hypothesis in line 3533).  
  *Fix:* Drop the `\ClaimStatusProvedHere` wrapper for both definitions (or replace it with a definition‑level status) since no proof exists or is required. No additional mathematical content is needed.  
  *Status change:* Reclassify these surfaces as definitions rather than proved claims, so the audit no longer complains about missing proofs.

I confirm that the filtered‑comparison lemmas (`lem:filtered-comparison` and `lem:filtered-comparison-unit`) already provide the necessary strong‑convergence arguments for the spectral sequences used elsewhere in this part of the chapter (they guarantee the associated graded twisting datum is classical, so the chiral Koszul condition reduces to the familiar LV12 picture).




thinking
**Refining theorem details**

I think the wording is pretty good, but maybe I should update line 569 to "Verdier duality, applied to the bar coalgebra, sends it to..." I also need to check if the theorem proof part (2) should cite thm:verdier-bar-cobar. Right now, it uses the definition of a pair plus part (1). The user seems to indicate that proof imports Verdier compatibility as a definition rather than deriving it. However, since the theorem's hypothesis includes this, it may not be necessary to derive it explicitly.
thinking
**Enhancing proof clarity**

I could add a sentence in the proof: "For the standard pairs in Definition ref, this hypothesis comes from thm:verdier-bar-cobar, which associates D_Ran(barB_X(\cA_i)) with the factorization algebra Omega_X(\cC_j)." This might address the finding 2 concern. I also need to clarify the definition of chiral Koszul pair or standard construction and add more explicit "post-Verdier" wording. Additionally, I should remark on line 568 that it’s "after applying D_Ran to the bar coalgebra" to clear up any confusion.
thinking
**Adjusting theorem details**

If the proof of theorem A uses the definition of a pair, it might be okay, but since the user explicitly requested a fix, I should adjust the definition's "Standard construction" to cite the theorem. I could explain that "algebra-level Verdier compatibility is provided by thm:verdier-bar-cobar after applying D_Ran to the bar coalgebra." I think I’m almost there, and I can rephrase to be more explicit. It seems finding 3 might already be resolved.
thinking
**Addressing theorem A inconsistencies**

I need to mention that it's been "already resolved in the file," and there's verified confirmation that no further changes are needed. However, they seem to be asking after each edit, which is okay. Still, I might want to check for any residual inconsistencies around theorem A to patch up. I plan to search for the wording that could imply coalgebra equivalence, focusing on terms like `bar coalgebra` with theorem A references. I've already noted some findings and should search broader.
exec
/bin/zsh -lc 'rg -n "Verdier duality sends|Verdier duality identifies|homotopy Koszul dual|bar coalgebra|dual factorization algebra|algebra-level Verdier" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
52:homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
193:its bar coalgebra. The bridge between them is a \emph{twisting morphism},
382:bar structure, the associated graded bar coalgebra is canonically
569: dual pair, Verdier duality sends the bar coalgebra of one side
570: to the dual factorization algebra of the other.
679:algebra-level Verdier compatibility
710:the bar coalgebra
1307:\begin{example}[Truncated polynomials: the homotopy Koszul dual off the Koszul locus]
1331:(Lu--Palmieri--Wu--Zhang \cite{LPWZ09}). The homotopy Koszul dual
3553:of the completed bar coalgebra, independently of any curvature
3603:\index{bar coalgebra!reduced-weight window}
3645:\index{bar coalgebra!exponential growth rate}
3693:determines \emph{how large} the completed bar coalgebra is
3750:The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
3782:\item the homotopy Koszul dual factorization algebras are
3850:together with relative algebra-level Verdier identifications,
3898:hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
3920: relative Ran space, lift the algebra-level Verdier-compatible pair
3949:part~(2) says Verdier duality sends the bar coalgebra of one side
3950:to the dual factorization algebra recovered from the other;
exec
/bin/zsh -lc "sed -n '700,715p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{example}[Heisenberg specialization]\label{ex:heisenberg-koszul-pair}
For the Heisenberg algebra $\mathcal{H}_k$ at level $k \neq 0$,
Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$,
where $\mathcal{H}_k$ is $\chirLie$-type (generated by a single
bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
the bar coalgebra
$\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
whose linear dual is the Koszul dual algebra
$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by


thinking
**Evaluating theorem clarity**

I’m considering whether this example needs adjustment. The sentence "Theorem A identifies the bar coalgebra..." is misleading because theorem A doesn't directly make that identification; frame sections might instead. The user focuses on the relationship between algebra and coalgebra, so attributing the example to theorem A could confuse things. To resolve any inconsistencies, it would be helpful to modify the example, stating it more clearly with the Verdier dual identification. Minimal but truthful changes are the goal!
thinking
**Refining the example**

I can adjust the example to state: "The bar coalgebra \barB(H_k) was computed explicitly as coLie^ch(V^*); Theorem A then identifies its Verdier dual factorization algebra with the Koszul dual algebra \mathcal H_k^! = Sym^ch(V^*)." This harmonizes the concepts. I'll inspect line 52, as it seems to suggest that theorem A connects \barB with the homotopy dual factorization algebra. Searching around lines 46-57 should clarify everything to make sure it all aligns well!
exec
/bin/zsh -lc "sed -n '40,60p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Koszul: it does not see the genus corrections in the bar
complex, and it does not detect the shadow obstruction tower
whose depth varies from two to infinity across the standard
families.

The bar-cobar adjunction of Theorem~A
(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
functorial pair that resolves all three obstructions. It is the
unique adjunction that (a)~inverts on the Koszul locus, producing
$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
H^*(\overline{\mathcal{M}}_g, Z(\cA))$
(Theorem~\ref{thm:quantum-complementarity-main}).
No other functorial construction achieves all three: the operadic
adjunction achieves (a) but not (b) or (c); Verdier duality alone
achieves (b) but has no bar-cobar content; complementarity (c)
requires both (a) and (b) as input.

thinking
**Considering edits and proofs**

It's alright! I might need to focus on line 193 and look into some edits for the example. I could also think about decomposing the remarks, proof of the theorem, and defining standards for the construction. I should pay special attention to something like the remark on theorem-a-tau. It seems I should wait for the explorer to finish up for now, but I feel ready to make these adjustments!
collab wait(call_EzdmwBQTKy71XduiFgwdyQEU)
  receivers: 019d8674-a520-7521-b075-690f36a93455
wait(call_EzdmwBQTKy71XduiFgwdyQEU) 1 agents complete:
  019d8674-a520-7521-b075-690f36a93455 completed: "Checked each of the seven “missing-proof” findings from `foundation_audit_chapters_report.md` against the live `chapters…"
codex
Pre-edit verification for the Theorem A surface:

```text
surface: chapters/theory/chiral_koszul_pairs.tex, Theorem A + nearby explanatory remarks/examples
four objects:
1. B(A) = bar coalgebra
2. A^i = H^*(B(A)) = dual coalgebra
3. A^! = Verdier/linear dual algebra
4. Z^der_ch(A) = Hochschild bulk
Verdier target in this edit: D_Ran(B(A)) as factorization algebra, not B(A) as coalgebra
theorem scope/status: unchanged; ClaimStatusProvedHere remains accurate
residual inconsistency found: nearby prose still says “Verdier duality sends the bar coalgebra...” without explicitly naming the post-D_Ran algebra target
verdict: ACCEPT
```

I’m making a narrow coherence edit now: theorem-adjacent remarks, the standard-construction paragraph, the Heisenberg example, and the Theorem A proof will all say the same thing about the Verdier output.

thinking
**Inspecting code for patches**

I need to apply a patch, but I realize I should focus on the exact context since line breaks might be different. There’s this chunk in the code I want to inspect carefully. I'll pay special attention to the relevant sections around lines 670-690 and also lines 704-714, including the theorem proof lines. By examining these specifics, I can ensure that the patch fits correctly. Let's get into the details!
codex
The first patch missed exact local line breaks. I’m re-reading the target snippets and applying the same content with tighter context so the edit stays strictly local.
exec
/bin/zsh -lc "sed -n '700,720p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '560,690p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{example}[Heisenberg specialization]\label{ex:heisenberg-koszul-pair}
For the Heisenberg algebra $\mathcal{H}_k$ at level $k \neq 0$,
Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$,
where $\mathcal{H}_k$ is $\chirLie$-type (generated by a single
bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
the bar coalgebra
$\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
whose linear dual is the Koszul dual algebra
$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
producing exactly the commutative Koszul dual
(\S\ref{sec:frame-koszul-dual}).
Because $\mathcal{H}_k$ is abelian, the PBW spectral sequence
 succeeded in 51ms:
 twisting datum, Koszulity $\Leftrightarrow$ counit qi
 $\Leftrightarrow$ unit we $\Leftrightarrow$ twisted tensor
 products acyclic.
\item \emph{$\mathrm{A}_1$}: bar concentration
 (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
 $H^i(\bar{B}^{\mathrm{ch}}(\cA)) = 0$ for $i \neq 0$ and
 $H^0 \cong \cC$.
\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
 dual pair, Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra of the other.
\end{itemize}
$\mathrm{A}_0$ is the Koszul recognition theorem;
$\mathrm{A}_1$ extracts the dual coalgebra;
$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
\end{remark}

\begin{proposition}[Universal property of bar construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]
\label{prop:bar-universal-property}
\index{bar construction!universal property}
exec
/bin/zsh -lc "sed -n '3770,3798p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3942,3954p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Let $(\cA_1, \cC_1, \tau_1, F_\bullet)$ and
$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
Then:
\begin{enumerate}
\item the canonical units and counits are quasi-isomorphisms:
\[
\cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
\Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
\qquad (i = 1, 2);
\]

\item the homotopy Koszul dual factorization algebras are
 identified with the opposite member of the pair:
\[
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
\simeq \Omega_X(\cC_2) \simeq \cA_2, \qquad
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_2)
\simeq \Omega_X(\cC_1) \simeq \cA_1;
\]
 succeeded in 51ms:
\index{twisting morphism!Theorem A content}
The unit $\eta_{\tau_i} \colon \cC_i \to \barB_X(\cA_i)$ and
counit $\varepsilon_{\tau_i} \colon \Omega_X(\cC_i) \to \cA_i$
in part~(1) are induced by the Koszul morphism~$\tau_i$
of the underlying twisting datum
(Definition~\ref{def:chiral-twisting-datum}).
Part~(1) says each~$\tau_i$ is acyclic;
part~(2) says Verdier duality sends the bar coalgebra of one side
to the dual factorization algebra recovered from the other;
and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
the extra relative Verdier/base-change input needed to transport
these identifications over a base.
\end{remark}
exec
/bin/zsh -lc "sed -n '3798,3825p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{theorem}

\begin{proof}
Part~(1) is the fundamental theorem of chiral twisting morphisms
(Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
conditions
(Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
the unit and counit being quasi-isomorphisms.
For part~(2), the Verdier compatibility in
Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
factorization algebra $\Omega_X(\cC_2)$, and likewise with the
indices reversed. Let
\[
\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
\qquad
\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
\]
be the unit and counit equivalences from part~(1). Applying
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -568,4 +568,4 @@
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
@@ -683,3 +683,5 @@
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
@@ -708,7 +710,8 @@
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
@@ -3810,3 +3813,5 @@
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
@@ -3948,4 +3953,5 @@
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
apply_patch(auto_approved=true) exited 0 in 43ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.

codex
The local patch is in. I’m re-reading the modified theorem surface and the adjacent examples/remarks to confirm the Verdier story is uniformly “bar coalgebra before `D_Ran`, factorization algebra after `D_Ran`,” and that I didn’t disturb the already-repaired scope results for `(vii)` and `(viii)`.
exec
/bin/zsh -lc "sed -n '560,690p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,720p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

\begin{proposition}[Universal property of bar construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]
\label{prop:bar-universal-property}
\index{bar construction!universal property}
 succeeded in 51ms:
\end{definition}


\begin{example}[Heisenberg specialization]\label{ex:heisenberg-koszul-pair}
For the Heisenberg algebra $\mathcal{H}_k$ at level $k \neq 0$,
Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$,
where $\mathcal{H}_k$ is $\chirLie$-type (generated by a single
bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
The explicit bar computation gives the bar coalgebra
$\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
coalgebra identifies its Verdier dual factorization algebra with the
Koszul dual algebra
$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
exec
/bin/zsh -lc "sed -n '2038,2108p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3942,3954p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3798,3825p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2558,2718p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
On the uniform-weight lane, condition~\textup{(vii)} strengthens to
the all-genera concentration statement recorded there and remains
equivalent to them.
Condition~\textup{(viii)} is a proved one-way consequence of
them on the Koszul locus: it yields Hochschild duality,
polynomial Hilbert series, and $\Etwo$-formality, but it does not
force the underlying graded-commutative algebra to be free.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
 succeeded in 50ms:
the Lagrangian from its groupoid algebra.
\end{remark}

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
 succeeded in 51ms:
(\cA_2)^!_\infty := \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_2)
\simeq \cA_2^!.
\]
\end{enumerate}
\end{theorem}

\begin{proof}
Part~(1) is the fundamental theorem of chiral twisting morphisms
(Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
conditions
(Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
the unit and counit being quasi-isomorphisms.
For part~(2), the Verdier compatibility in
Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
factorization algebra $\Omega_X(\cC_2)$, and likewise with the
indices reversed. In the standard examples, this hypothesis is
supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
lives on the post-Verdier factorization-algebra side. Let
\[
 succeeded in 50ms:
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Class}
& \textbf{Families}
& $m_3^{\mathrm{SC}}$
& $m_4^{\mathrm{SC}}$
& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
\midrule
$G$ \textup{(}$r_{\max}=2$\textup{)}
& Heisenberg, lattice VOA, free fermion
& $= 0$
& $= 0$
& $= 0$ \\
$L$ \textup{(}$r_{\max}=3$\textup{)}
& affine KM
& $\neq 0$
& $= 0$
& $= 0$ \\
$C$ \textup{(}$r_{\max}=4$\textup{)}
& $\beta\gamma$
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.


thinking
**Verifying references and phrases**

I think everything looks good, but I might need to run a check for any problematic phrases or verify that no line references are broken. I should search for "Verdier duality sends the bar coalgebra" on theorem-a—perhaps something changed there. Also, looking for the theorem proof and remarks could be helpful, so I'll try searching for those exact phrases too. It's all about ensuring everything aligns correctly!
codex
The reread is clean on the edited surface. I’m doing one last grep pass for the old misleading theorem-A phrasing and then I’ll close with a finding-by-finding disposition, including the items that were already repaired in the live file before this pass.
exec
/bin/zsh -lc 'rg -n -F "factorization algebra, not a coalgebra" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Verdier duality sends the bar coalgebra" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F "free polynomial" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index ff230b2..fba5941 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@ duality theorem:
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@ algebra-level Verdier compatibility
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.




thinking
**Evaluating git changes**

I’m looking at the git diff, and it shows more changes than our patch. It’s important to note that some diff sections refer to prior modifications from before this session. We need to be cautious and clarify that certain findings were already resolved in the current file, not by our patch. The diff shows pre-existing changes, and since the worktree is dirty, we won’t revert anything. I’ll verify that we acknowledged findings already resolved in the live file.
thinking
**Exploring git verification**

I'm considering if I should use `git diff --stat`, but it might not be necessary. I need to verify that old phrases are no longer present, and a search shows no results. I might run a command to check references, but I think all `\ref` and `\label` commands are untouched. Since I only changed text, there shouldn't be any new labels. I could run a TeX compile for verification, but following the user's request, I'm focusing on specific edits. Running a lightweight compile could be beneficial.
thinking
**Considering document verification**

I think running a targeted syntax parser might be better since I only made text edits and no changes to labels. However, for the strongest local verification, a minimal compile of the document could be useful. I can run `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, but it might take some time. I notice the instructions specify to edit only specific files, so I should remember that compiling doesn’t modify files besides generating build artifacts. I'll have to consider that carefully!
collab close_agent(call_uetyuP60DWyyBLr4PRybKbRe)
  receiver: 019d8674-a520-7521-b075-690f36a93455
close_agent(call_uetyuP60DWyyBLr4PRybKbRe) completed: "Checked each of the seven “missing-proof” findings from `foundation_audit_chapters_report.md` against the live `chapters…":
  receiver: 019d8674-a520-7521-b075-690f36a93455
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.


thinking
**Considering line numbers for edits**

I’m thinking I might use update_plan, although it may not be necessary in the end. It could still be helpful to gather line numbers for edits to reference in the final product. I’ll use `nl -ba` around relevant sections to get those line numbers. I should also collect line numbers for existing resolved findings, like vii/viii and class G, so I can cite the same file accurately. Let’s get those exact line numbers for patched sections!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '564,690p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   564	 (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
   565	 $H^i(\bar{B}^{\mathrm{ch}}(\cA)) = 0$ for $i \neq 0$ and
   566	 $H^0 \cong \cC$.
   567	\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
   568	 (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
   569	 dual pair, applying Verdier duality to the bar coalgebra of one side
   570	 produces the dual factorization algebra of the other.
   571	\end{itemize}
   572	$\mathrm{A}_0$ is the Koszul recognition theorem;
   573	$\mathrm{A}_1$ extracts the dual coalgebra;
   574	$\mathrm{A}_2$ links two Koszul data via Verdier geometry.
   575	\end{remark}
   576	
   577	\begin{proposition}[Universal property of bar construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]
   578	\label{prop:bar-universal-property}
   579	\index{bar construction!universal property}
   580	For any augmented chiral algebra~$\cA$, the bar construction
   581	$\barB_X(\cA)$ together with its canonical twisting morphism
   582	$\tau_{\mathrm{can}} \colon \barB_X(\cA) \to \cA$
   583	is initial among pairs $(C, \tau)$ consisting of a conilpotent chiral
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2558,2715p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3804,3956p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '700,716p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2038,2108p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2558	\begin{tabular}{@{}lcccc@{}}
  2559	\toprule
  2560	\textbf{Class}
  2561	& \textbf{Families}
  2562	& $m_3^{\mathrm{SC}}$
  2563	& $m_4^{\mathrm{SC}}$
  2564	& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
  2565	\midrule
  2566	$G$ \textup{(}$r_{\max}=2$\textup{)}
  2567	& Heisenberg, lattice VOA, free fermion
  2568	& $= 0$
  2569	& $= 0$
  2570	& $= 0$ \\
  2571	$L$ \textup{(}$r_{\max}=3$\textup{)}
  2572	& affine KM
  2573	& $\neq 0$
  2574	& $= 0$
  2575	& $= 0$ \\
  2576	$C$ \textup{(}$r_{\max}=4$\textup{)}
  2577	& $\beta\gamma$
 succeeded in 51ms:
  2038	
  2039	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  2040	with PBW filtration $F_\bullet$.
  2041	Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
  2042	genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
  2043	On the uniform-weight lane, condition~\textup{(vii)} strengthens to
  2044	the all-genera concentration statement recorded there and remains
  2045	equivalent to them.
  2046	Condition~\textup{(viii)} is a proved one-way consequence of
  2047	them on the Koszul locus: it yields Hochschild duality,
  2048	polynomial Hilbert series, and $\Etwo$-formality, but it does not
  2049	force the underlying graded-commutative algebra to be free.
  2050	Under the additional perfectness and non-degeneracy hypotheses on the
  2051	ambient tangent complex, condition~\textup{(xi)} is also equivalent to
  2052	them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  2053	(Remark~\ref{rem:d-module-purity-content}); the converse is open.
  2054	
  2055	\smallskip
  2056	\noindent\textbf{Unconditional equivalences:}
  2057	\begin{enumerate}
 succeeded in 53ms:
  3804	\begin{proof}
  3805	Part~(1) is the fundamental theorem of chiral twisting morphisms
  3806	(Theorem~\ref{thm:fundamental-twisting-morphisms}): the Koszulness
  3807	conditions
  3808	(Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
  3809	the unit and counit being quasi-isomorphisms.
  3810	For part~(2), the Verdier compatibility in
  3811	Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
  3812	Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
  3813	factorization algebra $\Omega_X(\cC_2)$, and likewise with the
  3814	indices reversed. In the standard examples, this hypothesis is
  3815	supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
  3816	lives on the post-Verdier factorization-algebra side. Let
  3817	\[
  3818	\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
  3819	\qquad
  3820	\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
  3821	\]
  3822	be the unit and counit equivalences from part~(1). Applying
  3823	$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
 succeeded in 53ms:
   700	\end{definition}
   701	
   702	
   703	\begin{example}[Heisenberg specialization]\label{ex:heisenberg-koszul-pair}
   704	For the Heisenberg algebra $\mathcal{H}_k$ at level $k \neq 0$,
   705	Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
   706	$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$,
   707	where $\mathcal{H}_k$ is $\chirLie$-type (generated by a single
   708	bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
   709	and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
   710	chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
   711	The explicit bar computation gives the bar coalgebra
   712	$\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
   713	\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
   714	Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
   715	coalgebra identifies its Verdier dual factorization algebra with the
   716	Koszul dual algebra
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.

codex
Edited [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:567) to make the Theorem A Verdier lane uniformly algebra-level after `\mathbb{D}_{\operatorname{Ran}}`: the decomposition remark, the standard-construction paragraph, the Heisenberg example, the main proof, and the theorem-A content remark now all distinguish `\barB_X(\cA)` as the bar coalgebra from `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` as the resulting factorization algebra.

I then re-read the other flagged surfaces in the same file and verified they are already repaired on the live surface: the bar-side filtered comparison lemma exists and is cited, `(vii)` is only genus-`0` unconditionally with the all-genera version restricted to the uniform-weight lane, `(viii)` is only a one-way Hochschild consequence, and the SC-formality/class-`G` discussion now covers Heisenberg, lattice VOA, and free fermion without the invalid `\kappa`-trilinear argument. I did not run a full TeX build; verification was by local reread and grep, and I did not change any labels.

## Rectification Summary
- [FIXED] finding 1 — harmonized Theorem A’s Verdier wording so the bar object stays a coalgebra and the post-`\mathbb{D}_{\operatorname{Ran}}` object is always a factorization algebra.
- [FIXED] finding 2 — clarified that the standard-example Verdier input comes from `thm:verdier-bar-cobar` on the algebra side after applying `\mathbb{D}_{\operatorname{Ran}}`, not from a coalgebra identification.
- [FIXED] finding 3 — verified the missing “bar-side filtered comparison” is already present as `lem:filtered-comparison-unit`, and the theorem proof uses that correct local result.
- [NARROWED] finding 4 — verified `(vii)` is already narrowed to the genus-`0` clause unconditionally, with the all-genera strengthening kept only on the uniform-weight lane.
- [NARROWED] finding 5 — verified `(viii)` is already weakened to the proved one-way consequence: Hochschild duality, polynomial Hilbert series, and `\Etwo`-formality, without any free-polynomial claim.
- [FIXED] finding 6 — verified the converse SC-formality proof no longer uses the invalid `\kappa(x,[y,z])` construction and instead runs through shadow-tower truncation/classification.
- [FIXED] finding 7 — verified class `G` is now treated consistently and the forward implication covers the full class-`G` family listed there, including lattice VOA and free fermion.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -3808,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3946,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.

tokens used
115,313
