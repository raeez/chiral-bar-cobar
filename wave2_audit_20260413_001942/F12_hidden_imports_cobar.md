# F12_hidden_imports_cobar (685s)

- [CRITICAL] chapters/theory/cobar_construction.tex:353 — PROBLEM: `lem:verdier-extension-exchange` is proved by invoking the same identity at line 379 (`\mathbb D_Y\circ j_*\circ \mathbb D_U \cong j_!`), so the proof is circular. FIX: replace lines 363-382 with a derived-Hom/Yoneda proof, or change the lemma to `\ClaimStatusProvedElsewhere` and cite the standard HTT/KS theorem instead of giving a local proof.

- [CRITICAL] chapters/theory/cobar_construction.tex:452 — PROBLEM: the chapter identifies the Verdier-dual residue with `\delta(z_i-z_j)` on `C_n(X)`, but the diagonal is excluded from the open configuration space; the same error drives Example `ex:simplest-cobar` and `d_{\text{extend}}`. FIX: redefine the distributional model on the compactification via `j_!`/boundary currents, and replace every diagonal delta distribution on `C_n(X)` by a boundary current on `\overline C_n(X)`.

- [CRITICAL] chapters/theory/cobar_construction.tex:544 — PROBLEM: `thm:cobar-diff-geom` mixes incompatible bidegrees and decompositions: the statement sends `\Omega_{p,q}` to `\Omega_{p-1,q+1}\oplus\Omega_{p,q}\oplus\Omega_{p+1,q}`, but the three components below preserve `q`; the proof also uses undefined “regularization counterterms.” FIX: choose one decomposition and make the codomain match it; best repair is to define `d_{\mathrm{cobar}}:=\mathbb D(d_{\mathrm{bar}})` abstractly and move the coordinate formulas to a heuristic remark.

- [CRITICAL] chapters/theory/cobar_construction.tex:665 — PROBLEM: `thm:cobar-d-squared-zero` is marked `\ClaimStatusProvedHere`, but its own statement says the rigorous proof is elsewhere and its Term 3 uses formally undefined products like `\delta(z)^2`. FIX: change the environment to `remark` or `verification` with heuristic status, and redirect all rigorous citations to `cor:cobar-nilpotence-verdier`.

- [CRITICAL] chapters/theory/cobar_construction.tex:1387 — PROBLEM: the proof of `thm:bar-cobar-verdier` uses the non-type-correct computation `\int \eta_{ij}\wedge\delta(z_i-z_j)=1`; a logarithmic 1-form is being paired with a scalar regularization without a defined current-valued pairing. FIX: delete Step 3’s Gaussian calculation and replace it with the canonical Verdier evaluation map `\mathbb D\mathcal M\otimes \mathcal M\to\omega`; if an analytic lemma is wanted, prove it separately with precise test-form conventions.

- [CRITICAL] chapters/theory/cobar_construction.tex:1798 — PROBLEM: `prop:cobar-modular-shadow` claims an `\mathrm{FCom}`-algebra structure on `\Omega(\bar B(\cA))`, but the cited source theorem `thm:bar-modular-operad` only gives that structure on the bar complex itself. FIX: restate the proposition for `\bar B(\cA)`, or insert a new theorem proving transport of the modular-operad structure through cobar before using it.

- [CRITICAL] chapters/theory/cobar_construction.tex:1829 — PROBLEM: `thm:cobar-cech` asserts the induced cover is Leray because intersections are contractible “being intersections of coordinate discs in `C_n(X)`”; this is false already for `U\times U\setminus\Delta`. The proof also jumps to `H^p(X^n,\mathcal F_{\mathcal C})`, which is the wrong space. FIX: delete the theorem unless you provide an actual acyclic hypercover of `\overline C_n(X)`; if you keep it, replace `X^n` by the correct configuration space and cite a genuine descent theorem for that cover.

- [CRITICAL] chapters/theory/cobar_construction.tex:1879 — PROBLEM: `thm:bar-cobar-adjunction` is used earlier as a twisting-representability theorem, but the local theorem is only a “geometric unit”; its displayed integral formula is not type-checked, and line 1904 cites `thm:completion-necessity`, which does not prove spectral-sequence convergence. FIX: keep this as `thm:geom-unit` only, change the earlier reference to the actual twisting-representability theorem, and move the integral formula to a remark unless a chain map and convergence proof are supplied.

- [CRITICAL] chapters/theory/cobar_construction.tex:2388 — PROBLEM: `thm:central-charge-cocycle` is ill-typed: `c_1` is defined at lines 2384-2385 in a tensor product of chain groups, but the theorem treats it as a class in `H_1^{(1)}(\mathcal A)`. The proof then inserts a “normalized trace” by fiat. FIX: define a single chain complex and place `c_1` in one explicit degree, or downgrade the theorem to a heuristic example and cite a rigorous genus-1 obstruction theorem instead.

- [CRITICAL] chapters/theory/cobar_construction.tex:2484 — PROBLEM: `thm:genus1-cobar-bar` claims `H^0(\Omega C_\bullet^{(1)}(\mathcal A))\cong\widehat{\mathcal A}` for any vertex algebra with modular characteristic, but the proof never defines the coalgebra structure on `C_\bullet^{(1)}(\mathcal A)` or proves the universal-central-extension claim; line 2522 (“any 2-cocycle factors through the trace pairing”) is an unsupported global assertion. FIX: either restrict the statement to a specific family with a cited computation, or downgrade it to a conjecture/roadmap.

- [CRITICAL] chapters/theory/cobar_construction.tex:2747 — PROBLEM: `thm:essential-image-bar` proves necessity, then switches to slogans for sufficiency (“reading each axiom as a construction step”); no reconstruction theorem is supplied. FIX: keep only the necessity direction as a proved proposition, or downgrade the iff statement to a conjecture until a real reconstruction functor is built.

- [CRITICAL] chapters/theory/cobar_construction.tex:2800 — PROBLEM: `cor:recognition-principle` states an `iff`, but the proof only uses the bar-cobar adjunction on the Koszul locus and never proves the converse. FIX: replace “if and only if” by the one implication actually shown, or mark the converse as conjectural.

- [HIGH] chapters/theory/cobar_construction.tex:187 — PROBLEM: `thm:schwartz-kernel-cobar` gives a pointwise formula for `(K\phi)(z_1,\dots,z_m)` even though the codomain is `\mathcal D'(C_m(X))`, not functions. FIX: replace the displayed formula by the standard kernel identity `\langle K\phi,\psi\rangle=\langle K,\psi\boxtimes\phi\rangle`.

