# U09_missing_examples (611s)

- [CRITICAL] chapters/connections/concordance.tex:1943 — PROBLEM: the canonical MC5 row says “analytic and coderived proved” and then treats `thm:bv-bar-coderived` as proved, but the source theorem is explicitly `\ClaimStatusConditional` in `chapters/connections/bv_brst.tex:1881-1917`. FIX: rewrite the row to split the package truthfully: “analytic proved; genus-0 algebraic BRST/bar proved; Heisenberg scalar BV=bar proved (`thm:heisenberg-bv-bar-all-genera`); coderived BV=bar conditional (`thm:bv-bar-coderived`); chain-level conjectural; tree-level conditional.”

- [CRITICAL] chapters/frame/guide_to_main_results.tex:99 — PROBLEM: the flagship guide repeats the same false MC5 status, says `$D^{\mathrm{co}}$-level BV=bar proved`, and mentions “Heisenberg sewing via Fredholm determinant” without citing `thm:heisenberg-sewing` at all. FIX: change clause (3) to “$D^{\mathrm{co}}$-level BV=bar conditional,” add the proved Heisenberg scalar theorem `thm:heisenberg-bv-bar-all-genera`, and expand the location cell to include `\ref{thm:heisenberg-sewing}` alongside `\ref{thm:general-hs-sewing}` and `\ref{thm:algebraic-string-dictionary}`.

- [CRITICAL] chapters/connections/editorial_constitution.tex:440 — PROBLEM: the MC5 master-conjecture note says “Resolved in $D^{\mathrm{co}}$” by `thm:bv-bar-coderived`, again contradicting the theorem’s own conditional tag. FIX: replace “Resolved in $D^{\mathrm{co}}$” with “Conditional in $D^{\mathrm{co}}$,” then add a separate proved sentence pointing to `thm:heisenberg-bv-bar-all-genera` and the genus-0 theorem `thm:algebraic-string-dictionary`.

- [HIGH] metadata/claims.jsonl:180 — PROBLEM: generated metadata records `thm:bv-bar-coderived` as `"status": "ProvedHere"`, and the dependency graph likewise paints it proved (`metadata/dependency_graph.dot:190`), so downstream audit tooling is being fed a false closed status. FIX: regenerate the generated metadata from the TeX source so `thm:bv-bar-coderived` is `Conditional`, and regenerate the dependency graph so the node is no longer marked `[Pr]` / green.

- [HIGH] chapters/frame/guide_to_main_results.tex:43 — PROBLEM: the Theorem C row says the theorem is “Upgraded to shifted-symplectic Lagrangian geometry,” but the concordance makes the Verdier-side Lagrangian splitting unconditional and the ambient shifted-symplectic upgrade conditional (`chapters/connections/concordance.tex:47-53`), with the upgrade separated out as `thm:shifted-symplectic-complementarity` (`chapters/theory/higher_genus_complementarity.tex:441,1899`). FIX: rewrite the row to say “Verdier-side Lagrangian splitting unconditional; ambient shifted-symplectic upgrade conditional on perfectness/nondegeneracy,” or cite `thm:shifted-symplectic-complementarity` separately as conditional.

- [HIGH] chapters/frame/guide_to_main_results.tex:56 — PROBLEM: the Theorem H row adds “explicit Koszul resolution of length bounded by the number of generators,” but the cited theorem `thm:hochschild-polynomial-growth` only states concentration in degrees `0,1,2`, polynomial Hilbert series, and Koszul functoriality (`chapters/theory/chiral_hochschild_koszul.tex:701-749`). I did not find the claimed “length bounded by the number of generators” theorem on the audited H surface. FIX: delete that clause and replace the row text with the actual theorem content from `thm:hochschild-polynomial-growth`.

- [MEDIUM] chapters/frame/guide_to_main_results.tex:75 — PROBLEM: the MC1 row claims PBW degeneration for “Kac--Moody, Virasoro, `\cW_N`, free fields, lattice” but points only to `prop:pbw-universality`, whose printed scope is the freely-strongly-generated criterion (`chapters/theory/chiral_koszul_pairs.tex:1365-1379`) and whose listed families are universal Kac--Moody, universal Virasoro, and universal principal `\mathcal W` (`chapters/theory/chiral_koszul_pairs.tex:1390-1404`). The cited locator does not itself establish the five-family sentence. FIX: make the row smaller and true: restrict it to the universal/freely-strongly-generated families actually covered by `prop:pbw-universality`, or replace the locator with the actual family-by-family MC1 package.

- [MEDIUM] chapters/examples/yangians_computations.tex:3873 — PROBLEM: the all-types MC3 theorem surface has no worked non-type-A example in prose. On the audited MC3 surface, the concrete worked computation is still type-A / `Y(\mathfrak{sl}_2)` (`chapters/examples/yangians_computations.tex:3254-3328`), so the failure-prone non-simply-laced cases are not exercised by a printed example even though the theorem claims all simple types. FIX: insert a worked `B_2` or `C_2` example immediately after `thm:categorical-cg-all-types`, computing one multiplicity-free `q`-character and the resulting prefundamental categorical Clebsch--Gordan decomposition.

All 10 audited main packages `A, B, C, D, H, MC1, MC2, MC3, MC4, MC5` do have at least one worked example somewhere in source; none is completely exampleless. The failures are status drift, unsupported summary prose, and one missing non-type-A MC3 example on the theorem surface.

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
session id: 019d840a-fa35-7b13-9211-5cf23a63a9b7
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


MISSION: UNFINISHED WORK AUDIT.

For each main theorem (A-D, H, MC1-5): is there at least ONE worked example? If a theorem has no example: flag it and suggest which family to use.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers

thinking
**Inspecting theorem statements**

I need to closely examine the actual theorem statements and the relevant examples or chapters around them. I’ll search for each theorem label and look for references to examples exhaustively. It’s crucial to maintain accuracy, noting line numbers without making any changes, just reporting findings. I might want to deploy explorer agents in parallel — one for theorem surfaces and another for finding examples or cross-references. However, I realize that multi_tool_use.parallel is limited to developer tools only.
codex
I’m auditing the theorem/example surface for A-D, H, and MC1-5, using `deep-beilinson-audit` and a code-review mindset. First I’m locating the canonical theorem labels, concordance entries, and any worked-example anchors so the findings stay tied to exact file lines rather than folklore.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg -n \"thm:[A-DH]\\b|thm:mc[1-5]\\b|MC1|MC2|MC3|MC4|MC5|Theorem A|Theorem B|Theorem C|Theorem D|Theorem H\" CLAUDE.md chapters metadata raeeznotes archive || true" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 51ms:
Total output lines: 3055

/Users/raeez/chiral-bar-cobar
rg: raeeznotes: No such file or directory (os error 2)
CLAUDE.md:19:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
CLAUDE.md:332:- B29. Theorem C^{E1} with `n` free on RHS but only `g` on LHS. CORRECT: fully quantify n with `2g-2+n > 0`. AP139.
CLAUDE.md:414:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:571:AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
CLAUDE.md:812:AP139: Unbound variable in theorem. If the LHS of a displayed equation depends on variables {g} but the RHS depends on {g,n}, the variable n is FREE. Every variable in a theorem statement MUST be either universally quantified ("for all n") or bound by the context ("at each degree n with 2g-2+n>0"). Unbound variables make the theorem ill-formed. Found in Theorem C^{E1} where the complementarity equation had n on the RHS but only g on the LHS.
CLAUDE.md:826:AP147: Circular proof routing. Theorem B and def:koszul-chiral-algebra appeared mutually circular until the routing was made explicit: twisted-tensor → cone identification → bar-cobar (commit 65262ee). When a proof chain involves multiple theorems that reference each other, insert a ROUTING REMARK citing the primitive non-circular anchor. If no such anchor exists, the proof is genuinely circular and must be restructured.
CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
CLAUDE.md:840:AP160: Three Hochschild theories -- geometry determines which. (i) Topological HH: E_1 input -> E_2 (Deligne). (ii) Chiral ChirHoch: E_inf-chiral input -> {0,1,2} (Theorem H). (iii) Categorical HH: dg category -> E_2 with CY shifted Poisson. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts. Conv:three-hochschild in concordance.tex is constitutional.
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
CLAUDE.md:919:**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).
chapters/examples/w_algebras_deep.tex:41:(ii)~the MC4 closure via $\mathcal{W}_N$ rigidity
chapters/examples/w_algebras_deep.tex:527:MC4 endpoint: the theorematic target is the filtered H-level target


thinking
**Identifying theorem examples**

I need to determine if there’s at least one worked example for each theorem in the manuscript. I might cross-reference this with the theorem discussions or later chapters. I'll conduct an exhaustive search for references, checking example chapters against theorem labels. Since the user is asking for specific main theorems, I’ll interpret “at least one worked example” to be anywhere in the manuscript, not just adjacent to the theorems. I’ll also identify when examples are absent and provide exact fix suggestions, along with search techniques.
thinking
**Defining worked examples**

