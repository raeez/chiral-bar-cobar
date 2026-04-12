# T16_depth_gap (442s, gpt-5.4)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:17115 — `prop:depth-gap-trichotomy` is over-scoped as stated. It assumes `\kappa\neq 0` on the primary line, but its own proof says the only `d_{\mathrm{alg}}=2` case is the boundary case `\kappa|_L=0` for `\beta\gamma` (`17167-17176`). Under the stated hypothesis, the rank-one argument only yields `d_{\mathrm{alg}}\in\{0,1,\infty\}`, not the claimed `{0,1,2,\infty}` or a bijection with all four classes.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16414 — The class-`C` witness is internally contradicted by its own cited dependencies. This theorem says `\beta\gamma` on the weight-changing line has `\mathfrak Q_{\beta\gamma}\neq 0` and `r_{\max}=4`, but the imported `\beta\gamma` results prove the opposite on that line: `\mu_{\beta\gamma}=0` and the quartic contact invariant vanishes identically (`appendices/nonlinear_modular_shadows.tex:1166-1173`, `chapters/examples/beta_gamma.tex:2516-2528`), and one proved proposition even says the whole shadow tower vanishes there (`chapters/examples/free_fields.tex:1148-1166`). So the manuscript does not presently supply a stable realized `d_{\mathrm{alg}}=2` example on the claimed slice.

- [CRITICAL] chapters/examples/free_fields.tex:1171 — The proved `\beta\gamma` global-depth theorem contradicts the proved T-line theorem in the same file. The T-line proposition gives `S_r\neq 0` for all `r\ge 2` and infinite shadow depth (`1130-1145`), while the global theorem says `r_{\max}=4` and `S_5=0` globally despite `S_5\neq 0` on the T-line restriction (`1175-1178`). The follow-up remark (`1224-1231`) does not resolve that contradiction; it just restates it. Since the depth-gap proof relies on this stratum-separation story, the `d_{\mathrm{alg}}=2` realization is not trustworthy.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:17195 — The multi-sector extension is not actually proved at theorem strength. The proof jumps from the rank-one dichotomy to all multi-generator algebras by citing `Remark~rem:contact-stratum-separation` (`18632-18699`) plus decoupling (`27946-28001`). I did not find a proved theorem in that dependency chain excluding a finite mixed-sector quintic obstruction. That is exactly the step needed to rule out a genuine `d_{\mathrm{alg}}=3` counterexample beyond rank one.

- [MEDIUM] chapters/connections/arithmetic_shadows.tex:1857 — Downstream propagation of the class-`C` mechanism is unstable. This chapter says `d_{\mathrm{alg}}=2` because `m_3` and `m_4` are both nonzero (`1858-1861`), the `\beta\gamma` chapter introduction attributes class `C` to `m_4` (`chapters/examples/beta_gamma.tex:20-28`), but the quartic-birth theorem attributes the quartic to `\operatorname{cyc}(m_3)` instead (`chapters/examples/beta_gamma.tex:2098-2127`; appendix mirror at `1142-1163`). I did not find a proved local block here establishing a nonzero `m_4`, so the operation-count interpretation of `d_{\mathrm{alg}}=2` is not stably grounded.

## Summary
Instances checked: 18 | Violations found: 5 | Verdict: FAIL

The rank-one `\kappa\neq 0` argument does explain why `d_{\mathrm{alg}}=3` is impossible on a single primary line: once `S_4\neq 0`, either `S_5` or `S_6` survives, and the closed form then forces an infinite tail. What fails is the extension beyond that setting and, especially, the realization of the four values: `0`, `1`, and `\infty` are supported much better than `2`, whose `\beta\gamma` witness is contradictory across proved surfaces. I did not find a direct AP131 conflation inside the theorem block itself; the manuscript distinguishes `d_{\mathrm{gen}}(\mathrm{Vir})=3` from `d_{\mathrm{alg}}(\mathrm{Vir})=\infty` correctly. The failure mode here is scope/dependency collapse, not a bare `d_{\mathrm{gen}}` vs `d_{\mathrm{alg}}` mix-up.


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
session id: 019d8393-7d22-79e0-a527-da140284ad55
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: FALSIFY the proof of Depth gap: d_alg in {0,1,2,inf}, gap at 3. Check: (a) why is 3 impossible? (b) are the four values realized? (c) is there confusion between d_gen and d_alg (AP131)?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers

thinking
**Planning for user update**

