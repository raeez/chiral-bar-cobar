# F03_definitions_shadow (818s)

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex:12518](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12518) — PROBLEM: the tower changes carrier mid-chapter. `Definition~\ref{def:extension-tower}` and `Definition~\ref{def:shadow-postnikov-tower}` put the MC tower in `\mathfrak g^{\mathrm{amb}}_{\cA}/F^{N+1}` at lines 12524, 12550, 12567, but the surrounding prose and `Theorem~\ref{thm:recursive-existence}` switch to `\gAmod/F^{N+1}` at lines 12773 and 13338-13464. The ambient carrier is not even defined until line 31515, and its square-zero differential is only stated at line 32023. As written, the tower has no stable, defined carrier. FIX: choose one carrier and enforce it. The minimal true fix is to split the constructions explicitly:
  `ambient tower`: lines 12480-12593 and 13302-13470 become `F^N\mathfrak g^{\mathrm{amb}}_{\cA}`, `\mathcal E^{\mathrm{amb}}_\cA(N)`, `\Theta^{\le r,\mathrm{amb}}_\cA`;
  `coinvariant tower`: introduce separately after [chapters/theory/higher_genus_modular_koszul.tex:10463](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10463) on `\gAmod`;
  add a comparison proposition after [chapters/theory/higher_genus_modular_koszul.tex:31515](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31515) stating exactly how `\mathfrak g^{\mathrm{amb}}_{\cA}` maps to `\gAmod`. Until that proposition exists, delete claims that a single tower lives in both.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:36](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:36) — PROBLEM: the opening treats `\gAmod` as already defined (`\Theta_\cA \in \gAmod`, weight filtration on `\gAmod`, truncations in `\gAmod`) but the first formal definition of the modular convolution dg Lie algebra is only at lines 10463-10507. The foundation is backwards: the chapter uses the carrier for ~10,000 lines before defining it. FIX: move the subsection beginning at [chapters/theory/higher_genus_modular_koszul.tex:10459](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10459) to the first occurrence of `\gAmod`, or insert there a local recall:
  `\gAmod := \prod_{2g-2+n>0}\Hom_{\Sigma_n}(C_*(\overline{\mathcal M}_{g,n}),\End_\cA(n))`,
  with a forward pointer to Definition~`\ref{def:modular-convolution-dg-lie}`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:39](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:39) — PROBLEM: the chapter invokes “the Maurer--Cartan equation” from the opening and again in the proof of Theorem~`\ref{thm:universal-theta}` at lines 3826-3830, but the first place that distinguishes the strict dg-Lie MC equation from the full quantum `L_\infty` MC equation is the later remark at lines 11022-11047. Until then, the chapter never states which MC notion its proofs are actually using. FIX: insert a short convention immediately after line 43 or immediately before line 3785:
  `Strict MC in \gAmod: D\Theta_\cA + \frac12[\Theta_\cA,\Theta_\cA]=0;`
  `Homotopy MC in \Definfmod(\cA): \sum_{n,g}\frac{\hbar^g}{n!}\ell_n^{(g)}(\Theta_\cA^{\otimes n})=0.`
  Then rewrite Remark~`\ref{rem:two-mc-equations}` as a later explanation, not the first definition.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:180](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:180) — PROBLEM: the file uses the ordered object `\Theta_\cA^{E_1}` and later `\MC((\gAmod)^{E_1})` at lines 3813-3815 and 4227-4229, but this chapter never defines the ordered convolution algebra. The actual carrier lives in another file, [chapters/theory/e1_modular_koszul.tex:234](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:234). That is a hidden import on a load-bearing object. FIX: at the first use add an explicit local scope sentence:
  `Here ({\gAmod})^{E_1}` denotes the ordered modular convolution dg Lie algebra of Definition~`\ref{def:e1-modular-convolution}` in Chapter~`\ref{chap:e1-modular-koszul}`, and `\operatorname{av}\colon ({\gAmod})^{E_1}\to\gAmod` is the averaging map.
  If this chapter is not meant to develop the ordered carrier, state that and forbid uncited use of `\Theta_\cA^{E_1}` before the cross-reference.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:131](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:131) — PROBLEM: the opening says “Exactly one of two cases holds (Theorem~`\ref{thm:single-line-dichotomy}`)” and then lists classes `\mathbf G`, `\mathbf L`, `\mathbf C`, `\mathbf M`. But the theorem later proved at lines 18809-18833 only gives `\mathbf G/\mathbf L/\mathbf M` on a primary line; `\mathbf C` is not part of that dichotomy. It enters separately through the global contact/stratum-separation material and is only formally defined much later at lines 16869ff. FIX: rewrite lines 131-144 as:
  `On a primary line, Theorem~\ref{thm:single-line-dichotomy} yields the three cases \mathbf G, \mathbf L, \mathbf M.`
  `The global contact class \mathbf C is added separately by Theorem~\ref{thm:shadow-archetype-classification} together with Remark~\ref{rem:contact-stratum-separation}.`
  Also add a one-line inline class definition here or move Definition~`\ref{def:shadow-depth-classification}` forward.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:16869](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16869) — PROBLEM: `Definition~\ref{def:shadow-depth-classification}` is not just a definition. After defining `\kappa_d(\cA)=r_{\max}(\cA)`, it switches at lines 16922-16935 to a different, unqualified notion of depth `d`, claiming finite depths `d\ge 5` are realized by lattices. Later the example table marks rank-48 and rank-72 lattices as class `\mathbf G` with `d=5,6` but `d_{\mathrm{alg}}=0` (lines 17162-17167), and the later remark at lines 19631-19640 explicitly separates arithmetic depth from algebraic depth. The definition is mixing two invariants and is therefore not self-consistent. FIX: end the definition at line 16921. Move lines 16922-16935 to a new remark after `Remark~\ref{rem:depth-arith-vs-homotopy}` and rewrite them as:
  `Higher-rank lattice VOAs can have larger total depth d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}} while remaining algebraically class \mathbf G, with d_{\mathrm{alg}}=0 and r_{\max}=2.`
  Do not use bare `d` inside the class definition.

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex:52](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:52) — PROBLEM: the opening and the overview at lines 97-101 put the obstruction class directly in `H^2(\cA^{\mathrm{sh}}_{r+1,0})`, but the formal definition later at lines 12557-12573 first places it in the filtered carrier cohomology and only then passes to the shadow algebra. That is a hidden conflation of the primary obstruction class with its shadow image. FIX: after fixing the carrier, replace the early codomain by
  `H^2(F^{r+1}\mathfrak g_{\text{chosen}}/F^{r+2}\mathfrak g_{\text{chosen}})`
  and add:
  `its image in \cA^{\mathrm{sh}}_{r+1,0} is the degree-(r+1), genus-0 shadow obstruction after Definition~\ref{def:shadow-algebra}.`

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex:12577](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12577) — PROBLEM: `\Theta_{\cA}^{\le 2} = \kappa(\cA)` is type-wrong. The left-hand side is a truncated MC element in a filtered Lie carrier; the right-hand side is a scalar. The chapter itself later gives the correctly typed formula at lines 30121-30123. FIX: replace line 12577 by
  `\Theta_{\cA}^{\le 2} = \kappa(\cA)\,\eta\otimes\Lambda`
  or, if only the projection is intended,
  `\pi_{2,0}(\Theta_{\cA}^{\le 2})=\kappa(\cA)`.
  Do not identify an MC truncation with a bare scalar.

- [LOW] [chapters/theory/higher_genus_modular_koszul.tex:78](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:78) — PROBLEM: `\Defcyc^{\mathrm{mod}}(\cA)` is foundational for the shadow algebra, but this chapter uses it on first appearance with no local definition and no citation. Its definition is external, at [chapters/theory/chiral_hochschild_koszul.tex:2244](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:2244). That is a hidden import at exactly the point where the chapter claims to be laying foundations. FIX: add `(Definition~\ref{def:modular-cyclic-deformation-complex})` after the first occurrence at line 78 and again in `Definition~\ref{def:shadow-algebra}` at lines 12799-12808, or inline a one-line recall of the complex.

## Summary
Checked: 9 | Findings: 9 | Verdict: FAIL


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
session id: 019d88ac-0161-7a10-97b0-db54eae27bdc
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
codex
Auditing [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex) as an adversarial foundation pass. I’m starting by loading the audit workflow, then I’ll read the live theorem surface and the specific prerequisite files this repo treats as authoritative before I enumerate defects.
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
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
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



thinking
**Considering audit approach**

I’m focused on auditing the target file and thinking of using the update plan since the task is substantial. I need to read the exact file and possibly cite dependencies directly. The explorer agent might be helpful for codebase questions to find the target file structure, labels, and definitions. Even though the task is auditing a mathematical tex file, I should still get grounded in the actual file contents. Using explorer to locate definitions and any suspicious references feels like a careful approach. Although we could also use tools like rg and sed, I’m leaning towards using the explorer as the instructions prefer it. I’m also wondering if updating the plan is necessary; it might be helpful, even if the user hasn’t requested it. Since this is an audit, providing PE templates might not be required.
thinking
**Finalizing findings approach**

I’m thinking that maybe when I quote the final findings, I won’t need to add too much. However, it might still be helpful to include some commentary to state the scope lock and plan. It’s important to clarify the context so that everything makes sense. I want to ensure that the user understands the limitations and the overall plan without overwhelming them with unnecessary details. So, okay, let’s proceed with that!
codex
Using `deep-beilinson-audit` because this is a pressure-test of a theorem chapter, not a style pass. Next I’m mapping the file’s internal definition/proof surface: labels, theorem blocks, every occurrence of `Theta_A`, `g^{E1}`, `g^{mod}`, the MC equation, and the G/L/C/M family classes, then I’ll read the cited dependencies those passages rely on.
Plan update
Foundation audit of higher_genus_modular_koszul.tex focused on definition order, hidden imports, and proof dependencies named by the user.
  → Map the target file: labels, claim blocks, and all occurrences of Theta_A, MC, g^{E1}, g^{mod}, G/L/C/M, and related references
  • Read the relevant target-file sections in context and inspect directly cited dependency definitions/proofs
  • Attack for missing definitions, hidden imports, unresolved references, and unjustified steps; re-verify each surviving finding

thinking
**Inspecting file details**

I need to inspect a file that’s probably large. I’m thinking of using the `rg` command to search for specific terms. It could be efficient to execute the commands in parallel to speed things up. First, I'll check the file length to see how big it really is, and then focus on identifying any relevant lines. I'll make sure to approach this systematically to avoid overlooking anything important!
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   35739 chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc "rg -n \"ref\\{def:|ref\\{thm:|eqref\\{eq:\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\begin\\{(definition|theorem|proposition|lemma|corollary|remark|conjecture|example|construction)\\}|\\\\ClaimStatus|\\\\label\\{\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theta_|Theta\\\\_|\\\\Theta|g\\"'^'"\\{E_1\\}|g\\"'^'"\\{mod\\}|\\\\gAmod|E1|Maurer|MC equation|Maurer--Cartan|G/L/C/M|class G|class L|class C|class M|shadow tower|convolution algebra|modular convolution|ordered lift|averag\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1264

17:characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
26:(Theorem~\ref{thm:bar-modular-operad}).
32:(Theorem~\ref{thm:higher-genus-inversion}).
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
80: (Definition~\ref{def:shadow-algebra})
87: (Definition~\ref{def:modular-bar-hamiltonian})
101: (Definition~\ref{def:shadow-postnikov-tower}).
112: Theorem~\ref{thm:recursive-existence}:
126: (Theorem~\ref{thm:riccati-algebraicity}). On any one-dimensional
132: (Theorem~\ref{thm:single-line-dichotomy}):
150: (Theorem~\ref{thm:shadow-formality-identification}). The
161: (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
184:Theorem~\ref{thm:gz26-commuting-differentials}; the Gaudin
186:Theorem~\ref{thm:gaudin-yangian-identification}.
205:For each $g \geq 0$, the bar-cobar inversion of Theorem~\ref{thm:higher-genus-inversion}
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
269:(Theorem~\ref{thm:bar-modular-operad}).
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
 exited 2 in 50ms:
rg: regex parse error:
    (?:\begin\{(definition|theorem|proposition|lemma|corollary|remark|conjecture|example|construction)\}|\ClaimStatus|\label\{)
                                                                                                         ^^
error: unrecognized escape sequence
 exited 2 in 50ms:
rg: regex parse error:
    (?:Theta_|Theta\_|\Theta|g\^\{E_1\}|g\^\{mod\}|\gAmod|E1|Maurer|MC equation|Maurer--Cartan|G/L/C/M|class G|class L|class C|class M|shadow tower|convolution algebra|modular convolution|ordered lift|averag)
                      ^^
error: unrecognized escape sequence

thinking
**Refining search syntax**

I need to refine the rg syntax for better precision. Using fixed strings might help. It seems like I also need to establish actual line numbers and context. I could use the explorer tool to find the specific section and line ranges, as well as any missing definitions. I should also inspect the beginning of the file to understand its structure since the user is asking for an audit of a chapter. Let's do a targeted search!
codex
I’ve got the file map. The next pass is narrower: I’m isolating the exact passages where the chapter claims to define or use `\Theta_\cA`, the convolution algebras, the Maurer–Cartan equation, and the G/L/C/M shadow classes, because the failure modes here are almost always order-of-definition or hidden-import defects rather than syntax.
exec
/bin/zsh -lc "rg -nF \"Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 410

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
exec
/bin/zsh -lc 'rg -nF "Maurer--Cartan" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF \"\\gAmod\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "class G" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "class L" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "class C" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "class M" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
449:a genus-completed Maurer--Cartan datum~$\Theta_{\cA}$
486:The genus tower arises from a filtered Maurer--Cartan deformation
2645:\index{universal Maurer--Cartan class|textbf}
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2661:\item The \emph{universal Maurer--Cartan class}
2752: is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
3176:Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
3686:\index{Maurer--Cartan element!two projections}
3785:\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
3787:\index{universal Maurer--Cartan class|textbf}
3791:universal Maurer--Cartan class
3830:gives the Maurer--Cartan equation. See
3970:simultaneously. The Maurer--Cartan equation
3988:\index{universal Maurer--Cartan class!bar-intrinsic construction}
4018:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
4127:\emph{(i) Maurer--Cartan.}
4147:which is the Maurer--Cartan equation
4314:$\Theta_\cA$ is automatically a Maurer--Cartan element.
4376:\index{Maurer--Cartan element!scattering-diagram construction}
 succeeded in 52ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
63:$\gAmod$ controls the extension tower: each finite truncation
2352: \in \MC(\gAmod)$ exists at all genera
3689:element~$\Theta_\cA \in \MC(\gAmod)$:
3710:in~$\gAmod$, not by the KdV hierarchy.
4018:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
4076: $D^2 = 0$ on $\gAmod$
4083: algebra $\gAmod$
4111: The weight filtration $F^N\gAmod$
4115: $\widehat{\gAmod} = \varprojlim_N \gAmod/F^{N+1}$
4226:$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
4229:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
4346: The identity $D^2 = 0$ on $\gAmod$ is
4351: $\widehat{\gAmod}$ is the inverse limit of
4352: finite-dimensional quotients $\gAmod/F^{N+1}$, and
4368:in $\gAmod/F^{N+1}$, the projections are compatible, and the
4371:an MC element in~$\widehat{\gAmod}$.
4382:$\widehat{\gAmod}$ of
4399:\exp(F^1\widehat{\gAmod}).
 exited 1 in 52ms:

 succeeded in 51ms:
26401:$F_1(\cA)=\kappa(\cA)/24$. The $\psi$-class CohFT
 exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -nF "g''^{E_1}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Exploring classification formats**

I’m considering how to represent the class G notation, possibly using boldface or something like \mathbf{G}. I think I need to dive into the classification and look for archetypes like G, L, C, and M. Direct lines seem necessary. Also, I’m pondering whether g^{E1} needs a different approach since I might not want to use a literal representation. I should search for more patterns to clarify my thoughts.
exec
/bin/zsh -lc "rg -n \"\\\\mathbf\\{G\\}|\\\\mathbf\\{L\\}|\\\\mathbf\\{C\\}|\\\\mathbf\\{M\\}|archetype|archetypes|depth classification|shadow-depth|single-line-dichotomy|nms-archetype-trichotomy\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"E_1\\}|E1|ordered lift|ordered.*Theta|coinvariant|averaging|Sigma_n|\\\\Sigma_n|g\\"'^'"\\{\\\\mathrm\\{mod\\}\\}|g\\"'^'"\\{mod\\}|g\\"'^'"\\{E1\\}|g\\"'^'"\\{E_1\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\mathbf\{G\}|\mathbf\{L\}|\mathbf\{C\}|\mathbf\{M\}|archetype|archetypes|depth classification|shadow-depth|single-line-dichotomy|nms-archetype-trichotomy)
       ^^
error: unrecognized escape sequence
 succeeded in 50ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

 exited 2 in 51ms:
rg: regex parse error:
    (?:E_1\}|E1|ordered lift|ordered.*Theta|coinvariant|averaging|Sigma_n|\Sigma_n|g\^\{\mathrm\{mod\}\}|g\^\{mod\}|g\^\{E1\}|g\^\{E_1\})
                                                                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -nF "def:shadow-algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:modular-bar-hamiltonian" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
