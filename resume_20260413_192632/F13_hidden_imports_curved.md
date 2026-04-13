# F13_hidden_imports_curved (551s)

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:41` — PROBLEM: This paragraph treats `thm:bar-cobar-adjunction` as the full adjunction with unit, counit, and Verdier compatibility, but the live label in [chapters/theory/cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1904) is only the geometric unit theorem. FIX: replace the sentence beginning “The precise content of Theorem~A...” with: “The geometric unit is Theorem~\ref{thm:bar-cobar-adjunction}. The full unit/counit package on the Koszul locus is Theorem~\ref{thm:bar-cobar-isomorphism-main}; bar-cobar inversion is Theorem~\ref{thm:bar-cobar-inversion-qi}; Verdier intertwining is Theorem~\ref{thm:verdier-bar-cobar}.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:37` — PROBLEM: “Bar-cobar preserves quasi-isomorphisms because it is a quantum \(L_\infty\) functor...” is not what `thm:operadic-homotopy-convolution` states in [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:880); that theorem gives one-slot \(sL_\infty\) functoriality of convolution, not a blanket bar-cobar quasi-isomorphism theorem. FIX: replace those two sentences with: “The relevant homotopy-invariant object is the convolution \(L_\infty\)-algebra of Theorem~\ref{thm:operadic-homotopy-convolution}. We use it only to control Maurer--Cartan data under one-slot \(\infty\)-morphisms.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:367` — PROBLEM: `prop:curved-bar-acyclicity` claims ordinary cohomological acyclicity, but the proof conflates the curved fiberwise differential \(\dfib\) with the strict total differential \(\Dg{g}\), replaces chain-level \(\omega_g\) by cohomological \(\lambda_g\), and then invokes Positselski on a different CDG surface. It also asserts \(m_1^2\neq0\) at line 381, contradicting this file’s own remark at line 255 that central \(m_0\) can give \(m_1^2=0\) even when \(d_{\mathrm{fib}}^2\neq0\). FIX: retract the proposition as an ordinary-cohomology claim. Replace it by: “For \(g\ge1\) and \(\kappa(\cA)\neq0\), the fiberwise bar object is a nonzero-curvature CDG-coalgebra; ordinary cohomology is not the correct invariant, and the relevant statement is the coderived/contraderived equivalence of Theorem~\ref{thm:positselski-chiral-proved}.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:977` — PROBLEM: Theorem~\ref{thm:completed-bar-cobar-strong}(2) identifies the completed cobar object with the twisted tensor product \(\cA\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\cA)\). Those are different objects: the cobar object is free on \(s^{-1}\bar C\); the twisted tensor product is the acyclicity complex from [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:689). FIX: replace item (2) by “\(\widehat\Omega^{\mathrm{ch}}(\widehat{\bar B}^{\mathrm{ch}}(\cA))\) is a separated complete curved dg chiral algebra.” Then add: “The associated completed twisted tensor product \(\cA \widehat\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\cA)\) is the acyclic resolution used in item~(3).”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:5711` — PROBLEM: The proof of `thm:central-implies-strict` says it is recalling `def:bar-differential-complete`, but that definition in [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:510) only defines \(d_{\mathrm{internal}}+d_{\mathrm{residue}}+d_{\mathrm{form}}\). It never defines the `d_correction` term used in the nine-term expansion, so the proof expands an undefined operator. FIX: delete the nine-term proof. If the intended claim is \(m_1^2=[\mu_0,-]\), cite Theorem~\ref{thm:curvature-central}. If the intended claim is higher-genus flatness, cite Theorem~\ref{thm:quantum-diff-squares-zero}. Do not keep this as a proved-here theorem until the corrected differential is defined first.

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:6592` — PROBLEM: `thm:bar-functorial-grothendieck` is circular: it derives \(d_{\bar B}^2=0\) from the adjunction, but the adjunction already presupposes a valid dg coalgebra structure on \(B(\mathcal A)\). It also cites `thm:bar-cobar-adjunction`, which is only the geometric unit theorem. FIX: downgrade this to a remark/corollary. Keep functoriality by citing `thm:bar-functorial`, and cite `thm:central-implies-strict` or `thm:quantum-diff-squares-zero` for nilpotence. Remove the sentence “This adjunction automatically implies \(d_{\mathrm{bar}}^2=0\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:403` — PROBLEM: Remark~\ref{rem:derived-coderived-chiral-CDG} uses `thm:coalgebra-via-NAP}(4)` to justify conilpotency of \(\bar B^{\mathrm{ch}}(\cA)\), but [poincare_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality.tex:356) is a theorem about \(\mathcal A^!\), not about the bar coalgebra. This is an object switch. FIX: replace lines 407-411 by a direct bar-length proof: “For the reduced bar coalgebra, the reduced coproduct lowers bar length, so \(\bar\Delta^{(N)}\) vanishes on words of length \(<N\); hence \(\bar B^{\mathrm{ch}}(\cA)\) is conilpotent.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:502` — PROBLEM: Example~\ref{ex:w-algebra-filtered-comprehensive} treats \(T,W,{:}TT{:},\dots\) as curvature pieces \(\mu_0^{(2)},\mu_0^{(3)},\mu_0^{(4)}\). In this chapter, \(\mu_0\) is a nullary curvature operation, not a list of generators. FIX: replace the display by filtration data, e.g. \(F^2\mathcal W_3=\langle T\rangle\), \(F^3\mathcal W_3=\langle T,W,\partial T\rangle\), \(F^4\mathcal W_3=\langle T,W,\partial T,{:}TT{:},\partial W,\dots\rangle\), and conclude: “The higher-weight relations are not encoded by a single central \(\mu_0\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:533` — PROBLEM: The proof of `thm:filtered-to-curved` hides the whole filtered duality step. It sets \(\mathcal A=\mathcal C^\vee\), invokes `prop:filtered-to-curved-fc`, and then says “dualizing back” preserves the curved identity, but no lemma in this file proves that continuous dualization exchanges filtered chiral cooperads and filtered chiral algebras or preserves the curved structure. FIX: insert a lemma before line 514 proving filtered finite-type duality and exactness on the quotient tower; otherwise downgrade the theorem to a conditional corollary.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:588` — PROBLEM: `thm:conilpotency-convergence` says conilpotency makes “the Koszul duality \(A\leftrightarrow A^!\) well-defined without taking \(\hat A\),” but the proof only establishes that the bar-cobar reconstruction map is well-defined. \(A^!\) is not produced by bar-cobar inversion. FIX: replace item (3) and the closing sentence of the proof by “the unreduced bar-cobar reconstruction map \(\Omega(\bar B(A))\to A\) is well-defined without completion.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5625` — PROBLEM: This regime summary says Regime III uses the strong-filtration axiom, but Proposition~\ref{prop:standard-strong-filtration} at lines 1147-1150 explicitly says the standard conformal-weight filtration does not satisfy that axiom on \(\cA\) itself. The file contradicts itself on the main completion criterion. FIX: replace lines 5623-5629 by: “Regime III uses an auxiliary bar-level weight filtration. In special towers satisfying Definition~\ref{def:strong-completion-tower}, the strong-filtration axiom is sufficient; for the standard conformal-weight filtration one instead uses Proposition~\ref{prop:mc4-weight-cutoff}.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5942` — PROBLEM: The Kac--Moody example identifies the curvature as \(k\cdot K\) and then switches to the scalar genus curvature \(\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)\). That conflates the level, the central extension generator, and the bar-curvature scalar. FIX: replace lines 5942-5949 by: “The OPE central term is governed by the level \(k\). The genus-\(g\) bar curvature used here is the scalar \(m_0^{(g)}=\kappa(\widehat{\fg}_k)\lambda_g\,\mathbf1\), where \(\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5979` — PROBLEM: The \(W_3\) example switches from the weight-cutoff completion developed earlier to an augmentation-ideal completion \(\varprojlim_n \bar B(W_3)/I^n\) with no comparison theorem. FIX: replace `\varprojlim_n \bar B(W_3)/I^n` by the weight-completed bar tower used earlier, or insert a theorem comparing the augmentation-ideal and conformal-weight completions before using them interchangeably.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5988` — PROBLEM: `\label{eq:mc-equation}` is attached to a blank line, not an equation environment; line 6496 therefore points to a phantom equation. The neighboring `ex:` alias labels are also live labels without matching environments. FIX: delete lines 5987-5990. Put a real equation label on the displayed MC equation inside Definition~\ref{def:mc-element-curved}, e.g. `\label{eq:curved-mc-equation}`, and change line 6496 to reference that new label.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:308` — PROBLEM: `thm:completion-necessity` is marked `\ClaimStatusProvedElsewhere`, but lines 319-330 are manuscript-specific claims about the strong-filtration axiom and Theorem~\ref{thm:completed-bar-cobar-strong}. FIX: end the external theorem at line 317 and move lines 319-330 into a separate local remark.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5541` — PROBLEM: The curved Maurer--Cartan definition and twisting theorem omit the nilpotence/completeness hypothesis needed for the infinite series to converge. FIX: add “Assume \(A\) is nilpotent or complete filtered so that the MC series and twisted operations converge.” If that is not intended, downgrade the theorem to a formal remark.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5642` — PROBLEM: The claim that \(\dfib\) is not a coderivation because the cross terms produce “twice the contribution” has no cited proof or local computation. FIX: delete that sentence unless you add a proposition computing \(\Delta\circ\dfib-(\dfib\otimes\mathrm{id}+\mathrm{id}\otimes\dfib)\circ\Delta\) with explicit signs.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5879` — PROBLEM: Remark~\ref{rem:voa-central-curvature} says the curvature equals the central charge or level times \(\mathbf1\). That is false on this chapter’s own scalar lane for affine Kac--Moody. FIX: replace that clause by “the fiberwise bar curvature is the family-specific scalar \(\kappa(\mathcal A)\) times the vacuum, or \(\kappa(\mathcal A)\omega_g\,\mathbf1\) on the genus-\(g\) fiber.”

- [LOW] `chapters/theory/bar_cobar_adjunction_curved.tex:6210` — PROBLEM: The “computational verification through genus~5” remark gives no test name, file, computation label, or citation. FIX: either delete the remark or replace it with a concrete reference to the compute surface and test count.

## Summary
Checked: 14 files/surfaces | Findings: 18 | Verdict: FAIL


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
session id: 019d87f4-65e3-7571-8509-72c6985c72a6
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


MISSION: FOUNDATION AUDIT of chapters/theory/bar_cobar_adjunction_curved.tex

Same: search for hidden imports. Especially for the strong filtration, weight completion, and curved bar-cobar.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Exploring import issues**

The user is asking about hidden imports and unresolved references. I might need to run a build check for that file or relevant chapter. It seems important to read the local file and check dependencies, and possibly cross-reference theorem labels. I wonder if using claim-surface-sync is necessary, but I'll focus on the minimal set like deep-beilinson-audit. After the initial exploration, I'll think about updating the plan based on what I find.
codex
Using `deep-beilinson-audit` for the adversarial pass, then `build-surface` only if the local surface suggests unresolved references or verification debt. I’m starting by reading the target file in context, then tracing its hidden imports, labels, and any dependencies it silently relies on.
Plan update
  → Read audit prerequisites and the target file with surrounding context
  • Trace hidden imports, referenced labels, and dependency files actually used by the target surface
  • Run narrow verification checks for unresolved refs, missing definitions, and internal consistency
  • Produce a severity-ordered audit with exact fixes and verified line references
codex
I’m pulling the live surface from source rather than relying on registry prose. The next pass is target-file context plus every label or definition this chapter pulls in implicitly.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "bar_cobar_adjunction_curved|curved bar|bar-cobar adjunction|strong filtration|weight completion|curved" chapters/connections/concordance.tex metadata/theorem_registry.md CLAUDE.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
\chapter{Bar-cobar adjunction and curved Koszul duality}
\label{chap:bar-cobar-adjunction}

The bar-cobar adjunction $\Omegach \dashv \barBch$ represents the
space of twisting morphisms
$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
by a pair of functors between chiral algebras and conilpotent
chiral coalgebras on $\Ran(X)$
(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
morphism
$\tau_\cA \in \MC\bigl(\operatorname{Conv}(\barBch(\cA), \cA)\bigr)$
is the genus-$0$ binary component of the MC element
$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
cohomology, so the counit
$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
is a quasi-isomorphism on the Koszul locus.
 exited 2 in 52ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
CLAUDE.md:363:**grading / curved**
CLAUDE.md:366:- B48. `m_1^2 = 0` universally in curved A-inf. CORRECT: `m_1^2(a) = [m_0, a]`. AP46.
CLAUDE.md:377:- B56. "Curved SC^{ch,top}-algebra" for the genus >= 1 bar complex. FALSE. It is a curved A_infinity-chiral algebra. The curvature d^2_{fib} = kappa * omega_g is on the A_infinity structure, not on an SC structure. AP165.
CLAUDE.md:408:- B80. Two obstruction complexes for one obstruction. The same obstruction class Ob_g may live in different complexes with different H^2. Exactness in one complex (e.g., modular-bootstrap H^2=0) does NOT imply exactness in another (e.g., curved-Dunn twisting-cochain). Always specify WHICH complex.
CLAUDE.md:537:| C | PROVED | C0 in D^co unconditional (curved well-typedness resolved via coderived fiber-center); C0 ordinary-cohomology conditional on perfectness. C1 g>=1 duality (genus-0 separated); reflexivity from perfectness (not hidden). C2 conditional on uniform-weight; object identity fixed; center-to-bar lift proved. ALT PROOF: PTVV shifted symplectic (H03). |
CLAUDE.md:593:**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.
CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
metadata/theorem_registry.md:61:| `chapters/theory/bar_cobar_adjunction_curved.tex` | 113 |
metadata/theorem_registry.md:125:#### `chapters/theory/bar_cobar_adjunction_curved.tex` (113)
metadata/theorem_registry.md:130:| `prop:curved-bar-acyclicity` | `proposition` | 367 | Acyclicity of curved bar complexes |
metadata/theorem_registry.md:131:| `thm:filtered-to-curved` | `theorem` | 515 | When filtered reduces to curved |
metadata/theorem_registry.md:247:| `prop:filtered-to-curved` | `proposition` | 345 | Filtered implies curved |
metadata/theorem_registry.md:444:| `thm:curved-koszul-pairs` | `theorem` | 6220 | Curved Koszul pairs |
metadata/theorem_registry.md:522:| `thm:curved-mc-cobar` | `theorem` | 2150 | Curved Maurer--Cartan equation |
metadata/theorem_registry.md:534:| `cor:curved-differential` | `corollary` | 3415 | Curved differential formula |
metadata/theorem_registry.md:700:#### `chapters/theory/filtered_curved.tex` (2)
metadata/theorem_registry.md:704:| `prop:filtered-to-curved-fc` | `proposition` | 16 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
metadata/theorem_registry.md:705:| `thm:bar-convergence-fc` | `theorem` | 171 | Convergence criterion in the filtered/curved regimes |
metadata/theorem_registry.md:826:| `thm:bar-curved-ch-infty` | `theorem` | 1881 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
codex
The target file is already showing scope-risk: it imports many results by label, and several strong claims are being made in the introduction before any local proof surface appears. I’m reading the full file with line numbers now and cross-checking each imported dependency against what it actually states.
exec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '120,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "ls archive/raeeznotes/raeeznotes100 && sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   120	| `prop:circ-associative` | `proposition` | 1124 | Associativity of the composition product |
   121	| `thm:geometric-bridge` | `theorem` | 1612 | Geometric realization |
   122	| `prop:orthogonal` | `proposition` | 1800 | Orthogonality |
   123	| `prop:chirAss-self-dual` | `proposition` | 2242 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
   124	
   125	#### `chapters/theory/bar_cobar_adjunction_curved.tex` (113)
   126	
   127	| Label | Env | Line | Title |
   128	|---|---|---:|---|
   129	| `thm:curvature-central` | `theorem` | 262 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
   130	| `prop:curved-bar-acyclicity` | `proposition` | 367 | Acyclicity of curved bar complexes |
   131	| `thm:filtered-to-curved` | `theorem` | 515 | When filtered reduces to curved |
   132	| `thm:conilpotency-convergence` | `theorem` | 584 | Conilpotency ensures convergence |
   133	| `comp:virasoro-spectral-r-matrix` | `computation` | 757 | Virasoro spectral R-matrix on primary states |
   134	| `lem:degree-cutoff` | `lemma` | 931 | Degree cutoff: finite MC equation at each stage |
   135	| `thm:completed-bar-cobar-strong` | `theorem` | 950 | MC element lifts to the completed convolution algebra |
   136	| `prop:standard-strong-filtration` | `proposition` | 1097 | Standard weight truncations and the induced bar filtration |
   137	| `prop:mc4-reduction-principle` | `proposition` | 1217 | Reduction of MC4 to finite-stage compatibility |
   138	| `cor:mc4-degreewise-stabilization` | `corollary` | 1282 | Degreewise stabilization criterion for MC4 |
   139	| `cor:mc4-surjective-criterion` | `corollary` | 1319 | Finite-dimensional surjectivity criterion for MC4 |
 succeeded in 51ms:
     1	\chapter{Bar-cobar adjunction and curved Koszul duality}
     2	\label{chap:bar-cobar-adjunction}
     3	
     4	The bar-cobar adjunction $\Omegach \dashv \barBch$ represents the
     5	space of twisting morphisms
     6	$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
     7	by a pair of functors between chiral algebras and conilpotent
     8	chiral coalgebras on $\Ran(X)$
     9	(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
    10	morphism
    11	$\tau_\cA \in \MC\bigl(\operatorname{Conv}(\barBch(\cA), \cA)\bigr)$
    12	is the genus-$0$ binary component of the MC element
    13	$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
    14	$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
    15	Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
    16	that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
    17	product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
    18	cohomology, so the counit
    19	$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
    20	is a quasi-isomorphism on the Koszul locus.
 succeeded in 52ms:
informal_claim_harvest.csv
label_status_conflicts.csv
master_claim_ledger_filtered.csv
provisionally_dismissed_claims.csv
red_team_summary.md
suspicious_proved_claim_dependencies.csv
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

thinking
**Evaluating file structure**

I can use scripts to look for any undefined references and cited dependencies not found in the file. Using grep for "ref{" seems like a good option! I should probably use an update plan to mark step 1 as done once I have enough context. Now, I need to inspect the structure of the file, including the section headings, subsections, labels, and line count — I think using `rg` could help with that!
codex
I’ve confirmed the file is large and status-dense. I’m mapping its sections, theorem labels, cross-references, and citation surface first so the audit can target hidden imports rather than just local prose defects.
exec
/bin/zsh -lc 'wc -l chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
p=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex')
text=p.read_text()
labels=re.findall(r'\\\\label\\{(["'^}]+)'"\\}', text)
refs=re.findall(r'\\\\(?:eq)?ref\\{(["'^}]+)'"\\}', text)
cites=re.findall(r'\\\\cite\\{(["'^}]+)'"\\}', text)
print('labels', len(labels))
print('refs', len(refs), 'unique', len(set(refs)))
print('cites', len(cites))
missing=sorted(set(refs)-set(labels))
print('internal_missing_labels_sample', missing[:80])
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^'"\\\\(section|subsection|subsubsection|begin\\{(theorem|proposition|lemma|corollary|definition|remark|computation)\\}|label\\{|ref\\{|cite\\{)\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    7218 chapters/theory/bar_cobar_adjunction_curved.tex
 exited 2 in 51ms:
