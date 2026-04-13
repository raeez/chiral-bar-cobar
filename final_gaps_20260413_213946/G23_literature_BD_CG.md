# G23_literature_BD_CG (416s)



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
session id: 019d88a7-f12f-7e53-9cd4-7d15c6fc650d
--------
user
<task>
You are a FINAL GAPS agent. This is the LAST PASS. Every remaining gap must be closed.
832 agents have already run. You fix what they couldn't finish.
Read files on disk — they reflect ALL prior work. Be surgical. Be complete.
</task>
<action_safety>Keep changes scoped. After edits, re-read and verify. Grep for AP violations.</action_safety>
<completeness_contract>Fix EVERY issue in your scope. Report: FIXED or BLOCKED (with reason).</completeness_contract>
<verification_loop>After all edits, verify no new violations introduced.</verification_loop>


Literature cross-check: BD + CG/CFG.

1. BD [BD04]: Does our bar construction agree with BD's factorization coalgebra?
   Read bar_construction.tex. Check: augmentation, Ran space, Arnold relation.
2. CG [CG17]: Does our BV/bar (MC5) agree with CG's BV quantization?
3. CFG [arXiv:2602.12412]: Does our E_3 topologization agree with CFG's E_3?

Write findings as Remarks in the relevant .tex files if discrepancies found.
If consistent: write Remark[Literature confirmation] noting the agreement.
mcp startup: no servers

thinking
**Planning file exploration**

I’m considering using the spawn_agent explorer to find relevant files or labels efficiently. However, the instructions indicate that I should read files on disk to reflect prior work. While the explorer could help identify relevant surfaces, I still need to do a direct read. I think I should start with a commentary update and then work on a plan since this is substantial work. Let's get started!
codex
I’m treating this as a scoped literature-audit pass on the three cited surfaces: BD in `bar_construction.tex`, CG for the BV/bar claim around MC5, and CFG for the `E_3` topologization lane. I’ll read the constitutional files first, then the exact chapter files and nearby labels, and only then patch in minimal Remarks plus verification greps.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Identifying relevant files**

I need to pinpoint specific files, especially the .tex and literature references. Using the `rg` tool seems necessary. I might also require actual paper references rather than just internet sources, especially since network access is restricted. The user requested a literature cross-check for BD + CG/CFG. Since our literature references are potentially stable but without contents provided, I may need to cross-check my memory. I should leverage local resources if available or infer from citations. Even though network access is limited, I might still be able to use the analysis tool.
thinking
**Planning literature cross-check**

Since the user needs a literature cross-check, I must browse for specific papers. I should use the web to access actual papers or search through them. However, I'm also working within a coding environment that requires local repository edits. I need to ensure the modifications are grounded in sources and might have to provide links in the final report. I'll need to locate bibliography keys like BD04, CG17, and arXiv:2602.12412 in the repository. I should inspect files such as bar_construction.tex and those related to MC5 and topologization, then update my plan with the steps needed.
codex
I’ve loaded the repo-wide constitutional files and the risk surface. Next I’m locating the exact theorem/remark lanes for `bar_construction.tex`, the MC5/BV quantization discussion, and the `E_3` topologization result so the edits stay local and label-safe.
Plan update
Scoped literature-audit pass on three surfaces: BD/bar construction, CG/BV quantization around MC5, and CFG/E3 topologization. I will verify local statements against source context, patch only the relevant files, and finish with AP greps and a narrow build-style verification.
  → Locate the exact files, labels, and bibliography entries for BD04, CG17, and CFG in the current TeX tree
  • Read the relevant local sections and cross-check each surface against the cited literature
  • Patch minimal Remarks in the relevant .tex files, only where a discrepancy or confirmation should be recorded
  • Re-read edited regions and run AP-violation greps plus targeted verification
exec
/bin/zsh -lc "rg -n \"bar_construction|BD04|CG17|2602\\.12412|CFG|MC5|topologization|thm:topologization|BV quantization|factorization coalgebra|Arnold relation|Ran\\(\" -S chapters appendices bibliography*.bib *.bib" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg 'bar_construction\\.tex|topologization|koszul_duality|bar.*construction|swiss|hoch|center|editorial_constitution|bar_cobar|mc5'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: no matches found: bibliography*.bib
 succeeded in 51ms:
survey_modular_koszul_duality.pdf
healing_20260413_132214/H23_vol2_bar_cobar_review_heal.md
wave2_audit_20260413_001942/C04_bar_construction.md
wave2_audit_20260413_001942/G03_bar_cobar_adjunction_inversion.md
wave2_audit_20260413_001942/H02_factorisation_swiss_cheese.md
wave2_audit_20260413_001942/H08_hochschild.md
wave2_audit_20260413_001942/G02_cobar_construction.md
wave2_audit_20260413_001942/G04_bar_cobar_adjunction_curved.md
wave2_audit_20260413_001942/J24_engine_swiss_cheese.md
wave2_audit_20260413_001942/G01_bar_construction.md
wave2_audit_20260413_001942/C19_chiral_hochschild_koszul.md
wave2_audit_20260413_001942/C05_cobar_construction.md
wave2_audit_20260413_001942/G09_en_koszul_duality.md
wave2_audit_20260413_001942/I05_bar_cobar_bridge.md
wave2_audit_20260413_001942/G10_chiral_hochschild_koszul.md
wave2_audit_20260413_001942/G15_chiral_center_theorem.md
wave2_audit_20260413_001942/D12_hochschild_disambiguation.md
wave2_audit_20260413_001942/S08_en_to_topologization.md
wave2_audit_20260413_001942/C10_en_koszul_duality.md
wave2_audit_20260413_001942/F06_definitions_hochschild.md

thinking
**Reviewing tool usage**

It looks like the first run failed due to a global issue, so I need to rerun it properly. Using the explorer skill might help, particularly to locate labels for literature references. But since I'm already working on the current task, I think the direct commands might suffice. I need to confirm that I’m using the multi-path-verify skill, as the task suggests this approach. I’ll keep an eye on any changes in shared formulas that might affect the outcome.
codex
I’m using `multi-path-verify` for this pass because the job is exactly a literature-grounded verification of a small claim family. If a confirmation or discrepancy touches duplicated wording beyond the local file, I’ll add `cross-volume-propagation`; otherwise I’ll keep the patch inside the originating chapter files.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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


thinking
**Locating files and entries**

I need to pinpoint the exact files and bibliographic entries. I should use the rg tool correctly this time to streamline the search process. I'm thinking about including the bibliographic files as part of this search. It’s important to be thorough to ensure I don't miss anything crucial! Let’s get started on digging into those files and see what I can find efficiently.
exec
/bin/zsh -lc "rg -n \"BD04|CG17|2602\\.12412|CFG|MC5|topologization|thm:topologization|BV quantization|factorization coalgebra|Arnold relation|Ran\\\\\\(|Arnol[d]?\" -S chapters appendices standalone *.tex refs.bib bibliography.bib main.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:BD04|CG17|2602\.12412|CFG|MC5|topologization|thm:topologization|BV quantization|factorization coalgebra|Arnold relation|Ran\\(|Arnol[d]?)
    ^