80: (Definition~\ref{def:shadow-algebra})
4383:Definition~\ref{def:shadow-algebra}, graded by shadow degree, and
4597: Definition~\textup{\ref{def:shadow-algebra}}\textup{)}.
4611:(Definition~\ref{def:shadow-algebra}):
12786:\label{def:shadow-algebra}
30696: (Definition~\ref{def:shadow-algebra}).
 succeeded in 52ms:
87: (Definition~\ref{def:modular-bar-hamiltonian})
4774:Definition~\ref{def:modular-bar-hamiltonian}: the
21772:\textup{(}Definition~\textup{\ref{def:modular-bar-hamiltonian}})
31298:\label{def:modular-bar-hamiltonian}
exec
/bin/zsh -lc 'rg -nF "def:shadow-postnikov-tower" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "subsec:two-level-convention" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "thm:single-line-dichotomy" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:modular-convolution-dg-lie" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "thm:universal-theta" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:modular-koszul-chiral" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4084: (Definition~\ref{def:modular-convolution-dg-lie}).
4341: (Definition~\ref{def:modular-convolution-dg-lie},
8893: (Definition~\ref{def:modular-convolution-dg-lie}) on the arc space
10464:\label{def:modular-convolution-dg-lie}
11031:(Definition~\ref{def:modular-convolution-dg-lie}):
11127:Definition~\ref{def:modular-convolution-dg-lie} is its strict model.
11241:Definition~\ref{def:modular-convolution-dg-lie} is the strict
11727:(Definition~\ref{def:modular-convolution-dg-lie}) is the bar-side
12340:(Definition~\ref{def:modular-convolution-dg-lie}) induces a
13623:(Definition~\ref{def:modular-convolution-dg-lie}).
25868:(Definition~\ref{def:modular-convolution-dg-lie})
26918:convolution algebra (Definition~\ref{def:modular-convolution-dg-lie}):
30669:(Definition~\ref{def:modular-convolution-dg-lie}).
31180:(Definition~\ref{def:modular-convolution-dg-lie}).
32046:\textup{(}Definition~\textup{\ref{def:modular-convolution-dg-lie})},
 succeeded in 52ms:
62:(\S\ref{subsec:two-level-convention}). The weight filtration on
11113:\label{subsec:two-level-convention}
31142: \textup{(}\S\textup{\ref{subsec:two-level-convention}}\textup{)}.
31173:(\S\ref{subsec:two-level-convention}) establishes that
 succeeded in 52ms:
132: (Theorem~\ref{thm:single-line-dichotomy}):
16477:(Theorem~\ref{thm:single-line-dichotomy}):
16654:(Theorem~\ref{thm:single-line-dichotomy}). Hence
16840:(Theorem~\ref{thm:single-line-dichotomy}).
18795:\label{thm:single-line-dichotomy}
19516: \textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)}.
19533:and Theorem~\ref{thm:single-line-dichotomy}.
20313:Theorem~\ref{thm:single-line-dichotomy} gives
20330:so Theorem~\ref{thm:single-line-dichotomy} gives a perfect square
32450:\textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)},
35569:Theorem~\ref{thm:single-line-dichotomy} in the fixed family-level
35611:Theorem~\ref{thm:single-line-dichotomy},
35646:(Theorem~\ref{thm:single-line-dichotomy}) describes the
35665:Theorem~\ref{thm:single-line-dichotomy} is the equation of the
 succeeded in 52ms:
101: (Definition~\ref{def:shadow-postnikov-tower}).
2824:(Definition~\ref{def:shadow-postnikov-tower};
3981:Definition~\ref{def:shadow-postnikov-tower}.
4317:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.}%
10450:(Definition~\ref{def:shadow-postnikov-tower}).
10882:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
12533:\label{def:shadow-postnikov-tower}
13472:(Definition~\ref{def:shadow-postnikov-tower}).
15127:(Definition~\ref{def:shadow-postnikov-tower}):
15599: \textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
16063: \textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)}.
28902:(Definition~\ref{def:shadow-postnikov-tower}).
31004:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)}.
31290:(Definition~\ref{def:shadow-postnikov-tower}) is defined
 succeeded in 50ms:
673:(Theorem~\ref{thm:universal-theta}).
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2662: (Theorem~\ref{thm:universal-theta}):
2710:and~\ref{thm:universal-theta}).
2806:Theorem~\ref{thm:universal-theta}, made unconditional by
2825:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
3786:\label{thm:universal-theta}
3863:Theorem~\ref{thm:universal-theta} extends the canonical twisting
5282:The proof of Theorem~\ref{thm:universal-theta} assembles:
5816:Theorem~\ref{thm:universal-theta}. Then:
8417:In particular, Theorem~\ref{thm:universal-theta}
8475:Theorem~\textup{\ref{thm:universal-theta}} with the stated scalar
8512: $\Theta_{\cA}$ of Theorem~\ref{thm:universal-theta};
8525:modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
8535:$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
10348:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
10416:(Theorem~\ref{thm:universal-theta}) is established
14606:(Theorem~\ref{thm:universal-theta}). By
 succeeded in 51ms:
426:version; Definition~\ref{def:modular-koszul-chiral} gives the concrete
530:chosen model. Definition~\ref{def:modular-koszul-chiral} provides
535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
694:\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
799:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1041:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1392:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1580:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
1648:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1731:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
1783:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
2101:Definition~\textup{\ref{def:modular-koszul-chiral})} and
2219:Definition~\ref{def:modular-koszul-chiral}
2617:(Definition~\ref{def:modular-koszul-chiral}). The
2800:Definition~\ref{def:modular-koszul-chiral} and
2856:(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
3377:(Definition~\ref{def:modular-koszul-chiral}) realized as the
3846:(Definition~\textup{\ref{def:modular-koszul-chiral}}); see
4188:Definition~\textup{\ref{def:modular-koszul-chiral}}
4695:Definition~\textup{\ref{def:modular-koszul-chiral})}, the
exec
/bin/zsh -lc "sed -n '3780,3865p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '500,760p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{remark}[Shared discriminant, distinct sewing]\label{rem:shared-discriminant-sheet}
The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
\end{remark}

\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
\label{thm:universal-theta}
\index{universal Maurer--Cartan class|textbf}
For every modular Koszul chiral algebra~$\cA$ on a smooth
projective curve~$X$ with non-degenerate invariant form,
there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
universal Maurer--Cartan class
\[
\Theta_{\cA} \in
\operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
\bigr)
\]
such that:
 succeeded in 50ms:
$\boldsymbol{\Omega}_X \mathbf{B}_X(\cA) \simeq \cA$
on the Koszul locus in
$\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$.

\item\label{MK:complementarity-htpy}
\emph{(Lagrangian complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
The complementarity complex
$\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})$
decomposes as
$\mathbf{C}_g \simeq \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$,
where $\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}
\colon \mathbf{C}_g \to \mathbf{C}_g)$ and
$\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id})$
are homotopy eigenspaces of the Verdier involution~$\sigma$, each
Lagrangian for the shifted symplectic pairing
\textup{(}Proposition~\textup{\ref{prop:ptvv-lagrangian}},
Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}.
\end{enumerate}
The cohomological shadows
$Q_g(\cA) := H^*(\mathbf{Q}_g(\cA))$ and
exec
/bin/zsh -lc "sed -n '10450,11150p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12520,12870p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18780,18845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
(Definition~\ref{def:shadow-postnikov-tower}).
The five main theorems and the genus expansion descend from this tower;
Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
cubic and quartic shadows are proved at finite order.
The all-degree limit is a Maurer--Cartan element
$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
constructed from the genus-completed bar differential
(Theorem~\ref{thm:mc2-bar-intrinsic}).

\subsection{The modular convolution dg~Lie algebra}
\label{subsec:modular-convolution-algebra}
\index{modular convolution dg Lie algebra|textbf}

\begin{definition}[Modular convolution dg~Lie algebra]
\label{def:modular-convolution-dg-lie}
Let $\cA$ be a cyclic chiral algebra on a smooth projective curve~$X$.
The following dg~Lie algebra is the strict model of the modular
quantum $L_\infty$-algebra of
Theorem~\ref{thm:modular-homotopy-convolution}.
The \emph{modular convolution dg~Lie algebra} is
 succeeded in 51ms:
\label{eq:extension-tower}
\mathcal{E}_{\cA}(N)
:=
\operatorname{MC}\bigl(
\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
\bigr),
\qquad N \geq 1.
\end{equation}
A full lift is a compatible point of the inverse limit
$\Theta_{\cA} \in \varprojlim_N \mathcal{E}_{\cA}(N)$.
\end{definition}

\begin{definition}[Shadow obstruction tower]
\label{def:shadow-postnikov-tower}
\ClaimStatusProvedHere
\index{shadow obstruction tower|textbf}
\index{modular characteristic!shadow obstruction tower}
The \emph{shadow obstruction tower} of $\cA$
\textup{(}Figure~\textup{\ref{fig:shadow-postnikov-tower})}
is the sequence of
 succeeded in 50ms:
The shadow coefficients exhibit \emph{approximate alternation}:
$\operatorname{sgn}(S_r(c)) = (-1)^r$ for
$4 \leq r < r_*(c)$, where
$r_*(c) \approx \pi/|\pi - \arg(t_0)|$
and $t_0$ is the nearest complex zero of~$Q_L$.
The alternation arises from the binomial expansion of
$\sqrt{Q_L}$ around the Gaussian envelope; it breaks when
$\cos(r \cdot \arg(t_0))$ changes sign.
For $\mathrm{Vir}_{13}$: $r_* = 27$;
for $c = 1$: $r_* = 17$.
As $c \to \infty$: $\arg(t_0) \to \pi$ and
$r_* \to \infty$ (exact alternation in the semiclassical limit).
\end{remark}

\begin{theorem}[Single-line dichotomy; \ClaimStatusProvedHere]
\label{thm:single-line-dichotomy}
\index{single-line dichotomy|textbf}
\index{shadow obstruction tower!single-line dichotomy}
\index{shadow depth!pump mechanism}
Let $L$, $S_r$, $\alpha$, $\Delta$, $Q_L$ be as above.

thinking
**Considering line numbering and definitions**

I’m thinking I might need line numbers that aren't just absolute—so using `nl -ba` could help with that. I want exact line references, and later I'll open specific ranges using the same command. Next, I need to inspect the definition of shadow-depth classification, and I should look into the label and context to make sure I'm on the right track. It's all about getting the details sorted!
exec
/bin/zsh -lc 'rg -nF "g''^{'"\\mathrm{mod}}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "E_1" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:shadow-depth-classification" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30170,30230p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
181:shadow of the $E_1$-framed MC element.
806:$E_1$ page splits as
808:E_1^{p,q}(g)
810:E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
908:an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
1052:\emph{Step~1: Decomposition of the $E_1$ page.}
1066:collision divisors. The $E_1$ page concentrates
1090:Hence the $E_1$ page decomposes:
1092:E_1^{p,q}(g{=}1) \;=\; E_1^{p,q}(g{=}0)
1095:where $E_1(g{=}0)$ is the concentrated genus-$0$
1116:\;\longrightarrow\; E_1^{n-1,h}(g{=}0)
1407:\emph{Step~1: $E_1$ decomposition at genus~$g$.}
1426:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
1653:The genus-$g$ decomposition of the enriched $E_1$ page is identical to
1656:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
1911:already accounted for on~$E_1$), while generators with $s < 2$
2061:$E_1$ statement. The affine KM proof gives the boundary example:
2065:$E_1$-collapse claim without adding a false statement.
2278: $E_1$ differentials as on~$\mathbb{P}^1$: the
 succeeded in 52ms:
2489:(Definition~\ref{def:shadow-depth-classification})
12637:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}
16855:\label{def:shadow-depth-classification}
17176:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
17552:(Definition~\ref{def:shadow-depth-classification}).
18019:of Definition~\textup{\ref{def:shadow-depth-classification}}.
27979:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}\textup{)}
28875:(Definition~\textup{\ref{def:shadow-depth-classification}})
30180:(Definition~\ref{def:shadow-depth-classification}):
 succeeded in 51ms:
\end{proof}