rg: regex parse error:
    (?:^\(section|subsection|subsubsection|begin\{(theorem|proposition|lemma|corollary|definition|remark|computation)\}|label\{|ref\{|cite\{))
                                                                                                                                             ^
error: unopened group
 exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "rg -n -e '"'^'"\\\\section' -e '"'^'"\\\\subsection' -e '"'^'"\\\\subsubsection' -e '"'^'"\\\\begin\\{theorem\\}' -e '"'^'"\\\\begin\\{proposition\\}' -e '"'^'"\\\\begin\\{lemma\\}' -e '"'^'"\\\\begin\\{corollary\\}' -e '"'^'"\\\\begin\\{definition\\}' -e '"'^'"\\\\begin\\{remark\\}' -e '"'^'"\\\\begin\\{computation\\}' -e '\\\\label\\{' -e '\\\\ref\\{' -e '\\\\eqref\\{' -e '\\\\cite\\{' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
p=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex')
text=p.read_text()
labels=set(re.findall(r'\\\\label\\{(["'^}]+)'"\\}', text))
refs=re.findall(r'\\\\(?:eqref|ref)\\{(["'^}]+)'"\\}', text)
refset=set(refs)
print('labels', len(labels))
print('refs', len(refs), 'unique', len(refset))
missing=sorted(refset-labels)
print('refs_not_defined_in_same_file', len(missing))
for x in missing[:200]:
    print(x)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1064

