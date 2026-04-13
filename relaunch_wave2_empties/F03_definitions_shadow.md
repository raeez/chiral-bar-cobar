# F03_definitions_shadow (841s)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:12206 — PROBLEM: the extension tower and shadow tower are defined in `\mathfrak{g}^{\mathrm{amb}}_\cA/F^{r+1}`, but the same file later puts the same tower in `\gAmod/F^{r+1}` and proves convergence in `\widehat{\gAmod}` at 12425, 13010, and 14743. The carrier object of the foundation is unstable. FIX: make `\mathfrak{g}^{\mathrm{mod}}_\cA` the unique foundational carrier: replace `\mathfrak{g}^{\mathrm{amb}}_\cA` by `\mathfrak{g}^{\mathrm{mod}}_\cA` in 12206 and 12232, redefine the filtration on `\gAmod`, and keep `\mathfrak{g}^{\mathrm{amb}}_\cA` only as a later graph-sum model after an explicit comparison theorem.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:12245 — PROBLEM: `o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})` is cohomology-of-cohomology, because `\cA^{\mathrm{sh}}` is later defined as `H_\bullet(...)` at 12467. The same file uses `H^2(F^{r+1}\gAmod/F^{r+2}\gAmod)` instead at 13010 and 31110. FIX: change 53, 100, 12238-12245, and 14976 to `H^2(F^{r+1}\gAmod/F^{r+2}\gAmod)`; if a shadow-algebra image is wanted, define a separate projection map after 12467 instead of writing `H^2(\cA^{\mathrm{sh}}_{r+1,0})`.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:126 — PROBLEM: the opening classification is wrong and overclaims its source. It says class `L` is the `\kappa=0` case and folds class `C` into `Theorem~\ref{thm:single-line-dichotomy}`, but the actual theorem at 18470 only gives `G/L/M` on a primary line via `(Δ=0,\alpha=0)`, `(Δ=0,\alpha\neq0)`, `Δ\neq0`; class `C` is later supplied globally by `\beta\gamma` in [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1180). FIX: replace 126-146 by a faithful split: primary-line `G/L/M` from `(\Delta,\alpha)` as in 18479-18495, then a separate sentence that class `C` is global and comes from `\beta\gamma` via `thm:betagamma-global-depth`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:16535 — PROBLEM: `Definition~\ref{def:shadow-depth-classification}` identifies the class with total depth `r_{\max}`, but Example 16775 later labels `V_{\mathrm{Leech}}`, rank-48, and rank-72 as class `G` with depths `4,5,6`. The file silently switches from total depth to algebraic depth. FIX: split the notions. Define total depth `d(\cA):=r_{\max}(\cA)` separately, and define the four classes by `d_{\mathrm{alg}}`: `\mathbf G/\mathbf L/\mathbf C/\mathbf M = 0/1/2/\infty`. Then state that `r_{\max}=2,3,4,\infty` only for the primitive archetypes.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:39 — PROBLEM: the first page uses `\gAmod`, and line 180 uses `\Theta_\cA^{E_1}`, before this chapter defines either `\mathfrak g^{\mathrm{mod}}_\cA` or the ordered algebra/averaging map. `\gAmod` only appears formally at 10159; `(\gAmod)^{E_1}` and `\operatorname{av}` are only defined in [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:246). FIX: insert a local foundational convention immediately after line 43: define `\gAmod` by the formula of 10168-10179, import the ordered formula and averaging map from `e1_modular_koszul.tex:246-287`, and only then use `\Theta_\cA^{E_1}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3595 — PROBLEM: the proof of `thm:universal-theta` relies on “the Maurer--Cartan equation” as established infrastructure, but the chapter never promotes that equation to a formal definition/convention before proof use; it appears only as running prose at 37-43. FIX: move 36-43 into a numbered definition or convention placed before the first theorem that uses it, label it, and state explicitly that the strict chapter-level equation is `[\dzero,\Theta_\cA]+\tfrac12[\Theta_\cA,\Theta_\cA]=0` in `\gAmod`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:14975 — PROBLEM: the “tower construction” template reverses the obstruction logic. It says `[o_3]=0` gives `\mathfrak C(\cA)=0`, while `[o_3]\neq0` is where one defines the next correction. That contradicts the actual recursion at 12974-12994, where vanishing of the obstruction class is the condition for choosing the next lift. FIX: rewrite Steps 2 and 3 to match 12988-12993: “If `[o_{N+1}]=0`, choose `-h(o_{N+1})` and adjoin it as the next correction; in the Gaussian/contact special cases that correction may itself vanish.”

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:12512 — PROBLEM: the shadow algebra definition equates invariants with whole graded pieces: `\kappa(\cA)=\cA^{\mathrm{sh}}_{2,0}`, `\Delta_\cA=\cA^{\mathrm{sh}}_{2,*}`, etc. Those are type errors, and they also collapse the full degree-2 truncation to the scalar `\kappa` alone, contradicting the later spectral projection at 4289-4297. FIX: replace 12250, 12365, 12512-12515, and 14968 by projection/membership statements: `\mathfrak C(\cA)\in\cA^{\mathrm{sh}}_{3,0}`, `\mathfrak Q(\cA)\in\cA^{\mathrm{sh}}_{4,0}`, `\operatorname{Sh}_r(\cA)\in\cA^{\mathrm{sh}}_{r,\bullet}`, and describe `\kappa(\cA)` as the scalar trace of the quadratic shadow while the non-scalar quadratic shadow is `T_{\mathrm{br},\cA}` with `\Delta_\cA(x)=\det(1-xT_{\mathrm{br},\cA})`.

## Summary
Checked: 10 | Findings: 8 | Verdict: FAIL


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
session id: 019d8693-d522-71d0-847c-7f68f5d46d7a
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_modular_koszul.tex

Check: is the shadow tower Theta_A formally defined? Are G/L/C/M classes defined before use? Is the MC equation stated as a definition before being invoked in proofs? Is the convolution algebra g^{E1} and g^{mod} defined?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Planning an audit**

I need to audit the specific file higher_genus_modular_koszul.tex and check related dependencies or definitions imported elsewhere. The user requests a thorough audit, so I’ll aim to be a harsh adversarial auditor and ensure every claim is based on my actual readings in the file. I’ll use my deep-beilinson-audit skill and consider reading through related documents like CLAUDE.md and the theorem registry. It seems I’ll want to use an explorer agent for codebase questions since this isn't strictly code.
thinking
**Preparing for file audit**

I need to ground myself by reading actual files, even though the explorers might be authoritative. The user emphasizes that I should verify every claim based on what I've read. I’ll identify relevant files through the explorer but still read them myself for accuracy, noting exact line numbers. I might also check surrounding files for definitions or macros and could use rg for searches. It seems wise to prepare a commentary update acknowledging the user's request before diving deeper into exploration. Let's get started on that!
codex
Using `deep-beilinson-audit` for a hostile foundation audit of `chapters/theory/higher_genus_modular_koszul.tex`. I’m reading the governing files and then the target chapter with exact line references, focusing on definition order, hidden imports, and whether the named objects actually exist before they are used.
exec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g '*/red_team_summary.md' -g 'chapters/theory/higher_genus_modular_koszul.tex' -g '.agents/skills/deep-beilinson-audit/SKILL.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/concordance.tex
chapters/theory/higher_genus_modular_koszul.tex
Plan update
Set up an adversarial audit focused on the requested foundation surface and required constitutional reads before evaluating findings.
  → Read governing instructions and audit skill workflow
  • Read target chapter and map definitions/usages with line numbers
  • Cross-check whether required objects are defined locally or hidden-imported
  • Re-verify findings and produce exact-fix audit report

thinking
**Locating the skill file**

I need to read the skill file, but it seems like rg didn't list it. I wonder if that’s because of the path or if it’s hidden? Okay, I’ll focus on locating it properly. It's crucial to find out where that file is, so I can access it and make sure everything's in order. Let's explore this together and figure it out!
codex
The constitutional files are present; next I’m loading the audit skill and the target surfaces, then I’ll trace whether the chapter actually defines its primitives or is leaning on unstated imports.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Preparing for file inspection**

I need to read the red team summary and locate the target file, considering using line numbering. I'll check with tools like nl -ba or rg to get the line details. My plan includes searching for terms like shadow tower, Theta_A, G/L/C/M, the MC equation, and specific variables. I need to identify if definitions are missing or if there are hidden imports based on the user's request for a foundation audit, ensuring I capture the exact findings and necessary fixes.
codex
I’ve loaded the constitutional and registry surfaces. Now I’m mapping the target chapter’s actual definition/use graph for `\Theta_\cA`, the shadow tower, `\mathfrak g^{E1}`, `\mathfrak g^{mod}`, G/L/C/M, and the MC equation, with exact line numbers before I decide what survives as a finding.
exec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theta|shadow tower|shadow|G/L/C/M|class~G|class~L|class~C|class~M|Maurer|MC equation|g\\"'^'"\\{E1\\}|g\\"'^'"\\{mod\\}|mathfrak\\{g\\}|convolution|\\bG\\b|\\bL\\b|\\bC\\b|\\bM\\b|four-class|four classes|formal depth|d_alg|r_max|def:.*shadow|def:.*mc|def:.*convolution|def:.*class\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
Total output lines: 4509

7:rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
16:$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
30:curve over $\overline{\mathcal{M}}_{g,n}$, the cobar functor
37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
41: d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
46:$\Theta_\cA$ carries.
50:the cubic shadow~$\mathfrak{C}$ at degree~$3$,
54:do not obstruct existence of~$\Theta_\cA$; they obstruct its
57:%% CARRIER ALGEBRA: strict model of the L-infinity deformation complex.
59:The algebraic carrier of this structure is the modular convolution
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
70:Five constructions govern $\Theta_\cA$.
75: The MC element $\Theta_\cA$ lives in an infinite-dimensional
80: (Definition~\ref{def:shadow-algebra})
82: degree-$r$, genus-$g$ projections of~$\Theta_\cA$.
85: The shadow algebra records \emph{what} the projections are;
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   34979 chapters/theory/higher_genus_modular_koszul.tex

thinking
**Inspecting large files**

I need to look at a huge output, likely by checking the first few lines of the file, maybe the first 220. Definitions are probably at the beginning, so I should inspect those relevant sections. I’m thinking about using a command like nl -ba to get a clearer view. It’s crucial to pinpoint exact line numbers, especially around the definitions for concepts like shadow algebra and the shadow Postnikov tower.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2620,2725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3560,3838p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31690,32060p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2620	 (Theorem~\ref{thm:genus-universality}).
  2621	\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
  2622	 of free energies determined by the bar complex at genus~$g$
  2623	 (Theorem~\ref{thm:universal-generating-function}).
  2624	\end{enumerate}
  2625	Both components are established. The Heisenberg specialization
  2626	appears in Chapter~\ref{ch:heisenberg-frame},
  2627	Definition~\ref{def:frame-modular-package}.
  2628	
  2629	\smallskip
  2630	\emph{The spectral discriminant}
  2631	$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
  2632	encodes bar cohomology dimensions
  2633	(Theorem~\ref{thm:ds-bar-gf-discriminant}).
  2634	It is a separate non-scalar invariant depending on
  2635	the full quadratic OPE data, not
  2636	on~$\kappa(\cA)$ alone.
  2637	\end{definition}
  2638	
  2639	\begin{definition}[Full modular characteristic package]
 succeeded in 51ms:
 31690	 - d_{\mathrm{sew}}^{(2)}
 31691	 - d_{\mathrm{pf}}^{(2)}.
 31692	\end{align*}
 31693	The genus-$2$ right side decomposes into three shells:
 31694	\[
 31695	\Theta_\cA^{(2)}
 31696	\;=\;
 31697	\underbrace{\Theta_{\mathrm{loop}\circ\mathrm{loop}}^{(2)}}_
 31698	 {-\frac{1}{2}[\Theta^{(1)},\Theta^{(1)}]}
 31699	\;+\;
 31700	\underbrace{\Theta_{\mathrm{sep}\circ\mathrm{loop}}^{(2)}}_
 31701	 {-\Delta(\Theta^{(1)}) - d_{\mathrm{sew}}^{(2)}}
 31702	\;+\;
 31703	\underbrace{\Theta_{\mathrm{pf}}^{(2)}}_
 31704	 {-d_{\mathrm{pf}}^{(2)}}.
 31705	\]
 31706	\end{corollary}
 31707	
 31708	\begin{theorem}[Genus-$2$ shell activation as depth diagnostic;
 31709	\ClaimStatusProvedHere]
 succeeded in 51ms:
  3560	\begin{remark}[Shared discriminant, distinct sewing]\label{rem:shared-discriminant-sheet}
  3561	The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
  3562	\end{remark}
  3563	
  3564	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3565	\label{thm:universal-theta}
  3566	\index{universal Maurer--Cartan class|textbf}
  3567	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3568	projective curve~$X$ with non-degenerate invariant form,
  3569	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3570	universal Maurer--Cartan class
  3571	\[
  3572	\Theta_{\cA} \in
  3573	\operatorname{MC}\!\bigl(
  3574	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3575	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3576	\bigr)
  3577	\]
  3578	such that:
  3579	\begin{enumerate}[label=\textup{(\roman*)}]