- [HIGH] chapters/theory/cobar_construction.tex:1095 — PROBLEM: `thm:fermion-boson-koszul` is tagged `ProvedHere`, but the proof only cites classical finite-dimensional Koszul duality and “Part~\ref{part:characteristic-datum}`; it does not give a local chiral proof or an exact imported theorem. FIX: either mark it `ProvedElsewhere` and cite the explicit example theorem already in the repo (for example `chapters/examples/beta_gamma.tex` `thm:betagamma-fermion-koszul` if that is the intended statement), or restrict to the exact special case you can prove here.

- [HIGH] chapters/theory/cobar_construction.tex:2127 — PROBLEM: `thm:curved-mc-cobar` bundles a standard algebraic MC equation together with unproved geometric claims about anomalies and genus-1 central extensions. FIX: split it: keep the algebraic curved-MC statement as `ProvedElsewhere` with citation to Positselski/Loday–Vallette, and move the geometric bullets to a remark with explicit hypotheses.

- [HIGH] chapters/theory/cobar_construction.tex:2153 — PROBLEM: `prop:km-bar-curvature` conflates the total bar differential, the internal differential, and higher-genus fiberwise curvature; the final `\mathfrak{sl}_2` calculation does not follow from the preceding equalities. FIX: rewrite the proposition in the fiberwise genus-`g` language already used elsewhere (`m_0^{(g)}=\kappa(\widehat{\mathfrak g}_k)\omega_g`, `d_{\mathrm{fib}}^2=[m_0^{(g)},-]`), keep `d_{\bar B}^2=0` separate, and replace the ad hoc `\mathfrak{sl}_2` paragraph with a checked computation or a citation.

- [HIGH] chapters/theory/cobar_construction.tex:3262 — PROBLEM: `lem:obs-def-pairing` is stated for all genera but lands in `H^{3g-3}`, which is nonsense at `g=0`; the source complementarity theorem only gives the nondegenerate pairing for `g\ge1`. FIX: add the hypothesis `g\ge1` to the lemma, state the `g=0` case separately, and cite `thm:quantum-complementarity-main` for the degree shift.

- [HIGH] chapters/theory/cobar_construction.tex:3389 — PROBLEM: `cor:curved-differential` mixes cohomology classes and their integrals incoherently: `\omega_g` is said to live on `\mathcal M_g`, yet the formula inserts `\int_{\mathcal M_g}\omega_g` into the differential and then squares it to `\omega_g^2`. FIX: replace the display by the class-level identity `d_{\mathrm{fib}}^2=[\mu_0,-]\otimes\omega_g`; if the curvature is central, say that the commutator vanishes and the scalar class records the obstruction.

- [MEDIUM] chapters/theory/cobar_construction.tex:45 — PROBLEM: the chapter calls `thm:bar-cobar-adjunction` the theorem `\operatorname{Tw}(\cC,\cA)=\MC(\operatorname{Conv}(\cC,\cA))`, but the local label is attached to the geometric unit theorem, not to twisting representability. FIX: retarget this reference to the actual twisting-representability theorem, or rename the local theorem/label so the reference matches the statement.

- [MEDIUM] chapters/theory/cobar_construction.tex:503 — PROBLEM: the chapter defines “geometric cobar complex” twice: intrinsically at line 249 and again distributionally at line 503, but never states a clean equivalence before reusing the same notation. FIX: rename line 503 to “Distributional model of the geometric cobar complex” and prepend “By Theorem~\ref{thm:cobar-distributional-model}”.

## Summary
Checked: 30 | Findings: 20 | Verdict: FAIL


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
session id: 019d83e2-81b2-7ca1-b422-a7d370864688
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


MISSION: FOUNDATION AUDIT of chapters/theory/cobar_construction.tex

Same: search for hidden imports. Every 'by Theorem X' — does X exist and prove what's needed?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Planning the audit process**

I need to audit a specific file following the user's instructions. First, it's important to read the constitutional files before making any substantive edits. Although the user requested an audit rather than an edit, there are likely mathematical aspects involved that will still require consulting the mandated files. I should announce using the deep-beilinson-audit skill and inspect the repository. The developer suggests using explorer agents to analyze codebase-related questions, and I'll need to provide regular commentary updates throughout the process.
thinking
**Clarifying the audit requirements**

The user has requested specific fixes, which I can provide as instructions rather than actual edits to the files. It seems they’re looking for an audit rather than an edit, focusing on findings. The directive is clear: for every finding, I need to give an exact fix along with the diagnosis. I must conduct an exhaustive audit of cobar_construction.tex and any hidden imports, checking every referenced theorem. It’s crucial to note the exact line numbers and consider dependencies where applicable. My findings need to be organized by severity, grounding them in the actual file contents.
thinking
**Planning to remove false positives**

I want to ensure that I’m removing any false positives effectively. It seems I might not need to modify the files directly. Instead, I could use tools like rg, sed, or nl for file analysis. An explorer agent could be beneficial, but I could also consider a manual approach using shell commands and a subagent to search for theorem references across the repository. Before diving into that, I’ll provide a commentary update to keep everything clear.
codex
I’m auditing `chapters/theory/cobar_construction.tex` as a hostile proof surface, including hidden imports and every internal theorem dependency. First I’m loading the required constitutional context and the exact local source before I start grading claims.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
exec
/bin/zsh -lc 'pwd && rg -n --no-heading "''^#|''^##|''^###|''^'"\\*\\*|"'^<|''^##" AGENTS.md CLAUDE.md | sed -n '"'1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 200ms:
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

 succeeded in 219ms:
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

 succeeded in 167ms:
/Users/raeez/chiral-bar-cobar
AGENTS.md:1:# AGENTS.md — Modular Koszul Duality Programme (Canonical)
AGENTS.md:5:**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims.
AGENTS.md:11:## I. Mission
AGENTS.md:15:## II. GPT-5.4 Design Axioms
AGENTS.md:30:### GPT-5.4 Prompt Architecture (for composing task prompts)
AGENTS.md:45:**Anti-patterns to avoid**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding.
AGENTS.md:47:## III. Programme Identity (Crystallized 2026-04-12)
AGENTS.md:51:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
AGENTS.md:53:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11.
AGENTS.md:55:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.
AGENTS.md:57:**SC^{ch,top} ≠ E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.
AGENTS.md:59:**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
AGENTS.md:61:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical.
AGENTS.md:63:**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).
AGENTS.md:65:**What we study:** Holomorphic chiral (factorisation) (co)homology via bar and cobar chain constructions at various different geometric locations, hence the different (modular) operads at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
AGENTS.md:67:**North star:** platonic_ideal_reconstituted_2026_04_12.md is THE SINGLE REFERENCE for all structural questions.
AGENTS.md:69:## IV. The Beilinson Principle
AGENTS.md:75:**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.
AGENTS.md:77:## V. Truth Hierarchy
 succeeded in 256ms:
     1	\chapter{The geometric cobar complex}
     2	\label{chap:cobar-construction}
     3	
     4	The bar functor destroys the algebra: it encodes~$\cA$ as a
     5	factorization coalgebra $\barB(\cA)$ from which no multiplication
     6	is directly visible. The cobar complex $\Omega(\cC)$ is the
     7	reconstruction machine that recovers~$\cA$ from this coalgebraic
     8	residue, realizing the inversion
     9	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
    10	proving that the MC element
    11	$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
    12	quasi-isomorphism on the Koszul locus. Both functors are
    13	projections of a single universal twisting morphism
    14	$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
    15	(Definition~\ref{def:twisting-morphism}): bar records collision
    16	residues via the logarithmic propagator
    17	$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
    18	duals over the open configuration space $C_n(X)$.
    19	The duality between them (residues versus delta functions,
    20	$j_*$ versus $j_!$) is the Verdier exchange on

thinking
**Planning task execution**

I’m considering how to parse references in the file and confirm their existence. Maybe using the explorer agent would be helpful? The user didn't ask for anything parallel or delegated, so I think I should avoid spawning an agent. I'm wondering if I can still use multi_tool_use.parallel—seems permissible. I'll probably need to call `update_plan` when I've gathered enough context. It's probably best to set up a longer plan in commentary after the initial read. I'll describe the skill I'm using and communicate that in the update.
codex
I’ve loaded the required constitutional files and the audit skill, and the target file is already exposing risk: it mixes foundational prose, imported theorems, and distribution-theoretic definitions in one chapter. Next I’m enumerating every local label/reference, then I’ll check each dependency in source rather than trusting the prose.
Plan update
Foundation audit plan for chapters/theory/cobar_construction.tex under the deep-beilinson-audit workflow.
  → Map the local claim surface: labels, theorem-like environments, references, and status markers in cobar_construction.tex
  • Verify every imported theorem/definition/lemma used by the chapter against live source and check hypothesis match
  • Attack formulas, object identities, and hidden assumptions inside the chapter line by line
  • Re-check surviving findings against file contents and produce severity-ordered audit output with exact fixes
exec
/bin/zsh -lc "wc -l chapters/theory/cobar_construction.tex && rg -n --no-heading \"\\\\(ref|eqref)\\{["'^}]+'"\\}|Theorem~\\\\ref|Lemma~\\\\ref|Definition~\\\\ref|Proposition~\\\\ref|Corollary~\\\\ref|Chapter~\\\\ref|Convention~\\\\ref\" chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"\\\\label\\{|\\\\ClaimStatus|\\\\begin\\{(theorem|proposition|lemma|corollary|definition|remark|example|conjecture|computation|verification|calculation)\\}\" chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '261,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '781,1040p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '521,780p'" in /Users/raeez/chiral-bar-cobar exited 2 in 389ms:
    3425 chapters/theory/cobar_construction.tex
rg: regex parse error:
    (?:\(ref|eqref)\{[^}]+\}|Theorem~\ref|Lemma~\ref|Definition~\ref|Proposition~\ref|Corollary~\ref|Chapter~\ref|Convention~\ref)
                                                                                                                                 ^
error: unopened group
 exited 2 in 464ms:
rg: regex parse error:
    (?:\label\{|\ClaimStatus|\begin\{(theorem|proposition|lemma|corollary|definition|remark|example|conjecture|computation|verification|calculation)\})
       ^^
error: unrecognized escape sequence
 succeeded in 447ms:
   781	\emph{Rigorous alternative.} A clean proof avoiding distributional issues entirely is given in Corollary~\ref{cor:cobar-nilpotence-verdier} above, which deduces $d^2 = 0$ from Verdier duality on the Fulton--MacPherson compactification without reference to distributional products.
   782	
   783	This completes term~3.
   784	
   785	\emph{Term 4: $d_{\text{comult}} \circ d_{\text{internal}} + d_{\text{internal}} 
   786	\circ d_{\text{comult}} = 0$}
   787	
   788	This states that $\Delta: \mathcal{C} \to \mathcal{C} \boxtimes \mathcal{C}$ is a 
   789	chain map (compatible with the differential). By hypothesis:
   790	\[\Delta \circ d_{\mathcal{C}} = (d_{\mathcal{C}} \otimes \text{id} + \text{id} 
   791	\otimes d_{\mathcal{C}}) \circ \Delta\]
   792	
   793	Applied to cobar elements:
   794	\begin{align*}
   795	(d_{\text{comult}} \circ d_{\text{internal}})(K) &= d_{\text{comult}}\left(\sum_i 
   796	K(\ldots, d_{\mathcal{C}}(c_i), \ldots)\right) \\
   797	&= \sum_{i,j} K(\ldots, \Delta(d_{\mathcal{C}}(c_i)), \ldots)
   798	\end{align*}
   799	
   800	By the chain map property:
 succeeded in 467ms:
   261	\Omega^{\mathrm{ch}}_n(\mathcal{C})
   262	:= \mathbb{D}_{\overline{C}_{n+1}(X)}\!\left(
   263	 j_*\, j^*\bigl((\mathcal{C}^\vee)^{\boxtimes(n+1)}\bigr)
   264	 \otimes \Omega^n_{\overline{C}_{n+1}(X)}(\log D)
   265	\right)
   266	\]
   267	where $j\colon C_{n+1}(X) \hookrightarrow \overline{C}_{n+1}(X)$ is the
   268	inclusion, $D = \partial\overline{C}_{n+1}(X)$ is the boundary divisor, and
   269	$\mathbb{D}_{\overline{C}_{n+1}(X)}$ is the Verdier duality functor on the
   270	compactified configuration space.
   271	
   272	The \emph{cobar differential} is:
   273	\[
   274	d_{\mathrm{cobar}} := \mathbb{D}(d_{\mathrm{bar}})
   275	\]
   276	the Verdier dual of the bar differential
   277	(Definition~\ref{def:bar-differential-complete}).
   278	\end{definition}
   279	
   280	\begin{remark}\label{rem:cobar-intrinsic-meaning}
 succeeded in 502ms:
   521	Equivalently, using the Schwartz kernel theorem (Theorem~\ref{thm:schwartz-kernel-cobar}):
   522	\[\Omega^{\text{ch}}_n(\mathcal{C}) = \text{Dist}\left(C_n(X), \mathcal{C}^{\boxtimes n}\right) 
   523	\otimes \Omega^*_{C_n(X)}\]
   524	consisting of distributional sections of $\mathcal{C}^{\boxtimes n}$ over the open 
   525	configuration space with differential forms.
   526	\end{definition}
   527	
   528	\begin{remark}[Distributions]\label{rem:why-distributions}
   529	The cobar differential inserts delta functions $\delta(z_i - z_j)$, forcing the complex to consist of distributions. Geometrically, distributions on $C_n(X)$ are Verdier-dual to logarithmic forms on $\overline{C}_n(X)$. Physically, cobar operations implement propagator composition: $(\Box - m^2) G(z,w) = \delta^{(2)}(z - w)$.
   530	\end{remark}
   531	
   532	\begin{example}[Simplest cobar element]\label{ex:simplest-cobar}
   533	For $n=2$ with trivial coalgebra $\mathcal{C} = \omega_X$, the basic cobar element is:
   534	\[K_2(z_1, z_2) = \delta(z_1 - z_2) \otimes (dz_1 \wedge d\bar{z}_1)\]
   535	
   536	This acts on test functions $\phi \in \mathcal{D}(C_2(X))$ by:
   537	\[\langle K_2, \phi \rangle = \int_X \phi(z, z) dz \wedge d\bar{z}\]
   538	enforcing the diagonal constraint.
   539	
   540	\emph{Physical meaning.} This is the propagator for a free scalar field with

thinking
**Evaluating file audit strategy**

I might need some rest, especially considering the lengthy task of auditing the entire file, which consists of about 3425 lines. It seems I should initially use grep commands to correct the inspection structure for theorem-like environments. However, since the user wants an exhaustive audit, it feels essential to read through everything—at least every theorem or remark. I’m thinking using 'rg' could help to pinpoint theorem-like environments to streamline the inspection process. Let's gather a structural list for better organization.
codex
The first 1,000 lines already contain hard failures: claimed rigorous theorems with proofs that openly rely on heuristic distribution products, and imported labels that need direct source verification. I’m tightening the audit by mapping every theorem-like block and every `\ref` target in the chapter before I continue through the rest of the file.
exec
/bin/zsh -lc "rg -n --fixed-strings '\\\\begin{' chapters/theory/cobar_construction.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref)\\{["'^}]+'"\\}' chapters/theory/cobar_construction.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\ClaimStatus' chapters/theory/cobar_construction.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\label{' chapters/theory/cobar_construction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 53ms:
15:(Definition~\ref{def:twisting-morphism}): bar records collision
30:(Definition~\ref{def:geom-cobar-intrinsic}), where
37:(Lemma~\ref{lem:verdier-extension-exchange}) identifies the
41:Theorem~\ref{thm:schwartz-kernel-cobar} is the $j_!$-side of the
45:(Theorem~\ref{thm:bar-cobar-adjunction}).
50:(Chapter~\ref{chap:bar-cobar-adjunction}). The total bar differential
53:(Theorem~\ref{thm:bar-modular-operad}) encodes the shadow
55:(Proposition~\ref{prop:cobar-modular-shadow}).
69: (Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}):
73: (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
107: Definition~\ref{def:factorization-coalgebra});
118:(Theorem~\ref{thm:cobar-free}). Bar-cobar inversion
119:(Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}) is stated for
217:(Theorem~\ref{thm:cobar-distributional-model}).
218:See also Definition~\ref{def:conilpotent-complete} for the
239: equation~\eqref{eq:borcherds-axiom}) holds for the
277:(Definition~\ref{def:bar-differential-complete}).
288:(Lemma~\ref{lem:verdier-extension-exchange}).
326:crossings divisor (Theorem~\ref{thm:FM}).
338:(Definition~\ref{def:bar-differential-complete}).
 succeeded in 53ms:

 succeeded in 51ms:

exec
/bin/zsh -lc "rg -n '\\\\begin\\{(theorem|lemma|proposition|corollary|definition|remark|example|conjecture|computation|verification|calculation)' chapters/theory/cobar_construction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{' chapters/theory/cobar_construction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1301,1560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1041,1300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1561,1820p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
61:\begin{remark}[Three functors on the bar coalgebra: cobar is NOT the Koszul dual]
95:\begin{remark}[Which bar complex does the cobar invert?]
127:\begin{remark}[Inverse prism principle]
148:\begin{definition}[Test function space]\label{def:test-functions}
155:\begin{definition}[Distribution space]\label{def:distributions}
165:\begin{example}[Fundamental distributions]\label{ex:fundamental-distributions}
180:\begin{theorem}[Schwartz kernel theorem for cobar {\cite{Hormander}}; \ClaimStatusProvedElsewhere]\label{thm:schwartz-kernel-cobar}
196:\begin{definition}[Conilpotent coalgebra]\label{def:conilpotent-cobar}
222:\begin{definition}[Factorization coalgebra]\label{def:factorization-coalgebra}
249:\begin{definition}[Intrinsic geometric cobar complex]\label{def:geom-cobar-intrinsic}
280:\begin{remark}\label{rem:cobar-intrinsic-meaning}
291:\begin{lemma}[Holonomicity of the bar complex; \ClaimStatusProvedHere]%
352:\begin{lemma}[Verdier duality exchanges extensions; \ClaimStatusProvedHere]%
385:\begin{theorem}[Distributional model of the cobar; \ClaimStatusProvedHere]%
467:\begin{corollary}[\texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality;
480:\begin{remark}[Resolution of delta-function products]\label{rem:delta-product-resolution}
503:\begin{definition}[Geometric cobar complex]\label{def:geom-cobar}
528:\begin{remark}[Distributions]\label{rem:why-distributions}
532:\begin{example}[Simplest cobar element]\label{ex:simplest-cobar}
544:\begin{theorem}[Cobar differential; \ClaimStatusProvedHere]\label{thm:cobar-diff-geom}
 succeeded in 51ms:
2:\label{chap:cobar-construction}
62:\label{rem:cobar-three-functors}
96:\label{rem:cobar-which-bar}
148:\begin{definition}[Test function space]\label{def:test-functions}
155:\begin{definition}[Distribution space]\label{def:distributions}
165:\begin{example}[Fundamental distributions]\label{ex:fundamental-distributions}
180:\begin{theorem}[Schwartz kernel theorem for cobar {\cite{Hormander}}; \ClaimStatusProvedElsewhere]\label{thm:schwartz-kernel-cobar}
194:\subsection{Intrinsic cobar via Verdier duality}\label{subsec:intrinsic-cobar}
196:\begin{definition}[Conilpotent coalgebra]\label{def:conilpotent-cobar}
222:\begin{definition}[Factorization coalgebra]\label{def:factorization-coalgebra}
249:\begin{definition}[Intrinsic geometric cobar complex]\label{def:geom-cobar-intrinsic}
280:\begin{remark}\label{rem:cobar-intrinsic-meaning}
292:\label{lem:bar-holonomicity}
353:\label{lem:verdier-extension-exchange}
386:\label{thm:cobar-distributional-model}
468:\ClaimStatusProvedHere]\label{cor:cobar-nilpotence-verdier}
480:\begin{remark}[Resolution of delta-function products]\label{rem:delta-product-resolution}
501:\subsection{Explicit distributional model}\label{subsec:distributional-model}
503:\begin{definition}[Geometric cobar complex]\label{def:geom-cobar}
528:\begin{remark}[Distributions]\label{rem:why-distributions}
 succeeded in 52ms:
  1561	\emph{Extension.}
  1562	By the universal property of the free chiral algebra
  1563	(Theorem~\ref{thm:cobar-free}), the restriction
  1564	\eqref{eq:augmentation-on-generators} extends uniquely to a
  1565	chiral algebra morphism
  1566	$\varepsilon\colon
  1567	\mathrm{Free}_{\mathrm{ch}}(s^{-1}\overline{B}) \to \mathcal{A}$.
  1568	
  1569	\emph{Low-degree formulas.}
  1570	On generators:
  1571	\begin{align}
  1572	\varepsilon(s^{-1}[s\bar{a}]) &= \bar{a}
  1573	 &&\text{(inclusion of the augmentation ideal),}
  1574	 \label{eq:aug-degree-1} \\
  1575	\varepsilon(s^{-1}[s\bar{a}_1 \mid s\bar{a}_2]) &= 0
  1576	 &&\text{(projection kills bar degree $\geq 2$).}
  1577	 \label{eq:aug-degree-2-gen}
  1578	\end{align}
  1579	On products of generators (by the algebra map property):
  1580	\begin{equation}\label{eq:aug-product}
 succeeded in 53ms:
  1041	
  1042	\emph{Geometric interpretation.} These formulas encode how a single insertion
  1043	point with ``charge'' $v^n$ splits into two insertion points with charges $v^k$ and
  1044	$v^{n-k}$, weighted by binomial coefficients. In CFT, this corresponds to the OPE expansion.
  1045	
  1046	\emph{Cohomology.} Since all generators except $s^{-1}v$ are exact (boundaries 
  1047	of products), the cohomology is:
  1048	\[H^*(\Omega^{\text{ch}}(T^c_{\text{ch}}(V))) = \text{Free}_{\text{ch}}(s^{-1}v)\]
  1049	
  1050	This recovers the original generator $V$, as expected from bar-cobar inversion.
  1051	\end{example}
  1052	
  1053	\begin{example}[Cobar of exterior coalgebra: free fermions]\label{ex:cobar-fermion-complete}
  1054	
  1055	Let $\mathcal{C} = \Lambda^*_{\text{ch}}(V)$ be the chiral exterior coalgebra on 
  1056	$V = \text{span}\{\psi\}$ with $|\psi| = \frac{1}{2}$ (fermionic). The comultiplication:
  1057	\[\Delta(\psi) = \psi \otimes 1 + 1 \otimes \psi, \quad \Delta(\psi^2) = 0\]
  1058	(since $\psi^2 = 0$ by anticommutativity).
  1059	
  1060	\emph{Cobar complex.}
 succeeded in 53ms:
  1301	
  1302	The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
  1303	structure constants.
  1304	
  1305	The cobar construction thus provides a geometric derivation
  1306	of the OPE algebra in CFT.
  1307	\end{remark}
  1308	
  1309	\subsection{Verdier duality on bar and cobar}
  1310	
  1311	
  1312	\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
  1313	\label{thm:verdier-bar-cobar}
  1314	\index{Verdier duality!bar-cobar|textbf}
  1315	\textup{[Regime: quadratic, genus-$0$
  1316	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1317	
  1318	Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
  1319	Koszul dual.
  1320	

thinking
**Identifying findings for audit**

I need to pinpoint specific findings with line numbers and precise fixes, which could add up to many—potentially dozens. The user has asked for a thorough audit, so I'll aim to provide as many issues as possible without getting stuck on every minor detail. I want to be both detailed and accurate in my report. So, let’s keep reading through the entire file and gather the relevant information to present.
codex
I’ve mapped the chapter structure. It is not a small local note; it’s a 3,400-line mixed surface with multiple independently “proved here” theorems, several conjectural physics dictionaries, and repeated foundational definitions. I’m reading the remaining theorem/proof blocks now, because the later sections will determine whether the early defects are isolated or systemic.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1821,2080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2861,3120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2341,2600p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2601,2860p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2081,2340p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1821	Choose a cover $\mathfrak{U} = \{U_\sigma\}_{\sigma \in S}$ of $X$ by coordinate discs. The configuration space $C_n(X)$ inherits an open cover $\mathfrak{U}^{(n)} = \{U_{\sigma_1} \times \cdots \times U_{\sigma_n} \cap C_n(X)\}$. The FM compactification $\overline{C}_n(X)$ is covered by the closures $\overline{U_{\sigma_1} \times \cdots \times U_{\sigma_n}}$ together with boundary coordinate charts at collision strata. The nerve of this cover computes the Čech complex $\check{C}^\bullet(\mathfrak{U}, \mathcal{F}_{\mathcal{C}})$.
  1822	
  1823	\emph{Step 2: Čech-de Rham comparison.}
  1824	On each chart $U_\sigma$, the factorization algebra $\mathcal{F}_{\mathcal{C}}|_{U_\sigma}$ is computed by the cobar complex with local coordinates. The cobar differential $d_\Omega$ on $U_\sigma$ uses the coproduct $\bar{\Delta}$ of $\mathcal{C}$ together with the local propagator $\eta_{ij} = d\log(z_i - z_j)$. On overlaps $U_\sigma \cap U_\tau$, the transition data is encoded by the change-of-coordinate forms, which are $\bar{\partial}$-exact on the holomorphic curve $X$.
  1825	
  1826	The cobar complex $\Omega^{\mathrm{ch}}(\mathcal{C})$ computes global sections of $\mathcal{F}_{\mathcal{C}}$ via integration of local cobar elements against logarithmic forms on $\overline{C}_n(X)$. This is the Čech-de Rham double complex: the Čech direction glues local cobar data across charts, while the de Rham direction is the cobar differential.
  1827	
  1828	\emph{Step 3: Quasi-isomorphism.}
  1829	Since $X$ is a smooth algebraic curve, the FM compactification $\overline{C}_n(X)$ is a smooth variety with normal crossings boundary (Theorem~\ref{thm:normal-crossings}). The cover $\mathfrak{U}^{(n)}$ can be chosen to be a Leray cover: each finite intersection $U_{\sigma_1} \cap \cdots \cap U_{\sigma_k}$ is either empty or contractible (being an intersection of coordinate discs in $C_n(X)$). For a Leray cover of a smooth variety, the Čech-to-derived-functor spectral sequence degenerates at $E_1$, giving:
  1830	\[
  1831	\check{H}^p(\mathfrak{U}, \mathcal{F}_{\mathcal{C}}) \cong H^p(X^n, \mathcal{F}_{\mathcal{C}}).
  1832	\]
  1833	The right-hand side is the factorization homology $\int_X \mathcal{F}_{\mathcal{C}}$, which by the Costello--Gwilliam equivalence (cf.\ \cite{CG17}) agrees with the cobar cohomology $H^*(\Omega^{\mathrm{ch}}(\mathcal{C}))$.
  1834	\end{proof}
  1835	
  1836	\subsection{Integration kernels and cobar operations}
  1837	
  1838	\begin{definition}[Cobar integration kernel]\label{def:cobar-kernel}
  1839	Elements of the cobar complex can be represented by integration kernels:
  1840	\[
 succeeded in 54ms:
  2341	
  2342	This is the first manifestation of the principle that central extensions are intrinsically one-loop phenomena.
  2343	
  2344	\subsubsection{Absence at genus 0}
  2345	
  2346	Consider the genus 0 bar differential on $\mathcal{A} \otimes \mathcal{A}$:
  2347	\[d^{(0)}(a \otimes b) = \mu(a \otimes b) - a \otimes \mathbbm{1} - \mathbbm{1} \otimes b\]
  2348	where $\mu$ is the OPE product.
  2349	
  2350	For central terms: $\mu(a \otimes a^*) \sim \kappa \cdot \mathbbm{1}$
  2351	
  2352	But $d^{(0)}(\kappa \cdot \mathbbm{1}) = \kappa \cdot \mathbbm{1} - \kappa \cdot \mathbbm{1} - \kappa \cdot \mathbbm{1} = -\kappa \cdot \mathbbm{1}$
  2353	
  2354	So the cocycle $a \otimes a^* - \kappa \cdot \mathbbm{1}$ satisfying $d^{(0)}(\cdots) = 0$
  2355	would require $\kappa = 0$. The central charge cannot appear at genus 0.
  2356	
  2357	\subsection{The geometric construction: configuration spaces on the torus}
  2358	
  2359	\subsubsection{Setup: the genus 1 configuration space}
  2360	
 succeeded in 54ms:
  2861	$d = d_{\text{int}} + d_{\text{fact}} + d_{\text{config}}$.
  2862	
  2863	\emph{Step 4: Cohomology.} BRST classes are represented by
  2864	BRST-closed states modulo exact states, and the conjectural
  2865	comparison predicts
  2866	\[
  2867	H^*_{\text{BRST}}
  2868	=
  2869	\text{Ker}(Q_{\text{BRST}})/\text{Im}(Q_{\text{BRST}})
  2870	\cong
  2871	H^*(\barBgeom(\mathcal{A})).
  2872	\]
  2873	\end{remark}
  2874	
  2875	\begin{example}[Bosonic string theory]
  2876	For the bosonic string with central charge $c = 26$:
  2877	
  2878	\emph{Ghost System.} The $(b,c)$ ghost system has OPE:
  2879	\[b(z)c(w) \sim \frac{1}{z-w}\]
  2880	
 succeeded in 51ms:
  2601	\item Free theories (Heisenberg at any level, free fermions with spin structure) extend to all genera without central charge restrictions, as the curvature $m_0$ is central and the obstruction class is scalar (Proposition~\ref{prop:km-bar-curvature}).
  2602	\end{enumerate}
  2603	\end{proof}
  2604	
  2605	\begin{example}[Free fermion extension]
  2606	The free fermion extends to all genera with spin structure:
  2607	
  2608	For genus 1: The extension depends on the choice of spin structure (periodic/antiperiodic boundary conditions):
  2609	\[
  2610	\mathcal{F}_{E_\tau}^{\text{NS}} = \bigoplus_{n \in \mathbb{Z}} \mathcal{F}_n \quad \text{(Neveu--Schwarz)}
  2611	\]
  2612	\[
  2613	\mathcal{F}_{E_\tau}^{\text{R}} = \bigoplus_{n \in \mathbb{Z} + 1/2} \mathcal{F}_n \quad \text{(Ramond)}
  2614	\]
  2615	
  2616	The partition function encodes the obstruction:
  2617	\[
  2618	Z_{\text{ferm}}(\tau) = \frac{\theta_3(0|\tau)}{\eta(\tau)} \quad \text{(NS sector)}
  2619	\]
  2620	\end{example}
 succeeded in 51ms:
  2081	For the free fermion algebra $\mathcal{F}$, bar-cobar inversion gives:
  2082	\[
  2083	\Omega^{\text{ch}}(\bar{B}^{\text{ch}}(\mathcal{F})) \xrightarrow{\sim} \mathcal{F}
  2084	\]
  2085	recovering the free fermion algebra itself (not the $\beta\gamma$ system). The Koszul dual $\mathcal{F}^! \cong \beta\gamma$ is obtained instead by linear duality of the bar coalgebra: $\mathcal{F}^! = \bar{B}^{\text{ch}}(\mathcal{F})^\vee$ (see Example~\ref{ex:fermion-betagamma-bar-cobar} and Theorem~\ref{thm:fermion-boson-koszul}). This distinction is the chiral analog of the classical fact that $\Omega(\bar{B}({\Lambda}(V))) \simeq {\Lambda}(V)$ (bar-cobar inversion), while ${\Lambda}(V)^! = \mathrm{Sym}(V^*)$ (Koszul dual algebra via linear duality).
  2086	\end{example}
  2087	
  2088	
  2089	\subsection{\texorpdfstring{Cobar $A_\infty$ structure}{Cobar A-infinity structure}}
  2090	\label{subsec:cobar-diff-ainfty}
  2091	
  2092	\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure on cobar {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:cobar-ainfty}
  2093	The cobar construction $\Omega^{\text{ch}}(\mathcal{C})$ carries a canonical $A_\infty$ structure with operations:
  2094	\[
  2095	m_k: \Omega^{\text{ch}}(\mathcal{C})^{\otimes k} \to \Omega^{\text{ch}}(\mathcal{C})[2-k]
  2096	\]
  2097	geometrically realized by:
  2098	\[
  2099	m_k(\alpha_1, \ldots, \alpha_k) = \int_{\partial \overline{M}_{0,k+1}} \alpha_1 \wedge \cdots \wedge \alpha_k \wedge \omega_{0,k+1}
  2100	\]
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3121,3425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:verdier-bar-cobar|thm:poincare-verdier|thm:cobar-distributional-model|thm:cobar-diff-geom|thm:cobar-d-squared-zero|thm:genus1-cobar-bar|thm:central-charge-cocycle|thm:essential-image-bar|cor:recognition-principle|thm:cobar-cech|thm:cobar-free|thm:geom-unit|thm:weak-topology|thm:curved-mc-cobar|prop:km-bar-curvature|cor:level-shifting-part1)\\}' chapters metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(def:geom-cobar-precise|thm:bar-cobar-inversion-qi|thm:bar-cobar-isomorphism-main|thm:bar-modular-operad|thm:genus-induction-strict|thm:FM|thm:normal-crossings|thm:arnold-three|def:conilpotent-complete|def:bar-differential-complete|def:chiral-koszul-pair|conv:regime-tags|conv:bar-coalgebra-identity|thm:completion-necessity|thm:obstruction-quantum|thm:prism-higher-genus|thm:fundamental-twisting-morphisms|prop:universal-twisting-adjunction|def:chiral-twisting-datum|lem:degree-cutoff|def:strong-completion-tower|thm:explicit-theta|def:shadow-postnikov-tower|thm:quantum-complementarity-main|thm:quantum-diff-squares-zero|thm:chiral-koszul-duality|prop:cdg-hom-complex|thm:chiral-hochschild-differential|lem:center-cohomology|lem:deformation-space|lem:period-integral|thm:curvature-central|cor:shadow-extraction|thm:mc2-bar-intrinsic|thm:bar-concentration)\\}' chapters appendices metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3121	\[
  3122	m_0^{(g)} = \int_{\Sigma_g} \omega_g \in \bar{B}^0_g(\mathcal{A}),
  3123	\]
  3124	where $\omega_g$ is the volume form of the genus-$g$ propagator
  3125	(cf.\ Definition~\ref{def:genus-stratified-bar}).
  3126	
  3127	\emph{Centrality.}
  3128	The element $m_0^{(g)}$ lies in the center $Z(\mathcal{A})$ by the
  3129	following chain-level argument. For any generator $a \in \mathcal{A}$,
  3130	the OPE $m_0^{(g)}{}_{(n)} a$ for $n \geq 0$ vanishes because $m_0^{(g)}$
  3131	has conformal weight~$0$ (it is a scalar on each conformal-weight space),
  3132	and the Borcherds identity forces the iterated residue
  3133	$[\mathrm{Res}_{D_{ij}}, \mathrm{Res}_{D_{kl}}]$ to act trivially on
  3134	generators when $D_{ij} \cap D_{kl} = \emptyset$ (factorization axiom),
  3135	while nested collisions contribute only scalar multiples (OPE associativity).
  3136	
  3137	\emph{Cocycle condition.}
  3138	The curved $A_\infty$ relation at $n=0$
  3139	(Definition~\ref{def:curved-ainfty}) gives
  3140	$\mu_1(m_0^{(g)}) = 0$, so $m_0^{(g)}$ is a $d$-cocycle. The map
exec
/bin/zsh -lc "rg -n 'cobar_construction\\.tex' metadata/theorem_registry.md | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/cobar_construction.tex:386:\label{thm:cobar-distributional-model}
chapters/theory/cobar_construction.tex:544:\begin{theorem}[Cobar differential; \ClaimStatusProvedHere]\label{thm:cobar-diff-geom}
chapters/theory/cobar_construction.tex:664:\begin{theorem}[Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0}; \ClaimStatusProvedHere]\label{thm:cobar-d-squared-zero}
chapters/theory/cobar_construction.tex:1313:\label{thm:verdier-bar-cobar}
chapters/theory/cobar_construction.tex:1809:\begin{theorem}[Cobar as Čech complex; \ClaimStatusProvedHere]\label{thm:cobar-cech}
chapters/theory/cobar_construction.tex:1857:\begin{theorem}[Cobar as free chiral algebra; \ClaimStatusProvedHere]\label{thm:cobar-free}
chapters/theory/cobar_construction.tex:1878:\begin{theorem}[Geometric unit of adjunction; \ClaimStatusProvedHere]\label{thm:geom-unit}
chapters/theory/cobar_construction.tex:1968:\begin{theorem}[Topology; \ClaimStatusProvedHere]\label{thm:weak-topology}
chapters/theory/cobar_construction.tex:2027:\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
chapters/theory/cobar_construction.tex:2127:\begin{theorem}[Curved Maurer--Cartan equation; \ClaimStatusProvedHere]\label{thm:curved-mc-cobar}
chapters/theory/cobar_construction.tex:2152:\label{prop:km-bar-curvature}
chapters/theory/cobar_construction.tex:2198:\label{cor:level-shifting-part1}
chapters/theory/cobar_construction.tex:2387:\begin{theorem}[Central charge cocycle; \ClaimStatusProvedHere]\label{thm:central-charge-cocycle}
chapters/theory/cobar_construction.tex:2483:\begin{theorem}[Genus 1 cobar-bar duality; \ClaimStatusProvedHere]\label{thm:genus1-cobar-bar}
chapters/theory/cobar_construction.tex:2746:\label{thm:essential-image-bar}
chapters/theory/cobar_construction.tex:2799:\label{cor:recognition-principle}
 succeeded in 53ms:
chapters/theory/configuration_spaces.tex:176:\begin{theorem}[Fulton--MacPherson compactification at genus \texorpdfstring{$g$}{g} \cite{FM94}; \ClaimStatusProvedElsewhere]\label{thm:FM}
chapters/theory/configuration_spaces.tex:483:\begin{theorem}[Normal crossings; \ClaimStatusProvedHere]\label{thm:normal-crossings}
chapters/theory/chiral_hochschild_koszul.tex:173:\label{thm:chiral-hochschild-differential}
chapters/theory/algebraic_foundations.tex:713:{\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{prop:universal-twisting-adjunction}
chapters/theory/higher_genus_complementarity.tex:459:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:3331:\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
chapters/theory/bar_construction.tex:81:\label{conv:bar-coalgebra-identity}
chapters/theory/bar_construction.tex:501:\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
chapters/theory/bar_construction.tex:1189:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-three}
chapters/theory/chiral_koszul_pairs.tex:200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
chapters/theory/chiral_koszul_pairs.tex:400:\label{thm:fundamental-twisting-morphisms}
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:1113:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
chapters/theory/chiral_koszul_pairs.tex:4138:\label{thm:chiral-koszul-duality}
chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
chapters/theory/cobar_construction.tex:3156:\begin{lemma}[Period integral formula {\cite{Fay73}}; \ClaimStatusProvedElsewhere]\label{lem:period-integral}
chapters/theory/cobar_construction.tex:3219:\begin{lemma}[Deformation space; \ClaimStatusProvedHere]\label{lem:deformation-space}
chapters/theory/cobar_construction.tex:3309:\begin{lemma}[Center as obstruction-deformation space; \ClaimStatusProvedHere]\label{lem:center-cohomology}
chapters/theory/bar_cobar_adjunction_curved.tex:258:\label{thm:curvature-central}
 succeeded in 53ms:
492:#### `chapters/theory/cobar_construction.tex` (30)
codex
I’ve now read the full chapter. The failure pattern is systemic, not local: later sections keep promoting sketches, analogies, and imported slogans into `ProvedHere` theorems. I’m cross-checking the chapter’s labels against the theorem registry and the cited source files so I can separate genuine imports from unsupported assertions.
exec
/bin/zsh -lc "if [ -f label_status_conflicts.csv ]; then rg -n 'thm:(cobar|verdier|central-charge-cocycle|genus1-cobar-bar|essential-image-bar|weak-topology|curved-mc-cobar|poincare-verdier)|prop:km-bar-curvature|cor:recognition-principle' label_status_conflicts.csv; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f suspicious_proved_claim_dependencies.csv ]; then rg -n 'cobar_construction\\.tex' suspicious_proved_claim_dependencies.csv; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '492,560p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'cobar_construction\\.tex:.*(Conditional|Conjectured|Heuristic|Open|Unknown)' suspicious_proved_claim_dependencies.csv master_claim_ledger_filtered.csv 2>/dev/null" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 51ms:

 succeeded in 50ms:
#### `chapters/theory/cobar_construction.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 292 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 353 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 386 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 468 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 544 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 665 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 935 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1095 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1313 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1447 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1525 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1798 | Cobar as modular shadow carrier |
| `thm:cobar-cech` | `theorem` | 1810 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1858 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1879 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1969 | Topology |
 exited 2 in 50ms:


