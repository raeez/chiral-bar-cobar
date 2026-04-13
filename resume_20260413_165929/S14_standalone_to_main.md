# S14_standalone_to_main (838s)

- [CRITICAL] `standalone/programme_summary.tex:1600` — PROBLEM: the Swiss-cheese seam is stale and self-contradictory. This section first says `\mathrm{SC}^{\mathrm{ch,top}}` emerges on the derived center pair, then the table at `1600`-`1608` reassigns the closed/open colors to the bar differential and deconcatenation, the prose at `1614`-`1617` says the bar differential “acquires curvature `\kappa(\cA)\cdot\omega_g`”, the hierarchy table at `1785` reduces the 3d layer to plain `E_1`, and the class summary at `1432` and `1812` calls classes `\mathbf{G},\mathbf{L}` “Swiss-cheese-formal bar complexes.” Main text rejects all of this: [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1248) puts `\SCchtop` on the derived center pair, not the bar complex; [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2695) says `d^2=0` always for the bar differential; [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2876) says SC-formality holds iff class `\mathbf{G}`. FIX: rewrite `sec:swiss-cheese` to match `princ:sc-two-incarnations`; delete the closed/open color table or replace it with a bar-vs-derived-center separation table; replace “acquires curvature `\kappa\omega_g`” with “the bar differential still satisfies `d_{\bar B}^2=0`; curvature appears on the curved `A_\infty`/fiber side”; change the 3d row at `1785` to `\SCchtop` on the derived center pair; change the class statements at `1432` and `1812` to “finite shadow depth for classes `\mathbf{G},\mathbf{L}`; SC-formality only for class `\mathbf{G}`.”

- [CRITICAL] `standalone/programme_summary_sections5_8.tex:300` — PROBLEM: this split standalone preserves the same broken Swiss-cheese story as the full summary. The table at `300`-`308` identifies SC colors with `d_{\bar B}` and `\Delta`, the prose at `314`-`317` again attributes curvature to the bar differential, the hierarchy table at `485` reduces the 3d layer to `E_1`, and the class summary at `134` says classes `\mathbf{G},\mathbf{L}` have “Swiss-cheese-formal bar complexes.” These all conflict with [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1248), [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2695), and [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2876). FIX: make the same rewrite as above in this extract; do not keep a second, stale version of the Swiss-cheese summary.

- [CRITICAL] `chapters/theory/ordered_associative_chiral_kd.tex:11428` — PROBLEM: this chapter contains phantom labels that duplicate real labels already defined elsewhere in the main manuscript: `ch:derived-langlands` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), `ch:genus1-seven-faces` duplicates [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2), `ch:holographic-datum-master` duplicates [chapters/connections/holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), `ch:landscape-census` duplicates [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:2), `comp:bp-kappa-three-paths` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), `conv:three-hochschild` duplicates [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:115), `prop:nilpotent-transport-typeA` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:1519), and `thm:langlands-bar-bridge` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:95). FIX: delete every duplicate phantom label in this block. Where cross-references are needed, point to the real chapter labels; if a local placeholder is unavoidable, rename it with a non-colliding prefix such as `placeholder:`.

- [HIGH] `chapters/theory/ordered_associative_chiral_kd.tex:40` — PROBLEM: the chapter manufactures seam anchors for content that was never integrated: `def:chiral-coproduct`, `eq:bar-degree1-yangian`, `eq:yangian-drinfeld-coprod`, and `eq:yangian-qybe` exist here only as `\phantomsection\label{...}` stubs, while the actual content still lives in `standalone/ordered_chiral_homology.tex` at `2523`, `8978`, `781`, and `684`. That is not integration; it is dead scaffolding. FIX: either import the actual definition/equation blocks into the chapter at the correct logical locations, or rename these stubs to `placeholder:*` and update any local references so the main manuscript stops pretending the content is present.

- [HIGH] `standalone/ordered_chiral_homology.tex:111` — PROBLEM: the standalone suppresses epistemic status by defining claim-status macros as empty no-ops. The file still uses those macros on live theorem surfaces, e.g. `\ClaimStatusProvedHere` at `4107` and `4319`, but the printed standalone erases the status boundary completely. That is exactly how stale claims survive migration. FIX: replace the empty definitions at `112`-`115` with visible markers matching the survey standalones, e.g. `\textsuperscript{\textsc{[ph]}}`, `\textsuperscript{\textsc{[pe]}}`, `\textsuperscript{\textsc{[cj]}}`, `\textsuperscript{\textsc{[he]}}`, or load the shared claim-status macro block.

- [HIGH] `standalone/ordered_chiral_homology.tex:455` — PROBLEM: the standalone and the chapter reuse the same theorem labels for materially different theorem surfaces. `thm:e3-cs` here is “Derived centre, topologization, and Chern--Simons” with a three-part affine bulk package/topologization statement, while [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4112) uses `thm:e3-cs` for “The `\Ethree`-algebra and Chern--Simons” with a different four-part statement and explicit `\ClaimStatusProvedElsewhere`. The same drift hits `thm:cfg` at `5905`, which cites `CFG26` while the chapter theorem at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4148) cites `CFG25` and carries status. FIX: do one of two things, and only one: either rename the standalone labels to `thm:e3-cs-standalone` / `thm:cfg-standalone` and update local refs, or rewrite the standalone theorems to match the chapter statements and statuses exactly, including the repository citation key.

- [MEDIUM] `standalone/classification.tex:38` — PROBLEM: this standalone globally redefines `\ref` to silently print “full monograph” on missing labels. The same seam-masking hack recurs at `standalone/computations.tex:33`, `standalone/programme_summary_sections2_4.tex:63`, `standalone/programme_summary_sections5_8.tex:62`, `standalone/programme_summary_sections9_14.tex:61`, `standalone/introduction_full_survey.tex:107`, `standalone/riccati.tex:36`, `standalone/survey_modular_koszul_duality.tex:102`, `standalone/survey_modular_koszul_duality_v2.tex:165`, `standalone/survey_track_a_compressed.tex:94`, and `standalone/survey_track_b_compressed.tex:149`. This hides broken seam refs instead of fixing them. FIX: remove the global `\renewcommand{\ref}` in each file; if a fallback is genuinely needed, introduce a dedicated macro such as `\fullmonoref{...}` only at the intended out-of-scope references and leave ordinary `\ref` unresolved until the labels are synced.

- [LOW] `standalone/ordered_chiral_homology.tex:39` — PROBLEM: integration-target standalones still use unguarded `\newcommand` blocks instead of `\providecommand`, so they are not safe to port into chapter files. The same problem appears at `standalone/N1_koszul_meta.tex:34`, `standalone/N3_e1_primacy.tex:34`, `standalone/N4_mc4_completion.tex:33`, `standalone/N5_mc5_sewing.tex:33`, `standalone/bp_self_duality.tex:36`, `standalone/classification_trichotomy.tex:33`, `standalone/chiral_chern_weil.tex:37`, and `standalone/programme_summary_section1.tex:36`. FIX: convert all manuscript-shared preamble symbols in these files from `\newcommand` to `\providecommand`, following the chapter-side pattern in [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5); keep any true override behind a standalone-only guard instead of making it global.

## Summary
Checked: 52 | Findings: 8 | Verdict: FAIL


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
session id: 019d875a-d422-7d63-aaf9-56e9f20fc839
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


MISSION: SEAM AUDIT between standalone/ and chapters/.

Standalones→Main manuscript. Check: (a) formulas in standalone papers match the main text, (b) no convention drift, (c) macros defined via providecommand, (d) no stale claims

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers
codex
Using `deep-beilinson-audit` for this seam review. I’m first mapping the `standalone/` surfaces against `chapters/`, then I’ll read the overlap points directly and only report findings I can pin to exact lines with a concrete fix.
exec
/bin/zsh -lc "printf 'SKILL\\n'; sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md; printf '\\nFILES\\n'; rg --files standalone chapters | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
SKILL
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
**Evaluating file access methods**

I need to read required files, and maybe using a parallel approach makes sense. The instructions suggest starting with explorers, so I'll consider that to map standalone sections to chapters. However, the user wants claims grounded in actual file contents, so I should inspect key constitutional files and focus on the relevant lines without needing the entire documents. I'll search for standalone mentions to identify corresponding chapters, while also considering the file types we should prioritize for comparison, like .tex over PDFs.
thinking
**Auditing file contents**

I realize there could be many files to review, and I need to exhaustively audit these. It seems essential to determine all standalone .tex files and see if they are present in the chapters, since some may be article versions. I need to identify overlaps carefully and look for transition points, such as `\input{standalone/...}`. Searching for standalone titles or theorem labels in chapters could help, and I might even run a script to compare labels and check for stale claims. Let's focus on reading the relevant portions of the files.
codex
I have the audit surface mapped at a high level. Next I’m reading the constitution files and then building an explicit standalone→chapter overlap map so the findings stay pinned to real seam points rather than superficial filename similarity.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

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

thinking
**Considering text processing options**

I need to be careful with my approach, maybe skipping Python this time. I could use tools like rg, sed, or awk to handle this. A simple shell command should be sufficient. I’ll use rg with the -n flag for line numbers while focusing on patterns. The goal is to extract titles and check for the `\providecommand` presence in a standalone context. Let's see how this goes!
codex
I’ve loaded the repo-wide constraints and concordance. Now I’m building a concrete overlap inventory: standalone titles, local macros, and labels, so I can compare only actual seam surfaces and not manufacture mismatches from unrelated files.
exec
/bin/zsh -lc 'rg -n "standalone/|ordered chiral homology|virasoro r-matrix|shadow towers|seven faces|w3 holographic|gaudin from collision|garland lepowsky|riccati|three parameter|classification trichotomy|chiral chern|programme summary|survey modular koszul|introduction full survey|N1|N2|N3|N4|N5|N6|bp self duality|koszul meta" chapters standalone' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "for f in standalone/*.tex; do printf 'FILE %s\\n' \""'$f"; rg -n '"'"'^'"\\\\title|"'^'"\\\\providecommand|"'^'"\\\\newcommand|"'^'"\\\\renewcommand|"'^'"\\\\def|"'^'"\\\\ClaimStatus|"'^'"\\\\begin\\{(theorem|proposition|lemma|corollary|conjecture|remark|definition)\\}|"'^'"\\\\label\\{' \""'$f"; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/N6_shadow_formality.tex:88:\subjclass[2020]{17B69, 18M70, 18N40, 81T40}
standalone/cover_letter_virasoro_r_matrix.tex:8:Waterloo, ON N2L 2Y5, Canada\\
standalone/gaudin_from_collision.tex:513:The Gaudin identification is one of the seven faces of the collision
standalone/shadow_towers_v2.tex:74: Waterloo, ON N2L 2Y5, Canada}
standalone/shadow_towers_v2.tex:236:equation of degree~$2$ in~$\wp'$. Here three parameters
standalone/shadow_towers_v2.tex:487:\input{riccati}
standalone/shadow_towers_v2.tex:551:Parts (i)--(ii) are proved in Theorem~\ref{thm:riccati-algebraicity}
standalone/shadow_towers_v2.tex:777:\textit{The seven faces of the collision residue},
standalone/riccati.tex:48:% riccati.tex — §3--4 of the standalone paper
standalone/riccati.tex:223:\label{thm:riccati-algebraicity}
standalone/riccati.tex:231:\label{eq:riccati-algebraic-relation}
standalone/riccati.tex:245:The claim \eqref{eq:riccati-algebraic-relation} is equivalent to
standalone/riccati.tex:304:The equivalence of \eqref{eq:riccati-algebraic-relation} with
standalone/riccati.tex:311:\label{rem:riccati-ode}
standalone/riccati.tex:314:\eqref{eq:riccati-algebraic-relation} is equivalent to the
standalone/riccati.tex:317:\label{eq:riccati-ode}
standalone/riccati.tex:371:by Theorem~\ref{thm:riccati-algebraicity}, comparing
standalone/riccati.tex:462:The classification follows from Theorem~\ref{thm:riccati-algebraicity}
chapters/examples/w_algebras_deep.tex:641:algebraicity theorem (Theorem~\ref{thm:riccati-algebraicity}) applies
chapters/examples/w_algebras_deep.tex:3374:theorem~\cite{BFN18} identifies $\mathcal{M}_C$ with the Slodowy
 succeeded in 112ms:
36:\providecommand{\cA}{\mathcal{A}}
37:\providecommand{\cD}{\mathcal{D}}
38:\providecommand{\cH}{\mathcal{H}}
39:\providecommand{\cM}{\mathcal{M}}
40:\providecommand{\cW}{\mathcal{W}}
41:\providecommand{\barB}{\overline{B}}
42:\providecommand{\Ran}{\mathrm{Ran}}
43:\providecommand{\FM}{\overline{\mathrm{FM}}}
44:\providecommand{\Conf}{\mathrm{Conf}}
45:\providecommand{\fg}{\mathfrak{g}}
46:\providecommand{\Sym}{\mathrm{Sym}}
47:\providecommand{\Res}{\operatorname{Res}}
48:\providecommand{\Spec}{\operatorname{Spec}}
49:\providecommand{\Diff}{\mathrm{Diff}}
50:\providecommand{\Vir}{\mathrm{Vir}}
51:\providecommand{\Hom}{\mathrm{Hom}}
52:\providecommand{\id}{\mathrm{id}}
53:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
54:\renewcommand{\Bbbk}{\mathbf{C}}
63:\renewcommand{\ref}[1]{%


thinking
**Clarifying standalone file issues**

I need to address every standalone file that's intended for porting. The exact fix is to replace definitions with `\providecommand` or guards, but there might be multiple instances to consider. The user wants any mismatches or gaps noted, especially concerning seams caused by using `\newcommand`. I could categorize findings by file, mentioning line ranges. I need to ensure that modifications for local macros are clear, particularly in regards to `\newcommand` and `\providecommand`. Ultimately, it's crucial to prevent collisions in the main manuscript.
thinking
**Comparing formulas in documents**

I need to compare formulas in standalone files against those in chapters to identify actual mismatches. It's a good idea to use grep for specific formulas like r-matrix, kappa, S_2, and others. This is part of the seam audit, and I also have to consider stale claims—some standalones might make stronger statements than what's in the chapters. A potential strategy would be to map standalones with overlapping themes and then search for each standalone title within the chapters using their file names.
codex
I’ve got the broad inventory. The next pass is mechanical: shared labels and canonical hot-formula grep across `standalone/` and `chapters/`, which is the fastest way to expose real seam drift rather than just prose differences.
exec
/bin/zsh -lc "rg -n 'kappa\\(|r\\"'^|r'"\\(|S_2\\s*=|S_4\\s*=|B\\(A\\)\\s*=|T\\"'^c'"\\(s\\"'^{-1}|SC'"\\"'^'"\\{ch,top\\}|Swiss|bar complex|ordered chiral homology|critical level|k=0|k=-h\\"'^v|c/2|H_N - 1|H_'"\\{N-1\\}|\\Omega/z|q\\"'^'"\\{1/24\\}|F_2\\s*=\\s*7/5760|98/3|196|13/2' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -n '"'"'^'"\\\\label\\{' standalone/*.tex | sed -E 's#"'^([''^:]+):([0-9]+):'"\\\\label\\{(["'^}]*)'"\\}#\\3\\t\\1\\t\\2#' | sort > \""'$tmp1"; rg -n '"'"'^'"\\\\label\\{' chapters/**/*.tex | sed -E 's#"'^([''^:]+):([0-9]+):'"\\\\label\\{(["'^}]*)'"\\}#\\3\\t\\1\\t\\2#' | sort > \""'$tmp2"; join -t $'"'\\t' -1 1 -2 1 \""'$tmp1" "$tmp2" | sed -n '"'1,260p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:kappa\(|r\^|r\(|S_2\s*=|S_4\s*=|B\(A\)\s*=|T\^c\(s\^{-1}|SC\^\{ch,top\}|Swiss|bar complex|ordered chiral homology|critical level|k=0|k=-h\^v|c/2|H_N - 1|H_\{N-1\}|\Omega/z|q\^\{1/24\}|F_2\s*=\s*7/5760|98/3|196|13/2)
                                                            ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
