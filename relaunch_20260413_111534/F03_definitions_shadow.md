# F03_definitions_shadow (685s)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:59-63,11825-11916,30439-30449 — PROBLEM: the chapter changes the carrier object without saying so. The opening says the carrier is `\gAmod`; the shadow-tower section says it is defining a filtration on the “modular convolution algebra” but actually defines `F^\bullet` on `\mathfrak{g}^{\mathrm{amb}}_{\cA}`; the carrier `\mathfrak{g}^{\mathrm{amb}}_{\cA}` is only formally defined later at lines 30439-30449. The same definition then sends the obstruction class to `H^2(\cA^{\mathrm{sh}}_{r+1,0})` before the shadow algebra is formally defined at lines 12138-12163. The tower is therefore founded on two undeclared objects and no comparison map between `\gAmod` and `\mathfrak{g}^{\mathrm{amb}}_{\cA}` is stated. FIX: move Definition `ambient-modular-complementarity-algebra` to immediately before line 11832, add an explicit comparison sentence (`\gAmod \hookrightarrow \mathfrak{g}^{\mathrm{amb}}_{\cA}` or `\gAmod = \mathfrak{g}^{\mathrm{amb}}_{\cA}`, whichever is intended), and replace line 11916 by a carrier-internal target such as `H^2(F^{r+1}\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+2}\mathfrak{g}^{\mathrm{amb}}_{\cA})` until the identification with `\cA^{\mathrm{sh}}_{r+1,0}` is proved after Definition~`\ref{def:shadow-algebra}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:180 — PROBLEM: `\Theta_\cA^{E_1}` is invoked as if the ordered carrier were already in scope, but this file does not define `${\gAmod}^{E_1}` or the averaging map there. The local ordered/coinvariant bridge only appears later at lines 3585-3592, and the actual ordered definition is in `chapters/theory/e1_modular_koszul.tex:233-287`. This is a hidden import at the first `E_1`-level use. FIX: insert a local scope paragraph before line 177: define or import `${\gAmod}^{E_1}` and `\operatorname{av}:{\gAmod}^{E_1}\to\gAmod` from Definition~`\ref{def:e1-modular-convolution}`, and explicitly state `\Theta_\cA=\operatorname{av}(\Theta_\cA^{E_1})` before mentioning `\pi_{2,0}(\Theta_\cA^{E_1})`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3359-3372 — PROBLEM: the proof of `thm:universal-theta` derives and uses “the Maurer--Cartan equation” before this chapter has put the strict MC equation on a formal standalone surface. The strict equation is only written later at lines 10396-10408, and the full bar-intrinsic theorem only appears later at lines 3507-3582. The proof is therefore forward-dependent on undeclared formalism. FIX: either move Theorem~`\ref{thm:mc2-bar-intrinsic}` above `thm:universal-theta`, or insert immediately before line 3332 a short definition/lemma package:
  `\begin{definition}[Strict Maurer--Cartan equation] ... D x + \frac12[x,x]=0 ... \end{definition}`
  and
  `\begin{lemma}[Bar-intrinsic MC identity] If D_\cA=\dzero+\Theta_\cA and D_\cA^2=0, then \Theta_\cA satisfies the strict MC equation. \end{lemma}`
  Then change line 3371 to cite that lemma instead of pointing forward.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:4212-4218,4251-4254 — PROBLEM: `thm:bipartite-linfty-tree` and its proof use the shadow classes `\mathsf{G},\mathsf{L},\mathsf{C},\mathsf{M}` as if they were already defined, but the formal depth-class definition is only at lines 16191-16240. There is no local alias, no forward pointer, and the proof relies on those class names in an essential termination argument. FIX: move Definition~`\ref{def:shadow-depth-classification}` above this theorem, or rewrite both the statement and proof with explicit vanishing conditions (`o_3=0`, `o_3\neq0,o_4=0`, `o_4\neq0,o_5=0`, infinitely many nonzero `o_r`) and then add “these are later named classes `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}` in Definition~`\ref{def:shadow-depth-classification}`.”

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:16503-16507,16566-16568 — PROBLEM: `thm:shadow-archetype-classification` cites Definition~`\ref{def:shadow-depth-classification}` but does not use that definition’s notation. The definition at lines 16215-16240 defines `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}`; the theorem opens with `\mathbf{F}_2,\mathbf{F}_3,\mathbf{F}_4,\mathbf{M}`, switches back to `\mathbf{G},\mathbf{L},\mathbf{C}` inside the enumerated items, and later introduces `\mathbf{F}_d` with no local alias. Concordance does record the alias (`G/L/C/M = F_2/F_3/F_4/M`), but this theorem does not. FIX: make the theorem self-contained. Replace lines 16504-16505 by `\mathbf{G}, \mathbf{L}, \mathbf{C}, or \mathbf{M}` and add one sentence after line 16506: “We also write `\mathbf{F}_2:=\mathbf{G}`, `\mathbf{F}_3:=\mathbf{L}`, `\mathbf{F}_4:=\mathbf{C}` when indexing by depth.” Then reserve `\mathbf{F}_d` for genuinely higher finite depths `d\ge 5`.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:2188-2200 — PROBLEM: `thm:three-tier-architecture` states `\Theta_\cA\in\MC(\gAmod)`, the shadow obstruction tower, and the shadow algebra before the file has formally introduced those objects locally (`\Theta_\cA` theorem at 3528, `\gAmod` definition at 9837, tower definition at 11885, shadow algebra definition at 12138). Because this is a theorem environment, not casual roadmap prose, the statement is not self-contained. FIX: either move this theorem below the formal setup, or rewrite each item with inline definitions: `\Theta_\cA:=D_\cA-\dzero`, `\Theta_\cA^{\le r}:=\pi_{\le r}(\Theta_\cA)`, and `\cA^{\mathrm{sh}}:=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))`, followed by explicit forward references to the later formal definitions.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:11921-11925 — PROBLEM: the shadow-tower definition collapses objects of different types. `\Theta_{\cA}^{\le 2}` is a truncated MC element in a quotient Lie algebra, but line 11921 identifies it directly with the scalar `\kappa(\cA)`; the next bullets similarly treat `\Theta_{\cA}^{\le 3}` and `\Theta_{\cA}^{\le 4}` as if they were literally the cubic and quartic classes. No embedding or projection map is stated. FIX: rewrite these bullets as projections, e.g. `\pi_{2,0}(\Theta_{\cA}^{\le 2})=\kappa(\cA)`, `\pi_{3,0}(\Theta_{\cA}^{\le 3})=\mathfrak{C}(\cA)`, `\pi_{4,0}(\Theta_{\cA}^{\le 4})=\mathfrak{Q}(\cA)`, or explicitly define the scalar/class embeddings into the truncated carrier before these identifications.

## Summary
Checked: 4 | Findings: 7 | Verdict: FAIL


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
session id: 019d8648-99b7-7491-8cc5-9ae1b9251b55
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



thinking
**Auditing coding files**

I need to act as a coding agent to audit specific file chapters with critical findings and precise fixes. It’s crucial to ground every claim in the file contents that I read. My approach will involve a thorough check of specified areas, possibly using the deep-beilinson-audit skill. The user wants an audit, not an edit, but I still need to consider reading related files like CLAUDE and the theorem registry if necessary before any significant edits.
thinking
**Following developer instructions**

I need to adhere to the developer's instructions, which emphasize using explorers instead of manual searches. I could deploy explorer agents to inspect the target file and its dependencies. However, the instructions also suggest that I should read the actual file contents myself. The explorer can help gather file references, and then I can examine those files. Ultimately, I need to ground my claims in what I read, so I’ll also look into related definitions and potentially produce an update plan.
thinking
**Planning command usage**

I likely need to use tools like `rg` and `sed` for my task, and I definitely need line numbers for my findings. Browsing the internet isn’t an option, so I’ll probably stick to the terminal instead. I should also use commentary updates to keep track of my progress. For efficiency, it might be helpful to use parallel commands with multi_tool_use.parallel. I’ll begin by updating my commentary to mention the skills I’m using and outline my first step.
codex
Using `deep-beilinson-audit` for an adversarial proof-surface audit. I’m starting by reading the audit skill, then the target file and the local definition surfaces it depends on, so every finding is tied to exact text rather than repo folklore.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Evaluating file exploration tools**

I need to read the required load files first. It might be useful to consider using parallel shell commands for inspection, or maybe I should use the explorer agent since the developer mentioned that for all codebase questions. Spawning an explorer could help locate definitions in the repo. Since the user asked about an audit, I don't need to use subagents, but I think using the explorer for references and definitions makes sense. Let’s proceed with one explorer to find everything needed.
codex
I’ve fixed the audit surface to `chapters/theory/higher_genus_modular_koszul.tex` and I’m now loading the constitutional files plus the target’s dependency surface. In parallel, I’m locating where the key objects (`Theta_A`, `g^{E1}`, `g^{mod}`, G/L/C/M, MC) are defined elsewhere so I can distinguish explicit local definitions from hidden imports.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 53ms:
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
 succeeded in 58ms:
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
collab spawn_agent(call_kEopWVNB6eSOOR8hZtfpbOjn, prompt="Locate the definition surfaces relevant to chapters/theory/higher_genus_modular_koszul.tex. Find exact file paths and li…")
spawn_agent(call_kEopWVNB6eSOOR8hZtfpbOjn, prompt="Locate the definition surfaces relevant to chapters/theory/higher_genus_modular_koszul.tex. Find exact file paths and li…") pending init:
  agent: 019d8649-0f59-7301-9d55-ada4dd196cff
mcp startup: no servers
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theta_A"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2037

CLAUDE.md:5:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
CLAUDE.md:199:1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature).
CLAUDE.md:206:The convolution algebra has two levels: g^{E1}_A (the primitive, carrying the R-matrix) and g^mod_A (the coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in this monograph is its Sigma_n-coinvariant projection.
CLAUDE.md:495:| Theta_A | PROVED | Bar-intrinsic; all-degree inverse limit (thm:recursive-existence) |
CLAUDE.md:532:AP6: Specify genus, degree, level (convolution vs ambient) for D^2=0, kappa, Theta_A.
CLAUDE.md:690:Trigger: any formula shared across volumes (kappa, r-matrix, Theta_A, bar differential, connection 1-form, complementarity).
CLAUDE.md:871:AP180: Cross-volume convention clash for shadow coefficients. Vol I defines S_r as the degree-r projection of Theta_A in the convolution algebra, with S_2 = kappa. Vol II 3d_gravity.tex uses "S_2" for a different quantity (the lambda-bracket coefficient c/12 = kappa/6). No bridge identity is given. AP144 requires: when two conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site. The bridge is: S_2^{Vol I} = kappa = c/2 = 6 * S_2^{lambda-bracket} (if the latter is even a well-defined invariant, which is doubtful since S_r should not depend on presentation). Most likely resolution: S_2^{Vol II} is simply WRONG and should be corrected to c/2.
CLAUDE.md:920:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
wave2_audit_20260413_001942/D15_hardcoded_parts.md:115:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:204:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:266:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:389:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1337:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1597:    94	The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:328:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
appendices/nonlinear_modular_shadows.tex:180:\index{Theta_A@$\Theta_{\cA}$!as Maurer--Cartan element}%
appendices/spectral_higher_genus.tex:112: components $\Theta_A^{>2} \neq 0$ even when $\kappa = 0$; see).
wave2_audit_20260413_001942/F05_definitions_en.md:109:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

thinking
**Evaluating file inspection**

I need to consider updating the plan, possibly to inspect the target file and locate definitions. Perhaps using an explorer would be helpful. I'll look for suspected sections and search for mission terms as well. Using rg could be a great way to find terms in the target and its dependencies. I'll explore parallel command execution and count lines to get exact line numbers, maybe using nl -ba or rg -n for patterns in the huge file.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	
codex
The constitutional layer confirms the E1-first requirement: the file is supposed to build `\Theta_A` in `\mathfrak g^{E1}`, then project to `\mathfrak g^{mod}`. I’m now checking whether this chapter actually satisfies that contract or quietly leans on undeclared objects and imported conventions.
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theta_|Theta\\\\_|shadow tower|G/L/C/M|class~G|class~L|class~C|class~M|Maurer|MC equation|D_\\\\cA|g\\\\"'^'"\\{E1\\}|g\\\\"'^'"\\{mod\\}|\\\\gAmod|\\\\Convstr|modular convolution|convolution algebra|def:modular-convolution-dg-lie|thm:mc2-bar-intrinsic|def:scalar-lane|thm:genus-universality|thm:modular-homotopy-convolution|def:shadow-growth-rate|thm:single-line-dichotomy\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow tower" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   34233 chapters/theory/higher_genus_modular_koszul.tex
 exited 2 in 51ms:
rg: regex parse error:
    (?:Theta_|Theta\_|shadow tower|G/L/C/M|class~G|class~L|class~C|class~M|Maurer|MC equation|D_\cA|g\^\{E1\}|g\^\{mod\}|\gAmod|\Convstr|modular convolution|convolution algebra|def:modular-convolution-dg-lie|thm:mc2-bar-intrinsic|def:scalar-lane|thm:genus-universality|thm:modular-homotopy-convolution|def:shadow-growth-rate|thm:single-line-dichotomy)
                                                                                                ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Total output lines: 3255