codex
The early chapter already exposes one likely failure mode: it names four classes and two convolution algebras before I’ve seen formal local definitions. I’m checking whether those are actually defined later in this file or only by off-file imports, and whether the order is clean enough to support the claims made at the start.
exec
/bin/zsh -lc "rg -n \"label\\{def:shadow-postnikov-tower\\}|label\\{def:shadow-algebra\\}|label\\{def:modular-convolution-dg-lie\\}|label\\{def:modular-deformation-complex\\}|label\\{def:full-modular-package\\}|label\\{def:scalar-modular-package\\}|label\\{def:modular-characteristic-package\\}|label\\{def:shadow-depth-classification\\}|label\\{def:two-level-convention\\}|label\\{subsec:two-level-convention\\}|label\\{thm:e1-mc-element\\}|label\\{const:explicit-convolution-bracket\\}|label\\{thm:convolution-dg-lie-structure\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\newcommand\\\\gAmod|\\\\def\\\\gAmod|\\\\newcommand\\\\Gmod|\\\\def\\\\Gmod|\\\\newcommand\\\\Defcyc|\\\\newcommand\\\\Definfmod|\\\\newcommand\\\\gAmod|\\\\newcommand\\\\MC|\\\\newcommand\\\\dzero\" -g '*.tex' -g '*.sty' ." in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\newcommand\gAmod|\def\gAmod|\newcommand\Gmod|\def\Gmod|\newcommand\Defcyc|\newcommand\Definfmod|\newcommand\gAmod|\newcommand\MC|\newcommand\dzero)
                  ^^
error: unrecognized escape sequence
 succeeded in 52ms:
2610:\label{def:modular-characteristic-package}
2611:\label{def:scalar-modular-package}
2640:\label{def:full-modular-package}
10160:\label{def:modular-convolution-dg-lie}
10229:\label{thm:convolution-dg-lie-structure}
10364:\label{const:explicit-convolution-bracket}
10809:\label{subsec:two-level-convention}
12215:\label{def:shadow-postnikov-tower}
12468:\label{def:shadow-algebra}
16527:\label{def:shadow-depth-classification}
exec
/bin/zsh -lc "rg -n \"label\\{def:shadow-depth-classification\\}|class~\\\\\\\\mathsf\\{G\\}|class~\\\\\\\\mathbf\\{G\\}|archetype classification|nms-archetype|four-class\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"g\\"'^'"\\{E_1\\}|g\\"'^'"\\{mod\\}|mathfrak\\{g\\}_\\\\cA\\"'^'"\\{\\\\mathrm\\{mod\\}\\}|mathfrak\\{g\\}_\\\\cA\\"'^'"\\{E_1\\}|coinvariant modular convolution|ordered.*MC|averaging sends|Theta_\\\\cA\\"'^'"\\{E_1\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/algebraic_foundations.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
154: obstructions at degrees $2$, $3$, $4$, and the four-class
11792:The archetype classification
16485:four-class partition
16527:\label{def:shadow-depth-classification}
16836:\begin{theorem}[Shadow archetype classification]
16840:\index{shadow archetype classification|textbf}
17083:is a strict four-class refinement of the binary formal/non-formal
19234:The four-class partition
31856:By the archetype classification
31857:(Theorem~\ref{thm:nms-archetype-trichotomy}):
32088:The archetype classification
32089:(Theorem~\ref{thm:nms-archetype-trichotomy})
 exited 2 in 52ms:
rg: regex parse error:
    (?:g\^\{E_1\}|g\^\{mod\}|mathfrak\{g\}_\cA\^\{\mathrm\{mod\}\}|mathfrak\{g\}_\cA\^\{E_1\}|coinvariant modular convolution|ordered.*MC|averaging sends|Theta_\cA\^\{E_1\})
                                           ^^
error: unrecognized escape sequence

thinking
**Inspecting definitions and quotes**

I need to ensure I have the correct regular expressions for quoting. It seems I might need to use fixed strings. I'll look into sections around the labels and definitions, specifically inspecting ranges 10080-10880, 12180-12550, and 16480-16920. Additionally, I should check for definitions and possibly hidden imports in the macros file. It sounds like searching for macro definitions in the preamble could be useful, and fixed strings with `rg` might be helpful here.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10090,10890p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 10090	measured by $\Theta_{\cA}$.
 10091	
 10092	Theorem~C
 10093	(Theorem~\ref{thm:quantum-complementarity-main}): the ambient
 10094	moduli cohomology $\mathcal{H}_g(\cA) =
 10095	H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$ carries a
 10096	shifted-symplectic pairing from Verdier duality, and the deformation
 10097	and obstruction spaces of a Koszul pair embed as complementary
 10098	Lagrangians.
 10099	
 10100	Theorem~D$_{\mathrm{scal}}$
 10101	(Theorem~\ref{thm:modular-characteristic}): a single number
 10102	$\kappa(\cA)$ determines the scalar invariants of the modular
 10103	characteristic hierarchy. It is universal (controls all genera),
 10104	additive (a group homomorphism under tensor product), duality-constrained
 10105	($\kappa + \kappa' = 0$ for KM/free fields); its vanishing is anomaly cancellation.
 10106	
 10107	Theorem~D$_\Delta$
 10108	(Theorem~\ref{thm:spectral-characteristic}): the spectral
 10109	discriminant is a separately proved non-scalar invariant.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12180,12560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16480,16930p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
 16480	through seven degrees, with the all-degree identification
 16481	proved non-constructively by induction
 16482	\textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}}\textup{)}.
 16483	
 16484	In the depth classification, this confirms that the
 16485	four-class partition
 16486	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 16487	is an operadic invariant: it measures the $L_\infty$-formality
 16488	level of $\gAmod$ simultaneously in the $A_\infty$
 16489	\textup{(}associative\textup{)} and $L_\infty$
 16490	\textup{(}Lie\textup{)} pictures. The agreement at
 16491	degrees $5$--$7$ for the Virasoro algebra is a nontrivial
 16492	check because the $A_\infty$ tree formula
 16493	\textup{(}$14 + 42 + 132$ trees at degrees $5$--$7$
 16494	via HPL\textup{)} and the $L_\infty$ stable-graph expansion
 16495	\textup{(}$105 + 945 + 10395$ trivalent trees at degrees
 16496	$5$--$7$\textup{)} count different combinatorial objects
 16497	yet produce the same scalar value $S_k$ on the primary
 16498	line.
 16499	\end{corollary}
 succeeded in 54ms:
 12180	\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
 12181	\;:\; \varphi_{g,r;d} = 0 \;\text{for all}\;
 12182	(g,r,d) \;\text{with}\; w(g,r,d) < N\bigr\}.
 12183	\]
 12184	This filtration is \emph{exhaustive}
 12185	($\mathfrak{g}^{\mathrm{amb}} = F^1$),
 12186	\emph{separated}
 12187	($\bigcap_{N} F^N = 0$),
 12188	\emph{complete} (the completion
 12189	$\widehat{\mathfrak{g}}^{\mathrm{amb}}
 12190	= \varprojlim_N \mathfrak{g}^{\mathrm{amb}}/F^{N+1}$
 12191	equals the product of weight-$w$ components), and
 12192	\emph{pronilpotent}
 12193	($[F^{N_1}, F^{N_2}] \subseteq F^{N_1 + N_2 - 2}$;
 12194	the shift $-2$ is from degree reduction upon gluing two
 12195	external legs).
 12196	\end{definition}
 12197	
 12198	\begin{definition}[Extension tower]
 12199	\label{def:extension-tower}
exec
/bin/zsh -lc "rg -n -F '\\newcommand{\\gAmod}' . && rg -n -F '\\newcommand{\\Gmod}' . && rg -n -F '\\newcommand{\\Defcyc}' . && rg -n -F '\\newcommand{\\Definfmod}' . && rg -n -F '\\newcommand{\\dzero}' ." in /Users/raeez/chiral-bar-cobar succeeded in 103ms:
./main.tex:509:\newcommand{\Definfmod}{\operatorname{Def}_{\infty}^{\mathrm{mod}}} % homotopy-invariant modular deformation object
./main.tex:500:\newcommand{\dzero}{d_0} % genus-0 collision differential (Arnold d^2=0)
./wave2_audit_20260413_001942/C10_en_koszul_duality.md:1149:main.tex:500:\newcommand{\dzero}{d_0} % genus-0 collision differential (Arnold d^2=0)
./relaunch_20260413_111534/F16_undefined_macros_v1.md:7:- [HIGH] standalone/introduction_full_survey.tex:280 — PROBLEM: `\dzero` is undefined here and again at 547, 714, 4514, 4783, 5301, and 5307. FIX: add `\newcommand{\dzero}{d_0}` to the macro block near lines 27–101.
./relaunch_20260413_111534/F16_undefined_macros_v1.md:1740:- [HIGH] standalone/introduction_full_survey.tex:280 — PROBLEM: `\dzero` is undefined here and again at 547, 714, 4514, 4783, 5301, and 5307. FIX: add `\newcommand{\dzero}{d_0}` to the macro block near lines 27–101.

thinking
**Searching definitions and strings**

I need to search for g^{E1} to see if ordering and averaging are defined in this file. It’s important to clarify what’s in there to make sense of it all. I should check for fixed strings to ensure I'm pulling the right information. That way, I can get a clearer understanding of how to proceed with the task, making sure I'm thorough and accurate. Let’s see what I can find!
codex
The chapter’s local definitions land very late: `\mathfrak g^{\mathrm{mod}}` at line 10159, the shadow tower at 12214, and the class taxonomy at 16526. I’m now checking every earlier use against those anchors and against the claimed ordered/coinvariant split, because a lot of the opening prose appears to presuppose infrastructure it has not yet built.
exec
/bin/zsh -lc "rg -n -F 'Theta_\\cA"'^{E_1}'"' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{mod}}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:4332:\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\cA)$
chapters/theory/higher_genus_modular_koszul.tex:10151:$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
chapters/theory/higher_genus_modular_koszul.tex:11422:$\mathfrak{g}^{\mathrm{mod}}_\cA$
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
chapters/theory/higher_genus_modular_koszul.tex:3830:$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
chapters/theory/higher_genus_modular_koszul.tex:3833:$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{E_1}'"' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'averaging sends' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:3832:Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb},E_1}_\\cA' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}_{\\cA}"'^{'"\\mathrm{amb},E_1}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb}}_\\cA' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:31396:\mathfrak{g}^{\mathrm{amb},E_1}_\cA / \Sigma
 exited 1 in 52ms:

 succeeded in 51ms:
30861:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31126:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
31398:\mathfrak{g}^{\mathrm{amb}}_\cA.
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}_{\\cA}"'^{'"\\mathrm{amb}}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11280,11500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31300,31420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4300,4448p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31300	 by the same codimension-$2$ cancellation as
 31301	 Theorem~\textup{\ref{thm:ambient-d-squared-zero}}.
 31302	\end{enumerate}
 31303	\end{proposition}
 31304	
 31305	\begin{proof}
 31306	Part~(i): the forgetful map
 31307	$\operatorname{Conf}_n^{\mathrm{ord}} \to
 31308	\operatorname{Conf}_n$ is a principal $\Sigma_n$-bundle
 31309	(finite \'etale cover of degree $n!$).
 31310	Normal crossings is an \'etale-local property: a divisor
 31311	is snc iff it is \'etale-locally a coordinate hyperplane
 31312	arrangement. The normalization of a smooth variety in a
 31313	finite \'etale cover preserves this property,
 31314	giving part~(i).
 31315	
 31316	Part~(ii): each boundary stratum of
 31317	$\operatorname{FM}_n(X \mathbin{|} D)$ is indexed by a
 31318	planted forest $F$
 31319	(\cite[Theorem~3.3.1(2)]{Mok25}). The fibre over a
 succeeded in 52ms:
  4300	 \textup{(}the degree-$r$ component of the shadow algebra,
  4301	 Definition~\textup{\ref{def:shadow-algebra}}\textup{)}.
  4302	\end{enumerate}
  4303	The scalar, spectral, and quartic invariants are the first three
  4304	visible shadows of one master object. Two algebras share a
  4305	spectral sheet if and only if they share the same quadratic shadow;
  4306	the quartic resonance shadow first separates algebras on the same
  4307	sheet.
  4308	\end{corollary}
  4309	
  4310	\begin{proof}
  4311	Each projection is the restriction of
  4312	$\Theta_\cA = D_\cA - \dzero$ to the relevant bigraded
  4313	component of $\cA^{\mathrm{sh}} =
  4314	H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
  4315	(Definition~\ref{def:shadow-algebra}):
  4316	(i) is the $(r{=}2, g{=}\bullet)$ scalar trace,
  4317	(ii) is the $(r{=}2, g{=}\bullet)$ matrix-valued component,
  4318	(iii) is $(r{=}4, g{=}0)$,
  4319	(iv) is $(r, g{=}\bullet)$ in general.
 succeeded in 52ms:
 11280	\check{C}^\bullet(\mathfrak{U};\, \cA)
 11281	\]
 11282	carries a $\mathrm{Ch}_\infty$-algebra structure
 11283	\cite[Theorem~3.1]{MS24}: higher operations
 11284	$F_n\colon \mathrm{Lie}(n) \otimes \mathcal{Y}(n) \to
 11285	P_n(\{A^{\mathrm{ch}}_\infty\},\, A^{\mathrm{ch}}_\infty)$
 11286	encode all derived OPE data. Different covers yield
 11287	quasi-isomorphic $\mathrm{Ch}_\infty$-algebras
 11288	(Corollary~\ref{cor:rectification-ch-infty}).
 11289	\end{construction}
 11290	
 11291	\begin{construction}[Logarithmic FM coefficient cooperad;
 11292	\ClaimStatusProvedElsewhere]
 11293	\label{const:vol1-logfm-coefficient-cooperad}
 11294	\index{logarithmic Fulton--MacPherson!coefficient cooperad}
 11295	For a logarithmic boundary pair $(X, D)$ or a semistable
 11296	degeneration $W \to B$, define
 11297	\begin{align}
 11298	\cC^{\log\mathrm{FM}}_{X \mathbin{|} D}(n)
 11299	&\;:=\;




