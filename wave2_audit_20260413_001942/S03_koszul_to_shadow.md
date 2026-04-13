# S03_koszul_to_shadow (673s)

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:349` — PROBLEM: the proof of `thm:genus-graded-koszul` sets `(\mathcal A^!)^{(g)} := \bar B^{(g)}(\mathcal A)`, so the bar coalgebra is identified with the Koszul dual algebra. That contradicts the seam source in `chapters/theory/chiral_koszul_pairs.tex:160-166`, which distinguishes bar coalgebra, bar cohomology, and dual algebra, and it also contradicts the later dg definition in `higher_genus_modular_koszul.tex:550-555`, which says `\bar B_X(\cA)` is the Koszul dual coalgebra and `\cA^!` appears only after dualization. The same theorem also uses a direct-sum “completion” at `:335`, while the file’s own completed bar object is the `\hbar`-adic product at `:568` and `:2562`. FIX: rewrite the theorem/proof so the completed object is `\bar B_X^{\mathrm{full}}(\cA):=\prod_{g\ge0}\hbar^g\bar B_X^{(g)}(\cA)`, the genus-`g` dual coalgebra is `(\mathcal A^i)^{(g)}:=H^*(\bar B_X^{(g)}(\mathcal A))`, and the dual algebra is obtained only after dualization, e.g. `(\mathcal A^!)^{(g)}:=((\mathcal A^i)^{(g)})^\vee`.

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2593` — PROBLEM: `thm:genus-internalization` states the full scalar trace `\operatorname{tr}(\Theta_{\cA})=\sum_{g\ge1}\kappa(\cA)\lambda_g` unconditionally for every simple-Lie-symmetry algebra. The same file later restricts that all-genera formula to the proved uniform-weight lane in `:3530-3534` and again in `:7755-7758`; only the genus-1 scalar trace is universal. FIX: replace lines `2593-2600` with: `whose genus-1 scalar trace is \kappa(\cA)\lambda_1; on the proved uniform-weight lane this refines to \operatorname{tr}(\Theta_{\cA})=\sum_{g\ge1}\kappa(\cA)\lambda_g. Its clutching compatibility recovers ...` and change the proof at `:2616-2620` to cite that same qualifier instead of calling the full formula unconditional.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:16215` — PROBLEM: the shadow-depth definition first presents exactly four classes `\mathbf G/\mathbf L/\mathbf C/\mathbf M`, then immediately says lattices realize every finite depth `d\ge5` at `:16217-16230`. Later the theorem puts lattice VOAs back in class `\mathbf G` at `:16482-16483`, and `chapters/theory/chiral_koszul_pairs.tex:75-90` treats the seam as exactly four classes with depths `{2,3,4,\infty}`. Those claims cannot all be true on one seam surface. FIX: keep the four-class theorematic surface and delete the fine-depth lattice paragraph at `16217-16230` and the parallel lattice-depth paragraph at `16529-16540`; replace `16215-16216` by `These four classes are exhaustive and mutually exclusive on the standard-family theorematic surface used in this chapter.` Also rename the depth symbol `\kappa_d` at `:16172`, `:16174`, `:16183`, and `:28671` to `d_{\mathrm{sh}}` so scalar `\kappa` is no longer overloaded.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14442` — PROBLEM: the remark says “The five main theorems are projections of the scalar level `\Theta_{\cA}^{\le2}=\kappa(\cA)`,” but the table immediately underneath assigns Theorem A to the genus-0 twisting component, B to `\mathrm{FT}^2\simeq\mathrm{id}`, C to cross-polarization, and H to a degree-preserving sub-MC. Only Theorem D is scalar-level. FIX: replace lines `14442-14445` with `The five main theorems are projections of the shadow obstruction tower. Theorem D is the scalar-level projection \Theta_{\cA}^{\le2}; Theorems A, B, C, and H come respectively from the genus-0 twisting component, the Feynman-transform involution, the cross-polarized splitting, and the degree-preserving sub-MC sector.`

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14484` — PROBLEM: the file states `\kappa=\operatorname{av}(r(z))` as the theorem-D extraction rule; the same bare formula recurs at `:2943`. But the same file later gives the affine Kac--Moody correction `\operatorname{av}(r(z))+\tfrac12\dim(\fg)=\kappa(V_k(\fg))` at `:3117-3124`. The seam therefore drops the non-abelian Sugawara shift exactly where it connects ordered `r`-matrix data to scalar `\kappa`. FIX: at `:14484` replace the sentence by `Theorem~D extracts the scalar \kappa from the coinvariant degree-2 projection of the ordered spectral r-matrix; in the trace-form convention this is \operatorname{av}(r(z)) for abelian families and \operatorname{av}(r(z))+\tfrac12\dim(\fg) for affine Kac--Moody.` Replace `:2943` by the same family-sensitive statement.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:48` — PROBLEM: the chapter opens by treating `\Theta_{\cA}`, `\kappa`, `\mathfrak C`, and `\mathfrak Q` as unqualified bar-theoretic invariants, but only later admits at `:3556-3563` that MC2 in this file is the symmetric/coinvariant statement and the ordered lift `\Theta_{\cA}^{E_1}` lives in the ordered chapter. The seam from `chiral_koszul_pairs.tex` never explicitly says whether the shadow tower here is built from `B^{\mathrm{ord}}` or from its coinvariant shadow. FIX: insert after line `47`: `In this chapter the shadow tower is the symmetric/coinvariant projection of the ordered E_1 theory. The ordered bar complex B^{\mathrm{ord}}(\cA) and its Maurer--Cartan element \Theta_{\cA}^{E_1} are constructed in Chapter~\ref{chap:e1-modular-koszul}; the present \Theta_{\cA}, \kappa, \mathfrak C, \mathfrak Q are their \Sigma_n-coinvariant images under averaging.`

## Summary
Checked: 2 | Findings: 6 | Verdict: FAIL


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
session id: 019d83c7-8316-74a3-8b08-9d38229c5e33
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: SEAM AUDIT between chiral_koszul_pairs.tex and higher_genus_modular_koszul.tex.

Koszul pairs→Shadow tower. Check: (a) Koszul equivalences feed correctly into shadow tower, (b) the shadow tower uses the right bar (B^ord vs B^Sigma), (c) kappa definition consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers

thinking
**Planning the audit process**

I need to conduct a thorough audit between two files and identify transition points. This involves inspecting the files in detail, using grep to search for specific terms like Koszul and shadow. I must compare formulas with the census and focus on findings, as the user wants a review. If there are no findings, I should state that clearly. Including summary counts, ensuring precision for file lines, and frequently updating my plan will be helpful too.
codex
Seam audit scope is the transition from `chiral_koszul_pairs.tex` into `higher_genus_modular_koszul.tex`, with emphasis on Koszul-pair outputs, bar choice, and `\kappa` consistency. I’m using `deep-beilinson-audit` for the adversarial pass and starting by reading the required constitutional surfaces plus the two target files in context.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

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

 succeeded in 54ms:
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

thinking
**Auditing files for context**

I need to audit the seams in the documents to find relevant files and dependencies related to transition points. It sounds like I should use commentary, possibly with a scope lock, and maybe update my plan once I gather enough context. I’ll locate files and relevant terms, likely starting with `chapters/theory/chiral_koszul_pairs.tex` and `chapters/theory/higher_genus_modular_koszul.tex`. I should inspect the ends of the first chapter and the beginnings of the second for references. I'll search for label references across both using keywords.
codex
I’ve loaded the constitutional surfaces. Next I’m mapping the seam itself: chapter order, cross-references between the two files, and every local occurrence of `Koszul`, `shadow`, `B^ord`, `B^\\Sigma`, `\kappa`, and averaging language.
exec
/bin/zsh -lc "rg -n \"chiral_koszul_pairs|higher_genus_modular_koszul\" main.tex chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:22599:%: from higher_genus_modular_koszul.tex:2888; lambda=0 -> 1, lambda=1/2 -> -1/2 verified
main.tex:992:\include{chapters/theory/chiral_koszul_pairs}
chapters/theory/higher_genus.tex:6:\input{chapters/theory/higher_genus_modular_koszul}
chapters/theory/higher_genus_foundations.tex:2542:% Theorem A now lives in chiral_koszul_pairs.tex
chapters/theory/higher_genus_foundations.tex:2561:% are in chiral_koszul_pairs.tex.
 succeeded in 50ms:
     1	\chapter{Chiral Koszul duality}
     2	\label{chap:koszul-pairs}
     3	
     4	\index{chiral Koszul duality|textbf}
     5	\index{twisting morphism!chiral|textbf}
     6	\index{Francis--Gaitsgory|textbf}
     7	
     8	Classical Koszul duality, in the sense of
     9	Priddy~\cite{Priddy70} and
    10	Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
    11	algebras over a field: the bar complex is a tensor coalgebra on a
    12	finite-dimensional vector space, the cobar functor inverts it
    13	when bar cohomology is concentrated in degree one, and the
    14	duality exchanges quadratic algebras with quadratic coalgebras.
    15	Three features of chiral algebras on algebraic curves defeat
    16	this framework simultaneously. First, chiral algebras are
    17	\emph{curved}: the bar differential on the genus expansion
    18	satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
    19	rather than $d^2 = 0$, so the classical bar-cobar adjunction,
    20	which requires strict nilpotence, does not apply beyond genus
 succeeded in 51ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	


thinking
**Analyzing quantum files**

It looks like the query failed due to a null character, so I should rerun it in a simpler way. I need to read more from both files, focusing on the end of the chiral_koszul_pairs and the transition points in higher_genus_modular_koszul, especially around the seam and references. 

I should inspect labels and theorems in both files and check definitions like modular characteristic and shadow algebra. There’s a need for a thorough search for citations and potential inconsistencies in definitions.
thinking
**Reviewing mathematical definitions**

I need to check for contradictions like \(d_{\text{bar}}^2 = 0\) versus \(d_{\text{fib}}^2\) being fiberwise only. They mention genus expansion and possibly bar differentials, which could be ambiguous. The user wants the seam to ensure Koszul equivalences correctly feed into the shadow tower.

In the higher_genus_modular_koszul, line 10 mentions \(\barB^{(g)}(\mathcal{A})\) without clarifying ordered versus symmetric. I should search for terms like \(B^{\text{ord}}\) and \(B^{\Sigma}\) for possible inconsistencies. Additionally, line 49 discusses the modular characteristic at degree 2; I need to see if this aligns with earlier statements or definitions.
codex
The first pass already exposed the core seam language. I’m now drilling into every local `\kappa` and bar-object mention in both files, plus the exact definitions they cite, to separate true contradictions from merely vague prose.
exec
/bin/zsh -lc "rg -n '\\\\kappa|kappa|modular characteristic|scalar lane|shadow tower|shadow algebra|B\\\\"'^'"\\\\{ord\\\\}|B\\\\"'^'"\\\\{\\\\Sigma\\\\}|ordered bar|symmetric bar|coinvariant|averag|Theta|R-matrix|r-matrix' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'def:modular-characteristic-package|def:scalar-lane|thm:modular-characteristic|thm:genus-universality|thm:mc2-bar-intrinsic|thm:koszul-equivalences-meta|prop:e1-shadow-r-matrix|constr:dk-shadow-projections|def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:recursive-existence|thm:shadow-archetype-classification|prop:sc-formal-iff-class-g' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '260,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '260,720p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\kappa|kappa|modular characteristic|scalar lane|shadow tower|shadow algebra|B\\^\\{ord\\}|B\\^\\{\\Sigma\\}|ordered bar|symmetric bar|coinvariant|averag|Theta|R-matrix|r-matrix)
                                                                                           ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
   260	 is quadratic/Koszul in the ordinary operadic sense;
   261	\item the filtration converges strongly on $\bar{B}_X(\cA)$ and
   262	 $\Omega_X(\cC)$.
   263	\end{enumerate}
   264	\end{definition}
   265	
   266	\begin{remark}[Construction versus resolution]\label{rem:construction-vs-resolution}
   267	For every augmented chiral algebra $\cA$, the bar
   268	$\bar{B}_X(\cA)$ and cobar $\Omega_X(\bar{B}_X(\cA))$ exist as
   269	constructions. But the counit
   270	$\Omega_X(\bar{B}_X(\cA)) \to \cA$ is a quasi-isomorphism
   271	\emph{only when $\tau$ is a Koszul morphism}
   272	(Theorem~\ref{thm:bar-cobar-inversion-qi}).
   273	Off the Koszul locus, the bar-cobar object persists in the
   274	provisional coderived category
   275	$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
   276	(Appendix~\ref{sec:coderived-models}),
   277	not in the ordinary derived category.
   278	This is the chiral/factorization analogue of the fundamental
   279	theorem of twisting morphisms \cite[Theorem~2.3.1]{LV12}.
 succeeded in 52ms:
Total output lines: 1020