CLAUDE.md:11:**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
CLAUDE.md:204:NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.
CLAUDE.md:829:AP143: DS ghost charge background shift omission. DS reduction from sl_N to W_{N,f} requires subtracting the full ghost central charge c_ghost(N,f,k) = c(sl_N,k) - c(W_{N,f},k), which includes the background charge contribution from the DS BRST complex. The simplified formula c_ghost(N,k=0) = N*(N-1) OMITS this background charge; the correct formula gives (N-1)*((N^2-1)*(N-1)-1). At N=7: 1722 vs 42. This error caused a cascade across W6/W7 shadow tower engines where engine and test were synchronized to the same wrong value (AP128 variant). VERIFY: at N=2, ghost_c = 1*((4*1)-1) = 3 = c(sl_2,0) - c(Vir,0) = 3 - 0. Before writing ANY DS ghost formula for N>=3, compute c(sl_N,k) - c(W_{N,f},k) directly from the Fateev-Lukyanov formula.
CLAUDE.md:860:AP171: Associator dependence dichotomy. The chiral QG equivalence (R-matrix <-> A_inf <-> coproduct) holds "up to choice of Drinfeld associator Phi." COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (proved for sl_2: GRT_1 shifts P_3 by coboundaries). COCHAIN-LEVEL derived center = ASSOCIATOR-DEPENDENT (the cochain-level E_3 carries the quantum group structure). Bar-side invariants (kappa, shadow tower) are associator-FREE. Cobar-side and coproduct-side depend on Phi. Analogous to deformation quantization: gauge-equivalent star products.
CLAUDE.md:930:**Vol I**: Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M/M*/W, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin) + Part VI (Frontier) + Appendices.
scripts/platonic_rectification_20.py:208:1. The shadow tower gives obs_g as a specific cohomology class on M-bar_g
scripts/platonic_rectification_20.py:216:the shadow tower recursive structure.
scripts/platonic_rectification_20.py:338:   to all genera. The shadow tower obs_g = kappa*lambda_g at uniform weight IS the
scripts/platonic_rectification_20.py:361:   Delta = 0 (shadow tower finite at degree 2). SC-formality means m_k^{SC} = 0 for k>=3.
scripts/platonic_rectification_20.py:363:   This should follow from the shadow tower controlling the SC operations via the
scripts/platonic_rectification_20.py:367:   of the SC bar implies the shadow tower truncates at degree 2 (by the tower-bar
appendices/nonlinear_modular_shadows.tex:36:\index{period correction!shadow tower}%
appendices/nonlinear_modular_shadows.tex:75:\index{shadow tower!prefundamental compatibility}
appendices/nonlinear_modular_shadows.tex:213:\index{L-infinity formality@$L_\infty$ formality!shadow tower identification}%
appendices/nonlinear_modular_shadows.tex:396:\index{shadow tower!from Maurer--Cartan evaluation}%
appendices/nonlinear_modular_shadows.tex:436:\index{shadow tower!family evaluation}%
appendices/nonlinear_modular_shadows.tex:992:In class~$G$ the shadow tower terminates at degree~$2$
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

collab wait(call_rSZcDMqxgDGCciH2y6RdNc6F)
  receivers: 019d8649-0f59-7301-9d55-ada4dd196cff
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def:shadow-postnikov-tower" -n' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 214

appendices/branch_line_reductions.tex:49:obstruction tower (Definition~\ref{def:shadow-postnikov-tower}),
appendices/branch_line_reductions.tex:92: (Definition~\ref{def:shadow-postnikov-tower}).
wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1267:   478	\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
appendices/combinatorial_frontier.tex:490: (Definition~\ref{def:shadow-postnikov-tower}) is the
metadata/label_index.json:7810:  "def:shadow-postnikov-tower": {
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:610:/bin/zsh -lc "rg -n '\\\\label\\{(def:geom-cobar-precise|thm:bar-cobar-inversion-qi|thm:bar-cobar-isomorphism-main|thm:bar-modular-operad|thm:genus-induction-strict|thm:FM|thm:normal-crossings|thm:arnold-three|def:conilpotent-complete|def:bar-differential-complete|def:chiral-koszul-pair|conv:regime-tags|conv:bar-coalgebra-identity|thm:completion-necessity|thm:obstruction-quantum|thm:prism-higher-genus|thm:fundamental-twisting-morphisms|prop:universal-twisting-adjunction|def:chiral-twisting-datum|lem:degree-cutoff|def:strong-completion-tower|thm:explicit-theta|def:shadow-postnikov-tower|thm:quantum-complementarity-main|thm:quantum-diff-squares-zero|thm:chiral-koszul-duality|prop:cdg-hom-complex|thm:chiral-hochschild-differential|lem:center-cohomology|lem:deformation-space|lem:period-integral|thm:curvature-central|cor:shadow-extraction|thm:mc2-bar-intrinsic|thm:bar-concentration)\\}' chapters appendices metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
audit_campaign_20260412_231034/T12_MC5_BV_bar.md:697:chapters/examples/toroidal_elliptic.tex:54:The Arnold relation (Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex of Part~\ref{part:bar-complex} (Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/B04_thm_D_bridge.md:441:chapters/frame/heisenberg_frame.tex:1866:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}). The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
wave2_audit_20260413_001942/B04_thm_D_bridge.md:442:chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1815:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
audit_campaign_20260412_231034/T20_gerstenhaber.md:1051:chapters/examples/toroidal_elliptic.tex:54:The Arnold relation (Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex of Part~\ref{part:bar-complex} (Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:565:478:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:1796:  6018	(Definition~\ref{def:shadow-postnikov-tower},
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:2099:478:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:204:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:266:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:389:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1337:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1597:    94	The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '11840,11940p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
(g,r,d) \;\text{with}\; w(g,r,d) < N\bigr\}.
\]
This filtration is \emph{exhaustive}
($\mathfrak{g}^{\mathrm{amb}} = F^1$),
\emph{separated}
($\bigcap_{N} F^N = 0$),
\emph{complete} (the completion
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"mathfrak\\{g\\}\\"'^'"\\\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched "
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{E1\\}\\}\"" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:mathfrak\{g\}\^\{\mathrm\{E1\}\})
                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{E1\\}\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{E1\\}\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\mathfrak\\{g\\}\\"'^{E_1}'"'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\mathfrak\{g\}\^{E_1})
                         ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\mathfrak\\{g\\}\\"'^'"\\{E_1\\}'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/B04_thm_D_bridge.md:943:  3747	\mathfrak{g}^{E_1}_{\mathrm{Vir}} \to
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1378:   150	$\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
audit_campaign_20260412_231034/F14_averaging.md:796:   150	$\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
audit_campaign_20260412_231034/F14_averaging.md:1269:   134	algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of
audit_campaign_20260412_231034/F14_averaging.md:1286:    88	$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
audit_campaign_20260412_231034/F14_averaging.md:1292:   134	algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of
audit_campaign_20260412_231034/F14_averaging.md:1297:    48	averaging map $\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
audit_campaign_20260412_231034/F14_averaging.md:1316:   160	$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:515:$\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
wave2_audit_20260413_001942/D12_hochschild_disambiguation.md:1760:$\mathfrak{g}^{E_1}_\cA$: the primitive object, carrying the
chapters/examples/toroidal_elliptic.tex:3055:\mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$, which
chapters/connections/concordance.tex:3779:\operatorname{av}\colon \mathfrak{g}^{E_1}_\cA
chapters/frame/preface.tex:439:$\mathrm{av}\colon\mathfrak{g}^{E_1}_\cA
chapters/frame/preface.tex:1028:Maurer--Cartan element $\Theta_\cA \in \MC(\mathfrak{g}^{E_1}_\cA)$
chapters/frame/preface.tex:1418:$\mathfrak{g}^{E_1}_\cA$: the primitive object, carrying the
chapters/frame/preface.tex:1744:$\mathfrak{g}^{E_1}_\cA$ (the third rung
chapters/frame/preface.tex:2175:$\Theta_\cA\in\MC(\mathfrak{g}^{E_1}_\cA)$ into the modular
chapters/theory/introduction.tex:61:$E_1$-modular convolution algebra~$\mathfrak{g}^{E_1}_\cA$,
standalone/gaudin_from_collision.tex:160:$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
standalone/virasoro_r_matrix.tex:88:$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\mathfrak\\{g\\}\\"'^{E_1}'"' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 66ms:
rg: regex parse error:
    (?:\\mathfrak\{g\}\^{E_1})
                         ^
error: repetition quantifier expects a valid decimal
wait(call_rSZcDMqxgDGCciH2y6RdNc6F) timed out:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "g''^{E_1}" chapters' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:g^{E_1})
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"g\\"'^'"\\{E_1\\}\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
chapters/theory/e1_modular_koszul.tex:2185:& $Q_g^{E_1} + Q_g^{!,E_1}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{mod\\}\\}' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:4011:\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\cA)$
chapters/theory/higher_genus_modular_koszul.tex:9829:$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
chapters/theory/higher_genus_modular_koszul.tex:11100:$\mathfrak{g}^{\mathrm{mod}}_\cA$
chapters/theory/quantum_corrections.tex:46:convolution algebra $\mathfrak{g}^{\mathrm{mod}}_{\cA}$, dictated by
chapters/theory/bar_cobar_adjunction_inversion.tex:5135:$\mathfrak{g}^{\mathrm{mod}}_\cA$
chapters/theory/bar_cobar_adjunction_inversion.tex:5153:$\mathfrak{g}^{\mathrm{mod}}_\cA$ is indexed by stable graphs
chapters/theory/chiral_hochschild_koszul.tex:5072:$\mathfrak{g}^{\mathrm{mod}}_\cA$
chapters/theory/configuration_spaces.tex:1342:$\mathfrak{g}^{\mathrm{mod}}_\cA$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3980,4045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
 Definition~\textup{\ref{def:shadow-algebra}}\textup{)}.
\end{enumerate}
The scalar, spectral, and quartic invariants are the first three
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'two-level' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
62:(\S\ref{subsec:two-level-convention}). The weight filtration on
10400:Maurer--Cartan equation, one in each layer of the two-level
10401:convention (Remark~\ref{rem:two-level-convention}).
10486:\subsection{The two-level convention: strict models and homotopy-invariant objects}
10487:\label{subsec:two-level-convention}
10489:\begin{remark}[The two-level convention]
10490:\label{rem:two-level-convention}
10491:\index{two-level convention}
10611:the two-level convention. The complete filtered $L_\infty$-algebra
11105:algebra (Remark~\ref{rem:two-level-convention}(d)) in which the
15163:shadow algebra; Convention~\ref{rem:two-level-convention}).
30080: \textup{(}\S\textup{\ref{subsec:two-level-convention}}\textup{)}.
30110:The two-level convention
30111:(\S\ref{subsec:two-level-convention}) establishes that
codex
I’ve got the opening 260 lines. The first pass already shows this chapter invoking `\Theta_\cA`, `\gAmod`, the four shadow classes, and `\Theta_\cA^{E_1}` before any local definition block for those objects. I’m now tracing whether those are actually defined later in the same file or only imported by reference.
exec
/bin/zsh -lc "rg -n \"Theta_\\\\cA|Theta_\\\\cA\\"'^'"\\{E_1\\}|shadow tower|class~\\\\mathsf\\{G\\}|class~\\\\mathsf\\{L\\}|class~\\\\mathsf\\{C\\}|class~\\\\mathsf\\{M\\}|\\\\gAmod|\\\\Definfmod|modular convolution|Maurer--Cartan equation|MC element|convolution dg~Lie algebra|E_1-framed|two-level-convention|def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:mc2-bar-intrinsic|def:modular-convolution-dg-lie|thm:modular-homotopy-convolution|sec:koszul-across-genera|subsec:two-level-convention|def:e1|g\\"'^'"\\{E1\\}|g\\"'^'"\\{mod\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{def:shadow-algebra\\}|label\\{def:modular-bar-hamiltonian\\}|label\\{def:shadow-postnikov-tower\\}|label\\{subsec:two-level-convention\\}|label\\{def:modular-convolution-dg-lie\\}|label\\{thm:mc2-bar-intrinsic\\}|label\\{thm:modular-homotopy-convolution\\}|label\\{def:scalar-lane\\}|label\\{thm:single-line-dichotomy\\}|label\\{prop:depth-gap-trichotomy\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Theta_\cA|Theta_\cA\^\{E_1\}|shadow tower|class~\mathsf\{G\}|class~\mathsf\{L\}|class~\mathsf\{C\}|class~\mathsf\{M\}|\gAmod|\Definfmod|modular convolution|Maurer--Cartan equation|MC element|convolution dg~Lie algebra|E_1-framed|two-level-convention|def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:mc2-bar-intrinsic|def:modular-convolution-dg-lie|thm:modular-homotopy-convolution|sec:koszul-across-genera|subsec:two-level-convention|def:e1|g\^\{E1\}|g\^\{mod\})
             ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2552:\label{def:scalar-lane}
chapters/theory/higher_genus_modular_koszul.tex:3528:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:9838:\label{def:modular-convolution-dg-lie}
chapters/theory/higher_genus_modular_koszul.tex:10487:\label{subsec:two-level-convention}
chapters/theory/higher_genus_modular_koszul.tex:10597:\label{thm:modular-homotopy-convolution}
chapters/theory/higher_genus_modular_koszul.tex:11886:\label{def:shadow-postnikov-tower}
chapters/theory/higher_genus_modular_koszul.tex:12139:\label{def:shadow-algebra}
chapters/theory/higher_genus_modular_koszul.tex:17227:\label{prop:depth-gap-trichotomy}
chapters/theory/higher_genus_modular_koszul.tex:18016:\label{thm:single-line-dichotomy}
chapters/theory/higher_genus_modular_koszul.tex:30236:\label{def:modular-bar-hamiltonian}
chapters/theory/higher_genus_modular_koszul.tex:2552:\label{def:scalar-lane}
chapters/theory/higher_genus_modular_koszul.tex:3528:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:9838:\label{def:modular-convolution-dg-lie}
chapters/theory/higher_genus_modular_koszul.tex:10487:\label{subsec:two-level-convention}
chapters/theory/higher_genus_modular_koszul.tex:10597:\label{thm:modular-homotopy-convolution}
chapters/theory/higher_genus_modular_koszul.tex:11886:\label{def:shadow-postnikov-tower}
chapters/theory/higher_genus_modular_koszul.tex:12139:\label{def:shadow-algebra}
chapters/theory/higher_genus_modular_koszul.tex:17227:\label{prop:depth-gap-trichotomy}
chapters/theory/higher_genus_modular_koszul.tex:18016:\label{thm:single-line-dichotomy}
chapters/theory/higher_genus_modular_koszul.tex:30236:\label{def:modular-bar-hamiltonian}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '10460,10570p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 (Theorem~\ref{thm:shadow-formality-identification}).
\item \emph{Gauge equivalence.}
 Two MC elements
 $\Theta, \Theta' \in \MC(\Definfmod(\cA))$ are gauge
 equivalent if and only if they lie in the same
 connected component of the Deligne--Getzler--Hinich
 $\infty$-groupoid $\MC_\bullet(\Definfmod(\cA))$.
 The $1$-simplices (gauge transformations) involve all
 higher brackets $\ell_n$ ($n \geq 3$), not just the
 strict differential and bracket. In the strict model,
 gauge equivalence reduces to the classical exponential
 action of degree-$0$ elements; the $L_\infty$
 gauge groupoid is the homotopy-invariant enlargement
 that persists across quasi-isomorphic replacements.
\end{enumerate}
The strict form~\eqref{eq:strict-mc} suffices for \emph{existence}
of MC elements and for the obstruction-recursion tower
(Construction~\ref{constr:obstruction-recursion}). The $L_\infty$
form~\eqref{eq:quantum-linfty-mc} is the invariant statement that
persists under all operations in the homotopy category.
exec
/bin/zsh -lc "rg -n \"class~\\\\mathsf\\{G\\}|class~\\\\mathsf\\{L\\}|class~\\\\mathsf\\{C\\}|class~\\\\mathsf\\{M\\}|\\\\mathsf\\{G\\}|\\\\mathsf\\{L\\}|\\\\mathsf\\{C\\}|\\\\mathsf\\{M\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:class~\mathsf\{G\}|class~\mathsf\{L\}|class~\mathsf\{C\}|class~\mathsf\{M\}|\mathsf\{G\}|\mathsf\{L\}|\mathsf\{C\}|\mathsf\{M\})
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'fg\\"'^'"\\{E_1\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'fg\\"'^{E_1}'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:fg\^{E_1})
            ^
error: repetition quantifier expects a valid decimal

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'fg\\"'^'"\\{E_1\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Assessing line ranges**

I need to read line ranges around definitions. To do this, I'll use sed for label lines. I also want to search for fixed strings to find their first occurrences. For instance, I might use `rg -n -F 'Theta_\cA'` for that purpose. I want to ensure I'm thorough in capturing everything I need, keeping my approach as efficient as possible while not missing essential details.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -nF 'fg"'^{E_1}'"'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:621:chapters/theory/e1_modular_koszul.tex:30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
audit_campaign_20260412_231034/F14_averaging.md:274:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:21:averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
audit_campaign_20260412_231034/F14_averaging.md:774:    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
audit_campaign_20260412_231034/F14_averaging.md:1079:    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
audit_campaign_20260412_231034/F01_kappa_KM.md:679:  1321	 $\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$,
audit_campaign_20260412_231034/F01_kappa_KM.md:773:    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
audit_campaign_20260412_231034/F01_kappa_KM.md:1040:  1321	 $\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$,
audit_campaign_20260412_231034/F01_kappa_KM.md:1140:  1321	 $\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$,
audit_campaign_20260412_231034/F01_kappa_KM.md:1183:    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
chapters/theory/e1_modular_koszul.tex:30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
audit_campaign_20260412_231034/T09_MC2_theta.md:868:chapters/theory/e1_modular_koszul.tex:30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
standalone/garland_lepowsky.tex:1321: $\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$,
compute/audit/true_formula_census_draft_wave12.md:121:**Canonical form.** The coinvariant projection $\mathrm{av}: \fg^{E_1}\to \fg^{\mathrm{mod}}$ at arity 2 satisfies
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'convolution' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarcodex
The key labels are all much later in the file: `def:scalar-lane` at line 2552, `thm:mc2-bar-intrinsic` at 3528, `def:modular-convolution-dg-lie` at 9838, `subsec:two-level-convention` at 10487, `def:shadow-postnikov-tower` at 11886, `def:shadow-algebra` at 12139, and `def:modular-bar-hamiltonian` at 30236. That means the opening section is front-loading a lot of terminology before the formal surfaces appear, so I’m verifying whether that’s just roadmap prose or whether later proofs rely on the undefined objects.
 succeeded in 52ms:
58:convolution}
63:\index{E1 algebra@$E_1$-algebra!modular convolution}
233:\begin{definition}[$E_1$ modular convolution dg~Lie algebra]
234:\label{def:e1-modular-convolution}
236:\index{E1 algebra@$E_1$-algebra!modular convolution|textbf}
237:\index{modular convolution dg Lie algebra!E1@$E_1$ (ordered)}
247:\label{eq:e1-modular-convolution}
260:(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
285:morphism: the symmetrization converts $T^c$-convolution to
286:$\mathrm{Sym}^c$-convolution, which is exactly the passage from ordered
316:By Definition~\ref{def:e1-modular-convolution}, the differential and
358: Definition~\textup{\ref{def:e1-modular-convolution}}: $\operatorname{av}$
360: surjective dg~Lie morphism from $T^c$-convolution to
361: $\mathrm{Sym}^c$-convolution.
526: in the holomorphic $E_1$ convolution Lie algebra, so no such
652:convolution algebra, and no section of $\operatorname{av}$
1433:(Definition~\ref{def:e1-modular-convolution})
1471:of Definition~\textup{\ref{def:e1-modular-convolution}} sends each
2150:\textup{(}Definition~\textup{\ref{def:e1-modular-convolution}}),
2240:Definition~\textup{\ref{def:e1-modular-convolution}} sends the $E_1$
exec
/bin/zsh -lc "rg -n -F 'Theta_\\cA' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\gAmod' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathsf{G}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Maurer--Cartan equation' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
257:amplitude $Z_g(\cA) = \operatorname{Tr}^{\circ g}(\Theta_\cA^{(g)})$
292:The universal MC element $\Theta_\cA := D_\cA - d_0$
 succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
63:$\gAmod$ controls the extension tower: each finite truncation
2190: \in \MC(\gAmod)$ exists at all genera
3235:element~$\Theta_\cA \in \MC(\gAmod)$:
3256:in~$\gAmod$, not by the KdV hierarchy.
3554:\item \emph{Maurer--Cartan on\/~$\gAmod$.}
3587:$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
3590:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
3706: $D^2 = 0$ on $\gAmod$
3713: algebra $\gAmod$
3741: The weight filtration $F^N\gAmod$
3745: $\widehat{\gAmod} = \varprojlim_N \gAmod/F^{N+1}$
3877: The identity $D^2 = 0$ on $\gAmod$ is
3882: $\widehat{\gAmod}$ is the inverse limit of
3883: finite-dimensional quotients $\gAmod/F^{N+1}$, and
3899:in $\gAmod/F^{N+1}$, the projections are compatible, and the
3902:an MC element in~$\widehat{\gAmod}$.
4122:(viewed as an element of $\gAmod$)
4180:of~$\gAmod$: each zero-internal-edge bipartite graph with $r$
 succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
3371:gives the Maurer--Cartan equation. See
3511:simultaneously. The Maurer--Cartan equation
3777:which is the Maurer--Cartan equation
3911:and the Maurer--Cartan equation is a tautological consequence
4994: At each genus~$g$, the Maurer--Cartan equation
5252: The Maurer--Cartan equation in $\widehat{L}_{\Gmod}$ is
9645:differential. The full Maurer--Cartan equation
10396:\begin{remark}[The two Maurer--Cartan equations]
10398:\index{Maurer--Cartan equation!strict vs $L_\infty$}
10400:Maurer--Cartan equation, one in each layer of the two-level
11275:Maurer--Cartan equation is
11372:\item The Maurer--Cartan equation stratifies by weight:
11608:The fixed-$(g,n)$ projection of the Maurer--Cartan equation
11902:of the Maurer--Cartan equation in
12365:consequence of the Maurer--Cartan equation for
12657:+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
12682: satisfies the full Maurer--Cartan equation.
12808: the full Maurer--Cartan equation
13611:The image of the Maurer--Cartan equation under this quotient
 succeeded in 51ms:
136: (class~$\mathsf{G}$, Gaussian).
155: partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
172:(class~$\mathsf{G}$, formal, quadratic)
4178:$\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators
4212: For finite-depth algebras (classes $\mathsf{G}$, $\mathsf{L}$,
4251:Depth termination: for classes $\mathsf{G}$, $\mathsf{L}$,
15168:$\mathfrak{g}_{\cA}^{\mathrm{mod},(0)} := \mathfrak{g}_{\cA}^{\mathrm{mod}} \otimes \mathsf{G}^{(0)}$,
15169:where $\mathsf{G}^{(0)}$ is the coefficient subalgebra
15179:\mathsf{G}^{(0)}$, because genus-$0$ stable graphs are
17343:$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an
22001:\textup{(}class~$\mathsf{G}$\textup{)}, $bc$ and $\beta\gamma$
22027:\emph{Mechanism~\textup{1}: class~$\mathsf{G}$ factorization
22029:For free fields of class~$\mathsf{G}$ (Heisenberg, lattice),
22087:(class~$\mathsf{G}$ factorization) is the restriction of
24603: Class~$\mathsf{G}$ ($r_{\max} = 2$): $\ell_k = 0$ for $k \geq 3$,
24670: Class~$\mathsf{G}$ ($S_3 = S_4 = S_5 = 0$):
25687: ($\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$) \\
25851:For class~$\mathsf{G}$ $($Heisenberg$)$: $S_3 = 0$, so
25936:$\mathsf{G}$ & Heisenberg & $\kappa$ only
25955:For $\cH_\kappa$ $($class~$\mathsf{G})$,
exec
/bin/zsh -lc "rg -n -F 'g"'^{E1}'"' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'g"'^{mod}'"' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '210,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   210	
   211	\begin{proof}
   212	Two distinct operations are composed. First, $\pi_{\mathrm{rib}}$
   213	forgets the cyclic ordering of half-edges at each vertex; the fibre
   214	over a stable graph $\Gamma$ of genus~$g$ with~$n$ legs is the finite
   215	set of cyclic orderings at its vertices, and the edge-orientation
   216	determinant supplies signs so that $\pi_{\mathrm{rib}}$ intertwines
   217	edge contraction in $F\!\Ass$ with edge contraction in the
   218	intermediate ``symmetric $F\!\Ass$''
   219	(Getzler--Kapranov \cite{GK98}, \S3).
   220	Second, $\pi_{\Sigma_n}$ takes external $\Sigma_n$-coinvariants on
   221	the labels of the~$n$ legs; this is well-defined because
   222	$\Sigma_n$ acts on the set of stable graphs by permuting leg labels
   223	and the differential commutes with relabelling. The composite is a
   224	quasi-isomorphism by the standard comparison between ribbon and
   225	commutative modular operads (Getzler--Kapranov \cite{GK98}, Thm.~4.9).
   226	Only the external-label step is used by the averaging map
   227	$\operatorname{av}$ of~\eqref{eq:e1-to-einfty-projection}; the
   228	ribbon-forgetting step is absorbed into the identification of the
   229	target at the Hom-level, where $\operatorname{End}_\cA(n)$ sees only

thinking
**Searching for definitions**

I find it interesting that there's no fixed string for g^{E1}/g^{mod}. I should create macros to represent them. Next, I need to locate the definitions related to the E1-framed MC element and the two-level convention. I want to use sed around specific line ranges. I'll also need to look for definitions of classes G, L, C, and M later. Lastly, I plan to search for a label or definition environment for shadow classes, querying with the fixed string "four shadow classes."
exec
/bin/zsh -lc "sed -n '9800,10660p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'four shadow classes' chapters/theory/higher_genus_modular_koszul.tex; rg -n -F 'shadow classes' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3470,3610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:recursive-existence}).

These five theorems are aspects of a single object: the modular Koszul chiral
algebra (Definition~\ref{def:modular-koszul-chiral}). Every chiral
algebra in Part~\ref{part:physics-bridges} is an instance of this structure.
The computations that follow (bar cohomology, genus expansions,
discriminants, complementarity sums) are invariants of the modular characteristic
package $\mathcal{C}_{\cA} = (\Theta_{\cA}, \kappa(\cA),
\Delta_{\cA}, \Pi_{\cA}, \mathcal{H}_{\cA})$
(Definition~\ref{def:full-modular-package}).
What one algebra sees as
deformation, its dual sees as obstruction: the Lagrangian
principle at work, algebra by algebra, genus by genus.


%================================================================
% THE MODULAR BAR-HAMILTONIAN AND THE EXTENSION TOWER
%================================================================

\section{The modular convolution algebra and the master equation}
 succeeded in 51ms:
17499:The Hankel data for the standard shadow classes:
21296:\index{tautological ring!shadow classes}
21417:\index{tautological ring!shadow classes|textbf}
 succeeded in 50ms:
satisfying the locality axiom \textup{(}the chiral bracket
$\mu\colon \cA \boxtimes \cA \to \Delta_* \cA$ is supported on
the diagonal~$\Delta$\textup{)}, the genus-$g$ curvature
$\mu_0^{(g)}$ lies in the center~$Z(\cA)$ for all $g \geq 1$.
In particular, every chiral algebra in the standard landscape
satisfies the centrality hypothesis of
Theorem~\textup{\ref{thm:genus-induction-strict}}.
\end{proposition}

\begin{proof}
Each genus-$g$ differential~$d_g$ ($g \geq 1$) is constructed from
period integrals $\oint_{\gamma_k} \omega$ over homology cycles
$\gamma_k \subset \Sigma_g$. These are \emph{global} operations:
they act on the bar complex by integration over $1$-cycles disjoint
from the collision locus~$\Delta$. The chiral bracket~$\mu$ is
\emph{local}: supported on~$\Delta$. By the locality axiom,
operations supported on disjoint subsets commute:
\[
 \bigl[\textstyle\oint_{\gamma_k},\;\mu(a,-)\bigr] = 0
 \qquad \text{for all } a \in \cA,\;

exec
/bin/zsh -lc "rg -n -F '\\begin{definition}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
224:\begin{definition}[Completed chiral algebra]\label{def:completed-chiral-algebra}
429:\begin{definition}[Modular Koszul object: homotopy form]\label{def:modular-koszul-homotopy}
534:\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
2450:\begin{definition}[Scalar modular characteristic package]
2480:\begin{definition}[Full modular characteristic package]
2551:\begin{definition}[Uniform-weight lane (scalar lane)]
9837:\begin{definition}[Modular convolution dg~Lie algebra]
10635:\begin{definition}[Modular homotopy type;
11301:\begin{definition}[Depth filtration and tridegree;
11832:\begin{definition}[Weight filtration]
11869:\begin{definition}[Extension tower]
11885:\begin{definition}[Shadow obstruction tower]
12138:\begin{definition}[Shadow algebra]
12399:\begin{definition}[$\sigma$-invariant shadow ring]
13002:\begin{definition}[Primitive logarithmic modular kernel]
13044:\begin{definition}[Primitive pre-Lie product]
13510:\begin{definition}[Reduced branch BV packet]
14361:\begin{definition}[Complementarity action]
14450:\begin{definition}[Modular chiral algebra structure]
16191:\begin{definition}[Shadow depth classification]
thinking
**Compiling reference bullets for definitions**

I’m gathering precise file paths and line numbers to bullet the locations where Theta_A and the Maurer-Cartan equation are defined in `chapters/theory/higher_genus_modular_koszul.tex`. I’m also pinpointing the shadow tower, classes G/L/C/M, and convolution algebras g^{E1} and g^{mod}, making clear which items this file defines internally versus references externally. I’m aiming to organize the info clearly for each requested element with proper citations.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'modular convolution dg' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
9833:\subsection{The modular convolution dg~Lie algebra}
9835:\index{modular convolution dg Lie algebra|textbf}
9843:The \emph{modular convolution dg~Lie algebra} is
9908:\index{modular convolution dg Lie algebra!structure}
10043:\index{modular convolution dg Lie algebra!explicit bracket}
30200:The modular convolution dg~Lie algebra

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '9820,9888p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{sec:modular-bar-hamiltonian}

A single algebraic object controls the modular theory: the
convolution dg~Lie algebra together with its shadow obstruction tower
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
thinking
**Evaluating class definitions**

I need to wait for the explorer, possibly for a later moment. I'm thinking about whether the classes are defined before their usage. I noticed there's a shadow depth classification at line 16191, and it seems to define the classes. However, I'm seeing the first usage at line 136, which is way before the definition. So, I should read around line 16191 to clarify everything. Let's explore that further!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'E_1' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
181:shadow of the $E_1$-framed MC element.
803:$E_1$ page splits as
805:E_1^{p,q}(g)
807:E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
935:\emph{Step~1: Decomposition of the $E_1$ page.}
949:collision divisors. The $E_1$ page concentrates
973:Hence the $E_1$ page decomposes:
975:E_1^{p,q}(g{=}1) \;=\; E_1^{p,q}(g{=}0)
978:where $E_1(g{=}0)$ is the concentrated genus-$0$
999:\;\longrightarrow\; E_1^{n-1,h}(g{=}0)
1069:$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
1285:\emph{Step~1: $E_1$ decomposition at genus~$g$.}
1304:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
1526:The genus-$g$ decomposition of the enriched $E_1$ page is identical to
1529:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
1784:already accounted for on~$E_1$), while generators with $s < 2$
2116: $E_1$ differentials as on~$\mathbb{P}^1$: the
2429:$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g \barB_g(\cA))$
3589:$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
codex
The file does eventually contain a `Shadow depth classification` definition, but only at line 16191. So the opening section’s use of classes `\mathsf G/\mathsf L/\mathsf C/\mathsf M` at lines 136–155 is not a local introduction; it is anticipatory prose. I’m checking whether later theorem/proof blocks also use those classes before line 16191, because that turns exposition debt into a formal dependency error.
exec
/bin/zsh -lc "sed -n '16160,16280p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}$105 + 945 + 10395$ trivalent trees at degrees
$5$--$7$\textup{)} count different combinatorial objects
yet produce the same scalar value $S_k$ on the primary
line.
\end{corollary}

\begin{proof}
Parts~(i) and~(ii) are immediate from
Propositions~\ref{prop:shadow-formality-higher-degree}
and~\ref{prop:linfty-obstruction-5-6} respectively.
Part~(iii) follows from the explicit verification tables in
those propositions: for classes $\mathbf{G}$,
$\mathbf{L}$, $\mathbf{C}$, all three quantities vanish at
degrees $5$, $6$, $7$ because the tower terminates
earlier. For class $\mathbf{M}$, all three are nonzero
because $\Delta \neq 0$ forces $S_k \neq 0$ for all
$k \geq 4$
(Theorem~\ref{thm:single-line-dichotomy}).

The tree count at degree~$7$ for the stable-graph route is
exec
/bin/zsh -lc "awk 'NR<9837' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\gAmod' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<3528' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'Maurer--Cartan equation' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathsf{G}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<12138' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'shadow tower' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
63:$\gAmod$ controls the extension tower: each finite truncation
2190: \in \MC(\gAmod)$ exists at all genera
3235:element~$\Theta_\cA \in \MC(\gAmod)$:
3256:in~$\gAmod$, not by the KdV hierarchy.
3554:\item \emph{Maurer--Cartan on\/~$\gAmod$.}
3587:$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
3590:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
3706: $D^2 = 0$ on $\gAmod$
3713: algebra $\gAmod$
3741: The weight filtration $F^N\gAmod$
3745: $\widehat{\gAmod} = \varprojlim_N \gAmod/F^{N+1}$
3877: The identity $D^2 = 0$ on $\gAmod$ is
3882: $\widehat{\gAmod}$ is the inverse limit of
3883: finite-dimensional quotients $\gAmod/F^{N+1}$, and
3899:in $\gAmod/F^{N+1}$, the projections are compatible, and the
3902:an MC element in~$\widehat{\gAmod}$.
4122:(viewed as an element of $\gAmod$)
4180:of~$\gAmod$: each zero-internal-edge bipartite graph with $r$
 succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
3371:gives the Maurer--Cartan equation. See
3511:simultaneously. The Maurer--Cartan equation
 succeeded in 51ms:
2754:the bar-intrinsic shadow tower of
2824:\Theta_\cA \text{ and its shadow tower}
3181:\index{random matrix theory!shadow tower}
11985:\index{Brown--Henneaux!shadow tower reading}
 succeeded in 51ms:
136: (class~$\mathsf{G}$, Gaussian).
155: partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
172:(class~$\mathsf{G}$, formal, quadratic)
4178:$\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators
4212: For finite-depth algebras (classes $\mathsf{G}$, $\mathsf{L}$,
4251:Depth termination: for classes $\mathsf{G}$, $\mathsf{L}$,
15168:$\mathfrak{g}_{\cA}^{\mathrm{mod},(0)} := \mathfrak{g}_{\cA}^{\mathrm{mod}} \otimes \mathsf{G}^{(0)}$,
15169:where $\mathsf{G}^{(0)}$ is the coefficient subalgebra
15179:\mathsf{G}^{(0)}$, because genus-$0$ stable graphs are


thinking
**Summarizing definitions and references with file and line citations**

I’m organizing a clear bullet list that identifies whether each main item—theta_A, shadow tower, G/L/C/M classes, modular and E1 convolutions—is defined or just referenced in the `higher_genus_modular_koszul.tex` file. For each, I include precise file paths and line numbers, noting that `g^{E1}` is defined externally while the others are defined in or referenced by the higher_genus file. I also clarify that the MC equation is wrapped into the theta_A bullet for clarity.
codex
- `chapters/theory/higher_genus_modular_koszul.tex:34-45` defines the positive-genus bar correction `Θₐ := Dₐ − d₀` and immediately spells out the Maurer–Cartan equation `d₀Θₐ + ½[Θₐ,Θₐ] = 0`, so this file introduces both the MC element and its equation (not just a reference).  
- `chapters/theory/higher_genus_modular_koszul.tex:125-146` carries the discriminant/Δ analysis that partitions shadow depth into the four classes `𝔾` (Gaussian), `𝔏` (Lie), `ℭ` (contact) and `𝔐` (mixed), so the higher_genus chapter itself defines the G/L/C/M classification.  
- `chapters/theory/higher_genus_modular_koszul.tex:11886-11930` is Definition \ref{def:shadow-postnikov-tower}, which constructs the shadow obstruction tower `Θₐ^{≤r}` and states the obstruction class `o_{r+1}(𝔄)` before insisting the inverse limit exists; the shadow tower definition therefore lives in this file.  
- `chapters/theory/higher_genus_modular_koszul.tex:9823-9871` (Definition \ref{def:modular-convolution-dg-lie}) defines the modular convolution dg Lie algebra `𝔤ₐ^{mod}` from the `Σₙ`‑coinvariant Hom into `Endₐ(n)` and describes its differential/bracket, so `higher_genus_modular_koszul.tex` provides `𝔤^{mod}` directly.  
- `chapters/theory/e1_modular_koszul.tex:233-288` defines the ordered convolution dg Lie algebra `${𝔤ₐ^{mod}}^{E₁}` (the `E₁` convolution) and the averaging map `av: 𝔤^{E₁} → 𝔤^{mod}`; the higher_genus chapter only references this ordered layer (e.g., `Θₐ^{E₁}`) and does not reintroduce the definition itself.


thinking
**Searching for MC equation occurrences**

I need to check when the term "shadow tower" first appears, possibly related to the definition, but not until 11885. I want to see if there are formal usages earlier in the proofs. Particularly, I should locate where the Maurer-Cartan (MC) equation is defined and if it's used before its definition in any proofs. The early proposition at line 239 mentions "universal MC element." It seems I should search the lines before 3528 for any references to proofs mentioning the MC equation.
thinking
**Investigating MC dependencies**

I need to search for line numbers around 3371, focusing on lines 3340-3380. I'm also curious about occurrences at line 2190, so I’ll read around 2160-2200. I want to determine if any proof mentions the MC equation before it's formally defined, which could pose a problem if undeclared terms are involved. I believe the proposition at line 239 references the "universal MC element." This might create a serious concern if undefined objects are used in the theorem's statements. I'll check that forward reference to ensure it's clear.
thinking
**Fixing theorem issues**

I think I’ve spotted a potential issue: if the theorem at line 239 uses an undefined object in its statement. The exact fix might involve adding a parenthetical note like "assuming Theorem ..." or moving the proposition after the theorem or definition. Since the user has been asking for every missing definition, I could note that the theorem statement remains formally incomplete until a later theorem. I'll check for early proof blocks that reference undefined classes before line 16191 to assess the severity of this issue.
codex
I’ve isolated three likely defect patterns and I’m testing each one against actual theorem/proof blocks instead of just the chapter opening: forward use of `\Theta_\cA`, forward use of the shadow classes, and proofs that cite “the Maurer–Cartan equation” before the file has actually put that equation on a formal footing.
exec
/bin/zsh -lc "sed -n '4160,4275p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
edge must run from $L^+$ to~$L^-$. The summation over stable
graphs automatically restricts to the bipartite subposet
$\Gamma^{\mathrm{st,bip}}_{g,n}
\subset \Gamma^{\mathrm{st}}_{g,n}$.
This bipartite restriction is the chain-level
expression of Theorem~C: the two dual sides
interact only through the opposite polarization, and
the Lagrangian condition $\omega_\cA|_{L^\pm} = 0$ kills all
same-side contractions.
\end{remark}

\begin{theorem}[Bipartite shadow as $L_\infty$ tree-level structure]
\label{thm:bipartite-linfty-tree}
\ClaimStatusProvedHere
\index{bipartite shadow!$L_\infty$ tree-level structure|textbf}
\index{homotopy transfer!bipartite graphs}
\index{L-infinity algebra@$L_\infty$ algebra!bipartite tree-level}
The polarized graph algebra
$\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators
$P^{+-}$ identifies with the tree-level $L_\infty$-algebra
exec
/bin/zsh -lc "sed -n '2160,2210p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3340,3395p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'class~"'$'"\\mathsf{L}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'class~"'$'"\\mathsf{C}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
divisors. The differential $d_{\mathrm{coll}}$ acts
on the $\cA$-valued factor and leaves the
$H^{1,0}$-factor unchanged (the residue at
$z_i = z_j$ extracts the OPE from the
$\cA$-valued part and does not act on
$\omega_k(z_\ell)$, which has no pole at $z_i = z_j$
for $\ell \neq i,j$; for $\ell = i$, the product
$\omega_k(z_i) \cdot \eta^{(0)}(z_i,z_j)$ has
residue $\omega_k(z_j)$, which remains a
holomorphic form on~$X$ and multiplies the
OPE output without affecting the spectral-sequence
bigrading).
\end{proof}

\begin{theorem}[Three-tier logical architecture of
 modular Koszul duality;
 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
\index{three-tier architecture|textbf}
\index{modular Koszul duality!logical architecture|textbf}
The modular Koszul engine decomposes into three tiers
 succeeded in 50ms:
\operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
\bigr)
\]
such that:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the genus-$1$ component of its scalar trace is
 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
 the full scalar trace is
 $\operatorname{tr}(\Theta_{\cA})
 = \sum_{g \geq 1} \kappa(\cA) \lambda_g$;
\item it is compatible with clutching morphisms of stable curves;
\item under Verdier/Koszul duality, $\Theta_{\cA}$ is sent to
 $\Theta_{\cA^!}$.
\end{enumerate}
This is Theorem~\ref{thm:master-theta} (MC2).
\end{theorem}

\begin{proof}
exec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'class~"'$'"\\mathsf{M}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
138: (class~$\mathsf{L}$, Lie).
 succeeded in 52ms:
140: depth~$4$ (class~$\mathsf{C}$, contact).
 succeeded in 52ms:
144: (class~$\mathsf{M}$, mixed).
4218: For class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$), the

thinking
**Investigating theorem proof**

I'm noticing an interesting proof at 4212 that uses classes before their formal definition at 16191, along with a theorem statement. I find this is a concrete finding that needs an exact fix. I could suggest inserting a cross-reference or moving the definition, but I need line references. Now, I should inspect the definitions of the full modular package around certain lines, especially for "shadow tower" introduced. I'll check definitions around 2450-2555 for clarity.
exec
/bin/zsh -lc "sed -n '2430,2565p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
degenerates at~$E_2$.
\end{lemma}

\begin{proof}
The PBW filtration is a filtration by chiral algebras, and the
Koszulness hypothesis ensures that the associated graded is a
Koszul complex in the classical sense. The $d_r$ differential
for $r \geq 2$ maps between PBW-graded components separated
by~$r$ steps, and the Koszul concentration (all bar cohomology
is in bar-degree~$0$ on the associated graded) forces these maps
to have zero source or zero target.

On each geometric fiber (a fixed smooth or stable curve), the
collision differential is genus-$0$ type (with $d_0^2 = 0$), and
the genus-$g$ quantum corrections live in higher Leray degrees,
contributing only to $d_r$ for $r \geq 2$. Since $E_2$ is
already concentrated on the diagonal by Koszul concentration,
these higher differentials vanish.
\end{proof}

exec
/bin/zsh -lc "rg -n -F 'E_1-framed MC element' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2800,2845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\Theta_\\cA"'^{E_1}'"' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 50ms:
(Remark~\ref{rem:moduli-variation}). The generating
function~\eqref{eq:modular-char-gf} is $c_1$ of the
determinant line bundle of this sheaf, the trace of the
modular functor, extracted via GRR.

For $\widehat{\mathfrak{sl}}_{2,k}$ at integrable level, the
trace gives one number $\kappa = 3(k{+}2)/4$; the sheaf
gives $k{+}1$ conformal blocks at genus~$1$
(Remark~\ref{rem:chain-vs-classical-mf}). The full Chern
character recovers the spectral
discriminant~$\Delta_{\cA}$
(Remark~\ref{rem:spectral-characteristic-programme});
the flat connection furnishes the bar-side comparison surface for
the KZ/Hitchin package on that
integrable affine lane; the factorization structure recovers the modular
functor (Theorem~\ref{thm:chain-modular-functor},
Conjecture~\ref{conj:categorical-modular-kd}).
\end{remark}

\begin{remark}[Proof routing for Theorem~D;
 succeeded in 51ms:
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
3589:$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
3592:$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.

thinking
**Investigating theorem references**

I’m thinking about the modular package references, specifically the theorem universal-theta. I wonder if universal-theta is the same as mc2? It’s important to check labels since the user’s mission is about a foundation audit, so I need to focus on any foundation issues that might arise. It could involve bad forward references or undefined theorem labels. I'll take a closer look at line 2480, which references the theorem universal-theta, to see if the label exists.
collab wait(call_EV8giFqXiDwrjqkoKMCJBbWF)
  receivers: 019d8649-0f59-7301-9d55-ada4dd196cff
wait(call_EV8giFqXiDwrjqkoKMCJBbWF) 1 agents complete:
  019d8649-0f59-7301-9d55-ada4dd196cff completed: "- `chapters/theory/higher_genus_modular_koszul.tex:34-45` defines the positive-genus bar correction `Θₐ := Dₐ − d₀` and …"

thinking
**Clarifying definitions**

I need to be careful with my wording; instead of saying "undefined," I think "not formally defined" is better. The user's question is about whether the shadow tower Theta_A and G/L/C/M classes are defined before use. I’ll say they're not formally defined for now. I should check the contents of the file and specifically look at the e1_modular_koszul lines for the exact definition of g^{E1}. I’ll also explore references to the E1-framed MC element. Let's read through this carefully!
codex
I’ve confirmed the split: `\mathfrak g^{mod}` is defined locally around line 9838, but the ordered `E_1` convolution object is not. The only local `E_1` mention I’ve found so far is a forward allusion to `\Theta_\cA^{E_1}`, so I’m reading the ordered chapter now to pin that dependency precisely.
exec
/bin/zsh -lc "sed -n '220,310p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:universal-theta}' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3332:\label{thm:universal-theta}
chapters/theory/higher_genus_modular_koszul.tex:3332:\label{thm:universal-theta}
exec
/bin/zsh -lc "rg -n -F '\\label{thm:shadow-archetype-classification}' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:universal-MC}' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:master-theta}' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:e1-mc-element}' chapters/theory/e1_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:16499:\label{thm:shadow-archetype-classification}
chapters/theory/higher_genus_modular_koszul.tex:16499:\label{thm:shadow-archetype-classification}
 succeeded in 51ms:
chapters/connections/concordance.tex:5251:\ClaimStatusProvedHere]\label{thm:universal-MC}
chapters/connections/outlook.tex:661:\phantomsection\label{thm:universal-MC}
 succeeded in 52ms:
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
 succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}

thinking
**Inspecting theorems**

I need to check into the universal-theta theorem since it seems crucial. There might be a situation where a full package references the wrong theorem, and it's possible that universal-theta exists and has been proven. I'm considering where to look for this information, and there's something significant around the reference number 3332 that I want to explore further. Let's see what I can find to clarify this!
exec
/bin/zsh -lc "sed -n '3300,3378p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16470,16550p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{spectral discriminant!invariance theorem|textbf}

\smallskip\noindent
\textup{[Regime: quadratic;
Convention~\ref{conv:regime-tags}.]}
Let $\cA$ be a modular Koszul chiral algebra.
The spectral discriminant
$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
depends only on the quadratic OPE data of the Koszul pair and is invariant
under Drinfeld--Sokolov reduction.
In particular, $\Delta_{\cA}$ is a separate non-scalar invariant:
it is not determined by $\kappa(\cA)$ alone.
\end{theorem}

\begin{proof}
This is Theorem~\ref{thm:ds-bar-gf-discriminant}.
\end{proof}

\begin{remark}[\texorpdfstring{$K$}{K}-theoretic hierarchy]\label{rem:spectral-characteristic-programme}
\index{spectral discriminant!K-theoretic hierarchy}
 succeeded in 52ms:
$\mathrm{Vir}_c$ &
 $\mathbf{M}$ & $\infty$ & $\infty$
 & $\frac{40}{5c{+}22}$ &
 Thm~\ref{thm:w-virasoro-quintic-forced} \\
$\mathcal{W}_N$ &
 $\mathbf{M}$ & $\infty$ & $\infty$
 & $\neq 0$ &
 \S\ref{sec:mixed-cubic-quartic-shadows} \\[6pt]
\multicolumn{6}{l}{\emph{Higher-rank lattice VOAs
 (\S\ref{sec:higher-depths}; class by $d_{\mathrm{alg}}$, cf.\
 Theorem~\ref{thm:depth-decomposition}):}} \\
$V_{\mathrm{Leech}}$ &
 $\mathbf{G}$ & $4$ & $0$ & $0$ &
 Prop~\ref{prop:leech-epstein} \\
Rank-$48$ &
 $\mathbf{G}$ & $5$ & $0$ & $0$ &
 \S\ref{sec:higher-depths} \\
Rank-$72$ &
 $\mathbf{G}$ & $6$ & $0$ & $0$ &
 \S\ref{sec:higher-depths} \\
exec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'obstruction class' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\Theta_\\cA"'^{'"\\leq' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
52:The obstruction classes
104: The obstruction classes are not independent: they satisfy
142: $\Delta \neq 0$: every obstruction class is nonzero, and the
457:whose global sections house the obstruction classes.
2701: \item \emph{Cohomological\textup{:}} The genus-$g$ obstruction class
4252:$\mathsf{C}$, the obstruction classes $o_{r+1}(\cA) = 0$
4505:with obstruction classes
5429:and write $o_g(\cA)\in W_g$ for the one-channel obstruction class.
7768: The genus-$g$ obstruction class $o_g(\cA)$ lies in the
7847:\item \emph{MC2-3}: The genus-$g$ obstruction class lies on the
8270: obstruction class of the bar complex, which measures the curvature
10683:obstruction classes~$\mathfrak{o}_{r+1}(\cA)$ in the shadow
 succeeded in 51ms:
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
94: The graph-sum formula produces $\Theta_\cA^{\leq r}$ but gives
98: (D_\cA\Theta_\cA^{\leq r}
99: + \tfrac12[\Theta_\cA^{\leq r},\Theta_\cA^{\leq r}])_{r+1}
114: construction, and $\Theta_\cA^{\leq r}$ are its degree
2193: $\Theta_\cA^{\leq r}$ exists at all finite degrees,
2195: \Theta_\cA^{\leq r}$
3898:$\Theta_\cA^{\leq N} := \pi_{\leq N}(\Theta_\cA)$ is MC
3901:$\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists as
4024:\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
4504:$\Theta_\cA^{\leq 2}, \Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},\ldots$