I want to search for the word "example" near references or explicit computations that match the theorem content. I need to figure out what counts as a worked example and establish criteria for that. Specifically, I'm looking for explicit theorems instantiated in named families, complete with computations, proofs, or sections—not just passing mentions. I might also need to inspect the introduction or main results file for descriptions related to MC1-5 and search for canonical labels.
codex
The concordance pins A–D and H cleanly, but MC1–5 are split across several theorem packages rather than a single table. I’m now reading the actual theorem statements and tracing whether each one is backed by a concrete family-level worked example, rather than just a status line or a passing reference.
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-isomorphism-main\\}|label\\{thm:higher-genus-inversion\\}|label\\{thm:quantum-complementarity-main\\}|label\\{thm:genus-universality\\}|label\\{thm:w-algebra-hochschild\\}|label\\{thm:virasoro-hochschild\\}|label\\{thm:critical-level-cohomology\\}|label\\{prop:chirhoch1-affine-km\\}\" chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:master-pbw\\}|label\\{thm:mc2-bar-intrinsic\\}|label\\{thm:master-theta\\}|label\\{thm:mc3-type-a-resolution\\}|label\\{thm:mc3-arbitrary-type\\}|label\\{thm:weightwise-MC4-principal-RTT\\}|label\\{thm:yangian-weightwise-MC4\\}|label\\{thm:general-hs-sewing\\}|label\\{thm:heisenberg-sewing\\}|label\\{thm:algebraic-string-dictionary\\}|label\\{thm:bv-bar-coderived\\}|label\\{conj:master-bv-brst\\}\" chapters | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"bar-cobar-isomorphism-main|higher-genus-inversion|quantum-complementarity-main|genus-universality|w-algebra-hochschild|virasoro-hochschild|critical-level-cohomology|chirhoch1-affine-km|master-pbw|mc2-bar-intrinsic|master-theta|mc3-type-a-resolution|mc3-arbitrary-type|weightwise-MC4-principal-RTT|yangian-weightwise-MC4|general-hs-sewing|heisenberg-sewing|algebraic-string-dictionary|bv-bar-coderived|master-bv-brst\" chapters/examples chapters/frame chapters/theory chapters/connections | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC1|MC2|MC3|MC4|MC5\" chapters/frame/guide_to_main_results.tex chapters/frame/heisenberg_frame.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/*.tex chapters/connections/concordance.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/free_fields.tex:4745:\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}
chapters/examples/yangians_computations.tex:3790:\label{thm:mc3-type-a-resolution}
chapters/examples/yangians_computations.tex:3875:\label{thm:mc3-arbitrary-type}% backward compat
chapters/examples/yangians_computations.tex:4602:\label{thm:yangian-weightwise-MC4}
chapters/connections/typeA_baxter_rees_theta.tex:546:\label{thm:weightwise-MC4-principal-RTT}
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%
chapters/theory/higher_genus_modular_koszul.tex:3499:\label{thm:mc2-bar-intrinsic}
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:434:\label{conj:master-bv-brst}
chapters/connections/bv_brst.tex:1883:\label{thm:bv-bar-coderived}%
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
chapters/connections/outlook.tex:674:\phantomsection\label{conj:master-bv-brst}
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
chapters/theory/chiral_center_theorem.tex:2009:\label{prop:chirhoch1-affine-km}
chapters/theory/higher_genus_complementarity.tex:459:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/hochschild_cohomology.tex:96:\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
chapters/theory/hochschild_cohomology.tex:150:\begin{theorem}[Critical level Lie algebra cohomology; \ClaimStatusProvedElsewhere]\label{thm:critical-level-cohomology}
chapters/theory/hochschild_cohomology.tex:205:\begin{theorem}[W-algebra Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
 succeeded in 52ms:
chapters/frame/preface_sections10_13_draft.tex:425:Theorem~\ref{thm:general-hs-sewing}), and the Heisenberg one-particle
chapters/frame/preface_sections10_13_draft.tex:429:(Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
chapters/frame/preface_sections10_13_draft.tex:433:including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/frame/preface_sections10_13_draft.tex:435:(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
chapters/frame/preface_sections10_13_draft.tex:560: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
chapters/frame/preface_sections10_13_draft.tex:563: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
chapters/frame/guide_to_main_results.tex:35: Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]
chapters/frame/guide_to_main_results.tex:41: Thm~\ref{thm:higher-genus-inversion} \\[4pt]
chapters/frame/guide_to_main_results.tex:47: Thm~\ref{thm:quantum-complementarity-main} \\[4pt]
chapters/frame/guide_to_main_results.tex:85: Thm~\ref{thm:mc2-bar-intrinsic} \\[4pt]
chapters/frame/guide_to_main_results.tex:107: Thms~\ref{thm:general-hs-sewing},
chapters/frame/guide_to_main_results.tex:108: \ref{thm:algebraic-string-dictionary},
chapters/frame/guide_to_main_results.tex:109: \ref{thm:bv-bar-coderived} \\[4pt]
chapters/frame/guide_to_main_results.tex:133:(Theorem~\ref{thm:general-hs-sewing}); at genus~$0$ the algebraic
chapters/frame/guide_to_main_results.tex:135:(Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level
chapters/frame/guide_to_main_results.tex:147: (Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/frame/guide_to_main_results.tex:157: (Theorem~\ref{thm:general-hs-sewing}).
chapters/frame/guide_to_main_results.tex:315:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)};
chapters/frame/guide_to_main_results.tex:317:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
chapters/examples/deformation_quantization.tex:711:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:1749:\index{MC1!algorithmic verification}
chapters/examples/bar_complex_tables.tex:1769:MC1 concentration ($E_2^{p,q} = 0$ for $q \neq 0$) therefore
chapters/examples/yangians_foundations.tex:117:\fi constrains the MC3 categorical lift:
chapters/examples/yangians_foundations.tex:118:the all-types MC3 core is proved
chapters/examples/yangians_foundations.tex:836: $\mathcal{O}^{\mathrm{sh}}$ is the MC3 programme;
chapters/examples/yangians_foundations.tex:1102:\item \emph{MC3 categorical closure.}
chapters/examples/yangians_foundations.tex:1119: by evaluation modules for all simple types. MC3 Layers~1
chapters/examples/yangians_foundations.tex:1170:\emph{Step~4: MC3 categorical closure.}
chapters/examples/yangians_foundations.tex:1207:\begin{remark}[MC3, the DK bridge, and the ordered bar]
chapters/examples/yangians_foundations.tex:1209:\index{MC3!ordered bar interpretation}
chapters/examples/yangians_foundations.tex:1211:\index{ordered bar complex!MC3 and DK bridge}
chapters/examples/yangians_foundations.tex:1212:The MC3 programme is natively an ordered-bar phenomenon. The
chapters/examples/yangians_foundations.tex:1235:Clebsch--Gordan multiplicities. MC3 is proved on the evaluation-generated core by
chapters/examples/yangians_foundations.tex:1512:\item \emph{MC4 closure.}
chapters/examples/yangians_foundations.tex:1515: automatic; the remaining MC4 input is compact generation plus
chapters/examples/yangians_foundations.tex:1555:The canonical H-level target already exists (Proposition~\ref{prop:yangian-canonical-hlevel-target}); the remaining MC4 problem is to equip it with compatible RTT-level quotients. Line-operator OPEs are organized by pole order, matching the RTT filtration, and the Maurer--Cartan element $r(z)$ appears as the degree-$2$ bar twisting morphism.
chapters/examples/yangians_foundations.tex:2538:\index{MC4!three-layer verification}
chapters/examples/yangians_foundations.tex:2575:Yangian completion programme (MC4 structural framework proved by Theorem~\ref{thm:completed-bar-cobar-strong}; the finite RTT stages lie in $\CompCl(\Fft)$). The evaluation-core comparison
chapters/examples/yangians_foundations.tex:2580:MC3 \textup{(}categorical CG closure plus the evaluation-generated-core
chapters/examples/yangians_foundations.tex:2583:not MC4-intrinsic.



thinking
**Auditing theorem examples**

I need to ensure we have the exact lines and theorem statements related to the user's findings. It's crucial to verify if there are any missing examples or weaknesses. My mission is to conduct an audit of the examples around the theorems. We're likely to find that some examples exist, but there may be other theorems lacking explicit worked examples. I should read the relevant sections carefully to check for any explicit mention or subsections regarding examples.
thinking
**Identifying worked examples**

To determine if something counts as a worked example, I need to see actual computations in the preceding lines. However, I should look for stronger worked example sections. The Heisenberg frame has clear theorems connected to A/B/C, which might be the easiest to analyze. For D, examples could be in beta_gamma, y_algebras, or genus_expansions. The user wants me to identify both obvious and subtle weaknesses, particularly noting any missing worked examples for the MC5 chain-level, which is only partly conjectural.
thinking
**Assessing weaknesses in examples**

Even if a theorem does have an example, there might still be weaknesses, like a lack of cross-references or examples being split across multiple files, which complicates the audit. I should flag missing back-references from the theorem to the example or instances where examples aren't clearly labeled. My goal is to conduct a thorough audit, and it's possible that findings for each theorem could reveal weaknesses. I wonder if MC3 or MC5 might lack worked examples.
codex
I’ve isolated the canonical labels. Next I’m checking the manuscript’s own “main results” table against concrete family-level sections, because a theorem can be “proved” in concordance yet still fail the worked-example standard if all it has is status prose or a dangling cross-reference.
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '60,170p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    60	 of generators. &
    61	 Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
    62	
    63	\hline\\[-8pt]
    64	\multicolumn{3}{@{}l}{\textsc{Additional principal results}} \\[2pt]
    65	\hline
    66	
    67	\textbf{Koszulness} &
    68	 Twelve characterizations of chiral Koszulness:
    69	 ten unconditionally proved equivalent, one conditional
    70	 (Lagrangian criterion, pending perfectness/nondegeneracy),
    71	 one one-directional (D-module purity: forward direction
    72	 established, converse open). &
    73	 Thm~\ref{thm:koszul-equivalences-meta} \\[4pt]
    74	
    75	\textbf{MC1 (PBW)} &
    76	 PBW spectral sequence degenerates at $E_2$ for all
    77	 standard families (Kac--Moody, Virasoro, $\cW_N$,
    78	 free fields, lattice). &
    79	 Prop~\ref{prop:pbw-universality} \\[4pt]
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,3698p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1828,1955p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
  1828	 formalism.
  1829	\end{itemize}
  1830	\end{remark}
  1831	
  1832	\begin{remark}[Three-pillar architecture and the MC open problems]
  1833	\label{rem:three-pillar-mc-unification}
  1834	\index{three-pillar architecture!MC open problems}
  1835	\index{MC open problems!three-pillar unification}
  1836	The three-pillar architecture determines the MC resolution strategy:
  1837	\begin{itemize}
  1838	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1839	 element in the modular convolution $sL_\infty$-algebra; the
  1840	 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
  1841	 obstruction tower) are the constructive content.
  1842	 MC1 (PBW concentration) holds unconditionally for universal
  1843	 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
  1844	 (Proposition~\ref{prop:pbw-universality}). For simple quotients
  1845	 $L_k(\fg)$ at admissible levels, PBW concentration fails at
  1846	 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
  1847	 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '80,245p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5260,5368p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '430,540p;4110,4188p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    80	$\mathcal{M}$ is
    81	\[\ChirHoch^*(\mathcal{A}, \mathcal{M})
    82	= \operatorname{RHom}_{\mathcal{D}_X}(\barBgeom(\mathcal{A}), \mathcal{M}).\]
    83	The chain-level model is Definition~\ref{def:chiral-hochschild}.
    84	\end{definition}
    85	
    86	\begin{theorem}[Comparison with classical theory {\cite{BD04}}; \ClaimStatusProvedElsewhere]\label{thm:hochschild-classical-comparison}
    87	There is a spectral sequence:
    88	\[E_2^{p,q} = HH^p(\mathcal{A}_0, H^q(\Omega^*_X)) \Rightarrow \ChirHoch^{p+q}(\mathcal{A})\]
    89	where $\mathcal{A}_0$ is the fiber at a point.
    90	\end{theorem}
    91	
    92	\section{Periodicity phenomena}
    93	
    94	\subsection{Virasoro Hochschild cohomology}
    95	
    96	\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
    97	For the Virasoro algebra at generic central charge $c$ (avoiding
    98	$c_{p,q} = 1 - 6(p-q)^2/(pq)$ and $c = 1$):
    99	\[\ChirHoch^n(\mathrm{Vir}_c) = \begin{cases}
 succeeded in 51ms:
   430	$\mathcal{Z}_{\cA}$ by the fiber-level identification
   431	from Step~3, which holds uniformly over the base.
   432	\end{proof}
   433	
   434	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   435	\index{Theorem C!decomposition}
   436	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   437	identification, this theorem) produces the ambient complex;
   438	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   439	gives the Verdier eigenspace decomposition and its Lagrangian
   440	splitting; $\mathrm{C}_2$
   441	(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
   442	conditional bar-side BV / shifted-symplectic upgrade.
   443	The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
   444	$\sigma$ exchanging the two eigenspaces; at the scalar level
   445	the complementarity formulas below are consequences of the
   446	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   447	separate $\mathrm{C}_2$ label:
   448	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
   449	while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
 succeeded in 51ms:
  5260	$(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2 = 0$
  5261	for \emph{all} $g \geq 1$, by Mumford's relation.
  5262	\end{example}
  5263	
  5264	\subsection{Summary table: obstruction classes for key examples}
  5265	\label{subsec:obstruction-summary-table}
  5266	
  5267	\begin{table}[ht]
  5268	\centering
  5269	\caption{Genus-$g$ obstruction classes For single-generator families, $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  5270	 holds unconditionally at all genera. For multi-weight families
  5271	 \textup{(}$W_3$\textup{)}, the formula is unconditional at $g = 1$;
  5272	 at $g \geq 2$, a cross-channel correction
  5273	 $\delta F_g^{\mathrm{cross}} \neq 0$
  5274	 \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
  5275	 \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.}
  5276	\label{tab:obstruction-summary}
  5277	\begin{tabular}{|l|c|c|}
  5278	\hline
  5279	\textbf{Chiral Algebra} & \textbf{Obstruction $\text{obs}_g$} & \textbf{Physical Meaning} \\


thinking
**Looking into theorem H**

I think I need to explore the theorem H canonical, possibly referred to as `thm:hochschild-polynomial-growth`. I haven't read it yet, so I should check out what concordance defines H as—something about being an aggregate. It seems necessary to inspect the main theorem H statement further. I might want to perform a search for the specific label to get more information. It's crucial I understand this better!
thinking
**Looking into theorem H**

I need to read the main theorem statement for the H theorem, specifically related to the affine KM generic level. The user is asking about each main theorem from A to D and H. I think the H theorem isn't just about individual family theorems; it likely includes the Hochschild polynomial growth aspect. My next step is to locate relevant examples to clarify this! I'll get started on that search.
codex
I’ve confirmed Theorem A explicitly points to a Heisenberg verification inside its own statement, and Theorem C similarly cites the Heisenberg complementarity section. The remaining question is not “are there any references,” but whether each theorem package has a genuinely worked family-level example or only a vague breadcrumb.
exec
/bin/zsh -lc "rg -n \"label\\{thm:hochschild-polynomial-growth\\}|Theorem H|hochschild-polynomial-growth\" chapters/theory/hochschild_cohomology.tex chapters/frame chapters/examples chapters/connections | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/hochschild_cohomology.tex:112:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
chapters/theory/hochschild_cohomology.tex:163:(Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:234:Koszulness. Theorem~H (Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:830:(Theorem~\ref{thm:hochschild-polynomial-growth}). The two invariants
chapters/frame/guide_to_main_results.tex:56:\textbf{Theorem H} &
chapters/frame/guide_to_main_results.tex:61: Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/connections/thqg_open_closed_realization.tex:300:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives
chapters/frame/heisenberg_frame.tex:206:\textbf{H}~(Theorem~\ref{thm:hochschild-polynomial-growth}): $\mathrm{ChirHoch}^*(\mathcal{H}_k) = (\mathbb{C}, \mathbb{C}, \mathbb{C})$ concentrated in degrees $\{0, 1, 2\}$; Hilbert polynomial $P(t) = 1 + t + t^2$.
chapters/frame/heisenberg_frame.tex:1992:(Theorem~\ref{thm:hochschild-polynomial-growth}) this complex is
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:167:\textbf{H}~(Theorem~\ref{thm:hochschild-polynomial-growth}): $\mathrm{ChirHoch}^*(\mathcal{H}_k) = (\mathbb{C}, \mathbb{C}, \mathbb{C})$ concentrated in degrees $\{0, 1, 2\}$; Hilbert polynomial $P(t) = 1 + t + t^2$.
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/bershadsky_polyakov.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/w_algebras.tex:2751: Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}.
chapters/examples/w_algebras.tex:2814: Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}.
chapters/examples/n2_superconformal.tex:54: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/moonshine.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1988,2036p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1300,1865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3780,4050p;4588,4668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:pbw-universality\\}|label\\{cor:mc3-all-types\\}|label\\{thm:completed-bar-cobar-strong\\}\" chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3490,3568p;4704,4760p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1988	because the deformation $c \mapsto c + \epsilon$ does not shift
  1989	conformal weights. The Virasoro Jacobi identity
  1990	(associativity of the OPE) forces all higher-weight deformations
  1991	within $\ChirHoch^2$ to vanish: there is no independent weight-$4$
  1992	deformation, no weight-$6$ deformation, etc.
  1993	\end{proof}
  1994	
  1995	The $\mathfrak{sl}_2$ computation in Part~(ii) already exhibits the
  1996	essential phenomenon: the first chiral Hochschild group
  1997	$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
  1998	This is not a coincidence special to rank one. For any simple Lie
  1999	algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
  2000	chirally Koszul with generating space $V = \fg$; the Koszul resolution
  2001	is a three-term complex whose degree-$1$ piece is $\fg$ itself.
  2002	Degree-$1$ Hochschild cochains are infinitesimal deformations of the
  2003	current algebra: maps $J^a \mapsto J^a + \epsilon\,\phi^a$ preserving
  2004	the OPE to first order. The space of such deformations is determined
  2005	by the generating space alone, and the generating space is~$\fg$.
  2006	The deformation space of $V_k(\fg)$ \emph{is}~$\fg$.
  2007	
 succeeded in 53ms:
  3780	of the Hern\'andez--Negu\c{t} ordinary/shifted bridge
  3781	\cite{HerNeg24} as the target theorem.
  3782	In type~$A$, option~(b) is reduced to a single remaining packet:
  3783	Theorem~\ref{thm:mc3-type-a-resolution} proves packages~(i)--(iii)
  3784	and isolates Conjecture~\ref{conj:dk-compacts-completion} as the last
  3785	step needed to reach the entire completed shifted-prefundamental
  3786	category.
  3787	\end{remark}
  3788	
  3789	\begin{theorem}[Type-$A$ MC3 reduction to the compact-completion packet; \ClaimStatusProvedHere]
  3790	\label{thm:mc3-type-a-resolution}
  3791	\index{MC3!type-A resolution|textbf}
  3792	\index{Drinfeld--Kohno!derived!type-A completion}
  3793	\index{prefundamental!Clebsch--Gordan closure!type A}
  3794	For $\mathfrak{g} = \mathfrak{sl}_N$ with $N \geq 2$, the old
  3795	four-package MC3 extension problem is reduced to a single remaining
  3796	compact-completion packet:
  3797	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  3798	\item \emph{Baxter exact triangles.}
  3799	 The TQ relations lift from $K_0$ to derived exact triangles in the
 succeeded in 53ms:
  1300	$\mathcal{H}_k$ is Koszul: the bar cohomology
  1301	\[
  1302	H^n\bigl(\barB(\mathcal{H}_k)\bigr) =
  1303	\begin{cases}
  1304	\mathbb{C} & n = 0, \\
  1305	\mathbb{C} \cdot c_k & n = 2, \\
  1306	0 & \text{otherwise}
  1307	\end{cases}
  1308	\]
  1309	is concentrated in the minimal degrees consistent with the
  1310	central extension, so the bar complex is formal
  1311	(quasi-isomorphic to its cohomology as a coalgebra).
  1312	Formality forces the counit~$\varepsilon$ to be
  1313	a quasi-isomorphism: the resolution carries no higher
  1314	obstructions.
  1315	
  1316	The chain of identifications underlying the duality:
  1317	\[
  1318	\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)
  1319	\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)
 succeeded in 51ms:
chapters/examples/yangians_computations.tex:4022:\label{cor:mc3-all-types}%
chapters/theory/bar_cobar_adjunction_curved.tex:946:\label{thm:completed-bar-cobar-strong}
chapters/theory/chiral_koszul_pairs.tex:1366:\label{prop:pbw-universality}
 succeeded in 51ms:
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
  3508	\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
  3509	with $d_\cA^{(0)} = \dzero$ the genus-$0$ bar differential.
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '1,85p;780,865p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	\chapter{Chiral Hochschild cohomology and deformation theory}
     2	
     3	\index{Hochschild cohomology!classical}
     4	\index{cyclic homology!chiral}
     5	
     6	The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ is the
     7	tangent complex to the MC moduli at~$\Theta_\cA$: the cohomology
     8	of the convolution $L_\infty$-algebra controlling deformations,
     9	obstructions, and bulk-field couplings.
    10	
    11	The chiral Hochschild complex carries a degree $-1$ Lie bracket
    12	(the chiral Gerstenhaber bracket, Theorem~\ref{thm:gerstenhaber-structure}),
    13	computed by OPE residues on FM configuration spaces.
    14	In the classical limit (fiber at a point), it recovers
    15	Gerstenhaber's bracket~\cite{Ger63} on associative Hochschild
    16	cochains. The chiral bracket is the strict shadow of a full
    17	$L_\infty$ bracket on the chiral Hochschild complex. In the strict model, $\mathrm{HH}^2$ classifies
    18	first-order deformations and $\mathrm{HH}^3$ contains obstructions;
    19	the $L_\infty$ extension records coherent homotopies governing
    20	convergence of formal deformations and transfer of Koszul properties
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '900,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1336,1412p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1336	bigraded by cohomological degree~$p$ and conformal weight~$q$.
  1337	Then $\cA$ is chirally Koszul if and only if
  1338	$\operatorname{Ext}^{p,q}_\cA(\omega_X, \omega_X) = 0$ for $p \neq q$.
  1339	
  1340	\smallskip\noindent\textbf{Classical precedent.}
  1341	On the formal disk $\hat{D}$, this reduces to the
  1342	Beilinson--Ginzburg--Soergel criterion for $\operatorname{Zhu}(\cA)$
  1343	\cite{BGS96}.
  1344	On $\bP^1$, diagonal vanishing follows from PBW since
  1345	$H^1(\bP^1, \cO) = 0$.
  1346	At genus $g \geq 1$, the Hodge-theoretic contributions from
  1347	$H^0(X, \omega_X)$ produce the exceptional set $\Sigma(\fg)$ of
  1348	Theorem~\ref{thm:bar-cohomology-level-independence} where diagonal
  1349	vanishing may fail.
  1350	
  1351	\end{theorem}
  1352	
  1353	\begin{proof}
  1354	Forward: $E_2$-collapse concentrates $H^*(\barBgeom(\cA))$ on
  1355	the diagonal $p = q$; since the bar resolution computes Ext,
 succeeded in 52ms:
   900	\[
   901	\cA = F^0\cA \supset F^1\cA \supset F^2\cA \supset \cdots,
   902	\qquad
   903	\textstyle\bigcap_{N \ge 0} F^{N+1}\cA = 0,
   904	\]
   905	such that:
   906	\begin{enumerate}
   907	\item $\cA$ is separated and complete:
   908	 $\cA \cong \varprojlim_N \cA_{\le N}$, where
   909	 $\cA_{\le N} := \cA/F^{N+1}\cA$;
   910	\item every quotient $\cA_{\le N}$ is finite type and lies in the proved
   911	 bar-cobar regime;
   912	\item $\bar\cA = F^1\cA$ (the augmentation ideal is the first filtration
   913	 piece); and
   914	\item all chiral $\Ainf$-operations are filtration-nondecreasing:
   915	 \begin{equation}\label{eq:strong-filtration-condition}
   916	 \mu_r(F^{i_1}\cA, \dots, F^{i_r}\cA)
   917	 \subset F^{i_1+\cdots+i_r}\cA.
   918	 \end{equation}
   919	\end{enumerate}
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '416,446p;1210,1234p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '1928,1972p;3608,3642p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   416	$\beta\gamma$ system is concentrated in degree~$0$:
   417	\[H^n(\bar{B}(\beta\gamma)) = \begin{cases}
   418	\mathbb{C} & n = 0 \\
   419	0 & n \geq 1
   420	\end{cases}\]
   421	This is the Koszul property: the bar complex is acyclic above degree~$0$.
   422	\end{theorem}
   423	
   424	\begin{proof}
   425	By the Koszul duality $(\beta\gamma)^! \cong \mathcal{F}$
   426	(Theorem~\ref{thm:betagamma-fermion-koszul}) and the bar-cobar
   427	adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}), the bar
   428	complex $\bar{B}(\beta\gamma)$ is quasi-isomorphic to the Chevalley
   429	coalgebra of the free fermion system. Since the $\beta\gamma$--fermion
   430	pair is Koszul (the underlying operadic duality is $\chirCom$--$\chirLie$,
   431	which is Koszul by Theorem~\ref{thm:chiral-koszul-duality}), acyclicity
   432	follows from the general inversion theorem
   433	(Theorem~\ref{thm:higher-genus-inversion}).
   434	
   435	Alternatively, one verifies directly: in degree~$0$, $H^0 = \mathbb{C}$
 succeeded in 51ms:
  1928	\end{table}
  1929	
  1930	\subsection{The three theorems for lattice algebras}
  1931	
  1932	\begin{remark}[Main theorems for lattice VOAs]
  1933	\label{rem:lattice-three-theorems}
  1934	\index{main theorems!lattice VOA verification}
  1935	The computations of this chapter provide an abelian verification of the
  1936	main theorems of Part~\ref{part:bar-complex}. Each verification reveals structure invisible
  1937	in the abstract theory:
  1938	
  1939	\begin{enumerate}
  1940	\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
  1941	 Applied to $\Vlat_\Lambda$, the bar-cobar adjunction shows
  1942	 that the lattice bar complex concentrates in
  1943	 conformal-weight-graded degrees, with the concentration pattern
  1944	 governed by the root system of $\Lambda$
  1945	 (Theorem~\ref{thm:lattice:bar-structure}). The Koszul dual is
  1946	 identified as the lattice algebra with inverse cocycle
  1947	 (Theorem~\ref{thm:lattice:koszul-dual}), so the duality is
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '1038,1066p;1950,1972p;2638,2654p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1038	at every weight through $h = 16$
  1039	(Computation~\ref{comp:w3-deg3-cohom}):
  1040	\begin{center}
  1041	\renewcommand{\arraystretch}{1.1}
  1042	\begin{tabular}{c|ccccccccccc}
  1043	$h$ & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
  1044	\hline
  1045	$\dim \barB^3_h$ & 2 & 12 & 42 & 112 & 270 & 600 & 1260 & 2520 & 4884 & 9152 & 16758 \\
  1046	$\dim H^3_h$ & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
  1047	\end{tabular}
  1048	\end{center}
  1049	The bar complex is enormous but exact in degree~$3$: this is the
  1050	Koszul property, sector by sector. For the global statement,
  1051	$\Einf$-Koszulness of $\mathcal{W}_3$ at generic~$k$ is
  1052	Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
  1053	Combined with sectorwise finiteness, this gives the factorization
  1054	bar-cobar quasi-isomorphism
  1055	$\Omega^{\mathrm{fact}}(\barB^{\mathrm{fact}}(\mathcal{W}_3))
  1056	\xrightarrow{\sim} \mathcal{W}_3$
  1057	on $\operatorname{Ran}(X)$.