thinking
**Inspecting definition usage**

I need to check the usage of the definition `Definition\ref{def:modular-characteristic-package}` around line 17 and `\S\ref{subsec:two-level-convention}` around line 62. This seems like a local forward reference, which could be a problem. It looks like foundational prose is using objects before their definitions are presented. I should consider how serious this is since the user asked for a foundation audit, and missing definitions or hidden imports could be significant findings.
thinking
**Refining audit suggestions**

I'm focusing on providing precise fixes for definitions and equations. The user wants exact line-by-line suggestions, such as inserting a "Foundational prerequisites" paragraph or moving definitions. I need to state what needs to be inserted, ensuring clarity without being too verbose. This includes providing specifics like moving a definition from one line to another and offering clear replacement text. It’s all about being grounded in the content without making guesses.
thinking
**Analyzing definitions**

I’m considering how to propose a compact local preview definition and thinking about whether my fix should be more direct. I might suggest specific text replacements, like replacing lines 121-166 with later definitions. But first, I need to inspect the actual definitions for mismatches. For instance, the shadow tower, Theta_A, isn't formally defined until a later line, which could be problematic since references appear before its definition. I need to check various lines to confirm how these definitions interact.
thinking
**Clarifying definitions**

In the earlier part of the document, I see that $\Theta_\cA^{\leq r}$ is introduced as a "graph sum through degree r" with vertex labels and edge contractions around lines 64-66. This specific formula is actually more detailed than the formal definition that appears later on. It’s important to highlight this discrepancy, as having a more specific phrase earlier could confuse readers about the expectations of the formal definition that follows. I need to ensure clarity in my suggestions about these definitions.
codex
A concrete inconsistency just surfaced: the shadow tower is defined in the ambient algebra quotient at lines 12230–12233, but the figure caption later says the same levels live in `\gAmod/F^{r+1}` at lines 12425–12428. I’m tracing whether the file ever identifies those two algebras or whether this is an uncorrected object swap.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30780,30980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{def:ambient-modular-complementarity-algebra\\}|ambient modular complementarity algebra|g\\"'^'"\\{amb\\}|mathfrak\\{g\\}\\"'^'"\\{\\mathrm\\{amb\\}\\}|shadow obstruction tower.*gAmod|gAmod/F\\"'^'"\\{r\\+1\\}|g\\"'^'"\\{amb\\}.*gAmod|ambient algebra.*convolution algebra|identify.*ambient.*convolution\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 30780	($\ell_3^{(0)}, \ell_4^{(0)}, \ldots$) and all genus-$g \geq 1$
 30781	BV-type loop operators. These contribute
 30782	$O(\hbar^2)$ and higher to the partition function; the genus-$1$
 30783	boundary recursion from the genus-$0$ master element is determined
 30784	entirely by $D\Theta$ and $[\Theta,\Theta]$.
 30785	The full quantum $L_\infty$ equation is needed for
 30786	\emph{gauge equivalences between different presentations} and for
 30787	\emph{homotopy transfer to the minimal model}: the transferred
 30788	operations $\ell_n^{\mathrm{tr}}$ that label the vertices of the
 30789	graph sum~\eqref{eq:modular-bar-hamiltonian} are precisely the
 30790	quantum $A_\infty$-minimal model operations.
 30791	
 30792	The shadow obstruction tower is the direct manifestation of this homotopy
 30793	structure: the degree-$r$ shadow $\operatorname{Sh}_r(\cA)$ is
 30794	the genus-$0$ component of $\ell_r^{(0)}(\Theta^{\otimes r})$,
 30795	and the genus-$1$ Hessian correction
 30796	$\delta H^{(1)} = \Lambda_P(\mathfrak{Q})$ comes from
 30797	$\ell_1^{(1)}(\Theta)$. The full shadow calculus
 30798	(\S\ref{sec:heisenberg-shadow-gaussianity}--\S\ref{sec:mixed-cubic-quartic-shadows}
 30799	and Appendix~\ref{app:nonlinear-modular-shadows}) is the
 exited 2 in 50ms:
rg: regex parse error:
    (?:label\{def:ambient-modular-complementarity-algebra\}|ambient modular complementarity algebra|g\^\{amb\}|mathfrak\{g\}\^\{\mathrm\{amb\}\}|shadow obstruction tower.*gAmod|gAmod/F\^\{r\+1\}|g\^\{amb\}.*gAmod|ambient algebra.*convolution algebra|identify.*ambient.*convolution)
                                                                                                                                ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12198,12440p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12198	\begin{definition}[Extension tower]
 12199	\label{def:extension-tower}
 12200	The \emph{modular extension tower} of $\cA$ is the inverse system
 12201	\begin{equation}
 12202	\label{eq:extension-tower}
 12203	\mathcal{E}_{\cA}(N)
 12204	:=
 12205	\operatorname{MC}\bigl(
 12206	\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
 12207	\bigr),
 12208	\qquad N \geq 1.
 12209	\end{equation}
 12210	A full lift is a compatible point of the inverse limit
 12211	$\Theta_{\cA} \in \varprojlim_N \mathcal{E}_{\cA}(N)$.
 12212	\end{definition}
 12213	
 12214	\begin{definition}[Shadow obstruction tower]
 12215	\label{def:shadow-postnikov-tower}
 12216	\ClaimStatusProvedHere
 12217	\index{shadow obstruction tower|textbf}

thinking
**Searching for algebra discrepancies**

I'm noticing an inconsistency between ambient algebra and convolution. I need to identify why that is, so I’m thinking about searching for something like "ambient algebra is strict model of convolution." It looks like the ambient algebra at 30900 represents a different vector space compared to convolution. Maybe there’s a mapping or isomorphism in play? I should definitely dive into my search to clarify this!
exec
/bin/zsh -lc "rg -n -F 'strict model' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb}}_\\cA' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ambient algebra' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
30861:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31126:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
31398:\mathfrak{g}^{\mathrm{amb}}_\cA.
 succeeded in 52ms:
57:%% CARRIER ALGEBRA: strict model of the L-infinity deformation complex.
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
4028:This dg~Lie algebra is a strict model of the full cyclic
10162:The following dg~Lie algebra is the strict model of the modular
10217:The strict model suffices for all Maurer--Cartan computations in
10692:chain-level correction that upgrades the strict model
10754:The strict model $\Convstr$ has $\ell_n = 0$ for
10772: particular strict model of $\cA'$.
10778: it is independent of the choice of strict model
10791: strict differential and bracket. In the strict model,
10805:%% Two-level convention: strict models and homotopy-invariant objects
10808:\subsection{The two-level convention: strict models and homotopy-invariant objects}
10815:as a \emph{strict model} of an underlying homotopy-invariant
10823:Definition~\ref{def:modular-convolution-dg-lie} is its strict model.
10829:The \emph{reason} the strict model suffices for MC elements is
10838:The strict model has $\ell_k = 0$ for $k \geq 3$, so it computes
10901:strict model: $\ell_1 = D$, $\ell_2 = [-,-]$,
10953:strict model are related by $L_\infty$-quasi-isomorphisms
11060:All dg~Lie algebras in this monograph are functorial strict models
11067: \operatorname{End}_{\cA}\bigr)$ is a strict model of
 succeeded in 50ms:
20588: of the ambient algebra.
30811:ambient algebra:
30843:at the full homotopy level the ambient algebra
30861:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31125:The weight filtration on the ambient algebra
31371:\begin{definition}[Ordered ambient algebra]
31374:\index{ambient algebra!ordered variant|textbf}
31375:\index{E1 algebra@$E_1$-algebra!ordered ambient algebra}
31408:on the ambient algebra
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11040,11140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4010,4055p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30490,30590p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 11040	\end{proposition}
 11041	
 11042	\begin{proof}
 11043	Parts~(i)--(ii): standard deformation theory for MC elements in
 11044	complete filtered $L_\infty$-algebras
 11045	(Manetti~\cite{Manetti04a}).
 11046	Part~(iii): the genus filtration is compatible with
 11047	the $L_\infty$-structure
 11048	(Theorem~\ref{thm:modular-homotopy-convolution}).
 11049	Part~(iv): $\dim H^1(T^{\mathrm{mod}}_{\Theta_{\cH_k}})=1$
 11050	(one-channel, scalar saturation); for Virasoro,
 11051	$H^1$ is infinite-dimensional by the non-termination of
 11052	the shadow obstruction tower ($o^{(r)}_{\mathrm{Vir}}\neq 0$ for all
 11053	$r\geq 5$).
 11054	\end{proof}
 11055	
 11056	\begin{corollary}[Strictification comparison;
 11057	\ClaimStatusProvedHere]
 11058	\label{cor:strictification-comparison}
 11059	\index{strictification comparison}
 succeeded in 51ms:
  4010	= \underbrace{\dzero^2}_{=\,0}
  4011	+ [\dzero, \Theta_\cA]
  4012	+ \tfrac{1}{2}[\Theta_\cA, \Theta_\cA],
  4013	\]
  4014	where brackets denote the graded commutator in the coderivation
  4015	algebra~(F3). Since $\dzero^2 = 0$:
  4016	\[
  4017	[\dzero, \Theta_\cA]
  4018	+ \tfrac{1}{2}[\Theta_\cA, \Theta_\cA]
  4019	= 0,
  4020	\]
  4021	which is the Maurer--Cartan equation
  4022	$l_1(\Theta_\cA) + \tfrac12 l_2(\Theta_\cA, \Theta_\cA) = 0$
  4023	in the dg~Lie algebra $\Defcyc(\cA) \widehat{\otimes} \Gmod$
  4024	with $l_1 = [\dzero,-]$ and $l_2 = [-,-]$.
  4025	By~(F4), this is the same completed algebra as the genuswise product in
  4026	\eqref{eq:theta-bar-intrinsic}; no further identification is being
  4027	used tacitly.
  4028	This dg~Lie algebra is a strict model of the full cyclic
  4029	$L_\infty$-structure
 succeeded in 50ms:
 30490	\ClaimStatusProvedHere
 30491	\index{rectification!meta-theorem|textbf}
 30492	\index{formality!modular convolution algebra}
 30493	\begin{enumerate}[label=\textup{(\roman*)}]
 30494	\item \emph{Scalar-orbit formality.}
 30495	 Assume the full universal Maurer--Cartan element is scalar:
 30496	 \[
 30497	 \Theta_\cA
 30498	 \;=\;
 30499	 \kappa(\cA)\cdot \eta \otimes \Lambda.
 30500	 \]
 30501	 Then the distinguished scalar Maurer--Cartan orbit in
 30502	 $\Convinf(\cA)$ is formal: the higher transferred brackets
 30503	 vanish on the scalar line
 30504	 $\mathbb{C}\!\cdot\!\eta\otimes\Lambda$, and the MC equation
 30505	 restricts there to the scalar genus identities.
 30506	 No converse is proved here. In particular, one-channel
 30507	 minimal-model concentration
 30508	 $\Theta_\cA^{\min}=\eta\otimes\Gamma_\cA$ does not by itself
 30509	 imply scalar saturation, nor does it identify the full MC moduli

