# B03_thm_C_bridge (662s)

- [CRITICAL] Vol I `chapters/theory/higher_genus_complementarity.tex:40`, `chapters/theory/introduction.tex:830`; Vol II `chapters/frame/preface_trimmed.tex:362`; Vol III `chapters/connections/modular_koszul_bridge.tex:105`, `147` — PROBLEM: the live bridge surface redefines `C2` as the scalar `\kappa+\kappa^!` rule. The canonical Vol I theorem surface says `C0` = fiber-center identification, `C1` = unconditional eigenspace decomposition, `C2` = conditional shifted-symplectic/bar-side BV upgrade, and the scalar formulas are consequences of `C1 + D`, “not a separate C2 label.” FIX: in all three downstream files, replace the current `C2` wording with: `Theorem C has three layers C0/C1/C2. The scalar complementarity identity is a uniform-weight consequence of Theorem C1 together with Theorem D; C2 is the conditional shifted-symplectic upgrade.` In Vol II, replace `the scalar part C2 of Theorem~C` with `the scalar complementarity consequences of Theorem~C1 + Theorem~D`. In Vol III, rename `C2^{CY}` to a non-`C2` scalar label or remove that label entirely.

- [CRITICAL] Vol I `chapters/theory/higher_genus_complementarity.tex:53`, `72`; Vol II `chapters/connections/thqg_symplectic_polarization.tex:31`, `1104`; Vol III `chapters/connections/modular_koszul_bridge.tex:121`, `163`, `chapters/connections/bar_cobar_bridge.tex:219` — PROBLEM: the Vol III bridge rewrites Theorem C with the wrong object. Vol I/Vol II use the complementarity surface `H^*(\overline{\mathcal{M}}_g,\mathcal{Z}(A)) = Q_g(A)\oplus Q_g(A^!)`, with the shifted-symplectic upgrade separate. Vol III replaces that by `\cZ^{der}_{\mathrm{ch}}(A)` / “full Hochschild cohomology” / “CY Euler characteristic,” which is Theorem H or CY-D territory, not Theorem C. FIX: in `modular_koszul_bridge.tex`, replace both occurrences of `H^\bullet(...,\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC))` by `H^\bullet(...,\mathcal{Z}(A_\cC))` or the local system notation already used in Vol I. In `bar_cobar_bridge.tex:219`, replace the bullet with: `Theorem C (complementarity). Assuming A_\cC exists, H^*(\overline{\mathcal{M}}_g,\mathcal{Z}(A_\cC)) \cong Q_g(A_\cC)\oplus Q_g(A_{\cC^!}); for g\ge1 the Verdier pairing identifies the two summands dually.` Keep derived-center/Hochschild claims under Theorem H only, and prefix all `d=3` uses with `Assume CY-A$_3$`.

- [HIGH] Vol I `chapters/theory/introduction.tex:592`, `chapters/theory/chiral_koszul_pairs.tex:70`; Vol II `chapters/connections/thqg_symplectic_polarization.tex:1114`; Vol III `chapters/connections/modular_koszul_bridge.tex:156` — PROBLEM: the unconditional/conditional boundary is reversed or missing. The Vol I introduction presents the shifted-symplectic form as if it were part of unconditional Theorem C; `chiral_koszul_pairs.tex` makes the C1 eigenspace decomposition conditional on perfectness; Vol III never transports the true conditional `C2` at all. Vol II already states the correct split: `C1` unconditional, `C2` conditional. FIX: in `introduction.tex`, replace the shifted-symplectic sentence with `C1 gives the Verdier eigenspace decomposition; the shifted-symplectic/bar-side BV refinement is the separate conditional theorem thm:shifted-symplectic-complementarity.` In `chiral_koszul_pairs.tex`, replace `the Lagrangian eigenspace decomposition is conditional` with `the bar-side shifted-symplectic/Lagrangian criterion is conditional; the C1 eigenspace decomposition is unconditional on the Koszul locus.` In `modular_koszul_bridge.tex`, add a real `C2^{CY}` item: conditional on `CY-A$_3`, perfectness, and nondegeneracy.

- [HIGH] Vol I `chapters/theory/higher_genus_complementarity.tex:444`, `chapters/theory/introduction.tex:355`; Vol II `compute/lib/genus_one_bridge.py:407`, `compute/lib/holographic_ht_engine.py:215`, `compute/lib/bulk_boundary_duality_engine.py:261`, `compute/lib/hochschild_bulk_bridge.py:14`, `compute/lib/genus2_obstruction_engine.py:1002`, `compute/tests/test_hochschild_bulk_bridge.py:213`; Vol III `chapters/theory/braided_factorization.tex:538`, `chapters/connections/modular_koszul_bridge.tex:168`, `compute/lib/fukaya_shadow_tower.py:1942` — PROBLEM: downstream prose, docstrings, and tests cite scalar `\kappa+\kappa^!` / `\rho K` identities as “Theorem C” itself. Canonical Vol I says these are scalar consequences of `C1 + D`, not `C2`; `modular_koszul_bridge.tex:168` also uses Virasoro `K=26` at the kappa-level, contradicting Vol I’s `K=13`. FIX: change every such surface to `scalar complementarity consequence of Vol I Theorem C1 plus Theorem D` or `AP24 scalar complementarity`. In `braided_factorization.tex:538`, replace the opening with `Vol~I Theorem~C1 gives the Verdier eigenspace decomposition; combined with Vol~I Theorem~D it yields the scalar family-dependent sum.` In `modular_koszul_bridge.tex:168`, replace `Virasoro gives K = 26 with scalar sum 13` by `Virasoro scalar sum is 13; 26 is the central-charge sum and must not be used as the kappa-level conductor.`

## Summary
Checked: 26 | Findings: 4 | Verdict: FAIL


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
session id: 019d8426-71a1-7572-a56b-4a8d9937ba9f
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


MISSION: CROSS-VOLUME BRIDGE AUDIT.

Same for Theorem C (all parts). Is complementarity correctly cited? Is C2 conditional status propagated?

Search across all three repos:
- ~/chiral-bar-cobar/
- ~/chiral-bar-cobar-vol2/
- ~/calabi-yau-quantum-groups/

For each finding: exact file:line in EACH volume, PROBLEM, and EXACT FIX.
mcp startup: no servers
codex
Using `deep-beilinson-audit` first, then `cross-volume-propagation` only as an audit lens. I’m locating every live Theorem C / complementarity / C2-conditional surface across the three volumes, then I’ll verify each citation and status against the source text before writing findings.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

 succeeded in 53ms:
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

 succeeded in 53ms:
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
**Updating search strategy**

I’m focusing on relevant surfaces to find exact file lines. I think I could use `rg` across repositories for theorem C and its various parts, like complementarity and the c2 conditional status. I should clearly identify theorem C's actual statement and its parts, which I suspect are in volume I, likely in higher_genus_complementarity.tex. I'll also search in volumes II and III for further references to theorem C and complementarity, and consider reading the theorem registry and concordance for relevant labels. Let's refine the plan!
codex
I have the constitutional surface and the audit scope. Next I’m pinning down the canonical Theorem C statement in Vol I, then I’ll sweep all three repos for every duplicate or citation surface that can misstate complementarity or C2’s conditional boundary.
Plan update
Cross-volume theorem-status audit requires locking the canonical Theorem C surface first, then checking every downstream advertisement against it.
  → Locate the canonical Theorem C statement and part structure in Vol I, including any C1/C2 split and stated conditional hypotheses
  • Search all three volumes for Theorem C, complementarity, and C2 references; collect exact file:line surfaces
  • Compare each occurrence against the canonical status/citation surface and verify whether complementarity and C2 conditionality are propagated correctly
  • Produce severity-ordered findings with exact file:line references and exact fixes

thinking
**Searching for theorem C**

I need to use `rg` to locate theorem C. It might be helpful to consider using parallel executions for my searches. I think I should search across repositories for `thm:quantum-complementarity-main` and possibly C2 as well. I may need to read the canonical file related to the theorem to get more context. So, let's run `rg` on the relevant strings to see what I can find!
exec
/bin/zsh -lc "rg -n --no-heading \"thm:quantum-complementarity-main|Quantum complementarity|Complementarity|Theorem C|C2|C_2|part \\(C2\\)|conditional\" /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"thm:quantum-complementarity-main|Quantum complementarity|Complementarity|Theorem C|C2|C_2|part \\(C2\\)|conditional\" /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"thm:quantum-complementarity-main|Quantum complementarity|Complementarity|Theorem C|C2|C_2|part \\(C2\\)|conditional\" /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 649

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:17:| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROGRAMME | d=3 conditional on chain-level S^3-framing |
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:77:### HZ3-3. AP-CY11 (conditional propagation)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:79:If a result depends on Conjecture X which depends on CY-A_3, the result IS conditional on CY-A_3. Use `\ClaimStatusConditional` and state the dependency chain. Pattern caught at Tier 2: `cor:kappa-from-charts` was `ProvedHere` despite chaining through `conj:e1-chart-gluing -> CY-A_3`. Fixed in cy_to_chiral.tex L1127.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:115:For K3 x E, the identification `Phi_10 = bar Euler product` is an OBSERVATION, not a theorem. It is conditional on:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:192:AP-CY11: Conditional d=3 transitivity. If Result B depends on Result A which depends on CY-A_3, then B is ALSO conditional on CY-A_3. Use \ClaimStatusConditional and state the dependency chain. DEFAULT environment for new Vol III formal statements is \begin{conjecture} unless proof is COMPLETE and UNCONDITIONAL.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:34:- Any `d = 3` version depends on a chain-level `S^3` framing construction and is not unconditional.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:167:   Decide whether the surface is proved, proved elsewhere, conditional, conjectural, heuristic, or open.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:227:- Volume III is dominated by build noise, compute/test frontier corrections, AP113 `kappa`-subscript repair, AP-CY6/AP-CY11/AP-CY14 conditionality failures, AP-CY12 shadow-depth misclassification, AP-CY13 stale Part references, AP-CY17/AP-CY18/AP-CY19 geometric/computational convention drift, README/doc scope inflation, and pi_3(BU)/kappa_ch=h^{1,1}/McKay corrections (AP181-AP183).
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:287:- overclaimed biconditionals;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:410:- `RED`: logic, formulas, signs, hypotheses, scope, hidden conditionality;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:456:- `AP-CY6` / `AP-CY11` / `AP-CY14`: d=3 conditionality propagates;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:508:4. separate construction, evidence, conditional result, conjecture, heuristic, and slogan explicitly;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:510:6. default new Vol III formal frontier statements to `conjecture` unless the proof is complete and unconditional.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:587:- `CY-A` is unconditional only for `d = 2`.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:776:- `AP-CY6` / `AP-CY11` / `AP-CY14` d=3 existence and conditionality;
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:7:Vol I Theorem C (Quantum Complementarity):
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:31:the purely algebraic Theorem C of Vol I.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:141:    Vol I: higher_genus_complementarity.tex (Theorem C)
 succeeded in 53ms:
Total output lines: 1190

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:156:The algebraic framework is unconditional. Former (H1)-(H4) are no longer background axioms: (H1)-(H2) conditions of physics bridge theorem, (H3) theorem of configuration space geometry, (H4) recognition theorem (proved). Homotopy-Koszulity of SC^{ch,top}: PROVED (Kontsevich formality + transfer). All formerly conditional results now unconditional.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:312:| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) Analytic HS-sewing proved at all genera; (2) genus-0 algebraic BRST/bar proved; (3) D^co-level BV=bar proved for all shadow classes including class M; (4) genuswise chain-level BV/BRST/bar conjectural (class M chain-level false); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:335:**Examples** (chapters/examples/): rosetta_stone, examples-computing, examples-worked, examples-complete-proved, examples-complete-conditional, w-algebras-virasoro, w-algebras-w3.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:224:- Vol III `CLAUDE.md`: `AP-CY1` through `AP-CY19` for center discipline, conditionality propagation, CY3 existence boundaries, and cross-volume bridge hazards.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:327:- conditional on `Theorem thm:physics-bridge`;
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:434:- overclaimed biconditionals;
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:572:- unconstructed CY3 objects remain conditional downstream if the proof chain touches them;
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:574:- conditionality propagates through downstream results and summaries.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:772:- if bulk, center, or CY3 bridge language was touched, is scope and conditionality still honest.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:792:The algebraic framework is unconditional. The former standing hypotheses are no longer background fog:
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:815:- any bridge statement whose proof chain depends on an unconstructed CY3 object remains conditional downstream.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:836:- Vol III bridge statements may carry conditionality from unconstructed CY3 objects.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:911:- `chapters/examples/examples-complete-conditional`
/Users/raeez/chiral-bar-cobar-vol2/ROADMAP_85_TO_100.md:156:- **C2.** Define the Boardman-Vogt tensor product of curved operads.
/Users/raeez/chiral-bar-cobar-vol2/ROADMAP_85_TO_100.md:162:  - *Depends on:* C1, C2.
/Users/raeez/chiral-bar-cobar-vol2/ROADMAP_85_TO_100.md:260:7. **C1-C2** (novel operadic algebra, independent research contribution)
/Users/raeez/chiral-bar-cobar-vol2/compute/free_fermion_ordered_bar.py:935:    # Complementarity sum (with Koszul dual)
/Users/raeez/chiral-bar-cobar-vol2/compute/free_fermion_ordered_bar.py:1205:    lines.append(f"    Complementarity: κ + κ! = {md.complementarity_sum}")
 succeeded in 53ms:
Total output lines: 1422

