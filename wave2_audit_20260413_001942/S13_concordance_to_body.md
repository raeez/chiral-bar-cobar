# S13_concordance_to_body (559s)

- [CRITICAL] chapters/connections/concordance.tex:2392 — PROBLEM: The heading `Unconditional equivalences (i)--(x)` is false on the live chapter surface. In `chapters/theory/chiral_koszul_pairs.tex:2021-2027`, only `(i)--(vii),(ix)--(x)` are equivalent; `chapters/theory/chiral_koszul_pairs.tex:2062-2072` isolates `(viii)` as an unconditional consequence on the Koszul locus, and `chapters/theory/chiral_koszul_pairs.tex:2117-2123` explicitly says no converse from `(viii)` is proved. The item now sitting in the equivalence block at `chapters/connections/concordance.tex:2426-2433` is status-inflated. FIX: rename the block to `Unconditional equivalences (i)--(vii),(ix)--(x)`, move the `item:kp-hochschild` paragraph into its own block headed `Unconditional consequence on the Koszul locus`, and add the chapter’s caveat that no converse from `(viii)` is proved.

- [CRITICAL] chapters/connections/concordance.tex:3214 — PROBLEM: The “core cycle” makes `(\ref{item:kp-hochschild})` part of an equivalence chain, contradicting `chapters/theory/chiral_koszul_pairs.tex:2022-2023` and `2117-2123`, where `(viii)` is consequence-only. FIX: rewrite the line to `(\ref{item:kp-def})\Leftrightarrow(\ref{item:kp-pbw})\Leftrightarrow(\ref{item:kp-ainfty})\Leftrightarrow(\ref{item:kp-barcobar})`, and change the next sentence so Hochschild is a one-way output: `(\ref{item:kp-barcobar})\Rightarrow(\ref{item:kp-hochschild}) on the Koszul locus`, not a return arrow to Koszul-complex acyclicity.

- [HIGH] chapters/connections/concordance.tex:2416 — PROBLEM: Item `(vi)` drops the fiber restriction and says the Barr--Beck--Lurie comparison “is an equivalence”. The chapter states only the fibered version: `chapters/theory/chiral_koszul_pairs.tex:2048-2050` says the comparison is an equivalence `on the fiber over \barBgeom(\cA)`. FIX: replace the item text with `Barr--Beck--Lurie comparison for \barBch\dashv\Omegach is an equivalence on the fiber over \barBgeom(\cA)`.

- [HIGH] chapters/connections/concordance.tex:2421 — PROBLEM: Item `(vii)` overstates the scope to `\int_X\cA` “for all smooth X”. The live chapter narrows this: `chapters/theory/chiral_koszul_pairs.tex:2051-2052` states `\int_{\mathbb{P}^1}\cA` is concentrated in degree `0`, and `2185-2196` says the unconditional equivalence is only the `g=0` specialization; higher genus needs the uniform-weight hypothesis. FIX: replace the item with `Factorization homology \int_{\mathbb{P}^1}\cA is concentrated in degree~0`, and append `the intended equivalence is the genus-0 specialization; see Remark~\ref{rem:fh-vii-uniform-weight-scope}`.

- [HIGH] chapters/connections/concordance.tex:2451 — PROBLEM: The line cites `Theorem~\ref{conj:lagrangian-koszulness}` even though the source is a conjecture: `chapters/theory/bar_cobar_adjunction_inversion.tex:2823-2825` is `\begin{conjecture}...\label{conj:lagrangian-koszulness}`, and `chapters/theory/chiral_koszul_pairs.tex:2024-2027` treats `(xi)` as conditional. FIX: change the citation to `Conjecture~\ref{conj:lagrangian-koszulness}`, rename the item `Lagrangian criterion`, and keep unconditional status only via `Proposition~\ref{prop:lagrangian-perfectness}` and `Corollary~\ref{cor:lagrangian-unconditional}`.

- [HIGH] chapters/connections/concordance.tex:3197 — PROBLEM: The status summary says `ten equivalences`, but the chapter introduction `chapters/theory/chiral_koszul_pairs.tex:61-73` and the live theorem statement `2021-2027` give `9 + 1 + 1 + 1`: nine unconditional equivalences, one proved consequence, one conditional equivalence, one one-directional condition. FIX: replace the sentence with `nine unconditional equivalences (i)--(vii),(ix)--(x); item (viii) is an unconditional consequence on the Koszul locus; item (xi) is conditional in general and unconditional on the standard landscape; item (xii) is one-directional`.

- [MEDIUM] chapters/connections/concordance.tex:2387 — PROBLEM: The seam promises that the item numbering in concordance and chapter is identical, but `chapters/theory/chiral_koszul_pairs.tex:2031-2059,2063-2083` has no `\label{item:kp-*}` anchors at all. The concordance numbering exists only locally. FIX: add `\label{item:kp-def}`, `item:kp-pbw`, `item:kp-ainfty`, `item:kp-ext`, `item:kp-barcobar`, `item:kp-barrbeck`, `item:kp-facthom`, `item:kp-hochschild`, `item:kp-nullvec`, `item:kp-fmbdy`, `item:kp-lagrangian`, and `item:kp-dmod` to the twelve `\item[...]` lines in `chapters/theory/chiral_koszul_pairs.tex`.

- [MEDIUM] chapters/connections/concordance.tex:2385 — PROBLEM: The concordance enters the meta-theorem seam with no routing remark for the chapter’s circularity control. The live chapter is explicit that no bar-cobar quasi-isomorphism is built into the definition (`chapters/theory/chiral_koszul_pairs.tex:623`), that the hypotheses are antecedent (`647-654`), and that the circularity-free construction is carried out in `3935-4405`; none of that is surfaced here. FIX: insert immediately after line 2389: `Routing note: Definition~\ref{def:chiral-koszul-pair} uses only antecedent twisting/Koszul/Verdier data; no bar-cobar quasi-isomorphism is built into the definition. See \S\ref{sec:three-stage-construction}, especially Corollary~\ref{cor:circularity-free-koszul}, for the circularity-free construction.`

## Summary
Checked: 15 | Findings: 8 | Verdict: FAIL


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
session id: 019d83d4-c236-7b33-a4d9-9906889ea63f
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


MISSION: SEAM AUDIT between concordance.tex and chiral_koszul_pairs.tex.

Concordance→Theory. Check: (a) every theorem status in concordance matches the actual .tex, (b) no stale statuses, (c) routing remarks present for circular dependencies

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers



thinking
**Auditing files for user requests**

I need to act as a coding agent since the user wants an audit between two specific files: concordance.tex and chiral_koszul_pairs.tex. It seems I’m expected to read these files carefully and produce findings without making edits. The user mentions they want an "exact fix," but likely they just want an audit. I'll follow repository instructions, which means I should read relevant documents like CLAUDE.md first. I might need to use special skills and tools to inspect the files thoroughly.
thinking
**Planning the file audit**

Since I won’t be coding, I think I can still use an explorer tool for a fast and authoritative search through the files. I might want to use multi_tool_use.parallel to read files quickly. It’s important to avoid nested bullets in the final output, focusing first on the findings without any fluff. I should include exact file and line references, grounding all claims in actual content to avoid guesses. I need to carefully compare the theorem statuses in both files, looking for inconsistencies, gaps, and specific routing remarks regarding circular dependencies. This could involve only entries in concordance that reference chiral_koszul_pairs too.
thinking
**Cross-checking theorem registry**

I should consider cross-checking the theorem_registry as well. The mission is to ensure the seam between concordance and chapter aligns with the actual theorem statuses in .tex files, verifying that there are no stale statuses and that routing remarks for circular dependencies are present. This seems relevant for accurate checks. Reading the theorem_registry might help confirm the statuses. I might also use `rg` to find references to `chiral_koszul_pairs` in both concordance and the theorem registry.
codex
Using `deep-beilinson-audit` and `claim-surface-sync` because this is a seam audit on theorem-status surfaces. First I’m loading the constitutional files, locating every concordance entry that routes into `chiral_koszul_pairs.tex`, and then I’ll compare those statuses and transition remarks against the live chapter text line by line.
exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs|koszul pairs|Koszul pairs|thm:|prop:|conj:" chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files | rg 'CLAUDE\\.md|concordance\\.tex|theorem_registry\\.md|red_team_summary\\.md|chiral_koszul_pairs\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 3044

