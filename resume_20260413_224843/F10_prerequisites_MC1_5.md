# F10_prerequisites_MC1_5 (628s)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:10237 — PROBLEM: Theorem `thm:tautological-line-support` starts from total nilpotence `d_{\mathrm{bar}}^2=0`, then at 10293–10313 identifies the same obstruction with the fiberwise curvature `\dfib^{\,2}=\kappa\omega_g` and simply declares `\mathrm{obs}_g` and `o_g` to be the same class. That collapses the total/fiberwise distinction and leaves the load-bearing identification unproved; it also conflicts with the chapter’s own routing at 2996–3015, where `\mathrm{obs}_g=\kappa\lambda_g` is downstream of `\Theta_\cA`. FIX: Rewrite the theorem so the total differential is always `D_\cA^2=0`, the fiberwise statement is separately `d_{\mathrm{fib}}^2=\kappa\omega_g`, and insert a lemma proving the projection `d_{\mathrm{fib}}^2 \mapsto o_g`; if that lemma is unavailable, restrict the theorem to the unconditional genus-1 case and leave higher-genus/all-weight as downstream of Theorem D.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3894 — PROBLEM: `rem:theta-modular-twisting` calls
  `\partial\Theta^{(g)}+\pi\star\Theta^{(g)}+\Theta^{(g)}\star\pi+\cdots=\kappa(\cA)\omega_g`
  the “genus-$g$ component of the MC equation,” but the same remark ends at 3914–3915 by saying the MC equation is the nilpotent zero-RHS equation for `D_{\mathrm{tot}}`. This is an active flat/curved conflation. FIX: Rename 3894–3905 as the “fiberwise curved genus-$g$ identity,” explicitly say it is not the total Maurer–Cartan equation, and keep the zero-RHS MC equation only for the completed total differential.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2366 — PROBLEM: `thm:three-tier-architecture` says “Theorem D … holds unconditionally” and then says at 2370 that no Koszulity hypothesis is required. That contradicts the concordance, which scopes all-genera Theorem D to the proved uniform-weight lane and keeps genus 1 as the only universal case (`chapters/connections/concordance.tex:59`, `:64`). FIX: Replace item 0.4 with “genus-1 scalar universality holds unconditionally; all-genera scalar trace holds on the proved uniform-weight lane; multi-weight `g\ge2` requires `\delta F_g^{\mathrm{cross}}` via `thm:multi-weight-genus-expansion`,” and scope “No Koszulity hypothesis is required” only to Tier-0 items that actually use only `D_\cA^2=0`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:5816 — PROBLEM: `prop:mc2-reduction-principle` defines its coefficient package by reference to `Theorem~\ref{thm:universal-theta}`, but `thm:mc2-conditional-completion` at 8432–8437 later uses this proposition to recover `Theorem~\ref{thm:universal-theta}`. That is a paper-level circular chain in the comparison route. FIX: Remove the reference to `thm:universal-theta` from the proposition statement and define `W_g` independently as `\Gmod^{(g)}` or as explicit finite-dimensional subspaces of `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`; then add one sentence in `thm:mc2-conditional-completion` that this route is a downstream scalar-lane recovery of an already-constructed `\Theta_\cA`, not an independent proof of MC2.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:3790 — PROBLEM: `thm:universal-theta` claims existence of the cyclic `L_\infty` algebra `\Defcyc(\cA)`, but the proof at 3818–3847 only derives the MC identity from `D_\cA^2=0` and never cites the theorem that actually constructs `\Defcyc(\cA)` (`thm:cyclic-linf-graph`). As written, the proof proves “MC once the algebra exists,” not the existence claim in the theorem statement. FIX: Insert an explicit first sentence in the proof: “The cyclic deformation algebra `\Defcyc(\cA)` exists by `Theorem~\ref{thm:cyclic-linf-graph}`; `Theorem~\ref{thm:mc2-bar-intrinsic}` identifies `\Theta_\cA` as an MC element in its strict coinvariant model.”

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:3812 — PROBLEM: “This is Theorem~\ref{thm:master-theta} (MC2)” is too strong. The canonical master theorem in `chapters/connections/editorial_constitution.tex:218–237` is a package statement centered on `\Theta_\cA^{\le2}` and then cites `thm:mc2-bar-intrinsic` and `thm:recursive-existence` for the all-degree limit. The local theorem is the all-degree realization used to resolve MC2, not the master theorem verbatim. FIX: Change 3812 to “This theorem supplies the all-degree realization used in Theorem~\ref{thm:master-theta} (MC2).”

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:5282 — PROBLEM: `rem:mc2-status` says “The proof of Theorem~\ref{thm:universal-theta} assembles” from scalar shadow, determinant line bundle, spectral discriminant, and bar-coderivation algebra. After the bar-intrinsic proof at 3818–3847, that is stale and reverses outputs into prerequisites. FIX: Either retitle it “Historical route to MC2 (superseded)” and say so explicitly, or replace the list by the live proof chain `thm:bar-modular-operad -> thm:cyclic-linf-graph -> prop:geometric-modular-operadic-mc -> thm:mc2-bar-intrinsic -> thm:genus-universality + MK:verdier`.

- [LOW] chapters/theory/higher_genus_modular_koszul.tex:6004 — PROBLEM: `prop:geometric-modular-operadic-mc` invokes the Getzler–Kapranov correspondence directly on the completed tensor product `\widehat{L}_{\Gmod}` without stating the compatibility needed to pass from the classical Feynman-transform statement to this completed setting. That is a hidden import, not a checked hypothesis. FIX: Insert a lemma before 6004 verifying that completion preserves the relevant Feynman-transform algebra structure and that `\widehat{L}_{\Gmod}` remains in the scope of `GeK98`; otherwise downgrade the last sentence of part (c) to a conditional remark.

