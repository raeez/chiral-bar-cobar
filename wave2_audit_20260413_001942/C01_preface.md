# C01_preface (546s)

- [CRITICAL] chapters/frame/preface.tex:833 — PROBLEM: `\Bbbk` is used on the live book surface before any definition appears in the main build, so this is an undefined-control-sequence risk, not a stylistic quirk. FIX: change `When $X=\operatorname{Spec}\Bbbk$ is a point` to `When $X=\operatorname{Spec}\mathbb{k}$ is a point`, or add `\providecommand{\Bbbk}{\mathbb{k}}` to the local macro block at lines 1–16.

- [HIGH] chapters/frame/preface.tex:25 — PROBLEM: the preface opening is descriptive instead of deficiency-first; it starts with “This monograph studies…” rather than the failure the book repairs. FIX: replace lines 25–27 with `Local OPE residue calculus sees one collision at a time; it does not organise singularities on $n$ points of a genus-$g$ curve into a global complex over moduli. This monograph resolves that defect by constructing bar and cobar chain complexes at the geometric levels relevant to chiral algebra on curves.` Then keep the existing operad list starting at `The geometry determines the operad:`.

- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`

- [HIGH] chapters/frame/preface.tex:101,1219,2120 — PROBLEM: Theorem~C drifts across three different objects: derived chiral centre, genus-$g$ cohomology of the center local system, and “the genus tower.” That is theorem-surface drift, not harmless rephrasing. FIX: keep lines 1219–1224 as the only theorem statement; rewrite lines 101–105 as `Theorem~C extracts this Lagrangian splitting from the derived chiral centre.`; rewrite lines 2120–2121 as `Under Theorem~C, the genus tower projects to these two Lagrangian summands.`

- [HIGH] chapters/frame/preface.tex:1198 — PROBLEM: the subsection `The five theorems` restates the full theorem list after the opening already did it, then lines 1257–1264 summarize the same list yet again. This is visible redundancy, not orientation. FIX: delete lines 1198–1264 and replace them with `Theorems~A--D and~H, stated in the body, are the five projections of the ordered bar used throughout the rest of this preface.`

- [HIGH] chapters/frame/preface.tex:2116 — PROBLEM: after the projection table at 2078–2108, lines 2116–2125 paraphrase the same mapping in prose. The table already does that work. FIX: delete lines 2116–2125 and replace them with `Table~5.1 records the five projections of $\Theta_\cA$ that organise the remainder of the preface.`

- [HIGH] chapters/frame/preface.tex:3731 — PROBLEM: `The open/closed world (Volume~II)` expands into a second preface inside the first; hundreds of lines of Volume II material swamp the Volume I close. FIX: replace lines 3731–4201 with `\noindent\textbf{Volume~II interface.} Volume~II studies the ordered data discarded by averaging: the spectral $R$-matrix, Yangian, open/closed extension, and the $\SCchtop$-governed derived-center pair. In this volume these appear only as outputs or conjectural extensions of the ordered bar; the three-dimensional holomorphic-topological constructions are deferred to Volume~II.`

- [HIGH] chapters/frame/preface.tex:4216 — PROBLEM: `The boxed machine` repeats the same summary function already performed by the projection table and earlier theorem summaries, then restates the box immediately in prose. FIX: keep the boxed display at 4218–4232; delete lines 4234–4267; replace them with `Everything in this preface is a projection of $\Theta_\cA$, with Theorems~A--D and~H extracting its scalar and low-degree shadows.`

- [MEDIUM] chapters/frame/preface.tex:32,573,700 — PROBLEM: macro use is inconsistent inside a single file. You mix raw `\mathrm{SC}^{\mathrm{ch,top}}` with `\SCchtop`, raw `\mathcal H_k` with `\cH_k`, and raw `\mathfrak g` with `\fg`. FIX: line 32 use `$\SCchtop$`; replace every listed `\mathcal H_k`/`\mathcal H_{-k}` occurrence with `\cH_k`/`\cH_{-k}`; replace every listed `\mathfrak g`/`\widehat{\mathfrak g}_k` occurrence with `\fg`/`\widehat{\fg}_k`.

- [MEDIUM] chapters/frame/preface.tex:1008,1020 — PROBLEM: the curvature formula drops from `\kappa(\cA)` to bare `\kappa` exactly where the symbol is used in equations. FIX: line 1008 `the fibrewise curvature $\kappa(\cA)\cdot\omega_g$`; line 1020 `\kappa(\cA)\cdot\omega_g-\kappa(\cA)\cdot\omega_g+0`.

- [MEDIUM] chapters/frame/preface.tex:1097,1101,1103 — PROBLEM: the discriminant paragraph repeats the same notation drift: bare `\kappa` and bare `S_4` in a generic formula. FIX: write `\Delta(\cA)=8\,\kappa(\cA)\,S_4(\cA)`, `\kappa(\cA)\cdot\lambda_g`, and `(\kappa(\cA),\alpha(\cA),S_4(\cA))`.

- [MEDIUM] chapters/frame/preface.tex:2511,2514,2517,2675 — PROBLEM: the algebraicity section uses bare `\kappa` even though the object is a primary line `L`; the notation should be line-indexed there. FIX: introduce `\kappa_L:=\kappa(\cA_L)`, `\alpha_L:=\alpha(\cA_L)`, `S_{4,L}:=S_4(\cA_L)`, then rewrite `Q_L(t)=4\kappa_L^2+12\kappa_L\alpha_L\,t+(9\alpha_L^2+16\kappa_LS_{4,L})t^2`, `(\kappa_L,\alpha_L,S_{4,L})`, `\Delta_L=8\kappa_LS_{4,L}`, and `\rho(\cA)=\sqrt{9\alpha_L^2+2\Delta_L}/(2|\kappa_L|)`.

- [MEDIUM] chapters/frame/preface.tex:2854,2968,3128,3135,3319,3478,4264 — PROBLEM: later sections never stabilize the modular-characteristic notation; the file keeps oscillating between explicit family notation and bare `\kappa`. FIX: use `\kappa(\cA)` in generic formulas, and family-tagged forms in family passages: `\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g`, `F_g(\beta\gamma_\lambda)=\kappa(\beta\gamma_\lambda)\cdot\lambda_g^{\mathrm{FP}}`, `\kappa(\cA)+\kappa(\cA^!)`, `\Theta_\cA^{\min}=\kappa(\cA)\cdot\eta\otimes\Lambda`, `d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_1`, and `the scalar projection~$\kappa(\cA)$`.

- [MEDIUM] chapters/frame/preface.tex:2168,2335,2414,2856,3158,3197,3292,3324,3467,3934 — PROBLEM: these transitions are pure signpost rhetoric (`The question is...`, `The answer is...`) instead of mathematically forced transitions. FIX: replace them with direct statements: 2168 `These projections are the characteristic classes of the modular bar bundle.`; 2335 `These projections assemble into a CohFT once the MC equation is pushed to $\overline{\cM}_{g,n+1}$.`; 2414 `The output is independent of the retraction data up to MC gauge equivalence.`; 2856 `Multiple conformal weights are precisely where the scalar formula can fail.`; 3158 `These rational numbers acquire arithmetic meaning through the genus-one Eisenstein channel.`; 3197 `The shadow tower instead carries non-automorphic arithmetic, detected by the shadow $L$-function and the Polyakov bridge.`; 3292 `What the four classes share is concentration of bar cohomology in bar degree~$1$.`; 3324 `The full MC element is controlled by the Koszul condition.`; 3467 `At genus~$0$, the BRST operator generates the bar differential computing these groups.`; 3934 `Higher-genus quantization is governed by the obstruction theory of node degenerations.`

- [MEDIUM] chapters/frame/preface.tex:2653,2655,2657,3112 — PROBLEM: table cells use `---` as placeholders. In this repo that collides with the em-dash blacklist, and here it also fails to say whether the entry is zero, absent, or not applicable. FIX: replace the 2653/2655/2657 placeholders with `\text{no}` and the 3112 placeholder with `\text{n/a}` or the actual invariant if one is intended.

- [LOW] chapters/frame/preface.tex:673 — PROBLEM: there is a stray space before the semicolon in `$F_1 = \kappa(\cH_k)/24 = k/24$ ;`. FIX: change it to `$F_1 = \kappa(\cH_k)/24 = k/24$.`

## Summary
Checked: 4374 | Findings: 15 | Verdict: FAIL


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
session id: 019d83f0-3c14-7db3-81b1-b42ec8e46888
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/frame/preface.tex

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \textbf, \emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \kappa without family?
   Any bare \Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.
mcp startup: no servers

thinking
**Planning auditing approach**

I need to read the entire file, making sure to include line numbers. I’ll also look for filler words, em dashes, and any TODO notes. Using regex and maybe a script would help me count repeated phrases thoroughly. Since the user mentioned a "MAXIMALLY HARSH adversarial auditor," I need to present findings in order of severity without including extraneous information. For each finding, I’ll provide exact fixes, as the user wants specific rewrites and changes. Let's get to it!
codex
Using `deep-beilinson-audit` for this turn. I’m reading the full `chapters/frame/preface.tex` with line numbers first, then I’ll run targeted pattern checks and verification passes so every finding is grounded and line-specific.
exec
/bin/zsh -lc 'nl -ba chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 4374

     1	\providecommand{\cZ}{\mathcal{Z}}
     2	\providecommand{\cA}{\mathcal{A}}
     3	\providecommand{\barB}{\overline{B}}
     4	\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
     5	\providecommand{\MC}{\text{MC}}
     6	\providecommand{\cM}{\mathcal{M}}
     7	\providecommand{\cC}{\mathcal{C}}
     8	\providecommand{\cO}{\mathcal{O}}
     9	\providecommand{\cP}{\mathcal{P}}
    10	\providecommand{\Eone}{E_1}
    11	\providecommand{\Convinf}{\mathrm{Conv}_\infty}
    12	\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
    13	\providecommand{\orline}[1]{\mathrm{or}(#1)}
    14	\providecommand{\fg}{\mathfrak{g}}
    15	\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
    16	
    17	\chapter*{Preface}
    18	\addcontentsline{toc}{chapter}{Preface}

thinking
**Considering audit requirements**

I’m thinking that a cosmetic audit might have been requested by the user, but it might not be necessary. The AGENTS could first review for substantive edits, especially if no edits have been made yet. However, there's a possibility that the deep-beilinson-audit skill could provide instructions. I should definitely check SKILL.md to gather more information on what to do next. Let's dive into that!
codex
I have the file length and the endpoints. Next I’m reading the audit skill instructions and then scanning the preface in bounded chunks so I can verify line-level findings instead of relying on pattern hits alone.
exec
/bin/zsh -lc 'rg -n --context 1 "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|---|—|TODO|FIXME|`|'"\\*\\*|_["'^ ]+_" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
zsh:1: unmatched "
 succeeded in 53ms:
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

 succeeded in 51ms:
    4374 chapters/frame/preface.tex