chapters/connections/concordance.tex:34: \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
chapters/connections/concordance.tex:39: \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
chapters/connections/concordance.tex:44: $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
chapters/connections/concordance.tex:49: \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
chapters/connections/concordance.tex:62: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
chapters/connections/concordance.tex:68: \textup{(}Thms~\ref{thm:w-algebra-hochschild},
chapters/connections/concordance.tex:69: \ref{thm:virasoro-hochschild},
chapters/connections/concordance.tex:70: \ref{thm:critical-level-cohomology};
chapters/connections/concordance.tex:71: Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
chapters/connections/concordance.tex:88:(Theorem~\ref{thm:modular-homotopy-convolution}). The universal
chapters/connections/concordance.tex:90:construction (Theorem~\ref{thm:mc2-bar-intrinsic}:
chapters/connections/concordance.tex:167: (Theorem~\ref{thm:riccati-algebraicity}).
chapters/connections/concordance.tex:179: (Theorem~\ref{thm:shadow-formality-identification}).
chapters/connections/concordance.tex:188: (Theorem~\ref{thm:quantum-complementarity-main}).
chapters/connections/concordance.tex:204:(Theorem~\ref{thm:single-line-dichotomy}:
chapters/connections/concordance.tex:238:(Theorem~\ref{thm:oper-bar-h0-dl}) is the bar \emph{cohomology}
chapters/connections/concordance.tex:263: (Theorems~\ref{thm:bar-cobar-isomorphism-main}
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/master_concordance.tex
chapters/connections/concordance.tex
chapters/theory/chiral_koszul_pairs.tex

thinking
**Locating relevant references**

I need to inspect the relevant sections in the concordance and chapter while gathering line numbers. It seems like using explorer agents could help me search for file relations. I should focus on finding concordance lines related to "chiral_koszul_pairs." The theorem registry might contain the chapter lines, but I'd need exact statuses, possibly through macros within theorem headings. I should ask the explorer to identify all concordance entries relating to chiral_koszul_pairs and any status or routing remarks. It might work best to use multiple explorers in parallel.
codex
I have the target files and the registry hit list. Next I’m isolating the exact concordance block for `chiral_koszul_pairs.tex` and extracting every theorem/proposition/conjecture status plus any circular-dependency routing language so the comparison is on the live seam only.
collab spawn_agent(call_KO8VpWy2JTa2rl6iaWYYrYCv, prompt="Inspect chapters/theory/chiral_koszul_pairs.tex. Return: 1) every theorem/proposition/conjecture/remark/definition label…")
mcp startup: no servers
spawn_agent(call_KO8VpWy2JTa2rl6iaWYYrYCv, prompt="Inspect chapters/theory/chiral_koszul_pairs.tex. Return: 1) every theorem/proposition/conjecture/remark/definition label…") pending init:
  agent: 019d83d5-28b9-7f22-a041-02c2257be59e
collab spawn_agent(call_4F5Idv74DQnLS8Mn0K1s3ys1, prompt="Inspect chapters/connections/concordance.tex and identify the exact block(s) that describe chapters/theory/chiral_koszul…")
spawn_agent(call_4F5Idv74DQnLS8Mn0K1s3ys1, prompt="Inspect chapters/connections/concordance.tex and identify the exact block(s) that describe chapters/theory/chiral_koszul…") pending init:
  agent: 019d83d5-28e1-7950-8f9f-fd133569550d
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
bibliography
bp_self_duality.pdf
chapters
chiral_chern_weil.pdf
exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "theory/chiral_koszul_pairs" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
224:\begin{remark}[Explicit twisted differential]
252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
266:\begin{remark}[Construction versus resolution]\label{rem:construction-vs-resolution}
399:\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
513:\begin{remark}[Why the MC equation is Stokes' theorem]
536:\begin{remark}[Theorem~A decomposition]\label{rem:theorem-A-decomposition}
561:\begin{proposition}[Universal property of bar construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]
594:\begin{theorem}[Comparison lemma for chiral twisted products {\cite[Theorem~2.4.1]{LV12}}; \ClaimStatusProvedElsewhere]
625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
747:\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
819:\begin{remark}[Relation to classical Koszulness]
825:\begin{theorem}[Affine Kac--Moody algebras are chiral Koszul; \ClaimStatusProvedHere]
880:\begin{theorem}[Virasoro chiral Koszulness; \ClaimStatusProvedHere]
1077:\begin{remark}[CE cohomology vs exterior algebra dimensions]
1083:\begin{remark}[Chevalley--Eilenberg cohomology vs chiral bar cohomology]%
1112:\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
1205:\begin{remark}[One-loop exactness]
1224:\begin{proposition}[Formality implies chiral Koszulness; \ClaimStatusProvedHere]
1257:\begin{theorem}[Converse: chiral Koszulness implies formality;
exec
/bin/zsh -lc 'rg -n "chiral" chapters/connections/concordance.tex | head' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
102:\index{chiral Hochschild cohomology!distinguished from topological and categorical}%
117: Input: a chiral algebra~$\cA$ on a smooth curve~$X$
139:curve~$X$ $\to$ chiral,
150:\emph{topological}, \emph{chiral}, or
162:trace of~$\Theta_\cA$, and the chiral Hochschild ring is a
220:of the chiral theory (class~G, $r_{\max} = 2$) via
247:Within the chirally Koszul standard examples treated in
269: for all Koszul chiral algebras at all genera. Inversion is
275: chiral twisting morphisms
284: (Theorem~\ref{thm:quillen-equivalence-chiral});
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5949,6200p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{remark}[Dependency digest]\label{rem:ckp-dependency-digest}
\index{chiral Koszul pairs!dependency map}
This chapter provides the following results used by later chapters:
\begin{itemize}
\item $\mathrm{A}_0$: Fundamental theorem of chiral twisting morphisms
 (Theorem~\ref{thm:fundamental-twisting-morphisms}), used by
 Chapters~\ref{chap:higher-genus}, \ref{chap:chiral-modules}.
\item $\mathrm{A}_1$: Bar concentration
 (Theorem~\ref{thm:bar-concentration}), used by
 Theorem~$\mathrm{C}_0$
 (Theorem~\ref{thm:fiber-center-identification}).
\item $\mathrm{A}_2$: Geometric bar-cobar duality
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}), used
 everywhere.
\item Theorem~B: Higher genus inversion
 (Theorem~\ref{thm:higher-genus-inversion}) is
 proved in Chapter~\ref{chap:higher-genus} using the foundations
 above.
\item PBW Koszulness criterion
 (Theorem~\ref{thm:pbw-koszulness-criterion}), used by all
exec
/bin/zsh -lc "sed -n '230,320p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The Drinfeld--Kohno bridge recovers the classical $R$-matrix
as the genus-$0$ binary shadow projection
(Construction~\ref{constr:dk-shadow-projections};
DK-0/1 proved, DK-2/3 proved on the evaluation-generated core,
DK-4/5 conjectural).
The Feigin--Frenkel center
$H^0(\barB(\widehat{\fg}_{\critLevel})) \cong
\operatorname{Fun}(\operatorname{Op}_{\fg^\vee}(D))$
(Theorem~\ref{thm:oper-bar-h0-dl}) is the bar \emph{cohomology}
at the critical level $k = \critLevel$, where $\kappa = 0$
and the scalar class vanishes; it is orthogonal to the
full shadow obstruction tower, not a projection of it.
Algebraicity, the formality identification,
and Lagrangian complementarity have no classical analogue.

\medskip\noindent
\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
Within the chirally Koszul standard examples treated in
Part~\ref{part:physics-bridges} (Heisenberg, affine Kac--Moody,
$bc$-$\beta\gamma$, Virasoro, universal principal $\Walg_N$),
exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs|Koszul pairs|koszul pairs|thm:pbw-koszulness-criterion|thm:bar-cobar-inversion-qi|thm:main-koszul-hoch|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:ext-diagonal-vanishing|thm:kac-shapovalov-koszulness|thm:koszul-equivalences-meta|thm:operadic-complexity|thm:nms-archetype-trichotomy|thm:nms-finite-termination|thm:ds-bar-gf-discriminant|prop:n2-koszulness|prop:moonshine-kappa|prop:finite-jet-rigidity|prop:gaussian-collapse-abelian|conj:graph-complex-shadow" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
326: The Kodaira--Spencer map is constructed for all Koszul pairs
394: operator~$S$ (Theorem~\ref{thm:main-koszul-hoch},
819:\label{prop:finite-jet-rigidity}
880:\label{prop:gaussian-collapse-abelian}
1992:Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
2022: (Theorem~\ref{thm:nms-finite-termination}).
2116: the $(r{+}1)$-jet (Proposition~\ref{prop:finite-jet-rigidity})
2371:The PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion})
2385:Theorem~\ref{thm:koszul-equivalences-meta} in
2400: (Theorem~\ref{thm:pbw-koszulness-criterion}).
2404: (Theorem~\ref{thm:ainfty-koszul-characterization}).
2409: (Theorem~\ref{thm:ext-diagonal-vanishing}).
2414: (Theorem~\ref{thm:bar-cobar-inversion-qi}).
2428: (Theorem~\ref{thm:main-koszul-hoch}).
2436: (Theorem~\ref{thm:kac-shapovalov-koszulness}).
2480: (Theorem~\ref{thm:kac-shapovalov-koszulness}):
2518:\label{thm:operadic-complexity-concordance}%
2523:(Theorem~\ref{thm:nms-finite-termination}), $d_\infty$ is
2591:See Theorem~\ref{thm:nms-archetype-trichotomy}.
2974:(Proposition~\ref{prop:n2-koszulness},
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3110,3205p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
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
 succeeded in 52ms:
  3110	have been verified for the full multi-generator landscape:
  3111	$\nabla^{\mathrm{sh}}$ for Virasoro and $\cW_3$ (both T-line and
  3112	W-line), with residue $1/2$ and monodromy $-1$ confirmed;
  3113	$\delta_{\mathrm{mix}}$ for six families ($\cW_3$, $\cW_4$, $\cW_5$,
  3114	$\beta\gamma{+}bc$, $\cH{+}\mathrm{Vir}$,
  3115	$V(\mathfrak{sl}_2){+}V(\mathfrak{sl}_3)$); $\cW_4$ is never
  3116	autonomous at any real central charge.
  3117	Suites: \texttt{test\_shadow\_connection.py} (114 tests),
  3118	\texttt{test\_propagator\_variance\_landscape.py} (143 tests).
  3119	
  3120	
  3121	%% ------------------------------------------------------------------
  3122	\subsection{Cross-reference table}
  3123	\label{subsec:concordance-koszulness-xref}
  3124	
  3125	\begin{center}
  3126	\renewcommand{\arraystretch}{1.15}
  3127	\begin{tabular}{@{}p{3.6cm}lp{4.5cm}@{}}
  3128	\toprule
  3129	\textbf{Item} & \textbf{Label} & \textbf{Location} \\
exec
/bin/zsh -lc 'rg -n "Koszul" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
38: on the Koszul locus
56: for uniform-weight modular Koszul algebras
66: $P(t)=1+t^2$, Koszul-functorial;
121: modular Koszul algebras (Theorem~H).
163:polynomial consequence of Koszul functoriality.
189: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ partition
217:Classical Koszul duality (Priddy; Beilinson--Ginzburg--Soergel)
246:\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
247:Within the chirally Koszul standard examples treated in
252:Koszulness status:
269: for all Koszul chiral algebras at all genera. Inversion is
291: For a Koszul chiral algebra~$\cA$ with uniform-weight
323: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ obstructions
326: The Kodaira--Spencer map is constructed for all Koszul pairs
329:\item \emph{$\Eone$-chiral Koszul duality
337: Complete Koszul duality computations for all standard families:
348: Koszul despite nonvanishing $H^2_{\mathrm{CE}}$\textup{)},
393: Functorial under Koszul duality via the Connes
427: and homotopy-Koszulity of~$\mathsf{SC}^{\mathrm{ch,top}}$
429: explicit brace morphism with Koszul signs

exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs" -g"*" -n' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '150,340p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
% ================================================================
% SECTION 8.1: FROM THE HEISENBERG EXAMPLE TO GENERAL TWISTING DATA
% ================================================================


\section{From the Heisenberg example to general twisting data}
\label{sec:chiral-twisting-data}

The bar complex of $\mathcal{H}_k$ (Chapter~\ref{ch:heisenberg-frame},
Theorem~\ref{thm:frame-heisenberg-koszul-dual})
produces the coalgebra $\bar{B}(\mathcal{H}_k)
\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)$,
whose cohomology gives the Koszul dual algebra
$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$.
The bar-cobar counit
$\Omega_X(\bar{B}_X(\mathcal{H}_k)) \xrightarrow{\;\sim\;} \mathcal{H}_k$
is a quasi-isomorphism (recovering the original algebra, not its dual). Two structural features make this work:

\begin{enumerate}
\item The twisted tensor product
 succeeded in 4.71s:
.claude/worktrees/agent-a2a46b8f/compute/lib/km_chiral_bar.py:41:  - Cor cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a2a46b8f/compute/lib/km_chiral_bar.py:46:  - Thm thm:km-chiral-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-ac71dfbc/compute/lib/ainfty_transferred_structure.py:28:  - prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-ac71dfbc/compute/lib/bar_modular.py:9:See chiral_koszul_pairs.tex: thm:pbw-koszulness-criterion.
.claude/worktrees/agent-a992e05a/compute/lib/ainfty_transferred_structure.py:28:  - prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/compute/lib/virasoro_bar_explicit.py:50:  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a992e05a/compute/lib/bar_modular.py:9:See chiral_koszul_pairs.tex: thm:pbw-koszulness-criterion.
.claude/worktrees/agent-ac71dfbc/compute/lib/km_chiral_bar.py:41:  - Cor cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
.claude/worktrees/agent-ac71dfbc/compute/lib/km_chiral_bar.py:46:  - Thm thm:km-chiral-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a992e05a/compute/lib/km_chiral_bar.py:41:  - Cor cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a992e05a/compute/lib/km_chiral_bar.py:46:  - Thm thm:km-chiral-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/compute/lib/ainfty_transferred_structure.py:28:  - prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/compute/lib/bar_modular.py:9:See chiral_koszul_pairs.tex: thm:pbw-koszulness-criterion.
.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/compute/lib/km_chiral_bar.py:41:  - Cor cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/compute/lib/km_chiral_bar.py:46:  - Thm thm:km-chiral-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_landscape.py:4:(thm:pbw-koszulness-criterion, chiral_koszul_pairs.tex) for each
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_landscape.py:59:    thm:pbw-koszulness-criterion (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_landscape.py:60:    prop:pbw-universality (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_landscape.py:61:    cor:universal-koszul (chiral_koszul_pairs.tex)
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_landscape.py:62:    thm:kac-shapovalov-koszulness (chiral_koszul_pairs.tex)
thinking
**Searching for theorem data**

I need more lines from the chiral_koszul_pairs file since I've only got the first 260 lines. It seems the file is likely much longer, and I want to make sure I have all the theorem labels and their statuses. I might ask the agent for help with this. I should inspect all relevant theorem environments in the chapter and search for specific labels of interest using rg. Let’s get this done!
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}|\\\\label\\{(thm:pbw-koszulness-criterion|thm:bar-cobar-inversion-qi|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:ext-diagonal-vanishing|thm:kac-shapovalov-koszulness|rem:dq-koszul-compatibility|thm:koszul-equivalences-meta)\\}\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '260,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2360,2418p'" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:\begin\{(theorem|proposition|conjecture|remark|definition)\}|\label\{(thm:pbw-koszulness-criterion|thm:bar-cobar-inversion-qi|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:ext-diagonal-vanishing|thm:kac-shapovalov-koszulness|rem:dq-koszul-compatibility|thm:koszul-equivalences-meta)\})
                                                                    ^^
error: unrecognized escape sequence
 succeeded in 50ms:
  2360	\end{proposition}
  2361	
  2362	
  2363	%% ====================================================================
  2364	%% INTRINSIC KOSZULNESS: THE CHARACTERIZATION PROGRAMME
  2365	%% ====================================================================
  2366	\section{Intrinsic Koszulness: the characterization programme}
  2367	\label{sec:concordance-koszulness-programme}
  2368	\index{Koszul property!characterization programme|textbf}
  2369	\index{chiral Koszulness!intrinsic characterization|textbf}
  2370	
  2371	The PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion})
  2372	detects chiral Koszulness for every standard family but does
  2373	not characterize it intrinsically. This section is the
  2374	constitutional index for the intrinsic characterization
  2375	programme. Full statements and proofs live in the source
  2376	chapters cited below.
  2377	
  2378	%% ------------------------------------------------------------------
  2379	\subsection{The meta-theorem: twelve characterizations}
 succeeded in 50ms:
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
exec
/bin/zsh -lc "rg -n \"chiral_koszul_pairs\\.tex\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "bar-cobar-isomorphism" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
34: \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
263: (Theorems~\ref{thm:bar-cobar-isomorphism-main}
280: ($\mathrm{A}_2$, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
564:Our Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the
4549:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) for boundary
4706:$A_{\mathrm{mod}}$ & Bar-cobar intertwined with Verdier, & \textbf{Proved} & Thm~\ref{thm:bar-cobar-isomorphism-main} \\
4920:$\operatorname{Ran}(X)$. Theorem~\ref{thm:bar-cobar-isomorphism-main}
9779: (Theorems~\textup{\ref{thm:bar-cobar-isomorphism-main}}
11208: (Theorem~\ref{thm:bar-cobar-isomorphism-main}),
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3200,3350p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
\index{Sklyanin bracket!Poisson rigidity}

The Koszulness meta-theorem
(Theorem~\ref{thm:koszul-equivalences-meta}) characterizes chiral
Koszulness intrinsically, through the bar complex and its spectral
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '980,1700p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2418,2468p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:pbw-koszulness-criterion|thm:bar-cobar-inversion-qi|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:ext-diagonal-vanishing|thm:kac-shapovalov-koszulness|rem:dq-koszul-compatibility|thm:koszul-equivalences-meta|conj:graph-complex-shadow)\\}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
748:\label{thm:pbw-koszulness-criterion}
1225:\label{prop:ainfty-formality-implies-koszul}
1259:\label{thm:ainfty-koszul-characterization}%
1329:\label{thm:ext-diagonal-vanishing}%
1458:\label{thm:kac-shapovalov-koszulness}
1641:\label{rem:dq-koszul-compatibility}
2016:\label{thm:koszul-equivalences-meta}
 succeeded in 53ms:
  2418	 (Theorem~\ref{thm:barr-beck-lurie-koszulness}).
  2419	 Conservativity + totalization on log-FM strata.
  2420	 \hfill \checkmark
  2421	\item\label{item:kp-facthom}
  2422	 Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
  2423	 (Theorem~\ref{thm:fh-concentration-koszulness}).
  2424	 Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  2425	 \hfill \checkmark
  2426	\item\label{item:kp-hochschild}
  2427	 $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
  2428	 (Theorem~\ref{thm:main-koszul-hoch}).
  2429	 For single-generator algebras with no simple pole in the OPE,
  2430	 $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
  2431	 the zero mode is central); for algebras with simple poles,
  2432	 $\ChirHoch^1 = 0$ (all derivations inner).
  2433	 \hfill \checkmark
  2434	\item\label{item:kp-nullvec}
  2435	 Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
  2436	 (Theorem~\ref{thm:kac-shapovalov-koszulness}).
  2437	 Non-degeneracy forces PBW injectivity; $d_r$-exactness contradicts pairing.
 succeeded in 53ms:
   980	\operatorname{gr}_F \barBgeom(\cA) \;\cong\;
   981	\barBgeom(\operatorname{gr}_F \cA)
   982	\;=\; \barBgeom(\operatorname{Sym}^{\mathrm{ch}}(V))
   983	\end{equation}
   984	where $V$ is the generating $\mathcal{D}_X$-module.
   985	This identification holds because the bar differential on the
   986	associated graded sees only the leading-order OPE terms.
   987	For $\widehat{\fg}_k$: the singular OPE
   988	$J^a(z) J^b(w) \sim f^{ab}_c J^c(w)/(z-w)
   989	+ k\kappa^{ab}/(z-w)^2$
   990	reduces on $\operatorname{gr}_F$ to the commutative product
   991	(the bracket $f^{ab}_c J^c$ and level term $k\kappa^{ab}$ are
   992	lower-order in the PBW filtration).
   993	For $\mathrm{Vir}_c$: similarly, the Virasoro OPE reduces to a
   994	commutative product on the associated graded.
   995	
   996	\emph{Step~3: Computation of the $E_1$ page.}
   997	The $E_0$ page is
   998	$E_0^{p,q} = \operatorname{gr}^p_F \barBgeom^{p+q}(\cA)$,
   999	with $d_0$ the associated-graded bar differential.
exec
/bin/zsh -lc "sed -n '1,200p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
/bin/zsh -lc 'rg -n "chiral Koszul pair" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Chiral Koszul" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
488:Chiral Koszul duality & Chiral Koszul duality (same) \\
7263:\item \textbf{Chiral Koszulness from (H1)--(H4).}
7294: Chiral Koszulness is an $A_\infty$ homotopy invariant:
10254:\item \textbf{Chiral Koszulness of simple quotients at admissible levels}
exec
/bin/zsh -lc "sed -n '430,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (\S\ref{sec:chiral-center-theorem}).

\end{enumerate}

\begin{remark}[Geometric Langlands connection]%
\label{rem:oper-langlands-concordance}
\index{geometric Langlands!oper from bar complex}%
\index{oper!concordance summary}%
The bar complex
$\barB(\widehat{\fg}_{-h^\vee})$ at critical level is a
\emph{chain-level enhancement} of the Feigin--Frenkel center:
it encodes functions on the oper space (in $H^0$),
K\"ahler differentials (in $H^1$), and higher exterior forms
(in $H^{\geq 2}$), reproducing the oper differential-form
package central to the Langlands programme
(Theorem~\ref{thm:oper-bar}).
\end{remark}

\begin{remark}[The twisting morphism as organizing datum]
\label{rem:tau-protagonist}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python - <<'PY'
import re, pathlib
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
results = []
for i,line in enumerate(lines):
    m = pattern.search(line)
    if not m:
        continue
    env = m.group(1)
    heading = None
    claim_statuses = []
    # capture heading argument if exists
    rest = line[m.end():]
    start = rest.find('[')
    end = -1
    j = i
    if start "'!= -1:
        buf = rest[start+1:]
        # look for closing bracket
        while True:
            idx = buf.find('"']')
            if idx "'!= -1:
                heading = buf[:idx]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    # find claim statuses if heading present
    if heading:
        claim_statuses = re.findall(r'\\\\ClaimStatus\\w+', heading)
    # find label in lines until next blank? search next 6 lines maybe
    label = None
    for k in range(i, min(len(lines), i+20)):
        lab_match = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab_match:
            label = lab_match.group(1)
            break
    results.append((i+1, env, label, claim_statuses))
# print
for entry in results:
    print(entry)
print('Total envs', len(results))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
codex
The seam is narrower than the raw registry list: concordance has a dedicated intrinsic-Koszulness block plus a cross-reference table that points into `chap:koszul-pairs`. I’m now checking whether those summaries actually agree with the live meta-theorem and nearby remarks in `chiral_koszul_pairs.tex`, especially the conditional items and any routing language that prevents circularity.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1960,2115p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"circular|cycle|circularity|routing|antecedent hypotheses|Theorem A decomposition|No quasi-isomorphism statement is built into the definition|proves the full bar-cobar identification as a consequence|Remark~\\\\ref\\{rem:construction-vs-resolution\\}|Theorem~\\\\ref\\{thm:bar-cobar-isomorphism-main\\} then\" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2468,2538p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1960	$\mathbb{O}_{\mathrm{subreg}}$ & $(N{-}1, 1)$ &
  1961	 reduced Li--bar concentration open & nilradical-dependent \\
  1962	$\mathcal{N}$ & $(N)$ &
  1963	 reduced Li--bar concentration open & nilradical-dependent \\
  1964	\bottomrule
  1965	\end{tabular}
  1966	\end{center}
  1967	
  1968	\smallskip\noindent
  1969	The reduced orbit geometry can still provide useful input, but
  1970	the present theorem does not identify the reduced Li--bar
  1971	$E_2$ page with ordinary Poisson cohomology or with
  1972	$H^*(\widetilde{\mathbb{O}}, \mathcal{O}_{\widetilde{\mathbb{O}}})$
  1973	for a symplectic resolution. What it does show is that any
  1974	reduced-level diagonal-concentration statement constrains only the
  1975	reduced Li--bar page and leaves nilradical contributions as a
  1976	separate obstruction.
  1977	
  1978	A conjectural type-$A$ orbit-duality principle
  1979	\textup{(}Conjecture~\textup{\ref{conj:orbit-duality}}\textup{)}
 succeeded in 51ms:
  2468	
  2469	Two sufficient conditions for chiral Koszulness are established:
  2470	\begin{enumerate}[label=\textup{(\alph*)}]
  2471	\item \emph{PBW universality}
  2472	 (Proposition~\ref{prop:pbw-universality}):
  2473	 freely strongly generated vertex algebras are chirally Koszul.
  2474	 Applies to the \emph{universal} algebras $V_k(\fg)$ (all $k$),
  2475	 $\mathrm{Vir}_c$ (all $c$), $\mathcal{W}^k(\fg)$ (Miura free
  2476	 generators). The simple quotient $L_k(\fg) = V_k(\fg)/I_k$
  2477	 is \emph{not} freely strongly generated when the null-vector ideal
  2478	 $I_k$ is nontrivial, and PBW universality does not apply to it.
  2479	\item \emph{Kac--Shapovalov criterion}
  2480	 (Theorem~\ref{thm:kac-shapovalov-koszulness}):
  2481	 $\det G_h \neq 0$ in the bar-relevant range.
  2482	 Applies to: $V_k(\fg)$, $\mathrm{Vir}_c$ at generic $c$.
  2483	 For simple quotients at admissible levels, null vectors enter the
  2484	 bar-relevant range and this route is blocked.
  2485	\end{enumerate}
  2486	
  2487	\noindent\textbf{Simple quotients at admissible levels.}
 succeeded in 52ms:
chapters/connections/concordance.tex:585: cycles. The AF framework predicts this (factorization homology
chapters/connections/concordance.tex:902:with pairing determined by the cocycle of~$R$.
chapters/connections/concordance.tex:2126: on specific moduli cycles. The five-component differential
chapters/connections/concordance.tex:2973:provide coboundaries that kill the CE cocycles
chapters/connections/concordance.tex:3214:The core cycle
chapters/connections/concordance.tex:4871:\emph{Non-circular logical chain.}
chapters/connections/concordance.tex:4873:is free of circularity
chapters/connections/concordance.tex:4874:(Remark~\ref{rem:non-circular-logical-chain}).
chapters/connections/concordance.tex:4898:Remark~\ref{rem:non-circular-logical-chain}).
chapters/connections/concordance.tex:5307:degree-$2$ cocycle on each side together with bar-length-$\leq 3$
chapters/connections/concordance.tex:5318:functorial normalization splitting off the one-channel cocycle line.
chapters/connections/concordance.tex:7029: & CohFT string equation at rank $1$ & DR cycle forgetful $+$ Buryak DR/DZ \\
chapters/connections/concordance.tex:7384: filtration); the resulting spectral $3$-cocycles are
chapters/connections/concordance.tex:8843:satisfying the \emph{nilpotent $N$-cycle relation}
chapters/connections/concordance.tex:8844:\begin{equation}\label{eq:nilpotent-N-cycle}
chapters/connections/concordance.tex:8860:The nilpotent $N$-cycle \eqref{eq:nilpotent-N-cycle}
chapters/theory/chiral_koszul_pairs.tex:623:No quasi-isomorphism statement is built into the definition itself.
chapters/theory/chiral_koszul_pairs.tex:647:These are \emph{antecedent hypotheses}: the twisting data
chapters/theory/chiral_koszul_pairs.tex:1099:(the three independent cocycles $L_{-1}^*, L_{-2}^*, L_{-3}^*$
chapters/theory/chiral_koszul_pairs.tex:1108:which collapses the three CE cocycles to the single
exec
/bin/zsh -lc 'rg -n "Chiral Koszul pairs" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "chap:chiral" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
1645: (Chapter~\ref{chap:chiral-deformation})
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
results = []
for i,line in enumerate(lines):
    m = pattern.search(line)
    if not m:
        continue
    env = m.group(1)
    heading = None
    claim_statuses = []
    # capture heading argument if exists
    rest = line[m.end():]
    start = rest.find('[')
    j = i
    if start "'!= -1:
        buf = rest[start+1:]
        while True:
            idx = buf.find('"']')
            if idx "'!= -1:
                heading = buf[:idx]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    if heading:
        claim_statuses = re.findall(r'\\\\ClaimStatus\\w+', heading)
    label = None
    for k in range(i, min(len(lines), i+40)):
        lab_match = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab_match:
            label = lab_match.group(1)
            break
    results.append((i+1, env, label, claim_statuses))
for entry in results:
    print(entry)
print('Total envs', len(results))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
(200, 'definition', 'def:chiral-twisting-datum', [])
(224, 'remark', 'rem:explicit-twisted-differential', [])
(252, 'definition', 'def:chiral-koszul-morphism', [])
(266, 'remark', 'rem:construction-vs-resolution', [])
(399, 'theorem', 'thm:fundamental-twisting-morphisms', ['\\ClaimStatusProvedHere'])
(513, 'remark', 'rem:MC-is-Stokes', [])
(536, 'remark', 'rem:theorem-A-decomposition', [])
(561, 'proposition', 'prop:bar-universal-property', ['\\ClaimStatusProvedElsewhere'])
(594, 'theorem', 'thm:chiral-comparison-lemma', [])
(625, 'definition', 'def:chiral-koszul-pair', [])
(747, 'theorem', 'thm:pbw-koszulness-criterion', ['\\ClaimStatusProvedHere'])
(819, 'remark', 'rem:classical-to-chiral-koszul', [])
(825, 'theorem', 'thm:km-chiral-koszul', ['\\ClaimStatusProvedHere'])
(880, 'theorem', 'thm:virasoro-chiral-koszul', ['\\ClaimStatusProvedHere'])
(1077, 'remark', 'rem:ce-vs-exterior', [])
(1083, 'remark', 'rem:ce-vs-chiral-bar', [])
(1112, 'theorem', 'thm:bar-concentration', ['\\ClaimStatusProvedHere'])
(1205, 'remark', 'rem:one-loop-exactness', [])
(1224, 'proposition', 'prop:ainfty-formality-implies-koszul', ['\\ClaimStatusProvedHere'])
(1257, 'theorem', 'thm:ainfty-koszul-characterization', ['\\ClaimStatusProvedHere'])

exec
/bin/zsh -lc "sed -n '4660,4740p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\mathrm{BV} = \mathrm{bar}$ identification at higher
genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
\end{conjecture}

\begin{remark}[PVA quantization bridge]
\label{rem:concordance-pva-bridge}
\index{Poisson vertex algebra!quantization bridge}%
Volume~II constructs the modular PVA quantization pipeline:
a Poisson vertex algebra $V$ (the classical shadow of a
chiral algebra) determines a stable-graph modular deformation
complex $\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(V)$,
and the genus-$1$ obstruction is the variational modular class
$\mathrm{Mod}(V) = [\Delta_{\mathrm{cyc}} P_\Pi]$.
For the $\mathcal{W}_3$ PVA, $\mathrm{Mod}(V) = 0$
(Volume~II, Theorem~N). The lift freedom is one-dimensional,
generated by the central-parameter direction: the unique
deformation that produces the quantized $\mathcal{W}_3$
at central charge $c = c(k)$. This connects Volume~II's
PVA descent (Theorem~G) with Volume~I's shadow obstruction tower
(the degree-$2$ projection $\Theta_\cA^{\leq 2}$ recovers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3900,3980p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The three hypotheses are verified as follows.
\begin{enumerate}
\item \emph{PBW basis.}
 Molev~\cite{molev-yangians} establishes a PBW basis for
 $Y(\mathfrak{g})$ in the RTT presentation for every
 simple~$\mathfrak{g}$: ordered monomials in the generators
 $\{T_{ij}^{(r)}\}$ form a vector space basis, and the associated
 graded is the polynomial algebra $\mathrm{Sym}(V)$ with
 $V = \bigoplus_{r \geq 0} \mathrm{End}(\mathbb{C}^N)_r$,
 $N = \dim V_0$ the dimension of the chosen fundamental
 representation. This gives a flat deformation from
 $Y(\mathfrak{g})$ to $\mathrm{Sym}(V)$.
\item \emph{Quadraticity.}
 The RTT relation~\eqref{eq:rtt-relation} is quadratic in the
 generators $T_{ij}^{(r)}$, so $Y(\mathfrak{g})$ is a quadratic
 algebra in the sense of Polishchuk--Positselski.
\item \emph{Local finiteness.}
 Each level component $V_r = \mathrm{span}\{T_{ij}^{(r)}\}$
 has dimension $N^2 = (\dim V_0)^2$, which is finite and
 independent of~$r$. Since the RTT relation is homogeneous of
thinking
**Inspecting routing remarks**

I need to check line 3935 for any comments about circularity in routing. The mission requires that we have remarks for circular dependencies, so it’s important to ensure everything is correctly noted. I think it might be a good idea to compare the remarks with what's actually in the file to confirm accuracy. I’ll open the file around line 3935 and look closely at what's there. Let's see what I find!
exec
/bin/zsh -lc 'rg -n "rem:non-circular-logical-chain|circularity-free|resolving the circularity|circularity problem|Stage 1|Stage 2|Stage 3|Logical independence" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3928,4425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4858,4906p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/concordance.tex:1363:\emph{Logical independence of the proved core}
chapters/connections/concordance.tex:4874:(Remark~\ref{rem:non-circular-logical-chain}).
chapters/connections/concordance.tex:4898:Remark~\ref{rem:non-circular-logical-chain}).
chapters/theory/chiral_koszul_pairs.tex:3935:\section{The three-stage construction: resolving the circularity}
chapters/theory/chiral_koszul_pairs.tex:3938:\subsection{The circularity problem}
chapters/theory/chiral_koszul_pairs.tex:3960:\subsection{\texorpdfstring{Stage 1: independent definition of $\mathcal{A}_2^!$}{Stage 1: independent definition of A-2!}}
chapters/theory/chiral_koszul_pairs.tex:4040:\subsection{Stage 2: verification of coalgebra axioms}
chapters/theory/chiral_koszul_pairs.tex:4134:\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}
chapters/theory/chiral_koszul_pairs.tex:4274:\label{cor:circularity-free-koszul}
chapters/theory/chiral_koszul_pairs.tex:4292:\noindent\emph{Stage 1: Intrinsic construction of $\mathcal{A}^!$.}
chapters/theory/chiral_koszul_pairs.tex:4312:\noindent\emph{Stage 2: Verification of coalgebra axioms.}
chapters/theory/chiral_koszul_pairs.tex:4336:\noindent\emph{Stage 3: The comparison map is a quasi-isomorphism.}
chapters/theory/chiral_koszul_pairs.tex:4399:\noindent\emph{Logical independence.} We record that the argument is circularity-free:
chapters/theory/chiral_koszul_pairs.tex:4409:When $\mathcal{A}$ is quadratic with relations $R \subset j_*j^*(\mathcal{V}^{\boxtimes 2})$, the weight filtration on $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is bounded and the spectral sequence of Stage~3d collapses at $E_2$. In this case $\mathcal{A}^!$ is the classical quadratic dual; no completion is needed, and Corollary~\ref{cor:circularity-free-koszul} reduces to the Ginzburg--Kapranov theorem for operads.
 succeeded in 50ms:
  4858	$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
  4859	(Definition~\ref{def:provisional-coderived},
  4860	Proposition~\ref{prop:coderived-adequacy})
  4861	provides a working substitute within the scope of this monograph.
  4862	On the flat finite-type locus singled out in the bar-cobar
  4863	foundations, the coderived and derived categories agree.
  4864	Bar-cobar inversion there is genus~$0$ unconditional and, at higher
  4865	genus, unconditional on the CFT-type standard landscape except
  4866	integer-spin $\beta\gamma$ by
  4867	Theorem~\ref{thm:pbw-propagation}; in general it remains
  4868	conditional on axiom~\ref{MK:modular}
  4869	\textup{(}Theorem~\ref{thm:higher-genus-inversion}\textup{)}.
  4870	
  4871	\emph{Non-circular logical chain.}
  4872	The logical foundation for bar-cobar inversion at all genera
  4873	is free of circularity
  4874	(Remark~\ref{rem:non-circular-logical-chain}).
  4875	The antecedent
  4876	hypotheses~\ref{MK:koszul}--\ref{MK:modular}
  4877	(Definition~\ref{def:modular-koszul-chiral}) are verified
 succeeded in 53ms:
  3928	$K(\mathrm{Sym}(V)) = \mathrm{Sym}(V) \otimes \bigwedge(V^*)$
  3929	to acyclicity of $K(Y(\mathfrak{g}))$, proving Koszulness.
  3930	\end{proof}
  3931	
  3932	% Hopf structure, physical interpretation, explicit computations, and quantum group
  3933	% connections for Yangians are developed in Chapter~\ref{chap:yangians}.
  3934	
  3935	\section{The three-stage construction: resolving the circularity}
  3936	\label{sec:three-stage-construction}
  3937	
  3938	\subsection{The circularity problem}
  3939	
  3940	\begin{problem}[Circularity in Koszul duality]\label{prob:circularity}
  3941	In stating "$\bar{B}^{\text{ch}}(\mathcal{A}_1) \simeq \mathcal{A}_2^!$", we face a logical gap:
  3942	\begin{enumerate}
  3943	\item We have not given an \emph{independent definition} of $\mathcal{A}_2^!$ as a chiral coalgebra
  3944	\item We have not \emph{proven} that $\mathcal{A}_2^!$ satisfies coalgebra axioms
  3945	\item We have not \emph{constructed} the quasi-isomorphism $\bar{B}^{\text{ch}}(\mathcal{A}_1) \xrightarrow{\sim} \mathcal{A}_2^!$
  3946	\end{enumerate}
  3947	
exec
/bin/zsh -lc 'rg -n "Koszul pair" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
189: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ partition
323: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ obstructions
326: The Kodaira--Spencer map is constructed for all Koszul pairs
4965:For a modular Koszul pair $(\cA, \cA^!)$, the following hold:
5901:$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
6000:of a Koszul pair is a fixed multiple of the
7706:The factorization homology of the Koszul pair $(\cA, \cA^!)$
7736:Test~3 requires the Koszul pair but is a genus-by-genus statement,
8968:encodes the Koszul pairing
exec
/bin/zsh -lc "sed -n '4930,4985p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
restriction via the injective characterization
(Theorem~\ref{thm:stratified-conservative-restriction}),
and the factorization co-contra correspondence
(Theorem~\ref{thm:fact-co-contra-general}). The provisional
coderived category embeds fully faithfully
(Proposition~\ref{prop:provisional-embedding}).

\emph{Now complete.}
The formerly conjectural off-Koszul bar-cobar inversion on
$\operatorname{Ran}(X)$ is proved
(Theorem~\ref{thm:off-koszul-ran-inversion}): the counit
$\Omega_X \barB_X(\cA) \to \cA$ is an isomorphism in
$D^{\mathrm{co}}(\mathrm{CoFact}(X))$ without Koszulness.
The proof follows the same three-step assembly as
Theorem~\ref{thm:fact-co-contra-general}: (i) on each stratum
$\operatorname{Ran}_n$, Positselski~\cite[Theorem~7.2]{Positselski11}
gives the coderived equivalence for the restricted CDG-coalgebra;
(ii)~factorization compatibility of the bar-cobar counit;
(iii)~conservative assembly via
Theorem~\ref{thm:stratified-conservative-restriction}.
exec
/bin/zsh -lc 'rg -n "chap:[''^}]*chiral" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1645: (Chapter~\ref{chap:chiral-deformation})

exec
/bin/zsh -lc "rg -n \"include\\{chapters/theory/chiral_koszul_pairs\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/S03_koszul_to_shadow.md:203:main.tex:992:\include{chapters/theory/chiral_koszul_pairs}
main.tex:1020:\include{chapters/theory/chiral_koszul_pairs}
audit_campaign_20260412_231034/T20_gerstenhaber.md:1440:992:\include{chapters/theory/chiral_koszul_pairs}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        env = m.group(1)
        entries.append({'line': i, 'env': env, 'line_num': i+1, 'line_text': line})
# sort entries by line though already in order
for idx, entry in enumerate(entries):
    i = entry['line']
    line = entry['line_text']
    rest = line[line.find('{'+entry['env']) + len(entry['env']) + 1:]
    # find heading if exists on line or subsequent lines.
    heading = None
    claim_statuses = []
    start_pos = line.find('[')
    j = i
    if start_pos "'!= -1:
        buf = line[start_pos+1:]
        while True:
            idx_close = buf.find('"']')
            if idx_close "'!= -1:
                heading = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    if heading is not None:
        claim_statuses = re.findall(r'\\\\ClaimStatus\\w+', heading)
    entry['heading'] = heading
    entry['claim_statuses'] = claim_statuses
    # determine search range for label: until next entry start or end of file
    next_start = entries[idx+1]['line'] if idx+1 < len(entries) else len(lines)
    label = None
    for k in range(i, next_start):
        lab_match = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab_match:
            label = lab_match.group(1)
            break
    entry['label'] = label
# print results
for entry in entries:
    print(entry['line_num'], entry['env'], entry['label'], entry['claim_statuses'])
print('total', len(entries))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
200 definition def:chiral-twisting-datum []
224 remark rem:explicit-twisted-differential []
252 definition def:chiral-koszul-morphism []
266 remark rem:construction-vs-resolution []
399 theorem thm:fundamental-twisting-morphisms ['\\ClaimStatusProvedHere']
513 remark rem:MC-is-Stokes []
536 remark rem:theorem-A-decomposition []
561 proposition prop:bar-universal-property ['\\ClaimStatusProvedElsewhere']
594 theorem thm:chiral-comparison-lemma []
625 definition def:chiral-koszul-pair []
747 theorem thm:pbw-koszulness-criterion ['\\ClaimStatusProvedHere']
819 remark rem:classical-to-chiral-koszul []
825 theorem thm:km-chiral-koszul ['\\ClaimStatusProvedHere']
880 theorem thm:virasoro-chiral-koszul ['\\ClaimStatusProvedHere']
1077 remark rem:ce-vs-exterior []
1083 remark rem:ce-vs-chiral-bar []
1112 theorem thm:bar-concentration ['\\ClaimStatusProvedHere']
1205 remark rem:one-loop-exactness []
1224 proposition prop:ainfty-formality-implies-koszul ['\\ClaimStatusProvedHere']
1257 theorem thm:ainfty-koszul-characterization ['\\ClaimStatusProvedHere']
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2300,2370p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
classes contradicting~(iv)). The PBW spectral sequence converges
conditionally in the sense of Boardman: the filtration is Hausdorff
and complete (the PBW filtration on a positively graded algebra is
bounded below). In characteristic zero with a split filtration (the
PBW filtration splits by conformal weight), the extension problem is
trivial: $E_\infty = E_2$ as bigraded objects, not merely as
filtered objects. Hence $E_2$-collapse, hence~(i).

\medskip
\textsc{Lagrangian criterion}
\textup{(i)}$\Leftrightarrow$\textup{(xi)}
\emph{(unconditional for the standard landscape by
Proposition~\textup{\ref{prop:lagrangian-perfectness}}; conditional
on perfectness in general)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(xi)}:
On the Koszul locus, the bar-cobar adjunction provides a free
resolution, and the complementarity splitting
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
exec
/bin/zsh -lc 'rg -n "chiral-koszul" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
330: (Theorem~\ref{thm:e1-chiral-koszul-duality}).}
2396: Chirally Koszul (Definition~\ref{def:chiral-koszul-morphism}).
7832: (Definition~\ref{def:chiral-koszul-morphism}):
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5560,5645p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{itemize}
\item Trivial $A_\infty$ (Com) $\leftrightarrow$ Maximal $A_\infty$ (Lie)
\item Non-vanishing of $m_k^{(1)}$ for $\mathcal{A}_1$ is detected by the dual operations $m_k^{(2)}$ on $\mathcal{A}_2$ via the pairing on configuration spaces
\item Massey products of $\mathcal{A}_1$ $\leftrightarrow$ Comassey products of $\mathcal{A}_2$
\end{itemize}
\end{theorem}