I need to acknowledge the user's request and outline my first steps in the commentary. It's essential to confirm my understanding and update the plan before diving into substantial work. I'll probably open relevant files using exec_command or spawn explorer, utilizing the required skill in SKILL.md. To explore, I might read core files about the depth gap and theorem. I’ll also search for specific chapters and ensure I comply with no network access. Let’s get started!
codex
Using `deep-beilinson-audit` and `multi-path-verify` for this pass. I’m locating the exact theorem surface, then I’ll read the full statement, proof, cited dependencies, and any cross-volume duplicates before I assess whether the depth-gap claim actually survives scrutiny.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pwd && rg -n "depth gap|d_alg|gap at 3|3 impossible|d_gen" chapters CLAUDE.md metadata chapters/connections/concordance.tex .agents/skills/deep-beilinson-audit/SKILL.md .agents/skills/multi-path-verify/SKILL.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

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

 succeeded in 51ms:
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

 succeeded in 51ms:
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
/Users/raeez/chiral-bar-cobar
chapters/connections/concordance.tex:7079: & Algebraic depth gap:
chapters/connections/concordance.tex:9649:& Algebraic depth gap:
CLAUDE.md:215:alpha_g = 2*rank + 4*dim*h^v (universal Hilbert-series growth, all simple types). d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy). kappa(BP)+kappa(BP^!)=98/3 (self-dual k=-3).
CLAUDE.md:358:- B43. `d_alg(Vir) = 3`. CORRECT: `d_gen(Vir) = 3`, `d_alg(Vir) = inf` (class M). AP131/FM18.
CLAUDE.md:434:**FM18. Generating-depth vs algebraic-depth conflation.** `d_gen(Vir) = 3` (m_3 generates recursively) but `d_alg(Vir) = inf` (class M). Counter: every depth statement carries the subscript `gen` or `alg`. Refuse bare `d(...)`.
CLAUDE.md:497:| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy) |
CLAUDE.md:515:**fiber-base/depth** (AP130, AP131, AP134): AP130: Objects on the fiber (forms on Σ_g) are NOT objects on the base (classes on M̄_g). Verify: does this expression live on moduli or on the curve? AP131: Generating depth (degree at which higher ops are determined) != algebraic depth (whether tower terminates). Vir: d_gen finite, d_alg=∞. AP134: Cohomological amplitude [0,d] != virtual dimension d.
CLAUDE.md:804:AP131: Generating depth != algebraic depth. d_gen (the degree at which all higher operations are determined by lower ones) ≠ d_alg (whether the tower terminates). Virasoro: m_3 generates all m_k (finite generating depth), but ALL m_k are nonzero (d_alg = ∞, class M). Writing d_alg(Vir) = 1 because "m_3 generates everything" conflates the two. Always specify WHICH depth.
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
metadata/theorem_registry.md:983:| `prop:depth-gap-trichotomy` | `proposition` | 16625 | Algebraic depth gap: no $d_{\mathrm{alg}} = 3$ |
metadata/dependency_graph.dot:283:  lem_free_closed_generating_kernel [label="lem:free-closed-generating-kernel\nlemma [Pr]\nClosed generating kernel", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:997:  cor_formal_neighborhood_generated_by_KR [label="cor:formal-neighborhood-generated-by-KR\ncorollary [Pr]\nFormal neighborhood generated by the com...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2872:  thm_arnold_genus1 [label="thm:arnold-genus1\ntheorem [Pr]\nGenus-1 Arnold relation", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:3056:  prop_depth_gap_trichotomy [label="prop:depth-gap-trichotomy\nproposition [Pr]\nAlgebraic depth gap: no $d_{\mathrm{alg}...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3424:  prop_chiral_operad_genus0 [label="prop:chiral-operad-genus0\nproposition [Pr]\nGenus-zero identification", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3479:  thm_arnold_general_n [label="thm:arnold-general-n\ntheorem [Pr]\nArnold relations for \texorpdfstring{$n$...", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:5323:  thm_arnold_genus1 -> thm_quantum_arnold_relations;
metadata/claims.jsonl:2944:{"label": "prop:depth-gap-trichotomy", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16625, "title": "Algebraic depth gap: no $d_{\\mathrm{alg}} = 3$", "labels_in_block": ["prop:depth-gap-trichotomy", "eq:depth-gap"], "refs_in_block": ["def:shadow-depth-classification"]}
chapters/connections/arithmetic_shadows.tex:5:% d = 1 + d_arith + d_alg separates arithmetic from homotopy.
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

thinking
**Evaluating theorem dependencies**

I need to locate theorems, proofs, and their dependencies. Perhaps using the explorer agent would help, as the developer advises using it for all codebase inquiries. The user has asked for a full audit, but I can still query theorem and proof dependencies with the explorer. It's best to avoid using subagents unless the user specifically requests it. I’ll read the complete theorem statement and proof context, inspecting lines and checking cited dependencies thoroughly.
codex
I’ve fixed the audit surface at `chapters/theory/higher_genus_modular_koszul.tex` around `prop:depth-gap-trichotomy`. Next I’m reading the theorem block in full, then the definition and earlier results it depends on, so I can test each proof step against its actual hypotheses rather than the surrounding prose.
exec
/bin/zsh -lc "python - <<'PY'
import json
label='prop:depth-gap-trichotomy'
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line)
        if obj.get('label')==label:
            print(json.dumps(obj, indent=2))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def:shadow-depth-classification|single-line-dichotomy|depth gap|d_\\\\mathrm\\{alg\\}|d_\\{\\\\mathrm\\{alg\\}\\}|d_gen|d_\\{\\\\mathrm\\{gen\\}\\}|class G|class L|class C|class M|S_4|Delta\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17040,17320p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:depth-gap-trichotomy|def:shadow-depth-classification|thm:single-line-dichotomy|prop:depth-gap-trichotomy" metadata/dependency_graph.dot metadata/claims.jsonl chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
 exited 2 in 52ms:
rg: regex parse error:
    (?:def:shadow-depth-classification|single-line-dichotomy|depth gap|d_\mathrm\{alg\}|d_\{\mathrm\{alg\}\}|d_gen|d_\{\mathrm\{gen\}\}|class G|class L|class C|class M|S_4|Delta)
                                                                         ^^
error: unrecognized escape sequence
 succeeded in 51ms:
metadata/dependency_graph.dot:3056:  prop_depth_gap_trichotomy [label="prop:depth-gap-trichotomy\nproposition [Pr]\nAlgebraic depth gap: no $d_{\mathrm{alg}...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3063:  thm_single_line_dichotomy [label="thm:single-line-dichotomy\ntheorem [Pr]\nSingle-line dichotomy", style=filled, fillcolor="#c8e6c9"];
chapters/connections/concordance.tex:204:(Theorem~\ref{thm:single-line-dichotomy}:
chapters/connections/concordance.tex:814:(Definition~\textup{\ref{def:shadow-depth-classification}})
chapters/connections/concordance.tex:916:(Definition~\ref{def:shadow-depth-classification}):
chapters/connections/concordance.tex:3818:(Theorem~\ref{thm:single-line-dichotomy}) proves the gap between
chapters/connections/concordance.tex:7078:\ref{prop:depth-gap-trichotomy}
chapters/connections/concordance.tex:7082: \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)}
chapters/connections/concordance.tex:9651: \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)} \\
metadata/claims.jsonl:36:{"label": "thm:ainfty-formality-depth", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/arithmetic_shadows.tex", "line": 1896, "title": "$A_\\infty$ formality criterion", "labels_in_block": ["thm:ainfty-formality-depth", "thm:shadow-sullivan"], "refs_in_block": ["thm:single-line-dichotomy", "thm:shadow-tower-asymptotics"]}
metadata/claims.jsonl:62:{"label": "rem:ode-im-shadow-identification", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/arithmetic_shadows.tex", "line": 4052, "title": "ODE/IM correspondence as shadow projection", "labels_in_block": ["rem:ode-im-shadow-identification", "eq:shadow-potential-ode-im"], "refs_in_block": ["thm:mc2-bar-intrinsic", "rem:hitchin-wkb", "prop:universal-stokes-constants", "prop:universal-instanton-action", "def:shadow-depth-classification"], "cites_in_block": ["DT99", "BLZ99"]}
metadata/claims.jsonl:457:{"label": "thm:shadow-euler-independence", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/genus_complete.tex", "line": 2499, "title": "", "refs_in_block": ["def:shadow-depth-classification", "def:euler-koszul-class", "thm:gram-positivity", "constr:interacting-kernel"]}
metadata/claims.jsonl:1559:{"label": "thm:w3hol-discriminants", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/w3_holographic_datum.tex", "line": 628, "title": "Critical discriminants and shadow class", "labels_in_block": ["thm:w3hol-discriminants", "eq:w3hol-discriminants"], "refs_in_block": ["thm:single-line-dichotomy"]}
metadata/claims.jsonl:2284:{"label": "prop:envelope-shadow", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 5457, "title": "Factorization envelope shadow functor", "refs_in_block": ["def:cyclically-admissible", "def:shadow-depth-classification"]}
metadata/claims.jsonl:2285:{"label": "conj:graph-complex-shadow", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 5681, "title": "Graph complex controls shadow obstruction tower deformations", "refs_in_block": ["def:shadow-depth-classification"], "cites_in_block": ["Willwacher15"]}
metadata/claims.jsonl:2613:{"label": "thm:en-shadow-tower", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 2681, "title": "$\\En$ shadow obstruction tower: universality of $\\kappa$ and formality collapse", "refs_in_block": ["def:shadow-depth-classification"]}
metadata/claims.jsonl:2939:{"label": "thm:shadow-archetype-classification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16007, "title": "Shadow archetype classification", "refs_in_block": ["def:shadow-depth-classification", "cor:nms-betagamma-mu-vanishing", "thm:w-virasoro-quintic-forced", "prop:propagator-variance", "thm:modular-koszul-duality-main", "fig:shadow-archetype-classification", "thm:shadow-spectral-correspondence", "sec:higher-depths", "prop:free-interacting-dichotomy"]}
metadata/claims.jsonl:2944:{"label": "prop:depth-gap-trichotomy", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16625, "title": "Algebraic depth gap: no $d_{\\mathrm{alg}} = 3$", "labels_in_block": ["prop:depth-gap-trichotomy", "eq:depth-gap"], "refs_in_block": ["def:shadow-depth-classification"]}
metadata/claims.jsonl:2951:{"label": "thm:single-line-dichotomy", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 17391, "title": "Single-line dichotomy", "labels_in_block": ["thm:single-line-dichotomy", "eq:universal-factorization", "eq:pump-coefficients"]}
metadata/claims.jsonl:2956:{"label": "cor:discriminant-atlas", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 18041, "title": "The discriminant atlas", "labels_in_block": ["cor:discriminant-atlas", "eq:discriminant-complementarity-cor", "eq:w3-wline-discriminant", "eq:w3-discriminant-ratio"], "refs_in_block": ["def:shadow-metric", "thm:single-line-dichotomy"]}
 succeeded in 51ms:
Set $U(t) := \sum_{r \geq 3} S_r\,t^r$ (the nonlinear part, removing
$\mathrm{Sh}_2$). The algebraic relation~\eqref{eq:riccati-algebraic-relation}
is equivalent to the Riccati-type first-order ODE
\begin{equation}\label{eq:riccati-ode-form}
 2t\,U'(t) \;+\; \frac{P}{2}\bigl(U'(t)\bigr)^2
 \;=\; R_3\,t^3 + R_4\,t^4,
\end{equation}
where $R_3 = 6\alpha$ and
$R_4 = (9\alpha^2 + 2\Delta)/(2\kappa)$ encode the cubic and quartic inputs.
The left-hand side is \emph{quadratic in~$U'$}: this is the precise sense in
which the shadow obstruction tower is algebraic of degree~$2$. All terms at $t^r$ for
$r \geq 5$ cancel identically, verified through
degree~$15$ by direct computation. The ODE~\eqref{eq:riccati-ode-form}
determines $U$ uniquely from $(\kappa, \alpha, S_4)$ by power-series inversion,
reproducing the MC recursion~\eqref{eq:single-line-inversion}.
\end{remark}

\begin{corollary}[Gaussian decomposition]
\label{cor:gaussian-decomposition}
\label{cor:shadow-algebraic-degree}

thinking
**Gathering relevant information**

I'm figuring out how to get line numbers from `sed`, and I think using `nl -ba` might help. I need the exact file and line number for clarity. I also need to keep in mind any discrepancies in metadata due to extraction. I want to inspect certain definitions and theorems, making sure I read proofs related to `riccati-algebraicity` to see if any closed forms are established. It’s essential to check dependencies between theorems and propositions as well. Let's collect the relevant blocks!
codex
The local proof already exposes two pressure points I need to verify against source, not rhetoric: the `βγ` boundary case for `d_alg=2`, and the multi-sector jump from one primary line to the full algebra. I’m reading those dependencies and the exact depth definition now to see whether the proof really imports enough to justify the claimed trichotomy.
exec
/bin/zsh -lc "rg -n \"label\\{def:shadow-depth-classification\\}|label\\{thm:riccati-algebraicity\\}|label\\{eq:critical-discriminant\\}|label\\{eq:single-line-inversion\\}|label\\{thm:nms-betagamma-quartic-birth\\}|label\\{rem:contact-stratum-separation\\}|label\\{prop:independent-sum-factorization\\}|label\\{sec:betagamma-quartic-birth\\}|label\\{thm:single-line-dichotomy\\}|d_\\{\\\\mathrm\\{gen\\}\\}|d_\\{\\\\mathrm\\{alg\\}\\}|d_\\mathrm\\{gen\\}|d_\\mathrm\\{alg\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17320,17680p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15880,16180p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16780,17060p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Q^{\mathrm{contact}}
 \;=\;
 -\frac{\operatorname{disc}(Q_L)}{256\,\kappa^3}.
\end{equation}
\item
The \emph{MC-corrected Schur complement}
of~$\kappa$ in~$\mathbf{S}_2$ is the intrinsic quartic:
\begin{equation}\label{eq:intrinsic-quartic-schur}
 S_4^{\mathrm{int}}
 \;:=\;
 S_4 - S_4^{\mathrm{free}}
 \;=\;
 S_4 + \frac{9\,\alpha^2}{16\,\kappa},
\end{equation}
where $S_4^{\mathrm{free}} = -9\,\alpha^2/(16\,\kappa)$
is the inherited quartic from the cubic self-bracket
\textup{(}the unique solution
of~\eqref{eq:single-line-inversion}
at $r = 4$ with $S_r = 0$ for $r \geq 4$
on the right-hand side\textup{)}.
 exited 2 in 52ms:
rg: regex parse error:
    (?:label\{def:shadow-depth-classification\}|label\{thm:riccati-algebraicity\}|label\{eq:critical-discriminant\}|label\{eq:single-line-inversion\}|label\{thm:nms-betagamma-quartic-birth\}|label\{rem:contact-stratum-separation\}|label\{prop:independent-sum-factorization\}|label\{sec:betagamma-quartic-birth\}|label\{thm:single-line-dichotomy\}|d_\{\mathrm\{gen\}\}|d_\{\mathrm\{alg\}\}|d_\mathrm\{gen\}|d_\mathrm\{alg\})
                                                                                                                                                                                                                                                                                                                                                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
convolution recursion produces $a_n \neq 0$ for all
$n \geq 1$
(Theorem~\ref{thm:single-line-dichotomy}). Hence
$S_5 \neq 0$ and $S_6 \neq 0$.

\emph{Part~(iv).}
At the scalar level, the scalar MC equation closes with the
binary bracket $\ell_2^{(0)}$ alone: the recursion
$a_n = -(2a_0)^{-1} \sum_{j=1}^{n-1} a_j a_{n-j}$
involves only $\ell_2^{(0)}$-compositions. The higher
brackets $\ell_k^{(0)}$ for $k \geq 3$ contribute zero at
the scalar level
(Construction~\ref{constr:explicit-convolution-linfty}),
so every term in the Jacobi sum at orders $5$ and $6$
vanishes individually. At the vector level, the
generalized Jacobi identity is the integrability condition
for the MC equation, which holds by the bar-intrinsic
construction
(Theorem~\ref{thm:mc2-bar-intrinsic}).
\end{proof}
 succeeded in 50ms:
 Proposition~\textup{\ref{prop:ds-package-functoriality}(i))}.

\item \emph{Quartic creation from zero.}
 The Jacobi identity kills the quartic invariant for affine
 algebras: $S_4^{\mathrm{KM}} = 0$, hence $\Delta = 0$, hence
 class~$\mathbf{L}$. The BRST differential creates a nonzero
 quartic on the quotient: $S_4^{\cW} \neq 0$, $\Delta \neq 0$,
 hence class~$\mathbf{M}$. Drinfeld--Sokolov reduction does
 not modify the quartic invariant; it creates it from nothing.

\item \emph{Growth-rate improvement.}
 The convergence radius of the shadow obstruction tower increases
 under reduction: at $N = 2$, $\rho(13) \approx 0.467$ for the
 Virasoro; at $N = 3$, $\rho$ is smaller. The tower becomes
 better-behaved as the algebra becomes more complicated.
\end{enumerate}
The shadow depth classification is a property of the algebra
\emph{relative to its pre-reduction ancestor}: Drinfeld--Sokolov
reduction is the escalator that lifts the tower from finite to
infinite.


thinking
**Analyzing definitions and theorems**

I’m noting that the definition states finite depths of 5 or more in arithmetic shadows, which clashes with the theorem regarding d_alg in the set {0,1,2,inf}. I need to distinguish between shadow depth and algebraic depth. The definition uses shadow depth classification classes—G/L/C/M—indicating maximum values of 2, 3, 4, and ∞. The theorem asserts that algebraic depths in {0,1,2,∞} correspond to these classes. I need to search for formal definitions of d_alg and d_gen.
thinking
**Rethinking theorem proof**

I find the theorem proof a bit suspicious. It mentions that d_alg is in {0,1,2} based on different alpha and kappa conditions—there seem to be some duplicate cases. I'm starting to wonder if the d_alg formula might be shifted by 2 from r_max. I think I need to read the formal definitions of algebraic depth and generating depth to clarify these points. It could help me grasp the overall structure better. Let's check the file or other chapters!
codex
The manuscript’s own depth definition surface is now a likely failure point: the chapter distinguishes `r_max`/shadow depth from `d_alg`, but I need the exact formal definitions because the proposition is currently using class labels and termination degrees in a way that may already be off by an index shift. I’m tracing those definitions next.
exec
/bin/zsh -lc "rg -n \"label\\{def:algebraic-depth\\}|label\\{def:generating-depth\\}|algebraic depth|generating depth|d_\\{\\\\mathrm\\{alg\\}\\}|d_\\{\\\\mathrm\\{gen\\}\\}|d_{\\\\mathrm{alg}}|d_{\\\\mathrm{gen}}|d_alg|d_gen\" chapters/theory/higher_genus_modular_koszul.tex chapters chapters/connections/concordance.tex CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3790,3845p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15520,16080p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
modular operad).

\paragraph{The thesis.}
The $E_1$ MC element $\Theta^{E_1}_\cA$ is the primary
algebraic invariant. The modular MC element
$\Theta_\cA = \operatorname{av}(\Theta^{E_1}_\cA)$ is its
shadow. Volume~II's Part~VII (ordered
associative chiral Koszul duality, dg-shifted factorization
bridge, gravitational Yangian) develops the $E_1$ layer;
Parts~\ref{part:bar-complex}--\ref{part:v1-frontier} describe the modular/symmetric framework that is the
$\operatorname{av}$-image. Line operators, spectral $R$-matrices,
and Yangian structures are natively $E_1$ and
should be read as primary, not auxiliary.


\section{Structural upgrades}
\label{sec:concordance-structural-upgrades}

\paragraph{Shadow archetype classification and single-line dichotomy.}
Theorem~\ref{thm:shadow-archetype-classification} classifies the
 exited 2 in 51ms:
rg: regex parse error:
    (?:label\{def:algebraic-depth\}|label\{def:generating-depth\}|algebraic depth|generating depth|d_\{\mathrm\{alg\}\}|d_\{\mathrm\{gen\}\}|d_{\mathrm{alg}}|d_{\mathrm{gen}}|d_alg|d_gen)
                                                                                                       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
$\ell_k^{(0)}$ vanishes for $k \geq 3$: the scalar MC
recursion closes with the binary bracket $\ell_2^{(0)}$ alone.
This is immediate from the shadow metric factorization
$f^2 = Q_L$: the $t^n$-coefficients for $n \geq 3$ all vanish,
and these are precisely the higher-bracket contributions at
the scalar level.

\emph{At the vector level}, the brackets are nontrivial for
class~$\mathbf{M}$ algebras. The evaluation
$\operatorname{Sh}_k(\cA) = \ell_k^{(0),\mathrm{tr}}
(\Theta^{\leq k-1}, \dotsc, \Theta^{\leq k-1})$
holds by the inductive argument of
Theorem~\ref{thm:shadow-formality-identification}, Step~3.

For the specific tree counts at degrees $5$ and $6$:
\begin{center}
\small
\begin{tabular}{lcccl}
\toprule
\textbf{Route} & $k = 5$ & $k = 6$ & \textbf{Objects} \\

thinking
**Searching for definitions**

I need to find the formal definitions of "d_alg" and "d_gen." I think starting with a general search might help clarify what those terms mean. Perhaps there are simpler patterns or examples associated with them that could make understanding easier. By breaking it down, I can hopefully get a clearer view of what each term involves. Let's dig into this to ensure I'm gathering the right information!
exec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{alg}}\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{gen}}\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"algebraic depth|generating depth|depth decomposition|label\\{thm:depth-decomposition\\}|label\\{def:["'^}]*depth|label'"\\{prop:["'^}]*depth|AP131" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/arithmetic_shadows.tex chapters/connections/concordance.tex CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:4348:$d_{\mathrm{gen}}(\cA)$ is the smallest degree at which
chapters/connections/concordance.tex:4352:$d_{\mathrm{gen}} = 3$ (finite), $d_{\mathrm{alg}} = \infty$
chapters/connections/concordance.tex:7064: & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
chapters/connections/concordance.tex:7066: Virasoro $d_{\mathrm{gen}} = 3$,
chapters/theory/higher_genus_modular_koszul.tex:17255:Recall that $d_{\mathrm{gen}}(\operatorname{Vir}_c) = 3$ (finite
chapters/theory/higher_genus_modular_koszul.tex:18757:The \emph{generating depth} $d_{\mathrm{gen}}(\cA)$ is the smallest
chapters/theory/higher_genus_modular_koszul.tex:18761:$d_{\mathrm{gen}}$ is the smallest~$N$ such that the truncated
chapters/theory/higher_genus_modular_koszul.tex:18769:The two depths are not equal in general: trivially $d_{\mathrm{gen}}
chapters/theory/higher_genus_modular_koszul.tex:18772:For Virasoro on the primary line, $d_{\mathrm{gen}}(\mathrm{Vir}_c)$
chapters/theory/higher_genus_modular_koszul.tex:18779:$d_{\mathrm{gen}}(\mathrm{Vir}_c) = 3$ is the generating-depth
chapters/connections/concordance.tex:4348:$d_{\mathrm{gen}}(\cA)$ is the smallest degree at which
chapters/connections/concordance.tex:4352:$d_{\mathrm{gen}} = 3$ (finite), $d_{\mathrm{alg}} = \infty$
chapters/connections/concordance.tex:7064: & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
chapters/connections/concordance.tex:7066: Virasoro $d_{\mathrm{gen}} = 3$,
chapters/theory/introduction.tex:101:The \emph{generating depth} $d_{\mathrm{gen}}$ is the smallest degree at which all higher operations are determined recursively.
chapters/theory/introduction.tex:104:These are independent invariants: Virasoro has $d_{\mathrm{gen}} = 3$ but $d_{\mathrm{alg}} = \infty$; $m_3$ generates all higher operations, yet none vanish.
chapters/theory/higher_genus_modular_koszul.tex:17255:Recall that $d_{\mathrm{gen}}(\operatorname{Vir}_c) = 3$ (finite
chapters/theory/higher_genus_modular_koszul.tex:18757:The \emph{generating depth} $d_{\mathrm{gen}}(\cA)$ is the smallest
chapters/theory/higher_genus_modular_koszul.tex:18761:$d_{\mathrm{gen}}$ is the smallest~$N$ such that the truncated
chapters/theory/higher_genus_modular_koszul.tex:18769:The two depths are not equal in general: trivially $d_{\mathrm{gen}}
 succeeded in 50ms:
CLAUDE.md:358:- B43. `d_alg(Vir) = 3`. CORRECT: `d_gen(Vir) = 3`, `d_alg(Vir) = inf` (class M). AP131/FM18.
CLAUDE.md:359:- B44. Bare `d(Vir) = 3` without `gen`/`alg` subscript. AP131.
CLAUDE.md:515:**fiber-base/depth** (AP130, AP131, AP134): AP130: Objects on the fiber (forms on Σ_g) are NOT objects on the base (classes on M̄_g). Verify: does this expression live on moduli or on the curve? AP131: Generating depth (degree at which higher ops are determined) != algebraic depth (whether tower terminates). Vir: d_gen finite, d_alg=∞. AP134: Cohomological amplitude [0,d] != virtual dimension d.
CLAUDE.md:804:AP131: Generating depth != algebraic depth. d_gen (the degree at which all higher operations are determined by lower ones) ≠ d_alg (whether the tower terminates). Virasoro: m_3 generates all m_k (finite generating depth), but ALL m_k are nonzero (d_alg = ∞, class M). Writing d_alg(Vir) = 1 because "m_3 generates everything" conflates the two. Always specify WHICH depth.
chapters/connections/concordance.tex:2672:The depth decomposition
chapters/connections/concordance.tex:4345:\paragraph{Generating depth versus algebraic depth.}
chapters/connections/concordance.tex:4347:distinction mandated: the generating depth
chapters/connections/concordance.tex:4350:algebraic depth $d_{\mathrm{alg}}(\cA)$ is the smallest
chapters/connections/concordance.tex:7064: & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
chapters/connections/concordance.tex:7068: & depth decomposition $+$ class~M tower non-termination \\
chapters/connections/concordance.tex:8315:The depth decomposition is the motivic weight decomposition
chapters/connections/concordance.tex:8653:the depth decomposition $d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
chapters/connections/arithmetic_shadows.tex:90:not its representation theory. The depth decomposition
chapters/connections/arithmetic_shadows.tex:112:The depth decomposition
chapters/connections/arithmetic_shadows.tex:1654:\index{fusion ring!invisible to depth decomposition}%
chapters/connections/arithmetic_shadows.tex:1680:The depth decomposition captures only the spectral content
chapters/connections/arithmetic_shadows.tex:1757:\label{def:arithmetic-depth-filtration}
chapters/connections/arithmetic_shadows.tex:1782:\section{The depth decomposition}
chapters/connections/arithmetic_shadows.tex:1788:\label{thm:depth-decomposition}
chapters/connections/arithmetic_shadows.tex:1882:\index{depth decomposition!universality}%
 succeeded in 51ms:
chapters/connections/concordance.tex:2674:$d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$,
chapters/connections/concordance.tex:2676:(determines critical lines) and $d_{\mathrm{alg}}$ measures
chapters/connections/concordance.tex:2678:For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
chapters/connections/concordance.tex:2680:$d_{\mathrm{alg}} = \infty$. The Borel sum of the
chapters/connections/concordance.tex:3836:giving $d_{\mathrm{alg}} \leq 2$), or they couple
chapters/connections/concordance.tex:3838:cubic pump and forcing $d_{\mathrm{alg}} = \infty$).
chapters/connections/concordance.tex:3839:Hence $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
chapters/connections/concordance.tex:3842:$d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
chapters/connections/concordance.tex:4350:algebraic depth $d_{\mathrm{alg}}(\cA)$ is the smallest
chapters/connections/concordance.tex:4352:$d_{\mathrm{gen}} = 3$ (finite), $d_{\mathrm{alg}} = \infty$
chapters/connections/concordance.tex:7065: $d_{\mathrm{alg}}$: formal distinction~;
chapters/connections/concordance.tex:7067: $d_{\mathrm{alg}} = \infty$
chapters/connections/concordance.tex:7080: $d_{\mathrm{alg}}(\cA) \in \{0,\,1,\,2,\,\infty\}$,
chapters/connections/concordance.tex:7081: no finite $d_{\mathrm{alg}} \geq 3$ realized
chapters/connections/concordance.tex:8161:$d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$,
chapters/connections/concordance.tex:8163:(critical lines) and $d_{\mathrm{alg}}$ is the homotopy defect
chapters/connections/concordance.tex:8166:Lattice: $d_{\mathrm{alg}} = 0$.
chapters/connections/concordance.tex:8167:Virasoro: $d_{\mathrm{alg}} = \infty$.
chapters/connections/concordance.tex:8318:$d_{\mathrm{alg}}$ is the depth of the Tate part.
chapters/connections/concordance.tex:8653:the depth decomposition $d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
exec
/bin/zsh -lc "sed -n '4338,4365p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1782,1915p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18740,18810p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2666,2685p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Proposition~\ref{prop:shadow-tower-three-lenses} identifies
three equivalent readings of the degree-$r$ shadow
$S_r(\cA)$: algebraic (bar-intrinsic MC projection),
geometric (genus-$0$ transferred $L_\infty$ formality
obstruction), and holographic (boundary-bulk correction
in the derived-centre factorization).

\paragraph{Generating depth versus algebraic depth.}
Definition~\ref{def:generating-depth} formalizes the
distinction mandated: the generating depth
$d_{\mathrm{gen}}(\cA)$ is the smallest degree at which
higher operations are recursively determined, while the
algebraic depth $d_{\mathrm{alg}}(\cA)$ is the smallest
degree beyond which all operations vanish. Virasoro:
$d_{\mathrm{gen}} = 3$ (finite), $d_{\mathrm{alg}} = \infty$
(class~M). Bare $d(\cA)$ without subscript is forbidden.

\paragraph{MC3 three-layer split and Lemma~L.}
Corollary~\ref{cor:mc3-all-types} is rewritten as an
explicit three-layer decomposition: MC3a (evaluation-generated
 succeeded in 50ms:
\section{The depth decomposition}
\label{sec:depth-decomposition-section}
\label{sec:honest-assessment}
\label{sec:spectral-continuation}

\begin{theorem}[Depth decomposition]
\label{thm:depth-decomposition}
\ClaimStatusProvedHere
The shadow depth of~$\cA$ decomposes as
\begin{equation}\label{eq:depth-decomposition}
 d(\cA)
 = 1 + d_{\mathrm{arith}}(\cA) + d_{\mathrm{alg}}(\cA),
\end{equation}
where $d_{\mathrm{arith}}$ counts the independent holomorphic Hecke
eigenforms in the Roelcke--Selberg spectral decomposition
of~$\widehat{Z}^c_\cA$ on~$\cM_{1,1}$, and
\[
 d_{\mathrm{alg}}
 := d(\cA) - 1 - d_{\mathrm{arith}}(\cA)
 \;\ge\; 0
 succeeded in 50ms:
$d_{\mathrm{alg}}$, $\operatorname{ek}$) are pairwise
independent
(Theorem~\ref{thm:shadow-euler-independence}).
The Dirichlet--sewing lift packages the arithmetic content of
genus~$1$ as a two-variable $L$-object
$L_\cA(s,u)$
(Definition~\ref{def:two-variable-L})
whose $s$-slice carries zero-side Rankin--Selberg data and
whose $u$-slice carries the prime-side Euler-product
structure.
\end{remark}

\begin{definition}[Generating depth vs algebraic depth]
\label{def:generating-depth}
Two distinct depths attach to the bar/shadow tower of a chiral algebra
$\cA$, and conflating them is forbidden.

The \emph{generating depth} $d_{\mathrm{gen}}(\cA)$ is the smallest
degree~$N$ such that every higher transferred product $m_n$ for
$n > N$ on $\bar{H}^*(B(\cA))$ is determined recursively by
 succeeded in 52ms:
The sewing--Selberg formula
(Theorem~\ref{thm:sewing-selberg-formula}):
$\int_{\cM_{1,1}}\log\det(1{-}K)\cdot E_s\,d\mu
=-2(2\pi)^{-(s-1)}\Gamma(s{-}1)\,\zeta(s{-}1)\zeta(s)$.

\smallskip\noindent
The depth decomposition
(Theorem~\ref{thm:depth-decomposition}):
$d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$,
where $d_{\mathrm{arith}}$ counts holomorphic Hecke eigenforms
(determines critical lines) and $d_{\mathrm{alg}}$ measures
non-holomorphic OPE complexity (invisible to $L$-functions).
For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
minimal models: $d_{\mathrm{arith}}$ finite,
$d_{\mathrm{alg}} = \infty$. The Borel sum of the
Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
order (Proposition~\ref{thm:shadow-gf-borel}).

\smallskip\noindent\textbf{Shadow growth rate}
(Definition~\ref{def:shadow-growth-rate},

thinking
**Inspecting theorem classification**

I want to take a closer look at theorem archetype classification and the results that have been cited. It seems important to search through the labels and read the relevant blocks. This will help me understand how the classification works and what the cited results imply. I'm curious about the connections and patterns that might emerge from this inspection! Let's see what insights I can gain from this exploration.
codex
I now have the formal depth definitions. `d_alg` is the smallest cutoff after which all transferred products vanish; `d_gen` is the recursive-generation cutoff. That makes the audit concrete: I’m checking whether the proof ever sneaks from “generated by low degree” to “vanishes above low degree,” and whether the claimed class realizations actually match those definitions.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:shadow-archetype-classification}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:nms-betagamma-quartic-birth}' chapters/theory/higher_genus_modular_koszul.tex chapters/examples/beta_gamma.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{rem:contact-stratum-separation}' chapters/theory/higher_genus_modular_koszul.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{prop:independent-sum-factorization}' chapters/theory/higher_genus_modular_koszul.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1940,2065p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17380,17640p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15980,16840p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
16390:\label{thm:shadow-archetype-classification}
exec
/bin/zsh -lc "rg -n -F '\\label{thm:single-line-dichotomy}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:18632:\label{rem:contact-stratum-separation}
chapters/theory/higher_genus_modular_koszul.tex:18632:\label{rem:contact-stratum-separation}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:27947:\label{prop:independent-sum-factorization}
chapters/theory/higher_genus_modular_koszul.tex:27947:\label{prop:independent-sum-factorization}
 succeeded in 51ms:
17884:\label{thm:single-line-dichotomy}
 succeeded in 52ms:
$\int_{\Sigma_g} \mathrm{Fact}_{\beta\gamma}$ is quasi-isomorphic to
$\mathcal{D}_{g,\lambda}^{\beta\gamma}$
as a graded line over the moduli space $\mathcal{M}_g$.
\end{conjecture}

\begin{remark}[Why determinantal]
\label{rem:betagamma-why-determinantal}
This is the expected output of the Gaussian path integral: for a free
field theory, the partition function is a ratio of functional
determinants, which on a compact Riemann surface are finite-dimensional
determinant lines. The two factors in~\eqref{eq:betagamma-det-line}
correspond to the $\beta$-sector ($K^\lambda \otimes L$) and the
$\gamma$-sector ($K^{1-\lambda} \otimes L^\vee$), reflecting the
Serre-dual pairing between the two fields.
\end{remark}

\subsection{The holographic partition function}

\begin{definition}[Holographic $\beta\gamma$ partition function]
\label{def:betagamma-holographic-partition-function}
 succeeded in 52ms:
 & $0$ & $0$ & $0$ & $0$
 & $\mathbf{G}$ \\[3pt]
$\hat{\fg}_k$
 & $-\alpha^2$ & $0$
 & $\frac{9\alpha^2}{16\kappa}$
 & $0$
 & $\mathbf{L}$ \\[3pt]
$\mathrm{Vir}_c$
 & $-\frac{20c+83}{5c+22}$
 & $-\frac{320\,c^2}{5c+22}$
 & $\frac{45c+218}{2c(5c+22)}$
 & $\frac{10}{c(5c+22)}$
 & $\mathbf{M}$ \\
\bottomrule
\end{tabular}
\end{center}
\noindent
For Heisenberg ($\alpha = 0$, $S_4 = 0$):
all Hankel invariants vanish.
For affine Kac--Moody ($S_4 = 0$, $\alpha \neq 0$):
 succeeded in 52ms:
\begin{proposition}[Shadow coefficient rationality;
\ClaimStatusProvedHere]
\label{prop:shadow-coefficient-rationality}
\index{shadow coefficients!rationality|textbf}
\index{rationality!shadow tower}
For any chiral algebra with rational OPE structure
constants, every shadow coefficient $S_r(c)$ is a
rational function of the central charge~$c$. The
denominator has the form
$c^{r-3} \cdot (5c{+}22)^{\lfloor(r-2)/2\rfloor}$
\textup{(}up to a positive integer factor dividing~$r$\textup{)},
and the numerator is a polynomial of degree
$\lfloor(r{-}4)/2\rfloor$.
\end{proposition}

\begin{proof}
The convolution recursion
$a_n = -(2c)^{-1}\sum_{j=1}^{n-1} a_j a_{n-j}$ with
$a_0 = c$, $a_1 = 6$, $a_2 = 40/(c(5c{+}22))$ produces
rational functions of~$c$ by induction: each step involves

thinking
**Investigating theorem labels**

I noticed that the label `thm:nms-betagamma-quartic-birth` isn’t found. Perhaps the label has been changed to something like `thm:betagamma-quartic-birth` or maybe it’s under `cor:nms`? The proof seems to cite a missing label, which is concerning. I think I need to search for the exact theorem reference, considering it might be an unresolved label. There’s a strong need to look into anything related to beta gamma.
codex
The `βγ` realization surface is unstable. In the example chapter, the same quartic object is described as “appears” and then immediately set to zero on the weight-changing line, while the depth theorem later needs a nonzero quartic to realize class `C`. I’m tracing the exact labeled result it cites, because a mislabeled or internally inconsistent `βγ` theorem would break the only finite `d_alg=2` case.
exec
/bin/zsh -lc 'rg -n "betagamma-quartic-birth|beta.?gamma quartic birth|quartic birth|mu-vanishing|weight-changing line|rank-one abelian rigidity|contact quartic" chapters/examples/beta_gamma.tex chapters/theory/higher_genus_modular_koszul.tex chapters' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2065,2175p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2175,2275p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18590,18670p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:119:On the weight-changing line, the degree-$2$ shadow vanishes
chapters/examples/beta_gamma.tex:127:vanishes by rank-one abelian rigidity: class~C
chapters/examples/beta_gamma.tex:139:On the weight-changing line (the $\lambda$-marginal slice),
chapters/examples/beta_gamma.tex:143:though $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity).
chapters/examples/beta_gamma.tex:163:contact invariant $\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
chapters/examples/beta_gamma.tex:188:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}) implies no quartic
chapters/examples/beta_gamma.tex:205:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), terminates
chapters/examples/beta_gamma.tex:338:the degree-$2$ shadow restricted to the weight-changing line vanishes
chapters/examples/beta_gamma.tex:352:rank-one abelian rigidity
chapters/examples/beta_gamma.tex:2002:\section{The \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth and rank-one rigidity}
chapters/examples/beta_gamma.tex:2003:\label{sec:betagamma-quartic-birth}
chapters/examples/beta_gamma.tex:2004:\index{beta-gamma system@$\beta\gamma$ system!quartic birth}
chapters/examples/beta_gamma.tex:2034:On the weight-changing line, the genus-$0$ curvature vanishes ($m_0 = 0$) and the
chapters/examples/beta_gamma.tex:2042:On the weight-changing line, the Maurer--Cartan equation is linear
chapters/examples/beta_gamma.tex:2052:By rank-one abelian rigidity
chapters/examples/beta_gamma.tex:2053:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}),
chapters/examples/beta_gamma.tex:2058:The tower terminates on the weight-changing line.
chapters/examples/beta_gamma.tex:2076:Theorem~\ref{thm:betagamma-quartic-birth} and
chapters/examples/beta_gamma.tex:2094:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth;
 succeeded in 51ms:
despite having shadow depth~$4$. In contrast, the direct
sum $\cH \oplus \cH$ shares the same weight multiset
$\{1,1\}$, the same character $\eta(q)^{-2}$, and the same
$\operatorname{ek} = 0$, but has shadow depth~$2$
(Gaussian, not contact). This is the decisive witness that
$\operatorname{ek}$ depends on the character while
$\kappa_d$ depends on the OPE
(Corollary~\ref{cor:two-faces-theta}).

\medskip
The formal statements are
Theorem~\ref{thm:betagamma-quartic-birth} and
Corollary~\ref{cor:betagamma-postnikov-termination} below.

\subsection{The weight/contact slice}

\begin{definition}[Weight/contact slice]
\label{def:betagamma-weight-contact-slice}
\index{weight/contact slice!beta-gamma@$\beta\gamma$}
Let $V_{\beta\gamma}$ be the \emph{minimal cyclic slice} generated by
 succeeded in 51ms:
\end{equation}
where:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $K_{0,2}^{\beta\gamma}$
 is the degree-$2$ corolla from the bilinear $\beta\gamma$ pairing;
\item $K_{0,3}^{\beta\gamma} = 0$
 \textup{(}cubic vanishes on the weight-changing line\textup{)};
\item $K_{0,4}^{\beta\gamma}
 = \operatorname{cyc}(m_3)$
 is the quartic contact corolla from the transferred operation~$m_3$,
 with $\mu_{\beta\gamma}
 := \langle\eta, m_3(\eta,\eta,\eta)\rangle = 0$
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing})};
\item $K_{1,1}^{\beta\gamma}$ is the genus-$1$ corolla;
\item $R_{\mathrm{pf}}^{\beta\gamma}$ is the rigid-cutting residue
 from the contact stratum of Mok's log-FM boundary
 \textup{(}Theorem~\textup{\ref{thm:logfm-modular-cocomposition})}.
