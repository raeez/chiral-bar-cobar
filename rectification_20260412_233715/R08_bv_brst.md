# R08_bv_brst (816s)

Updated [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:30) so the higher-genus BV/bar coderived lane is no longer overstated. The opening status prose, the class-by-class status remarks, the theorem at [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1881), and the two follow-up remarks now say exactly what is proved and what remains conditional.

I re-read the modified sections and checked that the new references point to existing coderived definitions/propositions. I also ran a quiet `latexmk`; it failed before reaching this chapter because `main.aux` is already malformed at an unrelated old write (`Proposition 9.7.5`), so I could not get a clean full-build confirmation from this tree.

## Rectification Summary
- [FIXED] finding 1 — removed the unsupported use of `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}` as if proved, and rewrote the surrounding prose to identify it explicitly as the missing class-`M` mechanism rather than established input.
- [CONDITIONAL] finding 1 — changed `thm:bv-bar-coderived` from `\ClaimStatusProvedHere` to `\ClaimStatusConditional`, with the theorem now conditional on the harmonic-factorization package plus the coderived weak-equivalence input.
- [FIXED] finding 2 — deleted the false coderived argument that treated `m_0\cdot x = d^2(x)` / `\operatorname{Im}(d)` as enough in `D^{\mathrm{co}}`, and replaced it with the correct coderived criterion via `def:curved-weak-equiv`, `def:provisional-coderived`, and `prop:provisional-embedding`.
- [NARROWED] finding 2 — narrowed the theorem from an unconditional coderived quasi-isomorphism for all chirally Koszul algebras to a conditional coderived comparison criterion: a higher-genus comparison map must be a weak equivalence, equivalently have coacyclic cone after passage to the coderived formalism.
- [FIXED] adjacent consistency issue — removed the local class-status overclaim in the nearby remarks and corrected the “free `\beta\gamma` = class G” slip inside the class-`C` discussion.


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
session id: 019d83a0-a0bb-7da1-a411-1d18909215d1
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


TARGET: chapters/connections/bv_brst.tex

FINDINGS TO FIX:

1. [CRITICAL T12] Line ~1932: Core class-M mechanism delta_r^harm = c_r(A)*m_0^{floor(r/2)-1}
   is introduced without proof or citation. This is the main engine of thm:bv-bar-coderived.
   FIX: Either prove this factorization (derive from the harmonic projection properties)
   or cite the source. If genuinely unproved: mark the coderived result as conditional on this mechanism.

2. [CRITICAL T12] Line ~1945: Proof treats m_0*x = d^2(x) in Im(d) as sufficient to kill
   the obstruction in D^co. But coderived category is Verdier quotient by coacyclic objects,
   not "boundaries mod Im(d)." The manuscript itself says curved objects are NOT zero in D^co.
   FIX: This is a genuine logical failure. Either reprove using the correct coderived
   characterization (coacyclic = totalizations of short exact sequences), or honestly
   downgrade the coderived result.

Read the file, verify both findings, make the strongest truthful fix.
mcp startup: no servers



thinking
**Considering coding tasks**

I need to operate as a coding agent in the repository, starting with reading mandatory files such as CLAUDE.md and others before making any substantial edits. It looks like “beilinson-rectify” is the relevant skill for this task, and I might also need "claim-surface-sync" if there's a change in theorem status. However, I can't edit other files unless assigned, so I’ll just focus on the target file. It might be useful to send a commentary update and plan before getting started.
thinking
**Exploring codebase needs**

I need to inspect the file along with other mandatory ones. Since this is a math repo, using an explorer agent might be preferable for codebase questions. The instructions emphasize that explorers are faster and more authoritative. I could use the explorer to quickly locate relevant sections and discussions about the theorem. However, maybe it's simpler to read manually with tools like rg/sed. I'll also consider parallelizing my reading with the multi_tool_use.parallel option while complying with all guidance.
thinking
**Planning execution strategy**

I can run multiple `exec_command` in parallel using multi_tool_use.parallel, which makes sense to consider for reading mandatory files. Tools like `rg` and `sed` could help, but I need to be careful about output truncation since I'll be reading limited sections. With the network restricted, web searches aren't relevant here. I should consider filling the Pre-Edit Verification Protocol because the focus is on theorem status and proof, even if it isn’t directly about a formula. This task really centers on editing the theorem and its proof.
codex
Using `beilinson-rectify` for a load-bearing proof repair in [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex). I’m first reading the mandated repo surfaces and the local theorem context so I can decide whether this can be strengthened or must be narrowed honestly.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 52ms:
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

 succeeded in 50ms:
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


thinking
**Investigating theorem files**

I need to read the exact target file related to the theorem. Maybe I should grep the theorem label and check for any conditional references. It could be useful to search for "delta_r^harm" in the repository to see if the source exists. I'll try using "rg" for that. Additionally, I might want to search for the "coderived" theorem label. Let's inspect the lines around the target. I'm curious to find out more!
codex
I’ve loaded the constitutional surfaces. Next I’m isolating the exact theorem block, its dependencies, and whether the missing class-M mechanism or coderived step is already proved elsewhere in this repo.
exec
/bin/zsh -lc "rg -n \"delta_r\\"'^'"\\{harm\\}|delta_r\\"'^harm|thm:bv-bar-coderived|coderived|coacyclic|harmonic projection|m_0'"\\"'^'"\\{|m_0\\"'^'"\\\\{|m_0\\*|d\\"'^2'"\\(x\\)\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1860,2015p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"delta_r\\"'^'"\\{harm\\}|delta_r\\"'^harm|c_r'"\\(A\\).*m_0|floor\\(r/2\\)-1|coderived|coacyclic|harmonic projection\" chapters | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
30:The two prescriptions are proved to match on the coderived category
31:for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
1838:not cancel it. However, in the coderived category
1841:and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
1842:$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
1844:$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
1848:(Theorem~\ref{thm:bv-bar-coderived}).
1895:the coderived category $D^{\mathrm{co}}$
1896:(Theorem~\ref{thm:bv-bar-coderived} below).
1902:\begin{theorem}[BV$=$bar in the coderived category;
1904:\label{thm:bv-bar-coderived}%
1905:\index{BV algebra!bar complex identification!coderived category|textbf}%
1906:\index{coderived category!BV/bar identification|textbf}%
1908:complex are quasi-isomorphic in the coderived category
1934: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
1941:so the chain-level quasi-isomorphism implies the coderived one
1945:in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
1952: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
1965:\label{rem:bv-bar-coderived-higher-genus}%
1966:\index{coderived category!higher-genus validity}%
 succeeded in 52ms:
modular convolution algebra~$\gAmod$: both contract a pair of
inputs through the Bergman kernel $d\log E(z,w)$ along the
non-separating boundary divisor
$\delta^{\mathrm{ns}}\colon
\overline{\mathcal{M}}_{g,n+2} \to
\overline{\mathcal{M}}_{g+1,n}$.
The identification is verified by four independent paths
(operator definition, spectral sequence, Heisenberg extraction,
modular operad) and has the following class-by-class status.
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lccl}
\toprule
Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
\midrule
$\mathsf{G}$ \textup{(}Heisenberg\textup{)}
 & $2$ & \textbf{unconditional} & no interaction vertices \\
$\mathsf{L}$ \textup{(}affine KM\textup{)}
 & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
 succeeded in 51ms:
chapters/examples/free_fields.tex:3684:\index{factorization homology!as Fourier integral}\index{homotopy transfer!Fourier interpretation}\index{coderived category!Fourier interpretation}
chapters/examples/landscape_census.tex:799:extension to the ordinary-derived/completed/coderived enlargement and
chapters/examples/landscape_census.tex:1435: ordinary-derived/completed/coderived enlargement, and then the
chapters/examples/kac_moody.tex:4141:adjunction's Verdier intertwining; and the coderived identification
chapters/examples/kac_moody.tex:4176:\begin{conjecture}[KL-II: coderived lift and semisimplified target;
chapters/examples/kac_moody.tex:4177:\ClaimStatusConjectured]\label{conj:kl-coderived}
chapters/examples/kac_moody.tex:4179:coderived category of the periodic bar complex identifies with the
chapters/examples/kac_moody.tex:4208:Assuming Conjecture~\textup{\ref{conj:kl-coderived}}, the equivalence
chapters/examples/kac_moody.tex:4235:\emph{Homotopy templates} (Convention~\ref{conv:hms-levels}): Conjecture~\ref{conj:kl-periodic-cdg}: Type~V (periodicity). Conjecture~\ref{conj:kl-coderived}: Type~II (coderived equivalence with $\mathcal{C}(U_q(\fg))$). Conjecture~\ref{conj:kl-braided}: Type~II (braided monoidal lift).
chapters/examples/yangians_drinfeld_kohno.tex:1017:infinite-dimensional modules via a completed or coderived
chapters/examples/yangians_drinfeld_kohno.tex:1519:coderived/contraderived category of
chapters/examples/yangians_drinfeld_kohno.tex:1525:\index{coderived category!factorization|textbf}
chapters/examples/yangians_drinfeld_kohno.tex:1536:\item The factorization coderived category
chapters/examples/yangians_drinfeld_kohno.tex:1541: pro-object\textup{)}, so the coacyclicity localizing
chapters/examples/yangians_drinfeld_kohno.tex:1553: where the left side is the coderived category of conilpotent
chapters/examples/yangians_drinfeld_kohno.tex:1559: also holds\textup{)}, the coderived and ordinary derived categories
chapters/examples/yangians_drinfeld_kohno.tex:1580:coacyclicity localizing subcategory (thick closure of totalizations
chapters/examples/yangians_drinfeld_kohno.tex:1583:Definition~\ref{def:chiral-coderived}, applied sectorwise.
chapters/examples/yangians_drinfeld_kohno.tex:1603:coacyclic = acyclic (Positselski~\cite[Thm~3.7]{Positselski11}),
chapters/examples/yangians_drinfeld_kohno.tex:1614:\begin{remark}[The coderived category as the natural ambient]
🌐 Searching the web...
🌐 Searched the web

thinking
**Adjusting my approach**

Oh no, I might've used the web when it wasn't actually necessary. That's a little bit of a hiccup! I think I should switch gears and use local grep instead. It could be more efficient for what I'm trying to accomplish. Making sure I’m using the right tool is important, so I’ll adjust my strategy accordingly. Let's make this happen!
codex
The local theorem has exactly the two gaps flagged: the class-M factorization is asserted without support, and the proof incorrectly treats `m_0` as a boundary in the coderived quotient. I’m now checking the surrounding coderived formalism so I can replace the false step with the strongest statement the repo actually supports.
exec
/bin/zsh -lc "rg -n \"\\\\ClaimStatusConditional.*begin\\{theorem\\}|begin\\{theorem\\}.*ClaimStatusConditional|\\\\begin\\{theorem\\}.*ClaimStatusConditional\" chapters | head -n 50" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '500,710p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '220,360p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:\ClaimStatusConditional.*begin\{theorem\}|begin\{theorem\}.*ClaimStatusConditional|\begin\{theorem\}.*ClaimStatusConditional)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products
 succeeded in 50ms:
\index{CDG-contramodule!factorization|textbf}
Let $(C, d, h)$ be a curved factorization coalgebra on~$X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item A \emph{factorization CDG-comodule} $(M, d_M)$ over~$C$
 is a CDG-comodule over~$C$
 (Definition~\ref{def:cdg-comod-contra-appendix}) equipped with
 factorization structure: for disjoint opens $U_1, U_2$, the
 CDG structure on $M(U_1 \sqcup U_2)$ agrees with the tensor
 product CDG structure on
 $M(U_1) \otimes C(U_2)$
 under the comodule factorization isomorphism.
\item A \emph{factorization CDG-contramodule} $(P, d_P)$
 over~$C$ is defined dually, with the factorization-compatible
 contraaction.
\end{enumerate}
\end{definition}

\begin{definition}[Coacyclic and contraacyclic factorization objects]
\label{def:coacyclic-fact}
\index{coacyclic object!factorization|textbf}
 succeeded in 51ms:
 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
\item The induced map on coacyclic quotients
 $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
 isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
 generated by totalizations of short exact sequences
 (Positselski~\cite{Positselski11}).
\end{enumerate}
The equivalence of (i) and (ii) holds for bounded-below filtrations
by~\cite[Proposition~3.5]{Positselski11}.
\end{definition}

\begin{definition}[Provisional coderived category]
\label{def:provisional-coderived}
\index{coderived category!provisional|textbf}
The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
is the localization of the category of filtered curved factorization
models (Definition~\ref{def:filtered-curved-model}) at the weak
equivalences of Definition~\ref{def:curved-weak-equiv}.

thinking
**Exploring harmonic concepts**

I'm realizing I need to dig deeper into topics like harmonic projection, potentially looking at Hodge decomposition and transfer formula. I should search in the target or repository for details on the class M mechanism. Maybe I can strengthen the proof by referencing an existing proposition about harmonic discrepancy through m0 — though I'm unsure if that will be the right direction. I think I should also broaden my search for more insights.
exec
/bin/zsh -lc "rg -n \"c_r\\(\\\\cA\\).*m_0|m_0\\"'^'"\\{\\\\lfloor r/2|harmonic.*m_0|Quillen anomaly|Q\\"'^'"\\{contact\\}|delta_4\\"'^'"\\{\\\\mathrm\\{harm\\}\\}|delta_r\\"'^'"\\{\\\\mathrm\\{harm\\}\\}\" chapters/connections/bv_brst.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1740,1910p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32130,32210p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10490,10570p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c_r\(\cA\).*m_0|m_0\^\{\lfloor r/2|harmonic.*m_0|Quillen anomaly|Q\^\{contact\}|delta_4\^\{\mathrm\{harm\}\}|delta_r\^\{\mathrm\{harm\}\})
            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