thinking
**Verifying references and imports**

I think I might need to check for some missing dependencies and verify the references in my code. I’m not sure if the "suspicious_proved_claim_dependencies" file is in the current working directory, and while it’s not crucial, it could help. I might consider writing a script using a loop to find any missing labels among the references. Compiling a list of references and checking for their corresponding labels sounds like a good plan.
exec
/bin/zsh -lc 'refs=$(rg -o '"'\\\\(?:ref|eqref)\\{["'^}]+'"\\}' chapters/theory/cobar_construction.tex | sed -E 's/.*\\{(["'^}]+)'"\\}.*/\\1/' | sort -u); for r in "'$refs; do hits=$(rg -n --glob '"'*.tex' --glob '*.md' --fixed-strings \"\\\\label{"'$r}" chapters appendices metadata | wc -l | tr -d '"' '); if [ \""'$hits" = "0" ]; then echo "MISSING $r"; elif [ "$hits" != "1" ]; then echo "MULTI $r $hits"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
MISSING app:sign-conventions
app:signs
ch:holographic-datum-master
chap:bar-cobar-adjunction
conj:cobar-physical
conv:bar-coalgebra-identity
conv:higher-genus-differentials
conv:hms-levels
conv:regime-tags
cor:bar-cobar-inverse
cor:cobar-nilpotence-verdier
cor:shadow-extraction
cor:spectral-degeneration
def:bar-differential-complete
def:chiral-CDG-coalgebra
def:chiral-koszul-pair
exec
/bin/zsh -lc "rg -o '\\\\(ref|eqref)\\{["'^}]+'"\\}' chapters/theory/cobar_construction.tex | sed -E 's/.*\\{(["'^}]+)'"\\}.*/\\1/' | sort -u > /tmp/cobar_refs.txt
while IFS= read -r r; do hits="'$(grep -R -n -F "'"\\\\label{"'$r}" chapters appendices metadata 2>/dev/null | wc -l | tr -d '"' '); if [ \""'$hits" = "0" ]; then echo "MISSING $r"; elif [ "$hits" != "1" ]; then echo "MULTI $r $hits"; fi; done < /tmp/cobar_refs.txt' in /Users/raeez/chiral-bar-cobar succeeded in 15.40s:
MULTI conv:hms-levels 2
MULTI conv:regime-tags 2
MISSING part:characteristic-datum
MULTI sec:frame-koszul-dual 2
MULTI subsec:ambient-category 2
MULTI thm:central-charge-complementarity 2
exec
/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\label{subsec:ambient-category}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\label{sec:frame-koszul-dual}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\label{thm:central-charge-complementarity}' chapters appendices" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '\\\\label\\{part:characteristic-datum\\}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:central-charge-complementarity\\}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{sec:frame-koszul-dual\\}' chapters appendices" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '\\\\label\\{subsec:ambient-category\\}' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/heisenberg_frame.tex:1074:\section{Reading off the Koszul dual}\label{sec:frame-koszul-dual}
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1025:\section{Reading off the Koszul dual}\label{sec:frame-koszul-dual}
 succeeded in 52ms:
chapters/theory/introduction.tex:1028:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
 succeeded in 53ms:
chapters/theory/introduction.tex:2602:\label{subsec:ambient-category}
exec
/bin/zsh -lc "rg -n '\\\\label\\{part:' chapters appendices main.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:895:\label{part:bar-complex}
main.tex:1073:\label{part:characteristic-datum}
main.tex:1164:\label{part:standard-landscape}
main.tex:1368:\label{part:physics-bridges}
main.tex:1450:\label{part:seven-faces}
main.tex:1483:\label{part:v1-frontier}

thinking
**Correcting the Grep Scope**

Oh no, I see that the label in main.tex isn't categorized under chapters or appendices, which is causing some confusion. It looks like our grep didn’t cover main.tex, so we should definitely include it along with the root. I’ll rerun the missing check across all the .tex files in the entire repo. I could also consider using `rg -g '*.tex'` to streamline the process, but that's going to involve a lot of files.
exec
/bin/zsh -lc "rg -o '\\\\(ref|eqref)\\{["'^}]+'"\\}' chapters/theory/cobar_construction.tex | sed -E 's/.*\\{(["'^}]+)'"\\}.*/\\1/' | sort -u > /tmp/cobar_refs.txt
while IFS= read -r r; do hits="'$(rg -n -g '"'*.tex' --fixed-strings \"\\\\label{"'$r}" . | wc -l | tr -d '"' '); if [ \""'$hits" = "0" ]; then echo "MISSING $r"; elif [ "$hits" != "1" ]; then echo "MULTI $r $hits"; fi; done < /tmp/cobar_refs.txt' in /Users/raeez/chiral-bar-cobar succeeded in 1.99s:
MULTI conv:hms-levels 2
MULTI conv:regime-tags 2
MULTI lem:degree-cutoff 2
MULTI subsec:ambient-category 2
MULTI thm:central-charge-complementarity 2