thinking
**Clarifying definitions and fixes**

I need to define the fix more clearly, possibly by renaming κ_d to d_alg and introducing a total shadow depth d_tot at line 16535ff. The user's mission is focused on whether G/L/C/M classes are defined before use, which makes me question the definitions themselves for consistency. I should verify by searching if there's a different d_alg defined earlier, especially since line 146 mentions prop depth-gap-trichotomy. I'll inspect around that to gather more information.
codex
Another deeper failure is now clear: the file does not just delay the G/L/C/M definition, it destabilizes it. One block ties the classes to total shadow depth `r_max = 2,3,4,∞`, while a later example labels lattices as class `G` with depths `4,5,6`. I’m tracing the exact points where “class” silently switches from total depth to algebraic depth.
exec
/bin/zsh -lc "rg -n -F 'depth-gap-trichotomy' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'd_{\\mathrm{alg}}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17020,17120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16775,16830p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
146: No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
17580:\label{prop:depth-gap-trichotomy}
17776:Proposition~\ref{prop:depth-gap-trichotomy} without using the
 succeeded in 52ms:
147: $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$, with a gap at~$3$.
16786:$d_{\mathrm{alg}}$ &
16814: (\S\ref{sec:higher-depths}; class by $d_{\mathrm{alg}}$, cf.\
16844: d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
16854:$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
16861:$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
16868:$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
16887:$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
16920:$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
16948:$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
17579:\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
17588: d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
17593: $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
17594:\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
17604:\item no value $d_{\mathrm{alg}} = 3$
17605: \textup{(}or any finite $d_{\mathrm{alg}} \geq 3$\textup{)}
17633:$d_{\mathrm{alg}} \in \{0, 1\}$ according to whether
17635:(class~$\mathbf{G}$, $d_{\mathrm{alg}} = 0$),
17637:(class~$\mathbf{L}$, $d_{\mathrm{alg}} = 1$).
17648:$d_{\mathrm{alg}} = \infty$ (class~$\mathbf{M}$).
 succeeded in 51ms:
 17020	\draw[thick, black!40] (1.65,1.5) -- (2.35,1.5);
 17021	\node[font=\tiny, text=black!50] at (2,1.25) {\textsf{terminates}};
 17022	%
 17023	% ---- M column: infinite tower ----
 17024	\node[font=\scriptsize] at (3,3.8) {$\kappa$};
 17025	\node[font=\scriptsize] at (3,2.9) {$\mathfrak{C} = 2x^3$};
 17026	\node[font=\scriptsize] at (3,2.0)
 17027	 {$\mathfrak{Q}^{\mathrm{ct}} = \tfrac{10}{c(5c+22)}x^4$};
 17028	\node[font=\scriptsize] at (3,1.1)
 17029	 {$o_5 = \{\mathfrak{C},\mathfrak{Q}\}_H \neq 0$};
 17030	\node[font=\scriptsize] at (3,0.2) {$o_r \neq 0\;\forall\,r$};
 17031	\node[font=\tiny, text=black!50] at (3,-0.2) {\textsf{infinite}};
 17032	%
 17033	% ---- Horizontal rule below headers ----
 17034	\draw[black!25] (-0.5,4.3) -- (3.5,4.3);
 17035	%
 17036	% ---- Complexity arrow ----
 17037	\draw[maparrow, black!40] (-0.45,-0.5) -- (3.45,-0.5);
 17038	\node[font=\tiny\scshape, text=black!50, anchor=north] at (1.5,-0.55)
 17039	 {increasing shadow complexity};
 succeeded in 50ms:
 16775	\begin{example}[Shadow depth of all computed families]
 16776	\label{ex:shadow-depth-all-families}
 16777	\index{shadow depth!computed families}
 16778	\begin{center}
 16779	\small
 16780	\renewcommand{\arraystretch}{1.15}
 16781	\begin{tabular}{llcccl}
 16782	\toprule
 16783	\emph{Family} &
 16784	\emph{Class} &
 16785	$d$ &
 16786	$d_{\mathrm{alg}}$ &
 16787	$\Delta$ &
 16788	\emph{Reference} \\
 16789	\midrule
 16790	Heisenberg $\cH_k$ &
 16791	 $\mathbf{G}$ & $2$ & $0$ & $0$ &
 16792	 \S\ref{sec:heisenberg-shadow-gaussianity} \\
 16793	Lattice VOA $V_\Lambda$ &
 16794	 $\mathbf{G}$ & $2$ & $0$ & $0$ &


thinking
**Checking definitions in proofs**

The user asked about the foundation audit, specifically if the MC equation is defined before it's used in proofs. I see that line 36 starts defining Theta_A and the MC equation, but I wonder if it's formal enough. I need to check if their definitions actually appear before the first proof that uses them. I should look for the earliest `\begin{proof}` after line 36 that mentions Theta_A or the MC equation, possibly around line 671 or in theorem 644. It's crucial to confirm that there’s a formal definition and not just a narrative.
thinking
**Validating definitions and proofs**

Line 37 states "Define Theta_A := D_A - d_0" in prose, but I’m not sure if that’s sufficient for the audit. The user specifically asked whether the MC equation is defined before it’s used in proofs. I need to check for proofs that mention "the Maurer–Cartan equation" to see if they come before any formal definition environment or theorem. It’s essential to clarify this to provide an accurate audit response!
codex
I’m checking the use-order of the MC equation now. The file does name `\Theta_\cA := D_\cA-d_0` in the opening prose, but that is not the same as giving a load-bearing formal definition before later proofs cite “the Maurer–Cartan equation” as established infrastructure.
exec
/bin/zsh -lc "rg -n \"Maurer--Cartan equation|MC equation|\\bMC\\b|Theta_\\\\cA := D_\\\\cA - \\\\dzero|Theta_\\\\cA := D_\\\\cA - d_0|D_\\\\cA\\\\Theta_\\\\cA|\\[\\\\Theta_\\\\cA, \\\\Theta_\\\\cA\\]|\\[\\\\Theta_\\\\cA,\\\\Theta_\\\\cA\\]\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:Maurer--Cartan equation|MC equation|\bMC\b|Theta_\cA := D_\cA - \dzero|Theta_\cA := D_\cA - d_0|D_\cA\Theta_\cA|\[\Theta_\cA, \Theta_\cA\]|\[\Theta_\cA,\Theta_\cA\])
                                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"begin\\{proof\\}|end\\{proof\\}|Maurer--Cartan equation|MC equation|Theta_\\\\cA\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:begin\{proof\}|end\{proof\}|Maurer--Cartan equation|MC equation|Theta_\cA)
                                                                             ^^
error: unrecognized escape sequence

thinking
**Simplifying search queries**

I'm considering simpler fixed strings for my search, thinking about using `rg -n -F` for queries. Maybe I could even use multiple queries to make things easier. For example, I could try searching with `rg -n -F "Maurer--Cartan equation"` and separately, `rg -n -F "\Theta_\cA"`. Keeping it straightforward seems like a good approach to avoid confusion! Let's see how these queries work out.
exec
/bin/zsh -lc "rg -n -F 'Maurer--Cartan equation' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\Theta_\\cA' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
3607:gives the Maurer--Cartan equation. See
3747:simultaneously. The Maurer--Cartan equation
4021:which is the Maurer--Cartan equation
4218:assembly rule, and the Maurer--Cartan equation is the infinitesimal
4232:and the Maurer--Cartan equation is a tautological consequence
5315: At each genus~$g$, the Maurer--Cartan equation
5573: The Maurer--Cartan equation in $\widehat{L}_{\Gmod}$ is
9967:differential. The full Maurer--Cartan equation
10718:\begin{remark}[The two Maurer--Cartan equations]
10720:\index{Maurer--Cartan equation!strict vs $L_\infty$}
10722:Maurer--Cartan equation, one in each layer of the two-level
11604:Maurer--Cartan equation is
11701:\item The Maurer--Cartan equation stratifies by weight:
11937:The fixed-$(g,n)$ projection of the Maurer--Cartan equation
12231:of the Maurer--Cartan equation in
12694:consequence of the Maurer--Cartan equation for
12986:+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
13011: satisfies the full Maurer--Cartan equation.
13137: the full Maurer--Cartan equation
 succeeded in 51ms:
37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
41: d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
46:$\Theta_\cA$ carries.
54:do not obstruct existence of~$\Theta_\cA$; they obstruct its
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
70:Five constructions govern $\Theta_\cA$.
75: The MC element $\Theta_\cA$ lives in an infinite-dimensional
82: degree-$r$, genus-$g$ projections of~$\Theta_\cA$.
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
94: The graph-sum formula produces $\Theta_\cA^{\leq r}$ but gives
98: (D_\cA\Theta_\cA^{\leq r}
99: + \tfrac12[\Theta_\cA^{\leq r},\Theta_\cA^{\leq r}])_{r+1}
113: $\Theta_\cA$ exists unconditionally by the bar-intrinsic
114: construction, and $\Theta_\cA^{\leq r}$ are its degree
121:The tower $\Theta_\cA$ forces three questions.
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
251:$\Theta_\cA^{(g)} \in
257:amplitude $Z_g(\cA) = \operatorname{Tr}^{\circ g}(\Theta_\cA^{(g)})$
292:The universal MC element $\Theta_\cA := D_\cA - d_0$

thinking
**Inspecting definitions and references**

I need to look into the definitions around line 292 and the top summaries. Additionally, I should identify any unresolved forward references, particularly `Theorem\ref{thm:e1-mc-element}` and `Chapter\ref{chap:e1-modular-koszul}`. They might be defined elsewhere, so checking for the existence of these labels is important. I’ll need to run a search to clarify any context or missing information! This will really help in understanding the content better.
exec
/bin/zsh -lc "rg -n -F '\\label{chap:e1-modular-koszul}' chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:e1-mc-element}' chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/e1_modular_koszul.tex:10:\label{chap:e1-modular-koszul}
 succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}