thinking
**Inspecting examples for results**

I notice we have many exact lines and need to figure out which examples might be missing. My next step is to look at the top part of the guide to the main results, specifically sections A-D and H, to see what's there. I wonder if reviewing these sections will help me identify anything we're lacking. Let's check them out together!
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '1,65p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	% ======================================================================
     2	% GUIDE TO MAIN RESULTS
     3	% A compact reference for the five main theorems and their dependencies.
     4	% ======================================================================
     5	
     6	\chapter*{Guide to main results}
     7	\addcontentsline{toc}{chapter}{Guide to main results}
     8	\label{ch:guide}%
     9	
    10	\noindent
    11	The principal results, with labels, locations, and logical
    12	dependencies. All five theorems hold for augmented chiral
    13	algebras~$\cA$ on a smooth projective curve~$X$ satisfying the
    14	standing finiteness conditions (\S\ref{sec:standing-assumptions}).
    15	
    16	\medskip
    17	
    18	\renewcommand{\arraystretch}{1.3}
    19	\begin{longtable}{@{}lp{8.5cm}l@{}}
    20	\textsc{Label} & \textsc{Statement} & \textsc{Location} \\


thinking
**Investigating theorem discrepancies**

I’m noticing a possible discrepancy here where one guide points to `thm:modular-characteristic`, while another refers to `thm:genus-universality`. I need to investigate if these are actually the same theorem or not. It would be helpful to perform a search on the labels to confirm any relations between these theorems. I want to ensure I’m clear on this to avoid confusion!
thinking
**Investigating theorem discrepancies**

