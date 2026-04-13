# E19_notation_index (615s)

- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:1): no Vol I notation index existed. `EXACT edit applied`: created a standalone LaTeX document that lists the core symbols from `main.tex` and `chapters/theory/`, with columns for symbol, meaning, and first explicit definition at `file:line`.

- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:12): the standalone file needed its own local symbol definitions, and the prose note used Markdown-style backticks, which are not valid repository-style LaTeX. `EXACT edit applied`: added local macros for `\barBgeom` and `\barBch`, and rewrote the scope note with `\texttt{main.tex}` and `\texttt{chapters/theory/}`.

- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:41): the initial table geometry was too wide for the page. `EXACT edit applied`: tightened the `longtable` column widths to `0.24/0.46/0.20\textwidth`.

Verification: `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp standalone/notation_index.tex` succeeds. The output PDF was written to `/tmp`, so no extra repo artifacts were created.


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
session id: 019d87db-bd9e-7290-8f5b-f522c4698862
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Create a notation index for Vol I.
Scan main.tex and chapters/theory/ for key macros: \kappa, \Theta, B(A), A^!, Z^{der}, r(z), etc.
Produce a list of: symbol, meaning, first defined at file:line.
Write to standalone/notation_index.tex.
mcp startup: no servers


thinking
**Executing coding task**

I need to act in coding agent mode and utilize the tools effectively while adhering to the guidelines. The user requested that I create a notation index for Volume I, which involves scanning specific files for key macros and producing a list with symbols and their meanings. I should read and edit only the assigned files. I’ll ensure to report any problems encountered and the exact edits made along the way, focusing on being thorough within the designated scope.
thinking
**Creating notation index**

I need to focus on the assigned file, standalone/notation_index.tex, and I can't edit others like main or theory. My main task is to create the notation index and fix any potential issues related to it within that scope. The problem seems to be that the notation index is missing or incomplete, which means I may need to create a new file or edit an outdated one. I should start with an update for the user and use commentary often while examining the files. Tool calls might help in this process.
codex
I’m treating this as a scoped audit-and-fix on the Vol I notation surface. First I’m reading the required repo-wide control files and the live theory sources, then I’ll extract the earliest definitions in `main.tex` and `chapters/theory/` and write a minimal truthful notation index to `standalone/notation_index.tex`.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

 succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
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
**Considering notation entries**

I need to extract meaning from context, which likely involves many symbols. I should aim for an exhaustive list but wonder how many entries to include. The core notation seems to suggest about 15-25 key macros like \kappa, \Theta, and B(A). I’ll scan the main.tex and theory chapters to find their definitions. Maybe I can use scripts or shell commands to gather occurrences, considering potential parallelization for efficiency. Let's inspect and see how best to proceed!
codex
I’ve loaded the constitutional files. Next I’m mapping the theory surface: `main.tex`, the current `standalone/notation_index.tex` state, and the first occurrences of the core symbols in `chapters/theory/` so the index is anchored to live source rather than memory.
exec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^'"\\\\input\\{chapters/theory/|"'^'"\\\\include\\{chapters/theory/' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f standalone/notation_index.tex ]; then sed -n '1,260p' standalone/notation_index.tex; else echo '__MISSING__'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\(kappa|Theta|barB|B\\(|Omegach|Omega\\(|ChirHoch|gAmod|Convstr|mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{mod\\}\\}|mathbb\\{D\\}_\\{\\\\Ran\\}|mathbb\\{D\\}_\\{Ran\\}|A\\"'^!|A'"\\"'^i|Z'"\\"'^'"\\{der\\}|r\\"'^|r'"\\()' chapters/theory main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{4} % Numbers down to subsubsubsection
\setcounter{tocdepth}{4} % TOC includes subsubsubsections

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

% EB Garamond with full features
\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols % This prevents conflicts
]{newtxmath}
\usepackage{ebgaramond}

% Fine-tuning for optimal appearance
\usepackage[
 activate={true,nocompatibility},
 succeeded in 50ms:
859:\include{chapters/theory/introduction}
963:\include{chapters/theory/fourier_seed}
970:\include{chapters/theory/algebraic_foundations}
976:\include{chapters/theory/three_invariants}
982:\include{chapters/theory/configuration_spaces}
988:\include{chapters/theory/bar_construction}
994:\include{chapters/theory/cobar_construction}
1004:\input{chapters/theory/bar_cobar_adjunction_curved}
1005:\input{chapters/theory/bar_cobar_adjunction_inversion}
1022:\include{chapters/theory/poincare_duality}
1030:\include{chapters/theory/chiral_koszul_pairs}
1031:\include{chapters/theory/koszul_pair_structure}
1040:\input{chapters/theory/higher_genus_foundations}
1041:\input{chapters/theory/higher_genus_complementarity}
1042:\input{chapters/theory/higher_genus_modular_koszul}
1056:\include{chapters/theory/chiral_hochschild_koszul}
1062:\include{chapters/theory/chiral_modules}
1063:\include{chapters/theory/poincare_duality_quantum}
1064:\include{chapters/theory/quantum_corrections}
1069:\input{chapters/theory/filtered_curved}
 succeeded in 50ms:
__MISSING__
 succeeded in 52ms:
Total output lines: 5825

main.tex:439:\newcommand{\barB}{\overline{B}}
main.tex:482:\newcommand{\barBgeom}{\bar{\mathbf{B}}}
main.tex:483:\newcommand{\barBch}{\bar{B}^{\text{ch}}} % Chiral bar complex notation
main.tex:484:\newcommand{\Omegach}{\Omega^{\text{ch}}} % Chiral cobar complex notation
main.tex:489:\newcommand{\ChirHoch}{CH} % Chiral Hochschild
main.tex:507:\newcommand{\Convstr}{\operatorname{Conv}_{\mathrm{str}}} % strict dg Lie convolution model
main.tex:511:\newcommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}} % modular convolution dg Lie algebra of A
main.tex:517:\newcommand{\Thetaenv}{\Theta^{\mathrm{env}}} % envelope-shadow functor
main.tex:704:\providecommand{\gmod}{\mathfrak{g}^{\mathrm{mod}}_{\cA}}
main.tex:749:$\Theta_\cA \in \gAmod$ satisfying
main.tex:750:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$
main.tex:757:$\kappa(\cA) + \kappa(\cA^!) = K(\cA)$;
main.tex:759:$F_g = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$
main.tex:824:\item $\barBgeom(\mathcal{A})$ denotes the geometric bar complex.
main.tex:825:\item $\barBch(\mathcal{A})$ denotes the abstract chiral bar complex (when distinction needed).
main.tex:916:forces $d^2 = 0$. This is the bar complex~$\barB_X(\cA)$: the
main.tex:923: The bar-cobar adjunction $(\barB, \Omega)$, intertwined with
main.tex:928: $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$: the cobar inverts


thinking
**Extracting definitions and symbols**

I need to extract definitions and have produced quite a few with `rg`, but I think a more precise search might help. I want to inspect macro definitions in the main.tex file, especially around lines 430-520, and check the notation section near line 820. The user is looking for a list of symbols with their meanings, alongside where they were first defined. For example, I might find `\ChirHoch` defined in main.tex at line 489. I'll also consider earlier occurrences to ensure accuracy in definitions.
thinking
**Creating notation index**

I need to create a notation index with "first defined at file:line" for each symbol. Since this index will be in a standalone file, I won't be changing the source definitions but will ensure to cite line numbers. I'm thinking there might be a standalone directory with other documentation. It would be useful to inspect the style of these standalone docs, possibly using an article or subsection format. I’ll check out the standalone directory for more insights.
codex
The repository has no existing `standalone/notation_index.tex`, so the only fix surface is creating it. I’m now pinning the earliest definitional lines for the core notation instead of taking first raw occurrences, because several symbols first appear in summary prose before they are actually defined.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'ls -1 standalone' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '720,860p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,540p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N1_koszul_meta.aux
N1_koszul_meta.log
N1_koszul_meta.out
N1_koszul_meta.pdf
N1_koszul_meta.tex
N2_mc3_all_types.aux
N2_mc3_all_types.log
N2_mc3_all_types.out
N2_mc3_all_types.pdf
N2_mc3_all_types.tex
N3_e1_primacy.aux
N3_e1_primacy.log
N3_e1_primacy.out
N3_e1_primacy.pdf
N3_e1_primacy.tex
N4_mc4_completion.aux
N4_mc4_completion.log
N4_mc4_completion.out
N4_mc4_completion.pdf
N4_mc4_completion.tex
 succeeded in 50ms:


\maketitle

\begin{abstract}
\itshape

\noindent
We define ordered chiral homology
$\int_X^{\mathrm{ord}} \cA$ for a chiral algebra~$\cA$
on a smooth algebraic curve~$X$ as the derived pushforward
of the ordered factorisation $\cD$-module
$\cF^{\mathrm{ord}}(\cA)$ on the ordered Ran space
$\operatorname{Ran}^{\mathrm{ord}}(X)
= \coprod_n U_n(X)$.
The ordered bar complex
$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
carries a deconcatenation coproduct, an $R$-matrix,
and Yangian structure; the symmetric bar
$B^\Sigma(\cA)$ on $\operatorname{Ran}(X)$ is its
 succeeded in 50ms:
\newcommand{\DX}{\mathcal{D}_X}
\newcommand{\OX}{\mathcal{O}_X}
\newcommand{\omX}{\omega_X}
\newcommand{\IndCoh}{\cat{IndCoh}}
\newcommand{\QCoh}{\cat{QCoh}}

% ==========================================
% COMMON SYMBOLS
% ==========================================
\newcommand{\C}{\mathbb{C}} % NB: overrides built-in accent command \c (cedilla)
\newcommand{\Z}{\mathbb{Z}} % NB: overrides built-in accent command
\newcommand{\R}{\mathbb{R}} % NB: overrides built-in accent command
\newcommand{\Vlat}{V} % Lattice vertex algebra (V_\Lambda)
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cV}{\mathcal{V}}
\newcommand{\cW}{\mathcal{W}}
\newcommand{\cI}{\mathcal{I}}
\newcommand{\Sh}{\operatorname{Sh}}
\newcommand{\barB}{\overline{B}}
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
🌐 Searching the web...
🌐 Searched: time: {"utc_offset":"-04:00"}

thinking
**Creating a plan**

I think I should create a plan since this task seems a bit substantial. It might be helpful to structure my approach so I can stay organized. I could use an update plan tool to outline my steps. This way, I’ll have a clearer view of what needs to be done, and I can track my progress efficiently. Having a plan sounds like a good idea to tackle this effectively!
Plan update
Building the notation index from live theory sources and restricting edits to `standalone/notation_index.tex`.
  ✓ Map included theory files and extract candidate core notation from `main.tex` and `chapters/theory/`.
  → Pin the first definitional occurrence and line number for each retained symbol.
  • Write `standalone/notation_index.tex` with a concise notation table.
  • Verify the new file for scope, formatting, and source references.

