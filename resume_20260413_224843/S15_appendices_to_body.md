# S15_appendices_to_body (1113s)

- [HIGH] main.tex:1010 — PROBLEM: `appendices/homotopy_transfer.tex` (1010), `appendices/nonlinear_modular_shadows.tex` (1112), `appendices/branch_line_reductions.tex` (1116), and `appendices/combinatorial_frontier.tex` (1374) are loaded before `\appendix` at `main.tex:1588`, so the live build treats them as body chapters, but theory and those files still cite/described them as appendices: `chapters/theory/higher_genus_foundations.tex:1635`, `chapters/theory/quantum_corrections.tex:360,525`, `chapters/theory/chiral_modules.tex:2672`, `chapters/theory/chiral_hochschild_koszul.tex:3143,3175,6021,6053`, `chapters/theory/higher_genus_complementarity.tex:98`, `chapters/theory/higher_genus_modular_koszul.tex:4455,4990,10286,12438,12477,13369,15619,15633,29926,31269`, `chapters/theory/introduction.tex:1962`, `chapters/theory/chiral_koszul_pairs.tex:1116`, `appendices/combinatorial_frontier.tex:334`, plus self-descriptions at `appendices/branch_line_reductions.tex:28,57,141` and `appendices/nonlinear_modular_shadows.tex:2495,3136,3162,3175`. FIX: keep these four files before `\appendix`, rename their head labels to chapter labels (`chap:homotopy-transfer`, `chap:nonlinear-modular-shadows`, `chap:branch-line-reductions`, `chap:combinatorial-frontier`), replace every listed `Appendix~\ref{app:...}` with `Chapter~\ref{chap:...}`, and change the listed internal nouns `appendix` to `chapter`.

- [HIGH] chapters/theory/algebraic_foundations.tex:116 — PROBLEM: the body definition of the bar construction depends on `Definition~\ref{def:bar-complex-algebraic}`, but that label exists only in `appendices/notation_index.tex:342-344`, where the “definition” is just “The algebraic bar complex is represented by the DG coalgebra model of Theorem~\ref{thm:bar-coalgebra}.” This is circular appendix→theory routing and the appendix entry is not a real definition. FIX: insert a real body definition at `chapters/theory/algebraic_foundations.tex:116`, e.g. `\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic} For an augmented algebra A with augmentation ideal \bar A, define B_{\mathrm{alg}}(A)=T^c(s^{-1}\bar A) with the standard bar differential induced by multiplication in A. \end{definition}`, then rewrite `appendices/notation_index.tex:342-344` to `The algebraic bar complex is Definition~\ref{def:bar-complex-algebraic}.`

- [MEDIUM] appendices/general_relations.tex:101 — PROBLEM: the curved `A_\infty` appendix switches curvature notation to `\mu_0` in the exact package cited from theory, while the live theory and the sign appendix use `m_0` consistently (`chapters/theory/higher_genus_foundations.tex:1926-1928`, `appendices/signs_and_shifts.tex:1311-1312,1545-1547`). The seam is therefore not notation-stable. FIX: replace `\mu_0` by `m_0` throughout `appendices/general_relations.tex:101-126`, so the opening reads `(\mathcal A,\{m_k\}_{k\ge0})`, and the formulas become `m_1(m_0)=0`, `m_1^2(a)=m_2(m_0,a)-m_2(a,m_0)`, etc.

- [LOW] chapters/theory/en_koszul_duality.tex:508 — PROBLEM: the proof of `thm:e2-d-squared` cites `Corollary~\ref{cor:bar-d-squared-zero-arnold}` as the chiral prototype, but that appendix corollary immediately defers its proof to `Theorem~\ref{thm:bar-nilpotency-complete}` at `appendices/arnold_relations.tex:168-169`. The body is citing a wrapper, not the actual source theorem. FIX: change `chapters/theory/en_koszul_duality.tex:508-510` to cite `Theorem~\ref{thm:bar-nilpotency-complete}` directly.

- [LOW] appendices/ordered_associative_chiral_kd.tex:37 — PROBLEM: this dormant appendix mirror is not included in `main.tex`, but it still duplicates `311` labels from `chapters/theory/ordered_associative_chiral_kd.tex` starting with the chapter label at line 37. The seam is therefore grep-fragile: source ownership is ambiguous even before any future inclusion. FIX: mark the file as dormant and rename all duplicated labels with a dormant prefix starting at line 37 (for example `ch:ordered-associative-chiral-kd` -> `oldapp:ordered-associative-chiral-kd`), or move the file out of `appendices/` so it cannot be mistaken for a live seam source.

## Summary
Checked: 311 | Findings: 5 | Verdict: FAIL


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
session id: 019d889a-9002-7431-aabe-86a816708952
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


MISSION: SEAM AUDIT between appendices/ and chapters/theory/.