## DAG
- MC1 is `thm:master-pbw` (`chapters/connections/editorial_constitution.tex:193`). Its explicit inputs are `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, and `thm:pbw-allgenera-principal-w`; `thm:pbw-universal-semisimple` is an extension criterion, not part of the named-family proof. Status: satisfied only for the standard finite-type interacting families.

- Within this chapter’s own architecture (`chapters/theory/higher_genus_modular_koszul.tex:2347–2449`), intrinsic MC2 is not downstream of MC1. Tier 0 starts from `D_\cA^2=0`; Tier 1 adds genus-0 Koszulity; Tier 2 adds HS-sewing.

- MC2 intrinsic is `thm:universal-theta` / `thm:master-theta`, realized locally by `thm:mc2-bar-intrinsic`. The local dependency chain read from source is:
  `thm:bar-modular-operad -> thm:prism-higher-genus -> lem:stable-graph-d-squared -> thm:convolution-d-squared-zero -> const:explicit-convolution-bracket + def:modular-convolution-dg-lie + thm:convolution-dg-lie-structure -> prop:geometric-modular-operadic-mc -> thm:cyclic-linf-graph -> thm:genus-universality + MK:verdier -> thm:mc2-bar-intrinsic -> thm:universal-theta`.
  Status: acyclic and usable, modulo the proof-citation omission in finding 5.

- MC2 comparison lane is:
  `prop:mc2-reduction-principle -> prop:geometric-modular-operadic-mc -> thm:tautological-line-support -> thm:mc2-conditional-completion -> thm:mc2-full-resolution`.
  Status: not an independent proof. The file’s own routing at 2996–3015 makes Theorem D / genus universality downstream of `\Theta_\cA`, so this lane is circular if read as foundational.

- MC3 is the evaluation-generated-core package from `chapters/theory/introduction.tex:2068–2093`: `thm:categorical-cg-all-types + cor:dk23-all-types + cor:mc3-all-types`, with type-A reinforcement by `thm:mc3-type-a-resolution`. Status: satisfied on the evaluation-generated core; post-core enlargement remains downstream.

- MC4 is the structural completion package from `chapters/theory/higher_genus_modular_koszul.tex:912` and `chapters/connections/editorial_constitution.tex:522–529`: `thm:completed-bar-cobar-strong + thm:coefficient-stability-criterion + winfty rigidity`. Status: structural framework satisfied; H-level target identification remains open via `conj:master-infinite-generator`.

- MC5, as currently proved, is only the analytic lane from `chapters/theory/introduction.tex:2060–2070` and `chapters/connections/editorial_constitution.tex:531–543`:
  `thm:algebraic-string-dictionary (g=0) + thm:genus1-universal-curvature + thm:genus1-d-squared + thm:inductive-genus-determination + prop:2d-convergence + thm:general-hs-sewing`.
  Status: analytic sewing/convergence satisfied; full genuswise BV/BRST/bar identification remains open via `conj:v1-master-bv-brst`.

- Canonical master-chain status from `editorial_constitution.tex:498–543`: `evaluation-generated core -> MC3 enlargement -> MC4 H-level comparison -> MC5 physics completion`. No unavoidable global cycle survives on that chain. The only surviving circular surface is the old MC2 comparison lane inside this chapter.

## Summary
Checked: 15 surfaces | Findings: 8 | Verdict: FAIL


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
session id: 019d88ac-01c2-72b3-b978-39faa0fae2e3
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

For MC1-MC5: trace the dependency DAG. Which theorems depend on which? Is each dependency satisfied? Are there circular chains? List the complete DAG.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Planning skill usage**

I’m considering using the deep-beilinson-audit skill, and I might also run the build-surface skill if we decide to build. It’s essential for me to announce what skills I'm using in commentary. I'll need to open the skill file first and read up on the AGENTS. I should skim through CLAUDE and others, focusing on the first 120 lines or relevant sections. Since the user asked for an audit, I’ll inspect the file and its dependencies, while keeping frequent commentary updates. Time to get started!
codex
Auditing `chapters/theory/higher_genus_modular_koszul.tex` as a hostile review surface. I’m loading the required repo constitution files, the audit skill, and the target chapter first; then I’ll trace MC1–MC5 dependencies from source, attack the proof surface, and verify each finding against exact lines.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 50ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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



thinking
**Exploring dependencies in the target file**

I need a lot more information about the target file, especially regarding MC1-MC5 and their dependencies. It seems like I might need the entire file or at least sections around those points. I'll consider using a tool to search for the labels and references related to MC1-MC5. There's emphasis on tracing dependencies and checking if they're all satisfied, as well as making sure there are no circular chains. The user mentioned a foundation audit, so it might need a thorough review of everything.
thinking
**Reviewing claims systematically**

I realize it might be impossible to inspect all 266 claims in one go, so I’ll have to take a more systematic approach through the chapters using dependency graphs and scans for unresolved references. I should be honest about how many claims or blocks I’ve checked, as there will likely be significant findings. I'll use specific commands to search for labels and references within the file, gathering line numbers for easier organization. I'll even consider running searches in parallel to expedite the process.
codex
I’ve loaded the constitutional files and the audit skill. Next I’m mapping the chapter’s claim surface and locating the exact MC1–MC5 package so the dependency graph is grounded in source rather than memory.
exec
/bin/zsh -lc 'rg -n "thm:mc|prop:mc|lem:mc|cor:mc|def:mc|conj:mc" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\\\{(thm|prop|lem|cor|def|conj|rem):\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC1|MC2|MC3|MC4|MC5|mc1|mc2|mc3|mc4|mc5" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{(thm|prop|lem|cor|def|conj|rem):)
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
237:\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2353: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2651:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2708:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2807:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2825:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
2918:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3831:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3847:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3852:Theorem~\ref{thm:mc2-full-resolution} recovers the same MC class
3987:\label{thm:mc2-bar-intrinsic}
4224:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4232:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4325:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4380:Theorem~\ref{thm:mc2-bar-intrinsic}.
4514: Until that comparison is proved, Theorem~\ref{thm:mc2-bar-intrinsic}
4525:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
 succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
650:(Lemma~\ref{lem:mk67-from-mc2}). MK8 is the remaining
661:symmetry, Lemma~\ref{lem:mk67-from-mc2} adds MK6--MK7 as theorematic
684:Lemma~\ref{lem:mk67-from-mc2}. MK8 remains programmatic.
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
2353: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2651:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2708:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2807:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2825:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
2918:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3812:This is Theorem~\ref{thm:master-theta} (MC2).
3813:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3831:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3847:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3852:Theorem~\ref{thm:mc2-full-resolution} recovers the same MC class
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   35739 chapters/theory/higher_genus_modular_koszul.tex

thinking
**Analyzing file sections**

I need the whole file since it's quite large, focusing on target sections like MC1-MC5 and any unresolved references. I might consider using a script to analyze labels and references, wondering if the explorer agent would be necessary, though using exec might be enough. I'll look into using rg patterns to identify MC1-MC5 labels like "universal-theta" while searching for "MC1," "MC3," "MC4," and "MC5." Theorem names could correspond to packages, so I'll use rg for that.
codex
The file is large enough that a blind read is not useful. I’m narrowing to the theorem blocks, proofs, and reference edges for the MC1–MC5 package, then I’ll audit the actual proof bodies and the definitions they import.
exec
/bin/zsh -lc "rg -n \"\\bMC1\\b|\\bMC3\\b|\\bMC4\\b|\\bMC5\\b|universal-theta|master-theta|sewing|comparison|periodicity\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3920,4305p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
421:(Remark~\ref{rem:nilpotence-periodicity}) holds at all genera:
464:\item\label{D:periodicity-htpy}
465:A \emph{periodicity profile}
467:\textup{(}Remark~\textup{\ref{rem:periodicity-triple})}.
585:\item\label{D:periodicity-dg}
586:A periodicity profile
588:(Remark~\ref{rem:periodicity-triple}).
673:(Theorem~\ref{thm:universal-theta}).
681:(Proposition~\ref{prop:dg-shifted-comparison}).
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
1157:comparison is therefore representation-theoretic rather than
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
2413:\textbf{Tier~2} \textup{(analytic input: HS-sewing)}.
2415:\item The sewing envelope $\cA^{\mathrm{sew}}$ exists
2416: \textup{(Definition~\ref{def:sewing-envelope})}.
2419: \textup{(Theorem~\ref{thm:general-hs-sewing})}.
2423: \textup{(Theorem~\ref{thm:heisenberg-one-particle-sewing})}.
2427: \textup{(Theorem~\ref{thm:lattice-sewing})}.
2435:HS-sewing is \emph{automatic}: the PBW theorem gives
 succeeded in 52ms:
extending from tree level to genus~$g$.
\end{remark}

\begin{proposition}[Centrality of higher-genus curvature;
 \ClaimStatusProvedHere]
\label{prop:curvature-centrality-general}%
\index{curvature!centrality!locality argument|textbf}%
\index{centrality!higher-genus curvature}%
For any chiral algebra~$\cA$ on a smooth projective curve~$X$
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
exec
/bin/zsh -lc "sed -n '5280,8605p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29580,30560p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
condition~(iv) of
Definition~\ref{def:v1-cyclically-admissible}.

\emph{Adjunction (iii).}
We construct the unit and counit explicitly.

\emph{Unit.} The natural map
$\eta_L \colon L \to
\operatorname{Prim}^{\mathrm{mod}}(U_X^{\mathrm{mod}}(L))$
sends each $a \in L$ to the corresponding degree-$1$ current
in the envelope. This is a primitive element because
$\bar\Delta(a) = 0$: the reduced coproduct of a generator
vanishes in the free factorization algebra modulo Lie
relations (generators are by definition cogenerators of
the bar coalgebra).

\emph{Counit.} Given $\varphi \colon L \to
\operatorname{Prim}^{\mathrm{mod}}(\cF)$ in
$\LCA_{\mathrm{cyc}}(X)$, define
$\tilde\varphi \colon U_X^{\mathrm{mod}}(L) \to \cF$
 succeeded in 52ms:
\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
\index{universal Maurer--Cartan class!proof history}
The proof of Theorem~\ref{thm:universal-theta} assembles:
(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
(ii)~the determinant line bundle with $c_1=\kappa\cdot\lambda$
(Remark~\ref{rem:homotopy-native-d});
(iii)~the spectral discriminant $\Delta_{\cA}(x)$
(Theorem~\ref{thm:spectral-characteristic});
(iv)~the cyclic deformation algebra on bar coderivations
(Proposition~\ref{prop:genus0-cyclic-coderivation}), with
MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.
Computationally verified for $\mathfrak{sl}_2$, $\mathfrak{sl}_3$,
$\mathfrak{sp}_4$, $\mathfrak{g}_2$ via
\texttt{compute/lib/mc2\_cyclic\_linf.py}.
\end{remark}

% ================================================================
% COMMENTED OUT: Detailed computational session notes (items v-ix)
% that formerly occupied ~270 lines. The mathematical content is
% captured in the four items above; the computational verification
codex
I have the MC2 proof surface. Now I’m extracting the chapter’s own packaging of MC1–MC5, because several later arguments appear to cite MC2 as if it settled more than it actually states.
exec
/bin/zsh -lc "rg -n \"\\\\label\\\\{thm:master-theta|\\\\label\\\\{thm:universal-theta|\\\\label\\\\{thm:.*mc[1-5]|\\\\label\\\\{prop:.*mc[1-5]|\\\\label\\\\{rem:.*mc[1-5]|\\\\label\\\\{cor:.*mc[1-5]\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "master-theta|universal-theta|MC1|MC2|MC3|MC4|MC5|master theorem|five-step|five packages|five conditions|five theorems" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3720,3925p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
 F_g(\cA)
 \;=\;
 F_g^{\mathrm{CEO}}(Q_L)
 \;+\;
 \delta_{\mathrm{pf}}^{(g,0)}(\kappa, S_3, \ldots, S_{2g}),
\]
partitions the genus-$g$ stable-graph sum into two disjoint,
exhaustive classes. The \emph{tree-like} graphs (no genus-$0$
vertex of valence~$\geq 3$) are accessible by iterated
codimension-$1$ degenerations and are computed by
Chekhov--Eynard--Orantin topological recursion on the spectral
curve $y^2 = Q_L(t)$
(Theorem~\ref{thm:riccati-algebraicity}). The
\emph{planted-forest} graphs (at least one genus-$0$ vertex of
valence~$\geq 3$) live on codimension-$\geq 2$ strata that
the CEO residue formula does not reach; their sum is
$\delta_{\mathrm{pf}}^{(g,0)}$. At genus~$1$, no planted-forest
graphs exist, so $\delta_{\mathrm{pf}}^{(1,0)} = 0$ and
$F_1 = F_1^{\mathrm{CEO}} = \kappa/24$. At genus~$2$,
 exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:master-theta|\label\{thm:universal-theta|\label\{thm:.*mc[1-5]|\label\{prop:.*mc[1-5]|\label\{rem:.*mc[1-5]|\label\{cor:.*mc[1-5])
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
673:(Theorem~\ref{thm:universal-theta}).
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2662: (Theorem~\ref{thm:universal-theta}):
2710:and~\ref{thm:universal-theta}).
2806:Theorem~\ref{thm:universal-theta}, made unconditional by
2825:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
3786:\label{thm:universal-theta}
3812:This is Theorem~\ref{thm:master-theta} (MC2).
3813:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3863:Theorem~\ref{thm:universal-theta} extends the canonical twisting
3960:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3986:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3989:\index{MC2!bar-intrinsic proof}
3990:\index{MC2!full generality}
4222:\begin{remark}[Scope of MC2 in this chapter]
4223:\index{MC2!coinvariant scope}
4224:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
exec
/bin/zsh -lc "sed -n '29660,30520p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\circ \eta_L$. Since $\eta_L(L) \subset
\operatorname{Prim}^{\mathrm{mod}}$, this restricts to the
primitive-current subalgebra. The six package components
$(\Fact, \barB, \Theta, \cL, (V^{\mathrm{br}}, T^{\mathrm{br}}),
\mathfrak{R}_4^{\mathrm{mod}})$ are successive projections of
$\Theta$ at degrees $0, 1, \ldots, 4$
(Corollary~\ref{cor:shadow-extraction}); each inherits the
primitive-current restriction.
\end{proof}

\begin{remark}
\label{rem:platonic-adjunction-classical}
\index{enveloping algebra!universal property}
Classically: $U(\fg) \dashv \mathrm{Prim}$ between Lie algebras
and cocommutative Hopf algebras (Milnor--Moore). Here: $L$ replaces
$\fg$, $\mathsf{Fact}_{\mathrm{cyc}}(X)$ replaces Hopf algebras,
$U_X^{\mathrm{mod}}$ replaces $U$. The modular
extension equips the envelope with the shadow obstruction tower
$\Theta_L$ of
Construction~\textup{\ref{constr:v1-platonic-package}}.
codex
I have the chapter’s MC2 statements. I’m now reading the local passages that mention MC1, MC4, and MC5 directly, because those are the places where the dependency chain is most likely to be misstated or silently broadened.
exec
/bin/zsh -lc "sed -n '1960,2065p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
Here the mode truncation has already been absorbed into the
finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
By the Whitehead--Chevalley--Eilenberg vanishing theorem,
$H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
finite-dimensional $\fg$-module~$N$ with no trivial summand,
since $\fg$ is semisimple. Therefore the non-trivial
enrichment is acyclic already at the $E_2$ page:
\[
E_2^{*,h}(g)_{\mathrm{enr,\, non\text{-}triv}} = 0.
\]

\emph{Invariant summands.}
The surviving $\fg$-invariant enrichment classes live in
$M_h^{\fg} \otimes H^{1,0}(\Sigma_g)$. On these, the
$d_2^{\mathrm{PBW}}$ differential acts through $T_{(1)} = L_0$
as proved above: the conformal vector is the unique weight-$2$
generator, and its $(1)$-product gives
$L_0|_{M_h^{\fg}} = h \cdot \mathrm{id}$. Since
exec
/bin/zsh -lc "rg -n \"\\\\label\\\\{thm:.*period|\\\\label\\\\{rem:.*period|\\\\label\\\\{thm:general-hs-sewing|\\\\label\\\\{thm:completed-bar-cobar-strong|\\\\label\\\\{conj:master-infinite-generator\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29590,30520p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "master theorem|master package|MC3|MC4|MC5|periodicity profile|sewing theorem|completed-bar-cobar-strong|master-infinite-generator|periodicity" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{thm:.*period|\label\{rem:.*period|\label\{thm:general-hs-sewing|\label\{thm:completed-bar-cobar-strong|\label\{conj:master-infinite-generator)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
in the envelope. This is a primitive element because
$\bar\Delta(a) = 0$: the reduced coproduct of a generator
vanishes in the free factorization algebra modulo Lie
relations (generators are by definition cogenerators of
the bar coalgebra).

\emph{Counit.} Given $\varphi \colon L \to
\operatorname{Prim}^{\mathrm{mod}}(\cF)$ in
$\LCA_{\mathrm{cyc}}(X)$, define
$\tilde\varphi \colon U_X^{\mathrm{mod}}(L) \to \cF$
as follows. At genus~$0$, the universal property of
the Nishinaka envelope~\cite{Nish26} extends $\varphi$
uniquely to a factorization algebra map
$\tilde\varphi_0 \colon \Fact_X(L) \to \cF$.
The extension to all genera is forced by the modular
bar construction: the map on $\barB(\Fact_X(L))$ induced
by $\tilde\varphi_0$ intertwines the stable-graph
differentials (since the bar construction is functorial
in algebra maps,
Theorem~\ref{thm:bar-modular-operad}), and the
 succeeded in 52ms:
421:(Remark~\ref{rem:nilpotence-periodicity}) holds at all genera:
464:\item\label{D:periodicity-htpy}
465:A \emph{periodicity profile}
467:\textup{(}Remark~\textup{\ref{rem:periodicity-triple})}.
585:\item\label{D:periodicity-dg}
586:A periodicity profile
588:(Remark~\ref{rem:periodicity-triple}).
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2049:stage; the completed MK3 statement is part of the MC4 package.
2647:\index{periodicity profile!in full package}
2680: \emph{periodicity profile}
2681: (Remark~\ref{rem:periodicity-triple});
2822:exponential $=$ periodicity profile~$\Pi_{\cA}$;
2844:periodicity profile~$\Pi_\cA$, and full MC
5576:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
9511:at level~(L3), $\Pi_{\cA}$ carries the periodicity data.
14852: \textup{(}Theorem~\textup{\ref{thm:completed-bar-cobar-strong}}),
14881:(Theorem~\ref{thm:completed-bar-cobar-strong}) applies directly:
16984:\label{rem:bott-periodicity-dichotomy}
16986:\index{Bott periodicity!shadow depth dichotomy}
codex
I’m pinning down the MC1–MC5 naming itself. The chapter already identifies MC2 explicitly; I’m searching for the same “This is … (MCx)” style anchors and the internal tables that route later claims through them.
exec
/bin/zsh -lc "rg -n \"\\(MC[1-5]\\)|MC[1-5]\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"This is Theorem~\\ref{thm:master-\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3812:This is Theorem~\ref{thm:master-theta} (MC2).
 succeeded in 52ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
3812:This is Theorem~\ref{thm:master-theta} (MC2).
3813:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3960:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3986:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3989:\index{MC2!bar-intrinsic proof}
3990:\index{MC2!full generality}
4222:\begin{remark}[Scope of MC2 in this chapter]
4223:\index{MC2!coinvariant scope}
4224:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4323:\index{MC2!foundational dependency chain}
4377:\index{Kontsevich--Soibelman!alternative construction of MC2}
4457:installed, it gives a redundant proof path to MC2.
4462:\index{Kontsevich--Soibelman!MC2 comparison}
4463:\index{wall-crossing!MC2 comparison}
4515: remains the primary proof of MC2 and
4523:\index{MC2!bar-intrinsic perspective}
4524:\index{MC2!two regimes}
exec
/bin/zsh -lc 'rg -n -F "master-pbw" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "(MC" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
29945:By PBW concentration (Theorem~\ref{thm:master-pbw}),
 succeeded in 51ms:
3812:This is Theorem~\ref{thm:master-theta} (MC2).
4274: font=\footnotesize] (MC) at (7.2,-0.3)
8367:\begin{enumerate}[label=\textup{(MC2-\arabic*)}]
8418:\textup{(MC2)} holds for~$\cA$.
9015:(iv)~semi-simple products (MC equation decouples).
10234:Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
10241:Hypothesis~\textup{\ref{mc2-hyp:tautological}} \textup{(MC2-3)}
10260:Hypothesis~(MC2-1) implies~(MC2-2) by
10264:modular-operadic clutching. It remains to establish~(MC2-3).
10317:With~(MC2-3) established, Theorem~\ref{thm:mc2-conditional-completion}
10318:now requires only~(MC2-1): the cyclic $L_\infty$ model.
10319:Hypothesis~(MC2-2) was already resolved conditionally on~(MC2-1) by
10320:Proposition~\ref{prop:geometric-modular-operadic-mc}, and~(MC2-3) is
10348:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
codex
The chapter only names MC2 explicitly. I’m searching the repo for the other master labels so the DAG uses the manuscript’s own theorem names rather than my reconstruction.
exec
/bin/zsh -lc 'rg -n -F "thm:master-pbw" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:master-theta" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1749: \phantomsection\label{thm:master-pbw}%
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1151: \textup{(}Theorem~\textup{\ref{thm:master-pbw})},
chapters/examples/w_algebras_deep.tex:1225:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:450:downstream of Theorem~\textup{\ref{thm:master-pbw}},
chapters/connections/editorial_constitution.tex:478:Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
chapters/connections/editorial_constitution.tex:554:Theorem~\ref{thm:master-pbw} $\to$ Future~2;
chapters/connections/editorial_constitution.tex:804:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
chapters/connections/outlook.tex:667:\phantomsection\label{thm:master-pbw}
metadata/theorem_registry.md:2365:| `thm:master-pbw` | `theorem` | 194 | Higher-genus PBW concentration for the standard finite-type interacting families |
metadata/dependency_graph.dot:236:  thm_master_pbw [label="thm:master-pbw\ntheorem [Pr]\nHigher-genus PBW concentration for the s...", style=filled, fillcolor="#c8e6c9"];
chapters/theory/bar_cobar_adjunction_inversion.tex:4083:(Theorem~\ref{thm:master-pbw}). The Virasoro algebra has a
chapters/theory/higher_genus_modular_koszul.tex:29945:By PBW concentration (Theorem~\ref{thm:master-pbw}),
metadata/label_index.json:42266:  "thm:master-pbw": {
metadata/claims.jsonl:225:{"label": "thm:master-pbw", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/editorial_constitution.tex", "line": 194, "title": "Higher-genus PBW concentration for the standard\n finite-type interacting families", "refs_in_block": ["thm:pbw-allgenera-km", "thm:pbw-allgenera-virasoro", "thm:pbw-allgenera-principal-w", "thm:pbw-universal-semisimple"]}
metadata/claims.jsonl:229:{"label": "conj:v1-master-bv-brst", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 434, "title": "BV/BRST/bar identification", "refs_in_block": ["thm:bv-bar-coderived", "thm:master-pbw", "thm:master-theta", "conj:master-dk-kl", "conj:v1-master-infinite-generator", "thm:algebraic-string-dictionary", "cor:string-amplitude-genus0"]}
metadata/claims.jsonl:1112:{"label": "thm:winfty-factorization-kd", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/w_algebras_deep.tex", "line": 1138, "title": "Factorization Koszul dual of\n\\texorpdfstring{$\\mathcal{W}_\\infty$}{W_infinity} via DS--sectorwise convergence", "labels_in_block": ["thm:winfty-factorization-kd", "eq:winfty-stage-kd"], "refs_in_block": ["thm:master-pbw", "eq:w3-kd-explicit", "thm:ds-koszul-intertwine", "eq:ds-bar-commute", "prop:winfty-factorization-package"]}
 succeeded in 52ms:
main.tex:1748: \phantomsection\label{thm:master-theta}%
metadata/dependency_graph.dot:237:  thm_master_theta [label="thm:master-theta\ntheorem [Pr]\nCyclic \texorpdfstring{$L_\infty$}{L-inf...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:2366:| `thm:master-theta` | `theorem` | 220 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, resolved)} |
metadata/claims.jsonl:226:{"label": "thm:master-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/editorial_constitution.tex", "line": 220, "title": "Cyclic \\texorpdfstring{$L_\\infty$}{L-infinity} deformation algebra and\nuniversal \\texorpdfstring{$\\Theta_\\cA$}{Theta\\_A} {\\normalfont (MC2, resolved)}", "refs_in_block": ["thm:mc2-bar-intrinsic", "thm:recursive-existence", "thm:mc2-full-resolution", "def:full-modular-package"]}
metadata/claims.jsonl:229:{"label": "conj:v1-master-bv-brst", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 434, "title": "BV/BRST/bar identification", "refs_in_block": ["thm:bv-bar-coderived", "thm:master-pbw", "thm:master-theta", "conj:master-dk-kl", "conj:v1-master-infinite-generator", "thm:algebraic-string-dictionary", "cor:string-amplitude-genus0"]}
metadata/claims.jsonl:230:{"label": "conj:standard-tower-mc5-reduction", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 573, "title": "Standard-tower MC5 reduction after MC3 and realized\nMC4", "refs_in_block": ["conj:master-dk-kl", "prop:winfty-mc4-frontier-package", "def:winfty-stage4-ward-normalized", "prop:yangian-typea-realization-criterion", "thm:yangian-typea-realization-plus-compacts", "thm:yangian-typea-realization-plus-fundamental-packet", "thm:algebraic-string-dictionary", "thm:master-theta"]}
metadata/claims.jsonl:231:{"label": "cor:standard-tower-mc5-closure", "env_type": "corollary", "status": "Conditional", "file": "chapters/connections/editorial_constitution.tex", "line": 664, "title": "Standard-tower MC5 closure on the canonical Yangian\nlocus", "refs_in_block": ["conj:master-dk-kl", "def:winfty-stage4-ward-normalized", "thm:yangian-formal-moduli-plus-core-realization", "thm:yangian-canonical-realization-plus-vector-line", "thm:algebraic-string-dictionary", "thm:master-theta"]}
metadata/claims.jsonl:2326:{"label": "thm:universal-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 3650, "title": "Universal modular Maurer--Cartan class", "refs_in_block": ["thm:master-theta", "thm:e1-mc-element", "chap:e1-modular-koszul"]}
metadata/label_index.json:42274:  "thm:master-theta": {
chapters/theory/higher_genus_modular_koszul.tex:3812:This is Theorem~\ref{thm:master-theta} (MC2).
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:451:Theorem~\textup{\ref{thm:master-theta}}, and
chapters/connections/editorial_constitution.tex:489:Theorem~\ref{thm:master-theta} (originally conjectured, now resolved
chapters/connections/editorial_constitution.tex:555:Theorem~\ref{thm:master-theta} $\to$ Futures~3, 4;
chapters/connections/editorial_constitution.tex:600: Theorem~\ref{thm:master-theta}.
chapters/connections/editorial_constitution.tex:658:Theorem~\ref{thm:master-theta}, compatibly with truncation, Verdier
chapters/connections/editorial_constitution.tex:690: Theorem~\ref{thm:master-theta}.
chapters/connections/editorial_constitution.tex:806:MC2 & \textbf{Proved} (Thm~\ref{thm:master-theta})
chapters/connections/editorial_constitution.tex:1564: $\Theta_{\cA}$ (Theorem~\ref{thm:master-theta}).
chapters/connections/concordance.tex:5523:(Theorem~\ref{thm:master-theta}).
exec
/bin/zsh -lc 'rg -n -F "thm:completed-bar-cobar-strong" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:general-hs-sewing" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "conj:master-infinite-generator" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
main.tex:1618: \phantomsection\label{thm:general-hs-sewing}% % genus_complete.tex
chapters/examples/lattice_foundations.tex:161:Theorem~\ref{thm:general-hs-sewing} then gives HS-sewing
metadata/dependency_graph.dot:398:  thm_general_hs_sewing [label="thm:general-hs-sewing\ntheorem [Pr]\nGeneral HS-sewing criterion", style=filled, fillcolor="#c8e6c9"];
chapters/connections/editorial_constitution.tex:181:\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/editorial_constitution.tex:463:Theorem~\ref{thm:general-hs-sewing} (HS-sewing at all genera)
chapters/connections/editorial_constitution.tex:541:(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
chapters/connections/editorial_constitution.tex:906:(Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/editorial_constitution.tex:2091:(Theorem~\ref{thm:general-hs-sewing}).
chapters/connections/editorial_constitution.tex:2655:(Theorem~\ref{thm:general-hs-sewing}); see also
chapters/connections/genus_complete.tex:1390:\label{thm:general-hs-sewing}%
chapters/connections/genus_complete.tex:1452:Theorem~\ref{thm:general-hs-sewing} must be checked in the completed
chapters/connections/thqg_introduction_supplement_body.tex:1457:Theorem~\textup{\ref{thm:general-hs-sewing}}.
chapters/connections/thqg_introduction_supplement_body.tex:1728:HS-sewing criterion (Theorem~\ref{thm:general-hs-sewing}) covers
chapters/connections/frontier_modular_holography_platonic.tex:3862:(Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth +
metadata/label_index.json:41434:  "thm:general-hs-sewing": {
metadata/claims.jsonl:34:{"label": "rem:depth-decomposition-universality", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/arithmetic_shadows.tex", "line": 1881, "title": "Universality and the complete $d_{\\mathrm{alg}}$ table", "refs_in_block": ["eq:depth-decomposition", "thm:general-hs-sewing", "thm:refined-shadow-spectral"]}
metadata/claims.jsonl:69:{"label": "thm:sewing-shadow-intertwining", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/arithmetic_shadows.tex", "line": 4823, "title": "Sewing--shadow intertwining at genus~$1$", "labels_in_block": ["thm:sewing-shadow-intertwining", "eq:sewing-shadow-intertwining"], "refs_in_block": ["thm:general-hs-sewing"]}
metadata/claims.jsonl:72:{"label": "thm:shadow-moduli-resolution", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/arithmetic_shadows.tex", "line": 4989, "title": "Shadow-moduli resolution", "labels_in_block": ["thm:shadow-moduli-resolution", "eq:shadow-moduli-implicit", "eq:shadow-moduli-leading"], "refs_in_block": ["thm:general-hs-sewing", "thm:shadow-spectral-measure", "eq:shadow-moduli-implicit"]}
metadata/claims.jsonl:104:{"label": "conj:cps-from-mc", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/arithmetic_shadows.tex", "line": 8103, "title": "CPS hypotheses from MC $+$ HS-sewing", "refs_in_block": ["rem:cps-conditional-status", "thm:general-hs-sewing", "thm:mc-recursion-moment"]}
metadata/claims.jsonl:218:{"label": "rem:four-test-interface", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 7813, "title": "The four-test interface", "refs_in_block": ["thm:bar-modular-operad", "thm:quantum-diff-squares-zero", "thm:mc2-bar-intrinsic", "thm:modular-characteristic", "thm:algebraic-family-rigidity", "thm:quantum-complementarity-main", "thm:shifted-symplectic-complementarity", "thm:general-hs-sewing", "thm:heisenberg-sewing", "op:multi-generator-universality", "thm:multi-weight-genus-expansion", "thm:heisenberg-bv-bar-all-genera", "conj:master-bv-brst", "conj:analytic-realization"]}
 succeeded in 50ms:
metadata/dependency_graph.dot:1493:  thm_completed_bar_cobar_strong [label="thm:completed-bar-cobar-strong\ntheorem [Pr]\nMC element lifts to the completed convol...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:130:| `thm:completed-bar-cobar-strong` | `theorem` | 953 | MC element lifts to the completed convolution algebra |
metadata/label_index.json:40470:  "thm:completed-bar-cobar-strong": {
metadata/claims.jsonl:173:{"label": "cor:anomaly-duality-w", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1196, "title": "Curvature complementarity for principal \\texorpdfstring{$\\mathcal{W}$}{W}-algebra pairs", "refs_in_block": ["thm:wn-obstruction", "thm:quantum-complementarity-main", "thm:w-algebra-koszul-main", "thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:228:{"label": "conj:v1-master-infinite-generator", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 317, "title": "H-level target identification for standard infinite towers", "refs_in_block": ["thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion", "def:finite-window"]}
metadata/claims.jsonl:1122:{"label": "comp:wn-stabilization-windows", "env_type": "computation", "status": "ProvedHere", "file": "chapters/examples/w_algebras_deep.tex", "line": 3150, "title": "Coefficient stabilization windows for $\\mathcal{W}_N$", "refs_in_block": ["thm:coefficient-stability-criterion", "thm:completed-bar-cobar-strong", "lem:degree-cutoff"]}
metadata/claims.jsonl:1250:{"label": "cor:completed-bar-cobar-yangian", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 2064, "title": "Completed bar-cobar equivalence for Yangians", "refs_in_block": ["thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:1293:{"label": "cor:yangian-hlevel-comparison-criterion", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 4878, "title": "H-level comparison criterion for dg-shifted Yangians", "refs_in_block": ["prop:yangian-canonical-hlevel-target", "thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion"]}
metadata/claims.jsonl:1374:{"label": "cor:shifted-rtt-tower-convergence", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_foundations.tex", "line": 2971, "title": "Automatic tower convergence", "refs_in_block": ["thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion", "cor:yangian-bar-cobar"]}
metadata/claims.jsonl:1430:{"label": "thm:completion-necessity", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 311, "title": "When completion is necessary {\\cite{Positselski11,GLZ22}}", "refs_in_block": ["def:strong-completion-tower", "lem:degree-cutoff", "part:characteristic-datum", "part:standard-landscape", "thm:completed-bar-cobar-strong"], "cites_in_block": ["Positselski11", "GLZ22"]}
metadata/claims.jsonl:1438:{"label": "thm:completed-bar-cobar-strong", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 953, "title": "MC element lifts to the completed convolution algebra", "refs_in_block": ["def:strong-completion-tower", "thm:completed-twisting-representability", "lem:degree-cutoff", "prop:mc4-weight-cutoff", "prop:inverse-limit-differential-continuity", "prop:mc4-reduction-principle"]}
metadata/claims.jsonl:1452:{"label": "cor:completion-closure-equivalence", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 1849, "title": "Homotopy-categorical equivalence on the completion\nclosure", "refs_in_block": ["thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:1453:{"label": "thm:coefficient-stability-criterion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 1903, "title": "Coefficient-stability criterion", "refs_in_block": ["thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:2106:{"label": "prop:w-algebra-koszul", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/existence_criteria.tex", "line": 553, "title": "\\texorpdfstring{$\\mathcal{W}$}{W}-algebra Koszul analysis", "refs_in_block": ["thm:completed-bar-cobar-strong", "thm:stabilized-completion-positive"], "cites_in_block": ["Arakawa15"]}
metadata/claims.jsonl:2412:{"label": "thm:ran-coherent-bar-cobar", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 14641, "title": "Ran-coherent bar-cobar equivalence", "refs_in_block": ["thm:completed-bar-cobar-strong", "lem:degree-cutoff"]}
metadata/claims.jsonl:2626:{"label": "prop:three-levels-mc-completion", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/koszul_pair_structure.tex", "line": 135, "title": "Three levels as MC at successive completions", "refs_in_block": ["thm:completed-bar-cobar-strong"]}
chapters/examples/landscape_census.tex:936:Theorem~\ref{thm:completed-bar-cobar-strong}.
chapters/examples/landscape_census.tex:1081:corresponding H-level infinite-generator dual object is the residual identification task (MC4 structural framework proved; Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/examples/landscape_census.tex:2033: calculations; MC4 structural framework proved (Theorem~\ref{thm:completed-bar-cobar-strong}); H-level identification residual.
chapters/examples/landscape_census.tex:3913:(Theorem~\ref{thm:completed-bar-cobar-strong}) resolves the formal
 succeeded in 51ms:
main.tex:1761: \phantomsection\label{conj:master-infinite-generator}%
metadata/claims.jsonl:1798:{"label": "rem:scope-curved-koszul", "env_type": "remark", "status": "Conjectured", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 6386, "title": "Scope", "refs_in_block": ["conj:derived-bc-betagamma", "sec:counter-examples", "conv:hms-levels", "conj:master-infinite-generator"], "cites_in_block": ["Zwi93"]}
chapters/theory/higher_genus_modular_koszul.tex:912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
chapters/theory/coderived_models.tex:424:Conjecture~\textup{\ref{conj:master-infinite-generator}} \textup{(MC4: proved; residual H-level comparison).}
chapters/theory/chiral_modules.tex:2002:(Conjecture~\ref{conj:master-infinite-generator};
chapters/theory/chiral_koszul_pairs.tex:6463:Conjecture~\ref{conj:master-infinite-generator}, not to the standard

thinking
**Searching for MC1-MC5 details**

I think I should search the introduction table for MC1 to MC5. Since it's about mission files, but I need the complete DAG for them. The introduction might provide a good summary. I’ll focus on lines around 2060 for any relevant information. It sounds like this could help clarify things and make my task easier! Let’s see what I find in the search!
exec
/bin/zsh -lc "sed -n '180,260p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '300,360p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2040,2085p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 on~$\mathcal{O}_{\mathrm{poly}}$ does not extend by density.
\item The resolution obstruction $\delta(k) = p(k) - 1$ is
 superpolynomial, forcing localizing generation in place of thick
 generation.
\item The braided monoidal structure requires the derived
 Drinfeld--Kohno theorem, additional data beyond the bare categorical
 equivalence.
\end{enumerate}
The conformal weight filtration offers a path: it decomposes the problem
into countably many finite-dimensional strata, each resolved by the
sectorwise spectral-sequence convergence of
Theorem~\ref{thm:sectorwise-spectral-convergence}, with Efimov-type
categorical formal completion assembling the answer via the
pro-Weyl--Mittag-Leffler tower.
\end{remark}

\begin{conjecture}[H-level target identification for standard infinite towers]
\label{conj:v1-master-infinite-generator}
\ClaimStatusConjectured{}
The structural completion framework is \textbf{proved}
 succeeded in 52ms:
HS-sewing package
\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
$+$ subexponential sector growth implies HS-sewing convergence;
Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
identification is still conjectural; at genus~$0$ the algebraic
BRST/bar comparison is proved
\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
while the tree-level amplitude pairing requires the additional
hypothesis isolated in
Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
orthogonal weak flank, not a link in this dependency chain.

\begin{theorem}[Higher-genus PBW concentration for the standard
 finite-type interacting families]\label{thm:master-pbw}
\ClaimStatusProvedHere{}
The genus-$g$ PBW spectral sequence concentrates at all genera for the
three standard finite-type interacting families treated in the proved
core: affine Kac--Moody
\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
 succeeded in 51ms:
The twelve characterisations K1--K12 of Koszulness (Theorem~\ref{thm:koszul-equivalences-meta}) comprise ten unconditional equivalences, one conditional (the Lagrangian criterion, conditional on perfectness; unconditional for the standard landscape), and one one-directional ($\mathcal{D}$-module purity, with only the forward direction proved). The bifunctor decomposition theorem is a further proved consequence outside the twelve numbered items.

Condition~(vii) of Theorem~\ref{thm:koszul-equivalences-meta} (factorization homology concentrated in degree~$0$) is scoped to genus~$0$ unconditionally and to $g \geq 1$ on the uniform-weight lane; the class-M Virasoro counterexample is documented in Remark~\ref{rem:fh-vii-uniform-weight-scope}. Chiral Koszulness is closed under tensor products, dualization, and base change (Proposition~\ref{prop:koszul-closure-properties}); quotients such as Drinfeld--Sokolov reduction fall outside this closure (Remark~\ref{rem:koszul-closure-not-quotients}).

The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).

\subsection{Entanglement entropy from the shadow obstruction tower}

At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).

Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.

Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.

\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

exec
/bin/zsh -lc "sed -n '520,690p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
problem (compact/completed extension beyond evaluation modules,
Conjecture~\ref{conj:dk-compacts-completion}) is downstream of MC3.
MC4 on the $\mathcal{W}_\infty$ tower is
\textbf{unconditionally closed} at all stages via
$\mathcal{W}_N$ rigidity
(Theorem~\ref{thm:winfty-all-stages-rigidity-closure})
within the strong completion-tower framework
(Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
Yangian tower is closed on the evaluation-generated core ($249$~tests);
the DK-$5$ categorical packet in type~$A$ is now accessible
(downstream of the MC3 package proved on the evaluation-generated core).
On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
the genus-$1$ bar-side curvature package is proved
\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
and~\ref{thm:genus1-d-squared}\textup{)}; and for
genus $g \ge 2$, inductive genus determination
(Theorem~\ref{thm:inductive-genus-determination}),
two-dimensional convergence
(Proposition~\ref{prop:2d-convergence}),
codex
I now have the canonical master labels for MC1, MC2, MC4, and MC5. I’m filling the missing MC3 node from the repo’s own status surface, then I’ll compare that canon against how this chapter claims to use those packages.
exec
/bin/zsh -lc 'rg -n -F "cor:mc3-all-types" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/theorem_registry.md:2011:| `cor:mc3-all-types` | `corollary` | 4224 | Three-layer MC3 status after categorical CG closure |
metadata/dependency_graph.dot:1259:  cor_mc3_all_types [label="cor:mc3-all-types\ncorollary [Pr]\nThree-layer MC3 status after categorical...", style=filled, fillcolor="#c8e6c9"];
chapters/connections/thqg_introduction_supplement_body.tex:1742:Corollary~\ref{cor:mc3-all-types}); the residual DK-4/5 problem
chapters/examples/lattice_foundations.tex:3972:Corollary~\ref{cor:mc3-all-types}\textup{)}; post-CG completion open
chapters/examples/lattice_foundations.tex:4008:\textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}. The exact remaining input
chapters/examples/lattice_foundations.tex:4642:Corollary~\ref{cor:mc3-all-types}; the remaining obstacles
chapters/examples/yangians_computations.tex:3281:\textup{(}Corollary~\textup{\ref{cor:mc3-all-types}}\textup{)}
chapters/examples/yangians_computations.tex:4224:\label{cor:mc3-all-types}%
chapters/examples/w3_holographic_datum.tex:122:Corollary~\ref{cor:mc3-all-types}). Thick generation by
chapters/examples/w3_holographic_datum.tex:124:(Corollary~\ref{cor:mc3-all-types}); the residual problem of
chapters/connections/concordance.tex:4450:Corollary~\ref{cor:mc3-all-types} still records the two unconditional
chapters/connections/concordance.tex:11305:(Corollary~\ref{cor:mc3-all-types} and
chapters/connections/outlook.tex:268:Corollary~\ref{cor:mc3-all-types}). The remaining open frontiers:
chapters/examples/free_fields.tex:3842:Corollary~\ref{cor:mc3-all-types}; the residual DK-4/5
chapters/examples/yangians_drinfeld_kohno.tex:4749:already proved \textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)};
chapters/examples/yangians_drinfeld_kohno.tex:6131:\textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}; the residual
chapters/examples/yangians_foundations.tex:119:\textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}: categorical
chapters/examples/yangians_foundations.tex:840: \textup{(}Corollary~\ref{cor:mc3-all-types}\textup{)}; the
chapters/examples/yangians_foundations.tex:1127: \textup{(}Corollary~\textup{\ref{cor:mc3-all-types}}\textup{)}.
chapters/examples/yangians_foundations.tex:2584:Corollary~\ref{cor:mc3-all-types}\textup{)},
exec
/bin/zsh -lc "sed -n '430,560p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC3" chapters/connections/editorial_constitution.tex chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:categorical-cg-all-types" chapters metadata main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Yangian reduction chain is detailed in \S\ref{sec:infty-cat-factorization-kd}.
\end{remark}

\begin{conjecture}[BV/BRST/bar identification]
\label{conj:v1-master-bv-brst}
\ClaimStatusConjectured{}
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.

\emph{Resolved in $D^{\mathrm{co}}$}
\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
the BV and bar complexes are quasi-isomorphic in the coderived category
for all chirally Koszul algebras, including class~M.
The chain-level identification holds for classes~G and~L, is
conditional for class~C on harmonic decoupling, and
\emph{fails} for class~M
\textup{(}quartic harmonic obstruction\textup{)}.

\emph{This is the mathematical-physics bridge. It is
 succeeded in 52ms:
chapters/examples/lattice_foundations.tex:3971:\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
chapters/examples/w3_holographic_datum.tex:121:(Theorem~\ref{thm:categorical-cg-all-types},
metadata/claims.jsonl:1204:{"label": "conj:rank-independence-step2", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_computations.tex", "line": 3242, "title": "Lift-and-lower \\textup{(}Lemma~L\\textup{)}", "refs_in_block": ["thm:categorical-cg-all-types", "thm:shifted-prefundamental-generation", "prop:prefundamental-clebsch-gordan"], "cites_in_block": ["HJZ25"]}
metadata/claims.jsonl:1212:{"label": "thm:mc3-arbitrary-type", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 4077, "title": "Categorical prefundamental CG decomposition, all types", "labels_in_block": ["thm:mc3-arbitrary-type", "thm:categorical-cg-all-types", "eq:prefundamental-cg-general-type"]}
metadata/claims.jsonl:1213:{"label": "cor:mc3-all-types", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 4224, "title": "Three-layer MC3 status after categorical CG closure", "refs_in_block": ["thm:categorical-cg-all-types", "cor:dk23-all-types", "thm:shifted-prefundamental-generation", "conj:rank-independence-step2"]}
metadata/claims.jsonl:1310:{"label": "conj:dk5-restricted", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 6267, "title": "DK-5: modular Yangian-shadow equivalence", "refs_in_block": ["thm:categorical-cg-all-types", "def:modular-yangian-pro", "conj:modular-yang-baxter", "thm:mc2-bar-intrinsic", "thm:recursive-existence", "thm:r-matrix-koszul-dual-inverse"]}
metadata/claims.jsonl:1348:{"label": "thm:all-types-yangian-structure", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_foundations.tex", "line": 1046, "title": "All-types Yangian structure", "labels_in_block": ["thm:all-types-yangian-structure", "eq:r-matrix-all-types"], "refs_in_block": ["comp:sl2-collision-residue-kz", "thm:rtt-all-classical-types", "thm:categorical-cg-all-types", "conj:rank-independence-step2", "cor:mc3-all-types"], "cites_in_block": ["ChariMoura06", "HJ12"]}
metadata/label_index.json:40126:  "thm:categorical-cg-all-types": {
chapters/examples/yangians_computations.tex:2945:\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}.
chapters/examples/yangians_computations.tex:3249:\textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.
chapters/examples/yangians_computations.tex:3276:Theorem~\ref{thm:categorical-cg-all-types}; the missing step is
chapters/examples/yangians_computations.tex:3963: Theorem~\ref{thm:categorical-cg-all-types} supplies the
chapters/examples/yangians_computations.tex:4078:\label{thm:categorical-cg-all-types}%
chapters/examples/yangians_computations.tex:4194:Theorem~\ref{thm:categorical-cg-all-types} rests on three
chapters/examples/yangians_computations.tex:4232: \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.
chapters/examples/yangians_computations.tex:4253:Theorem~\ref{thm:categorical-cg-all-types} gives Layer~1 for all
chapters/examples/yangians_computations.tex:4516:After Theorem~\ref{thm:categorical-cg-all-types} and
chapters/examples/yangians_computations.tex:4530:(Theorem~\ref{thm:categorical-cg-all-types}), using
chapters/examples/yangians_computations.tex:4540:\emph{unnecessary}: Theorem~\ref{thm:categorical-cg-all-types}
chapters/examples/yangians_computations.tex:4548:(Theorem~\ref{thm:categorical-cg-all-types}) resolves the CG
 succeeded in 52ms:
chapters/theory/introduction.tex:1396:(Conjecture~\ref{conj:dk5-restricted}). The proved content (MC3 on the
chapters/theory/introduction.tex:2019: quotient whose dual is an orthogonal coideal. For the Yangian MC3
chapters/theory/introduction.tex:2060:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
chapters/theory/introduction.tex:2068:MC3 & Thick generation & \textbf{proved} & CG all types + eval-core DK (Cor.~\ref{cor:mc3-all-types}); DK-4/5 downstream \\[2pt]
chapters/theory/introduction.tex:2091:\noindent\textbf{MC3} (Thick generation): Proved for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights~\cite{ChariMoura06} (Theorem~\ref{thm:categorical-cg-all-types}), with DK comparison proved separately (Corollary~\ref{cor:dk23-all-types}, Corollary~\ref{cor:mc3-all-types}). For type~$A$, shifted-prefundamental generation and pro-Weyl recovery are also proved (Theorem~\ref{thm:mc3-type-a-resolution}). DK-4/5 (extension beyond evaluation modules) is downstream.
chapters/theory/introduction.tex:2093: The proof decomposes into three layers: MC3a (evaluation core, all types, unconditional), MC3b (categorical thick generation, all types, unconditional), and MC3c (full category~$\mathcal{O}$, type~$A$ unconditional; other types conditional on Conjecture~\ref{conj:rank-independence-step2}, the rank-independence lift-and-lower conjecture for shifted prefundamental representations; see Remark~\ref{rem:lemma-L-status} for the dependency chain).
chapters/connections/editorial_constitution.tex:145:MC3 & $\Eone$-modular extension
chapters/connections/editorial_constitution.tex:159:MC3: \textbf{proved for all simple types} on the evaluation-generated
chapters/connections/editorial_constitution.tex:170:downstream of MC3.
chapters/connections/editorial_constitution.tex:502:&\Longrightarrow \text{MC3 enlargement}\\
chapters/connections/editorial_constitution.tex:513:MC3 is \textbf{proved for all simple types} on the evaluation-generated
chapters/connections/editorial_constitution.tex:521:Conjecture~\ref{conj:dk-compacts-completion}) is downstream of MC3.
chapters/connections/editorial_constitution.tex:530:(downstream of the MC3 package proved on the evaluation-generated core).
chapters/connections/editorial_constitution.tex:544:\emph{Critical point}: MC3 package~(i) (categorical CG) is now
chapters/connections/editorial_constitution.tex:547:input for the full four-package MC3 beyond type~$A$ is thick
chapters/connections/editorial_constitution.tex:568:remaining MC3--MC5 dependency chain.
chapters/connections/editorial_constitution.tex:571:\begin{conjecture}[Standard-tower MC5 reduction after MC3 and realized
chapters/connections/editorial_constitution.tex:610:MC3/MC4 inputs on the standard principal and RTT towers. The
chapters/connections/editorial_constitution.tex:613:\text{MC3 enlargement}
chapters/connections/editorial_constitution.tex:647:Thus, after the MC3 enlargement of assumption~\textup{(i)}, no new




thinking
**Analyzing MC5 physics**

I see that the editorial constitution mentions that MC5 physics completion is still conjecture, while the introduction states that the analytic part is proven. It's crucial to compare how this chapter treats MC5 to identify any conflation between the analytic part and the full MC5. I should inspect table or lines around specific numbers to see how these sections are packaged. I'll need to ensure every claim is grounded in the actual file content while possibly utilizing the metadata dependency graph.
thinking
**Tracing dependency DAG**

The user specifically asked to trace the dependency DAG in this file. I can root the DAG in file references to certain labels rather than relying only on the master theorem texts. To construct a complete DAG, I probably need to read the relevant theorem blocks that utilize external master labels. I’ll focus on the dependencies of MC2's local theorem and its imported results, ensuring to include a listing of the entire DAG for MC1-MC5 as indicated by chapter cross-references. I'll be thorough about any missing definitions or unresolved references!
thinking
**Auditing target file**

I need to audit the target file's handling of the MCs, which likely involves listing the DAG with dependencies and findings. It might be useful to create a reference graph for the relevant theorems and sections. Since the file is quite large, I could use `metadata/claims.jsonl` to help identify entries related to refs_in_block. However, the user emphasized reading the actual file contents. I'll focus on quoting the theorem statements and proofs, ensuring that I identify specific issues along the way. Let's outline any potential findings!
thinking
**Considering coding methods**

I think the easiest approach might be to use a Python one-liner to parse references and labels since it avoids any file editing, which shouldn't be forbidden. It's noted that using Python for file reading or writing is off-limits in this case, where shell or applying patches would be more suitable. For analysis, maybe the shell is indeed better. I could also consider using tools like `rg` and `sort` to assist with that.
codex
I’ve found a likely drift point: some active prose still describes MC2 via an older assembly route rather than the bar-intrinsic proof that the chapter now claims as primary. I’m checking the live reference surface next so I can separate actual proof defects from mere narrative drift.
exec
/bin/zsh -lc 'labels=$(mktemp); refs=$(mktemp); rg -o -N '"'\\\\label\\{["'^}]+'"' chapters | sed 's/"'^'"\\\\label{//' | sort -u > \""'$labels"; rg -o -N '"'\\\\(?:eq|ref|autoref|cref|Cref)\\{["'^}]+'"' chapters/theory/higher_genus_modular_koszul.tex | sed -E 's/"'^'"\\\\(eq|ref|autoref|cref|Cref)\\{//' | sort -u > \""'$refs"; comm -23 "$refs" "$labels" | sed -n '"'1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\\\ClaimStatus' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
D:genus-tower
MK:koszul
MK:koszul-htpy
MK:modular
MK:modular-htpy
MK:verdier
MK:verdier-htpy
app:nonlinear-modular-shadows
ch:heisenberg-frame
ch:landscape-census
chap:arithmetic-shadows
chap:bar-cobar
chap:bar-cobar-adjunction
chap:beta-gamma
chap:concordance
chap:e1-modular-koszul
chap:free-fields
comp:bp-shadow-tower
comp:ff-thooft-involution
comp:genus2-multichannel-catalogue
 succeeded in 51ms:

exec
/bin/zsh -lc "sed -n '10220,10380p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'undefined' chapters/theory/higher_genus_modular_koszul.tex chapters/connections/editorial_constitution.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Theta_\cA$ is upstream (how the genus tower is assembled);
$\mathcal{V}_\cA=[R\pi_{g*}\barB^{(g)}(\cA)]\in K_0(\overline{\mathcal{M}}_g)$
is downstream (what virtual object remains after pushforward).
When $\dim H^2_{\mathrm{cyc}}=1$, $\mathcal{V}_\cA$ is rank one
and $\Theta_\cA^{\min}=\eta\otimes\Gamma_\cA$; on the proved
uniform-weight lane this specializes to
$\Theta_\cA^{\min}=\kappa\cdot\eta\otimes\Lambda$;
beyond scalar, Construction~\ref{constr:non-scalar-hpt} provides
the higher-rank upstream data.
\end{remark}

\begin{theorem}[Tautological line support from genus universality;
\ClaimStatusProvedHere]\label{thm:tautological-line-support}
\index{MC2!tautological line support}
Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
$L_\infty$-algebra on bar coderivations, with the MC equation in
$\Defcyc(\cA)\widehat{\otimes}\Gmod$ modelling the nilpotence
condition $d_{\mathrm{bar}}^2 = 0$ of the genus-expanded bar
differential.
 succeeded in 50ms:
chapters/theory/introduction.tex:1107:\emph{At $k = -h^\vee$} the Sugawara construction is undefined: the
chapters/theory/introduction.tex:1745:level $k = -h^\vee$ the Sugawara element is undefined and
chapters/theory/introduction.tex:2704:The Sugawara construction is \emph{undefined} at critical level $k = -h^\vee$; the Sugawara vector does not lie in the appropriate completion. This is not ``$c$ diverges''; the construction does not exist.
chapters/theory/higher_genus_modular_koszul.tex:16927:the shadow depth is undefined


thinking
**Evaluating reference outputs**

I'm looking into why the missing references script returned so many outputs. It seems like it’s listing labels not found within the chapters, but this might include existing labels from other files too. I noticed it includes labels that actually do exist, like `chap:concordance`, which is puzzling. I should probably run a more comprehensive search across the entire repository to get an accurate read on all labels, including those in appendices. This current list doesn't seem reliable, so I need to be careful moving forward.
thinking
**Analyzing candidate findings**

I'm reviewing the candidate findings and looking at the `rem:theta-modular-twisting` with curved and flat conflation. It seems like the proof for `thm:universal-theta` references `thm:master-theta`, even though the latter only shows that `\Theta^{\le 2}` holds. There's also an editorial theorem indicating that the universal MC element `\Theta_\cA^{\le 2} \in MC(...)` relates to the genus-1 trace and its higher-degree tower. I wonder if the statements are overemphasizing their equivalence, especially since `thm:master-theta` in main.tex may have a more limited scope.
codex
I’ve reached the key reduction theorem that turns MC2-3 into “genus universality = tautological support.” That proof is where hidden identifications are most likely, so I’m reading the geometric-completion proposition it imports before deciding whether the reduction actually closes.
exec
/bin/zsh -lc 'rg -n -F "label{prop:geometric-modular-operadic-mc}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5839:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
exec
/bin/zsh -lc "sed -n '5840,6038p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3855,3925p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8300,8465p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{MC2!geometric modular-operadic framework}
\index{modular graph coefficient algebra!geometric realization}
Let\/ $(L, \{l_n\}_{n \geq 1},$\allowbreak
$\langle{-},{-}\rangle)$ be a complete
cyclic $L_\infty$-algebra as in
Proposition~\textup{\ref{prop:genus-completed-mc-framework}}.
Then:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Genus filtration on $\Gmod$.}
 The modular graph coefficient algebra $\Gmod$
 \textup{(}Definition~\textup{\ref{def:modular-graph-algebra}}\textup{)}
 carries a complete descending genus filtration
 $G^m{\Gmod} := \prod_{g \geq m} {\Gmod}^{(g)}$
 with each genus-$g$ component ${\Gmod}^{(g)}$ finite-dimensional.
 The dg~Lie structure on $\Gmod$ respects the filtration:
 $[G^{m_1}, G^{m_2}] \subseteq G^{m_1+m_2}$ and
 $d(G^m) \subseteq G^m$.

\item \emph{Convergent completed tensor product.}
 The pro-nilpotent completed tensor product
 succeeded in 51ms:
  3855	all-genera scalar-trace proof
  3856	(Corollary~\ref{cor:scalar-saturation}).
  3857	\end{proof}
  3858	
  3859	\begin{remark}[The universal class as modular twisting cochain]
  3860	\label{rem:theta-modular-twisting}
  3861	\index{twisting morphism!modular|textbf}
  3862	\index{modular twisting cochain|textbf}
  3863	Theorem~\ref{thm:universal-theta} extends the canonical twisting
  3864	morphism $\pi \colon \barB_X(\cA) \to \cA$ of genus-$0$ bar-cobar
  3865	duality (Proposition~\ref{prop:universal-twisting-adjunction}) to
  3866	higher genus by a single algebraic step:
  3867	\emph{promoting the twisting morphism from flat to curved, and from
  3868	the convolution algebra $\mathrm{Hom}(\barB, \cA)$ to the modular
  3869	convolution algebra
  3870	$\operatorname{Def}^{\mathrm{mod}}(\cA) =
  3871	\prod_{g,n} \mathrm{Hom}_{\Sigma_n}(C_*(\overline{\mathcal{M}}_{g,n}),
  3872	\operatorname{End}_\cA(g,n))$
  3873	\textup{(}Definition~\textup{\ref{def:modular-deformation-complex})}.}
  3874	
 succeeded in 50ms:
\item that scalar is recovered by a single normalized evaluation:
 \[
 c_g(\cA) \;=\; \ell_g\bigl(o_g(\cA)\bigr);
 \]
\item consequently, the identification
 $o_g(\cA)=\kappa(\cA)\tau_g$ is equivalent to the conjunction of:
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item the line-support statement $o_g(\cA)\in T_g$;
 \item the single scalar equality
 $\ell_g(o_g(\cA))=\kappa(\cA)$.
 \end{enumerate}
\end{enumerate}
In particular, if $T_g=\mathbb{C}\lambda_g \subset W_g$, then the
one-channel normalization package reduces to placing the obstruction in
the tautological line $\mathbb{C}\lambda_g$ and matching one normalized
scalar evaluation with the already-proved shadow coefficient
$\kappa(\cA)$.
\end{proposition}

\begin{proof}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3980,4228p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5280,5310p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3768,3857p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10226,10326p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3980	obstructions in the Postnikov tower of
  3981	Definition~\ref{def:shadow-postnikov-tower}.
  3982	There is no separate construction for each invariant; there is
  3983	$\Theta_\cA$, and the invariants are what remain after
  3984	forgetting all but finitely many degrees.
  3985	
  3986	\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
  3987	\label{thm:mc2-bar-intrinsic}
  3988	\index{universal Maurer--Cartan class!bar-intrinsic construction}
  3989	\index{MC2!bar-intrinsic proof}
  3990	\index{MC2!full generality}
  3991	Let $\cA$ be a modular Koszul chiral algebra on a smooth
  3992	projective curve~$X$ with non-degenerate invariant form.
  3993	Write
  3994	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
  3995	for the genus-completed bar differential
  3996	\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
  3997	with $d_\cA^{(0)} = \dzero$ the genus-$0$ bar differential.
  3998	Define the \emph{positive-genus correction}
  3999	\begin{equation}\label{eq:theta-bar-intrinsic}
 succeeded in 51ms:
  3768	\begin{proof}
  3769	This is Theorem~\ref{thm:ds-bar-gf-discriminant}.
  3770	\end{proof}
  3771	
  3772	\begin{remark}[\texorpdfstring{$K$}{K}-theoretic hierarchy]\label{rem:spectral-characteristic-programme}
  3773	\index{spectral discriminant!K-theoretic hierarchy}
  3774	Setting $\mathcal{V}=[R\pi_{g*}\bar{B}^{(g)}(\cA)]\in
  3775	K_0(\overline{\mathcal{M}}_g)$: $c_1(\det\mathcal{V})$
  3776	recovers~$\kappa$, $\operatorname{ch}(\mathcal{V})$
  3777	recovers~$\Delta_{\cA}$, and the holonomy recovers~$\Pi_{\cA}$.
  3778	See Remark~\ref{rem:structural-saturation}.
  3779	\end{remark}
  3780	
  3781	\begin{remark}[Shared discriminant, distinct sewing]\label{rem:shared-discriminant-sheet}
  3782	The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
  3783	\end{remark}
  3784	
  3785	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3786	\label{thm:universal-theta}
  3787	\index{universal Maurer--Cartan class|textbf}
 succeeded in 51ms:
  5280	\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
  5281	\index{universal Maurer--Cartan class!proof history}
  5282	The proof of Theorem~\ref{thm:universal-theta} assembles:
  5283	(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
  5284	(ii)~the determinant line bundle with $c_1=\kappa\cdot\lambda$
  5285	(Remark~\ref{rem:homotopy-native-d});
  5286	(iii)~the spectral discriminant $\Delta_{\cA}(x)$
  5287	(Theorem~\ref{thm:spectral-characteristic});
  5288	(iv)~the cyclic deformation algebra on bar coderivations
  5289	(Proposition~\ref{prop:genus0-cyclic-coderivation}), with
  5290	MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.
  5291	Computationally verified for $\mathfrak{sl}_2$, $\mathfrak{sl}_3$,
  5292	$\mathfrak{sp}_4$, $\mathfrak{g}_2$ via
  5293	\texttt{compute/lib/mc2\_cyclic\_linf.py}.
  5294	\end{remark}
  5295	
  5296	% ================================================================
  5297	% COMMENTED OUT: Detailed computational session notes (items v-ix)
  5298	% that formerly occupied ~270 lines. The mathematical content is
  5299	% captured in the four items above; the computational verification
 succeeded in 52ms:
 10226	$\Theta_\cA^{\min}=\kappa\cdot\eta\otimes\Lambda$;
 10227	beyond scalar, Construction~\ref{constr:non-scalar-hpt} provides
 10228	the higher-rank upstream data.
 10229	\end{remark}
 10230	
 10231	\begin{theorem}[Tautological line support from genus universality;
 10232	\ClaimStatusProvedHere]\label{thm:tautological-line-support}
 10233	\index{MC2!tautological line support}
 10234	Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
 10235	cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
 10236	$L_\infty$-algebra on bar coderivations, with the MC equation in
 10237	$\Defcyc(\cA)\widehat{\otimes}\Gmod$ modelling the nilpotence
 10238	condition $d_{\mathrm{bar}}^2 = 0$ of the genus-expanded bar
 10239	differential.
 10240	Then the genus-$1$ instance of
 10241	Hypothesis~\textup{\ref{mc2-hyp:tautological}} \textup{(MC2-3)}
 10242	holds:
 10243	\[
 10244	 o_1(\cA) \;=\; \kappa(\cA)\,\lambda_1
 10245	 \quad\text{in } W_1 .
codex
The main technical defect is sharpening: the chapter keeps sliding between the total nilpotent bar differential and the curved fiberwise differential. I’m pinning the exact reduction statement now, because if that reduction is overstated it contaminates every downstream “MC2-3 is settled” sentence.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5798,5865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5866,5925p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5866	 \end{equation}
  5867	 is a complete $L_\infty$-algebra: the tensor product of the
  5868	 $L_\infty$ structure on~$L$ with the dg~Lie structure on~$\Gmod$
  5869	 yields $L_\infty$ brackets $\{\hat{l}_n^{\Gmod}\}$
  5870	 on $\widehat{L}_{\Gmod}$ that respect the genus filtration.
  5871	 The Maurer--Cartan equation in $\widehat{L}_{\Gmod}$ is
  5872	 convergent at each genus, with the same finiteness bound as
  5873	 Proposition~\textup{\ref{prop:genus-completed-mc-framework}(b)}.
  5874	
  5875	\item \emph{Clutching from Feynman structure.}
  5876	 The dg~Lie structure on $\Gmod$ encodes the boundary
  5877	 stratification of $\overline{\mathcal{M}}_{g,n}$:
  5878	 \begin{itemize}
  5879	 \item separating degenerations correspond to the
  5880	 edge-gluing Lie bracket $[-,-]_{\Gmod}$;
  5881	 \item non-separating degenerations correspond to the
  5882	 self-gluing component of the differential $d_{\Gmod}$.
  5883	 \end{itemize}
  5884	 An MC element
  5885	 $\Theta \in \mathrm{MC}(\widehat{L}_{\Gmod})$
 succeeded in 52ms:
  5798	genus~$g$ is a single element of~$W_g$.
  5799	For simple~$\mathfrak{g}$,
  5800	Proposition~\ref{prop:cyclic-ce-identification} gives
  5801	$H^2_{\mathrm{cyc}}(\mathfrak{g}, \mathfrak{g}) \cong
  5802	H^3(\mathfrak{g}) \cong \mathbb{C}$ with generator the
  5803	Killing $3$-cocycle.
  5804	\end{proof}
  5805	
  5806	\begin{proposition}[MC2 reduction principle;
  5807	\ClaimStatusProvedHere]\label{prop:mc2-reduction-principle}
  5808	\index{MC2!reduction principle}
  5809	Let $\cA$ be a modular Koszul chiral algebra. Assume that the
  5810	bar-intrinsic complex $\Defcyc(\cA)$ of
  5811	Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
  5812	$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
  5813	coefficient spaces chosen from
  5814	$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
  5815	modular-operadic package of
  5816	Theorem~\ref{thm:universal-theta}. Then:
  5817	\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '188,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8338,8458p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
 succeeded in 51ms:
  8338	$o_g(\cA)=\kappa(\cA)\tau_g$ is exactly the same as requiring
  8339	$\ell_g(o_g(\cA))=\kappa(\cA)$.
  8340	\end{proof}
  8341	
  8342	\begin{remark}[Reduction consequence for MC2]
  8343	\label{rem:mc2-reduction-consequence}
  8344	Proposition~\ref{prop:mc2-reduction-principle} turns MC2 into a
  8345	three-package extension problem:
  8346	(1)~construct the cyclic $L_\infty$ model $\Defcyc(\cA)$;
  8347	(2)~realize the modular-operadic clutching package over
  8348	$\overline{\mathcal{M}}_{g,\bullet}$;
  8349	(3)~identify the one-channel genus-$g$ obstruction with the
  8350	tautological line via clutching/trace isolation, then reduce
  8351	through the Verdier/Koszul Lagrangian plane, PTVV lift,
  8352	chain-model seeds, root-string transfer, and a single scalar
  8353	comparison
  8354	(Propositions~\ref{prop:tautological-line-support-criterion}
  8355	through~\ref{prop:one-channel-normalization-criterion}).
  8356	Once packages~(1)--(2) exist, package~(3) is a finite
  8357	reduction to one normalized scalar check. What remains open beyond
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '478,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2058,2098p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:three-tier-architecture}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2338,2585p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   478	Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
   479	with Theorems~\ref{thm:pbw-allgenera-km},
   480	\ref{thm:pbw-allgenera-virasoro},
   481	and~\ref{thm:pbw-allgenera-principal-w},
   482	it resolves MC1 for the standard finite-type interacting families.
   483	Theorem~\ref{thm:pbw-universal-semisimple} packages the common
   484	unique-weight-$2$ $d_2$ mechanism used in the Virasoro and principal
   485	finite-type $\mathcal{W}$ proofs; under hypotheses~(a)--(b) alone, it
   486	should be read as a criterion requiring separate later-page and
   487	extension control. Under the additional semisimple symmetry
   488	hypothesis~(c), the enrichment-killing is unconditional.
   489	Theorem~\ref{thm:master-theta} (originally conjectured, now resolved
   490	by Theorem~\ref{thm:mc2-bar-intrinsic}) constructs the H-level
   491	completion of the modular characteristic hierarchy.
   492	Conjectures~\ref{conj:master-dk-kl}
   493	and~\ref{conj:v1-master-infinite-generator} are
   494	\emph{staged structural extensions}: the DK/KL enlargement beyond the
   495	theorematic evaluation-generated core and the filtered H-level
   496	comparison problem for the
   497	standard infinite towers.
 succeeded in 51ms:
  2058	\index{master conjectures}
  2059	
  2060	The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
  2061	
  2062	\begin{center}
  2063	\small
  2064	\begin{tabular}{llll}
  2065	\textbf{MC} & \textbf{Statement} & \textbf{Status} & \textbf{Key input} \\ \hline
  2066	MC1 & PBW concentration & \textbf{proved} & all standard families \\[2pt]
  2067	MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & coinvariant bar-intrinsic MC2 (Thm~\ref{thm:mc2-bar-intrinsic}); ordered lift (Thm~\ref{thm:e1-mc-element}) \\[2pt]
  2068	MC3 & Thick generation & \textbf{proved} & CG all types + eval-core DK (Cor.~\ref{cor:mc3-all-types}); DK-4/5 downstream \\[2pt]
  2069	MC4 & $\mathcal{W}_\infty$ closure & \textbf{proved} & strong completion towers on weight-completed standard families + weight cutoff \\[2pt]
  2070	MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}
  2071	\end{tabular}
  2072	\end{center}
  2073	
  2074	\noindent\textbf{MC1} (PBW concentration): Bar cohomology of every standard-landscape chiral algebra concentrates in PBW degrees, proved for all standard families by explicit computation.
  2075	
  2076	\noindent\textbf{MC2} (Universal MC class): the symmetric, coinvariant statement is
  2077	$\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$, proved by
 succeeded in 51ms:
2338: \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
 succeeded in 52ms:
  2338	 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
  2339	\index{three-tier architecture|textbf}
  2340	\index{modular Koszul duality!logical architecture|textbf}
  2341	The modular Koszul engine decomposes into three tiers
  2342	of decreasing generality and increasing analytic
  2343	content. At each tier, the listed results follow
  2344	from the stated input alone.
  2345	
  2346	\smallskip\noindent
  2347	\textbf{Tier~0} \textup{(topological input:
  2348	$D_\cA^2 = 0$)}.
  2349	\begin{enumerate}[label=\textup{(0.\arabic*)}]
  2350	\item The universal MC element
  2351	 $\Theta_\cA := D_\cA - \dzero
  2352	 \in \MC(\gAmod)$ exists at all genera
  2353	 \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
  2354	\item The shadow obstruction tower
  2355	 $\Theta_\cA^{\leq r}$ exists at all finite degrees,
  2356	 with $\Theta_\cA = \varprojlim_r
  2357	 \Theta_\cA^{\leq r}$


thinking
**Evaluating theorem D in architecture**

I find it interesting that the three-tier architecture has a claim about Tier 0 and theorem D that seems incompatible with the concordance statement. Concordance notes that the modular characteristic theorem applies to a specific configuration. Since tier 0 item 4 states theorem D holds unconditionally, it's probably overstated, especially considering its implications for genus universality. So, I think I need to adjust the documentation to clarify the conditions under which different types of families hold true. This seems like an important realization!
thinking
**Examining proof lines and hypotheses**

I feel like I need to revisit proof lines 2445-2449 because they might imply that Tier 0 requires D^2 alone. However, Theorem D doesn't necessarily follow from that alone, so it's a significant concern. There are candidate findings at lines 2376-2379 discussing Axiom MK related to modular aspects during all genera. In later lines, it seems to indicate that Tier 1 needs MK:koszul, which could be critical, but I wonder if some families necessitate additional conditions. I should double-check these hypotheses to ensure clarity in the proof.
exec
/bin/zsh -lc 'rg -n -F "obs_g and o_g are two names" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"o_g\\(|\\\\mathrm\\{obs\\}_g|obstruction class.*obs\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorem D\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '44,78p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
2955:\index{Lagrangian self-intersection!Theorem D}
3172:\index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
3173:\index{Hodge bundle!alternative proof of Theorem D}
3232:\index{Frenkel--Gaitsgory!comparison with Theorem D}
 succeeded in 51ms:
rg: regex parse error:
    (?:o_g\(|\mathrm\{obs\}_g|obstruction class.*obs)
             ^^
error: unrecognized escape sequence
 succeeded in 51ms:
    44	 the counit is an unconditional coderived coacyclic-equivalence,
    45	 promoted back to an ordinary quasi-isomorphism on collapse loci
    46	 & \ClaimStatusProvedHere \\
    47	\textbf{C} & Complementarity
    48	 & C0: coderived fiber-center identification unconditional,
    49	 ordinary-derived only on the flat perfect locus
    50	 \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
    51	 C1: homotopy eigenspace decomposition for all~$g$, with
    52	 duality/Lagrangian only for $g \geq 1$ and genus~$0$
    53	 treated separately
    54	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
    55	 C2: shifted-symplectic/BV upgrade conditional on the
    56	 uniform-weight perfectness package
    57	 \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
    58	 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
    59	\textbf{D} & Modular characteristic
    60	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    61	 on the proved uniform-weight lane at all genera
    62	 \textup{(}Definition~\ref{def:scalar-lane},
    63	 Thm~\ref{thm:modular-characteristic}\textup{)};
codex
The concordance confirms the status boundary I suspected: all-genera Theorem D is only on the proved uniform-weight lane, with genus 1 universal and multi-weight corrections at higher genus. I’m checking where this chapter silently erases that boundary.
exec
/bin/zsh -lc "rg -n -F 'o_g(' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathrm{obs}_g' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
6048:and write $o_g(\cA)\in W_g$ for the one-channel obstruction class.
6060:$o_g(\cA)$ and $\lambda_g$ such that the joint map
6070:\mathrm{clut}_g\bigl(o_g(\cA)\bigr)
6076:\ell_g\bigl(o_g(\cA)\bigr)
6082:o_g(\cA) \;=\; \kappa(\cA)\,\lambda_g.
6097:o_g(\cA)-\kappa(\cA)\lambda_g \in U_g.
6103:\mathrm{clut}_g\bigl(o_g(\cA)\bigr)
6112:\ell_g\bigl(o_g(\cA)\bigr)-\kappa(\cA)\ell_g(\lambda_g)
6117:$o_g(\cA)=\kappa(\cA)\lambda_g$.
8290:$o_g(\cA) \in W_g$.
8294:If $o_g(\cA)$ lies in $T_g$, then:
8298: o_g(\cA) \;=\; c_g(\cA)\,\tau_g;
8302: c_g(\cA) \;=\; \ell_g\bigl(o_g(\cA)\bigr);
8305: $o_g(\cA)=\kappa(\cA)\tau_g$ is equivalent to the conjunction of:
8307: \item the line-support statement $o_g(\cA)\in T_g$;
8309: $\ell_g(o_g(\cA))=\kappa(\cA)$.
8320:If $o_g(\cA)\in T_g=\mathbb{C}\tau_g$, then by definition of a
8323:$o_g(\cA)=c_g(\cA)\tau_g$; this is part~\textup{(i)}.
8326:\ell_g(o_g(\cA))
8337:$\ell_g(o_g(\cA))$, so requiring
 succeeded in 51ms:
488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) for
2728:On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
2867: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
2929:\mathrm{obs}_g=\kappa(\cA)\lambda_g
3003:\mathrm{obs}_g=\kappa\cdot\lambda_g
3015:load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
3017:$\mathrm{obs}_g=\kappa\cdot\lambda_g$ \textup{(}UNIFORM-WEIGHT;
3215:\mathrm{obs}_g(\cA)
3952:$\mathrm{obs}_g
10308:$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for all
10310:Since $\mathrm{obs}_g$ and $o_g$ are two names for the same
23020: $\mathrm{obs}_g$.
25952:2 & $\mathrm{obs}_g = \kappa \cdot \lambda_g$
35686:$\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ in the
exec
/bin/zsh -lc "rg -n -F 'Theorem~D' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2360,2372p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2360	 $\cA^{\mathrm{sh}} =
  2361	 H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
  2362	 a graded Lie bracket with
  2363	 projections $\kappa$, $\Delta$,
  2364	 $\mathfrak{C}$, $\mathfrak{Q}$
  2365	 \textup{(Corollary~\ref{cor:shadow-extraction})}.
  2366	\item Theorem~D \textup{(}modular characteristic
  2367	 $\kappa(\cA)$, $\hat{A}$-genus generating
  2368	 function\textup{)} holds unconditionally.
  2369	\end{enumerate}
  2370	No Koszulity hypothesis is required.
  2371	
  2372	\smallskip\noindent
 succeeded in 52ms:
2366:\item Theorem~D \textup{(}modular characteristic
2996:\begin{remark}[Proof routing for Theorem~D;
3095:Theorem~D as the scalar degree-$2$ projection of the ordered
3175:Theorem~D which does not use the shadow tower, the
3226:Theorem~D, using only the family of fiber bar complexes and Hodge
3235:Theorem~D matches the oper side of the local geometric Langlands
3239:$\kappa(\cA)$ is the scalar modular characteristic of Theorem~D.
3265: side remains external to Theorem~D.
3268: On the proved uniform-weight lane, Theorem~D gives
4581: \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
4635:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
5791:of Theorem~D$_{\mathrm{scal}}$
10138:Theorem~D establishes that $\kappa$ exists as a universal
10158:Properties~(i)--(iv) of Theorem~D arise from the bar-intrinsic scalar
10404:Theorem~D$_{\mathrm{scal}}$
10411:Theorem~D$_\Delta$
10452:Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
12578: \quad(the modular characteristic, Theorem~D);
12833: \quad(the modular characteristic, Theorem~D);
14620:Theorem~D



thinking
**Analyzing theorem references**

Great! I need to check the proof routing for Theorem D to see if any corrections are necessary. I notice potential circular references in lines 2366-2368 and in line 3812 with Theorem master-theta. I’m considering if `thm:three-tier-architecture` might also rely on Theorem D without conditions. It seems there’s a hidden import in `prop:geometric-modular-operadic-mc`, specifically regarding the Getzler-Kapranov correspondence. I’ll explore if the GK correspondence is applicable here, but it requires exact conditions. It’s tricky to audit without reviewing the citations thoroughly, especially since the user prefers no guesses.
thinking
**Identifying missing hypotheses**

I could mark the missing hypotheses in the proposition since it doesn't state the conditions required for the GK theorem, like finite-dimensionality and operad/cooperad compatibility. It seems the text cites the GK theorem but doesn't clarify those hypotheses. To highlight the missing link, I might say, "PROBLEM: Part (c) mentions the Getzler-Kapranov correspondence without specifying the needed hypotheses for \(L\widehat\otimes \Gmod\)." A solution could involve adding a sentence about compatibility or inserting a lemma. Since the user wants every hidden import noted, I’ll check for line numbers around 5957 or part (c) around 5960.
thinking
**Locating line numbers**

I want to locate exact line numbers, particularly around 597. It seems I need more detailed information for the section spanning from 5950 to 6000. Maybe I should gather more context to ensure I'm not missing anything important in this range. Gathering those specific lines will help clarify the information I'm looking for, so I'll make sure to take notes on anything significant in those areas as I go along. This will help in addressing any relevant issues in the text later.
codex
The strongest surviving issues are now structural, not computational: one explicit circle, one flat/curved conflation, and one status overclaim already confirmed against concordance. I’m checking whether the modular-operadic clutching proposition has any equally explicit hidden imports before I finalize the DAG and findings.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5960,6026p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2990,3025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'UNIFORM-WEIGHT' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3260,3275p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5960	Proposition~\ref{prop:genus-completed-mc-framework}, with the
  5961	additional dg~Lie structure on $\Gmod$ incorporated via the
  5962	Leibniz rule. The MC equation at genus~$g$ involves the same
  5963	partition count $\binom{g+n-1}{n-1}$ summands at degree~$n$,
  5964	hence converges (is a finite sum) at each genus.
  5965	
  5966	\emph{(c) Clutching from Feynman structure.}
  5967	The Feynman transform is built from the modular operad
  5968	$\mathcal{M}od = \{\overline{\mathcal{M}}_{g,n}\}$
  5969	(Theorem~\ref{thm:prism-higher-genus}(i)) by summing
  5970	over stable graphs. The dg~Lie structure on $\Gmod$
  5971	decomposes along the boundary stratification of the moduli spaces:
  5972	
  5973	\emph{Separating degenerations.}
  5974	A separating boundary stratum
  5975	$\delta_{g_1} \cong
  5976	\overline{\mathcal{M}}_{g_1,n_1+1} \times
  5977	\overline{\mathcal{M}}_{g_2,n_2+1}
  5978	\hookrightarrow \overline{\mathcal{M}}_{g,n}$
  5979	corresponds to a stable graph with a single separating edge.
 succeeded in 51ms:
  2990	the KZ/Hitchin package on that
  2991	integrable affine lane; the factorization structure recovers the modular
  2992	functor (Theorem~\ref{thm:chain-modular-functor},
  2993	Conjecture~\ref{conj:categorical-modular-kd}).
  2994	\end{remark}
  2995	
  2996	\begin{remark}[Proof routing for Theorem~D;
  2997	Convention~\ref{conv:proof-architecture}]
  2998	\label{rem:theorem-d-model}
  2999	\index{modular characteristic theorem!model presentation}
  3000	\[
  3001	\Theta_\cA \text{ and its shadow tower}
  3002	\Longrightarrow
  3003	\mathrm{obs}_g=\kappa\cdot\lambda_g
  3004	\Longrightarrow
  3005	\sum_{g \ge 1} F_g x^{2g}
  3006	=
  3007	\kappa\cdot(\hat{A}(ix)-1)
  3008	\]
  3009	The bar-intrinsic shadow tower is the common source.
 succeeded in 50ms:
488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) for
2729:\textup{(}UNIFORM-WEIGHT\textup{)}
2787: \textup{(}UNIFORM-WEIGHT\textup{}),
2868: \textup{(}UNIFORM-WEIGHT\textup{}) in $H^{2g}(\overline{\mathcal{M}}_g)$ for all $g \geq 1$
2869: \textup{(}UNIFORM-WEIGHT; unconditional at $g = 1$\textup{)}.
2885: \textup{(UNIFORM-WEIGHT)}.
3017:$\mathrm{obs}_g=\kappa\cdot\lambda_g$ \textup{(}UNIFORM-WEIGHT;
3221:\textup{(UNIFORM-WEIGHT)}.
3329:\textup{(}UNIFORM-WEIGHT\textup{)}.
3807: \textup{(}UNIFORM-WEIGHT\textup{)};
4029: \textup{(}UNIFORM-WEIGHT\textup{}).
4950: \textup{(}UNIFORM-WEIGHT\textup{}),
4984: \textup{(}UNIFORM-WEIGHT\textup{}),
6084:\textup{(}UNIFORM-WEIGHT\textup{}).
8407:$\sum_{g\ge1}\kappa(\cA)\lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) on the proved uniform-weight lane
9107: \textup{(}UNIFORM-WEIGHT\textup{})
10256:\textup{(}UNIFORM-WEIGHT\textup{}).
13098: \qquad \textup{(}UNIFORM-WEIGHT\textup{}),
13565: \textup{(}UNIFORM-WEIGHT\textup{})
13577:\textup{(}UNIFORM-WEIGHT\textup{)}
 succeeded in 51ms:
  3260	 of \cite[Theorem~1]{FG06}, recorded internally as
  3261	 Theorem~\ref{thm:fg-localization}. The match is therefore at the
  3262	 level of the critical oper package and its bar model. It is not an
  3263	 identification of bar-cobar Koszul duality with the full categorical
  3264	 local geometric Langlands equivalence: the Whittaker or automorphic
  3265	 side remains external to Theorem~D.
  3266	
  3267	\item \emph{The Feigin--Frenkel center.}
  3268	 On the proved uniform-weight lane, Theorem~D gives
  3269	 $\operatorname{obs}_g(V_{-h^\vee}(\fg)) = 0$ because
  3270	 $\kappa(V_{-h^\vee}(\fg)) = 0$. This agrees with the critical
  3271	 Feigin--Frenkel package, recorded in
  3272	 Theorem~\ref{thm:critical-level-structure}, because the vanishing of
  3273	 $\kappa$ is the statement that the scalar fiber curvature
  3274	 $d_{\mathrm{fib}}^2$ disappears. The information does not vanish; it
  3275	 moves from the scalar shadow to bar cohomology, whose degree-$0$

thinking
**Investigating label discrepancies**

I’m looking into potential findings regarding theorem D and uniform-weight. There might be other untagged uses, but they don't seem relevant right now. I'm curious if there's an unresolved reference to `conj:master-infinite-generator` versus `conj:v1-master-infinite-generator`. The file at line 912 mentions `conj:master-infinite-generator`, but the actual label is `conj:v1-master-infinite-generator`. I'll need to search the entire repository for `conj:master-infinite-generator` to check if it’s missing, which could explain the discrepancy.
codex
I found a likely dead reference: this chapter points to `conj:master-infinite-generator`, while the canonical label surface I read uses `conj:v1-master-infinite-generator`. I’m verifying that before I count it as a hard failure.
exec
/bin/zsh -lc "rg -n -F '\\label{conj:master-infinite-generator}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{conj:v1-master-infinite-generator}' chapters/connections/editorial_constitution.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 164ms:
./healing_20260413_130533/H24_vol3_cy_to_chiral_heal.md:705:\phantomsection\label{conj:master-infinite-generator}%
exec
/bin/zsh -lc "rg -n -F 'conj:master-infinite-generator' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_modules.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '900,920p'" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
chapters/connections/editorial_constitution.tex:317:\label{conj:v1-master-infinite-generator}
 succeeded in 54ms:
   900	Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
   901	Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
   902	$\mathcal{W}$ (block upper triangular,
   903	Theorem~\ref{thm:pbw-allgenera-principal-w}).
   904	For semisimple weightwise symmetry, the genus enrichment splits into
   905	non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
   906	invariant pieces killed by the family-specific $d_2$ transgression.
   907	The affine KM Killing class shows that this is an $E_3$ statement, not
   908	an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
   909	radical cohomology of the weightwise Lie action.
   910	Open: non-principal families; the $\mathcal{W}_\infty$
   911	inverse-limit package
   912	(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
   913	\end{remark}
   914	
   915	\begin{lemma}[Weightwise reduction of the genus enrichment to
   916	 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
   917	\label{lem:pbw-weightwise-g-module}
   918	\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
   919	\index{truncated current algebra!mode bookkeeping only}
 succeeded in 60ms:
chapters/theory/chiral_modules.tex:2002:(Conjecture~\ref{conj:master-infinite-generator};
chapters/theory/chiral_koszul_pairs.tex:6463:Conjecture~\ref{conj:master-infinite-generator}, not to the standard
chapters/theory/coderived_models.tex:424:Conjecture~\textup{\ref{conj:master-infinite-generator}} \textup{(MC4: proved; residual H-level comparison).}
chapters/theory/higher_genus_modular_koszul.tex:912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).












thinking
**Evaluating potential theorem issues**

I see that the label in main.tex is fine, and I don't need to find anything. Although there might be concerns about duplicate labels across volumes, they don't apply here, so I can ignore that. I'm noticing line 5816 might reference the universal-theta theorem, causing a cycle, and I need to inspect line 912 and the MC4 package for H-level identification. I have potential concerns about the three-tier architecture theorem and its claims regarding modular Koszul requirements to check further.
thinking
**Analyzing the cyclic L∞ algebra proof**

The proposition only suggests that if L is a complete cyclic L∞ algebra as stated in the genus-completed-mc-framework, but it seems that `thm:mc2-bar-intrinsic` doesn't independently construct `Defcyc(\cA)`. It relies on `thm:cyclic-linf-graph` for justification on lines 4154-4156 but doesn't reference it earlier in the proof. I’m questioning whether this oversight is a significant gap since the universal-theta proof doesn’t explicitly provide a theorem constructing `Defcyc(\cA)`, only mentioning it in relation to the MC equation from the bar differential.
thinking
**Exploring structural frameworks**

I'm thinking that the introduction states MC4 has proved something important. So, for the chapter on DAG, it seems I should highlight that `thm:completed-bar-cobar-strong` serves as a structural framework. Meanwhile, `conj:master-infinite-generator` should be identified as a residual H-level target. It feels like a clear way to align these concepts with what I'm supposed to be communicating. Let's make sure I get this right!
thinking
**Considering proofs and plans**

I’m wondering if it’s necessary to stick to my current plan. It might not be essential, but maybe it’s worth maintaining. I really need to search for the specific lines in the theorem D proof that provide clear disclaimers to back up any no-cycle claims. It feels a bit like I’m going in circles with this thought, so getting some exact references would definitely help clarify things for me.
thinking
**Considering DAG incorporation**

The user asked me to list the complete DAG, and I need to provide more than just findings. However, the structured output contract is strict. I’m thinking I could possibly add the DAG after the findings section under a `## DAG` header and then follow it with a `## Summary`. But the contract specifies returning findings as bullet points and ending with a summary. I want to keep everything concise while navigating these guidelines.
thinking
**Considering format structure**