2:\label{chap:bar-cobar-adjunction}
9:(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
15:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
42:(Theorem~\ref{thm:bar-cobar-adjunction}) is this: there is an
56:(Definition~\ref{def:convolution-dg-lie}); at the homotopy level,
59:(Theorem~\ref{thm:operadic-homotopy-convolution}). On the strict
63:(Theorem~\ref{thm:curvature-central}), so the bar differential
78: MC4 completion (proved; Theorem~\ref{thm:completed-bar-cobar-strong}).
80:This hierarchy is codified in Convention~\ref{conv:regime-tags} and
84:(\S\ref{sec:curved-koszul-i-adic}--\S\ref{sec:reconstruction-duality-casimir})
88:second (\S\ref{sec:filtered-vs-curved-comprehensive}--\S\ref{sec:cech-hca})
94:(Chapter~\ref{chap:higher-genus}) amounts to deforming the
99:\begin{remark}[The ordered bar as primitive]
100:\label{rem:bar-ordered-primacy}
109:Chapter~\ref{ch:ordered-associative-chiral-kd}, the cofree
112:\begin{equation}\label{eq:bar-ordered-to-symmetric}
138: \textup{(}equation~\eqref{eq:intro-kappa-from-r}\textup{)}: the
164:Chapter~\ref{ch:ordered-associative-chiral-kd}, and the passage
 succeeded in 52ms:
labels 265
refs 610 unique 220
refs_not_defined_in_same_file 60
app:nilpotent-completion
ch:genus-expansions
ch:ordered-associative-chiral-kd
chap:higher-genus
chap:koszul-pairs
conv:bar-coalgebra-identity
conv:higher-genus-differentials
conv:regime-tags
cor:critical-level-universality
cor:level-shifting-part1
def:bar-differential-complete
def:chiral-koszul-pair
def:convolution-dg-lie
def:geometric-bar
def:primitive-defect-series
def:resonance-rank
def:twisting-morphism


thinking
**Inspecting file claims and proofs**

I need to inspect the claims statuses in the file, as there might be dependencies on theorems that are either proven elsewhere or nonexistent. I'm thinking about potential issues like theorem/proof mismatches and hidden imports, such as `prop:filtered-to-curved-fc` from another file. There could be errors in the filtration inequality direction from AP199. I plan to check relevant sections for definitions and proofs to confirm the integrity of the theorems and propositions involved.
thinking
**Gathering proof content**

I need to pinpoint the exact line numbers and gather proof content around specific sections. I'm thinking about reading chunks from lines 240 to 700, then 880 to 1230, and 1210 to 1700, possibly extending further if necessary. I also want to check relevant lines from other files, like `filtered_curved.tex`, `higher_genus_modular_koszul.tex`, and `bar_cobar_adjunction_inversion.tex`, along with definitions from various sources to ensure everything aligns accurately.
codex
The risk concentration is where the file starts asserting “proved here” bridges from filtered data to completed bar-cobar. I’m now reading the actual proof blocks around `thm:filtered-to-curved`, `thm:completed-bar-cobar-strong`, and the strong-filtration machinery, then checking whether the imported labels really carry the hypotheses being used.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '880,1260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '240,700p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1260,1715p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   240	% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
   241	\begin{remark}[Gravity dictionary for curved \texorpdfstring{$A_\infty$}{A-infinity}]
   242	\label{rem:curved-ainfty-gravity-dictionary}
   243	For genus $g \geq 1$, the curved fiberwise bar model carries the scalar curvature element
   244	\[
   245	 m_0^{(g)} = \kappa(\mathcal{A}) \cdot \omega_g \cdot \mathbf{1},
   246	 \qquad
   247	 \omega_g = c_1(\lambda) \in H^2(\overline{\mathcal{M}}_g),
   248	\]
   249	where $\lambda = \det \mathbb{E}$ is the Hodge line bundle on the moduli space. The fiberwise differential satisfies
   250	\[
   251	 d_{\mathrm{fib}}^2 = \kappa(\mathcal{A}) \cdot \omega_g,
   252	\]
   253	while the total bar differential still satisfies $d_{\mathrm{bar}}^2 = 0$. This gives the gravity dictionary:
   254	\begin{enumerate}[label=(\roman*)]
   255	\item $m_0^{(g)} \neq 0$ if and only if $\kappa(\mathcal{A}) \neq 0$, equivalently if and only if $d_{\mathrm{fib}}^2 \neq 0$. This is the precise sense in which gravity is turned on. The scalar curvature term $m_0^{(g)}$ is the cosmological-constant term of the genus-$g$ curved $A_\infty$ model. This statement is fiberwise. For the standard families $m_0^{(g)}$ is central, so the internal commutator formula $m_1^2 = [m_0,-]$ may vanish even when $d_{\mathrm{fib}}^2 \neq 0$.
   256	\item $\kappa(\mathcal{A})$ is the coefficient of the Hodge class in $d_{\mathrm{fib}}^2$, hence the strength of the genus-$g$ gravitational backreaction. In that dictionary, $\kappa(\mathcal{A})$ is the Newton coupling. It is family-specific: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$ for affine Kac--Moody, $\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro, and $\kappa(\mathcal{B}^k) = c/6$ for Bershadsky--Polyakov.
   257	\item The critical gravitational coupling is the fixed point of the duality involution on the scalar lane. When the scalar complementarity constant is written as $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = K_\kappa(\mathcal{A})$, the fixed point is $\kappa_{\mathrm{crit}} = K_\kappa(\mathcal{A})/2$. This constant is family-specific. For affine Kac--Moody, Heisenberg, and free-field families one has $K_\kappa = 0$, so $\kappa_{\mathrm{crit}} = 0$. For Virasoro one has $K_\kappa = 13$, so $\kappa_{\mathrm{crit}} = 13/2$, equivalently $c = 13$. For the Bershadsky--Polyakov family the manuscript uses $\kappa(\mathcal{B}^k) = c/6$ together with the central-charge conductor $c(\mathcal{B}^k) + c((\mathcal{B}^k)^!) = 196$; hence the self-dual central charge is $c = 98$, and the induced scalar critical coupling is $\kappa_{\mathrm{crit}} = 49/3$.
   258	\end{enumerate}
   259	\end{remark}
 succeeded in 51ms:
  1260	\to H^m(\widehat{C})
  1261	\to \varprojlim_N H^m(C_N) \to 0.
  1262	\]
  1263	Assumption~\textup{(2)} kills the derived limit term
  1264	$\varprojlim^1$, so the first claim follows.
  1265	
  1266	For the second claim, the maps $\epsilon_N$ assemble by
  1267	Assumption~\textup{(3)} into a morphism of inverse systems. Passing to
  1268	limits therefore gives a map
  1269	$\widehat{\epsilon}\colon \Omega(\widehat{C}) \to \varprojlim_N \cA_{\le N}$.
  1270	The finite-stage maps are quasi-isomorphisms, so after applying the
  1271	first part to the bar complexes and the same Milnor argument to the
  1272	compatible cobar tower, $\widehat{\epsilon}$ induces an isomorphism on
  1273	cohomology. The continuity hypothesis ensures that the completed cobar
  1274	differential is well defined, so $\widehat{\epsilon}$ is a
  1275	quasi-isomorphism.
  1276	\end{proof}
  1277	
  1278	% \label{rem:mc4-concrete-checklist} removed (echo of Proposition~\ref{prop:mc4-reduction-principle})
  1279	
 succeeded in 51ms:
   880	which is a Maurer--Cartan element in the convolution algebra
   881	$\operatorname{Conv}(\bar B^{\mathrm{ch}}(\cA_{\le N}),
   882	\cA_{\le N})$
   883	(Definition~\ref{def:twisting-morphism}).
   884	The MC4 completion problem asks: \emph{when do these finite-stage
   885	MC elements assemble to an MC element
   886	$\widehat\tau \in
   887	\MC\bigl(\widehat{\operatorname{Conv}}(\widehat{\bar B}^{\mathrm{ch}}(\cA),
   888	\cA)\bigr)$
   889	in the completed convolution algebra?}
   890	The answer is that a single axiom on the filtration (that
   891	the $A_\infty$~operations respect the additive weight) makes
   892	the MC equation $\partial(\widehat\tau) + \widehat\tau \star
   893	\widehat\tau = 0$ converge in the inverse limit. Each component
   894	of this equation involves only finitely many terms
   895	(Lemma~\ref{lem:degree-cutoff}), so the passage to the completion
   896	is automatic.
   897	
   898	\begin{definition}[Strong completion tower]
   899	\label{def:strong-completion-tower}
