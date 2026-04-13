# A01_koszul_pairs_rect (291s)

Edited [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex).

FIXED 1: Koszul equivalence `(vii)` is now explicitly genus-0 only in the theorem statement, not just in the proof. See [chiral_koszul_pairs.tex:2022](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2022) and [chiral_koszul_pairs.tex:2053](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2053).

FIXED 2: Koszul equivalence `(viii)` is now explicitly one-way, matching the proved Hochschild content rather than an equivalence. I also synced the earlier summary count from `10` unconditional equivalences to `9 + 1 + 1 + 1`. See [chiral_koszul_pairs.tex:1199](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1199), [chiral_koszul_pairs.tex:2024](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2024), and [chiral_koszul_pairs.tex:2064](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2064).

FIXED 3: The SC-formality converse now states that it uses only the class-by-class non-formality proposition, not any invalid `\kappa`-based trilinear-form argument. See [chiral_koszul_pairs.tex:2598](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2598).

Verification: I re-read the touched ranges, made no `\label` or `\ref` changes, and grep-confirmed the modified file no longer contains the stale `ten proved unconditionally equivalent` phrasing or any `\kappa(x,[y,z])` surface. No blockers.


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
session id: 019d862a-da51-7193-b497-908e8639475c
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/theory/chiral_koszul_pairs.tex

This is the LARGEST theory file. The previous rectification agent timed out.
Focus on the THREE most critical fixes only (do not try to rewrite the whole file):

1. Koszul equivalence (vii): currently listed as unconditional but proof only covers g=0.
   FIX: Move (vii) to conditional equivalences OR add "at genus 0" qualifier.

2. Koszul equivalence (viii): claims ChirHoch is free polynomial algebra, but Hochschild
   theorems only prove duality + concentration. FIX: Weaken (viii) to match proved content.

3. SC-formality converse: uses bilinear form C(x,y,z)=kappa(x,[y,z]) but kappa is scalar.
   FIX: Restrict to families with invariant bilinear form (KM, not betagamma).

Read the relevant sections ONLY (search for 'equiv' and 'SC-formal'). Do not read the whole file.
mcp startup: no servers

thinking
**Deciding on methods for search**

I’m thinking about the instructions that say to prefer automated tools over manual searches or file reading. This is a codebase question, but the user has asked us to read relevant sections. I might still use the explorer to efficiently search for authoritative code. Yet, I’m questioning if it’s necessary for something simple. Ultimately, I think using the explorer agent will help locate occurrences and any relevant context in a more efficient way.
codex
Using `beilinson-rectify` for a tightly scoped mathematical repair. I’m locating the exact `equiv` and `SC-formal` surfaces in the assigned file, plus the minimal concordance/registry context needed to keep the edit truthful and status-consistent.
exec
/bin/zsh -lc 'rg -n "equiv|SC-formal|sc-formal|formality|ChirHoch|genus 0|genus-zero|genus-zero|Koszul" chapters/theory/chiral_koszul_pairs.tex CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md .agents/skills/beilinson-rectify/SKILL.md' in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
Total output lines: 1371

rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
metadata/theorem_registry.md:94:| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1156 | Heisenberg Koszul dual |
metadata/theorem_registry.md:145:| `cor:completion-closure-equivalence` | `corollary` | 1782 | Homotopy-categorical equivalence on the completion closure |
metadata/theorem_registry.md:181:| `cor:winfty-dual-candidate-construction` | `corollary` | 3279 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
metadata/theorem_registry.md:186:| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3596 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
metadata/theorem_registry.md:221:| `thm:genus-zero-strict` | `theorem` | 6039 | Strict nilpotence at genus zero |
metadata/theorem_registry.md:227:| `thm:recognition-koszul-pairs` | `theorem` | 6689 | Recognition theorem for finite chiral Koszul pairs |
metadata/theorem_registry.md:251:| `thm:positselski-chiral-proved` | `theorem` | 1441 | Positselski equivalence for the chiral bar coalgebra |
metadata/theorem_registry.md:252:| `thm:full-derived-module-equiv-proved` | `theorem` | 1498 | Flat finite-type reduction on the completed-dual side |
metadata/theorem_registry.md:261:| `cor:completed-derived-equivalence` | `corollary` | 2358 | Completed derived equivalence |
metadata/theorem_registry.md:262:| `thm:barr-beck-lurie-koszulness` | `theorem` | 2470 | Barr--Beck--Lurie characterization of chiral Koszulness |
metadata/theorem_registry.md:350:| `thm:main-koszul-hoch` | `theorem` | 578 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
metadata/theorem_registry.md:353:| `prop:e2-formality-hochschild` | `proposition` | 829 | $\Etwo$-formality of chiral Hochschild cohomology |
metadata/theorem_registry.md:354:| `thm:convolution-formality-one-channel` | `theorem` | 909 | Scalar universal class implies convolution formality along its distinguished orbit |
metadata/theorem_registry.md:379:| `prop:periodicity-exchange-koszul` | `proposition` | 4441 | Periodicity-profile transport under Koszul duality |
metadata/theorem_registry.md:382:| `ver:boson-fermion-HH` | `verification` | 4817 | $bc$/$\beta\gamma$ Koszul duality |
metadata/theorem_registry.md:395:| `thm:pbw-koszulness-criterion` | `theorem` | 682 | PBW criterion for chiral Koszulness |
metadata/theorem_registry.md:396:| `thm:km-chiral-koszul` | `theorem` | 760 | Affine Kac--Moody algebras are chiral Koszul |

