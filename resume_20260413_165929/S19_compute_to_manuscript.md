# S19_compute_to_manuscript (642s)

- [CRITICAL] chapters/examples/w_algebras_deep.tex:3598 — PROBLEM: This summary says the self-dual central charges are the points where duality acts trivially on `\kappa`, then line 3604 states `\kappa(\text{SCA}_3)=1/2`. That contradicts the proved formula later in the same file at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5166) and [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5225), and the compute oracle at [compute/lib/theorem_sca_kappa_fix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sca_kappa_fix_engine.py:83), all of which give `\kappa(N=2)=(6-c)/(2(3-c))` with a simple pole at `c=3`. FIX: rewrite the sentence so `c=3` is only the self-dual point of the central-charge involution, not a finite fixed point of `\kappa`; replace `For N = 2: \kappa(\text{SCA}_3) = 1/2.` with `For N = 2: c=3 is the free-field limit, and \kappa has a simple pole there.`

- [HIGH] chapters/examples/w_algebras_deep.tex:3605 — PROBLEM: The `N=4` item in the same self-dual-point list uses the K3 value `\kappa(\text{small}_{c=6})=2`, not the self-dual value for the duality just stated two lines above (`c=-12`). The live chapter itself says `c=-12` is self-dual at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3569), and the corrected compute formula is `\kappa=c/3`, so the self-dual value is `-4`, not `2`. FIX: replace `For N = 4: \kappa(\text{small}_{c=6}) = 2 (= c/3, not c/2).` with `For N = 4: \kappa(\text{small}_{c=-12}) = -4 (= c/3, not c/2).` Leave the `c=6` K3 example only in the cautionary paragraph at lines 3590-3596.

- [HIGH] compute/lib/theorem_cross_volume_ap49_engine.py:933 — PROBLEM: `verify_superconformal_kappa()` still encodes the obsolete Vol I `N=4` story: the docstring says `\kappa=c/2` at line 939, and the returned `N4_small_AP49` block hardcodes `vol1_complementarity_sum = 0` and `vol1_self_dual_c = 6` at lines 998-1012. That no longer matches the live manuscript at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3569) and [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3606), which now gives self-dual `c=-12`, `\kappa=c/3`, and `\kappa+\kappa'=-8`. FIX: replace the `N=4` branch with the corrected Vol I data, ideally by importing `kappa_n4_from_c`, `n4_koszul_dual_c`, and `n4_complementarity_sum_ff` from [compute/lib/theorem_sca_kappa_fix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sca_kappa_fix_engine.py:145); the result should report `self_dual_c = -12`, `kappa_self_dual = -4`, and `ff_complementarity_sum = -8`, not a generic “convention mismatch.”

- [HIGH] compute/tests/test_theorem_cross_volume_ap49_engine.py:557 — PROBLEM: The `N=4` AP49 test is a stale oracle. It only asserts `r['N4_small_AP49']['convention_mismatch']`, so `pytest -q compute/tests/test_theorem_cross_volume_ap49_engine.py -k superconformal` passes even while the engine contradicts the current Vol I chapter. This is the exact AP128 failure mode: the test validates a hardcoded mismatch flag, not the live manuscript formula surface. FIX: delete the boolean-mismatch assertion and replace it with direct checks of the corrected values after fixing the engine, e.g. assert self-dual `c=-12`, `\kappa(-12)=-4`, and Feigin-Frenkel complementarity sum `-8`; if a Vol II comparison is still wanted, parse the actual external source in that test instead of hardcoding a discrepancy.

- [MEDIUM] chapters/examples/bar_complex_tables.tex:2609 — PROBLEM: This sentence credits `458` tests to `test_exceptional_shadows.py` and `test_non_simply_laced_shadows.py`, but `pytest --collect-only -q` gives `178` and `168` tests respectively, total `346`. The stated count is unsupported by the two named files. FIX: change `458` to `346`; if `test_exceptional_shadow_complete.py` is meant to be part of the cited verification surface, add that filename explicitly and recompute the total instead of leaving an unexplained number.

- [LOW] chapters/examples/w_algebras.tex:5768 — PROBLEM: The manuscript says `test_w3_genus2.py` has `105` tests, but `pytest --collect-only -q compute/tests/test_w3_genus2.py` collects `125`. FIX: change `$105$~tests` to `$125$~tests`, or remove the numeric count and keep only the file reference so the prose stops drifting when the test surface grows.

- [LOW] compute/lib/theorem_sca_kappa_fix_engine.py:6 — PROBLEM: The audit engine’s seam pointers are stale: it sends the Vol I `N=2` formula to `w_algebras_deep.tex line 4913` and the `N=4` correction to `line 3328`, but the live chapter now carries the `N=2` formula at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5166) and the corrected superconformal hierarchy at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3548). FIX: replace raw line numbers with stable labels (`thm:n2-kappa`, `prop:n2-koszul-duality`, `rem:superconformal-complementarity-hierarchy`) or update the line references to the current locations.

## Summary
Checked: 11 | Findings: 7 | Verdict: FAIL


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
session id: 019d875a-d422-76b2-a4dd-dd79f9f90c8e
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


MISSION: SEAM AUDIT between compute/lib/ and chapters/examples/.

Compute engines→Manuscript. Check: (a) computed values in engines match what manuscript claims, (b) test expected values match compute output, (c) no AP128 (engine/test same wrong model)

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers
codex
Audit scope is the `compute/lib/` ↔ `chapters/examples/` seam: I’m reading the repo constitution, the audit skill, and then I’ll map every example surface that cites or depends on compute outputs before checking engines, tests, and manuscript claims against each other.
exec
/bin/zsh -lc "rg --files compute/lib chapters/examples tests | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files | rg '"'^(CLAUDE'"\\.md|chapters/connections/concordance\\.tex|metadata/theorem_registry\\.md|(.*/)?red_team_summary\\.md|\\.agents/skills/deep-beilinson-audit/SKILL\\.md)"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/concordance.tex
 succeeded in 52ms:
rg: tests: No such file or directory (os error 2)
chapters/examples/deformation_quantization.tex
chapters/examples/w_algebras_deep.tex
chapters/examples/symmetric_orbifolds.tex
chapters/examples/lattice_foundations.tex
chapters/examples/beta_gamma.tex
chapters/examples/yangians.tex
chapters/examples/y_algebras.tex
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/w3_holographic_datum.tex
chapters/examples/heisenberg_eisenstein.tex
chapters/examples/free_fields.tex
chapters/examples/yangians_foundations.tex
chapters/examples/kac_moody.tex
chapters/examples/toroidal_elliptic.tex
chapters/examples/bershadsky_polyakov.tex
chapters/examples/bar_complex_tables.tex
chapters/examples/minimal_model_fusion.tex
chapters/examples/landscape_census.tex
chapters/examples/w3_composite_fields.tex

thinking
**Locating red team summary**

I need to locate the red_team_summary, but there might be issues with the search pattern not matching. I think I'll try using a command to search for files ending in 'red_team_summary.md'. 

It seems I might also need to run an explorer agent to address questions about the codebase. Maybe I'll spawn the explorer for mapping the seam. An exhaustive audit of the surface, including chapters, examples, and references, sounds necessary. I should start by defining a plan and using the deep-beilinson-audit skill file first.
codex
I’ve mapped the seam directories. Next I’m loading the audit workflow and the required constitutional files, then I’ll enumerate which example chapters actually mention specific engines, outputs, or test oracles so the audit stays grounded instead of diffuse.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg '(?:"'^|/)red_team_summary'"\\.md"'$|'"\\.agents/skills/deep-beilinson-audit/SKILL\\.md"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

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

 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 exited 1 in 51ms:


thinking
**Searching for skill file**

I need to locate the skill file, possibly along with the red_team files. When I search, it seems I'm getting no results, which is frustrating. Maybe I should check the archive path? It's puzzling because I expected to find something there. I'll keep looking and explore those archives to see if I can uncover what I need. There’s definitely something I must be missing!
codex
The constitutional reads are loaded. I still need the local audit skill and the red-team note, then I’ll trace which example files actually consume compute outputs so I can audit concrete seam claims rather than every file indiscriminately.
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc "find . -name 'red_team_summary.md' -o -path './.agents/skills/deep-beilinson-audit/SKILL.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 521ms:
./archive/raeeznotes/raeeznotes100/red_team_summary.md
./.agents/skills/deep-beilinson-audit/SKILL.md

thinking
**Planning for codebase audit**

I think I might need to use an explorer agent for this task since it's about a codebase audit. It makes sense to utilize the explorer for searching efficiently. I should also consider updating my plan, so let's put together a structured plan with the necessary steps. It’s important that I lay this out clearly to make sure I cover everything needed for the audit. Let's dive into that!
Plan update
Audit will stay on the compute/manuscript seam and only report grounded inconsistencies with exact fixes.
  → Map seam links between `compute/lib/`, tests, and `chapters/examples/` by explicit file references and shared invariants
  • Read each linked engine/test/manuscript cluster in context and compare claimed values, formulas, and statuses
  • Run targeted engines/tests where needed to break ties and detect AP128 engine/test lockstep failures
  • Re-verify surviving findings and return exact file:line fixes in severity order

thinking
**Searching and mapping seams**

I need to search for relevant files and read transition points thoroughly. The task involves checking if computed values in engines match the manuscript's claims and testing expected values against compute outputs. So, I should identify all the seam surfaces between the compute/lib and chapters/examples. It seems like I'll need to use tools to find chapter names or labels and search for specific references in `.tex` files. I'll also look for tests, potentially in `compute/tests`. Let’s get started!
codex
I’m at the seam-mapping stage now. The key question is which example chapters are actually backed by specific engines or test oracles; after that I can audit cluster by cluster instead of scanning 200 unrelated modules.
exec
/bin/zsh -lc "find compute -maxdepth 3 \\( -path '*/test*' -o -name '*test*.py' -o -name 'test_*.py' \\) | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"chapters/examples|landscape_census|genus_expansions|free_fields|kac_moody|beta_gamma|w_algebras|yangians|bershadsky_polyakov|moonshine|minimal_model|symmetric_orbifolds|n2_superconformal|lattice_foundations|heisenberg_eisenstein|bar_complex_tables|deformation_quantization|w3_holographic_datum|w3_composite_fields\" compute/lib -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 2824

compute/lib/arithmetic_comparison_test.py
compute/lib/coxeter_anomaly_test.py
compute/lib/kac_chevalley_test.py
compute/lib/modular_periodicity_test.py
compute/lib/offdiag_newton_test.py
compute/lib/theorem_bv_brst_genus2_test_engine.py
compute/lib/virasoro_c13_test.py
compute/scripts/analyze_pytest_shards.py
compute/scripts/run_full_pytest.py
compute/tests
compute/tests/__init__.py
compute/tests/__pycache__
compute/tests/__pycache__/__init__.cpython-314.pyc
compute/tests/__pycache__/conftest.cpython-314-pytest-9.0.2.pyc
compute/tests/__pycache__/test_a2_polynomial_combinatorics_engine.cpython-314-pytest-9.0.2.pyc
compute/tests/__pycache__/test_admissible_deep_bar_engine.cpython-314-pytest-9.0.2.pyc
compute/tests/__pycache__/test_admissible_koszul_rank2_engine.cpython-314-pytest-9.0.2.pyc
compute/tests/__pycache__/test_admissible_level_bar_engine.cpython-314-pytest-9.0.2.pyc
exec
/bin/zsh -lc "rg -n \"compute/lib|compute/|engine|verification|verified|script|generated|oracle|pytest|unittest|expected\" chapters/examples compute -g '"'!**/__pycache__/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1681

compute/lib/mv_positivity_sl3.py:32:  - yangians.tex: conj:mv-positivity-yangian, sec:asymptotic-characters
compute/lib/genus_expansion.py:38:# Known kappa values (ground truth from Master Table / genus_expansions.tex)
compute/lib/w3_wline_shadow_tower.py:31:  - cor:w3-wline-parity-vanishing (w_algebras.tex)
compute/lib/w3_bar.py:235:    Ground truth: comp:w3-deg3-structure (w_algebras_deep.tex:519-610).
compute/lib/w3_bar.py:264:    Ground truth: comp:w3-deg3-mixed (w_algebras_deep.tex:612-657).
compute/lib/w3_bar.py:286:    Ground truth: comp:w3-deg3-mixed (w_algebras_deep.tex:640-657).
compute/lib/w3_bar.py:309:    Ground truth: comp:w3-arnold-deg3 (w_algebras_deep.tex:659-698).
compute/lib/w3_bar.py:326:    Ground truth: comp:w3-deg3-cohom (w_algebras_deep.tex:724-758).
compute/lib/moment_matrix_exclusion.py:37:from virasoro_epstein_attack import minimal_model_primaries, minimal_model_central_charge
compute/lib/moment_matrix_exclusion.py:71:    primaries = minimal_model_primaries(m)
compute/lib/moment_matrix_exclusion.py:90:    primaries = minimal_model_primaries(m)
compute/lib/moment_matrix_exclusion.py:91:    c = minimal_model_central_charge(m)
compute/lib/cy_lattice_voa_k3_engine.py:123:  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
compute/lib/bar_cohomology_virasoro_explicit_engine.py:71:  comp:virasoro-ope, comp:virasoro-bar-diff (bar_complex_tables.tex)
compute/lib/bar_cohomology_virasoro_explicit_engine.py:73:  prop:virasoro-generic-koszul-dual (w_algebras.tex)
compute/lib/bar_cohomology_virasoro_explicit_engine.py:74:  prop:arnold-virasoro-deg3 (bar_complex_tables.tex)
compute/lib/quartic_arithmetic_closure.py:505:        # Contact (depth 4): mu_{beta_gamma} = 0, terminates at arity 4
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:1083:def verify_pva_deformation_quantization_frontier() -> Dict[str, Any]:
 succeeded in 51ms:
Total output lines: 9929

chapters/examples/deformation_quantization.tex:254:angle integral). Higher orders are verified in
chapters/examples/deformation_quantization.tex:262:verification that configuration space integrals on $\overline{C}_n^{\mathrm{ch}}(X)$
chapters/examples/deformation_quantization.tex:836:\begin{computation}[Complete \texorpdfstring{$\hbar^2$}{2} weight verification]
chapters/examples/deformation_quantization.tex:934:This is verified by Stokes' theorem on $\overline{C}_3(\mathfrak{H})$
chapters/examples/deformation_quantization.tex:942:verified by Arnal--Manchon--Masmoudi):
chapters/examples/deformation_quantization.tex:979:compactification is generated by logarithmic forms with
chapters/examples/deformation_quantization.tex:1036:\emph{Associativity verification.}
chapters/examples/deformation_quantization.tex:1443:\begin{verification}[Node: $b_F^2 = 0$ for $F(x) = x^2$]
chapters/examples/deformation_quantization.tex:1455:\end{verification}
chapters/examples/deformation_quantization.tex:1457:\begin{verification}[Cusp: $b_F^2 = 0$ for $F(x) = x^3$]
chapters/examples/deformation_quantization.tex:1467:\end{verification}
chapters/examples/deformation_quantization.tex:1557:\begin{verification}[$A_\infty$ identities for the cusp $F(x) = x^3$]
chapters/examples/deformation_quantization.tex:1559:\index{$A_\infty$ algebra!cusp verification}
chapters/examples/deformation_quantization.tex:1609:\end{verification}
chapters/examples/deformation_quantization.tex:1695:derived critical locus admits a particularly clean description:
chapters/examples/deformation_quantization.tex:1863:commutative dg algebra: it is freely generated as a graded-commutative
chapters/examples/deformation_quantization.tex:1875:states that for a smooth (semi-free, finitely generated)
chapters/examples/w_algebras_deep.tex:24:nilpotent currents) reduces, through the bar-cobar engine, to