thinking
**Investigating theorem inconsistencies**

I'm noticing an inconsistency in the theorem's shadow archetype classification; it uses classes \mathbf{G}/L/C/M, while the theorem statement references classes \mathbf{F}_2,\mathbf{F}_3,\mathbf{F}_4,\mathbf{M}. This seems important, and I should inspect more lines to determine if the F classes are typos or if they're defined elsewhere. I definitely need to take a closer look to clarify this situation and ensure everything aligns correctly!
thinking
**Searching for definitions**

I need to look up definitions for F_2. It’s crucial I pinpoint exactly what it means since terms can vary based on context. I’m wondering if it relates to a concept in mathematics, physics, or something entirely different. Let’s explore multiple sources to find a comprehensive understanding. I want to be thorough and make sure I’m not missing anything important. It should be interesting to see the different ways the term F_2 is used!
codex
A deeper pass exposed a second-order defect: the later “Shadow archetype classification” theorem does not even name the same class family consistently inside its own statement. I’m checking whether `\mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4` is a defined synonym anywhere or just drift against `\mathbf{G}/\mathbf{L}/\mathbf{C}`.
exec
/bin/zsh -lc "rg -n -F '\\mathbf{F}_2' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbf{F}_3' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:3824:$= \mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4/\mathbf{M}$)
chapters/connections/thqg_introduction_supplement_body.tex:712:$\mathbf{F}_2=$ \textbf{G} (Gaussian)
chapters/theory/higher_genus_modular_koszul.tex:16504:exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
chapters/theory/higher_genus_modular_koszul.tex:16504:exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
 succeeded in 50ms:
chapters/connections/concordance.tex:3824:$= \mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4/\mathbf{M}$)
chapters/connections/thqg_introduction_supplement_body.tex:715:$\mathbf{F}_3=$ \textbf{L} (Lie/tree)
chapters/theory/higher_genus_modular_koszul.tex:16504:exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
chapters/theory/higher_genus_modular_koszul.tex:16504:exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
exec
/bin/zsh -lc "rg -n -F '\\mathsf{G}/\\mathsf{L}/\\mathsf{C}/\\mathsf{M}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16499,16580p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbf{F}_4' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbf{G}/\\mathbf{L}/\\mathbf{C}/\\mathbf{M}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
155: partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
17343:$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an
25687: ($\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$) \\
 succeeded in 50ms:
\label{thm:shadow-archetype-classification}
\ClaimStatusProvedHere
\index{shadow depth!classification theorem|textbf}
\index{shadow archetype classification|textbf}
Every chirally Koszul algebra in the standard landscape belongs to
exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
$\mathbf{F}_4$, or $\mathbf{M}$
\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
The class is determined by the vanishing pattern of obstruction
classes at degrees~$3$, $4$, $5$, and the assignments for the
primitive archetypes are as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
 All higher obstruction classes vanish:
 $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
 exactly quadratic.

\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
 Affine Kac--Moody $V_k(\fg)$ at generic level.
 succeeded in 51ms:
2326:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
16136: classes $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
16151:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
16256:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ thus
16291:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}/\mathbf{W}$,
16292:with $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ exhaustive
16304:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
16710:class $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ is an
16729:The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
16800: \emph{all} four classes $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
18786:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
18822:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$.
28734:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ is constant.
34030:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ are recovered from the
34139:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
34210:The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
 succeeded in 51ms:
chapters/connections/concordance.tex:3824:$= \mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4/\mathbf{M}$)
chapters/connections/concordance.tex:3831:$\mathbf{F}_4$ and $\mathbf{M}$ is structural, not empirical:
chapters/theory/higher_genus_modular_koszul.tex:16505:$\mathbf{F}_4$, or $\mathbf{M}$
chapters/theory/higher_genus_modular_koszul.tex:18655: & $\infty$ & $\mathbf{F}_4$: $r_{\max} = 4$\;${}^{**}$ \\
chapters/connections/thqg_introduction_supplement_body.tex:718:$\mathbf{F}_4=$ \textbf{C} (contact/quartic)
chapters/connections/thqg_introduction_supplement_body.tex:726:The gap between $\mathbf{F}_4$ and $\mathbf{M}$ is an empirical
chapters/theory/higher_genus_modular_koszul.tex:16505:$\mathbf{F}_4$, or $\mathbf{M}$
chapters/theory/higher_genus_modular_koszul.tex:18655: & $\infty$ & $\mathbf{F}_4$: $r_{\max} = 4$\;${}^{**}$ \\


thinking
**Evaluating notation consistency**

I'm noticing some notation drift with \mathsf, \mathbf, and F_2, which might indicate a need for a mission focus foundation audit on the first section. The user wants a file audit with checks, so I need to make sure we address any subtle notation drift. I should inspect the definition of shadow depth classification and how it relates to the theorem shadow archetype classification since they use synonyms like F_2. There seems to be an inconsistency with references and definitions that could be serious. I’ll also search for the use of \Theta shadow tower in the relevant theorem and proof sections.
thinking
**Assessing shadow tower references**

I need to determine if there are any proofs or statements regarding the shadow tower before definition at line 11885. For instance, the theorem on three-tier architecture mentions "The shadow obstruction tower Theta^{<=r} exists..." at line 2193, which references Theorem recursive-existence. This might summarize the architecture, but it’s still in a formal theorem environment before the definition. I should consider moving the theorem below the definition or replacing it with an explicit inline definition. I also want to search for other references to "shadow tower" or \Theta^{<=r} in earlier proofs, especially around lines 3870-3905.
codex
The notation drift is worse than a single forward reference. I’m seeing three competing naming schemes for the same class family inside the same chapter: `\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}`, `\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}`, and `\mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4/\mathbf{M}`. I’m now checking whether the chapter ever explicitly declares these as equivalent; if it doesn’t, that’s a formal ambiguity, not just style noise.
exec
/bin/zsh -lc "rg -n -F 'F_2=' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbf{F}_d' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:22685:% lambda=0: kappa=1, F_1=1/24, F_2=7/5760.
chapters/theory/higher_genus_modular_koszul.tex:22689:% lambda=1/2: kappa=-1/2, F_1=-1/48, F_2=-7/11520.
chapters/theory/higher_genus_modular_koszul.tex:22690:% Census (landscape_census.tex:590): F_1=-1/48, F_2=-7/11520. Matches.
chapters/theory/higher_genus_modular_koszul.tex:22691:% lambda=1: kappa=1, F_1=1/24, F_2=7/5760.
chapters/theory/higher_genus_modular_koszul.tex:22692:% Census (landscape_census.tex:588): F_1=1/24, F_2=7/5760. Matches.
chapters/theory/higher_genus_modular_koszul.tex:22685:% lambda=0: kappa=1, F_1=1/24, F_2=7/5760.
chapters/theory/higher_genus_modular_koszul.tex:22689:% lambda=1/2: kappa=-1/2, F_1=-1/48, F_2=-7/11520.
chapters/theory/higher_genus_modular_koszul.tex:22690:% Census (landscape_census.tex:590): F_1=-1/48, F_2=-7/11520. Matches.
chapters/theory/higher_genus_modular_koszul.tex:22691:% lambda=1: kappa=1, F_1=1/24, F_2=7/5760.
chapters/theory/higher_genus_modular_koszul.tex:22692:% Census (landscape_census.tex:588): F_1=1/24, F_2=7/5760. Matches.
 succeeded in 51ms:
chapters/connections/arithmetic_shadows.tex:76:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d/\mathbf{M}$
chapters/connections/arithmetic_shadows.tex:1350:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d/\mathbf{M}$
chapters/connections/arithmetic_shadows.tex:1354:$\mathbf{F}_d$ classes correspond to lattices whose theta
chapters/theory/higher_genus_modular_koszul.tex:16567:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
chapters/theory/higher_genus_modular_koszul.tex:16567:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{F}_d$\textup{)} to
exec
/bin/zsh -lc "sed -n '18635,18675p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3868,3915p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$V_\Lambda$ & $\operatorname{rank}(\Lambda)$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{G}$: $r_{\max} = 2$ \\
Free fermion & $\frac{1}{2}$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{G}$: $r_{\max} = 2$ \\[4pt]
$\hat{\fg}_k$ (generic) & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\neq 0$ & $0$ & $0$
 & $\infty$ & $\mathbf{L}$: $r_{\max} = 3$ \\[4pt]
$\beta\gamma$ & --- & --- & --- & ---
 & --- & $\mathbf{C}$: $r_{\max} = 4$\;${}^*$ \\[4pt]
$\mathrm{Vir}_c$ & $\frac{c}{2}$ & $2$
 & $\frac{10}{c(5c{+}22)}$
 & $\frac{40}{5c{+}22}$
 & $c\sqrt{\frac{5c{+}22}{180c{+}872}}$
 & $\mathbf{M}$: $r_{\max} = \infty$ \\[4pt]
$\mathcal{W}_N$ ($N \geq 3$)
 & $\frac{c}{2}$ (T-line)
 & $2$ & $\frac{10}{c(5c{+}22)}$ & $\frac{40}{5c{+}22}$
 & (T-line)
 & $\mathbf{M}$: $r_{\max} = \infty$ \\[4pt]
$V_{\mathrm{Leech}}$ & $24$ & $0$ & $0$ & $0$
exec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathbf{G}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<16191' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathbf{F}_2' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 and the identity $D_\cA^2 = 0$
 (Theorem~\ref{thm:prism-higher-genus},
 Lemma~\ref{lem:stable-graph-d-squared}).
\item \emph{Convolution dg~Lie algebra}
 (Definition~\ref{def:modular-convolution-dg-lie},
 Theorem~\ref{thm:convolution-dg-lie-structure},
 Construction~\ref{const:explicit-convolution-bracket}):
 the coderivation algebra carries a strict dg~Lie structure
 whose bracket is the graded commutator.
 The identity $D^2 = 0$ on $\gAmod$ is
 Theorem~\ref{thm:convolution-d-squared-zero}.
\item \emph{Weight filtration and pronilpotent completion}
 (Definition~\ref{def:weight-filtration-tower},
 Proposition~\ref{prop:geometric-modular-operadic-mc}):
 $\widehat{\gAmod}$ is the inverse limit of
 finite-dimensional quotients $\gAmod/F^{N+1}$, and
 $\Theta_\cA$ converges in the completed space.
\item \emph{Centrality of genus-$g$ curvature}
 (Proposition~\ref{prop:curvature-centrality-general}):
 no conditional simple-Lie-symmetry hypothesis is needed,
 succeeded in 52ms:
2326:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
11988:the four shadow depth classes $\mathbf{G}$, $\mathbf{L}$,
12001:$\mathbf{G}$ & $2$ & $S_2$ only & Heisenberg &
12012:Class~$\mathbf{G}$ is the Brown--Henneaux regime: the leading
12072: {$\mathbf{G}$: Heis, $r_{\max}\!=\!2$};
12101:archetypes terminate at their respective depths: class~$\mathbf{G}$
14687: & $\mathbf{G}$ & $2$
14691: & $\mathbf{G}$ & $2$
14736:$\mathbf{G}$ & $2$
14808:$\Delta(\cH_k) = 0$ and the tower terminates at degree~$2$ (class~$\mathbf{G}$).
14822:$\mathbf{G}$~(depth~$2$: both $\kappa$ and $S_4$ contribute, but the
14831:structural constraint: class~$\mathbf{G}$ because commutativity kills
15538: Heisenberg & $0$ & $0$ & $0$ & $\mathbf{G}$ &
15698:For classes $\mathbf{G}$, $\mathbf{L}$, and $\mathbf{C}$,
15818: terminates (classes $\mathbf{G}$ and $\mathbf{L}$).
15917: $\mathbf{G}$ \textup{(}Heisenberg\textup{)} &
15976:Classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$: the
16034:when $\Delta \leq 0$, which forces class~$\mathbf{G}$
16083:coefficients. Classes $\mathbf{G}$ and $\mathbf{L}$
16136: classes $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 succeeded in 51ms:


thinking
**Inspecting definitions**

I'm noticing I need to check around entry 11988 for the shadow-postnikov-tower definition, which possibly includes a table of classes. Oh, but I should also consider whether the definition at 11885 actually defines classes earlier than 16191. I feel like I should read through the entries from 11885 to 12020 because it could significantly affect my findings. Let's take a careful look at that!
codex
The chapter has an earlier local classification surface around the shadow tower section too, so I’m checking whether that earlier table already defines the classes or whether it only summarizes them. The distinction matters because “appears in a table” is not the same thing as being formally introduced before later proofs use it.
exec
/bin/zsh -lc "sed -n '12035,12125p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11870,12035p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 rounded corners=2pt, font=\footnotesize]
 (L2) at (0,0) {$\Theta^{\leq 2}\!:\; \kappa(\cA)$};
\node[draw, thick, minimum width=2.8cm, minimum height=0.55cm,
 rounded corners=2pt, font=\footnotesize]
 (L3) at (0,1.2) {$\Theta^{\leq 3}\!:\; \mathfrak{C}(\cA)$};
\node[draw, thick, minimum width=2.8cm, minimum height=0.55cm,
 rounded corners=2pt, font=\footnotesize]
 (L4) at (0,2.4) {$\Theta^{\leq 4}\!:\; \mathfrak{Q}(\cA)$};
\node[draw, thick, minimum width=2.8cm, minimum height=0.55cm,
 rounded corners=2pt, font=\footnotesize]
 (L5) at (0,3.6) {$\Theta^{\leq 5}$};
\node[font=\footnotesize] at (0,4.4) {$\vdots$};
\node[draw, thick, minimum width=2.8cm, minimum height=0.55cm,
 rounded corners=2pt, font=\footnotesize]
 (Linf) at (0,5.2)
 {$\Theta_{\cA} = \varprojlim\Theta^{\leq r}$};
%
% ---- Vertical arrows ----
\draw[maparrow] (L3.south) -- (L2.north);
\draw[maparrow] (L4.south) -- (L3.north);
 succeeded in 51ms:
\label{def:extension-tower}
The \emph{modular extension tower} of $\cA$ is the inverse system
\begin{equation}
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
exec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathbf{C}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathbf{L}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathbf{M}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
507:$\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})$
509:$\mathbf{C}_g \simeq \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$,
511:\colon \mathbf{C}_g \to \mathbf{C}_g)$ and
2326:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
5576:$C_g$ for $\mathbf{C}_g(\cA)$ with strict involution $\sigma$,
5943:\mathbf{C}_g^{\mathrm{corr}} := \operatorname{span}(R_g),
5945:\mathbf{C}_g^{!,\mathrm{corr}} := \operatorname{span}(R_g^!),
5949:\mathbf{D}_g := \mathbb{C}\delta_g \oplus \mathbf{C}_g^{\mathrm{corr}},
5951:\mathbf{D}_g^! := \mathbb{C}\delta_g^! \oplus \mathbf{C}_g^{!,\mathrm{corr}},
5961: l_1\bigl(\mathbf{C}_g^{\mathrm{corr}}\bigr)
5962: \subset \mathbf{C}_g^{\mathrm{corr}},
5964: l_1\bigl(\mathbf{C}_g^{!,\mathrm{corr}}\bigr)
5965: \subset \mathbf{C}_g^{!,\mathrm{corr}};
6023:$\mathbf{C}_g^{\mathrm{corr}}$ and
6024:$\mathbf{C}_g^{!,\mathrm{corr}}$ are finite-dimensional. Therefore
6026:\mathbf{D}_g = \mathbb{C}\delta_g \oplus \mathbf{C}_g^{\mathrm{corr}},
6028:\mathbf{D}_g^! = \mathbb{C}\delta_g^! \oplus \mathbf{C}_g^{!,\mathrm{corr}}
 succeeded in 51ms:
2326:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
5599: $\mathbf{L}_g \subset C_g^+$ and
5600: $\mathbf{L}_g^! \subset C_g^-$ such that:
5604: H^*(\mathbf{L}_g) = L_g,
5606: H^*(\mathbf{L}_g^!) = L_g^!;
5610: \langle \mathbf{L}_g,\mathbf{L}_g\rangle_{\mathbb{D}} = 0,
5612: \langle \mathbf{L}_g^!,\mathbf{L}_g^!\rangle_{\mathbb{D}} = 0;
5616: \mathbf{L}_g
5618: (\mathbf{L}_g^!)^\vee[-(3g{-}3)],
5620: \mathbf{L}_g^!
5622: (\mathbf{L}_g)^\vee[-(3g{-}3)].
5636:\mathbf{L}_g := E_g^{\bullet,+},
5638:\mathbf{L}_g^! := E_g^{\bullet,-}.
5665:E_g^\bullet \;:=\; \mathbf{L}_g \oplus \mathbf{L}_g^!
5669:exactly $\mathbf{L}_g$ and $\mathbf{L}_g^!$.
5678:$x,x' \in \mathbf{L}_g$ and $y,y' \in \mathbf{L}_g^!$, the projector
5773:\mathbf{L}_g := \mathbf{D}_g \,\widehat{\otimes}\, \mathbf{T}_g^\bullet
5776:\mathbf{L}_g^! := \mathbf{D}_g^! \,\widehat{\otimes}\, \mathbf{T}_g^\bullet
5783:H^*(\mathbf{L}_g)=L_g,
5785:H^*(\mathbf{L}_g^!)=L_g^!.
 succeeded in 51ms:
2326:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
exec
/bin/zsh -lc "sed -n '3990,4045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
\index{logical foundation!non-circular chain}
The bar-intrinsic construction partitions the five main
theorems into two tiers by logical prerequisites.

\smallskip\noindent
\emph{Tier~1: unconditional consequences of~$D_\cA^2 = 0$.}
The MC element
exec
/bin/zsh -lc "sed -n '4485,4525p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'shadow obstruction tower' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10390,10430p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'Definition~\\ref{def:shadow-postnikov-tower}' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<11885' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\Theta_\\cA"'^{'"\\leq' | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Part~(f) is the family index theorem
(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
because
$\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
pushed forward to $\overline{\mathcal{M}}_g$, produces the
$\hat{A}$-class by Mumford's formula.
\end{proof}

\begin{remark}[Scope of Theorem~\ref{thm:explicit-theta}]
\label{rem:explicit-theta-scope}
\index{universal Maurer--Cartan class!scope}
The minimal model holds for KM
(Corollary~\ref{cor:km-minimal-linf}) and extends to
$\mathcal{W}$-algebras via DS functoriality. For VOAs
with $\dim H^2_{\mathrm{cyc}}\geq 2$, scalar saturation
is conditional;
see Conjecture~\ref{conj:scalar-saturation-universality}.
In the multi-channel regime, the correct framework is the
shadow obstruction tower
$\Theta_\cA^{\leq 2}, \Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},\ldots$
 succeeded in 51ms:
(Theorem~\ref{thm:non-renormalization-tree}) follows: tree-level
operations are exact because $L_\infty$ transfer preserves MC
elements, and loop corrections are absorbed into the genus-raising
BV operator~$\Delta$.
\end{remark}

\begin{remark}[The two Maurer--Cartan equations]
\label{rem:two-mc-equations}
\index{Maurer--Cartan equation!strict vs $L_\infty$}
The universal MC element $\Theta_\cA$ satisfies two forms of the
Maurer--Cartan equation, one in each layer of the two-level
convention (Remark~\ref{rem:two-level-convention}).

\emph{Strict form.} In the dg~Lie model
$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
(Definition~\ref{def:modular-convolution-dg-lie}):
\begin{equation}\label{eq:strict-mc}
D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0,
\end{equation}
where $D = \ell_1^{(0)}$ and $[-,-] = \ell_2^{(0)}$ are the only
 succeeded in 51ms:
151: genus-$0$ shadow obstruction tower coincides with the
2072:\text{Thm D, shadow obstruction tower}
2192:\item The shadow obstruction tower
2560:$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
2659:(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
3895:The shadow obstruction tower convergence
4024:\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
4503:shadow obstruction tower
7991:shadow obstruction tower and by the spectral/periodic invariants.
9793:uniform-weight lane; the non-scalar shadow obstruction tower
9823:convolution dg~Lie algebra together with its shadow obstruction tower
10458: The shadow obstruction tower measures the
10730:the shadow obstruction tower ($o^{(r)}_{\mathrm{Vir}}\neq 0$ for all
10826:\item The full shadow obstruction tower
10927:%% algebra, E₁ shadow obstruction tower, and the five main theorems
11794:\subsection{The shadow obstruction tower}
 succeeded in 51ms:
101: (Definition~\ref{def:shadow-postnikov-tower}).
2660:(Definition~\ref{def:shadow-postnikov-tower};
3522:Definition~\ref{def:shadow-postnikov-tower}.
9824:(Definition~\ref{def:shadow-postnikov-tower}).
 succeeded in 51ms:
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
94: The graph-sum formula produces $\Theta_\cA^{\leq r}$ but gives
98: (D_\cA\Theta_\cA^{\leq r}
99: + \tfrac12[\Theta_\cA^{\leq r},\Theta_\cA^{\leq r}])_{r+1}
114: construction, and $\Theta_\cA^{\leq r}$ are its degree
2193: $\Theta_\cA^{\leq r}$ exists at all finite degrees,
2195: \Theta_\cA^{\leq r}$
3898:$\Theta_\cA^{\leq N} := \pi_{\leq N}(\Theta_\cA)$ is MC
3901:$\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists as
4024:\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
4504:$\Theta_\cA^{\leq 2}, \Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},\ldots$




thinking
**Finding proof details**

I’m realizing that a proof actually employs the MC equation even before there's a formal theorem statement or definition. That feels like an interesting and important finding! I should pay attention to specific lines, perhaps lines 3367-3371, to look for more insights or clarification on this. It’s nice when I can uncover nuances like this while going through the material!
thinking
**Examining theorem references**

I’m considering whether cross-referencing external theorem labels from a theoretical chapter is okay. There’s a potential issue since the label `thm:master-theta` is missing in this file, which could lead to confusion. I need to inspect line 2480 more thoroughly, as it uses `thm:universal-theta` and mentions something about simple Lie symmetry concerning the theorem `mc2-bar-intrinsic`. Wait, I realize that the parenthetical is misleading—`mc2-bar-intrinsic` actually states there’s no restriction to simple Lie symmetry.
thinking
**Considering audit definitions**

I notice that `g^{mod}` is defined later, and that `g^{E1}` isn't defined in this file. The opening uses the symmetric shadow first, which could lead to identifying the risk level as either HIGH or CRITICAL. Since the mission relates to a foundational audit, it seems logical to consider it HIGH due to a potential structural foundation mismatch, rather than labeling it as a false theorem. It's all about getting these definitions clear!
thinking
**Considering homotopy invariance**

I'm thinking about how the theorem uses `\gAmod` right before the definition. It mentions a "strict model of homotopy invariant L∞-algebra \Definfmod," which refers to a later subsection. I could potentially note this point because it helps clarify the relationship within the theorem and the definition. There’s a lot to unpack here, and I want to make sure I’m considering all aspects accurately!
codex
A more subtle object-conflation check is now in play: the shadow tower definition is phrased in the ambient algebra `\mathfrak g^{amb}_\cA/F^{r+1}`, while the surrounding prose often states the truncations in `\gAmod/F^{r+1}`. If the file never states the comparison map or identification before switching notation, that’s not harmless shorthand; it’s a hidden change of object.
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb}}_\\cA' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ambient modular complementarity algebra' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'label{def:ambient' chapters/theory/higher_genus_modular_koszul.tex chapters/**/*.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
30405:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
30668:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
30922:\mathfrak{g}^{\mathrm{amb}}_\cA.
 succeeded in 51ms:

 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:5256:\label{def:ambient-tangent-complex}
chapters/theory/higher_genus_complementarity.tex:4761:\label{def:ambient-complementarity-datum}
chapters/theory/higher_genus_complementarity.tex:4797:\label{def:ambient-complementarity-tangent-complex}
chapters/theory/higher_genus_modular_koszul.tex:30273:\label{def:ambient-master-equation}
chapters/theory/higher_genus_modular_koszul.tex:30439:\label{def:ambient-modular-complementarity-algebra}
chapters/theory/higher_genus_modular_koszul.tex:30273:\label{def:ambient-master-equation}
chapters/theory/higher_genus_modular_koszul.tex:30439:\label{def:ambient-modular-complementarity-algebra}
exec
/bin/zsh -lc "sed -n '11790,11895p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30430,30475p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
sequence operates \emph{within} each genus stratum, while the genus
spectral sequence operates \emph{across} strata.
\end{remark}

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
 succeeded in 52ms:
\end{remark}

\subsection{The carrier algebra}
\label{subsec:carrier-algebra}

The graph sum~\eqref{eq:modular-bar-hamiltonian} lives in a specific
graded vector space.

\begin{definition}[Ambient modular complementarity algebra]
\label{def:ambient-modular-complementarity-algebra}
The \emph{carrier} for the modular bar--Hamiltonian is the filtered
completed graded vector space
\begin{equation}
\label{eq:ambient-modular-complementarity-algebra}
\mathfrak{g}^{\mathrm{amb}}_{\cA}
:=
\bigl(L_{\cA} \oplus K_{\cA} \oplus L_{\cA^!}\bigr)
\widehat\otimes \mathbb{G}_{\mathrm{st}}
\widehat\otimes \mathbb{G}_{\mathrm{pf}},
\end{equation}

thinking
**Evaluating definitions**