thinking
**Planning file searches**

I'm thinking the output from the search is huge, but I still need to extract relevant lines from the target file, maybe using `rg` to locate sections and find a corresponding concordance. I should also check the red_team_summary path in the archive. It might be helpful to utilize the explorer agent, but I've already used exec, so no worries there. I should send an update and adjust my plan, possibly mentioning reading the skill file. Using `sed -n` could help narrow down relevant line ranges around the theorem and proposition based on patterns in the target file.
codex
I’ve narrowed the work to the theorem listing the equivalences and the SC-formality proposition/proof. Next I’m reading only those local ranges, plus the matching concordance/registry entries, to decide the minimum wording change that matches what is actually proved.
Plan update
Scoped to the three audit findings in one file. I’m reading only the theorem/proposition surfaces and their status context, then making minimal local edits and verifying the modified surface for forbidden drift.
  → Locate the exact equivalence items (vii), (viii) and the SC-formality converse in the assigned file, plus matching registry/concordance context
  • Apply the minimum truthful edits in chapters/theory/chiral_koszul_pairs.tex
  • Re-read the edited ranges and grep the modified file for forbidden patterns relevant to the changes

thinking
**Considering code execution**

I need to read a skill file snippet that's relevant. To do that, I could use `sed` on the skill file and target file to focus on specific sections. Maybe I can also implement `multi_tool_use.parallel` with `exec_command`, since it can only use developer tools. I should get the line numbers first using `rg -n` with the exact label to set the ranges for my commands. Let's work through this!
exec
/bin/zsh -lc 'rg -n "thm:koszul-equivalences-meta|SC-formal|sc-formal|prop:sc-formal-iff-class-g|prop:swiss-cheese-nonformality-by-class|equiv|ChirHoch" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:koszul-equivalences-meta|prop:sc-formal-iff-class-g|prop:swiss-cheese-nonformality-by-class" chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
61:Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
63:unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
89:(Heisenberg and its relatives) is SC-formal
90:(Proposition~\ref{prop:sc-formal-iff-class-g}).
241:\emph{equivalent} to $(d_\cA + d_\cC + d_\tau^L)^2 = 0$
321:$\eta_\tau$ is a weak equivalence.
365:If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
392:equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
410:the following are equivalent:
422: is a weak equivalence of conilpotent complete factorization
431:The equivalence follows the same logical structure as the
442:Acyclicity of $K_\tau^L$ is therefore equivalent to
448:Acyclicity of $K_\tau^R$ is therefore equivalent to
449:$\eta_\tau$ being a weak equivalence.
461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
504:MC equation for $\tau$ is equivalent to $g_\tau$ commuting
757:(equivalently, a vertex Poisson algebra).
1195:determined by its binary part; equivalently, all genus-$0$
1199:Koszulness (ten proved unconditionally equivalent, one conditional on
1252:$m_n = 0$ for $n \geq 3$ is equivalent to $E_2 = E_\infty$, which
 succeeded in 52ms:
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
metadata/theorem_registry.md:409:| `thm:koszul-equivalences-meta` | `theorem` | 1908 | Equivalences of chiral Koszulness |
metadata/theorem_registry.md:411:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2358 | Swiss-cheese non-formality by shadow class |
metadata/theorem_registry.md:412:| `prop:sc-formal-iff-class-g` | `proposition` | 2455 | SC-formality characterises class~$G$ |
chapters/connections/concordance.tex:1992:Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
chapters/connections/concordance.tex:2385:Theorem~\ref{thm:koszul-equivalences-meta} in
chapters/connections/concordance.tex:3156: & \texttt{thm:koszul-equivalences-meta}
chapters/connections/concordance.tex:7073:\ref{prop:sc-formal-iff-class-g}
chapters/connections/concordance.tex:7076: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
chapters/connections/concordance.tex:9601: \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
chapters/connections/concordance.tex:9648: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} \\
chapters/connections/concordance.tex:9719: Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
chapters/connections/concordance.tex:10221: (item~(xii) of Theorem~\ref{thm:koszul-equivalences-meta}).
codex
The theorem surface is at `thm:koszul-equivalences-meta`, and the SC-formality converse sits in `prop:sc-formal-iff-class-g`. I’m reading the item text and the proof paragraphs where those items are justified, because that is where the overclaim needs to be narrowed rather than rewritten globally.
exec
/bin/zsh -lc "sed -n '1998,2074p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2178,2260p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7066,7082p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2458,2602p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
filtration level~$p$, and the Poisson bracket determines
whether this relation propagates to the bar complex via~$d_1$.
The Shapovalov criterion asks: are there null vectors in the
bar-relevant range? The Li--bar criterion asks: does the
\emph{geometry} of the associated variety~$X_V$ force those
null vectors to produce off-diagonal bar cohomology?