thinking
**Inspecting definitions**

I need to use comments for updates and might look into using the `rg` tool to find definitions in sections like introduction, bar construction, and others. Custom `grep` patterns could help too. I should inspect the `chapters/theory/introduction.tex` file, focusing on the relevant lines to search for notation definitions. Specifically, I'll look for lines featuring `\Theta`, `\kappa`, `r(z)`, `Z^{der}`, and `A^!`. It could be efficient to parallelize targeted searches with `rg`.
codex
I’ve separated macro declarations in `main.tex` from actual mathematical definitions in the chapters. The remaining work is source pinning: for each retained symbol I’m checking the earliest line that states what the object is, not just where it is first mentioned in a theorem summary.
exec
/bin/zsh -lc "rg -n '\\\\Theta_\\\\cA|\\\\Theta_\\{\\\\cA\\}|\\\\Theta_A|Theta_\\\\cA|Theta_A' chapters/theory/introduction.tex chapters/theory/bar_construction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa\\(\\\\cA\\)|\\\\kappa\\(A\\)|modular characteristic|invariant pairing \\\\kappa|scalar shadow|av\\(r\\(z\\)\\)' chapters/theory/introduction.tex chapters/theory/bar_construction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/three_invariants.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Z_\\{\\\\mathrm\\{ch\\}\\}\\"'^'"\\{\\\\mathrm\\{der\\}\\}|Z\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}|derived chiral center|\\\\ChirHoch\\"'^'"\\*|\\\\ChirHoch\\"'^n|'"\\\\operatorname\\{HH\\}\\"'^'"\\*' chapters/theory/introduction.tex chapters/theory/bar_construction.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/ordered_associative_chiral_kd.tex main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'r\\(z\\)|R-matrix|\\\\Res\\"'^'"\\{\\\\mathrm\\{coll\\}\\}_\\{0,2\\}|classical r-matrix|collision residue' chapters/theory/introduction.tex chapters/theory/three_invariants.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/e1_modular_koszul.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 643

chapters/theory/bar_construction.tex:36:$\Theta_\cA \in \MC(\gAmod)$ governing the genus expansion,
chapters/theory/bar_construction.tex:38:tower $\Theta_\cA^{\leq r}$.
chapters/theory/bar_construction.tex:165:$\tau_{\mathrm{mod}} = \tau + \Theta_\cA$
chapters/theory/bar_construction.tex:1048:(The collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ is the universal twisting morphism; see Theorem~\ref{thm:gz26-commuting-differentials} for its genus-$0$ realization as commuting Hamiltonians.) Morphisms of chiral algebras induce
chapters/theory/bar_construction.tex:2044:$\Theta_\cA^{E_1}$ on the tensor bar $T^c$
chapters/theory/e1_modular_koszul.tex:296:\Theta_\cA^{E_1}
chapters/theory/e1_modular_koszul.tex:304:$D\Theta_\cA^{E_1}
chapters/theory/e1_modular_koszul.tex:305:+ \tfrac{1}{2}[\Theta_\cA^{E_1}, \Theta_\cA^{E_1}] = 0$.
chapters/theory/e1_modular_koszul.tex:309:\operatorname{av}\bigl(\Theta_\cA^{E_1}\bigr)
chapters/theory/e1_modular_koszul.tex:311:\Theta_\cA.
chapters/theory/e1_modular_koszul.tex:319:$D_\cA^{E_1} = \dzero + \Theta_\cA^{E_1}$, so the identity
chapters/theory/e1_modular_koszul.tex:321:$D\Theta_\cA^{E_1}
chapters/theory/e1_modular_koszul.tex:322:+ \tfrac{1}{2}[\Theta_\cA^{E_1}, \Theta_\cA^{E_1}] = 0$
chapters/theory/e1_modular_koszul.tex:336:\operatorname{av}\bigl(\Theta_\cA^{E_1}\bigr)
chapters/theory/e1_modular_koszul.tex:342:\Theta_\cA,
chapters/theory/e1_modular_koszul.tex:770:The degree-$r$ component of $\Theta_\cA^{E_1}$ at genus~$0$ is an
chapters/theory/e1_modular_koszul.tex:1350:$\Theta_\cA$. Before taking $\Sigma_r$-coinvariants, the genus-$0$
chapters/theory/e1_modular_koszul.tex:1351:degree-$r$ component of $\Theta_\cA^{E_1}$ is a meromorphic function
 succeeded in 51ms:
Total output lines: 501

chapters/theory/bar_construction.tex:40:$d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$ from the Hodge bundle
chapters/theory/bar_construction.tex:169:$\kappa(\cA)\cdot\omega_g$ controls the genus tower.
chapters/theory/bar_construction.tex:385:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, and the curvature
chapters/theory/bar_construction.tex:386:$\kappa(\cA)$ is the \emph{infinitesimal generator} of this
chapters/theory/bar_construction.tex:398:Theorem~D that the leading coefficient~$\kappa(\cA)$ of the
chapters/theory/bar_construction.tex:400:$F_g(\cA) = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$
chapters/theory/bar_construction.tex:409:characteristic~$\kappa(\cA)$. At the scalar level, the T-matrix
chapters/theory/bar_construction.tex:1735:oriented at each genus. It is the determinant line of $T_{C_{p+1}(\Sigma_g)}$ with genus-dependent corrections, ensuring consistent signs across all face maps. At genus~$0$, this guarantees $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}); at genus~$g \geq 1$, the fiberwise differential satisfies $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ and the total corrected differential $\Dg{g}^2 = 0$ is established in Chapter~\ref{chap:higher-genus}.
chapters/theory/bar_construction.tex:2054:= \kappa(\cA)$.
chapters/theory/higher_genus_foundations.tex:38:That amount is $\kappa(\cA) \cdot \omega_g$, and its appearance
chapters/theory/higher_genus_foundations.tex:42:H^2(\overline{\cM}_{g,n})$ on moduli. $\kappa(\cA)$ is the scalar extracted from the
chapters/theory/higher_genus_foundations.tex:98:$\dfib^{\,2}|_{g=1} = \kappa(\cA)\cdot\omega_1$ arises from
chapters/theory/higher_genus_foundations.tex:115:with~$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, and obstruction classes
chapters/theory/higher_genus_foundations.tex:119:The modular characteristic
chapters/theory/higher_genus_foundations.tex:120:$\kappa(\cA)$ is the linear shadow (Ring~1), the spectral
chapters/theory/higher_genus_foundations.tex:151:(\dfib)^{\,2} = \kappa(\cA) \cdot \omega_1, \qquad
chapters/theory/higher_genus_foundations.tex:172:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, where $\omega_g$ is the
chapters/theory/higher_genus_foundations.tex:186:$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in
 succeeded in 50ms:
main.tex:786:Higher Deligne Conjecture, the derived chiral center
main.tex:787:$Z_{\mathrm{ch}}^{\mathrm{der}}(\cA)
main.tex:788:= \operatorname{HH}^*(\cA, \cA)$
main.tex:793:$Z_{\mathrm{ch}}^{\mathrm{der}}(V_k(\mathfrak{g}))$
main.tex:944:$\ChirHoch^*(\cA)$ is polynomial on the Koszul locus and dual to
main.tex:945:$\ChirHoch^*(\cA^!)$. The full Taylor series of the logarithm lives
chapters/theory/ordered_associative_chiral_kd.tex:10530:(derived chiral center) to $D^{\mathrm{co}}$; the coproduct
chapters/theory/ordered_associative_chiral_kd.tex:10646:The derived chiral center
chapters/theory/ordered_associative_chiral_kd.tex:10647:$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the Hochschild
chapters/theory/ordered_associative_chiral_kd.tex:10662:% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
chapters/theory/ordered_associative_chiral_kd.tex:11235:$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ and the
chapters/theory/chiral_hochschild_koszul.tex:12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
chapters/theory/chiral_hochschild_koszul.tex:16:$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
chapters/theory/chiral_hochschild_koszul.tex:21:refinement of $\ChirHoch^*(\cA)$.
chapters/theory/chiral_hochschild_koszul.tex:136:$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
chapters/theory/chiral_hochschild_koszul.tex:357:The left side is precisely $\ChirHoch^n(\mathcal{A})$ by definition.
chapters/theory/chiral_hochschild_koszul.tex:371:The chiral Hochschild complex $\ChirHoch^*(\mathcal{A})$ is a double complex with horizontal differential $d_{\mathrm{bar}}$ (the bar differential of Definition~\ref{def:bar-differential-complete}) and vertical differential $d_{\mathrm{sheaf}}$ (sheaf cohomology on configuration spaces). Filter by bar degree: $F^n = \bigoplus_{m \geq n} \ChirHoch^{m,*}$. The resulting spectral sequence has $E_0^{n,q} = \Gamma(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$ with $d_0 = d_{\mathrm{sheaf}}$, so $E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$. Convergence follows from the bounded-below hypothesis on $\mathcal{A}$ and the finite cohomological dimension of configuration spaces.
chapters/theory/chiral_hochschild_koszul.tex:711:\ChirHoch^n(\mathcal{A}) \cong \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee} \otimes \omega_X.
chapters/theory/chiral_hochschild_koszul.tex:778:\ChirHoch^n(\cA)
chapters/theory/chiral_hochschild_koszul.tex:812: $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
 succeeded in 52ms:
chapters/theory/three_invariants.tex:44:produces no collision residue: the \emph{collision depth} of
chapters/theory/three_invariants.tex:117:the collision residue of a term $1/(z-w)^n$ in the OPE contributes
chapters/theory/three_invariants.tex:118:to $1/z^{n-1}$ in the collision residue: the $\mathrm{d}\log(z-w)$
chapters/theory/three_invariants.tex:269:the pole order of the degree-$2$ collision residue) or with
main.tex:1092:The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
main.tex:1094:scalar is extracted from the collision residue $r(z)$ by a
main.tex:1321:% holographic datum H(W_3) = (A, A!, C, r(z), Theta_A, nabla^hol).
main.tex:1503:% The centrepiece. One mathematical object --- the collision residue
main.tex:1504:% r(z) = Res^coll_{0,2}(Theta_A) --- realized in seven independent
main.tex:1512:One mathematical object, the collision residue
main.tex:1513:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$,
main.tex:1519:% The seven faces of the collision residue: master chapter for Part V.
main.tex:1520:% One mathematical object (r(z) = Res^coll_{0,2}(Theta_A)) realized in
main.tex:1528:% Genus-1 extension of the seven-face programme. The collision residue
chapters/theory/e1_modular_koszul.tex:13:$\Sigma_2$-coinvariant of a meromorphic function $r(z)$ that records
chapters/theory/e1_modular_koszul.tex:35:the classical $r$-matrix $r(z)$, the Knizhnik--Zamolodchikov
chapters/theory/e1_modular_koszul.tex:769:\index{R-matrix!as $E_1$ shadow}
chapters/theory/e1_modular_koszul.tex:781:$r = 2$ & $r(z)$ (classical $r$-matrix)
chapters/theory/e1_modular_koszul.tex:941:consists of the $R$-matrix data $r(z)$ modulo its scalar
chapters/theory/e1_modular_koszul.tex:942:$\Sigma_2$-coinvariant $\av(r(z))$).
codex
I have enough candidate symbols now. Before I write the file, I’m doing a final pass with line-numbered context so each row uses a defensible “first defined here” citation instead of a loose earliest mention.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '80,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '680,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    80	\begin{convention}[Bar coalgebra and Koszul dual algebra]
    81	\label{conv:bar-coalgebra-identity}
    82	\index{bar construction!as bar coalgebra|textbf}
    83	\index{Koszul dual!coalgebra vs.\ algebra|textbf}
    84	The bar construction $\barB_X(\cA)$ of an augmented chiral
    85	algebra~$\cA$ is a dg factorization \emph{coalgebra} on
    86	$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the bar coalgebra
    87	of~$\cA$: the bar complex computes the dual
    88	coalgebra
    89	\[
    90	\cA^i \;:=\; H^*(\barB_X(\cA)).
    91	\]
    92	Thus $\barB_X(\cA)$, $\cA^i$, and $\cA^!$ are distinct objects.
    93	
    94	When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
    95	in bar degree~$1$, so $\cA^i$ is concentrated there. The Koszul dual
    96	\emph{algebra}~$\cA^! = ((\cA^i)^\vee)$ is a
    97	separate object: it has generators $\mathcal{V}^\vee =
    98	\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
    99	($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
 succeeded in 51ms:
   680	 $\ChirHoch^1(V_k(\fg)) \cong \fg$, so no uniform four-dimensional
   681	 bound is available. Critical level is outside the theorem's regime:
   682	 there the Beilinson--Drinfeld comparison yields an unbounded oper-type
   683	 center. The primitive step is the descent lemma
   684	 (Lemma~\ref{lem:chirhoch-descent}), reducing Theorem~H to Theorem~A's
   685	 Verdier intertwining.
   686	\end{itemize}
   687	
   688	\begin{warning}[Three Hochschild theories]
   689	\label{warn:three-hochschild-intro}
   690	\index{Hochschild cohomology!three variants}%
   691	Three inequivalent notions of ``Hochschild cohomology'' coexist
   692	in this programme; conflating them is a persistent source of
   693	error.
   694	\emph{Chiral Hochschild} $\ChirHoch^*(\cA) =
   695	H^*(\operatorname{CoDer}(\barB(\cA)))$ is the cohomology of
   696	coderivations of the bar coalgebra; it lives on the
   697	curve~$X$ and has cohomological amplitude~$[0,2]$ on the
   698	Koszul locus (Theorem~H).
   699	\emph{Topological Hochschild} $\mathrm{HH}^*_{\mathrm{top}}$
 succeeded in 51ms:
     1	\chapter{Introduction}
     2	
     3	\section{From a point to a curve}
     4	\label{sec:volume-one-route}
     5	
     6	Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. In the non-abelian affine Kac--Moody case the precise degree-$2$ formula is $\kappa(\cA) = \mathrm{av}(r_\cA(z)) + \dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.
     7	
     8	The organising principle is as follows. The geometry of the
     9	curve~$X$ determines an operad (the Fulton--MacPherson
    10	compactifications $\FM_n(X)$ with their boundary strata); the
    11	operad determines a bar complex (the cofree coalgebra
    12	$T^c(s^{-1}\bar\cA)$ with its residue-extraction differential);
    13	the bar complex computes the invariants (the modular
    14	characteristic~$\kappa$, the shadow obstruction tower, the
    15	chiral Hochschild cohomology $\ChirHoch^*$). At each step the
    16	passage is forced: one form ($\eta = d\log(z_1 - z_2)$), one
    17	relation (Arnold), one object ($\Theta_\cA$), one equation
    18	($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$).
    19	
    20	The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
 succeeded in 51ms:
    30	curve over $\overline{\mathcal{M}}_{g,n}$, the cobar functor
    31	inverts at genus~$g$
    32	(Theorem~\ref{thm:higher-genus-inversion}).
    33	
    34	%% FORCED CONSEQUENCE: the MC element and its degree projections.
    35	
    36	The identity $D_\cA^2 = 0$ has an immediate algebraic consequence.
    37	Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
    38	bar differential. Because $D_\cA^2 = 0$, the element
    39	$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
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
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1278,1318p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '6728,6740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '10640,10658p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1278	over the Koszul dual cooperad
  1279	$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
  1280	It has a differential (from OPE collision residues) and a
  1281	coassociative deconcatenation coproduct. These are the two
  1282	structures of a dg coalgebra. The bar complex does \emph{not}
  1283	carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.
  1284	
  1285	The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
  1286	the \emph{derived chiral center}
  1287	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
  1288	= C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$,
  1289	computed \emph{using} the bar complex as a resolution.
  1290	The derived center is the algebra of bulk observables of
  1291	the 3d HT theory on $X \times \bR$:
  1292	\begin{itemize}
  1293	\item It carries $\Etwo$ structure from
  1294	  $\FM_k(\bC)$ (the operadic center theorem,
  1295	  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
  1296	\item With an inner conformal vector at non-critical level,
  1297	  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
 succeeded in 51ms:
  6728	 \textup{(}Lurie~\cite{HA}, \S5.3; Francis~\cite{Francis2013}\textup{)},
  6729	 if $\barB^{\Sigma}(\cA)$ is an $\Etwo$-algebra, then
  6730	 the resulting Hochschild cochain object carries a natural
  6731	 $\mathsf{E}_3$ structure. In the present chiral setting, this
  6732	 structure lives on the derived center
  6733	 $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \HH^*(\cA,\cA)$, computed by the
  6734	 symmetric bar resolution. This is the correct $\mathsf{E}_3$ object:
  6735	 the derived center, not the symmetric bar.
  6736	
  6737	\item \textup{(Obstruction dimension.)}
  6738	 The obstruction to extending $\Etwo$ to $\mathsf{E}_3$ on
  6739	 $\barB^{\Sigma}(\cA)$ lives in
  6740	 $\HH^3_{\Etwo}(\barB^{\Sigma}(\cA), \barB^{\Sigma}(\cA))$. For the Heisenberg
 succeeded in 50ms:
     1	\chapter{Chiral Hochschild cohomology and Koszul duality}
     2	\label{chap:deformation-theory}
     3	
     4	\index{deformation theory!chiral|textbf}
     5	\index{Hochschild cohomology!chiral|textbf}
     6	
     7	The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
     8	Koszul duality, but how rigid is the moduli it lives in? Without
     9	knowing the tangent complex to
    10	$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
    11	bulk-field coupling remains inaccessible. The chiral Hochschild
    12	complex $\ChirHoch^*(\cA)$ is that tangent complex;
    13	Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
    14	Koszul locus, so the MC moduli has cohomological
    15	amplitude~$[0,2]$, and the Koszul duality
    16	$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
    17	is Verdier duality on this tangent space.
    18	
    19	The cyclic deformation complex $\Defcyc(\cA)$
    20	(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
 succeeded in 50ms:
 10640	Conjecture~\ref{conj:coderived-chiral-coproduct}).
 10641	The bar differential~$d_{\barB}$ as coderivation of~$\Delta$
 10642	encodes the RTT relation, the vertex bialgebra axiom, and the
 10643	OPE-coproduct intertwining: these are the
 10644	\emph{same} coderivation property read in different
 10645	coordinates.
 10646	The derived chiral center
 10647	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the Hochschild
 10648	cochain complex of the bialgebra, carrying the
 10649	$\mathsf{E}_3$ structure of
 10650	Conjecture~\ref{conj:coderived-e3}.
 10651	
 10652	The variety of structures that appear in the
 10653	literature (CoHA multiplication, Yangian coproduct,
 10654	W-algebra OPE, quantum group R-matrix, vertex
 10655	bialgebra axioms) are projections of this single coderived
 10656	chiral bialgebra through different forgetful functors:
 10657	%
 10658	% FOUR OBJECTS (AP25/AP34/AP50):

thinking
**Inspecting definitions in the text**

I need to check the lines for the Chiral Hochschild definition, possibly around lines 346 or 4835. There's an introductory warning at line 694 that could work as the first definition. The derived center might be at introduction line 842 or main.tex line 787, but line 1286 in en_koszul is explicit and could be cited. Since I'm scanning the scope that includes chapters and main.tex, I should focus on introduction line 842 as well.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '388,430p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1218,1275p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '856,910p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2608,2674p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   388	The ordered bar differential $D_\cA^{\Eone}$ on
   389	$\barB^{\mathrm{ord}}(\cA)$ defines
   390	$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
   391	\in \MC({\gAmod}^{\Eone})$
   392	(Theorem~\ref{thm:e1-mc-element}); since
   393	$(D_\cA^{\Eone})^2 = 0$, the MC equation
   394	$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
   395	is automatic. Averaging into~$\gAmod$ produces the modular
   396	Maurer--Cartan element $\Theta_\cA$ of
   397	Theorem~\ref{thm:mc2-bar-intrinsic}. The binary ordered projection of
   398	$\Theta_\cA^{\Eone}$ is the collision residue $r_\cA(z)$, and
   399	$\operatorname{av}(r_\cA(z)) = \kappa(\cA)$. The five theorems
   400	characterize five structural properties of this projection.
   401	\emph{Existence}: Theorem~A identifies the duality arena.
   402	\emph{Faithfulness}: Theorem~B reconstructs~$\cA$ from its bar data on
   403	the Koszul lane.
   404	\emph{Decomposition}: Theorem~C polarizes the genus-$g$ ambient
   405	complex.
   406	\emph{Leading coefficient}: Theorem~D extracts the scalar shadow
   407	$\kappa(\cA)$.
 succeeded in 52ms:
  1218	\Theta_\cA^{\Eone}
  1219	\;:=\;
  1220	D_\cA^{\Eone} - d_\cA^{(0)}
  1221	\;\in\;
  1222	\MC\!\bigl({\gAmod}^{\Eone}\bigr).
  1223	\end{equation}
  1224	The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
  1225	genus~$0$ is the \emph{classical $r$-matrix}
  1226	$r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
  1227	the meromorphic function whose residue at $z = 0$ controls the
  1228	spectral scattering of~$\cA$. The degree-$3$ component is the
  1229	\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
  1230	components are the higher Yangian/braided coherences that satisfy
  1231	the boundary equations of Stasheff associahedra:
  1232	classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
  1233	quartic $R$-matrix identity for $r_4$, and so on
  1234	(Proposition~\ref{prop:e1-shadow-r-matrix}).
  1235	The components of $\Theta_\cA^{\Eone}$ are the full data of the
  1236	line-operator algebra: an $R$-matrix, a braided category, a
  1237	Drinfeld--Jimbo Yangian.
 succeeded in 50ms:
   856	algebraic consequences of the MC element; the five claims above are
   857	the five boundary-bulk consequences of the same theorems.
   858	\end{conjecture}
   859	
   860	\begin{proposition}[Five facets of the collision residue $r(z)$;
   861	 \ClaimStatusProvedElsewhere]
   862	\label{prop:five-facets-collision-residue}
   863	\index{collision residue!five facets|textbf}%
   864	\index{r-matrix@$r(z)$!five facets|textbf}%
   865	\index{Seven Faces!and five facets of $r(z)$}%
   866	The degree-$2$, genus-$0$ projection
   867	\[
   868	r(z)
   869	\;:=\;
   870	\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{\Eone})
   871	\;\in\;
   872	\End(V^{\otimes 2}) \otimes \cO(*\Delta)
   873	\]
   874	of the universal Maurer--Cartan element
   875	\textup{(}Theorem~\textup{\ref{thm:e1-mc-element}}\textup{)}
 succeeded in 51ms:
  2608	\end{proof}
  2609	
  2610	\begin{definition}[Scalar modular characteristic package]
  2611	\label{def:modular-characteristic-package}
  2612	\label{def:scalar-modular-package}
  2613	\index{modular characteristic package!scalar|textbf}
  2614	Let $\cA$ be a modular Koszul chiral algebra
  2615	(Definition~\ref{def:modular-koszul-chiral}). The
  2616	\emph{scalar modular characteristic package} of~$\cA$ consists of:
  2617	\begin{enumerate}[label=\textup{(\roman*)}]
  2618	\item The \emph{obstruction invariant}
  2619	 $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
  2620	 fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
  2621	 (Theorem~\ref{thm:genus-universality}).
  2622	\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
  2623	 of free energies determined by the bar complex at genus~$g$
  2624	 (Theorem~\ref{thm:universal-generating-function}).
  2625	\end{enumerate}
  2626	Both components are established. The Heisenberg specialization
  2627	appears in Chapter~\ref{ch:heisenberg-frame},

thinking
**Creating a notation index**

I think I need to establish definitions for the \Convstr and \gAmod macros in main.tex, particularly around lines 507 and 511. I should also consider adding macros like `\dzero`, `\dfib`, and `\Dg`, especially since the user is interested in key macros like \kappa. There’s a need to create a notation index for Volume I that includes symbols like \Theta, B(A), and others, specifying their meaning and first occurrence in the files. This might just turn into a table instead of a full document.
exec
/bin/zsh -lc "sed -n '1,220p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,
 linkcolor=blue!60!black,
 citecolor=green!40!black,
 urlcolor=blue!60!black]{hyperref}