\begin{definition}[Generalized Polyakov class]
\label{def:generalized-polyakov-class}
\index{Polyakov class!generalized|textbf}
\index{shadow depth!Polyakov class interpretation}
\index{effective action!shadow tower decomposition}
A chirally Koszul algebra~$\cA$ belongs to the
\emph{generalized Polyakov class} determined by its shadow
depth $r_{\max}(\cA)$
(Definition~\ref{def:shadow-depth-classification}):
\begin{center}
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}clp{24em}@{}}
\toprule
\emph{Class} & $r_{\max}$ & \emph{Effective action content} \\
\midrule
$\mathbf{G}$ & $2$
 & $S_{\mathrm{eff}}(\cA) = \kappa \cdot S_{\mathrm{Polyakov}}$.

thinking
**Inspecting definitions in context**

I'm noticing that the user is curious about the definitions related to g^{E1} and g^{mod}. It seems like I need to check if g^{E1} is specifically defined as ambient or modular, especially around the sections near 31980 and 31970. I also need to see if the file clarifies what g^{mod}_A is at 10464. I'll dig into those areas to gather the necessary information for the user!
codex
The initial defect pattern is already visible: the chapter’s opening uses foundational objects tens of thousands of lines before their formal definitions. I’m now checking whether those are acceptable forward references with local restatements, or whether they actually leave the reader without a usable definition when the proofs start leaning on them.
exec
/bin/zsh -lc "sed -n '16845,16920p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30660,30720p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '31940,32030p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12190,12240p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\pi_{r,g} \colon \gAmod
\longrightarrow
\operatorname{Hom}_{\Sigma_r}\!\bigl(
C_*(\overline{\mathcal{M}}_{g,r}),\;
\operatorname{End}_\cA(r)
\bigr)
\end{equation}
is the projection to the $(g,r)$-bigraded component of the
modular convolution algebra
(Definition~\ref{def:modular-convolution-dg-lie}).
Composing with the bar-intrinsic MC element
$\Theta_\cA = D_\cA - \dzero$
(Theorem~\ref{thm:mc2-bar-intrinsic}) gives:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Scalar curvature.}
 $\kappa(\cA) := \operatorname{tr}\,\pi_{2,0}(\Theta_\cA)$,
 the invariant of Theorem~\ref{thm:modular-characteristic}.
\item \emph{Spectral characteristic.}
 $T_{\mathrm{br},\cA} := \pi_{2,\bullet}(\Theta_\cA)|_{V^{\mathrm{br}}}$,
 with discriminant
 succeeded in 51ms:
fully resolved genus-$0$ stable graphs contributing to the
bracket $\ell_7^{(0)}$. The agreement with the HPL
route ($C_6 = 132$ planar trees) and the Feynman transform
route ($C_7 = 429$ binary trees on $8$ leaves) is a
consequence of the universal property
(Theorem~\ref{thm:shadow-formality-identification},
Step~$3$).
\end{proof}

\begin{definition}[Shadow depth classification]
\label{def:shadow-depth-classification}
\ClaimStatusProvedHere
\index{shadow depth|textbf}
\index{shadow depth!classification}
\index{shadow obstruction tower!depth classification}
Let $\cA$ be a modular Koszul chiral algebra with
obstruction classes $o_r(\cA)$ from
Construction~\ref{constr:obstruction-recursion}.
Define the \emph{shadow depth}
$\kappa_d(\cA) := r_{\max}(\cA) =
 succeeded in 51ms:
codimension-$2$ stratum appears in exactly two
codimension-$1$ strata with opposite orientations.
The ordering does not affect the orientation
cancellation.
\end{proof}

\begin{corollary}[$E_1$ ambient $D^2 = 0$]
\label{cor:e1-ambient-d-squared-zero}
\ClaimStatusProvedHere
\index{differential!E1 ambient square-zero@$E_1$ ambient square-zero}
The five-component differential on the ordered ambient
algebra
\textup{(}Definition~\textup{\ref{def:ordered-ambient-algebra}}\textup{)}
satisfies $D^2 = 0$. For each stable pair $(g,n)$, its geometric
source is the ordered relative
Fulton--MacPherson space
$\operatorname{FM}^{\mathrm{ord}}_k(\cC_{g,n}/\overline{\cM}_{g,n})$
of the universal curve: the ordered collision faces give the
bar part, whose square vanishes by the ordered Arnold cancellation,
and the base-degeneration faces give the same Hodge-class curvature
 succeeded in 51ms:
\end{equation}
where $\kappa_\rho$ is the push-pull correspondence from
$\operatorname{FM}_n(W/B)(\rho) \to
\prod_v \operatorname{FM}_{I_v}(Y_v \mathbin{|} D_v)$.
\end{construction}

\subsubsection{Modular tangent complex and characteristic shadows}

\begin{construction}[Modular tangent complex; \ClaimStatusProvedHere]
\label{const:vol1-modular-tangent-complex}
\index{modular tangent complex|textbf}
\index{Chern--Weil theory!modular factorization algebras}
Let $\Theta_\cA\in
\operatorname{MC}({\Definfmod}_{\!\log}(\cA;\mathfrak{U}))$. The
$L_\infty$-twisted differential
\begin{equation}\label{eq:twisted-differential-theta}
d_{\Theta_\cA}(x)
\;:=\;
\sum_{n\ge 0}\,\sum_{g\ge 0}
\frac{\hbar^g}{n!}\,

thinking
**Exploring shadow depth classification**

I’m finding something interesting about the definition of shadow depth classification, which mentions finite depths of 5 or more. This seems to contradict the previously stated limitations of d_alg, which can only be 0, 1, 2, or infinity. It’s a subtle yet severe contradiction. I need to check if shadow depth is indeed different from d_alg and how this all ties in with the classes defined earlier. I should inspect this depth-gap trichotomy proposition further.
exec
/bin/zsh -lc "rg -n \"d_\\{\\\\mathrm\\{alg\\}\\}|d_alg|depth gap|finite depths\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17520,17610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "prop:depth-gap-trichotomy" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:d_\{\mathrm\{alg\}\}|d_alg|depth gap|finite depths)
           ^^
error: unrecognized escape sequence
 succeeded in 50ms:
146: No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
17989:\label{prop:depth-gap-trichotomy}
 succeeded in 52ms:
while aspects~\textup{(ii)} and~\textup{(iii)} detect the
shadow depth class. The common notation~``$m_k$'' for both
\textup{(i)} and~\textup{(ii)} is a source of systematic
confusion (i)~lives on $H^*(\Barch)$,
(ii)~lives on~$\cA$, and (iii)~lives on~$\gAmod$.
Computational verification:
\texttt{compute/lib/theorem\_ainfty\_nonformality\_class\_m\_engine.py}.
\end{proposition}

\begin{proof}
Aspect~(i): Theorem~\ref{thm:koszul-equivalences-meta}(iii).
Aspect~(ii): for class~$\mathbf{G}$,
the SC operations on~$\cA$ vanish for $k \geq 3$ because
Heisenberg has trivial OPE beyond the Killing form.
For class~$\mathbf{L}$ (affine KM), $m_3^{\mathrm{SC}} \neq 0$
from the Jacobi cubic tree sum, but
$m_k^{\mathrm{SC}} = 0$ for $k \geq 4$ because the Jacobi
identity kills the quartic contact
(Proposition~\ref{prop:swiss-cheese-nonformality-by-class}).
For class~$\mathbf{C}$
codex
I found a likely structural contradiction, not just a missing cross-reference: one place says the only possible finite depths are the four G/L/C/M archetypes, while a later “definition” asserts finite depths `d ≥ 5` are realized by lattice examples. I’m checking whether that’s a genuine conflict of notions or an unannounced change of invariant; if it’s genuine, it’s a high-severity foundation defect.
exec
/bin/zsh -lc 'rg -nF "finite depths" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF \"d_{\\mathrm{alg}}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17980,18035p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
16909:\emph{finite depths $d \geq 5$} are realized by lattice vertex
 succeeded in 51ms:
147: $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$, with a gap at~$3$.
17114:$d_{\mathrm{alg}}$ &
17142: (\S\ref{sec:higher-depths}; class by $d_{\mathrm{alg}}$, cf.\
17172: d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
17182:$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
17189:$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
17196:$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
17215:$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
17248:$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
17277:$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
17907:\begin{lemma}[Impossibility of $d_{\mathrm{alg}} = 3$]
17915:$d_{\mathrm{alg}} = 3$ is impossible on any $\kappa \neq 0$ line.
17982:$d_{\mathrm{alg}} \in \{0, 1\}$ (finite tower, $S_4 = 0$) or
17983:$d_{\mathrm{alg}} = \infty$ ($S_4 \neq 0$, infinite tower) on any
17984:$\kappa \neq 0$ primary line. The value $d_{\mathrm{alg}} = 3$
17988:\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
17997: d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
18002: $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
18003:\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
18013:\item no value $d_{\mathrm{alg}} = 3$
 succeeded in 50ms:

The two arguments identify the same structural constraint:
$d_{\mathrm{alg}} \in \{0, 1\}$ (finite tower, $S_4 = 0$) or
$d_{\mathrm{alg}} = \infty$ ($S_4 \neq 0$, infinite tower) on any
$\kappa \neq 0$ primary line. The value $d_{\mathrm{alg}} = 3$
falls in neither class.
\end{proof}

\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
\label{prop:depth-gap-trichotomy}
\ClaimStatusProvedHere
\index{algebraic depth!gap theorem|textbf}
\index{shadow depth!forbidden values}
\index{depth classification!algebraic depth gap}
Let $\cA$ be a chirally Koszul algebra in the standard landscape.
Then the algebraic depth satisfies
\begin{equation}\label{eq:depth-gap}
 d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
\end{equation}
More precisely:
exec
/bin/zsh -lc 'rg -nF "d_{alg}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Investigating classification definitions**

I'm trying to make sense of a classification definition that mentions finite depths of d≥5 realized by lattices. I wonder if that's referring to total depth as d = 1 + d_arith + d_alg. I need to check around line 19600. There's also a tricky sentence around line 16909 that states finite depths d≥5 but not d_alg. Maybe I should look closer around line 17110 to clarify my understanding.
exec
/bin/zsh -lc "sed -n '19620,19690p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17100,17220p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
transformation.
\end{remark}

\begin{example}[Shadow depth of all computed families]
\label{ex:shadow-depth-all-families}
\index{shadow depth!computed families}
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{llcccl}
\toprule
\emph{Family} &
\emph{Class} &
$d$ &
$d_{\mathrm{alg}}$ &
$\Delta$ &
\emph{Reference} \\
\midrule
Heisenberg $\cH_k$ &
 $\mathbf{G}$ & $2$ & $0$ & $0$ &
 succeeded in 52ms:
on~$\cM_{1,1}$; each eigenform contributes one $L$-function and one
critical line of the constrained Epstein zeta~$\varepsilon^c_s$
(Chapter~\ref{chap:arithmetic-shadows}).
The \emph{homotopy-theoretic component} $d_{\mathrm{alg}}$ measures
the formal non-formality depth of the $A_\infty$-structure on bar
cohomology: how far the transferred products~$m_n$ extend before
vanishing. For Virasoro on the primary line, $m_n(\bar{T},\dotsc,
\bar{T}) = S_n(c)\cdot\bar{T}$, and the shadow
coefficients~$S_r$ \emph{are} the $A_\infty$ products, the
Sullivan minimal model of~$\gAmod[\mathrm{Vir}_c]$.

For lattice vertex algebras, $d_{\mathrm{alg}} = 0$: the shadow
tower is purely arithmetic, and the depth equals
$3 + \dim S_{r/2}$
(\S\ref{sec:higher-depths}).
For Virasoro minimal models ($c < 1$), $d_{\mathrm{arith}}$ is
finite but $d_{\mathrm{alg}} = \infty$: the infinite shadow obstruction tower
detects the \emph{algebra itself}, the self-referential OPE
$T \in T_{(1)}T$, independently of which representations appear in
the partition function.
exec
/bin/zsh -lc "sed -n '4218,4238p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "ordered ambient algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:modular-characteristic}(iii),
Theorem~\ref{thm:genus-universality}(ii)).
\end{proof}

\begin{remark}[Scope of MC2 in this chapter]
\index{MC2!coinvariant scope}
Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
statement: its target dg~Lie algebra is
$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
The ordered lift
$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
therefore incorrect; the ordered theorem is
Theorem~\ref{thm:e1-mc-element}.
\end{remark}

% ========================================================
 succeeded in 51ms:
31996:\index{E1 algebra@$E_1$-algebra!ordered ambient algebra}
exec
/bin/zsh -lc 'rg -nF "ordered modular" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "coinvariant/symmetric" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3813:In this chapter, it is the coinvariant/symmetric MC2 statement; the
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"g\\"'^'"\\{.*E_1|MC\\(\\{\\\\gAmod\\}\\"'^'"\\{E_1\\}\\)|ordered lift|e1-mc-element|modular convolution\" chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/*e1* chapters/theory/*ordered* appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:e1" chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:g\^\{.*E_1|MC\(\{\gAmod\}\^\{E_1\}\)|ordered lift|e1-mc-element|modular convolution)
                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/ordered_associative_chiral_kd.tex:9023:Definition~\ref{def:e1-chiral}. The functor $\alpha$
exec
/bin/zsh -lc 'rg -nF "gAmod" chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -nF \"e1-mc-element\" -g '*.tex' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF \"ordered lift\" -g '*.tex' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "g''^{'"\\mathrm{amb},E_1}\" -g '*.tex' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}
chapters/theory/e1_modular_koszul.tex:363: is Theorem~\textup{\ref{thm:e1-mc-element}}, equation
chapters/theory/e1_modular_koszul.tex:1375:(Theorem~\ref{thm:e1-mc-element}).
chapters/theory/higher_genus_modular_koszul.tex:3814:ordered $E_1$ lift is Theorem~\ref{thm:e1-mc-element} in
chapters/theory/higher_genus_modular_koszul.tex:4229:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
chapters/theory/higher_genus_modular_koszul.tex:4234:Theorem~\ref{thm:e1-mc-element}.
chapters/theory/en_koszul_duality.tex:6802: but Theorem~\ref{thm:e1-mc-element} gives
chapters/theory/introduction.tex:392:(Theorem~\ref{thm:e1-mc-element}); since
chapters/theory/introduction.tex:875:\textup{(}Theorem~\textup{\ref{thm:e1-mc-element}}\textup{)}
chapters/theory/introduction.tex:1263:(Theorem~\ref{thm:e1-mc-element}):
chapters/theory/introduction.tex:1367:(Theorem~\ref{thm:e1-mc-element}).
chapters/theory/introduction.tex:2067:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & coinvariant bar-intrinsic MC2 (Thm~\ref{thm:mc2-bar-intrinsic}); ordered lift (Thm~\ref{thm:e1-mc-element}) \\[2pt]
chapters/theory/introduction.tex:2084:\textup{(}Theorem~\ref{thm:e1-mc-element}\textup{)}, and averaging
chapters/connections/concordance.tex:106:\textup{(}Theorem~\ref{thm:e1-mc-element}\textup{)},
chapters/connections/concordance.tex:3348: Theorem~\ref{thm:e1-mc-element}. \\
 succeeded in 50ms:
chapters/connections/concordance.tex:103:The ordered lift
chapters/connections/concordance.tex:3345: $\gAmod$; the ordered lift
chapters/theory/bar_construction.tex:432:$\Eone$-ordered lift of the BD symmetric factorization coalgebra, with
chapters/theory/introduction.tex:2067:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & coinvariant bar-intrinsic MC2 (Thm~\ref{thm:mc2-bar-intrinsic}); ordered lift (Thm~\ref{thm:e1-mc-element}) \\[2pt]
chapters/theory/higher_genus_modular_koszul.tex:4227:The ordered lift
chapters/theory/en_koszul_duality.tex:6799: associator-free. The ordered lift retains the full $\GRT_1$-torsor of
chapters/theory/en_koszul_duality.tex:6806: the chosen ordered lift. Proposition~\ref{prop:shadow-gc2-bridge} is a
 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -nF "g''^{E_1}" -g '"'*.tex' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF \"gAmod\" -g '*.tex' chapters appendices | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/e1_modular_koszul.tex:30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
chapters/theory/e1_modular_koszul.tex:2185:& $Q_g^{E_1} + Q_g^{!,E_1}
 succeeded in 51ms:
appendices/nonlinear_modular_shadows.tex:17:$\Theta_\cA \in \MC(\gAmod)$
appendices/nonlinear_modular_shadows.tex:99:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
appendices/nonlinear_modular_shadows.tex:113:\index{g_A^mod@$\gAmod$|see{modular convolution dg Lie algebra}}%
appendices/nonlinear_modular_shadows.tex:122: \gAmod
appendices/nonlinear_modular_shadows.tex:133: $d_{\partial}\colon \gAmod \to \gAmod$
appendices/nonlinear_modular_shadows.tex:140: \gAmod \otimes \gAmod \to \gAmod$
appendices/nonlinear_modular_shadows.tex:143: $g$ in the $(g_2,n_2)$-component of~$\gAmod$, the bracket
appendices/nonlinear_modular_shadows.tex:151:By Theorem~\ref{thm:operadic-homotopy-convolution}, $\gAmod$ is the
appendices/nonlinear_modular_shadows.tex:159:The modular convolution algebra $\gAmod$ carries a natural modular
appendices/nonlinear_modular_shadows.tex:183:$\Theta_{\cA} \in \mathrm{MC}(\gAmod)$ satisfying
appendices/nonlinear_modular_shadows.tex:205:Maurer--Cartan equation~\eqref{eq:nms-mc-equation} in~$\gAmod$.
appendices/nonlinear_modular_shadows.tex:218:genus-$0$ part of the modular convolution algebra~$\gAmod$:
appendices/nonlinear_modular_shadows.tex:223: classical Lie bracket of~$\gAmod$.
appendices/nonlinear_modular_shadows.tex:245:The degree filtration $F^r\gAmod$ on the modular convolution
appendices/nonlinear_modular_shadows.tex:250:(Theorem~\ref{thm:nms-mc-principle}) to $F^{\leq r}\gAmod$.
appendices/nonlinear_modular_shadows.tex:256:lives in $H^2(F^3\gAmod/F^4\gAmod, d_2)$,
appendices/nonlinear_modular_shadows.tex:266:$H^2(F^4\gAmod/F^5\gAmod, d_2)$
appendices/nonlinear_modular_shadows.tex:309:$H^2(F^{r+1}\gAmod/F^{r+2}\gAmod, d_2)$
appendices/nonlinear_modular_shadows.tex:384:Stratify $\gAmod$ by genus and partition the boundary strata of
appendices/nonlinear_modular_shadows.tex:430:is the filtration of~$\gAmod$ by degree: each shadow is the

thinking
**Searching for definitions**

I’m looking into “e1_modular_koszul” to find some definitions. It might be helpful to cite the exact label in the fix. I plan to open the early lines, probably around lines 1 to 60, and check out theorem 291 too. It seems like focusing on those specific parts could help make everything clearer! Let’s see what I can unearth when I dive into those sections.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,340p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
%% ════════════════════════════════════════════════════════════════════════
%% E₁ MODULAR KOSZUL DUALITY
%%
%% The ordered (associative) parallel to the commutative modular
%% Koszul theory. Extracted to a standalone chapter so that the
%% E₁/E_∞ parallelism is architecturally visible.
%% ════════════════════════════════════════════════════════════════════════

\chapter{\texorpdfstring{$E_1$}{E1} Modular Koszul Duality}
\label{chap:e1-modular-koszul}

The scalar curvature $\kappa(\cA)$ is a single number: the
$\Sigma_2$-coinvariant of a meromorphic function $r(z)$ that records
the full spectral scattering of the algebra. The cubic shadow
$\mathfrak{C}(\cA)$ is the $\Sigma_3$-coinvariant of the Drinfeld
associator $\Phi_{\mathrm{KZ}}$. At every degree the $E_\infty$
invariant is a scalar projection of an ordered object that carries
strictly more information, and the data killed by the coinvariant
projection is the associative factorization pattern governed by
Stasheff associahedra rather than symmetric groups.
 succeeded in 51ms:
(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
uses the symmetric cooperad $\mathrm{Sym}^c$ obtained from $T^c$ by external
$\Sigma_n$-coinvariants. The dg~Lie structure is inherited from
$F\!\Ass$: $D$ from $D_{F\!\Ass}$, $[-,-]$ from ribbon-graph
composition.
The \emph{averaging map}
\begin{equation}
\label{eq:e1-to-einfty-projection}
\operatorname{av}\colon
{\gAmod}^{E_1}
\;\twoheadrightarrow\;
\gAmod,
\qquad
\operatorname{av}(\phi)(g,n)
\;:=\;
\frac{1}{n!}\sum_{\sigma \in \Sigma_n}
\sigma \cdot
\bigl(\phi(g,n) \circ \iota^{\mathrm{rib}}_{g,n}\bigr)
\end{equation}
takes external $\Sigma_n$-coinvariants after pullback along a choice
exec
/bin/zsh -lc 'rg -nF "label{def:" chapters/theory/e1_modular_koszul.tex | head -n 40' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
74:\label{def:ribbon-modular-operad}
146:\label{def:feynman-transform-ass}
234:\label{def:e1-modular-convolution}
828:\label{def:ordered-ran-space}
851:\label{def:ordered-fact-dmod}
878:\label{def:ordered-chiral-homology}
1201:\label{def:e1-formality-hierarchy}
1356:\label{def:e1-shadow-degree-r}
2601:\label{def:ribbonized-swiss-cheese}%

thinking
**Inspecting definitions for clarity**

I need to fix something and cite `Definition\ref{def:e1-modular-convolution}`. It will be helpful to inspect that definition to know the exact formula. I’ll check around the section of 220-260 in the document. This should give me the information I need to ensure everything is accurate. It feels like a little detail, but I know it can make a significant difference in the work!
exec
/bin/zsh -lc "sed -n '220,260p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Second, $\pi_{\Sigma_n}$ takes external $\Sigma_n$-coinvariants on
the labels of the~$n$ legs; this is well-defined because
$\Sigma_n$ acts on the set of stable graphs by permuting leg labels
and the differential commutes with relabelling. The composite is a
quasi-isomorphism by the standard comparison between ribbon and
commutative modular operads (Getzler--Kapranov \cite{GK98}, Thm.~4.9).
Only the external-label step is used by the averaging map
$\operatorname{av}$ of~\eqref{eq:e1-to-einfty-projection}; the
ribbon-forgetting step is absorbed into the identification of the
target at the Hom-level, where $\operatorname{End}_\cA(n)$ sees only
external legs.
\end{proof}

\begin{definition}[$E_1$ modular convolution dg~Lie algebra]
\label{def:e1-modular-convolution}
\ClaimStatusProvedHere
\index{E1 algebra@$E_1$-algebra!modular convolution|textbf}
\index{modular convolution dg Lie algebra!E1@$E_1$ (ordered)}
Let $\cA$ be a cyclic $E_1$-chiral algebra
(Definition~\ref{def:e1-chiral}).




thinking
**Assessing shadow tower definitions**

I need to check if "shadow tower Theta_A" is formally defined before its use. The early section refers to "shadow obstruction tower" but only provides a definition later. I'm considering whether there’s a definition at line 12533. It's important to look at any usages in the proof before the formal definition to see if the local restatement suffices. The opening lines introduce some concepts but might not define everything adequately. I should also verify if all symbols are properly defined.
thinking
**Defining structure properly**

I need to make precise changes, like inserting a miniature definition block or moving the definitions of "extension tower," "shadow Postnikov tower," and "shadow algebra" right after the introduction. This will allow the proof of properties to come later. At the very least, I should add a formal forward definition in the first section. 

Additionally, early lines define Theta as D-d0, but they refer to \gAmod without a local definition before the formal one, so I need to include a local definition or move it earlier. Also, I should check if the MC equation is defined beforehand because it looks like it’s used before its definition later on.
thinking
**Searching for definitions**

I need to check if there's an earlier formal definition of the Maurer-Cartan element or equation in the file or any imported files. My first step will be to search for "definition" along with "Maurer-Cartan." There's a chance it might not exist in this file, so I should also consider that it could be in another file altogether. It’s really important to ensure everything is properly defined before proceeding!
thinking
**Analyzing class definitions**

I'm looking at the use of class G/L/C/M in the early lines 136-144, noting that the formal definition comes later at line 16855 under `def:shadow-depth-classification`. The theorem at line 18795 only defines G/L/M on the primary line, which means C isn't included there. It seems this early use occurs before the formal definition. I also find the later definition potentially inconsistent, mixing total and algebraic depth. So, I have two findings: the issue of order of definition and a possible contradiction.
exec
/bin/zsh -lc "sed -n '12480,12545p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
\label{def:weight-filtration-tower}
\index{weight filtration!definition|textbf}
Each component of the modular convolution algebra carries a
\emph{tridegree} $(g, r, d)$, where
$g \geq 0$ is the loop genus (genus label on the stable graph),
$r \geq 2$ is the degree (number of external half-edges), and
$d \geq 0$ is the planted-forest depth (codimension of the
log-FM boundary stratum in the sense of
Definition~\ref{def:vol1-rigid-planted-forest-depth-filtration}).
Define the \emph{total weight}
\[
w(g, r, d) \;:=\; 2g - 2 + r + d.
\]
The stability condition $2g - 2 + n > 0$ ensures $w \geq 1$.
The \emph{weight filtration} is the descending filtration
\[
F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
\;:=\;
\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
\;:\; \varphi_{g,r;d} = 0 \;\text{for all}\;
exec
/bin/zsh -lc "sed -n '12545,12630p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\Theta_{\cA}^{\leq 4},\;
\ldots
\end{equation}
where $\Theta_{\cA}^{\leq r}$ is a solution
of the Maurer--Cartan equation in
$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$,
i.e.\ a point of $\mathcal{E}_{\cA}(r)$
(Definition~\ref{def:extension-tower}).
The tower condition is compatibility under the quotient maps:
for every $r \geq 2$, the image of $\Theta_{\cA}^{\leq r+1}$ in
$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$ is
$\Theta_{\cA}^{\leq r}$.
At each level, the \emph{obstruction class}
\begin{equation}
\label{eq:obstruction-class}
o_{r+1}(\cA)
\;:=\;
\bigl(
D_{\cA}\Theta_{\cA}^{\leq r}
+ \tfrac12[\Theta_{\cA}^{\leq r},\Theta_{\cA}^{\leq r}]

thinking
**Searching algebra relationships**

The early lines mention that `gAmod controls the extension tower`, but formally it's defined as `g^{amb}`. I think I need to clarify what "ground" refers to here, as it might be important. Let's explore more about the connections between ambient algebra and `gAmod`. I want to make sure I'm understanding how they relate, which could be significant for my analysis. Let's dive into that!
exec
/bin/zsh -lc 'rg -nF "ambient algebra" chapters/theory/higher_genus_modular_koszul.tex | head -n 40' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
20933: of the ambient algebra.
31432:ambient algebra:
31464:at the full homotopy level the ambient algebra
31482:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31746:The weight filtration on the ambient algebra
31992:\begin{definition}[Ordered ambient algebra]
31995:\index{ambient algebra!ordered variant|textbf}
31996:\index{E1 algebra@$E_1$-algebra!ordered ambient algebra}
32029:on the ambient algebra
exec
/bin/zsh -lc 'rg -nF "modular extension tower" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "g''^{'"\\mathrm{amb}}\" chapters/theory/higher_genus_modular_koszul.tex | head -n 80" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "shadow obstruction tower" chapters/theory/higher_genus_modular_koszul.tex | head -n 40' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12518:The \emph{modular extension tower} of $\cA$ is the inverse system
 succeeded in 51ms:

 succeeded in 50ms:
151: genus-$0$ shadow obstruction tower coincides with the
2234:\text{Thm D, shadow obstruction tower}
2354:\item The shadow obstruction tower
2722:$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
2823:(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
4364:The shadow obstruction tower convergence
4641:\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
5122:shadow obstruction tower
8612:shadow obstruction tower and by the spectral/periodic invariants.
10419:uniform-weight lane; the non-scalar shadow obstruction tower
10449:convolution dg~Lie algebra together with its shadow obstruction tower
11084: The shadow obstruction tower measures the
11356:the shadow obstruction tower ($o^{(r)}_{\mathrm{Vir}}\neq 0$ for all
11452:\item The full shadow obstruction tower
11553:%% algebra, E₁ shadow obstruction tower, and the five main theorems
12441:\subsection{The shadow obstruction tower}
12535:\index{shadow obstruction tower|textbf}
12536:\index{modular characteristic!shadow obstruction tower}
12537:The \emph{shadow obstruction tower} of $\cA$
12585:The shadow obstruction tower is the primary nonlinear object of

thinking
**Considering algebraic searching**

I'm contemplating searching for the term "ambient algebra," but maybe not just with a fixed string. I could try a command like rg -nF "g^{amb}_\cA," or perhaps use something like `\mathfrak{g}^{\mathrm{amb}}_{\cA}`. I’m wondering if it’s best to utilize a fixed definition label for accuracy. There’s a lot to consider!
exec
/bin/zsh -lc "rg -nF \"\\mathfrak{g}"'^{'"\\mathrm{amb}}_{\\cA}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12496:F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
12498:\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
12524:\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
12550:$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$,
12555:$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$ is
12567:H^2\bigl(F^{r+1}\mathfrak{g}^{\mathrm{amb}}_{\cA}/
12568:F^{r+2}\mathfrak{g}^{\mathrm{amb}}_{\cA}\bigr)
31430:\in \operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA})$
31439:\operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA}).
31443:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ by $\Theta_{\cA}$; the genus
31521:\mathfrak{g}^{\mathrm{amb}}_{\cA}
31638: $\mathfrak{g}^{\mathrm{amb}}_{\cA}$
31641: contributes to $F^w\mathfrak{g}^{\mathrm{amb}}_{\cA}$.
31660:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ through the Hom functor.
32030:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ of
32076:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$
32277:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ could use

thinking
**Searching for ambient algebra**

I need to check if the ambient algebra is defined before the extension tower. To do this, I'll search for the label “ambient-modular-complementarity-algebra.” It's important to find the correct definitions and see how they relate to the topic I'm exploring. I’ll make sure to gather accurate information to clarify my understanding, as it's crucial for the task at hand. Let’s see what I can find!
exec
/bin/zsh -lc 'rg -nF "def:ambient-modular-complementarity-algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31516:\label{def:ambient-modular-complementarity-algebra}
31748:Definition~\textup{\ref{def:ambient-modular-complementarity-algebra}}
32031:Definition~\textup{\ref{def:ambient-modular-complementarity-algebra}}
32077:\textup{(}Definition~\textup{\ref{def:ambient-modular-complementarity-algebra})},
exec
/bin/zsh -lc "sed -n '31690,31740p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 where $C$ is the curve and $D_{\mathrm{nodes}}$ is the nodal
 divisor. Here $\cong$ is an isomorphism of dg~algebras: both
 sides have differentials given by edge contraction (algebraic side)
 and codimension increase (tropical side), and the product is
 disjoint union of forests on both sides.
\item The planted-forest depth filtration
 $($\S\textup{\ref{subsec:carrier-algebra}}$)$ corresponds to the
 codimension filtration on the boundary of
 $\operatorname{FM}_n(X|D)$: depth-$k$ forests index
 codimension-$k$ strata. The rubber torus action on grid
 expansions \textup{(\cite{Mok25}, \S2.7.1)} corresponds to our
 planted-forest depth grading.
\end{enumerate}
\end{theorem}

\begin{remark}[Degeneration formula $=$ clutching law]
\label{rem:degeneration-equals-clutching}%
\index{degeneration formula!as clutching law}%
Mok's degeneration formula \cite[Theorem~5.3.4]{Mok25} states that
each irreducible component of the special fibre of

thinking
**Clarifying ambient algebra**

I'm noticing that the ambient algebra is defined at a much later point than the extension tower, which raises questions about the order of definitions. This seems messy. Maybe the earlier mentions of `g^{amb}` around 123 in the carrier-algebra section could shed light, but I need to search for a formal definition or explanation. I should look around section 12390 for anything relevant!
exec
/bin/zsh -lc 'rg -nF "carrier algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31509:\subsection{The carrier algebra}
31763:\subsubsection{Planar planted forests and the ordered carrier algebra}
exec
/bin/zsh -lc "sed -n '12390,12480p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{genus spectral sequence!non-degeneration}
\index{bar spectral sequence!E2 degeneration}
The bar spectral sequence and the genus spectral sequence play
complementary but \emph{distinct} roles. Their conflation leads to
incorrect arguments; we record the precise distinction.

\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{The bar spectral sequence} (also called the PBW
 spectral sequence) arises from the conformal-weight filtration
 within a \emph{fixed} genus. For a Koszul chiral algebra~$\cA$,
 it degenerates at~$E_2$: the associated graded
 $\gr_{\mathrm{wt}} \overline{B}^{\mathrm{ch},(g)}(\cA)$ computes
 the bar cohomology, and Koszulness forces all higher differentials
 to vanish. This is the mechanism by which
 $H^\bullet(\overline{B}^{\mathrm{ch},(g)}(\cA))$ becomes a
 locally free sheaf on~$\overline{\mathcal{M}}_g$
 (Theorem~\ref{thm:primitive-flat-descent}\textup{(i)}).

\item \emph{The genus spectral sequence}
 (Construction~\ref{const:vol1-genus-spectral-sequence}) arises

thinking
**Examining algebra definitions**

I see that there's an informal mention of ambient algebra later, but there's a potential inconsistency between the claimed carrier algebra of the tower (modular convolution g^mod) and the actual formal carrier (ambient algebra g^amb). This could be a serious issue since the user asked if the shadow tower is formally defined. It is, but possibly on a different algebra than initially stated. I should also check if the all-degree limit theorem "recursive-existence" involves ambient or modular algebra. Let’s search around 13323.
exec
/bin/zsh -lc "sed -n '13320,13480p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
weight $N+1$.
\end{construction}

\begin{theorem}[Recursive existence and shadow obstruction tower convergence;
\ClaimStatusProvedHere]
\label{thm:recursive-existence}
\index{recursive existence!proved}
\index{shadow obstruction tower!convergence}
\index{inverse limit!shadow tower}
Let $\cA$ be a modular Koszul chiral algebra.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Recursive lift.}
 All obstruction classes in the extension tower
 $\{\mathcal{E}_{\cA}(N)\}_{N \geq 1}$
 \textup{(}Definition~\textup{\ref{def:extension-tower})}
 vanish: for every $N \geq 1$, the class
 $[\mathfrak{o}_{N+1}] \in
 H^2(F^{N+1}\gAmod / F^{N+2}\gAmod)$ of
 Construction~\textup{\ref{constr:obstruction-recursion}}