/Users/raeez/chiral-bar-cobar/main.tex:163: \newcommand{\ClaimStatusConditional}{\textnormal{[conditional]}}
/Users/raeez/chiral-bar-cobar/main.tex:1340:% W(p) at p>=2: C_2-cofinite, non-rational, 4 generators.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:289:\[w = \int_{C_2^{\text{ch}}(X)} d\arg(z_2 - z_1) = \frac{1}{2}\]
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:308:Weight: $w_{\Gamma_1} = \frac{1}{8}$ (computed via the Kontsevich configuration space integral on $C_2(\mathfrak{H})$)
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:849:\int_{C_2(\mathfrak{H})} d\phi(z_1,q_1) \wedge d\phi(z_1,q_1)
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:877:\int_{C_2(\mathfrak{H})}
/Users/raeez/chiral-bar-cobar/appendices/koszul_reference.tex:491:unconditionally.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2059: mechanism and a conditional corridor, but not an unconditional
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2346: Koszul conductor (Theorem~\textup{\ref{thm:quantum-complementarity-main}}).
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2938:conditionally:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2942: is unconditional
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3283: by Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:4377:\textup{($g = 1$ only; all-weight at $g = 1$ is unconditional)}
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5022:generated at \emph{all}~$\Psi$ and Koszulness is unconditional.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5089:becomes conditional on the Kac--Shapovalov criterion
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:92:Complementarity & $\kappa(\Psi) + \kappa(-\Psi) = K$

thinking
**Searching for theorem references**

I need to inspect all three repositories for bridge claims about Theorem C. I’ll start by searching for patterns like "Theorem C", "thm:quantum-complementarity-main", "C1", and "C2." Additionally, I should look into label aliasing V1-thm:quantum-complementarity-main. I might want to specifically search for those reference labels and the surfaces C1/C2 in volumes II and III. I can use rg to target "quantum-complementarity-main" along with relevant references to narrow it down. There are many instances of "C2" that are irrelevant, so focusing on exact matches will help.
codex
The raw grep is noisy. I’m narrowing to the canonical theorem statement and the explicit `(C1)/(C2)` bridge surfaces now; that’s where status drift can actually be proven rather than guessed.
exec
/bin/zsh -lc "sed -n '1150,1325p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '120,190p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '790,860p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"label\\{thm:quantum-complementarity-main\\}|Quantum complementarity|C1|C2|Lagrangian|shifted symplectic|perfectness|nondegeneracy\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
(Theorem~\ref{thm:shadow-formality-identification}).
At genus~$0$, the shadow obstruction tower coincides with the $L_\infty$
formality obstruction tower of the convolution algebra
at all degrees. Genus~$g \geq 1$ corrections form a separate layer; the genus and degree directions are orthogonal
(Remark~\ref{rem:two-orthogonal-axes}).
The \emph{visibility formula}
(Corollary~\ref{cor:shadow-visibility-genus})
determines which shadow coefficients contribute at each genus:
\begin{equation}\label{eq:intro-visibility}
g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
\qquad (r \geq 3).
\end{equation}
Genus~$1$ sees only~$\kappa$ (degree~$2$).
Genus~$2$ first sees~$S_3$ (degree~$3$).
Genus~$3$ first sees~$S_4$ and~$S_5$ (degrees~$4$,~$5$).
Two new shadow coefficients enter at each genus.

\emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}).
$Q_g(\cA) \oplus Q_g(\cA^!) \simeq H^*(\overline{\mathcal{M}}_g, Z(\cA))$:
the Verdier involution decomposes the ambient complex into complementary Lagrangians, constraining the Koszul
 succeeded in 53ms:
27:complex, which splits the moduli contribution into two Lagrangian
50: This produces the ambient complex on which~\textup{(C1)}
51: and~\textup{(C2)} operate.
72:\item \emph{Shifted-symplectic Lagrangian upgrade
73: \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
80: $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
83: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
90:The conditionality in~(C2) is substantive:
91:perfectness requires PBW filterability and finite-dimensional
92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
93:nondegeneracy of the Verdier pairing is a hypothesis verified
97:S-level decomposition~(C1) hold unconditionally on the
98:Koszul locus; the H-level Lagrangian upgrade~(C2) is the
101:\begin{remark}[Calabi--Yau exchange and the perfectness hypothesis]
109:(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
110:fiber-level perfectness of the bar complex, and makes
113:intertwining. The family-level perfectness over
114:$\overline{\mathcal{M}}_g$ required by~(C2) is a stronger
116:base change (Lemma~\ref{lem:perfectness-criterion}).
 succeeded in 53ms:
 pair, which equips the pair
 $(\cA_1, \cA_2)$ with Verdier-compatible identifications
 $\mathbb{D}_{\mathrm{Ran}}(\cC_1) \simeq \cC_2$ from the
 outset; Theorem~A part~(1), the bar-cobar adjunction, then
 supplies the unit and counit quasi-isomorphisms
 $\cC_i \simeq \barB_X(\cA_i)$ on the Koszul locus.
 Part~(2), the Verdier intertwining
 $\mathbb{D}_{\mathrm{Ran}}\barB_X(\cA_1) \simeq \barB_X(\cA_2)$,
 then unpacks the Verdier clause of the definition by transport
 across part~(1). This supplies the algebraic pair
 $(\cA, \cA^!)$ on which the Drinfeld double $U_\cA$ is
 defined.

\item \emph{Non-degenerate reconstruction}
 \textup{(}Theorem~B\textup{)}.
 On the Koszul locus the counit
 $\Omega_X\barB_X(\cA) \xrightarrow{\sim} \cA$ is a
 quasi-isomorphism. The non-tautological content lies at
 genus $g \ge 1$, where the inductive genus step of
 Theorem~B extends the quasi-isomorphism across the genus
 succeeded in 53ms:
which extends to:
\begin{equation}
\mathcal{A}^{\boxtimes n} \otimes (\mathcal{A}^!)^{\boxtimes n} \to \mathcal{O}_{X^n}
\end{equation}

Combining with the Verdier pairing on $\Omega^*_{\log}$ from Theorem~\ref{thm:verdier-duality-config-complete}, we obtain:
\begin{equation}
\langle s, t \rangle = \int_{\overline{C}_n(X)} (s \otimes t) \wedge (-)
\end{equation}
for $s \in \bar{B}^n(\mathcal{A})$ and $t \in \bar{B}^n(\mathcal{A}^!)$.

This pairing is perfect because both the Koszul pairing and the Verdier pairing are 
perfect.
\end{proof}

\emph{Step 6: Duality interchanges spectral sequences.}

\begin{lemma}[Spectral sequence duality; \ClaimStatusProvedHere]
\label{lem:ss-duality-complete}
The Verdier duality of Theorem~\ref{thm:verdier-duality-config-complete} induces an isomorphism 

thinking
**Examining theorem lines**

I need to focus on finding the specific canonical theorem statement around line 458. It's important to read through the lines surrounding it to fully understand the context. I want to ensure I grasp the content thoroughly, so I'll be taking the time to delve into that section and make sure I'm not missing anything key. Let’s get that done so I can have a solid foundation moving forward!
exec
/bin/zsh -lc "sed -n '440,610p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
splitting; $\mathrm{C}_2$
(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
conditional bar-side BV / shifted-symplectic upgrade.
The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
$\sigma$ exchanging the two eigenspaces; at the scalar level
the complementarity formulas below are consequences of the
$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
separate $\mathrm{C}_2$ label:
$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
Table~\ref{tab:complementarity-landscape}).
\end{remark}

The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}

thinking
**Inspecting theorem statements**

I see that the theorem mentions perfect duality and Lagrangian conditions. But there’s an earlier note about C2 conditional bar-side BV and shifted-symplectic upgrades. It seems that theorem C might only involve decomposition and perfect duality at the cochain level. I need to check the preamble around lines 50-100 for more context since it has an initial summary. I’ll take a closer look at the beginning of the file.
exec
/bin/zsh -lc "sed -n '1,130p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)

thinking
**Considering Lagrangian concepts**

I’m thinking about the term “Lagrangian” in relation to a cochain-level pairing. It’s intriguing how, in finite-dimensional linear algebra, Lagrangian might not necessitate a shifted symplectic ambient. This makes me wonder about the implications for various structures and contexts I'm exploring. I might need to look deeper into how these definitions interplay and affect each other. It's like there's a lot of nuances to unpack here!
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem~C|Theorem C|\\(C1\\)|\\(C2\\)|part~\\(1\\)|part~\\(2\\)|part~\\(C1\\)|part~\\(C2\\)|eigenspace decomposition|scalar sum rule|Lagrangian upgrade|shifted-symplectic\" chapters/theory chapters/connections chapters/examples appendices | head -n 400" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"Theorem C|\\(C1\\)|\\(C2\\)|part~\\(1\\)|part~\\(2\\)|eigenspace decomposition|scalar sum rule|Lagrangian upgrade|shifted-symplectic|quantum-complementarity-main|V1-thm:quantum-complementarity-main\" /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute | head -n 400" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"Theorem C|\\(C1\\)|\\(C2\\)|part~\\(1\\)|part~\\(2\\)|eigenspace decomposition|scalar sum rule|Lagrangian upgrade|shifted-symplectic|quantum-complementarity-main|V1-thm:quantum-complementarity-main\" /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute /Users/raeez/calabi-yau-quantum-groups/README.md /Users/raeez/calabi-yau-quantum-groups/main.tex | head -n 400" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/homotopy_transfer.tex:815:This gives a homotopy-algebraic interpretation of Theorem~C
appendices/homotopy_transfer.tex:828:This interpretation elevates Theorem~C from a numerical identity to a
appendices/nonlinear_modular_shadows.tex:567:An additive splitting can always be faked by eigenspace decompositions, arbitrary direct sums, or linear bookkeeping identities. The ambient theorem is harder to fake because it requires:
appendices/nonlinear_modular_shadows.tex:2050:\item The quadratic theory is the proved scalar and shifted-symplectic complementarity package.
chapters/connections/editorial_constitution.tex:2224:(shifted-symplectic/Lagrangian enhancement). The conjecture
chapters/connections/editorial_constitution.tex:2226:shifted-symplectic structure on the total deformation complex.
chapters/connections/editorial_constitution.tex:2444:\item \emph{The Lagrangian branch structure.} A shifted-symplectic
chapters/examples/lattice_foundations.tex:1957:\item \emph{Theorem~C}
appendices/combinatorial_frontier.tex:701:the Casimir eigenspace decomposition of $\mathfrak{sl}_3^{\otimes 4}$ has been
chapters/connections/thqg_symplectic_polarization.tex:25:\section{Complementarity as shifted-symplectic polarization}
chapters/connections/thqg_symplectic_polarization.tex:38:\textup{(}Theorem~\ref{thm:shifted-symplectic-complementarity}\textup{)},
chapters/connections/thqg_symplectic_polarization.tex:39:while the ambient Verdier and cyclic-deformation shifted-symplectic
chapters/connections/thqg_symplectic_polarization.tex:43:decomposition is unconditional on the Koszul locus~(C1), while the
chapters/connections/thqg_symplectic_polarization.tex:44:shifted-symplectic Lagrangian structure~(C2) becomes the natural
chapters/connections/thqg_symplectic_polarization.tex:61:unconditional eigenspace decomposition~(C1) with complete detail.
chapters/connections/thqg_symplectic_polarization.tex:62:\S\ref{subsec:thqg-III-shifted-symplectic} develops the
chapters/connections/thqg_symplectic_polarization.tex:63:shifted-symplectic structure~(C2), including a self-contained
chapters/connections/thqg_symplectic_polarization.tex:433: giving a genuine shifted-symplectic structure.
chapters/connections/thqg_symplectic_polarization.tex:459:% 2. THE UNCONDITIONAL EIGENSPACE DECOMPOSITION (C1)
chapters/connections/thqg_symplectic_polarization.tex:463:\subsection{The unconditional eigenspace decomposition}
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex:1178:\section{An Airy--Witt normal form for the odd ladder sector of \texorpdfstring{$T^*[1]\operatorname{Ham}(\mathbb{C}^2)$}{T*[1]Ham(C2)}}
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus_one_bridge.py:407:    From Theorem C: κ(A) + κ(A!) = const for each family.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:119:theorem (Theorem~\ref{V1-thm:quantum-complementarity-main}). In the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer.tex:1189:\section{An Airy--Witt normal form for the odd ladder sector of \texorpdfstring{$T^*[1]\operatorname{Ham}(\mathbb{C}^2)$}{T*[1]Ham(C2)}}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2292:of a shifted-symplectic deformation problem. The complementarity
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1123: & \checkmark\;Thm~\ref{thm:quantum-complementarity-main} \\[4pt]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1221: (Theorem~\ref{thm:quantum-complementarity-main}), and the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1429: (Theorem~\ref{thm:quantum-complementarity-main}) are
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1601: (Theorem~\ref{V1-thm:quantum-complementarity-main}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1644:Feigin--Frenkel; its all-genera shadow is shifted-symplectic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:2058:(Theorem~\ref{V1-thm:shifted-symplectic-complementarity}): the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:63:\label{rem:shifted-symplectic-from-cyclic}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:485:(Remark~\ref{rem:shifted-symplectic-from-cyclic}) restricts
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2195:shifted-symplectic small resolution.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2462:admits a well-defined derived structure. In the shifted-symplectic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:1567:natural shifted-symplectic structure, and the two summands are
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:1611:The eigenspace decomposition
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:1626:The eigenspace decomposition is immediate from $\sigma_g^2 = \operatorname{id}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:1688:eigenspace decomposition.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:1707:Under the eigenspace decomposition
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:105:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:135:(C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:219: \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/kl_sl2_level1.py:9:This is the prototypical instance of Theorem CY-C (quantum group
/Users/raeez/calabi-yau-quantum-groups/compute/lib/kl_sl2_level1.py:884:    This is the simplest non-trivial case and the prototype for Theorem CY-C.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/kl_sl2_level1.py:1067:    lines.append(f"at q = exp(pi*i/3), the simplest instance of Theorem CY-C.")
/Users/raeez/calabi-yau-quantum-groups/compute/lib/vafa_witten_shadow.py:285:    The complementarity relation (Theorem C) gives:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3e_e1_product_chain.py:1203:    Theorem CY-A_2; the d=3 case is Conjecture CY-A_3).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:16:\begin{theorem}[CY modular characteristic: Theorem CY-D]
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_euler.py:8:  chapters/theory/modular_trace.tex (Theorem CY-D),
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_euler.py:40:is the BKM superalgebra -- the content of Theorem CY-D.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_euler.py:789:    This is the CY Euler characteristic chi^CY in the sense of Theorem CY-D.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_euler.py:1331:    For K3 x E, kappa = 5 (Theorem CY-D, verified above).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_euler.py:1352:        "kappa_source": "Theorem CY-D + Borcherds product",
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:143:  - For CY3 algebras: kappa = chi^CY(X) (Theorem CY-D).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:506:    kappa = 5 (Theorem CY-D, from weight of Delta_5).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py:1942:    from Vol I Theorem C for Koszul pairs.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py:1960:        This is the geometric manifestation of Theorem C:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:310:\begin{theorem}[$E_2$-bar-cobar adjunction: Theorem CY-B]






thinking
**Deciding on output formatting**

I’m looking at the structured output contract, which indicates each finding should be reported as one file:line. However, the user wants exact file:line references for each finding across different volumes. This adds complexity, as a finding might span multiple files. I could report each drift cluster with multiple file:line references, possibly using semicolons to separate them. I should ensure to maintain the format like `[HIGH] file1:line; file2:line — PROBLEM: ... FIX: ...`.
thinking
**Considering cross-volume findings**

I think I need to mention surfaces in each volume for the cross-volume finding. If there's no corresponding bad surface in one volume, it might not be literal for each volume. Since they asked for a search across all three repos, I might mention findings from Vol III alongside the canonical source in Vol I. The request specifies giving exact file and line for each, which makes me wonder about how to present findings correctly. I'll need to check references carefully, especially regarding Theorem C.
thinking
**Verifying volume II findings**

It seems that Vol II on twisted holography and quantum gravity is likely correct since it cites both the theorem and the upgrade, but I need to verify that. I’m noticing that some surfaces might only reference Theorem C for the shifted-symplectic Lagrangian splitting without any conditionality. I’ll need to search through the flagged lines in Vol II and read those files closely. Oh, and I should probably check the introduction in Vol I for context!
thinking
**Considering search methods**

I’m thinking about searching through three repositories, focusing on bridge files in volumes 2 and 3, along with canonical surfaces from volume 1. Maybe explorer agents could help, but direct searches could work too. However, since I’ve already conducted a manual search, I'm wondering if that’s enough. The instructions say to prefer explorers unless specified otherwise. Since user didn’t request subagents, I should stick to manual for now and inspect files with potential issues.
thinking
**Planning an inspection**

I'm planning to inspect the introduction in Volume I around the theorem C section and line 460, along with checking `chapters/theory/chiral_koszul_pairs.tex`, particularly line 70, which discusses eigenspace decomposition under perfectness. I think there could be issues in Volume I, so I'll focus on bridge chapters and major introductions, as the user wants a thorough audit. It might be necessary to check all explicit theorem C references in the three repositories, but that feels overwhelming. I’ll define the audit surface more specifically to include summary and bridge files across volumes for relevant insights.
thinking
**Inspecting candidate files**

I want to inspect some candidate problem files. First, I’ll look at Volume I's `chapters/theory/introduction.tex`, particularly around theorem C, focusing on lines 460, 581, and 830. I should also check `chapters/theory/chiral_koszul_pairs.tex` in Volume I, especially line 70, which talks about eigenspace decomposition under perfectness. There might be critical insights hidden in these sections, so it's essential to be thorough here and understand the context of these claims.
codex
I’ve isolated the highest-risk drift pattern already: downstream files are reusing “C2” to mean the scalar `κ + κ^!` rule, while the canonical Vol I source defines `C2` as the conditional shifted-symplectic/Lagrangian upgrade. I’m now verifying every concrete occurrence before I keep it as a finding.
exec
/bin/zsh -lc "sed -n '450,620p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,840p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,130p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,160p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '200,240p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '720,760p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa(\cH_k^!) = -k$, the opposite modular characteristic
(the Heisenberg is \emph{not} Koszul self-dual;
see~\S\ref{sec:frame-koszul-dual}).
The cobar of the bar is
$\Omega(\barB(\cH_k)) = T(s\,\C\cdot s^{-1}J) = \C[J]$,
which is $\cH_k$ as a graded algebra. The counit
$\varepsilon\colon\Omega(\barB(\cH_k)) \to \cH_k$ is a
quasi-isomorphism: the Heisenberg is Koszul.

\smallskip
\noindent\textbf{Theorem~C (complementarity).}\enspace
At genus~$g \ge 1$:
$Q_g(\cH_k) \oplus Q_g(\cH_k^!) \cong
H^*(\overline{\cM}_g, \cZ_{\cH_k})$.
The modular characteristic is $\kappa(\cH_k) = k$, and
$\kappa(\cH_k) + \kappa(\cH_k^!) = k + (-k) = 0$. The
complementarity sum of central charges is
$c(\cH_k) + c(\cH_k^!) = 1 + 1 = 2$
(noting that the dual is curved, so $c(\cH_k^!)=1$ refers to
the underlying graded algebra).
 succeeded in 51ms:
 For each standard family, the modular characteristic of the
 boundary and its Koszul dual sum to a family-specific Koszul
 conductor,
 $\kappa(\cA) + \kappa(\cA^!) = K_\cA$:
 $K = 0$ for Heisenberg and affine Kac--Moody at the linear
 level, $K = 13$ for Virasoro (self-dual at $c = 13$), with
 family-dependent nonzero values for the principal
 $\mathcal{W}$-algebras
 (Theorem~\ref{thm:central-charge-complementarity}). The
 sum rule is a family-specific holographic conservation law,
 not a universal constant. Theorem~C part~(1) (eigenspace
 decomposition under the Verdier involution) is
 unconditional; part~(2) (scalar sum rule) is proved on the
 uniform-weight lane.

\item \emph{Brown--Henneaux coefficient}
 \textup{(}Theorem~D\textup{)}.
 On the uniform-weight lane, the genus-$g$ obstruction
 is $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$, with
 $\lambda_g$ the $g$-th Mumford class (the gravitational
 succeeded in 51ms:
% Section file for Chapter: Twisted Holography and Quantum Gravity
% Result (G3): Complementarity as Shifted-Symplectic Polarization

% Local macros (providecommand only; never \newcommand in chapter files)
\providecommand{\MC}{\mathrm{MC}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
\providecommand{\Sh}{\mathrm{Sh}}
\providecommand{\gr}{\operatorname{gr}}
\providecommand{\id}{\mathrm{id}}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\Sym}{\operatorname{Sym}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\End}{\operatorname{End}}
\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\rank}{\operatorname{rank}}
\providecommand{\ad}{\operatorname{ad}}
\providecommand{\Fred}{\operatorname{Fred}}
\providecommand{\Map}{\operatorname{Map}}
 succeeded in 50ms:
\chapter{Modular Koszul Duality and CY Geometry}
\label{ch:modular-koszul-bridge}

A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.


%% ===================================================================
%% SECTION 1: CY modular convolution algebra
%% ===================================================================

\section{The modular convolution algebra for CY categories}
\label{sec:modular-conv-cy}

Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.

\begin{definition}[CY modular convolution algebra]
\label{def:cy-modular-convolution}
The \emph{CY modular convolution algebra} of the pair $(B(A_\cC), A_\cC)$ is the graded vector space
\[
 \mathrm{Conv}_{\mathrm{str}}\bigl(B(A_\cC), A_\cC\bigr)
 succeeded in 51ms:
\end{conjecture}


%% ===================================================================
%% SECTION 6: The five theorems in the CY setting
%% ===================================================================

\section{The five theorems in the CY setting}
\label{sec:five-theorems-cy}

We summarize the status of the five main theorems of Volume~I when specialized to chiral algebras arising from CY categories.

\begin{theorem*}[The five theorems for CY chiral algebras]
Let $A = A_\cC$ be the chiral algebra of a CY$_3$ category $\cC$. Then:
\begin{description}
 \item[Theorem A (adjunction).] The bar-cobar adjunction $B \dashv \Omega$ restricts to CY chiral algebras: $B(A_\cC)$ is a factorization coalgebra on $\Ran(X)$, and $D_{\Ran}(B(A_\cC)) \simeq B(A_{\cC^!})$. The CY identification CY-A(ii) gives $\mathrm{CC}_\bullet(\cC) \simeq B(A_\cC)$.

 \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.

 \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
 succeeded in 51ms:
\begin{theorem}[\textbf{G3}: Symplectic polarization; \ClaimStatusProvedHere]
% label removed: thm:thqg-g3-polarization
\index{symplectic polarization!gravitational}
\index{Lagrangian decomposition!complementarity}
Let $(\cA, X, \langle\cdot,\cdot\rangle, k)$ be a gravitational input.
\textbf{Additional hypotheses}: (a)~the cyclic pairing
$\langle\cdot,\cdot\rangle$ is nondegenerate at the chain level
(not merely on cohomology); (b)~the ambient complex $\mathbf{C}_g(\cA)$
is perfect as a chain complex.
Under these hypotheses, the complementarity splitting
\eqref{V1-eq:thqg-lagrangian-splitting} is a shifted-symplectic Lagrangian
decomposition: both summands are Lagrangian with respect to the
$(-1)$-shifted symplectic form on $\mathbf{C}_g(\cA)$. The Verdier
involution acts as gravitational CPT conjugation.

\smallskip\noindent
\textit{Conditionality note.}
The perfectness and chain-level nondegeneracy hypotheses are satisfied
for all standard families in the landscape
(Definition~\ref{V1-def:thqg-standing-hypotheses}), but may fail for

thinking
**Inspecting file accuracy**

It looks like the Volume II current file seems correct, but I’m considering if there might be other files to look at too. I think I need to inspect the line in `thqg_3d_gravity_movements_vi_x`, around line 119, to see if I miscite theorem C. 

But honestly, it seems likely to be correct. I also need to check the Volume II compute docstrings and any tests. Let’s read through these candidate files for more clarity.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus_one_bridge.py | sed -n '398,414p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py | sed -n '255,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py | sed -n '998,1015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py | sed -n '208,224p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py | sed -n '8,22p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_hochschild_bulk_bridge.py | sed -n '207,218p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   398	
   399	
   400	# ═══════════════════════════════════════════════════════════════════════
   401	# Complementarity at genus 1
   402	# ═══════════════════════════════════════════════════════════════════════
   403	
   404	def complementarity_genus1(family: str, **params) -> Dict[str, object]:
   405	    """Verify genus-1 complementarity: F₁(A) + F₁(A!) = const/24.
   406	
   407	    From Theorem C: κ(A) + κ(A!) = const for each family.
   408	    Therefore F₁(A) + F₁(A!) = const/24.
   409	
   410	    The complementarity constant depends only on the root datum,
   411	    not on the level or central charge.
   412	    """
   413	    if family not in _FAMILIES:
   414	        raise ValueError(f"Unknown family '{family}'. Known: {list(_FAMILIES.keys())}")
 succeeded in 51ms:
   208	    C: LineCategoryData
   209	    r_z: CollisionResidueData
   210	    theta: MCElementData
   211	    connection: Dict[Tuple[int, int], HolographicConnectionData]
   212	    # (genus, arity) -> connection data
   213	
   214	    def kappa_complementarity(self) -> Dict[str, Any]:
   215	        """Verify kappa(A) + kappa(A!) = rho*K (Theorem C).
   216	
   217	        For KM and free fields: rho*K = 0.
   218	        For W-algebras: rho*K = constant (level-independent).
   219	        """
   220	        kappa_A = self.A.kappa
   221	        kappa_dual = self.A_dual.kappa
   222	        kappa_sum = simplify(S(kappa_A) + S(kappa_dual))
   223	        expected = self.A_dual.kappa_sum
   224	        return {
 succeeded in 51ms:
   255	
   256	# =========================================================================
   257	# 2. KAPPA COMPLEMENTARITY VERIFICATION (THEOREM C)
   258	# =========================================================================
   259	
   260	def verify_kappa_complementarity(pair: KoszulDualPair) -> Dict[str, Any]:
   261	    """Verify kappa(A) + kappa(A!) = rho*K (Theorem C).
   262	
   263	    For Kac-Moody and free fields: rho*K = 0.
   264	    For W-algebras: rho*K = constant depending only on the algebra type.
   265	
   266	    The complementarity constant is LEVEL-INDEPENDENT. This is the
   267	    content of Theorem C: the modular characteristic is duality-constrained.
   268	    """
   269	    kappa_sum = simplify(pair.kappa + pair.dual_kappa)
   270	    expected_sum = pair.kappa_sum
 succeeded in 51ms:
   998	
   999	def genus2_complementarity_check(c_val=None):
  1000	    r"""Check Theorem C complementarity at genus 2.
  1001	
  1002	    Theorem C states: Q_g(A) + Q_g(A!) = H*(M_g, Z(A))
  1003	
  1004	    At the scalar level (free energy):
  1005	      F_g(A) + F_g(A!) = F_g(A) + F_g(A!)
  1006	
  1007	    For Virasoro: A = Vir_c, A! = Vir_{26-c}
  1008	      kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2
  1009	      F_2(Vir_c) + F_2(Vir_{26-c}) = 7c/11520 + 7(26-c)/11520
  1010	                                    = 7*26/11520 = 182/11520 = 91/5760
  1011	
  1012	    This sum is INDEPENDENT of c (universal, Theorem C).
  1013	    """
  1014	    c = Symbol('c') if c_val is None else S(c_val)
  1015	
 succeeded in 51ms:
     8	At genus 0, these are quasi-isomorphic via translation invariance on C,
     9	contractibility of C, and a filtration argument. This module checks the
    10	isomorphism explicitly for the standard landscape:
    11	  Heisenberg, affine sl_2, Virasoro, betagamma, lattice VOAs.
    12	
    13	Also verifies:
    14	  - kappa-complementarity: kappa(A) + kappa(A!) is level-independent (Theorem C)
    15	  - Shadow archetype transfer: shadow depth matches Vol I classification
    16	  - Koszul dual pairing: Euler characteristic and Poincare duality
    17	
    18	Paper references:
    19	  Vol I: chiral_hochschild_koszul.tex (Theorem H), concordance.tex
    20	  Vol II: bulk_chc.tex, examples-computing.tex
    21	  Cross-volume: thm:hochschild-bridge-genus0
    22	
 succeeded in 51ms:
   207	# KAPPA COMPLEMENTARITY (Theorem C)
   208	# ===================================================================
   209	
   210	class TestKappaComplementarity:
   211	    """Verify kappa(A) + kappa(A!) is level-independent.
   212	
   213	    Theorem C: Q_g(A) + Q_g(A!) = H*(M_g, Z(A)).
   214	    At the scalar level, this means kappa(A) + kappa(A!) is a constant
   215	    depending only on the root datum, not on the level parameter.
   216	    """
   217	
   218	    def test_virasoro_kappa_sum(self):

thinking
**Searching for scalar complementarity**

I noticed that the compute documents are misattributing scalar complementarity to Theorem C. I might need to choose a representative example. The user mentioned something about exhaustiveness, so it seems I need to search all compute files in volume 2 for the term "kappa(A) + kappa(A!)" and Theorem C. There might be quite a few instances to look through. Searching by pattern could be a good approach here!
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem C.*kappa|kappa\\(A\\) \\+ kappa\\(A"'!'"\\)|rho\\*K|kappa-complementarity|Complementarity .*Theorem C\" /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/chiral-bar-cobar-vol2/chapters | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_cross_engine_consistency.py:235:    """kappa(A) + kappa(A!) consistent across engines."""
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:14:  - kappa-complementarity: kappa(A) + kappa(A!) is level-independent (Theorem C)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:59:    kappa_sum: object               # kappa(A) + kappa(A!), should be level-independent
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:492:    """Verify kappa-complementarity: kappa(A) + kappa(A!) is level-independent.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:495:    At the scalar level: kappa(A) + kappa(A!) depends only on root data,
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:498:    For KM families: kappa(A) + kappa(A!) = 0.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/cross_volume_deep_bridge.py:569:    """Verify kappa complementarity: kappa(A) + kappa(A!) is constant.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/cross_volume_deep_bridge.py:744:    2. kappa(A) + kappa(A!) is constant
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:72:    kappa_sum: Any  # kappa(A) + kappa(A!)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:231:    This is the rho*K constant for W_3 (Theorem C).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:261:    """Verify kappa(A) + kappa(A!) = rho*K (Theorem C).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:263:    For Kac-Moody and free fields: rho*K = 0.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:264:    For W-algebras: rho*K = constant depending only on the algebra type.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/modular_pva_quantization.py:1006:    """Verify kappa(A) + kappa(A!) = const for each family.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:125:    kappa_sum: Any  # kappa(A) + kappa(A!) = rho*K (level-independent)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:215:        """Verify kappa(A) + kappa(A!) = rho*K (Theorem C).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:217:        For KM and free fields: rho*K = 0.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:218:        For W-algebras: rho*K = constant (level-independent).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:1266:    """Verify Theorem C (kappa complementarity) for all standard families."""
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/modular_obstruction_engine.py:1069:        kappa(A) + kappa(A!) = 0  (for affine/free field families)

thinking
**Searching for compute resources**

I'm considering how many compute surfaces there are. I think I might need to utilize a cluster to find compute documents in volume 2. Additionally, I could search for something similar in volume 3. It seems like I'll need to explore those options further. Okay, let's get to searching!
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem C.*kappa|kappa\\(A\\) \\+ kappa\\(A"'!'"\\)|kappa\\+kappa|Complementarity.*Theorem C|Theorem C bridge|Theorem C \\(Quantum Complementarity\\)|Vol I Theorem C\" /Users/raeez/calabi-yau-quantum-groups/compute /Users/raeez/calabi-yau-quantum-groups/chapters | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:255: \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:7:Vol I Theorem C (Quantum Complementarity):
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:936:    Returns a list of (name, kappa, kappa^!, kappa+kappa^!, type, antisymmetric).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/mirror_e1_koszul_engine.py:65:   (AP24: kappa(A) + kappa(A!) = 0 for KM/free fields).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/conifold_e1_full_chain.py:1043:                "so AP24 complementarity kappa+kappa'=0 need not hold)."
/Users/raeez/calabi-yau-quantum-groups/compute/lib/c3_grand_verification.py:1065:    Complementarity: kappa(A) + kappa(A!) = 0 for free fields.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py:1942:    from Vol I Theorem C for Koszul pairs.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py:1961:            kappa(A) + kappa(A!) = 0
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_bar_complex_engine.py:523:    Theorem CY-D: kappa(A_C) = chi^CY(C).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_bar_complex_engine.py:535:        of the CATEGORY. Theorem CY-D equates kappa(A_C) = chi^CY(C),
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:51:Hook flagged AP24 (bare kappa+kappa'=0), AP25/AP34 (bar-cobar), AP113 (bare kappa), AP7/AP32 (scope), AP14 (Koszulness), AP106 (narration block), V2-AP26 (hardcoded Part numbers) at lines NOT touched by this sweep (working_notes.tex lines 179, 213, 274, 798, 1167, 1785, 1878, 2399, 2494, 2522, 3492, 3527; cy_to_chiral.tex lines 202, 596, 1039, 1261; preface.tex lines 196 context, 284-291; fukaya_categories.tex lines 196, 558). These are pre-existing content violations unrelated to MC5 status and outside task scope.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/attractor_shadow_e1_engine.py:1273:# 19. DISCRIMINANT COMPLEMENTARITY (Theorem C bridge)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/modular_cy_characteristic.py:27:  Theorem CY-D: kappa(A_C) = chi^CY(C) when A_C is the chiral algebra
/Users/raeez/calabi-yau-quantum-groups/compute/lib/modular_cy_characteristic.py:201:    Theorem CY-D: kappa(A_C) = chi^CY(C).
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:13:However, several CRITICAL and SERIOUS issues hide in the substance. The preface uses `\HH_\bullet(\cC) \to k[-d]` (line 21-22) for the CY trace, directly violating AP-CY2 (CY trace lives in HC^-_d, negative cyclic, not Hochschild homology). The modular characteristic identity `\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)` (line 28) is asserted in the preface but is exactly the content of Theorem CY-D, which is labelled PROGRAMME in CLAUDE.md (d=3 conditional on A_C existing). The "six independent paths" verification of `\kappa_{\mathrm{ch}}(K3 x E) = 3` is asserted without citation and would fail AP10 if queried. The CoHA paragraph declares CoHA "the ordered bar complex of the CY_3 chiral algebra" -- but the CY_3 chiral algebra is exactly the object that does not yet exist (AP-CY6), so this is an unconstructed-object assertion in a preface posing as theorem. The `\C^3 -> W_{1+infty} -> Rep^{E_2}(Y(gl_1-hat))` chain is claimed "verified end-to-end" with no citation.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:31:  This is asserted in preface-voice. But A_C for CY_3 is exactly the d=3 programme (AP-CY6: "A_X for CY3 does NOT exist"). CLAUDE.md marks CY-A (existence of Phi) as "d=2 PROVED; d=3 PROGRAMME" and CY-D (modular characteristic) as "PROGRAMME". The preface then tries to fix this at line 62-64 by saying "Theorem CY-A constructs Phi for d=2: all three steps are proved. For d=3, step (3) is a programme..." But this is inconsistent: lines 28-30 have already asserted kappa_ch(A_C) and shadow/automorphic identification for the d=3 case (since the following paragraph is about K3 x E, a CY_3). The scope disclaimer arrives 35 lines too late.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:53:  kappa(A) + kappa(A!) = 0         for KM / free fields / lattice
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:54:  kappa(A) + kappa(A!) = 13        for Virasoro (c + (26-c))/2 = 13
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:55:  kappa(A) + kappa(A!) = 250/3     for W_3 (5c/6 + 5(100-c)/6)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:329:    r"""kappa(A) + kappa(A!) for each family.

thinking
**Inspecting file details**

I need to check the volume 3 compute docstrings. They might not require as much scrutiny since there could be no misuse of Theorem C. I’ll look into `entropy_koszul_complement_cy3.py`, as it likely cites Theorem C directly, which could be fine. It seems important to inspect the start of the file and I’ll also take a look at `cross_volume_shadow_bridge.py` to determine if anything needs revisiting.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py | sed -n '45,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/vafa_witten_shadow.py | sed -n '280,292p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py | sed -n '1936,1965p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   280	
   281	    The S-duality relation is:
   282	      Z_VW(S, G; -1/tau) ~ Z_VW(S, G^v; tau)
   283	
   284	    Both have the same modular weight (since chi(S) is the same).
   285	    The complementarity relation (Theorem C) gives:
   286	      kappa(G) + kappa(G^v) depends on the algebra family.
   287	    """
   288	    return {
   289	        'kappa_G': kappa_G,
   290	        'kappa_Gv': kappa_Gv,
   291	        'kappa_sum': kappa_G + kappa_Gv,
   292	        'same_weight': kappa_G == kappa_Gv,
 succeeded in 53ms:
    45	
    46	SHADOW DEPTH CLASSIFICATION (G/L/C/M, from Vol I):
    47	  G (Gaussian, r_max = 2):   Heisenberg, pure lattice VOAs
    48	  L (Lie/tree, r_max = 3):   affine Kac-Moody at all types
    49	  C (contact/quartic, r_max = 4): beta-gamma, bc ghosts
    50	  M (mixed, r_max = infinity):    Virasoro, W_N
    51	
    52	COMPLEMENTARITY (Theorem C, AP24):
    53	  kappa(A) + kappa(A!) = 0         for KM / free fields / lattice
    54	  kappa(A) + kappa(A!) = 13        for Virasoro (c + (26-c))/2 = 13
    55	  kappa(A) + kappa(A!) = 250/3     for W_3 (5c/6 + 5(100-c)/6)
    56	
    57	SWISS-CHEESE FORMALITY (Vol II, AP14):
    58	  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
    59	  SC-non-formal: affine KM (class L, m_3^{SC} != 0), beta-gamma (class C, m_4^{SC} != 0),
    60	                 Virasoro/W_N (class M, m_k^{SC} != 0 for all k >= 3)
 succeeded in 53ms:
     1	r"""
     2	entropy_koszul_complement_cy3.py -- Black hole entropy from Koszul complementarity.
     3	
     4	MATHEMATICAL CONTENT
     5	====================
     6	
     7	Vol I Theorem C (Quantum Complementarity):
     8	
     9	    H^*(M_bar_g, Z(A)) = Q_g(A) (+) Q_g(A^!)
    10	
    11	For a chiral Koszul pair (A, A^!), the genus-g cohomology of M_bar_g with
    12	coefficients in the center local system Z(A) decomposes into complementary
    13	Lagrangian halves: what A sees as obstruction, A^! sees as deformation.
    14	
    15	KOSZUL COMPLEMENTARITY DEFECT:
    16	
    17	    delta_g(A) := dim H^*(M_bar_g, Z(A)) = dim Q_g(A) + dim Q_g(A^!)
    18	
    19	For CY3 mirror pairs (X, X_check) with A_X, A_{X_check} = A_X^{!,E_1}:
    20	
 succeeded in 53ms:
  1936	    These are OPPOSITE in sign, reflecting the fact that mirror symmetry
  1937	    EXCHANGES the sign of chi.  At the shadow level, this means:
  1938	
  1939	        kappa(A_model) + kappa(B_model) = 0
  1940	
  1941	    This is the CY3 avatar of the complementarity sum kappa + kappa' = 0
  1942	    from Vol I Theorem C for Koszul pairs.
  1943	    """
  1944	
  1945	    @staticmethod
  1946	    def a_model_kappa() -> Fraction:
  1947	        """kappa from the A-model (Fuk(Q))."""
  1948	        return Fraction(-FukayaQuintic.CHI)  # = 200
  1949	
  1950	    @staticmethod
  1951	    def b_model_kappa() -> Fraction:
  1952	        """kappa from the B-model (D^b(Q_mirror))."""
  1953	        chi_mirror = -FukayaQuintic.CHI  # chi(Q_mirror) = -chi(Q) = 200
  1954	        return Fraction(-chi_mirror)  # = -200
  1955	

thinking
**Inspecting theorem details**

I’m checking the Vol3 compute surfaces, but I'm a bit unsure if they’re accurate. I really need to focus on the mislabeling of theorem C/C2. I should inspect the line numbers in volume 1's introduction and possibly look at `chiral_koszul_pairs.tex`. There seems to be a conditional mismatch in the rg results; specifically, `chapters/theory/chiral_koszul_pairs.tex:70`. It mentions that something is conditional on perfectness, but the canonical source says C1 is unconditional. I definitely need to look into this further.
exec
/bin/zsh -lc "nl -ba chapters/theory/koszul_pair_structure.tex | sed -n '95,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '60,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '824,834p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '581,608p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   824	 $K = 0$ for Heisenberg and affine Kac--Moody at the linear
   825	 level, $K = 13$ for Virasoro (self-dual at $c = 13$), with
   826	 family-dependent nonzero values for the principal
   827	 $\mathcal{W}$-algebras
   828	 (Theorem~\ref{thm:central-charge-complementarity}). The
   829	 sum rule is a family-specific holographic conservation law,
   830	 not a universal constant. Theorem~C part~(1) (eigenspace
   831	 decomposition under the Verdier involution) is
   832	 unconditional; part~(2) (scalar sum rule) is proved on the
   833	 uniform-weight lane.
   834	
 succeeded in 53ms:
    60	
    61	Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
    62	tests and consequences around chiral Koszulness. Nine are
    63	unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
    64	vanishing of transferred $A_\infty$ operations $m_k$ for
    65	$k \geq 3$, acyclicity of the twisted tensor product
    66	$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
    67	$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
    68	duality and concentration in degrees $\{0,1,2\}$) is a proved
    69	consequence on the Koszul locus. One (the Lagrangian
    70	eigenspace decomposition) is conditional on perfectness of the
    71	bar-cobar normal complex. One (D-module purity) is a
    72	one-directional implication. The count is exact:
    73	$9 + 1 + 1 + 1$.
    74	
    75	Two distinctions require emphasis. First, the four complexity
    76	classes G/L/C/M, with shadow depths
    77	$\{2, 3, 4, \infty\}$
    78	(Theorem~\ref{thm:shadow-archetype-classification}), record the
    79	degree at which the shadow obstruction tower first becomes
 succeeded in 53ms:
   581	\item \emph{Theorem~C} (Deformation-obstruction complementarity,
   582	 Theorem~\ref{thm:quantum-complementarity-main}).
   583	 The \emph{center local system} $\mathcal{Z}_\cA$ is the
   584	 local system on $\overline{\cM}_g$ whose fibre over a
   585	 smooth curve $[\Sigma_g]$ is the center
   586	 $Z(\cA|_{\Sigma_g})$ (the commutant of~$\cA$ acting on
   587	 itself via the chiral bracket).
   588	 The \emph{ambient complex}
   589	 $\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g,
   590	 \mathcal{Z}_\cA)$
   591	 (derived global sections of this local system)
   592	 carries a shifted-symplectic pairing from Verdier duality.
   593	 The Verdier involution decomposes it
   594	 into \emph{complementary Lagrangians}
   595	 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$:
   596	 the $+1$ and $-1$ eigenspaces of the involution
   597	 (Definition~\ref{def:complementarity-complexes}).
   598	 At the cohomological level,
   599	 \begin{equation}\label{eq:complementarity-intro}
   600	 Q_g(\cA) \oplus Q_g(\cA^!) \cong
 succeeded in 53ms:
    95	$\barB_g(\cA)$ now lives on $\overline{\mathcal{M}}_g$, and the
    96	fiberwise differential $\dfib$ becomes \emph{curved}:
    97	\[
    98	 \dfib^2 = \kappa \cdot \omega_g \neq 0,
    99	\]
   100	where $\kappa = \kappa(\cA)$ is the modular characteristic (Theorem~D) and $\omega_g \in H^2(\overline{\mathcal{M}}_g)$
   101	is the Hodge class. The differential is no longer a differential; it squares to a curvature term controlled by $\kappa$.
   102	
   103	The total corrected differential $\Dg{g}$ absorbs the curvature into a higher-order correction, a curved $A_\infty$-structure in which $m_0 \neq 0$ and $m_1^2(a) = [m_0, a]$, and satisfies $\Dg{g}^2 = 0$. The passage from $\dzero$ to $\Dg{g}$ is the passage from classical to quantum: the quantum corrections are controlled by $H^*(\overline{\mathcal{M}}_g, Z(\cA))$, and Theorem~B (Theorem~\ref{thm:higher-genus-inversion}) shows that bar-cobar inversion persists via $E_2$~collapse of the associated spectral sequence. Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) identifies the obstruction and deformation spaces as Lagrangian complements.
   104	
   105	\begin{remark}[Three levels of Koszul pair]\label{rem:three-koszul-levels}
   106	\index{Koszul pair!comparison of levels}
   107	The construction above exhibits three levels of structure, each
   108	strictly refining the previous:
   109	\begin{enumerate}[leftmargin=2em]
   110	\item \textbf{Classical} (Definition~\ref{def:koszul-pair-classical}).

thinking
**Evaluating conditionality in structures**

I'm noticing some issues with the condition outlined for eigenspace decomposition in volume I, particularly regarding `chiral_koszul_pairs`. Additionally, `koszul_pair_structure` seems to overemphasize certain aspects. It looks like there's a need to check the theorem that identifies obstruction and deformation as Lagrangian complements without considering the condition. The user is asking about a bridge audit, so I want to ensure that I check volume II for any misstatements and inspect specific lines for clarity.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex | sed -n '1425,1432p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex | sed -n '1828,1838p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex | sed -n '1104,1116p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex | sed -n '1118,1126p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex | sed -n '1218,1224p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1218	 \emph{Shadow depth classification and complementarity.}
  1219	 The four-class partition G/L/C/M of Koszul algebras by shadow
  1220	 depth, the complementarity theorem
  1221	 (Theorem~\ref{thm:quantum-complementarity-main}), and the
  1222	 Lagrangian geometry of the ambient complex are algebraic
  1223	 structures that do not arise in the perturbative framework.
  1224	
 succeeded in 53ms:
  1828	\ClaimStatusProvedHere]
  1829	% label removed: thm:thqg-III-landscape-census
  1830	For each standard family, the hypotheses
  1831	\textup{(H1)} perfectness and \textup{(H2)} nondegeneracy
  1832	of Theorem~\textup{\ref{thm:thqg-III-lagrangian-polarization}}
  1833	are satisfied. The eigenspace decomposition \textup{(C1)} and
  1834	the shifted-symplectic Lagrangian structure \textup{(C2)} both
  1835	hold. The shadow depth classes are:
  1836	
  1837	\begin{center}
  1838	\renewcommand{\arraystretch}{1.3}
 succeeded in 53ms:
  1104	\begin{remark}[Conditionality of (C2)]
  1105	% label removed: rem:thqg-III-conditionality
  1106	\index{complementarity!conditionality}
  1107	Hypotheses (H1) and (H2) are substantive. Perfectness
  1108	requires PBW filterability and finite-dimensional fiber
  1109	cohomology (Lemma~\ref{V1-lem:perfectness-criterion}).
  1110	Nondegeneracy of the Verdier pairing is verified family
  1111	by family
  1112	(Proposition~\ref{V1-prop:standard-examples-modular-koszul}).
  1113	Both hold for the entire standard landscape
  1114	(\S\ref{V1-subsec:thqg-III-standard-landscape}). The C1
  1115	eigenspace decomposition is strictly weaker, requiring
  1116	only $\sigma^2 = \id$, and holds unconditionally.
 succeeded in 53ms:
  1425	\item \emph{Modular characteristic~$\kappa$ and complementarity.}
  1426	 The universal invariant~$\kappa(\cA_T)$, its duality
  1427	 constraints (Theorem~\ref{thm:modular-characteristic}),
  1428	 and the complementarity theorem
  1429	 (Theorem~\ref{thm:quantum-complementarity-main}) are
  1430	 algebraic structures not visible from perturbative gauge
  1431	 theory.
  1432	\end{enumerate}
 succeeded in 53ms:
  1118	HS-sewing convergence
  1119	 & ---
  1120	 & \checkmark\;Thm~\ref{thm:general-hs-sewing} \\
  1121	Complementarity (Thm~C)
  1122	 & ---
  1123	 & \checkmark\;Thm~\ref{thm:quantum-complementarity-main} \\[4pt]
  1124	\multicolumn{3}{@{}l}{\emph{Duality and structure}} \\[2pt]
  1125	BV quantization framework
  1126	 & \checkmark\;\cite{CG17}

thinking
**Searching for mathematical references**

I’m looking into Volume II on holomorphic topology, which mentions theorem C but isn’t specific, so it might not be a major issue. I should check Volume III regarding the modular Koszul bridge for C2 conditional propagation in the d3 conjecture. Let’s investigate more around the d3 theorem to gather necessary insights. It feels like there’s a lot to uncover here, so I want to get it right!
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '100,230p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   100	%% ===================================================================
   101	
   102	\section{CY complementarity}
   103	\label{sec:cy-complementarity-bridge}
   104	
   105	Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
   106	\[
   107	 \kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) \;=\; \rho \cdot K,
   108	\]
   109	where $K$ is the Koszul conductor and $\rho$ the anomaly ratio; this holds only on the \emph{uniform-weight lane} (all generators of $A$ of equal conformal weight), and at $g \geq 2$ multi-weight algebras incur a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$. This section transports both statements to CY categories via the functor $\Phi$.
   110	
   111	\subsection{The $d = 2$ theorem}
   112	
   113	\begin{theorem}[CY complementarity at $d = 2$]
   114	\label{thm:cy-complementarity-d2}
   115	\ClaimStatusProvedHere
   116	Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d = 2$ with Serre duality $\mathbb{S}_\cC \simeq [2]$, and let $A_\cC = \Phi(\cC)$ be its quantum chiral algebra (CY-A at $d = 2$, PROVED). Let $\cC^!$ denote the Koszul dual CY$_2$ category (for $\cC = D^b(\Coh(X))$ with $X$ a K3 surface, $\cC^! \simeq \Fuk(X)$ under homological mirror self-duality). Then:
   117	\begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}}$)}]
   118	 \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies
   119	 \[
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem C2|Theorem~C\\"'$_2'"\\"'$|Vol~I Theorem~C'"\\"'$_2'"\\"'$|Vol I Theorem C2|C2'"\\"'^'"\\{CY\\}|C1\\"'^'"\\{CY\\}|Theorem~C has two components|scalar complementarity|shifted-symplectic\" /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:105:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:183:When $\kappa_{\mathrm{ch}}(A_\cC)$ vanishes (banana manifold, Heisenberg at level $k = 0$, Virasoro at $c = 0$; see \S\ref{subsec:banana-manifold}), the free-field/KM branch of the scalar complementarity forces the Koszul-dual characteristic $\kappa_{\mathrm{ch}}'$ to vanish likewise, but this does \emph{not} imply $\Theta_{A_\cC}$ vanishes. Higher-degree shadow components can remain nonzero, sourced in the banana case by genus-$0$ GV invariants. The leading scalar complementarity degenerates; the full tower complementarity continues to encode nontrivial Koszul duality data. Note: the Virasoro-at-$c=0$ example sits on the free-field boundary of the $c = 13$ self-dual Virasoro family, where the generic scalar sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$; $c = 0$ is the exceptional point of that family.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:484:    """Compute the scalar complementarity defect at genus g.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:943:        The scalar complementarity defect VANISHES at all genera.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:1137:    The scalar complementarity defect:

thinking
**Inspecting modular issues**

I’m focusing on a major issue in vol3 related to the modular_koszul_bridge. I think it might be helpful to inspect volume II to check for any potential misuse of C2 as a scalar sum. To dig deeper, I plan to search for “Theorem C2” or look into the scalar part of C2. This could clarify the situation and help me resolve the problem!
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem C2|Theorem~C\\"'$_2'"\\"'$|part~C2|scalar part.*C2|scalar sum.*C2|Vol~I Theorem~C2|Theorem C has two components|Theorem~C part~'"\\(2\\)|part~\\(2\\) \\(scalar|C2\\).*scalar\" /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:362:are unconditional; Theorem~D and the scalar part C2 of Theorem~C
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:26:- **MODERATE -- "Theorem C2" is cited as a Vol I input (line 268--277).** The preface says "Theorem~D and the scalar part~C2 of Theorem~C are tagged uniform-weight." This is AP32-compliant tagging: every occurrence of obs_g, F_g, lambda_g downstream "inherits the explicit tag from its Vol~I source." Good. No violation here -- logging as a positive finding that AP32 was properly absorbed.

thinking
**Inspecting scalar part**

I’m looking into the preface of vol2, where it mentions the scalar part, C2, of Theorem C. I have a hunch that it might be incorrect if the canonical C2 is supposed to be shifted-symplectic. It feels like I need to dig deeper and really inspect this further to clarify things. There’s definitely something interesting to unravel here! I wonder what the implications of this could be.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex | sed -n '356,368p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   356	
   357	\section*{VII.\quad The Vol~I engine}
   358	
   359	Volume~I is Koszul duality on a curve: the bar construction for
   360	chiral algebras on an algebraic curve~$X$, with five main
   361	theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
   362	are unconditional; Theorem~D and the scalar part C2 of Theorem~C
   363	carry uniform-weight scope at $g \ge 2$, with a cross-channel
   364	correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
   365	regime. Three structure theorems organise the
   366	representation-theoretic content: \emph{algebraicity}
   367	($H(t)^2 = t^4 Q_L(t)$, shadow generating function algebraic of
   368	degree~$2$); \emph{formality identification}, where the shadow

thinking
**Revising audit notes**

I realize that the audit note was misjudged and needs to be included. Vol2 states there’s no violation, but I’m not sure it’s the right source; I could ignore the notes, but they might be relevant as evidence. I think I should search more in volume I for sections misnumbered, specifically looking into "scalar part C2" and checking volumes I, II, and III for related information.
exec
/bin/zsh -lc "rg -n --no-heading \"scalar part C2|scalar statement \\(C2\\)|Theorem~C has two components|part~\\(2\\) \\(scalar sum rule\\)|Vol~I Theorem~C\\"'$_2'"\\"'$|Theorem~C part~'"\\(2\\).*scalar|scalar complementarity \\(C2|C2\\"'$'"\\"'^'"\\{|Theorem C2\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | head -n 300" in /Users/raeez/chiral-bar-cobar succeeded in 78ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:362:are unconditional; Theorem~D and the scalar part C2 of Theorem~C
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:105:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:476:/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/D02_scope_inflation.md:828:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:26:- **MODERATE -- "Theorem C2" is cited as a Vol I input (line 268--277).** The preface says "Theorem~D and the scalar part~C2 of Theorem~C are tagged uniform-weight." This is AP32-compliant tagging: every occurrence of obs_g, F_g, lambda_g downstream "inherits the explicit tag from its Vol~I source." Good. No violation here -- logging as a positive finding that AP32 was properly absorbed.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U05_stub_chapters_v3.md:665:chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S06_intro_to_body.md:784:   832	 unconditional; part~(2) (scalar sum rule) is proved on the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:832: unconditional; part~(2) (scalar sum rule) is proved on the
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F04_kappa_WN.md:928:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F18_complementarity.md:274:/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F18_complementarity.md:1829:   105	Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:15:- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:433](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:433) — The live manuscript no longer defines C2 as a scalar BV pairing. It defines C2 as the conditional bar-side BV / shifted-symplectic upgrade and explicitly says the scalar complementarity formulas are consequences of C1 plus Theorem D, “not a separate C2 label” ([higher_genus_complementarity.tex:441](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:441)). So the requested “Theorem C2: scalar BV pairing (conditional on uniform-weight)” is already off the current theorem surface.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:70:MISSION: FALSIFY the proof of Theorem C2: scalar BV pairing (conditional on uniform-weight). Check: (a) what is the condition? (b) does uniform-weight actually suffice? (c) what fails at multi-weight? (d) is the delta_F_g^cross correction properly scoped?
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:83:Using `deep-beilinson-audit` for this turn because the task is an adversarial proof audit, not a local formula check. I’ll lock the theorem surface first by locating Theorem C2 and reading the constitutional files that govern status, scope, and known drift before I inspect the statement and proof.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:89:/bin/zsh -lc "pwd && rg -n \"Theorem C2|thm:C2|scalar BV pairing|uniform-weight|delta_F_g\\"'^cross|delta_F_g|BV pairing" chapters metadata CLAUDE.md /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar/raeeznotes/raeeznotes100/red_team_summary.md /Users/raeez/chiral-bar-cobar/archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:197:/bin/zsh -lc "rg -n \"scalar BV pairing|scalar.*BV pairing|BV pairing.*scalar|Theorem C2|C2\\b|uniform-weight.*BV|delta F_g\\"'^'"\\{\\\\mathrm\\{cross\\}\\}|delta F_g\\"'^cross|cross-channel correction|multi-weight-genus-expansion|genus-universality|quantum-complementarity-main|minimal scalar package" chapters/theory chapters/connections chapters/frame' in /Users/raeez/chiral-bar-cobarexec
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:200:    (?:scalar BV pairing|scalar.*BV pairing|BV pairing.*scalar|Theorem C2|C2\b|uniform-weight.*BV|delta F_g\^\{\mathrm\{cross\}\}|delta F_g\^cross|cross-channel correction|multi-weight-genus-expansion|genus-universality|quantum-complementarity-main|minimal scalar package)
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:301:I’m realizing that the search results aren't sufficient. I need to look more specifically for "C2," possibly related to enumerating subtheorems. There might be a theorem called "thm:mc2-full-resolution" in an editorial constitution. My main focus is on the proof of Theorem C2 regarding scalar BV pairing, assuming uniform weight. I should search for references to "C2:" or "scalar BV pairing" and delve deeper into the relevant files and metadata.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T05_thm_C2.md:304:/bin/zsh -lc 'rg -n "C2[''^A-Za-z]|Theorem~C2|Theorem C2|scalar BV|BV pair|uniform-weight[''^'"\\n]{0,40}conditional|conditional on uniform-weight|minimal scalar package|cross-channel correction\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex chapters/frame/guide_to_main_results.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem C|quantum-complementarity|Complementarity \\(Theorem~C\\)|Vol I Theorem C|Theorem~C\\)|Theorem~C\" /Users/raeez/calabi-yau-quantum-groups/chapters | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:234:Theorem~CY-D (Theorem~\ref{thm:cy-modular-characteristic}) when
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:527:$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for KM/free fields (Volume~I, Theorem~C).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:400:\emph{Theorem~C} (Vol~I, complementarity): $\mathrm{obs}_g(U_{q,t}) + \mathrm{obs}_g(U_{q^{-1},t^{-1}})$ controlled by $H^*$ of a framed moduli space (the $\Eone$ replacement for $\overline{\mathcal{M}}_g$; cf.\ Vol~I, Remark~\ref{rem:yangian-three-theorems}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4853: \item \textbf{(Conjecture.)} There exists a chiral algebra $A_{K3 \times E} = \Phi(D^b(\mathrm{Coh}(X)))$ whose bar complex $B(A)$ encodes the product formula for $\Delta_5$. \emph{Note}: the functor $\Phi$ is constructed for $d = 2$ (Theorem~CY-A$_2$); the $d = 3$ case (which applies here, since $K3 \times E$ is CY$_3$) is the content of Conjecture~CY-A$_3$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:139: \item The functor $\Phi$ (Theorem~CY-A$_2$) produces an
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:158:Item (ii): Theorem~CY-A$_2$ applies since $d = 2$ and the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:164:Theorem~CY-D (Theorem~\ref{thm:cy-modular-characteristic}),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:367:(matching the abstract construction of Theorem~CY-A):
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:33:The CY dimension of $\MF(W)$ is $n - 2$, not $n - 1$. The shift by two arises from the $\Z/2$-grading: the ambient $n$-dimensional affine space is traded for the $(n-1)$-dimensional critical locus, and a further shift comes from the Serre functor of the periodic category. Consequently ADE singularities in $n = 2$ variables give CY$_0$ (semisimple) categories, and one needs $n = 4$ variables to obtain a CY$_2$ category accessible to the Vol~III functor $\Phi$ of Theorem~CY-A$_2$ (Section~\ref{sec:cy-chiral-functor}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:67:a two-dimensional $\Z/2$-graded Clifford algebra on one generator. The Jacobi ring is $\Jac(x^2) = \C[x]/(2x) \cong \C$, so $\HH_\bullet(\MF(x^2)) \cong \C$ is one-dimensional; the two-dimensional endomorphism algebra counts the $\Z/2$-graded indecomposable and its parity shift. The dimension count $2$ is the rank count of the free-fermion representation: a single holomorphic fermion contributes a two-dimensional Clifford sector, and this is the smallest nonzero input to the LG-to-chiral passage at the level of Hochschild invariants. The $n = 1$ case sits outside the CY$_2$ domain of Theorem~CY-A$_2$ (Remark~\ref{rem:mf-dim-caveat}) and is used only as the building block for the stabilized four-variable model in Section~\ref{sec:ade-w-algebras}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:72:Let $W \colon \C^4 \to \C$ have an isolated critical point at the origin. By Theorem~\ref{thm:mf-cy-dimension} the category $\MF(W)$ is CY$_2$, hence Theorem~CY-A$_2$ applies and produces a chiral algebra
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:81:Theorem~CY-A$_2$ (Section~\ref{sec:cy-chiral-functor}) applies to any smooth proper CY$_2$ category. The value $\kappa_{\mathrm{ch}} = \chi(\HH_\bullet)$ is the CY Euler characteristic clause of that theorem; Theorem~\ref{thm:mf-hh} identifies $\HH_\bullet$ with $\Jac(W)$ placed in a single parity, whose Euler characteristic is the $\C$-dimension of the Jacobi ring, namely $\mu(W)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:99:Let $W$ be a homogeneous polynomial of degree $n + 1$ in $n + 1$ variables with smooth projective zero locus $Q \subset \mathbf{P}^n$. Assume Theorem~CY-A$_3$ (the $d = 3$ CY-to-chiral functor). Then
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:108:Orlov's theorem is an equivalence of CY$_3$ dg-categories; the functor $\Phi$ of Theorem~CY-A$_3$ (should it exist) depends only on the CY dg-equivalence class of its input. The two sides agree as inputs, so their images under $\Phi$ agree. The modular characteristic equality follows from the CY Euler characteristic clause of Theorem~CY-A$_3$ (Section~\ref{sec:cy-chiral-functor}), which depends only on $\HH_\bullet$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:113:Theorem~CY-A$_3$ is a programme, not a theorem: the chain-level $\bS^3$-framing and global existence of $A_X$ for a compact CY$_3$ are open. Proposition~\ref{prop:lg-cy-matching} therefore carries \texttt{ClaimStatusConditional} with CY-A$_3$ as its named dependency. The observation that Orlov's equivalence exists on the CY categorical side is unconditional; the chiral image is not. For the quintic the two sides of the correspondence are the LG source $\MF^{\gr}(W_{\mathrm{quintic}})_0$ and the CY source $D^b(\Coh(Q))$ studied in the sister chapter~\ref{ch:derived-cy}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:130:To obtain a CY$_2$ input for Theorem~CY-A$_2$ one stabilizes by adding two quadratic variables:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:138:where $\mathrm{Cl}_2$ is the $\Z/2$-graded Clifford algebra on two generators; the dimension count in Theorem~\ref{thm:mf-cy-dimension} becomes $n - 2 = 2$, so $\MF(\widetilde{W}_{\mathrm{ADE}})$ is CY$_2$ and $\Phi$ of Theorem~CY-A$_2$ applies.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:154:The ADE prediction sits in the image of Theorem~CY-A$_2$, hence the $d = 2$ case where $\Phi$ is proved. What prevents stating it as a theorem is not the functor but the identification of the output with a named $\cW$-algebra: we have no intrinsic construction of $\cW_k(\mathfrak{g})$ from $\HH_\bullet(\MF(\widetilde{W}_{\mathrm{ADE}}))$, only a matching of the modular characteristic and a physical argument for the full structure. Conjecture~\ref{conj:ade-w-algebra} is therefore stated as a prediction, not a proved theorem, in line with AP-CY14.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:171:the $\Z/2$-graded category of finite-dimensional vector spaces (the Morita equivalence $\mathrm{Cl}_4 \simeq \C$ removes the Clifford factor because $\mathrm{Cl}_4 \cong M_2(\C)$ as a $\Z/2$-graded algebra, and $M_2(\C)$ is Morita trivial). Theorem~\ref{thm:mf-cy-dimension} places $\MF(\widetilde{W}_{A_1})$ in dimension $2$, matching the CY$_2$ hypothesis of Theorem~CY-A$_2$.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex | sed -n '532,566p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   532	\end{example}
   533	
   534	
   535	\section{Braided complementarity}
   536	\label{sec:braided-complementarity}
   537	
   538	Vol~I Theorem~C establishes complementarity:
   539	$\kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) = K$
   540	(the Koszul conductor, family-dependent). The $\Etwo$-refinement
   541	upgrades this scalar relation to an $R$-matrix-level statement.
   542	
   543	\begin{conjecture}[Braided complementarity]
   544	\label{conj:braided-complementarity}
   545	\ClaimStatusConjectured
   546	For an $\Etwo$-chiral algebra $\cA$ on the Koszul locus, the braided
   547	Koszul dual $\cA^!_{E_2}$ satisfies:
   548	\begin{enumerate}[label=(\roman*)]
   549	 \item \emph{Scalar complementarity}:
   550	 $\kappa_{\mathrm{cat}}(\cA) + \kappa_{\mathrm{cat}}(\cA^!_{E_2}) = K$,
   551	 the family-dependent Koszul conductor (Vol~I, Theorem~C);
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '434,444p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '444,448p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   444	$\sigma$ exchanging the two eigenspaces; at the scalar level
   445	the complementarity formulas below are consequences of the
   446	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   447	separate $\mathrm{C}_2$ label:
   448	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,

thinking
**Organizing theorem details**

I need to gather the canonical lines from 40 to 98, and I'll probably need to include citations for those. I'm also thinking about adding a theorem label for the shifted-symplectic complementarity. I'll make sure to inspect the line numbers around 1899 as well. It feels like I have a good plan in place, but I'm keen to ensure all details are accurate and nothing is overlooked!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1890,1908p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1890	Lagrangian polarization at the level of cohomology, and
  1891	Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
  1892	proved shifted-symplectic statement on the ambient complex~$C_g$. The
  1893	direct bar-side realization of a $(-1)$-shifted symplectic chart on
  1894	$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
  1895	Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
  1896	upgrade conditionally.
  1897	
  1898	\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
  1899	\label{thm:shifted-symplectic-complementarity}
  1900	\index{shifted symplectic!(-1)-shifted|textbf}
  1901	\index{Lagrangian!complementarity!shifted symplectic|textbf}
  1902	\textup{[Regime: curved-central on the Koszul locus; all genera
  1903	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1904	
  1905	Assume the conditional BV package of
  1906	Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
  1907	genus-$1$ complementarity
  1908	$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
exec
/bin/zsh -lc "rg -n --no-heading \"Theorem~C.*Lagrangian|Theorem~C \\(Theorem~\\\\ref\\{thm:quantum-complementarity-main\\}\\).*Lagrangian|Lagrangian complements|shifted-symplectic pairing from Verdier duality|eigenspace decomposition\\) is conditional on perfectness|Theorem~C part~\\(1\\)|part~\\(2\\) \\(scalar sum rule\\)|Theorem~C has three named pieces\" chapters/theory chapters/connections chapters/examples appendices | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:9745:shifted-symplectic pairing from Verdier duality, and the deformation
chapters/theory/computational_methods.tex:1325:Theorem~C (complementarity): the Lagrangian decomposition
chapters/theory/introduction.tex.bak:807:  carries a shifted-symplectic pairing from Verdier duality.
chapters/theory/chiral_koszul_pairs.tex:70:eigenspace decomposition) is conditional on perfectness of the
chapters/theory/higher_genus_complementarity.tex:436:Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
chapters/theory/higher_genus_complementarity.tex:543:as Lagrangian complements.
chapters/theory/introduction.tex:382:\emph{Decomposition}: Theorem~C splits the genus-$g$ projection into complementary Lagrangians.
chapters/theory/introduction.tex:592: carries a shifted-symplectic pairing from Verdier duality.
chapters/theory/introduction.tex:830: not a universal constant. Theorem~C part~(1) (eigenspace
chapters/theory/introduction.tex:832: unconditional; part~(2) (scalar sum rule) is proved on the
chapters/theory/koszul_pair_structure.tex:103:The total corrected differential $\Dg{g}$ absorbs the curvature into a higher-order correction, a curved $A_\infty$-structure in which $m_0 \neq 0$ and $m_1^2(a) = [m_0, a]$, and satisfies $\Dg{g}^2 = 0$. The passage from $\dzero$ to $\Dg{g}$ is the passage from classical to quantum: the quantum corrections are controlled by $H^*(\overline{\mathcal{M}}_g, Z(\cA))$, and Theorem~B (Theorem~\ref{thm:higher-genus-inversion}) shows that bar-cobar inversion persists via $E_2$~collapse of the associated spectral sequence. Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) identifies the obstruction and deformation spaces as Lagrangian complements.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '374,386p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   374	(Theorem~\ref{thm:mc2-bar-intrinsic}); since
   375	$(D_\cA^{\Eone})^2 = 0$, the MC equation
   376	$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
   377	is automatic. Averaging into~$\gAmod$ produces the
   378	$\Sigma_n$-invariant content: the five theorems characterize five
   379	structural properties of this projection.
   380	\emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
   381	\emph{Faithfulness}: Theorem~B shows $\Theta_\cA$ determines~$\cA$.
   382	\emph{Decomposition}: Theorem~C splits the genus-$g$ projection into complementary Lagrangians.
   383	\emph{Leading coefficient}: Theorem~D extracts the universal scalar~$\kappa(\cA)$.
   384	\emph{Coefficient ring}: Theorem~H identifies $\ChirHoch^*(\cA)$ as the finite-dimensional space over which~$\Theta_\cA$ varies.
   385	The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
   386	$\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
codex
I’ve confirmed the main logical drift, not just a wording drift: live bridge files are treating `C2` as the scalar `κ + κ^!` rule, while the canonical Vol I theorem surface defines `C2` as the conditional bar-side shifted-symplectic upgrade. I’m collecting the exact downstream files where that false decomposition is still live, plus the compute/docstring surfaces that inherit the same bad citation.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex | sed -n '538,565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex | sed -n '359,364p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex | sed -n '214,222p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '40,100p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"Theorem C.*kappa|kappa-complementarity|rho\\*K|Theorem C bridge|At the scalar level|scalar complementarity|Vol I Theorem C for Koszul pairs|Theorem C establishes complementarity\" /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/chiral-bar-cobar-vol2/chapters | head -n 120" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading \"Theorem C.*kappa|kappa-complementarity|scalar complementarity|Vol I Theorem C for Koszul pairs|Theorem C establishes complementarity|Theorem C \\(complementarity\\)\\.\" /Users/raeez/calabi-yau-quantum-groups/compute /Users/raeez/calabi-yau-quantum-groups/chapters | head -n 120" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   359	Volume~I is Koszul duality on a curve: the bar construction for
   360	chiral algebras on an algebraic curve~$X$, with five main
   361	theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
   362	are unconditional; Theorem~D and the scalar part C2 of Theorem~C
   363	carry uniform-weight scope at $g \ge 2$, with a cross-channel
   364	correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 succeeded in 52ms:
    40	Theorem~C decomposes into three layers
    41	with distinct logical statuses.
    42	\begin{enumerate}[label=\textup{(C\arabic*)},start=0]
    43	\item \emph{Fiber--center identification
    44	 \textup{(}unconditional on the Koszul locus\textup{)}.}\;
    45	 For every chiral algebra~$\cA$ carrying a modular pre-Koszul datum
    46	 with finite-dimensional fiber cohomology, the relative bar family
    47	 satisfies $R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0$ for $q \neq 0$,
    48	 with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
    49	 \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
    50	 This produces the ambient complex on which~\textup{(C1)}
    51	 and~\textup{(C2)} operate.
    52	
    53	\item \emph{Eigenspace decomposition \textup{(}unconditional on the
    54	 Koszul locus\textup{)}.}\;
    55	 For every chiral Koszul pair $(\cA, \cA^!)$ on a smooth projective
    56	 curve~$X$ and every genus $g \geq 0$, the cohomology of the ambient
    57	 complex splits as
    58	 \begin{equation}\label{eq:complementarity-summary}
    59	 H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
 succeeded in 53ms:
   538	Vol~I Theorem~C establishes complementarity:
   539	$\kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) = K$
   540	(the Koszul conductor, family-dependent). The $\Etwo$-refinement
   541	upgrades this scalar relation to an $R$-matrix-level statement.
   542	
   543	\begin{conjecture}[Braided complementarity]
   544	\label{conj:braided-complementarity}
   545	\ClaimStatusConjectured
   546	For an $\Etwo$-chiral algebra $\cA$ on the Koszul locus, the braided
   547	Koszul dual $\cA^!_{E_2}$ satisfies:
   548	\begin{enumerate}[label=(\roman*)]
   549	 \item \emph{Scalar complementarity}:
   550	 $\kappa_{\mathrm{cat}}(\cA) + \kappa_{\mathrm{cat}}(\cA^!_{E_2}) = K$,
   551	 the family-dependent Koszul conductor (Vol~I, Theorem~C);
   552	 \item \emph{$R$-matrix inversion}:
   553	 $\cR_{\cA^!_{E_2}}(z) = \cR_\cA(z)^{-1}$ as formal power series
   554	 in $z^{-1}$, so the braided Koszul dual reverses the braiding;
   555	 \item \emph{Conductor from $R$-matrix}:
   556	 the Koszul conductor $K$ is recovered from the $R$-matrix
   557	 as $K = \mathrm{av}(\cR_\cA(z)) + \mathrm{av}(\cR_\cA(z)^{-1})$.
 succeeded in 52ms:
   214	\begin{description}
   215	 \item[Theorem A (adjunction).] The bar-cobar adjunction $B \dashv \Omega$ restricts to CY chiral algebras: $B(A_\cC)$ is a factorization coalgebra on $\Ran(X)$, and $D_{\Ran}(B(A_\cC)) \simeq B(A_{\cC^!})$. The CY identification CY-A(ii) gives $\mathrm{CC}_\bullet(\cC) \simeq B(A_\cC)$.
   216	
   217	 \item[Theorem B (inversion).] Bar-cobar inversion $\Omega(B(A_\cC)) \xrightarrow{\sim} A_\cC$ holds on the Koszul locus. For CY categories, chirally Koszul is equivalent to the formality of $\mathrm{CC}_\bullet(\cC)$ as a dg coalgebra.
   218	
   219	 \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
   220	
   221	 \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
   222	
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:147:Proposition~\ref{prop:kappa-cat-chi-cy} allows the scalar complementarity (C2$^{\mathrm{CY}}$) to be restated on the categorical side. The \emph{CY Koszul conductor} is
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:183:When $\kappa_{\mathrm{ch}}(A_\cC)$ vanishes (banana manifold, Heisenberg at level $k = 0$, Virasoro at $c = 0$; see \S\ref{subsec:banana-manifold}), the free-field/KM branch of the scalar complementarity forces the Koszul-dual characteristic $\kappa_{\mathrm{ch}}'$ to vanish likewise, but this does \emph{not} imply $\Theta_{A_\cC}$ vanishes. Higher-degree shadow components can remain nonzero, sourced in the banana case by genus-$0$ GV invariants. The leading scalar complementarity degenerates; the full tower complementarity continues to encode nontrivial Koszul duality data. Note: the Virasoro-at-$c=0$ example sits on the free-field boundary of the $c = 13$ self-dual Virasoro family, where the generic scalar sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$; $c = 0$ is the exceptional point of that family.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:219: \item[Theorem C (complementarity).] The CY Euler characteristic $\chi(\cC)$ splits into complementary halves: $Q_g(\cC) + Q_g(\cC^!)$ recovers the full Hochschild cohomology.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:255: \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:484:    """Compute the scalar complementarity defect at genus g.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:943:        The scalar complementarity defect VANISHES at all genera.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/entropy_koszul_complement_cy3.py:1137:    The scalar complementarity defect:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/fukaya_shadow_tower.py:1942:    from Vol I Theorem C for Koszul pairs.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_bar_complex_engine.py:523:    Theorem CY-D: kappa(A_C) = chi^CY(C).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy_bar_complex_engine.py:535:        of the CATEGORY. Theorem CY-D equates kappa(A_C) = chi^CY(C),
/Users/raeez/calabi-yau-quantum-groups/compute/lib/modular_cy_characteristic.py:27:  Theorem CY-D: kappa(A_C) = chi^CY(C) when A_C is the chiral algebra
/Users/raeez/calabi-yau-quantum-groups/compute/lib/modular_cy_characteristic.py:201:    Theorem CY-D: kappa(A_C) = chi^CY(C).
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:13:However, several CRITICAL and SERIOUS issues hide in the substance. The preface uses `\HH_\bullet(\cC) \to k[-d]` (line 21-22) for the CY trace, directly violating AP-CY2 (CY trace lives in HC^-_d, negative cyclic, not Hochschild homology). The modular characteristic identity `\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)` (line 28) is asserted in the preface but is exactly the content of Theorem CY-D, which is labelled PROGRAMME in CLAUDE.md (d=3 conditional on A_C existing). The "six independent paths" verification of `\kappa_{\mathrm{ch}}(K3 x E) = 3` is asserted without citation and would fail AP10 if queried. The CoHA paragraph declares CoHA "the ordered bar complex of the CY_3 chiral algebra" -- but the CY_3 chiral algebra is exactly the object that does not yet exist (AP-CY6), so this is an unconstructed-object assertion in a preface posing as theorem. The `\C^3 -> W_{1+infty} -> Rep^{E_2}(Y(gl_1-hat))` chain is claimed "verified end-to-end" with no citation.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:31:  This is asserted in preface-voice. But A_C for CY_3 is exactly the d=3 programme (AP-CY6: "A_X for CY3 does NOT exist"). CLAUDE.md marks CY-A (existence of Phi) as "d=2 PROVED; d=3 PROGRAMME" and CY-D (modular characteristic) as "PROGRAMME". The preface then tries to fix this at line 62-64 by saying "Theorem CY-A constructs Phi for d=2: all three steps are proved. For d=3, step (3) is a programme..." But this is inconsistent: lines 28-30 have already asserted kappa_ch(A_C) and shadow/automorphic identification for the d=3 case (since the following paragraph is about K3 x E, a CY_3). The scope disclaimer arrives 35 lines too late.
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cy_euler.py:5:  chapters/theory/modular_trace.tex (Theorem CY-D: kappa(A_C) = chi^CY(C)),
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/compute/remaining_families_ordered_bar.py:503:        # At the scalar level (vacuum expectation): ⟨J⟩ = 0
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:231:    This is the rho*K constant for W_3 (Theorem C).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:261:    """Verify kappa(A) + kappa(A!) = rho*K (Theorem C).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:263:    For Kac-Moody and free fields: rho*K = 0.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/bulk_boundary_duality_engine.py:264:    For W-algebras: rho*K = constant depending only on the algebra type.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/modular_obstruction_engine.py:1070:        kappa(A) + kappa(A!) = rho*K  (for W-algebras)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/modular_obstruction_engine.py:1073:        Ob_1(A) + Ob_1(A!) = 0 or rho*K*omega_1
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:350:        # At the scalar level: amplitude = F_1 * kappa * propagator = (kappa/24) * kappa * (1/kappa)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:354:        # Sh_2^{(1)} is the genus-1 bilinear form. At the scalar level, Sh_2^{(1)} = kappa
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:374:        # At the scalar level: amplitude = F_1 * propagator * F_1
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:390:        # At the scalar level: amplitude = Sh_4^{(0)} * P^2
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:460:    At the scalar level on the 1D primary line:
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:492:      propagator. At the scalar level:
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:497:      At the scalar level:
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:587:    theta_2 = F_2  # At the scalar level, Theta_2 = F_2
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:786:    At the scalar level on the 1D primary line:
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_obstruction_engine.py:1004:    At the scalar level (free energy):
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:14:  - kappa-complementarity: kappa(A) + kappa(A!) is level-independent (Theorem C)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:453:# Kappa values and complementarity (Theorem C bridge)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:492:    """Verify kappa-complementarity: kappa(A) + kappa(A!) is level-independent.




thinking
**Considering volume labeling**

I think I might need to focus on Volume II's chapter, specifically checking for any mislabeling that appears in the preface. For the compute cluster, it seems like I should look at the exact file lines across Volume II and Volume III to ensure everything aligns correctly. There's a lot to keep track of, but I want to make sure I get it right! Let’s see how that goes.
thinking
**Evaluating conditions in modular contexts**

I’m thinking that perhaps the term "preface_trimmed" indicates that C1 is unconditional while C2 is uniform-weight; they're not identical but related in some way. Also, in Vol III about "modular_koszul_bridge," it states that C1 is unconditional and mentions that C2 is scalar. This distinction seems important, and I need to clarify how these concepts connect to each other and their implications in this context. It seems there’s a lot to unpack here!
thinking
**Finding theorem volumes**

I'm looking for volume 3 regarding the bar_cobar_bridge, but it seems like I can pair it with volume 1 for the canonical theorem and possibly volume 2 for the correct bridge. However, since the user wants each volume, I should consider using volume 2’s section `thqg_symplectic_polarization.tex:31-40` as a correctly cited source for the theorem C/C2 split. It's a bit tricky, but I'll figure it out!
thinking
**Evaluating internal misstatements**

I’m looking at Vol I and notice it still contains two outdated internal misstatements. One mistakenly presents the shifted-symplectic theorem C as unconditional, while chiral_koszul_pairs makes C1 conditional. Since the cross-volume bridge uses this surface, it’s crucial to be precise. I wonder if I should include surfaces from vol2/III that propagate correctly or incorrectly? It might be worth combining this with cluster 1 somehow. There's a lot to consider!
exec
/bin/zsh -lc "rg -n --no-heading \"13\\)|kappa\\(\\mathrm\\{Vir|kappa\\+kappa|K = 13|Virasoro.*13|250/3\" chapters/theory/higher_genus_foundations.tex chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
rg: regex parse error:
    (?:13\)|kappa\(\mathrm\{Vir|kappa\+kappa|K = 13|Virasoro.*13|250/3)
                   ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n --no-heading -F "13" chapters/theory/higher_genus_foundations.tex chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex | head -n 60' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading -F \"kappa(\\mathrm{Vir}\" chapters/theory/higher_genus_foundations.tex chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n --no-heading -F "250/3" chapters/theory/higher_genus_foundations.tex chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex | head -n 40' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:1530:$\kappa = 78(k+12)/24 = 13(k+12)/4$. At $k=1$: $\kappa = 169/4$.
chapters/examples/kac_moody.tex:1531:\item \emph{$E_7$}: $\dim = 133$, $h^\vee = 18$.
chapters/examples/kac_moody.tex:1532:$\kappa = 133(k+18)/36$. At $k=1$: $\kappa = 2527/36$.
chapters/examples/kac_moody.tex:1643: & $13(k+12)/4$ & $156$ & L \\
chapters/examples/kac_moody.tex:1644:$E_7$ & $133$ & $7$ & $18$ & $63$
chapters/examples/kac_moody.tex:1645: & $133(k+18)/36$ & $266$ & L \\
chapters/examples/kac_moody.tex:1677:$\gcd(78, 24) = 6$ (giving $13(k+12)/4$ for $E_6$)
chapters/examples/kac_moody.tex:1679:For $E_7$, $\gcd(133, 36) = 1$ ($133 = 7 \cdot 19$, $36 = 2^2 \cdot 3^2$),
chapters/examples/kac_moody.tex:1680:so the fraction $133(k+18)/36$ is already in lowest terms.
chapters/examples/kac_moody.tex:1695:$E_6$ & $1,\, 4,\, 5,\, 7,\, 8,\, 11$ & $36$ & $78$ & $78 = 6 \cdot 13$ \\
chapters/examples/kac_moody.tex:1696:$E_7$ & $1,\, 5,\, 7,\, 9,\, 11,\, 13,\, 17$ & $63$ & $399/2$ & $133 = 7 \cdot 19$ \\
chapters/examples/kac_moody.tex:1697:$E_8$ & $1,\, 7,\, 11,\, 13,\, 17,\, 19,\, 23,\, 29$ & $120$ & $620$ & $248 = 8 \cdot 31$ \\
chapters/examples/kac_moody.tex:2267:[r_{12}(z_{12}),\; r_{13}(z_{13})]
chapters/examples/kac_moody.tex:2271:[r_{13}(z_{13}),\; r_{23}(z_{23})]
chapters/examples/kac_moody.tex:2279:\frac{[\Omega_{12}, \Omega_{13}]}{z_{12}\,z_{13}}
chapters/examples/kac_moody.tex:2283:\frac{[\Omega_{13}, \Omega_{23}]}{z_{13}\,z_{23}}
chapters/examples/kac_moody.tex:2291:$[\Omega_{12}, \Omega_{13}]$ in $\mathfrak{sl}_2^{\otimes 3}$
chapters/examples/kac_moody.tex:2295:$1/(z_{12}\,z_{13}) + 1/(z_{12}\,z_{23}) + 1/(z_{13}\,z_{23}) = 0$
chapters/examples/kac_moody.tex:4931:$(ij|k\ell) \in \{(12|34),\,(13|24),\,(14|23)\}$.
chapters/examples/kac_moody.tex:5006:\textup{$t$-channel } (13|24)\colon\quad
 succeeded in 50ms:
chapters/examples/w_algebras.tex:71: $\kappa + \kappa' = 250/3$ \\
chapters/examples/w_algebras.tex:1924:Dually, the complementarity sum $\kappa + \kappa' = 250/3$
chapters/examples/w_algebras.tex:1925:reflects $\Theta + \Theta^! = (250/3) \cdot \eta \otimes \Lambda$,
chapters/examples/w_algebras.tex:2129: $\kappa + \kappa' = 5c/6 + 5(100-c)/6 = 250/3$.
chapters/examples/w_algebras.tex:2148:$\mathcal{W}_3^k$ & $100$ & $250/3$ & $c = 50$ \\
chapters/examples/w_algebras.tex:2801: Complementarity sum $\kappa + \kappa' = 5c/6 + 5(100-c)/6 = 250/3$.
chapters/theory/higher_genus_foundations.tex:4163:$\mathcal{W}_3$ charge $c$ & $5c/6$ & $5(100-c)/6$ & $250/3$ & $5c/144$ \\
chapters/theory/higher_genus_foundations.tex:5342:and $\kappa + \kappa' = 250/3$ for $\mathcal{W}_3$
chapters/theory/higher_genus_foundations.tex:5913:$3$ & $5/6$ & $100$ & $250/3$ \\
 succeeded in 50ms:
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/w_algebras.tex:1584:$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
chapters/examples/w_algebras.tex:2743: $\kappa(\mathrm{Vir}_c) = c/2$, anomaly ratio $\varrho = 1/2$.
chapters/examples/w_algebras.tex:3477:\item $\kappa(\mathrm{Vir}_c) = c/2$
chapters/examples/w_algebras.tex:3489:\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c})
chapters/examples/w_algebras.tex:3915:\item At $c = 0$: the curvature $\kappa(\mathrm{Vir}_0) = 0$ vanishes,
chapters/examples/w_algebras.tex:3922: $\kappa(\mathrm{Vir}_{-22/5}) = -11/5 \neq 0$ is nonzero, so the
chapters/examples/w_algebras.tex:4734:$\kappa(\mathrm{Vir}_c) = c/2$.
chapters/connections/concordance.tex:3943:$\kappa(\cH_1) = \kappa(\mathrm{Vir}_2)$ but
chapters/connections/concordance.tex:8739:$\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$
chapters/connections/concordance.tex:9612: $\kappa(\mathrm{Vir}_c) = c/2$,
chapters/theory/higher_genus_foundations.tex:5323:$\kappa(\mathrm{Vir}_c) = \frac{c}{2}$.
chapters/theory/higher_genus_foundations.tex:6011:$\kappa(\mathrm{Vir}_c) = c/2$,