% ================================================================
% Theorem environments
 succeeded in 50ms:
\documentclass[11pt]{article}

%%% Packages
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{tikz-cd}

%%% Page geometry
\usepackage[margin=1.15in]{geometry}

%%% Theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}





thinking
**Creating notation index**

I’m considering creating a notation index for an article, perhaps using a longtable in LaTeX. I wonder if I need to compile it, but it might be possible via pdflatex instead. I’ll need to make sure to list essential symbols exhaustively, focusing on those in the specified scope. 

I'll verify symbols like \kappa and \Theta to ensure they’re included effectively. The user has asked for a list of symbols, meanings, and where they're defined, so I should cover core symbols.
thinking
**Structuring notation with longtable**

I’m thinking I could use a `longtable` with three columns for the notation index. It might include a "Scope note" indicating the first definitional occurrence in either `main.tex` or `chapters/theory/`, possibly formatted in monospace with LaTeX's `\texttt{}`. I’ll need to ensure line numbers are included and compile specific entries with file:line references. For example, the introduction of `\barB^{\mathrm{ord}}_X(\cA)=T^c(s^{-1}\bar\cA)` occurs at line 6 in the introduction.
thinking
**Clarifying source references**

I’m considering how to handle the "first defined at file:line" references since files are separate, which can be ambiguous. It seems the user is likely interested in the first definition based on the document's order, especially since `main.tex` includes chapters in sequence. The explicit definition of `higher_genus_modular_koszul` occurs at line 715 within the introduction, so I think I’ll refer to that as the first definitional occurrence in the book. I could mention that this follows the document's order, not alphabetical.
thinking
**Determining document order**

I’m working on understanding how to derive the document order from the main includes. It looks like the introduction comes before the sections on bar construction and higher genus, which is good to note. For some symbols, the introduction at line 6 is the first instance. For `r(z)`, it seems like it’s first defined at line 868, although line 398 talks about a related concept. Since I need to focus on the symbols correctly, I think using line 868 is best, even if line 398 is earlier.
thinking
**Choosing symbol definitions**