The gain is maximal when $X_V \neq \{0\}$ and one can
separately establish diagonal concentration on the reduced
Li--bar page, possibly guided by geometric input from a
symplectic resolution. Minimal-orbit levels are the first
test case where the reduced geometry suggests concentration, but
an unconditional Koszul theorem still requires the extra
reducedness and reduced Li--bar concentration hypotheses recorded in
Corollary~\ref{cor:minimal-orbit-koszul}.
\end{remark}

\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}
 succeeded in 52ms:
homology $\int_{\mathbb{P}^1}\cA$ is computed by the bar complex:
$\int_{\mathbb{P}^1}\cA \simeq |\barBgeom(\cA)|$, the geometric
realization. Concentration in degree~$0$ means the bar spectral
sequence computing $H^*(\int_{\mathbb{P}^1}\cA)$ collapses, which
by Theorem~\ref{thm:pbw-koszulness-criterion} is Koszulness.

\begin{remark}[Scope of factorization-homology concentration]
\label{rem:fh-vii-uniform-weight-scope}
Condition~\textup{(vii)} is asserted at $g = 0$ unconditionally and
at $g \geq 1$ only on the uniform-weight lane. The
class~M Virasoro example shows that the all-genera version is
strictly stronger than Koszulness: $\mathrm{Vir}_c$ is chirally
Koszul (Theorem~\ref{thm:virasoro-chiral-koszul}) but its
multi-weight higher-genus factorization homology carries
nonvanishing cross-channel corrections $\delta F_g^{\mathrm{cross}}$
that obstruct degree-$0$ concentration. The intended unconditional
equivalence (i)$\Leftrightarrow$(vii) is therefore the
\emph{$g = 0$ specialization}; the full all-genera version is
recovered as a Koszulness $+$ uniform-weight conjunction.
\end{remark}
 succeeded in 52ms:
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: structural propositions and depth classification}} \\
\hline
\ref{prop:sc-formal-iff-class-g}
 & SC-formality characterises class~$\mathbf{G}$:
 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
 & abelian bracket $+$ nondegeneracy of~$\kappa$ \\
\ref{prop:depth-gap-trichotomy}
 & Algebraic depth gap:
 $d_{\mathrm{alg}}(\cA) \in \{0,\,1,\,2,\,\infty\}$,
 no finite $d_{\mathrm{alg}} \geq 3$ realized
 \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)}
 succeeded in 52ms:
This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
\end{remark}

\begin{proposition}[Swiss-cheese non-formality by shadow class; \ClaimStatusProvedHere]
\label{prop:swiss-cheese-nonformality-by-class}
\index{Swiss-cheese operad!non-formality by shadow class|textbf}
\index{shadow depth!Swiss-cheese formality}
\index{Ainfty@$A_\infty$!non-formality for class M}
The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
\textup{(}not on the bar cohomology $H^*(\barB(\cA))$, which is
always $A_\infty$-formal for Koszul algebras by
Theorem~\textup{\ref{thm:koszul-equivalences-meta}(iii)}\textup{)}
are classified by shadow depth as follows.
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Class}
& \textbf{Families}
& $m_3^{\mathrm{SC}}$
exec
/bin/zsh -lc "rg -n \"free polynomial|polynomial algebra|ChirHoch\\"'^'"\\*\\(\\\\cA\\)|Theorem~H|main-koszul-hoch|Hochschild\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9588,9660p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2068,2178p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1984,2006p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:free polynomial|polynomial algebra|ChirHoch\^\*\(\cA\)|Theorem~H|main-koszul-hoch|Hochschild)
                                                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 \textup{(proved local algebra)}} \\[2pt]
& Theorems A--H
 (bar-cobar adjunction, inversion,
 complementarity, modular characteristic,
 Hochschild) \\
& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
 strong completion towers, HS-sewing) \\
& MC3 proved for all simple types on the
 evaluation-generated core; DK-4/5
 (extension beyond evaluation modules) downstream \\
& Koszulness programme: $10$ unconditional
 equivalences $+$ $1$ conditional (Lagrangian)
 $+$ $1$ one-directional (D-module purity)
 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
& Shadow obstruction tower algebraicity:
 $H(t)^2 = t^4 Q_L(t)$, tower determined by
 $(\kappa, \alpha, S_4)$
 \textup{(}Theorem~\ref{thm:riccati-algebraicity}\textup{)};
 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
 $\alpha = 0$ \textup{(}Heis\textup{)},
 succeeded in 51ms:
 \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X
 \]
 \textup{(}Theorem~H,
 Theorem~\textup{\ref{thm:main-koszul-hoch})}.