I’m thinking that I should provide the user with a clear format that includes file and line numbers, along with corroborating information. It might be useful to include a Directed Acyclic Graph (DAG) to visualize it. I could use concise bullet points to lay out the nodes clearly, like: MC1 node, MC2 node with intrinsic and comparison branches, MC3 node, MC4 node, and MC5 node. This way, it’s organized and easier to understand!
thinking
**Understanding file logic**

I’m thinking about line 912 in the file and how it relates to MC4 residual identification. It seems important! Also, the MC2 comparison lane is dependent on Theorem D, meaning it’s downstream of MC2. So, it’s not an independent route, which could have implications in the cycle statement. It's all interconnected, and I want to ensure I get these details right, as they could be crucial for understanding the overall context!
thinking
**Refining theorem statements**

I think I need to clarify the statement that this theorem is a downstream corollary of the proved scalar lane, rather than an independent proof of MC2. I might also want to consider adjusting or removing the phrase about Theorem universal-theta. If the theorem is logically sound, then perhaps it doesn’t need to change. I should definitely mention the circular chain in the final DAG, and I might look through some specific lines in the model for more context.
thinking
**Assessing findings and terms**

I'm considering focusing on one critical finding around 10237 since it's theorem-related and pairing it with a medium finding at 3894 for repeated false equations. I think I could reduce the findings down to seven. I need to evaluate the severity of the mislabel at line 3812; it’s not about falsehood, but more about DAG drift, possibly low. The user wants precise measures, but I wonder if I should label something as low. I’ll double-check how certain terms are used in the context.
thinking
**Determining findings focus**