error: unclosed group
exec
/bin/zsh -lc "rg -n \"BD04|CG17|2602\\.12412|CFG\" -S ." in /Users/raeez/chiral-bar-cobar succeeded in 168ms:
./resume_20260413_165929/X08_Verlinde_3vol.md:29:3. CROSS-CHECK against published literature (BD, FG, CG, Lurie, PTVV, CFG, Costello-Li)
./resume_20260413_192632/M24_bv_brst.md:54:MC5 BV/bar. Verify harmonic mechanism (AP203). Verify coderived argument (AP202). Cross-check with Costello-Gwilliam BV [CG17].
./final_gaps_20260413_213946/G08_hochschild_theory.md:5590:residue, independently of any comparison with the CFG
./final_gaps_20260413_213946/G08_hochschild_theory.md:5623:$\Gamma(D, \omega_D) \cong \CC\,dz$, this is the CFG
./resume_20260413_192632/M30_v2_3d_gravity.md:54:CLIMAX. Verify topologization scope (affine KM only, NOT unconditional — fix line 6516). Cross-check with CFG E_3. Genus tower.
./resume_20260413_165929/C06_averaging_sugawara.md:9926:-residue, independently of any comparison with the CFG
./resume_20260413_165929/C06_averaging_sugawara.md:10055:-comparison with CFG.
./resume_20260413_165929/C06_averaging_sugawara.md:10366:-$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ and the CFG
./resume_20260413_165929/C06_averaging_sugawara.md:10372:-associated-graded and $\Pthree$ data of the CFG
./resume_20260413_165929/C06_averaging_sugawara.md:10520:-Poisson structures (Beilinson--Drinfeld~\cite{BD04},
./resume_20260413_165929/C06_averaging_sugawara.md:10543:-match the associated-graded and $\Pthree$ data of the CFG
./resume_20260413_165929/C06_averaging_sugawara.md:10963:-by construction (Beilinson--Drinfeld~\cite{BD04}, Chapter 3).
./resume_20260413_165929/C06_averaging_sugawara.md:10980:-topological CFG construction.
./resume_20260413_165929/C06_averaging_sugawara.md:11056:-\subsection{Comparison with CFG: formal disk global sections}
./resume_20260413_165929/C06_averaging_sugawara.md:11061:-carries the KZ connection; the CFG algebra $\cA^\lambda$
./resume_20260413_165929/C06_averaging_sugawara.md:11065:-CFG algebra as the fiber.
./resume_20260413_165929/C06_averaging_sugawara.md:11067:-\begin{theorem}[Formal disk restriction recovers CFG]
./resume_20260413_165929/C06_averaging_sugawara.md:11077:-on the formal disk to the CFG $\Ethree$-algebra of
./resume_20260413_165929/C06_averaging_sugawara.md:11078:-Theorem~\textup{\ref{thm:cfg}}, where the CFG coupling
./resume_20260413_165929/C06_averaging_sugawara.md:11093:-  CFG construction have the same classical limit.


thinking
**Searching for relevant papers**

I need to focus on retrieving the actual research papers relevant to my topic. Maybe I can search for local PDFs or use resources like arXiv and Google Books to find accessible material. I want to limit quotes and zero in on specific sections, such as audit notes related to BD/CG/CFG. I must rely on primary literature for accuracy, but secondary notes might help me locate some key content. I need to check local files and relevant sections cautiously.
thinking
**Using explorer agent**

I think it would be helpful to use the explorer agent to locate specific labels in the files efficiently. The developer mentioned that I should use explorer for codebase-related questions, so this seems like a solid plan. By spawning explorer, I can quickly summarize the information I find. I believe this method will streamline my search and help me get clearer insights into the codebase. Let's dive in and see what I can find!
codex
The file search turned up the expected surfaces plus a likely bibliography wrinkle: the repo has both `CFG25` and `CFG26` history around arXiv `2602.12412`. I’m pulling the local contexts now so I can patch the right citation lane without adding fresh citation debt.
exec
/bin/zsh -lc "rg -n \"BD04|Ran\\(|Arnold|augmentation|T\\"'^c'"\\(s\\"'^{-1}|factorization coalgebra|factorisation coalgebra|Remark'"\\[Literature|Remark\\[BD|Beilinson--Drinfeld\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC5|BV|bar complex|Costello--Gwilliam|CG17|Remark\\[Literature|Remark\\[CG|BV complex =|BV quantization|BRST\" chapters/connections/editorial_constitution.tex chapters/connections/bv_brst.tex standalone/N5_mc5_sewing.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 407

standalone/N5_mc5_sewing.tex:118:state but analytically delicate. One forms the bar complex
chapters/connections/bv_brst.tex:1:\chapter{BV-BRST formalism and Gaiotto's perspective}
chapters/connections/bv_brst.tex:3:\index{Batalin--Vilkovisky|see{BV algebra}}
chapters/connections/bv_brst.tex:5:The physicist's BRST cohomology and the algebraist's bar resolution
chapters/connections/bv_brst.tex:6:are not analogous: they are the same computation. The BV formalism
chapters/connections/bv_brst.tex:7:is a machine for computing derived functors; the bar complex is a
chapters/connections/bv_brst.tex:11:identification inevitable: the BRST operator computes the derived
chapters/connections/bv_brst.tex:16:The BV Laplacian and the sewing operator agree at genus~$0$. The
chapters/connections/bv_brst.tex:18:the BV formalism coincides on $\mathbb{P}^1$ with the bar
chapters/connections/bv_brst.tex:20:BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
chapters/connections/bv_brst.tex:26:A natural obstruction sits in the way. At higher genus, the BV
chapters/connections/bv_brst.tex:30:What is proved in this chapter is the genus-$0$ BV/bar comparison
chapters/connections/bv_brst.tex:44:$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
chapters/connections/bv_brst.tex:54:sewing expansion has no counterpart in the BV side until
chapters/connections/bv_brst.tex:58:\begin{remark}[BRST anomaly brackets and transferred SC operations]
chapters/connections/bv_brst.tex:60:\index{Gaiotto--Kulp--Wu!BRST anomaly brackets}
chapters/connections/bv_brst.tex:61:\index{BRST operator!GKW higher operations}
chapters/connections/bv_brst.tex:62:The BRST-anomaly brackets of Gaiotto--Kulp--Wu~\cite{GKW2025}
 exited 2 in 52ms:
rg: regex parse error:
    (?:BD04|Ran\(|Arnold|augmentation|T\^c\(s\^{-1}|factorization coalgebra|factorisation coalgebra|Remark\[Literature|Remark\[BD|Beilinson--Drinfeld)
                                                ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n \"CFG25|CFG26|2602\\.12412|topologization|E_3|E_3-TOPOLOGICAL|Remark\\[Literature|Formal disk restriction recovers CFG|Costello--Francis--Gwilliam\" chapters/theory/en_koszul_duality.tex bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
chapters/theory/en_koszul_duality.tex:24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
chapters/theory/en_koszul_duality.tex:27:The topologization proof is made constructive by an explicit
chapters/theory/en_koszul_duality.tex:1302:  topologization theorem
chapters/theory/en_koszul_duality.tex:1303:  (Theorem~\textup{\ref{thm:topologization}}).
chapters/theory/en_koszul_duality.tex:2101:$E_2$ to $E_3$ for $E_1$-chiral input requires the Drinfeld
chapters/theory/en_koszul_duality.tex:2939:% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
chapters/theory/en_koszul_duality.tex:2945:\label{sec:topologization}
chapters/theory/en_koszul_duality.tex:2946:\index{topologization theorem|textbf}
chapters/theory/en_koszul_duality.tex:2947:\index{Sugawara construction!topologization}
chapters/theory/en_koszul_duality.tex:2994:\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
chapters/theory/en_koszul_duality.tex:2995:\label{thm:topologization}
chapters/theory/en_koszul_duality.tex:2997:\index{topologization theorem!statement}
chapters/theory/en_koszul_duality.tex:3010:has the following topologization package.
chapters/theory/en_koszul_duality.tex:3015:  \begin{equation}\label{eq:topologization}
chapters/theory/en_koszul_duality.tex:3061:Conjecture~\textup{\ref{conj:topologization-general}}.
chapters/theory/en_koszul_duality.tex:3132:\label{rem:topologization-inputs}
chapters/theory/en_koszul_duality.tex:3133:\index{topologization theorem!external inputs}
chapters/theory/en_koszul_duality.tex:3169:\begin{remark}[Scope: which algebras admit topologization]
chapters/theory/en_koszul_duality.tex:3170:\label{rem:topologization-scope}

thinking
**Searching for bar construction**

I need to conduct a focused search for bar construction. Instead of using regex, it sounds like fixed-strings might be the way to go. I think I could use `rg -F` for that. I may also need to read about specific regions to ensure I'm getting the right information. This makes me think about how pivotal these details are for a successful search, so I need to pay close attention!
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "BD04" chapters/theory/bar_construction.tex; rg -n -F "Arnold" chapters/theory/bar_construction.tex; rg -n -F "Ran" chapters/theory/bar_construction.tex; rg -n -F "T''^c(s''^{-1}" chapters/theory/bar_construction.tex; rg -n -F "augmentation" chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.
 succeeded in 51ms:
314:framework~\cite[\S3.4]{BD04}:
320:Non-abelian Poincar\'e duality~\cite[\S3.4]{BD04} integrates
323:collision data; the key inputs are~\cite[Theorem~3.4.22, \S3.6]{BD04}
355:The identification follows from \cite{AF15} (for the factorization homology framework) and \cite{BD04} (Section~3.4, for the chiral algebra case). The bar differential $d = d_{\text{int}} + d_{\text{res}} + d_{dR}$ corresponds to the three components of the factorization structure:
373:\cite[Theorem~3.4.9, §§3.4.11--3.4.12]{BD04}.
383:\cite[§§3.4.11--3.4.12]{BD04} together with
387:Chapter~4 of \cite{BD04} uses ``commutative'' for commutative
389:product extends across the diagonal; see \cite[Theorem~4.6.1]{BD04}.
399:\cite[Theorem~4.8.1]{BD04}: on the symmetric side, BD identify chiral
494:The external tensor product $j_*j^*\mathcal{A}^{\boxtimes(n+1)}$ extends $\mathcal{A}^{\boxtimes(n+1)}$ from the open locus of distinct points across collisions, with the OPE controlling the singularity structure (BD~\cite[\S3.4.14--3.4.22]{BD04}).
1019:(Beilinson--Drinfeld~\cite{BD04};
2250:(cf.\ \cite[Theorem~3.7.4]{BD04}, \cite[Theorem~5.1]{Get95}).
2255:Following Beilinson--Drinfeld \cite[§3.7.4, p.228]{BD04}, 
28:Arnold relation makes $d^2 = 0$ at genus~$0$.
66:and proves $\dzero^2 = 0$; the key input is the Arnold relation
249:Arnold relation $\Rightarrow d^2 = 0$ & Quantum master equation \\
274:The Arnold relation $\eta_{ij} \wedge \eta_{jk} + \text{cyc.} = 0$
301:\emph{Arnold relations.}
380:written here as the Arnold relation on logarithmic forms; in BD it is
384:Theorem~\ref{thm:bar-operadic-comparison}; BD do not isolate the Arnold
exec
/bin/zsh -lc "sed -n '168,340p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3160,3275p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{intermediary} between
$\Eone$-chiral and $\Ethree$; the conformal vector is
the bridge. This resolves the apparent paradox of the
dimensional ladder: the $n = 2$ (chiral) and $n = 3$
(Chern--Simons) rows are connected not by an automatic
operadic promotion, but by the physical data of a stress
tensor.
\end{remark}

\begin{remark}[Scope: which algebras admit topologization]
\label{rem:topologization-scope}
\index{topologization theorem!scope}
Theorem~\ref{thm:topologization} is proved for affine
Kac--Moody $V_k(\fg)$ at non-critical level
$k \neq -h^\vee$, where the Sugawara element provides
an explicit inner conformal vector and the $3$d
holomorphic--topological theory is Chern--Simons.
For affine Kac--Moody, the chain-level topologization is
now fully resolved. Three layers are proved:
the cohomological $\Ethree^{\mathrm{top}}$ on BRST
 succeeded in 52ms:
\section{BV formalism for chiral algebras}

\begin{definition}[BV data for a chiral algebra]
\label{def:bv-data-chiral}
\index{antibracket}
\index{BV algebra!data}
Let $\cA$ be a chiral algebra on a smooth curve~$X$.
The BV formalism associates to~$\cA$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Fields}: $\phi \in \mathcal{A}$, sections of the chiral algebra sheaf.
\item \emph{Antifields}: $\phi^+ \in \mathcal{A}^*[1]$, the Serre dual shifted by~$1$.
\item \emph{BV bracket}: $\{\cdot, \cdot\}\colon \mathcal{A} \otimes \mathcal{A}^*[1] \to \mathbb{C}$ of degree~$+1$, an odd Poisson structure.
\item \emph{Action}: $S[\phi, \phi^+]$ satisfying the classical master equation $\{S, S\} = 0$.
\end{enumerate}
\end{definition}

\begin{theorem}[BV complex $=$ geometric bar complex; \ClaimStatusProvedElsewhere{} \cite{CG17}]
\label{thm:bv-bar-geometric}
\index{BV algebra!bar complex identification}
Let $\cA$ be a chiral algebra on $X = \mathbb{P}^1$. The BV complex
exec
/bin/zsh -lc "sed -n '280,415p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{example}[OPE as residue: the Heisenberg current]\label{ex:ope-to-residue}
The Heisenberg current $J(z)$ with OPE $J(z)J(w) = k/(z-w)^2 + \text{reg.}$ gives the bar element $J(z_1) \otimes J(z_2) \otimes \eta_{12} \in \bar{B}^1(\mathcal{H})$, where $\eta_{12} = d\log(z_1 - z_2)$. The bar differential extracts the full chiral product~$\mu$ (Convention~\ref{conv:product-vs-bracket}): since $J_{(0)}J = 0$ (no simple pole) and $J_{(1)}J = k$ (double pole), the result is
\[
d_{\mathrm{res}}(J \otimes J \otimes \eta_{12}) = k \cdot \mathbf{1}.
\]
The entire bar differential comes from the curvature component $d_{\mathrm{curvature}}$ (Proposition~\ref{prop:pole-decomposition}). One must not multiply the OPE pole by the propagator~$\eta_{12}$ and take a combined residue; the logarithmic form accounts for the bar degree, not an additional pole (Computation~\ref{comp:deg1-general}).
\end{example}

\begin{remark}[Logarithmic forms are forced]\label{rem:why-log-forced}
Three requirements distinguish logarithmic forms $\eta_{ij} = d\log(z_i - z_j)$ among meromorphic 1-forms with poles along diagonals, and together determine them uniquely.

\emph{Conformal invariance.}
Under a conformal transformation $z \mapsto f(z)$, a direct computation gives
$d\log(f(z_i) - f(z_j)) = \frac{f'(z_i)dz_i - f'(z_j)dz_j}{f(z_i) - f(z_j)}$,
which near the diagonal $z_i \approx z_j$ reduces to $(dz_i - dz_j)/(z_i - z_j)$
by cancellation of $f'$. Thus $\eta_{ij}$ is conformally invariant up to regular terms.

\emph{Well-defined residues.}
The residue $\operatorname{Res}_{D_{ij}}$ requires a \emph{simple pole} along $D_{ij}$: forms with higher-order poles (e.g.\ $dz_i/(z_i - z_j)^2$) do not admit canonical residues. A logarithmic form $\omega = \frac{df}{f} \wedge \alpha + \beta$ with $f = z_i - z_j$ has $\operatorname{Res}_{D_{ij}}(\omega) = \alpha|_{D_{ij}}$, which is canonical.
exec
/bin/zsh -lc "sed -n '2420,2555p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
package, the BV operator $\Delta_{\mathrm{BV}}$ is the closed-colour
contraction induced by the Swiss-cheese pairing, whereas the bar
differential $d_{\barB}$ is the open-colour coderivation induced by
the chiral product. The two operators therefore come from the same
operadic bar-cobar datum, but they live in different colours. What is
compared is not ``the bar complex as a Swiss-cheese algebra'': the
Swiss-cheese object is the pair
\[
\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\,\cA\bigr),
\]
and the ordered bar complex enters as the open-colour coalgebra model
used to resolve the boundary algebra.

Once one imports the homotopy-Koszulity input recorded in
Remark~\ref{rem:homotopy-koszulity-center}, together with the explicit
description of the Koszul dual cooperad in
Proposition~\ref{prop:sc-koszul-dual-three-sectors} and the center
identification of Theorem~\ref{thm:operadic-center-hochschild}, the
coderived comparison becomes automatic: Livernet's Koszulity theorem
for the classical Swiss-cheese operad, transported to the chiral
exec
/bin/zsh -lc "sed -n '296,380p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4428,4545p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  \textup{(}Costello--Francis--Gwilliam\textup{)}.
\item \textup{(Topological enhancement.)}
  The Sugawara Virasoro element at non-critical level
  upgrades the holomorphic $\Etwo$ to topological $\Etwo$;
  Dunn additivity gives $\Ethree^{\mathrm{top}}$
  \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}.
  At $k = -h^\vee$, the enhancement fails.
\end{enumerate}
\end{theorem}

\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
\label{thm:cfg}
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra.
BV quantisation of Chern--Simons theory on $\RR^3$ with
gauge algebra $\fg$ and coupling $\lambda$ yields
a filtered $\Ethree$-algebra $\cA^\lambda$ on
$C^*(\fg) = \Sym(\fg^\vee[-1])$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Classical observables: $C^*(\fg)$, commutative.
 succeeded in 51ms:
\bibitem{CDG2023}
K. Costello, T. Dimofte, and D. Gaiotto, \emph{Boundary chiral algebras and holomorphic twists}, Comm. Math. Phys. \textbf{399} (2023), no.~2, 1203--1290, arXiv:2005.00083.

\bibitem{CDG2024}
K. Costello, T. Dimofte, and D. Gaiotto, \emph{Line operators and holomorphic-topological field theories}, in preparation, 2024.

\bibitem{CG17}
K. Costello and O. Gwilliam, \emph{Factorization Algebras in Quantum Field Theory}, vols.~1--2, Cambridge University Press, 2017.

\bibitem{CG-vol2}
K. Costello and O. Gwilliam, \emph{Factorization Algebras in Quantum Field Theory, Volume 2}, Cambridge University Press, 2021.

\bibitem{CG97}
N. Chriss and V. Ginzburg, \emph{Representation Theory and Complex Geometry}, Birkh\"auser, 1997.

\bibitem{CL16}
K. Costello and S. Li, \emph{Twisted supergravity and its quantization}, arXiv:1606.00365, 2016.

\bibitem{CL20}
K. Costello and S. Li, \emph{Anomaly cancellation in the topological string}, arXiv:1905.09269, 2019.

thinking
**Searching for reliable sources**

I realize I need direct sources and that local computation notes aren’t sufficient. I want to browse official sources and check places like ArXiv for more credible information. It might make sense to search specific topics or papers individually to ensure that I'm covering all the necessary bases. This should help me gather the most accurate and helpful information for whatever I’m working on!
🌐 Searching the web...
🌐 Searched: Beilinson Drinfeld Chiral Algebras Chapter 3.4 factorization coalgebra Ran space PDF
🌐 Searching the web...
🌐 Searched: site:archive.org Beilinson Drinfeld Chiral Algebras pdf

thinking
**Exploring research sources**

The search results aren't turning out well. I think I should consider using open pages directly from arXiv or DOI instead. I wonder if I could also look into accessible sources like Cambridge previews on CG and BD via Google Books. It seems like targeting specific sections might yield better results. Let me focus on that approach to gather the information effectively!
🌐 Searching the web...
🌐 Searched: "Chiral Algebras" "Ran" "3.4.9"
🌐 Searching the web...
🌐 Searched: https://arxiv.org/abs/2602.12412
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: https://papers.cool/arxiv/2602.12412
🌐 Searching the web...
🌐 Searched: "Beilinson Drinfeld" "Chiral Algebras" pdf ran space factorization coalgebra
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: site:cambridge.org "5.5 Kac-Moody Algebras and Factorization Envelopes" pdf


thinking
**Searching for information sources**

I’m considering ways to find accessible preprints beyond Cambridge. I could check local PDFs or search through repositories, though that might not work out. There's potential to utilize information from volumes via arXiv. For CG, definitions from Costello-Gwilliam on factorization algebras might suffice, particularly chapters 5.4-5.5 that relate to vertex/Kac-Moody theories. I could explore search queries like "cg17 bar complex" and look into local notes for exact theorems.
thinking
**Checking for citations**

I’m thinking I might need to provide an external citation, possibly just citing CG17, since its content is broad enough. It seems important to inspect whether there's already a `\label{rem:costello-gwilliam-factorization}` in the section on bar construction or similar areas. I should definitely search for that detail to make sure I'm covering all bases accurately and providing the necessary references for clarity.
codex
I’ve read the three local lanes. The BD surface is already close to what the literature supports; the CG lane needs a scope-precise confirmation because `MC5` is broader than the genus-0 BV/bar theorem; and the CFG lane already has a strong comparison but it should explicitly say that the agreement is at the derived-center/topologized bulk level, not on the ordered bar itself.
🌐 Searching the web...
🌐 Searched: "Factorization Algebras in Quantum Field Theory" "Kac-Moody Algebras and Factorization Envelopes" pdf

thinking
**Evaluating MC5 scope revisions**

I'm thinking that if there's a discrepancy in the MC5 scope, it might be useful to add a remark in `bv_brst.tex` or near the theorem in `editorial_constitution`. I should check around the relevant lines in `editorial_constitution.tex` to see if the scope is already stated. Since the user asked about whether our BV/bar (MC5) agrees with CG's BV quantization, adding a remark there could clarify things. I really need to read the local region around the conjecture too.
exec
/bin/zsh -lc "sed -n '420,490p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Literature confirmation|CG17|BD04|CFG25|CFG26" chapters/theory/bar_construction.tex chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "rem:costello-gwilliam-factorization|rem:bd-comparison-bar|thm:bv-bar-geometric|thm:cfg|rem:topologization-scope" metadata/theorem_registry.md chapters/theory/bar_construction.tex chapters/connections/bv_brst.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
datum. On the spectral vector-line locus,
Corollary~\ref{thm:yangian-canonical-realization-plus-vector-line}
closes DK-4/DK-5 on the canonical target; on the sharper equivariant
multiplicative spectral realization locus,
Corollary~\ref{thm:yangian-canonical-realization-plus-one-seed}
contracts this to the single canonical spectral seed
$V^\omega(0)=J_q^\omega(V(0))$.
Corollary~\ref{thm:yangian-formal-moduli-plus-core-realization}
reduces the remaining categorical step to compact-core realization of
a chosen finite-dimensional factorization DK pair. The full
Yangian reduction chain is detailed in \S\ref{sec:infty-cat-factorization-kd}.
\end{remark}

\begin{conjecture}[BV/BRST/bar identification]
\label{conj:v1-master-bv-brst}
\ClaimStatusConjectured{}
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.

 succeeded in 50ms:
chapters/theory/bar_construction.tex:68:Remark~\ref{rem:costello-gwilliam-factorization}).
chapters/theory/bar_construction.tex:262:\label{rem:costello-gwilliam-factorization}
chapters/theory/bar_construction.tex:364:\begin{remark}[BD comparison]\label{rem:bd-comparison-bar}
chapters/theory/bar_construction.tex:2161:(Remark~\ref{rem:costello-gwilliam-factorization}); the bar
chapters/theory/en_koszul_duality.tex:3170:\label{rem:topologization-scope}
chapters/theory/en_koszul_duality.tex:4372:(Theorem~\ref{thm:cfg}).
chapters/theory/en_koszul_duality.tex:4439:\label{thm:cfg}
chapters/theory/en_koszul_duality.tex:4507:  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
chapters/theory/en_koszul_duality.tex:4631:(Theorem~\ref{thm:cfg}). Both are parametrised by
chapters/theory/en_koszul_duality.tex:4648:Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
chapters/theory/en_koszul_duality.tex:4713:Theorem~\ref{thm:cfg}(iv) respectively).
chapters/theory/en_koszul_duality.tex:5382:(Theorem~\ref{thm:cfg}(iv)). The generator of
chapters/theory/en_koszul_duality.tex:5406:(Theorem~\ref{thm:cfg}(iv));
chapters/theory/en_koszul_duality.tex:6241:Theorem~\textup{\ref{thm:cfg}}, where the CFG coupling
chapters/theory/en_koszul_duality.tex:6365:(Theorem~\ref{thm:cfg}(i)).
chapters/theory/en_koszul_duality.tex:6390:(Theorem~\ref{thm:cfg}(ii)).
chapters/theory/en_koszul_duality.tex:6401:Theorem~\ref{thm:cfg}(iv) respectively). Since the
chapters/connections/bv_brst.tex:83: \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
chapters/connections/bv_brst.tex:96:Item~\textup{(i)} is Theorem~\ref{thm:bv-bar-geometric}. The scalar
chapters/connections/bv_brst.tex:185:\label{thm:bv-bar-geometric}
 succeeded in 50ms:
chapters/theory/bar_construction.tex:232:(Costello--Gwilliam~\cite{CG17}), a chiral algebra~$\cA$ determines a
chapters/theory/bar_construction.tex:268:Costello--Gwilliam~\cite{CG17} restricted to codimension-$1$
chapters/theory/bar_construction.tex:314:framework~\cite[\S3.4]{BD04}:
chapters/theory/bar_construction.tex:320:Non-abelian Poincar\'e duality~\cite[\S3.4]{BD04} integrates
chapters/theory/bar_construction.tex:323:collision data; the key inputs are~\cite[Theorem~3.4.22, \S3.6]{BD04}
chapters/theory/bar_construction.tex:355:The identification follows from \cite{AF15} (for the factorization homology framework) and \cite{BD04} (Section~3.4, for the chiral algebra case). The bar differential $d = d_{\text{int}} + d_{\text{res}} + d_{dR}$ corresponds to the three components of the factorization structure:
chapters/theory/bar_construction.tex:373:\cite[Theorem~3.4.9, §§3.4.11--3.4.12]{BD04}.
chapters/theory/bar_construction.tex:383:\cite[§§3.4.11--3.4.12]{BD04} together with
chapters/theory/bar_construction.tex:387:Chapter~4 of \cite{BD04} uses ``commutative'' for commutative
chapters/theory/bar_construction.tex:389:product extends across the diagonal; see \cite[Theorem~4.6.1]{BD04}.
chapters/theory/bar_construction.tex:399:\cite[Theorem~4.8.1]{BD04}: on the symmetric side, BD identify chiral
chapters/theory/bar_construction.tex:494:The external tensor product $j_*j^*\mathcal{A}^{\boxtimes(n+1)}$ extends $\mathcal{A}^{\boxtimes(n+1)}$ from the open locus of distinct points across collisions, with the OPE controlling the singularity structure (BD~\cite[\S3.4.14--3.4.22]{BD04}).
chapters/theory/bar_construction.tex:1019:(Beilinson--Drinfeld~\cite{BD04};
chapters/theory/bar_construction.tex:2159:Costello--Gwilliam framework~\cite[\S5.4]{CG17}: the bar
chapters/theory/bar_construction.tex:2250:(cf.\ \cite[Theorem~3.7.4]{BD04}, \cite[Theorem~5.1]{Get95}).
chapters/theory/bar_construction.tex:2255:Following Beilinson--Drinfeld \cite[§3.7.4, p.228]{BD04}, 
chapters/theory/en_koszul_duality.tex:3229:Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
chapters/theory/en_koszul_duality.tex:4172:  $D^{\mathrm{co}}$}. Costello--Gwilliam~\cite{CG17}
chapters/theory/en_koszul_duality.tex:4251:  \textup{(}Costello--Gwilliam~\cite{CG17}\textup{)}.
chapters/theory/en_koszul_duality.tex:4289:constructed in~\cite{CG17} and~\cite{CG-vol2}. The product
exec
/bin/zsh -lc "sed -n '248,285p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Logarithmic form $\eta_{ij}$ & Propagator \\
Arnold relation $\Rightarrow d^2 = 0$ & Quantum master equation \\
Bar cohomology $H^*(\bar{B}(\cA))$ & Physical observables \\
Curvature $m_0$ (Chapter~\ref{chap:higher-genus}) & Conformal anomaly
\end{tabular}
\end{center}
\noindent
This is not an analogy; it is Theorem~\ref{thm:brst-bar-genus0}.
The algebraic-geometric side comes first because it admits complete
proofs; the physical identifications follow as theorems, not
heuristics.
\end{remark}

\begin{remark}[Holomorphic factorization on $\FM_k(X)$]
\label{rem:costello-gwilliam-factorization}
\index{Costello--Gwilliam!factorization algebra}%
\index{bar differential!as factorization structure}%
The bar differential $d_{\mathrm{res}}$, constructed from OPE
residues along collision divisors in $\overline{\Conf}_{k}(X)$,
is the factorization algebra structure of

thinking
**Investigating literature confirmations**

I’m considering adding literature confirmation after the rem:bd-comparison-bar or perhaps after the Costello-Gwilliam factorization. I should also explicitly mention augmentation and the Ran/Arnold aspect. It makes sense to see if there’s a conjecture or theorem about BRST/bar and coderived, specifically looking at theorem thm:bv-bar-coderived. I might also need literature confirmation around the genus-0 theorem or coderived theorem in bv_brst. It's all about locating that information and reviewing the lines.
exec
/bin/zsh -lc "sed -n '2260,2365p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:bv-bar-coderived|Coderived|coderived" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Theta_\cA$ in the convolution algebra.
For class~$\mathsf{G}$ and class~$\mathsf{L}$
\textup{(}shadow depth $r_{\max} \leq 3$\textup{)},
$S_4(\cA) = 0$ and thus $c_4(\cA) = 0$.
For class~$\mathsf{M}$ \textup{(}Virasoro\textup{)},
$S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$
at generic~$c$, confirming that the quartic harmonic
discrepancy is nontrivial.

\emph{Step~5: Class-by-class vanishing.}
For class~$\mathsf{G}$: no interaction vertices at
any degree, so $c_r(\cA) = 0$ for all $r \geq 2$.
For class~$\mathsf{L}$: shadow depth $r_{\max} = 3$
implies $c_r(\cA) = 0$ for $r \geq 4$
\textup{(}no interaction vertex exists at degree
$\geq 4$\textup{)}, and Jacobi kills $c_3$.
For class~$\mathsf{M}$: the shadow tower does not
terminate \textup{(}Corollary~\ref{cor:virasoro-postnikov-nontermination}\textup{)},
so $c_r(\cA)$ is generically nonzero for $r \geq 4$.
The factorization through $m_0^{\lfloor r/2 \rfloor - 1}$
 succeeded in 51ms:
32:all-genera coderived comparison of
33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
1855:Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
1863:curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
1864:class~$\mathsf{M}$ BV and bar models in the coderived category even
1902: & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
1911:powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
2287:\begin{theorem}[BV$=$bar in the coderived category;
2289:\label{thm:bv-bar-coderived}%
2290:\index{BV algebra!bar complex identification!coderived category|textbf}%
2291:\index{coderived category!BV/bar identification|textbf}%
2372:becomes an isomorphism in the coderived quotient
2379:of Definition~\ref{def:coderived-fact}. This is the required
2380:coderived comparison. The provisional localization is not needed
2384:\begin{remark}[Harmonic mechanism behind the coderived comparison]
2385:\label{rem:bv-bar-coderived-higher-genus}%
2386:\index{coderived category!higher-genus validity}%
2391:Theorem~\ref{thm:bv-bar-coderived}. The proof has two inputs:
2409:\label{rem:bv-bar-coderived-operadic}%
2413:Theorem~\ref{thm:bv-bar-coderived}. By

thinking
**Exploring BV Quantization**

I’m considering if the theorem for MC5 is indeed a local theorem. The user asked if our BV/bar for MC5 aligns with CG's BV quantization, noting that the theorem goes beyond CG. I think I need to clarify literature confirmation and the theorem's scope, particularly for genus-0 and higher genus. I might look for book reviews or chapter summaries on boundary chiral observables, and also check accessible online notes by Costello and Gwilliam.
🌐 Searching the web...
🌐 Searched: "Costello Gwilliam" "5.4 Free beta-gamma system" "vertex algebra"

thinking
**Exploring chapter content**

I noticed that my search returned a chapter summary instead of the full text. Perhaps I could look at the chapter pages for headings or specific lines? Searching within could be useful. I might also consider using Cambridge pages for metadata, even if I can't access the complete text. It could be helpful to search for specific phrases, like "Kac-Moody algebras and factorization envelopes,” to find relevant excerpts or information.
🌐 Searching the web...
🌐 Searched: "Kac-Moody algebras and factorization envelopes"

thinking
**Searching for theories**

I’m looking into possible search results for the general factorization envelope of Kac-Moody and holomorphic field theories. BV quantization might not be included exactly, but searching terms like "divergence complex" or "quantum observables" could help. Volume 2 might have useful content, but it's not necessary since the local file cites CG17's genus-0 theorem. I’ll check for accessible arXiv PDFs, possibly opening abstracts to find a theorem summary. Let’s go ahead and search!
🌐 Searching the web...
🌐 Searched: "2602.12412" theorem 1.4
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: https://papers.cool/arxiv/2602.12412
🌐 Searching the web...
🌐 Searched: https://papers.cool/arxiv/2602.12412
🌐 Searching the web...
🌐 Searched: "Theorem 3.4.9" "Chiral Algebras"
🌐 Searching the web...
🌐 Searched: site:math.uchicago.edu/~drinfeld/langlands/chiral cha_ch3.pdf
🌐 Searching the web...
🌐 Searched: https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf

thinking
**Searching within PDF**

Okay, I need to find specific lines, like 3.4.11 and 3.4.9, in the PDF. I’m thinking of using the "find" feature to make this easier. That way, I can quickly locate the lines I need without having to scroll through the entire document. It's a straightforward plan, but I want to make sure I’m thorough about the search, so I get all the right references. Let’s get started!
🌐 Searching the web...
🌐 Searched: '3.4.9' in https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf
🌐 Searching the web...
🌐 Searched: https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf

thinking
**Searching for definitions and theorems**

I need to find the definition for 3.4.4 factorization. Also, I think I should look at Chapter 4 for the 4.8.1 chiral homology. I need the details of Theorem 4.8.1, which might be in the Chapter 4 PDF. So, I'll search for it and open the lines surrounding that theorem. It seems like a good starting point to gather the information I need!
🌐 Searching the web...
🌐 Searched: https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch4.pdf
🌐 Searching the web...
🌐 Searched: '4.8.1' in https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch4.pdf
🌐 Searching the web...
🌐 Searched: "Holomorphic field theories and vertex algebras" pdf Costello Gwilliam filetype:pdf

thinking
**Considering citations and edits**

I’m thinking about how to cite the chapter summary page and frontmatter contents. For the BV quantization scope, I'm not sure. I might search for Costello's paper on supersymmetric and holomorphic field theories, since it could mention relevant concepts like holomorphic factorization. 

I’ll need to do some literature cross-checking in the repo and inspect the current work before editing. Checking the git status seems smart, and I should add commentary before I make any changes.
codex
I have enough evidence to patch now. The changes will be three short confirmation remarks: BD in `bar_construction.tex`, CG in the BV/MC5 lane with an explicit scope boundary, and CFG in the topologization/derived-center lane stating the precise overlap and the non-overlap.
exec
/bin/zsh -lc "sed -n '220,260p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '360,410p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4460,4538p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
normal-crossing divisors of the smooth
variety~$\overline{C}_{n+1}(X)$: the residue map
$\Res_{D_{ij}}\colon \Omega^k_{\log}(\overline{C}_{n+1})
\to \Omega^{k-1}_{D_{ij}}$ is an algebraic morphism of sheaves
on a smooth variety. The factor $1/(z_i - z_k)$ is a pole along
the transverse divisor $D_{ik}$ (Theorem~\ref{thm:FM}(3):
$D_{ij} \cap D_{ik}$ has normal crossings), so on~$D_{ij}$
it restricts to a regular meromorphic function with poles only
along~$D_{ij} \cap D_{ik}$, a codimension-$2$ stratum.
The FM compactification resolves all coincidence singularities
into normal-crossing divisors, and the log-de~Rham complex on
this resolution is the correct algebraic framework: it replaces
distributional regularization with algebraic residues.

The logarithmic $1$-forms $\eta_{ij} = d\log(z_i - z_j)$ generate
$H^1(C_n(X); \mathbb{C})$ by the Arnold--Brieskorn theorem;
for $X = \mathbb{C}$, all $\binom{n}{2}$ classes are linearly independent in degree~$1$
(the Arnold relations constrain products in degree~$\geq 2$), giving
$\dim H^1(C_n(\mathbb{C})) = \binom{n}{2}$. (For a curve of genus~$g > 0$, additional generators from $H^1(X)$ contribute $2gn$ classes.)

 succeeded in 52ms:
\end{itemize}
The key verification is that Weiss covers of $C_n(X)$ compute factorization homology (\cite{AF15}, Theorem~5.1), and the FM compactification provides a canonical system of Weiss covers whose \v{C}ech complex is precisely the bar complex (Definition~\ref{def:weiss-cover}).
\end{proof}

\begin{remark}[BD comparison]\label{rem:bd-comparison-bar}
The comparison with Beilinson--Drinfeld is on the symmetric bar
$\barB_X(\cA)$ on $\Ran(X)$, not on the ordered tensor coalgebra
$B_X^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$. The ordered object is an
$\Eone$ refinement that keeps the ordered collision data and the
$R$-matrix; BD's Ran-space formalism is permutation-invariant from the
start. Passing from $B_X^{\mathrm{ord}}(\cA)$ to $\barB_X(\cA)$ is the
convention bridge from the ordered presentation used in this monograph
to the symmetric factorization-coalgebra formalism of
\cite[Theorem~3.4.9, §§3.4.11--3.4.12]{BD04}.

At genus~$0$, the differential
$d_{\mathrm{internal}} + d_{\mathrm{residue}} + d_{\mathrm{de\,Rham}}$
is the Fulton--MacPherson/logarithmic-form model for the same Cousin
differential that Beilinson--Drinfeld define abstractly on the Ran
stratification. The codimension-two compatibility forcing $d^2 = 0$ is
 succeeded in 52ms:
\end{enumerate}
\end{theorem}

\begin{remark}[CFG comparison]
\index{Costello--Francis--Gwilliam!comparison with present topologization}%
\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
meet on the affine Kac--Moody formal-disk lane, but they start from
different primitive objects. Their deformation parameter is the
Chern--Simons coupling $\lambda$; ours is the departure from critical
level $k + h^\vee$. The comparison splits into four checks.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Does the CFG $\Ethree$ match ours?)}
  On the CFG side, BV quantization produces a factorization algebra of
  filtered dg modules on $\RR^3$, and local constancy upgrades the
  local quantum observables to a filtered $\Ethree$-algebra
  \textup{(}\cite[Theorem~1.2]{CFG25},
  \cite[Proposition~4.6]{CFG25},
  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
  not the ordered bar coalgebra but the derived chiral center after
 succeeded in 51ms:
 M appendices/ordered_associative_chiral_kd.tex
 M bibliography/references.tex
 M chapters/connections/outlook.tex
 M chapters/theory/chiral_hochschild_koszul.tex
 M chapters/theory/chiral_koszul_pairs.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/ordered_associative_chiral_kd.tex
 M compute/lib/depth_classification.py
 M compute/lib/koszul_conductor_table_engine.py
 M compute/tests/test_depth_classification.py
 M compute/tests/test_koszul_conductor_table_engine.py
 M standalone/ordered_chiral_homology.tex
 M standalone/references.bib
?? compute/lib/sl2_chiral_bar_dims.py
?? compute/tests/test_sl2_chiral_bar_dims.py
?? elite_rescue_20260413_221642/L06_EF_comparison.md
?? elite_rescue_20260413_221642/L07_KS_comparison.md
?? elite_rescue_20260413_221642/L08_Livernet_comparison.md

thinking
**Searching for algebra terms**

I could look up book pages or chapter titles for more context. To verify genus-0 BV/bar identification, I might use local theorems suggesting it’s in CG17. I wonder if I should create a search query for the exact phrases “vertex algebras” and “factorization algebras.” That could help narrow down results and give me a clearer picture of what I need! Let’s see what the web has to offer on these terms.
🌐 Searching the web...
🌐 Searched: "Costello Gwilliam" factorization algebras in quantum field theory vertex algebras observables holomorphic field theories pdf
🌐 Searching the web...
🌐 Searched: https://www.cambridge.org/core/books/factorization-algebras-in-quantum-field-theory/holomorphic-field-theories-and-vertex-algebras/A43983CCDB45278C425DAB8E9E4999FB

thinking
**Looking for summaries**

I’m noticing that the contents beyond line 444 in this book might not be very helpful. I wonder if I should check further down the page for a chapter summary. That could make things clearer! I’ll keep an eye out for anything labeled as "Summary," since that might provide the concise information I need. It’s often easier to grasp key points that way. Let’s see what I can find!
🌐 Searching the web...
🌐 Searched: 'Summary' in https://www.cambridge.org/core/books/factorization-algebras-in-quantum-field-theory/holomorphic-field-theories-and-vertex-algebras/A43983CCDB45278C425DAB8E9E4999FB
🌐 Searching the web...
🌐 Searched: "Free beta-gamma system" "Costello Gwilliam" factorization algebra
🌐 Searching the web...
🌐 Searched: "Chern-Simons factorization algebras and knot polynomials" arxiv abstract E3 local observables
🌐 Searching the web...
🌐 Searched: https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/8/48667/files/2025/10/CS_tangle_TFT-2.pdf

thinking
**Exploring factorization algebras**

I'm looking into the connection between CFG and CG. It seems like the CFG intro cites CG in the section around lines 236-274, which describes factorization algebras of observables and locally constant factorization algebras on R^3. That's a good find! I might also want to verify CG and CFG using the same source and check out the surrounding lines around theorem 1.4 and remark 6. I should search in the PDF for more details.
🌐 Searching the web...
🌐 Searched: 'Theorem 1.4' in https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/8/48667/files/2025/10/CS_tangle_TFT-2.pdf
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf
🌐 Searching the web...
🌐 Searched: 'Theorem 3.4.9' in https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf
🌐 Searching the web...
🌐 Searched: '4.8.1' in https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch4.pdf

thinking
**Searching for quantization resources**

I'm realizing this confirms the use of the kernel of augmentation morphism U(L)→ω from theorem 4.8.1. That's great! I think I might need to incorporate actual CG or perhaps reference CFG lines that relate to CG. For MC5, using the CFG PDF and other sources could be enough. Also, I could search Williams' paper for effective BV quantization on Riemann surfaces. Maybe I should search for "effective BV quantization" to find more relevant lines!
🌐 Searching the web...
🌐 Searched: https://brianrwilliams.github.io/papers/vir.pdf

thinking
**Reviewing bibliography details**

I see that there's an existing remark, and I’m thinking a new short remark could work, too. I’m wondering if I should fix the inconsistencies in CFG25/CFG26 bibliography. Right now, the current file only mentions CFG25, and the bibliography reflects that. So, there's some confusion because earlier, it seemed to reference CFG26. I think I need to include some absolute sources in my remarks, possibly citing BD04, CG17, and CFG25.
codex
I’m patching three local remarks now. I’m not touching the existing theorem/status surfaces, only recording the literature verdicts and the exact scope boundary where the overlap ends.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -405,2 +405,33 @@
 
+\begin{remark}[Literature confirmation: Beilinson--Drinfeld]
+The present bar construction agrees with the Beilinson--Drinfeld
+factorization-coalgebra formalism at the symmetric level. Three points
+match exactly.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Augmentation.)} The reduced bar used here,
+  $T^c(s^{-1}\bar\cA)$ with $\bar\cA = \ker(\varepsilon)$, is the
+  ordered refinement of the augmented symmetric object that appears in
+  BD. On the BD side, the augmentation ideal enters through the kernel
+  of the augmentation morphism for the chiral envelope in
+  \cite[Theorem~4.8.1]{BD04}; our ordered bar keeps that reduced input
+  before passing to $\Sigma_n$-coinvariants.
+\item \textup{(Ran space and factorization.)} BD's principal theorem in
+  \cite[Theorem~3.4.9]{BD04} identifies factorization algebras with
+  chiral algebras on the Ran space, and the explicit factorization
+  compatibility in \cite[(3.4.11.5)]{BD04} is the symmetric counterpart
+  of our descent from $B_X^{\mathrm{ord}}(\cA)$ to $\barB_X(\cA)$ on
+  $\Ran(X)$.
+\item \textup{(Arnold relation.)} The codimension-two compatibility that
+  BD package inside the Cousin/factorization differential
+  \textup{(}\cite[(3.4.11.4)--(3.4.11.5), Lemma~3.4.12]{BD04}\textup{)}
+  is the same nilpotence mechanism written here in logarithmic-form
+  language as the Arnold relation. This is a reformulation, not a new
+  differential.
+\end{enumerate}
+Hence there is no discrepancy with BD: our bar complex is an
+$\Eone$-ordered lift of the BD symmetric factorization coalgebra, with
+the same augmentation, the same Ran-space output, and the same
+genus-$0$ square-zero relation after translating conventions.
+\end{remark}
+
 \begin{remark}[The nilpotence-periodicity correspondence]
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -246,2 +246,23 @@
 