exec
/bin/zsh -lc "rg -n -F '\\label{thm:nms-archetype-trichotomy}' chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/nonlinear_modular_shadows.tex:1208:\label{thm:nms-archetype-trichotomy}
exec
/bin/zsh -lc "rg -n -F '\\label{thm:depth-decomposition}' chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/arithmetic_shadows.tex:1788:\label{thm:depth-decomposition}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12096,12170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12996,13080p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12996	
 12997	\begin{theorem}[Recursive existence and shadow obstruction tower convergence;
 12998	\ClaimStatusProvedHere]
 12999	\label{thm:recursive-existence}
 13000	\index{recursive existence!proved}
 13001	\index{shadow obstruction tower!convergence}
 13002	\index{inverse limit!shadow tower}
 13003	Let $\cA$ be a modular Koszul chiral algebra.
 13004	\begin{enumerate}[label=\textup{(\roman*)}]
 13005	\item \emph{Recursive lift.}
 13006	 All obstruction classes in the extension tower
 13007	 $\{\mathcal{E}_{\cA}(N)\}_{N \geq 1}$
 13008	 \textup{(}Definition~\textup{\ref{def:extension-tower})}
 13009	 vanish: for every $N \geq 1$, the class
 13010	 $[\mathfrak{o}_{N+1}] \in
 13011	 H^2(F^{N+1}\gAmod / F^{N+2}\gAmod)$ of
 13012	 Construction~\textup{\ref{constr:obstruction-recursion}}
 13013	 is zero.
 13014	\item \emph{Convergence.}
 13015	 The inverse limit
 succeeded in 52ms:
 12096	
 12097	\item \emph{The genus spectral sequence}
 12098	 (Construction~\ref{const:vol1-genus-spectral-sequence}) arises
 12099	 from the genus filtration $F^g L_{\mathrm{mod}}$ on the modular
 12100	 convolution algebra. Its differentials are the obstruction maps
 12101	 $\operatorname{Ob}_g$: the $d_1$-differential is the curvature
 12102	 $\kappa(\cA) \cdot \omega_1$
 12103	 (Remark~\ref{rem:vol1-curvature-as-d1}), $d_2$ is the genus-$2$
 12104	 obstruction, and so on. The genus spectral sequence does
 12105	 \emph{not} degenerate at~$E_2$ in general: its differentials
 12106	 \emph{are} the genus expansion. For any algebra with
 12107	 $\kappa(\cA) \neq 0$, the $d_1$-differential is already
 12108	 nontrivial.
 12109	
 12110	\item \emph{The flatness argument.}
 12111	 The flatness of bar cohomology over~$\overline{\mathcal{M}}_g$
 12112	 follows from the bar spectral sequence degeneration alone (the
 12113	 PBW/Koszulness input), \emph{not} from any degeneration of the
 12114	 genus spectral sequence. The genus spectral sequence controls a
 12115	 different question: the lift of MC solutions across genera
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14728,14770p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 14728	
 14729	\begin{proof}
 14730	A cyclic Maurer--Cartan element defines a Hamiltonian whose
 14731	Euler--Lagrange equation is the Maurer--Cartan equation. The
 14732	derived intersection of the two Lagrangians is identified with the
 14733	corresponding shifted critical locus.
 14734	\end{proof}
 14735	
 14736	\begin{remark}[The unifying principle]
 14737	\label{rem:unifying-principle}
 14738	\index{unifying principle|textbf}
 14739	\index{shadow obstruction tower!as primary object}
 14740	The \emph{shadow obstruction tower}
 14741	$\Theta_\cA^{\leq 2},\, \Theta_\cA^{\leq 3},\,
 14742	\Theta_\cA^{\leq 4},\, \ldots$
 14743	in the modular convolution algebra
 14744	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is the
 14745	organizing structure from which all five main theorems, the
 14746	nonlinear shadow calculus, and the genus expansion descend.
 14747	Each finite truncation $\Theta_\cA^{\leq r}$ is \emph{proved}

thinking
**Analyzing theorem inconsistencies**

I'm finding an interesting contradiction: remark 14740 mentions a shadow tower in modular convolution algebra, which goes against definition 12232 for ambient algebra. I notice that there might be a problem with the theorem on the recursive existence part, particularly in lines 13006-13013. Those lines reference the extension tower, but the class mentioned is in H^2. I need to double-check specific lines and maybe look closely at the construction `constr:obstruction-recursion` in line 12680.
exec
/bin/zsh -lc "rg -n -F '\\label{constr:obstruction-recursion}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12660,12740p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12976:\label{constr:obstruction-recursion}
 succeeded in 51ms:
 12660	chiral algebras \textup{(}in the sense of
 12661	Proposition~\textup{\ref{prop:mc2-functoriality})},
 12662	the induced map
 12663	$f_*^{\mathrm{sh}}\colon \cA^{\mathrm{sh}} \to
 12664	\cB^{\mathrm{sh}}$
 12665	is a morphism of bigraded Lie algebras.
 12666	If $f$ is a quasi-isomorphism, then $f_*^{\mathrm{sh}}$ is
 12667	an isomorphism. In particular, the shadow algebra
 12668	$\cA^{\mathrm{sh}}$ is an invariant of the
 12669	quasi-isomorphism class of~$\cA$.
 12670	\end{corollary}
 12671	
 12672	\begin{proof}
 12673	Proposition~\ref{prop:mc2-functoriality}(iii) provides
 12674	$f_*^{\mathrm{sh}}$ as a bigrading-preserving map on
 12675	cohomology. It is a Lie algebra morphism because
 12676	$f_*$ is a dg~Lie morphism at the chain level
 12677	(composition with an algebra morphism preserves the
 12678	convolution bracket). For the quasi-isomorphism
 12679	assertion: when $f\colon \cA \to \cB$ is a

thinking
**Inspecting algebra definitions**

I’m realizing there’s a type error regarding direct sums or graded pieces. It seems like there might be a bigger issue with the shadow algebra definition. I should focus on checking lines 4275 regarding shadow extraction to clarify what's going on. It's important to understand these definitions properly to avoid further confusion down the line. Giving this a detailed look is definitely a priority, so I'll dive in and investigate!
codex
I’ve hit a second-order defect inside the formal definition itself: the tower’s first stage is identified with `\kappa(\cA)` alone, but elsewhere the file says the degree-2 shadow also contains spectral data. I’m checking whether this is just shorthand in prose or an actual typed equality that breaks the definition.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12494,12516p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4274,4308p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2600,2640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12494	connects different degree components and drives the
 12495	Maurer--Cartan recursion: the obstruction class
 12496	$o_{r+1}(\cA)$ at degree~$r+1$ is a Lie bracket of
 12497	shadows at degrees~$\leq r$
 12498	\textup{(}Lemma~\textup{\ref{lem:nms-euler-inversion})},
 12499	giving the tower its inductive character.
 12500	\par
 12501	The shadow algebra carries a bigrading by degree
 12502	$r \geq 2$ and genus $g \geq 0$:
 12503	\begin{equation}
 12504	\label{eq:shadow-algebra-bigrading}
 12505	\cA^{\mathrm{sh}}
 12506	=
 12507	\bigoplus_{r \geq 2}\;\bigoplus_{g \geq 0}\;
 12508	\cA^{\mathrm{sh}}_{r,g}.
 12509	\end{equation}
 12510	The projections to graded components recover the individual shadows:
 12511	\begin{itemize}
 12512	\item $\kappa(\cA) = \cA^{\mathrm{sh}}_{2,0}$
 12513	 \quad(the modular characteristic, Theorem~D);
 succeeded in 51ms:
  4274	itself carries independent non-scalar parameters built by
  4275	the homological perturbation recursion
  4276	(Construction~\ref{constr:obstruction-recursion}).
  4277	In both regimes, $\Theta_\cA$ \emph{exists} by the
  4278	bar-intrinsic construction.
  4279	\end{remark}
  4280	
  4281	\begin{corollary}[Shadow extraction; \ClaimStatusProvedHere]
  4282	\label{cor:shadow-extraction}
  4283	\index{shadow extraction|textbf}
  4284	\index{universal Maurer--Cartan class!shadow extraction}
  4285	The bar-intrinsic MC element $\Theta_\cA$ of
  4286	Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
  4287	projections recovering all named modular invariants:
  4288	\begin{enumerate}[label=\textup{(\roman*)}]
  4289	\item \emph{Scalar shadow:}
  4290	 $\pi_{\mathrm{sc}}(\Theta_\cA)
  4291	 = \sum_{g \geq 1} \kappa(\cA)\,\lambda_g$
  4292	 \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
  4293	\item \emph{Spectral shadow:}
 succeeded in 51ms:
  2600	
  2601	On each geometric fiber (a fixed smooth or stable curve), the
  2602	collision differential is genus-$0$ type (with $d_0^2 = 0$), and
  2603	the genus-$g$ quantum corrections live in higher Leray degrees,
  2604	contributing only to $d_r$ for $r \geq 2$. Since $E_2$ is
  2605	already concentrated on the diagonal by Koszul concentration,
  2606	these higher differentials vanish.
  2607	\end{proof}
  2608	
  2609	\begin{definition}[Scalar modular characteristic package]
  2610	\label{def:modular-characteristic-package}
  2611	\label{def:scalar-modular-package}
  2612	\index{modular characteristic package!scalar|textbf}
  2613	Let $\cA$ be a modular Koszul chiral algebra
  2614	(Definition~\ref{def:modular-koszul-chiral}). The
  2615	\emph{scalar modular characteristic package} of~$\cA$ consists of:
  2616	\begin{enumerate}[label=\textup{(\roman*)}]
  2617	\item The \emph{obstruction invariant}
  2618	 $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
  2619	 fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
codex
The definition layer is worse than just being late: it mixes levels. `\cA^{\mathrm{sh}}` is defined as cohomology, but the obstruction class is placed in `H^2(\cA^{\mathrm{sh}}_{r+1,0})`, which is “cohomology of a cohomology object.” I’m verifying whether the file ever repairs that type mismatch elsewhere.
exec
/bin/zsh -lc "rg -n -F 'H"'^2(F''^{N+1}'"\\gAmod / F"'^{N+2}'"\\gAmod)' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'H"'^2('"\\cA"'^{'"\\mathrm{sh}}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'o_{r+1}(\\cA)' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
53:$o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
100: \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
14976:If $[o_3] = 0$ in $H^2(\cA^{\mathrm{sh}}_{3,0})$, the cubic shadow
 succeeded in 51ms:
13011: H^2(F^{N+1}\gAmod / F^{N+2}\gAmod)$ of
 succeeded in 51ms:
53:$o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
97: $o_{r+1}(\cA) :=
4580:$\mathsf{C}$, the obstruction classes $o_{r+1}(\cA) = 0$
4834:$o_{r+1}(\cA)$ at each level
12148:class $o_{r+1}(\cA)$ at degree~$r{+}1$ is a Lie bracket of the
12245:o_{r+1}(\cA)
12469:$o_{r+1}(\cA)$ is a bracket of shadows at degrees~$\leq r$,
12496:$o_{r+1}(\cA)$ at degree~$r+1$ is a Lie bracket of
14765: $o_{r+1}(\cA) \in H^2(F^{r+1}/F^{r+2})$ controlling the next
15136:obstruction $o_{r+1}(\cA) \neq 0$ forcing extension to the next
15197:o_{r+1}(\cA)
30414: $o_{r+1}(\cA)
30420: If $o_{r+1}(\cA) = 0$, there exists
30431: $r_{\max}(\cA) := \sup\{r : o_{r+1}(\cA) \neq 0\}$
31110:obstruction class $o_{r+1}(\cA) \in H^2(F^{r+1}/F^{r+2})$. For a
31113:$\xi^* o_{r+1}(\cA) = o_{r+1}(\cA_1) \otimes 1 + 1 \otimes
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14960,14995p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31100,31124p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 14960	
 14961	\smallskip
 14962	\noindent\textbf{Input}: a cyclic chiral algebra~$\cA$ with cyclic
 14963	deformation complex $\Defcyc(\cA)$, Hessian~$H_{\cA}$,
 14964	propagator~$P_{\cA}$.
 14965	
 14966	\smallskip
 14967	\noindent\textbf{Step~1} (Degree~$2$).
 14968	Solve the Maurer--Cartan equation at weight~$2$.
 14969	The unique solution is $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$, the
 14970	modular characteristic (Theorem~D).
 14971	
 14972	\smallskip
 14973	\noindent\textbf{Step~2} (Degree~$3$).
 14974	Compute the obstruction $o_3(\cA) =
 14975	(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
 14976	If $[o_3] = 0$ in $H^2(\cA^{\mathrm{sh}}_{3,0})$, the cubic shadow
 14977	$\mathfrak{C}(\cA) = 0$ (Gaussian archetype: Heisenberg).
 14978	If $[o_3] \neq 0$, define
 14979	$\Theta_{\cA}^{\leq 3} = \Theta_{\cA}^{\leq 2}
 succeeded in 52ms:
 31100	quartic resonance class
 31101	$($Theorem~\textup{\ref{thm:nms-clutching-law-modular-resonance}}$)$
 31102	and the non-separating clutching law
 31103	$($Theorem~\textup{\ref{thm:nms-nonseparating-clutching-law}}$)$:
 31104	the algebraic clutching identities ARE the degeneration formula
 31105	applied to the bar complex on the relative log-FM spaces of the
 31106	universal family.
 31107	
 31108	More explicitly: in the finite-order shadow obstruction tower, the extension
 31109	$\Theta_\cA^{\leq r} \to \Theta_\cA^{\leq r+1}$ is governed by an
 31110	obstruction class $o_{r+1}(\cA) \in H^2(F^{r+1}/F^{r+2})$. For a
 31111	separating degeneration $\cA = \cA_1 \cup_\xi \cA_2$, the
 31112	obstruction classes satisfy a multiplicative relation
 31113	$\xi^* o_{r+1}(\cA) = o_{r+1}(\cA_1) \otimes 1 + 1 \otimes
 31114	o_{r+1}(\cA_2) + \text{tree correction}$,
 31115	where the tree correction comes from the birational modification
 31116	relating the product of log-FM factors to the actual special-fibre
 31117	component (Mok~\cite[Theorem~5.3.4]{Mok25}).
 31118	For non-separating degenerations, an additional term
 31119	$\hbar\Delta(\Theta_\cA^{\leq r})$ appears: this is the
codex
I’m checking the obstruction logic now. One summary block appears to reverse the usual vanishing criterion: it treats a nonzero `o_3` as the condition for defining `\Theta^{\le 3}`, even though the later recursive theorem says all obstruction classes vanish because the global MC element already exists. If that survives context, it’s a real mathematical inversion, not just bad wording.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14940,15020p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 14940	In both cases the recursion terminates at each finite weight.
 14941	Convergence of the full tower is guaranteed by the bar-intrinsic
 14942	element \textup{(}Theorem~\textup{\ref{thm:recursive-existence})}.
 14943	
 14944	MC2 is therefore \emph{proved in full generality} at the level of
 14945	existence by the bar-intrinsic construction. What remains open is
 14946	the stronger scalar-lane universality problem: for arbitrary
 14947	multi-weight one-channel families, must
 14948	$\Gamma_\cA = \kappa(\cA)\Lambda$?
 14949	\end{remark}
 14950	
 14951	\begin{construction}[Tower construction: the step-by-step template]
 14952	\label{constr:tower-template}
 14953	\index{shadow obstruction tower!construction template}
 14954	\index{tower construction template|textbf}
 14955	The following algorithm instantiates the obstruction recursion
 14956	(Construction~\ref{constr:obstruction-recursion}) for a concrete
 14957	chiral algebra. Each example chapter in Part~\ref{part:physics-bridges} follows this
 14958	template.
 14959	
exec
/bin/zsh -lc "rg -n -F 'If [o_3] = 0' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'all obstruction classes in the extension tower' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:


thinking
**Evaluating search methods**

I’m thinking about searching an exact phrase, possibly in lowercase. The algorithm seems to have some issues, so I need to compare it with the construction obstruction-recursion to better understand the intended logic. I’ll also look into the numbers around 12976 and 15190 to gather more context. It’s all about piecing together the puzzle! Let’s confirm the approach and refine the plan from there.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12970,13036p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 12970	shadow $\operatorname{Sh}_4$ is the first place where
 12971	the specific representation theory of~$\fg$ enters.
 12972	\end{remark}
 12973	
 12974	\begin{construction}[Obstruction recursion]
 12975	\label{constr:obstruction-recursion}
 12976	Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
 12977	constructed through weight $N$. Its next obstruction is
 12978	\begin{equation}
 12979	\label{eq:next-obstruction}
 12980	\mathfrak{o}_{N+1}
 12981	:=
 12982	\Bigl(
 12983	D_{\cA}\Theta_{\cA}^{\leq N}
 12984	+ \tfrac12[\Theta_{\cA}^{\leq N},
 12985	\Theta_{\cA}^{\leq N}]
 12986	\Bigr)_{N+1}.
 12987	\end{equation}
 12988	If $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanishes,
 12989	choose a contracting homotopy $h$ and define
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15184,15210p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 15184	$A_\infty$-operation $m_r^{\mathrm{tr}}$ on the minimal model.
 15185	The shadow obstruction tower is the formality obstruction tower.
 15186	
 15187	\begin{lemma}[Graph-sum truncation criterion]
 15188	\label{lem:graph-sum-truncation}
 15189	\ClaimStatusProvedHere
 15190	\index{graph-sum truncation|textbf}
 15191	\index{shadow obstruction tower!truncation mechanism}
 15192	Let $\cA$ be a modular Koszul chiral algebra.
 15193	The obstruction class at degree $r{+}1$ decomposes as
 15194	\begin{equation}
 15195	\label{eq:truncation-obstruction}
 15196	o_{r+1}(\cA)
 15197	\;=\;
 15198	\underbrace{\bigl[\Theta_\cA^{\leq r},\,
 15199	\Theta_\cA^{\leq r}\bigr]_{r+1}}_{\text{bracket term}}
 15200	\;+\;
 15201	\underbrace{\hbar\,\Lambda_P\!\bigl(\Theta_\cA^{\leq r}
 15202	\bigr)_{r+1}}_{\text{genus-loop term}},
 15203	\end{equation}
exec
/bin/zsh -lc "rg -n -i 'averag|coinvariant|Sigma_n|ordered.*lift|ordered.*mc|E_1-framed|ordered.*convolution|coinvariant/symmetric|symmetric/coinvariant' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3818,3836p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3597:ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
3654:\prod_{g,n} \mathrm{Hom}_{\Sigma_n}(C_*(\overline{\mathcal{M}}_{g,n}),
3798:coinvariant modular convolution algebra.
3801:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
3826:argument. The universal MC element on the coinvariant modular
3831:\index{MC2!coinvariant scope}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3835:The ordered lift
3838:Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
3968:\item \emph{$\Theta_\cA$ lies in the completed coinvariant algebra.}
4235:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
10177:\operatorname{Hom}_{\Sigma_n}\!\bigl(
10378:\operatorname{End}_{\cA}(n)$ is $\Sigma_n$-equivariant.
14838:\begin{remark}[The five theorems as coinvariant shadows of the $E_1$ theory]
14841:Each row of the table above is the $\Sigma_n$-coinvariant
14844:Theorem~A is the averaged form of the $E_1$ bar-cobar
14846:Theorem~B is the averaged form of the $E_1$~Quillen equivalence;
14847:Theorem~C is the averaged form of complementarity in the ordered
14854:and higher Yangian coherences that averaging discards
 succeeded in 52ms:
  3818	 and non-separating degenerations give
  3819	 $\xi_{\mathrm{ns}}^*(\Theta^{(g+1)})
  3820	 = \Delta_{\mathrm{ns}}(\Theta^{(g)})$.
  3821	\item \emph{Verdier duality.}
  3822	 $\mathbb{D}(\Theta_\cA) = \Theta_{\cA^!}$.
  3823	\end{enumerate}
  3824	This construction requires no restriction to simple Lie symmetry,
  3825	no one-channel hypothesis, and no tautological-line support
  3826	argument. The universal MC element on the coinvariant modular
  3827	convolution algebra is therefore proved in full generality.
  3828	\end{theorem}
  3829	
  3830	\begin{remark}[Scope of MC2 in this chapter]
  3831	\index{MC2!coinvariant scope}
  3832	Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
  3833	statement: its target dg~Lie algebra is
  3834	$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
  3835	The ordered lift
  3836	$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3830,3845p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3830	\begin{remark}[Scope of MC2 in this chapter]
  3831	\index{MC2!coinvariant scope}
  3832	Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
  3833	statement: its target dg~Lie algebra is
  3834	$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
  3835	The ordered lift
  3836	$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
  3837	\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
  3838	Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
  3839	$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
  3840	Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
  3841	therefore incorrect; the ordered theorem is
  3842	Theorem~\ref{thm:e1-mc-element}.
  3843	\end{remark}
  3844	
  3845	% ----------------------------------------------------------------

thinking
**Considering MC equation definition**

The user is asking if the MC equation appears as a definition before being used in proofs. They note that it may not be defined in a formal environment, which suggests a somewhat weaker issue than complete absence. I’m thinking that there’s still no dedicated definition or proposition, just some informal writing. I might need to check if Theorem 3564 refers to "See Theorem mc2 bar intrinsic for full construction," indicating that the formal theorem is presented later.
codex
A more serious defect showed up in the opening taxonomy itself. The file says class `L` occurs when `\kappa=0` at lines 134–138, but later the same chapter identifies generic affine Kac–Moody as class `L`, and its own formula census says generic affine `\kappa` is not zero. I’m pinning down the later internal characterization so the fix is exact rather than speculative.
exec
/bin/zsh -lc "rg -n -F 'S_3 = 0' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'single-line-dichotomy' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'o_3(\\cA) \\neq 0 and o_4(\\cA) = 0' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17440,17540p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
132: (Theorem~\ref{thm:single-line-dichotomy}):
16155:(Theorem~\ref{thm:single-line-dichotomy}):
16332:(Theorem~\ref{thm:single-line-dichotomy}). Hence
16518:(Theorem~\ref{thm:single-line-dichotomy}).
18471:\label{thm:single-line-dichotomy}
19192: \textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)}.
19209:and Theorem~\ref{thm:single-line-dichotomy}.
19989:Theorem~\ref{thm:single-line-dichotomy} gives
20006:so Theorem~\ref{thm:single-line-dichotomy} gives a perfect square
31833:\textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)},
34891:Theorem~\ref{thm:single-line-dichotomy} in the fixed family-level
34933:Theorem~\ref{thm:single-line-dichotomy},
34968:(Theorem~\ref{thm:single-line-dichotomy}) describes the
34987:Theorem~\ref{thm:single-line-dichotomy} is the equation of the
 succeeded in 51ms:
3531:$\cW_3$ $\mathbb{Z}_2$-parity ($S_3 = 0$ kills
15037: & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
15055:family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
15100:$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
16834: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
16881:  S_3 = 0,\qquad
17606:  S_3 = 0,\qquad
17767:so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
25515: For $S_3 = 0$ \textup{(}Heisenberg\textup{)}:
25551:For $S_3 = 0$: all planted-forest vertex weights vanish
26313:For class~$\mathsf{G}$ $($Heisenberg$)$: $S_3 = 0$, so
31817:$S_3 = 0$ \textup{(}equivalently, iff the cubic shadow
31822:Classes~$G$ and~$C$ have $S_3 = 0$ \textup{(}$\beta\gamma$
31877:\item $S_3 = 0$ (classes~$G$ and~$C$):
31883:$\mathfrak{Q} \neq 0$ but $S_3 = 0$
31969:vanishes for class~G (where $S_3 = 0$) and
31975:(the $T$-line contribution; the $W$-line has $S_3 = 0$ and contributes
 exited 1 in 50ms:

 succeeded in 51ms:
 17440	\label{thm:shadow-metric-existence}
 17441	\ClaimStatusProvedHere
 17442	\index{shadow generating function!algebraicity|textbf}
 17443	\index{Riccati algebraicity|textbf}
 17444	Let $L$, $S_r$, $Q_L$ be as in
 17445	Definition~\textup{\ref{def:shadow-metric}}.
 17446	Set $P = 1/\kappa$ and define the weighted shadow
 17447	generating function
 17448	$H(t) := \sum_{r \geq 2} r\,S_r\,t^r$.
 17449	The all-degree master equation
 17450	$\nabla_H(\mathrm{Sh}_r) + \mathfrak{o}^{(r)} = 0$
 17451	\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc})}
 17452	on~$L$ is equivalent to the algebraic relation
 17453	\begin{equation}\label{eq:riccati-algebraic-relation}
 17454	 H(t)^2
 17455	 \;=\;
 17456	 t^4\,Q_L(t),
 17457	\end{equation}
 17458	so that
 17459	\begin{equation}\label{eq:shadow-gf-closed-form}

thinking
**Inspecting the theorem**

I need to take a close look at the single-line dichotomy related to the theorem around 18471. There's a lot to unpack here! I wonder what specific aspects I should focus on, and I want to ensure I'm grasping the core elements correctly. Am I going to find any interesting insights or challenges in this theorem? Let’s dive into the details and see what I can discover about it!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18460,18540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17576,17618p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 18460	and $t_0$ is the nearest complex zero of~$Q_L$.
 18461	The alternation arises from the binomial expansion of
 18462	$\sqrt{Q_L}$ around the Gaussian envelope; it breaks when
 18463	$\cos(r \cdot \arg(t_0))$ changes sign.
 18464	For $\mathrm{Vir}_{13}$: $r_* = 27$;
 18465	for $c = 1$: $r_* = 17$.
 18466	As $c \to \infty$: $\arg(t_0) \to \pi$ and
 18467	$r_* \to \infty$ (exact alternation in the semiclassical limit).
 18468	\end{remark}
 18469	
 18470	\begin{theorem}[Single-line dichotomy; \ClaimStatusProvedHere]
 18471	\label{thm:single-line-dichotomy}
 18472	\index{single-line dichotomy|textbf}
 18473	\index{shadow obstruction tower!single-line dichotomy}
 18474	\index{shadow depth!pump mechanism}
 18475	Let $L$, $S_r$, $\alpha$, $\Delta$, $Q_L$ be as above.
 18476	Then $r_{\max}|_L \in \{2,\,3,\,\infty\}$, classified by the
 18477	shadow metric:
 18478	\begin{enumerate}[label=\textup{(\roman*)}]
 18479	\item \emph{$\Delta = 0$, $\alpha = 0$
 succeeded in 51ms:
 17576	does, $\sqrt{Q_L}$ is linear and the tower terminates after
 17577	finitely many terms; when it does not, $\sqrt{Q_L}$ is
 17578	irrational over the polynomial ring and the binomial series for
 17579	$(1+u)^{1/2}$ produces infinitely many nonzero shadow
 17580	coefficients. There is no third possibility. The depth of the
 17581	shadow tower is not a free parameter: it is \emph{read off} from
 17582	the arithmetic of a single quadratic, and the only outcomes are
 17583	termination or infinite extent.
 17584	
 17585	\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
 17586	\label{prop:depth-gap-trichotomy}
 17587	\ClaimStatusProvedHere
 17588	\index{algebraic depth!gap theorem|textbf}
 17589	\index{shadow depth!forbidden values}
 17590	\index{depth classification!algebraic depth gap}
 17591	Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 17592	Then the algebraic depth satisfies
 17593	\begin{equation}\label{eq:depth-gap}
 17594	 d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
 17595	\end{equation}
codex
The opening taxonomy has a second flaw beyond the wrong `\kappa=0` criterion: it attributes class `C` to the “single-line dichotomy,” but the actual theorem at lines 18470–18495 only classifies `G/L/M` on a primary line. I’m locating the later `\beta\gamma` theorem so the fix can separate line-level and global classification cleanly.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:betagamma-global-depth}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17680,17720p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
 17680	 S_6
 17681	 \;=\;
 17682	 -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
 17683	 \;=\;
 17684	 -\frac{2\,S_4^2}{3\kappa},
 17685	\]
 17686	which is again nonzero. Thus there is no second finite
 17687	cancellation beyond the affine one: away from $S_4 = 0$ the
 17688	single-line tower does not terminate. By induction,
 17689	$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
 17690	$H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.
 17691	
 17692	\emph{Global contact witness.}
 17693	The value $d_{\mathrm{alg}} = 2$ is realized by the
 17694	conformal-weight family $\beta\gamma_\lambda$, not by either of its
 17695	one-dimensional internal slices. On the weight-changing line,
 17696	all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 17697	rigidity
 17698	\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 17699	On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}