exec
/bin/zsh -lc 'rg -nF "thm:mc2-bar-intrinsic" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4600,4680p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2353: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2651:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2708:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2807:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2918:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3831:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3847:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3987:\label{thm:mc2-bar-intrinsic}
4224:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4232:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4325:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4380:Theorem~\ref{thm:mc2-bar-intrinsic}.
4514: Until that comparison is proved, Theorem~\ref{thm:mc2-bar-intrinsic}
4525:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4575:Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
4629:exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
5129:(Theorem~\ref{thm:mc2-bar-intrinsic};
 succeeded in 51ms:
visible shadows of one master object. Two algebras share a
spectral sheet if and only if they share the same quadratic shadow;
the quartic resonance shadow first separates algebras on the same
sheet.
\end{corollary}

\begin{proof}
Each projection is the restriction of
$\Theta_\cA = D_\cA - \dzero$ to the relevant bigraded
component of $\cA^{\mathrm{sh}} =
H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
(Definition~\ref{def:shadow-algebra}):
(i) is the $(r{=}2, g{=}\bullet)$ scalar trace,
(ii) is the $(r{=}2, g{=}\bullet)$ matrix-valued component,
(iii) is $(r{=}4, g{=}0)$,
(iv) is $(r, g{=}\bullet)$ in general.
\end{proof}

\begin{remark}[Non-circular logical foundation]
\label{rem:non-circular-logical-chain}

thinking
**Investigating a theorem**

It looks like I'm thinking about the theorem mc2-bar-intrinsic, which is around 3987. I wonder if it likely uses the \gAmod formal structure? I might need to inspect the lines there for more clarity. It's interesting how these details come into play, and I’m curious about what specific lines could reveal. I just need to take a closer look to dive deeper into this theorem.
exec
/bin/zsh -lc "sed -n '3987,4175p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{thm:mc2-bar-intrinsic}
\index{universal Maurer--Cartan class!bar-intrinsic construction}
\index{MC2!bar-intrinsic proof}
\index{MC2!full generality}
Let $\cA$ be a modular Koszul chiral algebra on a smooth
projective curve~$X$ with non-degenerate invariant form.
Write
$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
for the genus-completed bar differential
\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
with $d_\cA^{(0)} = \dzero$ the genus-$0$ bar differential.
Define the \emph{positive-genus correction}
\begin{equation}\label{eq:theta-bar-intrinsic}
\Theta_\cA
\;:=\;
D_\cA - \dzero
\;=\;
\sum_{g \geq 1} \hbar^g\, d_\cA^{(g)}
\;\in\;
\prod_{g \geq 1}
exec
/bin/zsh -lc 'rg -nF "Defcyc''^{'"\\mathrm{mod}}\" chapters/theory/higher_genus_modular_koszul.tex | head -n 40" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "def:modular-cyclic-deformation-complex" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
25918:(Definition~\ref{def:modular-cyclic-deformation-complex}).
28809:(Definition~\ref{def:modular-cyclic-deformation-complex})
30317: \textup{(}Definition~\textup{\ref{def:modular-cyclic-deformation-complex})}.
 succeeded in 52ms:
78: $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
2361: H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
2722:$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
4610:H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
11373:\item $\Defcyc^{\mathrm{mod}}(\cA)$ is a strict model via the
11448: $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
11464:the homology of the strict model $\Defcyc^{\mathrm{mod}}(\cA)$
11529:The assignment $\cA \mapsto \Defcyc^{\mathrm{mod}}(\cA)$ is
11534:f_+\colon \Defcyc^{\mathrm{mod}}(\cA)
11536:\Defcyc^{\mathrm{mod}}(\cA')
12776:deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$, the strict model
12780:$\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
12800:$\Defcyc^{\mathrm{mod}}(\cA)$, the \emph{shadow algebra} is the
12806:H_\bullet\bigl(\Defcyc^{\mathrm{mod}}(\cA)\bigr)
12809:bracket on~$\Defcyc^{\mathrm{mod}}(\cA)$.
12855:The Lie bracket on $\Defcyc^{\mathrm{mod}}(\cA)$ descends to a
12857:$\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$.
12861:The bracket $[-,-]$ on $\Defcyc^{\mathrm{mod}}(\cA)$ is a chain
12880:H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
12884:$\Defcyc^{\mathrm{mod}}(\cA)$ and any cyclic deformation retract
exec
/bin/zsh -lc "sed -n '5810,5845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar-intrinsic complex $\Defcyc(\cA)$ of
Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
coefficient spaces chosen from
$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
modular-operadic package of
Theorem~\ref{thm:universal-theta}. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the universal Maurer--Cartan problem for $\Theta_{\cA}$ is posed
 on the genus-completed convolution algebra
 $\widehat{L}_W = \prod_{g \geq 0}\Defcyc(\cA)\otimes W_g$, and its
 genus-$g$ equation is a finite sum;
\item extending a partial solution through genus~$g-1$ to genus~$g$ is
 obstructed by a class in
 $H^2(\Defcyc(\cA), l_1) \otimes W_g$;
\item if $H^2(\Defcyc(\cA), l_1) \cong \mathbb{C}$, then the
 genus-$g$ extension problem has a single obstruction channel valued
 in~$W_g$.
\end{enumerate}
\end{proposition}

thinking
**Searching for labels**

I'm trying to define modular cyclic deformation, and I'm wondering if it might be complex or if there’s an external factor to consider. It seems that the specific label I'm looking for may not be present in the file; it might even be missing altogether. The rg only shows references without the label. So, I’ll need to conduct a search for the exact label globally to see if I can find it.
exec
/bin/zsh -lc "rg -nF \"label{def:modular-cyclic-deformation-complex}\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./chapters/theory/chiral_hochschild_koszul.tex:2244:\label{def:modular-cyclic-deformation-complex}

thinking
**Evaluating file references**

I’m thinking about how the file `Defcyc^{mod}` is mentioned before it’s defined in another chapter. There might be a hidden import, but it could be fine if it's cited as a definition. However, the early usage at line 78 doesn’t include a citation, which could be a concern. The user might not focus on this, but I wonder if including those specifics about direct cited dependencies is necessary, especially when assessing shadow algebra. Let's inspect that label.
exec
/bin/zsh -lc "sed -n '2238,2278p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
invariant form.
(Part of the MC2 theorem package; Theorem~\ref{thm:mc2-full-resolution}.)
\end{definition}

\begin{definition}[Modular cyclic deformation complex;
\ClaimStatusProvedHere]
\label{def:modular-cyclic-deformation-complex}
\index{modular cyclic deformation complex|textbf}
\index{cyclic deformation complex!modular extension}
For a chiral algebra~$\cA$ with bar
complex~$\barB(\cA)$, the \emph{modular cyclic deformation complex} is
\begin{equation}\label{eq:modular-cyc-def-complex}
\Defcyc^{\mathrm{mod}}(\cA)
\;:=\;
\prod_{\substack{g,n \\ 2g-2+n>0}}
\operatorname{CoDer}^{\mathrm{cyc}}\!\bigl(
 \barB^{(g,n)}(\cA)
\bigr)[1],
\end{equation}
where $\barB^{(g,n)}(\cA)$ is the genus-$g$, $n$-marked bar complex
codex
I’ve isolated the high-signal defects. The remaining work is line-accurate verification: I’m pulling exact numbered ranges so every finding is anchored to a sentence that actually says the broken thing, and I’m checking each proposed fix against the later chapter content so I don’t overstate or duplicate.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '120,150p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 52ms:
   120	
   121	The tower $\Theta_\cA$ forces three questions.
   122	How deep does it go? What does its depth classify?
   123	What constraint links $\cA$ to its dual $\cA^!$?
   124	\begin{enumerate}[label=\textup{(\Alph*)}]
   125	\item \emph{Algebraicity}
   126	 (Theorem~\ref{thm:riccati-algebraicity}). On any one-dimensional
   127	 primary slice~$L$, the shadow generating function satisfies
   128	 $H(t)^2 = t^4 Q_L(t)$ with $Q_L$ a quadratic polynomial in~$t$
   129	 determined by three invariants $(\kappa, \alpha, S_4)$. The
   130	 discriminant $\Delta := 8\kappa S_4$ forces the tower depth.
   131	 Exactly one of two cases holds
   132	 (Theorem~\ref{thm:single-line-dichotomy}):
   133	
   134	 $\Delta = 0$: the tower terminates.
   135	 If $S_4 = 0$, the tower stops at depth~$2$
   136	 (class~$\mathsf{G}$, Gaussian).
   137	 If $\kappa = 0$, it stops at depth~$3$
   138	 (class~$\mathsf{L}$, Lie).
   139	 Stratum separation produces a single additional class at
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13324,13470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12518,12620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12770,12835p'" in /Users/raeez/chiral-bar-cobar succeeded in 80ms:
 12518	The \emph{modular extension tower} of $\cA$ is the inverse system
 12519	\begin{equation}
 12520	\label{eq:extension-tower}
 12521	\mathcal{E}_{\cA}(N)
 12522	:=
 12523	\operatorname{MC}\bigl(
 12524	\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
 12525	\bigr),
 12526	\qquad N \geq 1.
 12527	\end{equation}
 12528	A full lift is a compatible point of the inverse limit
 12529	$\Theta_{\cA} \in \varprojlim_N \mathcal{E}_{\cA}(N)$.
 12530	\end{definition}
 12531	
 12532	\begin{definition}[Shadow obstruction tower]
 12533	\label{def:shadow-postnikov-tower}
 12534	\ClaimStatusProvedHere
 12535	\index{shadow obstruction tower|textbf}
 12536	\index{modular characteristic!shadow obstruction tower}
 12537	The \emph{shadow obstruction tower} of $\cA$
 succeeded in 86ms:
 13324	\begin{theorem}[Recursive existence and shadow obstruction tower convergence;
 13325	\ClaimStatusProvedHere]
 13326	\label{thm:recursive-existence}
 13327	\index{recursive existence!proved}
 13328	\index{shadow obstruction tower!convergence}
 13329	\index{inverse limit!shadow tower}
 13330	Let $\cA$ be a modular Koszul chiral algebra.
 13331	\begin{enumerate}[label=\textup{(\roman*)}]
 13332	\item \emph{Recursive lift.}
 13333	 All obstruction classes in the extension tower
 13334	 $\{\mathcal{E}_{\cA}(N)\}_{N \geq 1}$
 13335	 \textup{(}Definition~\textup{\ref{def:extension-tower})}
 13336	 vanish: for every $N \geq 1$, the class
 13337	 $[\mathfrak{o}_{N+1}] \in
 13338	 H^2(F^{N+1}\gAmod / F^{N+2}\gAmod)$ of
 13339	 Construction~\textup{\ref{constr:obstruction-recursion}}
 13340	 is zero.
 13341	\item \emph{Convergence.}
 13342	 The inverse limit
 13343	 $\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$
 succeeded in 94ms:
 12770	
 12771	The shadow obstruction tower defines $\Theta_\cA$ as an inverse limit
 12772	of truncated MC elements. Each truncation $\Theta_\cA^{\leq r}$
 12773	lives in the quotient $\gAmod / F^{r+1}$, an infinite-dimensional
 12774	dg~Lie algebra. To extract finite-dimensional invariants from this
 12775	structure requires passing to cohomology. The modular cyclic
 12776	deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$, the strict model
 12777	of $\Definfmod(\cA)$
 12778	(Remark~\ref{rem:modular-cyc-strictification}), carries an $L_\infty$
 12779	bracket; the \emph{shadow algebra}
 12780	$\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
 12781	the cohomology with its descended graded Lie bracket.
 12782	
 12783	The shadow algebra does two things that the tower alone does not.
 12784	First, it decomposes the MC element $\Theta_\cA$ into components
 12785	graded by degree and genus, so that each named shadow ($\kappa$,
 12786	$\mathfrak{C}$, $\mathfrak{Q}$) is a projection to a specific
 12787	bigraded component. Second, the descended Lie bracket on
 12788	$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
 12789	$o_{r+1}(\cA)$ is a bracket of shadows at degrees~$\leq r$,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3785,3845p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10456,10515p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31512,31540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4224,4235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11022,11080p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3785	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3786	\label{thm:universal-theta}
  3787	\index{universal Maurer--Cartan class|textbf}
  3788	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3789	projective curve~$X$ with non-degenerate invariant form,
  3790	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3791	universal Maurer--Cartan class
  3792	\[
  3793	\Theta_{\cA} \in
  3794	\operatorname{MC}\!\bigl(
  3795	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3796	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3797	\bigr)
  3798	\]
  3799	such that:
  3800	\begin{enumerate}[label=\textup{(\roman*)}]
  3801	\item the genus-$1$ component of its scalar trace is
  3802	 $\kappa(\cA)\lambda_1$
  3803	 \textup{(}g=1 only; ALL-WEIGHT at g=1 is unconditional\textup{)}; on the proved uniform-weight lane,
  3804	 the full scalar trace is
 succeeded in 50ms:
 10456	constructed from the genus-completed bar differential
 10457	(Theorem~\ref{thm:mc2-bar-intrinsic}).
 10458	
 10459	\subsection{The modular convolution dg~Lie algebra}
 10460	\label{subsec:modular-convolution-algebra}
 10461	\index{modular convolution dg Lie algebra|textbf}
 10462	
 10463	\begin{definition}[Modular convolution dg~Lie algebra]
 10464	\label{def:modular-convolution-dg-lie}
 10465	Let $\cA$ be a cyclic chiral algebra on a smooth projective curve~$X$.
 10466	The following dg~Lie algebra is the strict model of the modular
 10467	quantum $L_\infty$-algebra of
 10468	Theorem~\ref{thm:modular-homotopy-convolution}.
 10469	The \emph{modular convolution dg~Lie algebra} is
 10470	\begin{equation}
 10471	\label{eq:modular-convolution}
 10472	\mathfrak{g}_{\cA}^{\mathrm{mod}}
 10473	\;:=\;
 10474	\prod_{\substack{g,n \\ 2g-2+n > 0}}
 10475	\operatorname{Hom}_{\Sigma_n}\!\bigl(
 succeeded in 50ms:
 11022	\begin{remark}[The two Maurer--Cartan equations]
 11023	\label{rem:two-mc-equations}
 11024	\index{Maurer--Cartan equation!strict vs $L_\infty$}
 11025	The universal MC element $\Theta_\cA$ satisfies two forms of the
 11026	Maurer--Cartan equation, one in each layer of the two-level
 11027	convention (Remark~\ref{rem:two-level-convention}).
 11028	
 11029	\emph{Strict form.} In the dg~Lie model
 11030	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
 11031	(Definition~\ref{def:modular-convolution-dg-lie}):
 11032	\begin{equation}\label{eq:strict-mc}
 11033	D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0,
 11034	\end{equation}
 11035	where $D = \ell_1^{(0)}$ and $[-,-] = \ell_2^{(0)}$ are the only
 11036	nonvanishing operations. This is a polynomial equation of degree~$2$
 11037	in the degree-$1$ component.
 11038	
 11039	\emph{$L_\infty$ form.} In the quantum $L_\infty$-algebra
 11040	$\Definfmod(\cA)$
 11041	(Theorem~\ref{thm:modular-homotopy-convolution}),
 succeeded in 52ms:
  4224	Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
  4225	statement: its target dg~Lie algebra is
  4226	$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
  4227	The ordered lift
  4228	$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
  4229	\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
  4230	Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
  4231	$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
  4232	Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
  4233	therefore incorrect; the ordered theorem is
  4234	Theorem~\ref{thm:e1-mc-element}.
  4235	\end{remark}
 succeeded in 52ms:
 31512	The graph sum~\eqref{eq:modular-bar-hamiltonian} lives in a specific
 31513	graded vector space.
 31514	
 31515	\begin{definition}[Ambient modular complementarity algebra]
 31516	\label{def:ambient-modular-complementarity-algebra}
 31517	The \emph{carrier} for the modular bar--Hamiltonian is the filtered
 31518	completed graded vector space
 31519	\begin{equation}
 31520	\label{eq:ambient-modular-complementarity-algebra}
 31521	\mathfrak{g}^{\mathrm{amb}}_{\cA}
 31522	:=
 31523	\bigl(L_{\cA} \oplus K_{\cA} \oplus L_{\cA^!}\bigr)
 31524	\widehat\otimes \mathbb{G}_{\mathrm{st}}
 31525	\widehat\otimes \mathbb{G}_{\mathrm{pf}},
 31526	\end{equation}
 31527	where $L_{\cA} := \operatorname{Def}_{\mathrm{cyc}}(\cA)$,
 31528	$K_{\cA} := (\cA^!\widehat\otimes\cA)[1]$,
 31529	$\mathbb{G}_{\mathrm{st}}$ is the completed stable-graph coefficient
 31530	algebra (connected stable graphs with genus/leg labels), and
 31531	$\mathbb{G}_{\mathrm{pf}}$ is the planted-forest coefficient algebra
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17160,17220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16855,16918p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '19620,19645p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16855	(Theorem~\ref{thm:single-line-dichotomy}).
 16856	
 16857	The tree count at degree~$7$ for the stable-graph route is
 16858	$(2 \cdot 8 - 5)!! = 11!! = 10395$: this is the number of
 16859	trivalent trees with $8$ external legs, which are the
 16860	fully resolved genus-$0$ stable graphs contributing to the
 16861	bracket $\ell_7^{(0)}$. The agreement with the HPL
 16862	route ($C_6 = 132$ planar trees) and the Feynman transform
 16863	route ($C_7 = 429$ binary trees on $8$ leaves) is a
 16864	consequence of the universal property
 16865	(Theorem~\ref{thm:shadow-formality-identification},
 16866	Step~$3$).
 16867	\end{proof}
 16868	
 16869	\begin{definition}[Shadow depth classification]
 16870	\label{def:shadow-depth-classification}
 16871	\ClaimStatusProvedHere
 16872	\index{shadow depth|textbf}
 16873	\index{shadow depth!classification}
 16874	\index{shadow obstruction tower!depth classification}
 succeeded in 51ms:
 17160	 $\mathbf{G}$ & $4$ & $0$ & $0$ &
 17161	 Prop~\ref{prop:leech-epstein} \\
 17162	Rank-$48$ &
 17163	 $\mathbf{G}$ & $5$ & $0$ & $0$ &
 17164	 \S\ref{sec:higher-depths} \\
 17165	Rank-$72$ &
 17166	 $\mathbf{G}$ & $6$ & $0$ & $0$ &
 17167	 \S\ref{sec:higher-depths} \\
 17168	\bottomrule
 17169	\multicolumn{6}{l}{\textsuperscript{$\ast$}%
 17170	 Stratum-separated global family:
 17171	 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 17172	 $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
 17173	 The charged quartic lies off the $T$-line, so the single-line
 17174	 discriminant is not the class-$\mathbf{C}$ witness.}
 17175	\end{tabular}
 17176	\end{center}
 17177	\end{example}
 17178	
 17179	\begin{theorem}[Shadow archetype classification]
 succeeded in 52ms:
 19620	are purely arithmetic: they arise from $d_{\mathrm{arith}}$
 19621	(Hecke eigenforms from the partition function on~$\cM_{1,1}$,
 19622	Chapter~\ref{chap:arithmetic-shadows}), not from the
 19623	$A_\infty$ structure.
 19624	From the shadow metric perspective, the contact class lies outside the single-line framework: the quartic data lives on a charged stratum where $\kappa = 0$, and the shadow metric (Definition~\ref{def:shadow-metric}) requires $\kappa \neq 0$.
 19625	\end{remark}
 19626	
 19627	\begin{remark}[Arithmetic and homotopy-theoretic content of the shadow depth]
 19628	\label{rem:depth-arith-vs-homotopy}
 19629	\index{shadow depth!arithmetic component}
 19630	\index{shadow depth!homotopy-theoretic component}
 19631	The shadow depth carries two independent types of information
 19632	(Theorem~\ref{thm:depth-decomposition}).
 19633	The \emph{arithmetic component} $d_{\mathrm{arith}}$ counts the
 19634	Hecke eigenforms in the partition function's spectral decomposition
 19635	on~$\cM_{1,1}$; each eigenform contributes one $L$-function and one
 19636	critical line of the constrained Epstein zeta~$\varepsilon^c_s$
 19637	(Chapter~\ref{chap:arithmetic-shadows}).
 19638	The \emph{homotopy-theoretic component} $d_{\mathrm{alg}}$ measures
 19639	the formal non-formality depth of the $A_\infty$-structure on bar
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16918,16925p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16918	 \end{minipage} \\
 16919	\bottomrule
 16920	\end{tabular}
 16921	\end{center}
 16922	These four classes are exhaustive and mutually exclusive
 16923	for the standard families at low rank. At higher rank,
 16924	\emph{finite depths $d \geq 5$} are realized by lattice vertex
 16925	algebras whose theta functions involve cusp forms
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16922,16935p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
 16922	These four classes are exhaustive and mutually exclusive
 16923	for the standard families at low rank. At higher rank,
 16924	\emph{finite depths $d \geq 5$} are realized by lattice vertex
 16925	algebras whose theta functions involve cusp forms
 16926	(Chapter~\ref{chap:arithmetic-shadows},
 16927	\S\ref{sec:higher-depths}): depth~$d$ requires a lattice
 16928	of rank~$r$ with $\dim S_{r/2}(\Gamma) \geq d-3$, and
 16929	each independent cusp form contributes one critical line
 16930	of the constrained Epstein zeta. Even unimodular lattices
 16931	of ranks $48, 72, 96, \dotsc$ achieve depths
 16932	$5, 6, 7,\dotsc$\,, with the depth growing as the
 16933	number of cusp forms in $M_{r/2}$ grows. The four classes
 16934	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ thus
 16935	form a \emph{coarse} classification; the fine classification

thinking
**Looking into depth decomposition**

I'm thinking I need to continue the work on depth decomposition, possibly by using a formula like `depth = 1 + d_arith + d_alg`. I should check out the theorem related to depth decomposition lines, as that could help me fix any issues I’m encountering. There's definitely a path to explore here, so I’ll get started on searching for that specific information!
exec
/bin/zsh -lc 'rg -nF "thm:depth-decomposition" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
17158: Theorem~\ref{thm:depth-decomposition}):}} \\
19455:${}^{**}$\,Arithmetic depth from cusp forms: $d_{\mathrm{arith}} = 1$, $d_{\mathrm{alg}} = 0$ (Theorem~\ref{thm:depth-decomposition}).\\
19619:(Theorem~\ref{thm:depth-decomposition})
19632:(Theorem~\ref{thm:depth-decomposition}).
19703:Theorem~\ref{thm:depth-decomposition}). Saying ``Virasoro has depth
21488:\textup{(}Theorem~\textup{\ref{thm:depth-decomposition})}
exec
/bin/zsh -lc "sed -n '19445,19610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & $2$ & $\frac{10}{c(5c{+}22)}$ & $\frac{40}{5c{+}22}$
 & (T-line)
 & $\mathbf{M}$: $r_{\max} = \infty$ \\[4pt]