Appendices→Theory. Check: (a) appendix results cited correctly in body, (b) no circular dependencies, (c) notation consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers
codex
I’m auditing the `appendices/` ↔ `chapters/theory/` seam as a hostile reader. I’ll first load the required repo-wide invariants and map every appendix/theory cross-reference before checking citation accuracy, dependency direction, and notation drift.
exec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'raeeznotes/raeeznotes100/red_team_summary.md' -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md' -g '.agents/skills/deep-beilinson-audit/SKILL.md' -g 'appendices/**' -g 'chapters/theory/**'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/concordance.tex
chapters/theory/three_invariants.aux
chapters/theory/existence_criteria.tex
chapters/theory/chiral_center_theorem.tex
chapters/theory/ordered_associative_chiral_kd.tex
chapters/theory/higher_genus_complementarity.tex
chapters/theory/higher_genus_modular_koszul.tex
chapters/theory/quantum_corrections.tex
chapters/theory/fourier_seed.tex
chapters/theory/poincare_duality_quantum.tex
chapters/theory/en_koszul_duality.tex
chapters/theory/koszul_pair_structure.aux
chapters/theory/bar_cobar_adjunction_inversion.tex
chapters/theory/bar_cobar_adjunction_curved.tex
chapters/theory/poincare_duality.tex
chapters/theory/filtered_curved.tex
chapters/theory/higher_genus_foundations.tex
collab spawn_agent(call_flv1Fcc6qzqINECBglIm00AK, prompt="Map the seam between appendices/ and chapters/theory/ in /Users/raeez/chiral-bar-cobar. Identify all files under appendi…")
spawn_agent(call_flv1Fcc6qzqINECBglIm00AK, prompt="Map the seam between appendices/ and chapters/theory/ in /Users/raeez/chiral-bar-cobar. Identify all files under appendi…") pending init:
  agent: 019d889a-cd25-7953-a496-cfc7698bf6e2
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'rg --files appendices chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex
chapters/theory/quantum_corrections.tex
chapters/theory/fourier_seed.tex
chapters/theory/poincare_duality_quantum.tex
chapters/theory/en_koszul_duality.tex
chapters/theory/bar_cobar_adjunction_inversion.tex
chapters/theory/bar_cobar_adjunction_curved.tex
chapters/theory/poincare_duality.tex
chapters/theory/filtered_curved.tex
chapters/theory/higher_genus_foundations.tex
chapters/theory/computational_methods.tex
chapters/theory/chiral_koszul_pairs.tex
chapters/theory/bar_cobar_adjunction.tex
chapters/theory/introduction.tex
chapters/theory/nilpotent_completion.tex
chapters/theory/cobar_construction.tex
chapters/theory/hochschild_cohomology.tex
chapters/theory/three_invariants.tex
chapters/theory/bar_construction.tex
chapters/theory/coderived_models.tex
codex
I’ve mapped the candidate files. Next I’m reading the repo’s governing surfaces and the audit skill, then I’ll enumerate every appendix/theory cross-reference and inspect the seam points in context rather than grep-only.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Designing cross-reference mapping script**

I’m planning a Python script to collect all LaTeX label definitions and cross-references between chapters and appendices by scanning files for macros like \label and \ref variants. I want to identify references crossing directories and note any circular referencing patterns, aiming to produce a clear inventory linking files and labels for both directions.

thinking
**Planning cross-references**

I think I might not need to use subagents since the skill indicates they're for parallel or delegated tasks. However, we already spawned an explorer. I could still work with the results without adding more subagents. 

Next, I need to map all cross-references, possibly using `rg` for labels and references. I should consider employing the theorem registry for appendices. It’s essential to identify cross-references in both directions and read the relevant files. Since the user wants to exhaust the seam surface, I'll inspect all references thoroughly.
Plan update
Seam audit needs a full inventory before inspecting context. I’m separating cross-reference mapping, contextual reads, and final verification so findings stay grounded and line-exact.
  → Enumerate all appendix/theory cross-references in both directions and candidate notation seams
  • Read each seam point in context and test citation accuracy, dependency direction, and notation consistency
  • Re-verify surviving findings and produce exact fixes with line references
exec
/bin/zsh -lc "python - <<'PY'
import re
from pathlib import Path
base=Path('.')
chap_files=sorted([str(p) for p in base.glob('chapters/theory/*.tex')])
app_files=sorted([str(p) for p in base.glob('appendices/*.tex')])
files=chap_files+app_files
label_def={}  # label->file
label_files={}
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in files:
    text=Path(path).read_text()
    labels=label_pat.findall(text)
    for lab in labels:
        if lab in label_def:
            label_def[lab].append(path)
        else:
            label_def[lab]=[path]

# order macros
macros=['ref','Cref','cref','autoref','nameref','eqref','vref','pageref','hyperref']
ref_pat=re.compile(r'\\\\('+'|'.join(macros)+r')\\{(["'^}]+)'"\\}')
refs=[]
for path in files:
    text=Path(path).read_text()
    for m, content in ref_pat.findall(text):
        # split by comma
        for lab in [x.strip() for x in content.split(',') if x.strip()]:
            refs.append((path,m,lab))

# Determine cross references
chap_set=set(chap_files)
app_set=set(app_files)
cross=[]
for src,macro,lab in refs:
    defs=label_def.get(lab,[])
    if not defs:
        continue
    src_type='chap' if src in chap_set else 'app'
    for d in defs:
        dst_type='chap' if d in chap_set else 'app'
        if src_type"'!=dst_type:
            cross.append({'"'src':src,'macro':macro,'label':lab,'target_file':d,'src_type':src_type,'dst_type':dst_type})

# check circular patterns: label defined in one dir referenced by other and vice versa, maybe label pair referencing each other? We'll find label1 defined in chap referenced in app and label2 defined in app referenced in chap.
labels_chap_referenced_by_app=set()
labels_app_referenced_by_chap=set()
for c in cross:
    if c['src_type']=='chap' and c['dst_type']=='app':
        labels_app_referenced_by_chap.add(c['label'])
    if c['src_type']=='app' and c['dst_type']=='chap':
        labels_chap_referenced_by_app.add(c['label'])

# candidate circular: if there exist non-empty both sets? Need identify pairs? maybe unstoppable. We'll compute label categories and note counts.

# Build output summary lines for cross references for final message to interpret.
print('LABELS_DEF_COUNT', len(label_def))
print('CHAP->APP', sum(1 for c in cross if c['src_type']=='chap' and c['dst_type']=='app'))
print('APP->CHAP', sum(1 for c in cross if c['src_type']=='app' and c['dst_type']=='chap'))

# Also gather for final message details: e.g. limit referencing to candidate seam points: only unique combination of file pair and label maybe.
cross_summary=[]
for c in cross:
    cross_summary.append((c['src'],c['macro'],c['label'],c['target_file'],c['src_type'],c['dst_type']))

# Print summary for copying
for item in cross_summary:
    print(item)
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 50ms:
zsh:1: command not found: python

thinking
**Cross-referencing inventory**

I need to perform inventory cross-references using regex patterns. The goal is to identify references to labels defined in the appendices within the theory chapters, and vice versa. I should compile a list of labels from each set. Since Python might not be an option, I can try using `rg`, perhaps coupled with small shell loops, and consider including results from explorer as well. I'll wait for the explorer output to proceed!
collab wait(call_c7g9RuMvDTMJX6ol9lcgyWIC)
  receivers: 019d889a-cd25-7953-a496-cfc7698bf6e2
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
base=Path('.')
chap_files=sorted([str(p) for p in base.glob('chapters/theory/*.tex')])
app_files=sorted([str(p) for p in base.glob('appendices/*.tex')])
files=chap_files+app_files
label_def={}
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in files:
    text=Path(path).read_text()
    for lab in label_pat.findall(text):
        label_def.setdefault(lab,[]).append(path)
macros=['ref','Cref','cref','autoref','nameref','eqref','vref','pageref','hyperref']
ref_pat=re.compile(r'\\\\('+'|'.join(macros)+r')\\{(["'^}]+)'"\\}')
refs=[]
for path in files:
    text=Path(path).read_text()
    for m, content in ref_pat.findall(text):
        for lab in [x.strip() for x in content.split(',') if x.strip()]:
            refs.append((path,m,lab))
cross=[]
chap_set=set(chap_files)
app_set=set(app_files)
for src,macro,lab in refs:
    defs=label_def.get(lab,[])
    if not defs:
        continue
    src_type='chap' if src in chap_set else 'app'
    for d in defs:
        dst_type='chap' if d in chap_set else 'app'
        if src_type"'!=dst_type:
            cross.append({'"'src':src,'macro':macro,'label':lab,'target_file':d,'src_type':src_type,'dst_type':dst_type})
print('CHAP->APP', sum(1 for c in cross if c['src_type']=='chap' and c['dst_type']=='app'))
print('APP->CHAP', sum(1 for c in cross if c['src_type']=='app' and c['dst_type']=='chap'))
labels_app_fromchap=set()
labels_chap_fromapp=set()
for c in cross:
    if c['src_type']=='chap' and c['dst_type']=='app':
        labels_app_fromchap.add(c['label'])
    if c['src_type']=='app' and c['dst_type']=='chap':
        labels_chap_fromapp.add(c['label'])
print('labels_app_fromchap', len(labels_app_fromchap))
print('labels_chap_fromapp', len(labels_chap_fromapp))
for c in cross:
    print(c['src'],c['macro'],c['label'],'->',c['target_file'])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 825

CHAP->APP 385
APP->CHAP 436
labels_app_fromchap 176
labels_chap_fromapp 239
chapters/theory/algebraic_foundations.tex ref def:bar-complex-algebraic -> appendices/notation_index.tex
chapters/theory/algebraic_foundations.tex ref app:signs -> appendices/signs_and_shifts.tex
chapters/theory/algebraic_foundations.tex ref app:sign-conventions -> appendices/signs_and_shifts.tex
chapters/theory/algebraic_foundations.tex ref rem:three-bar-variants -> appendices/ordered_associative_chiral_kd.tex
chapters/theory/bar_cobar_adjunction_curved.tex ref ch:ordered-associative-chiral-kd -> appendices/ordered_associative_chiral_kd.tex
chapters/theory/bar_cobar_adjunction_curved.tex ref ch:ordered-associative-chiral-kd -> appendices/ordered_associative_chiral_kd.tex
chapters/theory/bar_cobar_adjunction_inversion.tex ref thm:htt -> appendices/homotopy_transfer.tex
chapters/theory/bar_cobar_adjunction_inversion.tex ref thm:essential-image-koszul -> appendices/koszul_reference.tex
chapters/theory/bar_construction.tex ref app:signs -> appendices/signs_and_shifts.tex
chapters/theory/bar_construction.tex ref app:sign-conventions -> appendices/signs_and_shifts.tex
chapters/theory/bar_construction.tex ref sec:sign-dictionary-complete -> appendices/signs_and_shifts.tex
chapters/theory/bar_construction.tex ref ver:d2-degree3 -> appendices/signs_and_shifts.tex
chapters/theory/bar_construction.tex ref prop:master-sign -> appendices/signs_and_shifts.tex
chapters/theory/bar_construction.tex ref app:signs -> appendices/signs_and_shifts.tex

thinking
**Summarizing cross-reference aggregation plan**

I’m figuring out how to process the huge volume of cross-reference data between the appendices and chapters directories by aggregating references per file pair, highlighting main bridging points, and detecting circular dependencies. My goal is to create a concise inventory of key seam points with filenames, counts, and patterns instead of listing everything raw, so the final summary is manageable and insightful.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
base=Path('.')
chap_files=sorted([str(p) for p in base.glob('chapters/theory/*.tex')])
app_files=sorted([str(p) for p in base.glob('appendices/*.tex')])
files=chap_files+app_files
label_def={}
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in files:
    text=Path(path).read_text()
    for lab in label_pat.findall(text):
        label_def.setdefault(lab,[]).append(path)
macros=['ref','Cref','cref','autoref','nameref','eqref','vref','pageref','hyperref']
ref_pat=re.compile(r'\\\\('+'|'.join(macros)+r')\\{(["'^}]+)'"\\}')
refs=[]
for path in files:
    text=Path(path).read_text()
    for m, content in ref_pat.findall(text):
        for lab in [x.strip() for x in content.split(',') if x.strip()]:
            refs.append((path,m,lab))
cross=[]
chap_set=set(chap_files)
app_set=set(app_files)
for src,macro,lab in refs:
    defs=label_def.get(lab,[])
    if not defs:
        continue
    src_type='chap' if src in chap_set else 'app'
    for d in defs:
        dst_type='chap' if d in chap_set else 'app'
        if src_type"'!=dst_type:
            cross.append({'"'src':src,'macro':macro,'label':lab,'target_file':d,'src_type':src_type,'dst_type':dst_type})
from collections import defaultdict
pairs=defaultdict(lambda: set())
for c in cross:
    pairs[(c['src'], c['target_file'])].add(c['label'])
# sort pairs by size descending
sorted_pairs=sorted(pairs.items(), key=lambda item: len(item[1]), reverse=True)
print('TOTAL_CHAP_APP', sum(1 for c in cross if c['src_type']=='chap' and c['dst_type']=='app'))
print('TOTAL_APP_CHAP', sum(1 for c in cross if c['src_type']=='app' and c['dst_type']=='chap'))
print('PAIR_COUNT', len(pairs))
print('TOP_CHAP->APP (path, references):')
count=0
for (src,dst),labs in sorted_pairs:
    if src.startswith('chapters/theory/') and dst.startswith('appendices/'):
        print(f\"{src} -> {dst} ({len(labs)} labels)\")
        count+=1
        if count>=5:
            break
print('TOP_APP->CHAP')
count=0
for (src,dst),labs in sorted_pairs:
    if src.startswith('appendices/') and dst.startswith('chapters/theory/'):
        print(f\"{src} -> {dst} ({len(labs)} labels)\")
        count+=1
        if count>=5:
            break
# detect mutual cross referencing pairs
mutual_pairs=set()
pair_map=set(pairs.keys())
for (src,dst) in pair_map:
    if dst.startswith('chapters/theory/') and src.startswith('appendices/') and (dst,src) in pair_map:
        mutual_pairs.add(tuple(sorted((src,dst))))
print('MUTUAL_PAIRS_COUNT', len(mutual_pairs))
for pair in sorted(mutual_pairs):
    print('MUTUAL', pair)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
TOTAL_CHAP_APP 385
TOTAL_APP_CHAP 436
PAIR_COUNT 98
TOP_CHAP->APP (path, references):
chapters/theory/ordered_associative_chiral_kd.tex -> appendices/ordered_associative_chiral_kd.tex (129 labels)
chapters/theory/higher_genus_modular_koszul.tex -> appendices/nonlinear_modular_shadows.tex (15 labels)
chapters/theory/higher_genus_foundations.tex -> appendices/homotopy_transfer.tex (6 labels)
chapters/theory/bar_construction.tex -> appendices/signs_and_shifts.tex (5 labels)
chapters/theory/higher_genus_complementarity.tex -> appendices/nonlinear_modular_shadows.tex (3 labels)
TOP_APP->CHAP
appendices/ordered_associative_chiral_kd.tex -> chapters/theory/ordered_associative_chiral_kd.tex (122 labels)
appendices/nonlinear_modular_shadows.tex -> chapters/theory/higher_genus_modular_koszul.tex (14 labels)
appendices/notation_index.tex -> chapters/theory/algebraic_foundations.tex (14 labels)
appendices/notation_index.tex -> chapters/theory/configuration_spaces.tex (7 labels)
appendices/branch_line_reductions.tex -> chapters/theory/higher_genus_modular_koszul.tex (6 labels)
MUTUAL_PAIRS_COUNT 16
MUTUAL ('appendices/arnold_relations.tex', 'chapters/theory/bar_construction.tex')
MUTUAL ('appendices/combinatorial_frontier.tex', 'chapters/theory/chiral_koszul_pairs.tex')
MUTUAL ('appendices/combinatorial_frontier.tex', 'chapters/theory/higher_genus_modular_koszul.tex')
MUTUAL ('appendices/homotopy_transfer.tex', 'chapters/theory/higher_genus_complementarity.tex')
wait(call_c7g9RuMvDTMJX6ol9lcgyWIC) timed out:


thinking
**Considering extraction methods**

I'm looking into how to extract labels, and it seems I might use regex with `rg` for that. I might create a shell script using Ruby or Perl since I'm trying to avoid Python. I think using `rg -n '\\label{([^}]*)}'` for labels could work. To match references to these labels might require a Perl one-liner. Also, I should include various reference macros like `\ref`, `\Cref`, and others while checking for mentions in the text.
thinking
**Exploring label extraction**

I'm considering whether I need to mention labels in the text. It might be easiest to use ripgrep for each appendix label and cross-check it against theory labels. However, there could be a lot of them—possibly dozens or even hundreds. I think I should automate this using Perl to generate matches. Since the user wants to audit all seam points, it makes sense to first inspect the counts. A shell script could be useful for counting labels and references.

codex
The governing files are loaded. I’m now extracting the actual appendix/theory label graph so I can audit the seam by concrete cross-reference edges instead of by file names or chapter titles.
thinking
**Preparing detailed seam summary**

I’m organizing a concise final summary covering the full file list for chapters and appendices, cross-reference counts, key candidate seam points with file paths and bridging labels, and notable circular dependency pairs. I’ll keep it clear and friendly with bullet points, ensuring I mention all 33 chapter and 13 appendix files by name inline, highlight top cross-references and seam points, and provide an overview of 16 mutual (circular) dependencies as instructed.
exec
/bin/zsh -lc "perl -0ne 'while(/\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){for "'$l (split /'"\\s*,\\s*/, "'$1){print "$ARGV:$.:$l'"\\n\"}}' appendices/*.tex | sed '/:"'$/d'"' | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' appendices/*.tex | sort -u | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -0ne 'while(/\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){for "'$l (split /'"\\s*,\\s*/, "'$1){print "$ARGV:$.:$l'"\\n\"}}' chapters/theory/*.tex | sed '/:"'$/d'"' | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/*.tex | sort -u | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    1013
 succeeded in 52ms:
     877
 succeeded in 51ms:
    7718
 succeeded in 50ms:
    4923
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
chap=sorted(str(p) for p in Path('.').glob('chapters/theory/*.tex'))
app=sorted(str(p) for p in Path('.').glob('appendices/*.tex'))
print('chap count', len(chap))
print('\\n'.join(chap))
print('app count', len(app))
print('\\n'.join(app))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chap count 33
chapters/theory/algebraic_foundations.tex
chapters/theory/bar_cobar_adjunction.tex
chapters/theory/bar_cobar_adjunction_curved.tex
chapters/theory/bar_cobar_adjunction_inversion.tex
chapters/theory/bar_construction.tex
chapters/theory/chiral_center_theorem.tex
chapters/theory/chiral_hochschild_koszul.tex
chapters/theory/chiral_koszul_pairs.tex
chapters/theory/chiral_modules.tex
chapters/theory/cobar_construction.tex
chapters/theory/coderived_models.tex
chapters/theory/computational_methods.tex
chapters/theory/configuration_spaces.tex
chapters/theory/derived_langlands.tex
chapters/theory/e1_modular_koszul.tex
chapters/theory/en_koszul_duality.tex
chapters/theory/existence_criteria.tex
chapters/theory/filtered_curved.tex
chapters/theory/fourier_seed.tex

thinking
**Generating cross edges**

I’m thinking about how counts are significant, but maybe I only need to focus on the cross-directional edges, which could be more manageable. I should consider using a script to intersect the references with other direction labels. It seems like generating actual cross edges is the next step. Let’s see how that plays out! I wonder what insights will come from the intersections.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %theory; for my "'$f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } for my $f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ print qq{$f:$ln:$l'"\\n} if "'$theory{$l}; } } } }'"' | sort -u" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %app; for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ print qq{$f:$ln:$l'"\\n} if "'$app{$l}; } } } }'"' | sort -u" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/arnold_relations.tex:169:thm:bar-nilpotency-complete
appendices/arnold_relations.tex:175:sec:genus-2-complete
appendices/arnold_relations.tex:175:sec:genus-3-complete
appendices/arnold_relations.tex:175:thm:arnold-genus1
appendices/arnold_relations.tex:175:thm:arnold-higher-genus
appendices/arnold_relations.tex:175:thm:arnold-quantum
appendices/arnold_relations.tex:515:thm:bar-nilpotency-complete
appendices/arnold_relations.tex:523:thm:bar-nilpotency-complete
appendices/branch_line_reductions.tex:1064:thm:modular-characteristic
appendices/branch_line_reductions.tex:130:thm:modular-characteristic
appendices/branch_line_reductions.tex:134:thm:spectral-characteristic
appendices/branch_line_reductions.tex:138:thm:universal-theta
appendices/branch_line_reductions.tex:139:thm:mc2-full-resolution
appendices/branch_line_reductions.tex:181:thm:universal-theta
appendices/branch_line_reductions.tex:192:thm:universal-theta
appendices/branch_line_reductions.tex:208:thm:spectral-characteristic
appendices/branch_line_reductions.tex:24:thm:modular-characteristic
appendices/branch_line_reductions.tex:25:thm:spectral-characteristic
appendices/branch_line_reductions.tex:27:thm:mc2-full-resolution
appendices/branch_line_reductions.tex:27:thm:universal-theta
 succeeded in 52ms:
chapters/theory/algebraic_foundations.tex:1079:app:sign-conventions
chapters/theory/algebraic_foundations.tex:1079:app:signs
chapters/theory/algebraic_foundations.tex:116:def:bar-complex-algebraic
chapters/theory/algebraic_foundations.tex:2465:rem:three-bar-variants
chapters/theory/bar_cobar_adjunction_curved.tex:109:ch:ordered-associative-chiral-kd
chapters/theory/bar_cobar_adjunction_curved.tex:166:ch:ordered-associative-chiral-kd
chapters/theory/bar_cobar_adjunction_inversion.tex:1884:thm:htt
chapters/theory/bar_cobar_adjunction_inversion.tex:3514:thm:essential-image-koszul
chapters/theory/bar_construction.tex:1007:ver:d2-degree3
chapters/theory/bar_construction.tex:1008:app:signs
chapters/theory/bar_construction.tex:1008:prop:master-sign
chapters/theory/bar_construction.tex:1289:app:arnold-relations
chapters/theory/bar_construction.tex:694:app:sign-conventions
chapters/theory/bar_construction.tex:694:app:signs
chapters/theory/bar_construction.tex:694:sec:sign-dictionary-complete
chapters/theory/chiral_hochschild_koszul.tex:1414:thm:nms-all-degree-master-equation
chapters/theory/chiral_hochschild_koszul.tex:2705:app:sign-conventions
chapters/theory/chiral_hochschild_koszul.tex:2705:app:signs
chapters/theory/chiral_hochschild_koszul.tex:3143:app:homotopy-transfer
chapters/theory/chiral_hochschild_koszul.tex:3175:app:homotopy-transfer



thinking
**Auditing label duplicates**

I need to think through the raw output and its overlapping label references. It seems like I'm including duplicate labels, which is making it noisy. I should focus on unique labels linked to appendices, especially those not defined in the theory. Citation accuracy is key, so I need to ensure that any duplicates don't create confusion. Detecting these duplicates is crucial, and I'll need to get exact file lines to fix this issue for clarity.
thinking
**Inspecting seam duplicates**

The user is asking for a seam audit, which means I need to explore relevant files while not getting bogged down by all the duplicates. I should check if the appendices and theory files are duplicating, which can cause circular dependencies. I’ll build an inventory of labels defined in both settings, identifying potential seam risks. It's crucial to cross-reference these labels, especially focusing on unique definitions in appendices and theory. Manually inspecting all edges might be too much, so I’ll need a strategic approach here.
thinking
**Classifying labels with a script**

I think I need to write a script to classify different labels effectively. First, I’ll identify unique appendix labels that are referenced from the theory. This will highlight the true appendix-to-theory seam. Then, I want to find unique theory labels referenced from appendices to see the opposite direction. Lastly, I’ll address any duplicate labels existing in both directories. It’ll be helpful to compute counts and lists for clarity. Let's get started on that script!
codex
**Seam Map**
- Files: 33 theory chapters (`chapters/theory/algebraic_foundations.tex`, `chapters/theory/bar_cobar_adjunction.tex`, `chapters/theory/bar_cobar_adjunction_curved.tex`, `chapters/theory/bar_cobar_adjunction_inversion.tex`, `chapters/theory/bar_construction.tex`, `chapters/theory/chiral_center_theorem.tex`, `chapters/theory/chiral_hochschild_koszul.tex`, `chapters/theory/chiral_koszul_pairs.tex`, `chapters/theory/chiral_modules.tex`, `chapters/theory/cobar_construction.tex`, `chapters/theory/coderived_models.tex`, `chapters/theory/computational_methods.tex`, `chapters/theory/configuration_spaces.tex`, `chapters/theory/derived_langlands.tex`, `chapters/theory/e1_modular_koszul.tex`, `chapters/theory/en_koszul_duality.tex`, `chapters/theory/existence_criteria.tex`, `chapters/theory/filtered_curved.tex`, `chapters/theory/fourier_seed.tex`, `chapters/theory/higher_genus.tex`, `chapters/theory/higher_genus_complementarity.tex`, `chapters/theory/higher_genus_foundations.tex`, `chapters/theory/higher_genus_modular_koszul.tex`, `chapters/theory/hochschild_cohomology.tex`, `chapters/theory/introduction.tex`, `chapters/theory/koszul_pair_structure.tex`, `chapters/theory/nilpotent_completion.tex`, `chapters/theory/ordered_associative_chiral_kd.tex`, `chapters/theory/poincare_duality.tex`, `chapters/theory/poincare_duality_quantum.tex`, `chapters/theory/quantum_corrections.tex`, `chapters/theory/spectral_sequences.tex`, `chapters/theory/three_invariants.tex`) and 15 appendices (`appendices/_sl2_yangian_insert.tex`, `appendices/arnold_relations.tex`, `appendices/branch_line_reductions.tex`, `appendices/combinatorial_frontier.tex`, `appendices/computational_tables.tex`, `appendices/dual_methodology.tex`, `appendices/general_relations.tex`, `appendices/homotopy_transfer.tex`, `appendices/koszul_reference.tex`, `appendices/nonlinear_modular_shadows.tex`, `appendices/notation_index.tex`, `appendices/ordered_associative_chiral_kd.tex`, `appendices/signs_and_shifts.tex`, `appendices/spectral_higher_genus.tex`, `appendices/theta_functions.tex`).
- Cross refs: 385 chapter→appendix citations and 436 appendix→chapter citations span 98 distinct file pairs, so every seam candidate connects via dozens of labelled anchors rather than isolated mentions.
- Candidate seam points: `chapters/theory/ordered_associative_chiral_kd.tex` ↔ `appendices/ordered_associative_chiral_kd.tex` (≈251 shared labels such as `thm:HH-coHH-homology`, `thm:ordered-open`, `thm:diagonal`, `prop:tensor-cotensor`); `chapters/theory/higher_genus_modular_koszul.tex` ↔ `appendices/nonlinear_modular_shadows.tex` (labels like `thm:nms-betagamma-quartic-birth`, `thm:nms-clutching-law-modular-resonance`, `conj:w3-bar-gf`); `chapters/theory/higher_genus_foundations.tex` ↔ `appendices/homotopy_transfer.tex` (`thm:htt`, `lem:sdr-existence`, `thm:tree-formula`, `constr:transfer-ainf`); `chapters/theory/bar_construction.tex` ↔ `appendices/signs_and_shifts.tex` (`sec:bar-nilpotency`, `prop:master-sign`, `eq:qme-cg`, `eq:cobar-diff-generators`); `chapters/theory/algebraic_foundations.tex` ↔ `appendices/notation_index.tex` (`def:bar-complex-algebraic`, `app:notation-index`), with the same appendix supplying `chapters/theory/configuration_spaces.tex` via `def:bar-complex-algebraic`/`sec:genus-spectral-sequence`. Another seam is `appendices/branch_line_reductions.tex` ↔ `chapters/theory/higher_genus_modular_koszul.tex` (multiple `thm:nms-*` hooks), and `appendices/spectral_higher_genus.tex` ↔ `chapters/theory/poincare_duality_quantum.tex` plus `chapters/theory/bar_cobar_adjunction_curved.tex` via prism/complementarity labels.
- Circular dependency patterns: 16 mutual pairs share labels both ways (for example `appendices/arnold_relations.tex` ↔ `chapters/theory/bar_construction.tex`, `appendices/combinatorial_frontier.tex` ↔ `chapters/theory/chiral_koszul_pairs.tex`, `appendices/combinatorial_frontier.tex` ↔ `chapters/theory/higher_genus_modular_koszul.tex`, `appendices/homotopy_transfer.tex` ↔ `chapters/theory/higher_genus_complementarity.tex`, `appendices/homotopy_transfer.tex` ↔ `chapters/theory/higher_genus_foundations.tex`, `appendices/koszul_reference.tex` ↔ `chapters/theory/bar_cobar_adjunction_inversion.tex`, `appendices/koszul_reference.tex` ↔ `chapters/theory/existence_criteria.tex`, `appendices/nonlinear_modular_shadows.tex` ↔ `chapters/theory/chiral_koszul_pairs.tex`, `appendices/nonlinear_modular_shadows.tex` ↔ `chapters/theory/higher_genus_complementarity.tex`, `appendices/nonlinear_modular_shadows.tex` ↔ `chapters/theory/higher_genus_foundations.tex`, `appendices/nonlinear_modular_shadows.tex` ↔ `chapters/theory/higher_genus_modular_koszul.tex`, `appendices/notation_index.tex` ↔ `chapters/theory/algebraic_foundations.tex`, `appendices/ordered_associative_chiral_kd.tex` ↔ `chapters/theory/en_koszul_duality.tex`, `appendices/ordered_associative_chiral_kd.tex` ↔ `chapters/theory/higher_genus_modular_koszul.tex`, `appendices/ordered_associative_chiral_kd.tex` ↔ `chapters/theory/ordered_associative_chiral_kd.tex`, `appendices/signs_and_shifts.tex` ↔ `chapters/theory/bar_construction.tex`).
codex
The first pass exposed a bigger seam risk than simple refs: many labels exist on both sides, so some “appendix references” are not obviously hitting appendix-only definitions. I’m splitting the graph into `appendix-only`, `theory-only`, and `duplicate-label` classes before reading contexts.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } my @app_only = sort grep { !exists $theory{$_} } keys %app; my @theory_only = sort grep { !exists $app{$_} } keys %theory; print "appendix_only=",scalar(@app_only)," theory_only=",scalar(@theory_only),"'"\\n\";'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$app{$1}}, "$f:$ln"; } } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$theory{$1}}, "$f:$ln"; } } } my @dup = sort grep { exists $app{$_} && exists $theory{$_} } keys %{{%app,%theory}}; print scalar(@dup),"'"\\n\"; for my "'$l (@dup){ print "$l'"\\n\"; print \"  APP  @{"'$app{$l}}'"\\n\"; print \"  THY  @{"'$theory{$l}}'"\\n\"; }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendix_only=702 theory_only=4612
 succeeded in 51ms:
311
D1
  APP  appendices/ordered_associative_chiral_kd.tex:2829
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2577
D2
  APP  appendices/ordered_associative_chiral_kd.tex:2831
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2579
D3
  APP  appendices/ordered_associative_chiral_kd.tex:2834
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2582
D4
  APP  appendices/ordered_associative_chiral_kd.tex:2836
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2584
D5
  APP  appendices/ordered_associative_chiral_kd.tex:2838
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2586
D6
  APP  appendices/ordered_associative_chiral_kd.tex:2842
  THY  chapters/theory/ordered_associative_chiral_kd.tex:2590
ch:ordered-associative-chiral-kd
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my @hits; for my $f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ push @hits, "$f:$ln:$l" if $thy_only{$l}; } } } } print scalar(@hits),"'"\\n\"; print join(\"\\n\", sort @hits),\"\\n\";'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my @hits; for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ push @hits, "$f:$ln:$l" if $app_only{$l}; } } } } print scalar(@hits),"'"\\n\"; print join(\"\\n\", sort @hits),\"\\n\";'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
197
appendices/arnold_relations.tex:169:thm:bar-nilpotency-complete
appendices/arnold_relations.tex:175:sec:genus-2-complete
appendices/arnold_relations.tex:175:sec:genus-3-complete
appendices/arnold_relations.tex:175:thm:arnold-genus1
appendices/arnold_relations.tex:175:thm:arnold-higher-genus
appendices/arnold_relations.tex:175:thm:arnold-quantum
appendices/arnold_relations.tex:515:thm:bar-nilpotency-complete
appendices/arnold_relations.tex:523:thm:bar-nilpotency-complete
appendices/branch_line_reductions.tex:1064:thm:modular-characteristic
appendices/branch_line_reductions.tex:130:thm:modular-characteristic
appendices/branch_line_reductions.tex:134:thm:spectral-characteristic
appendices/branch_line_reductions.tex:138:thm:universal-theta
appendices/branch_line_reductions.tex:139:thm:mc2-full-resolution
appendices/branch_line_reductions.tex:181:thm:universal-theta
appendices/branch_line_reductions.tex:192:thm:universal-theta
appendices/branch_line_reductions.tex:208:thm:spectral-characteristic
appendices/branch_line_reductions.tex:24:thm:modular-characteristic
appendices/branch_line_reductions.tex:25:thm:spectral-characteristic
appendices/branch_line_reductions.tex:27:thm:mc2-full-resolution
 succeeded in 52ms:
114
chapters/theory/algebraic_foundations.tex:1079:app:sign-conventions
chapters/theory/algebraic_foundations.tex:1079:app:signs
chapters/theory/algebraic_foundations.tex:116:def:bar-complex-algebraic
chapters/theory/bar_cobar_adjunction_inversion.tex:1884:thm:htt
chapters/theory/bar_cobar_adjunction_inversion.tex:3514:thm:essential-image-koszul
chapters/theory/bar_construction.tex:1007:ver:d2-degree3
chapters/theory/bar_construction.tex:1008:app:signs
chapters/theory/bar_construction.tex:1008:prop:master-sign
chapters/theory/bar_construction.tex:1289:app:arnold-relations
chapters/theory/bar_construction.tex:694:app:sign-conventions
chapters/theory/bar_construction.tex:694:app:signs
chapters/theory/bar_construction.tex:694:sec:sign-dictionary-complete
chapters/theory/chiral_hochschild_koszul.tex:1414:thm:nms-all-degree-master-equation
chapters/theory/chiral_hochschild_koszul.tex:2705:app:sign-conventions
chapters/theory/chiral_hochschild_koszul.tex:2705:app:signs
chapters/theory/chiral_hochschild_koszul.tex:3143:app:homotopy-transfer
chapters/theory/chiral_hochschild_koszul.tex:3175:app:homotopy-transfer
chapters/theory/chiral_hochschild_koszul.tex:5982:app:nonlinear-modular-shadows
chapters/theory/chiral_hochschild_koszul.tex:5994:app:branch-line-reductions



thinking
**Evaluating duplicate labels**

Wow, I've identified 311 duplicate labels, which is significant! Most of them are linked to ordered_associative_chiral_kd. The user wants exact fixes for every inconsistency, mismatch, or gap, but addressing every duplicate individually might be overwhelming. I could group related issues together and ensure I conduct a thorough audit. Reporting findings with references could streamline the process. However, I need to stay mindful of formatting requirements and aim to produce a clear, comprehensive report.
thinking
**Inspecting contexts for issues**

I need to carefully examine the contexts to identify actual problems, like potential duplicates and forward references. I want to avoid any circular dependencies, which means I might need to use scripts to detect cycles between files by building a directed graph from the references. I'll also look for appendices referencing theory labels and vice versa. While some cross-references could be harmless, I'll be vigilant for any cycles. Focusing on seam files with unique cross-directory references might be more efficient, given the high number of theory and appendix hits.
thinking
**Deriving issues through audits**

I might be able to find potential issues by checking if label names match their titles or semantics and if the introduction cites the appendix for proof details. I need to access actual line contexts to look deeper. It could help to leverage metadata or patterns to spot suspicious dependencies between proof blocks and external references. Since the user asked for a seam audit, I should examine all cross-directory references at a higher level and spot any inconsistencies. Using automated extraction for references to `app:*` macros could be a beneficial approach.
codex
The label graph is messy: there are `311` labels defined on both sides of the seam, overwhelmingly from the ordered-associative chapter and appendix. I’m checking whether both surfaces are actually included in `main.tex`; if they are, that is not a cosmetic issue but an ambiguous-reference failure.
exec
/bin/zsh -lc "rg -n 'ordered_associative_chiral_kd|appendices/|chapters/theory/' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{4} % Numbers down to subsubsubsection
\setcounter{tocdepth}{4} % TOC includes subsubsubsections

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

% EB Garamond with full features
\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols % This prevents conflicts
]{newtxmath}
\usepackage{ebgaramond}

% Fine-tuning for optimal appearance
\usepackage[
 activate={true,nocompatibility},
 succeeded in 51ms:
859:\include{chapters/theory/introduction}
963:\include{chapters/theory/fourier_seed}
970:\include{chapters/theory/algebraic_foundations}
976:\include{chapters/theory/three_invariants}
982:\include{chapters/theory/configuration_spaces}
988:\include{chapters/theory/bar_construction}
994:\include{chapters/theory/cobar_construction}
1002:% \include{chapters/theory/bar_cobar_adjunction}
1004:\input{chapters/theory/bar_cobar_adjunction_curved}
1005:\input{chapters/theory/bar_cobar_adjunction_inversion}
1010:\input{appendices/homotopy_transfer}
1016:% omitted: chapters/theory/bar_cobar_quasi_isomorphism.tex
1022:\include{chapters/theory/poincare_duality}
1030:\include{chapters/theory/chiral_koszul_pairs}
1031:\include{chapters/theory/koszul_pair_structure}
1038:% \include{chapters/theory/higher_genus}
1040:\input{chapters/theory/higher_genus_foundations}
1041:\input{chapters/theory/higher_genus_complementarity}
1042:\input{chapters/theory/higher_genus_modular_koszul}
1045:% omitted: chapters/theory/higher_genus_full.tex




thinking
**Evaluating appendix inclusion**

I'm looking into an appendix that seems not to be included in the main document. At line 1596, I need to check if that particular appendix file is part of the output. It looks like duplicate labels might not be an issue unless this appendix is actually somewhere else in the document. The user is focused on the appendices and theory chapters, which may mean I should double-check the actual files in those directories.
thinking
**Assessing appendices and theory references**

The user is focused on the seam between the appendices and the theory sections. While there is a duplicate file in the appendices, it might not pose a risk if it's not part of the live output. I think I need a list of the included appendices to assess that properly. The user mentioned appendices that might not be included, so I might have to audit all the relevant files. Still, I need to clarify any unique references if some appendix-only labels were not included.
thinking
**Identifying included appendices**

I need to gather information on the included appendices, which are homotopy_transfer, nonlinear_modular_shadows, branch_line_reductions, and a few others. It looks like the ordered appendix isn't included, which is good. I'll probably wait for the explorer results to find any seam points, but I can also do this manually. It's important to inspect the references with unique labels and check if any appendix references back to the theory, as that could create cycles.
thinking
**Identifying mutual pairs**

I’m thinking about how to identify mutual pairs efficiently. Maybe I should use unique labels for the included appendices to keep things organized. I think it's important to construct a cross-directional edge list between the files. I'll focus on including only the files that are referenced and counting them. This way, I can keep track of what I'm working with and ensure I’m referencing the right connections!
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; my %label_file; for my $f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $app_only{$1}; }} } my %pairs; for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $app_only{$l}; my ($af) = split /:/, $label_file{$l}; $pairs{"$f -> $af"}{$l}++; } } } } for my $p (sort keys %pairs){ my @labs = sort keys %{$pairs{$p}}; print "$p | ".join('"', ', @labs).\"\\n\"; }'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only); for my "'$f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my %label_file; for my $f (glob "chapters/theory/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $thy_only{$1}; }} } my %pairs; for my $f (glob "appendices/*.tex") { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $thy_only{$l}; my ($tf) = split /:/, $label_file{$l}; $pairs{"$f -> $tf"}{$l}++; } } } } for my $p (sort keys %pairs){ my @labs = sort keys %{$pairs{$p}}; print "$p | ".join('"', ', @labs).\"\\n\"; }'" in /Users/raeez/chiral-bar-cobar exited 2 in 56ms:
syntax error at -e line 1, near "join(,"
Missing right curly or square bracket at -e line 1, at end of line
Execution of -e aborted due to compilation errors.
 exited 2 in 56ms:
syntax error at -e line 1, near "join(,"
Missing right curly or square bracket at -e line 1, at end of line
Execution of -e aborted due to compilation errors.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only); for my "'$f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; my %label_file; for my $f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $app_only{$1}; }} } my %pairs; for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $app_only{$l}; my ($af) = split /:/, $label_file{$l}; $pairs{"$f -> $af"}{$l}++; } } } } for my $p (sort keys %pairs){ my @labs = sort keys %{$pairs{$p}}; print $p, q{ | }, join(q{, }, @labs), qq{'"\\n}; }'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/algebraic_foundations.tex -> appendices/notation_index.tex | def:bar-complex-algebraic
chapters/theory/algebraic_foundations.tex -> appendices/signs_and_shifts.tex | app:sign-conventions, app:signs
chapters/theory/bar_cobar_adjunction_inversion.tex -> appendices/homotopy_transfer.tex | thm:htt
chapters/theory/bar_cobar_adjunction_inversion.tex -> appendices/koszul_reference.tex | thm:essential-image-koszul
chapters/theory/bar_construction.tex -> appendices/arnold_relations.tex | app:arnold-relations
chapters/theory/bar_construction.tex -> appendices/signs_and_shifts.tex | app:sign-conventions, app:signs, prop:master-sign, sec:sign-dictionary-complete, ver:d2-degree3
chapters/theory/chiral_hochschild_koszul.tex -> appendices/branch_line_reductions.tex | app:branch-line-reductions
chapters/theory/chiral_hochschild_koszul.tex -> appendices/homotopy_transfer.tex | app:homotopy-transfer
chapters/theory/chiral_hochschild_koszul.tex -> appendices/nonlinear_modular_shadows.tex | app:nonlinear-modular-shadows, thm:nms-all-degree-master-equation
chapters/theory/chiral_hochschild_koszul.tex -> appendices/signs_and_shifts.tex | app:sign-conventions, app:signs
chapters/theory/chiral_koszul_pairs.tex -> appendices/combinatorial_frontier.tex | app:combinatorial-frontier
chapters/theory/chiral_koszul_pairs.tex -> appendices/nonlinear_modular_shadows.tex | lem:nms-euler-inversion, thm:nms-archetype-trichotomy
chapters/theory/chiral_modules.tex -> appendices/_sl2_yangian_insert.tex | thm:sl2-koszul-dual
chapters/theory/chiral_modules.tex -> appendices/homotopy_transfer.tex | app:homotopy-transfer
chapters/theory/cobar_construction.tex -> appendices/signs_and_shifts.tex | app:sign-conventions, app:signs
chapters/theory/configuration_spaces.tex -> appendices/arnold_relations.tex | thm:arnold-iff-nilpotent
chapters/theory/configuration_spaces.tex -> appendices/signs_and_shifts.tex | app:signs, eq:qme-cg
chapters/theory/en_koszul_duality.tex -> appendices/arnold_relations.tex | cor:bar-d-squared-zero-arnold
chapters/theory/en_koszul_duality.tex -> appendices/homotopy_transfer.tex | thm:htt-operadic
chapters/theory/existence_criteria.tex -> appendices/koszul_reference.tex | app:koszul-reference
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%thy_only); for my "'$f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my %label_file; for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $thy_only{$1}; }} } my %pairs; for my $f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $thy_only{$l}; my ($tf) = split /:/, $label_file{$l}; $pairs{"$f -> $tf"}{$l}++; } } } } for my $p (sort keys %pairs){ my @labs = sort keys %{$pairs{$p}}; print $p, q{ | }, join(q{, }, @labs), qq{'"\\n}; }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/arnold_relations.tex -> chapters/theory/bar_construction.tex | thm:bar-nilpotency-complete
appendices/arnold_relations.tex -> chapters/theory/higher_genus_foundations.tex | sec:genus-2-complete, sec:genus-3-complete, thm:arnold-genus1, thm:arnold-higher-genus, thm:arnold-quantum
appendices/branch_line_reductions.tex -> chapters/theory/higher_genus_modular_koszul.tex | def:scalar-lane, def:shadow-postnikov-tower, thm:mc2-full-resolution, thm:modular-characteristic, thm:spectral-characteristic, thm:universal-theta
appendices/combinatorial_frontier.tex -> chapters/theory/bar_cobar_adjunction_inversion.tex | thm:spectral-sequence-collapse
appendices/combinatorial_frontier.tex -> chapters/theory/chiral_koszul_pairs.tex | cor:bar-cohomology-koszul-dual, rem:ce-vs-exterior, thm:km-chiral-koszul, thm:virasoro-chiral-koszul
appendices/combinatorial_frontier.tex -> chapters/theory/configuration_spaces.tex | thm:fm-associahedron
appendices/combinatorial_frontier.tex -> chapters/theory/higher_genus_foundations.tex | thm:genus-universality
appendices/combinatorial_frontier.tex -> chapters/theory/higher_genus_modular_koszul.tex | def:shadow-postnikov-tower, thm:mc2-bar-intrinsic, thm:modular-characteristic, thm:operadic-complexity-detailed
appendices/computational_tables.tex -> chapters/theory/chiral_koszul_pairs.tex | ex:w3-completion-full
appendices/dual_methodology.tex -> chapters/theory/chiral_koszul_pairs.tex | thm:bar-cobar-isomorphism-main, thm:koszul-equivalences-meta
appendices/general_relations.tex -> chapters/theory/bar_construction.tex | sec:bar-nilpotency, thm:residue-formula
appendices/homotopy_transfer.tex -> chapters/theory/chiral_koszul_pairs.tex | thm:bar-cobar-isomorphism-main
appendices/homotopy_transfer.tex -> chapters/theory/higher_genus_complementarity.tex | rem:homotopy-native-b, thm:quantum-complementarity-main
appendices/homotopy_transfer.tex -> chapters/theory/higher_genus_foundations.tex | chap:higher-genus, conv:higher-genus-differentials, thm:bar-ainfty-complete, thm:concrete-quantum-differential, thm:genus-differential, thm:genus-universality
appendices/homotopy_transfer.tex -> chapters/theory/higher_genus_modular_koszul.tex | thm:rectification-meta
appendices/homotopy_transfer.tex -> chapters/theory/spectral_sequences.tex | prop:degen-koszul
appendices/koszul_reference.tex -> chapters/theory/bar_cobar_adjunction_curved.tex | ex:mc-deformations, ex:mc-periods, thm:genus-induction-strict, thm:koszul-conilpotent
appendices/koszul_reference.tex -> chapters/theory/bar_cobar_adjunction_inversion.tex | sec:filtered-vs-curved-comprehensive, thm:bar-cobar-inversion-qi
appendices/koszul_reference.tex -> chapters/theory/bar_construction.tex | def:bar-geometric, def:geometric-bar, thm:geometric-equals-operadic-bar
appendices/koszul_reference.tex -> chapters/theory/chiral_koszul_pairs.tex | def:chiral-koszul-pair, thm:bar-concentration, thm:e1-chiral-koszul-duality, thm:pbw-koszulness-criterion

thinking
**Identifying file cycles**

I can inspect mutual file pairs to identify cycles. It seems that many appendices point back to the theory files they support, creating potential circular dependencies. For example, if a theory theorem uses an appendix theorem and that theorem relies back on the theory theorem, I could have a cycle on my hands. I’ll need to detect these mutual pairs at the file level and do a contextual read to see if the appendix theorem is used in the proof.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only,%AtoT,%TtoA); for my "'$f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my %app_label_file; for my $f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app_label_file{$1} = $f if $app_only{$1}; }} } my %thy_label_file; for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$thy_label_file{$1} = $f if $thy_only{$1}; }} } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $app_only{$l}; $TtoA{$f}{$app_label_file{$l}}=1; } } } } for my $f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $thy_only{$l}; $AtoT{$f}{$thy_label_file{$l}}=1; } } } } for my $t (sort keys %TtoA){ for my $a (sort keys %{$TtoA{$t}}){ if($AtoT{$a}{$t}){ print "$t <-> $a'"\\n\"; } } }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/algebraic_foundations.tex <-> appendices/notation_index.tex
chapters/theory/bar_cobar_adjunction_inversion.tex <-> appendices/koszul_reference.tex
chapters/theory/bar_construction.tex <-> appendices/arnold_relations.tex
chapters/theory/bar_construction.tex <-> appendices/signs_and_shifts.tex
chapters/theory/chiral_koszul_pairs.tex <-> appendices/combinatorial_frontier.tex
chapters/theory/chiral_koszul_pairs.tex <-> appendices/nonlinear_modular_shadows.tex
chapters/theory/existence_criteria.tex <-> appendices/koszul_reference.tex
chapters/theory/higher_genus_complementarity.tex <-> appendices/homotopy_transfer.tex
chapters/theory/higher_genus_complementarity.tex <-> appendices/nonlinear_modular_shadows.tex
chapters/theory/higher_genus_foundations.tex <-> appendices/homotopy_transfer.tex
chapters/theory/higher_genus_foundations.tex <-> appendices/nonlinear_modular_shadows.tex
chapters/theory/higher_genus_modular_koszul.tex <-> appendices/combinatorial_frontier.tex
chapters/theory/higher_genus_modular_koszul.tex <-> appendices/nonlinear_modular_shadows.tex
collab wait(call_osd2OILoqBQ5xQxbdjt0fvqs)
  receivers: 019d889a-cd25-7953-a496-cfc7698bf6e2
wait(call_osd2OILoqBQ5xQxbdjt0fvqs) 1 agents complete:
  019d889a-cd25-7953-a496-cfc7698bf6e2 completed: "**Seam Map**
- Files: 33 theory chapters (`chapters/theory/algebraic_foundations.tex`, `chapters/theory/bar_cobar_adjunc…"
codex
A real seam failure surfaced: `chapters/theory/chiral_modules.tex` cites `thm:sl2-koszul-dual`, and that label is only defined in `appendices/_sl2_yangian_insert.tex`, which `main.tex` does not include. I’m checking the whole seam for this exact class: body/appendix references that point into omitted files.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %inc; open my "'$fh, q{<}, q{main.tex} or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:input|include)\\{(["'^}]+)'"\\}/g){ my "'$p = $1; $p .= q{.tex} unless $p =~ /'"\\.tex"'$/; $inc{$p}=1; } } my (%app,%theory,%app_only,%thy_only,%label_file); for my $f (glob q{appendices/*.tex}) { open my $fh2, q{<}, $f or die $!; local $/; my $t=<$fh2>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh2, q{<}, $f or die $!; local $/; my $t=<$fh2>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; for my $f (glob q{appendices/*.tex}) { open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){ $ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $app_only{$1}; } } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $app_only{$l}; my ($target,$tln)=split /:/,$label_file{$l},2; next if $inc{$target}; print "$f:$ln -> $l -> $target:$tln'"\\n\"; } } } }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_modules.tex:2889 -> thm:sl2-koszul-dual -> appendices/_sl2_yangian_insert.tex:533
chapters/theory/chiral_modules.tex:2961 -> thm:sl2-koszul-dual -> appendices/_sl2_yangian_insert.tex:533
chapters/theory/chiral_modules.tex:2982 -> thm:sl2-koszul-dual -> appendices/_sl2_yangian_insert.tex:533
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %inc; open my "'$fh, q{<}, q{main.tex} or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:input|include)\\{(["'^}]+)'"\\}/g){ my "'$p = $1; $p .= q{.tex} unless $p =~ /'"\\.tex"'$/; $inc{$p}=1; } } my (%app,%theory,%app_only,%thy_only,%label_file); for my $f (glob q{appendices/*.tex}) { open my $fh2, q{<}, $f or die $!; local $/; my $t=<$fh2>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=1 } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh2, q{<}, $f or die $!; local $/; my $t=<$fh2>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; for my $f (glob q{chapters/theory/*.tex}) { open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){ $ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$label_file{$1} = "$f:$ln" if $thy_only{$1}; } } } for my $f (glob q{appendices/*.tex}) { open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){ $ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ next unless $thy_only{$l}; my ($target,$tln)=split /:/,$label_file{$l},2; next if $inc{$target}; print "$f:$ln -> $l -> $target:$tln'"\\n\"; } } } }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:


thinking
**Inspecting omitted references**

I'm thinking there could be appendix references that might relate to missing theory files, but I don't see any. I need to dig a bit deeper into the line contexts to see if there are any omitted references and relevant theorem contents. I should look into the chiral_modules and _sl2_yangian_insert. It seems important to check the main files concerning the includes. There's definitely a lot to go through here!
exec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '500,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2868,2992p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   500	\begin{proposition}[Tensor products and Yang--Baxter;
   501	\ClaimStatusProvedHere]
   502	\label{prop:eval-tensor-sl2}
   503	The tensor product of evaluation modules $V_a\otimes V_b$ ($a\neq b$) is
   504	irreducible as a $Y_\hbar(\mathfrak{sl}_2)$-module. The
   505	$R$-matrix intertwining $V_a\otimes V_b\cong V_b\otimes V_a$ is
   506	\begin{equation}\label{eq:eval-r-sl2}
   507	\check R_{ab}\;=\;(a-b)\,I+\hbar\,P\;=\;R(a-b)
   508	\;\in\;\operatorname{End}(V_a\otimes V_b),
   509	\end{equation}
   510	recovering the Yang $R$-matrix of Theorem~\ref{thm:yang-r-matrix}. At
   511	$a=b$, the tensor product is reducible:
   512	$V_a\otimes V_a\cong \operatorname{Sym}^2 V\oplus\bigwedge^2 V$ decomposes
   513	as a direct sum of the $3$-dimensional irreducible and the trivial
   514	representation. The $R$-matrix $R(0)=\hbar P$ is the
   515	permutation, consistent with $R(0)$ having eigenvalue
   516	$+\hbar$ on $\operatorname{Sym}^2$ and $-\hbar$ on $\bigwedge^2$.
   517	\end{proposition}
   518	
   519	\begin{proof}
 succeeded in 52ms:
  2868	Kac--Wakimoto theorem
  2869	\textup{(}Theorem~\ref{thm:kw-bar-general-rank}\textup{)}, not a
  2870	general bar-spectral-sequence theorem proved here.
  2871	For integrable levels,
  2872	$d_1 = 0$ and the full $E_1$ page survives, but the
  2873	resolution terminates at length
  2874	$|\mathcal{W}_{\mathrm{aff}}/\mathcal{W}_{\mathrm{fin}}|$
  2875	due to the vanishing of the Verma modules beyond the
  2876	affine Weyl chamber.
  2877	\end{remark}
  2878	
  2879	\begin{computation}[BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat}
  2880	at generic level; \ClaimStatusProvedHere]
  2881	\label{comp:bgg-sl2-pipeline}
  2882	\index{BGG resolution!explicit pipeline}
  2883	\index{bar complex!BGG pipeline}
  2884	We trace the bar complex of $\widehat{\mathfrak{sl}}_{2,k}$ through
  2885	the BGG spectral sequence (Theorem~\ref{thm:bgg-from-bar}) step by
  2886	step, connecting the explicit bar differential matrix
  2887	(Computation~\ref{comp:sl2-bar-matrix}) to the classical BGG
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1148,1166p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1148	
  1149	% --------------------------------------------------
  1150	% E₁ MODULAR KOSZUL DUALITY
  1151	% Ribbon modular operad, FAss, E₁ convolution algebra, E₁ shadow
  1152	% Postnikov tower, and the five main theorems A^{E₁}--H^{E₁} at
  1153	% all genera.
  1154	% --------------------------------------------------
  1155	\input{chapters/theory/e1_modular_koszul}
  1156	
  1157	% ------ Ordered Associative Chiral Koszul Duality ------
  1158	% Diagonal bicomodule, Hochschild-coHochschild dictionary, open trace formalism.
  1159	\input{chapters/theory/ordered_associative_chiral_kd}
  1160	
  1161	% E_n Koszul duality: higher-dimensional bar complexes,
  1162	% Totaro relations, connection to Ayala--Francis, the n=2 case.
  1163	\input{chapters/theory/en_koszul_duality}
  1164	
  1165	% The open/closed realization: proved theorem establishing the correct
  1166	% architecture. The derived center is the universal bulk (not the bar
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1624,1728p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1624	\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
  1625	\label{thm:chain-vs-homology}
  1626	Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
  1627	\begin{enumerate}[label=\textup{(\roman*)}]
  1628	\item \emph{Chain level.}
  1629	 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
  1630	 all operations are computable via configuration space integrals,
  1631	 and homotopies have geometric meaning as forms on
  1632	 $\overline{C}_n(X)$.
  1633	\item \emph{Homology level.}
  1634	 The homotopy transfer theorem
  1635	 (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
  1636	 $A_\infty$ structure $\{m_k^H\}$ on $H^*(\mathcal{A})$ with
  1637	 $m_1^H = 0$. The product $m_2^H$ descends to homology
  1638	 (it is strictly associative if $\mathcal{A}$ is formal).
  1639	 However, the transferred higher operations
  1640	 $m_k^H$ for $k \geq 3$ are in general \emph{non-trivial}:
  1641	 they are the Massey products, encoding obstructions to formality.
  1642	\item \emph{What is lost.}
  1643	 The explicit chain-level homotopies $\{h_n\}$ (the contracting
 succeeded in 51ms:
     1	\chapter{Homotopy transfer}
     2	\label{app:homotopy-transfer}
     3	
     4	\index{homotopy transfer theorem|textbf}
     5	
     6	The homotopy
     7	transfer theorem is the mechanism by which classical Koszul duality
     8	acquires quantum corrections. Passing from a chain complex to its
     9	cohomology via a deformation retract necessarily introduces higher
    10	operations $m_k$ for $k \geq 3$; these are precisely the genus-$0$
    11	quantum corrections of the bar complex
    12	(Theorem~\ref{thm:bar-ainfty-complete}).
    13	
    14	\begin{proposition}[Homotopy transfer as rectification mechanism]
    15	\label{prop:htt-rectification}
    16	\ClaimStatusProvedHere
    17	The homotopy transfer theorem is the technical engine of the
    18	rectification meta-theorem
    19	(Theorem~\ref{thm:rectification-meta}): given a deformation retract
    20	$V \xrightarrow{p} H \xrightarrow{i} V$ with $pi = \mathrm{id}$
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '720,840p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   720	formality is a property of the \emph{resolution}, not of the
   721	\emph{interactions}.
   722	\end{remark}
   723	
   724	\subsection{Genus corrections as transferred operations}
   725	\label{subsec:genus-corrections-htt}
   726	
   727	At genus $g \geq 1$, the fiberwise bar differential acquires curvature
   728	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$
   729	(Convention~\ref{conv:higher-genus-differentials}), and the
   730	HTT framework extends to the curved setting.
   731	
   732	\begin{proposition}[Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0};
   733	\ClaimStatusProvedHere]
   734	\label{prop:genus1-curvature-m0}
   735	\index{curvature!as $m_0$}
   736	The genus-$1$ obstruction $\kappa(\cA) \in k$ of
   737	Theorem~\textup{\ref{thm:genus-universality}} is the nullary
   738	operation $m_0$ of the curved $\Ainf$-structure transferred from
   739	the genus-$1$ bar complex:


thinking
**Evaluating theorem dependencies**

I need to determine the issues regarding the higher genus foundations theorem proof and its appendix. The appendix references the main theorem, which doesn't seem circular but could raise questions about dependencies. It might be fine if the appendix supports the core theorem since the proof relies on it. However, I need to inspect any mismatches or circular dependencies carefully. The proof's reliance on constructions in the appendix could be acceptable, given that standard theorems are referenced correctly.
thinking
**Analyzing appendix references**

I need to check if the appendix references the theorem it supports within its proof or statements. For instance, the `prop:genus1-curvature-m0` references `thm:genus-universality`, which isn’t circular unless theorem C uses it, so I should confirm that. A stronger concern may arise because the proof in the theory chapter relies on appendix theorems defined later, while the appendix also uses these theorems. However, if the appendix theorems are standard and proven elsewhere, there shouldn’t be a cycle. I might look for specific dependencies in the labels to clarify.
exec
/bin/zsh -lc "nl -ba appendices/notation_index.tex | sed -n '336,350p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '100,130p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   100	\subsection{Quadratic algebras and Koszul duality}
   101	
   102	\begin{definition}[Quadratic algebra]
   103	\label{def:quadratic-algebra}
   104	\index{quadratic algebra|textbf}
   105	A graded algebra $A = T(V)/I$ is \emph{quadratic} if:
   106	\begin{enumerate}
   107	\item $V$ is a graded vector space (generators)
   108	\item $I \subset V \otimes V$ is a subspace of relations in degree 2
   109	\item The defining ideal is $(I)$ generated by $I$
   110	\end{enumerate}
   111	We write $A = A(V, R)$ where $R \subset V \otimes V$ are the
   112	relations. The algebra carries a canonical \emph{augmentation}
   113	$\varepsilon \colon A \twoheadrightarrow k$ sending all generators
   114	to zero; the \emph{augmentation ideal} is
   115	$\bar{A} = \ker(\varepsilon) = \bigoplus_{n \geq 1} V^{\otimes n}/(I)$.
   116	The bar construction (Definition~\ref{def:bar-complex-algebraic})
   117	is built from~$\bar{A}$.
   118	\end{definition}
   119	
 succeeded in 51ms:
   336	\end{definition}
   337	
   338	\begin{definition}[Arnold relations]\label{def:arnold-relations}
   339	The Arnold-relation package is the one established in Theorem~\ref{thm:arnold-relations}.
   340	\end{definition}
   341	
   342	\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic}
   343	The algebraic bar complex is represented by the DG coalgebra model of Theorem~\ref{thm:bar-coalgebra}.
   344	\end{definition}
   345	
   346	\begin{definition}[Geometric bar complex]\label{def:geometric-bar-complex}
   347	The geometric bar complex is Definition~\ref{def:geometric-bar}.
   348	\end{definition}
   349	
   350	\begin{definition}[Central charge]\label{def:central-charge}
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:bar-complex-algebraic\\}' -S ." in /Users/raeez/chiral-bar-cobar succeeded in 61ms:
./appendices/notation_index.tex:342:\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic}

thinking
**Inspecting dependencies**

I'm considering whether the appendix can reference main chapter proofs. If it's a deliberate appendix dependency, it's crucial to check cited references to avoid circular dependencies. The appendix `homotopy_transfer` cites `thm:genus-differential` and `thm:genus-universality`, but I need to check if these theorems rely on results from the appendix. I'll search within `higher_genus_foundations` for any citations to ensure there's no cycle. If they don't cite back, then it might be acceptable. Let’s inspect the details carefully.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:genus-universality\\}|\\\\label\\{thm:genus-differential\\}|\\\\label\\{conv:higher-genus-differentials\\}|\\\\label\\{thm:bar-ainfty-complete\\}|\\\\label\\{thm:rectification-meta\\}|\\\\label\\{thm:concrete-quantum-differential\\}' chapters/theory/higher_genus_foundations.tex appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
chapters/theory/higher_genus_foundations.tex:1210:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex; \ClaimStatusProvedHere]\label{thm:bar-ainfty-complete}
chapters/theory/higher_genus_foundations.tex:3748:\label{thm:genus-differential}
chapters/theory/higher_genus_foundations.tex:3808:\label{thm:concrete-quantum-differential}
chapters/theory/higher_genus_foundations.tex:5555:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5200,5440p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5200	H^{4g}(\overline{\mathcal{M}}_g, Z(\mathcal{A})^{\otimes 2}).
  5201	\end{equation}
  5202	For multi-generator algebras, see
  5203	Remark~\textup{\ref{rem:multi-generator-nilpotence}} below.
  5204	\end{theorem}
  5205	
  5206	\begin{proof}
  5207	By Theorem~\ref{thm:genus-universality} (single strong generator hypothesis),
  5208	$\operatorname{obs}_g = \kappa \cdot \lambda_g$ where
  5209	$\lambda_g = c_g(\mathbb{E}) \in \mathrm{CH}^g(\overline{\mathcal{M}}_g)$
  5210	is the top Chern class of the rank-$g$ Hodge bundle~$\mathbb{E}$.
  5211	Therefore $(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2$,
  5212	and it suffices to show $\lambda_g^2 = 0$ in
  5213	$\mathrm{CH}^{2g}(\overline{\mathcal{M}}_g)$.
  5214	
  5215	This is an immediate consequence of
  5216	\emph{Mumford's relation}~\cite{Mumford83}:
  5217	\begin{equation}\label{eq:mumford-relation}
  5218	c(\mathbb{E}) \cdot c(\mathbb{E}^\vee) = 1
  5219	\qquad \text{in } \mathrm{CH}^*(\overline{\mathcal{M}}_g).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3728,3836p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5548,5616p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3728	\end{definition}
  3729	
  3730	\begin{remark}[Genus filtration of the modular deformation object]
  3731	\label{rem:genus-filtration-deformation}
  3732	The genus stratification of
  3733	Definition~\ref{def:genus-stratified-bar} is the chain-level
  3734	incarnation of the complete genus filtration on $\Definfmod(\cA)$
  3735	(Theorem~\ref{thm:modular-homotopy-convolution}), with each stratum
  3736	$\gr_g$ computing deformations at fixed genus.
  3737	\end{remark}
  3738	
  3739	\begin{remark}[String theory interpretation]
  3740	\label{rem:string-theory-genus}
  3741	This is the genus expansion of string amplitudes:
  3742	$A = \sum_{g=0}^\infty g_s^{2g-2} A^{(g)}$, with each $A^{(g)}$ an integral over $\overline{\mathcal{M}}_{g,n}$.
  3743	\end{remark}
  3744	
  3745	\subsection{The differential}
  3746	
  3747	\begin{theorem}[Genus-dependent differential; \ClaimStatusProvedHere]
 succeeded in 52ms:
  5548	Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
  5549	\hline
  5550	\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
  5551	\hline
  5552	\end{tabular}
  5553	\end{table}
  5554	
  5555	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5556	\index{genus universality theorem|textbf}
  5557	\textup{[Regime: curved-central on the Koszul locus; all genera
  5558	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5559	
  5560	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5561	all have the \emph{same} conformal weight. There exists a
  5562	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5563	curvature, such that \begin{equation}\label{eq:genus-universality}
  5564	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5565	\qquad \textup{(}UNIFORM-WEIGHT\textup{)}
  5566	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5567	\quad \text{for all } g \geq 1,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '35120,35268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/combinatorial_frontier.tex | sed -n '328,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 35120	\end{proof}
 35121	
 35122	\begin{remark}[Position in the shadow obstruction tower]
 35123	\label{rem:spectral-shadow-position}
 35124	\index{shadow tower!spectral level}
 35125	The lifted spectral cover sits at the $L_2$ level of the
 35126	characteristic hierarchy
 35127	(cf.~\S\ref{subsec:completion-kinematics-programme}): $L_1$ is the scalar
 35128	modular characteristic~$\kappa(\cA)$, while $L_2$ is the
 35129	spectral discriminant~$\Delta_\cA$ together with its module
 35130	structure. The defect calculus developed here provides the
 35131	geometric content of this level: the discriminant polynomial is
 35132	the visible shadow, but tensor transport, DS reduction, and
 35133	level-rank duality require the full lifted cover.
 35134	The $\widehat{\mathfrak{sl}}_3/\mathcal{W}_3$ orbit
 35135	(Conjectures~\ref{conj:sl3-bar-gf}
 35136	and~\ref{conj:w3-bar-gf}) is the first example where the
 35137	visible generating functions are both rational but the lifted
 35138	covers are nontrivially cubic: the algebra and its DS image
 35139	live on different sheets of a common $S_3$ cover, and the DS
 succeeded in 52ms:
   328	\end{tabular}
   329	\end{center}
   330	
   331	\emph{How they appear.}
   332	
   333	\begin{enumerate}[label=(\roman*)]
   334	\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.
   335	
   336	\item \emph{Associahedra.} The associahedron $K_n$ has $C_{n-1}$ vertices (maximal bracketings of an $(n+1)$-fold product). The FM compactification $\overline{C}_n(\mathbb{P}^1) \cong K_n$ of the genus-$0$ configuration space is isomorphic to the associahedron as a stratified space (Theorem~\ref{thm:fm-associahedron}). The Betti numbers of $K_n$ are related to Narayana numbers, and the $f$-vector encodes the bar spectral sequence page dimensions.
   337	
   338	\item \emph{Virasoro at low degree.} The first few Virasoro bar cohomology dimensions $(1, 2, 5, 12, 30)$ begin with a Catalan-adjacent pattern: $C_1 = 1$, $C_2 = 2$, $C_3 = 5$. The agreement is not coincidental but breaks at $n = 4$ ($C_4 = 14 \neq 12$), reflecting the distinction between the full Catalan enumeration and the Motzkin-difference count.
   339	\end{enumerate}
   340	
   341	\subsection{Bernoulli numbers (genus expansion)}
   342	\label{subsec:bernoulli}
   343	
   344	The Bernoulli numbers $B_{2g}$ (OEIS~A027642 for denominators) govern the genus expansion of every Koszul chiral algebra.
   345	
   346	\begin{center}
   347	\renewcommand{\arraystretch}{1.2}

thinking
**Considering theorem structure**

I’m thinking about organizing an appendix section focused on signs that rely on bar nilpotency. Then, I could use a theorem in the body that references a proposition from the appendix related to signs. It feels like a clear way to structure the information, and I’m curious if that could enhance the overall understanding. Let’s inspect that further and see how everything connects!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '680,714p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   680	The Heisenberg algebra $\mathcal{H}_k$ with OPE $J(z)J(w) = k/(z-w)^2 + \text{regular}$ has bar differential
   681	$d_{\mathrm{res}}(J \otimes J \otimes \eta_{12}) = J_{(1)}J = k \cdot \mathbf{1}$
   682	at degree~$1$: the full chiral product extracts the double-pole mode $J_{(1)}J = k$. Since $J_{(0)}J = 0$ (no simple pole), only the curvature component $d_{\mathrm{curvature}}$ contributes (Proposition~\ref{prop:pole-decomposition}). The level~$k$ is visible at genus~$0$ through the bar differential; at genus~$g \geq 1$, it acquires a topological partner $\kappa(\cH_k)\cdot\omega_g$ from the Hodge bundle (Chapter~\ref{chap:higher-genus}). See Chapter~\ref{ch:heisenberg-frame}, \S\ref{sec:frame-bar-deg1} for the full computation.
   683	\end{example}
   684	
   685	% Orientation bundle: see Definition~\ref{def:orientation} below.
   686	
   687	\subsection{Sign conventions}\label{sec:sign-conventions}
   688	
   689	\begin{convention}[Enhanced sign system]\label{conv:orientations-enhanced}
   690	The bar complex requires three types of sign conventions:
   691	
   692	\emph{Type 1: Koszul signs (algebraic).}
   693	
   694	The standard Koszul sign rule (Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}; see also \S\ref{sec:sign-dictionary-complete}) applies with total degree $|\phi| + k$ for a field $\phi \in \mathcal{A}$ tensored with a form in $\Omega^k$.
   695	
   696	\emph{Type 2: Orientation signs (geometric).}
   697	
   698	Configuration spaces and their boundary divisors carry orientations:
   699	
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '996,1016p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
   996	$\Res_{D_{ij}}$ is a $\cD_X$-module operation, and
   997	$d_\cA$ is $\cD_X$-linear.
   998	
   999	For $\{d_1, d_3\} = 0$: the operators $d_1$ and $d_3$ act on the algebra and form tensor factors respectively. The Koszul sign accompanying $d_3$ includes a factor $(-1)^{\sum_i |\phi_i|}$ from passing the de Rham differential past the algebra elements. After $d_1$ increases one algebra degree by $1$, the sign acquires an extra factor of $(-1)$. Thus $d_3 \circ d_1 = -d_1 \circ d_3$, and the anticommutator vanishes.
  1000	
  1001	For $\{d_2, d_3\} = 0$: this follows from the residue exact sequence for logarithmic forms. On a normal crossing divisor $D = \bigcup D_{ij} \subset \overline{C}_{n+1}(X)$, the residue map fits into the exact sequence $0 \to \Omega^k \to \Omega^k(\log D) \xrightarrow{\text{Res}} \bigoplus_{D_{ij}} \Omega^{k-1}_{D_{ij}}(\log D') \to 0$, and the de Rham differential is compatible with the residue map: $\text{Res}_{D_{ij}} \circ d_{\text{dR}} = d_{\text{dR}}|_{D_{ij}} \circ \text{Res}_{D_{ij}}$. Since $d_2$ is a signed sum of residues and $d_3 = d_{\text{dR}}$, they anticommute (with signs from Convention~\ref{conv:orientations-enhanced}).
  1002	\end{proof}
  1003	
  1004	\begin{remark}[Sign-level verification]\label{rem:sign-bridge}
  1005	For a complete sign-by-sign verification of $d^2 = 0$ at low degrees
  1006	(including the explicit computation for degree-3 elements $[a|b|c]$ in a
  1007	graded associative algebra), see Verification~\ref{ver:d2-degree3} and
  1008	Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
  1009	\end{remark}
  1010	
  1011	\begin{remark}[Synthesis]\label{rem:d-squared-synthesis}\label{rem:geometric-miracle}
  1012	The three mechanisms entering the proof of $d^2 = 0$,
  1013	the Borcherds identity (algebra), Stokes' theorem (topology), and
  1014	residue calculus (analysis), all arise from the boundary
  1015	stratification of $\overline{C}_n(X)$. For the Heisenberg algebra,
exec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '960,1010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1278,1296p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '1748,1772p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   960	\subsubsection{Collision divisor signs}
   961	
   962	\emph{Rule.} Collision divisors are always written with indices in increasing order: $\colldiv{i}{j}$ means $i < j$.
   963	
   964	\emph{Convention.} We write $\colldiv{i}{j}$ with $i < j$. Geometrically $D_{ij} = D_{ji}$ (same subvariety $z_i = z_j$). The sign convention $\colldiv{j}{i} = -\colldiv{i}{j}$ applies to the \emph{oriented divisor} (i.e., to the associated residue forms, not the subvariety itself).
   965	
   966	\subsubsection{Arnold relation signs}
   967	
   968	\emph{3-term Arnold relation.}
   969	\[\LogForm{i}{j} \wedge \LogForm{j}{k} + \LogForm{j}{k} \wedge \LogForm{k}{i} + \LogForm{k}{i} \wedge \LogForm{i}{j} = 0\]
   970	
   971	\emph{Higher-degree consequences.}
   972	All higher-degree relations in the OS algebra follow from the 3-term Arnold relations by repeated application. There is no independent ``general Arnold relation'' beyond the 3-term version.
   973	
   974	\subsubsection{Residue signs}
   975	
   976	The sign arising from the residue at $\colldiv{i}{j}$ is determined by the Koszul sign rule: the residue operation (cohomological degree~$1$) must commute past the preceding tensor factors. For elements $s^{-1}a_1 \otimes \cdots \otimes s^{-1}a_n$ in the bar complex, the residue at $D_{ij}$ (colliding factors $i$ and $j$) picks up the sign $(-1)^{\sum_{k<i}|s^{-1}a_k|}$. In particular, when all generators have even desuspended degree, all residue signs are positive.
   977	
   978	For the explicit sign computations relevant to the bar differential, see the proof of $d^2 = 0$ in \S\ref{sec:bar-nilpotency}.
   979	
 succeeded in 51ms:
  1278	\]
  1279	which is the Jacobi identity for the structure constants extracted by residues. The implication is bidirectional: the Arnold relations \emph{are} the Jacobi identity via the residue dictionary. See Computation~\ref{comp:geom-alg-comparison-deg3} for the complete term-by-term verification in $\widehat{\mathfrak{sl}}_{2,k}$ and Theorem~\ref{thm:arnold-jacobi} for the general CFT formulation.
  1280	\end{remark}
  1281	
  1282	\begin{corollary}[Cohomology of configuration spaces {\cite{Arnold69}}; \ClaimStatusProvedElsewhere]\label{cor:cohomology-config}
  1283	The cohomology ring $H^*(C_n(\mathbb{C}); \mathbb{Q})$ of the open configuration space is:
  1284	\[H^*(C_n(\mathbb{C})) \cong \mathbb{Q}[\eta_{ij} : 1 \leq i < j \leq n] / \mathcal{I}_{\text{Arnold}}\]
  1285	where $\mathcal{I}_{\text{Arnold}}$ is the ideal generated by Arnold relations.
  1286	\end{corollary}
  1287	
  1288	\begin{proof}
  1289	By Arnol'd~\cite{Arnold69}, the 1-forms $\eta_{ij} = d\log(z_i - z_j)$ generate $H^*(C_n(\mathbb{C}); \mathbb{Q})$ and satisfy the Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$. That these generate \emph{all} relations follows from Cohen's computation of $H^*(C_n(\mathbb{C}))$ as the cohomology of the Arnol'd--Brieskorn braid arrangement complement~\cite{Coh76}. See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph.
  1290	\end{proof}
  1291	
  1292	\subsection{Low-degree explicit computations}
  1293	
  1294	\subsubsection{Degree 0: the vacuum}
  1295	
  1296	\begin{computation}[Degree 0; \ClaimStatusProvedHere]\label{comp:deg0}
 succeeded in 51ms:
  1748	\[
  1749	\omega_g(z,w) = d_z d_w \log E(z,w) = \text{Bergman kernel}
  1750	\]
  1751	and introduces a global sign error in the higher-genus bar complex
  1752	$\bar{B}^{(g,n)}(\cA)$ for $g \geq 1$.
  1753	
  1754	\subsection{Pitfall 12: the Borcherds identity and $d^2$}
  1755	
  1756	The Borcherds bracket-differential satisfies $d_{\mathrm{bracket}}^2 \neq 0$
  1757	in general (this is proved for all $2^{11} = 2048$ sign choices; see
  1758	\S\ref{sec:bar-nilpotency}). Nilpotency $d^2 = 0$ requires the
  1759	\emph{full} Borcherds differential, which includes both the bracket term
  1760	and the internal differential. Forgetting the internal differential, a
  1761	common error when translating from LV's purely algebraic setting to our
  1762	geometric one, breaks $d^2 = 0$.
  1763	
  1764	\emph{Explicit example.} For the affine algebra $\hat{\mathfrak{sl}}_2$ at level $k$,
  1765	the bar differential has:
  1766	\[
  1767	d^2[e|f|h] = d\bigl((-1)^0[ef|h] - (-1)^0[e|fh]\bigr)
 succeeded in 51ms:
     1	\chapter{Arnold relations}\label{app:arnold-relations}
     2	
     3	
     4	\section{Arnold relations: historical development and attribution}
     5	\label{sec:arnold-historical}
     6	\index{Arnold relations!detailed|textbf}
     7	
     8	\subsection{Historical context}
     9	
    10	Arnold~\cite{Arnold69} proved that $H^*(\mathrm{Conf}_n(\mathbb{C}), \mathbb{Z})$ is generated by classes $\eta_{ij}$ subject to
    11	\begin{equation}\label{eq:arnold-original}
    12	\eta_{ij} \eta_{jk} + \eta_{jk} \eta_{ki} + \eta_{ki} \eta_{ij} = 0
    13	\end{equation}
    14	for distinct $i, j, k$. Brieskorn~\cite{Brieskorn73} extended this to arbitrary hyperplane arrangements via the deletion-restriction exact sequence. The Orlik--Solomon theorem~\cite{OS80} gives the definitive algebraic form: $H^*(M(\mathcal{A}), \mathbb{Z}) \cong A(\mathcal{A})$, the exterior algebra on arrangement generators modulo Arnold relations.
    15	
    16	The connection to chiral algebras runs through Kontsevich's formality theorem~\cite{Kontsevich97} (configuration space integrals satisfying $d^2 = 0$ via Arnold relations), Beilinson--Drinfeld~\cite{BD04} (Arnold relations in the chiral bar construction), Costello--Gwilliam~\cite{CG17} (Arnold relations as locality in factorization algebras), and recent extensions to derived categories and higher genus~\cite{GLZ22, FG12}.
    17	
    18	\section{The Arnold relation and its proofs}
    19	
    20	\begin{theorem}[Arnold relations \cite{Arnold69}; \ClaimStatusProvedElsewhere]
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:master-sign\\}|\\\\label\\{ver:d2-degree3\\}|sec:bar-nilpotency' appendices/signs_and_shifts.tex chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '1248,1312p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_construction.tex:839:\subsection{\texorpdfstring{Proof that $d^2 = 0$: nine-term verification}{Proof that d2 = 0: nine-term verification}}\label{sec:bar-nilpotency-nine-terms-complete}\label{sec:bar-nilpotency}
appendices/signs_and_shifts.tex:576:\label{prop:master-sign}
appendices/signs_and_shifts.tex:607:\label{ver:d2-degree3}
appendices/signs_and_shifts.tex:978:For the explicit sign computations relevant to the bar differential, see the proof of $d^2 = 0$ in \S\ref{sec:bar-nilpotency}.
appendices/signs_and_shifts.tex:1758:\S\ref{sec:bar-nilpotency}). Nilpotency $d^2 = 0$ requires the
 succeeded in 52ms:
  1248	
  1249	\begin{example}[Explicit sign: two generators of odd degree]
  1250	Let $a, b \in \cA^1$ (cohomological degree~1). Then $|s^{-1}a| = 0$,
  1251	$|s^{-1}b| = 0$.
  1252	\begin{align*}
  1253	\text{Us:} &\quad d_{\mathrm{bar}}[a|b]
  1254	 = (-1)^{|a|-1}[a\cdot b] = (-1)^{0}[ab] = [ab]. \\
  1255	\text{LV:} &\quad d_1(sa\otimes sb)
  1256	 = (-1)^{|sa|}s(ab) = (-1)^{2}s(ab) = s(ab).
  1257	\end{align*}
  1258	Both give the unsigned product; the apparent sign $(-1)^2 = +1$ in LV
  1259	matches $(-1)^0 = +1$ in ours.
  1260	
  1261	Now let $a \in \cA^0$, $b \in \cA^1$:
  1262	\begin{align*}
  1263	\text{Us:} &\quad d_{\mathrm{bar}}[a|b]
  1264	 = (-1)^{|a|-1}[ab] = (-1)^{-1}[ab] = -[ab]. \\
  1265	\text{LV:} &\quad d_1(sa\otimes sb)
  1266	 = (-1)^{|sa|}s(ab) = (-1)^{1}s(ab) = -s(ab).
  1267	\end{align*}
exec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '560,620p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   560	d_\Omega(s^{-1}c_1 \otimes s^{-1}c_2) &= d_\Omega(s^{-1}c_1) \otimes s^{-1}c_2
   561	 + (-1)^{|s^{-1}c_1|} s^{-1}c_1 \otimes d_\Omega(s^{-1}c_2) \\
   562	&= \Bigl( -s^{-1}(dc_1) - \sum (-1)^{|c_1'|} s^{-1}c_1' \otimes s^{-1}c_1'' \Bigr) \otimes s^{-1}c_2 \\
   563	&\quad + (-1)^{|c_1|-1} s^{-1}c_1 \otimes \Bigl( -s^{-1}(dc_2) - \sum (-1)^{|c_2'|} s^{-1}c_2' \otimes s^{-1}c_2'' \Bigr)
   564	\end{align*}
   565	
   566	Expanding:
   567	\begin{align*}
   568	d_\Omega(s^{-1}c_1 \otimes s^{-1}c_2) &= -s^{-1}(dc_1) \otimes s^{-1}c_2 \\
   569	&\quad - \sum (-1)^{|c_1'|} s^{-1}c_1' \otimes s^{-1}c_1'' \otimes s^{-1}c_2 \\
   570	&\quad + (-1)^{|c_1|} s^{-1}c_1 \otimes s^{-1}(dc_2) \\
   571	&\quad + (-1)^{|c_1|} \sum (-1)^{|c_2'|} s^{-1}c_1 \otimes s^{-1}c_2' \otimes s^{-1}c_2''
   572	\end{align*}
   573	\end{computation}
   574	
   575	\begin{proposition}[Master sign formula {\cite{LV12}}; \ClaimStatusProvedElsewhere]
   576	\label{prop:master-sign}
   577	For the bar complex of an $\Ainf$-algebra $(A, \{m_n\})$, the full differential 
   578	on $[a_1|\cdots|a_n]$ is:
   579	\[
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1188,1210p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{app:curved-ainfty-formulas\\}' appendices/general_relations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1188	\[\text{Res}_{D_{23}}[\eta_{12} \wedge \eta_{23}] = m_2(a,m_2(b,c))\]
  1189	\[\text{Res}_{D_{123}}[\eta_{12} \wedge \eta_{23}] = m_3(a,b,c)\]
  1190	\item The difference of boundary residues equals an exact form:
  1191	\[m_2(m_2 \otimes \text{id}) - m_2(\text{id} \otimes m_2) = d(h_3)\]
  1192	where $h_3$ is the homotopy between associations
  1193	\end{itemize}
  1194	\end{example}
  1195	
  1196	\subsubsection{\texorpdfstring{Complete $A_\infty$ structure from configuration spaces}{Complete A-infinity structure from configuration spaces}}
  1197	
  1198	\begin{definition}[\texorpdfstring{$A_\infty$}{A-infinity} algebra]\label{def:a-infinity-complete}
  1199	An $A_\infty$ algebra consists of a graded vector space $A$ with operations $m_k: A^{\otimes k} \to A[2-k]$ for $k \geq 1$ satisfying (cf.\ Appendix~\ref{app:curved-ainfty-formulas}):
  1200	\[\sum_{\substack{r+s+t=n \\ r,t \geq 0,\; s \geq 1}} (-1)^{rs+t}\, m_{r+1+t}(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}) = 0\]
  1201	
  1202	Explicitly for small $k$:
  1203	\begin{align}
  1204	k=1: &\quad m_1 \circ m_1 = 0 \quad \text{($m_1$ is a differential)} \\
  1205	k=2: &\quad m_1(m_2) = m_2(m_1 \otimes 1) + m_2(1 \otimes m_1) \quad \text{(Leibniz rule)} \\
  1206	k=3: &\quad m_2(m_2 \otimes 1) - m_2(1 \otimes m_2) = m_1(m_3) + m_3(m_1 \otimes 1 \otimes 1) + \cdots
  1207	\end{align}
 succeeded in 51ms:
98:\label{app:curved-ainfty-formulas}
exec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '1,50p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{Geometric dictionary}
     2	\label{app:geometric-dictionary}
     3	
     4	Each entry represents a precise mathematical correspondence, not merely an analogy, between three languages: the physical (conformal field theory and operator products), the algebraic (operads and homological algebra), and the geometric (configuration spaces and residues).
     5	
     6	\begin{center}
     7	\begin{tabular}{|l|l|}
     8	\hline
     9	\textbf{Algebraic Structure} & \textbf{Geometric Realization} \\
    10	\hline
    11	Chiral multiplication & Residues at collision divisors \\
    12	Central extensions & Curved $A_\infty$ structures \\
    13	Conformal weights & Pole orders in residue extraction \\
    14	Normal ordering & NBC basis choice \\
    15	BRST cohomology & Spectral sequence pages \\
    16	Operator product expansion & Logarithmic form singularities \\
    17	Jacobi identity & Arnold--Orlik--Solomon relations \\
    18	Module categories & D-module pushforward \\
    19	Koszul duality & Orthogonality under residue pairing \\
    20	Vertex operators & Sections over configuration spaces \\

thinking
**Inspecting file structure**

I noticed that the general_relations appendix has multiple chapters bundled into one file, which seems a bit odd. I’m curious about this arrangement. I also spotted the `app:curved-ainfty-formulas` label at line 98, so I think it makes sense to take a closer look around that area. There might be some interesting insights or explanations to uncover regarding how the content is organized!
exec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '88,124p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    88	 
    89	\emph{General $n$.} The cohomology ring $H^*(C_n(\mathbb{C}))$ is the quotient of the
    90	exterior algebra $\bigwedge^* \mathbb{C}^{\binom{n}{2}}$ (generated by classes $\eta_{ij}$ in degree~1)
    91	by the ideal generated by $\binom{n}{3}$ quadratic Arnold relations (one for each triple $i < j < k$).
    92	The Poincar\'{e} polynomial is $\prod_{i=0}^{n-1}(1 + it)$, so
    93	$\dim H^k(C_n(\mathbb{C})) = |s(n, n-k)|$ (unsigned Stirling numbers of the first kind)
    94	and the total Betti number is $n!$.
    95	
    96	
    97	\chapter{\texorpdfstring{Curved $A_\infty$ relations: complete formulas}{Curved A infty relations: complete formulas}}
    98	\label{app:curved-ainfty-formulas}
    99	
   100	For reference, we collect the complete curved $A_\infty$ relations. An $A_\infty$ algebra 
   101	$(\mathcal{A}, \{m_k\}_{k \geq 0}, \mu_0)$ satisfies:
   102	
   103	\emph{$n = 0$.} (Curvature is a cycle.)
   104	\[m_1(\mu_0) = 0\]
   105	
   106	\emph{$n = 1$.} (Failure of strict nilpotence.)
   107	\[m_1^2 = m_2(\mu_0 \otimes \text{id}) - m_2(\text{id} \otimes \mu_0)\]
exec
/bin/zsh -lc "rg -n '\\\\label\\{app:signs\\}|\\\\label\\{app:sign-conventions\\}|\\\\label\\{sec:sign-dictionary-complete\\}' appendices/signs_and_shifts.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2:\label{app:signs}
713:\label{app:sign-conventions}
1012:\label{sec:sign-dictionary-complete}


thinking
**Exploring theory references**

I'm thinking about introducing a theory that cites appendix chapters, which might be okay, but I'm curious about how to handle references. Perhaps I can search for labels specific to the appendix that are linked to labels in the theory itself, especially if the target block contains `\ref{...}`. That could indicate the target isn't entirely self-contained. So, I guess I need to look into that!
thinking
**Evaluating proof structure**

I’m wondering if a theorem with proof elsewhere, or a proposition claiming "proof via theorem X," could lead to circular reasoning. I'll consider what this means for my script. It seems I need to identify line types and environments. A simple extraction of label lines and nearby lines might work. Using regex could make it easier. I’ll look for labels in appendix references and check the surrounding lines for any `\ref` to theory-only labels.
codex
I’ve ruled out one tempting false positive: the giant `ordered_associative` label collision is mostly dead surface because the appendix copy is not included in `main.tex`. I’m now filtering for the sharper class: appendix labels that theory depends on but whose own local block points back into theory, which is where real circularity or hollow citations show up.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only,%thy_only); for my "'$f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; my @lines=<$fh>; for my $i (0..$#lines){ while($lines[$i] =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1} = [$f,$i+1]; } } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; %thy_only = map { $_=>1 } grep { !exists $app{$_} } keys %theory; my %used; for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ $used{$l}=1 if $app_only{$l}; } } } } for my $l (sort keys %used){ my ($f,$ln) = @{$app{$l}}; open my $fh, q{<}, $f or die $!; my @lines=<$fh>; my $start = $ln-1; $start = 0 if $start<0; my $end = $ln+25; $end = $#lines if $end>$#lines; my %back; for my $i ($start..$end){ while($lines[$i] =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$r (split /'"\\s*,\\s*/, "'$1){ $back{$r}=1 if $thy_only{$r}; } } } next unless %back; print "$f:$ln:$l => ", join(q{, }, sort keys %back), qq{'"\\n}; }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/branch_line_reductions.tex:2:app:branch-line-reductions => thm:mc2-full-resolution, thm:modular-characteristic, thm:spectral-characteristic, thm:universal-theta
appendices/homotopy_transfer.tex:2:app:homotopy-transfer => thm:bar-ainfty-complete, thm:rectification-meta
appendices/koszul_reference.tex:2:app:koszul-reference => app:koszul_higher_genus, thm:extended-koszul
appendices/nonlinear_modular_shadows.tex:2:app:nonlinear-modular-shadows => thm:mc2-bar-intrinsic, thm:recursive-existence
appendices/combinatorial_frontier.tex:469:conj:w3-bar-gf => def:shadow-postnikov-tower, thm:mc2-bar-intrinsic
appendices/arnold_relations.tex:164:cor:bar-d-squared-zero-arnold => sec:genus-2-complete, sec:genus-3-complete, thm:arnold-genus1, thm:arnold-higher-genus, thm:arnold-quantum, thm:bar-nilpotency-complete
appendices/notation_index.tex:342:def:bar-complex-algebraic => def:factorization-algebra-AF, def:geometric-bar, thm:bar-coalgebra, thm:bar-factorization-homology, thm:chiral-factorization, thm:residue-operations
appendices/homotopy_transfer.tex:61:sec:ainfty-historical => chap:higher-genus
appendices/homotopy_transfer.tex:524:thm:bar-cobar-htt => thm:bar-cobar-isomorphism-main
appendices/nonlinear_modular_shadows.tex:2191:thm:nms-finite-termination => thm:mc2-bar-intrinsic

