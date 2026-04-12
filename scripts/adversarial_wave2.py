#!/usr/bin/env python3
"""
Adversarial Wave 2 — 110 Codex Agents
MAXIMALLY harsh: seams, foundations, broken tiles, cosmetics, aesthetics.
Every finding MUST include the fix.

Usage:
    python3 scripts/adversarial_wave2.py [--batch-size 12] [--timeout 900]
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"wave2_audit_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
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
"""


def agent(aid, prompt, cwd=VOL1):
    AGENTS.append({"id": aid, "prompt": PREAMBLE + "\n\n" + prompt, "cwd": cwd, "model": "gpt-5.4"})


def run_agent(a, timeout=900):
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-", "-m", a["model"], "-C", a["cwd"], "--full-auto"],
            input=a["prompt"], capture_output=True, text=True, timeout=timeout,
        )
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} ({dt:.0f}s)\n\n{r.stdout}\n\n---\nSTDERR:\n{r.stderr}")
        return a["id"], r.returncode == 0, dt
    except subprocess.TimeoutExpired:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — TIMEOUT ({dt:.0f}s)\n")
        return a["id"], False, dt
    except Exception as e:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — ERROR: {e}\n")
        return a["id"], False, dt


# ═══════════════════════════════════════════════════════════════════════════
# TIER A: SEAM AUDIT (20 agents)
# Transitions between chapters. Cross-reference consistency.
# Convention bridges. Information that falls through cracks.
# ═══════════════════════════════════════════════════════════════════════════

SEAM_PAIRS = [
    ("S01_bar_to_cobar", "bar_construction.tex", "cobar_construction.tex",
     "Bar→Cobar transition. Check: (a) conventions for coalgebra/algebra consistent at the interface, (b) desuspension/suspension grading consistent, (c) augmentation ideal convention matches, (d) T^c vs T notation consistent, (e) the 'four objects' clearly distinguished at the boundary"),
    ("S02_bar_to_higher_genus", "bar_construction.tex", "higher_genus_foundations.tex",
     "Bar→Higher genus transition. Check: (a) flat bar (d^2=0) to curved bar (d^2=kappa*omega_g) transition is explicit, (b) which differential is which (d_bar vs d_g vs d_fib), (c) coderived vs ordinary category specified at each point"),
    ("S03_koszul_to_shadow", "chiral_koszul_pairs.tex", "higher_genus_modular_koszul.tex",
     "Koszul pairs→Shadow tower. Check: (a) Koszul equivalences feed correctly into shadow tower, (b) the shadow tower uses the right bar (B^ord vs B^Sigma), (c) kappa definition consistent"),
    ("S04_shadow_to_examples", "higher_genus_modular_koszul.tex", "landscape_census.tex",
     "Shadow tower→Landscape census. Check: (a) every family in the census has correct kappa, r-matrix, class, (b) the shadow tower classification (G/L/C/M) matches the census entries, (c) boundary values checked"),
    ("S05_foundations_to_complementarity", "higher_genus_foundations.tex", "higher_genus_complementarity.tex",
     "Foundations→Complementarity. Check: (a) the fiber-center identification (C0) feeds correctly into C1/C2, (b) the duality involution is well-defined on the correct objects, (c) no hidden perfectness assumptions"),
    ("S06_intro_to_body", "introduction.tex", "concordance.tex",
     "Introduction→Body. Check: (a) every theorem advertised in the introduction is actually proved in the body, (b) status claims match, (c) no scope inflation in the introduction vs actual theorems, (d) cross-references resolve"),
    ("S07_preface_to_intro", "preface.tex", "introduction.tex",
     "Preface→Introduction. Check: (a) the preface narrative is consistent with the introduction's theorem statements, (b) no stronger claims in preface than introduction, (c) notation introduced in preface used consistently"),
    ("S08_en_to_topologization", "en_koszul_duality.tex", "higher_genus_modular_koszul.tex",
     "E_n Koszul→Topologization. Check: (a) the topologization theorem scope is consistent between files, (b) chain-level vs cohomological status consistent, (c) Sugawara hypothesis present in all relevant statements"),
    ("S09_examples_mutual", "kac_moody.tex", "virasoro.tex",
     "KM→Vir examples. Check: (a) kappa formulas consistent, (b) r-matrix conventions consistent, (c) classification (L vs M) consistent, (d) central charge formulas match census"),
    ("S10_examples_to_wn", "virasoro.tex", "w_algebras.tex",
     "Vir→W_N. Check: (a) W_2=Vir specialization works, (b) kappa(W_N) at N=2 gives c/2, (c) harmonic number H_N convention consistent"),
    ("S11_bv_brst_to_body", "bv_brst.tex", "higher_genus_modular_koszul.tex",
     "BV/BRST→Main theorems. Check: (a) MC5 status consistent between files, (b) chain-level vs coderived distinction maintained, (c) class-M caveats propagated"),
    ("S12_ordered_to_symmetric", "e1_modular_koszul.tex", "higher_genus_modular_koszul.tex",
     "E1 ordered→Symmetric modular. Check: (a) the averaging map av: g^{E1}→g^mod is explicit, (b) which theorems are on g^{E1} vs g^{mod} is clear, (c) the E1-first architecture is maintained"),
    ("S13_concordance_to_body", "concordance.tex", "chiral_koszul_pairs.tex",
     "Concordance→Theory. Check: (a) every theorem status in concordance matches the actual .tex, (b) no stale statuses, (c) routing remarks present for circular dependencies"),
    ("S14_standalone_to_main", "standalone/", "chapters/",
     "Standalones→Main manuscript. Check: (a) formulas in standalone papers match the main text, (b) no convention drift, (c) macros defined via providecommand, (d) no stale claims"),
    ("S15_appendices_to_body", "appendices/", "chapters/theory/",
     "Appendices→Theory. Check: (a) appendix results cited correctly in body, (b) no circular dependencies, (c) notation consistent"),
    ("S16_v1_to_v2_bridge", "", "",
     "Vol I→Vol II bridge. Check across ~/chiral-bar-cobar and ~/chiral-bar-cobar-vol2: (a) theorem status claims about Vol I results in Vol II are accurate, (b) formula conventions converted (OPE→lambda-bracket), (c) the E1/E_inf hierarchy (V2-AP1-AP24) is respected, (d) no bare Omega/z or bare kappa in Vol II"),
    ("S17_v1_to_v3_bridge", "", "",
     "Vol I→Vol III bridge. Check across ~/chiral-bar-cobar and ~/calabi-yau-quantum-groups: (a) kappa subscripted in Vol III (AP113), (b) theorem status claims accurate, (c) CY-to-chiral functor claims match Vol I theorems, (d) no bare kappa"),
    ("S18_v2_to_v3_bridge", "", "",
     "Vol II→Vol III bridge. Check across ~/chiral-bar-cobar-vol2 and ~/calabi-yau-quantum-groups: (a) 3d HT claims in Vol III match Vol II, (b) E_3 scope consistent, (c) BPS/CoHA claims properly conditioned"),
    ("S19_compute_to_manuscript", "compute/lib/", "chapters/examples/",
     "Compute engines→Manuscript. Check: (a) computed values in engines match what manuscript claims, (b) test expected values match compute output, (c) no AP128 (engine/test same wrong model)"),
    ("S20_readme_to_manuscript", "README.md", "chapters/",
     "README→Manuscript. Check: (a) page counts accurate, (b) theorem status claims in README match actual, (c) no scope inflation, (d) test counts accurate"),
]