+\begin{remark}[Literature confirmation: Costello--Gwilliam]
+The genus-$0$ BV/bar identification used in this chapter is consistent
+with the Costello--Gwilliam BV formalism. In the CG framework, a
+perturbative quantum field theory determines a factorization algebra of
+observables, and for holomorphic theories this is the source of the
+vertex-algebra structure treated in Chapter~5 of~\cite{CG17}. Our
+Theorem~\ref{thm:bv-bar-geometric} is the chiral-bar model of that same
+local observable package on $X=\mathbb{P}^1$: the BV differential is
+the genus-$0$ bar differential, and collision residues are the
+factorization products written in logarithmic-form language.
+
+There is also no scope mismatch once MC5 is stated carefully. CG supply
+the BV quantization and factorization-observable formalism; the present
+manuscript adds the bar-side genus expansion, harmonic comparison, and
+coderived package. Thus the exact overlap with~\cite{CG17} is the
+genus-$0$ local comparison and the general BV/factorization dictionary,
+while the all-genera coderived theorem
+\textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)} is our extension,
+not a theorem attributed to CG.
+\end{remark}
+
 \subsection{Quantum master equation}
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -4537,2 +4537,24 @@
 
+\begin{remark}[Literature confirmation: CFG]
+There is no discrepancy with
+Costello--Francis--Gwilliam~\cite{CFG25} once the object boundary is
+kept fixed. CFG construct a filtered $\Ethree$-algebra from BV
+quantization of bulk Chern--Simons observables on~$\RR^3$; our
+topologization theorem constructs the corresponding $\Ethree$ structure
+on the \emph{derived chiral center} after passing through the boundary
+chiral algebra and then topologizing it. These are two routes to the
+same affine Kac--Moody bulk object on the formal-disk lane, not two
+competing structures on the ordered bar complex.
+
+The overlap is therefore exact at the derived-center level and only
+there: CFG's $\Ethree$ agrees with our
+$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+formal-disk restriction, while the ordered bar complex remains the
+$\Eone$ boundary resolution used to compute that center. The only
+remaining difference is methodological. CFG obtain the chain-level
+$\Ethree$ from bulk local constancy ab initio; our chapter isolates the
+extra boundary-side coherence problem needed to lift the transferred
+model back to the original BRST complex.
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index bcae5ed97f62b216144592596b8851b6e8425a75..c256ac561c9ee037692b3698070e5c83110851c5
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -244,6 +244,27 @@
 \[d = d_{\text{strat}} + d_{\text{int}} + d_{\text{res}}\]
 \end{proof}
 
