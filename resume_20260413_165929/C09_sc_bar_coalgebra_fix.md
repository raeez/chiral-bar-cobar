# C09_sc_bar_coalgebra_fix (999s)

**Applied**
- PROBLEM at [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:135), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:304), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:315): it said classes `G/L` have “Swiss-cheese-formal bar complexes” and put the SC colours on `B(\cA)`. EXACT edit applied: changed this to “finite shadow depth; only class `G` is Swiss-cheese-formal on the derived-center side,” replaced the table with `SC datum = (C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`, and rewrote the paragraph so `d_{\bar B}` and `\Delta` are only the two operations of the ordered `E_1` dg coalgebra.

- PROBLEM at [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1433), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1601), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1612), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1812): same AP165/B54 drift, repeated in both the colour table and the gauge/gravity summary. EXACT edit applied: same correction as above, plus changed the gauge-theory summary to “finite shadow depth; only class `G` is Swiss-cheese-formal on the derived-center side.”

- PROBLEM at [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) and [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:6135): both said the bar differential/coproduct are the closed/open SC colours. EXACT edit applied: rewrote both passages so the bar complex is the ordered `E_1` coalgebraic engine, and the actual `\SCchtop` datum lives on `(C^\bullet_{\mathrm{ch}}(A_b,A_b), A_b)`.

- PROBLEM at [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:2368), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:6201), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7765), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:1316), and [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:1395): the derived-center pair was reversed as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and one survey still said “the bar complex carrying both structures is an SC-algebra.” EXACT edit applied: swapped every reversed pair to `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)` and replaced the SC-on-bar sentence with “ordered bar = `E_1`-chiral coassociative coalgebra; SC appears on `(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`.”

- PROBLEM at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1733) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1929): the appendix still called the bar differential/coproduct the closed/open colours of the Swiss-cheese algebra. EXACT edit applied: synced it to the corrected chapter wording, changing this to “chiral/coassociative components” and “components of the `E_1`-chiral coalgebra.”

- PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar/working_notes.tex:1680) and [working_notes.tex](/Users/raeez/chiral-bar-cobar/working_notes.tex:8044): the notes still said “This is the Swiss-cheese algebra” and “the bar complex presents the Swiss-cheese algebra.” EXACT edit applied: changed this to “Swiss-cheese operation space” plus “the bar complex is the `E_1` coalgebraic engine,” and moved the SC datum explicitly to `(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`.

- PROBLEM at [theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:2), [theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:648), [test_theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4), and [test_heisenberg_bridge.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bridge.py:16): compute docs/tests still taught “bar complex = Swiss-cheese algebra” and “SC on boundary algebra.” EXACT edit applied: changed them to “ordered bar = `E_1` coalgebraic engine” and “SC lives on the derived-center pair.”

- PROBLEM at [swiss_cheese_chain_model.py](/Users/raeez/chiral-bar-cobar/compute/lib/swiss_cheese_chain_model.py:339), [factorization_coproduct_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/factorization_coproduct_engine.py:619), and [theorem_vicedo_envelope_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vicedo_envelope_engine.py:826): helper docstrings still read the two geometric directions as a Swiss-cheese structure on `B(A)`. EXACT edit applied: rewrote each to say those directions are only the provenance of the ordered `E_1` bar complex, while the genuine SC datum is the derived-center pair.

**Blocked Outside Workspace**
- PROBLEM at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1108), [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:7), [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2071), [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2230), [log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:2047), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:8), [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:152), [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149), and [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3358): Vol II still has affirmative SC-on-bar claims. Edit not applied: those files are outside the writable workspace here.

- PROBLEM at [swiss_cheese_cy3_e1.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:4): Vol III still says the `E_1` bar complex has Swiss-cheese structure. Edit not applied: that file is also outside the writable workspace here.

Verification: I ran a post-edit grep over live Vol I surfaces for the AP165/B54 slogans and pair-order drift; it returned no remaining local matches. I did not run TeX builds or `pytest`, since these were prose/docstring-only edits.


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
session id: 019d87f9-a7b5-7090-b5c3-cf13daf6ad0c
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Fix any remaining 'B(A) is SC coalgebra' claims (AP165/B54).
Search ALL volumes for 'bar.*SC\|B(A).*SC\|coalgebra.*SC'.
B(A) is E_1 coalgebra. SC lives on (C^bullet_ch(A,A), A). Fix each.
mcp startup: no servers


thinking
**Considering codebase search options**

I might need to spawn explorer agents for searching the codebase. The instructions suggest using explorers first for codebase questions. They’re fast and authoritative, so I prefer them over manual searches. I could use one explorer for each volume or one for all, but I have to be mindful that some volumes aren't writable. The user asked to search all volumes and fix issues, but I think I can't edit outside of the writable roots.
thinking
**Evaluating filesystem permissions**

It seems that filesystem sandboxing might allow reading other files, but editing requires approval, which we never get. This means I can't edit outside the current working directory. I’m wondering if the user is sharing the same workspace, but permissions suggest I can only edit in the current directory and writable roots, meaning Volumes II and III are off-limits. Maybe I should check if those paths are symlinked under the current working directory, but they probably aren't. I guess I can only read them and edit assigned files.
codex
Using `cross-volume-propagation` and `deep-beilinson-audit` here: I’m first reading the required repo constitution files, then I’ll grep the exact AP165/B54 claim surface across all three volumes and patch only the concrete false assertions I can legally edit.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

 succeeded in 51ms:
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

codex
I’ve loaded the repo’s live constitutional surfaces. Next I’m doing a three-volume grep for the SC/bar conflation, then I’ll inspect each hit in context, patch only false assertions, and verify no live advertisement remains in Vol I plus any readable-but-nonwritable collisions in Vol II/III.
Plan update
Audit and fix AP165/B54 within the requested cross-volume scope, keeping edits minimal and truthful.
  → Search all three volumes for SC/bar-coalgebra conflations and collect exact hits
  • Inspect each hit in context and classify whether it asserts the forbidden claim
  • Patch every writable false assertion with the minimal truthful replacement
  • Run post-edit verification grep and summarize any remaining nonwritable collisions
exec
/bin/zsh -lc "rg -n -i -e 'bar.*SC|B\\(A\\).*SC|coalgebra.*SC' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2554

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:29:Bare "kappa" is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:212:AP151: Convention clash from coexisting hbar definitions. Two definitions of hbar (e.g. hbar = log(q) vs hbar = (log q)/(2*pi*i), or hbar as deformation parameter vs hbar as Planck constant) can coexist in the same chapter when material is drawn from different sources. The discrepancy cascades silently through all formulas that depend on hbar. Counter: before introducing ANY hbar, grep the current file and all imported chapters for existing definitions. If a second convention is needed, introduce a distinct symbol (hbar', hbar_1, Psi) with an explicit bridge identity. One file, one hbar.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:336:3. Check AP113: bare kappa -> subscripted kappa_{ch,BKM,cat,fiber}.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:163:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:165:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:167:**The E_n operadic circle (2026-04-12):** E_3(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:299:  - SC^{ch,top} structural correction: B(A) is E_1 coalgebra, NOT SC-coalgebra (AP165); SC is NOT self-dual (AP166);
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:701:B(A) is E_1 coalgebra          # NOT SC-coalgebra; SC on derived center pair
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:723:"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra; SC in derived center pair (AP165)
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:749:**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:835:- `AP165` B(A) not attributed SC structure;
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:7:The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:36:- **Moduli M_{g,n}** (stratified by stable graphs): Curved bar complex. d^2 = kappa * omega_g. Shadow obstruction tower {F_g}. Discriminant. G/L/C/M classification.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:125:5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top})
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:131:### Critical strata with dedicated bar chain models (MUST BE IN MANUSCRIPT)
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:152:**Pair of pants (genus-0, 3 boundary circles)**: The multiplication cobordism. Its bar chain model encodes the product on chiral homology / Hochschild homology. The pair of pants = the three-punctured sphere P^1 \ {0, 1, infty}. The bar chain model on the pair of pants is the chain-level avatar of the chiral product.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:160:- B(A) is NOT an SC^{ch,top}-coalgebra (AP165). B(A) is an E_1 chiral coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). See Vol I CLAUDE.md AP165/B54-B56.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:227:AP151: Convention clash within single file. Two definitions of hbar cascade into wrong q (real instead of root of unity). Counter: grep all definitions of hbar after writing any formula.
codex
The raw grep is noisy because it catches constitutions, engines, and correct negations. I’m narrowing to actual affirmative manuscript/README claims now and separating writable Vol I hits from Vol II/III collisions that I may only be able to report.
collab spawn_agent(call_EdZomrqWZngSVoStmaKyb5oL, prompt="Search /Users/raeez/chiral-bar-cobar for remaining affirmative claims conflating the bar complex B(A) with Swiss-cheese/…")
spawn_agent(call_EdZomrqWZngSVoStmaKyb5oL, prompt="Search /Users/raeez/chiral-bar-cobar for remaining affirmative claims conflating the bar complex B(A) with Swiss-cheese/…") pending init:
  agent: 019d87fa-7f86-79e3-9153-ac3a76799974
mcp startup: no servers
collab spawn_agent(call_SaTVsjjJOEMB7SSQG3JAKJau, prompt="Search /Users/raeez/chiral-bar-cobar-vol2 for remaining affirmative claims conflating the bar complex B(A) with Swiss-ch…")
mcp startup: no servers
spawn_agent(call_SaTVsjjJOEMB7SSQG3JAKJau, prompt="Search /Users/raeez/chiral-bar-cobar-vol2 for remaining affirmative claims conflating the bar complex B(A) with Swiss-ch…") pending init:
  agent: 019d87fa-7f8a-7511-8db8-e23f75eff083
collab spawn_agent(call_5gVAxtuICLOrPDWYxwcCtIbC, prompt="Search /Users/raeez/calabi-yau-quantum-groups for remaining affirmative claims conflating the bar complex B(A) with Swis…")
spawn_agent(call_5gVAxtuICLOrPDWYxwcCtIbC, prompt="Search /Users/raeez/calabi-yau-quantum-groups for remaining affirmative claims conflating the bar complex B(A) with Swis…") pending init:
  agent: 019d87fa-7f9d-76c2-85ed-bdce297b4d1a
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"bar.*SC|B\\(A\\).*SC|coalgebra.*SC\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1972

rectification_20260412_233715/R13_introduction.md:98:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
rectification_20260412_233715/R13_introduction.md:100:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
rectification_20260412_233715/R13_introduction.md:106:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
audit_campaign_20260412_231034/XV11_claim_status_sync.md:172:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:174:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:180:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
rectification_20260412_233715/R19_coderived_models.md:167:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
rectification_20260412_233715/R19_coderived_models.md:169:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
rectification_20260412_233715/R19_coderived_models.md:175:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
audit_campaign_20260412_231034/AP23_pi3_BU.md:126:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
audit_campaign_20260412_231034/AP23_pi3_BU.md:128:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
audit_campaign_20260412_231034/AP23_pi3_BU.md:134:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
audit_campaign_20260412_231034/AP23_pi3_BU.md:403:/Users/raeez/chiral-bar-cobar/AGENTS.md:537:**Categorical confusion**: FM4 (k=0 vs k=-h^v), FM11 (Sugawara shift missing: av(r)+dim(g)/2=kappa for non-abelian), FM23 (local-global on curves: point≠D≠A^1≠P^1), FM24 (B-cycle i^2: q becomes real), FM25 (SC disaster: B(A) is NOT SC-coalgebra — entire false framework), FM26 (false SC self-duality: dim check fails), FM27 (scope inflation in metadata), FM28 (topologization scope: proved KM only), FM32 (pi_3(BU)=pi_2(U)=0, not Z), FM33 (formula outside hypothesis domain), FM34 (excision/coproduct: ⊗_A vs plain ⊗)
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:144:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:146:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:152:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
healing_20260413_130533/H11_SC_formal_alt.md:3:I repaired the converse of `prop:sc-formal-iff-class-g` and added the requested `Remark[Operadic alternative proof]` in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2823) and [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2863). The key correction is that I did not use the requested `B_{SC}` / `Δ=0 \Rightarrow` class `G` converse, because that is not true on the manuscript’s own classification surface: class `L` still has `\Delta=0`. The new converse instead uses the full operadic vanishing pattern `S_r=0` for all `r\ge 3`, via the genus-0 transfer tree and the averaging map `\operatorname{av}(\Theta^{E_1}_\cA)=\Theta_\cA`.
healing_20260413_130533/H11_SC_formal_alt.md:80:1. SC-formality means the SC bar complex B_{SC}(A) is formal.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"bar.*SC|B\\(A\\).*SC|coalgebra.*SC\" -g\"*\" --glob '"'!*'"' --color never --line-number --text /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"bar.*SC|B\\(A\\).*SC|coalgebra.*SC\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:163:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
AGENTS.md:165:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.
AGENTS.md:167:**The E_n operadic circle (2026-04-12):** E_3(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.
AGENTS.md:299:  - SC^{ch,top} structural correction: B(A) is E_1 coalgebra, NOT SC-coalgebra (AP165); SC is NOT self-dual (AP166);
AGENTS.md:701:B(A) is E_1 coalgebra          # NOT SC-coalgebra; SC on derived center pair
AGENTS.md:723:"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra; SC in derived center pair (AP165)
AGENTS.md:749:**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
AGENTS.md:835:- `AP165` B(A) not attributed SC structure;
chapters/examples/toroidal_elliptic.tex:1867:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1868:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
compute/lib/e1_bar_cobar_cy3.py:424:    The E₁ bar complex uses ORDERED tensor products and the HOCHSCHILD
chapters/theory/braided_factorization.tex:262:a Swiss-cheese ($\SC^{\mathrm{ch,top}}$) coalgebra. The SC structure of
chapters/theory/introduction.tex:13:A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
chapters/theory/hochschild_calculus.tex:390:(Koszulness K2): both are manifestations of bar-cohomological formality (Koszulness, not SC formality) at
notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
notes/physics_bv_brst_cy.tex:388:\begin{definition}[$E_1$ coalgebra structure on $B(A)$ and the $\SC^{\mathrm{ch,top}}$ open-closed pair, cf.~Vol~II]
notes/physics_bv_brst_cy.tex:405:\begin{warning}[$B(A)$ does not carry $\SC^{\mathrm{ch,top}}$-algebra structure]
notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.
notes/physics_bv_brst_cy.tex:586: \item \textbf{The closed string field theory and $\mathcal{W}$-algebras.} For CY3, the closed string sector is controlled by the BCOV theory, whose algebraic structure is a $\mathcal{W}$-algebra (the vertex algebra of polyvector fields with Schouten bracket and $\partial$ operator). The full open-closed BV-BRST complex should be the Swiss-cheese bar complex $B_{\SC}(A_\cC)$, combining the $\mathcal{W}$-algebra (bulk) with $G(X)$ (boundary) via the open-closed coupling.
chapters/theory/cy_to_chiral.tex:2054:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -e \"bar.*SC\" -e \"B\\(A\\).*SC\" -e \"coalgebra.*SC\" --text /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:340:- **Critical level center jump** (prop:critical-level-ordered): at k=-h^v, ALL monodromy trivial, Koszulness fails, H^1 doubles, bar H* = Omega*(Op). The SC^{ch,top} structure at critical level is the genuine holomorphic intermediary (no topologization possible).
/Users/raeez/chiral-bar-cobar-vol2/README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
/Users/raeez/chiral-bar-cobar-vol2/README.md:22:| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:7:The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:125:5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top})
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:131:### Critical strata with dedicated bar chain models (MUST BE IN MANUSCRIPT)
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:160:- B(A) is NOT an SC^{ch,top}-coalgebra (AP165). B(A) is an E_1 chiral coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). See Vol I CLAUDE.md AP165/B54-B56.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:277:FM52: Within-surface SC = holographic bulk-boundary. Claimed the half-plane bar complex "is where the bulk-boundary correspondence should be made precise." WRONG. The within-surface SC (R ⊂ C) governs restriction to a real locus. The holographic bulk-boundary goes through the derived center (circle model / Hochschild). Counter: SC governs within-surface structure; holography goes through Hochschild/derived center.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:331:| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:48:These make `B(A)` a dg coassociative coalgebra. It is NOT an `SC^{ch,top}`-coalgebra: `B(A)` is a single E_1 coalgebra, not a two-colored SC datum.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:66:The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:70:- "B(A) is a coalgebra over SC^{ch,top}"
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:261:- AP165: B(A) is NOT an SC^{ch,top}-coalgebra. B(A) is E_1 chiral coassociative. SC^{ch,top} emerges in the derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) coalgebra over SC", "bar presents Swiss-cheese", "bar differential is closed color", "bar coproduct is open color."
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:279:- AP177: lem:operadic-kunneth chain-level decomposition is WRONG at chain level. The bar differential of SC^{ch,top}_mix has cross-terms d_mix from open edge contractions between mixed vertices (the map μ₁ combining closed inputs). The CORRECT statement is: the decomposition holds on the ASSOCIATED GRADED with respect to the closed-input-excess filtration. The pentagon theorem does NOT depend on this lemma (direct Koszul duality suffices).
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:284:- AP182: Curved Dunn three-level refinement. Level 1 (genus 0): PROVED. Level 2 (obstruction theory): obstruction in H²(Hom(B(E₁^tr), gr^g(B_mod(SC)))). Level 3 (twisted Künneth): full modular bar = twisted tensor product B_mod(SC) ⊗^{Mon(R)} B(E₁^tr). Genus-1 twisted tensor product PROVED (prop:genus1-twisted-tensor-product). Full genus tower OPEN.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:828:- `B(A)` is an E_1 coassociative coalgebra classifying twisting morphisms; it does NOT carry `SC^{ch,top}` structure; the SC structure emerges in the chiral derived center pair `(C^bullet_{ch}(A,A), A)`;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:73:The E$_1$ bar complex $\barB(\cA)$ on $\FM_k(\C) \times \Conf_k^{<}(\R)$ is one coalgebra; three functors extract three objects: cobar $\Omega(\barBch(\cA)) \simeq \cA$ recovers the original algebra (bar-cobar inversion), Verdier duality $\mathbb{D}_{\mathrm{Ran}}(\barBch(\cA)) \simeq \barBch(\cA^!)$ produces the line-side Koszul dual, and chiral Hochschild cochains $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ compute the bulk observables. The $\SCchtop$~structure is not carried by $\barB(\cA)$ itself but by the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is the bulk-acting-on-boundary datum. Every chapter of this volume is a different projection of the bar coalgebra.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:87:Volume~II lifts this from one to three dimensions. The bar differential~$D_\cA$ is holomorphic factorisation on~$\C$; the deconcatenation coproduct~$\Delta$ is topological factorisation on~$\R$; together they form an $E_1$ dg coassociative coalgebra on $\FM_k(\C) \times \Conf_k^<(\R)$. The $\mathrm{SC}^{\mathrm{ch,top}}$ structure emerges in the chiral derived center: the pair $(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is the bulk-boundary datum. The modular characteristic~$\kappa(\cA)$ determines the curved $A_\infty$ deformation at genus $g \ge 1$, complementarity lifts to the bulk-boundary-line triangle, and the discriminant~$\Delta$ classifies the complexity of bulk-boundary pairs. Classical Koszul duality is genus~$0$ on the formal disk; Volume~I is genus~$g$ on a curve; Volume~II is the dimensional lift to $\C \times \R$.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:263:The bar-cobar adjunction on $\SCchtop$-algebras is a Quillen
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '240,300p' chapters/theory/braided_factorization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\]
equipped with:
\begin{enumerate}[label=(\roman*)]
 \item two commuting differentials $d_X, d_Y$ from OPE residues
 in each $\Eone$-direction, satisfying $d_X^2 = d_Y^2 = 0$ and
 $d_X \circ d_Y = d_Y \circ d_X$;
 \item two deconcatenation coproducts $\Delta_X, \Delta_Y$ giving
 $B_{E_2}(\cA)$ the structure of an $\Etwo$-coalgebra;
 \item a braid group action: the symmetric group $S_n$ action on
 $B^{\mathrm{ord}}_n(\cA) = (s^{-1}\bar{\cA})^{\otimes n}$ lifts
 to a braid group $B_n$ action via the $R$-matrix
 $\cR_\cA(z)$ (Definition~\ref{def:categorical-r-matrix}).
\end{enumerate}
The total differential is $d = d_X + d_Y$; it satisfies $d^2 = 0$ on
the nose (genus-$0$ bar complex). At genus $g \geq 1$, the fiberwise
differential satisfies $d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$
(Hodge curvature; see Theorem~\ref{thm:e2-bar-cobar}(iii)).
\end{definition}

\begin{remark}[$B_{E_2}(\cA)$ is not a Swiss-cheese coalgebra]
collab wait(call_lzBcCLzko23Ia6kr5anxwbSM)
  receivers: 019d87fa-7f86-79e3-9153-ac3a76799974, 019d87fa-7f8a-7511-8db8-e23f75eff083, 019d87fa-7f9d-76c2-85ed-bdce297b4d1a
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"B\\(A\\) is .*SC\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 599

healing_20260413_132214/H03_thm_C_alt_proof.md:138:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
healing_20260413_132214/H15_remove_chain_level_topol.md:449:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:146:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
rectification_20260412_233715/R13_introduction.md:100:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
healing_20260413_132214/H08_topol_alt_proof.md:119:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
healing_20260413_132214/H19_remove_genus0_koszul_vii.md:157:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
rectification_20260412_233715/R19_coderived_models.md:169:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
relaunch_20260413_111534/R13_introduction.md:111:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:117:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 775350)
relaunch_20260413_111534/AP23_pi3_BU.md:164:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
relaunch_20260413_111534/AP23_pi3_BU.md:435:/Users/raeez/chiral-bar-cobar/AGENTS.md:537:**Categorical confusion**: FM4 (k=0 vs k=-h^v), FM11 (Sugawara shift missing: av(r)+dim(g)/2=kappa for non-abelian), FM23 (local-global on curves: point≠D≠A^1≠P^1), FM24 (B-cycle i^2: q becomes real), FM25 (SC disaster: B(A) is NOT SC-coalgebra — entire false framework), FM26 (false SC self-duality: dim check fails), FM27 (scope inflation in metadata), FM28 (topologization scope: proved KM only), FM32 (pi_3(BU)=pi_2(U)=0, not Z), FM33 (formula outside hypothesis domain), FM34 (excision/coproduct: ⊗_A vs plain ⊗)
rectification_20260412_233715/R21_standalone_e1_primacy.md:115:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
healing_20260413_132214/H09_koszul_equivs_alt.md:132:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
relaunch_20260413_111534/R19_coderived_models.md:104:**FM25. The SC^{ch,top} disaster of 2025-2026 (Opus 4.6 structural confabulation).** Opus constructed an elaborate but FALSE framework claiming B(A) is an SC^{ch,top}-coalgebra. The chain of errors:
relaunch_20260413_111534/R19_coderived_models.md:112:(4) WRONG: "The SC structure on B(A) is dual to the SC structure on (Z^{der}(A), A)." TRUTH: B(A) is an INPUT to the Hochschild computation. The derived center C^bullet_ch(A,A) is computed FROM B(A) via the convolution Hom(B(A), A). The SC structure emerges in the OUTPUT (the derived center pair), not on the INPUT (the bar complex). The passage B(A) → C^bullet_ch(A,A) is the Hochschild construction, not an operadic duality.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:174:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
rectification_20260412_233715/R11_thqg_symplectic_polarization.md:84:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '2020,2085p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ============================================================
\section{Cross-volume bridges}
\label{sec:cross-volume}
% ============================================================

The results of this chapter connect the CY$_3$ programme to the algebraic engine of Vol~I (Theorems~A--D, the bar-intrinsic MC element $\Theta_A := D_A - d_0$) and the holomorphic-topological QFT framework of Vol~II (Swiss-cheese structure, PVA descent).

\subsection{Shadow tower identification}
\label{subsec:cross-vol-shadow}

The shadow obstruction tower $\Theta_A$ of Vol~I specializes as follows for CY$_3$ chiral algebras:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
 \toprule
 \textbf{Vol~I object} & \textbf{CY$_3$ specialization} & \textbf{Identification} \\
 \midrule
 $\kappa_{\mathrm{ch}}(A)$ & $\kappa_{\mathrm{ch}}(\C^3) = 1$ & MacMahon genus-$1$ \\
 Cubic shadow $C$ & BKM lightlike roots & $c(0) = 10$ for $K3 \times E$ \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"B\\(A\\).*SC\" | grep -i -v \"not\" | head" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H07_MC5_alt_approach.md:128:I need to determine if the requested content conflicts with AGENTS. The user mentioned a technique involving SC^ch,top Koszul duality, which connects SC-algebras with SC^!-coalgebras in the coderived category. This seems to be automatically derived from Livernet Koszulity and the general bar-cobar construction. However, AGENTS states that SC^{ch,top} isn't related to B(A), which is an E1 coalgebra, while SC is defined on the pair (C_ch^\bullet(A,A),A).
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 775350)
healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
scripts/adversarial_wave2.py:340:    ("B09_SC_bridge", "How is SC^{ch,top} described in Vol II? Is it on the derived center pair (correct) or B(A) (wrong AP165)? Is SC^! = (Lie,Ass) correctly stated? Is topologization scope correct?"),
resume_20260413_163457/S14_standalone_to_main.md:870:I need to see if the chapters in question have been corrected. The lines around 1247+ in "en_koszul_duality" should be checked closely. Also, it appears that the `programme_summary_sections5_8` file might already have some corrections, but line 314 misstates some colors, which shows inconsistency. I could also look for contradictions in "survey_modular_koszul_duality.tex." It might be important to search for more specific phrases like `B(A)` SC, `SC-algebra`, or `SC coalgebra` to clarify any issues.
resume_20260413_163457/S16_v1_to_v2_bridge.md:288:README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
resume_20260413_163457/S16_v1_to_v2_bridge.md:366:README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
resume_20260413_163457/S16_v1_to_v2_bridge.md:491:     6	The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
audit_campaign_20260412_231034/T20_gerstenhaber.md:124:CLAUDE.md:210:A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.
audit_campaign_20260412_231034/T20_gerstenhaber.md:126:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '550,620p' notes/physics_bv_brst_cy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{enumerate}[label=(\arabic*)]
 \item \textbf{Fields.} The open string field $\alpha \in \RHom(\cF,\cF)[1]$ is an element of the bar complex $B(A_\cC)$.

 \item \textbf{Action.} The BV action $S(\alpha) = \sum \frac{1}{n}\Tr(\mu_n(\alpha^{\otimes n}))$ is the CY trace of the universal MC element $\Theta_A$.

 \item \textbf{Bracket.} The BV antibracket $\{-,-\}$ is the odd Poisson bracket induced by the CY pairing on $A[1]$.

 \item \textbf{QME = MC.} The quantum master equation $\hbar\Delta S + \frac{1}{2}\{S,S\} = 0$ is the Maurer--Cartan equation for $\Theta_A$.

 \item \textbf{Bar differential = BRST.} The bar differential $d_B$ on $B(A)$ is the BRST operator $Q_{\BRST} = \{S,-\}$.

 \item \textbf{Curvature = anomaly.} The curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ at genus $g$ is the BRST anomaly. Anomaly cancellation requires $\kappa_{\mathrm{ch}}(A_\cC) = 0$.

 \item \textbf{Swiss-cheese = open-closed BV.} The $\SC^{\mathrm{ch,top}}$ structure on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ is the BV structure on the combined open-closed string field theory. The bar complex $B(A)$ is the $E_1$ dg coassociative coalgebra (the open sector); the chiral derived center $C^\bullet_{\mathrm{ch}}(A,A)$ is the closed sector.

 \item \textbf{$E_1$ = BRST, $E_2$ = braiding.} The $E_1$ coalgebra structure on $B(A)$ is the BRST direction; the $E_2$ enhancement (when available from CY$_{\geq 2}$ framing) adds the braiding/quantum group structure.

 \item \textbf{For CY3.} The full BV-BRST complex of the topological B-model on $X$ is the bar complex $B(G(X))$ of the quantum vertex chiral group. The denominator identity of the BKM superalgebra $\mathfrak{g}_X$ is the BV partition function.
\end{enumerate}

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 4164