codex
A second defect surface is appearing later in the file: duplicated “strict vs homotopy” foundations that may override or contradict the earlier curved-material lane. I’m reading that back half now because hidden imports are often disguised as repeated local “foundations” sections.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6628,7218p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6245,6628p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5530,6245p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6245	 = \circ_{\Gamma' \circ \Gamma}$, and for $\sigma \in \mathrm{Aut}(\Gamma)$
  6246	 the maps are $\sigma$-equivariant.
  6247	\item The identity $\partial^2 = 0$ on $\barB^{(g,n)}(\cA)$ is a formal
  6248	 consequence of the boundary-of-boundary relation $\partial^2 = 0$ on the
  6249	 stratification of $\overline{\mathcal{M}}_{g,n}$.
  6250	\end{enumerate}
  6251	\end{theorem}
  6252	
  6253	\begin{proof}
  6254	Part~(i) is the stable-graph bar differential construction of
  6255	Lemma~\ref{lem:stable-graph-d-squared}: each edge $e \in E(\Gamma)$ contributes
  6256	a contraction against the propagator $P_\cA$, and the composition
  6257	$\circ_\Gamma$ is the iterated contraction over all internal edges.
  6258	
  6259	Part~(ii) follows from the associativity of edge contraction on stable graphs.
  6260	If $\Gamma' \to \Gamma$ is a refinement (collapsing a subset of edges of
  6261	$\Gamma'$ to produce $\Gamma$), then contracting in two stages (first the
  6262	edges internal to each $\Gamma'_v$, then the remaining edges of $\Gamma$) gives
  6263	the same result as contracting all edges of $\Gamma'$ at once. Equivariance
  6264	under automorphisms is immediate from the symmetric monoidal structure of the
 succeeded in 52ms:
  6628	\end{remark}
  6629	
  6630	%% ================================================================
  6631	%% RECONSTRUCTION, DUALITY, AND THE CASIMIR TRANSGRESSION
  6632	%% ================================================================
  6633	
  6634	\section{Reconstruction, duality, and the Casimir transgression}
  6635	\label{sec:reconstruction-duality-casimir}
  6636	\index{reconstruction!versus duality}
  6637	\index{Casimir transgression|textbf}
  6638	\index{Sugawara coupling!bar complex}
  6639	
  6640	There are two natural operations on the bar complex of a chiral
  6641	algebra, and they are not the same. The first applies the cobar
  6642	functor directly: $\Omegach(\barBch(\cA)) \to \cA$. This is
  6643	\emph{reconstruction}: it recovers~$\cA$ from its collision data,
  6644	and Theorem~B says it is a quasi-isomorphism on the Koszul locus.
  6645	The second interposes Verdier duality on the Ran space:
  6646	$\Omegach(\mathbb{D}_{\Ran}\barBch(\cA))$. This is
  6647	\emph{duality}: it produces the Koszul dual partner~$\cA^!$, not
 succeeded in 52ms:
  5530	to the foundational algebraic layer: the role of Maurer--Cartan
  5531	elements in the curved setting, the genus-by-genus obstruction
  5532	analysis, the bar complex as an algebra over the modular operad, and
  5533	the separation of reconstruction from duality that underlies the
  5534	entire monograph.
  5535	
  5536	\subsection{Maurer--Cartan elements and deformation theory}
  5537	\label{sec:maurer-cartan-curved}
  5538	
  5539	\begin{definition}[Maurer--Cartan element in curved context]
  5540	\label{def:mc-element-curved}
  5541	For a curved $A_\infty$ algebra $(A, \{\mu_n\})$, a \emph{Maurer--Cartan element} is $\alpha 
  5542	\in A^1$ satisfying:
  5543	\begin{equation}
  5544	\sum_{n \geq 0} \mu_n(\alpha^{\otimes n}) = 0
  5545	\end{equation}
  5546	\end{definition}
  5547	
  5548	\begin{theorem}[Twisting by MC elements {\cite{LV12}}; \ClaimStatusProvedElsewhere]
  5549	\label{thm:twisting-mc}



thinking
**Identifying findings in code audit**

I need to pinpoint any issues clearly, focusing on severity, specific lines, and solutions. It's crucial to verify using dependency files to avoid any misleading results. I'll aim to find concrete problems while being thorough but not overwhelming. The user wants a comprehensive audit, so I might compile 15-25 significant findings with precise fixes. I’ll also check for any missing or incorrect labels and may employ scripts to identify undefined labels throughout the repository.
thinking
**Verifying code references and fixes**

I’m examining how to address issues like suggesting a sentence replacement or splitting a theorem into a remark and a theorem. It's essential to verify specific assumptions and check for mismatches, particularly for `prop:filtered-to-curved-fc` and several other terms. I'll also look for hidden imports that might be missing, like `def:bar-differential-complete`, and maybe check for outdated labels such as `eq:mc-equation`. This might lead to a wrong reference, so I need to propose a proper fix or redirect as needed.
thinking
**Reviewing theorem and lemma references**

I’m looking at line 325, which suggests that a strong filtration axiom guarantees that the bar differential on each finite quotient is a finite sum. This seems true because of a supporting lemma. However, the theorem `thm:completion-necessity` references previous work while incorporating conclusions specific to this manuscript. I need to ensure these connections are clear and accurate when presenting this information to keep everything consistent and properly referenced.
codex
I’ve reached the duplicated late section, and it is much worse than a harmless recap: there are live alias labels, undeclared imported definitions, and at least one theorem surface whose proof uses a local formula not defined in the file. I’m cross-checking those imports now against the actual source that supposedly supplies them.
exec
/bin/zsh -lc "nl -ba chapters/theory/filtered_curved.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def:bar-differential-complete|lem:complete-filtered-comparison|thm:bar-functorial\\b|eq:mc-equation\\b|thm:bar-cobar-adjunction\\b|thm:bar-cobar-isomorphism-main\\b|thm:bar-cobar-inversion-qi\\b|thm:modular-characteristic\\b|thm:genus-universality\\b|conv:regime-tags\\b|conv:higher-genus-differentials\\b|thm:quantum-diff-squares-zero\\b|thm:prism-higher-genus\\b|thm:positselski-chiral-proved\\b|thm:positselski-chiral\\b|thm:coalgebra-via-NAP\\b|def:twisting-morphism\\b|def:convolution-dg-lie\\b|thm:operadic-homotopy-convolution\\b|thm:verdier-bar-cobar\\b\" chapters appendices metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess, json
path='chapters/theory/bar_cobar_adjunction_curved.tex'
text=pathlib.Path(path).read_text()
labels=[]
for i,line in enumerate(text.splitlines(),1):
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
        labels.append((m.group(1), i, line.strip()))
for lab in ['ex:maurer-cartan','eq:mc-equation','ex:mc-deformations','ex:mc-periods','ex:curved-ainfty-complete']:
    print('LABEL', lab)
    for x in labels:
        if x[0]==lab:
            print(x)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	% This file is \input'd as part of the Quantum Corrections chapter (quantum_corrections.tex).
     2	% It continues within the preceding chapter and has no \chapter command of its own.
     3	
     4	
     5	\subsection{When does filtering degenerate to curved?}
     6	
     7	A chiral algebra with an exhaustive filtration falls into one of three regimes:
     8	quadratic (Heisenberg, no completion needed), curved (Virasoro, with curvature scalar
     9	$m_0 = \kappa(\mathrm{Vir}_c) \cdot \mathbf{1} = (c/2) \cdot \mathbf{1}$),
    10	or genuinely filtered ($\mathcal{W}_3$,
    11	$\mathcal{W}_N$, where composites such as ${:}LL{:}$ appear at
    12	arbitrarily high weight). The regime determines the convergence criterion
    13	(Theorem~\ref{thm:bar-convergence}) and the shadow archetype
    14	(Gaussian, Lie, contact, mixed) in Part~\ref{part:characteristic-datum}.
    15	
    16	\begin{proposition}[Filtered \texorpdfstring{$\Rightarrow$}{=>} curved; \ClaimStatusProvedHere]\label{prop:filtered-to-curved-fc}
    17	\index{filtered!vs curved}
    18	\index{curved Ainfinity@curved $A_\infty$!filtered comparison}
    19	Let $\mathcal{A}$ be a filtered chiral algebra with an
    20	\emph{exhaustive, separated, complete} filtration
 succeeded in 51ms:
Total output lines: 830

metadata/theorem_registry.md:229:| `thm:bar-functorial-grothendieck` | `theorem` | 6584 | Functoriality of bar construction |
metadata/theorem_registry.md:255:| `thm:positselski-chiral-proved` | `theorem` | 1443 | Positselski equivalence for the chiral bar coalgebra |
metadata/theorem_registry.md:257:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
metadata/theorem_registry.md:264:| `lem:complete-filtered-comparison` | `lemma` | 2580 | Complete filtered comparison lemma |
metadata/theorem_registry.md:315:| `thm:bar-functorial-complete` | `theorem` | 1446 | Bar construction is functorial |
metadata/theorem_registry.md:428:| `thm:bar-cobar-isomorphism-main` | `theorem` | 4055 | Geometric bar--cobar duality |
metadata/theorem_registry.md:770:| `thm:quantum-diff-squares-zero` | `theorem` | 3650 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
metadata/theorem_registry.md:833:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2586 | Bar-cobar isomorphism, retained for equation labels |
metadata/theorem_registry.md:853:| `thm:genus-universality` | `theorem` | 5336 | Genus universality |
metadata/theorem_registry.md:906:| `thm:modular-characteristic` | `theorem` | 2845 | Modular characteristic |
metadata/theorem_registry.md:1193:| `thm:positselski-chiral` | `theorem` | 1264 | Positselski equivalence for the chiral bar coalgebra |
metadata/theorem_registry.md:1323:| `thm:coalgebra-via-NAP` | `theorem` | 356 | Coalgebra structure via NAP |
metadata/theorem_registry.md:1338:| `thm:prism-higher-genus` | `theorem` | 645 | Prism principle: higher-genus extension |
appendices/homotopy_transfer.tex:531:of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} is the
appendices/homotopy_transfer.tex:584:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): on the Koszul locus,
appendices/homotopy_transfer.tex:729:(Convention~\ref{conv:higher-genus-differentials}), and the
appendices/homotopy_transfer.tex:737:Theorem~\textup{\ref{thm:genus-universality}} is the nullary
appendices/homotopy_transfer.tex:866:(Theorem~\ref{thm:genus-universality}).
 succeeded in 52ms:
LABEL ex:maurer-cartan
('ex:maurer-cartan', 5987, '\\label{ex:maurer-cartan}%')
LABEL eq:mc-equation
('eq:mc-equation', 5988, '\\label{eq:mc-equation}%')
LABEL ex:mc-deformations
('ex:mc-deformations', 5989, '\\label{ex:mc-deformations}%')
LABEL ex:mc-periods
('ex:mc-periods', 5990, '\\label{ex:mc-periods}%')
LABEL ex:curved-ainfty-complete
('ex:curved-ainfty-complete', 5665, '\\label{ex:curved-ainfty-complete}')
codex
I’m validating each external label against its actual statement, not the way this chapter paraphrases it. That’s where hidden-import failures usually show up: a local proof borrows a conclusion that the cited theorem never stated.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '500,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2568,2625p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   500	\[\sum_{i,j,k} c_{ijk} \cdot \phi_i(z_1) \otimes \phi_j(z_2) \otimes \phi_k(z_3) \otimes (\eta_{12} \wedge \eta_{23})\]
   501	
   502	\emph{Dimension.} 
   503	\[\dim \bar{B}^{(0),2}(\mathcal{A}) = N^3 \cdot 2\]
   504	
   505	This grows rapidly with $n$.
   506	\end{example}
   507	
   508	\subsubsection{The bar differential}
   509	
   510	\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
   511	\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%
   512	\label{def:bar-diff-detailed}\label{def:diff-total}%
   513	\index{bar complex!differential|textbf}
   514	The bar complex carries a bigrading
   515	$\barB_{p,q}(\cA)$ by \emph{bar degree}~$p$ (number of
   516	desuspended tensor factors minus one) and
   517	\emph{form degree}~$q$. The \emph{cohomological
   518	degree} of a homogeneous element
   519	$s^{-1}\phi_0 \otimes \cdots \otimes s^{-1}\phi_p
 succeeded in 52ms:
  2568	Koszul locus of finite-type chiral algebras. The programmatic regime
  2569	($\mathcal{W}_\infty$, affine Yangians, RTT towers) requires an
  2570	extension of inversion to separated complete inverse limits. The key
  2571	structural input is the strong completion-tower framework developed in
  2572	\S\ref{sec:curved-koszul-i-adic}
  2573	(Definition~\ref{def:strong-completion-tower},
  2574	Theorem~\ref{thm:completed-bar-cobar-strong}); what follows gives the
  2575	homological comparison lemma that underlies the inverse-limit passage
  2576	and develops the inversion-side consequences of the completion closure
  2577	$\CompCl(\Fft)$ (Definition~\ref{def:completion-closure}).
  2578	
  2579	\begin{lemma}[Complete filtered comparison lemma; \ClaimStatusProvedHere]
  2580	\label{lem:complete-filtered-comparison}
  2581	\index{complete filtered comparison lemma|textbf}
  2582	\index{Mittag--Leffler!complete filtered comparison}
  2583	Let $f\colon C \to D$ be a morphism of separated complete filtered
  2584	cochain complexes, with descending filtrations
  2585	$F^\bullet C$ and $F^\bullet D$ satisfying:
  2586	\begin{enumerate}[label=\textup{(\roman*)}]
  2587	\item the quotient towers are surjective: for every~$N$, the
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-adjunction\\}|label\\{def:convolution-dg-lie\\}|label\\{def:twisting-morphism\\}|label\\{thm:operadic-homotopy-convolution\\}|label\\{thm:verdier-bar-cobar\\}|label\\{thm:genus-universality\\}|label\\{conv:higher-genus-differentials\\}|label\\{cor:critical-level-universality\\}|label\\{thm:positselski-chiral-proved\\}|label\\{thm:coalgebra-via-NAP\\}|label\\{thm:prism-higher-genus\\}|label\\{thm:quantum-diff-squares-zero\\}|label\\{thm:modular-characteristic\\}\" chapters/theory chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2848:\label{thm:modular-characteristic}
chapters/theory/poincare_duality_quantum.tex:645:\ClaimStatusProvedHere]\label{thm:prism-higher-genus}
chapters/theory/bar_cobar_adjunction_inversion.tex:1443:\label{thm:positselski-chiral-proved}
chapters/theory/poincare_duality.tex:356:\begin{theorem}[Coalgebra structure via NAP; \ClaimStatusProvedHere]\label{thm:coalgebra-via-NAP}
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
chapters/theory/higher_genus_foundations.tex:5339:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
chapters/theory/higher_genus_foundations.tex:5966:\begin{corollary}[Universal genus-$1$ criticality criterion; scalar-lane collapse; \ClaimStatusProvedHere]\label{cor:critical-level-universality}
chapters/theory/algebraic_foundations.tex:405:\label{def:convolution-dg-lie}
chapters/theory/algebraic_foundations.tex:670:\label{def:twisting-morphism}
chapters/theory/algebraic_foundations.tex:882:\label{thm:operadic-homotopy-convolution}%
chapters/theory/cobar_construction.tex:1320:\label{thm:verdier-bar-cobar}
chapters/theory/cobar_construction.tex:1905:\label{thm:bar-cobar-adjunction}
chapters/theory/higher_genus_complementarity.tex:3555:\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1880,1945p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '390,730p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '220,290p;5330,5395p;5958,5985p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1880	This kernel reconstructs the chiral multiplication from the coalgebra data.
  1881	\end{example}
  1882	
  1883	\begin{theorem}[Cobar as free chiral algebra; \ClaimStatusProvedHere]\label{thm:cobar-free}
  1884	As a graded chiral algebra (forgetting the differential), the cobar
  1885	construction $\Omega^{\mathrm{ch}}(\mathcal{C})$ is the free chiral
  1886	algebra generated by $s^{-1}\bar{\mathcal{C}}$, where
  1887	$\bar{\mathcal{C}} = \ker(\epsilon\colon \mathcal{C} \to \omega_X)$.
  1888	The differential $d_\Omega$ is the unique derivation extending the
  1889	reduced comultiplication
  1890	$\bar{\Delta}\colon \bar{\mathcal{C}} \to
  1891	\bar{\mathcal{C}} \otimes \bar{\mathcal{C}}$
  1892	(this is essential data: $\Omega^{\mathrm{ch}}(\mathcal{C})$ is a
  1893	\emph{DG} chiral algebra, not merely a free algebra).
  1894	\end{theorem}
  1895	
  1896	\begin{proof}
  1897	By construction (Definition~\ref{def:geom-cobar-precise}), the underlying graded chiral algebra of $\Omega^{\mathrm{ch}}(\mathcal{C})$ is $\mathrm{Free}_{\mathrm{ch}}(s^{-1}\bar{\mathcal{C}})$, the free chiral algebra generated by $s^{-1}\bar{\mathcal{C}}$ as a $\mathcal{D}_X$-module. The universal property of free algebras then gives: for any chiral algebra~$\mathcal{A}$ and graded $\mathcal{D}_X$-module morphism $f\colon s^{-1}\bar{\mathcal{C}} \to \mathcal{A}$, there exists a unique chiral algebra morphism $\tilde{f}\colon \mathrm{Free}_{\mathrm{ch}}(s^{-1}\bar{\mathcal{C}}) \to \mathcal{A}$ extending~$f$.
  1898	
  1899	It remains to verify that $d_\Omega$ is a derivation. Since $\mathrm{Free}_{\mathrm{ch}}$ is left adjoint to the forgetful functor, a derivation on a free algebra is determined by its restriction to generators. The restriction $d_\Omega|_{s^{-1}\bar{\mathcal{C}}}$ equals the desuspended reduced comultiplication $s^{-1}\bar{\Delta}\colon s^{-1}\bar{\mathcal{C}} \to (s^{-1}\bar{\mathcal{C}})^{\otimes 2} \hookrightarrow \mathrm{Free}_{\mathrm{ch}}(s^{-1}\bar{\mathcal{C}})$, which is a well-defined map of $\mathcal{D}_X$-modules. The Leibniz extension to all of $\Omega^{\mathrm{ch}}(\mathcal{C})$ is unique, giving $d_\Omega$ as the unique derivation extending $\bar{\Delta}$.
 succeeded in 51ms:
   390	homotopy level it carries an $L_\infty$-structure whose higher
   391	brackets encode the homotopy transfer data
   392	(\cite[Theorem~10.3.8]{LV12}).
   393	More precisely, the convolution dg~Lie algebra is a strict model
   394	$\Convstr(C,P)$ of the homotopy-invariant $L_\infty$-algebra
   395	$\Convinf(C,P)$
   396	(Theorem~\ref{thm:operadic-homotopy-convolution}); the strict model
   397	suffices for all explicit computations in this monograph.
   398	We begin with the classical dg theory
   399	(\cite[\S2.1--2.3]{LV12}) before the chiral generalization
   400	(Chapter~\ref{chap:koszul-pairs}); the hierarchy from dg through
   401	$L_\infty$ to the modular quantum $L_\infty$ appears in
   402	Remark~\ref{rem:convolution-hierarchy}.
   403	
   404	\begin{definition}[Convolution dg Lie algebra]
   405	\label{def:convolution-dg-lie}
   406	\index{convolution dg Lie algebra|textbf}
   407	Let $(C, \Delta, d_C)$ be a conilpotent dg coalgebra and
   408	$(A, \mu, d_A)$ a dg algebra. The \emph{convolution algebra}
   409	$\mathrm{Hom}(C, A)$ is the graded vector space of all linear maps
 succeeded in 52ms:
   220	$\kappa(\cA) = 0$ (flatness) & $\kappa_{\mathrm{eff}} = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$ \\
   221	Coderived category & Off-shell (curved background) \\
   222	Obstruction class $\mathrm{obs}_g$ & One-loop determinant on $\Sigma_g$ \\
   223	Complementarity $Q_g + Q_g' = H^*$ & Matter--ghost pairing
   224	\end{tabular}
   225	\end{center}
   226	These are theorems (Theorem~\ref{thm:brst-bar-genus0}), not analogies.
   227	\end{remark}
   228	
   229	\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
   230	\index{bar differential!higher-genus notation|textbf}
   231	The Feynman transform differential
   232	$d_{\mathrm{FT}} = d_{\mathrm{tree}} + d_{\mathrm{loop}}$
   233	\textup{(}Proposition~\textup{\ref{prop:loop-filtration-compatible})} is
   234	the single canonical differential on the genus-$g$ bar complex. For
   235	computational purposes, three projections of this differential are
   236	used throughout the manuscript.
   237	\begin{enumerate}
   238	\item[\textup{(i)}] \textbf{Fiberwise curved differential} $\dfib$.
   239	 On a fixed curve $\Sigma_g$, the collision-residue differential built