thinking
**Inspecting for duplicates**

I'm considering the potential issue of duplicates, particularly those generated by .bak files or related to the degree-cutoff. It seems I may need to inspect these to confirm whether they're active duplicates or if they resulted from some other process. Figuring this out could help streamline things and reduce any confusion or clutter involved. It will be important to ensure everything is clean and organized!
exec
/bin/zsh -lc "rg -n '\\\\label\\{lem:degree-cutoff\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:central-charge-complementarity\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{conv:hms-levels\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{subsec:ambient-category\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{conv:regime-tags\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./standalone/introduction_full_survey.tex:5260:\label{conv:hms-levels}
./chapters/theory/introduction.tex:2514:\label{conv:hms-levels}
 succeeded in 53ms:
./chapters/theory/bar_cobar_adjunction_curved.tex:927:\label{lem:degree-cutoff}
./standalone/N4_mc4_completion.tex:431:\label{lem:degree-cutoff}
 succeeded in 53ms:
./standalone/introduction_full_survey.tex:1755:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
./chapters/theory/introduction.tex:1028:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
 succeeded in 52ms:
./chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
./standalone/introduction_full_survey.tex:5297:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
 succeeded in 52ms:
./chapters/theory/introduction.tex:2602:\label{subsec:ambient-category}
./standalone/introduction_full_survey.tex:5348:\label{subsec:ambient-category}




thinking
**Inspecting dependencies**

I could use theorem_registry or source to look into some cited dependencies. I need to focus on key files around specific labels like geom-cobar-precise and others. I don't need every reference, just those linked to findings. It's important to verify if the imported theorems exist and their statements. I might need to restate or reassess some theorems in the chapter, ensuring exact fixes for each finding. It seems this might be quite extensive!
thinking
**Evaluating proof status**

I’m considering the theorem status "ProvedElsewhere," which includes a proof environment. There might be a proof for AGENTS HZ-8 following a conjecture, but I'm not entirely sure if that’s okay. The theorem states the operator from D(C_n) to D'(C_m) is represented by a kernel in D' of the product, and I need to clarify if these connections hold. It feels like there's a lot to unpack here!
thinking
**Analyzing theorem citations**

I'm questioning the formula in line 187, since it uses pointwise notation and isn't clearly defined if the codomain is D'(C_m). There’s a potential issue there. Line 190 refers to Hormander theorem 5.2.1, which might be fine. I'm considering if lemma proof uses HTT theorem 3.2.3, and whether it's applicable for external product or pullback. I should avoid guessing about the citation's content since I don't have internet access to verify. I can focus on identifying internal issues instead.
thinking
**Identifying potential issues**

I've noticed several potential issues with local references. For example, there are duplicate or inconsistent definitions like "Intrinsic geometric cobar complex" in line 249 and "Geometric cobar complex" in line 503. I'm wondering if they are consistent, as their contexts differ. There's also a duplicate definition of "Distribution space" with vague labeling. And regarding the factorization coalgebra definition at line 222, it includes theorem content within a definition. I might need to flag this as definitional overreach.
exec
/bin/zsh -lc "rg -n 'fermion|beta.?gamma|boson-koszul' chapters appendices -g '*.tex' | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:483:\subsection{\texorpdfstring{Example 3: $\beta\gamma$ system}{Example 3: system}}
chapters/examples/deformation_quantization.tex:494:The $\beta\gamma$ system is a \emph{free} theory: its OPE receives no quantum corrections to the singular terms. The singular part is exactly $1/(z-w)$ to all orders in $\hbar$. Nontrivial higher operations $m_n$ for $n \geq 3$ arise not from corrections to this OPE, but from the geometry of configuration space integrals when the $\beta\gamma$ system is coupled to a background (e.g., via background charge $Q$).
chapters/examples/deformation_quantization.tex:496:The $\beta\gamma$ system is Koszul dual to the $bc$ ghost system: $(\beta\gamma)^! \cong \mathcal{F}_{bc}$. This is a bosonic-to-fermionic ghost system duality realized through chiral Koszul duality (distinct from the standard boson-fermion correspondence/bosonization). The duality is visible at the level of configuration space integrals:
chapters/examples/deformation_quantization.tex:498:where $K_{\text{cobar}} \in H^n_{D}(\overline{C}_n, \mathcal{F}^{!\boxtimes n})$ is the local cohomology class supported on the boundary, and the symplectic (antisymmetric) pairing of $\beta\gamma$ dualizes under Verdier duality to the anticommuting (fermionic) pairing. See Section~\ref{sec:fermion-boson-koszul} for the complete computation.
chapters/examples/w_algebras_deep.tex:273:5 generators (3 from $\widehat{\mathfrak{sl}}_2$ + 2 fermionic), so:
chapters/examples/w_algebras_deep.tex:1982:f_{\min})$ (Computation~\ref{comp:sl3-ds-hierarchy}) has generators $J^a$ ($a = 1, 2, 3$), the $\widehat{\mathfrak{sl}}_2$ currents at level $k' = k + 1/2$ and conformal weight $1$, together with fermionic generators $G^+, G^-$ of conformal weight $3/2$.
chapters/examples/w_algebras_deep.tex:2434:fermionic strong generators) and the non-principal anomaly ratio
chapters/examples/w_algebras_deep.tex:2450:a generator of weight $1 - s$ (imitating the $\beta\gamma_\lambda
chapters/examples/w_algebras_deep.tex:2632:trivial: ghosts are free fermions with
chapters/examples/w_algebras_deep.tex:3470:$G$ (conformal weight~$3/2$, fermionic). The $\lambda$-bracket structure
chapters/examples/w_algebras_deep.tex:3491:and $\chi$ is the gravitino source (spin~$-1/2$ fermionic):
chapters/examples/w_algebras_deep.tex:3513:$\beta\gamma$ system with spins $(2,-1)$ for the bosonic sector and a
chapters/examples/w_algebras_deep.tex:3514:$\beta\gamma$ system with spins $(3/2,-1/2)$ for the fermionic sector.
chapters/examples/w_algebras_deep.tex:3517:c_{\beta\gamma}^{(2,-1)} + c_{\beta\gamma}^{(3/2,-1/2)}
chapters/examples/w_algebras_deep.tex:3530:the $G$-type generators (fermionic, from the superpartner). The
chapters/examples/w_algebras_deep.tex:3532:fermionic sector:
chapters/examples/w_algebras_deep.tex:3537:= \tfrac{c}{2} + \tfrac{c-2}{4}$, where the fermionic term
chapters/examples/w_algebras_deep.tex:3766:\item \emph{Gaussian} (Heisenberg, lattice VOA, free fermion):
chapters/examples/w_algebras_deep.tex:3772:\item \emph{Contact/quartic} ($\beta\gamma$ system):
chapters/examples/w_algebras_deep.tex:5149:of fermionic supercurrents $G^\pm$ of conformal weight~$3/2$. Its

thinking
**Inspecting proofs and citations**

I think the exact fix is to replace the proof with a citation to `thm:bar-cobar-isomorphism-main`, which shows the inversion. Then, I should restate the local corollary as a specialization. I need to inspect the source theorem to make sure it really proves what I think it does. Let’s take a closer look at `thm:bar-cobar-isomorphism-main` and maybe also check out `fundamental-twisting-morphisms` for further confirmation.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '380,460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,3688p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '494,540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1410,1458p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '250,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   380	\[
   381	\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
   382	\longrightarrow \operatorname{gr}\barB_X(\cA)
   383	\cong \barB(\operatorname{gr}\cA)
   384	\]
   385	is a quasi-isomorphism of classical conilpotent coalgebras. By the
   386	classical fundamental theorem of twisting morphisms
   387	\cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
   388	$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
   389	
   390	For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
   391	$K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
   392	equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
   393	$K_\tau^L$ by $F_\bullet$; its associated graded complex is the
   394	classical left twisted tensor product for $\operatorname{gr}\tau$,
   395	which is acyclic by~(a). Strong convergence then lifts this
   396	acyclicity to~$K_\tau^L$.
   397	\end{proof}
   398	
   399	\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
 succeeded in 53ms:
  3600	$G_\cA = H_\cA/(1 + H_\cA)$, or at the level of formal power
  3601	series,
  3602	\[
  3603	G_\cA(t) \;=\; H_\cA(t) - G_\cA(t)\,H_\cA(t).
  3604	\]
  3605	Extracting the coefficient of $t^q$ gives
  3606	$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
  3607	since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
  3608	follows by induction on~$q$.
  3609	\end{proof}
  3610	
  3611	\begin{remark}[The primitive defect as a Koszulness probe]
  3612	\label{rem:primitive-defect-probe}
  3613	\index{primitive defect series!Koszulness probe}
  3614	
  3615	For a quadratic chiral algebra $\cA$ with generators of
  3616	weights $d_1, \ldots, d_s$, the PBW basis ensures that all
  3617	quasi-primaries are generated by the declared strong generators,
  3618	so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
  3619	Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
 succeeded in 52ms:
   494	\[\dim \bar{B}^{(0),2}(\mathcal{A}) = N^3 \cdot 2\]
   495	
   496	This grows rapidly with $n$.
   497	\end{example}
   498	
   499	\subsubsection{The bar differential}
   500	
   501	\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
   502	\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%
   503	\label{def:bar-diff-detailed}\label{def:diff-total}%
   504	\index{bar complex!differential|textbf}
   505	The bar complex carries a bigrading
   506	$\barB_{p,q}(\cA)$ by \emph{bar degree}~$p$ (number of
   507	desuspended tensor factors minus one) and
   508	\emph{form degree}~$q$. The \emph{cohomological
   509	degree} of a homogeneous element
   510	$s^{-1}\phi_0 \otimes \cdots \otimes s^{-1}\phi_p
   511	\otimes \omega \in \barB_{p,q}$ is
   512	\begin{equation}\label{eq:bar-cohomological-degree}
   513	n \;=\; \sum_{i=0}^{p}\bigl(|\phi_i| - 1\bigr) + q
 succeeded in 53ms:
  1410	
  1411	\begin{proof}
  1412	By Verdier duality for constructible sheaves on $\overline{C}_n(X)$ (see~\cite{KS90}):
  1413	\[\mathbb{D}(\mathcal{F}) = \mathcal{RHom}(\mathcal{F}, \omega_{\overline{C}_n(X)}[d])\]
  1414	Applied to the sheaf $j_!\mathbb{C}_{C_n(X)}$ where $j: C_n(X) \hookrightarrow \overline{C}_n(X)$ is the open inclusion, this exchanges $j_!$ and $Rj_*$ (Theorem~\ref{thm:verdier-config}), identifying logarithmic forms on the compactification with distributional forms on the open configuration space. The perfect pairing $\langle \eta_{ij}, \delta(z_i - z_j) \rangle = 1$ realizes the NAP isomorphism at the level of differential forms, since residues (bar operations) and delta functions (cobar operations) are Verdier duals.
  1415	\end{proof}
  1416	
  1417	\subsubsection{Distributions vs. differential forms: the dual picture}
  1418	
  1419	While the bar complex uses differential forms on compactified configuration spaces, the cobar complex uses distributions on open configuration spaces. This duality is the distributional manifestation of the intrinsic Verdier-dual definition (Definition~\ref{def:geom-cobar-intrinsic}); see Theorem~\ref{thm:cobar-distributional-model} for the precise identification.
  1420	
  1421	\begin{definition}[Geometric cobar complex]\label{def:geom-cobar-precise}
  1422	For a conilpotent chiral coalgebra $\mathcal{C}$ (valued in holonomic $\mathcal{D}$-modules), the distributional model of the geometric cobar complex is:
  1423	\[\Omega^{\text{ch}}_{p,q}(\mathcal{C}) = \text{Hom}_{\mathcal{D}}\left(\mathcal{C}^{\otimes(p+1)}, \mathcal{D}_{C_{p+1}(X)} \otimes \Omega^q_{\text{dist}}\right)\]
  1424	where $C_{p+1}(X)$ is the open configuration space, $\Omega^q_{\text{dist}}$ are distributional $q$-forms with singularities along diagonals, and the differential inserts delta functions rather than extracting residues.
  1425	\end{definition}
  1426	
  1427	\begin{example}[Delta function vs.\ residue]
  1428	\emph{Bar operation.} Extract residue when points collide
  1429	\[m_2^{\text{bar}}(a \otimes b) = \text{Res}_{z_1=z_2}\left[\frac{a(z_1)b(z_2)}{z_1-z_2}dz_1\right]\]
 succeeded in 52ms:
   250	\begin{enumerate}[label=(\roman*)]
   251	\item $m_0^{(g)} \neq 0$ if and only if $\kappa(\mathcal{A}) \neq 0$, equivalently if and only if $d_{\mathrm{fib}}^2 \neq 0$. This is the precise sense in which gravity is turned on. The scalar curvature term $m_0^{(g)}$ is the cosmological-constant term of the genus-$g$ curved $A_\infty$ model. This statement is fiberwise. For the standard families $m_0^{(g)}$ is central, so the internal commutator formula $m_1^2 = [m_0,-]$ may vanish even when $d_{\mathrm{fib}}^2 \neq 0$.
   252	\item $\kappa(\mathcal{A})$ is the coefficient of the Hodge class in $d_{\mathrm{fib}}^2$, hence the strength of the genus-$g$ gravitational backreaction. In that dictionary, $\kappa(\mathcal{A})$ is the Newton coupling. It is family-specific: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$ for affine Kac--Moody, $\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro, and $\kappa(\mathcal{B}^k) = c/6$ for Bershadsky--Polyakov.
   253	\item The critical gravitational coupling is the fixed point of the duality involution on the scalar lane. When the scalar complementarity constant is written as $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = K_\kappa(\mathcal{A})$, the fixed point is $\kappa_{\mathrm{crit}} = K_\kappa(\mathcal{A})/2$. This constant is family-specific. For affine Kac--Moody, Heisenberg, and free-field families one has $K_\kappa = 0$, so $\kappa_{\mathrm{crit}} = 0$. For Virasoro one has $K_\kappa = 13$, so $\kappa_{\mathrm{crit}} = 13/2$, equivalently $c = 13$. For the Bershadsky--Polyakov family the manuscript uses $\kappa(\mathcal{B}^k) = c/6$ together with the central-charge conductor $c(\mathcal{B}^k) + c((\mathcal{B}^k)^!) = 196$; hence the self-dual central charge is $c = 98$, and the induced scalar critical coupling is $\kappa_{\mathrm{crit}} = 49/3$.
   254	\end{enumerate}
   255	\end{remark}
   256	
   257	\begin{theorem}[Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle; \ClaimStatusProvedHere]
   258	\label{thm:curvature-central}
   259	For a curved $A_\infty$ algebra $(A, \mu_0, \mu_1, \mu_2, \ldots)$, the curvature element satisfies:
   260	\begin{enumerate}
   261	\item $\mu_1(\mu_0) = 0$ \quad (the curvature is a $\mu_1$-cycle);
   262	\item $\mu_1^2 = [\mu_0, -]_{\mu_2}$, where $[\mu_0, a]_{\mu_2} := \mu_2(\mu_0, a) - \mu_2(a, \mu_0)$ is the inner derivation.
   263	\end{enumerate}
   264	In particular, $\mu_1$ fails to be a differential precisely when $\mu_0$ is \emph{not} central with respect to $\mu_2$. For chiral algebras (which are graded-commutative), $[\mu_0, -]_{\mu_2} = 0$ automatically, so the curvature enters through higher operations ($\mu_3, \mu_4, \ldots$) or via the completed tensor product.
   265	\end{theorem}
   266	
   267	\begin{proof}
   268	The curved $A_\infty$ relations $\sum_{r+s+t=n}(-1)^{rs+t}\mu_{r+1+t}(\mathrm{id}^{\otimes r}\otimes \mu_s \otimes \mathrm{id}^{\otimes t})=0$ give, at each level:
   269	\begin{itemize}