I'm considering whether to use `r_\cA(z)` to match the first definition or stick with `r(z)`, since that’s what the user provided. I think I could potentially present both, indicating that one refers to the "degree-2, genus-0 collision residue of the ordered MC element." I could cite either the introduction at line 398 or 868 for clarification. It seems like I need to find a way to make these definitions clear and useful for the user.
codex
I’ve narrowed the index to the symbols that actually carry the Vol I spine: bar/cobar objects, duals, modular/ordered MC classes, collision residue, scalar shadow, higher-genus differentials, and derived-center/Hochschild notation. I’m checking the preamble macros now so the table cites the earliest source line when a notation is introduced in `main.tex` before the chapters use it.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '478,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '784,792p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '1088,1096p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '820,832p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   478	\providecommand{\zetareg}{\zeta_{\mathrm{reg}}}
   479	\providecommand{\GL}{\mathrm{GL}}
   480	\providecommand{\Imag}{\operatorname{Im}}
   481	% ==========================================
   482	\newcommand{\barBgeom}{\bar{\mathbf{B}}}
   483	\newcommand{\barBch}{\bar{B}^{\text{ch}}} % Chiral bar complex notation
   484	\newcommand{\Omegach}{\Omega^{\text{ch}}} % Chiral cobar complex notation
   485	\newcommand{\ConfigSpace}[1]{\overline{C}_{#1}(X)} % Configuration space
   486	\newcommand{\LogForm}[2]{\eta_{#1#2}} % Logarithmic forms
   487	
   488	% Additional notation for consistency
   489	\newcommand{\ChirHoch}{CH} % Chiral Hochschild
   490	\newcommand{\Walg}{\mathcal{W}} % W-algebra
   491	\newcommand{\critLevel}{-h^\vee} % Critical level
   492	
   493	% ==========================================
   494	% HIGHER-GENUS DIFFERENTIAL NOTATION
   495	% (Convention~\ref{conv:higher-genus-differentials})
   496	% ==========================================
   497	% Three mathematically distinct differentials act on genus-g bar complexes.
 succeeded in 51ms:
   784	For $\mathsf{E}_\infty$-chiral~$\cA$, the symmetric bar
   785	carries an $\mathsf{E}_2$-coalgebra structure; by the
   786	Higher Deligne Conjecture, the derived chiral center
   787	$Z_{\mathrm{ch}}^{\mathrm{der}}(\cA)
   788	= \operatorname{HH}^*(\cA, \cA)$
   789	carries $\mathsf{E}_3$ structure.
   790	For $\mathsf{E}_1$-chiral~$\cA$, the derived center is
   791	$\mathsf{E}_2$.
   792	The $\mathsf{E}_3$-deformation space of
 succeeded in 51ms:
   820	
   821	\section*{Notation and conventions}
   822	Throughout this manuscript:
   823	\begin{itemize}
   824	\item $\barBgeom(\mathcal{A})$ denotes the geometric bar complex.
   825	\item $\barBch(\mathcal{A})$ denotes the abstract chiral bar complex (when distinction needed).
   826	\item $\ConfigSpace{n} = \overline{C}_n(X)$ is the compactified configuration space.
   827	\item $\LogForm{i}{j} = d\log(z_i - z_j)$ are the logarithmic 1-forms.
   828	\item $\Einf$-chiral, $\Eone$-chiral, $\Pinf$-chiral refer to
   829	 curve-based chiral factorization levels
   830	 (Definition~\ref{def:einf-chiral}ff.); bare $\En$ refers to the
   831	 little-disks/topological axis on real $n$-manifolds. A complex
   832	 curve therefore enters the topological ladder at $n = 2$, not
 succeeded in 52ms:
  1088	\part{The Characteristic Datum}
  1089	\label{part:characteristic-datum}
  1090	
  1091	\noindent
  1092	The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
  1093	linear leading term of the categorical logarithm: even this degree-$2$
  1094	scalar is extracted from the collision residue $r(z)$ by a
  1095	$\Sigma_2$-coinvariant integral on the Fulton--MacPherson
  1096	compactification $\overline{C}_2(X)$, so the shadow tower is rooted

thinking
**Investigating definitions**

I think I'll need to examine the definitions of higher-genus differentials, possibly looking through the introduction or a dedicated chapter. It's essential to find a clear understanding of the conventions used. I wonder if that will provide the context I need. I'll set out to research this topic further to ensure I get the definitions right! Let’s see what other relevant resources are out there to help clarify this.
exec
/bin/zsh -lc "rg -n '\\\\omega_g = c_1\\(\\\\mathbb\\{E\\}\\)|\\\\omega_g\\s*=\\s*c_1\\(\\\\mathbb\\{E\\}\\)|Hodge class on' chapters/theory/introduction.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Delta\\s*=\\s*8\\\\kappa S_4|critical discriminant|\\\\Delta\\(\\\\cA\\) := 8\\\\kappa\\(\\\\cA\\) \\, S_4\\(\\\\cA\\)' chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/three_invariants.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathrm\\{obs\\}_g\\(\\\\cA\\) = \\\\kappa\\(\\\\cA\\) \\\\cdot \\\\lambda_g|F_g\\(\\\\cA\\) = \\\\kappa\\(\\\\cA\\)\\\\cdot\\\\lambda_g\\"'^'"\\{\\\\mathrm\\{FP\\}\\}|lambda_g' chapters/theory/introduction.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Theta_\\\\cA\\"'^'"\\{\\\\leq r\\}|shadow obstruction tower|finite-order projections' chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/three_invariants.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex:53:$\omega_g = c_1(\mathbb{E})$ is the Hodge class on
chapters/theory/higher_genus_modular_koszul.tex:15:where $\omega_g = c_1(\lambda)$ is the Hodge class on
chapters/theory/higher_genus_modular_koszul.tex:33390:is the Hodge class on $\overline{\cM}_2$
 succeeded in 51ms:
chapters/theory/introduction.tex:79:have $r_{\max} = \infty$. The \emph{critical discriminant}
chapters/theory/introduction.tex:80:$\Delta = 8\kappa S_4$ forces $r_{\max}$ to lie in
chapters/theory/higher_genus_modular_koszul.tex:16137:for class~$\mathbf{M}$: the critical discriminant
chapters/theory/higher_genus_modular_koszul.tex:16138:$\Delta = 8\kappa S_4 = 40/(5c{+}22) > 0$ for $c > 0$
chapters/theory/higher_genus_modular_koszul.tex:16182:discriminant $\Delta = 8\kappa S_4$
chapters/theory/higher_genus_modular_koszul.tex:16356:$\Delta = 8\kappa S_4 = 40/(5c{+}22) > 0$ for $c > 0$,
chapters/theory/higher_genus_modular_koszul.tex:16693:The critical discriminant $\Delta = 0$ characterizes exact Bott
chapters/theory/higher_genus_modular_koszul.tex:16746: The discriminant $\Delta = 8\kappa S_4 \neq 0$ is the
chapters/theory/higher_genus_modular_koszul.tex:17147:$\Delta = 8\kappa S_4$
chapters/theory/higher_genus_modular_koszul.tex:17426:\index{critical discriminant|textbf}
chapters/theory/higher_genus_modular_koszul.tex:17458:The \emph{critical discriminant} of~$L$ is
chapters/theory/higher_genus_modular_koszul.tex:17575:where $\Delta = 8\kappa S_4$ is the critical discriminant.
chapters/theory/higher_genus_modular_koszul.tex:17659:$\Delta = 8\kappa S_4$ is the critical discriminant
chapters/theory/higher_genus_modular_koszul.tex:17907:the critical discriminant as
chapters/theory/higher_genus_modular_koszul.tex:18060:critical discriminant; the Cauchy--Schwarz defect
chapters/theory/higher_genus_modular_koszul.tex:18607:controlled by the critical discriminant: $\Sigma_L$ acquires a
chapters/theory/higher_genus_modular_koszul.tex:19148:\index{critical discriminant!atlas|textbf}
chapters/theory/higher_genus_modular_koszul.tex:19149:\index{critical discriminant!Virasoro closed form}
chapters/theory/higher_genus_modular_koszul.tex:19150:\index{critical discriminant!regularity at $c=0$}
chapters/theory/higher_genus_modular_koszul.tex:19151:\index{critical discriminant!complementarity|textbf}
 succeeded in 51ms:
chapters/theory/introduction.tex:93:$F_g = \kappa \cdot \lambda_g$ is exact at all genera
chapters/theory/introduction.tex:365:$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
chapters/theory/introduction.tex:618: $\mathrm{obs}_g = \kappa \cdot \lambda_g
chapters/theory/introduction.tex:625: F_g(\cA) = \kappa(\cA)\lambda_g^{\mathrm{FP}}
chapters/theory/introduction.tex:748: $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
chapters/theory/introduction.tex:826:is $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
chapters/theory/introduction.tex:828:$\lambda_g$ the $g$-th Mumford class (the gravitational
chapters/theory/introduction.tex:1933:Between the proved scalar tower $\kappa(\cA)\lambda_g$ and the full
chapters/theory/introduction.tex:2155:$\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight lane), complementarity, and
chapters/theory/introduction.tex:2357: scalar projection $\mathrm{obs}_g = \kappa(\cA)\,\lambda_g$
chapters/theory/higher_genus_foundations.tex:186:$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in
chapters/theory/higher_genus_foundations.tex:188:uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
chapters/theory/higher_genus_foundations.tex:253: $\mcurv{g} = \kappa(\cA)\cdot\lambda_g \in H^{2g}(\overline{\cM}_g)$ is the Chern--Weil image of this chain-level operator
chapters/theory/higher_genus_foundations.tex:490:$\kappa(\cA) \cdot \lambda_g$
chapters/theory/higher_genus_foundations.tex:591: \kappa(\cA)\cdot\lambda_g
chapters/theory/higher_genus_foundations.tex:595: where $\lambda_g = c_g(\mathbb{E})$ is the top Chern
chapters/theory/higher_genus_foundations.tex:667: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ \textup{(}Proposition~\textup{\ref{prop:genus-g-curvature-package}(iv))}
chapters/theory/higher_genus_foundations.tex:689: \kappa(\cA) \cdot \lambda_g
chapters/theory/higher_genus_foundations.tex:694: $\lambda_g$ but is not equal to it: the passage from the
chapters/theory/higher_genus_foundations.tex:749:identifies that class as $\kappa(\cA)\cdot\lambda_g$.
 succeeded in 51ms:
chapters/theory/three_invariants.tex:51:shadow obstruction tower $\Theta_{\beta\gamma}^{\leq r}$ has a
chapters/theory/three_invariants.tex:151:\text{the shadow obstruction tower }\Theta_\cA^{\leq r}
chapters/theory/three_invariants.tex:156:engine $\Theta_\cA^{\leq r}$ first terminates: for $r_{\max}(\cA)<\infty$,
chapters/theory/three_invariants.tex:157:the shadow obstruction tower is nontrivial only through
chapters/theory/three_invariants.tex:224:shadow obstruction tower, so $r_{\max}(\beta\gamma) = 4$.
chapters/theory/three_invariants.tex:251:\item \emph{The shadow obstruction tower classification}
chapters/theory/introduction.tex:14:characteristic~$\kappa$, the shadow obstruction tower, the
chapters/theory/introduction.tex:66:finite-order projections $\Theta_\cA^{\leq r}$ extract successively
chapters/theory/introduction.tex:121:At genus~$0$, the shadow obstruction tower coincides with the $L_\infty$
chapters/theory/introduction.tex:272:or the shadow obstruction tower.
chapters/theory/introduction.tex:410:The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
chapters/theory/introduction.tex:412:consists of finite-order projections:
chapters/theory/introduction.tex:773:shadow obstruction tower $\{S_r(\cA)\}_{r \ge 2}$ is the
chapters/theory/introduction.tex:899: characteristic, the first entry of the shadow obstruction tower
chapters/theory/introduction.tex:1295:shadow obstruction tower
chapters/theory/introduction.tex:1320: In particular, the shadow obstruction tower
chapters/theory/introduction.tex:1410:characteristic~$\kappa$, the shadow obstruction tower, and the
chapters/theory/introduction.tex:1931:\emph{Ring~2: the shadow obstruction tower.}
chapters/theory/introduction.tex:1974:from the Feynman transform of the modular operad; $\Convstr$ is its strict model. The shadow obstruction tower consists of
chapters/theory/introduction.tex:1975:finite-order projections of~$\Theta_\cA$:

thinking
**Considering inspection details**

I’m thinking about whether to include \Delta or not. Maybe it’s worth inspecting the line around the intro from 1974, especially concerning any shadow obstruction from the tower. I'll need to check those details to ensure everything looks right. Overall, I want to avoid any oversights, so I’ll make sure to assess the situation thoroughly.  It's all about getting the specifics right!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1968,1984p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '180,190p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '592,596p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1968	admits a universal gravitational form determined by the conformal
  1969	weights of the strong generators alone
  1970	(Theorem~\ref{thm:w-universal-gravitational-cubic}).
  1971	
  1972	The unifying principle is the modular $L_\infty$ convolution
  1973	algebra~$\gAmod$, whose $L_\infty$ structure comes
  1974	from the Feynman transform of the modular operad; $\Convstr$ is its strict model. The shadow obstruction tower consists of
  1975	finite-order projections of~$\Theta_\cA$:
  1976	$\kappa$ (degree~$2$),
  1977	$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
  1978	a projection of the next. The weight filtration on~$\gAmod$
  1979	controls extension; each truncation
  1980	$\Theta_\cA^{\le r}$ is constructive without requiring the full
  1981	all-genera modular envelope. The all-degree master equation
  1982	$D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
  1983	bar-intrinsic construction
  1984	(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4668,4674p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   180	by the Fay trisecant identity, so the nine-term verification
   181	of nilpotence goes through verbatim from genus~$0$.
   182	
   183	As $[\Sigma_g]$ varies over $\overline{\mathcal{M}}_g$, the bar
   184	complex forms a family of curved cochain complexes. The fiberwise
   185	curvature defines a characteristic class
   186	$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in
   187	H^*(\overline{\mathcal{M}}_g)$ for
   188	uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
   189	the top Chern class of the Hodge bundle; at genus~$1$ the same
   190	scalar formula is \textup{(g=1 only; all-weight at g=1 is unconditional)}
 succeeded in 52ms:
   592	 \;\in\;
   593	 H^{2g}(\overline{\mathcal{M}}_g,\mathbb{Q}),
   594	 \end{equation}
   595	 where $\lambda_g = c_g(\mathbb{E})$ is the top Chern
   596	 class \textup{(LOCAL)}.
 succeeded in 52ms:
  4668	 \kappa(\cA) \cdot \eta \otimes \Lambda,
  4669	 \qquad
  4670	 \Lambda := \sum_{g \geq 1} \lambda_g \;\in\; \Gmod,
  4671	 \end{equation}
  4672	 where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  4673	 Hodge bundle on~$\overline{\mathcal{M}}_g$.
  4674	

thinking
**Defining mathematical terms**

I'm considering whether to include \Lambda and also the definitions for \omega_g and \lambda_g separately. I think for \omega_g, I could look at the introduction around line 53, and for \lambda_g, I might refer to higher_genus_foundations at line 188 or higher_genus_modular_koszul at 4672. I wonder if the earliest mention of \lambda_g is in the introduction section at line 748, even though it seems that definition isn’t clear there. I'll double-check lines 820-830 for more context.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '820,830p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   820	 $13$ for Virasoro are shadows of this decomposition, not the theorem
   821	 itself.
   822	
   823	\item \emph{Brown--Henneaux coefficient}
   824	 \textup{(}Theorem~D\textup{)}.
   825	On the uniform-weight lane, the genus-$g$ obstruction
   826	is $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
   827	\textup{(}UNIFORM-WEIGHT\textup{)}, with
   828	$\lambda_g$ the $g$-th Mumford class (the gravitational
   829	 moduli characteristic). The scalar $\kappa(\cA)$ is the
   830	 Brown--Henneaux one-loop coefficient of the bulk partition







thinking
**Standardizing notation**

I'm trying to standardize on `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)` since the user asked about it, even though `\mathcal{Z}` is also relevant. I might note that it’s also written as `\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)` in the introduction, but will that clutter things? Should I include a mention of "derived chiral center/bulk"? 

The index could potentially have sections like Bar/cobar objects, ordered deformation objects, characteristic classes, and higher-genus differentials, but the user's request was specific to listing only. A single longtable might be the best way to go.
thinking
**Organizing macro declarations**

I’m thinking about the order of rows for various macro declarations. Even though the user didn’t specifically ask for a sort, I might organize them alphabetically or by their first definition. Grouping related items conceptually seems like a good idea. I’ll need to reference the first definitional occurrence in the document order. I could use `\footnotesize` in the table to fit everything and ensure ASCII compatibility by avoiding non-standard characters. Finally, I might compile it via pdflatex.
thinking
**Planning edits and commentary**

I think it's a good solution to use the output directory for compiling since the source file is read-only. I want to include some commentary before making edits and maybe verify the protocol first. I'm not sure if I'll need to write formulas in hot zones, but we might need to for kappa and bar formulas due to their complexity and the r(z) function. I should make sure to fill the relevant PE blocks before editing since that’s mandatory. I'll end with a verdict of ACCEPT.
thinking
**Structuring commentary**

I want to create commentary with fenced blocks. I need to determine the values, starting with PE-1 for the general r. The row will write something like `r_\cA(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})` or just `r(z)` as the collision residue. It's important to note that this won't be family-specific. Maybe I'll consider a template for "general ordered MC" while avoiding family-specific formulas. That's the plan!
thinking
**Organizing references**

I need to figure out how to handle commentary, maybe cutting out the em dash for clarity. I'll compute actual line references from the preamble and cited files. My plan is to gather a manageable set of exact rows and create a notation table with around 24 entries. For the potential final rows, I've identified various citation examples in the documentation. I need to confirm the full details for line 398, as it seems to be an important reference in this context.
thinking
**Clarifying citations**

I’m considering how to handle the citation details. For `\kappa(\cA)`, I see multiple possible references: introduction 6, 1269, or main 1092. The first formula appears in the introduction, but the first standalone definition seems to be either introduction 399 or 1269. I might cite introduction 1269 due to its clarity, but it’s not the very first mention. Since the user asked for the first defined occurrence, I should clarify that introduction 6 may already provide a definition, which introduces some ambiguity.
thinking
**Refining notation choices**

I’m figuring out which notation to include in the main.tex where the user asked about key macros. It seems like it's okay to keep the table compact with around 27 rows. I might want to include certain macros like `\barBgeom` and `\barBch`, but I'm not sure about `\ConfigSpace{n}` since it's not core. However, since the notation index should cover symbols used throughout, it makes sense to add `\overline{C}_n(X)` as it's central. I might also consider a curated list instead of listing everything exhaustively.
codex
I’m writing a single new standalone file with only sourced notation rows. Because the index touches the bar formula, the MC/residue package, and the scalar shadow, I’m locking those formulas against the repo’s hot-zone checks before I patch the file.

```text
PE-4: bar complex formula
object: B_X^{ord}(\cA) = T^c(s^{-1}\bar\cA)
T^c argument: [s^{-1} A-bar? Y]  AP132: augmentation? [Y]
AP22: |s^{-1}v| = |v| [-1] (must be -1)
s^{-1} not bare s? [Y]
coproduct: [deconcatenation]
match to intended bar: [B^ord -> deconc]
grading: cohomological |d|=+1? [Y]
verdict: ACCEPT
```

```text
PE-1: r-matrix write
family: [abstract collision residue / ordered MC]
r(z): [r(z) = Res^{coll}_{0,2}(Theta_A^{E_1})]
level param: [none in abstract definition]
OPE pole: [general]
r pole: [one less than OPE pole order]
AP126 (trace-form): [NA: no family-specific Omega/z formula written]
AP141 grep: bare \Omega/z in scope: [N]  allowed? N
critical-level (KM): [NA]
source: [chapters/theory/introduction.tex:868]
verdict: ACCEPT
```

```text
PE-2: kappa formula write
family: [abstract scalar shadow]
kappa written: [kappa(A) = av(r(z))]
census: [abstract extraction formula from chapters/theory/introduction.tex:1269]  match? [Y]
at k=0: [NA]
at k=-h^v (KM): [NA]
at c=13 (Vir): [NA]
wrong variants avoided: [NOT bare family formula, NOT H_{N-1}, NOT c unscoped]
verdict: ACCEPT
```

```text
PE-10: scope quantifier
genus: [all, but row explicitly marked uniform-weight for obs_g]
degree: [degree-2 scalar lane]
AP32 weight tag: [(UNIFORM)]  tagged? [Y]
AP139 free-var audit: LHS vars:{g,A} RHS vars:{g,A} LHS⊇RHS? [Y]
AP36: [implies/iff not used]
verdict: ACCEPT
```




thinking
**Considering row inclusion**

I'm thinking about whether I should include a row for `\operatorname{Ran}(X)`. There might be reasons for adding it, but then again, it may not be necessary. I need to weigh the importance of that row in the overall context. It might also depend on the focus of the work or what I want to convey. I'll take some time to evaluate its relevance before making a final decision.
thinking
**Considering LaTeX options**

I'm exploring how to use the `\path{}` command, which works well with special characters if the hyperref package is loaded. It breaks nicely at slashes and underscores, making it perfect for file references. I might also include `\urlstyle{tt}` for consistency and should decide between `\usepackage[hyphens]{url}` or `\usepackage{hyperref}`. I need to draft the table content carefully and perhaps add a note about definitions, along with the title "Notation Index for Vol I."
thinking
**Evaluating notation options**

Okay, I’m considering whether to use `\barB(\cA)` or `\barB_X(\cA)`. In row 25, I noted that `\ChirHoch^*(\cA)` means "chiral Hochschild cohomology." In the introduction, it’s defined as the cohomology of coderivations of the bar coalgebra. This approach might help me avoid complexity with the formula. It's good to clarify these details!
thinking
**Documenting definitions**

I'm noting that the table records the first explicit definitions instead of earlier mentions. The document order follows `main.tex`, which is good. I think I might need to build verification later, too. I should also run a search in the file for any forbidden formulas and non-ASCII characters. I can compile with pdflatex to the /tmp directory. Alright, let’s go ahead and apply that patch!
codex
I’m adding the standalone file now. The edit is limited to `standalone/notation_index.tex`; it is a source-backed table with explicit file:line anchors and no source changes outside that file.
file update
A /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}

\newcommand{\cA}{\mathcal{A}}
\newcommand{\barB}{\overline{B}}
\newcommand{\Ran}{\operatorname{Ran}}
\newcommand{\MC}{\operatorname{MC}}
\newcommand{\Res}{\operatorname{Res}}
\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
\DeclareMathOperator{\CoDer}{CoDer}

\title{Vol I Notation Index}
\author{}
\date{}

\begin{document}
\maketitle

This index is scoped to the notation introduced in `main.tex` and
`chapters/theory/`.
Line references record the first explicit definitional occurrence on that
surface, following Vol I document order from `main.tex`.
Earlier motivational mentions are ignored when a later line gives the first
actual symbol declaration or formula.

\bigskip

\small
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\renewcommand{\arraystretch}{1.15}

\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
\toprule
\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
\midrule
\endfirsthead
\toprule
\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
\midrule
\endhead
\bottomrule
\endfoot

$\barBgeom(\cA)$
& geometric bar complex
& \path{main.tex:824} \\

$\barBch(\cA)$
& abstract chiral bar complex, used when the distinction from the geometric model matters
& \path{main.tex:825} \\

$\overline{C}_n(X)$
& compactified configuration space
& \path{main.tex:826} \\

$\eta_{ij} = d\log(z_i-z_j)$
& logarithmic $1$-form used as the basic bar propagator
& \path{main.tex:827} \\

$d_0$
& genus-$0$ collision differential
& \path{main.tex:500} \\

$d_{\mathrm{fib}}$
& fiberwise curved differential on a fixed genus-$g$ curve
& \path{main.tex:501} \\

$D_g$
& total corrected differential at genus $g$
& \path{main.tex:502} \\

$\operatorname{Conv}_{\mathrm{str}}$
& strict dg Lie model of the modular convolution deformation object
& \path{main.tex:507} \\

$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
& modular convolution dg Lie algebra of $\cA$
& \path{main.tex:511} \\

$\barB_X(\cA)$
& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
& \path{chapters/theory/bar_construction.tex:84} \\

$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
& \path{chapters/theory/bar_construction.tex:86} \\

$\cA^i = H^*(\barB_X(\cA))$
& dual coalgebra computed by bar cohomology
& \path{chapters/theory/bar_construction.tex:90} \\

$\cA^! = ((\cA^i)^\vee)$
& Koszul dual algebra
& \path{chapters/theory/bar_construction.tex:96} \\

$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
& \path{chapters/theory/bar_construction.tex:108} \\

$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
& \path{chapters/theory/bar_construction.tex:135} \\

$\tau \colon \barB_X(\cA) \to \cA$
& canonical twisting morphism
& \path{chapters/theory/bar_construction.tex:142} \\

$\kappa(a,b) = a_{(1)}b$
& invariant pairing extracting the double-pole residue of the chiral product
& \path{chapters/theory/bar_construction.tex:206} \\

$\Theta_\cA = D_\cA - d_\cA^{(0)}$
& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
& \path{chapters/theory/introduction.tex:715} \\

$\mathfrak{g}^{E_1}_\cA$
& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
& \path{chapters/theory/introduction.tex:61} \\

$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
& ordered Maurer--Cartan lift retaining the non-averaged collision data
& \path{chapters/theory/introduction.tex:1218} \\

$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
& averaging map from ordered to coinvariant modular data
& \path{chapters/theory/introduction.tex:1245} \\

$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
& \path{chapters/theory/introduction.tex:868} \\

$\kappa(\cA) = \operatorname{av}(r(z))$
& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
& \path{chapters/theory/introduction.tex:1269} \\

$\Theta_\cA^{\le r}$
& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
& \path{chapters/theory/introduction.tex:1975} \\

$\Delta = 8\kappa S_4$
& critical discriminant governing finite versus infinite shadow depth
& \path{chapters/theory/introduction.tex:80} \\

$\ChirHoch^*(\cA)$
& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
& \path{chapters/theory/introduction.tex:694} \\

$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
& derived chiral center; the bulk object computed by Hochschild cochains
& \path{main.tex:787} \\

$\omega_g = c_1(\mathbb{E})$
& Hodge class governing fiberwise curvature
& \path{chapters/theory/introduction.tex:53} \\

$\lambda_g = c_g(\mathbb{E})$
& top Chern, or Mumford, class of the Hodge bundle
& \path{chapters/theory/higher_genus_foundations.tex:188} \\

$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
& scalar genus-$g$ obstruction class on the uniform-weight lane
& \path{chapters/theory/higher_genus_foundations.tex:186} \\

$\Lambda = \sum_{g \ge 1} \lambda_g$
& universal Hodge-class series used in the scalar shadow package
& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\

$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\

\end{longtable}

\end{document}
apply_patch(auto_approved=true) exited 0 in 19ms:
Success. Updated the following files:
A /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..785bb865fdc3ac6db6aa3495e262a19a8b0a659d
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,181 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in `main.tex` and
+`chapters/theory/`.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from `main.tex`.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..785bb865fdc3ac6db6aa3495e262a19a8b0a659d
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,181 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in `main.tex` and
+`chapters/theory/`.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from `main.tex`.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}


thinking
**Verifying file integrity**

I need to verify the file before proceeding. I could read it and perhaps compile it to the /tmp directory. However, I should consider sending an update before using any tools to ensure I'm on the right track. It's always good to double-check before diving in! Let's make sure everything is set up correctly before moving forward.
codex
The file is in place. I’m verifying two things now: the table entries still match the source lines they cite, and the standalone document is syntactically clean without introducing repo-side build artifacts.

thinking
**Considering file processing**

I need to run a read and compile operation with the output directory set to /tmp. It might also be helpful to grep for any banned em dashes, non-ASCII characters, or forbidden formulas; even if it’s not entirely necessary, it could be a good precaution. I am also thinking that using parallel processing could speed things up, so I’ll keep that in mind as well!
exec
/bin/zsh -lc "sed -n '1,260p' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}

\newcommand{\cA}{\mathcal{A}}
\newcommand{\barB}{\overline{B}}
\newcommand{\Ran}{\operatorname{Ran}}
\newcommand{\MC}{\operatorname{MC}}
\newcommand{\Res}{\operatorname{Res}}
\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
\DeclareMathOperator{\CoDer}{CoDer}

\title{Vol I Notation Index}
\author{}
\date{}
exec
/bin/zsh -lc "rg -n '---|—|Moreover|Additionally|notably|crucially|Remarkably|Interestingly|furthermore|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "LC_ALL=C grep -n '["'^ -~]'"' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: unrecognized flag ---|—|Moreover|Additionally|notably|crucially|Remarkably|Interestingly|furthermore|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate
 exited 1 in 52ms:

exec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp standalone/notation_index.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 187ms:
entering extended mode
(./standalone/notation_index.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/article.cls
Document Class: article 2024/06/29 v1.4n Standard LaTeX document class
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/longtable.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..785bb865fdc3ac6db6aa3495e262a19a8b0a659d
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,181 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in `main.tex` and
+`chapters/theory/`.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from `main.tex`.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}



thinking
**Fixing LaTeX macros and formatting**

I need to address undefined macros like \barBgeom and \barBch, either by defining them or writing them out explicitly. Using backticks in LaTeX may not be ideal, but it seems to compile. Replacing them with `\texttt{main.tex}` could help avoid issues. There's also a slight inconsistency in how I'm writing some equations. I might define those macros or use explicit symbols instead. Additionally, I should address the overfull alignment warning by adjusting column widths or using `\footnotesize`.
thinking
**Addressing LaTeX formatting issues**

I see that the row `\operatorname{Conv}_{\mathrm{str}}` is quite long. I need to check why the `rg` command failed due to the `---` flag, and I’ll use `rg -n -- 'pattern' file` to rerun it later. I'm also wondering if `\operatorname{CoDer}` is necessary since it’s not used. I think defining `\Pi_\cA` and `\overline{C}_n(X)` isn’t needed as they're just symbols. I’ll manage `\mathbb D_Ran` with the defined \Ran macro. Lastly, I need to note the use of `\path` in text columns.
codex
The first verification pass found a real issue in the new standalone file: I cited the `\barBgeom` and `\barBch` symbols without defining those macros locally, and I also left Markdown-style backticks in LaTeX prose. I’m fixing that now and then rerunning the isolated build to `/tmp`.
file update
M /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
@@ -11,2 +11,4 @@
 \newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
 \newcommand{\Ran}{\operatorname{Ran}}
@@ -24,6 +26,6 @@
 
-This index is scoped to the notation introduced in `main.tex` and
-`chapters/theory/`.
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
 Line references record the first explicit definitional occurrence on that
-surface, following Vol I document order from `main.tex`.
+surface, following Vol I document order from \texttt{main.tex}.
 Earlier motivational mentions are ignored when a later line gives the first
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..351388852a35a35b2c0bad9c683eb62444425162
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..351388852a35a35b2c0bad9c683eb62444425162
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

exec
/bin/zsh -lc "LC_ALL=C grep -n '["'^ -~]'"' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '---|—|Moreover|Additionally|notably|crucially|Remarkably|Interestingly|furthermore|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,60p' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

 succeeded in 52ms:
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}

\newcommand{\cA}{\mathcal{A}}
\newcommand{\barB}{\overline{B}}
\newcommand{\barBgeom}{\bar{\mathbf{B}}}
\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
\newcommand{\Ran}{\operatorname{Ran}}
\newcommand{\MC}{\operatorname{MC}}
\newcommand{\Res}{\operatorname{Res}}
\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
\DeclareMathOperator{\CoDer}{CoDer}

\title{Vol I Notation Index}
exec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp standalone/notation_index.tex' in /Users/raeez/chiral-bar-cobar succeeded in 297ms:
)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/longtable.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/refcount/refcount.sty)
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..351388852a35a35b2c0bad9c683eb62444425162
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}