ch:preface	standalone/survey_modular_koszul_duality.tex	111	chapters/frame/preface.tex	19
constr:chiral-p3-bracket	standalone/ordered_chiral_homology.tex	6765	chapters/theory/en_koszul_duality.tex	5221
conv:hms-levels	standalone/introduction_full_survey.tex	5270	chapters/theory/introduction.tex	2543
conv:standing-assumptions	standalone/introduction_full_survey.tex	5338	chapters/theory/introduction.tex	2611
cor:bar-encodes-all	standalone/ordered_chiral_homology.tex	5149	chapters/theory/ordered_associative_chiral_kd.tex	8055
cor:gaussian-decomposition	standalone/riccati.tex	331	chapters/theory/higher_genus_modular_koszul.tex	17543
cor:mc3-all-types	standalone/N2_mc3_all_types.tex	734	chapters/examples/yangians_computations.tex	4220%
def:chiral-ass-operad	standalone/introduction_full_survey.tex	5075	chapters/theory/algebraic_foundations.tex	2231
def:chiral-ce-complex	standalone/ordered_chiral_homology.tex	6739	chapters/theory/en_koszul_duality.tex	5195
def:e1-chiral	standalone/introduction_full_survey.tex	5058	chapters/theory/algebraic_foundations.tex	2214
def:einf-chiral	standalone/introduction_full_survey.tex	5025	chapters/theory/algebraic_foundations.tex	2181
def:filtered-e3-chiral	standalone/ordered_chiral_homology.tex	6895	chapters/theory/en_koszul_duality.tex	5351
def:ord-ch-g2	standalone/ordered_chiral_homology.tex	9841	chapters/theory/higher_genus_modular_koszul.tex	33239
def:pinf-chiral	standalone/introduction_full_survey.tex	5101	chapters/theory/algebraic_foundations.tex	2257
def:shadow-growth-rate	standalone/riccati.tex	527	chapters/theory/higher_genus_modular_koszul.tex	19754
def:shadow-metric	standalone/shadow_towers.tex	617	chapters/theory/higher_genus_modular_koszul.tex	17405
def:shadow-radius	standalone/shadow_towers.tex	1113	chapters/theory/higher_genus_modular_koszul.tex	19755
ex:gl2-chiral-qg	standalone/ordered_chiral_homology.tex	4608	chapters/theory/ordered_associative_chiral_kd.tex	9417
ex:heis-coproduct	standalone/ordered_chiral_homology.tex	3624	chapters/theory/ordered_associative_chiral_kd.tex	8226
ex:sl2-chiral-e3	standalone/ordered_chiral_homology.tex	7761	chapters/theory/en_koszul_duality.tex	6199

thinking
**Considering environment extraction**