FRONTIER.md:208:| 7 | Swiss-cheese structure of chiral Koszul pairs | Selecta | SC^{ch,top} operadic structure, PVA descent |
healing_20260413_132214/H03_thm_C_alt_proof.md:146:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
healing_20260413_132214/H02_thm_B_alt_proof.md:134:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
healing_20260413_132214/H15_remove_chain_level_topol.md:176:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
healing_20260413_132214/H15_remove_chain_level_topol.md:193:874:AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
healing_20260413_132214/H15_remove_chain_level_topol.md:450:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
healing_20260413_132214/H15_remove_chain_level_topol.md:466:- **CLAUDE.md:7‑15,879** – Chain-level topologization is strictly scoped: the ordered bar B^ord(A) is only an E₁ coassociative coalgebra, the Swiss-cheese structure (and any E₃-topological lift) lives on the derived chiral center, and the topologization theorem in `en_koszul_duality.tex` is proved only for affine Kac–Moody at non-critical level (Sugawara makes C-translations Q-exact; no conformal vector = SC^{ch,top} only). General conformal-vector families remain conjectural and require the 3d HT BRST/cohomological control, so any edit must keep those qualifiers and avoid claiming SC^{ch,top} = E₃.  
healing_20260413_132214/H15_remove_chain_level_topol.md:4732:/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:159:**SC^{ch,top} != E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.
healing_20260413_132214/H15_remove_chain_level_topol.md:5725:\index{Swiss-cheese operad!generic vs.\ $E_3$}
healing_20260413_132214/H18_remove_class_M_MC5.md:117:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
healing_20260413_132214/H18_remove_class_M_MC5.md:287:healing_20260413_132214/H07_MC5_alt_approach.md:3:Updated [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2029). The operadic remark now states the alternative MC5 route in the corrected two-colour form: `\Delta_{\mathrm{BV}}` is the closed-colour Swiss-cheese contraction, `d_{\bar B}` is the open-colour coderivation, the relevant `SC^{\mathrm{ch,top}}` object is the pair `\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA\bigr)` rather than `B(A)` itself, the coderived comparison is presented as the coloured Koszul bar-cobar correspondence, and the class `\mathsf{M}` chain-level gap is isolated as non-formality of the explicit transferred model rather than a failure of coderived duality.
healing_20260413_132214/H18_remove_class_M_MC5.md:562:healing_20260413_132214/H07_MC5_alt_approach.md:600: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H18_remove_class_M_MC5.md:563:healing_20260413_132214/H07_MC5_alt_approach.md:652: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H18_remove_class_M_MC5.md:564:healing_20260413_132214/H07_MC5_alt_approach.md:704: Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
healing_20260413_132214/H18_remove_class_M_MC5.md:698:  2044	contraction induced by the Swiss-cheese pairing, whereas the bar
healing_20260413_132214/H18_remove_class_M_MC5.md:702:  2048	compared is not ``the bar complex as a Swiss-cheese algebra'': the
healing_20260413_132214/H18_remove_class_M_MC5.md:703:  2049	Swiss-cheese object is the pair
healing_20260413_132214/H18_remove_class_M_MC5.md:828:- `chapters/connections/bv_brst.tex:1893‑2240` bundles the existing constraints. The obstruction table (1893‑1901) singles out class \(\mathsf{M}\) (Virasoro/\(\mathcal W_N\)) as the lone entry where BV=bar only holds in \(D^{\mathrm{co}}\). The coderived theorem \(thm:bv-bar-coderived\) at 1917‑1956 spells out the \(m_0\)-power torsion mechanism, Proposition \ref{prop:chain-level-three-obstructions}, and the fact that all higher harmonic discrepancies are absorbed only after passing to the coderived quotient. Remarks 2031‑2166 revisit the Swiss-cheese/Koszul route, explain why the curved setting forces \(D^{\mathrm{co}}\), and point to the unresolved filtered‑completed upgrade for class \(\mathsf{M}\). The research remark candidate (2169‑2240) already encodes that the “shadow obstruction tower” never stops for Virasoro/principal \(\mathcal W_N\), proposes a shadow-window/spectral filtration (via Proposition \ref{prop:coderived-bar-degree-spectral-sequence}) whose differentials should record the harmonic classes \(c_r(\cA)\), and raises the weight-completion/completed bar-cobar interplay (Proposition \ref{prop:standard-strong-filtration}, Theorem \ref{thm:completed-bar-cobar-strong}, the continuous maps \(\widehat f_g\), and definitions of filtered weak equivalence/provisional coderived). Any new remark must respect these line numbers and the existing labels \(rem:bv-bar-class-m-frontier\), \(thm:bv-bar-coderived\), and the surrounding spectral/completion references.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -e \"bar.*SC\" -e \"B\\(A\\).*SC\" -e \"coalgebra.*SC\" --text /Users/raeez/chiral-bar-cobar-vol2 | grep -viE \"\\bnot\\b|does NOT|FORBIDDEN\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:340:- **Critical level center jump** (prop:critical-level-ordered): at k=-h^v, ALL monodromy trivial, Koszulness fails, H^1 doubles, bar H* = Omega*(Op). The SC^{ch,top} structure at critical level is the genuine holomorphic intermediary (no topologization possible).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:7:The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:125:5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top})
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:131:### Critical strata with dedicated bar chain models (MUST BE IN MANUSCRIPT)
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:277:FM52: Within-surface SC = holographic bulk-boundary. Claimed the half-plane bar complex "is where the bulk-boundary correspondence should be made precise." WRONG. The within-surface SC (R ⊂ C) governs restriction to a real locus. The holographic bulk-boundary goes through the derived center (circle model / Hochschild). Counter: SC governs within-surface structure; holography goes through Hochschild/derived center.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:331:| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:70:- "B(A) is a coalgebra over SC^{ch,top}"
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:284:- AP182: Curved Dunn three-level refinement. Level 1 (genus 0): PROVED. Level 2 (obstruction theory): obstruction in H²(Hom(B(E₁^tr), gr^g(B_mod(SC)))). Level 3 (twisted Künneth): full modular bar = twisted tensor product B_mod(SC) ⊗^{Mon(R)} B(E₁^tr). Genus-1 twisted tensor product PROVED (prop:genus1-twisted-tensor-product). Full genus tower OPEN.
/Users/raeez/chiral-bar-cobar-vol2/README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
/Users/raeez/chiral-bar-cobar-vol2/README.md:22:| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:87:Volume~II lifts this from one to three dimensions. The bar differential~$D_\cA$ is holomorphic factorisation on~$\C$; the deconcatenation coproduct~$\Delta$ is topological factorisation on~$\R$; together they form an $E_1$ dg coassociative coalgebra on $\FM_k(\C) \times \Conf_k^<(\R)$. The $\mathrm{SC}^{\mathrm{ch,top}}$ structure emerges in the chiral derived center: the pair $(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is the bulk-boundary datum. The modular characteristic~$\kappa(\cA)$ determines the curved $A_\infty$ deformation at genus $g \ge 1$, complementarity lifts to the bulk-boundary-line triangle, and the discriminant~$\Delta$ classifies the complexity of bulk-boundary pairs. Classical Koszul duality is genus~$0$ on the formal disk; Volume~I is genus~$g$ on a curve; Volume~II is the dimensional lift to $\C \times \R$.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:263:The bar-cobar adjunction on $\SCchtop$-algebras is a Quillen
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1704:The holographic Lagrangian $\cL_\cA^{(0)}$ is constructed from genus-$0$ data: the bar-cobar adjunction on $\FM_k(\C) \times \Conf_k^<(\R)$. \emph{Is the holographic Lagrangian complete?} That is, does $\cL_\cA^{(0)}$ extend to a family $\cL_\cA^{(g)} \hookrightarrow \cM_{\mathrm{vac}}$ over the moduli $\overline{\cM}_{g,n}$, compatible with gluing along boundary strata? For algebras with clean self-intersection (classes~$\mathbf{G}$ and~$\mathbf{L}$: Heisenberg, Kac--Moody), the Lagrangian meets itself transversally and the scalar curvature $d^2 = \kappa(\cA) \cdot \omega_g$ extends automatically. For algebras with excess self-intersection (class~$\mathbf{M}$: Virasoro, $\mathcal{W}_N$), the derived self-intersection carries higher Tor, the Swiss-cheese operations $m_k$ are successive obstruction classes, and the question is open. (Classes~$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$ are chirally Koszul: the PBW spectral sequence concentrates and bar cohomology is concentrated. Class~$\mathbf{M}$ has infinite shadow depth and non-formal Swiss-cheese structure: the fourth-order pole forces nonvanishing transferred operations $m_k^{\mathrm{SC}} \neq 0$ for all $k \geq 3$, though the algebra is chirally Koszul (PBW spectral sequence concentrates) and well-defined Koszul duals exist. The difficulty for class~$\mathbf{M}$ is the non-formality: beyond the global self-intersection geometry, the big Koszul dual carries higher $\Ainf$ operations.) This is the central problem of the modular programme: existence, compatibility, and computation of the higher-genus Lagrangian, developed in Part~\ref{part:holography}.
/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_factorization_modular_engine.py:251:        """Bar-cobar for SC_mod is a Quillen equivalence."""
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/line_operators_engine.py:26:   Koszul, so bar B(SC) has cohomology concentrated in degree 0.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/line_operators_engine.py:230:    """Verify bar complex concentration for SC^{ch,top} at small arities.
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/line_operators_engine.py:309:        from lib.sc_bar_cobar_engine import SCArityData, sc_arity_dimensions
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/full_volume_math_catalogue_2026-04-08.md:213:- [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L48) still marks `SC \leftrightarrow HT prefactorization` as `ProvedHere`.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/full_volume_math_catalogue_2026-04-08.md:222:- [chapters/connections/affine_half_space_bv.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex#L1726) still claims the half-space programme is complete for any logarithmic `\SCchtop`-algebra.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:100:- **POSITIVE -- key theorem labels resolve.** Spot-checked thm:rosetta-swiss-cheese, thm:homotopy-Koszul, thm:cohomology_PVA, thm:YBE, thm:boundary-linear-bulk-boundary, thm:lines_as_modules, thm:3d-universal-mc, thm:affine-monodromy-identification, thm:bar-is-self-intersection, thm:holographic-reconstruction, thm:complete-strictification, thm:general-half-space-bv, thm:doubling-rwi, thm:bulk-boundary-line-factorization, thm:modular-bar, thm:formal-genus-expansion, thm:synthesis, thm:resolvent-principle, thm:SC-self-duality. All resolve via grep across chapters/. PASS.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 567

resume_20260413_163457/S14_standalone_to_main.md:3:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:4:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:6:- [HIGH] [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:1515) — PROBLEM: line 1515 reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and line 3658 later says the bar differential/coproduct encode the closed/open colours. The corrected manuscript surface uses `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )` and keeps `SC^{ch,top}` off the bar complex: see [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466) and [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247). FIX: swap the pair order at line 1515, and replace the line-3658 sentence with “the bar complex is the `E_1` coalgebraic engine; the closed/open Swiss-cheese colours live on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:7:- [HIGH] [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) — PROBLEM: lines 995–997 say the bar differential “encodes the closed colour” and the coproduct “the open colour.” That is exactly the AP165/ B55–B56 retracted formulation; the corrected rule is in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1257). FIX: replace those lines with “the bar complex classifies twisting morphisms and carries an `E_1` differential plus deconcatenation coproduct; the Swiss-cheese closed/open colours belong to the derived center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:544:/bin/zsh -lc "rg -n -C 2 'bar complex.*Swiss|Swiss-cheese.*bar complex|bar complex.*SC|SC.*bar complex|Swiss-cheese-formal bar|bar complexes; algebras|bar complex is.*coalgebra|bar complex.*coalgebra' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
resume_20260413_163457/S14_standalone_to_main.md:569:I find this interesting! I need to take a closer look at lines 659 and so on. It seems there might be something not stale with the bar complex E1, which could lead to a Swiss-cheese effect emerging at the derived center. I want to carefully inspect those lines to understand what's happening around there. Let's see if I can uncover something important or if my assumptions need adjustment!
resume_20260413_163457/S14_standalone_to_main.md:878:/bin/zsh -lc "rg -n -C 1 'SC-algebra|SC-coalgebra|The bar complex carrying both structures|bar complex.*Swiss-cheese|bar complex.*SC|Swiss-cheese.*pair' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
resume_20260413_163457/S14_standalone_to_main.md:880:standalone/survey_track_b_compressed.tex:1489:bar complex, the shadow tower, the Swiss-cheese structure, the
resume_20260413_163457/S14_standalone_to_main.md:888:standalone/survey_modular_koszul_duality_v2.tex:4152:bar complex, the shadow tower, the Swiss-cheese structure, the
resume_20260413_163457/S14_standalone_to_main.md:1349:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:1350:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:1352:- [HIGH] [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:1515) — PROBLEM: line 1515 reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and line 3658 later says the bar differential/coproduct encode the closed/open colours. The corrected manuscript surface uses `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )` and keeps `SC^{ch,top}` off the bar complex: see [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466) and [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247). FIX: swap the pair order at line 1515, and replace the line-3658 sentence with “the bar complex is the `E_1` coalgebraic engine; the closed/open Swiss-cheese colours live on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:1353:- [HIGH] [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) — PROBLEM: lines 995–997 say the bar differential “encodes the closed colour” and the coproduct “the open colour.” That is exactly the AP165/ B55–B56 retracted formulation; the corrected rule is in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1257). FIX: replace those lines with “the bar complex classifies twisting morphisms and carries an `E_1` differential plus deconcatenation coproduct; the Swiss-cheese closed/open colours belong to the derived center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
tmp_standalone_audit/survey_v2_xr.tex:4158:bar complex, the shadow tower, the Swiss-cheese structure, the
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:38:- PROBLEM at [qc_math_surfaces.json](/Users/raeez/chiral-bar-cobar/compute/audit/vol1_full_audit_2026_04_08/qc_math_surfaces.json:724): generated audit metadata still normalized the false prefix “The bar complex presents the Swiss-cheese coalgebra.” EXACT edit applied: changed that normalized prefix to “The ordered bar complex is an `E_1` coalgebra and does not itself present the Swiss-cheese datum ...”.
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:399:healing_20260413_130533/H11_SC_formal_alt.md:403:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:400:healing_20260413_130533/H11_SC_formal_alt.md:410:CLAUDE.md:881:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:403:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1840,1875p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
curve independence). Path (v): the Gepner model uses the Virasoro
stress tensor for each $c = 3/2$ factor, giving $\kappa_{\mathrm{ch}} = c/2 = 3/4$
per factor; the physical sigma model has the full $\cN = 4$
structure whose $\kappa_{\mathrm{ch}} = 2$ is lower due to supersymmetric
Ward identities. Path (vi) follows from the additivity of $\kappa_{\mathrm{ch}}$
under tensor products
(Vol~I, Proposition~\ref{prop:independent-sum-factorization}).
\end{proof}

\begin{remark}[$\kappa_{\mathrm{ch}}(K3) = 2 \neq c/2 = 3$: modular characteristic vs central charge]
\label{rem:ap48-k3}
\index{modular characteristic!K3 example}
The K3 sigma model provides a sharp illustration: the
modular characteristic $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$ differs from the
Virasoro formula $c/2 = 3$. The reduction arises because the
$\cN = 4$ superconformal Ward identities constrain the genus-$1$
obstruction below what the Virasoro subalgebra alone would produce.
The naive Virasoro computation $\kappa_{\mathrm{ch}}(\mathrm{Vir}_6) = 3$ counts
the Virasoro contribution, but the full $\cN = 4$ algebra at $c = 6$
has $\kappa_{\mathrm{ch}} = 2k_R = 2$.
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "Swiss-cheese bar" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
notes/physics_bv_brst_cy.tex:586: \item \textbf{The closed string field theory and $\mathcal{W}$-algebras.} For CY3, the closed string sector is controlled by the BCOV theory, whose algebraic structure is a $\mathcal{W}$-algebra (the vertex algebra of polyvector fields with Schouten bracket and $\partial$ operator). The full open-closed BV-BRST complex should be the Swiss-cheese bar complex $B_{\SC}(A_\cC)$, combining the $\mathcal{W}$-algebra (bulk) with $G(X)$ (boundary) via the open-closed coupling.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '40,120p' /Users/raeez/chiral-bar-cobar-vol2/AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Volume I built the categorical logarithm: the bar construction `B(A)` for chiral algebras on curves, with theorems proving existence, inversion, branch structure, leading coefficient, and coefficient ring. Volume II reads that machine in three dimensions.

The bar complex `B(A)` is an E_1 chiral coassociative coalgebra carrying two structures:

- a differential `d_B` from OPE residues on `FM_k(C)`, encoding the holomorphic chiral product;
- a coproduct `Delta` from ordered deconcatenation on `Conf_k(R)`, encoding the topological interval-cutting.

These make `B(A)` a dg coassociative coalgebra. It is NOT an `SC^{ch,top}`-coalgebra: `B(A)` is a single E_1 coalgebra, not a two-colored SC datum.

The `SC^{ch,top}` structure emerges in the chiral derived center construction. The chiral Hochschild cochain complex `C^bullet_{ch}(A,A)` (defined via the chiral endomorphism operad `End^{ch}_A` with spectral parameters from `FM_k(C)`, NOT via topological Hochschild cochains `RHom_{A^e}(A,A)`) carries brace operations and a Gerstenhaber bracket. The pair `(C^bullet_{ch}(A,A), A)` is the `SC^{ch,top}` datum: bulk (chiral Hochschild cochains) acts on boundary (the algebra `A`) via braces. Open-to-closed is empty: bulk restricts to boundary, not conversely.

Critical distinction:

- `B(A)` is an E_1 coassociative coalgebra classifying twisting morphisms (Theorem A);
- the `SC^{ch,top}` structure lives on the pair `(C^bullet_{ch}(A,A), A)`, NOT on `B(A)`;
- bulk observables are the chiral derived center `Z^{der}_{ch}(A) = H^*(C^bullet_{ch}(A_b, A_b))` of a boundary chart, Morita-invariant in the open-sector factorization dg-category.

At genus `g >= 1`, the curved structure is essential: the non-vanishing of higher `A_infinity` operations is the curved bar structure `d^2 = kappa(A) * omega_g`. Formality fails because the logarithm acquires monodromy.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '120,160p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\midrule
$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
$1$ & Kac--Moody $\widehat{\fg}_k$ & $\Omega/((k{+}h^\vee)z)$ & $\mathbf{L}$ \\
$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
$2N{-}1$ & $\mathcal{W}_N$ & poles through $z^{-(2N-1)}$
 & $\mathbf{M}$ \\
\bottomrule
\end{tabular}
\end{center}

\noindent
This table encodes a structural dichotomy: algebras whose
collision residue has at most a simple pole (classes~$\mathbf{G}$
and~$\mathbf{L}$) have finite shadow depth and
Swiss-cheese-formal bar complexes; algebras with higher-order
poles (class~$\mathbf{M}$) have infinite shadow towers and
genuinely non-formal $A_\infty$-structure.

The dichotomy is not a property of individual OPE coefficients
but of the collision residue as a whole: the $d\log$ absorption
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '260,310p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
$d_{\barB}([s^{-1}J]) = 0$ (no unary OPE), so the differential
commutes with the cut. The coderivation property
$\Delta \circ d_{\barB} = (d_{\barB} \otimes \id + \id \otimes
d_{\barB}) \circ \Delta$ is the algebraic statement that the
holomorphic collision $z_1 \to z_2$ is independent of the
topological cut $t_* \in (t_1, t_2)$: collisions in $\C$ commute
with cuts in $\R$.

\section*{The Swiss-cheese identification}

A bar element of degree~$k$ is parametrised by
$\FM_k(\C) \times \Conf_k^<(\R)$:
the differential sees $\FM_k(\C)$, the coproduct sees
$\Conf_k^<(\R)$. This product is the operation space of the
two-coloured operad $\SCchtop$ (the chiral-topological Swiss-cheese operad, constructed in detail in \S\ref{sec:SC-operad-foundations} below): closed colour from $\FM_k(\C)$,
open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
an $E_1$ chiral coassociative coalgebra
(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
Section~\ref{sec:foundations} in general).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese-formal bar" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:879:resume_20260413_163457/S14_standalone_to_main.md:3:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:880:resume_20260413_163457/S14_standalone_to_main.md:4:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:883:resume_20260413_163457/S14_standalone_to_main.md:544:/bin/zsh -lc "rg -n -C 2 'bar complex.*Swiss|Swiss-cheese.*bar complex|bar complex.*SC|SC.*bar complex|Swiss-cheese-formal bar|bar complexes; algebras|bar complex is.*coalgebra|bar complex.*coalgebra' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:888:resume_20260413_163457/S14_standalone_to_main.md:1349:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:889:resume_20260413_163457/S14_standalone_to_main.md:1350:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:892:relaunch_20260413_111534/S14_standalone_to_main.md:13:- [HIGH] `standalone/programme_summary.tex:1414` and `standalone/programme_summary.tex:1783`, plus `standalone/programme_summary_sections5_8.tex:58` — PROBLEM: these summaries assign Swiss-cheese formality to the *bar complex* and even to classes `G/L` together. The chapter surface defines SC-formality as a property of the algebra/open-closed higher operations and singles out only class `G`. FIX: replace “Swiss-cheese-formal bar complex(es)” with “finite shadow depth; SC-formality is stronger and selects exactly class `G`,” and rewrite the gauge-theory item as “class `G` is SC-formal; class `L` has one surviving cubic correction.”
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
resume_20260413_163457/S14_standalone_to_main.md:3:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:4:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:407:standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
resume_20260413_163457/S14_standalone_to_main.md:544:/bin/zsh -lc "rg -n -C 2 'bar complex.*Swiss|Swiss-cheese.*bar complex|bar complex.*SC|SC.*bar complex|Swiss-cheese-formal bar|bar complexes; algebras|bar complex is.*coalgebra|bar complex.*coalgebra' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
resume_20260413_163457/S14_standalone_to_main.md:553:standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
resume_20260413_163457/S14_standalone_to_main.md:559:standalone/programme_summary.tex:1812: $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
resume_20260413_163457/S14_standalone_to_main.md:1093:/bin/zsh -lc "rg -n -C 2 'Swiss-cheese-formal bar|SC-formal bar|SC-formality.*bar|bar complex \\(\\"'$m_k'"\\"'^'"\\{SC\\}\\"'$'"' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
resume_20260413_163457/S14_standalone_to_main.md:1096:standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
resume_20260413_163457/S14_standalone_to_main.md:1102:standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
resume_20260413_163457/S14_standalone_to_main.md:1108:standalone/programme_summary.tex:1812: $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
resume_20260413_163457/S14_standalone_to_main.md:1349:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
resume_20260413_163457/S14_standalone_to_main.md:1350:- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
tmp_standalone_audit/wrap_programme_summary_sections5_8_fixed.tex:119:Swiss-cheese-formal bar complexes; algebras with higher-order
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '360,430p' chapters/theory/hochschild_calculus.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 vector space;
 \item The CY structure class $[\sigma] \in \HC^-_d(\cC)$
 determines a preferred splitting of the Hodge filtration;
 \item In the commutative case $\cC = \Perf(X)$, the
 categorical Hodge filtration recovers the classical Hodge
 filtration on $H^n_{\mathrm{dR}}(X)$ via HKR.
\end{enumerate}
\end{proposition}

\begin{remark}[Bridge to the shadow obstruction tower]
\label{rem:hodge-shadow-bridge}
%: always subscript kappa in Vol III.
Under the CY-to-chiral functor $\Phi$ (Part~\ref{part:bridge}), the categorical
Hodge filtration maps to the weight filtration on the modular
convolution algebra $\mathfrak{g}^{\mathrm{mod}}_A$. The
associated graded pieces correspond to the degree-stratified
components of the shadow obstruction tower:
\begin{center}
\begin{tabular}{lll}
\toprule
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '300,340p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textbf{Structure} & Bar differential $d_{\barB}$ &
 Deconcatenation $\Delta$ \\
\textbf{Physics} & Holomorphic factorization & Topological
 factorization \\
\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
 $T^c(s^{-1}\bar\cA)$ \\
\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
 Deconcatenation ($n+1$ terms) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The closed colour is the holomorphic factorization of
Section~\ref{sec:bar}: the bar differential extracts OPE
residues, produces $d^2 = 0$ at genus~$0$, and acquires
curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
open colour is the topological factorization: the
deconcatenation coproduct splits an ordered sequence at every
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '140,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
**Anti-patterns to avoid**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding.

## Codex-Native Operating Stance

- Default deliverable: a verified change or a precisely named blocker, not an outline.
- Default reasoning: `medium`.
- Escalate to `high` or `xhigh` only for load-bearing proof surgery, chapter-scale architecture, or stalled frontier synthesis after the workflow itself has already been sharpened.
- No plan theater.
  If a plan exists, it must cash out into edits, checks, or a blocker.
- Tool persistence.
  The first plausible answer is not enough; stop only when the relevant falsifier passes or the blocker is real.
- Dependency-first execution.
  Read before editing. Verify prerequisites before downstream claims.
- Parallel evidence gathering.
  Batch independent greps, file reads, log checks, and targeted tests whenever they do not couple tightly.
- Skill-first specialization.
  If a task matches a repo skill, use the skill instead of reconstructing the workflow from scratch.
- `AGENTS.md`, `CLAUDE.md`, README files, and prior agent prose are operational guides, not mathematical evidence.

## Programme Identity (Crystallized 2026-04-12)
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '400,460p' compute/lib/e1_bar_cobar_cy3.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

    gen_a = E1Generator("a", weight=1, degree=0)

    # At the self-dual point (h2=0): the OPE is purely second-order pole.
    # At generic h2: the structure function g(z) introduces corrections.
    # For the single Heisenberg channel, the OPE is always a(z)a(w) ~ k/(z-w)^2
    # with k = 1 (the deformation affects higher-spin channels).
    return CY3ChiralOPE(
        name=f"W_{{1+inf}} (h1={h1}, h2={h2}, h3={h3})",
        generators=(gen_a,),
        ope_data={("a", "a"): {2: Rational(1)}},
        bracket_data={("a", "a"): None},
        kappa_value=Fraction(1),
    )


# =========================================================================
#  3.  E₁ bar complex B^{E₁}(A_C)
# =========================================================================

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1400,1460p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
power of $(z - w)$. For a chiral algebra with OPE poles of
maximal order~$p$, the collision residue has poles of
order~$p - 1$.

% ====================================================================
\subsection{Pole-order dichotomy}
\label{ssec:pole-dichotomy}
% ====================================================================

The maximal pole order of the collision residue separates the
standard landscape into two regimes:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{clcl}
\toprule
\textbf{Pole order} & \textbf{Algebra}
 & \textbf{Collision} & \textbf{Class} \\
\midrule
$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2020,2065p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection{Corollaries}

\begin{corollary}[Reduced HT line category for the affine lineage; \ClaimStatusProvedHere]
\label{cor:affine-line-category}
\index{line operators!affine identification}
For $\fg$ simple and $k$ generic, the reduced HT line category (the monodromic braided monoidal category of Corollary~\textup{\ref{cor:braided-category}}), restricted to evaluation modules, is equivalent as a braided monoidal category to $\mathrm{Rep}_q(\fg)$ at $q = e^{i\pi/(k + h^\vee)}$:
\[
 \cC_{\mathrm{line}}^{\mathrm{red}}\big|_{\mathrm{eval}} \;\simeq\; \mathrm{Rep}_q(\fg).
\]
\end{corollary}

\begin{proof}
Theorem~\ref{thm:affine-monodromy-identification}(iii) identifies the braiding and associator. The monoidal structure (tensor product of evaluation modules) is the same on both sides. The equivalence follows from the reconstruction theorem for braided monoidal categories: a braided monoidal category with the same objects, morphisms, associator, and braiding is equivalent.
\end{proof}

\begin{corollary}[Jones polynomial from the bar complex; \ClaimStatusProvedHere]
\label{cor:jones-polynomial}
\index{Jones polynomial|textbf}
\index{Kontsevich integral}
For $\fg = \mathfrak{sl}_2$ at level $k$, the bar complex integrals over $\FM_n(\CC) \times \Conf_n(\RR)$, evaluated on the fundamental weight system of $\mathfrak{sl}_2$, compute the colored Jones polynomial $J_K(q)$ of a framed knot $K$ at $q = e^{i\pi/(k+2)}$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1770,1825p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{ssec:4d-3d-2d}
% ====================================================================

The three volumes of the programme correspond to three levels
of a dimensional hierarchy:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{cllll}
\toprule
\textbf{$d$} & \textbf{Level} & \textbf{Operadic type}
 & \textbf{Key datum} & \textbf{Volume} \\
\midrule
$4$ & CY source & $E_2$
 & CY category $\mathcal{C}$ & III \\
$3$ & Swiss-cheese & $E_1$
 & $R$-matrix $r(z)$ & II \\
$2$ & Modular shadow & $E_\infty$
 & $\kappa(\cA)$ & I \\
\bottomrule
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '60,120p' notes/physics_bv_brst_cy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\newcommand{\FM}{\overline{\mathrm{FM}}}
\newcommand{\Ger}{\mathrm{Ger}}
\newcommand{\QME}{\mathrm{QME}}
\newcommand{\MC}{\mathrm{MC}}
\newcommand{\DGCat}{\mathbf{dgCat}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cC}{\mathcal{C}}
\newcommand{\cD}{\mathcal{D}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cM}{\mathcal{M}}
\newcommand{\cO}{\mathcal{O}}
\newcommand{\cZ}{\mathcal{Z}}
\newcommand{\frakg}{\mathfrak{g}}
\DeclareMathOperator{\obs}{obs}
\DeclareMathOperator{\colim}{colim}

\title{BV-BRST Formalism for CY Categories\\and the Bar Complex}
\author{Raeez Lorgat}
\date{April 2026}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '10,60p' /Users/raeez/chiral-bar-cobar-vol2/compute/lib/line_operators_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  SC(k, m; o) = FM_k(C) x E_1(m)  [open output]
  SC(k, m; c) = FM_k(C)            [closed output, m must be 0]

Key mathematical facts:

1. **FM_k(C)** (Fulton-MacPherson on C): real dimension 2(k-1) for k >= 2,
   a point for k=1, empty for k=0. Euler characteristic chi = k!.
   Top Betti: b_{2(k-1)} = (k-1)! (Arnold).

2. **E_1(m)** (little intervals): contractible for m >= 2, a point for m=1.
   dim = 0 (homologically trivial).

3. **No open-to-closed**: SC(k, m; closed) = empty when m > 0. Bulk
   interactions restrict to boundaries but not conversely.

4. **Homotopy-Koszulity** (thm:homotopy-Koszul): SC^{ch,top} is homotopy-
   Koszul, so bar B(SC) has cohomology concentrated in degree 0.

References:
  Vol II: thm:homotopy-Koszul, line-operators chapter, SC operad chapter
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1600,1640p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textbf{Structure} & Bar differential $d_{\barB}$ &
 Deconcatenation $\Delta$ \\
\textbf{Physics} & Holomorphic factorization & Topological
 factorization \\
\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
 $T^c(s^{-1}\bar\cA)$ \\
\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
 Deconcatenation ($n+1$ terms) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The closed colour is the holomorphic factorization of
Section~\ref{sec:bar}: the bar differential extracts OPE
residues, produces $d^2 = 0$ at genus~$0$, and acquires
curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
open colour is the topological factorization: the
deconcatenation coproduct splits an ordered sequence at every
wait(call_lzBcCLzko23Ia6kr5anxwbSM) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,60p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\providecommand{\HH}{\operatorname{HH}}
\providecommand{\Har}{\operatorname{Har}}

\section{Bulk--boundary functoriality and spectral $R(z)$}
\label{sec:bulk-boundary-R}
\label{sec:spectral_braiding}
\label{sec:spectral-braiding}
\label{chap:spectral-braiding}
\label{sec:bulk-boundary}

The Yangian $Y(\fg)$ is the universal quantization of the classical $r$-matrix $r(z) = k\,\Omega/z$. Yet the RTT formalism that defines it treats the spectral parameter $z$ as a formal variable, the Hopf coproduct as a given axiom, and the Yang--Baxter equation as a constraint to be verified. None of these are \emph{explained}: the spectral parameter has no geometric origin, the Hopf coproduct has no universal property, and the YBE is an identity without a cause.

The $E_1$ bar construction resolves all three deficiencies at once. The ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with its deconcatenation coproduct \emph{is} the Yangian's coproduct: the spectral parameter is the coordinate on $\C$ (the holomorphic direction), the coproduct arises from the $E_1$-factorization along the topological half-line $\R_{\ge 0}$, and the Yang--Baxter equation is Stokes' theorem on the Fulton--MacPherson compactification $\FM_3(\C)$. The $\SCchtop$ structure emerges not on $B(A)$ itself but on the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ of chiral Hochschild cochains and boundary algebra is the $\SCchtop$ datum. The symmetric bar $B^\Sigma$ is the $\Sigma_n$-coinvariant shadow; $R$-matrix descent relates $B^{\mathrm{ord}}$ to $B^\Sigma$.

The spectral $R$-matrix $R(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta^{\mathrm{oc}})$ is the genus-$0$, degree-$2$ collision residue of the open/closed MC element, extracted from the bulk-to-boundary composition of two parallel line operators. It equals the Laplace transform of the chiral $\lambda$-bracket (Proposition~\ref{prop:field-theory-r}), placing the RTT relation, the Sklyanin bracket, the Drinfeld presentation, and the PVA descent on a single geometric footing.

\subsection{Boundary data and factorization module structure}
\label{subsec:boundary-module}
The geometric content enters through the boundary. Let $A=(A_{\mathsf{ch}},A_{\mathsf{top}})$ be a $C_\ast\!\bigl(W(\mathsf{SC}^{\mathrm{ch,top}})\bigr)$-algebra.
A topological boundary condition along $t=0$ is a \emph{right $W(\mathsf{SC}^{\mathrm{ch,top}})$-module} $M$ supported on $\C\times \R_{\ge 0}$: a prefactorization algebra $\mathsf{Obs}^{\partial}$ on half-rectangles with actions
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"bar.*SC|B\\(A\\).*SC|coalgebra.*SC\" --no-heading --hidden" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:163:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
AGENTS.md:165:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.
AGENTS.md:167:**The E_n operadic circle (2026-04-12):** E_3(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.
AGENTS.md:299:  - SC^{ch,top} structural correction: B(A) is E_1 coalgebra, NOT SC-coalgebra (AP165); SC is NOT self-dual (AP166);
AGENTS.md:701:B(A) is E_1 coalgebra          # NOT SC-coalgebra; SC on derived center pair
AGENTS.md:723:"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra; SC in derived center pair (AP165)
AGENTS.md:749:**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
AGENTS.md:835:- `AP165` B(A) not attributed SC structure;
chapters/examples/toroidal_elliptic.tex:1867:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1868:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
notes/physics_bv_brst_cy.tex:388:\begin{definition}[$E_1$ coalgebra structure on $B(A)$ and the $\SC^{\mathrm{ch,top}}$ open-closed pair, cf.~Vol~II]
notes/physics_bv_brst_cy.tex:405:\begin{warning}[$B(A)$ does not carry $\SC^{\mathrm{ch,top}}$-algebra structure]
notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.
notes/physics_bv_brst_cy.tex:586: \item \textbf{The closed string field theory and $\mathcal{W}$-algebras.} For CY3, the closed string sector is controlled by the BCOV theory, whose algebraic structure is a $\mathcal{W}$-algebra (the vertex algebra of polyvector fields with Schouten bracket and $\partial$ operator). The full open-closed BV-BRST complex should be the Swiss-cheese bar complex $B_{\SC}(A_\cC)$, combining the $\mathcal{W}$-algebra (bulk) with $G(X)$ (boundary) via the open-closed coupling.
chapters/theory/braided_factorization.tex:262:a Swiss-cheese ($\SC^{\mathrm{ch,top}}$) coalgebra. The SC structure of
compute/tests/test_kodaira_spencer_e1_engine.py:295:        bar = KSBarComplex(KSChiralAlgebra(q))
compute/tests/test_kodaira_spencer_e1_engine.py:302:        bar = KSBarComplex(KSChiralAlgebra(q))
compute/tests/test_kodaira_spencer_e1_engine.py:311:        bar = KSBarComplex(KSChiralAlgebra(q))
compute/tests/test_kodaira_spencer_e1_engine.py:331:        bar = KSBarComplex(KSChiralAlgebra(q))
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex presents the Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 89ms:
Total output lines: 200

audit_campaign_20260412_231034/T20_gerstenhaber.md:126:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
CLAUDE.md:920:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
audit_campaign_20260412_231034/XV05_topologization_xvol.md:129:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
working_notes.tex:8022:\emph{the bar complex presents the Swiss-cheese algebra, as the
audit_campaign_20260412_231034/T14_topologization.md:111:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
audit_campaign_20260412_231034/AP20_over_point_P1.md:110:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
wave2_audit_20260413_001942/F01_definitions_bar.md:166:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
wave2_audit_20260413_001942/F01_definitions_bar.md:584:   845	AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
audit_campaign_20260412_231034/AP04_bare_A_bar.md:212:CLAUDE.md:845:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
audit_campaign_20260412_231034/XV04_SC_claims_xvol.md:137:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
healing_20260413_130533/H11_SC_formal_alt.md:403:CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
healing_20260413_130533/H11_SC_formal_alt.md:410:CLAUDE.md:881:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
fix_wave_D_20260413_182434/D17_chapter_openings_v2.md:12148:   `bar complex presents the Swiss-cheese`,
fix_wave_D_20260413_182434/D17_chapter_openings_v2.md:12446:   `bar complex presents the Swiss-cheese`,
fix_wave_D_20260413_182434/D17_chapter_openings_v2.md:12780:   `bar complex presents the Swiss-cheese`,
fix_wave_D_20260413_182434/D17_chapter_openings_v2.md:13089:   `bar complex presents the Swiss-cheese`,
fix_wave_D_20260413_182434/D17_chapter_openings_v2.md:13427:   `bar complex presents the Swiss-cheese`,
collab wait(call_GjcBbpTVfGHcdxa2ZjXAPgOG)
  receivers: 019d87fa-7f86-79e3-9153-ac3a76799974, 019d87fa-7f8a-7511-8db8-e23f75eff083, 019d87fa-7f9d-76c2-85ed-bdce297b4d1a
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '8000,8045p' working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$m_k\big|_{\mathrm{scalar}} = (c/12)\,P_k$) is equivalent to
inverting the Shapovalov form at all levels---the same problem as
constructing all Virasoro singular vectors.  The generating
function is the graviton self-energy resolvent
\[
G(t;\lambda)
  = \mathrm{Tr}_{\fh}\!\left(\frac{1}{1 - t\,K(\lambda)}\right),
\]
where $K(\lambda)$ is the collision kernel at conformal
weight~$\lambda$.  At the symmetric point $\lambda = (c-1)/24$
(where $\Delta = \bar\Delta$), a universal factor $(x+2)$ appears
in $P_k$ for all $k \leq 5$---this is the conformal weight Ward
identity forcing a zero at $x = -2$.  Whether the factor persists
at all arities is tied to the question of whether the Shapovalov
determinant has a universal factorisation beyond the
Kac determinant formula.

\subsection{AP-OC Steinberg refinement}
\label{subsec:ap-oc-steinberg}

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*Swiss-cheese" -n /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:71:- "the bar complex presents the Swiss-cheese algebra"
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1078:$A_\infty$~chiral algebra, bar complex, Swiss-cheese operad,
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14564:   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14595:  `bar complex presents the Swiss-cheese`,
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:157:they make the bar complex a coalgebra over the Swiss-cheese
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149:The bar complex presents the Swiss-cheese algebra, as the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:200:\index{three bar complexes!Swiss-cheese decomposition}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:1351:\index{three bar complexes!Swiss-cheese provenance}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:48:MC element, bar complex, and Swiss-cheese structure exist
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:2048:compared is not ``the bar complex as a Swiss-cheese algebra'': the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:379:\,d\lambda$ produces the infinitesimal braiding, and the full quantum $R(z)$ produces the finite braiding. For the affine lineage, this is proved unconditionally: one-loop exactness collapses the $A_\infty$ tower, on the reduced evaluation comparison surface the reduced HT monodromy identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares that monodromy with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\fg)$ there (Theorem~\ref{thm:affine-monodromy-identification}). On the $\mathfrak{sl}_2$ weight system, the bar complex integrals over $\FM_n(\C) \times \Conf_n(\R)$ compute the colored Jones polynomial (Corollary~\ref{cor:jones-polynomial}), recovering the Reshetikhin--Turaev invariant directly from the Swiss-cheese structure. The all-types categorical Clebsch--Gordan and
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"B\\(A\\).*SC\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md:299:  - SC^{ch,top} structural correction: B(A) is E_1 coalgebra, NOT SC-coalgebra (AP165); SC is NOT self-dual (AP166);
AGENTS.md:701:B(A) is E_1 coalgebra          # NOT SC-coalgebra; SC on derived center pair
AGENTS.md:723:"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra; SC in derived center pair (AP165)
AGENTS.md:749:**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
AGENTS.md:835:- `AP165` B(A) not attributed SC structure;
chapters/theory/cy_to_chiral.tex:2054:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
chapters/theory/introduction.tex:13:A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
notes/physics_bv_brst_cy.tex:388:\begin{definition}[$E_1$ coalgebra structure on $B(A)$ and the $\SC^{\mathrm{ch,top}}$ open-closed pair, cf.~Vol~II]
notes/physics_bv_brst_cy.tex:405:\begin{warning}[$B(A)$ does not carry $\SC^{\mathrm{ch,top}}$-algebra structure]
notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '120,190p' /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\newcommand{\dzero}{d_0}
\newcommand{\dfib}{d_{\mathrm{fib}}}
\newcommand{\Dtot}{D_{\mathrm{tot}}}
\newcommand{\normord}[1]{:\!#1\!:}
\newcommand{\Zder}{\cZ^{\mathrm{der}}_{\mathrm{ch}}}

\DeclareMathOperator{\gr}{gr}
\DeclareMathOperator{\Spec}{Spec}
\DeclareMathOperator{\Conf}{Conf}
\DeclareMathOperator{\Sym}{Sym}
\DeclareMathOperator{\diag}{diag}

\declaretheorem[style=notesdef, name=Computation, sibling=theorem]{computation}

% Separator
\newcommand{\sep}{\bigskip\begin{center}$*$\end{center}\medskip}

% Blackboard bold (used in working notes but not defined in monograph preamble)
\providecommand{\bR}{\mathbb{R}}
\providecommand{\bC}{\mathbb{C}}
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "bar complex.*Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/swiss_cheese_cy3_e1.py:4:of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.

thinking
**Collecting positive Swiss-cheese claims**

I'm gathering all genuine positive statements in the repo that explicitly say the bar complex presents or has Swiss-cheese algebra structure. I'll focus mainly on the `working_notes`, `standalone` files, and maybe `chapters`, searching and filtering carefully for positive assertions without negations, to compile a comprehensive list with classifications and snippets.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1,160p' compute/lib/swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.

Connects Vol II's SC^{ch,top} theory to the CY3-derived E_1 algebras
of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
where the E_1 (associative/ordered) direction is the R-direction
(boundary) and the chiral direction is the C-direction (bulk).

MATHEMATICAL BACKGROUND:
========================

1. SC^{E_1,ch} OPERAD FOR E_1-CHIRAL ALGEBRAS FROM CY3.
   Vol II proves (thm:homotopy-Koszul, def:SC-operations) that B(A) is
   an algebra over SC^{ch,top} = FM(C) x Conf(R). For CY3-derived E_1
   algebras, the E_1 direction is PRIMITIVE data: the factorization on
   ordered configurations comes from the CoHA multiplication (critical
   equivariant cohomology), NOT from a symmetric OPE.

   The SC^{E_1,ch} operad has operation spaces:
     SC^{E_1,ch}(n_c, n_o) = FM_{n_c}(C) x Conf^{ord}_{n_o}(R)
   where n_c = number of closed (bulk/chiral) inputs,
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex presents the Swiss-cheese" chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex | sed -n '140,210p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   140	\providecommand{\bZ}{\mathbb{Z}}
   141	\providecommand{\bQ}{\mathbb{Q}}
   142	\providecommand{\bN}{\mathbb{N}}
   143	
   144	\title{\textit{Working Notes on $\Ainf$ Chiral Algebras\\
   145	and 3D Holomorphic-Topological QFT}}
   146	\author{Raeez Lorgat}
   147	\date{2024--2026}
   148	
   149	\begin{document}
   150	\maketitle
   151	
   152	\begin{abstract}
   153	The $1$-form $\eta_{ij} = d\log(z_i - z_j)$ acquires a second
   154	direction.  OPE residues on~$\mathrm{FM}_k(\mathbb{C})$ give the
   155	bar differential; ordered deconcatenation
   156	on~$\mathrm{Conf}_k(\mathbb{R})$ gives the coproduct.  Together
   157	they make the bar complex a coalgebra over the Swiss-cheese
   158	cooperad, the operadic fingerprint
   159	of a $3$d holomorphic-topological field theory
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2130,2250p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
sed: chapters/theory/factorization_swiss_cheese.tex: No such file or directory
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex | sed -n '1120,1185p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1120	\item The \textbf{bulk} is
  1121	  $A_{\mathrm{bulk}} \simeq \cO(T^*[-1]\cL)$: polyvector fields
  1122	  on the Lagrangian.  Note: the restriction
  1123	  $\cO(\cM)|_\cL = \cO(\cL)$ is the boundary, not the bulk.
  1124	  The bulk retains the full $(-1)$-shifted cotangent fibre.
  1125	\item The \textbf{boundary} is $B_\partial = \cO(\cL)$: functions
  1126	  on the Lagrangian.
  1127	\item The \textbf{line category} is
  1128	  $\cC_{\mathrm{line}} = \mathfrak{S}_b\text{-mod}$: modules for
  1129	  the self-intersection algebra
  1130	  $\mathfrak{S}_b = \cL \times_\cM \cL$.
  1131	\end{itemize}
  1132	
  1133	The equivalence $\Zder(B_\partial) \simeq A_{\mathrm{bulk}}$ is
  1134	the Hochschild--Kostant--Rosenberg theorem: Hochschild cochains of
  1135	$\cO(\cL)$ are polyvector fields on $T^*[-1]\cL \simeq \cM|_\cL$,
  1136	by the Lagrangian condition
  1137	$T_\cL\cM / T\cL \simeq T^*\cL[-1]$.
  1138	
  1139	The equivalence $\cC_{\mathrm{line}} \simeq \cA^!\text{-mod}$ is

thinking
**Identifying affirmative misclaims**

I'm planning to search the codebase for positive claims that the bar complex B(A) has a Swiss-cheese algebra structure, focusing on lines that affirm this without negations. I'll gather file locations, snippets, and brief classifications for each confirmed misclaim. This involves running searches for keywords like "Swiss-cheese" and filtering out any negated statements. Let's explore this carefully!
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:224:AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
AGENTS.md:43:- **E_1-chiral bialgebra**: the correct Hopf framework (NOT E_∞ vertex bialgebra). Axioms in `e1_chiral_algebras.tex` §7 (~400 lines). Coproduct on E_1 (ordered) side of Swiss-cheese; E_∞ averaging kills Hopf data.
AGENTS.md:169:**SC^{ch,top} != E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.
compute/lib/swiss_cheese_chart_gluing.py:1:r"""Swiss-cheese decomposition over quiver charts for CY3 atlas gluing.
compute/lib/swiss_cheese_chart_gluing.py:4:to the CY3 chart-gluing setting.  The Swiss-cheese operad SC^{ch,top}
compute/lib/swiss_cheese_chart_gluing.py:207:    """Full Swiss-cheese data on a single chart.
compute/lib/swiss_cheese_chart_gluing.py:753:    """Result of gluing Swiss-cheese data over charts.
compute/lib/swiss_cheese_chart_gluing.py:947:    """Glue Swiss-cheese data for the conifold 2-chart atlas.
compute/lib/swiss_cheese_chart_gluing.py:949:    This is the complete Swiss-cheese gluing computation:
compute/lib/swiss_cheese_chart_gluing.py:988:    """Glue Swiss-cheese data for C^3 (trivial single-chart atlas).
compute/lib/swiss_cheese_chart_gluing.py:1036:    """Multi-path verification of the conifold Swiss-cheese gluing.
compute/lib/swiss_cheese_chart_gluing.py:1361:    """Entry in the Swiss-cheese landscape census."""
compute/lib/swiss_cheese_chart_gluing.py:1428:    This is the top-level entry point for the Swiss-cheese chart gluing
compute/lib/swiss_cheese_chart_gluing.py:1433:    # 1. Swiss-cheese chart data
compute/lib/hms_shadow_equivalence.py:1277:        # would appear in the Swiss-cheese structure, not the scalar shadow.
compute/lib/cross_volume_shadow_bridge.py:5:  Vol II (~/chiral-bar-cobar-vol2): Swiss-cheese, PVA descent, open/closed, 3D HT QFT
compute/lib/cross_volume_shadow_bridge.py:289:    r"""Whether the family is Swiss-cheese formal.
compute/lib/cross_volume_shadow_bridge.py:486:    r"""Import Swiss-cheese directionality check from Vol II.
compute/lib/c3_grand_verification.py:1092:    Vol II: kappa(H_1) = 1 (from Swiss-cheese formality, class G)
compute/lib/swiss_cheese_cy3_e1.py:1:r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1060,1095p' /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Three-dimensional quantum gravity is the climax: the
Virasoro $\lambda$-bracket generates ten movements from the
$\Ainf$ Koszul triangle through gravitational S-duality
$c \mapsto 26 - c$ to derived-center bulk reconstruction.
The boundary chiral algebra determines the bulk via
Hochschild cochains (proved boundary-linear; global triangle
conjectural beyond the Koszul locus).
\end{abstract}

\bigskip
\noindent
\textbf{2020 Mathematics Subject Classification.}
Primary 18M75, 17B69;
Secondary 81T70, 18N70, 81T30, 55R80.

\medskip
\noindent
\textbf{Keywords.}
$A_\infty$~chiral algebra, bar complex, Swiss-cheese operad,
holomorphic--topological field theory, Poisson vertex algebra,
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"B\\(A\" compute/lib/swiss_cheese_*" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/swiss_cheese_cy3_e1.py:12:   Vol II proves (thm:homotopy-Koszul, def:SC-operations) that B(A) is

thinking
**Summarizing positive Swiss-cheese bar complex mentions**

I’m gathering specific file locations and line numbers where positive statements about the Swiss-cheese-formal bar complex appear, focusing on snippets that discuss classifications, color assignments, and algebra presentations. I plan to extract excerpts from several `.tex` files and notes in the root repo, compiling a clear list of these sections with references to actual lines. This will help precisely document the user’s highlighted content without venturing into other repositories.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese-formal bar" -l' in /Users/raeez/chiral-bar-cobar succeeded in 64ms:
standalone/programme_summary_sections5_8.tex
resume_20260413_163457/S14_standalone_to_main.md
relaunch_20260413_111534/S14_standalone_to_main.md
standalone/programme_summary.tex
tmp_standalone_audit/wrap_programme_summary_sections5_8_fixed.tex
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md
resume_20260413_165929/S14_standalone_to_main.md
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"B\\(A\" compute/lib/swiss_cheese_chart_gluing.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '350,410p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 51ms:
$\alpha_{12} \wedge \alpha_{23}
+ \alpha_{23} \wedge \alpha_{31}
+ \alpha_{31} \wedge \alpha_{12} = 0$
on $H^\bullet(\Conf_3(\C))$, with $\mathfrak{g}$-valued
Casimir decorations (see Remark~\ref{rem:IHX-Arnold} of
spectral-braiding-core). For the affine lineage,
one-loop exactness (Theorem~\ref{thm:one-loop-koszul})
forces $m_3 = 0$, so the degree-$3$ bar differential
involves only pairwise collisions, exactly the chord
diagram sector. The unique $\mathfrak{sl}_2$ invariant
$w_3 = \sum f^{abc}f^{abc} = 8$ matches the degree-$3$
coefficient $v_3(3_1) = 1$.

\medskip
\noindent\textbf{Status.}
The degree-by-degree matching at $n \le 3$ is unconditional
for the $\mathfrak{sl}_2$ weight system: it uses the proved
spectral $R$-matrix
(Corollary~\ref{cor:jones-polynomial}), the proved one-loop
exactness, and the proved Arnold cancellation
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "closed colour" standalone' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/three_dimensional_quantum_gravity.tex:680:(closed colour) acts on the boundary (open colour). This is the
standalone/en_chiral_operadic_circle.tex:1080: \emph{closed colour} (bulk), carrying $\Etwo$ from
standalone/en_chiral_operadic_circle.tex:1149: No mixed operations with closed output: the closed colour
standalone/en_chiral_operadic_circle.tex:1247: The closed colour is a Lie coalgebra
standalone/en_chiral_operadic_circle.tex:1253: carrying the closed colour and the boundary
standalone/en_chiral_operadic_circle.tex:2839: (Proposition~\ref{prop:e-koszul-dual-sc}): the closed colour
standalone/programme_summary_sections5_8.tex:314:The closed colour is the holomorphic factorization of
standalone/sc_chtop_pva_descent.tex:140:$\SCchtop$, with closed colour $\FM_k(\CC)$, open colour
standalone/sc_chtop_pva_descent.tex:146:for the closed colour composed with Livernet's Koszulity of the
standalone/sc_chtop_pva_descent.tex:220:$\SCchtop$.  The closed colour is the bulk; the open colour is
standalone/sc_chtop_pva_descent.tex:235:  the closed colour, and transferred to $\SCchtop$ via
standalone/sc_chtop_pva_descent.tex:241:  (Theorem~\ref{thm:SC-koszul-dual}).  The closed colour
standalone/sc_chtop_pva_descent.tex:299:variant $\SCchtop$ replaces the $\Etwo$ closed colour by
standalone/sc_chtop_pva_descent.tex:427:The operad $\SCchtop$ replaces the $\Etwo$ closed colour by
standalone/sc_chtop_pva_descent.tex:468:$\SCchtop$-algebra.  The closed colour is the bulk; the open
standalone/sc_chtop_pva_descent.tex:502:\subsection{Formality of the closed colour}
standalone/sc_chtop_pva_descent.tex:504:The closed colour of $\SCchtop$ is the FM-operad
standalone/sc_chtop_pva_descent.tex:518:\begin{remark}[Formality is for the closed colour, not the
standalone/sc_chtop_pva_descent.tex:520:Kontsevich formality applies to the closed colour of $\SCchtop$
standalone/sc_chtop_pva_descent.tex:555:a chain of quasi-isomorphisms connecting the closed colour
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "E_1 bar complex.*Swiss-cheese"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/swiss_cheese_cy3_e1.py:4:of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '320,360p' /Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

## Cross-Volume: Vol III 6d hCS Session (2026-04-12/13, ~170 agents)

Key Vol III results affecting Vol II:
- **E_1-chiral bialgebra** (e1_chiral_algebras.tex §7, ~490 lines): the correct Hopf framework for chiral quantum groups. Uses Vol II's Swiss-cheese operad SC^{ch,top} and ordered bar B^{ord}. The coproduct Δ_z lives on the E_1 (open/topological) side. The E_∞ averaging forgets the Hopf structure: av(r(z)) = κ_ch.
- **Universal coproduct from Miura**: Δ_z(e_s) = Σ C(N_R-b,k) z^k e_a^L·e_b^R. All spins in closed form. z-degree = s. Extends Vol II's spin-2 Drinfeld coproduct to arbitrary spin.
- **ZTE failure**: the E_3 3-particle S-operator requires corrections beyond pairwise YBE. These corrections connect to the Vol II shadow tower via the A_∞ coproduct theory.
- **Holomorphic CS hierarchy**: 3d→5d→6d produces E_1→E_2→E_3. The Vol II E_1 sector IS the boundary algebra of 5d hCS (Costello 2013). The 6d extension gives quantum toroidal algebras.
- **E_2→E_3 promotion**: the DERIVED center HH*(B,B) (algebraic, E_n→E_{n+1}), NOT iterated Drinfeld center Z(Z(C)). BZFN agreement only at E_1→E_2 level.
- See ~/calabi-yau-quantum-groups/FRONTIER.md F13-F24 for full details.

## Cross-Volume: Chiral Quantum Group Session (2026-04-12/13, Vol I primary)

Key Vol I results affecting Vol II:

- **E_3 identification PROVED** (thm:e3-identification): Z^{der}_{ch}(V_k(g)) ≅ CFG A^lambda for simple g. Proof via E_3 formality + 1-dim H^3(g). Alternative proof via Dunn (prop:e3-via-dunn) bypasses HDC entirely. The E_n circle CLOSES. Extended to gl_N.
- **gl_N chiral QG for all N** (thm:glN-chiral-qg): Yang R-matrix R(u) = uI + Psi·P, Drinfeld coproduct as N×N matrix multiplication. Non-trivial RTT for N ≥ 2. Central qdet uses DECREASING column index (FM33).
- **Antipode does NOT lift** (rem:antipode-ope-analysis): S(T(u))=T(u)^{-1} fails as vertex algebra (anti-)homomorphism. Two obstructions: OPE (quartic pole shift) and Hopf axiom (z·J residual). Source: Miura nonlinearity.
- **Conformal anomaly = c/2 = kappa**: quantitative obstruction to constant coproduct. At c=0 constant exists; c≠0 forces spectral parameter.
- **Sign convention harmonized**: nabla = d-A throughout (23 fixes in standalone). Vol II KZB already used d-A.
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "Swiss-cheese" compute/lib/swiss_cheese_cy3_e1.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '980,1010p' standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1:r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.
4:of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
233:    For Swiss-cheese: the number of TREES (generators) at arity (n_c, n_o)
941:    """Swiss-cheese formality data for a CY3-derived E_1 algebra.
1009:    """Complete landscape census of CY3 Swiss-cheese data."""
 succeeded in 51ms:
factorization, and the open/closed mixed sector encodes the
action of bulk on boundary. Without this operadic habitat, the
bar coproduct has no definition and the line-operator category
has no foundation.

The primitive object of 3d HT quantum field theory on
$\bC_z \times \bR_t$ is not the bar complex but the open/closed
factorization dg-category $\cC$ on the bordified curve
$\widetilde X_D$. Objects are boundary conditions, morphisms
are open-string states, and a vacuum $b$ produces a boundary
algebra $A_b = \End_\cC(b)$ only up to Morita equivalence. The
governing operad is $\SCchtop$; it is homotopy-Koszul (proved
via Kontsevich formality), so the bar-cobar adjunction on
$\SCchtop$-algebras is a Quillen equivalence.

The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
its differential encodes the closed colour, and its coproduct
the open colour. Three objects must never be conflated:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the \emph{bar complex} $\barB(A_b)$ classifies twisting
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '220,260p' compute/lib/swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
def sc_e1_operation_count(n_c: int, n_o: int) -> int:
    """Number of generators of the SC^{E_1,ch} operad at arity (n_c, n_o).

    For the E_1 direction: n_o! orderings (since ordered configurations
    have n_o! connected components when discretized to a lattice).
    For the closed direction: 1 (the FM compactification is connected).

    Total: n_o! for n_o >= 1, 1 for n_o = 0.

    But actually, for the operad, the generators are the top cells:
    for the Stasheff associahedron, there is 1 top cell in each dimension.
    The correct count is the Euler characteristic of the operation space.

    For Swiss-cheese: the number of TREES (generators) at arity (n_c, n_o)
    is the number of planar trees with n_c + n_o leaves, n_c of which
    are marked "closed" (unordered among themselves) and n_o are "open"
    (ordered).

    For small arities we just enumerate.
    """
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"bar complex\" standalone | grep -i 'closed colour'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "bar complex" compute/lib/swiss_cheese_cy3_e1.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4:of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
34:   The E_1 bar complex uses only the ORDERED bar construction:
38:   For the full bar complex (E_inf): B^{Sigma}_k(A) = (s^{-1}A)^{tensor k} / S_k.
39:   The E_1 bar complex has STRICTLY MORE generators than the E_inf bar complex
75:   The E_1 bar complex has FEWER symmetrization terms than E_inf.
102:   for a genuinely E_1 algebra, B^{ord} IS the canonical bar complex.
151:  Vol I:  bar_cobar_adjunction_curved.tex (bar complex)
264:    """Dimensions of the E_1 bar complex at each bar degree.
285:    """Compute E_1 and E_inf bar complex dimensions.
575:    For the E_1 bar complex: the quartic contact invariant is the SAME
576:    as for the E_inf bar complex, because the contact term is CYCLIC
878:    invariant. The E_1 bar complex has more generators at each arity,
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"bar complex.*SC\" -g'*'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:1867:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1868:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
AGENTS.md:165:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.
AGENTS.md:167:**The E_n operadic circle (2026-04-12):** E_3(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.
AGENTS.md:749:**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
chapters/theory/introduction.tex:13:A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
chapters/theory/cy_to_chiral.tex:2054:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.
notes/physics_bv_brst_cy.tex:586: \item \textbf{The closed string field theory and $\mathcal{W}$-algebras.} For CY3, the closed string sector is controlled by the BCOV theory, whose algebraic structure is a $\mathcal{W}$-algebra (the vertex algebra of polyvector fields with Schouten bracket and $\partial$ operator). The full open-closed BV-BRST complex should be the Swiss-cheese bar complex $B_{\SC}(A_\cC)$, combining the $\mathcal{W}$-algebra (bulk) with $G(X)$ (boundary) via the open-closed coupling.
compute/lib/e1_bar_cobar_cy3.py:424:    The E₁ bar complex uses ORDERED tensor products and the HOCHSCHILD
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6110,6165p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The passage from algebraic geometry to physics is through the
derived centre.

On the product $\bC_z \times \bR_t$, the holomorphic direction
produces the bar differential of Sections~1--9, extracting OPE
residues from collisions in the holomorphic plane. The
topological direction produces the deconcatenation coproduct,
splitting an ordered tensor sequence at a cut point of the real
line. The two are unified by the \emph{holomorphic-topological
Swiss-cheese operad} $\SCchtop$: closed colour
$\mathrm{ch} = \FM_k(\bC)$ governs holomorphic factorization,
open colour $\mathrm{top} = E_1(m)$ governs topological
factorization, and the open/closed mixed sector encodes the
action of bulk on boundary.

The primitive object of 3d HT quantum field theory on
$\bC_z \times \bR_t$ is not the bar complex but the open/closed
factorization dg-category $\cC$ on the bordified curve
$\widetilde X_D$. Objects are boundary conditions, morphisms
are open-string states, and a vacuum $b$ produces a boundary
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*SC" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1,40p' compute/lib/swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1600,1635p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.

Connects Vol II's SC^{ch,top} theory to the CY3-derived E_1 algebras
of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
where the E_1 (associative/ordered) direction is the R-direction
(boundary) and the chiral direction is the C-direction (bulk).

MATHEMATICAL BACKGROUND:
========================

1. SC^{E_1,ch} OPERAD FOR E_1-CHIRAL ALGEBRAS FROM CY3.
   Vol II proves (thm:homotopy-Koszul, def:SC-operations) that B(A) is
   an algebra over SC^{ch,top} = FM(C) x Conf(R). For CY3-derived E_1
   algebras, the E_1 direction is PRIMITIVE data: the factorization on
   ordered configurations comes from the CoHA multiplication (critical
   equivariant cohomology), NOT from a symmetric OPE.

   The SC^{E_1,ch} operad has operation spaces:
     SC^{E_1,ch}(n_c, n_o) = FM_{n_c}(C) x Conf^{ord}_{n_o}(R)
   where n_c = number of closed (bulk/chiral) inputs,
 succeeded in 51ms:
The depth gap $d_{\mathrm{alg}} \ne 3$ is forced because
no configuration of $(S_3, S_4)$ with $S_4 \ne 0$ can
produce $S_5 = S_6 = \cdots = 0$.


% ================================================================
% 7. SC-FORMALITY AND CLASS G
% ================================================================

\section{SC-formality characterizes
class~$\mathbf{G}$}\label{sec:sc-formal}

The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$ is a
two-coloured operad governing the interaction of a bulk
algebra (closed colour) with a boundary algebra (open
colour). A chirally Koszul vertex algebra~$\cA$ is
\emph{SC-formal} if the transferred Swiss-cheese operations
$m_k^{\mathrm{SC}}$ vanish for all $k \ge 3$.

\begin{proposition}[SC-formality iff class
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex" /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
157:they make the bar complex a coalgebra over the Swiss-cheese
171:bar complex, the five theorems, the shadow obstruction tower.
173:a second direction, what the bar complex becomes when read in
186:The bar complex of a chiral algebra $\cA$ on a curve $X$ carries
326:the bar complex's native role: a representability theorem for
417:The bar complex makes this visible.  The bar \textit{differential}
596:on cohomology.  The bar complex is quadratic.  The Koszul dual
623:Volume~I's five theorems: bar complex exists (Theorem~A), boundary
680:The two-arc cover produces the two-sided bar complex, which is
681:the cyclic bar complex.  In the homotopy category:
726:The proof is Koszul duality on the open colour.  The bar complex
1047:\item The bar complex $\barB(A_b)$ encodes the twisting data
1149:The bar complex presents the Swiss-cheese algebra, as the
1242:\item ``The bar complex is the bulk algebra.''  The bar complex
1442:The bar complex of a chiral algebra $\cA$ lives on the product
1505:The bar complex of a chiral algebra on a curve carries a
1625:The bar complex $\barB(\cA)$ classifies couplings between boundary
1634:This is the bar complex's role: a representability theorem.  It
1646:$\barB(\cA) \neq \Zder(\cA)$.  The bar complex is a Fourier
1674:The two-arc cover produces the two-sided bar complex, which is the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/programme_summary_sections5_8.tex | sed -n '120,145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   120	\midrule
   121	$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
   122	$1$ & Kac--Moody $\widehat{\fg}_k$ & $\Omega/((k{+}h^\vee)z)$ & $\mathbf{L}$ \\
   123	$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
   124	$2N{-}1$ & $\mathcal{W}_N$ & poles through $z^{-(2N-1)}$
   125	 & $\mathbf{M}$ \\
   126	\bottomrule
   127	\end{tabular}
   128	\end{center}
   129	
   130	\noindent
   131	This table encodes a structural dichotomy: algebras whose
   132	collision residue has at most a simple pole (classes~$\mathbf{G}$
   133	and~$\mathbf{L}$) have finite shadow depth and
   134	Swiss-cheese-formal bar complexes; algebras with higher-order
   135	poles (class~$\mathbf{M}$) have infinite shadow towers and
   136	genuinely non-formal $A_\infty$-structure.
   137	
   138	The dichotomy is not a property of individual OPE coefficients
   139	but of the collision residue as a whole: the $d\log$ absorption
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "bar complex" notes/theory_coha_e1_sector.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
542:The $E_2$ bar complex $B_{E_2}(G(X))$ (see the main text, Chapter 9) has:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '150,210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Since $\Phi = \phi \times \mathrm{id}$ on mixed operations and
$\phi$ intertwines $\gamma^{\FM}$, we get
\[
 \Phi \circ \gamma_{\mathrm{mix}}
 = (\phi \circ \gamma^{\FM}) \times (\mathrm{id} \circ \mathrm{id}_{E_1})
 = (\gamma^{E_2} \circ (\phi \otimes \phi)) \times \mathrm{id}_{E_1}
 = \gamma_{\mathrm{mix}}^{\mathrm{SC}} \circ (\Phi \otimes \Phi),
\]
and likewise for open insertions. The no-open-to-closed rule is
preserved trivially (both sides are empty).

\smallskip\noindent
\emph{Equivariance:}
The $\Sigma_k$-equivariance on the closed color and the identity on
the open color are preserved because $\phi$ is $\Sigma_k$-equivariant
and the product decomposition respects the symmetric group
action on the $\FM$-factor with the trivial action on $E_1$.

\smallskip
Thus $\Phi$ is a map of two--colored dg operads. The map $\Phi$ is a
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/programme_summary_sections5_8.tex | sed -n '292,325p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   292	
   293	\begin{center}
   294	\renewcommand{\arraystretch}{1.3}
   295	\begin{tabular}{lll}
   296	\toprule
   297	& \textbf{Closed colour} & \textbf{Open colour} \\
   298	\midrule
   299	\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
   300	\textbf{Structure} & Bar differential $d_{\barB}$ &
   301	 Deconcatenation $\Delta$ \\
   302	\textbf{Physics} & Holomorphic factorization & Topological
   303	 factorization \\
   304	\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
   305	\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
   306	 $T^c(s^{-1}\bar\cA)$ \\
   307	\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
   308	 Deconcatenation ($n+1$ terms) \\
   309	\bottomrule
   310	\end{tabular}
   311	\end{center}

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba compute/lib/swiss_cheese_cy3_e1.py | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.
     2	
     3	Connects Vol II's SC^{ch,top} theory to the CY3-derived E_1 algebras
     4	of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
     5	where the E_1 (associative/ordered) direction is the R-direction
     6	(boundary) and the chiral direction is the C-direction (bulk).
     7	
     8	MATHEMATICAL BACKGROUND:
     9	========================
    10	
    11	1. SC^{E_1,ch} OPERAD FOR E_1-CHIRAL ALGEBRAS FROM CY3.
    12	   Vol II proves (thm:homotopy-Koszul, def:SC-operations) that B(A) is
    13	   an algebra over SC^{ch,top} = FM(C) x Conf(R). For CY3-derived E_1
    14	   algebras, the E_1 direction is PRIMITIVE data: the factorization on
    15	   ordered configurations comes from the CoHA multiplication (critical
    16	   equivariant cohomology), NOT from a symmetric OPE.
    17	
    18	   The SC^{E_1,ch} operad has operation spaces:
    19	     SC^{E_1,ch}(n_c, n_o) = FM_{n_c}(C) x Conf^{ord}_{n_o}(R)
    20	   where n_c = number of closed (bulk/chiral) inputs,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/programme_summary.tex | sed -n '1410,1445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1410	standard landscape into two regimes:
  1411	
  1412	\begin{center}
  1413	\renewcommand{\arraystretch}{1.3}
  1414	\begin{tabular}{clcl}
  1415	\toprule
  1416	\textbf{Pole order} & \textbf{Algebra}
  1417	 & \textbf{Collision} & \textbf{Class} \\
  1418	\midrule
  1419	$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
  1420	$1$ & Kac--Moody $\widehat{\fg}_k$ & $k\,\Omega/z$ & $\mathbf{L}$ \\
  1421	$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
  1422	$2N{-}1$ & $\cW_N$ & poles through $z^{-(2N-1)}$
  1423	 & $\mathbf{M}$ \\
  1424	\bottomrule
  1425	\end{tabular}
  1426	\end{center}
  1427	
  1428	\noindent
  1429	This table encodes a structural dichotomy: algebras whose
thinking
**Examining claim locations and classifications**

I'm verifying all occurrences of positive claims, especially near line 157 in `chapters/connections/line-operators` and other candidate files from search results. I want to assign clear, concise classification labels describing the claim severity or type, and accurately capture file and line numbers using numbered line outputs for precise referencing. This will help me deliver a well-organized summary of all claim sites with their classifications.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '2030,2065p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2030	
  2031	\begin{proof}
  2032	Theorem~\ref{thm:affine-monodromy-identification}(iii) identifies the braiding and associator. The monoidal structure (tensor product of evaluation modules) is the same on both sides. The equivalence follows from the reconstruction theorem for braided monoidal categories: a braided monoidal category with the same objects, morphisms, associator, and braiding is equivalent.
  2033	\end{proof}
  2034	
  2035	\begin{corollary}[Jones polynomial from the bar complex; \ClaimStatusProvedHere]
  2036	\label{cor:jones-polynomial}
  2037	\index{Jones polynomial|textbf}
  2038	\index{Kontsevich integral}
  2039	For $\fg = \mathfrak{sl}_2$ at level $k$, the bar complex integrals over $\FM_n(\CC) \times \Conf_n(\RR)$, evaluated on the fundamental weight system of $\mathfrak{sl}_2$, compute the colored Jones polynomial $J_K(q)$ of a framed knot $K$ at $q = e^{i\pi/(k+2)}$.
  2040	\end{corollary}
  2041	
  2042	\begin{proof}
  2043	The argument has two steps: one proved here, one classical.
  2044	
  2045	\medskip
  2046	\noindent\textbf{Step 1 (Braid representation from the bar complex).}
  2047	The bar complex of $V^k(\mathfrak{sl}_2)$, viewed as a logarithmic $\SCchtop$-algebra, produces a flat connection on configuration spaces by Theorem~\ref{thm:synthesis}. By Theorem~\ref{thm:affine-monodromy-identification}(i)--(ii), on the reduced evaluation comparison surface the monodromy of this connection identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares it with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$. In particular, the bar complex computes the braid-group representation
  2048	\[
  2049	 \rho_n^{\mathrm{HT}} = \rho_n^{\mathrm{KZ}} \colon B_n \longrightarrow \Aut(V^{\otimes n})
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/programme_summary.tex | sed -n '1775,1825p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1775	
  1776	\begin{center}
  1777	\renewcommand{\arraystretch}{1.3}
  1778	\begin{tabular}{cllll}
  1779	\toprule
  1780	\textbf{$d$} & \textbf{Level} & \textbf{Operadic type}
  1781	 & \textbf{Key datum} & \textbf{Volume} \\
  1782	\midrule
  1783	$4$ & CY source & $E_2$
  1784	 & CY category $\mathcal{C}$ & III \\
  1785	$3$ & Swiss-cheese & $E_1$
  1786	 & $R$-matrix $r(z)$ & II \\
  1787	$2$ & Modular shadow & $E_\infty$
  1788	 & $\kappa(\cA)$ & I \\
  1789	\bottomrule
  1790	\end{tabular}
  1791	\end{center}
  1792	
  1793	\noindent
  1794	At each level, information is lost. From 4d to 3d, one

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1230,1255p' /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Annulus trace & $S^1$ excision &
  \textsc{green} \\[3pt]
Full modular cooperad & Bordered FM + log extension &
  \textsc{amber} \\[3pt]
BV/BRST $=$ bar at $g \geq 1$ & Genus-$g$ QME
  & \textsc{red}
\end{tabular}
\end{center}

\subsection*{Five false ideas to dismiss}

\begin{enumerate}[nosep]
\item ``The bar complex is the bulk algebra.''  The bar complex
  classifies twisting morphisms.  The bulk is the derived center.
  These are different objects produced by different functors.
\item ``The boundary algebra determines the theory.''  The boundary
  algebra is a chart of the open-sector category, not its essence.
  Different compact generators produce Morita-equivalent charts.
  The category is the invariant.
\item ``Modularity is a property of the closed algebra.''  It is a
thinking
**Summarizing misleading docstring claims**

I'll organize the findings into a clear, concise final message highlighting the misleading docstring around lines 4 and 11-16 in the indicated file, including quoted snippets and precise classification while excluding negation references as requested.
codex
Found 1 remaining affirmative claim in this volume that still conflates the bar complex with Swiss-cheese structure (all other hits were negations or clarifications):

- `compute/lib/swiss_cheese_cy3_e1.py:4-16`  
  “The E₁ bar complex has a Swiss-cheese algebra structure … Vol II proves … B(A) is an algebra over SC^{ch,top} = FM(C) × Conf(R).”  
  *Classification:* misleading docstring asserting that B(A) carries the Swiss-cheese algebra structure (contrary to AP165).
wait(call_GjcBbpTVfGHcdxa2ZjXAPgOG) 1 agents complete:
  019d87fa-7f9d-76c2-85ed-bdce297b4d1a completed: "Found 1 remaining affirmative claim in this volume that still conflates the bar complex with Swiss-cheese structure (all…"
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/programme_summary.tex | sed -n '1590,1630p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1590	This product is the operadic fingerprint of the Swiss-cheese
  1591	operad:
  1592	
  1593	\begin{center}
  1594	\renewcommand{\arraystretch}{1.3}
  1595	\begin{tabular}{lll}
  1596	\toprule
  1597	& \textbf{Closed colour} & \textbf{Open colour} \\
  1598	\midrule
  1599	\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
  1600	\textbf{Structure} & Bar differential $d_{\barB}$ &
  1601	 Deconcatenation $\Delta$ \\
  1602	\textbf{Physics} & Holomorphic factorization & Topological
  1603	 factorization \\
  1604	\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
  1605	\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
  1606	 $T^c(s^{-1}\bar\cA)$ \\
  1607	\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
  1608	 Deconcatenation ($n+1$ terms) \\
  1609	\bottomrule

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/survey_track_b_compressed.tex | sed -n '950,1015p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   950	the Gaussian base. The nontrivial zeros of the component
   951	$L$-functions are the scattering resonances of the hyperbolic
   952	Laplacian on $\cM_{1,1}$: frequencies at which the genus-$1$
   953	sewing amplitude fails to decay.
   954	
   955	\medskip\noindent\textbf{Genus-$2$ B\"ocherer bridge.}
   956	For the Leech lattice VOA, the Siegel modular form
   957	$\chi_{12} = \mathrm{SK}(f_{22})$ is the Saito--Kurokawa lift
   958	of the unique weight-$22$ cuspidal eigenform, and the
   959	MC-derived second Fourier coefficient $c_2 \approx
   960	-1.918 \times 10^{-6} \neq 0$ is the first nonzero central
   961	$L$-value produced by the shadow obstruction tower,
   962	connecting $\Theta_\cA$ to genus-$2$ Siegel modular forms via
   963	the Furusawa--Morimoto theorem.
   964	
   965	
   966	% ====================================================================
   967	\section*{10.\quad The open/closed world (Volume II)}
   968	% ====================================================================
   969	
thinking
**Evaluating agent statuses**

I’m noticing that only one agent has returned. I’m wondering if there are others still running. It seems that the wait function returns the status of one or more agents, but maybe those other agents are still active? I need to check the status of each one individually to be sure. It’s sort of puzzling, and I want to be precise in understanding what’s going on!
codex
One volume already surfaced a concrete affirmative claim in a Vol III compute docstring. I’m waiting on the Vol I and Vol II sweeps before I patch, so I can edit the whole writable surface in one pass and avoid leaving local drift.
collab wait(call_6J5LJTKifRe8B1mIPEcjE1Gn)
  receivers: 019d87fa-7f86-79e3-9153-ac3a76799974, 019d87fa-7f8a-7511-8db8-e23f75eff083

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '6100,6165p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  6100	% ====================================================================
  6101	
  6102	Sections~1--9 construct $E_n$-chiral algebras as
  6103	algebraic-geometric objects on curves: bar complexes on every
  6104	curve geometry, $R$-matrices, Yangian structures, derived chiral
  6105	centres carrying $E_2$/$E_3$ structure, and the
  6106	$\SCchtop$ datum on the pair
  6107	$(\cZ^{\der}_{\ch}(\cA),\, \cA)$. Volume~II discovers that
  6108	these constructions are physics: the derived chiral centre IS the
  6109	bulk algebra of a real 3d holomorphic-topological gauge theory.
  6110	The passage from algebraic geometry to physics is through the
  6111	derived centre.
  6112	
  6113	On the product $\bC_z \times \bR_t$, the holomorphic direction
  6114	produces the bar differential of Sections~1--9, extracting OPE
  6115	residues from collisions in the holomorphic plane. The
  6116	topological direction produces the deconcatenation coproduct,
  6117	splitting an ordered tensor sequence at a cut point of the real
  6118	line. The two are unified by the \emph{holomorphic-topological
  6119	Swiss-cheese operad} $\SCchtop$: closed colour
thinking
**Investigating search limitations with multiline patterns**

I'm looking into why search patterns with dots aren't catching multiline references to the bar complex and Swiss-cheese in working_notes. It looks like newlines are splitting phrases, so I'll try searching just for "Swiss-cheese" in working_notes to find relevant context more reliably.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese" /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
157:they make the bar complex a coalgebra over the Swiss-cheese
163:and curved Swiss-cheese at genus~$g \ge 1$ where
232:two-coloured Swiss-cheese operad $\SCchtop$ has operation spaces
247:and compatible with $d_{\barB}$: these are the Swiss-cheese
254:The Swiss-cheese algebra becomes \textit{curved}.  The failure of
287:of the theorem: the two colours of the Swiss-cheese operad arise
295:algebra).  Without it, the Swiss-cheese structure would be a
379:\section{The Swiss-cheese pentagon}
429:The Swiss-cheese operad is Koszul.
433:The chiral-topological Swiss-cheese operad $\SCchtop$ is
439:(1)~the classical Swiss-cheese operad is Koszul
456:The holomorphic Swiss-cheese algebra, projected to cohomology,
876:as an axiom.  The Swiss-cheese framework reverses this.
883:The modular Swiss-cheese operad extends $\SCchtop$ by replacing
896:ordinary to curved Swiss-cheese algebras.  The modular MC element
936:Modular Swiss-cheese $d^2 = 0$ & proved (by $\partial^2 = 0$ on
1149:The bar complex presents the Swiss-cheese algebra, as the
1159:Swiss-cheese algebra on $\FM_k(\C) \times \Conf_k(\R)$; its
1457:\textbf{Steinberg} & \textbf{Swiss-cheese} \\
1507:direction); together these form a Swiss-cheese algebra on
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba working_notes.tex | sed -n '7990,8035p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7990	$k \mapsto -k - 2h^\vee$ does not cancel completely.  The three
  7991	operations---Koszul duality, FF involution, negative-level
  7992	substitution---share surface similarities but differ in every
  7993	family beyond the free field, confirming AP33 at the level of
  7994	explicit formulas.
  7995	
  7996	\subsection{Shapovalov obstruction for closed-form $m_k$}
  7997	\label{subsec:shapovalov-obstruction}
  7998	
  7999	A closed form for the Virasoro scalar polynomials $P_k$ (where
  8000	$m_k\big|_{\mathrm{scalar}} = (c/12)\,P_k$) is equivalent to
  8001	inverting the Shapovalov form at all levels---the same problem as
  8002	constructing all Virasoro singular vectors.  The generating
  8003	function is the graviton self-energy resolvent
  8004	\[
  8005	G(t;\lambda)
  8006	  = \mathrm{Tr}_{\fh}\!\left(\frac{1}{1 - t\,K(\lambda)}\right),
  8007	\]
  8008	where $K(\lambda)$ is the collision kernel at conformal
  8009	weight~$\lambda$.  At the symmetric point $\lambda = (c-1)/24$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3330,3375p' /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the \emph{hyperbolic geometry of the function that
$q$-series defines}: its growth, its equidistribution, its
spectral decomposition.  The passage from $q$-series to
hyperbolic geometry requires:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{A positive-definite inner product} on the
  function space (axiom AU1), to define the Hilbert space
  $L^2(\cM_{1,1})$ on which $\Delta_H$ acts.
\item \emph{Growth bounds} on $Z(\tau)$ as
  $\mathrm{Im}(\tau) \to \infty$ (axiom AU2), to place
  $Z$ in the correct Sobolev space.
\item \emph{Convergence of the spectral decomposition}
  (axiom AU3), to make the Roelcke--Selberg expansion
  meaningful.
\item \emph{Spectral gap control} (axiom AU4), to
  quantify the equidistribution rate.
\end{enumerate}
These are precisely the axioms (AU1)--(AU4) of the analytic
unitary $\SCchtop$-algebra
(Definition~\ref{def:analytic-unitary-SC}).  The analytic
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex" standalone/sc_chtop_pva_descent.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
174:The bar complex of a chiral algebra carries two independent
208:The bar complex itself does not carry the answer.  It is the
260:\begin{warning}[The bar complex is not an
262:The bar complex $\barB(\cA) = T^c(s^{-1}\barA)$ is an $\Eone$
270:the bar complex as a resolution.  The bar complex is the
279:$|s^{-1}v| = |v| - 1$.  The bar complex uses the augmentation
469:colour is the boundary.  The bar complex $\barB(\cA)$ is used
1018:preserves all boundary strata.  On the bar complex, translation
1034:map.  On the bar complex, this exchanges
1361:bar complex is flat).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '150,220p' standalone/sc_chtop_pva_descent.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
in particular $\SCchtop$ is \emph{not} Koszul self-dual
($\dim\SCchtop_{\mathrm{cl}}(n) = 1$ versus
$\dim(\SCchtop)^!_{\mathrm{cl}}(n) = (n-1)!$).
Third, the cogenerator projections of the bar differential
produce $\Ainf$ operations $\{m_k\}_{k \geq 1}$ whose Stasheff
relations are Stokes' theorem on $\FM_n(\CC)$; on cohomology
these descend to the five axioms of a Poisson vertex algebra.
The descent is computed in three cases:
the Heisenberg algebra (formal, class~G, shadow depth zero),
affine Kac--Moody at level~$k$ (Lie-transverse, class~L, shadow
depth one), and $\cW_3$ (infinite tower, class~M).
\end{abstract}

\maketitle
\tableofcontents


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Introduction: two colours, one operad}
\label{sec:introduction}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "presents the Swiss-cheese" /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1149:The bar complex presents the Swiss-cheese algebra, as the
3361:complex presents the Swiss-cheese algebra.  Neither presents
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex of Volume" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
tmp_standalone_audit/survey_v2_xr.tex:3664:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1008:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1008:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
standalone/survey_modular_koszul_duality_v2.tex:6135:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
standalone/survey_modular_koszul_duality.tex:6070:The bar complex of Volume~I is an $E_1$-chiral coassociative
standalone/survey_track_b_compressed.tex:995:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
resume_20260413_163457/S14_standalone_to_main.md:581:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
resume_20260413_163457/S14_standalone_to_main.md:616:The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
chapters/frame/preface_sections10_13_draft.tex:26:only up to Morita equivalence. The bar complex of Volume~I is the
chapters/frame/preface.tex:4037:only up to Morita equivalence. The bar complex of Volume~I is the
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:742:> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:1122:   202	> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:1749:> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:6613:-> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:6615:+> Superseded by AP165: the bar complex of Volume I, equipped with its
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:6733:-> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:6735:+> Superseded by AP165: the bar complex of Volume I, equipped with its
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:7536:-> "The bar complex of Volume I, equipped with its coproduct, is a
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:7538:+> Superseded by AP165: the bar complex of Volume I, equipped with its
fix_wave_C_20260413_175943/C09_sc_bar_coalgebra_fix.md:8394:-> "The bar complex of Volume I, equipped with its coproduct, is a
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -U \"bar complex[\\s\\S]{0,80}Swiss-cheese\" /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:71:- "the bar complex presents the Swiss-cheese algebra"
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1078:$A_\infty$~chiral algebra, bar complex, Swiss-cheese operad,
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1109: chiral algebras. Volume~II reinterprets the bar complex as an
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1110: algebra over the Swiss-cheese operad
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2236:Thus: the bar complex is the universal coalgebraic stage on which the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2237:Swiss-cheese clutching correspondences act, as the Steinberg variety
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:27:$\cL_\cA \hookrightarrow \cM_{\mathrm{vac}}(\cA)$. The bar complex is the
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:28:endomorphism algebra of this point. The Swiss-cheese operad is the local
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1746:$\cL_\cA \hookrightarrow \cM_{\mathrm{vac}}(\cA)$. The bar complex is the
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1747:endomorphism algebra of this point. The Swiss-cheese operad is the local
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:157:they make the bar complex a coalgebra over the Swiss-cheese
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149:The bar complex presents the Swiss-cheese algebra, as the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:198:\begin{remark}[The Swiss-cheese operad and the three bar complexes]
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:199:\label{rem:sc-three-bar-complexes}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:200:\index{three bar complexes!Swiss-cheese decomposition}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:201:\index{Swiss-cheese operad!two colours and bar complexes}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:202:The two-coloured Swiss-cheese operad $\SCchtop$ acts on a boundary
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:1351:\index{three bar complexes!Swiss-cheese provenance}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:1352:\index{Swiss-cheese operad!three bar complexes}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:6:% Swiss-cheese inside the bar complex") with the dependency narrative
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4020,4055p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Volume~II lifts the bar complex to three dimensions. On the product
$\mathbb C_z \times \mathbb R_t$, the bar complex $\barB(\cA)$ is a
single-coloured $\Eone$-chiral dg coalgebra over
$(\mathrm{ChirAss})^!$: its differential extracts OPE residues from
collisions in the holomorphic plane, and its deconcatenation coproduct
is the cofree coassociative structure on the desuspended augmentation
ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$, not the bar
complex itself: the two-colour open/closed structure emerges when the
bar complex is fed into the Hochschild construction.

The primitive object of three-dimensional holomorphic-topological
quantum field theory on $\mathbb C_z \times \mathbb R_t$ is the
open/closed factorization dg-category~$\mathcal C$ on the bordified
curve~$\widetilde{X}_D$. Its objects are boundary conditions, its
morphisms are open-string states, and a choice of vacuum~$b$ yields a
boundary algebra $A_b = \operatorname{End}_{\mathcal C}(b)$, determined
only up to Morita equivalence. The bar complex of Volume~I is the
coalgebraic shadow of this category: its differential encodes OPE
residues (the chiral product), and its deconcatenation coproduct
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1085,1115p' /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
datum.

\tableofcontents

\section*{Notation and conventions}
\begin{itemize}[leftmargin=2em]
\item All algebraic structures are over $\C$ unless stated otherwise.
\item Grading is \emph{cohomological}: differentials have degree $+1$.
\item $\Ainf$ denotes the $A_\infty$ operad; $\Eone$, $\Etwo$, $\Einf$ the little-disks operads.
\item $\SCchtop$ is the holomorphic--topological Swiss-cheese operad (Definition~\ref{def:SC}).
\item $\FM(X)$ denotes the Fulton--MacPherson compactification of $\Conf(X)$.
\item $m_k$ are the $\Ainf$ chiral operations; $\lambda_i$ are spectral parameters.
\item Volume~I notation: $\cA$ for chiral algebras, $\barB(\cA)$ for bar, $\Omegach(C)$ for cobar, $\cA^!$ for Koszul dual; on the two-color Vol~II surface we write $\cA^!_{\mathrm{ch}}$ and $\cA^!_{\mathrm{line}}$ for the closed- and open-color duals.
\end{itemize}

\subsection*{What this volume assumes from Volume~I}

Volume~I proves five structural theorems for chiral algebras on
curves. This volume depends on all five.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2210,2265p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[The factorization setting]
\label{rem:steinberg-factorization}
The Steinberg--Hecke parallel extends to the
factorization framework of this chapter.  The factorizable
$D$-module $F_\cA$ on $\Ran(\Sigma_g)$ associates to each point
of $\Mbar_g$ a factorization algebra on the corresponding curve.
The clutching correspondence \eqref{eq:sep-clutching-span} acts on
$F_\cA$ by the factorization splitting: the restriction of $F_\cA$
to a separating node decomposes as $F_\cA|_{z_1} \otimes F_\cA|_{z_2}$
by the factorization isomorphism
(Construction~\ref{constr:fact-dmod-from-chiral}(iii)), and the
convolution product contracts this tensor product by the invariant
bilinear form on~$\cA$.  This is the factorization-level
realisation of the Lie bracket on $L_{\mathrm{mod}}$.

The non-separating clutching acts on $F_\cA$ by the non-separating
clutching map $\Delta_{\mathrm{cyc}}$
(Construction~\ref{constr:nonsep-clutching}): it contracts a pair
of tensor factors by $\langle{-},{-}\rangle_{\mathrm{inv}}$ and

thinking
**Listing residual affirmative B(A)-SC claims**

I’m gathering all remaining positive or materially misleading claims about B(A) presenting Swiss-cheese structures from key `.tex` and `.md` files only, excluding logs like resumes. For each, I’ll include the file and line number, a concise quoted snippet showcasing the claim, and a one-line classification explaining the misattribution or conflation, compiling about eight such entries into a bullet list. This will give the user a clear, referenced summary of leftover assertive statements in the codebase.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1085,1120p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1085	datum.
  1086	
  1087	\tableofcontents
  1088	
  1089	\section*{Notation and conventions}
  1090	\begin{itemize}[leftmargin=2em]
  1091	\item All algebraic structures are over $\C$ unless stated otherwise.
  1092	\item Grading is \emph{cohomological}: differentials have degree $+1$.
  1093	\item $\Ainf$ denotes the $A_\infty$ operad; $\Eone$, $\Etwo$, $\Einf$ the little-disks operads.
  1094	\item $\SCchtop$ is the holomorphic--topological Swiss-cheese operad (Definition~\ref{def:SC}).
  1095	\item $\FM(X)$ denotes the Fulton--MacPherson compactification of $\Conf(X)$.
  1096	\item $m_k$ are the $\Ainf$ chiral operations; $\lambda_i$ are spectral parameters.
  1097	\item Volume~I notation: $\cA$ for chiral algebras, $\barB(\cA)$ for bar, $\Omegach(C)$ for cobar, $\cA^!$ for Koszul dual; on the two-color Vol~II surface we write $\cA^!_{\mathrm{ch}}$ and $\cA^!_{\mathrm{line}}$ for the closed- and open-color duals.
  1098	\end{itemize}
  1099	
  1100	\subsection*{What this volume assumes from Volume~I}
  1101	
  1102	Volume~I proves five structural theorems for chiral algebras on
  1103	curves. This volume depends on all five.
  1104	
codex
Remaining affirmative conflations in the live surface:

- `standalone/programme_summary_sections5_8.tex:134`: “This table … classes 𝖦 and 𝖫 … have finite shadow depth and Swiss-cheese-formal bar complexes; …” — classification: SC-formality is attached directly to `B(A)` instead of to the derived-center pair.
- `standalone/programme_summary_sections5_8.tex:300`: table rows “Structure … Bar differential `d_{\barB}` … Open colour … Deconcatenation Δ …” plus the follow-up prose that makes the closed/open Swiss-cheese colours equal to the bar differential/coproduct — classification: presents `B(A)` as carriers of the two SC colours rather than the derived center.
- `standalone/programme_summary.tex:1432`: same dichotomy wording “classes 𝖦/𝖫 … have finite shadow depth and Swiss-cheese-formal bar complexes; …” — classification: again misattributes Swiss-cheese formality to the bar complex.
- `standalone/programme_summary.tex:1600`: “Structure … Bar differential `d_{\barB}` … Deconcatenation Δ …” and text describing the closed colour as the bar differential and the open colour as Δ — classification: keeps assigning the SC closed/open colours to `B(A)` operations.
- `standalone/programme_summary.tex:1812`: “Gauge theories (classes 𝖦, 𝖫): finite shadow depth, Swiss-cheese-formal bar complex (`m_k^{SC}=0` for large k), …” — classification: reasserts that `B(A)` itself is SC-formal for these families.
- `standalone/survey_track_b_compressed.tex:970`: “On ℂ×ℝ the holomorphic direction produces the closed-string bar differential … the topological direction produces the open-string coproduct … The bar complex of Volume I is the coalgebraic shadow of 𝒞: its differential encodes the closed colour, and its coproduct the open colour.” — classification: again equates the two SC colours directly with the bar complex.
- `standalone/survey_modular_koszul_duality_v2.tex:6113`: identical wording that “the bar complex of Volume I is the coalgebraic shadow of 𝒞: its differential encodes the closed colour, and its coproduct the open colour.” — classification: same B(A)‑SC conflation.
- `working_notes.tex:8022`: “The bar complex presents the Swiss-cheese algebra, as the Steinberg variety presents the Hecke algebra …” — classification: explicitly declares `B(A)` to be the Swiss-cheese presenting object instead of the derived-center output.
wait(call_6J5LJTKifRe8B1mIPEcjE1Gn) 1 agents complete:
  019d87fa-7f86-79e3-9153-ac3a76799974 completed: "Remaining affirmative conflations in the live surface:

- `standalone/programme_summary_sections5_8.tex:134`: “This tabl…"
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '2225,2255p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2225	
  2226	The non-separating clutching acts on $F_\cA$ by the non-separating
  2227	clutching map $\Delta_{\mathrm{cyc}}$
  2228	(Construction~\ref{constr:nonsep-clutching}): it contracts a pair
  2229	of tensor factors by $\langle{-},{-}\rangle_{\mathrm{inv}}$ and
  2230	raises genus by~$1$.  The bar complex $\barB(F_\cA)$, viewed as a
  2231	factorization coalgebra on $\Ran(\Sigma_g)$ parametrised by $\Mbar_g$,
  2232	is the \emph{universal} object on which both clutching correspondences
  2233	act: it is the simultaneous presentation of all convolution products
  2234	at all genera.
  2235	
  2236	Thus: the bar complex is the universal coalgebraic stage on which the
  2237	Swiss-cheese clutching correspondences act, as the Steinberg variety
  2238	is the geometric stage underlying the Hecke algebra.  Both arise from
  2239	convolution structures on self-intersection varieties of resolution
  2240	correspondences, differing only in the ambient geometry.
  2241	$\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
  2242	modular one.
  2243	\end{remark}
  2244	
collab wait(call_zKgFM1cVmvAvb2NgNjeoTSdp)
  receivers: 019d87fa-7f8a-7511-8db8-e23f75eff083
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,40p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ================================================================
% THE HEISENBERG ROSETTA STONE
% ================================================================
% This chapter lives in BOTH volumes.
% Volume I: chapters/theory/rosetta_stone.tex
% Volume II: chapters/examples/rosetta_stone.tex
%
% It proves, by explicit computation on H_k, that the bar complex
% is a Swiss-cheese algebra in the sense of Definition~\ref{def:SC}.
% The chapter uses only macros available in both volumes.
% ================================================================

% Fallback macros: ensure compilation in both volumes.
\providecommand{\barB}{\bar{B}}
\providecommand{\cA}{\mathcal{A}}
\providecommand{\cH}{\mathcal{H}}
\providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
\providecommand{\Ainf}{\mathsf{A}_{\infty}}
\providecommand{\Eone}{\mathsf{E}_1}
\providecommand{\Einf}{\mathsf{E}_{\infty}}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '1,15p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	% ================================================================
     2	% THE HEISENBERG ROSETTA STONE
     3	% ================================================================
     4	% This chapter lives in BOTH volumes.
     5	% Volume I: chapters/theory/rosetta_stone.tex
     6	% Volume II: chapters/examples/rosetta_stone.tex
     7	%
     8	% It proves, by explicit computation on H_k, that the bar complex
     9	% is a Swiss-cheese algebra in the sense of Definition~\ref{def:SC}.
    10	% The chapter uses only macros available in both volumes.
    11	% ================================================================
    12	
    13	% Fallback macros: ensure compilation in both volumes.
    14	\providecommand{\barB}{\bar{B}}
    15	\providecommand{\cA}{\mathcal{A}}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese" /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
9:% is a Swiss-cheese algebra in the sense of Definition~\ref{def:SC}.
56:\index{Swiss-cheese operad!Heisenberg example|textbf}
608:\index{Swiss-cheese operad!curved}
1002:(Volume~II), unified by the Swiss-cheese structure of a single
1011:Swiss-cheese structure becomes necessary.
1026:The Swiss-cheese convolution $L_\infty$-algebra
1034:$\C \times \R_{\ge 0}$, the Swiss-cheese convolution algebra
1186:The Swiss-cheese structure is SC-formal: the higher
3876:The pole structure determines the Swiss-cheese formality
3898: shadow depth is infinite, and the Swiss-cheese structure is
3911: formal Swiss-cheese structure at genus~$0$; class~$\mathbf{M}$
3912: has non-formal Swiss-cheese structure. At genus~$g \ge 1$, the
4009:concentrated by PBW). Class~$\mathbf{G}$ has formal Swiss-cheese structure
4018:shadow depth} and fully non-formal Swiss-cheese structure
4087:\emph{non-formal} Swiss-cheese structure: the higher
5918: contributes corrections from the higher Swiss-cheese
5921: has non-formal Swiss-cheese structure (the transferred
6174: the Swiss-cheese structure is formal at genus~$0$, and
6178: (from composite-field exchange), the Swiss-cheese
6267:non-formal Swiss-cheese structure.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,20p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ===================================================================
% DRAFT: The open primitive and the gravitational genus expansion
%
% This is a draft recast of Vol II foundations, written from the
% correct primitives. It replaces the discovery narrative ("we found
% Swiss-cheese inside the bar complex") with the dependency narrative
% ("the Swiss-cheese operad is primitive; the bar complex is a
% coalgebraic projection; the derived center is the universal bulk;
% modularity is trace plus clutching on the open sector; and the
% genus expansion of the MC element IS gravity").
% ===================================================================

\section{The open factorization category}
\label{sec:open-primitive}

\subsection{Statement of the problem}

A chiral algebra on a curve is a factorization algebra on the
Ran space, with the chiral product encoding collisions of
points. Volume~I constructed the bar complex~$\barB(\cA)$,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2050,2085p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
in three dimensions (the Swiss-cheese structure is the endomorphism
composition law) and explores its consequences: the Koszul triangle,
the spectral $R$-matrix, the genus tower, the PVA shadow, the
modular holography programme.

The modular programme asks: does the local geometry extend to a
global geometry? Is the point part of a family over $\Mbar_{g,n}$?
Are the transition functions Lagrangian correspondences? What are
the global intersection numbers?

These questions are not separate from the local theory. They are
its natural continuation: from a point in the derived symplectic
category, to a sheaf of points over the moduli of curves, to a
section of the universal Lagrangian correspondence over the
stable-graph boundary. The two volumes compute the first term of
this expansion. The modular programme is the rest.
\end{remark}

\bigskip
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '2060,2088p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2060	
  2061	These questions are not separate from the local theory. They are
  2062	its natural continuation: from a point in the derived symplectic
  2063	category, to a sheaf of points over the moduli of curves, to a
  2064	section of the universal Lagrangian correspondence over the
  2065	stable-graph boundary. The two volumes compute the first term of
  2066	this expansion. The modular programme is the rest.
  2067	\end{remark}
  2068	
  2069	\bigskip
  2070	
  2071	A chiral algebra is a point in the derived symplectic category.
  2072	The bar complex is the endomorphism algebra of this point.
  2073	The Swiss-cheese operad is the composition law. Koszul duality is
  2074	the symplectic complement. The genus tower is the deformation of
  2075	the point over the moduli of curves. The holographic principle is
  2076	the theorem that the point determines its ambient.
  2077	
  2078	Everything else is a shadow of the local geometry at a single point.
  2079	

thinking
**Compiling bar complex claim references**

I'm gathering and cross-referencing all explicit claims in the repo that describe the bar complex as related to the Swiss-cheese operad, carefully noting file paths, line numbers, and claim classifications to build a focused list of key statements while deciding which ones are directly relevant or potentially misleading.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex | sed -n '3345,3378p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3345	  quantify the equidistribution rate.
  3346	\end{enumerate}
  3347	These are precisely the axioms (AU1)--(AU4) of the analytic
  3348	unitary $\SCchtop$-algebra
  3349	(Definition~\ref{def:analytic-unitary-SC}).  The analytic
  3350	VOA programme does not attempt to make the bar complex see
  3351	the zeta zeros---it cannot, because the zeros are geometric,
  3352	not algebraic.  Instead, it provides the analytic
  3353	infrastructure to study how $Z(\tau)$, produced by the bar
  3354	complex, \emph{sits on the modular surface}---the
  3355	meeting point where algebra, geometry, and arithmetic
  3356	converge.
  3357	
  3358	\subsubsection{The Steinberg principle}
  3359	
  3360	The Steinberg variety presents the Hecke algebra.  The bar
  3361	complex presents the Swiss-cheese algebra.  Neither presents
  3362	the Riemann zeta function.  The zeta function is presented
  3363	by the \emph{modular surface itself}---its spectral theory,
  3364	its scattering matrix, its Selberg trace formula.  The
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,40p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{Conclusion and Outlook}
\label{sec:conclusion}%
\label{sec:concordance}%

\subsection{The single object}

Volume~I is genus~$g$ on a curve; Volume~II is the dimensional
lift to $\C \times \R$. The bar complex
$\barB^{\mathrm{ch}}(\cA)$ of Volume~I and the Swiss-cheese operad
$\SCchtop$ of Volume~II are two views of a single structure, not two theories.
The MC element $\alpha_T$ in the Swiss-cheese convolution algebra
encodes the direct data of this volume through its projections: the
$\Ainf$ operations as its closed face, the open-colour line-sector
operations as its open face, the PVA bracket as its cohomological
shadow, the spectral $R$-matrix as its mixed-color component, and the
genus tower as its $\hbar$-expansion. The corrected
bulk-boundary-line triangle is then assembled from these faces
together with the later comparison theorems. Each of the following
results is a coordinate expression for this single object.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '1,25p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\section{Conclusion and Outlook}
     2	\label{sec:conclusion}%
     3	\label{sec:concordance}%
     4	
     5	\subsection{The single object}
     6	
     7	Volume~I is genus~$g$ on a curve; Volume~II is the dimensional
     8	lift to $\C \times \R$. The bar complex
     9	$\barB^{\mathrm{ch}}(\cA)$ of Volume~I and the Swiss-cheese operad
    10	$\SCchtop$ of Volume~II are two views of a single structure, not two theories.
    11	The MC element $\alpha_T$ in the Swiss-cheese convolution algebra
    12	encodes the direct data of this volume through its projections: the
    13	$\Ainf$ operations as its closed face, the open-colour line-sector
    14	operations as its open face, the PVA bracket as its cohomological
    15	shadow, the spectral $R$-matrix as its mixed-color component, and the
    16	genus tower as its $\hbar$-expansion. The corrected
    17	bulk-boundary-line triangle is then assembled from these faces
    18	together with the later comparison theorems. Each of the following
    19	results is a coordinate expression for this single object.
    20	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '190,210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the boundary interval $I_0 \cong \R$ recovers the topological
direction~$\R_t$, and $\cC$ encodes the full two-colored
Swiss-cheese data of Definition~\ref{def:SC-algebra} promoted
to a category. The local constancy axiom~(iv) is the
categorical avatar of the locally-constant factorization
structure on~$\R$ that produces the $E_1$ (associative) color.
\end{remark}

\begin{remark}[The Swiss-cheese operad and the three bar complexes]
\label{rem:sc-three-bar-complexes}
\index{three bar complexes!Swiss-cheese decomposition}
\index{Swiss-cheese operad!two colours and bar complexes}
The two-coloured Swiss-cheese operad $\SCchtop$ acts on a boundary
algebra $\cA$ through two distinct channels, each of which produces
its own bar complex. The \emph{closed colour} (holomorphic,
$\FM_k(\C)$) assembles collision residues into the symmetric bar
complex $\barB^{\Sigma}(\cA)$, the factorization coalgebra of
Volume~I, Theorem~A. The \emph{open colour} (topological,
$E_1(m) \simeq \Conf^<_m(\R)$) assembles ordered tensor factors
into the ordered bar complex $\barB^{\mathrm{ord}}(\cA)$, the

thinking
**Summarizing Swiss-cheese and bar complex claims**

I’m gathering a clear list of all the places the texts claim or conflate the bar complex B(A) with the Swiss-cheese operad, focusing on positive assertions. I’m preparing a summary that includes file names, line numbers, quoted snippets, and classifies each claim—distinguishing canonical statements from working notes or less formal remarks—to give the user a thorough but clear overview.
codex
Found the following remaining affirmative statements in Vol II that equate the ordered bar complex with an SC/Swiss-cheese object (all are still present in the live files):

- `main.tex:1108-1111` – “Volume II reinterprets the bar complex as an algebra over the Swiss-cheese operad SC^{ch,top}; the adjunction is assumed, not reproved.” – classification: explicit introduction-level conflation that makes B(A) itself the SC algebra.

- `chapters/connections/conclusion.tex:7-10` – “The bar complex \barB^{ch}(A) of Volume I and the Swiss-cheese operad SC^{ch,top} of Volume II are two views of a single structure, not two theories.” – classification: grand concluding claim that B(A) and the SC operad are identical rather than the derived center being the SC output.

- `chapters/connections/conclusion.tex:2071-2074` – “A chiral algebra is a point… The bar complex is the endomorphism algebra of this point. The Swiss-cheese operad is the composition law. Koszul duality is the symplectic complement.” – classification: local geometric summary that again makes the bar complex the Swiss-cheese datum.

- `chapters/theory/factorization_swiss_cheese.tex:2230-2239` – “The bar complex \barB(F_A)… is the universal coalgebraic stage on which the Swiss-cheese clutching correspondences act…” – classification: factorization remark that treats B(A) as carrying the Swiss-cheese action.

- `chapters/connections/log_ht_monodromy_core.tex:2047-2052` – “The bar complex of V^k(sl_2), viewed as a logarithmic SC^{ch,top}-algebra, produces a flat connection…” – classification: proof step that directly identifies the bar complex with an SC algebra.

- `chapters/examples/rosetta_stone.tex:8-10` – “It proves… that the bar complex is a Swiss-cheese algebra in the sense of Definition \ref{def:SC}.” – classification: chapter header committing to the forbidden identification.

- `working_notes.tex:152-165` – “Together they make the bar complex a coalgebra over the Swiss-cheese cooperad…” – classification: working notes still present the wrong SC-on-bar story in the abstract.

- `working_notes.tex:1149-1162` – “The bar complex presents the Swiss-cheese algebra, as the Steinberg variety presents the Hecke algebra… The bar complex… is the Swiss-cheese algebra on FM_k(C) × Conf_k(R)…” – classification: detailed working-note narrative repeating the conflation.

- `working_notes.tex:3358-3373` – “The Steinberg variety presents the Hecke algebra. The bar complex presents the Swiss-cheese algebra…” – classification: later working-note analogy that again ties B(A) directly to SC structure.

These are the only remaining affirmative claim sites matching your search (I skipped the explicit “NOT”/forbidden notes). Let me know if you’d like help patching any of them.
wait(call_zKgFM1cVmvAvb2NgNjeoTSdp) 1 agents complete:
  019d87fa-7f8a-7511-8db8-e23f75eff083 completed: "Found the following remaining affirmative statements in Vol II that equate the ordered bar complex with an SC/Swiss-chee…"


thinking
**Inspecting repo patterns**

I need to check for more hits in the Volume I main repository beyond what's just in standalone and working notes; the explorer only found those. I also suspect that compute/tests may contain a correct docstring. The user asked me to search all volumes for patterns and fix each one. It’s possible that I can include standalone documents under the repo, which might need patching. I’ll also verify if there are any other local hits by running rg targeted around false claim patterns from the explorer. There were 8 hits in Volume I that I need to inspect further.
thinking
**Patching compute tests**

I could potentially patch one or two compute tests in Volume I. The search results include a line in `compute/tests/test_theorem_swiss_cheese_kontsevich_engine.py`, though it might be misleading. The explorer didn't flag it, but the user asked me to find and fix issues in one pass, so I need to be thorough. I also want to inspect any compute docstrings in the current repo that may affirm any false claims. A targeted search will help with that.
codex
The explorer sweep isolated eight real Vol I claims rather than generic SC discussion. I’m opening those exact contexts now so the edits stay minimal and local instead of rewriting wider exposition.
exec
/bin/zsh -lc "sed -n '110,170p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The maximal pole order of the collision residue separates the
standard landscape into two regimes:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{clcl}
\toprule
\textbf{Pole order} & \textbf{Algebra}
 & \textbf{Collision} & \textbf{Class} \\
\midrule
$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
$1$ & Kac--Moody $\widehat{\fg}_k$ & $\Omega/((k{+}h^\vee)z)$ & $\mathbf{L}$ \\
$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
$2N{-}1$ & $\mathcal{W}_N$ & poles through $z^{-(2N-1)}$
 & $\mathbf{M}$ \\
\bottomrule
\end{tabular}
\end{center}

exec
/bin/zsh -lc "sed -n '1410,1455p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '280,340p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '950,995p' standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1580,1635p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8005,8040p' working_notes.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1790,1835p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6090,6140p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standard landscape into two regimes:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{clcl}
\toprule
\textbf{Pole order} & \textbf{Algebra}
 & \textbf{Collision} & \textbf{Class} \\
\midrule
$1$ & Heisenberg $\cH_k$ & $k/z$ & $\mathbf{G}$ \\
$1$ & Kac--Moody $\widehat{\fg}_k$ & $k\,\Omega/z$ & $\mathbf{L}$ \\
$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
$2N{-}1$ & $\cW_N$ & poles through $z^{-(2N-1)}$
 & $\mathbf{M}$ \\
\bottomrule
\end{tabular}
\end{center}

\noindent
This table encodes a structural dichotomy: algebras whose
 succeeded in 51ms:
the Gaussian base. The nontrivial zeros of the component
$L$-functions are the scattering resonances of the hyperbolic
Laplacian on $\cM_{1,1}$: frequencies at which the genus-$1$
sewing amplitude fails to decay.

\medskip\noindent\textbf{Genus-$2$ B\"ocherer bridge.}
For the Leech lattice VOA, the Siegel modular form
$\chi_{12} = \mathrm{SK}(f_{22})$ is the Saito--Kurokawa lift
of the unique weight-$22$ cuspidal eigenform, and the
MC-derived second Fourier coefficient $c_2 \approx
-1.918 \times 10^{-6} \neq 0$ is the first nonzero central
$L$-value produced by the shadow obstruction tower,
connecting $\Theta_\cA$ to genus-$2$ Siegel modular forms via
the Furusawa--Morimoto theorem.


% ====================================================================
\section*{10.\quad The open/closed world (Volume II)}
% ====================================================================

 succeeded in 51ms:
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

% ====================================================================
\subsection{The two colours}
\label{ssec:two-colours}
% ====================================================================

The bar complex lives on $\FM_k(\Bbbk) \times \Conf_k(\mathbb{R})$,
the product of holomorphic and topological configuration spaces.
This product is the operadic fingerprint of the Swiss-cheese
operad:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
& \textbf{Closed colour} & \textbf{Open colour} \\
\midrule
\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
 succeeded in 50ms:
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

% ====================================================================
\subsection{The two colours}
\label{ssec:two-colours}
% ====================================================================

The bar complex lives on $\FM_k(\Bbbk) \times \Conf_k(\mathbb{R})$,
the product of holomorphic and topological configuration spaces.
This product is the operadic fingerprint of the Swiss-cheese
operad:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
& \textbf{Closed colour} & \textbf{Open colour} \\
\midrule
\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
 succeeded in 50ms:
G(t;\lambda)
  = \mathrm{Tr}_{\fh}\!\left(\frac{1}{1 - t\,K(\lambda)}\right),
\]
where $K(\lambda)$ is the collision kernel at conformal
weight~$\lambda$.  At the symmetric point $\lambda = (c-1)/24$
(where $\Delta = \bar\Delta$), a universal factor $(x+2)$ appears
in $P_k$ for all $k \leq 5$---this is the conformal weight Ward
identity forcing a zero at $x = -2$.  Whether the factor persists
at all arities is tied to the question of whether the Shapovalov
determinant has a universal factorisation beyond the
Kac determinant formula.

\subsection{AP-OC Steinberg refinement}
\label{subsec:ap-oc-steinberg}

The three-functor picture from
Observation~\ref{obs:three-functors} acquires a slogan:
\emph{the bar complex presents the Swiss-cheese algebra, as the
Steinberg variety presents the Hecke algebra.}  More precisely,
$\barB(\cA)$ is the presenting coalgebra from which bulk,
 succeeded in 51ms:
\end{tabular}
\end{center}

\noindent
At each level, information is lost. From 4d to 3d, one
topological direction is forgotten: $E_2 \to E_1$ (the
braiding becomes ordering). From 3d to 2d,
$\Sigma_n$-coinvariance projects the $R$-matrix to a scalar:
$r(z) \mapsto \kappa$. The five main theorems are the
invariants that survive both projections.

% ====================================================================
\subsection{Gauge versus gravity}
\label{ssec:gauge-vs-gravity}
% ====================================================================

The shadow depth classification
(Definition~\ref{def:shadow-depth}) separates the standard
landscape into two physical regimes:

 succeeded in 50ms:
restriction. Specialisation to simple quotients $L_k(\fg)$
requires additional analysis that depends on the level denominator
and the rank of $\fg$.

% ====================================================================
% TRACK B: sections 10--13 (open/closed, PVA quantization, holography,
% completion and frontier)
% ====================================================================

\section*{10.\quad The open/closed world (Volume II)}
% ====================================================================

Sections~1--9 construct $E_n$-chiral algebras as
algebraic-geometric objects on curves: bar complexes on every
curve geometry, $R$-matrices, Yangian structures, derived chiral
centres carrying $E_2$/$E_3$ structure, and the
$\SCchtop$ datum on the pair
$(\cZ^{\der}_{\ch}(\cA),\, \cA)$. Volume~II discovers that
these constructions are physics: the derived chiral centre IS the
bulk algebra of a real 3d holomorphic-topological gauge theory.

thinking
**Examining context for edits**

I think I need more context beyond just the snippet to make effective edits. It might be helpful to look at the lines following 8022 for extra clarity. I'll check the preceding sentence around line 280 regarding "pair not on B(A) itself." I want to keep my edits minimal, so I’ll also consider searching for more elements in the current repository that might not be flagged, like comments in `test_theorem_swiss_cheese_kontsevich_engine`. It’s possible there are false claims in docstrings too, so running a targeted grep for suspicious phrases could be beneficial.
exec
/bin/zsh -lc "rg -n -i -e 'Swiss-cheese-formal bar|bar complex presents the Swiss-cheese|bar complex.*Swiss-cheese algebra|differential encodes the closed colour|coproduct the open colour|bar complex.*SC\\"'^'"\\{ch,top\\}|coalgebra over the Swiss-cheese|bar complex.*closed colour|bar complex.*open colour|closed-string bar differential|open-string coproduct|m_k\\"'^'"\\{SC\\}' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1558

/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H03_thm_C_alt_proof.md:138:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H03_thm_C_alt_proof.md:144:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R13_introduction.md:100:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R13_introduction.md:106:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H02_thm_B_alt_proof.md:126:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H02_thm_B_alt_proof.md:132:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R19_coderived_models.md:169:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R19_coderived_models.md:175:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H17_remove_perfectness_C1.md:186:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H17_remove_perfectness_C1.md:192:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/scripts/healing_fortification_40.py:319:2. The SC operations m_k^{SC} at order k >= 3 are controlled by S_{k-1} in the shadow tower.
/Users/raeez/chiral-bar-cobar/scripts/healing_fortification_40.py:320:3. S_r = 0 for r >= 3 (class G) implies m_k^{SC} = 0 for k >= 3. QED.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H10_depth_gap_alt.md:126:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H10_depth_gap_alt.md:132:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H18_remove_class_M_MC5.md:109:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H18_remove_class_M_MC5.md:115:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H18_remove_class_M_MC5.md:702:  2048	compared is not ``the bar complex as a Swiss-cheese algebra'': the
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H15_remove_chain_level_topol.md:449:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
exec
/bin/zsh -lc "rg -n -i --glob '"'!healing_*'"' --glob '"'!rectification_*'"' --glob '"'!audit_campaign_*'"' --glob '"'!fix_wave_*'"' --glob '"'!superseded/**'"' --glob '"'!archive/**'"' -e 'bar complex.*Swiss-cheese|Swiss-cheese.*bar complex|closed colour.*bar differential|open colour.*deconcatenation|presents the Swiss-cheese|coalgebra over.*Swiss|SC-?coalgebra|full Swiss-cheese algebra|bar differential is the closed color|bar coproduct is the open color|differential encodes the closed colour|coproduct the open colour' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 509

/Users/raeez/chiral-bar-cobar/CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
/Users/raeez/chiral-bar-cobar/CLAUDE.md:376:- B55. "The bar differential is the closed color" / "the bar coproduct is the open color." FALSE. d_B and Delta make B(A) an E_1 dg coalgebra, NOT an SC two-color datum. AP165.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:473:(3) WRONG: "Together, d_B and Delta make B(A) an SC-coalgebra." TRUTH: A dg coassociative coalgebra (differential + coproduct) is a SINGLE-colored E_1 dg coalgebra. Having two structures does not make it two-colored. SC is two-colored (bulk + boundary); B(A) is one object, not a pair.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:920:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
/Users/raeez/chiral-bar-cobar/AGENTS.md:53:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11.
/Users/raeez/chiral-bar-cobar/AGENTS.md:140:**SC^{ch,top} is NOT on B(A) (AP165).** B(A) is E_1 coassociative coalgebra. SC^{ch,top} lives on the pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."
/Users/raeez/chiral-bar-cobar/AGENTS.md:537:**Categorical confusion**: FM4 (k=0 vs k=-h^v), FM11 (Sugawara shift missing: av(r)+dim(g)/2=kappa for non-abelian), FM23 (local-global on curves: point≠D≠A^1≠P^1), FM24 (B-cycle i^2: q becomes real), FM25 (SC disaster: B(A) is NOT SC-coalgebra — entire false framework), FM26 (false SC self-duality: dim check fails), FM27 (scope inflation in metadata), FM28 (topologization scope: proved KM only), FM32 (pi_3(BU)=pi_2(U)=0, not Z), FM33 (formula outside hypothesis domain), FM34 (excision/coproduct: ⊗_A vs plain ⊗)
/Users/raeez/chiral-bar-cobar/resume_20260413_165929/R01_chiral_koszul_pairs.md:127:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/relaunch_wave2_empties/S19_compute_to_manuscript.md:148:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R13_introduction.md:111:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/AP23_pi3_BU.md:164:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/AP23_pi3_BU.md:435:/Users/raeez/chiral-bar-cobar/AGENTS.md:537:**Categorical confusion**: FM4 (k=0 vs k=-h^v), FM11 (Sugawara shift missing: av(r)+dim(g)/2=kappa for non-abelian), FM23 (local-global on curves: point≠D≠A^1≠P^1), FM24 (B-cycle i^2: q becomes real), FM25 (SC disaster: B(A) is NOT SC-coalgebra — entire false framework), FM26 (false SC self-duality: dim check fails), FM27 (scope inflation in metadata), FM28 (topologization scope: proved KM only), FM32 (pi_3(BU)=pi_2(U)=0, not Z), FM33 (formula outside hypothesis domain), FM34 (excision/coproduct: ⊗_A vs plain ⊗)
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:2155:  thm_bar_swiss_cheese [label="thm:bar-swiss-cheese\ntheorem [Pr]\nBar complex as $\Eone$-chiral coassociat...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R19_coderived_models.md:110:(3) WRONG: "Together, d_B and Delta make B(A) an SC-coalgebra." TRUTH: A dg coassociative coalgebra (differential + coproduct) is a SINGLE-colored E_1 dg coalgebra. Having two structures does not make it two-colored. SC is two-colored (bulk + boundary); B(A) is one object, not a pair.
/Users/raeez/chiral-bar-cobar/relaunch_wave2_empties/D06_desuspension_direction.md:155:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:669:| `thm:bar-swiss-cheese` | `theorem` | 1295 | Bar complex as $\Eone$-chiral coassociative coalgebra |
/Users/raeez/chiral-bar-cobar/resume_20260413_163457/S14_standalone_to_main.md:3:- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”


thinking
**Identifying false claims in current files**

It seems like I need to check for current repo files that might have false claims, particularly some specific .tex and .py files. I need to determine whether these files genuinely have B(A) SC claims or if they're just okay. The search results are still noisy, and I should be exhaustive in my search across all volumes. It might help to use manual classification and refine the search string for exact patterns to filter out the noise better. Let’s stay focused on finding actual relevant claims!
thinking
**Inspecting for false claims**

The user wants me to search for exact patterns and descriptions to fix any remaining claims related to B(A) and SC coalgebra, including anything about Swiss-cheese. I need to be thorough rather than focusing on just exact terms. There might be false claims, so I should review lines in the appendices as well as the theorem and test files for corrections. Also, I should check other files for possible inaccuracies regarding Swiss-cheese terminology. To streamline my search, I’ll narrow down by excluding terms related to archive or resumes.
codex
I found one live appendix hit and several live compute/test docstrings that the first sweep missed because they say “Swiss-cheese algebra” rather than `SC`. I’m checking those now so the local repo doesn’t keep advertising the same false object through helper engines or tests.
exec
/bin/zsh -lc "sed -n '1728,1755p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '320,360p' compute/lib/swiss_cheese_chain_model.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The product $\FM_k(\mathbb C)\times\mathrm{Conf}_k^{<}(\mathbb R)$
is the geometric fingerprint of a 3d holomorphic-topological
field theory on $\mathbb C_z\times\mathbb R_t$:
observables factorise holomorphically in~$z$ and
associatively in~$t$. The bar differential is the
closed (holomorphic) colour. The bar coproduct is the
open (topological) colour.
\end{remark}

\begin{remark}[Codimension-one generators for
\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
The construction above gives the operation space, not yet a minimal
generators-and-relations presentation, and by itself it does not
equip the ordered bar complex with a full Swiss-cheese algebra
structure. On compactified models the codimension-$1$ generator
families are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
 $|S|\ge 2$;
\item open interval-splitting faces in a Stasheff compactification
 succeeded in 51ms:
r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.

CORE CLAIMS VERIFIED:
1. Bar differential = C-direction (holomorphic) factorization
2. Bar coproduct = R-direction (topological) factorization
3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
4. d_fib^2 = kappa * omega_g at genus g >= 1
5. Arnold relation ensures d^2 = 0 at genus 0
6. Arnold DEFECT at genus g produces curvature kappa * omega_g
7. PVA descent: H*(A, Q) is (-1)-shifted PVA
8. AP44 convention: lambda-bracket coeff = a_{(n)}b / n!
9. AP19: bar kernel d log absorbs one pole order
10. Three models: flat (d^2=0), corrected holomorphic (D_g^2=0), curved (d_fib^2 = kappa*omega_g)
11. CDG bulk algebra = commutative with shifted Poisson bracket
12. Swiss-cheese directionality: no open-to-closed maps
13. Moriwaki absolute convergence compatible with our sewing
14. Koszul duality decomposes along C x R: chiral KD x E_1 KD

CROSS-VOLUME CHECKS (AP49):
- Vol I OPE modes vs Vol II lambda-brackets (AP44 conversion)
 succeeded in 51ms:
r"""Tests for Vol II Part I rectification engine.

50+ tests verifying the core claims of Vol II Part I:
bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).

Test structure follows the multi-path verification mandate:
every claim verified by at least 2 independent paths.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_vol2_swiss_cheese_rectification_engine import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine,
    kappa_wn,
    arnold_relation_genus0,
    curvature_from_arnold_defect,
    verify_heisenberg_curvature_genus1,
 succeeded in 51ms:
#  Swiss-cheese pair dimensions: (Z^der, A) = (bulk, boundary)
# ======================================================================

def swiss_cheese_pair_dimensions(family: str,
                                 weight_bound: int,
                                 **kwargs) -> Dict[str, object]:
    """Compute dimensions of (Z^der, A) = (bulk, boundary) at each weight.

    The Swiss-cheese pair consists of:
      - Bulk (closed sector): the derived center Z^der_ch(A)
        By Theorem H, concentrated in degrees {0, 1, 2}.
      - Boundary (open sector): the algebra A itself, graded by
        conformal weight.

    At each weight level w <= weight_bound, we compute:
      - bulk_dim[n]: dim Z^n for n in {0, 1, 2} (from Theorem H)
      - boundary_dim[w]: number of states in A at weight w
        (counting derivatives of generators up to weight w)

    The swiss-cheese identification says the bar complex differential
exec
/bin/zsh -lc "sed -n '810,840p' compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '600,660p' compute/lib/factorization_coproduct_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_heisenberg_bridge.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1100,1125p' compute/lib/higher_dim_chiral_comparison_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    Chern-Simons theory for semisimple Lie algebras.  The key theorem:
      factorization homology trace = Reshetikhin-Turaev link invariant.

    Connection to our framework:
      - The E_3-algebra structures the 3d TFT.
      - Restricting from E_3 to E_1 (via the forgetful functor
        E_3 -> E_2 -> E_1) gives the associative structure on the
        boundary chiral algebra.
      - The boundary chiral algebra is V_k(g), the affine KM envelope.
      - Our bar complex B(V_k(g)) computes the Koszul dual, which by
        Theorem A is the Verdier dual factorization coalgebra.
      - The modular operad algebra structure on {B^{(g,n)}(A)} organizes
        the higher-genus data that CFG's E_3 algebra encodes via
        factorization homology on 3-manifolds.

    The precise bridge: CFG's E_3 acts on the boundary via the
    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
    E_1-algebra data (the C-direction factorization) while the coproduct
    extracts the E_1-coalgebra data (the R-direction factorization).
    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
 succeeded in 52ms:
    For P = Ass (associative/E_1):
      P^{!,c} = Ass^c (associative cooperad)
      B_Ass(A) has the COFREE COASSOCIATIVE coalgebra structure
      Ass^c(n) = k (one-dimensional, no symmetry)
      Coproduct: deconcatenation (non-cocommutative)

    A chiral algebra A on a curve X is an E_infinity-CHIRAL algebra
    (meaning: the factorization structure is defined on UNORDERED
    configurations).  Its bar complex uses P = Com in the chiral
    direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.

    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
    The bar complex in the R-direction uses P = Ass, giving the
    associative cooperad and DECONCATENATION coproduct.

    The full Swiss-cheese bar complex uses BOTH simultaneously:
      - Lie^c in the C-direction (bar differential, cocommutative)
      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
    """
    # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
 succeeded in 50ms:
"""The Heisenberg bridge: Vol I bar complex → Vol II Swiss-cheese structure.

As the Steinberg variety presents the Hecke algebra, the Heisenberg bar
complex presents the categorical logarithm.  This test file demonstrates
the FULL inter-volume pipeline on the simplest atom:

  Vol I (The Algebraic Engine):
    1. Bar differential d from OPE residues on FM(C)
    2. Arnold nilpotence d^2 = 0 at genus 0
    3. Curvature d_fib^2 = kappa * omega_g at genus >= 1
    4. Bar cohomology = Koszul dual Hilbert series
    5. Complementarity: kappa + kappa' = 0

  Vol II (Swiss-Cheese and 3D HT):
    6. Coproduct Delta from ordered deconcatenation (R-factorization)
    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
    8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
    9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
   10. Spectral R-matrix: trivial (E_infty => no braiding)

 succeeded in 50ms:
                '6d HCS on twistor PT -> 4d SDYM on R^4 (E_2, holomorphic-topological) '
                '-> 2d celestial chiral algebra on P^1 (E_1). '
                'The celestial OPE = holomorphic collinear limit of 4d amplitudes = our '
                'chiral algebra OPE. For SDYM with gauge group G: the celestial algebra is '
                'affine G at tree level, W_{1+inf} type at all loops. This is a standard '
                'chiral algebra in our framework (Costello-Paquette 2022, Fernandez-Paquette 2024).'
            ),
        },
        'Q5_en_structure': {
            'answer': 'E_1 (chiral) in 2d; E_2 (braided) in 4d CS; E_3 in 6d HCS',
            'detail': (
                'Our algebras are E_1 (associative/chiral on curves). Costello 4d CS gives '
                'E_2 = E_1 x E_1 (Dunn) where one E_1 is chiral (C-direction) and one is '
                'topological (Sigma-direction). The E_2 braiding IS the R-matrix, which our '
                'bar complex also captures via Res^{coll}_{0,2}(Theta_A). The Swiss-cheese '
                'construction (Vol II) is the precise mechanism: SC^{ch,top} realizes the '
                'E_2 structure inside the chiral framework. So: E_2 braiding is ALREADY '
                'encoded in our E_1 bar complex via the Swiss-cheese decomposition.'
            ),
        },

thinking
**Considering file exploration**

I need to focus on the current repository and ensure we're excluding audit directories but including compute files. It seems like I’ll ask the explorer to identify live current-repo files that involve the B(A)/bar complex SC conflation, but I should exclude archives, resumes, and healing. By using seed patterns alongside what I call "Swiss-cheese algebra," hopefully, I can prevent missing out on important files. It sounds like a solid plan!
codex
The appendix and compute layer do still contain live affirmative wording, not just manuscript standalones. I’m doing one focused live-surface sweep now across `chapters/`, `appendices/`, `standalone/`, `compute/`, `README`, and `working_notes.tex` so I don’t leave stale helper engines behind.
collab spawn_agent(call_4j5C28UHKuSDkKnAznVam4DN, prompt="Within /Users/raeez/chiral-bar-cobar only, search the LIVE surfaces (chapters/, appendices/, standalone/, compute/, READ…")
mcp startup: no servers
spawn_agent(call_4j5C28UHKuSDkKnAznVam4DN, prompt="Within /Users/raeez/chiral-bar-cobar only, search the LIVE surfaces (chapters/, appendices/, standalone/, compute/, READ…") pending init:
  agent: 019d87ff-1291-78c3-8043-4f849d9122df
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese" chapters appendices standalone compute metadata README* main.tex working_notes.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 871

README.md:13:| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
working_notes.tex:1680:This is the \textbf{Swiss-cheese algebra} on
working_notes.tex:6403:\item \textbf{The Swiss-cheese centre}
working_notes.tex:6430:the Swiss-cheese centre, and the extra direction is topological.
working_notes.tex:6640:    is Swiss-cheese \\
working_notes.tex:6643:  & $\Longrightarrow\;$ Swiss-cheese extends to modular
working_notes.tex:6644:    Swiss-cheese
working_notes.tex:7632:  $\Etwo$ structure at genus~$0$.  The Swiss-cheese theorem
working_notes.tex:7880:mediated by the Swiss-cheese structure.
working_notes.tex:7946:At genus~$0$, the Swiss-cheese operad $\SCchtop$ enforces
working_notes.tex:8022:\emph{the bar complex presents the Swiss-cheese algebra, as the
working_notes.tex:8038:$\barB(\cA)$ presents the Swiss-cheese algebra via
working_notes.tex:8706:relationship between the chiral bar complex and the Swiss-cheese
metadata/dependency_graph.dot:1846:  prop_swiss_cheese_nonformality_by_class [label="prop:swiss-cheese-nonformality-by-class\nproposition [Pr]\nSwiss-cheese non-formality by shadow cla...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2525:  prop_sc_formality_by_class [label="prop:sc-formality-by-class\nproposition [Pr]\nSwiss-cheese formality classification by...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:419:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2782 | Swiss-cheese non-formality by shadow class |
metadata/theorem_registry.md:1008:| `prop:sc-formality-by-class` | `proposition` | 17173 | Swiss-cheese formality classification by shadow class |
metadata/theorem_registry.md:2624:| `thm:thqg-swiss-cheese` | `theorem` | 382 | Universal open/closed pair (chiral Swiss-cheese theorem) |

thinking
**Investigating file structure**

While I’m waiting, I think it might be a good idea to check the `main.tex` or the README file. I’m not sure if the search results are yielding anything relevant in the current repo. I may need to look into `chapters/theory` as well. It feels like I should explore other files like `chapters/theory/introduction.tex`, but I'm considering searching all chapters and appendices more effectively. Using a tool like `rg` could help me do that quickly.
exec
/bin/zsh -lc "rg -n -i -e 'Swiss-cheese algebra|SC-coalgebra|closed colour|open colour|presents the Swiss-cheese|Swiss-cheese-formal bar|full Swiss-cheese algebra' chapters appendices standalone compute README.md main.tex working_notes.tex metadata 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -e 'bar complex.*SC|B\\(A\\).*SC|coalgebra.*SC' chapters appendices standalone compute README.md main.tex working_notes.tex metadata 2>/dev/null" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
working_notes.tex:1680:This is the \textbf{Swiss-cheese algebra} on
working_notes.tex:8022:\emph{the bar complex presents the Swiss-cheese algebra, as the
working_notes.tex:8038:$\barB(\cA)$ presents the Swiss-cheese algebra via
appendices/ordered_associative_chiral_kd.tex:1741:equip the ordered bar complex with a full Swiss-cheese algebra
appendices/ordered_associative_chiral_kd.tex:2029: holomorphic direction (closed colour) and ordered
appendices/ordered_associative_chiral_kd.tex:2030: configurations in the topological direction (open colour).
appendices/ordered_associative_chiral_kd.tex:3508:The full duality operates on both colours: the \emph{closed colour}
appendices/ordered_associative_chiral_kd.tex:3511:the double pole; the \emph{open colour} (ordered bar
appendices/ordered_associative_chiral_kd.tex:3528:\index{central extension!invisible to open colour}
appendices/ordered_associative_chiral_kd.tex:3556:information. The open colour sees the Yangian; the closed colour sees
appendices/ordered_associative_chiral_kd.tex:7502:differential decouples from the curved closed colour. When
appendices/ordered_associative_chiral_kd.tex:8033:holomorphic colour of the Swiss-cheese algebra, and
standalone/three_dimensional_quantum_gravity.tex:680:(closed colour) acts on the boundary (open colour). This is the
standalone/holographic_datum.tex:307:\begin{warning}[Bar complex is not an SC-coalgebra]
standalone/en_chiral_operadic_circle.tex:941:$\cO$-algebra pairs $(B, A)$ with fixed open colour~$A$:
standalone/en_chiral_operadic_circle.tex:1080: \emph{closed colour} (bulk), carrying $\Etwo$ from
standalone/en_chiral_operadic_circle.tex:1082:\item The chiral algebra $\cA$ is the \emph{open colour}
standalone/en_chiral_operadic_circle.tex:1105:(Example~\ref{ex:e-heis-chirhoch}) and open colour
standalone/en_chiral_operadic_circle.tex:1149: No mixed operations with closed output: the closed colour
standalone/en_chiral_operadic_circle.tex:1150: receives no information from the open colour.
 succeeded in 51ms:
Total output lines: 265

main.tex:1290:% chiral de Rham complex, bar coalgebra, screening operators, Toda systems.
README.md:6:The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.
metadata/dependency_graph.dot:2877:  thm_wakimoto_ordered_bar [label="thm:wakimoto-ordered-bar\ntheorem [Pr]\nWakimoto bar complex descent", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3141:  thm_wakimoto_ordered_bar [label="thm:wakimoto-ordered-bar\ntheorem [Pr]\nWakimoto bar complex descent", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:1285:| `thm:annular-HH` | `theorem` | 4893 | Annular bar complex computes chiral Hochschild homology |
metadata/theorem_registry.md:1298:| `thm:wakimoto-ordered-bar` | `theorem` | 6710 | Wakimoto bar complex descent |
metadata/theorem_registry.md:2831:| `thm:wakimoto-ordered-bar` | `theorem` | 2472 | Wakimoto bar complex descent |
metadata/theorem_registry.md:2882:| `thm:annular-HH` | `theorem` | 7268 | Annular bar complex computes chiral Hochschild homology |
chapters/examples/deformation_quantization.tex:525:\[W_3^{-22/5} \text{ bar complex} = \text{Free theory} \oplus \text{Screening operators}\]
chapters/examples/w_algebras_deep.tex:21:bar coalgebra structure, screening operators, and Toda field theory.
metadata/claims.jsonl:527:{"label": "thm:bgg-sl2-bar-explicit", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/bar_complex_tables.tex", "line": 2119, "title": "BGG resolution of \\texorpdfstring{$L(\\Lambda_0)$}{L(Lambda_0)} via bar complex", "labels_in_block": ["thm:bgg-sl2-bar-explicit", "eq:bgg-E1", "eq:screening-sl2"], "refs_in_block": ["thm:bgg-from-bar", "comp:bgg-differential"]}
metadata/claims.jsonl:1402:{"label": "thm:rosetta-sl2-swiss", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/frame/heisenberg_frame.tex", "line": 2751, "title": "$\\mathfrak{sl}_2$ bar complex as $E_1$-chiral\ncoassociative coalgebra", "refs_in_block": ["def:SC"]}
metadata/claims.jsonl:2044:{"label": "prop:sn-irrep-decomposition-bar", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/e1_modular_koszul.tex", "line": 2318, "title": "$\\Sigma_n$-irreducible decomposition of the ordered bar complex", "labels_in_block": ["prop:sn-irrep-decomposition-bar", "eq:schur-weyl-bar", "eq:frobenius-char-bar", "eq:information-ratio-bar"]}
metadata/claims.jsonl:2069:{"label": "thm:bar-swiss-cheese", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 1295, "title": "Bar complex as $\\Eone$-chiral coassociative coalgebra", "labels_in_block": ["thm:bar-swiss-cheese", "thm:bar-e1-coalgebra"], "refs_in_block": ["eq:bar-product-space", "princ:sc-two-incarnations", "thm:operadic-center-hochschild"]}
metadata/claims.jsonl:2749:{"label": "thm:annular-HH", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 4893, "title": "Annular bar complex computes chiral Hochschild homology", "refs_in_block": ["thm:HH-coHH-homology"]}
metadata/claims.jsonl:2765:{"label": "thm:wakimoto-ordered-bar", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 6710, "title": "Wakimoto bar complex descent", "labels_in_block": ["thm:wakimoto-ordered-bar", "eq:wakimoto-ordered-bar-descent"]}
metadata/claims.jsonl:3028:{"label": "thm:wakimoto-ordered-bar", "env_type": "theorem", "status": "ProvedHere", "file": "appendices/ordered_associative_chiral_kd.tex", "line": 2472, "title": "Wakimoto bar complex descent", "labels_in_block": ["thm:wakimoto-ordered-bar", "eq:wakimoto-ordered-bar-descent"]}
metadata/claims.jsonl:3088:{"label": "thm:annular-HH", "env_type": "theorem", "status": "ProvedHere", "file": "appendices/ordered_associative_chiral_kd.tex", "line": 7268, "title": "Annular bar complex computes chiral Hochschild homology", "refs_in_block": ["thm:HH-coHH-homology"]}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '8000,8050p' working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$m_k\big|_{\mathrm{scalar}} = (c/12)\,P_k$) is equivalent to
inverting the Shapovalov form at all levels---the same problem as
constructing all Virasoro singular vectors.  The generating
function is the graviton self-energy resolvent
\[
G(t;\lambda)
  = \mathrm{Tr}_{\fh}\!\left(\frac{1}{1 - t\,K(\lambda)}\right),
\]
where $K(\lambda)$ is the collision kernel at conformal
weight~$\lambda$.  At the symmetric point $\lambda = (c-1)/24$
(where $\Delta = \bar\Delta$), a universal factor $(x+2)$ appears
in $P_k$ for all $k \leq 5$---this is the conformal weight Ward
identity forcing a zero at $x = -2$.  Whether the factor persists
at all arities is tied to the question of whether the Shapovalov
determinant has a universal factorisation beyond the
Kac determinant formula.

\subsection{AP-OC Steinberg refinement}
\label{subsec:ap-oc-steinberg}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1730,1760p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
field theory on $\mathbb C_z\times\mathbb R_t$:
observables factorise holomorphically in~$z$ and
associatively in~$t$. The bar differential is the
closed (holomorphic) colour. The bar coproduct is the
open (topological) colour.
\end{remark}

\begin{remark}[Codimension-one generators for
\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
The construction above gives the operation space, not yet a minimal
generators-and-relations presentation, and by itself it does not
equip the ordered bar complex with a full Swiss-cheese algebra
structure. On compactified models the codimension-$1$ generator
families are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
 $|S|\ge 2$;
\item open interval-splitting faces in a Stasheff compactification
 of $E_1(m)$, equivalently cuts of the ordered open inputs into
 consecutive blocks;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1910,1945p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
[s^{-1}e_{I_1}|\cdots|s^{-1}e_{I_p}]
\otimes
[s^{-1}e_{I_{p+1}}|\cdots|s^{-1}e_{I_k}],
\]
where the $p=0$ and $p=k$ terms produce the coaugmentation.

This coproduct is the topological structure: it comes from
the ordered configuration space
$\mathrm{Conf}_k^{<}(\mathbb R)$ by cutting the
ordered real line at a point between $t_p$ and $t_{p+1}$.
The $p$ points to the left form one ordered subconfiguration;
the $k{-}p$ points to the right form another. The coassociativity
of~$\Delta$ is the associativity of interval composition.

\emph{Contrast with the holomorphic differential.}
The bar differential~$d$ extracts residues in the holomorphic
direction (collisions of points on~$\mathbb C$). The coproduct
$\Delta$ cuts in the topological direction (splitting the
ordered sequence on~$\mathbb R$). Together, the pair
$(d,\Delta)$ encodes both colours of the Swiss-cheese

thinking
**Focusing on claims**

I see that there are live hits to assess. It's important to focus specifically on affirmative false claims. There's also a possibility that the new explorer could provide a curated list. I might consider waiting for that. It seems like a good path forward to ensure we handle this accurately and make the most informed decisions. Let's explore this together! There’s plenty to analyze here, so I’ll take my time.
collab wait(call_MzapqgXJXJbAU0JceNaTZglq)
  receivers: 019d87ff-1291-78c3-8043-4f849d9122df
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '640,680p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Eone$-multiplication. Open-string field theory and
factorization on bordered curves carry intrinsic boundary
orderings. Integrable lattice models have $R$-matrices that
satisfy the (ordered) Yang--Baxter equation, not its symmetric
projection. In every physical setting where the bar complex
appears, the line/boundary direction is ordered before any
$\Sigma_n$-symmetrization is taken.

\textsc{Categorical primacy.} The categorical objects of
representation theory are ordered. Quantum groups, Yangians, and
braided tensor categories are the natural framework for chiral
algebras coupled to a spectral parameter; their structure
constants are matrix-valued and obey ordered identities (CYBE,
pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
categories are obtained from braided ones by the
$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
exactly the categorical analogue of the averaging
map~\eqref{eq:intro-averaging}.

\textsc{Operadic primacy of Swiss-cheese.} The bar complex
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*Swiss-cheese" chapters appendices standalone compute metadata README* main.tex working_notes.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
working_notes.tex:8022:\emph{the bar complex presents the Swiss-cheese algebra, as the
working_notes.tex:8706:relationship between the chiral bar complex and the Swiss-cheese
appendices/ordered_associative_chiral_kd.tex:1741:equip the ordered bar complex with a full Swiss-cheese algebra
compute/audit/forgetful_e_infty_to_e1_report.md:180:> Superseded by AP165: the bar complex is the ordered E_1 coalgebraic engine, not the Swiss-cheese algebra itself. The genuine SC datum is the derived-center pair $(C^\bullet_{ch}(A,A), A)$; three functors still extract the original algebra, the line-side Koszul dual, and the bulk observables.
compute/audit/forgetful_e_infty_to_e1_report.md:225:For the bar complex, the relevant coproduct depends on whether one works on ordered or unordered configuration spaces. Vol I works on unordered configurations (Sigma_n-equivariant), so the native coproduct is the factorization (cocommutative) one. Vol II's Swiss-cheese treatment introduces the ordered configurations, giving the deconcatenation (coassociative) coproduct as the open colour.
chapters/connections/bv_brst.tex:2050:compared is not ``the bar complex as a Swiss-cheese algebra'': the
compute/lib/en_bar_coproduct_engine.py:939:    r"""Analyze how the chiral bar complex sits inside the Swiss-cheese picture.
standalone/survey_modular_koszul_duality.tex:7087:bar complex, the shadow obstruction tower, the Swiss-cheese structure, the PVA
compute/audit/session_summary_2026_04_07_08.md:86:4. **thm:bar-swiss-cheese cited wrong bar complex.** The theorem statement referenced B(A) (unordered) when the Swiss-cheese structure lives on B^{ord}(A) (ordered). Fixed with proper E_1 primacy.
standalone/survey_track_b_compressed.tex:1489:bar complex, the shadow tower, the Swiss-cheese structure, the
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:2343:\begin{theorem}[$\mathfrak{sl}_2$ bar complex as Swiss-cheese
compute/lib/higher_dim_chiral_comparison_engine.py:1114:                'bar complex also captures via Res^{coll}_{0,2}(Theta_A). The Swiss-cheese '
compute/lib/higher_dim_chiral_comparison_engine.py:1117:                'encoded in our E_1 bar complex via the Swiss-cheese decomposition.'
chapters/theory/ordered_associative_chiral_kd.tex:1829:equip the ordered bar complex with a full Swiss-cheese algebra
compute/audit/vol1_full_audit_2026_04_08/qc_math_surfaces.json:724:      "normalized_prefix": "The ordered bar complex is an E_1 coalgebra and does not itself present the Swiss-cheese datum (Theorem~REF). The complete strictification theorem says that, once "
compute/audit/platonic_ideal_reconception.md:15:**Vol II** lifts the bar complex to three dimensions by identifying the Swiss-cheese structure, constructs the bulk-boundary-line triangle, computes examples, and develops the holographic frontier. The bar complex remains the protagonist; the Swiss-cheese structure is presented as a property it "carries."
compute/audit/platonic_ideal_reconception.md:33:**Vol II current thesis**: "The bar complex carries a Swiss-cheese structure that lifts chiral Koszul duality to three dimensions."
compute/audit/benjamin_chang/zhu_spectrum.md:388:4. **Non-vacuum modules**: The constrained Epstein as defined uses only the vacuum module. For a FULL CFT, one would sum over primaries of ALL modules (as in the Benjamin-Chang construction). Can the bar complex of V constrain the primary content of non-vacuum modules? This is related to the Swiss-cheese structure (Vol II) and the open/closed MC element Theta^{oc}.
compute/audit/fortification_plan_from_swarm.md:84:Volume II identifies a natural categorical context for these theorems: the open factorization dg-category C on a tangential log curve. In this context, the bar complex is the coalgebraic encoding of the twisting data of C, the derived center is the universal bulk, and the Koszul dual governs line operators. The Swiss-cheese operad SC^{ch,top} is the operadic governance, proved to be homotopy-Koszul.
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:1:r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1820,1845p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
associatively in~$t$. The bar differential is the
chiral (holomorphic) component. The bar coproduct is the
coassociative (topological) component.
\end{remark}

\begin{remark}[Codimension-one generators for
\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
The construction above gives the operation space, not yet a minimal
generators-and-relations presentation, and by itself it does not
equip the ordered bar complex with a full Swiss-cheese algebra
structure. On compactified models the codimension-$1$ generator
families are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
 $|S|\ge 2$;
\item open interval-splitting faces in a Stasheff compactification
 of $E_1(m)$, equivalently cuts of the ordered open inputs into
 consecutive blocks;
\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
 product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and

thinking
**Summarizing affirmative Swiss-cheese claims on bar complex**

I'm gathering three precise locations where the bar complex is affirmatively linked to Swiss-cheese structures, per the user's criteria. Each snippet carefully highlights claims attributing Swiss-cheese algebra or colors to the bar complex B(A) rather than the derived-center pair, along with a brief classification flagging the misleading aspect. I'll include file paths with line numbers and concise quotes to keep it clear and aligned with instructions.
codex
- `working_notes.tex:8022` — “the bar complex presents the Swiss-cheese algebra … $\barB(\cA)$ presents the Swiss-cheese algebra via factorisation on $\FM_k(\C)\times \Conf_k(\bR)$; in both cases the presenting object is a correspondence, not the algebra it produces.”  
  Classification: affirmative claim that B(A) itself is the Swiss-cheese algebra (misplaced SC datum).

- `appendices/ordered_associative_chiral_kd.tex:1741` — “The bar differential is the closed (holomorphic) colour. The bar coproduct is the open (topological) colour.”  
  Classification: assigns the two Swiss-cheese colours directly to the bar complex’s differential/coproduct, implying SC structure lives on B(A).

- `appendices/ordered_associative_chiral_kd.tex:1929` — “Together, the pair $(d,\Delta)$ encodes both colours of the Swiss-cheese algebra: … Bar differential $d$ … Coproduct $\Delta$ …”  
  Classification: explicitly reads the Swiss-cheese algebra onto the bar complex data rather than on the derived-center pair.
wait(call_MzapqgXJXJbAU0JceNaTZglq) 1 agents complete:
  019d87ff-1291-78c3-8043-4f849d9122df completed: "- `working_notes.tex:8022` — “the bar complex presents the Swiss-cheese algebra … $\barB(\cA)$ presents the Swiss-cheese…"
codex
The focused live sweep confirms the appendix and working-notes seams, but I’m also patching the compute/test docstrings that still say “bar complex = Swiss-cheese algebra” so the local tooling stops teaching the wrong object, not just the prose files.
exec
/bin/zsh -lc "rg -n -i -e 'bar complex = Swiss-cheese algebra|Together = Swiss-cheese algebra|\\(d, Delta\\) = Swiss-cheese algebra|bar complex presents the Swiss-cheese algebra|bar differential is the closed|bar coproduct is the open|full Swiss-cheese algebra structure|bar complex extracts the E_1-algebra data.*Together: Swiss-cheese|The swiss-cheese identification says the bar complex differential|The full Swiss-cheese bar complex uses BOTH simultaneously' appendices standalone working_notes.tex compute/lib compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
working_notes.tex:8022:\emph{the bar complex presents the Swiss-cheese algebra, as the
compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4:bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
compute/tests/test_heisenberg_bridge.py:16:    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:1:r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:6:3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
compute/lib/swiss_cheese_chain_model.py:339:    The swiss-cheese identification says the bar complex differential
compute/lib/factorization_coproduct_engine.py:615:    The full Swiss-cheese bar complex uses BOTH simultaneously:
exec
/bin/zsh -lc "sed -n '1815,1850p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2008,2045p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1908,1950p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 'bar differential|bar coproduct|Together, the pair \\(d,\\\\Delta\\)|closed \\(holomorphic\\) colour|open \\(topological\\) colour' chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2008,2045p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1908,1950p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:two-colours-geom}
The product $\FM_k(\mathbb C)\times\mathrm{Conf}_k^{<}(\mathbb R)$
is the geometric fingerprint of a 3d holomorphic-topological
field theory on $\mathbb C_z\times\mathbb R_t$:
observables factorise holomorphically in~$z$ and
associatively in~$t$. The bar differential is the
chiral (holomorphic) component. The bar coproduct is the
coassociative (topological) component.
\end{remark}

\begin{remark}[Codimension-one generators for
\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
The construction above gives the operation space, not yet a minimal
generators-and-relations presentation, and by itself it does not
equip the ordered bar complex with a full Swiss-cheese algebra
structure. On compactified models the codimension-$1$ generator
families are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
 $|S|\ge 2$;
 succeeded in 50ms:
\partial_F\overline{\FM}_k^{\mathrm{ord}}(\mathbb C)
\;\cong\;
\prod_{j=1}^r
\overline{\FM}_{|T_j|}^{\mathrm{ord}}(\mathbb C),
\]
where $|T_j|$ is the number of leaves of~$T_j$.

For the codimension-one faces: each is indexed by a forest
with $k{-}1$~trees, $k{-}2$ of which are single leaves and one
of which is a single binary tree with two leaves.
Concretely, the face $D_{i,i+1}$ corresponds to the forest in
which points $i$ and $i{+}1$ form a binary tree (they collide)
and all other points are isolated.

\emph{Contrast with the unordered case.}
In the unordered FM compactification, boundary strata are
indexed by \emph{trees} (rooted trees with unordered children).
In the ordered case, the strata are indexed by
\emph{planted forests} (ordered sequences of planar trees):
the ordering of trees within the forest records the linear
 succeeded in 50ms:
\label{rem:why-ordered-spaces}
The use of ordered versus unordered configuration spaces
reflects the operadic symmetry of the algebra:
\begin{itemize}
\item An $E_\infty$-algebra (any vertex algebra, any BD chiral
 algebra) has operations that are $\Sigma_n$-equivariant:
 the factorisation structure is defined on the \emph{unordered}
 configuration space $\mathrm{Conf}_k(X)/\Sigma_k$. The
 ordering on the bar complex is a computational convenience
 that can be quotiented out.
\item An $E_1$-algebra (an associative chiral algebra, a
 quantum vertex algebra in the sense of Etingof--Kazhdan)
 has operations indexed by \emph{ordered} compositions:
 its bar complex uses
 $\mathrm{Conf}_k^{\mathrm{ord}}(X)$. The ordering
 records the topological direction: in
 $\mathbb C_z\times\mathbb R_t$, points along
 $\mathbb R_t$ are ordered by time, and the
 $E_1$-structure is the time-ordered product.
\item The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$
 succeeded in 51ms:

\subsection{The deconcatenation coproduct}
\label{subsec:deconcatenation}

\begin{construction}[Deconcatenation coproduct;
\ClaimStatusProvedHere]
\label{constr:deconcatenation}
The ordered bar coalgebra carries a coassociative coproduct
$\Delta$ defined by \emph{deconcatenation}: cutting the
ordered sequence at every possible position. For a bar word
of length~$k$:
\[
\Delta[s^{-1}e_{I_1}|\cdots|s^{-1}e_{I_k}]
\;=\;
\sum_{p=0}^{k}
[s^{-1}e_{I_1}|\cdots|s^{-1}e_{I_p}]
\otimes
[s^{-1}e_{I_{p+1}}|\cdots|s^{-1}e_{I_k}],
\]
where the $p=0$ and $p=k$ terms produce the coaugmentation.
 succeeded in 51ms:
\;=\;
\sum_{p=0}^{k}
[s^{-1}e_{I_1}|\cdots|s^{-1}e_{I_p}]
\otimes
[s^{-1}e_{I_{p+1}}|\cdots|s^{-1}e_{I_k}],
\]
where the $p=0$ and $p=k$ terms produce the coaugmentation.

This coproduct is the topological structure: it comes from
the ordered configuration space
$\mathrm{Conf}_k^{<}(\mathbb R)$ by cutting the
ordered real line at a point between $t_p$ and $t_{p+1}$.
The $p$ points to the left form one ordered subconfiguration;
the $k{-}p$ points to the right form another. The coassociativity
of~$\Delta$ is the associativity of interval composition.

\emph{Contrast with the holomorphic differential.}
The bar differential~$d$ extracts residues in the holomorphic
direction (collisions of points on~$\mathbb C$). The coproduct
$\Delta$ cuts in the topological direction (splitting the
 succeeded in 51ms:
Total output lines: 574

appendices/ordered_associative_chiral_kd.tex-418-\index{monodromy!R-matrix}
appendices/ordered_associative_chiral_kd.tex-419-\index{Kohno connection}
appendices/ordered_associative_chiral_kd.tex:420:The bar differential on $\Barchord(A)$ extracts, at each
appendices/ordered_associative_chiral_kd.tex-421-collision $z_i=z_j$, the collision residue
appendices/ordered_associative_chiral_kd.tex-422-$r_{ij}(z_i-z_j)\in\operatorname{End}(\bar A\otimes\bar A)\otimes
--
appendices/ordered_associative_chiral_kd.tex-818-Geometrically, this is induced by the order-reversal involution on the ordered configuration space.
appendices/ordered_associative_chiral_kd.tex-819-
appendices/ordered_associative_chiral_kd.tex:820:The bar differential is the alternating sum of adjacent collision maps. The $i$-th face for
appendices/ordered_associative_chiral_kd.tex-821-$A^{\op}$ multiplies the $i$-th and $(i+1)$-st slots in the opposite order. Reversal carries that
appendices/ordered_associative_chiral_kd.tex-822-face to the $(n-i)$-th face for $A$ with exactly the sign written above. Hence $\mathsf{R}_A$ is a
--
appendices/ordered_associative_chiral_kd.tex-983-Therefore only the zero-defect and one-defect pieces survive.
appendices/ordered_associative_chiral_kd.tex-984-
appendices/ordered_associative_chiral_kd.tex:985:The bar differential merges adjacent slots. Multiplying two ordinary $A$-slots remains in $A$.
appendices/ordered_associative_chiral_kd.tex-986-Multiplying an $A$-slot with the unique $M$-slot remains in $M$ by the bimodule structure.
appendices/ordered_associative_chiral_kd.tex-987-There is no nonzero product of two defect slots. Hence the one-defect sector is a subcomplex.
--

thinking
**Reviewing chapter corrections**

I'm diving into an interesting chapter, and I’ve already noticed corrections at line 1815. However, a search result at line 1829 mentions something about not equipping with a "full Swiss-cheese algebra structure," which seems alright as is. I might not need to edit that phrase. The appendix feels a bit stale, so I’ll inspect my working notes further around line 8022. Also, I need to check line 1680, where it talks about "Swiss-cheese algebra" to clarify context.
exec
/bin/zsh -lc "sed -n '8018,8045p' working_notes.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1668,1695p' working_notes.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4048,4090p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{subsec:ap-oc-steinberg}

The three-functor picture from
Observation~\ref{obs:three-functors} acquires a slogan:
\emph{the bar complex presents the Swiss-cheese algebra, as the
Steinberg variety presents the Hecke algebra.}  More precisely,
$\barB(\cA)$ is the presenting coalgebra from which bulk,
boundary, and lines are extracted by three distinct functors:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $\Omega(\barB(\cA)) \simeq \cA$
  (cobar $=$ boundary reconstruction).
\item $\Omega(D_{\mathrm{Ran}}(\barB(\cA))) \simeq \cA^!$
  (Verdier dual cobar $=$ Koszul dual $=$ dual boundary).
\item $\RHom(\Omega(\barB(\cA)),\, \cA)
  \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
  (chiral Hochschild cochains $=$ bulk).
\end{enumerate}
The Steinberg variety $\widetilde{\cN} \times_{\cN}
\widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
convolution on the resolution; the bar complex
 succeeded in 52ms:
d_{\Ainf} &:\quad
  &&\text{boundary points collide (Stasheff)} \\
d_{\mathrm{mix}} &:\quad
  &&\text{bulk point hits boundary (bubbling)} \\
d_{\mathrm{clutch}} &:\quad
  &&\text{curve degenerates (nodal clutching)}
\end{alignat*}
Total: $d_{\mathrm{mod}} = d_{\mathrm{res}} + d_{\Ainf}
+ d_{\mathrm{mix}} + d_{\mathrm{clutch}}$, with
$d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
$d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.

This is the \textbf{Swiss-cheese algebra} on
$\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.

\medskip

On the other side of the boundary lives the \textbf{chiral
derived center}
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 succeeded in 52ms:
 R\!\operatorname{Hom}_{\operatorname{Fun}(\mathcal C,\mathcal C)}
 (\operatorname{Id}, \operatorname{Id})$
 is the universal bulk, computed in any chart by chiral Hochschild
 cochains $C^\bullet_{\mathrm{ch}}(A_b, A_b)$;
\item the \emph{Koszul dual} $A_b^!$ governs the line-operator
 category $\cA^!\text{-}\mathsf{mod}$ with its spectral braiding
 $R(z)$.
\end{enumerate}
The primitive hierarchy is:
\[
\mathcal C_{\mathrm{op}}
\;\xrightarrow{\;\operatorname{End}(b)\;}
A_b
\;\xrightarrow{\;\barB\;}
\barB(A_b)
\;\xrightarrow{\;\Theta\;}
\Theta_\cA
\;\xrightarrow{\;+\mu^{M_j}\;}
\Theta^{\mathrm{oc}}_\cA.
\]

thinking
**Inspecting structure encoding**

I’ve got a search result mentioning SC-algebra structure that encodes both closed and open colors. It could be related to the derived-center pair, but I'm not entirely sure. I definitely need to inspect this further to understand the connections better. It feels like there's a lot to unpack here, and I want to make sure I get it right! Let's take a closer look at this SC-algebra structure and its implications.
exec
/bin/zsh -lc "sed -n '6048,6098p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6186,6205p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1308,1328p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1458,1478p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7748,7772p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
A bar element of tensor degree~$k$ lives on the product
$\operatorname{FM}_k(\mathbb C)\times\operatorname{Conf}_k(\mathbb R)$.
The bar differential extracts OPE residues along collision divisors
of the first factor: when points $z_i$ and $z_j$ collide, the
residue of the propagator $\eta_{ij}=d\log(z_i-z_j)$ against the
collision divisor $\sigma_{\{i,j\}}$ yields the OPE mode
$a_{(n)}b$. The coproduct splits an ordered sequence of tensor
factors at a point of the second factor: an element
$a_1\otimes\cdots\otimes a_k$ with ordering
$t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
$t_p<c<t_{p+1}$ into
$(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
The bar complex carrying both structures is an
$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.

\subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}

The classical Swiss-cheese operad $\mathsf{SC}$ is Koszul
(Livernet, Voronov; Ginzburg--Kapranov). The proof: the
Koszul dual cooperad $\mathsf{SC}^{\text{\raisebox{0.3ex}{!\textasciigrave}}}$
 succeeded in 52ms:
ordered splitting of tensor factors at a cut point of the real line.
The Swiss-cheese operad encodes the interaction of these two
structures: holomorphic operations acting on the fiber above
the topological interval, topological operations governing the
sequential composition. The resulting two-colour algebraic
framework is not an embellishment of the bar complex but its
natural habitat: without the topological direction, the coproduct
has no operadic home, and the line-operator category has no
definition.

The primitive object of three-dimensional holomorphic-topological
quantum field theory on $\mathbb C_z \times \mathbb R_t$ is
therefore not the bar complex but the open/closed factorization
dg-category $\mathcal C$ on the bordified curve~$\widetilde{X}_D$. Its
objects are boundary conditions, its morphisms are open-string
states, and a choice of vacuum~$b$ yields a boundary algebra
$A_b = \operatorname{End}_{\mathcal C}(b)$, determined only up to
Morita equivalence. The governing operadic structure is the two-coloured
Swiss-cheese operad~$\mathsf{SC}^{\mathrm{ch,top}}$, with closed
colour $\operatorname{FM}_k(\mathbb C)$ and open colour $E_1(m)$,
 succeeded in 51ms:
$(\kappa,\alpha,S_4)$. The inverse limit exists and is automatically
Maurer--Cartan because $D_\cA^2=0$ (MC4).

In three dimensions, $\Theta_\cA$ extends to an open/closed
Maurer--Cartan element
$\Theta^{\mathrm{oc}}_\cA=\Theta_\cA+\sum_j\mu^{M_j}$
packaging the holomorphic-topological QFT on
$\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
(Volume~II).

The bar complex thus organises five mathematical structures as
projections of one object: the genus expansion
$F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$ \textsc{(uniform-weight)} is
a GUE matrix model at $N^2=\kappa$; the ordered bar
$\barB^{\mathrm{ord}}(\cA)$ produces $U_q(\mathfrak g)$ via FRT
reconstruction; the quantum-group $R$-matrix yields knot invariants;
 succeeded in 51ms:
pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
categories are obtained from braided ones by the
$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
exactly the categorical analogue of the averaging
map~\eqref{eq:intro-averaging}.

\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself
is a single-coloured $\Eone$-chiral coassociative coalgebra
over $(\mathrm{ChirAss})^!$. The SC structure emerges on the
derived center, not on the bar complex. The closed sector of any
Swiss-cheese algebra is recovered from the open sector by passing
to $\Sigma_n$-coinvariants along the open-to-closed boundary
operator. The closed sector is intrinsically a quotient of the
open sector, never an enrichment of it.

\paragraph{Historical context.}
The manuscript developed from the Beilinson--Drinfeld theory of
 succeeded in 51ms:
universal MC element~$\Theta_\cA$.
Sections~5--6 extracted the full hierarchy of characteristic
invariants from~$\Theta_\cA$ and classified chiral algebras by
shadow depth.
Section~7 tested the machine on every standard family.
Section~8 lifted the shadow obstruction tower into number theory: Dirichlet--sewing
series, Euler--Koszul classification, the two-variable $L$-object, and
the arithmetic packet connection.
Section~9 proved one-channel line concentration on the
simple-Lie-symmetry locus, the scalar package on the proved scalar
lane, and assembled the Koszulness programme.
Sections~10--11 transported the machine to three dimensions:
the bar differential became holomorphic factorization on the closed
colour, the deconcatenation coproduct became topological factorization
on the open colour, and the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
$\SCchtop$-algebra structure whose PVA shadow governs the deformation
quantization of Poisson vertex algebras to vertex algebras.
Section~12 packaged the entire holographic correspondence into a
six-component modular Koszul datum controlled by a single MC equation.


thinking
**Reviewing survey modifications**

It looks like there's a false line in the survey_modular_koszul_duality.tex around line 6190. There may also be an issue with a reversed pair at line 7760, which might not relate to AP165 but I'll check the pair order. Since the user asked about B(A) being E1 coalgebra, I see that SC lives on (Cbullet, A). I need to fix this reversed pair order in both files. I should inspect some additional lines in v2 too.
thinking
**Planning precise edits**

The user specifically requested exact edits based on findings, so I need to be careful and not broaden the scope too much. I'll aim to keep things minimal. My next step is to inspect the `survey_modular_koszul_duality_v2.tex` file, especially around lines 1390 and 6130 to ensure I apply those precise edits accurately. It’s important to stay focused on what the user needs without adding unnecessary changes.
exec
/bin/zsh -lc "sed -n '6128,6144p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1388,1405p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\widetilde X_D$. Objects are boundary conditions, morphisms
are open-string states, and a vacuum $b$ produces a boundary
algebra $A_b = \End_\cC(b)$ only up to Morita equivalence. The
governing operad is $\SCchtop$; it is homotopy-Koszul (proved
via Kontsevich formality), so the bar-cobar adjunction on
$\SCchtop$-algebras is a Quillen equivalence.

The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
its differential encodes the closed colour, and its coproduct
the open colour. Three objects must never be conflated:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the \emph{bar complex} $\barB(A_b)$ classifies twisting
morphisms, universal couplings between $A_b$ and $A_b^!$;
\item the \emph{chiral derived centre}
$\cZ^{\der}_{\ch}(\cC) =
R\Hom_{\Fun(\cC,\cC)}(\Id, \Id)$ is the universal bulk,
computed by chiral Hochschild cochains in any chart;
 succeeded in 51ms:
(Swiss-cheese: two colours, bulk and boundary) emerges on the
\emph{derived chiral centre}
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)=\ChirHoch^*(\cA,\cA)$,
computed using the bar complex as a resolution:
\[
\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)=R\Hom_{\cA\text{-bimod}}(\cA,\cA)\simeq\Hom(\barB(\cA),\cA).
\]
The pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)$ is the
$\SCchtop$-datum: $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the
bulk (closed colour), $\cA$ is the boundary (open colour), and the
action of the bulk on the boundary is by Hochschild evaluation.

For $E_\infty$-chiral input: Theorem~H gives
$\ChirHoch^*(\cA)\in\{0,1,2\}$ (concentrated, polynomial Hilbert
series). With conformal vector at non-critical level (Sugawara):
$\SCchtop+\text{conformal vector}=E_3$-topological;
the conformal vector kills the chiral direction. Proved for affine
KM at non-critical level; conjectural for general chiral algebras
exec
/bin/zsh -lc "sed -n '6518,6545p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Five negative principles: (N1) bar $\neq$ bulk; (N2) boundary
algebra is a chart; (N3) tangential log geometry required;
(N4) modularity is trace plus clutching on the open sector;
(N5) dg-shifted Yangian is proved for affine lineage only,
extension to non-standard families is programme.

\medskip\noindent\textbf{Stage~1 in detail: the local one-colour
theorem.}\enspace
The chiral derived centre
$\cZ^{\der}_{\ch}(\cA) = C^\bullet_{\ch}(\cA, \cA)$ is computed
by chiral Hochschild cochains: the cochain complex
$\prod_{k \ge 0} \Hom(\cA^{\otimes k}, \cA)$ with differential
from the bar resolution. On the Koszul locus, the complex
concentrates in cohomological degrees $\{0, 1, 2\}$ by
Theorem~H; the chiral Gerstenhaber bracket
$[-,-]_G \colon C^p \otimes C^q \to C^{p+q-1}$ makes
$C^\bullet_{\ch}(\cA, \cA)$ into an $E_2$-algebra. The
$\SCchtop$ structure emerges: the pair
$(C^\bullet_{\ch}(\cA, \cA),\, \cA)$ carries an
exec
/bin/zsh -lc "rg -n -i -e 'Swiss-cheese.*bar complex|bar complex.*Swiss-cheese|\\(d, Delta\\).*Swiss-cheese|Together: Swiss-cheese|bar complex extracts.*Swiss-cheese|bar complex differential.*closed colour|coproduct.*open colour|bar complex.*closed colour|bar complex.*open colour' compute/lib compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_higher_dim_chiral_comparison_engine.py:462:        """E_1 bar complex recovers E_2 braiding via Swiss-cheese."""
compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4:bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
compute/tests/test_heisenberg_bridge.py:1:"""The Heisenberg bridge: Vol I bar complex → Vol II Swiss-cheese structure.
compute/tests/test_heisenberg_bridge.py:16:    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
compute/lib/sc_koszul_dual_cooperad_engine.py:12:  bar complex and the convolution dg Lie algebra (Vol II, def:thqg-swiss-cheese-conv).
compute/lib/en_bar_coproduct_engine.py:90:3. The Swiss-cheese operad naturally produces ordered bar complexes.
compute/lib/en_bar_coproduct_engine.py:939:    r"""Analyze how the chiral bar complex sits inside the Swiss-cheese picture.
compute/lib/higher_dim_chiral_comparison_engine.py:746:            'Together: Swiss-cheese = E_2.'
compute/lib/higher_dim_chiral_comparison_engine.py:1114:                'bar complex also captures via Res^{coll}_{0,2}(Theta_A). The Swiss-cheese '
compute/lib/higher_dim_chiral_comparison_engine.py:1117:                'encoded in our E_1 bar complex via the Swiss-cheese decomposition.'
compute/lib/theorem_vicedo_envelope_engine.py:826:    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
compute/lib/theorem_vicedo_envelope_engine.py:829:    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
compute/lib/factorization_coproduct_engine.py:31:2. THE ORDERED (SWISS-CHEESE / E_1) BAR COMPLEX
compute/lib/factorization_coproduct_engine.py:615:    The full Swiss-cheese bar complex uses BOTH simultaneously:
compute/lib/factorization_coproduct_engine.py:645:            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
compute/lib/en_factorization_shadow.py:788:    The Swiss-cheese decomposition splits the bar complex into:
compute/lib/swiss_cheese_chain_model.py:339:    The swiss-cheese identification says the bar complex differential
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:1:r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.

thinking
**Inspecting patch possibilities**

I’m considering whether I could patch the higher_dim_chiral_comparison_engine. I noticed that line 1117 mentions it’s encoded in the E1 bar complex through Swiss-cheese decomposition. I definitely need to inspect this closely. I might also have to look into compute/tests/test_higher_dim—maybe something in there, but I’m not entirely sure if it’s applicable or not. More inspection of the relevant snippets seems essential here!
exec
/bin/zsh -lc "sed -n '736,752p' compute/lib/higher_dim_chiral_comparison_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    the chiral setting.  The bar complex in the C-direction is the
    factorization coalgebra; its coproduct in the R-direction gives the
    associative (topological) structure.  Together: E_2.
    """
    return {
        'e2_contains_e1': True,
        'e1_bar_recovers_e2': True,  # Via Swiss-cheese
        'mechanism': (
            'Bar coproduct = R-direction factorization. '
            'Bar differential = C-direction factorization. '
            'Together: Swiss-cheese = E_2.'
        ),
        'r_matrix_from_bar': 'r(z) = Res^{coll}_{0,2}(Theta_A)',
        'ybe_from_mc': 'MC equation => r(z) satisfies classical YBE',
        'quantum_ybe_from_bar': (
            'Quantum R-matrix from bar perturbative expansion '
            'satisfies quantum YBE (proved for type A).'
exec
/bin/zsh -lc "sed -n '1108,1120p' compute/lib/higher_dim_chiral_comparison_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '454,468p' compute/tests/test_higher_dim_chiral_comparison_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '780,796p' compute/lib/en_factorization_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20,40p' compute/lib/factorization_coproduct_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,100p' compute/lib/en_bar_coproduct_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
        'Q5_en_structure': {
            'answer': 'E_1 (chiral) in 2d; E_2 (braided) in 4d CS; E_3 in 6d HCS',
            'detail': (
                'Our algebras are E_1 (associative/chiral on curves). Costello 4d CS gives '
                'E_2 = E_1 x E_1 (Dunn) where one E_1 is chiral (C-direction) and one is '
                'topological (Sigma-direction). The E_2 braiding IS the R-matrix, which our '
                'bar complex also captures via Res^{coll}_{0,2}(Theta_A). The Swiss-cheese '
                'construction (Vol II) is the precise mechanism: SC^{ch,top} realizes the '
                'E_2 structure inside the chiral framework. So: E_2 braiding is ALREADY '
                'encoded in our E_1 bar complex via the Swiss-cheese decomposition.'
            ),
        },
    }
 succeeded in 51ms:
        assert 'Dunn' in data['decomposition']

    def test_e2_braiding_is_r_matrix(self):
        """The E_2 braiding gives the R-matrix."""
        data = four_d_cs_operadic_structure()
        assert 'R-matrix' in data['r_matrix_origin']

    def test_e2_vs_e1_bar_recovery(self):
        """E_1 bar complex recovers E_2 braiding via Swiss-cheese."""
        result = e2_braiding_vs_e1_bar()
        assert result['e2_contains_e1'] is True
        assert result['e1_bar_recovers_e2'] is True

    def test_r_matrix_from_bar(self):
        """r(z) = Res^{coll}_{0,2}(Theta_A) recovers the R-matrix."""
 succeeded in 50ms:
def swiss_cheese_shadow_heisenberg(k: Fraction = Fraction(1)) -> Dict[str, Any]:
    """E_2 shadow obstruction tower for Heisenberg, decomposed via Swiss-cheese.

    The Heisenberg algebra H_k has:
        kappa = k  (AP39: NOT k/2; all E_n agree)
        S_3 = 0      (free field, class G)
        shadow depth = 2 (terminates at kappa)

    The Swiss-cheese decomposition splits the bar complex into:
    - Pure chiral component (E_1^{ch} bar): classical chiral bar complex
    - Pure topological component (E_1^{top} bar): trivial (Heisenberg is
      commutative as a topological algebra)
    - Mixed component: vanishes for free fields (no mixed OPE)

    All three components give kappa = k, consistent with universality.
    """
    kappa = k
 succeeded in 51ms:
The manuscript contains TWO DIFFERENT bar complexes with TWO DIFFERENT
coproducts, related by the ordered-to-unordered covering:

1. THE UNORDERED (CHIRAL / FACTORIZATION) BAR COMPLEX
   B^ch(A) = sections over C_n(X) / FM_n(X)
   Coproduct: sum over ALL partitions I sqcup J = [0,n]
   This is COCOMMUTATIVE (symmetric under I <-> J)
   Source: factorization structure on Ran(X)
   Defined in: bar_construction.tex, thm:bar-chiral (line 1998)
               bar_construction.tex, thm:coassociativity-complete (line 1420)

2. THE ORDERED (SWISS-CHEESE / E_1) BAR COMPLEX
   B^ord(A) = sections over Conf_k^<(C) = ordered configurations
   Coproduct: deconcatenation, sum over positions i = 0,...,n only
   This is NOT cocommutative (depends on ordering)
   Source: E_1 coalgebra structure from Conf_k^<(R)
   Defined in: ordered_associative_chiral_kd.tex, constr:deconcatenation (line 1857)
               en_koszul_duality.tex, thm:bar-swiss-cheese (line 1219)

THEIR RELATIONSHIP
exec
/bin/zsh -lc "sed -n '932,946p' compute/lib/en_bar_coproduct_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

This is NOT the same as B_{E_2}(A) or B_{Com}(A).  It is the ordered
E_1 bar that preserves tensor ordering.  Concretely:

    B_{E_2}(A): elements are symmetric (up to homotopy) in the E_2 sense
    B^ch(A):    elements are ORDERED (the R-direction ordering is physical)

The manuscript uses the ordered (tensor coalgebra) structure because:
1. The R-matrix R(z) lives in End(V tensor V), which requires ordering.
2. The Yangian/quantum group structure requires the non-cocommutative part.
3. The Swiss-cheese operad naturally produces ordered bar complexes.

If one took the E_2 bar B_{E_2}(A) instead, one would lose the R-matrix
data and the quantum group structure.  One would retain only the
COMMUTATIVE part of the quantum group: the classical r-matrix r(z).

EXPLICIT COMPUTATIONS (this module):

1. B_{E_1}(k[x]) at arities 1-6: dimensions, coproduct matrices
2. B_{E_infty}(k[x]) at arities 1-6: dimensions, coproduct matrices
 succeeded in 52ms:


# ================================================================
# 8. The key theorem: Swiss-cheese decomposition
# ================================================================

def swiss_cheese_analysis() -> Dict[str, object]:
    r"""Analyze how the chiral bar complex sits inside the Swiss-cheese picture.

    The ordered chiral bar complex B^ch(A) is an E_1 bar coalgebra:
    - Differential d_B: from E_2/holomorphic collision data on Conf_k(C)
    - Coproduct Delta: from E_1/topological ordering on Conf_k(R)

    This means B^ch(A) is NOT B_{E_2}(A).  It is the ordered E_1 bar
    whose mixed holomorphic/topological provenance is later used to



thinking
**Considering bar complex structure**

I'm thinking about whether to include the section on bar complex in FM x Conf. If I do, I might want to mention the bar differential or coproduct as the E1 engine. I could add a row for "E1 engine on B(A): bar differential / deconcatenation," but I need to ensure the table's closed/open columns match the SC colors. Structuring the row to reflect derived center and boundary seems like a better approach.
thinking
**Revising subsection content**

It might be best to replace the entire subsection "The two colours" with concise and accurate prose. The product FM x Conf involves geometric provenance of bar differential and deconcatenation, wherein these operations create an E1 dg coalgebra, not an SC datum. The colors relate to closed and open colors from chiral Hochschild braces. I wonder if we should patch just a few lines or remove the table entirely. Consistency across both standalones is essential, so I’ll ensure the same corrected content is used. Let's craft a fitting replacement!
thinking
**Clarifying product functions**

This product captures the two geometric directions that are fundamental to the ordered E1 bar construction. I think it's important to present this clearly, ensuring that the reader understands how these directions play a role in the overall construction. Keeping it concise and straightforward will help prevent any confusion. Let's make sure the details are precise and convey the core concept effectively.
exec
/bin/zsh -lc "rg -n '\\(\\\\cA, ?\\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)|\\(\\\\cA, ?\\\\cZ\\"'^'"\\{\\\\der\\}_\\{\\\\ch\\}\\(\\\\cA\\)\\)' standalone/survey_modular_koszul_duality.tex standalone/survey_modular_koszul_duality_v2.tex standalone/programme_summary.tex standalone/programme_summary_sections5_8.tex standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/survey_modular_koszul_duality.tex:2369:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
standalone/survey_modular_koszul_duality.tex:7763:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
standalone/survey_modular_koszul_duality_v2.tex:2740:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
exec
/bin/zsh -lc "sed -n '2734,2746p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2362,2374p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
In three dimensions, $\Theta_\cA$ extends to an open/closed
Maurer--Cartan element
$\Theta^{\mathrm{oc}}_\cA=\Theta_\cA+\sum_j\mu^{M_j}$
packaging the holomorphic-topological QFT on
$\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
(Volume~II).

The bar complex thus organises five mathematical structures as
projections of one object: the genus expansion
 succeeded in 51ms:

In three dimensions, $\Theta_\cA$ extends to an open/closed
Maurer--Cartan element
$\Theta^{\mathrm{oc}}_\cA = \Theta_\cA + \sum_j \mu^{M_j}$
that packages the complete holomorphic-topological quantum field
theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
(Volume~II).

The bar complex thus organizes five mathematical structures
exec
/bin/zsh -lc "rg -n 'Swiss-cheese|bar complex =|Together =|closed colour|open colour|SC' compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_heisenberg_bridge.py compute/lib/swiss_cheese_chain_model.py compute/lib/factorization_coproduct_engine.py compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/tests/test_heisenberg_bridge.py:1:"""The Heisenberg bridge: Vol I bar complex → Vol II Swiss-cheese structure.
compute/tests/test_heisenberg_bridge.py:16:    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
compute/tests/test_heisenberg_bridge.py:188:    """B(A) is an E_1 chiral coassociative coalgebra; SC^{ch,top} on derived center pair."""
compute/tests/test_heisenberg_bridge.py:195:        The R-direction of the Swiss-cheese algebra is the tensor ordering.
compute/tests/test_heisenberg_bridge.py:218:        All higher A_infty operations vanish. The Swiss-cheese algebra
compute/lib/factorization_coproduct_engine.py:13:      the Swiss-cheese product FM_k(C) x Conf_k^<(R).
compute/lib/factorization_coproduct_engine.py:94:The Swiss-cheese theorem (thm:bar-swiss-cheese) lives in the ORDERED
compute/lib/factorization_coproduct_engine.py:444:    splitting in R (the two colors of the Swiss-cheese operad
compute/lib/factorization_coproduct_engine.py:611:    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
compute/lib/factorization_coproduct_engine.py:615:    The full Swiss-cheese bar complex uses BOTH simultaneously:
compute/lib/factorization_coproduct_engine.py:645:            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
compute/lib/factorization_coproduct_engine.py:911:# 13. R-MATRIX AND THE DESCENT FROM ORDERED TO UNORDERED
compute/lib/factorization_coproduct_engine.py:1015:            f"The Swiss-cheese structure adds a NON-cocommutative direction "
compute/lib/factorization_coproduct_engine.py:1031:    directions of the Swiss-cheese product:
compute/lib/factorization_coproduct_engine.py:1049:    These two directions later feed the Swiss-cheese picture, but
compute/lib/factorization_coproduct_engine.py:1050:    they do NOT by themselves make B(A) a two-coloured SC datum;
compute/lib/factorization_coproduct_engine.py:1055:    FACTORIZATION (cocommutative) coproduct.  The Swiss-cheese
compute/lib/factorization_coproduct_engine.py:1069:            "Used in: Swiss-cheese theorem, brace dg algebra, "
compute/lib/theorem_vicedo_envelope_engine.py:558:    kappa * lambda_1, which is a SCALAR (one-dimensional H^2(M_{1,0})).
compute/lib/theorem_vicedo_envelope_engine.py:826:    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the

thinking
**Evaluating theorem references**

I’m considering whether I need to patch all mentions inside the theorem_vol2 file. It seems some are about the structure of SC generally, which might be fine. For instance, line 643 refers to "SC^{ch,top} algebra structure on boundary algebra," but I'm questioning if I need the derived-center pair rather than the boundary algebra. I should inspect relevant functions, especially lines 560-650, to determine if anything is incorrect.
exec
/bin/zsh -lc "sed -n '184,226p' compute/tests/test_heisenberg_bridge.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '560,648p' compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Vol II: Swiss-Cheese and 3D HT
# ============================================================

class TestVolII_SwissCheese:
    """B(A) is an E_1 chiral coassociative coalgebra; SC^{ch,top} on derived center pair."""

    def test_coproduct_is_deconcatenation(self):
        """Delta: T^c(V) → T^c(V) ⊗ T^c(V) is the cofree coproduct.

        This is the R-factorization: TAUTOLOGICAL, not geometric.
        Every cofree coalgebra has a unique deconcatenation coproduct.
        The R-direction of the Swiss-cheese algebra is the tensor ordering.

        For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
        (modulo signs from the desuspension).
        """
        # The coproduct exists by the universal property of T^c(V).
        # We verify its structural properties.
        for h in range(2, 6):
            # At bar degree n, total weight h:
 succeeded in 51ms:
    shifted Poisson bracket (a "higher stress tensor").
    The boundary algebra is a module for the bulk.

    Our Vol II claims:
    (a) The bulk is the chiral derived center Z^der_ch(A) = C^bullet_ch(A_b, A_b).
        On cohomology, this is a Gerstenhaber algebra (= shifted Poisson).
        CDG's "shifted Poisson" IS our Gerstenhaber structure.

    (b) CDG's "boundary is a module for bulk" matches our Swiss-cheese
        directionality: the mixed sector F_mix makes F_op a module for F_cl.
        This IS the SC^{ch,top} structure.

    (c) CDG's setup: 3d N=2 gauge theories on C x R.
        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
        The operation spaces match.

    Returns: dict with compatibility verification.
    """
    return {
        "bulk_algebra": {
exec
/bin/zsh -lc "sed -n '818,836p' compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
      - The boundary chiral algebra is V_k(g), the affine KM envelope.
      - Our bar complex B(V_k(g)) computes the Koszul dual, which by
        Theorem A is the Verdier dual factorization coalgebra.
      - The modular operad algebra structure on {B^{(g,n)}(A)} organizes
        the higher-genus data that CFG's E_3 algebra encodes via
        factorization homology on 3-manifolds.

    The precise bridge: CFG's E_3 acts on the boundary via the
    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
    E_1-algebra data (the C-direction factorization) while the coproduct
    extracts the E_1-coalgebra data (the R-direction factorization).
    Together: Swiss-cheese on FM_k(C) x Conf_k(R).

    This is NOT a new theorem -- it is a COMPARISON between two descriptions
    of the same physical data (3d CS TFT on R x C with boundary on C).

    Attributes:
        lie_algebra: the semisimple Lie algebra g
        level: the CS level k
codex
```text
PE-8 cross-volume formula
formula: B(A) is E_1 coassociative coalgebra; SC^{ch,top} lives on (C^bullet_{ch}(A,A), A)
Vol I: live affirmative hits in standalone/, appendices/, working_notes.tex, compute/
Vol II: live affirmative hits in main.tex, conclusion.tex, factorization_swiss_cheese.tex, log_ht_monodromy_core.tex, rosetta_stone.tex, working_notes.tex
Vol III: live affirmative hit in compute/lib/swiss_cheese_cy3_e1.py
consistent? N
canonical vol: Vol I constitution + chapters/theory/en_koszul_duality.tex
others updated same session? Vol I yes; Vol II/III not writable, will report exact collisions
convention conversion: NA
verdict: ACCEPT
```

I’m editing only the writable Vol I files now. The changes are all narrow scoping fixes: replace “bar complex = Swiss-cheese algebra/colours” with “bar complex = E_1 engine; SC on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`,” and correct the couple of reversed pair orders in standalones.




thinking
**Inspecting patch details**

I need to edit multiple files. I should only use apply_patch and avoid using cat or running tools in parallel. First, I have to gather the exact file list and the changes I want. I’ll check out the file compute/lib/factorization_coproduct_engine.py around line 600 and then maybe look at theorem_vol2, especially line 645 for the explanation string after "Swiss-cheese bar complex adds Ass^c." I wonder if "Swiss-cheese bar complex" refers to the two-colored SC bar complex instead of B(A). I'll inspect the context more carefully between lines 600-646 to clarify.
thinking
**Examining chiral algebra structure**

I noticed that it says chiral algebra A on curve X is E_infty-chiral. The Swiss-cheese structure seems to add an ordered direction along R. When it states, "The full Swiss-cheese bar complex uses BOTH simultaneously," it describes B(A) with different aspects: Lie^c in the C-direction and Ass^c in the R-direction. I wonder if the module is comparing two bar constructions intentionally. I might need to update the documentation, especially around lines 603-648. I'll patch the compute/lib/theorem_vol2 top docstring and ensure the compatibility dictionary is correct.
thinking
**Reviewing docstring for clarity**

It looks like I need to check the test_heisenberg top docstring, specifically line 16 and possibly line 195, which mentions, "R-direction of the Swiss-cheese algebra is the tensor ordering." That sounds general and possibly fine, but since SC open color applies to the boundary algebra, it may not fit well with the tensor ordering of the bar complex. I also see that in test_coproduct_is_deconcatenation, the R-direction being linked to tensor ordering could be misleading unless it's explained with the geometry behind the bar coproduct. I'll be careful with this comparison.
thinking
**Searching for cheese bar uses**

I’m considering searching for “swiss cheese bar uses.” Maybe I should test some ideas or look into various applications. Using the right tool would help me find relevant information quickly, like looking up recipes or creative uses in cooking or food pairings. I want to make sure I gather helpful insights and suggestions to share! Let's see what I can find about this swiss cheese—it sounds interesting.
exec
/bin/zsh -lc "rg -n 'swiss_cheese_bar_uses|Swiss-cheese bar complex adds Ass\\"'^c|Together: Swiss-cheese on FM_k'"\\(C\\)|bar complex = Swiss-cheese algebra|\\(d, Delta\\) = Swiss-cheese algebra' compute" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/factorization_coproduct_engine.py:640:        'swiss_cheese_bar_uses': 'Com x Ass (closed x open)',
compute/lib/factorization_coproduct_engine.py:645:            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
compute/lib/theorem_vicedo_envelope_engine.py:829:    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:1:r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4:bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
compute/tests/test_heisenberg_bridge.py:16:    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)


thinking
**Exploring mathematical concepts**

I’m considering how holomorphic and topological directions are recorded. It's interesting because they capture different aspects of mathematical structures, but they don't directly provide the dual colours seen in Swiss-cheese algebra. There’s something intriguing about the relationship between these concepts, like how one influences the other without fully merging. This makes me think about how different mathematical ideas intersect, which feels like a puzzle waiting to be solved!
thinking
**Considering code improvements**

I’m thinking it might be a good idea to patch the docstring on line 4 in the same way as before. It could clarify things for anyone reading the code. Also, I could consider patching the results in `compute/lib/higher_dim_chiral_comparison_engine.py`. There’s a lot that could be improved there, so I want to ensure everything is in tip-top shape. Let’s see what else needs attention!
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,2 +1,3 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
@@ -5,3 +6,4 @@
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
@@ -572,3 +574,6 @@
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
@@ -642,3 +647,3 @@
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
M /Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bridge.py
@@ -15,3 +15,4 @@
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
@@ -194,3 +195,3 @@
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_vicedo_envelope_engine.py
@@ -825,6 +825,8 @@
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
M /Users/raeez/chiral-bar-cobar/working_notes.tex
@@ -1679,4 +1679,8 @@
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
@@ -8021,5 +8025,6 @@
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which boundary,
 boundary, and lines are extracted by three distinct functors:
@@ -8037,5 +8042,8 @@
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
@@ -8873,2 +8881 @@
 \end{document}
-
M /Users/raeez/chiral-bar-cobar/compute/lib/factorization_coproduct_engine.py
@@ -610,9 +610,12 @@
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
@@ -644,4 +647,5 @@
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
M /Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex
@@ -132,4 +132,5 @@
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
@@ -301,12 +302,8 @@
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
@@ -316,9 +313,10 @@
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
M /Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex
@@ -2739,3 +2739,3 @@
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
@@ -6134,5 +6134,9 @@
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
M /Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex
@@ -1430,4 +1430,5 @@
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
@@ -1598,12 +1599,8 @@
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
@@ -1613,9 +1610,10 @@
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
@@ -1811,4 +1809,5 @@
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
M /Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex
@@ -2368,3 +2368,3 @@
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
@@ -6197,4 +6197,7 @@
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
@@ -7762,3 +7765,3 @@
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
M /Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -3,3 +3,4 @@
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
M /Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex
@@ -1732,4 +1732,4 @@
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
@@ -1928,4 +1928,4 @@
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
M /Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex
@@ -994,5 +994,9 @@
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
M /Users/raeez/chiral-bar-cobar/compute/lib/swiss_cheese_chain_model.py
@@ -338,5 +338,7 @@
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
apply_patch(auto_approved=true) exited 0 in 92ms:
Success. Updated the following files:
M standalone/programme_summary_sections5_8.tex
M standalone/programme_summary.tex
M standalone/survey_track_b_compressed.tex
M standalone/survey_modular_koszul_duality_v2.tex
M standalone/survey_modular_koszul_duality.tex
M appendices/ordered_associative_chiral_kd.tex
M working_notes.tex
M compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
M compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
M compute/tests/test_heisenberg_bridge.py
M compute/lib/swiss_cheese_chain_model.py
M compute/lib/factorization_coproduct_engine.py
M compute/lib/theorem_vicedo_envelope_engine.py
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..9d87d678e38cd0fdc51c30ad38887766cc5d85d7
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,9 +8023,10 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which boundary,
 boundary, and lines are extracted by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
@@ -8035,9 +8040,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8879,3 @@
 No counterexample is known.
 
 \end{document}
-

file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..9d87d678e38cd0fdc51c30ad38887766cc5d85d7
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,9 +8023,10 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which boundary,
 boundary, and lines are extracted by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
@@ -8035,9 +8040,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8879,3 @@
 No counterexample is known.
 
 \end{document}
-


thinking
**Checking for typos**

I need to fix a typo in the working notes where I wrote "boundary, boundary, and lines." It should be clearer than that! I should check the phrasing to ensure it reads well. I should inspect it carefully. Also, I want to verify if there's any weird compile behavior happening. It seems like a good idea to search using rg for those specific phrases to catch any other potential issues. Let’s get this sorted out!
codex
The first patch batch is in. I’m checking the edited contexts now for accidental wording mistakes, then I’ll run a post-edit grep over the live surfaces to confirm the AP165/B54 formulations are actually gone locally.
exec
/bin/zsh -lc 'git diff -- standalone/programme_summary_sections5_8.tex standalone/programme_summary.tex standalone/survey_track_b_compressed.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex appendices/ordered_associative_chiral_kd.tex working_notes.tex compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_heisenberg_bridge.py compute/lib/swiss_cheese_chain_model.py compute/lib/factorization_coproduct_engine.py compute/lib/theorem_vicedo_envelope_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -e 'Swiss-cheese-formal bar|bar complex presents the Swiss-cheese|bar complex = Swiss-cheese algebra|\\(d, Delta\\) = Swiss-cheese algebra|differential encodes the closed colour|coproduct the open colour|bar differential is the closed|bar coproduct is the open|Together = Swiss-cheese algebra|The bar complex carrying both structures is an|\\(\\\\cA, \\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)|\\(\\\\cA, \\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)' standalone appendices chapters compute README.md main.tex working_notes.tex metadata 2>/dev/null" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 4419

diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 15cdbf4..b365657 100644
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -433,10 +433,10 @@ $\bar A^{\otimes n}$:
 d
 \;-\;
 \sum_{1\leq i<j\leq n}
-r_{ij}(z_i-z_j)\,d\log(z_i-z_j).
+r_{ij}(z_i-z_j)\,d(z_i-z_j).
 \end{equation}
 Here $r_{ij}$ acts in the $(i,j)$ tensor slots of~$\bar A^{\otimes n}$
-and $d\log(z_i-z_j)=dz_{ij}/(z_i-z_j)$ is the logarithmic form
+and $r_{ij}(z_{ij})\,dz_{ij}$ is the connection $1$-form
 on $\mathrm{Conf}_n^{\mathrm{ord}}(\mathbb{C})$.
 
 \emph{Flatness.}
@@ -479,7 +479,7 @@ R(z)
 succeeded in 51ms:
standalone/survey_track_a_compressed.tex:1317:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
standalone/introduction_full_survey.tex:1395:derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..9d87d678e38cd0fdc51c30ad38887766cc5d85d7
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,9 +8023,10 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which boundary,
 boundary, and lines are extracted by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
@@ -8035,9 +8040,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8879,3 @@
 No counterexample is known.
 
 \end{document}
-



thinking
**Evaluating git diff issues**

Oops, I've noticed that the git diff is huge because there are unrelated changes in the files. I need to be careful not to revert anything unrelated. It seems our patch might be large due to a dirty worktree from the user. 

I'll inspect the exact changes using `git diff -U2 -- <file> | rg`. I found leftover pair-order issues in `standalone/survey_track_a_compressed.tex` and `standalone/introduction_full_survey.tex`, which need patching since they are still active surfaces. I might also need to look for more pair orders in version 2!
thinking
**Patching and fixing typos**

I need to go ahead and patch the typo in `working_notes` that says, "from which boundary, boundary, and lines." It should be changed to "boundary, dual boundary, and bulk." 

Actually, the sentence should specify that "from which boundary, dual boundary, and bulk are extracted by three distinct functors." I’ll check to ensure the final search didn't miss any instances of `survey_track_a_compressed` and `introduction_full_survey`, so I need to inspect those contexts too. I want to make sure everything’s accurate!
codex
The post-edit grep cleared the direct bar/SC slogans I targeted, but it exposed two remaining live standalone files with the derived-center pair still reversed. I’m patching those pair-order drifts and a wording typo in `working_notes.tex`, then I’ll rerun the grep.
exec
/bin/zsh -lc "sed -n '1310,1322p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1388,1400p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

In three dimensions, $\Theta_\cA$ extends to an open/closed
Maurer--Cartan element
$\Theta^{\mathrm{oc}}_\cA=\Theta_\cA+\sum_j\mu^{M_j}$
packaging the holomorphic-topological QFT on
$\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
(Volume~II).

The bar complex thus organises five mathematical structures as
 succeeded in 51ms:
governing twisting morphisms between~$\cA$ and~$\cA^!$) and bulk data
(the chiral derived center
$\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, governing operators
in the interior).
The five theorems characterize the closed projection
$\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
projection is controlled by the $\SCchtop$-algebra structure on the
derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
(Theorem~\ref{thm:thqg-swiss-cheese}).
Modularity (the genus expansion and its
tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
trace and clutching operations on the open sector, not to the closed
algebra alone.
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..9d87d678e38cd0fdc51c30ad38887766cc5d85d7
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,9 +8023,10 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which boundary,
 boundary, and lines are extracted by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
@@ -8035,9 +8040,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8879,3 @@
 No counterexample is known.
 
 \end{document}
-


thinking
**Correcting typos**

I'm noticing that there are a couple of typos I need to patch up, specifically in the "working_notes" section. It’s important to ensure everything is clear and accurate, especially if others are relying on this information. Typos can create confusion, and I want to avoid any misunderstandings. Let’s get this sorted out right away! I'll address those issues to keep things tidy and professional.
file update
M /Users/raeez/chiral-bar-cobar/working_notes.tex
@@ -8028,4 +8028,5 @@
 Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which boundary,
-boundary, and lines are extracted by three distinct functors:
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
M /Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex
@@ -1316,3 +1316,3 @@
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
M /Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex
@@ -1394,3 +1394,3 @@
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
apply_patch(auto_approved=true) exited 0 in 99ms:
Success. Updated the following files:
M standalone/survey_track_a_compressed.tex
M standalone/introduction_full_survey.tex
M working_notes.tex
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-

file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-


thinking
**Rerunning searches**

I think I need to rerun the grep command because there might be other remaining hits that I haven’t captured yet. It’s important to search again using the right patterns to make sure I’m thorough. I want to ensure I'm not missing anything crucial. Let’s see what I can find this time to get a clearer picture of what I’m working with!
exec
/bin/zsh -lc "sed -n '8019,8046p' working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Kac determinant formula.

\subsection{AP-OC Steinberg refinement}
\label{subsec:ap-oc-steinberg}

The three-functor picture from
Observation~\ref{obs:three-functors} acquires a slogan:
\emph{the bar complex is the $E_1$ coalgebraic engine for the
Swiss-cheese programme, as the Steinberg variety presents the
Hecke algebra.}  More precisely,
$\barB(\cA)$ is the presenting coalgebra from which the
boundary algebra, the dual boundary, and the bulk are extracted
by three distinct functors:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $\Omega(\barB(\cA)) \simeq \cA$
  (cobar $=$ boundary reconstruction).
\item $\Omega(D_{\mathrm{Ran}}(\barB(\cA))) \simeq \cA^!$
  (Verdier dual cobar $=$ Koszul dual $=$ dual boundary).
\item $\RHom(\Omega(\barB(\cA)),\, \cA)
  \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
exec
/bin/zsh -lc "rg -n -i -e 'Swiss-cheese-formal bar|bar complex presents the Swiss-cheese|bar complex = Swiss-cheese algebra|\\(d, Delta\\) = Swiss-cheese algebra|differential encodes the closed colour|coproduct the open colour|bar differential is the closed|bar coproduct is the open|Together = Swiss-cheese algebra|The bar complex carrying both structures is an|\\(\\\\cA, \\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)|\\(\\\\cA, \\\\cZ\\"'^'"\\{\\\\der\\}_\\{\\\\ch\\}\\(\\\\cA\\)\\)' standalone appendices chapters compute README.md main.tex working_notes.tex metadata 2>/dev/null" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-






thinking
**Clarifying grep patterns**

So, "grep exit 1" indicates there are no matches, which is a good start. I need to consider that some false phrases may have slipped through, like "Together: Swiss-cheese = E2". The banned phrases seem to be cleared, but I need to search for the original exact pattern across all volumes to ensure we've covered everything thoroughly. If we get local hits, we can classify them, possibly using "rg" on text files and look for the most relevant lines. It's a bit complex, and I want to make sure nothing is missed!
thinking
**Checking write permissions**

Since we’ve only modified the local repository, there may still be issues with cross-volume collisions. I think I need to point out the inability to edit some files. It might be good to test write permissions, possibly using the `test -w` command on one file from each volume. However, the permission instructions might already indicate that editing isn’t allowed. I’ll definitely mention that certain files are not writable due to being outside the workspace, just to be clear!
thinking
**Evaluating editing process**

I want to confirm that the current repository still contains the expected items in the revised constitutions. The user asked for issues to be fixed in one pass, so the final output should detail the fixed findings along with non-writable issues in Vol II/III that remain. Since we can't edit these volumes, I think the final version should clarify that, but I wonder if mentioning non-writable status is necessary. I'll consider all volumes while addressing possible blockers and remaining collisions.
thinking
**Considering edit constraints**

I need to show the exact edits for each finding, but the prompt specifies that I should include the issue at file:line and the exact edits applied. If I can't make edits, I'm unsure if I should exclude findings from other volumes, even though the user wants them searched. I could possibly note them as unresolved blockers. I wonder if using exec_command with `perl -0pi` outside the workspace would work, but permissions might prevent that, especially without approval.
thinking
**Organizing findings for edits**

I need to lay out each finding clearly by specifying the problem at file:line, followed by the exact edit applied. The user mentioned there are around 15 local findings, plus some external collisions, so I should keep it concise. Including line numbers is essential, too. I think I can use "rg" to help with the changed patterns to make this process smoother. I’m aiming for clarity and manageability!
codex
Local Vol I is now clean for the specific AP165/B54 slogans I targeted. I’m collecting the final line numbers from the edited files and the remaining Vol II/III collision sites so the closeout can be a literal finding-by-finding audit log, not a vague summary.
exec
/bin/zsh -lc "printf '%s
' '/Users/raeez/chiral-bar-cobar-vol2/main.tex:1108' '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:7' '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2071' '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2230' '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:2047' '/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:8' '/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:152' '/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149' '/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3358' '/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:4'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'test -w /Users/raeez/chiral-bar-cobar-vol2/main.tex && echo writable || echo not_writable; test -w /Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py && echo writable || echo not_writable' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'derived-center side|SC datum|ordered \\"'$E_1'"\\"'$ dg coalgebra|Swiss-cheese-formal on the|ordered '"\\"'$E_1'"\\"'$ coalgebraic|ordered '"\\"'$E_1'"\\"'$ coalgebra on FM|derived-center pair|chiral '"\\(holomorphic\\) component|components of the \\"'$E_1'"\\"'$-chiral|Swiss-cheese operation space|coalgebraic engine for the'"\\nSwiss-cheese programme' standalone/programme_summary_sections5_8.tex standalone/programme_summary.tex standalone/survey_track_b_compressed.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/survey_track_a_compressed.tex standalone/introduction_full_survey.tex appendices/ordered_associative_chiral_kd.tex working_notes.tex compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_heisenberg_bridge.py compute/lib/swiss_cheese_chain_model.py compute/lib/factorization_coproduct_engine.py compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1108
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:7
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2071
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2230
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:2047
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:8
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:152
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3358
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:4
 succeeded in 52ms:
not_writable
not_writable
 exited 2 in 50ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-

exec
/bin/zsh -lc "rg -n 'derived-center side|SC datum|ordered \\"'$E_1'"\\"'$ dg coalgebra|ordered '"\\"'$E_1'"\\"'$ coalgebraic engine|ordered '"\\"'$E_1'"\\"'$ coalgebra on FM|Swiss-cheese operation space|components of the '"\\"'$E_1'"\\"'$-chiral coalgebra|chiral '"\\(holomorphic\\) component|derived-center pair \\"'$'"\\(C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\),\\\\cA\\)\\"'$|derived-center pair '"\\"'$'"\\(\\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\), \\\\cA\\)\\"'$'"' standalone/programme_summary_sections5_8.tex standalone/programme_summary.tex standalone/survey_track_b_compressed.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/survey_track_a_compressed.tex standalone/introduction_full_survey.tex appendices/ordered_associative_chiral_kd.tex working_notes.tex compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_heisenberg_bridge.py compute/lib/swiss_cheese_chain_model.py compute/lib/factorization_coproduct_engine.py compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/programme_summary.tex:1433:derived-center side. Algebras with higher-order
standalone/programme_summary.tex:1601:\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
standalone/programme_summary.tex:1612:two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
standalone/programme_summary.tex:1812: derived-center side.
standalone/programme_summary_sections5_8.tex:135:derived-center side. Algebras with higher-order
standalone/programme_summary_sections5_8.tex:304:\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
standalone/programme_summary_sections5_8.tex:315:two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:8:   the SC datum appears on (C^bullet_ch(A,A), A)
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:577:        the E_1 coalgebraic engine and the SC datum lives on the
working_notes.tex:1680:This is the \textbf{Swiss-cheese operation space} on
compute/lib/factorization_coproduct_engine.py:619:    the inputs for the ordered E_1 bar coalgebra, while the SC datum
compute/lib/factorization_coproduct_engine.py:1054:    they do NOT by themselves make B(A) a two-coloured SC datum;
appendices/ordered_associative_chiral_kd.tex:1733:chiral (holomorphic) component. The bar coproduct is the
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-

exec
/bin/zsh -lc "rg -n 'ordered \\"'$E_1'"\\"'$ coalgebraic|derived-center pair|derived center pair'"' standalone/survey_track_b_compressed.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/survey_track_a_compressed.tex standalone/introduction_full_survey.tex working_notes.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'ordered bar = E_1 coalgebra|ordered E_1 coalgebra on FM|derived-center pair|genuine Swiss-cheese datum|These data feed the Swiss-cheese pair' compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py compute/tests/test_heisenberg_bridge.py compute/lib/swiss_cheese_chain_model.py compute/lib/theorem_vicedo_envelope_engine.py compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/survey_track_a_compressed.tex:1316:supplies the holomorphic factorization data; the derived center pair
standalone/survey_track_b_compressed.tex:995:The bar complex of Volume~I is the ordered $E_1$ coalgebraic
standalone/survey_track_b_compressed.tex:999:derived-center pair
standalone/introduction_full_survey.tex:662:open/closed derived center pair
standalone/introduction_full_survey.tex:1222:of Volume~II emerges on the chiral derived center pair
standalone/introduction_full_survey.tex:1395:derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
standalone/introduction_full_survey.tex:1977: emerges on the chiral derived center pair, not on $\barB_X(\cA)$
working_notes.tex:1684:$\SCchtop$ datum lives on the derived-center pair
working_notes.tex:8047:Swiss-cheese datum itself lives on the derived-center pair
standalone/survey_modular_koszul_duality.tex:2368:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality.tex:6075:structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:6201:derived-center pair
standalone/survey_modular_koszul_duality.tex:7118: structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:7765:on the open colour, and the derived center pair
standalone/survey_modular_koszul_duality_v2.tex:2739:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality_v2.tex:6135:The bar complex of Volume~I is the ordered $E_1$ coalgebraic
standalone/survey_modular_koszul_duality_v2.tex:6139:derived-center pair
 succeeded in 52ms:
compute/tests/test_heisenberg_bridge.py:16:    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
compute/tests/test_heisenberg_bridge.py:17:       SC lives on the derived-center pair
compute/lib/theorem_vicedo_envelope_engine.py:826:    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
compute/lib/theorem_vicedo_envelope_engine.py:830:    factorization. These data feed the Swiss-cheese pair; they do not
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:2:coalgebraic engine; SC lives on the derived-center pair.
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:7:3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:578:        derived-center pair.
compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:648:            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4:ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:5:Swiss-cheese datum on the derived-center pair.
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-

exec
/bin/zsh -lc "rg -n 'components of the \\"'$E_1'"\\"'$-chiral|chiral '"\\(holomorphic\\) component|Swiss-cheese operation space|ordered \\"'$E_1'"\\"'$ presenting coalgebra'"' appendices/ordered_associative_chiral_kd.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
working_notes.tex:1680:This is the \textbf{Swiss-cheese operation space} on
working_notes.tex:8044:$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
appendices/ordered_associative_chiral_kd.tex:1733:chiral (holomorphic) component. The bar coproduct is the
appendices/ordered_associative_chiral_kd.tex:1929:$(d,\Delta)$ encodes both components of the $E_1$-chiral
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-






thinking
**Evaluating verification process**

I’m thinking about the verification of edits on the live Vol I surfaces, confirming there are no remaining matches for the targeted phrases. Vol II and III still have exact collisions, but those files aren't writable. I should mention the current line numbers with markdown links to the files for clarity. It seems practical to keep the final answer concise and list-shaped, aiming for about 20-25 lines and including 10 bullets with two sentences each for clarity.
thinking
**Clarifying edits to local clusters**

I’m outlining the local cluster bullet points based on specific files and edits. For instance, in `standalone/programme_summary_sections5_8.tex`, there were issues with class G/L being incorrectly labeled, and I changed it to a more accurate representation regarding colour tables and bar operations. Similar edits were made in `standalone/programme_summary.tex`, along with gauge summaries. The same goes for `standalone/survey_track_b_compressed.tex`, where I adjusted the bar differential. Lastly, I corrected a pair order and encoding in `standalone/survey_modular_koszul_duality_v2.tex`.
thinking
**Detailing the edit in modular Koszul duality**

I need to address the issues in `standalone/survey_modular_koszul_duality.tex`. It seems like there was a problem where the pair order was reversed, and the bar complex was incorrectly representing both structures as an SC-algebra. My edit involved swapping the pair order and updating the sentence to reflect an ordered E1 coalgebra, specifically noting the SC structure on `(C^\bullet_ch(A,A), A)`. This clarification is important for proper understanding and accurate documentation.
thinking
**Structuring findings**

I could group findings under "Remaining nonwritable," separate from the main list. In Vol III compute/lib/swiss_cheese_cy3_e1.py, I should mention it wasn't applied due to sandbox constraints. The citations might need clickable absolute paths. I can include multiple links in a single bullet, keeping it within about 30 lines with 12 bullets, each around two lines. Also, I need to refer to verification—post-edit grep returned no matches for the AP165/B54 slogans. I'll need to note external blockers too.
thinking
**Drafting concise findings**

I want to keep things clear and concise in my draft. I should include phrasing like "PROBLEM..." and "EXACT edit applied..." for each bullet, using a format like:  
- `PROBLEM at [file](...): ... EXACT edit applied: ...`  
This meets the user's request well. For external blocks, I can simply say "edit not applied," clarifying it's because the file is outside the writable workspace. To avoid confusion, I’ll use a separate heading "**Blocked**" and keep the bullets flat without nesting. Considering line count, I could cluster my points to stay within 70 lines total.
codex
**Applied**
- PROBLEM at [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:135), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:304), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:315): it said classes `G/L` have “Swiss-cheese-formal bar complexes” and put the SC colours on `B(\cA)`. EXACT edit applied: changed this to “finite shadow depth; only class `G` is Swiss-cheese-formal on the derived-center side,” replaced the table with `SC datum = (C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`, and rewrote the paragraph so `d_{\bar B}` and `\Delta` are only the two operations of the ordered `E_1` dg coalgebra.

- PROBLEM at [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1433), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1601), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1612), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1812): same AP165/B54 drift, repeated in both the colour table and the gauge/gravity summary. EXACT edit applied: same correction as above, plus changed the gauge-theory summary to “finite shadow depth; only class `G` is Swiss-cheese-formal on the derived-center side.”

- PROBLEM at [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) and [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:6135): both said the bar differential/coproduct are the closed/open SC colours. EXACT edit applied: rewrote both passages so the bar complex is the ordered `E_1` coalgebraic engine, and the actual `\SCchtop` datum lives on `(C^\bullet_{\mathrm{ch}}(A_b,A_b), A_b)`.

- PROBLEM at [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:2368), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:6201), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7765), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:1316), and [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:1395): the derived-center pair was reversed as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and one survey still said “the bar complex carrying both structures is an SC-algebra.” EXACT edit applied: swapped every reversed pair to `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)` and replaced the SC-on-bar sentence with “ordered bar = `E_1`-chiral coassociative coalgebra; SC appears on `(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`.”

- PROBLEM at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1733) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1929): the appendix still called the bar differential/coproduct the closed/open colours of the Swiss-cheese algebra. EXACT edit applied: synced it to the corrected chapter wording, changing this to “chiral/coassociative components” and “components of the `E_1`-chiral coalgebra.”

- PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar/working_notes.tex:1680) and [working_notes.tex](/Users/raeez/chiral-bar-cobar/working_notes.tex:8044): the notes still said “This is the Swiss-cheese algebra” and “the bar complex presents the Swiss-cheese algebra.” EXACT edit applied: changed this to “Swiss-cheese operation space” plus “the bar complex is the `E_1` coalgebraic engine,” and moved the SC datum explicitly to `(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)`.

- PROBLEM at [theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:2), [theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:648), [test_theorem_vol2_swiss_cheese_rectification_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py:4), and [test_heisenberg_bridge.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bridge.py:16): compute docs/tests still taught “bar complex = Swiss-cheese algebra” and “SC on boundary algebra.” EXACT edit applied: changed them to “ordered bar = `E_1` coalgebraic engine” and “SC lives on the derived-center pair.”

- PROBLEM at [swiss_cheese_chain_model.py](/Users/raeez/chiral-bar-cobar/compute/lib/swiss_cheese_chain_model.py:339), [factorization_coproduct_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/factorization_coproduct_engine.py:619), and [theorem_vicedo_envelope_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_vicedo_envelope_engine.py:826): helper docstrings still read the two geometric directions as a Swiss-cheese structure on `B(A)`. EXACT edit applied: rewrote each to say those directions are only the provenance of the ordered `E_1` bar complex, while the genuine SC datum is the derived-center pair.

**Blocked Outside Workspace**
- PROBLEM at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1108), [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:7), [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2071), [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2230), [log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:2047), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:8), [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:152), [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1149), and [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3358): Vol II still has affirmative SC-on-bar claims. Edit not applied: those files are outside the writable workspace here.

- PROBLEM at [swiss_cheese_cy3_e1.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:4): Vol III still says the `E_1` bar complex has Swiss-cheese structure. Edit not applied: that file is also outside the writable workspace here.

Verification: I ran a post-edit grep over live Vol I surfaces for the AP165/B54 slogans and pair-order drift; it returned no remaining local matches. I did not run TeX builds or `pytest`, since these were prose/docstring-only edits.
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 8bf3c953c85fa2349ad929e5b27989aebf276665..b365657b48cf599e5a5a852ff0acfb9c0cfbbb96
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1730,8 +1730,8 @@
 field theory on $\mathbb C_z\times\mathbb R_t$:
 observables factorise holomorphically in~$z$ and
 associatively in~$t$. The bar differential is the
-closed (holomorphic) colour. The bar coproduct is the
-open (topological) colour.
+chiral (holomorphic) component. The bar coproduct is the
+coassociative (topological) component.
 \end{remark}
 
 \begin{remark}[Codimension-one generators for
@@ -1926,8 +1926,8 @@
 direction (collisions of points on~$\mathbb C$). The coproduct
 $\Delta$ cuts in the topological direction (splitting the
 ordered sequence on~$\mathbb R$). Together, the pair
-$(d,\Delta)$ encodes both colours of the Swiss-cheese
-algebra:
+$(d,\Delta)$ encodes both components of the $E_1$-chiral
+coalgebra:
 \begin{center}
 \begin{tabular}{lll}
 \textbf{Structure} & \textbf{Direction} &
diff --git a/compute/lib/factorization_coproduct_engine.py b/compute/lib/factorization_coproduct_engine.py
index ee25cbae5cba614ff827a3febc6f3007117a311b..23cf69067abf9752724d3942ed7314decdb19f52
--- a/compute/lib/factorization_coproduct_engine.py
+++ b/compute/lib/factorization_coproduct_engine.py
@@ -608,13 +608,16 @@
     configurations).  Its bar complex uses P = Com in the chiral
     direction, giving the Lie cooperad and COCOMMUTATIVE coproduct.
 
-    The Swiss-cheese structure adds an ORDERED (E_1) direction along R.
-    The bar complex in the R-direction uses P = Ass, giving the
+    The Swiss-cheese comparison adds an ORDERED (E_1) direction along R.
+    The ordered bar complex uses P = Ass in that direction, giving the
     associative cooperad and DECONCATENATION coproduct.
 
-    The full Swiss-cheese bar complex uses BOTH simultaneously:
-      - Lie^c in the C-direction (bar differential, cocommutative)
-      - Ass^c in the R-direction (deconcatenation coproduct, non-cocommutative)
+    The same two geometric directions must be tracked simultaneously:
+      - Lie^c in the C-direction (bar differential provenance)
+      - Ass^c in the R-direction (deconcatenation provenance)
+    These do NOT make B(A) itself a two-coloured SC object; they are
+    the inputs for the ordered E_1 bar coalgebra, while the SC datum
+    appears on the derived-center pair (C^bullet_ch(A,A), A).
     """
     # Lie cooperad dimension: dim Lie^c(n) = (n-1)! for n >= 1
     lie_cooperad_dim = factorial(n - 1) if n >= 1 else 0
@@ -642,8 +645,9 @@
             f"At arity {n}: Lie^c({n}) has dim {lie_cooperad_dim}, "
             f"Ass^c({n}) has dim {ass_cooperad_dim}. "
             f"The chiral bar complex uses Lie^c (cocommutative factorization "
-            f"coproduct). The Swiss-cheese bar complex adds Ass^c "
-            f"(non-cocommutative deconcatenation) in the R-direction."
+            f"coproduct). Tracking the Swiss-cheese comparison adds Ass^c "
+            f"(non-cocommutative deconcatenation) in the R-direction, "
+            f"while B(A) remains the ordered E_1 coalgebraic engine."
         ),
     }
 
diff --git a/compute/lib/swiss_cheese_chain_model.py b/compute/lib/swiss_cheese_chain_model.py
index 6aab5f7d7f1b4e246eda2639bbb6b2e38ee472c8..ab5210d401c07b0f589d9e7fd6f8432d10dcfd54
--- a/compute/lib/swiss_cheese_chain_model.py
+++ b/compute/lib/swiss_cheese_chain_model.py
@@ -336,9 +336,11 @@
       - boundary_dim[w]: number of states in A at weight w
         (counting derivatives of generators up to weight w)
 
-    The swiss-cheese identification says the bar complex differential
-    is the C-direction factorization and the coproduct is the
-    R-direction factorization.
+    The same two geometric directions feed the ordered bar complex:
+    the differential records the C-direction factorization and the
+    coproduct records the R-direction factorization. The genuine
+    Swiss-cheese datum is the pair (Z^der_ch(A), A), not the bar
+    complex by itself.
     """
     algebra = _get_algebra(family, **kwargs)
     weights = _generator_weights(family)
diff --git a/compute/lib/theorem_vicedo_envelope_engine.py b/compute/lib/theorem_vicedo_envelope_engine.py
index aca1d32240c3aa02028d9fbdbab1da8c7ce64cdb..6896e03f0539a8c070a33faa038c8001c690d156
--- a/compute/lib/theorem_vicedo_envelope_engine.py
+++ b/compute/lib/theorem_vicedo_envelope_engine.py
@@ -823,10 +823,12 @@
         factorization homology on 3-manifolds.
 
     The precise bridge: CFG's E_3 acts on the boundary via the
-    Swiss-cheese algebra SC^{ch,top}.  Our bar complex extracts the
-    E_1-algebra data (the C-direction factorization) while the coproduct
-    extracts the E_1-coalgebra data (the R-direction factorization).
-    Together: Swiss-cheese on FM_k(C) x Conf_k(R).
+    Swiss-cheese operad SC^{ch,top}, realized on the derived-center pair
+    (Z^der_ch(A), A). Our ordered bar complex supplies the E_1
+    coalgebraic engine: its differential records the C-direction
+    factorization and its coproduct records the R-direction
+    factorization. These data feed the Swiss-cheese pair; they do not
+    make B(A) itself an SC algebra.
 
     This is NOT a new theorem -- it is a COMPARISON between two descriptions
     of the same physical data (3d CS TFT on R x C with boundary on C).
diff --git a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
index 5a7e3bf480bc56db4caae7570c9721c70d0ee1d1..6344e9370829471f5964c7923e8d1dc4ad0fb31e
--- a/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,9 +1,11 @@
-r"""Vol II Part I rectification engine: bar complex = Swiss-cheese algebra.
+r"""Vol II Part I rectification engine: ordered bar is the E_1
+coalgebraic engine; SC lives on the derived-center pair.
 
 CORE CLAIMS VERIFIED:
 1. Bar differential = C-direction (holomorphic) factorization
 2. Bar coproduct = R-direction (topological) factorization
-3. Together = Swiss-cheese algebra on FM_k(C) x Conf_k(R)
+3. Together = ordered E_1 coalgebra on FM_k(C) x Conf_k(R);
+   the SC datum appears on (C^bullet_ch(A,A), A)
 4. d_fib^2 = kappa * omega_g at genus g >= 1
 5. Arnold relation ensures d^2 = 0 at genus 0
 6. Arnold DEFECT at genus g produces curvature kappa * omega_g
@@ -570,7 +572,10 @@
         This IS the SC^{ch,top} structure.
 
     (c) CDG's setup: 3d N=2 gauge theories on C x R.
-        Our setup: SC^{ch,top} algebras on FM_k(C) x Conf_k(R).
+        Our setup: the SC^{ch,top} operation spaces are modeled on
+        FM_k(C) x Conf_k(R), while the ordered bar complex supplies
+        the E_1 coalgebraic engine and the SC datum lives on the
+        derived-center pair.
         The operation spaces match.
 
     Returns: dict with compatibility verification.
@@ -640,7 +645,7 @@
         },
         "swiss_cheese_action": {
             "Moriwaki": "SC operad acts on C_1-cofinite module categories",
-            "Vol_II": "SC^{ch,top} algebra structure on boundary algebra",
+            "Vol_II": "SC^{ch,top} structure on the derived-center pair (C^bullet_ch(A,A), A)",
             "compatible": True,
             "level_difference": "module categories vs algebras",
         },
diff --git a/compute/tests/test_heisenberg_bridge.py b/compute/tests/test_heisenberg_bridge.py
index 03031051f516cbacc3ec06621014aab9f9c6d6ed..5006eea733129910f1a296d569ddec8f68368b75
--- a/compute/tests/test_heisenberg_bridge.py
+++ b/compute/tests/test_heisenberg_bridge.py
@@ -13,7 +13,8 @@
 
   Vol II (Swiss-Cheese and 3D HT):
     6. Coproduct Delta from ordered deconcatenation (R-factorization)
-    7. (d, Delta) = Swiss-cheese algebra on FM(C) x Conf(R)
+    7. (d, Delta) = ordered E_1 coalgebra on FM(C) x Conf(R);
+       SC lives on the derived-center pair
     8. m_k = 0 for k >= 3 (formality: Heisenberg is E_infty)
     9. PVA descent: regular part of m_2 = commutative, singular = lambda-bracket
    10. Spectral R-matrix: trivial (E_infty => no braiding)
@@ -192,7 +193,7 @@
 
         This is the R-factorization: TAUTOLOGICAL, not geometric.
         Every cofree coalgebra has a unique deconcatenation coproduct.
-        The R-direction of the Swiss-cheese algebra is the tensor ordering.
+        The R-direction behind the Swiss-cheese comparison is the tensor ordering.
 
         For Heisenberg: Delta(a⊗a⊗η) = (a⊗η) ⊗ (a) + (a) ⊗ (a⊗η)
         (modulo signs from the desuspension).
diff --git a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
index 69fe03209dd61ae9dd5aaa76c8a35557e551df7a..ea6d3391da85a0b42a5f4693fc463b900a57f6bc
--- a/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
+++ b/compute/tests/test_theorem_vol2_swiss_cheese_rectification_engine.py
@@ -1,7 +1,8 @@
 r"""Tests for Vol II Part I rectification engine.
 
 50+ tests verifying the core claims of Vol II Part I:
-bar complex = Swiss-cheese algebra on FM_k(C) x Conf_k(R).
+ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
+Swiss-cheese datum on the derived-center pair.
 
 Test structure follows the multi-path verification mandate:
 every claim verified by at least 2 independent paths.
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index 75999f7e98874565f6b0f0a7333a0bd3e1e92254..7ea2042f37dceb32a17e1c2652587cd3874f23bd
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -1392,7 +1392,7 @@
 The five theorems characterize the closed projection
 $\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
 projection is controlled by the $\SCchtop$-algebra structure on the
-derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
+derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 Modularity (the genus expansion and its
 tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 7d61e282455a2a0b506bdca3358dab15010e7ab6..3102669d44cc66dee8dd6193ad5099c063b7d231
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -1428,8 +1428,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -1596,28 +1597,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
@@ -1809,8 +1807,9 @@
 
 \begin{enumerate}[(a)]
 \item \emph{Gauge theories} (classes~$\mathbf{G}$,
- $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
+ $\mathbf{L}$): finite shadow depth; only
+ class~$\mathbf{G}$ is Swiss-cheese-formal on the
+ derived-center side.
  The collision residue has at most a simple pole.
  The bar complex is effectively quadratic or cubic.
  The representation theory is governed by quantum groups with
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index ae60a6020fb8a7af42ba30212842ee186c7d65a9..36a8e39cf710d16b8660d185a6951e185b85fe94
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -130,8 +130,9 @@
 \noindent
 This table encodes a structural dichotomy: algebras whose
 collision residue has at most a simple pole (classes~$\mathbf{G}$
-and~$\mathbf{L}$) have finite shadow depth and
-Swiss-cheese-formal bar complexes; algebras with higher-order
+and~$\mathbf{L}$) have finite shadow depth; only
+class~$\mathbf{G}$ is Swiss-cheese-formal on the
+derived-center side. Algebras with higher-order
 poles (class~$\mathbf{M}$) have infinite shadow towers and
 genuinely non-formal $A_\infty$-structure.
 
@@ -299,28 +300,25 @@
 \toprule
 & \textbf{Closed colour} & \textbf{Open colour} \\
 \midrule
-\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
-\textbf{Structure} & Bar differential $d_{\barB}$ &
- Deconcatenation $\Delta$ \\
-\textbf{Physics} & Holomorphic factorization & Topological
- factorization \\
-\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
-\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
- $T^c(s^{-1}\bar\cA)$ \\
-\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
- Deconcatenation ($n+1$ terms) \\
+\textbf{Geometry} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
+\textbf{SC datum} & $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
+ $\cA$ \\
+\textbf{Bar engine} & Collision-residue differential on $B(\cA)$ &
+ Deconcatenation coproduct on $B(\cA)$ \\
+\textbf{Physics} & Bulk operators & Boundary operators \\
 \bottomrule
 \end{tabular}
 \end{center}
 
 \noindent
-The closed colour is the holomorphic factorization of
-Section~\ref{sec:bar}: the bar differential extracts OPE
-residues, produces $d^2 = 0$ at genus~$0$, and acquires
-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
-open colour is the topological factorization: the
-deconcatenation coproduct splits an ordered sequence at every
-consecutive position, producing the cofree tensor coalgebra.
+The bar differential and the deconcatenation coproduct are the
+two operations of the ordered $E_1$ dg coalgebra $B(\cA)$.
+They record the holomorphic and topological directions, but
+they do not by themselves furnish the two colours of a
+Swiss-cheese algebra. The closed and open colours live on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$:
+bulk operators act on the boundary, but not conversely.
 
 The directionality of the Swiss-cheese operad is strict:
 \emph{no open inputs produce closed outputs}. Bulk operators
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 4fdcd4f13106e05910b52a9c086c8569ecad4cf6..1fff0d3896a740111394e3f7d4f4eeffa721e32c
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -2366,7 +2366,7 @@
 that packages the complete holomorphic-topological quantum field
 theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6195,8 +6195,11 @@
 $t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
 $t_p<c<t_{p+1}$ into
 $(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
-The bar complex carrying both structures is an
-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
+These two operations make the ordered bar complex an
+$E_1$-chiral coassociative coalgebra. The
+$\mathsf{SC}^{\mathrm{ch,top}}$ structure appears only on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}
 
@@ -7760,7 +7763,7 @@
 the bar differential became holomorphic factorization on the closed
 colour, the deconcatenation coproduct became topological factorization
 on the open colour, and the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ acquired an
 $\SCchtop$-algebra structure whose PVA shadow governs the deformation
 quantization of Poisson vertex algebras to vertex algebras.
 Section~12 packaged the entire holographic correspondence into a
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index e403f6c3c54071eff7f093accf2843d19d72ad23..d22685a4c4d9c8b7ef5549a8a85897ca10d21294
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -2737,7 +2737,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
@@ -6132,9 +6132,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index b613c97f7c62fb32cbc1ab9f07da1749a4b3f6c5..cb62bb8b88937153678a962d34c4c5dac04b9700
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -1314,7 +1314,7 @@
 packaging the holomorphic-topological QFT on
 $\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
 supplies the holomorphic factorization data; the derived center pair
-$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
+$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ carries the
 $\SCchtop$-algebra structure encoding both closed and open colours;
 and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 (Volume~II).
diff --git a/standalone/survey_track_b_compressed.tex b/standalone/survey_track_b_compressed.tex
index 9e98d291931a79782ac70791b7ab2099aa2d39af..a925c778e7c0eeef604009fac74007c4e1b36d10
--- a/standalone/survey_track_b_compressed.tex
+++ b/standalone/survey_track_b_compressed.tex
@@ -992,9 +992,13 @@
 via Kontsevich formality), so the bar-cobar adjunction on
 $\SCchtop$-algebras is a Quillen equivalence.
 
-The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
-its differential encodes the closed colour, and its coproduct
-the open colour. Three objects must never be conflated:
+The bar complex of Volume~I is the ordered $E_1$ coalgebraic
+engine for $\cC$: its differential records holomorphic
+collision data, and its coproduct records ordered topological
+splitting. The $\SCchtop$ structure itself lives on the
+derived-center pair
+$(C^\bullet_{\mathrm{ch}}(A_b, A_b),\, A_b)$.
+Three objects must never be conflated:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item the \emph{bar complex} $\barB(A_b)$ classifies twisting
 morphisms, universal couplings between $A_b$ and $A_b^!$;
diff --git a/working_notes.tex b/working_notes.tex
index c8313548e85b3acdc5ed14763aa349016ebd056c..5602c7f07a58a6beb7f35c2c99e9544540b8e5bd
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -1677,8 +1677,12 @@
 $d_{\mathrm{mod}}^2 = 0$ at genus~$0$ and
 $d_{\mathrm{mod}}^2 = m_0$ at genus $g \geq 1$.
 
-This is the \textbf{Swiss-cheese algebra} on
+This is the \textbf{Swiss-cheese operation space} on
 $\FM_k(\C) \times \mathrm{Conf}_m(\mathbb{R})$.
+The ordered bar complex extracted from it remains a
+single-coloured $E_1$-chiral coalgebra; the genuine
+$\SCchtop$ datum lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$.
 
 \medskip
 
@@ -8019,10 +8023,12 @@
 
 The three-functor picture from
 Observation~\ref{obs:three-functors} acquires a slogan:
-\emph{the bar complex presents the Swiss-cheese algebra, as the
-Steinberg variety presents the Hecke algebra.}  More precisely,
-$\barB(\cA)$ is the presenting coalgebra from which bulk,
-boundary, and lines are extracted by three distinct functors:
+\emph{the bar complex is the $E_1$ coalgebraic engine for the
+Swiss-cheese programme, as the Steinberg variety presents the
+Hecke algebra.}  More precisely,
+$\barB(\cA)$ is the presenting coalgebra from which the
+boundary algebra, the dual boundary, and the bulk are extracted
+by three distinct functors:
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item $\Omega(\barB(\cA)) \simeq \cA$
   (cobar $=$ boundary reconstruction).
@@ -8035,9 +8041,12 @@
 The Steinberg variety $\widetilde{\cN} \times_{\cN}
 \widetilde{\cN}$ presents the Hecke algebra $H(W)$ via
 convolution on the resolution; the bar complex
-$\barB(\cA)$ presents the Swiss-cheese algebra via
-factorisation on the configuration space
-$\mathrm{FM}_k(\C) \times \mathrm{Conf}_k(\bR)$.  In both
+$\barB(\cA)$ is the ordered $E_1$ presenting coalgebra whose
+bar-cobar, Verdier-dual, and Hochschild functors recover the
+boundary algebra, the dual boundary, and the bulk. The
+Swiss-cheese datum itself lives on the derived-center pair
+$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$ computed from
+$\barB(\cA)$ via the bar resolution. In both
 cases, the presenting object is a \emph{correspondence},
 not the algebra it produces.
 
@@ -8871,4 +8880,3 @@
 No counterexample is known.
 
 \end{document}
-

tokens used
460,508