\end{enumerate}
\end{proposition}

 succeeded in 51ms:
 \frac{\Delta_W}{\Delta_T}
 \;=\;
 \frac{512}{3\,(5c{+}22)^2},
 \end{equation}
 which decays as $c^{-2}$:
 the $W$-line interaction is suppressed relative to
 the $T$-line by two additional powers of the
 Lee--Yang denominator.

\item \emph{Class determination.}\enspace
 $\Delta = 0 \iff S_4 = 0$ \textup{(}given $\kappa \neq 0$\textup{)},
 and the vanishing locus of~$\Delta$ classifies the shadow depth:
 $\Delta = 0$ with $\alpha = 0$ gives class~$\mathbf{G}$;
 $\Delta = 0$ with $\alpha \neq 0$ gives class~$\mathbf{L}$;
 $\Delta \neq 0$ gives class~$\mathbf{M}$
 \textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)}.
\end{enumerate}
\end{corollary}

\begin{proof}
exec
/bin/zsh -lc "sed -n '18670,18720p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
either the sectors decouple (vanishing mixed OPE,
so $\Defcyc(L_1 \oplus L_2)
= \Defcyc(L_1) \oplus \Defcyc(L_2)$
by Proposition~\ref{prop:independent-sum-factorization},
giving $d_{\mathrm{alg}}
\leq \max(d_{\mathrm{alg},1},\, d_{\mathrm{alg},2}) \leq 2$),
or they couple (nonvanishing mixed bracket,
$\alpha \neq 0$ on the mixed sector, activating the
cubic pump and forcing $r_{\max} = \infty$
on every reachable sector).
A rank-$n$ abelian system with cross-sector quartic
sewing would require
$\dim \Defcyc^{(\mathbf{q}_1 + \mathbf{q}_2)} > 0$
for distinct fundamental charges $\mathbf{q}_1, \mathbf{q}_2$;
but for decoupled sectors this dimension vanishes, and
for coupled sectors the cubic pump gives
$d_{\mathrm{alg}} = \infty$.
The algebraic shadow depth
$d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
therefore exhausts the classes
exec
/bin/zsh -lc "rg -n -F '\\label{thm:nms-betagamma-quartic-birth}' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./appendices/nonlinear_modular_shadows.tex:1143:\label{thm:nms-betagamma-quartic-birth}
exec
/bin/zsh -lc "sed -n '1120,1185p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1185,1265p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{cor:nms-betagamma-mu-vanishing}' appendices/nonlinear_modular_shadows.tex chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Derived center interpretation: Lie/tree class]
\label{rem:nms-affine-derived-center}
In the chiral derived center, the cubic shadow
$\mathfrak{C}_{\mathrm{aff}} \in \cZ^1$ is a degree-$1$
Gerstenhaber algebra element (a bulk derivation), and the quartic
contact vanishes in the standard gauge:
$[\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{aff}}] = 0$ in $\cZ^2$.
The open/closed quartic resonance class reduces to the tree correction:
$\mathfrak{R}^{\mathrm{oc}}_4(\widehat{\mathfrak{g}}_k)
= [\mathfrak{C} \star_{P} \mathfrak{C}] \in \cZ^2$
(Theorem~\ref{thm:thqg-oc-quartic-vanishing}(ii)).
This is the trace of cubic graviton exchange across a boundary node.
\end{remark}