I’m thinking about extracting the environmental information that comes before each label in standalone sections and chapters. Since the user mentioned they want no stale claims, it sounds like a good idea to compute the shared labels for environment and status. This approach should help ensure the data I present is fresh and accurate. I'm curious to see how it all comes together!
exec
/bin/zsh -lc "node - <<'NODE'
const fs=require('fs');
const cp=require('child_process');
function parse(file){
  const lines=fs.readFileSync(file,'utf8').split(/\\n/);
  const out=[];
  let curEnv=null, curStatus='';
  for(let i=0;i<lines.length;i++){
    const line=lines[i];
    const env=line.match(/"'^'"\\\\begin\\{(theorem|proposition|lemma|corollary|conjecture|remark|definition|convention|maintheorem|computation|verification|calculation)\\}/);
    if(env) curEnv=env[1];
    const st=line.match(/\\\\ClaimStatus([A-Za-z]+)/);
    if(st) curStatus=st[1];
    const lab=line.match(/"'^'"\\\\label\\{(["'^}]*)'"\\}/);
    if(lab) out.push({label:lab[1], file, line:i+1, env:curEnv||'', status:curStatus||''});
  }
  return out;
}
const standalone=cp.execSync(\"rg --files standalone -g '*.tex'\",{encoding:'utf8'}).trim().split(/\\n/).filter(Boolean);
const chapters=cp.execSync(\"rg --files chapters -g '*.tex'\",{encoding:'utf8'}).trim().split(/\\n/).filter(Boolean);
const S=new Map();
for(const f of standalone) for(const x of parse(f)) { if("'!S.has(x.label)) S.set(x.label,[]); S.get(x.label).push(x); }
const C=new Map();
for(const f of chapters) for(const x of parse(f)) { if(!C.has(x.label)) C.set(x.label,[]); C.get(x.label).push(x); }
const labels=[...S.keys()].filter(k=>C.has(k)).sort();
for(const k of labels){
  const s=S.get(k); const c=C.get(k);
  for(const a of s) for(const b of c){
    console.log([k,`${a.file}:${a.line}:${a.env}:${a.status||'"'-'}"'`,`${b.file}:${b.line}:${b.env}:${b.status||'"'-'}"'`].join('"'\\t'));
  }
}
NODE" in /Users/raeez/chiral-bar-cobar succeeded in 84ms:
ch:preface	standalone/survey_modular_koszul_duality.tex:111::Conditional	chapters/frame/preface.tex:19::-
constr:chiral-p3-bracket	standalone/ordered_chiral_homology.tex:6765:definition:ProvedHere	chapters/theory/en_koszul_duality.tex:5221:definition:ProvedHere
conv:hms-levels	standalone/introduction_full_survey.tex:5270:convention:ProvedHere	chapters/theory/introduction.tex:2543:convention:ProvedHere
conv:standing-assumptions	standalone/introduction_full_survey.tex:5338:convention:ProvedHere	chapters/theory/introduction.tex:2611:convention:ProvedHere
cor:bar-encodes-all	standalone/ordered_chiral_homology.tex:5149:corollary:ProvedHere	chapters/theory/ordered_associative_chiral_kd.tex:8055:corollary:ProvedHere
cor:gaussian-decomposition	standalone/riccati.tex:331:corollary:-	chapters/theory/higher_genus_modular_koszul.tex:17543:corollary:ProvedHere
cor:mc3-all-types	standalone/N2_mc3_all_types.tex:734:corollary:-	chapters/examples/yangians_computations.tex:4220:corollary:ProvedHere
def:chiral-ass-operad	standalone/introduction_full_survey.tex:5075:definition:ProvedHere	chapters/theory/algebraic_foundations.tex:2231:definition:ProvedElsewhere
def:chiral-ce-complex	standalone/ordered_chiral_homology.tex:6739:definition:ProvedHere	chapters/theory/en_koszul_duality.tex:5195:definition:ProvedHere
def:e1-chiral	standalone/introduction_full_survey.tex:5058:definition:ProvedHere	chapters/theory/algebraic_foundations.tex:2214:definition:ProvedElsewhere
def:einf-chiral	standalone/introduction_full_survey.tex:5025:definition:ProvedHere	chapters/theory/algebraic_foundations.tex:2181:definition:ProvedElsewhere
def:filtered-e3-chiral	standalone/ordered_chiral_homology.tex:6895:definition:ProvedHere	chapters/theory/en_koszul_duality.tex:5351:definition:ProvedHere
def:ord-ch-g2	standalone/ordered_chiral_homology.tex:9841:definition:ProvedHere	chapters/theory/higher_genus_modular_koszul.tex:33239:definition:ProvedHere
def:pinf-chiral	standalone/introduction_full_survey.tex:5101:definition:ProvedHere	chapters/theory/algebraic_foundations.tex:2257:definition:ProvedHere
def:shadow-growth-rate	standalone/riccati.tex:527:definition:-	chapters/theory/higher_genus_modular_koszul.tex:19754:definition:ProvedHere
def:shadow-metric	standalone/shadow_towers.tex:617:definition:-	chapters/theory/higher_genus_modular_koszul.tex:17405:definition:Conjectured
def:shadow-radius	standalone/shadow_towers.tex:1113:definition:-	chapters/theory/higher_genus_modular_koszul.tex:19755:definition:ProvedHere
ex:gl2-chiral-qg	standalone/ordered_chiral_homology.tex:4608:lemma:ProvedHere	chapters/theory/ordered_associative_chiral_kd.tex:9417:remark:ProvedHere
ex:heis-coproduct	standalone/ordered_chiral_homology.tex:3624:remark:Heuristic	chapters/theory/ordered_associative_chiral_kd.tex:8226:remark:ProvedHere
ex:sl2-chiral-e3	standalone/ordered_chiral_homology.tex:7761:proposition:ProvedHere	chapters/theory/en_koszul_duality.tex:6199:proposition:ProvedHere

thinking
**Identifying relevant patterns**

This seems huge but manageable if I search systematically for known problem patterns and shared labels. Maybe I should use an explorer agent to scan for seam drift. It could be beneficial to audit the standalone chapters for any drift and return the relevant files. Since the user didn't explicitly ask for parallel work, I will conduct my own audit. I’ll identify relevant standalones like `ordered_chiral_homology`, `riccati`, and others to narrow my search effectively.
exec
/bin/zsh -lc "rg -n 'STANDALONE|standalone|companion papers|NEW MATERIAL FROM STANDALONE|extracts the essential|ported from|migrated from' chapters standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/computations.tex:46:% COMPUTATIONS.TEX -- Sections 7--8 of the standalone paper
standalone/computations.tex:50:\begin{remark}[Relationship to companion papers]
standalone/computations.tex:581:\begin{theorem}[DS-HPL transfer]\label{thm:ds-hpl-standalone}
standalone/computations.tex:611:\label{thm:grav-primitivity-standalone}
standalone/computations.tex:736:Theorem~\ref{thm:grav-primitivity-standalone} proves this for
standalone/classification.tex:50:%% classification.tex — §5--6 of the standalone paper
standalone/classification.tex:53:\begin{remark}[Relationship to companion papers]
standalone/classification.tex:720:transformation. The depth gap (Proposition~\ref{prop:depth-gap-standalone})
standalone/classification.tex:725:(Proposition~\ref{prop:sc-formality-standalone}) shows that
standalone/classification.tex:728:(Proposition~\ref{prop:betagamma-contact-standalone}) reveals
standalone/classification.tex:731:(Conjecture~\ref{conj:ds-shadow-escalation-standalone})
standalone/classification.tex:734:(Proposition~\ref{prop:shadow-semilattice-standalone}) shows that
standalone/classification.tex:775:\begin{proposition}[Depth gap]\label{prop:depth-gap-standalone}
standalone/classification.tex:834:Proposition~\ref{prop:betagamma-contact-standalone} below.
standalone/classification.tex:869:\label{prop:sc-formality-standalone}
standalone/classification.tex:916:\label{rem:sc-vs-ainfty-standalone}
standalone/classification.tex:924:Proposition~\ref{prop:sc-formality-standalone} identifies the
standalone/classification.tex:954:\label{prop:betagamma-contact-standalone}
standalone/classification.tex:1078:\label{conj:ds-shadow-escalation-standalone}
standalone/classification.tex:1095:(Proposition~\ref{prop:depth-gap-standalone}) reduces the
codex
A concrete seam gap already surfaced: `ordered_associative_chiral_kd.tex` carries placeholder `\phantomsection\label{...}` markers explicitly tagged `TODO: integrate from standalone`. I’m reading those transition blocks now, because they’re stronger evidence than pattern-based drift.
exec
/bin/zsh -lc "sed -n '100,130p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11420,11450p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\DeclareMathOperator{\Perf}{Perf}
\DeclareMathOperator{\Rep}{Rep}
\DeclareMathOperator{\Cl}{Cl}
\DeclareMathOperator{\Mod}{Mod}
\DeclareMathOperator{\Hol}{Hol}
\renewcommand{\SS}{\mathbb{S}}
\newcommand{\HHH}{\mathbb{H}}

\numberwithin{equation}{section}

% Claim status macros (standalone: no-op definitions)
\providecommand{\ClaimStatusConjectured}{}
\providecommand{\ClaimStatusProvedHere}{}
\providecommand{\ClaimStatusProvedElsewhere}{}
\providecommand{\ClaimStatusHeuristic}{}

% ================================================================
\begin{document}

 succeeded in 51ms:
factors the Heisenberg sewing determinant over primes
via the unordered divisor function $\sigma_{-1}$.
The $\mathsf{E}_1$-ordered bar complex replaces
unordered by ordered factorizations; the analogous
ordered sewing lift should involve composition-weighted
divisor sums and factor in the ring of non-commutative
formal Dirichlet series.
\end{remark}
\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
\phantomsection\label{ch:genus1-seven-faces} % TODO: integrate from standalone
\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
\phantomsection\label{conv:three-hochschild} % TODO: integrate from standalone
\phantomsection\label{part:seven-faces} % TODO: integrate from standalone
\phantomsection\label{part:v1-frontier} % TODO: integrate from standalone
\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone
\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone
\phantomsection\label{sec:complementarity} % TODO: integrate from standalone
\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone
 succeeded in 51ms:
% Ordered Associative Chiral Koszul Duality
% Integration-ready chapter file (stripped from standalone amsart draft).
% Uses only \providecommand for macros that may not be in main.tex preamble.

\providecommand{\Assch}{\mathrm{Ass}^{\mathrm{ch}}}
\providecommand{\Barch}{\overline{B}^{\mathrm{ch}}}
\providecommand{\Cobar}{\Omega^{\mathrm{ch}}}
\providecommand{\coHoch}{\operatorname{coHH}}
\providecommand{\Cotor}{\operatorname{Cotor}}
\providecommand{\Coext}{\operatorname{Coext}}
\providecommand{\RHom}{R\!\operatorname{Hom}}
\providecommand{\Tot}{\operatorname{Tot}}
\providecommand{\KK}{\mathbb{K}}
\providecommand{\Dpbw}{D^{\mathrm{pbw}}}
\providecommand{\Dco}{D^{\mathrm{co}}}
\providecommand{\chotimes}{\mathbin{\otimes^{\mathrm{ch}}}}
\providecommand{\wt}{\widetilde}
\providecommand{\eps}{\varepsilon}
\providecommand{\susp}{s}
\providecommand{\coeq}{\operatorname{coeq}}

thinking
**Searching for patterns**

I’m thinking about the phantom labels and I definitely need to dig deeper. I’ll inspect formula drift and perhaps run multiple regex commands to identify forbidden patterns given their complexity. I’m considering comparing formulas in overlapping files using `git diff --no-index`, but that might be too much. I should also look for suspicious duplicate label contexts linked to status mismatches. Before I do that, I might perform a targeted grep for patterns in standalone files only.
exec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega\\\\,d\\\\log z|r\\"'^Vir'"\\(z\\) = \\(c/2\\)/z\\"'^4|r'"\\"'^Vir'"\\(z\\) = \\(c/2\\)/z\\"'^2|S_2 = c/12|H_'"\\{N-1\\}|kappa\\(W_N\\) = c\\*H|kappa\\+kappa.?= 1/3|98/3|K_BP = 2|T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\|\\+1|q\\"'^'"\\{1/24\\}|1/\\(2\\\\pi\\)|7/2880|1/5760|SC\\"'^'"\\{ch,top\\}|Swiss-cheese|Swiss cheese|E_3-chiral|bar-cobar produces bulk|Omega\\(B\\(A\\)\\) is the Koszul dual|D_Ran\\(B\\(A\\)\\) is the cobar complex|B\\(A\\) is SC|SC coalgebra|Koszul self-dual' standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'providecommand|newcommand|renewcommand' standalone/*.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\Omega/z|\\Omega\\,d\\log z|r\^Vir\(z\) = \(c/2\)/z\^4|r\^Vir\(z\) = \(c/2\)/z\^2|S_2 = c/12|H_\{N-1\}|kappa\(W_N\) = c\*H|kappa\+kappa.?= 1/3|98/3|K_BP = 2|T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\|\+1|q\^\{1/24\}|1/\(2\\pi\)|7/2880|1/5760|SC\^\{ch,top\}|Swiss-cheese|Swiss cheese|E_3-chiral|bar-cobar produces bulk|Omega\(B\(A\)\) is the Koszul dual|D_Ran\(B\(A\)\) is the cobar complex|B\(A\) is SC|SC coalgebra|Koszul self-dual)
                                                                                                                                                                               ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
standalone/classification_trichotomy.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/classification_trichotomy.tex:34:\newcommand{\cM}{\mathcal{M}}
standalone/classification_trichotomy.tex:35:\newcommand{\barB}{\bar{B}}
standalone/classification_trichotomy.tex:36:\newcommand{\fg}{\mathfrak{g}}
standalone/classification_trichotomy.tex:37:\newcommand{\Walg}{\mathcal{W}}
standalone/classification_trichotomy.tex:38:\newcommand{\Vir}{\mathrm{Vir}}
standalone/classification_trichotomy.tex:39:\newcommand{\OPE}{\mathrm{OPE}}
standalone/classification_trichotomy.tex:40:\newcommand{\Res}{\operatorname{Res}}
standalone/classification_trichotomy.tex:41:\newcommand{\Sh}{\mathrm{Sh}}
standalone/classification_trichotomy.tex:249:\renewcommand{\arraystretch}{1.2}
standalone/classification_trichotomy.tex:319:\renewcommand{\arraystretch}{1.2}
standalone/classification_trichotomy.tex:449:\renewcommand{\arraystretch}{1.2}
standalone/chiral_chern_weil.tex:37:\newcommand{\cA}{\mathcal{A}}
standalone/chiral_chern_weil.tex:38:\newcommand{\cE}{\mathcal{E}}
standalone/chiral_chern_weil.tex:39:\newcommand{\cM}{\mathcal{M}}
standalone/chiral_chern_weil.tex:40:\newcommand{\cW}{\mathcal{W}}
standalone/chiral_chern_weil.tex:41:\newcommand{\Mbar}{\overline{\mathcal{M}}}
standalone/chiral_chern_weil.tex:42:\newcommand{\fg}{\mathfrak{g}}
standalone/chiral_chern_weil.tex:43:\newcommand{\fh}{\mathfrak{h}}
standalone/chiral_chern_weil.tex:44:\newcommand{\gmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
exec
/bin/zsh -lc "sed -n '200,280p' standalone/riccati.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17420,17540p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '176,214p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
Setting $a_n := (n+2)\,S_{n+2}$ for $n \geq 0$, this becomes
$H(t) = \sum_{n \geq 0} a_n \, t^{n+2}$, with initial values
$a_0 = 2\kappa$, $a_1 = 3\alpha$, $a_2 = 4S_4$.
\end{definition}

The weighted generating function $H$ packages the recursion
\eqref{eq:single-line-recursion} as a convolution identity.
Set $F(t) := H(t)/t^2 = \sum_{n \geq 0} a_n \, t^n$.
The MC recursion forces every Cauchy coefficient of $F^2$ beyond
degree~$2$ to vanish, so $F^2$ is a polynomial of degree~$2$.


% ================================================================
% §4. Algebraicity and the Depth Classification
% ================================================================

\section{Algebraicity and the depth classification}
\label{sec:algebraicity}

 succeeded in 51ms:
$S_2 =: \kappa$, and cubic coefficient
$S_3 =: \alpha$. Define the \emph{weighted initial data}
$a_0 := 2\kappa$, $a_1 := 3\alpha$, $a_2 := 4S_4$.
The \emph{shadow quadratic form on~$L$} (or \emph{shadow metric},
by analogy with its role in controlling the tower geometry; not a
Riemannian metric) is the quadratic polynomial
\begin{equation}\label{eq:shadow-metric}
 Q_L(t)
 \;:=\;
 a_0^2
 \;+\;
 2\,a_0\,a_1\,t
 \;+\;
 \bigl(a_1^2 + 2\,a_0\,a_2\bigr)\,t^2
 \;=\;
 4\kappa^2 + 12\kappa\alpha\,t
 + \bigl(9\alpha^2 + 16\kappa S_4\bigr)\,t^2
 \;\in\; k(c)[t].
\end{equation}
The \emph{critical discriminant} of~$L$ is
 succeeded in 50ms:
Theorems~D and~H are \emph{projectional outputs}: $\kappa$ is the scalar
trace of~$\Theta_\cA$, and the chiral Hochschild ring is a
polynomial consequence of Koszul functoriality.

\begin{itemize}
\item \textbf{Algebraicity}
 (Theorem~\ref{thm:riccati-algebraicity}).
 On any one-dimensional primary slice~$L$ of the cyclic
 deformation complex, the weighted shadow generating function
 $H(t) = \sum r\,S_r\,t^r$ satisfies
 $H(t)^2 = t^4 Q_L(t)$
 for an explicit quadratic polynomial~$Q_L$.
 The shadow obstruction tower is therefore algebraic of degree~$2$
 over $k(c)[t]$, determined by three invariants:
 the modular characteristic~$\kappa$, the cubic coefficient~$\alpha$,
 and the quartic shadow~$S_4$.

\item \textbf{Formality identification}
 (Theorem~\ref{thm:shadow-formality-identification}).
 The degree-$r$ shadow~$\operatorname{Sh}_r(\cA)$ has genus-$0$
exec
/bin/zsh -lc "rg -n 'SC\\"'^'"\\{ch,top\\}|Swiss-cheese|Swiss cheese|E_3-chiral|bar complex .*SC|SC.*bar complex|B\\(A\\).*SC|SC coalgebra|SC\\-coalgebra|bar-cobar produces bulk|Omega\\(B\\(A\\)\\).*Koszul dual|the Koszul dual equals the bar complex|D_\\\\Ran\\(B\\(A\\)\\).*cobar|derived center|bulk' standalone/ordered_chiral_homology.tex standalone/programme_summary*.tex standalone/survey_modular_koszul_duality*.tex standalone/introduction_full_survey.tex standalone/N3_e1_primacy.tex standalone/N1_koszul_meta.tex standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'SC\\"'^'"\\{ch,top\\}|Swiss-cheese|Swiss cheese|E_3-chiral|bar complex .*SC|SC.*bar complex|B\\(A\\).*SC|SC coalgebra|SC\\-coalgebra|bar-cobar produces bulk|Omega\\(B\\(A\\)\\).*Koszul dual|the Koszul dual equals the bar complex|D_\\\\Ran\\(B\\(A\\)\\).*cobar|derived center|bulk' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/theory/algebraic_foundations.tex chapters/theory/bar_construction.tex chapters/theory/hochschild_cohomology.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/N1_koszul_meta.tex:958:Swiss-cheese formality (which is the vanishing of higher
standalone/N1_koszul_meta.tex:961:is Swiss-cheese formal. In this paper we have focused on chiral
standalone/N3_e1_primacy.tex:170:ordered, while the closed (bulk) sector is symmetric; the
standalone/N3_e1_primacy.tex:849: In the open-closed picture this plays the role of the bulk:
standalone/N3_e1_primacy.tex:851: closed (bulk) sector. This functor is \emph{not} the bar--cobar
standalone/N3_e1_primacy.tex:865:``$\Barord(\cA)$ computes the bulk'' is category-theoretically
standalone/N3_e1_primacy.tex:866:ill-formed, because the bulk is the derived centre, not the bar.
standalone/N3_e1_primacy.tex:872:$\cA^{!}$; Hochschild cochains give the bulk. The averaging map
standalone/N3_e1_primacy.tex:924:the ribbonised Swiss-cheese construction provides the
standalone/N3_e1_primacy.tex:940:\subsection*{The Swiss-cheese and curved sectors}
standalone/N3_e1_primacy.tex:942:The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$, in its
standalone/N3_e1_primacy.tex:946:Swiss-cheese setting takes $\cA$ to the pair $(\cA, \cA)$ with
standalone/N3_e1_primacy.tex:949:Swiss-cheese degree $(k,m)$. The averaging map restricted to the
standalone/N3_e1_primacy.tex:954:Koszul theorem for the Swiss-cheese operad would give a unified
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary_sections5_8.tex:267:\section{The Swiss-cheese realization}
standalone/programme_summary_sections5_8.tex:278:on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
standalone/programme_summary_sections5_8.tex:279:$\mathrm{SC}^{\mathrm{ch,top}}$ emerges on the chiral derived center
standalone/programme_summary_sections5_8.tex:290:This product is the operadic fingerprint of the Swiss-cheese
standalone/programme_summary_sections5_8.tex:322:The directionality of the Swiss-cheese operad is strict:
 succeeded in 51ms:
chapters/theory/hochschild_cohomology.tex:9:obstructions, and bulk-field couplings.
chapters/theory/hochschild_cohomology.tex:895:\index{derived center|textbf}
chapters/theory/hochschild_cohomology.tex:899:The derived center of a dg-category is the derived endomorphisms of
chapters/theory/hochschild_cohomology.tex:977:\subsection{The derived center}
chapters/theory/hochschild_cohomology.tex:981:\index{derived center|textbf}
chapters/theory/hochschild_cohomology.tex:982:For a $k$-linear dg-category $\mathcal{C}$, the \emph{derived center}
chapters/theory/hochschild_cohomology.tex:1000:The bridge between the derived center and Hochschild cochains is the
chapters/theory/hochschild_cohomology.tex:1053:\index{derived center!Hochschild identification}
chapters/theory/hochschild_cohomology.tex:1054:\index{Hochschild cohomology!derived center}
chapters/theory/hochschild_cohomology.tex:1064:In particular, the derived center depends on $\mathcal{C}$ only up to
chapters/theory/hochschild_cohomology.tex:1075:The derived center is manifestly invariant under quasi-equivalence of
chapters/theory/hochschild_cohomology.tex:1229:\index{derived center!chiral application}
chapters/theory/hochschild_cohomology.tex:1284:Hochschild cochains are the derived center (deformations of the
chapters/theory/bar_construction.tex:2043:\index{Swiss-cheese!topological factorization on $\bR$}%
chapters/theory/bar_construction.tex:2054:Together they constitute the Swiss-cheese algebra
chapters/theory/algebraic_foundations.tex:2132:Swiss-cheese structure of Volume~II combines both.
chapters/theory/algebraic_foundations.tex:2325:Each notion admits its own derived center construction, and the
chapters/theory/algebraic_foundations.tex:2358:\item \emph{Swiss-cheese factorisation algebra on
chapters/theory/algebraic_foundations.tex:2366:  Output: mixed chiral-topological center: the derived center in
chapters/theory/algebraic_foundations.tex:2380:and~\textup{(ii)} via the Swiss-cheese mechanism;

thinking
**Investigating document inconsistencies**

I'm searching for potential inconsistencies between the standalone introduction and the program summary regarding SC. It's essential to compare the standalone `programme_summary.tex` against the chapter `en_koszul_duality`. I suspect there may be mismatches in theorem-level labels. There's a line that caught my attention: `standalone/programme_summary.tex:1785 "$3$ & Swiss-cheese & $E_1$"`, which may incorrectly summarize Swiss-cheese as E1 rather than SC/E2/E3. I need to inspect the surrounding context for clarification.
exec
/bin/zsh -lc "sed -n '2254,2286p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1768,1792p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '478,492p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
\end{tabular}
\end{center}

 succeeded in 52ms:
% ====================================================================
\subsection{The 4d--3d--2d resolution}
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
 succeeded in 52ms:
 Bar tables through high degree; OEIS; growth rates \\[6pt]
\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
\hline
Feynman diagrams (Ch.~\ref{ch:feynman}) &
 Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
BV-BRST (Ch.~\ref{ch:bv-brst}) &
 Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
 Derived center = universal bulk; open-sector primitive; four-stage architecture \\
HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
 3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
 Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
 Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
Arithmetic shadows (Ch.~\ref{chap:arithmetic-shadows}) &
 Shadow $L$-function; depth decomposition $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$; Eisenstein spectral content \\[6pt]
\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:seven-faces}: The Seven Faces of the Collision Residue} \emph{(archive-only)}} \\[3pt]
\hline
Holographic datum master (Ch.~\ref{ch:holographic-datum-master}) &
exec
/bin/zsh -lc "rg -n 'Volume~II|4d--3d--2d|Swiss-cheese.*E_1|Operadic type|dimensional hierarchy|E_1\\"'$; '"\\\\SCchtop|SCchtop.*derived center' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/concordance.tex standalone/programme_summary*.tex standalone/survey_modular_koszul_duality*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/programme_summary_sections5_8.tex:304:\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
standalone/programme_summary_sections5_8.tex:469:\subsection{The 4d--3d--2d resolution}
standalone/programme_summary_sections5_8.tex:474:of a dimensional hierarchy:
standalone/programme_summary_sections5_8.tex:480:\textbf{$d$} & \textbf{Level} & \textbf{Operadic type}
standalone/programme_summary_sections5_8.tex:485:$3$ & Swiss-cheese & $E_1$
standalone/programme_summary_sections5_8.tex:590:Volume~III.
standalone/survey_modular_koszul_duality_v2.tex:1518:(Volume~II).
standalone/survey_modular_koszul_duality_v2.tex:3509:chiral homology complex of Volume~II. The bulk-boundary-line triangle
standalone/survey_modular_koszul_duality_v2.tex:3892:Volume~II identifies the geometric substrate of the bar
standalone/survey_modular_koszul_duality_v2.tex:4330:The bridge is completed in Volume~II by the doubling theorem:
standalone/survey_modular_koszul_duality_v2.tex:4974:Volume~III extends the engine to Calabi--Yau geometry: forty-two
standalone/survey_modular_koszul_duality_v2.tex:4981:Volume~II develops the 3d theory in three new chapters: the
standalone/survey_modular_koszul_duality_v2.tex:4988:Volume~II programme.
standalone/survey_modular_koszul_duality_v2.tex:5010:tower). Volume~II identifies the local composition law (the
standalone/survey_modular_koszul_duality_v2.tex:5035:for $d = 3$; Volume~III).
standalone/programme_summary.tex:1604:\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
standalone/programme_summary.tex:1769:\subsection{The 4d--3d--2d resolution}
standalone/programme_summary.tex:1774:of a dimensional hierarchy:
standalone/programme_summary.tex:1780:\textbf{$d$} & \textbf{Level} & \textbf{Operadic type}
standalone/programme_summary.tex:1785:$3$ & Swiss-cheese & $E_1$

thinking
**Correcting inconsistencies**

I’ve noticed that the standalone program summary table isn’t matching the current main text. I need to determine the exact fix here. I think changing E1 to SC^{ch,top} or possibly using “Swiss-cheese / derived center” could be the answer. It would be helpful to inspect line 304 in sections 5 and 8 to ensure we’re addressing the inconsistency accurately. Let's take a closer look to clarify what's needed.
exec
/bin/zsh -lc "sed -n '296,308p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\toprule
& \textbf{Closed colour} & \textbf{Open colour} \\
\midrule
\textbf{Space} & $\FM_k(\Bbbk)$ & $\Conf_k(\mathbb{R})$ \\
\textbf{Structure} & Bar differential $d_{\barB}$ &
 Deconcatenation $\Delta$ \\
\textbf{Physics} & Holomorphic factorization & Topological
 factorization \\
\textbf{Operadic type} & $E_\infty$ & $E_1$ \\
\textbf{Coalgebra} & $\Sym^c(s^{-1}\bar\cA)$ &
 $T^c(s^{-1}\bar\cA)$ \\
\textbf{Coproduct} & Coshuffle ($2^n$ terms) &
 Deconcatenation ($n+1$ terms) \\

thinking
**Examining color assignments**

I’m noticing something off about this table: it mentions closed color “bar differential” and open color “deconcatenation.” That makes me wonder if we're conflating forbidden SC colors. It categorizes bar differential and deconcatenation as Swiss-cheese closed/open structures, but according to AGENTS B54-B55-B56, those aren't SC colors. SC is tied to the derived center pair. This could indicate a seam-critical stale claim. I need to compare it with the main chapter on en_koszul_duality or the introductory section. I should check around `sec:swiss-cheese`.
exec
/bin/zsh -lc "sed -n '1567,1628p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '268,326p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1196,1268p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\section{The Swiss-cheese realization}
\label{sec:swiss-cheese}
% ====================================================================

The bar complex of a chiral algebra on a curve $X$ has two
structures: a differential (from OPE residues on Fulton--MacPherson
compactifications of~$X$) and a coproduct (from interval-cutting
in a topological direction). The bar complex $B(\cA)$ is an $E_1$
chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$: the
differential encodes holomorphic factorization on~$\mathbb{C}$, the
deconcatenation coproduct encodes topological factorization
on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ emerges on the chiral derived center
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

% ====================================================================
\subsection{The two colours}
\label{ssec:two-colours}
% ====================================================================
 succeeded in 50ms:
\label{sec:swiss-cheese}
% ====================================================================

The bar complex of a chiral algebra on a curve $X$ has two
structures: a differential (from OPE residues on Fulton--MacPherson
compactifications of~$X$) and a coproduct (from interval-cutting
in a topological direction). The bar complex $B(\cA)$ is an $E_1$
chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$: the
differential encodes holomorphic factorization on~$\mathbb{C}$, the
deconcatenation coproduct encodes topological factorization
on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ emerges on the chiral derived center
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

% ====================================================================
\subsection{The two colours}
\label{ssec:two-colours}
% ====================================================================

 succeeded in 51ms:
\section{The Swiss-cheese case: holomorphic--topological
factorization}
\label{sec:swiss-cheese}
\index{Swiss-cheese operad|textbf}
\index{bar complex!$\Eone$-chiral coassociative coalgebra|textbf}
\index{holomorphic--topological!factorization|textbf}

The dimensional ladder has so far been one-dimensional: $n = 1$
(associative), $n = 2$ (chiral), $n = 3$ (Chern--Simons). But the
ordered bar complex $\barB^{\mathrm{ord}}(\cA)$ of this monograph
already carries a \emph{mixed}
structure that does not fit on this line. The differential
$d_{\barB}$ lives on $\FM_k(\bC)$ (the $n = 2$ slot); the
coassociative coproduct~$\Delta$ lives on $\Conf_k(\bR)$ (the
$n = 1$ slot). Together, a bar element of degree~$k$ is
parametrized by
\begin{equation}\label{eq:bar-product-space}
\FM_k(\bC) \times \Conf_k(\bR),
\end{equation}
the product of holomorphic and topological configuration spaces.

thinking
**Searching for structure**

I need to look for other standalones that have the same stagnant subsection as `programme_summary.tex` and `sections5_8`, since both seem to be identical. Maybe I could do a survey? Searching for "Structure Bar differential" in the standalone might reveal more similarities or help identify what's going on. I’ll investigate this further to clarify the situation!
exec
/bin/zsh -lc "rg -n 'Bar differential \\\\d_\\{\\\\barB\\}|Deconcatenation \\\\Delta|the bar differential extracts OPE|open colour is the topological factorization|closed colour is the holomorphic factorization' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex:314:The closed colour is the holomorphic factorization of
standalone/programme_summary_sections5_8.tex:315:Section~\ref{sec:bar}: the bar differential extracts OPE
standalone/programme_summary_sections5_8.tex:318:open colour is the topological factorization: the
standalone/programme_summary.tex:1614:The closed colour is the holomorphic factorization of
standalone/programme_summary.tex:1615:Section~\ref{sec:bar}: the bar differential extracts OPE
standalone/programme_summary.tex:1618:open colour is the topological factorization: the

thinking
**Searching for patterns**

Alright, I need to find other stale claims about r-matrices and check out some known hot patterns. Since I've had issues with regex errors, I’m considering using fixed-string arrays or multiple regex. It might be easier to do it with a simple shell loop that works with these patterns. So, I’ll approach patterns as literal or more straightforward regex to avoid complications. Let’s get started on this!
codex
The Swiss-cheese seam is a real break, not a cosmetic difference: the standalone summary still assigns the SC colors to the bar differential/coproduct even though the chapter explicitly retracts that and places `\SCchtop` on the derived center pair. I’m now doing the same targeted search for formula drift and theorem-status drift on the other shared standalone surfaces.
exec
/bin/zsh -lc "patterns=('Omega/z' 'S_2 = c/12' 'H_{N-1}' 'kappa(W_N) = c' 'K_BP = 2' '1/3' 'T"'^c(s''^{-1} A)'"' 'T"'^c(s A)'"' '|s"'^{-1}v| = |v|+1'"' 'q"'^{1/24}'"' '1/(2\\pi)' '7/2880' '1/5760' 'E_3-chiral' 'B(A) is a coalgebra over SC' 'SC coalgebra' 'Koszul self-dual' 'bar-cobar produces bulk' 'Omega(B(A)) is the Koszul dual' 'the Koszul dual equals the bar complex' 'D_Ran(B(A)) is the cobar complex'); for p in \""'${patterns[@]}"; do echo "PATTERN: $p"; rg -n -F "$p" standalone/*.tex || true; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 100ms:

PATTERN: SC coalgebra

PATTERN: Koszul self-dual
standalone/introduction_full_survey.tex:1025:\subsection{The Koszul self-duality principle}
standalone/introduction_full_survey.tex:1027:\index{Koszul self-duality!introduction}
standalone/introduction_full_survey.tex:1029:Koszul self-duality $\cA \simeq \cA^!$ forces
standalone/introduction_full_survey.tex:1430:The Heisenberg is not Koszul self-dual:
standalone/introduction_full_survey.tex:1444:(the Heisenberg is \emph{not} Koszul self-dual;
standalone/introduction_full_survey.tex:3949:Heisenberg algebra is \emph{not} Koszul self-dual.
standalone/introduction_full_survey.tex:4020:The Virasoro algebra has OPE $T(z)\,T(w) \sim c/2(z-w)^4 + 2T(w)/(z-w)^2 + \partial T(w)/(z-w)$, a quartic pole, the highest in the standard landscape. The Koszul dual is $\mathrm{Vir}_{26-c}$ (chiral Koszul self-dual at $c = 13$, not $c = 26$).
standalone/introduction_full_survey.tex:5428:The Virasoro algebra is chiral Koszul self-dual at $c = 13$ ($\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$), not $c = 26$. Quadratic self-duality (uncurved bar, $\kappa = 0$) holds at $c = 0$.
standalone/bp_self_duality.tex:56:\title{Bershadsky--Polyakov Koszul self-duality\\
standalone/bp_self_duality.tex:71:minimal nilpotent orbit. We prove that, for $k \neq -3$ (away from the critical level), it is Koszul self-dual under
standalone/bp_self_duality.tex:218:\section{Koszul self-duality}\label{sec:koszul}
standalone/bp_self_duality.tex:228:\begin{proposition}[BP Koszul self-duality]\label{prop:bp-self-dual}
standalone/bp_self_duality.tex:230:$k' = -k-6$. In particular, $\cB^k$ is Koszul self-dual in the
standalone/bp_self_duality.tex:487:$W_k(\fsl_N, f_\lambda)$ is Koszul self-dual:

PATTERN: bar-cobar produces bulk

thinking
**Inspecting high-value theorems**

I'm looking at some high-value theorems, particularly the aspect of `thm:e3-cs` in standalone ordered chiral homology and chapter en_koszul_duality. I need to ensure I have the actual lines surrounding the theorem to analyze it properly. It's important to capture all the relevant details so I can fully understand the context and implications of this theorem while comparing to other related findings. Let's make sure I'm thorough in this investigation!
exec
/bin/zsh -lc "sed -n '430,490p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2590,2625p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7948,7984p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4090,4150p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    = \sum_{i < j} r_{ij}(z_i - z_j) \, dz_{ij},
    \qquad
    dz_{ij} = d(z_i - z_j),
  \end{equation}
  the Knizhnik--Zamolodchikov connection.
  The Arnold forms
  $\omega_{ij} = d\log(z_i - z_j)$ are generators of the
  cohomology algebra $H^*(\Conf_n(\CC))$ and appear as
  coefficients in the bar differential $d_{\mathrm{bar}}$;
  they are \emph{not} the connection $1$-form of $\nabla_{\mathrm{KZ}}$.
\item \textup{(Formality bridge.)} For $\Einf$-chiral $\cA$,
  the formality bridge
  \textup{(}Theorem~\textup{\ref{thm:formality-bridge}}%
  \textup{)} gives a quasi-isomorphism
  $\cC_n^{\mathrm{ord}}(D^\times, \cA)
  \xrightarrow{\sim} \HH_*(\cA)$:
  ordered and symmetric chiral homologies agree as chain
  complexes, though the transferred $\Ainf$-structure may
  carry non-trivial higher operations for class $L/C/M$.
  For genuinely $\Eone$-chiral $\cA$ \textup{(}where
 succeeded in 52ms:
\index{R-matrix!vertex!as projection of ordered bar}
\index{A-infinity@$A_\infty$!chiral endomorphism operad}
\index{coproduct!chiral!from ordered bar}

The ordered bar complex $\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
is a single object from which three structures are recovered: the
vertex $R$-matrix $S(z)$ (braiding data from the degree-$2$ collision
residue), the chiral $A_\infty$-structure maps
$m_k^{\mathrm{ch}}$ (higher associativity from boundary strata of
associahedra), and the chiral coproduct $\Delta^{\mathrm{ch}}$
(coalgebra data from deconcatenation). The three structures
determine each other.

\begin{theorem}[Chiral quantum group equivalence]
\label{thm:chiral-qg-equiv}
\ClaimStatusProvedHere
\index{chiral quantum group!three equivalent descriptions}
The following three structures on an $\Eone$-chiral
algebra~$\cA$ on the Koszul locus determine each other,
up to the choice of a Drinfeld associator
 succeeded in 52ms:
$\Eone$-chiral algebras, it is essential structural data.
\end{remark}


% ----------------------------------------------------------------
\subsection{The equivalence theorem}
\label{subsec:equiv-thm}

The three descriptions of the preceding subsection are not
independent: a vertex $R$-matrix determines the chiral
$\Ainf$ operations via the bar complex, the $\Ainf$
operations determine the chiral coproduct via cobar
dualization, and the coproduct recovers the $R$-matrix.
The equivalences close into a triangle, each arrow depending
on the choice of a Drinfeld associator $\Phi$.

\begin{theorem}[Chiral quantum group equivalence]
\label{thm:chiral-qg-equiv}
The following three structures on an $\Eone$-chiral
algebra $\cA$ on the Koszul locus determine each other,
 succeeded in 50ms:
required), and it gives $\Ethree$ without the Sugawara hypothesis.

On the original complex, both routes remain cohomological:
the Dunn route uses local constancy only after passing to
BRST cohomology, and the HDC route uses formality to compare
chain-level operations with their cohomological shadow. For
affine Kac--Moody, Theorem~\ref{thm:topologization} adds the
stronger statement that the cohomology complex itself is an
unconditional chain-level $\Ethree^{\mathrm{top}}$ model on a
quasi-isomorphic complex. What remains open is the lift to
the original cochain complex, governed by the
$A_\infty$-coherence equation
$[m,G]=\partial_z$ of
Remark~\ref{rem:topologization-chain-vs-cohomology}.
For class~M algebras, even the cohomological route still
depends on the conjectural bulk BRST construction
(Conjecture~\ref{conj:topologization-general}), and the
coderived alternative remains Conjecture~\ref{conj:coderived-e3}.
\end{remark}


thinking
**Comparing theorem fixes**

I’m looking to compare an exact fix for `thm:cfg`. It seems like it might have the same label but with a claim status that changed from standalone to potentially being proved here versus proved elsewhere in the chapter. I need to inspect this closely. It’s possible that the label has been reused with a different theorem statement. I'll make sure to take a careful look into this!
exec
/bin/zsh -lc "sed -n '4150,4215p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5888,5965p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Ethree$-algebra is the \emph{derived centre}, not the
bar complex.
\end{warning}


% ----------------------------------------------------------------
\subsection{The CFG comparison}
\label{subsec:cfg}

Costello, Francis, and Gwilliam construct a filtered
$\Ethree$-algebra $\cA^\lambda$ from BV quantisation of
Chern--Simons theory on $\RR^3$. The derived chiral centre
of $V_k(\fg)$ and the CFG algebra both deform $C^*(\fg)$
over $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$. The question is whether
these deformation families are isomorphic as
$\Ethree$-algebras.

\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
\label{thm:cfg}
Let $\fg$ be a simple finite-dimensional Lie algebra.
 succeeded in 52ms:
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra.
BV quantisation of Chern--Simons theory on $\RR^3$ with
gauge algebra $\fg$ and coupling $\lambda$ yields
a filtered $\Ethree$-algebra $\cA^\lambda$ on
$C^*(\fg) = \Sym(\fg^\vee[-1])$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Classical observables: $C^*(\fg)$, commutative.
\item Quantum observables: $\cA^\lambda$, filtered
  $\Ethree$-algebra with deformation space
  $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$.
\item $\mathrm{Mod}_{\cA^\lambda}$ is braided monoidal;
  filtered Koszul duality gives
  $\mathrm{Perf}_{C^*(\fg)} \simeq
  \mathrm{Rep}_{\mathrm{fin}}(\fg)^{\mathrm{dg}}$,
  recovering the Drinfeld--Jimbo quantum group.
\item \textup{(Theorem~1.4 of \cite{CFG25}.)} Canonical
  bijection between perturbative CS quantisations,
  filtered $\Ethree$-deformations, braided monoidal
  deformations, and quasi-triangular quasi-Hopf algebras.

thinking
**Checking bibliography consistency**

I’m looking at the standalone citations from CFG26 and the chapter cites from CFG25. I wonder if there might be a date drift, so I need to check the latest within the repository. There could be a bibliography entry that I missed indicating differences in the bibkey between the main chapter and the standalone citation. I should search through the bibliography to verify that everything aligns correctly.
exec
/bin/zsh -lc "rg -n '"'^@.*'"\\{CFG25|"'^@.*'"\\{CFG26|CFG25|CFG26' standalone/references.bib bib*.bib references.bib chapters -g '*.bib' -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: bib*.bib

thinking
**Searching for references**

I think I need to use the command `rg --files` to see if there’s a `references.bib` file. It sounds like a good place to start looking for citations or sources I might need. I'll run the command and check the output. This should help me identify if the references I’m seeking are indeed present. Let's see what I find!
exec
/bin/zsh -lc "rg -n 'CFG25|CFG26' . -g '*.bib' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./staging/pre_e3_ident.tex:38:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
./staging/pre_e3_ident.tex:56:\item \textup{(Theorem~1.4 of \cite{CFG26}.)} Canonical
./staging/thm_e3_cs.tex:28:  Costello--Francis--Gwilliam~\cite{CFG26}:
./bibliography/references.tex:359:\bibitem{CFG25}
./staging/thm_cfg.tex:9:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
./staging/thm_cfg.tex:33:\item \textup{(Theorem~1.4 of \cite{CFG26}.)} Canonical
./standalone/ordered_chiral_homology.tex:498:  Costello--Francis--Gwilliam~\cite{CFG26} identify
./standalone/ordered_chiral_homology.tex:1722:  theory (Costello--Francis--Gwilliam~\cite{CFG26}).
./standalone/ordered_chiral_homology.tex:5905:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
./standalone/ordered_chiral_homology.tex:5929:\item \textup{(Theorem~1.4 of \cite{CFG26}.)} Canonical
./standalone/ordered_chiral_homology.tex:10690:(Costello's $4$d Chern--Simons~\cite{CWY1,CWY2,CFG26,CG17}),
./standalone/ordered_chiral_homology.tex:11047:\bibitem{CFG26}
./staging/combined_for_en_koszul.tex:99:Costello--Francis--Gwilliam~\cite{CFG26},
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:473:  Costello--Francis--Gwilliam~\cite{CFG26}:
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1691:  theory (Costello--Francis--Gwilliam~\cite{CFG26}).
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5371:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5395:\item \textup{(Theorem~1.4 of \cite{CFG26}.)} Canonical
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5490:Costello--Francis--Gwilliam~\cite{CFG26},
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10198:(Costello's $4$d Chern--Simons~\cite{CWY1,CWY2,CFG26,CG17}),
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10505:\bibitem{CFG26}
exec
/bin/zsh -lc "sed -n '350,366p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11042,11054p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\bibitem{BittlestonCostelloZeng24}
L. Bittleston, K. Costello, and K. Zeng, \emph{3d mirror symmetry from S-duality and the teleparallel formulation of GR}, arXiv:2412.02680, 2024.

\bibitem{FernandezCostelloP24}
N. Fernandez, K. Costello, and N. M. Paquette, \emph{Koszul duality in quantum field theory}, arXiv:2412.17168, 2024.

\bibitem{BittlestonCostello25}
L. Bittleston and K. Costello, \emph{Twisted eleven-dimensional supergravity}, arXiv:2510.26764, 2025.

\bibitem{CFG25}
K. Costello, J. Francis, and O. Gwilliam, \emph{Chern--Simons factorization algebras and knot polynomials}, arXiv:2602.12412, 2026.

\bibitem{BRvR14-6d}
C. Beem, L. Rastelli, and B. C. van Rees, \emph{$\mathcal{W}$-symmetry in six dimensions}, J.\ High Energy Phys.\ (2015), no.~5, Paper No.~017, arXiv:1404.1079.

\bibitem{HS98}
M. Henningson and K. Skenderis, \emph{The holographic Weyl anomaly}, J.\ High Energy Phys.\ (1998), no.~7, Paper No.~023, arXiv:hep-th/9806087.
 succeeded in 51ms:
V.~G.~Drinfeld,
\emph{Quasi-Hopf algebras},
Leningrad Math. J. \textbf{1} (1990), 1419--1457.


\bibitem{CFG26}
K.~Costello, J.~Francis, and O.~Gwilliam,
\emph{Chern--Simons factorization algebras and knot
polynomials},
arXiv:2602.12412, 2026.

\bibitem{CG17}
K.~Costello and O.~Gwilliam,

thinking
**Investigating macros**

I think I could inspect `ordered_chiral_homology` to look for no-op status macros. I wonder if there are others out there, so a survey of the documentation might help define any visible macros. Searching for `standalone: no-op definitions` seems like a good idea, but it might only lead me to that specific file. Additionally, I’ll check all standalone files for occurrences of `\providecommand{\ClaimStatus` to gather more context.
exec
/bin/zsh -lc "rg -n 'ClaimStatusProvedHere|ClaimStatusProvedElsewhere|ClaimStatusConjectured|ClaimStatusConditional|ClaimStatusHeuristic' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/ordered_chiral_homology.tex:112:\providecommand{\ClaimStatusConjectured}{}
standalone/ordered_chiral_homology.tex:113:\providecommand{\ClaimStatusProvedHere}{}
standalone/ordered_chiral_homology.tex:114:\providecommand{\ClaimStatusProvedElsewhere}{}
standalone/ordered_chiral_homology.tex:115:\providecommand{\ClaimStatusHeuristic}{}
standalone/ordered_chiral_homology.tex:4107:\ClaimStatusProvedHere
standalone/ordered_chiral_homology.tex:4319:\ClaimStatusProvedHere
standalone/survey_track_a_compressed.tex:76:\providecommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
standalone/survey_track_a_compressed.tex:77:\providecommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
standalone/survey_track_a_compressed.tex:78:\providecommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
standalone/survey_track_a_compressed.tex:79:\providecommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}
standalone/survey_track_a_compressed.tex:80:\providecommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
standalone/survey_track_b_compressed.tex:131:\providecommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
standalone/survey_track_b_compressed.tex:132:\providecommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
standalone/survey_track_b_compressed.tex:133:\providecommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
standalone/survey_track_b_compressed.tex:134:\providecommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}
standalone/survey_track_b_compressed.tex:135:\providecommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
standalone/introduction_full_survey.tex:75:\providecommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
standalone/introduction_full_survey.tex:76:\providecommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
standalone/introduction_full_survey.tex:77:\providecommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
standalone/introduction_full_survey.tex:78:\providecommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}

thinking
**Searching for theorem surfaces**

I just realized that only ordered chiral homology uses no-op statuses, which is an interesting finding. I might need to consider that there could be theorem surfaces without any status macros at all. The user mentioned stale claims, so I wonder if it's just this file they’re concerned about. I'll look for `TODO` placeholders from standalone integration past phantom labels. I'll search for `TODO: integrate from standalone` across all chapters since I’ve already found it in ordered associative and maybe some other files.
exec
/bin/zsh -lc "rg -n 'TODO: integrate from standalone|Phantom labels for standalone cross-references|integration-ready chapter file|stripped from standalone' chapters/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: chapters/*.tex
exec
/bin/zsh -lc "rg -n 'TODO: integrate from standalone|Phantom labels for standalone cross-references|integration-ready chapter file|stripped from standalone' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:2:% Integration-ready chapter file (stripped from standalone amsart draft).
chapters/theory/ordered_associative_chiral_kd.tex:39:%% --- Phantom labels for standalone cross-references (TODO: integrate) ---
chapters/theory/ordered_associative_chiral_kd.tex:40:\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:41:\phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:42:\phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:43:\phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11428:\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11429:\phantomsection\label{ch:genus1-seven-faces} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11430:\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11431:\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11432:\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11433:\phantomsection\label{conv:three-hochschild} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11434:\phantomsection\label{part:seven-faces} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11435:\phantomsection\label{part:v1-frontier} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11436:\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11437:\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11438:\phantomsection\label{sec:complementarity} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11439:\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:11440:\phantomsection\label{thm:langlands-bar-bridge} % TODO: integrate from standalone
exec
/bin/zsh -lc "sed -n '10188,10228p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '33728,33764p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{two-component} dynamical parameter
$\lambda = (\lambda_1, \lambda_2) \in \fh^* \oplus \fh^*$,
replacing the single dynamical parameter $\lambda \in \fh^*$
of the genus-$1$ theory
(Remark~\textup{\ref{rem:dynamical-parameter}}).
The dynamical Yang--Baxter equation is replaced by a
system of two coupled equations, one for each $B$-cycle.
This is the genus-$2$ instantiation of the Felder dynamical
$R$-matrix theory~\cite{Felder94,FelderVarchenko96}.
\end{remark}

\begin{proposition}[Degree-$2$ ordered chiral homology on
$\Sigma_2$]
\label{prop:g2-degree2}
The degree-$2$ ordered chiral homology
$H^*(\cC_2^{\mathrm{ord}}(\Sigma_2, Y_\hbar))$ is the
de~Rham cohomology of the KZB local system on
$\Conf_2^{\mathrm{ord}}(\Sigma_2)$ with coefficients in
$(s^{-1}\bar{Y}_\hbar)^{\otimes 2}$.
On evaluation modules $V_a \otimes V_b$
 succeeded in 51ms:
the doubly-dynamical YBE is verified numerically at
generic off-diagonal period matrix $\Omega$ to relative
error $< 10^{-12}$
\textup{(}$29$ compute tests in
\texttt{face\_model\_ddybe\_engine.py}\textup{)}.
The genus-$2$ odd theta factorises at diagonal $\Omega$
as $-\theta_1(x|\tau_1) \cdot \theta_3(0|\tau_2)$; the
sign cancels in all Boltzmann-weight ratios, giving exact
degeneration to two copies of the genus-$1$ DYBE.
\end{remark}

\begin{proposition}[Degree-$2$ ordered chiral homology on
$\Sigma_2$]
\label{prop:g2-degree2}
\ClaimStatusProvedHere
The degree-$2$ ordered chiral homology
$H^*(\cC_2^{\mathrm{ord}}(\Sigma_2, Y_\hbar))$ is the
de~Rham cohomology of the KZB local system on
$\Conf_2^{\mathrm{ord}}(\Sigma_2)$ with coefficients in
$(s^{-1}\bar{Y}_\hbar)^{\otimes 2}$.
exec
/bin/zsh -lc "sed -n '4620,4652p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4828,4846p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2168,2182p' standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8316,8342p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
families, the genus-$2$ and genus-$3$ planted-forest shell formulas,
the spectral discriminant for all simple Lie types through rank~$8$,
the Koszul conductor for every family in the landscape census,
and the cross-channel corrections $\delta F_g^{\mathrm{cross}}$ at
genus~$2$--$3$ for $\mathcal{W}_3$ through $\mathcal{W}_7$. The
computation is adversarial: tests encode cross-family consistency checks
(additivity of~$\kappa$ under direct sum, complementarity sum rules,
anti-symmetry of the averaging kernel, Feigin--Frenkel involution on
$r$-matrices) that cannot be fooled by a single hardcoded value. Every
hardcoded expected value is derived by at least two independent methods.

\begin{principle}[The four-test interface]
\label{princ:four-test-interface}
\index{four-test interface|textbf}%
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline{\mathcal M}_{g,n}$, consisting of
four independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$:
 the bar differential squares to zero at all genera and degrees
 succeeded in 52ms:
 &&\text{(universal MC element)}.
\end{align*}
Theorems~A--D and Theorem~H are proved projections at the
scalar level $\kappa$. The holographic datum
$\cH(T) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\hol})$
packages $\Theta_\cA$ and its projections into the data of a
3d HT field theory.

\begin{principle}[The four-test interface]
\label{princ:four-test-interface}
\index{four-test interface|textbf}%
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline\cM_{g,n}$ consisting of four
independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$: the bar differential squares to zero at
all genera and degrees (Theorems~\ref{thm:bar-modular-operad},
\ref{thm:quantum-diff-squares-zero}).
\item $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for
 succeeded in 50ms:
$\mathcal H(T)=(\cA,\cA^!,\cC,r(z),\Theta_\cA,\nabla^{\mathrm{hol}})$
is the packaging of $\Theta_\cA$ and its projections into
the data of a 3d holomorphic-topological field theory. The weight
filtration on $\mathfrak g^{\mathrm{mod}}_\cA$ controls the
extension tower; each finite truncation
$\Theta_\cA^{\le r}$ is constructive and does not require the
full all-genera modular envelope. The modular tangent complex
extracts Chern--Weil invariants. The genus spectral sequence
controls the lift across genera. The standard landscape is
computed.

\begin{principle}[The four-test interface]
\label{princ:four-test-interface}
\index{four-test interface|textbf}%
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline{\mathcal M}_{g,n}$, consisting of
four independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$:
 the bar differential squares to zero at all genera and degrees
 succeeded in 52ms:
scalar level $\kappa$. The holographic datum
$\cH(T) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\hol})$
packages $\Theta_\cA$ and its projections into the data of a
3d HT field theory.

\begin{principle}[The four-test interface]
\label{princ:four-test-interface}
\index{four-test interface|textbf}%
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline\cM_{g,n}$ consisting of four
independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$: the bar differential squares to zero at
all genera and degrees (Theorems~\ref{thm:bar-modular-operad},
\ref{thm:quantum-diff-squares-zero}).
exec
/bin/zsh -lc "node - <<'NODE'
const fs=require('fs'); const cp=require('child_process');
function extract(file){
  const lines=fs.readFileSync(file,'utf8').split(/\\n/);
  const out=[];
  for(let i=0;i<lines.length;i++){
    const m=lines[i].match(/"'^'"\\\\begin\\{(theorem|proposition|lemma|corollary|conjecture|remark|definition|principle|convention)\\}(?:\\[(["'^'"\\]]*))?/);
    if(m){
      let title=m[2]||'';
      let j=i;
      while("'!lines[j].includes('"']') && j+1<lines.length && title && title.split('[').length>title.split(']').length){ j++; title += '\\n'+lines[j]; }
      for(let k=i;k<Math.min(i+6,lines.length);k++){
        const lab=lines[k].match(/\\\\label\\{(["'^}]*)'"\\}/);
        if(lab){ out.push({label:lab[1], env:m[1], title:title.replace(/\\\\ClaimStatus[A-Za-z]+/g,'').replace(/\\s+/g,' ').trim(), line:k+1, file}); break; }
      }
    }
  }
  return out;
}
const standalone=cp.execSync(\"rg --files standalone -g '*.tex'\",{encoding:'utf8'}).trim().split(/\\n/).filter(Boolean);
const chapters=cp.execSync(\"rg --files chapters -g '*.tex'\",{encoding:'utf8'}).trim().split(/\\n/).filter(Boolean);
const S=new Map(), C=new Map();
for(const f of standalone) for(const x of extract(f)){ if("'!S.has(x.label)) S.set(x.label,[]); S.get(x.label).push(x); }
for(const f of chapters) for(const x of extract(f)){ if(!C.has(x.label)) C.set(x.label,[]); C.get(x.label).push(x); }
for(const label of [...S.keys()].filter(k=>C.has(k)).sort()){
  for(const a of S.get(label)) for(const b of C.get(label)){
    if(a.env!==b.env || a.title!==b.title){
      console.log(label+'"'\\t'+a.file+':'+a.line+'\\t'+a.env+'\\t'+a.title+'\\t'+b.file+':'+b.line+'\\t'+b.env+'\\t'+b.title);
    }
  }
}
NODE" in /Users/raeez/chiral-bar-cobar succeeded in 72ms:
cor:bar-encodes-all	standalone/ordered_chiral_homology.tex:5149	corollary	The ordered bar complex encodes all three	chapters/theory/ordered_associative_chiral_kd.tex:8055	corollary	The ordered bar encodes all three structures
cor:mc3-all-types	standalone/N2_mc3_all_types.tex:734	corollary	MC3 for all simple types	chapters/examples/yangians_computations.tex:4220	corollary	Three-layer MC3 status after categorical CG closure;
def:filtered-e3-chiral	standalone/ordered_chiral_homology.tex:6895	definition	The filtered affine bulk package	chapters/theory/en_koszul_duality.tex:5351	definition	The filtered $\Ethree$-chiral algebra
def:hs-sewing	standalone/N5_mc5_sewing.tex:331	definition	HS-sewing	chapters/connections/genus_complete.tex:1355	definition	HS-sewing condition
def:ran-space	standalone/ordered_chiral_homology.tex:1620	definition	The Ran space as coinvariant quotient	chapters/theory/algebraic_foundations.tex:1172	definition	Ran space
def:shadow-metric	standalone/shadow_towers.tex:617	definition	Shadow metric and critical discriminant	chapters/theory/higher_genus_modular_koszul.tex:17405	definition	Shadow metric
lem:degree-cutoff	standalone/N4_mc4_completion.tex:431	lemma	Degree cutoff	chapters/theory/bar_cobar_adjunction_curved.tex:927	lemma	Degree cutoff: finite MC equation at each stage;
lem:filtered-comparison	standalone/N4_mc4_completion.tex:550	lemma	Complete filtered comparison	chapters/theory/chiral_koszul_pairs.tex:333	lemma	Filtered comparison;
prop:bp-central-charge	standalone/bp_self_duality.tex:151	proposition	BP central charge	chapters/examples/bershadsky_polyakov.tex:146	proposition	BP central charge;\;
rem:d-module-purity-content	standalone/N1_koszul_meta.tex:736	remark	Converse direction	chapters/theory/chiral_koszul_pairs.tex:2974	remark	D-module purity: reduction to a single gap
rem:depth-vs-koszulness	standalone/classification.tex:255	remark	Depth and Koszulness	chapters/connections/thqg_holographic_reconstruction.tex:385	remark	Shadow depth versus Koszulness
rem:dynamical-g2	standalone/ordered_chiral_homology.tex:10186	remark	Dynamical parameters at genus~$2$	chapters/theory/higher_genus_modular_koszul.tex:33586	remark	The doubly-dynamical parameter at genus~$2$
rem:ker-av-table	standalone/ordered_chiral_homology.tex:1437	remark	Explicit values and	chapters/theory/ordered_associative_chiral_kd.tex:6149	remark	Explicit values and conjectural ordered-centre bounds
rem:sl2-admissible	standalone/garland_lepowsky.tex:1026	remark		chapters/examples/kac_moody.tex:3808	remark	Admissible levels
rem:verlinde-vs-shadow	standalone/ordered_chiral_homology.tex:9684	remark	Verlinde bundle vs shadow tower	chapters/theory/higher_genus_modular_koszul.tex:32875	remark	Verlinde bundle vs shadow curvature
thm:cfg	standalone/ordered_chiral_homology.tex:5906	theorem	Costello--Francis--Gwilliam~\cite{CFG26}	chapters/theory/en_koszul_duality.tex:4149	theorem	Costello--Francis--Gwilliam~\cite{CFG25}
thm:chiral-e3-structure	standalone/ordered_chiral_homology.tex:6924	theorem	Structure of the affine bulk package	chapters/theory/en_koszul_duality.tex:5375	theorem	Structure of the chiral $\Ethree$-algebra
thm:e3-cs	standalone/ordered_chiral_homology.tex:457	theorem	Derived centre, topologization, and	chapters/theory/en_koszul_duality.tex:4113	theorem	The $\Ethree$-algebra and Chern--Simons
thm:e3-identification	standalone/ordered_chiral_homology.tex:5941	theorem	Matching deformation spaces and first	chapters/theory/en_koszul_duality.tex:4273	theorem	Identification of $\Ethree$-deformation families
thm:general-hs-sewing	standalone/N5_mc5_sewing.tex:617	theorem	General HS-sewing criterion	chapters/connections/genus_complete.tex:1386	theorem	General HS-sewing criterion;

thinking
**Inspecting macro issues**

I need to investigate potential seam issues related to imported files. While main chapters might be unaffected, the user specifically asked about macros defined via providecommand. A problematic command I’m spotting is `\renewcommand{\ref}` in standalone documents, which could lead to issues if imported. I'll need to report on this and recommend replacing local commands with a standalone helper like `\newcommand{\sref}[1]{...}` or guarding it within `\ifstandalone`. I’ll check specific lines, like in classification.
exec
/bin/zsh -lc "sed -n '34,46p' standalone/classification.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29,40p' standalone/computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '100,106p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '58,67p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\providecommand{\Vir}{\mathrm{Vir}}

\makeatletter
\let\cls@oldref\ref
\renewcommand{\ref}[1]{%
 \@ifundefined{r@#1}{\textit{full monograph}}{\cls@oldref{#1}}%
}
\makeatother

\title{The G/L/C/M classification and shadow tables}
\author{Raeez Lorgat}
\date{}

 succeeded in 52ms:
\providecommand{\Res}{\operatorname{Res}}

\makeatletter
\let\cmp@oldref\ref
\renewcommand{\ref}[1]{%
 \@ifundefined{r@#1}{\textit{full monograph}}{\cmp@oldref{#1}}%
}
\makeatother

\title{The genus-2 free energy of $W_3$ and the gravitational coproduct}
\author{Raeez Lorgat}
\date{}
 succeeded in 51ms:
\numberwithin{equation}{section}

\makeatletter
\let\ps@oldref\ref
\renewcommand{\ref}[1]{%
 \@ifundefined{r@#1}{\textit{full monograph}}{\ps@oldref{#1}}%
}
\makeatother

% ================================================================
 succeeded in 52ms:
\makeatletter
\let\svy@oldref\ref
\renewcommand{\ref}[1]{%
 \@ifundefined{r@#1}{\textit{full monograph}}{\svy@oldref{#1}}%
}
\makeatother




thinking
**Examining macro issues**

I think there's a seam issue here since imported content might change global references if copied. However, these are standalone documents and not imported. The requirement says something about macros through providecommand, which could be low severity. I might need to check `programme_summary_sections5_8.tex` for how certain commands are set. There seems to be some complexity around integrating or redefining symbols in this context. The user has asked about every inconsistency, so I should focus on that, even if it feels overwhelming!
thinking
**Analyzing theorem inconsistencies**

I need to look at how other standalone documents, like `ordered_chiral_homology`, use the formula `Z^{der}_ch(V_k(g)) = HH^*(\BarSig(V_k(g)),\BarSig(V_k(g)))` in `thm:e3-cs`, while the chapter has a similar yet slightly different content. There's a mismatch here because the same label leads to different theorems based on the build target. I need to decide whether to split the standalone result into two new labels or rename the standalone label. There are also similar citation issues with `thm:cfg`.
thinking
**Inspecting chiral E3 algebra**

I'm examining chiral E3 algebra and wondering if it might be more about terminology drift than actual content. I should look into the sections of `standalone/programme_summary*.tex` where it discusses closed color as a holomorphic factorization. There's a concern regarding the bar differential and its relationship with curvature at different genera. I think comparing it to the main chapter could clarify this, so I’ll search for the phrase “acquires curvature” in the chapters.
exec
/bin/zsh -lc "rg -n 'acquires curvature .*kappa|d\\"'^2 = 0 at genus~0|curvature '"\\\\kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g|bar differential.*curvature|produces \\"'$d'"\\"'^2 = 0'"\\"'$ at genus~'"\\"'$0'"\\"'$, and acquires curvature'"' standalone/programme_summary*.tex chapters/theory/en_koszul_duality.tex chapters/theory/bar_construction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_construction.tex:279:The entire bar differential comes from the curvature component $d_{\mathrm{curvature}}$ (Proposition~\ref{prop:pole-decomposition}). One must not multiply the OPE pole by the propagator~$\eta_{12}$ and take a combined residue; the logarithmic form accounts for the bar degree, not an additional pole (Computation~\ref{comp:deg1-general}).
chapters/theory/bar_construction.tex:973:\index{bar differential!curvature component}
chapters/theory/introduction.tex:20:The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
chapters/theory/introduction.tex:2695:$m_1^2(a) = [m_0, a]$ (commutator, with a minus sign). The bar differential satisfies $d^2 = 0$ always; curvature shows as $m_1^2 \neq 0$ in the $A_\infty$ algebra, not in the bar complex.


thinking
**Examining curvature inconsistencies**

I'm realizing the search didn't catch the same phrase in standalones, possibly due to the lack of exact matches. I need to inspect lines 314-318 closely. They claim d^2=0 at genus 0 and mention curvature at higher genus, which seems to contradict the introduction at line 2695. It's tricky, as chapter introductions have their own nuances. The user is interested in the seam between standalone and chapters, so I need to dig deeper into inconsistencies and conflict around AGENTS.
thinking
**Gathering line comparisons**

I think it’s important to report the seam if the standalone summary repeats a misleading curvature formulation while the chapters or introduction at line 2695 provides a correction. I need to ensure I have the exact lines from the chapter to compare them accurately. So, gathering those line numbers is a priority now. I could use `nl -ba` to help with that and make sure I’m thorough in my analysis. Let's get started!
codex
Another substantive seam issue surfaced inside the Swiss-cheese summary block: the standalone says the “bar differential … acquires curvature \\\\kappa\\\\omega_g”, while the main introduction later states explicitly that `d^2=0` always and curvature appears on the `A_\\infty` side, not in the bar complex. I’m pinning exact lines now so I can separate real contradictions from loose paraphrase.
exec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections5_8.tex | sed -n '296,322p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '1596,1622p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2688,2699p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1248,1289p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2688	bracket in all convolution computations
  2689	(Appendix~\ref{app:signs}, Pitfall~9).
  2690	The Heisenberg algebra is \emph{not} self-dual.
  2691	Chiral Koszulness is not the same as classical
  2692	Koszulness.
  2693	
  2694	\smallskip\noindent\textbf{Curved $A_\infty$.}
  2695	$m_1^2(a) = [m_0, a]$ (commutator, with a minus sign). The bar differential satisfies $d^2 = 0$ always; curvature shows as $m_1^2 \neq 0$ in the $A_\infty$ algebra, not in the bar complex.
  2696	
  2697	\smallskip\noindent\textbf{Sugawara.}
  2698	The Sugawara construction is \emph{undefined} at critical level $k = -h^\vee$; the Sugawara vector does not lie in the appropriate completion. This is not ``$c$ diverges''; the construction does not exist.
  2699	
 succeeded in 52ms:
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
  1610	\end{tabular}
  1611	\end{center}
  1612	
  1613	\noindent
  1614	The closed colour is the holomorphic factorization of
  1615	Section~\ref{sec:bar}: the bar differential extracts OPE
 succeeded in 52ms:
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
   312	
   313	\noindent
   314	The closed colour is the holomorphic factorization of
   315	Section~\ref{sec:bar}: the bar differential extracts OPE
 succeeded in 51ms:
  1248	$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
  1249	\label{princ:sc-two-incarnations}
  1250	\index{Swiss-cheese operad!on derived center, NOT on bar}
  1251	\index{bar complex!is E1 coassociative, NOT SC}
  1252	The ordered bar complex
  1253	$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$
  1254	is an $\Eone$-chiral coassociative coalgebra: a coalgebra
  1255	over the Koszul dual cooperad
  1256	$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
  1257	It has a differential (from OPE collision residues) and a
  1258	coassociative deconcatenation coproduct. These are the two
  1259	structures of a dg coalgebra. The bar complex does \emph{not}
  1260	carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.
  1261	
  1262	The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
  1263	the \emph{derived chiral center}
  1264	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
  1265	= C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$,
  1266	computed \emph{using} the bar complex as a resolution.
  1267	The derived center is the algebra of bulk observables of

thinking
**Evaluating dimensional hierarchy**

I’m thinking about whether I need line numbers for the dimensional hierarchy in the introduction or preface. It might be helpful to make comparisons, especially with the main introduction of volume II, specifically lines 2279-2283. So, let’s check on that and see if I can gather the relevant line numbers for reference. Getting them will definitely help clarify things!
exec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections5_8.tex | sed -n '476,488p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '1776,1788p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   476	\begin{center}
   477	\renewcommand{\arraystretch}{1.3}
   478	\begin{tabular}{cllll}
   479	\toprule
   480	\textbf{$d$} & \textbf{Level} & \textbf{Operadic type}
   481	 & \textbf{Key datum} & \textbf{Volume} \\
   482	\midrule
   483	$4$ & CY source & $E_2$
   484	 & CY category $\mathcal{C}$ & III \\
   485	$3$ & Swiss-cheese & $E_1$
   486	 & $R$-matrix $r(z)$ & II \\
   487	$2$ & Modular shadow & $E_\infty$
   488	 & $\kappa(\cA)$ & I \\
 succeeded in 51ms:
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
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2278,2284p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2278	\hline
  2279	Concordance (Ch.~\ref{chap:concordance}) &
  2280	 Five theorems; three pillars; three rings; Koszulness programme; open frontiers \\
  2281	Volume~II &
  2282	 $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
  2283	\end{longtable}
  2284	}
exec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '452,490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4108,4144p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   452	\end{enumerate}
   453	\end{theorem}
   454	
   455	\begin{theorem}[Derived centre, topologization, and
   456	Chern--Simons]
   457	\label{thm:e3-cs}
   458	Let $\fg$ be a simple finite-dimensional Lie algebra and
   459	$V_k(\fg)$ the affine Kac--Moody vertex algebra at level~$k$.
   460	\begin{enumerate}[label=\textup{(\roman*)}]
   461	\item \textup{(The algebraic bulk package.)}
   462	  The curve geometry provides the $\Etwo$ structure on
   463	  $\BarSig(V_k(\fg))$
   464	  \textup{(}Warning~\textup{\ref{warn:e1-vs-e2-source}}\textup{)}.
   465	  Its Hochschild cochains
   466	  \begin{equation}\label{eq:e3-center}
   467	    Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
   468	    = \HH^*\bigl(\BarSig(V_k(\fg)),\;
   469	    \BarSig(V_k(\fg))\bigr)
   470	  \end{equation}
   471	  carries the algebraic $\Etwo$ structure of the derived
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4148,4170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '5900,5936p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4108	\end{remark}
  4109	
  4110	% ================================================================
  4111	
  4112	\begin{theorem}[The $\Ethree$-algebra and Chern--Simons]
  4113	\label{thm:e3-cs}
  4114	\ClaimStatusProvedElsewhere
  4115	Let $\fg$ be a simple finite-dimensional Lie algebra and
  4116	$V_k(\fg)$ the affine Kac--Moody vertex algebra at level~$k$.
  4117	\begin{enumerate}[label=\textup{(\roman*)}]
  4118	\item \textup{(The $\Ethree$ structure.)}
  4119	  The curve geometry provides the $\Etwo$ structure on
  4120	  $\BarSig(V_k(\fg))$. By the Higher Deligne Conjecture
  4121	  \textup{(}Lurie~\cite{HA}, Francis~\cite{Francis2013}\textup{)},
  4122	  the derived chiral centre
  4123	  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
  4124	  = \HH^*(\BarSig(V_k(\fg)), \BarSig(V_k(\fg)))$
  4125	  carries a natural $\Ethree$-algebra structure
  4126	  \textup{(}$\Etwo + 1 = \Ethree$\textup{)}.
  4127	\item \textup{(Deformation classification.)}
 succeeded in 50ms:
  4148	\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
  4149	\label{thm:cfg}
  4150	\ClaimStatusProvedElsewhere
  4151	Let $\fg$ be a simple finite-dimensional Lie algebra.
  4152	BV quantisation of Chern--Simons theory on $\RR^3$ with
  4153	gauge algebra $\fg$ and coupling $\lambda$ yields
  4154	a filtered $\Ethree$-algebra $\cA^\lambda$ on
  4155	$C^*(\fg) = \Sym(\fg^\vee[-1])$.
  4156	\begin{enumerate}[label=\textup{(\roman*)}]
  4157	\item Classical observables: $C^*(\fg)$, commutative.
  4158	\item Quantum observables: $\cA^\lambda$, filtered
  4159	  $\Ethree$-algebra with deformation space
  4160	  $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$.
  4161	\item $\mathrm{Mod}_{\cA^\lambda}$ is braided monoidal;
  4162	  filtered Koszul duality gives
  4163	  $\mathrm{Perf}_{C^*(\fg)} \simeq
  4164	  \mathrm{Rep}_{\mathrm{fin}}(\fg)^{\mathrm{dg}}$,
  4165	  recovering the Drinfeld--Jimbo quantum group.
  4166	\item \textup{(Theorem~1.4 of \cite{CFG25}.)} Canonical
  4167	  bijection between perturbative CS quantisations,
 succeeded in 51ms:
  5900	of $V_k(\fg)$ and the CFG algebra both deform $C^*(\fg)$
  5901	over $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$. The question is whether
  5902	these deformation families are isomorphic as
  5903	$\Ethree$-algebras.
  5904	
  5905	\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
  5906	\label{thm:cfg}
  5907	Let $\fg$ be a simple finite-dimensional Lie algebra.
  5908	BV quantisation of Chern--Simons theory on $\RR^3$ with
  5909	gauge algebra $\fg$ and invariant pairing $\lambda$ yields
  5910	a filtered $\Ethree$-algebra $\cA^\lambda$ on the
  5911	Chevalley--Eilenberg cochains $C^*(\fg)$.
  5912	\begin{enumerate}[label=\textup{(\roman*)}]
  5913	\item The classical observables are
  5914	  $C^*(\fg) = \Sym(\fg^\vee[-1])$
  5915	  with the CE differential: a commutative
  5916	  \textup{(}$\Einf$\textup{)} algebra.
  5917	\item The quantum observables
  5918	  $\cA^\lambda$ are a filtered $\Ethree$-algebra deforming
  5919	  $C^*(\fg)$, with deformation space

thinking
**Searching for duplicate labels**

I need to check if these labels already exist elsewhere. For instance, `conv:three-hochschild` is in `chapters/connections/concordance.tex`, and `ch:genus1-seven-faces` does too. These duplicate labels might cause issues with LaTeX by being defined multiple times in the same build. So, I should inspect whether the actual labels in the chapters are the same. Let’s get searching!
exec
/bin/zsh -lc 'for lbl in def:chiral-coproduct eq:bar-degree1-yangian eq:yangian-drinfeld-coprod eq:yangian-qybe ch:derived-langlands ch:genus1-seven-faces ch:holographic-datum-master ch:landscape-census comp:bp-kappa-three-paths conv:three-hochschild part:seven-faces part:v1-frontier prop:nilpotent-transport-typeA sec:bar-complex-introduction sec:complementarity thm:ds-hpl-transfer thm:langlands-bar-bridge; do echo LABEL $lbl; rg -n -F "'"\\\\label{"'$lbl}" chapters standalone | sed -n '"'1,20p'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 87ms:
chapters/connections/subregular_hook_frontier.tex:1519:\label{prop:nilpotent-transport-typeA}
chapters/theory/ordered_associative_chiral_kd.tex:11436:\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone

LABEL sec:bar-complex-introduction
chapters/theory/ordered_associative_chiral_kd.tex:11437:\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone

LABEL sec:complementarity
chapters/theory/ordered_associative_chiral_kd.tex:11438:\phantomsection\label{sec:complementarity} % TODO: integrate from standalone

LABEL thm:ds-hpl-transfer
chapters/theory/ordered_associative_chiral_kd.tex:11439:\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone

LABEL thm:langlands-bar-bridge
chapters/theory/derived_langlands.tex:95:\label{thm:langlands-bar-bridge}
chapters/theory/ordered_associative_chiral_kd.tex:11440:\phantomsection\label{thm:langlands-bar-bridge} % TODO: integrate from standalone




thinking
**Investigating Duplicate Labels**

I’m realizing there are duplicate labels across the chapters, and I need to check for warnings regarding this issue. The exact fix would be to remove any phantom duplicates and ensure references point to the actual labels instead. It's crucial because duplicate labels can cause unpredictable resolution. I should verify if these duplicates exist in the main.tex file since they appear to be real. Perhaps I can use `grep` or `rg` results to locate them, noting down findings for each duplicate cluster.
thinking
**Fixing Phantom Labels**

I need to delete any phantom labels. If local references require fallbacks, I'll replace each `\ref{...}` with the actual chapter labels like `derived_langlands` or `genus1_seven_faces`. Alternatively, I could rename fallback labels using the `standalone:` prefix to prevent collisions. It's worth checking whether `part:seven-faces` and `part:v1-frontier` are genuine labels or just placeholders. The search showed none aside from placeholders, so maybe I should separate findings about duplicates and unresolved placeholders to clarify the situation.
thinking
**Importing Missing Definitions**

I need to address the missing definitions or equations by either importing them or renaming the placeholder labels to start with `placeholder:`. I'll also update the local references until everything is fully integrated. This issue is significant because it isn’t a duplicate with the main content, as it relates to genuinely missing information. Additionally, I noticed that lines 11428-11440 have some duplicate chapter labels that create cross-reference collisions, along with placeholders that lack targets, like `part:seven-faces`.
exec
/bin/zsh -lc 'for lbl in part:seven-faces part:v1-frontier sec:bar-complex-introduction sec:complementarity thm:ds-hpl-transfer; do echo LABEL $lbl; rg -n -F "'"\\\\ref{"'$lbl}|'"\\\\eqref{"'$lbl}|'"\\\\autoref{"'$lbl}|'"\\\\cref{"'$lbl}|'"\\\\label{"'$lbl}" chapters standalone; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
LABEL part:seven-faces

LABEL part:v1-frontier

LABEL sec:bar-complex-introduction

LABEL sec:complementarity

LABEL thm:ds-hpl-transfer


thinking
**Considering placeholder issues**

I’m thinking about how no references might just mean unused placeholders, which could be harmless unless they lead to duplicate labels. But those placeholders can clutter things and potentially cause future drift. I wonder if it would be better to focus on the actually used labels. Searching for any references might help clarify if these top placeholders are mentioned in the chapter or not. The concern about duplicate labels definitely stands out.
exec
/bin/zsh -lc 'for lbl in def:chiral-coproduct eq:bar-degree1-yangian eq:yangian-drinfeld-coprod eq:yangian-qybe; do echo LABEL $lbl; rg -n -F "'"\\\\ref{"'$lbl}|'"\\\\eqref{"'$lbl}|'"\\\\autoref{"'$lbl}|'"\\\\cref{"'$lbl}" chapters/theory/ordered_associative_chiral_kd.tex chapters standalone/ordered_chiral_homology.tex; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
LABEL def:chiral-coproduct

LABEL eq:bar-degree1-yangian

LABEL eq:yangian-drinfeld-coprod

LABEL eq:yangian-qybe

exec
/bin/zsh -lc 'for lbl in ch:derived-langlands ch:genus1-seven-faces ch:holographic-datum-master ch:landscape-census comp:bp-kappa-three-paths conv:three-hochschild prop:nilpotent-transport-typeA thm:langlands-bar-bridge; do echo LABEL $lbl; rg -n -F "'"\\\\ref{"'$lbl}|'"\\\\eqref{"'$lbl}|'"\\\\autoref{"'$lbl}|'"\\\\cref{"'$lbl}" chapters standalone | sed -n '"'1,20p'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
LABEL ch:derived-langlands

LABEL ch:genus1-seven-faces

LABEL ch:holographic-datum-master

LABEL ch:landscape-census

LABEL comp:bp-kappa-three-paths

LABEL conv:three-hochschild

LABEL prop:nilpotent-transport-typeA

LABEL thm:langlands-bar-bridge

exec
/bin/zsh -lc "rg -n 'Swiss-cheese-formal bar complexes|SC-formal bar complexes|Swiss-cheese formal bar complexes|bar complexes; algebras with higher-order poles' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order

thinking
**Exploring mathematical structures**

Okay, something feels off with the phrase "Swiss-cheese-formal bar complexes." The main constitution states that a bar complex is E1-coassociative, and I'm considering the SC structure on the derived center. I should search in chapters for class G or compare it to the chapter introduction or en_koszul. I think looking up "Swiss-cheese-formal" will help clarify this confusion. Let's dig deeper!
exec
/bin/zsh -lc "rg -n 'Swiss-cheese-formal|SC-formal|class~\\\\mathbf\\{G\\}|SC-formality iff' standalone/programme_summary*.tex chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/theory/en_koszul_duality.tex chapters/examples/free_fields.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:2878:a chiral algebra in the standard landscape is SC-formal if and
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
chapters/connections/concordance.tex:7202: & SC-formality characterises class~$\mathbf{G}$:
chapters/connections/concordance.tex:9789:& SC-formality $\iff$ class~$\mathbf{G}$
standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary.tex:1812: $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar

thinking
**Inspecting chapter preface**

I’m considering whether the chapter preface refers to chiral algebra in the SC-formal context instead of the bar complex. It might be useful to take a closer look at the standalone lines to clarify this. I want to ensure I understand the content accurately so I can convey the right information. Let’s dig into those lines for better context!
exec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '1426,1436p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '1808,1814p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections5_8.tex | sed -n '128,136p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1426	\end{center}
  1427	
  1428	\noindent
  1429	This table encodes a structural dichotomy: algebras whose
  1430	collision residue has at most a simple pole (classes~$\mathbf{G}$
  1431	and~$\mathbf{L}$) have finite shadow depth and
  1432	Swiss-cheese-formal bar complexes; algebras with higher-order
  1433	poles (class~$\mathbf{M}$) have infinite shadow towers and
  1434	genuinely non-formal $A_\infty$-structure.
  1435	
  1436	The dichotomy is not a property of individual OPE coefficients
 succeeded in 50ms:
  1808	landscape into two physical regimes:
  1809	
  1810	\begin{enumerate}[(a)]
  1811	\item \emph{Gauge theories} (classes~$\mathbf{G}$,
  1812	 $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
  1813	 complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
  1814	 The collision residue has at most a simple pole.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2874,2882p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   128	\end{center}
   129	
   130	\noindent
   131	This table encodes a structural dichotomy: algebras whose
   132	collision residue has at most a simple pole (classes~$\mathbf{G}$
   133	and~$\mathbf{L}$) have finite shadow depth and
   134	Swiss-cheese-formal bar complexes; algebras with higher-order
   135	poles (class~$\mathbf{M}$) have infinite shadow towers and
   136	genuinely non-formal $A_\infty$-structure.
 succeeded in 51ms:
  2874	$\mathbf{M}$ = genuinely nonlinear.
  2875	
  2876	The Swiss-cheese formality condition ($m_k^{\mathrm{SC}}=0$ for
  2877	all $k\ge 3$) selects exactly class~$\mathbf{G}$:
  2878	a chiral algebra in the standard landscape is SC-formal if and
  2879	only if it is Heisenberg
  2880	(Proposition~\ref{prop:sc-formal-iff-class-g}).
  2881	The forward direction is immediate (abelian bracket kills all
  2882	nested operations); the converse uses nondegeneracy of the

thinking
**Searching for terminology clarity**

I need to look into the phrase "Swiss-cheese-formal bar complex" because something seems off about it. I could explore other standalone terms or concepts that relate to SC formality and class L, perhaps in a survey or introduction. I'll try searching "class L SC-formal," but it’s unclear if that would yield useful results. I’m just trying to gather accurate information!
exec
/bin/zsh -lc "rg -n 'class.?L|classes~\\\\mathbf\\{G\\} and~\\\\mathbf\\{L\\}.*SC|Swiss-cheese-formal bar complex|SC-formal iff class|SC-formality iff' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/garland_lepowsky.tex:899:\begin{theorem}\label{thm:km-class-L}
standalone/garland_lepowsky.tex:1149:Theorem~\ref{thm:km-class-L}.
standalone/garland_lepowsky.tex:1306: (Theorem~\ref{thm:km-class-L}) places affine Kac--Moody
standalone/classification.tex:141:\begin{definition}\label{def:class-L}
standalone/classification.tex:404:data for exceptional and non-simply-laced types. All are class~L.
standalone/classification.tex:665:class~L algebras have $\rho = 0$ (the tower terminates, so there is no
standalone/classification.tex:868:\begin{proposition}[SC-formality iff class~$\mathbf{G}$]
standalone/shadow_towers.tex:1281:\label{subsec:class-L}
chapters/connections/bv_brst.tex:1769:$c_r(\cA)$ vanishes. For class~L
standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/introduction_full_survey.tex:4840:The bar-cobar adjunction $B \dashv \Omega$ encodes boundary data into a bar coalgebra and recovers it via the cobar construction. On the Koszul locus, Theorem~B guarantees exact recovery. Chapter~\ref{chap:holographic-codes-koszul} proves the equivalence: \emph{chiral Koszulness is equivalent to exact holographic reconstruction}. The twelve characterisations K1--K12 of Koszulness (Theorem~\ref{thm:koszul-equivalences-meta}), comprising ten unconditional equivalences, one conditional (the Lagrangian criterion, conditional on perfectness; unconditional for the standard landscape), and one one-directional ($\mathcal{D}$-module purity, with only the forward direction proved), provide a comprehensive suite of conditions for the holographic code to admit exact recovery. The bifunctor decomposition theorem is a further proved consequence outside the twelve numbered items. The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).
standalone/introduction_full_survey.tex:4844:At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval: $S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}). For Virasoro, complementarity sharpens this: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C with Koszul conductor $K = 26$, saturated at the self-dual point $c = 13$. Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; and class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.
chapters/connections/concordance.tex:269:class~L (single Massey product, $r_{\max} = 3$),
chapters/connections/concordance.tex:2677:$(m, \Delta_z)$ when the coproduct tower is included: class~L
chapters/connections/concordance.tex:2861:to a \emph{two-channel complexity plane} $(m, \Delta_z)$: class~L
chapters/connections/thqg_entanglement_programme.tex:550: Hamiltonian, class~L cubic, and so on.
chapters/connections/frontier_modular_holography_platonic.tex:2573:$E_\infty = E_2$. Shadow depth~$3$ (Lie/tree class~L).
chapters/connections/thqg_fredholm_partition_functions.tex:1724:\label{prop:thqg-X-class-L-feynman}%
chapters/connections/thqg_fredholm_partition_functions.tex:1725:\index{class L!Feynman integrals}%
exec
/bin/zsh -lc "rg -n 'ClaimStatusConditional' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Investigating seam audit**

I think I need to consider the seam audit as a standalone introduction. I'll search for relevant terms like "Swiss-cheese-formal bar," "bar differential acquires curvature," and check the "E1" row. There's potential here to connect these concepts meaningfully, and I want to make sure I'm accurately covering each aspect. Let's see where this inquiry leads me and how it all ties together!
exec
/bin/zsh -lc "rg -n 'Swiss-cheese-formal|bar differential extracts OPE|acquires curvature \\\\kappa|Swiss-cheese.*E_1|4d--3d--2d|Operadic type' standalone/introduction_full_survey.tex standalone/survey_modular_koszul_duality*.tex standalone/survey_track_*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/survey_modular_koszul_duality_v2.tex:374:The ordered bar differential extracts OPE data at each collision
standalone/survey_modular_koszul_duality.tex:6183:The bar differential extracts OPE residues along collision divisors

thinking
**Investigating survey details**

It seems the search is too broad, but maybe that’s not an issue. I should inspect the survey's Swiss-cheese discussion to see if it's stale. Looking closely at the same table lines around 6044 could be useful too, as they might also be outdated. Plus, I should search for "closed colour" within the survey to gather more specific insights. This might help clarify things a bit!
exec
/bin/zsh -lc "rg -n 'Closed colour|Open colour|bar complex remains|derived center pair|not on B\\(A\\)|not the bulk object|The bar complex .*SC|SC\\"'^'"\\{ch,top\\} emerges' standalone/survey_modular_koszul_duality.tex standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/survey_modular_koszul_duality_v2.tex:1524:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality.tex:2363:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality.tex:6070:structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:7110: structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:7757:on the open colour, and the derived center pair
exec
/bin/zsh -lc "rg -n 'self-dual|self dual|Koszul dual cooperad|classical Swiss-cheese operad .*Koszul|Swiss-cheese operad .*Koszul' standalone/programme_summary*.tex standalone/survey_modular_koszul_duality*.tex chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex:568:tower is self-dual. At $c = 26$: $\kappa(\Vir_0^!) = 0$, the
standalone/programme_summary_sections2_4.tex:292:At the self-dual point ($c = 13$ for Virasoro), the
standalone/programme_summary_sections2_4.tex:791:$c \ne 0$. The self-dual point $c = 13$
standalone/survey_modular_koszul_duality_v2.tex:745:At $c=13$, Virasoro is self-dual under Koszul duality.
standalone/survey_modular_koszul_duality_v2.tex:857:``self-dual at $c=13$ under Koszul
standalone/survey_modular_koszul_duality_v2.tex:1652:$h_{\cA^!}$. Three properties: $\Delta_\cA$ is self-dual
standalone/survey_modular_koszul_duality_v2.tex:1914:G16: Page curve at $c=13$ from the shadow connection at the self-dual
standalone/survey_modular_koszul_duality_v2.tex:2619:shadow tower. Koszul dual: $\Vir_c^!=\Vir_{26-c}$ (self-dual at $c=13$). Complementarity (Virasoro branch, sum $=13$; KM
standalone/survey_modular_koszul_duality_v2.tex:2712:Koszul dual: $\cW_3^!=\cW_{3,100-c}$ (self-dual at $c=50$).
standalone/survey_modular_koszul_duality_v2.tex:3233:For the rank-$1$ lattice at self-dual radius $R = 1$, every
standalone/survey_modular_koszul_duality_v2.tex:3619:On the open/closed side, the Koszul dual cooperad
standalone/survey_modular_koszul_duality_v2.tex:3746:The classical Swiss-cheese operad $\SC$ is Koszul
standalone/survey_modular_koszul_duality_v2.tex:4427:Koszul dual $\Vir_{26-c}$ (self-dual at $c = 13$, not $c = 26$);
standalone/programme_summary.tex:866:At the self-dual point ($c = 13$ for Virasoro), the
standalone/programme_summary.tex:1366:$c \ne 0$. The self-dual point $c = 13$
standalone/programme_summary.tex:1868:tower is self-dual. At $c = 26$: $\kappa(\Vir_0^!) = 0$, the
chapters/theory/en_koszul_duality.tex:1255:over the Koszul dual cooperad
chapters/theory/en_koszul_duality.tex:1308:coalgebra over the Koszul dual cooperad
chapters/theory/en_koszul_duality.tex:1595:\begin{proposition}[Koszul dual cooperad of
chapters/theory/en_koszul_duality.tex:1599:\index{Swiss-cheese operad!Koszul dual cooperad|textbf}

thinking
**Investigating chapter formulas**

I’m considering that the chapter file might use different labels, which could cause seam issues if the formulas drift. I think it’s a good idea to search for filenames and relevant formulas, like `w3_holographic_datum.tex`, since that chapter likely has integrations. I could compare key formulas like kappa and genus2 by inspecting lines around the main theorems. The user needs to know if the formulas in standalone papers match the main text, which is worth checking!
exec
/bin/zsh -lc "sed -n '136,206p' standalone/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '130,220p' chapters/examples/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '5c/6|100-c|delta F|Four-channel|Roots of|Lambda_0|kappa|H_3|50|c/6|c/2' standalone/w3_holographic_datum.tex chapters/examples/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
modular characteristic $\kappa = \mathrm{av}(r(z))$ is its
$\Sigma_2$-coinvariant projection.

% ================================================================
\section{\texorpdfstring{$\kappa(\Walg_3) = 5c/6$}{kappa(W3) = 5c/6}
and channel decomposition}\label{sec:kappa}
% ================================================================

\begin{theorem}[Modular characteristic]\label{thm:kappa}
For $\Walg_3$ at generic central charge $c \neq 0$,
\begin{equation}\label{eq:kappa}
\kappa(\Walg_3) = \frac{5c}{6}.
\end{equation}
Equivalently, $\kappa(\Walg_3) = c \cdot (H_3 - 1)$ where
$H_3 = 1 + 1/2 + 1/3$ is the third harmonic number.
\end{theorem}

\begin{proof}
The algebra $\Walg_3 = \Walg^k(\fsl_3, f_{\mathrm{prin}})$ is the
Drinfeld--Sokolov reduction of $\widehat{\fsl}_3$ at the principal
 succeeded in 52ms:

The spectral $r$-matrix is the binary genus-0 collision residue of
the bar-intrinsic MC element:
\begin{equation}\label{eq:w3hol-r-collision}
r(z) := \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\Walg_3}).
\end{equation}
The pole structure is governed by the OPE poles minus one
(: the bar propagator $d\log(z-w)$
absorbs one power of $(z-w)$).
The four channel pieces are catalogued in
\S\ref{sec:w3hol-r-matrix-channels}.

\subsection{The MC element \texorpdfstring{$\Theta_{\cA}$}{Theta A}}
\label{subsec:w3hol-Theta}

By the bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}), the element
\begin{equation}
\Theta_{\Walg_3} := D_{\Walg_3} - d_0
\end{equation}
 succeeded in 51ms:
standalone/w3_holographic_datum.tex:69:characteristic is $\kappa(\Walg_3) = 5c/6$ with channel
standalone/w3_holographic_datum.tex:70:decomposition $\kappa_T = c/2$, $\kappa_W = c/3$; the Koszul dual
standalone/w3_holographic_datum.tex:71:is $\Walg_3(100-c)$ with complementarity sum $250/3$; the
standalone/w3_holographic_datum.tex:74:primaries by $\Lambda_0|h\rangle = (h^2 - 9h/5)|h\rangle$,
standalone/w3_holographic_datum.tex:76:$\delta F_2(\Walg_3) = (c+204)/(16c)$, which is nonzero for all
standalone/w3_holographic_datum.tex:117: complementarity sum $\kappa + \kappa^! = 250/3 \neq 0$.
standalone/w3_holographic_datum.tex:118:\item The genus-$2$ cross-channel correction $\delta F_2 = (c+204)/(16c)$
standalone/w3_holographic_datum.tex:119: witnesses the failure of the scalar formula $F_g = \kappa \lambda_g$
standalone/w3_holographic_datum.tex:128:weights. The modular characteristic $\kappa$ is the genus-$1$
standalone/w3_holographic_datum.tex:136:modular characteristic $\kappa = \mathrm{av}(r(z))$ is its
standalone/w3_holographic_datum.tex:140:\section{\texorpdfstring{$\kappa(\Walg_3) = 5c/6$}{kappa(W3) = 5c/6}
standalone/w3_holographic_datum.tex:141:and channel decomposition}\label{sec:kappa}
standalone/w3_holographic_datum.tex:144:\begin{theorem}[Modular characteristic]\label{thm:kappa}
standalone/w3_holographic_datum.tex:146:\begin{equation}\label{eq:kappa}
standalone/w3_holographic_datum.tex:147:\kappa(\Walg_3) = \frac{5c}{6}.
standalone/w3_holographic_datum.tex:149:Equivalently, $\kappa(\Walg_3) = c \cdot (H_3 - 1)$ where
standalone/w3_holographic_datum.tex:150:$H_3 = 1 + 1/2 + 1/3$ is the third harmonic number.
standalone/w3_holographic_datum.tex:157:$\kappa(\Walg_N) = c \cdot (H_N - 1)$, specializing at $N = 3$ to
standalone/w3_holographic_datum.tex:158:$c(1/2 + 1/3) = 5c/6$.
standalone/w3_holographic_datum.tex:164:\kappa(\Walg_3) = \kappa_T + \kappa_W, \qquad

thinking
**Analyzing label syncing**

I think this situation might be significant. Instead of syncing actual labels, these standalones are substituting "full monograph." This means that stale or missing transitions are concealed. I could report it as a medium since the files hide broken seam references by changing `\ref`. To fix it, I should replace the `\ref` redefinition with explicit local labels or visible `??` during the standalone build. If I need a fallback, I can use a macro like `\fullmonoref{...}` for specific seam references. I'll need to search through files for relevant citations and list them.
exec
/bin/zsh -lc "rg -n '\\\\renewcommand\\{\\\\ref\\}' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/computations.tex:33:\renewcommand{\ref}[1]{%
standalone/classification.tex:38:\renewcommand{\ref}[1]{%
standalone/programme_summary_sections5_8.tex:62:\renewcommand{\ref}[1]{%
standalone/programme_summary_sections2_4.tex:63:\renewcommand{\ref}[1]{%
standalone/survey_track_b_compressed.tex:149:\renewcommand{\ref}[1]{%
standalone/survey_track_a_compressed.tex:94:\renewcommand{\ref}[1]{%
standalone/introduction_full_survey.tex:107:\renewcommand{\ref}[1]{%
standalone/riccati.tex:36:\renewcommand{\ref}[1]{%
standalone/survey_modular_koszul_duality.tex:102:\renewcommand{\ref}[1]{%
standalone/programme_summary_sections9_14.tex:61:\renewcommand{\ref}[1]{%
standalone/survey_modular_koszul_duality_v2.tex:165:\renewcommand{\ref}[1]{%
exec
/bin/zsh -lc 'for lbl in thm:e3-cs thm:cfg; do echo LABEL $lbl; rg -n -F "'"\\\\ref{"'$lbl}|'"\\\\eqref{"'$lbl}|'"\\\\autoref{"'$lbl}|'"\\\\cref{"'$lbl}" chapters standalone | sed -n '"'1,40p'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
LABEL thm:e3-cs

LABEL thm:cfg






thinking
**Fixing duplication issues in LaTeX**

I’m addressing a collision issue with duplicate labels in LaTeX. First, I suggest deleting phantom labels. If navigation anchors are still needed, I could rename them to “placeholder” or point references to actual labels. For duplicates, I think labeling them based on importance could help, like using [HIGH] or [CRITICAL]. I need to extract findings related to `ordered_chiral_homology` and also address any label drift regarding `thm:e3-cs`. Adjusting these markers will improve clarity.
thinking
**Updating theorem references**

I’m considering renaming the standalone theorem to `thm:e3-cs-standalone` and updating local references, while keeping `thm:e3-cs` for the main manuscript theorem. Alternatively, I could rewrite the standalone theorem to match the chapter theorem and create a new proposition for any additional material. I also need to look at the `thm:cfg` bibkey drift, which may not be significant, but I should include it for clarity. Lastly, I’ll ensure the references to `CFG25` are consistent across the board.
thinking
**Examining global ref wrappers**

I want to investigate the global `\ref` redefinition wrappers across multiple standalone files. These could be a medium concern since they might be hiding unresolved references. The exact fix would be to remove these wrappers and switch to using a dedicated helper for better clarity. This approach should help avoid potential confusion and keep my references organized. I think it's important to address this to enhance the overall structure.
thinking
**Reviewing LaTeX files**

I'm looking at a few LaTeX files, checking if they use `newcommand` instead of `providecommand`. I need to convert any preamble symbol declarations in `main.tex` to `\providecommand`, keeping local overrides carefully organized.

There’s also a potential issue with a table in `standalone/programme_summary.tex` where closed and open colors might be confused. I’ll need to verify this against the main chapter's content to ensure consistency, as it relates to the Swiss-cheese issue.
thinking
**Organizing findings**

To keep things manageable, I might want to separate my findings into critical and high priorities. For instance, there's a critical table related to SC color and curvature in `programme_summary.tex`, and then a high-priority issue about class-L formalities in the same file.

I should verify the line numbers for accuracy while also checking for duplicates across two files to see if I can combine my findings. It looks like these files might have very similar content, so consolidating them could work well to cover stale claims effectively.
exec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '108,116p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '4102,4112p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '4314,4324p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   108	
   109	\numberwithin{equation}{section}
   110	
   111	% Claim status macros (standalone: no-op definitions)
   112	\providecommand{\ClaimStatusConjectured}{}
   113	\providecommand{\ClaimStatusProvedHere}{}
   114	\providecommand{\ClaimStatusProvedElsewhere}{}
   115	\providecommand{\ClaimStatusHeuristic}{}
   116	
 succeeded in 52ms:
  4102	the $\psi$-basis.
  4103	\end{remark}
  4104	
  4105	\begin{theorem}[Universal Miura cross-term coefficient]
  4106	\label{thm:miura-cross-universality}
  4107	\ClaimStatusProvedHere
  4108	Let $W_s$ denote the spin-$s$ primary generator of
  4109	$\cW_{1+\infty}[\Psi]$ (so $W_1 = J$, $W_2 = T$,
  4110	$W_3 = W$, $W_4$, \ldots). For each $s \geq 2$,
  4111	the spectral coproduct of
  4112	Theorem~\textup{\ref{thm:w-infty-chiral-qg}} satisfies
 succeeded in 51ms:
  4314	\end{remark}
  4315	
  4316	\begin{proposition}[Yangian antipode on $\cW_{1+\infty}$:
  4317	explicit formula and vertex Hopf obstruction]
  4318	\label{prop:w-infty-antipode-obstruction}
  4319	\ClaimStatusProvedHere
  4320	Let $\cW_{1+\infty}[\Psi]$ carry the chiral quantum group
  4321	structure of Theorem~\textup{\ref{thm:w-infty-chiral-qg}},
  4322	with spectral coproduct
  4323	$\Delta_z(T(u)) = T(u) \otimes T(u-z)$ and Miura
  4324	identification $\psi_1 = J$,



thinking
**Identifying content issues**

I might be facing a seam issue with `standalone/programme_summary*.tex` since it uses section labels similar to chapters. While that may not be a problem, the content certainly is. There’s a specific line where the description seems off regarding a table, which misinterprets the information. I need to keep the first paragraph intact and remove any misleading table or prose. Also, it seems like I can consolidate information about the 3D Swiss-cheese E1 into the same section for clarity.
thinking
**Exploring file audits**

It seems the user might not need the exact unit calculations, so I’ll compute it anyway. I could define “Checked” as the unique seam files read or searched during the audit. This includes all standalone .tex files and chapter transition files. We used rg to check 34 standalone .tex files and about 85 chapters. However, did we exhaust the audit surface completely? I think I could set “Checked” to 42, considering we searched everything.
thinking
**Calculating findings and checks**

The user is asking for a summary, and I’m considering how to present it clearly. I can say `Checked: 42 | Findings: 8`. Additionally, I should compute the specific distinct files I opened or inspected through search results. Maybe that's around 17? To simplify, since it's about the combination of standalone and chapter seams, I could summarize it as `Checked: 34 standalones + 12 chapter seam files = 46`, assuming that's accurate. I should check if there are indeed 33 standalones in `.tex`.
exec
/bin/zsh -lc "echo -n 'standalone_tex='; rg --files standalone -g '*.tex' | wc -l; echo -n 'chapter_seam_files='; printf '%s
' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/frame/preface.tex chapters/examples/w3_holographic_datum.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/yangians_computations.tex chapters/connections/genus_complete.tex chapters/theory/derived_langlands.tex chapters/connections/genus1_seven_faces.tex chapters/connections/holographic_datum_master.tex chapters/examples/landscape_census.tex chapters/connections/subregular_hook_frontier.tex | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standalone_tex=      36
chapter_seam_files=      16



thinking
**Organizing findings**

I'm checking files: 52 in total, which includes 36 standalone .tex files and 16 chapter seam files. That seems plausible since we searched through all those. I think I found about 8 or 9 issues that need deciding on. I need to gather specific lines for the duplicate labels and phantom labels I've encountered. I could format the findings with information about exact target lines and it seems reasonable to group similar findings together.
thinking
**Listing inconsistencies**

The user wants to see every inconsistency, so I need to list issues from both files separately. Here are the findings:

1. In `standalone/programme_summary.tex:1600`, there are issues with SC colors and a need to rewrite the section.
2. The same copy issue shows up in `standalone/programme_summary_sections5_8.tex:300`.
3. Duplicate phantom labels in `chapters/theory/ordered_associative_chiral_kd.tex:11428` conflict with real labels, so I should fix that by deleting placeholder labels.
4. Finally, phantom labels for definitions in `chapters/theory/ordered_associative_chiral_kd.tex:40` do not link correctly, requiring an update.
thinking
**Fixing reference issues**

Alright, I need to remove the global `\renewcommand{\ref}`. Instead, I should introduce a dedicated fallback macro only where it’s necessary. This way, any unresolved seam references will fail visibly during synchronization. It’s important to keep things clear and manageable, as that can help avoid confusion later on. I think this approach will lead to more reliable reference management! Let’s make sure we implement that change effectively.
codex
- [CRITICAL] `standalone/programme_summary.tex:1600` — PROBLEM: the Swiss-cheese seam is stale and self-contradictory. This section first says `\mathrm{SC}^{\mathrm{ch,top}}` emerges on the derived center pair, then the table at `1600`-`1608` reassigns the closed/open colors to the bar differential and deconcatenation, the prose at `1614`-`1617` says the bar differential “acquires curvature `\kappa(\cA)\cdot\omega_g`”, the hierarchy table at `1785` reduces the 3d layer to plain `E_1`, and the class summary at `1432` and `1812` calls classes `\mathbf{G},\mathbf{L}` “Swiss-cheese-formal bar complexes.” Main text rejects all of this: [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1248) puts `\SCchtop` on the derived center pair, not the bar complex; [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2695) says `d^2=0` always for the bar differential; [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2876) says SC-formality holds iff class `\mathbf{G}`. FIX: rewrite `sec:swiss-cheese` to match `princ:sc-two-incarnations`; delete the closed/open color table or replace it with a bar-vs-derived-center separation table; replace “acquires curvature `\kappa\omega_g`” with “the bar differential still satisfies `d_{\bar B}^2=0`; curvature appears on the curved `A_\infty`/fiber side”; change the 3d row at `1785` to `\SCchtop` on the derived center pair; change the class statements at `1432` and `1812` to “finite shadow depth for classes `\mathbf{G},\mathbf{L}`; SC-formality only for class `\mathbf{G}`.”

- [CRITICAL] `standalone/programme_summary_sections5_8.tex:300` — PROBLEM: this split standalone preserves the same broken Swiss-cheese story as the full summary. The table at `300`-`308` identifies SC colors with `d_{\bar B}` and `\Delta`, the prose at `314`-`317` again attributes curvature to the bar differential, the hierarchy table at `485` reduces the 3d layer to `E_1`, and the class summary at `134` says classes `\mathbf{G},\mathbf{L}` have “Swiss-cheese-formal bar complexes.” These all conflict with [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1248), [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2695), and [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2876). FIX: make the same rewrite as above in this extract; do not keep a second, stale version of the Swiss-cheese summary.

- [CRITICAL] `chapters/theory/ordered_associative_chiral_kd.tex:11428` — PROBLEM: this chapter contains phantom labels that duplicate real labels already defined elsewhere in the main manuscript: `ch:derived-langlands` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), `ch:genus1-seven-faces` duplicates [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2), `ch:holographic-datum-master` duplicates [chapters/connections/holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), `ch:landscape-census` duplicates [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:2), `comp:bp-kappa-three-paths` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), `conv:three-hochschild` duplicates [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:115), `prop:nilpotent-transport-typeA` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:1519), and `thm:langlands-bar-bridge` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:95). FIX: delete every duplicate phantom label in this block. Where cross-references are needed, point to the real chapter labels; if a local placeholder is unavoidable, rename it with a non-colliding prefix such as `placeholder:`.

- [HIGH] `chapters/theory/ordered_associative_chiral_kd.tex:40` — PROBLEM: the chapter manufactures seam anchors for content that was never integrated: `def:chiral-coproduct`, `eq:bar-degree1-yangian`, `eq:yangian-drinfeld-coprod`, and `eq:yangian-qybe` exist here only as `\phantomsection\label{...}` stubs, while the actual content still lives in `standalone/ordered_chiral_homology.tex` at `2523`, `8978`, `781`, and `684`. That is not integration; it is dead scaffolding. FIX: either import the actual definition/equation blocks into the chapter at the correct logical locations, or rename these stubs to `placeholder:*` and update any local references so the main manuscript stops pretending the content is present.

- [HIGH] `standalone/ordered_chiral_homology.tex:111` — PROBLEM: the standalone suppresses epistemic status by defining claim-status macros as empty no-ops. The file still uses those macros on live theorem surfaces, e.g. `\ClaimStatusProvedHere` at `4107` and `4319`, but the printed standalone erases the status boundary completely. That is exactly how stale claims survive migration. FIX: replace the empty definitions at `112`-`115` with visible markers matching the survey standalones, e.g. `\textsuperscript{\textsc{[ph]}}`, `\textsuperscript{\textsc{[pe]}}`, `\textsuperscript{\textsc{[cj]}}`, `\textsuperscript{\textsc{[he]}}`, or load the shared claim-status macro block.

- [HIGH] `standalone/ordered_chiral_homology.tex:455` — PROBLEM: the standalone and the chapter reuse the same theorem labels for materially different theorem surfaces. `thm:e3-cs` here is “Derived centre, topologization, and Chern--Simons” with a three-part affine bulk package/topologization statement, while [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4112) uses `thm:e3-cs` for “The `\Ethree`-algebra and Chern--Simons” with a different four-part statement and explicit `\ClaimStatusProvedElsewhere`. The same drift hits `thm:cfg` at `5905`, which cites `CFG26` while the chapter theorem at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4148) cites `CFG25` and carries status. FIX: do one of two things, and only one: either rename the standalone labels to `thm:e3-cs-standalone` / `thm:cfg-standalone` and update local refs, or rewrite the standalone theorems to match the chapter statements and statuses exactly, including the repository citation key.

- [MEDIUM] `standalone/classification.tex:38` — PROBLEM: this standalone globally redefines `\ref` to silently print “full monograph” on missing labels. The same seam-masking hack recurs at `standalone/computations.tex:33`, `standalone/programme_summary_sections2_4.tex:63`, `standalone/programme_summary_sections5_8.tex:62`, `standalone/programme_summary_sections9_14.tex:61`, `standalone/introduction_full_survey.tex:107`, `standalone/riccati.tex:36`, `standalone/survey_modular_koszul_duality.tex:102`, `standalone/survey_modular_koszul_duality_v2.tex:165`, `standalone/survey_track_a_compressed.tex:94`, and `standalone/survey_track_b_compressed.tex:149`. This hides broken seam refs instead of fixing them. FIX: remove the global `\renewcommand{\ref}` in each file; if a fallback is genuinely needed, introduce a dedicated macro such as `\fullmonoref{...}` only at the intended out-of-scope references and leave ordinary `\ref` unresolved until the labels are synced.

- [LOW] `standalone/ordered_chiral_homology.tex:39` — PROBLEM: integration-target standalones still use unguarded `\newcommand` blocks instead of `\providecommand`, so they are not safe to port into chapter files. The same problem appears at `standalone/N1_koszul_meta.tex:34`, `standalone/N3_e1_primacy.tex:34`, `standalone/N4_mc4_completion.tex:33`, `standalone/N5_mc5_sewing.tex:33`, `standalone/bp_self_duality.tex:36`, `standalone/classification_trichotomy.tex:33`, `standalone/chiral_chern_weil.tex:37`, and `standalone/programme_summary_section1.tex:36`. FIX: convert all manuscript-shared preamble symbols in these files from `\newcommand` to `\providecommand`, following the chapter-side pattern in [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5); keep any true override behind a standalone-only guard instead of making it global.

## Summary
Checked: 52 | Findings: 8 | Verdict: FAIL
tokens used
363,363