\begin{proof}
We prove each item.

\emph{Item~1.} For a commutative chiral algebra $\mathcal{A}_1 = \mathcal{A}_{\mathrm{Com}}$, all higher operations $m_k^{(1)} = 0$ for $k \geq 3$ (the chiral product is strictly associative). The bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{A}_1)$ then has only the binary coproduct, and its Koszul dual $\mathcal{A}_2 = \mathcal{A}_1^!$ carries the Lie operad structure with all brackets $m_k^{(2)}$ potentially non-vanishing. This is the chiral lift of the classical $\mathrm{Com}^! = \mathrm{Lie}$ duality (\cite{LV12}, Theorem~7.6.5).

\emph{Item~2.} The Verdier duality pairing on configuration spaces (Theorem~\ref{thm:verdier-config}) gives:
\[
\langle m_k^{(1)}, n_k^{(2)} \rangle = \int_{\overline{C}_k(X)} \omega_{m_k} \wedge \delta_{n_k}
\]
where $\omega_{m_k} \in \Omega^*_{\log}(\overline{C}_k(X))$ represents the $k$-ary operation of $\mathcal{A}_1$ and $\delta_{n_k} \in \mathcal{D}^*_{\mathrm{dist}}(C_k(X))$ represents the dual operation of $\mathcal{A}_2$. Non-degeneracy of the Verdier pairing (Theorem~\ref{thm:verdier-config}) ensures that $m_k^{(1)} \neq 0$ if and only if the corresponding $n_k^{(2)}$ pairs non-trivially.