\subsection{The \texorpdfstring{$\beta\gamma$}{betagamma} system}
\label{subsec:nms-betagamma}

\begin{definition}[Weight/contact slice]
\label{def:nms-betagamma-slice}
Let $V_{\beta\gamma}$ be the minimal cyclic slice generated by the explicit weight-changing deformation class and the first contact class detected by the first nontrivial higher operation $m_3$.
 succeeded in 52ms:
the weight-changing line is a one-dimensional cyclic subspace with
vanishing higher brackets.
Computational verification: \texttt{compute/lib/betagamma\_quartic\_contact.py}.
\end{proof}

\begin{corollary}[Pure contact boundary law; \ClaimStatusProvedHere]
\label{cor:nms-betagamma-boundary-law}
On the weight/contact slice of $\beta\gamma$ one has
\[
\xi^*\mathfrak Q_{\beta\gamma}
=
H_{\beta\gamma}\star_{P_{\beta\gamma}}\mathfrak Q_{\beta\gamma}
+
\mathfrak Q_{\beta\gamma}\star_{P_{\beta\gamma}}H_{\beta\gamma}.
\]
There is no cubic tree contribution.
\end{corollary}

\begin{proof}
Apply the quartic boundary recursion with $\mathfrak C_{\beta\gamma}=0$.\qedhere
 succeeded in 51ms:
appendices/nonlinear_modular_shadows.tex:1167:\label{cor:nms-betagamma-mu-vanishing}

thinking
**Investigating algebraic properties**

I need to inspect the betagamma-rank-one-rigidity theorem, which might indicate that one line vanishes, but the full slice has quartic behavior. I should search for the theorem and check the free_fields proposition. I'm curious if a multi-generator full algebra can have a d_alg of 2, even with a weight-changing line where the quartic invariant vanishes. It sounds like contacting the stratum might reveal different lines. I also need explicit proof of d_alg=2 in the beta_gamma example and a summary around line 2700.
codex
The appendix confirms the core `βγ` tension rather than resolving it: on the named weight-changing line, `Q_{βγ}(η^4)=μ_{βγ}` and a proved corollary sets `μ_{βγ}=0`. If that line is the claimed class-`C` witness, it does not realize a nonzero quartic there. I’m reading the later `βγ` summary statements to see whether the manuscript quietly switches from the line to a larger slice.
exec
/bin/zsh -lc "sed -n '1128,1215p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2688,2755p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1848,1875p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"d_{\\\\mathrm{alg}} = 2|class.?C|weight/contact slice|weight-changing line|quartic.*nonzero|mu_\\{\\\\beta\\\\gamma\\}|m_4|m_3\" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/connections/arithmetic_shadows.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For $\beta\gamma$: $d = 4$
(Theorem~\ref{thm:shadow-archetype-classification}(iii)),
$d_{\mathrm{arith}} = 1$ (the primary-counting function
$\widehat{Z}^c_{\beta\gamma} = y\,|\theta_3/\eta|^2$
has $|\theta_3|^2$ holomorphic and $|\eta|^{-2}$ producing
a non-holomorphic Maass spectral component; the Hecke
decomposition of $|\theta_3|^2$ contributes one eigenform,
giving one critical line at $\mathrm{Re}(s) = 1/2$),
$d_{\mathrm{alg}} = d - 1 - d_{\mathrm{arith}} = 4 - 1 - 1 = 2$.
The homotopy defect $d_{\mathrm{alg}} = 2$ comes from the
contact quartic $\mathfrak{Q}_{\beta\gamma} \neq 0$
(Theorem~\ref{thm:betagamma-quartic-birth}):
two $A_\infty$-operations ($m_3, m_4$) are nonzero beyond
$m_2$, contributing shadow depths $3$ and $4$ to the
homotopy side.
For minimal-model Virasoro: $d_{\mathrm{arith}}$ is finite
(finitely many primaries) but $d_{\mathrm{alg}} = \infty$:
all transferred operations $m_n$ are nonzero for $n \geq 2$
(Theorem~\ref{thm:shadow-tower-asymptotics}, $S_n(c) \neq 0$
for all $n \geq 4$ and $c \notin \{0, -22/5\}$).
 succeeded in 52ms:
 \label{eq:bg-S4-Tline}
\end{alignat}
and $S_r \neq 0$ for all $r \geq 2$.
The restriction to the T-line has infinite shadow depth
\textup{(}class~M on the one-dimensional slice\textup{)}.
\end{proposition}

\begin{proof}
The shadow invariants on the T-line are the Virasoro shadow invariants
at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
$S_3 = 2$ from the universal Virasoro cubic (the coefficient of
$z^{-3}$ in the $r$-matrix, which is one pole order below the $z^{-4}$
OPE pole by pole absorption), and $S_4 = Q^{\mathrm{contact}}_{\mathrm{Vir}}(c) =
10/(c(5c+22))$. The critical discriminant
$\Delta = 8\kappa S_4 = 40/(5c+22)$ is nonzero for all real~$\lambda$
(the denominator $5c+22 = 60\lambda^2 - 60\lambda + 32$ has negative
discriminant $-4080 < 0$), so the T-line tower does not terminate
(Theorem~\ref{thm:single-line-dichotomy}).\qedhere
\end{proof}

 succeeded in 52ms:
$r_{\max} = \infty$ in class~$\mathsf{M}$ is absent.

\item[\textup{(ii)}]
\textbf{The Sugawara composite produces a nonzero quartic contact.}
The stress tensor
$T_\lambda = (1{-}\lambda)\normord{\beta\,\partial\gamma}
- \lambda\,\normord{(\partial\beta)\,\gamma}$
is a \emph{composite} field: it is not a generator of the vertex algebra
but a quadratic expression in the generators.
The $TT$ OPE has a quartic pole with coefficient
$c_{\beta\gamma}(\lambda)/2 = 6\lambda^2 - 6\lambda + 1$,
and the transferred operation $m_3$ inherits a nontrivial
quartic contact corolla $\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
$($Theorem~\textup{\ref{thm:betagamma-quartic-birth}}$)$.
This composite interaction is invisible at the generator level
but creates genuine shadow depth beyond degree~$3$.

\item[\textup{(iii)}]
\textbf{Stratum separation kills the quintic pump.}
The cyclic deformation complex decomposes by charge:
 exited 2 in 51ms:
rg: regex parse error:
    (?:d_{\mathrm{alg}} = 2|class.?C|weight/contact slice|weight-changing line|quartic.*nonzero|mu_\{\beta\gamma\}|m_4|m_3)
          ^
error: repetition quantifier expects a valid decimal

thinking
**Inspecting global shadow depth**

I’m noticing there’s something about the free_fields theorem that relates to global shadow depth. I really want to explore the proof and check how the remainder is connected to it. There could be some interesting insights or implications there. I'll dive into it and see what I can uncover! It feels like there's more to discover in this topic, and I'm curious about what the proof might reveal.
exec
/bin/zsh -lc "sed -n '1215,1265p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
self-bracket exits the complex by rank-one rigidity; no further
obstruction propagates.

Therefore $r_{\max} = 4$: the tower terminates at the quartic level.\qedhere
\end{proof}

\begin{remark}[Why the T-line tower continues but the global tower stops]
\label{rem:betagamma-stratum-separation-mechanism}
\index{stratum separation!mechanism}
The phenomenon that the T-line restriction has infinite shadow depth
(class~M) while the full algebra has finite shadow depth (class~C) is
\emph{stratum separation}: the quintic obstruction $o_5$ couples
the cubic and quartic shadows, but these live on different strata
of the deformation complex. The cubic shadow is supported on the
T-direction, the quartic contact lives on the charged stratum, and
their Lie bracket vanishes because $\mathfrak{C}_{\beta\gamma} = 0$
on the weight-changing line removes the required input.
Stratum separation is an intrinsically multi-channel
effect; it cannot occur for single-generator algebras, where the
shadow obstruction tower on the unique primary line \emph{is} the global tower.

thinking
**Verifying the theorem**