thinking
**Inspecting theorem status**

I need to check the status of certain theories, especially regarding whether any proofs depend on appendix-only theorems that might be conjectural or already proved. This is important because if a proof relies on an appendix conjecture, that could lead to issues. I think I can automate the process by identifying appendix-only labels within a theory and checking their defined status. This might involve scripting to track those labels and see if they correspond with any claims made in the proof.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%app,%theory,%app_only); for my "'$f (glob q{appendices/*.tex}) { open my $fh, q{<}, $f or die $!; my @lines=<$fh>; for my $i (0..$#lines){ while($lines[$i] =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$app{$1}=[$f,$i+1]; } } } for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; local $/; my $t=<$fh>; while($t =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$theory{$1}=1 } } %app_only = map { $_=>1 } grep { !exists $theory{$_} } keys %app; my %used; for my $f (glob q{chapters/theory/*.tex}) { open my $fh, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh>){$ln++; while($line =~ /'"\\\\(?:[cC]?ref|eqref|autoref|nameref)\\{(["'^}]+)'"\\}/g){ for my "'$l (split /'"\\s*,\\s*/, "'$1){ push @{$used{$l}}, "$f:$ln" if $app_only{$l}; } } } } for my $l (sort keys %used){ my ($f,$ln) = @{$app{$l}}; open my $fh, q{<}, $f or die $!; my @lines=<$fh>; my $start=$ln-3; $start=0 if $start<0; my $end=$ln+4; $end=$#lines if $end>$#lines; my $snippet=join q{}, @lines[$start..$end]; my $env=q{}; if($snippet =~ /'"\\\\begin\\{(["'^}]+)'"\\}/){ "'$env=$1; } my $status=q{}; if($snippet =~ /(ClaimStatus(?:ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open))/){ $status=$1; } print "$l'"\\t"'$f:$ln'"\\t"'$env'"\\t"'$status'"\\t\", scalar(@{"'$used{$l}}), qq{'"\\n}; }'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
app:arnold-relations	appendices/arnold_relations.tex:1			1
app:branch-line-reductions	appendices/branch_line_reductions.tex:2			3
app:combinatorial-frontier	appendices/combinatorial_frontier.tex:2			2
app:curved-ainfty-formulas	appendices/general_relations.tex:98			1
app:homotopy-transfer	appendices/homotopy_transfer.tex:2			6
app:koszul-reference	appendices/koszul_reference.tex:2	remark		1
app:nonlinear-modular-shadows	appendices/nonlinear_modular_shadows.tex:2			15
app:sign-conventions	appendices/signs_and_shifts.tex:713			7
app:signs	appendices/signs_and_shifts.tex:2			12
comp:bp-shadow-tower	appendices/nonlinear_modular_shadows.tex:3924	computation		1
conj:w3-bar-gf	appendices/combinatorial_frontier.tex:469	conjecture	ClaimStatusConjectured	3
constr:bipartite-linfty-truncation	appendices/nonlinear_modular_shadows.tex:3012	construction		1
constr:transfer-ainf	appendices/homotopy_transfer.tex:179	construction		3
cor:bar-d-squared-zero-arnold	appendices/arnold_relations.tex:164	corollary	ClaimStatusProvedHere	1
cor:nms-betagamma-mu-vanishing	appendices/nonlinear_modular_shadows.tex:1167	corollary	ClaimStatusProvedHere	5
def:bar-complex-algebraic	appendices/notation_index.tex:342	definition		1
def:nms-modular-quartic-resonance-class	appendices/nonlinear_modular_shadows.tex:1734	definition		1
eq:qme-cg	appendices/signs_and_shifts.tex:1385	equation		1
lem:nms-euler-inversion	appendices/nonlinear_modular_shadows.tex:3555	lemma	ClaimStatusProvedHere	2
lem:sdr-existence	appendices/homotopy_transfer.tex:146	lemma	ClaimStatusProvedHere	1
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3498,3524p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/koszul_reference.tex | sed -n '252,286p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3498	$\widehat{\mathcal{C}}$, producing three distinct objects \begin{itemize}
  3499	\item \textbf{Cobar}: $\Omega(\widehat{\mathcal{C}})$ recovers the
  3500	 \emph{original} algebra $\cA$ when
  3501	 $\widehat{\mathcal{C}} = \barB(\cA)$.
  3502	\item \textbf{Verdier dual}:
  3503	 $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \cA^!_\infty$
  3504	 produces the homotopy Koszul dual \emph{algebra}; equivalently,
  3505	 $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \barB(\cA^!)$
  3506	 as factorization coalgebras
  3507	 \textup{(}Convention~\ref{conv:bar-coalgebra-identity}\textup{)}.
  3508	 These are two descriptions of the same object: the
  3509	 identification of $\cA^!_\infty$ with $\barB(\cA^!)$ is the content
  3510	 of Theorem~A.
  3511	\end{itemize}
  3512	
  3513	\emph{Step 1: Check necessary conditions}
  3514	(Theorem~\ref{thm:essential-image-koszul}):
  3515	\begin{itemize}
  3516	\item[$\square$] Conilpotent? ($\bigcap_n \text{coker}(\Delta^n) = 0$)
  3517	\item[$\square$] Connected? ($\epsilon\colon \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}$)
 succeeded in 51ms:
   252	
   253	\begin{question}[Inverse problem]\label{q:inverse-problem-koszul}
   254	Given a chiral coalgebra $\widehat{\mathcal{C}}$, when does there exist a chiral 
   255	algebra $\mathcal{A}$ such that:
   256	\[\widehat{\mathcal{C}} \cong \mathcal{A}^!\]
   257	(as Koszul dual)?
   258	
   259	Equivalently: what is the \emph{essential image} of the Koszul duality functor?
   260	\end{question}
   261	
   262	\begin{remark}\label{rem:why-essential-image-matters}
   263	The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
   264	\end{remark}
   265	
   266	\subsection{Main characterization theorem}
   267	
   268	\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
   269	A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
   270	$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:
   271	
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:bar-cobar-inversion-qi\\}|\\\\label\\{thm:essential-image-koszul\\}|essential image' chapters/theory/bar_cobar_adjunction_inversion.tex appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/koszul_reference.tex:8:tables and the essential image characterization; the core definitions
appendices/koszul_reference.tex:259:Equivalently: what is the \emph{essential image} of the Koszul duality functor?
appendices/koszul_reference.tex:263:The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
appendices/koszul_reference.tex:268:\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
chapters/theory/bar_cobar_adjunction_inversion.tex:1613:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it]\label{thm:bar-cobar-inversion-qi}