thinking
**Inspecting bar_modular_operad**

I need to take a closer look at `bar_modular_operad` because it seems like the property `cobar-modular-shadow` could be misusing it. It's funny how sometimes a simple assumption can lead me down a rabbit hole of confusion. I’ll have to evaluate how these components interact to ensure everything is working as intended! Let’s dive into that and clarify what’s going on. It's all about getting the details right, right?
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6188,6228p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6188	confirmation.
  6189	\end{remark}
  6190	
  6191	The proof of Theorem~\ref{thm:genus-induction-strict} relies at every step on
  6192	the modular operad axioms for $\{\overline{\mathcal{M}}_{g,n}\}$. The next
  6193	statement crystallizes this dependence into an explicit algebraic statement: the bar
  6194	complex \emph{is} an algebra over the Feynman transform of the commutative
  6195	modular operad.
  6196	
  6197	\begin{theorem}[Bar complex as algebra over the modular operad;
  6198	 \ClaimStatusProvedHere]\label{thm:bar-modular-operad}%
  6199	\index{bar complex!algebra over modular operad}%
  6200	\index{modular operad!bar complex as algebra over}%
  6201	\index{Feynman transform!commutative modular operad}%
  6202	For a chiral algebra $\cA$, the collection
  6203	$\{\barB^{(g,n)}(\cA)\}_{2g-2+n>0}$ is an algebra over the Feynman transform
  6204	$\mathsf{F}\mathrm{Com}$ of the commutative modular operad in the sense of
  6205	Getzler--Kapranov~\textup{\cite{GetzlerKapranov98}}. Concretely:
  6206	\begin{enumerate}[label=\textup{(\roman*)}]
  6207	\item For each stable graph $\Gamma$ of type $(g,n)$, there is a composition

thinking
**Evaluating quantum theories**

I’ve been thinking about using a modular shadow carrier and whether I need to inspect the theorem of quantum complementarity for future theorems. There’s a chance the later section might not make sense, but I still might need to find a precise source if it misapplies the theorem. It looks like I should focus on checking the main statements related to the quantum complementarity theorem.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '452,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '520,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3328,3360p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   452	\end{remark}
   453	
   454	The Heisenberg complementarity
   455	of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
   456	polarization:
   457	
   458	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   459	\label{thm:quantum-complementarity-main}
   460	\label{thm:quantum-complementarity}
   461	\index{deformation-obstruction complementarity|textbf}
   462	\index{Lagrangian!complementarity|textbf}
   463	\textup{[}Regime: curved-central
   464	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   465	
   466	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
   467	curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
   468	the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
   469	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
   470	Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
   471	for the ambient complex and homotopy eigenspaces of
 succeeded in 51ms:
  3328	where $\tau$ is the modulus of the torus and $d_{\text{elliptic}}$ involves elliptic functions.
  3329	\end{definition}
  3330	
  3331	\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
  3332	\textup{[Regime: curved-central
  3333	\textup{(}i.e., curvature $\kappa$ is a central scalar;
  3334	the theorem proves that $\Dg{g}$ is \emph{flat}\/\textup{)};
  3335	all genera
  3336	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  3337	
  3338	The total corrected differential $\Dg{g}$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))} satisfies $\Dg{g}^{\,2} = 0$.
  3339	\end{theorem}
  3340	
  3341	\begin{proof}
  3342	\emph{Step 1: Expansion of $\Dg{g}^{\,2}$.}
  3343	
  3344	\begin{align*}
  3345	\Dg{g}^{\,2} &= \left(\dzero + \sum_k t_k d_k\right)^2 \\
  3346	&= \dzero^2 + \sum_k t_k (\dzero d_k + d_k \dzero) + \sum_{k,l} t_k t_l d_k d_l
  3347	\end{align*}
 succeeded in 52ms:
   520	Q_g(\cA) \cong Q_g(\cA^!)^\vee.
   521	\end{equation}
   522	At genus $0$, the unique point class is $\sigma$-fixed, so
   523	\[
   524	Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
   525	\qquad
   526	Q_0(\cA^!)=0.
   527	\]
   528	\end{theorem}
   529	
   530	\begin{remark}\label{rem:lagrangian-decomp}
   531	What one algebra sees as deformation, its dual sees as obstruction.
   532	\end{remark}
   533	
   534	\begin{proof}
   535	The proof occupies the remainder of this chapter,
   536	organized as three steps:
   537	Step~I (\S\ref{lem:genus-filtration}ff.) constructs the spectral
   538	sequence from the genus filtration;
   539	Step~II (from Theorem~\ref{thm:verdier-duality-config-complete})




thinking
**Identifying findings in proofs**

I think it's not necessary to explore every detail. Many later proofs reference a main theorem and local lemmas, and likely many may fail. I might want to check the line after 3338. Instead, I could search for self-referential proofs connected to the same theorem. There are potential critical findings, like the theorem between lines 664-675 that needs a fix for rigor. I also need to classify any issues by their impact for clarity.
thinking
**Evaluating critical findings in proofs**

I’ve identified a few critical issues. The proof for lemma `lem:verdier-extension-exchange` shows circular reasoning, as it invokes an identity that it’s meant to prove. I think I should either derive a new argument or cite external sources for clarification. 

Another critical finding in theorem `thm:cobar-diff-geom` includes undefined terms and unproven assertions, making it not a valid proof. I could suggest either rewriting it or providing a microlocal theorem with the necessary conditions.

Finally, the proposition concerning `prop:cobar-modular-shadow` presents what seems to be a significant claim that needs to be addressed.
thinking
**Clarifying proof connections**

I'm noticing that in lines 1803-1804, the proof identifies the graph sum with the Theta projection based on `cor:shadow-extraction`. However, the theorem `thm:bar-modular-operad` only states that the bar complex is an algebra over FCom, referencing lines 6197-6223, but it doesn't mention the cobar. I need to consider how this difference impacts the proof's integrity and whether I should address this discrepancy further for clarity.
thinking
**Evaluating theorem context**