I think I should verify the theorem `thm:single-line-dichotomy`. The proof suggests that a closed form makes things clear. If this theorem already proves a gap, then the proposition might just be a duplicate. It's crucial for me to check the scope of the theorem to fully understand it. Alright, I’m ready to dive in and read it closely!
codex
A deeper structural problem is emerging in the `βγ` witness: the repo contains a proved theorem that the T-line restriction has infinite shadow depth, and another proved theorem that the global `βγ` tower stops at degree 4. Unless “restriction” is being used in a very nonstandard way, a global vanishing should not coexist with an infinite nonzero restriction to a slice. I’m checking the exact statements and line-level definitions before I record that as a genuine contradiction.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '1128,1245p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17095,17265p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16080,16495p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17880,17975p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1128	 \label{eq:bg-S4-Tline}
  1129	\end{alignat}
  1130	and $S_r \neq 0$ for all $r \geq 2$.
  1131	The restriction to the T-line has infinite shadow depth
  1132	\textup{(}class~M on the one-dimensional slice\textup{)}.
  1133	\end{proposition}
  1134	
  1135	\begin{proof}
  1136	The shadow invariants on the T-line are the Virasoro shadow invariants
  1137	at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
  1138	$S_3 = 2$ from the universal Virasoro cubic (the coefficient of
  1139	$z^{-3}$ in the $r$-matrix, which is one pole order below the $z^{-4}$
  1140	OPE pole by pole absorption), and $S_4 = Q^{\mathrm{contact}}_{\mathrm{Vir}}(c) =
  1141	10/(c(5c+22))$. The critical discriminant
  1142	$\Delta = 8\kappa S_4 = 40/(5c+22)$ is nonzero for all real~$\lambda$
  1143	(the denominator $5c+22 = 60\lambda^2 - 60\lambda + 32$ has negative
  1144	discriminant $-4080 < 0$), so the T-line tower does not terminate
  1145	(Theorem~\ref{thm:single-line-dichotomy}).\qedhere
  1146	\end{proof}
  1147	
 succeeded in 50ms:
 17095	The Gaussian decomposition reduces the entire shadow tower to a
 17096	single algebraic question: is $Q_L(t)$ a perfect square in
 17097	$k(c)[t]$? Because $Q_L$ is quadratic in~$t$, the answer is
 17098	governed by a classical dichotomy. A quadratic polynomial is a
 17099	perfect square if and only if its discriminant vanishes; when it
 17100	does, $\sqrt{Q_L}$ is linear and the tower terminates after
 17101	finitely many terms; when it does not, $\sqrt{Q_L}$ is
 17102	irrational over the polynomial ring and the binomial series for
 17103	$(1+u)^{1/2}$ produces infinitely many nonzero shadow
 17104	coefficients. There is no third possibility. The depth of the
 17105	shadow tower is not a free parameter: it is \emph{read off} from
 17106	the arithmetic of a single quadratic, and the only outcomes are
 17107	termination or infinite extent.
 17108	
 17109	\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
 17110	\label{prop:depth-gap-trichotomy}
 17111	\ClaimStatusProvedHere
 17112	\index{algebraic depth!gap theorem|textbf}
 17113	\index{shadow depth!forbidden values}
 17114	\index{depth classification!algebraic depth gap}
 succeeded in 51ms:
 17880	$r_* \to \infty$ (exact alternation in the semiclassical limit).
 17881	\end{remark}
 17882	
 17883	\begin{theorem}[Single-line dichotomy; \ClaimStatusProvedHere]
 17884	\label{thm:single-line-dichotomy}
 17885	\index{single-line dichotomy|textbf}
 17886	\index{shadow obstruction tower!single-line dichotomy}
 17887	\index{shadow depth!pump mechanism}
 17888	Let $L$, $S_r$, $\alpha$, $\Delta$, $Q_L$ be as above.
 17889	Then $r_{\max}|_L \in \{2,\,3,\,\infty\}$, classified by the
 17890	shadow metric:
 17891	\begin{enumerate}[label=\textup{(\roman*)}]
 17892	\item \emph{$\Delta = 0$, $\alpha = 0$
 17893	 \textup{(}class~$\mathbf{G}$\textup{)}.}\enspace
 17894	 $Q_L = (2\kappa)^2$, a constant.
 17895	 $H(t) = 2\kappa\,t^2$. Only $S_2$ survives: $r_{\max} = 2$.
 17896	
 17897	\item \emph{$\Delta = 0$, $\alpha \neq 0$
 17898	 \textup{(}class~$\mathbf{L}$\textup{)}.}\enspace
 17899	 $Q_L = (2\kappa + 3\alpha\,t)^2$, a perfect square.
 succeeded in 52ms:
 16080	\end{proof}
 16081	
 16082	\begin{definition}[Shadow depth classification]
 16083	\label{def:shadow-depth-classification}
 16084	\ClaimStatusProvedHere
 16085	\index{shadow depth|textbf}
 16086	\index{shadow depth!classification}
 16087	\index{shadow obstruction tower!depth classification}
 16088	Let $\cA$ be a modular Koszul chiral algebra with
 16089	obstruction classes $o_r(\cA)$ from
 16090	Construction~\ref{constr:obstruction-recursion}.
 16091	Define the \emph{shadow depth}
 16092	$\kappa_d(\cA) := r_{\max}(\cA) =
 16093	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16094	(with the convention $\kappa_d = \infty$ if the tower
 16095	does not terminate).
 16096	The \emph{shadow depth class} of~$\cA$ is determined
 16097	by the vanishing pattern of obstruction classes:
 16098	\begin{center}
 16099	\small
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17975,18035p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 17975	so $\sqrt{Q_L}$ is even, and $H(t)$ has only even powers,
 17976	giving $S_{2n+1} = 0$.
 17977	
 17978	Full pump: $R_5 = -3\alpha/(20\kappa^2) \neq 0$;
 17979	for $r \geq 5$, the vanishing loci $\{R_r = 0\}$ are
 17980	hypersurfaces of distinct degrees in
 17981	$\mathbb{A}^2_{\alpha,S_4}$,
 17982	with pairwise intersection in codimension~$\geq 2$;
 17983	generic parameters avoid all.
 17984	\end{proof}
 17985	
 17986	\begin{corollary}[Spectral curve]
 17987	\label{cor:spectral-curve}
 17988	\index{spectral curve!shadow tower}
 17989	The algebraic relation~\eqref{eq:riccati-algebraic-relation}
 17990	defines, for each primary line~$L$, a spectral curve
 17991	$\Sigma_L := \{H^2 = t^4 Q_L(t)\} \subset \mathbb{A}^2_{t,H}$.
 17992	Since $Q_L$ is quadratic in~$t$, $\Sigma_L$ has arithmetic
 17993	genus~$0$; the projection $(t,H) \mapsto t$ is a double cover
 17994	ramified at the zeros of~$Q_L$. The degeneration loci of~$\Sigma_L$

thinking
**Evaluating mathematical proofs**

I need to verify the proof for independent-sum-factorization and see if it assumes decoupling. That might be an important detail, but I'm wondering if it's enough on its own. I think it would help to search with "nl" to gather additional information. It’s essential to make sure I'm covering all my bases before coming to any conclusions. I'll dig into this further to clarify my understanding.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '27940,28030p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 27940	(a geometric identity), not by algebraic projection of
 27941	the MC equation at degree~$3$. The stable-graph YBE
 27942	$R^{\mathrm{mod}}_\cA(z;\hbar) \in \MC(Y^{\mathrm{mod}}_\cA)$
 27943	requires the MC equation at \emph{all degrees and genera}.
 27944	\end{remark}
 27945	
 27946	\begin{proposition}[Independent sum factorization]
 27947	\label{prop:independent-sum-factorization}
 27948	\ClaimStatusProvedHere
 27949	\index{shadow algebra!direct sum factorization}
 27950	\index{modular characteristic!additivity}
 27951	\index{independent sum!shadow factorization}
 27952	Let $L = L_1 \oplus L_2$ be a direct sum of cyclically
 27953	admissible Lie conformal algebras
 27954	(Definition~\textup{\ref{def:cyclically-admissible}})
 27955	with all mixed OPE coefficients vanishing. Then
 27956	the modular envelope splits:
 27957	\[
 27958	U_X^{\mathrm{mod}}(L)
 27959	\;\cong\;

thinking
**Investigating theorem details**

I notice that the theorem states the four values correspond bijectively to shadow depth classes, and there's a remark about shadow depth being related to algebraic complexity. However, the example table differentiates between `d` and `d_alg`, which could be confusing. I need to look more closely at the introduction and examples, particularly around AP131, and find the direct formula linking d_alg to r_max. It seems crucial to read the exact lines to clarify these connections.
exec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '118,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'r_{\\max} = 4' chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/beta_gamma.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'd_{\\mathrm{alg}} = \\max\\{r : m_r \\ne 0\\} - 2' chapters/connections/arithmetic_shadows.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18752,18785p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   118	zeta $\varepsilon^c_s$: one for each $L$-function
   119	factor in the Hecke decomposition of the lattice theta
   120	function. The algebraic component $d_{\mathrm{alg}} \ge 0$
   121	is the $A_\infty$ non-formality depth
   122	(Theorem~\ref{thm:ainfty-formality-depth}):
   123	$d_{\mathrm{alg}} = \max\{r : m_r \ne 0\} - 2$ for finite
   124	shadow depth, $d_{\mathrm{alg}} = \infty$ when all
   125	transferred operations are nonzero. For lattice vertex algebras,
   126	$d_{\mathrm{arith}} = 2 + \dim S_{r/2}$ is finite because
   127	the Hecke decomposition terminates. The shadow--spectral
   128	correspondence
   129	(Theorem~\ref{thm:shadow-spectral-correspondence})
   130	identifies each Hecke eigenform $f_j$ with a depth stratum.
 succeeded in 50ms:
chapters/connections/arithmetic_shadows.tex:123:$d_{\mathrm{alg}} = \max\{r : m_r \ne 0\} - 2$ for finite
chapters/connections/arithmetic_shadows.tex:123:$d_{\mathrm{alg}} = \max\{r : m_r \ne 0\} - 2$ for finite
 succeeded in 50ms:
chapters/examples/beta_gamma.tex:26:$r_{\max} = 4$. The shadow depth is not inherited from the pole
chapters/examples/beta_gamma.tex:128:($r_{\max} = 4$), beyond the Gaussian families
chapters/examples/beta_gamma.tex:190:degree~$4$ ($r_{\max} = 4$), so genus-$2$ corrections are purely
chapters/examples/beta_gamma.tex:234:The discrepancy between $k_{\max} = 0$ and $r_{\max} = 4$ arises
chapters/examples/beta_gamma.tex:264:$(r_{\max} = 4)$ but trivial commuting Hamiltonians. Any treatment of
chapters/examples/beta_gamma.tex:2674:$($shadow depth $r_{\max} = 4)$ despite being a free field.
chapters/examples/beta_gamma.tex:2745:The tower terminates at $r_{\max} = 4$: class~$\mathsf{C}$.
chapters/examples/free_fields.tex:85:($r_{\max} = 4$) by the same stratum separation mechanism; the
chapters/examples/free_fields.tex:705:Shadow depth $r_{\max} = 4$ (class~C).
chapters/examples/free_fields.tex:748:Shadow depth $r_{\max} = 4$ (class~C), the same as its Koszul dual
chapters/examples/free_fields.tex:772:$\beta\gamma$ and $bc$ are class~C with $r_{\max} = 4$.
chapters/examples/free_fields.tex:790:$r_{\max} = 4$ (class~C, contact/quartic archetype), with Virasoro
chapters/examples/free_fields.tex:814:kills the quintic obstruction for every $\lambda$, so $r_{\max} = 4$
chapters/examples/free_fields.tex:1175:The $\beta\gamma$ system has global shadow depth $r_{\max} = 4$
chapters/examples/free_fields.tex:1218:Therefore $r_{\max} = 4$: the tower terminates at the quartic level.\qedhere
chapters/examples/free_fields.tex:5511:Shadow archetype: C (contact/quartic, $r_{\max} = 4$).
chapters/examples/free_fields.tex:5566:Shadow archetype: C (contact/quartic, $r_{\max} = 4$),
chapters/theory/higher_genus_modular_koszul.tex:15247:\textbf{C} (contact, $r_{\max} = 4$): &
chapters/theory/higher_genus_modular_koszul.tex:16257:\item Class~$\mathbf{C}$ ($r_{\max} = 4$):
chapters/theory/higher_genus_modular_koszul.tex:16299:\item Class~$\mathbf{C}$ ($r_{\max} = 4$): quadratic BPS.
 succeeded in 50ms:
 18752	\begin{definition}[Generating depth vs algebraic depth]
 18753	\label{def:generating-depth}
 18754	Two distinct depths attach to the bar/shadow tower of a chiral algebra
 18755	$\cA$, and conflating them is forbidden.
 18756	
 18757	The \emph{generating depth} $d_{\mathrm{gen}}(\cA)$ is the smallest
 18758	degree~$N$ such that every higher transferred product $m_n$ for
 18759	$n > N$ on $\bar{H}^*(B(\cA))$ is determined recursively by
 18760	$\{m_2, \ldots, m_N\}$ via the $A_\infty$ relations. Equivalently,
 18761	$d_{\mathrm{gen}}$ is the smallest~$N$ such that the truncated
 18762	$A_\infty$-structure $(m_2, \ldots, m_N)$ already encodes the full
 18763	homotopy type of $B(\cA)$ as an $A_\infty$-coalgebra.
 18764	
 18765	The \emph{algebraic depth} $d_{\mathrm{alg}}(\cA)$ is the smallest
 18766	degree~$N$ such that $m_n = 0$ for all $n > N$ on $\bar{H}^*(B(\cA))$,
 18767	or $\infty$ if no such finite~$N$ exists.
 18768	
 18769	The two depths are not equal in general: trivially $d_{\mathrm{gen}}
 18770	\leq d_{\mathrm{alg}}$ when both are finite, but for class~$M$
 18771	algebras the inequality is strict in the strongest possible sense.

thinking
**Evaluating shadow invariants**

I'm noticing that the proposition states "shadow invariants on the T-line are the Virasoro shadow invariants." That seems contradictory, considering the implications. It feels like there’s a strong internal conflict here that I need to unpack further. I wonder how I can clarify this contradiction and what it means for the overall understanding of the topic. I might need to take a closer look at the definitions and implications involved.
codex
I’m checking one more layer of the `βγ` realization because the depth count itself may be misindexed. The arithmetic chapter claims `d_alg=2` because `m_3` and `m_4` are nonzero, but the `βγ` quartic-birth theorem says the first nonlinearity is quartic from `m_3` with no cubic shadow. If `m_4` is not actually established, then the finite `d_alg=2` witness collapses to `d_alg=1` or worse.
exec
/bin/zsh -lc "rg -n \"m_4.*beta|beta.?gamma.*m_4|two A_\\\\infty-operations|m_3, m_4|first higher operation m_3|quartic.*m_3|m_n\\(eta|m_4\\(|A_\\\\infty.*beta.?gamma\" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/connections/arithmetic_shadows.tex chapters/theory/higher_genus_modular_koszul.tex appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1140,1185p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '2088,2160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '1854,1862p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:m_4.*beta|beta.?gamma.*m_4|two A_\infty-operations|m_3, m_4|first higher operation m_3|quartic.*m_3|m_n\(eta|m_4\(|A_\infty.*beta.?gamma)
                                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1140	\end{definition}
  1141	
  1142	\begin{theorem}[\texorpdfstring{$\beta\gamma$}{betagamma} quartic birth; \ClaimStatusProvedHere]
  1143	\label{thm:nms-betagamma-quartic-birth}
  1144	On the weight/contact slice one has
  1145	\[
  1146	\mathfrak C_{\beta\gamma}=0,
  1147	\qquad
  1148	\mathfrak o_{\beta\gamma}^{(4)}=0,
  1149	\qquad
  1150	\mathfrak Q_{\beta\gamma}=\operatorname{cyc}(m_3).
  1151	\]
  1152	Equivalently, the first nonlinear local shadow is quartic rather than cubic. Writing $\eta$ for the weight-changing class,
  1153	\[
  1154	\mathfrak Q_{\beta\gamma}(\eta,\eta,\eta,\eta)
  1155	=
  1156	\mu_{\beta\gamma},
  1157	\qquad
  1158	\mu_{\beta\gamma}:=\langle \eta,m_3(\eta,\eta,\eta)\rangle.
  1159	\]
 succeeded in 51ms:
  2088	to the moduli of deformations spanned by the class $\eta$ that shifts
  2089	conformal weight $\lambda \mapsto \lambda + \epsilon$.
  2090	\end{definition}
  2091	
  2092	\subsection{Quartic birth}
  2093	
  2094	\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth;
  2095	\ClaimStatusProvedHere]
  2096	\label{thm:betagamma-quartic-birth}
  2097	\index{quartic birth!beta-gamma@$\beta\gamma$}
  2098	On the weight/contact slice
  2099	(Definition~\textup{\ref{def:betagamma-weight-contact-slice}}), one has
  2100	\[
  2101	 \mathfrak{C}_{\beta\gamma} = 0,
  2102	 \qquad
  2103	 \mathfrak{o}_{\beta\gamma}^{(4)} = 0,
  2104	 \qquad
  2105	 \mathfrak{Q}_{\beta\gamma} = \operatorname{cyc}(m_3).
  2106	\]
  2107	Equivalently, the first nonlinear local shadow is quartic rather than
 succeeded in 51ms:
  1854	decomposition of $|\theta_3|^2$ contributes one eigenform,
  1855	giving one critical line at $\mathrm{Re}(s) = 1/2$),
  1856	$d_{\mathrm{alg}} = d - 1 - d_{\mathrm{arith}} = 4 - 1 - 1 = 2$.
  1857	The homotopy defect $d_{\mathrm{alg}} = 2$ comes from the
  1858	contact quartic $\mathfrak{Q}_{\beta\gamma} \neq 0$
  1859	(Theorem~\ref{thm:betagamma-quartic-birth}):
  1860	two $A_\infty$-operations ($m_3, m_4$) are nonzero beyond
  1861	$m_2$, contributing shadow depths $3$ and $4$ to the
  1862	homotopy side.