for sid, file1, file2, desc in SEAM_PAIRS:
    prompt = f"""MISSION: SEAM AUDIT between {file1 or 'cross-volume'} and {file2 or 'cross-volume'}.

{desc}

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX."""
    agent(sid, prompt)


# ═══════════════════════════════════════════════════════════════════════════
# TIER B: FOUNDATION AUDIT (20 agents)
# Missing definitions. Prerequisites not established. Hidden imports.
# Objects used before axiomatization.
# ═══════════════════════════════════════════════════════════════════════════

FOUNDATION_CHECKS = [
    ("F01_definitions_bar", "chapters/theory/bar_construction.tex", "Check every \\begin{definition} and every object first used. Is each object DEFINED before USED? Are all ambient categories specified? Is the augmentation ideal defined? Is the grading (cohomological |d|=+1) stated?"),
    ("F02_definitions_koszul", "chapters/theory/chiral_koszul_pairs.tex", "Check every definition. Is 'Koszul pair' properly defined with hypotheses? Is 'Koszul locus' defined? Are the 10+1+1 equivalences properly enumerated with clear hypotheses?"),
    ("F03_definitions_shadow", "chapters/theory/higher_genus_modular_koszul.tex", "Check: is the shadow tower Theta_A formally defined? Are G/L/C/M classes defined before use? Is the MC equation stated as a definition before being invoked in proofs? Is the convolution algebra g^{E1} and g^{mod} defined?"),
    ("F04_definitions_complementarity", "chapters/theory/higher_genus_complementarity.tex", "Check: is complementarity (kappa+kappa'=K) defined? Is the center local system Z_A defined? Is the Lagrangian decomposition defined? Are all objects in C0/C1/C2 defined before the theorem statements?"),
    ("F05_definitions_en", "chapters/theory/en_koszul_duality.tex", "Check: is SC^{ch,top} properly defined (generators, relations)? Is topologization defined? Is 'inner conformal vector' defined? Are the five presentations of SC listed?"),
    ("F06_definitions_hochschild", "chapters/theory/chiral_hochschild_koszul.tex", "Check: is chiral Hochschild ChirHoch defined via End^{ch}_A (NOT via RHom_{A^e})? Is the Gerstenhaber bracket defined (both insertions, not just one)? Is the concentration claim in {0,1,2} precise (amplitude vs dimension)?"),
    ("F07_prerequisites_thm_A", "chapters/theory/chiral_koszul_pairs.tex", "For Theorem A: trace EVERY prerequisite lemma/proposition cited in the proof. Is each one (a) stated, (b) proved, (c) used with its hypotheses satisfied? List every missing or unproved prerequisite."),
    ("F08_prerequisites_thm_D", "chapters/theory/higher_genus_modular_koszul.tex", "For Theorem D: trace the FULL proof chain. Start from obs_g = kappa*lambda_g. What is cited? Is each cited result proved? Is there circularity (thm:genus-universality <-> thm:family-index)?"),
    ("F09_prerequisites_thm_H", "chapters/theory/chiral_hochschild_koszul.tex", "For Theorem H: trace every input. Is the bar-Hochschild complex properly defined? Is the spectral sequence from bar degree to Hochschild degree set up? Is concentration in {0,1,2} proved from the spectral sequence?"),
    ("F10_prerequisites_MC1_5", "chapters/theory/higher_genus_modular_koszul.tex", "For MC1-MC5: trace the dependency DAG. Which theorems depend on which? Is each dependency satisfied? Are there circular chains? List the complete DAG."),
    ("F11_hidden_imports_bar", "chapters/theory/bar_construction.tex", "Search for any result USED but not PROVED or CITED in this file. Look for 'by', 'from', 'via', 'using', 'follows from' — does the cited source exist and prove what's claimed?"),
    ("F12_hidden_imports_cobar", "chapters/theory/cobar_construction.tex", "Same: search for hidden imports. Every 'by Theorem X' — does X exist and prove what's needed?"),
    ("F13_hidden_imports_curved", "chapters/theory/bar_cobar_adjunction_curved.tex", "Same: search for hidden imports. Especially for the strong filtration, weight completion, and curved bar-cobar."),
    ("F14_hidden_imports_hg_found", "chapters/theory/higher_genus_foundations.tex", "Same: hidden imports. Especially for the genus-g fiber bar, spectral sequences, and base-change arguments."),
    ("F15_hidden_imports_hg_comp", "chapters/theory/higher_genus_complementarity.tex", "Same: hidden imports for C0/C1/C2 proofs."),
    ("F16_undefined_macros_v1", "standalone/", "Grep ALL standalone files for undefined LaTeX macros. Run: for f in standalone/*.tex; do grep -oP '\\\\[a-zA-Z]+' $f | sort -u; done — cross-check against preamble. Every undefined macro is a finding."),
    ("F17_dangling_refs_v1", "chapters/", "Find all \\ref{} that don't resolve. Run: grep -roh '\\\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix."),
    ("F18_dangling_refs_v2", "", "Same for Vol II. Find all \\ref{} that don't resolve in ~/chiral-bar-cobar-vol2/chapters/.", ),
    ("F19_dangling_refs_v3", "", "Same for Vol III. Find all \\ref{} that don't resolve in ~/calabi-yau-quantum-groups/chapters/."),
    ("F20_status_audit", "chapters/", "For EVERY \\ClaimStatusProvedHere in the manuscript: verify a \\begin{proof} follows within 50 lines. For every theorem/proposition WITHOUT a ClaimStatus tag: flag it. For every ClaimStatusConjectured in a theorem (not conjecture) env: flag AP40 violation."),
]