thinking
**Checking theorem citations**

I need to inspect the proof of the essential-image theorem to see if it cites back to the main theorem. It's important to establish whether the proof is properly supported by the main theorem it refers to. I want to ensure everything aligns appropriately because clarity and accuracy are key! Let’s get started on analyzing the proof and its connections to the main theorem.
exec
/bin/zsh -lc "nl -ba appendices/koszul_reference.tex | sed -n '268,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   268	\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
   269	A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
   270	$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:
   271	
   272	\begin{enumerate}
   273	\item \emph{Conilpotency.} $\widehat{\mathcal{C}}$ is conilpotent: every element of $\ker(\epsilon)$ is annihilated by a sufficiently high iterate of the reduced coproduct $\bar{\Delta}$:
   274	 \[\ker(\epsilon) = \bigcup_{n \geq 0} \ker(\bar{\Delta}^{(n)})\]
   275	 
   276	\item \emph{Connected.} The counit is surjective onto the ground field:
   277	 \[\epsilon: \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}\]
   278	 
   279	\item \emph{Geometric representability.} $\widehat{\mathcal{C}}$ admits a presentation as sections of a $\mathcal{D}_X$-module coalgebra on the Ran space of~$X$; equivalently, there exists a factorization coalgebra~$\mathcal{F}$ such that $\widehat{\mathcal{C}} \simeq \Gamma(\mathrm{Ran}(X),\, \mathcal{F})$, compatible with the operadic structure of the Fulton--MacPherson compactification
   280	 
   281	\item \emph{Curvature centrality.} Any curvature term $\mu_0 \in \widehat{\mathcal{C}}^2$ (degree-$2$ component)
   282	 is central in the dual algebra
   283	 
   284	\item \emph{Formal completeness.} $\widehat{\mathcal{C}}$ is complete with respect 
   285	 to its coaugmentation coideal
   286	\end{enumerate}
   287	