I’m finding that the theorem guide and concordance use different labels for theorem D. I wonder if this could indicate a potential drift in status or location. This is relevant since the task is about an unfinished work audit and particularly about identifying weaknesses. I should verify the actual label's existence and how it relates. A quick search around `thm:modular-characteristic` might clarify things.
codex
A second-order issue has appeared: the guide cites Theorem D via `thm:modular-characteristic`, while the concordance identifies D with `thm:genus-universality`. I’m checking whether that’s a harmless alias or a live locator drift, because if the main-results guide and concordance point to different theorem surfaces, the example audit becomes structurally unreliable.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5168,5306p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:modular-characteristic\\}|label\\{thm:genus-universality\\}|Theorem D\" chapters/theory/higher_genus_foundations.tex chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex chapters/frame/heisenberg_frame.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\begin\\{example\\}|\\\\begin\\{remark\\}\\[.*example|worked example|for example|example\" chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/yangians_computations.tex chapters/frame/heisenberg_frame.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:hochschild-polynomial-growth\\}|thm:hochschild-polynomial-growth|Theorem~H\" chapters/examples chapters/frame chapters/connections | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5168	(where $\lambda_3^2 \in \mathrm{CH}^6(\overline{\mathcal{M}}_3)$
  5169	with $\dim \overline{\mathcal{M}}_3 = 6$, so the dimensional
  5170	argument fails) and all $g \geq 4$.
  5171	\end{remark}
  5172	
  5173	\begin{remark}[Multi-generator nilpotence]\label{rem:multi-generator-nilpotence}
  5174	\index{obstruction class!nilpotence!multi-generator}
  5175	For multi-generator algebras,
  5176	$\mathrm{obs}_1 = \kappa \cdot \lambda_1$
  5177	\textup{(g=1 only; all-weight at g=1 is unconditional)}
  5178	(Proposition~\ref{prop:multi-generator-obstruction}\textup{(a)}),
  5179	so $(\mathrm{obs}_1)^2 = \kappa^2 \cdot \lambda_1^2 = 0$
  5180	by Mumford's relation $\lambda_g^2 = 0$ \textup{(LOCAL)}.
  5181	For uniform-weight algebras, the same nilpotence holds at all genera;
  5182	for multi-weight algebras at $g \geq 2$, nilpotence follows from
  5183	Theorem~\ref{thm:multi-generator-universality}.
  5184	\end{remark}
  5185	
  5186	\begin{corollary}[Mumford multiplicative relations for obstruction classes; \ClaimStatusProvedHere]
  5187	\label{cor:mumford-multiplicative}
 succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:49:\textbf{Theorem D} &
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
 succeeded in 51ms:
chapters/examples/yangians_computations.tex:48:\begin{example}[Quiver of type \texorpdfstring{$A_n$}{A_n}]\label{ex:coulomb-an}
chapters/examples/yangians_computations.tex:54:\end{example}
chapters/examples/yangians_computations.tex:93:\begin{example}[Jordan quiver CoHA]\label{ex:jordan-coha}
chapters/examples/yangians_computations.tex:99:\end{example}
chapters/examples/yangians_computations.tex:137:\begin{example}[Type \texorpdfstring{$A_1$}{A_1} quiver with framing]
chapters/examples/yangians_computations.tex:162:\end{example}
chapters/examples/yangians_computations.tex:4391:\begin{example}[Pure $\fg$-gauge theory]
chapters/examples/yangians_computations.tex:4407:\end{example}
chapters/frame/heisenberg_frame.tex:104:supplies the first example where the $\Eone$ ordering is genuine:
chapters/frame/heisenberg_frame.tex:1224:\index{twisting morphism!Heisenberg example}
chapters/frame/heisenberg_frame.tex:2359:The free-field examples expose the two independent axes of the
chapters/frame/heisenberg_frame.tex:2615:$\widehat{\mathfrak{sl}}_{2,k}$ is the first example where the full
chapters/frame/heisenberg_frame.tex:3162:not just the Arnold relation. Every subsequent example
chapters/frame/heisenberg_frame.tex:3167:\subsection{The braided example: the odd current algebra and the spectral
chapters/frame/heisenberg_frame.tex:4082:\noindent\textbf{The three-example comparison.}\enspace
chapters/frame/heisenberg_frame.tex:4083:The odd current algebra is the third example in the Rosetta Stone,
chapters/frame/heisenberg_frame.tex:4149:Genuinely $\Eone$ example
chapters/frame/heisenberg_frame.tex:4180:All three examples are $\Einf$-chiral: their $R$-matrices are
chapters/frame/heisenberg_frame.tex:4237:The three examples of this section are the $\Einf$ base camp.
chapters/frame/heisenberg_frame.tex:4658:operadic structure visible in the Heisenberg example.
 succeeded in 51ms:
chapters/frame/preface_sections10_13_draft.tex:117:by Theorem~H), and the lines
chapters/frame/preface_sections10_13_draft.tex:138:growth (Theorem~H) is the HKR theorem for the Lagrangian embedding.
chapters/frame/preface_sections2_4_draft.tex:1199:Hochschild complex: Theorem~H identifies the deformation ring.
chapters/frame/guide_to_main_results.tex:61: Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
chapters/frame/guide_to_main_results.tex:195:(complementarity) requires~D. Theorem~H (Hochschild) is
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/frame/preface.tex:107:at all genera on the uniform-weight locus Theorem~H bounds the chiral Hochschild complex in degrees
chapters/frame/preface.tex:1235:\noindent\textbf{Theorem~H} (chiral Hochschild cohomology, generic
chapters/frame/preface.tex:2125:Hochschild complex: Theorem~H identifies the deformation ring.
chapters/frame/preface.tex:3433:\subsection*{9.3.\enspace Chiral Hochschild cohomology (Theorem~H)}
chapters/frame/preface.tex:3644: $\mathrm{ChirHoch}^*(\cA)$: the subject of Theorem~H,
chapters/frame/preface.tex:3850:by Theorem~H), and the lines
chapters/frame/preface.tex:3871:growth (Theorem~H) is the HKR theorem for the Lagrangian embedding.
chapters/connections/thqg_open_closed_realization.tex:299:Gerstenhaber algebra. On the Koszul locus, Theorem~H
chapters/connections/thqg_open_closed_realization.tex:300:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives
chapters/frame/heisenberg_frame.tex:206:\textbf{H}~(Theorem~\ref{thm:hochschild-polynomial-growth}): $\mathrm{ChirHoch}^*(\mathcal{H}_k) = (\mathbb{C}, \mathbb{C}, \mathbb{C})$ concentrated in degrees $\{0, 1, 2\}$; Hilbert polynomial $P(t) = 1 + t + t^2$.
chapters/frame/heisenberg_frame.tex:1991:By Theorem~H
chapters/frame/heisenberg_frame.tex:1992:(Theorem~\ref{thm:hochschild-polynomial-growth}) this complex is
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/frame/preface_section1_v2.tex:518:the chiral Hochschild polynomial growth (Theorem~H) are all
exec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1984,2006p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1984	\item \textbf{Derived chiral center and bulk.}
  1985	The derived chiral center of $\cH_k$ is the chiral Hochschild complex
  1986	\[
  1987	 \mathrm{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)
  1988	 \;=\;
  1989	 \ChirHoch^{\bullet}(\cH_k,\cH_k).
  1990	\]
  1991	By Theorem~H
  1992	(Theorem~\ref{thm:hochschild-polynomial-growth}) this complex is
  1993	concentrated in degrees $\{0,1,2\}$ with Hilbert polynomial
  1994	$P(t) = 1 + t + t^2$, hence total dimension~$3$. The
  1995	explicit computation in~\S\ref{sec:frame-center-theorem}
  1996	(Computation~\ref{comp:heisenberg-center}) gives
  1997	\[
  1998	 \ChirHoch^0(\cH_k) = \bC,
  1999	 \qquad
  2000	 \ChirHoch^1(\cH_k) = \bC\cdot D,
  2001	 \qquad
  2002	 \ChirHoch^2(\cH_k) = \bC\cdot \delta_k,
  2003	\]
exec
/bin/zsh -lc "rg -n \"begin\\{theorem\\}\\[.*hochschild-polynomial-growth|label\\{thm:hochschild-polynomial-growth\\}\" chapters/theory/hochschild_cohomology.tex && nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '1120,1188p'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Searching globally for the theorem**