thinking
**Clarifying citation details**

I need to check line 357 in the introduction for K=13 to correct the reference to vol3, which mistakenly shows K=26. I think using vol1 intro line 357 or higher_genus_foundations line 4162 could be enough for my citation. I'll need to closely inspect the exact line number between 350 and 358 to make sure I get it right. It's important to ensure I'm accurate in my citations!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '352,358p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   352	Theorem~B inverts the transform: at genus~$0$ via chiral
   353	Koszulity (Theorem~\ref{thm:koszul-equivalences-meta}),
   354	at genus~$g \ge 1$ via the inductive genus step.
   355	Theorem~C constrains the Koszul dual pair by a family-specific sum rule:
   356	$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
   357	Kac--Moody and free fields and $K = 13$ for Virasoro
   358	(self-dual at $c = 13$).








thinking
**Considering text changes**

I need to mention the specific fixes needed: in volume 1, I should replace lines 830-832 with new text; for volume 2, it’s about changing line 362. Then in volume 3, I’m looking at modifying the "modular_koszul_bridge," changing its opening and section 2 to use a three-layer language approach. I wonder if renaming `C2^CY` and the like might be overly detailed. Maybe it’s best to keep "modular_koszul_bridge" separate since it has more issues.
thinking
**Evaluating code structure**