chapters/theory/chiral_koszul_pairs.tex:61:Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
chapters/theory/chiral_koszul_pairs.tex:78:(Theorem~\ref{thm:shadow-archetype-classification}), record the
chapters/theory/chiral_koszul_pairs.tex:90:(Proposition~\ref{prop:sc-formal-iff-class-g}).
chapters/theory/chiral_koszul_pairs.tex:111:(Theorem~\ref{thm:modular-characteristic});
chapters/theory/chiral_koszul_pairs.tex:131:(Theorem~\ref{thm:mc2-bar-intrinsic}) recovers the classical
chapters/theory/chiral_koszul_pairs.tex:1285:\ldots$ of Theorem~\ref{thm:mc2-bar-intrinsic}: the $m_n$ measure
chapters/theory/chiral_koszul_pairs.tex:2016:\label{thm:koszul-equivalences-meta}
chapters/theory/chiral_koszul_pairs.tex:2437:(item~(iii) of Theorem~\ref{thm:koszul-equivalences-meta})
chapters/theory/chiral_koszul_pairs.tex:2469:Theorem~\textup{\ref{thm:koszul-equivalences-meta}(iii)}\textup{)}
chapters/theory/chiral_koszul_pairs.tex:2573:\label{prop:sc-formal-iff-class-g}
chapters/theory/chiral_koszul_pairs.tex:2696: Theorem~\textup{\ref{thm:koszul-equivalences-meta}}\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:2711:Theorem~\ref{thm:koszul-equivalences-meta}.
chapters/theory/chiral_koszul_pairs.tex:2816:Theorem~\ref{thm:koszul-equivalences-meta} is equivalent
chapters/theory/chiral_koszul_pairs.tex:3019:Theorem~\textup{\ref{thm:koszul-equivalences-meta}}.
chapters/theory/chiral_koszul_pairs.tex:3027:Theorem~\ref{thm:koszul-equivalences-meta}, establishing
chapters/theory/chiral_koszul_pairs.tex:3141:(Theorem~\ref{thm:koszul-equivalences-meta}). Beyond this boundary
chapters/theory/chiral_koszul_pairs.tex:3172:Theorem~\ref{thm:koszul-equivalences-meta} requires, at its core,
chapters/theory/chiral_koszul_pairs.tex:3218:(Theorem~\ref{thm:koszul-equivalences-meta}) characterizes chiral
 succeeded in 51ms:
   260	
   261	\begin{proof}
   262	The argument has three steps.
   263	
   264	\emph{Step~1: MCG acts on the bar differential.}
   265	The genus-completed bar differential
   266	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
   267	is built from the modular operad structure on
   268	$\{\overline{\mathcal{M}}_{g,n}\}$
   269	(Theorem~\ref{thm:bar-modular-operad}).
   270	At genus~$g$, the component $d_\cA^{(g)}$ is defined by
   271	summing over boundary strata of
   272	$\overline{\mathcal{M}}_{g,n}$, with each stratum
   273	contributing an integral of OPE data against the
   274	logarithmic propagator along the corresponding edge.
   275	The mapping class group
   276	$\mathrm{MCG}(\Sigma_g)$ acts on the Teichm\"uller space
   277	$\mathcal{T}_{g,n}$, and the moduli space
   278	$\overline{\mathcal{M}}_{g,n} = \overline{\mathcal{T}}_{g,n}
   279	/ \mathrm{MCG}$ is the orbifold quotient.
codex
I’m into the load-bearing definitions now. The next pass is around the theorem/definition labels that the seam relies on: the 12-way Koszul equivalence theorem in the first file, and the modular characteristic / scalar lane / MC / shadow definitions in the second.
exec
/bin/zsh -lc "rg -n -F 'B"'^{ord}'"' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ordered bar' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'B"'^{'"\\Sigma}' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'averag' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'coinvariant' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'symmetric bar' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:13704:\item \emph{$E_1$ ordered bar complex}
chapters/theory/higher_genus_modular_koszul.tex:27034: The ordered bar complex $B^{\mathrm{ord}}(\mathrm{Vir}_{13})
chapters/theory/higher_genus_modular_koszul.tex:31944:  The ordered bar complex factorization under non-separating
chapters/theory/higher_genus_modular_koszul.tex:32018:(Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$)
chapters/theory/higher_genus_modular_koszul.tex:32040:different operations on the ordered bar complex, and
chapters/theory/higher_genus_modular_koszul.tex:32044:At \emph{generic} level, the ordered bar complex
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3562:Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
chapters/theory/higher_genus_modular_koszul.tex:14479:Theorem~A is the averaged form of the $E_1$ bar-cobar
chapters/theory/higher_genus_modular_koszul.tex:14481:Theorem~B is the averaged form of the $E_1$~Quillen equivalence;
chapters/theory/higher_genus_modular_koszul.tex:14482:Theorem~C is the averaged form of complementarity in the ordered
chapters/theory/higher_genus_modular_koszul.tex:14489:and higher Yangian coherences that averaging discards
chapters/theory/higher_genus_modular_koszul.tex:22284:\begin{remark}[Evidence for a motivic genus ladder in the averaging kernel]
chapters/theory/higher_genus_modular_koszul.tex:22285:\label{rem:motivic-evidence-genus2-averaging-kernel}
chapters/theory/higher_genus_modular_koszul.tex:22286:\index{averaging kernel!motivic evidence}
chapters/theory/higher_genus_modular_koszul.tex:22295:$E_2^*, E_4, E_6$, and the genus-$1$ averaging kernel enlarges
chapters/theory/higher_genus_modular_koszul.tex:22326:\begin{conjecture}[Motivic content of the genus-$2$ averaging kernel]
chapters/theory/higher_genus_modular_koszul.tex:22327:\label{conj:motivic-content-genus2-averaging-kernel}
chapters/theory/higher_genus_modular_koszul.tex:22329:\index{averaging kernel!motivic content conjecture|textbf}
chapters/theory/higher_genus_modular_koszul.tex:22356:For general $g$, the genus-$g$ averaging kernel is governed by mixed
chapters/theory/higher_genus_modular_koszul.tex:22376:\begin{remark}[Weight filtration on the averaging kernel]
chapters/theory/higher_genus_modular_koszul.tex:22377:\label{rem:motivic-weight-filtration-averaging-kernel}
chapters/theory/higher_genus_modular_koszul.tex:22380:of Conjecture~\ref{conj:motivic-content-genus2-averaging-kernel}.
chapters/theory/higher_genus_modular_koszul.tex:31990:  the integrable quotient). The averaging map $\av_0$ is
chapters/theory/higher_genus_modular_koszul.tex:32862:The averaging map $\av_2$ at degree~$2$ sends the
chapters/theory/higher_genus_modular_koszul.tex:32867:genus~$0$ and genus~$1$: the averaging map is a local
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3550:argument. The universal MC element on the coinvariant modular
chapters/theory/higher_genus_modular_koszul.tex:3555:\index{MC2!coinvariant scope}
chapters/theory/higher_genus_modular_koszul.tex:3556:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
chapters/theory/higher_genus_modular_koszul.tex:3689:\item \emph{$\Theta_\cA$ lies in the completed coinvariant algebra.}
chapters/theory/higher_genus_modular_koszul.tex:14473:\begin{remark}[The five theorems as coinvariant shadows of the $E_1$ theory]
chapters/theory/higher_genus_modular_koszul.tex:14476:Each row of the table above is the $\Sigma_n$-coinvariant
chapters/theory/higher_genus_modular_koszul.tex:15766:representation, so the coinvariant space
chapters/theory/higher_genus_modular_koszul.tex:22288:$E_1$ data discarded by the coinvariant projection
chapters/theory/higher_genus_modular_koszul.tex:22330:For the ordered $E_1$-to-coinvariant projection
chapters/theory/higher_genus_modular_koszul.tex:22381:At degree~$n$, the kernel of the coinvariant projection
chapters/theory/higher_genus_modular_koszul.tex:30698:\label{prop:planar-forest-coinvariant}
chapters/theory/higher_genus_modular_koszul.tex:30699:\index{planar planted forest!coinvariant quotient}
chapters/theory/higher_genus_modular_koszul.tex:30704:\label{eq:planar-forest-coinvariant}
chapters/theory/higher_genus_modular_koszul.tex:30709:which is the $\Sigma$-coinvariant quotient: at each vertex with
chapters/theory/higher_genus_modular_koszul.tex:30724:The coinvariant identification holds because
chapters/theory/higher_genus_modular_koszul.tex:30726:setting, and the coinvariant quotient divides by exactly this
chapters/theory/higher_genus_modular_koszul.tex:30747:planar planted forests. The coinvariant quotient recovers the
chapters/theory/higher_genus_modular_koszul.tex:30772:Proposition~\ref{prop:planar-forest-coinvariant}.
chapters/theory/higher_genus_modular_koszul.tex:30806:\item The $\Sigma_n$-coinvariant quotient recovers the
chapters/theory/higher_genus_modular_koszul.tex:30888:The $\Sigma_n$-coinvariant quotient recovers the symmetric ambient
 exited 1 in 51ms:


thinking
**Inspecting theoretical details**