\emph{Item~3.} Massey products on $\mathcal{A}_1$ are defined by the higher $A_\infty$ operations $m_k^{(1)}$ for $k \geq 3$ (the obstructions to formality). Under bar-cobar duality, these correspond to comassey products (the dual obstructions in $\mathcal{A}_2$) by the general principle that the bar construction converts algebra operations to coalgebra cooperations (\cite{LV12}, \S10.3). The Verdier pairing identifies $m_k^{(1)}$ with the dual of $m_k^{(2)}$ at the level of configuration space integrals, so vanishing of Massey products on one side is equivalent to triviality of comassey products on the other.
\end{proof}
exec
/bin/zsh -lc "sed -n '300,360p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 all-genera scalar formula
 $\Theta^{\min} = \kappa\cdot\eta\otimes\Lambda$
 and hence $\mathrm{obs}_g = \kappa\cdot\lambda_g$
 \emph{fails} for multi-weight families: the full genus-$g$
 free energy receives a cross-channel correction
 $\delta F_g^{\mathrm{cross}}$
 (Theorem~\ref{thm:multi-weight-genus-expansion},
 Open Problem~\ref{op:multi-generator-universality} resolved
 negatively).
 Here $\kappa$ is an algebra-dependent constant and $\lambda_g$
 is the Faber--Pandharipande tautological class
 on~$\overline{\mathcal{M}}_g$.
 The genus-independent coefficient $\kappa(\cA)$ is determined
 by the genus-$1$ curvature. This is the \emph{scalar} genus
 universality (Level~$0$ of Remark~\ref{rem:four-levels}): the
 first Chern class of the factorization homology bundle.
 The full genus-$g$ invariant, the cohomology
 $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
 $\mathcal{M}_g$, is categorically richer
 (Theorem~\ref{thm:chain-modular-functor}).
thinking
**Searching labels and statuses**

I need to search all references and labels in the chapter. It might be easiest to compare the references to the actual claims. I could write a script to list labels in the chapter alongside reference hits, ensuring I gather actual statuses. Using tools like `rg`, I can find label occurrences and get line numbers for mentions. 

Creating a list of chapter labels and their statuses will help identify explicit mismatches and focus on the labels both files share. A table with contexts could be useful, including line numbers for problems and fixes.
thinking
**Identifying potential mismatches**

I might discover some existing mismatches in the statuses that I need to check exhaustively. For example, there's one point from the concordance, specifically line 3197, that states, "Status: ten equivalences proved unconditionally." Yet, the chapter introduction (lines 61-73) only mentions "Nine are unconditional equivalences." This feels like a clear discrepancy I need to address. I'll carefully analyze both references to clarify these inconsistencies before proceeding.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append(i)
entries2 = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries2.append((i,line))
results=[]
for idx,(i,line) in enumerate(entries2):
    next_start=entries2[idx+1][0] if idx+1<len(entries2) else len(lines)
    label=None
    for k in range(i, next_start):
        lab_match=re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab_match:
            label=lab_match.group(1)
            break
    if label:
        results.append(label)
print(len(results))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
103
codex
I’ve confirmed one hard seam failure already: concordance promotes the Hochschild item to an unconditional equivalence, while the chapter keeps it as a consequence only. I’m now scanning for the other seam-level status drifts, especially places where concordance compresses a conditional or routed statement into a stronger one.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2115,2215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "conj:lagrangian-koszulness|lagrangian-koszulness|cor:lagrangian-unconditional|rem:d-module-purity-content|thm:fm-boundary-acyclicity|thm:barr-beck-lurie-koszulness|thm:fh-concentration-koszulness|thm:main-koszul-hoch|thm:bar-cobar-inversion-qi" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2215,2315p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:394: operator~$S$ (Theorem~\ref{thm:main-koszul-hoch},
chapters/connections/concordance.tex:2414: (Theorem~\ref{thm:bar-cobar-inversion-qi}).
chapters/connections/concordance.tex:2418: (Theorem~\ref{thm:barr-beck-lurie-koszulness}).
chapters/connections/concordance.tex:2423: (Theorem~\ref{thm:fh-concentration-koszulness}).
chapters/connections/concordance.tex:2428: (Theorem~\ref{thm:main-koszul-hoch}).
chapters/connections/concordance.tex:2441: (Theorem~\ref{thm:fm-boundary-acyclicity}).
chapters/connections/concordance.tex:2452: (Theorem~\ref{conj:lagrangian-koszulness}).
chapters/connections/concordance.tex:2455: Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
chapters/connections/concordance.tex:3135: & \texttt{thm:bar-cobar-inversion-qi}
chapters/connections/concordance.tex:3138: & \texttt{thm:main-koszul-hoch}
chapters/connections/concordance.tex:4718: & Koszul functoriality via Connes~$S$ & & Thm~\ref{thm:main-koszul-hoch} \\
chapters/theory/chiral_koszul_pairs.tex:50:(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
chapters/theory/chiral_koszul_pairs.tex:272:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
chapters/theory/chiral_koszul_pairs.tex:2027:(Remark~\ref{rem:d-module-purity-content}); the converse is open.
chapters/theory/chiral_koszul_pairs.tex:2047: \textup{(}Theorem~\textup{\ref{thm:bar-cobar-inversion-qi})}.
chapters/theory/chiral_koszul_pairs.tex:2071: Theorem~\textup{\ref{thm:main-koszul-hoch})}.
chapters/theory/chiral_koszul_pairs.tex:2102:bar-cobar inversion (Theorem~\ref{thm:bar-cobar-inversion-qi}).
chapters/theory/chiral_koszul_pairs.tex:2121:Theorem~\ref{thm:main-koszul-hoch} then give the stated
chapters/theory/chiral_koszul_pairs.tex:2345:modules; see Remark~\textup{\ref{rem:d-module-purity-content}}).
chapters/theory/chiral_koszul_pairs.tex:2348:(Remark~\ref{rem:d-module-purity-content}).
 succeeded in 52ms:
  2115	
  2116	\smallskip\noindent
  2117	The quasi-isomorphism
  2118	$\Omega(\barBgeom(\cA)) \xrightarrow{\sim} \cA$ identifies the
  2119	bar-cobar resolution with the chiral Hochschild complex. On the
  2120	Koszul locus, Theorem~H and
  2121	Theorem~\ref{thm:main-koszul-hoch} then give the stated
  2122	cohomological concentration and duality. No converse from
  2123	\textup{(viii)} to the bar-cobar counit is proved here.
  2124	
  2125	\medskip
  2126	\textsc{$A_\infty$ formality}
  2127	\textup{(i)}$\Leftrightarrow$\textup{(iii)}:
  2128	
  2129	\smallskip\noindent
  2130	\textup{(ii)}$\Rightarrow$\textup{(iii)}:
  2131	$E_2$-collapse means all PBW differentials $d_r = 0$ for $r \geq 2$.
  2132	The $A_\infty$ products $m_n$ are identified with $d_{n-1}$ under
  2133	the HPL transfer, so $m_n = 0$ for $n \geq 3$
  2134	(Proposition~\ref{prop:ainfty-formality-implies-koszul}).
 succeeded in 53ms:
  2215	At the deepest stratum $S = D_{\{1,2\}} \cong X \times
  2216	\overline{\operatorname{Conf}}_{n-1}(X)$ (binary collision), the
  2217	restriction $i_S^!\,\barB_n(\cA)$ computes the bar-complex
  2218	contribution from the OPE $a_{(k)}b$ at a single collision point.
  2219	Acyclicity of $i_S^!$ at all strata forces the residues at every
  2220	collision to be exact, which is the PBW condition:
  2221	$d_1(e_i) = 0$ on the associated graded, hence $E_2$-collapse.
  2222	
  2223	\medskip
  2224	\textsc{Barr--Beck--Lurie monadicity}
  2225	\textup{(i)}$\Leftrightarrow$\textup{(vi)}:
  2226	
  2227	\smallskip\noindent
  2228	The Barr--Beck--Lurie theorem (\cite[Theorem~4.7.3.5]{HA}) states
  2229	that the comparison functor $\Phi$ is an equivalence if and only if
  2230	$\barB_\kappa$ is conservative and preserves totalizations of
  2231	$\barB_\kappa$-split cosimplicial objects.
  2232	Conservativity: $\barB_\kappa$ detects quasi-isomorphisms on the
  2233	Koszul locus by bar-cobar inversion~(v).
  2234	Totalization preservation: on the Koszul locus, the bar-cobar
exec
/bin/zsh -lc 'rg -n "circular" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
4871:\emph{Non-circular logical chain.}
4873:is free of circularity
4874:(Remark~\ref{rem:non-circular-logical-chain}).
4898:Remark~\ref{rem:non-circular-logical-chain}).

thinking
**Summarizing labeled environments and remarks**

I’m preparing to list all 103 labeled environments with their types and claim statuses, carefully including any ClaimStatus macros for each entry. Then, I’ll look for remarks explicitly about deferring proofs or routing circular dependencies by searching relevant keywords and checking line numbers to capture any such special notes.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "circular" -n chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3935:\section{The three-stage construction: resolving the circularity}
3938:\subsection{The circularity problem}
3940:\begin{problem}[Circularity in Koszul duality]\label{prob:circularity}
4274:\label{cor:circularity-free-koszul}
4399:\noindent\emph{Logical independence.} We record that the argument is circularity-free:
4409:When $\mathcal{A}$ is quadratic with relations $R \subset j_*j^*(\mathcal{V}^{\boxtimes 2})$, the weight filtration on $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is bounded and the spectral sequence of Stage~3d collapses at $E_2$. In this case $\mathcal{A}^!$ is the classical quadratic dual; no completion is needed, and Corollary~\ref{cor:circularity-free-koszul} reduces to the Ginzburg--Kapranov theorem for operads.
exec
/bin/zsh -lc "sed -n '4850,4905p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar-cobar foundations.

Curved bar objects can lose ordinary cohomological visibility while
their coderived/contraderived invariants remain nontrivial. The
coderived framework is built to retain that information without
promoting the monodromy metaphor itself into a theorem.

The provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
(Definition~\ref{def:provisional-coderived},
Proposition~\ref{prop:coderived-adequacy})
provides a working substitute within the scope of this monograph.
On the flat finite-type locus singled out in the bar-cobar
foundations, the coderived and derived categories agree.
Bar-cobar inversion there is genus~$0$ unconditional and, at higher
genus, unconditional on the CFT-type standard landscape except
integer-spin $\beta\gamma$ by
Theorem~\ref{thm:pbw-propagation}; in general it remains
conditional on axiom~\ref{MK:modular}
\textup{(}Theorem~\ref{thm:higher-genus-inversion}\textup{)}.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4370,4435p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\]
Since $\Phi$ is defined by integration, this is exactly the same
boundary contribution that defines the residue part of $d_!$.
\end{itemize}

The precise cancellation follows from Stokes' theorem on manifolds with corners applied to $\overline{C}_{n+1}(X)$ (Theorem~\ref{thm:stokes-config}).

\emph{Step 3c: $\Phi$ preserves the coalgebra structure.} The coproduct on $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is the boundary restriction map $\Delta_{\bar{B}}(\alpha) = \mathrm{Res}_{\partial}\alpha$, splitting a configuration of $(k+1)$ points into two sub-configurations. Under the pairing \eqref{eq:comparison-map}, this corresponds to the factorisation of integration over $\overline{C}_{k+1}(X)$ into integrations over strata $\overline{C}_{|I|+1}(X) \times \overline{C}_{|J|+1}(X)$ for $I \sqcup J = \{1,\ldots,k+1\}$. But this factorised integration is precisely how the deconcatenation coproduct on $T^c_{\mathrm{chiral}}(\mathcal{V}^{\vee})$ acts. Hence $(\Phi \boxtimes \Phi) \circ \Delta_{\bar{B}} = \bar\Delta \circ \Phi$.

\emph{Step 3d: Quasi-isomorphism via filtration and spectral sequence.} Equip both sides with the \emph{weight filtration} by cogenerator count:
\begin{align*}
F_p \bar{B}^{\mathrm{ch}}(\mathcal{A}) &= \bigoplus_{n \leq p} \bar{B}^n(\mathcal{A}), \\
F_p \mathcal{A}^! &= \bigoplus_{n \leq p} (T^c_{\mathrm{chiral}}(\mathcal{V}^{\vee}))^{(n)}.
\end{align*}
These are exhaustive, bounded-below filtrations preserved by $\Phi$, $d_{\mathrm{bar}}$, and $d_!$. The associated spectral sequences have
\[E_1^{p,q}(\bar{B}) = H^{p+q}\!\left(\overline{C}_{p+1}(X),\; \mathcal{A}^{\boxtimes(p+1)} \otimes \Omega^p_{\log}\right), \qquad E_1^{p,q}(\mathcal{A}^!) = H^{p+q}((\mathcal{V}^{\vee})^{\boxtimes(p+1)}, d_!^{(1)})\]
where $d_!^{(1)}$ is the linear (weight-preserving) part of $d_!$, which encodes only the simple-pole OPE data.