I’m trying to fit this into cluster 2, but I’m not so sure. I need to inspect `modular_koszul_bridge`. The opening line has both misnumbering and incorrect information about complementarity. That makes me think it's probably cluster 1 instead. The user specifically wants exact file:line references, and I wonder if we should use single lines or maybe multiple exact ranges. I’ll consider how `structured_output_contract` uses `file:line` to format this properly.
thinking
**Analyzing theorem adjustments**

I see there's an issue with the vol3 summary theorem replacing theorem C by stating “chi(C) splits into halves/full Hochschild cohomology.” That’s not theorem C at all, and it seems to overlook the d=3 conditionality. I should really delve into this to understand what that means for the theorem's application and implications. This mismatch raises questions about the clarity and accuracy of the changes being proposed. Let's ensure we address this properly!
thinking
**Updating documentation details**

I need to fix several things: first, I'll update the docstring to reflect “scalar consequence of C1 + D / AP24.” I'll also correct the Virasoro kappa-level conductor to 13. Since the vol2 compute cluster may have several files, I could list a few representative surfaces, but maybe not exhaustively. The user wants exact file references, but clustering is okay. I’ll include 4–5 lines from vol2 and 3 from vol3. I should highlight specific lines where appropriate, too!
thinking
**Exploring object conflation**