I'm noticing that B^ord/B^Sigma isn't mentioned in the early seam, so I need to inspect around 3550 and other numbers like 14473 and 32862. It seems like the initial section of the seam doesn't mention E1->coinvariant until later, which could be an issue. I'll need to read the relevant lines carefully. Plus, I want to check out the theorem in chiral_koszul_pairs called `thm:koszul-equivalences-meta`, especially around 2016 and line 16580.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1980,2105p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3488,3575p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32850,32890p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14460,14505p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2400,2765p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1980	would exchange the associated varieties of $L_k$ and~$L_{k'}$:
  1981	$\overline{\mathbb{O}} \leftrightarrow
  1982	\overline{d_{\mathrm{BV}}(\mathbb{O})}$. If that principle holds,
  1983	it imposes a \emph{compatibility constraint}: the Li--bar
  1984	obstructions for~$L_k$ and~$L_{k'}$ should be
  1985	Barbasch--Vogan dual.
  1986	\end{remark}
  1987	
  1988	\begin{remark}[Comparison with the Kac--Shapovalov criterion]
  1989	\label{rem:li-bar-vs-kac-shapovalov}
  1990	\index{Li filtration!comparison with Kac--Shapovalov}
  1991	
  1992	Theorem~\ref{thm:associated-variety-koszulness} refines
  1993	Theorem~\ref{thm:kac-shapovalov-koszulness} as follows.
  1994	The Shapovalov form~$G_h$ detects null vectors weight by weight.
  1995	The Li filtration organizes these null vectors \emph{geometrically}:
  1996	a null vector at weight~$h$ in the vacuum module corresponds
  1997	to a relation in $R_V = \operatorname{gr}^F V$ at Li
  1998	filtration level~$p$, and the Poisson bracket determines
  1999	whether this relation propagates to the bar complex via~$d_1$.
 succeeded in 50ms:
 32850	space of flat sections with prescribed singular behaviour at
 32851	the puncture. The genus-$0$ entry $\dim H^1 = 4$ uses
 32852	$\chi(\PP^1 \setminus \{0, \infty\}) = 0$ for the
 32853	once-punctured sphere (the relative coordinate lives on
 32854	$\CC^\times$), so
 32855	$\chi = 0$ and the $H^1$-dimension does not follow from
 32856	$\chi$ alone; it is computed directly from KZ flat sections
 32857	\textup{(}cf.\ \S\ref{subsec:ell-degree2}\textup{)}.
 32858	\end{remark}
 32859	
 32860	\begin{remark}[The symmetric shadow at genus~$2$]
 32861	\label{rem:g2-shadow}
 32862	The averaging map $\av_2$ at degree~$2$ sends the
 32863	$12$-dimensional ordered de~Rham cohomology to
 32864	$\Sigma_2$-coinvariants. The scalar surviving $\av_2$ is
 32865	$\kappa = 3(k+2)/4$
 32866	(equation~\eqref{comp:sl2-kappa}), the same value as at
 32867	genus~$0$ and genus~$1$: the averaging map is a local
 32868	computation (residue extraction), independent of the global
 32869	topology.
 succeeded in 51ms:
  3488	Every shadow invariant of the programme is a projection of
  3489	$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
  3490	the cubic shadow $\mathfrak{C}$ at degree~$3$, the quartic
  3491	resonance $\mathfrak{Q}$ at degree~$4$, and all higher
  3492	obstructions in the Postnikov tower of
  3493	Definition~\ref{def:shadow-postnikov-tower}.
  3494	There is no separate construction for each invariant; there is
  3495	$\Theta_\cA$, and the invariants are what remain after
  3496	forgetting all but finitely many degrees.
  3497	
  3498	\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
  3499	\label{thm:mc2-bar-intrinsic}
  3500	\index{universal Maurer--Cartan class!bar-intrinsic construction}
  3501	\index{MC2!bar-intrinsic proof}
  3502	\index{MC2!full generality}
  3503	Let $\cA$ be a modular Koszul chiral algebra on a smooth
  3504	projective curve~$X$ with non-degenerate invariant form.
  3505	Write
  3506	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
  3507	for the genus-completed bar differential
 succeeded in 51ms:
 14460	 Cross-polarization &
 14461	 $\cA/\cA^!$-sides interact only through $P_{\cA}$ \\
 14462	D (modular char.) &
 14463	 $\Theta_{1,0;0}$ &
 14464	 Genus-$1$ degree-$0$ projection $= \kappa \cdot \lambda_1$ \\
 14465	H (Hochschild) &
 14466	 Degree-preserving sub-MC &
 14467	 Polynomiality from Koszul concentration \\
 14468	\bottomrule
 14469	\end{tabular}
 14470	\end{center}
 14471	\end{remark}
 14472	
 14473	\begin{remark}[The five theorems as coinvariant shadows of the $E_1$ theory]
 14474	\label{rem:five-theorems-as-av-images}
 14475	\index{main theorems!as av-images of E1@$E_1$ theory}
 14476	Each row of the table above is the $\Sigma_n$-coinvariant
 14477	image of a richer $E_1$ statement
 14478	(Theorem~\textup{\ref{thm:e1-primacy}}):
 14479	Theorem~A is the averaged form of the $E_1$ bar-cobar
 succeeded in 52ms:
  2400	\begin{lemma}[$E_2$ collapse at higher genus]\label{lem:e2-higher-genus}
  2401	\ClaimStatusProvedHere
  2402	For a Koszul chiral algebra $\cA$ on a genus-$g$ curve, the PBW
  2403	spectral sequence
  2404	$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g \barB_g(\cA))$
  2405	degenerates at~$E_2$.
  2406	\end{lemma}
  2407	
  2408	\begin{proof}
  2409	The PBW filtration is a filtration by chiral algebras, and the
  2410	Koszulness hypothesis ensures that the associated graded is a
  2411	Koszul complex in the classical sense. The $d_r$ differential
  2412	for $r \geq 2$ maps between PBW-graded components separated
  2413	by~$r$ steps, and the Koszul concentration (all bar cohomology
  2414	is in bar-degree~$0$ on the associated graded) forces these maps
  2415	to have zero source or zero target.
  2416	
  2417	On each geometric fiber (a fixed smooth or stable curve), the
  2418	collision differential is genus-$0$ type (with $d_0^2 = 0$), and
  2419	the genus-$g$ quantum corrections live in higher Leray degrees,

thinking
**Investigating seam mismatches**

I'm considering a potential seam mismatch related to the chiral_koszul_pairs between lines 61-73, which notes 9 unconditional equivalences. There's also a reference in higher_genus at 16580 that discusses theorem item (iv) for each class. It seems I might need to inspect the area around 16580 more closely, as it could connect from Koszul equivalences to shadow classification. This warrants a thorough look!
codex
One real seam risk is convention drift between the genus-zero “equivalences” theorem and the higher-genus shadow classification. I’m checking whether the later chapter silently changes what the “bar”, “depth”, or “\kappa” objects mean when it imports those genus-zero results.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16460,16620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'SC' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'bar complex is' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13700,13740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31930,32055p'" in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
 16460	 \S\ref{sec:higher-depths} \\
 16461	\bottomrule
 16462	\multicolumn{6}{l}{\textsuperscript{$\ast$}%
 16463	 Stratum separation: $\Delta \neq 0$ on charged stratum,
 16464	 $\dim\Defcyc^{(2q)} = 0$.}
 16465	\end{tabular}
 16466	\end{center}
 16467	\end{example}
 16468	
 16469	\begin{theorem}[Shadow archetype classification]
 16470	\label{thm:shadow-archetype-classification}
 16471	\ClaimStatusProvedHere
 16472	\index{shadow depth!classification theorem|textbf}
 16473	\index{shadow archetype classification|textbf}
 16474	Every chirally Koszul algebra in the standard landscape belongs to
 16475	exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
 16476	$\mathbf{F}_4$, or $\mathbf{M}$
 16477	\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 16478	The class is determined by the vanishing pattern of obstruction
 16479	classes at degrees~$3$, $4$, $5$, and the assignments for the
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:84:Koszulness and SC formality are logically independent properties.
chapters/theory/chiral_koszul_pairs.tex:86:in degree one; SC formality is the condition
chapters/theory/chiral_koszul_pairs.tex:87:$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
chapters/theory/chiral_koszul_pairs.tex:89:(Heisenberg and its relatives) is SC-formal
chapters/theory/chiral_koszul_pairs.tex:2466:The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
chapters/theory/chiral_koszul_pairs.tex:2477:& $m_3^{\mathrm{SC}}$
chapters/theory/chiral_koszul_pairs.tex:2478:& $m_4^{\mathrm{SC}}$
chapters/theory/chiral_koszul_pairs.tex:2479:& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
chapters/theory/chiral_koszul_pairs.tex:2523:the contact stratum kills all $m_k^{\mathrm{SC}}$ for $k \geq 5$.
chapters/theory/chiral_koszul_pairs.tex:2534:compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
chapters/theory/chiral_koszul_pairs.tex:2564:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2567:non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
chapters/theory/chiral_koszul_pairs.tex:2568:class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
chapters/theory/chiral_koszul_pairs.tex:2569:nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
chapters/theory/chiral_koszul_pairs.tex:2572:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2575:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2578:\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
chapters/theory/chiral_koszul_pairs.tex:2584:SC-formal\textup{)} is established in
chapters/theory/chiral_koszul_pairs.tex:2587:VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
chapters/theory/chiral_koszul_pairs.tex:2589:For the converse, suppose~$\cA$ is SC-formal.
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:11:algebras over a field: the bar complex is a tensor coalgebra on a
chapters/theory/chiral_koszul_pairs.tex:1134:% means the bar complex is quasi-isomorphic to $\cA_1^i$ in graded chiral
chapters/theory/chiral_koszul_pairs.tex:4265:only the case where the bar complex is finite-dimensional in each
chapters/theory/chiral_koszul_pairs.tex:4285:For non-quadratic chiral algebras (Virasoro, $W$-algebras, Yangians), the $I$-adic completion is essential: the uncompleted bar complex is not quasi-isomorphic to $\mathcal{A}^!$.
chapters/theory/higher_genus_modular_koszul.tex:707:For (a)--(b), the bar complex is explicit
chapters/theory/higher_genus_modular_koszul.tex:721:(Theorem~\ref{thm:verdier-bar-cobar}), (2)~the bar complex is an
chapters/theory/higher_genus_modular_koszul.tex:12961:The modular bar complex is a cofree coalgebra over the
chapters/theory/higher_genus_modular_koszul.tex:13311:bar complex is cofree by
chapters/theory/higher_genus_modular_koszul.tex:13319:The modular bar complex is cofree \emph{as a coalgebra}
chapters/theory/higher_genus_modular_koszul.tex:16527:complexity of $\Theta_\cA$, not whether the bar complex is acyclic.
chapters/theory/higher_genus_modular_koszul.tex:16547:(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
chapters/theory/higher_genus_modular_koszul.tex:16670:not whether the bar complex is acyclic.}%
chapters/theory/higher_genus_modular_koszul.tex:28833:leaves ordered by edge contraction. The tropical bar complex is
chapters/theory/higher_genus_modular_koszul.tex:30336:$\Theta_{\cA}$. The bar complex is the twisting of
 succeeded in 51ms:
 13700	 in the proved corridor \textup{(}principal, hook-type in type~A\textup{)}.
 13701	 For non-principal $f$ outside this corridor, the obstruction is
 13702	 concentrated in the rigid cutting sector: $\operatorname{DS}_f$
 13703	 may fail to commute with the planted-forest corrections $R_\rho$.
 13704	\item \emph{$E_1$ ordered bar complex}
 13705	 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul})}:
 13706	 the cofree-coderivation principle applied to $F\!\Ass$ gives an
 13707	 $E_1$ primitive kernel $\mathfrak{K}_\cA^{E_1}$ with
 13708	 $\operatorname{av}(\mathfrak{K}_\cA^{E_1}) = \mathfrak{K}_\cA$.
 13709	 The genus-$0$, degree-$2$ $E_1$ primitive corolla is the classical
 13710	 $r$-matrix: $K_{0,2}^{\cA,E_1} = r(z)$.
 13711	\end{enumerate}
 13712	\end{remark}
 13713	
 13714	%% ----------------------------------------------------------------
 13715	%% THE PRIMITIVE FLAT CONNECTION
 13716	%% ----------------------------------------------------------------
 13717	
 13718	\subsection{The primitive flat connection and conformal block
 13719	reconstruction}
 succeeded in 50ms:
 31930	  $k$ & $Z_0$ & $Z_1$ & $Z_2$ & $Z_3$ & $Z_4$ \\
 31931	  \midrule
 31932	  $1$ & $1$ & $2$ & $4$ & $8$ & $16$ \\
 31933	  $2$ & $1$ & $3$ & $10$ & $36$ & $136$ \\
 31934	  $3$ & $1$ & $4$ & $20$ & $120$ & $800$ \\
 31935	  $4$ & $1$ & $5$ & $35$ & $329$ & $3{,}611$ \\
 31936	  $5$ & $1$ & $6$ & $56$ & $784$ & $13{,}328$ \\
 31937	  \bottomrule
 31938	  \end{tabular}
 31939	  \end{center}
 31940	  At $k = 1$: $S_{00} = S_{01} = 1/\sqrt{2}$, so
 31941	  $Z_g(1) = 2 \cdot (1/\sqrt{2})^{2-2g} = 2^g$.
 31942	
 31943	\item \textup{(Handle attachment.)}
 31944	  The ordered bar complex factorization under non-separating
 31945	  sewing recovers the TQFT handle-attachment formula:
 31946	  each isospin channel $j$ contributes a handle operator
 31947	  $H_j = S_{0j}^{-2}$, so
 31948	  \begin{equation}\label{eq:handle-attachment}
 31949	    Z_{g+1}
exec
/bin/zsh -lc 'tail -n 160 chapters/theory/chiral_koszul_pairs.tex | nl -ba' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'higher-genus|shadow|modular characteristic|\\kappa|bar complex|ordered|coinvariant|averag' chapters/theory/chiral_koszul_pairs.tex | tail -n 120" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	(see~\S\ref{sec:w3-bar-degree3}).
     2	
     3	However, $\mathcal{W}^k(\mathfrak{g})$ is \emph{chirally Koszul at all
     4	levels}~$k$ by Proposition~\ref{prop:pbw-universality}: the universal
     5	$\mathcal{W}$-algebra is freely strongly generated (Feigin--Frenkel),
     6	so the PBW criterion applies. The quartic obstruction~$[\Lambda]$
     7	measures \emph{shadow depth} (the algebra lies in class~M with
     8	$r_{\max}=\infty$), not failure of chiral Koszulness.
     9	
    10	\emph{Caution}: The \emph{simple quotient}~$\mathcal{W}_k(\mathfrak{g})$
    11	at admissible levels has vacuum null vectors that may obstruct PBW; its
    12	chiral Koszulness remains \textbf{open} (the gap is between bar-Ext and
    13	ordinary Ext).
    14	\end{remark}
    15	
    16	\subsection{Tensor products and Koszulity}
    17	
    18	\begin{remark}[Tensor products in the algebraic setting]
    19	In the classical (non-chiral) setting, tensor products of Koszul algebras are Koszul: if $A_1$ and $A_2$ are Koszul quadratic algebras, then $A_1 \otimes A_2$ is Koszul with $(A_1 \otimes A_2)^! \cong A_1^! \otimes A_2^!$ (Polishchuk--Positselski, Theorem 3.1).
    20	
 succeeded in 51ms:
rg: regex parse error:
    (?:higher-genus|shadow|modular characteristic|\kappa|bar complex|ordered|coinvariant|averag)
                                                  ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'thm:koszul-equivalences-meta|thm:bar-cobar-isomorphism-main|thm:bar-cobar-inversion-qi|thm:fundamental-twisting-morphisms|thm:pbw-koszulness-criterion|def:chiral-koszul-pair|def:chiral-koszul-morphism' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'barB_X' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'barBgeom' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