codex
I’ve loaded the audit workflow. I’m pulling the local constitution entries that bear on this file now: the blacklist/slop rules from `CLAUDE.md` and any concordance/registry/red-team references to the preface, so I can separate cosmetic defects from status drift that the preface is advertising.
exec
/bin/zsh -lc 'rg -n -C 2 "preface|ch:preface|Preface" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -C 2 "AP29|AP121|Wrong Formulas Blacklist|AI slop|Markdown in LaTeX|em-dash|preface" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -C 2 "preface|ch:preface|Preface" archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -C 2 "preface|ch:preface|Preface" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 exited 2 in 53ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
 succeeded in 53ms:
168-- "D_Ran(B(A)) is the cobar complex" (wrong: D_Ran is Verdier; cobar is Omega)
169-
170:### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits
171-
172-PRE-WRITE mental check: does the sentence start with one of the banned tokens below? If yes, REWRITE before typing.
--
281-**C31. Bershadsky-Polyakov complementarity conductor.** `kappa(BP) + kappa(BP^!) = 98/3` (NOT 1/3). `varrho_BP = 1/6`. Checks: K_BP = c(k) + c(-k-6) = 196 (cross-check C20); at self-dual level k=-3, kappa(BP) = 49/3. Wrong: kappa(BP)+kappa(BP^!)=1/3 (off by factor 98); varrho_BP=1/2 (confusing with rank-1 value).
282-
283:## Wrong Formulas Blacklist
284-
285-Concrete forbidden forms repeatedly emitted. Source: wrong_formulas_blacklist_wave12.md (B1-B51). Grep these after every .tex write; any match = fix immediately.
--
350-**prose hygiene**
351-
352:- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
353-- B41. Em-dash (`---` or Unicode U+2014). CORRECT: colon, semicolon, separate sentences.
354:- B42. AI slop vocabulary: `notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone`.
355-
356-**depth / dimension / fiber-base**
--
 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '401,800p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,400p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '801,1200p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The ordered bar $\barB^{\mathrm{ord}}(\cA)$ carries the
\emph{deconcatenation coproduct}:
\begin{equation}\label{eq:pf1-deconc}
\Delta[s^{-1}a_1|\cdots|s^{-1}a_n]
\;=\;
\sum_{i=0}^{n}
[s^{-1}a_1|\cdots|s^{-1}a_i]
\;\otimes\;
[s^{-1}a_{i+1}|\cdots|s^{-1}a_n]\,,
\end{equation}
splitting an ordered sequence at every position: $n+1$ terms.
This is coassociative but not cocommutative, an
$E_1$-coalgebra reflecting the linear ordering.