thinking
**Evaluating proof structure**

I think my proof outline is looking okay so far, as long as I’m careful not to reference the body too much. However, I’m starting to notice a potential issue with the theorem labels in the appendices, particularly "thm:arnold-iff-nilpotent" and how they might refer back to the body. I really want to be thorough, so I should inspect that carefully to avoid any confusion.
exec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '60,92p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '3818,3844p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    60	genus-$0$ tangent-space screen. For nested collisions
    61	($S_1 \subset S_2 \subset \cdots$), this iterates to produce
    62	screens within screens, each genus~$0$, giving the full boundary
    63	stratification by stable trees. Second, the logarithmic
    64	$1$-forms $\eta_{ij} = d\log(z_i - z_j)$ extend across the
    65	boundary as sections of
    66	$\Omega^1_{\overline{C}_n(X)}(\log D)$ and satisfy the
    67	\emph{Arnold relation}
    68	(Theorem~\ref{thm:arnold-relations}):
    69	\begin{equation}\tag{$\star$}
    70	\eta_{ij} \wedge \eta_{jk}
    71	+ \eta_{jk} \wedge \eta_{ki}
    72	+ \eta_{ki} \wedge \eta_{ij} = 0
    73	\qquad (i,j,k \text{ distinct}).
    74	\end{equation}
    75	Third, this relation forces $d_{\mathrm{residue}}^2 = 0$
    76	(Theorem~\ref{thm:bar-nilpotency-complete}): the
    77	bar differential at degree~$2$ is a sum of double residues
    78	at pairs of collision divisors $D_{ij} \cap D_{jk}$, and
    79	the Arnold relation is the precise cancellation identity
 succeeded in 52ms:
  3818	Correctness follows from the residue formula in Theorem~\ref{thm:residue-operations}: nonzero contributions arise only when the weight condition is satisfied, corresponding to simple poles. The procedure checks all $\binom{n}{2}$ pairs, each in time $T_{\mathrm{OPE}}$.
  3819	\end{proof}
  3820	
  3821	\section{Arnold relations: explicit computations and physical interpretation}
  3822	\label{sec:arnold-three-proofs-comprehensive}
  3823	\label{sec:arnold-chiral}
  3824	
  3825	The Arnold relation (Theorem~\ref{thm:arnold-relations}) was proved
  3826	by two independent methods in \S\ref{sec:FM-compactification}: the
  3827	partial-fraction argument and the coordinate-reduction argument. Both
  3828	establish the relation in $\Omega^2(C_n(X))$ for every $n \geq 3$,
  3829	and Theorem~\ref{thm:arnold-iff-nilpotent} shows that the Arnold
  3830	relation is equivalent to $d_{\mathrm{residue}}^2 = 0$.
  3831	
  3832	% Labels preserved for cross-referencing from other chapters.
  3833	\label{prop:arnold-topological}%
  3834	\label{sec:arnold-proof-topological}%
  3835	\label{prop:nilpotency-arnold-comprehensive}%
  3836	
  3837	\subsection{\texorpdfstring{Explicit computations for $n = 3, 4, 5$}{Explicit computations for n = 3, 4, 5}}
exec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '156,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   156	The Arnold relations can be verified systematically for each triple $\{i,j,k\} \subset \{1,\ldots,n\}$:
   157	\begin{itemize}
   158	\item $n=3$: $\binom{3}{3} = 1$ relation (verified above)
   159	\item $n=4$: $\binom{4}{3} = 4$ relations (all follow from the $n=3$ case by restriction)
   160	\item $n=5$: $\binom{5}{3} = 10$ relations (similarly)
   161	\end{itemize}
   162	\end{remark}
   163	
   164	\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
   165	The Arnold relations ensure $d^2 = 0$ for the geometric bar differential:
   166	\[d^2 = \sum_{\text{cycles}} [\operatorname{Res}_{D_i}, \operatorname{Res}_{D_j}] = 0\]
   167	because the residue commutators sum to zero by Arnold relations.
   168	\begin{proof}
   169	This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
   170	\end{proof}
   171	\end{corollary}
   172	
   173	\subsection{Attribution}
   174	
   175	Arnold~\cite{Arnold69} discovered the relations (1969); Brieskorn~\cite{Brieskorn73} generalized to hyperplane arrangements; Orlik--Solomon~\cite{OS80} gave the definitive algebraic presentation; Beilinson--Drinfeld~\cite{BD04} recognized their role in the chiral bar construction. This work extends to all genera (Theorem~\ref{thm:arnold-higher-genus}) with quantum corrections (Theorem~\ref{thm:arnold-quantum}). Higher-genus corrections are computed explicitly at genus~$1$ (Theorem~\ref{thm:arnold-genus1}), genus~$2$ (Section~\ref{sec:genus-2-complete}), and genus~$3$ (Section~\ref{sec:genus-3-complete}). We follow Beilinson--Drinfeld in using the name ``Arnold relations.''
exec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '195,250p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   195	\begin{proof}
   196	\emph{(1) $\Rightarrow$ (3).}
   197	
   198	Start with the Arnold relation for forms:
   199	\[\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0\]
   200	
   201	Apply the residue operator $\text{Res}_{D_{ij}}$ to the whole relation. Since $\eta_{ij} = d\log(z_i - z_j)$ has a simple pole along $D_{ij}$ while $\eta_{jk}$ is smooth there, the residue of their wedge product is:
   202	\[\text{Res}_{D_{ij}}[\eta_{ij} \wedge \eta_{jk}] = \text{Res}_{D_{ij}}[\eta_{ij}] \cdot \eta_{jk}\big|_{D_{ij}} = 1 \cdot \eta_{jk}\big|_{D_{ij}} = \eta_{jk}\big|_{D_{ij}}\]
   203	(This is the standard formula: for a form $\omega = f\,d\log(t) \wedge \alpha$ with $\alpha$ smooth across $\{t=0\}$, one has $\text{Res}_{t=0}[\omega] = f|_{t=0} \cdot \alpha|_{t=0}$.)
   204	
   205	Similarly for the other terms. Applying $\text{Res}_{D_{ij}}$ to the Arnold relation yields:
   206	\[\eta_{jk}|_{D_{ij}} + \text{Res}_{D_{ij}}[\eta_{jk} \wedge \eta_{ki}] + 
   207	\text{Res}_{D_{ij}}[\eta_{ki} \wedge \eta_{ij}] = 0\]
   208	
   209	This is the required composition formula.
   210	
   211	\emph{(3) $\Rightarrow$ (2).}
   212	
   213	The square of $d_{\text{residue}}$ expands as:
   214	\[d_{\text{residue}}^2 = \sum_{i<j} \sum_{k<\ell} \text{Res}_{D_{ij}} \circ \text{Res}_{D_{k\ell}}\]


thinking
**Evaluating proof issues**

The proof doesn't reference the body theorem, which is a good sign—no cycles there. However, I’m noticing potential objective issues with omitted files and how appendix definitions are indexed. It seems like the appendix acts more as a summary than precise theorems. The user requested an audit, so I should verify findings against the actual contents. I might search build logs for unresolved references, perhaps using a targeted command for undefined references in the logs.
thinking
**Searching logs for verification**

I think it's useful to verify everything, so I should search the latest log for relevant information. I need to know the correct path to do this. Maybe I can use a command like `rg` in the repository to find references to `sl2-koszul-dual` in either the .aux or log files. Let's get started on that search! This will help me ensure everything is in order.
codex
I have one already re-verified build-surface bug in hand and I’m checking whether TeX logs corroborate it. In parallel I’m still looking for seam problems that are stronger than “appendix supplies background,” because I only want findings that survive an adversarial reread.
exec
/bin/zsh -lc "rg -n 'sl2-koszul-dual|undefined references|Undefined control sequence|Reference.*undefined' -g '*.log' -g '*.aux' -g '*.out' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\include\\{|\\\\input\\{' main.tex | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 6561