554:\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
600:(Definition~\ref{def:chiral-koszul-pair}): the bar spectral
874:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
939:Theorem~\ref{thm:pbw-koszulness-criterion}.
1097:Theorem~\ref{thm:pbw-koszulness-criterion}), the
1407:Theorem~\ref{thm:pbw-koszulness-criterion}), the spectral
1562:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}, the spectral
1785:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}
1840:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
2615:Theorem~\ref{thm:bar-cobar-isomorphism-main}. Part~\textup{(iii)} is
3405: (Theorem~\ref{thm:fundamental-twisting-morphisms}).
9731:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): the bar-cobar
14203:$\operatorname{Ran}^{\leq n}$ (Theorem~\ref{thm:bar-cobar-inversion-qi})
16580:(Theorem~\ref{thm:koszul-equivalences-meta}(iv)) for
16772: \textup{(}Theorem~\textup{\ref{thm:koszul-equivalences-meta}},
16820:Aspect~(i): Theorem~\ref{thm:koszul-equivalences-meta}(iii).
28603: Theorems~\textup{\ref{thm:bar-cobar-isomorphism-main}}
29359: \textup{(Thm~\ref{thm:bar-cobar-inversion-qi})} \\
29660: \textup{(}Theorem~\textup{\ref{thm:bar-cobar-inversion-qi}}\textup{)}
29736:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
 succeeded in 57ms:
chapters/theory/chiral_koszul_pairs.tex:764: $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
chapters/theory/chiral_koszul_pairs.tex:767: chain group $\barBgeom^n_h(\cA)$ is finite-dimensional.
chapters/theory/chiral_koszul_pairs.tex:770:$\barBgeom(\cA) \otimes_\tau \cA$ is acyclic in positive degrees.
chapters/theory/chiral_koszul_pairs.tex:774:Equip the Koszul complex $K = \barBgeom(\cA) \otimes_\tau \cA$ with
chapters/theory/chiral_koszul_pairs.tex:777:F_p K^n = \sum_{i+j = n} F_i \barBgeom(\cA) \otimes_\tau F_j \cA.
chapters/theory/chiral_koszul_pairs.tex:792:\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA.
chapters/theory/chiral_koszul_pairs.tex:868:The bar chain group $\barBgeom^n_h(\widehat{\fg}_k)$ is a
chapters/theory/chiral_koszul_pairs.tex:929:the PBW spectral sequence on $\barBgeom(\cA)$ collapses
chapters/theory/chiral_koszul_pairs.tex:933:\dim H^n(\barBgeom(\cA)) = \dim (\cA^!)_n
chapters/theory/chiral_koszul_pairs.tex:934:\qquad\textup{(identifying $(\cA^!)_n = H^n(\barBgeom(\cA))^\vee$)}.
chapters/theory/chiral_koszul_pairs.tex:939: $\dim H^n(\barBgeom(\widehat{\fg}_k)) = \dim (\widehat{\fg}_k^!)_n$
chapters/theory/chiral_koszul_pairs.tex:946: $\dim H^n(\barBgeom(\mathrm{Vir}_c)) = \dim (\mathrm{Vir}_c^!)_n$,
chapters/theory/chiral_koszul_pairs.tex:953:Equip $\barBgeom(\cA)$ with the filtration inherited from
chapters/theory/chiral_koszul_pairs.tex:956:F_p \barBgeom^n(\cA) = \bigl\{
chapters/theory/chiral_koszul_pairs.tex:969:underlying $\barBgeom(\cA)$; the configuration-space form factor
chapters/theory/chiral_koszul_pairs.tex:980:\operatorname{gr}_F \barBgeom(\cA) \;\cong\;
chapters/theory/chiral_koszul_pairs.tex:981:\barBgeom(\operatorname{gr}_F \cA)
chapters/theory/chiral_koszul_pairs.tex:982:\;=\; \barBgeom(\operatorname{Sym}^{\mathrm{ch}}(V))
chapters/theory/chiral_koszul_pairs.tex:998:$E_0^{p,q} = \operatorname{gr}^p_F \barBgeom^{p+q}(\cA)$,
chapters/theory/chiral_koszul_pairs.tex:1011:E_1^{p,q} = H^{p+q}(\barBgeom^p(\operatorname{Sym}^{\mathrm{ch}}(V)))
 succeeded in 57ms:
chapters/theory/chiral_koszul_pairs.tex:49:$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
chapters/theory/chiral_koszul_pairs.tex:51:Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
chapters/theory/chiral_koszul_pairs.tex:143:connects $\barB_X(\cA)$ with the homotopy dual factorization
chapters/theory/chiral_koszul_pairs.tex:382:\longrightarrow \operatorname{gr}\barB_X(\cA)
chapters/theory/chiral_koszul_pairs.tex:565:$\barB_X(\cA)$ together with its canonical twisting morphism
chapters/theory/chiral_koszul_pairs.tex:566:$\tau_{\mathrm{can}} \colon \barB_X(\cA) \to \cA$
chapters/theory/chiral_koszul_pairs.tex:571:$f_\alpha \colon C \to \barB_X(\cA)$
chapters/theory/chiral_koszul_pairs.tex:583:that $\barB_X(\cA) = T^c_{\mathrm{chiral}}(s^{-1}\bar{\cA})$
chapters/theory/chiral_koszul_pairs.tex:3632:The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
chapters/theory/chiral_koszul_pairs.tex:3724:the bar complex $\barB_X(\cA)$ is the structure sheaf of the
chapters/theory/chiral_koszul_pairs.tex:3733:The unit $\eta_{\tau_i} \colon \cC_i \to \barB_X(\cA_i)$ and
chapters/theory/higher_genus_modular_koszul.tex:393:\cA \arrow[r, "\barB_X^{(g)}"]
chapters/theory/higher_genus_modular_koszul.tex:395:& \barB_X^{(g)}(\cA)
chapters/theory/higher_genus_modular_koszul.tex:400:\cA^! \arrow[r, "\barB_X^{(g)}"']
chapters/theory/higher_genus_modular_koszul.tex:401:& \barB_X^{(g)}(\cA^!)
chapters/theory/higher_genus_modular_koszul.tex:3376:morphism $\pi \colon \barB_X(\cA) \to \cA$ of genus-$0$ bar-cobar
chapters/theory/higher_genus_modular_koszul.tex:3404: twisted tensor product $\barB_X(\cA) \otimes_\pi \cA$ is acyclic
chapters/theory/higher_genus_modular_koszul.tex:10850: $\barB_X(\cA)$ twisted by~$\Theta$ is quasi-isomorphic to the
chapters/theory/higher_genus_modular_koszul.tex:27910: \barB_X(L),\;\;
chapters/theory/higher_genus_modular_koszul.tex:27921:\item $\barB_X(L) := \barB(\Fact_X(L))$ is the reduced bar
exec
/bin/zsh -lc "rg -n -F 'barB"'^{(g)}'"' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:10:The bar complex $\barB^{(g)}(\cA)$ acquires curvature
chapters/theory/higher_genus_modular_koszul.tex:243:$\barB^{(g)}(\cA)$ and on the genus-$g$ algebra $\cA^{(g)}$.
chapters/theory/higher_genus_modular_koszul.tex:246:\Omega^{(g)}(\sigma^* \barB^{(g)}(\cA))
chapters/theory/higher_genus_modular_koszul.tex:2647:cochain complex $V_{g,n} = \barB^{(g)}_n(\cA)$, to each boundary
chapters/theory/higher_genus_modular_koszul.tex:2763:makes $\barB^{(g)}(\cA)$ a CDG-coalgebra
chapters/theory/higher_genus_modular_koszul.tex:2769:$H^*(\barB^{(g)}(\cA), \Dg{g})$ varies over
chapters/theory/higher_genus_modular_koszul.tex:2815:\emph{B$\to$A}: GRR maps $[\barB^{(g)}(\cA)]\in K_0(\overline{\mathcal{M}}_g)$
chapters/theory/higher_genus_modular_koszul.tex:3520: \barB^{(g)}_X(\cA)
chapters/theory/higher_genus_modular_koszul.tex:9568:$\mathcal{V}_\cA=[R\pi_{g*}\barB^{(g)}(\cA)]\in K_0(\overline{\mathcal{M}}_g)$

thinking
**Aligning mathematical statements**

I need to check if the initial seam statements regarding kappa from Theorem D and `av(r(z))` match up. For instance, line 14484 indicates that Theorem D extracts the scalar κ = av(r(z)) from the spectral r-matrix. However, AGENTS mention that the averaging formula is `av(r(z))=kappa` for abelian groups and `av(r(z))+dim(g)/2=kappa` for non-abelian KM. This seems to indicate a potential discrepancy that needs clarification.
codex
I’ve found one hard falsehood already: the higher-genus file explicitly identifies the genus-$g$ bar object with the Koszul dual, which collapses the bar coalgebra / dual algebra distinction that the genus-zero chapter carefully keeps separate. I’m now checking for the same kind of object-conflation in the `\kappa` and averaging passages.
exec
/bin/zsh -lc "rg -n '\\\\kappa\\s*=|kappa\\s*=|av\\(r|operatorname\\{av\\}\\(r|r\\(z\\)' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~D extracts the scalar' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'degree-2 projection' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'genus-"'$0$ binary shadow'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'first characteristic number' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/chiral_koszul_pairs.tex:2552:= 2\kappa/\kappa = 2$, independent of~$c$;
chapters/theory/higher_genus_modular_koszul.tex:137: If $\kappa = 0$, it stops at depth~$3$
chapters/theory/higher_genus_modular_koszul.tex:1147: $\kappa = e \otimes f + f \otimes e
chapters/theory/higher_genus_modular_koszul.tex:2716: In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
chapters/theory/higher_genus_modular_koszul.tex:2777:trace gives one number $\kappa = 3(k{+}2)/4$; the sheaf
chapters/theory/higher_genus_modular_koszul.tex:2943:$\kappa(\cA) = \operatorname{av}(r(z))$, and the right-hand
chapters/theory/higher_genus_modular_koszul.tex:3003:$r$-matrix is level-stripped, $r(z) = 0 \cdot \Omega/z = 0$,
chapters/theory/higher_genus_modular_koszul.tex:3011:gravity is singular with $\kappa = 0$; at $k = 0$ gravity is
chapters/theory/higher_genus_modular_koszul.tex:3012:free with $\kappa = \dim(\fg)/2$. The holographic
chapters/theory/higher_genus_modular_koszul.tex:3117:\operatorname{av}(r(z))
chapters/theory/higher_genus_modular_koszul.tex:3127:$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
chapters/theory/higher_genus_modular_koszul.tex:3139:survives: $\kappa = \dim(\fg)/2$ is the residual holographic
chapters/theory/higher_genus_modular_koszul.tex:3142:and $\kappa = 0$: the critical level is where bulk gravity and
chapters/theory/higher_genus_modular_koszul.tex:4555:For Virasoro, $\rho(\mathfrak{sl}_2) = 1/2$, so $\kappa = c/2$.
chapters/theory/higher_genus_modular_koszul.tex:4557:$\kappa = 5c/6$. For Heisenberg, $\kappa = k$ directly
chapters/theory/higher_genus_modular_koszul.tex:4559:$\kappa = d$ by additivity
chapters/theory/higher_genus_modular_koszul.tex:4563:$c + c' = 26$ with $\kappa = c/2$ for Virasoro.
chapters/theory/higher_genus_modular_koszul.tex:4576:it retains higher-degree components with $\kappa = 0$); (vi)~complementarity lifts
chapters/theory/higher_genus_modular_koszul.tex:4615:The total is $\kappa = 5c/6$, consistent with the Fateev--Lukyanov
chapters/theory/higher_genus_modular_koszul.tex:4627:$\cW_N$ in general, $\kappa = c \cdot (H_N - 1)$ where
 succeeded in 59ms:
9797:Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
14484:Theorem~D extracts the scalar $\kappa = \operatorname{av}(r(z))$
 exited 1 in 50ms:

 succeeded in 51ms:
2486: the first characteristic number of~$\Theta_{\cA}$
2662:\index{kappa@$\kappa$!as first characteristic number|textbf}
7884:The scalar $\kappa(\cA)$ is the first characteristic number of
 exited 1 in 52ms:


thinking
**Inspecting line ranges**

I'm considering using regex to identify issues within lines 2943 and surrounding areas, such as lines 2928-2948 and 3110-3130. I should also take a look at lines 9790, 7880, and 14040, since they could contain problems too. It seems wise to open these specific lines for inspection to figure out what's really going on. There could be significant insights in these areas!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3108,3145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2928,2950p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3108	\end{remark}
  3109	
  3110	\begin{remark}[Sugawara shift as holographic anomaly]
  3111	\label{rem:kappa-holo-sugawara-shift}
  3112	\index{Sugawara construction!holographic shift}%
  3113	\index{holographic anomaly!Sugawara shift}%
  3114	For an affine Kac--Moody algebra at level~$k$, the bar-intrinsic
  3115	identity
  3116	\begin{equation}\label{eq:sugawara-shift-holographic}
  3117	\operatorname{av}(r(z))
  3118	\;+\;
  3119	\tfrac{1}{2}\dim(\fg)
  3120	\;=\;
  3121	\kappa(V_k(\fg))
  3122	\;=\;
  3123	\frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee}
  3124	\end{equation}
  3125	splits the holographic central charge into two pieces with
  3126	distinct bulk interpretations. The first summand
  3127	$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
 succeeded in 51ms:
  2928	+ c_{\mathrm{bulk}}(T_2)$ for decoupled bulk theories.
  2929	\item The duality clause
  2930	$\kappa(\cA) + \kappa(\cA^!) = K_\fg \cdot \varrho(\fg)$ is the
  2931	bulk Koszul conductor: it records the gravitational anomaly of
  2932	the bulk theory seen by the slab
  2933	$\cA \otimes \cA^!$-bimodule of Dimofte--Niu--Py.
  2934	\end{enumerate}
  2935	\end{conjecture}
  2936	
  2937	\begin{remark}[Evidence]
  2938	The identity~\eqref{eq:kappa-holographic-identity} is a
  2939	consequence of Theorem~\ref{thm:modular-characteristic} and
  2940	Corollary~\ref{cor:free-energy-ahat-genus}: the left-hand side
  2941	is the genus-$1$ obstruction coefficient extracted from the
  2942	bar complex at degree~$2$ by
  2943	$\kappa(\cA) = \operatorname{av}(r(z))$, and the right-hand
  2944	side is defined as the coefficient of~$\hbar^0$ in the
  2945	logarithm of the bulk one-loop partition function on the solid
  2946	torus, which by the $\hat A$-corollary reads
  2947	$F_1(\cA) = \kappa(\cA)/24$. Clauses (i)--(iii) then follow
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7868,7895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9788,9806p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14040,14105p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7868	universal MC package.
  7869	\end{lemma}
  7870	
  7871	\begin{proof}
  7872	Proposition~\ref{prop:geometric-modular-operadic-mc} places the
  7873	universal Maurer--Cartan problem on
  7874	$\Defcyc(\cA)\widehat{\otimes}\Gmod$ and furnishes the
  7875	modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
  7876	constructs the realized class~$\Theta_{\cA}$ with the stated trace,
  7877	clutching, and Verdier properties, while
  7878	Theorem~\ref{thm:mc2-bar-intrinsic} supplies its unconditional
  7879	bar-intrinsic existence. This is exactly MK6 and MK7.
  7880	\end{proof}
  7881	
  7882	\begin{remark}[Relation to the universal class]
  7883	\label{rem:kappa-theta-relation}
  7884	The scalar $\kappa(\cA)$ is the first characteristic number of
  7885	$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
  7886	and~\ref{thm:mc2-bar-intrinsic}); the
  7887	spectral discriminant $\Delta_{\cA}$
 succeeded in 51ms:
  9788	%================================================================
  9789	
  9790	\section{The modular convolution algebra and the master equation}
  9791	\label{sec:modular-bar-hamiltonian}
  9792	
  9793	A single algebraic object controls the modular theory: the
  9794	convolution dg~Lie algebra together with its shadow obstruction tower
  9795	(Definition~\ref{def:shadow-postnikov-tower}).
  9796	The five main theorems and the genus expansion descend from this tower;
  9797	Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
  9798	cubic and quartic shadows are proved at finite order.
  9799	The all-degree limit is a Maurer--Cartan element
  9800	$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
  9801	constructed from the genus-completed bar differential
  9802	(Theorem~\ref{thm:mc2-bar-intrinsic}).
  9803	
  9804	\subsection{The modular convolution dg~Lie algebra}
  9805	\label{subsec:modular-convolution-algebra}
  9806	\index{modular convolution dg Lie algebra|textbf}
 succeeded in 51ms:
 14040	with vertex weights from $K_{0,n}^\cA$, edge weights
 14041	from~$P_\cA$, and stratum weights from log-FM chains.
 14042	Conformal blocks on all Riemann surfaces are determined by
 14043	the OPE on the formal disk.
 14044	\end{theorem}
 14045	
 14046	\begin{proof}
 14047	(i)~Genus-zero projection of the primitive equation.
 14048	
 14049	(ii)~At genus~$1$, degree~$0$: the non-separating self-sewing
 14050	$\Delta_{\mathrm{ns}}(K_{0,2})$ gives
 14051	$\kappa = \operatorname{tr}_{\mathrm{cyc}}
 14052	(\Delta_{\mathrm{ns}}(K_{0,2}))$
 14053	by~\eqref{eq:kappa-from-binary-corolla}.
 14054	At genus~$1$, degree~$1$: stability forces $a, b \geq 2$ in any
 14055	separating bracket at genus~$0$, giving total degree~$\geq 2$;
 14056	the equation reduces to
 14057	$dK_{1,1} + \Delta_{\mathrm{ns}}(K_{0,3}) = 0$, solved by
 14058	$K_{1,1} = -P_\cA \circ \Delta_{\mathrm{ns}}(K_{0,3})$.
 14059	






thinking
**Clarifying findings**

I’m realizing that I can’t have conflicting answers here. There’s a robust finding that needs a precise solution. Since the user specifically asked about the relationship between Koszul pairs and Shadow towers, I think this definitely qualifies as relevant. I want to ensure I’m providing accurate information, so I’ll focus on figuring out the exact fix here. It feels really important to get this right for the user!
thinking
**Fixing theorem alignment**