$V_{\mathrm{Leech}}$ & $24$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{F}_4$: $r_{\max} = 4$\;${}^{**}$ \\
\bottomrule
\end{tabular}
\end{center}
\noindent
${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
${}^{**}$\,Arithmetic depth from cusp forms: $d_{\mathrm{arith}} = 1$, $d_{\mathrm{alg}} = 0$ (Theorem~\ref{thm:depth-decomposition}).\\
For $\mathcal{W}_N$ ($N \geq 3$), the $T$-line data equals the Virasoro data (autonomous, Remark~\ref{rem:w3-multi-channel-tower}); the full rank-$(N{-}1)$ shadow metric is multi-channel with non-autonomy controlled by the propagator variance (Proposition~\ref{prop:propagator-variance}).
\end{example}

\begin{corollary}[The discriminant atlas]
\label{cor:discriminant-atlas}
\ClaimStatusProvedHere
\index{discriminant atlas|textbf}
\index{critical discriminant!atlas|textbf}
\index{critical discriminant!Virasoro closed form}

thinking
**Providing coding guidance**

The user is asking for a specific fix in the code, so I should direct them to replace line 12577 with `\Theta_{\cA}^{\le 2} = \kappa(\cA)\,\eta\otimes\Lambda` and reference the relevant theorem. I’ll need to locate the exact line that contains the correctly typed formula, specifically searching around line 30146 for the context. This way, I can ensure I’m providing clear and accurate direction for the user!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30120,30155p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30120	is the evaluation of the degree-$2$ shadow
 30121	$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 30122	\textup{(}where $\eta$ is the cyclic pairing and $\Lambda$ the
 30123	modular graph class\textup{)} against the conformal
 30124	deformation~$\sigma$.
 30125	
 30126	\item The coefficient $\kappa/(6\pi)$ involves the modular
 30127	characteristic, \emph{not} the central charge: $\kappa/(6\pi)
 30128	\neq c/(6\pi)$ in general. The classical Polyakov coefficient
 30129	$1/(6\pi)$ for a single scalar field arises only for the
 30130	Heisenberg algebra at level $\kappa = 1$, where
 30131	$\kappa = c = 1$.
 30132	
 30133	\item The integrand $|\nabla\sigma|^2 + R_{g_0}\,\sigma$ is the
 30134	Liouville action functional $S_{\mathrm{Liou}}[\sigma; g_0]$.
 30135	It is the unique local, conformally covariant, scalar density
 30136	of weight~$2$ on~$\Sigma_g$, the Euler density integrated
 30137	against~$\sigma$. Its role in~\eqref{eq:polyakov-formula}
 30138	is forced by conformal covariance: the shadow extraction
 30139	map $\pi_{2,g}$
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18795,18828p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 18795	The shadow coefficients exhibit \emph{approximate alternation}:
 18796	$\operatorname{sgn}(S_r(c)) = (-1)^r$ for
 18797	$4 \leq r < r_*(c)$, where
 18798	$r_*(c) \approx \pi/|\pi - \arg(t_0)|$
 18799	and $t_0$ is the nearest complex zero of~$Q_L$.
 18800	The alternation arises from the binomial expansion of
 18801	$\sqrt{Q_L}$ around the Gaussian envelope; it breaks when
 18802	$\cos(r \cdot \arg(t_0))$ changes sign.
 18803	For $\mathrm{Vir}_{13}$: $r_* = 27$;
 18804	for $c = 1$: $r_* = 17$.
 18805	As $c \to \infty$: $\arg(t_0) \to \pi$ and
 18806	$r_* \to \infty$ (exact alternation in the semiclassical limit).
 18807	\end{remark}
 18808	
 18809	\begin{theorem}[Single-line dichotomy; \ClaimStatusProvedHere]
 18810	\label{thm:single-line-dichotomy}
 18811	\index{single-line dichotomy|textbf}
 18812	\index{shadow obstruction tower!single-line dichotomy}
 18813	\index{shadow depth!pump mechanism}
 18814	Let $L$, $S_r$, $\alpha$, $\Delta$, $Q_L$ be as above.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18828,18842p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 18828	
 18829	\item \emph{$\Delta \neq 0$
 18830	 \textup{(}class~$\mathbf{M}$\textup{)}.}\enspace
 18831	 $Q_L$ is irreducible over $k(c)$; $\sqrt{Q_L}$ is irrational;
 18832	 $S_r \neq 0$ for all $r \geq 4$ (generically):
 18833	 $r_{\max} = \infty$.
 18834	\end{enumerate}
 18835	
 18836	\noindent
 18837	\emph{Universal factorization.}\enspace
 18838	For every $r \geq 4$,
 18839	\begin{equation}\label{eq:universal-factorization}
 18840	 S_r \;=\; \Delta \cdot R_r,
 18841	 \qquad
 18842	 R_r \in \mathbb{Q}(\alpha, \kappa, S_4).

thinking
**Considering algebra definitions and references**

I need to come up with a line for defining ambient algebra and possibly extend the tower I mentioned earlier. There's a potential finding about shadow algebra that references Defcyc^mod, which isn't defined locally. Since the user asked for something exhaustive, I could include either medium or low as possibilities. I'll need to look closely at line 12776, which refers to `Remark\ref{rem:modular-cyc-strictification}` for additional context or structure.
exec
/bin/zsh -lc 'rg -nF "rem:modular-cyc-strictification" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12778:(Remark~\ref{rem:modular-cyc-strictification}), carries an $L_\infty$
exec
/bin/zsh -lc "rg -nF \"label{rem:modular-cyc-strictification}\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./chapters/theory/chiral_hochschild_koszul.tex:2286:\label{rem:modular-cyc-strictification}
exec
/bin/zsh -lc "rg -nF \"label{thm:modular-homotopy-convolution}\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./chapters/theory/higher_genus_modular_koszul.tex:11223:\label{thm:modular-homotopy-convolution}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '172,182p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   172	(class~$\mathsf{G}$, formal, quadratic)
   173	via formal-disk restriction, but the embedding is not an
   174	equivalence: the deformation retract to a point is additional
   175	data, and configuration-space geometry on curves is richer.
   176	Theorems~(A), (B), and (C)
   177	have no classical antecedent. The Drinfeld--Kohno bridge
   178	(Construction~\ref{constr:dk-shadow-projections};
   179	Proposition~\ref{prop:e1-shadow-r-matrix}) recovers the classical
   180	$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
   181	shadow of the $E_1$-framed MC element.
   182	The genus-$0$ projection of the shadow connection gives the

thinking
**Revising theorem presentation**

I realize the theorem ends up providing just G/L/M, while class C is global and introduced in a different context. I think I should rewrite that paragraph with separate citations and clarify or incorporate a definition. That seems like it could neatly cover both aspects. Plus, it might be helpful to add one finding related to E1 algebra that isn’t defined locally. These adjustments should enhance clarity!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4060,4088p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4060	 of Theorem~\ref{thm:bar-modular-operad}(i)--(ii) in
  4061	 Chapter~\ref{chap:bar-cobar-adjunction}: the collection
  4062	 $\{\barB^{(g,n)}(\cA)\}$ is an algebra over the Feynman
  4063	 transform~$\mathsf{F}\mathrm{Com}$, with composition maps
  4064	 $\circ_\Gamma$ for every stable graph~$\Gamma$ of
  4065	 type~$(g,n)$ given by iterated edge contraction against
  4066	 the propagator~$P_\cA$.
  4067	\item \emph{$D_\cA^2 = 0$.}
  4068	 This is Theorem~\ref{thm:bar-modular-operad}(iii), itself
  4069	 proved via Theorem~\ref{thm:prism-higher-genus}:
  4070	 the bar differential satisfies $d_{\mathrm{full}}^2 = 0$
  4071	 because each codimension-$2$ boundary stratum of
  4072	 $\overline{\cM}_{g,n}$ appears with opposite signs from
  4073	 the two codimension-$1$ strata containing it
  4074	 (Lemma~\ref{lem:stable-graph-d-squared}).
  4075	 At the convolution-algebra level, this translates to
  4076	 $D^2 = 0$ on $\gAmod$
  4077	 (Theorem~\ref{thm:convolution-d-squared-zero}).
  4078	\item \emph{Brackets well-defined.}
  4079	 The graded commutator $[-,-]$ in the coderivation algebra
exec
/bin/zsh -lc "rg -nF \"providecommand{\\gAmod}\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./tmp_standalone_audit/survey_v2_xr.tex:78:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:76:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./tmp_standalone_audit/wrap_survey_track_b_compressed.tex:76:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./tmp_standalone_audit/wrap_survey_track_b_fixed.tex:76:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./appendices/nonlinear_modular_shadows.tex:99:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./tmp_standalone_audit/wrap_survey_track_a_compressed.tex:76:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./chapters/frame/preface_sections2_4_draft.tex:6:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./standalone/survey_track_a_compressed.tex:51:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./standalone/survey_track_b_compressed.tex:51:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./standalone/survey_modular_koszul_duality_v2.tex:76:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./chapters/frame/preface.tex:4:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./standalone/introduction_full_survey.tex:63:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
./chapters/frame/preface_section1_draft.tex:6:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./chapters/frame/preface_section1_v2.tex:5:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./chapters/frame/preface_sections5_9_draft.tex:6:\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
./standalone/survey_modular_koszul_duality.tex:63:\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}