On the $E_1$ page, $\Phi$ reduces to the classical Verdier duality isomorphism between logarithmic cohomology and distributional cohomology on $\overline{C}_{p+1}(X)$ (Theorem~\ref{thm:verdier-config}). For each fixed $p$, this is an isomorphism:
\[\Phi_1^{p,*} \colon E_1^{p,*}(\bar{B}) \xrightarrow{\;\cong\;} E_1^{p,*}(\mathcal{A}^!).\]
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '250,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
   250	shadow depth $r_{\max}$ and the four-class partition
   251	G/L/C/M measure $L_\infty$ non-formality, not
   252	Koszulness status:
   253	class~G (formal, $r_{\max} = 2$),
   254	class~L (single Massey product, $r_{\max} = 3$),
   255	class~C (quartic then rigid by stratum separation, $r_{\max} = 4$),
   256	class~M (intrinsically non-formal, $r_{\max} = \infty$).
   257	
   258	\section{Principal contributions}\label{sec:principal-contributions}
   259	
   260	\begin{enumerate}[label=\emph{(\arabic*)}]
   261	
   262	\item \emph{Configuration space bar-cobar adjunction
   263	 (Theorems~\ref{thm:bar-cobar-isomorphism-main}
   264	 and~\ref{thm:higher-genus-inversion}).}
   265	 Bar and cobar are realized via explicit integrals over
   266	 Fulton--MacPherson compactifications $\overline{C}_n(X)$:
   267	 bar differential by residues at collision divisors, cobar
   268	 differential by inclusions of strata. The adjunction holds
   269	 for all Koszul chiral algebras at all genera. Inversion is
thinking
**Considering proof requirements**

I think I need to focus on the D-module purity remark and the rest of the proof. There’s definitely something important about making sure the arguments are clear and correctly structured. I wonder if I should outline the proof step-by-step to ensure nothing gets missed. Okay, that sounds like a good plan! I’ll make a note to emphasize the critical points in the proof too. This will help in understanding the overall argument better.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2315,2375p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:operadic-complexity\\}|thm:operadic-complexity["'^-]|operadic complexity" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2588,2635p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "defer" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2315	\smallskip\noindent
  2316	\textup{(i)}$\Rightarrow$\textup{(xi)}:
  2317	On the Koszul locus, the bar-cobar adjunction provides a free
  2318	resolution, and the complementarity splitting
  2319	$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
  2320	\simeq H^*(\overline{\cM}_g, \cZ_\cA)$
  2321	(Theorem~C) identifies $\cM_\cA$ and $\cM_{\cA^!}$ as
  2322	complementary subspaces of $\cM_{\mathrm{comp}}$. The
  2323	shifted-symplectic structure
  2324	(Theorem~\ref{thm:ambient-complementarity-fmp})
  2325	makes these subspaces isotropic; the complementarity splitting
  2326	gives maximal dimension, hence Lagrangian.
  2327	
  2328	\smallskip\noindent
  2329	\textup{(xi)}$\Rightarrow$\textup{(i)}:
  2330	If $\cM_\cA$ and $\cM_{\cA^!}$ are transverse Lagrangians,
  2331	their derived intersection
  2332	$\cM_\cA \times^h_{\cM_{\mathrm{comp}}} \cM_{\cA^!}$
  2333	is discrete (transverse Lagrangian intersection in a $(-1)$-shifted
  2334	symplectic space has expected dimension~$0$). This derived
 succeeded in 53ms:
chapters/connections/concordance.tex:2513:\index{operadic complexity|textbf}
chapters/connections/concordance.tex:2514:\index{shadow obstruction tower!operadic complexity}
chapters/connections/concordance.tex:2519:\index{operadic complexity|textbf}
chapters/connections/concordance.tex:3159: & \texttt{thm:operadic-complexity}
chapters/connections/concordance.tex:7033:\ref{thm:operadic-complexity}
chapters/connections/concordance.tex:7035: \textup{(}operadic complexity identification\textup{)}
 succeeded in 51ms:
  2588	
  2589	For the converse, suppose~$\cA$ is SC-formal.
  2590	Because the standard landscape is exhausted by the four classes
  2591	$G$, $L$, $C$, $M$, it is enough to eliminate the three
  2592	non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
  2593	does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
  2594	class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
  2595	nonzero higher operations in every arity $k \geq 3$. Each of
  2596	these contradicts SC-formality. Hence an SC-formal algebra must
  2597	belong to class~$G$.
  2598	\end{proof}
  2599	
  2600	\begin{remark}[D-module purity: reduction to a single gap]
  2601	\label{rem:d-module-purity-content}
  2602	\index{D-module purity!reduction to Saito weight}
  2603	\index{Saito weight filtration!and PBW filtration}
  2604	The converse direction of condition~\textup{(xii)} (Koszulness
  2605	$\Longrightarrow$ D-module purity of~$\barBgeom_n(\cA)$) admits
  2606	a five-step proof strategy. Steps~1--3 are established; step~4
  2607	is the single remaining gap.
 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '360,420p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 and its cohomology recovers the formal-disc oper
 differential-form package:
 $H^n(\barB(\widehat{\fg}_{-h^\vee}))
 \cong \Omega^n(\mathrm{Op}_{\fg^\vee}(D))$.
 The $H^0$ identification gives the Feigin--Frenkel
 center~\cite{Feigin-Frenkel}; the $H^1$ identification
 gives K\"ahler differentials of the oper space; and the
 full cohomological identification follows from the bar-Ext
 identification combined with the
 Frenkel--Teleman theorem~\cite{FT06}.
 This gives a vertex-algebraic chain model interfacing with the
 oper side of the geometric Langlands programme.

\item \emph{Chiral Hochschild cohomology
 (Theorems~\ref{thm:w-algebra-hochschild},
 \ref{thm:virasoro-hochschild},
 \ref{thm:critical-level-cohomology};
 Proposition~\ref{prop:chirhoch1-affine-km}).}
 For the principal $\Walg$-algebra $\Walg^k(\fg)$ at generic level:
 $\ChirHoch^n(\Walg^k(\fg)) = 0$ for $n > 2$, with Hilbert polynomial
exec
/bin/zsh -lc "sed -n '420,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$. The pair
 $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ is terminal in the
 category of local chiral Swiss-cheese pairs over~$\cA$: for every
 such pair $(B, \cA, \mu)$, there exists a unique morphism
 $\Phi \colon B \to C^\bullet_{\mathrm{ch}}(\cA,\cA)$
 intertwining the brace structures and the mixed operations.
 Two independent proofs: (i)~operadic, via the recognition theorem
 and homotopy-Koszulity of~$\mathsf{SC}^{\mathrm{ch,top}}$
 (\S\ref{sec:operadic-center-theorem}); (ii)~direct, via the
 explicit brace morphism with Koszul signs
 (\S\ref{sec:chiral-center-theorem}).

\end{enumerate}

\begin{remark}[Geometric Langlands connection]%
\label{rem:oper-langlands-concordance}
\index{geometric Langlands!oper from bar complex}%
\index{oper!concordance summary}%
The bar complex
$\barB(\widehat{\fg}_{-h^\vee})$ at critical level is a

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3990,4055p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The \emph{coproduct} $\Delta: \mathcal{A}_2^! \to \mathcal{A}_2^! \boxtimes \mathcal{A}_2^!$ is the universal coproduct from the cofree construction. For generators $\phi_i^* \in \mathcal{V}^{\vee}$, the full coproduct is:
\[\Delta(\phi_i^*) = \phi_i^* \boxtimes 1 + 1 \boxtimes \phi_i^*\]
(generators are primitive; the \emph{reduced} coproduct $\bar{\Delta}(\phi_i^*) = 0$).

For higher tensor products $\phi_{i_1}^* \boxtimes \cdots \boxtimes \phi_{i_k}^*$:
\[\bar{\Delta}(\phi_{i_1}^* \boxtimes \cdots \boxtimes \phi_{i_k}^*) = \sum_{\substack{I \sqcup J = \{1,\ldots,k\} \\ I, J \neq \emptyset}} \pm \left(\bigboxtimes_{i \in I} \phi_i^*\right) \boxtimes \left(\bigboxtimes_{j \in J} \phi_j^*\right)\]
with Koszul signs $\pm = (-1)^{\sum_{i \in I, j \in J, i > j} |\phi_i^*| \cdot |\phi_j^*|}$.

\medskip
\noindent\emph{Step 3 (Coderivation/Differential):}

The \emph{differential} $d_!: \mathcal{A}_2^! \to \mathcal{A}_2^![1]$ is the unique coderivation determined by its values on generators. For $\phi_i^* \in \mathcal{V}^{\vee}$:
\[d_!(\phi_i^*) = -\sum_{\substack{j,k,m \\ m \geq 1}} \frac{C_{ij}^{k,m}}{(m-1)!} \cdot \phi_j^* \boxtimes \phi_k^* \boxtimes \omega_X^{\otimes (m-1)}\]

More precisely: the differential encodes the \emph{residue structure} of OPEs in $\mathcal{A}_2$. If $\phi_i(z)\phi_j(w)$ has a pole of order $m$ with residue $C_{ij}^{k,m}\phi_k$, then:
\[d_!(\phi_i^*) \text{ contains the term } -C_{ij}^{k,m} \cdot (\phi_j^* \boxtimes \phi_k^*) \otimes \eta^{\otimes(m-1)}\]
where $\eta = d\log(z_1 - z_2) = \frac{dz_1 - dz_2}{z_1 - z_2}$ is the standard logarithmic form.

\medskip
thinking
**Investigating theorem labels**

I’m noticing that there seems to be a discrepancy with the concordance cross-reference table. It uses the label `thm:operadic-complexity`, but the actual theorem is labeled `thm:operadic-complexity-concordance`. This might mean I need to look through the chapter to see if it has a label, `thm:operadic-complexity`, as well. Let's explore that further to ensure everything is aligned correctly!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '500,560p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The first bijection sends $\tau \in \mathrm{Tw}(\cC, \cA)$
to the algebra morphism $g_\tau\colon \Omega_X(\cC) \to \cA$
defined on cogenerators by $g_\tau(s^{-1} c) = \tau(c)$; the
MC equation for $\tau$ is equivalent to $g_\tau$ commuting
with differentials
(the same proof as \cite[Theorem~2.2.7]{LV12}).
The second bijection sends $\tau$ to the coalgebra morphism
$f_\tau\colon \cC \to \bar{B}_X(\cA)$ defined dually.
The universal property of the bar construction as a cofree
coalgebra ensures uniqueness of factorization.
\end{proof}

\begin{remark}[Why the MC equation is Stokes' theorem]
\label{rem:MC-is-Stokes}
\index{Maurer--Cartan equation!geometric origin}
The Maurer--Cartan equation $d\tau + \tau \star \tau = 0$ is
not an imposed axiom. It is forced by the geometry of
$\overline{C}_2(X)$. The convolution
$(\tau \star \tau)(x) = \mu \circ (\tau \otimes \tau)
codex
I’ve found a second seam problem: concordance’s own status summary is internally stronger than both the chapter intro and the chapter meta-theorem. I’m now checking for label-surface drift and whether concordance’s routing language actually points to the circularity-resolution material that exists in the chapter.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:operadic-complexity\\}|\\\\ref\\{thm:operadic-complexity\\}|\\\\label\\{thm:operadic-complexity-concordance\\}' chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Status: ten equivalences|Unconditional equivalences \\(i\\)--\\(x\\)|No converse from \\(viii\\)|Condition~\\\\textup\\{\\(viii\\)\\} is a proved consequence|Nine are unconditional equivalences|9 \\+ 1 \\+ 1 \\+ 1\" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3205,3225p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/theorem_registry.md:2931:| `thm:thqg-intro-operadic-complexity` | `theorem` | 860 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |
chapters/connections/concordance.tex:2518:\label{thm:operadic-complexity-concordance}%
chapters/connections/concordance.tex:7033:\ref{thm:operadic-complexity}
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:73:$9 + 1 + 1 + 1$.
 succeeded in 51ms:
  3205	Two further characterizations, tropical Koszulness
  3206	(Theorem~\ref{thm:tropical-koszulness}) and
  3207	bifunctor obstruction decomposition
  3208	(Theorem~\ref{thm:bifunctor-obstruction-decomposition}),
  3209	are proved separately but are not among the twelve numbered
  3210	conditions.
  3211	
  3212	\smallskip\noindent
  3213	\emph{Proof circuit.}
  3214	The core cycle
  3215	(\ref{item:kp-def})$\Leftrightarrow$(\ref{item:kp-pbw})$\Leftrightarrow$(\ref{item:kp-ainfty})$\Leftrightarrow$(\ref{item:kp-barcobar})$\Leftrightarrow$(\ref{item:kp-hochschild})
  3216	is proved by PBW concentration~$\to$
  3217	bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
  3218	Koszul-complex acyclicity, with $A_\infty$ formality equivalent
  3219	to PBW via Keller classicality. From this core,
  3220	Ext diagonal vanishing~(\ref{item:kp-ext}) follows by bigrading
  3221	constraints,
  3222	Barr--Beck--Lurie~(\ref{item:kp-barrbeck}) by conservativity +
  3223	monadic descent (\cite[Prop.~4.7.3.16]{HA}),
  3224	FH concentration~(\ref{item:kp-facthom}) via bar = FH,
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4660,4755p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
  4660	$\mathrm{BV} = \mathrm{bar}$ identification at higher
  4661	genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
  4662	\end{conjecture}
  4663	
  4664	\begin{remark}[PVA quantization bridge]
  4665	\label{rem:concordance-pva-bridge}
  4666	\index{Poisson vertex algebra!quantization bridge}%
  4667	Volume~II constructs the modular PVA quantization pipeline:
  4668	a Poisson vertex algebra $V$ (the classical shadow of a
  4669	chiral algebra) determines a stable-graph modular deformation
  4670	complex $\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(V)$,
  4671	and the genus-$1$ obstruction is the variational modular class
  4672	$\mathrm{Mod}(V) = [\Delta_{\mathrm{cyc}} P_\Pi]$.
  4673	For the $\mathcal{W}_3$ PVA, $\mathrm{Mod}(V) = 0$
  4674	(Volume~II, Theorem~N). The lift freedom is one-dimensional,
  4675	generated by the central-parameter direction: the unique
  4676	deformation that produces the quantized $\mathcal{W}_3$
  4677	at central charge $c = c(k)$. This connects Volume~II's
  4678	PVA descent (Theorem~G) with Volume~I's shadow obstruction tower
  4679	(the degree-$2$ projection $\Theta_\cA^{\leq 2}$ recovers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3700,3780p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
part~(1) yields
\[
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
\simeq \Omega_X(\cC_2) \simeq \cA_2,
\]
and similarly for the other index. This is the Verdier
identification at the factorization-algebra level.
Part~(3) is the same statement after naming $\cA_2$ as the Koszul
dual~$\cA_1^!$.
The relative/family statement follows from proper base change
(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
so the fiberwise quasi-isomorphisms lift to the family by
Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
duality commutes with proper base change by
Theorem~\ref{thm:verdier-bar-cobar}.
\end{proof}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-a-lagrangian}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4220,4330p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\emph{Solution.} Take the \emph{I-adic completion}:
\[\widehat{\bar{B}^{\text{ch}}(\mathcal{A}_1)} := \varprojlim_n \bar{B}^{\text{ch}}(\mathcal{A}_1)/I^n\]
where $I = \ker(\epsilon)$ is the augmentation ideal.

\begin{lemma}[Completion convergence; \ClaimStatusProvedHere]\label{lem:completion-convergence}
For chiral algebras satisfying:
\begin{itemize}
\item Finite generation over $\mathcal{D}_X$
\item Polynomial growth of structure constants
\item Formal smoothness: $\dim H^*(\mathcal{A}, \mathcal{A}) < \infty$
\end{itemize}

The completion converges and:
\[\widehat{\bar{B}^{\text{ch}}(\mathcal{A}_1)} \simeq \mathcal{A}_2^!\]
as chiral coalgebras.
\end{lemma}

\begin{proof}[Proof of Lemma]
The \emph{conilpotent filtration} on $\bar{B}^{\text{ch}}(\mathcal{A}_1)$ is:
thinking
**Investigating mismatches**

I noticed that line 3215 mentions that the core cycle includes the item kp-hochschild, but there’s a contradiction in the chapter, which states there's no converse from (viii). This seems like a significant mismatch. I think it’s essential to dig deeper into the following lines, like 3225, to find any additional inconsistencies or details that could clarify this issue. Let’s see what I can uncover!
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3225,3240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"core cycle|No converse from \\(viii\\)|\\(viii\\).*consequence|Condition~\\\\textup\\{\\(viii\\)\\}|item:kp-hochschild\\)|kp-hochschild\" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3225	Kac--Shapovalov~(\ref{item:kp-nullvec}) via Shapovalov
  3226	non-degeneracy, FM boundary acyclicity~(\ref{item:kp-fmbdy})
  3227	by stratum-by-stratum PBW, and
  3228	the Lagrangian criterion~(\ref{item:kp-lagrangian}) via PTVV
  3229	derived-intersection theory (unconditional for the standard
  3230	landscape by Proposition~\ref{prop:lagrangian-perfectness}).
  3231	
  3232	
  3233	%% ====================================================================
  3234	%% RECTIFICATION: THE ORGANIZING META-THEOREM
  3235	%% ====================================================================
  3236	\section{Rectification: the organizing meta-theorem}
  3237	\label{sec:concordance-rectification}
  3238	\index{rectification!organizing meta-theorem|textbf}
  3239	\index{formality!as universal mechanism|textbf}
  3240	
 succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:2022:equivalent. Condition~\textup{(viii)} is a proved consequence of
chapters/connections/concordance.tex:2426:\item\label{item:kp-hochschild}
chapters/connections/concordance.tex:3214:The core cycle
chapters/connections/concordance.tex:3215:(\ref{item:kp-def})$\Leftrightarrow$(\ref{item:kp-pbw})$\Leftrightarrow$(\ref{item:kp-ainfty})$\Leftrightarrow$(\ref{item:kp-barcobar})$\Leftrightarrow$(\ref{item:kp-hochschild})
collab wait(call_Qx8Beopk9AC5I8jfGagsLDIH)
  receivers: 019d83d5-28e1-7950-8f9f-fd133569550d, 019d83d5-28b9-7f22-a041-02c2257be59e
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "deffer" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 63ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5065,5125p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\[
\mathcal{A} \;\xrightarrow{\;\sim\;}\;
(\mathcal{A}^!)^!
\]
is a quasi-isomorphism. This is the $\Eone$-chiral manifestation
of the classical self-duality $\operatorname{Ass}^! \cong
\operatorname{Ass} \otimes \operatorname{sgn}$.
\end{corollary}

\begin{proof}
The double-dual map factors as
$\mathcal{A} \xrightarrow{\sim}
\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))
= \Omega^{\mathrm{ch}}(\mathcal{A}^!)
\xrightarrow{\sim} (\mathcal{A}^!)^!$,
where the first map is the counit quasi-isomorphism
\eqref{eq:e1-counit} and the second identifies the cobar of
$\mathcal{A}^!$ with the Koszul dual algebra of $\mathcal{A}^!$
(by the Koszulity of $\chirAss$).
\end{proof}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "defers" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Summarizing chapter description blocks with labels and remarks**