I think I could create a finding related to object conflation across Theorem C bridge. This might be more substantial than what I had before. I’ll take a look through other files and search for `Z^{der}` in modular_koszul_bridge or bar_cobar_bridge. I’ve already found something in line 121. The `bar_cobar_bridge` might mention Hochschild cohomology, which could help with finding 2. I might also need to check volume 2 for similar instances of object conflation.
thinking
**Structuring references and problems**

I’m organizing canonical references and considering multiple lines for clarity. I might mention a specific line that's incorrect, and I could also include the start of a theorem. I’m thinking about another line for derived center use too. There are some lines that don’t pose problems, but I wonder if the user will object to anything. I’ll need to phrase my bullet points neatly, focusing mainly on the conflicting volumes while maintaining clarity about where corrections are needed.
thinking
**Considering file references**

The user requested exact file and line references in each volume, which is important. I think it's fine to use control surfaces, but I could also list only the problematic surfaces across the volumes if that makes sense. In bullet point 2, it appears there’s no problem in volume 2, so I should clarify that. I want to make sure my response is clear and directly addresses the user's needs while being concise.
thinking
**Evaluating bullet points**

I'm noticing that bullet 1 and bullet 3 overlap, which is a concern. Merging bullet 3 into bullet 1 could help avoid redundancy. I think I should also add a bullet about `K=26` from vol3 and the compute docs. The four findings seem alright, but I want to keep duplication to a minimum. Maybe I can make bullet 1 focus more on the `C2` label, while bullet 3 can emphasize conditionality mispropagation. That might keep things distinct enough.
codex
- [CRITICAL] Vol I `chapters/theory/higher_genus_complementarity.tex:40`, `chapters/theory/introduction.tex:830`; Vol II `chapters/frame/preface_trimmed.tex:362`; Vol III `chapters/connections/modular_koszul_bridge.tex:105`, `147` — PROBLEM: the live bridge surface redefines `C2` as the scalar `\kappa+\kappa^!` rule. The canonical Vol I theorem surface says `C0` = fiber-center identification, `C1` = unconditional eigenspace decomposition, `C2` = conditional shifted-symplectic/bar-side BV upgrade, and the scalar formulas are consequences of `C1 + D`, “not a separate C2 label.” FIX: in all three downstream files, replace the current `C2` wording with: `Theorem C has three layers C0/C1/C2. The scalar complementarity identity is a uniform-weight consequence of Theorem C1 together with Theorem D; C2 is the conditional shifted-symplectic upgrade.` In Vol II, replace `the scalar part C2 of Theorem~C` with `the scalar complementarity consequences of Theorem~C1 + Theorem~D`. In Vol III, rename `C2^{CY}` to a non-`C2` scalar label or remove that label entirely.