thinking
**Searching for labels**

I'm thinking I need to find an actual label, possibly in the appendix. Searching more broadly seems like a good idea. It might help me locate what I'm looking for more easily. I feel like exploring different sources could yield better results. Let's see if expanding my search parameters will provide more relevant information! I'm eager to get this right and find what I need.
exec
/bin/zsh -lc "rg -n -F 'betagamma-global-depth' chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:15106:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:16810: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
chapters/theory/higher_genus_modular_koszul.tex:16888: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:16953:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:17702:Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/ordered_associative_chiral_kd.tex:6571:Theorem~\textup{\ref*{thm:betagamma-global-depth}}\textup{)},
appendices/ordered_associative_chiral_kd.tex:2440:Theorem~\textup{\ref*{thm:betagamma-global-depth}}\textup{)},
chapters/examples/free_fields.tex:1165:Theorem~\ref{thm:betagamma-global-depth}.
chapters/examples/free_fields.tex:1181:\label{thm:betagamma-global-depth}
chapters/examples/free_fields.tex:5573:(Theorem~\ref{thm:betagamma-global-depth}):

thinking
**Checking weight filtration**

I need to inspect the definition of weight filtration and look at the specific lines from the document, which are 12168 to 12196. It seems like a crucial step in understanding the context. I want to ensure I’m clear on the concept and how it’s applied. I wonder if there’s anything I might be missing, so I’ll delve into those lines carefully. Alright, let’s see what details I can pull from them!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12168,12196p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12168	\label{def:weight-filtration-tower}
 12169	\index{weight filtration!definition|textbf}
 12170	Each component of the modular convolution algebra carries a
 12171	\emph{tridegree} $(g, r, d)$, where
 12172	$g \geq 0$ is the loop genus (genus label on the stable graph),
 12173	$r \geq 2$ is the degree (number of external half-edges), and
 12174	$d \geq 0$ is the planted-forest depth (codimension of the
 12175	log-FM boundary stratum in the sense of
 12176	Definition~\ref{def:vol1-rigid-planted-forest-depth-filtration}).
 12177	Define the \emph{total weight}
 12178	\[
 12179	w(g, r, d) \;:=\; 2g - 2 + r + d.
 12180	\]
 12181	The stability condition $2g - 2 + n > 0$ ensures $w \geq 1$.
 12182	The \emph{weight filtration} is the descending filtration
 12183	\[
 12184	F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
 12185	\;:=\;
 12186	\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
 12187	\;:\; \varphi_{g,r;d} = 0 \;\text{for all}\;


thinking
**Clarifying algebra definitions**

I need to clarify some details in the mathematical definitions. I should rewrite lines 12170-12176 to say, "Each component of the ambient modular complementarity algebra..." or potentially drop the "d" from convolution algebra and focus on defining weight based on genus and degree. There seem to be inconsistencies regarding filtering definitions across the algebra components. To fix these, I might need to state the object clearly and possibly define a weight filtration directly on \gAmod, taking into account the isomorphism with the ambient algebra.
thinking
**Adjusting mathematical references**

Since the file heavily uses the weight `w(g,r,d)`, I’m thinking I might need to modify line 12170 to say, "Each component of the ambient modular complementarity algebra carries tridegree..." and ensure that all subsequent uses of `\gAmod` are in reference to the ambient context. However, I’m noticing that the intrinsic MC2 theorem and other sections still mention Theta in `\gAmod`, so I’ll have to find a way to reconcile these references to maintain consistency.
codex
To avoid inventing an ordered formula from memory, I’m reading the actual `E_1` chapter now. If I cite an exact fix for the missing `\mathfrak g^{E_1}` definition, it needs to match the repository’s live ordered notation, not a generic guess.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:e1-mc-element}' -B 40 -A 40 chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}_{\\cA}"'^{E_1}'"' chapters/theory/e1_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
251-\operatorname{Hom}\!\bigl(
252-\cM_{\Ass}(g,n),\,
253-\operatorname{End}_{\cA}(n)
254-\bigr).
255-\end{equation}
256-The Hom carries no $\Sigma_n$-equivariance; this is the structural
257-distinction from $\gAmod =
258-\prod \operatorname{Hom}_{\Sigma_n}(\cM_\Com(g,n),
259-\operatorname{End}_\cA(n))$
260-(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
261-uses the symmetric cooperad $\mathrm{Sym}^c$ obtained from $T^c$ by external
262-$\Sigma_n$-coinvariants. The dg~Lie structure is inherited from
263-$F\!\Ass$: $D$ from $D_{F\!\Ass}$, $[-,-]$ from ribbon-graph
264-composition.
265-The \emph{averaging map}
266-\begin{equation}
267-\label{eq:e1-to-einfty-projection}
268-\operatorname{av}\colon
269-{\gAmod}^{E_1}
270-\;\twoheadrightarrow\;
 succeeded in 50ms:

exec
/bin/zsh -lc "rg -n -i 'coinvariant|averag|Sigma_n' chapters/theory/e1_modular_koszul.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
13:$\Sigma_2$-coinvariant of a meromorphic function $r(z)$ that records
15:$\mathfrak{C}(\cA)$ is the $\Sigma_3$-coinvariant of the Drinfeld
18:strictly more information, and the data killed by the coinvariant
25:augmentation ideal, before any symmetric-group averaging has been
26:performed. Its $\Sigma_n$-coinvariant shadow
27:$\Barch(\cA) = {\Barch}^{\mathrm{ord}}(\cA)_{\Sigma_n}$
29:irreversible. The averaging map
106:$\Sigma_n$-quotient
108:\overline{\cM}_{g,n}^{\,\mathrm{rib}}/\Sigma_n$;
124:merely the symmetric group $\Sigma_n$. Over a point, the
126:$\{1, \ldots, n\}$ with its $\Sigma_n$-action: there is
135:$\BarSig(\cA) = \Barord(\cA)_{\Sigma_n}$ via
136:the averaging map $\mathrm{av}$ is a $\Sigma_n$-coinvariant
194:\label{thm:fcom-coinvariant-fass}
202:\;\xrightarrow{\;\pi_{\Sigma_n}\;}
207:underlying stable graph and $\pi_{\Sigma_n}$ is the coinvariant
220:Second, $\pi_{\Sigma_n}$ takes external $\Sigma_n$-coinvariants on
222:$\Sigma_n$ acts on the set of stable graphs by permuting leg labels
226:Only the external-label step is used by the averaging map
256:The Hom carries no $\Sigma_n$-equivariance; this is the structural

thinking
**Researching formulas**

I need to review the definitions between pages 245-288 to find the exact formula for ordered algebra and averaging. This seems important if I'm aiming to clarify or fix something. Checking these specific sections should help me identify the details I need. I want to make sure I'm accurate with the citation and that I understand the formulas fully. I'll dive into those pages and take notes!
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '236,288p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   236	\index{E1 algebra@$E_1$-algebra!modular convolution|textbf}
   237	\index{modular convolution dg Lie algebra!E1@$E_1$ (ordered)}
   238	Let $\cA$ be a cyclic $E_1$-chiral algebra
   239	(Definition~\ref{def:e1-chiral}).
   240	The degree-$n$ component of the ordered bar complex is the tensor
   241	coalgebra $T^c(s^{-1}\bar\cA)$ built on the augmentation ideal
   242	$\bar\cA = \ker(\varepsilon)$, with $n$ linearly ordered external
   243	legs and deconcatenation coproduct (distinct from the coshuffle
   244	coproduct of $\mathrm{Sym}^c$). The modular grading is supplied
   245	separately by $\cM_{\Ass}(g,n)$ above.
   246	\begin{equation}
   247	\label{eq:e1-modular-convolution}
   248	{\gAmod}^{E_1}
   249	\;:=\;
   250	\prod_{\substack{g,n \\ 2g-2+n > 0}}
   251	\operatorname{Hom}\!\bigl(
   252	\cM_{\Ass}(g,n),\,
   253	\operatorname{End}_{\cA}(n)
   254	\bigr).
   255	\end{equation}




thinking
**Gathering audit findings**

I need to search for issues related to lines 22229 or 2348 and create a summary table. It seems important to show whether a theorem is applicable, but I shouldn’t overwhelm with too many findings—instead, I aim for about 8-12 distinct issues. The format requires exact file:line references, and I can only cite each file once per finding. If an issue spans multiple lines, I should reference the primary line and note surrounding lines in the problem text.
thinking
**Determining line references**

I should consider using the first line for citation and mention the range "at 12230-12245" in the text. It seems acceptable to have one line number after the file reference, but I want to ensure I follow the user's request for exact line citations. Instead of using a range, I might stick with the first line mentioned and include other relevant lines inline. If needed, I can have multiple findings in the same file but reference different lines.
thinking
**Identifying critical fixes**

I need to make my fixes as concrete as possible. First, I'll enumerate the likely findings. 

For instance, there's something critical regarding 12214 or 12230 — the shadow tower carrier object flip. It seems to be defined in an ambient algebra quotient, but I have noticed that there's a theorem, proof, or figure that calls for a tower in the context of \gAmod. I really want to get this right!
thinking
**Identifying references and plans**

I'm considering a few things. First, there's the issue of font inconsistency with \mathsf vs. \mathbf, but I might skip that unless needed. I've been asked to find every missing definition, unresolved reference, or unjustified step, which seems like a lot! For instance, while verifying references, I noticed `Theorem\ref{thm:betagamma-global-depth}` is in another file and thus not unresolved. Additionally, I might look into the `\gAmod` macro, but it seems unnecessary for now. I should possibly update my plan as I gather more context.
Plan update
Mapped the target chapter’s definition/use graph and checked the ordered chapter for the missing E1 conventions. The remaining step is to consolidate the verified object-level inconsistencies into a final audit with exact fixes.
  ✓ Read governing instructions and audit skill workflow
  ✓ Read target chapter and map definitions/usages with line numbers
  ✓ Cross-check whether required objects are defined locally or hidden-imported
  → Re-verify findings and produce exact-fix audit report
codex
I need one more dependency read for the class-`C` fix. The opening summary should point to the actual `\beta\gamma` theorem, so I’m loading the statement instead of citing the label blind.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '1170,1208p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1170	rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
  1171	transferred higher brackets $\ell_n^{\mathrm{tr}}|_L = 0$ for
  1172	$n \geq 2$. The shadow obstruction tower is therefore purely quadratic, and since
  1173	$\kappa|_{\mathrm{wc}} = 0$ (the weight-changing deformation does not
  1174	produce genus-$0$ curvature), the entire tower
  1175	vanishes.\qedhere
  1176	\end{proof}
  1177	
  1178	\subsubsection{Stratum separation and the quintic vanishing}
  1179	
  1180	\begin{theorem}[$\beta\gamma$ global shadow depth; \ClaimStatusProvedHere]
  1181	\label{thm:betagamma-global-depth}
  1182	\index{stratum separation!beta-gamma@$\beta\gamma$}
  1183	\index{beta-gamma system@$\beta\gamma$ system!shadow depth}
  1184	On the full two-channel deformation space, the $\beta\gamma$ system has
  1185	global shadow depth $r_{\max} = 4$
  1186	\textup{(}class~C, the contact/quartic archetype\textup{)}.
  1187	The depth-$4$ witness is the quartic contact class on the mixed charged
  1188	stratum coupling the T-line to the weight-changing direction; neither
  1189	one-dimensional slice realizes class~C by itself.
codex
There is one more foundation-level leak: several flagship formulas write `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` with a free genus variable `g`. I’m checking whether the file ever defines that shorthand as the full stable-pair product; if it does not, that is another load-bearing scope bug.
exec
/bin/zsh -lc "rg -n -F '\\overline{\\mathcal{M}}_{\\bullet,\\bullet}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'R\\Gamma(\\overline{\\mathcal{M}}_{g,\\bullet},' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 52ms:
2664: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
2774: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
3581: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
5522:$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
8087: R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$
8108: R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})
exec
/bin/zsh -lc "rg -n -F 'R\\Gamma(\\overline{\\mathcal{M}}_{g,\\bullet},' chapters/theory/e1_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/algebraic_foundations.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5508,5534p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5508	Proposition~\ref{prop:cyclic-ce-identification} gives
  5509	$H^2_{\mathrm{cyc}}(\mathfrak{g}, \mathfrak{g}) \cong
  5510	H^3(\mathfrak{g}) \cong \mathbb{C}$ with generator the
  5511	Killing $3$-cocycle.
  5512	\end{proof}
  5513	
  5514	\begin{proposition}[MC2 reduction principle;
  5515	\ClaimStatusProvedHere]\label{prop:mc2-reduction-principle}
  5516	\index{MC2!reduction principle}
  5517	Let $\cA$ be a modular Koszul chiral algebra. Assume that the
  5518	bar-intrinsic complex $\Defcyc(\cA)$ of
  5519	Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
  5520	$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
  5521	coefficient spaces chosen from
  5522	$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
  5523	modular-operadic package of
  5524	Theorem~\ref{thm:universal-theta}. Then:
  5525	\begin{enumerate}[label=\textup{(\roman*)}]
  5526	\item the universal Maurer--Cartan problem for $\Theta_{\cA}$ is posed
  5527	 on the genus-completed convolution algebra