I’m considering that the term "rg" may not be found simply because its theorem label is somewhere else. So, I should expand my approach and search on a broader scale. I'll look into various sources to see if I can locate relevant information, ensuring I’m thorough in my search. Let's see what I can uncover globally!
exec
/bin/zsh -lc "rg -n \"label\\{thm:hochschild-polynomial-growth\\}|hochschild-polynomial-growth\" chapters/theory/hochschild_cohomology.tex chapters/theory chapters | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/hochschild_cohomology.tex:112:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
chapters/theory/hochschild_cohomology.tex:163:(Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:234:Koszulness. Theorem~H (Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:830:(Theorem~\ref{thm:hochschild-polynomial-growth}). The two invariants
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/higher_genus_modular_koszul.tex:29700: \textup{(}Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:29785:(Theorem~\ref{thm:hochschild-polynomial-growth}). Under the
chapters/theory/fourier_seed.tex:975:Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/examples/bershadsky_polyakov.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/chiral_koszul_pairs.tex:1448:\textup{(Theorem~\ref{thm:hochschild-polynomial-growth})}
chapters/examples/moonshine.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/introduction.tex:666: Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/examples/n2_superconformal.tex:54: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/koszul_pair_structure.tex:574:bound on a curve (Theorem~\ref{thm:hochschild-polynomial-growth}):
chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
chapters/theory/chiral_hochschild_koszul.tex:884:By Theorem~\ref{thm:hochschild-polynomial-growth},
chapters/theory/chiral_hochschild_koszul.tex:923:Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
chapters/theory/chiral_hochschild_koszul.tex:4121:vanishes for $n > 2$ by Theorem~\ref{thm:hochschild-polynomial-growth})
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '680,760p;868,936p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   680	$\mathcal{Z}(\cA)$ and $\mathcal{Z}(\cA^!)$ via the canonical isomorphism
   681	$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$ of
   682	Theorem~\ref{thm:quantum-complementarity-main}(Step~7), one obtains
   683	a duality on the endomorphism complex
   684	$\mathrm{End}_{D(\mathrm{Mod}_{\cA})}(\cA) \cong
   685	\mathrm{End}_{D(\mathrm{Comod}_{\cA^!})}(\cA^!)^{\vee}$
   686	by the module Koszul duality equivalence
   687	(Theorem~\ref{thm:e1-module-koszul-duality}).
   688	Passing to cohomology, Lemma~\ref{lem:hochschild-shift-computation}
   689	computes the grading shift: the variable~$[n+2]$ collapses to the
   690	uniform~$[2]$. The $\omega_X$ twist comes from Serre duality on
   691	the underlying curve, yielding the result.
   692	\end{proof}
   693	
   694	\begin{remark}[Proof infrastructure]
   695	Both proofs use the bar-cobar quasi-isomorphism at all genera
   696	(Theorem~\ref{thm:higher-genus-inversion}) and the Kodaira--Spencer map
   697	for Koszul pairs
   698	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   699	\end{remark}
codex
Theorem H is anchored cleanly: its actual statement is in `chiral_hochschild_koszul.tex`, and the manuscript does give concrete family computations for Heisenberg, Virasoro, and principal W-algebras. I’m now checking whether the MC package is comparably concrete or whether some of its “main results” are only declared in summary tables and never worked out on a named family.
exec
/bin/zsh -lc "nl -ba chapters/examples/bar_complex_tables.tex | sed -n '1738,1778p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1360,1418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '180,245p;430,470p;788,812p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '160,230p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1866,1918p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:heisenberg-sewing\\}|label\\{thm:general-hs-sewing\\}|label\\{thm:algebraic-string-dictionary\\}|label\\{thm:bv-bar-coderived\\}|label\\{cor:string-amplitude-genus0\\}\" chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1360	exists $0 < q < 1$ such that
  1361	\begin{equation}\label{eq:hs-sewing}
  1362	\sum_{a,b,c \geq 0} q^{a+b+c}\,
  1363	\|m_{a,b}^c\|_{\mathrm{HS}}^2
  1364	\;<\; \infty.
  1365	\end{equation}
  1366	Define the \emph{weighted completion}
  1367	$H_q := \widehat{\bigoplus}_{n \geq 0} q^n H_n$.
  1368	\end{definition}
  1369	
  1370	\begin{proposition}[Closed amplitudes are trace class;
  1371	\ClaimStatusProvedHere]\label{prop:hs-trace-class}%
  1372	Under HS-sewing, $m_q \colon H_q \,\widehat{\otimes}\, H_q \to H_q$
  1373	is Hilbert--Schmidt and every closed amplitude is trace class.
  1374	\end{proposition}
  1375	
  1376	\begin{proof}
  1377	$\|m_q\|_{\mathrm{HS}}^2 = \sum_{a,b,c} q^{a+b+c}
  1378	\|m_{a,b}^c\|_{\mathrm{HS}}^2 < \infty$ by~\eqref{eq:hs-sewing}.
  1379	A genus-$g$ surface with~$n$ punctures decomposes into $2g-2+n$
 succeeded in 51ms:
  1866	 & unresolved at chain level & harmonic correction survives \\
  1867	\bottomrule
  1868	\end{tabular}
  1869	\end{center}
  1870	For class~$\mathsf{M}$, the quartic discrepancy
  1871	$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
  1872	\kappa / \operatorname{Im}(\tau)$ is not a coboundary
  1873	in the ordinary chain complex. A coderived upgrade requires the
  1874	conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
  1875	one must prove the curvature-factorization formula for the full
  1876	harmonic discrepancy and then prove that the resulting BV/bar
  1877	comparison map has coacyclic cone in the sense of
  1878	Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
  1879	\end{remark}
  1880	
  1881	\begin{theorem}[Conditional BV$=$bar in the coderived category;
  1882	\ClaimStatusConditional]%
  1883	\label{thm:bv-bar-coderived}%
  1884	\index{BV algebra!bar complex identification!coderived category|textbf}%
  1885	\index{coderived category!BV/bar identification|textbf}%
 succeeded in 52ms:
  1738	$\dim (V_k)_h^{\mathfrak{g}} = [q^h]\,\prod_{n \ge 1}
  1739	(1-q^n)^{-1}$ for~$\mathfrak{sl}_2$.
  1740	The Sugawara construction
  1741	$T = \frac{1}{2(k+2)}\sum_a {:}J^a J^a{:}$
  1742	acts as~$L_0 = h$ on each weight-$h$ subspace, confirming the
  1743	conformal-weight grading of the bar complex.
  1744	\end{remark}
  1745	
  1746	\begin{proposition}[PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data;
  1747	\ClaimStatusProvedHere]\label{prop:pbw-e2-from-vacuum-module}
  1748	\index{PBW spectral sequence!E2 from vacuum module}
  1749	\index{MC1!algorithmic verification}
  1750	Let $\mathfrak{g}$ be a simple Lie algebra and
  1751	$\widehat{\mathfrak{g}}_k$ the associated Kac--Moody algebra
  1752	with vacuum module~$V_k$.
  1753	The $E_2$ page of the PBW spectral sequence for
  1754	$\barB(\widehat{\mathfrak{g}}_k)$ is:
  1755	\begin{equation}\label{eq:pbw-e2-vacuum}
  1756	E_2^{p,q}
  1757	\;\cong\;
 succeeded in 53ms:
   180	HS-sewing package
   181	\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
   182	$+$ subexponential sector growth implies HS-sewing convergence;
   183	Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
   184	Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
   185	identification is still conjectural; at genus~$0$ the algebraic
   186	BRST/bar comparison is proved
   187	\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
   188	while the tree-level amplitude pairing requires the additional
   189	hypothesis isolated in
   190	Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
   191	orthogonal weak flank, not a link in this dependency chain.
   192	
   193	\begin{theorem}[Higher-genus PBW concentration for the standard
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
 succeeded in 52ms:
   160	\index{Heisenberg!mode--Bergman correspondence}%
   161	\index{Bergman space!Heisenberg identification}%
   162	On the algebraic Heisenberg Fock core, define the mode--Bergman map
   163	\[
   164	\Theta(a_{-n-1}\mathbf{1})
   165	\;=\;
   166	\sqrt{n{+}1}\; z^n
   167	\;\in\; A^2(D),
   168	\]
   169	extended multiplicatively by symmetrization:
   170	$\Theta(a_{-n_1-1} \cdots a_{-n_k-1}\mathbf{1})
   171	= \operatorname{Sym}(\Theta(a_{-n_1-1}\mathbf{1}) \otimes
   172	\cdots \otimes \Theta(a_{-n_k-1}\mathbf{1}))$.
   173	This gives a dense algebraic map
   174	$\Theta \colon \text{Fock core} \to
   175	\operatorname{Sym} A^2(D)$
   176	from the Heisenberg Fock space to the symmetric algebra of the
   177	Bergman space of the disk.
   178	Moriwaki~\cite{Moriwaki26b} identifies a conformally flat 2-disk
   179	algebra on $\operatorname{Sym} A^2(D)$ with the ind-Hilbert completion
 succeeded in 50ms:
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/free_fields.tex:4745:\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}
chapters/examples/free_fields.tex:4808:\ClaimStatusConditional]\label{cor:string-amplitude-genus0}
chapters/connections/bv_brst.tex:1883:\label{thm:bv-bar-coderived}%
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%


thinking
**Verifying theorem status**

I see there’s a discrepancy between the guide and the concordance regarding the theorem status. It seems like there’s a serious status drift since the file indicates conditions. I need to verify if there’s another theorem with the same label elsewhere and check for exact line references where they might have overclaimed. This is an important finding! So, I'll likely check the theorem registry to clarify the status.
thinking
**Checking references**

It seems there's a broken reference in Theorem D, which is labeled as `thm:modular-characteristic`, but that label doesn’t exist. I think I need to check if it might be labeled elsewhere or if it needs to be defined. Maybe conducting a search for that specific label would help clear things up. I want to ensure all references are correct and functional for a smoother reading experience. Let's see what I can find!
codex
I found a live status contradiction in the MC5 package: the guide/editorial summary says the coderived BV=bar component is proved, but the theorem carrying that label is actually marked `\ClaimStatusConditional`. That is not a cosmetic issue; it changes whether MC5 currently has a proved example at all on that lane.
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:master-pbw\\}|thm:master-pbw|MC1 for\" chapters/examples chapters/theory chapters/frame | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC5\" chapters/examples/heisenberg_eisenstein.tex chapters/examples/free_fields.tex chapters/connections/bv_brst.tex chapters/examples/yangians_computations.tex chapters/examples/w_algebras_deep.tex chapters/frame/heisenberg_frame.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"bv-bar-coderived|MC5 \\(genus tower\\)|analytic and coderived proved|coderived proved|\\"'$D'"\\"'^'"\\{\\\\mathrm\\{co\\}\\}-level BV=bar\" chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex metadata/theorem_registry.md | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:modular-characteristic|modular-characteristic\" chapters metadata | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bv-bar-coderived\\}\" -n chapters/connections/bv_brst.tex && nl -ba chapters/connections/concordance.tex | sed -n '1940,1970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:mc2-bar-intrinsic\\}|thm:mc2-bar-intrinsic|MC2\" chapters/examples/beta_gamma.tex chapters/examples/w3_holographic_datum.tex chapters/examples/lattice_foundations.tex chapters/examples/w_algebras_deep.tex chapters/frame/heisenberg_frame.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:2301:the higher-genus MC5 comparison between the handle-gluing BRST
chapters/connections/bv_brst.tex:2333:$bc$ ghosts gives the MC5 genus-$0$ case proved in
 succeeded in 52ms:
1883:\label{thm:bv-bar-coderived}%
  1940	 $\lambda_{\mathrm{eff}} = -6/c$
  1941	 (Chapter~\ref{chap:arithmetic-shadows},
  1942	 Remark~\ref{rem:effective-coupling}).
  1943	\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
  1944	 Inductive genus
  1945	 determination, 2D convergence (no UV renormalization needed),
  1946	 analytic-algebraic comparison, and the general HS-sewing criterion
  1947	 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
  1948	 plus subexponential sector growth implies convergence at all genera).
  1949	 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
  1950	 one-particle Bergman reduction, Fredholm determinant). At genus~$0$
  1951	 the algebraic BRST/bar comparison is proved
  1952	 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
  1953	 amplitude pairing is conditional on
  1954	 Corollary~\ref{cor:string-amplitude-genus0}.
  1955	 BV=bar in the coderived category is proved for all four shadow
  1956	 classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  1957	 The genuswise chain-level BV/BRST/bar identification remains
  1958	 conjectural (Conjecture~\ref{conj:master-bv-brst}; class~M
 succeeded in 52ms:
rg: regex parse error:
    (?:bv-bar-coderived|MC5 \(genus tower\)|analytic and coderived proved|coderived proved|$D\^\{\mathrm\{co\}\}-level BV=bar)
                                                                                                 ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1152: \textup{(}Theorem~\textup{\ref{thm:master-pbw})},
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/theory/higher_genus_modular_koszul.tex:28855:By PBW concentration (Theorem~\ref{thm:master-pbw}),
chapters/theory/bar_cobar_adjunction_inversion.tex:3844:(Theorem~\ref{thm:master-pbw}). The Virasoro algebra has a
 succeeded in 52ms:
metadata/dependency_graph.dot:2942:  thm_modular_characteristic [label="thm:modular-characteristic\ntheorem [Pr]\nModular characteristic", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:878:| `thm:modular-characteristic` | `theorem` | 2543 | Modular characteristic |
chapters/examples/heisenberg_eisenstein.tex:308:the free-field pairing $\kappa_{\mathrm{Heis}} + \kappa_{\mathrm{Heis}}' = 0$ This is the abelian case of Theorem~\ref{thm:modular-characteristic}(iv).
chapters/examples/heisenberg_eisenstein.tex:1103:Theorem~\ref{thm:modular-characteristic}(iii).
chapters/examples/free_fields.tex:261:(Theorem~\ref{thm:modular-characteristic}).
chapters/examples/free_fields.tex:367:Theorem~\ref{thm:modular-characteristic},
chapters/examples/free_fields.tex:4262:(Definition~\ref{def:modular-characteristic-package}) that determines
chapters/examples/yangians_foundations.tex:238: of Theorem~\textup{\ref{thm:modular-characteristic}};
chapters/examples/kac_moody.tex:1310:(Theorem~\ref{thm:modular-characteristic}(i)) controls every genus
chapters/examples/kac_moody.tex:1344:(Theorem~\ref{thm:modular-characteristic}) decomposes into
chapters/examples/kac_moody.tex:1596:Theorem~\textup{\ref{thm:modular-characteristic}}(iv).
metadata/label_index.json:7102:  "def:modular-characteristic-package": {
metadata/label_index.json:33714:  "rem:modular-characteristic-package": {
metadata/label_index.json:39990:  "sec:modular-characteristic": {
metadata/label_index.json:45058:  "tab:thqg-I-modular-characteristics": {
metadata/label_index.json:48262:  "thm:modular-characteristic": {
chapters/examples/toroidal_elliptic.tex:4130:Theorem~\textup{\ref{thm:modular-characteristic})}, in the
chapters/examples/toroidal_elliptic.tex:4160:(Theorem~\ref{thm:modular-characteristic})
metadata/claims.jsonl:246:{"label": "rem:four-test-interface", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 7345, "title": "The four-test interface", "refs_in_block": ["thm:bar-modular-operad", "thm:quantum-diff-squares-zero", "thm:mc2-bar-intrinsic", "thm:modular-characteristic", "thm:algebraic-family-rigidity", "thm:quantum-complementarity-main", "thm:ambient-complementarity-fmp", "thm:general-hs-sewing", "rem:thqg-I-admissible", "thm:heisenberg-sewing", "op:multi-generator-universality", "thm:multi-weight-genus-expansion", "thm:heisenberg-bv-bar-all-genera", "conj:master-bv-brst", "conj:analytic-realization"]}
metadata/claims.jsonl:300:{"label": "thm:volume-one-concrete-modular-datum", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/editorial_constitution.tex", "line": 2470, "title": "Volume~I concrete modular datum", "refs_in_block": ["def:modular-koszul-homotopy", "thm:bar-cobar-isomorphism-main", "thm:quantum-complementarity-main", "thm:mc2-bar-intrinsic", "def:modular-koszul-chiral", "thm:bar-nilpotency-complete", "thm:genus-universality", "thm:quantum-diff-squares-zero", "def:full-modular-package", "thm:modular-characteristic", "thm:discriminant-spectral", "rem:periodicity-triple"]}
 succeeded in 51ms:
chapters/examples/w3_holographic_datum.tex:146:(Theorem~\ref{thm:mc2-bar-intrinsic}), the element
chapters/frame/heisenberg_frame.tex:1811:full homotopy completion (Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/frame/heisenberg_frame.tex:1850: by Theorem~\ref{thm:mc2-bar-intrinsic}; for Heisenberg
chapters/frame/heisenberg_frame.tex:1866:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}). The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
chapters/examples/w_algebras_deep.tex:1960:In the language of Theorem~\ref{thm:mc2-bar-intrinsic}, the zero locus
chapters/examples/w_algebras_deep.tex:2533: (Theorem~\textup{\ref{thm:mc2-bar-intrinsic}})
chapters/examples/w_algebras_deep.tex:2615:(Theorem~\ref{thm:mc2-bar-intrinsic}) depends
chapters/examples/w_algebras_deep.tex:2732:(Theorem~\ref{thm:mc2-bar-intrinsic}),
chapters/examples/w_algebras_deep.tex:3618:\textup{(}Theorem~\ref{thm:mc2-bar-intrinsic}\textup{)} carries, in
chapters/examples/w_algebras_deep.tex:5456:$\Theta_{\cA}$: Theorem~\ref{thm:mc2-bar-intrinsic}
chapters/examples/beta_gamma.tex:337:(Theorem~\ref{thm:mc2-bar-intrinsic}). At degree~$2$,
chapters/examples/lattice_foundations.tex:211:Theorem~\ref{thm:mc2-bar-intrinsic},

thinking
**Inspecting theorem details**

I need to take a closer look at the statement of the theorem `thm:modular-characteristic` and maybe explore some examples related to it for D. There doesn’t seem to be any issues, so I’ll just view the theorem and check out the examples. It’s interesting how these things often connect, and I'm curious to see how it all fits together!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2648,2735p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2648	degeneration a chain map, to each consistency relation a chain
  2649	homotopy. Passing to cohomology recovers the classical
  2650	modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
  2651	Tsuchiya--Ueno--Yamada space of conformal blocks
  2652	(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
  2653	of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
  2654	entire genus tower (the spectral discriminant~$\Delta_\cA$,
  2655	periodicity profile~$\Pi_\cA$, and full MC
  2656	class~$\Theta_\cA$ require data beyond~$\kappa$;
  2657	see Definition~\ref{def:full-modular-package}).
  2658	
  2659	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2660	\label{thm:modular-characteristic}
  2661	\index{modular characteristic theorem|textbf}
  2662	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2663	\textup{[}Regime: curved-central
  2664	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2665	
  2666	Let $\cA$ be a modular Koszul chiral algebra
  2667	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
exec
/bin/zsh -lc "rg -n \"bv-bar-coderived\" metadata/theorem_registry.md metadata/claims.jsonl chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:109: \ref{thm:bv-bar-coderived} \\[4pt]
chapters/connections/editorial_constitution.tex:441:\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
chapters/connections/concordance.tex:697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:3291: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:6940: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:7611: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9690: \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
chapters/connections/concordance.tex:10087: (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/concordance.tex:11015: Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
chapters/connections/concordance.tex:11135: (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
metadata/claims.jsonl:179:{"label": "rem:bv-sewing-chain-level-classes", "env_type": "remark", "status": "ProvedElsewhere", "file": "chapters/connections/bv_brst.tex", "line": 1844, "title": "BV sewing at the chain level: class-by-class status", "refs_in_block": ["rem:bv-bar-class-c-proof", "prop:chain-level-three-obstructions", "thm:bv-bar-coderived"]}
metadata/claims.jsonl:180:{"label": "thm:bv-bar-coderived", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1895, "title": "BV$=$bar in the coderived category"}
metadata/claims.jsonl:283:{"label": "conj:master-bv-brst", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 434, "title": "BV/BRST/bar identification", "refs_in_block": ["thm:bv-bar-coderived", "thm:master-pbw", "thm:master-theta", "conj:master-dk-kl", "conj:master-infinite-generator", "thm:algebraic-string-dictionary", "cor:string-amplitude-genus0"]}
metadata/theorem_registry.md:2316:| `thm:bv-bar-coderived` | `theorem` | 1895 | BV$=$bar in the coderived category |
codex
The easy passes are A, B, C, D, H, MC1, and MC2: each of those has at least one concrete family-level computation on the page. MC3 and MC5 are the danger zones now, because their “main theorem” surfaces are split across status summaries and package theorems, which makes it much easier to claim example coverage that never actually materializes in a worked low-rank family.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '1088,1248p;2528,2620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '1,180p;3588,3668p;4070,4124p;4388,4412p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"sl_2|sl2|sl_3|type A|A_1|A_2|prefundamental|Clebsch--Gordan|evaluation-generated core|dk23-all-types|categorical-cg-all-types|mc3-type-a-resolution|cor:mc3-all-types\" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/lattice_foundations.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\begin\\{example\\}|Heisenberg sewing|algebraic-string-dictionary|bv-bar-coderived|MC5\" chapters/connections/bv_brst.tex chapters/examples/free_fields.tex chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex chapters/frame/guide_to_main_results.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\section{Coulomb branch algebras}
     2	\label{sec:coulomb-branch}
     3	% Regime I: Quadratic, $\Eone$-chiral (Convention~\ref{conv:regime-tags}).
     4	
     5	The preceding sections established the Yangian $Y(\fg)$ as an
     6	$\Eone$-chiral algebra and constructed its bar-cobar duality. This
     7	section and those that follow serve as the computational verification
     8	ground: every algebraic claim from the foundations is tested against
     9	explicit calculations with specific rank, specific shift parameters,
    10	and specific representation-theoretic data. The shifted Yangian isomorphisms with
    11	Coulomb branch algebras (Braverman--Finkelberg--Nakajima), the
    12	cohomological Hall algebra structures (Schiffmann--Vasserot,
    13	Kontsevich--Soibelman), and the explicit bar complex computations for
    14	$\mathfrak{sl}_2$ through $\mathfrak{sl}_4$ are the primary evidence
    15	for the MC3 thick generation theorem and the DK ladder beyond the
    16	evaluation locus.
    17	
    18	Two organizational principles govern the exposition. First, every
    19	computation is placed in the four-level hierarchy: gauge-theoretic
    20	origin (level~C), algebraic/RTT presentation (level~A),
 succeeded in 52ms:
  1088	\item \emph{Multiplicity-free $\ell$-weights.}
  1089	 For any simple~$\fg$ and any fundamental weight~$\omega_i$, the
  1090	 evaluation module $V_{\omega_i}(a) = \mathrm{ev}_a^*(V_{\omega_i})$
  1091	 of $Y(\fg)$ has the property that its $q$-character
  1092	 $\chi_q(V_{\omega_i}(a))$ is a sum of distinct $\ell$-weight
  1093	 monomials: no $\ell$-weight has multiplicity $> 1$. This is the
  1094	 fundamental result of Chari--Moura~\cite{ChariMoura06}.
  1095	 The multiplicity-free property ensures that the tensor product
  1096	 $V_{\omega_i}(a) \otimes V_{\omega_j}(b)$
  1097	 has a composition series whose successive quotients are
  1098	 $\ell$-weight-separated at generic spectral parameters, enabling
  1099	 the categorical Clebsch--Gordan decomposition
  1100	 \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.
  1101	
  1102	\item \emph{MC3 categorical closure.}
  1103	 The multiplicity-free $\ell$-weight property, combined with the
  1104	 Francis--Gaitsgory pro-nilpotent completion and the DK comparison
  1105	 on compacts, yields:
  1106	 \begin{enumerate}[label=\textup{(\alph*)}]
  1107	 \item Prefundamental representations $L_i^\pm(a)$ exist as
 succeeded in 50ms:
chapters/examples/yangians_foundations.tex:119:\textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}: categorical
chapters/examples/yangians_foundations.tex:120:prefundamental Clebsch--Gordan closure via multiplicity-free
chapters/examples/yangians_foundations.tex:275:representation for $A_1$--$A_4$, $B_2$--$B_4$, $C_2$--$C_4$,
chapters/examples/yangians_foundations.tex:791:\label{rem:prefundamental-koszul-extension}
chapters/examples/yangians_foundations.tex:792:\index{prefundamental module!Koszul dual}
chapters/examples/yangians_foundations.tex:795:prefundamental~$L^-(b)$
chapters/examples/yangians_foundations.tex:798:Koszul dual is the positive prefundamental~$L^+(b')$ with Drinfeld
chapters/examples/yangians_foundations.tex:800:pole~$1/(u - b)$ of~$L^-$). The prefundamental Clebsch--Gordan
chapters/examples/yangians_foundations.tex:802:(Theorem~\ref{thm:shifted-prefundamental-generation},
chapters/examples/yangians_foundations.tex:804:preserves the prefundamental class, so any eventual Koszul-duality
chapters/examples/yangians_foundations.tex:807:prefundamental-duality statement.
chapters/examples/yangians_foundations.tex:812:\index{tensor ideal!prefundamental}%
chapters/examples/yangians_foundations.tex:814:The prefundamental Clebsch--Gordan
chapters/examples/yangians_foundations.tex:815:(Proposition~\ref{prop:prefundamental-clebsch-gordan})
chapters/examples/yangians_foundations.tex:819:for the thick subcategory generated by the prefundamental family
chapters/examples/yangians_foundations.tex:840: \textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}; the
chapters/examples/yangians_foundations.tex:845:\begin{example}[Yangian \texorpdfstring{$Y(\mathfrak{sl}_2)$}{Y(sl_2)} fundamental modules]
chapters/examples/yangians_foundations.tex:846:\label{ex:yangian-sl2-modules}
chapters/examples/yangians_foundations.tex:847:\index{Yangian!sl2 modules@sl2 mods}
chapters/examples/yangians_foundations.tex:1061: (Computation~\ref{comp:sl2-collision-residue-kz}).
 succeeded in 53ms:
chapters/frame/guide_to_main_results.tex:99:\textbf{MC5 (genus tower)} &
chapters/frame/guide_to_main_results.tex:102: all genera; Heisenberg sewing via Fredholm determinant.
chapters/frame/guide_to_main_results.tex:108: \ref{thm:algebraic-string-dictionary},
chapters/frame/guide_to_main_results.tex:109: \ref{thm:bv-bar-coderived} \\[4pt]
chapters/frame/guide_to_main_results.tex:131:MC1 through MC4 are proved. MC5 is partially proved: the analytic
chapters/frame/guide_to_main_results.tex:135:(Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level
chapters/connections/genus_complete.tex:703:Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
chapters/connections/genus_complete.tex:1740:\item The Heisenberg sewing theorem
chapters/examples/heisenberg_eisenstein.tex:187:\begin{theorem}[Heisenberg sewing theorem;
chapters/examples/heisenberg_eisenstein.tex:2489:\item the Heisenberg sewing theorem
chapters/connections/bv_brst.tex:37:Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
chapters/connections/bv_brst.tex:1827:the sense of the coderived formalism. Theorem~\ref{thm:bv-bar-coderived}
chapters/connections/bv_brst.tex:1874:conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
chapters/connections/bv_brst.tex:1883:\label{thm:bv-bar-coderived}%
chapters/connections/bv_brst.tex:1951:\label{rem:bv-bar-coderived-higher-genus}%
chapters/connections/bv_brst.tex:1956:mechanism behind Theorem~\ref{thm:bv-bar-coderived}. A proof would
chapters/connections/bv_brst.tex:1973:\label{rem:bv-bar-coderived-why}
chapters/connections/bv_brst.tex:2301:the higher-genus MC5 comparison between the handle-gluing BRST
chapters/connections/bv_brst.tex:2333:$bc$ ghosts gives the MC5 genus-$0$ case proved in
chapters/examples/free_fields.tex:4745:\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}

thinking
**Investigating MC3 references**

I found that MC3 might reference an example related to `yangians_foundations.tex` with an explicit module for Y(sl2) fundamental modules. There's also mention of various computations in `yangians_computations.tex` concerning sl2/sl3, which could be relevant to prefundamental CG. I need to look closely at lines 845 and beyond to confirm this connection and see if it can indeed support MC3. Let’s get reading!
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '840,878p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   840	 \textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}; the
   841	 residual DK-4/5 extension/completion packet is downstream.
   842	\end{enumerate}
   843	\end{remark}
   844	
   845	\begin{example}[Yangian \texorpdfstring{$Y(\mathfrak{sl}_2)$}{Y(sl_2)} fundamental modules]
   846	\label{ex:yangian-sl2-modules}
   847	\index{Yangian!sl2 modules@sl2 mods}
   848	The Yangian $Y(\mathfrak{sl}_2)$ has evaluation modules
   849	$V(a) \cong \mathbb{C}^2$ for each $a \in \mathbb{C}$. The
   850	$R$-matrix on $V(a) \otimes V(b)$ is:
   851	\[
   852	R(u) = \frac{u - \hbar P}{u}
   853	= \begin{pmatrix}
   854	1 - \frac{\hbar}{u} & 0 & 0 & 0 \\
   855	0 & 1 & \frac{-\hbar}{u} & 0 \\
   856	0 & \frac{-\hbar}{u} & 1 & 0 \\
   857	0 & 0 & 0 & 1 - \frac{\hbar}{u}
   858	\end{pmatrix}
   859	\quad\text{at } u = a-b,
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3248,3372p;3418,3456p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3248	only in the identification of the graded pieces with simple
  3249	prefundamentals; at non-generic parameters, the graded pieces
  3250	may be indecomposable but reducible, and the thick-generation
  3251	conclusion still holds.
  3252	\end{remark}
  3253	
  3254	\begin{computation}[Thick generation obstruction analysis for \texorpdfstring{$Y(\mathfrak{sl}_2)$}{Y(sl_2)}]
  3255	\label{comp:thick-generation-sl2}
  3256	\index{thick generation!obstruction analysis}
  3257	For $L^-_a$ the negative prefundamental module of~$Y(\mathfrak{sl}_2)$
  3258	with character $\operatorname{ch}(L^-) = \prod_{n \geq 1}(1-q^{2n})^{-1}$
  3259	(partition generating function), the character factorizes as
  3260	\begin{equation}\label{eq:fock-verma-factorization}
  3261	 \operatorname{ch}(L^-)
  3262	 \;=\;
  3263	 \operatorname{ch}(M(0)) \cdot \prod_{n \geq 2}(1-q^{2n})^{-1},
  3264	\end{equation}
  3265	identifying a ``multi-particle'' factor $F_{\geq 2}$ with weight
  3266	multiplicities $p_2(k) := p(k) - p(k-1)$ (partitions into parts
  3267	$\geq 2$). This factorization is the character shadow of the
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '840,872p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   840	
   841	The Virasoro example exposes the shape of the general completion
   842	problem: finite-type truncations $W_N$ lie in the proved Koszul
   843	regime, and the challenge is to assemble these finite-stage
   844	quasi-isomorphisms into a completed quasi-isomorphism for the full
   845	infinite-type algebra. The obstacle is purely analytic (convergence
   846	of the inverse system), and it admits a clean algebraic resolution
   847	once the correct filtration axiom is identified.
   848	
   849	\begin{example}[\texorpdfstring{$W_\infty$}{W-infinity}: MC4 completion (proved)]
   850	\label{ex:winfty-completion-frontier}
   851	
   852	The tower $W_\infty = \varprojlim_N W_N$ is the archetype of the
   853	programmatic regime: each finite stage~$W_N$ is principal finite
   854	type with proved bar-cobar quasi-isomorphism, but infinitely many
   855	generators prevent a direct application of the finite-stage
   856	theorem. The strong completion-tower theorem
   857	(Theorem~\ref{thm:completed-bar-cobar-strong}) resolves this:
   858	the strong filtration axiom
   859	$\mu_r(F^{i_1},\dots,F^{i_r}) \subset F^{i_1+\cdots+i_r}$


thinking
**Clarifying PBW claims**

I’m looking at editorial line 193-204, which discusses three finite-type interacting families. It mentions `prop:pbw-universality`, but that refers to universal vertex algebras, not lattices. I’m realizing the main results guide seems to mix up two separate PBW claims. It’s crucial to distinguish these concepts clearly so that the discussion stays accurate. I want to ensure I'm aligning the information properly without conflating ideas.
thinking
**Searching for resolution bounds**

I’m checking if there’s a resolution length bound related to a theorem. The guideline seems to indicate that the length is bounded by the number of generators. So, I’ll need to search for that specific phrase to get more details. This sounds like it could clarify a lot, and it’s exciting to dig deeper into this topic! Let’s see what information I can uncover!
exec
/bin/zsh -lc "rg -n \"length bounded by the number of generators|number of generators|resolution of length\" chapters/theory/chiral_hochschild_koszul.tex chapters/frame/guide_to_main_results.tex chapters/theory/hochschild_cohomology.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:59: Koszul resolution of length bounded by the number

thinking
**Evaluating search options**

I'm noticing there's no such phrase found in the files I've checked. This makes me wonder if I should expand my search parameters or try a more global approach. Broader searches might reveal more context or information that isn't immediately visible. It could lead me to helpful insights or details that I hadn't considered yet. Let’s see what comes up when I widen my search!
exec
/bin/zsh -lc "rg -n \"length bounded by the number|resolution of length bounded|bounded by the number of generators\" chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/frame/guide_to_main_results.tex:59: Koszul resolution of length bounded by the number
chapters/examples/w_algebras.tex:7005:former is conjecturally bounded by the number of generators; the










thinking
**Analyzing theorem claims**

I noticed that the guide seems to overstate theorem H by including an unsupported clause. I should reference specific lines and fix it by either deleting or replacing that clause. It's also worth checking other claims in the guide, like how theorem C suggests an upgrade to shifted-symplectic Lagrangian geometry. However, the main theorem is unconditional, while that upgrade is conditional. So I need to ensure the language in the guide accurately reflects this.
thinking
**Correcting theorem details**

I need to make a precise fix by adding that "Verdier-side Lagrangian splitting is unconditional; the ambient shifted-symplectic upgrade is conditional on perfectness/non-degeneracy," as stated in concordance lines 41-45. This could be a significant finding. The guide for Theorem B mentions quasi-isomorphism at all genera but overlooks the conditionality regarding the Koszul locus. It's essential to clarify this for accuracy since the guide may oversimplify the conditions, and there might be a missing worked example for Theorem H.
thinking
**Inspecting the guide for findings**

I need to check `guide_to_main_results` around line 43 for Theorem C and line 37 for Theorem B. We've already looked at some of this, but it might yield new findings. One crucial point to focus on is the status drift on MC5, specifically regarding the proof versus the conditional nature of `thm:bv-bar-coderived`. I think pinpointing these elements could help clarify the communication of these theorems.
thinking
**Clarifying example relevance**

I’m thinking about the guide being pretty generic, which might be acceptable in this case. I don't want to over-flag things. It seems like I need to consider if there are any findings related to Theorem H, as I know the user is specifically asking if there's no example connected to it. I want to make sure I'm thinking this through clearly for them!
thinking
**Evaluating example references**

I need to check if the guide has example pointers for MC1, MC3, and MC4. The user didn't ask directly about that, but there's a gap concerning example cross-links, which might be part of an unfinished work audit. While it seems medium to low importance, the user seeks an exact fix. I could suggest adding worked-example backlinks for MC3 and MC4 to improve clarity since the current references are scattered. However, I wonder if that’s being overly critical.
thinking
**Considering weaknesses analysis**

I think the phrase "tear apart every weakness" could be beneficial, but it might also apply to A/B/C/H, which feels like a lot to cover. I don’t want to overwhelm the user, so I should focus on producing high-signal findings. It seems important to concentrate only on genuine weaknesses rather than merely pointing out areas of inconvenience. This approach could provide deeper insights without getting bogged down by unnecessary details.
thinking
**Evaluating theorem references**

I’m considering the order for theorems `Thms\ref{thm:general-hs-sewing}, \ref{thm:heisenberg-sewing}, \ref{thm:algebraic-string-dictionary}` and wondering if I should add a conditional note if co-derived works remain. It seems right. I notice that guideline 87-91 mentions cor:mc3-all-types but lacks examples like `comp:thick-generation-sl2` or `ex:yangian-sl2-modules`. Additionally, the `guide_to_main_results` Theorem A, B, C, D, H rows don’t cite examples either. I might need to search `frame/heisenberg_frame` for more context.
thinking
**Evaluating metadata consistency**

I think this is important because the generated metadata is used during audits. Now, there might be another metadata issue I need to consider: the theorem registry mentions `thm:modular-characteristic` at line 2543, but the actual label appears at line 2660. Wait, theorem_registry line 878 also states line 2543. Hmm, this discrepancy of about 117 lines might not be a problem if it's due to preprocessing or line numbering changes. I'll need to delve deeper into this.
thinking
**Exploring theorem examples**

I’m thinking we could say that there’s no worked non-type-A example for the all-types MC3 theorem. This statement seems grounded if I search and don’t find any examples around theorem sections with B2, C2, or G2. I really want to make sure I’m understanding this correctly, so looking into the specific details of the theorem will be essential. Let’s keep an eye out for those examples!
thinking
**Finalizing findings structure**

I’m thinking I could briefly state that I checked 10 surfaces and note which had examples. The structured output contract indicates I need findings plus a summary. I wonder if I should also include a "no findings" statement, but since the user asked for findings in a specific format, it might make sense to just add a sentence about the theorem example coverage afterward. I think running more searches to confirm no example environments in bv_brst and MC3 non-type-A would be useful too.
codex
I have enough evidence to start separating genuine failures from mere awkward exposition. The current high-signal failures are not “there is no example anywhere” but “the manuscript’s own flagship summary surfaces misstate theorem status, omit the very example they mention, or overclaim what the cited theorem actually proves.”
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '20,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"shifted-symplectic-complementarity|Theorem C\" chapters/theory/higher_genus_complementarity.tex chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '24,61p;75,109p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    20	
    21	\bigskip
    22	
    23	\noindent\textbf{The five main theorems.}\quad
    24	The algebraic engine rests on five theorems, all proved.
    25	
    26	\begin{center}
    27	\renewcommand{\arraystretch}{1.3}
    28	\begin{tabular}{clp{7.5cm}l}
    29	& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
    30	\hline
    31	\textbf{A} & Bar-cobar adjunction
    32	 & $\barBch \dashv \Omegach$ on $\Ran(X)$,
    33	 with Verdier intertwining
    34	 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
    35	 & \ClaimStatusProvedHere \\
    36	\textbf{B} & Bar-cobar inversion
    37	 & $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
    38	 on the Koszul locus
    39	 \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
exec
/bin/zsh -lc "nl -ba metadata/claims.jsonl | sed -n '176,184p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:43:\textbf{Theorem C} &
chapters/theory/higher_genus_complementarity.tex:435:\index{Theorem C!decomposition}
chapters/theory/higher_genus_complementarity.tex:441:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
chapters/theory/higher_genus_complementarity.tex:1766:\index{Theorem C!proof architecture summary}
chapters/theory/higher_genus_complementarity.tex:1794:\index{Lagrangian self-intersection!Theorem C}
chapters/theory/higher_genus_complementarity.tex:1886:\label{sec:shifted-symplectic-complementarity}
chapters/theory/higher_genus_complementarity.tex:1899:\label{thm:shifted-symplectic-complementarity}
chapters/theory/higher_genus_complementarity.tex:2017:Theorem~\ref{thm:shifted-symplectic-complementarity} is a genus-$g$
chapters/theory/higher_genus_complementarity.tex:2095:Conditional on Theorem~\ref{thm:shifted-symplectic-complementarity},
chapters/connections/concordance.tex:4993:conditional on Theorem~\ref{thm:shifted-symplectic-complementarity}.
 succeeded in 53ms:
    24	\hline
    25	\endhead
    26	\textbf{Theorem A} &
    27	 Bar--cobar adjunction: $\barB_X \dashv \Omega_X$ on
    28	 $\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
    29	 \rightleftarrows
    30	 \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$,
    31	 intertwined with Verdier duality:
    32	 $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA)
    33	 \simeq \cA^!_\infty$ (factorization \emph{algebra},
    34	 not coalgebra). &
    35	 Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]
    36	
    37	\textbf{Theorem B} &
    38	 Bar--cobar inversion: on the Koszul locus, the counit
    39	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$ is a
    40	 quasi-isomorphism at all genera. &
    41	 Thm~\ref{thm:higher-genus-inversion} \\[4pt]
    42	
    43	\textbf{Theorem C} &
 succeeded in 52ms:
   176	{"label": "thm:bv-functor", "env_type": "theorem", "status": "Conditional", "file": "chapters/connections/bv_brst.tex", "line": 1350, "title": "Conditional BV functor package", "refs_in_block": ["thm:config-space-bv", "thm:verdier-bar-cobar"]}
   177	{"label": "thm:heisenberg-bv-bar-all-genera", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1400, "title": "BV $=$ bar for the Heisenberg at all genera", "labels_in_block": ["thm:heisenberg-bv-bar-all-genera", "eq:bv-bar-heisenberg"]}
   178	{"label": "prop:chain-level-three-obstructions", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1646, "title": "Three chain-level obstructions", "refs_in_block": ["conj:master-bv-brst", "rem:bv-bar-class-c-proof"]}
   179	{"label": "rem:bv-sewing-chain-level-classes", "env_type": "remark", "status": "ProvedElsewhere", "file": "chapters/connections/bv_brst.tex", "line": 1844, "title": "BV sewing at the chain level: class-by-class status", "refs_in_block": ["rem:bv-bar-class-c-proof", "prop:chain-level-three-obstructions", "thm:bv-bar-coderived"]}
   180	{"label": "thm:bv-bar-coderived", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1895, "title": "BV$=$bar in the coderived category"}
   181	{"label": "comp:burns-koszul-datum", "env_type": "computation", "status": "ProvedElsewhere", "file": "chapters/connections/bv_brst.tex", "line": 2061, "title": "Burns space Koszul datum"}
   182	{"label": "conj:non-cy-local-surfaces", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/bv_brst.tex", "line": 2142, "title": "Hirzebruch, del Pezzo, and Enriques Koszul data", "refs_in_block": ["tab:non-cy-local-surfaces", "rem:burns-shadow-class"]}
   183	{"label": "rem:non-cy-scope", "env_type": "remark", "status": "ProvedElsewhere", "file": "chapters/connections/bv_brst.tex", "line": 2179, "title": "Scope and status", "refs_in_block": ["tab:non-cy-local-surfaces"]}
   184	{"label": "__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:66", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/casimir_divisor_core_transport.tex", "line": 66, "title": "Universal property"}

thinking
**Investigating claims in JSONL**

I find it interesting that claims.jsonl features a proved theorem, `thm:heisenberg-bv-bar-all-genera`, at line 1400. I’m wondering if this could be related to the worked example for the MC5 coderived or chain-level theories. I'll need to investigate further and search through this document to gain more clarity. It’s important to dig deeper to fully understand how this theorem fits into the bigger picture!
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1388,1422p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1388	and~\ref{thm:bv-functor}, the BV bracket on
  1389	$\barB^{\mathrm{ch}}(\cA)$ would provide a bar-side
  1390	$(-1)$-shifted Poisson model for the deformation theory. The
  1391	unconditional shifted-symplectic statements used later in the
  1392	manuscript instead come from the Verdier pairing on
  1393	$C_g = R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$
  1394	\textup{(}Proposition~\ref{prop:ptvv-lagrangian}\textup{)} and from
  1395	the ambient cyclic deformation formal moduli problem
  1396	\textup{(}Theorem~\ref{thm:ambient-complementarity-fmp}\textup{)}.
  1397	\end{remark}
  1398	
  1399	\section{Resolution for the Heisenberg algebra at all genera}
  1400	\label{sec:bv-bar-heisenberg-all-genera}
  1401	\index{Heisenberg!BV/bar identification|textbf}
  1402	\index{BV algebra!bar complex identification!Heisenberg}
  1403	
  1404	The free-field case resolves
  1405	Conjecture~\ref{conj:master-bv-brst} at the scalar level
  1406	for the Heisenberg family. The proof uses four independent
  1407	arguments that all produce the same identity.






thinking
**Analyzing theorem weaknesses**

I’m considering whether there’s a contradiction regarding the overall proved status of the theorem with conditional scope. It seems I should flag some specific theorem lines that discuss quasi-isomorphism without the necessary conditions. Omitting the genus≥1 conditionality is a weakness since the main results should be compact. I might need to fix this by adding qualifiers. The user requested a harsh audit, which could reveal overstatements in Theorem C and H. Maybe I should also check coverage status per theorem and address example discoverability issues.
thinking
**Summarizing example coverage**

I’m thinking we might want to summarize that only MC3 all-types lacks a non-type-A example. Next, I should evaluate if there's any theorem with zero examples. From what I've gathered, it seems like there may not be any theorems among A-D, H, and MC1-5 without at least one worked example somewhere. However, MC5 might have a coderived theorem with a Heisenberg example, so it appears no main theorem is completely exampleless.
thinking
**Inspecting metadata and references**

I'm working with `theorem_registry.md` and realizing it doesn't show status, but `metadata/dependency_graph.dot` may indicate the status for `thm:bv-bar-coderived`. I need to look into the `concordance` line 7611 regarding the claimed resolved Dco. The user wants exhaustive information, so I might mention references while focusing on key surfaces like the guide and editorial constitution. I’ll also check if the `guide_to_main_results` has any relevant findings to share.
thinking
**Evaluating theorem discrepancies**

I’m looking at `guide_to_main_results` and comparing Theorem B lines 37-40 with concordance lines 36-45. The guide seems to erase genus≥1 conditionality, so I might suggest importing the wording. Theorem C has a similar issue with overclaimed upgrades, and Theorem H has an unsupported clause, pointing towards high or medium importance. There are also omissions in MC1 and MC5. My summary should clarify that all ten main theorem packages have at least one example, but five surfaces misrepresent or hide those details.
thinking
**Verifying theorem examples**

I could mention that I checked all ten theorem packages. I need to verify that Theorems A through D, H, and MC1 to MC5 each have at least one worked example included. This will help ensure accuracy in the summary and provide the user with the most comprehensive information possible. I want to make sure that I'm thorough and don't miss any key components in these theorems!
thinking
**Inspecting findings on results**

I need to check `guide_to_main_results` around lines 131-138, where it states that MC5 was partially proved and is conjectural at the chain level. That makes sense, so only the row might be wrong due to using `thm:bv-bar-coderived`, which is proven. I want to enhance the discoverability of examples, like noting that `guide_to_main_results.tex:107-109` is missing `\ref{thm:heisenberg-sewing}`. Also, I think MC3's row at `guide_to_main_results.tex:91` lacks a proper citation for its example.
exec
/bin/zsh -lc "rg -n \"thm_bv_bar_coderived|bv-bar-coderived\" metadata/dependency_graph.dot | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
190:  thm_bv_bar_coderived [label="thm:bv-bar-coderived\ntheorem [Pr]\nBV$=$bar in the coderived category", style=filled, fillcolor="#c8e6c9"];
3861:  rem_bv_sewing_chain_level_classes -> thm_bv_bar_coderived;
3927:  conj_master_bv_brst -> thm_bv_bar_coderived;



thinking
**Analyzing metadata and graph issues**

Okay, I’m looking at a dot file marked `[Pr]` with a green fill, and there seems to be some generated metadata drift. Maybe there are duplicates? I could mention the files claims.jsonl and dependency_graph.dot. Using one finding per file might work, making it exhaustive without overwhelming the user. I need to inspect line numbers in dependency_graph.dot, as I have 190 already. I can propose regenerating the graph so it reflects the corrected status. I'll suggest modifying certain rows for clarity on the claims as well.
thinking
**Updating theorem references**

I’m looking into the `concordance` from lines 1943-1958. The exact fix seems to be rewriting it to specify the proofs clearly: “analytic proved; Heisenberg scalar BV=bar proved; coderived BV=bar conditional on Theorem…” It looks like the current line may need to reflect any conditional status correctly. If there’s a conditional theorem, I’ll need to adjust the language. The update should split the MC5 status to clearly highlight the proof surfaces. I also want to ensure similar updates for editorial_constitution and the guide row MC5, particularly regarding any unsupported claims.
thinking
**Considering precise statements**

I think it might be better to narrow the statement to what the cited proposition proves since precision is crucial. The easiest fix would be to change lines 75-79 to say, "Every freely strongly generated vertex algebra is chirally Koszul." However, that alters the MC1 package's meaning. The user asked for an audit of current surfaces—maybe the better fix is to adjust the location to `Thm\ref{thm:master-pbw}` and rewrite it to address the three interacting families while considering the existing proofs.
exec
/bin/zsh -lc "rg -n \"heisenberg-bv-bar-all-genera\" chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex chapters/frame/preface.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/concordance.tex:699: (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
chapters/connections/concordance.tex:6943: (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
chapters/connections/concordance.tex:7767: (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
chapters/connections/concordance.tex:9693: \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
chapters/connections/concordance.tex:10109: (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '260,286p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   260	 $n \geq 3)$.}
   261	 The $R$-matrix is
   262	 \begin{equation}\label{eq:rmatrix-type-d}
   263	 R(u) = \mathbb{1} - \frac{P}{u} + \frac{Q}{u - \varkappa},
   264	 \qquad \varkappa = n - 1,
   265	 \end{equation}
   266	 with the same trace projection~$Q$ as type~$B$ (now on $\bC^{2n}$),
   267	 satisfying $Q^2 = 2n\, Q$ and $PQ = QP = Q$.
   268	\end{enumerate}
   269	In all four cases, the Yang--Baxter equation
   270	\begin{equation}\label{eq:ybe-all-types}
   271	R_{12}(u{-}v)\, R_{13}(u)\, R_{23}(v)
   272	= R_{23}(v)\, R_{13}(u)\, R_{12}(u{-}v)
   273	\end{equation}
   274	holds, verified numerically in the fundamental
   275	representation for $A_1$--$A_4$, $B_2$--$B_4$, $C_2$--$C_4$,
   276	$D_3$--$D_5$ at $10^3$ random spectral parameters per type
   277	\textup{(}\texttt{yangian\_rtt\_all\_types.py}\textup{)}.
   278	The RTT relation~\eqref{eq:rtt-relation} with the type-specific
   279	$R$-matrix defines $Y(\fg)$ for all classical~$\fg$.




thinking
**Evaluating theorem clarity**

I could mention free-field or lattice references, but they aren't precise enough. A smaller true fix would be better. I think it’s okay to avoid mentioning an option and just use the small true fix. 

In the document `yangians_computations.tex`, there's an issue where the all-types MC3 theorem is printed without a worked non-type-A example. I found a type-A/sl2 example, but that doesn't cover most failure-prone cases. So, I'll fix it by inserting a worked `B_2` or `C_2` example after Theorem\ref{thm:categorical-cg-all-types}. This will illustrate a multiplicity-free q-character and the resulting categorical prefundamental decomposition.
thinking
**Clarifying theorem package results**

I think I should mention that all 10 theorem packages include at least one worked example, maybe right before or in the summary. But the summary’s structure only allows for a concise statement: `Checked: N | Findings: N | Verdict: PASS/FAIL`. I can include a sentence to explain the results, specifying that A, B, C, D, H, MC1, MC2, MC3, MC4, and MC5 each have examples. I’ll keep the findings clear and concise, with bullets if possible.
thinking
**Formatting findings for output**

I need to return my findings in a structured way, using the format: `- [CRITICAL] file:line — PROBLEM: ... FIX: ...`. I can use flat bullets for clarity. I should definitely include the exact file and line numbers. For instance, for line 1943, I can start with `chapters/connections/concordance.tex:1943`. I’ll note line 99 for the guide row, 440 for editorial, 180 for claims, 43 for guide C, and 56 for guide H.
thinking
**Evaluating findings and summary**

I’m thinking I should note that all 10 main packages had at least one worked example above the summary. That seems important. I need to ensure I reference the line numbers for editorial between 440-455 like I did in the earlier output. It might help to mention both `metadata/dependency_graph.dot:190` and `claims.jsonl` in the PROBLEM and FIX sections, but I want to formulate that carefully to avoid confusion.
codex
- [CRITICAL] chapters/connections/concordance.tex:1943 — PROBLEM: the canonical MC5 row says “analytic and coderived proved” and then treats `thm:bv-bar-coderived` as proved, but the source theorem is explicitly `\ClaimStatusConditional` in `chapters/connections/bv_brst.tex:1881-1917`. FIX: rewrite the row to split the package truthfully: “analytic proved; genus-0 algebraic BRST/bar proved; Heisenberg scalar BV=bar proved (`thm:heisenberg-bv-bar-all-genera`); coderived BV=bar conditional (`thm:bv-bar-coderived`); chain-level conjectural; tree-level conditional.”

- [CRITICAL] chapters/frame/guide_to_main_results.tex:99 — PROBLEM: the flagship guide repeats the same false MC5 status, says `$D^{\mathrm{co}}$-level BV=bar proved`, and mentions “Heisenberg sewing via Fredholm determinant” without citing `thm:heisenberg-sewing` at all. FIX: change clause (3) to “$D^{\mathrm{co}}$-level BV=bar conditional,” add the proved Heisenberg scalar theorem `thm:heisenberg-bv-bar-all-genera`, and expand the location cell to include `\ref{thm:heisenberg-sewing}` alongside `\ref{thm:general-hs-sewing}` and `\ref{thm:algebraic-string-dictionary}`.

- [CRITICAL] chapters/connections/editorial_constitution.tex:440 — PROBLEM: the MC5 master-conjecture note says “Resolved in $D^{\mathrm{co}}$” by `thm:bv-bar-coderived`, again contradicting the theorem’s own conditional tag. FIX: replace “Resolved in $D^{\mathrm{co}}$” with “Conditional in $D^{\mathrm{co}}$,” then add a separate proved sentence pointing to `thm:heisenberg-bv-bar-all-genera` and the genus-0 theorem `thm:algebraic-string-dictionary`.

- [HIGH] metadata/claims.jsonl:180 — PROBLEM: generated metadata records `thm:bv-bar-coderived` as `"status": "ProvedHere"`, and the dependency graph likewise paints it proved (`metadata/dependency_graph.dot:190`), so downstream audit tooling is being fed a false closed status. FIX: regenerate the generated metadata from the TeX source so `thm:bv-bar-coderived` is `Conditional`, and regenerate the dependency graph so the node is no longer marked `[Pr]` / green.

- [HIGH] chapters/frame/guide_to_main_results.tex:43 — PROBLEM: the Theorem C row says the theorem is “Upgraded to shifted-symplectic Lagrangian geometry,” but the concordance makes the Verdier-side Lagrangian splitting unconditional and the ambient shifted-symplectic upgrade conditional (`chapters/connections/concordance.tex:47-53`), with the upgrade separated out as `thm:shifted-symplectic-complementarity` (`chapters/theory/higher_genus_complementarity.tex:441,1899`). FIX: rewrite the row to say “Verdier-side Lagrangian splitting unconditional; ambient shifted-symplectic upgrade conditional on perfectness/nondegeneracy,” or cite `thm:shifted-symplectic-complementarity` separately as conditional.

- [HIGH] chapters/frame/guide_to_main_results.tex:56 — PROBLEM: the Theorem H row adds “explicit Koszul resolution of length bounded by the number of generators,” but the cited theorem `thm:hochschild-polynomial-growth` only states concentration in degrees `0,1,2`, polynomial Hilbert series, and Koszul functoriality (`chapters/theory/chiral_hochschild_koszul.tex:701-749`). I did not find the claimed “length bounded by the number of generators” theorem on the audited H surface. FIX: delete that clause and replace the row text with the actual theorem content from `thm:hochschild-polynomial-growth`.

- [MEDIUM] chapters/frame/guide_to_main_results.tex:75 — PROBLEM: the MC1 row claims PBW degeneration for “Kac--Moody, Virasoro, `\cW_N`, free fields, lattice” but points only to `prop:pbw-universality`, whose printed scope is the freely-strongly-generated criterion (`chapters/theory/chiral_koszul_pairs.tex:1365-1379`) and whose listed families are universal Kac--Moody, universal Virasoro, and universal principal `\mathcal W` (`chapters/theory/chiral_koszul_pairs.tex:1390-1404`). The cited locator does not itself establish the five-family sentence. FIX: make the row smaller and true: restrict it to the universal/freely-strongly-generated families actually covered by `prop:pbw-universality`, or replace the locator with the actual family-by-family MC1 package.

- [MEDIUM] chapters/examples/yangians_computations.tex:3873 — PROBLEM: the all-types MC3 theorem surface has no worked non-type-A example in prose. On the audited MC3 surface, the concrete worked computation is still type-A / `Y(\mathfrak{sl}_2)` (`chapters/examples/yangians_computations.tex:3254-3328`), so the failure-prone non-simply-laced cases are not exercised by a printed example even though the theorem claims all simple types. FIX: insert a worked `B_2` or `C_2` example immediately after `thm:categorical-cg-all-types`, computing one multiplicity-free `q`-character and the resulting prefundamental categorical Clebsch--Gordan decomposition.

All 10 audited main packages `A, B, C, D, H, MC1, MC2, MC3, MC4, MC5` do have at least one worked example somewhere in source; none is completely exampleless. The failures are status drift, unsupported summary prose, and one missing non-type-A MC3 example on the theorem surface.

## Summary
Checked: 10 | Findings: 8 | Verdict: FAIL
tokens used
288,470