I'm sorting out the relevant sections that describe the chapter in question. There are distinct line ranges: the modular homotopy table block (lines 4685-4752 in chapters/connections/concordance.tex) containing labels A_mod, B_mod, C_mod, Index, DK, H with explicit status texts at lines like 4706-4718; plus the "Non-circular logical chain" remark at lines 4850-4874 which discusses circular-dependency concerns. I'll provide these line number references, label statuses as quoted, and briefly paraphrase the routing/circular dependency remark exactly as stated. This keeps me aligned with the user’s request without inferring beyond the source.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5130,5175p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
asserting $D^b\mathrm{Coh}(X) \simeq D^\pi\mathcal{F}(X^\vee)$,
is, in the language of the present work, the statement that the bar-cobar
adjunction of Theorem~\ref{thm:bar-cobar-isomorphism-main} restricts
to an equivalence between the algebraic (coherent sheaf) and
symplectic (Fukaya) models of the same derived
category~\cite{SeidelBook}.
The four objects remain distinct:
\(B^{\mathrm{ord}}(\mathcal A)\) is the bar coalgebra (Floer
cochains with deconcatenation coproduct), $\mathcal{A}^!$ is its
Koszul dual algebra (wrapped endomorphisms), and the derived
center~$Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A})$ is the
Hochschild cochain complex (closed-string sector), not any Fukaya
object.
\end{remark}

% ================================================================
% SECTION 8.5: CATEGORIES OF MODULES AND DERIVED EQUIVALENCES
% ================================================================

\section{Categories of modules and derived equivalences}
codex
**Modular-homotopy summary (covers `chapters/theory/chiral_koszul_pairs.tex`)**  
- Range: `chapters/connections/concordance.tex:4685-4752` (section “Towards modular homotopy theory”, including the six-component table and the “four levels” remark).  
- Labels/statuses (quoted text + line refs):  
  - `A_{\mathrm{mod}}`: “Bar-cobar intertwined with Verdier, functorial over \overline{\mathcal{M}}_{g,n}” with status **Proved** (line 4706).  
  - `B_{\mathrm{mod}}`: “Inversion on Koszul locus; persistence off it” with status “Proved on Koszul locus; coderived persistence conjectural” (lines 4708‑4709).  
  - `C_{\mathrm{mod}}`: “Shifted symplectic complementarity (PTVV Lagrangian embedding)” with status **Proved** (line 4710).  
  - `Index`: “GRR: scalar genus series …; genus-1 unconditional” with status **Proved** (line 4712).  
  - `DK`: “DK-0/1/1\frac12 …; DK-2/3 …; DK-4/5 …” with statuses (“proved” or “DK-5: proved for \mathfrak{sl}_2”, “DK-4: ML proved, alg. id. open”, “general: conj.”) exactly as printed (lines 4713‑4715).  
  - `H`: “Chiral Hochschild …; Koszul functoriality via Connes S” with status **Proved** (generic level) and “critical level: ProvedElsewhere” (lines 4716‑4718).  
- Routing / circular-dependency remark (immediately following this block in the same section):  
  - `chapters/connections/concordance.tex:4851-4874` (“Non-circular logical chain.”) states that the antecedent hypotheses MK:koszul–MK:modular are verified independently (via Theorem~\ref{thm:fundamental-twisting-morphisms}, Theorem~\ref{thm:verdier-bar-cobar}, Theorems~\ref{thm:pbw-allgenera-km}–\ref{thm:pbw-allgenera-principal-w}) and that Theorem~\ref{thm:higher-genus-inversion} then inductively proves inversion without invoking the genus under consideration.
wait(call_Qx8Beopk9AC5I8jfGagsLDIH) 1 agents complete:
  019d83d5-28e1-7950-8f9f-fd133569550d completed: "**Modular-homotopy summary (covers `chapters/theory/chiral_koszul_pairs.tex`)**  