I need to determine whether the definition is referring to ambient or modular. Since it opens at 11794 with "weight filtration on modular convolution algebra" and defines `F^N\mathfrak g^{amb}_A`, it seems inconsistent since it doesn't mention `\gAmod`. That feels like it could be a significant finding. I should gather more context around 11794 and again at 30439. I wonder if `g^{amb}` differs from `g^{mod}`; a comparison might be necessary. I’ll search for their relation later.
codex
The file has a genuine carrier-object drift: the shadow tower section announces a filtration on the “modular convolution algebra” but then immediately defines the filtration on `\mathfrak g^{amb}_\cA`, whose actual definition does not appear until line 30439. I’m now checking whether the chapter ever states a comparison map between `\mathfrak g^{amb}_\cA` and `\mathfrak g^{mod}_\cA`; without that, the tower’s carrier is not even stable across sections.
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb}}_\\cA' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{g}_{\\cA}"'^{'"\\mathrm{mod}}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
30405:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
30668:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
30922:\mathfrak{g}^{\mathrm{amb}}_\cA.
 succeeded in 51ms:
9846:\mathfrak{g}_{\cA}^{\mathrm{mod}}
9887:The dg~Lie algebra $\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is a strict
9910:$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is as follows:
9938: $\alpha \in \mathfrak{g}_{\cA}^{\mathrm{mod}}(g_1,n_1)$ and
9939: $\beta \in \mathfrak{g}_{\cA}^{\mathrm{mod}}(g_2,n_2)$,
10046:An element $\alpha \in \mathfrak{g}_{\cA}^{\mathrm{mod}}$ is a
10052:$\alpha \in \mathfrak{g}_{\cA}^{\mathrm{mod}}(g_1,n_1)$ and
10053:$\beta \in \mathfrak{g}_{\cA}^{\mathrm{mod}}(g_2,n_2)$,
10055:$\mathfrak{g}_{\cA}^{\mathrm{mod}}(g_1+g_2,\, n_1+n_2-2)$ and is
10404:$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
10500:$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ of
10614:$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ of
10624:representative $\mathfrak{g}_{\cA}^{\mathrm{mod}}$, not only a
10743:\item $\mathfrak{g}_{\cA}^{\mathrm{mod}} =
14407:$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is the
14418:\item Define $\mathfrak{g}_{\cA}^{\mathrm{mod}}$ from the modular
14422: the dg~Lie algebra $\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is its
14458:\operatorname{MC}(\mathfrak{g}_{\cA}^{\mathrm{mod}})
14461:\alpha \in (\mathfrak{g}_{\cA}^{\mathrm{mod}})^1
15168:$\mathfrak{g}_{\cA}^{\mathrm{mod},(0)} := \mathfrak{g}_{\cA}^{\mathrm{mod}} \otimes \mathsf{G}^{(0)}$,
exec
/bin/zsh -lc "rg -n -e 'ambient.*modular convolution' -e 'comparison.*g\\"'^'"\\{amb\\}.*g\\"'^'"\\{mod\\}' -e 'projection.*g\\"'^'"\\{amb\\}.*g\\"'^'"\\{mod\\}' -e 'strict model.*ambient' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11794,11860p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30380,30450p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
shadows at degrees~$\leq r$: whether the tower can be truncated at
 exited 1 in 52ms:

 succeeded in 51ms:
\begin{remark}[MC elements in convolution algebras for factorization algebras]
\label{rem:chriss-ginzburg-philosophy}
\index{Chriss--Ginzburg structure principle!factorization algebra interpretation}
Master objects are defined directly as
Maurer--Cartan elements in convolution homotopy Lie algebras. At
the dg~level the governing equation is
$D_{\cA}\Theta_{\cA} + \tfrac12[\Theta_{\cA},\Theta_{\cA}] = 0$;
at the full homotopy level the ambient algebra
$\mathfrak{g}_\cA^{\mathrm{amb}}$ carries a quantum
$L_\infty$-structure
(Theorem~\ref{thm:modular-quantum-linfty}), and the
Maurer--Cartan equation becomes
$\sum_{n \geq 1}\tfrac{1}{n!}\,\ell_n^{(0)}(\Theta,\dots,\Theta)
+ \sum_{g \geq 1}\hbar^{2g}\,\ell_1^{(g)}(\Theta) = 0$,
where $\ell_n^{(0)}$ are the operadic higher brackets from
Loday--Vallette~\cite[Thm~10.3.8]{LV12} and $\ell_1^{(g)}$ are
the genus-$g$ BV operators. The dg~equation is the leading-order
truncation; the full quantum $L_\infty$ equation encodes all
higher Feynman amplitudes.
At the scalar level (where the shadow obstruction tower


thinking
**Evaluating mathematical definitions**

There seems to be no direct comparison, which is a significant problem. I need to check if `\mathfrak g^{amb}` appears anywhere before line 11794 through macro definitions. It looks like earlier lines only show later results because the fixed string shows different outputs. The ambient definition at line 30439 needs moving. Either I should reposition the "Ambient modular complementarity algebra" definition or adjust how subsequent lines reference it to ensure clarity and correctness. This fix seems critical.
thinking
**Examining notation consistency**

I need to check if `\Theta_\cA^{\leq 2} = \kappa(\cA)` defines whether a scalar is used as an element versus a tower level. I'm not sure if that's formal, but I might not even need that detail. I should also look at the shadow tower definition to see if it relies on `Definition\ref{def:vol1-rigid-planted-forest-depth-filtration}`, though that might not matter. However, there's definitely a mismatch in the theorem `thm:shadow-archetype-classification` since it uses different notations than `def:shadow-depth-classification`. This seems important! I'll need to unify the notation across both definitions.
codex
The shadow tower section itself may be internally unstable: its obstruction class lands in `H^2(\cA^{sh}_{r+1,0})`, but the “shadow algebra” carrying those graded pieces is only defined later. I’m checking first-use lines now so I can separate a bad carrier reference from a bad codomain reference.
exec
/bin/zsh -lc "rg -n -F '\\cA"'^{'"\\mathrm{sh}}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
53:$o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
78: $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
81: whose components $\cA^{\mathrm{sh}}_{r,g}$ receive the
100: \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
2198: $\cA^{\mathrm{sh}} =
3978: \in \cA^{\mathrm{sh}}_{r,\bullet}$
3992:component of $\cA^{\mathrm{sh}} =
4095: $f_*^{\mathrm{sh}}\colon \cA^{\mathrm{sh}} \to
10822: $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
10842:of $\cA^{\mathrm{sh}}$. Part~(iv) is the Deligne--Getzler--Hinich
11916:H^2\bigl(\cA^{\mathrm{sh}}_{r+1,0}\bigr)
11953:= \cA^{\mathrm{sh}}_{r,0}$ is the order-$r$ correction to this
12124:$\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
12132:$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
12134:computed in $\cA^{\mathrm{sh}}$ rather than in the ambient
12148:\cA^{\mathrm{sh}}
12157:this gives a graded Lie bracket on~$\cA^{\mathrm{sh}}$ that
12169:\cA^{\mathrm{sh}}
12172:\cA^{\mathrm{sh}}_{r,g}.
12176:\item $\kappa(\cA) = \cA^{\mathrm{sh}}_{2,0}$
exec
/bin/zsh -lc "sed -n '12130,12180p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<12138' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'shadow algebra' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<12138' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\cA"'^{'"\\mathrm{sh}}' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathfrak{C}$, $\mathfrak{Q}$) is a projection to a specific
bigraded component. Second, the descended Lie bracket on
$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
$o_{r+1}(\cA)$ is a bracket of shadows at degrees~$\leq r$,
computed in $\cA^{\mathrm{sh}}$ rather than in the ambient
infinite-dimensional algebra. The tower provides existence;
the shadow algebra provides computability.

\begin{definition}[Shadow algebra]
\label{def:shadow-algebra}
\ClaimStatusProvedHere
\index{shadow algebra|textbf}
\index{modular characteristic!shadow algebra}
For a chiral algebra $\cA$ with modular cyclic deformation complex
$\Defcyc^{\mathrm{mod}}(\cA)$, the \emph{shadow algebra} is the
cohomology
\begin{equation}
\label{eq:shadow-algebra}
\cA^{\mathrm{sh}}
:=
 succeeded in 50ms:
85: The shadow algebra records \emph{what} the projections are;
2197:\item The shadow algebra
3979: \textup{(}the degree-$r$ component of the shadow algebra,
4094:\item $f_*$ descends to a morphism of shadow algebras
4104:$f_*^{\mathrm{sh}}$ is an isomorphism of shadow algebras,
10803:\begin{theorem}[Homotopy invariance of the shadow algebra;
10806:\index{shadow algebra!homotopy invariance|textbf}
10807:\index{homotopy invariance!shadow algebra}
10821:\item The shadow algebra
10837:(Robert-Nicoud--Wierstra~\cite[Section~8]{RNW19}). The shadow algebra is
10885: of~$\cA$. The shadow algebra and all its invariants
12123:bracket; the \emph{shadow algebra}
12127:The shadow algebra does two things that the tower alone does not.
12136:the shadow algebra provides computability.
 succeeded in 50ms:
53:$o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
78: $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
81: whose components $\cA^{\mathrm{sh}}_{r,g}$ receive the
100: \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$
2198: $\cA^{\mathrm{sh}} =
3978: \in \cA^{\mathrm{sh}}_{r,\bullet}$
3992:component of $\cA^{\mathrm{sh}} =
4095: $f_*^{\mathrm{sh}}\colon \cA^{\mathrm{sh}} \to
10822: $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
10842:of $\cA^{\mathrm{sh}}$. Part~(iv) is the Deligne--Getzler--Hinich
11916:H^2\bigl(\cA^{\mathrm{sh}}_{r+1,0}\bigr)
11953:= \cA^{\mathrm{sh}}_{r,0}$ is the order-$r$ correction to this
12124:$\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
12132:$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
12134:computed in $\cA^{\mathrm{sh}}$ rather than in the ambient
exec
/bin/zsh -lc "sed -n '10795,10845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<12138' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'Homotopy invariance of the shadow algebra' -A 20 -B 2" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Part~(v) is Robert-Nicoud--Wierstra~\cite[Thm~5.1]{RNW19}
with explicit components from the homotopy transfer
theorem; the strict model has $\ell_n = 0$ for $n \geq 3$,
so $\varphi_2 = 0$ and the first nontrivial component
$\varphi_3$ is determined by the contracting homotopy.
Part~(vi) is \cite[Theorem~6.6]{RNW19}.
\end{proof}

\begin{theorem}[Homotopy invariance of the shadow algebra;
\ClaimStatusProvedElsewhere]
\label{thm:shadow-homotopy-invariance}
\index{shadow algebra!homotopy invariance|textbf}
\index{homotopy invariance!shadow algebra}
Let $f\colon \cA \xrightarrow{\sim} \cA'$ be an
$\infty_\alpha$-quasi-isomorphism of chiral algebras. Then
the induced map on convolution $sL_\infty$-algebras
\[
f_*\colon
\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA)
\;\xrightarrow{\;\sim\;}
 succeeded in 52ms:
10801-\end{proof}
10802-
10803:\begin{theorem}[Homotopy invariance of the shadow algebra;
10804-\ClaimStatusProvedElsewhere]
10805-\label{thm:shadow-homotopy-invariance}
10806-\index{shadow algebra!homotopy invariance|textbf}
10807-\index{homotopy invariance!shadow algebra}
10808-Let $f\colon \cA \xrightarrow{\sim} \cA'$ be an
10809-$\infty_\alpha$-quasi-isomorphism of chiral algebras. Then
10810-the induced map on convolution $sL_\infty$-algebras
10811-\[
10812-f_*\colon
10813-\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA)
10814-\;\xrightarrow{\;\sim\;}
10815-\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA')
10816-\]
10817-is an $\infty_\alpha$-quasi-isomorphism, and the induced map on
10818-Maurer--Cartan $\infty$-groupoids is a weak homotopy equivalence.
10819-In particular:
10820-\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "awk 'NR<9837' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathfrak{g}_{\\cA}"'^{'"\\mathrm{mod}}' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR<30439' chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\mathfrak{g}"'^{'"\\mathrm{amb}}_{\\cA}' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 51ms:
11849:F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
11851:\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
11877:\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
11903:$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$,
30353:\in \operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA})$
30362:\operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA}).
30366:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ by $\Theta_{\cA}$; the genus
codex
I have the main defect candidates. I’m pulling exact numbered excerpts now so the final findings can cite precise lines and propose line-local fixes instead of vague rewrites.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30,70p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '125,190p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   140	 depth~$4$ (class~$\mathsf{C}$, contact).
   141	
   142	 $\Delta \neq 0$: every obstruction class is nonzero, and the
   143	 tower has depth~$\infty$
   144	 (class~$\mathsf{M}$, mixed).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9837,9895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4208,4258p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3332,3374p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2184,2202p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2184	\smallskip\noindent
  2185	\textbf{Tier~0} \textup{(topological input:
  2186	$D_\cA^2 = 0$)}.
  2187	\begin{enumerate}[label=\textup{(0.\arabic*)}]
  2188	\item The universal MC element
  2189	 $\Theta_\cA := D_\cA - \dzero
  2190	 \in \MC(\gAmod)$ exists at all genera
  2191	 \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
  2192	\item The shadow obstruction tower
  2193	 $\Theta_\cA^{\leq r}$ exists at all finite degrees,
  2194	 with $\Theta_\cA = \varprojlim_r
  2195	 \Theta_\cA^{\leq r}$
  2196	 \textup{(Theorem~\ref{thm:recursive-existence})}.
  2197	\item The shadow algebra
  2198	 $\cA^{\mathrm{sh}} =
  2199	 H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
  2200	 a graded Lie bracket with
  2201	 projections $\kappa$, $\Delta$,
  2202	 $\mathfrak{C}$, $\mathfrak{Q}$
 succeeded in 52ms:
  4208	 to~$V^-$, so only bipartite graphs survive the
  4209	 contraction. This is the homological perturbation lemma
  4210	 applied to the Lagrangian splitting.
  4211	\item \emph{Depth termination.}
  4212	 For finite-depth algebras (classes $\mathsf{G}$, $\mathsf{L}$,
  4213	 $\mathsf{C}$), the truncation
  4214	 $\boldsymbol\Theta^{\pm}_{\leq r_{\max}}
  4215	 = \boldsymbol\Theta^{\pm}$ is exact and the tree-level
  4216	 $L_\infty$-algebra is formal
  4217	 (Proposition~\textup{\ref{prop:shadow-formality-low-degree}}).
  4218	 For class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$), the
  4219	 bipartite tower is infinite and receives contributions at
  4220	 every degree.
  4221	\end{enumerate}
  4222	\end{theorem}
  4223	
  4224	\begin{proof}
  4225	The Lagrangian decomposition
  4226	$V_\cA = V^+ \oplus V^-$ with
  4227	$\omega_\cA|_{V^\pm} = 0$ determines a homotopy retract
 succeeded in 52ms:
  9837	\begin{definition}[Modular convolution dg~Lie algebra]
  9838	\label{def:modular-convolution-dg-lie}
  9839	Let $\cA$ be a cyclic chiral algebra on a smooth projective curve~$X$.
  9840	The following dg~Lie algebra is the strict model of the modular
  9841	quantum $L_\infty$-algebra of
  9842	Theorem~\ref{thm:modular-homotopy-convolution}.
  9843	The \emph{modular convolution dg~Lie algebra} is
  9844	\begin{equation}
  9845	\label{eq:modular-convolution}
  9846	\mathfrak{g}_{\cA}^{\mathrm{mod}}
  9847	\;:=\;
  9848	\prod_{\substack{g,n \\ 2g-2+n > 0}}
  9849	\operatorname{Hom}_{\Sigma_n}\!\bigl(
  9850	C_*(\overline{\mathcal{M}}_{g,n}),\,
  9851	\operatorname{End}_{\cA}(n)
  9852	\bigr),
  9853	\end{equation}
  9854	where $C_*(\overline{\mathcal{M}}_{g,n})$ is the chain complex of
  9855	the Deligne--Mumford moduli space and
  9856	$\operatorname{End}_{\cA}(n) = \operatorname{Hom}(\cA^{\otimes n}, \cA)$
 succeeded in 52ms:
  3332	\label{thm:universal-theta}
  3333	\index{universal Maurer--Cartan class|textbf}
  3334	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3335	projective curve~$X$ with non-degenerate invariant form,
  3336	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3337	universal Maurer--Cartan class
  3338	\[
  3339	\Theta_{\cA} \in
  3340	\operatorname{MC}\!\bigl(
  3341	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3342	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3343	\bigr)
  3344	\]
  3345	such that:
  3346	\begin{enumerate}[label=\textup{(\roman*)}]
  3347	\item the genus-$1$ component of its scalar trace is
  3348	 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
  3349	 the full scalar trace is
  3350	 $\operatorname{tr}(\Theta_{\cA})
  3351	 = \sum_{g \geq 1} \kappa(\cA) \lambda_g$;
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11794,11925p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12120,12165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16190,16245p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 11794	\subsection{The shadow obstruction tower}
 11795	\label{subsec:shadow-postnikov-tower}
 11796	
 11797	%% DEFICIENCY OPENING: what does the tower structure reveal
 11798	%% that individual shadows do not?
 11799	
 11800	The MC element $\Theta_\cA = D_\cA - d_0$ satisfies
 11801	$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ by
 11802	construction. Its degree-$2$ projection is the scalar
 11803	$\kappa(\cA)$; its degree-$3$ projection is the cubic
 11804	shadow~$\mathfrak{C}(\cA)$; its degree-$4$ projection is the quartic
 11805	resonance class~$\mathfrak{Q}(\cA)$. Each projection is a useful
 11806	invariant in isolation. The question is: what structure do the
 11807	projections carry \emph{collectively} that none of them carries alone?
 11808	
 11809	The answer is that $\Theta_\cA$ is not a list of invariants but an
 11810	inverse-limit element in a filtered pronilpotent Lie algebra, and the
 11811	MC equation couples the projections across degrees. The obstruction
 11812	class $o_{r+1}(\cA)$ at degree~$r{+}1$ is a Lie bracket of the
 11813	shadows at degrees~$\leq r$: whether the tower can be truncated at
 succeeded in 52ms:
 12120	deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$, the strict model
 12121	of $\Definfmod(\cA)$
 12122	(Remark~\ref{rem:modular-cyc-strictification}), carries an $L_\infty$
 12123	bracket; the \emph{shadow algebra}
 12124	$\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is
 12125	the cohomology with its descended graded Lie bracket.
 12126	
 12127	The shadow algebra does two things that the tower alone does not.
 12128	First, it decomposes the MC element $\Theta_\cA$ into components
 12129	graded by degree and genus, so that each named shadow ($\kappa$,
 12130	$\mathfrak{C}$, $\mathfrak{Q}$) is a projection to a specific
 12131	bigraded component. Second, the descended Lie bracket on
 12132	$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
 12133	$o_{r+1}(\cA)$ is a bracket of shadows at degrees~$\leq r$,
 12134	computed in $\cA^{\mathrm{sh}}$ rather than in the ambient
 12135	infinite-dimensional algebra. The tower provides existence;
 12136	the shadow algebra provides computability.
 12137	
 12138	\begin{definition}[Shadow algebra]
 12139	\label{def:shadow-algebra}
 succeeded in 52ms:
 16190	
 16191	\begin{definition}[Shadow depth classification]
 16192	\label{def:shadow-depth-classification}
 16193	\ClaimStatusProvedHere
 16194	\index{shadow depth|textbf}
 16195	\index{shadow depth!classification}
 16196	\index{shadow obstruction tower!depth classification}
 16197	Let $\cA$ be a modular Koszul chiral algebra with
 16198	obstruction classes $o_r(\cA)$ from
 16199	Construction~\ref{constr:obstruction-recursion}.
 16200	Define the \emph{shadow depth}
 16201	$\kappa_d(\cA) := r_{\max}(\cA) =
 16202	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16203	(with the convention $\kappa_d = \infty$ if the tower
 16204	does not terminate).
 16205	The \emph{shadow depth class} of~$\cA$ is determined
 16206	by the vanishing pattern of obstruction classes:
 16207	\begin{center}
 16208	\small
 16209	\renewcommand{\arraystretch}{1.15}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16499,16575p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30439,30455p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '233,305p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16499	\label{thm:shadow-archetype-classification}
 16500	\ClaimStatusProvedHere
 16501	\index{shadow depth!classification theorem|textbf}
 16502	\index{shadow archetype classification|textbf}
 16503	Every chirally Koszul algebra in the standard landscape belongs to
 16504	exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
 16505	$\mathbf{F}_4$, or $\mathbf{M}$
 16506	\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 16507	The class is determined by the vanishing pattern of obstruction
 16508	classes at degrees~$3$, $4$, $5$, and the assignments for the
 16509	primitive archetypes are as follows:
 16510	\begin{enumerate}[label=\textup{(\roman*)}]
 16511	\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
 16512	 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
 16513	 All higher obstruction classes vanish:
 16514	 $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
 16515	 exactly quadratic.
 16516	
 16517	\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
 16518	 Affine Kac--Moody $V_k(\fg)$ at generic level.
 succeeded in 51ms:
 30439	\label{def:ambient-modular-complementarity-algebra}
 30440	The \emph{carrier} for the modular bar--Hamiltonian is the filtered
 30441	completed graded vector space
 30442	\begin{equation}
 30443	\label{eq:ambient-modular-complementarity-algebra}
 30444	\mathfrak{g}^{\mathrm{amb}}_{\cA}
 30445	:=
 30446	\bigl(L_{\cA} \oplus K_{\cA} \oplus L_{\cA^!}\bigr)
 30447	\widehat\otimes \mathbb{G}_{\mathrm{st}}
 30448	\widehat\otimes \mathbb{G}_{\mathrm{pf}},
 30449	\end{equation}
 30450	where $L_{\cA} := \operatorname{Def}_{\mathrm{cyc}}(\cA)$,
 30451	$K_{\cA} := (\cA^!\widehat\otimes\cA)[1]$,
 30452	$\mathbb{G}_{\mathrm{st}}$ is the completed stable-graph coefficient
 30453	algebra (connected stable graphs with genus/leg labels), and
 30454	$\mathbb{G}_{\mathrm{pf}}$ is the planted-forest coefficient algebra
 30455	(nested collision types from the $\overline{\operatorname{FM}}_3$
 succeeded in 51ms:
   233	\begin{definition}[$E_1$ modular convolution dg~Lie algebra]
   234	\label{def:e1-modular-convolution}
   235	\ClaimStatusProvedHere
   236	\index{E1 algebra@$E_1$-algebra!modular convolution|textbf}
   237	\index{modular convolution dg Lie algebra!E1@$E_1$ (ordered)}
   238	Let $\cA$ be a cyclic $E_1$-chiral algebra
   239	(Definition~\ref{def:e1-chiral}).
   240	The degree-$n$ component of the ordered bar complex is the tensor
   241	coalgebra $T^c(s^{-1}\bar\cA)$ built on the augmentation ideal
   242	$\bar\cA = \ker(\varepsilon)$, with $n$ linearly ordered external
   243	legs and deconcatenation coproduct (distinct from the coshuffle
   244	coproduct of $\mathrm{Sym}^c$). The modular grading is supplied
   245	separately by $\cM_{\Ass}(g,n)$ above.
   246	\begin{equation}
   247	\label{eq:e1-modular-convolution}
   248	{\gAmod}^{E_1}
   249	\;:=\;
   250	\prod_{\substack{g,n \\ 2g-2+n > 0}}
   251	\operatorname{Hom}\!\bigl(
   252	\cM_{\Ass}(g,n),\,

thinking
**Collecting citation information**

I need to collect the remark from line 3587 to reference the local ordered lift later. It's important to ensure I have accurate information for the citation. I'll make sure to keep track of it properly, so I don't forget. This way, I can provide a robust and well-supported reference when needed. It's always good to be thorough and double-check these details!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3584,3594p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3584	\index{MC2!coinvariant scope}
  3585	Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
  3586	statement: its target dg~Lie algebra is
  3587	$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
  3588	The ordered lift
  3589	$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
  3590	\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
  3591	Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
  3592	$\Theta_\cA^{E_1}$ to~$\Theta_\cA$.
  3593	\end{remark}
  3594	

thinking
**Collecting remarks on MC equations**

I need to gather the remark related to two MC equations from line 10396. I've already collected around 10396 from a source, but it seems I don't have the specific line numbers. It might not be necessary right now, but to make a fix, I may want to mention moving that remark. Citing line 10396 sounds appropriate, so let's gather all the relevant information together!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10396,10418p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 10396	\begin{remark}[The two Maurer--Cartan equations]
 10397	\label{rem:two-mc-equations}
 10398	\index{Maurer--Cartan equation!strict vs $L_\infty$}
 10399	The universal MC element $\Theta_\cA$ satisfies two forms of the
 10400	Maurer--Cartan equation, one in each layer of the two-level
 10401	convention (Remark~\ref{rem:two-level-convention}).
 10402	
 10403	\emph{Strict form.} In the dg~Lie model
 10404	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$
 10405	(Definition~\ref{def:modular-convolution-dg-lie}):
 10406	\begin{equation}\label{eq:strict-mc}
 10407	D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0,
 10408	\end{equation}
 10409	where $D = \ell_1^{(0)}$ and $[-,-] = \ell_2^{(0)}$ are the only
 10410	nonvanishing operations. This is a polynomial equation of degree~$2$
 10411	in the degree-$1$ component.
 10412	
 10413	\emph{$L_\infty$ form.} In the quantum $L_\infty$-algebra
 10414	$\Definfmod(\cA)$
 10415	(Theorem~\ref{thm:modular-homotopy-convolution}),





thinking
**Considering definition placement**

I'm noticing some informal use here, so I might need to position the definition better. The exact fix could be adding `\textup{(Definition\ref{def:shadow-depth-classification})}` in the statement and proof, or I could move the definition earlier. Since it shows up later, I might either move the shadow-depth definition subsection before line 4211 or replace the classes with explicit vanishing conditions, which would clarify things and reduce dependence. These adjustments seem precise and possibly an improvement!
thinking
**Standardizing notation in findings**

I’m thinking about how to address the classification notation in the document. It seems like there's inconsistency with the use of \mathsf, \mathbf G/L/C/M, and \mathbf F2/F3/F4/M. To fix this, I could standardize on one notation, likely \mathbf G/L/C/M. I might have to define \mathbf F_d separately for d≥5 or remove it altogether. I want to make sure I’m offering the user an exact file:line but I'm also considering if multiple line locations could be allowed.
thinking
**Considering separate findings**

I’m thinking it might be better to separate the findings into distinct sections. For instance, I should clearly outline the points regarding the ambient carrier drift and the issues surrounding the undefined carrier and shadow algebra codomain. I believe this distinction is critical for clarity and understanding. I'll focus on referencing the specific lines, like `11825-11916`, to ensure the user can easily locate this information later. This should provide a more structured approach!
thinking
**Examining definitions and theorems**

I’m considering whether there’s a definitive environment at all based on the user's question. There are specific references at line 3367 that prove an equation and cite a theorem later on at 3528, and I see a formal remark at line 10396. There might be a concern with the local definition of `g^{mod}` at line 9837 after the universal-theta proof. It's also worth checking if `\Definfmod` is defined at line 10597. A potential fix could involve moving the theorem below the local definitions or rewriting them with forward pointers. That seems like a solid idea!
thinking
**Inspecting constitutional uses**

I’m thinking about how AGENTS uses G/L/C/M. Since concordance is higher in the hierarchy than AGENTS, I need to be cautious. I should read around line 3824 of the concordance to understand it better. If the concordance defines F2/F3/F4 as G/L/C, then using F2 in a theorem might not be wrong. Let’s take a closer look to clarify this!
codex
Before I call the class-notation drift a real defect, I’m checking the concordance. If the concordance deliberately aliases `\mathbf F_2/\mathbf F_3/\mathbf F_4` to `\mathbf G/\mathbf L/\mathbf C`, this becomes a local consistency failure rather than a contradiction of the governing chapter.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '708,722p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3818,3836p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   708	\small
   709	\begin{tabular}{llll}
   710	\textbf{Class} & \textbf{$r_{\max}$} & \textbf{Archetype}
   711	 & \textbf{Examples} \\ \hline
   712	$\mathbf{F}_2=$ \textbf{G} (Gaussian)
   713	 & $2$ & abelian, no bracket
   714	 & Heisenberg, free fermion, lattice \\[2pt]
   715	$\mathbf{F}_3=$ \textbf{L} (Lie/tree)
   716	 & $3$ & Lie bracket, tree-level
   717	 & affine Kac--Moody $\widehat{\mathfrak{g}}_k$ \\[2pt]
   718	$\mathbf{F}_4=$ \textbf{C} (contact/quartic)
   719	 & $4$ & quartic contact interaction
   720	 & $\beta\gamma$, symplectic fermion \\[2pt]
   721	\textbf{M} (mixed)
   722	 & $\infty$ & infinite tower
 succeeded in 51ms:
  3818	\label{sec:concordance-structural-upgrades}
  3819	
  3820	\paragraph{Shadow archetype classification and single-line dichotomy.}
  3821	Theorem~\ref{thm:shadow-archetype-classification} classifies the
  3822	standard-landscape shadow depth classes
  3823	($\mathbf{G}$/$\mathbf{L}$/$\mathbf{C}$/$\mathbf{M}$
  3824	$= \mathbf{F}_2/\mathbf{F}_3/\mathbf{F}_4/\mathbf{M}$)
  3825	with complete proofs for all primitive archetypes.
  3826	Shadow depth is orthogonal
  3827	to Koszulness: all computed archetypes are chirally Koszul, yet their
  3828	shadow depths differ.
  3829	The single-line dichotomy
  3830	(Theorem~\ref{thm:single-line-dichotomy}) proves the gap between
  3831	$\mathbf{F}_4$ and $\mathbf{M}$ is structural, not empirical:
  3832	on any one-dimensional primary slice of
  3833	$\Defcyc^{\mathrm{mod}}(\cA)$, every shadow coefficient
  3834	$S_r$ ($r \geq 4$) factors through the critical discriminant
  3835	$\Delta = 8\kappa S_4$, and the quotients $R_r = S_r/\Delta$
  3836	are generically nonvanishing, so $r_{\max} \in \{2, 3, \infty\}$






thinking
**Evaluating task summary**

I need to read the target and direct dependency e1. Since the task surface is one file, I could indicate something like `Checked: 2 files | Findings: 7 | Verdict: FAIL`. However, the template states that it should say `Checked: N`. Maybe I can just use `Checked: 2 files` instead. It seems necessary to mention the target and dependency lines in the findings if they're used. Ultimately, my final summary may be `Checked: 2 files | Findings: 7 | Verdict: FAIL`.
thinking
**Revising mathematical definitions**

I want to ensure that the theorem is self-contained, especially since it includes the alias `G/L/C/M = F_2/F_3/F_4/M`, but it's not fully stated here. So, I'll revise lines 16504-16506 to present `\mathbf G,\mathbf L,\mathbf C,\mathbf M` and add a clarifying sentence about indexing. It seems important to use `\mathbf F_d` for `d ≥ 5` only. I think the severity of the issue should be considered HIGH since it mis-cites its own definition.
thinking
**Checking definitions andnotations**

I need to confirm if `\cA^{sh}` is properly defined, as it's inline earlier but formally later. Using “formal definition” helps avoid misunderstanding about it being undefined. I wonder about another issue with theorem on line 2189, which uses \gAmod before definition 9837—is that covered by high 2? I’m also contemplating the notation styles like `\mathsf` vs. `\mathbf` between lines 136-155 and 16215. However, if we have high 5, we might not need to address it.
thinking
**Checking findings and formats**

I think I should check if there are any open questions about `Theta_A`. The final findings need to clarify that `\Theta_\cA` is already defined. The user wants a strict summary, so I might summarize as `Checked: 4 | Findings: 7 | Verdict: FAIL`. I need to count the files and it might be 5. It sounds like I should aim for a flat list without nested bullets and check if I have the 7 findings confirmed.
thinking
**Listing findings**

I need to present my findings clearly. I've got 1 critical issue regarding carrier drift, 4 high issues about missing information or misuse in proofs, and 2 medium issues concerning architecture and type mismatches. I’m considering omitting any redundant opening lines in my final presentation to keep things concise. It looks like my findings are well-categorized, and I want to ensure I share them effectively without unnecessary fluff.
thinking
**Identifying potential errors**

I need to mention that "There is no local definition of `\gAmod` until 9837" in finding 6. That seems important! There's a potential risk because, in line 4212, the theorem uses \mathsf instead of \mathbf. That's a detail I can't overlook. It seems classes might have been informal earlier at 136. I'm wondering if I should clarify these points to avoid confusion or mistakes, which might impact my overall findings.
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:59-63,11825-11916,30439-30449 — PROBLEM: the chapter changes the carrier object without saying so. The opening says the carrier is `\gAmod`; the shadow-tower section says it is defining a filtration on the “modular convolution algebra” but actually defines `F^\bullet` on `\mathfrak{g}^{\mathrm{amb}}_{\cA}`; the carrier `\mathfrak{g}^{\mathrm{amb}}_{\cA}` is only formally defined later at lines 30439-30449. The same definition then sends the obstruction class to `H^2(\cA^{\mathrm{sh}}_{r+1,0})` before the shadow algebra is formally defined at lines 12138-12163. The tower is therefore founded on two undeclared objects and no comparison map between `\gAmod` and `\mathfrak{g}^{\mathrm{amb}}_{\cA}` is stated. FIX: move Definition `ambient-modular-complementarity-algebra` to immediately before line 11832, add an explicit comparison sentence (`\gAmod \hookrightarrow \mathfrak{g}^{\mathrm{amb}}_{\cA}` or `\gAmod = \mathfrak{g}^{\mathrm{amb}}_{\cA}`, whichever is intended), and replace line 11916 by a carrier-internal target such as `H^2(F^{r+1}\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+2}\mathfrak{g}^{\mathrm{amb}}_{\cA})` until the identification with `\cA^{\mathrm{sh}}_{r+1,0}` is proved after Definition~`\ref{def:shadow-algebra}`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:180 — PROBLEM: `\Theta_\cA^{E_1}` is invoked as if the ordered carrier were already in scope, but this file does not define `${\gAmod}^{E_1}` or the averaging map there. The local ordered/coinvariant bridge only appears later at lines 3585-3592, and the actual ordered definition is in `chapters/theory/e1_modular_koszul.tex:233-287`. This is a hidden import at the first `E_1`-level use. FIX: insert a local scope paragraph before line 177: define or import `${\gAmod}^{E_1}` and `\operatorname{av}:{\gAmod}^{E_1}\to\gAmod` from Definition~`\ref{def:e1-modular-convolution}`, and explicitly state `\Theta_\cA=\operatorname{av}(\Theta_\cA^{E_1})` before mentioning `\pi_{2,0}(\Theta_\cA^{E_1})`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3359-3372 — PROBLEM: the proof of `thm:universal-theta` derives and uses “the Maurer--Cartan equation” before this chapter has put the strict MC equation on a formal standalone surface. The strict equation is only written later at lines 10396-10408, and the full bar-intrinsic theorem only appears later at lines 3507-3582. The proof is therefore forward-dependent on undeclared formalism. FIX: either move Theorem~`\ref{thm:mc2-bar-intrinsic}` above `thm:universal-theta`, or insert immediately before line 3332 a short definition/lemma package:
  `\begin{definition}[Strict Maurer--Cartan equation] ... D x + \frac12[x,x]=0 ... \end{definition}`
  and
  `\begin{lemma}[Bar-intrinsic MC identity] If D_\cA=\dzero+\Theta_\cA and D_\cA^2=0, then \Theta_\cA satisfies the strict MC equation. \end{lemma}`
  Then change line 3371 to cite that lemma instead of pointing forward.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:4212-4218,4251-4254 — PROBLEM: `thm:bipartite-linfty-tree` and its proof use the shadow classes `\mathsf{G},\mathsf{L},\mathsf{C},\mathsf{M}` as if they were already defined, but the formal depth-class definition is only at lines 16191-16240. There is no local alias, no forward pointer, and the proof relies on those class names in an essential termination argument. FIX: move Definition~`\ref{def:shadow-depth-classification}` above this theorem, or rewrite both the statement and proof with explicit vanishing conditions (`o_3=0`, `o_3\neq0,o_4=0`, `o_4\neq0,o_5=0`, infinitely many nonzero `o_r`) and then add “these are later named classes `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}` in Definition~`\ref{def:shadow-depth-classification}`.”

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:16503-16507,16566-16568 — PROBLEM: `thm:shadow-archetype-classification` cites Definition~`\ref{def:shadow-depth-classification}` but does not use that definition’s notation. The definition at lines 16215-16240 defines `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}`; the theorem opens with `\mathbf{F}_2,\mathbf{F}_3,\mathbf{F}_4,\mathbf{M}`, switches back to `\mathbf{G},\mathbf{L},\mathbf{C}` inside the enumerated items, and later introduces `\mathbf{F}_d` with no local alias. Concordance does record the alias (`G/L/C/M = F_2/F_3/F_4/M`), but this theorem does not. FIX: make the theorem self-contained. Replace lines 16504-16505 by `\mathbf{G}, \mathbf{L}, \mathbf{C}, or \mathbf{M}` and add one sentence after line 16506: “We also write `\mathbf{F}_2:=\mathbf{G}`, `\mathbf{F}_3:=\mathbf{L}`, `\mathbf{F}_4:=\mathbf{C}` when indexing by depth.” Then reserve `\mathbf{F}_d` for genuinely higher finite depths `d\ge 5`.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:2188-2200 — PROBLEM: `thm:three-tier-architecture` states `\Theta_\cA\in\MC(\gAmod)`, the shadow obstruction tower, and the shadow algebra before the file has formally introduced those objects locally (`\Theta_\cA` theorem at 3528, `\gAmod` definition at 9837, tower definition at 11885, shadow algebra definition at 12138). Because this is a theorem environment, not casual roadmap prose, the statement is not self-contained. FIX: either move this theorem below the formal setup, or rewrite each item with inline definitions: `\Theta_\cA:=D_\cA-\dzero`, `\Theta_\cA^{\le r}:=\pi_{\le r}(\Theta_\cA)`, and `\cA^{\mathrm{sh}}:=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))`, followed by explicit forward references to the later formal definitions.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:11921-11925 — PROBLEM: the shadow-tower definition collapses objects of different types. `\Theta_{\cA}^{\le 2}` is a truncated MC element in a quotient Lie algebra, but line 11921 identifies it directly with the scalar `\kappa(\cA)`; the next bullets similarly treat `\Theta_{\cA}^{\le 3}` and `\Theta_{\cA}^{\le 4}` as if they were literally the cubic and quartic classes. No embedding or projection map is stated. FIX: rewrite these bullets as projections, e.g. `\pi_{2,0}(\Theta_{\cA}^{\le 2})=\kappa(\cA)`, `\pi_{3,0}(\Theta_{\cA}^{\le 3})=\mathfrak{C}(\cA)`, `\pi_{4,0}(\Theta_{\cA}^{\le 4})=\mathfrak{Q}(\cA)`, or explicitly define the scalar/class embeddings into the truncated carrier before these identifications.

## Summary
Checked: 4 | Findings: 7 | Verdict: FAIL
tokens used
164,017