thinking
**Adjusting column widths**

I need to fix the build that's passing with overfull boxes. It seems the total column widths exceed the available width. I could adjust them to reduce overflow—maybe trying widths like 0.24, 0.48, and 0.20 totals to 0.92. Alternatively, I might consider using `@{}` to eliminate some intercolumn padding, which could simplify the layout. If I modify the longtable preamble correctly, it could help avoid those overflow warnings and keep everything aligned well.
thinking
**Fixing column widths**

I’m thinking about adjusting the column widths to 0.24, 0.46, and 0.20, which sums to 0.90. That seems like a good fit since it fits within the limit of 345. After calculating, 0.90 times 345 equals 310.5, and adding the extra 24pt brings us to 334.5, still under the 345 limit. The table might wrap a bit more, but that should be manageable. Alright, let’s go ahead and implement this change!
codex
The isolated build passed, but it reported avoidable layout overflow in the table preamble. I’m tightening the column widths so the standalone file verifies cleanly without warnings that come from the table geometry itself.
file update
M /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
@@ -40,3 +40,3 @@
 
-\begin{longtable}{>{\raggedright\arraybackslash}p{0.26\textwidth} >{\raggedright\arraybackslash}p{0.50\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
 \toprule
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

exec
/bin/zsh -lc "grep -n 'Overfull \\\\hbox' /tmp/notation_index.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '34,46p' standalone/notation_index.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\bigskip

\small
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\renewcommand{\arraystretch}{1.15}

\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
\toprule
\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
\midrule
\endfirsthead
\toprule
 succeeded in 52ms:
394:Overfull \hbox (17.20576pt too wide) in alignment at lines 41--45
399:Overfull \hbox (17.20576pt too wide) in alignment at lines 45--49
404:Overfull \hbox (17.20576pt too wide) in alignment at lines 49--51
413:Overfull \hbox (17.20576pt too wide) in alignment at lines 51--181
exec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp standalone/notation_index.tex' in /Users/raeez/chiral-bar-cobar succeeded in 363ms:
entering extended mode
(./standalone/notation_index.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/article.cls
Document Class: article 2024/06/29 v1.4n Standard LaTeX document class
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/longtable.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}


thinking
**Investigating log issues**

I'm finding it interesting that the grep command on the log is still showing old overfull lines. It makes me wonder if the log had some old content appended. Actually, pdflatex output indicated underfull issues instead of overfull, which suggests the grep found overfulls from an earlier run that may not have been truncated. I could try cleaning the old log or check the line numbers in the current log to see what's up.
codex
The second build is successful. The remaining log noise is layout-only table alignment chatter, not a TeX error, but I’m checking whether it is stale output from the earlier run or a real current warning before I close the loop.
exec
/bin/zsh -lc "grep -n 'Underfull \\\\hbox' /tmp/notation_index.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '388,418p' /tmp/notation_index.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
394:Underfull \hbox (badness 10000) in alignment at lines 41--45
399:Underfull \hbox (badness 10000) in alignment at lines 45--49
404:Underfull \hbox (badness 10000) in alignment at lines 49--51
413:Underfull \hbox (badness 10000) in alignment at lines 51--181
 succeeded in 51ms:
LaTeX Font Info:    Trying to load font information for U+msb on input line 26.


(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsb.fd
File: umsb.fd 2013/01/14 v3.01 AMS symbols B
)
Underfull \hbox (badness 10000) in alignment at lines 41--45
[] [] []
 []


Underfull \hbox (badness 10000) in alignment at lines 45--49
[] [] []
 []


Underfull \hbox (badness 10000) in alignment at lines 49--51
[] [] []
 []

exec
/bin/zsh -lc "stat -f '%Sm %N' /tmp/notation_index.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Apr 13 19:29:31 2026 /tmp/notation_index.log
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}


thinking
**Evaluating status and updates**

I see that it's only underfull, and that might not need any serious fixes. I wonder if I could use `@{}` to remove any warnings. Maybe I can check the git diff and reference specific lines in my final response. It might be a good idea to update the plan to mark it as completed. I’m curious if that would streamline everything and help ensure clarity!
Plan update
Pinned the first explicit definitions, wrote the standalone notation index, and verified the new file with an isolated build to `/tmp`.
  ✓ Map included theory files and extract candidate core notation from `main.tex` and `chapters/theory/`.
  ✓ Pin the first definitional occurrence and line number for each retained symbol.
  ✓ Write `standalone/notation_index.tex` with a concise notation table.
  ✓ Verify the new file for scope, formatting, and source references.
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}