thinking
**Evaluating definitions and fixes**

I see we have specific fixes for gAmod and class definitions. It might be a good idea to avoid saying "separate," since moving definitions can address the problem. The user asked if things are defined before use, and the answer is no. I’m considering that we still need to include this info because not all issues are caught by later line-specific mentions. However, I think findings 8 and 9 might be enough without keeping things too lengthy.
thinking
**Clarifying algebra definitions**

The user is asking about the definition of convolution algebra, specifically regarding g^{E1} and g^{mod}. I realize I need to focus on both, but especially g^{mod}, to provide a clear answer. It seems important to dig deeper into the definitions to ensure I completely address the user's question. I want to make sure I'm getting this right and giving the user the information they need. So, let's look into both concepts carefully!
thinking
**Clarifying notation**

I’m checking if `\cA^{sh}_{2,0}` denotes a scalar rather than a vector space. The definition states that `\cA^{sh} = \bigoplus \cA^{sh}_{r,g}`, indicating that each part is a vector space. So, it seems I’m right in saying that equality with a scalar is invalid. That's a good confirmation! It's always nice to be precise with mathematical definitions.
thinking
**Evaluating theorem proof structure**

I'm looking at the proof of the Theorem universal-theta, which uses the Maurer-Cartan equation as if it's a well-established definition. However, it doesn't formally define it before use, which feels too loose for a foundational chapter. I should suggest moving that section into a numbered definition right before the relevant theorem, labeled as `def:bar-intrinsic-mc-equation`, and explicitly stating the equation. 

For the 7 tower template, there's an issue where the logic reverses the obstruction recursion. It presents that `[o_3]=0` implies `\mathfrak C=0`, contradicting an earlier construction.
thinking
**Fixing theorem steps**

I need to rewrite Steps 2 and 3 to align with Construction 12974. Specifically, it should state: “If `[o_3]=0` in `H^2(F^3/F^4)`, then choose `\mathfrak C=-h(o_3)` and set `\Theta^{\le3}=\Theta^{\le2}+\mathfrak C`. In the Gaussian case, it’s permissible to choose `\mathfrak C=0` since the cocycle itself vanishes.” I should apply the same revision for `o_4`.

Now, about the shadow algebra component type: there’s a problem where the definition incorrectly matches invariants with complete graded pieces, like `\kappa(\cA)=\cA^{sh}_{2,0}`. The left-hand side involves scalars or classes, while the right side presents vector spaces. But the correct projection language is found later in the chapter.
thinking
**Summarizing definitions and findings**

I’m considering how to structure my response, possibly with nine concise bullets plus a summary. The user has specific questions: Is the shadow tower formally defined? Are the classes and equations outlined before their use? 

Based on my findings:  
- The shadow tower is defined but inconsistently.  
- The classes are not defined before use, which is incorrect.  
- The MC equation isn't stated as a definition prior to proof.  
- \( g^{E1} \) is not locally defined, while \( g^{mod} \) is only defined later.  

Good—omitting the earlier, generic use might streamline the response!
thinking
**Considering scope details**

I'm identifying a scope bug since the user asked about exact scope. It seems this wasn't included in the initial checklist. I should inspect specific lines for clarity. I can condense down to about 9 concise bullet points plus a brief summary, targeting around 12-15 lines altogether. Each bullet will likely take up two lines, still keeping it within a reasonable length. I need to ensure references point to the correct file and mention any issues in my conclusion as needed.
thinking
**Finalizing fix text**

I need to mention lines 246-287 in the fix text. Also, including line 16579 is important since it identifies the ranks, with examples showing classes by d_alg. I’ll create a bullet list without nesting and finish with a summary header. To maintain clarity, I should count the checked surfaces—it's 10 findings with a verdict of FAIL. I’ll order severity as CRITICAL first, followed by HIGH and MEDIUM, while including precise file line references for each bullet point.
thinking
**Evaluating relevance of issues**

I think the degree-2 truncation issue is more important, so I'll use 12250 since it connects directly to the shadow tower formal definition. It makes sense to focus on that and skip mentioning free g, especially since the user specifically inquired about shadow towers. However, I need to remember that the exact scope of `RΓ(\overline M_{g,\bullet})` is also foundational. With our current findings totaling 8, I must be concise yet thorough.
thinking
**Consolidating findings**

I need to summarize my findings, aiming for about 8 to keep it concise. I'm wondering if including the free-g variable is necessary; it's not crucial but could add depth due to its role in the universal theta definition. However, since this is a targeted mission, I think I should stick to those high-signal findings without overwhelming the user. I should also note that my final summary is "Checked: 10 | Findings: 8 | Verdict: FAIL." I’ll proceed carefully with the final output.
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:12206 — PROBLEM: the extension tower and shadow tower are defined in `\mathfrak{g}^{\mathrm{amb}}_\cA/F^{r+1}`, but the same file later puts the same tower in `\gAmod/F^{r+1}` and proves convergence in `\widehat{\gAmod}` at 12425, 13010, and 14743. The carrier object of the foundation is unstable. FIX: make `\mathfrak{g}^{\mathrm{mod}}_\cA` the unique foundational carrier: replace `\mathfrak{g}^{\mathrm{amb}}_\cA` by `\mathfrak{g}^{\mathrm{mod}}_\cA` in 12206 and 12232, redefine the filtration on `\gAmod`, and keep `\mathfrak{g}^{\mathrm{amb}}_\cA` only as a later graph-sum model after an explicit comparison theorem.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:12245 — PROBLEM: `o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})` is cohomology-of-cohomology, because `\cA^{\mathrm{sh}}` is later defined as `H_\bullet(...)` at 12467. The same file uses `H^2(F^{r+1}\gAmod/F^{r+2}\gAmod)` instead at 13010 and 31110. FIX: change 53, 100, 12238-12245, and 14976 to `H^2(F^{r+1}\gAmod/F^{r+2}\gAmod)`; if a shadow-algebra image is wanted, define a separate projection map after 12467 instead of writing `H^2(\cA^{\mathrm{sh}}_{r+1,0})`.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:126 — PROBLEM: the opening classification is wrong and overclaims its source. It says class `L` is the `\kappa=0` case and folds class `C` into `Theorem~\ref{thm:single-line-dichotomy}`, but the actual theorem at 18470 only gives `G/L/M` on a primary line via `(Δ=0,\alpha=0)`, `(Δ=0,\alpha\neq0)`, `Δ\neq0`; class `C` is later supplied globally by `\beta\gamma` in [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1180). FIX: replace 126-146 by a faithful split: primary-line `G/L/M` from `(\Delta,\alpha)` as in 18479-18495, then a separate sentence that class `C` is global and comes from `\beta\gamma` via `thm:betagamma-global-depth`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:16535 — PROBLEM: `Definition~\ref{def:shadow-depth-classification}` identifies the class with total depth `r_{\max}`, but Example 16775 later labels `V_{\mathrm{Leech}}`, rank-48, and rank-72 as class `G` with depths `4,5,6`. The file silently switches from total depth to algebraic depth. FIX: split the notions. Define total depth `d(\cA):=r_{\max}(\cA)` separately, and define the four classes by `d_{\mathrm{alg}}`: `\mathbf G/\mathbf L/\mathbf C/\mathbf M = 0/1/2/\infty`. Then state that `r_{\max}=2,3,4,\infty` only for the primitive archetypes.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:39 — PROBLEM: the first page uses `\gAmod`, and line 180 uses `\Theta_\cA^{E_1}`, before this chapter defines either `\mathfrak g^{\mathrm{mod}}_\cA` or the ordered algebra/averaging map. `\gAmod` only appears formally at 10159; `(\gAmod)^{E_1}` and `\operatorname{av}` are only defined in [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:246). FIX: insert a local foundational convention immediately after line 43: define `\gAmod` by the formula of 10168-10179, import the ordered formula and averaging map from `e1_modular_koszul.tex:246-287`, and only then use `\Theta_\cA^{E_1}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3595 — PROBLEM: the proof of `thm:universal-theta` relies on “the Maurer--Cartan equation” as established infrastructure, but the chapter never promotes that equation to a formal definition/convention before proof use; it appears only as running prose at 37-43. FIX: move 36-43 into a numbered definition or convention placed before the first theorem that uses it, label it, and state explicitly that the strict chapter-level equation is `[\dzero,\Theta_\cA]+\tfrac12[\Theta_\cA,\Theta_\cA]=0` in `\gAmod`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:14975 — PROBLEM: the “tower construction” template reverses the obstruction logic. It says `[o_3]=0` gives `\mathfrak C(\cA)=0`, while `[o_3]\neq0` is where one defines the next correction. That contradicts the actual recursion at 12974-12994, where vanishing of the obstruction class is the condition for choosing the next lift. FIX: rewrite Steps 2 and 3 to match 12988-12993: “If `[o_{N+1}]=0`, choose `-h(o_{N+1})` and adjoin it as the next correction; in the Gaussian/contact special cases that correction may itself vanish.”

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:12512 — PROBLEM: the shadow algebra definition equates invariants with whole graded pieces: `\kappa(\cA)=\cA^{\mathrm{sh}}_{2,0}`, `\Delta_\cA=\cA^{\mathrm{sh}}_{2,*}`, etc. Those are type errors, and they also collapse the full degree-2 truncation to the scalar `\kappa` alone, contradicting the later spectral projection at 4289-4297. FIX: replace 12250, 12365, 12512-12515, and 14968 by projection/membership statements: `\mathfrak C(\cA)\in\cA^{\mathrm{sh}}_{3,0}`, `\mathfrak Q(\cA)\in\cA^{\mathrm{sh}}_{4,0}`, `\operatorname{Sh}_r(\cA)\in\cA^{\mathrm{sh}}_{r,\bullet}`, and describe `\kappa(\cA)` as the scalar trace of the quadratic shadow while the non-scalar quadratic shadow is `T_{\mathrm{br},\cA}` with `\Delta_\cA(x)=\det(1-xT_{\mathrm{br},\cA})`.

## Summary
Checked: 10 | Findings: 8 | Verdict: FAIL
tokens used
209,336