I’m deciding to include seven findings, focusing on the most robust ones. Here’s what I have in mind: 

1. A CRITICAL total vs. fiberwise conflation in `thm:tautological-line-support`. 
2. A HIGH conflation in `rem:theta-modular-twisting`.
3. A HIGH unconditional overclaim in `thm:three-tier-architecture`.
4. A HIGH circular reference in `prop:mc2-reduction-principle`.
5. A MEDIUM proof gap in `thm:universal-theta` missing `thm:cyclic-linf-graph`.
6. A MEDIUM stale proof-routing remark in `rem:mc2-status`.
7. A LOW hidden import in `prop:geometric-modular-operadic-mc`. 

I wonder if I should also fit in the LOW line 3812, but I think seven will be sufficient.
thinking
**Evaluating findings and relevance**

I'm considering replacing low 6004 with 3812 because it seems more relevant. I realize 3812 directly misstates the DAG while 6004's hidden import might not be as critical. Maybe I should include both for a total of eight findings, which I think is manageable. The final report will consist of eight bullets plus a summary and stay within 60 lines. Alright, I feel confident about including 3812 and maybe dropping 6004, which could still meet the user's request for the hidden import.
thinking
**Crafting a structured plan**

I need to create a clear structure for the DAG, focusing on bullet point 1, covering the canonical chain and its statuses. There might be around six bullets needed, plus one note about cycles. It's important that everything is organized logically so it’s easy to follow. I want to ensure that nothing gets missed in the overview, and the note about cycles is definitely going to be crucial!
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:10237 — PROBLEM: Theorem `thm:tautological-line-support` starts from total nilpotence `d_{\mathrm{bar}}^2=0`, then at 10293–10313 identifies the same obstruction with the fiberwise curvature `\dfib^{\,2}=\kappa\omega_g` and simply declares `\mathrm{obs}_g` and `o_g` to be the same class. That collapses the total/fiberwise distinction and leaves the load-bearing identification unproved; it also conflicts with the chapter’s own routing at 2996–3015, where `\mathrm{obs}_g=\kappa\lambda_g` is downstream of `\Theta_\cA`. FIX: Rewrite the theorem so the total differential is always `D_\cA^2=0`, the fiberwise statement is separately `d_{\mathrm{fib}}^2=\kappa\omega_g`, and insert a lemma proving the projection `d_{\mathrm{fib}}^2 \mapsto o_g`; if that lemma is unavailable, restrict the theorem to the unconditional genus-1 case and leave higher-genus/all-weight as downstream of Theorem D.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3894 — PROBLEM: `rem:theta-modular-twisting` calls
  `\partial\Theta^{(g)}+\pi\star\Theta^{(g)}+\Theta^{(g)}\star\pi+\cdots=\kappa(\cA)\omega_g`
  the “genus-$g$ component of the MC equation,” but the same remark ends at 3914–3915 by saying the MC equation is the nilpotent zero-RHS equation for `D_{\mathrm{tot}}`. This is an active flat/curved conflation. FIX: Rename 3894–3905 as the “fiberwise curved genus-$g$ identity,” explicitly say it is not the total Maurer–Cartan equation, and keep the zero-RHS MC equation only for the completed total differential.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2366 — PROBLEM: `thm:three-tier-architecture` says “Theorem D … holds unconditionally” and then says at 2370 that no Koszulity hypothesis is required. That contradicts the concordance, which scopes all-genera Theorem D to the proved uniform-weight lane and keeps genus 1 as the only universal case (`chapters/connections/concordance.tex:59`, `:64`). FIX: Replace item 0.4 with “genus-1 scalar universality holds unconditionally; all-genera scalar trace holds on the proved uniform-weight lane; multi-weight `g\ge2` requires `\delta F_g^{\mathrm{cross}}` via `thm:multi-weight-genus-expansion`,” and scope “No Koszulity hypothesis is required” only to Tier-0 items that actually use only `D_\cA^2=0`.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:5816 — PROBLEM: `prop:mc2-reduction-principle` defines its coefficient package by reference to `Theorem~\ref{thm:universal-theta}`, but `thm:mc2-conditional-completion` at 8432–8437 later uses this proposition to recover `Theorem~\ref{thm:universal-theta}`. That is a paper-level circular chain in the comparison route. FIX: Remove the reference to `thm:universal-theta` from the proposition statement and define `W_g` independently as `\Gmod^{(g)}` or as explicit finite-dimensional subspaces of `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`; then add one sentence in `thm:mc2-conditional-completion` that this route is a downstream scalar-lane recovery of an already-constructed `\Theta_\cA`, not an independent proof of MC2.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:3790 — PROBLEM: `thm:universal-theta` claims existence of the cyclic `L_\infty` algebra `\Defcyc(\cA)`, but the proof at 3818–3847 only derives the MC identity from `D_\cA^2=0` and never cites the theorem that actually constructs `\Defcyc(\cA)` (`thm:cyclic-linf-graph`). As written, the proof proves “MC once the algebra exists,” not the existence claim in the theorem statement. FIX: Insert an explicit first sentence in the proof: “The cyclic deformation algebra `\Defcyc(\cA)` exists by `Theorem~\ref{thm:cyclic-linf-graph}`; `Theorem~\ref{thm:mc2-bar-intrinsic}` identifies `\Theta_\cA` as an MC element in its strict coinvariant model.”

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:3812 — PROBLEM: “This is Theorem~\ref{thm:master-theta} (MC2)” is too strong. The canonical master theorem in `chapters/connections/editorial_constitution.tex:218–237` is a package statement centered on `\Theta_\cA^{\le2}` and then cites `thm:mc2-bar-intrinsic` and `thm:recursive-existence` for the all-degree limit. The local theorem is the all-degree realization used to resolve MC2, not the master theorem verbatim. FIX: Change 3812 to “This theorem supplies the all-degree realization used in Theorem~\ref{thm:master-theta} (MC2).”

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:5282 — PROBLEM: `rem:mc2-status` says “The proof of Theorem~\ref{thm:universal-theta} assembles” from scalar shadow, determinant line bundle, spectral discriminant, and bar-coderivation algebra. After the bar-intrinsic proof at 3818–3847, that is stale and reverses outputs into prerequisites. FIX: Either retitle it “Historical route to MC2 (superseded)” and say so explicitly, or replace the list by the live proof chain `thm:bar-modular-operad -> thm:cyclic-linf-graph -> prop:geometric-modular-operadic-mc -> thm:mc2-bar-intrinsic -> thm:genus-universality + MK:verdier`.