- Range: `chapters/connections/concord…"
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "deferred" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Considering agent actions**

Oops, it looks like the agent didn't inspect the requested file? Maybe it misfired. I might need to ignore that for now. It's possible that the second agent could inspect the file instead. But wait—only one agent returned, likely due to whichever process finished first. I need to pause and think whether to wait again or ask for assistance. There’s a lot here to untangle!
codex
One scan finished on the wrong seam block, so I’m discarding that and pulling the chapter-specific extraction directly. The remaining pass is focused on the live labels/statuses and the explicit circularity-resolution material inside `chiral_koszul_pairs.tex` only.
collab wait(call_YbmkdnCZiuZrJTXu0fP4rtDk)
  receivers: 019d83d5-28b9-7f22-a041-02c2257be59e
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append({'line': i, 'env': m.group(1), 'line_num': i+1, 'line': line})
for idx, entry in enumerate(entries):
    i = entry['line']
    next_i = entries[idx+1]['line'] if idx+1 < len(entries) else len(lines)
    label = None
    for k in range(i, next_i):
        lab = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab:
            label = lab.group(1)
            break
    entry['label'] = label
    heading = None
    start = entry['line'].find('[')
    heading_text = None
    if start "'!= -1:
        buf = entry['"'line'][start+1:]
        j = i
        while True:
            idx_close = buf.find(']')
            if idx_close "'!= -1:
                heading_text = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    entry['claim_statuses'] = []
    if heading_text:
        entry['claim_statuses'] = re.findall(r'\\\\ClaimStatus\\w+', heading_text)
# filter entries with label
from collections import defaultdict
env_map = defaultdict(list)
for entry in entries:
    if entry['label']:
        env_map[entry['env']].append((entry['label'], entry['claim_statuses'], entry['line_num']))
for env in env_map:
    env_map[env].sort(key=lambda x: x[2])
for env in ['theorem','proposition','conjecture','remark','definition']:
    data = env_map.get(env, [])
    print(env, len(data))
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
Traceback (most recent call last):
  File "<stdin>", line 14, in <module>
TypeError: 'str' object cannot be interpreted as an integer
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
from collections import defaultdict
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append({'line_idx': i, 'line_num': i+1, 'env': m.group(1), 'text': line})
for idx, entry in enumerate(entries):
    i = entry['line_idx']
    next_i = entries[idx+1]['line_idx'] if idx+1 < len(entries) else len(lines)
    label = None
    for k in range(i, next_i):
        lab = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab:
            label = lab.group(1)
            break
    entry['label'] = label
    heading_text = None
    start = entry['text'].find('[')
    j = i
    if start "'!= -1:
        buf = entry['"'text'][start+1:]
        while True:
            idx_close = buf.find(']')
            if idx_close "'!= -1:
                heading_text = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    entry['claim_statuses'] = []
    if heading_text:
        entry['claim_statuses'] = re.findall(r'\\\\ClaimStatus\\w+', heading_text)
# group by env
env_map = defaultdict(list)
for entry in entries:
    if entry['label']:
        env_map[entry['env']].append((entry['label'], entry['claim_statuses'], entry['line_num']))
for env in env_map:
    env_map[env].sort(key=lambda x: x[2])
for env in ['theorem','proposition','conjecture','remark','definition']:
    print(env, len(env_map.get(env, [])))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
theorem 22
proposition 18
conjecture 3
remark 48
definition 12
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
from collections import defaultdict
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append({'line_idx': i, 'line_num': i+1, 'env': m.group(1), 'text': line})
for idx, entry in enumerate(entries):
    i = entry['line_idx']
    next_i = entries[idx+1]['line_idx'] if idx+1 < len(entries) else len(lines)
    label = None
    for k in range(i, next_i):
        lab = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab:
            label = lab.group(1)
            break
    entry['label'] = label
    heading_text = None
    start = entry['text'].find('[')
    j = i
    if start "'!= -1:
        buf = entry['"'text'][start+1:]
        while True:
            idx_close = buf.find(']')
            if idx_close "'!= -1:
                heading_text = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    entry['claim_statuses'] = []
    if heading_text:
        entry['claim_statuses'] = re.findall(r'\\\\ClaimStatus\\w+', heading_text)
# group by env
env_map = defaultdict(list)
for entry in entries:
    if entry['label']:
        env_map[entry['env']].append((entry['label'], entry['claim_statuses'], entry['line_num']))
for env in env_map:
    env_map[env].sort(key=lambda x: x[2])
for env in ['theorem','proposition','conjecture','remark','definition']:
    data = env_map.get(env, [])
    print(env.upper(), len(data))
    for label, statuses, line_num in data:
        print(f\"{label} | line {line_num} | statuses: {statuses if statuses else ['none']}\")
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
THEOREM 22
thm:fundamental-twisting-morphisms | line 399 | statuses: ['\\ClaimStatusProvedHere']
thm:chiral-comparison-lemma | line 594 | statuses: ['none']
thm:pbw-koszulness-criterion | line 747 | statuses: ['\\ClaimStatusProvedHere']
thm:km-chiral-koszul | line 825 | statuses: ['\\ClaimStatusProvedHere']
thm:virasoro-chiral-koszul | line 880 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-concentration | line 1112 | statuses: ['\\ClaimStatusProvedHere']
thm:ainfty-koszul-characterization | line 1257 | statuses: ['\\ClaimStatusProvedHere']
thm:ext-diagonal-vanishing | line 1328 | statuses: ['\\ClaimStatusProvedHere']
thm:kac-shapovalov-koszulness | line 1456 | statuses: ['\\ClaimStatusProvedHere']
thm:associated-variety-koszulness | line 1778 | statuses: ['\\ClaimStatusProvedHere']
thm:koszul-equivalences-meta | line 2015 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-from-sklyanin | line 3232 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-bootstrap | line 3325 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-cobar-isomorphism-main | line 3638 | statuses: ['\\ClaimStatusProvedHere']
thm:yangian-self-dual | line 3829 | statuses: ['\\ClaimStatusProvedHere']
thm:coalgebra-axioms-verified | line 4042 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-computes-koszul-dual-complete | line 4136 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-chiral-koszul-duality | line 4833 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-module-koszul-duality | line 5174 | statuses: ['\\ClaimStatusProvedHere']
wait(call_YbmkdnCZiuZrJTXu0fP4rtDk) timed out:

thinking
**Inspecting potential mismatches**

I think closing the agent might not be necessary right now. I need to inspect the concordance lines, especially line 3214, since there seems to be a mismatch. I should check for more mismatches, like how line 2451 references `Theorem\ref{conj:lagrangian-koszulness}`, which could indicate an environment mismatch with conjecture. The user asked about the seam status, and it might be stale because there's no label here. I'll verify if the actual label exists elsewhere, searching quickly.
exec
/bin/zsh -lc "rg -n \"label\\{conj:lagrangian-koszulness\\}|begin\\{conjecture\\}|begin\\{theorem\\}.*lagrangian|cor:lagrangian-unconditional|lagrangian-perfectness\" chapters/theory/chiral_koszul_pairs.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/arithmetic_shadows.tex:1470:\begin{conjecture}[General finiteness conjecture]
chapters/connections/arithmetic_shadows.tex:3721:\begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
chapters/connections/arithmetic_shadows.tex:4570:\begin{conjecture}[The $\cW_N$ shadow Galois hierarchy;
chapters/connections/arithmetic_shadows.tex:5309:\begin{conjecture}[Shadow principal class]
chapters/connections/arithmetic_shadows.tex:6200:\begin{conjecture}[Quartic closure]%
chapters/connections/arithmetic_shadows.tex:6807:\begin{conjecture}[Defect unification]%
chapters/connections/arithmetic_shadows.tex:7066:\begin{conjecture}[Clutching closure]%
chapters/connections/arithmetic_shadows.tex:7155:\begin{conjecture}[Beilinson closure]%
chapters/connections/arithmetic_shadows.tex:7507:\begin{conjecture}[Modular spectral rigidity]%
chapters/connections/arithmetic_shadows.tex:7951:\begin{conjecture}[Modular spectral rigidity, sharpened form]%
chapters/connections/arithmetic_shadows.tex:8099:\begin{conjecture}[CPS hypotheses from MC $+$ HS-sewing]%
chapters/connections/arithmetic_shadows.tex:8183:\begin{conjecture}[Prime-locality]%
chapters/connections/arithmetic_shadows.tex:8433:\begin{conjecture}[Operadic Rankin--Selberg, main form]%
chapters/connections/arithmetic_shadows.tex:8845:\begin{conjecture}[Ramanujan bound for irrational VOAs]%
chapters/connections/arithmetic_shadows.tex:10215:\begin{conjecture}[Complex saddle-point access to scattering
chapters/connections/arithmetic_shadows.tex:11003:\begin{conjecture}[Conditional Ramanujan for all chirally Koszul
chapters/connections/arithmetic_shadows.tex:11446:\begin{conjecture}[The arithmetic comparison conjecture]%
chapters/connections/concordance.tex:2454: landscape (Proposition~\ref{prop:lagrangian-perfectness},
chapters/connections/concordance.tex:2455: Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
chapters/connections/concordance.tex:3201:(Proposition~\ref{prop:lagrangian-perfectness} verifies
exec
/bin/zsh -lc 'rg -n "thm:operadic-complexity|operadic-complexity-concordance|thm:operadic-complexity-concordance" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7030,7040p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
  7030	\ref{thm:pixton-from-mc-semisimple}
  7031	 & Pixton ideal from MC for semisimple cases
  7032	 & FSZ $+$ PPZ $+$ Givental--Teleman \\
  7033	\ref{thm:operadic-complexity}
  7034	 & $r_{\max} = d_\infty = f_\infty$
  7035	 \textup{(}operadic complexity identification\textup{)}
  7036	 & induction on degree $+$ HPL tree formula \\
  7037	\hline
  7038	\multicolumn{3}{l}{\textit{%
  7039	 April 2026 session: theorem architecture rewrites (A1--A6~+~G7)}} \\
  7040	\hline
 succeeded in 55ms:
metadata/theorem_registry.md:970:| `thm:operadic-complexity-detailed` | `theorem` | 14492 | Operadic complexity |
metadata/theorem_registry.md:2360:| `thm:operadic-complexity-concordance` | `theorem` | 2436 | Operadic complexity |
metadata/theorem_registry.md:2621:| `thm:operadic-complexity` | `theorem` | 248 | Operadic complexity |
metadata/theorem_registry.md:2931:| `thm:thqg-intro-operadic-complexity` | `theorem` | 860 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |
chapters/connections/concordance.tex:2518:\label{thm:operadic-complexity-concordance}%
chapters/connections/concordance.tex:3159: & \texttt{thm:operadic-complexity}
chapters/connections/concordance.tex:7033:\ref{thm:operadic-complexity}
codex
I’m checking one more class of seam failure: concordance appears to refer to labels and theorem names that may not be the live surface in `chiral_koszul_pairs.tex`. If those labels drifted or the routing landed on the wrong object, that’s a stale seam even when the prose is otherwise accurate.
exec
/bin/zsh -lc 'rg -n "operadic-complexity" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "rem:non-circular-logical-chain|non-circular logical chain|Logical independence of the proved core|circularity-free" chapters/connections/concordance.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1356,1372p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:4274:\label{cor:circularity-free-koszul}
chapters/theory/chiral_koszul_pairs.tex:4399:\noindent\emph{Logical independence.} We record that the argument is circularity-free:
chapters/theory/chiral_koszul_pairs.tex:4409:When $\mathcal{A}$ is quadratic with relations $R \subset j_*j^*(\mathcal{V}^{\boxtimes 2})$, the weight filtration on $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is bounded and the spectral sequence of Stage~3d collapses at $E_2$. In this case $\mathcal{A}^!$ is the classical quadratic dual; no completion is needed, and Corollary~\ref{cor:circularity-free-koszul} reduces to the Ginzburg--Kapranov theorem for operads.
chapters/connections/concordance.tex:1363:\emph{Logical independence of the proved core}
chapters/connections/concordance.tex:4874:(Remark~\ref{rem:non-circular-logical-chain}).
chapters/connections/concordance.tex:4898:Remark~\ref{rem:non-circular-logical-chain}).
 succeeded in 54ms:
  1356	degrees; however, the fullness of the all-degree unification
  1357	$\Theta_\cA \in \mathrm{MC}(\operatorname{hom}_\alpha)$ at all orders
  1358	is MC2 (proved by the bar-intrinsic construction,
  1359	Theorem~\ref{thm:mc2-bar-intrinsic}); finite-order projections
  1360	$\Theta_\cA^{\leq r}$ are its truncations. Item~(7) is an external structural
  1361	fact independent of degree.
  1362	
  1363	\emph{Logical independence of the proved core}
  1364	(cf.\ Remark~\ref{rem:mok-dependency}).
  1365	The five main theorems~A--D,\,H and the bar-intrinsic MC
  1366	construction (Theorem~\ref{thm:mc2-bar-intrinsic}) depend on
  1367	\emph{no external preprint}: they rest on the convolution-level
  1368	$D^2 = 0$, which follows from the classical fact
  1369	$\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$.
  1370	The three-pillar preprints provide structural enrichment beyond
  1371	the proved core:
  1372	\begin{itemize}[nosep]
exec
/bin/zsh -lc 'rg -n "item:kp-" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4720,4785p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{example}[Superconformal algebras]
\label{ex:n2-superconformal}

The $\mathcal{N}=2$ superconformal algebra has:
\begin{itemize}
\item Bosonic: $T(z)$ weight 2, $J(z)$ weight 1
\item Fermionic: $G^+(z)$, $G^-(z)$ weight $3/2$
\end{itemize}

The $\mathbb{Z}/2\mathbb{Z}$-grading introduces fermionic signs:
\[G^+(z)G^+(w) \sim 0, \quad G^+(z)G^-(w) \sim \frac{c/3}{(z-w)^3} + \frac{J(w)}{(z-w)^2} + \cdots\]

\emph{Completion.} Requires \emph{super-coalgebra} structure:
\[\Delta(G^+) = G^+ \boxtimes 1 + 1 \boxtimes G^+\]
(generators are primitive, as in Step~2 above; the fermionic sign enters in the \emph{cocommutativity} constraint $\tau \circ \Delta = \Delta$ where $\tau(x \boxtimes y) = (-1)^{|x||y|} y \boxtimes x$).
\end{example}

%----------------------------------------------------------------
% SUMMARY TABLE


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
from collections import defaultdict
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append({'line_idx': i, 'line_num': i+1, 'env': m.group(1), 'text': line})
max_lookahead = 15
for idx, entry in enumerate(entries):
    i = entry['line_idx']
    next_i = entries[idx+1]['line_idx'] if idx+1 < len(entries) else len(lines)
    label = None
    upper = min(next_i, i + max_lookahead)
    for k in range(i, upper):
        lab = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab:
            label = lab.group(1)
            break
    entry['label'] = label
    heading_text = None
    start = entry['text'].find('[')
    j = i
    if start "'!= -1:
        buf = entry['"'text'][start+1:]
        while True:
            idx_close = buf.find(']')
            if idx_close "'!= -1:
                heading_text = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    entry['claim_statuses'] = []
    if heading_text:
        entry['claim_statuses'] = re.findall(r'\\\\ClaimStatus\\w+', heading_text)
# group entries with labels
env_map = defaultdict(list)
for entry in entries:
    if entry['label']:
        env_map[entry['env']].append((entry['label'], entry['claim_statuses'], entry['line_num']))
for env in env_map:
    env_map[env].sort(key=lambda x: x[2])
for env in ['theorem','proposition','conjecture','remark','definition']:
    data = env_map.get(env, [])
    print(env.upper(), len(data))
    for label, statuses, line_num in data:
        print(f\"{label} | line {line_num} | statuses: {statuses if statuses else ['none']}\")
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
THEOREM 22
thm:fundamental-twisting-morphisms | line 399 | statuses: ['\\ClaimStatusProvedHere']
thm:chiral-comparison-lemma | line 594 | statuses: ['none']
thm:pbw-koszulness-criterion | line 747 | statuses: ['\\ClaimStatusProvedHere']
thm:km-chiral-koszul | line 825 | statuses: ['\\ClaimStatusProvedHere']
thm:virasoro-chiral-koszul | line 880 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-concentration | line 1112 | statuses: ['\\ClaimStatusProvedHere']
thm:ainfty-koszul-characterization | line 1257 | statuses: ['\\ClaimStatusProvedHere']
thm:ext-diagonal-vanishing | line 1328 | statuses: ['\\ClaimStatusProvedHere']
thm:kac-shapovalov-koszulness | line 1456 | statuses: ['\\ClaimStatusProvedHere']
thm:associated-variety-koszulness | line 1778 | statuses: ['\\ClaimStatusProvedHere']
thm:koszul-equivalences-meta | line 2015 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-from-sklyanin | line 3232 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-bootstrap | line 3325 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-cobar-isomorphism-main | line 3638 | statuses: ['\\ClaimStatusProvedHere']
thm:yangian-self-dual | line 3829 | statuses: ['\\ClaimStatusProvedHere']
thm:coalgebra-axioms-verified | line 4042 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-computes-koszul-dual-complete | line 4136 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-chiral-koszul-duality | line 4833 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-module-koszul-duality | line 5174 | statuses: ['\\ClaimStatusProvedHere']


thinking
**Analyzing numbering discrepancies**

I find it interesting that the concordance lists items with identical labels based on the meta-theorem's numbering, but the chapter doesn’t have item labels like `item:kp-...`. I need to verify by checking specific lines. This suggests the concordance references internal labels that are absent in the chapter. The claim that the references are identical seems false. Since the user asked about theorem status, it could really point to a navigation issue due to mismatched item labels.
thinking
**Identifying a fix for labeling issues**

To fix the issue, I could either add `\label{item:kp-*}` to the chapter theorem items or revise the concordance to state that the "numbering agrees conceptually" without claiming identical labels. The user specifically asked for an exact fix, so I should lean toward adding the labels. I’ll need to check if the chapter uses enumeration without labels and look at the relevant lines where numbering conflicts occur. It seems bridging the gap at the seam is essential here.
thinking
**Implementing a fix for labeling**

To address the issue, I can either add matching `\label{item:kp-*}` tags to each item in the theorem `thm:koszul-equivalences-meta` or simply remove the sentence asserting that the numbering and anchors are identical. Both approaches seem valid, but adding the labels appears to be the more thorough solution. This will ensure consistency and clarity in referencing items throughout the document. Good to have a straightforward fix!
thinking
**Evaluating mention formats**

I’m thinking about how the format requires a singular `file:line`, but maybe it would be helpful to reference the primary line and mention others in the problem. I need to decide on that. I should probably search for other "equivalent" mentions about item (viii) in concordance as there might be more information to uncover. I could really use regular expressions for this!
exec
/bin/zsh -lc "rg -n \"item:kp-hochschild|ChirHoch\\"'^'"\\*|Hochschild polynomial|ten equivalences|Unconditional equivalences \\(i\\)--\\(x\\)|core cycle|\\Leftrightarrow.*kp-hochschild|kp-facthom|kp-barrbeck|kp-dmod\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:item:kp-hochschild|ChirHoch\^\*|Hochschild polynomial|ten equivalences|Unconditional equivalences \(i\)--\(x\)|core cycle|\Leftrightarrow.*kp-hochschild|kp-facthom|kp-barrbeck|kp-dmod)
                                                                                                                                 ^^
error: unrecognized escape sequence

thinking
**Refining label search within environment boundaries**

I’m planning to improve the logic for finding `\label` entries by scanning only from the environment’s `\begin` line up to its closing `\end` line, to avoid capturing labels from subsequent environments. This approach should prevent mistakenly linking labels from nearby corollaries or remarks and keep the detection accurate. I’ll implement this by locating the `\end{env}` line after the entry start and restricting the label search within these bounds.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import re, pathlib
from collections import defaultdict
path = pathlib.Path('chapters/theory/chiral_koszul_pairs.tex')
lines = path.read_text().splitlines()
begin_pattern = re.compile(r'\\\\begin\\{(theorem|proposition|conjecture|remark|definition)\\}')
entries = []
for i,line in enumerate(lines):
    m = begin_pattern.search(line)
    if m:
        entries.append({'line_idx': i, 'line_num': i+1, 'env': m.group(1), 'text': line})
for entry in entries:
    env = entry['env']
    start = entry['line_idx']
    end_idx = None
    for j in range(start, len(lines)):
        if f\"\\\\end{{{env}}}\" in lines[j]:
            end_idx = j
            break
    if end_idx is None:
        end_idx = len(lines)
    label = None
    for k in range(start, end_idx+1):
        lab = re.search(r'\\\\label\\{(["'^}]+)'"\\}', lines[k])
        if lab:
            label = lab.group(1)
            break
    entry['label'] = label
    heading_text = None
    start_bracket = entry['text'].find('[')
    j = start
    if start_bracket "'!= -1:
        buf = entry['"'text'][start_bracket+1:]
        while True:
            idx_close = buf.find(']')
            if idx_close "'!= -1:
                heading_text = buf[:idx_close]
                break
            j += 1
            if j >= len(lines):
                break
            buf += '"'\\n' + lines[j]
    entry['claim_statuses'] = []
    if heading_text:
        entry['claim_statuses'] = re.findall(r'\\\\ClaimStatus\\w+', heading_text)
# group entries with labels
env_map = defaultdict(list)
for entry in entries:
    if entry['label']:
        env_map[entry['env']].append((entry['label'], entry['claim_statuses'], entry['line_num']))
for env in ['theorem','proposition','conjecture','remark','definition']:
    data = env_map.get(env, [])
    data.sort(key=lambda x: x[2])
    print(env.upper(), len(data))
    for label, statuses, line_num in data:
        print(f\"{label} | line {line_num} | statuses: {statuses if statuses else ['none']}\")
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
THEOREM 22
thm:fundamental-twisting-morphisms | line 399 | statuses: ['\\ClaimStatusProvedHere']
thm:chiral-comparison-lemma | line 594 | statuses: ['none']
thm:pbw-koszulness-criterion | line 747 | statuses: ['\\ClaimStatusProvedHere']
thm:km-chiral-koszul | line 825 | statuses: ['\\ClaimStatusProvedHere']
thm:virasoro-chiral-koszul | line 880 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-concentration | line 1112 | statuses: ['\\ClaimStatusProvedHere']
thm:ainfty-koszul-characterization | line 1257 | statuses: ['\\ClaimStatusProvedHere']
thm:ext-diagonal-vanishing | line 1328 | statuses: ['\\ClaimStatusProvedHere']
thm:kac-shapovalov-koszulness | line 1456 | statuses: ['\\ClaimStatusProvedHere']
thm:associated-variety-koszulness | line 1778 | statuses: ['\\ClaimStatusProvedHere']
thm:koszul-equivalences-meta | line 2015 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-from-sklyanin | line 3232 | statuses: ['\\ClaimStatusProvedHere']
thm:koszulness-bootstrap | line 3325 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-cobar-isomorphism-main | line 3638 | statuses: ['\\ClaimStatusProvedHere']
thm:yangian-self-dual | line 3829 | statuses: ['\\ClaimStatusProvedHere']
thm:coalgebra-axioms-verified | line 4042 | statuses: ['\\ClaimStatusProvedHere']
thm:bar-computes-koszul-dual-complete | line 4136 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-chiral-koszul-duality | line 4833 | statuses: ['\\ClaimStatusProvedHere']
thm:e1-module-koszul-duality | line 5174 | statuses: ['\\ClaimStatusProvedHere']
exec
/bin/zsh -lc "rg -n -F -e 'item:kp-hochschild' -e 'Hochschild polynomial' -e 'ten equivalences' -e 'Unconditional equivalences (i)--(x)' -e 'core cycle' -e 'kp-facthom' -e 'kp-barrbeck' -e 'kp-dmod' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2388:\textup{(\ref{item:kp-def})}--\textup{(\ref{item:kp-dmod})}
2416:\item\label{item:kp-barrbeck}
2421:\item\label{item:kp-facthom}
2426:\item\label{item:kp-hochschild}
2458:\item\label{item:kp-dmod}
2461: \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
3197:\emph{Status}: ten equivalences
3203:$\mathcal{D}$-module purity~(\ref{item:kp-dmod})
3214:The core cycle
3215:(\ref{item:kp-def})$\Leftrightarrow$(\ref{item:kp-pbw})$\Leftrightarrow$(\ref{item:kp-ainfty})$\Leftrightarrow$(\ref{item:kp-barcobar})$\Leftrightarrow$(\ref{item:kp-hochschild})
3217:bar-cobar inversion~$\to$ Hochschild polynomial growth~$\to$
3222:Barr--Beck--Lurie~(\ref{item:kp-barrbeck}) by conservativity +
3224:FH concentration~(\ref{item:kp-facthom}) via bar = FH,
codex
**Label inventory**

Theorem labels (environment: theorem; claim-status macros shown when present):

```text
Label | ClaimStatus macros
`thm:fundamental-twisting-morphisms` | `\ClaimStatusProvedHere`
`thm:chiral-comparison-lemma` | none
`thm:pbw-koszulness-criterion` | `\ClaimStatusProvedHere`
`thm:km-chiral-koszul` | `\ClaimStatusProvedHere`
`thm:virasoro-chiral-koszul` | `\ClaimStatusProvedHere`
`thm:bar-concentration` | `\ClaimStatusProvedHere`
`thm:ainfty-koszul-characterization` | `\ClaimStatusProvedHere`
`thm:ext-diagonal-vanishing` | `\ClaimStatusProvedHere`
`thm:kac-shapovalov-koszulness` | `\ClaimStatusProvedHere`
`thm:associated-variety-koszulness` | `\ClaimStatusProvedHere`
`thm:koszul-equivalences-meta` | `\ClaimStatusProvedHere`
`thm:koszulness-from-sklyanin` | `\ClaimStatusProvedHere`
`thm:koszulness-bootstrap` | `\ClaimStatusProvedHere`
`thm:bar-cobar-isomorphism-main` | `\ClaimStatusProvedHere`
`thm:yangian-self-dual` | `\ClaimStatusProvedHere`
`thm:coalgebra-axioms-verified` | `\ClaimStatusProvedHere`
`thm:bar-computes-koszul-dual-complete` | `\ClaimStatusProvedHere`
`thm:e1-chiral-koszul-duality` | `\ClaimStatusProvedHere`
`thm:e1-module-koszul-duality` | `\ClaimStatusProvedHere`
`thm:structure-exchange` | `\ClaimStatusProvedHere`
`thm:ainfty-duality-exchange` | `\ClaimStatusProvedHere`
`thm:curved-koszul-pairs` | `\ClaimStatusProvedHere`
```

Proposition labels (environment: proposition):

```text
Label | ClaimStatus macros
`prop:bar-universal-property` | `\ClaimStatusProvedElsewhere`
`prop:ainfty-formality-implies-koszul` | `\ClaimStatusProvedHere`
`prop:pbw-universality` | `\ClaimStatusProvedHere`
`prop:li-bar-poisson-differential` | `\ClaimStatusProvedHere`
`prop:large-orbit-obstruction` | `\ClaimStatusProvedHere`
`prop:koszul-closure-properties` | `\ClaimStatusProvedHere`
`prop:swiss-cheese-nonformality-by-class` | `\ClaimStatusProvedHere`
`prop:sc-formal-iff-class-g` | `\ClaimStatusProvedHere`
`prop:d-module-purity-km` | none
`prop:d-module-purity-km-equivalence` | `\ClaimStatusProvedHere`
`prop:koszulness-formality-equivalence` | `\ClaimStatusProvedHere`
`prop:minimal-model-non-koszul` | `\ClaimStatusProvedHere`
`prop:cumulant-window-inversion` | `\ClaimStatusProvedHere`
`prop:yangian-koszul-general` | `\ClaimStatusProvedHere`
`prop:koszul-character-identity` | `\ClaimStatusProvedHere`
`prop:bar-neq-quasiprimary` | `\ClaimStatusProvedHere`
`prop:ff-involution-uniqueness` | `\ClaimStatusProvedHere`
`prop:koszul-dual-tensor-product` | `\ClaimStatusProvedHere`
```

Conjecture labels (environment: conjecture):

```text
Label | ClaimStatus macros
`conj:admissible-koszul-rank-obstruction` | none
`conj:d-module-purity-wn-principal` | `\ClaimStatusConjectured`
`conj:derived-bc-betagamma` | `\ClaimStatusConjectured`
```

Remark labels (environment: remark):

```text
Label | ClaimStatus macros
`rem:explicit-twisted-differential` | none
`rem:construction-vs-resolution` | none
`rem:MC-is-Stokes` | none
`rem:theorem-A-decomposition` | none
`rem:classical-to-chiral-koszul` | none
`rem:ce-vs-exterior` | none
`rem:ce-vs-chiral-bar` | none
`rem:one-loop-exactness` | none
`rem:ainfty-genus0-shadow` | none
`rem:pbw-vs-diagonal-critical` | none
`rem:rationality-not-koszul-criterion` | none
`rem:admissible-koszul-status` | none
`rem:w2-koszulness` | none
`rem:kac-shapovalov-arithmetic-shadow` | none
`rem:dq-koszul-compatibility` | none
`rem:li-bar-no-poisson-identification` | none
`rem:orbit-hierarchy-koszulness` | none
`rem:li-bar-vs-kac-shapovalov` | none
`rem:fh-vii-uniform-weight-scope` | none
`rem:koszul-closure-not-quotients` | none
`rem:ainfty-formality-gkw` | none
`rem:loop-exactness-ordering` | none
`rem:d-module-purity-content` | none
`rem:d-module-purity-family-dependence` | none
`rem:koszulness-computational-landscape` | none
`rem:koszulness-vs-shadow-depth` | none
`rem:shadow-class-direct-sum` | none
`rem:class-w-koszul-frontier` | none
`rem:sklyanin-koszulness-scope` | none
`rem:kinematics-dynamics-split` | none
`rem:primitive-defect-probe` | none
`rem:theorem-a-lagrangian` | none
`rem:theorem-a-tau` | none
`rem:theorem-a-model` | none
`rem:independence-construction` | none
`rem:comparison-classical` | none
`sec:feynman_genus_g` | none
`rem:convergence-pro-nil` | none
`rem:e1-koszul-hypotheses` | none
`rem:FG-comparison` | none
`rem:fukaya-bar-koszul` | `\ClaimStatusProvedElsewhere`
`rem:module-category-frontier` | none
`rem:bar-quasiprimary-free-field` | none
`rem:categorified-koszul-kl-bfm` | none
`rem:scope-curved-koszul` | none
`rem:w-algebra-classical-vs-chiral-koszul` | none
`rem:ckp-dependency-digest` | none
```

Definition labels (environment: definition):

```text
Label | ClaimStatus macros
`def:chiral-twisting-datum` | none
`def:chiral-koszul-morphism` | none
`def:chiral-koszul-pair` | none
`def:primitive-cumulant-quotient` | `\ClaimStatusProvedHere`
`def:primitive-generating-series` | `\ClaimStatusProvedHere`
`def:completion-hilbert-series` | `\ClaimStatusProvedHere`
`def:primitive-defect-series` | `\ClaimStatusProvedHere`
`def:completion-entropy` | `\ClaimStatusProvedHere`
`def:koszul-dual-coalgebra` | none
`def:augmented-e1` | none
`def:pronilpotent-conilpotent` | none
`def:curved-ainfty-kp` | none
```

**Dependency / defer remarks**

- Line 4018 (`rem:independence-construction`): Stage 1’s definition of the Koszul dual coalgebra uses only the $(\mathcal{V},R)$ presentation, OPE constants, and residue pairing; it “makes no reference” to the bar construction, $\mathcal{A}_1$, or any Koszul pair, so the construction is explicitly circularity-free.
- Line 5153 (`rem:module-category-frontier`): Signals that the full ordinary-derived module-category duality for an arbitrary chiral Koszul pair is not proved here—extending it is left to future extra hypotheses/comparison theorems—so the general construction/proof is deferred.
- Line 5949 (`rem:ckp-dependency-digest`): Lists the chapter’s key results (Theorems A₀–A₂, PBW criterion, $\Eone$ duality, etc.) and notes the later chapters that consume them, providing an explicit dependency map (“A₀ … used by Chapters …,” etc.).




thinking
**Evaluating theorem status**

I'm looking at a potential mismatch with the concordance header saying "conditional/partial," but the item text references a theorem. I think I need to change the reference from Theorem to Conjecture since mixing the two is likely stale. I should verify the actual label and status in the source, especially noting that the meta-theorem conditionally refers to item (xi). It seems I might get conflicting information between the concordance and chapter, but I’ll see how relevant that is.
thinking
**Investigating theorem status**

I’m thinking there might be a mismatch with the theorem registry. The user’s mission indicates it’s about concordance and theory, not necessarily the theorem registry. Initially, I need to check if the theorem status in concordance matches the actual .tex file, ensuring there are no outdated statuses. I want to search for `thm:operadic-complexity`, but my search didn't yield matches in the chapter. Instead, it seems to be listed in the concordance, which might not be relevant to the chapter.
thinking
**Reviewing edits for clarity**

I’m looking at three edits that need attention: First, the heading at line 2392 should change to a block structure. Second, the status summary at line 3197 requires modifications to include nine equivalences, and third, I need to remove `kp-hochschild` from the equivalence chain at line 3214. I also see there's a potential gap at line 2426 that would require moving item text from the equivalence block to the consequence block and adding scope on Koszul locus. I want to clarify these lines to make sure everything matches up correctly.
thinking
**Investigating concordance cross-references**

I need to check if the concordance cross-reference table summary at line 3197 is located in the same section as the cross-reference table. I have the relevant line numbers I’ll be examining. It’s important to thoroughly inspect the concordance from lines 2383 to 2462 to ensure I can accurately reference those line numbers. This will help me gather all necessary details for clarity and consistency. Let's get this sorted out!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2818,2832p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2818	(Conjecture~\ref{conj:ambient-complementarity},
  2819	Theorem~\ref{thm:ambient-complementarity-fmp}) equips the modular
  2820	deformation space with a $(-1)$-shifted symplectic structure.
  2821	Koszulness should be Lagrangian transversality.
  2822	
  2823	\begin{conjecture}[Conditional Lagrangian characterization of chiral Koszulness;
  2824	\ClaimStatusConjectured]%
  2825	\label{conj:lagrangian-koszulness}%
  2826	\index{Koszulness!Lagrangian characterization}
  2827	\index{Lagrangian!transversality and Koszulness}
  2828	\index{shifted-symplectic!Lagrangian criterion for Koszulness}
  2829	Suppose the ambient complementarity tangent complex $T_{\mathrm{comp}}(\cA)$
  2830	carries a $(-1)$-shifted symplectic structure~$\omega$ \textup{(}as in
  2831	Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}, and the
  2832	one-sided deformation maps


thinking
**Evaluating Lagrangian characterization**

I'm considering a fix for the "Conditional Lagrangian characterization," possibly noting it as conjecture. The severity might be MEDIUM or HIGH due to a stale environment or label. I need to search if the concordance has anything about circularity in this section, but I don't see it. I'll check line 2469-2508 regarding simple quotients, which might be consistent. I also want to inspect cross-references in the table to ensure everything aligns correctly.
thinking
**Searching for concordance**

I might need to search for whether there's any concordance related to the chapter route mentioning "antecedent hypotheses." I'm feeling a bit unsure about whether I'll find it, but I think a search could help clarify things. Let's see what I can uncover with that keyword! I wonder if it will lead me to useful information that connects the dots. Let's get started!
exec
/bin/zsh -lc "rg -n -F -e 'antecedent hypotheses' -e 'No quasi-isomorphism statement is built into the definition itself' -e 'circularity-free' -e 'Theorem~\\ref{thm:bar-cobar-isomorphism-main} then' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '625,655p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   625	\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
   626	\index{Koszul pair!chiral|textbf}
   627	A \emph{chiral Koszul pair} on a smooth projective curve~$X$
   628	is a pair of chiral Koszul data
   629	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
   630	Definition~\textup{\ref{def:chiral-koszul-morphism})}
   631	\[
   632	(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
   633	(\cA_2, \cC_2, \tau_2, F_\bullet)
   634	\]
   635	equipped with Verdier-compatible factorization-algebra
   636	identifications
   637	\[
   638	\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
   639	\qquad
   640	\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
   641	\]
   642	compatible with the twisting morphisms and filtrations.
   643	In this situation we write $\cA_2 \simeq \cA_1^!$ and
   644	$\cA_1 \simeq \cA_2^!$.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '617,624p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   617	\subsection{The concept of chiral Koszul pairs: precise formulation}
   618	
   619	To handle non-quadratic examples, we extend the notion of Koszul pairs
   620	beyond the quadratic setting. The defining property is a set of
   621	\emph{recognition criteria} (checkable conditions on the pair) from
   622	which the full bar-cobar identification follows as a theorem.
   623	No quasi-isomorphism statement is built into the definition itself.
   624	







thinking
**Organizing fixes**

I need to restructure the list: keeping sections (i)-(vii) and (ix)-(x) under “Unconditional equivalences” while moving (viii) to a new block titled “Unconditional consequence on the Koszul locus.” I should make clear that there's no converse from (viii) to the equivalence circuit. For referencing, I might need to use file:line format, specifying line 2392 and mentioning others like 2426. I see several findings to address, ensuring I’m both exhaustive and concise.
thinking
**Inspecting inconsistencies**

The user has asked for every inconsistency or gap at the seam, but I’m thinking there likely aren't too many. I should check if the chapter actually includes `rem:dq-koszul-compatibility` and verify if table line 3152 is correctly placed. It seems essential to ensure these details match up as expected. Let’s dig into this to confirm accuracy and clarify any potential issues. That could help wrap things up neatly!
thinking
**Evaluating audit findings**

I'm thinking about the number of seam items audited and how best to present them. I could count 12 numbered items, plus 2 status summaries and 1 routing seam, bringing the total to 15. So, maybe I should note "Checked: 15 | Findings: 8 | Verdict: FAIL." But I wonder if I should clarify what counts as checked. It seems essential to ensure clarity and honesty in my findings, especially for grounded claims in the chapter references.
thinking
**Deciding on findings inclusion**

I'm thinking I should include both files among the findings. For the navigation label gap, I might cite chapter line 2031 or concordance line 2387. If the fix requires editing, I could go either way. The exact fix could mean adding labels in the chapter, but maybe a change in the concordance would be an easier fix. I need to make a choice on which file to modify. It's important to clarify that!
thinking
**Reviewing routing remarks**

I'm considering whether to note the absence of "routing remarks for circular dependencies" at two specific transition points: right after line 2385, where the meta-theorem is introduced, and before line 3214, where the proof circuit starts. I think one finding may be enough with line 3214 or 2385. Maybe I should insert a note after line 2389, clarifying some definitions and their construction. Overall, I might have identified a gap to address.
thinking
**Fixing chapter details**

I’m considering how to adjust the wording from lines 2062-2071, specifically about `\mathrm{ChirHoch}^*(\cA)$`, which focuses on cohomological degrees $\{0,1,2\}$ and duality. The user requested an exact fix, but I wonder if I need the full formula for concordance. Perhaps it's better to move this adjustment to a separate block, starting with “On the Koszul locus.” I might also need to add 12 labels to items, but that could get lengthy. Let’s tackle it carefully!
thinking
**Adjusting routing remarks**

I need to insert a routing note right after line 2389 or before 3214. It's crucial to clarify that a specific definition uses antecedent hypotheses only and doesn't involve a bar-cobar quasi-isomorphism. I’m also considering if findings at lines 3197 and 3214 reflect the same equivalence inflation, but the user asked for any inconsistencies, so I’ll note that. Adjusting severity at 3197 to MEDIUM seems reasonable since the user summary repeats the same error. Lastly, I should ensure line 2426 is scoped properly.
codex
- [CRITICAL] chapters/connections/concordance.tex:2392 — PROBLEM: The heading `Unconditional equivalences (i)--(x)` is false on the live chapter surface. In `chapters/theory/chiral_koszul_pairs.tex:2021-2027`, only `(i)--(vii),(ix)--(x)` are equivalent; `chapters/theory/chiral_koszul_pairs.tex:2062-2072` isolates `(viii)` as an unconditional consequence on the Koszul locus, and `chapters/theory/chiral_koszul_pairs.tex:2117-2123` explicitly says no converse from `(viii)` is proved. The item now sitting in the equivalence block at `chapters/connections/concordance.tex:2426-2433` is status-inflated. FIX: rename the block to `Unconditional equivalences (i)--(vii),(ix)--(x)`, move the `item:kp-hochschild` paragraph into its own block headed `Unconditional consequence on the Koszul locus`, and add the chapter’s caveat that no converse from `(viii)` is proved.

- [CRITICAL] chapters/connections/concordance.tex:3214 — PROBLEM: The “core cycle” makes `(\ref{item:kp-hochschild})` part of an equivalence chain, contradicting `chapters/theory/chiral_koszul_pairs.tex:2022-2023` and `2117-2123`, where `(viii)` is consequence-only. FIX: rewrite the line to `(\ref{item:kp-def})\Leftrightarrow(\ref{item:kp-pbw})\Leftrightarrow(\ref{item:kp-ainfty})\Leftrightarrow(\ref{item:kp-barcobar})`, and change the next sentence so Hochschild is a one-way output: `(\ref{item:kp-barcobar})\Rightarrow(\ref{item:kp-hochschild}) on the Koszul locus`, not a return arrow to Koszul-complex acyclicity.

- [HIGH] chapters/connections/concordance.tex:2416 — PROBLEM: Item `(vi)` drops the fiber restriction and says the Barr--Beck--Lurie comparison “is an equivalence”. The chapter states only the fibered version: `chapters/theory/chiral_koszul_pairs.tex:2048-2050` says the comparison is an equivalence `on the fiber over \barBgeom(\cA)`. FIX: replace the item text with `Barr--Beck--Lurie comparison for \barBch\dashv\Omegach is an equivalence on the fiber over \barBgeom(\cA)`.

- [HIGH] chapters/connections/concordance.tex:2421 — PROBLEM: Item `(vii)` overstates the scope to `\int_X\cA` “for all smooth X”. The live chapter narrows this: `chapters/theory/chiral_koszul_pairs.tex:2051-2052` states `\int_{\mathbb{P}^1}\cA` is concentrated in degree `0`, and `2185-2196` says the unconditional equivalence is only the `g=0` specialization; higher genus needs the uniform-weight hypothesis. FIX: replace the item with `Factorization homology \int_{\mathbb{P}^1}\cA is concentrated in degree~0`, and append `the intended equivalence is the genus-0 specialization; see Remark~\ref{rem:fh-vii-uniform-weight-scope}`.

- [HIGH] chapters/connections/concordance.tex:2451 — PROBLEM: The line cites `Theorem~\ref{conj:lagrangian-koszulness}` even though the source is a conjecture: `chapters/theory/bar_cobar_adjunction_inversion.tex:2823-2825` is `\begin{conjecture}...\label{conj:lagrangian-koszulness}`, and `chapters/theory/chiral_koszul_pairs.tex:2024-2027` treats `(xi)` as conditional. FIX: change the citation to `Conjecture~\ref{conj:lagrangian-koszulness}`, rename the item `Lagrangian criterion`, and keep unconditional status only via `Proposition~\ref{prop:lagrangian-perfectness}` and `Corollary~\ref{cor:lagrangian-unconditional}`.

- [HIGH] chapters/connections/concordance.tex:3197 — PROBLEM: The status summary says `ten equivalences`, but the chapter introduction `chapters/theory/chiral_koszul_pairs.tex:61-73` and the live theorem statement `2021-2027` give `9 + 1 + 1 + 1`: nine unconditional equivalences, one proved consequence, one conditional equivalence, one one-directional condition. FIX: replace the sentence with `nine unconditional equivalences (i)--(vii),(ix)--(x); item (viii) is an unconditional consequence on the Koszul locus; item (xi) is conditional in general and unconditional on the standard landscape; item (xii) is one-directional`.

- [MEDIUM] chapters/connections/concordance.tex:2387 — PROBLEM: The seam promises that the item numbering in concordance and chapter is identical, but `chapters/theory/chiral_koszul_pairs.tex:2031-2059,2063-2083` has no `\label{item:kp-*}` anchors at all. The concordance numbering exists only locally. FIX: add `\label{item:kp-def}`, `item:kp-pbw`, `item:kp-ainfty`, `item:kp-ext`, `item:kp-barcobar`, `item:kp-barrbeck`, `item:kp-facthom`, `item:kp-hochschild`, `item:kp-nullvec`, `item:kp-fmbdy`, `item:kp-lagrangian`, and `item:kp-dmod` to the twelve `\item[...]` lines in `chapters/theory/chiral_koszul_pairs.tex`.

- [MEDIUM] chapters/connections/concordance.tex:2385 — PROBLEM: The concordance enters the meta-theorem seam with no routing remark for the chapter’s circularity control. The live chapter is explicit that no bar-cobar quasi-isomorphism is built into the definition (`chapters/theory/chiral_koszul_pairs.tex:623`), that the hypotheses are antecedent (`647-654`), and that the circularity-free construction is carried out in `3935-4405`; none of that is surfaced here. FIX: insert immediately after line 2389: `Routing note: Definition~\ref{def:chiral-koszul-pair} uses only antecedent twisting/Koszul/Verdier data; no bar-cobar quasi-isomorphism is built into the definition. See \S\ref{sec:three-stage-construction}, especially Corollary~\ref{cor:circularity-free-koszul}, for the circularity-free construction.`

## Summary
Checked: 15 | Findings: 8 | Verdict: FAIL
tokens used
129,275