The $\Sigma_n$-coinvariant quotient
\[
\barB^{\Sigma}_X(\cA)
\;=\;
\bigoplus_{n\ge 1}
\bigl(s^{-1}\bar\cA\bigr)^{\otimes n}_{\Sigma_n}
 succeeded in 51ms:
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cA}{\mathcal{A}}
\providecommand{\barB}{\overline{B}}
\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
\providecommand{\MC}{\text{MC}}
\providecommand{\cM}{\mathcal{M}}
\providecommand{\cC}{\mathcal{C}}
\providecommand{\cO}{\mathcal{O}}
\providecommand{\cP}{\mathcal{P}}
\providecommand{\Eone}{E_1}
\providecommand{\Convinf}{\mathrm{Conv}_\infty}
\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
\providecommand{\orline}[1]{\mathrm{or}(#1)}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\label{ch:preface}
\markboth{Preface}{Preface}
 succeeded in 51ms:
beyond the symmetric coinvariant at every genus~$g\ge 1$.


% ====================================================================
\subsection*{From genus $0$ to all genera}
% ====================================================================

Everything above takes place at genus~$0$: the propagator
$\eta_{12} = d\log(z_1-z_2)$ is globally defined
on~$\mathbb P^1$, and the Arnold relation holds without correction.
The genus-$0$ theory is not classical: already on~$\mathbb A^1$
the configuration spaces $\mathrm{Conf}_n(\mathbb A^1)$ carry
FM compactifications and the Arnol'd algebra of logarithmic
forms; these structures, together with the Borcherds extraction
rule, are genuinely chiral and have no counterpart over a point. The classical Yang--Baxter equation
is already a genus-$0$ theorem (the Arnold relation on
$\overline{\mathcal{M}}_{0,4}$ evaluated on the Casimir tensor);
the Drinfeld--Kohno comparison between braid-group monodromy and
quantum-group braiding is a genus-$0$ theorem; the KZ connection
is a genus-$0$ shadow of the universal MC element. Genus~$0$ on

thinking
**Completing the audit**

I need to continue with the remainder of the audit. For the cosmetic audit, I should focus on the issues throughout the whole file since the user wants every finding. It’s important to identify patterns within the audit categories rather than digging into every specific mathematical issue. So, I’ll need to work through chunks 1201-2400, 2401-3600, and 3601-4374 to ensure I cover everything.
exec
/bin/zsh -lc "sed -n '1601,2000p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2001,2400p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1201,1600p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
each slot, but does not assemble into a bifunctor on the
$\infty$-categorical level. This is a structural constraint, not
a technical gap: the MC3 categorical lift of bar-cobar duality
must proceed one slot at a time.

The bar-cobar adjunction $B_\kappa\dashv\Omega_\kappa$ is a
\emph{Quillen equivalence} (Vallette): different
$\mathrm{Ch}_\infty$ presentations yield quasi-isomorphic
deformation theories.

\subsection*{3.7.\enspace Assembly}

The \emph{modular convolution $L_\infty$-algebra}:
\begin{equation}\label{eq:pref-convolution}
\mathfrak g^{\mathrm{mod}}_\cA
\;:=\;
\Convinf\!\Bigl(
\cC^{\log\mathrm{FM}}_{\mathrm{mod}},\;
\mathrm{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr).
 succeeded in 51ms:
$\Phi_s+\Phi_t+\Phi_u=F_3$,
the Malikov--Schechtman Jacobiator homotopy: the Jacobiator is a
boundary in the bar complex.

In degree $(1,1)$: the single boundary divisor
$\delta_{\mathrm{irr}}\subset\overline{\cM}_{1,1}$ gives
\[
\Theta^{[1]}_\cA\big|_{(1,1)}
=[\delta_{\mathrm{irr}}]\otimes\Delta,
\]
where $\Delta=\sum_i e_i\otimes e^i$ is the Casimir element of the
cyclic pairing.

In degree $(0,5)$: the weight-one component restricts to the ten
boundary divisors of $\overline{\cM}_{0,5}$ (the Petersen graph),
and the MC equation recovers the pentagon identity. The entire
$A_\infty$ hierarchy is the tree-level, genus-zero projection of a
single MC element.

\subsection*{4.6.\enspace The all-genus recursion}
 succeeded in 50ms:

\medskip

\noindent\textbf{Theorem~A} (bar-cobar adjunction and Verdier
intertwining). The bar functor~$B$ and the cobar functor~$\Omega$
form an adjoint pair on the category of chiral algebras
over~$\operatorname{Ran}(X)$. Verdier duality on~$\operatorname{Ran}(X)$
intertwines the bar of~$\cA$ with the bar of the Koszul
dual: $\mathbb D_{\operatorname{Ran}}(B(\cA))\simeq\cA^!_\infty$.
\medskip

\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
locus, the cobar of the bar recovers the original algebra:
$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$. The bar complex is a
complete invariant on the Koszul locus; no information is lost
there.
\medskip

\noindent\textbf{Theorem~C} (complementarity). The genus-$g$
cohomology of the center local system decomposes into two
codex
I’ve read through the first 2,400 lines. The file is not just cosmetically noisy; the preface is overloaded with duplicated theorem advertisements, signpost transitions, and repeated “pipeline” summaries. I’m finishing the last two chunks now and then I’ll collapse the findings to line-specific defects that actually survive re-checking.
exec
/bin/zsh -lc "sed -n '2401,2800p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3201,3600p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2801,3200p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3601,4374p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
tree-level MC element to one-loop. Convergence follows from
completeness of the depth filtration and pronilpotence of the
weight filtration: the $\varprojlim^1$ term vanishes by
Mittag-Leffler.

For Heisenberg, the spectral sequence degenerates at~$E_1$.
For Virasoro, $d_1\neq 0$ and nontrivial differentials persist
at every page.

\subsection*{5.5.\enspace Homotopy invariance}

The characteristic classes of~\S5.1 and the CohFT of~\S5.3 are
defined from the MC element~$\Theta_\cA$, which depends on the
choice of homotopy retraction data. The question is whether the
output is independent of the input.

The shadow algebra
$\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
homotopy invariant. For any $\infty_\alpha$-quasi-isomorphism
$f\colon\cA\xrightarrow{\sim}\cA'$, the induced map on MC
 succeeded in 52ms:
\cong \mathrm{Fun}(\mathrm{Op}_{{}^L\fg})$, the Feigin--Frenkel
centre of opers on the formal disc. The Feigin--Frenkel involution
$k \leftrightarrow -k - 2h^\vee$ is Koszul duality on
configuration spaces: it interchanges~$\cA$ and~$\cA^!$ while
preserving the bar-cobar adjunction.

\subsection*{From Kac--Moody to Virasoro: the self-coupling}

Shadow depth~$3$ means the cubic obstruction (the Lie bracket) is the
last invariant the tower sees. The Jacobi identity, by killing the
quartic shadow $\mathfrak{Q}$, forces the discriminant
$\Delta = 8\kappa S_4$ to vanish, and the algebraicity theorem of
Section~6 forces the tower to terminate. For an infinite tower, the
quartic must survive: some mechanism must generate new obstructions at
every degree, feeding structure into the tower that the Jacobi identity
cannot kill.

The mechanism is self-coupling. The stress tensor~$T$ satisfies
$T_{(1)}T = 2T$: it appears in its own OPE as a singular term.
No Kac--Moody current has this property ($J^a_{(1)}J^b$ is a
 succeeded in 53ms:
\subsection*{8.2.\enspace The Polyakov correspondence}

Polyakov's programme computes the string partition function
$Z=\sum_g g_s^{2g-2}\int_{\cM_g}[\mathrm{det}'_\zeta\Delta]
^{-d/2}\,d\mu_{\mathrm{WP}}$
by gauge-fixing the worldsheet metric to conformal gauge, paying
the price of a conformal anomaly
$\langle T^a{}_a\rangle=(c/12)\,R$ and a ghost system with
$c_{\mathrm{ghost}}=-26$. Every element of this programme has a
bar-cobar counterpart:
\begin{itemize}[nosep]
\item The conformal anomaly is $\kappa(\cA)$: both measure the
 obstruction to metric-independence at genus~$1$, one by
 functional-integral trace, the other by bar curvature.
\item The critical dimension $c=26$ is the vanishing of the dual
 curvature: $\kappa(\mathrm{Vir}_{26-c})=(26{-}c)/2=0$ when
 $c=26$.
\item The ghost system $bc$ with $c_{\mathrm{ghost}}=-26$ is the
 Koszul dual $\cA^!$ in the BRST pairing: the ghost partition
 function is the complementarity partner.
 succeeded in 53ms:
(Virasoro, $\cW$-algebras), the same conclusion is
expected but conditional on constructing the bulk BRST
complex (Conjecture~\ref{conj:topologization-general}).
At the critical level $k=-h^\vee$ for affine Kac--Moody
algebras, the Sugawara construction degenerates, the
conformal vector ceases to exist, and the $\SCchtop$-algebra
does not topologise. The critical level is therefore the
precise obstruction to closing the $E_n$ circle at the
$\SCchtop$ stage.

\subsection*{10.3.\enspace Five notions of $E_1$-chiral algebra}

The phrase ``$E_1$-chiral algebra'' admits at least five
inequivalent definitions:
\begin{enumerate}[label=\textup{(\Alph*)},nosep]
\item a strict algebra over the chiral associative operad
 $\operatorname{Ass}^{\mathrm{ch}}$ (D-module formulation);
\item an $A_\infty$-algebra in $\operatorname{End}^{\mathrm{ch}}_\cA$
 (the working definition of this monograph);
\item an Etingof--Kazhdan quantum vertex algebra





thinking
**Evaluating file contents**

I need to decide if there are bare \kappa occurrences in this file that should be family-tagged. It's crucial to base my assessment on the actual content of the file. I should note any inconsistencies, especially when the same paragraph mentions both `\kappa(\cA)` and a bare `\kappa`. For example, line 4373 uses "one extraction..." which doesn’t seem relevant to my analysis.
thinking
**Exploring Markdown in LaTeX**

I’m wondering about using Markdown in LaTeX, possibly questioning if it’s feasible. I should search for syntax elements like backticks or formatting for bold and italic text. For the chapter opening quality, I think it should begin with something like, "This monograph studies...," rather than something unconvincing. I also need to consider the use of passive voice hedging phrases. I'll look for terms like "can be shown" and "seems reasonable," and explore other subtle passive constructions.
thinking
**Evaluating mathematical documentation**

I need to focus on actual cases within my mathematical statements. There are a few notation issues, like using bare symbols without definitions, probably more than I realize. I should search for areas with dead code, like long commented sections or unused labels. Redundancy seems to be a concern too, with the same theorem repeated in different ways. I want to ensure transition quality and check for issues like double spaces or mismatched braces, possibly using a LaTeX linter. My findings should be categorized based on severity.
thinking
**Assessing structural issues**

I'm wondering if the opening chapter might fail or if redundancy affects readability. While it's not exactly critical, since the user wants a harsh review, I should label major structural issues as HIGH or CRITICAL. I’ll define categories: HIGH for macro inconsistency and redundancy, MEDIUM for signpost transitions. I need to conduct a systematic search using patterns like slop list and various macros. Unused labels could be tricky to identify, especially if they’re referenced elsewhere. If there's no dead code, I'll just focus on what I find.
thinking
**Searching suspicious macros**

I'm planning to search for macro definitions, focusing on potentially suspicious ones like `\SCchtop`, `\Einf`, `\cH`, and `\Bbbk`. It’s unclear if they’re defined elsewhere, so I’ll look specifically for any undefined instances in the repo. I’m wondering if there are a lot of them or if it might be more limited. I’ll need to collect this information carefully to ensure everything aligns properly. Let's see what I find!
codex
I’ve finished the full read. Now I’m doing the verification pass: exact pattern scans for forbidden prose/notation, plus repo-wide macro-definition checks for the preface-specific commands so I can distinguish real defects from mere local unfamiliarity.
exec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|---|—|TODO|FIXME|it can be shown|one might expect|it seems reasonable|We now turn to|we now turn to|The question is|The answer is|The question forced|The distinction forces|The question is what|The question is whether" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "`|'"\\*\\*|_[A-Za-z0-9]\" chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\kappa(?"'!'"\\()|\\\\Omega/z|r\\(z\\)\\s*=\\s*\\\\Omega/z|\\\\SCchtop|\\\\Einf|\\\\cH|\\\\Bbbk\" chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2168:$\Theta_\cA$ from which every invariant projects. The question is
2335:degrees $2$, $2$, and $4$. The question is whether the full
2414:choice of homotopy retraction data. The question is whether the
2653: & $\checkmark$ & --- & --- & G\\
2655: & $\checkmark$ & $\checkmark$ & --- & L\\
2657: & $\checkmark$ & --- & --- & C\\
2856:$\mathbb{E}_1$. The question forced by the depth classification
3112: & ---
3158:data. The question is whether these rational numbers carry
3197:shadow tower does not. The distinction forces the question: what
3295:The answer is concentration: the bar cohomology
3324:element at degree~$2$. The question is what controls it at
3325:\emph{all} degrees. The answer is the Koszul condition: bar
3467:The question is what \emph{generates} the bar differential that
3934:The question is whether the tree-level PVA extends to a quantum
 exited 1 in 53ms:
zsh:1: unmatched "
 exited 2 in 51ms:
rg: regex parse error:
    (?:\kappa(?!\()|\Omega/z|r\(z\)\s*=\s*\Omega/z|\SCchtop|\Einf|\cH|\Bbbk)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"\\\\(providecommand|newcommand|def|DeclareMathOperator)\\{\\\\(SCchtop|Einf|cH|Bbbk)\\}|\\\\def\\\\(SCchtop|Einf|cH|Bbbk)\" ." in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:\(providecommand|newcommand|def|DeclareMathOperator)\{\(SCchtop|Einf|cH|Bbbk)\}|\def\(SCchtop|Einf|cH|Bbbk))
                                                                                   ^
error: unopened group

thinking
**Refining regex searches**

I need to get my regex quoting right with single quotes and appropriate escaping. Maybe I should consider using grep for markdown or backticks. It seems I’ve found some extra question phrases and `---` from table dashes that might not be what I want. I might need to focus on targeted patterns and use `-P` for lookarounds. A simpler search could be `\\kappa[^({]`, but it's not perfect. Let's try `rg -n -P '\\\\kappa(?!\()'` instead.
exec
/bin/zsh -lc "rg -n -P '\\\\kappa(?"'!'"\\()|\\\\Omega/z|r\\(z\\)\\s*=\\s*\\\\Omega/z|\\\\SCchtop|\\\\Einf|\\\\cH|\\\\Bbbk' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '"'`|'"\\*\\*|_[A-Za-z0-9]' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
28:the operad: a curve~$X$ gives $\Einf$ (symmetric factorisation on
673:$F_1 = \kappa(\cH_k)/24 = k/24$ ;
708:\frac{k\,\kappa^{ab}}{(z-w)^2}\,,
711:algebra~$\mathfrak g$ and $\kappa^{ab}$ is the Killing form
716:$J^a_{(1)}J^b = k\,\kappa^{ab}\cdot\mathbf 1$.
729:\underbrace{k\,\kappa^{ab}\cdot\mathbf 1\cdot
769:the passage from $r(z) = k\,\Omega/z$ to
833:When $X=\operatorname{Spec}\Bbbk$ is a point, configuration spaces
960:affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
967:$\mathrm{av}\colon\operatorname{End}_\cA(2)\to\Bbbk$:
1008:The mechanism: the fibrewise curvature $\kappa\cdot\omega_g$ is a
1020:\kappa\cdot\omega_g-\kappa\cdot\omega_g+0
1097:governed by a single discriminant $\Delta = 8\kappa S_4$ that
1101:the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
1103:data $(\kappa,\alpha,S_4)$ through the Riccati algebraicity
1126:\;\simeq\;\Bbbk[-(3g-3)]
1242:$P_{\cH_k}(t)=1+t+t^2$ for Heisenberg,
1356:$\Com(g,n)=\Bbbk$ for every stable $(g,n)$), the Feynman transform
1411: & \text{coinvariant genus towers ($\kappa$)}
1482:$C_1(\overline{\cM}_{0,4})\cong\Bbbk$ provides a
exec
/bin/zsh -lc "rg -n 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|it can be shown|one might expect|it seems reasonable|we now turn to|We now turn to' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 627

10:\providecommand{\Eone}{E_1}
41:$\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
43:$E_1$-coalgebra with deconcatenation coproduct, whose differential
45:$\eta = d\log(z_1 - z_2)$ on Fulton--MacPherson configuration spaces.
48:its $\Sigma_n$-coinvariant quotient
49:$\barB^\Sigma_X(\cA)$ retains only the scalar
53:The moduli space $\overline{\mathscr{M}}_g$ is global: it parametrises
56:$\mathrm{obs}_1(\cA) = \kappa(\cA)\cdot\lambda_1$ unconditionally;
58:$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ persists at all genera.
66:\barB^{\mathrm{ord}}_X(\cA)
70:\Delta[a_1|\cdots|a_n]
71:= \sum_{i=0}^{n}[a_1|\cdots|a_i]\otimes[a_{i+1}|\cdots|a_n],
73:is a cofree $E_1$-coalgebra with deconcatenation coproduct. Its
79:where $\Theta_\cA := D_\cA - d_0$ is the universal Maurer--Cartan
82:invariant~$S_r(\cA)$; the tower $\{S_r(\cA)\}_{r\ge 2}$ is the
83:correction hierarchy. The $\Sigma_n$-coinvariant quotient
84:$\barB^\Sigma_X(\cA)$ erases $r_\cA(z)$ and retains only the scalar
90:locus $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$.
exec
/bin/zsh -lc "rg -n -P '\\\\(providecommand|newcommand|DeclareMathOperator)\\{\\\\(SCchtop|Einf|cH|Bbbk)\\}|\\\\def\\\\(SCchtop|Einf|cH|Bbbk)' ." in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 63ms:
./standalone/survey_modular_koszul_duality.tex:34:\providecommand{\cH}{\mathcal{H}}
./standalone/survey_modular_koszul_duality.tex:71:\providecommand{\Einf}{E_\infty}
./standalone/survey_modular_koszul_duality.tex:85:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./standalone/survey_modular_koszul_duality.tex:91:\providecommand{\Bbbk}{\mathbb{k}}
./standalone/chiral_chern_weil.tex:47:\newcommand{\Einf}{E_\infty}
./standalone/shadow_towers_v2.tex:36:\newcommand{\cH}{\mathcal{H}}
./tmp_standalone_audit/survey_v2_xr.tex:45:\providecommand{\cH}{\mathcal{H}}
./tmp_standalone_audit/survey_v2_xr.tex:90:\providecommand{\Bbbk}{\mathbb{k}}
./tmp_standalone_audit/survey_v2_xr.tex:97:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/wrap_programme_summary_sections5_8.tex:38:\newcommand{\cH}{\mathcal{H}}
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:44:\newcommand{\cH}{\mathcal{H}}
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:62:\newcommand{\Einf}{\mathsf{E}_{\infty}}
./standalone/shadow_towers.tex:41:\newcommand{\cH}{\mathcal{H}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:43:\providecommand{\cH}{\mathcal{H}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:88:\providecommand{\Bbbk}{\mathbb{k}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:95:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./standalone/ordered_chiral_homology.tex:44:\newcommand{\cH}{\mathcal{H}}
./standalone/ordered_chiral_homology.tex:62:\newcommand{\Einf}{\mathsf{E}_{\infty}}
./standalone/N3_e1_primacy.tex:35:\newcommand{\cH}{\mathcal{H}}
./standalone/programme_summary_section1.tex:38:\newcommand{\cH}{\mathcal{H}}






thinking
**Refining search methods**

I found the `rg` output too noisy because it's matching subscripts with `_`, which isn't useful. I should look for better ways to search for backticks and formatting symbols like `**` and `_`. I could use a command like `grep -n '\*\*'`, but I want to try to find specific AI tokens instead. Also, I need to identify problematic uses of bare kappa occurrences. The user wants consistency in notation, such as ensuring families and levels are defined properly.
thinking
**Auditing notation inconsistencies**

I need to look for areas where the notation isn't consistent, specifically not all `\kappa^{ab}` on the Killing form. I’ll find lines where the modular characteristic appears as a bare scalar outside of explicit contexts. I've noted candidate line numbers to check: 1008, 1020, 1097, and several others. I should inspect the context around these lines to determine if `\kappa(\cA)` or similar replacements are needed. The user wants every inconsistency, even the signpost phrases, so I'll audit the transition quality as well.
thinking
**Identifying formulaic transitions**

I want to flag any repeated formulaic transitions that resemble the AP109-like signposts. This means I'll need to pinpoint the exact lines where these transitions occur and figure out specific fixes for each instance. It might require identifying multiple occurrences, which could be a bit tedious, but addressing these formulaic phrases will help improve clarity in the text. I’m just making sure to stay organized while working through this!
thinking
**Considering compilation options for the book**

I'm thinking about using the command `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`, but it might take quite a while to compile the entire book. The user is interested in an audit specifically, and yes, compilation can help catch any undefined environments. Should I go ahead with that? Alternatively, maybe I should consider using the build-surface skill instead to improve efficiency.
thinking
**Identifying redundancies**

I need to fix some issues in the document. For lines 112-116, I don't see a problem; it might be related to Volume II. Lines 1204-1260 contain another theorem summary in Section 2, which might overlap with earlier sections. I notice potential redundancy with theorems repeated in different sections.

I’ll specify paragraphs where theorems are restated in two styles. I’m considering keeping only a compact summary in one section, while referencing theorems elsewhere to streamline things. I'll pinpoint exact line numbers to ensure clarity.
thinking
**Gathering line contexts**

I need to identify the line numbers around the table and use newline characters for clarity in the relevant sections. I'll gather contexts surrounding the candidate findings. To do this, I plan to use `rg -n` to pinpoint the exact lines of important phrases, such as "The five theorems," "Read together," and others. Doing this will help me collect the relevant contexts effectively and ensure I have all the necessary details.
codex
I’ve narrowed the candidate findings. I’m checking the remaining risky ones now: table `---` placeholders, repeated theorem surfaces, and whether `\Bbbk` is actually defined in the book build or only in standalones.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3108,3116p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '\\\\(providecommand|newcommand|DeclareMathOperator)\\{\\\\Bbbk\\}|\\\\def\\\\Bbbk' main.tex chapters styles preamble.tex texmf 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '88,112p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2648,2660p'" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
  3108	 & $\mathrm{av}(r(z))$
  3109	 & $k\,\Omega/z$
  3110	 & $3$
  3111	 & L
  3112	 & ---
  3113	 & YBE $=$ degree-$3$ MC
  3114	\end{tabular}
  3115	\end{center}
  3116	
 succeeded in 52ms:
  2648	& $\Theta^{(2)}_{\mathrm{sep}\circ\mathrm{loop}}$
  2649	& $\Theta^{(2)}_{\mathrm{pf}}$
  2650	& \textbf{Class}\\
  2651	\hline
  2652	\textbf{Heisenberg} $\cH_k$
  2653	 & $\checkmark$ & --- & --- & G\\
  2654	\textbf{Affine} $\widehat{\fg}_k$
  2655	 & $\checkmark$ & $\checkmark$ & --- & L\\
  2656	\textbf{$\beta\gamma$ system}
  2657	 & $\checkmark$ & --- & --- & C\\
  2658	\textbf{Virasoro} $\mathrm{Vir}_c$
  2659	 & $\checkmark$ & $\checkmark$ & $\checkmark$ & M
  2660	\end{tabular}
 exited 2 in 56ms:
chapters/connections/twisted_holography_quantum_gravity.tex:20:\providecommand{\Bbbk}{\mathbb{k}}
chapters/connections/semistrict_modular_higher_spin_w3.tex:11:\providecommand{\Bbbk}{\mathbb{k}}
chapters/connections/thqg_gravitational_s_duality.tex:12:\providecommand{\Bbbk}{\mathbb{k}}
 succeeded in 55ms:
    88	the modular characteristic: the single number that survives averaging.
    89	At genus~$1$ unconditionally, and at all genera on the uniform-weight
    90	locus $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$.
    91	
    92	\medskip
    93	
    94	\noindent\textbf{The five theorems.}\enspace
    95	Five theorems extract the $\Sigma_n$-invariant content of the ordered
    96	bar. Theorem~A constructs the bar-cobar adjunction and its Verdier
    97	intertwining, producing the pair
    98	$(\cA,\cA^{!}_\infty)$ from $\barB^{\mathrm{ord}}(\cA)$.
    99	Theorem~B proves bar-cobar inversion
   100	$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$ on the Koszul locus.
   101	Theorem~C decomposes the derived chiral centre
   102	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)
   103	= R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
   104	into Lagrangian halves controlled by~$\cA$ and~$\cA^!$, with
   105	$\kappa(\cA)+\kappa(\cA^!)$ as the scalar shadow of the splitting.
   106	Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and
   107	at all genera on the uniform-weight locus Theorem~H bounds the chiral Hochschild complex in degrees

thinking
**Investigating file structure**

I’m searching for the main files, but so far, I’ve only found chapters and connection files, not the main file itself. I need to figure out if those chapters are loaded before the preface, but it seems likely they're not. I could use "rg" in the main order to see if the preface is included before the chapters. I should inspect the main includes and search specifically for the preface and those chapter connections.
exec
/bin/zsh -lc "rg -n 'twisted_holography_quantum_gravity|semistrict_modular_higher_spin_w3|thqg_gravitational_s_duality' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'preface|chapters/frame/preface|include\\{|input\\{' main.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '820,840p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '620,710p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1493:% \input{chapters/connections/twisted_holography_quantum_gravity}
1498:\input{chapters/connections/semistrict_modular_higher_spin_w3}
1590: % twisted_holography_quantum_gravity.tex phantom labels
 succeeded in 52ms:
841:\include{chapters/frame/preface}
845: \input{chapters/frame/guide_to_main_results}
854:\include{chapters/theory/introduction}
869:\include{chapters/frame/heisenberg_frame}
882:% \input{platonic_introduction_volume_I} % archived; content absorbed into introduction.tex
958:\include{chapters/theory/fourier_seed}
965:\include{chapters/theory/algebraic_foundations}
971:\include{chapters/theory/three_invariants}
977:\include{chapters/theory/configuration_spaces}
983:\include{chapters/theory/bar_construction}
989:\include{chapters/theory/cobar_construction}
996:\include{chapters/theory/bar_cobar_adjunction}
1000:\input{appendices/homotopy_transfer}
1006:% \input{chapters/theory/bar_cobar_quasi_isomorphism}
1012:\include{chapters/theory/poincare_duality}
1020:\include{chapters/theory/chiral_koszul_pairs}
1021:\include{chapters/theory/koszul_pair_structure}
1027:\include{chapters/theory/higher_genus}
1029:% \include{chapters/theory/higher_genus_full}
1034:% \input{chapters/theory/higher_genus_quasi_isomorphism}
 succeeded in 58ms:
   620	\providecommand{\bC}{\mathbb{C}}
   621	\providecommand{\bF}{\mathbb{F}}
   622	\providecommand{\bP}{\mathbb{P}}
   623	\providecommand{\bZ}{\mathbb{Z}}
   624	\providecommand{\bR}{\mathbb{R}}
   625	\providecommand{\bQ}{\mathbb{Q}}
   626	\providecommand{\bG}{\mathbb{G}}
   627	\providecommand{\cC}{\mathcal{C}}
   628	\providecommand{\cD}{\mathcal{D}}
   629	\providecommand{\cE}{\mathcal{E}}
   630	\providecommand{\cF}{\mathcal{F}}
   631	\providecommand{\cH}{\mathcal{H}}
   632	\providecommand{\cL}{\mathcal{L}}
   633	\providecommand{\cM}{\mathcal{M}}
   634	\providecommand{\cN}{\mathcal{N}}
   635	\providecommand{\cO}{\mathcal{O}}
   636	\providecommand{\cP}{\mathcal{P}}
   637	\providecommand{\cY}{\mathcal{Y}}
   638	\providecommand{\cZ}{\mathcal{Z}}
   639	\providecommand{\fS}{\mathfrak{S}}
 succeeded in 58ms:
   820	is a genus-$0$ shadow of the universal MC element. Genus~$0$ on
   821	a curve is the locus where $E_1$ operadic structure lives, and
   822	$E_1$ structure is strictly richer than $E_\infty$ structure
   823	(the $R$-matrix, the Yangian, and the ordered bar coproduct are
   824	all genus-$0$ invariants invisible to the symmetric coinvariant).
   825	
   826	On a curve of genus $g \geq 1$, the function $z_1 - z_2$ has no
   827	global meaning, and the bar differential no longer squares to zero.
   828	The failure is controlled by a single scalar $\kappa(\cA)$ extracted
   829	from the leading OPE singularity: the modular characteristic.
   830	Restoring nilpotence across all genera is the subject of Section~2.
   831	
   832	\begin{remark}[The zero-dimensional shadow]\label{rem:pf1-zero-dim}
   833	When $X=\operatorname{Spec}\Bbbk$ is a point, configuration spaces
   834	collapse, logarithmic forms vanish, and the chiral bar complex
   835	recovers the classical bar construction of an associative
   836	algebra~$A$. A quadratic algebra $A = T(V)/(R)$ has quadratic dual
   837	$A^! = T(V^*)/(R^\perp)$; when~$A$ is Koszul, the bar cohomology
   838	concentrates in diagonal degrees and
   839	$H^*(B(A)) \cong (A^!)^\vee$. The operadic instances


thinking
**Analyzing undefined command**

I’m noticing that `\Bbbk` isn’t defined in the main excerpt, which might mean it's either defined later or not at all. It looks like it’s treated as an undefined macro, possibly due to being absent from included packages or files. I need to confirm its absence prior to line 833 in the preface. My solution is to add `\providecommand{\Bbbk}{\mathbb{k}}` near the top, or replace every instance of `\Bbbk` with `\mathbb{k}` for consistency.
thinking
**Examining macro definitions**

I see that in line 10 of the preface, `\Eone` is defined, but in the main sections from lines 702–706, it’s defined as `\mathsf{E}_{1}`. Because the preface is included after the main preamble, that definition will not change anything. However, `\Einf` is only defined in the main, so there may be inconsistency if the preface uses `$E_1$` instead of `\Eone`. I also need to check if `\cH` is defined in the main. I'll use regex to identify duplicate theorems and transition phrases too.
exec
/bin/zsh -lc "rg -n 'Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|The five theorems|five main theorems|Read together' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
34:factorisation (co)homology. The five theorems of this volume
94:\noindent\textbf{The five theorems.}\enspace
96:bar. Theorem~A constructs the bar-cobar adjunction and its Verdier
99:Theorem~B proves bar-cobar inversion
101:Theorem~C decomposes the derived chiral centre
106:Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and
107:at all genera on the uniform-weight locus Theorem~H bounds the chiral Hochschild complex in degrees
111:The five theorems are the $\Sigma_n$-invariant skeleton. The full
434:deformation. The five main theorems of this monograph
458:$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$ (Theorem~B).
477:content of Theorem~A, not a tautology.
504:without information loss (Theorem~B). The Verdier functor
507:(Theorem~A). This is what Volume~I proves.
781:retains only what is $\Sigma_n$-invariant. The five main theorems
1101:the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
1198:\subsection*{The five theorems}
1204:\noindent\textbf{Theorem~A} (bar-cobar adjunction and Verdier
1212:\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
1219:\noindent\textbf{Theorem~C} (complementarity). The genus-$g$
1227:\noindent\textbf{Theorem~D} (modular characteristic).
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1196,1264p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2078,2108p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '4248,4270p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2078	\textbf{Projection of $\Theta_\cA$}
  2079	 & \textbf{Invariant} & \textbf{Section} \\
  2080	\hline
  2081	Scalar ($r=2$, genus tower)
  2082	 & $\kappa(\cA)$, $F_g$, $\hat A$-genus
  2083	 & \S2 \\[2pt]
  2084	Binary genus-$0$ residue
  2085	 & classical $r$-matrix, Yangian seed
  2086	 & \S7 \\[2pt]
  2087	Binary Verdier dual
  2088	 & complementarity $Q_g \oplus Q_g^!$
  2089	 & \S2 \\[2pt]
  2090	Bar-cobar counit
  2091	 & inversion $\Omega(\barB(\cA))\xrightarrow{\sim}\cA$
  2092	 & \S1 \\[2pt]
  2093	Chiral Hochschild
  2094	 & $\mathrm{ChirHoch}^*(\cA)$, deformation ring
  2095	 & \S9 \\[2pt]
  2096	Spectral discriminant
  2097	 & $\Delta_\cA(x)$, genus-$1$ Hessian
 succeeded in 53ms:
  1196	boundaries do not commute.
  1197	
  1198	\subsection*{The five theorems}
  1199	
  1200	Five theorems extract the structural content of the bar complex.
  1201	
  1202	\medskip
  1203	
  1204	\noindent\textbf{Theorem~A} (bar-cobar adjunction and Verdier
  1205	intertwining). The bar functor~$B$ and the cobar functor~$\Omega$
  1206	form an adjoint pair on the category of chiral algebras
  1207	over~$\operatorname{Ran}(X)$. Verdier duality on~$\operatorname{Ran}(X)$
  1208	intertwines the bar of~$\cA$ with the bar of the Koszul
  1209	dual: $\mathbb D_{\operatorname{Ran}}(B(\cA))\simeq\cA^!_\infty$.
  1210	\medskip
  1211	
  1212	\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
  1213	locus, the cobar of the bar recovers the original algebra:
  1214	$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$. The bar complex is a
  1215	complete invariant on the Koszul locus; no information is lost
 succeeded in 53ms:
  4248	$\Theta_\cA:=D_\cA-d_0$, which is MC because $D_\cA^2=0$.
  4249	
  4250	The shadow obstruction tower consists of finite-order projections:
  4251	\begin{align*}
  4252	\Theta_\cA^{\le 2}&:\qquad\kappa(\cA)
  4253	 &&\text{(modular characteristic, scalar curvature)},\\
  4254	\Theta_\cA^{\le 3}&:\qquad\mathfrak C(\cA)
  4255	 &&\text{(cubic shadow, Lie structure)},\\
  4256	\Theta_\cA^{\le 4}&:\qquad\mathfrak Q(\cA)
  4257	 &&\text{(quartic resonance class, contact structure)},\\
  4258	\Theta_\cA^{\le r}&:\qquad\operatorname{Sh}_r(\cA)
  4259	 &&\text{(degree-$r$ shadow)},\\
  4260	\Theta_\cA&:\qquad\varprojlim_r\Theta_\cA^{\le r}
  4261	 &&\text{(the universal MC element)}.
  4262	\end{align*}
  4263	Theorems~A--D+H and the genus expansion are proved projections
  4264	of the scalar level~$\kappa$. The holographic datum
  4265	$\mathcal H(T)=(\cA,\cA^!,\cC,r(z),\Theta_\cA,\nabla^{\mathrm{hol}})$
  4266	packages $\Theta_\cA$ and its projections into the data of a 3d
  4267	holomorphic-topological field theory.
exec
/bin/zsh -lc "rg -n -P '\\\\kappa(?"'![({_''^A-Za-z])'"' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1008:The mechanism: the fibrewise curvature $\kappa\cdot\omega_g$ is a
1020:\kappa\cdot\omega_g-\kappa\cdot\omega_g+0
1097:governed by a single discriminant $\Delta = 8\kappa S_4$ that
1101:the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
1103:data $(\kappa,\alpha,S_4)$ through the Riccati algebraicity
1411: & \text{coinvariant genus towers ($\kappa$)}
1606:The bar-cobar adjunction $B_\kappa\dashv\Omega_\kappa$ is a
2134:determined by three seed invariants $(\kappa, \alpha, S_4)$.
2272:invariant not recoverable from~$\kappa$ and~$\Delta_\cA$. Its
2333:The three projections ($\kappa$, $\Delta_\cA$,
2489:not polynomial in~$\kappa$. The quartic contact invariant:
2511:Q_L(t)=4\kappa^2+12\kappa\alpha\,t+(9\alpha^2+16\kappa S_4)t^2,
2514:$(\kappa,\alpha,S_4)$
2517:discriminant $\Delta = 8\kappa S_4$ governs the depth
2675:$\rho(\cA) = \sqrt{9\alpha^2+2\Delta}\,/\,(2|\kappa|)$
2718:is not determined by $\kappa=c/2$; it detects the quartic
2724:all shadow invariants separate: $\kappa$ is additive,
2758:one shadow invariant ($\kappa = k$), one depth class (G). The
2798:At the critical level $k = -h^\vee$: $\kappa = 0$, the bar complex
2812:$\Delta = 8\kappa S_4$ to vanish, and the algebraicity theorem of

thinking
**Evaluating notation inconsistencies**

I need to decide which items are actual notation inconsistencies versus what might be acceptable generic variables. For general discussions, using bare kappa could be fine if I define it as a generic scalar invariant. The user asked if any bare kappa can stand alone, which probably suggests I can flag it as representative. However, the phrase "every finding" implies I’m looking at about 33 findings, which could become extensive. I might focus on cosmetic issues alongside notation consistency. I also need categories for signpost phrases, which I’ve started to find.
exec
/bin/zsh -lc "rg -n -C 1 'The question is|The answer is|The distinction forces|The question forced' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2167-Section~4 constructed a universal Maurer--Cartan element
2168:$\Theta_\cA$ from which every invariant projects. The question is
2169-what those projections are: what characteristic classes does the
--
2334-$\mathfrak{R}^{\mathrm{mod}}_4$) capture the shadow data at
2335:degrees $2$, $2$, and $4$. The question is whether the full
2336-collection of projections at all $(g,n)$ assembles into a
--
2413-defined from the MC element~$\Theta_\cA$, which depends on the
2414:choice of homotopy retraction data. The question is whether the
2415-output is independent of the input.
--
2855-propagator weight~$1$ couples to a single Hodge bundle
2856:$\mathbb{E}_1$. The question forced by the depth classification
2857-is whether the scalar formula survives the passage to multiple
--
3157-complex extracts its coefficients by residues from rational OPE
3158:data. The question is whether these rational numbers carry
3159-arithmetic meaning beyond their algebraic origin.
--

thinking
**Searching for placeholders**

I think I need to search for `---` placeholder lines in the tables, especially around line 2653 where I found another one with `rg`. I wonder if `\ldots` could be relevant too. Maybe I should check for double spaces in the text caused by line wrapping, although that might not be worth the effort. I feel I should compile everything to catch any undefined macros or environments that might exist.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '24,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    24	\noindent
    25	This monograph studies holomorphic chiral factorisation
    26	(co)homology via bar and cobar chain constructions at various
    27	geometric locations on algebraic curves. The geometry determines
    28	the operad: a curve~$X$ gives $\Einf$ (symmetric factorisation on
    29	the Ran space), ordered configurations on~$X$ give~$\Eone$
    30	(the associative chiral operad $\operatorname{Ass}^{\mathrm{ch}}$),
    31	and the product $\bC \times \bR$ gives the holomorphic-topological
    32	Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$. Each operad
    33	determines a bar complex; the bar complex computes the
    34	factorisation (co)homology. The five theorems of this volume
    35	are structural properties of the result at each level.
    36	
    37	\medskip
    38	
    39	\noindent
    40	The computational engine is the ordered bar complex
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2166,2172p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2412,2418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2332,2338p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3157,3200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3322,3326p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2853,2858p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3933,3936p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3466,3469p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2332	
  2333	The three projections ($\kappa$, $\Delta_\cA$,
  2334	$\mathfrak{R}^{\mathrm{mod}}_4$) capture the shadow data at
  2335	degrees $2$, $2$, and $4$. The question is whether the full
  2336	collection of projections at all $(g,n)$ assembles into a
  2337	cohomological field theory.
  2338	
 succeeded in 52ms:
  2412	The characteristic classes of~\S5.1 and the CohFT of~\S5.3 are
  2413	defined from the MC element~$\Theta_\cA$, which depends on the
  2414	choice of homotopy retraction data. The question is whether the
  2415	output is independent of the input.
  2416	
  2417	The shadow algebra
  2418	$\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
 succeeded in 52ms:
  2166	\noindent
  2167	Section~4 constructed a universal Maurer--Cartan element
  2168	$\Theta_\cA$ from which every invariant projects. The question is
  2169	what those projections are: what characteristic classes does the
  2170	modular bar bundle carry?
  2171	
  2172	\subsection*{5.1.\enspace Three characteristic projections}
 succeeded in 52ms:
  3322	
  3323	Scalar saturation establishes that $\kappa$ controls the MC
  3324	element at degree~$2$. The question is what controls it at
  3325	\emph{all} degrees. The answer is the Koszul condition: bar
  3326	cohomology concentrated in degree~$1$.
 succeeded in 52ms:
  3466	The Hilbert polynomials measure the algebra's deformation ring.
  3467	The question is what \emph{generates} the bar differential that
  3468	produces these cohomology groups: the answer, at genus~$0$, is
  3469	the BRST operator.
 succeeded in 52ms:
  3933	Arnold on $\operatorname{FM}_3(\mathbb C)$. All of this is tree-level.
  3934	The question is whether the tree-level PVA extends to a quantum
  3935	algebra at genus~$g\ge 1$, and the answer is controlled by an
  3936	obstruction theory whose structure mirrors the geometry of stable
 succeeded in 52ms:
  2853	The Virasoro algebra has a single generator of weight~$2$. The
  2854	scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
  2855	propagator weight~$1$ couples to a single Hodge bundle
  2856	$\mathbb{E}_1$. The question forced by the depth classification
  2857	is whether the scalar formula survives the passage to multiple
  2858	generators at different conformal weights.
 succeeded in 52ms:
  3157	complex extracts its coefficients by residues from rational OPE
  3158	data. The question is whether these rational numbers carry
  3159	arithmetic meaning beyond their algebraic origin.
  3160	
  3161	\subsection*{8.1.\enspace The shadow Eisenstein theorem}
  3162	
  3163	At genus~$1$, the bar complex over a family of elliptic curves
  3164	$\cC_\tau\to\mathfrak H$ produces the amplitude
  3165	$\mathrm{Sh}_2^{(1)}(\cA,\tau)=\kappa(\cA)\cdot E_2^*(\tau)$,
  3166	where $E_2^*(\tau)=1-24\sum_{n\ge 1}\sigma_1(n)\,q^n$ is the
  3167	quasi-modular Eisenstein series (not holomorphic: the
  3168	non-holomorphic completion absorbs the anomaly from
  3169	$d\log E(z,w)$). The Fourier coefficients $\sigma_1(n)$ are
  3170	divisor sums, and their Dirichlet series is a product of
  3171	Riemann zeta functions:
  3172	\[
  3173	D_2(\cA,s)
  3174	\;:=\;
  3175	\sum_{n\ge 1}\sigma_1(n)\,n^{-s}
  3176	\;=\;
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3288,3297p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3288	standard family is chirally Koszul. Heisenberg (class~G) is
  3289	Koszul. Affine Kac--Moody (class~L) is Koszul. The
  3290	$\beta\gamma$ system (class~C) is Koszul. The Virasoro algebra
  3291	(class~M), with its infinite shadow tower and its irremovable
  3292	quintic forcing, is Koszul. What property do they share that the
  3293	depth classification does not see?
  3294	
  3295	The answer is concentration: the bar cohomology
  3296	$H^*(\barB^{\mathrm{ord}}(\cA))$ sits in bar degree~$1$. When
  3297	this holds, the bar-cobar spectral sequence collapses, the




thinking
**Assessing redundancy in sections**

I need to evaluate potential redundancy in section 10 of Volume II, especially regarding the definitions of bar complex and the five theorems. It seems there's a lot of duplication, like the summary of the five theorems appearing twice. I notice specific lines repeating similar content, such as across various theorems. I could point out several redundancy clusters, focusing on key findings without covering every single duplicate. Also, I might revise the "Read together" line for clarity.
thinking
**Considering exact fixes for redundancy**

I’m contemplating a straightforward way to address the redundancy issue. Perhaps I could delete lines 1200-1264 and replace them with just one concise sentence. I'd need to think carefully about the exact rewrite to maintain clarity. For the content in lines 2117-2125, I could either delete that and keep the table or choose to keep the content and remove the table. It’s a balancing act to ensure the final version remains coherent!
thinking
**Deciding on output format**

I'm working on how to present the output for the user's request. They want a precise line number, but multiple entries could be useful. I'm considering if I can create clusters of related issues. Maybe I should list each line as a bullet point while ensuring it's clear and manageable—like maybe 10 bullets. 

I need to focus on the critical severity of issues using a scale, identifying which ones might break the build.
thinking
**Assessing notation issues**

I'm examining the notation drift caused by bare kappa, which I think is a medium to high concern. Since the user is looking for harsh critiques, the undefined macro `\Bbbk` feels critical because it could lead to compilation errors. I also see potential issues in line 106-107 with a broken theorem and maybe high worries about chapter openings.

Other issues, like table placeholders and question signposts, seem less severe. I might need to gather more evidence on `\Bbbk` and confirm definitions like `\mathbb` for consistency.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3728,3744p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3728	
  3729	\bigskip
  3730	
  3731	\noindent\textbf{The open/closed world (Volume~II).}
  3732	Volume~II lifts the bar complex to three dimensions. On the product
  3733	$\mathbb C_z \times \mathbb R_t$, the bar complex $\barB(\cA)$ is a
  3734	single-coloured $\Eone$-chiral dg coalgebra over
  3735	$(\mathrm{ChirAss})^!$: its differential extracts OPE residues from
  3736	collisions in the holomorphic plane, and its deconcatenation coproduct
  3737	is the cofree coassociative structure on the desuspended augmentation
  3738	ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
  3739	pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$, not the bar
  3740	complex itself: the two-colour open/closed structure emerges when the
  3741	bar complex is fed into the Hochschild construction.
  3742	
  3743	The primitive object of three-dimensional holomorphic-topological
  3744	quantum field theory on $\mathbb C_z \times \mathbb R_t$ is the




thinking
**Clarifying table usage**

I'm considering whether to keep the table or have a one-sentence reminder, but I shouldn't have both. The line about importing details from 3731-4201 into Volume I preface seems clear. It’s just about deciding how best to present this information without redundancy. I want to make sure it's straightforward for anyone reviewing it! Let’s keep it simple!
thinking
**Finalizing structural findings**

I'm going through key structural findings and notation. There are about 25 bullet points to review, which should fit within 30 lines. I need to make specific changes for each signpost, like at 2168 where I’ll say, "These projections are the characteristic classes of the modular bar bundle" or consider an alternative phrasing. I’m also refining other sections to ensure clarity around key concepts, transitioning smoothly with accurate claims and relevant details. This looks like it's coming together nicely!
thinking
**Updating key notations**

Looks like I need to update section 3197. I’ll replace the current text with, "The shadow tower instead carries non-automorphic arithmetic, detected by the Polyakov correspondence below." This change should clarify the point being made and ensure it ties in well with the surrounding content. I want to make sure my wording is precise and clearly communicates the idea to readers. It's essential to have everything align nicely!
thinking
**Organizing severity levels**

I'm thinking about organizing the issues I have by severity. 

For critical issues, I have a build break and a possible scope bleed in Volume II. The high-severity problems include a failure related to opening deficiencies and redundancy clusters. Then there are medium issues with kappa clusters and signposts, plus a spacing issue before a semicolon. 

For low priority, it seems there's nothing else. I wonder if line spacing at 673 is connected to a potential issue at line 1250, but it may not be necessary to check.
exec
/bin/zsh -lc "rg -n ' ;| ,| \\.|\\) :' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
673:$F_1 = \kappa(\cH_k)/24 = k/24$ ;
898:$\omega(z_1,z_2) := d_{z_1}\log E(z_1,z_2)$
971:\kappa(\cA) := \mathrm{av}\bigl(r_\cA(z)\bigr).





thinking
**Examining content details**

I’m looking at line 673, which seems strange. I might want to check if line 971's `:=` is okay — it doesn't seem to be an issue. I could also search for double spaces, but maybe that's not needed. There’s a thought about the table headers for lines 3035 and 3039 needing bare kappa, but maybe that’s fine since the column labels are pretty generic as the user requested. I'll consider flagging clusters with bare kappa as equations or numeric invariants and check `\Omega/z` for any issues.
thinking
**Reviewing conventions and redundancies**

I'm considering whether line 4054 follows the KZ convention and not bare — it seems fine. I should also check if line 1606, referring to `B_\kappa \dashv \Omega_\kappa`, isn't indicating a modular characteristic, which seems okay. There might be a need to verify if there are any `---` in the comments, but that doesn't seem like an issue. 

I notice potential redundancy in theorem phrasing; for instance, Theorem C starts with "derived chiral centre" and later uses different wording in the description. This might create confusion, and I’ll need to find the exact fix by comparing lines 101-105 with 1219-1224 and 2119-2122.
thinking
**Addressing theorem formulations**

I've noticed that the same theorem surface is being presented under different names, like derived center decomposition, genus-g cohomology, and Theta decomposition. To fix this, I should select one formulation in the preface and ensure it’s cited consistently throughout the work — that's a subtle but effective approach. I could apply the same strategy to Theorem D and possibly Theorem H. I’ll need to be attentive to these details to maintain clarity.
thinking
**Evaluating theorems for redundancy**

I’m considering the drift for Theorem C as the best option. Theorem H might be okay, but I could find redundancy on the surface lines noted. Since the user asked about redundancy across multiple wordings, I should report at least one finding. The duplication of some lines could also indicate redundancy. I might look into moving certain discussions to the introduction or preface to enhance clarity and avoid feeling stacked at the end.
thinking
**Identifying redundancy and clarity**

I’m considering whether I should flag certain elements as redundant. For instance, line 4230 seems fine, but I’m unsure about line 4271, which mentions verification by an independent symbolic computation layer. It comes off as somewhat boastful, like a "build/evidence bragging." I wonder if this could be seen as a substantial issue rather than just cosmetic. It’s important to strike the right balance between information and clarity in the presentation!
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2116,2125p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2116	The existence of~$\Theta_\cA$ is encoded by the bar-cobar
  2117	adjunction: Theorem~A constructs the arena in which~$\Theta_\cA$
  2118	lives. Bar-cobar inversion proves that~$\Theta_\cA$ is a complete
  2119	invariant: Theorem~B recovers~$\cA$ from~$\Theta_\cA$. Verdier
  2120	duality decomposes~$\Theta_\cA$ into complementary halves: Theorem~C
  2121	splits the genus tower into Lagrangian summands. The leading
  2122	coefficient of~$\Theta_\cA$ is the modular characteristic: Theorem~D
  2123	extracts the scalar $\kappa(\cA)$ with $\hat A$-genus generating
  2124	function. The coefficient ring of~$\Theta_\cA$ is the chiral
  2125	Hochschild complex: Theorem~H identifies the deformation ring.

thinking
**Evaluating theorem adjustments**

I'm considering adjustments to Theorem C. There might be a duplication issue between clusters 94 and 1204, and I need to figure out the exact lines. I think we could fix section 2 by possibly keeping just one sentence. It's worth contemplating whether to separate the concepts of drift and duplication. 

We could list the entire duplicate theorem from 1204-1253 and identify the drift within specific ranges in Theorem C. I'll need to check more specific lines to clarify things.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '4216,4267p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4216	\noindent\textbf{The boxed machine.}
  4217	The entire construction can be stated in a single pipeline:
  4218	\[
  4219	\boxed{
  4220	\text{homotopy chiral input }\cA
  4221	\;+\;
  4222	\text{log-FM cutting cooperad }\mathcal C^!_{\mathrm{ch}}
  4223	\;+\;
  4224	\text{modular convolution }L_\infty
  4225	\;\;\Longrightarrow\;\;
  4226	\Theta_\cA,\;
  4227	\mathcal T^{\mathrm{mod}}_{\Theta_\cA},\;
  4228	\kappa,\;
  4229	\Delta_\cA,\;
  4230	\mathfrak R^{\mathrm{mod}}_4,\;\ldots
  4231	}
  4232	\]
  4233	
  4234	\noindent
  4235	The modular convolution $L_\infty$-algebra



thinking
**Evaluating redundancy and clarity**

I’m noticing some redundancy in my work. I could streamline things by focusing on just the essential sentences. I need to check section 2 for possible improvements. There’s a line about structural properties that might duplicate later, but it doesn’t seem problematic. I should also consider how to clarify rhetorical questions and if certain terminology, like "class-M," is used correctly. There are a few signposts that could be refined for better readability too!
thinking
**Checking macro consistency**

I need to spot a notation inconsistency between line 3570, where `\SCchtop` is defined as `\mathsf{SC}^{\mathrm{ch,top}}`, and its earlier usage in line 32, which uses `\mathrm{SC}^{\mathrm{ch,top}}`. It looks like there’s inconsistent macro usage throughout. I’ve noticed similar issues with `E_\infty` versus `\Einf` and `E_1` versus `\Eone`. The user raised a good point about whether macros are used consistently, and they’re not! I should look for more raw forms.
thinking
**Addressing aesthetic inconsistency**

I see there might be an inconsistency in the aesthetics regarding macros. The user specifically asks for macro consistency, so I should point out the exact lines needing correction. For instance, in lines 31-32, they use `\mathrm{SC}^{\mathrm{ch,top}}`, while in line 3570 and beyond, it switches to `\SCchtop`. To fix this, I’ll recommend replacing line 32 with `$\SCchtop$`. Additionally, lines 573, 610, and 681 use `\mathcal H_k`, while lines 673, 1242, and 2756 use `\cH_k`. I should standardize on `\cH_k` throughout the preface and check how many occurrences there are. It seems worth the effort!
exec
/bin/zsh -lc "rg -n '\\\\mathcal H_k|\\\\cH_k' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathrm\\{SC\\}\\"'^'"\\{\\\\mathrm\\{ch,top\\}\\}|\\\\SCchtop' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathfrak g|\\\\fg' chapters/frame/preface.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
32:Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$. Each operad
3570:\subsection*{10.2.\enspace The $\SCchtop$ intermediary}
3573:Swiss-cheese operad~$\SCchtop$: a two-coloured operad with
3577:($\SCchtop(\ldots,\mathrm{top},\ldots;\mathrm{ch})
3580:The operad $\SCchtop$ is \emph{not} $E_3$. Dunn additivity
3582:operads; the two-coloured $\SCchtop$ does not factor as a
3583:tensor product. The passage from $\SCchtop$ to $E_3$
3594:\SCchtop\text{-}\mathsf{alg}
3606:conformal vector ceases to exist, and the $\SCchtop$-algebra
3609:$\SCchtop$ stage.
3622:\item a double $A_\infty$-structure on the $\SCchtop$-cohomology
3738:ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
3786:The operad $\SCchtop$ is homotopy-Koszul (proved). The operation spaces
3787:are $\SCchtop(\mathrm{ch}^k;\mathrm{ch})=\operatorname{FM}_k(\mathbb C)$,
3788:$\SCchtop(\mathrm{ch}^k,\mathrm{top}^m;\mathrm{top})
3790:$\SCchtop(\ldots,\mathrm{top},\ldots;\mathrm{ch})=\varnothing$:
3791:open-to-closed is forbidden. An $\SCchtop$-operation of degree~$(k,m)$
3800:The $\SCchtop$ structure emerges on the derived center pair
3803:quasi-isomorphism $\Phi\colon\SCchtop\xrightarrow{\sim}\mathsf{SC}$ from
3805:and the bar-cobar adjunction on $\SCchtop$-algebras is a Quillen
 succeeded in 51ms:
573:The Heisenberg chiral algebra $\mathcal H_k$ is generated by a
588:\barB^n_X(\mathcal H_k)
610:$\kappa(\mathcal H_k) = k$.
613:\mathcal H_k^!
626:The ordered bar complex $\barB^{\mathrm{ord}}(\mathcal H_k)$
638:\;=\; \kappa(\mathcal H_k).
657:\cZ^{\mathrm{der}}_{\mathrm{ch}}(\mathcal H_k)
671:The modular characteristic $\kappa(\mathcal H_k) = k$ is the
673:$F_1 = \kappa(\cH_k)/24 = k/24$ ;
676:pole, so $S_r(\mathcal H_k)=0$ for all $r\ge 3$. Class~G
681:\mathcal H_k^!
685:\kappa(\mathcal H_k)+\kappa(\mathcal H_k^!) = k + (-k) = 0.
688:$U_{\mathcal H_k} = \mathcal H_k \bowtie \mathcal H_k^!$ reduces
689:to $\mathcal H_k\otimes\mathcal H_{-k}$ modulo the diagonal,
977:$\kappa(\mathcal H_k) = k$;\;
1242:$P_{\cH_k}(t)=1+t+t^2$ for Heisenberg,
2205:Heisenberg $\cH_k$ & $k$ & $-k$ & $0$\\[2pt]
2557: & Heisenberg $\cH_k$, free fermion\\
2652:\textbf{Heisenberg} $\cH_k$
2756:The Heisenberg algebra $\cH_k$ (Section~1) is the base case.
 succeeded in 51ms:
14:\providecommand{\fg}{\mathfrak{g}}
700:The affine Kac--Moody algebra $\widehat{\mathfrak g}_k$ at
702:$J^a$, $a = 1,\dots,\dim\mathfrak g$, with OPE
711:algebra~$\mathfrak g$ and $\kappa^{ab}$ is the Killing form
718:The bar complex of $\widehat{\mathfrak g}_k$ has nontrivial
734:product supplies the curvature~$\kappa(\widehat{\fg}_k)$. The coexistence of both
736:$\widehat{\mathfrak g}_k$ the first nontrivial example.
740:The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
747:where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
756:\operatorname{av}\bigl(r(z)\bigr) \;+\; \tfrac{\dim(\mathfrak g)}{2}
758:\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
760:\kappa(\widehat{\mathfrak g}_k),
762:where the additive $\dim(\mathfrak g)/2$ is the Sugawara
765:vanishes and $\kappa(\widehat{\mathfrak g}_k) = 0$. The matrix
767:the representation theory of~$\mathfrak g$. At this point the
770:$\kappa(\widehat{\mathfrak g}_k)$ discards the Casimir tensor,
771:which is precisely the datum that builds the Yangian~$Y(\mathfrak g)$.
774:that deforms the enveloping algebra $U(\mathfrak g[z])$ of
776:dual $\widehat{\mathfrak g}_k^!$, the Verdier-dual factorization
978:$\kappa(\widehat{\fg}_k) = (k{+}h^\vee)\dim\fg/(2h^\vee)$,





thinking
**Evaluating macro usage**

I need to check if the `\Einf` macro outputs correctly as `\mathsf{E}_{\infty}` while also considering `\Eone` which refers to `$E_1`. The main issue seems to be that while `\Eone` is defined as `\mathsf`, there are multiple raw `$E_1$` usages instead of `\Eone`. The user wants macro consistency, so I might mention this issue. However, not all symbols in the preface need to be macro since it's largely manually written math. I'll focus on the more glaring macro inconsistencies.
thinking
**Checking bullet counts and formatting**

I need to make sure there’s no em dash, only the three hyphens. I might mention the "Checked: 4374 | Findings: 15" data. I’ve counted the bullets: there’s 1 critical, 7 high, 6 medium, and 1 low, totaling 15. Great, I double-checked, and it still adds up! I’m considering if bullet 4216 and bullet 3731 should be highlighted. Also, the macro consistency bullet could be low instead of medium. I'll include the lines in the header.
thinking
**Formatting audit findings**

I’m thinking about how to present audit findings. It looks like I need to avoid nested bullets and keep things simple. The developer prefers short paragraphs, which makes sense. I could output each finding on its own line, totaling around 18 lines plus a summary, which is manageable. I might use monospace for code symbols, and maybe backticks could help clarify problems and fixes. I want to make everything concise yet precise, especially with replacements for consistency.
thinking
**Refining replacement instructions**

I’m thinking about how to shorten the replacement instructions for mathematical symbols. I want to make sure to replace every instance of `\mathcal H_k` with `\cH_k`, and for `\mathfrak g` or `\widehat{\mathfrak g}_k`, I'll use `\fg` or `\widehat{\fg}_k`. I should also mention the exact replacement for line 32. It might help to list specific phrases for other lines, like 2856 and 3197, to keep everything clear and precise. Plus, line 3292 needs its exact fix noted too.
thinking
**Finalizing replacement details**

I’m considering replacements for specific lines, like line 3324 and 3325, which should read: "The full MC element is controlled by the Koszul condition: bar cohomology concentrated in degree1." Lines 3467 and 3934 also need their replacements confirmed. For the final summary, I’ll format it as: "Checked: 4374 lines in chapters/frame/preface.tex | Findings: 15 | Verdict: FAIL." This aligns with the user contract, where "N" will likely be 4374. I want to ensure I keep bullet points concise—ideally no more than 70 lines total.
codex
- [CRITICAL] chapters/frame/preface.tex:833 — PROBLEM: `\Bbbk` is used on the live book surface before any definition appears in the main build, so this is an undefined-control-sequence risk, not a stylistic quirk. FIX: change `When $X=\operatorname{Spec}\Bbbk$ is a point` to `When $X=\operatorname{Spec}\mathbb{k}$ is a point`, or add `\providecommand{\Bbbk}{\mathbb{k}}` to the local macro block at lines 1–16.

- [HIGH] chapters/frame/preface.tex:25 — PROBLEM: the preface opening is descriptive instead of deficiency-first; it starts with “This monograph studies…” rather than the failure the book repairs. FIX: replace lines 25–27 with `Local OPE residue calculus sees one collision at a time; it does not organise singularities on $n$ points of a genus-$g$ curve into a global complex over moduli. This monograph resolves that defect by constructing bar and cobar chain complexes at the geometric levels relevant to chiral algebra on curves.` Then keep the existing operad list starting at `The geometry determines the operad:`.

- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`

- [HIGH] chapters/frame/preface.tex:101,1219,2120 — PROBLEM: Theorem~C drifts across three different objects: derived chiral centre, genus-$g$ cohomology of the center local system, and “the genus tower.” That is theorem-surface drift, not harmless rephrasing. FIX: keep lines 1219–1224 as the only theorem statement; rewrite lines 101–105 as `Theorem~C extracts this Lagrangian splitting from the derived chiral centre.`; rewrite lines 2120–2121 as `Under Theorem~C, the genus tower projects to these two Lagrangian summands.`

- [HIGH] chapters/frame/preface.tex:1198 — PROBLEM: the subsection `The five theorems` restates the full theorem list after the opening already did it, then lines 1257–1264 summarize the same list yet again. This is visible redundancy, not orientation. FIX: delete lines 1198–1264 and replace them with `Theorems~A--D and~H, stated in the body, are the five projections of the ordered bar used throughout the rest of this preface.`

- [HIGH] chapters/frame/preface.tex:2116 — PROBLEM: after the projection table at 2078–2108, lines 2116–2125 paraphrase the same mapping in prose. The table already does that work. FIX: delete lines 2116–2125 and replace them with `Table~5.1 records the five projections of $\Theta_\cA$ that organise the remainder of the preface.`

- [HIGH] chapters/frame/preface.tex:3731 — PROBLEM: `The open/closed world (Volume~II)` expands into a second preface inside the first; hundreds of lines of Volume II material swamp the Volume I close. FIX: replace lines 3731–4201 with `\noindent\textbf{Volume~II interface.} Volume~II studies the ordered data discarded by averaging: the spectral $R$-matrix, Yangian, open/closed extension, and the $\SCchtop$-governed derived-center pair. In this volume these appear only as outputs or conjectural extensions of the ordered bar; the three-dimensional holomorphic-topological constructions are deferred to Volume~II.`

- [HIGH] chapters/frame/preface.tex:4216 — PROBLEM: `The boxed machine` repeats the same summary function already performed by the projection table and earlier theorem summaries, then restates the box immediately in prose. FIX: keep the boxed display at 4218–4232; delete lines 4234–4267; replace them with `Everything in this preface is a projection of $\Theta_\cA$, with Theorems~A--D and~H extracting its scalar and low-degree shadows.`

- [MEDIUM] chapters/frame/preface.tex:32,573,700 — PROBLEM: macro use is inconsistent inside a single file. You mix raw `\mathrm{SC}^{\mathrm{ch,top}}` with `\SCchtop`, raw `\mathcal H_k` with `\cH_k`, and raw `\mathfrak g` with `\fg`. FIX: line 32 use `$\SCchtop$`; replace every listed `\mathcal H_k`/`\mathcal H_{-k}` occurrence with `\cH_k`/`\cH_{-k}`; replace every listed `\mathfrak g`/`\widehat{\mathfrak g}_k` occurrence with `\fg`/`\widehat{\fg}_k`.

- [MEDIUM] chapters/frame/preface.tex:1008,1020 — PROBLEM: the curvature formula drops from `\kappa(\cA)` to bare `\kappa` exactly where the symbol is used in equations. FIX: line 1008 `the fibrewise curvature $\kappa(\cA)\cdot\omega_g$`; line 1020 `\kappa(\cA)\cdot\omega_g-\kappa(\cA)\cdot\omega_g+0`.

- [MEDIUM] chapters/frame/preface.tex:1097,1101,1103 — PROBLEM: the discriminant paragraph repeats the same notation drift: bare `\kappa` and bare `S_4` in a generic formula. FIX: write `\Delta(\cA)=8\,\kappa(\cA)\,S_4(\cA)`, `\kappa(\cA)\cdot\lambda_g`, and `(\kappa(\cA),\alpha(\cA),S_4(\cA))`.

- [MEDIUM] chapters/frame/preface.tex:2511,2514,2517,2675 — PROBLEM: the algebraicity section uses bare `\kappa` even though the object is a primary line `L`; the notation should be line-indexed there. FIX: introduce `\kappa_L:=\kappa(\cA_L)`, `\alpha_L:=\alpha(\cA_L)`, `S_{4,L}:=S_4(\cA_L)`, then rewrite `Q_L(t)=4\kappa_L^2+12\kappa_L\alpha_L\,t+(9\alpha_L^2+16\kappa_LS_{4,L})t^2`, `(\kappa_L,\alpha_L,S_{4,L})`, `\Delta_L=8\kappa_LS_{4,L}`, and `\rho(\cA)=\sqrt{9\alpha_L^2+2\Delta_L}/(2|\kappa_L|)`.

- [MEDIUM] chapters/frame/preface.tex:2854,2968,3128,3135,3319,3478,4264 — PROBLEM: later sections never stabilize the modular-characteristic notation; the file keeps oscillating between explicit family notation and bare `\kappa`. FIX: use `\kappa(\cA)` in generic formulas, and family-tagged forms in family passages: `\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g`, `F_g(\beta\gamma_\lambda)=\kappa(\beta\gamma_\lambda)\cdot\lambda_g^{\mathrm{FP}}`, `\kappa(\cA)+\kappa(\cA^!)`, `\Theta_\cA^{\min}=\kappa(\cA)\cdot\eta\otimes\Lambda`, `d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_1`, and `the scalar projection~$\kappa(\cA)$`.

- [MEDIUM] chapters/frame/preface.tex:2168,2335,2414,2856,3158,3197,3292,3324,3467,3934 — PROBLEM: these transitions are pure signpost rhetoric (`The question is...`, `The answer is...`) instead of mathematically forced transitions. FIX: replace them with direct statements: 2168 `These projections are the characteristic classes of the modular bar bundle.`; 2335 `These projections assemble into a CohFT once the MC equation is pushed to $\overline{\cM}_{g,n+1}$.`; 2414 `The output is independent of the retraction data up to MC gauge equivalence.`; 2856 `Multiple conformal weights are precisely where the scalar formula can fail.`; 3158 `These rational numbers acquire arithmetic meaning through the genus-one Eisenstein channel.`; 3197 `The shadow tower instead carries non-automorphic arithmetic, detected by the shadow $L$-function and the Polyakov bridge.`; 3292 `What the four classes share is concentration of bar cohomology in bar degree~$1$.`; 3324 `The full MC element is controlled by the Koszul condition.`; 3467 `At genus~$0$, the BRST operator generates the bar differential computing these groups.`; 3934 `Higher-genus quantization is governed by the obstruction theory of node degenerations.`

- [MEDIUM] chapters/frame/preface.tex:2653,2655,2657,3112 — PROBLEM: table cells use `---` as placeholders. In this repo that collides with the em-dash blacklist, and here it also fails to say whether the entry is zero, absent, or not applicable. FIX: replace the 2653/2655/2657 placeholders with `\text{no}` and the 3112 placeholder with `\text{n/a}` or the actual invariant if one is intended.

- [LOW] chapters/frame/preface.tex:673 — PROBLEM: there is a stray space before the semicolon in `$F_1 = \kappa(\cH_k)/24 = k/24$ ;`. FIX: change it to `$F_1 = \kappa(\cH_k)/24 = k/24$.`

## Summary
Checked: 4374 | Findings: 15 | Verdict: FAIL
tokens used
162,184