I'm wondering if using AGENTS as context is appropriate. It might be smarter to consider local contradictions alongside the cross-source bar_cobar_adjunction_curved theorem. I think I need to inspect the `d_fib^2` formula in the source to clarify this further. So, I should probably do a search to gather more information and see how everything connects!
exec
/bin/zsh -lc "rg -n 'd_\\{?fib|d\\\\mathrm\\{fib\\}|m_0\\"'^'"\\{\\(g\\)\\}|curvature of the affine bar complex|k\\+h\\"'^'"\\\\vee|d_\\{\\\\barB\\}\\"'^2'"' chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:1867:\item Curvature element $m_0^{(g)} = \kappa(\cA) \cdot \omega_g$,
chapters/theory/higher_genus_foundations.tex:1871: $m_1^{(g)} \circ m_1^{(g)} = [m_0^{(g)}, -]$, i.e.,
chapters/theory/higher_genus_foundations.tex:4926:&= \dim(\mathfrak{g}) \cdot \frac{k+h^\vee}{2h^\vee} \cdot \lambda_g \\
chapters/theory/higher_genus_foundations.tex:4927:&= \frac{(k+h^\vee)\dim(\mathfrak{g})}{2h^\vee} \cdot \lambda_g
chapters/theory/higher_genus_foundations.tex:4945:= \frac{-(k+h^\vee)\dim(\mathfrak{g})}{2h^\vee} \cdot \lambda_g
chapters/theory/higher_genus_foundations.tex:5322:$\kappa(\widehat{\mathfrak{g}}_k) = \frac{(k+h^\vee)\dim\mathfrak{g}}{2h^\vee}$,\;
chapters/theory/higher_genus_foundations.tex:5423:Part~(ii): for Kac--Moody, $\kappa = (k+h^\vee)\dim\fg/(2h^\vee)$;
chapters/theory/higher_genus_foundations.tex:5848:For Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ (before DS reduction), $\kappa/c = (k+h^\vee)^2/(2h^\vee k)$, which depends on the level. The level-independence of $\kappa/c$ is specific to $\mathcal{W}$-algebras and reflects the DS reduction.
chapters/theory/higher_genus_foundations.tex:5862:For KM: $\kappa = (k+h^\vee)d/(2h^\vee)$, which is linear in $k$ with slope $d/(2h^\vee)$. Level shift $k \to k+n$ adds $nd/(2h^\vee)$.
chapters/theory/higher_genus_foundations.tex:6325:coefficient $\kappa = (k+h^\vee)d/(2h^\vee)$ is proportional to the
chapters/theory/higher_genus_complementarity.tex:2416:$\mathrm{obs}_g = \frac{(k+h^\vee)\dim(\mathfrak{g})}{2h^\vee}\,
chapters/theory/higher_genus_complementarity.tex:5809: \dfrac{(k+h^\vee)\dim\fg}{2h^\vee}
chapters/theory/higher_genus_complementarity.tex:5856:For~$V_k(\fg)$: $\kappa = (k+h^\vee)\dim\fg/(2h^\vee)$ and
chapters/theory/higher_genus_complementarity.tex:5959:$d_{\barB}^2 = \kappa(\mathrm{Vir}_c) \cdot \omega_g$ with
chapters/theory/higher_genus_complementarity.tex:5983:The curvature identity $d_{\barB}^2 = \kappa \cdot \omega_g$
chapters/theory/bar_cobar_adjunction_curved.tex:65:$d_{\barB}^2 = 0$ is preserved, but the internal differential
chapters/theory/bar_cobar_adjunction_curved.tex:236:% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
chapters/theory/bar_cobar_adjunction_curved.tex:241: m_0^{(g)} = \kappa(\mathcal{A}) \cdot \omega_g \cdot \mathbf{1},
chapters/theory/bar_cobar_adjunction_curved.tex:251:\item $m_0^{(g)} \neq 0$ if and only if $\kappa(\mathcal{A}) \neq 0$, equivalently if and only if $d_{\mathrm{fib}}^2 \neq 0$. This is the precise sense in which gravity is turned on. The scalar curvature term $m_0^{(g)}$ is the cosmological-constant term of the genus-$g$ curved $A_\infty$ model. This statement is fiberwise. For the standard families $m_0^{(g)}$ is central, so the internal commutator formula $m_1^2 = [m_0,-]$ may vanish even when $d_{\mathrm{fib}}^2 \neq 0$.
chapters/theory/bar_cobar_adjunction_curved.tex:252:\item $\kappa(\mathcal{A})$ is the coefficient of the Hodge class in $d_{\mathrm{fib}}^2$, hence the strength of the genus-$g$ gravitational backreaction. In that dictionary, $\kappa(\mathcal{A})$ is the Newton coupling. It is family-specific: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$ for affine Kac--Moody, $\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro, and $\kappa(\mathcal{B}^k) = c/6$ for Bershadsky--Polyakov.


thinking
**Evaluating cohomology statement**

I'm considering the statement about CG17 agreeing with cobar cohomology. However, I realize that it lacks a specific theorem or hypotheses, which leaves it unproven. It might be better to either downgrade it to a remark or to cite a precise theorem if one is available. That way, I can ensure the information is presented more accurately and reliably!
thinking
**Searching for missing labels**

I’m pondering whether my approach counts if I don't ask about every unjustified step. I think it could be helpful to focus on the surfaces that have been proven here. I noticed that there's a missing label referenced in the text at line 50, specifically `chap:bar-cobar-adjunction`. However, I realized that my previous check included this label but didn't search across the main document. Maybe I need to conduct a broader search to find it.
exec
/bin/zsh -lc "rg -n '\\\\label\\{chap:bar-cobar-adjunction\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./chapters/theory/bar_cobar_adjunction_curved.tex:2:\label{chap:bar-cobar-adjunction}








thinking
**Evaluating mathematical findings**

I need to check line 1849 about the fundamental cobar element formula and the antisymmetric determinant. I wonder if this could be nonsensical. The kernel expression is linked to reconstructing chiral multiplication, but I think it's unsupported. Maybe mention the severity is low? I need to see if the source on `thm:weak-topology` is worth inspecting. I should indicate specific file and line references. I can probably cite a start line since the user prefers `file:line` format. I'll also verify for any false positives against the file’s contents.
thinking
**Inspecting statement lines**

I need to look closely at specific lines to identify the statements that might need adjustments. It seems like I should focus on providing more precise fixes. Maybe I can gather a few examples to clarify what needs to be changed. I want to ensure that I’m thorough in my inspection, so I can pinpoint exactly where the issues lie. Overall, I'll concentrate on being clear and accurate for a better understanding.
thinking
**Checking mathematical conventions**

I need to check if the convention indeed states that H^0(B) equals A^i. It might not be essential if the main theorem already exists, but it could still be beneficial to confirm this. I’m curious about the relationship between these two mathematical concepts, and I want to ensure I have the right understanding. Let's explore this further to see if everything aligns properly!
thinking
**Adjusting citations for clarity**

I'm thinking about the best way to fix this: I could either replace the citation that’s causing confusion with a theorem that actually proves filtration convergence—like those strong filtration or degree cutoff results. Alternatively, I could just remove the convergence claim altogether. It seems like that would simplify things and make the message clearer. I feel like either option could make the information more precise. Let's go for it!
thinking
**Clarifying findings on definitions**

The user is asking about each missing definition, unresolved reference, or unjustified step being a finding. It seems like we might say there were none found for unresolved external references, except maybe that no labels were missing. However, there could be some missing definitions that we need to check. This could be especially true if any definitions use undefined terms, so I’ll want to consider that carefully.
thinking
**Identifying issues in theorems**

I'm looking into some undefined terms like `K_prop` and `ω_n` related to the `thm:geom-unit` formula, which needs a clearer definition. There’s also a concern with the `def:cobar-kernel` line that lacks a measure. It might help to reference exact line numbers for clarity while listing findings by severity—around 14 in total. I need to check mismatches, especially with `prop:cobar-modular-shadow` and `geom-unit`, to ensure accuracy. Lastly, there's potential complexity with the involution on the center local system.
thinking
**Reviewing theorem findings**

I'm considering inspecting `def:complementarity-complexes` for the `Q_g` decomposition, but I realize that it's only necessary for cases where \( g \geq 1 \). This ties in with the lemma on observations in pairing missing genus restrictions. I also need to check if `thm:deformation-obstruction` has been proved elsewhere, as local lemmas are still unsupported. Since the user wants every finding, I should aim for thoroughness—possibly around 18 findings total. I should specifically check lines like `thm:cobar-cech`, noting some false claims and issues related to weak topology definitions.
thinking
**Clarifying definitions**

I'm examining line 1976, which uses `C_c^\infty(C_n(X), (\C^{\boxtimes n})^*)` that isn't properly defined. This lack of definition is something I definitely need to address. I should think about how to clarify this to make sure it aligns with other components in the work. It's crucial to ensure definitions are consistent to support the overall framework of the theories being proposed. Let's focus on getting that fixed so it can stand as a clear reference point.
exec
/bin/zsh -lc "rg -n 'Tw\\(|MC\\(\\\\operatorname\\{Conv\\}|representability theorem|Tw\\"'^'"\\{ch\\}|Tw\\(' chapters/theory -g '*.tex' | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/poincare_duality_quantum.tex:1222: representability theorem for deformations)
chapters/theory/bar_cobar_adjunction_curved.tex:6:$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
chapters/theory/cobar_construction.tex:43:This is the geometric content of the representability theorem
chapters/theory/cobar_construction.tex:44:$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$

thinking
**Searching for theorems**

I’m thinking about whether I should search for the exact label of the theorem. Maybe I won't find the right one if I only look for a specific name. Instead, I might search for the broader term "twisting representability." This might give me a wider range of results and help me discover related concepts or different ways to approach the topic. It's worth considering! Let's see what I can find.
exec
/bin/zsh -lc "rg -n 'representability|Tw\\(|MC\\(' chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
6:$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
13:$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
1010: equivalence by twisting representability
1012: \ref{thm:completed-twisting-representability})}.
1929:\begin{theorem}[Completed twisting representability; \ClaimStatusProvedHere]
1930:\label{thm:completed-twisting-representability}
1946:quotient, ordinary bar/cobar representability holds by the finite-stage
exec
/bin/zsh -lc "rg -n '\\\\label\\{ch:holographic-datum-master\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./chapters/connections/holographic_datum_master.tex:2:\label{ch:holographic-datum-master}




thinking
**Evaluating theorem dependencies**

I'm considering a potential cycle between theorem 385 and theorem 1312. It seems theorem 385 might rely on theorem 1312, which in turn could reference 385? Looking at line 1419, theorem bar-cobar-verdier appears to use a pairing without citing theorem 385, and yet step 1380 identifies the cobar side with constructions from previous steps. The dependency might not be circular, but the proof order raises questions. I need to clarify those references to ensure logical consistency.
thinking
**Considering theorem reliance**

I'm wondering what happens if the proof of theorem 1312 actually relies on theorem 385 or its corollary. That could create issues with the proofs being interdependent. If 1312 needs 385 for its foundation, and 385 is using 1312 in some way, then I’d have to really analyze the proof structures. This could complicate the entire approach if they're linked. I need to clarify their arguments and dependencies to ensure coherence in the reasoning.
thinking
**Evaluating mathematical concepts**

I'm considering the expression ∈ D'(C_n×C_m) since it seems to deal with product open spaces. I need to confirm the definition of C_n(X) and keep in mind the diagonal exclusion. A strong aspect is the theorem about extending distributions across collision divisors, but the codomain needs fixing due to the support issue on diagonals. I'll also mention a broader finding on distributions related to open configuration space. This is crucial as foundational objects may be misdefined. An exact fix is to redefine the distributional model.
thinking
**Identifying critical issues in findings**

I'm evaluating some significant findings that might replace earlier ones. Here’s what I’ve noted: 

A. Delta distributions on open configuration spaces need correction regarding compactification instead of just D'(C_n(X)). B. The lemma regarding Verdier seems circular. C. There’s a heuristic issue with the d^2 theorem. D. The Cech theorem's claim about contractibility appears false. 