thinking
**Drafting findings and edits**

I need to prepare a report that includes git diff or file line numbers for reference. The user specifically asked for problems at certain locations in the file, along with the exact edits made. 

I should mention two key findings: 

1. There's a problem at [standalone/notation_index.tex:1] — the file is missing. The exact edit I applied involved creating a standalone document with a longtable of notation entries and citations.

2. At [standalone/notation_index.tex:10-29], I fixed undefined macros and replaced backticks with proper commands. 

I might note a warning about table widths too!
thinking
**Addressing table width issues**

There’s an issue with table column widths causing alignment overflow in the isolated build. I changed the longtable widths from `0.26/0.50/0.20` to `0.24/0.46/0.20`. 

I should verify that the command `pdflatex -output-directory=/tmp standalone/notation_index.tex` passed since no artifacts were left behind. The build succeeded but I still have underfull alignment warnings, which aren't errors but might need attention. 

Should I fix those? They could arise from raggedright p-columns in the longtable. Perhaps I can address those with tweaks like `\setlength{\emergencystretch}`?
exec
/bin/zsh -lc "nl -ba standalone/notation_index.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\documentclass[11pt]{article}
     2	
     3	\usepackage{amsmath,amssymb}
     4	\usepackage{booktabs}
     5	\usepackage{longtable}
     6	\usepackage{array}
     7	\usepackage[margin=1in]{geometry}
     8	\usepackage[hidelinks]{hyperref}
     9	
    10	\newcommand{\cA}{\mathcal{A}}
    11	\newcommand{\barB}{\overline{B}}
    12	\newcommand{\barBgeom}{\bar{\mathbf{B}}}
    13	\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
    14	\newcommand{\Ran}{\operatorname{Ran}}
    15	\newcommand{\MC}{\operatorname{MC}}
    16	\newcommand{\Res}{\operatorname{Res}}
    17	\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
    18	\DeclareMathOperator{\CoDer}{CoDer}
    19	
    20	\title{Vol I Notation Index}
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}