thinking
**Evaluating the theorem and dependencies**

I’m looking at dependency lines and wondering if this remark can indeed be proved, despite lacking an actual theorem. There might be unsupported claims, particularly regarding potential confusion about the arithmetic shadows and their implications for m3 and m4. It seems important to focus on theorem proof as requested, which leads me to consider mediums and issues of propagation. I should target my search for the relevant theorem specifically around beta_gamma to verify m4’s status.
codex
The proof’s remaining weak point is the multi-sector jump. The main proposition treats it as proved, but the only cited support is a remark about “cubic pump” and sector decoupling. I’m checking whether an actual theorem establishes that dichotomy or whether the proof is leaning on unproved narrative at the exact place where a `d_alg=3` counterexample could hide.
exec
/bin/zsh -lc "rg -n -F 'm_4' chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/connections/arithmetic_shadows.tex appendices/nonlinear_modular_shadows.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'cubic pump' chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '2514,2565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:betagamma-rank-one-rigidity}' chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/nonlinear_modular_shadows.tex:52:\item $t_g^{(3)}$: involves $m_4$ and $m_3 \circ m_3$ terms,
chapters/examples/beta_gamma.tex:28:degree~$4$ detected by the transferred $A_\infty$ operation $m_4$.
chapters/theory/higher_genus_modular_koszul.tex:14543:vertex from~$m_4$. If $[o_4] = 0$, define
chapters/theory/higher_genus_modular_koszul.tex:16630: $m_4 \neq 0$ from the contact quartic, $m_k = 0$ for
chapters/theory/higher_genus_modular_koszul.tex:16703: $m_3^{\mathrm{SC}}{=}0$, $m_4^{\mathrm{SC}}{\neq}0$ &
chapters/theory/higher_genus_modular_koszul.tex:16743:stratum and $m_4^{\mathrm{SC}} \neq 0$ from the contact
chapters/connections/arithmetic_shadows.tex:1860:two $A_\infty$-operations ($m_3, m_4$) are nonzero beyond
chapters/connections/arithmetic_shadows.tex:6168:c/2 & m_3^\sharp(c,\rho;u_0) & m_4^\sharp(c,\rho;u_0)
 succeeded in 51ms:
chapters/examples/beta_gamma.tex:2678:\textbf{Abelianness kills the cubic pump.}
chapters/examples/beta_gamma.tex:2687:The cubic pump $\mathrm{ad}_{S_3}$ that drives the tower to
chapters/theory/higher_genus_modular_koszul.tex:17197:$L_1, \dotsc, L_n$, the cubic pump
chapters/theory/higher_genus_modular_koszul.tex:18665:$\mathbf{q}_0 + \mathbf{q}$: the cubic pump is
chapters/theory/higher_genus_modular_koszul.tex:18678:cubic pump and forcing $r_{\max} = \infty$
chapters/theory/higher_genus_modular_koszul.tex:18685:for coupled sectors the cubic pump gives
chapters/examples/beta_gamma.tex:2678:\textbf{Abelianness kills the cubic pump.}
chapters/examples/beta_gamma.tex:2687:The cubic pump $\mathrm{ad}_{S_3}$ that drives the tower to
chapters/theory/higher_genus_modular_koszul.tex:17197:$L_1, \dotsc, L_n$, the cubic pump
chapters/theory/higher_genus_modular_koszul.tex:18665:$\mathbf{q}_0 + \mathbf{q}$: the cubic pump is
chapters/theory/higher_genus_modular_koszul.tex:18678:cubic pump and forcing $r_{\max} = \infty$
chapters/theory/higher_genus_modular_koszul.tex:18685:for coupled sectors the cubic pump gives
chapters/connections/concordance.tex:3838:cubic pump and forcing $d_{\mathrm{alg}} = \infty$).
 succeeded in 51ms:
  2514	\subsection{Vanishing of the quartic contact invariant}
  2515	
  2516	\begin{corollary}[Vanishing of the quartic contact invariant;
  2517	\ClaimStatusProvedHere]
  2518	\label{cor:betagamma-mu-vanishing}
  2519	\index{quartic contact invariant!vanishing}
  2520	On the weight-changing line of the $\beta\gamma$ system,
  2521	\[
  2522	 \mu_{\beta\gamma}
  2523	 \;:=\;
  2524	 \langle \eta,\, m_3(\eta,\eta,\eta) \rangle
  2525	 \;=\; 0.
  2526	\]
  2527	The quartic contact invariant vanishes identically on the weight-changing
  2528	deformation.
  2529	\end{corollary}
  2530	
  2531	\begin{proof}
  2532	Two independent arguments.
  2533	
 succeeded in 50ms:
chapters/examples/beta_gamma.tex:2560:\label{thm:betagamma-rank-one-rigidity}
chapters/examples/beta_gamma.tex:2560:\label{thm:betagamma-rank-one-rigidity}
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '2560,2588p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2560	\label{thm:betagamma-rank-one-rigidity}
  2561	\index{rank-one abelian rigidity}
  2562	Let $L \subset V_{\cA}$ be a one-dimensional cyclic subspace on which
  2563	all transferred higher brackets vanish:
  2564	\[
  2565	 \ell_n^{\mathrm{tr}}\big|_L = 0
  2566	 \qquad (n \ge 2).
  2567	\]
  2568	Then the restriction of the complementarity potential to $L$ is exactly
  2569	quadratic. In particular, complementarity on $L$ is formally fake.
  2570	\end{theorem}
  2571	
  2572	\begin{proof}
  2573	On such a line the cyclic action expansion collapses to its quadratic
  2574	Hessian part. Every higher jet
  2575	$\mathrm{Sh}_r(\Theta_{\cA})|_L$ for $r \ge 3$ involves at least one
  2576	factor of some $\ell_n^{\mathrm{tr}}$ with $n \ge 2$, and all such
  2577	factors vanish by hypothesis. The complementarity potential therefore
  2578	reduces to
  2579	\[
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '20,35p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    20	$\mathcal{W}_N$ (class~$\mathsf{M}$) run to infinity. The
    21	$\beta\gamma$ system is the sole representative of class~$\mathsf{C}$,
    22	the contact/quartic class: nontrivial beyond the scalar level, yet
    23	terminating at degree~$4$. Three invariants pin down the archetype
    24	: the maximal OPE pole order $p_{\max} = 1$, the collision
    25	depth $k_{\max} = p_{\max} - 1 = 0$, and the shadow depth
    26	$r_{\max} = 4$. The shadow depth is not inherited from the pole
    27	order; it arises from an independent contact interaction at
    28	degree~$4$ detected by the transferred $A_\infty$ operation $m_4$.
    29	The Koszul dual is the $bc$ ghost system
    30	(Theorem~\ref{thm:betagamma-fermion-koszul}), exchanging bosonic
    31	and fermionic statistics: the chiral lift of
    32	$\mathrm{Sym}(V)^! = \Lambda(V^*)$, with matching shadow invariants
    33	in opposite statistical sector. Two generators of complementary
    34	conformal weight $\lambda$ and $1-\lambda$, coupled by the simple-pole
    35	OPE $\beta(z)\gamma(w) \sim 1/(z{-}w)$, are the minimal data forcing




thinking
**Verifying classification statement**

I need to clarify the statement regarding `thm:shadow-archetype-classification`, which seems to suggest it points to one of F2, F3, F4, or M. I'm also considering how the definition at 16082 describes higher finite depths \(d \geq 5\) as realized by lattice VOAs. My goal is to ensure that my understanding aligns correctly with the definitions and classifications presented. Let’s dive into this further!
thinking
**Analyzing algebra claims**

I'm noticing that the statement "every chirally Koszul algebra in standard landscape belongs to exactly one of F2, F3, F4, or M" conflicts with a later paragraph in the same theorem regarding lattice VOAs of depths 5, 6, and 7. It makes me wonder if these higher-rank lattice VOAs are considered outside the "standard landscape." However, the example table does include them. It seems like the theorem may be overreaching its claims since it mentions that all are in this standard landscape.
thinking
**Clarifying lattice classifications**

I’m pondering how higher-rank lattices might still fall under class G because d_alg=0, even with total depths d=5 or 6 derived from arithmetic. That seems consistent. However, the shadow depth classification in lines 16137-16150 mentions finite shadow depths d≥5 realized by lattice VOAs, which contradicts theorem 16394-16397's claim that every chirally Koszul algebra belongs to F2, F3, F4, or M. Maybe the definition means total depth, but the text clarifies that shadow depth includes values from {2,3,4,...} and ∞. It feels like there's a real contradiction in the chapter!
thinking
**Examining depth classifications**

I’m considering that they might interpret higher total depths as being coarse in class G. That leads me to think that the definitions in lines 16137-16150 might actually misuse "shadow depth d" when they mean total depth. If that's true, it creates a definitional inconsistency. However, the user’s focus is more on the depth-gap proof. This inconsistency highlights a confusion between shadow depth, total depth, and d_alg, which is quite important to clarify!
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1142,1184p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '2516,2555p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '20,30p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '1856,1862p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18632,18699p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1142	\begin{theorem}[\texorpdfstring{$\beta\gamma$}{betagamma} quartic birth; \ClaimStatusProvedHere]
  1143	\label{thm:nms-betagamma-quartic-birth}
  1144	On the weight/contact slice one has
  1145	\[
  1146	\mathfrak C_{\beta\gamma}=0,
  1147	\qquad
  1148	\mathfrak o_{\beta\gamma}^{(4)}=0,
  1149	\qquad
  1150	\mathfrak Q_{\beta\gamma}=\operatorname{cyc}(m_3).
  1151	\]
  1152	Equivalently, the first nonlinear local shadow is quartic rather than cubic. Writing $\eta$ for the weight-changing class,
  1153	\[
  1154	\mathfrak Q_{\beta\gamma}(\eta,\eta,\eta,\eta)
  1155	=
  1156	\mu_{\beta\gamma},
  1157	\qquad
  1158	\mu_{\beta\gamma}:=\langle \eta,m_3(\eta,\eta,\eta)\rangle.
  1159	\]
  1160	\end{theorem}
  1161	
 succeeded in 50ms:
  2516	\begin{corollary}[Vanishing of the quartic contact invariant;
  2517	\ClaimStatusProvedHere]
  2518	\label{cor:betagamma-mu-vanishing}
  2519	\index{quartic contact invariant!vanishing}
  2520	On the weight-changing line of the $\beta\gamma$ system,
  2521	\[
  2522	 \mu_{\beta\gamma}
  2523	 \;:=\;
  2524	 \langle \eta,\, m_3(\eta,\eta,\eta) \rangle
  2525	 \;=\; 0.
  2526	\]
  2527	The quartic contact invariant vanishes identically on the weight-changing
  2528	deformation.
  2529	\end{corollary}
  2530	
  2531	\begin{proof}
  2532	Two independent arguments.
  2533	
  2534	\medskip
  2535	\noindent\emph{Proof~1 (homotopy transfer).}
 succeeded in 51ms:
    20	$\mathcal{W}_N$ (class~$\mathsf{M}$) run to infinity. The
    21	$\beta\gamma$ system is the sole representative of class~$\mathsf{C}$,
    22	the contact/quartic class: nontrivial beyond the scalar level, yet
    23	terminating at degree~$4$. Three invariants pin down the archetype
    24	: the maximal OPE pole order $p_{\max} = 1$, the collision
    25	depth $k_{\max} = p_{\max} - 1 = 0$, and the shadow depth
    26	$r_{\max} = 4$. The shadow depth is not inherited from the pole
    27	order; it arises from an independent contact interaction at
    28	degree~$4$ detected by the transferred $A_\infty$ operation $m_4$.
    29	The Koszul dual is the $bc$ ghost system
    30	(Theorem~\ref{thm:betagamma-fermion-koszul}), exchanging bosonic
 succeeded in 51ms:
  1856	$d_{\mathrm{alg}} = d - 1 - d_{\mathrm{arith}} = 4 - 1 - 1 = 2$.
  1857	The homotopy defect $d_{\mathrm{alg}} = 2$ comes from the
  1858	contact quartic $\mathfrak{Q}_{\beta\gamma} \neq 0$
  1859	(Theorem~\ref{thm:betagamma-quartic-birth}):
  1860	two $A_\infty$-operations ($m_3, m_4$) are nonzero beyond
  1861	$m_2$, contributing shadow depths $3$ and $4$ to the
  1862	homotopy side.
 succeeded in 50ms:
 18632	\label{rem:contact-stratum-separation}
 18633	\index{contact class!stratum separation}
 18634	\index{stratum separation|textbf}
 18635	\index{rank-one abelian rigidity!stratum separation}
 18636	The single-line dichotomy governs
 18637	$r_{\max}|_L \in \{2,3,\infty\}$. The value
 18638	$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
 18639	requires \emph{stratum separation}.
 18640	The cyclic deformation complex decomposes by charge:
 18641	$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
 18642	For $\beta\gamma$, the quartic contact invariant
 18643	$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
 18644	lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 18645	The self-bracket
 18646	$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
 18647	has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
 18648	the quartic pump does not activate, so $r_{\max} = 4$.
 18649	This is rank-one rigidity
 18650	(Theorem~\ref{thm:betagamma-rank-one-rigidity})
 18651	as stratum separation.

thinking
**Inspecting chapter details**

I need to check the contents of `chapters/examples/beta_gamma.tex`, specifically around line 2670. It seems like there’s a summary related to a cubic pump that I want to look at. I wonder what specific aspects of the pump are covered and if there are any key takeaways or details that could be particularly interesting or relevant for my context. Let’s look at that closely!
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '2668,2748p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2668	\label{prop:betagamma-sugawara-class-c}
  2669	\ClaimStatusProvedHere
  2670	\index{beta-gamma system@$\beta\gamma$ system!class C mechanism}
  2671	\index{stratum separation!class C mechanism}
  2672	\index{Sugawara construction!class C depth}
  2673	The $\beta\gamma$ system is class~$\mathsf{C}$
  2674	$($shadow depth $r_{\max} = 4)$ despite being a free field.
  2675	Three independent mechanisms interact to produce this classification:
  2676	\begin{enumerate}
  2677	\item[\textup{(i)}]
  2678	\textbf{Abelianness kills the cubic pump.}
  2679	The generator OPE
  2680	$\beta(z)\gamma(w) \sim 1/(z{-}w)$ has a simple pole:
  2681	$d\log$ absorption gives collision depth $k_{\max} = 0$ and the degree-$2$ transferred bracket vanishes on
  2682	the weight-changing line
  2683	$($Lemma~\textup{\ref{lem:betagamma-ell2-vanishing}}$)$.
  2684	Every ternary bracket factors through the vanishing binary bracket:
  2685	$\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$
  2686	$($Proposition~\textup{\ref{prop:betagamma-ell3-vanishing}}$)$.
  2687	The cubic pump $\mathrm{ad}_{S_3}$ that drives the tower to
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7074,7083p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7074	 & SC-formality characterises class~$\mathbf{G}$:
  7075	 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
  7076	 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
  7077	 & abelian bracket $+$ nondegeneracy of~$\kappa$ \\
  7078	\ref{prop:depth-gap-trichotomy}
  7079	 & Algebraic depth gap:
  7080	 $d_{\mathrm{alg}}(\cA) \in \{0,\,1,\,2,\,\infty\}$,
  7081	 no finite $d_{\mathrm{alg}} \geq 3$ realized
  7082	 \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)}
  7083	 & Riccati algebraicity $+$ $\Delta$-dichotomy \\





thinking
**Evaluating theorem validity**

I see that the core theorem surface appears to be unsupported. The statement includes class C, which is under an excluded hypothesis, making it questionable. It seems the proof relies on contradictory βγ material, which is a concern. I should really dig deeper into these elements to ensure clarity and correctness. There’s definitely something here that needs more careful consideration.
thinking
**Evaluating logical constraints**

I need to compute direct logic to show that a statement with κ≠0 cannot belong to class C. The proof indicates that class C emerges only when κ=0 on the primary line. So, the theorem shouldn't suggest that four values correspond bijectively to classes under κ≠0. I might articulate my findings using specific lines from the higher genus modular Koszul classification and other relevant references. I wonder if citing multiple file:line segments might clarify things.
thinking
**Considering formatting options**

I’m thinking about using plain lines without a header, but I’m not entirely sure if that’s the best approach. The user's contract expects things ordered by severity, so I might want to list them from highest to lowest. However, I’m considering whether severity groups should be listed separately instead of being sorted as well. It could be a clean final output, but I need to include the exact file references.
thinking
**Crafting precise descriptions**

I’m organizing findings by severity, starting with critical, then high, and medium. I might mention an additional medium finding regarding the theorem using d_alg before its formal definition, though it’s not essential. I want to ensure that each description is grounded and avoids speculation, only making clear inferences. For finding 4, I can phrase it as "I found no proved theorem in the cited support," and label it as an inference. I’ll craft this carefully!
thinking
**Finalizing the theorem descriptions**

I want to clearly state that I didn’t find a proved theorem in the cited dependency chain that excludes a mixed-sector finite quintic obstruction, as the proof refers only to a remark and a decoupling proposition. I might need to include exact line references, like `17195-17205`, while remembering to start with one file:line. I’ll craft the final version with five bullets and a summary paragraph, ensuring I follow the user contract strictly without adding extra commentary.
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:17115 — `prop:depth-gap-trichotomy` is over-scoped as stated. It assumes `\kappa\neq 0` on the primary line, but its own proof says the only `d_{\mathrm{alg}}=2` case is the boundary case `\kappa|_L=0` for `\beta\gamma` (`17167-17176`). Under the stated hypothesis, the rank-one argument only yields `d_{\mathrm{alg}}\in\{0,1,\infty\}`, not the claimed `{0,1,2,\infty}` or a bijection with all four classes.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:16414 — The class-`C` witness is internally contradicted by its own cited dependencies. This theorem says `\beta\gamma` on the weight-changing line has `\mathfrak Q_{\beta\gamma}\neq 0` and `r_{\max}=4`, but the imported `\beta\gamma` results prove the opposite on that line: `\mu_{\beta\gamma}=0` and the quartic contact invariant vanishes identically (`appendices/nonlinear_modular_shadows.tex:1166-1173`, `chapters/examples/beta_gamma.tex:2516-2528`), and one proved proposition even says the whole shadow tower vanishes there (`chapters/examples/free_fields.tex:1148-1166`). So the manuscript does not presently supply a stable realized `d_{\mathrm{alg}}=2` example on the claimed slice.

- [CRITICAL] chapters/examples/free_fields.tex:1171 — The proved `\beta\gamma` global-depth theorem contradicts the proved T-line theorem in the same file. The T-line proposition gives `S_r\neq 0` for all `r\ge 2` and infinite shadow depth (`1130-1145`), while the global theorem says `r_{\max}=4` and `S_5=0` globally despite `S_5\neq 0` on the T-line restriction (`1175-1178`). The follow-up remark (`1224-1231`) does not resolve that contradiction; it just restates it. Since the depth-gap proof relies on this stratum-separation story, the `d_{\mathrm{alg}}=2` realization is not trustworthy.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:17195 — The multi-sector extension is not actually proved at theorem strength. The proof jumps from the rank-one dichotomy to all multi-generator algebras by citing `Remark~rem:contact-stratum-separation` (`18632-18699`) plus decoupling (`27946-28001`). I did not find a proved theorem in that dependency chain excluding a finite mixed-sector quintic obstruction. That is exactly the step needed to rule out a genuine `d_{\mathrm{alg}}=3` counterexample beyond rank one.

- [MEDIUM] chapters/connections/arithmetic_shadows.tex:1857 — Downstream propagation of the class-`C` mechanism is unstable. This chapter says `d_{\mathrm{alg}}=2` because `m_3` and `m_4` are both nonzero (`1858-1861`), the `\beta\gamma` chapter introduction attributes class `C` to `m_4` (`chapters/examples/beta_gamma.tex:20-28`), but the quartic-birth theorem attributes the quartic to `\operatorname{cyc}(m_3)` instead (`chapters/examples/beta_gamma.tex:2098-2127`; appendix mirror at `1142-1163`). I did not find a proved local block here establishing a nonzero `m_4`, so the operation-count interpretation of `d_{\mathrm{alg}}=2` is not stably grounded.

## Summary
Instances checked: 18 | Violations found: 5 | Verdict: FAIL

The rank-one `\kappa\neq 0` argument does explain why `d_{\mathrm{alg}}=3` is impossible on a single primary line: once `S_4\neq 0`, either `S_5` or `S_6` survives, and the closed form then forces an infinite tail. What fails is the extension beyond that setting and, especially, the realization of the four values: `0`, `1`, and `\infty` are supported much better than `2`, whose `\beta\gamma` witness is contradictory across proved surfaces. I did not find a direct AP131 conflation inside the theorem block itself; the manuscript distinguishes `d_{\mathrm{gen}}(\mathrm{Vir})=3` from `d_{\mathrm{alg}}(\mathrm{Vir})=\infty` correctly. The failure mode here is scope/dependency collapse, not a bare `d_{\mathrm{gen}}` vs `d_{\mathrm{alg}}` mix-up.
tokens used
168,283
