# S14_standalone_to_main (961s)

- [CRITICAL] chapters/connections/genus1_seven_faces.tex:473 — PROBLEM: Face~5 uses `k/(k+h^\vee)` in `r_{\widehat{\fg}_k}^{(1)}(z,\tau)`, but the seam does not support that normalization: the standalone paper has `1/(k+h^\vee)` at `standalone/genus1_seven_faces.tex:435`, and the same chapter later degenerates to `\Omega/((k+h^\vee)z)` at `chapters/connections/genus1_seven_faces.tex:976`. FIX: change `k/(k+h^\vee)` to `1/(k+h^\vee)` here and at the repeated restatements `chapters/connections/genus1_seven_faces.tex:864` and `:892`, then add one explicit bridge sentence that `chapters/examples/yangians_drinfeld_kohno.tex:7271-7278` is the trace-form presentation of the same residue.

- [CRITICAL] standalone/analytic_sewing.tex:2822 — PROBLEM: `def:analytic-koszul-pair` is stale and self-contradictory at the seam. The standalone defines an analytic Koszul pair by already having the Quillen equivalence `\barB^{an} \dashv \Omega^{an}` on sewing-complete categories, then immediately restates that same equivalence as conjecture `conj:analytic-realisation` at `standalone/analytic_sewing.tex:2844-2849`. The main chapter no longer does this: `chapters/connections/genus_complete.tex:1588-1605` gives a structural definition, and the realization criterion is separately conjectural at `:1717-1735`. FIX: replace the standalone definition body with the four-item chapter definition from `genus_complete.tex:1591-1604`, delete the Quillen-equivalence clause from the definition, and keep the equivalence only as the conjecture.

- [CRITICAL] standalone/ordered_chiral_homology.tex:39 — PROBLEM: this standalone is not import-safe. It redeclares the exact ordered-homology insertion surface (`\cA`, `\MC`, `\HH`, `\Ainf`, `\Eone`, `\Barord`, `\BarSig`, `\gmod`, `\gEone`, `\RR`, `\ZZ`, `\PP`, `\HHH`, etc.) with `\newcommand`/`\DeclareMathOperator`, but `main.tex:694-719` already predefines that surface with `\providecommand` specifically for standalone insertion. FIX: replace the whole macro block `standalone/ordered_chiral_homology.tex:39-107` by guarded definitions: `\providecommand` for symbols already supplied by `main.tex`, and `\@ifundefined{...}{\DeclareMathOperator...}{}` or `\providecommand{\foo}{\operatorname{...}}` for operators.

- [HIGH] standalone/analytic_sewing.tex:679; standalone/N5_mc5_sewing.tex:331 — PROBLEM: `def:hs-sewing` does not match the canonical chapter definition. Both standalones define HS-sewing “at parameter `q`”, while `chapters/connections/genus_complete.tex:1358-1365` defines the same label existentially: there exists `0<q<1` such that the HS sum converges. Downstream refs to `\ref{def:hs-sewing}` therefore point to different mathematics on the two sides of the seam. FIX: rewrite both standalone definitions to match `genus_complete.tex`: “Say `\cA` satisfies HS-sewing if there exists `0<q<1` such that …”, keep the displayed sum unchanged, and keep the “for every `q`” statement only in `thm:general-hs-sewing`.

- [HIGH] standalone/analytic_sewing.tex:798 — PROBLEM: `eq:connected-free-energy` changed meaning across the seam. In the standalone it is the genus-`g` formula `F_g^{conn}(\cA;q)=-\log\det(1-K_g)`, but in the chapter it is the genus-1 definition `F_\cA^{conn}(q)=-\log\det(1-K_q(\cA))` at `chapters/connections/genus_complete.tex:1801-1807`. Same label, different object. FIX: rename the standalone display to a new label such as `eq:connected-free-energy-g` and reserve `eq:connected-free-energy` for the chapter’s genus-1 definition, or rewrite the standalone display to the genus-1 formula and add a separately labeled genus-`g` variant.

- [HIGH] standalone/genus1_seven_faces.tex:710 — PROBLEM: the degeneration formula contains a false equality: `k\,\Omega/((k+h^\vee)z) = \Omega/((k+h^\vee)z)`. That is not a convention issue; it is algebraically wrong. The chapter already has the corrected degeneration wording at `chapters/connections/genus1_seven_faces.tex:969-980`. FIX: replace `standalone/genus1_seven_faces.tex:710-714` by the chapter text: “The Belavin `r`-matrix degenerates … `r^{(1)}_{\widehat{\fg}_k}(z,\tau)\to \Omega/((k+h^\vee)z)`”, and delete the bogus equality.

- [HIGH] standalone/analytic_sewing.tex:37; standalone/bp_self_duality.tex:36; standalone/garland_lepowsky.tex:36; standalone/genus1_seven_faces.tex:33; standalone/multi_weight_cross_channel.tex:35; standalone/classification_trichotomy.tex:33 — PROBLEM: these seam-critical standalone preambles still use unguarded `\newcommand`/`\DeclareMathOperator` for names the manuscript already owns in `main.tex:600-719` (`\cA`, `\MC`, `\Res`, `\Vir`, `\fg`, `\rk`, `\gr`, etc.). Imported under the main preamble, they will raise duplicate-definition errors. FIX: change all seam-facing `\newcommand` declarations in these files to `\providecommand`, and replace each `\DeclareMathOperator{\foo}{...}` by either `\providecommand{\foo}{\operatorname{...}}` or `\@ifundefined{foo}{\DeclareMathOperator{\foo}{...}}{}`.

- [HIGH] standalone/introduction_full_survey.tex:107; standalone/survey_modular_koszul_duality.tex:102; standalone/survey_modular_koszul_duality_v2.tex:166; standalone/survey_track_a_compressed.tex:94; standalone/survey_track_b_compressed.tex:149; standalone/programme_summary_sections2_4.tex:63; standalone/programme_summary_sections5_8.tex:62; standalone/programme_summary_sections9_14.tex:61; standalone/classification.tex:38; standalone/riccati.tex:36; standalone/arithmetic_shadows.tex:103; standalone/computations.tex:33 — PROBLEM: these standalones globally redefine `\ref` to inject fallback text like “full monograph”. If any of them are loaded into the manuscript, they silently corrupt reference behavior for everything that follows. FIX: do not redefine `\ref`; rename the helper to a standalone-local macro such as `\monographref`, or wrap the override in a standalone-only guard and restore the original `\ref` before any import boundary.

- [MEDIUM] standalone/programme_summary_section1.tex:52; standalone/programme_summary_sections2_4.tex:54; standalone/programme_summary_sections5_8.tex:53; standalone/programme_summary_sections9_14.tex:52 — PROBLEM: these summaries overwrite the manuscript’s generic base-field symbol with `\renewcommand{\Bbbk}{\mathbf{C}}`. That is a convention drift, not a harmless local shorthand. FIX: remove the `\renewcommand{\Bbbk}{...}` lines; if these summaries need a hard-coded complex field, introduce a local macro such as `\StandaloneField` and use that in the standalone only.

- [MEDIUM] standalone/analytic_sewing.tex:2845 — PROBLEM: the same conjecture has two labels at the seam: `conj:analytic-realisation` in the standalone and `conj:analytic-realization` in the chapter (`chapters/connections/genus_complete.tex:1718`). This breaks propagation, theorem indexing, and status sync. FIX: rename the standalone label to `conj:analytic-realization` and update the local reference at `standalone/analytic_sewing.tex:3035`.

- [LOW] standalone/bp_self_duality.tex:151 — PROBLEM: `prop:bp-central-charge` is surfaced as an unqualified proposition in the standalone, but the chapter mirror marks the same claim as `\ClaimStatusProvedElsewhere` with attribution at `chapters/examples/bershadsky_polyakov.tex:144-153`. The seam drops epistemic status and source. FIX: copy the chapter header and attribution into the standalone: mark it as proved elsewhere and add the `FKR20`/Kac--Roan--Wakimoto provenance sentence, or rename the standalone label if it is meant to be expository rather than canonical.

## Summary
Checked: 29 | Findings: 11 | Verdict: FAIL


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
session id: 019d889a-9002-7332-9f1f-352f6a58b8e4
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


thinking
**Auditing file seams**

I need to focus on the audit between the standalone and chapters directories, making sure I cover all aspects thoroughly. It looks like using the deep-beilinson-audit and possibly claim-surface-sync skills could be beneficial here. The user wants specific audit findings, which means I need to dig into the repository and review constitutional files before making any changes. I'm feeling like I might need to use the explorer sub-agent for codebase questions, so I'll start by updating the plan and my commentary.
thinking
**Updating file structure**

I need to frequently update and find the relevant files in both the standalone and chapters directories. I think I'll start by reviewing AGENTS, CLAUDE, concordance, theorem_registry, and red_team_summary. It might be worth using multi_tool parallel functionality for listing and grepping files. Since the developer recommends parallelizing tasks, I can use exec_command through multi_tool_use.parallel for efficiency. I also want to consider using rg to locate standalone references. I'll take a close look at the repository structure next.
codex
I’m treating this as a hostile seam audit of `standalone/` against `chapters/`, with findings only if I can ground them in source lines. First I’m mapping the seam surface and loading the repo’s required constitutional files so the audit uses the manuscript’s actual conventions rather than memory.
exec
/bin/zsh -lc "pwd && rg --files | rg '"'^(CLAUDE'"\\.md|chapters/connections/concordance\\.tex|metadata/theorem_registry\\.md|raeeznotes/raeeznotes100/red_team_summary\\.md|archive/raeeznotes/raeeznotes100/red_team_summary\\.md|standalone/|chapters/)';" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
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
chapters/examples/bershadsky_polyakov.tex
chapters/examples/bar_complex_tables.tex
chapters/examples/minimal_model_fusion.tex
chapters/examples/landscape_census.tex
collab spawn_agent(call_dIZQ1EaO80T5Rq3gCaQ8zRe9, prompt="Map the seam surface between standalone/ and chapters/ in /Users/raeez/chiral-bar-cobar. Identify which standalone .tex …")
spawn_agent(call_dIZQ1EaO80T5Rq3gCaQ8zRe9, prompt="Map the seam surface between standalone/ and chapters/ in /Users/raeez/chiral-bar-cobar. Identify which standalone .tex …") pending init:
  agent: 019d889a-c2f1-79b2-92f0-1887f6d130b6
mcp startup: no servers
Plan update
  → Inspect repository structure to locate standalone/ and chapters/ directories and get an overview
  • Identify candidate seam-critical file pairs/groups by comparing standalone files with chapter files via filenames, shared labels or key formulas using rg and directory listings
  • Summarize likely overlaps with concise evidence references
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar

exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
thinking
**Exploring chapters for references**

I’m thinking about how to explore the results and possibly conduct a broad search for standalone references within the chapters or main text. It sounds like there might be some interesting details to uncover! I want to ensure I’m thorough and not missing any significant references, so a careful approach seems important here. I'll gather the details and see what connections I can find. Let's dive in!
Plan update
  ✓ Inspect repository structure to locate standalone/ and chapters/ directories and get an overview
  → Identify candidate seam-critical file pairs/groups by comparing standalone files with chapter files via filenames, shared labels or key formulas using rg and directory listings
  • Summarize likely overlaps with concise evidence references
exec
/bin/zsh -lc 'ls standalone' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
N1_koszul_meta.tex
N2_mc3_all_types.tex
N3_e1_primacy.tex
N4_mc4_completion.tex
N5_mc5_sewing.tex
N6_shadow_formality.tex
analytic_sewing.aux
analytic_sewing.log
analytic_sewing.out
analytic_sewing.pdf
analytic_sewing.tex
analytic_sewing.toc
arithmetic_shadows.aux
arithmetic_shadows.log
arithmetic_shadows.out
arithmetic_shadows.pdf
arithmetic_shadows.tex
arithmetic_shadows.toc
bp_self_duality.tex
chi_R_plot.png
codex
I’ve got the repository surface. Next I’m narrowing to actual seam-critical pairs instead of auditing unrelated chapters blindly: shared filenames, shared labels, and places where `standalone/` papers are clearly mirrored or imported into `chapters/`.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
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
connections
examples
frame
theory
exec
/bin/zsh -lc 'find chapters -maxdepth 2 -type f | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex
chapters/theory/ordered_associative_chiral_kd.tex
chapters/theory/chiral_center_theorem.tex
chapters/theory/existence_criteria.tex
chapters/theory/three_invariants.aux
chapters/theory/bar_construction.aux
chapters/theory/cobar_construction.aux
chapters/theory/introduction.aux
chapters/theory/configuration_spaces.tex
chapters/theory/chiral_koszul_pairs.aux
collab wait(call_iI6N3f34rpy4P8Etfis8R050)
  receivers: 019d889a-c2f1-79b2-92f0-1887f6d130b6