I also need to verify the label mismatch on the `thm:bar-cobar-adjunction`. Good catch on searching for local labels to confirm. An exact fix could involve changing that reference correctly.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1920,1956p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1920	$(m,q)$-window provides a compatible inverse system of multilinear
  1921	operations on all finite quotients. Passing to the inverse limit
  1922	defines continuous $\Ainf$-operations on~$\cA$. The $\Ainf$ identities
  1923	are polynomial on each quotient and pass to the limit entrywise.
  1924	Continuity of the completed bar differential follows because on each
  1925	weight quotient only finitely many degrees survive and all matrices are
  1926	stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
  1927	\end{proof}
  1928	
  1929	\begin{theorem}[Completed twisting representability; \ClaimStatusProvedHere]
  1930	\label{thm:completed-twisting-representability}
  1931	\index{twisting morphism!completed|textbf}
  1932	For $\cA \in \CompCl(\Fft)$ and $C \in \Cstr$, define $\Twcts(C,\cA)$
  1933	to be the set of degree-$(-1)$ continuous twisting morphisms from~$C$
  1934	to~$\cA$. Then
  1935	\[
  1936	\operatorname{Hom}_{\mathrm{alg}}(\widehat\Omega^{\mathrm{ch}}C,\,\cA)
  1937	\;\cong\; \Twcts(C,\cA)
  1938	\;\cong\; \operatorname{Hom}_{\mathrm{coalg}}(C,\,
  1939	\widehat{\bar B}^{\mathrm{ch}}\cA).
exec
/bin/zsh -lc "rg -n 'MC\\(\\\\operatorname\\{Conv\\}|Tw\\(\\cC, \\cA\\)|Twcts|twisting representability' chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:MC\(\\operatorname\{Conv\}|Tw\(\cC, \cA\)|Twcts|twisting representability)
                                      ^^
error: unrecognized escape sequence




thinking
**Revising mathematical proof**

I'm thinking about the theorem labeled ProvedHere. However, it seems the proof has some undefined regularization counterterms and lacks wavefront analysis. To address this, my plan is to demote the explicit formulas to remarks and define `d_cobar := \mathbb D(d_bar)` more abstractly instead. This also gives me the option to keep them separate if necessary. It’s a bit tricky, but I believe this approach will clarify things!
thinking
**Refining findings count**

I’m considering consolidating my findings to keep the count at 18. I think maybe I should have "Checked: N | Findings: N," with N potentially being 30. If I aim for 18 findings, maybe that could break down into 10 critical, 6 high, and 2 medium. I need to pinpoint exact fixes for each one based on specific line numbers, like theorem kernel at line 180, verdier extension at line 353, and cobar distributional model at line 386.
thinking
**Examining theorem findings**

I'm weighing the best options for findings, considering line 386 because the theorem statement is affected. There are several candidates, such as lines 544, 665, and others, all the way to line 3389. I'm wondering if I should settle on about 21 findings. It might feel like too many, but maybe 25 lines would work if I condense each bullet point. I could consider excluding lines like 2028 if it's not a critical duplicate. The user wanted an exhaustive list, though, so maybe I'll include it along with some others.
thinking
**Determining findings details**

I'm estimating that I can fit about 50 lines, with each bullet being a single line, though some are long. That seems manageable. I’m considering including the 45 label mismatch and 503 duplicate definition as medium priority. For each fix, I want to be precise. For line 180, I’d replace the formula with the kernel pairing using the test function. With line 353, instead of the proof, I might use the Yoneda derivation or note it as "Proved Elsewhere" and cite appropriate references.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:betagamma-bc-koszul\\}|\\\\label\\{thm:betagamma-fermion-koszul\\}' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
449:\label{thm:betagamma-fermion-koszul}
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '440,470p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   440	residue calculus of the bar differential (Definition~\ref{def:bar-differential-complete}).
   441	\end{proof}
   442	
   443	\section{Koszul dual}
   444	\label{sec:betagamma-koszul-dual}
   445	
   446	\subsection{Main result: Koszul duality with free fermions}
   447	
   448	\begin{theorem}[Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma}; \ClaimStatusProvedHere]
   449	\label{thm:betagamma-fermion-koszul}
   450	\index{Koszul duality!beta-gamma vs.\ free fermion@$\beta\gamma$ vs.\ free fermion|textbf}
   451	The Koszul dual of the $\beta\gamma$ system is the $bc$ ghost system:
   452	\[(\beta\gamma)^! \cong bc \quad \text{and} \quad (bc)^! \cong \beta\gamma\]
   453	
   454	This is a \emph{two-generator} duality ($\dim V = 2$: one bosonic pair
   455	$\beta, \gamma$ dualizes to one fermionic pair $b, c$), not to be confused with
   456	the single-generator duality $\Lambda^{\mathrm{ch}}(\psi) \leftrightarrow
   457	\mathrm{Sym}^{\mathrm{ch}}(\gamma)$. The $bc$ system has:
   458	\begin{enumerate}
   459	\item \emph{Generators.} $b$ with conformal weight $h_b = \lambda$ and $c$ with conformal weight $h_c = 1 - \lambda$

thinking
**Improving citation clarity**

The user wants to improve the citation from file:line at line 1387. I think it might be better to start citing from theorem 1312 instead. This could provide clearer context for the reference and make it easier for readers to understand. I need to make sure that the changes help enhance the overall clarity of the document. Let’s work on refining that citation now!
codex
- [CRITICAL] chapters/theory/cobar_construction.tex:353 — PROBLEM: `lem:verdier-extension-exchange` is proved by invoking the same identity at line 379 (`\mathbb D_Y\circ j_*\circ \mathbb D_U \cong j_!`), so the proof is circular. FIX: replace lines 363-382 with a derived-Hom/Yoneda proof, or change the lemma to `\ClaimStatusProvedElsewhere` and cite the standard HTT/KS theorem instead of giving a local proof.

- [CRITICAL] chapters/theory/cobar_construction.tex:452 — PROBLEM: the chapter identifies the Verdier-dual residue with `\delta(z_i-z_j)` on `C_n(X)`, but the diagonal is excluded from the open configuration space; the same error drives Example `ex:simplest-cobar` and `d_{\text{extend}}`. FIX: redefine the distributional model on the compactification via `j_!`/boundary currents, and replace every diagonal delta distribution on `C_n(X)` by a boundary current on `\overline C_n(X)`.

- [CRITICAL] chapters/theory/cobar_construction.tex:544 — PROBLEM: `thm:cobar-diff-geom` mixes incompatible bidegrees and decompositions: the statement sends `\Omega_{p,q}` to `\Omega_{p-1,q+1}\oplus\Omega_{p,q}\oplus\Omega_{p+1,q}`, but the three components below preserve `q`; the proof also uses undefined “regularization counterterms.” FIX: choose one decomposition and make the codomain match it; best repair is to define `d_{\mathrm{cobar}}:=\mathbb D(d_{\mathrm{bar}})` abstractly and move the coordinate formulas to a heuristic remark.

- [CRITICAL] chapters/theory/cobar_construction.tex:665 — PROBLEM: `thm:cobar-d-squared-zero` is marked `\ClaimStatusProvedHere`, but its own statement says the rigorous proof is elsewhere and its Term 3 uses formally undefined products like `\delta(z)^2`. FIX: change the environment to `remark` or `verification` with heuristic status, and redirect all rigorous citations to `cor:cobar-nilpotence-verdier`.

- [CRITICAL] chapters/theory/cobar_construction.tex:1387 — PROBLEM: the proof of `thm:bar-cobar-verdier` uses the non-type-correct computation `\int \eta_{ij}\wedge\delta(z_i-z_j)=1`; a logarithmic 1-form is being paired with a scalar regularization without a defined current-valued pairing. FIX: delete Step 3’s Gaussian calculation and replace it with the canonical Verdier evaluation map `\mathbb D\mathcal M\otimes \mathcal M\to\omega`; if an analytic lemma is wanted, prove it separately with precise test-form conventions.

- [CRITICAL] chapters/theory/cobar_construction.tex:1798 — PROBLEM: `prop:cobar-modular-shadow` claims an `\mathrm{FCom}`-algebra structure on `\Omega(\bar B(\cA))`, but the cited source theorem `thm:bar-modular-operad` only gives that structure on the bar complex itself. FIX: restate the proposition for `\bar B(\cA)`, or insert a new theorem proving transport of the modular-operad structure through cobar before using it.

- [CRITICAL] chapters/theory/cobar_construction.tex:1829 — PROBLEM: `thm:cobar-cech` asserts the induced cover is Leray because intersections are contractible “being intersections of coordinate discs in `C_n(X)`”; this is false already for `U\times U\setminus\Delta`. The proof also jumps to `H^p(X^n,\mathcal F_{\mathcal C})`, which is the wrong space. FIX: delete the theorem unless you provide an actual acyclic hypercover of `\overline C_n(X)`; if you keep it, replace `X^n` by the correct configuration space and cite a genuine descent theorem for that cover.

- [CRITICAL] chapters/theory/cobar_construction.tex:1879 — PROBLEM: `thm:bar-cobar-adjunction` is used earlier as a twisting-representability theorem, but the local theorem is only a “geometric unit”; its displayed integral formula is not type-checked, and line 1904 cites `thm:completion-necessity`, which does not prove spectral-sequence convergence. FIX: keep this as `thm:geom-unit` only, change the earlier reference to the actual twisting-representability theorem, and move the integral formula to a remark unless a chain map and convergence proof are supplied.

- [CRITICAL] chapters/theory/cobar_construction.tex:2388 — PROBLEM: `thm:central-charge-cocycle` is ill-typed: `c_1` is defined at lines 2384-2385 in a tensor product of chain groups, but the theorem treats it as a class in `H_1^{(1)}(\mathcal A)`. The proof then inserts a “normalized trace” by fiat. FIX: define a single chain complex and place `c_1` in one explicit degree, or downgrade the theorem to a heuristic example and cite a rigorous genus-1 obstruction theorem instead.

- [CRITICAL] chapters/theory/cobar_construction.tex:2484 — PROBLEM: `thm:genus1-cobar-bar` claims `H^0(\Omega C_\bullet^{(1)}(\mathcal A))\cong\widehat{\mathcal A}` for any vertex algebra with modular characteristic, but the proof never defines the coalgebra structure on `C_\bullet^{(1)}(\mathcal A)` or proves the universal-central-extension claim; line 2522 (“any 2-cocycle factors through the trace pairing”) is an unsupported global assertion. FIX: either restrict the statement to a specific family with a cited computation, or downgrade it to a conjecture/roadmap.

- [CRITICAL] chapters/theory/cobar_construction.tex:2747 — PROBLEM: `thm:essential-image-bar` proves necessity, then switches to slogans for sufficiency (“reading each axiom as a construction step”); no reconstruction theorem is supplied. FIX: keep only the necessity direction as a proved proposition, or downgrade the iff statement to a conjecture until a real reconstruction functor is built.

- [CRITICAL] chapters/theory/cobar_construction.tex:2800 — PROBLEM: `cor:recognition-principle` states an `iff`, but the proof only uses the bar-cobar adjunction on the Koszul locus and never proves the converse. FIX: replace “if and only if” by the one implication actually shown, or mark the converse as conjectural.

- [HIGH] chapters/theory/cobar_construction.tex:187 — PROBLEM: `thm:schwartz-kernel-cobar` gives a pointwise formula for `(K\phi)(z_1,\dots,z_m)` even though the codomain is `\mathcal D'(C_m(X))`, not functions. FIX: replace the displayed formula by the standard kernel identity `\langle K\phi,\psi\rangle=\langle K,\psi\boxtimes\phi\rangle`.

- [HIGH] chapters/theory/cobar_construction.tex:1095 — PROBLEM: `thm:fermion-boson-koszul` is tagged `ProvedHere`, but the proof only cites classical finite-dimensional Koszul duality and “Part~\ref{part:characteristic-datum}`; it does not give a local chiral proof or an exact imported theorem. FIX: either mark it `ProvedElsewhere` and cite the explicit example theorem already in the repo (for example `chapters/examples/beta_gamma.tex` `thm:betagamma-fermion-koszul` if that is the intended statement), or restrict to the exact special case you can prove here.

- [HIGH] chapters/theory/cobar_construction.tex:2127 — PROBLEM: `thm:curved-mc-cobar` bundles a standard algebraic MC equation together with unproved geometric claims about anomalies and genus-1 central extensions. FIX: split it: keep the algebraic curved-MC statement as `ProvedElsewhere` with citation to Positselski/Loday–Vallette, and move the geometric bullets to a remark with explicit hypotheses.

- [HIGH] chapters/theory/cobar_construction.tex:2153 — PROBLEM: `prop:km-bar-curvature` conflates the total bar differential, the internal differential, and higher-genus fiberwise curvature; the final `\mathfrak{sl}_2` calculation does not follow from the preceding equalities. FIX: rewrite the proposition in the fiberwise genus-`g` language already used elsewhere (`m_0^{(g)}=\kappa(\widehat{\mathfrak g}_k)\omega_g`, `d_{\mathrm{fib}}^2=[m_0^{(g)},-]`), keep `d_{\bar B}^2=0` separate, and replace the ad hoc `\mathfrak{sl}_2` paragraph with a checked computation or a citation.

- [HIGH] chapters/theory/cobar_construction.tex:3262 — PROBLEM: `lem:obs-def-pairing` is stated for all genera but lands in `H^{3g-3}`, which is nonsense at `g=0`; the source complementarity theorem only gives the nondegenerate pairing for `g\ge1`. FIX: add the hypothesis `g\ge1` to the lemma, state the `g=0` case separately, and cite `thm:quantum-complementarity-main` for the degree shift.

- [HIGH] chapters/theory/cobar_construction.tex:3389 — PROBLEM: `cor:curved-differential` mixes cohomology classes and their integrals incoherently: `\omega_g` is said to live on `\mathcal M_g`, yet the formula inserts `\int_{\mathcal M_g}\omega_g` into the differential and then squares it to `\omega_g^2`. FIX: replace the display by the class-level identity `d_{\mathrm{fib}}^2=[\mu_0,-]\otimes\omega_g`; if the curvature is central, say that the commutator vanishes and the scalar class records the obstruction.

- [MEDIUM] chapters/theory/cobar_construction.tex:45 — PROBLEM: the chapter calls `thm:bar-cobar-adjunction` the theorem `\operatorname{Tw}(\cC,\cA)=\MC(\operatorname{Conv}(\cC,\cA))`, but the local label is attached to the geometric unit theorem, not to twisting representability. FIX: retarget this reference to the actual twisting-representability theorem, or rename the local theorem/label so the reference matches the statement.

- [MEDIUM] chapters/theory/cobar_construction.tex:503 — PROBLEM: the chapter defines “geometric cobar complex” twice: intrinsically at line 249 and again distributionally at line 503, but never states a clean equivalence before reusing the same notation. FIX: rename line 503 to “Distributional model of the geometric cobar complex” and prepend “By Theorem~\ref{thm:cobar-distributional-model}”.

## Summary
Checked: 30 | Findings: 20 | Verdict: FAIL
tokens used
194,158