exec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '860,920p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1428,1465p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality_quantum.tex | sed -n '632,665p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   632	the contribution is the non-separating gluing
   633	$\xi_{\mathrm{ns}}\colon \cA(\mathrm{val}(v)) \to
   634	\cA(\mathrm{val}(v) - 2)$.
   635	The identity $d_{\mathrm{FT}}^2 = 0$ follows because each
   636	codimension-$2$ face (edge pair $\{e, e'\}$) appears in
   637	exactly two codimension-$1$ faces with opposite signs
   638	$(-1)^{\epsilon(e,\Gamma)} \cdot (-1)^{\epsilon(e',\Gamma/e)}
   639	+ (-1)^{\epsilon(e',\Gamma)} \cdot
   640	(-1)^{\epsilon(e,\Gamma/e')} = 0$,
   641	the standard boundary-of-boundary cancellation.
   642	\end{definition}
   643	
   644	\begin{theorem}[Prism principle: higher-genus extension;
   645	\ClaimStatusProvedHere]\label{thm:prism-higher-genus}
   646	The operadic identification extends to all genera via the
   647	modular operad structure on $\{\overline{\mathcal{M}}_{g,n}\}$
   648	(Definition~\ref{def:modular-operad}).
   649	Precisely:
   650	\begin{enumerate}[label=\textup{(\roman*)}]
   651	\item The collection $\mathcal{M}od = \{\overline{\mathcal{M}}_{g,n}
 succeeded in 52ms:
  1428	from the finite-generation hypothesis on~$\cA$.
  1429	\end{remark}
  1430	
  1431	\subsection{Application: the Positselski equivalence on the chiral bar-coalgebra surface}
  1432	\label{subsec:positselski-chiral-equivalence}
  1433	
  1434	The chiral comodule-contramodule correspondence applies directly to the
  1435	bar coalgebra. Its intrinsic output is a coderived/contraderived
  1436	equivalence for $\barB^{\mathrm{ch}}(\cA)$ and its contramodules; only
  1437	on additional finite-type or genus-$0$ bar-dual surfaces may one
  1438	rewrite the target in terms of ordinary modules over an explicit dual
  1439	algebra.
  1440	
  1441	\begin{theorem}[Positselski equivalence for the chiral bar coalgebra;
  1442	\ClaimStatusProvedHere]
  1443	\label{thm:positselski-chiral-proved}
  1444	\index{Positselski!chiral equivalence|textbf}
  1445	\index{comodule-contramodule correspondence!chiral Koszul|textbf}
  1446	For a Koszul chiral algebra $\cA$ on a smooth curve $X$ with
  1447	curved bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$
 succeeded in 52ms:
   860	obtained by restricting to genus~$0$ ($\hbar \to 0$) and truncating
   861	to lower homotopy operations. The shadow obstruction tower
   862	$\Theta^{\leq r}$ in row~4 is the primary proved content;
   863	the five main theorems are read off from this full tower, with
   864	Theorem~D extracting the scalar level $\Theta^{\leq 2} = \kappa$
   865	(Remark~\ref{rem:unifying-principle}).
   866	
   867	Each row admits a \emph{homotopy upgrade}: the dg~Lie bracket
   868	$[-,-]$ is the shadow of a full $L_\infty$-structure whose higher
   869	brackets $\ell_n$ ($n \ge 3$) arise from homotopy transfer through
   870	the convolution Hom functor
   871	(\cite[Theorem~10.3.8]{LV12}, van~der~Laan~\cite{vdL03}). At the
   872	modular level, this produces a \emph{quantum $L_\infty$-algebra}
   873	with operations $\ell_n^{(g)}$ indexed by stable type $(g,n)$
   874	(Theorem~\ref{thm:modular-quantum-linfty}). The dg~level suffices
   875	for the existence of MC elements; the full homotopy level is needed
   876	for transfer to minimal models and for gauge equivalences
   877	(Remark~\ref{rem:full-homotopy-why}).
   878	\end{remark}
   879	

thinking
**Evaluating mathematical concepts**

I need to take a closer look at the quantum differential squares equating to zero, as it might contradict the genus induction theorem. There’s a possibility of confusion here, especially since the later section references the strict genus induction theorem with "d_full" instead of "Dg." I should definitely inspect this further to clarify any discrepancies and better understand what's going on!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3548,3576p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1590,1628p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1310,1338p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3548	\end{itemize}
  3549	
  3550	\emph{Explicit form.} For genus $g=1$ (elliptic case), there is one $A$-period $t_1 = \tau$, and:
  3551	\[\Dg{1} = \dzero + \tau \cdot d_{\text{elliptic}}\]
  3552	where $\tau$ is the modulus of the torus and $d_{\text{elliptic}}$ involves elliptic functions.
  3553	\end{definition}
  3554	
  3555	\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
  3556	\textup{[Regime: curved-central
  3557	\textup{(}i.e., curvature $\kappa$ is a central scalar;
  3558	the theorem proves that $\Dg{g}$ is \emph{flat}\/\textup{)};
  3559	all genera
  3560	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  3561	
  3562	The total corrected differential $\Dg{g}$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))} satisfies $\Dg{g}^{\,2} = 0$.
  3563	\end{theorem}
  3564	
  3565	\begin{proof}
  3566	\emph{Step 1: Expansion of $\Dg{g}^{\,2}$.}
  3567	
 succeeded in 51ms:
  1310	structure constants.
  1311	
  1312	The cobar construction thus provides a geometric derivation
  1313	of the OPE algebra in CFT.
  1314	\end{remark}
  1315	
  1316	\subsection{Verdier duality on bar and cobar}
  1317	
  1318	
  1319	\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
  1320	\label{thm:verdier-bar-cobar}
  1321	\index{Verdier duality!bar-cobar|textbf}
  1322	\textup{[Regime: quadratic, genus-$0$
  1323	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1324	
  1325	Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
  1326	Koszul dual.
  1327	
  1328	Write
  1329	\[
 succeeded in 51ms:
  1590	%================================================================
  1591	
  1592	\section{Bar-cobar inversion}
  1593	\label{sec:bar-cobar-inversion-quasi-iso}
  1594	
  1595	The comodule-contramodule correspondence of the preceding section
  1596	provides the categorical framework in which bar-cobar inversion
  1597	lives: at genus~$0$ the coderived category reduces to the
  1598	ordinary derived category, and the inversion theorem is a
  1599	quasi-isomorphism in the classical sense; at genus~$g \geq 1$
  1600	the curvature forces passage to the coderived setting, and the
  1601	inversion theorem becomes a statement about coderived equivalences.
  1602	The central result of this chapter is the following.
  1603	
  1604	\subsection{Statement of the main result}
  1605	
  1606	\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
  1607	\textup{[Regime: quadratic on the strict lane; curved-central and
  1608	filtered-complete on the coderived lane
  1609	\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}

thinking
**Inspecting theorem details**

I need to check the actual statement of the bar-cobar isomorphism and see if it covers adjunction and Verdier. I should also look around line 6341 where it mentions bar-cobar isomorphism. I think inspecting around line 4072 might be relevant too. There's a lot to unpack here, so I want to make sure I’m thorough in understanding these concepts and how they relate to one another.
codex
One foundational mismatch is now confirmed from source: this chapter repeatedly treats `thm:bar-cobar-adjunction` as the full adjunction with counit and Verdier compatibility, but the live labeled theorem is only the geometric unit statement. I’m checking the neighboring theorem surface to see which label actually carries the stronger content.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4068,4145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-adjunction\\}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"eq:mc-equation\\b\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4068	Theorem~A identifies the conditions under which $\cA^!_\infty$ is
  4069	\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.
  4070	
  4071	\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
  4072	\label{thm:bar-cobar-isomorphism-main}
  4073	\index{bar-cobar duality!main theorem|textbf}
  4074	\index{Theorem A|textbf}
  4075	\textup{[}Regime: quadratic on the Koszul locus
  4076	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  4077	The unit maps in part~\textup{(1)} are equivalences in the derived
  4078	category of conilpotent complete factorization coalgebras on
  4079	$\operatorname{Ran}(X)$. The counit maps in part~\textup{(1)} and all
  4080	post-Verdier identifications in parts~\textup{(2)}--\textup{(3)} are
  4081	equivalences in the derived category
  4082	$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
  4083	factorization algebras on~$X$.
  4084	
  4085	\smallskip\noindent
  4086	The Heisenberg instance was verified in~\S\ref{sec:frame-inversion}.
  4087	In general:
 succeeded in 51ms:
chapters/theory/cobar_construction.tex:1905:\label{thm:bar-cobar-adjunction}
standalone/five_theorems_modular_koszul.tex:616:\label{thm:bar-cobar-adjunction}
 succeeded in 52ms:
tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:305:equation~(\ref{eq:mc-equation}). The algebraic-family
standalone/shadow_towers.tex:522:\begin{equation}\label{eq:mc-equation}
standalone/shadow_towers.tex:566:The MC equation~\eqref{eq:mc-equation}, projected onto
standalone/N6_shadow_formality.tex:252:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary.tex:1158:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary.tex:1204:MC equation~\eqref{eq:mc-equation} imposes a quadratic
standalone/programme_summary.tex:2292:equation~(\ref{eq:mc-equation}). The algebraic-family
standalone/programme_summary_sections2_4.tex:583:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary_sections2_4.tex:629:MC equation~\eqref{eq:mc-equation} imposes a quadratic
standalone/koszulness_fourteen_characterizations.tex:902:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary_sections9_14.tex:315:equation~(\ref{eq:mc-equation}). The algebraic-family
standalone/shadow_towers_v3.tex:603:\begin{equation}\label{eq:mc-equation}
chapters/theory/bar_cobar_adjunction_curved.tex:5988:\label{eq:mc-equation}%
chapters/theory/bar_cobar_adjunction_curved.tex:6002:\begin{equation}\label{eq:mc-equation-DISABLED}
chapters/theory/bar_cobar_adjunction_curved.tex:6496:is equation~\eqref{eq:mc-equation} in the field theory context:





thinking
**Analyzing findings systematically**

I might consider using regex to identify duplicate labels within the same file or across files, though it seems like checking relevant label alias lines could be more necessary. Inspecting the theorem registry could help with file counts and any duplicates. 

I need to highlight some potential findings:  
1. The introduction claims that Theorem A, `thm:bar-cobar-adjunction`, gives a complete adjunction, but it misstates the theorem because it only describes the geometric unit. I should correct the references to distinguish between different theorems accurately.  
2. There's a claim regarding the preservation of quasi-isomorphisms related to quantum L_infty functors.
thinking
**Clarifying theorem interpretations**

It seems the cited theorem, operadic-homotopy-convolution, only indicates that the one-slot hom^alpha functor extends to infinity-morphisms in either slot. It doesn’t directly address the bar-cobar functor or the preservation of gauge invariance for quasi-isomorphisms. This raises concerns about unsupported claims or possible overstatements in the interpretation of the theorem. I should keep this in mind as I analyze the findings further to ensure accurate conclusions.
thinking
**Evaluating theorem structure**

I see that theorem completion-necessity line 308 references ProvedElsewhere with citations, but the content in lines 319-330 seems to add internal manuscript ideas that aren't sourced, which complicates things. I think it might be a good plan to split the theorem; the external theorem could finish at line 317, moving the internal content into a local remark or roadmap. The proof of lines 344-350 uses an infinite sum, which could be invalid in a discrete bar complex context. However, it might still serve as a hypothetical illustration.
thinking
**Considering proposition adjustments**

I think this needs clarification. I should explicitly state that "the formal family of terms is not an element;" the crucial point is that the completed differential in the completion must accommodate an arbitrary number of contributions. The severity of this issue might be low to medium. As for the proposition on curved-bar-acyclicity, I’ll want to revisit lines 370-384 to see how it fits with the adjustments made. It’s about ensuring clarity throughout!
thinking
**Investigating theorem details**

I'm looking into the chiral bar complex related to the coalgebra-via-NAP theorem in conformance weight grading with exhaustive filtration. It seems I need to confirm if the theorem supports that specific statement. I think it would be helpful to closely inspect line 356 in the poincare_duality.tex document to get more clarity. Let's make sure everything aligns correctly!
exec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality.tex | sed -n '340,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   340	
   341	\emph{Counit.}
   342	\[\epsilon: \mathcal{A}^! \to \omega_X\]
   343	\[\epsilon(\phi^*) = \langle \phi^*, \mathbb{1}_{\mathcal{A}} \rangle\]
   344	\end{construction}
   345	
   346	\begin{remark}\label{rem:intrinsic-nature}
   347	Construction~\ref{const:A-dual-intrinsic} uses no bar construction, orthogonal relations, or quadraticity
   348	hypothesis.
   349	The Koszul dual is defined by the geometry of configuration spaces
   350	and Verdier duality alone; the bar construction is then identified
   351	with it (Theorem~\ref{thm:bar-computes-dual}), rather than defining it.
   352	\end{remark}
   353	
   354	\subsection{Verification of coalgebra axioms}
   355	
   356	\begin{theorem}[Coalgebra structure via NAP; \ClaimStatusProvedHere]\label{thm:coalgebra-via-NAP}
   357	The construction of $\mathcal{A}^!$ via Verdier duality yields a well-defined conilpotent chiral coalgebra:
   358	\begin{enumerate}
   359	\item \emph{Coassociativity:}




thinking
**Evaluating algebraic connections**

I need to focus on fixing my approach: I can either add and prove a lemma that establishes filtered algebra or cooperad duality, assuming finite-type quotient hypotheses. This would require me to explicitly translate curvature and coderivation identities. Alternatively, I might consider downgrading my theorem to a corollary that depends on the existence of that lemma. It’s about choosing the best path forward for clarity and rigor in my work.
thinking
**Identifying contradictions in chiral algebras**

I'm analyzing this statement about chiral algebras and their central curvature, noting the conflicts between different parts of the document regarding filtered-complete and fiberwise curvature. It seems that there are inconsistencies in filtering and adherence to the strong filtration axiom. Specifically, the claims about standard families and descending conformal-weight filtration contradict earlier propositions. This could be resolved by clarifying the distinction between the auxiliary bar-level weight-cutoff filtration and the strong-filtration axiom, marking this as a significant issue.
thinking
**Examining chiral algebras**

I'm looking at sections 5634-5644, which state that all standard chiral algebras, including W-algebras, have central μ0, suggesting that m1 is strict. I think that's an interesting point to consider, but I want to ensure I'm interpreting it correctly. It might be worth double-checking how this aligns with earlier statements in the document, as I want to avoid any misinterpretations. I'll need to analyze this further for clarity.
thinking
**Evaluating label checks**

I might run a check for labels starting with a specific prefix, but it seems that specific alias lines should suffice. I should see how widely `thm:bar-cobar-adjunction` is used versus `thm:bar-cobar-isomorphism-main` across various line numbers. Also, I'll consider checking for this label in `standalone/five_theorems_modular_koszul.tex`, though it might not be necessary. I could potentially script a detection for mismatched label prefixes, but it doesn’t seem essential right now. Let's keep exploring!
exec
/bin/zsh -lc 'rg -n "bar_cobar_adjunction_curved|thm:completed-bar-cobar-strong|thm:central-implies-strict|thm:filtered-to-curved|prop:curved-bar-acyclicity|thm:bar-functorial-grothendieck" archive/raeeznotes/raeeznotes100/suspicious_proved_claim_dependencies.csv archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 145

archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1601:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,181,thm:curvature-central,theorem,ProvedHere,Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle,"For a curved algebra , the curvature element satisfies: begin{enumerate} item quad (the curvature is a -cycle); item , where is the inner derivation. end{enumerate} In particular, fails to be a differential precisely when is emph{not} central with respect to . For chiral algebras (which are graded-commutative), automatically, so the curvature enters through higher operations ( ) or via the complet",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1602:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,228,thm:completion-necessity,theorem,ProvedElsewhere,When completion is necessary,"Completion is necessary when: begin{enumerate} item emph{Infinite sums}: Operations produce infinite sums not convergent in item emph{Non-conilpotent}: Bar complex is not conilpotent item emph{Non-quadratic}: Relations involve infinitely many generators end{enumerate} For example, the Virasoro algebra and need completion, while Heisenberg and Kac--Moody (conilpotent) do not. The key question is no",medium,"Citation auditor: verify imported theorem matches hypotheses actually used here; hidden mismatches are common at the curve/derived/stack boundary. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.","Provisionally retain, but only after hypothesis matching to the cited external theorem."
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1603:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,285,prop:curved-bar-acyclicity,proposition,ProvedHere,Acyclicity of curved bar complexes,"index{acyclicity!curved bar complex} index{Positselski!acyclicity} Let be a Koszul chiral algebra with nonzero obstruction coefficient . At genus , the curved bar complex has emph{acyclic} underlying cochain complex: .",medium,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1604:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,320,thm:filtered-cooperads,theorem,ProvedElsewhere,Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}),"A emph{filtered cooperad} is more general than a curved cooperad: begin{equation} mathcal{C} = bigcup_{n=0}^ infty F^n mathcal{C} end{equation} where is an increasing filtration, with: begin{enumerate} item Comultiplication: item Counit: end{enumerate} The filtered structure does not reduce to a single curvature element.",low,"Citation auditor: verify imported theorem matches hypotheses actually used here; hidden mismatches are common at the curve/derived/stack boundary. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.","Provisionally retain, but only after hypothesis matching to the cited external theorem."
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1605:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,334,__unlabeled_chapters/theory/bar_cobar_adjunction_curved.tex:334,remark,ProvedElsewhere,Provenance and citation,This theorem is imported and treated as ClaimStatusProvedElsewhere. The filtered-cooperad framework used here is sourced from cite{GLZ22}; subsequent internal reductions in this manuscript are organized by Theorem~ and Theorem~.,low,"Citation auditor: verify imported theorem matches hypotheses actually used here; hidden mismatches are common at the curve/derived/stack boundary. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.","Provisionally retain, but only after hypothesis matching to the cited external theorem."
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1606:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,362,thm:filtered-to-curved,theorem,ProvedHere,When filtered reduces to curved,"Let be a filtered chiral cooperad with exhaustive, separated, complete filtration . Assume: begin{enumerate} item for every ; item is generated in degree with quadratic relations; item higher relation classes differ from quadratic consequences by central filtration- corrections. end{enumerate} Then there exists a curved cooperad with curvature and a filtered quasi-isomorphism [ mathcal{C}_{ mathrm",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1607:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,431,thm:conilpotency-convergence,theorem,ProvedHere,Conilpotency ensures convergence,"index{bar construction!convergence} If is conilpotent, then: begin{enumerate} item The bar-cobar composition converges without completion item All infinite sums in the cobar differential terminate after finitely many steps item The Koszul duality is well-defined without taking end{enumerate}",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1608:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,603,lem:arity-cutoff,lemma,ProvedHere,Arity cutoff: finite MC equation at each stage,"index{arity cutoff} For a strong completion tower, the MC equation in involves only arities : the bar differential on is a finite sum.",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1609:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,622,thm:completed-bar-cobar-strong,theorem,ProvedHere,MC element lifts to the completed convolution algebra,index{completed bar-cobar!strong completion tower} index{MC4!completion closure theorem} index{twisting morphism!completed} Let be a strong completion tower textup{(}Definition~ textup{)}. Write for the universal twisting morphism at stage~ . Then: begin{enumerate} item emph{Completed coalgebra.} The completed bar construction exists as a separated complete pronilpotent curved dg chiral coalgebra ,medium,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1610:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,764,prop:mc4-reduction-principle,proposition,ProvedHere,Reduction of MC4 to finite-stage compatibility,"Let be the inverse system of finite-stage bar complexes [ C_N := bar B( cA_{ le N}), qquad widehat{C} := varprojlim_N C_N, ] for a tower satisfying the finite-stage hypotheses of Theorem~. Assume: begin{enumerate} item each transition map is a morphism of complexes; item for every cohomological degree~ , the inverse system satisfies the Mittag--Leffler condition; and item the finite-stage bar-coba",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1611:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,829,cor:mc4-degreewise-stabilization,corollary,ProvedHere,Degreewise stabilization criterion for MC4,"In the setting of Proposition~, assume in addition that for every cohomological degree~ there exists such that the transition maps [ H^m(C_{N+1}) longrightarrow H^m(C_N) ] are isomorphisms for all . Then: begin{enumerate} item the inverse system is Mittag--Leffler; item the completed cohomology stabilizes at the finite stage, [ H^m( widehat{C}) cong H^m(C_{N(m)}); ] item every compatible system of",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1612:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,866,cor:mc4-surjective-criterion,corollary,ProvedHere,Finite-dimensional surjectivity criterion for MC4,"In the setting of Proposition~, assume in addition that for every cohomological degree~ : begin{enumerate} item each is finite-dimensional; and item there exists such that the transition maps [ H^m(C_{N+1}) longrightarrow H^m(C_N) ] are surjective for all . end{enumerate} Then the inverse system is Mittag--Leffler, and every compatible system of finite-stage bar-cobar quasi-isomorphisms induces a ",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1613:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,904,prop:mc4-weight-cutoff,proposition,ProvedHere,Weight-cutoff criterion for MC4,"In the setting of Proposition~, assume in addition that each finite-stage bar complex carries an exhaustive increasing auxiliary-weight filtration [ F_{ le 0}C_N subset F_{ le 1}C_N subset cdots subset C_N ] such that: begin{enumerate} item the differential and the transition maps preserve the filtration; item for each weight bound , the filtered piece is finite-dimensional in every cohomological ",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1614:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,953,prop:winfty-mc4-criterion,proposition,ProvedHere,\texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages,"Let [ W_ infty = varprojlim_N W_N ] be a separated complete infinite-generator -tower whose finite stages lie in the proved principal finite-type regime. Assume: begin{enumerate} item the transition maps are compatible with the finite-stage bar complexe…14983 tokens truncated…y Verdier intertwining: (underlying complex ; Convention~).",medium,"Citation auditor: verify imported theorem matches hypotheses actually used here; hidden mismatches are common at the curve/derived/stack boundary. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.","Provisionally retain, but only after hypothesis matching to the cited external theorem."
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1825:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,6034,cor:genus-expansion-converges,corollary,ProvedHere,Genus expansion convergence,"The genus expansion: begin{equation} Z( mathcal{A}) = sum_{g=0}^ infty hbar^{2g-2} Z_g( mathcal{A}) end{equation} where , converges in the -adic topology of the formal power series ring .",medium,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break. | Moduli-space checker: clutching compatibility, boundary orientation, codimension-two cancellation, and logarithmic normal-crossings hypotheses are the key fragilities.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1826:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,6094,thm:bar-functorial-grothendieck,theorem,ProvedHere,Functoriality of bar construction,"The bar construction: [B: mathrm{ChAlg}^{ mathrm{central}} to mathrm{Coalg} ] is a functor from chiral algebras with central curvature to coalgebras, characterized by the universal property: [ mathrm{Hom}_{ mathrm{Coalg}}(B( mathcal{A}), C) simeq mathrm{Hom}_{ mathrm{ChAlg}}( mathcal{A}, Omega(C)) ] This adjunction automatically implies by the universal property.",low,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1827:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,6203,thm:reconstruction-vs-duality,theorem,ProvedHere,Reconstruction versus duality,"Assume~ lies on the finite chiral Koszul locus and is a finite chiral Koszul pair. Then [ R_X( cA) simeq cA, qquad K_X( cA) simeq cA^ sharp. ]",high,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.
archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv:1828:V1,theory,chapters/theory/bar_cobar_adjunction_curved.tex,6265,thm:recognition-koszul-pairs,theorem,ProvedHere,Recognition theorem for finite chiral Koszul pairs,"index{Koszul pair!recognition theorem} Let and~ be augmented chiral algebras satisfying finite-type and convergence hypotheses. The following are equivalent: begin{enumerate}[label= textup{( roman*)}] item is a finite chiral Koszul pair. item There are quasi-isomorphisms and . end{enumerate} In particular, is a contravariant involution on the finite chiral Koszul locus: .",medium,"Proof auditor: check whether the proof is internal, whether spectral-sequence collapse, formality, or adjunction arguments import unstated finiteness or convergence assumptions. | Hypothesis hunter: isolate exact domain (finite type? simple type? genus zero? principal locus? characteristic zero? perturbative only?). Overstated scope is the default failure mode. | Categorical/geometric auditor: descent, compactification, Verdier duality, and stacky/coherent-vs-derived issues are the main places proofs can break.",Not dismissed by metadata alone; requires localized proof checking. Default stance: provisionally retain with listed attack surfaces.






thinking
**Investigating reference issues**

I’m considering whether to use master ledger lines, but it might not be necessary. I think I need to run a script to check for an environment-label mismatch, especially since there are references like `\label{eq:mc-equation}` outside their environment. The user mentioned issues like hidden imports and unresolved references, specifically pointing to an unresolved alias label problem. 

I should focus on line 6496 for the broken equation label, ensuring to inspect if other references are used properly.
thinking
**Analyzing theorem details**

I'm considering the theorem titled "Acyclicity of Curved Bar Complexes," which discusses ordinary cohomology but references Positselski's coderived category in its proof. I think I need to check the `ClaimStatusProvedElsewhere` flag on the theorem regarding filtered cooperads, which cites GLZ22. However, I can't confirm if GLZ22 really discusses chiral cooperads since I can’t browse the internet. 

I should note that there are internal remarks between lines 487-491 that could clarify this without referencing external literature. The claim about the theorem being proved elsewhere may be problematic since it includes specific internal references instead of valid external citations.
thinking
**Planning fixes for findings**

I need to focus on providing exact fixes based on the file contents, which the user prefers without any external literature references. The user emphasized that for every finding, I must provide precise fixes, not just diagnoses. That means I'll need to think about clear and concise ways to express those fixes. 

I could propose sentence replacements or suggest structural edits that enhance clarity, but it seems I might just need to report these suggestions without directly making the edits myself.
thinking
**Evaluating file checks**

I'm assessing the summary that states "Checked: N | Findings: N." If "Checked: N" indicates how many files were read, I might estimate around 15 files. To be precise, I should say, "Checked: 14 files/surfaces | Findings: 16 | Verdict: FAIL." 

I need to consider both the target file and the 10 dependency files I've read. Keeping accurate counts is important, so I’ll track the specific files I’ve examined. Before finalizing, a quick check for line numbers might be useful.
thinking
**Organizing findings**

I might need to inspect lines around 1743, but I'm not sure if it's necessary. It’s probably best to identify the exact file and line number for each issue. I could generate a structured list of findings sorted by severity, aiming for 12-16 findings overall. A balanced approach is key here, so I’ll focus on high-signal findings with accurate fixes. 

For the critical issues, I’ve started outlining some specific mis-citations and conflated propositions. I’ll continue from there.
thinking
**Analyzing findings and discrepancies**

I'm tallying potential mismatches and issues: there's the adjunction mismatch, the intro L_infty overclaim, and several points regarding acyclicity, central issues, and curvature. I found 18 findings in total. However, I wonder if that seems excessive. Maybe I should also think about pre-edit verification commentary—though I don't think editing is necessary. I should note the plan is complete before wrapping up. This process feels a bit overwhelming, but I’m aiming for thoroughness!
Plan update
Audit surface and dependency statements were read; findings were re-checked against the live source and the cited local labels.
  ✓ Read audit prerequisites and the target file with surrounding context
  ✓ Trace hidden imports, referenced labels, and dependency files actually used by the target surface
  ✓ Run narrow verification checks for unresolved refs, missing definitions, and internal consistency
  → Produce a severity-ordered audit with exact fixes and verified line references

thinking
**Drafting careful fixes**

I’m thinking about how to approach the introduction for L_infty on line 37. I might not need too many details for each bullet; one or two sentences could be enough. It’s important to draft carefully here. I should definitely include "FIX: replace..." with the exact wording, since the user specifically wants the precise fix. Clarity is key, so I'll make sure not to overcomplicate things!
codex
- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:41` — PROBLEM: This paragraph treats `thm:bar-cobar-adjunction` as the full adjunction with unit, counit, and Verdier compatibility, but the live label in [chapters/theory/cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1904) is only the geometric unit theorem. FIX: replace the sentence beginning “The precise content of Theorem~A...” with: “The geometric unit is Theorem~\ref{thm:bar-cobar-adjunction}. The full unit/counit package on the Koszul locus is Theorem~\ref{thm:bar-cobar-isomorphism-main}; bar-cobar inversion is Theorem~\ref{thm:bar-cobar-inversion-qi}; Verdier intertwining is Theorem~\ref{thm:verdier-bar-cobar}.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:37` — PROBLEM: “Bar-cobar preserves quasi-isomorphisms because it is a quantum \(L_\infty\) functor...” is not what `thm:operadic-homotopy-convolution` states in [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:880); that theorem gives one-slot \(sL_\infty\) functoriality of convolution, not a blanket bar-cobar quasi-isomorphism theorem. FIX: replace those two sentences with: “The relevant homotopy-invariant object is the convolution \(L_\infty\)-algebra of Theorem~\ref{thm:operadic-homotopy-convolution}. We use it only to control Maurer--Cartan data under one-slot \(\infty\)-morphisms.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:367` — PROBLEM: `prop:curved-bar-acyclicity` claims ordinary cohomological acyclicity, but the proof conflates the curved fiberwise differential \(\dfib\) with the strict total differential \(\Dg{g}\), replaces chain-level \(\omega_g\) by cohomological \(\lambda_g\), and then invokes Positselski on a different CDG surface. It also asserts \(m_1^2\neq0\) at line 381, contradicting this file’s own remark at line 255 that central \(m_0\) can give \(m_1^2=0\) even when \(d_{\mathrm{fib}}^2\neq0\). FIX: retract the proposition as an ordinary-cohomology claim. Replace it by: “For \(g\ge1\) and \(\kappa(\cA)\neq0\), the fiberwise bar object is a nonzero-curvature CDG-coalgebra; ordinary cohomology is not the correct invariant, and the relevant statement is the coderived/contraderived equivalence of Theorem~\ref{thm:positselski-chiral-proved}.”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:977` — PROBLEM: Theorem~\ref{thm:completed-bar-cobar-strong}(2) identifies the completed cobar object with the twisted tensor product \(\cA\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\cA)\). Those are different objects: the cobar object is free on \(s^{-1}\bar C\); the twisted tensor product is the acyclicity complex from [algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:689). FIX: replace item (2) by “\(\widehat\Omega^{\mathrm{ch}}(\widehat{\bar B}^{\mathrm{ch}}(\cA))\) is a separated complete curved dg chiral algebra.” Then add: “The associated completed twisted tensor product \(\cA \widehat\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\cA)\) is the acyclic resolution used in item~(3).”

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:5711` — PROBLEM: The proof of `thm:central-implies-strict` says it is recalling `def:bar-differential-complete`, but that definition in [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:510) only defines \(d_{\mathrm{internal}}+d_{\mathrm{residue}}+d_{\mathrm{form}}\). It never defines the `d_correction` term used in the nine-term expansion, so the proof expands an undefined operator. FIX: delete the nine-term proof. If the intended claim is \(m_1^2=[\mu_0,-]\), cite Theorem~\ref{thm:curvature-central}. If the intended claim is higher-genus flatness, cite Theorem~\ref{thm:quantum-diff-squares-zero}. Do not keep this as a proved-here theorem until the corrected differential is defined first.

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:6592` — PROBLEM: `thm:bar-functorial-grothendieck` is circular: it derives \(d_{\bar B}^2=0\) from the adjunction, but the adjunction already presupposes a valid dg coalgebra structure on \(B(\mathcal A)\). It also cites `thm:bar-cobar-adjunction`, which is only the geometric unit theorem. FIX: downgrade this to a remark/corollary. Keep functoriality by citing `thm:bar-functorial`, and cite `thm:central-implies-strict` or `thm:quantum-diff-squares-zero` for nilpotence. Remove the sentence “This adjunction automatically implies \(d_{\mathrm{bar}}^2=0\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:403` — PROBLEM: Remark~\ref{rem:derived-coderived-chiral-CDG} uses `thm:coalgebra-via-NAP}(4)` to justify conilpotency of \(\bar B^{\mathrm{ch}}(\cA)\), but [poincare_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality.tex:356) is a theorem about \(\mathcal A^!\), not about the bar coalgebra. This is an object switch. FIX: replace lines 407-411 by a direct bar-length proof: “For the reduced bar coalgebra, the reduced coproduct lowers bar length, so \(\bar\Delta^{(N)}\) vanishes on words of length \(<N\); hence \(\bar B^{\mathrm{ch}}(\cA)\) is conilpotent.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:502` — PROBLEM: Example~\ref{ex:w-algebra-filtered-comprehensive} treats \(T,W,{:}TT{:},\dots\) as curvature pieces \(\mu_0^{(2)},\mu_0^{(3)},\mu_0^{(4)}\). In this chapter, \(\mu_0\) is a nullary curvature operation, not a list of generators. FIX: replace the display by filtration data, e.g. \(F^2\mathcal W_3=\langle T\rangle\), \(F^3\mathcal W_3=\langle T,W,\partial T\rangle\), \(F^4\mathcal W_3=\langle T,W,\partial T,{:}TT{:},\partial W,\dots\rangle\), and conclude: “The higher-weight relations are not encoded by a single central \(\mu_0\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:533` — PROBLEM: The proof of `thm:filtered-to-curved` hides the whole filtered duality step. It sets \(\mathcal A=\mathcal C^\vee\), invokes `prop:filtered-to-curved-fc`, and then says “dualizing back” preserves the curved identity, but no lemma in this file proves that continuous dualization exchanges filtered chiral cooperads and filtered chiral algebras or preserves the curved structure. FIX: insert a lemma before line 514 proving filtered finite-type duality and exactness on the quotient tower; otherwise downgrade the theorem to a conditional corollary.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:588` — PROBLEM: `thm:conilpotency-convergence` says conilpotency makes “the Koszul duality \(A\leftrightarrow A^!\) well-defined without taking \(\hat A\),” but the proof only establishes that the bar-cobar reconstruction map is well-defined. \(A^!\) is not produced by bar-cobar inversion. FIX: replace item (3) and the closing sentence of the proof by “the unreduced bar-cobar reconstruction map \(\Omega(\bar B(A))\to A\) is well-defined without completion.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5625` — PROBLEM: This regime summary says Regime III uses the strong-filtration axiom, but Proposition~\ref{prop:standard-strong-filtration} at lines 1147-1150 explicitly says the standard conformal-weight filtration does not satisfy that axiom on \(\cA\) itself. The file contradicts itself on the main completion criterion. FIX: replace lines 5623-5629 by: “Regime III uses an auxiliary bar-level weight filtration. In special towers satisfying Definition~\ref{def:strong-completion-tower}, the strong-filtration axiom is sufficient; for the standard conformal-weight filtration one instead uses Proposition~\ref{prop:mc4-weight-cutoff}.”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5942` — PROBLEM: The Kac--Moody example identifies the curvature as \(k\cdot K\) and then switches to the scalar genus curvature \(\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)\). That conflates the level, the central extension generator, and the bar-curvature scalar. FIX: replace lines 5942-5949 by: “The OPE central term is governed by the level \(k\). The genus-\(g\) bar curvature used here is the scalar \(m_0^{(g)}=\kappa(\widehat{\fg}_k)\lambda_g\,\mathbf1\), where \(\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)\).”

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5979` — PROBLEM: The \(W_3\) example switches from the weight-cutoff completion developed earlier to an augmentation-ideal completion \(\varprojlim_n \bar B(W_3)/I^n\) with no comparison theorem. FIX: replace `\varprojlim_n \bar B(W_3)/I^n` by the weight-completed bar tower used earlier, or insert a theorem comparing the augmentation-ideal and conformal-weight completions before using them interchangeably.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:5988` — PROBLEM: `\label{eq:mc-equation}` is attached to a blank line, not an equation environment; line 6496 therefore points to a phantom equation. The neighboring `ex:` alias labels are also live labels without matching environments. FIX: delete lines 5987-5990. Put a real equation label on the displayed MC equation inside Definition~\ref{def:mc-element-curved}, e.g. `\label{eq:curved-mc-equation}`, and change line 6496 to reference that new label.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:308` — PROBLEM: `thm:completion-necessity` is marked `\ClaimStatusProvedElsewhere`, but lines 319-330 are manuscript-specific claims about the strong-filtration axiom and Theorem~\ref{thm:completed-bar-cobar-strong}. FIX: end the external theorem at line 317 and move lines 319-330 into a separate local remark.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5541` — PROBLEM: The curved Maurer--Cartan definition and twisting theorem omit the nilpotence/completeness hypothesis needed for the infinite series to converge. FIX: add “Assume \(A\) is nilpotent or complete filtered so that the MC series and twisted operations converge.” If that is not intended, downgrade the theorem to a formal remark.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5642` — PROBLEM: The claim that \(\dfib\) is not a coderivation because the cross terms produce “twice the contribution” has no cited proof or local computation. FIX: delete that sentence unless you add a proposition computing \(\Delta\circ\dfib-(\dfib\otimes\mathrm{id}+\mathrm{id}\otimes\dfib)\circ\Delta\) with explicit signs.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:5879` — PROBLEM: Remark~\ref{rem:voa-central-curvature} says the curvature equals the central charge or level times \(\mathbf1\). That is false on this chapter’s own scalar lane for affine Kac--Moody. FIX: replace that clause by “the fiberwise bar curvature is the family-specific scalar \(\kappa(\mathcal A)\) times the vacuum, or \(\kappa(\mathcal A)\omega_g\,\mathbf1\) on the genus-\(g\) fiber.”

- [LOW] `chapters/theory/bar_cobar_adjunction_curved.tex:6210` — PROBLEM: The “computational verification through genus~5” remark gives no test name, file, computation label, or citation. FIX: either delete the remark or replace it with a concrete reference to the compute surface and test count.

## Summary
Checked: 14 files/surfaces | Findings: 18 | Verdict: FAIL
tokens used
193,324
