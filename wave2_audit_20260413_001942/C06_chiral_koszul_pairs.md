# C06_chiral_koszul_pairs (676s)

- [HIGH] `chapters/theory/chiral_koszul_pairs.tex:4759` — PROBLEM: a `remark` is labeled `sec:feynman_genus_g`, but `chapters/theory/higher_genus_foundations.tex:4754` references `rem:feynman_genus_g`; `main.log` reports that reference as undefined. FIX: rename the label here to `\label{rem:feynman_genus_g}` and delete `\label{sec:feynman_genus_g}`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:45` — PROBLEM: the introduction abandons the deficiency opening and front-loads theorem inventory plus bookkeeping (`Theorem A`, `9+1+1+1`) before the local mathematics starts. FIX: replace lines 45-73 with one necessity paragraph, e.g. `Any usable duality here must invert on the Koszul locus, intertwine Verdier duality, and fit complementarity; the precise equivalences are stated when those results are proved below.` Move the `9+1+1+1` count to Theorem~`\ref{thm:koszul-equivalences-meta}`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:114` — PROBLEM: the paragraph introduces `\kappa(\cA)` and then degrades to bare `\Delta = 8\kappa S_4` and bare `\kappa` at line 117, so the algebra dependence disappears. FIX: write `\Delta_\cA = 8\,\kappa(\cA)\,S_4(\cA)` and `At genus zero all three collapse: \kappa(\cA) plays no role`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:1433` — PROBLEM: `At generic level ($\kappa \neq 0$)` uses bare `\kappa` inside a Kac--Moody-only remark. FIX: write `At generic level ($\kappa(\widehat{\fg}_k)\neq 0$)` or introduce a local symbol `\kappa_k`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:2445` — PROBLEM: the Gaiotto--Kulp--Wu remark again uses bare `\Delta = 8\kappa S_4`. FIX: write `\Delta_\cA = 8\,\kappa(\cA)\,S_4(\cA)`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:2528` — PROBLEM: the class-`M` discussion and proof use bare `\kappa` in a Virasoro-only computation (`\Delta = 8\kappa S_4`, `2\kappa/\kappa`). FIX: replace that block with `\Delta_{\mathrm{Vir}_c}=8\,\kappa_c S_4` and `2\kappa_c/\kappa_c=2`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:4136` — PROBLEM: `Bar computes Koszul dual, complete statement` restates the earlier bar-cobar theorem in a second notation system (`\mathcal{A}`, `\bar{B}^{\text{ch}}`, completion language), so the chapter carries two competing main statements. FIX: demote this to a proposition such as `Completed comparison map for Stage~3`, state only the extra completion content, and normalize the statement to the chapter macros (`\cA_i`, `\barBgeom`/`\barB_X`).

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:5415` — PROBLEM: the remark falls back from `\kappa(\cA)+\kappa(\cA^!)=K` to bare `\kappa + \kappa^! = K`. FIX: rewrite the sentence as `decategorification recovers the scalar identity \kappa(\cA)+\kappa(\cA^!)=K`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:136` — PROBLEM: `The chapter proceeds in three stages.` is roadmap prose, not a forced transition. FIX: replace the paragraph with a necessity transition, e.g. `The Heisenberg calculation isolates the twisting datum; once that datum is fixed, PBW comparison yields the recognition theorem and the genus-zero bar-cobar adjunction.`

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1663` — PROBLEM: the section changes track with empty signpost prose (`We now give...` here; the same defect recurs at 3220 `We now record...` and 3825 `We record here only...`). FIX: replace them with mathematical-necessity transitions: `The Li filtration is the first refinement that sees the geometry hidden from the Shapovalov test`; `Because the PBW route is affine-specific, the next invariant must be Poisson-geometric`; `Only the Yangian self-duality statements are needed for the Koszul argument; the Hopf-theoretic material stays in Chapter~\ref{chap:yangians}.`

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1129` — PROBLEM: the eight-line `RECTIFICATION-FLAG` comment is stale audit residue embedded in the theorem surface. FIX: delete lines 1129-1136 entirely.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1409` — PROBLEM: there is a stray space before punctuation in `range ;`; the same defect recurs at 2829 (`family-dependent :`). FIX: change them to `range;` and `family-dependent:`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:2933` — PROBLEM: the table uses `---` as a cell value, which violates the no-em-dash rule and reads like placeholder text. FIX: replace `---` with `undetermined` or `not yet identified`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:4665` — PROBLEM: this table uses vertical rules and `\hline`, which clashes with the chapter’s `booktabs` tables; the same drift recurs at 4745 and 5779. FIX: rewrite these three tables with `\begin{tabular}{@{}...@{}}`, `\toprule`, `\midrule`, and `\bottomrule`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:485` — PROBLEM: legacy italic correction `where\/` appears in roman text; the same outdated markup recurs at 4938-4945 (`Let\/`, `If\/`, `then\/`, `construction\/`). FIX: remove every `\/` in these lines and keep plain prose.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:3940` — PROBLEM: the file carries dead or redundant labels with no `.tex` refs in `chapters/` or `appendices/`: `prob:circularity` (3940), `def:koszul-dual-coalgebra` (3962), `const:wn-general` (4634), `ex:affine-yangian-kp`/`ex:yangian-completion` (4684-4685), `rem:convergence-pro-nil`/`rem:convergence-pronilpotent` (4818-4819), `con:verify-koszul-pair` (5910). FIX: delete those labels; if a handle is actually needed later, keep one canonical label per block and reference it.

## Summary
Checked: 5986 | Findings: 16 | Verdict: FAIL


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
session id: 019d83f0-3a6b-7cd1-a3db-428f06fcc2d7
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/theory/chiral_koszul_pairs.tex

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
**Planning for file audit**

I need to audit an entire file, complying with requests outlined in the AGENTS document. Even though the user asked for an audit rather than editing, I might still review relevant constitutional files for context. The task seems to align with deep-beilinson-audit processes, and since it's a harsh adversarial audit request, I should announce skill use and the reasoning behind it in comments. Using the explorer agent will help gather information efficiently, especially since the developer recommended it for codebase questions.
thinking
**Clarifying audit process**

I need to ensure my findings are based on the actual contents of the files I read. I might ask the explorer to review the AGENTS and the target file, but if the explorer reads it and reports, does that mean I fully read it? Probably not. It seems I should read the files myself via shell, while still utilizing the explorer for a broad scan to identify structure and hotspots. My aim is to output findings without extra summaries, noting exact line numbers, and focusing on a thorough audit rather than code changes.
thinking
**Planning file inspection**

I need to inspect the file for slop words, em dashes, markdown issues, passive voice, notation consistency, dead code, redundancy, transitions, and typography. It’s crucial to find every single issue comprehensively. I might run a regex search for specific patterns and read through the entire file while capturing line numbers. I should start by updating my commentary and perhaps refining the plan. It seems necessary to provide clear commentary before diving into exploration.
codex
Using `deep-beilinson-audit` for this turn because the request is an adversarial manuscript audit with exact fixes. I’m opening the skill, then I’ll read the full target file and verify each finding against the source before I report anything.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
**Gathering line counts and snippets**

I'm thinking about using the `rg -n` command along with `wc -l` to gather line counts, and also using `sed` for pulling relevant snippets from some files. It sounds like a practical way to get both the number of lines and key pieces of text. I need to make sure I'm applying these tools correctly to get the best results. Let's explore combining these commands effectively!
codex
I’ve loaded the audit workflow. Next I’m grounding the audit surface against the repo’s live constitution files, then I’ll read `chapters/theory/chiral_koszul_pairs.tex` in full and verify pattern matches with exact line numbers.
exec
/bin/zsh -lc 'rg -n "AP29|AP106|AP109|AP121|Wrong Formulas Blacklist|Pre-Edit Verification Protocol" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "chiral_koszul_pairs|Koszul pairs|koszul pairs" chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
170:### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits
283:## Wrong Formulas Blacklist
352:- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
519:**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.
550:AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
552:AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
573:## Pre-Edit Verification Protocol
790:AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
967:1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE section (HZ-1 through HZ-10) and run the Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.
 succeeded in 51ms:
    5986 chapters/theory/chiral_koszul_pairs.tex
 succeeded in 52ms:
metadata/theorem_registry.md:71:| `chapters/theory/chiral_koszul_pairs.tex` | 47 |
metadata/theorem_registry.md:227:| `thm:recognition-koszul-pairs` | `theorem` | 6689 | Recognition theorem for finite chiral Koszul pairs |
metadata/theorem_registry.md:386:#### `chapters/theory/chiral_koszul_pairs.tex` (47)
metadata/theorem_registry.md:399:| `thm:bar-concentration` | `theorem` | 1047 | Bar concentration for Koszul pairs |
metadata/theorem_registry.md:435:| `thm:curved-koszul-pairs` | `theorem` | 5242 | Curved Koszul pairs |
metadata/theorem_registry.md:461:| `thm:koszul-resolution-module` | `theorem` | 2582 | Koszul pairs simplify resolutions |
chapters/connections/concordance.tex:326: The Kodaira--Spencer map is constructed for all Koszul pairs
chapters/connections/concordance.tex:5901:$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:

thinking
**Planning efficient reading strategy**

I think I need to set up line numbers for reading, maybe in batches of 1-500 lines. Using a parallel approach could work, but I have to be mindful of the output length. I could consider generating an explorer agent for summarizing sections, but I also want to read them myself. Sequentially reading seems best for now. Additionally, I need to scan for patterns that include slop words, em dashes, backticks, TODOs, labels, and symbols like \kappa and Omega.
codex
The target chapter is large, so I’m reading it in numbered chunks before I classify anything. After the full pass, I’ll run targeted greps for the audit categories and then re-read each hit in context to eliminate false positives.
exec
/bin/zsh -lc "sed -n '540,560p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '780,800p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '386,470p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5888,5912p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

**operadic** (AP65, AP81, AP82, AP83, AP84, AP85, AP88, AP103, AP104): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebra structures: Lie^c (Harrison, coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered configs); R-matrix descent relates. B_{Com}(A) is coLie, NOT cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.

**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).

**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.

### BEFORE WRITING PROSE

AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
AP111: No "What this chapter proves" blocks. Restructure instead.
AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
**Prose laws**: (1) No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (2) No hedging where math is clear. (3) No em dashes; use colons, semicolons, or separate sentences. (4) No passive voice hedging. (5) Every paragraph forces the next. (6) State once, prove once. (7) Scope always explicit. (8) Comparison with prior work: one sentence per paper.

### AFTER EVERY EDIT

AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
 succeeded in 52ms:
AP80: Engine without test file -> verify BOTH exist after every agent completion.
AP135: q-expansion coefficients. 1/eta(tau)^r has r-coloured partition numbers p_{-r}(n), NOT simpler sequences. r=2: (1,2,5,10,20,...) bicoloured partitions, NOT triangular (1,3,6,10,...). OEIS lookup before hardcoding.
AP140: Koszul conductor vs local constant. K=c+c' is a GLOBAL duality invariant. Ghost numbers, grading shifts, normalization factors are LOCAL. K_BP=196, not 2.

### Empirical (AP116-AP123, from 150-commit error archaeology)
AP116: Summation boundary verification. After writing sum_{j=a}^{b}, substitute smallest index. H_N=sum_{j=1}^{N}, NOT N-1. Off-by-one is the #1 formula error that passes visual inspection.
AP117: Differential form type. Connection is r(z)dz, NOT r(z) d log(z). KZ=sum r_{ij} dz_{ij}. Arnold d log(z_i-z_j) is bar coefficient, not connection. NEVER write d log without verification.
AP118: Genus-1 scalar collapse. Formula at g=1 where matrix=(Im Omega)^{-1} becomes scalar 1/Im(tau) MUST be written in full matrix form. Verify at g=2 with 2x2 period matrix.
AP119: Convergent vs divergent series. Before applying Borel summation: verify series is Gevrey-1 (factorial divergence). If |F_{g+1}/F_g| approaches constant (not growing like 2g), series is Gevrey-0. Use direct Pade, NOT Borel.
AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
AP122: Test tolerance proportional to magnitude. For Q~10^17, absolute tol 1e-4 is meaningless. Use relative: abs(computed-expected)/abs(expected) < rtol. Always verify tolerance achievable at float precision.
AP123: Combinatorial enumeration completeness. Verify count against known formula or generating function BEFORE hardcoding. Genus-2 stable graphs: 7 (not 6). Hand enumeration without cross-check = future AP10 violation.

### Deep Empirical (AP124-AP128, from 300-commit deep archaeology)
AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
AP126: Level-stripped r-matrix. Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. The level k survives d-log absorption. Verify: at k=0 the r-matrix MUST vanish. 42+ instances found across all three volumes (12 in first commit, 30 more in full-volume CG sweep). THE MOST VIOLATED AP in the manuscript. After writing ANY r-matrix, verify k=0 -> r=0.
AP127: Cross-refs to migrated chapters. When migrating \input{chapter} between volumes, immediately add \phantomsection\label{} stubs for EVERY label in the migrated file, and grep for all \ref{} pointing to those labels. Never leave a bare \ref to a label that no longer exists in the build.
AP128: Engine-test synchronized to same wrong value. When correcting a compute engine formula, NEVER update test expectations from engine output. Derive correct expected value INDEPENDENTLY (different formula, limiting case, literature). Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.
 succeeded in 53ms:
#### `chapters/theory/chiral_koszul_pairs.tex` (47)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 267 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 294 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 314 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 342 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 417 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 682 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 760 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 815 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 859 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1047 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1159 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1193 | Converse: chiral Koszulness implies formality |
| `thm:ext-diagonal-vanishing` | `theorem` | 1263 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1300 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1326 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1350 | Kac--Shapovalov criterion for simple quotients |
 succeeded in 53ms:
$x=1/(k{+}4)$ (Feigin--Frenkel dual levels); pole at $x=1/2$
(critical level $k=-2$, where the center acquires opers).

For $\mathcal W_3$: two zeros at $x_1=1/\kappa_c$ and
$x_2=(5c{+}22)/(\kappa_c(5c{+}22){+}48)$, reflecting the
two-dimensional deformation space $(T,W)$. At $c=50$:
$x_1\to\infty$, $x_2=3/2$.

For $\beta\gamma$: the unique standard family with
$\kappa<0$. Branch point at $x=-1/2$; the genus tower has
alternating signs.

\emph{Duality.}
$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
the spectral discriminant is self-dual. For
$\widehat{\mathfrak{sl}}_2$: the zero at $1/k$ corresponds
to level~$k$; the zero at $1/(k{+}4)$ corresponds to the
dual level $-k-4$. The product of the two zeros is
$1/(k(k{+}4))$; their sum is $(2k{+}4)/(k(k{+}4))=2/k+2/(k{+}4)
\to 0$ as $k\to\infty$.


thinking
**Planning file reading strategy**

I need to read the target file completely. My plan is to do chunk reads and perhaps use parallel processing with three chunks at a time. I should manage the max output tokens, aiming for around 7000 tokens. 

Initially, I thought of reading 500-line chunks, which would give me about 12 chunks. After some consideration, doing 300 lines at a time sounds better, leading to around 20 chunks. I’ll have to keep track of everything closely to avoid truncation and detect any issues early on.
thinking
**Planning file reading approach**

Reading through the entire huge file manually feels like a lot, but it’s doable. I can make the process easier by supplementing my efforts with targeted greps. To begin, I’ll start by focusing on the first 1500 lines, divided into three chunks. That way, I can manage it more effectively while still getting a comprehensive view of the contents. This approach seems like a good balance to tackle the task without overwhelming myself!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1,500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1001,1500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '501,1000p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
  1001	is the bar cohomology of the commutative chiral algebra
  1002	$\operatorname{Sym}^{\mathrm{ch}}(V)$.
  1003	
  1004	Since $\operatorname{Sym}^{\mathrm{ch}}(V)$ is a free
  1005	commutative algebra, it is Koszul with Koszul dual
  1006	the exterior coalgebra $\Lambda^{\mathrm{c}}(V^*)$
  1007	(Priddy's theorem applied to the chiral setting,
  1008	cf.\ Remark~\ref{rem:classical-to-chiral-koszul}).
  1009	Therefore:
  1010	\begin{equation}\label{eq:e1-page-exterior}
  1011	E_1^{p,q} = H^{p+q}(\barBgeom^p(\operatorname{Sym}^{\mathrm{ch}}(V)))
  1012	= \begin{cases}
  1013	\Lambda^p(V^*) & \text{if } q = 0, \\
  1014	0 & \text{if } q \neq 0.
  1015	\end{cases}
  1016	\end{equation}
  1017	The $E_1$ page is \emph{concentrated in the row $q = 0$}.
  1018	In particular, for $\widehat{\fg}_k$ with
  1019	$V = \fg \otimes t^{-1}\bC[t^{-1}]$:
  1020	\[
 succeeded in 53ms:
   501	The first bijection sends $\tau \in \mathrm{Tw}(\cC, \cA)$
   502	to the algebra morphism $g_\tau\colon \Omega_X(\cC) \to \cA$
   503	defined on cogenerators by $g_\tau(s^{-1} c) = \tau(c)$; the
   504	MC equation for $\tau$ is equivalent to $g_\tau$ commuting
   505	with differentials
   506	(the same proof as \cite[Theorem~2.2.7]{LV12}).
   507	The second bijection sends $\tau$ to the coalgebra morphism
   508	$f_\tau\colon \cC \to \bar{B}_X(\cA)$ defined dually.
   509	The universal property of the bar construction as a cofree
   510	coalgebra ensures uniqueness of factorization.
   511	\end{proof}
   512	
   513	\begin{remark}[Why the MC equation is Stokes' theorem]
   514	\label{rem:MC-is-Stokes}
   515	\index{Maurer--Cartan equation!geometric origin}
   516	The Maurer--Cartan equation $d\tau + \tau \star \tau = 0$ is
   517	not an imposed axiom. It is forced by the geometry of
   518	$\overline{C}_2(X)$. The convolution
   519	$(\tau \star \tau)(x) = \mu \circ (\tau \otimes \tau)
   520	\circ \Delta(x)$ evaluates the two-point OPE: it extracts
codex
The first quarter confirms the chapter is not a light cosmetic pass: the opening, theorem staging, and several exposition blocks already show audit targets. I’m continuing through the full file before I lock the finding list so I can catch repeats and second-order drift.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2001,2500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1501,2000p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2501,3000p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2001	bar-relevant range? The Li--bar criterion asks: does the
  2002	\emph{geometry} of the associated variety~$X_V$ force those
  2003	null vectors to produce off-diagonal bar cohomology?
  2004	
  2005	The gain is maximal when $X_V \neq \{0\}$ and one can
  2006	separately establish diagonal concentration on the reduced
  2007	Li--bar page, possibly guided by geometric input from a
  2008	symplectic resolution. Minimal-orbit levels are the first
  2009	test case where the reduced geometry suggests concentration, but
  2010	an unconditional Koszul theorem still requires the extra
  2011	reducedness and reduced Li--bar concentration hypotheses recorded in
  2012	Corollary~\ref{cor:minimal-orbit-koszul}.
  2013	\end{remark}
  2014	
  2015	\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
  2016	\label{thm:koszul-equivalences-meta}
  2017	\index{Koszul property!equivalences of characterizations|textbf}
  2018	
  2019	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  2020	with PBW filtration $F_\bullet$.
 succeeded in 52ms:
  1501	\index{Koszul property!rationality not sufficient}
  1502	\index{rational vertex algebra!limitations of rationality}
  1503	Rationality, $C_2$-cofiniteness, and semisimplicity of the Zhu
  1504	algebra are strong \emph{finiteness} inputs, but they do not by
  1505	themselves imply chiral Koszulness in the sense used here.
  1506	The obstruction is categorical: the ordinary positive-energy module
  1507	category $V$-$\mathrm{gmod}$ controls Zhu theory and conformal
  1508	blocks, whereas Ext groups in the
  1509	chiral/factorization module setting are computed via the bar complex
  1510	\textup{(}Corollary~\ref{cor:bar-computes-ext}\textup{)}.
  1511	The manuscript does not identify these two Ext theories for
  1512	general rational vertex algebras.
  1513	
  1514	Consequently, the implication
  1515	\[
  1516	\text{ordinary semisimplicity}
  1517	\;\Longrightarrow\;
  1518	H^{>0}\!\bigl(\barBgeom(V)\bigr)=0
  1519	\]
  1520	is \emph{not} established here. For simple quotients at
 succeeded in 51ms:
  2501	\bottomrule
  2502	\end{tabular}
  2503	\end{center}
  2504	
  2505	\medskip\noindent
  2506	\emph{Mechanism.}
  2507	For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
  2508	Gaussian: the Heisenberg bracket
  2509	$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
  2510	VOAs the shadow obstruction tower terminates at weight~$2$ by
  2511	Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
  2512	all higher tree sums vanish.
  2513	For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
  2514	three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
  2515	\textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
  2516	tower terminates at depth~$3$ because $S_r = 0$ for $r \geq 4$.
  2517	For class~$C$\textup{:}
  2518	the cubic shadow vanishes by weight parity of the $\gamma$
  2519	generator \textup{(}conformal weight~$0$\textup{)}, while the
  2520	quartic contact invariant
codex
I’ve reached the middle of the file. The chapter has a lot of prose scaffolding and explanatory remarks, which is exactly where the cosmetic defects concentrate, so I’m continuing the full read and then I’ll do a second pass only on concrete line hits.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3001,3500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4001,4500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3501,4000p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3001	\index{Koszul property!convolution algebra formality}
  3002	\index{formality!convolution algebra characterization}
  3003	
  3004	A chiral algebra $\cA$ is chirally Koszul if and only if the modular
  3005	convolution algebra $\gAmod$ satisfies:
  3006	\begin{enumerate}[label=\textup{(\roman*)}]
  3007	\item The shadow algebra
  3008	 $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
  3009	 concentrated in degree~$2$:
  3010	 $\cA^{\mathrm{sh}}_{r,g} = 0$ for $r \geq 3$, $g = 0$.
  3011	\item The bar spectral sequence
  3012	 $E_1^{p,q} = H^q(F^p\gAmod/F^{p+1}\gAmod)$ degenerates
  3013	 at~$E_2$.
  3014	\item The genus-$0$ convolution algebra
  3015	 $\mathfrak{g}^{(0)}_\cA$ is formal as a dg Lie algebra.
  3016	\end{enumerate}
  3017	These three conditions are equivalent to each other and to the ten
  3018	unconditional equivalences~\textup{(i)--(x)} in
  3019	Theorem~\textup{\ref{thm:koszul-equivalences-meta}}.
  3020	\end{proposition}
 succeeded in 52ms:
  3501	
  3502	\begin{definition}[Primitive defect series; \ClaimStatusProvedHere]
  3503	\label{def:primitive-defect-series}
  3504	\index{primitive defect series|textbf}
  3505	\index{strong generators!primitive defect}
  3506	
  3507	For a chiral algebra with declared strong generators of conformal
  3508	weights $d_1, \ldots, d_s$, the \emph{primitive defect series} is
  3509	\begin{equation}
  3510	\label{eq:primitive-defect-series}
  3511	\Delta^{\mathrm{prim}}_\cA(t) \;:=\;
  3512	G_\cA(t) - \sum_{i=1}^s t^{d_i - 1}.
  3513	\end{equation}
  3514	The defect vanishes identically for quadratic (or free-like)
  3515	behaviour: $\Delta^{\mathrm{prim}}_\cA = 0$ when the
  3516	declared generators account for all quasi-primaries at every
  3517	weight. Nonzero defect detects precisely those weights at
  3518	which nonquadratic OPEs force new primitive cumulants beyond the
  3519	declared generators.
  3520	\end{definition}
 succeeded in 53ms:
Total output lines: 500

  4001	
  4002	The \emph{differential} $d_!: \mathcal{A}_2^! \to \mathcal{A}_2^![1]$ is the unique coderivation determined by its values on generators. For $\phi_i^* \in \mathcal{V}^{\vee}$:
  4003	\[d_!(\phi_i^*) = -\sum_{\substack{j,k,m \\ m \geq 1}} \frac{C_{ij}^{k,m}}{(m-1)!} \cdot \phi_j^* \boxtimes \phi_k^* \boxtimes \omega_X^{\otimes (m-1)}\]
  4004	
  4005	More precisely: the differential encodes the \emph{residue structure} of OPEs in $\mathcal{A}_2$. If $\phi_i(z)\phi_j(w)$ has a pole of order $m$ with residue $C_{ij}^{k,m}\phi_k$, then:
  4006	\[d_!(\phi_i^*) \text{ contains the term } -C_{ij}^{k,m} \cdot (\phi_j^* \boxtimes \phi_k^*) \otimes \eta^{\otimes(m-1)}\]
  4007	where $\eta = d\log(z_1 - z_2) = \frac{dz_1 - dz_2}{z_1 - z_2}$ is the standard logarithmic form.
  4008	
  4009	\medskip
  4010	\noindent\emph{Step 4 (Counit):}
  4011	\[\epsilon: \mathcal{A}_2^! \to \mathcal{O}_X, \quad \epsilon(\phi_{i_1}^* \boxtimes \cdots \boxtimes \phi_{i_n}^*) = 
  4012	\begin{cases}
  4013	1_X & \text{if } n = 0 \\
  4014	0 & \text{if } n > 0
  4015	\end{cases}\]
  4016	\end{definition}
  4017	
  4018	\begin{remark}[Independence]\label{rem:independence-construction}
codex
The later sections are worse on the cosmetic surface than the early theorem lane: there are line-level style violations, overt signpost prose, and some notation formatting drift. I’m finishing the last read now, then I’ll verify every candidate hit in context before I rank them.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5001,5500p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5501,5986p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4501,5000p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5001	$\mathcal{V} = \mathcal{D}\text{-mod}(X)$ equipped with the chiral
  5002	tensor product~$\otimes^{\mathrm{ch}}$. We verify the required
  5003	hypotheses on~$\mathcal{V}$:
  5004	\begin{enumerate}
  5005	\item \emph{Stable presentable $\infty$-category.}
  5006	The $\infty$-category $\mathcal{D}\text{-mod}(X)$ is stable and
  5007	presentable by \cite[Chapter~I.3]{GR17}; see also
  5008	\cite[Proposition~5.5.3.6]{HA} and \cite[§1.1]{HA}.
  5009	\item \emph{Symmetric monoidal structure.}
  5010	The chiral tensor product endows $\mathcal{D}\text{-mod}(X)$ with a
  5011	symmetric monoidal structure by \cite[3.4.10]{BD04}. While
  5012	$\otimes^{\mathrm{ch}}$ does not in general coincide with the
  5013	$!$-tensor product, it does define a symmetric monoidal structure on
  5014	the $\infty$-categorical enhancement, as established in
  5015	\cite[Chapter~IV.5]{GR17}.
  5016	\item \emph{Exactness of base change
  5017	\textup{(}Lemma~\textup{\ref{lem:operadic-koszul-transfer}},
  5018	Step~\textup{2)}.}
  5019	The unit functor $k\text{-}\mathrm{Mod} \to \mathcal{D}\text{-mod}(X)$
  5020	is exact because $\mathcal{D}\text{-mod}(X)$ is $k$-linear and
 succeeded in 50ms:
  4501	This is a curved coalgebra, a consequence of the central extension.
  4502	\end{example}
  4503	
  4504	%----------------------------------------------------------------
  4505	% SUBSECTION: W_3 ALGEBRA - COMPLETE
  4506	%----------------------------------------------------------------
  4507	
  4508	\subsection{\texorpdfstring{$W_3$ algebra: explicit calculation}{W-3 algebra: explicit calculation}}
  4509	
  4510	\begin{example}[\texorpdfstring{$W_3$}{W3} algebra: full completion]
  4511	\label{ex:w3-completion-full}
  4512	
  4513	The $W_3$ algebra is generated by $T(z)$ (weight 2) and $W(z)$ (weight 3), with OPEs as in Definition~\ref{def:w3-algebra}; the complete $W$--$W$ expansion is given in Theorem~\ref{thm:w-w-ope-complete}. In particular, $\Lambda(w) = :T(w)T(w): - \frac{3}{10}\partial^2 T(w)$ is the quasi-primary composite field
  4514	(the unique normal ordering prescription ensuring $T(z)\Lambda(w) \sim \frac{4\Lambda(w)}{(z-w)^2} + \frac{\partial\Lambda(w)}{z-w} + \text{reg}$, with no $(z-w)^{-3}$ term).
  4515	
  4516	\medskip
  4517	\noindent\emph{Step 1: Bar Complex Structure}
  4518	
  4519	\[\bar{B}^0(W_3) = \mathbb{C}\]
  4520	\[\bar{B}^1(W_3) = \Gamma(\overline{C}_2, T^{\boxtimes 2} \otimes \eta) \oplus \Gamma(\overline{C}_2, W^{\boxtimes 2} \otimes \eta) \oplus \Gamma(\overline{C}_2, T \boxtimes W \otimes \eta)\]
 succeeded in 52ms:
  5501	$\fg$, the Kazhdan--Lusztig equivalence is the genus-zero fibre
  5502	at affine~$\widehat{\fg}$ with integral level, and BFM is the
  5503	geometric fibre over the affine Grassmannian where the Koszul
  5504	dual is governed by~$\fg^\vee$.
  5505	\end{remark}
  5506	
  5507	
  5508	% ================================================================
  5509	% SECTION 8.6: INTERCHANGE OF STRUCTURES
  5510	% ================================================================
  5511	
  5512	\section{Interchange of structures under Koszul duality}
  5513	
  5514	\subsection{Generators and relations}
  5515	
  5516	\begin{theorem}[Structure exchange; \ClaimStatusProvedHere]\label{thm:structure-exchange}
  5517	Under Koszul duality between $(\mathcal{A}_1, \mathcal{A}_2)$:
  5518	\begin{enumerate}
  5519	\item \emph{Generators $\leftrightarrow$ Relations:}
  5520	\[\mathrm{Gen}(\mathcal{A}_1) \leftrightarrow \mathrm{Rel}(\mathcal{A}_2)^{\perp}\]




thinking
**Conducting the audit**

I need to run an audit on the requested categories, focusing on AI-related terminology, em dashes, and markdown usage. I might search for undefined macros, checking for backticks and special characters that could signal issues. It’s essential to look for signpost phrases like "We now" and gather line numbers for each finding. Although the user requested cosmetic and aesthetic consistency, I'll ensure we read the entire file carefully and report all findings accurately, even if it ends up being dozens.
thinking
**Running the audit search**

I'm planning to run a search for AI slop words, banned patterns, and specific elements like em dashes, backticks, and markdown formats like bold and italics. I'll also check for signpost phrases like "we now" and any usage of bare \kappa. The user specifically requested to identify any bare \kappa that aren't associated with a family, which I need to inspect closely. While there are many generic instances like `\kappa(\cA)`, the notational consistency is key, especially in avoiding any undefined macros. We have to ensure that everything aligns with their requests!
thinking
**Searching for undefined macros**

I need to look for occurrences of `\Omega/z` and possibly `k\Omega/z`, especially around line 3225. It’s essential to catch any bare `\Omega/z` instances. I’m thinking it might help to compile the document locally to detect undefined macros, though it could get heavy. I can try using `rg` for `\text{}` as well. Identifying undefined macros could be easiest by searching for macros that are used only once, but that’s a bit tricky. I could run a command like `rg -o '\\[A-Za-z]+' file | sort | uniq -c` to cross-reference occurrences, but it might be overwhelming!
thinking
**Considering editing and updates**

I'm deciding whether to use pre-edit verification for agents, but it seems like I'm not in the editing phase right now. I could consider filling something in, but I'm not sure it's needed. Maybe using an update plan would be a good choice since there's a substantial context to cover. However, I think we already provided updates, so I should continue and run targeted searches across the file instead.
codex
I’ve finished the full-file read. Now I’m reducing the audit to verified line hits: pattern searches for slop vocabulary, forbidden typography, markdown, dead code, signpost transitions, hedging, and notation markers, then I’ll re-open each hit in context so the final list has no false positives.
exec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n --pcre2 "—|---" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "`|'"\\*\\*|_[A-Za-z]\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "TODO|FIXME|todo|fixme|RECTIFICATION-FLAG" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1182:%%% ---------------------------------------------------------------
1184:%%% ---------------------------------------------------------------
2933: & logarithmic & $4$ & Open & --- & unknown \\
3956:%----------------------------------------------------------------
3958:%----------------------------------------------------------------
4036:%----------------------------------------------------------------
4038:%----------------------------------------------------------------
4130:%----------------------------------------------------------------
4132:%----------------------------------------------------------------
4423:%----------------------------------------------------------------
4425:%----------------------------------------------------------------
4504:%----------------------------------------------------------------
4506:%----------------------------------------------------------------
4627:%----------------------------------------------------------------
4629:%----------------------------------------------------------------
4678:%----------------------------------------------------------------
4680:%----------------------------------------------------------------
4738:%----------------------------------------------------------------
4740:%----------------------------------------------------------------
 exited 1 in 52ms:
zsh:1: unmatched "
 succeeded in 52ms:
1129:% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
exec
/bin/zsh -lc "rg -n \"\\*\\*|"'`" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\b\\\\kappa\\b|\\\\Omega/z|\\\\Omega/z|\\\\Omega\\\\/z|\\\\Omega/z\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "We now|we now|The chapter proceeds|This chapter|What this chapter|we record here|We verify each|We prove each|The proof proceeds|It can be shown|one might expect|it seems reasonable|it is natural to|we give a geometric refinement|We construct|We record" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:1: unmatched "
 exited 2 in 51ms:
rg: regex parse error:
    (?:\b\kappa\b|\Omega/z|\Omega/z|\Omega\/z|\Omega/z)
         ^^
error: unrecognized escape sequence
 succeeded in 51ms:
136:The chapter proceeds in three stages.
1663:by non-degeneracy of a bilinear form weight by weight. We now
3220:sequences. We now record a Poisson-geometric characterization that
3825:see Chapter~\ref{chap:yangians}. We record here only the Koszul-duality-specific results.
4061:We verify each axiom using the explicit formulas from Definition~\ref{def:intrinsic-koszul-dual}.
4157:We construct $\Phi$ explicitly through \emph{configuration space integration}, following Kontsevich's geometric approach in five steps.
4289:The proof proceeds through three logically independent stages, each relying only on the output of the preceding stage and on configuration space geometry.
4399:\noindent\emph{Logical independence.} We record that the argument is circularity-free:
4880:The proof proceeds in three steps.
5257:We verify each property in turn.
5532:We prove each item from the quadratic duality formalism lifted to the chiral setting.
5568:We prove each item.
5951:This chapter provides the following results used by later chapters:

thinking
**Exploring regex for quotes**

I need to be careful with the regex for quotes. Using a fixed string might simplify things. I’m thinking of searching for bare `\kappa`, but maybe that’s too many occurrences. Perhaps using Perl or grep would be wise. I could try `rg -n '\\kappa' file` to see where it appears and later inspect those contexts. It might also be necessary to fix `\Omega/z`. Let’s plan for multiple regex approaches!
codex
I have concrete signpost hits now. I’m separating genuine AP109/AP106 violations from acceptable local proof scaffolding, then I’ll do the notation pass and dead-code pass so the final list stays precise.
exec
/bin/zsh -lc "rg -n '  +|\\.  |,  |;  |:\\s\\s+' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega\\\\/z|Omega/z|\\\\Omega' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'it can be shown|one might expect|it seems reasonable|it is natural to|appears to|suggests that|we expect|can be seen' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 51ms:
49:$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
165:$\Omega_X(\bar{B}_X(\mathcal{H}_k)) \xrightarrow{\;\sim\;} \mathcal{H}_k$
213: $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
262: $\Omega_X(\cC)$.
268:$\bar{B}_X(\cA)$ and cobar $\Omega_X(\bar{B}_X(\cA))$ exist as
270:$\Omega_X(\bar{B}_X(\cA)) \to \cA$ is a quasi-isomorphism
293:where $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ is the
304:$\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ shifted by~$[-1]$:
417: $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$
452:By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
480:\operatorname{Hom}_{\mathrm{alg}}(\Omega_X(\cC), \cA)
495:$\iota\colon \cC \to \Omega_X(\cC)$
502:to the algebra morphism $g_\tau\colon \Omega_X(\cC) \to \cA$
573:Dually, the cobar construction $\Omega_X(C)$ together with
574:$\iota_{\mathrm{can}} \colon C \to \Omega_X(C)$ is terminal among
638:\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
640:\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
666:\simeq \Omega_X(\cC_2)
670:$\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
734:\[\bar{B}^{\text{ch}}(\mathcal{BC})_n = \Gamma\left(\overline{C}_n(X), (b \oplus c)^{\boxtimes n} \otimes \Omega^*_{\log}\right)\]
 succeeded in 52ms:
18:satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
109:the modular characteristic $\kappa(\cA)$, which measures
114:and the critical discriminant $\Delta = 8\kappa S_4$, whose
117:At genus zero all three collapse: $\kappa$ plays no role,
532:$\kappa(\cA) \cdot \omega_g$, and $\tau$ becomes curved
989:+ k\kappa^{ab}/(z-w)^2$
991:(the bracket $f^{ab}_c J^c$ and level term $k\kappa^{ab}$ are
1433:At generic level ($\kappa \neq 0$), the curvature of the bar
1652:bracket $[J^a, J^b]_\star = f^{ab}_c J^c + k\kappa^{ab}$ lies in
2230:$\barB_\kappa$ is conservative and preserves totalizations of
2231:$\barB_\kappa$-split cosimplicial objects.
2232:Conservativity: $\barB_\kappa$ detects quasi-isomorphisms on the
2248:$\barB_\kappa$ is conservative (detecting quasi-isomorphisms).
2445:governed by the discriminant $\Delta = 8\kappa S_4$.
2528:$\Delta = 8\kappa S_4 \neq 0$ forces all higher operations to be
2552:= 2\kappa/\kappa = 2$, independent of~$c$;
2553:$S_4 = 10/[c(5c{+}22)]$ and $\Delta = 8\kappa S_4 = 40/(5c{+}22) \neq 0$
2873:Cross-family consistency checks: $\kappa$ additivity,
3558: $D_\cA$, $\kappa(\cA)$, $\Theta_\cA$, $r_\cA(z)$; depends
3562:data (it sends $\kappa_c$ to $\kappa_{26-c}$) but does not
 exited 1 in 51ms:

codex
The banned-vocabulary pass is clean, which narrows this to structure, signposting, dead code, markdown-like LaTeX, and notation/typography drift. I’m now verifying the remaining edge cases individually rather than broad-searching, because most of the risk is in subtle local misuse.
exec
/bin/zsh -lc "rg -n '\\*\\*' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n '\\"'`'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{' chapters/theory/chiral_koszul_pairs.tex | cut -d: -f1,2,3 | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 50ms:
1439:Accordingly, the parenthetical ``including $k = -h^\vee$'' in
1617:The ``null vector at weight~$15$'' reported in earlier analyses is a
4030:\item Any notion of ``Koszul pair''
4066:This follows from the \emph{cofree construction}. For the cofree coalgebra $T^c(\mathcal{V}^{\vee})$, coassociativity is automatic; it is part of the universal property defining ``cofree''.
4333:It does not invoke the bar construction, nor any notion of ``Koszul pair.''
 succeeded in 61ms:
2:\label{chap:koszul-pairs}
156:\label{sec:chiral-twisting-data}
200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
225:\label{rem:explicit-twisted-differential}
229:\begin{equation}\label{eq:chiral-twisted-differential-L}
234:\begin{equation}\label{eq:chiral-twisted-differential-R}
252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
266:\begin{remark}[Construction versus resolution]\label{rem:construction-vs-resolution}
286:\label{lem:twisted-product-cone-counit}
313:\label{lem:twisted-product-cone-unit}
333:\label{lem:filtered-comparison}
361:\label{lem:filtered-comparison-unit}
400:\label{thm:fundamental-twisting-morphisms}
412:\item\label{ftm:koszul}
415:\item\label{ftm:counit}
419:\item\label{ftm:unit}
424:\item\label{ftm:acyclic}
472:\label{cor:three-bijections}
477:\begin{align}\label{eq:three-bijections}
514:\label{rem:MC-is-Stokes}
exec
/bin/zsh -lc "sed -n '3216,3225p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3819,3826p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1658,1668p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '132,141p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

The Koszulness meta-theorem
(Theorem~\ref{thm:koszul-equivalences-meta}) characterizes chiral
Koszulness intrinsically, through the bar complex and its spectral
sequences. We now record a Poisson-geometric characterization that
applies on the affine Kac--Moody locus and is logically independent of
the PBW spectral sequence.

The classical $r$-matrix
$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
 succeeded in 53ms:

The Yangian $Y(\mathfrak{g})$ and affine Yangian $Y_{\hbar}(\widehat{\mathfrak{g}})$
provide examples where Koszul duality manifests as self-duality.

For the RTT definition of $Y(\mathfrak{g})$, its Hopf structure, affine
Yangian, connection to quantum groups, and physical interpretation,
see Chapter~\ref{chap:yangians}. We record here only the Koszul-duality-specific results.

 succeeded in 53ms:
\subsection{The Li--bar spectral sequence and geometric Koszulness}
\label{subsec:li-bar-geometric-koszulness}

The Kac--Shapovalov criterion
(Theorem~\ref{thm:kac-shapovalov-koszulness}) detects Koszulness
by non-degeneracy of a bilinear form weight by weight. We now
give a geometric refinement: the Li filtration on~$\cA$ induces a
spectral sequence on the bar complex whose $E_1$~page is the bar
complex of a \emph{commutative Poisson algebra}, and Koszulness
is controlled by the geometry of the associated variety~$X_\cA$.

 succeeded in 53ms:
$R$-matrix, linking the Koszul pairs of this chapter to the
Drinfeld--Kohno bridge of
Chapter~\ref{chap:koszul-pair-structure}.

The chapter proceeds in three stages.
\S\ref{sec:chiral-twisting-data}ff.\ extracts from the
Heisenberg example the general notion of chiral twisting data
and formulates the PBW recognition criterion. The chiral Koszul
pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
and the full bar-cobar adjunction and inversion on the Koszul



thinking
**Identifying code issues**

I need to determine if any commented-out sections are more than 10 lines long. There are several two-line separators, but they're not dead code. I noticed an eight-line rectification comment that could be considered dead, even though it's under 10 lines. The user asked about dead code, like unused labels and TODOs. I might want to search for any unused labels within the file since that’s the user's focus. A script could help identify these labels not referenced anywhere.
thinking
**Scanning for unused labels**

I need to scan the repository, but since the user specifically asked to audit the target file, I should focus on that. I have to check for unused labels, but they could potentially be used elsewhere in the repo. To identify these, I could write a script using Python or shell commands to find labels defined in the file that have zero references. Using a simple shell command might be more efficient for this task.
thinking
**Evaluating shell options**

I might need to use a shell command, considering something like using `while read label; do rg -n --fixed-strings "\\ref{$label}" chapters appendices metadata ???`. There could be variations like `\autoref`, `\cref`, and others for cross-referencing that I should check for globally. Hm, maybe a ruby script would simplify this? I’m pondering if I should count duplicates, though it may only be cosmetic.

The user is focused on dead code and identifying duplicate labels, especially since multiple labels exist on specific definition lines. I should verify if any are unused aliases. Let's search for those labels like `def:koszul-dual-coalgebra`.
codex
I’m checking label hygiene now, because the later half of the file introduces alias labels and duplicated theorem handles. If any of those names are unreferenced across the manuscript, they count as dead surface, not harmless metadata.
exec
/bin/zsh -lc 'for lbl in prob:circularity const:wn-general rem:comparison-classical sec:feynman_genus_g; do echo "LABEL $lbl"; rg -n --fixed-strings "$lbl" . | sed '"'s#"'^./##'"'; done" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for lbl in def:koszul-dual-coalgebra def:intrinsic-koszul-dual def:koszul-dual-chiral thm:chiral-koszul-duality rem:convergence-pro-nil rem:convergence-pronilpotent ex:affine-yangian-kp ex:yangian-completion; do echo "LABEL $lbl"; rg -n --fixed-strings "$lbl" . | sed '"'s#"'^./##'"'; done" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{def:intrinsic-koszul-dual\\}|\\\\label\\{def:koszul-dual-coalgebra\\}|\\\\label\\{def:koszul-dual-chiral\\}|\\\\label\\{thm:chiral-koszul-duality\\}|\\\\label\\{rem:convergence-pro-nil\\}|\\\\label\\{rem:convergence-pronilpotent\\}|\\\\label\\{ex:affine-yangian-kp\\}|\\\\label\\{ex:yangian-completion\\}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
3962:\begin{definition}[Koszul dual chiral coalgebra: intrinsic construction]\label{def:koszul-dual-coalgebra}
3963:\label{def:intrinsic-koszul-dual}
3964:\label{def:koszul-dual-chiral}
4138:\label{thm:chiral-koszul-duality}
4684:\begin{example}[Affine Yangian]\label{ex:affine-yangian-kp}
4685:\label{ex:yangian-completion}
4818:\begin{remark}[Convergence role of pro-nilpotence]\label{rem:convergence-pro-nil}
4819:\label{rem:convergence-pronilpotent}
 succeeded in 256ms:
metadata/label_index.json:3202:  "const:wn-general": {
audit_campaign_20260412_231034/F04_kappa_WN.md:1520:\label{const:wn-general}
chapters/theory/chiral_koszul_pairs.tex:4634:\label{const:wn-general}
LABEL rem:comparison-classical
wave2_audit_20260413_001942/S13_concordance_to_body.md:2207:`rem:comparison-classical` | none
metadata/label_index.json:30082:  "rem:comparison-classical": {
metadata/label_index.json:30086:  "rem:comparison-classical-fm": {
compute/audit/d_module_purity_converse_2026_04_05.md:397:   collapses at E_2 (rem:comparison-classical, line 3299). In this case, the
chapters/theory/chiral_koszul_pairs.tex:4408:\begin{remark}[Comparison with classical Koszul duality]\label{rem:comparison-classical}
chapters/theory/configuration_spaces.tex:2232:\label{rem:comparison-classical-fm}
LABEL sec:feynman_genus_g
wave2_audit_20260413_001942/S13_concordance_to_body.md:2208:`sec:feynman_genus_g` | none
chapters/theory/chiral_koszul_pairs.tex:4759:\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
metadata/label_index.json:38986:  "sec:feynman_genus_g": {
 succeeded in 403ms:
metadata/label_index.json:6862:  "def:intrinsic-koszul-dual": {
metadata/claims.jsonl:2324:{"label": "thm:coalgebra-axioms-verified", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 3785, "title": "Coalgebra structure on \\texorpdfstring{$\\mathcal{A}_2^!$}{A2-dual}", "refs_in_block": ["def:intrinsic-koszul-dual"]}
appendices/notation_index.tex:408:The intrinsic Koszul dual algebra object is Definition~\ref{def:intrinsic-koszul-dual}.
chapters/theory/chiral_koszul_pairs.tex:3963:\label{def:intrinsic-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:4045:The structure $(\mathcal{A}_2^!, \Delta, \epsilon, d_!)$ defined in Definition~\ref{def:intrinsic-koszul-dual} satisfies:
chapters/theory/chiral_koszul_pairs.tex:4061:We verify each axiom using the explicit formulas from Definition~\ref{def:intrinsic-koszul-dual}.
chapters/theory/chiral_koszul_pairs.tex:4184:This coincides with the coproduct defined on $\mathcal{A}_2^!$ in Definition~\ref{def:intrinsic-koszul-dual}.
chapters/theory/chiral_koszul_pairs.tex:4294:Given only the presentation data $(\mathcal{V}, R)$ and the OPE structure constants $C_{ij}^{k,m}$, we define $\mathcal{A}^!$ as in Definition~\ref{def:intrinsic-koszul-dual}:
LABEL def:koszul-dual-chiral
metadata/label_index.json:6906:  "def:koszul-dual-chiral": {
audit_campaign_20260412_231034/T05_thm_C2.md:765:chapters/theory/higher_genus_complementarity.tex:1135:By Koszul duality (Definition~\ref{def:koszul-dual-chiral}), there is a natural pairing:
audit_campaign_20260412_231034/T05_thm_C2.md:1582:By Koszul duality (Definition~\ref{def:koszul-dual-chiral}), there is a natural pairing:
chapters/theory/chiral_koszul_pairs.tex:3964:\label{def:koszul-dual-chiral}
chapters/theory/higher_genus_complementarity.tex:1146:By Koszul duality (Definition~\ref{def:koszul-dual-chiral}), there is a natural pairing:
LABEL thm:chiral-koszul-duality
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:610:/bin/zsh -lc "rg -n '\\\\label\\{(def:geom-cobar-precise|thm:bar-cobar-inversion-qi|thm:bar-cobar-isomorphism-main|thm:bar-modular-operad|thm:genus-induction-strict|thm:FM|thm:normal-crossings|thm:arnold-three|def:conilpotent-complete|def:bar-differential-complete|def:chiral-koszul-pair|conv:regime-tags|conv:bar-coalgebra-identity|thm:completion-necessity|thm:obstruction-quantum|thm:prism-higher-genus|thm:fundamental-twisting-morphisms|prop:universal-twisting-adjunction|def:chiral-twisting-datum|lem:degree-cutoff|def:strong-completion-tower|thm:explicit-theta|def:shadow-postnikov-tower|thm:quantum-complementarity-main|thm:quantum-diff-squares-zero|thm:chiral-koszul-duality|prop:cdg-hom-complex|thm:chiral-hochschild-differential|lem:center-cohomology|lem:deformation-space|lem:period-integral|thm:curvature-central|cor:shadow-extraction|thm:mc2-bar-intrinsic|thm:bar-concentration)\\}' chapters appendices metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:664:chapters/theory/chiral_koszul_pairs.tex:4138:\label{thm:chiral-koszul-duality}
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:1022:   469	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
wave2_audit_20260413_001942/F04_definitions_complementarity.md:1243:   469	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
wave2_audit_20260413_001942/S05_foundations_to_complementarity.md:286:/bin/zsh -lc 'rg -n "cor:bar-cohomology-koszul-dual|thm:chiral-koszul-duality|thm:verdier-duality-config-complete|def:complementarity-complexes|lem:perfectness-criterion|thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|bar cohomology|center local system|Verdier duality on configuration" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:





thinking
**Evaluating unused labels**

It looks like there are several alias labels in the code that aren't referenced anywhere, like `\label{def:koszul-dual-coalgebra}` and `\label{rem:convergence-pro-nil}`. I’m guessing some might be dead code. There are others like `\label{prob:circularity}` and `\label{sec:feynman_genus_g}` that I'm uncertain about. The user wants to address dead code, so I could suggest removing those unused labels but also verify that they’re not used elsewhere. Maybe a targeted search could help check for undefined macros?
thinking
**Addressing undefined macros**

The user is asking about undefined macros, which is tricky without a full build. Compiling just a chapter might not be possible, and running `make fast` could be too extensive. Since the user wants an audit based on what’s actually in the file, I can't just guess about undefined macros. I should be cautious about claiming any undefined macros unless I can verify them through build evidence or open macro definitions. Maybe I could run specific searches to check for suspicious macros and their definitions. It’d be good to have concrete evidence before making any claims.
thinking
**Evaluating build requirements**

I’m considering whether using the build-surface skill is necessary, especially since the user asked about undefined macros. The core task seems to be an audit, but if the task aligns with what build-surface does, it might be useful. I wonder if the logs could help verify findings. Even though compiling might catch undefined control sequences, the user seems to only want a cosmetic audit. Still, running a build could reveal warnings or errors worth checking.
thinking
**Deciding on tools for audit**

I need to detect undefined macros, but it's not immediately clear if using the build-surface skill is necessary since the user's task doesn't explicitly request it. Still, it might be helpful, so I could run a build to check for issues. However, I really need to focus on typography matters like double spaces and mismatched braces. Using tools like `chktex`, `latexmk`, or even `grep` might help identify issues effectively without relying on the skill. Let’s see what I can install!
thinking
**Identifying typographic issues**

I expect to find some specific line issues manually. For instance, line 1409 has a stray space before a semicolon, and lines 2828-2829 have an awkward line break before a colon. Line 5775 could be a long line, which might be fine, but line 4253 appears truncated, suggesting possible syntax issues. The user mentioned double spaces, and I could search for typographic errors like spaces before punctuation. Maybe I should check with a regex search, like `rg -n " [;:]"`, to find those occurrences easily.
codex
I’m adding one verification pass from the build surface, but only to catch objective LaTeX issues like undefined control sequences or malformed environments. The rest of the findings stay source-grounded and line-specific.
exec
/bin/zsh -lc "if command -v chktex >/dev/null 2>&1; then chktex -q -v0 chapters/theory/chiral_koszul_pairs.tex; else echo 'CHKTeX_MISSING'; fi" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
Total output lines: 1470

chapters/theory/chiral_koszul_pairs.tex:2:1:24:Delete this space to maintain correct pagereferences.
chapters/theory/chiral_koszul_pairs.tex:4:1:24:Delete this space to maintain correct pagereferences.
chapters/theory/chiral_koszul_pairs.tex:5:1:24:Delete this space to maintain correct pagereferences.
chapters/theory/chiral_koszul_pairs.tex:6:1:24:Delete this space to maintain correct pagereferences.
chapters/theory/chiral_koszul_pairs.tex:10:10:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:10:20:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:24:7:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:36:18:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:38:26:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:96:29:40:You should put punctuation outside inner math mode.
chapters/theory/chiral_koszul_pairs.tex:112:51:40:You should put punctuation outside inner math mode.
chapters/theory/chiral_koszul_pairs.tex:121:33:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:126:4:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:133:9:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:156:1:24:Delete this space to maintain correct pagereferences.
chapters/theory/chiral_koszul_pairs.tex:173:19:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:194:38:8:Wrong length of dash may have been used.
chapters/theory/chiral_koszul_pairs.tex:201:1:24:Delete this space to maintain correct pagereferences.



thinking
**Analyzing chktex output**

The chktex output is extensive, and I need to focus on relevant objective issues rather than style concerns that might not align with the user's requests. A critical error I see is "Mathmode still on at end of LaTeX file," which indicates a serious syntax problem. I should verify this issue by checking for any unmatched dollar signs, possibly starting from line 5950 onwards. At first glance near the end, everything looks okay, but I should inspect it further.
thinking
**Investigating chktex issues**

I think the chktex false positive might stem from an unmatched dollar sign earlier in the document. To confirm this, I could run an actual LaTeX build or use `lualatex` in draft mode on the main file. However, I need solid evidence from the build to ground my claims. There seems to be suspicious unmatched math around line 443, so I should check reports for unmatched math at the end of the file. I might also consider running `latexmk` if the main file exists. Let’s investigate!
thinking
**Considering file handling**

This seems heavy, and I'm thinking maybe I could use the existing Makefile, but that might lead to complications. Instead, perhaps I should focus on the specific file surface rather than performing a complete build. I could consider using `texfot pdflatex` to streamline the process. Anyway, my next step is to inspect the root files to see what options are available. I want to make sure I'm being efficient!
codex
`chktex` surfaced one hard signal that’s worth verifying further: it thinks this file leaves math mode open at EOF. I’m checking that directly in context so I don’t report a spurious build claim.
exec
/bin/zsh -lc 'ls -1' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5950,5986p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5718,5730p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 53ms:
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
 interacting-family example chapters.
 succeeded in 53ms:

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~II
(equivalence of homotopy categories). At H-level: a derived chiral
Koszul duality framework extending the quadratic bar-cobar adjunction
to DG chiral algebras, with the free fermion and $(\beta\gamma \oplus bc,
d_{\mathrm{BRST}})$ forming a derived Koszul pair. The M-level model
is the derived bar-cobar adjunction for DG chiral algebras. The shadow
is the decomposition of the BRST complex into Koszul dual sectors.
(Contributing to the derived/super extension flank adjoining
Conjecture~\ref{conj:master-infinite-generator}, not to the standard
$W_\infty$/Yangian packet.)
\end{remark}


thinking
**Searching for math errors**

I’m trying to figure out if there's an unmatched math issue. I realize it might not be worth reporting unless I find solid evidence. I could note a low severity if I see a math-mode imbalance at the end, but without verification, I think it's safer to skip it for now. I might want to check the main.log file for chapter lines from a previous build to see if there are any undefined macros to investigate further. Let's go ahead and search.
exec
/bin/zsh -lc "rg -n 'Undefined control sequence|LaTeX Error|Emergency stop|chapters/theory/chiral_koszul_pairs.tex' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'undefined|Undefined' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
4237: (./chapters/theory/chiral_koszul_pairs.tex
 succeeded in 51ms:
2184:LaTeX Warning: Reference `conv:three-hochschild' on page 95 undefined on input 
2300:LaTeX Warning: Reference `ch:derived-langlands' on page 118 undefined on input 
2307:LaTeX Warning: Reference `part:seven-faces' on page 119 undefined on input line
2311:LaTeX Warning: Reference `ch:holographic-datum-master' on page 119 undefined on
2315:LaTeX Warning: Reference `part:seven-faces' on page 119 undefined on input line
2319:LaTeX Warning: Reference `ch:holographic-datum-master' on page 119 undefined on
2326:LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
2333:LaTeX Warning: Reference `comp:bp-kappa-three-paths' on page 121 undefined on i
2337:LaTeX Warning: Reference `prop:nilpotent-transport-typeA' on page 121 undefined
2367:LaTeX Warning: Reference `part:seven-faces' on page 126 undefined on input line
2380:LaTeX Warning: Reference `part:v1-frontier' on page 128 undefined on input line
2394:LaTeX Warning: Reference `thm:ds-hpl-transfer' on page 129 undefined on input l
2440:LaTeX Warning: Reference `ch:derived-langlands' on page 132 undefined on input 
2444:LaTeX Warning: Reference `part:seven-faces' on page 132 undefined on input line
2448:LaTeX Warning: Reference `ch:holographic-datum-master' on page 132 undefined on
2452:LaTeX Warning: Reference `ch:genus1-seven-faces' on page 132 undefined on input
2456:LaTeX Warning: Reference `part:v1-frontier' on page 132 undefined on input line
2478:LaTeX Warning: Reference `ch:derived-langlands' on page 136 undefined on input 
2482:LaTeX Warning: Reference `part:seven-faces' on page 136 undefined on input line
2486:LaTeX Warning: Reference `ch:holographic-datum-master' on page 136 undefined on

thinking
**Inspecting log file references**

I need to locate lines in main.log around line 4921 to look for a specific undefined reference. It looks like I should search for occurrences of `rem:feynman_genus_g`, which might be undefined due to a label named "sec" not being rem. That's concrete in the file and build. Good finding! Now, I should inspect the relevant lines in the file where `rem:feynman_genus_g` is referenced and see if it appears elsewhere. Time to search!
codex
The build log gives one concrete in-file ref bug, which is better than speculation: there’s at least one undefined reference caused by a label-prefix mismatch inside this chapter. I’m tracing it to the source line now and checking whether there are more of the same kind.
exec
/bin/zsh -lc "rg -n 'rem:feynman_genus_g|sec:feynman_genus_g' chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4918,4926p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:4759:\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
chapters/theory/higher_genus_foundations.tex:4754:(We use the closed-string convention $\hbar^{2g-2}$; the Feynman-diagram convention in \S\ref{rem:feynman_genus_g} uses $\hbar^{g-1}$, corresponding to $\hbar_{\text{there}} = \hbar_{\text{here}}^2$.)
chapters/theory/chiral_koszul_pairs.tex:4759:\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
 succeeded in 52ms:

[763]

LaTeX Warning: Reference `rem:feynman_genus_g' on page 764 undefined on input l
ine 4754.



[764]
exec
/bin/zsh -lc "sed -n '4756,4761p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{tabular}
\end{table}

\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
The Feynman diagram interpretation of the bar-cobar complex (the identification
of bar chains with off-shell amplitudes and cobar chains with on-shell propagator



thinking
**Investigating label mismatches**

I’m facing a concrete dead/code label mismatch and I need to identify any undefined references in the file. I think I can search for target file labels that are incorrectly prefixed and compare them with reference names in the repository. I might need to look for labels with canonical mismatches, focusing on duplicates with different prefixes. The user wants every finding in the target file, so I may need to review main.log warnings to find unused or mismatched labels as well.
thinking
**Exploring label mismatches**

I'm going to search the whole repository for labels defined in this file that have zero references. I’ve already found a few, which I can report. However, there’s an undefined control sequence in the main.log that isn't relevant right now. I might want to check build warnings corresponding to target file line numbers. It looks like I need to identify improper label prefixes, especially in the `\begin{remark}` and `\begin{construction}` instances where mismatches might occur. I should verify the naming conventions to ensure things are consistent.
thinking
**Searching for mismatches**

I'm looking at the theorem registry and noticed that earlier it used labels like `constr:li-bar-spectral-sequence` and `comp:bgg-sl2-pipeline`. However, line 4634 has the label `const:wn-general`, which seems inconsistent with its construction environment, likely AP125. It's not one of the approved prefixes, so I need to check for any more mismatches. I think searching through the `\begin{construction}` labels will be helpful to catch any additional inconsistencies.
codex
The label audit found a genuine internal hygiene problem, not just dead aliases: this file mixes `constr:`, `const:`, `con:`, and even a `sec:` label on a `remark`. I’m checking which of those names are actually live before I report the exact renames.
exec
/bin/zsh -lc "sed -n '5908,5912p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\begin\\{construction\\}|\\\\begin\\{remark\\}|\\\\begin\\{problem\\}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4629,4636p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for lbl in constr:li-bar-spectral-sequence const:wn-general con:verify-koszul-pair prob:circularity sec:feynman_genus_g rem:feynman_genus_g; do echo "LABEL $lbl"; rg -n --fixed-strings "$lbl" chapters appendices metadata -g '"'*.tex' -g '*.md'; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection{Algorithm for checking Koszul pairs}

\begin{construction}[Verification of Koszul pairs]\label{con:verify-koszul-pair}
Given chiral algebras $\mathcal{A}_1, \mathcal{A}_2$, one verifies whether they form a Koszul pair as follows.
In the quadratic case, extract generators and relations, check that the residue pairing is perfect, and verify orthogonality $R_1 \perp R_2$.
 succeeded in 52ms:
%----------------------------------------------------------------

\subsection{\texorpdfstring{General $W_N$ algebras}{General W-N algebras}}

\begin{construction}[$W_N$ Koszul dual]
\label{const:wn-general}

For $W_N$ with generators $\{W^{(2)}, W^{(3)}, \ldots, W^{(N)}\}$ of weights $2, 3, \ldots, N$:
 succeeded in 52ms:
224:\begin{remark}[Explicit twisted differential]
266:\begin{remark}[Construction versus resolution]\label{rem:construction-vs-resolution}
513:\begin{remark}[Why the MC equation is Stokes' theorem]
536:\begin{remark}[Theorem~A decomposition]\label{rem:theorem-A-decomposition}
819:\begin{remark}[Relation to classical Koszulness]
1077:\begin{remark}[CE cohomology vs exterior algebra dimensions]
1083:\begin{remark}[Chevalley--Eilenberg cohomology vs chiral bar cohomology]%
1205:\begin{remark}[One-loop exactness]
1280:\begin{remark}[$A_\infty$ products as genus-$0$ shadows]
1414:\begin{remark}[Critical level: PBW degeneration vs diagonal Ext concentration]
1499:\begin{remark}[Rationality is not, by itself, a Koszul criterion]
1528:\begin{remark}[Status of admissible simple quotients]
1601:\begin{remark}[$W(2)$ at $c = -2$: Koszulness status]
1630:\begin{remark}[Arithmetic shadows: Koszulness as harmonic metric]
1640:\begin{remark}[Deformation quantization compatibility]
1669:\begin{construction}[Li--bar spectral sequence]
1837:\begin{remark}[What this theorem does not identify]
1932:\begin{remark}[The orbit hierarchy of Koszulness]
1988:\begin{remark}[Comparison with the Kac--Shapovalov criterion]
2184:\begin{remark}[Scope of factorization-homology concentration]
 succeeded in 52ms:
LABEL constr:li-bar-spectral-sequence
chapters/examples/kac_moody.tex:2810:Construction~\ref{constr:li-bar-spectral-sequence},
chapters/examples/kac_moody.tex:2954:(Construction~\ref{constr:li-bar-spectral-sequence}) and the
chapters/theory/chiral_koszul_pairs.tex:1670:\label{constr:li-bar-spectral-sequence}
chapters/theory/chiral_koszul_pairs.tex:1823:Construction~\ref{constr:li-bar-spectral-sequence}
chapters/connections/concordance.tex:7326: (Construction~\ref{constr:li-bar-spectral-sequence})
chapters/connections/concordance.tex:10288: (Construction~\ref{constr:li-bar-spectral-sequence}) and the
LABEL const:wn-general
chapters/theory/chiral_koszul_pairs.tex:4634:\label{const:wn-general}
LABEL con:verify-koszul-pair
chapters/theory/chiral_koszul_pairs.tex:5910:\begin{construction}[Verification of Koszul pairs]\label{con:verify-koszul-pair}
LABEL prob:circularity
chapters/theory/chiral_koszul_pairs.tex:3940:\begin{problem}[Circularity in Koszul duality]\label{prob:circularity}
LABEL sec:feynman_genus_g
chapters/theory/chiral_koszul_pairs.tex:4759:\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
LABEL rem:feynman_genus_g
chapters/theory/higher_genus_foundations.tex:4754:(We use the closed-string convention $\hbar^{2g-2}$; the Feynman-diagram convention in \S\ref{rem:feynman_genus_g} uses $\hbar^{g-1}$, corresponding to $\hbar_{\text{there}} = \hbar_{\text{here}}^2$.)


thinking
**Reviewing code issues**

I see that there’s a potential inconsistency with label prefixes like `const:` and `con:`. However, there are no build warnings because they’re unused, which might indicate there's dead code. The user asked about dead code and notation consistency, so I should use `chktex` to identify malformed constructs—I can focus on a few meaningful instances since the user is concerned with typography and mismatched braces. There might also be notable build warnings in the log file, particularly about undefined references.
thinking
**Finding undefined references**

I'm noticing that the search output shows many undefined references on pages like 701, which seem to relate to the `thm:family-index` theorem in this chapter. I really need to pin down the exact source line numbers in the file. To do that, I should search for `thm:family-index` within the file to locate where exactly these references are coming from. This should help me figure out how to address the issues properly.
codex
The file also emits in-file undefined references to other labels, not just an external chapter pointing back into it. I’m extracting the exact source lines for those now so the final report can distinguish “bad label defined here” from “bad reference written here.”
exec
/bin/zsh -lc "rg -n 'thm:family-index|sec:landscape-census|ch:landscape-census|sec:complementarity|thm:langlands-bar-bridge' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '468,485p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for lbl in thm:family-index sec:landscape-census ch:landscape-census sec:complementarity thm:langlands-bar-bridge; do echo "LABEL $lbl"; rg -n --fixed-strings "$lbl" chapters appendices metadata -g '"'*.tex' -g '*.md'; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1424:\textup{(}Theorem~\textup{\ref{thm:langlands-bar-bridge}}\textup{)}
 succeeded in 51ms:
\end{proof}

\begin{corollary}[Three bijections for chiral twisting morphisms;
\ClaimStatusProvedHere]
\label{cor:three-bijections}
\index{twisting morphism!three bijections|textbf}
For a conilpotent complete factorization coalgebra $\cC$
and an augmented chiral algebra $\cA$ on a smooth curve~$X$,
there are natural bijections
\begin{align}\label{eq:three-bijections}
\mathrm{Tw}(\cC, \cA)
&\;\cong\;
\operatorname{Hom}_{\mathrm{alg}}(\Omega_X(\cC), \cA)
\notag\\
&\;\cong\;
\operatorname{Hom}_{\mathrm{coalg}}(\cC, \bar{B}_X(\cA))
\end{align}
where\/ $\mathrm{Tw}(\cC, \cA)$ is the set of degree~$+1$
 succeeded in 53ms:
LABEL thm:family-index
chapters/examples/heisenberg_eisenstein.tex:1738:confirming Theorem~\ref{thm:family-index} directly from the shadow
metadata/theorem_registry.md:2369:| `thm:family-index` | `theorem` | 5769 | Family index theorem for genus expansions |
chapters/examples/genus_expansions.tex:169:This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
chapters/examples/genus_expansions.tex:1904:index theorem (Theorem~\ref{thm:family-index}) shows that
chapters/connections/editorial_constitution.tex:2579:(Theorem~\ref{thm:family-index}).
chapters/connections/editorial_constitution.tex:2668:5 & Index genus expansions & \textbf{Realized} (Thm~\ref{thm:family-index}) \\
chapters/connections/bv_brst.tex:1502:\textup{(}Theorem~\ref{thm:family-index}\textup{)},
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:4712:Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
chapters/connections/concordance.tex:5928:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/connections/concordance.tex:6227:Theorem~\ref{thm:family-index} synthesizes the preceding results:
chapters/connections/thqg_fredholm_partition_functions.tex:1449:(Theorem~\textup{\ref{thm:family-index}}).
chapters/frame/heisenberg_frame.tex:1616:(Theorem~\ref{thm:family-index})
chapters/frame/heisenberg_frame.tex:1718:(Theorem~\ref{thm:family-index})
chapters/frame/heisenberg_frame.tex:4642:(Theorem~\ref{thm:family-index})
chapters/theory/higher_genus_modular_koszul.tex:2730:$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
chapters/theory/higher_genus_modular_koszul.tex:2806:series. In particular, Theorem~\ref{thm:family-index} is downstream of
chapters/theory/higher_genus_modular_koszul.tex:2816:to $\kappa\cdot(\hat{A}(ix)-1)$ (Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_modular_koszul.tex:4407: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
exec
/bin/zsh -lc "rg -n 'sec:complementarity|sec:landscape-census|ch:landscape-census|thm:family-index' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3858,3868p' main.log" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 52ms:

[514]

[515]

[516]

LaTeX Warning: Reference `sec:complementarity' on page 517 undefined on input l
ine 1980.



thinking
**Searching for regex patterns**

I see there are no relevant references in the target file and notice a warning in `main.log` from another file, so it's not totally relevant right now. I need to focus on searching for spacing around punctuation in the file, specifically colons that are preceded by a space. Using a regex like `\s+:` seems to be a good approach.  This feels a bit overwhelming, but it's necessary to get the right formatting.
exec
/bin/zsh -lc "rg -n ' ;| :| ,| \\\\' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1406,1411p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'range and Koszulness may fail\\. For the Virasoro algebra|family-dependent\\s*:|bar-relevant range\\s*;|\\s+; the precise criterion|\\s+: it depends' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2826,2831p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1188

18:satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
37:$\chirLie \dashv \chirCom$ on $\Ran(X)$~\cite{FG12} settles
49:$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
53:$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
65:$k \geq 3$, acyclicity of the twisted tensor product
66:$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
77:$\{2, 3, 4, \infty\}$
80:nontrivial; they do \emph{not} record failure of Koszulness.
87:$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
96:$\tau \colon \barB(A) \to A^!$ is a degree-$+1$ element in the
97:convolution dg~Lie algebra satisfying $d\tau + \tau \star \tau = 0$.
101:integration kernel on $X^2 \setminus \Delta$. The acyclicity of
102:the twisted tensor product $K_\tau^L(\cA, \cC)$, the defining
161:\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)$,
163:$\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$.
165:$\Omega_X(\bar{B}_X(\mathcal{H}_k)) \xrightarrow{\;\sim\;} \mathcal{H}_k$
170: $K_\tau^L(\mathcal{H}_k, \mathrm{coLie}^{\mathrm{ch}}(V^*))$
172: $\tau\colon \mathrm{coLie}^{\mathrm{ch}}(V^*) \to \mathcal{H}_k$
 succeeded in 51ms:
\noindent\textbf{The universal vs.\ simple distinction.}
The universal algebra $V_k(\fg)$ is always chirally Koszul.
The simple quotient $L_k(\fg) = V_k(\fg)/I_k$ may fail Koszulness
at levels where the singular vector lies in the bar-relevant range
; the precise criterion is
Theorem~\textup{\ref{thm:kac-shapovalov-koszulness}}.
 succeeded in 51ms:
behavior reintroduces the Virasoro obstruction.

The upshot is that condition~(xii) is family-dependent
: it depends on more than $\dim(\fg)$ or Euler
characteristic data, and the equivalence of (xii) with the
Koszulness hierarchy survives only on the affine
 succeeded in 51ms:
1474:range and Koszulness may fail. For the Virasoro algebra, the Kac

thinking
**Exploring typography issues**

I'm looking into typography findings, particularly for spacing issues around the page. I might consider checking for duplicate labels, but I'm not sure it's necessary. I could use `chktex` to find vertical rules in tables, especially since the user mentioned typography and broken environments. There's potential to report unattractive tables with vertical rules, and perhaps suggest switching to booktabs. I should also identify all tables with vertical bars and audit aspects related to aesthetics.
codex
I’m doing one last typography sweep for local surface issues that aren’t mathematical but still degrade the chapter: punctuation spacing, table style drift, and quote/label consistency. That’s the last pass before I freeze the finding list.
exec
/bin/zsh -lc "rg -n '\\\\begin\\{tabular\\}\\{\\|' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\\\\\label\\{(sec:|const:|con:)' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'``|'"''' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 53ms:
4665:\begin{tabular}{|c|c|c|c|}
4745:\begin{tabular}{|l|c|c|l|}
5779:\begin{tabular}{|l|c|c|c|}
exec
/bin/zsh -lc "sed -n '4662,4676p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 5986

1:\chapter{Chiral Koszul duality}
2:\label{chap:koszul-pairs}
3:
4:\index{chiral Koszul duality|textbf}
5:\index{twisting morphism!chiral|textbf}
6:\index{Francis--Gaitsgory|textbf}
7:
8:Classical Koszul duality, in the sense of
9:Priddy~\cite{Priddy70} and
10:Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
11:algebras over a field: the bar complex is a tensor coalgebra on a
12:finite-dimensional vector space, the cobar functor inverts it
13:when bar cohomology is concentrated in degree one, and the
14:duality exchanges quadratic algebras with quadratic coalgebras.
15:Three features of chiral algebras on algebraic curves defeat
16:this framework simultaneously. First, chiral algebras are
17:\emph{curved}: the bar differential on the genus expansion
18:satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
 succeeded in 53ms:
\begin{table}[ht]
\centering
\caption{$W_N$ completion complexity}
\begin{tabular}{|c|c|c|c|}
\hline
$N$ & Generators & Max pole order & $\dim(\bar{B}^1/I^2)$ \\
\hline
2 (Virasoro) & 1 & 4 & 1 \\
3 & 2 & 6 & 3 \\
4 & 3 & 8 & 6 \\
5 & 4 & 10 & 10 \\
$N$ & $N-1$ & $2N$ & $\binom{N}{2}$ \\
\hline
\end{tabular}
\end{table}


thinking
**Inspecting for errors**

I think I might need to look for instances of the word "remarkably" and check the lines around 3938-4251 since there's a huge section that could have many issues. The circularity section likely has style problems too. I should also consider examining undefined macros or hypotheses in the proofs from the file contents. It seems like there could be a lot to fix or clarify here!
thinking
**Searching for labels' definitions**

I need to check if the labels like `hyp:fg`, `hyp:poly`, and `hyp:smooth` exist somewhere in the text. The theorem text at 4225 gives a bullet list but doesn’t clarify these labels. It’s confusing since those references might be undefined, which could mean a warning wasn’t shown because I might need a second pass. So, I’m planning to do a thorough search to find out more about these undefined references!
codex
I found a likely second-order issue in the circularity/completion block: it references hypothesis labels that I didn’t see defined locally. I’m verifying that against the manuscript rather than inferring from the prose.
exec
/bin/zsh -lc "sed -n '4388,4395p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4225,4234p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'hyp:fg|hyp:poly|hyp:smooth' chapters/theory/chiral_koszul_pairs.tex chapters appendices metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
On the $E_1$ page, $\Phi$ reduces to the classical Verdier duality isomorphism between logarithmic cohomology and distributional cohomology on $\overline{C}_{p+1}(X)$ (Theorem~\ref{thm:verdier-config}). For each fixed $p$, this is an isomorphism:
\[\Phi_1^{p,*} \colon E_1^{p,*}(\bar{B}) \xrightarrow{\;\cong\;} E_1^{p,*}(\mathcal{A}^!).\]
By the comparison theorem for spectral sequences (Weibel, \emph{Homological Algebra}, Theorem~5.2.12), a map of filtered complexes inducing an isomorphism on $E_1$ pages induces an isomorphism on abutments. Therefore $\Phi$ is a quasi-isomorphism of the associated graded complexes.

For the \emph{completed} statement: hypothesis \ref{hyp:fg} (finite generation) ensures that each graded piece $\bar{B}^n$ is a coherent $\mathcal{D}_X$-module. Hypothesis \ref{hyp:poly} (polynomial growth) ensures that the inverse system $\{\bar{B}^{\mathrm{ch}}(\mathcal{A})/I^n\}_{n \geq 1}$ satisfies the Mittag-Leffler condition: the images $\mathrm{im}(I^{n+k}/I^n \to I^n/I^{n-1})$ stabilise for $k \gg 0$, since the $\mathcal{D}_X$-module structure constants grow at most polynomially. Hypothesis \ref{hyp:smooth} (formal smoothness) ensures that the spectral sequence converges strongly in the $I$-adic topology.

By the Mittag-Leffler criterion, the derived inverse limit $R^1\varprojlim$ vanishes, so the natural map
\[H^*(\widehat{\bar{B}^{\mathrm{ch}}(\mathcal{A})}) \to \varprojlim_n H^*(\bar{B}^{\mathrm{ch}}(\mathcal{A})/I^n)\]
 succeeded in 51ms:
\begin{lemma}[Completion convergence; \ClaimStatusProvedHere]\label{lem:completion-convergence}
For chiral algebras satisfying:
\begin{itemize}
\item Finite generation over $\mathcal{D}_X$
\item Polynomial growth of structure constants
\item Formal smoothness: $\dim H^*(\mathcal{A}, \mathcal{A}) < \infty$
\end{itemize}

The completion converges and:
\[\widehat{\bar{B}^{\text{ch}}(\mathcal{A}_1)} \simeq \mathcal{A}_2^!\]
 succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:4277:\item\label{hyp:fg} $\mathcal{A} = T_{\mathrm{chiral}}(\mathcal{V})/(R)$ is finitely generated over $\mathcal{D}_X$,
chapters/theory/chiral_koszul_pairs.tex:4278:\item\label{hyp:poly} the OPE structure constants satisfy polynomial growth: $|C_{ij}^{k,m}| \leq P(m)$ for a polynomial~$P$,
chapters/theory/chiral_koszul_pairs.tex:4279:\item\label{hyp:smooth} $\mathcal{A}$ is formally smooth: $\dim H^*_{\mathrm{ch}}(\mathcal{A},\mathcal{A}) < \infty$.
chapters/theory/chiral_koszul_pairs.tex:4392:For the \emph{completed} statement: hypothesis \ref{hyp:fg} (finite generation) ensures that each graded piece $\bar{B}^n$ is a coherent $\mathcal{D}_X$-module. Hypothesis \ref{hyp:poly} (polynomial growth) ensures that the inverse system $\{\bar{B}^{\mathrm{ch}}(\mathcal{A})/I^n\}_{n \geq 1}$ satisfies the Mittag-Leffler condition: the images $\mathrm{im}(I^{n+k}/I^n \to I^n/I^{n-1})$ stabilise for $k \gg 0$, since the $\mathcal{D}_X$-module structure constants grow at most polynomially. Hypothesis \ref{hyp:smooth} (formal smoothness) ensures that the spectral sequence converges strongly in the $I$-adic topology.
chapters/theory/chiral_koszul_pairs.tex:4277:\item\label{hyp:fg} $\mathcal{A} = T_{\mathrm{chiral}}(\mathcal{V})/(R)$ is finitely generated over $\mathcal{D}_X$,
chapters/theory/chiral_koszul_pairs.tex:4278:\item\label{hyp:poly} the OPE structure constants satisfy polynomial growth: $|C_{ij}^{k,m}| \leq P(m)$ for a polynomial~$P$,
chapters/theory/chiral_koszul_pairs.tex:4279:\item\label{hyp:smooth} $\mathcal{A}$ is formally smooth: $\dim H^*_{\mathrm{ch}}(\mathcal{A},\mathcal{A}) < \infty$.
chapters/theory/chiral_koszul_pairs.tex:4392:For the \emph{completed} statement: hypothesis \ref{hyp:fg} (finite generation) ensures that each graded piece $\bar{B}^n$ is a coherent $\mathcal{D}_X$-module. Hypothesis \ref{hyp:poly} (polynomial growth) ensures that the inverse system $\{\bar{B}^{\mathrm{ch}}(\mathcal{A})/I^n\}_{n \geq 1}$ satisfies the Mittag-Leffler condition: the images $\mathrm{im}(I^{n+k}/I^n \to I^n/I^{n-1})$ stabilise for $k \gg 0$, since the $\mathcal{D}_X$-module structure constants grow at most polynomially. Hypothesis \ref{hyp:smooth} (formal smoothness) ensures that the spectral sequence converges strongly in the $I$-adic topology.

thinking
**Reviewing notation consistency**

I need to ensure that I consistently use `\kappa(\cA)` throughout. For line 2445, I think it should probably be `\Delta = 8\,\kappa(\cA)\,S_4(\cA)`, or at the very least `\Delta_\cA = 8\,\kappa(\cA) S_4(\cA)`. It seems that using just `\kappa` might overlook family dependence. I need to inspect not just this line, but potentially many others and search for contexts where this might apply.
codex
The notation pass has one subtle class of issue: the file often starts with `\kappa(\cA)` and then slips into bare `\kappa` later in the same paragraph. I’m re-opening those spots now to keep only the genuinely inconsistent ones.
exec
/bin/zsh -lc "sed -n '107,118p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2440,2450p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 80ms:
$m_k = 0$ for $k \geq 3$ on bar cohomology if and only if
$\cA$ is chirally Koszul. The shadow depth classification
$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
(Remark~\ref{rem:shadow-depth-gkw-refinement}) refines their
binary formal/non-formal dichotomy into a four-class stratification
governed by the discriminant $\Delta = 8\kappa S_4$.
\end{remark}

\begin{remark}[Loop-exactness ordering $G < L < C < M$]
\label{rem:loop-exactness-ordering}
\index{shadow depth!loop-exactness ordering}
 succeeded in 82ms:
Three phenomena distinguish the chiral setting from its
point-set ancestor, and all three are invisible at genus zero:
the modular characteristic $\kappa(\cA)$, which measures
curvature of the genus expansion
(Theorem~\ref{thm:modular-characteristic});
Lagrangian complementarity between $\cA$ and $\cA^!$
(Theorem~\ref{thm:quantum-complementarity-main});
and the critical discriminant $\Delta = 8\kappa S_4$, whose
vanishing controls termination of the shadow obstruction tower
(Theorem~\ref{thm:riccati-algebraicity}).
At genus zero all three collapse: $\kappa$ plays no role,
complementarity reduces to the genus-$0$ bar-cobar adjunction,
exec
/bin/zsh -lc "sed -n '2524,2554p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5406,5416p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
the shadow obstruction tower with its weight-$2$ truncation, so the
transferred Swiss-cheese operations vanish for every $k \geq 3$.
Class~$L$: the cubic shadow
$S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
ratio (the structure constant divided by the level); the quartic
and higher shadows vanish because the Jacobi identity and rank
constraints eliminate all $\overline{\cM}_{0,r+1}$ tree sums for
$r \geq 4$ when the OPE has at most double poles.
 succeeded in 52ms:
\index{Koszul duality!categorified}
\index{Kazhdan--Lusztig conjecture!bar complex interpretation}
The numerical complementarity $\kappa(\cA) + \kappa(\cA^!) = K$
(Theorem~\ref{thm:quantum-complementarity-main}) admits a
categorified lift: the bar-cobar adjunction of Theorem~A
induces, on module categories, an equivalence
$D(\mathrm{Mod}_{\cA}^{\mathrm{compl}}) \simeq
D(\mathrm{CoMod}_{B(\cA)}^{\mathrm{conil}})$
(Theorem~\ref{thm:e1-module-koszul-duality}) whose
decategorification recovers the scalar identity $\kappa + \kappa^! = K$.

codex
The `\kappa` inconsistencies are real: some paragraphs lose the algebra argument entirely, and one Virasoro-only computation collapses from `\kappa_c` to bare `\kappa`. I’m checking whether the critical-level remark has the same drift before I include it.
exec
/bin/zsh -lc "sed -n '1414,1445p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Critical level: PBW degeneration vs diagonal Ext concentration]
\label{rem:pbw-vs-diagonal-critical}
\index{Koszul property!critical level subtlety}
At the critical level $k = -h^\vee$, the PBW spectral sequence
degenerates at~$E_2$ (the $E_2$-collapse mechanism is
$k$-independent, since $\operatorname{gr}_F V_k(\fg) \cong
\operatorname{Sym}^{\mathrm{ch}}(\fg)$ for all~$k$).
However, the $E_2$ page is \emph{not} diagonally concentrated:
the bar cohomology
$H^*(\barB(V_{-h^\vee}(\fg))) = \Omega^*(\mathrm{Op}_{\fg^\vee}(D))$
\textup{(}Theorem~\textup{\ref{thm:langlands-bar-bridge}}\textup{)}
has $H^0 = \operatorname{Fun}(\mathrm{Op}) \neq \bC$,
contributing off-diagonal classes
$\operatorname{Ext}^{0,q} \neq 0$ for all even $q \geq 0$.
Hence the diagonal criterion of
Theorem~\textup{\ref{thm:pbw-koszulness-criterion}}
\textup{(}$\operatorname{Ext}^{p,q} = 0$ for
$p \neq q$\textup{)} \emph{fails} at $k = -h^\vee$.

At generic level ($\kappa \neq 0$), the curvature of the bar

thinking
**Considering notation consistency**

I'm noticing that the standard `\textexclamdown` symbol looks aesthetically strange. I feel like it might not fit the context well. I think the actual line 4987 weird symbol should be used because `\text{\textexclamdown}` is just an upside-down exclamation point, instead of the operadic dual. The user seems to want a cosmetic approach, but consistency in notation is important. I should verify the context, especially since this might be a typo regarding cooperad `P^¡`.
codex
There’s one more low-level typography class worth checking: legacy italic corrections like `where\/` and inconsistent raw table syntax in otherwise `booktabs` tables. I’m validating those now; after that the list is stable.
exec
/bin/zsh -lc "rg -n '\\\\/' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '482,486p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4936,4942p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
&\;\cong\;
\operatorname{Hom}_{\mathrm{coalg}}(\cC, \bar{B}_X(\cA))
\end{align}
where\/ $\mathrm{Tw}(\cC, \cA)$ is the set of degree~$+1$
morphisms $\tau\colon \cC \to \cA$ satisfying the
 succeeded in 53ms:
485:where\/ $\mathrm{Tw}(\cC, \cA)$ is the set of degree~$+1$
4938:Let\/ $\mathcal{P}$ be a quadratic operad over a field\/~$k$, and let\/
4939:$\mathcal{V}$ be a stable presentably symmetric monoidal\/
4940:$\infty$-category over\/~$k$. If\/ $\mathcal{P}$ is Koszul in the
4941:classical sense \textup{(}i.e., over the category of\/ $k$-modules\textup{)},
4942:then\/ $\mathcal{P}$ is Koszul as an operad internal to\/~$\mathcal{V}$:
4943:the operadic bar construction\/
4945:is a quasi-isomorphism of cooperads in\/ $\Sigma$-objects of\/~$\mathcal{V}$.
 succeeded in 53ms:
\label{lem:operadic-koszul-transfer}
\index{Koszul operad!transfer to symmetric monoidal categories}
Let\/ $\mathcal{P}$ be a quadratic operad over a field\/~$k$, and let\/
$\mathcal{V}$ be a stable presentably symmetric monoidal\/
$\infty$-category over\/~$k$. If\/ $\mathcal{P}$ is Koszul in the
classical sense \textup{(}i.e., over the category of\/ $k$-modules\textup{)},
then\/ $\mathcal{P}$ is Koszul as an operad internal to\/~$\mathcal{V}$:



thinking
**Addressing unused labels**

I'm considering which unused labels to report under the dead-code category. For example, I can suggest removing redundant alias labels or renaming/correcting them, which would yield several minor findings. I need to check if both `thm:bar-computes-koszul-dual-complete` and `thm:chiral-koszul-duality` are utilized. If they aren't, I’ll handle the mismatch of prefixes for labels like `con:verify-koszul-pair` and `const:wn-general`, potentially deleting them if unused. For others, like `prob:circularity`, I'll remove it if it has no references, considering similar unused aliases.
thinking
**Fixing label references**

So, the user mentioned that dead code means unused labels, which suggests I should remove those. If I delete both, and they need them later, it could cause issues. I might want to check if `prob:circularity` is unreferenced, but maybe it's worth keeping for future reference. The user’s right about removing unused labels, though. I also need to rename a label to maintain external references properly while ensuring backward compatibility. The final fix involves adjusting the line to correct the reference and dropping the unnecessary alias.
thinking
**Searching for label patterns**

I need to look for patterns of labels in the file that start with `sec:` or incorrect environment prefixes. I remember trying to use `rg` to find labels like sec/const/con, but it didn't work out. Trying regex might have been the issue — perhaps it was due to quoting. So, I'll make sure to do it properly this time to get the results I need!
codex
I’ve got the label picture now: one broken external ref, several unused aliases, and two inconsistent construction prefixes that are only surviving because nothing points at them. I’m doing a final grep for any other noncanonical prefixes inside this file before I write the report.
exec
/bin/zsh -lc "perl -ne 'if(/\\\\begin\\{(\\w+)\\}.*\\\\label\\{(["'^}]+)'"\\}/){print "'$. . ":ENV=" . $1 . ":LBL=" . $2 . "'"\\n\"}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
200:ENV=definition:LBL=def:chiral-twisting-datum
229:ENV=equation:LBL=eq:chiral-twisted-differential-L
234:ENV=equation:LBL=eq:chiral-twisted-differential-R
252:ENV=definition:LBL=def:chiral-koszul-morphism
266:ENV=remark:LBL=rem:construction-vs-resolution
477:ENV=align:LBL=eq:three-bijections
536:ENV=remark:LBL=rem:theorem-A-decomposition
625:ENV=definition:LBL=def:chiral-koszul-pair
685:ENV=example:LBL=ex:heisenberg-koszul-pair
979:ENV=equation:LBL=eq:pbw-associated-graded-bar
1010:ENV=equation:LBL=eq:e1-page-exterior
1692:ENV=equation:LBL=eq:li-bar-ss
3829:ENV=theorem:LBL=thm:yangian-self-dual
3889:ENV=proposition:LBL=prop:yangian-koszul-general
3940:ENV=problem:LBL=prob:circularity
3962:ENV=definition:LBL=def:koszul-dual-coalgebra
4018:ENV=remark:LBL=rem:independence-construction
4225:ENV=lemma:LBL=lem:completion-convergence
4349:ENV=equation:LBL=eq:comparison-map
4408:ENV=remark:LBL=rem:comparison-classical

thinking
**Creating a parsing script**

I'm realizing that the current method only catches same-line labels and not the separate label lines, like 4634. It seems I need to parse those separate line labels after the "begin environment" line. Maybe I'll use awk while maintaining the current environment line to address this issue. Alright, I think creating a small script could help streamline the process effectively. Let’s see how I can get that set up!
exec
/bin/zsh -lc "perl -ne 'if(/\\\\begin\\{(\\w+)\\}/){"'$env=$1;$eline=$.;} if(/'"\\\\label\\{(["'^}]+)'"\\}/){print "'$. . ":ENV=" . ($env//"?") . ":LBL=" . $1 . ":BEGIN=" . ($eline//"?") . "'"\\n\"}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2:ENV=?:LBL=chap:koszul-pairs:BEGIN=?
156:ENV=?:LBL=sec:chiral-twisting-data:BEGIN=?
200:ENV=definition:LBL=def:chiral-twisting-datum:BEGIN=200
225:ENV=remark:LBL=rem:explicit-twisted-differential:BEGIN=224
229:ENV=equation:LBL=eq:chiral-twisted-differential-L:BEGIN=229
234:ENV=equation:LBL=eq:chiral-twisted-differential-R:BEGIN=234
252:ENV=definition:LBL=def:chiral-koszul-morphism:BEGIN=252
266:ENV=remark:LBL=rem:construction-vs-resolution:BEGIN=266
286:ENV=lemma:LBL=lem:twisted-product-cone-counit:BEGIN=285
313:ENV=lemma:LBL=lem:twisted-product-cone-unit:BEGIN=312
333:ENV=lemma:LBL=lem:filtered-comparison:BEGIN=332
361:ENV=lemma:LBL=lem:filtered-comparison-unit:BEGIN=360
400:ENV=theorem:LBL=thm:fundamental-twisting-morphisms:BEGIN=399
412:ENV=enumerate:LBL=ftm:koszul:BEGIN=411
415:ENV=enumerate:LBL=ftm:counit:BEGIN=411
419:ENV=enumerate:LBL=ftm:unit:BEGIN=411
424:ENV=enumerate:LBL=ftm:acyclic:BEGIN=411
472:ENV=corollary:LBL=cor:three-bijections:BEGIN=470
477:ENV=align:LBL=eq:three-bijections:BEGIN=477
514:ENV=remark:LBL=rem:MC-is-Stokes:BEGIN=513
exec
/bin/zsh -lc "rg -n '"'^:|''^;'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2928,2935p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1126,1138p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\"'$'"\\\\kappa\\"'$|'"\\\\Delta = 8\\\\kappa S_4|\\\\kappa \\+ \\\\kappa\\"'^!|At generic level '"\\(\\\\kappa' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\qquad
H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
\]
% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
% $\cA_2 = \cA_1^!$ creates a notational double-dual. The intended meaning
% is the bar cohomology of $\cA_1$, i.e.\ $\cA_1^i = H^*(\barBch(\cA_1))$
% viewed as a graded coalgebra (Convention~\ref{conv:bar-coalgebra-identity}).
% The subsequent prose clarifies this: $\barBch(\cA_1) \simeq \cA_2^!$
% means the bar complex is quasi-isomorphic to $\cA_1^i$ in graded chiral
% coalgebras. No mathematical ambiguity; notation retained for consistency
% with the Koszul-pair framework.
Equivalently, $\bar{B}^{\mathrm{ch}}(\cA_1) \simeq \cA_2^!$ in the
derived category of graded chiral coalgebras, where $\cA_2^!$ carries
 succeeded in 53ms:
1410:; the precise criterion is
2829:: it depends on more than $\dim(\fg)$ or Euler
4851::\Omega^{\mathrm{ch}},
5769::TT:(z) = \lim_{w \to z} \left( T(z)T(w) - \frac{c/2}{(z-w)^4} - \frac{2T(w)}{(z-w)^2} - \frac{\partial T(w)}{z-w} \right)
 succeeded in 51ms:
\midrule
\multicolumn{6}{@{}l}{\textit{Lattice and logarithmic}} \\[2pt]
$V_{D_4}$ lattice VOA
 & lattice & $28$ & Proved & lattice filt.\ & $G$, $r_{\max}=2$ \\
Triplet $\cW(2)$
 & logarithmic & $4$ & Open & --- & unknown \\
\bottomrule
\end{tabular}
 succeeded in 51ms:
114:and the critical discriminant $\Delta = 8\kappa S_4$, whose
117:At genus zero all three collapse: $\kappa$ plays no role,
2445:governed by the discriminant $\Delta = 8\kappa S_4$.
2528:$\Delta = 8\kappa S_4 \neq 0$ forces all higher operations to be
2553:$S_4 = 10/[c(5c{+}22)]$ and $\Delta = 8\kappa S_4 = 40/(5c{+}22) \neq 0$
2873:Cross-family consistency checks: $\kappa$ additivity,
4962:by~$\kappa$. Both the composition product and the
5415:decategorification recovers the scalar identity $\kappa + \kappa^! = K$.





thinking
**Evaluating findings and output format**

I'm working on a transition-quality pattern and using line 136 as a roadmap for the chapter. The output format requires exact lines, so we might need to separate them. I'm estimating around 15 final findings, which feels manageable. I need to verify that there's no extraneous AI content or formatting issues. The user is specifically asking for findings, so I'll present the counts and severity levels as they requested: CRITICAL, HIGH, MEDIUM, and LOW. I also need precise line numbers in the specified format.
thinking
**Identifying reference issues and fixes**

I’m considering how to address the broken external reference. I might mention source line 4759 and the build log since the format requires a file:line structure. The issue is a label prefix mismatch, causing an undefined reference in `higher_genus_foundations.tex`. I need to recommend a specific fix: renaming the label to `\label{rem:feynman_genus_g}` and either updating or deleting the other label. I’ll also assess severity levels for various lines in the document, noting that the chapter opens effectively with the problem.
thinking
**Analyzing structural quality**

I’m evaluating line 45, which lists results before the proof, specifically for AP109. The user requested attention to transition quality and redundancy. While I could include it, it shouldn't be part of the chapter's opening. I think the severity should be rated as MEDIUM because it contributes to early structural bloat. I should also consider line 61, and I'll note that lines 45-73 actually contain two separate paragraphs that list theorems.
thinking
**Organizing findings for clarity**

I’m considering how to combine findings from lines 45 and 61 about front-loading theorem inventory and bookkeeping before definitions. It might be better to move inventory to the theorem lane. For lines 1663, 3220, and 3825, I must ensure the transition signposts are clear. The user asked for specific lines, so I might list them as file:line with notes about recurring issues. Overall, I'll separate them into three distinct low findings, ensuring output length is still manageable.
thinking
**Organizing unused labels**

I need to consider how to address several unused labels, such as at lines 3962, 4684, 4818, 3940, 4634, and 5910. It might make sense to group dead labels together, especially since many are zero-ref labels. For example, I could combine several into a low finding starting at 3940 due to their isolated nature. The challenge is that the user wants every finding to have an exact line, and I might need to eventually list about six additional findings. That feels like it could be too much, but it might work.
exec
/bin/zsh -lc "sed -n '45,73p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
tests and consequences around chiral Koszulness. Nine are
unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
vanishing of transferred $A_\infty$ operations $m_k$ for








thinking
**Organizing items for clarity**

I'm thinking of drafting a list with around 17 items. The first one is a high-priority issue related to a wrong label prefix and an undefined reference, which is a bit concerning. Next, I have a medium-priority point about introducing a theorem inventory before the proofs, something labeled as AP109. Lastly, there's a low-priority item concerning a roadmap signpost. This feels like a solid start, but I might need to elaborate more on some points as I go!
thinking
**Summarizing findings for a report**

It looks like I have around 5986 lines to check. I should summarize everything clearly with the format: "Checked: 5986 | Findings: 28 | Verdict: FAIL." It might be helpful to include line numbers for findings that span multiple lines, like citing file:114 and mentioning also 117. The user seems to want the exact lines referenced, so I need to keep that in mind while organizing the information.
thinking
**Organizing items by severity**

I need to keep a list of 28 items and ensure it's concise, aiming for under 70 lines. Each bullet might contain 1-2 clauses, and I'm thinking of categorizing these by severity. 

For example, I can mark some items as HIGH, like 4759; MEDIUM for 45, 114, 1433, 2445, 2528, 5415, and 4136; and LOW for the remaining 20, which could include things like line 45 and 136. I'll need to evaluate each item carefully!
thinking
**Revising text for clarity**

I think I need to delete the sentence and let the next one facilitate the transition. The following reference still serves as a roadmap. I can fix the entire paragraph by clarifying how the Heisenberg calculation isolates twisting data, explaining that once fixed, the PBW comparison provides the recognition criterion while proving the bar-cobar adjunction on the Koszul locus. I'll address specifics for lines 1663, 3220, and 3825, along with kappa lines adjustments.
thinking
**Clarifying labeling and reporting**

I’m considering line 4684, where two labels are unused. If I delete both, the example will become unlabeled, which is fine, but it may be desirable for future reference. The same goes for line 4818. I need to figure out how to present `Checked: 5986` clearly; maybe it's best to say `Checked: 5986 | Findings: 28 | Verdict: FAIL`. I might skip mentioning AI slop or markdown issues unless the user wants exhaustive details. The final summary should use flat bullets and the requested format for file line references.
thinking
**Organizing issues**

I'm considering that items 1409 and 2829 might share the same issue, so it could make sense to group them as "1409 — ... same spacing defect recurs at 2829." That feels efficient! I also think it would be smart to group the italic corrections for 485 and 4938 together. Oh, and for the unused label cluster, it could work to consolidate those into one bullet point, maybe if I specify the exact lines. This way, the information stays clear!
thinking
**Considering audit details**

I’m thinking we should include the 4759 high, since there might not be enough higher values. I need to mention that no AI slop, markdown, or hedging was found—unless I decide not to. However, to be exhaustive, I feel like I should summarize accurately. Since the user asked for an audit, I should mention the full file and targeted scans. Including something like "Checked: 5986 | Findings: 16 | Verdict: FAIL" seems relevant. Plus, I’ll ensure the bullets are flat and use the exact relative path, even if it feels repetitive.
thinking
**Organizing the output**

I’m thinking maybe I should aim for around 16 lines total. It makes sense to order them by severity—starting with high, then medium, and finally low. I should be able to include multiple line numbers in the format `file:line` within a single bullet, which is great! I also want to ensure my final answer with equations like `\kappa(\cA)+\kappa(\cA^!)=K` is correct. Keeping it no more than 70 lines seems solid, with 16 bullets plus a concise summary.
codex
- [HIGH] `chapters/theory/chiral_koszul_pairs.tex:4759` — PROBLEM: a `remark` is labeled `sec:feynman_genus_g`, but `chapters/theory/higher_genus_foundations.tex:4754` references `rem:feynman_genus_g`; `main.log` reports that reference as undefined. FIX: rename the label here to `\label{rem:feynman_genus_g}` and delete `\label{sec:feynman_genus_g}`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:45` — PROBLEM: the introduction abandons the deficiency opening and front-loads theorem inventory plus bookkeeping (`Theorem A`, `9+1+1+1`) before the local mathematics starts. FIX: replace lines 45-73 with one necessity paragraph, e.g. `Any usable duality here must invert on the Koszul locus, intertwine Verdier duality, and fit complementarity; the precise equivalences are stated when those results are proved below.` Move the `9+1+1+1` count to Theorem~`\ref{thm:koszul-equivalences-meta}`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:114` — PROBLEM: the paragraph introduces `\kappa(\cA)` and then degrades to bare `\Delta = 8\kappa S_4` and bare `\kappa` at line 117, so the algebra dependence disappears. FIX: write `\Delta_\cA = 8\,\kappa(\cA)\,S_4(\cA)` and `At genus zero all three collapse: \kappa(\cA) plays no role`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:1433` — PROBLEM: `At generic level ($\kappa \neq 0$)` uses bare `\kappa` inside a Kac--Moody-only remark. FIX: write `At generic level ($\kappa(\widehat{\fg}_k)\neq 0$)` or introduce a local symbol `\kappa_k`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:2445` — PROBLEM: the Gaiotto--Kulp--Wu remark again uses bare `\Delta = 8\kappa S_4`. FIX: write `\Delta_\cA = 8\,\kappa(\cA)\,S_4(\cA)`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:2528` — PROBLEM: the class-`M` discussion and proof use bare `\kappa` in a Virasoro-only computation (`\Delta = 8\kappa S_4`, `2\kappa/\kappa`). FIX: replace that block with `\Delta_{\mathrm{Vir}_c}=8\,\kappa_c S_4` and `2\kappa_c/\kappa_c=2`.

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:4136` — PROBLEM: `Bar computes Koszul dual, complete statement` restates the earlier bar-cobar theorem in a second notation system (`\mathcal{A}`, `\bar{B}^{\text{ch}}`, completion language), so the chapter carries two competing main statements. FIX: demote this to a proposition such as `Completed comparison map for Stage~3`, state only the extra completion content, and normalize the statement to the chapter macros (`\cA_i`, `\barBgeom`/`\barB_X`).

- [MEDIUM] `chapters/theory/chiral_koszul_pairs.tex:5415` — PROBLEM: the remark falls back from `\kappa(\cA)+\kappa(\cA^!)=K` to bare `\kappa + \kappa^! = K`. FIX: rewrite the sentence as `decategorification recovers the scalar identity \kappa(\cA)+\kappa(\cA^!)=K`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:136` — PROBLEM: `The chapter proceeds in three stages.` is roadmap prose, not a forced transition. FIX: replace the paragraph with a necessity transition, e.g. `The Heisenberg calculation isolates the twisting datum; once that datum is fixed, PBW comparison yields the recognition theorem and the genus-zero bar-cobar adjunction.`

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1663` — PROBLEM: the section changes track with empty signpost prose (`We now give...` here; the same defect recurs at 3220 `We now record...` and 3825 `We record here only...`). FIX: replace them with mathematical-necessity transitions: `The Li filtration is the first refinement that sees the geometry hidden from the Shapovalov test`; `Because the PBW route is affine-specific, the next invariant must be Poisson-geometric`; `Only the Yangian self-duality statements are needed for the Koszul argument; the Hopf-theoretic material stays in Chapter~\ref{chap:yangians}.`

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1129` — PROBLEM: the eight-line `RECTIFICATION-FLAG` comment is stale audit residue embedded in the theorem surface. FIX: delete lines 1129-1136 entirely.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:1409` — PROBLEM: there is a stray space before punctuation in `range ;`; the same defect recurs at 2829 (`family-dependent :`). FIX: change them to `range;` and `family-dependent:`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:2933` — PROBLEM: the table uses `---` as a cell value, which violates the no-em-dash rule and reads like placeholder text. FIX: replace `---` with `undetermined` or `not yet identified`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:4665` — PROBLEM: this table uses vertical rules and `\hline`, which clashes with the chapter’s `booktabs` tables; the same drift recurs at 4745 and 5779. FIX: rewrite these three tables with `\begin{tabular}{@{}...@{}}`, `\toprule`, `\midrule`, and `\bottomrule`.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:485` — PROBLEM: legacy italic correction `where\/` appears in roman text; the same outdated markup recurs at 4938-4945 (`Let\/`, `If\/`, `then\/`, `construction\/`). FIX: remove every `\/` in these lines and keep plain prose.

- [LOW] `chapters/theory/chiral_koszul_pairs.tex:3940` — PROBLEM: the file carries dead or redundant labels with no `.tex` refs in `chapters/` or `appendices/`: `prob:circularity` (3940), `def:koszul-dual-coalgebra` (3962), `const:wn-general` (4634), `ex:affine-yangian-kp`/`ex:yangian-completion` (4684-4685), `rem:convergence-pro-nil`/`rem:convergence-pronilpotent` (4818-4819), `con:verify-koszul-pair` (5910). FIX: delete those labels; if a handle is actually needed later, keep one canonical label per block and reference it.

## Summary
Checked: 5986 | Findings: 16 | Verdict: FAIL
tokens used
388,402