+\begin{remark}[Literature confirmation: Costello--Gwilliam]
+The genus-$0$ BV/bar identification used in this chapter is consistent
+with the Costello--Gwilliam BV formalism. In the CG framework, a
+perturbative quantum field theory determines a factorization algebra of
+observables, and for holomorphic theories this is the source of the
+vertex-algebra structure treated in Chapter~5 of~\cite{CG17}. Our
+Theorem~\ref{thm:bv-bar-geometric} is the chiral-bar model of that same
+local observable package on $X=\mathbb{P}^1$: the BV differential is
+the genus-$0$ bar differential, and collision residues are the
+factorization products written in logarithmic-form language.
+
+There is also no scope mismatch once MC5 is stated carefully. CG supply
+the BV quantization and factorization-observable formalism; the present
+manuscript adds the bar-side genus expansion, harmonic comparison, and
+coderived package. Thus the exact overlap with~\cite{CG17} is the
+genus-$0$ local comparison and the general BV/factorization dictionary,
+while the all-genera coderived theorem
+\textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)} is our extension,
+not a theorem attributed to CG.
+\end{remark}
+
 \subsection{Quantum master equation}
 
 \begin{definition}[BV Laplacian]
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index c9e9b299105e9dea7b96d7ba1fcdf657e2c76e89..e09f6765a43673e9af3fa087f6cd5598c04594d2
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -403,6 +403,37 @@
 bar-cobar inversion.
 \end{remark}
 