thinking
**Inspecting references and definitions**

I need to check if line 12577 is using `Theorem D` correctly instead of just a theorem label. There's also a potential issue with a forward reference to `Definition weight filtration` in line 12496, which uses `\mathfrak g^{amb}` before its definition. It could be worth mentioning this mismatch; the chapter seems to define a filtration on an undefined carrier. Additionally, I might need to explore the line about the ambient algebra relation to the bar complex, and consider checking for any unresolved references.
thinking
**Considering exploration vs. manual review**

I think we have enough information to proceed. The developer suggested using the explorer for codebase questions, but I've managed manually, which might be fine. However, it could be beneficial to consider using the explorer for further clarity on foundation inconsistencies since the user asked for exhaustive help. But the guidelines specify not to use subagents unless the user explicitly requests them, so I’ll refrain from that. I also need to look into some potential citation fixes related to `Theorem universal-theta`.
thinking
**Checking class definitions**

I need to verify that classes G, L, C, and M are defined before their usage, not just at line 132 but also at line 172. It's crucial to look closely at lines 16922-16935, as the definition there mixes theorem content and uses a bare `d`. To address this, I should consider splitting the definition for clarity. This might help ensure the classes are properly referenced and defined, maintaining the integrity of the work.
exec
/bin/zsh -lc 'rg -nF "constr:obstruction-recursion" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4565:(Construction~\ref{constr:obstruction-recursion}).
11103:(Construction~\ref{constr:obstruction-recursion}). The $L_\infty$
11894:(Construction~\ref{constr:obstruction-recursion}) factorises by
12258:(Construction~\ref{constr:obstruction-recursion}). The scalar,
12354: (Construction~\ref{constr:obstruction-recursion});
12376:Construction~\ref{constr:obstruction-recursion},
13050:(Construction~\ref{constr:obstruction-recursion})
13303:\label{constr:obstruction-recursion}
13339: Construction~\textup{\ref{constr:obstruction-recursion}}
13411:Construction~\ref{constr:obstruction-recursion} vanishes for
15259:\textup{(}Construction~\textup{\ref{constr:obstruction-recursion}}):
15290:(Construction~\ref{constr:obstruction-recursion}) for a concrete
15571:(Construction~\ref{constr:obstruction-recursion})
15900:recursion (Construction~\ref{constr:obstruction-recursion}):
16877:Construction~\ref{constr:obstruction-recursion}.
25903:(Construction~\ref{constr:obstruction-recursion}).
26465:(Construction~\ref{constr:obstruction-recursion}) rather than
28957:(Construction~\ref{constr:obstruction-recursion}),
31307:(Construction~\ref{constr:obstruction-recursion}).
31399:extension tower (Construction~\ref{constr:obstruction-recursion}).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13290,13323p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 13290	$\operatorname{Sh}_3 = 2$ for all simple types is the statement
 13291	that the soft graviton theorem at order~$1$ is determined by the
 13292	Lie bracket alone, which is the same across all simple types at
 13293	the appropriate normalization of the Killing form. This is the
 13294	cubic counterpart of the binary universality
 13295	$\Delta^{(2)} = K_\fg/2$: the binary shadow is determined by the
 13296	central charge (the Casimir trace), the cubic shadow is determined
 13297	by the structure constants (the Lie bracket), and the quartic
 13298	shadow $\operatorname{Sh}_4$ is the first place where
 13299	the specific representation theory of~$\fg$ enters.
 13300	\end{remark}
 13301	
 13302	\begin{construction}[Obstruction recursion]
 13303	\label{constr:obstruction-recursion}
 13304	Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
 13305	constructed through weight $N$. Its next obstruction is
 13306	\begin{equation}
 13307	\label{eq:next-obstruction}
 13308	\mathfrak{o}_{N+1}
 13309	:=
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12480,12518p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12480	\label{def:weight-filtration-tower}
 12481	\index{weight filtration!definition|textbf}
 12482	Each component of the modular convolution algebra carries a
 12483	\emph{tridegree} $(g, r, d)$, where
 12484	$g \geq 0$ is the loop genus (genus label on the stable graph),
 12485	$r \geq 2$ is the degree (number of external half-edges), and
 12486	$d \geq 0$ is the planted-forest depth (codimension of the
 12487	log-FM boundary stratum in the sense of
 12488	Definition~\ref{def:vol1-rigid-planted-forest-depth-filtration}).
 12489	Define the \emph{total weight}
 12490	\[
 12491	w(g, r, d) \;:=\; 2g - 2 + r + d.
 12492	\]
 12493	The stability condition $2g - 2 + n > 0$ ensures $w \geq 1$.
 12494	The \emph{weight filtration} is the descending filtration
 12495	\[
 12496	F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
 12497	\;:=\;
 12498	\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
 12499	\;:\; \varphi_{g,r;d} = 0 \;\text{for all}\;

thinking
**Inspecting line issues**

I'm thinking I need to inspect the line around 32029, but there's an extension tower that seems to be much earlier in the sequence. That's a significant concern. I should search around that 32029 area and also look into "ambient-d-squared-zero" to gather more information. There's definitely a few elements to consider there, and it's important to clarify what might be going on! Let's figure this out!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32020,32042p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 32020	\]
 32021	\end{definition}
 32022	
 32023	\begin{proposition}[Square-zero property of the ambient differential;
 32024	\ClaimStatusProvedHere]
 32025	\label{prop:coefficient-algebras-well-defined}
 32026	The five-component differential
 32027	$D_{\cA} = d_{\mathrm{int}} + [\tau_{\cA},-] + d_{\mathrm{sew}} +
 32028	d_{\mathrm{pf}} + \hbar\Delta$
 32029	on the ambient algebra
 32030	$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ of
 32031	Definition~\textup{\ref{def:ambient-modular-complementarity-algebra}}
 32032	satisfies $D_{\cA}^2 = 0$.
 32033	\end{proposition}
 32034	
 32035	\begin{proof}
 32036	The diagonal terms are each square-zero:
 32037	\begin{enumerate}[label=\textup{(\roman*)}]
 32038	\item $d_{\mathrm{int}}^2 = 0$: the internal differential on each bar
 32039	 complex is square-zero by construction.