I need to align the theorem with its item (i) by potentially replacing or removing certain text about the lattice. The exact fix requires some decision-making. I might use chiral_koszul_pairs/constitution and read the file contents with CLAUDE. The claims are grounded in this content. CLAUDE indicates that certain classes and the lattice may imply that I should delete a contradictory paragraph. I think I could suggest a replacement that's consistent with the theorem item (i) for clarity.
thinking
**Identifying inconsistencies**

I see a potential issue at line 2943 where it states kappa = av(r(z)) without qualifications. I should mark this as HIGH. There's a similar issue at line 14484, and I wonder if they might be duplicates concerning the same inconsistency. Since the user wants to identify every inconsistency, I could list both lines in my report. It makes sense to group them as they represent the same conceptual problem across the two lines.
thinking
**Analyzing findings for clarity**

I’m considering whether to list both findings without being redundant. One option is to mention the earliest instance at line 2943 and then note that the same formula appears again at line 14484. I think I can cite both in a format like: "[HIGH] higher_genus_modular_koszul.tex:2943 — PROBLEM: ... The same bare formula recurs at line 14484."  

There may be a potential issue with lines 2433-2439 discussing scalar modular characteristics. It seems to contrast with the scalar lane theorem and requires further checking with the definition and theorem discussed.
thinking
**Exploring definitions and gaps**

I’m considering searching around line 22600, but the user specifically asked about the definitions for seam and kappa. I need to inspect "Theorem D" that extracts the scalar level κ(cA) at line 9797; it doesn't mention certain matrices, which could be a gap. I'll also need to look at "Theoremref{thm:mc2-bar-intrinsic}" for existence conditions.  

Early sections using \(\Theta_A\) without qualifiers might mislead, and I could mark this as MEDIUM due to the missing seam. I should verify whether there's a mismatch in bar usage as I examine other relevant lines, especially around the genus tower.
thinking
**Fixing code insertion**

I need to insert a line in the code, and it should go after either line 23 or line 36. The line I need to add is: "In this chapter \barB^{(g)}_X(\cA) denotes the symmetric/coinvariant bar object \(B^\Sigma\)." It's important to get the placement right so everything flows correctly. I’ll double-check that I’m inserting the text in the right spot, making sure it aligns with the overall context of the chapter!
codex
A second hard issue surfaced: one proved-here theorem states the full all-genus scalar trace `\sum_g \kappa \lambda_g` with no uniform-weight qualifier, but the chapter’s own MC2 theorem only proves that formula on the scalar lane and gives genus~1 universally. I’m checking whether that qualifier drift appears anywhere else near the seam definitions.
exec
/bin/zsh -lc "rg -n 'thm:universal-generating-function|Theorem~\\\\ref\\{thm:universal-generating-function\\}|universal-generating-function|multi-generator-universality|genus-universality' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{genus-universality}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11680,11740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '20390,20540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{thm:genus-universality}' chapters/theory/higher_genus_modular_koszul.tex | head -n 80" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2436: (Theorem~\ref{thm:genus-universality}).
2439: (Theorem~\ref{thm:universal-generating-function}).
2543:(Theorem~\ref{thm:genus-universality}).
2686: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
2701: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2737:Theorem~\ref{thm:multi-generator-universality}.
2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2740:Theorem~\ref{thm:genus-universality}(ii).
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
2881:Theorem~\ref{thm:universal-generating-function}.
2962:Theorem~\ref{thm:multi-generator-universality}.
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3820:Theorem~\ref{thm:genus-universality}(ii)).
 succeeded in 52ms:
 11680	 $\operatorname{Ob}_r$.
 11681	\item Completeness and pronilpotence of $F^1 L_{\mathrm{mod}}$ give
 11682	 $E_\infty^{p,q}\cong \operatorname{gr}_F^p\, H^{p+q}(L_{\mathrm{mod}})$.
 11683	\end{enumerate}
 11684	This is the spectral sequence of the Maurer--Cartan extension tower.
 11685	It is distinct from the PBW spectral sequence (which uses the
 11686	conformal-weight filtration within each fixed genus to compute bar
 11687	cohomology): the genus spectral sequence controls the
 11688	\emph{lift across genera}, and its differentials are the obstruction
 11689	maps.
 11690	\end{construction}
 11691	
 11692	\begin{remark}[Curvature as $d_1$-obstruction]
 11693	\label{rem:vol1-curvature-as-d1}
 11694	\index{curvature!as spectral sequence obstruction}
 11695	The curvature $\kappa(\cA) \cdot \omega_g$ of the fiberwise
 11696	differential $\dfib$
 11697	(Convention~\ref{conv:higher-genus-differentials}(i))
 11698	is the $d_1$-differential of the genus spectral sequence:
 11699	the obstruction $\operatorname{Ob}_1$ of
 succeeded in 51ms:
2436: (Theorem~\ref{thm:genus-universality}).
2543:(Theorem~\ref{thm:genus-universality}).
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2740:Theorem~\ref{thm:genus-universality}(ii).
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3820:Theorem~\ref{thm:genus-universality}(ii)).
5386:(Theorem~\ref{thm:genus-universality},
7787:(Theorem~\ref{thm:genus-universality}).
7943:Theorem~\ref{thm:genus-universality} identifies the scalar trace
8091:Theorem~\ref{thm:genus-universality} identifies
8515:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
9650:By Theorem~\ref{thm:genus-universality},
11703:theorem (Theorem~\ref{thm:genus-universality}).
14532:Theorem~\ref{thm:genus-universality} identifies the scalar trace with
21900:(Theorem~\ref{thm:genus-universality} at $g=1$, the
 succeeded in 51ms:
 20390	$\rho^2(c)$ is a rational function of~$c$ with
 20391	$\frac{d(\rho^2)}{dc}
 20392	= \frac{-8(225c^2 + 2130c + 4796)}{c^3(5c{+}22)^2}$.
 20393	The quadratic $225c^2 + 2130c + 4796$ has both roots
 20394	negative ($\approx -3.69$ and $\approx -5.78$),
 20395	so it is positive for all $c > 0$, giving
 20396	$d(\rho^2)/dc < 0$ on $(0, \infty)$.
 20397	Hypothesis~(a) is verified in
 20398	Proposition~\ref{prop:propagator-universality}.
 20399	\end{proof}
 20400	
 20401	\begin{proposition}[Koszul conductor of \texorpdfstring{$\cW_N$}{WN}]
 20402	\label{prop:koszul-conductor-wn}
 20403	\ClaimStatusProvedHere
 20404	\index{Koszul conductor!$\cW_N$ formula|textbf}
 20405	\index{$\cW_N$!Koszul conductor}
 20406	For the principal $\cW$-algebra $\cW^k(\mathfrak{sl}_N)$,
 20407	the Koszul conductor
 20408	\textup{(}Definition~\textup{\ref{def:koszul-conductor})} is
 20409	\begin{equation}\label{eq:koszul-conductor-wn}

thinking
**Inspecting mathematical concepts**

I need to take a closer look at the universality theorem regarding the genus spectral sequence and its d1 curvature. There might be a universal aspect involved, but I want to confirm. I'll search for the theorem statement, specifically looking at around 7790 to verify the all-genus qualifier. This will help ensure that I'm interpreting it correctly. Let's get started on this investigation!
exec
/bin/zsh -lc "rg -n '"'^'"\\\\begin\\{theorem\\}\\[.*genus.*universality|\\\\label\\{thm:genus-universality\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7740,7815p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
9578:\begin{theorem}[Tautological line support from genus universality;
 succeeded in 51ms:
  7740	 tautological line
  7741	 $\mathbb{C} \cdot \tau_g \subset R^*(\overline{\mathcal{M}}_g)$.
  7742	 \textup{[}\emph{Resolved at genus~$1$ universally and at all
  7743	 genera on the proved uniform-weight lane:}
  7744	 Theorem~\textup{\ref{thm:tautological-line-support}}.\textup{]}
  7745	\end{enumerate}
  7746	Then there exists a universal Maurer--Cartan element
  7747	\[
  7748	 \Theta_{\cA}
  7749	 \;\in\;
  7750	 \mathrm{MC}\bigl(
  7751	 \Defcyc(\cA) \widehat{\otimes}
  7752	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})
  7753	 \bigr)
  7754	\]
  7755	whose genus-$1$ scalar trace is
  7756	$\kappa(\cA) \cdot \lambda_1$, and whose full scalar trace equals
  7757	$\sum_{g\ge1}\kappa(\cA)\lambda_g$ on the proved uniform-weight lane
  7758	(when MC2-3 is available at all genera).
  7759	The element $\Theta_{\cA}$ is compatible with clutching of stable
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7815,7865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21690,21840p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7815	 $\Defcyc(\cA) \widehat{\otimes} \Gmod$ converges and carries
  7816	 modular-operadic clutching morphisms, by
  7817	 Proposition~\textup{\ref{prop:geometric-modular-operadic-mc}}.
  7818	\item \emph{MC2-3}: The genus-$g$ obstruction class lies on the
  7819	 tautological line, by
  7820	 Theorem~\textup{\ref{thm:tautological-line-support}}.
  7821	\end{enumerate}
  7822	Consequently, on that lane the explicit-hypotheses completion route
  7823	reconstructs the universal Maurer--Cartan element
  7824	$\Theta_{\cA}$ of
  7825	Theorem~\textup{\ref{thm:universal-theta}} with the stated scalar
  7826	trace, clutching, and Verdier properties. For arbitrary
  7827	multi-weight families with simple Lie symmetry, parts
  7828	\textup{(i)}--\textup{(ii)} remain unconditional, while part
  7829	\textup{(iii)} is proved only at genus~$1$.
  7830	\end{theorem}
  7831	
  7832	\begin{proof}
  7833	Hypothesis~(i) is Theorem~\ref{thm:cyclic-linf-graph}, whose
  7834	two analytic inputs, the Stokes regularity on
 succeeded in 51ms:
 21690	The five-component differential $D = d_{\mathrm{int}} +
 21691	[\tau,-] + d_{\mathrm{sew}} + d_{\mathrm{pf}} + \hbar\Delta$
 21692	(eq.~\eqref{eq:D-five-components}) acts on
 21693	$\Theta_\cA = \sum_{g,n} \Theta_\cA^{(g,n)}$.
 21694	Applying $\Phi_\cA^{(g,n)}$~\eqref{eq:tautological-evaluation-map}
 21695	to the MC equation decomposes it by boundary type:
 21696	\begin{align*}
 21697	\text{codim-$0$ (interior):}&\quad
 21698	 d_{\mathrm{int}}(\Theta) + [\tau,\Theta]
 21699	 \;\leadsto\;
 21700	 \text{absorbed into transferred operations } \ell_k^{(g)},
 21701	\\
 21702	\text{codim-$1$ separating:}&\quad
 21703	 d_{\mathrm{sew}}(\Theta) + \tfrac{1}{2}[\Theta,\Theta]_{\mathrm{sep}}
 21704	 \;\leadsto\;
 21705	 \text{CohFT axiom (ii)},
 21706	\\
 21707	\text{codim-$1$ non-separating:}&\quad
 21708	 \hbar\Delta(\Theta)
 21709	 \;\leadsto\;
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:universal-generating-function\\}|universal generating function' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2860,2895p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
  2860	 \;=\;
  2861	 \prod_{n=1}^{\infty}
  2862	 \Bigl(1 - \frac{\hbar^2}{4n^2\pi^2}\Bigr)^{\!-1}$,
  2863	 the zeta-regularized determinant of the Laplacian
  2864	 on~$S^1$ with eigenvalues $\omega_n = 2n\pi$.
  2865	\item \emph{Low-genus values.}
  2866	 $\lambda_1^{\mathrm{FP}} = 1/24$, \;
  2867	 $\lambda_2^{\mathrm{FP}} = 7/5760$, \;
  2868	 $\lambda_3^{\mathrm{FP}} = 31/967680$.
  2869	 The universal genus-$2$-to-genus-$1$ ratio is
  2870	 $F_2/F_1 = 7/240$, independent of~$\cA$.
  2871	\item \emph{Perturbative structure.}
  2872	 The ratio
  2873	 $F_2/F_1^2 = 7/(10\kappa(\cA))$ is perturbative
  2874	 in $1/\kappa$: genus-$2$ relative to genus-$1$ squared
  2875	 is suppressed at large level.
  2876	\end{enumerate}
  2877	\end{corollary}
  2878	
  2879	\begin{proof}

thinking
**Searching for labels**

I need to locate a specific label that might not be in the snippet. I’ll search for `label{thm:universal-generating-function}` using a fixed string approach, possibly with the `F` option. I think using `rg -F` could help with that. It feels like a smart way to narrow down my search and find the exact label I need. Let's dive into this and see what I can uncover!
exec
/bin/zsh -lc "rg -n -F '\\label{thm:universal-generating-function}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Searching for a label**