+\begin{remark}[Literature confirmation: Beilinson--Drinfeld]
+The present bar construction agrees with the Beilinson--Drinfeld
+factorization-coalgebra formalism at the symmetric level. Three points
+match exactly.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Augmentation.)} The reduced bar used here,
+  $T^c(s^{-1}\bar\cA)$ with $\bar\cA = \ker(\varepsilon)$, is the
+  ordered refinement of the augmented symmetric object that appears in
+  BD. On the BD side, the augmentation ideal enters through the kernel
+  of the augmentation morphism for the chiral envelope in
+  \cite[Theorem~4.8.1]{BD04}; our ordered bar keeps that reduced input
+  before passing to $\Sigma_n$-coinvariants.
+\item \textup{(Ran space and factorization.)} BD's principal theorem in
+  \cite[Theorem~3.4.9]{BD04} identifies factorization algebras with
+  chiral algebras on the Ran space, and the explicit factorization
+  compatibility in \cite[(3.4.11.5)]{BD04} is the symmetric counterpart
+  of our descent from $B_X^{\mathrm{ord}}(\cA)$ to $\barB_X(\cA)$ on
+  $\Ran(X)$.
+\item \textup{(Arnold relation.)} The codimension-two compatibility that
+  BD package inside the Cousin/factorization differential
+  \textup{(}\cite[(3.4.11.4)--(3.4.11.5), Lemma~3.4.12]{BD04}\textup{)}
+  is the same nilpotence mechanism written here in logarithmic-form
+  language as the Arnold relation. This is a reformulation, not a new
+  differential.
+\end{enumerate}
+Hence there is no discrepancy with BD: our bar complex is an
+$\Eone$-ordered lift of the BD symmetric factorization coalgebra, with
+the same augmentation, the same Ran-space output, and the same
+genus-$0$ square-zero relation after translating conventions.
+\end{remark}
+
 \begin{remark}[The nilpotence-periodicity correspondence]
 \label{rem:nilpotence-periodicity}
 \index{nilpotence-periodicity correspondence|textbf}
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index e24ea9921ec6d4fac794d184e86cd41de71b34c7..b297fbdcf21f174d5ab2f3e924e956bf5078986a
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4535,6 +4535,28 @@
 \end{enumerate}
 \end{remark}
 