exec
/bin/zsh -lc 'rg -nF "constr:dk-shadow-projections" chapters/theory/higher_genus_modular_koszul.tex && rg -nF "prop:e1-shadow-r-matrix" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
178:(Construction~\ref{constr:dk-shadow-projections};
179:Proposition~\ref{prop:e1-shadow-r-matrix}) recovers the classical
exec
/bin/zsh -lc "rg -nF \"label{constr:dk-shadow-projections}\" -g '*.tex' . && rg -nF \"label{prop:e1-shadow-r-matrix}\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./chapters/examples/yangians_drinfeld_kohno.tex:96:\label{constr:dk-shadow-projections}
./chapters/theory/e1_modular_koszul.tex:767:\label{prop:e1-shadow-r-matrix}
codex
I hit the key second-order failure: this is not just a missing cross-reference. The file alternates between two different carriers for the same tower, `\gAmod` and `\mathfrak g^{amb}_\cA`, and the filtration/grading data do not obviously transport between them. I’m checking whether the chapter actually states the comparison map; if it does not, that becomes the load-bearing defect, not merely the order of presentation.
exec
/bin/zsh -lc 'rg -n "ambient.*gAmod|gAmod.*ambient|filtered quasi-isomorphism|comparison.*ambient|carrier algebra|weight filtration.*gAmod|planted-forest depth" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4111: The weight filtration $F^N\gAmod$
12486:$d \geq 0$ is the planted-forest depth (codimension of the
13355:The weight filtration $F^N\gAmod$
15042:genus~$g$, degree~$r$, and planted-forest depth~$d$.
25934:structure, with planted-forest depth~$d$ as a third, subordinate
31509:\subsection{The carrier algebra}
31695:\item The planted-forest depth filtration
31701: planted-forest depth grading.
31763:\subsubsection{Planar planted forests and the ordered carrier algebra}
32238:\item The planted-forest depth filtration
exec
/bin/zsh -lc "sed -n '31420,31510p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12440,12518p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
and Appendix~\ref{app:nonlinear-modular-shadows}) is the
visible face of the quantum $L_\infty$
structure on $\mathfrak{g}_{\cA}^{\mathrm{mod}}$.
\end{remark}

\begin{proposition}[MC structure principle; \ClaimStatusProvedHere]
\label{prop:chriss-ginzburg-structure}
\index{Chriss--Ginzburg structure principle|textbf}
\index{modular bar--Hamiltonian!as structure map}
The assignment $\cA \mapsto \Theta_{\cA}
\in \operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA})$
is a functor from chiral algebras to Maurer--Cartan moduli of the
ambient algebra:
\begin{equation}
\label{eq:chriss-ginzburg-functor}
\Theta\colon
\{\text{chiral algebras}\}
\longrightarrow
\coprod_{\cA}\,
\operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA}).
 succeeded in 52ms:

\subsection{The shadow obstruction tower}
\label{subsec:shadow-postnikov-tower}

%% DEFICIENCY OPENING: what does the tower structure reveal
%% that individual shadows do not?

The MC element $\Theta_\cA = D_\cA - d_0$ satisfies
$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ by
construction. Its degree-$2$ projection is the scalar
$\kappa(\cA)$; its degree-$3$ projection is the cubic
shadow~$\mathfrak{C}(\cA)$; its degree-$4$ projection is the quartic
resonance class~$\mathfrak{Q}(\cA)$. Each projection is a useful
invariant in isolation. The question is: what structure do the
projections carry \emph{collectively} that none of them carries alone?

The answer is that $\Theta_\cA$ is not a list of invariants but an
inverse-limit element in a filtered pronilpotent Lie algebra, and the
MC equation couples the projections across degrees. The obstruction
class $o_{r+1}(\cA)$ at degree~$r{+}1$ is a Lie bracket of the
exec
/bin/zsh -lc "rg -n \"ambient.*convolution|convolution.*ambient|g\\"'^'"\\{amb\\}.*gAmod|gAmod.*g\\"'^'"\\{amb\\}|carrier.*convolution\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
59:The algebraic carrier of this structure is the modular convolution


thinking
**Exploring audit surface options**

The user asks about fixing the audit surface, so it’s essential to provide two clear options. However, since the prompt requests an exact fix, I should clearly state that. I think I can suggest: "FIX: choose one carrier and enforce it." It seems straightforward! I want to make sure my response is precise and helpful, so I’ll focus on delivering this suggestion clearly to the user.
thinking
**Considering problem formatting**

I'm thinking about how to format references when a problem spans multiple lines. It might help to use the starting line or a few key separated references within the text. For instance, I could format it as `chapters/theory/higher_genus_modular_koszul.tex:12518` and include supporting lines in the problem to clarify the context. I want to make sure this is clear and easy to follow!
Plan update
Finished the targeted foundation audit. I verified the surviving defects against the target file and the directly cited dependency definitions in the E1 and chiral Hochschild chapters.
  ✓ Map the target file: labels, claim blocks, and all occurrences of Theta_A, MC, g^{E1}, g^{mod}, G/L/C/M, and related references
  ✓ Read the relevant target-file sections in context and inspect directly cited dependency definitions/proofs
  ✓ Attack for missing definitions, hidden imports, unresolved references, and unjustified steps; re-verify each surviving finding




thinking
**Evaluating audit format**

I’m thinking about the format, which says `Checked: N | Findings: N`. It seems to suggest a count of audit checkpoints. I could say `Checked: 9 | Findings: 8`, but it feels important to compute based on the specific checkpoints. Since the user asked for a foundation audit, maybe I should stick to the checked foundation surfaces. I could settle on saying I checked 9 load-bearing surfaces, and my final summary would be `Checked: 9 | Findings: 8 | Verdict: FAIL`.
thinking
**Considering format options**

I’m thinking about using markdown bullets that include the file path and line numbers for clarity. I could definitely create clickable links, like `[chapters/theory/higher_genus_modular_koszul.tex](/abs/path:12518)`, but since the user requested a specific format, I need to make sure I stick to that. It’s important that I follow their guidelines closely while providing the required details. I’ll aim to keep it straightforward and aligned with their request!
thinking
**Resolving carrier issues**

I’m dealing with the undefined carrier in the tower proof, and I need to either split or choose one carrier. A straightforward fix involves renaming the current construction to `ambient extension tower` in certain sections, replacing occurrences of `\gAmod` with `\mathfrak g^{amb}_\cA`, and adding a proposition for comparison. I also noticed issues regarding the order of definitions that need addressing. For example, I’ll need to insert a definition before line 39. Let's clarify these points!
thinking
**Clarifying severity labeling**

I need to incorporate the user's severity labeling of `[CRITICAL] [HIGH] [MEDIUM] [LOW]`, which is great. I have to be careful — no guesses or inferences should be presented as facts. I can only state claims from the lines we read. If there's a contradiction, like between specific lines, I'll phrase it correctly. Also, mentioning cross-file fixes with external definitions could be useful. I want to keep it concise, but still informative. A clickable absolute file path might be a good option, though maybe not strictly necessary.
codex
- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex:12518](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12518) — PROBLEM: the tower changes carrier mid-chapter. `Definition~\ref{def:extension-tower}` and `Definition~\ref{def:shadow-postnikov-tower}` put the MC tower in `\mathfrak g^{\mathrm{amb}}_{\cA}/F^{N+1}` at lines 12524, 12550, 12567, but the surrounding prose and `Theorem~\ref{thm:recursive-existence}` switch to `\gAmod/F^{N+1}` at lines 12773 and 13338-13464. The ambient carrier is not even defined until line 31515, and its square-zero differential is only stated at line 32023. As written, the tower has no stable, defined carrier. FIX: choose one carrier and enforce it. The minimal true fix is to split the constructions explicitly:
  `ambient tower`: lines 12480-12593 and 13302-13470 become `F^N\mathfrak g^{\mathrm{amb}}_{\cA}`, `\mathcal E^{\mathrm{amb}}_\cA(N)`, `\Theta^{\le r,\mathrm{amb}}_\cA`;
  `coinvariant tower`: introduce separately after [chapters/theory/higher_genus_modular_koszul.tex:10463](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10463) on `\gAmod`;
  add a comparison proposition after [chapters/theory/higher_genus_modular_koszul.tex:31515](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31515) stating exactly how `\mathfrak g^{\mathrm{amb}}_{\cA}` maps to `\gAmod`. Until that proposition exists, delete claims that a single tower lives in both.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:36](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:36) — PROBLEM: the opening treats `\gAmod` as already defined (`\Theta_\cA \in \gAmod`, weight filtration on `\gAmod`, truncations in `\gAmod`) but the first formal definition of the modular convolution dg Lie algebra is only at lines 10463-10507. The foundation is backwards: the chapter uses the carrier for ~10,000 lines before defining it. FIX: move the subsection beginning at [chapters/theory/higher_genus_modular_koszul.tex:10459](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10459) to the first occurrence of `\gAmod`, or insert there a local recall:
  `\gAmod := \prod_{2g-2+n>0}\Hom_{\Sigma_n}(C_*(\overline{\mathcal M}_{g,n}),\End_\cA(n))`,
  with a forward pointer to Definition~`\ref{def:modular-convolution-dg-lie}`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:39](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:39) — PROBLEM: the chapter invokes “the Maurer--Cartan equation” from the opening and again in the proof of Theorem~`\ref{thm:universal-theta}` at lines 3826-3830, but the first place that distinguishes the strict dg-Lie MC equation from the full quantum `L_\infty` MC equation is the later remark at lines 11022-11047. Until then, the chapter never states which MC notion its proofs are actually using. FIX: insert a short convention immediately after line 43 or immediately before line 3785:
  `Strict MC in \gAmod: D\Theta_\cA + \frac12[\Theta_\cA,\Theta_\cA]=0;`
  `Homotopy MC in \Definfmod(\cA): \sum_{n,g}\frac{\hbar^g}{n!}\ell_n^{(g)}(\Theta_\cA^{\otimes n})=0.`
  Then rewrite Remark~`\ref{rem:two-mc-equations}` as a later explanation, not the first definition.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:180](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:180) — PROBLEM: the file uses the ordered object `\Theta_\cA^{E_1}` and later `\MC((\gAmod)^{E_1})` at lines 3813-3815 and 4227-4229, but this chapter never defines the ordered convolution algebra. The actual carrier lives in another file, [chapters/theory/e1_modular_koszul.tex:234](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:234). That is a hidden import on a load-bearing object. FIX: at the first use add an explicit local scope sentence:
  `Here ({\gAmod})^{E_1}` denotes the ordered modular convolution dg Lie algebra of Definition~`\ref{def:e1-modular-convolution}` in Chapter~`\ref{chap:e1-modular-koszul}`, and `\operatorname{av}\colon ({\gAmod})^{E_1}\to\gAmod` is the averaging map.
  If this chapter is not meant to develop the ordered carrier, state that and forbid uncited use of `\Theta_\cA^{E_1}` before the cross-reference.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:131](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:131) — PROBLEM: the opening says “Exactly one of two cases holds (Theorem~`\ref{thm:single-line-dichotomy}`)” and then lists classes `\mathbf G`, `\mathbf L`, `\mathbf C`, `\mathbf M`. But the theorem later proved at lines 18809-18833 only gives `\mathbf G/\mathbf L/\mathbf M` on a primary line; `\mathbf C` is not part of that dichotomy. It enters separately through the global contact/stratum-separation material and is only formally defined much later at lines 16869ff. FIX: rewrite lines 131-144 as:
  `On a primary line, Theorem~\ref{thm:single-line-dichotomy} yields the three cases \mathbf G, \mathbf L, \mathbf M.`
  `The global contact class \mathbf C is added separately by Theorem~\ref{thm:shadow-archetype-classification} together with Remark~\ref{rem:contact-stratum-separation}.`
  Also add a one-line inline class definition here or move Definition~`\ref{def:shadow-depth-classification}` forward.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:16869](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16869) — PROBLEM: `Definition~\ref{def:shadow-depth-classification}` is not just a definition. After defining `\kappa_d(\cA)=r_{\max}(\cA)`, it switches at lines 16922-16935 to a different, unqualified notion of depth `d`, claiming finite depths `d\ge 5` are realized by lattices. Later the example table marks rank-48 and rank-72 lattices as class `\mathbf G` with `d=5,6` but `d_{\mathrm{alg}}=0` (lines 17162-17167), and the later remark at lines 19631-19640 explicitly separates arithmetic depth from algebraic depth. The definition is mixing two invariants and is therefore not self-consistent. FIX: end the definition at line 16921. Move lines 16922-16935 to a new remark after `Remark~\ref{rem:depth-arith-vs-homotopy}` and rewrite them as:
  `Higher-rank lattice VOAs can have larger total depth d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}} while remaining algebraically class \mathbf G, with d_{\mathrm{alg}}=0 and r_{\max}=2.`
  Do not use bare `d` inside the class definition.

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex:52](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:52) — PROBLEM: the opening and the overview at lines 97-101 put the obstruction class directly in `H^2(\cA^{\mathrm{sh}}_{r+1,0})`, but the formal definition later at lines 12557-12573 first places it in the filtered carrier cohomology and only then passes to the shadow algebra. That is a hidden conflation of the primary obstruction class with its shadow image. FIX: after fixing the carrier, replace the early codomain by
  `H^2(F^{r+1}\mathfrak g_{\text{chosen}}/F^{r+2}\mathfrak g_{\text{chosen}})`
  and add:
  `its image in \cA^{\mathrm{sh}}_{r+1,0} is the degree-(r+1), genus-0 shadow obstruction after Definition~\ref{def:shadow-algebra}.`

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex:12577](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12577) — PROBLEM: `\Theta_{\cA}^{\le 2} = \kappa(\cA)` is type-wrong. The left-hand side is a truncated MC element in a filtered Lie carrier; the right-hand side is a scalar. The chapter itself later gives the correctly typed formula at lines 30121-30123. FIX: replace line 12577 by
  `\Theta_{\cA}^{\le 2} = \kappa(\cA)\,\eta\otimes\Lambda`
  or, if only the projection is intended,
  `\pi_{2,0}(\Theta_{\cA}^{\le 2})=\kappa(\cA)`.
  Do not identify an MC truncation with a bare scalar.

- [LOW] [chapters/theory/higher_genus_modular_koszul.tex:78](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:78) — PROBLEM: `\Defcyc^{\mathrm{mod}}(\cA)` is foundational for the shadow algebra, but this chapter uses it on first appearance with no local definition and no citation. Its definition is external, at [chapters/theory/chiral_hochschild_koszul.tex:2244](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:2244). That is a hidden import at exactly the point where the chapter claims to be laying foundations. FIX: add `(Definition~\ref{def:modular-cyclic-deformation-complex})` after the first occurrence at line 78 and again in `Definition~\ref{def:shadow-algebra}` at lines 12799-12808, or inline a one-line recall of the complex.

## Summary
Checked: 9 | Findings: 9 | Verdict: FAIL
tokens used
196,005
