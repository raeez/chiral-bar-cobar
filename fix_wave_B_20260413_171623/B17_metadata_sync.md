# B17_metadata_sync (243s)

Updated [metadata/theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md) to match the current TeX tree.

FIXED: stale snapshot totals. The registry had `2845` proved claims, `3673` tagged claims, and `128` scanned `.tex` files; the live extractor now gives `2367`, `3113`, and `104`, and the file now reflects those values.

FIXED: stale proved-claim surface from deleted chapters. The old registry still indexed many claims from deleted connection files; the regenerated registry no longer mentions those files.

FIXED: stale line references for concordance-critical proved claims. Examples now aligned with source:
- `thm:bar-cobar-isomorphism-main` -> `chapters/theory/chiral_koszul_pairs.tex:4014`
- `thm:higher-genus-inversion` -> `chapters/theory/higher_genus_complementarity.tex:4440`
- `thm:bar-cobar-inversion-qi` -> `chapters/theory/bar_cobar_adjunction_inversion.tex:1606`
- `thm:modular-characteristic` -> `chapters/theory/higher_genus_modular_koszul.tex:2844`
- `thm:mc2-bar-intrinsic` -> `chapters/theory/higher_genus_modular_koszul.tex:3770`

FIXED: concordance cross-check for proved labels. The registry includes the concordance’s `ProvedHere` theorem/proposition labels that should appear there.

FIXED: correct absences from the proved registry. These are not disagreements:
- `thm:shifted-symplectic-complementarity` is `Conditional`, so it should not appear.
- `def:scalar-lane` and `def:modular-convolution-dg-lie` are definitions, not `ProvedHere` claims.
- `thm:modular-koszul-duality-main` is a label-only intro anchor, not a tagged theorem block.

BLOCKED: none.

Verification: a fresh extraction after the edit matches the registry snapshot exactly, and a post-edit grep found no stale snapshot rows or references to deleted chapter files in `metadata/theorem_registry.md`.


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
session id: 019d8798-c749-7b33-a900-ec8be15d6ad8
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: metadata/theorem_registry.md
Read the theorem registry. Cross-check against concordance.tex and the actual .tex files.
Flag any disagreements. Update the registry to match current state.
mcp startup: no servers


thinking
**Working on the repo**

I need to follow the instructions closely while updating the theorem registry to align with the concordance and actual tex files. This involves reading mandatory files like CLAUDE.md and theorem_registry.md. I might have to use the claim-surface-sync skill, possibly alongside multi-path-verify, since it's relevant to the task. The developer suggests using an explorer agent for codebase queries, even for file-related questions. I'll start by checking the repo state and providing insights based on my understanding.
thinking
**Planning the update**

It looks like I need to consider using an update_plan for this task since it's substantial. First, I should focus on providing a commentary update to gather enough context. This will help lay the groundwork before I dive deeper into planning. It’s essential to ensure I have all the necessary information, so I'm setting the stage for a thorough approach to tackle this effectively. Let’s start gathering what’s needed!
codex
I’m checking the registry surface against the live sources: `metadata/theorem_registry.md`, `chapters/connections/concordance.tex`, and the theorem environments in the referenced `.tex` files. I’ll read the mandatory repo context first, then isolate any status/label drift and make only the minimum registry edits needed.
exec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'AGENTS.md' -g 'metadata/theorem_registry.md' -g 'chapters/connections/concordance.tex' -g 'raeeznotes/raeeznotes100/red_team_summary.md' -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md' -g '.agents/skills/claim-surface-sync/SKILL.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
AGENTS.md
chapters/connections/concordance.tex
 succeeded in 52ms:
 M CLAUDE.md
 M Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
 M N1_koszul_meta.pdf
 M N2_mc3_all_types.pdf
 M N3_e1_primacy.pdf
 M N4_mc4_completion.pdf
 M N5_mc5_sewing.pdf
 M N6_shadow_formality.pdf
 M bibliography/references.tex
 M bp_self_duality.pdf
 M chapters/connections/bv_brst.tex
 D chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/concordance.tex
 D chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/connections/frontier_modular_holography_platonic.tex
 D chapters/connections/holomorphic_topological.tex
 D chapters/connections/kontsevich_integral.tex
 D chapters/connections/physical_origins.tex
 D chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex

thinking
**Exploring theorem registry**

I need to read the CLAUDE relevant sections, maybe starting with the theorem registry. I'll consider using parallel to read headers and parts. There might be a way to use `sed` or even check out explorer. Since I'm reading files, using exec_command could work as well. I should probably read the mandatory files first and figure out the structure of the theorem registry. I can use `rg` to locate references to the theorem registry.
codex
I’ve confirmed the worktree is dirty, including `concordance.tex`, so I’m treating that file as authoritative for the current session and avoiding unrelated surfaces. Next I’m reading the registry format, the concordance entries it depends on, and the claim-surface skill so the edits stay purely synchronizing rather than speculative.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
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
 succeeded in 51ms:
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