+\begin{remark}[Literature confirmation: CFG]
+There is no discrepancy with
+Costello--Francis--Gwilliam~\cite{CFG25} once the object boundary is
+kept fixed. CFG construct a filtered $\Ethree$-algebra from BV
+quantization of bulk Chern--Simons observables on~$\RR^3$; our
+topologization theorem constructs the corresponding $\Ethree$ structure
+on the \emph{derived chiral center} after passing through the boundary
+chiral algebra and then topologizing it. These are two routes to the
+same affine Kac--Moody bulk object on the formal-disk lane, not two
+competing structures on the ordered bar complex.
+
+The overlap is therefore exact at the derived-center level and only
+there: CFG's $\Ethree$ agrees with our
+$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+formal-disk restriction, while the ordered bar complex remains the
+$\Eone$ boundary resolution used to compute that center. The only
+remaining difference is methodological. CFG obtain the chain-level
+$\Ethree$ from bulk local constancy ab initio; our chapter isolates the
+extra boundary-side coherence problem needed to lift the transferred
+model back to the original BRST complex.
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index bcae5ed97f62b216144592596b8851b6e8425a75..c256ac561c9ee037692b3698070e5c83110851c5
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -244,6 +244,27 @@
 \[d = d_{\text{strat}} + d_{\text{int}} + d_{\text{res}}\]
 \end{proof}
 
