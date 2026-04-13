# C02_introduction (653s)

- [CRITICAL] chapters/theory/introduction.tex:2508 — PROBLEM: `\phantomsection\label{thm:modular-koszul-duality-main}` is a dummy anchor, not a theorem, but the manuscript cites it as “Theorem” and even cites parts `(ii)` and `(iv)`. FIX: restore the real theorem block at this location from `standalone/introduction_full_survey.tex:1877` onward as a theorem/maintheorem with parts `(i)`–`(v)`, and keep the `thm:` label on that environment instead of on a phantom section.

- [HIGH] chapters/theory/introduction.tex:2494 — PROBLEM: theorem-like stubs `def:modular-homotopy-theory-intro`, `prop:modular-homotopy-classification`, `prop:shadow-massey-identification`, and `rem:categorical-logarithm-paradigm` were left behind as `\phantomsection` anchors after relocation, but other chapters still cite them as Definition/Proposition/Remark objects. FIX: restore the actual environments from `standalone/introduction_full_survey.tex:3448`, `3504`, `3574`, and `1986`, or rename those labels to neutral `sec:` anchors and update every downstream `Definition~\ref`, `Proposition~\ref`, and `Remark~\ref` accordingly.

- [HIGH] chapters/theory/introduction.tex:2495 — PROBLEM: equation/section stubs `eq:all-degree-master-eq-intro`, `eq:arnold-seed`, `eq:bar-graded-object-intro`, `eq:the-seed`, `eq:universal-MC`, `sec:flat-connection-intro`, `sec:modular-char-spectral-disc-intro`, `sec:primitive-kernel-intro`, and `sec:the-seed` are anchored to `\phantomsection`, yet the manuscript uses `\eqref`/`\ref` on them as if they were real numbered displays or sections. FIX: move each label onto the corresponding live equation/section, or restore the original displays from `standalone/introduction_full_survey.tex:234`, `242`, `284`, `2679`, `3134`, `1051`, `1133`, `2058`, and `2938`.

- [HIGH] chapters/theory/introduction.tex:2141 — PROBLEM: notation collides with itself. Earlier the file defines the family constant by `\kappa(\cA)+\kappa(\cA^!)=K_\cA` (lines 355–358), but this table redefines `K` as `c+c'`. FIX: rename the table column and prose to `c+c'` or `K_c`, and add a separate `K_\kappa := \kappa(\cA)+\kappa(\cA^!)` column if that invariant is also meant to appear.

- [HIGH] chapters/theory/introduction.tex:606 — PROBLEM: the same sentence says `Q_g(\cA)` and `Q_g(\cA^!)` are the `\pm1` eigenspaces of an involution, that their intersection is `Z(\cA)`, and that the ambient complex is their direct sum. `\pm1` eigenspaces intersect trivially. FIX: replace the last sentence with “Their intersection is \(0\); the ambient complex is the direct sum \(Q_g(\cA)\oplus Q_g(\cA^!)\).” If the center is intended to appear, describe it separately as the fiber/local system, not as the intersection.

- [HIGH] chapters/theory/introduction.tex:1481 — PROBLEM: the Swiss-cheese paragraph asserts an “open-to-closed boundary operator” and says the closed sector is a quotient of the open sector. That contradicts the manuscript’s own SC directionality convention. FIX: rewrite the last two sentences to: “The SC structure is two-coloured and directional; it lives on the pair \((\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)\), not on the bar complex. There is no open-to-closed operadic map, so the closed sector is not obtained as a quotient of the open bar complex.”

- [MEDIUM] chapters/theory/introduction.tex:2592 — PROBLEM: the standing-assumptions block cites `conj:FM-convergence` as `Theorem~\ref{conj:FM-convergence}` even though the source object is a conjecture. FIX: change the sentence to “Configuration space integrals are assumed to converge absolutely on FM compactifications; see Conjecture~\ref{conj:FM-convergence}.”

- [MEDIUM] chapters/theory/introduction.tex:340 — PROBLEM: the unnumbered “boundary-bulk reconstruction thesis” paragraph duplicates the formal conjecture at lines 768–868, so the introduction states the same thesis twice with different granularity. FIX: delete the paragraph body at lines 340–349 and replace it with a one-sentence forward reference to `Conjecture~\ref{conj:boundary-bulk-thesis}`.

- [MEDIUM] chapters/theory/introduction.tex:368 — PROBLEM: lines 368–390 enumerate the five facets of `\Theta_\cA`, then lines 718–765 do the same again in `Principle~\ref{princ:five-facets}`. FIX: keep the formal principle and compress lines 368–390 to a bridge sentence plus the unique shadow-degree data.

- [LOW] chapters/theory/introduction.tex:2164 — PROBLEM: “Each chapter builds on the previous one; the five theorems emerge as milestones.” is table-of-contents boilerplate, not a forced transition. FIX: replace it with a dependency sentence, e.g. “Because every later result constructs, projects, or tests \(\Theta_\cA\), the volume proceeds from the bar complex that defines it to the examples and bridges that constrain it.”

- [LOW] chapters/theory/introduction.tex:2565 — PROBLEM: the regime-tag convention uses bare `\kappa` in a global statement, with no algebra fixed. FIX: write `\kappa(\cA)` or `\kappa_\cA` in the curved-central bullet: `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`.

- [LOW] chapters/theory/introduction.tex:1661 — PROBLEM: `\omega_3(z)` appears without local definition and reuses a symbol already used elsewhere in the repo for an unrelated 3-form. FIX: replace the example with the explicit Virasoro singular part `r(z)=\frac{c/2}{z^3}+\frac{2T}{z}`.

- [LOW] chapters/theory/introduction.tex:927 — PROBLEM: the sentence is broken: “the OPE Thus \(r(z)\)…” is missing punctuation. FIX: insert a period or semicolon after “OPE”.

- [LOW] chapters/theory/introduction.tex:2153 — PROBLEM: the lattice and Yangian rows use `---` as placeholders, which this repo forbids. FIX: replace each `---` with `\text{n/a}` or leave the cells blank.

- [LOW] chapters/theory/introduction.tex:128 — PROBLEM: the file carries substantial unused-label debt. `rg` finds no live refs to anchors including `eq:intro-visibility` (128), `sec:NAP-unifying` (332), `sec:main-results-complete` (333), `subsec:five-theorems-heisenberg` (410), `subsec:five-theorems-general` (511), `sec:e1-as-primitive` (1184), `sec:architecture` (1766), `sec:traverse` (2161), `subsec:traverse-part-I`–`IV` (2165–2168), `subsec:numbered-traverse` (2258), `SA:ground-field`–`SA:completion` (2584–2595), and `subsec:critical-pitfalls` (2639). FIX: delete unused `\label{...}` commands; reintroduce an anchor only when a real reference exists.

## Summary
Checked: 2684 | Findings: 15 | Verdict: FAIL


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
session id: 019d83f0-3bb5-75c0-a45f-5b33e6a2602a
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/theory/introduction.tex

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
**Considering user requests**

The user specifically wants a cosmetic audit of one file, not a mathematical edit. I think I need to read the relevant sections for AP29/AP121 since those were mentioned. It’s important that my findings are grounded in the actual contents of the file. While knowing the banned vocabulary would be helpful, the user has already provided that list. I should focus on reading the entire target file to ensure I'm thorough.
codex
Using `deep-beilinson-audit` for this pass because the request is an adversarial audit of a manuscript surface. First step is to read the full target file and the minimal repo guidance needed to apply the named anti-patterns exactly, then I’ll enumerate only grounded findings with line numbers and concrete rewrites.
exec
/bin/zsh -lc 'wc -l chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP29|AP121|AP106|AP109" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
170:### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits
352:- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
519:**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.
550:AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
552:AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
790:AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
 succeeded in 77ms:
    2684 chapters/theory/introduction.tex
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



thinking
**Assessing file processing**

I’m thinking about how to effectively audit an entire file by reading manageable chunks. First, I could use tools like `rg` or `sed` to search for specific patterns quickly. I'll likely read the file in chunks of around 300 lines, maybe using `nl -ba` to include line numbers for clarity. It seems like I should process the file in about ten chunks given its size, potentially executing commands in parallel to be more efficient. I'll need to figure out how to save outputs and inspect them, too.
thinking
**Refining inspection methods**

I feel like I need to inspect the files carefully. It might be easier to use an explorer subagent, although that’s not allowed. Instead, I could utilize `exec_command` with `rg -n` to narrow down findings while using `sed` to read everything. Since the files are quite large, I might want to use a chunked approach with `nl -ba` for clearer output, or even consider `split` for better analysis. For now, I'll focus on reading only the necessary files.
codex
I’ve locked the audit surface to [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex). Next I’m reading the entire file in numbered chunks and scanning the repo guidance that defines the specific anti-patterns you named, so the findings stay tied to exact lines rather than broad impressions.
exec
/bin/zsh -lc "nl -ba CLAUDE.md | sed -n '784,796p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba CLAUDE.md | sed -n '540,560p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   540	
   541	**operadic** (AP65, AP81, AP82, AP83, AP84, AP85, AP88, AP103, AP104): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebra structures: Lie^c (Harrison, coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered configs); R-matrix descent relates. B_{Com}(A) is coLie, NOT cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.
   542	
   543	**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
   544	
   545	**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
   546	
   547	### BEFORE WRITING PROSE
   548	
   549	AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
   550	AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
   551	AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
   552	AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
   553	AP111: No "What this chapter proves" blocks. Restructure instead.
   554	AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
   555	**Prose laws**: (1) No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (2) No hedging where math is clear. (3) No em dashes; use colons, semicolons, or separate sentences. (4) No passive voice hedging. (5) Every paragraph forces the next. (6) State once, prove once. (7) Scope always explicit. (8) Comparison with prior work: one sentence per paper.
   556	
   557	### AFTER EVERY EDIT
   558	
   559	AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
 succeeded in 52ms:
   784	### Empirical (AP116-AP123, from 150-commit error archaeology)
   785	AP116: Summation boundary verification. After writing sum_{j=a}^{b}, substitute smallest index. H_N=sum_{j=1}^{N}, NOT N-1. Off-by-one is the #1 formula error that passes visual inspection.
   786	AP117: Differential form type. Connection is r(z)dz, NOT r(z) d log(z). KZ=sum r_{ij} dz_{ij}. Arnold d log(z_i-z_j) is bar coefficient, not connection. NEVER write d log without verification.
   787	AP118: Genus-1 scalar collapse. Formula at g=1 where matrix=(Im Omega)^{-1} becomes scalar 1/Im(tau) MUST be written in full matrix form. Verify at g=2 with 2x2 period matrix.
   788	AP119: Convergent vs divergent series. Before applying Borel summation: verify series is Gevrey-1 (factorial divergence). If |F_{g+1}/F_g| approaches constant (not growing like 2g), series is Gevrey-0. Use direct Pade, NOT Borel.
   789	AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
   790	AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
   791	AP122: Test tolerance proportional to magnitude. For Q~10^17, absolute tol 1e-4 is meaningless. Use relative: abs(computed-expected)/abs(expected) < rtol. Always verify tolerance achievable at float precision.
   792	AP123: Combinatorial enumeration completeness. Verify count against known formula or generating function BEFORE hardcoding. Genus-2 stable graphs: 7 (not 6). Hand enumeration without cross-check = future AP10 violation.
   793	
   794	### Deep Empirical (AP124-AP128, from 300-commit deep archaeology)
   795	AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
   796	AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	\chapter{Concordance with primary literature}
     2	\label{chap:concordance}
     3	
     4	\index{concordance|textbf}
     5	
     6	This chapter is the constitution of the monograph. When chapters
     7	disagree, this chapter governs. It records the five main theorems
     8	with their precise status and locates every result against the
     9	prior literature: what is proved, what is conditional, what
    10	remains conjectural.
    11	
    12	The governing principle is falsification: every claim in these three
    13	volumes is presumed false until it appears below with an explicit
    14	status tag and a proof reference or independent verification trail.
    15	A theorem that contradicts the concordance is not a theorem; it is an
    16	error in the chapter that states it. Omission from this chapter is
    17	itself a verdict: what is not recorded here has not survived scrutiny.
    18	The concordance does not summarize the monograph; the monograph
    19	approximates the concordance.
    20	
 succeeded in 52ms:
     1	# Red-Team Summary of Vol1/Vol2 Claim Audit
     2	## Scope
     3	- Formal tagged claims catalogued: **4866**
     4	- Volume I formal claims: **2841**
     5	- Volume II formal claims: **2025**
     6	- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
     7	- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.
     8	
     9	## Status profile
    10	- ProvedHere: **3801**
    11	- Conjectured: **327**
    12	- Heuristic: **35**
    13	- ProvedElsewhere: **513**
    14	- Conditional: **116**
    15	- Open: **74**
    16	
    17	## Risk profile
    18	- medium: **1999**
    19	- low: **1913**
    20	- high: **807**
 succeeded in 52ms:
Total output lines: 220

     1	# Theorem Registry
     2	
     3	Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.
     4	
     5	This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
     6	
     7	## Snapshot
     8	
     9	| Metric | Value |
    10	|---|---:|
    11	| ProvedHere claims | 2809 |
    12	| Total tagged claims | 3615 |
    13	| Active files in `main.tex` | 85 |
    14	| Total `.tex` files scanned | 128 |
    15	
    16	## Status Totals
    17	
    18	| Status | Count |

thinking
**Planning file reading strategy**

I need to read the entire target file, which has 2,684 lines. To manage this efficiently, I could use `rg` first to find specific patterns, but since the user wants me to read it all, I should. I’m thinking about processing it in chunks of 300 lines, parallelizing three chunks at a time. This might help handle output size since each chunk could generate around 5,000 tokens. Using commands like `nl -ba` with targeted `rg` queries will be useful for identifying patterns too.
codex
I’ve loaded the local audit constitution and the anti-pattern definitions. Now I’m walking the introduction itself in full and, in parallel, extracting the exact pattern hits for the mechanical failures so the final list is line-accurate instead of impressionistic.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '301,600p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1,300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|We now turn to|we now turn to|In this chapter we|it can be shown|one might expect|it seems reasonable|TODO|FIXME|XXX|---|—|`|'"\\*\\*|_[A-Za-z]\" chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '601,900p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   301	FG~\cite{FG12}
   302	 & \checkmark & \checkmark\textsuperscript{*} & & & \\
   303	CG~\cite{CG17}
   304	 & & & & & \\
   305	GLZ~\cite{GLZ22}
   306	 & \checkmark\textsuperscript{*} & & & & \\
   307	MS~\cite{MS24}
   308	 & & & & & \\
   309	\textbf{This work}
   310	 & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
   311	\bottomrule
   312	\end{tabular}
   313	\end{center}
   314	
   315	\noindent
   316	{\footnotesize ${}^*$FG: inversion at genus~$0$ for Lie-type bar
   317	complexes. GLZ: adjunction at genus~$0$, degree~$2$ only.}
   318	
   319	\smallskip\noindent
   320	No existing framework proves all five.
 exited 1 in 52ms:
zsh:1: unmatched "
 succeeded in 52ms:
     1	\chapter{Introduction}
     2	
     3	\section{From a point to a curve}
     4	\label{sec:volume-one-route}
     5	
     6	Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic $\kappa(\cA) = \mathrm{av}(r_\cA(z))$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.
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
 succeeded in 53ms:
   601	 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA).
   602	 \end{equation}
   603	 The anomaly of one algebra is the ghost-number violation of
   604	 its dual.
   605	
   606	 The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.
   607	
   608	\item \emph{Theorem~D$_{\mathrm{scal}}$} (Scalar modular
   609	 characteristic, Theorem~\ref{thm:modular-characteristic}).
   610	 A single scalar $\kappa(\cA)$, the genus-$1$ curvature
   611	 coefficient (Theorem~\ref{thm:genus-universality}), determines the
   612	 entire \emph{scalar modular package}: the collection
   613	 $(\kappa, \{\mathrm{obs}_g\}_{g \ge 1},
   614	 \{F_g\}_{g \ge 1})$ consisting of the modular
   615	 characteristic, its genus-$g$ obstruction classes, and the
   616	 free energies. For algebras whose strong generators have the
   617	 same conformal weight (including all single-generator families),
   618	 $\mathrm{obs}_g = \kappa \cdot \lambda_g
   619	 \in H^*(\overline{\cM}_g)$ and
   620	 $F_g = \kappa \cdot \hat{A}_g$ at all genera.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '901,1200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|We now turn to|we now turn to|In this chapter we|it can be shown|one might expect|it seems reasonable|TODO|FIXME|XXX|---|—|"'`|'"\\*\\*|_[A-Za-z]' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1201,1500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1501,1800p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   901	 are the KZ associator, the quartic $R$-matrix identity, and so on
   902	 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}};
   903	 equation~\textup{\eqref{eq:intro-theta-e1}}\textup{)}. The full tower
   904	 $(r(z), r_3, r_4, \ldots)$ is one object read at ascending degree.
   905	
   906	\item \emph{Leading-order modular shadow.}
   907	 The $\Sigma_2$-coinvariant projection
   908	 $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
   909	 characteristic, the first entry of the shadow obstruction tower
   910	 \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
   911	 Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
   912	 a matrix-valued refinement; averaging produces the scalar.
   913	
   914	\item \emph{Collision kernel of the bar differential.}
   915	 The bar differential $d_{\bar{B}}$ at degree~$2$ is the residue of
   916	 $r(z)$ at the collision divisor: given sections $a, b$ of $\cA$,
   917	 the binary component of $d_{\bar{B}}(a \otimes b)$ extracts
   918	 $\Res_{z=0}\bigl[r(z)(a \otimes b)\bigr]$ along the
   919	 diagonal in $\overline{C}_2(X)$
   920	 \textup{(}Chapter~\textup{\ref{chap:bar-cobar}};
 succeeded in 51ms:
6:Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic $\kappa(\cA) = \mathrm{av}(r_\cA(z))$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.
10:compactifications $\FM_n(X)$ with their boundary strata); the
20:The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
22:To state what changes, recall the classical theory. Let $V$ be a finite-dimensional graded vector space, $R \subset V^{\otimes 2}$ a subspace of quadratic relations, and $A = T(V)/(R)$ the quadratic algebra. The bar construction $B(A) = (T^c(s^{-1}\bar{A}), d_B)$ is the cofree conilpotent coalgebra on the desuspended augmentation ideal, with differential recording the splitting of elements into pairs of generators: $d_B(s^{-1}a) = \sum s^{-1}a' \otimes s^{-1}a''$. The cobar construction $\Omega(C)$ reverses the process. The comparison map
26:is always a dg algebra morphism. When it is a quasi-isomorphism, $A$ is \emph{Koszul}: the bar cohomology concentrates in degree~$1$, the Koszul dual coalgebra is $A^{\scriptstyle \text{\normalfont !`}} = H^1(B(A))$, and the Koszul dual algebra is $A^! = (A^{\scriptstyle \text{\normalfont !`}})^\vee = T(V^*)/R^\perp$. The derived categories of $A$-modules and $A^!$-modules become equivalent (Priddy~\cite{Priddy70}, Beilinson--Ginzburg--Soergel~\cite{BGS96}, Loday--Vallette~\cite{LV12}). The theory is complete: $\Omega(B(A)) \simeq A$ is bar-cobar \emph{inversion}, and nothing beyond this equivalence remains.
28:Over a curve, the theory does not terminate; the question is what replaces it. Let $X$ be a smooth projective curve over~$\mathbb{C}$. A \emph{chiral algebra}~$\cA$ on~$X$ (Beilinson--Drinfeld~\cite{BD04}) is a $\mathcal{D}_X$-module equipped with a chiral bracket
32:where $j \colon X^2 \setminus \Delta \hookrightarrow X^2$ is the complement of the diagonal and $\Delta_! \colon D(\mathcal{D}_X) \to D(\mathcal{D}_{X^2})$ is the pushforward. In local coordinates the chiral bracket encodes the operator product expansion:
49:\omega_g$, matrix-valued in
50:$\operatorname{End}_\cA(2) \otimes H^{1,1}(\mathcal{C}_g)$.
52:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$, where
53:$\omega_g = c_1(\mathbb{E})$ is the Hodge class on
54:$\overline{\mathcal{M}}_g$ and
64:$\Sigma_n$-coinvariance, $\Theta_\cA$ projects to a pronilpotent
88:Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
93:$F_g = \kappa \cdot \lambda_g$ is exact at all genera
95:$\delta F_g^{\mathrm{cross}}$ vanishes identically
112:$H(t)^2 = t^4 Q_L(t)$,
113:where $Q_L$ is a quadratic polynomial in three invariants $(\kappa, \alpha, S_4)$. The
114:tower is the Taylor expansion of~$\sqrt{Q_L}$, algebraic of degree~$2$.
129:g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 succeeded in 52ms:
  1201	\begin{equation}\label{eq:intro-bar-ord}
  1202	\barB^{\mathrm{ord}}(\cA)
  1203	\;=\;
  1204	T^c(s^{-1}\bar\cA)
  1205	\;=\;
  1206	\bigoplus_{n \ge 0}\,(s^{-1}\bar\cA)^{\otimes n}
  1207	\end{equation}
  1208	with deconcatenation coproduct, which by Stasheff's theorem
  1209	\textup{\cite{Sta63}} is the universal cofree conilpotent
  1210	coalgebra on~$s^{-1}\bar\cA$. Every $A_\infty$-chiral algebra
  1211	admits a canonical ordered bar; the symmetric bar arises only
  1212	after applying $\Sigma_n$-coinvariants externally on each tensor
  1213	factor. The unsymmetrized object retains strictly more
  1214	information (\S\ref{subsec:e1-as-primitive}).
  1215	
  1216	\paragraph{The ordered convolution algebra and its MC element.}
  1217	The ordered convolution dg Lie algebra
  1218	\begin{equation}\label{eq:intro-gAmod-e1}
  1219	{\gAmod}^{\Eone}
  1220	\;:=\;
 succeeded in 50ms:
  1501	Chapter~\ref{chap:bar-cobar} onward present the av-images of the
  1502	ordered constructions.
  1503	
  1504	\begin{remark}[Scope of the $\Eone$ reframing]
  1505	\label{rem:e1-primacy-scope}
  1506	\index{primacy thesis!E1@$\Eone$!scope of reframing}
  1507	The proofs of Theorems~A--D and~H are unchanged.
  1508	The conceptual reordering is as follows: the modular convolution
  1509	algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
  1510	universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
  1511	and the modular characteristic $\kappa(\cA)$ as
  1512	$\operatorname{av}(r(z))$ at degree~$2$.
  1513	The ordered theory of
  1514	Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
  1515	the symmetric theory is its image.
  1516	
  1517	The $\Eone$ side is strictly richer: at degree~$2$ alone it
  1518	distinguishes algebras that the symmetric side identifies.
  1519	The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
  1520	$\widehat{\mathfrak{sl}}_2$-shadow

thinking
**Reviewing search patterns**

I'm noticing that the interesting output I received consists mostly of pattern hits due to many false positives, like underscores and such. I really need to refine the search to target slop more effectively. The output is substantial, but it doesn’t cover all the lines. It might help to manually review the patterns. Before that, I should read the remaining chunks, focusing on 1801-2100, 2101-2400, and 2401-2684. It's a bit of a process!
codex
I’ve now covered roughly two-thirds of the file and have the first pattern-derived failures in hand. The remaining pass is the last 900 lines plus focused re-checks for notation drift and dead surfaces, because the subtle issues are showing up in later summary tables and glossary material rather than in the chapter’s early prose.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1801,2100p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1801	 proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
  1802	 is compatible with clutching, trace, and Verdier duality.
  1803	\item \emph{Associative structure.}
  1804	 \index{ordered factorization|see{$\Eone$-chiral algebra}}
  1805	 The Yangian $Y(\mathfrak{g})$ is $\Eone$-chiral
  1806	 (Definition~\ref{def:e1-chiral}): its bar complex uses ordered
  1807	 configuration spaces, and Verdier duality acts by $R$-matrix
  1808	 inversion $R \mapsto R^{-1}$
  1809	 (Theorem~\ref{thm:yangian-koszul-dual}).
  1810	 The sign flip $\hbar \mapsto -\hbar$ replaces the Feigin--Frenkel
  1811	 involution.
  1812	\end{enumerate}
  1813	
  1814	\smallskip\noindent
  1815	In the Heisenberg algebra, only pieces~(i)--(iv) are active, and they
  1816	already force the full commutative/modular package: Arnold ensures
  1817	$d^2 = 0$; Verdier produces
  1818	$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$; the genus-$1$
  1819	period integral creates curvature $\kappa = k$; clutching assembles
  1820	the genus tower.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2401,2684p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|We now turn to|we now turn to|In this chapter we|it can be shown|one might expect|it seems reasonable|TODO|FIXME|XXX|---|—' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2101,2400p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2401	 M (mixed), $r_{\max} = \infty$: $\Theta_\cA$ has infinite shadow
  2402	 tower.
  2403	
  2404	\item \emph{Chiral deformation quantization}
  2405	 (Ch.~\ref{ch:chiral-deformation}).
  2406	 Chiral Kontsevich formality; $\Pinf \to \Einf$ passage; star
  2407	 products as MC deformations of $\Theta_\cA$. Bridges the
  2408	 Poisson side to the bar-complex side.
  2409	
  2410	\item \emph{Yangians} (Ch.~\ref{chap:yangians}).
  2411	 $\Eone$-chiral bar on ordered configurations; $R$-matrix inversion
  2412	 as Koszul duality; the DK bridge. The only tier-(c) family of
  2413	 Definition~\ref{def:three-tier-r-matrix}, with $\Theta_\cA^{\Eone}$
  2414	 independent of any $\Einf$ shadow.
  2415	
  2416	\item \emph{Genus expansions} (Ch.~\ref{ch:genus-expansions}).
  2417	 Explicit expansions: modular forms, Eisenstein, Mumford, bosonization.
  2418	 Verifies Theorem~D scalar saturation family-by-family.
  2419	
  2420	\item \emph{Detailed computations + combinatorial frontier}
 succeeded in 54ms:
2153:$V_\Lambda$ (lattice) & $\mathrm{rk}(\Lambda)$ & $\mathrm{rk}(\Lambda)$ & $2\mathrm{rk}$ & --- & braided \\[2pt]
2154:$Y(\mathfrak{sl}_2)$ & --- & --- & --- & --- & $\Eone$, $R$-matrix
 succeeded in 52ms:
  2101	
  2102	\noindent\textbf{MC5} (Genus tower / BV-BRST comparison): the algebraic
  2103	genus recursion and the analytic sewing package are \textbf{proved},
  2104	but the full genuswise BV/BRST/bar identification remains open. The
  2105	algebraic bar differential at genus~$g$ is determined inductively from
  2106	lower genera (Theorem~\ref{thm:inductive-genus-determination}). Graph
  2107	amplitudes on~$\Sigma_g$ converge without UV renormalization in
  2108	dimension~$2$ (Proposition~\ref{prop:2d-convergence}). The analytic
  2109	and algebraic differentials agree on the algebraic core
  2110	(Theorem~\ref{thm:analytic-algebraic-comparison}). HS-sewing holds
  2111	for the standard landscape (Theorem~\ref{thm:general-hs-sewing}):
  2112	polynomial OPE growth and subexponential sector growth imply
  2113	convergent mode sums for all~$0 < q < 1$. For the Heisenberg algebra,
  2114	the genus-$g$ partition function is the Fredholm determinant of the
  2115	one-particle Bergman sewing operator
  2116	\textup{(}Theorem~\ref{thm:heisenberg-one-particle-sewing}\textup{)}.
  2117	At genus~$0$, the algebraic BRST/bar comparison is proved, while the
  2118	top-degree amplitude pairing is only conditional
  2119	\textup{(}Theorem~\ref{thm:algebraic-string-dictionary},
  2120	Corollary~\ref{cor:string-amplitude-genus0}\textup{)}.








thinking
**Inspecting file contents**

I need to check the exact file contents we've read, considering the user's requirement to ground every claim in them. For unused labels, reading grep results might suffice, but "file contents" could also include grep output across the entire repository. We'll search each stub label using a command. There are 15 labels to consider, and we should also identify any commented-out sections over 10 lines — though it seems there aren't any. We need to determine if these stub labels are unused or necessary, as referenced labels aren't dead code but may have aesthetic implications.
thinking
**Searching for dead code**

The user asked about dead code, and it seems that what's considered "dead" may not actually be if it's still in use. However, there could be some cosmetic issues to address. I need to search for specific vocabulary using the command for exact matches in the file. I'll look for terms like "moreover," "additionally," and others. It's important to refine this search to determine the presence of such vocabulary, but maybe it's not necessary.
thinking
**Auditing transitions and references**

I need to check the references from lines 2165 to 2168; they could be placeholders or inactive. There are also sections marked as "phantom." It seems I should audit their transition quality, asking myself if each section effectively leads into the next. For instance, I need to search for "The selection principle determines" to find instances of generic signposting. The chapter opening also indicates a deficiency, beginning with "Koszul duality over a point terminates..."
thinking
**Assessing curve theory and file auditing**

I'm looking at the curve theory and wondering if there are any definitive findings. It might be fine to not mention certain things for clarity. I should check typography for issues like double spaces and indentation, perhaps using commands like `rg -n ' +'`. There might be time for brace mismatches, but since the user only asks for one file audit rather than a full build, tools like `latexmk` or `chktex` may not be necessary. I'll keep it simple!
thinking
**Identifying undefined macros**

I need to find undefined macros in the file, and I'm considering using a command like `rg -n '\\[A-Za-z@]+' chapters/theory/introduction.tex | sort | uniq`, but that might be too complicated. It might be better to run `latexmk`, although that could be resource-intensive. Instead, I could specifically target macros with something like `rg -n '\\SCchtop|\\CompCl|\\Fft|\\Convstr|\\Definfmod|\\barBgeom'` to streamline the process. A focused approach will likely yield better results!
thinking
**Detecting issues in code**

I need to focus on finding actual issues, rather than hidden labels or stubs. It seems like a search for `TODO|FIXME|XXX` might not yield anything significant from previous checks. I'll also look for sections that start with phrases like "In this section/chapter we" and check for "We now turn to." 

Potential findings include: em dashes in the master table using ASCII placeholders, a section with possible dead code, and duplicate labels that might be intentional. I should only report what’s truly unresolved.
thinking
**Evaluating facets enumeration**

It looks like I'm dealing with almost the same enumeration of five facets. I might need to flag any duplicate theorem or proposition statements. For instance, the "five facets of r(z)" proposition, which spans lines 870-937 and has remarks from lines 939-968, might be appropriate as it is, but I’ll want to double-check for any needed adjustments or overlaps. It's essential to keep things clear and concise!
thinking
**Considering the audit process**

I think we need an audit, and it might be easiest to use a command like `rg -o '\\[A-Za-z@]+' chapters/theory/introduction.tex | sort -u` to find unique identifiers. Then, I could run `rg` again to check for definitions of less obvious macros. There seem to be too many macros to sift through. I wonder if we might utilize LaTeX's undefined control sequence detection, but compiling just this file may not be possible.
codex
The last pass is now on cross-reference scaffolding and notation hygiene. I’m checking whether the introduction is carrying dead alias labels and placeholder rows, because those are the highest-probability “cosmetic but structurally harmful” surfaces after the prose itself.
exec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z])'"\\\\kappa(?"'!'"\\s*\\()' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Omega/z' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
14:characteristic~$\kappa$, the shadow obstruction tower, the
80:$\Delta = 8\kappa S_4$ forces $r_{\max}$ to lie in
93:$F_g = \kappa \cdot \lambda_g$ is exact at all genera
113:where $Q_L$ is a quadratic polynomial in three invariants $(\kappa, \alpha, S_4)$. The
132:Genus~$1$ sees only~$\kappa$ (degree~$2$).
359:Theorem~D identifies $\kappa$
388:$\kappa$ at degree~$2$, the cubic shadow~$C$ at
613: $(\kappa, \{\mathrm{obs}_g\}_{g \ge 1},
618: $\mathrm{obs}_g = \kappa \cdot \lambda_g
620: $F_g = \kappa \cdot \hat{A}_g$ at all genera.
626: all-genera identities $\mathrm{obs}_g = \kappa \cdot \lambda_g$
627: and $F_g = \kappa \cdot \hat{A}_g$, hold on the uniform-weight
634: The scalar $\kappa$ is universal,
636: ($\kappa + \kappa' = 0$ for affine Kac--Moody and free
654: $\kappa$ is the one-loop coefficient of the effective action;
773:\index{holographic central charge|see{$\kappa$}}%
774:\index{$\kappa$!as holographic central charge}%
1114:denominator $k + h^\vee$ in~$\kappa$ vanishes, the vacuum stress
1190:\index{R-matrix!as primitive of $\kappa$}
1292:\kappa\bigl(V_k(\mathfrak{g})\bigr)
 succeeded in 52ms:
1105:\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
1296:where $r_k(z) = k\,\Omega/z$ is the level-$k$ classical $r$-matrix
1442:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
1445:discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
1519:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
1658:the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
1659:$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
exec
/bin/zsh -lc "rg -n 'def:modular-homotopy-theory-intro|eq:all-degree-master-eq-intro|eq:arnold-seed|eq:bar-graded-object-intro|eq:the-seed|eq:universal-MC|prop:modular-homotopy-classification|prop:shadow-massey-identification|rem:categorical-logarithm-paradigm|sec:flat-connection-intro|sec:modular-char-spectral-disc-intro|sec:primitive-kernel-intro|sec:the-seed|subsec:shadow-postnikov-tower-intro|thm:modular-koszul-duality-main' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'subsec:traverse-part-I|subsec:traverse-part-II|subsec:traverse-part-III|subsec:traverse-part-IV|conv:proof-architecture' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(newcommand|def|DeclareMathOperator|DeclareRobustCommand|providecommand|ProvideDocumentCommand)\\{?\\\\(SCchtop|barBgeom|CompCl|Fft|Convstr|Definfmod)' ." in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
./wave2_audit_20260413_001942/S07_preface_to_intro.md:305:    12	\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/survey_v2_xr.tex:97:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/survey_v2_xr.tex:99:\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/survey_v2_xr.tex:148:\providecommand{\CompCl}{\mathrm{CompCl}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:95:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:97:\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:146:\providecommand{\CompCl}{\mathrm{CompCl}}
./tmp_standalone_audit/wrap_survey_track_b_compressed.tex:95:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/wrap_survey_track_b_compressed.tex:97:\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/wrap_survey_track_b_compressed.tex:146:\providecommand{\CompCl}{\mathrm{CompCl}}
./tmp_standalone_audit/wrap_survey_track_b_fixed.tex:95:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/wrap_survey_track_b_fixed.tex:97:\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/wrap_survey_track_b_fixed.tex:146:\providecommand{\CompCl}{\mathrm{CompCl}}
./tmp_standalone_audit/wrap_survey_track_a_compressed.tex:95:\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
./tmp_standalone_audit/wrap_survey_track_a_compressed.tex:97:\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
./tmp_standalone_audit/wrap_survey_track_a_compressed.tex:146:\providecommand{\CompCl}{\mathrm{CompCl}}
./chapters/connections/thqg_symplectic_polarization.tex:7:\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
./chapters/connections/thqg_modular_bootstrap.tex:24:\providecommand{\Definfmod}{\operatorname{Def}_{\infty}^{\mathrm{mod}}}
./chapters/connections/thqg_modular_bootstrap.tex:25:\providecommand{\Convstr}{\operatorname{Conv}_{\mathrm{str}}}
./chapters/connections/thqg_soft_graviton_theorems.tex:38:\providecommand{\Convstr}{\operatorname{Conv}_{\mathrm{str}}}
 succeeded in 55ms:
Total output lines: 206

./wave2_audit_20260413_001942/S13_concordance_to_body.md:109:chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:275:/bin/zsh -lc "rg -n \"thm:genus-universality|thm:quantum-complementarity-main|thm:modular-koszul-duality-main|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|Theorem~D|Theorem~C|Theorem~A|Theorem~B|Theorem~H|Vol I|Volume~I|Volume I\" /Users/raeez/calabi-yau-quantum-groups -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S07_preface_to_intro.md:225:/bin/zsh -lc "rg -n 'thm:modular-koszul-duality-main|thm:quantum-complementarity-main|thm:modular-characteristic|thm:genus-universality|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:riccati-algebraicity|prop:chirhoch1-affine-km|conj:v1-drinfeld-center-equals-bulk|thm:topologization|conj:topologization-general|warn:multiple-e1-chiral|princ:geometric-origin-hochschild|conv:three-hochschild' metadata/theorem_registry.md chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S07_preface_to_intro.md:754:    77	Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
./wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:1109:./wave2_audit_20260413_001942/S06_intro_to_body.md:341:/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./chapters/examples/heisenberg_eisenstein.tex:1952:\textup{(}\S\textup{\ref{sec:primitive-kernel-intro})}
./wave2_audit_20260413_001942/S06_intro_to_body.md:3:- [CRITICAL] chapters/theory/introduction.tex:2508 — PROBLEM: `\label{thm:modular-koszul-duality-main}` is only a `\phantomsection` stub, not a theorem environment or tagged claim. The concordance still cites it as “the flag theorem” at `chapters/connections/concordance.tex:77`, and body chapters cite nonexistent clause numbers at `chapters/theory/higher_genus_modular_koszul.tex:16686`, `21446`, `chapters/frame/heisenberg_frame.tex:4810`, and `chapters/connections/frontier_modular_holography_platonic.tex:4685`. FIX: either restore an actual theorem environment with numbered clauses and a claim-status tag at this anchor, or stop using the `thm:` label entirely: rename it to a non-theorem label and retarget every downstream citation to the concrete theorem labels that actually prove the cited claims.
./wave2_audit_20260413_001942/S06_intro_to_body.md:341:/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./wave2_audit_20260413_001942/S06_intro_to_body.md:673:chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
./wave2_audit_20260413_001942/S06_intro_to_body.md:706:  2494	\phantomsection\label{def:modular-homotopy-theory-intro}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:707:  2495	\phantomsection\label{eq:all-degree-master-eq-intro}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:708:  2496	\phantomsection\label{eq:arnold-seed}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:709:  2497	\phantomsection\label{eq:bar-graded-object-intro}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:710:  2498	\phantomsection\label{eq:the-seed}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:711:  2499	\phantomsection\label{eq:universal-MC}%
./wave2_audit_20260413_001942/S06_intro_to_body.md:757:I’m considering a specific fix for the inconsistencies found. I could suggest replacing “Theorem\ref{thm:modular-koszul-duality-main} (the flag theorem)” with “The Introduction's synthesis around Theorems A–D and H,” unless a proper theorem environment is set up. Well, I think I need to go for the minimal truthful fix by saying either restore the theorem environment with a precise statement and claim status, or delete the relevant language from the concordance. 
./wave2_audit_20260413_001942/S06_intro_to_body.md:815:    77	Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
./wave2_audit_20260413_001942/S06_intro_to_body.md:1186:Then there's Potential Finding 45: it might be necessary to check the theorem registry to see if `thm:modular-koszul-duality-main` is missing. I should perform a search for that.
 succeeded in 55ms:
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:665:chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:807:./chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:808:./standalone/introduction_full_survey.tex:5297:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F01_definitions_bar.md:543:standalone/introduction_full_survey.tex:5297:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F01_definitions_bar.md:546:./chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F04_definitions_complementarity.md:1064:conv:proof-architecture
./wave2_audit_20260413_001942/F11_hidden_imports_bar.md:1145:conv:regime-tags	chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F02_definitions_koszul.md:959:chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:431:chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./metadata/label_index.json:3694:  "conv:proof-architecture": {
./metadata/label_index.json:44058:  "subsec:traverse-part-I": {
./metadata/label_index.json:44062:  "subsec:traverse-part-II": {
./metadata/label_index.json:44066:  "subsec:traverse-part-III": {
./metadata/label_index.json:44070:  "subsec:traverse-part-IV": {
./audit_campaign_20260412_231034/T04_thm_C1.md:650:Convention~\ref{conv:proof-architecture}]
./standalone/introduction_full_survey.tex:4914:\label{subsec:traverse-part-I}%
./standalone/introduction_full_survey.tex:4915:\label{subsec:traverse-part-II}%
./standalone/introduction_full_survey.tex:4916:\label{subsec:traverse-part-III}%
./standalone/introduction_full_survey.tex:4917:\label{subsec:traverse-part-IV}%
./standalone/introduction_full_survey.tex:5297:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}

thinking
**Clarifying search strategy**

I’m realizing that the repository’s search results are muddied by audit artifacts. It might be best to restrict my search to specific files like `chapters`, `appendices`, and `metadata`, or even exclude the audit directories altogether. There’s also talk of grounding claims in the actual file contents read. I need to do a targeted search focusing only on the relevant sections. I might use commands to check for references as well, especially those related to specific labels. Let’s run that!
exec
/bin/zsh -lc "rg -nP '\\\\(it can be shown|one might expect|it seems reasonable|In this chapter we|We now turn to|we now turn to)\\b' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|nameref)\\{(def:modular-homotopy-theory-intro|eq:all-degree-master-eq-intro|eq:arnold-seed|eq:bar-graded-object-intro|eq:the-seed|eq:universal-MC|prop:modular-homotopy-classification|prop:shadow-massey-identification|rem:categorical-logarithm-paradigm|sec:flat-connection-intro|sec:modular-char-spectral-disc-intro|sec:primitive-kernel-intro|sec:the-seed|subsec:shadow-postnikov-tower-intro|thm:modular-koszul-duality-main)\\}' chapters appendices standalone metadata main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|nameref)\\{(subsec:traverse-part-I|subsec:traverse-part-II|subsec:traverse-part-III|subsec:traverse-part-IV)\\}' chapters appendices standalone metadata main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -in '\\b(moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone)\\b|it is worth noting' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:modular-koszul-duality-main' chapters appendices standalone metadata main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 57ms:

 exited 1 in 51ms:

 succeeded in 51ms:
standalone/introduction_full_survey.tex:279:The Arnold relation~\eqref{eq:arnold-seed} makes the triple
standalone/introduction_full_survey.tex:331:that vanishes if and only if the Arnold relation~\eqref{eq:arnold-seed} kills the form factor and the Borcherds identity kills the algebraic factor.
standalone/introduction_full_survey.tex:785:The bar construction of \S\ref{sec:the-seed} is a
standalone/introduction_full_survey.tex:1551: $\Theta_\cA$~\eqref{eq:universal-MC}.
standalone/introduction_full_survey.tex:3254:\item The transferred $A_\infty$ and $L_\infty$ structures on bar cohomology (homotopy transfer theorem, Chapter~\ref{app:homotopy-transfer}) yield the shadow obstructions: at genus~$0$, $o_{r+1}|_{g=0} = [m_{r+1}]$ (Proposition~\ref{prop:shadow-massey-identification}). Formality ($m_n = 0$ for $n \ge 3$) is the Gaussian archetype.
standalone/introduction_full_survey.tex:3565:(Proposition~\ref{prop:shadow-massey-identification}).
standalone/introduction_full_survey.tex:3627:The identification of Proposition~\ref{prop:shadow-massey-identification}
standalone/introduction_full_survey.tex:3630:Definition~\ref{def:modular-homotopy-theory-intro}:
standalone/introduction_full_survey.tex:3644: && shadow obstructions $o_{r+1}$ (Prop.~\ref{prop:shadow-massey-identification}) \\[2pt]
standalone/introduction_full_survey.tex:4581: The Arnold relation~\eqref{eq:arnold-seed} is factorization
chapters/examples/yangians_drinfeld_kohno.tex:86: homotopy theory (Definition~\ref{def:modular-homotopy-theory-intro}).
chapters/examples/yangians_foundations.tex:1477: by \eqref{eq:the-seed}), and the remaining local transport problem is
chapters/examples/heisenberg_eisenstein.tex:1952:\textup{(}\S\textup{\ref{sec:primitive-kernel-intro})}
standalone/survey_modular_koszul_duality.tex:950:see \S\textup{\ref{sec:modular-char-spectral-disc-intro}}\textup{)}. Grothendieck--Riemann--Roch
chapters/theory/higher_genus_complementarity.tex:4197:equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
chapters/frame/heisenberg_frame.tex:4811:Theorem~\ref{thm:modular-koszul-duality-main},
chapters/connections/thqg_preface_supplement.tex:2032: & \S\ref{subsec:shadow-postnikov-tower-intro}
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3749:Theorem~\ref{thm:modular-koszul-duality-main},
chapters/theory/higher_genus_modular_koszul.tex:16523:\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
chapters/theory/higher_genus_modular_koszul.tex:16686:By Theorem~\ref{thm:modular-koszul-duality-main}(iv),
 succeeded in 52ms:
metadata/label_index.json:48282:  "thm:modular-koszul-duality-main": {
metadata/claims.jsonl:2939:{"label": "thm:shadow-archetype-classification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16007, "title": "Shadow archetype classification", "refs_in_block": ["def:shadow-depth-classification", "cor:nms-betagamma-mu-vanishing", "thm:w-virasoro-quintic-forced", "prop:propagator-variance", "thm:modular-koszul-duality-main", "fig:shadow-archetype-classification", "thm:shadow-spectral-correspondence", "sec:higher-depths", "prop:free-interacting-dichotomy"]}
metadata/claims.jsonl:2973:{"label": "thm:shadow-tautological-ring", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 20460, "title": "Shadow classes in the tautological ring", "refs_in_block": ["thm:modular-koszul-duality-main", "prop:independent-sum-factorization"]}
standalone/introduction_full_survey.tex:1881:\label{thm:modular-koszul-duality-main}
chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
chapters/connections/frontier_modular_holography_platonic.tex:4685:(Theorem~\ref{thm:modular-koszul-duality-main})
chapters/frame/heisenberg_frame.tex:4811:Theorem~\ref{thm:modular-koszul-duality-main},
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3749:Theorem~\ref{thm:modular-koszul-duality-main},
chapters/theory/introduction.tex.bak:1817:\phantomsection\label{thm:modular-koszul-duality-main}%
chapters/theory/higher_genus_modular_koszul.tex:16523:\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
chapters/theory/higher_genus_modular_koszul.tex:16686:By Theorem~\ref{thm:modular-koszul-duality-main}(iv),
chapters/theory/higher_genus_modular_koszul.tex:16896:Theorem~\ref{thm:modular-koszul-duality-main}(ii)).
chapters/theory/higher_genus_modular_koszul.tex:21416: Theorem~\textup{\ref{thm:modular-koszul-duality-main}}\textup{(iv)}.
chapters/theory/higher_genus_modular_koszul.tex:21446:Theorem~\ref{thm:modular-koszul-duality-main}(iv):
chapters/theory/introduction.tex:2508:\phantomsection\label{thm:modular-koszul-duality-main}%
 exited 1 in 52ms:





thinking
**Evaluating section updates**

I'm considering how to address the phantom section at 2508. One option is to replace it with a theorem environment that summarizes A/B/C/D/H and includes specific parts (i)-(v). Alternatively, if restating isn’t feasible, I could rename it to `princ:intro-synthesis` and update the references at the specified file lines. However, it seems crucial that the precise fix should be straightforward; I just need to figure out the best approach.
thinking
**Deciding on the theorem fix**

I’m editing and need a precise fix for a theorem issue. Concordance mentions "flag theorem" while other documents reference clauses. A minimal truthful fix could be to restore the actual theorem environment, but that’s a significant change. Alternatively, updating all downstream citations to reflect concrete theorems is another route, yet the user is asking for an exact fix. The safest approach is to delete the misleading label and map specific references. An exact fix for the intro file could be replacing a label with a real theorem environment that outlines the introduction's synthesis.
thinking
**Clarifying the theorem structure**

I'm considering whether I should quote the exact theorem skeleton. I can propose parts like (i) bar-cobar adjunction, (ii) inversion on the Koszul locus, (iii) complementarity, (iv) modular characteristic, and (v) chiral Hochschild. However, since theorem H is the fifth, I should specify that. The introduction summarizes everything, and it should reflect the theorem correctly. 

To do this, I think I need to create a proper theorem environment using `maintheorem` with claim status and provide a concise example of the fix. It's important to keep it clear and direct, especially for the final document.
thinking
**Checking phantomsection labels**

I need to explore whether other phantomsection stub labels relate to the definition or proposition labels. It’s possible that some are also being utilized in the context of theorems or definitions. I guess reviewing these labels could help clarify their usage, ensuring consistency throughout. This might streamline the structure and enhance clarity for readers. Let’s dig deeper into this to confirm if they correspond correctly to their intended definitions.
codex
The strongest non-cosmetic defect is now confirmed: the introduction contains phantomsection anchors with `thm:`, `def:`, `prop:` and `eq:` prefixes, and the rest of the manuscript cites them as if they were real theorem-like objects. I’m reading the original standalone survey versions of those anchors now so the fixes can name the exact restoration target instead of hand-waving.
exec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '1860,1915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '3610,3655p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '3238,3275p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '1538,1560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '250,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1860	(i)~the Pixton ideal of the modular curve from the MC
  1861	tautological relations
  1862	(Theorem~\ref{thm:pixton-from-mc-semisimple}, proved for
  1863	semisimple shadow CohFTs; obstructed for non-semisimple by
  1864	Proposition~\ref{prop:non-semisimple-pixton-obstruction});
  1865	(ii)~a complete resolution of the BV/BRST identification for
  1866	free fields
  1867	(Theorem~\ref{thm:heisenberg-bv-bar-all-genera});
  1868	(iii)~the multi-weight genus tower through genus~$4$ with
  1869	explicit closed forms and a growth theorem
  1870	(Proposition~\ref{prop:cross-channel-growth});
  1871	(iv)~non-principal Koszul duality for the
  1872	Bershadsky--Polyakov algebra and nilpotent transport through
  1873	$\mathfrak{sl}_8$
  1874	(Computation~\ref{comp:bp-kappa-three-paths},
  1875	Proposition~\ref{prop:nilpotent-transport-typeA}).
  1876	
  1877	\subsection{The main theorem}
  1878	\label{subsec:main-theorem}
  1879	
 succeeded in 51ms:
  3610	deformation retract $(\barB(\cA), H^*(\barB(\cA)), i, p, h)$.
  3611	The genus-$0$ shadow obstructions $o_{r+1}|_{g=0}$ are the
  3612	obstructions to extending the truncated MC element
  3613	$\Theta_\cA^{\le r}|_{g=0}$ by one degree in the genus-$0$
  3614	sector of $\Defcyc(\cA)$. But the genus-$0$ sector of the
  3615	modular convolution algebra is the \emph{operadic} convolution
  3616	algebra $\mathrm{Hom}(\barB_{\mathrm{op}}(\mathrm{Com}),
  3617	\mathrm{End}_\cA)$, and the MC equation there is exactly the
  3618	$A_\infty$-structure equation. The identification~\eqref{eq:shadow-massey}
  3619	follows from the standard comparison between the operadic
  3620	bar-cobar obstruction tower and the $A_\infty$-Massey product
  3621	tower (cf.~\cite[Theorem~3.4.1]{LPWZ09}).
  3622	\end{proof}
  3623	
  3624	\begin{remark}[The Sullivan dictionary]
  3625	\label{rem:sullivan-dictionary}
  3626	\index{rational homotopy type!modular analogue}
  3627	The identification of Proposition~\ref{prop:shadow-massey-identification}
  3628	is the genus-$0$ case of a structural parallel between Sullivan's
  3629	rational homotopy theory and the modular homotopy theory of
 succeeded in 53ms:
  3238	\begin{theorem}[Rectification bridge]
  3239	\label{thm:rectification-bridge}
  3240	\ClaimStatusProvedElsewhere
  3241	\index{rectification!bridge theorem|textbf}
  3242	\index{formality!rectification bridge|textbf}
  3243	The three rectification principles are:
  3244	\begin{enumerate}[label=\textup{(\roman*)}]
  3245	\item \emph{Operadic}: the homotopy chiral algebra $\cA^{Ch_\infty}$ rectifies to a strict chiral algebra $\cA$ via bar-cobar (Theorem~\ref{thm:bar-cobar-inversion-qi}).
  3246	\item \emph{Convolution}: the $L_\infty$-algebra $\Convinf(\mathrm{FCom}, \operatorname{End}_{\barB(\cA)})$ and the dg Lie algebra $\Convstr(\barB(\cA), \cA)$ carry quasi-isomorphic MC moduli.
  3247	\item \emph{Reduction}: on the proved generic DS lanes, the derived DS functor $\mathbf{R}\mathrm{DS}_f$ and the classical functor $H^0_{Q_{\mathrm{DS}}}$ agree. This is established by Kazhdan filtration formality on the abelian-$\mathfrak{n}_+$ locus (Proposition~\ref{prop:ds-bar-formality}) and, in particular, in the principal case (Theorem~\ref{thm:ds-koszul-intertwine}).
  3248	\end{enumerate}
  3249	\end{theorem}
  3250	
  3251	Rectification, the passage from homotopy-coherent to strict structures, underlies all five main theorems:
  3252	\begin{enumerate}[label=\textup{(\alph*)}]
  3253	\item Bar-cobar preserves quasi-isomorphisms because it is a quantum $L_\infty$ functor: it respects the full homotopy package, not merely the strict dg structure. This gives Theorem~B.
  3254	\item The transferred $A_\infty$ and $L_\infty$ structures on bar cohomology (homotopy transfer theorem, Chapter~\ref{app:homotopy-transfer}) yield the shadow obstructions: at genus~$0$, $o_{r+1}|_{g=0} = [m_{r+1}]$ (Proposition~\ref{prop:shadow-massey-identification}). Formality ($m_n = 0$ for $n \ge 3$) is the Gaussian archetype.
  3255	\item On the proved generic DS lanes, Drinfeld--Sokolov reduction commutes with bar through the derived/classical comparison above: the principal case is unconditional, and additional non-principal cases require the verified DS--KD comparison hypotheses. In those regimes the universal MC class of the full current-plus-ghost system descends to that of the $\mathcal{W}$-algebra (Theorem~\ref{thm:ds-platonic-functor}, Corollary~\ref{cor:ds-theta-descent}); the bare affine tower alone does not capture the ghost-created quartic and higher shadows. The geometric content is the Slodowy-slice localization principle (Remark~\ref{rem:ds-geometric-localization-principle}): DS reduction is Hamiltonian reduction from $J_\infty(\fg^*)$ to $J_\infty(S_f)$ (the arc space of the Slodowy transverse slice), and the master commutative square (Theorem~\ref{thm:master-commutative-square}) encodes the compatibility of bar complexes with this geometric localization.
  3256	\item The dg Lie algebra is a faithful chart on the formal moduli problem $\cM^{\mathrm{mod}}_\cA$; every strict-model formula is a projection of $\Theta_\cA \in \MC(\Convinf)$. The space of models is contractible (Proposition~\ref{prop:model-independence}).
  3257	\end{enumerate}
 succeeded in 52ms:
  1538	 Verdier-geometric duality
  1539	 ($\mathrm{A}_2$,
  1540	 Theorem~\ref{thm:bar-cobar-isomorphism-main}).
  1541	 On the proved genus-$0$ locus, the bar complex admits a BRST
  1542	 comparison; Verdier duality is the algebraic shadow of CPT.
  1543	
  1544	\item \emph{Theorem~B} (Bar-cobar inversion,
  1545	 Theorem~\ref{thm:higher-genus-inversion}).
  1546	 On the Koszul locus, the counit
  1547	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$
  1548	 is an equivalence; the spectral sequence collapses at~$E_2$.
  1549	 Off the locus, the bar-cobar object persists but becomes curved;
  1550	 the failure is measured by
  1551	 $\Theta_\cA$~\eqref{eq:universal-MC}.
  1552	 The BRST resolution is complete.
  1553	
  1554	 More precisely, there is a spectral sequence with $E_1$ page
  1555	 $E_1^{p,q} = H^q(\barB^p_X(\cA))$ converging to $H^{p+q}(\Omega_X \barB_X(\cA))$.
  1556	 On the Koszul locus, $E_1^{p,q} = 0$ for $p \neq 1$, so
  1557	 $E_2 = E_\infty$, and the comparison map
 succeeded in 52ms:
   250	of $\overline{C}_n(X)$ and the Arnold relation).
   251	
   252	\subsection{From OPE to bar differential}
   253	\label{subsec:ope-to-bar}
   254	\index{bar complex!construction from OPE}
   255	\index{operator product expansion!as bar differential input}
   256	
   257	Let $\cA$ be a chiral algebra on~$X$. Place $n$ elements
   258	$a_1, \ldots, a_n$ at positions $z_1, \ldots, z_n$ and form
   259	\begin{equation}\label{eq:bar-element-intro}
   260	a_1(z_1) \otimes \cdots \otimes a_n(z_n)
   261	\otimes \bigwedge_{(i,j) \in E(T)} \eta_{ij}
   262	\;\in\;
   263	\cA^{\boxtimes n} \otimes
   264	\Omega^{n-1}_{\log}(\overline{C}_n(X)),
   265	\end{equation}
   266	where $T$ is a spanning tree of the complete graph $K_n$ on $\{1,\ldots,n\}$
   267	(selecting which pairs of log forms to wedge), and
   268	$\Omega^{n-1}_{\log}(\overline{C}_n(X))$ denotes
   269	$(n{-}1)$-forms on the FM compactification with at worst

thinking
**Researching modular homotopy theory**

I think I need to find the actual definition of modular homotopy theory around 3630. It might be better to look a bit earlier, but doing that may not be necessary. I know it’s included in the standalone full survey, so I should ensure that the references are redirected. It could help to restore the definition with a label from standalone 3630ff. Let’s check lines 3628-3675 to see if it includes the definition I need.
exec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '780,805p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '5490,5565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '3560,3610p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '3628,3685p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

 succeeded in 53ms:
  3628	is the genus-$0$ case of a structural parallel between Sullivan's
  3629	rational homotopy theory and the modular homotopy theory of
  3630	Definition~\ref{def:modular-homotopy-theory-intro}:
  3631	\begin{center}
  3632	\small
  3633	\renewcommand{\arraystretch}{1.15}
  3634	\begin{tabular}{lll}
  3635	\textbf{Rational (Sullivan)} && \textbf{Modular (this monograph)} \\
  3636	\hline
  3637	topological space~$X$
  3638	 && chiral algebra~$\cA$ on~$X$ \\[2pt]
  3639	de~Rham algebra $\Omega^*(X)$
  3640	 && modular convolution $\gAmod$ \\[2pt]
  3641	Sullivan minimal model
  3642	 && $L_\infty$-minimal model of $\gAmod$ \\[2pt]
  3643	Massey products $m_n$
  3644	 && shadow obstructions $o_{r+1}$ (Prop.~\ref{prop:shadow-massey-identification}) \\[2pt]
  3645	formality: $m_n = 0$ ($n \ge 3$)
  3646	 && Gaussian: shadow depth~$2$ \\[2pt]
  3647	K\"ahler $\Rightarrow$ formal
 succeeded in 53ms:
   780	\section{The selection principle}
   781	\label{sec:selection-principle}
   782	\index{selection principle|textbf}
   783	\index{Borcherds identity!as selection criterion}
   784	
   785	The bar construction of \S\ref{sec:the-seed} is a
   786	\emph{geometric} machine: take a $\mathcal{D}_X$-module~$V$
   787	with a meromorphic pairing
   788	$\mu \colon j_* j^*(V \boxtimes V) \to \Delta_!(V)$
   789	(the OPE), place sections at points of
   790	$\overline{C}_n(X)$, and extract residues along
   791	boundary divisors. The output is a graded object
   792	$\barB_X(V, \mu)$ with a candidate differential
   793	$d = d_{\mathrm{internal}} + d_{\mathrm{residue}}
   794	+ d_{\mathrm{dR}}$.
   795	
   796	The governing question:
   797	\begin{center}
   798	\emph{For which algebraic inputs $(V, \mu)$ does
   799	the FM bar construction produce $d^2 = 0$?}
 succeeded in 53ms:
  3560	degree-$3$ component of $\Theta_\cA$, is the graph sum over
  3561	trivalent trees, encoding the Lie bracket's contribution to the
  3562	modular bar construction. No quasi-isomorphism of modular bar
  3563	coalgebras can kill it, because it represents a nontrivial class in
  3564	$H^*(\Defcyc^{(3)}(\cA)|_{g=0})$
  3565	(Proposition~\ref{prop:shadow-massey-identification}).
  3566	
  3567	Shadow depth is therefore a modular-homotopy-type invariant. More
  3568	precisely: the $L_\infty$-minimal model of $\gAmod$ has
  3569	$\ell_r^{\mathrm{min}} = 0$ for $r < $ shadow depth and
  3570	$\ell_r^{\mathrm{min}} \ne 0$ at $r = $ shadow depth; this cannot
  3571	change under quasi-isomorphism.
  3572	\end{example}
  3573	
  3574	\begin{proposition}[Genus-$0$ shadow obstructions $=$ $A_\infty$
  3575	Massey products; \ClaimStatusProvedHere]
  3576	\label{prop:shadow-massey-identification}
  3577	\index{Sullivan dictionary|textbf}
  3578	\index{Massey product!shadow obstruction identification}
  3579	\index{shadow obstruction!as Massey product}

thinking
**Researching modular homotopy theory**

I think I need to clarify the actual definition of modular homotopy theory. It seems like I might not have the complete context, so I could be looking for a standalone explanation. Maybe it's possible that the definition was removed or not fully included where I initially looked. I'll definitely do a search to find the right label and ensure I have an accurate definition. Let's explore this together!
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:modular-homotopy-theory-intro\\}' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{eq:all-degree-master-eq-intro\\}|\\\\label\\{eq:universal-MC\\}|\\\\label\\{eq:the-seed\\}|\\\\label\\{eq:arnold-seed\\}|\\\\label\\{sec:flat-connection-intro\\}|\\\\label\\{sec:modular-char-spectral-disc-intro\\}|\\\\label\\{sec:primitive-kernel-intro\\}|\\\\label\\{subsec:shadow-postnikov-tower-intro\\}' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{prop:modular-homotopy-classification\\}|\\\\label\\{rem:categorical-logarithm-paradigm\\}' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3449:\label{def:modular-homotopy-theory-intro}
 succeeded in 52ms:
234:\begin{equation}\label{eq:the-seed}
242:\begin{equation}\label{eq:arnold-seed}
1051:\label{sec:primitive-kernel-intro}
1133:\label{sec:flat-connection-intro}
2058:\label{sec:modular-char-spectral-disc-intro}
2679:\begin{equation}\label{eq:universal-MC}
2938:\label{subsec:shadow-postnikov-tower-intro}
3134:\begin{equation}\label{eq:all-degree-master-eq-intro}
 succeeded in 52ms:
1987:\label{rem:categorical-logarithm-paradigm}
3506:\label{prop:modular-homotopy-classification}




thinking
**Analyzing LaTeX formatting**

I’m considering that LaTeX line breaks and indentation might be causing issues, maybe looking for spaces with `\s,` or something similar. I could search for unmatched braces or confined environments since the file is likely compiling. There’s an intro that's heavy, but the user wants to focus on transition quality and redundancy. I need to pinpoint lines discussing the five theorems and how they relate to geometry, algebra, and physics. I want to identify specific fixes, particularly where broad promises replace necessity.
thinking
**Refining section transitions**

I need to fix the text by replacing it with: "The ordered bar already supplies residues, Verdier duality, curvature, clutching, and associative ordering; the rest of the volume only decomposes those five inputs." However, this is somewhat of a rewrite. I should consider presenting an exact replacement. The user also asked if each section forces the next, or if transitions use signpost language like "We now turn to...". Many sections appear to open with such signpost formulas, which may need attention.
thinking
**Considering notation consistency**

I think the notation for `\omega_3(z)` might be ambiguous, as there's no local definition provided nearby. The user is concerned about consistency, and even though `\omega_3(z)` is a conventional placeholder, it seems important to flag that it’s not clearly defined. I should suggest either replacing it with a specific formula `r(z) = \frac{c/2}{z^3} + \frac{2T}{z}` or including a definition like `\omega_3(z)=z^{-3}` to clarify things. It does look like a potential reader obstruction.
thinking
**Searching for macro definitions**

The user specifically asks about any undefined macros. It seems `\omega_3` might not be a macro, but I’m unsure if it's defined elsewhere. I should search to see if a macro for `\omega_3` exists at all. Even if it is defined, I wonder if the notation has been introduced properly. I think the best approach right now is to look for occurrences of `\omega_3` in the relevant documents, just to clarify things.
exec
/bin/zsh -lc "rg -n '  ' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{subsec:e1-as-primitive\\}|\\\\label\\{sec:e1-as-primitive\\}' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\omega_3' chapters/theory/introduction.tex main.tex chapters appendices standalone | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|nameref)\\{(sec:e1-as-primitive|subsec:e1-as-primitive)\\}' chapters appendices standalone metadata main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 52ms:
1184:\label{sec:e1-as-primitive}
1185:\label{subsec:e1-as-primitive}
 succeeded in 51ms:
chapters/examples/yangians_foundations.tex:1218:\S\textup{\ref{subsec:e1-as-primitive}}. The Drinfeld--Kohno
chapters/connections/concordance.tex:3761:(\S\ref{subsec:e1-as-primitive}), which organises the relationship
chapters/theory/bar_construction.tex:1950: \S\textup{\ref{subsec:e1-as-primitive}}: at degree\/
standalone/introduction_full_survey.tex:414:information (\S\ref{subsec:e1-as-primitive}).
standalone/introduction_full_survey.tex:1510:(see~\S\ref{subsec:e1-as-primitive} for the averaging map
chapters/theory/introduction.tex.bak:139:information (\S\ref{subsec:e1-as-primitive}).
chapters/theory/introduction.tex.bak:743:(see~\S\ref{subsec:e1-as-primitive} for the averaging map
chapters/theory/introduction.tex:527:(see~\S\ref{subsec:e1-as-primitive} for the averaging map
chapters/theory/introduction.tex:1214:information (\S\ref{subsec:e1-as-primitive}).
 succeeded in 51ms:
chapters/theory/introduction.tex:1661:Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
chapters/examples/bar_complex_tables.tex:1589:$[J^a|J^b|J^c] \otimes \omega_3$
chapters/theory/en_koszul_duality.tex:3696:$\omega_3(X, Y, Z) = (X, [Y, Z])$,
chapters/theory/en_koszul_duality.tex:3699:scalar multiple of~$\omega_3$.
chapters/theory/en_koszul_duality.tex:4157:  \omega_3(X, Y, Z)
chapters/theory/en_koszul_duality.tex:4170:antisymmetric $3$-form $\omega_3$: the $\Pthree$ bracket
chapters/theory/en_koszul_duality.tex:4173:while any contraction of $\omega_3$ in two slots is
chapters/theory/en_koszul_duality.tex:4176:$H^3(\mathfrak{sl}_2)$, generated by $\omega_3$,
chapters/theory/en_koszul_duality.tex:4893:$\omega_3(X, Y, Z) = (X, [Y,Z])$ is the generator.
chapters/theory/koszul_pair_structure.tex:1077:d(\omega_3) = \text{(quadratic terms)} + \text{RTT}(J^a, J^b, J^c)
chapters/theory/higher_genus_foundations.tex:1274:\[m_3(\omega_1, \omega_2, \omega_3) = 
chapters/theory/higher_genus_foundations.tex:1275:\int_{\partial \overline{M}_{0,4}} \omega_1 \wedge \omega_2 \wedge \omega_3\]
chapters/theory/higher_genus_foundations.tex:1279:\item $(12|34)$: Gives $m_2(m_2(\omega_1,\omega_2),\omega_3)$
chapters/theory/higher_genus_foundations.tex:1281:\item $(14|23)$: Gives $m_2(\omega_1,m_2(\omega_2,\omega_3))$
chapters/theory/derived_langlands.tex:543:$\omega_3(a,b,c) = \kappa(a,[b,c])$ to the degree-$4$ invariant
chapters/theory/derived_langlands.tex:582:of~\eqref{eq:d4-obstruction} satisfies $d_4(\omega_3) \neq 0$.
chapters/theory/derived_langlands.tex:612:$d_4(\omega_3) \neq 0$.
chapters/theory/derived_langlands.tex:619:$\omega_3(a,b,c) = \kappa(a,[b,c])$ through the loop algebra:
chapters/theory/derived_langlands.tex:620:$\omega_3$ transgresses to a $1$-cocycle on $L\fg$ valued in the
chapters/theory/introduction.tex:1661:Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,


thinking
**Evaluating label usage**

I'm thinking about labeling sections and subsections. Is `sec:e1-as-primitive` still relevant, or should it be flagged as unused? I don't see references in real surfaces. Similarly, there are labels at 332 and 333; are both needed? A search could help clarify, but it might not be necessary. I'll need to look into other duplicate labels too, like `\label{sec:NAP-unifying}` and `\label{sec:main-results-complete}` to see if one could be eliminated. However, searching through everything could be overwhelming!
thinking
**Exploring label index**

I’m considering using a metadata or label index, but that might take some time and may not be comprehensive. I could audit the surfaces more exhaustively; there’s potential to utilize a label index. I can search for all the labels in the file and check their reference counts. A script could help; maybe using shell commands with `rg`. Producing a list of label names would allow me to find unused labels or aliases. I'll try looping through and ensure the output is clear!
codex
I’m doing one last systematic pass for unused labels inside the introduction rather than guessing from the obvious cases. The file has a lot of aliasing, and the only way to keep this honest is to count actual cross-references.
exec
/bin/zsh -lc 'labels=$(rg -o '"'\\\\label\\{["'^}]+'"\\}' chapters/theory/introduction.tex | sed 's/.*{//; s/}//'); for l in "'$labels; do c=$(rg -n "'"\\\\(ref|eqref|autoref|nameref)\\{"'$l'"\\}\" chapters appendices standalone metadata main.tex | wc -l | tr -d ' '); if [ \""'$c" = "0" ]; then printf '"'%s\\n' \""'$l"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
rg: regex parse error:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 1: (?:\(ref|eqref|autoref|nameref)\{sec:volume-one-route
 2: rem:two-strata
 3: eq:intro-visibility
 4: sec:selection-principle
 5: rem:classical-vs-chiral-selection
 6: sec:NAP-unifying
 7: sec:main-results-complete
 8: subsec:five-theorems-heisenberg
 9: subsec:five-theorems-general
10: eq:complementarity-intro
11: eq:ahat-genus-generating-function-intro
12: warn:three-hochschild-intro
13: princ:five-facets
14: conj:boundary-bulk-thesis
15: prop:five-facets-collision-residue
16: rem:five-facets-boundary-bulk
17: rem:five-facets-seven-faces
18: rem:e1-five-theorems
exec
/bin/zsh -lc "rg -o '\\\\label\\{["'^}]+'"\\}' chapters/theory/introduction.tex | sed 's/.*{//; s/}//' | while IFS= read -r l; do c="'$(rg -n "'"\\\\\\\\(ref|eqref|autoref|nameref)\\\\{"'$l'"\\\\}\" chapters appendices standalone metadata main.tex | wc -l | tr -d ' '); if [ \""'$c" = "0" ]; then printf '"'%s\\n' \""'$l"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 777ms:
subsec:five-theorems-heisenberg
subsec:five-theorems-general
eq:complementarity-intro
eq:ahat-genus-generating-function-intro
warn:three-hochschild-intro
conj:boundary-bulk-thesis
rem:five-facets-seven-faces
sec:e1-as-primitive
eq:intro-bar-ord
eq:intro-gAmod-e1
rem:categorical-e1-primacy
princ:e1-primacy
rem:e1-primacy-scope
warn:five-e1-notions-intro
rem:en-circle-intro
rem:three-tier-examples
rem:three-tier-boundary-bulk
rem:topologization-intro
sec:architecture
rem:dk-inevitability

thinking
**Executing label mapping**

I’m considering using the exec command to generate a mapping for `label line`, focusing only on the unused labels. This seems like a clear and efficient way to streamline my output. I want to ensure I’m targeting the right labels, which will help keep things organized. So, I'll go ahead and implement this mapping now. It feels good to make progress on this!
codex
The introduction is carrying a lot more unused anchor debt than the obvious four traverse labels. I’m mapping the exact line numbers now so the final report can name the dead labels precisely instead of vaguely saying “there are many”.
exec
/bin/zsh -lc 'unused=$(rg -o '"'\\\\label\\{["'^}]+'"\\}' chapters/theory/introduction.tex | sed 's/.*{//; s/}//' | while IFS= read -r l; do c="'$(rg -n "'"\\\\\\\\(ref|eqref|autoref|nameref)\\\\{"'$l'"\\\\}\" chapters appendices standalone metadata main.tex | wc -l | tr -d ' '); if [ \""'$c" = "0" ]; then printf '"'%s\\n' \""'$l"; fi; done); while IFS= read -r l; do rg -n "'"\\\\label\\{"'$l'"\\}\" chapters/theory/introduction.tex; done <<< \""'$unused"' in /Users/raeez/chiral-bar-cobar exited 2 in 1.57s:
rg: regex parse error:
    (?:\label\{eq:intro-visibility\})
       ^^
error: unrecognized escape sequence
rg: regex parse error:
    (?:\label\{rem:classical-vs-chiral-selection\})
       ^^
error: unrecognized escape sequence
rg: regex parse error:
    (?:\label\{sec:NAP-unifying\})
       ^^
error: unrecognized escape sequence
rg: regex parse error:
    (?:\label\{sec:main-results-complete\})
       ^^
error: unrecognized escape sequence
rg: regex parse error:
    (?:\label\{subsec:five-theorems-heisenberg\})
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'unused=$(rg -o '"'\\\\label\\{["'^}]+'"\\}' chapters/theory/introduction.tex | sed 's/.*{//; s/}//' | while IFS= read -r l; do c="'$(rg -n "'"\\\\\\\\(ref|eqref|autoref|nameref)\\\\{"'$l'"\\\\}\" chapters appendices standalone metadata main.tex | wc -l | tr -d ' '); if [ \""'$c" = "0" ]; then printf '"'%s\\n' \""'$l"; fi; done); while IFS= read -r l; do rg -n -F "'"\\\\label{"'$l}" chapters/theory/introduction.tex; done <<< "$unused"' in /Users/raeez/chiral-bar-cobar succeeded in 823ms:
128:\begin{equation}\label{eq:intro-visibility}
237:\label{rem:classical-vs-chiral-selection}
332:\label{sec:NAP-unifying}
333:\label{sec:main-results-complete}
410:\label{subsec:five-theorems-heisenberg}
511:\label{subsec:five-theorems-general}
599: \begin{equation}\label{eq:complementarity-intro}
642: \begin{equation}\label{eq:ahat-genus-generating-function-intro}
696:\label{warn:three-hochschild-intro}
770:\label{conj:boundary-bulk-thesis}
971:\label{rem:five-facets-seven-faces}
1184:\label{sec:e1-as-primitive}
1201:\begin{equation}\label{eq:intro-bar-ord}
1218:\begin{equation}\label{eq:intro-gAmod-e1}
1395:\label{rem:categorical-e1-primacy}
1408:\label{princ:e1-primacy}
1505:\label{rem:e1-primacy-scope}
1529:\label{warn:five-e1-notions-intro}
1576:\label{rem:en-circle-intro}
1647:\label{rem:three-tier-examples}










thinking
**Evaluating unused labels**

I'm noticing many labels that are currently unused, which suggests we might be looking at some dead code. There could be internal anchors for future use, but for now, they'll stay as dead code. The user asked about this, so grouping significant clusters could be a good idea. For instance, there are sections and equation labels that might be worth cleaning up. Overall, while many labels are unused, grouping them seems fair, and I think they can be considered low severity.
thinking
**Grouping findings for fixes**

I’m thinking that if I list all findings, the output might get too long. Instead, maybe I should group the findings by pattern. Since the user wants exact line numbers and fixes, I can organize the line sets within the relevant problem text. For example, there are various dead anchors I could recommend deleting, and I should check for item and equation labels that are unreferenced. Plus, it seems there’s an undefined term that could use some attention.
thinking
**Evaluating notation consistency**

I'm looking into some placeholders in a table related to `K` values, which don't seem to be family-specific. The table has a heading `K = c + c'`, but in earlier theorem C, `K` is defined differently. I notice a potential inconsistency where `K` is used in various ways, leading to confusion. The entries for different systems show central charge complementarity, highlighting a real collision in notation, which seems significant.
thinking
**Identifying notation issues**

I'm checking lines 355-357, which reference Theorem C and its constraints regarding the Koszul dual pair. Here, `K` is defined as the kappa-complementarity constant, with specific values for different systems. But then, the later table shows `K = c + c'`, leading to inconsistent notation! This finding feels significant. I should propose an exact fix, like renaming the column or splitting it into two for clarity. I also need to check lines 2141 and 2146 for further context. This could be serious!
thinking
**Clarifying sum collisions**

I'm looking back at some earlier lines where Heisenberg uses a kappa sum of 0 and a c sum of 2, which makes the collision of `K` values more evident. This inconsistency between the sums feels significant, especially considering how it might affect the overall interpretation of the data. It’s a small but important detail that I need to keep in mind as I continue to analyze the information.
thinking
**Evaluating technical details**

I’m noticing a potential issue at line 2195, where `The Characteristic Datum` uses `$E_1$` instead of `\Eone`. It mentions `$E_1$ wing; $E_n$ Koszul duality`, which might be fine after all. I need to check for any commented-out sections larger than ten lines but haven’t found any. There’s one four-line comment, but it's okay. However, there’s a critical issue at theorem label 2508 related to phantom sections, needing an exact fix to restore the theorem environment or rename it.
thinking
**Identifying unused labels**

I’m noticing there are several unused label clusters that I might need to address. There seems to be a dead labels cluster in sections 332, 333, 410, and a few others. Additionally, there's another cluster involving equations, and then there's a theorem/remark label cluster too. Since the user asked for every finding, I could summarize all the unused labels in a manageable way, listing them with their corresponding line numbers. It could be long, but it seems doable if I keep it concise!
thinking
**Evaluating mathematical concepts**

I'm grappling with whether the center can be nonzero since it seems contradictory regarding direct sums. Earlier, I defined complementary Lagrangians as eigenspaces with eigenvalues ±1, where the intersection isn’t the center. However, one line implies the intersection is the center, which feels off unless the center is zero. I need to double-check the lines outlining these ideas and understand how the ambient complex fits in, especially regarding the Verdier involution and its roles in the decomposition.
thinking
**Clarifying mathematical terms**

I'm finding this situation quite tricky because ±1 eigenspaces only intersect trivially, so it raises questions about the meaning of "center" in this context. If the intersection refers to something before cohomology, it still leads to contradictions about the direct sum. I see a need for a precise fix: either clarify the statement about direct sums and intersections or revise my understanding of how they connect to the center. I should consider different approaches to ensure accuracy in defining these relationships.
thinking
**Investigating logical consistency**

I think I need to search the main theorem or another file to clarify the intended complementarity. Earlier lines mention that \(Q_g(A) \oplus Q_g(A^!) \cong H^*(..., Z_A)\), which confirms a direct sum and an intersection of zero. So, it seems like line 606 might just be an oversight in the prose. This could indicate a significant logical error that should be addressed in the introduction. I should consider citing line 606 to support this point.
exec
/bin/zsh -lc "rg -n 'conj:FM-convergence' chapters appendices standalone metadata main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1474,1486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'open-to-closed boundary operator|open-to-closed' chapters/theory/introduction.tex AGENTS.md CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2588,2594p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/dependency_graph.dot:2618:  conj_FM_convergence [label="conj:FM-convergence\nconjecture [Co]\nConvergence criterion", style=filled, fillcolor="#fff9c4"];
metadata/label_index.json:1958:  "conj:FM-convergence": {
metadata/claims.jsonl:2517:{"label": "conj:FM-convergence", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/theory/configuration_spaces.tex", "line": 3421, "title": "Convergence criterion"}
chapters/theory/configuration_spaces.tex:3421:\begin{conjecture}[Convergence criterion; \ClaimStatusConjectured]\label{conj:FM-convergence}
chapters/theory/introduction.tex:2592: (Theorem~\ref{conj:FM-convergence}).
 succeeded in 51ms:
  1474	
  1475	\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
  1476	operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
  1477	open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
  1478	(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself
  1479	is a single-coloured $\Eone$-chiral coassociative coalgebra
  1480	over $(\mathrm{ChirAss})^!$. The SC structure emerges on the
  1481	derived center, not on the bar complex. The closed sector of any
  1482	Swiss-cheese algebra is recovered from the open sector by passing
  1483	to $\Sigma_n$-coinvariants along the open-to-closed boundary
  1484	operator. The closed sector is intrinsically a quotient of the
  1485	open sector, never an enrichment of it.
  1486	
 succeeded in 51ms:
AGENTS.md:57:**SC^{ch,top} ≠ E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:838:AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
chapters/theory/introduction.tex:1483:to $\Sigma_n$-coinvariants along the open-to-closed boundary
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '592,608p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2588	 See Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}.
  2589	\item\label{SA:convergence} Formal power series in completed
  2590	 tensor products. Configuration space integrals converge
  2591	 absolutely on FM compactifications
  2592	 (Theorem~\ref{conj:FM-convergence}).
  2593	\item\label{SA:curves} Smooth projective geometrically connected
  2594	 curves over~$\mathbb{C}$.
 succeeded in 52ms:
   592	 carries a shifted-symplectic pairing from Verdier duality.
   593	 The Verdier involution decomposes it
   594	 into \emph{complementary Lagrangians}
   595	 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$:
   596	 the $+1$ and $-1$ eigenspaces of the involution
   597	 (Definition~\ref{def:complementarity-complexes}).
   598	 At the cohomological level,
   599	 \begin{equation}\label{eq:complementarity-intro}
   600	 Q_g(\cA) \oplus Q_g(\cA^!) \cong
   601	 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA).
   602	 \end{equation}
   603	 The anomaly of one algebra is the ghost-number violation of
   604	 its dual.
   605	
   606	 The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.
   607	
   608	\item \emph{Theorem~D$_{\mathrm{scal}}$} (Scalar modular

thinking
**Searching propositions and theorems**

I'm planning to search for `Theorem\ref{conj:` in the file, thinking there might only be one occurrence. I might also look for `Proposition\ref{conj:` as well, but I could choose to ignore it if nothing shows up. It feels like a quick search could clear things up, just in case there’s something I’m missing. Keeping options open seems like a good idea!
exec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{conj:|Proposition~\\\\ref\\{conj:|Lemma~\\\\ref\\{conj:|Definition~\\\\ref\\{conj:|Remark~\\\\ref\\{conj:' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2592: (Theorem~\ref{conj:FM-convergence}).

thinking
**Investigating theorem issues**

I see a potential issue between the theorem and conjecture noted at line 2592. There’s also a mention of a phantom theorem in line 2508. It might be worthwhile to have one critical finding that addresses all the phantom section stubs. The exact fix could reference standalone survey sources. So, I plan to look into the actual blocks in the standalone section for prop: modular-homotopy-classification and definition, particularly around lines 3440 to 3515.
exec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '3438,3518p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '1978,2002p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1978	 \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}},
  1979	 Theorem~\textup{\ref{thm:chiral-deligne-tamarkin}}\textup{)}.
  1980	 This is the chiral analogue of the Deligne--Tamarkin theorem:
  1981	 the bulk of any holomorphic boundary theory is forced by
  1982	 locality to be the chiral Hochschild cochains.
  1983	\end{enumerate}
  1984	\end{theorem}
  1985	
  1986	\begin{remark}
  1987	\label{rem:categorical-logarithm-paradigm}
  1988	The genus tower is the Taylor expansion of the monodromy
  1989	$\kappa(\cA)\cdot\omega_g$. The nonlinear characteristic layer
  1990	computes the higher Taylor jets of this expansion: the quartic jets
  1991	of the complementarity potential
  1992	(Chapter~\ref{app:nonlinear-modular-shadows}), the spectral
  1993	cumulants of the branch-line quotient
  1994	(Appendix~\ref{app:branch-line-reductions}), and the canonical
  1995	homotopy degree in the non-principal $\mathcal W$-algebra sector.
  1996	\end{remark}
  1997	
 succeeded in 53ms:
  3438	Scalar saturation, the identity
  3439	$\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$
  3440	(Corollary~\ref{cor:scalar-saturation}), holds whenever
  3441	$\dim H^2_{\mathrm{cyc}}(\cA,\cA) = 1$.
  3442	Theorem~\ref{thm:algebraic-family-rigidity} extends it
  3443	to all non-critical levels for algebraic families with rational
  3444	OPE coefficients;
  3445	Conjecture~\ref{conj:scalar-saturation-universality} addresses
  3446	the residual non-algebraic-family case.
  3447	
  3448	\begin{definition}[Modular homotopy theory on a smooth curve]
  3449	\label{def:modular-homotopy-theory-intro}
  3450	\index{modular homotopy theory!definition|textbf}
  3451	A \emph{modular homotopy theory} for a chiral algebra~$\cA$
  3452	on a smooth projective curve~$X$ consists of the following data:
  3453	\begin{enumerate}[label=\textup{(\roman*)}]
  3454	\item \emph{Bar-cobar adjunction.}
  3455	 An adjunction
  3456	 $\barB_X \dashv \Omega_X$ on
  3457	 $D^{\mathrm{co}}(\operatorname{Fact}(X))$, the coderived


















thinking
**Checking notation consistency**

I’m noticing possible inconsistencies with the notations like `A^{\mathrm{i}}` or `A^i`, especially since the introduction uses unusual notation. The user requested consistency, and there are various notations for Koszul dual coalgebras throughout. I should also consider the convergence assumption for the configuration space integrals. It's important to note that there may be subtle issues like the direct sum versus intersection, directionality, notation collisions, and some unused labels that might need attention.
thinking
**Identifying potential issues**

I’m identifying several potential redundancy items and low typography issues. I need to check if labels like `subsec:traverse-part-I...` and `sec:NAP-unifying` are indeed unused—looks like they are. Also, I should see if `\label{sec:e1-as-primitive}` isn’t used while `subsec:e1-as-primitive` is—it's essential to mention in the unused anchor cluster. There may be a double label issue with `conv:proof-architecture` as well. I should search for any undefined macros too. It seems like `\omega_3(z)` isn't macro-defined in this context, which is something to keep an eye on.
thinking
**Identifying issues in documentation**

I’ve found some problems in the documentation. For the bar propagator \(d\log(z-w)\), it lacks punctuation, so I'd fix it by adding a period or semicolon after "OPE." 

Next, `\omega_3(z)` is introduced without definition, causing conflicts in notation. I should either replace it with the canonical formula or define it locally.

Also, in the table, the lattice and Yangian rows shouldn't use `---`, so I'll replace those with `\text{n/a}` or leave them blank.

Lastly, I noticed some unused labels that could create clutter.
thinking
**Considering label organization**

I’m thinking about how label clutter might appear when presenting the same pattern. It could be useful to group findings with all the labels enumerated, but that might become overwhelming. Perhaps I can shorten it by saying, “unused labels across the file, namely...” and then list them. I also wonder if it’s worth including line 237 for `rem:classical-vs-chiral-selection`. If there are many unused remarks or principles, could that really be harmful?
thinking
**Evaluating dead code findings**

I’m thinking about whether to omit unused labels if we have other findings like phantom stubs. The user did ask for all dead code and every finding. Maybe I should include just the dead traverse labels and unused SA labels since they’re clearer. Although not all dead surfaces might need inclusion. I could check line 2141 and possibly fix issues with the table row, particularly for Yangian where many entries seem to be n/a. There’s also a potential issue with line 2059.
thinking
**Assessing potential failures**

I’m considering whether there might be more second-order failures, particularly related to lines 359-363 where Theorem D identifies \kappa as a one-loop coefficient. Okay, table line 2141 uses `K = c+c'`, which is good to note. Now, line 2044 discusses proving the equivalence of chiral Koszulness and exact holographic reconstruction. While it might duplicate earlier theorem B, I’m not sure. Also, line 1442 brings up Heisenberg's r(z), which could be an identity but may not be related to the Casimir. I might just ignore that for now.
thinking
**Evaluating output format possibilities**

I’m thinking about how to address the problem list, particularly if there’s a chance of unused labels clustering at line 128. The user wants exact line numbers, so I should probably stick to that rather than using line ranges in the header. However, in the problem text, I might mention other lines as needed. It’s all about balancing clarity for the user while meeting their specifications!
thinking
**Evaluating unused aliases and potential issues**

I’m looking at the unused alias labels between lines 2165-2168, and that's okay. For clarity, I could refer to the first line and then mention the others. There's also the possibility of highlighting a specific cluster at lines 2165 and 2584. If I want to cover all unused labels, I might cite line 128 and list them. I also need to consider potential duplicates between `sec:e1-as-primitive` and `subsec:e1-as-primitive`. Then, I'll assess severity levels for various issues: phantom theorem stubs as critical, followed by high and medium classifications for others.
thinking
**Verifying line conflicts and references**

I need to check if the conflict at line 1482 can be validated based on the AGENTS file. It looks like I can confirm it, but I should base my final assertions on the actual file contents. The AGENTS document states that the "repo constitution forbids open-to-closed." However, since the user wants findings limited to the target file, I might only cite the specific line and the issue.

I shouldn’t quote AGENTS directly but could mention that this contradicts the stated SC convention. Overall, I can keep it general when referencing the manuscript’s SC convention. Lastly, I need to remember that phantom stubs involve searching the entire repo.
thinking
**Identifying potential kappa issues**

I've noticed a potential issue with line 2141 that the user brought up regarding bare kappa. I could mention that the `\kappa` table header is bare, but the more serious problem seems to be related to the K notation collision. I wonder if there might be other bare kappa issues, perhaps around line 2565 or even elsewhere. My goal is to ensure I'm being thorough in identifying all potential conflicts related to this in the document!
thinking
**Evaluating findings contextually**

I’m looking at the findings, and I think not every result will show bare kappas if the context is fixed. That aspect seems tricky. Similarly, I’ve noticed there aren’t any bare `\Omega/z` hits without k involved, so there shouldn’t be an issue there. It might be good to note in the summary that no bare `\Omega/z` hits are present. That should clarify things for anyone reading my summary.
thinking
**Reviewing potential issues**

I’m dealing with potential issues in the document. On line 365, it mentions "total dimension at most four," while there's a polynomial with P(t)=1+t^2. I want to confirm that Theorem H is applicable. I also noticed that line 606 might have copied text erroneously, so that’s a good catch. There are other minor issues, like a remark on line 237 being unused and potential formatting problems. Lastly, line 1661 brings up an undefined notation, which needs addressing.
thinking
**Identifying issues**

I’m noticing potential issues in the document. Line 925 refers to "OPE Thus," which seems good. Should I mention that lines 2153 and 2154 use `---`, which could be a markdown horizontal rule? But maybe that’s not necessary since em-dashes are forbidden. I also need to bring attention to line 2508, as there seems to be a theorem label prefix mismatch (AP125). Keeping track of these details is important!
thinking
**Exploring notation consistency**

I’m thinking about whether I could combine the line about K collision with my existing notation. There’s some ambiguity in the scalar notation, like the bare `\kappa` at one point and the reused `K` at another, which might be causing confusion. It seems like the K collision is quite significant, while the bare kappa is less so. I’ll need to clarify this to ensure consistency in my summary surfaces moving forward.
thinking
**Deciding on findings format**

I'm considering how to present the findings for the user. They requested a bullet format, so a flat bullet list seems best, with one or two sentences per bullet. I'm debating whether to use bold text or code formatting for file paths. The structure they want is `[SEVERITY] file:line — PROBLEM: ... FIX: ...`. I think I'll go with plain lines, ensuring no nested bullets, and provide a summary afterward. Let's aim for clarity!
thinking
**Considering document structure**

I could reference standalone file lines and maybe use clickable links to enhance the clarity. For example, I could say something like: "restore theorem block from standalone/introduction_full_survey.tex at line 1877." That feels helpful. Also, I’m wondering if I need to count findings, looks like around 13 or 14. It’s all about making the information clear and accessible for whoever's looking at it!
thinking
**Summarizing findings on theorems**

Let's highlight 15 key findings I need to address. First, I want to ensure that the bare kappa in line 2565 is rewritten correctly: either `\dfib^{\,2}=\kappa(\cA)\cdot \omega_g; \Dg{g}^{\,2}=0.` or `\dfib^{\,2} = \kappa_\cA \cdot \omega_g`. Since the repo uses `\kappa(\cA)` earlier, I should definitely go with that. For the undefined Virasoro notation in line 1661, the fix is to replace the row with the given expression and possibly shorten it within the tier example.
thinking
**Identifying precise fixes**

I want to focus on fixing the punctuation issue in line 927, which requires inserting a period after "OPE." A clear way to rewrite the sentence would be: "the bar propagator $d\log(z-w)$ absorbs one pole from the OPE. Thus, $r(z)$ is ...". This revision will ensure clarity and correctness in the text. Overall, it’s important to keep track of these details so everything flows smoothly.
codex
- [CRITICAL] chapters/theory/introduction.tex:2508 — PROBLEM: `\phantomsection\label{thm:modular-koszul-duality-main}` is a dummy anchor, not a theorem, but the manuscript cites it as “Theorem” and even cites parts `(ii)` and `(iv)`. FIX: restore the real theorem block at this location from `standalone/introduction_full_survey.tex:1877` onward as a theorem/maintheorem with parts `(i)`–`(v)`, and keep the `thm:` label on that environment instead of on a phantom section.

- [HIGH] chapters/theory/introduction.tex:2494 — PROBLEM: theorem-like stubs `def:modular-homotopy-theory-intro`, `prop:modular-homotopy-classification`, `prop:shadow-massey-identification`, and `rem:categorical-logarithm-paradigm` were left behind as `\phantomsection` anchors after relocation, but other chapters still cite them as Definition/Proposition/Remark objects. FIX: restore the actual environments from `standalone/introduction_full_survey.tex:3448`, `3504`, `3574`, and `1986`, or rename those labels to neutral `sec:` anchors and update every downstream `Definition~\ref`, `Proposition~\ref`, and `Remark~\ref` accordingly.

- [HIGH] chapters/theory/introduction.tex:2495 — PROBLEM: equation/section stubs `eq:all-degree-master-eq-intro`, `eq:arnold-seed`, `eq:bar-graded-object-intro`, `eq:the-seed`, `eq:universal-MC`, `sec:flat-connection-intro`, `sec:modular-char-spectral-disc-intro`, `sec:primitive-kernel-intro`, and `sec:the-seed` are anchored to `\phantomsection`, yet the manuscript uses `\eqref`/`\ref` on them as if they were real numbered displays or sections. FIX: move each label onto the corresponding live equation/section, or restore the original displays from `standalone/introduction_full_survey.tex:234`, `242`, `284`, `2679`, `3134`, `1051`, `1133`, `2058`, and `2938`.

- [HIGH] chapters/theory/introduction.tex:2141 — PROBLEM: notation collides with itself. Earlier the file defines the family constant by `\kappa(\cA)+\kappa(\cA^!)=K_\cA` (lines 355–358), but this table redefines `K` as `c+c'`. FIX: rename the table column and prose to `c+c'` or `K_c`, and add a separate `K_\kappa := \kappa(\cA)+\kappa(\cA^!)` column if that invariant is also meant to appear.

- [HIGH] chapters/theory/introduction.tex:606 — PROBLEM: the same sentence says `Q_g(\cA)` and `Q_g(\cA^!)` are the `\pm1` eigenspaces of an involution, that their intersection is `Z(\cA)`, and that the ambient complex is their direct sum. `\pm1` eigenspaces intersect trivially. FIX: replace the last sentence with “Their intersection is \(0\); the ambient complex is the direct sum \(Q_g(\cA)\oplus Q_g(\cA^!)\).” If the center is intended to appear, describe it separately as the fiber/local system, not as the intersection.

- [HIGH] chapters/theory/introduction.tex:1481 — PROBLEM: the Swiss-cheese paragraph asserts an “open-to-closed boundary operator” and says the closed sector is a quotient of the open sector. That contradicts the manuscript’s own SC directionality convention. FIX: rewrite the last two sentences to: “The SC structure is two-coloured and directional; it lives on the pair \((\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)\), not on the bar complex. There is no open-to-closed operadic map, so the closed sector is not obtained as a quotient of the open bar complex.”

- [MEDIUM] chapters/theory/introduction.tex:2592 — PROBLEM: the standing-assumptions block cites `conj:FM-convergence` as `Theorem~\ref{conj:FM-convergence}` even though the source object is a conjecture. FIX: change the sentence to “Configuration space integrals are assumed to converge absolutely on FM compactifications; see Conjecture~\ref{conj:FM-convergence}.”

- [MEDIUM] chapters/theory/introduction.tex:340 — PROBLEM: the unnumbered “boundary-bulk reconstruction thesis” paragraph duplicates the formal conjecture at lines 768–868, so the introduction states the same thesis twice with different granularity. FIX: delete the paragraph body at lines 340–349 and replace it with a one-sentence forward reference to `Conjecture~\ref{conj:boundary-bulk-thesis}`.

- [MEDIUM] chapters/theory/introduction.tex:368 — PROBLEM: lines 368–390 enumerate the five facets of `\Theta_\cA`, then lines 718–765 do the same again in `Principle~\ref{princ:five-facets}`. FIX: keep the formal principle and compress lines 368–390 to a bridge sentence plus the unique shadow-degree data.

- [LOW] chapters/theory/introduction.tex:2164 — PROBLEM: “Each chapter builds on the previous one; the five theorems emerge as milestones.” is table-of-contents boilerplate, not a forced transition. FIX: replace it with a dependency sentence, e.g. “Because every later result constructs, projects, or tests \(\Theta_\cA\), the volume proceeds from the bar complex that defines it to the examples and bridges that constrain it.”

- [LOW] chapters/theory/introduction.tex:2565 — PROBLEM: the regime-tag convention uses bare `\kappa` in a global statement, with no algebra fixed. FIX: write `\kappa(\cA)` or `\kappa_\cA` in the curved-central bullet: `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`.

- [LOW] chapters/theory/introduction.tex:1661 — PROBLEM: `\omega_3(z)` appears without local definition and reuses a symbol already used elsewhere in the repo for an unrelated 3-form. FIX: replace the example with the explicit Virasoro singular part `r(z)=\frac{c/2}{z^3}+\frac{2T}{z}`.

- [LOW] chapters/theory/introduction.tex:927 — PROBLEM: the sentence is broken: “the OPE Thus \(r(z)\)…” is missing punctuation. FIX: insert a period or semicolon after “OPE”.

- [LOW] chapters/theory/introduction.tex:2153 — PROBLEM: the lattice and Yangian rows use `---` as placeholders, which this repo forbids. FIX: replace each `---` with `\text{n/a}` or leave the cells blank.

- [LOW] chapters/theory/introduction.tex:128 — PROBLEM: the file carries substantial unused-label debt. `rg` finds no live refs to anchors including `eq:intro-visibility` (128), `sec:NAP-unifying` (332), `sec:main-results-complete` (333), `subsec:five-theorems-heisenberg` (410), `subsec:five-theorems-general` (511), `sec:e1-as-primitive` (1184), `sec:architecture` (1766), `sec:traverse` (2161), `subsec:traverse-part-I`–`IV` (2165–2168), `subsec:numbered-traverse` (2258), `SA:ground-field`–`SA:completion` (2584–2595), and `subsec:critical-pitfalls` (2639). FIX: delete unused `\label{...}` commands; reintroduce an anchor only when a real reference exists.

## Summary
Checked: 2684 | Findings: 15 | Verdict: FAIL
tokens used
166,709