for fid, target, desc in FOUNDATION_CHECKS:
    agent(fid, f"""MISSION: FOUNDATION AUDIT of {target}

{desc}

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER C: COSMETIC & AESTHETIC AUDIT (20 agents)
# Prose quality. Notation consistency. Formatting. Presentation.
# ═══════════════════════════════════════════════════════════════════════════

CHAPTERS_FOR_COSMETIC = [
    "chapters/frame/preface.tex",
    "chapters/theory/introduction.tex",
    "chapters/frame/overture.tex",
    "chapters/theory/bar_construction.tex",
    "chapters/theory/cobar_construction.tex",
    "chapters/theory/chiral_koszul_pairs.tex",
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/theory/en_koszul_duality.tex",
    "chapters/examples/heisenberg.tex",
    "chapters/examples/kac_moody.tex",
    "chapters/examples/virasoro.tex",
    "chapters/examples/w_algebras.tex",
    "chapters/examples/free_fields.tex",
    "chapters/examples/lattice_foundations.tex",
    "chapters/connections/concordance.tex",
    "chapters/connections/bv_brst.tex",
    "chapters/theory/chiral_hochschild_koszul.tex",
    "chapters/theory/e1_modular_koszul.tex",
]

for i, chap in enumerate(CHAPTERS_FOR_COSMETIC):
    cid = f"C{i+1:02d}_{Path(chap).stem}"
    agent(cid, f"""MISSION: COSMETIC & AESTHETIC AUDIT of {chap}

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \\textbf, \\emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \\kappa without family?
   Any bare \\Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER D: UNFINISHED WORK AUDIT (15 agents)
# Stubs. TODOs. Incomplete proofs. Dangling forward references.
# ═══════════════════════════════════════════════════════════════════════════

UNFINISHED_CHECKS = [
    ("U01_todos_v1", VOL1, "Find ALL TODO, FIXME, HACK, XXX, RECTIFICATION-FLAG, PLACEHOLDER markers in chapters/, appendices/, standalone/. For each: state what's unfinished and what the fix should be."),
    ("U02_todos_v2", VOL2, "Same for Vol II: find all TODO/FIXME/HACK/XXX/RECTIFICATION-FLAG markers."),
    ("U03_todos_v3", VOL3, "Same for Vol III."),
    ("U04_stub_chapters_v1", VOL1, "Find chapters that are <100 lines or have no \\begin{theorem}/\\begin{proposition}. These are stubs (AP114). For each: should it be developed, merged, or removed?"),
    ("U05_stub_chapters_v3", VOL3, "Same for Vol III. Check which of the 12 stub chapters have been developed and which are still thin."),
    ("U06_incomplete_proofs_v1", VOL1, "Find all \\begin{proof} that end with '...' or 'TO BE COMPLETED' or are <5 lines for a complex theorem. Also find ProvedHere tags without a following proof block."),
    ("U07_forward_refs_v1", VOL1, "Find all forward references: \\ref{} to labels that appear LATER in the file or in a later chapter. Are these genuine forward refs or dangling? For dangling: provide the fix."),
    ("U08_empty_sections", VOL1, "Find \\section{} or \\subsection{} with <3 lines of content. These are empty placeholders. For each: fill or remove."),
    ("U09_missing_examples", VOL1, "For each main theorem (A-D, H, MC1-5): is there at least ONE worked example? If a theorem has no example: flag it and suggest which family to use."),
    ("U10_missing_computations", VOL1, "For each formula in the census (C1-C31 in CLAUDE.md): is there a compute engine in compute/lib/ that verifies it? For each missing engine: flag it."),
    ("U11_test_gaps", VOL1, "Find compute engines (compute/lib/*.py) without matching test files (compute/tests/test_*.py). Each missing test is a finding."),
    ("U12_test_gaps_v3", VOL3, "Same for Vol III compute/lib/ vs compute/tests/."),
    ("U13_dead_labels", VOL1, "Find all \\label{} that are never \\ref{}'d anywhere. These are dead labels. For each: is the labeled object still needed? If not, flag for removal."),
    ("U14_orphaned_chapters", VOL1, "Check main.tex for \\input{} commands. Are all chapter files \\input'd? Are there .tex files in chapters/ NOT in the \\input graph? These are orphaned."),
    ("U15_build_warnings", VOL1, "Read main.log for LaTeX warnings: undefined references, multiply-defined labels, overfull/underfull boxes, missing citations. Each warning is a finding with fix."),
]

for uid, cwd, desc in UNFINISHED_CHECKS:
    agent(uid, f"""MISSION: UNFINISHED WORK AUDIT.

{desc}

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).""", cwd=cwd)


# ═══════════════════════════════════════════════════════════════════════════
# TIER E: DEEPENED ANTI-PATTERN SWEEP (15 agents)
# Patterns that survive surface-level review.
# ═══════════════════════════════════════════════════════════════════════════

DEEP_AP_CHECKS = [
    ("D01_circular_proofs", "Find ALL circular proof chains in chapters/theory/. A circular chain is: Theorem X cites Theorem Y, and Theorem Y (directly or transitively) cites Theorem X. Use grep to trace \\ref{thm:} chains. For each cycle: identify the primitive non-circular anchor."),
    ("D02_scope_inflation", "Find ALL theorems that claim 'for all g' or 'for all families' but whose proofs only cover specific cases. Grep for 'for all', 'every', 'any' in theorem environments. For each: verify the proof matches the scope."),
    ("D03_biconditional_drift", "Find ALL \\iff or 'if and only if' in theorem environments (AP36). For each: is the converse actually proved? If only forward direction is proved: flag and provide fix (change to \\implies)."),
    ("D04_kappa_drift", "Find EVERY instance of \\kappa in chapters/theory/ and chapters/examples/. For each: (a) is the family specified? (b) is the formula correct? (c) is it consistent with landscape_census.tex? Focus on instances where bare kappa could mean different things."),
    ("D05_rmatrix_level", "Find EVERY r-matrix formula (r(z), r_{ij}, Omega/z) in ALL three volumes. For each: is the level prefix present? Does k=0 give r=0 (trace-form)? Cross-check conventions."),
    ("D06_desuspension_direction", "Find EVERY instance of s^{-1} or desuspension in the manuscript. For each: is the grading correct (|s^{-1}v|=|v|-1, NOT +1)? Any bare s (not s^{-1}) in bar complex formulas?"),
    ("D07_augmentation_ideal", "Find EVERY instance of bar complex definition (T^c, B(A)) in the manuscript. For each: does it use A-bar = ker(epsilon), NOT bare A? (AP132)"),
    ("D08_curved_vs_flat", "Find EVERY instance of d^2 in the manuscript. For each: is it clear whether d^2=0 (flat/bar) or d^2=kappa*omega_g (curved/fiber)? Any place where ordinary cohomology is applied to a curved complex?"),
    ("D09_five_objects_discipline", "Search for paragraphs that mention both 'bar' and 'Koszul dual' or 'derived center'. For each: are all five objects (A, B(A), A^i, A^!, Z^der) correctly distinguished? Any conflation?"),
    ("D10_E1_vs_Einf", "Find EVERY E_1 or E_inf claim in the manuscript. For each: is the locality hierarchy correct? (All standard VAs are E_inf; E_1 = nonlocal). Any 'E_inf means no OPE poles' (WRONG)?"),
    ("D11_SC_discipline", "Find EVERY mention of SC^{ch,top} or Swiss-cheese. For each: (a) is it attributed to the derived center pair (correct) not B(A) (wrong)? (b) is it not claimed self-dual? (c) is topologization properly scoped?"),
    ("D12_hochschild_disambiguation", "Find EVERY 'Hochschild' in the manuscript. For each: is it qualified (chiral/topological/categorical)? Any bare 'Hochschild' that could mean different things?"),
    ("D13_genus_1_vs_all", "Find EVERY obs_g or F_g formula. For each: is it tagged (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta)? Any untagged formulas (AP32)?"),
    ("D14_proof_after_conj", "Find EVERY \\begin{proof} in the manuscript. For each: what is the nearest preceding theorem-like environment? If it's a conjecture/heuristic/remark/definition: flag AP4 violation."),
    ("D15_hardcoded_parts", "Find EVERY Part~, Chapter~, Section~ with hardcoded numbers (not \\ref). Each is a finding. Also check for stale cross-volume Part references."),
]

for did, desc in DEEP_AP_CHECKS:
    agent(did, f"""MISSION: DEEP ANTI-PATTERN SWEEP.

{desc}

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER F: CROSS-VOLUME BRIDGE AUDIT (20 agents)
# Every bridge claim between volumes. Convention conversion.
# Status synchronization.
# ═══════════════════════════════════════════════════════════════════════════

BRIDGE_CHECKS = [
    ("B01_thm_A_bridge", "How is Theorem A cited in Vol II and Vol III? Search for 'Theorem A' and 'bar-cobar adjunction' in all three repos. Is the citation accurate? Is the scope correct?"),
    ("B02_thm_B_bridge", "Same for Theorem B. Is 'bar-cobar inversion on Koszul locus' correctly cited in Vol II/III?"),
    ("B03_thm_C_bridge", "Same for Theorem C (all parts). Is complementarity correctly cited? Is C2 conditional status propagated?"),
    ("B04_thm_D_bridge", "Same for Theorem D. Is obs_g=kappa*lambda_g correctly cited with uniform-weight tag?"),
    ("B05_thm_H_bridge", "Same for Theorem H. Is ChirHoch concentration {0,1,2} correctly cited? Not confused with vdim?"),
    ("B06_MC_bridge", "Same for MC1-MC5. Are the MC theorem statuses correctly cited? Is MC5 chain-level conjectural status propagated?"),
    ("B07_kappa_bridge", "Search for kappa in Vol II and Vol III. For each: (a) correct formula for the family? (b) Vol III has subscript (AP113)? (c) consistent with Vol I census?"),
    ("B08_rmatrix_bridge", "Search for r-matrix formulas in Vol II and Vol III. For each: (a) level prefix present? (b) convention (trace-form vs KZ) consistent? (c) bridge identity stated?"),
    ("B09_SC_bridge", "How is SC^{ch,top} described in Vol II? Is it on the derived center pair (correct) or B(A) (wrong AP165)? Is SC^! = (Lie,Ass) correctly stated? Is topologization scope correct?"),
    ("B10_E3_bridge", "How is E_3 described in Vol II? Is it E_3-TOPOLOGICAL (correct) or E_3-chiral (wrong AP168)? Is the conformal vector hypothesis present? Is scope (affine KM only) correct?"),
    ("B11_convention_v1_v2", "Find formulas that appear in BOTH Vol I and Vol II. For each: is the convention conversion correct? OPE modes (Vol I) vs lambda-brackets (Vol II). Check c/2 vs c/12 divided power."),
    ("B12_convention_v1_v3", "Find formulas in both Vol I and Vol III. Is convention conversion correct? Chiral vs motivic conventions."),
    ("B13_E1_hierarchy_v2", "Check V2-AP1 through V2-AP24 discipline in Vol II. Is the E_1/E_inf hierarchy maintained? Any 'VAs are not E_inf' (WRONG V2-AP1)?"),
    ("B14_cy_claims_v3", "Check CY-to-chiral functor claims in Vol III against Vol I. Is CY-A only proved for d=2? Are d=3 claims properly conditioned? Are unconstructed objects marked?"),
    ("B15_status_sync_v1_v2", "Compare theorem status tables: Vol I CLAUDE.md vs Vol II CLAUDE.md. Any disagreements? Any stale statuses?"),
    ("B16_status_sync_v1_v3", "Compare theorem status: Vol I vs Vol III. Are Vol I results correctly cited in Vol III?"),
    ("B17_label_collisions", "Find duplicate labels across all three volumes. grep -roh '\\\\label{[^}]*}' from all three repos, sort, find duplicates. Each duplicate is a finding."),
    ("B18_bibliography_sync", "Check bibliographies across volumes. Are the same papers cited consistently? Any [?] in compile logs from undefined citations?"),
    ("B19_notation_sync", "Check key notation across volumes: B(A), A^!, Z^der, kappa, Theta_A, r(z), SC^{ch,top}. Any notation drift between volumes?"),
    ("B20_readme_sync", "Check READMEs across all three volumes. Page counts accurate? Theorem counts accurate? Test counts accurate? No scope inflation?"),
]

for bid, desc in BRIDGE_CHECKS:
    agent(bid, f"""MISSION: CROSS-VOLUME BRIDGE AUDIT.

{desc}

Search across all three repos:
- ~/chiral-bar-cobar/
- ~/chiral-bar-cobar-vol2/
- ~/calabi-yau-quantum-groups/

For each finding: exact file:line in EACH volume, PROBLEM, and EXACT FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER G: PER-CHAPTER DEEP AUDIT — Vol I (30 agents)
# One agent per major chapter. Complete read + adversarial report.
# ═══════════════════════════════════════════════════════════════════════════

V1_CHAPTERS = [
    "chapters/theory/bar_construction.tex",
    "chapters/theory/cobar_construction.tex",
    "chapters/theory/bar_cobar_adjunction_inversion.tex",
    "chapters/theory/bar_cobar_adjunction_curved.tex",
    "chapters/theory/chiral_koszul_pairs.tex",
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/theory/en_koszul_duality.tex",
    "chapters/theory/chiral_hochschild_koszul.tex",
    "chapters/theory/e1_modular_koszul.tex",
    "chapters/theory/nilpotent_completion.tex",
    "chapters/theory/ordered_chiral_koszul.tex",
    "chapters/theory/coderived_models.tex",
    "chapters/theory/chiral_center_theorem.tex",
    "chapters/theory/algebraic_foundations.tex",
    "chapters/examples/heisenberg.tex",
    "chapters/examples/kac_moody.tex",
    "chapters/examples/virasoro.tex",
    "chapters/examples/w_algebras.tex",
    "chapters/examples/free_fields.tex",
    "chapters/examples/lattice_foundations.tex",
    "chapters/examples/beta_gamma.tex",
    "chapters/examples/bershadsky_polyakov.tex",
    "chapters/examples/yangians_computations.tex",
    "chapters/examples/landscape_census.tex",
    "chapters/connections/bv_brst.tex",
    "chapters/connections/concordance.tex",
    "chapters/frame/preface.tex",
    "chapters/theory/introduction.tex",
]

for i, ch in enumerate(V1_CHAPTERS):
    stem = Path(ch).stem
    agent(f"G{i+1:02d}_{stem}", f"""MISSION: COMPLETE DEEP AUDIT of {ch}

Read the ENTIRE file. For every theorem, proposition, lemma, definition, and proof:

1. Is the statement precise? Are all variables quantified? Is scope explicit?
2. Does the proof actually prove the stated claim? Any gaps?
3. Are all cited results (a) stated, (b) proved, (c) used with correct hypotheses?
4. Are all objects defined before use?
5. Is the notation consistent with the rest of the manuscript?
6. Are there hidden assumptions not in the theorem statement?
7. Does the E1-first architecture hold (ordered before symmetric)?
8. Are kappa, r-matrix, bar complex formulas correct (check against census)?
9. Are ClaimStatus tags accurate?
10. Any AI slop, em dashes, or markdown in LaTeX?
11. Any scope inflation, biconditional drift, or status inflation?
12. Any conflation of the five objects (A, B(A), A^i, A^!, Z^der)?

Be MAXIMALLY harsh. This is the STRONGEST possible audit. For each finding: PROBLEM + FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER H: PER-CHAPTER DEEP AUDIT — Vol II (20 agents)
# ═══════════════════════════════════════════════════════════════════════════

V2_CHAPTERS = [
    "chapters/theory/bar-cobar-review.tex",
    "chapters/theory/factorisation_swiss_cheese.tex",
    "chapters/theory/foundations.tex",
    "chapters/theory/axioms.tex",
    "chapters/theory/equivalence.tex",
    "chapters/theory/line-operators.tex",
    "chapters/theory/ordered_associative_chiral_kd_core.tex",
    "chapters/theory/hochschild.tex",
    "chapters/theory/3d_gravity.tex",
    "chapters/connections/spectral-braiding-core.tex",
    "chapters/connections/ht_bulk_boundary_line_core.tex",
    "chapters/connections/thqg_holographic_reconstruction.tex",
    "chapters/connections/thqg_gravitational_complexity.tex",
    "chapters/connections/thqg_soft_graviton_theorems.tex",
    "chapters/connections/thqg_perturbative_finiteness.tex",
    "chapters/connections/celestial_holography_core.tex",
    "chapters/examples/rosetta_stone.tex",
    "chapters/examples/w-algebras-virasoro.tex",
    "chapters/frame/preface.tex",
    "chapters/theory/introduction.tex",
]

for i, ch in enumerate(V2_CHAPTERS):
    stem = Path(ch).stem
    agent(f"H{i+1:02d}_{stem}", f"""MISSION: COMPLETE DEEP AUDIT of {ch}

Read the ENTIRE file. Audit for ALL of the following:

1. Mathematical correctness: every theorem, proof, formula
2. E_1/E_inf hierarchy (V2-AP1-AP24): any "VAs are not E_inf" (WRONG)?
3. SC^{{ch,top}} discipline: on derived center pair, NOT on B(A)?
4. Lambda-bracket convention: divided powers correct (c/12 not c/2)?
5. Bar complex: E_1 coassociative coalgebra, NOT SC-coalgebra?
6. Topologization scope: only affine KM proved?
7. E_3 is TOPOLOGICAL, not chiral?
8. Chapter opening: deficiency opening, not "In this chapter..."?
9. AI slop, em dashes, markdown in LaTeX?
10. Hardcoded Part numbers (should be \\ref)?
11. Objects defined before use?
12. Cross-references resolve?

For each finding: PROBLEM + exact FIX.""", cwd=VOL2)


# ═══════════════════════════════════════════════════════════════════════════
# TIER I: PER-CHAPTER DEEP AUDIT — Vol III (10 agents)
# ═══════════════════════════════════════════════════════════════════════════

V3_CHAPTERS = [
    "chapters/theory/cy_to_chiral.tex",
    "chapters/theory/fukaya_categories.tex",
    "chapters/theory/e_n_factorization.tex",
    "chapters/theory/e1_chiral_algebras.tex",
    "chapters/theory/bar_cobar_bridge.tex",
    "chapters/theory/introduction.tex",
    "chapters/examples/toric_cy3_coha.tex",
    "chapters/examples/k3_times_e.tex",
    "chapters/examples/toroidal_elliptic.tex",
    "chapters/connections/cy_holographic_datum_master.tex",
]

for i, ch in enumerate(V3_CHAPTERS):
    stem = Path(ch).stem
    agent(f"I{i+1:02d}_{stem}", f"""MISSION: COMPLETE DEEP AUDIT of {ch}

Read the ENTIRE file. Audit for ALL of the following:

1. Mathematical correctness: every theorem, proof, formula
2. CY-to-chiral functor: is CY-A only proved for d=2? d=3 conditioned?
3. Bare kappa FORBIDDEN (AP113): must be kappa_ch/cat/BKM/fiber
4. pi_3(BU)=0 (NOT Z): any Bott periodicity errors?
5. kappa_ch = chi(S)/2: only for local surfaces Tot(K_S -> S)?
6. CoHA is NOT automatically E_1-chiral (AP-CY7)
7. Borcherds denominator != bar Euler product automatically (AP-CY8)
8. Drinfeld center != derived center unless hypotheses stated
9. Objects defined before use? Unconstructed d=3 objects marked?
10. AI slop, em dashes, markdown?
11. ClaimStatus accurate?
12. Cross-volume claims match Vol I/II actual theorems?

For each finding: PROBLEM + exact FIX.""", cwd=VOL3)


# ═══════════════════════════════════════════════════════════════════════════
# TIER J: COMPUTE ENGINE DEEP AUDIT (25 agents)
# ═══════════════════════════════════════════════════════════════════════════

import glob
ENGINE_DIRS = [
    (VOL1, "shadow"),
    (VOL1, "koszul"),
    (VOL1, "central_charge"),
    (VOL1, "r_matrix"),
    (VOL1, "bar_cohom"),
    (VOL1, "complementarity"),
    (VOL1, "ghost"),
    (VOL1, "ds_"),
    (VOL1, "stokes"),
    (VOL1, "gerstenhaber"),
    (VOL1, "categorical_zeta"),
    (VOL1, "modular_cy"),
    (VOL1, "w_algebra"),
    (VOL1, "yangian"),
    (VOL1, "genus"),
    (VOL1, "hilbert"),
    (VOL1, "partition"),
    (VOL1, "lattice"),
    (VOL1, "sc_koszul"),
    (VOL1, "depth"),
    (VOL3, "bar_euler"),
    (VOL3, "dolbeault"),
    (VOL3, "modular_cy"),
    (VOL3, "swiss_cheese"),
    (VOL3, "e1_refined"),
]

for i, (vol, pattern) in enumerate(ENGINE_DIRS):
    agent(f"J{i+1:02d}_engine_{pattern}", f"""MISSION: DEEP AUDIT of compute engines matching '{pattern}' in {vol}

1. Find all engine files: ls {vol}/compute/lib/*{pattern}*.py
2. Find matching test files: ls {vol}/compute/tests/test_*{pattern}*.py
3. For each engine:
   a. Read the engine code. Is the formula correct?
   b. Check against the canonical census (landscape_census.tex or CLAUDE.md)
   c. Read the test file. Are expected values independently verified (AP10/AP128)?
   d. Do expected values have '# VERIFIED' comments with 2+ sources?
   e. Run the tests: cd {vol} && python3 -m pytest compute/tests/test_*{pattern}*.py -v --tb=short 2>&1 | tail -30
   f. Any engine without a matching test file? (AP80)
   g. Any hardcoded value that could be wrong?

For each finding: PROBLEM + exact FIX.""", cwd=vol)


# ═══════════════════════════════════════════════════════════════════════════
# TIER K: CONVENTION CONSISTENCY PER FAMILY (15 agents)
# ═══════════════════════════════════════════════════════════════════════════

FAMILIES = [
    ("K01_heisenberg", "Heisenberg H_k", "kappa=k, r(z)=k/z, c=1 at k=1, class G, SC-formal, abelian KM"),
    ("K02_affine_km", "Affine KM V_k(g)", "kappa=dim(g)(k+h^v)/(2h^v), r(z)=k*Omega/z [trace-form], class L, k=0→dim(g)/2, k=-h^v→0 critical"),
    ("K03_virasoro", "Virasoro Vir_c", "kappa=c/2, r(z)=(c/2)/z^3+2T/z, class M, self-dual c=13, K(Vir)=13"),
    ("K04_w_algebras", "W_N algebras", "kappa=c*(H_N-1), H_N=sum 1/j, class M, W_2=Vir, generators at weights {2,...,N}"),
    ("K05_free_fields_bc", "bc ghost system", "c_bc=1-3(2lambda-1)^2, lambda=2→-26, class varies"),
    ("K06_free_fields_bg", "betagamma system", "c_bg=2(6lambda^2-6lambda+1), lambda=2→+26, c_bc+c_bg=0, class C"),
    ("K07_bershadsky_polyakov", "Bershadsky-Polyakov", "K_BP=196, self-dual k=-3, kappa+kappa'=98/3"),
    ("K08_lattice_voa", "Lattice VOAs", "class G, kappa=rank/2 (?), SC-formal"),
    ("K09_yangian", "Yangians Y_hbar(g)", "E_1-chiral (genuinely nonlocal), R-matrix independent, four types (classical/dg/chiral/spectral)"),
    ("K10_e8", "E_8 family", "adjoint=248, fundamental dims specific, NOT 779247"),
    ("K11_svir", "Super Virasoro", "kappa=(3c-2)/4, distinct from Vir kappa=c/2"),
    ("K12_sl2", "sl_2 computations", "dim=3, h^v=2, kappa=3(k+2)/4, bar H^2=5 (NOT 6)"),
    ("K13_monster", "Monster V-natural", "kappa open/estimate (AP48), c=24"),
    ("K14_k3_times_e", "K3 x E", "kappa_ch=3, kappa_BKM=5 (distinct), conifold kappa=1 but derivation needs care"),
    ("K15_coset_models", "Coset/DS models", "ghost charge includes background charge (AP143), W_{N,f} from sl_N"),
]

for kid, family, canonical in FAMILIES:
    agent(kid, f"""MISSION: CONVENTION CONSISTENCY AUDIT for {family}.

CANONICAL DATA: {canonical}

Search ALL .tex files across all three volumes for mentions of this family.
For EACH mention:
1. Is the kappa formula correct?
2. Is the r-matrix correct (with level prefix)?
3. Is the classification (G/L/C/M) correct?
4. Are boundary values correct?
5. Are convention conversions between volumes correct?
6. Is the family name/notation consistent?

Be EXHAUSTIVE. Cross-check every instance against the canonical data above.
For each discrepancy: PROBLEM + exact FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER L: PROOF CHAIN VERIFICATION (15 agents)
# ═══════════════════════════════════════════════════════════════════════════

PROOF_CHAINS = [
    ("L01_thmA_chain", "Trace Theorem A proof chain end-to-end. Start from thm:bar-cobar-adjunction. Follow EVERY cited result. For each: exists? proved? hypotheses satisfied? Flag any missing node or circularity."),
    ("L02_thmB_chain", "Trace Theorem B chain. thm:bar-cobar-inversion through bar_cobar_adjunction_inversion.tex. On-locus vs off-locus separate. Flag circularity with coderived_models.tex."),
    ("L03_thmC_chain", "Trace Theorem C (C0/C1/C2) chain through higher_genus_complementarity.tex + higher_genus_foundations.tex. Map every dependency. Flag curved-vs-flat issues."),
    ("L04_thmD_chain", "Trace Theorem D chain: obs_g=kappa*lambda_g. Follow thm:genus-universality, thm:family-index. CHECK FOR CIRCULARITY. Map the non-circular anchor."),
    ("L05_thmH_chain", "Trace Theorem H chain through chiral_hochschild_koszul.tex. Check bar-coalgebra/Koszul-dual identification. Check configuration space collapse."),
    ("L06_MC1_chain", "Trace MC1 (PBW) chain. Check Whitehead justification. Check enrichment-class control."),
    ("L07_MC2_chain", "Trace MC2 chain through higher_genus_modular_koszul.tex AND e1_modular_koszul.tex. g^{E1} vs g^{mod} correctly attributed?"),
    ("L08_MC3_chain", "Trace MC3 chain through yangians_computations.tex. Baxter constraint at lambda=0. Finite-dim to completed extension."),
    ("L09_MC4_chain", "Trace MC4 chain. Strong filtration inequality. Resonance lane. Transfer theorem."),
    ("L10_MC5_chain", "Trace MC5 chain through bv_brst.tex. Class-M mechanism. Coderived category usage."),
    ("L11_topol_chain", "Trace topologization chain. Chain-level vs cohomological. Sugawara at each step."),
    ("L12_koszul_web", "Trace ALL 10+1+1 Koszul equivalences. Draw the implication web. Are both directions proved for each? Which are truly unconditional?"),
    ("L13_SC_formal", "Trace SC-formality: iff class G. Both directions. Class-G membership for all claimed members."),
    ("L14_depth_gap", "Trace depth gap: {0,1,2,inf}. Each realized value. Impossibility of 3. All witnesses."),
    ("L15_D2_chain", "Trace D^2=0 chain. Convolution and ambient cases. Which spaces. Log FM definition."),
]

for lid, desc in PROOF_CHAINS:
    agent(lid, f"""MISSION: PROOF CHAIN VERIFICATION.
{desc}
For each node: [PROVED/CITED/MISSING/CIRCULAR]. Draw DAG. For every gap: PROBLEM + FIX.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER M: MISSING CONTENT (15 agents)
# ═══════════════════════════════════════════════════════════════════════════

MISSING = [
    ("M01_examples_thms", "For EACH of A-D,H: is there a fully worked example for a specific family? If not: which family and what should the example contain?"),
    ("M02_examples_MC", "For MC1-MC5: worked verification for at least one family? sl_2 explicit?"),
    ("M03_comparisons", "For each main theorem: comparison with BD, FG, CG, Lurie? Missing attributions?"),
    ("M04_counterexamples", "For each conditional theorem (C2, MC5 chain, topol general): explicit obstruction showing WHY the condition is needed?"),
    ("M05_diagrams", "Commutative diagrams for bar-cobar adjunction, Verdier, Koszul? Essential for 4-functor discipline."),
    ("M06_summary_tables", "Master table of ALL families: kappa, r-matrix, class, depth, K? Is landscape_census.tex complete?"),
    ("M07_genus1", "Dedicated genus-1 treatment: F_1=kappa/24, E_2*/E_4/E_6, modular group action?"),
    ("M08_genus2", "Explicit genus-2: 7 stable graphs, 2x2 period matrix, first multi-variable delta_F_g^cross?"),
    ("M09_E1_worked", "Complete B^ord example for non-abelian family (KM or Yangian)?"),
    ("M10_SC_presentation", "SC^{ch,top} generators-and-relations? All 5 presentations? Pentagon equivalences?"),
    ("M11_topol_example", "Worked topologization: V_k(g) Sugawara -> E_3-topological?"),
    ("M12_class_C", "Class C (betagamma): shadow tower fully computed? Quartic contact invariant exhibited?"),
    ("M13_frontier_status", "Each CONJECTURAL claim: known/conjectured/evidence clearly separated?"),
    ("M14_error_bounds", "Numerical computations: exact arithmetic or error bounds specified?"),
    ("M15_indices", "Notation index? Theorem index? Formula index? Standard for 2,650pp treatise."),
]

for mid, desc in MISSING:
    agent(mid, f"""MISSION: MISSING CONTENT AUDIT.
{desc}
Search the manuscript. If exists: report where, whether complete. If MISSING: PROBLEM + what the FIX should contain.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER N: ELEGANCE & CLARITY (10 agents)
# ═══════════════════════════════════════════════════════════════════════════

ELEGANCE = [
    ("N01_bar", "chapters/theory/bar_construction.tex — Maximum clarity? E1-first? Inevitability (Gelfand)?"),
    ("N02_koszul", "chapters/theory/chiral_koszul_pairs.tex — 10+1+1 equivalences compressed (Kazhdan)? Redundancy?"),
    ("N03_shadow", "chapters/theory/higher_genus_modular_koszul.tex — Shadow tower inevitable? Theta_A from necessity? G/L/C/M as dichotomy?"),
    ("N04_preface", "chapters/frame/preface.tex — Symphonic standard? All voices? Orients 2,650 pages?"),
    ("N05_intro", "chapters/theory/introduction.tex — Five theorems inevitable? Or lists results?"),
    ("N06_overture", "chapters/frame/overture.tex — Heisenberg CG deficiency opening? Instant computation? Forced transition?"),
    ("N07_complementarity", "chapters/theory/higher_genus_complementarity.tex — Structural theorem, not computational accident?"),
    ("N08_examples", "chapters/examples/ — Organic parts of theory or afterthought appendices?"),
    ("N09_concordance", "chapters/connections/concordance.tex — Complete constitution? Every theorem, status, bridge?"),
    ("N10_en_koszul", "chapters/theory/en_koszul_duality.tex — SC/E_3 story clear? Topologization mechanism transparent?"),
]

for nid, desc in ELEGANCE:
    agent(nid, f"""MISSION: ELEGANCE & CLARITY AUDIT.
{desc}
Read with Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity).
For each weakness: [HIGH/MEDIUM/LOW] + PROBLEM + specific REWRITE suggestion.""")


# ═══════════════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Adversarial Wave 2")
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()

    print(f"Wave 2: {len(AGENTS)} agents → {OUT}")
    print(f"Tiers: {sum(1 for a in AGENTS if a['id'].startswith('S'))} seam, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('F'))} foundation, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('C'))} cosmetic, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('U'))} unfinished, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('D'))} deep-AP, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('B'))} bridge")
    print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s\n")

    ok, fail = 0, 0
    results = []
    for i in range(0, len(AGENTS), args.batch_size):
        batch = AGENTS[i:i + args.batch_size]
        bn = i // args.batch_size + 1
        tb = (len(AGENTS) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")
        with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
            futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(AGENTS)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")

    summary = [f"# Wave 2 Summary — {TS}\n", f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