+\begin{remark}[Literature confirmation: Costello--Gwilliam]
+The genus-$0$ BV/bar identification used in this chapter is consistent
+with the Costello--Gwilliam BV formalism. In the CG framework, a
+perturbative quantum field theory determines a factorization algebra of
+observables, and for holomorphic theories this is the source of the
+vertex-algebra structure treated in Chapter~5 of~\cite{CG17}. Our
+Theorem~\ref{thm:bv-bar-geometric} is the chiral-bar model of that same
+local observable package on $X=\mathbb{P}^1$: the BV differential is
+the genus-$0$ bar differential, and collision residues are the
+factorization products written in logarithmic-form language.
+
+There is also no scope mismatch once MC5 is stated carefully. CG supply
+the BV quantization and factorization-observable formalism; the present
+manuscript adds the bar-side genus expansion, harmonic comparison, and
+coderived package. Thus the exact overlap with~\cite{CG17} is the
+genus-$0$ local comparison and the general BV/factorization dictionary,
+while the all-genera coderived theorem
+\textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)} is our extension,
+not a theorem attributed to CG.
+\end{remark}
+
 \subsection{Quantum master equation}
 
 \begin{definition}[BV Laplacian]
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index c9e9b299105e9dea7b96d7ba1fcdf657e2c76e89..e09f6765a43673e9af3fa087f6cd5598c04594d2
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -403,6 +403,37 @@
 bar-cobar inversion.
 \end{remark}
 