I'm considering the possibility that the label might not exist, or perhaps it's referenced in a way that makes it hard to identify, like using macros or comments. I need to search for "universal-generating-function" comprehensively. I saw some references, but they didn't specifically mention the label. Maybe searching more broadly with a tool like grep, using something like `rg -n "universal-generating"`, could help me find it better. Let's explore that!
exec
/bin/zsh -lc "rg -n 'universal-generating' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2439: (Theorem~\ref{thm:universal-generating-function}).
2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
2881:Theorem~\ref{thm:universal-generating-function}.
31845:(Theorem~\ref{thm:universal-generating-function},
codex
A smaller but still real seam issue may be a stale label: the higher-genus file cites `thm:universal-generating-function`, and I haven’t found a local definition yet. I’m verifying whether that theorem lives elsewhere or whether the scalar-package definition is pointing at a dead reference.
exec
/bin/zsh -lc "rg -n -F 'thm:universal-generating-function' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Generating function.' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'universal generating function' chapters/theory/higher_genus_modular_koszul.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2439: (Theorem~\ref{thm:universal-generating-function}).
chapters/theory/higher_genus_modular_koszul.tex:2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
chapters/theory/higher_genus_modular_koszul.tex:2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
chapters/theory/higher_genus_modular_koszul.tex:2881:Theorem~\ref{thm:universal-generating-function}.
chapters/theory/higher_genus_modular_koszul.tex:31845:(Theorem~\ref{thm:universal-generating-function},
chapters/connections/concordance.tex:5922:expansion (Theorem~\ref{thm:universal-generating-function})
chapters/connections/concordance.tex:6144:Theorem~\ref{thm:universal-generating-function}
chapters/theory/introduction.tex:641: \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
chapters/theory/introduction.tex:1928:(Theorem~\ref{thm:universal-generating-function}) are consequences
chapters/theory/higher_genus_foundations.tex:3432:(Theorem~\ref{thm:universal-generating-function}).
chapters/theory/higher_genus_foundations.tex:4138:\textup{(Theorem~\ref{thm:universal-generating-function})}. Then the fiberwise
chapters/theory/higher_genus_foundations.tex:4181:Theorem~\ref{thm:universal-generating-function}.
chapters/theory/higher_genus_foundations.tex:6383:Theorem~\ref{thm:universal-generating-function}.
chapters/examples/lattice_foundations.tex:1711:(Theorem~\ref{thm:universal-generating-function}).
chapters/examples/w_algebras.tex:2668:(Theorem~\ref{thm:universal-generating-function}).
chapters/examples/genus_expansions.tex:1867:\item \emph{Generating function.} $\sum_{g \geq 1} F_g\, x^{2g} = \kappa \cdot ((x/2)/\sin(x/2) - 1)$ \textup{(}Theorem~\textup{\ref{thm:universal-generating-function})}.
chapters/examples/genus_expansions.tex:1873:Parts~(i) and~(iii) are proved in Proposition~\ref{prop:genus-expansion-convergence}. Part~(ii) is Theorem~\ref{thm:universal-generating-function}. The generating function $(x/2)/\sin(x/2) - 1$ is determined by its Taylor coefficients (the Bernoulli numbers), and $\kappa$ is the unique free parameter (Theorem~\ref{thm:genus-universality}).
chapters/examples/genus_expansions.tex:1913:\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
chapters/examples/genus_expansions.tex:2203:The universal generating function (Theorem~\ref{thm:universal-generating-function}) gives an explicit genus expansion for each row of the Master Table (Table~\ref{tab:master-invariants}). The Heisenberg (\S\ref{sec:frame-genus-tower}), $\widehat{\mathfrak{sl}}_2$, and Virasoro cases appear above. We complete the remaining entries. For uniform-weight
chapters/examples/genus_expansions.tex:2522:(Theorem~\ref{thm:universal-generating-function}), the genus-$g$
 succeeded in 51ms:
2687:\item \emph{Generating function.}
4396:\item \emph{Generating function.}
 succeeded in 51ms:
chapters/examples/heisenberg_eisenstein.tex:58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
chapters/examples/landscape_census.tex:6:algebra. The universal generating function $x/\sin x$ governs the
chapters/examples/genus_expansions.tex:162:\begin{remark}[Todd genus, \texorpdfstring{$\hat{A}$}{A-hat}-genus, and the universal generating function]\label{rem:a-hat-genus}
chapters/examples/genus_expansions.tex:775:This is linear in $t$ (hence in $k$) and is the product of the algebra-dependent factor $3t/4 = \kappa$ with the universal generating function $\hat{A}(x) - 1$. For any single-generator Koszul chiral algebra (and for multi-generator algebras subject to the Hodge-type factorization of Theorem~\ref{thm:modular-characteristic}(i)(b)), the analogous formula is
chapters/examples/genus_expansions.tex:1914:\index{genus expansion!universal generating function}
chapters/examples/genus_expansions.tex:2203:The universal generating function (Theorem~\ref{thm:universal-generating-function}) gives an explicit genus expansion for each row of the Master Table (Table~\ref{tab:master-invariants}). The Heisenberg (\S\ref{sec:frame-genus-tower}), $\widehat{\mathfrak{sl}}_2$, and Virasoro cases appear above. We complete the remaining entries. For uniform-weight
chapters/examples/genus_expansions.tex:2521:By the universal generating function
chapters/examples/genus_expansions.tex:3617:where $\phi_0(x) = (x/2)/\sin(x/2)$ is the universal generating function.
chapters/theory/higher_genus_foundations.tex:4186:normalizes the genus-$1$ term in the universal generating function.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16760,16835p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16760	\label{prop:sc-formality-by-class}
 16761	\index{Swiss-cheese!formality classification|textbf}
 16762	\index{shadow depth!Swiss-cheese formality}
 16763	Three distinct formality properties are governed by the
 16764	shadow depth class. Let $\cA$ be a modular Koszul chiral
 16765	algebra.
 16766	\begin{enumerate}[label=\textup{(\roman*)}]
 16767	\item \emph{$A_\infty$-formality of bar cohomology}
 16768	 \textup{(}operations on $H^*(\Barch(\cA))$\textup{)}:
 16769	 the transferred $A_\infty$ operations $m_k = 0$ for
 16770	 $k \geq 3$. This holds for \emph{all} Koszul algebras in
 16771	 \emph{all} four classes $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 16772	 \textup{(}Theorem~\textup{\ref{thm:koszul-equivalences-meta}},
 16773	 item~\textup{(iii))}.
 16774	\item \emph{Swiss-cheese operations $m_k^{\mathrm{SC}}$ on
 16775	 $\cA$ itself} \textup{(}encoded by the
 16776	 $\mathrm{SC}^{\mathrm{ch,top}}$ operad\textup{)}:
 16777	 \begin{center}
 16778	 \small
 16779	 \renewcommand{\arraystretch}{1.15}
exec
/bin/zsh -lc "rg -n -F '\\label{def:shadow-depth-classification}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '75,95p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16690,16795p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
16163:\label{def:shadow-depth-classification}
 succeeded in 51ms:
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
    90	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    91	Confusing the two misidentifies what the shadow tower measures.
    92	
    93	On a point, the bar complex
    94	$\barB(A) = T^c(s^{-1}\bar{A})$ is built from tensor powers of
 succeeded in 72ms:
 16690	filtration, it bijects the obstruction classes:
 16691	$o_r(\cA) = 0$ if and only if $o_r(\cA^!) = 0$.
 16692	Hence $r_{\max}(\cA) = r_{\max}(\cA^!)$.
 16693	\end{proof}
 16694	
 16695	\begin{remark}[Shadow depth refines GKW formality]
 16696	\label{rem:shadow-depth-gkw-refinement}
 16697	\index{GKW formality!shadow depth refinement}
 16698	\index{Gaiotto--Kulp--Wu|see{GKW formality}}
 16699	\index{shadow depth!GKW refinement}
 16700	The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
 16701	is a strict four-class refinement of the binary formal/non-formal
 16702	dichotomy of Gaiotto--Kulp--Wu~\cite{GKW2025}.
 16703	In their framework, a theory with topological direction
 16704	$d' \geq 2$ is formal (all higher operations vanish),
 16705	while $d' = 1$ theories are generically non-formal.
 16706	The shadow depth resolves the $d' = 1$ non-formal class
 16707	into three distinct strata:
 16708	\begin{enumerate}[label=\textup{(\roman*)}]
 16709	\item Class~$\mathbf{G}$ is formal \emph{even at}

thinking
**Inspecting classification logic**

I’m noticing a potential contradiction in line 16535 compared to the later remark about the four-class system. I think it might be helpful to inspect the `def:shadow-depth-classification` around line 16163. I want to understand the distinction between F_d and G/L/C/M classifications better. It’s clear that resolving this could clarify any inconsistencies arising from the initial remarks. I’m curious to see how this ties everything together!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16160,16220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16160	\end{proof}
 16161	
 16162	\begin{definition}[Shadow depth classification]
 16163	\label{def:shadow-depth-classification}
 16164	\ClaimStatusProvedHere
 16165	\index{shadow depth|textbf}
 16166	\index{shadow depth!classification}
 16167	\index{shadow obstruction tower!depth classification}
 16168	Let $\cA$ be a modular Koszul chiral algebra with
 16169	obstruction classes $o_r(\cA)$ from
 16170	Construction~\ref{constr:obstruction-recursion}.
 16171	Define the \emph{shadow depth}
 16172	$\kappa_d(\cA) := r_{\max}(\cA) =
 16173	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16174	(with the convention $\kappa_d = \infty$ if the tower
 16175	does not terminate).
 16176	The \emph{shadow depth class} of~$\cA$ is determined
 16177	by the vanishing pattern of obstruction classes:
 16178	\begin{center}
 16179	\small
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16220,16255p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16220	\S\ref{sec:higher-depths}): depth~$d$ requires a lattice
 16221	of rank~$r$ with $\dim S_{r/2}(\Gamma) \geq d-3$, and
 16222	each independent cusp form contributes one critical line
 16223	of the constrained Epstein zeta. Even unimodular lattices
 16224	of ranks $48, 72, 96, \dotsc$ achieve depths
 16225	$5, 6, 7,\dotsc$\,, with the depth growing as the
 16226	number of cusp forms in $M_{r/2}$ grows. The four classes
 16227	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ thus
 16228	form a \emph{coarse} classification; the fine classification
 16229	is the shadow depth $d \in \{2,3,4,5,\dotsc\} \cup \{\infty\}$,
 16230	and every finite value is realized.
 16231	
 16232	The classification presupposes chiral Koszulness. Beyond the Koszul
 16233	boundary lies a fifth regime: class~$\mathbf{W}$ (wild), in which
 16234	the bar spectral sequence does not collapse at any finite page and
 16235	the shadow depth is undefined
 16236	(Remark~\ref{rem:wild-quiver-boundary}).
 16237	\end{definition}
 16238	
 16239	\begin{remark}[The Koszul boundary and class~$\mathbf{W}$]

thinking
**Searching for bar dual conflations**

I need to explore more about these explicit bar dual conflations. I might use a search command like `rg -n` with key phrases such as "is the correct Koszul dual" or "bar.*dual". It seems like a straightforward approach, but I'm also contemplating if there are better ways to effectively gather information on this topic. Any helpful insights or resources would be great, and I'm curious about any nuances I might be overlooking!
codex
The shadow-depth surface is worse than a vague gap. The higher-genus file contains mutually incompatible classification claims: one place says only four finite-depth classes exist in the standard lane, another says lattices realize every finite depth, and a later theorem puts lattices back in class `G`. I’m tightening that into exact line-cited findings and checking for any nearby duplicate object-conflations.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '154,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'correct Koszul dual|Koszul dual coalgebra|bar coalgebra|is the Koszul dual|bar.*dual|dual coalgebra|A\\"'^!'"' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16162,16238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '534,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '324,353p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   154	
   155	\section{From the Heisenberg example to general twisting data}
   156	\label{sec:chiral-twisting-data}
   157	
   158	The bar complex of $\mathcal{H}_k$ (Chapter~\ref{ch:heisenberg-frame},
   159	Theorem~\ref{thm:frame-heisenberg-koszul-dual})
   160	produces the coalgebra $\bar{B}(\mathcal{H}_k)
   161	\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)$,
   162	whose cohomology gives the Koszul dual algebra
   163	$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$.
   164	The bar-cobar counit
   165	$\Omega_X(\bar{B}_X(\mathcal{H}_k)) \xrightarrow{\;\sim\;} \mathcal{H}_k$
   166	is a quasi-isomorphism (recovering the original algebra, not its dual). Two structural features make this work:
   167	
   168	\begin{enumerate}
   169	\item The twisted tensor product
   170	 $K_\tau^L(\mathcal{H}_k, \mathrm{coLie}^{\mathrm{ch}}(V^*))$
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:52:homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
chapters/theory/chiral_koszul_pairs.tex:53:$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
chapters/theory/chiral_koszul_pairs.tex:96:$\tau \colon \barB(A) \to A^!$ is a degree-$+1$ element in the
chapters/theory/chiral_koszul_pairs.tex:112:Lagrangian complementarity between $\cA$ and $\cA^!$
chapters/theory/chiral_koszul_pairs.tex:143:connects $\barB_X(\cA)$ with the homotopy dual factorization
chapters/theory/chiral_koszul_pairs.tex:144:algebra~$\cA^!_\infty$ completes the
chapters/theory/chiral_koszul_pairs.tex:193:its bar coalgebra. The bridge between them is a \emph{twisting morphism},
chapters/theory/chiral_koszul_pairs.tex:508:$f_\tau\colon \cC \to \bar{B}_X(\cA)$ defined dually.
chapters/theory/chiral_koszul_pairs.tex:551:\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
chapters/theory/chiral_koszul_pairs.tex:553: dual pair, Verdier duality sends the bar coalgebra of one side
chapters/theory/chiral_koszul_pairs.tex:557:$\mathrm{A}_1$ extracts the dual coalgebra;
chapters/theory/chiral_koszul_pairs.tex:651:invoking bar-cobar duality itself.
chapters/theory/chiral_koszul_pairs.tex:694:the bar coalgebra
chapters/theory/chiral_koszul_pairs.tex:697:whose linear dual is the Koszul dual algebra
chapters/theory/chiral_koszul_pairs.tex:925:\label{cor:bar-cohomology-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:926:\index{bar complex!Koszul dual computation}
chapters/theory/chiral_koszul_pairs.tex:933:\dim H^n(\barBgeom(\cA)) = \dim (\cA^!)_n
chapters/theory/chiral_koszul_pairs.tex:934:\qquad\textup{(identifying $(\cA^!)_n = H^n(\barBgeom(\cA))^\vee$)}.
chapters/theory/chiral_koszul_pairs.tex:947: the $n$-th graded piece of the Virasoro Koszul dual coalgebra.
chapters/theory/chiral_koszul_pairs.tex:1043:= (\cA^!)_n.
 succeeded in 54ms:
   534	\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
   535	 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
   536	Let $X$ be a smooth projective curve over $\mathbb{C}$.
   537	A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
   538	algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
   539	the following data and satisfying the following axioms.
   540	
   541	\smallskip\noindent\textbf{Data.}
   542	\begin{enumerate}[label=\textup{(D\arabic*)}]
   543	\item\label{D:bar}
   544	A reduced bar construction
   545	$\bar{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
   546	(Definition~\ref{def:bar-differential-complete},
   547	Theorem~\ref{thm:bar-nilpotency-complete}).
   548	
   549	\item\label{D:dual}
   550	A candidate Koszul dual chiral algebra $\cA^!$ on~$X$ with
   551	universal twisting morphism
   552	$\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
   553	$\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 succeeded in 54ms:
 16162	\begin{definition}[Shadow depth classification]
 16163	\label{def:shadow-depth-classification}
 16164	\ClaimStatusProvedHere
 16165	\index{shadow depth|textbf}
 16166	\index{shadow depth!classification}
 16167	\index{shadow obstruction tower!depth classification}
 16168	Let $\cA$ be a modular Koszul chiral algebra with
 16169	obstruction classes $o_r(\cA)$ from
 16170	Construction~\ref{constr:obstruction-recursion}.
 16171	Define the \emph{shadow depth}
 16172	$\kappa_d(\cA) := r_{\max}(\cA) =
 16173	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16174	(with the convention $\kappa_d = \infty$ if the tower
 16175	does not terminate).
 16176	The \emph{shadow depth class} of~$\cA$ is determined
 16177	by the vanishing pattern of obstruction classes:
 16178	\begin{center}
 16179	\small
 16180	\renewcommand{\arraystretch}{1.15}
 16181	\begin{tabular}{clll}
 succeeded in 51ms:
   324	\begin{theorem}[Genus-graded Koszul duality; \ClaimStatusProvedHere]
   325	\label{thm:genus-graded-koszul}\label{thm:genus-graded-koszul-duality}\label{thm:extended-koszul}
   326	\index{genus-graded Koszul duality}
   327	Let $(\mathcal{A}, \mathcal{A}^!)$ be a Koszul chiral pair at genus~0
   328	with central curvature at all genera (Remark~\ref{rem:voa-central-curvature}).
   329	Assume:
   330	\begin{enumerate}
   331	\item \emph{Modular Koszulity:} At each genus $g \geq 1$, the bar complex
   332	$\bar{B}^{(g)}(\mathcal{A})$ satisfies diagonal Ext vanishing:
   333	$\mathrm{Ext}^{i,j}_{\mathcal{A}^{(g)}}(\mathbb{k}, \mathbb{k}) = 0$ for $i \neq j$.
   334	\item \emph{Convergence:} The genus-graded bar complex
   335	$\bar{B}^{\mathrm{full}}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$
   336	converges in the $\hbar$-adic topology.
   337	\end{enumerate}
   338	Then $\mathcal{A}^! := \bigoplus_{g \geq 0} (\mathcal{A}^!)^{(g)}$
   339	is genus-graded Koszul, $(\mathcal{A}^!)^! \cong \mathcal{A}$ in
   340	$\mathbb{C}[\![\hbar]\!]$-modules, and the tower above is a compatible
   341	system of Koszul dualities.
   342	\end{theorem}
   343	


thinking
**Identifying inconsistencies in definitions**

I’m seeing potential issues with the theorem about the genus-graded Koszul. It uses a direct sum, but the later definition regarding the genus tower uses a product instead. That's a clear inconsistency! The direct sum appears at line 335, while the product is mentioned at line 567. In hbar-adic completion, we expect a product, so I need to fix that by replacing the direct sum with a product. Adjusting the statements for clarity might be necessary too.
thinking
**Clarifying findings in the theorem**

I'm considering that the theorem encompasses two independent errors: the direct sum versus product issue and the confusion between bar and dual. It might be best to consolidate these findings into one critical item, clearly stating how both aspects contradict the later definition. The exact fix will involve rewriting the statement and proof. I should inspect line 335 as well and maybe check for similar direct sum/product inconsistencies elsewhere by searching `\bigoplus_{g \geq 0} \bar{B}^{(g)}`.
codex
The same early theorem has a second structural fault: it uses a direct sum genus completion, while the later definitions in the same file switch to the $\hbar$-adic product. I’m checking whether that direct-sum/product drift occurs elsewhere or is isolated to this theorem.
exec
/bin/zsh -lc "rg -n -F '\\bigoplus_{g \\geq 0} (\\mathcal{A}"'^!)''^{(g)}'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\prod_{g \\geq 0} \\hbar"'^g '"\\bar{B}"'^{(g)}'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\bigoplus_\\{g \\\\geq 0\\} \\\\bar\\{B\\}\\"'^'"\\{\\(g\\)\\}|\\\\bigoplus_\\{g \\\\geq 0\\} \\\\bar\\{B\\}\\"'^'"\\{\\(g\\)\\}|bar\\"'^'"\\{\\\\mathrm\\{full\\}\\}\\\\(\\\\mathcal\\{A\\}\\\\) = \\\\bigoplus' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\prod_{g \\geq 0}\\hbar"'^g'"\\,\\bar{B}"'^{(g)}_X('"\\cA)' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
335:$\bar{B}^{\mathrm{full}}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$
 succeeded in 52ms:
338:Then $\mathcal{A}^! := \bigoplus_{g \geq 0} (\mathcal{A}^!)^{(g)}$
 succeeded in 52ms:
568:\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
 succeeded in 52ms:
2562: \prod_{g \geq 0}\hbar^g\,\bar{B}^{(g)}_X(\cA)






thinking
**Evaluating algebra definitions**

I see a potential issue in line 338, where “dual” is defined as a direct sum, but perhaps it should be a product instead. In the context of genus-graded algebra, a direct sum might work, but consistency with the \(\mathbb{C}[[\hbar]]\)-module suggests a product or completed sum is needed. I’m also considering checking lines related to \(\Theta\) and other occurrences of `av(r(z))`, as well as certain lines discussing algebraic objects controlling modular theory.
thinking
**Analyzing potential issues**

I’m considering whether the existing MEDIUM gap at line 48 makes a change unnecessary. There might be a concern with line 324, where the theorem discusses \(A^!\) as genus-graded, and line 327 states it’s a Koszul chiral pair at genus 0. I’ll need to check line 600 to see if it references the genus-zero bar spectral sequence collapse. Also, I’m wondering about potential contradictions around remark 16695 and the classification definitions, and which file needs adjusting. I’ll need to decide what exactly needs fixing here.
thinking
**Adjusting classification definitions**

I'm thinking about the consistency of the surface in this four-class model. To fix things precisely, I’ll delete the higher-rank lattice paragraph from the definitions and theorems. If we're addressing higher-depth arithmetic shadows, it should go to a separate section marked as non-standard. The current text mostly assumes four classes, so it's crucial to clarify that.

For an exact fix, I could replace certain lines and delete others while possibly adjusting label references to maintain clarity. Would that cover what the user needs for the seam between files?
thinking
**Clarifying arithmetic shadows**

I need to clarify that if we're keeping the claim about arithmetic shadows, it must be relocated to that chapter and explicitly marked as excluded from the theorematic surface here. I wonder if I need to provide exact replacement text as well. 

There's also line 16521-16527 which discusses shadow depth and might be okay. I should check line 16767-16770 where `H^*(\Barch(\cA))` and `m_k=0 for all Koszul algebras` are mentioned since it might relate to theorems. 

Additionally, I worry about line 87 in the first file regarding "SC bar complex," which might conflict with its definition.
thinking
**Focusing on relevant issues**

It seems like there's a separate, possibly significant issue here, but the user didn't ask about that seam. I wonder if it's related to Koszul pairs and shadow towers, but maybe it's not. I really need to avoid scope creep. 

The reviewer's request specifically mentioned auditing the mission seam between two files with checks (a), (b), and (c). So, I should focus on keeping my findings directly relevant to that.
thinking
**Clarifying kappa notation**

I’m noticing a potential confusion in the notation for `\kappa_d(\cA)` being defined as `r_{max}(\cA)`, which seems inconsistent with its use to denote the kappa modular characteristic. There’s a risk that defining `\kappa_d` for shadow depth could lead to ambiguity with the modular characteristic. To resolve this, I should suggest renaming `\kappa_d` to `d_{\mathrm{sh}}(\cA)` or `r_{\max}(\cA)` throughout the definitions. I’ll also need to search for other instances of it using `rg`.
codex
I’m checking one last kappa-related collision before I write findings: the higher-genus file may also overload `\kappa` itself by introducing `\kappa_d` for shadow depth, which would contaminate the scalar `\kappa` seam the user asked me to audit.
exec
/bin/zsh -lc "rg -n '\\\\kappa_d|kappa_d' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~D extracts the scalar level~\\kappa(\\cA)' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Each row of the table above is the \\Sigma_n-coinvariant' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Its successive degree projections extract the invariants of~\\cA' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:16172:$\kappa_d(\cA) := r_{\max}(\cA) =
chapters/theory/higher_genus_modular_koszul.tex:16174:(with the convention $\kappa_d = \infty$ if the tower
chapters/theory/higher_genus_modular_koszul.tex:16183:\emph{Class} & \emph{Name} & $\kappa_d$ &
chapters/theory/higher_genus_modular_koszul.tex:28671: $\kappa_d(\cA) = \kappa_d(\cA')$.
 exited 1 in 50ms:

 exited 1 in 51ms:

 succeeded in 50ms:
3556:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
 exited 1 in 51ms:


thinking
**Investigating search issues**

I think the fixed string search might be failing due to escape sequences. We know about line 14476, but maybe searching for the plain substring "coinvariant image" isn't necessary after all. I might need to inspect line 28671 if `\kappa_d` is used later. It's probably not a major issue, but I should open up around line 28660 to see what's happening there. Let's check it out!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '28662,28678p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 28662	\end{proof}
 28663	
 28664	\begin{theorem}[Shadow depth is a homotopy invariant]
 28665	\label{thm:shadow-depth-invariant}
 28666	\ClaimStatusProvedHere
 28667	\index{shadow depth!invariance}
 28668	\begin{enumerate}[label=\textup{(\roman*)}]
 28669	\item If $f\colon \cA \xrightarrow{\sim} \cA'$ is a
 28670	 quasi-isomorphism of cyclic chiral algebras, then
 28671	 $\kappa_d(\cA) = \kappa_d(\cA')$.
 28672	\item The shadow depth class
 28673	 $\mathbf{G}, \mathbf{L}, \mathbf{C}, \mathbf{M}$
 28674	 is preserved under continuous deformation of
 28675	 parameters $(c, k)$ except at finitely many critical
 28676	 values where class jumps may occur.
 28677	\end{enumerate}
 28678	\end{theorem}
exec
/bin/zsh -lc "rg -n -F 'whose scalar trace is' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\sum_\\{g\\\\ge1\\}\\\\kappa|full scalar trace equals|scalar trace is|scalar trace with|kappa\\\\(\\\\cA\\\\)\\\\cdot\\\\lambda_g|obs_g\\\\(\\\\cA\\\\) = \\\\kappa' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'obs}_g = \\kappa(\\cA)\\cdot\\lambda_g' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2541:On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
 succeeded in 52ms:
2593: whose scalar trace is
 succeeded in 51ms:
2593: whose scalar trace is
3318:\item the genus-$1$ component of its scalar trace is
3320: the full scalar trace is
7755:whose genus-$1$ scalar trace is
7756:$\kappa(\cA) \cdot \lambda_1$, and whose full scalar trace equals
7757:$\sum_{g\ge1}\kappa(\cA)\lambda_g$ on the proved uniform-weight lane
9763:scalar trace is genus-$1$ universal and all-genera on the proved
14532:Theorem~\ref{thm:genus-universality} identifies the scalar trace with
31322:planted-forest graph sum. The scalar trace is
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3308,3324p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3308	universal Maurer--Cartan class
  3309	\[
  3310	\Theta_{\cA} \in
  3311	\operatorname{MC}\!\bigl(
  3312	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3313	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3314	\bigr)
  3315	\]
  3316	such that:
  3317	\begin{enumerate}[label=\textup{(\roman*)}]
  3318	\item the genus-$1$ component of its scalar trace is
  3319	 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
  3320	 the full scalar trace is
  3321	 $\operatorname{tr}(\Theta_{\cA})
  3322	 = \sum_{g \geq 1} \kappa(\cA) \lambda_g$;
  3323	\item it is compatible with clutching morphisms of stable curves;
  3324	\item under Verdier/Koszul duality, $\Theta_{\cA}$ is sent to

thinking
**Evaluating theorem qualifiers**

I'm considering whether this is related to a conditional theorem. It seems there's a missing qualifier of 2593, which might be fine. I need to check around 9763 to see if remark states are correct. It sounds promising, but I should stay open-minded about the results as I dig deeper. Let's explore what I find to make sure everything aligns properly!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9756,9768p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  9756	Theorem~D$_\Delta$
  9757	(Theorem~\ref{thm:spectral-characteristic}): the spectral
  9758	discriminant is a separately proved non-scalar invariant.
  9759	
  9760	The universal Maurer--Cartan class $\Theta_{\cA}$
  9761	(Theorem~\ref{thm:universal-theta}) is established
  9762	intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic}. Its
  9763	scalar trace is genus-$1$ universal and all-genera on the proved
  9764	uniform-weight lane; the non-scalar shadow obstruction tower
  9765	(cubic, quartic, and higher-degree obstructions)
  9766	is developed in
  9767	Appendix~\ref{app:nonlinear-modular-shadows} at each finite
  9768	order. All-degree convergence follows from the


thinking
**Analyzing findings on kappa and lattice contradictions**

I’m considering splitting the findings into two parts: one for kappa_d overload and another for the finite-depth lattice contradiction. The user asked about the definition of kappa, so the kappa_d overload may be relevant but is likely of lower importance. The finite-depth lattice contradiction seems more severe. I’m thinking of including a medium finding related to a specific chapter gap involving shadow towers that the user pointed out. It’s a gap worth mentioning!
thinking
**Assessing findings on kappa and seams**

I’m contemplating labeling a finding as medium regarding the kappa overload notation in the file higher_genus_modular_koszul.tex. If I include a classification finding, I can suggest renaming \kappa_d to d_{\mathrm{sh}}, ensuring consistency across specific lines. This could push the total to five findings. I should also check if chiral_koszul_pairs.tex has any seam issues, but so far, everything seems fine. I'll examine whether there's any relevant misuse and check specific lines for their claims.
codex
I have the surviving findings. I’m doing one final re-read around each line so the output stays false-positive free, then I’ll format only the issues that are directly evidenced by the text.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '40,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2550,2622p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3554,3564p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14376,14490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2938,2946p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    40	\[
    41	 d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
    42	\]
    43	unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
    44	Existence of the MC element is not a theorem to be proved; it is a
    45	tautology of the bar construction. The question is what structure
    46	$\Theta_\cA$ carries.
    47	
    48	Its successive degree projections extract the invariants of~$\cA$:
    49	the modular characteristic $\kappa(\cA)$ at degree~$2$,
    50	the cubic shadow~$\mathfrak{C}$ at degree~$3$,
    51	the quartic resonance class~$\mathfrak{Q}$ at degree~$4$.
    52	The obstruction classes
    53	$o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
    54	do not obstruct existence of~$\Theta_\cA$; they obstruct its
    55	\emph{truncation} at finite degree.
    56	
    57	%% CARRIER ALGEBRA: strict model of the L-infinity deformation complex.
    58	
    59	The algebraic carrier of this structure is the modular convolution
 succeeded in 52ms:
  2550	
  2551	\begin{theorem}[Genus internalization of modular Koszul duality; \ClaimStatusProvedHere]
  2552	\label{thm:genus-internalization}
  2553	\index{modular Koszul duality!genus internalization|textbf}
  2554	Let $\cA$ be a modular Koszul chiral algebra on a smooth projective
  2555	curve~$X$. Then genus is internal to the bar-cobar transform in the
  2556	following precise sense.
  2557	\begin{enumerate}[label=\textup{(\roman*)}]
  2558	\item The completed bar object
  2559	 \[
  2560	 \bar{B}^{\mathrm{full}}_X(\cA)
  2561	 \;:=\;
  2562	 \prod_{g \geq 0}\hbar^g\,\bar{B}^{(g)}_X(\cA)
  2563	 \]
  2564	 is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
  2565	 $\bar{B}_X(\cA)$: the fiberwise genus-$g$ differential satisfies
  2566	 $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\operatorname{id}$ and the
  2567	 strict total differential $\Dtot$ satisfies $\Dtot^{\,2} = 0$.
  2568	\item Verdier duality intertwines the full genus tower with the dual
  2569	 tower,
 succeeded in 51ms:
  3554	\begin{remark}[Scope of MC2 in this chapter]
  3555	\index{MC2!coinvariant scope}
  3556	Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
  3557	statement: its target dg~Lie algebra is
  3558	$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
  3559	The ordered lift
  3560	$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
  3561	\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
  3562	Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
  3563	$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
  3564	\end{remark}
 succeeded in 51ms:
  2938	The identity~\eqref{eq:kappa-holographic-identity} is a
  2939	consequence of Theorem~\ref{thm:modular-characteristic} and
  2940	Corollary~\ref{cor:free-energy-ahat-genus}: the left-hand side
  2941	is the genus-$1$ obstruction coefficient extracted from the
  2942	bar complex at degree~$2$ by
  2943	$\kappa(\cA) = \operatorname{av}(r(z))$, and the right-hand
  2944	side is defined as the coefficient of~$\hbar^0$ in the
  2945	logarithm of the bulk one-loop partition function on the solid
  2946	torus, which by the $\hat A$-corollary reads
 succeeded in 51ms:
 14376	\Theta_\cA^{\leq 4},\, \ldots$
 14377	in the modular convolution algebra
 14378	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is the
 14379	organizing structure from which all five main theorems, the
 14380	nonlinear shadow calculus, and the genus expansion descend.
 14381	Each finite truncation $\Theta_\cA^{\leq r}$ is \emph{proved}
 14382	constructively; the all-degree limit
 14383	$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ exists by the
 14384	bar-intrinsic construction
 14385	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
 14386	
 14387	The correct logical order is:
 14388	\begin{enumerate}[label=\textup{(\arabic*)}]
 14389	\item Define $\mathfrak{g}_{\cA}^{\mathrm{mod}}$ from the modular
 14390	 operad and the chiral algebra.
 14391	 More precisely, $\Definfmod(\cA)$ is the homotopy-invariant
 14392	 home \textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution})};
 14393	 the dg~Lie algebra $\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is its
 14394	 strict model
 14395	 \textup{(}Corollary~\textup{\ref{cor:strictification-comparison})}.