codex
The registry is auto-generated metadata, so I’m treating this as a synchronization job, not a theorem-edit job. I have the concordance and current registry format loaded; next I’m locating the actual source environments for the labels the concordance elevates, then I’ll compare those against the registry entries and only patch drift inside `metadata/theorem_registry.md`.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,200p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'MISSING red_team_summary.md'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^### Part I: Theory|''^### Part III: Connections|''^### Appendices|''^#### `|`thm:bar-cobar-isomorphism-main`|`thm:higher-genus-inversion`|`thm:bar-cobar-inversion-qi`|`thm:fiber-center-identification`|`thm:quantum-complementarity-main`|`thm:shifted-symplectic-complementarity`|`def:scalar-lane`|`thm:modular-characteristic`|`thm:main-koszul-hoch`|`thm:hochschild-polynomial-growth`|`prop:chirhoch1-affine-km`|`thm:modular-koszul-duality-main`|`thm:modular-homotopy-convolution`|`def:modular-convolution-dg-lie`|`thm:mc2-bar-intrinsic`|`thm:e1-mc-element`" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:bar-cobar-inversion-qi|thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|def:scalar-lane|thm:modular-characteristic|thm:main-koszul-hoch|thm:hochschild-polynomial-growth|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-homotopy-convolution|def:modular-convolution-dg-lie|thm:mc2-bar-intrinsic|thm:e1-mc-element\" chapters appendices metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 exited 1 in 51ms:
zsh:1: unmatched "
 succeeded in 51ms:
Total output lines: 992

chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
metadata/theorem_registry.md:253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 2009 | Generic affine first chiral Hochschild group |
metadata/theorem_registry.md:352:| `thm:main-koszul-hoch` | `theorem` | 693 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
metadata/theorem_registry.md:353:| `thm:hochschild-polynomial-growth` | `theorem` | 802 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
metadata/theorem_registry.md:424:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3941 | Geometric bar--cobar duality |
metadata/theorem_registry.md:630:| `thm:e1-mc-element` | `theorem` | 291 | $E_1$ Maurer--Cartan element |
metadata/theorem_registry.md:727:| `thm:fiber-center-identification` | `theorem` | 373 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
metadata/theorem_registry.md:728:| `thm:quantum-complementarity-main` | `theorem` | 525 | Quantum complementarity as Lagrangian polarization |
metadata/theorem_registry.md:782:| `thm:higher-genus-inversion` | `theorem` | 4424 | Higher genus inversion |
metadata/theorem_registry.md:828:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2586 | Bar-cobar isomorphism, retained for equation labels |
metadata/theorem_registry.md:901:| `thm:modular-characteristic` | `theorem` | 2844 | Modular characteristic |
metadata/theorem_registry.md:908:| `thm:mc2-bar-intrinsic` | `theorem` | 3770 | Bar-intrinsic MC2 |
metadata/theorem_registry.md:962:| `thm:modular-homotopy-convolution` | `theorem` | 10934 | Modular homotopy convolution |
chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
chapters/examples/w_algebras_deep.tex:1960:In the language of Theorem~\ref{thm:mc2-bar-intrinsic}, the zero locus


thinking
**Evaluating script modifications**

I’m looking into auto-generating via a script that modifies files, and it seems okay since formatting commands or bulk edits don’t need the apply_patch constraint. I might need to inspect the generator, but maybe that’s not necessary if the issue is just a registry mismatch from not regenerating after file changes. I should ensure the generator scans all relevant files and cross-check any mismatches. However, since the user specified only edits for the assigned files, I'll need to be careful running the script.
thinking
**Reviewing label modifications**