- [CRITICAL] Vol I `chapters/theory/higher_genus_complementarity.tex:53`, `72`; Vol II `chapters/connections/thqg_symplectic_polarization.tex:31`, `1104`; Vol III `chapters/connections/modular_koszul_bridge.tex:121`, `163`, `chapters/connections/bar_cobar_bridge.tex:219` — PROBLEM: the Vol III bridge rewrites Theorem C with the wrong object. Vol I/Vol II use the complementarity surface `H^*(\overline{\mathcal{M}}_g,\mathcal{Z}(A)) = Q_g(A)\oplus Q_g(A^!)`, with the shifted-symplectic upgrade separate. Vol III replaces that by `\cZ^{der}_{\mathrm{ch}}(A)` / “full Hochschild cohomology” / “CY Euler characteristic,” which is Theorem H or CY-D territory, not Theorem C. FIX: in `modular_koszul_bridge.tex`, replace both occurrences of `H^\bullet(...,\cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC))` by `H^\bullet(...,\mathcal{Z}(A_\cC))` or the local system notation already used in Vol I. In `bar_cobar_bridge.tex:219`, replace the bullet with: `Theorem C (complementarity). Assuming A_\cC exists, H^*(\overline{\mathcal{M}}_g,\mathcal{Z}(A_\cC)) \cong Q_g(A_\cC)\oplus Q_g(A_{\cC^!}); for g\ge1 the Verdier pairing identifies the two summands dually.` Keep derived-center/Hochschild claims under Theorem H only, and prefix all `d=3` uses with `Assume CY-A$_3$`.