- [LOW] chapters/theory/higher_genus_modular_koszul.tex:6004 — PROBLEM: `prop:geometric-modular-operadic-mc` invokes the Getzler–Kapranov correspondence directly on the completed tensor product `\widehat{L}_{\Gmod}` without stating the compatibility needed to pass from the classical Feynman-transform statement to this completed setting. That is a hidden import, not a checked hypothesis. FIX: Insert a lemma before 6004 verifying that completion preserves the relevant Feynman-transform algebra structure and that `\widehat{L}_{\Gmod}` remains in the scope of `GeK98`; otherwise downgrade the last sentence of part (c) to a conditional remark.

## DAG
- MC1 is `thm:master-pbw` (`chapters/connections/editorial_constitution.tex:193`). Its explicit inputs are `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, and `thm:pbw-allgenera-principal-w`; `thm:pbw-universal-semisimple` is an extension criterion, not part of the named-family proof. Status: satisfied only for the standard finite-type interacting families.

- Within this chapter’s own architecture (`chapters/theory/higher_genus_modular_koszul.tex:2347–2449`), intrinsic MC2 is not downstream of MC1. Tier 0 starts from `D_\cA^2=0`; Tier 1 adds genus-0 Koszulity; Tier 2 adds HS-sewing.

- MC2 intrinsic is `thm:universal-theta` / `thm:master-theta`, realized locally by `thm:mc2-bar-intrinsic`. The local dependency chain read from source is:
  `thm:bar-modular-operad -> thm:prism-higher-genus -> lem:stable-graph-d-squared -> thm:convolution-d-squared-zero -> const:explicit-convolution-bracket + def:modular-convolution-dg-lie + thm:convolution-dg-lie-structure -> prop:geometric-modular-operadic-mc -> thm:cyclic-linf-graph -> thm:genus-universality + MK:verdier -> thm:mc2-bar-intrinsic -> thm:universal-theta`.
  Status: acyclic and usable, modulo the proof-citation omission in finding 5.

- MC2 comparison lane is:
  `prop:mc2-reduction-principle -> prop:geometric-modular-operadic-mc -> thm:tautological-line-support -> thm:mc2-conditional-completion -> thm:mc2-full-resolution`.
  Status: not an independent proof. The file’s own routing at 2996–3015 makes Theorem D / genus universality downstream of `\Theta_\cA`, so this lane is circular if read as foundational.

- MC3 is the evaluation-generated-core package from `chapters/theory/introduction.tex:2068–2093`: `thm:categorical-cg-all-types + cor:dk23-all-types + cor:mc3-all-types`, with type-A reinforcement by `thm:mc3-type-a-resolution`. Status: satisfied on the evaluation-generated core; post-core enlargement remains downstream.

- MC4 is the structural completion package from `chapters/theory/higher_genus_modular_koszul.tex:912` and `chapters/connections/editorial_constitution.tex:522–529`: `thm:completed-bar-cobar-strong + thm:coefficient-stability-criterion + winfty rigidity`. Status: structural framework satisfied; H-level target identification remains open via `conj:master-infinite-generator`.

- MC5, as currently proved, is only the analytic lane from `chapters/theory/introduction.tex:2060–2070` and `chapters/connections/editorial_constitution.tex:531–543`:
  `thm:algebraic-string-dictionary (g=0) + thm:genus1-universal-curvature + thm:genus1-d-squared + thm:inductive-genus-determination + prop:2d-convergence + thm:general-hs-sewing`.
  Status: analytic sewing/convergence satisfied; full genuswise BV/BRST/bar identification remains open via `conj:v1-master-bv-brst`.

- Canonical master-chain status from `editorial_constitution.tex:498–543`: `evaluation-generated core -> MC3 enlargement -> MC4 H-level comparison -> MC5 physics completion`. No unavoidable global cycle survives on that chain. The only surviving circular surface is the old MC2 comparison lane inside this chapter.

## Summary
Checked: 15 surfaces | Findings: 8 | Verdict: FAIL
tokens used
209,553