I’m thinking about using tools like `rg` or `sed` around the labels for editing. It might also be helpful to find counts to compare them effectively. I should inspect the generator along with the relevant sections of the `.tex` files to ensure everything aligns correctly. I want to make sure all the modifications are accurate, so some careful checking will be crucial. Alright, let's dive into the specifics and see what needs adjusting!
codex
I’ve verified the current registry already contains several concordance-critical labels, but I haven’t trusted the metadata yet because the source tree changed after the last auto-generation stamp. I’m reading the actual theorem environments and the metadata generator now to decide whether the minimal truthful fix is a small manual patch or a scoped regeneration of `metadata/theorem_registry.md` only.
exec
/bin/zsh -lc "sed -n '1,260p' scripts/generate_metadata.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 \"label\\{thm:bar-cobar-isomorphism-main\\}|label\\{thm:higher-genus-inversion\\}|label\\{thm:bar-cobar-inversion-qi\\}|label\\{thm:fiber-center-identification\\}|label\\{thm:quantum-complementarity-main\\}|label\\{thm:shifted-symplectic-complementarity\\}|label\\{def:scalar-lane\\}|label\\{thm:modular-characteristic\\}|label\\{thm:main-koszul-hoch\\}|label\\{thm:hochschild-polynomial-growth\\}|label\\{prop:chirhoch1-affine-km\\}|label\\{thm:modular-koszul-duality-main\\}|label\\{thm:modular-homotopy-convolution\\}|label\\{def:modular-convolution-dg-lie\\}|label\\{thm:mc2-bar-intrinsic\\}|label\\{thm:e1-mc-element\\}\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
text=pathlib.Path('metadata/theorem_registry.md').read_text()
labels=['thm:bar-cobar-isomorphism-main','thm:higher-genus-inversion','thm:bar-cobar-inversion-qi','thm:fiber-center-identification','thm:quantum-complementarity-main','thm:shifted-symplectic-complementarity','def:scalar-lane','thm:modular-characteristic','thm:main-koszul-hoch','thm:hochschild-polynomial-growth','prop:chirhoch1-affine-km','thm:modular-koszul-duality-main','thm:modular-homotopy-convolution','def:modular-convolution-dg-lie','thm:mc2-bar-intrinsic','thm:e1-mc-element']
for lab in labels:
    m=re.search(rf\"\\| "'`{re.escape(lab)}` '"\\| "'`([''^`]*)` '"\\| ([0-9]+) \\| (.*?) \\|\",text)
    print(lab, 'FOUND' if m else 'MISSING', m.groups() if m else '')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
#!/usr/bin/env python3
"""
Generate machine-readable metadata from the chiral bar-cobar monograph.

Outputs:
  metadata/claims.jsonl         — One JSON line per tagged claim
  metadata/census.json          — Single source of truth for all counts
  metadata/dependency_graph.dot — Machine-traversable theorem DAG
  metadata/label_index.json     — All labels with file:line locations
  metadata/theorem_registry.md  — Auto-synchronized proved-claim registry

Usage:
  python3 scripts/generate_metadata.py
  # or: make metadata
"""

from __future__ import annotations

import json
import os
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex-370-\end{proof}
chapters/theory/higher_genus_complementarity.tex-371-
chapters/theory/higher_genus_complementarity.tex-372-\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:373:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex-374-\index{fiber--center identification|textbf}
chapters/theory/higher_genus_complementarity.tex-375-\textup{[}Regime: curved-central
chapters/theory/higher_genus_complementarity.tex-376-\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
--
chapters/theory/higher_genus_complementarity.tex-522-polarization:
chapters/theory/higher_genus_complementarity.tex-523-
chapters/theory/higher_genus_complementarity.tex-524-\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:525:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex-526-\label{thm:quantum-complementarity}
chapters/theory/higher_genus_complementarity.tex-527-\index{deformation-obstruction complementarity|textbf}
chapters/theory/higher_genus_complementarity.tex-528-\index{Lagrangian!complementarity|textbf}
--
chapters/theory/higher_genus_complementarity.tex-2080-\end{proof}
chapters/theory/higher_genus_complementarity.tex-2081-
chapters/theory/higher_genus_complementarity.tex-2082-\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
chapters/theory/higher_genus_complementarity.tex:2083:\label{thm:shifted-symplectic-complementarity}
 succeeded in 51ms:
thm:bar-cobar-isomorphism-main FOUND ('theorem', '3941', 'Geometric bar--cobar duality')
thm:higher-genus-inversion FOUND ('theorem', '4424', 'Higher genus inversion')
thm:bar-cobar-inversion-qi FOUND ('theorem', '1606', 'Bar-cobar inversion: strict on the Koszul locus, coderived off it')
thm:fiber-center-identification FOUND ('theorem', '373', 'Fiber--center identification \\textup{(Theorem~\\texorpdfstring{$\\mathrm{C}_0$}{C0})}')
thm:quantum-complementarity-main FOUND ('theorem', '525', 'Quantum complementarity as Lagrangian polarization')
thm:shifted-symplectic-complementarity MISSING 
def:scalar-lane MISSING 
thm:modular-characteristic FOUND ('theorem', '2844', 'Modular characteristic')
thm:main-koszul-hoch FOUND ('theorem', '693', 'Koszul duality for Hochschild cohomology \\textup{(}Theorem~H\\textup{)}')
thm:hochschild-polynomial-growth FOUND ('theorem', '802', 'Polynomial growth of chiral Hochschild cohomology \\textup{(}Theorem~H, growth clause\\textup{)}')
prop:chirhoch1-affine-km FOUND ('proposition', '2009', 'Generic affine first chiral Hochschild group')
thm:modular-koszul-duality-main MISSING 
thm:modular-homotopy-convolution FOUND ('theorem', '10934', 'Modular homotopy convolution')
def:modular-convolution-dg-lie MISSING 
thm:mc2-bar-intrinsic FOUND ('theorem', '3770', 'Bar-intrinsic MC2')
thm:e1-mc-element FOUND ('theorem', '291', '$E_1$ Maurer--Cartan element')

thinking
**Inspecting theorem metadata**

I need to inspect the full generate_metadata function related to theorem_registry to clarify if it only includes ProvedHere claims. It's essential to gather the right information, so I’ll continue reading the lower part of the script to see if I can uncover more details. Understanding this fully will help in evaluating how the claims are organized. Let's see what I find as I dig deeper into the script!
codex
The first concrete disagreement is structural: the concordance cites `\ref{def:scalar-lane}` and `\ref{def:modular-convolution-dg-lie}`, but the current registry intentionally omits non-`ProvedHere` definitions, so those are not registry errors. The live drift I’m looking for now is within the proved-claim surface itself: missing proved labels, stale line numbers, stale counts, or entries surviving for files no longer active.
exec
/bin/zsh -lc "sed -n '260,520p' scripts/generate_metadata.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
from scripts.generate_metadata import get_active_files, get_all_tex_files, extract_claims
from collections import Counter,defaultdict
active={p.relative_to(Path.cwd()).as_posix() if False else None}
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

        # Find the line of the primary label (for accurate location)
        label_line = env_start + 1  # default: the \begin line (1-indexed)
        for local_idx, local_line in enumerate(block_lines):
            if primary_label in local_line and "\\label{" in local_line:
                label_line = env_start + local_idx + 1
                break

        claim = Claim(
            label=primary_label,
            env_type=env_name,
            status=status,
            file=rel_path,
            line=label_line,
            title=title,
            labels_in_block=block_labels if len(block_labels) > 1 else [],
            refs_in_block=block_refs,
            cites_in_block=block_cites,
        )
        claims.append(claim)
 succeeded in 51ms:

exec
/bin/zsh -lc "sed -n '520,820p' scripts/generate_metadata.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    print(f"  label_index.json: {len(index)} labels")


def write_theorem_registry(
    claims: list[Claim],
    active_files: list[Path],
    all_tex_files: list[Path],
) -> None:
    """Write metadata/theorem_registry.md — synchronized proved-claim registry."""
    proved_claims = [claim for claim in claims if claim.status == "ProvedHere"]
    status_counts = Counter(claim.status for claim in claims)
    env_counts = Counter(claim.env_type for claim in proved_claims)
    part_counts = Counter()
    file_counts = Counter()

    for claim in proved_claims:
        part_name, _ = classify_part(claim.file)
        if part_name:
            part_counts[part_name] += 1
        file_counts[claim.file] += 1
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
from collections import Counter,defaultdict
from scripts.generate_metadata import ROOT,get_active_files,get_all_tex_files,extract_claims,classify_part
active_files=get_active_files()
all_files=get_all_tex_files()
claims=[]
for p in all_files:
    claims.extend(extract_claims(p))
status=Counter(c.status for c in claims)
proved=[c for c in claims if c.status=='ProvedHere']
envs=Counter(c.env_type for c in proved)
parts=Counter(classify_part(c.file)[1] for c in proved)
by_file=Counter(c.file for c in proved)
print('proved',len(proved))
print('total',len(claims))
print('statuses',dict(status))
print('envs',dict(envs))
print('parts',dict(parts))
print('active',len(active_files))
print('scanned',len(all_files))
print('top20')
for file,count in by_file.most_common(20):
    print(count,file)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
proved 2367
total 3113
statuses {'ProvedHere': 2367, 'Conjectured': 290, 'Heuristic': 27, 'Conditional': 12, 'ProvedElsewhere': 414, 'Open': 3}
envs {'theorem': 1010, 'proposition': 805, 'corollary': 317, 'computation': 92, 'remark': 30, 'lemma': 109, 'verification': 1, 'calculation': 3}
parts {'Part III: Connections': 358, 'Part II: Examples': 677, 'Frame': 19, 'Part I: Theory': 1100, 'Appendices': 213}
active 85
scanned 104
top20
265 chapters/theory/higher_genus_modular_koszul.tex
135 chapters/connections/arithmetic_shadows.tex
113 chapters/theory/bar_cobar_adjunction_curved.tex
97 chapters/examples/yangians_drinfeld_kohno.tex
90 chapters/theory/ordered_associative_chiral_kd.tex
89 appendices/ordered_associative_chiral_kd.tex
80 chapters/theory/higher_genus_complementarity.tex
70 chapters/examples/w_algebras.tex
69 appendices/nonlinear_modular_shadows.tex
67 chapters/examples/free_fields.tex
64 chapters/theory/higher_genus_foundations.tex
55 chapters/connections/frontier_modular_holography_platonic.tex



thinking
**Considering file edits**

I’m thinking about running a script, but it writes multiple files beyond the target. The user specifically asked to only edit the assigned file. I need to avoid editing others. Maybe I can import script functions to write the theorem_registry.md specifically, using a Python snippet. That feels acceptable since it’s not a manual edit. However, I’ll need to ensure no other file edits are made and stick with applying code edits via defined methods.
thinking
**Analyzing registry mismatches**

I need to check the current registry for stale entries from deleted files because there's a mismatch in evidence counts. We should cross-check specific concordance labels, possibly where line numbers differ. Most actual labels match, except for one at line 3941, while the record shows it's at 4014. That’s a significant disagreement! Many line numbers seem stale, so I’ll systematically compare critical labels. I might need to compute the difference between the current registry and the actual generated claims, then summarize the mismatches.
thinking
**Updating the plan**

I need to ensure I flag any disagreements and update the registry to reflect the current state. I think it's important to mention these flagged disagreements in my final output and possibly in the commentary as well. It seems like using the update_plan function now would be beneficial, especially since there might be substantial changes. I’ll go ahead and apply the update_plan to outline the necessary steps moving forward.
codex
The mismatch is not local to one row. The current registry is stale against the live tree: its snapshot says `2845` proved claims across `128` scanned `.tex` files, while the current extractor sees `2367` proved claims across `104` `.tex` files, and at least one concordance-critical line reference is off (`thm:bar-cobar-isomorphism-main` is `4014` in source, `3941` in the registry). I’m moving to a scoped regeneration of `metadata/theorem_registry.md` only, then I’ll re-read and grep the updated file for coherence.
Plan update
The registry is stale relative to the current TeX tree. I’ve validated the drift against concordance-critical labels and the live extractor; next I’ll regenerate only the assigned metadata file and then verify the result.
  ✓ Read mandatory context and locate concordance-critical labels in live TeX sources
  ✓ Compare current theorem registry against live proved-claim extraction and isolate drift
  → Regenerate only metadata/theorem_registry.md from the live claim surface
  • Re-read the updated registry and grep modified file for coherence/forbidden patterns

thinking
**Gathering comparison details**

I need to figure out the missing or deleted files in the current registry compared to the actual files. It might be helpful to compute this before finalizing anything. I plan to script a comparison between the parsed registry and the actual claims. A status map could help show what has changed. I’ll summarize the findings: missing labels, extra labels, stale line numbers, and file counts, using Python to assist with this task.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from scripts.generate_metadata import get_all_tex_files, extract_claims
reg=Path('metadata/theorem_registry.md').read_text()
reg_entries={}
current_file=None
for line in reg.splitlines():
    m=re.match(r\"#### "'`([''^`]+)` '"\\((\\d+)\\)\", line)
    if m:
        current_file=m.group(1)
        continue
    m=re.match(r\"\\| "'`([''^`]+)` '"\\| "'`([''^`]+)` '"\\| (\\d+) \\| (.*?) \\|"'$", line)
    if m and current_file:
        label,env,ln,title=m.groups()
        reg_entries[label]={'"'file':current_file,'env':env,'line':int(ln),'title':title}
claims=[]
for p in get_all_tex_files():
    claims.extend(extract_claims(p))
actual={c.label:{'file':c.file,'env':c.env_type,'line':c.line,'title':' '.join(c.title.replace('|','\\\\|').split())} for c in claims if c.status=='ProvedHere'}
missing=sorted(set(actual)-set(reg_entries))
extra=sorted(set(reg_entries)-set(actual))
stale=[]
for lab in sorted(set(actual)&set(reg_entries)):
    a=actual[lab]; r=reg_entries[lab]
    diffs=[]
    for k in ('file','env','line','title'):
        if a[k]"'!=r[k]:
            diffs.append((k,r[k],a[k]))
    if diffs:
        stale.append((lab,diffs))
print('"'registry_entries',len(reg_entries))
print('actual_entries',len(actual))
print('missing',len(missing))
print('extra',len(extra))
print('stale',len(stale))
print('\\nFirst 20 extra labels:')
for lab in extra[:20]:
    print(lab, reg_entries[lab]['file'], reg_entries[lab]['line'])
print('\\nFirst 20 missing labels:')
for lab in missing[:20]:
    print(lab, actual[lab]['file'], actual[lab]['line'])
print('\\nFirst 20 stale labels:')
for lab,diffs in stale[:20]:
    print(lab)
    for k,old,new in diffs:
        print(' ',k,old,'=>',new)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
registry_entries 2757
actual_entries 2279
missing 6
extra 484
stale 467

First 20 extra labels:
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1111 chapters/connections/casimir_divisor_core_transport.tex 1111
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1225 chapters/connections/casimir_divisor_core_transport.tex 1225
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1328 chapters/connections/casimir_divisor_core_transport.tex 1328
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:190 chapters/connections/casimir_divisor_core_transport.tex 190
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:387 chapters/connections/casimir_divisor_core_transport.tex 387
__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:66 chapters/connections/casimir_divisor_core_transport.tex 66
__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:1225 chapters/connections/dg_shifted_factorization_bridge.tex 1225
__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:192 chapters/connections/dg_shifted_factorization_bridge.tex 192
__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:415 chapters/connections/dg_shifted_factorization_bridge.tex 415
__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:444 chapters/connections/dg_shifted_factorization_bridge.tex 444
__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:769 chapters/connections/dg_shifted_factorization_bridge.tex 769
__unlabeled_chapters/theory/chiral_modules.tex:3968 chapters/theory/chiral_modules.tex 3968
__unlabeled_chapters/theory/chiral_modules.tex:3995 chapters/theory/chiral_modules.tex 3995


thinking
**Analyzing the registry counts**

I'm diving into why the actual entries are 2279 instead of 2367. It seems like the parser only retained unique labels, possibly leaving out duplicates. However, earlier data suggested 2367. Maybe these differences come from duplicate labels across files. Registry lists all blocks but collapses duplicates in the parser, leading to inaccuracies. To compare counts correctly, I might need to regenerate a file using `write_theorem_registry` after verifying current counts. This seems like a solid plan!
thinking
**Considering hot zones and protocols**

I'm thinking about using status labels for hot zones. It seems like PE-7 might not need to create labels since I'm just editing the registry. However, AGENTS say to run the Pre-Edit Protocol if I touch a hot zone, which includes status drift zones (like HZ-5/HZ-2). Since I'm focusing on metadata and not directly editing .tex labels, including a simple PE-7 in commentary could make sense. I might opt for just generating theorem_registry.md using a Python snippet instead. Let's proceed with that plan!
codex
I’ve finished the drift audit. The stale registry currently contains hundreds of entries from deleted connection chapters plus many stale line offsets in surviving files, so the minimum truthful repair is not a hand patch; it’s a one-file regeneration from the live extractor. I’m writing only `metadata/theorem_registry.md`, then I’ll read it back and grep the modified file for obvious structural problems.
exec
/bin/zsh -lc "python3 - <<'PY'
from scripts.generate_metadata import get_active_files, get_all_tex_files, extract_claims, write_theorem_registry
all_tex_files = get_all_tex_files()
claims = []
for path in all_tex_files:
    claims.extend(extract_claims(path))
write_theorem_registry(claims, get_active_files(), all_tex_files)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  theorem_registry.md: 2367 proved claims indexed
exec
/bin/zsh -lc "sed -n '1,120p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:bar-cobar-inversion-qi|thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|def:scalar-lane|thm:modular-characteristic|thm:main-koszul-hoch|thm:hochschild-polynomial-growth|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-homotopy-convolution|def:modular-convolution-dg-lie|thm:mc2-bar-intrinsic|thm:e1-mc-element" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "casimir_divisor_core_transport|dg_shifted_factorization_bridge|holomorphic_topological|kontsevich_integral|physical_origins|shifted_rtt_duality_orthogonal_coideals|thqg_concordance_supplement|thqg_critical_string_dichotomy|thqg_fredholm_partition_functions|thqg_gravitational_complexity|thqg_gravitational_s_duality|thqg_gravitational_yangian|thqg_holographic_reconstruction|thqg_modular_bootstrap|thqg_perturbative_finiteness|thqg_preface_supplement|thqg_soft_graviton_theorems|thqg_symplectic_polarization|twisted_holography_quantum_gravity|typeA_baxter_rees_theta|ym_boundary_theory|ym_higher_body_couplings|ym_instanton_screening" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
 exited 1 in 51ms:

 succeeded in 51ms:
252:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
336:| `prop:chirhoch1-affine-km` | `proposition` | 2009 | Generic affine first chiral Hochschild group |
351:| `thm:main-koszul-hoch` | `theorem` | 693 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
352:| `thm:hochschild-polynomial-growth` | `theorem` | 802 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
423:| `thm:bar-cobar-isomorphism-main` | `theorem` | 4014 | Geometric bar--cobar duality |
629:| `thm:e1-mc-element` | `theorem` | 291 | $E_1$ Maurer--Cartan element |
727:| `thm:fiber-center-identification` | `theorem` | 373 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
728:| `thm:quantum-complementarity-main` | `theorem` | 525 | Quantum complementarity as Lagrangian polarization |
782:| `thm:higher-genus-inversion` | `theorem` | 4440 | Higher genus inversion |
828:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2586 | Bar-cobar isomorphism, retained for equation labels |
901:| `thm:modular-characteristic` | `theorem` | 2844 | Modular characteristic |
908:| `thm:mc2-bar-intrinsic` | `theorem` | 3770 | Bar-intrinsic MC2 |
962:| `thm:modular-homotopy-convolution` | `theorem` | 10934 | Modular homotopy convolution |
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from scripts.generate_metadata import get_active_files,get_all_tex_files,extract_claims
text=Path('metadata/theorem_registry.md').read_text()
# snapshot numbers
nums={}
for pat,key in [
(r'\\| ProvedHere claims \\| (\\d+) \\|','proved'),
(r'\\| Total tagged claims \\| (\\d+) \\|','total'),
(r'\\| Active files in "'`main.tex` '"\\| (\\d+) \\|','active'),
(r'\\| Total "'`'"\\\\.tex"'` files scanned '"\\| (\\d+) \\|','scanned')]:
    m=re.search(pat,text)
    nums[key]=int(m.group(1)) if m else None
# recompute
all_files=get_all_tex_files()
claims=[]
for p in all_files:
    claims.extend(extract_claims(p))
proved=sum(c.status=='ProvedHere' for c in claims)
print('registry_snapshot',nums)
print('recomputed',{'proved':proved,'total':len(claims),'active':len(get_active_files()),'scanned':len(all_files)})
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
registry_snapshot {'proved': 2367, 'total': 3113, 'active': 85, 'scanned': None}
recomputed {'proved': 2367, 'total': 3113, 'active': 85, 'scanned': 104}

thinking
**Evaluating file management**

I've found the deleted file names, and I'm considering treating them as forbidden patterns. I might need to update my plan step. I'll also parse the current registry to ensure the counts match the actual stored data. Running a script snippet to compare stored snapshot numbers against what I've recomputed could be useful. Additionally, I should check the label line numbers for critical labels. Skimming the area around the `higher_genus_complementarity.tex` file in the registry may help too. I’ll also inspect the diff summary using `git diff`.
codex
The regeneration finished cleanly. I’m doing the post-edit pass now: checking that the updated snapshot matches a fresh recomputation, that concordance-critical proved labels point to the current source lines, and that the registry no longer contains entries from deleted chapter files.
exec
/bin/zsh -lc 'git diff --stat -- metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- metadata/theorem_registry.md | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 metadata/theorem_registry.md | 1686 ++++++++++++++----------------------------
 1 file changed, 551 insertions(+), 1135 deletions(-)
 succeeded in 52ms:
diff --git a/metadata/theorem_registry.md b/metadata/theorem_registry.md
index bc08e65..9053286 100644
--- a/metadata/theorem_registry.md
+++ b/metadata/theorem_registry.md
@@ -8,34 +8,33 @@ This registry now tracks every `\ClaimStatusProvedHere` block directly from sour
 
 | Metric | Value |
 |---|---:|
-| ProvedHere claims | 2845 |
-| Total tagged claims | 3673 |
+| ProvedHere claims | 2367 |
+| Total tagged claims | 3113 |
 | Active files in `main.tex` | 85 |
-| Total `.tex` files scanned | 128 |
+| Total `.tex` files scanned | 104 |
 
 ## Status Totals
 
 | Status | Count |
 |---|---:|
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from scripts.generate_metadata import get_active_files,get_all_tex_files,extract_claims
text=Path('metadata/theorem_registry.md').read_text()
extract=lambda pat:int(re.search(pat,text).group(1))
vals={
 'proved':extract(r'\\| ProvedHere claims \\| (\\d+) \\|'),
 'total':extract(r'\\| Total tagged claims \\| (\\d+) \\|'),
 'active':extract(r'\\| Active files in "'`main.tex` '"\\| (\\d+) \\|'),
 'scanned':extract(r'\\| Total "'`'"\\.tex"'` files scanned '"\\| (\\d+) \\|'),
}
all_files=get_all_tex_files(); claims=[]
for p in all_files: claims.extend(extract_claims(p))
recomputed={'proved':sum(c.status=='ProvedHere' for c in claims),'total':len(claims),'active':len(get_active_files()),'scanned':len(all_files)}
print(vals)
print(recomputed)
print('match', vals==recomputed)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
{'proved': 2367, 'total': 3113, 'active': 85, 'scanned': 104}
{'proved': 2367, 'total': 3113, 'active': 85, 'scanned': 104}
match True


thinking
**Checking registry and patterns**

I need to check if `thm:shifted-symplectic-complementarity` is absent, as it involves some conditional elements confirmed only by the registry indexes. I should verify that there's no disagreement, possibly searching the current registry for terms like `quantum`. It might make sense to compare the proven labels, but it may not be necessary. I could grep forbidden patterns in the modified file, especially known stale snapshot values. The user mentioned running this check after edits, so it's crucial to follow up on that!
thinking
**Cross-checking labels and statuses**

I noticed that the `rg -n` command only printed the found labels, confirming that `thm:shifted-symplectic-complementarity` is absent, which is a good sign. I need to cross-check all concordance labels with their actual states as the user requested a comparison against concordance.tex and actual .tex files. It's important to systematically document any flagged disagreements. I’ll compute statuses for the concordance-critical list and check their presence in the registry, possibly using a script to print actual statuses for those labels. Let’s also clarify if `thm:modular-koszul-duality-main` lacks an associated claim environment.
codex
The updated snapshot now matches a fresh extraction exactly. I’m doing one last cross-check against the specific concordance labels so I can report which were fixed in the registry and which were correctly absent because they are conditional or not `ProvedHere` theorem blocks.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
from scripts.generate_metadata import get_all_tex_files, extract_claims, extract_all_labels
labels=[
 'thm:bar-cobar-isomorphism-main','thm:higher-genus-inversion','thm:bar-cobar-inversion-qi',
 'thm:fiber-center-identification','thm:quantum-complementarity-main','thm:shifted-symplectic-complementarity',
 'def:scalar-lane','thm:modular-characteristic','thm:main-koszul-hoch','thm:hochschild-polynomial-growth',
 'prop:chirhoch1-affine-km','thm:modular-koszul-duality-main','thm:modular-homotopy-convolution',
 'def:modular-convolution-dg-lie','thm:mc2-bar-intrinsic','thm:e1-mc-element'
]
claims=[]
for p in get_all_tex_files():
    claims.extend(extract_claims(p))
claim_by_label={}
for c in claims:
    claim_by_label.setdefault(c.label, []).append(c)
all_labels={}
for p in get_all_tex_files():
    for e in extract_all_labels(p):
        all_labels.setdefault(e.label, []).append(e)
for lab in labels:
    if lab in claim_by_label:
        for c in claim_by_label[lab]:
            print(f\"{lab}\\tCLAIM\\t{c.status}\\t{c.env_type}\\t{c.file}:{c.line}\\t{c.title}\")
    elif lab in all_labels:
        for e in all_labels[lab]:
            print(f\"{lab}\\tLABEL_ONLY\\t-\\t-\\t{e.file}:{e.line}\\t\")
    else:
        print(f\"{lab}\\tMISSING\\t-\\t-\\t-\\t\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 122ms:
thm:bar-cobar-isomorphism-main	CLAIM	ProvedHere	theorem	chapters/theory/chiral_koszul_pairs.tex:4014	Geometric bar--cobar duality
thm:higher-genus-inversion	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_complementarity.tex:4440	Higher genus inversion
thm:bar-cobar-inversion-qi	CLAIM	ProvedHere	theorem	chapters/theory/bar_cobar_adjunction_inversion.tex:1606	Bar-cobar inversion: strict on the Koszul locus, coderived off it
thm:fiber-center-identification	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_complementarity.tex:373	Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}
thm:quantum-complementarity-main	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_complementarity.tex:525	Quantum complementarity as Lagrangian polarization
thm:shifted-symplectic-complementarity	CLAIM	Conditional	theorem	chapters/theory/higher_genus_complementarity.tex:2083	Conditional bar-side BV upgrade of complementarity
def:scalar-lane	LABEL_ONLY	-	-	chapters/theory/higher_genus_modular_koszul.tex:2711	
thm:modular-characteristic	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_modular_koszul.tex:2844	Modular characteristic
thm:main-koszul-hoch	CLAIM	ProvedHere	theorem	chapters/theory/chiral_hochschild_koszul.tex:693	Koszul duality for Hochschild cohomology
\textup{(}Theorem~H\textup{)}
thm:hochschild-polynomial-growth	CLAIM	ProvedHere	theorem	chapters/theory/chiral_hochschild_koszul.tex:802	Polynomial growth of chiral Hochschild cohomology
\textup{(}Theorem~H, growth clause\textup{)}
prop:chirhoch1-affine-km	CLAIM	ProvedHere	proposition	chapters/theory/chiral_center_theorem.tex:2009	Generic affine first chiral Hochschild group
thm:modular-koszul-duality-main	LABEL_ONLY	-	-	chapters/theory/introduction.tex:2537	
thm:modular-homotopy-convolution	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_modular_koszul.tex:10934	Modular homotopy convolution
def:modular-convolution-dg-lie	LABEL_ONLY	-	-	chapters/theory/higher_genus_modular_koszul.tex:10175	
thm:mc2-bar-intrinsic	CLAIM	ProvedHere	theorem	chapters/theory/higher_genus_modular_koszul.tex:3770	Bar-intrinsic MC2
thm:e1-mc-element	CLAIM	ProvedHere	theorem	chapters/theory/e1_modular_koszul.tex:291	$E_1$ Maurer--Cartan element
exec
/bin/zsh -lc 'rg -n "2845|3673|`maintheorem`|casimir_divisor_core_transport|dg_shifted_factorization_bridge|holomorphic_topological|kontsevich_integral|physical_origins|shifted_rtt_duality_orthogonal_coideals|thqg_concordance_supplement|thqg_critical_string_dichotomy|thqg_fredholm_partition_functions|thqg_gravitational_complexity|thqg_gravitational_s_duality|thqg_gravitational_yangian|thqg_holographic_reconstruction|thqg_modular_bootstrap|thqg_perturbative_finiteness|thqg_preface_supplement|thqg_soft_graviton_theorems|thqg_symplectic_polarization|twisted_holography_quantum_gravity|typeA_baxter_rees_theta|ym_boundary_theory|ym_higher_body_couplings|ym_instanton_screening" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 2898

zsh:1: command not found: maintheorem
1:# Theorem Registry
2:
3:Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
4:
5:This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
6:
7:## Snapshot
8:
9:| Metric | Value |
10:|---|---:|
11:| ProvedHere claims | 2367 |
12:| Total tagged claims | 3113 |
13:| Active files in `main.tex` | 85 |
14:| Total `.tex` files scanned | 104 |
15:
16:## Status Totals
17:

thinking
**Correcting grep command**

I encountered an issue with backticks in the shell command, which caused the whole file to print instead of executing as intended. I think we should rerun the proper grep command instead. Earlier, we used the rg command for deleted files, which returned no matches, but that’s logged. Now it’s time to ensure everything is clean and correct. I need to run a proper grep with single quotes around the regex to target deleted file names and old snapshot values.
codex
One verification command was malformed by shell backticks, so I’m rerunning the forbidden-pattern pass cleanly. The goal is narrow: confirm the updated registry does not still mention deleted chapter files or the old stale snapshot counts.
exec
/bin/zsh -lc "rg -n '2845|3673|casimir_divisor_core_transport|dg_shifted_factorization_bridge|holomorphic_topological|kontsevich_integral|physical_origins|shifted_rtt_duality_orthogonal_coideals|thqg_concordance_supplement|thqg_critical_string_dichotomy|thqg_fredholm_partition_functions|thqg_gravitational_complexity|thqg_gravitational_s_duality|thqg_gravitational_yangian|thqg_holographic_reconstruction|thqg_modular_bootstrap|thqg_perturbative_finiteness|thqg_preface_supplement|thqg_soft_graviton_theorems|thqg_symplectic_polarization|twisted_holography_quantum_gravity|typeA_baxter_rees_theta|ym_boundary_theory|ym_higher_body_couplings|ym_instanton_screening' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
374:| `thm:chiral-homology-recovery` | `theorem` | 3673 | Chiral homology recovery |

thinking
**Refining data extraction**

Oops! It looks like I matched 3673 as a line number instead of snapshot count. I need to refine this with the exact details, like `| Total tagged claims | 3673 |` and also consider `| ProvedHere claims | 2845 |`. I'm realizing I might need to delete names and possibly use multiple regex searches. Alright, it looks like I have to rerun the process for accuracy. Let's tackle this!
codex
The broad numeric grep hit an unrelated line number, so I’m narrowing it to exact stale snapshot rows plus the deleted-file names. That gives a meaningful pass/fail for this metadata file.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
text=Path('metadata/theorem_registry.md').read_text()
patterns={
    'old_proved_row':'| ProvedHere claims | 2845 |',
    'old_total_row':'| Total tagged claims | 3673 |',
    'old_scanned_row':'| Total "'`.tex` files scanned | 128 |'"',
}
deleted=[
'casimir_divisor_core_transport','dg_shifted_factorization_bridge','holomorphic_topological',
'kontsevich_integral','physical_origins','shifted_rtt_duality_orthogonal_coideals',
'thqg_concordance_supplement','thqg_critical_string_dichotomy','thqg_fredholm_partition_functions',
'thqg_gravitational_complexity','thqg_gravitational_s_duality','thqg_gravitational_yangian',
'thqg_holographic_reconstruction','thqg_modular_bootstrap','thqg_perturbative_finiteness',
'thqg_preface_supplement','thqg_soft_graviton_theorems','thqg_symplectic_polarization',
'twisted_holography_quantum_gravity','typeA_baxter_rees_theta','ym_boundary_theory',
'ym_higher_body_couplings','ym_instanton_screening']
for name,pat in patterns.items():
    print(name, pat in text)
for name in deleted:
    if name in text:
        print('FOUND_DELETED', name)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
old_proved_row False
old_total_row False
old_scanned_row False
Plan update
Regenerated the assigned registry file from the live extractor and verified the updated snapshot against fresh extraction plus concordance-critical labels. The post-edit grep confirmed the stale snapshot rows and deleted-chapter references are gone.
  ✓ Read mandatory context and locate concordance-critical labels in live TeX sources
  ✓ Compare current theorem registry against live proved-claim extraction and isolate drift
  ✓ Regenerate only metadata/theorem_registry.md from the live claim surface
  ✓ Re-read the updated registry and grep modified file for coherence/forbidden patterns
codex
Updated [metadata/theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md) to match the current TeX tree.

FIXED: stale snapshot totals. The registry had `2845` proved claims, `3673` tagged claims, and `128` scanned `.tex` files; the live extractor now gives `2367`, `3113`, and `104`, and the file now reflects those values.

FIXED: stale proved-claim surface from deleted chapters. The old registry still indexed many claims from deleted connection files; the regenerated registry no longer mentions those files.

FIXED: stale line references for concordance-critical proved claims. Examples now aligned with source:
- `thm:bar-cobar-isomorphism-main` -> `chapters/theory/chiral_koszul_pairs.tex:4014`
- `thm:higher-genus-inversion` -> `chapters/theory/higher_genus_complementarity.tex:4440`
- `thm:bar-cobar-inversion-qi` -> `chapters/theory/bar_cobar_adjunction_inversion.tex:1606`
- `thm:modular-characteristic` -> `chapters/theory/higher_genus_modular_koszul.tex:2844`
- `thm:mc2-bar-intrinsic` -> `chapters/theory/higher_genus_modular_koszul.tex:3770`

FIXED: concordance cross-check for proved labels. The registry includes the concordance’s `ProvedHere` theorem/proposition labels that should appear there.

FIXED: correct absences from the proved registry. These are not disagreements:
- `thm:shifted-symplectic-complementarity` is `Conditional`, so it should not appear.
- `def:scalar-lane` and `def:modular-convolution-dg-lie` are definitions, not `ProvedHere` claims.
- `thm:modular-koszul-duality-main` is a label-only intro anchor, not a tagged theorem block.

BLOCKED: none.

Verification: a fresh extraction after the edit matches the registry snapshot exactly, and a post-edit grep found no stale snapshot rows or references to deleted chapter files in `metadata/theorem_registry.md`.
tokens used
94,749