- [HIGH] Vol I `chapters/theory/introduction.tex:592`, `chapters/theory/chiral_koszul_pairs.tex:70`; Vol II `chapters/connections/thqg_symplectic_polarization.tex:1114`; Vol III `chapters/connections/modular_koszul_bridge.tex:156` — PROBLEM: the unconditional/conditional boundary is reversed or missing. The Vol I introduction presents the shifted-symplectic form as if it were part of unconditional Theorem C; `chiral_koszul_pairs.tex` makes the C1 eigenspace decomposition conditional on perfectness; Vol III never transports the true conditional `C2` at all. Vol II already states the correct split: `C1` unconditional, `C2` conditional. FIX: in `introduction.tex`, replace the shifted-symplectic sentence with `C1 gives the Verdier eigenspace decomposition; the shifted-symplectic/bar-side BV refinement is the separate conditional theorem thm:shifted-symplectic-complementarity.` In `chiral_koszul_pairs.tex`, replace `the Lagrangian eigenspace decomposition is conditional` with `the bar-side shifted-symplectic/Lagrangian criterion is conditional; the C1 eigenspace decomposition is unconditional on the Koszul locus.` In `modular_koszul_bridge.tex`, add a real `C2^{CY}` item: conditional on `CY-A$_3`, perfectness, and nondegeneracy.

- [HIGH] Vol I `chapters/theory/higher_genus_complementarity.tex:444`, `chapters/theory/introduction.tex:355`; Vol II `compute/lib/genus_one_bridge.py:407`, `compute/lib/holographic_ht_engine.py:215`, `compute/lib/bulk_boundary_duality_engine.py:261`, `compute/lib/hochschild_bulk_bridge.py:14`, `compute/lib/genus2_obstruction_engine.py:1002`, `compute/tests/test_hochschild_bulk_bridge.py:213`; Vol III `chapters/theory/braided_factorization.tex:538`, `chapters/connections/modular_koszul_bridge.tex:168`, `compute/lib/fukaya_shadow_tower.py:1942` — PROBLEM: downstream prose, docstrings, and tests cite scalar `\kappa+\kappa^!` / `\rho K` identities as “Theorem C” itself. Canonical Vol I says these are scalar consequences of `C1 + D`, not `C2`; `modular_koszul_bridge.tex:168` also uses Virasoro `K=26` at the kappa-level, contradicting Vol I’s `K=13`. FIX: change every such surface to `scalar complementarity consequence of Vol I Theorem C1 plus Theorem D` or `AP24 scalar complementarity`. In `braided_factorization.tex:538`, replace the opening with `Vol~I Theorem~C1 gives the Verdier eigenspace decomposition; combined with Vol~I Theorem~D it yields the scalar family-dependent sum.` In `modular_koszul_bridge.tex:168`, replace `Virasoro gives K = 26 with scalar sum 13` by `Virasoro scalar sum is 13; 26 is the central-charge sum and must not be used as the kappa-level conductor.`

## Summary
Checked: 26 | Findings: 4 | Verdict: FAIL
tokens used
206,455