thinking
**Determining exact fix**

The user is asking for a specific fix, not just to delete something, which is important. I think we should provide a replacement sentence too. It requires inserting a new sentence after line 47 about the shadow tower and related theories. The severity of this issue might range from medium to high, especially since it's crucial to address the seam. Additionally, we should consider issues like the renaming of `\kappa_d` on line 16172 and other potential problems in the document.
thinking
**Reviewing potential issues**

I see potential issues in lines 14442 to 14445, where it mentions, "The five main theorems are projections of the scalar level \(\Theta_A^{\le2} = \kappa(A)\) of the shadow obstruction tower." I need to ensure that this statement is clear and correctly aligns with the rest of the document. Is there any ambiguity? I should reconsider how this connects with previous explanations if necessary. This could lead to misinterpretations, so I definitely want to clarify any points that might be confusing.
thinking
**Evaluating theorem statements**

I think the intended statement is about the five main theorems being projections of the shadow obstruction tower. The theorem D specifically mentions the scalar-level projection, but I see that A, B, C, and H aren't scalar based on the immediate table. I need to fix lines 14442-14445 to clarify that these theorems stem from different components, which is a seam issue that seems quite significant since it misstates the logical dependence of the theorems.
thinking
**Correcting theorem statements**

I see that line 14442 improperly simplifies all theorems to a scalar level, which is definitely an issue. I need to replace it with a more accurate sentence that reflects the real relationships of the theorems involved. This correction feels significant and is strongly supported by the evidence I've gathered. It's probably more relevant than addressing the earlier gap in the text. Getting this right can really clarify the context for readers!
thinking
**Analyzing theorems and classifications**