+\begin{remark}[Literature confirmation: Beilinson--Drinfeld]
+The present bar construction agrees with the Beilinson--Drinfeld
+factorization-coalgebra formalism at the symmetric level. Three points
+match exactly.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Augmentation.)} The reduced bar used here,
+  $T^c(s^{-1}\bar\cA)$ with $\bar\cA = \ker(\varepsilon)$, is the
+  ordered refinement of the augmented symmetric object that appears in
+  BD. On the BD side, the augmentation ideal enters through the kernel
+  of the augmentation morphism for the chiral envelope in
+  \cite[Theorem~4.8.1]{BD04}; our ordered bar keeps that reduced input
+  before passing to $\Sigma_n$-coinvariants.
+\item \textup{(Ran space and factorization.)} BD's principal theorem in
+  \cite[Theorem~3.4.9]{BD04} identifies factorization algebras with
+  chiral algebras on the Ran space, and the explicit factorization
+  compatibility in \cite[(3.4.11.5)]{BD04} is the symmetric counterpart
+  of our descent from $B_X^{\mathrm{ord}}(\cA)$ to $\barB_X(\cA)$ on
+  $\Ran(X)$.
+\item \textup{(Arnold relation.)} The codimension-two compatibility that
+  BD package inside the Cousin/factorization differential
+  \textup{(}\cite[(3.4.11.4)--(3.4.11.5), Lemma~3.4.12]{BD04}\textup{)}
+  is the same nilpotence mechanism written here in logarithmic-form
+  language as the Arnold relation. This is a reformulation, not a new
+  differential.
+\end{enumerate}
+Hence there is no discrepancy with BD: our bar complex is an
+$\Eone$-ordered lift of the BD symmetric factorization coalgebra, with
+the same augmentation, the same Ran-space output, and the same
+genus-$0$ square-zero relation after translating conventions.
+\end{remark}
+
 \begin{remark}[The nilpotence-periodicity correspondence]
 \label{rem:nilpotence-periodicity}
 \index{nilpotence-periodicity correspondence|textbf}
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index e24ea9921ec6d4fac794d184e86cd41de71b34c7..b297fbdcf21f174d5ab2f3e924e956bf5078986a
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4535,6 +4535,28 @@
 \end{enumerate}
 \end{remark}
 
+\begin{remark}[Literature confirmation: CFG]
+There is no discrepancy with
+Costello--Francis--Gwilliam~\cite{CFG25} once the object boundary is
+kept fixed. CFG construct a filtered $\Ethree$-algebra from BV
+quantization of bulk Chern--Simons observables on~$\RR^3$; our
+topologization theorem constructs the corresponding $\Ethree$ structure
+on the \emph{derived chiral center} after passing through the boundary
+chiral algebra and then topologizing it. These are two routes to the
+same affine Kac--Moody bulk object on the formal-disk lane, not two
+competing structures on the ordered bar complex.
+
+The overlap is therefore exact at the derived-center level and only
+there: CFG's $\Ethree$ agrees with our
+$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+formal-disk restriction, while the ordered bar complex remains the
+$\Eone$ boundary resolution used to compute that center. The only
+remaining difference is methodological. CFG obtain the chain-level
+$\Ethree$ from bulk local constancy ab initio; our chapter isolates the
+extra boundary-side coherence problem needed to lift the transferred
+model back to the original BRST complex.
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Apr 16th, 2026 11:00 PM.
tokens used
256,938