./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:459:LaTeX Warning: Reference `eq:genus-g-propagator' on page 1 undefined on input l
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:463:LaTeX Warning: Reference `eq:d-squared-curvature' on page 1 undefined on input 
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:480:LaTeX Warning: Reference `sec:mc' on page 2 undefined on input line 235.
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:486:LaTeX Warning: Reference `eq:verdier' on page 3 undefined on input line 271.
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:492:LaTeX Warning: Reference `eq:ahat-generating' on page 4 undefined on input line
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:496:LaTeX Warning: Reference `rem:multi-weight' on page 4 undefined on input line 3
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:503:LaTeX Warning: Reference `sec:five-theorems' on page 5 undefined on input line 
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:507:LaTeX Warning: Reference `ssec:d-squared' on page 5 undefined on input line 476
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:514:LaTeX Warning: Reference `eq:mc-equation' on page 6 undefined on input line 546
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:531:LaTeX Warning: There were undefined references.
./main.log:1836:LaTeX Warning: Reference `def:einf-chiral' on page 2 undefined on input line 83
./main.log:1840:LaTeX Warning: Reference `rem:En-terminology' on page 2 undefined on input line
./main.log:1858:LaTeX Warning: Reference `MK:modular' on page 3 undefined on input line 55.
./main.log:1870:LaTeX Warning: Reference `eq:preface-arnold' on page 4 undefined on input line 
./main.log:1893:LaTeX Warning: Reference `eq:preface-arnold' on page 6 undefined on input line 
./main.log:1902:LaTeX Warning: Reference `eq:pf1-borcherds' on page 6 undefined on input line 3
./main.log:1915:LaTeX Warning: Reference `prop:e1-nonsplitting-genus1' on page 10 undefined on 
./main.log:1966:LaTeX Warning: Reference `thm:e1-formality-bridge' on page 13 undefined on inpu
 succeeded in 51ms:
846:\include{chapters/frame/preface}
850: \input{chapters/frame/guide_to_main_results}
859:\include{chapters/theory/introduction}
874:\include{chapters/frame/heisenberg_frame}
963:\include{chapters/theory/fourier_seed}
970:\include{chapters/theory/algebraic_foundations}
976:\include{chapters/theory/three_invariants}
982:\include{chapters/theory/configuration_spaces}
988:\include{chapters/theory/bar_construction}
994:\include{chapters/theory/cobar_construction}
1002:% \include{chapters/theory/bar_cobar_adjunction}
1004:\input{chapters/theory/bar_cobar_adjunction_curved}
1005:\input{chapters/theory/bar_cobar_adjunction_inversion}
1010:\input{appendices/homotopy_transfer}
1022:\include{chapters/theory/poincare_duality}
1030:\include{chapters/theory/chiral_koszul_pairs}
1031:\include{chapters/theory/koszul_pair_structure}
1038:% \include{chapters/theory/higher_genus}
1040:\input{chapters/theory/higher_genus_foundations}
1041:\input{chapters/theory/higher_genus_complementarity}

thinking
**Investigating search output**

I see that the search output is huge, and main.log has many undefined references. I could consider including our sl2, but it seems the output got truncated before I could check if it’s necessary. I really need to find a specific reference in main.log to make sense of all this. It's a bit of a mess, but I’m determined to sort through it! Let's see what I can dig up.
exec
/bin/zsh -lc "rg -n 'sl2-koszul-dual' main.log" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Investigating log issues**

I think the lack of a match might be because main.log isn't showing the label name due to truncation. My search for "undefined on input line 2889" might not be yielding results for the same reason. However, just because it’s omitted doesn’t mean it’s not in the current log; perhaps the label is in the .aux file instead. I'll look at chiral_modules.aux for `thm:sl2-koszul-dual`.
exec
/bin/zsh -lc "rg -n 'sl2-koszul-dual' chapters/theory/chiral_modules.aux chapters/theory/*.aux main.aux" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: chapters/theory/chiral_modules.aux: No such file or directory (os error 2)
exec
/bin/zsh -lc "rg -n 'sl2-koszul-dual' -g '*.aux' ." in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba appendices/koszul_reference.tex | sed -n '1,24p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/existence_criteria.tex | sed -n '462,482p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1948,1966p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter[Ambient complementarity and nonlinear modular shadows]{Ambient complementarity, nonlinear modular shadows, and the quartic resonance class}
     2	\label{app:nonlinear-modular-shadows}
     3	
     4	The modular characteristic $\kappa(\cA)$ (Theorem~D) and the spectral
     5	discriminant~$\Delta_{\cA}$ are the linear face of a single ambient
     6	deformation problem. The ambient problem carries a $(-1)$-shifted
     7	symplectic form, and the two dual packages $\mathcal{Q}_g(\cA)$
     8	and~$\mathcal{Q}_g(\cA^{!})$ are complementary Lagrangians inside it.
     9	Their interaction produces an infinite nonlinear tower
    10	\[
    11	\kappa \;\longrightarrow\; \Delta \;\longrightarrow\;
    12	\mathfrak{C} \;\longrightarrow\; \mathfrak{Q}
    13	\;\longrightarrow\; \Theta,
    14	\]
    15	the \emph{shadow obstruction tower}: the sequence of finite-order
    16	projections $\Theta_\cA^{\leq r}$ of the universal MC element
    17	$\Theta_\cA \in \MC(\gAmod)$
    18	(Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
    19	is MC because $D_\cA^2 = 0$; all-degree convergence
    20	$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ by
 succeeded in 52ms:
  1948	\;\longrightarrow\;
  1949	\underbrace{[\mathfrak C_\cA],\;\mathfrak o_\cA^{(4)},\;
  1950	 [\mathfrak Q_\cA]}_{\text{nonlinear shadows}}
  1951	\;\longrightarrow\;
  1952	\underbrace{\Theta_\cA}_{\text{universal class}}.
  1953	\]
  1954	The scalar characteristic $\kappa(\cA)$ is proved. The spectral
  1955	discriminant $\Delta_\cA$ is proved. The cubic and quartic shadow
  1956	classes $[\mathfrak C_\cA]$ and $[\mathfrak Q_\cA]$ are the first
  1957	genuinely nonlinear modular invariants, computable on any family
  1958	where the cyclic deformation package is available through the
  1959	relevant order
  1960	(Chapter~\ref{app:nonlinear-modular-shadows}).
  1961	The branch-line reductions
  1962	(Appendix~\ref{app:branch-line-reductions}) extract exact
  1963	finite-dimensional quotients of this layer, including genus-$2$
  1964	transparency and the universal genus-$3$ constant~$7$ on the shared
  1965	$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.
  1966	For class~$\mathbf{M}$ algebras the infinite tower has a computable
 succeeded in 52ms:
     1	\chapter{Koszul duality reference tables}
     2	\label{app:koszul-reference}
     3	
     4	
     5	\begin{remark}[Relationship to \S\ref{app:koszul_higher_genus}]
     6	The genus-graded Koszul duality theory is developed in
     7	\S\ref{app:koszul_higher_genus}. This appendix provides reference
     8	tables and the essential image characterization; the core definitions
     9	and theorems are stated there and should not be duplicated. Where a
    10	result appears in both locations, the version in
    11	\S\ref{app:koszul_higher_genus} is canonical.
    12	\end{remark}
    13	
    14	\section{Genus-graded Koszul duality}
    15	
    16	\begin{theorem}[Extended Koszul duality; \ClaimStatusProvedElsewhere]
    17	\label{thm:extended-koszul-appendix}
    18	If $(\mathcal{A}, \mathcal{A}^!)$ form a genus-0 Koszul dual pair with central curvature at
    19	all genera, then under suitable finiteness and convergence conditions:
    20	\[\left(\bigoplus_{g \geq 0} \mathcal{A}^{(g)}, \bigoplus_{g \geq 0} (\mathcal{A}^!)^{(g)}\right)\]
 succeeded in 52ms:
   462	\textbf{Chiral Algebra} & \textbf{Quadratic?} & \textbf{Has Dual?} & \textbf{Comments} \\
   463	\hline
   464	Heisenberg $\mathcal{H}$ & Yes & Yes & Primitive coalgebra \\
   465	\hline
   466	$\widehat{\mathfrak{g}}_k$ (Kac--Moody) & Yes & Yes (generic $k$) & See Prop.~\ref{prop:kac-moody-koszul-duals} \\
   467	\hline
   468	Virasoro $\text{Vir}$ & No & Yes (completion) & $I$-adic completion \\
   469	\hline
   470	$\mathcal{W}_3$ & No & Yes (all $c$, completed) & Strict Koszul at $c = -2$ only \\
   471	\hline
   472	$\mathcal{W}_N$ ($N < \infty$) & No & Sometimes & Depends on $(N, c)$ \\
   473	\hline
   474	$\mathcal{W}_{1+\infty}$ & No & Yes (completed) & Filtered; see Appendix~\ref{app:koszul-reference} \\
   475	\hline
   476	$\mathcal{W}_\infty$ & No & Yes (completion) & Weight stabilization; no strict finite-stage dual \\
   477	\hline
   478	Free fermion ($bc$ ghosts) & Yes & Yes & Exterior coalgebra \\
   479	\hline
   480	$\mathfrak{gl}_n$ current & Yes & Yes & Matrix coalgebra \\
   481	\hline

thinking
**Filtering duplicates**

I’ve identified 311 duplicates, mostly in some ordered way. Now, I need to filter through the included appendices while leaving out the ordered associative ones. To do this efficiently, I'll use a script that handles the filtering for me. I want to ensure I don't miss any important details while organizing this data. It's all about streamlining the process! Let’s get to it!
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %inc; open my "'$fh, q{<}, q{main.tex} or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\(?:input|include)\\{(["'^}]+)'"\\}/g){ my "'$p=$1; $p.=q{.tex} unless $p =~ /'"\\.tex"'$/; $inc{$p}=1; } } my (%app,%theory); for my $f (grep { $inc{$_} } glob q{appendices/*.tex}) { open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$app{$1}}, "$f:$ln"; } } } for my $f (glob q{chapters/theory/*.tex}) { next unless $inc{$f}; open my $fh2, q{<}, $f or die $!; my $ln=0; while(my $line=<$fh2>){$ln++; while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$theory{$1}}, "$f:$ln"; } } } my @dup = sort grep { exists $app{$_} && exists $theory{$_} } keys %app; print scalar(@dup), qq{'"\\n}; for my "'$l (@dup){ print "$l'"\\n  APP @{"'$app{$l}}'"\\n  THY @{"'$theory{$l}}'"\\n\"; }'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
0
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '496,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '160,170p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   496	\end{definition}
   497	
   498	\begin{theorem}[\texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations;
   499	\ClaimStatusProvedHere]
   500	\label{thm:e2-d-squared}
   501	\index{Totaro relations!and $d^2 = 0$}
   502	The differential $d_{\Etwo}$ of
   503	Definition~\textup{\ref{def:e2-bar-complex}} satisfies
   504	$d_{\Etwo}^2 = 0$.
   505	\end{theorem}
   506	
   507	\begin{proof}
   508	The proof follows the same structure as the chiral case
   509	(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
   510	relations replaced by Totaro relations.
   511	
   512	We compute $d_{\Etwo}^2$ on a bar element
   513	$\alpha \in \Omega^*(\overline{\Conf}_k(\bR^2))
   514	\otimes (s^{-1} \bar{A})^{\otimes k}$.
   515	The square decomposes into three terms:
 succeeded in 51ms:
   160	\item $n=5$: $\binom{5}{3} = 10$ relations (similarly)
   161	\end{itemize}
   162	\end{remark}
   163	
   164	\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
   165	The Arnold relations ensure $d^2 = 0$ for the geometric bar differential:
   166	\[d^2 = \sum_{\text{cycles}} [\operatorname{Res}_{D_i}, \operatorname{Res}_{D_j}] = 0\]
   167	because the residue commutators sum to zero by Arnold relations.
   168	\begin{proof}
   169	This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
   170	\end{proof}
exec
/bin/zsh -lc "rg -n 'cor:bar-d-squared-zero-arnold' chapters/theory/en_koszul_duality.tex appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:509:(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
appendices/arnold_relations.tex:164:\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}

thinking
**Evaluating theorem proof reliance**

I think there's an issue with the theorem e2-d-squared. It states that its proof follows the same structure as the chiral case, but the corollary mentions the theory's content as theorem bar-nilpotency-complete. The en_koszul_duality proof uses it merely as an analogy. I'm considering whether it truly relies on the corollary, or if it's just organizational. I should inspect the proof further to see if it's strong enough on its own.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '507,560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   507	\begin{proof}
   508	The proof follows the same structure as the chiral case
   509	(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
   510	relations replaced by Totaro relations.
   511	
   512	We compute $d_{\Etwo}^2$ on a bar element
   513	$\alpha \in \Omega^*(\overline{\Conf}_k(\bR^2))
   514	\otimes (s^{-1} \bar{A})^{\otimes k}$.
   515	The square decomposes into three terms:
   516	\[
   517	d_{\Etwo}^2
   518	\;=\;
   519	\underbrace{d_{\mathrm{dR}}^2}_{= 0}
   520	\;+\;
   521	\underbrace{[d_{\mathrm{dR}},\, d_{\mathrm{res}}]}_{(\star)}
   522	\;+\;
   523	\underbrace{d_{\mathrm{res}}^2}_{(\star\star)},
   524	\]
   525	where $d_{\mathrm{res}} = \sum_S \Res_{\partial_S}(G_S \wedge \mu_S)$.
   526	

thinking
**Identifying notation inconsistencies**

I'm noticing a potential inconsistency in the theory definition regarding the use of uncurved A∞ and citations to appendix sections that use curved formulas and extra symbols like `\mu_0`. It feels like a seam gap might exist here. I have a couple of options to address this: either focus on the uncurved section or rename notation in the appendix to align consistently. It looks like there's conflicting usage of `m_0` and `\mu_0` throughout, especially in the appendix. I need to ensure the lines match exactly.
codex
I’ve found a second seam candidate that is not just structural: the core theory points to the curved `A_\infty` appendix for formulas, but that appendix switches curvature notation from `m_0` to `\mu_0` inside the very package being cited. I’m checking whether that inconsistency is isolated or repeated before I keep it.
exec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '97,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mu_0|m_0' chapters/theory/higher_genus_foundations.tex appendices/general_relations.tex appendices/signs_and_shifts.tex appendices/notation_index.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    97	\chapter{\texorpdfstring{Curved $A_\infty$ relations: complete formulas}{Curved A infty relations: complete formulas}}
    98	\label{app:curved-ainfty-formulas}
    99	
   100	For reference, we collect the complete curved $A_\infty$ relations. An $A_\infty$ algebra 
   101	$(\mathcal{A}, \{m_k\}_{k \geq 0}, \mu_0)$ satisfies:
   102	
   103	\emph{$n = 0$.} (Curvature is a cycle.)
   104	\[m_1(\mu_0) = 0\]
   105	
   106	\emph{$n = 1$.} (Failure of strict nilpotence.)
   107	\[m_1^2 = m_2(\mu_0 \otimes \text{id}) - m_2(\text{id} \otimes \mu_0)\]
   108	
   109	\emph{$n = 2$.} (Associativity with curvature corrections.)
   110	\begin{multline}
   111	m_1 m_2 - m_2(m_1 \otimes \text{id}) - m_2(\text{id} \otimes m_1) + m_3(\mu_0 \otimes \text{id} 
   112	\otimes \text{id}) \\
   113	- m_3(\text{id} \otimes \mu_0 \otimes \text{id}) + m_3(\text{id} \otimes \text{id} \otimes \mu_0) = 0
   114	\end{multline}
   115	
   116	\emph{$n = 3$.} (Higher coherences.)
 succeeded in 50ms:
appendices/general_relations.tex:28:Each entry represents a precise functor or natural transformation between categories. For instance, the correspondence ``Chiral multiplication $\leftrightarrow$ Residues at collision divisors'' is the content of Theorem~\ref{thm:residue-formula}, establishing that the multiplication map factors through the residue homomorphism. Similarly, ``Central extensions $\leftrightarrow$ Curved $A_\infty$ structures'' reflects Theorem~\ref{thm:heisenberg-bar}, showing how the failure of strict associativity due to central charges is precisely captured by the curvature term $m_0$.
appendices/general_relations.tex:101:$(\mathcal{A}, \{m_k\}_{k \geq 0}, \mu_0)$ satisfies:
appendices/general_relations.tex:104:\[m_1(\mu_0) = 0\]
appendices/general_relations.tex:107:\[m_1^2 = m_2(\mu_0 \otimes \text{id}) - m_2(\text{id} \otimes \mu_0)\]
appendices/general_relations.tex:111:m_1 m_2 - m_2(m_1 \otimes \text{id}) - m_2(\text{id} \otimes m_1) + m_3(\mu_0 \otimes \text{id} 
appendices/general_relations.tex:113:- m_3(\text{id} \otimes \mu_0 \otimes \text{id}) + m_3(\text{id} \otimes \text{id} \otimes \mu_0) = 0
appendices/general_relations.tex:125:If $\mu_0 \in Z(\mathcal{A})$ (i.e., $m_2(\mu_0 \otimes a) = m_2(a \otimes \mu_0)$ for all $a$), then the $n=1$ relation gives:
appendices/general_relations.tex:126:\[m_1^2(a) = m_2(\mu_0, a) - m_2(a, \mu_0) = 0\]
appendices/signs_and_shifts.tex:1311:\emph{Curved case.} When $m_0 \neq 0$, the $A_\infty$ relation at $n=1$ becomes
appendices/signs_and_shifts.tex:1312:$m_1^2(a) = m_2(m_0, a) - m_2(a, m_0) = [m_0, a]$ (commutator with the curving element).
appendices/signs_and_shifts.tex:1545:Curvature & implicit & $F_\nabla = d\nabla + \nabla^2$ & $m_0$ & $\kappa(\cA)$ \\
appendices/signs_and_shifts.tex:1547:Curved $A_\infty$ relation & N/A & $m_1^2 = [m_0,-]$ & $m_1^2 = [m_0,-]$ & $m_1^2(a)=[m_0,a]$ \\
chapters/theory/higher_genus_foundations.tex:1926:\item $m_0 \in \mathcal{A}^2$ is the \emph{curvature element} (a nullary operation producing a degree-2 element)
chapters/theory/higher_genus_foundations.tex:1927:\item The $A_\infty$ relations hold for all $n \geq 0$: $\sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(\text{id}^{\otimes r} \otimes m_s \otimes \text{id}^{\otimes t}) = 0$, now including $s = 0$ terms involving $m_0$
chapters/theory/higher_genus_foundations.tex:1928:\item In particular, $m_1(m_0) = 0$ (curvature is a cocycle) and $m_1^2 = [m_0, -]$ (failure of strict nilpotence)
chapters/theory/higher_genus_foundations.tex:1943:\item Curvature element $m_0^{(g)} = \kappa(\cA) \cdot \omega_g$,
chapters/theory/higher_genus_foundations.tex:1947: $m_1^{(g)} \circ m_1^{(g)} = [m_0^{(g)}, -]$, i.e.,
chapters/theory/higher_genus_foundations.tex:1977:The absence of a simple pole gives $m_2(J \otimes J) = 0$, curvature $\kappa(\mathcal{H}_k) = k$, and modified differential $d_{\text{curved}} = d + k \cdot \mu_0$.
chapters/theory/higher_genus_foundations.tex:2510:$A_\infty$ structure with curvature $m_0 \neq 0$ controlled by the Arakelov form:
chapters/theory/higher_genus_foundations.tex:2511:\[m_0^{(2)} = \kappa \cdot \omega_{\mathrm{Ar}}^{(2)}\]

thinking
**Checking theory references**

I'm thinking about the references in `appendices/branch_line_reductions.tex`, like the theory `def:shadow-postnikov-tower`. There may be a mismatch with the definitions and the branch-line reductions. I should probably examine the top of the branch_line_reductions file closely since the theory introduces the appendix chapter label. Is there a chance there might be a circular or hollow issue here? I should check those top lines for clarity.
exec
/bin/zsh -lc "nl -ba appendices/branch_line_reductions.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter[Branch-line reductions and primitive modular characteristics]{Branch-line reductions, primitive modular characteristics, and the intrinsic invariant ladder}
     2	\label{app:branch-line-reductions}
     3	
     4	The full modular Maurer--Cartan element $\Theta_\cA$ lives in an
     5	infinite-dimensional convolution algebra. A \emph{branch-line
     6	reduction} restricts~$\Theta_\cA$ to a configuration of minimal
     7	complexity (two-point branch lines, rank-one spectral sectors,
     8	genus-$2$ transparency windows) and proves structural theorems
     9	inside the resulting finite-dimensional quotient.
    10	
    11	The \emph{primitive modular characteristics} are the irreducible
    12	components of~$\Theta_\cA$ under the clutching maps of
    13	$\overline{\mathcal{M}}_{g,n}$: they are to the shadow obstruction
    14	tower what primitive elements are to a Hopf algebra. The intrinsic
    15	invariant ladder
    16	\[
    17	\kappa(\cA)
    18	\rightsquigarrow
    19	\Delta_{\cA}(x)
    20	\rightsquigarrow
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '5968,6036p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1956,1966p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1956	classes $[\mathfrak C_\cA]$ and $[\mathfrak Q_\cA]$ are the first
  1957	genuinely nonlinear modular invariants, computable on any family
  1958	where the cyclic deformation package is available through the
  1959	relevant order
  1960	(Chapter~\ref{app:nonlinear-modular-shadows}).
  1961	The branch-line reductions
  1962	(Appendix~\ref{app:branch-line-reductions}) extract exact
  1963	finite-dimensional quotients of this layer, including genus-$2$
  1964	transparency and the universal genus-$3$ constant~$7$ on the shared
  1965	$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.
  1966	For class~$\mathbf{M}$ algebras the infinite tower has a computable
 succeeded in 52ms:
  5968	$\mathcal{M}_\cA$ or $\mathcal{M}_{\cA^!}$ as the zero
  5969	section. The change from one cotangent chart to the other
  5970	is the formal Legendre transform.
  5971	\end{evidence}
  5972	
  5973	\begin{remark}[Fake complementarity criterion]
  5974	\label{rem:fake-complementarity}
  5975	The complementarity potential $S_\cA$ detects genuine
  5976	complementarity: $S_\cA$ is quadratic if and only if the
  5977	dual Lagrangian $\mathcal{M}_{\cA^!}$ is linear in
  5978	formal Darboux coordinates, which holds if and only if the
  5979	derived critical locus $\mathrm{Crit}(S_\cA)$ is governed
  5980	entirely by its Hessian complex. The cubic and higher Taylor
  5981	coefficients of~$S_\cA$ are the first obstructions to fake
  5982	complementarity, the regime where an eigenspace splitting
  5983	mimics Lagrangian geometry without being one. The
  5984	Hessian $\mathrm{Hess}_0(S_\cA)$ is exactly the linear
  5985	complementarity isomorphism
  5986	$T_0\mathcal{M}_\cA \xrightarrow{\sim}
  5987	T_0\mathcal{M}_{\cA^!}^\vee[-1]$.


thinking
**Clarifying appendix labels**

I'm looking at the appendix top and it seems fine, but there's a potential inconsistency in the introduction using `Chapter\ref{app:nonlinear-modular-shadows}`, even though the appendix label prefix is `app`. Since appendices can be considered chapters, this might not be a problem. I could inspect specific labels from the chiral Hochschild-Koszul theory referencing appendix chapters. There could also be mislabeled theorem labels in the appendix. For example, the label `thm:extended-koszul` might be correct, but the references need checking to ensure they align properly.
thinking
**Examining appendix references**

I’m noticing that the appendix's theorem label is `thm:extended-koszul-appendix`, but it later references `Theorem\ref{thm:extended-koszul}` from the theory. This might be fine, but the body doesn’t cite the appendix theorem. The line in `existance_criteria.tex` pointing to Appendix\ref{app:koszul-reference} seems okay. I’ll need to check if there’s a notation mismatch between the definition of the bar complex in the index and the theory’s actual bar coalgebra theorem. I’ve found that the notation index doesn’t define it properly, which is an intriguing issue!
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '444,550p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4688,4732p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  4688	\end{remark}
  4689	
  4690	\begin{proposition}[\texorpdfstring{$E_2$}{E2}-collapse as formality;
  4691	\ClaimStatusProvedHere]
  4692	\label{prop:e2-collapse-formality}
  4693	\index{formality!spectral sequence collapse}
  4694	On the Koszul locus, the following conditions on a chiral algebra
  4695	$\cA$ are equivalent:
  4696	\begin{enumerate}[label=(\roman*)]
  4697	\item The bar spectral sequence
  4698	$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g\Bbar_g(\cA))$
  4699	collapses at~$E_2$ for all $g \geq 0$.
  4700	\item The filtered $\Ainf$-algebra $\Omega_g(\Bbar_g(\cA))$ is
  4701	\emph{formal}: quasi-isomorphic to its cohomology with the
  4702	transferred $\Ainf$-structure
  4703	(Theorem~\textup{\ref{thm:chiral-htt}}).
  4704	\item The transferred higher operations satisfy
  4705	$\tilde{m}_n^{(g)} = 0$ for $n \geq 3$ and all~$g$
  4706	(Koszulness at all genera).
  4707	\end{enumerate}
 succeeded in 51ms:
   444	\item $\tilde{\Delta}_3$ involves Massey products: corrections arise when $d_V$ is nontrivial.
   445	\item If $V$ is formal (quasi-isomorphic to $H_*(V)$ with zero differential), then $\tilde{\Delta}_n = 0$ for $n \geq 3$.
   446	\end{enumerate}
   447	\end{example}
   448	
   449	
   450	\section{Applications to chiral algebras}
   451	\label{sec:htt-chiral}
   452	
   453	
   454	\begin{theorem}[Chiral homotopy transfer; \ClaimStatusProvedHere]
   455	\label{thm:chiral-htt}
   456	\index{$A_\infty$-structure!transferred}
   457	Let $\cA$ be an $\Eone$-chiral algebra on a curve $X$ and suppose we have an 
   458	SDR of the underlying D-module:
   459	\[
   460	(\cA, H, p, \iota, h) \quad \text{with } H = H^{\mathrm{ch}}_*(\cA).
   461	\]
   462	Then:
   463	\begin{enumerate}[label=(\roman*)]

thinking
**Checking appendix labeling**

I'm considering a potential issue. In `chapters/theory/introduction.tex`, there's a reference to an appendix labeled as a "Chapter," which seems inconsistent. Appendices should probably be labeled as "Appendix," not "Chapter," unless styled as chapters. However, `main.tex` has appendices structured similarly to chapters. This could mean they’re numbered in a chapter-like format. I need to confirm if `\appendix` is used in `main.tex` to clarify how they're referenced. So, I'll search for `\appendix` there!
exec
/bin/zsh -lc "rg -n '\\\\appendix|\\\\appendixpage|\\\\appendixtitleon|\\\\appendixtitle' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '1584,1602p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1588:\appendix
 succeeded in 51ms:
  1584	% Reference material only: sign conventions, notation, relations,
  1585	% tables. Substantial mathematical content has been promoted to
  1586	% chapters in Parts II--III.
  1587	% ======================================================================
  1588	\appendix
  1589	
  1590	\input{appendices/general_relations}
  1591	\input{appendices/arnold_relations}
  1592	\input{appendices/signs_and_shifts}
  1593	\input{appendices/theta_functions}
  1594	\input{appendices/spectral_higher_genus}
  1595	\input{appendices/koszul_reference}
  1596	\ifannalsedition\else
  1597	 \input{appendices/dual_methodology}
  1598	\fi
  1599	\input{appendices/notation_index}
  1600	\ifannalsedition\else
  1601	 \input{appendices/computational_tables}
  1602	\fi

thinking
**Looking into appendix labeling**

I'm thinking that referring to the appendix as a Chapter is inconsistent. This might be a finding worth noting. I'll search for other theory files that use the "Chapter" label before "appendix." Using a tool for cross-references could help identify multiple low-severity findings that can be grouped together. It seems like a good approach to get a clearer picture, so let’s explore!
codex
The appendix/theory seam also has a plain citation-type consistency question now: `main.tex` switches into appendix mode at line `1588`, so any theory prose that says “Chapter” when pointing at `app:*` labels is mislabelled. I’m grepping that pattern across the seam rather than treating the introduction line as a one-off.
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\ref\\{app:|Chapter~\\\\textup\\{\\\\ref\\{app:|Chapter~\\\\Cref\\{app:|Chapter~\\\\cref\\{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_hochschild_koszul.tex:6009:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/theory/introduction.tex:1960:(Chapter~\ref{app:nonlinear-modular-shadows}).
exec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{ch:|Appendix~\\\\textup\\{\\\\ref\\{ch:|Appendix~\\\\Cref\\{ch:|Appendix~\\\\cref\\{ch:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering appendix references**

I'm thinking about whether using definitions from the appendix is acceptable if it extends concepts later on. However, if I reference it in the theory chapter, that might feel a bit odd. I guess I need to inspect line 28884 in the higher_genus_modular_koszul document to clarify. It seems important to ensure everything flows logically! Let's see what I find when I look into it further.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '28872,28896p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1728,1744p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 28872	 coalgebra;
 28873	\item $\Theta_L \in
 28874	 \MC(\Defcyc(L) \widehat\otimes \mathbb{G}_{\mathrm{mod}})$
 28875	 is the universal modular Maurer--Cartan class
 28876	 (Theorem~\ref{thm:mc2-bar-intrinsic});
 28877	\item $\mathcal{L}_L$ is the determinant line of the genus
 28878	 family;
 28879	\item $(V_L^{\mathrm{br}}, T_L^{\mathrm{br}})$ is the
 28880	 spectral branch object: a finite-rank complex with its
 28881	 genus-$1$ transport operator;
 28882	\item $\mathfrak{R}_4^{\mathrm{mod}}(L)$ is the quartic
 28883	 resonance class
 28884	 (Definition~\ref{def:nms-modular-quartic-resonance-class}).
 28885	\end{enumerate}
 28886	Every invariant of the theory (scalar anomaly, spectral
 28887	sheet, nonlinear resonance) is a successive shadow of one
 28888	universal class~$\Theta_L$.
 28889	\end{construction}
 28890	
 28891	\begin{theorem}[Cubic gauge triviality and canonical quartic class]
 succeeded in 52ms:
  1728	\in \Gamma\bigl(\overline{\mathcal M}_{g,n}\times B_{\cA}^{\circ},
  1729	\mathscr L_{4,g,n}^{\mathrm{res}}(\cA)\bigr).
  1730	\end{equation}
  1731	\end{construction}
  1732	
  1733	\begin{definition}[Modular quartic resonance class]
  1734	\label{def:nms-modular-quartic-resonance-class}
  1735	The \emph{modular quartic resonance class} of $\cA$ in genus $(g,n)$ is the Cartier divisor class
  1736	\begin{equation}
  1737	\label{eq:nms-modular-resonance-class}
  1738	\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)
  1739	:=
  1740	\operatorname{div}\bigl(s_{4,g,n}^{\mathrm{res}}(\cA)\bigr)
  1741	\in
  1742	\operatorname{Pic}\bigl(\overline{\mathcal M}_{g,n}\times B_{\cA}^{\circ}\bigr).
  1743	\end{equation}
  1744	\end{definition}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1402,1422p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3492,3510p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5348,5376p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1402	hence $A_\infty$-depth $d_\infty(\cA) = 2$ and
  1403	$L_\infty$-formality level $f_\infty(\cA) = 2$.
  1404	The genus-$0$ transferred $L_\infty$ brackets therefore
  1405	satisfy $\ell_k^{(0),\mathrm{tr}} = 0$ for $k \geq 3$:
  1406	the genus-$0$ convolution algebra is formal.
  1407	
  1408	For the full scalar orbit, the shadow
  1409	obstruction tower terminates at degree~$2$:
  1410	$\Theta_{\cA}^{(\le r)} = \kappa \cdot \eta \otimes \Lambda$
  1411	for all~$r$. The obstruction classes
  1412	$o^{(r+1)}(\cA) \in H^2(F^{r+1}\gAmod / F^{r+2}\gAmod, d_2)$
  1413	vanish for all $r \geq 2$
  1414	(Theorem~\ref{thm:nms-all-degree-master-equation}).
  1415	Since the genus-$g$ quantum brackets $\ell_k^{(g)}$ for
  1416	$g \geq 1$ are induced by sewing on $\overline{\cM}_{g,n}$,
  1417	and sewing applied to the scalar element
  1418	$\kappa \cdot \eta \otimes \Lambda$ produces the scalar
  1419	genus-$g$ curvature $\kappa^g \cdot \eta_g \otimes \Lambda_g$
  1420	(which lies in the image of the differential, not in
  1421	independent cohomology), the transferred higher-genus brackets
 succeeded in 51ms:
  3492	Proposition~\ref{prop:pbw-universality};
  3493	MC4 compl.\ =
  3494	Theorem~\ref{thm:completed-bar-cobar-strong};
  3495	lattice filt.\ =
  3496	Theorem~\ref{thm:lattice:koszul-morphism};
  3497	null vect.\ = Kac--Shapovalov obstruction
  3498	(Theorem~\ref{thm:kac-shapovalov-koszulness});
  3499	Cartan~$H^2$ = abelian Cartan subalgebra classes
  3500	surviving in $H^2(\barB)$
  3501	(Remark~\ref{rem:admissible-koszul-status}).
  3502	\textit{Shadow}: archetype class $G$/$L$/$C$/$M$
  3503	(Theorem~\ref{thm:nms-archetype-trichotomy})
  3504	and shadow depth $r_{\max}$;
  3505	all four classes contain Koszul algebras
  3506	(shadow depth $\neq$ Koszulness).
  3507	
  3508	\smallskip\noindent
  3509	${}^{\dagger}$\,The symplectic fermion
  3510	($\beta\gamma$ at $\lambda = \tfrac{1}{2}$,
 succeeded in 51ms:
  5348	\item Gaussian: all $\ell_n^{\mathrm{tr}} = 0$ for $n \geq 2$
  5349	(Heisenberg);
  5350	\item Lie/tree: $\ell_2^{\mathrm{tr}} \neq 0$,
  5351	$\ell_n^{\mathrm{tr}} = 0$ for $n \geq 3$ (affine);
  5352	\item Contact/quartic: $\ell_2^{\mathrm{tr}} = 0$,
  5353	$\ell_3^{\mathrm{tr}} \neq 0$ ($\beta\gamma$);
  5354	\item Mixed: $\ell_2^{\mathrm{tr}} \neq 0$ \emph{and}
  5355	$\ell_3^{\mathrm{tr}} \neq 0$ (Virasoro, $\mathcal{W}_N$).
  5356	\end{itemize}
  5357	The shadow obstruction tower is the homotopy structure made visible.
  5358	\end{remark}
  5359	
  5360	\begin{remark}[The three archetypes from the Lagrangian perspective]
  5361	\label{rem:three-archetypes-lagrangian}
  5362	The fake-complementarity criterion reframes the archetype trichotomy
  5363	(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
  5364	The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
  5365	Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
  5366	$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
  5367	so the dual Lagrangian bends cubically. The $\beta\gamma$ system is
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17110,17136p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 17110	\end{theorem}
 17111	
 17112	\begin{proof}
 17113	Each case follows from the established vanishing theorems:
 17114	
 17115	(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
 17116	coassociative ($m_k = 0$ for $k \geq 3$ in the transferred
 17117	$A_\infty$-structure), so all obstruction sources vanish
 17118	(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).
 17119	
 17120	(ii)~For affine algebras, the cubic shadow is the Lie bracket
 17121	transported through the bar complex
 17122	(Theorem~\ref{thm:nms-affine-cubic-normal-form}). The quartic
 17123	obstruction $o_4 = \tfrac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$
 17124	vanishes by the Jacobi identity: the cyclic double Lie bracket
 17125	$\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 17126	
 17127	(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
 17128	the class-$\mathbf{C}$ witness: its shadow tower vanishes and
 17129	$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity

thinking
**Inspecting theorem references**

I’m looking at theorem references related to appendix nonlinear modular shadows, and I'm wondering if they cite back to theory-only labels, which could indicate circularity. I should check local blocks like `thm:nms-all-degree-master-equation` and `thm:nms-archetype-trichotomy`. I feel like it’s important to see how these theories are used for support, because if their proofs rely on other theoretical theorems, it might lead to a circular reference. Let’s take a quick look!
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1198,1238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '2098,2140p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1198	\mathfrak Q_{\beta\gamma}\star_{P_{\beta\gamma}}H_{\beta\gamma}.
  1199	\]
  1200	There is no cubic tree contribution.
  1201	\end{corollary}
  1202	
  1203	\begin{proof}
  1204	Apply the quartic boundary recursion with $\mathfrak C_{\beta\gamma}=0$.\qedhere
  1205	\end{proof}
  1206	
  1207	\begin{theorem}[Primitive nonlinear archetype trichotomy; \ClaimStatusProvedHere]
  1208	\label{thm:nms-archetype-trichotomy}
  1209	Through quartic order, the three frame families realize the three primitive nonlinear archetypes:
  1210	\begin{enumerate}[label=\textup{(\roman*)}]
  1211	\item Heisenberg is Gaussian:
  1212	\[
  1213	\Theta_{\mathcal H}^{\le 4}=H_{\mathcal H}.
  1214	\]
  1215	\item Affine $\widehat{\mathfrak{sl}}_2$ is of Lie/tree type:
  1216	\[
  1217	\Theta_{\mathrm{aff}}^{\le 4}=H_{\mathrm{aff}}+\mathfrak C_{\mathrm{aff}},
 succeeded in 51ms:
  2098	&\qquad&\text{(quintic)}
  2099	\label{eq:nms-quintic-obstruction}
  2100	\\
  2101	\mathfrak o_{\cA}^{(6)}
  2102	&= \tfrac12\{\mathfrak Q_{\cA},\mathfrak Q_{\cA}\}_{H_{\cA}}
  2103	+\{\mathfrak C_{\cA},\mathrm{Sh}_5(\cA)\}_{H_{\cA}}.
  2104	&\qquad&\text{(sextic)}
  2105	\label{eq:nms-sextic-obstruction}
  2106	\end{alignat}
  2107	\end{definition}
  2108	
  2109	\begin{theorem}[All-degree master equation; \ClaimStatusProvedHere]
  2110	\label{thm:nms-all-degree-master-equation}
  2111	Assume the complementarity potential $S_{\cA}$ satisfies the classical master equation $\{S_{\cA},S_{\cA}\}_{H_{\cA}}=0$. Then for every $r\ge 3$, the shadow jets satisfy
  2112	\begin{equation}
  2113	\label{eq:nms-all-degree-master-equation}
  2114	\nabla_{H_{\cA}}\mathrm{Sh}_r(\cA) + \mathfrak o_{\cA}^{(r)} = 0,
  2115	\end{equation}
  2116	where $\nabla_{H_{\cA}}:=\{H_{\cA},\,\cdot\,\}_{H_{\cA}}$ and $\mathfrak o_{\cA}^{(r)}$ is the degree-$r$ obstruction of Definition~\ref{def:nms-degree-r-obstruction}. When $r=3$ the obstruction sum is empty and the equation reads $\nabla_{H_{\cA}}\mathfrak C_{\cA}=0$.
  2117	\end{theorem}
exec
/bin/zsh -lc "rg -n 'thm:nms-archetype-trichotomy|thm:nms-all-degree-master-equation|prop:pbw-universality|thm:modular-characteristic|thm:mc2-bar-intrinsic' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
18:(Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
48: contribution; Theorem~\ref{thm:modular-characteristic}).
56: (Theorem~\ref{thm:mc2-bar-intrinsic}).
71:The universal Maurer--Cartan class $\Theta_\cA$ exists unconditionally for every modular Koszul chiral algebra, by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): one sets $\Theta_\cA := D_\cA - \dzero$, where $D_\cA$ is the genus-completed bar differential, and the Maurer--Cartan equation is the tautological consequence of $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of the finite-order projections of this proved element. The \emph{constructive} value of the tower is computational: each level yields explicit graph-sum formulas (vertex labels from the transferred cyclic minimal model, edge contractions by the complementarity propagator) that the bar-intrinsic construction does not directly produce. The obstruction classes $o_{r+1}(\cA) \in H^2(\cA^{\mathrm{sh}}_{r+1,0})$ measure the failure of \emph{truncation} (can the degree-$r$ approximation be extended one step further without changing its lower-order terms?), not the failure of \emph{existence}. Every theorem below is tagged either as proved here, as a formal consequence of the bar-intrinsic construction, or as conjectural at the level of the \emph{Hamiltonian refinement} (the graph-completed modular master action of \S\ref{sec:nms-feynman-transform-programme}).
87:(Theorem~\ref{thm:nms-all-degree-master-equation}),
690:The full universal class $\Theta_{\cA}$ globalizes the entire modular deformation theory (Theorem~\ref{thm:mc2-bar-intrinsic}). Its first visible jets are accessible before the full globalization.
694:By the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}), the universal Maurer--Cartan class
707:Since the universal class $\Theta_\cA$ exists (Theorem~\ref{thm:mc2-bar-intrinsic}), the three tensors
812:Since the shadow jets are the degree-$\le 4$ projections of the bar-intrinsic MC element $\Theta_\cA$ \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}, which satisfies the modular clutching identity, on every separating clutching map $\xi$ one has
1208:\label{thm:nms-archetype-trichotomy}
1898:The bar-intrinsic MC element $\Theta_{\cA}$ \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} satisfies the modular clutching identity
2021:(Theorem~\ref{thm:mc2-bar-intrinsic}) produces
2110:\label{thm:nms-all-degree-master-equation}
2217:Since the shadow jets are projections of the bar-intrinsic MC element $\Theta_\cA$ \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}, which satisfies the modular clutching identity, for every $r\ge 2$ and every separating clutching map $\xi$,
2482:\item since the full universal class $\Theta_{\cA}$ exists (Theorem~\ref{thm:mc2-bar-intrinsic}), this clutching correction is the first nonlinear modular shadow of its universal clutching identity;
2490:Parts~(i)--(iii) are Theorems~\ref{thm:nms-shadow-master-equations}, \ref{thm:nms-separating-boundary-recursion}, and \ref{thm:nms-shadow-cocycle-characterization}. Part~(iv) is Theorem~\ref{thm:nms-archetype-trichotomy}. Part~(v) is Theorems~\ref{thm:nms-virasoro-mixed-shadow} and \ref{thm:nms-principal-wn-contact-nonvanishing} together with Corollary~\ref{cor:nms-principal-wn-mixed}. Part~(vi) is Construction~\ref{constr:nms-gram-determinant-line} and Definition~\ref{def:nms-modular-quartic-resonance-class}. Part~(vii) is Theorems~\ref{thm:nms-clutching-law-modular-resonance} and \ref{thm:nms-first-nonlinear-shadow-theta}. Part~(viii) is Theorems~\ref{thm:nms-all-degree-master-equation} and~\ref{thm:nms-finite-termination}. Parts~(ix) and~(x) are Theorem~\ref{thm:nms-nonseparating-clutching-law}, Corollary~\ref{cor:nms-genus-one-hessian-correction}, and Theorem~\ref{thm:nms-genus-loop-model-families}.\qedhere
2495:The universal class $\Theta_{\cA}$ is constructed by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}); the remaining task is to verify clutching and Verdier compatibilities in complete generality and to identify the resulting Hamiltonian modular master action. What this appendix does show is that the nonlinear layer is rigid enough to be organized theorematically, and that it carries genuinely new modular content. The genus loop operator converts quartic contact data into genus-$1$ Hessian corrections that no scalar invariant can see. The quartic resonance class is not an afterthought: it is the first modular characteristic that remembers that complementarity is nonlinear.
2501:The finite-order shadow calculus of the preceding sections captures the degree-$\le 4$ face of the universal Maurer--Cartan class $\Theta_\cA$, which exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}). The next question is not \emph{existence} (that is settled) but \emph{refinement}: can one upgrade the abstract MC element to a \emph{graph-completed Hamiltonian modular master action} that organizes the vertex-by-vertex computational content? This section constructs the natural carrier object for such a refinement, states the resulting conjecture, and introduces three new geometric avatars.
2550:The bar-intrinsic MC element $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic}) admits a canonical \emph{Hamiltonian} lift to a group-like element
2917:These names are a proposal, not yet a theorem; the shadow obstruction tower determines the singularity type of the wavefunction, so the archetype trichotomy of Theorem~\ref{thm:nms-archetype-trichotomy} becomes a classification of local wavefunctions by catastrophe type.

thinking
**Auditing references**

I need to audit all references to the mid-body appendices being called either "Appendix" or "Chapter." First, I have to identify which files should be listed before "\appendix." Right now, I'm looking at files like homotopy_transfer, nonlinear_modular_shadows, branch_line_reductions, and combinatorial_frontier. I might also consider general_relations, but it's not after the appendix. So, it'll be important to search for those labels using "Appendix" or "Chapter." Time to grep!
codex
The seam problem is sharper than I first thought: several files under `appendices/` are not appendices in the live build at all. `main.tex` inputs `homotopy_transfer`, `nonlinear_modular_shadows`, `branch_line_reductions`, and `combinatorial_frontier` before `\\appendix`, so every “Appendix …” reference to those labels is misclassified. I’m enumerating those miscitations now.
exec
/bin/zsh -lc "rg -n 'Appendix~\\\\ref\\{app:(homotopy-transfer|nonlinear-modular-shadows|branch-line-reductions|combinatorial-frontier|koszul-reference)\\}|Appendix~\\\\textup\\{\\\\ref\\{app:(homotopy-transfer|nonlinear-modular-shadows|branch-line-reductions|combinatorial-frontier|koszul-reference)\\}|cf\\.\\ Appendix~\\\\ref\\{app:(homotopy-transfer|nonlinear-modular-shadows|branch-line-reductions|combinatorial-frontier|koszul-reference)\\}' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Chapter~\\\\ref\\{app:(signs|sign-conventions|arnold-relations|koszul-reference|curved-ainfty-formulas)\\}|Chapter~\\\\textup\\{\\\\ref\\{app:(signs|sign-conventions|arnold-relations|koszul-reference|curved-ainfty-formulas)\\}' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
appendices/signs_and_shifts.tex:250:\item \emph{Koszul dual coalgebra} (suspension): $\cA^! \hookrightarrow \mathrm{Cofree}(sV^*)$ (Appendix~\ref{app:koszul-reference}). Suspension raises the dual generators $V^*$ by one degree because dualizing reverses the grading, and the shift restores it.
chapters/theory/higher_genus_modular_koszul.tex:4455: Appendix~\textup{\ref{app:nonlinear-modular-shadows}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:4990:(Appendix~\ref{app:nonlinear-modular-shadows});
chapters/theory/higher_genus_modular_koszul.tex:10286:Appendix~\ref{app:nonlinear-modular-shadows} at each finite
chapters/theory/higher_genus_modular_koszul.tex:12438: (Appendix~\ref{app:nonlinear-modular-shadows}).
chapters/theory/higher_genus_modular_koszul.tex:12477: Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:13369:and Appendix~\ref{app:nonlinear-modular-shadows}
chapters/theory/higher_genus_modular_koszul.tex:15619:Appendix~\ref{app:nonlinear-modular-shadows}:
chapters/theory/higher_genus_modular_koszul.tex:15633:Appendix~\ref{app:nonlinear-modular-shadows} enumerates
chapters/theory/higher_genus_modular_koszul.tex:29926:(Appendix~\ref{app:nonlinear-modular-shadows}) is
chapters/theory/higher_genus_modular_koszul.tex:31269:and Appendix~\ref{app:nonlinear-modular-shadows}) is the
chapters/theory/existence_criteria.tex:474:$\mathcal{W}_{1+\infty}$ & No & Yes (completed) & Filtered; see Appendix~\ref{app:koszul-reference} \\
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:525:full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
chapters/theory/chiral_hochschild_koszul.tex:3143:Appendix~\ref{app:homotopy-transfer}, the transferred higher
chapters/theory/chiral_hochschild_koszul.tex:3175:complete filtered dg~Lie algebras (Appendix~\ref{app:homotopy-transfer}).
chapters/theory/chiral_hochschild_koszul.tex:6021:Appendix~\ref{app:branch-line-reductions} extracts exact
chapters/theory/chiral_hochschild_koszul.tex:6053:(Appendix~\ref{app:branch-line-reductions}) are the spectral
chapters/theory/higher_genus_complementarity.tex:98: \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
appendices/combinatorial_frontier.tex:334:\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.





thinking
**Fixing document structure**

I'm exploring a potential fix for how files are organized in the document. The user is asking about seam audits, so I need to understand the intended architecture. It seems files currently labeled as "appendix" have actually been elevated to chapter-level content. To address this, I'll replace references from "Appendix" to "Chapter" for clarity. Renaming their labels from `app:` to `ch:` or `chap:` seems like an option, but it might not be strictly necessary for all cases since there are many references.
thinking
**Evaluating citation accuracy**

I'm assessing the citations in this context. It seems like the high rating is due to wrong citations that could misrepresent the direction of dependency. However, I'm not seeing any mathematical falsehoods, which makes me think maybe a medium rating is more appropriate. But since the user asked for a maximally harsh evaluation, I need to weigh my options carefully before deciding how to present this. There’s a lot to consider!
thinking
**Evaluating label issues**

I'm looking at the severity of some issues related to labels and citations in a document. It seems like there are problems with misclassified citations that I’d rate as moderate because they’re misleading and confusing. The omitted theorem could be more critical. 

I notice discrepancies with the `app:` label still being used, even in chapters. This indicates a label prefix drift. I could suggest renaming these labels to `chap:` or `ch:` for clarity and updating all references accordingly.
thinking
**Addressing structural findings**

It looks like there's a broader structural issue to address rather than just looking at 15 individual miscitations. I want to pinpoint specific lines in `main.tex`, like `1010, 1112, 1116, 1374`. The output guidelines ask for a singular file and line reference. While the user is interested in seam inconsistencies, I should note mismatched citations at those lines too. 

There seems to be a significant finding at `main.tex:1010` about promoting files before `\appendix`, so I should suggest moving the `\input`s or replacing `Appendices` with `Chapters` with clear references. I'll aim to list those specific lines to ensure clarity.
thinking
**Considering separate findings**

I'm thinking that it might be helpful to present separate findings for each file since the fixes need to be precise and localized. This approach could make it clearer for the user to understand where each issue lies and how to address them specifically in the respective files. By breaking them down this way, I can ensure that the exact fixes are easy to follow, ultimately making the process smoother for the user.
exec
/bin/zsh -lc "rg -n '\\bappendix\\b|\\bAppendix\\b' appendices/homotopy_transfer.tex appendices/nonlinear_modular_shadows.tex appendices/branch_line_reductions.tex appendices/combinatorial_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/branch_line_reductions.tex:28:The purpose of the appendix is not to replace the full MC2 package by a
appendices/branch_line_reductions.tex:57:The appendix proves five families of results.
appendices/branch_line_reductions.tex:141:The point of view of this appendix is that the scalar and spectral levels
appendices/combinatorial_frontier.tex:334:\item \emph{Planar rooted trees.} The number of planar rooted trees with~$n$ internal nodes is $C_{n-1}$. These trees index the terms of the $A_\infty$ structure maps $m_n$ in the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}, Theorem~\ref{thm:htt}). When one transfers the bar complex structure to a minimal model via a strong deformation retract, each $m_n$ is a sum over $C_{n-1}$ planar trees.
appendices/combinatorial_frontier.tex:1067:\begin{equation}\label{eq:yangian-gf-appendix}
appendices/nonlinear_modular_shadows.tex:207:of Appendix~\ref{app:signs}.
appendices/nonlinear_modular_shadows.tex:2495:The universal class $\Theta_{\cA}$ is constructed by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}); the remaining task is to verify clutching and Verdier compatibilities in complete generality and to identify the resulting Hamiltonian modular master action. What this appendix does show is that the nonlinear layer is rigid enough to be organized theorematically, and that it carries genuinely new modular content. The genus loop operator converts quartic contact data into genus-$1$ Hessian corrections that no scalar invariant can see. The quartic resonance class is not an afterthought: it is the first modular characteristic that remembers that complementarity is nonlinear.
appendices/nonlinear_modular_shadows.tex:3136:The full hierarchy, extended by the constructions of this appendix, is
appendices/nonlinear_modular_shadows.tex:3162:appendix supplies the higher-genus completion. That is, the
appendices/nonlinear_modular_shadows.tex:3175:For the archetype families computed in this appendix:

thinking
**Searching for labels**

I'm on a quest to find all the `app:` labels defined before `\appendix` that are referenced as Appendix. It looks like I have those identified. Next, I need to search for `app:` labels defined after `\appendix` that are referred to as Chapter. Surprisingly, I found that only `app:nonlinear-modular-shadows` had the Chapter reference, but it's situated before `\appendix`. So, it seems that’s not exactly what I’m looking for.
exec
/bin/zsh -lc "rg -n 'app:combinatorial-frontier' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/combinatorial_frontier.tex:2:\label{app:combinatorial-frontier}
chapters/theory/chiral_koszul_pairs.tex:1116:Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
chapters/theory/introduction.tex:2258:Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\ref\\{app:(homotopy-transfer|branch-line-reductions|combinatorial-frontier|nonlinear-modular-shadows)\\}|Chs\\.~\\\\ref\\{app:(homotopy-transfer|branch-line-reductions|combinatorial-frontier|nonlinear-modular-shadows)\\}|Chs\\.~\\\\ref\\{["'^}]*app:(homotopy-transfer|branch-line-reductions|combinatorial-frontier|nonlinear-modular-shadows)'"' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex:1960:(Chapter~\ref{app:nonlinear-modular-shadows}).
chapters/theory/chiral_hochschild_koszul.tex:6009:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic


thinking
**Determining exact fixes**

I’m thinking that a more durable method is to focus on specific edits rather than just overall prose. The user has requested an exact fix rather than a diagnosis, so I need to be precise. The main comment indicates that some files should be treated as chapters and not appendices, suggesting they need renaming and citation updates. While this may involve broader changes, it's crucial to follow the user's request for an audit. I've got to decide on the best straightforward fix.
thinking
**Evaluating file integration**

I see that the filename `_sl2_yangian_insert.tex` suggests it might be a dormant insert, so it's probably not wise to include it globally without caution. If the theory chapter relies on a theorem, I should consider moving or duplicating it into a source file that actually contains the claim. `chiral_modules.tex` might be appropriate for that. However, the theorem regarding the open-colour Koszul dual being Yangian fits better in theory or examples. I'll need to check if the same statement exists elsewhere in the repo and possibly use an existing label.
codex
The strongest live seam bug is still the omitted `sl_2` theorem, but I’m checking whether there is already an included theorem elsewhere that states the same result. If there is, the exact fix is to repoint the references rather than resurrect the dormant insert file.
exec
/bin/zsh -lc "rg -n 'Open-colour Koszul dual|Koszul dual of \\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|Y_\\\\hbar\\\\(\\\\mathfrak\\{sl\\}_2\\\\)|sl2-koszul-dual' chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:2634:\textup{(}Theorem~\textup{\ref{thm:sl2-koszul-dual}} for
chapters/examples/free_fields.tex:2667:\emph{Proved}: the free-field and Heisenberg dualities (Chapter~\ref{sec:betagamma-koszul-dual}, Theorem~\ref{thm:heisenberg-koszul-dual-early}); the Kac--Moody level shift $\widehat{\mathfrak{g}}_k \leftrightarrow \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Theorems~\ref{thm:sl2-koszul-dual} and~\ref{thm:universal-kac-moody-koszul}).
chapters/examples/kac_moody.tex:613:\begin{theorem}[Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]\label{thm:sl2-koszul-dual}
chapters/examples/kac_moody.tex:1179:The factor $h^\vee$ arises from the adjoint representation: by Lemma~\ref{lem:killing-structure-constants}, $\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee \cdot \delta^{ab}$, which gives $\sum_{c,d,e} f^{ac}{}_d f^{bc}{}_e (J^d, J^e) = 2h^\vee \cdot (J^a, J^b)$. (For $\mathfrak{sl}_2$ with $h^\vee = 2$, this was verified explicitly in Theorem~\ref{thm:sl2-koszul-dual}: $m_1^2(e \boxtimes f \cdot \eta_{12}) = (k+2) \cdot \partial h$.)
chapters/examples/kac_moody.tex:1208:which is precisely the OPE of $\widehat{\mathfrak{g}}_{-k-2h^\vee}$. (For $\mathfrak{sl}_2$: $-k-2 \cdot 2 = -k-4$, matching Theorem~\ref{thm:sl2-koszul-dual}.)
chapters/examples/kac_moody.tex:1221:\item \emph{Explicit verification}: For $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}) and $\mathfrak{sl}_3$ (\S\ref{sec:sl3-computation}), the low-degree bar complex computations confirm the predicted dual level. \checkmark
chapters/examples/kac_moody.tex:1298:Theorem~\ref{thm:sl2-koszul-dual}.
chapters/examples/kac_moody.tex:2139:(cf.\ Theorem~\ref{thm:sl2-koszul-dual}) is
chapters/examples/kac_moody.tex:2214:(Theorem~\ref{thm:sl2-koszul-dual}), the dualised collision
chapters/examples/kac_moody.tex:3667:The genus-0 level-shifting duality $(\widehat{\mathfrak{sl}}_{2,k})^! \simeq \widehat{\mathfrak{sl}}_{2,-k-4}$ (Theorem~\ref{thm:sl2-koszul-dual}) is the starting point. We carry out the genus-1 pipeline for $\widehat{\mathfrak{sl}}_2$ at generic level $k \neq -2$: the first non-abelian example of all three main theorems at genus~1.
chapters/examples/kac_moody.tex:3869:The Koszul dual $(\widehat{\mathfrak{sl}}_{2,k})^! = \widehat{\mathfrak{sl}}_{2,-k-4}$ (Theorem~\ref{thm:sl2-koszul-dual}) has shifted level $k^* = -k-4$. Repeating the curvature computation with $k$ replaced by $k^*$:
chapters/examples/bar_complex_tables.tex:1716:(Theorem~\ref{thm:sl2-koszul-dual}).
chapters/examples/bar_complex_tables.tex:4421:(Theorem~\ref{thm:sl2-koszul-dual}):
chapters/examples/landscape_census.tex:1391:for $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}),
chapters/examples/landscape_census.tex:3999: (Theorem~\ref{thm:sl2-koszul-dual}),
appendices/_sl2_yangian_insert.tex:531:\begin{theorem}[Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$
appendices/_sl2_yangian_insert.tex:533:\label{thm:sl2-koszul-dual}
chapters/theory/chiral_modules.tex:2889:(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
chapters/theory/chiral_modules.tex:2961:(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
chapters/theory/chiral_modules.tex:2982:Theorem~\ref{thm:sl2-koszul-dual},
exec
/bin/zsh -lc "rg -n 'thm:sl2-koszul-dual|koszul-dual-id-sl2|Y_\\\\hbar\\\\(\\\\mathfrak\\{sl\\}_2\\\\)' -S ." in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 93

./resume_20260413_163457/S15_appendices_to_body.md:250:appendices/_sl2_yangian_insert.tex:593:eq:koszul-dual-id-sl2
./metadata/dependency_graph.dot:803:  thm_sl2_koszul_dual [label="thm:sl2-koszul-dual\ntheorem [Pr]\nKoszul dual of \texorpdfstring{$\widehat...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:2965:  thm_sl2_koszul_dual [label="thm:sl2-koszul-dual\ntheorem [Pr]\nOpen-colour Koszul dual of $\widehat{\ma...", style=filled, fillcolor="#c8e6c9"];
./metadata/theorem_registry.md:1610:| `thm:sl2-koszul-dual` | `theorem` | 613 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
./metadata/theorem_registry.md:2644:| `thm:sl2-koszul-dual` | `theorem` | 533 | Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$ is $Y_\hbar(\mathfrak{sl}_2)$ |
./metadata/label_index.json:13666:  "eq:koszul-dual-id-sl2": {
./metadata/label_index.json:43502:  "thm:sl2-koszul-dual": {
./metadata/claims.jsonl:778:{"label": "thm:sl2-koszul-dual", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/kac_moody.tex", "line": 613, "title": "Koszul dual of \\texorpdfstring{$\\widehat{\\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}"}
./metadata/claims.jsonl:799:{"label": "comp:sl2-collision-residue-kz", "env_type": "computation", "status": "ProvedHere", "file": "chapters/examples/kac_moody.tex", "line": 2090, "title": "Collision residue and the KZ $r$-matrix for $\\widehat{\\mathfrak{sl}}_{2,k}$", "labels_in_block": ["comp:sl2-collision-residue-kz", "eq:sl2-collision-ope", "eq:sl2-collision-ef", "eq:sl2-collision-hh", "eq:sl2-collision-eh", "eq:sl2-collision-hf", "eq:sl2-collision-ff", "eq:sl2-collision-bar-diff", "eq:sl2-collision-residue-formula", "eq:sl2-collision-explicit-ef", "eq:sl2-collision-explicit-he", "eq:sl2-collision-explicit-hf", "eq:sl2-collision-explicit-diag", "eq:sl2-casimir-explicit", "eq:sl2-r-matrix-explicit", "eq:sl2-arnold", "eq:sl2-cybe", "eq:sl2-kz-connection"], "refs_in_block": ["thm:sl2-koszul-dual", "constr:thqg-V-binary-extraction", "prop:thqg-V-arnold-cohomology", "eq:sl2-arnold", "thm:thqg-V-cybe-from-arnold", "thm:gz26-commuting-differentials", "thm:kz-classical-quantum-bridge", "eq:sl2-cybe"]}
./metadata/claims.jsonl:1835:{"label": "comp:bgg-sl2-pipeline", "env_type": "computation", "status": "ProvedHere", "file": "chapters/theory/chiral_modules.tex", "line": 2881, "title": "BGG pipeline for \\texorpdfstring{$\\widehat{\\mathfrak{sl}}_2$}{sl2-hat}\nat generic level", "labels_in_block": ["comp:bgg-sl2-pipeline", "eq:bgg-sl2-generic"], "refs_in_block": ["thm:bgg-from-bar", "comp:sl2-bar-matrix", "thm:sl2-koszul-dual", "thm:screening-bar", "eq:sl2-bar-matrix", "prop:generic-irreducibility", "eq:dot-action-translations", "prop:weyl-kac-sl2-bar", "prop:vacuum-verma-koszul", "eq:bgg-sl2-generic", "prop:shapovalov-koszul", "sec:bgg-sl2-pipeline", "cor:bgg-koszul-involution"]}
./metadata/claims.jsonl:2852:{"label": "thm:sl2-koszul-dual", "env_type": "theorem", "status": "ProvedHere", "file": "appendices/_sl2_yangian_insert.tex", "line": 533, "title": "Open-colour Koszul dual of $\\widehat{\\mathfrak{sl}}_2$\nis $Y_\\hbar(\\mathfrak{sl}_2)$", "labels_in_block": ["thm:sl2-koszul-dual", "eq:koszul-dual-id-sl2"]}
./chapters/examples/free_fields.tex:2634:\textup{(}Theorem~\textup{\ref{thm:sl2-koszul-dual}} for
./chapters/examples/free_fields.tex:2667:\emph{Proved}: the free-field and Heisenberg dualities (Chapter~\ref{sec:betagamma-koszul-dual}, Theorem~\ref{thm:heisenberg-koszul-dual-early}); the Kac--Moody level shift $\widehat{\mathfrak{g}}_k \leftrightarrow \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Theorems~\ref{thm:sl2-koszul-dual} and~\ref{thm:universal-kac-moody-koszul}).
./chapters/examples/kac_moody.tex:613:\begin{theorem}[Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]\label{thm:sl2-koszul-dual}
./chapters/examples/kac_moody.tex:1179:The factor $h^\vee$ arises from the adjoint representation: by Lemma~\ref{lem:killing-structure-constants}, $\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee \cdot \delta^{ab}$, which gives $\sum_{c,d,e} f^{ac}{}_d f^{bc}{}_e (J^d, J^e) = 2h^\vee \cdot (J^a, J^b)$. (For $\mathfrak{sl}_2$ with $h^\vee = 2$, this was verified explicitly in Theorem~\ref{thm:sl2-koszul-dual}: $m_1^2(e \boxtimes f \cdot \eta_{12}) = (k+2) \cdot \partial h$.)
./chapters/examples/kac_moody.tex:1208:which is precisely the OPE of $\widehat{\mathfrak{g}}_{-k-2h^\vee}$. (For $\mathfrak{sl}_2$: $-k-2 \cdot 2 = -k-4$, matching Theorem~\ref{thm:sl2-koszul-dual}.)
./chapters/examples/kac_moody.tex:1221:\item \emph{Explicit verification}: For $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}) and $\mathfrak{sl}_3$ (\S\ref{sec:sl3-computation}), the low-degree bar complex computations confirm the predicted dual level. \checkmark
./chapters/examples/kac_moody.tex:1298:Theorem~\ref{thm:sl2-koszul-dual}.



thinking
**Re-evaluating theorem references**

I've found another theorem in a section that has the same label as before, which explains why our earlier script missed it. This happened because we only looked at appendices, neglecting the examples that follow. In LaTeX, references can link to later theorems, so the issue of an "omitted label" is actually a false alarm. The references in theory direct to the live theorem in the examples section. Now I need to check if the theorem statement matches its usage.
thinking
**Investigating theorem conflicts**

I see that the output suggests the theorem in the examples may discuss closed-colour Kac-Moody shifts, while the omitted theorem in the appendix refers to open-colour Yangians. This means that the reference in chiral_modules likely points to the theorem in examples, not the one that was omitted. I should check the context around these references, especially lines discussing compatibility with Koszul duality. It turns out we have a seam issue since the appendix defines a different statement for the same theorem label, potentially causing conflicts.
thinking
**Clarifying the mission focus**

The task at hand is to examine the differences between appendices and chapters/theory, not specifically examples. I realize the theory cites `thm:sl2-koszul-dual`, while the appendix defines it differently, which poses a risk. But since the example theorem is active, the references in the theory aren’t pointing to the appendix. The user asked about the seam between appendices and theory. I suppose this dormant appendix label might create confusion, yet I need to stick to confirmed information to avoid making assumptions.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '604,636p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2956,2968p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2956	character formula
  2957	(Proposition~\ref{prop:weyl-kac-sl2-bar}).
  2958	
  2959	\emph{Step~5: Koszul duality of the resolution.}
  2960	Under $k \mapsto -k - 2h^\vee = -k-4$
  2961	(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
  2962	functor (Proposition~\ref{prop:vacuum-verma-koszul}) sends each
  2963	term of~\eqref{eq:bgg-sl2-generic} to the corresponding term at
  2964	the dual level:
  2965	\[
  2966	\Phi\bigl(\mathcal{M}(w \cdot \Lambda_0)_k\bigr)
  2967	\simeq \mathcal{M}(w \cdot \Lambda_0)_{-k-4},
  2968	\qquad w \in \mathcal{W}.
 succeeded in 51ms:
   604	\item The bar complex becomes:
   605	\begin{equation}
   606	\bar{B}^n(\widehat{\mathfrak{sl}}_{2,-2}) = \bigoplus_{n_1+n_2+n_3=n} \Gamma(\overline{C}_{n+1}(X), \mathfrak{sl}_2^{\boxtimes(n+1)} \otimes \Omega^n_{\log})
   607	\end{equation}
   608	\end{enumerate}
   609	\end{theorem}
   610	
   611	\subsection{Koszul dual computation}
   612	
   613	\begin{theorem}[Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]\label{thm:sl2-koszul-dual}
   614	For $k \neq -2$, the Koszul dual is the chiral CE algebra at the dual level:
   615	\begin{equation}
   616	(\widehat{\mathfrak{sl}}_{2,k})^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{sl}}_{2,-k-4}),
   617	\quad \kappa((\widehat{\mathfrak{sl}}_{2,k})^!) = \kappa(\widehat{\mathfrak{sl}}_{2,-k-4}).
   618	\end{equation}
   619	This is verified through explicit bar-cobar computation.
   620	\end{theorem}
   621	
   622	\begin{proof}[Computation through degree 3]
   623	We compute the bar complex $\bar{B}^{\leq 3}(\widehat{\mathfrak{sl}}_{2,k})$ and the cobar complex $\Omega^{\leq 3}(\bar{B}(\widehat{\mathfrak{sl}}_{2,k}))$.












thinking
**Evaluating findings in appendices**

I'm noticing some misreferences regarding the structure of the appendices. For instance, I think `appendices/combinatorial_frontier.tex` should be included before the \appendix, labeled as `app:combinatorial-frontier`. There seem to be several severity levels for the findings. Some may be high due to possible structural mismatches or circular definitions, while others might be medium or low. I need to evaluate if dormant appendices should be included in the final mission findings, especially since the user wants relevant content.
thinking
**Clarifying appendix and theory discrepancies**

I found that the appendix includes a reference that the theory does not have. However, the live reference in the theory connects to an example theorem, which is outside our focus. This suggests that there's no issue of referencing appendices in the theory itself. I should verify there are no other mislabeled references to "Appendix" before making a decision. It might be beneficial to summarize a significant finding with all affected lines and a fix, while also considering self-descriptions as a lower finding.
thinking
**Correcting citations**

I’m looking at the proof that states it's structured like the chiral case, mentioning Totaro relations. The more direct analogy seems to be `Theorem\ref{thm:bar-nilpotency-complete}` since the proof shows that d^2=0. So, I should replace `Corollary\ref{cor:bar-d-squared-zero-arnold}` with `Theorem\ref{thm:bar-nilpotency-complete}`. 

It seems there's a chance I might find another miscitation with `higher_genus_modular_koszul`, as it references Appendix nonlinear mod shadows instead of Chapter. I might need specific low findings for each target.
thinking
**Evaluating data findings**

Okay, I'm looking at the root cause fix that includes affected lines, but the user wants each finding formatted as file:line. I think referencing something like "main.tex:1010" could work. For the final summary, should I say "Checked: N"? Maybe it could be 385, since we're counting seam points checked. 

I see 311 unique cross-directory hits, with 114 theory-to-appendix hits and 197 appendix-to-theory hits. I’m wondering if I should just count unique labels instead of file pairs. It seems I might need more than four findings to be thorough.
thinking
**Assessing citation issues**

I’m considering including root cause label prefixes separately from misclassified citations, but maybe just the root causes along with affected lines is enough. Should I add something like "[LOW] appendices/branch_line_reductions.tex:28"? That could be a self-description, but it seems a bit redundant. 

I also thought about searching for direct circular definitions in the notation index, but perhaps those aren’t referenced. Additionally, I found that some definitions in the appendix might not be fully self-contained, like `def:nms-modular-quartic-resonance-class`. I need to check line references for `higher_genus_modular_koszul`, as my grep output shows some inconsistencies.
thinking
**Deciding on line listings**

I’m thinking about whether I should list all affected lines or just mention, “affected lines include...”. But since the user asked for the exact fix, I might need to provide the full list. It feels like including all lines is necessary, even if it's lengthy. After all, including the exact affected lines can be really helpful for clarity. So, I’ll go with the comprehensive approach and ensure the user gets everything they need!
thinking
**Considering file sets**

I’m thinking it might be better to focus on mentioning file sets in a concise manner. I want to ensure that the final answer isn’t too lengthy, so aiming for around 20 lines seems reasonable. It’s all about balancing thoroughness without overwhelming detail. I want to provide a clear, informative response while keeping it brief and to the point! Let’s see how I can structure it effectively.
thinking
**Structuring findings and severity ratings**

I need to format my output precisely, using the structure `[SEVERITY] file:line — PROBLEM: ... FIX: ...`. It seems like I should avoid links but mention file paths in plain text. It might be good to compute summary counts, like `Checked: 311 | Findings: 4 | Verdict: FAIL`. 

I must use exact severity names from the structured output: CRITICAL, HIGH, MEDIUM, LOW. I'm considering that misdirected corollary could be low or medium, but structural promotion drift might actually be CRITICAL due to its broad implications.
thinking
**Considering additional findings**

I'm thinking about whether I should add one more finding: a dormant `_sl2_yangian_insert` duplicate label with a different statement. It seems like that possibility could be rated as low severity. I want to evaluate this further to ensure I'm not missing any important implications. It's always good to double-check if there are nuances in such cases. I’ll weigh the potential impact and make sure I have the right assessment before finalizing anything.
thinking
**Addressing label inconsistencies**

The user is curious about the connection between appendices and chapters, particularly regarding the `thm:sl2-koszul-dual` theory. There’s a conflict with an appendix that defines the same label differently, leading to potential misattribution during audits. This inconsistency could mislead maintenance efforts, though it's maybe a low severity issue. I might need to check if the theory mentions anything about the open-colour theorem under that label, as it’s important for clarity.
thinking
**Considering output details**

I’m looking at how to mention a conflict regarding the `thm:sl2-koszul-dual` between the appendix and the chapters. The appendix defines it for the Yangian/open-colour statement, while the chapters use it for a different theorem, leading to improper references. The suggested fix is either to rename the appendix label or delete it if it's outdated. Although this issue is low severity, the user wants a thorough examination. I might need to search for other possible misclassifications to provide more insights.
thinking
**Identifying underlying issues**

I'm looking into another specific issue related to `appendices/combinatorial_frontier.tex:334`, where it calls `Appendix\ref{app:homotopy-transfer}`. This seems tied to the same root cause, so there's no need to separate it if the root cause fix addresses it. I might check if `appendices/branch_line_reductions.tex` still references "appendix" in its self-description, as that could relate to the same underlying problem, but it looks like it doesn't. This helps me clarify any redundant references!
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:bar-coalgebra\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1613:\begin{theorem}[Bar coalgebra; \ClaimStatusProvedHere]\label{thm:bar-coalgebra}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:bar-nilpotency-complete\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
841:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}
exec
/bin/zsh -lc "rg -n 'thm:sl2-koszul-dual|eq:koszul-dual-id-sl2' appendices/_sl2_yangian_insert.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\input\\{appendices/_sl2_yangian_insert\\}|\\\\include\\{appendices/_sl2_yangian_insert\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
533:\label{thm:sl2-koszul-dual}
544:\begin{equation}\label{eq:koszul-dual-id-sl2}
593:The identification~\eqref{eq:koszul-dual-id-sl2} is thereby established.
 exited 1 in 51ms:




thinking
**Identifying potential risks**

The user asked about the seam between the appendices and theory. I see the dormant appendix copy and live theory file both share 311 labels, which is quite significant and could mislead any search-based auditing. While we confirmed that it’s not a live build issue, there’s still a repo seam risk. This seems like a low finding, but it could be bigger than initially thought. Renaming those dormant labels might be extensive, but it is crucial for accuracy.
thinking
**Considering file inclusion**

The file isn't included, so maybe this should be a low finding. Instead of referring to _sl2 duplicates, I think we should focus on the seam between appendices and theory, which seems more relevant. It’s essential to verify that the file isn't part of the main document—I've already checked that. I might need to cite exact lines, as the label at line 37 matches the theory's line 37. This will help clarify any potential issues.
thinking
**Analyzing duplicates in labels**

It seems useful to address the user's request for an exhaustive seam, particularly since the dormant mirror is a significant weakness. I should probably mention some examples, even if they aren't strictly necessary. I need to get a count of duplicate labels between the dormant appendix and the associated theory counterpart, which could be either 251 or 311. It's interesting that 311 duplicates were found across the appendices and theory, mostly originating from this pair. I'll need to verify the exact counts using the script.
codex
One more seam hazard is non-live but real: the dormant appendix copy of `ordered_associative_chiral_kd` mirrors the live theory chapter label-for-label. I’m quantifying that pair precisely so I can decide whether it survives as a finding or is just noisy background.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my (%a,%t); for my "'$f (q{appendices/ordered_associative_chiral_kd.tex}){ open my $fh,q{<},$f or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$a{$1}=1 } } } for my $f (q{chapters/theory/ordered_associative_chiral_kd.tex}){ open my $fh,q{<},$f or die $!; while(my $line=<$fh>){ while($line =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$t{$1}=1 } } } my @dup=sort grep { $a{$_} && $t{$_} } keys %a; print scalar(@dup), qq{'"\\n}; print join(qq{\\n}, @dup[0..9]), qq{\\n};'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
311
D1
D2
D3
D4
D5
D6
ch:ordered-associative-chiral-kd
comp:sl2-eval
comp:sl3-eval-adjoint
comp:sl3-eval-fundamental

thinking
**Updating plan progress**

I'm noticing a possible issue with how `appendices/nonlinear_modular_shadows` and `branch_line_reductions` are categorized. They're included before the appendices but still stored under the appendices path. That seems relevant for better organization. It's good to identify these details! I think I need to update my plan now. It feels like I've completed step 1 and step 2, and I'm currently working on step 3. Let's keep going!
Plan update
I’ve finished the seam inventory and contextual reads for the live transition points. I’m now collapsing the surviving issues to findings that are line-exact, non-duplicative, and re-verified against the actual inclusion order and local theorem blocks.
  ✓ Enumerate all appendix/theory cross-references in both directions and candidate notation seams
  ✓ Read each seam point in context and test citation accuracy, dependency direction, and notation consistency
  → Re-verify surviving findings and produce exact fixes with line references







thinking
**Reviewing document findings**

I'm looking over the final findings, and I notice that a dormant appendix redefines some labels, which could lead to confusion since it isn't included in the main document. It seems wise to either move this file to an archive or rename its labels with a prefix and add a note at the top. I think it would be helpful to mention the exact count of labels from our script—there's already significant detail in my findings. We might have enough with five main points.
thinking
**Cross-checking potential mismatches**

I need to ensure there are no false positives in my findings. I've noted several areas with mismatches, such as high main promotion and bar-complex definitions. For the medium m0 mu0 mismatch, I think the severity might be high, but I'm not entirely sure. As for the low en_koszul misdirected citation, I could judge it as medium severity since it's independent and only appears parenthetically. Maybe I should assign a low severity for the dormant mirror duplicate labels because they seem less critical.
thinking
**Planning findings output**

I'm considering listing every file line in finding 1, or at least grouping all misclassifications by file. I'll check if the final answer length is manageable by potentially using semicolons since no nested bullets are allowed. Each finding might be a long sentence. There will be 5 lines plus a summary. I'll mention that I checked 311 unique references and clearly state "Findings: 5". The verdict is FAIL, and I’ll format each entry according to user instructions.
thinking
**Refining fixes and paths**

I need to mention the file paths relative to the project, which is fine. It's important to craft the response carefully and concisely. I should include specific fixes rather than options. For the en_koszul case, I’ll decide on the exact fix and cite `Theorem\ref{thm:bar-nilpotency-complete}` clearly. This will help ensure clarity and precision in the final output for the user.
thinking
**Clarifying document updates**

I need to think about renaming labels and references, which could be significant but precise. I should reference line 1588 for the appendix and include details from earlier lines. I’ll indicate that the appendix only appears at 1588. I want to avoid making assumptions and state that the "live build treats them as chapters" is based on TeX inclusion order. Additionally, I’ll confirm issues with notation drift and duplicate labels, addressing the severity for the main promotion.
thinking
**Determining file adjustments**

I need to evaluate my approach for handling the m0 situation. For the dormant mirror, I could suggest moving the file to an archive or renaming labels. However, I should avoid vague options and instead focus on a specific action. Moving the file to `archive/appendices/` seems appropriate, but I can’t assume the archive path exists. It might be clearer to add a comment like `% NOT INCLUDED IN main.tex` and rename all 311 labels with the prefix `oldapp:`. That’s a lot of work, so archiving or deleting might be simpler, but clarity is key!
thinking
**Prescribing file management**

Since I’m focused on auditing rather than editing, I can suggest actions like moving the file to `archive/ordered_associative_chiral_kd_dormant.tex` and removing the live labels. However, that's just a guess about the path. It might be better to keep everything within the repository. There is an `archive/` folder from AGENTS, but it’s not absolutely necessary. I want to make sure my recommendations are practical and clear!
codex
- [HIGH] main.tex:1010 — PROBLEM: `appendices/homotopy_transfer.tex` (1010), `appendices/nonlinear_modular_shadows.tex` (1112), `appendices/branch_line_reductions.tex` (1116), and `appendices/combinatorial_frontier.tex` (1374) are loaded before `\appendix` at `main.tex:1588`, so the live build treats them as body chapters, but theory and those files still cite/described them as appendices: `chapters/theory/higher_genus_foundations.tex:1635`, `chapters/theory/quantum_corrections.tex:360,525`, `chapters/theory/chiral_modules.tex:2672`, `chapters/theory/chiral_hochschild_koszul.tex:3143,3175,6021,6053`, `chapters/theory/higher_genus_complementarity.tex:98`, `chapters/theory/higher_genus_modular_koszul.tex:4455,4990,10286,12438,12477,13369,15619,15633,29926,31269`, `chapters/theory/introduction.tex:1962`, `chapters/theory/chiral_koszul_pairs.tex:1116`, `appendices/combinatorial_frontier.tex:334`, plus self-descriptions at `appendices/branch_line_reductions.tex:28,57,141` and `appendices/nonlinear_modular_shadows.tex:2495,3136,3162,3175`. FIX: keep these four files before `\appendix`, rename their head labels to chapter labels (`chap:homotopy-transfer`, `chap:nonlinear-modular-shadows`, `chap:branch-line-reductions`, `chap:combinatorial-frontier`), replace every listed `Appendix~\ref{app:...}` with `Chapter~\ref{chap:...}`, and change the listed internal nouns `appendix` to `chapter`.

- [HIGH] chapters/theory/algebraic_foundations.tex:116 — PROBLEM: the body definition of the bar construction depends on `Definition~\ref{def:bar-complex-algebraic}`, but that label exists only in `appendices/notation_index.tex:342-344`, where the “definition” is just “The algebraic bar complex is represented by the DG coalgebra model of Theorem~\ref{thm:bar-coalgebra}.” This is circular appendix→theory routing and the appendix entry is not a real definition. FIX: insert a real body definition at `chapters/theory/algebraic_foundations.tex:116`, e.g. `\begin{definition}[Bar complex (algebraic)]\label{def:bar-complex-algebraic} For an augmented algebra A with augmentation ideal \bar A, define B_{\mathrm{alg}}(A)=T^c(s^{-1}\bar A) with the standard bar differential induced by multiplication in A. \end{definition}`, then rewrite `appendices/notation_index.tex:342-344` to `The algebraic bar complex is Definition~\ref{def:bar-complex-algebraic}.`

- [MEDIUM] appendices/general_relations.tex:101 — PROBLEM: the curved `A_\infty` appendix switches curvature notation to `\mu_0` in the exact package cited from theory, while the live theory and the sign appendix use `m_0` consistently (`chapters/theory/higher_genus_foundations.tex:1926-1928`, `appendices/signs_and_shifts.tex:1311-1312,1545-1547`). The seam is therefore not notation-stable. FIX: replace `\mu_0` by `m_0` throughout `appendices/general_relations.tex:101-126`, so the opening reads `(\mathcal A,\{m_k\}_{k\ge0})`, and the formulas become `m_1(m_0)=0`, `m_1^2(a)=m_2(m_0,a)-m_2(a,m_0)`, etc.

- [LOW] chapters/theory/en_koszul_duality.tex:508 — PROBLEM: the proof of `thm:e2-d-squared` cites `Corollary~\ref{cor:bar-d-squared-zero-arnold}` as the chiral prototype, but that appendix corollary immediately defers its proof to `Theorem~\ref{thm:bar-nilpotency-complete}` at `appendices/arnold_relations.tex:168-169`. The body is citing a wrapper, not the actual source theorem. FIX: change `chapters/theory/en_koszul_duality.tex:508-510` to cite `Theorem~\ref{thm:bar-nilpotency-complete}` directly.

- [LOW] appendices/ordered_associative_chiral_kd.tex:37 — PROBLEM: this dormant appendix mirror is not included in `main.tex`, but it still duplicates `311` labels from `chapters/theory/ordered_associative_chiral_kd.tex` starting with the chapter label at line 37. The seam is therefore grep-fragile: source ownership is ambiguous even before any future inclusion. FIX: mark the file as dormant and rename all duplicated labels with a dormant prefix starting at line 37 (for example `ch:ordered-associative-chiral-kd` -> `oldapp:ordered-associative-chiral-kd`), or move the file out of `appendices/` so it cannot be mistaken for a live seam source.

## Summary
Checked: 311 | Findings: 5 | Verdict: FAIL
tokens used
361,643