\end{enumerate}

\smallskip
\noindent\textbf{Conditional and partial:}
\begin{enumerate}
\item[\textup{(xi)}] The Lagrangian criterion: $\cM_\cA$ and
 $\cM_{\cA^!}$ are transverse Lagrangians in the $(-1)$-shifted
 symplectic deformation space~$\cM_{\mathrm{comp}}$.
\item[\textup{(xii)}] $\mathcal{D}$-module purity: each
 $\barBgeom_n(\cA)$ is pure of weight~$n$ as a mixed Hodge module,
 with characteristic variety aligned to FM boundary strata.
\end{enumerate}
\end{theorem}

\begin{proof}
\textsc{The core circuit}
 succeeded in 51ms:
chain-level BV/BRST/bar conjectural\textup{)},
MC3 \textup{(}three-layer split: MC3a evaluation core all types unconditional,
MC3b categorical thick generation all types unconditional,
MC3c full Cat~O type~A unconditional / other types conditional on
Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
and the Koszulness characterization programme
(10 unconditional, 1 conditional, 1 one-directional;
Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
appendices touches it except to cross-reference from it.

\subsection*{Ring~2: The nonlinear characteristic layer}
Before the extension appendices, the modular characteristic was
scalar: the single number~$\kappa(\cA)$ and its $\lambda_g$ tower,
plus the spectral discriminant~$\Delta_\cA(x)$. The full
hierarchy is:
\[
\kappa(\cA)
\;\longrightarrow\;
\Delta_\cA

thinking
**Searching for theorem details**

It looks like the theorem has weakened, and the audit findings might reference an outdated version. I’m wondering if there are still mentions of "ten proved unconditionally equivalent, one conditional on tangent complex perfectness, one one-directional" somewhere in the introduction, specifically around line 1199. I think I need to search for item (viii) related to the free polynomial in the document. I’ll use a simple search tool like rg to help with that.
exec
/bin/zsh -lc "rg -n \"free polynomial|polynomial algebra|freely generated|cofree polynomial|Hochschild consequence|viii|ChirHoch\\"'^'"\\*|ChirHoch\\"'^1|ChirHoch|Theorem~H" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
822:For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
857:This is a polynomial algebra on the generators
860:polynomial algebras are Koszul, with Koszul dual the
907:is a polynomial algebra (the OPE reduces to a commutative
1292:\index{truncated polynomial algebra!$A_\infty$ dual}
1447:Theorem~H
1453:Theorem~H at critical level.
2022:equivalent. Condition~\textup{(viii)} is a proved consequence of
2064:\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
2067: \ChirHoch^n(\cA)
2068: \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X
2070: \textup{(}Theorem~H,
2113:\textsc{Hochschild consequence}
2114:\textup{(v)}$\Rightarrow$\textup{(viii)}:
2120:Koszul locus, Theorem~H and
2123:\textup{(viii)} to the bar-cobar counit is proved here.
2849:consequence~\textup{(viii)} have been verified
3144:and the Hochschild consequence~\textup{(viii)} no longer follows.
3907: graded is the polynomial algebra $\mathrm{Sym}(V)$ with
4611:\item Formal smoothness: $\dim \ChirHoch^*(W_3) < \infty$ (verified by Zhu's theorem)
exec
/bin/zsh -lc "sed -n '1188,1204p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Koszul property!intrinsic characterizations}
\index{MC element!genus-0 formality}

The MC element $\Theta_\cA \in \MC(\mathfrak{g}_\cA^{\mathrm{mod}})$
lives in a modular convolution algebra bigraded by degree and genus.
Chiral Koszulness is a \emph{genus-$0$ formality property}:
it says the genus-$0$ component $\Theta_\cA^{(0)}$ is
determined by its binary part; equivalently, all genus-$0$
obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
The shadow obstruction tower probes all genera; Koszulness constrains only
genus~$0$. Twelve characterizations of chiral
Koszulness (ten proved unconditionally equivalent, one conditional on
perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
one-directional (D-module purity, forward direction established)), each
reading~$\Theta_\cA^{(0)}$ through a different invariant
of the convolution algebra.

exec
/bin/zsh -lc "rg -n \"ten proved unconditionally equivalent|10 unconditional|ten unconditional|nine unconditional|12 characterizations|twelve characterizations|12 unconditional|equivalences \\+\\"'$ 1 conditional|one-directional" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
72:one-directional implication. The count is exact:
1199:Koszulness (ten proved unconditionally equivalent, one conditional on
1201:one-directional (D-module purity, forward direction established)), each
2713:is the one-directional part of the meta-theorem
2848:The nine unconditional equivalences and the Hochschild
3143:nine unconditional Koszul equivalences lose force simultaneously,
3170:Each of the nine unconditional equivalences
3178:\textup{(xi)} and the one-directional $\mathcal{D}$-module purity
5936:twelve characterizations of
exec
/bin/zsh -lc "sed -n '56,76p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5928,5944p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
No other functorial construction achieves all three: the operadic
adjunction achieves (a) but not (b) or (c); Verdier duality alone
achieves (b) but has no bar-cobar content; complementarity (c)
requires both (a) and (b) as input.

Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
tests and consequences around chiral Koszulness. Nine are
unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
vanishing of transferred $A_\infty$ operations $m_k$ for
$k \geq 3$, acyclicity of the twisted tensor product
$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
duality and concentration in degrees $\{0,1,2\}$) is a proved
consequence on the Koszul locus. One (the Lagrangian
eigenspace decomposition) is conditional on perfectness of the
bar-cobar normal complex. One (D-module purity) is a
one-directional implication. The count is exact:
$9 + 1 + 1 + 1$.

Two distinctions require emphasis. First, the four complexity
 succeeded in 51ms:
% ================================================================

\section{Summary}

The PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion})
reduces chiral Koszulness to a classical spectral sequence
degeneration, applicable uniformly to all freely strongly generated
vertex algebras (Proposition~\ref{prop:pbw-universality}). The
twelve characterizations of
Theorem~\ref{thm:koszul-equivalences-meta} read the same
genus-$0$ formality condition through distinct invariants: bar
concentration, Ext diagonal vanishing, factorization homology,
Kac--Shapovalov determinants, FM boundary acyclicity. Two
characterizations remain partially open: the Lagrangian criterion
awaits perfectness verification in general, and D-module purity
awaits the converse direction. The $\Eone$-chiral Koszul duality
theorem (Theorem~\ref{thm:e1-chiral-koszul-duality}) extends the
exec
/bin/zsh -lc "rg -n \"C\\(x,y,z\\)|kappa\\(x,\\[y,z\\]\\)|\\[y,z\\]|invariant bilinear form|bilinear form|SC-formal\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
89:(Heisenberg and its relatives) is SC-formal
1663:by non-degeneracy of a bilinear form weight by weight. We now
2564:relationship between SC-formality and the classification is
2572:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
2575:\index{class G@class~$G$!characterised by SC-formality}
2584:SC-formal\textup{)} is established in
2589:For the converse, suppose~$\cA$ is SC-formal.
2596:these contradicts SC-formality. Hence an SC-formal algebra must

thinking
**Investigating bilinear forms**

I'm considering whether searching for a generic bilinear form could lead me to relevant information, even if it's not an exact match. There could be useful insights around line 1663 that connect to another proof. So, I want to closely inspect the section from lines 1640 to 1675. Let's see if there’s something enlightening there to help with my understanding!
exec
/bin/zsh -lc "sed -n '1644,1672p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Let $\cA_\hbar$ be a flat deformation of a classically Koszul
commutative chiral algebra~$\cA_0$, with
$\cA_\hbar/\hbar\cA_\hbar \cong \cA_0$.
Proposition~\ref{prop:pbw-universality} implies: $\cA_\hbar$ is
chirally Koszul whenever the PBW filtration deforms flatly
($\operatorname{gr}_F \cA_\hbar \cong \cA_0$). All standard
families satisfy this: for $V_k(\fg)$ with $\hbar = k^{-1}$, the
bracket $[J^a, J^b]_\star = f^{ab}_c J^c + k\kappa^{ab}$ lies in
$F_{\geq 1}$; Virasoro and $\mathcal{W}$-algebras are analogous
with $\hbar = c^{-1}$. Flat PBW deformation is therefore the
mechanism producing chirally Koszul algebras from commutative seeds.
\end{remark}

\subsection{The Li--bar spectral sequence and geometric Koszulness}
\label{subsec:li-bar-geometric-koszulness}

The Kac--Shapovalov criterion
(Theorem~\ref{thm:kac-shapovalov-koszulness}) detects Koszulness
by non-degeneracy of a bilinear form weight by weight. We now

thinking
**Inspecting summary lines**

Since the user is specifically targeting only the file, I might not need to look further. However, I wonder if there’s another formal proposition around line 89 or if the summary text references "Heisenberg and its relatives." I think I'll need to inspect the top summary lines from 80 to 90 to clarify what else might be important or relevant to the user's needs.
exec
/bin/zsh -lc "sed -n '80,92p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
nontrivial; they do \emph{not} record failure of Koszulness.
Every standard chiral algebra is chirally Koszul. The classes
separate algebras by the complexity of their higher-genus
behaviour, not by the validity of the duality. Second,
Koszulness and SC formality are logically independent properties.
Koszulness is the condition that bar cohomology is concentrated
in degree one; SC formality is the condition
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
bar complex. All standard families are Koszul; only class~$G$
(Heisenberg and its relatives) is SC-formal
(Proposition~\ref{prop:sc-formal-iff-class-g}).
Confusing the two misidentifies what the shadow tower measures.





thinking
**Editing proof language**

I think I should make a minor edit to the proof to clearly state, "For the converse, we only use the classification from Prop..." This change might help us avoid any issues with bilinear-form arguments, especially for class C, where no invariant bilinear form exists. This would address the audit finding with minimal effort. Additionally, I could add a sentence clarifying that the proof does not rely on such forms and doesn’t claim a bilinear-form converse for beta-gamma.
thinking
**Refining mathematical terminology**

I’m considering changing the heading from "Unconditional consequence on the Koszul locus" to "One-way Hochschild consequence on the Koszul locus." This adjustment could clarify that Condition (viii) is a proved one-way consequence rather than just a proved consequence. For item 3, I think I should emphasize that the converse in the proof of `prop:sc-formal-iff-class-g` doesn’t invoke the trilinear form and avoids bilinear-form claims for the beta-gamma family. I might need to adopt a more mathematical tone to ensure clarity.
thinking
**Adjusting for clarity**

I need to make a minimum truthful edit to address each finding. If the live proof already avoids bilinear forms, it would make sense to emphasize the classification route. However, if there's a specific request to restrict to families with invariant bilinear forms, I might adjust the introduction at line 89 regarding `(Heisenberg and its relatives)`. Still, the classification should remain a standard landscape. I should check the theorem registry entry, though updates might not be necessary, and I wonder about potential shifts in line counts with editing. It’s essential to follow the Pre-Edit Verification Protocol for hot zones.
thinking
**Clarifying restrictions**

The user asked about restricting to families with invariant bilinear forms, specifically KM, not betagamma. My initial thought is that no such restriction is necessary, and I wonder if that’s acceptable. It's good to note that the current proof doesn't rely on any invalid bilinear-form construction, so an explicit note may suffice. I’m considering mentioning `classL exclusion could be detected by the invariant form on affine KM`, but maybe that’s too complicated. I also need to check if line 89, referring to "Heisenberg and its relatives," is a concern.
codex
I have the minimal patch shape. Before editing, I’m locking the theorem scope so the change only narrows the two overclaims and makes the SC-formality converse explicit about what it does and does not use.

```text
genus: [g=0 for (vii); all for theorem surface otherwise]
degree: [n=all as stated; (vii) only on \mathbb{P}^1]
AP32 weight tag: [NA]  tagged? [Y]
AP139 free-var audit: LHS vars:{\cA} RHS vars:{\cA,\mathbb{P}^1} LHS⊇RHS? [Y]
AP36: [implies/iff]  if iff, converse proved same thm? [Y for (i)-(vi),(vii),(ix),(x); N/A for one-way (viii)]
verdict: ACCEPT
```

thinking
**Applying a patch**

I need to apply a patch, which sounds straightforward enough. I’m also considering revising the summary line at 1199 and possibly adding a heading for a theorem proof. That could help with organization and clarity. I wonder if these changes will enhance understanding! Alright, let’s get to it and see how these adjustments improve the overall structure. It's all about making things clearer and more effective.
codex
I’m editing only the local theorem/proof sentences in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex) to make the genus-0 scope explicit, mark the Hochschild item as one-way, and state that the SC-formality converse is classification-based rather than bilinear-form based.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -1198,3 +1198,4 @@
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
@@ -2020,4 +2021,5 @@
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
@@ -2050,3 +2052,3 @@
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
@@ -2061,3 +2063,3 @@
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
@@ -2595,3 +2597,6 @@
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..b9ea67e42df19fedcdd8a954378479660f2f3787
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..b9ea67e42df19fedcdd8a954378479660f2f3787
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 


thinking
**Inspecting modifications**

I need to re-read the modified ranges and search for any forbidden patterns in the updated file. I’m noticing a potential grammar mistake with the phrase "these contradicts," which might need to be corrected to just "contradicts." Since we've made changes, we could consider patching that up. I’ll also take some time to look around those modifications to ensure everything's accurate. Let's see if there's anything more I can note or fix!
codex
The patch is in. I’m re-reading the touched ranges now to check that the theorem count, the `(vii)/(viii)` logic, and the SC-formality proof still read coherently in context before I do the final grep pass.
exec
/bin/zsh -lc "sed -n '1192,1204p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
lives in a modular convolution algebra bigraded by degree and genus.
Chiral Koszulness is a \emph{genus-$0$ formality property}:
it says the genus-$0$ component $\Theta_\cA^{(0)}$ is
determined by its binary part; equivalently, all genus-$0$
obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
The shadow obstruction tower probes all genera; Koszulness constrains only
genus~$0$. Twelve characterizations of chiral
Koszulness (nine proved unconditionally equivalent, one one-way
Hochschild consequence on the Koszul locus, one conditional on
perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
one-directional (D-module purity, forward direction established)), each
reading~$\Theta_\cA^{(0)}$ through a different invariant
of the convolution algebra.
exec
/bin/zsh -lc "sed -n '2016,2130p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2578,2602p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"free polynomial|polynomial algebra|ten proved unconditionally equivalent|C\\(x,y,z\\)|kappa\\(x,\\[y,z\\]\\)|\\bcontradicts SC-formality\\b|Genus-\\"'$0'"\\"'$ factorization homology|One-way Hochschild consequence" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists exactly of Heisenberg and lattice
VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Because the standard landscape is exhausted by the four classes
$G$, $L$, $C$, $M$, it is enough to eliminate the three
non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
nonzero higher operations in every arity $k \geq 3$. Each of
 succeeded in 51ms:
\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
genus-$0$ condition~\textup{(vii)} below are equivalent.
Condition~\textup{(viii)} is a proved one-way consequence of
them on the Koszul locus.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
\item[\textup{(i)}] $\cA$ is chirally Koszul
 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
 succeeded in 51ms:
822:For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
857:This is a polynomial algebra on the generators
860:polynomial algebras are Koszul, with Koszul dual the
907:is a polynomial algebra (the OPE reduces to a commutative
1293:\index{truncated polynomial algebra!$A_\infty$ dual}
2064:\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
2598:these contradicts SC-formality. This converse uses only the
3912: graded is the polynomial algebra $\mathrm{Sym}(V)$ with
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..b9ea67e42df19fedcdd8a954378479660f2f3787
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

codex
There’s one local coherence issue from the re-read: a pre-existing grammar glitch in the SC-formality proof became more visible after the added sentence. I’m correcting that single sentence and then doing the forbidden-pattern grep the user requested.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2597,3 +2597,3 @@
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. This converse uses only the
+these cases contradicts SC-formality. This converse uses only the
 classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 


thinking
**Verifying patterns and implications**

I need some final verification, especially since "Each of these cases contradicts" sounds okay, but it's a singular subject. I should use `grep` to search for forbidden patterns and might want to check for any old issues. Maybe I’ll use `rg` to find patterns in the modified file. 

I’ll look into specific phrases like `C(x,y,z)` and `factorization homology`, to see if necessary criteria are met. Lastly, I can check labels/ref validity, and run `git diff --` for inspection.
exec
/bin/zsh -lc "rg -n \"ten proved unconditionally equivalent|free polynomial|polynomial algebra.*ChirHoch|ChirHoch.*polynomial|kappa\\(x,\\[y,z\\]\\)|C\\(x,y,z\\)|Conditions \\\\textup\\{\\(i\\)--\\(vii\\)\\}|Unconditional consequence on the Koszul locus|Genus-\\"'$0'"\\"'$ factorization homology|one-way Hochschild consequence" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2588,2600p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the class-$G$ row consists exactly of Heisenberg and lattice
VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Because the standard landscape is exhausted by the four classes
$G$, $L$, $C$, $M$, it is enough to eliminate the three
non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
nonzero higher operations in every arity $k \geq 3$. Each of
these cases contradicts SC-formality. This converse uses only the
classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
it does not invoke any trilinear form built from~$\kappa$.
 succeeded in 52ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

codex
The targeted grep is clean on the forbidden side, but I want one positive check as well: confirm the new genus-0 and one-way wording is actually present, and then I can close this out with a precise FIXED/BLOCKED accounting.
exec
/bin/zsh -lc 'rg -n -F "ten proved unconditionally equivalent" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Genus-"'$0$ factorization homology'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "kappa(x,[y,z])" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'One-way Hochschild consequence on the Koszul locus' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

 succeeded in 51ms:
2053:\item[\textup{(vii)}] Genus-$0$ factorization homology
 succeeded in 51ms:
2064:\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

Plan update
The three scoped fixes are now applied in the assigned file and verified by local re-read plus targeted grep checks for the old overclaims and the new replacement wording.
  ✓ Locate the exact equivalence items (vii), (viii) and the SC-formality converse in the assigned file, plus matching registry/concordance context
  ✓ Apply the minimum truthful edits in chapters/theory/chiral_koszul_pairs.tex
  ✓ Re-read the edited ranges and grep the modified file for forbidden patterns relevant to the changes
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 


thinking
**Finalizing response details**

I need to keep the final response concise while mentioning the file link. It's important to state if items are FIXED or BLOCKED based on my findings. The user is focused on the three most critical items, so item three might be clarified about proof using classification rather than bilinear form. I might include a short bullet list, but I should ensure no \ref/\label changes are made. Also, line numbers could be approximated, so I'll reference those in the summary.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1196,1204p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2592,2600p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2018,2068p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1196	obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
  1197	The shadow obstruction tower probes all genera; Koszulness constrains only
  1198	genus~$0$. Twelve characterizations of chiral
  1199	Koszulness (nine proved unconditionally equivalent, one one-way
  1200	Hochschild consequence on the Koszul locus, one conditional on
  1201	perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
  1202	one-directional (D-module purity, forward direction established)), each
  1203	reading~$\Theta_\cA^{(0)}$ through a different invariant
  1204	of the convolution algebra.
 succeeded in 51ms:
  2018	\index{Koszul property!equivalences of characterizations|textbf}
  2019	
  2020	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  2021	with PBW filtration $F_\bullet$.
  2022	Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
  2023	genus-$0$ condition~\textup{(vii)} below are equivalent.
  2024	Condition~\textup{(viii)} is a proved one-way consequence of
  2025	them on the Koszul locus.
  2026	Under the additional perfectness and non-degeneracy hypotheses on the
  2027	ambient tangent complex, condition~\textup{(xi)} is also equivalent to
  2028	them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  2029	(Remark~\ref{rem:d-module-purity-content}); the converse is open.
  2030	
  2031	\smallskip
  2032	\noindent\textbf{Unconditional equivalences:}
  2033	\begin{enumerate}
  2034	\item[\textup{(i)}] $\cA$ is chirally Koszul
  2035	 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
  2036	\item[\textup{(ii)}] The PBW spectral sequence on
  2037	 $\barBgeom(\cA)$ collapses at $E_2$
 succeeded in 51ms:
  2592	Because the standard landscape is exhausted by the four classes
  2593	$G$, $L$, $C$, $M$, it is enough to eliminate the three
  2594	non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
  2595	does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
  2596	class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
  2597	nonzero higher operations in every arity $k \geq 3$. Each of
  2598	these cases contradicts SC-formality. This converse uses only the
  2599	classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
  2600	it does not invoke any trilinear form built from~$\kappa$.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 


thinking
**Crafting a concise answer**

I want to make sure the final answer isn't too verbose. It should probably be one to two short sections to keep it clear and to the point. I’m aiming for something straightforward that communicates the essential information without unnecessary details. Keeping things concise can help the user grasp the key points quickly, which is super important! So, let’s get right to it and craft that answer.
codex
Edited [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex).

FIXED 1: Koszul equivalence `(vii)` is now explicitly genus-0 only in the theorem statement, not just in the proof. See [chiral_koszul_pairs.tex:2022](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2022) and [chiral_koszul_pairs.tex:2053](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2053).

FIXED 2: Koszul equivalence `(viii)` is now explicitly one-way, matching the proved Hochschild content rather than an equivalence. I also synced the earlier summary count from `10` unconditional equivalences to `9 + 1 + 1 + 1`. See [chiral_koszul_pairs.tex:1199](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1199), [chiral_koszul_pairs.tex:2024](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2024), and [chiral_koszul_pairs.tex:2064](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2064).

FIXED 3: The SC-formality converse now states that it uses only the class-by-class non-formality proposition, not any invalid `\kappa`-based trilinear-form argument. See [chiral_koszul_pairs.tex:2598](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2598).

Verification: I re-read the touched ranges, made no `\label` or `\ref` changes, and grep-confirmed the modified file no longer contains the stale `ten proved unconditionally equivalent` phrasing or any `\kappa(x,[y,z])` surface. No blockers.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index d1df6af3fd4e85270a5c0e34372125e8b4fea0f1..0305a104bdc30e807eec65ff86762c707d61a34b
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -1196,7 +1196,8 @@
 obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
 The shadow obstruction tower probes all genera; Koszulness constrains only
 genus~$0$. Twelve characterizations of chiral
-Koszulness (ten proved unconditionally equivalent, one conditional on
+Koszulness (nine proved unconditionally equivalent, one one-way
+Hochschild consequence on the Koszul locus, one conditional on
 perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
 one-directional (D-module purity, forward direction established)), each
 reading~$\Theta_\cA^{(0)}$ through a different invariant
@@ -2018,8 +2019,9 @@
 
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
-Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
-equivalent. Condition~\textup{(viii)} is a proved consequence of
+Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
+genus-$0$ condition~\textup{(vii)} below are equivalent.
+Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
@@ -2048,7 +2050,7 @@
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology
+\item[\textup{(vii)}] Genus-$0$ factorization homology
  $\int_{\mathbb{P}^1} \cA$ is concentrated in degree~$0$.
 \item[\textup{(ix)}] The Kac--Shapovalov determinant
  $\det G_h \neq 0$ in the bar-relevant range
@@ -2059,7 +2061,7 @@
 \end{enumerate}
 
 \smallskip
-\noindent\textbf{Unconditional consequence on the Koszul locus:}
+\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
 \begin{enumerate}
 \item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
  cohomological degrees $\{0,1,2\}$ and satisfies the duality
@@ -2593,7 +2595,10 @@
 does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
 class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
 nonzero higher operations in every arity $k \geq 3$. Each of
-these contradicts SC-formality. Hence an SC-formal algebra must
+these cases contradicts SC-formality. This converse uses only the
+classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
+it does not invoke any trilinear form built from~$\kappa$.
+Hence an SC-formal algebra must
 belong to class~$G$.
 \end{proof}
 

tokens used
118,962