exec
/bin/zsh -lc 'rg -n "thm:" standalone/ordered_chiral_homology.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
293:\begin{theorem}[Ordered chiral homology]\label{thm:main-ord-ch}
374:chiral homology of $D^\times$]\label{thm:hh-vs-ch}
427:  \textup{(}Theorem~\textup{\ref{thm:formality-bridge}}%
442:\label{thm:e3-cs}
582:The formality bridge (Theorem~\ref{thm:formality-bridge})
586:(Theorem~\ref{thm:chiral-qg-equiv}) concretely, then compute
756:Theorem~\ref{thm:chiral-qg-equiv}.
1073:(Theorem~\ref{thm:formality-bridge}) fails: the
1524:\label{thm:bridge}
2266:\label{thm:chiral-qg-equiv}
2505:(Theorem~\ref{thm:w-infty-chiral-qg}).
2604:Theorem~\ref{thm:chiral-qg-equiv} lifts Drinfeld's
2664:equivalence (Theorem~\ref{thm:chiral-qg-equiv}) lifts this
2763:\label{thm:w-infty-chiral-qg}
2766:Theorem~\textup{\ref{thm:chiral-qg-equiv}}: an $R$-matrix,
2818:  $\alpha$ of Theorem~\textup{\ref{thm:chiral-qg-equiv}},
2822:Theorem~\textup{\ref{thm:chiral-qg-equiv}}. The OPE
3017:Theorem~\textup{\ref{thm:chiral-qg-equiv}}, the bar
3038:Theorem~\textup{\ref{thm:chiral-qg-equiv}}, direction
3049:unique (Theorem~\ref{thm:chiral-qg-equiv}: the functors
exec
/bin/zsh -lc 'rg -n "thm:" chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
246:\label{thm:shuffle}
796:\label{thm:opposite}
846:Apply Theorem~\ref{thm:opposite} to the anti-involution
864:\textup{(}Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}\textup{)}
876:of Theorem~\textup{\ref{thm:opposite}}: the reversal involution
925:Now apply Theorem~\ref{thm:opposite} to the second factor:
1019:\label{thm:tangent=K}
1076:Theorem~\ref{thm:tangent=K} identifies that one-defect complex with
1109:Theorem~\ref{thm:HH-coHH-homology}.
1140:\label{thm:bimod-bicomod}
1173:\label{thm:diagonal}
1174:Under the equivalence of Theorem~\ref{thm:bimod-bicomod}, the diagonal bimodule ${}_A A_A$ is sent
1233:for $A$-bimodules along Theorem~\ref{thm:bimod-bicomod} and use
1234:Theorem~\ref{thm:diagonal}.
1250:Theorem~\ref{thm:bimod-bicomod} identifies the derived category of
1275:\label{thm:HH-coHH-homology}
1295:Apply the equivalence of Theorem~\ref{thm:bimod-bicomod} to the pair $(A,M)$.
1296:The diagonal bimodule $A$ goes to $C_\Delta$ by Theorem~\ref{thm:diagonal}, and $M$ goes to
1307:\label{thm:HH-coHH-cohomology}
1323:Derived Hom is preserved by the equivalence of Theorem~\ref{thm:bimod-bicomod}. Therefore
exec
/bin/zsh -lc 'rg -n "thm:chiral-qg-equiv" -n chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
8088:(Theorem~\ref{thm:chiral-qg-equiv}): the $R$-matrix from the
8190:\label{thm:chiral-qg-equiv}
8297:Theorem~\ref{thm:chiral-qg-equiv} provides three readouts of the same
8430:(Theorem~\ref{thm:chiral-qg-equiv},
8451:(Theorem~\ref{thm:chiral-qg-equiv}) exhibited
8479:Theorem~\textup{\ref{thm:chiral-qg-equiv}}: an $R$-matrix,
8531:  $\alpha$ of Theorem~\textup{\ref{thm:chiral-qg-equiv}},
8535:Theorem~\textup{\ref{thm:chiral-qg-equiv}}. The OPE
8729:Theorem~\textup{\ref{thm:chiral-qg-equiv}}, the bar
8750:Theorem~\textup{\ref{thm:chiral-qg-equiv}}, direction
8761:unique (Theorem~\ref{thm:chiral-qg-equiv}: the functors
8836:  (Theorem~\ref{thm:chiral-qg-equiv}), and the JKL vertex
8852:Theorem~\ref{thm:chiral-qg-equiv}: the $R$-matrix is
9018:Theorem~\ref{thm:chiral-qg-equiv} in two respects.
9050:of Theorem~\ref{thm:chiral-qg-equiv} remains the primary
9851:Theorem~\textup{\ref{thm:chiral-qg-equiv}}: an $N \times N$
9978:  Theorem~\textup{\ref{thm:chiral-qg-equiv}}, with
9983:Theorem~\textup{\ref{thm:chiral-qg-equiv}}.
10003:  \textup{(}Theorem~\textup{\ref{thm:chiral-qg-equiv}},
10144:(Theorem~\ref{thm:chiral-qg-equiv}).
exec
/bin/zsh -lc 'rg -l "kappa" standalone' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/analytic_sewing.tex
standalone/theorem_index.tex
standalone/computations.tex
standalone/N6_shadow_formality.tex
standalone/gaudin_from_collision.tex
standalone/ordered_chiral_homology.tex
standalone/programme_summary_section1.tex
standalone/programme_summary_sections5_8.tex
standalone/e1_primacy_ordered_bar.tex
standalone/three_parameter_hbar.tex
standalone/survey_modular_koszul_duality_v2.tex
standalone/three_dimensional_quantum_gravity.tex
standalone/introduction_full_survey.tex
standalone/virasoro_r_matrix.tex
standalone/cover_letter_garland_lepowsky.tex
standalone/five_theorems_modular_koszul.tex
standalone/riccati.tex
standalone/programme_summary_sections9_14.tex
standalone/survey_modular_koszul_duality.tex
standalone/survey_track_b_compressed.tex
exec
/bin/zsh -lc 'rg -n "kappa" chapters/theory/*' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 2770

chapters/theory/bar_construction.tex:40:$d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$ from the Hodge bundle
chapters/theory/bar_construction.tex:169:$\kappa(\cA)\cdot\omega_g$ controls the genus tower.
chapters/theory/bar_construction.tex:206:the \emph{invariant pairing} $\kappa(a,b) = a_{(1)}b$ extracts
chapters/theory/bar_construction.tex:212:uses~$\kappa$. Neither component is individually a differential
chapters/theory/bar_construction.tex:427:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, and the curvature
chapters/theory/bar_construction.tex:428:$\kappa(\cA)$ is the \emph{infinitesimal generator} of this
chapters/theory/bar_construction.tex:431:datum~$\kappa$ determines the periodic datum (the monodromy of the
chapters/theory/bar_construction.tex:440:Theorem~D that the leading coefficient~$\kappa(\cA)$ of the
chapters/theory/bar_construction.tex:442:$F_g(\cA) = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$
chapters/theory/bar_construction.tex:451:characteristic~$\kappa(\cA)$. At the scalar level, the T-matrix
chapters/theory/bar_construction.tex:456:nilpotency $\kappa(\lambda)^{g-1} = 0$
chapters/theory/bar_construction.tex:458:$\exp(\kappa(\lambda))$ \emph{unipotent}, not periodic: geometry
chapters/theory/bar_construction.tex:682:at degree~$1$: the full chiral product extracts the double-pole mode $J_{(1)}J = k$. Since $J_{(0)}J = 0$ (no simple pole), only the curvature component $d_{\mathrm{curvature}}$ contributes (Proposition~\ref{prop:pole-decomposition}). The level~$k$ is visible at genus~$0$ through the bar differential; at genus~$g \geq 1$, it acquires a topological partner $\kappa(\cH_k)\cdot\omega_g$ from the Hodge bundle (Chapter~\ref{chap:higher-genus}). See Chapter~\ref{ch:heisenberg-frame}, \S\ref{sec:frame-bar-deg1} for the full computation.
chapters/theory/bar_construction.tex:1031:where $d_{\mathrm{bracket}}$ extracts residues from simple poles (Lie bracket terms $a_{(0)}b$) and $d_{\mathrm{curvature}}$ extracts residues from double poles (metric/level terms $\kappa(a,b)|0\rangle$).
chapters/theory/bar_construction.tex:1066:which extracts the invariant bilinear form $(\phi_i)_{(1)}\phi_j = \kappa(\phi_i, \phi_j)|0\rangle$. For Kac--Moody algebras, this is the level: $(J^a)_{(1)}J^b = k\,\delta^{ab}|0\rangle$.
chapters/theory/bar_construction.tex:1086:For Kac--Moody algebras, the failure of $d_{\mathrm{bracket}}^2 = 0$ is controlled by the level-$k$ double-pole OPE coefficient $k \cdot (\,,\,)$, which gives rise to the curved $A_\infty$ curvature element $m_0$ with scalar projection $\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$ (Chapter~\ref{chap:deformation-theory}).
chapters/theory/bar_construction.tex:1420:$m_0 = \kappa \cdot \omega_g$
chapters/theory/bar_construction.tex:1815:oriented at each genus. It is the determinant line of $T_{C_{p+1}(\Sigma_g)}$ with genus-dependent corrections, ensuring consistent signs across all face maps. At genus~$0$, this guarantees $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}); at genus~$g \geq 1$, the fiberwise differential satisfies $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ and the total corrected differential $\Dg{g}^2 = 0$ is established in Chapter~\ref{chap:higher-genus}.
exec
/bin/zsh -lc 'rg -n "kappa" standalone/shadow_towers.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
61:characteristic~$\kappa$, cubic shadow~$\alpha$, and quartic
68: Q(t) \;=\; 4\kappa^2 + 12\kappa\alpha\,t
69: + (9\alpha^2 + 16\kappa S_4)\,t^2
73:The critical discriminant $\Delta = 8\kappa S_4$ partitions all
80:three invariants $(\kappa, \alpha, S_4)$.
167:\item $S_2 = \kappa(A)$, the \emph{modular characteristic}:
168: the genus-$1$ curvature scalar determining $F_1 = \kappa/24$.
184:genus-$0$ triple $(\kappa, \alpha, S_4)$.
189:with shadow data $S_r$, and $\kappa = S_2 \neq 0$. Define
192: \;=\; 4\kappa^2 + 12\kappa\alpha\,t
193: + (9\alpha^2 + 16\kappa S_4)\,t^2
200:$(\kappa, \alpha, S_4)$ via the closed form
206:$\Delta := 8\kappa S_4$ gives the Gaussian decomposition
208: Q(t) \;=\; (2\kappa + 3\alpha\,t)^2 + 2\Delta\,t^2.
215:On any primary line $L$ with $\kappa \neq 0$, the shadow
229: $R_r \in \mathbb{Q}(\alpha, \kappa, S_4)$.
264: F_2(A) \;=\; \kappa(A) \cdot \lambda_2^{\mathrm{FP}},
273:the scalar formula $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
337:The \emph{modular characteristic} $\kappa(A) \in \mathbb{Q}(c)$
339:$F_1(A) = \kappa(A)/24$. The \emph{central charge}~$c$ is
exec
/bin/zsh -lc 'rg -n "r''^Vir" standalone/virasoro_r_matrix.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"r\\"'^" standalone/virasoro_r_matrix.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
116:r^{\mathrm{coll}}(z) = \frac{c/2}{z^3} + \frac{2T}{z}.
exec
/bin/zsh -lc "rg -n \"av\\(r\\(z\\)\\)\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

wait(call_iI6N3f34rpy4P8Etfis8R050) timed out:
exec
/bin/zsh -lc "rg -n \"av\\(r\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
I’ve loaded the repo’s governing conventions and status surface. The next step is the actual seam map: which standalone papers duplicate or restate chapter material, then line-by-line checks at those transition points for formula drift, macro fragility, and stale theorem/status claims.
exec
/bin/zsh -lc "rg -n \"r\\(z\\)\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
134: $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$, a
137: $\kappa(\cA) = \operatorname{av}(r(z))$ for abelian algebras
139: $\kappa = \operatorname{av}(r(z)) + \dim(\fg)/2$;
Plan update
Seam audit needs a mapped surface before findings. I’m narrowing to standalone/chapter overlaps, then verifying each suspected seam against live lines only.
  → Map standalone/chapter seam-critical file pairs and transition points
  • Read paired files in context and extract grounded inconsistencies
  • Re-verify each finding and produce exact fixes with file:line
exec
/bin/zsh -lc "rg -n \"r\\(z\\)\" standalone/virasoro_r_matrix.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
82:r(z) := \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)
90:$\kappa(\cA) = \mathrm{av}(r(z))$ is its $\Sigma_2$-coinvariant.
95:primary line, the path-ordered exponential of $r(z)$ produces the
310:$r(z) = k/z$, a simple pole. On the primary sector,
318:collision residue is $r(z) = \Omega/((k+h^\vee)z)$ on the adjoint
exec
/bin/zsh -lc 'rg -n "Swiss" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_foundations.tex:990:closest existing work is the Swiss-cheese operad
chapters/examples/kac_moody.tex:5205:\index{Swiss-cheese!critical level deformation}
chapters/examples/kac_moody.tex:5208:governing the chiral Swiss-cheese pair
chapters/examples/w_algebras.tex:7037:Swiss-cheese operations, but
chapters/frame/preface_sections10_13_draft.tex:14:The Swiss-cheese operad $\SCchtop$ encodes the interaction of these two
chapters/frame/preface_sections10_13_draft.tex:74:the holomorphic-topological operad to the classical Swiss-cheese operad,
chapters/frame/preface_sections10_13_draft.tex:100:For the Heisenberg algebra $\mathcal H_k$ in Swiss-cheese coordinates:
chapters/frame/preface_sections10_13_draft.tex:166:complexity of the Swiss-cheese operations.
chapters/frame/preface_sections10_13_draft.tex:196:The Swiss-cheese structure at genus~$0$ produces a Poisson vertex
chapters/frame/preface_sections10_13_draft.tex:588:Volume~II identifies the local composition law (the Swiss-cheese
chapters/connections/thqg_open_closed_realization.tex:17:\index{Swiss-cheese theorem!chiral|textbf}
chapters/connections/thqg_open_closed_realization.tex:380:\begin{theorem}[Universal open/closed pair (chiral Swiss-cheese theorem);
chapters/connections/thqg_open_closed_realization.tex:383:\index{Swiss-cheese theorem!chiral|textbf}
chapters/connections/thqg_open_closed_realization.tex:393:Swiss-cheese pair over~$\cA$
chapters/connections/thqg_open_closed_realization.tex:402:of local chiral Swiss-cheese pairs.
chapters/connections/thqg_open_closed_realization.tex:422:where $\mu_{1;n}$ is the mixed operation of the Swiss-cheese pair.
chapters/connections/thqg_open_closed_realization.tex:429:The Swiss-cheese codimension-$1$ identities for the pair
chapters/connections/thqg_open_closed_realization.tex:438:Uniqueness: any Swiss-cheese morphism
chapters/connections/thqg_open_closed_realization.tex:466:\index{Swiss-cheese operad!mixed sector|textbf}
chapters/connections/thqg_open_closed_realization.tex:509:modular Swiss-cheese chapter) holds at all genera.
exec
/bin/zsh -lc 'rg -n "Swiss" standalone/five_theorems_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc 'rg -n "Swiss" standalone/analytic_sewing.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "F_g" chapters/theory/higher_genus_foundations.tex | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
598: a cross-channel correction $\delta F_g^{\mathrm{cross}}$
5114:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
5530: $\delta F_g^{\mathrm{cross}} \neq 0$
5531: \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
5616:On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,
5819:\textup{(}ALL-WEIGHT + $\delta F_g^{\mathrm{cross}}$\textup{)}
5823:$\delta F_g^{\mathrm{cross}} \neq 0$
5824:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
5844:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
5848:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
thinking
**Running commands efficiently**

I'm considering running commands in parallel to handle multiple tasks more efficiently. I want to list standalone tex basenames, grep for matching basenames in chapters, and then identify unique labels overlapping potentially using a diff command. It feels like shell loops might be the way to go, though I’m also contemplating using Python for a small one-liner. But honestly, I think using shell with tools like awk or exec commands could work better for this task!
exec
/bin/zsh -lc "printf 'Standalone basenames with direct chapter filename matches or close matches:\\n'; for f in standalone/*.tex; do b="'$(basename "$f" .tex); m=$(rg --files chapters | rg "/$b('"\\.tex)?"'$|/$b[_-]|'"\\" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched "
zsh:1: parse error near `m=$(rg --files chapt...'
exec
/bin/zsh -lc "printf 'Chapter references to standalone path or standalone titles:\\n'; rg -n 'standalone/|seven faces|arithmetic shadows|holographic datum|drinfeld|virasoro r-matrix|ordered chiral homology|e1 primacy|five theorems|Swiss-cheese|PVA descent|Garland|shadow towers|classification trichotomy|analytic sewing' chapters standalone main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1059

Chapter references to standalone path or standalone titles:
main.tex:694:% Standalone-paper macros (ordered chiral homology insertion)
main.tex:728:We define ordered chiral homology
main.tex:856:% The reader meets the five theorems before the Overture
main.tex:1324:% holographic datum H(W_3) = (A, A!, C, r(z), Theta_A, nabla^hol).
main.tex:1351:\input{chapters/examples/yangians_drinfeld_kohno}
main.tex:1522:% The seven faces of the collision residue: master chapter for Part V.
main.tex:1753: \phantomsection\label{conj:derived-drinfeld-kohno}%
main.tex:1760: % cor:dk23-all-types: real label in yangians_drinfeld_kohno.tex (always compiled)
standalone/analytic_sewing.tex:174:proved algebraically; the analytic sewing package developed here
standalone/analytic_sewing.tex:317:The analytic sewing programme is one component of a larger
standalone/analytic_sewing.tex:333:\item five theorems (A through D and~H) controlling the
standalone/analytic_sewing.tex:341:The analytic sewing programme begins where the algebraic
standalone/analytic_sewing.tex:636:The analytic sewing programme extends this family to a family of
standalone/analytic_sewing.tex:967:case: a chiral algebra for which the entire analytic sewing
standalone/analytic_sewing.tex:1660:forms of weight~$8$.  The analytic sewing programme detects
standalone/analytic_sewing.tex:2311:the primary open problem of the analytic sewing programme.
standalone/analytic_sewing.tex:3058:Combining the analytic sewing of this paper with Zhu's modular
exec
/bin/zsh -lc "printf 'Shared labels between standalone and chapters (first 200):\\n'; tmp1="'$(mktemp); tmp2=$(mktemp); rg -n '"'\\\\label\\{["'^}]+'"\\}' standalone/*.tex | sed -E 's#"'^([''^:]+):([0-9]+):.*'"\\\\label\\{(["'^}]+)'"\\}#\\3\\t\\1:\\2#' | sort > \""'$tmp1"; rg -n '"'\\\\label\\{["'^}]+'"\\}' chapters/**/*.tex | sed -E 's#"'^([''^:]+):([0-9]+):.*'"\\\\label\\{(["'^}]+)'"\\}#\\3\\t\\1:\\2#' | sort > \""'$tmp2"; join -t $'"'\\t' -1 1 -2 1 \""'$tmp1" "$tmp2" | head -200' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Shared labels between standalone and chapters (first 200):
SA:completion	standalone/introduction_full_survey.tex:5350 Completed chiral algebras at	chapters/theory/introduction.tex:2630 Completed chiral algebras at
SA:convergence	standalone/introduction_full_survey.tex:5344 Formal power series in completed	chapters/theory/introduction.tex:2624 Formal power series in completed
SA:curves	standalone/introduction_full_survey.tex:5348 Smooth projective geometrically connected	chapters/theory/introduction.tex:2628 Smooth projective geometrically connected
SA:grading	standalone/introduction_full_survey.tex:5342 Cohomological grading: $|d| = +1$.	chapters/theory/introduction.tex:2622 Cohomological grading: $|d| = +1$.
SA:ground-field	standalone/introduction_full_survey.tex:5339 Ground field $\mathbb{C}$. All	chapters/theory/introduction.tex:2619 Ground field $\mathbb{C}$. All
ch:preface	standalone/survey_modular_koszul_duality.tex:111	chapters/frame/preface.tex:20
conv:hms-levels	standalone/introduction_full_survey.tex:5269	chapters/theory/introduction.tex:2549
conv:proof-architecture	standalone/introduction_full_survey.tex:5306	chapters/theory/introduction.tex:2586
conv:standing-assumptions	standalone/introduction_full_survey.tex:5337	chapters/theory/introduction.tex:2617
cor:bar-encodes-all	standalone/ordered_chiral_homology.tex:4275	chapters/theory/ordered_associative_chiral_kd.tex:8283
cor:gaussian-decomposition	standalone/riccati.tex:331	chapters/theory/higher_genus_modular_koszul.tex:17716
cor:mc3-all-types	standalone/N2_mc3_all_types.tex:734	chapters/examples/yangians_computations.tex:4224%
def:analytic-koszul-pair	standalone/analytic_sewing.tex:2823	chapters/connections/genus_complete.tex:1589%
def:anomaly-ratio	standalone/bp_self_duality.tex:309	chapters/theory/algebraic_foundations.tex:2471
def:anomaly-ratio	standalone/introduction_full_survey.tex:5205	chapters/theory/algebraic_foundations.tex:2471
def:chiral-ass-operad	standalone/introduction_full_survey.tex:5074	chapters/theory/algebraic_foundations.tex:2231
def:chiral-coproduct	standalone/ordered_chiral_homology.tex:2182	chapters/theory/ordered_associative_chiral_kd.tex:8152
def:chiral-koszul-morphism	standalone/N1_koszul_meta.tex:365	chapters/theory/chiral_koszul_pairs.tex:268
def:e1-chiral	standalone/introduction_full_survey.tex:5057	chapters/theory/algebraic_foundations.tex:2214
exec
/bin/zsh -lc "rg -n \"F_g\\(\\cA\" chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:F_g\(\cA)
            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '6600,6645p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
bar-complex obstruction series and Chern--Simons/WRT asymptotics,
but the manuscript does not prove an identification with the
partition function of a $3$-manifold theory.
The universal MC class
$\Theta_{\widehat{\mathfrak{g}}_k}^{\min} =
\frac{t \cdot d}{2h^\vee}\,\eta \otimes \Lambda$
(Theorem~\ref{thm:explicit-theta}) is proportional to
$t = k + h^\vee$: on the same heuristic benchmark surface, the
bar-complex curvature may be viewed as an algebraic shadow of
Chern--Simons level dependence. At critical level the scalar
coefficient vanishes, but no theorematic identification with a
topological Chern--Simons phase is proved here.
\end{remark}

\begin{proposition}[Grothendieck--Riemann--Roch bridge on the proved uniform-weight scalar lane; \ClaimStatusProvedHere]
\label{prop:grr-bridge}
\index{Grothendieck--Riemann--Roch!genus expansion}
\index{Hodge bundle!genus expansion}
On the proved uniform-weight scalar lane for a modular Koszul chiral algebra
$\cA$, the genus generating

thinking
**Documenting theorem bridging across files**

I’m gathering evidence for three key pairs of files showing theorem bridging, using line references and labels like `thm:chiral-qg-equiv` to highlight duplication and connections. I’ll produce a bullet list with exact file:line pointers to support the case, noting this is not a full audit but a focused summary. I’m also tracking plan progress between identifying pairs and summarizing findings.
Plan update
  ✓ Inspect repository structure to locate standalone/ and chapters/ directories and get an overview
  ✓ Identify candidate seam-critical file pairs/groups by comparing standalone files with chapter files via filenames, shared labels or key formulas using rg and directory listings
  → Summarize likely overlaps with concise evidence references
collab wait(call_ALhFLwDXRdUpdJ4U1rSLyMXb)
  receivers: 019d889a-c2f1-79b2-92f0-1887f6d130b6

thinking
**Summarizing evidence for theorem bridging**

I'm organizing a final message listing pairs of files connected by shared theorem labels and concepts, referencing specific lines from ripgrep outputs to back the links. I’m including details like exact file paths with line numbers and highlighting overlapping formula references, while noting the scope limits and caution about not doing a full audit. This way, the user can see clear evidence grounded in code search results.
codex
**Seam surface**

- `standalone/ordered_chiral_homology.tex` *↔* `chapters/theory/ordered_associative_chiral_kd.tex`: both surfaces define the same anchor theorem `\label{thm:chiral-qg-equiv}` (standalone line 2266; chapter line 8190) and surround it with the R-matrix/ordered-bar machinery that the chapter amplifies (see the chapter’s repeated references around lines 8088‑8852). That shared label plus the mirrored R-matrix/HH/bar language marks this pair as a direct seam.

- `standalone/shadow_towers.tex` *↔* `chapters/theory/higher_genus_foundations.tex`: both treat `\kappa` as the modular characteristic controlling the genus tower (`shadow_towers` lines 264‑274 give `F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}` and the discriminant `\Delta = 8\kappa S_4`; the chapter’s Proposition 4.7 and surrounding text at lines 6610‑6644 deliver `F_g(\cA)=\kappa(\cA)⋅…` and related `\kappa` identities). The identical numeric/obstruction story makes these files a seam.

- `standalone/virasoro_r_matrix.tex` *↔* `chapters/theory/bar_cobar_adjunction_curved.tex`: the standalone paper isolates the collision residue `r(z)` with `\kappa(\cA)=\mathrm{av}(r(z))` (lines 82‑95), while the chapter states `\kappa=\mathrm{av}(r(z))` for abelian cases and adds the `\dim(\fg)/2` Sugawara shift in the general formula (lines 134‑139). The shared `r(z)`→`kappa` bridge (plus the same emphasis on level shifts) flags this pair as seam-critical.

No deeper audit performed—just the quick label/formula signals above.
wait(call_ALhFLwDXRdUpdJ4U1rSLyMXb) 1 agents complete:
  019d889a-c2f1-79b2-92f0-1887f6d130b6 completed: "**Seam surface**

- `standalone/ordered_chiral_homology.tex` *↔* `chapters/theory/ordered_associative_chiral_kd.tex`: bo…"


thinking
**Considering analysis methods**

I found some shared labels, but it's likely not exhaustive, so I need to dig deeper. I might construct a script to compare standalone labels and chapters by using something like `rg -n` alongside `diff`. A one-off shell script could work well with awk or perl since I'm not editing. Python is also on the table for analysis, but I prefer shell. Complexity might justify a Python one-liner, and I could use a quick Python script for processing, especially for hundreds of labels.
thinking
**Identifying critical files**

I need to start by identifying the seam-critical files based on shared label counts. I can use a script to count shared labels for each standalone file and its corresponding chapter file. This approach should help prioritize what to focus on. It seems straightforward enough, and I’m ready to dive in! Let’s get this sorted out so we can effectively analyze the labels and their significance.
codex
I’ve got the duplicate-label map. Now I’m quantifying the seam instead of cherry-picking: which standalone files actually share the most labeled mathematical surface with which chapter files, so the audit can target the real drift points rather than the obvious file-name matches.
exec
/bin/zsh -lc "python - <<'PY'
import re, glob, os, collections
pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
stand = {}
for path in glob.glob('standalone/*.tex'):
    labels=[]
    with open(path) as f:
        for i,line in enumerate(f,1):
            for m in pat.finditer(line):
                labels.append((m.group(1), i))
    stand[path]=labels
chap = {}
for path in glob.glob('chapters/**/*.tex', recursive=True):
    labels=[]
    with open(path) as f:
        for i,line in enumerate(f,1):
            for m in pat.finditer(line):
                labels.append((m.group(1), i))
    chap[path]=labels
chap_by_label=collections.defaultdict(list)
for path,labels in chap.items():
    for label,line in labels:
        chap_by_label[label].append((path,line))
counts=[]
for spath,labels in stand.items():
    c=collections.Counter()
    for label,sline in labels:
        for cpath,cline in chap_by_label.get(label,[]):
            c[cpath]+=1
    for cpath,n in c.most_common():
        if n>=3:
            counts.append((n, spath, cpath))
counts.sort(reverse=True)
for n,spath,cpath in counts[:80]:
    print(f'{n:3d} | {spath} | {cpath}')
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
import re, glob, collections
pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
stand = {}
for path in glob.glob('standalone/*.tex'):
    labels=[]
    with open(path) as f:
        for i,line in enumerate(f,1):
            for m in pat.finditer(line):
                labels.append((m.group(1), i))
    stand[path]=labels
chap = {}
for path in glob.glob('chapters/**/*.tex', recursive=True):
    labels=[]
    with open(path) as f:
        for i,line in enumerate(f,1):
            for m in pat.finditer(line):
                labels.append((m.group(1), i))
    chap[path]=labels
chap_by_label=collections.defaultdict(list)
for path,labels in chap.items():
    for label,line in labels:
        chap_by_label[label].append((path,line))
counts=[]
for spath,labels in stand.items():
    c=collections.Counter()
    for label,sline in labels:
        for cpath,cline in chap_by_label.get(label,[]):
            c[cpath]+=1
    for cpath,n in c.most_common():
        if n>=3:
            counts.append((n, spath, cpath))
counts.sort(reverse=True)
for n,spath,cpath in counts[:120]:
    print(f'{n:3d} | {spath} | {cpath}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 369ms:
 69 | standalone/ordered_chiral_homology.tex | chapters/theory/ordered_associative_chiral_kd.tex
 67 | standalone/introduction_full_survey.tex | chapters/theory/introduction.tex
 58 | standalone/ordered_chiral_homology.tex | chapters/theory/higher_genus_modular_koszul.tex
 19 | standalone/ordered_chiral_homology.tex | chapters/theory/en_koszul_duality.tex
 15 | standalone/introduction_full_survey.tex | chapters/theory/algebraic_foundations.tex
 14 | standalone/riccati.tex | chapters/theory/higher_genus_modular_koszul.tex
  9 | standalone/survey_modular_koszul_duality.tex | chapters/frame/preface.tex
  8 | standalone/survey_modular_koszul_duality.tex | chapters/frame/preface_sections2_4_draft.tex
  7 | standalone/survey_track_a_compressed.tex | chapters/frame/preface_sections2_4_draft.tex
  7 | standalone/survey_modular_koszul_duality_v2.tex | chapters/frame/preface_sections2_4_draft.tex
  7 | standalone/survey_modular_koszul_duality_v2.tex | chapters/frame/preface.tex
  7 | standalone/analytic_sewing.tex | chapters/connections/genus_complete.tex
  6 | standalone/survey_track_a_compressed.tex | chapters/frame/preface.tex
  6 | standalone/classification_trichotomy.tex | chapters/theory/three_invariants.tex
  6 | standalone/arithmetic_shadows.tex | chapters/theory/higher_genus_modular_koszul.tex
  5 | standalone/shadow_towers_v3.tex | chapters/theory/higher_genus_modular_koszul.tex
  5 | standalone/shadow_towers.tex | chapters/theory/higher_genus_modular_koszul.tex
  5 | standalone/multi_weight_cross_channel.tex | chapters/theory/higher_genus_modular_koszul.tex
  5 | standalone/N5_mc5_sewing.tex | chapters/connections/genus_complete.tex
  3 | standalone/seven_faces.tex | chapters/theory/three_invariants.tex




thinking
**Evaluating formula divergences**

I need to detect exact divergences using formula searches on specific hotspots like kappa formulas and the r-matrix. There are many duplicated labels, so I could normalize and compare around shared labels. It’s crucial to systematically inspect seam-critical pairs with high overlap. I might start by searching for known forbidden formulas in standalone and see if chapters have corrections. The audit should focus on inconsistencies between standalone and main documents, not just general errors. Also, I should check macro definitions to ensure everything is correctly included.
thinking
**Checking inconsistencies in claim statuses**

I want to see if standalones still have outdated claim statuses that don't match the chapters. I'll check differences in statuses using shared labels, focusing on environments and ClaimStatus. The theorem index might not be relevant if there are no statuses in standalone documents. Some standalones could just be papers without claim tags, but stale claims might show as theorem statements that contradict chapters. I could automate a comparison for each shared label and inspect lines around labels for significant differences. Alternatively, I could look for canonical formulas at known hotspots.
thinking
**Identifying seam mismatches**

I need to find places where the standalone documents still reflect older versions, which could lead to seam issues related to AGENTS invariants. Specifically, the SC structure on the bar complex should be retracted, but standalones might still claim it's a Swiss-cheese coalgebra. The r-matrix level prefix could be missing, and kappa formulas might be incorrect. Also, introductions or prefaces could have stale information about analytic sewing or topologization statuses. I should check for `\newcommand` usage in `standalone/ordered_chiral_homology.tex`, which might be causing collisions or reflect outdated information.
thinking
**Searching for discrepancies**

I’m thinking about how to identify hot patterns in standalone files. I want to use "rg" to look for forbidden formulas and phrases. If there are standalone instances with those forbidden phrases but the corresponding chapters don't contain them, that indicates a drift. So, I’ll search both the standalone files and the chapters to find any discrepancies. It's all about ensuring consistency between them!
codex
I’m moving from seam mapping to breakage hunting. The fastest path is the repo’s own failure modes: blacklist formulas and known object-conflation phrases in `standalone/`, then check whether `chapters/` already carries the corrected surface.
exec
/bin/zsh -lc "rg -n 'B\\(A\\) is (an |a )?(SC|Swiss-cheese)|bar complex.*Swiss-cheese|SC\\"'^'"\\{ch,top\\}.*bar complex|coalgebra over the .*Swiss-cheese|Swiss-cheese.*bar complex|bar complex.*SC' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Omega/z|k\\\\Omega/z|Omega/\\\\(\\\\(k\\+h\\"'^v'"\\\\)\\*z\\\\)|kappa\\(W_N\\)|H_\\{N-1\\}|c/12|T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\|\\+1|S_2 *= *c/12|d\\"'^2 *= *kappa'"\\\\*omega_g|F_2 *= *(1/5760|7/2880)' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 73ms:
rg: regex parse error:
    (?:\\Omega/z|k\\Omega/z|Omega/\\(\\(k\+h\^v\\)\*z\\)|kappa\(W_N\)|H_\{N-1\}|c/12|T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\|\+1|S_2 *= *c/12|d\^2 *= *kappa\\*omega_g|F_2 *= *(1/5760|7/2880))
                                                                                               ^
error: repetition quantifier expects a valid decimal
 succeeded in 93ms:
chapters/connections/bv_brst.tex:2425:compared is not ``the bar complex as a Swiss-cheese algebra'': the
standalone/koszulness_fourteen_characterizations.tex:301:the Swiss-cheese bar complex. All standard families are chirally
chapters/theory/bar_construction.tex:2164:feed the Swiss-cheese story. On the bar complex itself they still
chapters/theory/en_koszul_duality.tex:1278:\index{bar complex!is E1 coassociative, NOT SC}
standalone/introduction_full_survey.tex:658:\textsc{Operadic primacy of Swiss-cheese.} The bar complex
chapters/theory/ordered_associative_chiral_kd.tex:1825:equip the ordered bar complex with a full Swiss-cheese algebra
chapters/theory/introduction.tex:2238: Higher-dimensional bar complexes; Totaro relations; Ayala--Francis; topologization $\mathsf{SC}^{\mathrm{ch,top}} + T_{\mathrm{Sug}} \Rightarrow \Ethree$ (Thm~\ref{thm:topologization}, proved for affine KM; Conj~\ref{conj:topologization-general}, general) \\[6pt]
standalone/survey_track_b_compressed.tex:1493:bar complex, the shadow tower, the Swiss-cheese structure, the
standalone/survey_modular_koszul_duality.tex:7090:bar complex, the shadow obstruction tower, the Swiss-cheese structure, the PVA
exec
/bin/zsh -lc "rg -n '\\\\newcommand|\\\\renewcommand|\\\\def\\\\|\\\\DeclareMathOperator|\\\\DeclarePairedDelimiter' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1169

standalone/N5_mc5_sewing.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N5_mc5_sewing.tex:34:\newcommand{\cH}{\mathcal{H}}
standalone/N5_mc5_sewing.tex:35:\newcommand{\cW}{\mathcal{W}}
standalone/N5_mc5_sewing.tex:36:\newcommand{\cM}{\mathcal{M}}
standalone/N5_mc5_sewing.tex:37:\newcommand{\barB}{\bar{B}}
standalone/N5_mc5_sewing.tex:38:\newcommand{\MC}{\mathrm{MC}}
standalone/N5_mc5_sewing.tex:39:\newcommand{\Sym}{\mathrm{Sym}}
standalone/N5_mc5_sewing.tex:40:\newcommand{\HS}{\mathrm{HS}}
standalone/N5_mc5_sewing.tex:41:\newcommand{\Vir}{\mathrm{Vir}}
standalone/N5_mc5_sewing.tex:42:\newcommand{\Res}{\mathrm{Res}}
standalone/N5_mc5_sewing.tex:43:\newcommand{\fg}{\mathfrak{g}}
standalone/N5_mc5_sewing.tex:44:\newcommand{\GG}{\Gamma}
standalone/N1_koszul_meta.tex:34:\newcommand{\cA}{\mathcal{A}}
standalone/N1_koszul_meta.tex:35:\newcommand{\cC}{\mathcal{C}}
standalone/N1_koszul_meta.tex:36:\newcommand{\cM}{\mathcal{M}}
standalone/N1_koszul_meta.tex:37:\newcommand{\cZ}{\mathcal{Z}}
standalone/N1_koszul_meta.tex:38:\newcommand{\cD}{\mathcal{D}}
standalone/N1_koszul_meta.tex:39:\newcommand{\cO}{\mathcal{O}}


thinking
**Evaluating manuscript consistency**

I’m considering how the standalone manuscript might have stale claims compared to the chapters. If both parts have the same incorrect wording, that doesn't create a seam inconsistency, but rather a stale claim in both. It seems crucial to evaluate the mission between the standalone and the chapters. I think I should report if the standalone duplicates a stale claim that has already been corrected elsewhere in the main manuscript.
thinking
**Inspecting inconsistencies**

I'm focusing on searching for specific patterns in the canonical formulas, like the same label eq:km-rmatrix. I need to look at potential inconsistencies and gather contexts around any suspect occurrences. Using parallel tools like `sed/nl` on likely files could help. I should consider running `rg -n` to look into specific files for exact line references. I want to inspect the introduction_full_survey and theory/introduction around lines 650-700, as well as any related corrected sections.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '2154,2172p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '630,690p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1448,1492p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2230,2246p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2154	correspond to the $n+1$ ways of cutting
  2155	$\Conf_n^{<}(\bR) = \{t_1 < \cdots < t_n\}$ into two
  2156	consecutive segments $\{t_1,\ldots,t_p\} \sqcup
  2157	\{t_{p+1},\ldots,t_n\}$. This is topological factorization
  2158	on the~$\bR$-direction of~$\bC \times \bR$ in the
  2159	Costello--Gwilliam framework~\cite[\S5.4]{CG17}: the bar
  2160	differential is holomorphic factorization on~$\FM_k(\bC)$
  2161	(Remark~\ref{rem:costello-gwilliam-factorization}); the bar
  2162	coproduct is topological factorization on~$\Conf_n^{<}(\bR)$.
  2163	Together they exhibit the two geometric directions that later
  2164	feed the Swiss-cheese story. On the bar complex itself they still
  2165	form only the single-coloured $\Eone$ dg coalgebra
  2166	$T^c(s^{-1}\bar{\cA})$; the actual
  2167	$\mathrm{SC}^{\mathrm{ch,top}}$ datum appears only on the
  2168	derived-center pair
  2169	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
  2170	\end{remark}
  2171	
  2172	\begin{remark}[Conventions for this chapter]\label{rem:three-bar-conventions}
 succeeded in 51ms:
   630	= (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
   631	appears only after adding the Sugawara shift.
   632	
   633	\textsc{Physical primacy.} The natural physical objects are
   634	ordered. Three-dimensional holomorphic-topological theories
   635	have line operators along the topological direction $\R_t$
   636	(Costello--Gaiotto~\cite{CostelloGaiotto2020}); these line operators
   637	form the ordered convolution algebra ${\gAmod}^{\Eone}$ on
   638	$\C_z \times \R_t$, and their fusion is the
   639	$\Eone$-multiplication. Open-string field theory and
   640	factorization on bordered curves carry intrinsic boundary
   641	orderings. Integrable lattice models have $R$-matrices that
   642	satisfy the (ordered) Yang--Baxter equation, not its symmetric
   643	projection. In every physical setting where the bar complex
   644	appears, the line/boundary direction is ordered before any
   645	$\Sigma_n$-symmetrization is taken.
   646	
   647	\textsc{Categorical primacy.} The categorical objects of
   648	representation theory are ordered. Quantum groups, Yangians, and
   649	braided tensor categories are the natural framework for chiral
 succeeded in 51ms:
  1448	form the ordered convolution algebra ${\gAmod}^{\Eone}$ on
  1449	$\C_z \times \R_t$, and their fusion is the
  1450	$\Eone$-multiplication. Open-string field theory and
  1451	factorization on bordered curves carry intrinsic boundary
  1452	orderings. Integrable lattice models have $R$-matrices that
  1453	satisfy the (ordered) Yang--Baxter equation, not its symmetric
  1454	projection. In every physical setting where the bar complex
  1455	appears, the line/boundary direction is ordered before any
  1456	$\Sigma_n$-symmetrization is taken.
  1457	
  1458	\textsc{Categorical primacy.} The categorical objects of
  1459	representation theory are ordered. Quantum groups, Yangians, and
  1460	braided tensor categories are the natural framework for chiral
  1461	algebras coupled to a spectral parameter; their structure
  1462	constants are matrix-valued and obey ordered identities (CYBE,
  1463	pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
  1464	categories are obtained from braided ones by the
  1465	$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
  1466	exactly the categorical analogue of the averaging
  1467	map~\eqref{eq:intro-averaging}.
 succeeded in 51ms:
  2230	\hline
  2231	Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
  2232	 Shadow obstruction tower $\kappa\to\Delta\to\mathfrak C\to\mathfrak Q\to\cdots$; clutching law; archetypes G/L/C/M; branch-line reductions \\
  2233	$E_1$ modular Koszul duality (Ch.~\ref{chap:e1-modular-koszul}) &
  2234	 Ribbon modular operad; $F\!\Ass$; $E_1$ convolution; $E_1$ shadow tower; Thms $A^{E_1}$--$H^{E_1}$; ordered chiral homology (\S\ref{sec:ordered-chiral-homology}); formality bridge (Thm~\ref{thm:e1-formality-bridge}) \\
  2235	Ordered associative chiral KD (Ch.~\ref{ch:ordered-associative-chiral-kd}) &
  2236	 Diagonal bicomodule; Hochschild-coHochschild dictionary; open trace formalism; chiral--quantum group equivalence (Thm~\ref{thm:chiral-qg-equiv}) \\
  2237	$\En$ Koszul duality (Ch.~\ref{ch:en-koszul-duality}) &
  2238	 Higher-dimensional bar complexes; Totaro relations; Ayala--Francis; topologization $\mathsf{SC}^{\mathrm{ch,top}} + T_{\mathrm{Sug}} \Rightarrow \Ethree$ (Thm~\ref{thm:topologization}, proved for affine KM; Conj~\ref{conj:topologization-general}, general) \\[6pt]
  2239	\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:standard-landscape}: The Standard Landscape} \emph{(complete portrait of each family)}} \\[3pt]
  2240	\hline
  2241	Lattice VOAs (Ch.~\ref{ch:lattice}) &
  2242	 $\kappa(V_\Lambda)=\operatorname{rank}(\Lambda)$; curvature-braiding orthogonality; screening operators \\
  2243	Free fields (Ch.~\ref{chap:free-fields}) &
  2244	 Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
  2245	$\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
  2246	 First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
exec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '1776,1834p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '1760,1835p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'full Swiss-cheese|Swiss-cheese algebra|SC\\"'^'"\\{ch,top\\}|derived center pair|bar complex itself' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1776	\subsection{The product space and its operadic role}
  1777	\label{subsec:product-space}
  1778	
  1779	\begin{construction}[The SC$^{\mathrm{ch,top}}$ operation space]
  1780	\label{constr:sc-operation-space}
  1781	The two-coloured Swiss-cheese operad
  1782	$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
  1783	\[
  1784	\mathrm{SC}^{\mathrm{ch,top}}(k,m)
  1785	\;=\;
  1786	\FM_k(\mathbb C)\times E_1(m),
  1787	\]
  1788	where $\FM_k(\mathbb C)$ is the Fulton--MacPherson
  1789	compactification of $\mathrm{Conf}_k(\mathbb C)$
  1790	(the chiral, holomorphic factor) and $E_1(m)$ is
  1791	the little-intervals operad (the coassociative, topological factor).
  1792	Concretely, $E_1(m)\simeq \mathrm{Conf}_m^{<}(\mathbb R)$
  1793	up to translation and scaling, which is contractible.
  1794	
  1795	For the ordered bar complex of an $E_1$-chiral algebra,
 succeeded in 52ms:
  1760	  Both have a \emph{simple pole} along $\Delta_{ij}$:
  1761	  the connection is Fuchsian.
  1762	\item \textup{(Flatness.)} $\nabla_n^2 = 0$ on $U_n$,
  1763	  following from the classical Yang--Baxter equation
  1764	  for $r(z)$.
  1765	\item \textup{(Equivariant descent.)}
  1766	  For $\Einf$-chiral $\cA$ \textup{(}where $S(z) = \id$
  1767	  up to Koszul signs\textup{)}:
  1768	  $\cF_n^{\mathrm{ord}}$
  1769	  is $\Sigma_n$-equivariant, and
  1770	  $(\cF_n^{\mathrm{ord}})^{\Sigma_n}
  1771	  \simeq \cF_n^{\Sigma}$
  1772	  is the Beilinson--Drinfeld factorisation $\cD$-module
  1773	  on $X^{(n)}$.
  1774	\item \textup{(Non-equivariance for $\Eone$.)}
  1775	  For $\Eone$-chiral $\cA$:
  1776	  $\cF_n^{\mathrm{ord}}$ is \emph{not}
  1777	  $\Sigma_n$-equivariant. The braiding $S(z)$ on the
  1778	  $(i,j)$ factor introduces monodromy as the $i$-th and
  1779	  $j$-th points circle each other.
 succeeded in 52ms:
4651:\begin{warning}[The bar complex itself is not $\Ethree$]
5023:\begin{warning}[The bar complex itself is not $\Ethree$]


thinking
**Exploring automated comparisons**

I need more automated help, focusing on shared labels around formulas. I could compare files that share labels and look for mismatched patterns. Using a Python script sounds like a plan! I could extract lines with shared labels and check if they’re identical after removing whitespace. Though I still might need to inspect manually, I want to script comparisons for specific pairs of labels. I’ll make sure to highlight potential mismatches in environments and their bodies.
thinking
**Focusing on label extraction**

I think I’ll extract simple environments around each label based on the nearest beginnings and ends. I want to script this for a specific pair and possibly use grep to check for differences in formulas. With larger pairs, differences might be more numerous, so I’m looking for suspicious ones with patterns or statuses. There are only 7 shared labels in `standalone/analytic_sewing` versus `chapters/connections/genus_complete`, so I can manually compare contexts to find any drift. I’ll script to show shared labels and their line numbers for clarity.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, collections
from pathlib import Path
pairs=[('standalone/analytic_sewing.tex','chapters/connections/genus_complete.tex'),('standalone/N5_mc5_sewing.tex','chapters/connections/genus_complete.tex'),('standalone/bp_self_duality.tex','chapters/examples/bershadsky_polyakov.tex'),('standalone/garland_lepowsky.tex','chapters/examples/kac_moody.tex'),('standalone/riccati.tex','chapters/theory/higher_genus_modular_koszul.tex'),('standalone/arithmetic_shadows.tex','chapters/theory/higher_genus_modular_koszul.tex'),('standalone/multi_weight_cross_channel.tex','chapters/theory/higher_genus_modular_koszul.tex'),('standalone/classification_trichotomy.tex','chapters/theory/three_invariants.tex'),('standalone/genus1_seven_faces.tex','chapters/examples/yangians_drinfeld_kohno.tex')]
pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for a,b in pairs:
    da=collections.defaultdict(list); db=collections.defaultdict(list)
    for path,d in [(a,da),(b,db)]:
        with open(path) as f:
            for i,l in enumerate(f,1):
                for m in pat.finditer(l):
                    d[m.group(1)].append(i)
    shared=sorted(set(da)&set(db))
    print(f'PAIR {a} <-> {b} | shared labels={len(shared)}')
    for label in shared:
        print(f'  {label}: {a}:{da[label][0]} | {b}:{db[label][0]}')
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
PAIR standalone/analytic_sewing.tex <-> chapters/connections/genus_complete.tex | shared labels=7
  def:analytic-koszul-pair: standalone/analytic_sewing.tex:2823 | chapters/connections/genus_complete.tex:1589
  def:hs-sewing: standalone/analytic_sewing.tex:679 | chapters/connections/genus_complete.tex:1359
  def:sewing-envelope: standalone/analytic_sewing.tex:449 | chapters/connections/genus_complete.tex:1313
  eq:connected-free-energy: standalone/analytic_sewing.tex:798 | chapters/connections/genus_complete.tex:1802
  eq:heisenberg-fredholm: standalone/analytic_sewing.tex:1155 | chapters/connections/genus_complete.tex:1493
  eq:hs-sewing: standalone/analytic_sewing.tex:689 | chapters/connections/genus_complete.tex:1365
  thm:general-hs-sewing: standalone/analytic_sewing.tex:1773 | chapters/connections/genus_complete.tex:1390

PAIR standalone/N5_mc5_sewing.tex <-> chapters/connections/genus_complete.tex | shared labels=5
  def:hs-sewing: standalone/N5_mc5_sewing.tex:331 | chapters/connections/genus_complete.tex:1359
  def:sewing-envelope: standalone/N5_mc5_sewing.tex:264 | chapters/connections/genus_complete.tex:1313
  eq:heisenberg-fredholm: standalone/N5_mc5_sewing.tex:538 | chapters/connections/genus_complete.tex:1493
  eq:hs-sewing: standalone/N5_mc5_sewing.tex:340 | chapters/connections/genus_complete.tex:1365
  thm:general-hs-sewing: standalone/N5_mc5_sewing.tex:617 | chapters/connections/genus_complete.tex:1390

PAIR standalone/bp_self_duality.tex <-> chapters/examples/bershadsky_polyakov.tex | shared labels=3
  eq:bp-central-charge: standalone/bp_self_duality.tex:153 | chapters/examples/bershadsky_polyakov.tex:149
  eq:bp-ope-bosonic: standalone/bp_self_duality.tex:190 | chapters/examples/bershadsky_polyakov.tex:123
  prop:bp-central-charge: standalone/bp_self_duality.tex:151 | chapters/examples/bershadsky_polyakov.tex:146

thinking
**Comparing labeled blocks**

I’m thinking about directly comparing shared labeled blocks of text. I could write a script to extract the environment snippets around these shared labels and check for differences. Let’s focus on selected pairs and compute differences using heuristics, looking at about 5 lines before and after each label. I should consider using `diff -u` to see the variations in the extracted text snippets, but I’ll also need to read through them manually afterward. Let’s begin with specific examples.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
pairs=[('standalone/analytic_sewing.tex','chapters/connections/genus_complete.tex',['def:analytic-koszul-pair','def:hs-sewing','def:sewing-envelope','eq:connected-free-energy','eq:heisenberg-fredholm','eq:hs-sewing','thm:general-hs-sewing']),('standalone/bp_self_duality.tex','chapters/examples/bershadsky_polyakov.tex',['eq:bp-central-charge','eq:bp-ope-bosonic','prop:bp-central-charge']),('standalone/garland_lepowsky.tex','chapters/examples/kac_moody.tex',['eq:km-rmatrix','rem:sl2-admissible']),('standalone/genus1_seven_faces.tex','chapters/examples/yangians_drinfeld_kohno.tex',['eq:elliptic-rmatrix'])]
for a,b,labels in pairs:
    print('='*120)
    print(a,'<->',b)
    A=Path(a).read_text().splitlines(); B=Path(b).read_text().splitlines()
    for label in labels:
        print('-'*80)
        print(label)
        for path,lines in [(a,A),(b,B)]:
            for i,l in enumerate(lines):
                if f'\\\\label{{{label}}}' in l:
                    start=max(0,i-4); end=min(len(lines),i+6)
                    print(f'[{path}]')
                    for j in range(start,end):
                        print(f'{j+1:6d}: {lines[j]}')
                    break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
========================================================================================================================
standalone/analytic_sewing.tex <-> chapters/connections/genus_complete.tex
--------------------------------------------------------------------------------
def:analytic-koszul-pair
[standalone/analytic_sewing.tex]
  2819: at the algebraic level.  The analytic extension is the
  2820: following.
  2821: 
  2822: \begin{definition}[Analytic Koszul pair]
  2823: \label{def:analytic-koszul-pair}
  2824: An \emph{analytic Koszul pair} is a pair
  2825: $(\cA, \cA^!)^{\mathrm{an}}$ of chirally Koszul algebras,
  2826: both satisfying HS-sewing, for which the analytic bar-cobar
  2827: adjunction restricts to a Quillen equivalence on
  2828: sewing-complete categories:
[chapters/connections/genus_complete.tex]
  1585: pole order.
  1586: \end{proof}
  1587: 
  1588: \begin{definition}[Analytic Koszul pair]%
exec
/bin/zsh -lc "rg -n 'analytic Koszul pair|Quillen equivalence|sewing-complete' standalone/analytic_sewing.tex chapters/connections/genus_complete.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/analytic_sewing.tex | sed -n '2818,2855p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1588,1665p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/genus_complete.tex:1445:\begin{remark}[Completed algebras]\label{rem:hs-sewing-completed}
chapters/connections/genus_complete.tex:1591:An \emph{analytic Koszul pair} $(\cA, \cA^!)$ consists of:
standalone/analytic_sewing.tex:2815:\subsection{The analytic Koszul pair}\label{subsec:analytic-koszul}
standalone/analytic_sewing.tex:2824:An \emph{analytic Koszul pair} is a pair
standalone/analytic_sewing.tex:2827:adjunction restricts to a Quillen equivalence on
standalone/analytic_sewing.tex:2828:sewing-complete categories:
standalone/analytic_sewing.tex:2840:expected to extend to an analytic Koszul pair; the HS-sewing
standalone/analytic_sewing.tex:2847:for the analytic Koszul pair to exist: the analytic bar-cobar
standalone/analytic_sewing.tex:2848:adjunction restricts to a Quillen equivalence on
standalone/analytic_sewing.tex:2849:sewing-complete categories.
 succeeded in 51ms:
  2818	through~H of the modular Koszul duality programme
  2819	at the algebraic level.  The analytic extension is the
  2820	following.
  2821	
  2822	\begin{definition}[Analytic Koszul pair]
  2823	\label{def:analytic-koszul-pair}
  2824	An \emph{analytic Koszul pair} is a pair
  2825	$(\cA, \cA^!)^{\mathrm{an}}$ of chirally Koszul algebras,
  2826	both satisfying HS-sewing, for which the analytic bar-cobar
  2827	adjunction restricts to a Quillen equivalence on
  2828	sewing-complete categories:
  2829	\[
  2830	\barB^{\mathrm{an}} \colon
  2831	\cA^{\mathrm{sew}}\text{-}\mathrm{mod}
  2832	\rightleftarrows
  2833	(\cA^!)^{\mathrm{sew}}\text{-}\mathrm{comod}
  2834	\;\colon\!
  2835	\Omega^{\mathrm{an}}.
  2836	\]
  2837	\end{definition}
 succeeded in 51ms:
  1588	\begin{definition}[Analytic Koszul pair]%
  1589	\label{def:analytic-koszul-pair}%
  1590	\index{Koszul pair!analytic}%
  1591	An \emph{analytic Koszul pair} $(\cA, \cA^!)$ consists of:
  1592	\begin{enumerate}[label=\textup{(\roman*)}]
  1593	\item a sewing envelope $\cA^{\mathrm{sew}}$
  1594	 (Definition~\ref{def:sewing-envelope}),
  1595	\item an analytic bar coalgebra $\barB^{\mathrm{an}}(\cA)$
  1596	 (Definition~\ref{def:analytic-bar-coalgebra}),
  1597	\item a genus-zero equivalence
  1598	 $D^{\mathrm{an}}_{\mathrm{compl}}(\cA\text{-mod})
  1599	 \simeq
  1600	 D^{\mathrm{an}}_{\mathrm{conil}}
  1601	 (\barB^{\mathrm{an}}(\cA)\text{-comod})$,
  1602	\item under finite-type dualizability, an identification of
  1603	 conilpotent analytic comodules with complete
  1604	 $\cA^!$-modules.
  1605	\end{enumerate}
  1606	\end{definition}
  1607	
codex
I’ve found one real seam break already: `standalone/analytic_sewing.tex` is still using old labels for meanings that the chapter has already narrowed or redefined. I’m checking the other high-overlap pairs the same way, because this kind of label-reuse drift is worse than a cosmetic notation change.
exec
/bin/zsh -lc "rg -n 'k=0|trace-form|KZ|Sugawara shift|h\\"'^'"\\\\vee|kappa\\(|critical level|level normalization' standalone/garland_lepowsky.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'elliptic r-matrix|level normalization|k\\+h\\"'^'"\\\\vee|Belavin|collision residue' standalone/genus1_seven_faces.tex chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'HS-sewing|connected free energy|analytic Koszul pair|analytic realisation|Quillen equivalence' standalone/N5_mc5_sewing.tex chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_drinfeld_kohno.tex:1339:via the collision residue
chapters/examples/yangians_drinfeld_kohno.tex:6337:collision residues
chapters/examples/yangians_drinfeld_kohno.tex:6804:and the degree-$2$ collision residue gives
chapters/examples/yangians_drinfeld_kohno.tex:6920:For each standard family, the collision residue
chapters/examples/yangians_drinfeld_kohno.tex:7067:the collision residue $r^{\mathrm{KM}}(z) = k\Omega/z$
chapters/examples/yangians_drinfeld_kohno.tex:7150:The preceding subsections established that the collision residue
chapters/examples/yangians_drinfeld_kohno.tex:7255:\index{Belavin r-matrix@Belavin $r$-matrix|textbf}
chapters/examples/yangians_drinfeld_kohno.tex:7268:residue on $E_\tau$ produces the Belavin classical elliptic
chapters/examples/yangians_drinfeld_kohno.tex:7269:$r$-matrix~\cite{Belavin81, BelavinDrinfeld82}:
chapters/examples/yangians_drinfeld_kohno.tex:7320:The collision residue on $E_\tau$ proceeds exactly as in the
chapters/examples/yangians_drinfeld_kohno.tex:7327:$\phi_\pm(z, \tau)$ (Belavin~\cite{Belavin81}). The overall
chapters/examples/yangians_drinfeld_kohno.tex:7544:at degree~$2$, and the collision residue
chapters/examples/yangians_drinfeld_kohno.tex:7547:modular characteristic $\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$ to
chapters/examples/yangians_drinfeld_kohno.tex:7550:the relation $r(z)/\kappa = \Omega/(z(k+h^\vee))$ after
chapters/examples/yangians_drinfeld_kohno.tex:7890:The preceding subsection computed the collision residue
chapters/examples/yangians_drinfeld_kohno.tex:7905:\index{Koszul duality!binary inverse via collision residue}
chapters/examples/yangians_drinfeld_kohno.tex:7907:\index{collision residue!binary Koszul inverse}
chapters/examples/yangians_drinfeld_kohno.tex:7912:\item \emph{The collision residue determines the universal twisting
chapters/examples/yangians_drinfeld_kohno.tex:7913: morphism.} The genus-zero binary collision residue of the
chapters/examples/yangians_drinfeld_kohno.tex:7941: coalgebra. The collision residue reverses this:
 succeeded in 51ms:
Total output lines: 618

chapters/examples/kac_moody.tex:12:cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
chapters/examples/kac_moody.tex:24:$k \mapsto -k - 2h^\vee$, the critical-level center, opers,
chapters/examples/kac_moody.tex:41:$k \neq -h^\vee$.}\label{tab:km-five-theorems}
chapters/examples/kac_moody.tex:48: $(\widehat{\fg}_k)^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})$
chapters/examples/kac_moody.tex:57: Q_g(\widehat{\fg}_{-k-2h^\vee})
chapters/examples/kac_moody.tex:62: $\kappa(\widehat{\fg}_k)
chapters/examples/kac_moody.tex:63: = \frac{\dim\fg\,(k{+}h^\vee)}{2h^\vee}$;\quad
chapters/examples/kac_moody.tex:87:$\kappa(\widehat{\fg}_k)$ &
chapters/examples/kac_moody.tex:88: $\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ \\
chapters/examples/kac_moody.tex:90: $\kappa(x,[y,z])$ (Lie bracket) \\
chapters/examples/kac_moody.tex:92:$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
chapters/examples/kac_moody.tex:93:Koszul dual & $\mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})$
chapters/examples/kac_moody.tex:94: (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
chapters/examples/kac_moody.tex:96:Critical level & $k = -h^\vee$: uncurved,
chapters/examples/kac_moody.tex:108:Kac--Moody algebra at generic level $k \neq -h^\vee$ is
chapters/examples/kac_moody.tex:113:\widehat{\fg}_{-k-2h^\vee},\;\;
chapters/examples/kac_moody.tex:114:r(z) = \frac{\Omega}{(k{+}h^\vee)\,z}\,\Bigr),
chapters/examples/kac_moody.tex:117:$r$-matrix is recorded in the KZ normalisation
 succeeded in 50ms:
standalone/N5_mc5_sewing.tex:78:and polynomial OPE coefficient growth satisfies the HS-sewing
standalone/N5_mc5_sewing.tex:137:\emph{HS-sewing} if
standalone/N5_mc5_sewing.tex:170:growth $|C^{c,k}_{a,i;b,j}| \leq K(a+b+c+1)^N$ satisfies HS-sewing
standalone/N5_mc5_sewing.tex:313:The HS-sewing criterion of the next section is the device by
standalone/N5_mc5_sewing.tex:331:\begin{definition}[HS-sewing]\label{def:hs-sewing}
standalone/N5_mc5_sewing.tex:339:Say $\cA$ satisfies \emph{HS-sewing} at parameter $q \in (0,1)$ if
standalone/N5_mc5_sewing.tex:357:Suppose $\cA$ satisfies HS-sewing at parameter $q$. Then
standalone/N5_mc5_sewing.tex:405:Under HS-sewing, the connected sewing amplitudes
standalone/N5_mc5_sewing.tex:598:non-abelian chiral algebras known to satisfy HS-sewing require
standalone/N5_mc5_sewing.tex:607:\section{The general HS-sewing theorem}\label{sec:general-criterion}
standalone/N5_mc5_sewing.tex:616:\begin{theorem}[General HS-sewing criterion]
standalone/N5_mc5_sewing.tex:633:Then $\cA$ satisfies HS-sewing at every parameter
standalone/N5_mc5_sewing.tex:657:the three terms, the HS-sewing sum is bounded by
standalone/N5_mc5_sewing.tex:726:the degree). Hence $\cH_k$ satisfies HS-sewing at every
standalone/N5_mc5_sewing.tex:744:insertion of derivatives. HS-sewing at every $0 < q < 1$
standalone/N5_mc5_sewing.tex:773:HS-sewing at every $0 < q < 1$, and sector summation
standalone/N5_mc5_sewing.tex:785:HS-sewing at every $0 < q < 1$ follows, and sector summation
standalone/N5_mc5_sewing.tex:826:data and sector growth; the closed amplitudes of any HS-sewing
standalone/N5_mc5_sewing.tex:852:cone for HS-sewing amplitudes; it does not directly imply
chapters/connections/genus_complete.tex:698:HS-sewing condition (Definition~\ref{def:hs-sewing}) for mode-sum
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '7248,7288p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '7054,7076p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/genus1_seven_faces.tex | sed -n '704,716p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7248	$q \in \{e^{i\pi/3}, e^{i\pi/4}, e^{i\pi/5}\}$.
  7249	\end{proof}
  7250	
  7251	\begin{proposition}[Elliptic $R$-matrix from the genus-$1$ shadow;
  7252	\ClaimStatusProvedHere]
  7253	\label{prop:elliptic-rmatrix-shadow}
  7254	\index{R-matrix@$R$-matrix!elliptic|textbf}
  7255	\index{Belavin r-matrix@Belavin $r$-matrix|textbf}
  7256	\index{shadow connection!genus-1 deformation}
  7257	Let $E_\tau = \mathbb{C}/(\mathbb{Z} + \mathbb{Z}\tau)$ be an
  7258	elliptic curve with $\operatorname{Im}(\tau) > 0$. The bar
  7259	propagator on $E_\tau$ is
  7260	\[
  7261	\eta_{12}^{E_\tau}
  7262	= d\log E(z_1, z_2)
  7263	= \zeta_\tau(z_1 - z_2)\, d(z_1 - z_2),
  7264	\]
  7265	where $E(z,w)$ is the prime form on $E_\tau$ and $\zeta_\tau$ is
  7266	the Weierstrass zeta function for periods $(1, \tau)$.
  7267	For affine $\hat\fg_k$ with $\fg = \mathfrak{sl}_N$, the collision
 succeeded in 50ms:
   704	$\wp^{(m)}(z,\tau) \to (-1)^m(m+1)!/z^{m+2} + O(z^{-m})$.
   705	
   706	\item \textup{(KZB $\to$ KZ.)} The $dz$-component degenerates to
   707	the KZ connection: $\zeta_\tau(z_{ij}) \to 1/z_{ij}$. The
   708	$d\tau$-component has no genus-$0$ counterpart.
   709	
   710	\item \textup{(Elliptic $\to$ rational $r$-matrix.)}
   711	$r^{\mathrm{ell}}_\fg(z,\tau)/(k+h^\vee) \to
   712	k\,\Omega/((k+h^\vee)z) = \Omega/((k+h^\vee)z)$ through the
   713	intermediate trigonometric $r$-matrix:
   714	$r^{\mathrm{ell}} \to r^{\mathrm{trig}} \to r^{\mathrm{rat}}$.
   715	% AP126: level prefix mandatory; k=0 -> r=0 verified.
   716	
 succeeded in 52ms:
  7054	$z^{-(2h-1)}, z^{-(2h-3)}, \ldots, z^{-1}$, as claimed.
  7055	Computations \texttt{test\_rmatrix\_landscape.py}
  7056	and \texttt{test\_rmatrix\_poles\_comprehensive.py}
  7057	verify this for all eight standard families ($205$ tests).
  7058	\end{proof}
  7059	
  7060	\begin{proposition}[CYBE from bar-complex MC equation;
  7061	\ClaimStatusProvedHere]
  7062	\label{prop:cybe-from-mc}
  7063	\index{CYBE!from MC equation|textbf}
  7064	\index{classical Yang--Baxter equation|see{CYBE}}
  7065	\index{infinitesimal braid relation|see{CYBE}}
  7066	For affine $\hat\fg_k$ with $\fg = \mathfrak{sl}_N$,
  7067	the collision residue $r^{\mathrm{KM}}(z) = k\Omega/z$
  7068	satisfies the classical Yang--Baxter equation
  7069	\begin{equation}\label{eq:cybe-casimir}
  7070	[r_{12}(z_{12}),\, r_{13}(z_{13})]
  7071	+ [r_{12}(z_{12}),\, r_{23}(z_{23})]
  7072	+ [r_{13}(z_{13}),\, r_{23}(z_{23})]
  7073	= 0
exec
/bin/zsh -lc "rg -n 'KZ normal|trace-form|r\\"'^'"\\{KM\\}|r\\(z\\)=k\\\\Omega/z|Omega/\\\\(\\\\(k\\+h\\"'^'"\\\\vee\\)z\\\\)|kappa.*dim\\(\\\\fg\\)/2|av\\(r\\(z\\)\\)' standalone/genus1_seven_faces.tex chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:KZ normal|trace-form|r\^\{KM\}|r\(z\)=k\\Omega/z|Omega/\\(\\(k\+h\^\\vee\)z\\)|kappa.*dim\(\\fg\)/2|av\(r\(z\)\))
    ^
error: unclosed group


thinking
**Verifying chapter references**

I need to check if the chapters already use the normal references, especially around line 107. It's important for clarity and consistency. I'll look into that and make sure to report back once I verify everything. It's always good to double-check these things to avoid any confusion later on. Let's ensure everything aligns as it should!
thinking
**Considering macros and commands**

I need to address the macro commands mentioned in the seam mission. It looks like I want to compile standalones, but I’m running low on time. It might be helpful to use grep to find specific commands like `\newcommand` and `\renewcommand{\ref}`. I also need to identify any high-priority ones and check for any potential stale claims in the introduction_full_survey or survey modules. It’s worth searching for details related to analytic packages and the intro's claims on proofs and conjectures.
exec
/bin/zsh -lc "rg -n '\\\\renewcommand\\{\\\\ref\\}|\\\\renewcommand\\{\\\\Bbbk\\}|\\\\newcommand\\{\\\\cA\\}|\\\\newcommand\\{\\\\MC\\}|\\\\DeclareMathOperator\\{\\\\gr\\}|\\\\def\\\\archivebuild|\\\\def\\\\mainpreambleonly' standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'q = \\\\exp\\(2\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\)|exp\\(2\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\)|r\\"'^'"\\{\\\\mathrm\\{ell\\}\\}_\\\\fg\\(z,\\\\tau\\)/(k\\+h\\"'^'"\\\\vee)|k\\\\,\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' standalone/genus1_seven_faces.tex chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'analytic sewing package.*proved|analytic sewing.*proved|MC5|genuswise BV/BRST/bar|analytic part proved|bar-complex MC equation|topologization.*proved for affine|proved for all|derived center.*bulk|Drinfeld center equals bulk' standalone/*.tex chapters/theory/introduction.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/bp_self_duality.tex:40:\newcommand{\cA}{\mathcal{A}}
standalone/bp_self_duality.tex:44:\newcommand{\MC}{\mathrm{MC}}
standalone/N4_mc4_completion.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N4_mc4_completion.tex:41:\newcommand{\MC}{\mathrm{MC}}
standalone/N4_mc4_completion.tex:52:\DeclareMathOperator{\gr}{gr}
standalone/arithmetic_shadows.tex:91:\DeclareMathOperator{\gr}{gr}
standalone/arithmetic_shadows.tex:103:\renewcommand{\ref}[1]{%
standalone/N2_mc3_all_types.tex:35:\newcommand{\cA}{\mathcal{A}}
standalone/N2_mc3_all_types.tex:46:\newcommand{\MC}{\mathrm{MC}}
standalone/N2_mc3_all_types.tex:61:\DeclareMathOperator{\gr}{gr}
standalone/classification_trichotomy.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N5_mc5_sewing.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N5_mc5_sewing.tex:38:\newcommand{\MC}{\mathrm{MC}}
standalone/N1_koszul_meta.tex:34:\newcommand{\cA}{\mathcal{A}}
standalone/N1_koszul_meta.tex:44:\newcommand{\MC}{\mathrm{MC}}
standalone/N1_koszul_meta.tex:58:\DeclareMathOperator{\gr}{gr}
standalone/N3_e1_primacy.tex:34:\newcommand{\cA}{\mathcal{A}}
standalone/N3_e1_primacy.tex:41:\newcommand{\MC}{\mathrm{MC}}
standalone/classification.tex:38:\renewcommand{\ref}[1]{%
standalone/N6_shadow_formality.tex:33:\newcommand{\cA}{\mathcal{A}}
 succeeded in 50ms:
standalone/genus1_seven_faces.tex:76:group parameter $q = \exp(2\pi i/(k+h^\vee))$. For class~$M$
standalone/genus1_seven_faces.tex:712:k\,\Omega/((k+h^\vee)z) = \Omega/((k+h^\vee)z)$ through the
standalone/genus1_seven_faces.tex:823:$q = \exp(2\pi i/(k+h^\vee))$, and the Verlinde partition function
 succeeded in 50ms:
standalone/programme_summary.tex:2261:MC1 through MC4 are proved; MC5 is partially proved, with
standalone/programme_summary.tex:2263:and the genuswise BV/BRST/bar identification conjectural.
standalone/programme_summary.tex:2340:\subsection{MC5: analytic sewing}
standalone/survey_track_a_compressed.tex:1052:completion tower). MC5 is partially proved: the analytic HS-sewing
standalone/survey_track_a_compressed.tex:1053:package is established at all genera, while the genuswise BV/BRST/bar
standalone/cy_quantum_groups_6d_hcs.tex:233:level (the topologization theorem, proved for affine KM); without
standalone/programme_summary_sections9_14.tex:281:MC1 through MC4 are proved; MC5 is partially proved, with
standalone/programme_summary_sections9_14.tex:283:and the genuswise BV/BRST/bar identification conjectural.
standalone/programme_summary_sections9_14.tex:360:\subsection{MC5: analytic sewing}
standalone/survey_modular_koszul_duality_v2.tex:5241: & MC5 sewing, $F_g = \kappa\lambda_g^{\FP}$ (uniform)\\
standalone/survey_modular_koszul_duality_v2.tex:7655:proved; MC5 is partially proved, with the analytic HS-sewing package
standalone/survey_modular_koszul_duality_v2.tex:7656:established at all genera and the genuswise BV/BRST/bar identification
standalone/survey_modular_koszul_duality_v2.tex:7729:\medskip\noindent\textbf{MC5} (genus expansion). Partially proved.
standalone/survey_modular_koszul_duality_v2.tex:7731:with the algebraic genus tower. The full genuswise BV/BRST/bar
standalone/analytic_sewing.tex:2307:Layer~3 is proved for all standard families
standalone/analytic_sewing.tex:3004:proved for all four shadow classes,
standalone/ordered_chiral_homology.tex:560:The isomorphism \textup{(i)} $\cong$ \textup{(ii)} is classical~\cite{Drinfeld85}. The isomorphism \textup{(ii)} $\cong$ \textup{(iii)} is the spectral Drinfeld strictification \textup{(}\cite[\S III]{Lorgat26I}; proved for all simple~$\fg$\textup{)}.
standalone/theorem_index.tex:1881:proposition & \detokenize{prop:cybe-from-mc} & \detokenize{CYBE from bar-complex MC equation} & \texttt{ProvedHere} & \detokenize{chapters/examples/yangians_drinfeld_kohno.tex:7060}\\
standalone/theorem_index.tex:2115:conjecture & \detokenize{conj:standard-tower-mc5-reduction} & \detokenize{Standard-tower MC5 reduction after MC3 and realized MC4} & \texttt{Conjectured} & \detokenize{chapters/connections/editorial_constitution.tex:571}\\
standalone/survey_track_b_compressed.tex:834: & MC5 sewing, $F_g = \kappa\lambda_g^{\FP}$ (uniform)\\

thinking
**Exploring formula drift**

I need to find more formula drift by comparing similar labels. Maybe I can create a script that compares snippet sizes and detects changes between them. It seems label reuse with semantic drift could be significant for highly overlapping pairs. For example, I could identify labels where the standalone content differs greatly from chapter lines. I want to extract a few lines around each shared label and check for divergences. Calculating Levenshtein distance might be useful, but I could also just show the lines around each label for clarity.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
pairs=[('standalone/riccati.tex','chapters/theory/higher_genus_modular_koszul.tex',['eq:critical-discriminant','thm:riccati-algebraicity','eq:riccati-algebraic-relation','cor:gaussian-decomposition','eq:gaussian-decomposition','thm:single-line-dichotomy','eq:universal-factorization','eq:shadow-connection','def:shadow-growth-rate','eq:shadow-growth-rate','eq:unit-circle-criterion']),('standalone/arithmetic_shadows.tex','chapters/theory/higher_genus_modular_koszul.tex',['eq:P2','eq:P3','eq:P4','eq:P5','eq:P6','eq:verlinde-leading']),('standalone/multi_weight_cross_channel.tex','chapters/theory/higher_genus_modular_koszul.tex',['eq:multi-channel-amplitude','rem:propagator-ratio','eq:propagator-ratio','eq:w3-genus3-ratio','eq:n-degree-pattern']),('standalone/classification_trichotomy.tex','chapters/theory/three_invariants.tex',['def:p-max','eq:p-max-def','def:k-max','eq:k-max-def','def:r-max','eq:r-max-def'])]
for a,b,labels in pairs:
    print('='*120)
    print(a,'<->',b)
    A=Path(a).read_text().splitlines(); B=Path(b).read_text().splitlines()
    for label in labels:
        print('-'*80)
        print(label)
        for path,lines in [(a,A),(b,B)]:
            for i,l in enumerate(lines):
                if f'\\\\label{{{label}}}' in l:
                    start=max(0,i-2); end=min(len(lines),i+7)
                    print(f'[{path}]')
                    for j in range(start,end):
                        print(f'{j+1:6d}: {lines[j]}')
                    break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 81ms:
========================================================================================================================
standalone/riccati.tex <-> chapters/theory/higher_genus_modular_koszul.tex
--------------------------------------------------------------------------------
eq:critical-discriminant
[standalone/riccati.tex]
   132: The \emph{critical discriminant} of $L$ is
   133: \begin{equation}
   134: \label{eq:critical-discriminant}
   135:  \Delta := 8\kappa S_4 = a_0 \, a_2.
   136: \end{equation}
   137: \end{definition}
   138: 
   139: \begin{remark}
   140: The shadow metric $Q_L$ is a quadratic polynomial in~$t$,
[chapters/theory/higher_genus_modular_koszul.tex]
 17611: \end{equation}
 17612: The \emph{critical discriminant} of~$L$ is
 17613: \begin{equation}\label{eq:critical-discriminant}
 17614:  \Delta \;:=\; 8\,\kappa\,S_4
 17615:  \;=\; a_0\,a_2.

thinking
**Evaluating notation and formulas**

I’m considering whether changing notation while keeping the label the same would be an issue. I think I might need more context to see if \(\delta F_3\) is defined as a correction in the chapter. Regarding the Riccati pair, I noticed the shadow growth rate equation changed, but it's still algebraically equal. I’m also wondering about potential overlaps between standalone files and chapters, especially regarding forbidden patterns. I’ll search for any discrepancies and use targeted queries to find wrong formula patterns.
codex
I’m checking the seam for hard formula drift now, not just relabeling. The useful cases are where the standalone still carries an old normalization or obsolete notation while the chapter has already switched to the canonical lane.
exec
/bin/zsh -lc "rg -n 'S_2 *= *c/12|c/12|H_\\{N-1\\}|kappa\\(W_N\\)|T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\|\\+1|F_2 *= *1/5760|F_2 *= *7/2880|obs_g *= *kappa.*lambda_g|SC\\"'^'"\\{ch,top\\}.*E_3|Swiss-cheese.*self-dual|self-dual.*Swiss-cheese' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bulk|derived center|Drinfeld center|universal bulk|bar complex.*bulk|bar-cobar produces bulk|Omega\\(B\\(A\\)\\).*Koszul dual|bar complex.*Koszul dual|D_Ran\\(B\\(A\\)\\).*cobar' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:S_2 *= *c/12|c/12|H_\{N-1\}|kappa\(W_N\)|T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\|\+1|F_2 *= *1/5760|F_2 *= *7/2880|obs_g *= *kappa.*lambda_g|SC\^\{ch,top\}.*E_3|Swiss-cheese.*self-dual|self-dual.*Swiss-cheese)
                                                          ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
Total output lines: 1135

standalone/N3_e1_primacy.tex:170:ordered, while the closed (bulk) sector is symmetric; the
standalone/N3_e1_primacy.tex:849: In the open-closed picture this plays the role of the bulk:
standalone/N3_e1_primacy.tex:851: closed (bulk) sector. This functor is \emph{not} the bar--cobar
standalone/N3_e1_primacy.tex:865:``$\Barord(\cA)$ computes the bulk'' is category-theoretically
standalone/N3_e1_primacy.tex:866:ill-formed, because the bulk is the derived centre, not the bar.
standalone/N3_e1_primacy.tex:872:$\cA^{!}$; chiral Hochschild cochains give the bulk. The averaging map
standalone/drinfeld_kohno_bridge.tex:1258:``bulk'' side (the chiral algebra on the curve), while the
standalone/drinfeld_kohno_bridge.tex:1263:correspondence: bulk chiral algebras are Koszul dual to
standalone/cy_quantum_groups_6d_hcs.tex:124:The Drinfeld center recovers $\Etwo$-braiding, closing the $\En$
standalone/cy_quantum_groups_6d_hcs.tex:221: \Ethree(\text{bulk}) \;\to\;
standalone/cy_quantum_groups_6d_hcs.tex:224: \Etwo(\text{Drinfeld center}) \;\to\;
standalone/cy_quantum_groups_6d_hcs.tex:225: \Ethree(\text{derived center}).
standalone/cy_quantum_groups_6d_hcs.tex:230:$\Eone \to \Etwo$ is the Drinfeld center;
standalone/cy_quantum_groups_6d_hcs.tex:238:Drinfeld center carries it to $\Etwo$.  The tetrahedron equation
standalone/cy_quantum_groups_6d_hcs.tex:254:the Drinfeld center and the shadow-equals-GW identification.
standalone/cy_quantum_groups_6d_hcs.tex:293:the defect algebras, not in the bulk theory.
standalone/cy_quantum_groups_6d_hcs.tex:318:$(C^\bullet_{\mathrm{ch}}(A,A), A)$ is the boundary--bulk system.
standalone/cy_quantum_groups_6d_hcs.tex:329:at each level through the Drinfeld center.
exec
/bin/zsh -lc "rg -n '\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{conjecture\\}|ClaimStatus|proved for all|ProvedHere|Conjectured' standalone/bp_self_duality.tex standalone/analytic_sewing.tex standalone/genus1_seven_faces.tex standalone/garland_lepowsky.tex standalone/multi_weight_cross_channel.tex standalone/riccati.tex chapters/examples/bershadsky_polyakov.tex chapters/connections/genus_complete.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 953

chapters/examples/bershadsky_polyakov.tex:82:\ClaimStatusProvedElsewhere]
chapters/examples/bershadsky_polyakov.tex:144:\begin{proposition}[BP central charge;\;
chapters/examples/bershadsky_polyakov.tex:145:\ClaimStatusProvedElsewhere]
chapters/examples/bershadsky_polyakov.tex:194:\begin{proposition}[BP Koszul self-duality;\;
chapters/examples/bershadsky_polyakov.tex:195:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:258:\begin{proposition}[Modular characteristic of $\mathcal{B}^k$;\;
chapters/examples/bershadsky_polyakov.tex:259:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:291:\begin{proposition}[Complementarity;\;
chapters/examples/bershadsky_polyakov.tex:292:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:325:\begin{proposition}[T-line shadow depth;\;
chapters/examples/bershadsky_polyakov.tex:326:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:363:\begin{proposition}[J-line shadow depth;\;
chapters/examples/bershadsky_polyakov.tex:364:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:409:\begin{proposition}[Sigma non-vanishing;\;
chapters/examples/bershadsky_polyakov.tex:410:\ClaimStatusProvedHere]
chapters/examples/bershadsky_polyakov.tex:492:\begin{proposition}[Self-transpose hooks;\;
chapters/examples/bershadsky_polyakov.tex:493:\ClaimStatusProvedHere]
chapters/connections/genus_complete.tex:60:\begin{theorem}[Elliptic bar complex; \ClaimStatusProvedElsewhere{} \cite{FBZ04}]\label{thm:elliptic-bar}
exec
/bin/zsh -lc "nl -ba standalone/multi_weight_cross_channel.tex | sed -n '688,705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '23758,23778p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   688	 \frac{c}{27{,}648}
   689	 \qquad (c \to \infty),
   690	\end{equation}
   691	which is \emph{linear} in $c$, in contrast to the genus-$2$
   692	correction which approaches the constant $1/16$.
   693	The net $c$-degree of $\delta F_g^{\cross}$ increases with
   694	genus: degree $0$ at $g = 2$, degree $1$ at $g = 3$.
   695	
   696	The ratio to the scalar part reveals a dramatic shift:
   697	\begin{equation}\label{eq:w3-genus3-ratio}
   698	 \frac{\delta F_3^{\cross}(\Walg_3)}%
   699	 {\kappa(\Walg_3) \cdot \lambda_3^{\FP}}
   700	 \;\xrightarrow{\;c \to \infty\;}
   701	 \frac{42}{31}
   702	 \;\approx\; 1.35.
   703	\end{equation}
   704	At genus $3$ the cross-channel correction is already
   705	$35\%$ larger than the scalar part in the large-$c$ regime.
 succeeded in 51ms:
 23758	\end{equation}
 23759	All four numerator coefficients are positive, so
 23760	$\delta F_3(\cW_3) > 0$ for all $c > 0$.
 23761	At large~$c$:
 23762	\[
 23763	\delta F_3(\cW_3)
 23764	\;\sim\;
 23765	\frac{c}{27{,}648},
 23766	\]
 23767	which is \emph{linear} in~$c$ (net degree~$1$), in contrast
 23768	to the genus-$2$ correction which approaches
 23769	$1/16$ (net degree~$0$).
 23770	The ratio to the scalar part:
 23771	\begin{equation}\label{eq:w3-genus3-ratio}
 23772	\frac{\delta F_3(\cW_3)}%
 23773	 {\kappa(\cW_3) \cdot \lambda_3^{\mathrm{FP}}}
 23774	\;\xrightarrow{\;c \to \infty\;}
 23775	\frac{42}{31}
 23776	\;\approx\; 1.35.
 23777	\end{equation}
exec
/bin/zsh -lc "rg -n 'delta F_3\\(|delta F_3\\"'^'"\\\\cross|cross-channel correction|Theorem~\\\\ref\\{thm:multi-weight-genus-expansion\\}' chapters/theory/higher_genus_modular_koszul.tex standalone/multi_weight_cross_channel.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/multi_weight_cross_channel.tex:61:\title{Multi-weight genus expansion and cross-channel corrections}
standalone/multi_weight_cross_channel.tex:83:The cross-channel correction vanishes identically at
standalone/multi_weight_cross_channel.tex:90:$\overline{\cM}_{3,0}$; the cross-channel correction is
standalone/multi_weight_cross_channel.tex:102:channels simultaneously, and the cross-channel correction
standalone/multi_weight_cross_channel.tex:180:This paper develops the theory of the cross-channel correction
standalone/multi_weight_cross_channel.tex:193:\item The cross-channel correction vanishes identically at
standalone/multi_weight_cross_channel.tex:210: The cross-channel correction is comparable to the scalar
standalone/multi_weight_cross_channel.tex:216: gravitational cross-channel correction of $\Walg_N$
standalone/multi_weight_cross_channel.tex:226:\item The $E_1$ interpretation: the cross-channel correction
standalone/multi_weight_cross_channel.tex:261:unconditionally (possibly with a cross-channel correction term).
standalone/multi_weight_cross_channel.tex:265:% Section 2: The cross-channel correction
standalone/multi_weight_cross_channel.tex:267:\section{The cross-channel correction}\label{sec:cross-channel}
standalone/multi_weight_cross_channel.tex:367: The cross-channel correction
standalone/multi_weight_cross_channel.tex:477:controls the strength of the cross-channel correction.
standalone/multi_weight_cross_channel.tex:520:Graphs A, B, C, G contribute zero cross-channel correction:
standalone/multi_weight_cross_channel.tex:536:Graphs D, E, F carry the entire cross-channel correction.
standalone/multi_weight_cross_channel.tex:609:The cross-channel correction $\delta F_2^{\cross} = (c{+}204)/(16c)$
standalone/multi_weight_cross_channel.tex:613:The cross-channel correction is subleading at large $c$ and
standalone/multi_weight_cross_channel.tex:615:At $c = 204$, the cross-channel correction
standalone/multi_weight_cross_channel.tex:639:cross-channel corrections.

thinking
**Evaluating proof status**

I'm considering that Layer 3 is proved for all standard families and all four shadow classes, but I’m unsure if that remains valid. Maybe I need to dig deeper into whether the canonical status claims it's analytic or code-derived proof. It could be an okay conclusion. However, I wonder if the paper might overclaim full analytic realization. I should really check the specifics around lines 2300 and 3000 to clarify.
exec
/bin/zsh -lc "nl -ba standalone/analytic_sewing.tex | sed -n '2998,3010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/analytic_sewing.tex | sed -n '2298,2315p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2998	
  2999	Three layers separate the convergence statement from a complete
  3000	analytic theory: the sewing envelope for interacting algebras
  3001	(explicit Hilbert identification open), metric independence of
  3002	the ind-Hilbert factorisation (conjectural), and the coderived
  3003	shadow at $g \geq 1$ (the BV/bar comparison in~$\Dco$ is
  3004	proved for all four shadow classes,
  3005	Theorem~\ref{thm:bv-bar-coderived}).
  3006	
  3007	The coderived category is the correct receptacle for the curved
  3008	bar complex: curvature is data, not obstruction; the harmonic
  3009	discrepancy for class~M is coacyclic (divisible by the
  3010	curvature element); and the partition functions computed by
 succeeded in 51ms:
  2298	Lattice & proved & proved & proved \\
  2299	Affine KM & conjectural & conjectural & proved \\
  2300	Virasoro & conjectural & conjectural & proved \\
  2301	$\cW_N$ & conjectural & conjectural & proved \\
  2302	$\beta\gamma$ & conjectural & conjectural & conditional \\
  2303	\bottomrule
  2304	\end{tabular}
  2305	\end{center}
  2306	
  2307	Layer~3 is proved for all standard families
  2308	(Theorem~\ref{thm:bv-bar-coderived}); Layers~1 and~2 are
  2309	proved only for the abelian families (Heisenberg and lattice).
  2310	The resolution of Layers~1 and~2 for non-abelian families is
  2311	the primary open problem of the analytic sewing programme.
  2312	
  2313	\subsection{The sewing envelope as a nuclear
  2314	 space}\label{subsec:nuclear}
  2315	
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1714,1743p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '176,186p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   176	bridge from MC1 (Theorem~\ref{thm:uniform-pbw-bridge}).
   177	The remaining example-specific tasks are coefficient stabilization and
   178	H-level target identification.
   179	MC5 is not fully proved. What is proved at all genera is the analytic
   180	HS-sewing package
   181	\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
   182	$+$ subexponential sector growth implies HS-sewing convergence;
   183	Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
   184	Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
   185	identification is still conjectural; at genus~$0$ the algebraic
   186	BRST/bar comparison is proved
 succeeded in 51ms:
  1714	unitarity and partition-function data.
  1715	\end{remark}
  1716	
  1717	\begin{conjecture}[Analytic realization criterion;
  1718	\ClaimStatusConjectured]\label{conj:analytic-realization}%
  1719	\index{analytic realization criterion}%
  1720	Let $V$ be a unitary full VOA satisfying:
  1721	\begin{enumerate}[label=\textup{(\roman*)}]
  1722	\item its quasi-primary correlators satisfy conformal OS axioms
  1723	 \textup{(}in the sense of Adamo--Moriwaki--Tanimoto
  1724	 \cite{AMT24}\textup{)},
  1725	\item its graded pieces have polynomial spectral growth,
  1726	\item its intertwining OPE maps satisfy HS-sewing
  1727	 \textup{(}Definition~\textup{\ref{def:hs-sewing}}\textup{)}
  1728	 after exponential weight damping.
  1729	\end{enumerate}
  1730	Then $V$ admits a sewing envelope
  1731	$V_{\mathrm{alg}} \to V^{\mathrm{sew}} \in
  1732	\operatorname{IndHilb}$, a conformally flat 2-disk algebra~$F_V$, a
  1733	genus-zero analytic Koszul duality package, and a higher-genus

thinking
**Investigating equations and parameters**

I’m looking into the analytic sewing line 2307, and it seems alright with the main equation, which is a relief. However, I should check for seam issues in genus1_seven_faces beyond normalization. Maybe searching for a chapter equivalent will help because even if it’s not a direct duplicate, the equation label is the same. I'll also need to verify the q parameter formula, which might have different usages. Plus, I should explore whether the Yangians_drinfeld_kohno chapter uses the same q.
exec
/bin/zsh -lc "rg -n 'q = e\\"'^'"\\{|q = \\\\exp|quantum group parameter|B-cycle monodromy|Verlinde partition function|exp\\(2\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\)|e\\"'^'"\\{\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\}' chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/kac_moody.tex standalone/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/genus1_seven_faces.tex:76:group parameter $q = \exp(2\pi i/(k+h^\vee))$. For class~$M$
standalone/genus1_seven_faces.tex:117:residue encodes the quantum group parameter.
standalone/genus1_seven_faces.tex:161:$q = e^{2\pi i\tau} \to 0$ (Theorem~\ref{thm:degeneration}).
standalone/genus1_seven_faces.tex:696:$q = e^{2\pi i\tau} \to 0$), all seven genus-$1$ faces degenerate to
standalone/genus1_seven_faces.tex:822:coefficient. The quantum group parameter is
standalone/genus1_seven_faces.tex:823:$q = \exp(2\pi i/(k+h^\vee))$, and the Verlinde partition function
standalone/genus1_seven_faces.tex:847:$q = e^{2\pi i/(k+2)}$ is a root of unity. The passage from the
chapters/examples/kac_moody.tex:161:$q = e^{\pi i/(k+h^\vee)}$
chapters/examples/kac_moody.tex:2377:BGG reciprocity for $\mathcal{O}_k(\widehat{\mathfrak{g}})$ states $[P_k(\lambda) : M_k(\mu)] = [M_k(\mu) : L_k(\lambda)]$. On the non-semisimple lift of the KL correspondence at $q = e^{\pi i/(k+h^\vee)}$, this maps to quantum group reciprocity:
chapters/examples/kac_moody.tex:2389:integer and set $q = e^{\pi i/(k + h^\vee)}$. Then:
chapters/examples/kac_moody.tex:2394:\item The Kazhdan--Lusztig quantum group parameter for the dual level is
chapters/examples/kac_moody.tex:2416:q = e^{\pi i/(k + h^\vee)},
chapters/examples/kac_moody.tex:2483:$k$ & Simple objects & $|P^k_+|$ & $q = e^{\pi i/(k+2)}$ \\
chapters/examples/kac_moody.tex:2500:\quad\text{at } q = e^{\pi i/(k+2)}
chapters/examples/kac_moody.tex:3919:where $c = 3k/(k+2)$ is the central charge of $\widehat{\mathfrak{sl}}_{2,k}$ and $q = e^{2\pi i \tau}$.
chapters/examples/kac_moody.tex:4177:where $q = e^{\pi i/(k+h^\vee)} = e^{\pi i q/p}$.
chapters/examples/kac_moody.tex:4238:\emph{Remaining} (Conjecture~\ref{conj:kl-periodic-cdg}): the CDG periodicity $\barB^{n+2q} \cong \barB^n$ at root-of-unity $q = e^{\pi i/(k+h^\vee)}$. Computational evidence: $N$-complex structure of $\mathfrak{u}_q(\mathfrak{sl}_2)$ verified at $74$~tests ($d_q^N = 0$, $d_q^2 \neq 0$ for $N \geq 3$).
chapters/examples/kac_moody.tex:4245:At admissible $k = -h^\vee + p/q$ with $q = e^{\pi i/(k+h^\vee)}$ a primitive $N$-th root ($N = 2q$), the bar complex is an $N$-complex (Kapranov~\cite{Kapranov96}): $d^N = 0$ but $d^2 \neq 0$. The framework of \cite{Kapranov96} and Khovanov--Qi~\cite{KQ20} provides: (i) cohomology groups $H^{(j)}$ for $0 \leq j \leq N-1$; (ii) quantum group categorification via $N$-complexes; (iii) faithful braid group actions on derived categories of $N$-complexes, potentially realizing the braided structure of $\mathcal{C}(U_q(\fg))$.
chapters/examples/yangians_drinfeld_kohno.tex:10:$q = e^{\pi i/(k + h^\vee)}$. The bar-cobar framework reveals this as
chapters/examples/yangians_drinfeld_kohno.tex:165:$q = e^{\pi i/(k + h^\vee)}$, and $k' = -k - 2h^\vee$
exec
/bin/zsh -lc "nl -ba standalone/genus1_seven_faces.tex | sed -n '812,826p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '7336,7394p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   812	For $\cA = \widehat{\fg}_k$ at integer level $k \geq 1$, the $B$-cycle
   813	monodromy of the KZB connection is
   814	\begin{equation}\label{eq:b-monodromy}
   815	\mathcal{M}_B
   816	\;=\;
   817	\exp\Bigl(\frac{2\eta_\tau}{k+h^\vee}\,\Omega\Bigr)
   818	\;=\;
   819	\exp\bigl(2\eta_\tau \cdot c_0\bigr),
   820	\end{equation}
   821	where $c_0 = \Omega/(k+h^\vee)$ is the degree-$0$ collision
   822	coefficient. The quantum group parameter is
   823	$q = \exp(2\pi i/(k+h^\vee))$, and the Verlinde partition function
   824	at genus~$1$ is
   825	\begin{equation}\label{eq:verlinde-g1}
   826	Z_1(\widehat{\fg}_k)
 succeeded in 52ms:
  7336	$\pi \cot(\pi z/L) \to L/z$, recovering
  7337	$r^{\mathrm{rat}}(z) = k\Omega/z$.
  7338	Both limits are verified numerically in
  7339	\texttt{elliptic\_rmatrix\_shadow.py}:
  7340	the relative error $\|r^{\mathrm{ell}} - r^{\mathrm{trig}}\|/\|r^{\mathrm{trig}}\|$
  7341	decreases monotonically with
  7342	$\operatorname{Im}(\tau)$ and is $< 10^{-6}$ at
  7343	$\operatorname{Im}(\tau) = 12$ (function
  7344	\texttt{elliptic\_to\_trigonometric\_limit}).
  7345	
  7346	The identification~\eqref{eq:shadow-metric-wp}: the shadow metric
  7347	$Q^{(g)}_\cA$ at genus~$g$ is the curvature of the shadow connection
  7348	on $\overline{\mathcal{M}}_{g,n}$. At genus~$1$, the moduli space
  7349	$\mathcal{M}_{1,1}$ is parametrized by $(z, \tau)$. The $z$-dependence of
  7350	the connection involves $\zeta_\tau(z)$; its derivative
  7351	$-\zeta_\tau'(z) = \wp(z, \tau)$ is the curvature in the
  7352	$z$-direction, which is the shadow metric component.
  7353	
  7354	The classical YBE for $r^{\mathrm{ell}}$ is verified numerically
  7355	in \texttt{elliptic\_rmatrix\_shadow.py}, function


thinking
**Analyzing q drift**

I'm confirming there's a q drift — the chapter uses q = e^{π i/(k+h∨)} generally, while the standalone version uses 2π. Now, line 7857 says q = e^{2π i/(k+2)}, which might be for U_q. I really need to inspect the context around lines 7523 and 7857. The top of the chapter mentions q = e^{π i/(k+h∨)}. It feels like there could be some inconsistency, especially since we're looking for a clear convention to report on for the user.
thinking
**Correcting standalone lines**

I need to fix standalone lines 76, 823, and 847 to use `q = exp(\pi i/(k+h^\vee))`, or at least add an explicit statement if I'm gonna use \(q^2\). It feels important to verify this with the surrounding context, especially in line 847, to ensure consistency. I'll take a closer look at that line and make sure everything aligns properly. Getting these details right is crucial for clarity!
exec
/bin/zsh -lc "nl -ba standalone/genus1_seven_faces.tex | sed -n '842,850p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   842	group]\label{rem:quantum-group}
   843	The quasi-periodicity~\eqref{eq:B-cycle-monodromy} of the genus-$1$
   844	collision residue is the geometric origin of the quantum group
   845	parameter. For affine $\widehat{\fsl}_{2,k}$: the $B$-cycle monodromy
   846	eigenvalues are $q^{j(j+1)}$ for $j = 0, 1/2, \ldots, k/2$, where
   847	$q = e^{2\pi i/(k+2)}$ is a root of unity. The passage from the
   848	$E_1$ collision residue $r^{(1)}(z,\tau)$ to the quantum group
   849	$U_q(\fg)$ is the $B$-cycle monodromy of the ordered bar complex:
   850	the spectral parameter $z$ (genus-$0$ data) becomes the quantum
exec
/bin/zsh -lc "python3 - <<'PY'
import re, glob
pairs=[('standalone/analytic_sewing.tex','chapters/connections/genus_complete.tex'),('standalone/bp_self_duality.tex','chapters/examples/bershadsky_polyakov.tex'),('standalone/garland_lepowsky.tex','chapters/examples/kac_moody.tex'),('standalone/riccati.tex','chapters/theory/higher_genus_modular_koszul.tex'),('standalone/multi_weight_cross_channel.tex','chapters/theory/higher_genus_modular_koszul.tex'),('standalone/classification_trichotomy.tex','chapters/theory/three_invariants.tex')]
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
begin_re=re.compile(r'\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|conjecture|computation)\\}(?:\\[(.*?)\\])?')
for a,b in pairs:
    print('PAIR',a,'<->',b)
    texta=open(a).read().splitlines(); textb=open(b).read().splitlines()
    # map labels to nearest preceding begin line within 5 lines and inline title
    def envmap(lines):
        out={}
        last=[]
        for i,l in enumerate(lines,1):
            m=begin_re.search(l)
            if m:
                last=[i,m.group(1),m.group(2) or '']
            for lm in label_re.finditer(l):
                out[lm.group(1)] = tuple(last) if last else None
        return out
    ea=envmap(texta); eb=envmap(textb)
    shared=sorted(set(ea)&set(eb))
    for label in shared:
        A=ea[label]; B=eb[label]
        if A"'!=B:
            print('"' ',label,'|',A,'|',B)
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
PAIR standalone/analytic_sewing.tex <-> chapters/connections/genus_complete.tex
  def:analytic-koszul-pair | (2822, 'definition', 'Analytic Koszul pair') | (1588, 'definition', 'Analytic Koszul pair')
  def:hs-sewing | (679, 'definition', 'HS-sewing') | (1358, 'definition', 'HS-sewing condition')
  def:sewing-envelope | (449, 'definition', 'Sewing envelope') | (1312, 'definition', 'Sewing envelope')
  eq:connected-free-energy | (777, 'corollary', 'Gram positivity') | (1795, 'definition', 'Connected genus-$1$ free energy')
  eq:heisenberg-fredholm | (1136, 'theorem', 'One-particle sewing') | (1477, 'theorem', '')
  eq:hs-sewing | (679, 'definition', 'HS-sewing') | (1358, 'definition', 'HS-sewing condition')
  thm:general-hs-sewing | (1772, 'theorem', 'General HS-sewing criterion') | (1389, 'theorem', 'General HS-sewing criterion; \\ClaimStatusProvedHere')

PAIR standalone/bp_self_duality.tex <-> chapters/examples/bershadsky_polyakov.tex
  eq:bp-central-charge | (151, 'proposition', 'BP central charge') | (144, 'proposition', '')
  eq:bp-ope-bosonic | (178, 'remark', 'Admissible-level check') | (81, 'definition', '')
  prop:bp-central-charge | (151, 'proposition', 'BP central charge') | (144, 'proposition', '')

PAIR standalone/garland_lepowsky.tex <-> chapters/examples/kac_moody.tex
  eq:km-rmatrix | (961, 'remark', 'The collision residue') | (718, 'remark', 'Collision-residue $r$-matrix for $\\hat\\fg_k$')
  rem:sl2-admissible | (1026, 'remark', '') | (3812, 'remark', 'Admissible levels')

PAIR standalone/riccati.tex <-> chapters/theory/higher_genus_modular_koszul.tex
  cor:gaussian-decomposition | (330, 'corollary', 'Gaussian decomposition') | (17715, 'corollary', 'Gaussian decomposition')
exec
/bin/zsh -lc 'for f in standalone/analytic_sewing.tex standalone/bp_self_duality.tex standalone/garland_lepowsky.tex standalone/genus1_seven_faces.tex standalone/multi_weight_cross_channel.tex standalone/classification_trichotomy.tex standalone/ordered_chiral_homology.tex standalone/introduction_full_survey.tex standalone/riccati.tex standalone/arithmetic_shadows.tex; do echo "FILE $f"; rg -n '"'\\\\newcommand|\\\\renewcommand\\{\\\\ref\\}|\\\\renewcommand\\{\\\\Bbbk\\}|\\\\DeclareMathOperator' \""'$f"; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE standalone/analytic_sewing.tex
37:\newcommand{\cA}{\mathcal{A}}
38:\newcommand{\cB}{\mathcal{B}}
39:\newcommand{\cC}{\mathcal{C}}
40:\newcommand{\cD}{\mathcal{D}}
41:\newcommand{\cF}{\mathcal{F}}
42:\newcommand{\cH}{\mathcal{H}}
43:\newcommand{\cK}{\mathcal{K}}
44:\newcommand{\cL}{\mathcal{L}}
45:\newcommand{\cM}{\mathcal{M}}
46:\newcommand{\cO}{\mathcal{O}}
47:\newcommand{\cS}{\mathcal{S}}
48:\newcommand{\cV}{\mathcal{V}}
49:\newcommand{\cW}{\mathcal{W}}
50:\newcommand{\cZ}{\mathcal{Z}}
51:\newcommand{\bC}{\mathbb{C}}
52:\newcommand{\bN}{\mathbb{N}}
53:\newcommand{\bR}{\mathbb{R}}
54:\newcommand{\bZ}{\mathbb{Z}}
55:\newcommand{\barB}{\bar{B}}
exec
/bin/zsh -lc "nl -ba standalone/bp_self_duality.tex | sed -n '36,50p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '96,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '36,58p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    36	\newcommand{\fg}{\mathfrak{g}}
    37	\newcommand{\fh}{\mathfrak{h}}
    38	\newcommand{\fn}{\mathfrak{n}}
    39	\newcommand{\fsl}{\mathfrak{sl}}
    40	\newcommand{\cA}{\mathcal{A}}
    41	\newcommand{\cB}{\mathcal{B}}
    42	\newcommand{\cW}{\mathcal{W}}
    43	\newcommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
    44	\newcommand{\MC}{\mathrm{MC}}
    45	\newcommand{\Sh}{\mathrm{Sh}}
    46	\newcommand{\Res}{\operatorname{Res}}
    47	\newcommand{\DS}{\mathrm{DS}}
    48	\newcommand{\Vir}{\mathrm{Vir}}
    49	\DeclareMathOperator{\rk}{rk}
    50	\DeclareMathOperator{\ad}{ad}
 succeeded in 51ms:
    96	\providecommand{\SCchtop}{\mathrm{SC}^{\mathrm{ch,top}}}
    97	
    98	\DeclareMathOperator{\gr}{gr}
    99	\DeclareMathOperator{\rk}{rk}
   100	\DeclareMathOperator{\depth}{depth}
   101	\DeclareMathOperator{\Spec}{Spec}
   102	
   103	\numberwithin{equation}{section}
   104	
   105	\makeatletter
   106	\let\svy@oldref\ref
   107	\renewcommand{\ref}[1]{%
   108	 \@ifundefined{r@#1}{\textit{full monograph}}{\svy@oldref{#1}}%
   109	}
   110	\makeatother
 succeeded in 51ms:
    36	% ================================================================
    37	% Macros
    38	% ================================================================
    39	\newcommand{\cA}{\mathcal{A}}
    40	\newcommand{\cB}{\mathcal{B}}
    41	\newcommand{\cC}{\mathcal{C}}
    42	\newcommand{\cD}{\mathcal{D}}
    43	\newcommand{\cF}{\mathcal{F}}
    44	\newcommand{\cH}{\mathcal{H}}
    45	\newcommand{\cM}{\mathcal{M}}
    46	\newcommand{\cO}{\mathcal{O}}
    47	\newcommand{\cL}{\mathcal{L}}
    48	\newcommand{\cW}{\mathcal{W}}
    49	\newcommand{\cP}{\mathcal{P}}
    50	\newcommand{\cZ}{\mathcal{Z}}
    51	
    52	\newcommand{\Ran}{\mathrm{Ran}}
    53	\newcommand{\MC}{\mathrm{MC}}
    54	\newcommand{\HH}{\mathrm{HH}}
    55	\newcommand{\CE}{\mathrm{CE}}

thinking
**Exploring macros and commands**

I’m noticing that the introduction_full_survey seems to already utilize providecommand for SCchtop, which is interesting. I’m wondering if there are some macros being guarded but not others? Maybe I should consider opening more top lines to clarify this. It feels like there’s something valuable to uncover here, and I’m curious about how these commands and macros interact to enhance functionality. Let's see what I can deduce!
exec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '70,100p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    70	\providecommand{\Etwo}{E_2}
    71	\providecommand{\Einf}{E_\infty}
    72	\providecommand{\En}{E_n}
    73	\providecommand{\Pinf}{P_\infty}
    74	\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
    75	\providecommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
    76	\providecommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
    77	\providecommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
    78	\providecommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}
    79	\providecommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
    80	\providecommand{\Convinf}{\mathrm{Conv}_\infty}
    81	\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
    82	\providecommand{\Ass}{\mathrm{Ass}}
    83	\providecommand{\Com}{\mathrm{Com}}
    84	\providecommand{\Dg}{\mathrm{dg}}
    85	\providecommand{\CompCl}{\mathrm{CompCl}}
    86	\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
    87	\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
    88	\providecommand{\Gmod}{\mathfrak{G}^{\mathrm{mod}}}
    89	\providecommand{\Fft}{\mathrm{Fft}}
codex
I’m verifying the macro failures against the main manuscript surface, not treating `\newcommand` as bad in the abstract. The question is whether those standalone preambles collide with definitions the main manuscript already owns.
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\cA\\}|\\\\(providecommand|newcommand)\\{\\\\MC\\}|\\\\DeclareMathOperator\\{\\\\gr\\}|\\\\newcommand\\{\\\\Vir\\}|\\\\providecommand\\{\\\\Vir\\}|\\\\newcommand\\{\\\\Res\\}|\\\\providecommand\\{\\\\Res\\}' main.tex preamble.tex macros.tex setup.tex chapters standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: preamble.tex: No such file or directory (os error 2)
rg: macros.tex: No such file or directory (os error 2)
rg: setup.tex: No such file or directory (os error 2)
standalone/N5_mc5_sewing.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N5_mc5_sewing.tex:38:\newcommand{\MC}{\mathrm{MC}}
standalone/N5_mc5_sewing.tex:41:\newcommand{\Vir}{\mathrm{Vir}}
standalone/N5_mc5_sewing.tex:42:\newcommand{\Res}{\mathrm{Res}}
standalone/N3_e1_primacy.tex:34:\newcommand{\cA}{\mathcal{A}}
standalone/N3_e1_primacy.tex:41:\newcommand{\MC}{\mathrm{MC}}
standalone/N3_e1_primacy.tex:47:\newcommand{\Res}{\mathrm{Res}}
standalone/N3_e1_primacy.tex:57:\newcommand{\Vir}{\mathrm{Vir}}
standalone/N4_mc4_completion.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N4_mc4_completion.tex:41:\newcommand{\MC}{\mathrm{MC}}
standalone/N4_mc4_completion.tex:45:\newcommand{\Res}{\mathrm{Res}}
standalone/N4_mc4_completion.tex:49:\newcommand{\Vir}{\mathrm{Vir}}
standalone/N4_mc4_completion.tex:52:\DeclareMathOperator{\gr}{gr}
standalone/N1_koszul_meta.tex:34:\newcommand{\cA}{\mathcal{A}}
standalone/N1_koszul_meta.tex:44:\newcommand{\MC}{\mathrm{MC}}
standalone/N1_koszul_meta.tex:49:\newcommand{\Res}{\mathrm{Res}}
standalone/N1_koszul_meta.tex:53:\newcommand{\Vir}{\mathrm{Vir}}
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '688,708p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'repoinput|mainpreambleonly|archivebuild|providecommand' standalone/editorial.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   688	\providecommand{\Cstr}{\mathsf{C}_{\mathrm{str}}^{\wedge}}
   689	\providecommand{\CE}{\mathrm{CE}}
   690	\providecommand{\fib}{\operatorname{fib}}
   691	\providecommand{\cofib}{\operatorname{cofib}}
   692	\providecommand{\CoDer}{\operatorname{CoDer}}
   693	
   694	% Standalone-paper macros (ordered chiral homology insertion)
   695	\providecommand{\RR}{\mathbb{R}}
   696	\providecommand{\ZZ}{\mathbb{Z}}
   697	\providecommand{\PP}{\mathbb{P}}
   698	\providecommand{\HHH}{\mathbb{H}}
   699	\providecommand{\Barord}{\overline{B}^{\mathrm{ord}}}
   700	\providecommand{\BarSig}{\overline{B}^{\Sigma}}
   701	\providecommand{\Barch}{\overline{B}^{\mathrm{ch}}}
   702	\providecommand{\Sym}{\mathrm{Sym}}
   703	\providecommand{\Pthree}{\mathsf{P}_{3}}
   704	\providecommand{\gmod}{\mathfrak{g}^{\mathrm{mod}}_{\cA}}
   705	\providecommand{\gEone}{\mathfrak{g}^{\mathsf{E}_{1}}_{\cA}}
   706	\providecommand{\Ainf}{A_{\infty}}
   707	\providecommand{\Eone}{\mathsf{E}_{1}}
 succeeded in 51ms:
standalone/editorial.tex:2:\def\archivebuild{1}
standalone/editorial.tex:3:\def\mainpreambleonly{1}
standalone/editorial.tex:6:\newcommand{\repoinput}[1]{%
standalone/editorial.tex:14:\repoinput{chapters/connections/concordance}
standalone/editorial.tex:15:\repoinput{chapters/connections/editorial_constitution}
standalone/editorial.tex:17:\repoinput{bibliography/references}
main.tex:143:% Override: make archive passes \def\archivebuild{1} to enable full content.
main.tex:144:\ifdefined\archivebuild
main.tex:307:\providecommand*{\toclevel@theorem}{2}
main.tex:308:\providecommand*{\toclevel@lemma}{2}
main.tex:309:\providecommand*{\toclevel@proposition}{2}
main.tex:310:\providecommand*{\toclevel@corollary}{2}
main.tex:311:\providecommand*{\toclevel@verification}{2}
main.tex:312:\providecommand*{\toclevel@computation}{2}
main.tex:313:\providecommand*{\toclevel@definition}{2}
main.tex:314:\providecommand*{\toclevel@example}{2}
main.tex:315:\providecommand*{\toclevel@remark}{2}
main.tex:317:\providecommand*{\toclevel@conjecture}{2}
main.tex:318:\providecommand*{\toclevel@notation}{2}
main.tex:319:\providecommand*{\toclevel@convention}{2}

thinking
**Investigating theorem labels**

It seems the label `eq:shadow-connection` isn't actually part of the theorem. I should search whether the theorem or property labels are aligned, but `thm:riccati-algebraicity` and `thm:single-line-dichotomy` share the same labels as the chapter. There’s no issue here except for the missing ClaimStatus. Maybe I can gather missing statuses on certain theorem labels, but if the user wants inconsistencies, I'll need to review `standalone/analytic_sewing.tex` to locate exact issues. It might be a deeper inspection than I expected!
exec
/bin/zsh -lc "nl -ba standalone/bp_self_duality.tex | sed -n '186,204p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/bershadsky_polyakov.tex | sed -n '112,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'eq:bp-ope-bosonic|eq:bp-ope-TT' standalone/bp_self_duality.tex chapters/examples/bershadsky_polyakov.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   186	\subsection{OPE data}
   187	
   188	The OPE of $\cB^k$ is that of the $N{=}2$ superconformal algebra in
   189	the Kazama--Suzuki normalization. The bosonic sector is:
   190	\begin{align}\label{eq:bp-ope-bosonic}
   191	 T_{(3)}T &= \tfrac{c}{2}, &
   192	 T_{(1)}T &= 2T, &
   193	 T_{(0)}T &= \partial T, \notag\\
   194	 J_{(1)}J &= k_{\mathrm{res}}, &
   195	 J_{(0)}J &= 0, &
   196	 T_{(1)}J &= J.
   197	\end{align}
   198	The fermionic sector:
   199	\begin{align}\label{eq:bp-ope-fermionic}
   200	 G^+_{(2)}G^- &= \tfrac{2c}{3}, &
   201	 G^+_{(1)}G^- &= 2J, &
   202	 G^+_{(0)}G^- &= 2T + \partial J, \notag\\
   203	 G^-_{(2)}G^+ &= \tfrac{2c}{3}, &
   204	 G^-_{(1)}G^+ &= -2J, &
 succeeded in 51ms:
   112	\end{definition}
   113	
   114	The bosonic OPE data ($T$, $J$ bosonic):
   115	\begin{align}
   116	T_{(3)}T &= \tfrac{c}{2}, &
   117	T_{(1)}T &= 2T, &
   118	T_{(0)}T &= \partial T,
   119	\label{eq:bp-ope-TT} \\
   120	J_{(1)}J &= k_{\mathrm{res}}, &
   121	J_{(0)}J &= 0, &
   122	T_{(1)}J &= J.
   123	\label{eq:bp-ope-bosonic}
   124	\end{align}
   125	The fermionic OPE data:
   126	\begin{align}
   127	G^+_{(2)}G^- &= \tfrac{2c}{3}, &
   128	G^+_{(1)}G^- &= 2J, &
   129	G^+_{(0)}G^- &= 2T + \partial J,
   130	\label{eq:bp-ope-GpGm} \\
 succeeded in 51ms:
standalone/bp_self_duality.tex:190:\begin{align}\label{eq:bp-ope-bosonic}
chapters/examples/bershadsky_polyakov.tex:119:\label{eq:bp-ope-TT} \\
chapters/examples/bershadsky_polyakov.tex:123:\label{eq:bp-ope-bosonic}
chapters/examples/bershadsky_polyakov.tex:119:\label{eq:bp-ope-TT} \\
chapters/examples/bershadsky_polyakov.tex:123:\label{eq:bp-ope-bosonic}


thinking
**Looking for inconsistencies**

I'm planning to search for `q = exp(2πi/(k+h∨))` in the survey. There might be more seam drift to consider. It could be worthwhile to report findings from a genus1 paper. I'll look across different files to find occurrences of 2π and root-of-unity. I remember the user asked me to carefully read transition points and note any inconsistencies, mismatches, or gaps at the seams. This is a detailed task that requires attention!
thinking
**Analyzing parameter drift**

I think it could be useful to gather all occurrences of the q parameter drift within the same standalone file, particularly looking at lines 76, 823, and 847. That’s a good start! I also see potential issues in `analytic_sewing`, like duplicated conjecture with `def:analytic-koszul-pair` and `conj:analytic-realisation`. This seems to represent a seam issue, and I could report one finding there. I wonder if I should separate two findings related to `hs-sewing` as well. I could also check `N5_mc5_sewing` for similar older definitions. Time to inspect further!
exec
/bin/zsh -lc "nl -ba standalone/N5_mc5_sewing.tex | sed -n '331,345p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N5_mc5_sewing.tex | sed -n '612,636p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'connected free energy|eq:connected-free-energy|analytic Koszul pair|analytic realization|Quillen equivalence' standalone/N5_mc5_sewing.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   331	\begin{definition}[HS-sewing]\label{def:hs-sewing}
   332	Let $\cA_{\mathrm{alg}} = \bigoplus_n H_n$ be an algebraic chiral
   333	core with pre-Hilbert structure on each sector (for example, the
   334	invariant form restricted to $H_n$). Write the pair-of-pants
   335	sector multiplications as
   336	\[
   337	m_{a,b}^c \colon H_a \otimes H_b \longrightarrow H_c.
   338	\]
   339	Say $\cA$ satisfies \emph{HS-sewing} at parameter $q \in (0,1)$ if
   340	\begin{equation}\label{eq:hs-sewing}
   341	\sum_{a,b,c \geq 0} q^{a+b+c}\,
   342	\|m_{a,b}^c\|_{\HS}^2
   343	\;<\; \infty.
   344	\end{equation}
   345	The \emph{weighted completion} is
 succeeded in 51ms:
   612	growth of the structure constants and subexponential growth of
   613	the sector dimensions. Both hypotheses can be read off from
   614	character formulas and OPE tables.
   615	
   616	\begin{theorem}[General HS-sewing criterion]
   617	\label{thm:general-hs-sewing}
   618	Let $\cA$ be a positive-energy chiral algebra with a choice of
   619	pre-Hilbert structure on each sector $H_n$. Suppose
   620	\begin{enumerate}[label=\textup{(\roman*)}]
   621	\item (\textbf{subexponential sector growth})
   622	$\log\dim H_n = o(n)$, equivalently
   623	$\dim H_n \leq C e^{\alpha\sqrt{n}}$ for some
   624	$C, \alpha > 0$;
   625	\item (\textbf{polynomial OPE coefficient growth}) there exist
   626	constants $K > 0$ and $N \geq 0$ such that the matrix elements
   627	of $m_{a,b}^c$ in orthonormal bases satisfy
   628	\[
   629	|C^{c,k}_{a,i;\,b,j}| \;\leq\; K(a + b + c + 1)^N
   630	\]
   631	for all weights $a, b, c$ and all basis indices $i, j, k$.
 exited 1 in 51ms:



thinking
**Investigating potential issues**

I’m considering if there might be some seam drift if it isn't clearly marked as uniform. I should search line 5241 since there might be a lack of the AP32 weight tag. The table does mention uniform in a row, though. I could also search for “derived center equals bulk” labels throughout the standalones and chapters to double-check. However, it seems like it should be okay overall.
thinking
**Inspecting mathematical context**

I'm considering whether line 842 states `F_1(V_k(g)) = -dim(g)(k+h^\vee)/(2h^\vee)`. But I recall that canonical F_1 should be κ/24 and not negative. I think I need to inspect the context because this might not be the same F1. It's important to search the lines around 836-845, as it could be a serious issue if the standalone value has the wrong coefficient compared to the main equation. I should also check the chapter counterpart for any corrections.
codex
I’m looking for formula drift inside the example standalones now. The seam failures are only worth reporting if the standalone still says something mathematically different from the chapter, not just shorter.
exec
/bin/zsh -lc "nl -ba standalone/garland_lepowsky.tex | sed -n '836,848p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'F_1\\(|F_1 =|1/24|1/12|kappa\\(\\ghat_k\\)|kappa\\(V_k\\(\\\\fg\\)\\)' standalone/garland_lepowsky.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:F_1\(|F_1 =|1/24|1/12|kappa\(\ghat_k\)|kappa\(V_k\(\\fg\)\))
                                    ^^
error: unrecognized escape sequence
 succeeded in 52ms:
   836	\kappa \cdot \lambda_1$, where $\lambda_1$ is the first
   837	Chern class of the Hodge bundle on $\overline{\mathcal{M}}_{1,1}$.
   838	For the affine vertex algebra, the genus-$1$ partition
   839	function trace gives $F_1 = -\kappa \cdot \log\eta(\tau)$
   840	where $\eta(\tau) = q^{1/24}\prod_{n \geq 1}(1-q^n)$.
   841	Comparing with the explicit computation
   842	$F_1(V_k(\fg)) = -\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}
   843	\cdot \log\eta(\tau)$, we read off~\eqref{eq:kappa-km}.
   844	
   845	The complementarity sum is
   846	$\kappa(\ghat_k) + \kappa(\ghat_{k'})
   847	= \frac{\dim\fg}{2h^\vee}[(k{+}h^\vee) + (-k{-}2h^\vee{+}h^\vee)]
   848	= \frac{\dim\fg}{2h^\vee} \cdot 0 = 0$.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '836,850p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   836	 \quad \text{($8$ currents, $\dim\Omega^0 = 1$)} \\
   837	\dim(\bar{B}^2) &= 64 \cdot 1 = 64
   838	 \quad \text{($8^2$ ordered pairs, $\dim\Omega^1 = 1$)} \\
   839	\dim(\bar{B}^3) &= 512 \cdot 2 = 1024
   840	 \quad \text{($8^3$ ordered triples, $\dim\Omega^2 = 2$)}
   841	\end{align}
   842	The cubic growth $\dim(\bar{B}^n) \sim 8^n$ reflects the $8$-dimensional adjoint representation of $\mathfrak{sl}_3$; the Orlik--Solomon factor $(n-1)!$ accounts for independent logarithmic forms on $\overline{C}_n$.
   843	\end{computation}
   844	
   845	\begin{lemma}[Bar chain groups are level-independent; \ClaimStatusProvedHere]%
   846	\label{lem:bar-dims-level-independent}
   847	\index{bar complex!level-independence}
   848	The dimensions $\dim(\bar{B}^n(\widehat{\mathfrak{g}}_k))$ depend on
   849	$\mathfrak{g}$ but are \emph{independent of the level~$k$}. This is
   850	immediate from the construction: the bar chain groups
exec
/bin/zsh -lc "rg -n 'k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|q = e\\"'^'"\\{\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\}|q = e\\"'^'"\\{2\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\}|topologization|SC\\"'^'"\\{ch,top\\}.*derived center|bar complex itself is not' standalone/ordered_chiral_homology.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/ordered_chiral_homology.tex:278:topologization package that the ordered picture feeds but
standalone/ordered_chiral_homology.tex:440:\begin{theorem}[Derived centre, topologization, and
standalone/ordered_chiral_homology.tex:461:\item \textup{(Affine topologization at non-critical level.)}
standalone/ordered_chiral_homology.tex:1506:Only affine topologization with conformal vector raises
standalone/ordered_chiral_homology.tex:1706:    $r(z) = k\Omega/z$ \textup{(}trace-form\textup{)},
standalone/ordered_chiral_homology.tex:2639:  $r(z) = k\Omega/z$; at $k = 0$, $r = 0$; at
standalone/ordered_chiral_homology.tex:4617:and affine topologization]
standalone/ordered_chiral_homology.tex:4640:\item \textup{(Scope and topologization boundary.)} For
standalone/ordered_chiral_homology.tex:4646:  translations $Q$-exact, the affine topologization theorem
standalone/ordered_chiral_homology.tex:4702:\begin{warning}[The bar complex itself is not $\Ethree$]
standalone/ordered_chiral_homology.tex:4824:\subsection{Explicit $\Ethree$ operations, topologization,
standalone/ordered_chiral_homology.tex:4999:topologization of the derived centre.
standalone/ordered_chiral_homology.tex:5068:topologization, conformal vector at non-critical level)
standalone/ordered_chiral_homology.tex:5074:\begin{warning}[The bar complex itself is not $\Ethree$]
standalone/ordered_chiral_homology.tex:5154:$r(z) = k\Omega/z$ (at $k = 0$, $r = 0$);
chapters/theory/en_koszul_duality.tex:23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
chapters/theory/en_koszul_duality.tex:24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
chapters/theory/en_koszul_duality.tex:27:The topologization proof is made constructive by an explicit
chapters/theory/en_koszul_duality.tex:1302:  topologization theorem
chapters/theory/en_koszul_duality.tex:1303:  (Theorem~\textup{\ref{thm:topologization}}).
exec
/bin/zsh -lc "rg -n 'conj:v1-drinfeld-center-equals-bulk|drinfeld center equals bulk|derived center equals bulk' standalone/ordered_chiral_homology.tex chapters/theory/introduction.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'full Swiss-cheese algebra|Swiss-cheese structure emerges|bar complex.*not.*E_3|derived center pair' standalone/ordered_chiral_homology.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:6660:derived center pair
chapters/theory/ordered_associative_chiral_kd.tex:1825:equip the ordered bar complex with a full Swiss-cheese algebra
 succeeded in 51ms:
chapters/frame/preface.tex:3820:Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}
chapters/frame/preface.tex:3954:\begin{conjecture}\label{conj:v1-drinfeld-center-equals-bulk}

thinking
**Evaluating formula synchronization**

I don't see any immediate formula mismatches. It seems like the ordered chiral homology is synced with the SC warning. Maybe I should search for standalone survey files with something like `q = exp(2π i/(k+h∨))` or consider other aspects of root-of-unity drift. I’ll also look into using rg to compare standalone data versus chapters. There’s a lot to consider here!
exec
/bin/zsh -lc 'for f in standalone/programme_summary_section1.tex standalone/programme_summary_sections2_4.tex standalone/programme_summary_sections5_8.tex standalone/programme_summary_sections9_14.tex; do echo "FILE $f"; rg -n '"'\\\\renewcommand\\{\\\\Bbbk\\}|\\\\renewcommand\\{\\\\ref\\}|\\\\DeclareMathOperator\\{\\\\gr\\}' \""'$f"; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
FILE standalone/programme_summary_section1.tex
52:\renewcommand{\Bbbk}{\mathbf{C}}
54:\DeclareMathOperator{\gr}{gr}

FILE standalone/programme_summary_sections2_4.tex
54:\renewcommand{\Bbbk}{\mathbf{C}}
56:\DeclareMathOperator{\gr}{gr}
63:\renewcommand{\ref}[1]{%

FILE standalone/programme_summary_sections5_8.tex
53:\renewcommand{\Bbbk}{\mathbf{C}}
55:\DeclareMathOperator{\gr}{gr}
62:\renewcommand{\ref}[1]{%

FILE standalone/programme_summary_sections9_14.tex
52:\renewcommand{\Bbbk}{\mathbf{C}}
54:\DeclareMathOperator{\gr}{gr}
61:\renewcommand{\ref}[1]{%


thinking
**Examining label inconsistencies**

I’m considering reporting this group. I need to check the specific lines in `standalone/editorial.tex` since it uses `\newcommand{\repoinput}`, which may not provide the command but is local. I could actually ignore that issue for now. I think I should also look for label drift in `analytic_sewing` to compare chapter labels, such as `conj:analytic-realization` versus `conj:analytic-realisation`. It looks like those are spelled differently with an “s” in one and a “z” in the other. This could point to a seam break that needs fixing!
codex
I found a seam break in the analytic-sowing lane beyond mere wording: the same conjecture now has different label spellings in standalone and chapter. I’m checking for a few more of these because they silently break cross-references and status syncing.
exec
/bin/zsh -lc "rg -n 'realisation|realization' standalone/analytic_sewing.tex chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'conj:analytic-realisation|conj:analytic-realization' standalone/analytic_sewing.tex chapters/connections/genus_complete.tex chapters/**/*.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/analytic_sewing.tex:474:Let $E$ be any complete locally convex realisation of
standalone/analytic_sewing.tex:2844:\begin{conjecture}[Analytic realisation criterion]
standalone/analytic_sewing.tex:2845:\label{conj:analytic-realisation}
standalone/analytic_sewing.tex:3035:modular Koszul duality programme.  Conjecture~\ref{conj:analytic-realisation}
chapters/connections/genus_complete.tex:1103:\begin{conjecture}[Front-discriminant realization of resonance]
chapters/connections/genus_complete.tex:1338:If $E$ is any complete locally convex realization of\/
chapters/connections/genus_complete.tex:1346:Every such realization makes each seminorm $p_{\Sigma,\xi,\eta}$
chapters/connections/genus_complete.tex:1675:Conjecture~\ref{conj:analytic-realization}.
chapters/connections/genus_complete.tex:1717:\begin{conjecture}[Analytic realization criterion;
chapters/connections/genus_complete.tex:1718:\ClaimStatusConjectured]\label{conj:analytic-realization}%
chapters/connections/genus_complete.tex:1719:\index{analytic realization criterion}%
chapters/connections/genus_complete.tex:1753:\item Prove the realization criterion
chapters/connections/genus_complete.tex:1754: (Conjecture~\ref{conj:analytic-realization}) for unitary full
 succeeded in 51ms:
chapters/connections/genus_complete.tex:1675:Conjecture~\ref{conj:analytic-realization}.
chapters/connections/genus_complete.tex:1718:\ClaimStatusConjectured]\label{conj:analytic-realization}%
chapters/connections/genus_complete.tex:1754: (Conjecture~\ref{conj:analytic-realization}) for unitary full
chapters/connections/frontier_modular_holography_platonic.tex:3827:\label{conj:analytic-realization-criterion}
chapters/connections/frontier_modular_holography_platonic.tex:4237: \textup{(\ref{conj:analytic-realization-criterion})}
chapters/connections/concordance.tex:5314: (Conjecture~\ref{conj:analytic-realization}): a unitary full VOA
chapters/connections/concordance.tex:7773:\item \textup{Conjecture~\ref{conj:analytic-realization} (analytic realization criterion).}
chapters/connections/concordance.tex:7934: Conjecture~\ref{conj:analytic-realization}.
chapters/connections/concordance.tex:8012: (Conjecture~\ref{conj:analytic-realization}).
chapters/connections/concordance.tex:10715: (Conjecture~\ref{conj:analytic-realization}).
chapters/connections/concordance.tex:11215: \textup{(}Conjecture~\ref{conj:analytic-realization}\textup{)}.
chapters/connections/genus_complete.tex:1675:Conjecture~\ref{conj:analytic-realization}.
chapters/connections/genus_complete.tex:1718:\ClaimStatusConjectured]\label{conj:analytic-realization}%
chapters/connections/genus_complete.tex:1754: (Conjecture~\ref{conj:analytic-realization}) for unitary full
standalone/analytic_sewing.tex:2845:\label{conj:analytic-realisation}
standalone/analytic_sewing.tex:3035:modular Koszul duality programme.  Conjecture~\ref{conj:analytic-realisation}
chapters/connections/outlook.tex:285: criterion (Conjecture~\ref{conj:analytic-realization}) remains open.
standalone/analytic_sewing.tex:2845:\label{conj:analytic-realisation}
standalone/analytic_sewing.tex:3035:modular Koszul duality programme.  Conjecture~\ref{conj:analytic-realisation}
standalone/theorem_index.tex:2191:conjecture & \detokenize{conj:analytic-realization-criterion} & \detokenize{Analytic realization criterion for unitary VOAs} & \texttt{Conjectured} & \detokenize{chapters/connections/frontier_modular_holography_platonic.tex:3820}\\
exec
/bin/zsh -lc "python3 - <<'PY'
import re,glob,collections
pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
# heuristic: labels differing only s/z in realisation/realization
labels=collections.defaultdict(list)
for path in glob.glob('standalone/*.tex')+glob.glob('chapters/**/*.tex', recursive=True):
    for i,l in enumerate(open(path),1):
        for m in pat.finditer(l):
            labels[m.group(1)].append((path,i))
for a in sorted(labels):
    b=a.replace('realisation','realization')
    if b"'!=a and b in labels:
        print(a, '"'->', b, '|', labels[a][0], '|', labels[b][0])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 72ms:
conj:analytic-realisation -> conj:analytic-realization | ('standalone/analytic_sewing.tex', 2845) | ('chapters/connections/genus_complete.tex', 1718)
exec
/bin/zsh -lc "rg -n 'eq:connected-free-energy' standalone/analytic_sewing.tex chapters/connections/genus_complete.tex chapters/**/*.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'def:hs-sewing|eq:hs-sewing|def:analytic-koszul-pair|thm:general-hs-sewing' standalone/analytic_sewing.tex standalone/N5_mc5_sewing.tex chapters/connections/genus_complete.tex chapters/**/*.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/genus_complete.tex:1802:\begin{equation}\label{eq:connected-free-energy}
chapters/connections/genus_complete.tex:1802:\begin{equation}\label{eq:connected-free-energy}
chapters/connections/arithmetic_shadows.tex:6878:\begin{equation}\label{eq:connected-free-energy-splitting}
standalone/analytic_sewing.tex:798:\begin{equation}\label{eq:connected-free-energy}
standalone/analytic_sewing.tex:798:\begin{equation}\label{eq:connected-free-energy}
 succeeded in 51ms:
chapters/connections/frontier_modular_holography_platonic.tex:3768:\label{def:hs-sewing-condition}
chapters/connections/frontier_modular_holography_platonic.tex:3775:\begin{equation}\label{eq:hs-sewing-condition}
chapters/connections/frontier_modular_holography_platonic.tex:3788:\label{def:analytic-koszul-pair-frontier}
chapters/connections/frontier_modular_holography_platonic.tex:3862:(Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth +
standalone/analytic_sewing.tex:192:(Definition~\ref{def:hs-sewing}): the sector multiplication
standalone/analytic_sewing.tex:237:(Theorem~\ref{thm:general-hs-sewing}).  The criterion verifies
standalone/analytic_sewing.tex:363: abstractly (HS-sewing, Theorem~\ref{thm:general-hs-sewing})
standalone/analytic_sewing.tex:589:Level~(iv): HS-sewing (Theorem~\ref{thm:general-hs-sewing}).
standalone/analytic_sewing.tex:679:\begin{definition}[HS-sewing]\label{def:hs-sewing}
standalone/analytic_sewing.tex:689:\begin{equation}\label{eq:hs-sewing}
standalone/analytic_sewing.tex:703:when~\eqref{eq:hs-sewing} holds.
standalone/analytic_sewing.tex:1541:Theorem~\ref{thm:general-hs-sewing} are satisfied.
standalone/analytic_sewing.tex:1773:\label{thm:general-hs-sewing}
standalone/analytic_sewing.tex:1843:Theorem~\ref{thm:general-hs-sewing} for each standard family.
standalone/analytic_sewing.tex:1883:Theorem~\ref{thm:general-hs-sewing} gives HS-sewing at every
standalone/analytic_sewing.tex:1896:Theorem~\ref{thm:general-hs-sewing}.
standalone/analytic_sewing.tex:2823:\label{def:analytic-koszul-pair}
standalone/analytic_sewing.tex:2986:(Definition~\ref{def:hs-sewing}) is a single Hilbert--Schmidt
standalone/analytic_sewing.tex:2996:theorem (Theorem~\ref{thm:general-hs-sewing}) verifies the
chapters/connections/thqg_introduction_supplement_body.tex:1457:Theorem~\textup{\ref{thm:general-hs-sewing}}.
exec
/bin/zsh -lc "rg -n 'eq:elliptic-rmatrix|b-monodromy|quantum group parameter|e\\"'^'"\\{2\\\\pi i/\\(k\\+2\\)\\}|e\\"'^'"\\{\\\\pi i/\\(k\\+2\\)\\}' standalone/genus1_seven_faces.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/kac_moody.tex chapters/**/*.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/genus1_seven_faces.tex:117:residue encodes the quantum group parameter.
standalone/genus1_seven_faces.tex:432:\begin{equation}\label{eq:elliptic-rmatrix}
standalone/genus1_seven_faces.tex:488:identification~\eqref{eq:elliptic-rmatrix} follows from
standalone/genus1_seven_faces.tex:500:identification~\eqref{eq:elliptic-rmatrix} holds for all simple $\fg$.
standalone/genus1_seven_faces.tex:814:\begin{equation}\label{eq:b-monodromy}
standalone/genus1_seven_faces.tex:822:coefficient. The quantum group parameter is
standalone/genus1_seven_faces.tex:847:$q = e^{2\pi i/(k+2)}$ is a root of unity. The passage from the
chapters/connections/genus1_seven_faces.tex:1085:\section{The $B$-cycle monodromy and the quantum group parameter}
chapters/connections/genus1_seven_faces.tex:1108:quantum group parameter:
chapters/connections/genus1_seven_faces.tex:1136:the genus-$1$ collision residue: the quantum group parameter $q$ is
chapters/examples/kac_moody.tex:2394:\item The Kazhdan--Lusztig quantum group parameter for the dual level is
chapters/examples/kac_moody.tex:2483:$k$ & Simple objects & $|P^k_+|$ & $q = e^{\pi i/(k+2)}$ \\
chapters/examples/kac_moody.tex:2500:\quad\text{at } q = e^{\pi i/(k+2)}
chapters/theory/derived_langlands.tex:948:\subsection{Admissible levels and the quantum group parameter}
chapters/examples/yangians_drinfeld_kohno.tex:268:\item quantum Casimir eigenvalues $q^{C_2}$ at $q = e^{\pi i/(k+2)}$,
chapters/examples/yangians_drinfeld_kohno.tex:1330:\item At roots of unity $q = e^{2\pi i/(k+2)}$, the Verlinde
chapters/examples/yangians_drinfeld_kohno.tex:7270:\begin{equation}\label{eq:elliptic-rmatrix}
chapters/examples/yangians_drinfeld_kohno.tex:7857:$U_q(\mathfrak{sl}_2)$ with $q = e^{2\pi i/(k+2)}$
chapters/theory/higher_genus_modular_koszul.tex:32923:the quantum group parameter $q$ becomes a root of unity,
chapters/theory/higher_genus_modular_koszul.tex:32967:  at the root of unity $q = e^{2\pi i/(k+2)}$\textup{)}.
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '1080,1145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'q = e\\"'^'"\\{2\\\\pi i/\\(k\\+2\\)\\}|q = e\\"'^'"\\{\\\\pi i/\\(k\\+2\\)\\}|B-cycle monodromy|Verlinde partition function' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'q = \\\\exp\\(2\\\\pi i/\\(k\\+h\\"'^'"\\\\vee\\)\\)|q = e\\"'^'"\\{2\\\\pi i/\\(k\\+2\\)\\}|q = e\\"'^'"\\{\\\\pi i/\\(k\\+2\\)\\}' standalone/genus1_seven_faces.tex chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1097:\index{B-cycle monodromy@$B$-cycle monodromy!collision residue|textbf}
 succeeded in 50ms:
  1080	
  1081	%% ====================================================================
  1082	%% 11. THE B-CYCLE MONODROMY AND THE QUANTUM GROUP
  1083	%% ====================================================================
  1084	
  1085	\section{The $B$-cycle monodromy and the quantum group parameter}
  1086	\label{sec:g1sf-b-cycle}
  1087	
  1088	The genus-$1$ collision residue carries information that is invisible
  1089	at genus~$0$: the $B$-cycle monodromy. For affine Kac--Moody, the
  1090	$B$-cycle monodromy of the KZB connection produces the quantum group
  1091	parameter $q = \exp(2\pi i/(k + h^\vee))$
  1092	(Theorem~\ref{thm:b-cycle-quantum-group}).
  1093	
  1094	\begin{theorem}[$B$-cycle monodromy of the collision residue;
  1095	\ClaimStatusProvedHere]
  1096	\label{thm:g1sf-b-cycle-monodromy}
  1097	\index{B-cycle monodromy@$B$-cycle monodromy!collision residue|textbf}
  1098	Let $\cA$ be a modular Koszul chiral algebra with $c_0 \neq 0$. The
  1099	$B$-cycle monodromy of the genus-$1$ collision residue is
 succeeded in 50ms:
standalone/genus1_seven_faces.tex:76:group parameter $q = \exp(2\pi i/(k+h^\vee))$. For class~$M$
standalone/genus1_seven_faces.tex:823:$q = \exp(2\pi i/(k+h^\vee))$, and the Verlinde partition function
standalone/genus1_seven_faces.tex:847:$q = e^{2\pi i/(k+2)}$ is a root of unity. The passage from the

thinking
**Evaluating mathematical connections**

I’m looking at the connection between 2π and the chapters in genus1_seven_faces; it seems they both fit well together. So, I don't think there’s a seam issue. The standalone genus1_seven_faces aligns with chapters/connections properly, which is great! However, I still see an invalid equality between lines 711-712 that needs fixing. I need to check if there’s a corrected chapter version or if exact expressions exist elsewhere in those chapters.
exec
/bin/zsh -lc "rg -n 'k\\\\,\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|Elliptic.*rational|r\\"'^'"\\{\\\\mathrm\\{ell\\}\\}_\\\\fg\\(z,\\\\tau\\)/(k\\+h\\"'^'"\\\\vee)' standalone/genus1_seven_faces.tex chapters/connections/genus1_seven_faces.tex chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/genus1_seven_faces.tex:969:\item \textup{(}Elliptic $r$-matrix $\to$ rational $r$-matrix.\textup{)}
chapters/connections/genus1_seven_faces.tex:982:\item \textup{(}Elliptic Gaudin $\to$ rational Gaudin.\textup{)}
standalone/genus1_seven_faces.tex:710:\item \textup{(Elliptic $\to$ rational $r$-matrix.)}
standalone/genus1_seven_faces.tex:712:k\,\Omega/((k+h^\vee)z) = \Omega/((k+h^\vee)z)$ through the
standalone/genus1_seven_faces.tex:717:\item \textup{(Elliptic $\to$ rational Gaudin.)}
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '950,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Degeneration|KZB.*KZ|Elliptic.*rational.*r-matrix|intermediate trigonometric' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   950	\index{collision residue!degeneration to genus 0}
   951	As $\operatorname{Im}(\tau) \to \infty$
   952	\textup{(}equivalently, $q = e^{2\pi i\tau} \to 0$\textup{)}, all
   953	seven genus-$1$ faces degenerate to their genus-$0$ counterparts:
   954	\begin{enumerate}[label=\textup{(\roman*)}]
   955	\item \textup{(}Propagator.\textup{)}
   956	$\zeta_\tau(z) \to \pi\cot(\pi z) \to 1/z + O(z)$.
   957	
   958	\item \textup{(}Weierstrass functions.\textup{)}
   959	$\wp(z, \tau) \to \pi^2/\sin^2(\pi z) \to 1/z^2 + O(1)$, and
   960	$\wp^{(m)}(z, \tau) \to (-1)^m(m+1)!/z^{m+2} + O(z^{-m})$ at leading
   961	order.
   962	
   963	\item \textup{(}KZB $\to$ KZ.\textup{)}
   964	The $dz$-component of the KZB connection degenerates to the KZ
   965	connection: $\zeta_\tau(z_{ij}) \to 1/(z_{ij})$. The
   966	$d\tau$-component vanishes because the modulus $\tau$ is not a
   967	parameter at genus~$0$.
   968	
   969	\item \textup{(}Elliptic $r$-matrix $\to$ rational $r$-matrix.\textup{)}
 succeeded in 51ms:
937:\section{Degeneration to genus~$0$}
948:\begin{theorem}[Degeneration to genus~$0$; \ClaimStatusProvedHere]
963:\item \textup{(}KZB $\to$ KZ.\textup{)}
964:The $dz$-component of the KZB connection degenerates to the KZ
972:intermediate trigonometric $r$-matrix:
1065:\item \textbf{Degeneration.}

thinking
**Exploring label similarities**

I'm considering checking all standalone labels that aren't in chapters and have a similarity greater than 0.9. That seems like a heavy task, but I might limit it to just American and British versions. I think I already did that. Finding titles with different labels might be challenging, but comparing theorem titles could help. I could search for something like "Analytic realization criterion" in both contexts to spot mismatches, and I want to use grep for precise searches. This could reveal more label drift.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, glob, collections
begin_re=re.compile(r'\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|conjecture|computation)\\}(?:\\[(.*?)\\])?')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
# capture env title label within next 3 lines
entries=[]
for path in glob.glob('standalone/*.tex')+glob.glob('chapters/**/*.tex', recursive=True):
    lines=open(path).read().splitlines()
    for i,l in enumerate(lines):
        m=begin_re.search(l)
        if m:
            env,title=m.group(1), (m.group(2) or '').strip()
            lab=''
            for j in range(i,min(len(lines),i+4)):
                lm=label_re.search(lines[j])
                if lm:
                    lab=lm.group(1); break
            if title:
                entries.append((title,env,lab,path,i+1))
# normalize title by stripping claimstatus fragments and tex formatting crudely
import string

def norm(s):
    s=re.sub(r'\\\\ClaimStatus\\w+','',s)
    s=re.sub(r'\\\\cite\\{["'^}]*'"\\}','',s)
    s=re.sub(r'\\\\;',' ',s)
    s=re.sub(r'\\s+',' ',s)
    return s.strip().lower()
by=collections.defaultdict(list)
for e in entries:
    by[norm(e[0])].append(e)
for title,vals in sorted(by.items()):
    if len(vals)>=2:
        stand=[v for v in vals if v[3].startswith('standalone/')]
        chap=[v for v in vals if v[3].startswith('chapters/')]
        if stand and chap:
            labels={(v[2],v[3]) for v in vals}
            if len({v[2] for v in vals})>1:
                print('TITLE:',title)
                for v in vals:
                    print(' ',v)
                print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
TITLE: analytic koszul pair
  ('Analytic Koszul pair', 'definition', 'def:analytic-koszul-pair', 'standalone/analytic_sewing.tex', 2822)
  ('Analytic Koszul pair', 'definition', 'def:analytic-koszul-pair-frontier', 'chapters/connections/frontier_modular_holography_platonic.tex', 3787)
  ('Analytic Koszul pair', 'definition', 'def:analytic-koszul-pair', 'chapters/connections/genus_complete.tex', 1588)

TITLE: chiral bar complex
  ('Chiral bar complex', 'definition', 'def:bar-complex', 'standalone/shadow_towers.tex', 375)
  ('Chiral bar complex', 'definition', 'def:bar-complex', 'standalone/shadow_towers_v3.tex', 500)
  ('Chiral bar complex', 'definition', '', 'chapters/theory/koszul_pair_structure.tex', 218)

TITLE: chiral hochschild cochain complex
  ('Chiral Hochschild cochain complex', 'definition', 'def:e-chirHoch', 'standalone/en_chiral_operadic_circle.tex', 843)
  ('Chiral Hochschild cochain complex', 'definition', 'def:chiral-hochschild-cochain-brace', 'chapters/theory/chiral_center_theorem.tex', 298)

TITLE: chiral koszul morphism
  ('Chiral Koszul morphism', 'definition', 'def:chiral-koszul-morphism', 'standalone/N1_koszul_meta.tex', 364)
  ('Chiral Koszul morphism', 'definition', 'def:kfc-chiral-koszul-morphism', 'standalone/koszulness_fourteen_characterizations.tex', 332)
  ('Chiral Koszul morphism', 'definition', 'def:chiral-koszul-morphism', 'chapters/theory/chiral_koszul_pairs.tex', 268)

TITLE: chiral quantum group equivalence

thinking
**Verifying line ranges**

I need to verify specific line ranges in `standalone/analytic_sewing` and `standalone/N5_mc5_sewing`. It seems like the requested format should be `file:line` and possibly just the start line could work, but including a specific range after the colon sounds even better. I should check the lines around def/label drift in `standalone/analytic_sewing` and also in the `chapters/connections/genus_complete`. I also have a couple of line ranges noted for `standalone/genus1_seven_faces`.
exec
/bin/zsh -lc "rg -n 'g1sf-elliptic-rmatrix|1/\\(k\\+h\\"'^'"\\\\vee\\)|Belavin classical elliptic' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
470:\begin{equation}\label{eq:g1sf-elliptic-rmatrix}
537:The overall identification~\eqref{eq:g1sf-elliptic-rmatrix} is the
557:identification~\eqref{eq:g1sf-elliptic-rmatrix} holds for all simple
974:The collision residue~\eqref{eq:g1sf-elliptic-rmatrix} inherits
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '462,476p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   462	\ClaimStatusProvedElsewhere{} \textup{(}classical elliptic $r$-matrix:
   463	Belavin 1981, Belavin--Drinfeld 1982\textup{)}]
   464	\label{thm:g1sf-face-5}
   465	\index{R-matrix@$R$-matrix!elliptic!as genus-1 Face 5|textbf}
   466	\index{Belavin r-matrix@Belavin $r$-matrix!genus-1 identification}
   467	For $\cA = \widehat{\fg}_k$ with $\fg$ simple and
   468	$k \neq -h^\vee$, the genus-$1$ collision residue equals the
   469	classical elliptic $r$-matrix up to the standard level normalization:
   470	\begin{equation}\label{eq:g1sf-elliptic-rmatrix}
   471	r_{\widehat{\fg}_k}^{(1)}(z, \tau)
   472	\;=\;
   473	\frac{k}{k + h^\vee}\,
   474	r^{\mathrm{ell}}_\fg(z, \tau),
   475	\end{equation}
   476	where $r^{\mathrm{ell}}_\fg(z, \tau)$ is the Belavin elliptic

thinking
**Evaluating mathematical connections**

I'm considering whether theorem line 473 using \(k/(k+h^\vee) r^{ell}_\fg\) is accurate, especially if \(r^{ell}_\fg\) approaches \(\Omega/z\). If so, the limit would indeed be \(k\Omega/((k+h^\vee)z)\) rather than the stated 976. It seems like \(r^{ell}_\fg\) might be normalized differently as \(\Omega/kz\). I should check the connection chapter for \(r^{ell}_\fg\) and see if there's a \(k\) involved in the \(\sl_2\) formula after line 476. Let's take a closer look!
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '470,505p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   470	\begin{equation}\label{eq:g1sf-elliptic-rmatrix}
   471	r_{\widehat{\fg}_k}^{(1)}(z, \tau)
   472	\;=\;
   473	\frac{k}{k + h^\vee}\,
   474	r^{\mathrm{ell}}_\fg(z, \tau),
   475	\end{equation}
   476	where $r^{\mathrm{ell}}_\fg(z, \tau)$ is the Belavin elliptic
   477	$r$-matrix. For $\fg = \mathfrak{sl}_2$:
   478	\begin{equation}\label{eq:g1sf-sl2-elliptic}
   479	r^{\mathrm{ell}}_{\mathfrak{sl}_2}(z, \tau)
   480	\;=\;
   481	\zeta_\tau(z) \cdot \frac{H \otimes H}{2}
   482	\;+\;
   483	\phi_+(z, \tau)\, E \otimes F
   484	\;+\;
   485	\phi_-(z, \tau)\, F \otimes E,
   486	\end{equation}
   487	where $\{H, E, F\}$ is the standard basis of $\mathfrak{sl}_2$
   488	and the theta-function ratios are
   489	\begin{equation}\label{eq:g1sf-phi-pm}
exec
/bin/zsh -lc "nl -ba standalone/genus1_seven_faces.tex | sed -n '428,445p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'r\\"'^'"\\{\\\\mathrm\\{ell\\}\\}_\\\\fg|Belavin elliptic r-matrix|k/\\(k \\+ h\\"'^'"\\\\vee\\)|1/\\(k\\+h\\"'^'"\\\\vee\\)' chapters/connections/genus1_seven_faces.tex standalone/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   428	\begin{theorem}[Face~5: elliptic $r$-matrix]\label{thm:elliptic-r}
   429	For $\cA = \widehat{\fg}_k$ with $\fg$ simple and $k \neq -h^\vee$,
   430	the genus-$1$ collision residue equals the classical elliptic
   431	$r$-matrix up to the standard level normalization:
   432	\begin{equation}\label{eq:elliptic-rmatrix}
   433	r_{\widehat{\fg}_k}^{(1)}(z,\tau)
   434	\;=\;
   435	\frac{1}{k+h^\vee}\,r^{\mathrm{ell}}_\fg(z,\tau).
   436	\end{equation}
   437	For $\fg = \fsl_2$, the Belavin $r$-matrix is
   438	\begin{equation}\label{eq:sl2-elliptic}
   439	r^{\mathrm{ell}}_{\fsl_2}(z,\tau)
   440	\;=\;
   441	\zeta_\tau(z)\cdot\frac{H \otimes H}{2}
   442	\;+\;
   443	\phi_+(z,\tau)\,E \otimes F
   444	\;+\;
   445	\phi_-(z,\tau)\,F \otimes E,
 succeeded in 50ms:
chapters/connections/genus1_seven_faces.tex:474:r^{\mathrm{ell}}_\fg(z, \tau),
chapters/connections/genus1_seven_faces.tex:476:where $r^{\mathrm{ell}}_\fg(z, \tau)$ is the Belavin elliptic
chapters/connections/genus1_seven_faces.tex:864:$r_\cA^{(1)} = k\,r^{\mathrm{ell}}_\fg/(k + h^\vee)$
chapters/connections/genus1_seven_faces.tex:892:\frac{k\,r^{\mathrm{ell}}_\fg}{k + h^\vee}
standalone/genus1_seven_faces.tex:435:\frac{1}{k+h^\vee}\,r^{\mathrm{ell}}_\fg(z,\tau).
standalone/genus1_seven_faces.tex:711:$r^{\mathrm{ell}}_\fg(z,\tau)/(k+h^\vee) \to


thinking
**Evaluating normalization inconsistencies**

I'm noticing an inconsistency between two lines in the genus-1 elliptic residue encoding. One line uses a different normalization than the other, and they seem to contradict each other regarding the degeneration formulas in the chapters. The user requested an exact fix, so I need to decide on one convention to propagate. If the intention is to use the first degeneration, I'll suggest changing one line to match the other. But if we go with the second, we'll have to adjust the corresponding sections.
thinking
**Evaluating chapter findings**

The user wants me to audit the connections between the standalone and chapter findings, which is a good approach. I think I should include the specific file lines from the chapter with the issues referenced against the corresponding standalone line. This could be really valuable! It looks like I need to inspect lines 860-866 and 888-894 for context. Maybe just focusing on line 473 could be sufficient. I’ll definitely need to mention updating repeated instances in the same file.
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '858,895p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   858	\item \textbf{KZB connection.}
   859	The $dz$-component of the KZB connection equals the collision residue;
   860	the $d\tau$-component is its $z$-derivative
   861	\textup{(}Theorem~\textup{\ref{thm:g1sf-face-4})}.
   862	
   863	\item \textbf{Belavin--Drinfeld elliptic $r$-matrix.}
   864	$r_\cA^{(1)} = k\,r^{\mathrm{ell}}_\fg/(k + h^\vee)$
   865	\textup{(}Theorem~\textup{\ref{thm:g1sf-face-5})}; the level
   866	prefix~$k$ is required.
   867	
   868	\item \textbf{Elliptic Sklyanin bracket.}
   869	The elliptic $r$-matrix defines an elliptic Sklyanin Poisson bracket
   870	on $\fg^*$, generalizing the genus-$0$ Sklyanin bracket of
   871	Semenov-Tian-Shansky~\cite{STS83} to $E_\tau$.
   872	
   873	\item \textbf{Elliptic Gaudin Hamiltonians.}
   874	$H_i^{\mathrm{ell}} = \sum_{j \neq i}\,[r_\cA^{(1)}(z_i - z_j)]_{ij}$
   875	\textup{(}Theorem~\textup{\ref{thm:g1sf-face-7})}.
   876	\end{enumerate}
   877	All seven realizations agree as elements of



thinking
**Considering file references**

I’m thinking that files like `standalone/arithmetic_shadows.tex` and `standalone/riccati.tex` could use `\renewcommand{\ref}`. I need to gather exact line references for the survey file group. The user wants each finding cited with file and line references. An example could be `[HIGH] standalone/introduction_full_survey.tex:107; standalone/survey_modular_koszul_duality.tex:102; ...` for clarity. I’ll also add findings about macro collisions and global overrides in the summary, which seems acceptable.
thinking
**Resolving inconsistencies in chapters**

I need to address the problem with chapter connections in genus1_seven_faces, specifically line 473. I think the fix involves replacing `k/(k+h^\vee)` with `1/(k+h^\vee)` at lines 473, 864, and 892. I should reference line 976 and standalone line 435 as well. If the user wants all inconsistencies, I should clarify that this fix depends on the KZ convention mentioned in line 976. It seems standalone already uses the correct format, which aligns with my findings.
thinking
**Formulating findings on files**

I think I should focus on the files we've identified as seam-critical pairs and create a main standalone summary. It seems like potential group 3 references also apply to many. I can make a list of those we encountered. I should mention that `main.tex:600-719` already provides the macros to ground the collision. Instead of numerous details, maybe one high-level finding on the namespace-collision pattern would be better since every file requires the same fix. Let’s aim to formulate each bullet point succinctly!
codex
- [CRITICAL] chapters/connections/genus1_seven_faces.tex:473 — PROBLEM: Face~5 uses `k/(k+h^\vee)` in `r_{\widehat{\fg}_k}^{(1)}(z,\tau)`, but the seam does not support that normalization: the standalone paper has `1/(k+h^\vee)` at `standalone/genus1_seven_faces.tex:435`, and the same chapter later degenerates to `\Omega/((k+h^\vee)z)` at `chapters/connections/genus1_seven_faces.tex:976`. FIX: change `k/(k+h^\vee)` to `1/(k+h^\vee)` here and at the repeated restatements `chapters/connections/genus1_seven_faces.tex:864` and `:892`, then add one explicit bridge sentence that `chapters/examples/yangians_drinfeld_kohno.tex:7271-7278` is the trace-form presentation of the same residue.

- [CRITICAL] standalone/analytic_sewing.tex:2822 — PROBLEM: `def:analytic-koszul-pair` is stale and self-contradictory at the seam. The standalone defines an analytic Koszul pair by already having the Quillen equivalence `\barB^{an} \dashv \Omega^{an}` on sewing-complete categories, then immediately restates that same equivalence as conjecture `conj:analytic-realisation` at `standalone/analytic_sewing.tex:2844-2849`. The main chapter no longer does this: `chapters/connections/genus_complete.tex:1588-1605` gives a structural definition, and the realization criterion is separately conjectural at `:1717-1735`. FIX: replace the standalone definition body with the four-item chapter definition from `genus_complete.tex:1591-1604`, delete the Quillen-equivalence clause from the definition, and keep the equivalence only as the conjecture.

- [CRITICAL] standalone/ordered_chiral_homology.tex:39 — PROBLEM: this standalone is not import-safe. It redeclares the exact ordered-homology insertion surface (`\cA`, `\MC`, `\HH`, `\Ainf`, `\Eone`, `\Barord`, `\BarSig`, `\gmod`, `\gEone`, `\RR`, `\ZZ`, `\PP`, `\HHH`, etc.) with `\newcommand`/`\DeclareMathOperator`, but `main.tex:694-719` already predefines that surface with `\providecommand` specifically for standalone insertion. FIX: replace the whole macro block `standalone/ordered_chiral_homology.tex:39-107` by guarded definitions: `\providecommand` for symbols already supplied by `main.tex`, and `\@ifundefined{...}{\DeclareMathOperator...}{}` or `\providecommand{\foo}{\operatorname{...}}` for operators.

- [HIGH] standalone/analytic_sewing.tex:679; standalone/N5_mc5_sewing.tex:331 — PROBLEM: `def:hs-sewing` does not match the canonical chapter definition. Both standalones define HS-sewing “at parameter `q`”, while `chapters/connections/genus_complete.tex:1358-1365` defines the same label existentially: there exists `0<q<1` such that the HS sum converges. Downstream refs to `\ref{def:hs-sewing}` therefore point to different mathematics on the two sides of the seam. FIX: rewrite both standalone definitions to match `genus_complete.tex`: “Say `\cA` satisfies HS-sewing if there exists `0<q<1` such that …”, keep the displayed sum unchanged, and keep the “for every `q`” statement only in `thm:general-hs-sewing`.

- [HIGH] standalone/analytic_sewing.tex:798 — PROBLEM: `eq:connected-free-energy` changed meaning across the seam. In the standalone it is the genus-`g` formula `F_g^{conn}(\cA;q)=-\log\det(1-K_g)`, but in the chapter it is the genus-1 definition `F_\cA^{conn}(q)=-\log\det(1-K_q(\cA))` at `chapters/connections/genus_complete.tex:1801-1807`. Same label, different object. FIX: rename the standalone display to a new label such as `eq:connected-free-energy-g` and reserve `eq:connected-free-energy` for the chapter’s genus-1 definition, or rewrite the standalone display to the genus-1 formula and add a separately labeled genus-`g` variant.

- [HIGH] standalone/genus1_seven_faces.tex:710 — PROBLEM: the degeneration formula contains a false equality: `k\,\Omega/((k+h^\vee)z) = \Omega/((k+h^\vee)z)`. That is not a convention issue; it is algebraically wrong. The chapter already has the corrected degeneration wording at `chapters/connections/genus1_seven_faces.tex:969-980`. FIX: replace `standalone/genus1_seven_faces.tex:710-714` by the chapter text: “The Belavin `r`-matrix degenerates … `r^{(1)}_{\widehat{\fg}_k}(z,\tau)\to \Omega/((k+h^\vee)z)`”, and delete the bogus equality.

- [HIGH] standalone/analytic_sewing.tex:37; standalone/bp_self_duality.tex:36; standalone/garland_lepowsky.tex:36; standalone/genus1_seven_faces.tex:33; standalone/multi_weight_cross_channel.tex:35; standalone/classification_trichotomy.tex:33 — PROBLEM: these seam-critical standalone preambles still use unguarded `\newcommand`/`\DeclareMathOperator` for names the manuscript already owns in `main.tex:600-719` (`\cA`, `\MC`, `\Res`, `\Vir`, `\fg`, `\rk`, `\gr`, etc.). Imported under the main preamble, they will raise duplicate-definition errors. FIX: change all seam-facing `\newcommand` declarations in these files to `\providecommand`, and replace each `\DeclareMathOperator{\foo}{...}` by either `\providecommand{\foo}{\operatorname{...}}` or `\@ifundefined{foo}{\DeclareMathOperator{\foo}{...}}{}`.

- [HIGH] standalone/introduction_full_survey.tex:107; standalone/survey_modular_koszul_duality.tex:102; standalone/survey_modular_koszul_duality_v2.tex:166; standalone/survey_track_a_compressed.tex:94; standalone/survey_track_b_compressed.tex:149; standalone/programme_summary_sections2_4.tex:63; standalone/programme_summary_sections5_8.tex:62; standalone/programme_summary_sections9_14.tex:61; standalone/classification.tex:38; standalone/riccati.tex:36; standalone/arithmetic_shadows.tex:103; standalone/computations.tex:33 — PROBLEM: these standalones globally redefine `\ref` to inject fallback text like “full monograph”. If any of them are loaded into the manuscript, they silently corrupt reference behavior for everything that follows. FIX: do not redefine `\ref`; rename the helper to a standalone-local macro such as `\monographref`, or wrap the override in a standalone-only guard and restore the original `\ref` before any import boundary.

- [MEDIUM] standalone/programme_summary_section1.tex:52; standalone/programme_summary_sections2_4.tex:54; standalone/programme_summary_sections5_8.tex:53; standalone/programme_summary_sections9_14.tex:52 — PROBLEM: these summaries overwrite the manuscript’s generic base-field symbol with `\renewcommand{\Bbbk}{\mathbf{C}}`. That is a convention drift, not a harmless local shorthand. FIX: remove the `\renewcommand{\Bbbk}{...}` lines; if these summaries need a hard-coded complex field, introduce a local macro such as `\StandaloneField` and use that in the standalone only.

- [MEDIUM] standalone/analytic_sewing.tex:2845 — PROBLEM: the same conjecture has two labels at the seam: `conj:analytic-realisation` in the standalone and `conj:analytic-realization` in the chapter (`chapters/connections/genus_complete.tex:1718`). This breaks propagation, theorem indexing, and status sync. FIX: rename the standalone label to `conj:analytic-realization` and update the local reference at `standalone/analytic_sewing.tex:3035`.

- [LOW] standalone/bp_self_duality.tex:151 — PROBLEM: `prop:bp-central-charge` is surfaced as an unqualified proposition in the standalone, but the chapter mirror marks the same claim as `\ClaimStatusProvedElsewhere` with attribution at `chapters/examples/bershadsky_polyakov.tex:144-153`. The seam drops epistemic status and source. FIX: copy the chapter header and attribution into the standalone: mark it as proved elsewhere and add the `FKR20`/Kac--Roan--Wakimoto provenance sentence, or rename the standalone label if it is meant to be expository rather than canonical.

## Summary
Checked: 29 | Findings: 11 | Verdict: FAIL
tokens used
305,879