thinking
**Addressing LaTeX issues**

I'm tackling some problems with the `notation_index.tex` file. There were undefined local macros, so I added those definitions and changed Markdown backticks to `\texttt{}`. For another issue, the table geometry produced warnings in my build, so I tightened the column widths.

Now, I want to focus on verification and possibly include clickable links to the file and specific line numbers where I've made changes. I think referencing the newly created file is helpful, but I may skip the missing file line if it didn’t exist originally.
thinking
**Refining document output**

I made some edits to the column widths for the standalone build to keep it clean. I should confirm that the file was written successfully with a verification command that showed no errors, just some minor warnings about table alignment. If it's clean, maybe I should mention the warnings. It could help to note that there are 31 entries and source citations mentioned, but I need to avoid overdoing it with detail. I just need to finalize it!
codex
- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:1): no Vol I notation index existed. `EXACT edit applied`: created a standalone LaTeX document that lists the core symbols from `main.tex` and `chapters/theory/`, with columns for symbol, meaning, and first explicit definition at `file:line`.

- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:12): the standalone file needed its own local symbol definitions, and the prose note used Markdown-style backticks, which are not valid repository-style LaTeX. `EXACT edit applied`: added local macros for `\barBgeom` and `\barBch`, and rewrote the scope note with `\texttt{main.tex}` and `\texttt{chapters/theory/}`.

- `PROBLEM` at [standalone/notation_index.tex](/Users/raeez/chiral-bar-cobar/standalone/notation_index.tex:41): the initial table geometry was too wide for the page. `EXACT edit applied`: tightened the `longtable` column widths to `0.24/0.46/0.20\textwidth`.

Verification: `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp standalone/notation_index.tex` succeeds. The output PDF was written to `/tmp`, so no extra repo artifacts were created.
file update:
diff --git a/standalone/notation_index.tex b/standalone/notation_index.tex
new file mode 100644
index 0000000000000000000000000000000000000000..f2d2ed2a8bcf40e90d64f3f6c8e2e5ecaeb189f8
--- /dev/null
+++ b/standalone/notation_index.tex
@@ -0,0 +1,183 @@
+\documentclass[11pt]{article}
+
+\usepackage{amsmath,amssymb}
+\usepackage{booktabs}
+\usepackage{longtable}
+\usepackage{array}
+\usepackage[margin=1in]{geometry}
+\usepackage[hidelinks]{hyperref}
+
+\newcommand{\cA}{\mathcal{A}}
+\newcommand{\barB}{\overline{B}}
+\newcommand{\barBgeom}{\bar{\mathbf{B}}}
+\newcommand{\barBch}{\bar{B}^{\mathrm{ch}}}
+\newcommand{\Ran}{\operatorname{Ran}}
+\newcommand{\MC}{\operatorname{MC}}
+\newcommand{\Res}{\operatorname{Res}}
+\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
+\DeclareMathOperator{\CoDer}{CoDer}
+
+\title{Vol I Notation Index}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+This index is scoped to the notation introduced in \texttt{main.tex} and
+\texttt{chapters/theory/}.
+Line references record the first explicit definitional occurrence on that
+surface, following Vol I document order from \texttt{main.tex}.
+Earlier motivational mentions are ignored when a later line gives the first
+actual symbol declaration or formula.
+
+\bigskip
+
+\small
+\setlength{\LTleft}{0pt}
+\setlength{\LTright}{0pt}
+\renewcommand{\arraystretch}{1.15}
+
+\begin{longtable}{>{\raggedright\arraybackslash}p{0.24\textwidth} >{\raggedright\arraybackslash}p{0.46\textwidth} >{\raggedright\arraybackslash}p{0.20\textwidth}}
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endfirsthead
+\toprule
+\textbf{Symbol} & \textbf{Meaning} & \textbf{First defined at} \\
+\midrule
+\endhead
+\bottomrule
+\endfoot
+
+$\barBgeom(\cA)$
+& geometric bar complex
+& \path{main.tex:824} \\
+
+$\barBch(\cA)$
+& abstract chiral bar complex, used when the distinction from the geometric model matters
+& \path{main.tex:825} \\
+
+$\overline{C}_n(X)$
+& compactified configuration space
+& \path{main.tex:826} \\
+
+$\eta_{ij} = d\log(z_i-z_j)$
+& logarithmic $1$-form used as the basic bar propagator
+& \path{main.tex:827} \\
+
+$d_0$
+& genus-$0$ collision differential
+& \path{main.tex:500} \\
+
+$d_{\mathrm{fib}}$
+& fiberwise curved differential on a fixed genus-$g$ curve
+& \path{main.tex:501} \\
+
+$D_g$
+& total corrected differential at genus $g$
+& \path{main.tex:502} \\
+
+$\operatorname{Conv}_{\mathrm{str}}$
+& strict dg Lie model of the modular convolution deformation object
+& \path{main.tex:507} \\
+
+$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& modular convolution dg Lie algebra of $\cA$
+& \path{main.tex:511} \\
+
+$\barB_X(\cA)$
+& symmetric factorization bar coalgebra on unordered $\Ran(X)$; the unqualified bar notation in the geometric bar chapter
+& \path{chapters/theory/bar_construction.tex:84} \\
+
+$B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
+& ordered tensor bar; the primitive $E_1$ coalgebra whose $\Sigma_n$-coinvariants give the symmetric bar
+& \path{chapters/theory/bar_construction.tex:86} \\
+
+$\cA^i = H^*(\barB_X(\cA))$
+& dual coalgebra computed by bar cohomology
+& \path{chapters/theory/bar_construction.tex:90} \\
+
+$\cA^! = ((\cA^i)^\vee)$
+& Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:96} \\
+
+$\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$
+& Verdier dual of the symmetric bar, giving the homotopy Koszul dual algebra
+& \path{chapters/theory/bar_construction.tex:108} \\
+
+$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
+& cobar-bar counit; recovers $\cA$ itself rather than $\cA^!$
+& \path{chapters/theory/bar_construction.tex:135} \\
+
+$\tau \colon \barB_X(\cA) \to \cA$
+& canonical twisting morphism
+& \path{chapters/theory/bar_construction.tex:142} \\
+
+$\kappa(a,b) = a_{(1)}b$
+& invariant pairing extracting the double-pole residue of the chiral product
+& \path{chapters/theory/bar_construction.tex:206} \\
+
+$\Theta_\cA = D_\cA - d_\cA^{(0)}$
+& bar-intrinsic modular Maurer--Cartan element in $\mathfrak{g}_{\cA}^{\mathrm{mod}}$
+& \path{chapters/theory/introduction.tex:715} \\
+
+$\mathfrak{g}^{E_1}_\cA$
+& ordered $E_1$-modular convolution algebra carrying the full $R$-matrix data before coinvariants
+& \path{chapters/theory/introduction.tex:61} \\
+
+$\Theta_\cA^{E_1} = D_\cA^{E_1} - d_\cA^{(0)}$
+& ordered Maurer--Cartan lift retaining the non-averaged collision data
+& \path{chapters/theory/introduction.tex:1218} \\
+
+$\operatorname{av} \colon {\mathfrak{g}^{E_1}_\cA} \twoheadrightarrow \mathfrak{g}^{\mathrm{mod}}_\cA$
+& averaging map from ordered to coinvariant modular data
+& \path{chapters/theory/introduction.tex:1245} \\
+
+$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})$
+& degree-$2$, genus-$0$ collision residue; the classical $r$-matrix
+& \path{chapters/theory/introduction.tex:868} \\
+
+$\kappa(\cA) = \operatorname{av}(r(z))$
+& scalar modular characteristic extracted from the collision residue; the affine non-abelian Sugawara shift is handled later in the text
+& \path{chapters/theory/introduction.tex:1269} \\
+
+$\Theta_\cA^{\le r}$
+& finite-order truncation of the universal Maurer--Cartan class; the levels of the shadow obstruction tower
+& \path{chapters/theory/introduction.tex:1975} \\
+
+$\Delta = 8\kappa S_4$
+& critical discriminant governing finite versus infinite shadow depth
+& \path{chapters/theory/introduction.tex:80} \\
+
+$\ChirHoch^*(\cA)$
+& chiral Hochschild cohomology; in the introduction it is defined as the cohomology of coderivations of the bar coalgebra
+& \path{chapters/theory/introduction.tex:694} \\
+
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
+& derived chiral center; the bulk object computed by Hochschild cochains
+& \path{main.tex:787} \\
+
+$\omega_g = c_1(\mathbb{E})$
+& Hodge class governing fiberwise curvature
+& \path{chapters/theory/introduction.tex:53} \\
+
+$\lambda_g = c_g(\mathbb{E})$
+& top Chern, or Mumford, class of the Hodge bundle
+& \path{chapters/theory/higher_genus_foundations.tex:188} \\
+
+$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
+& scalar genus-$g$ obstruction class on the uniform-weight lane
+& \path{chapters/theory/higher_genus_foundations.tex:186} \\
+
+$\Lambda = \sum_{g \ge 1} \lambda_g$
+& universal Hodge-class series used in the scalar shadow package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:4670} \\
+
+$\mathcal{C}_{\cA} = (\Theta_\cA,\kappa(\cA),\Delta_\cA,\Pi_\cA,\mathcal{H}_\cA)$
+& full modular characteristic package: universal MC class, scalar characteristic, discriminant, periodicity profile, and Hilbert series package
+& \path{chapters/theory/higher_genus_modular_koszul.tex:2652} \\
+
+\end{longtable}
+
+\end{document}

tokens used
206,908