I’m thinking that the tower might start at the scalar level, but it seems like not all theorems come from that level. The grammar in "The five main theorems are projections of the scalar level..." sounds off because the table rows contradict this idea. I wonder if I should mention specific classifications like the chiral file at line 75, the higher_genus definition at 16215, and theorems 16482/16529 along with remark 16700 for clarity.
thinking
**Evaluating code details**

I want to note that I need to replace the statement lines between 338 and 341 accordingly. That's good! Also, for finding 2 on line 2593, there seems to be an issue with the all-genus scalar trace overclaim. It might be critical or high, since the theorem proven there misstates the scope. I should make sure to address that accurately in my review.
thinking
**Updating mathematical notation**

I need to make a couple of corrections in my text. First, at line 14484, I'm replacing a sentence to clarify how Theorem D extracts the scalar \(\kappa\). It should specify that for affine KM, it's \(\operatorname{av}(r(z))+\tfrac12\dim(\fg)\), and for the abelian case, just \(\operatorname{av}(r(z))\). Then at 2943, I’ll change \(\kappa(\cA)=\operatorname{av}(r(z))\) to reflect that. Lastly, I noticed there's an issue with the beginning of the chapter missing proper qualifications on some invariants—this could be a medium-level problem to address.
thinking
**Evaluating mathematical terms**

I’m wondering if there might be a false positive with finding line 14442. I need to ensure the phrase "projections of the scalar level" doesn't imply that "the five main theorems are projections." The table contradicts that idea, so I see the inconsistency. The user asked about inconsistencies, and I realize I may need to mention that line 14484's formula fix should use `operatorname{av}(r(z)) + \dim(\fg)/2 = \kappa` in trace-form convention. It's important to clarify that!
thinking
**Structuring output properly**

I’m considering how the user might expect the surface checks to be formatted. They might expect something like `Checked: 2`. I think I could say `Checked: 2 files | Findings: 6 | Verdict: FAIL`, but I need to stick to the structured output format, which is `Checked: N | Findings: N | Verdict: PASS/FAIL`. So, it seems I should exactly follow that. I’m realizing I don’t need to mention any commentary or commands. Let's draft that carefully!
codex
- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:349` — PROBLEM: the proof of `thm:genus-graded-koszul` sets `(\mathcal A^!)^{(g)} := \bar B^{(g)}(\mathcal A)`, so the bar coalgebra is identified with the Koszul dual algebra. That contradicts the seam source in `chapters/theory/chiral_koszul_pairs.tex:160-166`, which distinguishes bar coalgebra, bar cohomology, and dual algebra, and it also contradicts the later dg definition in `higher_genus_modular_koszul.tex:550-555`, which says `\bar B_X(\cA)` is the Koszul dual coalgebra and `\cA^!` appears only after dualization. The same theorem also uses a direct-sum “completion” at `:335`, while the file’s own completed bar object is the `\hbar`-adic product at `:568` and `:2562`. FIX: rewrite the theorem/proof so the completed object is `\bar B_X^{\mathrm{full}}(\cA):=\prod_{g\ge0}\hbar^g\bar B_X^{(g)}(\cA)`, the genus-`g` dual coalgebra is `(\mathcal A^i)^{(g)}:=H^*(\bar B_X^{(g)}(\mathcal A))`, and the dual algebra is obtained only after dualization, e.g. `(\mathcal A^!)^{(g)}:=((\mathcal A^i)^{(g)})^\vee`.

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2593` — PROBLEM: `thm:genus-internalization` states the full scalar trace `\operatorname{tr}(\Theta_{\cA})=\sum_{g\ge1}\kappa(\cA)\lambda_g` unconditionally for every simple-Lie-symmetry algebra. The same file later restricts that all-genera formula to the proved uniform-weight lane in `:3530-3534` and again in `:7755-7758`; only the genus-1 scalar trace is universal. FIX: replace lines `2593-2600` with: `whose genus-1 scalar trace is \kappa(\cA)\lambda_1; on the proved uniform-weight lane this refines to \operatorname{tr}(\Theta_{\cA})=\sum_{g\ge1}\kappa(\cA)\lambda_g. Its clutching compatibility recovers ...` and change the proof at `:2616-2620` to cite that same qualifier instead of calling the full formula unconditional.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:16215` — PROBLEM: the shadow-depth definition first presents exactly four classes `\mathbf G/\mathbf L/\mathbf C/\mathbf M`, then immediately says lattices realize every finite depth `d\ge5` at `:16217-16230`. Later the theorem puts lattice VOAs back in class `\mathbf G` at `:16482-16483`, and `chapters/theory/chiral_koszul_pairs.tex:75-90` treats the seam as exactly four classes with depths `{2,3,4,\infty}`. Those claims cannot all be true on one seam surface. FIX: keep the four-class theorematic surface and delete the fine-depth lattice paragraph at `16217-16230` and the parallel lattice-depth paragraph at `16529-16540`; replace `16215-16216` by `These four classes are exhaustive and mutually exclusive on the standard-family theorematic surface used in this chapter.` Also rename the depth symbol `\kappa_d` at `:16172`, `:16174`, `:16183`, and `:28671` to `d_{\mathrm{sh}}` so scalar `\kappa` is no longer overloaded.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14442` — PROBLEM: the remark says “The five main theorems are projections of the scalar level `\Theta_{\cA}^{\le2}=\kappa(\cA)`,” but the table immediately underneath assigns Theorem A to the genus-0 twisting component, B to `\mathrm{FT}^2\simeq\mathrm{id}`, C to cross-polarization, and H to a degree-preserving sub-MC. Only Theorem D is scalar-level. FIX: replace lines `14442-14445` with `The five main theorems are projections of the shadow obstruction tower. Theorem D is the scalar-level projection \Theta_{\cA}^{\le2}; Theorems A, B, C, and H come respectively from the genus-0 twisting component, the Feynman-transform involution, the cross-polarized splitting, and the degree-preserving sub-MC sector.`

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14484` — PROBLEM: the file states `\kappa=\operatorname{av}(r(z))` as the theorem-D extraction rule; the same bare formula recurs at `:2943`. But the same file later gives the affine Kac--Moody correction `\operatorname{av}(r(z))+\tfrac12\dim(\fg)=\kappa(V_k(\fg))` at `:3117-3124`. The seam therefore drops the non-abelian Sugawara shift exactly where it connects ordered `r`-matrix data to scalar `\kappa`. FIX: at `:14484` replace the sentence by `Theorem~D extracts the scalar \kappa from the coinvariant degree-2 projection of the ordered spectral r-matrix; in the trace-form convention this is \operatorname{av}(r(z)) for abelian families and \operatorname{av}(r(z))+\tfrac12\dim(\fg) for affine Kac--Moody.` Replace `:2943` by the same family-sensitive statement.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:48` — PROBLEM: the chapter opens by treating `\Theta_{\cA}`, `\kappa`, `\mathfrak C`, and `\mathfrak Q` as unqualified bar-theoretic invariants, but only later admits at `:3556-3563` that MC2 in this file is the symmetric/coinvariant statement and the ordered lift `\Theta_{\cA}^{E_1}` lives in the ordered chapter. The seam from `chiral_koszul_pairs.tex` never explicitly says whether the shadow tower here is built from `B^{\mathrm{ord}}` or from its coinvariant shadow. FIX: insert after line `47`: `In this chapter the shadow tower is the symmetric/coinvariant projection of the ordered E_1 theory. The ordered bar complex B^{\mathrm{ord}}(\cA) and its Maurer--Cartan element \Theta_{\cA}^{E_1} are constructed in Chapter~\ref{chap:e1-modular-koszul}; the present \Theta_{\cA}, \kappa, \mathfrak C, \mathfrak Q are their \Sigma_n-coinvariant images under averaging.`

## Summary
Checked: 2 | Findings: 6 | Verdict: FAIL
tokens used
187,810