thinking
**Auditing high-risk clusters**

I think the easiest approach is to audit high-risk clusters by looking at examples that have direct engine references or known compute-backed claims. I see a list of files to check, like `free_fields.tex` and `bar_complex_tables.tex`. However, the user asked about seam compute/lib and chapters/examples, so I should focus on example files that specifically mention compute modules. I might need to use grep to find these direct references in the chapters and examples.
exec
/bin/zsh -lc "rg -n \"compute/(lib|tests)|test_[A-Za-z0-9_]+\\.py|\\.py\\}|\\.py\\)|\\.py\\]|\\.py,|\\.py\\.\" chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"chapters/examples/[A-Za-z0-9_./-]+|free_fields\\.tex|kac_moody\\.tex|beta_gamma\\.tex|w_algebras\\.tex|w_algebras_deep\\.tex|bar_complex_tables\\.tex|genus_expansions\\.tex|landscape_census\\.tex|yangians\\.tex|yangians_foundations\\.tex|yangians_drinfeld_kohno\\.tex|lattice_foundations\\.tex|moonshine\\.tex|minimal_model_examples\\.tex|symmetric_orbifolds\\.tex|n2_superconformal\\.tex|bershadsky_polyakov\\.tex|heisenberg_eisenstein\\.tex\" compute/lib -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:3081:\texttt{test\_ds\_cascade\_shadows.py}.
chapters/examples/w_algebras_deep.tex:4399:All data verified by \texttt{test\_higher\_w\_shadows.py}
chapters/examples/w_algebras_deep.tex:5487:\texttt{test\_pixton\_genus3\_shadow\_engine.py} and
chapters/examples/w_algebras_deep.tex:5488:\texttt{test\_pixton\_shadow\_bridge.py}\textup{)}. Agreement
chapters/examples/lattice_foundations.tex:1845:\texttt{compute/lib/moonshine\_shadow\_depth.py}),
chapters/examples/lattice_foundations.tex:2448:(\texttt{compute/lib/e1\_lattice\_bar.py}, 45 tests passing).
chapters/examples/beta_gamma.tex:270:\texttt{theorem\_three\_paper\_intersection\_engine.py} module, which
chapters/examples/beta_gamma.tex:2554:\texttt{compute/lib/betagamma\_quartic\_contact.py}.\qedhere
chapters/examples/w3_holographic_datum.tex:5:% Source: compute/lib/theorem_w3_holographic_datum_engine.py (83 tests).
chapters/examples/w3_holographic_datum.tex:25:\texttt{compute/lib/theorem\_w3\_holographic\_datum\_engine.py}
chapters/examples/w3_holographic_datum.tex:221:\texttt{theorem\_w3\_holographic\_datum\_engine.py} implements:
chapters/examples/w3_holographic_datum.tex:747:\texttt{compute/lib/theorem\_w3\_holographic\_datum\_engine.py}
chapters/examples/w3_holographic_datum.tex:750:\texttt{compute/tests/test\_theorem\_w3\_holographic\_datum\_engine.py}.
chapters/examples/free_fields.tex:825:\texttt{compute/tests/} (the full family of $bc$-shadow tests all
chapters/examples/free_fields.tex:1387:\texttt{compute/lib/betagamma\_shadow\_full.py}
chapters/examples/free_fields.tex:1389:\texttt{compute/tests/test\_betagamma\_shadow\_full.py}
chapters/examples/bershadsky_polyakov.tex:179:\texttt{bp\_shadow\_tower.py} uses the FKR convention throughout;
chapters/examples/bershadsky_polyakov.tex:180:\texttt{kappa\_deficit\_ds.py} uses the alternate convention and
chapters/examples/bershadsky_polyakov.tex:280:paths in \texttt{bp\_shadow\_tower.py} and
chapters/examples/bershadsky_polyakov.tex:281:\texttt{kappa\_deficit\_ds.py}. The anomaly ratio $\varrho = 1/6$
 succeeded in 52ms:
Total output lines: 671

compute/lib/thick_generation_sl2.py:30:  - yangians.tex, conj:shifted-prefundamental-generation
compute/lib/theorem_c_complementarity.py:34:  prop:kappa-anti-symmetry-ff (kac_moody.tex)
compute/lib/theorem_c_complementarity.py:35:  prop:complementarity-genus-series (genus_expansions.tex)
compute/lib/shadow_mzv_engine.py:72:    yangians_drinfeld_kohno.tex: KZ connection
compute/lib/bc_exceptional_categorical_zeta_engine.py:57:    thm:categorical-cg-all-types (yangians_drinfeld_kohno.tex)
compute/lib/higher_w_shadows.py:62:  thm:w-universal-gravitational-cubic (w_algebras.tex)
compute/lib/higher_w_shadows.py:63:  comp:w4-kappa (w_algebras.tex)
compute/lib/genus3_landscape.py:35:KAPPA CONVENTIONS (authoritative, from landscape_census.tex, AP1/AP9):
compute/lib/genus3_landscape.py:48:    thm:lattice-all-genera (genus_expansions.tex)
compute/lib/genus3_landscape.py:49:    prop:betagamma-obstruction-coefficient (beta_gamma.tex)
compute/lib/genus3_landscape.py:50:    thm:wn-obstruction (w_algebras.tex)
compute/lib/genus3_landscape.py:51:    comp:genus-3-sl2 (genus_expansions.tex)
compute/lib/genus3_landscape.py:52:    comp:w3-genus-expansion (genus_expansions.tex)
compute/lib/genus4_landscape.py:30:KAPPA CONVENTIONS (authoritative, from landscape_census.tex, AP1/AP9):
compute/lib/genus4_landscape.py:42:    thm:lattice-all-genera (genus_expansions.tex)
compute/lib/genus4_landscape.py:43:    prop:betagamma-obstruction-coefficient (beta_gamma.tex)
compute/lib/genus4_landscape.py:44:    thm:wn-obstruction (w_algebras.tex)
compute/lib/mv_positivity_sl3.py:32:  - yangians.tex: conj:mv-positivity-yangian, sec:asymptotic-characters




thinking
**Auditing compute references**

I need to collect specific files for auditing. The direct chapter references show clear seam points. I'll focus on auditing explicit compute-backed claims instead of every compute/lib file, which still leaves a lot to check—around 39 lines. We should compare compute outputs, manuscripts, and tests, aiming for a thorough audit despite time constraints. Building a list of clusters based on direct engine mentions will help us find actual findings while avoiding false positives. I'll follow a systematic approach to make this as comprehensive as possible!
thinking
**Identifying inconsistencies for audit**

I need to focus on potential inconsistencies like outdated file names, incorrect test counts, and mismatched claimed values with engine constants. I'll provide fix instructions since the user is asking for an audit rather than edits. They’ve explicitly requested findings and not changes. I might run targeted tests to verify mismatches and could script a scan for chapter references to non-existent files, which seems to imply a gap. For example, checking if files like `betagamma_shadow_full.py` exist is essential. If not, that's definitely a finding!
thinking
**Addressing stale references and discrepancies**

I’m noticing that many references might be outdated. There's a seam issue where the chapters claim that all data is verified by 149 tests, but the actual test file might show a different count or could even be missing. I need to count the tests, possibly using `pytest --collect-only` or by checking function counts.

Another inconsistency could arise from comparing engine formulas to those in the manuscript. For example, the free_fields chapter references `betagamma_shadow_full.py`, which may be outdated, so I need to verify whether the current engine file exists and whether it has the correct coefficients.
thinking
**Inspecting compute references**

I think the user is asking for a thorough analysis of inconsistencies or gaps in the references I've used. To tackle this, I could start by mapping the direct compute references and their existence, which might uncover various findings. Additionally, I need to consider any subtle aspects related to AP128 and ensure that I’m including exact fixes. It seems like inspecting the direct references and checking for actual file existence would be a valuable step. Maybe using a shell script to parse the data would help too.
codex
I’ve identified the explicit seam points in the example chapters. The fastest way to break this surface is: first kill stale or nonexistent engine/test references, then inspect the surviving live clusters for value mismatches and engine/test lockstep failures.
exec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
root=pathlib.Path('.')
for path in sorted(pathlib.Path('chapters/examples').glob('*.tex')):
    for i,line in enumerate(path.read_text().splitlines(),1):
        for m in re.finditer(r'([A-Za-z0-9_/.-]+\\.py)', line):
            ref=m.group(1)
            print(f'{path}:{i}:{ref}:{(root/ref).exists()}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import pathlib,re
for path in sorted(pathlib.Path('chapters/examples').glob('*.tex')):
    for i,line in enumerate(path.read_text().splitlines(),1):
        if 'test_' in line or 'compute/lib/' in line:
            print(f'{path}:{i}:{line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
 exited 127 in 52ms:
zsh:1: command not found: python
codex
The first pass hit an environment issue: this workspace has `python3`, not `python`. I’m rerunning the seam extraction with `python3` so I can mechanically verify which cited engines/tests actually exist before reading deeper clusters.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
for path in sorted(pathlib.Path('chapters/examples').glob('*.tex')):
    for i,line in enumerate(path.read_text().splitlines(),1):
        for m in re.finditer(r'([A-Za-z0-9_/.-]+\\.py)', line):
            ref=m.group(1)
            print(f'{path}:{i}:{ref}:{(root/ref).exists()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
chapters/examples/bar_complex_tables.tex:1019:_loop.py:False
chapters/examples/bar_complex_tables.tex:1039:_decomp.py:False
chapters/examples/bar_complex_tables.tex:1163:_dims.py:False
chapters/examples/bar_complex_tables.tex:1965:_verification.py:False
chapters/examples/bar_complex_tables.tex:1967:_verification.py:False
chapters/examples/bar_complex_tables.tex:2609:_shadows.py:False
chapters/examples/bar_complex_tables.tex:2609:_shadows.py:False
chapters/examples/bar_complex_tables.tex:3145:_landscape.py:False
chapters/examples/bar_complex_tables.tex:3146:_comprehensive.py:False
chapters/examples/bershadsky_polyakov.tex:179:_tower.py:False
chapters/examples/bershadsky_polyakov.tex:180:_ds.py:False
chapters/examples/bershadsky_polyakov.tex:280:_tower.py:False
chapters/examples/bershadsky_polyakov.tex:281:_ds.py:False
chapters/examples/beta_gamma.tex:270:_engine.py:False
chapters/examples/beta_gamma.tex:2554:_contact.py:False
chapters/examples/free_fields.tex:1387:_full.py:False
chapters/examples/free_fields.tex:1389:_full.py:False
chapters/examples/genus_expansions.tex:1458:_explicit.py:False
chapters/examples/genus_expansions.tex:1509:_engine.py:False
chapters/examples/genus_expansions.tex:1602:_engine.py:False
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib
for path in sorted(pathlib.Path('chapters/examples').glob('*.tex')):
    for i,line in enumerate(path.read_text().splitlines(),1):
        if 'test_' in line or 'compute/lib/' in line or '.py' in line:
            print(f'{path}:{i}:{line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/bar_complex_tables.tex:1019:\texttt{ce\_cohomology\_loop.py}:
chapters/examples/bar_complex_tables.tex:1039:Direct computation (verified in \texttt{sl3\_casimir\_decomp.py})
chapters/examples/bar_complex_tables.tex:1163:\emph{Verified by \texttt{koszul\_dual\_dims.py} {\normalfont(27 tests)}.}
chapters/examples/bar_complex_tables.tex:1965:Module \texttt{compute/lib/bar\_cohomology\_verification.py},
chapters/examples/bar_complex_tables.tex:1967:\texttt{test\_bar\_cohomology\_verification.py}.
chapters/examples/bar_complex_tables.tex:2609:The following table collects the shadow obstruction tower data for all exceptional ($E_6, E_7, E_8$) and non-simply-laced ($B_2, G_2, F_4$) affine Kac--Moody algebras. Every family is class L (shadow depth $r_{\max} = 3$), with cubic shadow $C$ from the Lie bracket, quartic shadow $S_4 = 0$ by the Jacobi identity, and critical discriminant $\Delta = 8\kappa S_4 = 0$. The r-matrix has a simple pole at $z = 0$ ($d\log$ extraction absorbs one power), and complementarity $\kappa + \kappa' = 0$ holds for all Kac--Moody families. All data verified by 458 compute tests (\texttt{test\_exceptional\_shadows.py}, \texttt{test\_non\_simply\_laced\_shadows.py}).
chapters/examples/bar_complex_tables.tex:3145:\texttt{test\_rmatrix\_landscape.py} and
chapters/examples/bar_complex_tables.tex:3146:\texttt{test\_rmatrix\_poles\_comprehensive.py}
chapters/examples/bershadsky_polyakov.tex:179:\texttt{bp\_shadow\_tower.py} uses the FKR convention throughout;
chapters/examples/bershadsky_polyakov.tex:180:\texttt{kappa\_deficit\_ds.py} uses the alternate convention and
chapters/examples/bershadsky_polyakov.tex:280:paths in \texttt{bp\_shadow\_tower.py} and
chapters/examples/bershadsky_polyakov.tex:281:\texttt{kappa\_deficit\_ds.py}. The anomaly ratio $\varrho = 1/6$
chapters/examples/beta_gamma.tex:270:\texttt{theorem\_three\_paper\_intersection\_engine.py} module, which
chapters/examples/beta_gamma.tex:2554:\texttt{compute/lib/betagamma\_quartic\_contact.py}.\qedhere
chapters/examples/free_fields.tex:1387:\texttt{compute/lib/betagamma\_shadow\_full.py}
chapters/examples/free_fields.tex:1389:\texttt{compute/tests/test\_betagamma\_shadow\_full.py}
chapters/examples/genus_expansions.tex:1458:\texttt{w3\_genus3\_cross\_channel\_explicit.py}.
chapters/examples/genus_expansions.tex:1509:\textup{(}\texttt{delta\_f4\_universal\_engine.py},
chapters/examples/genus_expansions.tex:1602:\textup{(}\texttt{test\_multi\_weight\_cross\_channel\_engine.py}.\textup{)}
chapters/examples/genus_expansions.tex:1673:\textup{(}\texttt{test\_theorem\_w4\_full\_ope\_delta\_f2\_engine.py}.\textup{)}
codex
The direct-reference list is already productive: many chapter claims point to old engine/test names. I’m now checking whether each cited file has a live replacement, because a stale path is only a real finding if I can name the exact replacement or say the claim has lost its current oracle.
exec
/bin/zsh -lc "rg --files compute/lib compute/tests | rg 'virasoro_quartic_contact|virasoro_shadow_extended|w3_shadow_extended|w3_genus2|ds_cascade_shadows|higher_w_shadows|pixton|betagamma_shadow_full|betagamma_quartic_contact|theorem_three_paper_intersection_engine|theorem_w3_holographic_datum_engine|theorem_sl3_yangian_r_matrix_engine|lqt_e1_growth|sectorwise_finiteness|theorem_dk0_evaluation_bridge_engine|yangian_rtt_all_types|quantum_rmatrix_barcomplex|bethe_ansatz_shadow|kz_conformal_blocks|verlinde_shadow_algebra|linf_modular_higher|baxter_q_from_mc|wild_quiver_chiral_engine|moonshine_shadow_depth|e1_lattice_bar|cy_n4sca_k3_engine|cy_mock_modular_bps_engine|bar_hocolim_chain_level|theorem_class_l_generating_function_engine|exceptional_shadow|non_simply_laced_shadows|koszulness_landscape|shadow_connection|propagator_variance|shadow_epstein_zeta|rmatrix_landscape|rmatrix_poles_comprehensive|bar_cohomology_verification|koszul_dual_dims|ce_cohomology_loop|sl3_casimir_decomp'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_logarithmic_pixton.py
compute/tests/test_shadow_connection.py
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
compute/tests/test_pixton_planted_forest.py
compute/tests/test_non_simply_laced_shadows.py
compute/tests/test_exceptional_shadow_engine.py
compute/tests/test_verlinde_shadow_algebra.py
compute/tests/test_wild_quiver_chiral_engine.py
compute/tests/test_w3_genus2_cross_channel.py
compute/tests/test_theorem_pixton_membership_g3_engine.py
compute/tests/test_propagator_variance.py
compute/tests/test_propagator_variance_landscape.py
compute/tests/test_linf_modular_higher.py
compute/tests/test_yangian_rtt_all_types.py
compute/tests/test_theorem_w3_holographic_datum_engine.py
compute/tests/test_mg_w3_genus2_graph.py
compute/tests/test_ce_cohomology_loop.py
compute/tests/test_pixton_generation_g4_advanced.py
compute/lib/pixton_genus3_shadow_engine.py
compute/lib/moonshine_shadow_depth.py
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
refs = [
('chapters/examples/w_algebras.tex',3712,'virasoro_quartic_contact'),
('chapters/examples/w_algebras.tex',4453,'ds_cascade_shadows'),
('chapters/examples/w_algebras.tex',4722,'higher_w_shadows'),
('chapters/examples/w_algebras.tex',5015,'virasoro_shadow_extended'),
('chapters/examples/w_algebras.tex',5553,'w3_shadow_extended'),
('chapters/examples/w_algebras.tex',5768,'w3_genus2'),
('chapters/examples/w_algebras.tex',7092,'ds_nonprincipal_shadows'),
('chapters/examples/free_fields.tex',1387,'betagamma_shadow_full'),
('chapters/examples/beta_gamma.tex',2554,'betagamma_quartic_contact'),
('chapters/examples/w_algebras_deep.tex',3081,'ds_cascade_shadows'),
('chapters/examples/w_algebras_deep.tex',4399,'higher_w_shadows'),
('chapters/examples/w_algebras_deep.tex',5487,'pixton_genus3_shadow_engine'),
('chapters/examples/w_algebras_deep.tex',5488,'pixton_shadow_bridge'),
('chapters/examples/w3_holographic_datum.tex',5,'theorem_w3_holographic_datum_engine'),
('chapters/examples/yangians_computations.tex',624,'theorem_sl3_yangian_r_matrix_engine'),
('chapters/examples/yangians_computations.tex',2734,'lqt_e1_growth'),
('chapters/examples/yangians_computations.tex',2753,'sectorwise_finiteness'),
('chapters/examples/yangians_drinfeld_kohno.tex',272,'theorem_dk0_evaluation_bridge_engine'),
('chapters/examples/yangians_foundations.tex',277,'yangian_rtt_all_types'),
('chapters/examples/landscape_census.tex',387,'wild_quiver_chiral_engine'),
('chapters/examples/lattice_foundations.tex',1845,'moonshine_shadow_depth'),
('chapters/examples/lattice_foundations.tex',2448,'e1_lattice_bar'),
('chapters/examples/kac_moody.tex',5439,'theorem_class_l_generating_function_engine'),
]
allfiles=[str(p) for p in pathlib.Path('compute').rglob('*.py')]
for f,l,stem in refs:
    matches=[p for p in allfiles if pathlib.Path(p).stem==stem]
    print(f'{f}:{l}:{stem}:{matches}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 192ms:
chapters/examples/w_algebras.tex:3712:virasoro_quartic_contact:['compute/lib/virasoro_quartic_contact.py']
chapters/examples/w_algebras.tex:4453:ds_cascade_shadows:['compute/lib/ds_cascade_shadows.py']
chapters/examples/w_algebras.tex:4722:higher_w_shadows:['compute/lib/higher_w_shadows.py']
chapters/examples/w_algebras.tex:5015:virasoro_shadow_extended:['compute/lib/virasoro_shadow_extended.py']
chapters/examples/w_algebras.tex:5553:w3_shadow_extended:['compute/lib/w3_shadow_extended.py']
chapters/examples/w_algebras.tex:5768:w3_genus2:['compute/lib/w3_genus2.py']
chapters/examples/w_algebras.tex:7092:ds_nonprincipal_shadows:['compute/lib/ds_nonprincipal_shadows.py']
chapters/examples/free_fields.tex:1387:betagamma_shadow_full:['compute/lib/betagamma_shadow_full.py']
chapters/examples/beta_gamma.tex:2554:betagamma_quartic_contact:['compute/lib/betagamma_quartic_contact.py']
chapters/examples/w_algebras_deep.tex:3081:ds_cascade_shadows:['compute/lib/ds_cascade_shadows.py']
chapters/examples/w_algebras_deep.tex:4399:higher_w_shadows:['compute/lib/higher_w_shadows.py']
chapters/examples/w_algebras_deep.tex:5487:pixton_genus3_shadow_engine:['compute/lib/pixton_genus3_shadow_engine.py']
chapters/examples/w_algebras_deep.tex:5488:pixton_shadow_bridge:['compute/lib/pixton_shadow_bridge.py']
chapters/examples/w3_holographic_datum.tex:5:theorem_w3_holographic_datum_engine:['compute/lib/theorem_w3_holographic_datum_engine.py']
chapters/examples/yangians_computations.tex:624:theorem_sl3_yangian_r_matrix_engine:['compute/lib/theorem_sl3_yangian_r_matrix_engine.py']
chapters/examples/yangians_computations.tex:2734:lqt_e1_growth:['compute/lib/lqt_e1_growth.py']
chapters/examples/yangians_computations.tex:2753:sectorwise_finiteness:['compute/lib/sectorwise_finiteness.py']
chapters/examples/yangians_drinfeld_kohno.tex:272:theorem_dk0_evaluation_bridge_engine:['compute/lib/theorem_dk0_evaluation_bridge_engine.py']
chapters/examples/yangians_foundations.tex:277:yangian_rtt_all_types:['compute/lib/yangian_rtt_all_types.py']
chapters/examples/landscape_census.tex:387:wild_quiver_chiral_engine:['compute/lib/wild_quiver_chiral_engine.py']




thinking
**Evaluating file references**

I see that many references to files can be partial because the paths might be missing. I should compare counts and contents of files, and potentially use mechanical checks for test file counts. There might be ambiguity if a chapter references a test file that exists but lacks a specific path. 

I could write a script to map all referenced `.py` files to the existing files in the compute directory. It’s essential to check for any mismatches or missing files.
thinking
**Auditing test counts**

I think we should audit the clusters to compare the explicit test counts mentioned in the chapters against the actual test counts. A mismatch between these counts could be a concrete issue. We need to run `pytest --collect-only -q` on the specific test files to verify the counts. For example, the w3_holographic_datum references 83 tests, so I need to confirm this count. 

We can programmatically collect and verify all test counts, checking the discrepancies noted across chapters. It may require mapping chapter references to the respective test files and their expected counts.
thinking
**Checking computed values**

I realize that for comments on engine counts, the figures might not always align perfectly. However, the user wants to ensure that computed values correspond with what’s claimed in the manuscript. I need to check for any formula or value mismatches as well. 

We can investigate potential mismatches by examining engine comments that reference incorrect lines or corrections. For instance, the `theorem_sca_kappa_fix_engine.py` document mentions that w_algebras_deep had an incorrect table, but that might be an issue from a previous seam. I’ll need to assess the current state to clarify this.
thinking
**Considering testing options**

I should probably use `pytest --collect-only` with specific files, even if it might be a bit slow, especially for up to 20 files. It feels okay since it doesn't need a network connection. I’m thinking of utilizing a script loop to streamline the process further. This could be helpful to ensure I'm covering everything I need without unnecessary delays—efficiency is key here!
codex
I have the live engine/test replacements for the cited seam files. Now I’m checking whether the manuscript’s claimed oracle sizes are still true; stale test counts are low severity, but they’re reliable indicators of where the seam drifted and where the surrounding numerical claims deserve a closer read.
exec
/bin/zsh -lc "python3 - <<'PY'
import subprocess, re, pathlib
checks = [
('chapters/examples/w3_holographic_datum.tex',5,'compute/tests/test_theorem_w3_holographic_datum_engine.py',83),
('chapters/examples/w_algebras.tex',4453,'compute/tests/test_ds_cascade_shadows.py',149),
('chapters/examples/w_algebras.tex',4722,'compute/tests/test_higher_w_shadows.py',112),
('chapters/examples/w_algebras.tex',5553,'compute/tests/test_w3_shadow_extended.py',90),
('chapters/examples/w_algebras.tex',5768,'compute/tests/test_w3_genus2.py',105),
('chapters/examples/w_algebras_deep.tex',5487,'compute/tests/test_pixton_genus3_shadow_engine.py',None),
('chapters/examples/kac_moody.tex',4507,'compute/tests/test_non_simply_laced_shadows.py',168),
('chapters/examples/bar_complex_tables.tex',2609,'compute/tests/test_exceptional_shadows.py',None),
]
for tex,line,test,claimed in checks:
    p = subprocess.run(['pytest','--collect-only','-q',test],capture_output=True,text=True)
    out = p.stdout + p.stderr
    m = re.search(r'([0-9]+) tests? collected', out)
    count = int(m.group(1)) if m else None
    print(f'{tex}:{line}:{test}:claimed={claimed}:collected={count}:returncode={p.returncode}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 4.62s:
chapters/examples/w3_holographic_datum.tex:5:compute/tests/test_theorem_w3_holographic_datum_engine.py:claimed=83:collected=83:returncode=0
chapters/examples/w_algebras.tex:4453:compute/tests/test_ds_cascade_shadows.py:claimed=149:collected=149:returncode=0
chapters/examples/w_algebras.tex:4722:compute/tests/test_higher_w_shadows.py:claimed=112:collected=112:returncode=0
chapters/examples/w_algebras.tex:5553:compute/tests/test_w3_shadow_extended.py:claimed=90:collected=90:returncode=0
chapters/examples/w_algebras.tex:5768:compute/tests/test_w3_genus2.py:claimed=105:collected=125:returncode=0
chapters/examples/w_algebras_deep.tex:5487:compute/tests/test_pixton_genus3_shadow_engine.py:claimed=None:collected=97:returncode=0
chapters/examples/kac_moody.tex:4507:compute/tests/test_non_simply_laced_shadows.py:claimed=168:collected=168:returncode=0
chapters/examples/bar_complex_tables.tex:2609:compute/tests/test_exceptional_shadows.py:claimed=None:collected=178:returncode=0
codex
The count sweep is running under `pytest --collect-only`. After that I’ll read the clusters with live counts first, because those are the highest-probability places where surrounding statements drifted after engine/test churn.

thinking
**Inspecting test mismatches**

I'm noticing a mismatch: the document w_algebras.tex mentions 105 tests for w3_genus2, but the actual number is 125. I think I need to check the actual values around w3_genus2, not just the count. It makes sense to compare the chapter's claims with engine outputs, especially around line 5768. There may be additional tests due to modifications, leading to this drift. I could parse mentions of `(\d+ tests)` and systematically compare counts for accuracy. Let's figure out a comprehensive approach!
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib, re, subprocess, sys
entries=[]
for path in sorted(pathlib.Path('chapters/examples').glob('*.tex')):
    for i,line in enumerate(path.read_text().splitlines(),1):
        tests = re.findall(r'(test_[A-Za-z0-9_]+\\.py)', line)
        m = re.search(r'\\"'$?([0-9]+)'"\\"'$?~?tests'"', line)
        if tests and m:
            entries.append((str(path), i, tests, int(m.group(1)), line.strip()))
for tex, line_no, tests, claimed, raw in entries:
    for t in tests:
        # prefer exact compute/tests path if it exists
        candidates = list(pathlib.Path('compute/tests').glob(t))
        if not candidates:
            print(f'{tex}:{line_no}:{t}:claimed={claimed}:missing')
            continue
        test_path = str(candidates[0])
        p = subprocess.run(['pytest','--collect-only','-q',test_path],capture_output=True,text=True)
        out = p.stdout + p.stderr
        m = re.search(r'([0-9]+) tests? collected', out)
        count = int(m.group(1)) if m else None
        status = 'MATCH' if count == claimed else 'MISMATCH'
        print(f'{tex}:{line_no}:{test_path}:claimed={claimed}:collected={count}:{status}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:


thinking
**Inspecting code libraries**

I think the libraries I'm looking at are probably designed for seam checks, but it's important not to trust them blindly. I need to read through them and run some targeted tests. There may also be tests necessary for chapter rectification engines to identify any live mismatches. I'm planning to inspect several specific files, including landscape_census_verification.py and others related to chapter rectification, since these could reveal mismatches in the user’s scope. I'll open the relevant files now.
codex
I’m switching from metadata drift to substantive seam checks. There are dedicated audit engines in `compute/lib/` that already encode suspected chapter/engine mismatches; I’m reading those next and only keeping findings that still match the live `.tex` surface.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_yangian_consistency_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_w_algebra_chapter_rectification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/landscape_census_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_km_chapter_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Full landscape census verification engine.

Independently recomputes EVERY numerical entry in the landscape census
(chapters/examples/landscape_census.tex) and flags any discrepancy.

Tables verified:
  1. tab:master-invariants — c, c+c', kappa for all families
  2. tab:shadow-tower-census — archetype class, r_max
  3. tab:free-energy-landscape — F_1, F_2, kappa at specific k/c
  4. tab:shadow-invariants-landscape — S_3, S_4, Delta, rho, kappa+kappa'
  5. tab:rmatrix-census — r-matrix pole structure

Anti-pattern coverage:
  AP1  — kappa formulas recomputed from first principles per family
  AP5  — cross-family consistency checks
  AP9  — explicit qualifiers for every kappa
  AP10 — cross-check tests, not single-family hardcodes
  AP24 — complementarity sum NOT assumed zero
  AP39 — S_2 vs kappa explicitly distinguished
  AP48 — kappa != c/2 for general VOAs
 succeeded in 51ms:
r"""Theorem engine: W-algebra chapter rectification against Creutzig-Linshaw 2024-2026.

Deep Beilinson audit of w_algebras.tex against the full Creutzig-Linshaw output:
    [2403.08212] Type A successive hook-type reductions (JJM 2025)
    [2512.19508] New universal VAs as glueings
    [2508.18889] W-algebras as conformal extensions of affine VOAs
    [2506.15605] Minimal W(so_N) at level -1 (Arakawa-Moreau)
    [2409.03465] Building blocks for types B,C,D (W^sp_infty)
    [2411.11383] Logarithmic Verlinde formula
    [2508.18248] Butson-Nair inverse Hamiltonian reduction ALL type A

FINDING REGISTER:

F1 (CRITICAL): Bershadsky-Polyakov central charge formula WRONG.
    Location: w_algebras.tex:7044,7083; landscape_census.tex:134;
              subregular_hook_frontier.tex:908-970;
              compute/lib/bershadsky_polyakov_bar.py:15;
              compute/lib/sl3_subregular_bar.py; compute/lib/ds_nonprincipal_shadows.py
    Claim: c(BP, k) = 1 - 18/(k+3) = (k-15)/(k+3)
    Correct: c(BP, k) = 2 - 24(k+1)^2/(k+3) [Fehily-Kawasetsu-Ridout 2020]
 succeeded in 51ms:
r"""KM chapter rectification engine: deep verification across all level regimes.

CHAPTER TARGET: kac_moody.tex (chap:kac-moody-koszul)

RECTIFICATION SCOPE
===================

This engine verifies the KM chapter against five recent papers:

[GR24a]  Gaitsgory-Raskin, Proof of the geometric Langlands conjecture I,
         arXiv:2405.03599, 2024.
[GR24b]  Gaitsgory-Raskin, Proof of the geometric Langlands conjecture II,
         arXiv:2405.03648, 2024.
[Cre24]  Creutzig, Ribbon categories for admissible affine vertex algebras,
         arXiv:2411.11386, 2024.
[CDN26]  Creutzig-Dhillon-Nakatsuka, Braided tensor categories of W-algebras
         at irrational levels, arXiv:2603.04667, 2026.
[LQ26]   Linshaw-Qi, Deformation rigidity of vertex algebras at integral levels,
         arXiv:2601.12017, 2026.

 succeeded in 51ms:
r"""Yangian cross-chapter consistency engine.

Narrow verification layer for NOTATION and CONVENTION consistency between
two Yangian chapters in Vol I:

    chapters/examples/yangians_foundations.tex
    chapters/examples/yangians_drinfeld_kohno.tex

Scope (intentionally narrow; complements existing engines without duplication):

 1. Modular characteristic kappa: verify numerical agreement for sl_n
    between the E_infty convention kappa(g_k) = dim(g)(k+h^vee)/(2h^vee)
    (invoked in yangians_foundations.tex) and the E_1 Yangian test value
    kappa^{E_1}(Y(sl_2)) = hbar when specialised at k=1 and hbar=1.

 2. Yang R-matrix R(u) = 1 - hbar P / u (as declared in both chapters):
    - P^2 = I (permutation involutivity),
    - unitarity R(u) R(-u) = rational scalar times identity on fundamental,
    - crossing symmetry at the simple-pole residue.


thinking
**Verifying landscape functions**

I think I need to run tests for landscape verification to check for exact comparisons. It might be useful to look into mismatch counts in that engine or tests. I wonder if there's a function that verifies chapter table entries, so I should inspect that more closely. Running a search for any `FAIL` results could help me identify any issues that might exist. Let's get into this and see what I find!
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_sca_kappa_fix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_theorem_sca_kappa_fix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "def .*verify|return .*VerificationResult|FAILED|discrep|mismatch|assert|expected|wrong|rectification" compute/lib/landscape_census_verification.py compute/tests/test_landscape_census_verification.py compute/lib/theorem_sca_kappa_fix_engine.py compute/tests/test_theorem_sca_kappa_fix_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Tests for the superconformal algebra kappa fix engine.

AP49 cross-volume verification: N=2 SCA and N=4 small SCA kappa formulas.

Multi-path verification (AP mandate: >= 3 independent paths per claim):
  - Direct formula evaluation
  - Coset decomposition
  - Complementarity sum constancy
  - Limiting cases (k=0, k=1, k->inf)
  - Cross-family consistency
  - Comparison with Vol I authoritative values
  - Comparison with existing compute engines
  - AP48 violation detection (kappa != c/2)

Target: >= 30 tests.
"""

import pytest
from fractions import Fraction

 succeeded in 51ms:
r"""Superconformal algebra kappa verification engine.

AP49 CROSS-VOLUME FIX: Two errors in Vol II examples-worked.tex corrected.

ERROR 1 (CRITICAL): N=2 SCA kappa
  Vol I (w_algebras_deep.tex line 4913): kappa = (6-c)/(2(3-c)) = (k+4)/4.
  Vol II (examples-worked.tex line 4037): INCORRECTLY had kappa = c/2.
  At c=1: Vol I gives 5/4, Vol II gave 1/2 -- factor 5/2 discrepancy.
  FIX APPLIED: Vol II updated to match Vol I formula.

  The correct formula follows from the Kazama-Suzuki coset decomposition:
    N=2 SCA at c = 3k/(k+2) = Commutant(U(1), sl(2)_k x complex_fermion)
    kappa(N=2) = kappa(sl(2)_k) + kappa(fermion) - kappa(U(1))
              = 3(k+2)/4 + 1/2 - (k/2 + 1) = (k+4)/4

ERROR 2 (SERIOUS): N=4 small SCA
  Vol I TABLE (w_algebras_deep.tex line 3328): INCORRECTLY had c -> 12-c,
    self-dual c=6, kappa+kappa'=0.
  Vol II (examples-worked.tex line 4219): had c -> -c-24, self-dual c=-12
    (CORRECT for FF involution with c=6k), but kappa = c/2 (WRONG).
 succeeded in 51ms:
compute/lib/theorem_sca_kappa_fix_engine.py:8:  At c=1: Vol I gives 5/4, Vol II gave 1/2 -- factor 5/2 discrepancy.
compute/lib/theorem_sca_kappa_fix_engine.py:294:# 5. Cross-volume discrepancy verification
compute/lib/theorem_sca_kappa_fix_engine.py:297:def verify_n2_ap49_discrepancy() -> Dict[str, object]:
compute/lib/theorem_sca_kappa_fix_engine.py:298:    """Verify the N=2 SCA AP49 cross-volume discrepancy.
compute/lib/theorem_sca_kappa_fix_engine.py:302:      Vol II (was wrong): kappa = c/2 = 1/2
compute/lib/theorem_sca_kappa_fix_engine.py:310:    wrong = c / 2  # 1/2
compute/lib/theorem_sca_kappa_fix_engine.py:314:        'wrong_kappa': wrong,
compute/lib/theorem_sca_kappa_fix_engine.py:315:        'discrepancy_ratio': correct / wrong,
compute/lib/theorem_sca_kappa_fix_engine.py:316:        'is_discrepant': correct != wrong,
compute/lib/theorem_sca_kappa_fix_engine.py:320:def verify_n4_ap49_discrepancy() -> Dict[str, object]:
compute/lib/theorem_sca_kappa_fix_engine.py:321:    """Verify the N=4 small SCA AP49 cross-volume discrepancy.
compute/lib/theorem_sca_kappa_fix_engine.py:325:      Vol II (was wrong): kappa = c/2 = 3
compute/lib/theorem_sca_kappa_fix_engine.py:329:      Vol I table (was wrong): c -> 12-c
compute/lib/theorem_sca_kappa_fix_engine.py:333:    wrong = c / 2  # 3
compute/lib/theorem_sca_kappa_fix_engine.py:337:        'wrong_kappa_vol2': wrong,
compute/lib/theorem_sca_kappa_fix_engine.py:339:        'wrong_dual_c': 12 - c,
compute/lib/theorem_sca_kappa_fix_engine.py:390:    wrong = c / 2
compute/lib/theorem_sca_kappa_fix_engine.py:398:        'wrong_virasoro': wrong,
compute/lib/theorem_sca_kappa_fix_engine.py:399:        'not_virasoro': path1 != wrong,
compute/tests/test_theorem_sca_kappa_fix_engine.py:45:    verify_n2_ap49_discrepancy,
codex
I’m using the audit engines only as hypotheses. Next step is hostile re-read of the live chapter lines they point at; if the `.tex` is already corrected, the finding dies. If not, it survives with the exact line and patch.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '4898,4935p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '3288,3360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3048,3095p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '7000,7105p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4898	The first factor is $M(q)/(1-q)^{-1} \cdot (1-q)^{-1}
  4899	= M(q) \cdot (1-q)^{-1} \cdot \prod_{n \geq 2}(1-q^n)^{-1}$
  4900	; but more directly,
  4901	\[
  4902	 \prod_{n \geq 2}(1-q^n)^{-(n-1)}
  4903	 = \frac{\prod_{n \geq 1}(1-q^n)^{-n}}
  4904	 {\prod_{n \geq 1}(1-q^n)^{-1}}
  4905	 \cdot (1-q)^{-1+1}
  4906	 = \frac{M(q)}{\prod_{n \geq 1}(1-q^n)^{-1}}
  4907	 \cdot \frac{1}{1-q}
  4908	 \cdot (1-q)
  4909	\]
  4910	which simplifies to $M(q) \cdot \varphi(q)/(1-q)$, as claimed.
  4911	\end{proof}
  4912	
  4913	\begin{proposition}[$\Walg_\infty$ bar-window series and Koszul
  4914	entropy]\label{prop:winfty-bar-window}
  4915	\ClaimStatusProvedHere
  4916	\index{W-algebras@$\mathcal{W}$-algebras!W-infinity@$\mathcal{W}_\infty$!bar-window series}
  4917	\index{W-algebras@$\mathcal{W}$-algebras!W-infinity@$\mathcal{W}_\infty$!Koszul entropy}
 succeeded in 52ms:
  3288	is $k$-independent for \emph{all} partitions $\lambda \vdash N$,
  3289	equal to $\varrho_\lambda \cdot K_\lambda$ where
  3290	$\varrho_\lambda$ is the anomaly ratio and $K_\lambda = c(\lambda,k)
  3291	+ c(\lambda^t, k^\vee)$ is the $k$-independent Koszul conductor
  3292	(Proposition~\textup{\ref{prop:partition-dependent-complementarity}(iii)}).
  3293	\end{proposition}
  3294	
  3295	\begin{proof}
  3296	For~(i): the partition $(4,2) \vdash 6$ has distinct parts, so
  3297	$\mathfrak{n}_+$ is abelian by
  3298	Proposition~\ref{prop:abelian-locus-type-a}. Its transpose is
  3299	$(2,2,1,1) \neq (4,2)$. The KRW central charge formulas for
  3300	$\mathcal{W}_k(\mathfrak{sl}_6, f_{(4,2)})$ and
  3301	$\mathcal{W}_{-k-12}(\mathfrak{sl}_6, f_{(2,2,1,1)})$ involve
  3302	distinct Sugawara-type denominators $k + 6$ and $-k - 6$ whose
  3303	rational functions in~$k$ do not cancel in the sum, leaving
  3304	a $k$-dependent residue.
  3305	
  3306	For~(ii): the partition $(2^3) \vdash 6$ has repeated parts
  3307	(Dynkin label $d_2 = 3$), so $\mathfrak{n}_+$ is non-abelian by
 succeeded in 52ms:
  7000	combinatorial explosion of the ordered Miura product
  7001	$\prod_{j=0}^{n-1} u_j$. Thus the principal and subregular families
  7002	represent two qualitatively different mechanisms for generating
  7003	homotopy complexity: compositional nonlinearity (principal) versus
  7004	combinatorial depth of the screening resolution (subregular). The
  7005	former is conjecturally bounded by the number of generators; the
  7006	latter grows with the rank regardless of the generator count.
  7007	\end{remark}
  7008	
  7009	\begin{remark}[Geometric meaning]
  7010	\label{rem:w-subregular-geometric-meaning}
  7011	The PBW filtration is controlled by Slodowy slices and their
  7012	arc spaces. The homotopy degree is controlled by the failure of the
  7013	quantized slice to remain quadratic after one chooses a strong
  7014	generating set and performs chiral normal ordering. In the
  7015	Bershadsky--Polyakov case ($n = 3$), the Slodowy slice is
  7016	$\mathfrak{sl}_3^{e_{\mathrm{subreg}}}$, which is two-dimensional,
  7017	and the normal ordering produces only quadratic corrections. For
  7018	$n \ge 4$, the slice dimension grows and the screening-mediated
  7019	normal-ordering corrections introduce genuinely new cubic, quartic,
 succeeded in 52ms:
  3048	follows from the exactness of $H^0_{\mathrm{DS}}$ and the
  3049	fact that DS sends surjections to surjections.
  3050	
  3051	Part (iii): by Theorem~\ref{thm:ds-koszul-intertwine}, the
  3052	bar complexes are compatible: $\bar{B}_W(\mathcal{L}^W(\lambda))
  3053	\simeq H^0_{\mathrm{DS}}(\bar{B}(\mathcal{L}(\lambda)))$.
  3054	The Ext groups are computed by the bar complex
  3055	(Proposition~\ref{prop:logarithmic-bar}), so the isomorphism
  3056	follows from the quasi-isomorphism of bar complexes.
  3057	\end{proof}
  3058	
  3059	\begin{example}[Logarithmic Virasoro modules at \texorpdfstring{$c = 25$}{c=25}]
  3060	\label{ex:log-virasoro}
  3061	\index{Virasoro algebra!logarithmic modules}
  3062	At the Ising model value $c = 1/2$ ($k = -2 + 4/3$,
  3063	$p = 4$, $q = 3$ for $\mathfrak{sl}_2$), the Koszul dual
  3064	central charge is $c' = 51/2 = 25\tfrac{1}{2}$. The
  3065	$\mathrm{Vir}_{c'}$ algebra is non-rational at $c' > 25$:
  3066	the module category is non-semisimple.
  3067	


thinking
**Investigating test independence**

I’m thinking it might be helpful to search through compute/tests for lines where expected values come from the engine's private constants or formulas, especially indicating AP128. I need to ensure users check that there's no AP128 if the engine/test is using the same wrong model. I'll keep an eye out for tests relying on engine internals instead of independent expectations. If a chapter relies on test counts to justify compute backing, that could be a seam issue. Plus, I might need to check test files that are referenced by chapters.
thinking
**Inspecting suspicious test patterns**

I'm considering checking specific test files that could show suspicious patterns, like `compute/tests/test_w3_genus2.py` and several others. I need to inspect them for imports of engine constants or repetitive use of the same formulas. It might be useful to search these files for private/internal imports or shared functions. I think running a search across these cited tests for keywords like `_KNOWN` and internal helper imports could shed light on any issues.
codex
I’m now checking the oracle quality of the cited tests. A seam claim is not actually verified if the test just reuses the engine’s own constants or formulas; that’s the AP128 failure mode the user called out explicitly.
exec
/bin/zsh -lc "sed -n '1,220p' compute/tests/test_theorem_w3_holographic_datum_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/tests/test_w3_genus2.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Tests for the complete holographic modular Koszul datum H(T) for W_3.

THEOREM (Holographic Modular Koszul Datum for W_3):
The six-fold package H(T) = (A, A!, C, r(z), Theta_A, nabla^hol) for the
W_3 algebra is the first rank-2 example with genuinely multi-weight structure.

MULTI-PATH VERIFICATION (3+ per claim, per CLAUDE.md mandate):

Every numerical value is verified by at least 3 independent paths.
Cross-family consistency (AP10) verified against Virasoro and sl_2_hat.

ANTI-PATTERN AWARENESS:
    AP1:  kappa(W_3) = 5c/6, NOT c/2. Independently recomputed.
    AP10: Cross-family consistency checks, not just hardcoded values.
    AP19: r-matrix poles one below OPE poles.
    AP24: kappa + kappa' = 250/3 != 0 for W_3.
    AP27: bar propagator weight 1 for all channels.
    AP29: self-dual c* = 50 != critical c_crit = 100.
    AP32: genus-1 universal, genus-2 FAILS for multi-weight.
    AP39: kappa != c/2. kappa = 5c/6.
 succeeded in 51ms:
r"""Tests for the W₃ genus-2 free energy computation.

Verifies the multi-channel genus-2 graph sum for the W₃ algebra,
the first explicit computation for a multi-generator chiral algebra.

Test structure:
    1. Foundational data: λ_g^FP, κ values, OPE structure constants
    2. Graph topology: stability, genus, automorphism counts
    3. Per-graph amplitudes: analytic vs numerical for all 7 stable graphs
    4. Cross-channel correction: the multi-generator signal δF₂ = (c+204)/(16c)
    5. Planted-forest formula: δ_pf = S₃(10S₃ - κ)/48
    6. Single-channel limit: F₂ → κ·λ₂^FP when W decouples
    7. Koszul duality: constraints at c ↔ 100-c
    8. Physical consistency: positivity, linearity, large-c behavior
    9. Numerical spot-checks at c = 4 (free boson pair) and c = 50 (large c)

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    eq:delta-pf-genus2-explicit, rem:propagator-weight-universality
"""
exec
/bin/zsh -lc 'for f in compute/tests/test_ds_cascade_shadows.py compute/tests/test_higher_w_shadows.py compute/tests/test_virasoro_shadow_extended.py compute/tests/test_w3_shadow_extended.py compute/tests/test_w3_genus2.py compute/tests/test_theorem_w3_holographic_datum_engine.py compute/tests/test_non_simply_laced_shadows.py compute/tests/test_exceptional_shadows.py compute/tests/test_theorem_dk0_evaluation_bridge_engine.py compute/tests/test_yangian_rtt_all_types.py compute/tests/test_betagamma_shadow_full.py compute/tests/test_betagamma_quartic_contact.py compute/tests/test_theorem_class_l_generating_function_engine.py; do echo "FILE $f"; rg -n "from compute'"\\.lib\\.|import .* as|_KNOWN|_DATA|expected *= .*\\(|expected *= .*\\bfrom\\b|private|internal|helper|formula|same formula|cross-engine|VERIFIED\" \""'$f"; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE compute/tests/test_ds_cascade_shadows.py
11:  Section 1: Central charge formulas and additivity (18 tests)
12:  Section 2: Kappa formulas — affine and W_N (19 tests)
31:from compute.lib.ds_cascade_shadows import (
64:# Section 1: Central charge formulas and additivity
68:    """Test c(sl_N, k) and c(W_N, k) formulas for N = 2..6."""
88:        # VERIFIED: [DC] FL formula; [LT] canonical_c_wn_fl self-test on import
93:        # VERIFIED: [DC] FL formula; [LC] N=2 gives -7 (Vir check)
98:        # VERIFIED: [DC] FL formula; [LC] N=2 gives -7, N=3 gives -52
103:        # VERIFIED: [DC] FL formula; [CF] complementarity c+c' = 2*5+4*6*35 = 850
118:        With the Fateev-Lukyanov formula, the ghost central charge
121:        # VERIFIED: [DC] tautological by definition of c_ghost(N, k)
128:        """With FL formula, ghost central charge c_ghost(N, k) is k-DEPENDENT.
130:        The old simple formula gave c_ghost = N(N-1) (constant).
131:        The correct FL formula gives c_ghost that varies with k.
133:        # VERIFIED: [DC] c_ghost(2,1) = 1-(-7) = 8 != c_ghost(2,5) = 15/7-(-209/7) = 32
150:# Section 2: Kappa formulas
154:    """Test kappa formulas for affine sl_N and W_N."""
169:        """The correct formula has 2N in denominator, NOT 2.
172:        This tests AP1: the user's original formula was wrong by factor N.

thinking
**Inspections on outdated engine**

I’m noticing that there may be an issue with outdated line numbers in the engine documentation. The user is interested in compute engines related to the manuscript seam, so it seems that the outdated docstrings might cause confusion. I think it's more valuable to find the mismatched formulas instead. Let’s look into the n2 section of w_algebras_deep and toroidal_elliptic or n2_superconformal and search for kappa formulas to address these gaps.
codex
The current signal is mixed: most cited tests exist and many formulas are internally consistent, so I’m looking for the remaining high-value seam failures now, especially places where a compute audit engine still points at chapter claims or line numbers that no longer match the live manuscript.
exec
/bin/zsh -lc "sed -n '900,980p' compute/lib/theorem_cross_volume_ap49_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\kappa.*N=2|N=2.*\\\\kappa|\\(k\\+4\\)/4|\\(6-c\\)/\\(2\\(3-c\\)\\)|c/3|c/2|self-dual c=-12|self-dual c=6|12-c|-c-24\" chapters/examples/w_algebras_deep.tex chapters/examples/n2_superconformal.tex chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"AP49|w_algebras_deep\\.tex line|Vol I.*w_algebras_deep|Vol I table|line 4913|line 3328|theorem_cross_volume_ap49_engine|examples-worked\" compute/lib/theorem_sca_kappa_fix_engine.py compute/lib/theorem_cross_volume_ap49_engine.py" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\kappa.*N=2|N=2.*\kappa|\(k\+4\)/4|\(6-c\)/\(2\(3-c\)\)|c/3|c/2|self-dual c=-12|self-dual c=6|12-c|-c-24)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:

    # Heisenberg k=1: kappa = 1
    k_heis = kappa_heisenberg(Fraction(1))
    results['Heis_k1'] = {
        'kappa': k_heis,
        'expected': Fraction(1),
        'method1_direct': k_heis == 1,
        'method2_complement': kappa_heisenberg(Fraction(1)) + kappa_heisenberg(Fraction(-1)) == 0,
        'method3_F1': F_g_formula(k_heis, 1) == Fraction(1, 24),
    }

    return results


def kappa_n2_sca(c: Fraction) -> Fraction:
    """kappa(N=2 SCA) = (6-c)/(2(3-c)).

    Vol I (w_algebras_deep.tex line 4913): kappa = (k+4)/4 = (6-c)/(2(3-c)).
    PROVED by three independent routes (Kazama-Suzuki coset, DS of sl(2|1),
    spectral flow).
 succeeded in 52ms:
compute/lib/theorem_sca_kappa_fix_engine.py:3:AP49 CROSS-VOLUME FIX: Two errors in Vol II examples-worked.tex corrected.
compute/lib/theorem_sca_kappa_fix_engine.py:6:  Vol I (w_algebras_deep.tex line 4913): kappa = (6-c)/(2(3-c)) = (k+4)/4.
compute/lib/theorem_sca_kappa_fix_engine.py:7:  Vol II (examples-worked.tex line 4037): INCORRECTLY had kappa = c/2.
compute/lib/theorem_sca_kappa_fix_engine.py:17:  Vol I TABLE (w_algebras_deep.tex line 3328): INCORRECTLY had c -> 12-c,
compute/lib/theorem_sca_kappa_fix_engine.py:19:  Vol II (examples-worked.tex line 4219): had c -> -c-24, self-dual c=-12
compute/lib/theorem_sca_kappa_fix_engine.py:22:    Vol I table corrected to c -> -c-24, self-dual c=-12, kappa+kappa'=-8.
compute/lib/theorem_sca_kappa_fix_engine.py:35:  Vol I: w_algebras_deep.tex, toroidal_elliptic.tex
compute/lib/theorem_sca_kappa_fix_engine.py:36:  Vol II: examples-worked.tex
compute/lib/theorem_sca_kappa_fix_engine.py:38:           theorem_cross_volume_ap49_engine.py
compute/lib/theorem_sca_kappa_fix_engine.py:89:    AP49: This is NOT c/2. The naive Virasoro formula fails
compute/lib/theorem_sca_kappa_fix_engine.py:298:    """Verify the N=2 SCA AP49 cross-volume discrepancy.
compute/lib/theorem_sca_kappa_fix_engine.py:321:    """Verify the N=4 small SCA AP49 cross-volume discrepancy.
compute/lib/theorem_sca_kappa_fix_engine.py:329:      Vol I table (was wrong): c -> 12-c
compute/lib/theorem_cross_volume_ap49_engine.py:1:"""Cross-volume AP49 formula verification engine.
compute/lib/theorem_cross_volume_ap49_engine.py:3:AP49: Cross-volume formula propagation without convention check.
compute/lib/theorem_cross_volume_ap49_engine.py:53:    Vol I (genus_expansion.py, w_algebras_deep.tex): kappa = c/2.
compute/lib/theorem_cross_volume_ap49_engine.py:54:    Vol II (examples-worked.tex line 4735): kappa(Vir_c) = c/2.
compute/lib/theorem_cross_volume_ap49_engine.py:65:    Vol I (w_algebras_deep.tex line 2201): kappa(V_k) = (k+h^v)*dim(g)/(2h^v).
compute/lib/theorem_cross_volume_ap49_engine.py:66:    Vol II (examples-worked.tex line 1295): kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v).
compute/lib/theorem_cross_volume_ap49_engine.py:75:    Vol I (w_algebras_deep.tex line 3790): kappa = c*(H_N - 1).
exec
/bin/zsh -lc "rg -n \"small N=4|N=4 small|kappa\\(small N=4|c/3|c/2|self-dual.*-12|-c-24|12-c\" chapters/examples/w_algebras_deep.tex chapters/examples/toroidal_elliptic.tex chapters/examples/n2_superconformal.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '1650,1705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '3745,3825p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/n2_superconformal.tex:98:$(c/2)/z^3 + 2T/z$ from the Virasoro subalgebra and a simple
chapters/examples/n2_superconformal.tex:99:pole $(c/3)/z$ from the $\mathrm{U}(1)$ current~$J$.
chapters/examples/n2_superconformal.tex:309:$G^+_{(2)}G^- = c/3$
chapters/examples/n2_superconformal.tex:421:\index{N=4 small superconformal}
chapters/examples/n2_superconformal.tex:431: c & c/2 & 26{-}c & 13 & c = 13 \\
chapters/examples/toroidal_elliptic.tex:1714: Virasoro formula $\kappa = c/2$ for each $\cN = 2$ factor.
chapters/examples/toroidal_elliptic.tex:1734:stress tensor for each $c = 3/2$ factor, giving $\kappa = c/2 = 3/4$
chapters/examples/toroidal_elliptic.tex:1742:\begin{remark}[$\kappa(K3) = 2 \neq c/2 = 3$: modular characteristic vs central charge]
chapters/examples/toroidal_elliptic.tex:1747:Virasoro formula $c/2 = 3$. The reduction arises because the
chapters/examples/toroidal_elliptic.tex:1985:q^{L_0 - c/24}\,\bar{y}^{J_0}\,(-1)^{F+\bar{F}}\bigr)$ is a
chapters/examples/toroidal_elliptic.tex:4126:\textup{(}this is not $c/2$ in general; here the central charge is
chapters/examples/toroidal_elliptic.tex:4127:$c = 2 \cdot 3 = 6$, and $c/2 = 3$ coincides with $\kappa$
chapters/examples/toroidal_elliptic.tex:4404:($\kappa = c/2$ in all r\^oles) but diverge for
chapters/examples/w_algebras_deep.tex:500:$A_1$ (Vir) & $T$ & $4$ & $1$ ($m_0 = c/2$) & $26$ \\
chapters/examples/w_algebras_deep.tex:501:$A_2$ ($\mathcal{W}_3$) & $T, W$ & $4, 6$ & $2$ ($c/2$, $c/3$) & $100$ \\
chapters/examples/w_algebras_deep.tex:502:$B_2$ ($\mathcal{W}(B_2)$) & $T, W^{(4)}$ & $4, 8$ & $2$ ($c/2$, $c/4$) &
chapters/examples/w_algebras_deep.tex:504:$G_2$ ($\mathcal{W}(G_2)$) & $T, W^{(6)}$ & $4, 12$ & $2$ ($c/2$, $c/6$) &
chapters/examples/w_algebras_deep.tex:678:$2$ & $c/2$ \\
chapters/examples/w_algebras_deep.tex:732:$2$ & $c/3$ \\
chapters/examples/w_algebras_deep.tex:779:$\sqrt{Q_W} = (2c/3)(1 + 12u)^{1/2}$
 succeeded in 51ms:
  1650	\begin{tabular}{llcl}
  1651	\textbf{Generator} & \textbf{Weight $h$} & \textbf{Parity}
  1652	 & $J^3$ \textbf{charge} \\
  1653	\hline
  1654	$T$ & $2$ & bosonic & $0$ \\
  1655	$G^+, G^-$ & $3/2$ & fermionic & $\pm 1/2$ \\
  1656	$\tilde{G}^+, \tilde{G}^-$ & $3/2$ & fermionic & $\mp 1/2$ \\
  1657	$J^{++}, J^{--}$ & $1$ & bosonic & $\pm 1$ \\
  1658	$J^3$ & $1$ & bosonic & $0$
  1659	\end{tabular}
  1660	\end{center}
  1661	The OPE structure at $c = 6$, $k_R = 1$:
  1662	\begin{align}
  1663	T(z)\,T(w) &\sim \frac{3}{(z-w)^4} + \frac{2T}{(z-w)^2}
  1664	 + \frac{\partial T}{z-w}, \label{eq:n4-TT} \\
  1665	J^3(z)\,J^3(w) &\sim \frac{1/2}{(z-w)^2}, \label{eq:n4-J3J3} \\
  1666	J^{++}(z)\,J^{--}(w) &\sim \frac{1}{(z-w)^2}
  1667	 + \frac{2J^3}{z-w}, \label{eq:n4-JppJmm} \\
  1668	G^+(z)\,G^-(w) &\sim \frac{2}{(z-w)^3} + \frac{2J^3}{(z-w)^2}
  1669	 + \frac{T + \partial J^3}{z-w}. \label{eq:n4-GpGm}
 succeeded in 51ms:
  3745	 non-principal nilpotent $f$, where the DS BRST complex has
  3746	 a different ghost structure.
  3747	\item \emph{Tensor products}: K\"unneth gives
  3748	 $\dim H^2_{\mathrm{cyc}}(\mathcal{A} \otimes \mathcal{B}) = \dim H^2_{\mathrm{cyc}}(\mathcal{A}) + \dim H^2_{\mathrm{cyc}}(\mathcal{B})$,
  3749	 but the channels decouple (no genuine mixed coupling).
  3750	\item \emph{The $\mathcal{W}_\infty$ tower as an $E_1$-algebra}:
  3751	 the inverse system $\{\mathcal{W}_N\}_N$ viewed as an $E_1$-algebra
  3752	 in pro-vertex-algebras may carry deformation directions from
  3753	 the tower structure maps, even though each individual stage
  3754	 has $\dim H^2_{\mathrm{cyc}} = 1$.
  3755	\end{enumerate}
  3756	\end{remark}
  3757	
  3758	\begin{remark}[Shadow obstruction tower classification: the $\mathcal{W}$-algebra position]
  3759	\label{rem:w-algebra-shadow-position}
  3760	\index{shadow obstruction tower!W-algebra position@$\mathcal{W}$-algebra position}
  3761	The one-dimensional cyclic-line theorem places
  3762	$\mathcal{W}_\infty$ in a precise position within the shadow obstruction tower
  3763	classification of the landscape
  3764	(Table~\ref{tab:master-invariants}). Among the standard families:
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '3588,3612p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_cross_volume_ap49_engine.py | sed -n '930,1035p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\(small N=4\\)|c/3|not c/2|self-dual c=-12|-c-24|kappa\\+kappa'=-8\" chapters/examples/toroidal_elliptic.tex chapters/examples/n2_superconformal.tex chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3588	$\kappa' = 2(-k-4) = -2k - 8$.
  3589	
  3590	\textbf{Caution}: for the K3 sigma model
  3591	($c = 6$, $k = 1$), the geometric Verdier duality
  3592	gives $\kappa' = -\kappa = -2$ and
  3593	$\kappa + \kappa' = 0$; this is the CY sigma-model
  3594	duality $k \mapsto -k$ (not the FF involution
  3595	$k \mapsto -k - 4$) and applies only to the
  3596	geometric realization.
  3597	
  3598	The self-dual central charges $c = 13,\,15/2,\,3,\,-12$
  3599	are the points where bar-cobar duality acts trivially
  3600	on the modular characteristic.
  3601	For $N = 0$: $\kappa(\mathrm{Vir}_{13}) = 13/2$
  3602	.
  3603	For $N = 1$: $\kappa(\SVir_{15/2}) = 41/8$.
  3604	For $N = 2$: $\kappa(\text{SCA}_3) = 1/2$.
  3605	For $N = 4$: $\kappa(\text{small}_{c=6}) = 2$
  3606	($= c/3$, not $c/2$).
  3607	\end{remark}
 succeeded in 51ms:
chapters/examples/n2_superconformal.tex:99:pole $(c/3)/z$ from the $\mathrm{U}(1)$ current~$J$.
chapters/examples/n2_superconformal.tex:309:$G^+_{(2)}G^- = c/3$
chapters/examples/w_algebras_deep.tex:501:$A_2$ ($\mathcal{W}_3$) & $T, W$ & $4, 6$ & $2$ ($c/2$, $c/3$) & $100$ \\
chapters/examples/w_algebras_deep.tex:732:$2$ & $c/3$ \\
chapters/examples/w_algebras_deep.tex:779:$\sqrt{Q_W} = (2c/3)(1 + 12u)^{1/2}$
chapters/examples/w_algebras_deep.tex:797:$\kappa(\mathcal{W}_3) = \kappa_T + \kappa_W = c/2 + c/3 = 5c/6$.
chapters/examples/w_algebras_deep.tex:835: $\tilde{\kappa}_N = (c/2, c/3, \ldots, c/N)$ diverges as
chapters/examples/w_algebras_deep.tex:914:\operatorname{diag}(c/2,\, c/3,\, \ldots,\, c/N)$
chapters/examples/w_algebras_deep.tex:1926:$W$-curvature & $m_0^{(W)} = c/3$ &
chapters/examples/w_algebras_deep.tex:3606:($= c/3$, not $c/2$).
chapters/examples/w_algebras_deep.tex:4058:$\Walg_3$ & $11/6$ & $5/6$ & $5c/6$ & $(c/2,\, c/3)$ & $250/3$ \\
chapters/examples/w_algebras_deep.tex:4059:$\Walg_4$ & $25/12$ & $13/12$ & $13c/12$ & $(c/2,\, c/3,\, c/4)$
chapters/examples/w_algebras_deep.tex:4062: & $(c/2,\, c/3,\, c/4,\, c/5)$ & $(77/60)\cdot K_5$ \\
chapters/examples/w_algebras_deep.tex:4310:= c/2 + c/3 + c/4 = 13c/12$.
chapters/examples/w_algebras_deep.tex:4333:$\kappa_3 = c/3$, $\alpha_3 = 0$,
chapters/examples/w_algebras_deep.tex:4355:$\kappa(\Walg_5) = c/2 + c/3 + c/4 + c/5 = 77c/60$.
chapters/examples/w_algebras_deep.tex:5300:$J$-line \textup{(Heisenberg)} & $c/3$ & $0$ & $0$ & $0$ & G \\
chapters/examples/w_algebras_deep.tex:5314:The $J$-channel: $J_{(1)}J = c/3$ (the $U(1)$ level), giving
chapters/examples/w_algebras_deep.tex:5315:$\kappa_J = c/3$, and $J_{(0)}J = 0$ (abelian), so $\alpha_J = 0$
chapters/examples/w_algebras_deep.tex:5338:$Q_J = (2\kappa_J)^2 = (2c/3)^2 = 4c^2/9$. At degree~$2$ the
 succeeded in 52ms:
   930	    return (6 - c) / (2 * (3 - c))
   931	
   932	
   933	def verify_superconformal_kappa() -> Dict[str, object]:
   934	    """Verify superconformal kappa values from Vol I w_algebras_deep.tex.
   935	
   936	    N=0 (Virasoro): kappa = c/2, self-dual at c=13.
   937	    N=1 (SVir): kappa = (3c-2)/4.
   938	    N=2 (SCA): kappa = (6-c)/(2(3-c)) (NOT c/2; AP49 discrepancy).
   939	    N=4 (small N=4): kappa = c/2.
   940	
   941	    Vol I (w_algebras_deep.tex lines 3293-3355, 4910-4984).
   942	    Vol II (examples-worked.tex lines 4037-4213).
   943	    """
   944	    results = {}
   945	
   946	    # N=0: Virasoro
   947	    c = Fraction(13)
   948	    k_vir = kappa_virasoro(c)
   949	    results['N0_Vir'] = {

thinking
**Examining algebra consistency**

I’m noticing some interesting inconsistencies in the definitions related to N=2 self-dual cases. The w_algebras_deep mentions kappa as 1/2 at c=3, but the theorem_sca_kappa_fix_engine contradicts this by stating there's a pole at that point. So, I'm questioning whether there's an actual inconsistency between those lines. It seems I need to dig into the context around lines 3560 to 3607 to clarify these formulas — perhaps the N=2 SCA formula differs in this chapter.
codex
A real seam break just surfaced: the compute engine for the corrected superconformal formulas says `N=2` has a pole at `c=3`, but the live chapter currently records a finite self-dual value `κ(SCA_3)=1/2`. I’m reading the full local context before I keep it, because if the chapter is mixing two conventions I need the exact narrower fix, not a vague contradiction.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '3548,3608p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\text\\{SCA\\}_3|kappa\\(\\\\text\\{SCA\\}|kappa\\(SCA|N = 2|6-c|3-c|Kazama|spectral flow|pole at c=3|free-field limit\" chapters/examples/w_algebras_deep.tex chapters/examples/n2_superconformal.tex compute/lib/theorem_sca_kappa_fix_engine.py compute/tests/test_theorem_sca_kappa_fix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3548	\label{rem:superconformal-complementarity-hierarchy}
  3549	\index{complementarity sum!superconformal hierarchy|textbf}
  3550	\index{superconformal algebra!complementarity hierarchy}
  3551	\index{kappa@$\kappa$!superconformal complementarity}
  3552	The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$
  3553	is a monotone decreasing function of the number of
  3554	supersymmetries, forming a strict hierarchy:
  3555	\begin{center}
  3556	\small
  3557	\renewcommand{\arraystretch}{1.25}
  3558	\begin{tabular}{@{}lcccc@{}}
  3559	\toprule
  3560	\emph{Algebra} & \emph{Duality} & \emph{Self-dual}
  3561	 & $\kappa + \kappa'$ & \emph{Type} \\
  3562	\midrule
  3563	$N=0$: $\mathrm{Vir}_c$ & $c \mapsto 26 - c$ & $c = 13$
  3564	 & $13$ & W-type \\
  3565	$N=1$: $\SVir_c$ & $c \mapsto 15 - c$ & $c = 15/2$
  3566	 & $41/4$ & W-type \\
  3567	$N=2$: SCA & $c \mapsto 6 - c$ & $c = 3$
 succeeded in 51ms:
compute/tests/test_theorem_sca_kappa_fix_engine.py:51:# N=2 SCA: kappa = (6-c)/(2(3-c)) = (k+4)/4
compute/tests/test_theorem_sca_kappa_fix_engine.py:80:        """kappa has a pole at c=3 (free-field limit k->inf)."""
compute/tests/test_theorem_sca_kappa_fix_engine.py:103:        """(6-c)/(2(3-c)) = (k+4)/4 for corresponding k, c."""
compute/tests/test_theorem_sca_kappa_fix_engine.py:112:    """Verify kappa via the Kazama-Suzuki coset decomposition."""
compute/tests/test_theorem_sca_kappa_fix_engine.py:138:    """Verify kappa(c) + kappa(6-c) = 1."""
compute/tests/test_theorem_sca_kappa_fix_engine.py:157:        """c -> 6-c is an involution: (6-(6-c)) = c."""
compute/lib/theorem_sca_kappa_fix_engine.py:6:  Vol I (w_algebras_deep.tex line 4913): kappa = (6-c)/(2(3-c)) = (k+4)/4.
compute/lib/theorem_sca_kappa_fix_engine.py:11:  The correct formula follows from the Kazama-Suzuki coset decomposition:
compute/lib/theorem_sca_kappa_fix_engine.py:54:    The N=2 SCA is realized as the Kazama-Suzuki coset
compute/lib/theorem_sca_kappa_fix_engine.py:63:    Solving: c(k+2) = 3k => ck + 2c = 3k => k(3-c) = 2c => k = 2c/(3-c).
compute/lib/theorem_sca_kappa_fix_engine.py:64:    Pole at c = 3 (the free-field limit k -> infinity).
compute/lib/theorem_sca_kappa_fix_engine.py:67:        raise ValueError("c = 3 is the free-field limit (k -> infinity)")
compute/lib/theorem_sca_kappa_fix_engine.py:74:    Derived from Kazama-Suzuki coset decomposition:
compute/lib/theorem_sca_kappa_fix_engine.py:84:    """kappa(N=2 SCA) = (6-c)/(2(3-c)), in terms of central charge.
compute/lib/theorem_sca_kappa_fix_engine.py:86:    Equivalently (k+4)/4 with k = 2c/(3-c).
compute/lib/theorem_sca_kappa_fix_engine.py:87:    Pole at c = 3 (free-field limit).
compute/lib/theorem_sca_kappa_fix_engine.py:94:        raise ValueError("c = 3 is the free-field limit (pole of kappa)")
compute/lib/theorem_sca_kappa_fix_engine.py:132:    """kappa(c) + kappa(6-c) = 1 (constant, W-type).
compute/lib/theorem_sca_kappa_fix_engine.py:134:    PROOF: (6-c)/(2(3-c)) + c/(2(c-3))
compute/lib/theorem_sca_kappa_fix_engine.py:135:         = (6-c)/(2(3-c)) - c/(2(3-c))
exec
/bin/zsh -lc 'pytest -q compute/tests/test_theorem_sca_kappa_fix_engine.py -q' in /Users/raeez/chiral-bar-cobar succeeded in 561ms:
.......................................                                  [100%]

thinking
**Identifying manuscript inconsistencies**

I’ve spotted a direct contradiction within the manuscript itself. In `w_algebras_deep.tex`, lines 5163+ say the N=2 formula has a pole at c=3, but earlier in line 3604, it states that kappa(SCA_3)=1/2. This is definitely an internal inconsistency. I need to revise line 3604 to clarify it as "pole (free-field limit)" or something similar. This is a significant finding, and I should consider categorizing it as HIGH/CRITICAL since it inaccurately represents numerical information. I’ll need to inspect lines 5163-5240 for the correct quote.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '5158,5240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_sca_kappa_fix_engine.py | sed -n '80,145p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5158	
  5159	\begin{theorem}[$N=2$ modular characteristic; \ClaimStatusProvedHere]%
  5160	\label{thm:n2-kappa}
  5161	\index{kappa@$\kappa$!N=2 superconformal@$N=2$ superconformal}
  5162	\index{N=2 superconformal algebra@$N=2$ superconformal algebra!kappa}
  5163	The modular characteristic of the $N = 2$ SCA at central charge
  5164	$c = 3k/(k+2)$ is
  5165	\begin{equation}\label{eq:n2-kappa}
  5166	\kappa(N{=}2) \;=\; \frac{k+4}{4} \;=\; \frac{6-c}{2(3-c)}.
  5167	\end{equation}
  5168	This is established by three independent routes:
  5169	\begin{enumerate}[label=\textup{(\roman*)}]
  5170	\item \emph{Kazama--Suzuki coset decomposition:}
  5171	$\kappa(N{=}2) = \kappa(\mathfrak{sl}_{2,k}) + \kappa(\text{fermion})
  5172	- \kappa(U(1)) = \tfrac{3(k+2)}{4} + \tfrac{1}{2}
  5173	- (\tfrac{k}{2}+1) = \tfrac{k+4}{4}$.
  5174	\item \emph{DS reduction of $\mathfrak{sl}(2|1)$:}
  5175	The Kazama--Suzuki coset is isomorphic to the DS reduction
  5176	of $\mathfrak{sl}(2|1)_k$; the $\kappa$ computation via the
  5177	superalgebra realization gives the same result.
 succeeded in 52ms:
    80	    return (k + 4) / 4
    81	
    82	
    83	def kappa_n2_from_c(c: Fraction) -> Fraction:
    84	    """kappa(N=2 SCA) = (6-c)/(2(3-c)), in terms of central charge.
    85	
    86	    Equivalently (k+4)/4 with k = 2c/(3-c).
    87	    Pole at c = 3 (free-field limit).
    88	
    89	    AP49: This is NOT c/2. The naive Virasoro formula fails
    90	    because the N=2 SCA is a coset, and the coset subtraction
    91	    reduces kappa below the Virasoro value c/2.
    92	    """
    93	    if c == 3:
    94	        raise ValueError("c = 3 is the free-field limit (pole of kappa)")
    95	    return (6 - c) / (2 * (3 - c))
    96	
    97	
    98	def kappa_n2_coset_decomposition(k: Fraction) -> Dict[str, Fraction]:
    99	    """Explicit coset decomposition of kappa(N=2).
codex
I have one live contradiction locked: `w_algebras_deep.tex` contradicts its own later theorem and the compute test suite on the `N=2` self-dual point. I’m now checking whether the older AP49 engine is still publishing the obsolete superconformal formulas without any test catching it.
exec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_theorem_cross_volume_ap49_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files compute/tests | rg 'theorem_cross_volume_ap49_engine|cross_volume_ap49'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""Cross-volume AP49 formula verification tests.

Exhaustive verification that every shared formula between Vol I and Vol II
agrees after accounting for convention differences.

Categories tested:
  (a) kappa formulas for all families (AP1, AP39, AP48)
  (b) F_g = kappa * lambda_g^FP convention (AP22, AP38)
  (c) Complementarity sums kappa + kappa' (AP24)
  (d) Q^contact quartic invariant (AP44)
  (e) Shadow depth classification G/L/C/M (AP14)
  (f) Bar differential grading conventions (AP45)
  (g) R-matrix pole structure (AP19)

Each formula is verified by 3+ independent methods.
"""

import pytest
from fractions import Fraction

 succeeded in 51ms:
compute/tests/test_theorem_cross_volume_ap49_engine.py
exec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.theorem_cross_volume_ap49_engine import verify_superconformal_kappa
print(verify_superconformal_kappa())
PY" in /Users/raeez/chiral-bar-cobar succeeded in 177ms:
{'N0_Vir': {'kappa': Fraction(13, 2), 'expected': Fraction(13, 2), 'match': True}, 'N1_SVir': {'kappa': Fraction(41, 8), 'expected': Fraction(41, 8), 'match': True}, 'N2_SCA': {'kappa': Fraction(5, 4), 'expected': Fraction(5, 4), 'match': True}, 'N2_complementarity': {'sum': Fraction(1, 1), 'expected': Fraction(1, 1), 'match': True}, 'N2_AP49_discrepancy': {'vol1_correct': Fraction(5, 4), 'vol2_incorrect': Fraction(1, 2), 'discrepancy': True, 'match': True}, 'N4_small_AP49': {'vol1_complementarity_sum': Fraction(0, 1), 'vol1_self_dual_c': 6, 'vol2_claims_kappa': 'c/2', 'vol2_self_dual_c': -12, 'convention_mismatch': True, 'match': True}, 'N0_comp_sum': {'sum': Fraction(13, 1), 'match': True}, 'N1_comp_sum': {'kappa': Fraction(41, 8), 'kappa_dual': Fraction(41, 8), 'sum': Fraction(41, 4), 'expected': Fraction(41, 4)}}

thinking
**Evaluating test file imports**

I'm looking at the test file and noting that it imports verify_superconformal_kappa, but I’m wondering if it actually tests the N4 details adequately. There's a possibility that it might be missing crucial aspects. So, I think a quick search to clarify whether those details are covered in the tests could be really helpful. Ensuring thorough testing is key here! Let's dig into that and see what we can find.
exec
/bin/zsh -lc 'rg -n "verify_superconformal_kappa|N4_small_AP49|N2_AP49|superconformal" compute/tests/test_theorem_cross_volume_ap49_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
72:    verify_superconformal_kappa,
533:        r = verify_superconformal_kappa()
538:        r = verify_superconformal_kappa()
543:        r = verify_superconformal_kappa()
548:        r = verify_superconformal_kappa()
553:        r = verify_superconformal_kappa()
554:        assert r['N2_AP49_discrepancy']['discrepancy'], \
559:        r = verify_superconformal_kappa()
560:        assert r['N4_small_AP49']['convention_mismatch']
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_cross_volume_ap49_engine.py | sed -n '520,565p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   520	
   521	    def test_heis_k1(self):
   522	        r = verify_specific_kappa_values()
   523	        v = r['Heis_k1']
   524	        assert v['method1_direct']
   525	        assert v['method2_complement']
   526	        assert v['method3_F1']
   527	
   528	
   529	class TestSuperconformal:
   530	    """Superconformal kappa values across volumes."""
   531	
   532	    def test_n0_virasoro(self):
   533	        r = verify_superconformal_kappa()
   534	        assert r['N0_Vir']['match']
   535	
   536	    def test_n1_svir(self):
   537	        """SVir: kappa = (3c-2)/4, self-dual at c = 15/2."""
   538	        r = verify_superconformal_kappa()
   539	        assert r['N1_SVir']['match']


thinking
**Evaluating findings for accuracy**

I’m looking into some findings from the stale line numbers in the theorem_sca_kappa_fix_engine docstring. It seems like there's potential to combine low-severity notes and gather more findings. I want to search for contradictions across chapters and compute on various clusters. For instance, one cluster mentions a test count of 105, but the actual count is 125. I see low documentation drift between certain formulas and references, so I should identify more substantial mismatches in the compute and manuscript. I might use a verification script to ensure everything runs smoothly.
thinking
**Investigating count mismatches**

I'm noticing another issue related to count mismatches in w_algebras.tex, and I think there might be more out there. I really need to improve the systematic count parser to help identify these better. We already know about one mismatch, but I’ll check the other chapter lines for counts and tests. I want to verify counts for cited tests like in w_algebras.tex at certain lines. It seems there might be discrepancies with tests collected in certain files. I need to investigate some specific files and ensure all counts match correctly.
codex
I’m doing one more mechanical sweep for stale oracle counts. This catches quiet seam drift where the chapter still advertises a specific engine/test payload but the underlying test surface has changed.
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re,subprocess
texs=sorted(pathlib.Path('chapters/examples').glob('*.tex'))
pat_file=re.compile(r'([A-Za-z0-9_/.-]+\\.py)')
pat_count=re.compile(r'(\\d+)\\s*~?\\\\?tests|\\((\\d+) tests')
for tex in texs:
    for i,line in enumerate(tex.read_text().splitlines(),1):
        files=pat_file.findall(line)
        m=pat_count.search(line)
        if not files or not m:
            continue
        claimed=int(next(g for g in m.groups() if g))
        for ref in files:
            ref_path=pathlib.Path(ref)
            candidates=[]
            if ref_path.exists():
                if 'compute/tests/' in ref:
                    candidates=[ref]
                elif 'compute/lib/' in ref:
                    stem=ref_path.stem
                    tp=pathlib.Path('compute/tests')/f'test_{stem}.py'
                    if tp.exists():
                        candidates=[str(tp)]
                else:
                    # bare file: prefer exact test file, else test_ stem
                    tp=pathlib.Path('compute/tests')/ref_path.name
                    if tp.exists(): candidates=[str(tp)]
                    else:
                        tp2=pathlib.Path('compute/tests')/f'test_{ref_path.stem}.py'
                        if tp2.exists(): candidates=[str(tp2)]
            else:
                # resolve bare names
                tp=pathlib.Path('compute/tests')/ref_path.name
                if tp.exists(): candidates=[str(tp)]
                else:
                    tp2=pathlib.Path('compute/tests')/f'test_{ref_path.stem}.py'
                    if tp2.exists(): candidates=[str(tp2)]
                    lp=pathlib.Path('compute/lib')/ref_path.name
                    if lp.exists():
                        tp3=pathlib.Path('compute/tests')/f'test_{lp.stem}.py'
                        if tp3.exists(): candidates=[str(tp3)]
            for cand in candidates:
                p=subprocess.run(['pytest','--collect-only','-q',cand],capture_output=True,text=True)
                out=p.stdout+p.stderr
                mm=re.search(r'(\\d+) tests? collected',out)
                cnt=int(mm.group(1)) if mm else None
                status='MATCH' if cnt==claimed else 'MISMATCH'
                print(f'{tex}:{i}:{ref}:claimed={claimed}:test={cand}:collected={cnt}:{status}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 724ms:
chapters/examples/w3_holographic_datum.tex:5:compute/lib/theorem_w3_holographic_datum_engine.py:claimed=83:test=compute/tests/test_theorem_w3_holographic_datum_engine.py:collected=83:MATCH



thinking
**Exploring formula verification**

I found that the script only identified one result due to regex limitations. I think I should manually inspect the count claims from grep, but I feel like I might still need more findings. Using the `landscape_census_verification` engine to compare line counts and formulas sounds like a solid plan.

I could also run `pytest` and check if it passes, as that might indicate if there's any mismatch, but I should keep an eye out for other areas that might not be covered. I'll search for direct contradictions in the chapters related to formulas against the compute engine functions.
thinking
**Identifying internal inconsistencies**

I think I've found something interesting in `w_algebras_deep.tex` at line 3605. It mentions, "For N=4: κ(small_{c=6}) = 2," but it feels inconsistent because it talks about self-dual central charges including -12 while using c=6 instead. 

At the self-dual point, it should be κ(small_{-12}) = -4 instead. I’ll need to verify the context, as it appears there are two errors in this remark about N=2 and N=4. I should definitely confirm this with the compute engine and the theorem!
thinking
**Reviewing audit documentation**

I could mention that the severity is low because the engine deals with audit documentation. I need to fix the line references and use current labels like `thm:n2-kappa`, `prop:n2-koszul-duality`, and `rem:superconformal-complementarity-hierarchy` instead of outdated ones. There's also line 17 referring to "Vol I TABLE," but I found the actual N4 data at line 3567. The user wants an exact fix for every finding, so I might need to check another stale line count, `w_algebras.tex:5768`, for discrepancies.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5758,5776p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  5758	$C_{TTW} = C_{WWW} = 0$ by $\mathbb{Z}_2$~parity, so only
  5759	the $T$-channel contributes to the $s$-channel factorization:
  5760	$\eta^{TT} C_{iiT} C_{jjT} = (2/c) \cdot c \cdot c = 2c$.
  5761	
  5762	\smallskip\noindent\emph{Planted-forest correction.}
  5763	The $W$-channel planted-forest correction
  5764	$\delta_{\mathrm{pf}}^W = 0$ because $S_3^W = 0$ ($\mathbb{Z}_2$~parity).
  5765	The $T$-channel correction $\delta_{\mathrm{pf}}^T = (40{-}c)/48$
  5766	(Remark~\ref{rem:higher-degree-explicit}).
  5767	
  5768	\textup{(}\texttt{test\_w3\_genus2.py}, $105$~tests.\textup{)}
  5769	\end{computation}
  5770	
  5771	%% ================================================================
  5772	\section{The \texorpdfstring{$N\!=\!1$}{N=1} super-Virasoro PVA and 3d supergravity}
  5773	\label{sec:super-virasoro-pva}
  5774	\index{super-Virasoro algebra!PVA}
  5775	\index{supergravity!3d holomorphic-topological}
  5776	
exec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_w3_genus2.py | tail -n 2' in /Users/raeez/chiral-bar-cobar succeeded in 262ms:

125 tests collected in 0.10s
exec
/bin/zsh -lc "nl -ba compute/tests/test_w3_genus2.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Tests for the W₃ genus-2 free energy computation.
     2	
     3	Verifies the multi-channel genus-2 graph sum for the W₃ algebra,
     4	the first explicit computation for a multi-generator chiral algebra.
     5	
     6	Test structure:
     7	    1. Foundational data: λ_g^FP, κ values, OPE structure constants
     8	    2. Graph topology: stability, genus, automorphism counts
     9	    3. Per-graph amplitudes: analytic vs numerical for all 7 stable graphs
    10	    4. Cross-channel correction: the multi-generator signal δF₂ = (c+204)/(16c)
    11	    5. Planted-forest formula: δ_pf = S₃(10S₃ - κ)/48
    12	    6. Single-channel limit: F₂ → κ·λ₂^FP when W decouples
    13	    7. Koszul duality: constraints at c ↔ 100-c
    14	    8. Physical consistency: positivity, linearity, large-c behavior
    15	    9. Numerical spot-checks at c = 4 (free boson pair) and c = 50 (large c)
    16	
    17	Manuscript references:
    18	    thm:theorem-d, op:multi-generator-universality,
    19	    eq:delta-pf-genus2-explicit, rem:propagator-weight-universality
    20	"""
codex
The `W₃` genus-2 chapter also has a concrete count drift. I’m checking whether its cited test file is a real oracle or just the engine re-testing itself through the same functions, because that would be the exact AP128 failure mode on a headline computation.
exec
/bin/zsh -lc "rg -n \"def graph_total_amplitude|def analytic_fig_eight|def analytic_banana|def analytic_dumbbell|def analytic_theta|def analytic_lollipop|return analytic_|graph_total_amplitude\\(|analytic_\" compute/lib/w3_genus2.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/w3_genus2.py | sed -n '150,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_w3_genus2.py | sed -n '270,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
484:def graph_total_amplitude(graph_idx: int, c: Fraction) -> Dict[str, Fraction]:
523:def analytic_fig_eight(c_val: Fraction) -> Dict[str, Fraction]:
545:def analytic_banana(c_val: Fraction) -> Dict[str, Fraction]:
564:def analytic_dumbbell(c_val: Fraction) -> Dict[str, Fraction]:
585:def analytic_theta(c_val: Fraction) -> Dict[str, Fraction]:
612:def analytic_lollipop(c_val: Fraction) -> Dict[str, Fraction]:
775:        r = graph_total_amplitude(idx, c_val)
911:        r = graph_total_amplitude(idx, c_val)
1011:    r1 = graph_total_amplitude(1, c_val)
1012:    a1 = analytic_fig_eight(c_val)
1015:        'analytic_total': a1['total'],
1022:    r2 = graph_total_amplitude(2, c_val)
1023:    a2 = analytic_banana(c_val)
1031:    r3 = graph_total_amplitude(3, c_val)
1032:    a3 = analytic_dumbbell(c_val)
1039:    r4 = graph_total_amplitude(4, c_val)
1040:    a4 = analytic_theta(c_val)
1048:    r5 = graph_total_amplitude(5, c_val)
1049:    a5 = analytic_lollipop(c_val)
 succeeded in 52ms:
   270	        for c in C_VALUES:
   271	            for ch1 in ['T', 'W']:
   272	                for ch2 in ['T', 'W']:
   273	                    V = V04_s_channel(ch1, ch1, ch2, ch2, c)
   274	                    self.assertEqual(V, 2 * c,
   275	                                     f"V₀₄({ch1}{ch1}{ch2}{ch2}) != 2c at c={c}")
   276	
   277	
   278	class TestGraphAmplitudes(unittest.TestCase):
   279	    """Verify individual graph amplitudes against analytic formulas."""
   280	
   281	    def test_fig_eight_per_channel(self):
   282	        """Γ₁: A^T = 1/48, A^W = 1/48. Total = 1/24."""
   283	        for c in C_VALUES:
   284	            r = graph_total_amplitude(1, c)
   285	            self.assertEqual(r['all_T'], Fraction(1, 48))
   286	            self.assertEqual(r['all_W'], Fraction(1, 48))
   287	            self.assertEqual(r['total'], Fraction(1, 24))
   288	
   289	    def test_fig_eight_no_mixed(self):
 succeeded in 52ms:
   150	    g=3: 31/967680
   151	    """
   152	    if g < 1:
   153	        raise ValueError(f"λ_g^FP requires g ≥ 1, got {g}")
   154	    B2g = _bernoulli(2 * g)
   155	    abs_B2g = abs(B2g)
   156	    return Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1)) * abs_B2g / Fraction(factorial(2 * g))
   157	
   158	
   159	# ============================================================================
   160	# W₃ curvature data (OPE-derived, AP1/AP9 verified)
   161	# ============================================================================
   162	
   163	def kappa_T(c: Fraction) -> Fraction:
   164	    """Per-channel κ for T (Virasoro): κ_T = c/2.
   165	
   166	    Derivation: T_{(3)}T = c/2 (leading OPE pole).
   167	    The bar-complex metric η_{TT} = c/2.
   168	    """
   169	    return c / 2

thinking
**Inspecting graph functions**

I need to check if graph_total_amplitude is calling the analytic functions internally. I think I should look around line 484 or so to see if there's anything relevant there. It seems like a good idea to verify this, as it might help clarify how the whole thing operates. I really want to make sure I understand the connections properly. So, let’s dig into the code around that area for a closer look!
exec
/bin/zsh -lc "nl -ba compute/lib/w3_genus2.py | sed -n '468,670p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   468	    channels_at_v = _half_edge_channels_at_vertex(graph_idx, sigma)
   469	    vertex_product = Fraction(1)
   470	    for v_idx, (gv, nv) in enumerate(G['vertices']):
   471	        he_channels = channels_at_v[v_idx]
   472	        if gv == 0:
   473	            vertex_product *= genus0_vertex_factor(he_channels, c)
   474	        elif gv == 1:
   475	            vertex_product *= genus1_vertex_factor(he_channels, c)
   476	        elif gv == 2:
   477	            pass  # smooth part handled separately
   478	        else:
   479	            raise ValueError(f"Unsupported vertex genus {gv}")
   480	
   481	    return prop_product * vertex_product
   482	
   483	
   484	def graph_total_amplitude(graph_idx: int, c: Fraction) -> Dict[str, Fraction]:
   485	    """Total amplitude of graph Γ summed over all channel assignments.
   486	
   487	    Returns dict with 'all_T', 'all_W', 'mixed', 'total' components.
codex
I have the high-signal formula failures. I’m checking a few remaining count-backed chapter claims to see whether they’re just cosmetic drift or whether there are more stale oracle references worth reporting.
exec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_e1_lattice_bar.py | tail -n 2' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_theorem_class_l_generating_function_engine.py | tail -n 2' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_koszul_dual_dims.py | tail -n 2' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_wild_quiver_chiral_engine.py | tail -n 2' in /Users/raeez/chiral-bar-cobar succeeded in 614ms:

45 tests collected in 0.29s
 succeeded in 602ms:

27/28 tests collected (1 deselected) in 0.29s
 succeeded in 619ms:

89 tests collected in 0.29s
 succeeded in 625ms:

70 tests collected in 0.30s

thinking
**Identifying inconsistencies in documentation**

I see the chapter line mentions 458 compute tests but only names two files, which feels mismatched. I need to correct it by either changing the number from 458 to 346 or by ensuring that all three test files are cited accurately to reflect the total. I should also consider checking the count for `test_exceptional_shadow_complete.py` to clarify things. This needs attention to make everything consistent!
codex
One more count-backed seam looks wrong: `bar_complex_tables.tex` credits 458 tests to two specific files, but the two named files only collect 178 and 168 tests. I’m checking whether a third file was omitted before I keep that finding.
exec
/bin/zsh -lc "nl -ba chapters/examples/bar_complex_tables.tex | sed -n '2604,2614p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_non_simply_laced_shadows.py | tail -n 2' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_exceptional_shadow_complete.py | tail -n 2' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pytest --collect-only -q compute/tests/test_exceptional_shadows.py | tail -n 2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2604	\index{shadow obstruction tower!non-simply-laced types}
  2605	\index{E6@$E_6$!shadow data}
  2606	\index{E7@$E_7$!shadow data}
  2607	\index{F4@$F_4$!shadow data}
  2608	
  2609	The following table collects the shadow obstruction tower data for all exceptional ($E_6, E_7, E_8$) and non-simply-laced ($B_2, G_2, F_4$) affine Kac--Moody algebras. Every family is class L (shadow depth $r_{\max} = 3$), with cubic shadow $C$ from the Lie bracket, quartic shadow $S_4 = 0$ by the Jacobi identity, and critical discriminant $\Delta = 8\kappa S_4 = 0$. The r-matrix has a simple pole at $z = 0$ ($d\log$ extraction absorbs one power), and complementarity $\kappa + \kappa' = 0$ holds for all Kac--Moody families. All data verified by 458 compute tests (\texttt{test\_exceptional\_shadows.py}, \texttt{test\_non\_simply\_laced\_shadows.py}).
  2610	\begin{center}
  2611	\renewcommand{\arraystretch}{1.3}
  2612	\begin{tabular}{lcccccccl}
  2613	\toprule
  2614	$\mathfrak{g}$ & $d$ & $r$ & $h$ & $h^\vee$ & $r^\vee$ & $\kappa(\widehat{\mathfrak{g}}_k)$ & $c + c'$ & Class \\
 succeeded in 649ms:

178 tests collected in 0.31s
 succeeded in 654ms:

168 tests collected in 0.30s
 succeeded in 663ms:

307 tests collected in 0.31s

thinking
**Identifying verification files**

I’m figuring out if I need an exact fix of either 346 or if I should mention the third file as 653. The chapter specifies data for exceptional cases. This might include `test_exceptional_shadow_complete.py`, but I’m checking which files cover the data. I want to inspect the docstring of `test_exceptional_shadow_complete.py` to see if it covers exceptional cases, and I wonder if `test_exceptional_shadows.py` might duplicate that. I’ll confirm the combinations to identify errors.
exec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_exceptional_shadow_complete.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_non_simply_laced_shadows.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_exceptional_shadows.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Tests for exceptional simply-laced shadow obstruction tower data: E_6, E_7, E_8.

Verifies:
    1. Structural data (dim, rank, h, h^v, exponents) cross-checked against lie_algebra.py
    2. Exponent identities: sum(m_i) = rank*h/2, max(m_i) = h-1
    3. Kappa formula: kappa = dim(g)*(k+h^v)/(2*h^v) at multiple levels
    4. Shadow archetype: class L (alpha != 0, Delta = 0, r_max = 3)
    5. r-matrix: simple pole, modified CYBE from Jacobi
    6. Complementarity: kappa(g,k) + kappa(g,k') = 0 at multiple levels
    7. Central charge complementarity: c(g,k) + c(g,k') = 2*dim(g)
    8. Anomaly ratio: rho(g) = sum 1/(m_i+1) exact values
    9. W-algebra central charge via FKW / Strange Formula
   10. W-algebra kappa = rho * c identity
   11. Cross-family consistency (E6 vs E7 vs E8)
   12. Strange Formula: |rho|^2 = dim*h/12
   13. Positive root count from Cartan matrix
   14. Comparison with A-series
   15. Numeric evaluations at distinguished levels (k=1,2,5)

Mathematical references:
 succeeded in 52ms:
r"""Tests for complete exceptional shadow obstruction tower: G_2, F_4, E_6, E_7, E_8.

Verifies ALL shadow obstruction tower invariants for ALL five exceptional Lie types
from first principles (AP1, AP10).  Every expected value is independently
computed in the test, NOT imported from the library under test.

Test categories:
    1. Structural data (dim, rank, h, h^v, exponents, lacing) -- 5 types
    2. Kappa formula: kappa = dim(g)*(k+h^v)/(2*h^v) at multiple levels
    3. Shadow class L: S_3 != 0, S_4 = 0, Delta = 0, r_max = 3
    4. Complementarity: kappa + kappa' = 0, c + c' = 2*dim
    5. Feigin-Frenkel involution: (k')' = k, fixed at k = -h^vee
    6. Central charge: c = dim*k/(k+h^v), large-k limit = dim
    7. Casimir degrees: degrees = exponents + 1, no cubic Casimir
    8. Root system: num_roots, dim = 2*n_pos + rank, exponent sum
    9. Anomaly ratio: rho(g) = sum 1/(m_i+1) exact values
   10. Strange Formula: |rho|^2 = dim*h/12
   11. W-algebra: kappa(W) = rho * c(W) at multiple levels
   12. Genus amplitudes: F_1 = kappa/24, F_2^scalar = 7*kappa/5760
   13. E_8 theta function: leading coefficient = 240 = E_4 coefficient
 succeeded in 52ms:
"""Tests for non-simply-laced shadow obstruction tower data: B_2, C_2, G_2, F_4.

Verifies all shadow obstruction tower formulas from first principles (AP1).
Every expected value is independently computed in the test, NOT imported
from the library under test (AP10).

Test categories:
    1. Kappa formulas (primary definition, verified against dim(g)*(k+h^v)/(2*h^v))
    2. Shadow class L assignment (S_3 != 0, S_4 = 0, Delta = 0, r_max = 3)
    3. r-matrix structure (simple pole)
    4. Complementarity (kappa + kappa' = 0 for all KM)
    5. Feigin-Frenkel involution properties
    6. Central charge formulas
    7. Cross-family consistency (B2=C2 isomorphism, additivity)
    8. Numerical spot-checks at specific levels
    9. h vs h^vee distinction
"""

import pytest
from sympy import Rational, Symbol, simplify, cancel, S
codex
The AP49 engine/test pair is looking like a genuine stale-oracle problem, not just a bad comment. I’m running the specific test block now to confirm that the suite still passes while encoding the obsolete `N=4` narrative.
exec
/bin/zsh -lc 'pytest -q compute/tests/test_theorem_cross_volume_ap49_engine.py -k superconformal -q' in /Users/raeez/chiral-bar-cobar succeeded in 548ms:
......                                                                   [100%]
exec
/bin/zsh -lc "nl -ba compute/lib/theorem_sca_kappa_fix_engine.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Superconformal algebra kappa verification engine.
     2	
     3	AP49 CROSS-VOLUME FIX: Two errors in Vol II examples-worked.tex corrected.
     4	
     5	ERROR 1 (CRITICAL): N=2 SCA kappa
     6	  Vol I (w_algebras_deep.tex line 4913): kappa = (6-c)/(2(3-c)) = (k+4)/4.
     7	  Vol II (examples-worked.tex line 4037): INCORRECTLY had kappa = c/2.
     8	  At c=1: Vol I gives 5/4, Vol II gave 1/2 -- factor 5/2 discrepancy.
     9	  FIX APPLIED: Vol II updated to match Vol I formula.
    10	
    11	  The correct formula follows from the Kazama-Suzuki coset decomposition:
    12	    N=2 SCA at c = 3k/(k+2) = Commutant(U(1), sl(2)_k x complex_fermion)
    13	    kappa(N=2) = kappa(sl(2)_k) + kappa(fermion) - kappa(U(1))
    14	              = 3(k+2)/4 + 1/2 - (k/2 + 1) = (k+4)/4
    15	
    16	ERROR 2 (SERIOUS): N=4 small SCA
    17	  Vol I TABLE (w_algebras_deep.tex line 3328): INCORRECTLY had c -> 12-c,
    18	    self-dual c=6, kappa+kappa'=0.
    19	  Vol II (examples-worked.tex line 4219): had c -> -c-24, self-dual c=-12
    20	    (CORRECT for FF involution with c=6k), but kappa = c/2 (WRONG).





thinking
**Investigating code references**

I might address fixing the code by using labels or current line-free references. I’m noting that there are stale line references in the compute/lib/theorem_cross_volume_ap49_engine.py file. I could integrate this with the findings related to 3 or 7. Now, I also need to ensure the `bar_complex_tables` line has named tests and counts right. After checking, it seems I don’t need to worry about combined counts from other tests after deselection.
thinking
**Considering file references**

I’m thinking about how to reference the issue if it spans multiple lines. Maybe it’s best to use something like “file:3598” while also mentioning the lines, like 3598-3606, in prose. I want to ensure I'm providing the exact fix requested, so using a specific file and line reference seems like a good idea. It might be the clearest way to communicate the needed correction.
thinking
**Considering possible issues**

I’m thinking about whether there could be any other issues in `bar_complex_tables.tex` or the counts in `w_algebras.tex`. It seems like they’re not of high severity, which is a relief. I want to make sure I’m thorough in my evaluation to keep everything accurate and up to spec. If there are any discrepancies, I should address those as well. I'm curious if I need to look deeper into the specifics here.
thinking
**Finalizing report format**

I’m considering using markdown file links, but I want to keep the formatting consistent. I need to decide if "Checked: N" means the number of seam clusters or files, and maybe setting N to 18 based on the files read sounds good. I'm leaning towards counting the seam clusters verified instead of lines. It's crucial to be honest about what I've actually checked, so I’ll make sure we include the counts accurately.
thinking
**Organizing findings clearly**

I want to make sure that the first two findings aren’t overlapping too much. I might think about combining findings N2 and N4 into one critical finding at line 3598 since they share the same paragraph summary. But since the user asked for every finding, it’s probably better to keep them separate. I need to mention the exact fix text for N2 and N4 to avoid confusion. Let’s craft this carefully!
codex
- [CRITICAL] chapters/examples/w_algebras_deep.tex:3598 — PROBLEM: This summary says the self-dual central charges are the points where duality acts trivially on `\kappa`, then line 3604 states `\kappa(\text{SCA}_3)=1/2`. That contradicts the proved formula later in the same file at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5166) and [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5225), and the compute oracle at [compute/lib/theorem_sca_kappa_fix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sca_kappa_fix_engine.py:83), all of which give `\kappa(N=2)=(6-c)/(2(3-c))` with a simple pole at `c=3`. FIX: rewrite the sentence so `c=3` is only the self-dual point of the central-charge involution, not a finite fixed point of `\kappa`; replace `For N = 2: \kappa(\text{SCA}_3) = 1/2.` with `For N = 2: c=3 is the free-field limit, and \kappa has a simple pole there.`

- [HIGH] chapters/examples/w_algebras_deep.tex:3605 — PROBLEM: The `N=4` item in the same self-dual-point list uses the K3 value `\kappa(\text{small}_{c=6})=2`, not the self-dual value for the duality just stated two lines above (`c=-12`). The live chapter itself says `c=-12` is self-dual at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3569), and the corrected compute formula is `\kappa=c/3`, so the self-dual value is `-4`, not `2`. FIX: replace `For N = 4: \kappa(\text{small}_{c=6}) = 2 (= c/3, not c/2).` with `For N = 4: \kappa(\text{small}_{c=-12}) = -4 (= c/3, not c/2).` Leave the `c=6` K3 example only in the cautionary paragraph at lines 3590-3596.

- [HIGH] compute/lib/theorem_cross_volume_ap49_engine.py:933 — PROBLEM: `verify_superconformal_kappa()` still encodes the obsolete Vol I `N=4` story: the docstring says `\kappa=c/2` at line 939, and the returned `N4_small_AP49` block hardcodes `vol1_complementarity_sum = 0` and `vol1_self_dual_c = 6` at lines 998-1012. That no longer matches the live manuscript at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3569) and [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3606), which now gives self-dual `c=-12`, `\kappa=c/3`, and `\kappa+\kappa'=-8`. FIX: replace the `N=4` branch with the corrected Vol I data, ideally by importing `kappa_n4_from_c`, `n4_koszul_dual_c`, and `n4_complementarity_sum_ff` from [compute/lib/theorem_sca_kappa_fix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sca_kappa_fix_engine.py:145); the result should report `self_dual_c = -12`, `kappa_self_dual = -4`, and `ff_complementarity_sum = -8`, not a generic “convention mismatch.”

- [HIGH] compute/tests/test_theorem_cross_volume_ap49_engine.py:557 — PROBLEM: The `N=4` AP49 test is a stale oracle. It only asserts `r['N4_small_AP49']['convention_mismatch']`, so `pytest -q compute/tests/test_theorem_cross_volume_ap49_engine.py -k superconformal` passes even while the engine contradicts the current Vol I chapter. This is the exact AP128 failure mode: the test validates a hardcoded mismatch flag, not the live manuscript formula surface. FIX: delete the boolean-mismatch assertion and replace it with direct checks of the corrected values after fixing the engine, e.g. assert self-dual `c=-12`, `\kappa(-12)=-4`, and Feigin-Frenkel complementarity sum `-8`; if a Vol II comparison is still wanted, parse the actual external source in that test instead of hardcoding a discrepancy.

- [MEDIUM] chapters/examples/bar_complex_tables.tex:2609 — PROBLEM: This sentence credits `458` tests to `test_exceptional_shadows.py` and `test_non_simply_laced_shadows.py`, but `pytest --collect-only -q` gives `178` and `168` tests respectively, total `346`. The stated count is unsupported by the two named files. FIX: change `458` to `346`; if `test_exceptional_shadow_complete.py` is meant to be part of the cited verification surface, add that filename explicitly and recompute the total instead of leaving an unexplained number.

- [LOW] chapters/examples/w_algebras.tex:5768 — PROBLEM: The manuscript says `test_w3_genus2.py` has `105` tests, but `pytest --collect-only -q compute/tests/test_w3_genus2.py` collects `125`. FIX: change `$105$~tests` to `$125$~tests`, or remove the numeric count and keep only the file reference so the prose stops drifting when the test surface grows.

- [LOW] compute/lib/theorem_sca_kappa_fix_engine.py:6 — PROBLEM: The audit engine’s seam pointers are stale: it sends the Vol I `N=2` formula to `w_algebras_deep.tex line 4913` and the `N=4` correction to `line 3328`, but the live chapter now carries the `N=2` formula at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5166) and the corrected superconformal hierarchy at [chapters/examples/w_algebras_deep.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3548). FIX: replace raw line numbers with stable labels (`thm:n2-kappa`, `prop:n2-koszul-duality`, `rem:superconformal-complementarity-hierarchy`) or update the line references to the current locations.

## Summary
Checked: 11 | Findings: 7 | Verdict: FAIL
tokens used
211,403