higher vertices appear, so obstruction~(3) is resolved at all
degrees for affine Kac--Moody at genus~$1$.
For class~C ($r_{\max} = 4$, the $\beta\gamma$ system):
the quartic vertex is nonzero, but the harmonic-propagator
correction vanishes by a three-mechanism argument
(Remark~\ref{rem:bv-bar-class-c-proof}).
For class~M ($r_{\max} = \infty$),
the quartic vertex is nonzero, and no algebraic identity
analogous to the Jacobi identity is available.
\end{proof}

\begin{remark}[BV/bar identification for class~C:
three-mechanism proof]%
\label{rem:bv-bar-class-c-proof}%
\index{BV algebra!bar complex identification!class C|textbf}%
\index{$\beta\gamma$ system!BV/bar identification}%
\index{harmonic decoupling!role separation}%
The chain-level BV/bar identification
(Conjecture~\ref{conj:master-bv-brst})
holds for class~C algebras ($\beta\gamma$ systems) at
 succeeded in 51ms:
  \Bigr)
  d\Omega_{\alpha\beta}.
\end{equation}
At genus~$1$, the Siegel matrix reduces to the scalar
$\tau = \Omega_{11}$, $\omega_1(z) = dz$, and the modular
part reduces to
$\partial_\tau - \frac{\hbar}{2\pi i}\,
\wp(w, \tau)\,\Omega\,d\tau$
of equation~\eqref{eq:kzb-tau}. At genus~$2$, the modular
part has \emph{three} independent components
$d\Omega_{11}$, $d\Omega_{12}$, $d\Omega_{22}$ (the three
directions in~$\HHH_2$). The flatness of the full KZB
system follows from the genus-$2$ heat equation for the
theta function:
\begin{equation}\label{eq:heat-g2}
  \frac{\partial}{\partial \Omega_{\alpha\beta}}
  \theta[\delta](z|\Omega)
  = \frac{1}{2\pi i}\,
  \frac{\partial^2}{\partial z_\alpha\,\partial z_\beta}
  \theta[\delta](z|\Omega).
 succeeded in 51ms:
For any modular bar datum~$\cA$, there is a complete filtered
cyclic/modular $L_\infty$-algebra $\Definfmod(\cA)$ controlling
modular deformations. The coderivation dg~Lie algebra of a
chosen completed modular bar model is a strictification.
The universal class $\Theta_{\cA}$ is its canonical
Maurer--Cartan element. The full $L_\infty$-MC equation
recovers the quantum master
equation~\eqref{eq:quantum-linfty-mc}.
\end{theorem}

\begin{proof}
This synthesises Theorem~\ref{thm:modular-quantum-linfty} with
the two-level convention. The complete filtered $L_\infty$-algebra
is the quantum $L_\infty$-algebra of
Theorem~\ref{thm:modular-quantum-linfty}; the dg~Lie algebra
$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ of
Definition~\ref{def:modular-convolution-dg-lie} is the strict
model obtained by retaining only $\ell_1^{(0)} = D$ and
$\ell_2^{(0)} = [-,-]$.
For the chosen completed modular bar model, the transfer is taken
exec
/bin/zsh -lc "rg -n -U \"\\\\begin\\{theorem\\}.*\\n\\\\ClaimStatusConditional|\\\\begin\\{theorem\\}\\[["'^'"\\n]*\\n\\\\ClaimStatusConditional\" chapters | head -n 40" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "ClaimStatusConditional" chapters/connections/bv_brst.tex chapters | head -n 80' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:bv-bar-coderived|rem:bv-bar-coderived-higher-genus|conj:master-bv-brst|prop:chain-level-three-obstructions" chapters/connections/bv_brst.tex chapters/theory/en_koszul_duality.tex chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:\begin\{theorem\}.*\n\ClaimStatusConditional|\begin\{theorem\}\[[^\n]*\n\ClaimStatusConditional)
                            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/connections/bv_brst.tex:1123:\ClaimStatusConditional]
chapters/connections/bv_brst.tex:1166:\ClaimStatusConditional]
chapters/connections/bv_brst.tex:1302:\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
chapters/connections/bv_brst.tex:1358:\begin{theorem}[Conditional BV functor package; \ClaimStatusConditional]
chapters/examples/free_fields.tex:4808:\ClaimStatusConditional]\label{cor:string-amplitude-genus0}
chapters/examples/yangians_computations.tex:1809:\ClaimStatusConditional]\label{cor:dk-partial-conj}
chapters/examples/yangians_computations.tex:1837:category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A}; \ClaimStatusConditional]
chapters/connections/thqg_gravitational_complexity.tex:1185:\begin{proposition}[Complexity is a Koszul duality invariant; \ClaimStatusConditional]
chapters/connections/ym_instanton_screening.tex:498:\begin{theorem}[Conditional mass-gap transfer via screening domination; \ClaimStatusConditional]
chapters/connections/editorial_constitution.tex:657:locus; \ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:900:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:931:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1064:locus; \ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1153:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1215:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1268:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1314:\ClaimStatusConditional]
chapters/connections/thqg_symplectic_polarization.tex:1370:potential; \ClaimStatusConditional]
chapters/connections/arithmetic_shadows.tex:8167:\ClaimStatusConditional
chapters/connections/arithmetic_shadows.tex:10697:\textup{(iv)} \ClaimStatusConditional]%
 succeeded in 51ms:
chapters/connections/bv_brst.tex:31:for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/bv_brst.tex:36:(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
chapters/connections/bv_brst.tex:1403:Conjecture~\ref{conj:master-bv-brst} at the scalar level
chapters/connections/bv_brst.tex:1625:Conjecture~\ref{conj:master-bv-brst} at the \emph{scalar level}
chapters/connections/bv_brst.tex:1655:\label{prop:chain-level-three-obstructions}
chapters/connections/bv_brst.tex:1659:\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1758:(Conjecture~\ref{conj:master-bv-brst})
chapters/connections/bv_brst.tex:1811:Conjecture~\ref{conj:master-bv-brst} at the scalar level for
chapters/connections/bv_brst.tex:1846:This resolves Conjecture~\ref{conj:master-bv-brst} in
chapters/connections/bv_brst.tex:1848:(Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/bv_brst.tex:1890:(Proposition~\ref{prop:chain-level-three-obstructions}).
chapters/connections/bv_brst.tex:1896:(Theorem~\ref{thm:bv-bar-coderived} below).
chapters/connections/bv_brst.tex:1904:\label{thm:bv-bar-coderived}%
chapters/connections/bv_brst.tex:1926:Proposition~\ref{prop:chain-level-three-obstructions}.
chapters/connections/bv_brst.tex:1965:\label{rem:bv-bar-coderived-higher-genus}%
chapters/connections/bv_brst.tex:31:for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/bv_brst.tex:36:(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
chapters/connections/bv_brst.tex:1403:Conjecture~\ref{conj:master-bv-brst} at the scalar level
chapters/connections/bv_brst.tex:1625:Conjecture~\ref{conj:master-bv-brst} at the \emph{scalar level}
chapters/connections/bv_brst.tex:1655:\label{prop:chain-level-three-obstructions}

thinking
**Inspecting file updates**

I need to check the start of the file for summary statements that might need updating due to changes in theorem status. There could be mentions of theorems proved for all four classes around line 30. I should edit those too, focusing on only the specific file assigned. It's crucial to update all local mentions in the target to maintain consistency. I want to look closely at the beginning and the earlier conditional package, specifically lines 1 to 50.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1080,1375p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1580,1865p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
 succeeded in 51ms:
= 0$ (Theorem~\ref{thm:explicit-theta}), since
$\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$
by Theorem~\ref{thm:genus-universality}(ii).
The chain-level mechanism underlying~(c) is:
the Verdier involution exchanges
$\Theta_{\widehat{\fg}_k}$ and $-\Theta_{\widehat{\fg}_{k'}}$,
producing the Lagrangian splitting of
Theorem~\ref{thm:quantum-complementarity-main}.
\end{enumerate}
\end{corollary}

\begin{proof}
Part~(a) is the cohomology-level consequence of
Theorem~\ref{thm:bar-semi-infinite-km}. Part~(b): the
curvature $m_0 = \kappa \cdot \mathbf{1}$ in the bar complex
corresponds, under the quasi-isomorphism~$\Psi$, to the
semi-infinite anomaly (the failure of the naive CE differential
to square to zero, corrected by the semi-infinite charge).
The genus universality theorem identifies this with the
conformal anomaly coefficient. The KM anti-symmetry
 succeeded in 51ms:
Therefore the generating function for the genus-$g$ contributions is
\[
\sum_{g \geq 1} F_g(\cH_\kappa)\,\hbar^{2g}
= \kappa \cdot \bigl(\hat{A}(i\hbar) - 1\bigr)
= \kappa \cdot \Bigl(\frac{\hbar/2}{\sin(\hbar/2)} - 1\Bigr)
\]
\textup{(}\S\ref{subsec:why-ahat}\textup{)}.
The Taylor coefficient at $\hbar^{2g}$ is
$\kappa \cdot \frac{(2^{2g-1}-1)\,|B_{2g}|}{2^{2g-1}\,(2g)!}
= \kappa \cdot \lambda_g^{\mathrm{FP}}$,
confirming~\eqref{eq:bv-bar-heisenberg} by a third route.
Note: Path~\textup{(a)} derives the same generating function
from the Quillen anomaly and then extracts coefficients; this path
arrives at the generating function from the family index theorem
without passing through the determinant line bundle.
\index{family index theorem!BV/bar proof|)}

\medskip
\noindent\textbf{Path \textup{(d)}: numerical verification.}
\index{multi-path verification!Heisenberg BV/bar}

thinking
**Analyzing mathematical statements**

I'm thinking about how I need to focus on more specific statements around line 31. I want to discuss the current BV/bar landscape and touch on a theorem, particularly about higher genus. I find it intriguing to explore why a coderived category might be considered inevitable, especially if it involves a false mechanism. I should definitely inspect what follows after line 1990 to see if there are any updates needed.
exec
/bin/zsh -lc "sed -n '1987,2065p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2065,2135p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"m_0 = d\\"'^2/d|d'"\\"'^2/d|delta_r = c_r|delta_r '"\\propto m_0|coderived-trivial|BV=bar in the coderived category|for all four shadow classes|quasi-isomorphic in the coderived category\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Why the coderived category is inevitable]
\label{rem:bv-bar-coderived-why}
\index{coderived category!physical inevitability}
\index{BV algebra!bar complex identification!physical interpretation}
The passage from the ordinary derived category to the coderived
category is not a technical convenience but a physical necessity,
and its inevitability can be understood from three complementary
viewpoints.

\emph{The worldsheet viewpoint.}
On a genus-$g$ Riemann surface $\Sigma_g$, the worldsheet path
integral produces amplitudes via the sewing construction: one cuts
$\Sigma_g$ along a collar into two pieces and sums over a complete
set of intermediate states. The sewing sum introduces the
propagator $P = P_{\mathrm{bar}} + P_{\mathrm{exact}} +
P_{\mathrm{harm}}$, where $P_{\mathrm{harm}}$ is the harmonic
piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
\emph{full} propagator; the bar complex uses only
$P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
 exited 2 in 51ms:
rg: regex parse error:
    (?:m_0 = d\^2/d|d\^2/d|delta_r = c_r|delta_r \propto m_0|coderived-trivial|BV=bar in the coderived category|for all four shadow classes|quasi-isomorphic in the coderived category)
                                                 ^^^
error: Unicode property not found
 succeeded in 51ms:
\textup{(}the rank of the characteristic lattice\textup{)}. The Burns
space is the simplest member.

\begin{computation}[Burns space Koszul datum;
\ClaimStatusProvedElsewhere]
\label{comp:burns-koszul-datum}
\index{Burns space!Koszul datum}
\index{$\beta\gamma$ system!Burns}
The boundary VOA of the Burns space consists of four $\beta\gamma$
pairs with an $SO(8)$ global symmetry, giving:
\begin{itemize}[nosep]
\item central charge $c_{\mathrm{Burns}}
 = 4 \cdot c_{\beta\gamma}(\lambda{=}1)
 = 4 \cdot 2 = 8$,
 using $c_{\beta\gamma}(1) = 2(6 - 6 + 1) = 2$;
\item modular characteristic
 $\kappa_{\mathrm{Burns}} = c_{\mathrm{Burns}}/2 = 4$;
\item shadow class~$\mathsf{C}$ globally \textup{(}shadow depth
 $r_{\max} = 4$, governed by the quartic contact term of the
 $\beta\gamma$ system\textup{)}, degenerating to class~$\mathsf{M}$

thinking
**Investigating filtration on complexes**

I need to inspect if there's already a bounded-below PBW filtration on BV and bar complexes. It might be possible to show that the map is a weak equivalence in the provisional coderived category without needing each obstruction boundary. I should look through the file for a comparison map or filtered model and search for relevant keywords regarding PBW filtration and associated graded. Maybe I can find a stronger local route!
codex
I’m checking whether the coderived statement can be salvaged by the repo’s actual weak-equivalence criterion instead of the false “`Im(d)` in `D^co`” argument. If that route is unavailable, I’ll downgrade only the class-M/coderived claim and keep the proved chain-level classes intact.
exec
/bin/zsh -lc 'rg -n -F "weak equivalence" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "PBW filtration" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "coacyclic" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex | head -n 120' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "associated graded" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/coderived_models.tex:216:is a \emph{weak equivalence} if it satisfies either of the following
chapters/theory/coderived_models.tex:266:Theorem~\ref{thm:higher-genus-inversion}, hence a weak equivalence
chapters/theory/coderived_models.tex:268:Off the Koszul locus, the counit is still a weak equivalence
chapters/theory/coderived_models.tex:673:A provisional weak equivalence
chapters/theory/coderived_models.tex:683:sends provisional weak equivalences to coderived isomorphisms.
 succeeded in 51ms:
chapters/connections/bv_brst.tex:504:The proof uses a PBW filtration on both complexes, reducing the
chapters/connections/bv_brst.tex:946:On the bar side, this is the PBW filtration of
chapters/connections/bv_brst.tex:1353:where the semi-infinite complex may not admit a PBW filtration.
chapters/connections/bv_brst.tex:2283:\emph{Step~2: PBW filtration and Chevalley--Eilenberg reduction.}
chapters/theory/coderived_models.tex:273:For (b): the PBW filtration by conformal weight is exhaustive,
chapters/theory/coderived_models.tex:279:For (c): Verdier duality preserves the PBW filtration
chapters/theory/coderived_models.tex:293:image consists of objects admitting a bounded-below PBW filtration.
chapters/theory/coderived_models.tex:694:The PBW filtration on bar complexes
chapters/theory/higher_genus_modular_koszul.tex:937:Equip $\bar{B}^{(1)}(\widehat{\fg}_k)$ with the PBW filtration
chapters/theory/higher_genus_modular_koszul.tex:1667:admitting a PBW filtration by conformal weight, and satisfying:
chapters/theory/higher_genus_modular_koszul.tex:1700: PBW filtration.
chapters/theory/higher_genus_modular_koszul.tex:2090:(ii) The PBW filtration by conformal weight is intrinsic
chapters/theory/higher_genus_modular_koszul.tex:2377:The PBW filtration is a filtration by chiral algebras, and the
chapters/theory/higher_genus_modular_koszul.tex:27703:where $F_\bullet$ is the PBW filtration.
chapters/theory/higher_genus_modular_koszul.tex:28172:hypotheses are (1)~flatness of the PBW filtration
chapters/theory/higher_genus_modular_koszul.tex:28373:action on~$\cF$; the filtration from the PBW filtration;
 succeeded in 50ms:
chapters/theory/coderived_models.tex:219:\item The associated graded map
chapters/theory/coderived_models.tex:276:least one OPE contraction. At associated graded level, the
chapters/theory/coderived_models.tex:675:quasi-isomorphism on associated graded. For bounded-below
chapters/theory/coderived_models.tex:679:bounded-below spectral sequence with acyclic associated graded
chapters/theory/coderived_models.tex:689:on each stratum implies the associated graded spectral sequence
chapters/connections/bv_brst.tex:531:On the associated graded $\mathrm{gr}\,F^{\bullet}$, both complexes
chapters/connections/bv_brst.tex:543:In both cases, the associated graded complex is the
chapters/connections/bv_brst.tex:581:weight~$p$, the associated graded complexes are identified by~$\Phi_0$,
chapters/connections/bv_brst.tex:957:On the associated graded $\mathrm{gr}\,F^\bullet$,
chapters/connections/bv_brst.tex:968:Both associated graded complexes compute the Lie algebra cohomology
chapters/connections/bv_brst.tex:2259:On the PBW-associated graded, the BRST differential
chapters/connections/bv_brst.tex:2281:identify the differentials on the PBW-associated graded.
chapters/connections/bv_brst.tex:2286:chirally Koszul locus. On the BRST side, the associated graded
chapters/connections/bv_brst.tex:2289:vacuum module. On the bar side, the associated graded differential
 succeeded in 50ms:
chapters/theory/coderived_models.tex:57:\label{def:coacyclic-contraacyclic}
chapters/theory/coderived_models.tex:58:\index{coacyclic object|textbf}
chapters/theory/coderived_models.tex:62:\item A CDG-comodule $M$ is \emph{coacyclic} if it belongs to the
chapters/theory/coderived_models.tex:93:object is coacyclic (resp.\ contraacyclic), so there are natural
chapters/theory/coderived_models.tex:130:CDG-comodule is coacyclic, so the coderived category coincides
chapters/theory/coderived_models.tex:223:\item The induced map on coacyclic quotients
chapters/theory/coderived_models.tex:326: localization of the homotopy category at coacyclic objects, those
chapters/theory/coderived_models.tex:329: Definition~\ref{def:coacyclic-contraacyclic}).
chapters/theory/coderived_models.tex:518:\label{def:coacyclic-fact}
chapters/theory/coderived_models.tex:519:\index{coacyclic object!factorization|textbf}
chapters/theory/coderived_models.tex:523:\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
chapters/theory/coderived_models.tex:539:Definition~\ref{def:coacyclic-contraacyclic}. The factorization
chapters/theory/coderived_models.tex:542:through any additional axiom on the coacyclicity condition.
chapters/theory/coderived_models.tex:609:triples and direct sums. Hence it sends coacyclic factorization
chapters/theory/coderived_models.tex:610:objects to coacyclic $C_n$-comodules
chapters/theory/coderived_models.tex:611:(Definition~\ref{def:coacyclic-contraacyclic}), and descends to
chapters/theory/coderived_models.tex:642:Now $K|_m$ is coacyclic for every stratum~$m$ (by hypothesis),
chapters/theory/coderived_models.tex:650:$\mathrm{Hom}(K, J) = 0$, so $K$ is coacyclic.
chapters/theory/coderived_models.tex:676:filtrations, this implies the cone is coacyclic on each
chapters/theory/coderived_models.tex:680:produces a coacyclic totalization). By conservativity

thinking
**Considering genus0 identification**

I'm pondering how earlier proven theorems regarding genus0 identification using PBW filtration might apply to general coderived theories. It seems like there could be some useful connections! I should inspect around those specific lines—like 500 and 2250—to understand better. I want to make sure I'm grasping all the details, as each might provide valuable insights into the theorems that can be applied in this context. Let's keep exploring!
exec
/bin/zsh -lc "sed -n '910,990p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2235,2315p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '470,610p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \bigr)
\]
for the standard semi-infinite BRST complex of the genus-$0$ WZW
model, and write
\[
 \barB^{\mathrm{ch}}_0\bigl(V_k(\fg)\bigr)
 \;=\;
 T^c\bigl(s^{-1}\overline{V_k(\fg)}\bigr),
 \qquad
 \overline{V_k(\fg)} := \ker(\epsilon),
\]
for the genus-$0$ chiral bar complex, with desuspension
$|s^{-1}v| = |v| - 1$. Then for every degree $n \geq 3$
\textup{(}the stability range $2g - 2 + n > 0$ at genus~$0$\textup{)},
the WZW BRST complex is computed by the affine bar complex: there
is a natural filtered quasi-isomorphism
\begin{equation}\label{eq:wzw-brst-bar-qi}
 C_{\mathrm{BRST}}^{\bullet,\mathrm{WZW}}(\fg,k)
 \xrightarrow{\;\sim\;}
 \bigl(
 succeeded in 52ms:
\end{lemma}

\begin{remark}[BRST nilpotence and the bar construction]
\label{rem:brst-nilpotence-periodicity}
\index{nilpotence-periodicity correspondence!BRST instance}
The condition $Q_{\mathrm{BRST}}^2 = 0$ is the BRST instance of the nilpotence-periodicity correspondence (Remark~\ref{rem:nilpotence-periodicity}): $\kappa_{\mathrm{tot}} = 0$ ensures $d_{\mathrm{bar}}^2 = 0$ on the genus-$0$ bar complex, so the bar differential is a genuine differential. When $\kappa_{\mathrm{tot}} \neq 0$, the curvature term $Q_{\mathrm{BRST}}^2 = \frac{c-26}{12}\,c_0 \neq 0$ obstructs nilpotence.
\end{remark}

The \emph{semi-infinite cohomology} $H^{\infty/2+\bullet}(\cA)$
is the cohomology of $(\cA_{\mathrm{tot}}, Q_{\mathrm{BRST}})$, graded
by ghost number. For the bosonic string ($\cA = \mathcal{H}^{26}$,
$c = 26$), this computes the physical state space.

\subsection{The chain map}

\begin{theorem}[Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism;
\ClaimStatusProvedHere]
\label{thm:brst-bar-genus0}
\index{BRST!bar complex quasi-isomorphism}
Let $\cA$ be a conformal vertex algebra on $\mathbb{P}^1$ with
 succeeded in 52ms:

\subsection{The bar--semi-infinite identification for Kac--Moody algebras}

\begin{theorem}[Bar complex = semi-infinite complex for KM;
\ClaimStatusProvedHere]
\label{thm:bar-semi-infinite-km}
\index{semi-infinite cohomology!bar complex identification}
\index{BRST!semi-infinite identification}
Let $\widehat{\fg}_k$ be the universal affine vertex algebra at level
$k \neq -h^\vee$. There is a quasi-isomorphism of filtered cochain
complexes:
\begin{equation}\label{eq:bar-semi-infinite}
\Psi \colon
 \bigl(\barB^{\mathrm{ch}}(\widehat{\fg}_k),\, d_{\mathrm{bar}}\bigr)
 \xrightarrow{\;\sim\;}
 \bigl(C^{\infty/2+\bullet}(\widehat{\fg}_k, V_k),\, Q_{\mathrm{si}}\bigr)
\end{equation}
identifying the chiral bar complex with the semi-infinite complex
\textup{(}with coefficients in the vacuum module $V_k$\textup{)}.
In particular:
exec
/bin/zsh -lc "sed -n '200,320p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '320,430p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:bv-bar-geometric" -n chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The generators are operator insertions $\phi_i \in \mathcal{A}$ at marked points, paired with logarithmic $1$-forms $\eta_{ij} = d\log(z_i - z_j)$ dual to the collision divisors.

\emph{Step~2: BV Bracket.}

The BV bracket is a residue operation on the log-de~Rham complex
of~$\overline{C}_{n+1}(X)$. In local coordinates near the divisor
$D_{ij} = \{z_i = z_j\}$, with $\epsilon = z_i - z_j$:
\[\{\phi(z_i), \eta_{jk}\}
= \delta_{ij}\,\Res_{\epsilon = 0}
\Bigl[\frac{\partial\phi}{\partial z_i}\,
\frac{d\epsilon}{\epsilon(z_i - z_k)}\Bigr]
+ \delta_{ik}\,\Res_{\epsilon = 0}
\Bigl[\frac{\partial\phi}{\partial z_i}\,
\frac{d\epsilon}{\epsilon(z_i - z_j)}\Bigr].\]
Both terms are Poincar\'e residues of logarithmic forms along
normal-crossing divisors of the smooth
variety~$\overline{C}_{n+1}(X)$: the residue map
$\Res_{D_{ij}}\colon \Omega^k_{\log}(\overline{C}_{n+1})
\to \Omega^{k-1}_{D_{ij}}$ is an algebraic morphism of sheaves
 succeeded in 51ms:
\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
\end{remark}

\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
\index{anomaly!curvature identification}
By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
\end{remark}

\section{Gauge fixing and BRST}

\subsection{BRST from BV}

\begin{definition}[BRST operator]
\label{def:brst-operator}
\index{BRST cohomology|textbf}
\index{BRST operator|textbf}
The BRST operator $Q_{\mathrm{BRST}}$ arises from gauge fixing the BV action.
Choose a Lagrangian submanifold $\mathcal{L}$ of the total space of fields and
antifields:
 succeeded in 51ms:
79: \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
92:Item~\textup{(i)} is Theorem~\ref{thm:bv-bar-geometric}. The scalar
181:\label{thm:bv-bar-geometric}
195:\begin{proof}[Geometric construction supporting \textup{Theorem~\ref{thm:bv-bar-geometric}}]
271:comparison of Theorem~\ref{thm:bv-bar-geometric}. Extending this to a
375:under the identification of Theorem~\ref{thm:bv-bar-geometric}.
1923:Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
codex
The repo’s coderived appendix gives a real route only when there is a bounded-below filtered map whose associated graded is already a quasi-isomorphism. I haven’t found that input for the class-M BV/bar map, so I’m treating the current proof as irreparable on the existing evidence and rewriting it as a conditional statement with explicit hypotheses instead of a fake proof.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_bv_sewing_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "theorem_bv_sewing_engine.py" -n .' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "bv-bar-coderived" compute chapters | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
r"""Chain-level identification: Delta_BV = d_sew (both increment genus by 1).

THEOREM (thm:bv-sewing-chain-level):
  For a chirally Koszul algebra A, the BV Laplacian Delta_BV on Obs(Sigma_g, A)
  and the sewing operator d_sew on the bar complex B(A) agree as chain-level
  operators on the modular convolution algebra g^mod_A.  Both operations:
    (a) increment genus by 1: (g,n) -> (g+1, n-2),
    (b) contract a pair of inputs through the Bergman kernel / d log E(z,w),
    (c) are controlled by the non-separating boundary divisor
        delta^ns: M-bar_{g,n+2} -> M-bar_{g+1,n}.

  The identification holds unconditionally for classes G and L
  (Heisenberg, affine KM), and conditionally for classes C and M
  (beta-gamma, Virasoro, W_N) subject to the harmonic-propagator
  correction vanishing on bar cohomology at the quartic and higher levels.

PROOF STRATEGY (four independent paths):

  Path 1 (Operator definition):
    Both Delta_BV and d_sew act on bar-complex elements by contracting
 succeeded in 51ms:
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:19:- [LOW] compute/lib/theorem_bv_sewing_engine.py:12 — The cited compute layer is not independent evidence. It hardcodes theorem-status assumptions, upgrades Heisenberg to a chain-level quasi-isomorphism absent from `thm:heisenberg-bv-bar-all-genera` ([41–45]), and gives a different `C/M` status split from the chapter.
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1108:/bin/zsh -lc "nl -ba compute/lib/theorem_bv_sewing_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1109:/bin/zsh -lc "nl -ba compute/tests/test_theorem_bv_sewing_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1223:- [LOW] compute/lib/theorem_bv_sewing_engine.py:12 — The cited compute layer is not independent evidence. It hardcodes theorem-status assumptions, upgrades Heisenberg to a chain-level quasi-isomorphism absent from `thm:heisenberg-bv-bar-all-genera` ([41–45]), and gives a different `C/M` status split from the chapter.
./compute/audit/deep_beilinson_rectification_2026_04_07.md:84:- theorem_bv_sewing_engine.py: scope correctly qualified (G/L proved, C/M conditional)
./compute/audit/session_summary_2026_04_07_08.md:143:| theorem_bv_sewing_engine.py | ~107 | BV/BRST = bar class-by-class |
./compute/audit/bv_brst_bar_frontier_report.md:204:| `theorem_bv_sewing_engine.py` | -- | Chain-level Delta_BV = d_sew identification |
./compute/lib/theorem_bv_brst_rectification_engine.py:126:  theorem_bv_sewing_engine.py, chain_level_bv_bar.py.
./compute/lib/bv_bar_class_c_engine.py:10:  The BV sewing engine (theorem_bv_sewing_engine.py) proved:
./compute/lib/bv_bar_class_c_engine.py:135:  theorem_bv_sewing_engine.py (BV=bar conditional status for class C)
 succeeded in 51ms:
chapters/connections/bv_brst.tex:31:for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/bv_brst.tex:1848:(Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/bv_brst.tex:1896:(Theorem~\ref{thm:bv-bar-coderived} below).
chapters/connections/bv_brst.tex:1904:\label{thm:bv-bar-coderived}%
chapters/connections/bv_brst.tex:1965:\label{rem:bv-bar-coderived-higher-genus}%
chapters/connections/bv_brst.tex:1988:\label{rem:bv-bar-coderived-why}
chapters/connections/concordance.tex:697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:3291: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:6940: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:7611: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9690: \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
chapters/connections/concordance.tex:10087: (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/concordance.tex:11015: Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
chapters/connections/concordance.tex:11135: (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
chapters/frame/preface_sections10_13_draft.tex:433:including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/frame/guide_to_main_results.tex:109: \ref{thm:bv-bar-coderived} \\[4pt]
chapters/frame/preface.tex:4171:including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/editorial_constitution.tex:441:\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
chapters/theory/en_koszul_duality.tex:2706: (Theorem~\ref{thm:bv-bar-coderived}), and reconstruction

thinking
**Reviewing audit report**

I find it interesting that there's an audit report for T12. I think it's worth reading because it’s directly relevant and probably reveals the strongest fixes. The user asked to address the exact findings, so I should look into the audit file for insights. I'll focus on the relevant sections around the T12 findings to gather the necessary information. This is definitely a step in the right direction!
codex
I found the local T12 audit file for this exact theorem. I’m reading the targeted section because it may already isolate what survives truthfully, and that’s better evidence than trying to reconstruct a proof from memory.
exec
/bin/zsh -lc 'rg -n -F "delta_r''^{'"\\mathrm{harm}}\" audit_campaign_20260412_231034/T12_MC5_BV_bar.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' audit_campaign_20260412_231034/T12_MC5_BV_bar.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "coacyclic" audit_campaign_20260412_231034/T12_MC5_BV_bar.md | head -n 40' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:- [CRITICAL] chapters/connections/bv_brst.tex:1932 — The core class-M mechanism, `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}`, is introduced without proof or citation. In the files read, this factorization appears only in `thm:bv-bar-coderived`, its follow-up remark, and downstream restatements, so the theorem’s main engine is unproved.
1005:chapters/connections/bv_brst.tex:1968:$\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
1018:chapters/connections/bv_brst.tex:1968:$\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
1207:- [CRITICAL] chapters/connections/bv_brst.tex:1932 — The core class-M mechanism, `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}`, is introduced without proof or citation. In the files read, this factorization appears only in `thm:bv-bar-coderived`, its follow-up remark, and downstream restatements, so the theorem’s main engine is unproved.
 succeeded in 51ms:
5:- [CRITICAL] chapters/connections/bv_brst.tex:1945 — The proof treats `m_0\cdot x = d^2(x) \in \operatorname{Im}(d)` as enough to kill the obstruction in `D^{\mathrm{co}}`. But the appendix defines the coderived category as a Verdier quotient by coacyclic objects, not as “boundaries modulo `\operatorname{Im}(d)`” ([chapters/theory/coderived_models.tex:75]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:75), [chapters/theory/coderived_models.tex:545]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:545)). Worse, the manuscript itself says curved objects are *not* set to zero in the coderived category ([chapters/theory/bar_cobar_adjunction_inversion.tex:3355]( /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3355)). This is a direct logical failure in the coderived proof.
418:   523	\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
434:   539	Definition~\ref{def:coacyclic-contraacyclic}. The factorization
511:/bin/zsh -lc "rg -n \"m_0 .*exact|m_0.*Im\\(d\\)|d\\"'^2 = m_0|m_0'"\\"'^k|coderived-trivial|coderived-exact|not set to zero|coacyclic" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
538:chapters/theory/coderived_models.tex:57:\label{def:coacyclic-contraacyclic}
539:chapters/theory/coderived_models.tex:58:\index{coacyclic object|textbf}
540:chapters/theory/coderived_models.tex:62:\item A CDG-comodule $M$ is \emph{coacyclic} if it belongs to the
541:chapters/theory/coderived_models.tex:93:object is coacyclic (resp.\ contraacyclic), so there are natural
542:chapters/theory/coderived_models.tex:130:CDG-comodule is coacyclic, so the coderived category coincides
544:chapters/theory/coderived_models.tex:223:\item The induced map on coacyclic quotients
545:chapters/theory/coderived_models.tex:326: localization of the homotopy category at coacyclic objects, those
546:chapters/theory/coderived_models.tex:329: Definition~\ref{def:coacyclic-contraacyclic}).
547:chapters/theory/coderived_models.tex:518:\label{def:coacyclic-fact}
548:chapters/theory/coderived_models.tex:519:\index{coacyclic object!factorization|textbf}
549:chapters/theory/coderived_models.tex:523:\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
550:chapters/theory/coderived_models.tex:539:Definition~\ref{def:coacyclic-contraacyclic}. The factorization
551:chapters/theory/coderived_models.tex:542:through any additional axiom on the coacyclicity condition.
552:chapters/theory/coderived_models.tex:609:triples and direct sums. Hence it sends coacyclic factorization
1209:- [CRITICAL] chapters/connections/bv_brst.tex:1945 — The proof treats `m_0\cdot x = d^2(x) \in \operatorname{Im}(d)` as enough to kill the obstruction in `D^{\mathrm{co}}`. But the appendix defines the coderived category as a Verdier quotient by coacyclic objects, not as “boundaries modulo `\operatorname{Im}(d)`” ([chapters/theory/coderived_models.tex:75]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:75), [chapters/theory/coderived_models.tex:545]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:545)). Worse, the manuscript itself says curved objects are *not* set to zero in the coderived category ([chapters/theory/bar_cobar_adjunction_inversion.tex:3355]( /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3355)). This is a direct logical failure in the coderived proof.
 succeeded in 52ms:
# T12_MC5_BV_bar (415s, gpt-5.4)

- [CRITICAL] chapters/connections/bv_brst.tex:1932 — The core class-M mechanism, `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}`, is introduced without proof or citation. In the files read, this factorization appears only in `thm:bv-bar-coderived`, its follow-up remark, and downstream restatements, so the theorem’s main engine is unproved.

- [CRITICAL] chapters/connections/bv_brst.tex:1945 — The proof treats `m_0\cdot x = d^2(x) \in \operatorname{Im}(d)` as enough to kill the obstruction in `D^{\mathrm{co}}`. But the appendix defines the coderived category as a Verdier quotient by coacyclic objects, not as “boundaries modulo `\operatorname{Im}(d)`” ([chapters/theory/coderived_models.tex:75]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:75), [chapters/theory/coderived_models.tex:545]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:545)). Worse, the manuscript itself says curved objects are *not* set to zero in the coderived category ([chapters/theory/bar_cobar_adjunction_inversion.tex:3355]( /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3355)). This is a direct logical failure in the coderived proof.

- [CRITICAL] chapters/connections/bv_brst.tex:1624 — The chapter says the higher-genus chain-level quasi-isomorphism remains open “even for free fields,” i.e. Heisenberg ([1636–1650]), but later upgrades class `G` to chain-level proved ([1821–1822]) and uses chain-level quasi-isomorphisms for `G/L/C` inside `thm:bv-bar-coderived` ([1938–1941]). The status surface is internally contradictory.

- [HIGH] chapters/connections/bv_brst.tex:1925 — For classes `G/L/C`, the theorem cites only `prop:chain-level-three-obstructions`. That proposition classifies obstructions; it does not construct the BV-to-bar chain map or prove a quasi-isomorphism. For `L` and `C`, its proof text only reaches genus `1` ([1741], [1759–1760]), while `thm:bv-bar-coderived` claims all `g\ge1`.

- [HIGH] chapters/connections/bv_brst.tex:1751 — The only support for class `C` is an untagged remark. Its Hodge argument says a quartic correction is a “5-form on a 2-manifold” ([1783–1788]), which uses the wrong domain for a quartic graph/configuration-space integral, and it then calls the “free `\beta\gamma` system” class `G` ([1799–1800]), contradicting the chapter’s own classification of `\beta\gamma` as class `C` ([1825–1826]). This does not support an unconditional proof.

- [HIGH] chapters/connections/bv_brst.tex:1677 — Obstruction (2) is only claimed resolved for theories whose partition function comes from a zeta-regularized determinant ([1682–1684]), but `thm:bv-bar-coderived` upgrades that to “resolved for all classes” ([1927–1929]) without importing any determinant hypothesis. That is scope inflation.

- [HIGH] chapters/connections/bv_brst.tex:1834 — The manuscript does not actually prove that class `M` is chain-level false. The only written reason is the heuristic nonholomorphic factor `\kappa/\mathrm{Im}(\tau)` not lying in the image of the holomorphic bar differential ([1834–1837], [1891–1894]). The same surface then rewrites the obstruction as `Q^{\mathrm{contact}}\cdot m_0` with `m_0=\kappa(\cA)\omega_g` ([1840], [1975–1977]) without proving a bridge between these different objects. So “false” is asserted, not established.

- [MEDIUM] chapters/connections/concordance.tex:7611 — The unsupported claims have propagated: concordance repeats “class `M` chain-level false,” “classes `G/L/C` chain-level proved,” and “every `\delta_r` is coderived-exact” ([7611], [10085–10124]); `en_koszul_duality.tex` reuses the same coderived-exactness mechanism ([3395–3397], [3445–3453]). The overclaim is not local to one theorem.

- [LOW] compute/lib/theorem_bv_sewing_engine.py:12 — The cited compute layer is not independent evidence. It hardcodes theorem-status assumptions, upgrades Heisenberg to a chain-level quasi-isomorphism absent from `thm:heisenberg-bv-bar-all-genera` ([41–45]), and gives a different `C/M` status split from the chapter.


thinking
**Inspecting audit findings**

I need to confirm that we should edit only the target file. The audit file can help guide this process. I might want to inspect the line 3355 related to "curved objects not zero." Although I could potentially cite it in a rewritten remark, it may not be necessary since it pertains to the target file exclusively. I should also consider referencing coderived coacyclicity criterion in the appendix. Let’s take a closer look at that line!
exec
/bin/zsh -lc "sed -n '3335,3375p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Verdier), and the cobar functor translates back. Every other
duality in the programme, whether Poincar\'e--Koszul on manifolds,
Serre on moduli, or the $c \mapsto 26 - c$ involution on the Virasoro
line, is a specialization of this single adjunction acting on
different geometric inputs.
\end{remark}

\begin{remark}[Curvature and coderived categories]\label{rem:curvature-coderived}
\index{coderived category!bar-cobar}
\index{curvature!coderived category}
When curvature is present, i.e., when the genus-$1$ obstruction
$m_0^{(1)} = \kappa(\cA) \cdot \lambda_1 \neq 0$ (as it is for all
Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
Theorem~\ref{thm:genus-universality}), the bar complex satisfies
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \mathrm{id}$ rather than $\dfib^{\,2} = 0$
(see Convention~\ref{conv:higher-genus-differentials} for the notation).
The ordinary derived category of $\cA$-modules is then the wrong
quotient: it erases the distinction between ``acyclic because of
$\dfib^{\,2} \neq 0$'' and ``acyclic because of genuine exactness.''

exec
/bin/zsh -lc "sed -n '690,710p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 Virasoro, double for Heisenberg), not from a Feynman diagram sum.
 The genus universality theorem shows that these two perspectives
 produce the same genus-$g$ obstruction class.
\item \emph{BV-BRST.}
 The CG BV formalism motivates the BRST/bar comparison package in
 Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
 in the coderived category $D^{\mathrm{co}}$ for all shadow classes
 (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
 Heisenberg scalar identification is proved at all genera
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G, L, C are proved. The chain-level identification fails for
 class~M (Conjecture~\ref{conj:master-bv-brst}).
\item \emph{Monoidal bar-cobar.}
 Booth--Lazarev~\cite{BL24} construct monoidal model structures on
 categories of coalgebras, providing the homotopical infrastructure
 for the bar-cobar adjunction to be a Quillen equivalence in the
 monoidal setting. On the current record, this is realized by the
 fusion-compatibility theorem
 (Theorem~\ref{thm:fusion-bar-cobar}): the bar construction
 is a lax monoidal functor from the relevant complete module
exec
/bin/zsh -lc "sed -n '1940,1965p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 plus subexponential sector growth implies convergence at all genera).
 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
 one-particle Bergman reduction, Fredholm determinant). At genus~$0$
 the algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}.
 BV=bar in the coderived category is proved for all four shadow
 classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains
 conjectural (Conjecture~\ref{conj:master-bv-brst}; class~M
 chain-level false).






thinking
**Analyzing internal consistency**

I’m noticing a contradiction here. Since we’re modifying the target to fix a theorem, I should also resolve any internal inconsistencies on the surface. However, the user didn’t explicitly ask for that finding. Still, I think I should re-read the modified sections to verify that there are no new inconsistencies and to finish every finding. If the table still suggests that G/L/C coderived is proven, it might be consistent, but I’m unsure about L/C being proved.
thinking
**Evaluating genus conditions**

I'm thinking about the genus conditions and whether to apply the Jacobi heuristic as a potential option. I see that "C" and "M" are both conditional, but maybe changing this might be more complex than I originally thought. It feels important to clarify the current BV/bar landscape while distinguishing between "scalar" and "chain/coderived." I want to ensure my remarks align globally with the theorem to prevent contradictions, which means updating both the classification and the introduction paragraph for clarity.
thinking
**Clarifying coderived BV/bar comparisons**

I'm looking at the coderived BV/bar comparisons. They depend on the harmonic-factorization and coacyclicity package for the class-M discrepancy, and our genuswise chain-level identification is still conjectural. I realize that I might be overstating things here. It could be worth mentioning that for classes G/L/C, explicit vanishing mechanisms exist in obstruction analysis, but the global chain-level quasi-isomorphism isn't proven beyond genus 0. I want to clarify that the only higher-genus result is the Heisenberg scalar identity, and there's a critical need for a coacyclicity proof.
thinking
**Mentioning conditional status**

I need to include the explicit conditional status in the theorem title and the proof itself. I'm considering a potential rewrite for clarity. The new title could be something like: "Conditional BV=bar criterion in the coderived category." I should ensure the claim's status reflects this conditional aspect. Plus, I’ll need to define that \(\cA\) is a chirally Koszul algebra. This helps set the stage for the theorem and makes everything more precise and understandable.
thinking
**Evaluating mathematical logic**

I’m considering keeping the focus on physical motivation while discussing coderived categories. It seems that while curvature appears, it doesn't alone prove the BV/bar comparison. Curved objects don’t imply zero in \(D^{co}\), and I still need to show that the comparison cone is coacyclic. This is a key correction. I also need to update earlier statements regarding final paragraphs to reflect these adjustments and avoid contradictions. A reduction in claims may be necessary, especially in class C.
thinking
**Refining theorem presentation**

Since the user asked for the findings, I might minimize the focus to just the theorem block and the introductory paragraph. However, leaving the remark that contains the false proof claim for class M and `m_0 x = d^2(x)` would just bring back the issue. So, I’ll need to edit that remark as well. I think I can change the part starting from "The current BV/bar landscape is therefore," but maybe I can leave the earlier class C argument untouched if it's not necessary.
codex
Pre-edit verification for the load-bearing status change:

```text
environment: theorem
label: \label{thm:bv-bar-coderived}
prefix match (AP125): Y
status before: ProvedHere
proof completeness for unconditional theorem? N
strongest truthful surviving status: Conditional
scope: all g >= 0, but higher-genus coderived step requires extra hypotheses
missing inputs: (1) class-M harmonic factorization; (2) coacyclicity/weak-equivalence proof for the comparison cone
verdict: ACCEPT
```

I’m editing the theorem block and the nearby status prose now. The goal is to preserve the real genus-0 and scalar results while removing the false coderived proof and replacing it with the exact conditional bridge the appendix actually supports.






thinking
**Updating identification details**

I'm verifying the identification through four independent paths, but I think there’s some overclaiming there. I might need to fix local consistency since we changed the theorem to conditional. I’ll start by patching the first sentence to say, "The expected identification... is approached by four independent paths…" Then I’ll consider adjustments for the table and the concluding paragraph to ensure everything aligns better. The table currently states G/L/C unconditional and M conditional, so I'll refine that too.
thinking
**Patching modifications cautiously**

I’m considering whether the table and first sentence might over-claim something. Since that can be noticeable, maybe I need to adjust the table too. I think about changing a sentence to make it clearer while still meaningful. 

I could also modify the table column heading and entries for clarity. However, the table risks losing some original meaning. I wonder if simplifying by removing the table and replacing it with a short paragraph might be the best route, even if it’s a big change.
thinking
**Refining edits thoughtfully**

I think I'm on the right track here. I just need to avoid using em dashes since that seems a bit sloppy. Moderate edits sound just right. Also, at the theorem proof, I should probably avoid saying "for every chirally Koszul algebra" in an unconditional way. It might be better to start with "Let \(\cA\)... Assume..." That feels clearer. I should also mention that `Definitions\ref{def:filtered-curved-model}` and similar references are in the appendix; that’s a good addition!
thinking
**Considering mathematical remarks**

I’m thinking about the status of certain mathematical statements. Since it’s not a theorem, maybe it’s not a big deal? The phrase “proved elsewhere” feels a bit peculiar. Also, I’m pondering whether preserving the existing status macro is necessary. The remark isn’t too claim-heavy, which is good. I should double-check that saying “or equivalently has coacyclic cone” is fine. It could be key, especially regarding how morphisms work in the factorization coderived category.
thinking
**Considering remarks on the Verdier quotient**

I’m thinking about the Verdier quotient and how the class G (the genus-0 chain) might relate to local and scalar theorems. I see that the class C remark ends with a possibly redundant table. It could be more concise to link to the next theorem instead of using a duplicate table. I should rewrite the end of class C to have a paragraph instead. It’ll reduce redundancy and clarify how the mechanisms come together at the scalar level.
thinking
**Preparing theorem and remarks for clarity**

I'm noting that Theorem\ref{thm:bv-bar-coderived} specifies the conditional coderived upgrade, while Remark\ref{rem:bv-sewing-chain-level-classes} gives a clear class-by-class status. This change helps avoid bad tables and false logic, which is great! I will rewrite Remark\ref{rem:bv-sewing} accordingly. I'll also update the theorem block to be conditional and revise the remarks about the higher genus and missing packages. Lastly, it might be best to avoid mentioning \operatorname{Im}(d) after the patch. I'll search carefully and prepare the patch.

thinking
**Evaluating patch issues**

It seems the patch failed due to a mismatch, likely because the table formatting might be slightly different. I wonder if the issue relates to the line `\textbf{conditional}`. I think it’d be good to inspect the exact current block from the file to either check or modify it using tools like `nl` or `sed`. I'll need to dig deeper into the formatting to see where it went wrong!
codex
The first patch was too wide against a moving block. I’m re-reading the exact local text and applying a narrower patch region by region so I don’t accidentally stomp unrelated content.
exec
/bin/zsh -lc "sed -n '1800,1875p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1868,2015p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20,55p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
modular operad) and has the following class-by-class status.
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lccl}
\toprule
Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
\midrule
$\mathsf{G}$ \textup{(}Heisenberg\textup{)}
 & $2$ & \textbf{unconditional} & no interaction vertices \\
$\mathsf{L}$ \textup{(}affine KM\textup{)}
 & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
$\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
 & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
$\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
 & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
\bottomrule
\end{tabular}
\end{center}
For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
 succeeded in 52ms:
 (class~G), which is already resolved.
 For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
 itself a fundamental generator with its own propagator channel;
 the quartic vertex involves $T$ coupling to $T$, and the
 harmonic correction does not factor through a free subsystem.
\end{enumerate}
The three mechanisms combine to show that the quartic
harmonic-propagator correction vanishes for the $\beta\gamma$
system at genus~$1$, despite the nonzero quartic shadow
$Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
resolved obstructions~(1) and~(2), this establishes
Conjecture~\ref{conj:master-bv-brst} at the scalar level for
class~C at genus~$1$.
The \textbf{current BV/bar landscape} is therefore:
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lcccl}
\toprule
Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
 succeeded in 51ms:
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
classical master equation is $d_{\mathrm{bar}}^2 = 0$, and anomaly
cancellation ($c = 26$) is the condition $\kappa_{\mathrm{tot}} = 0$
on the total Virasoro central charge of matter plus ghosts. Do
they agree at all genera?

A natural obstruction sits in the way. At higher genus, the BV
Laplacian receives contributions from handle-gluing amplitudes that
involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
the bar differential collects OPE residues along FM boundary strata.
The two prescriptions are proved to match on the coderived category
for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
the BV and bar complexes are quasi-isomorphic in
$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
chain level, the identification holds for classes~$\mathsf{G}$,
$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
The Heisenberg case is resolved at the chain level at all genera:
exec
/bin/zsh -lc "sed -n '2015,2060p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
In the Costello--Li framework of twisted supergravity, the bulk
theory on $\mathrm{AdS}_{d+1}$ is computed by Witten diagrams
using the bulk propagator, while the boundary theory is computed
by the bar complex using the boundary OPE. The mismatch between
bulk and boundary propagators at one loop ($g = 1$) is the
holographic anomaly: the Weyl anomaly coefficient
$a - c$ in $4d$ becomes the harmonic discrepancy
$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
framework. The coderived resolution says: this anomaly is
\emph{exact} in the correct cohomological sense. The boundary
bar complex computes the same physics as the bulk BV complex,
provided one works in the coderived category where curvature is
absorbed into the differential.

\emph{The categorical viewpoint.}
The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
home for curved dg~algebras: it is the homotopy category of
dg~comodules over the bar coalgebra $B(\cA)$ in which
$d^2 = m_0 \cdot \mathrm{id}$ is permitted. The bar complex
$B(\cA)$ always satisfies $D_B^2 = 0$ (the total bar differential

thinking
**Applying patches sequentially**

I’m thinking about applying narrower patches one by one, aiming for maybe four calls. I need to make sure there's no parallel execution with `apply_patch`, as that could complicate things. My plan is to start by patching the intro first, which seems like a logical first step. By taking it step by step, I can keep everything organized and under control. Let’s see how that goes!
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -29,12 +29,14 @@
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..86c73a0820f4811ea77103c1bb17ee3904dd90fc
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..86c73a0820f4811ea77103c1bb17ee3904dd90fc
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.


thinking
**Patching remarks and theorems**

I'm planning to patch class C remark and the related theorem blocks. I think I might need one or two patches, starting from "The three mechanisms combine..." all the way to the end of class C remarks. I'm not entirely sure what changes I should implement, but I'll take a closer look to ensure everything aligns properly. It feels like a straightforward process, but I want to make sure I don’t overlook anything important!
codex
I’ve replaced the chapter opening overclaim. Next I’m rewriting the local class-M discussion so the section no longer claims coderived exactness from `m_0 = d^2/d`; that argument is being replaced with the actual coacyclicity criterion from the appendix.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1813,39 +1813,19 @@
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..d4a38aecb87e6e33d989c105f2608cc79267e545
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..d4a38aecb87e6e33d989c105f2608cc79267e545
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..d4a38aecb87e6e33d989c105f2608cc79267e545
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1847,5 +1847,6 @@
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
@@ -1853,14 +1854,14 @@
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
@@ -1868,6 +1869,2 @@
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
@@ -1875,8 +1872,8 @@
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..798052ecc58b8dd778e3a54364a4d795b807647a
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,40 +1845,37 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..798052ecc58b8dd778e3a54364a4d795b807647a
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,40 +1845,37 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1880,4 +1880,4 @@
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
@@ -1885,5 +1885,29 @@
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
@@ -1894,5 +1918,5 @@
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
@@ -1900,45 +1924,28 @@
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
@@ -1947,18 +1954,17 @@
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..a6e144a271a8485d8fc86b40dd3a4f081d4e7cf7
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
 \[
+ f_g \colon
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
+\[
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..a6e144a271a8485d8fc86b40dd3a4f081d4e7cf7
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
 \[
+ f_g \colon
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
+\[
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1990,9 +1990,9 @@
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
@@ -2005,9 +2005,8 @@
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
@@ -2023,4 +2022,4 @@
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
@@ -2029,3 +2028,6 @@
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
@@ -2033,8 +2035,7 @@
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fb3129c4671d7a32c3a2d13530b73b51b6e0df76
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fb3129c4671d7a32c3a2d13530b73b51b6e0df76
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

codex
The structural rewrite is in place. I’m re-reading the modified theorem and both surrounding remarks line by line now, checking for any leftover claim inflation, bad references, or places where the old false `Im(d)` logic still survives.
exec
/bin/zsh -lc "sed -n '20,55p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2015,2060p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1800,2015p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "operatorname{Im}(d)" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
classical master equation is $d_{\mathrm{bar}}^2 = 0$, and anomaly
cancellation ($c = 26$) is the condition $\kappa_{\mathrm{tot}} = 0$
on the total Virasoro central charge of matter plus ghosts. Do
they agree at all genera?

A natural obstruction sits in the way. At higher genus, the BV
Laplacian receives contributions from handle-gluing amplitudes that
involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
the bar differential collects OPE residues along FM boundary strata.
What is proved in this chapter is the genus-$0$ BV/bar comparison
and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
the obstruction analysis isolates why classes~$\mathsf{G}$,
$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
class~$\mathsf{M}$, but it does not by itself produce a global
chain-level quasi-isomorphism. The higher-genus coderived upgrade is
therefore recorded only as the conditional criterion of
Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
the missing input is precisely a proof that the harmonic discrepancy
 succeeded in 51ms:
home for curved dg~algebras: it is the homotopy category of
dg~comodules over the bar coalgebra $B(\cA)$ in which
$d^2 = m_0 \cdot \mathrm{id}$ is permitted. The bar complex
$B(\cA)$ always satisfies $D_B^2 = 0$ (the total bar differential
squares to zero regardless of curvature), so $B(\cA)$ lives
natively in $D^{\mathrm{co}}$. The BV complex, with its
$d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
satisfies the same curved relation. The coderived
category is the minimal ambient in which both objects are
well-defined. The ordinary derived
category, which requires $d^2 = 0$, is too restrictive: it
forces a choice of ``strictification'' (lifting the curvature
into the differential via a Maurer--Cartan twist), and different
choices produce inequivalent chain complexes. The coderived
category avoids this choice. By
Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
curved objects are not set to zero in this localization; the
comparison map still has to be shown to have coacyclic cone.

The upshot: the BV quantisation of the worldsheet sigma model
 succeeded in 51ms:
 in the fundamental fields, it factors through the
 genus-$1$ trace of the \emph{free} $\beta\gamma$ system
 (class~G), which is already resolved.
 For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
 itself a fundamental generator with its own propagator channel;
 the quartic vertex involves $T$ coupling to $T$, and the
 harmonic correction does not factor through a free subsystem.
\end{enumerate}
The three mechanisms combine to show that the quartic
harmonic-propagator correction vanishes for the $\beta\gamma$
system at genus~$1$, despite the nonzero quartic shadow
$Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
resolved obstructions~(1) and~(2), this establishes
Conjecture~\ref{conj:master-bv-brst} at the scalar level for
class~C at genus~$1$. What it does not yet supply is a global
all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
quartic harmonic discrepancy
$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
identity, and the missing higher-genus step is to prove that the full
 exited 1 in 53ms:

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fb3129c4671d7a32c3a2d13530b73b51b6e0df76
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

codex
There’s one local contradiction left inside the class-C remark itself: it calls the “free `\beta\gamma` system” class `G`. I’m removing that classification slip now so the surrounding rectified text is internally coherent.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1800,4 +1800,4 @@
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Searching theorem status**

I need to check the status of the theorem references in my file, particularly looking for mentions of it being "proved." I’ll use a search command to find specific lines in the document associated with the theorem. It’s essential that I don’t make too many overclaims about its validity. I’ll focus on any mentions of “proved” and narrow it down to the top mentions, especially those that are conditional. Let’s see what I find!
exec
/bin/zsh -lc 'rg -n -F "m_0 = d''^2/d" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"ClaimStatus(ProvedHere|Conditional)\" chapters/connections/bv_brst.tex | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "operatorname{Im}(d)" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F "thm:bv-bar-coderived" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
383:\ClaimStatusProvedHere]
488:\ClaimStatusProvedHere]
639:\ClaimStatusProvedHere]
681:\begin{proposition}[Koszul duality preserves BRST anomaly cancellation; \ClaimStatusProvedHere]
764:\ClaimStatusProvedHere]
916:\ClaimStatusProvedHere]
1029:\ClaimStatusProvedHere]
1125:\ClaimStatusConditional]
1168:\ClaimStatusConditional]
1192:\ClaimStatusProvedHere]
1304:\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
1360:\begin{theorem}[Conditional BV functor package; \ClaimStatusConditional]
1410:\ClaimStatusProvedHere]
1656:\ClaimStatusProvedHere]
1882:\ClaimStatusConditional]%
2194:\ClaimStatusProvedHere]
 exited 1 in 51ms:

 succeeded in 52ms:
37:Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
1827:the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
1874:conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
1883:\label{thm:bv-bar-coderived}%
1956:mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

codex
The false `Im(d)`/`m_0=d^2/d` language is gone. I’m doing one last structural pass: checking that the new theorem only cites existing definitions/propositions and that the modified labels stay stable without forcing cross-file edits.
exec
/bin/zsh -lc "rg -n -F \"\\label{def:curved-weak-equiv}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{def:provisional-coderived}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{prop:provisional-embedding}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{def:coacyclic-fact}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1798,2010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{def:coderived-fact}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '26,48p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
214:\label{def:curved-weak-equiv}
 succeeded in 52ms:
234:\label{def:provisional-coderived}
 succeeded in 51ms:
654:\label{prop:provisional-embedding}
 succeeded in 51ms:
518:\label{def:coacyclic-fact}
 succeeded in 51ms:
  1798	 the quartic vertex is built from composites of those
  1799	 same pairs. When the harmonic correction is expanded
  1800	 in the fundamental fields, it factors through the
  1801	 genus-$1$ trace of the underlying free-field sector,
  1802	 whose scalar anomaly is already resolved.
  1803	 For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  1804	 itself a fundamental generator with its own propagator channel;
  1805	 the quartic vertex involves $T$ coupling to $T$, and the
  1806	 harmonic correction does not factor through a free subsystem.
  1807	\end{enumerate}
  1808	The three mechanisms combine to show that the quartic
  1809	harmonic-propagator correction vanishes for the $\beta\gamma$
  1810	system at genus~$1$, despite the nonzero quartic shadow
  1811	$Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
  1812	resolved obstructions~(1) and~(2), this establishes
  1813	Conjecture~\ref{conj:master-bv-brst} at the scalar level for
  1814	class~C at genus~$1$. What it does not yet supply is a global
  1815	all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
  1816	quartic harmonic discrepancy
  1817	$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 succeeded in 52ms:
    26	A natural obstruction sits in the way. At higher genus, the BV
    27	Laplacian receives contributions from handle-gluing amplitudes that
    28	involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
    29	the bar differential collects OPE residues along FM boundary strata.
    30	What is proved in this chapter is the genus-$0$ BV/bar comparison
    31	and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
    32	the obstruction analysis isolates why classes~$\mathsf{G}$,
    33	$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
    34	class~$\mathsf{M}$, but it does not by itself produce a global
    35	chain-level quasi-isomorphism. The higher-genus coderived upgrade is
    36	therefore recorded only as the conditional criterion of
    37	Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
    38	filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
    39	the missing input is precisely a proof that the harmonic discrepancy
    40	factors through the curvature. The Heisenberg case is resolved at the
    41	scalar level at all genera:
    42	$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
    43	= \kappa \cdot \lambda_g^{\mathrm{FP}}$
    44	\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
    45	For general algebras what survives at every genus is the scalar
 succeeded in 54ms:
546:\label{def:coderived-fact}
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Evaluating introduction clarity**

I need to continue the lines after 2010, but I think I have enough content for now. However, there seems to be an issue in line 37 of the introduction where I mention a "comparison map of filtered curved models whose cone is coacyclic." It looks like the term "coacyclic cone" might not be defined properly right there. I should consider searching for "filtration models whose cone is coacyclic." Additionally, I need to ensure there's no confusing language like "proved for all shadow classes" left in the file.
exec
/bin/zsh -lc 'rg -n -F "for all four shadow classes" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "coacyclic cone" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"proved\" chapters/connections/bv_brst.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
1877:comparison map has coacyclic cone in the sense of
1963: coacyclic cone in the sense of
2032:comparison map still has to be shown to have coacyclic cone.
 succeeded in 51ms:
30:What is proved in this chapter is the genus-$0$ BV/bar comparison
81: \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
98:the intended BV reading of these proved algebraic statements, not
107:The proved object is the universal Maurer--Cartan class~$\Theta_\cA$
130:The displayed hierarchy is a heuristic BV translation of the proved
131:modular MC hierarchy, not a proved BV identity: the
281:full comparison is not proved here.
307:identification between these two quantities is not proved in the
1230: $\mathrm{Vir}_{26-c}$ is the proved M/S-level shadow partner used in
1347:For affine Kac--Moody algebras, this is proved:
1955:is not proved in this chapter. It is the candidate genus-independent
2333:$bc$ ghosts gives the MC5 genus-$0$ case proved in
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}



thinking
**Considering build commands**

I'm thinking about running the command `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. It might take 10 seconds, which seems a bit long. I wonder if I could use an existing build script instead. Also, it seems like searching for the build-surface skill might not be necessary for this task. I'm trying to find the most efficient approach to get this done smoothly.
thinking
**Running verification checks**

I need to run a full build, but the verification loop is asking me to check if `\ref` and `\label` are valid. It seems we already checked that using grep, which should be fine. However, I wonder if I should inspect the differences just to be sure. I'll use `git diff -- chapters/connections/bv_brst.tex` to see what changes have been made. It’s always better to double-check!
codex
I’ve verified the new references exist and the old false exactness language is fully removed. I’m doing one last diff review against the file to make sure the rectification stayed minimal and didn’t accidentally alter anything outside the intended proof surface.
exec
/bin/zsh -lc 'git diff -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9de..fedbee3 100644
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@ A natural obstruction sits in the way. At higher genus, the BV
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Considering execution commands**

I think I should use plain pipes since the compile process can take a while, especially if the repository is large and possibly partially built already. Setting `yield_time_ms` to 1000 might help, but I wonder if I need to add a session ID as well. It seems like `exec_command` returns the session ID only for tty, right? I might just need to wait, though it feels like there could be too much output truncated.
codex
The text is coherent on reread. I’m running a quiet LaTeX build once to catch any syntax or reference break introduced by the patch; if that fails or times out, I’ll report that explicitly.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error -quiet main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

 exited 12 in 1.38s:
Rc files read:
  NONE
Latexmk: Run number 1 of rule 'pdflatex'
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
Latexmk: Getting log file 'main.log'
Have index file 'main.idx', main.ind main
Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'main.log' and/or above output for details

codex
The build is running. I’m polling the log until it either succeeds or exposes a real TeX error on this surface.
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Investigating log errors**

I need to check the main.log file for any errors. I'll search within the file, possibly using "rg" to look for `bv_brst.tex` or the `!` symbol. It seems the best approach is to inspect the tail of the log or focus on the area around the specific error. This should help me understand what went wrong, so I can address it properly. Let's get started on this!
exec
/bin/zsh -lc 'rg -n "''^!|bv_brst'"\\.tex|Undefined control sequence|LaTeX Error|Emergency stop|Fatal error\" main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '54580,54740p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1374:! File ended while scanning use of \@writefile.
1393:!  ==> Fatal error occurred, no output PDF file produced!
 succeeded in 51ms:

exec
/bin/zsh -lc 'tail -n 80 main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Package: mhsetup 2021/03/18 v1.4 programming setup (MH)
)
\g_MT_multlinerow_int=\count409
\l_MT_multwidth_dim=\dimen341
\origjot=\skip268
\l_MT_shortvdotswithinadjustabove_dim=\dimen342
\l_MT_shortvdotswithinadjustbelow_dim=\dimen343
\l_MT_above_intertext_sep=\dimen344
\l_MT_below_intertext_sep=\dimen345
\l_MT_above_shortintertext_sep=\dimen346
\l_MT_below_shortintertext_sep=\dimen347
\xmathstrut@box=\box136
\xmathstrut@dim=\dimen348
) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thmtools.sty
Package: thmtools 2023/05/04 v0.76
\thmt@toks=\toks63
\c@thmt@dummyctr=\count410
(/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-patch.sty
Package: thm-patch 2023/05/04 v0.76
(/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/parseargs.sty
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Analyzing error in aux file**

I'm facing an error from the aux file, likely because it's been corrupted before this attempt. I wonder if I need to clean and rebuild it, though the user only asked about the file itself. Maybe I should inspect the .toc file since the error seems linked to the theorem environment changes? The issue arises at the beginning of the document, so I need to check the last lines of `.aux` for any unclosed braces in the chapter. I'll focus on the `bv_brst.aux` file tail.
codex
The build didn’t get far enough to typeset this chapter; it died while rereading a malformed auxiliary file at `\begin{document}`. I’m checking whether that malformed write came from the edited theorem title/status block or from stale preexisting aux state.
exec
/bin/zsh -lc 'tail -n 80 chapters/connections/bv_brst.aux' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Conditional BV" chapters/connections/bv_brst.aux main.toc main.out main.thm main.lof main.lot' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:bv-bar-coderived" chapters/connections/bv_brst.aux main.toc main.out main.thm' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "coacyclic cone" chapters/connections/bv_brst.aux main.toc main.out main.thm' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
tail: chapters/connections/bv_brst.aux: No such file or directory
 exited 2 in 51ms:
rg: chapters/connections/bv_brst.aux: No such file or directory (os error 2)
rg: main.thm: No such file or directory (os error 2)
rg: main.lof: No such file or directory (os error 2)
rg: main.lot: No such file or directory (os error 2)
 exited 2 in 51ms:
rg: chapters/connections/bv_brst.aux: No such file or directory (os error 2)
rg: main.thm: No such file or directory (os error 2)
 exited 2 in 51ms:
rg: chapters/connections/bv_brst.aux: No such file or directory (os error 2)
rg: main.thm: No such file or directory (os error 2)
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Exploring auxiliary files**

I'm considering whether there might be split auxiliary files in the root directory. To clarify this, I think it makes sense to list the auxiliary files available. I’m curious about their structure and how they might relate to what I'm working on. Let's take a closer look to ensure I understand what’s there! It could help in organizing things more effectively.
exec
/bin/zsh -lc "rg --files -g '*.aux'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
verify-main.aux
main.aux
bar_cobar_adjunction_curved.aux
chapters/examples/kac_moody.aux
chapters/examples/free_fields.aux
chapters/examples/level1_bridge.aux
chapters/examples/moonshine.aux
chapters/examples/w_algebras.aux
chapters/examples/lattice_foundations.aux
chapters/examples/beta_gamma.aux
chapters/examples/deformation_quantization.aux
chapters/examples/w3_holographic_datum.aux
chapters/frame/heisenberg_frame.aux
chapters/frame/preface.aux
chapters/theory/koszul_pair_structure.aux
chapters/theory/chiral_modules.aux
chapters/theory/chiral_hochschild_koszul.aux
chapters/theory/higher_genus.aux
chapters/theory/algebraic_foundations.aux
chapters/theory/configuration_spaces.aux
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

exec
/bin/zsh -lc 'rg -n -F "bv_brst" main.aux main.toc main.out' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'tail -n 80 main.aux' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'tail -n 120 main.toc' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
\newlabel{constr:transfer-ainf}{{9.3.1}{565}{Transferred \texorpdfstring {$\Ainf $}{A-infinity}-structure}{construction.9.3.1}{}}
\citation{LV12}
\citation{LV12}
\@writefile{loe}{\contentsline {theorem}{\ifthmt@listswap Theorem~9.3.2\else \numberline {9.3.2}Theorem\fi \thmtformatoptarg {Tree formula for transferred operations \cite  {LV12}; }}{566}{theorem.9.3.2}\protected@file@percent }
\newlabel{thm:tree-formula}{{9.3.2}{566}{Tree formula for transferred operations \cite {LV12}; \ClaimStatusProvedElsewhere }{theorem.9.3.2}{}}
\@@wrindexm@m{main}{tree formula!for transfer|hyperpage}{566}
\@writefile{loe}{\contentsline {remark}{\ifthmt@listswap Remark~9.3.3\else \numberline {9.3.3}Remark\fi \thmtformatoptarg {Tree-level only}}{566}{remark.9.3.3}\protected@file@percent }
\newlabel{rem:tree-level}{{9.3.3}{566}{Tree-level only}{remark.9.3.3}{}}
\@writefile{loe}{\contentsline {example}{\ifthmt@listswap Example~9.3.4\else \numberline {9.3.4}Example\fi \thmtformatoptarg {Trees for $\tilde  {m}_4$}}{566}{example.9.3.4}\protected@file@percent }
\newlabel{ex:trees-m4}{{9.3.4}{566}{Trees for \texorpdfstring {$\tilde {m}_4$}{m4-tilde}}{example.9.3.4}{}}
\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.3.5\else \numberline {9.3.5}Proposition\fi \thmtformatoptarg {Sign computation \cite  {LV12}; }}{566}{proposition.9.3.5}\protected@file@percent }
\newlabel{prop:transfer-signs}{{9.3.5}{566}{Sign computation \cite {LV12}; \ClaimStatusProvedElsewhere }{proposition.9.3.5}{}}
\citation{Kadeishvili80}
\citation{DGMS75}
\citation{Kon99}
\citation{LV12}
\@writefile{toc}{\contentsline {section}{\numberline {9.4}Applications to minimal models}{567}{section.9.4}\protected@file@percent }
\newlabel{sec:minimal-models}{{9.4}{567}{Applications to minimal models}{section.9.4}{}}
\@writefile{loe}{\contentsline {definition}{\ifthmt@listswap Definition~9.4.1\else \numberline {9.4.1}Definition\fi \thmtformatoptarg {Minimal model}}{567}{definition.9.4.1}\protected@file@percent }
\newlabel{def:minimal-model}{{9.4.1}{567}{Minimal model}{definition.9.4.1}{}}
 succeeded in 52ms:
\contentsline {subsubsection}{\numberline {G.7.6.1}From Loday--Vallette to our conventions}{2591}{subsubsection.G.7.6.1}%
\contentsline {subsubsection}{\numberline {G.7.6.2}From Beilinson--Drinfeld to our conventions}{2592}{subsubsection.G.7.6.2}%
\contentsline {subsubsection}{\numberline {G.7.6.3}From Costello--Gwilliam to our conventions}{2592}{subsubsection.G.7.6.3}%
\contentsline {subsection}{\numberline {G.7.7}Examples of translation}{2592}{subsection.G.7.7}%
\contentsline {subsection}{\numberline {G.7.8}Sign rules for this manuscript}{2592}{subsection.G.7.8}%
\contentsline {subsubsection}{\numberline {G.7.8.1}Koszul signs}{2593}{subsubsection.G.7.8.1}%
\contentsline {subsubsection}{\numberline {G.7.8.2}Collision divisor signs}{2593}{subsubsection.G.7.8.2}%
\contentsline {subsubsection}{\numberline {G.7.8.3}Arnold relation signs}{2593}{subsubsection.G.7.8.3}%
\contentsline {subsubsection}{\numberline {G.7.8.4}Residue signs}{2593}{subsubsection.G.7.8.4}%
\contentsline {subsection}{\numberline {G.7.9}Common pitfalls and how to avoid them}{2593}{subsection.G.7.9}%
\contentsline {subsubsection}{\numberline {G.7.9.1}Pitfall 1: forgetting Koszul signs}{2593}{subsubsection.G.7.9.1}%
\contentsline {subsubsection}{\numberline {G.7.9.2}Pitfall 2: confusing hat notations}{2593}{subsubsection.G.7.9.2}%
\contentsline {subsubsection}{\numberline {G.7.9.3}Pitfall 3: collision divisor ordering}{2594}{subsubsection.G.7.9.3}%
\contentsline {subsubsection}{\numberline {G.7.9.4}Pitfall 4: Arnold relation orientation}{2594}{subsubsection.G.7.9.4}%
\contentsline {subsection}{\numberline {G.7.10}Sign convention dictionary}{2594}{subsection.G.7.10}%
\contentsline {subsubsection}{\numberline {G.7.10.1}Conversion formulas}{2595}{subsubsection.G.7.10.1}%
\contentsline {subsubsection}{\numberline {G.7.10.2}Explicit sign calculations}{2595}{subsubsection.G.7.10.2}%
\contentsline {subsection}{\numberline {G.7.11}Master comparison table}{2596}{subsection.G.7.11}%
\contentsline {subsubsection}{\numberline {G.7.11.1}Detailed conversion formulas}{2596}{subsubsection.G.7.11.1}%
\contentsline {paragraph}{\numberline {G.7.11.1.1}Koszul signs.}{2596}{thmt@dummyctr.dummy.5478}%
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Considering file safety**

I'm thinking about the action safety related to editing the assigned file. It seems best not to proceed with the edit. I'll mention that the build couldn't validate due to preexisting aux corruption that isn't related to the file I've modified. It might be useful to run the command `nl -ba main.aux | tail -n 20` to check for any incomplete lines, but maybe that's not necessary. I also want to inspect `git status --short` to confirm which files have changed and if it's okay.
exec
/bin/zsh -lc 'git status --short -- chapters/connections/bv_brst.tex main.aux main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M chapters/connections/bv_brst.tex
 M main.aux
 M main.log
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

codex
Updated [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:30) so the higher-genus BV/bar coderived lane is no longer overstated. The opening status prose, the class-by-class status remarks, the theorem at [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1881), and the two follow-up remarks now say exactly what is proved and what remains conditional.

I re-read the modified sections and checked that the new references point to existing coderived definitions/propositions. I also ran a quiet `latexmk`; it failed before reaching this chapter because `main.aux` is already malformed at an unrelated old write (`Proposition 9.7.5`), so I could not get a clean full-build confirmation from this tree.

## Rectification Summary
- [FIXED] finding 1 — removed the unsupported use of `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}` as if proved, and rewrote the surrounding prose to identify it explicitly as the missing class-`M` mechanism rather than established input.
- [CONDITIONAL] finding 1 — changed `thm:bv-bar-coderived` from `\ClaimStatusProvedHere` to `\ClaimStatusConditional`, with the theorem now conditional on the harmonic-factorization package plus the coderived weak-equivalence input.
- [FIXED] finding 2 — deleted the false coderived argument that treated `m_0\cdot x = d^2(x)` / `\operatorname{Im}(d)` as enough in `D^{\mathrm{co}}`, and replaced it with the correct coderived criterion via `def:curved-weak-equiv`, `def:provisional-coderived`, and `prop:provisional-embedding`.
- [NARROWED] finding 2 — narrowed the theorem from an unconditional coderived quasi-isomorphism for all chirally Koszul algebras to a conditional coderived comparison criterion: a higher-genus comparison map must be a weak equivalence, equivalently have coacyclic cone after passage to the coderived formalism.
- [FIXED] adjacent consistency issue — removed the local class-status overclaim in the nearby remarks and corrected the “free `\beta\gamma` = class G” slip inside the class-`C` discussion.
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ba5e9ded3a36d9836652509c660b0039344438c0..fedbee31c9928ce085ab6011be2d31988585c69b
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -27,16 +27,18 @@
 Laplacian receives contributions from handle-gluing amplitudes that
 involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
 the bar differential collects OPE residues along FM boundary strata.
-The two prescriptions are proved to match on the coderived category
-for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
-the BV and bar complexes are quasi-isomorphic in
-$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
-chain level, the identification holds for classes~$\mathsf{G}$,
-$\mathsf{L}$, and~$\mathsf{C}$ but fails for class~$\mathsf{M}$
-(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
-of Theorem~\ref{thm:kz-classical-quantum-bridge} provides the
-genus-$0$ comparison for classes~$\mathsf{G}$ and~$\mathsf{L}$).
-The Heisenberg case is resolved at the chain level at all genera:
+What is proved in this chapter is the genus-$0$ BV/bar comparison
+and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
+the obstruction analysis isolates why classes~$\mathsf{G}$,
+$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
+class~$\mathsf{M}$, but it does not by itself produce a global
+chain-level quasi-isomorphism. The higher-genus coderived upgrade is
+therefore recorded only as the conditional criterion of
+Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
+filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
+the missing input is precisely a proof that the harmonic discrepancy
+factors through the curvature. The Heisenberg case is resolved at the
+scalar level at all genera:
 $F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
@@ -1796,8 +1798,8 @@
  the quartic vertex is built from composites of those
  same pairs. When the harmonic correction is expanded
  in the fundamental fields, it factors through the
- genus-$1$ trace of the \emph{free} $\beta\gamma$ system
- (class~G), which is already resolved.
+ genus-$1$ trace of the underlying free-field sector,
+ whose scalar anomaly is already resolved.
  For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  itself a fundamental generator with its own propagator channel;
  the quartic vertex involves $T$ coupling to $T$, and the
@@ -1809,43 +1811,23 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes
 Conjecture~\ref{conj:master-bv-brst} at the scalar level for
-class~C at genus~$1$.
-The \textbf{current BV/bar landscape} is therefore:
-\begin{center}
-\small
-\renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lcccl}
-\toprule
-Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
-\midrule
-\textsf{G} \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
-\textsf{L} \textup{(}affine KM\textup{)}
- & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
-\textsf{C} \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
-\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
-\bottomrule
-\end{tabular}
-\end{center}
-For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
-\emph{fails} at the ordinary chain level: the quartic harmonic
-discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
-\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
-$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
-of the holomorphic bar differential. The Fay trisecant identity does
-not cancel it. However, in the coderived category
-$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$,
-and $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in
-$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
-The same mechanism kills all higher-degree obstructions:
-$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
-$\operatorname{Im}(d)$ in $D^{\mathrm{co}}$ at every degree.
-This resolves Conjecture~\ref{conj:master-bv-brst} in
-$D^{\mathrm{co}}$ for all shadow classes
-(Theorem~\ref{thm:bv-bar-coderived}).
+class~C at genus~$1$. What it does not yet supply is a global
+all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
+quartic harmonic discrepancy
+$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
+\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
+identity, and the missing higher-genus step is to prove that the full
+harmonic discrepancy factors through the curvature as
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1},
+\]
+and then to show that the resulting comparison cone is coacyclic in
+the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
+records exactly that coderived upgrade conditionally, and
+Remark~\ref{rem:bv-sewing-chain-level-classes} summarizes the current
+class-by-class status.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1863,125 +1845,128 @@
 $\delta^{\mathrm{ns}}\colon
 \overline{\mathcal{M}}_{g,n+2} \to
 \overline{\mathcal{M}}_{g+1,n}$.
-The identification is verified by four independent paths
-(operator definition, spectral sequence, Heisenberg extraction,
-modular operad) and has the following class-by-class status.
+Four complementary descriptions of this comparison
+\textup{(}operator definition, spectral sequence, Heisenberg
+extraction, modular operad\textup{)} lead to the following
+class-by-class obstruction profile on the current written record.
 \begin{center}
 \small
 \renewcommand{\arraystretch}{1.15}
-\begin{tabular}{lccl}
+\begin{tabular}{lcl}
 \toprule
-Class & $r_{\max}$ & $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ (chain) & Mechanism \\
+Class & Status on current record & Comment \\
 \midrule
 $\mathsf{G}$ \textup{(}Heisenberg\textup{)}
- & $2$ & \textbf{unconditional} & no interaction vertices \\
+ & genus-$0$ chain; all-genera scalar & no interaction vertices \\
 $\mathsf{L}$ \textup{(}affine KM\textup{)}
- & $3$ & \textbf{unconditional} & Jacobi kills harmonic correction \\
+ & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
- & $4$ & \textbf{unconditional} & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
+ & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & $\infty$ & \textbf{conditional} & harmonic correction nonzero \\
+ & unresolved at chain level & harmonic correction survives \\
 \bottomrule
 \end{tabular}
 \end{center}
-For classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$, the
-harmonic-propagator correction vanishes and the chain-level
-identification holds unconditionally
-(Proposition~\ref{prop:chain-level-three-obstructions}).
 For class~$\mathsf{M}$, the quartic discrepancy
 $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
 \kappa / \operatorname{Im}(\tau)$ is not a coboundary
-in the ordinary chain complex; the identification holds only in
-the coderived category $D^{\mathrm{co}}$
-(Theorem~\ref{thm:bv-bar-coderived} below).
-Computational verification:
-\texttt{compute/lib/theorem\_bv\_sewing\_engine.py}
-(four proof paths, all shadow classes tested).
+in the ordinary chain complex. A coderived upgrade requires the
+conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
+one must prove the curvature-factorization formula for the full
+harmonic discrepancy and then prove that the resulting BV/bar
+comparison map has coacyclic cone in the sense of
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
 \end{remark}
 
-\begin{theorem}[BV$=$bar in the coderived category;
-\ClaimStatusProvedHere]%
+\begin{theorem}[Conditional BV$=$bar in the coderived category;
+\ClaimStatusConditional]%
 \label{thm:bv-bar-coderived}%
 \index{BV algebra!bar complex identification!coderived category|textbf}%
 \index{coderived category!BV/bar identification|textbf}%
-For every chirally Koszul algebra~$\cA$, the BV complex and the bar
-complex are quasi-isomorphic in the coderived category
-$D^{\mathrm{co}}(\cA)$:
+Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
+comparison is the chain-level quasi-isomorphism of
+Theorem~\ref{thm:bv-bar-geometric}. Assume that for each genus
+$g \geq 1$ there is a comparison morphism of filtered curved
+factorization models
+\[
+ f_g \colon
+ C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
+ \longrightarrow
+ B^{(g)}(\cA)
+\]
+such that:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item for class~$\mathsf{M}$ the harmonic discrepancy satisfies
+\[
+ \delta_r^{\mathrm{harm}}
+ \;=\;
+ c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
+ \qquad\text{for every } r \geq 4;
+\]
+\item each~$f_g$ is a weak equivalence in the sense of
+ Definition~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Then the genus-$g$ BV complex and bar complex become isomorphic in
+the provisional coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
+coderived category $D^{\mathrm{co}}(\cA)$:
 \[
  C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  \;\simeq_{D^{\mathrm{co}}}\;
  B^{(g)}(\cA)
  \qquad\text{for all } g \geq 0.
 \]
-In particular, the identification holds for all four shadow
-classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-and~$\mathsf{M}$.
+In particular, a proof of \textup{(i)} together with the coacyclicity
+criterion in \textup{(ii)} would supply the missing class~$\mathsf{M}$
+coderived comparison.
 \end{theorem}
 
 \begin{proof}
-At genus~$0$, the identification is the content of
-Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
+At genus~$0$, the comparison is the chain-level quasi-isomorphism
+of Theorem~\ref{thm:bv-bar-geometric}.
 
-At genus $g \geq 1$, the chain-level obstructions are classified by
-Proposition~\ref{prop:chain-level-three-obstructions}.
-Obstructions~(1) and~(2) (propagator regularity and moduli
-dependence) are resolved for all classes by the Hodge decomposition
-and the Quillen anomaly formula. Obstruction~(3) (higher-degree
-coupling through the harmonic propagator) produces, at degree~$r$,
-a discrepancy
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
-\]
-where $c_r(\cA)$ is a shadow coefficient
-(with $c_4 = Q^{\mathrm{contact}}$ at the quartic level).
-For classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$,
-the obstructions vanish at the chain level
-(no vertices, Jacobi, harmonic decoupling respectively),
-so the chain-level quasi-isomorphism implies the coderived one
-a~fortiori.
+For $g \geq 1$, assumption~\textup{(ii)} is exactly the hypothesis
+needed to pass from the filtered curved comparison map~$f_g$ to the
+provisional coderived category:
+Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
+as the morphisms inverted in
+Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
+becomes an isomorphism in
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
+Proposition~\ref{prop:provisional-embedding} then identifies this
+with an isomorphism in the full coderived category on the bounded-below
+PBW-filtered surface treated in this chapter.
 
-For class~$\mathsf{M}$:
-in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
-$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
-Hence $m_0 \cdot x = d(d(x)) \in \operatorname{Im}(d)$ for every
-element~$x$. Each degree-$r$ obstruction is a multiple of a positive
-power of~$m_0$:
-\[
- \delta_r^{\mathrm{harm}}
- \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
- \;\in\; \operatorname{Im}(d),
-\]
-since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
-for every $k \geq 1$. In particular, $\delta_4 =
-Q^{\mathrm{contact}} \cdot m_0 \in \operatorname{Im}(d)$,
-and every higher $\delta_r$ vanishes in $D^{\mathrm{co}}$ by the
-same mechanism. The chain map
-$C^{\bullet}_{\mathrm{BV}} \to B^{(g)}(\cA)$ therefore becomes a
-quasi-isomorphism after passage to $D^{\mathrm{co}}$.
+Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
+mechanism isolated by
+Proposition~\ref{prop:chain-level-three-obstructions}: it is the
+candidate factorization that would allow one to verify
+assumption~\textup{(ii)} from the harmonic-propagator analysis.
+The chapter does not prove \textup{(i)} or the resulting
+coacyclicity statement, so the coderived comparison remains
+conditional.
 \end{proof}
 
-\begin{remark}[Genus $\geq 2$ validity]
+\begin{remark}[Higher-genus missing input]
 \label{rem:bv-bar-coderived-higher-genus}%
 \index{coderived category!higher-genus validity}%
 The factored form
 $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
-holds at every genus~$g \geq 1$, not only at genus~$1$.
-On~$\Sigma_g$, the harmonic propagator
-$P_{\mathrm{harm}} = \sum_{i=1}^{g} \omega_i(z) \otimes
-\bar\omega_i(w)$
-involves~$g$ holomorphic $1$-forms, and each harmonic insertion in an
-degree-$r$ graph produces a factor of $P_{\mathrm{harm}}$.
-The fiberwise curvature $d^2_{\mathrm{fib}} = m_0 = \kappa(\cA) \cdot \omega_g$ arises from
-exactly this harmonic piece via the Quillen anomaly, so every
-degree-$r$ discrepancy is a polynomial in~$m_0$ with the stated
-exponent. The coderived absorption mechanism
-($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
-genus-independent, whence the theorem holds at all genera.
-The chain-level identification for classes~$\mathsf{G}$, $\mathsf{L}$,
-$\mathsf{C}$ is likewise genus-unrestricted: the vanishing mechanisms
-(no vertices, Jacobi, harmonic decoupling) depend on the OPE
-structure, not on~$g$.
+is not proved in this chapter. It is the candidate genus-independent
+mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
+have to show two things:
+\begin{enumerate}[label=\textup{(\roman*)},nosep]
+\item every harmonic insertion in the BV/bar discrepancy lands,
+ after harmonic projection, in the curvature direction
+ $m_0 = \kappa(\cA)\cdot\omega_g$ with the stated exponent;
+\item the comparison map built from this factorization has
+ coacyclic cone in the sense of
+ Definitions~\ref{def:coacyclic-fact}
+ and~\ref{def:curved-weak-equiv}.
+\end{enumerate}
+Neither step is established here, so the higher-genus
+class~$\mathsf{M}$ coderived comparison remains conditional for every
+genus~$g \geq 1$.
 \end{remark}
 
 \begin{remark}[Why the coderived category is inevitable]
@@ -2003,13 +1988,13 @@
 piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
 \emph{full} propagator; the bar complex uses only
 $P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
-is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
-\rfloor - 1}$. But $P_{\mathrm{harm}} = m_0/\kappa$ is the
-curvature divided by the modular characteristic: it is the
-geometric representative of the genus-$1$ obstruction class.
-In the coderived category, $m_0$ is exact ($m_0 = d^2/d$),
-so $P_{\mathrm{harm}}$ is cohomologically trivial: the harmonic
-modes do not contribute to the physical amplitudes.
+is controlled by the harmonic piece. This shows why curvature
+appears in higher genus: the harmonic sector is invisible to the
+genus-$0$ bar differential but survives in the BV propagator.
+Passing to the coderived setting is therefore natural once
+$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. What it does
+\emph{not} show by itself is that the discrepancy vanishes there;
+one still has to prove that the comparison cone is coacyclic.
 
 \emph{The spacetime viewpoint.}
 In the Costello--Li framework of twisted supergravity, the bulk
@@ -2018,13 +2003,12 @@
 by the bar complex using the boundary OPE. The mismatch between
 bulk and boundary propagators at one loop ($g = 1$) is the
 holographic anomaly: the Weyl anomaly coefficient
-$a - c$ in $4d$ becomes the harmonic discrepancy
-$\delta_4 = Q^{\mathrm{contact}} \cdot m_0$ in the algebraic
-framework. The coderived resolution says: this anomaly is
-\emph{exact} in the correct cohomological sense. The boundary
-bar complex computes the same physics as the bulk BV complex,
-provided one works in the coderived category where curvature is
-absorbed into the differential.
+$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
+correction to the BV/bar comparison. The coderived formalism
+packages this anomaly as curvature data rather than forcing a
+strict differential. The missing mathematical step is still to
+show that the comparison map becomes an isomorphism after
+localizing at coacyclic objects.
 
 \emph{The categorical viewpoint.}
 The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
@@ -2036,22 +2020,24 @@
 natively in $D^{\mathrm{co}}$. The BV complex, with its
 $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
 satisfies the same curved relation. The coderived
-quasi-isomorphism identifies the two objects in the minimal
-category where both are well-defined. The ordinary derived
+category is the minimal ambient in which both objects are
+well-defined. The ordinary derived
 category, which requires $d^2 = 0$, is too restrictive: it
 forces a choice of ``strictification'' (lifting the curvature
 into the differential via a Maurer--Cartan twist), and different
 choices produce inequivalent chain complexes. The coderived
-category avoids this choice.
+category avoids this choice. By
+Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
+curved objects are not set to zero in this localization; the
+comparison map still has to be shown to have coacyclic cone.
 
 The upshot: the BV quantisation of the worldsheet sigma model
 and the algebraic bar construction of the boundary vertex algebra
-compute the same cohomology in the coderived category. The chain
-level discrepancy for class~$\mathsf{M}$ is \emph{not} an
-error but an artifact of working in the wrong category: the
-ordinary derived category sees an obstruction that the coderived
-category absorbs. The curvature is not a bug; it is a feature
-that the coderived category is designed to handle.
+live naturally in the same curved homological framework. The
+chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
+signal that the coderived category is unnecessary; it is the reason
+the coderived category is the correct ambient. What remains open is
+the comparison theorem itself.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

tokens used
173,095
