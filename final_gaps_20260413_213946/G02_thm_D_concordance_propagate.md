# G02_thm_D_concordance_propagate (1425s)

**FIXED**

Vol I is aligned. I updated the live theorem surfaces in [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5975), [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1915), and [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1870), then propagated the narrowed Theorem D scope through [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2496), [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3069), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:814), [programme_summary_sections2_4.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:240), [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:643), and [five_theorems_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:1294). `cor:kappa-additivity` now routes through genus~1 only; `thm:universal-generating-function` is scoped to the proved uniform-weight lane with the genus-1 clause separated; `thm:anomaly-koszul` now uses `d_{\mathrm{fib}}^2 = 0` and the genus-1 curvature direction. The stale `C -> D` dependency prose in the standalone five-theorems file is removed.

[concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:55) was already consistent with the repaired Theorem D status, so it needed verification but no content change.

Verification: I regenerated metadata with `python3 scripts/generate_metadata.py`, ran targeted grep for the old AP228/AP230 phrases and theorem-status drift, and ran `git diff --check`. Those passed in Vol I.

**BLOCKED**

Cross-volume propagation is blocked by sandbox write limits outside `/Users/raeez/chiral-bar-cobar`. I could verify the remaining live collisions but not edit them:
- [bv_brst.tex](</Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:330>) and [bv_brst.tex](</Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:479>) in Vol II still repeat the old anomaly wording with `d_{\mathrm{bar}}^2 = 0`.
- [bar_cobar_bridge.tex](</Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221>) in Vol III still gives a compressed Theorem D summary that should be expanded to the genus-1/all-genera split if you want full cross-volume parity.


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
session id: 019d885b-768a-7662-be76-44fc96c547f9
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


After G01 fixes the universality gap, propagate to ALL downstream surfaces.

TARGETS: chapters/connections/concordance.tex, chapters/theory/introduction.tex,
chapters/frame/preface.tex, standalone/*.tex

Search for: 'obs_g', 'Theorem D', 'genus-universality', 'family-index', 'all genera'.
For each: update to match the new Theorem D status (either fully proved via
clutching-uniqueness/GRR, or split genus-1/all-genera).

Also fix: cor:kappa-additivity to route through genus-1 only (AP230).
Also fix: thm:universal-generating-function status to match.
Also fix: anomaly-Koszul dependency direction (AP228).
mcp startup: no servers

thinking
**Considering scope and search terms**

I'm thinking about the user's request regarding downstream surfaces. They mentioned it's possibly within the repo only, but I need to consider if the AGENTS cross-volume rule applies. It seems like the task specifies targets within standalone/*.tex files. Maybe I should search terms only in this repo. I could also grep all three volumes if there's a shared formula. Still, I'm wondering about editing—if there are no duplicates, perhaps I don't need to make changes at all.
codex
Using `claim-surface-sync` first, then `cross-volume-propagation` if the Theorem D status change leaks beyond the named targets. I’m reading the constitutional files, the live theorem registry/concordance, and the exact surfaces that mention `obs_g`/Theorem D before I touch anything.
exec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,719pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,681pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~319pp). Total ~4,719pp, 121K+ tests, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 52ms:
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

codex
The canonical surface currently says Theorem D is fully proved, but I haven’t trusted that yet. I’m locating every live advertisement of `obs_g`, Theorem D, `genus-universality`, `family-index`, `all genera`, plus the AP230/AP228 labels, then I’ll align the status boundary before editing.
exec
/bin/zsh -lc "rg -n \"obs_g|Theorem D|genus-universality|family-index|all genera|cor:kappa-additivity|thm:universal-generating-function|anomaly-Koszul|modular-characteristic|universal generating function\" chapters standalone metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"obs_g|Theorem D|genus-universality|family-index|all genera|cor:kappa-additivity|thm:universal-generating-function|anomaly-Koszul|modular-characteristic|universal generating function\" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 358

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:38:The modular extension: the A_inf structure becomes curved at genus >= 1. The curvature kappa * omega_g is the obstruction to flatness. Curved Dunn at genus 1: PROVED (prop:genus1-twisted-tensor-product, twisted Künneth). Genus >= 2: OPEN (genuine H² obstruction). Modular operad: composition PROVED (genus 0 all levels, all genera integrable via KZ pentagon + KL regularity); equivariance PROVED (quasi-triangularity + YBE); unitality PROVED (all genera, all shadow classes). Sole remaining gap: composition at generic non-integral level, genus >= 1 (Stokes gap).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:323:FM67: Curved Dunn two-complex distinction. There are TWO H² obstruction groups: (a) modular-bootstrap complex (H²=0, PROVED — every Ob_g is exact there), (b) curved-Dunn twisting-cochain complex (OPEN — no proof H²=0). The bridge between (a) and (b) is the precise frontier. If bridged, curved Dunn at all genera follows from the already-proved modular bootstrap exactness.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:336:| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) Analytic HS-sewing proved at all genera; (2) genus-0 algebraic BRST/bar proved; (3) D^co-level BV=bar proved for all shadow classes including class M; (4) genuswise chain-level BV/BRST/bar conjectural (class M chain-level false); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:235:Theorem~CY-D (Theorem~\ref{thm:cy-modular-characteristic}) when
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:531:% For W-algebras: kappa + kappa' = rho*K (Theorem D).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:13:A toric CY3 $X_\Sigma$ is determined by a fan $\Sigma$ in $\mathbb{Z}^3$ satisfying the CY condition (all generators coplanar). The toric diagram is the convex hull of the fan generators projected to the plane.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:33:\phantomsection\label{thm:genus-universality}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:39:\phantomsection\label{thm:modular-characteristic}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2305:$\Theta_{\cA_{\mathrm{free}}} = \kappa_{\mathrm{ch}} \cdot \omega_g$ at all genera.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2810:so $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ at all genera.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3272:$X$; the modular completion (incorporating all genera) is the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3754: $F_g$ data at all genera.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4170: (Theorem~\ref{thm:genus-universality}),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4355:Theorem~\textup{\ref{thm:modular-characteristic})}, in the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4387:(Theorem~\ref{thm:modular-characteristic})
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5211:This is proved by Beauville (1999) via deformation to the Hilbert scheme and by Bryan--Leung (2000) via symplectic techniques. The BPS integrality $n_h^g \in \Z$ for all genera is proved by Pandharipande--Thomas (2016).
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:97:- Modular operad: genus-0 product decomposition PROVED; π_1(Σ_g) PROVED for all affine KM at all genera (KZB flatness); COMPOSITION ASSOCIATIVITY PROVED at genus 0 all levels + all genera integrable levels (thm:affine-composition-associativity, KZ pentagon + KL regularity); EQUIVARIANCE PROVED (prop:qt-equivariance, quasi-triangularity + YBE); UNITALITY PROVED all genera all shadow classes (prop:modular-operad-unitality, unit vertex simply connected → Mon(R)=id). Full modular operad for Heisenberg: PROVED (prop:heisenberg-full-modular-operad). Sole remaining gap: composition at generic non-integral level, genus ≥ 1 (Stokes gap: KZB regularity at M̄_{g,n} boundary divisors).
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:232:3. thm:kz-classical-quantum-bridge — classical-to-quantum bridge at all genera (Vol I)
 succeeded in 51ms:
Total output lines: 897

metadata/theorem_registry.md:88:| `thm:guide-family-index` | `theorem` | 241 | Family index theorem for genus expansions |
metadata/theorem_registry.md:226:| `thm:genus-induction-strict` | `theorem` | 6117 | Strict nilpotence at all genera |
metadata/theorem_registry.md:645:| `thm:e1-theorem-A-modular` | `theorem` | 1920 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
metadata/theorem_registry.md:646:| `thm:e1-theorem-B-modular` | `theorem` | 1977 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
metadata/theorem_registry.md:647:| `thm:e1-theorem-C-modular` | `theorem` | 2003 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
metadata/theorem_registry.md:648:| `thm:e1-theorem-D-modular` | `theorem` | 2043 | Theorem~$\mathrm{D}^{E_1}$ at all genera: formal ordered degree-$2$ shadow series |
metadata/theorem_registry.md:649:| `thm:e1-theorem-H-modular` | `theorem` | 2114 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$ |
metadata/theorem_registry.md:851:| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5137 | Nilpotence of obstruction (all genera) |
metadata/theorem_registry.md:853:| `thm:genus-universality` | `theorem` | 5336 | Genus universality |
metadata/theorem_registry.md:858:| `cor:kappa-additivity` | `corollary` | 5921 | Additivity of the obstruction coefficient |
metadata/theorem_registry.md:889:| `thm:pbw-allgenera-principal-w` | `theorem` | 772 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
metadata/theorem_registry.md:894:| `thm:pbw-allgenera-km` | `theorem` | 1365 | PBW degeneration at all genera for Kac--Moody |
metadata/theorem_registry.md:896:| `thm:pbw-allgenera-virasoro` | `theorem` | 1625 | PBW degeneration at all genera for Virasoro |
metadata/theorem_registry.md:906:| `thm:modular-characteristic` | `theorem` | 2845 | Modular characteristic |
metadata/theorem_registry.md:1542:| `thm:heisenberg-all-genera` | `theorem` | 101 | Heisenberg free energy at all genera |
metadata/theorem_registry.md:1547:| `thm:sl2-all-genera` | `theorem` | 480 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
metadata/theorem_registry.md:1565:| `thm:universal-generating-function` | `theorem` | 1913 | Universal generating function |
metadata/theorem_registry.md:1570:| `thm:fermion-all-genera` | `theorem` | 2389 | Free fermion free energy at all genera |
 succeeded in 50ms:
?? scripts/final_gaps_campaign.py
exec
/bin/zsh -lc "sed -n '1,260p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files standalone | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cA}{\mathcal{A}}
\providecommand{\barB}{\overline{B}}
\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
\providecommand{\MC}{\text{MC}}
\providecommand{\cM}{\mathcal{M}}
\providecommand{\cC}{\mathcal{C}}
\providecommand{\cO}{\mathcal{O}}
\providecommand{\cP}{\mathcal{P}}
\providecommand{\Eone}{E_1}
\providecommand{\Convinf}{\mathrm{Conv}_\infty}
\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
\providecommand{\orline}[1]{\mathrm{or}(#1)}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Rep}{\mathrm{Rep}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\label{ch:preface}
 succeeded in 51ms:
\chapter{Introduction}

\section{From a point to a curve}
\label{sec:volume-one-route}

Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. In the non-abelian affine Kac--Moody case the precise degree-$2$ formula is $\kappa(\cA) = \mathrm{av}(r_\cA(z)) + \dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.

The organising principle is as follows. The geometry of the
curve~$X$ determines an operad (the Fulton--MacPherson
compactifications $\FM_n(X)$ with their boundary strata); the
operad determines a bar complex (the cofree coalgebra
$T^c(s^{-1}\bar\cA)$ with its residue-extraction differential);
the bar complex computes the invariants (the modular
characteristic~$\kappa$, the shadow obstruction tower, the
chiral Hochschild cohomology $\ChirHoch^*$). At each step the
passage is forced: one form ($\eta = d\log(z_1 - z_2)$), one
relation (Arnold), one object ($\Theta_\cA$), one equation
($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$).

The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
 succeeded in 50ms:
standalone/analytic_sewing.tex
standalone/drinfeld_kohno_bridge.pdf
standalone/theorem_index.tex
standalone/computations.tex
standalone/cover_letter_shadow_towers.pdf
standalone/N6_shadow_formality.tex
standalone/editorial.pdf
standalone/gaudin_from_collision.tex
standalone/ordered_chiral_homology.tex
standalone/three_dimensional_quantum_gravity.pdf
standalone/programme_summary_section1.tex
standalone/programme_summary_sections5_8.tex
standalone/e1_primacy_ordered_bar.tex
standalone/virasoro_r_matrix.tex
standalone/cover_letter_virasoro_r_matrix.pdf
standalone/cover_letter_garland_lepowsky.pdf
standalone/en_chiral_operadic_circle.tex
standalone/five_theorems_modular_koszul.tex
standalone/N4_mc4_completion.tex
standalone/riccati.tex

thinking
**Evaluating theorem status**

I see there's a huge search output, and I need to determine the actual status of theorems in higher_genus_foundations.tex. I’ll inspect around the specific theorem and related labels like thm:genus-universality, cor:kappa-additivity, and others. Opening up around those, I think, will help clarify things. I might also need to look into the anomaly-Koszul label as well. There’s a lot to unpack here!
codex
I’ve isolated the drift surface: the core inconsistency is that the live theorem files still advertise `thm:genus-universality` and `thm:universal-generating-function` as fully `ProvedHere`, while several downstream summaries already know the claim should be narrower. I’m reading the theorem blocks and the dependency remarks now so I can align the exact split instead of papering over phrases.
exec
/bin/zsh -lc "sed -n '5300,6065p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2 = 0$
for \emph{all} $g \geq 1$, by Mumford's relation.
\end{example}

\subsection{Summary table: obstruction classes for key examples}
\label{subsec:obstruction-summary-table}

\begin{table}[ht]
\centering
\caption{Genus-$g$ obstruction classes. For single-generator families, $\mathrm{obs}_g = \kappa \cdot \lambda_g$
 \textup{(}UNIFORM-WEIGHT\textup{)} holds unconditionally at all genera. For multi-weight families
 \textup{(}$W_3$\textup{)}, the formula is unconditional at $g = 1$;
 at $g \geq 2$, a cross-channel correction
 $\delta F_g^{\mathrm{cross}} \neq 0$
 \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
 \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.}
\label{tab:obstruction-summary}
\begin{tabular}{|l|c|c|}
\hline
\textbf{Chiral Algebra} & \textbf{Obstruction $\text{obs}_g$} & \textbf{Physical Meaning} \\
exec
/bin/zsh -lc "sed -n '1,220p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1880,1965p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"genus-universality|universal-generating-function|cor:kappa-additivity|family-index|modular-characteristic|obs_g\\(|obs_g|Theorem D\" standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2800,2915p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"anomaly-Koszul|anomaly-koszul|Koszul anomaly|Theorem~D|thm:anomaly\" chapters standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\begin{proposition}[Central charge genus series; \ClaimStatusProvedHere]\label{prop:complementarity-genus-series}
For $\widehat{\mathfrak{sl}}_{2,k}$, the generating function encoding all genus-$g$ free energies is:
\begin{equation}\label{eq:generating-function}
\sum_{g=1}^{\infty} F_g(\widehat{\mathfrak{sl}}_{2,k}) \, x^{2g} = \frac{3(k+2)}{4} \left(\frac{x/2}{\sin(x/2)} - 1\right)
\end{equation}
with radius of convergence $|x| < 2\pi$.
\end{proposition}

\begin{proof}
The standard expansion of $t/\sin(t)$ is:
\[
\frac{t}{\sin t} = 1 + \sum_{g=1}^{\infty} \frac{(2^{2g}-2)\,|B_{2g}|}{(2g)!}\, t^{2g}
\]
(the coefficients $(2^{2g}-2)|B_{2g}|/(2g)!$ arise from the partial fraction expansion of $\csc(t)$; the first two terms $1 + t^2/6 + 7t^4/360$ are verified directly). Substituting $t = x/2$:
\[
\frac{x/2}{\sin(x/2)} = 1 + \sum_{g=1}^{\infty} \frac{(2^{2g}-2)\,|B_{2g}|}{(2g)!} \cdot \frac{x^{2g}}{2^{2g}}
= 1 + \sum_{g=1}^{\infty} \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\, x^{2g}
\]
using $(2^{2g}-2)/2^{2g} = (2^{2g-1}-1)/2^{2g-1}$. Multiplying by $\kappa = 3(k+2)/4$ gives~\eqref{eq:generating-function}. The radius of convergence is $|x| = 2\pi$, the first zero of $\sin(x/2)$.
\end{proof}
 succeeded in 52ms:
% ======================================================================
% GUIDE TO MAIN RESULTS
% A compact reference for the five main theorems and their dependencies.
% ======================================================================

\chapter*{Guide to main results}
\addcontentsline{toc}{chapter}{Guide to main results}
\label{ch:guide}%

\noindent
The principal results, with labels, locations, and logical
dependencies. All five theorems hold for augmented chiral
algebras~$\cA$ on a smooth projective curve~$X$ satisfying the
standing finiteness conditions (\S\ref{sec:standing-assumptions}).

\medskip

\renewcommand{\arraystretch}{1.3}
\begin{longtable}{@{}lp{8.5cm}l@{}}
\textsc{Label} & \textsc{Statement} & \textsc{Location} \\
 succeeded in 50ms:
standalone/theorem_index.tex:84:theorem & \detokenize{thm:guide-family-index} & \detokenize{Family index theorem for genus expansions} & \texttt{ProvedHere} & \detokenize{chapters/frame/guide_to_main_results.tex:240}\\
standalone/theorem_index.tex:752:theorem & \detokenize{thm:genus-universality} & \detokenize{Genus universality} & \texttt{ProvedHere} & \detokenize{chapters/theory/higher_genus_foundations.tex:5339}\\
standalone/theorem_index.tex:783:theorem & \detokenize{thm:modular-characteristic} & \detokenize{Modular characteristic} & \texttt{ProvedHere} & \detokenize{chapters/theory/higher_genus_modular_koszul.tex:2845}\\
standalone/theorem_index.tex:1407:theorem & \detokenize{thm:universal-generating-function} & \detokenize{Universal generating function} & \texttt{ProvedHere} & \detokenize{chapters/examples/genus_expansions.tex:1914}\\
standalone/theorem_index.tex:2105:theorem & \detokenize{thm:family-index} & \detokenize{Family index theorem for genus expansions} & \texttt{ProvedHere} & \detokenize{chapters/connections/concordance.tex:6032}\\
standalone/five_theorems_modular_koszul.tex:105:$\obs_g(\cA) = \kappa(\cA) \cdot \lambda_g$
standalone/five_theorems_modular_koszul.tex:239: ($\obs_g = \kappa \cdot \lambda_g$, UNIFORM-WEIGHT).
standalone/five_theorems_modular_koszul.tex:968:\section{Theorem D: the genus expansion}
standalone/five_theorems_modular_koszul.tex:977:\begin{theorem}[Theorem D: genus universality]
standalone/five_theorems_modular_koszul.tex:978:\label{thm:genus-universality}
standalone/five_theorems_modular_koszul.tex:997: \obs_g(\cA) = \kappa(\cA) \cdot \lambda_g
standalone/five_theorems_modular_koszul.tex:1323:$\obs_g = \kappa \cdot \lambda_g$; without the correct
standalone/five_theorems_modular_koszul.tex:1462: $\obs_g = \kappa \cdot \lambda_g$ could hold
standalone/five_theorems_modular_koszul.tex:1502:D & $\obs_g = \kappa \cdot \lambda_g$
standalone/five_theorems_modular_koszul.tex:1656:\subsection{Theorem D for $\cH_k$: the genus expansion}
standalone/five_theorems_modular_koszul.tex:1663:\obs_g(\cH_k) \;=\; k \cdot \lambda_g
standalone/five_theorems_modular_koszul.tex:2267:$\obs_g = \kappa \cdot \lambda_g$ is unconditional at
standalone/programme_summary_sections2_4.tex:175:\begin{equation}\label{eq:genus-universality}
standalone/programme_summary_sections2_4.tex:432:\subsection{Theorem D: the modular characteristic}
standalone/chiral_chern_weil.tex:104:$\obs_g(\cA) = \kappa(\cA)\cdot\lambda_g$ on $\Mbar_g$
 succeeded in 50ms:
Convention~\ref{conv:higher-genus-differentials}. Part~\textup{(ii)} is
the Verdier intertwining axiom~\textup{\ref{MK:verdier-htpy}}, realized
on the dg model by
Theorem~\ref{thm:bar-cobar-isomorphism-main}. Part~\textup{(iii)} is
Theorem~\ref{thm:higher-genus-inversion}. Part~\textup{(iv)} is
Theorem~\ref{thm:universal-theta}, made unconditional by
Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
\textup{(i)}--\textup{(iii)} are exactly the stated trace, clutching,
and Verdier properties.
\end{proof}

\begin{remark}[The modular characteristic hierarchy]
\label{rem:modular-characteristic-package}
\label{rem:characteristic-hierarchy}
\index{modular characteristic!hierarchy|textbf}
The package~$\mathcal{C}_{\cA}$ \eqref{eq:full-package-quintuple}
has three logarithmic levels:
(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
exponential $=$ modular period~$N$;
(2)~spectral: $\Delta_{\cA}(x)$
 succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:3583:Theorem~D) or Kac--Moody-type ($\kappa + \kappa' = 0$).
chapters/examples/w_algebras_deep.tex:5193:under cosets (Theorem~D):
chapters/examples/symmetric_orbifolds.tex:194:status: Theorem~D is proved (Proposition~\ref{prop:symn-kappa}),
standalone/theorem_index.tex:2120:theorem & \detokenize{thm:anomaly-koszul} & \detokenize{Anomaly cancellation as Koszul constraint} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1869}\\
standalone/theorem_index.tex:2121:theorem & \detokenize{thm:anomaly-physical-genus0} & \detokenize{Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0}} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1903}\\
standalone/theorem_index.tex:2122:theorem & \detokenize{thm:anomaly-physical-km-w} & \detokenize{Physical anomaly cancellation for affine Kac--Moody algebras} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1919}\\
standalone/computations.tex:424:The per-channel (diagonal) graph sum, computed by applying Theorem~D
chapters/examples/lattice_foundations.tex:230:for single-generator algebras of uniform conformal weight (Theorem~D, Remark~\ref{rem:propagator-weight-universality}).
chapters/examples/lattice_foundations.tex:5131:(Theorem~D). The higher-degree corrections at genus~$1$ involve
chapters/examples/y_algebras.tex:415:sums (Theorem~D, additivity) gives the channel-by-channel
standalone/e1_primacy_ordered_bar.tex:878:$\mathfrak{C}(\cA)$ is~\cite[Theorem~D(iii)]{Lor26}.
standalone/e1_primacy_ordered_bar.tex:1208:Theorem~D.
standalone/e1_primacy_ordered_bar.tex:1227:\begin{remark}[Theorem~D is the cleanest example]
standalone/e1_primacy_ordered_bar.tex:1229:Among the five, Theorem~D makes the $\Eone$ primacy thesis most
chapters/examples/heisenberg_eisenstein.tex:58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
chapters/examples/heisenberg_eisenstein.tex:2362:= F_g(\cH_\kappa)$ which is the genus tower of Theorem~D.
standalone/five_theorems_modular_koszul.tex:103:Theorem~D identifies the genus expansion: on the
standalone/five_theorems_modular_koszul.tex:1146:Theorem~D identifies a universal genus expansion governed by
standalone/five_theorems_modular_koszul.tex:1302:is vacuous and the genus expansion of Theorem~D is
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the

thinking
**Investigating G01 Updates**

I’m focusing on the status after G01 addresses the universality gap. The user points out that once G01 fixes it, updates should propagate to all downstream surfaces. However, I’m wondering if our local files are up to date. I think I should check for any new remarks or proof routes related to Theorem D. Maybe G01 modified the proof route or the genus split? I need to inspect the higher genus modular Koszul remarks and the family-index theorem status too.
codex
I now have the source of drift. The core theorems still claim a full `ProvedHere` all-genera package, but the surrounding prose already contains the narrower language “proved scalar lane / genus-1 unconditional / multi-weight correction.” I’m checking whether G01 actually completed the clutching-uniqueness+GRR route or whether the honest fix is to split genus-1 from all-genera.
exec
/bin/zsh -lc "sed -n '2940,3115p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
strong scalar ansatz of
Theorem~\ref{thm:multi-generator-universality}.
Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
Part~(iii) is the duality clause of
Theorem~\ref{thm:genus-universality}(ii).
Part~(iv) is Corollary~\ref{cor:kappa-additivity};
Theorem~\ref{thm:anomaly-koszul} is the matter-ghost specialization.
The group homomorphism property follows from~(iv): additivity
under tensor product and $\kappa(\mathbb{C}) = 0$ (the trivial
algebra has no curvature) give a homomorphism to $(\mathbb{C}, +)$.
\end{proof}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-d-lagrangian}
\index{Lagrangian self-intersection!Theorem D}
Volume~II interprets $\kappa(\cA) \cdot \omega_g$ as the
Kodaira--Spencer class of the Lagrangian family over the Hodge
bundle: the boundary Lagrangian
$\mathcal{L} \hookrightarrow \mathcal{M}$ varies over
$\overline{\mathcal{M}}_g$, and $\kappa(\cA)$ is the first-order
exec
/bin/zsh -lc "sed -n '6488,6545p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"clutching|GRR|Grothendieck--Riemann--Roch|uniqueness\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/genus_expansions.tex chapters/connections/concordance.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1835,2015p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1400,1475p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '470,680p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\kappa(\cA)\lambda_g
\qquad
\textup{(UNIFORM-WEIGHT)}.
\]

By definition of the scalar free energy, $F_g(\cA)$ is the pairing of
this scalar class with $\psi_1^{2g-2}$ on
$\overline{\mathcal{M}}_{g,1}$, so \eqref{eq:grr-bridge} follows.
The Faber--Pandharipande formula
\textup{(}Theorem~\textup{\ref{thm:mumford-formula}}\textup{)}
evaluates the integral as
\[
\lambda_g^{\mathrm{FP}}
\;=\;
\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!},
\]
and summing these coefficients gives
\eqref{eq:grr-bridge-total}. At genus~$1$ the same computation yields
$F_1(\cA) = \kappa(\cA)/24$ for every modular Koszul algebra.
\end{proof}
 succeeded in 51ms:
chapters/examples/genus_expansions.tex:17:Grothendieck--Riemann--Roch pushforward.
chapters/examples/genus_expansions.tex:61:governs the clutching contributions to
chapters/examples/genus_expansions.tex:169:This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
chapters/connections/concordance.tex:1356:\item The quartic clutching law
chapters/connections/concordance.tex:1357: (Theorem~\ref{thm:nms-clutching-law-modular-resonance}) has a
chapters/connections/concordance.tex:1363:\item The log clutching conjecture is proved:
chapters/connections/concordance.tex:1364: Theorem~\ref{thm:log-clutching-degeneration} (formerly a
chapters/connections/concordance.tex:1399: clutching law (Theorem~\ref{thm:log-clutching-degeneration}),
chapters/connections/concordance.tex:1401: clutching. If revised, these revert to conjectured; the
chapters/connections/concordance.tex:1448:Thm~\ref{thm:log-clutching-degeneration}
chapters/connections/concordance.tex:1449: (log clutching)
chapters/connections/concordance.tex:1451: & Reverts to conjectured; quartic clutching law
chapters/connections/concordance.tex:1452: (Thm~\ref{thm:nms-clutching-law-modular-resonance})
chapters/connections/concordance.tex:1458: & Log-geometric derivation lost; the clutching law
chapters/connections/concordance.tex:1687: ambient $D^2 = 0$ and log clutching (\cite{Mok25});
chapters/connections/concordance.tex:1730:the clutching law becomes a literal boundary factorisation theorem
chapters/connections/concordance.tex:1732:(Construction~\ref{const:vol1-clutching-law-logfm}).
chapters/connections/concordance.tex:2051: clutching laws and a quartic resonance class.
chapters/connections/concordance.tex:2058: non-separating clutching: the genus-$1$ Hessian correction
chapters/connections/concordance.tex:2103: (Theorem~\ref{thm:nms-clutching-law-modular-resonance}) is the
 succeeded in 51ms:
geometric boundary (controlled by the period map and the
clutching morphisms of stable curves). The interaction between them
is the curvature~$\kappa(\cA)$: the fibrewise bar differential fails to
be nilpotent precisely because the vertical and horizontal
boundaries do not commute.

\subsection*{The five theorems}

Five theorems extract the structural content of the bar complex.

\medskip

\noindent\textbf{Theorem~A} (bar-cobar adjunction and Verdier
intertwining). The bar functor~$B$ and the cobar functor~$\Omega$
form an adjoint pair on the category of chiral algebras
over~$\operatorname{Ran}(X)$. Verdier duality on~$\operatorname{Ran}(X)$
intertwines the bar of~$\cA$ with the bar of the Koszul
dual: $\mathbb D_{\operatorname{Ran}}(B(\cA))\simeq\cA^!_\infty$.
\medskip

 succeeded in 51ms:
$\mathrm{Res}_{z_i \to z_j} \eta_{ij}$ extracts the
OPE coefficient $J^a(z_i) J^b(z_j) \sim k \kappa^{ab}/(z_i-z_j)^2
+ f^{ab}_c J^c/(z_i-z_j)$: the double pole contributes the
Killing contraction $k\kappa^{ab}$ and the simple pole the
structure constants~$f^{ab}_c$. These are precisely the
assignments in Bar-Natan's construction of weight systems from
Lie algebras~\cite{BarNatan95}.
\end{proof}

\begin{remark}[Scope]\label{rem:vassiliev-scope}
Proposition~\ref{prop:vassiliev-genus0} establishes the genus-$0$
weight system extraction. The Feynman transform of $\mathrm{Com}$
recovers the full graph complex computing Vassiliev invariants
(Getzler--Kapranov \cite{GeK98}), and our identification
$\barB^{\mathrm{full}} \simeq \mathrm{FT}$
(Theorem~\ref{thm:prism-higher-genus}) extends this to Koszul
chiral algebras. The gap at higher genus is the passage from
complex curves to real $1$-manifolds: our propagators are
holomorphic, while Kontsevich's are real. Comparing requires an
analytic continuation argument from holomorphic to topological
 succeeded in 52ms:
characteristic $\kappa(\cH_k^!) = -k$.
The cobar of the bar is
$\Omega(\barB(\cH_k)) = T(s\,\C\cdot s^{-1}J) = \C[J]$,
which is $\cH_k$ as a graded algebra. The counit
$\varepsilon\colon\Omega(\barB(\cH_k)) \to \cH_k$ is a
quasi-isomorphism: the Heisenberg is Koszul.

\smallskip
\noindent\textbf{Theorem~C (complementarity).}\enspace
Here the center local system is constant, so the ambient complex
already splits in the form asserted by Theorem~C:
\[
Q_g(\cH_k) \oplus Q_g(\cH_k^!) \cong
H^*(\overline{\cM}_g, \cZ_{\cH_k}).
\]
For $g \ge 1$ the two summands are Verdier-Lagrangian partners.
On the scalar shadow one recovers the Heisenberg identity
$\kappa(\cH_k) + \kappa(\cH_k^!) = k + (-k) = 0$.

\smallskip
🌐 Searching the web...
🌐 Searched the web
codex
The likely answer is becoming clearer: G01 seems to have installed an independent GRR route and a clutching-based bridge, not just weaker prose. I’m verifying whether that route is actually load-bearing enough to keep Theorem D as `ProvedHere`, or whether some core theorem block still depends on the unresolved strong scalar ansatz.
exec
/bin/zsh -lc "sed -n '6378,6485p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6020,6245p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"multi-generator-universality|strong scalar ansatz|resolved negatively|proved uniform-weight scalar lane|family index theorem|non-circular\" chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/concordance.tex chapters/examples/genus_expansions.tex standalone/*.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|begin\\{theorem\\}\\[Family index|Family index theorem for genus expansions\" chapters standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
function is a Hodge integral :
\begin{equation}\label{eq:grr-bridge}
F_g(\cA) \;=\; \kappa(\cA) \cdot
\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, c_g(\mathbb{E}),
\end{equation}
where $\mathbb{E}$ is the Hodge bundle and $\psi_1$ is the
 succeeded in 52ms:
Kac--Moody algebras, $\kappa$ further satisfies
$\kappa(\mathcal{A}^!) = -\kappa(\mathcal{A})$, making it a group
homomorphism from $K_0(\mathrm{KCA}_{\mathrm{KM}})$ to~$\mathbb{Q}$.
For $\mathcal{W}$-algebras the duality relation is affine
\textup{(}$\kappa' = \varrho(\mathfrak{g})\,K - \kappa$, where
$\varrho(\mathfrak{g}) = \sum 1/(m_i+1)$\textup{)}, so $\kappa$ is
additive but does not intertwine Koszul duality with negation.
\end{corollary}

\begin{proof}
The universal genus-$1$ identity
$\mathrm{obs}_1(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_1$
\textup{(g=1 only; all-weight at g=1 is unconditional)}
is Theorem~\ref{thm:genus-universality}; on the proved scalar lane,
the same theorem gives the higher-genus classes
$\mathrm{obs}_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g$ Since each $\lambda_g$ is tautological, these classes lie in the
tautological ring. Additivity
$\kappa(\mathcal{A} \otimes \mathcal{B}) =
\kappa(\mathcal{A}) + \kappa(\mathcal{B})$
\textup{(}Corollary~\ref{cor:kappa-additivity}\textup{)} gives a group
 succeeded in 50ms:
standalone/introduction_full_survey.tex:780:Open Problem~\ref{op:multi-generator-universality} resolved
standalone/introduction_full_survey.tex:1623: Open Problem~\ref{op:multi-generator-universality} resolved
standalone/introduction_full_survey.tex:2122:Open Problem~\ref{op:multi-generator-universality} negatively:
chapters/frame/preface.tex:3097:resolving Open Problem~\ref{op:multi-generator-universality}
chapters/examples/genus_expansions.tex:169:This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
chapters/examples/genus_expansions.tex:293:Open Problem~\textup{\ref{op:multi-generator-universality}} resolved
chapters/examples/genus_expansions.tex:1933:Proposition~\ref{prop:complementarity-genus-series} is the specialization $\kappa = 3(k+2)/4$ (the $\widehat{\mathfrak{sl}}_2$ value from the Master Table). The all-genera generating function applies to all modular Koszul algebras on the uniform-weight lane: Heisenberg ($\kappa = k$), affine Kac--Moody, and Virasoro ($\kappa = c/2$). For multi-weight algebras such as $\mathcal{W}_N$ ($N \geq 3$, $\kappa = c(H_N - 1)$), the genus-$1$ clause $F_1 = \kappa/24$ is unconditional; at $g \geq 2$ the scalar formula receives a cross-channel correction $\delta F_g^{\mathrm{cross}}$ from mixed-channel boundary graphs (Theorem~\ref{thm:multi-weight-genus-expansion}, resolving Open Problem~\ref{op:multi-generator-universality} negatively).
chapters/examples/genus_expansions.tex:2743:Open Problem~\ref{op:multi-generator-universality} resolved
chapters/examples/genus_expansions.tex:3041:Open Problem~\ref{op:multi-generator-universality} resolved
standalone/computations.tex:450:(\textbf{op:multi-generator-universality}) is resolved negatively:
standalone/survey_modular_koszul_duality_v2.tex:7770:(resolving Open Problem~\ref{op:multi-generator-universality}
standalone/survey_modular_koszul_duality_v2.tex:8013:Problem~\ref{op:multi-generator-universality}), BV/BRST${}={}$bar
standalone/shadow_towers.tex:271:resolved negatively
standalone/shadow_towers.tex:1715:\textup{op:multi-generator-universality} is resolved negatively:
standalone/shadow_towers.tex:2031:The open problem \textup{op:multi-generator-universality}
standalone/shadow_towers.tex:2032:is resolved negatively. The full genus-$2$
standalone/five_theorems_modular_koszul.tex:1413:\subsection{The non-circular routing}
standalone/five_theorems_modular_koszul.tex:1419:that the chain has a non-circular anchor.
standalone/five_theorems_modular_koszul.tex:1421:\begin{remark}[Primitive non-circular anchor]
standalone/five_theorems_modular_koszul.tex:1422:\label{rem:non-circular}
 succeeded in 50ms:
standalone/theorem_index.tex:84:theorem & \detokenize{thm:guide-family-index} & \detokenize{Family index theorem for genus expansions} & \texttt{ProvedHere} & \detokenize{chapters/frame/guide_to_main_results.tex:240}\\
standalone/theorem_index.tex:2105:theorem & \detokenize{thm:family-index} & \detokenize{Family index theorem for genus expansions} & \texttt{ProvedHere} & \detokenize{chapters/connections/concordance.tex:6032}\\
chapters/frame/guide_to_main_results.tex:240:\begin{theorem}[Family index theorem for genus expansions;
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:6034:\begin{theorem}[Family index theorem for genus expansions;
chapters/connections/concordance.tex:6035:\ClaimStatusProvedHere]\label{thm:family-index}
exec
/bin/zsh -lc "rg -n \"thm:genus-universality|thm:universal-generating-function|cor:kappa-additivity|thm:family-index|thm:modular-characteristic|thm:anomaly-koszul\" metadata standalone/theorem_index.tex chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:4594: \textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)}.
chapters/theory/introduction.tex:57:(Theorem~\ref{thm:modular-characteristic}).
chapters/theory/introduction.tex:612: Theorem~\ref{thm:genus-universality}).
chapters/theory/introduction.tex:639: \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
chapters/theory/introduction.tex:1780: (Theorem~\ref{thm:genus-universality}). The natural home is
chapters/theory/introduction.tex:1915:(Theorem~\ref{thm:universal-generating-function}) are consequences
chapters/connections/concordance.tex:63: Thm~\ref{thm:modular-characteristic}\textup{)};
chapters/connections/concordance.tex:307: (Theorem~\ref{thm:genus-universality}).}
chapters/connections/concordance.tex:667: (Theorem~\ref{thm:genus-universality}), which extends the FF involution
chapters/connections/concordance.tex:2463: \textup{(}Theorem~\ref{thm:genus-universality}\textup{)};
chapters/connections/concordance.tex:4790:Theorem~\ref{thm:modular-characteristic}) establishes the scalar
chapters/connections/concordance.tex:4815:Index & Scalar genus series on the uniform-weight lane; & \textbf{Proved} on the stated lane; & Thms~\ref{thm:modular-characteristic}, \\
chapters/connections/concordance.tex:4816: & genus-$1$ unconditional; family-index routed downstream & genus-$1$ universal & \ref{thm:family-index} \\[2pt]
chapters/connections/concordance.tex:5386:(Theorem~\ref{thm:genus-universality}).
chapters/connections/concordance.tex:5393:(Theorem~\ref{thm:genus-universality}). The clutching compatibility
chapters/connections/concordance.tex:5518:$\kappa(\cA) \cdot \lambda_g$ (proved, Theorem~\ref{thm:genus-universality}).
chapters/connections/concordance.tex:6029:expansion (Theorem~\ref{thm:universal-generating-function})
chapters/connections/concordance.tex:6035:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/connections/concordance.tex:6099:\textup{(}Theorem~\textup{\ref{thm:genus-universality}(ii))}
chapters/connections/concordance.tex:6118:\text{Theorem~\ref{thm:genus-universality}}


thinking
**Inferring theorem status**

I’m working on understanding the actual status of some mathematical propositions. It appears that the proposition regarding the grr-bridge is proved on a uniform-weight scalar lane, and there’s already a genus-universality theorem for that. The new status hints that Theorem D remains proved, emphasizing its application across certain genera. The user pointed out a distinction regarding full proofs or splits between genus-1 and all genera, but it seems we’re sticking to a more restricted interpretation for now. I’ll need to ensure this understanding propagates correctly.
thinking
**Updating theorem propagation**

The user mentioned that after fixing the universality gap with G01, we should propagate updates to all downstream surfaces, especially concerning non-circular routes and the family-index theorem. This sounds essential, as we need to update any ambiguous or outdated files, including targeted search terms. I should consider changing the cor:kappa-additivity proof to route through genus-1 only. I’ll also need to examine the status of the universal generating function and inspect the family-index theorem around line 240 to ensure everything is current. It’s a lot, but I think I can manage it!
codex
The theorem surface itself now supports a truthful narrow claim: `ProvedHere` on the uniform-weight scalar lane, universal at genus 1 for all families, with multi-weight `g >= 2` corrected by `\delta F_g^{cross}`. The remaining job is propagation: several summaries still flatten that into “all genera” or use the old proof direction.
exec
/bin/zsh -lc "sed -n '1,140p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Introduction}

\section{From a point to a curve}
\label{sec:volume-one-route}

Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. In the non-abelian affine Kac--Moody case the precise degree-$2$ formula is $\kappa(\cA) = \mathrm{av}(r_\cA(z)) + \dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.

The organising principle is as follows. The geometry of the
curve~$X$ determines an operad (the Fulton--MacPherson
compactifications $\FM_n(X)$ with their boundary strata); the
operad determines a bar complex (the cofree coalgebra
$T^c(s^{-1}\bar\cA)$ with its residue-extraction differential);
the bar complex computes the invariants (the modular
characteristic~$\kappa$, the shadow obstruction tower, the
chiral Hochschild cohomology $\ChirHoch^*$). At each step the
passage is forced: one form ($\eta = d\log(z_1 - z_2)$), one
relation (Arnold), one object ($\Theta_\cA$), one equation
($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$).

The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
exec
/bin/zsh -lc "sed -n '1428,1468p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '330,770p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2398,2425p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,110p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '970,1045p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3060,3198p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6000,6375p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\medskip

\noindent\textbf{Theorem~C} (complementarity). The genus-$g$
cohomology of the center local system decomposes into two
Lagrangian halves, one controlled by~$\cA$ and the other by the
Koszul dual~$\cA^!$:
$R\Gamma(\overline{\cM}_g,\mathcal Z_\cA)
\simeq\mathbf Q_g(\cA)\oplus\mathbf Q_g(\cA^!)$.
The Verdier-side Lagrangian splitting is proved; the ambient
shifted-symplectic upgrade is conditional on perfectness and
nondegeneracy.
\medskip

\noindent\textbf{Theorem~D} (modular characteristic).
At genus~$1$ for every family, and at all genera on the proved
uniform-weight lane, the obstruction class factors as
$\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$, where
$\kappa(\cA)$ is a single scalar determined by the OPE
\textup{(UNIFORM-WEIGHT)}. The theorem includes additivity,
Koszul-duality constraints, and the Faber--Pandharipande
 succeeded in 51ms:

\section{The five theorems}
\label{sec:NAP-unifying}
\label{sec:main-results-complete}
\index{Koszul duality!chiral|textbf}
\index{modular Koszul duality|textbf}
\index{quantum corrections!as modular completion}

The selection principle determines which algebraic inputs are admissible. The five theorems determine what survives once an admissible input is placed on a curve.

\medskip\noindent\textbf{The forced chain A $\Rightarrow$ B $\Rightarrow$ C $\Rightarrow$ D $\Rightarrow$ H.}
Without Theorem~A, the dual object is only a formal symbol: there is
no theorem identifying
$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ with a chiral algebra.
Without Theorem~B, the bar construction can lose the boundary algebra.
Without Theorem~C, higher-genus deformation theory has no canonical
polarization. Without Theorem~D, the genus tower has no distinguished
scalar shadow. Without Theorem~H, the bulk coefficient ring is
uncontrolled. The unique survivor of all five failures is the
genus-completed bar differential, first in the ordered $E_1$ theory and
 succeeded in 51ms:
\medskip

\noindent\textbf{The scalar curvature $\kappa(\cA)$.}\enspace
The degree-two, genus-zero trace:
\[
\kappa(\cA)
\;=\;
\operatorname{tr}(\Theta_\cA)_{2,0}
\;\in\;\Bbbk
\]
This is the first Chern class of the modular bar bundle:
$\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera, and unconditionally
at genus~$1$. On
the $E_1$ side, $\kappa(\cA)$ is the $\Sigma_2$-coinvariant of
the $R$-matrix $r(z)$; averaging collapses the $z$-dependent
profile to a number. Explicit values:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lccl}
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
Koszul dual: $\mathrm{Vir}_{26-c}$. At $c = 26$ the dual is
uncurved ($\kappa(\mathrm{Vir}_0) = 0$); at $c = 0$ the algebra
itself is uncurved; at $c = 13$ the algebra is self-dual
($\kappa + \kappa^! = 13$, the unique fixed point). The critical
dimension $c = 26$ is the statement that the Koszul dual's
curvature vanishes, not that the algebra's does: the string ghost
system $bc$ at $c_{\mathrm{ghost}} = -26$ is the complementarity
partner.

\subsection*{Multi-weight: the cross-channel correction}

The Virasoro algebra has a single generator of weight~$2$. The
scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
propagator weight~$1$ couples to a single Hodge bundle
$\mathbb{E}_1$. The question forced by the depth classification
is whether the scalar formula survives the passage to multiple
generators at different conformal weights.

The $\cW_3$-algebra answers negatively. Two generators
$T$ (weight~$2$) and $W$ (weight~$3$); the $WW$~OPE contains the
 succeeded in 51ms:

\subsection{Statement}

The Lagrangian decomposition of Theorem~C separates $\cA$ from
$\cA^!$ on moduli space, but does not identify what the scalar
projection $\kappa$ governs at each genus.

\begin{theorem}[Theorem D: genus universality]
\label{thm:genus-universality}
Let $\cA$ be a chirally Koszul chiral algebra with modular
characteristic $\kappa(\cA)$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Genus $1$ (unconditional).}
 The genus-$1$ obstruction class is
 \[
 \obs_1(\cA) = \kappa(\cA) \cdot \lambda_1
 \in H^*(\Mbar_{1,1}),
 \]
 and the genus-$1$ free energy is
 $F_1(\cA) = \kappa(\cA)/24$.
 succeeded in 51ms:
two-dimensional deformation space $(T,W)$. At $c=50$:
$x_1\to\infty$, $x_2=3/2$.

For $\beta\gamma$: the unique standard family with
$\kappa<0$. Branch point at $x=-1/2$; the genus tower has
alternating signs.

\emph{Duality.}
$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
the spectral discriminant is self-dual. For
$\widehat{\mathfrak{sl}}_2$: the zero at $1/k$ corresponds
to level~$k$; the zero at $1/(k{+}4)$ corresponds to the
dual level $-k-4$. The product of the two zeros is
$1/(k(k{+}4))$; their sum is $(2k{+}4)/(k(k{+}4))=2/k+2/(k{+}4)
\to 0$ as $k\to\infty$.

\emph{Rank.}
$\operatorname{rank}(\Delta_\cA)
=\deg\Delta_\cA
=\dim H^1_{\mathrm{cyc,prim}}(\cA)$: the number of independent

thinking
**Defining scope for updates**

I need to determine the exact scope for fixing target files and standalone files using specific search terms. The user referred to "standalone/*.tex" and various terms like 'obs_g', 'Theorem D', and others. It seems there could be many standalone files, so I should be thorough yet precise in my approach. I’m considering a broad search and replace pattern, but I also need to understand AP230 and AP228 better and see if I can search in CLAUDE.
codex
I’ve confirmed the live theorem stance: Theorem D is still `ProvedHere`, but only as “genus 1 universal for every family + all genera on the proved uniform-weight scalar lane,” with family-index downstream and non-circular. I’m now fixing the remaining mismatches against that exact boundary, especially `cor:kappa-additivity`, `thm:universal-generating-function`, and the anomaly theorem’s proof direction.
exec
/bin/zsh -lc "sed -n '1850,1945p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"AP228|AP230\" CLAUDE.md AGENTS.md chapters standalone metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
\frac{|B_{2g}|}{(2g)!} \sim \frac{2}{(2\pi)^{2g}}
\]
Since $(2^{2g-1}-1)/2^{2g-1} \to 1$ as $g \to \infty$, we obtain~\eqref{eq:Fg-asymptotics}.

In particular, $|F_{g+1}/F_g| \to 1/(2\pi)^2 \approx 0.025$, giving geometric convergence.
\end{proof}

\begin{remark}[Contrast with string amplitudes]\label{rem:convergence-vs-string}
The convergence of our genus expansion is in sharp contrast with the \emph{divergent} genus expansion of string theory, where amplitudes grow as $(2g)!$ (the volume of $\overline{\mathcal{M}}_g$ by Mirzakhani's recursion~\cite{Mirzakhani}). The distinction is structural: our $F_g$ is the integral $\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g$, which extracts a single tautological intersection number, while string amplitudes integrate over the full moduli space with a measure involving all $\lambda$-classes. The Bernoulli decay of the tautological integral $\int \psi^{2g-2}\lambda_g$ overwhelms the $(2g)!$ growth of $|B_{2g}|$.
\end{remark}

\begin{theorem}[Bernoulli universality; \ClaimStatusProvedHere]\label{thm:bernoulli-universality}
\index{Bernoulli universality}
\index{genus expansion!convergence}
The genus expansion of a modular Koszul chiral
algebra $\mathcal{A}$ is uniquely characterized by:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Convergence.} $\sum_{g=1}^\infty |F_g(\mathcal{A})| < \infty$, with geometric ratio $|F_{g+1}/F_g| \to 1/(2\pi)^2$.
\item \emph{Generating function.} $\sum_{g \geq 1} F_g\, x^{2g} = \kappa \cdot ((x/2)/\sin(x/2) - 1)$ \textup{(}UNIFORM-WEIGHT; Theorem~\textup{\ref{thm:universal-generating-function})}.
 succeeded in 51ms:
CLAUDE.md:1085:**Deep structural (AP225-AP233, from mega rescue 2026-04-13):** AP225 (CRITICAL: genus-universality gap — all-genera scalar factorization NOT proved; genus-1 unconditional; clutching-uniqueness needed for all g; affects Theorem D status), AP226 (K_0-class vs scalar — kappa is complex, K_0 multiplicity requires integer; use Chern character), AP227 (ProvedHere forwarding — proof body "By Theorem X" is ProvedElsewhere, not ProvedHere), AP228 (anomaly-Koszul dependency inversion — Thm D cites thm:anomaly-koszul which imports cor:kappa-additivity; backwards), AP229 (SC-formality propagation debt — Vol III compute carries stale class G/L), AP230 (genus-1 sufficient but claimed all-genera — route through genus-1 when only genus-1 needed), AP231 (draft artifacts in theorem statements — raw LOCAL/DRAFT markers in theorem envs), AP232 (duality clause overclaiming family scope — "affine KM and free-field" but proof only principal W_N), AP233 (compact/completed comparison gap in MC3 — bounded generation doesn't extend to completed category automatically).
exec
/bin/zsh -lc "sed -n '315,345p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,735p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '40,80p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1428,1455p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Then the dual total system
\[
 \cA_{\mathrm{tot}}^{\vee}
 \;=\; \cA_{\mathrm{matter}}^! \otimes \widetilde{\cA}_{\mathrm{ghost}}
\]
has vanishing total characteristic
\[
 \kappa(\cA_{\mathrm{tot}}^{\vee})
 \;=\; \kappa(\cA_{\mathrm{matter}}^!)
 + \kappa(\widetilde{\cA}_{\mathrm{ghost}})
 \;=\; -\kappa(\cA_{\mathrm{matter}})
 - \kappa(\cA_{\mathrm{ghost}})
 \;=\; -\kappa_{\mathrm{tot}}
 \;=\; 0,
\]
and the BRST anomaly cancellation of
Corollary~\textup{\ref{cor:anomaly-physical-genus0}} holds for
$\cA_{\mathrm{tot}}^{\vee}$ at genus~$0$.
\end{proposition}

 succeeded in 51ms:
\end{theorem}

\begin{proof}
We give four independent proofs, each arriving at the same
identity by a different route. The first two are the primary
arguments; the third and fourth provide independent confirmation.

\medskip
\noindent\textbf{Preliminary: the bar side.}
Theorem~D gives $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
for every chirally Koszul algebra on the uniform-weight lane.
The Heisenberg $\cH_\kappa$ qualifies:
\begin{itemize}[nosep]
\item $\kappa(\cH_\kappa) = \kappa$ (the level);
\item single generator of conformal weight~$1$
 (uniform-weight, no cross-channel correction at any genus;
 Remark~\ref{rem:propagator-weight-universality});
\item class~G (Gaussian): the OPE $a(z)a(w) \sim \kappa/(z{-}w)^2$
 has only a double pole, so shadow depth $r_{\max} = 2$ and all
 higher shadow components $\mathfrak{C}, \mathfrak{Q}, \ldots$
 succeeded in 51ms:
$\eta_{ij} = d\log(z_i - z_j)$ along collision divisors.
The displayed comparison is the expected physics reading of these
configuration-space forms, but the chapter does not prove the required
identification between the physical integration pairing and the Euler
characteristic of the genus-$0$ bar complex.
\end{remark}

\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
At genus~$1$, the $\hat{A}$-genus gives $F_1 = \kappa(\cA)/24$
\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
\end{remark}

\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
\index{anomaly!curvature identification}
By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
\end{remark}

\section{Gauge fixing and BRST}

 succeeded in 51ms:
classes~$\mathsf{G}$ and~$\mathsf{L}$, conditional for
class~$\mathsf{C}$ on harmonic decoupling, and fails for
class~$\mathsf{M}$. The Heisenberg case is resolved at the
scalar level at all genera:
$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
= \kappa \cdot \lambda_g^{\mathrm{FP}}$
\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
For general algebras what survives at every genus is the scalar
anomaly package: the universal MC class $\Theta_\cA$ encodes the
one-loop anomaly coefficient $\kappa(\cA)$, and its projection
onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
multi-weight correction $\delta F_g^{\mathrm{cross}}$ is where the
chain-level identification breaks: the cross-channel term in the
sewing expansion has no counterpart in the BV side until
harmonic decoupling is assumed, and class~$\mathsf{M}$ is precisely
where that assumption fails.

\begin{remark}[BRST anomaly brackets and transferred SC operations]
\label{rem:brst-anomaly-gkw}

thinking
**Evaluating metadata verification**

I need to consider the claim-surface-sync requirement for verifying metadata when status-bearing files are moved. Since line numbers might shift, the theorem_index metadata could become outdated, but that might not be essential if the theorem titles and status labels stay the same. The instruction suggests we regenerate or verify the metadata if files move. Should I run the metadata generator? It might be heavy but doable. Yet, since the user didn't specifically ask, maybe I could leave it unless necessary? I'll check for minor edits instead.
codex
I’m narrowing to the actual edits now. The concordance header table is already aligned; the remaining debt is local wording that still says “Theorem D / family index / universal generating function” too broadly, plus one proof that derives an all-genera statement when only the genus-1 input is needed.
exec
/bin/zsh -lc "rg -n \"Theorem~D|Theorem D|genus-universality|family-index|all genera|obs_g|universal-generating-function|cor:kappa-additivity|anomaly-koszul\" chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/concordance.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:62:nondegeneracy. Theorem~D identifies the universal genus-$1$ scalar
chapters/frame/preface.tex:774:\subsection*{From genus $0$ to all genera}
chapters/frame/preface.tex:799:Restoring nilpotence across all genera is the subject of Section~2.
chapters/frame/preface.tex:1309:the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
chapters/frame/preface.tex:1441:\noindent\textbf{Theorem~D} (modular characteristic).
chapters/frame/preface.tex:1442:At genus~$1$ for every family, and at all genera on the proved
chapters/frame/preface.tex:1945:\emph{Over a curve at all genera}: the $A_\infty$-products
chapters/frame/preface.tex:2118:bar complex across all genera simultaneously. The MC space of
chapters/frame/preface.tex:2342:coefficient of~$\Theta_\cA$ is the modular characteristic: Theorem~D
chapters/frame/preface.tex:2410:uniform-weight algebras at all genera, and unconditionally
chapters/frame/preface.tex:3072:scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
chapters/frame/preface.tex:3105:(Theorem~D is unconditional there) and requires the interaction of
chapters/frame/preface.tex:3178:The cross-channel correction vanishes at all genera:
chapters/frame/preface.tex:3189:cross-channel correction at all genera
chapters/frame/preface.tex:4159:characteristic (Theorem~D) is the Kodaira--Spencer class of the
chapters/frame/preface.tex:4295:(all genera)}}.
chapters/frame/preface.tex:4394:proved; MC5 is partially proved (analytic sewing at all genera,
chapters/frame/preface.tex:4452:implies Hilbert--Schmidt sewing at all genera;
chapters/frame/preface.tex:4585: the bar differential squares to zero at all genera and degrees
chapters/frame/preface.tex:4590: for uniform-weight algebras at all genera;
exec
/bin/zsh -lc "sed -n '600,655p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1296,1320p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,770p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3090,3115p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~D|Theorem D|genus-universality|family-index|all genera|obs_g|universal-generating-function|cor:kappa-additivity|anomaly-koszul\" standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 for every genus, and for $g \geq 1$ the induced pairing is perfect
 with each summand Lagrangian. At the cohomological shadow level,
 \begin{equation}\label{eq:complementarity-intro}
 Q_g(\cA) \oplus Q_g(\cA^!) \cong
 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA).
 \end{equation}
 The Verdier-side Lagrangian splitting is proved. The ambient
 shifted-symplectic upgrade is conditional on perfectness and
 nondegeneracy. Instant check: for Heisenberg the center local system
 is constant, so the decomposition is visible at once.

\item \emph{Theorem~D$_{\mathrm{scal}}$} (Genus universality,
 Theorem~\ref{thm:genus-universality}).
 The deficiency is scalar drift: genus by genus, the bar tower could
 produce unrelated numbers. Theorem~D says that on the proved
 uniform-weight lane they are forced by one scalar
 $\kappa(\cA)$, determined already at genus~$1$. For algebras whose
 strong generators have the same conformal weight,
 $\mathrm{obs}_g = \kappa \cdot \lambda_g
 \in H^*(\overline{\cM}_g)$ and
 succeeded in 51ms:
$\kappa(\cA)\cdot\tfrac{2^{2g-1}-1}{2^{2g-1}}
\cdot\tfrac{|B_{2g}|}{(2g)!}$.
The $\hat A$-genus appears from the bar complex as the connection
between chiral algebra and index theory.

The scalar $\kappa(\cA)$ is only the leading term. The bar complex
carries higher-degree data: a universal Maurer--Cartan element
$\Theta_\cA$ whose projection to degree~$r$ yields a shadow invariant
$S_r(\cA)$. The infinite tower of shadows is algebraic of degree~$2$,
governed by a single discriminant $\Delta = 8\kappa S_4$ that
classifies the standard landscape into four shadow-depth classes
(\S6). The genus-$g$ obstruction class $\alpha_g(\cA)$ admits a
universal formula in terms of $\kappa(\cA)$ and the shadow tower:
the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
higher-order corrections are determined recursively by the shadow
data $(\kappa,\alpha,S_4)$ through the Riccati algebraicity
theorem (Theorem~\ref{thm:riccati-algebraicity}).

\subsection*{Complementarity}

 succeeded in 51ms:
 into complementary Lagrangians
 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
 = H^*(\overline{\cM}_g,\, Z(\cA))$.

\item \emph{Leading coefficient}
 \textup{(}Theorem~D\textup{)}.
 $\Theta_\cA$ has \textbf{universal scalar projection}.
 On the uniform-weight lane, the degree-$2$ genus-$g$ component is
 $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
 with $\kappa(\cA)$ universal and governed by the
 $\hat{A}$-genus. At genus~$1$ this holds unconditionally
 for all families.

\item \emph{Coefficient ring}
 \textup{(}Theorem~H\textup{)}.
 $\Theta_\cA$ has \textbf{polynomial coefficients}.
 $\ChirHoch^*(\cA)$ is concentrated in degrees~$\{0,1,2\}$,
 controlling the deformation ring over which~$\Theta_\cA$ varies.
\end{enumerate}
\end{principle}
 succeeded in 51ms:
\[
F_2(\cW_3)
\;=\;
\underbrace{\frac{7c}{6912}}_{\kappa\cdot\lambda_2^{\mathrm{FP}}}
\;+\;
\underbrace{\frac{c+204}{16c}}_{\delta F_2^{\mathrm{cross}}}\,,
\]
resolving Open Problem~\ref{op:multi-generator-universality}
negatively: the scalar formula fails for multi-weight algebras at
genus~$\ge 2$. The cross-channel correction $\delta F_2$ is a
one-loop graph with mixed-weight propagators; it vanishes
identically for any algebra whose generators share a single
conformal weight (the uniform-weight locus), but is nonzero
whenever the conformal weights are distinct. Multi-weight is a
genuine genus-$2$ phenomenon: it is invisible at genus~$1$
(Theorem~D is unconditional there) and requires the interaction of
at least two distinct boundary strata.

\subsection*{Drinfeld--Sokolov reduction and the depth escalator}

 succeeded in 51ms:
standalone/programme_summary_sections5_8.tex:255:this mechanism to all generators, producing a
standalone/programme_summary_sections5_8.tex:429:correspondence at all genera.
standalone/programme_summary_sections5_8.tex:566:all genera, and the genus tower is trivial. At $c = 13$:
standalone/computations.tex:424:The per-channel (diagonal) graph sum, computed by applying Theorem~D
standalone/analytic_sewing.tex:91:amplitudes across all genera.  This paper develops the analytic
standalone/analytic_sewing.tex:98:implies trace-class closed amplitudes at all genera.  For the
standalone/analytic_sewing.tex:285:to genus one and by induction to all genera, under a list of
standalone/analytic_sewing.tex:312:Gwilliam~\cite{CG17} to all genera.
standalone/programme_summary_sections2_4.tex:171:generator (or more generally with all generators of the
standalone/programme_summary_sections2_4.tex:175:\begin{equation}\label{eq:genus-universality}
standalone/programme_summary_sections2_4.tex:232:$\delta F_g^{\mathrm{cross}} = 0$ at all genera. For
standalone/programme_summary_sections2_4.tex:296:$\kappa = 0$ and the bar complex is flat at all genera:
standalone/programme_summary_sections2_4.tex:423:holds for all modular Koszul algebras at all genera. The
standalone/programme_summary_sections2_4.tex:432:\subsection{Theorem D: the modular characteristic}
standalone/programme_summary_sections2_4.tex:453:single number. Theorem~D is the all-genera identity on the
standalone/programme_summary_sections2_4.tex:559:as~\S\ref{ssec:d-squared}, extended to all genera by Mok's
standalone/programme_summary_sections2_4.tex:766:$\kappa = 0$ the bar complex is flat at all genera:
standalone/five_theorems_modular_koszul.tex:96:standard landscape at all genera.
standalone/five_theorems_modular_koszul.tex:103:Theorem~D identifies the genus expansion: on the
standalone/five_theorems_modular_koszul.tex:105:$\obs_g(\cA) = \kappa(\cA) \cdot \lambda_g$

thinking
**Adjusting introduction lines**

I need to look over the introduction and possibly tweak it, especially around line 93, which mentions free-field algebras being exact at all genera—seems fine. However, lines around 365 and 748 might need some adjustments to include uniform-weight. I should inspect those specific spots closely to ensure they accurately reflect the intended message. It's all about refining things for clarity! Let's get to work on those lines.
codex
I’m shifting from discovery to edits. The standalones are the larger surface area: some are already correct, but several still phrase Theorem D as a blanket all-genera theorem rather than “uniform-weight all genera / genus-1 universal / multi-weight corrected.” I’m patching those exact overclaims rather than touching neutral mentions.
exec
/bin/zsh -lc "sed -n '86,100p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '358,370p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
admits no value~$3$ or any finite value $\geq 3$
(Proposition~\ref{prop:depth-gap-trichotomy}).
Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
$k \geq 3$) holds if and only if the algebra belongs to
class~$\mathbf{G}$
(Proposition~\ref{prop:sc-formal-iff-class-g}).
For free-field algebras, the scalar formula
$F_g = \kappa \cdot \lambda_g$ is exact at all genera
(all-weight): the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


Three depths measure distinct aspects of the tower.
The \emph{shadow depth} $r_{\max}$ is the largest degree at which the shadow is nonzero.
 succeeded in 52ms:
on the standard CFT-type landscape except integer-spin $\beta\gamma$.
Once both sides are present, Theorem~C forces the Verdier decomposition
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ of the ambient complex;
the Lagrangian splitting is proved, while the ambient
shifted-symplectic upgrade remains conditional on perfectness and
nondegeneracy. Tracing the same object yields Theorem~D: on the
uniform-weight modular Koszul lane,
$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
energies are the $\hat A$-series; at genus~$1$ this scalar statement is
unconditional for every family, while at genus $g \ge 2$ multi-weight
algebras acquire the explicit cross-channel term
$\delta F_g^{\mathrm{cross}}$. Theorem~H identifies the coefficient
ring of the same universal class: on the Koszul locus,
exec
/bin/zsh -lc "sed -n '2404,2415p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '742,752p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '62,76p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3068,3078p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,460p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1018,1034p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 = H^*(\overline{\cM}_g,\, Z(\cA))$.

\item \emph{Leading coefficient}
 \textup{(}Theorem~D\textup{)}.
 $\Theta_\cA$ has \textbf{universal scalar projection}.
 On the uniform-weight lane, the degree-$2$ genus-$g$ component is
 $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
 with $\kappa(\cA)$ universal and governed by the
 $\hat{A}$-genus. At genus~$1$ this holds unconditionally
 for all families.

 succeeded in 51ms:
\;=\;
\operatorname{tr}(\Theta_\cA)_{2,0}
\;\in\;\Bbbk
\]
This is the first Chern class of the modular bar bundle:
$\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera, and unconditionally
at genus~$1$. On
the $E_1$ side, $\kappa(\cA)$ is the $\Sigma_2$-coinvariant of
the $R$-matrix $r(z)$; averaging collapses the $z$-dependent
profile to a number. Explicit values:
\begin{center}
 succeeded in 51ms:

\subsection*{Multi-weight: the cross-channel correction}

The Virasoro algebra has a single generator of weight~$2$. The
scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
propagator weight~$1$ couples to a single Hodge bundle
$\mathbb{E}_1$. The question forced by the depth classification
is whether the scalar formula survives the passage to multiple
generators at different conformal weights.

The $\cW_3$-algebra answers negatively. Two generators
 succeeded in 51ms:
\let\ps@oldref\ref
\renewcommand{\ref}[1]{%
 \@ifundefined{r@#1}{\textit{full monograph}}{\ps@oldref{#1}}%
}
\makeatother

% ================================================================
\begin{document}

\title[Programme Summary: Sections 2--4]
{Modular Koszul Duality: Sections 2--4}

\author{Raeez Lorgat}
\address{Perimeter Institute for Theoretical Physics,
 Waterloo, ON N2L 2Y5, Canada}
 succeeded in 51ms:
\end{theorem}

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi, is conditional on
perfectness and nondegeneracy of the cyclic pairing.

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 succeeded in 51ms:
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure.
\end{theorem}

The universality is the point: no matter how complicated
the OPE structure, the genus tower is controlled by a
single number. Theorem~D is the all-genera identity on the
uniform-weight lane; at genus~$1$ it is unconditional
(Remark~\ref{rem:multi-weight}).

% ====================================================================
\subsection{Theorem H: chiral Hochschild cohomology}
\label{ssec:thm-h}
codex
The main text edits are localized. I’m not changing theorem statuses; I’m tightening advertisements so they say exactly what the theorem now proves, and I’m removing two proof-direction shortcuts that still point the wrong way.
exec
/bin/zsh -lc "sed -n '1298,1314p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The $\hat A$-genus appears from the bar complex as the connection
between chiral algebra and index theory.

The scalar $\kappa(\cA)$ is only the leading term. The bar complex
carries higher-degree data: a universal Maurer--Cartan element
$\Theta_\cA$ whose projection to degree~$r$ yields a shadow invariant
$S_r(\cA)$. The infinite tower of shadows is algebraic of degree~$2$,
governed by a single discriminant $\Delta = 8\kappa S_4$ that
classifies the standard landscape into four shadow-depth classes
(\S6). The genus-$g$ obstruction class $\alpha_g(\cA)$ admits a
universal formula in terms of $\kappa(\cA)$ and the shadow tower:
the leading term is $\kappa\cdot\lambda_g$ (Theorem~D), and the
higher-order corrections are determined recursively by the shadow
data $(\kappa,\alpha,S_4)$ through the Riccati algebraicity
theorem (Theorem~\ref{thm:riccati-algebraicity}).

\subsection*{Complementarity}
exec
/bin/zsh -lc "sed -n '2088,2102p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1518,1534p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2406,2414p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1596,1616p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1002,1034p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '417,430p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1768,1802p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\;\in\;\Bbbk
\]
This is the first Chern class of the modular bar bundle:
$\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera, and unconditionally
at genus~$1$. On
the $E_1$ side, $\kappa(\cA)$ is the $\Sigma_2$-coinvariant of
the $R$-matrix $r(z)$; averaging collapses the $z$-dependent
profile to a number. Explicit values:
 succeeded in 51ms:


% ================================================================
% Section 7: Multi-weight
% ================================================================
\section{Multi-weight structure and cross-channel
corrections}\label{sec:multi-weight}

The scalar formula $\obs_g = \kappa\cdot\lambda_g$ holds at
all genera for uniform-weight algebras.
The forced question: does it hold for multi-weight algebras,
where generators have different conformal weights?
The answer is no. At genus~$1$ the formula remains exact
(unconditionally), but at genus~$\ge 2$ a cross-channel
correction appears. The first witness is $\cW_3$ at genus~$2$,
where $\delta F_2 = (c{+}204)/(16c)$. This section derives
these results from the graph-sum structure of the genus
 succeeded in 51ms:
$\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro
(Theorem~\ref{thm:genus-universality}).
For uniform-weight algebras
(Definition~\ref{def:uniform-weight-lane}),
the obstruction class at genus~$g$ is universally determined:
\begin{equation}\label{eq:obstruction-class-formula-intro}
\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g, \mathbb{Q}),
\end{equation}
where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle.
This holds at all genera;
for multi-weight families such as~$\mathcal{W}_N$, the scalar
formula fails at $g \geq 2$: a cross-channel correction from
mixed-propagator boundary graphs is generically nonzero
\textup{(}Theorem~\ref{thm:multi-weight-genus-expansion}\textup{)}.
The free-energy formula
 succeeded in 51ms:
(see~\S\ref{ssec:genus}).
The modular bar $B^{\mathrm{mod}}(\cA)$ restores $D^2 = 0$
by completing over the Feynman transform of the commutative
modular operad. The $E_1$-modular bar
$B^{E_1\text{-}\mathrm{mod}}(\cA)$, an algebra over the
Feynman transform of the associative modular operad, is the
primitive among these; the modular bar is its
$\Sigma_n$-coinvariant image. No two of these six objects
are isomorphic in general.
\end{remark}


% ====================================================================
\subsection{Three operations on the bar}
 succeeded in 51ms:

 The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.

\item \emph{Theorem~D$_{\mathrm{scal}}$} (Scalar modular
 characteristic, Theorem~\ref{thm:modular-characteristic}).
 A single scalar $\kappa(\cA)$, the genus-$1$ curvature
 coefficient~\eqref{eq:curvature-intro}, determines the
 entire \emph{scalar modular package}: the collection
 $(\kappa, \{\mathrm{obs}_g\}_{g \ge 1},
 \{F_g\}_{g \ge 1})$ consisting of the modular
 characteristic, its genus-$g$ obstruction classes, and the
 free energies. For algebras whose strong generators have the
 same conformal weight (including all single-generator families),
 $\mathrm{obs}_g = \kappa \cdot \lambda_g
 \in H^*(\overline{\cM}_g)$ and
 $F_g = \kappa \cdot \hat{A}_g$ at all genera.
 For multi-weight algebras (e.g.\ $\mathcal{W}_N$, $N \geq 3$),
 the new rigidity theorem forces the minimal-model MC
 element into the one-dimensional cyclic direction
 $\Theta^{\min} = \eta \otimes \Gamma_\cA$; the stronger
 succeeded in 51ms:
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}, is conditional on
perfectness and nondegeneracy of the cyclic pairing.

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
 succeeded in 51ms:
the complexity of Koszul algebras, not Koszulness itself.

\medskip
\noindent\textbf{The twelve Koszul equivalences (overview).}\enspace
The characterisation of chirally Koszul algebras involves twelve
conditions, of which ten are unconditional:
\begin{enumerate}[label=(\roman*)]
\item Bar cohomology concentrates on the diagonal (PBW).
\item The cobar-bar counit is a quasi-isomorphism (inversion).
\item The Koszul complex is acyclic.
\item The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ has
polynomial Hilbert series, concentrated in degrees $\{0,1,2\}$.
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).


thinking
**Deciding on patches**

I need to determine which standalones to patch based on the user's targets like 'obs_g', 'Theorem D', 'genus-universality', and others. It seems broad, but only some documents might have actual overclaims. I think I could patch a reasonable set, including five_theorems_modular_koszul and programme_summary. Since apply_patch can update many files at once, I should first identify overclaiming lines in the targeted documents. I'll focus on key umbrella documents for patching.
thinking
**Reviewing theorem patches**

I need to consider patching the theorem D statement in `standalone/five_theorems_modular_koszul.tex`, especially the overview lines at the top. The `programme_summary_sections2_4.tex` document has some correct information, but it incorrectly states that kappa is determined by genus-0 data, whereas the new theorem states it's based on genus-1 curvature. I need to check `programme_summary.tex` as well. Additionally, `survey_modular_koszul_duality_v2` contains a mistake regarding "multi-weight: at genus 0 only," which needs to be patched to reflect genus ≥ 2. I'll inspect those lines and look for similar issues in `survey_track_b_compressed`.
codex
I’m expanding the standalone sweep only where the wording is genuinely stale. The pattern is repetitive: older summaries say “all genera” without the lane qualifier, or they still say the scalar package is fixed by genus-0 data, which is no longer the live proof route.
exec
/bin/zsh -lc "sed -n '2258,2274p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '90,110p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1048,1064p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Verdier intertwining, producing from the bar coalgebra
$\barB_X(\cA) = T^c(s^{-1}\Abar)$ the homotopy Koszul
dual $\cA^!_\infty$.
Theorem~B proves bar-cobar inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on the
Koszul locus: unconditionally at genus $0$ and on the
standard landscape at all genera.
Theorem~C decomposes the genus-$g$ ambient complex into
Verdier-Lagrangian complements
$Q_g(\cA) \oplus Q_g(\cA^!) \cong
H^*(\Mbar_g, \cZ_\cA)$, with the Koszul complementarity
sum $\kappa(\cA) + \kappa(\cA^!)$ family-dependent: $0$ for
Kac--Moody and free fields, $13$ for Virasoro.
Theorem~D identifies the genus expansion: on the
uniform-weight lane,
$\obs_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)} at all genera, with generating
function the $\Ahat$-genus; at genus $1$ the scalar
formula is unconditional for every family.
Theorem~H proves that chiral Hochschild cohomology is
 succeeded in 51ms:
identification remains conjectural; at genus~$0$ the algebraic
BRST/bar comparison is proved
(Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level
amplitude pairing is conditional on
Corollary~\ref{cor:string-amplitude-genus0}. Theorem A (bar-cobar
adjunction), Theorem B (bar-cobar inversion on the Koszul locus),
Theorem C (complementarity: C1 unconditional, C2
\textsc{(uniform-weight)}), Theorem~D
(obstruction $\operatorname{obs}_g=\kappa\lambda_g$
\textsc{(uniform-weight)}; multi-weight correction
$\delta F_g^{\mathrm{cross}}$), and Theorem~H (chiral
Hochschild concentration $\{0,1,2\}$, $\dim\le 4$) are the five
$\Sigma_n$-coinvariant projections of a single $E_1$ object.

\subsection*{4.1.\enspace $\Gamma$-amplitudes and Taylor coefficients}

Each stable graph produces a multilinear operation on the convolution
 succeeded in 51ms:
At $N = 3$: $H_3 - 1 = 1 + 1/2 + 1/3 - 1 = 5/6$, so
$\kappa(\cW_3) = 5c/6$.

All $\cW_N$-algebras with $N \geq 2$ are class~M: the shadow
tower is infinite and the critical discriminant $\Delta \neq 0$.
As multi-weight algebras (generators at weights $2, \ldots, N$),
at genus $g \geq 2$ the full free energy acquires a
cross-channel correction $\delta F_g^{\mathrm{cross}}$
from mixed conformal-weight interactions. The scalar formula
$\obs_g = \kappa \cdot \lambda_g$ is unconditional at
genus~$1$; at higher genera the diagonal term persists but
$\delta F_g^{\mathrm{cross}} \neq 0$ (ALL-WEIGHT).

\subsection{The Bershadsky--Polyakov algebra}

The Bershadsky--Polyakov algebra $\mathrm{BP}_k =
\cW_3^{(2)}(k)$ is the subregular DS reduction of
exec
/bin/zsh -lc "sed -n '2180,2195p' standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1780,1800p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '926,946p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
restricted to genus~$0$).

\subsection*{3.4.\enspace Homotopy chiral algebras}
exec
/bin/zsh -lc "sed -n '420,432p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5478,5514p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline\cM_{g,n}$ consisting of four
independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$: the bar differential squares to zero at
all genera and degrees (Theorems~\ref{thm:bar-modular-operad},
\ref{thm:quantum-diff-squares-zero}).
\item $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera , and
unconditionally at genus~$1$ for all families; for multi-weight
algebras at $g \ge 2$ (all-weight), with cross-channel
correction $\delta F_g^{\cross}$
(Theorem~\ref{thm:modular-characteristic},
Theorem~\ref{thm:multi-weight-genus-expansion}).
\item $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline\cM_g, Z(\cA))$:
complementarity assembles the Koszul pair into a Lagrangian
 succeeded in 51ms:
modular operad. The $E_1$-modular bar
$B^{E_1\text{-}\mathrm{mod}}(\cA)$, an algebra over the
Feynman transform of the associative modular operad, is the
primitive among these; the modular bar is its
$\Sigma_n$-coinvariant image. No two of these six objects
are isomorphic in general.
\end{remark}


% ====================================================================
\subsection{Three operations on the bar}
\label{ssec:three-operations}
% ====================================================================
 succeeded in 51ms:
\noindent\textbf{Free-field exactness.}\enspace
Scalar saturation determines the genus expansion up to the
cross-channel correction $\delta F_g^{\mathrm{cross}}$. For interacting
multi-weight algebras ($\cW_N$ with $N \geq 3$, non-principal
$\cW$-algebras), this correction is genuinely nonzero at genus~$\geq 2$
and grows with genus: the scalar formula
$F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ is an incomplete
approximation. The question is whether the cross-channel correction can
vanish even when generators carry distinct conformal weights, so that the
scalar formula persists beyond its natural uniform-weight habitat.

Free-field algebras provide such an extension. Their genus-$0$ OPE
is purely quadratic ($m_k = 0$ for $k \geq 3$), and this quadratic
structure propagates to all genera: every mixed-channel stable graph
collapses, not by a single mechanism but by three independent ones,
each adapted to a different subclass.

\begin{proposition}[Free-field exactness of the scalar formula]
\label{prop:svy-free-field-exact}
Let\/ $\cA$ be a free-field chiral algebra: a modular Koszul
 succeeded in 51ms:
\;=\;
\kappa\cdot\omega_g-\kappa\cdot\omega_g+0
\;=\;0.
\]

\subsection*{The genus tower}

The bar complex traces a family of curved cochain complexes over
$\overline{\mathcal M}_g$. For uniform-weight algebras
(single-generator, or multi-generator with all generators of the
same conformal weight), the obstruction to flatness at
genus~$g$ is the characteristic class
\[
\mathrm{obs}_g(\cA)
\;=\;
\kappa(\cA)\cdot\lambda_g
\;\in\;
H^*(\overline{\mathcal M}_g),
\qquad
\lambda_g\;=\;c_g(\mathbb E),


thinking
**Patching files for accuracy**

I might need to patch more files in the standalones, but maybe it's enough to only focus on a few theorems. There’s the five_theorems_modular_koszul statement, which seems okay. However, I need to address the line about multi-weight in `survey_modular_koszul_duality.tex` since it's incorrectly stated for genus 0 instead of genus ≥ 2. I also need to check `survey_modular_koszul_duality_v2` for similar errors and ensure the theorem statements are accurate. There might be more patches needed in other related documents too. Let's get to work on that!
thinking
**Inspecting context for clarity**

I'm wondering if everything will be okay if I'm on the proved lane. I definitely need to inspect the context surrounding it. I'll search around lines 640-670 to see if there's anything related to the W-algebra, as it seems important. Understanding the context better might help clarify things. I'm just needing to be thorough here, so let's dig into those lines to get a more comprehensive view!
codex
I found one clear stale survivor in the long survey: it still says the multi-weight correction is “restricted to genus 0,” which is the old, wrong boundary. That one has to move to “genus 1 unconditional; genus ≥ 2 acquires `\delta F_g^{cross}`.”
exec
/bin/zsh -lc "sed -n '656,672p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
critical-level recovery of the FF center, and the proof of
Theorem~\ref{thm:universal-kac-moody-koszul}, appears in
Chapter~\ref{chap:kac-moody}.

The extensions beyond FF are:
\begin{enumerate}[label=(\roman*)]
\item The complementarity formula $c(\widehat{\fg}_k) + c(\widehat{\fg}_{-k-2h^\vee}) = 2d$
 (Theorem~\ref{thm:central-charge-complementarity}), which shows the
 central charge sum is a root datum invariant, independent of the level.
\item The genus-$g$ obstruction formula $\mathrm{obs}_g = \kappa \cdot \lambda_g$
\textup{(}UNIFORM-WEIGHT\textup{})
 (Theorem~\ref{thm:genus-universality}), which extends the FF involution
 to all genera via the Hodge bundle on $\overline{\mathcal{M}}_g$;
 genus-$1$ universality is unconditional for all families.
\item The Virasoro and $\mathcal{W}_N$ generalizations, where the
 Drinfeld--Sokolov parametrization introduces nonlinear level shifts
 (e.g., $c \mapsto 26 - c$ for Virasoro) that do not arise from a linear
exec
/bin/zsh -lc "sed -n '4852,4870p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6290,6308p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,256p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '60,78p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"genus~\\"'$0'"\\"'$ only|restricted to genus~'"\\"'$0'"\\"'$|at genus~'"\\"'$0'"\\"'$ only|all modular Koszul algebras at all genera|Theorem~D is unconditional|determined by the genus-'"\\"'$0'"\\"'$ data|genus-'"\\"'$0'"\\"'$ data of|Theorem~D uses|Theorem~D gives" standalone/survey_modular_koszul_duality*.tex standalone/programme_summary*.tex standalone/introduction_full_survey.tex standalone/five_theorems_modular_koszul.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/concordance.tex -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & Chain-level modular functor & Structural \\
 & & (Thm~\ref{thm:chain-modular-functor}) & \\
\bottomrule
\end{tabular}
\end{center}
Theorem~D is the \emph{integrability condition}:
$\mathrm{obs}_g = \kappa \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) is, for
algebras, a pure
tautological class, free of boundary or non-tautological
contributions, guaranteeing that the curvature of the genus-$g$
bar complex is absorbable by a period correction.
For arbitrary modular Koszul algebras, the unconditional part of
Theorem~D is the genus-$1$ identity
$\mathrm{obs}_1 = \kappa\lambda_1$; the scalar formula
\emph{fails} at $g \geq 2$ for multi-weight algebras
(Theorem~\ref{thm:multi-weight-genus-expansion}).
The corrected complex $(\barB^{(g)}, \Dg{g})$ with
$\Dg{g}^{\,2} = 0$ (Level~$1$) is the
\emph{derived fiber} of the factorization homology bundle
 succeeded in 51ms:
 of generators. &
 Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]

\hline\\[-8pt]
\multicolumn{3}{@{}l}{\textsc{Additional principal results}} \\[2pt]
\hline

\textbf{Koszulness} &
 Twelve characterizations of chiral Koszulness:
 ten unconditionally proved equivalent, one conditional
 (Lagrangian criterion, pending perfectness/nondegeneracy),
 one one-directional (D-module purity: forward direction
 established, converse open). &
 Thm~\ref{thm:koszul-equivalences-meta} \\[4pt]

\textbf{MC1 (PBW)} &
 PBW spectral sequence degenerates at $E_2$ for all
 standard families (Kac--Moody, Virasoro, $\cW_N$,
 free fields, lattice). &
 succeeded in 51ms:
appear because they are the Taylor coefficients of
$\operatorname{tr}(\Theta)$, not because of any formal group
coincidence. The formal group is additive because $\kappa$
itself is additive under tensor product
(Corollary~\ref{cor:kappa-additivity}), which in turn follows
from $\Theta_{\cA \otimes \cB} = \Theta_{\cA} + \Theta_{\cB}$
in the factorization algebra sense.
\end{remark}

\begin{remark}[Scalar free energy package]
\label{rem:concordance-scalar-free-energy}
\index{free energy!concordance summary}
Corollary~\ref{cor:free-energy-ahat-genus} assembles
the scalar content of Theorem~D into a single formula:
$F(\cA;\hbar) = (\kappa/\hbar^2)\bigl[\hat{A}(i\hbar)-1\bigr]$
with $\hat{A}(ix) = (x/2)/\sin(x/2)$, convergent for
$|\hbar|<2\pi$, and admitting the infinite product
$(\hbar/2)/\sin(\hbar/2) = \prod_{n \geq 1}
(1 - \hbar^2/4n^2\pi^2)^{-1}$.
 succeeded in 51ms:
\end{enumerate}

\subsection*{Family index theorem}

\begin{theorem}[Family index theorem for genus expansions;
\ClaimStatusProvedHere]\label{thm:guide-family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{GRR formula.}
For uniform-weight algebras, the genus-$g$ free energy is the
GRR pushforward:
 succeeded in 50ms:
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
standalone/five_theorems_modular_koszul.tex:1433:in~A and identified in~B. Theorem~D uses the Lagrangian
chapters/theory/introduction.tex:2491: Theorem~D is unconditional.
chapters/frame/preface.tex:3105:(Theorem~D is unconditional there) and requires the interaction of
standalone/programme_summary_sections2_4.tex:423:holds for all modular Koszul algebras at all genera. The
standalone/programme_summary.tex:998:holds for all modular Koszul algebras at all genera. The
chapters/connections/concordance.tex:5573:gives the equivalence, Theorem~D gives its first Chern class,
chapters/connections/concordance.tex:8056:and Theorem~D gives $\mathrm{obs}_g = 0$ for all $g \geq 1$;
codex
A few more stale slogans turned up outside the obvious theorem blocks: one sentence in the Introduction still says “Theorem D is unconditional,” and the programme summaries still say “holds for all modular Koszul algebras at all genera.” Those are exactly the kind of flattening errors this pass is for.
exec
/bin/zsh -lc "sed -n '2480,2496p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 One object
 $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{\Eone})$
 computed in seven frameworks and verified to agree. The
 five-facets formulation of
 Proposition~\ref{prop:five-facets-collision-residue} becomes the
 falsification checklist.

\item \emph{Genus-$1$ seven faces}
 (Ch.~\ref{ch:genus1-seven-faces}).
 Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
 Seven-face verification transported to genus~$1$, where
 Theorem~D is unconditional.
\end{enumerate}

\textbf{Part~\ref{part:v1-frontier}: The Frontier}.
\begin{enumerate}[label=\textup{\arabic*.}, start=31]
\item \emph{Concordance} (Ch.~\ref{chap:concordance}).
exec
/bin/zsh -lc "sed -n '1316,1438p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '414,428p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '990,1004p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1410,1440p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8048,8060p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For $g \ge 1$, the summands $\mathbf{Q}_g(\cA) =
\operatorname{fib}(\sigma - \mathrm{id})$
and\/ $\mathbf{Q}_g(\cA^!) =
\operatorname{fib}(\sigma + \mathrm{id})$ are
Lagrangian for the $(-1)$-shifted symplectic pairing
on\/~$\mathbf{C}_g$.
\end{theorem}

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi, is conditional on
 succeeded in 51ms:

Without this identification, the decomposition
$Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
object $\cA^!_\infty$ whose relation to the strict dual
$\cA^!$ is uncontrolled: the summands may not be
complementary. The genus expansion of Theorem~D uses the
Lagrangian decomposition to force the scalar factorization
$\obs_g = \kappa \cdot \lambda_g$; without the correct
identification of $\cA^!$, the constraint
$\kappa + \kappa' = K$ that anchors the genus tower is
meaningless.
\end{proof}

The geometric input is the \emph{PBW filtration}: the
spectral sequence from conformal-weight filtration collapses
at $E_2$, reducing the problem to classical Koszul duality
of the associated graded. This is the only step that
involves the conformal weight grading; Theorem~A uses only
the chiral bracket and $\cD_X$-module structure.

 succeeded in 51ms:
\operatorname{fib}(\sigma - \mathrm{id})$
and\/ $\mathbf{Q}_g(\cA^!) =
\operatorname{fib}(\sigma + \mathrm{id})$ are
Lagrangian for the $(-1)$-shifted symplectic pairing
on\/~$\mathbf{C}_g$.
\end{theorem}

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}, is conditional on
perfectness and nondegeneracy of the cyclic pairing.
 succeeded in 51ms:
factorization through stable graphs uses the clutching
morphisms on the boundary of $\Mbar_g$.

\subsection{The non-circular routing}

The chain A $\Rightarrow$ B $\Rightarrow$ C $\Rightarrow$ D
$\Rightarrow$ H might appear circular: Theorem~A uses the
bar complex, whose higher-genus structure involves
$\kappa$ (which is computed in Theorem~D). The resolution is
that the chain has a non-circular anchor.

\begin{remark}[Primitive non-circular anchor]
\label{rem:non-circular}
The bar complex $\barB(\cA) = T^c(s^{-1}\Abar)$ and the
Maurer--Cartan element $\Theta_\cA = D_\cA - d_0$ are
defined intrinsically, without reference to any theorem.
The MC equation $d_0\Theta + \frac{1}{2}[\Theta,\Theta] = 0$
is a tautology of the bar differential $D_\cA^2 = 0$.

Theorem~A uses only genus-$0$ data: the twisting morphism
 succeeded in 51ms:
The relevant tools are homological algebra on the bar
complex (Ext groups, spectral sequences, derived categories),
and the target objects are opers, the geometric Langlands
correspondence, and the center of the completed
enveloping algebra at critical level.

The \emph{scalar} shadow obstruction tower is inert on this axis:
since $\kappa = 0$, the leading (degree-$2$) shadow vanishes
and Theorem~D gives $\mathrm{obs}_g = 0$ for all $g \geq 1$;
the discriminant $\Delta = 8\kappa S_4 = 0$.
However, higher-degree components of $\Theta_\cA$ are
independent of $\kappa$ and may be nonzero: $\kappa = 0$
does not imply $\Theta_\cA = 0$ or collapse of the full
codex
The remaining logic issue is not just phrasing. One standalone still says Theorem D is proved by the Lagrangian split from Theorem C, and `thm:anomaly-koszul` still proves uncurvedness by appealing to a stronger all-genera theorem when the genus-1 definition of `\kappa` is enough. I’m correcting those dependency arrows.
exec
/bin/zsh -lc "sed -n '2928,2955p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"anomaly-koszul|Theorem~D uses|Theorem~D gives|Theorem~D is unconditional|kappa-additivity|uses the Lagrangian decomposition|requires~D|requires D|D gives|Theorem~D.*Lagrangian|Theorem~D.*family index\" chapters standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathrm{obs}_g=\kappa(\cA)\lambda_g
\;\Longrightarrow\;
\sum_{g \geq 1} F_g x^{2g}
=
\kappa(\cA)\cdot(\hat{A}(ix)-1),
\]
and Theorem~\ref{thm:genus-universality} does not invoke
Theorem~\ref{thm:family-index}.
Part~(i) is Theorem~\ref{thm:genus-universality} for
uniform-weight algebras. For multi-generator algebras
($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
is unconditional; the higher-genus extension is conditional on the
strong scalar ansatz of
Theorem~\ref{thm:multi-generator-universality}.
Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
Part~(iii) is the duality clause of
Theorem~\ref{thm:genus-universality}(ii).
Part~(iv) is Corollary~\ref{cor:kappa-additivity};
Theorem~\ref{thm:anomaly-koszul} is the matter-ghost specialization.
The group homomorphism property follows from~(iv): additivity
 succeeded in 51ms:
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
standalone/five_theorems_modular_koszul.tex:1433:in~A and identified in~B. Theorem~D uses the Lagrangian
chapters/examples/w_algebras_deep.tex:2946: requires DS--bar commutation
chapters/examples/symmetric_orbifolds.tex:13:(Corollary~\ref{cor:kappa-additivity}) and the fact that twisted
standalone/theorem_index.tex:2120:theorem & \detokenize{thm:anomaly-koszul} & \detokenize{Anomaly cancellation as Koszul constraint} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1869}\\
chapters/examples/free_fields.tex:2908:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/examples/free_fields.tex:4825:Theorem~\ref{thm:anomaly-koszul};
chapters/examples/lattice_foundations.tex:1145: and Corollary~\ref{cor:kappa-additivity}),
chapters/connections/editorial_constitution.tex:1866:\label{subsec:anomaly-koszul}
chapters/connections/editorial_constitution.tex:1870:\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
chapters/connections/editorial_constitution.tex:1877: \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
chapters/connections/editorial_constitution.tex:1889:Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
chapters/connections/editorial_constitution.tex:1906:\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul})} is equivalent,
chapters/connections/editorial_constitution.tex:2310:(\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
chapters/connections/editorial_constitution.tex:2314:(Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
chapters/examples/yangians_drinfeld_kohno.tex:6529:\item The $r$-matrix transfer requires DS--bar commutation
chapters/connections/outlook.tex:652:\label{subsec:anomaly-koszul}
chapters/connections/outlook.tex:667:\phantomsection\label{thm:anomaly-koszul}
chapters/theory/higher_genus_modular_koszul.tex:2945:Part~(iv) is Corollary~\ref{cor:kappa-additivity};
chapters/theory/higher_genus_modular_koszul.tex:2946:Theorem~\ref{thm:anomaly-koszul} is the matter-ghost specialization.
exec
/bin/zsh -lc "sed -n '1988,2004p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2440,2496p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '440,456p' standalone/computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1408,1438p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
with the genus-$g$ bar complex. The algebraic infrastructure
is in place (curved $A_\infty$ at all genera, Feynman transform
identification); what is missing is the analytic comparison
between renormalized BRST and the bar differential at genus
$g \geq 1$. Note, however, that \emph{scalar} anomaly
cancellation extends to all genera unconditionally
for pairs with $\kappa + \kappa' = 0$:
Theorem~D (Theorem~\ref{thm:modular-characteristic})
gives $\mathrm{obs}_g(\cA) + \mathrm{obs}_g(\cA^!) = (\kappa + \kappa') \cdot \lambda_g = 0$
for such pairs (Kac--Moody, free fields, lattice VOAs; see Theorem~D for the general formula).

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
The conjecture asserts quasi-isomorphism of the $L_\infty$ algebras
controlling BRST and bar deformation problems, genus by genus.
(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
\end{remark}

 succeeded in 51ms:
integration}: the evaluation of $\lambda_g$ on $\Mbar_g$
produces the numerical coefficients $\Ahat_g$, and the
factorization through stable graphs uses the clutching
morphisms on the boundary of $\Mbar_g$.

\subsection{The non-circular routing}

The chain A $\Rightarrow$ B $\Rightarrow$ C $\Rightarrow$ D
$\Rightarrow$ H might appear circular: Theorem~A uses the
bar complex, whose higher-genus structure involves
$\kappa$ (which is computed in Theorem~D). The resolution is
that the chain has a non-circular anchor.

\begin{remark}[Primitive non-circular anchor]
\label{rem:non-circular}
The bar complex $\barB(\cA) = T^c(s^{-1}\Abar)$ and the
Maurer--Cartan element $\Theta_\cA = D_\cA - d_0$ are
defined intrinsically, without reference to any theorem.
The MC equation $d_0\Theta + \frac{1}{2}[\Theta,\Theta] = 0$
is a tautology of the bar differential $D_\cA^2 = 0$.
 succeeded in 51ms:
At large~$c$, the lollipop's $c$-independent contribution $1/16$
dominates, and the correction becomes a subleading $O(1/c)$ effect
relative to the $O(c)$ scalar term.
\end{remark}

\begin{remark}[Status of the cross-channel correction]
\label{rem:cross-channel-status}
The computation above uses the naive genus-$1$ vertex factors
$\kappa_i/24$ without $R$-matrix corrections. The
multi-generator universality problem
(\textbf{op:multi-generator-universality}) is resolved negatively:
the CohFT $R$-matrix does \emph{not} produce compensating terms
that cancel $\delta F_2$. The cross-channel correction
$\delta F_2 = (c{+}204)/(16c)$ is a genuine additional term,
and the correct decomposition is
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} +
\delta F_g^{\mathrm{cross}}$.
 succeeded in 51ms:
 independent of any $\Einf$ shadow.

\item \emph{Genus expansions} (Ch.~\ref{ch:genus-expansions}).
 Explicit expansions: modular forms, Eisenstein, Mumford, bosonization.
 Verifies Theorem~D scalar saturation family-by-family.

\item \emph{Detailed computations + combinatorial frontier}
 (Ch.~\ref{chap:detailed-computations}).
 Bar cohomology tables through high degree; OEIS; growth rates.
 Empirical calibration of $\Theta_\cA^{\leq r}$ across the
 standard landscape.
\end{enumerate}

\textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
\begin{enumerate}[label=\textup{\arabic*.}, start=25]
\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
 Perturbative incarnation of the bar complex: Feynman graphs on
 $\overline{C}_n(X)$; higher operations from nested collapses.
 $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.

codex
I’m only changing summary lines that are actually false. Mentions like “uniform-weight at all genera” stay. What changes are the stale bits: “determined by genus-0 data,” “Theorem D is unconditional,” and any argument that still makes Theorem D depend on complementarity or anomaly cancellation.
exec
/bin/zsh -lc "sed -n '172,190p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,650p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '996,1014p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"genus-\\"'$0'"\\"'$ data|genus~'"\\"'$0'"\\"'$ data|genus-0 data|Theorem~D is unconditional|Theorem D is unconditional|Theorem~D uses the Lagrangian decomposition|Theorem~D uses|at genus~'"\\"'$0'"\\"'$ only|restricted to genus~'"\\"'$0'"\\"'$" chapters standalone -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.

\medskip
\noindent\textbf{Theorem D} (modular characteristic). For uniform
weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
correction $\delta F_g^{\mathrm{cross}}$.

\medskip
\noindent\textbf{Theorem H} (chiral Hochschild).
$\mathrm{ChirHoch}^*(\cA)$ has polynomial Hilbert series,
concentrated in cohomological degrees $\{0,1,2\}$.
 succeeded in 51ms:
same conformal weight), the genus-$g$ obstruction class
$\mathrm{obs}_g(\cA)$ is proportional to the top Chern class
of the Hodge bundle:
\begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA)
\;=\;
\kappa(\cA) \cdot \lambda_g\,,
\qquad g \ge 1\,.
\end{equation}
The free energy $F_g(\cA) = \kappa(\cA) \cdot
\lambda_g^{\mathrm{FP}}$, where
\begin{equation}\label{eq:faber-pandharipande}
\lambda_g^{\mathrm{FP}}
\;=\;
\frac{2^{2g-1} - 1}{2^{2g-1}}
\cdot
\frac{|B_{2g}|}{(2g)!}
\end{equation}
is the Faber--Pandharipande coefficient ($B_{2g}$ the
 succeeded in 51ms:

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}, is conditional on
perfectness and nondegeneracy of the cyclic pairing.

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 succeeded in 51ms:
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
standalone/five_theorems_modular_koszul.tex:1433:in~A and identified in~B. Theorem~D uses the Lagrangian
chapters/frame/preface.tex:3105:(Theorem~D is unconditional there) and requires the interaction of
chapters/theory/introduction.tex:2491: Theorem~D is unconditional.
exec
/bin/zsh -lc "sed -n '630,648p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1776,1798p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$d_{\mathrm{fib}}^2 = \kappa(\cH_k)\cdot\omega_1$
(Example~\ref{ex:heisenberg-d-deg1}).

\emph{Tensor degree~$n\ge 3$}: every residue at a codimension-one
collision stratum $D_{\{i,j\}}$ extracts $\alpha_{(1)}\alpha
=k\cdot\mathbf 1$ on the pair $(i,j)$. The remaining $n-2$
factors are~$\alpha$; since $\mathbf 1_{(p)}\alpha=0$ for
$p\ge 0$, no further contractions occur. All structure is
captured at tensor degree~$2$: the bar complex is
\emph{quadratic}. The Heisenberg algebra is chirally Koszul.

The modular characteristic:
\[
\kappa(\mathcal H_k)\;=\;k.
\]
The Koszul dual is the \emph{curved} symmetric chiral algebra
\[
\mathcal H_k^!
\;=\;
 succeeded in 50ms:
\item The cobar-bar counit is a quasi-isomorphism (inversion).
\item The Koszul complex is acyclic.
\item The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ has
polynomial Hilbert series, concentrated in degrees $\{0,1,2\}$.
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.





thinking
**Patching summary sections**

I need to patch a few files: `standalone/programme_summary_sections2_4.tex` and `programme_summary.tex`. I think I need to check the theorem D statement and possibly the C2 line if it mentions that it holds for all modular Koszul at all genera. But actually, the C1 line seems fine. There’s a lot to consider here, and I want to ensure everything is accurate before making those changes.
thinking
**Analyzing Algebraic Theorems**

I’m looking at a statement about Koszul chiral algebras and thinking it’s fine, but maybe I should consider including the status of the theorem? The user notes that some surfaces might present this theorem without limiting it to uniform-weight scenarios. It seems important to acknowledge that possible context could help in understanding its full implications. I'll make sure to clarify this aspect to better align with the user's expectations and thoughts.
thinking
**Clarifying theorem details**

I’m considering whether the theorem title needs adjustment. I think it should specify “For any modular Koszul chiral algebra with uniform conformal weight,” rather than just any Koszul chiral algebra. The proof cites another theorem, but it doesn’t highlight uniform weight, which makes me wonder if it’s still okay. Maybe I could clarify by adding "On the proved uniform-weight scalar lane" to the theorem statement. I might also need to look for other potential patches to maintain clarity throughout.
thinking
**Reviewing theorem statements**

I’m thinking about the family index theorem. The statement says, “Let A be Koszul chiral algebra with obstruction coefficient,” but it may not specify modular algebra. It's possible that's okay. I could patch a note at line 667, but maybe it’s not necessary since line 61 might already be correct. I’m considering adding “on the affine uniform-weight lane” at line 8056, but context could dictate it’s not needed. Given that the user wants standalone edits for several sections, including higher_genus_foundations and genus_expansions, I’ll focus on making those required fixes. Plus, I might need to regenerate the theorem_index metadata to keep everything updated.
thinking
**Considering metadata updates**

I want to avoid making large changes that create a significant difference. However, if the edits shift lines in the theorem files, the theorem_index line numbers might become outdated. Those references are important! If I adjust files like higher_genus_foundations, genus_expansions, editorial_constitution, or sections like introduction and preface, the line numbers in the theorem_index will shift. To keep everything consistent, I may need to rerun the metadata generator, so I should inspect the script to see how it generates metadata and the theorem_index.
codex
I’m about to edit. The change set is now well scoped: one source theorem proof (`cor:kappa-additivity`), one specialization theorem statement/proof (`thm:universal-generating-function`), one dependency proof (`thm:anomaly-koszul`), then the advertised summaries in the Introduction, Preface, Concordance, and the stale standalone syntheses.
exec
/bin/zsh -lc "rg -n \"generate_metadata|theorem_index\" scripts . -g '*.py' -g '*.sh' -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1913,1932p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1870,1898p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5920,5942p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
\index{genus expansion!universal generating function}
\index{obstruction coefficient!generating function}
For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
\begin{equation}\label{eq:universal-generating-function}
\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
\end{equation}
with radius of convergence $|x| = 2\pi$, independent of $\mathcal{A}$.
For arbitrary modular Koszul algebras, the genus-$1$ coefficient
still satisfies $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
\end{proof}

\begin{remark}\label{rem:universal-generating-specializations}
 succeeded in 52ms:
\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
\index{anomaly cancellation!Koszul constraint}
For the matter-ghost system
$\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The obstruction coefficient is additive:
 $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
 \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
\item The total bar complex is uncurved
 ($d_{\mathrm{bar}}^2 = 0$) if and only if
 $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
\item For the Virasoro matter-ghost system,
 $\kappa(\mathrm{Vir}_c) = c/2$ and
 $\kappa(\mathrm{ghost}) = c_{\mathrm{ghost}}/2 = -13$, so
 $\kappa_{\mathrm{tot}} = 0$ precisely at $c = 26$.
\end{enumerate}
\end{theorem}

\begin{proof}
Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 succeeded in 53ms:
Total output lines: 635

scripts/fix_campaign_100.py:643:agent("E", "E20_theorem_index", """Create a theorem index for Vol I.
scripts/fix_campaign_100.py:646:Write to standalone/theorem_index.tex.""", preamble=AUDIT_PREAMBLE)
./scripts/fix_campaign_100.py:643:agent("E", "E20_theorem_index", """Create a theorem index for Vol I.
./scripts/fix_campaign_100.py:646:Write to standalone/theorem_index.tex.""", preamble=AUDIT_PREAMBLE)
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:234:Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:813:/bin/zsh -lc "rg -n \"ClaimStatus|begin\\{theorem\\}|begin\\{conjecture\\}|structured claim extractor|generate_metadata\" scripts metadata -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:814:metadata/theorem_registry.md:3:Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:826:scripts/generate_metadata.py:13:  python3 scripts/generate_metadata.py
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:827:scripts/generate_metadata.py:36:# All environments that can carry a ClaimStatus tag
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:828:scripts/generate_metadata.py:51:    r"\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Open|Heuristic)"
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:829:scripts/generate_metadata.py:216:        # Check for ClaimStatus
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:830:scripts/generate_metadata.py:224:        # Extract optional title from \begin{env}[title; ClaimStatus...]
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:831:scripts/generate_metadata.py:229:            # Remove ClaimStatus from title
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:832:scripts/generate_metadata.py:351:    """Count raw occurrences of \\ClaimStatus* strings (matches legacy grep method)."""
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:833:scripts/generate_metadata.py:552:        "extractor in `scripts/generate_metadata.py`."
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:845:/bin/zsh -lc "sed -n '200,280p' scripts/generate_metadata.py" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:847:/bin/zsh -lc "sed -n '1,120p' scripts/generate_metadata.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./audit_campaign_20260412_231034/XV11_claim_status_sync.md:902:  python3 scripts/generate_metadata.py
 succeeded in 51ms:
negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
\end{remark}

\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
\index{obstruction coefficient!additivity}
For Koszul chiral algebras $\mathcal{A}$, $\mathcal{B}$ such that $\mathcal{A} \otimes \mathcal{B}$ is Koszul:
\begin{equation}\label{eq:kappa-additivity}
\kappa(\mathcal{A} \otimes \mathcal{B}) = \kappa(\mathcal{A}) + \kappa(\mathcal{B}).
\end{equation}
In particular, on the proved scalar lane,
$\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ for all $g \geq 1$.
\end{corollary}

\begin{proof}
The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}

\begin{example}
For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
\end{example}



thinking
**Considering editing protocols**

I need to patch some items, and I'm thinking about using pre-edit verification commentary since I'm dealing with theorem statuses and hot zones. Since it's mandatory before making any edits, I want to ensure I mention the scope and verdict before proceeding. Hot zone environments like HZ-2 and HZ-8 are relevant here. I might need to fill in the commentary template and use PE-10 for clarity on the theorem, but I'm not changing labels or formulas.
thinking
**Planning volume updates**

I need to note that the search found no live cross-volume changes needed, possibly because references to V1 genus-universality are fine for now. The task focuses only on Volume I and is standalone, but we've already done a grep on AGENTS before editing. After editing, I’m unsure if we need to grep again. If there are no genuine duplicates outside Volume I regarding theorem D, I should mention that in the final commentary. It's time to set up an update plan since it's significant!
codex
```text
PE-10 scope quantifier
genus: genus-1 universal for all families; all genera only on the proved uniform-weight scalar lane
degree: scalar / degree-2 shadow package only
AP32 weight tag: (UNIFORM) on all-genera scalar claims; (g=1 only) for family-universal clauses
tagged? Y
AP139 free-var audit: LHS vars:{g,\cA} RHS vars:{g,\cA} LHS⊇RHS? Y
AP36: implies/iff only where locally proved; no blanket converse added
verdict: ACCEPT
```

I’m updating the source theorem proofs and the summary surfaces to this exact scope, then I’ll re-grep for stale “all genera / Theorem D” advertisements and AP225–AP230 regressions.
Plan update
The theorem surface is settled; the remaining work is propagation and dependency cleanup across source and standalone summaries.
  → Patch source theorem surfaces: cor:kappa-additivity, thm:universal-generating-function, thm:anomaly-koszul
  • Patch target summaries in concordance, introduction, and preface to match the narrowed Theorem D scope
  • Patch stale standalone summaries and surveys that still overclaim Theorem D or use the old dependency direction
  • Regenerate metadata if line-bearing claim indexes moved, then grep for AP225-AP230-style regressions
codex
I’ve kept the patch set narrower than the raw grep surface. I’m fixing files where the wording is objectively false today, not every harmless mention of “all genera.” That keeps the diff surgical and still closes the live theorem-status gap.
exec
/bin/zsh -lc "sed -n '1006,1024p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"restricted to genus~\\\\\\"'$0'"\\\\\\"'$|at genus~'"\\\\\\"'$0'"\\\\\\"'$ only|genus~'"\\\\\\"'$0'"\\\\\\"'$ only|Theorem~D '"\\(modular characteristic\\)|For uniform weight, \\\\mathrm\\{obs\\}_g|determines the genus-\\"'$0'"\\"'$ data|genus-'"\\"'$0'"\\"'$ data of" standalone/programme_summary*.tex standalone/survey_modular_koszul_duality*.tex -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:restricted to genus~\$0\$|at genus~\$0\$ only|genus~\$0\$ only|Theorem~D \(modular characteristic\)|For uniform weight, \mathrm\{obs\}_g|determines the genus-$0$ data|genus-$0$ data of)
                                                                                                                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure.
\end{theorem}
exec
/bin/zsh -lc "sed -n '640,648p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '942,954p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1790,1802p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The modular characteristic:
\[
\kappa(\mathcal H_k)\;=\;k.
\]
The Koszul dual is the \emph{curved} symmetric chiral algebra
\[
\mathcal H_k^!
\;=\;
 succeeded in 51ms:
\;\in\;
H^*(\overline{\mathcal M}_g),
\qquad
\lambda_g\;=\;c_g(\mathbb E),
\]
where $\mathbb E = \pi_*\omega_\pi$ is the \emph{Hodge bundle}:
the vector bundle on $\overline{\mathcal M}_g$ whose fibre over a
point $[C]$ is the $g$-dimensional space
$H^0(C, \omega_C)$ of holomorphic differentials on~$C$.
At genus~$1$ this
factorization holds unconditionally for all families; for
multi-weight families at genus~$g \geq 2$ the scalar formula
\emph{fails}: a cross-channel correction from mixed-propagator
 succeeded in 51ms:
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
restricted to genus~$0$).

\subsection*{3.4.\enspace Homotopy chiral algebras}

The convolution algebra requires a cochain-level algebraic input, not
merely the cohomology-level chiral bracket. The \v Cech totalisation


thinking
**Analyzing document updates**

I’m reviewing the original survey, and it seems like it didn't show the theorem D summary, which might not be necessary. I'll need to rerun the rg with simpler patterns later. I’ve got a list of files to patch, including multiple tex files, but possibly the introduction doesn't need changes. 

I’m wondering about the concordance line 6294; it might need a patch, and I’m considering the preface and specific lines for adjustments as well, though many might already be fine. I'll focus on line 2491 for sure.
thinking
**Reviewing theorem details**

I’m thinking that I might have misinterpreted the claim about the leading term in Theorem D — it seems it's not a strict overclaim since it just mentions the leading term. I need to patch certain lines in the five_theorems_modular_koszul.tex file, specifically around 1321 and 1433. 

I might also want to revise the introduction of the chain to clarify that "The genus expansion of Theorem D uses the bar-intrinsic scalar trace of Theta" instead of focusing on the Lagrangian decomposition. Additionally, I should inspect the continuation after "The routing is:" for further potential patches.
codex
The one file needing the most conceptual surgery is the standalone five-theorems survey: it still hardcodes the old “D from C” route. I’m replacing that with the live route “bar-intrinsic MC/scalar trace → genus universality → family index,” leaving the rest of the standalone intact.
exec
/bin/zsh -lc "sed -n '1438,1468p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '100,112p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '100,112p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
meromorphic function with a single simple zero must have a
simple pole. The \emph{prime form} $E(z_1, z_2)$, a
section of $K^{-1/2} \boxtimes K^{-1/2}$ vanishing to
first order along the diagonal, replaces it. The
genus-$g$ propagator
\begin{equation}\label{eq:genus-g-propagator}
\eta^{(g)}_{12}
\;=\;
d\log E(z_1, z_2)
+ \pi \sum_{\alpha,\beta = 1}^{g}
(\operatorname{Im}\Omega)^{-1}_{\alpha\beta}
\,\omega_\alpha(z_1)\,\bar\omega_\beta(z_2)
\end{equation}
 succeeded in 52ms:
with 120K+ computational tests; six new proved results
include the universal $\alpha_g$ identity, the soft
graviton coefficient $a_3 = 2$, and free-field exactness.
\end{abstract}

\maketitle

% ====================================================================
\section{The bar construction on algebraic curves}
\label{sec:bar}
% ====================================================================

The bar construction of an associative algebra is classical:
 succeeded in 52ms:
bound the coderivation complex.

The routing is: bar-intrinsic MC element (definition)
$\to$ adjunction/intertwining (A) $\to$ inversion (B)
$\to$ polarization (C) $\to$ scalar extraction (D)
$\to$ coefficient ring (H). Each step uses results from
the previous step and new geometric input; no step
requires a result proved later.
\end{remark}

\subsection{Independence of converses}

The converses of the five implications fail. This is not
a deficiency; it reflects the fact that each theorem addresses
a strictly different aspect of the bar complex.

\begin{enumerate}
\item \emph{H does not imply D.} A polynomial Hilbert series
 $P(t) = 1 + t^2$ (Virasoro) does not determine
 $\kappa = c/2$; it constrains $\dim \ChirHoch^2 = 1$
exec
/bin/zsh -lc "sed -n '638,646p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
sum to a topological invariant. The coinvariant projection
yields the scalar complementarity $\kappa(\cA)+\kappa(\cA^!)=K(\cA)$,
where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.

\medskip
\noindent\textbf{Theorem D} (modular characteristic). For uniform
weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
correction $\delta F_g^{\mathrm{cross}}$.


thinking
**Patching a proposition**

I need to address a statement in the file around 1321, which says "C is necessary for D--H." I've realized that's now false, so I've got to patch it! This feels critical, so let me inspect the full proposition block and prepare a rewrite. It's important to get this right!  I'm looking forward to sorting through the details so that I can make the necessary updates.
codex
I found a more serious standalone issue than just wording: `five_theorems_modular_koszul.tex` still contains a proposition claiming C is necessary for D. That is false on the live proof route. I’m rewriting that local argument so it says what’s actually true now: C strengthens the ambient decomposition, but D comes from the bar-intrinsic scalar trace plus clutching/GRR.
exec
/bin/zsh -lc "sed -n '1298,1360p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1360,1408p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proposition}[B is necessary for C--H]
\label{prop:B-necessary}
Without Theorem~B, the Lagrangian decomposition of Theorem~C
is vacuous and the genus expansion of Theorem~D is
ungrounded.
\end{proposition}

\begin{proof}
Theorem~A constructs the homotopy Koszul dual
$\cA^!_\infty$, but the construction produces a
factorization algebra that a priori differs from $\cA^!$.
Theorem~B proves that bar-cobar inversion is faithful:
$\barB$ is injective on quasi-isomorphism classes. This
identifies $\cA$ and $\cA^!$ as the two canonical algebras
recoverable from the bar coalgebra, and establishes that
Verdier duality on $\barB(\cA)$ produces the \emph{correct}
dual.

Without this identification, the decomposition
 succeeded in 51ms:
projection of this decomposition yields the complementarity
constraint $\kappa + \kappa' = K$. This constraint is the
input to the genus universality argument: the fact that the
scalar shadow factors through $\kappa$ alone, at every genus,
is a consequence of the polarization being Lagrangian (each
summand carries half the information).
\end{proof}

The geometric input is the \emph{Verdier involution}: the
existence of a functorial duality on sheaves on $\Mbar_g$
that exchanges the bar complex of $\cA$ with that of $\cA^!$.
This requires the moduli space $\Mbar_g$ as a smooth
Deligne--Mumford stack with Poincar\'{e} duality.

\subsection{D identifies the scalar shadow}

\begin{proposition}[D is necessary for H]
\label{prop:D-necessary}
Without Theorem~D, the coefficient ring of the genus tower
is unidentified, and Theorem~H cannot distinguish


thinking
**Patching mathematical propositions**

The user wants to fix all downstream surfaces and be surgical about it. I’m considering patching just the lines that mention D using C, rather than changing the entire proposition title to avoid major conceptual changes. However, since the proposition claims necessity, I feel I have to patch it. I might need to rewrite the section, specifically focusing on how C refines the ambient geometry and the implications of Theorem C regarding Theorem D.
thinking
**Revising the argument structure**

I think I need to update the previous sentence about the chain being circular. I could change it to say, “The five theorems share a common source, rather than a single linear chain.” However, updating it might be more complicated than I thought. I'll consider keeping changes limited to only the clearly erroneous lines, instead of rewriting the whole argument. But, wow, it seems like some proposition titles could still be false!
codex
I’m applying the edits now. After that I’ll re-run targeted greps for `Theorem D`, `genus-universality`, `family-index`, `all genera`, `cor:kappa-additivity`, and `anomaly-koszul` to catch any stale advertisements I missed.

thinking
**Inspecting patch failure**

I see that the patch has failed, and I really need to check the exact context in the file "standalone/survey_modular_koszul_duality.tex." It might be formatted differently than I expected. Hm, I wonder if splitting the patch into smaller parts could help. It seems like I need to take a closer look at the surrounding lines in that section to understand what went wrong. Let's see how it goes!
codex
One patch hunk missed because the older survey’s wording isn’t byte-for-byte the same as the v2 file. I’m re-reading those exact local contexts and then re-applying the edits file-by-file so the diff stays accurate.
exec
/bin/zsh -lc "sed -n '1298,1330p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '938,950p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
\mathrm{obs}_g(\cA)
\;=\;
\kappa(\cA)\cdot\lambda_g
\;\in\;
H^*(\overline{\mathcal M}_g),
\qquad
\lambda_g\;=\;c_g(\mathbb E),
\]
where $\mathbb E = \pi_*\omega_\pi$ is the \emph{Hodge bundle}:
the vector bundle on $\overline{\mathcal M}_g$ whose fibre over a
point $[C]$ is the $g$-dimensional space
$H^0(C, \omega_C)$ of holomorphic differentials on~$C$.
 succeeded in 51ms:

\begin{proposition}[B is necessary for C--H]
\label{prop:B-necessary}
Without Theorem~B, the Lagrangian decomposition of Theorem~C
is vacuous and the genus expansion of Theorem~D is
ungrounded.
\end{proposition}

\begin{proof}
Theorem~A constructs the homotopy Koszul dual
$\cA^!_\infty$, but the construction produces a
factorization algebra that a priori differs from $\cA^!$.
Theorem~B proves that bar-cobar inversion is faithful:
$\barB$ is injective on quasi-isomorphism classes. This
identifies $\cA$ and $\cA^!$ as the two canonical algebras
recoverable from the bar coalgebra, and establishes that
Verdier duality on $\barB(\cA)$ produces the \emph{correct}
dual.

Without this identification, the decomposition
exec
/bin/zsh -lc "sed -n '1330,1365p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1418,1462p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2486,2494p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3068,3108p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
spectral sequence from conformal-weight filtration collapses
at $E_2$, reducing the problem to classical Koszul duality
of the associated graded. This is the only step that
involves the conformal weight grading; Theorem~A uses only
the chiral bracket and $\cD_X$-module structure.

\subsection{C provides the polarization}

\begin{proposition}[C is necessary for D--H]
\label{prop:C-necessary}
Without Theorem~C, the genus tower has no canonical
factorization into $\cA$ and $\cA^!$ contributions, and
Theorem~D cannot distinguish the universal scalar
$\kappa$ from family-dependent corrections.
\end{proposition}

\begin{proof}
At genus $g \geq 1$, the bar differential satisfies
$d_{\mathrm{fib}}^2 = \kappa \cdot \omega_g$, and the
Maurer--Cartan element $\Theta_\cA$ encodes all genus
 succeeded in 50ms:
$\kappa$ (which is computed in Theorem~D). The resolution is
that the chain has a non-circular anchor.

\begin{remark}[Primitive non-circular anchor]
\label{rem:non-circular}
The bar complex $\barB(\cA) = T^c(s^{-1}\Abar)$ and the
Maurer--Cartan element $\Theta_\cA = D_\cA - d_0$ are
defined intrinsically, without reference to any theorem.
The MC equation $d_0\Theta + \frac{1}{2}[\Theta,\Theta] = 0$
is a tautology of the bar differential $D_\cA^2 = 0$.

Theorem~A uses only genus-$0$ data: the twisting morphism
and the Verdier functor on $\Ran(X)$. Theorem~B uses the
PBW filtration at genus~$0$. Theorem~C uses the Verdier
involution on $\Mbar_g$ applied to the objects constructed
in~A and identified in~B. Theorem~D uses the Lagrangian
decomposition from~C to extract the scalar shadow $\kappa$,
which was already present in the definition of $\Theta_\cA$
but not yet identified as universal. Theorem~H uses the
concentration result from Koszul duality (Theorem~B) to
 succeeded in 50ms:
\item \emph{Holographic datum master}
 (Ch.~\ref{ch:holographic-datum-master}).
 One object
 $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{\Eone})$
 computed in seven frameworks and verified to agree. The
 five-facets formulation of
 Proposition~\ref{prop:five-facets-collision-residue} becomes the
 falsification checklist.

 succeeded in 52ms:

\subsection*{Multi-weight: the cross-channel correction}

The Virasoro algebra has a single generator of weight~$2$. The
scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
propagator weight~$1$ couples to a single Hodge bundle
$\mathbb{E}_1$. The question forced by the depth classification
is whether the scalar formula survives the passage to multiple
generators at different conformal weights.

The $\cW_3$-algebra answers negatively. Two generators
$T$ (weight~$2$) and $W$ (weight~$3$); the $WW$~OPE contains the
composite quasi-primary
$\Lambda = {:}TT{:} - \tfrac{3}{10}\partial^2 T$ with structure
constant $16/(22{+}5c)$. The modular characteristic
$\kappa(\cW_3) = 5c/6$ (from $\kappa(\cW_N) = c(H_N{-}1)$ at
$N = 3$: $H_3 = 1 + 1/2 + 1/3 = 11/6$, so
$H_3 - 1 = 5/6$). The spectral discriminant
$\Delta_{\cW_3}(x) = (1 - \frac{c}{2}x)(1 - \frac{c}{3}x)$:
one eigenvalue for each generator weight. At genus~$2$, a
context compacted
codex
Using `claim-surface-sync` and `cross-volume-propagation` on the final theorem-status surfaces. I’ve isolated the remaining stale statements; next I’m patching them in smaller chunks, then I’ll regenerate metadata and grep for AP228/AP230 regressions.

thinking
**Considering plan update**

I’m thinking it’s time to update the plan, as the current summary doesn’t seem to be finalized. Maybe I haven’t set everything up yet? I’ll go ahead and call for an update on the plan now to get things in order and make sure everything is on track. It feels like a good step to ensure everything runs smoothly!
Plan update
Patch the remaining stale theorem-status statements, then verify propagation and metadata.
  → Patch theorem-status and dependency direction in core chapter files
  • Patch stale standalone summaries and theorem-route statements
  • Regenerate metadata and grep for AP228/AP230/theorem-status regressions
codex
I’m re-reading the exact local contexts before editing so the patches stay minimal and line-stable. After that I’ll apply the claim-status fixes and re-check the route statements against the live theorem scope.
exec
/bin/zsh -lc "sed -n '400,470p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '200,280p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '630,720p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
the exact stage-$4$ six-entry block on~$\mathcal{I}_4$; on the
stage-$4$ Ward-normalized H-level locus of
Definition~\ref{def:winfty-stage4-ward-normalized}, its effective content
contracts to the four higher-spin channels of
Corollary~\ref{cor:winfty-stage4-residue-four-channel}.

On the standard type-$A$ Yangian side, the local coefficient packet is
already closed on the factorization-side shared-seed locus. The
canonical H-level target exists as the tangent Lie algebra of the
factorization formal moduli problem
(Proposition~\ref{prop:yangian-canonical-hlevel-target}), with
canonical associative dg model
(Proposition~\ref{prop:yangian-canonical-envelope}). The next step is
to equip that dg model with the RTT-adapted package of
Proposition~\ref{prop:yangian-typea-realization-criterion}, after
which
Corollary~\ref{cor:yangian-canonical-realization-to-spectral-seed}
reduces the remaining input to the spectral vector-line realization
package; on the equivariant multiplicative spectral realization locus,
this is equivalently the standard spectral vector seed-and-shift
 succeeded in 53ms:
\end{enumerate}
\end{proposition}

\begin{proof}
Part~(i) is a direct application of genus universality
(Theorem~\ref{thm:genus-universality}).
Part~(ii) is the standard result from the
Quillen determinant line bundle computation \cite{Quillen85}
(\ClaimStatusProvedElsewhere).
Part~(iii) follows from the triviality of the
canonical bundle on an elliptic curve.
\end{proof}

\section{Lattice VOAs at all genera}\label{sec:lattice-genera}
\index{lattice VOA!genus expansion}

The Heisenberg genus expansion (\S\ref{sec:frame-genus-tower}) treats a single free boson. A lattice VOA $V_\Lambda$ tensors $d$ copies of $\mathcal{H}_1$ with $\mathbb{C}[\Lambda]$; lattice shifts leave $\kappa$ unchanged, so the genus expansion follows immediately.

\begin{theorem}[Lattice VOA free energy;
\ClaimStatusProvedHere]\label{thm:lattice-all-genera}
 succeeded in 51ms:
Part~(iv): the scalar factorization
\eqref{eq:obstruction-hodge} is Theorem~\ref{thm:genus-universality},
and the generating series
\eqref{eq:family-index-package} is its
Grothendieck--Riemann--Roch refinement
(Theorem~\ref{thm:family-index}).
\end{proof}

\begin{proposition}[Chain-level curvature operator; \ClaimStatusProvedHere]
\label{prop:chain-level-curvature-operator}
\index{curvature!chain-level operator|textbf}
\index{Arakelov form!as chain representative}
\index{Chern--Weil!chain-to-cohomology projection}
Let $\cA$ be a cyclic chiral algebra on a smooth curve
$\Sigma_g$ of genus~$g \geq 1$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Chain-level identity.}\;
 The operator $\dfib^{\,2}$ is an explicit degree-$2$
 endomorphism of the graded vector space underlying the
 bar complex $\barB^{(g)}(\cA)|_{[\Sigma_g]}
exec
/bin/zsh -lc "sed -n '1288,1435p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2480,2510p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3060,3115p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '105,175p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '140,210p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1780,1815p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '928,950p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '630,670p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{proof}

The geometric input that Theorem~A requires, beyond the bar
complex itself, is the Fulton--MacPherson compactification
$\overline{\FM}_n(X)$ and its boundary divisor structure: the
twisting morphism $\tau$ is mediated by integration kernels
on $\overline{\FM}_n(X)$, and the Verdier intertwining uses
the Poincar\'{e}--Verdier duality on $\Ran(X)$.

\subsection{B establishes faithfulness}

\begin{proposition}[B is necessary for C--H]
\label{prop:B-necessary}
Without Theorem~B, the Lagrangian decomposition of Theorem~C
is vacuous and the genus expansion of Theorem~D is
ungrounded.
\end{proposition}

\begin{proof}
Theorem~A constructs the homotopy Koszul dual
 succeeded in 52ms:
Koszul dual: $\mathrm{Vir}_{26-c}$. At $c = 26$ the dual is
uncurved ($\kappa(\mathrm{Vir}_0) = 0$); at $c = 0$ the algebra
itself is uncurved; at $c = 13$ the algebra is self-dual
($\kappa + \kappa^! = 13$, the unique fixed point). The critical
dimension $c = 26$ is the statement that the Koszul dual's
curvature vanishes, not that the algebra's does: the string ghost
system $bc$ at $c_{\mathrm{ghost}} = -26$ is the complementarity
partner.

\subsection*{Multi-weight: the cross-channel correction}

The Virasoro algebra has a single generator of weight~$2$. The
scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
propagator weight~$1$ couples to a single Hodge bundle
$\mathbb{E}_1$. The question forced by the depth classification
is whether the scalar formula survives the passage to multiple
generators at different conformal weights.

The $\cW_3$-algebra answers negatively. Two generators
$T$ (weight~$2$) and $W$ (weight~$3$); the $WW$~OPE contains the
 succeeded in 50ms:
\eta_{12}
\;=\;
d\log(z_1 - z_2)
\;=\;
\frac{dz_1 - dz_2}{z_1 - z_2}\,.
\end{equation}
This $1$-form has a simple pole along the diagonal
$\Delta \subset X \times X$ with residue~$1$. The residue is
intrinsic: it depends on no coordinate, no metric, no level.

Three properties single out~$\eta_{12}$. A double pole
$dz/(z-w)^2$ transforms under coordinate change and has no
coordinate-independent residue. A regular $1$-form has
residue zero and extracts nothing from the collision. The
logarithmic derivative is the unique $1$-form on~$C_2(X)$
with a first-order pole along~$\Delta$ and conformally
invariant residue.

On $C_3(X)$, the three pullbacks
$\eta_{12}, \eta_{23}, \eta_{31}$ satisfy
 succeeded in 50ms:
\begin{equation}\label{eq:genus-g-propagator}
\eta^{(g)}_{12}
\;=\;
d\log E(z_1, z_2)
+ \pi \sum_{\alpha,\beta = 1}^{g}
(\operatorname{Im}\Omega)^{-1}_{\alpha\beta}
\,\omega_\alpha(z_1)\,\bar\omega_\beta(z_2)
\end{equation}
is single-valued; the period correction couples to the
Hodge bundle $\mathbb{E} = R^0\pi_*\omega_\pi$ through
the period matrix~$\Omega$.

Three properties of~\eqref{eq:genus-g-propagator} constrain
the genus tower. First, the logarithmic derivative
$d\log E$ has conformal weight~$1$ in both variables,
regardless of the conformal weight of the field being
sewed: every edge of every graph sum at every genus uses
the standard Hodge bundle~$\mathbb{E}_1$. Second, the
period correction is harmonic in each variable and involves
$(\operatorname{Im}\Omega)^{-1}$, the Arakelov Green
 succeeded in 52ms:
 $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$; Eisenstein
 spectral content. Projects $\Theta_\cA$ to its arithmetic residue.
\end{enumerate}

\textbf{Part~\ref{part:seven-faces}: The Seven Faces of the Collision Residue}.
\begin{enumerate}[label=\textup{\arabic*.}, start=29]
\item \emph{Holographic datum master}
 (Ch.~\ref{ch:holographic-datum-master}).
 One object
 $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA^{\Eone})$
 computed in seven frameworks and verified to agree. The
 five-facets formulation of
 Proposition~\ref{prop:five-facets-collision-residue} becomes the
 falsification checklist.

\item \emph{Genus-$1$ seven faces}
 (Ch.~\ref{ch:genus1-seven-faces}).
 Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
 Seven-face verification transported to genus~$1$, where
 Theorem~D is unconditional.
 succeeded in 50ms:
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
restricted to genus~$0$).

\subsection*{3.4.\enspace Homotopy chiral algebras}
 succeeded in 53ms:
\noindent\textbf{Theorem B} (bar-cobar inversion). On the Koszul
locus, the counit $\varepsilon\colon\Omega(\barB(\cA))\to\cA$ is a
quasi-isomorphism at every genus. Koszulness is characterised by
twelve equivalent conditions (\S9).

\medskip
\noindent\textbf{Theorem C} (complementarity). The ordered
partition functions $Q^{E_1}_{g,n}(\cA)$ and $Q^{E_1}_{g,n}(\cA^!)$
sum to a topological invariant. The coinvariant projection
yields the scalar complementarity $\kappa(\cA)+\kappa(\cA^!)=K(\cA)$,
where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.

\medskip
\noindent\textbf{Theorem D} (modular characteristic). For uniform
weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
correction $\delta F_g^{\mathrm{cross}}$.

\medskip
\noindent\textbf{Theorem H} (chiral Hochschild).
$\mathrm{ChirHoch}^*(\cA)$ has polynomial Hilbert series,
 succeeded in 53ms:
\;=\;0.
\]

\subsection*{The genus tower}

The bar complex traces a family of curved cochain complexes over
$\overline{\mathcal M}_g$. For uniform-weight algebras
(single-generator, or multi-generator with all generators of the
same conformal weight), the obstruction to flatness at
genus~$g$ is the characteristic class
\[
\mathrm{obs}_g(\cA)
\;=\;
\kappa(\cA)\cdot\lambda_g
\;\in\;
H^*(\overline{\mathcal M}_g),
\qquad
\lambda_g\;=\;c_g(\mathbb E),
\]
where $\mathbb E = \pi_*\omega_\pi$ is the \emph{Hodge bundle}:
codex
I’ve confirmed the main stale surfaces. One pass of focused grep now will catch the remaining exact phrases so I can patch only the false statements and leave already-correct theorem text untouched.
exec
/bin/zsh -lc 'rg -n "family-index|Theorem D|genus-universality|all genera|obs_g|universal-generating-function|anomaly-koszul|kappa-additivity" chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"genus-\\\\\\"'$0'"\\\\\\"'$ data|genus-'"\\"'$0'"\\"'$ data|Theorem~D is unconditional|restricted to genus~'"\\\\\\"'$0'"\\\\\\"'$|restricted to genus~'"\\"'$0'"\\"'$|Theorem D is unconditional|uses the Lagrangian decomposition|genus expansion of Theorem~D" chapters/theory/introduction.tex chapters/frame/preface.tex standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/five_theorems_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
standalone/five_theorems_modular_koszul.tex:1302:is vacuous and the genus expansion of Theorem~D is
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
standalone/five_theorems_modular_koszul.tex:1429:Theorem~A uses only genus-$0$ data: the twisting morphism
standalone/programme_summary_sections2_4.tex:246:genus-$0$ data alone: the leading coefficient of the OPE,
standalone/programme_summary_sections2_4.tex:443:genus-$0$ data of\/~$\cA$. The generating function is
standalone/survey_modular_koszul_duality.tex:2852:at all $(g,n)$ from genus-$0$ data and~$P_\cA$
chapters/theory/higher_genus_foundations.tex:2563:At genus $g \geq 3$, modular forms of weight $\leq g(g+1)/2$ appear, with relations from gluing equations along boundary strata of $\overline{\mathcal{M}}_g$. All structures are determined by genus-$0$ data and modular invariance (Witten; see Remark~\ref{rem:parameter-source} for the precise reformulation in terms of the parameter-source chain).
standalone/programme_summary.tex:820:genus-$0$ data alone: the leading coefficient of the OPE,
standalone/programme_summary.tex:1018:genus-$0$ data of\/~$\cA$. The generating function is
chapters/frame/preface.tex:3105:(Theorem~D is unconditional there) and requires the interaction of
chapters/theory/introduction.tex:2499: Theorem~D is unconditional.
standalone/survey_modular_koszul_duality_v2.tex:1797:restricted to genus~$0$).
standalone/survey_modular_koszul_duality_v2.tex:3147:recovers $\{\tau_{g,n}\}$ at all $(g,n)$ from genus-$0$ data and
 succeeded in 53ms:
standalone/N3_e1_primacy.tex:562:coinvariant with the cubic shadow is Volume I Theorem D(iii).
standalone/N3_e1_primacy.tex:603:comparison, and highlight Theorem D as the cleanest example: the
standalone/N3_e1_primacy.tex:699:\begin{remark}[Theorem D is the cleanest example]
standalone/N3_e1_primacy.tex:701:Among the five, Theorem D makes the $E_{1}$ primacy thesis most
standalone/N3_e1_primacy.tex:715:The universality property of $\kappa$ in Volume I Theorem D
standalone/N3_e1_primacy.tex:888:symmetric images are the classical theorems. Theorem D is the
standalone/N3_e1_primacy.tex:964:Theorem D displays this most visibly at degree $2$: for Heisenberg
chapters/theory/introduction.tex:6:Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. In the non-abelian affine Kac--Moody case the precise degree-$2$ formula is $\kappa(\cA) = \mathrm{av}(r_\cA(z)) + \dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.
chapters/theory/introduction.tex:93:$F_g = \kappa \cdot \lambda_g$ is exact at all genera
chapters/theory/introduction.tex:365:$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
chapters/theory/introduction.tex:612: Theorem~\ref{thm:genus-universality}).
chapters/theory/introduction.tex:620: $F_g = \kappa \cdot \hat{A}_g$ at all genera.
chapters/theory/introduction.tex:639: \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
chapters/theory/introduction.tex:748: $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
chapters/theory/introduction.tex:1788: (Theorem~\ref{thm:genus-universality}). The natural home is
chapters/theory/introduction.tex:1923:(Theorem~\ref{thm:universal-generating-function}) are consequences
chapters/theory/introduction.tex:2060:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
chapters/theory/introduction.tex:2248: $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
chapters/theory/introduction.tex:2318: chiral theory will later extend to all genera.
chapters/theory/introduction.tex:2428: Koszul duality; PBW at all genera. Depth class L (Lie/tree),
codex
I’ve got the obvious stale phrases. I’m checking the surrounding theorem summaries in the introduction and prefatory material now, because a few `all genera` hits are correct only if they already carry the uniform-weight/genus-1 split.
exec
/bin/zsh -lc "sed -n '350,375p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,105p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\Delta = 8\kappa S_4$ forces $r_{\max}$ to lie in
$\{2, 3, \infty\}$ on any one-dimensional primary slice
(Theorem~\ref{thm:single-line-dichotomy}); the
fourth class $r_{\max} = 4$ arises from stratum
separation.
The algebraic depth $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
admits no value~$3$ or any finite value $\geq 3$
(Proposition~\ref{prop:depth-gap-trichotomy}).
Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
$k \geq 3$) holds if and only if the algebra belongs to
class~$\mathbf{G}$
(Proposition~\ref{prop:sc-formal-iff-class-g}).
For free-field algebras, the scalar formula
$F_g = \kappa \cdot \lambda_g$ is exact at all genera
(all-weight): the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


Three depths measure distinct aspects of the tower.
 succeeded in 53ms:
then in its $\Sigma_n$-coinvariant shadow.

Theorem~A identifies the homotopy Koszul dual on the quadratic Koszul
lane: for a chiral Koszul pair, the unit and counit are
quasi-isomorphisms and Verdier duality exchanges the two members of the
pair. Theorem~B shows that the bar-cobar transform is faithful on the
Koszul locus: genus~$0$ is unconditional, while the genus-$g \ge 1$
inversion is proved on the modular pre-Koszul lane and is unconditional
on the standard CFT-type landscape except integer-spin $\beta\gamma$.
Once both sides are present, Theorem~C forces the Verdier decomposition
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ of the ambient complex;
the Lagrangian splitting is proved, while the ambient
shifted-symplectic upgrade remains conditional on perfectness and
nondegeneracy. Tracing the same object yields Theorem~D: on the
uniform-weight modular Koszul lane,
$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
energies are the $\hat A$-series; at genus~$1$ this scalar statement is
unconditional for every family, while at genus $g \ge 2$ multi-weight
algebras acquire the explicit cross-channel term
$\delta F_g^{\mathrm{cross}}$. Theorem~H identifies the coefficient
exec
/bin/zsh -lc "sed -n '740,758p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '608,642p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4580,4600p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '438,448p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,252p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2400,2420p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '814,826p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1012,1022p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2844,2860p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3138,3154p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 nondegeneracy. Instant check: for Heisenberg the center local system
 is constant, so the decomposition is visible at once.

\item \emph{Theorem~D$_{\mathrm{scal}}$} (Genus universality,
 Theorem~\ref{thm:genus-universality}).
 The deficiency is scalar drift: genus by genus, the bar tower could
 produce unrelated numbers. Theorem~D says that on the proved
 uniform-weight lane they are forced by one scalar
 $\kappa(\cA)$, determined already at genus~$1$. For algebras whose
 strong generators have the same conformal weight,
 $\mathrm{obs}_g = \kappa \cdot \lambda_g
 \in H^*(\overline{\cM}_g)$ and
 $F_g = \kappa \cdot \hat{A}_g$ at all genera.
 At genus~$1$ the scalar formula is unconditional for every family.
 For multi-weight algebras and $g \geq 2$, the diagonal term remains
 universal but the full free energy is
 \[
 F_g(\cA) = \kappa(\cA)\lambda_g^{\mathrm{FP}}
 + \delta F_g^{\mathrm{cross}}(\cA),
 \]
 succeeded in 52ms:
 into complementary Lagrangians
 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
 = H^*(\overline{\cM}_g,\, Z(\cA))$.

\item \emph{Leading coefficient}
 \textup{(}Theorem~D\textup{)}.
 $\Theta_\cA$ has \textbf{universal scalar projection}.
 On the uniform-weight lane, the degree-$2$ genus-$g$ component is
 $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
 with $\kappa(\cA)$ universal and governed by the
 $\hat{A}$-genus. At genus~$1$ this holds unconditionally
 for all families.

\item \emph{Coefficient ring}
 \textup{(}Theorem~H\textup{)}.
 $\Theta_\cA$ has \textbf{polynomial coefficients}.
 $\ChirHoch^*(\cA)$ is concentrated in degrees~$\{0,1,2\}$,
 controlling the deformation ring over which~$\Theta_\cA$ varies.
\end{enumerate}
 succeeded in 51ms:
\noindent\textbf{The scalar curvature $\kappa(\cA)$.}\enspace
The degree-two, genus-zero trace:
\[
\kappa(\cA)
\;=\;
\operatorname{tr}(\Theta_\cA)_{2,0}
\;\in\;\Bbbk
\]
This is the first Chern class of the modular bar bundle:
$\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera, and unconditionally
at genus~$1$. On
the $E_1$ side, $\kappa(\cA)$ is the $\Sigma_2$-coinvariant of
the $R$-matrix $r(z)$; averaging collapses the $z$-dependent
profile to a number. Explicit values:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lccl}
\textbf{Algebra $\cA$}
 & $\kappa(\cA)$
 succeeded in 51ms:
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure.
 succeeded in 51ms:
The modular Koszul machine has a complete algebraic-geometric
interface with $\overline{\mathcal M}_{g,n}$, consisting of
four independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$:
 the bar differential squares to zero at all genera and degrees
 \textup{(}Theorems~\textup{\ref{thm:bar-modular-operad},
 \ref{thm:quantum-diff-squares-zero}}\textup{)}.
\item $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for uniform-weight algebras at all genera;
 at genus~$1$ the same scalar identity is unconditional for all
 families, while at $g \ge 2$ outside the scalar lane one has
 \textup{(ALL-WEIGHT $+\delta F_g^{\mathrm{cross}}$)}
 \textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)}.
\item $Q_g(\cA)+Q_g(\cA^!)=H^*(\overline{\mathcal M}_g,Z(\cA))$:
 complementarity assembles the Koszul pair into a Lagrangian
 decomposition
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
\item Sewing:
 succeeded in 51ms:
= (c + 204)/(16c) > 0$ for all $c > 0$.
\end{remark}

% ====================================================================
\subsection{The modular characteristic}
\label{ssec:kappa}
% ====================================================================

The modular characteristic $\kappa(\cA)$ is the single
scalar controlling the genus tower. It is computed from
genus-$0$ data alone: the leading coefficient of the OPE,
extracted through the bar construction.

\begin{table}[ht]
\centering
\caption{Modular characteristic for the standard families}
\label{tab:kappa}
 succeeded in 51ms:
\subsection{The modular characteristic}
\label{ssec:kappa}
% ====================================================================

The modular characteristic $\kappa(\cA)$ is the single
scalar controlling the genus tower. It is computed from
genus-$0$ data alone: the leading coefficient of the OPE,
extracted through the bar construction.

\begin{table}[ht]
\centering
\caption{Modular characteristic for the standard families}
\label{tab:kappa}
 succeeded in 51ms:
(Proposition~\ref{prop:mumford-from-mc}).

The complementarity propagator
$P_\cA\colon H^*(\cA)\otimes H^*(\cA^!)\to\mathbb C$
is the Givental $R$-matrix of the shadow CohFT; when
it carries a flat unit (all standard families
with vacuum in~$V$; Theorem~\ref{thm:shadow-cohft}),
Teleman reconstruction recovers $\{\tau_{g,n}\}$
at all $(g,n)$ from genus-$0$ data and~$P_\cA$
(Theorem~\ref{thm:cohft-reconstruction}). Eynard--Orantin
topological recursion is the MC equation applied to the shadow obstruction tower
(Corollary~\ref{cor:topological-recursion-mc-shadow}).

\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{ll}
 succeeded in 52ms:
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
 succeeded in 52ms:
$\overline{\cM}_{0,4}$ reduces to WDVV. At degree~$2$, genus~$g\ge 2$:
substituting $\tau_{g,2}(\cA)=\kappa\cdot\pi^*\lambda_g$
\textsc{(uniform-weight)} recovers the Mumford $\lambda$-class
clutching relation on $\overline{\cM}_g$.

The complementarity propagator
$P_\cA\colon H^*(\cA)\otimes H^*(\cA^!)\to\mathbb C$ is the Givental
$R$-matrix of the shadow CohFT; when it carries a flat unit (all
standard families with vacuum in $V$), Teleman reconstruction
recovers $\{\tau_{g,n}\}$ at all $(g,n)$ from genus-$0$ data and
$P_\cA$. Eynard--Orantin topological recursion is the MC equation
applied to the shadow obstruction tower.

\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{ll}

thinking
**Inspecting the theorem summary**

I need to look closely at the survey on the modular Koszul duality theorem, focusing on the summary at 643. It might be similar to version 2, so I’ll check that out. I want to inspect the context around lines 638 to 650 to ensure I have a clear understanding and to see how everything connects. I'm excited to dig into this!
exec
/bin/zsh -lc "sed -n '638,650p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
sum to a topological invariant. The coinvariant projection
yields the scalar complementarity $\kappa(\cA)+\kappa(\cA^!)=K(\cA)$,
where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.

\medskip
\noindent\textbf{Theorem D} (modular characteristic). For uniform
weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
correction $\delta F_g^{\mathrm{cross}}$.

\medskip
\noindent\textbf{Theorem H} (chiral Hochschild).
$\mathrm{ChirHoch}^*(\cA)$ has polynomial Hilbert series,
concentrated in cohomological degrees $\{0,1,2\}$.
exec
/bin/zsh -lc "sed -n '930,945p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '790,825p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '238,250p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

% ====================================================================
\subsection{The modular characteristic}
\label{ssec:kappa}
% ====================================================================

The modular characteristic $\kappa(\cA)$ is the single
scalar controlling the genus tower. It is computed from
genus-$0$ data alone: the leading coefficient of the OPE,
extracted through the bar construction.

\begin{table}[ht]
\centering
 succeeded in 52ms:
\label{rem:multi-weight}
For a chiral algebra with generators of distinct conformal
weights $h_1, \ldots, h_r$, the genus-$g$ free energy
decomposes as
\begin{equation}\label{eq:multi-weight-decomposition}
F_g(\cA)
\;=\;
\kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
\;+\;
\delta F_g^{\mathrm{cross}}(\cA)\,,
\end{equation}
where $\delta F_g^{\mathrm{cross}}$ is a graph sum over
mixed-channel boundary graphs of~$\overline{\cM}_{g,0}$.
At genus~$1$, $\delta F_1^{\mathrm{cross}} = 0$
unconditionally. For uniform-weight algebras
($h_1 = \cdots = h_r$),
$\delta F_g^{\mathrm{cross}} = 0$ at all genera. For
multi-weight algebras at $g \ge 2$, the correction is
generically nonzero: for $\cW_3$ at genus~$2$,
$\delta F_2^{\mathrm{cross}}(\cW_3)
 succeeded in 52ms:

\subsection*{The genus tower}

The bar complex traces a family of curved cochain complexes over
$\overline{\mathcal M}_g$. For uniform-weight algebras
(single-generator, or multi-generator with all generators of the
same conformal weight), the obstruction to flatness at
genus~$g$ is the characteristic class
\[
\mathrm{obs}_g(\cA)
\;=\;
\kappa(\cA)\cdot\lambda_g
\;\in\;
H^*(\overline{\mathcal M}_g),
\qquad
\lambda_g\;=\;c_g(\mathbb E),

thinking
**Inspecting mathematical details**

I think stale surfaces are calling for a shift away from using only genus-0 data to a more comprehensive genus-1/all-genera split. That’s important because the universal scalar no longer solely relies on genus-0 alone; it's influenced by genus-1 curvature too. However, kappa is still discernible at genus-0. I need to be precise here and take a closer look at the actual wording of the theorem `thm:genus-universality` and its corollary.
codex
I’m checking the live theorem statement again before patching the summaries, because the edits need to reflect the exact split already proved in source: genus~1 universally, all genera only on the proved scalar lane, and no circular dependence on the family-index theorem.
exec
/bin/zsh -lc "sed -n '1900,1948p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5426,5515p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5328,5425p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is therefore a one-variable recursion.
Every edge in every stable-graph contribution carries the standard
weight-$1$ propagator $d\log E(z,w)$, hence the standard Hodge bundle
$\mathbb{E}=R^0\pi_*\omega_\pi$
(Remark~\ref{rem:propagator-weight-universality}).
Because all strong generators have the same conformal weight, no
mixed-weight vertex channel is available: the scalar recursion
propagates the genus-$1$ coefficient through the same Hodge line at
every genus. The clutching maps for the Hodge bundle therefore force
\[
\Gamma_{\cA,g}
\;=\;
\kappa(\cA)\cdot c_g(\mathbb{E})
\;=\;
\kappa(\cA)\cdot\lambda_g
\qquad (g \geq 1),
\]
which is exactly \eqref{eq:genus-universality}. This argument uses
the genus-$1$ base case and the scalar shadow-tower recursion; it
does not invoke Theorem~\ref{thm:family-index}.
 succeeded in 52ms:
\hline
$W_3(c)$ & $\frac{5c}{6} \lambda_g$\rlap{${}^*$} & Conformal anomaly \\
\hline
Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
\hline
\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
\hline
\end{tabular}
\end{table}

\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a modular Koszul chiral algebra whose strong generators
all have the \emph{same} conformal weight. There exists a
genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
curvature, such that \begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
 succeeded in 52ms:

\begin{remark}[Relation to the \texorpdfstring{$\hat{A}$}{A-hat}-genus]\label{rem:A-hat-genus}
\index{A-hat genus@$\hat{A}$-genus}
The generating function $(x/2)/\sin(x/2)$ is the Wick rotation of the
$\hat{A}$-genus: $\hat{A}(x) = (x/2)/\sinh(x/2)$, related by the
substitution $x \mapsto ix$. This reflects the family
index theorem (Theorem~\ref{thm:family-index}) shows that
the genus expansion is the Gro\-then\-dieck--Rie\-mann--Roch pushforward of
the Todd class of the universal curve, and $(x/2)/\sin(x/2)$ is the
even part of the Wick-rotated Todd class. The positivity of all coefficients
($\lambda_g^{\mathrm{FP}} > 0$ for all~$g$), in contrast to the
alternating-sign $\hat{A}$-expansion, reflects the Hodge index
theorem on $\overline{\mathcal{M}}_g$.
\end{remark}

\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
\index{genus expansion!universal generating function}
\index{obstruction coefficient!generating function}
For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
exec
/bin/zsh -lc "sed -n '1860,1888p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
holomorphic (chiral bar) and topological (Kontsevich integral)
deformation problems are quasi-isomorphic.
(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
\end{remark}

\subsection{Anomaly cancellation and Koszul structure}
\label{subsec:anomaly-koszul}
\index{anomaly!Koszul-theoretic}

\begin{theorem}[Anomaly cancellation as Koszul constraint;
\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
\index{anomaly cancellation!Koszul constraint}
For the matter-ghost system
$\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The obstruction coefficient is additive:
 $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
 \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
\item The total bar complex is uncurved
 ($d_{\mathrm{bar}}^2 = 0$) if and only if
exec
/bin/zsh -lc "sed -n '1888,1918p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{proof}
Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
of the tensor product is the sum of the individual singular OPEs
(the fields act on disjoint sectors), so the genus-$1$ curvature
is additive. Part~(ii) follows from
$\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
(Theorem~\ref{thm:genus-universality},
Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
is the computation $\kappa(\mathrm{Vir}_c) = c/2$
(Computation~\ref{comp:virasoro-curvature}) combined with
$c_{\mathrm{ghost}} = -26$, so
$\kappa_{\mathrm{tot}} = c/2 - 13 = 0$ at $c = 26$.
\end{proof}

\begin{theorem}[Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0};
\ClaimStatusProvedHere]\label{thm:anomaly-physical-genus0}
The condition $\kappa_{\mathrm{tot}} = 0$
\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul})} is equivalent,
at genus~$0$, to the BRST anomaly cancellation
exec
/bin/zsh -lc 'rg -n "cor:kappa-additivity|Kappa additivity|tensor product" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1991:Since $\mathcal{A}$ is complete and separated, and the tensor product of
3799:\item \emph{Separating degeneration}: $\Sigma_g \rightsquigarrow \Sigma_{g_1} \cup \Sigma_{g_2}$ with $g_1 + g_2 = g$, contributing a term involving the tensor product of lower-genus bar complexes.
5923:\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
5934:The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
6016:under tensor products:
6019:\textup{(}Corollary~\ref{cor:kappa-additivity}\textup{)}. For
6039:\textup{(}Corollary~\ref{cor:kappa-additivity}\textup{)} gives a group
6100:\textup{(}Corollary~\ref{cor:kappa-additivity}\textup{)} extends the
6192:Let $\mathrm{KCA}$ denote the category of Koszul chiral algebras with tensor product $\otimes$. The obstruction coefficient defines a group homomorphism
6205:Additivity is Corollary~\ref{cor:kappa-additivity}. The unit $\mathbf{1}$ (trivial algebra) has $\kappa(\mathbf{1}) = 0$. Surjectivity follows from $\kappa(\mathcal{H}_q) = q$ for $q \in \mathbb{Q}$. Non-injectivity: the Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{g}}_{-h^\vee})$ is a non-trivial Koszul algebra with $\kappa = 0$. Part (iii) is Theorem~\ref{thm:genus-universality}(ii).
6838:for the tensor product over vertices, the cohomology is the
7205:tensor product. The factor $(-1)^{|E|}$ comes from the
exec
/bin/zsh -lc "sed -n '5923,5942p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
\index{obstruction coefficient!additivity}
For Koszul chiral algebras $\mathcal{A}$, $\mathcal{B}$ such that $\mathcal{A} \otimes \mathcal{B}$ is Koszul:
\begin{equation}\label{eq:kappa-additivity}
\kappa(\mathcal{A} \otimes \mathcal{B}) = \kappa(\mathcal{A}) + \kappa(\mathcal{B}).
\end{equation}
In particular, on the proved scalar lane,
$\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ for all $g \geq 1$.
\end{corollary}

\begin{proof}
The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}

\begin{example}
For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
\end{example}

\begin{corollary}[Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)}; \ClaimStatusProvedHere]
\label{cor:kappa-sum-wn}
\index{obstruction coefficient!W-algebra complementarity}

thinking
**Inspecting proof formatting**

I need to fix the proof formatting, as it has \end{proof} on the same line. I should also check the concordance references to cor:kappa-additivity to see if they're already routed; maybe no changes are necessary there. I might need to look at the theorem registry and the top table for any patches. Additionally, I need to inspect sections 1429 onward for more snippets and notes related to the remark.
exec
/bin/zsh -lc "sed -n '1425,1468p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
defined intrinsically, without reference to any theorem.
The MC equation $d_0\Theta + \frac{1}{2}[\Theta,\Theta] = 0$
is a tautology of the bar differential $D_\cA^2 = 0$.

Theorem~A uses only genus-$0$ data: the twisting morphism
and the Verdier functor on $\Ran(X)$. Theorem~B uses the
PBW filtration at genus~$0$. Theorem~C uses the Verdier
involution on $\Mbar_g$ applied to the objects constructed
in~A and identified in~B. Theorem~D uses the Lagrangian
decomposition from~C to extract the scalar shadow $\kappa$,
which was already present in the definition of $\Theta_\cA$
but not yet identified as universal. Theorem~H uses the
concentration result from Koszul duality (Theorem~B) to
bound the coderivation complex.

The routing is: bar-intrinsic MC element (definition)
$\to$ adjunction/intertwining (A) $\to$ inversion (B)
$\to$ polarization (C) $\to$ scalar extraction (D)
$\to$ coefficient ring (H). Each step uses results from
the previous step and new geometric input; no step
exec
/bin/zsh -lc "sed -n '968,1015p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\section{Theorem D: the genus expansion}
\label{sec:theorem-D}

\subsection{Statement}

The Lagrangian decomposition of Theorem~C separates $\cA$ from
$\cA^!$ on moduli space, but does not identify what the scalar
projection $\kappa$ governs at each genus.

\begin{theorem}[Theorem D: genus universality]
\label{thm:genus-universality}
Let $\cA$ be a chirally Koszul chiral algebra with modular
characteristic $\kappa(\cA)$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Genus $1$ (unconditional).}
 The genus-$1$ obstruction class is
 \[
 \obs_1(\cA) = \kappa(\cA) \cdot \lambda_1
 \in H^*(\Mbar_{1,1}),
 \]
exec
/bin/zsh -lc "sed -n '6035,6055p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6288,6300p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Theta_{\cA}$: it computes how the universal MC element
distributes its weight across genera. The Bernoulli numbers
appear because they are the Taylor coefficients of
$\operatorname{tr}(\Theta)$, not because of any formal group
coincidence. The formal group is additive because $\kappa$
itself is additive under tensor product
(Corollary~\ref{cor:kappa-additivity}), which in turn follows
from $\Theta_{\cA \otimes \cB} = \Theta_{\cA} + \Theta_{\cB}$
in the factorization algebra sense.
\end{remark}

\begin{remark}[Scalar free energy package]
\label{rem:concordance-scalar-free-energy}
 succeeded in 52ms:
\ClaimStatusProvedHere]\label{thm:family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families, including multi-generator.
Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
\begin{equation}\label{eq:modular-deformation-complex-concordance}
\mathcal{D}_{\cA}^{(g)}
\;:=\;
\kappa(\cA) \cdot \mathbb{E}
\;\in\; K_0(\overline{\mathcal{M}}_g) \otimes_{\mathbb{Z}} \mathbb{Q},
\end{equation}
the $K$-theory class given by $\kappa(\cA)$ copies of the
Hodge bundle. Then:
exec
/bin/zsh -lc "sed -n '6258,6275p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\mathcal{D}_{\cA^!}^{(g)} = \kappa(\cA^!) \cdot \mathbb{E}$
and the linearity of $F_g$ in~$\kappa$.
\end{proof}

\begin{remark}[GRR origin of the genus expansion]\label{rem:family-index-punchline}
The theorem strengthens
Theorem~\ref{thm:universal-generating-function}
by identifying the \emph{origin} of the generating function identity:
the scalar genus expansion of a Koszul chiral
algebra is the Grothendieck--Riemann--Roch pushforward of the
Todd class of the universal curve, scaled by the bar-complex
curvature. The $\hat{A}$-genus appears precisely because
$\hat{A}$ is the multiplicative genus associated to the formal
group law $F(x,y) = x + y$, the trivial (additive) formal
group, and the bar-complex genus expansion is additive in
$\kappa$. Equivalently, the Bernoulli numbers governing both the
Todd class and the $\psi$-$\lambda_g$ integrals are the same
Bernoulli numbers because both are computed by the same GRR



thinking
**Evaluating theorem references**

I'm pondering whether to keep or edit the line about "strengthens theorem universal generating function." It might not be necessary. For the patch regarding standalone survey modes and duality, I find the mention of Teleman's reconstruction from genus-0 data feels a bit off-track for Theorem D. The user specifically asked for searches related to Theorem D, so genus-0 data might not be relevant. I need to check other summaries for mentions of Theorem D and ensure they align with the user's request. The search results are extensive, but I'll focus on updating each to match the new status.
thinking
**Identifying false statements in summaries**

I need to systematically search through all standalone files for mentions of "Theorem D" and "genus-universality" to identify any false statements. Using rg with potential stale phrases is tricky, especially when looking for patterns like "all genera" near Theorem D. However, many summaries appear to be well-qualified already. I should look for exact stale phrases such as "genus-0 data alone" and "Theorem D is unconditional." Also, I’ll need to update theorem D mini-summaries that lack genus-1 clauses to ensure completeness.
thinking
**Checking for Theorem D summaries**

I see that the search results might only show the genus tower section without a summary for Theorem D. I need to look earlier in the file for a list of theorems to see if it's included there. My next step is to search for "Theorem D" in the relevant files to ensure I'm not missing any important details or summaries. It's essential to confirm whether Theorem D is mentioned and to gather any related context for clarity.
exec
/bin/zsh -lc "sed -n '55,90p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Theorem D|genus-universality|modular characteristic" standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/five_theorems_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 C2: shifted-symplectic/BV upgrade conditional on the
 uniform-weight perfectness package
 \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
\textbf{D} & Modular characteristic
 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
 on the proved uniform-weight lane at all genera
 \textup{(}Definition~\ref{def:scalar-lane},
 Thm~\ref{thm:modular-characteristic}\textup{)};
 genus~$1$ is universal for all families;
 multi-weight $g \geq 2$ acquires the cross-channel term
 $\delta F_g^{\mathrm{cross}}$
 \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
 the routing
 $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
 & \ClaimStatusProvedHere \\
\textbf{H} & Chiral Hochschild
 & On the Koszul locus at generic level:
 $\ChirHoch^*(\cA)$ is concentrated in $\{0,1,2\}$,
 satisfies the duality shift~$[2]$, has degree-$\leq 2$
 succeeded in 51ms:
standalone/five_theorems_modular_koszul.tex:226:the modular characteristic: the single number that survives
standalone/five_theorems_modular_koszul.tex:317:The modular characteristic is
standalone/five_theorems_modular_koszul.tex:569:The \emph{modular characteristic} of a chiral algebra $\cA$ is
standalone/five_theorems_modular_koszul.tex:937:opposite modular characteristic (the Verdier involution
standalone/five_theorems_modular_koszul.tex:968:\section{Theorem D: the genus expansion}
standalone/five_theorems_modular_koszul.tex:977:\begin{theorem}[Theorem D: genus universality]
standalone/five_theorems_modular_koszul.tex:978:\label{thm:genus-universality}
standalone/five_theorems_modular_koszul.tex:1395:The answer is Theorem~H. The modular characteristic $\kappa$
standalone/five_theorems_modular_koszul.tex:1554:The modular characteristic is $\kappa(\cH_k) = \av(r^{\cH}(z)) = k$.
standalone/five_theorems_modular_koszul.tex:1633:The Koszul dual has modular characteristic
standalone/five_theorems_modular_koszul.tex:1656:\subsection{Theorem D for $\cH_k$: the genus expansion}
standalone/five_theorems_modular_koszul.tex:1789:$\partial M^3 = \Sigma$. The modular characteristic
standalone/five_theorems_modular_koszul.tex:1846:which every invariant has been computed: the modular characteristic
standalone/five_theorems_modular_koszul.tex:2038:$2h^\vee$. The full modular characteristic is
standalone/five_theorems_modular_koszul.tex:2218:$c \mapsto 26 - c$. The modular characteristic:
standalone/five_theorems_modular_koszul.tex:2247:of conformal weights $2, 3, \ldots, N$. The modular characteristic:
standalone/five_theorems_modular_koszul.tex:2281:The modular characteristic $\kappa(\mathrm{BP}_k) = c/6$, and
standalone/programme_summary_sections2_4.tex:147:characteristic}. The modular characteristic is intrinsic to
standalone/programme_summary_sections2_4.tex:175:\begin{equation}\label{eq:genus-universality}
standalone/programme_summary_sections2_4.tex:240:\subsection{The modular characteristic}

thinking
**Inspecting theorem D summary**

I need to check the summary of theorem D in the program summary, particularly around line 1007. I'm considering how best to approach this inspection to ensure I grasp all the relevant details. It's important to be thorough so that I can provide accurate information based on what I find. Let’s see what’s going on around that line and understand any nuances involved with theorem D.
exec
/bin/zsh -lc "sed -n '430,460p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1004,1035p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure.
\end{theorem}
 succeeded in 51ms:
perfectness and nondegeneracy of the cyclic pairing.

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar determined by the
genus-$0$ data of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure.
exec
/bin/zsh -lc "sed -n '7988,8000p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8340,8355p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2328,2345p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1788,1805p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Gamma_2$ (two vertices, one edge): $\Phi^{\cH_k}_{\Gamma_2} = k$
(the level). Every graph with $|E| \ge 2$ vanishes because the only
OPE mode is $\alpha_{(1)}\alpha = k$, and two propagator insertions
on the same vertex yield zero by degree. Hence
$\Theta_{\cH_k} = k \cdot \eta_{\mathrm{univ}} \otimes
\Lambda_{\mathrm{univ}}$: the MC element is a scalar multiple of
the universal class. The genus-$g$ projection is
$F_g(\cH_k) = k \cdot \lambda_g^{\mathrm{FP}}$
\textup{(\textsc{uniform-weight})}. The modular characteristic
$\kappa(\cH_k) = k$ is the sole surviving datum.

\medskip
\noindent\textbf{Kac--Moody: $\Theta_{\widehat\fg_k}$ terminates at
degree~$3$.}\enspace
For the affine Kac--Moody algebra $\widehat\fg_k$, the graph
amplitudes at degree $r\le 3$ are:
\begin{itemize}
\item Degree~$2$: the single-edge graph gives
 succeeded in 52ms:
\item $D_\cA^2 = 0$: the bar differential squares to zero at
all genera and degrees (Theorems~\ref{thm:bar-modular-operad},
\ref{thm:quantum-diff-squares-zero}).
\item $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for
uniform-weight algebras at all genera , and
unconditionally at genus~$1$ for all families; for multi-weight
algebras at $g \ge 2$ (all-weight), with cross-channel
correction $\delta F_g^{\cross}$
(Theorem~\ref{thm:modular-characteristic},
Theorem~\ref{thm:multi-weight-genus-expansion}).
\item $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline\cM_g, Z(\cA))$:
complementarity assembles the Koszul pair into a Lagrangian
decomposition
 succeeded in 52ms:
four independent proved tests:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $D_\cA^2 = 0$:
 the bar differential squares to zero at all genera and degrees
 \textup{(}Theorems~\textup{\ref{thm:bar-modular-operad},
 \ref{thm:quantum-diff-squares-zero}}\textup{)}.
\item $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
 for uniform-weight algebras at all genera,
 and unconditionally at genus~$1$ for all families:
 the genus-$g$ obstruction factors as modular characteristic
 times Hodge class
 \textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)}.
\item $Q_g(\cA)+Q_g(\cA^!)=H^*(\overline{\mathcal M}_g,Z(\cA))$:
 complementarity assembles the Koszul pair into a Lagrangian
 decomposition
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 succeeded in 51ms:
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
restricted to genus~$0$).

\subsection*{3.4.\enspace Homotopy chiral algebras}

The convolution algebra requires a cochain-level algebraic input, not
merely the cohomology-level chiral bracket. The \v Cech totalisation
provides this: it replaces the strict chiral algebra with a
homotopy-coherent model carrying all derived OPE data.


thinking
**Revising theorem D summary**

I’m considering updating the statement in the program summary to say it’s “determined by genus-1 curvature” instead of genus-0 data. It seems okay to reference the genus-0 OPE, but it might be better to clarify that it’s proved by genus-1 curvature. I want to incorporate the cross-channel correction in the summary of theorem D and survey v2. I’ll also check the modular Koszul duality regarding theorem D, possibly around 641. Let's look into it!
exec
/bin/zsh -lc "sed -n '636,648p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
factors are~$\alpha$; since $\mathbf 1_{(p)}\alpha=0$ for
$p\ge 0$, no further contractions occur. All structure is
captured at tensor degree~$2$: the bar complex is
\emph{quadratic}. The Heisenberg algebra is chirally Koszul.

The modular characteristic:
\[
\kappa(\mathcal H_k)\;=\;k.
\]
The Koszul dual is the \emph{curved} symmetric chiral algebra
\[
\mathcal H_k^!
\;=\;
exec
/bin/zsh -lc "sed -n '420,435p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2338,2350p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '990,1005p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{theorem}

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi, is conditional on
perfectness and nondegeneracy of the cyclic pairing.

% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

 succeeded in 51ms:

\medskip
\noindent\textbf{Kac--Moody: $\Theta_{\widehat\fg_k}$ terminates at
degree~$3$.}\enspace
For the affine Kac--Moody algebra $\widehat\fg_k$, the graph
amplitudes at degree $r\le 3$ are:
\begin{itemize}
\item Degree~$2$: the single-edge graph gives
$\Phi_{\Gamma_2}=k\,\Omega=k\sum_a t^a\otimes t^a$ (the Casimir, with
level prefix; at $k=0$, $\Phi=0$). Averaging:
$\mathrm{av}(\Phi_{\Gamma_2})=\kappa=(k+h^\vee)\dim\fg/(2h^\vee)$.
\item Degree~$3$: the trivalent tree gives
$\Phi_{\Gamma_3}(a,b,c)=\kappa([a,b],c)$, where $[\cdot,\cdot]$ is
 succeeded in 51ms:
\operatorname{fib}(\sigma - \mathrm{id})$
and\/ $\mathbf{Q}_g(\cA^!) =
\operatorname{fib}(\sigma + \mathrm{id})$ are
Lagrangian for the $(-1)$-shifted symplectic pairing
on\/~$\mathbf{C}_g$.
\end{theorem}

The eigenspace decomposition (C1) is unconditional: it
holds for all modular Koszul algebras at all genera. The
scalar identity $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
on each summand (C2) requires the uniform-weight hypothesis
at $g \ge 2$. The Lagrangian property, a
$(-1)$-shifted symplectic statement in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}, is conditional on
perfectness and nondegeneracy of the cyclic pairing.

exec
/bin/zsh -lc "sed -n '2628,2638p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
are computed; the standard landscape is fully mapped.
Six new results extend the proved core: the universal
genus-$g$ shadow identity $\alpha_g = \kappa \cdot
\lambda_g^{\mathrm{FP}}$ at all genera (uniform-weight),
the soft graviton theorem $a_3 = 2$ fixing the cubic
shadow coefficient, and free-field exactness of the bar
complex (the bar spectral sequence collapses at $E_1$
for all free-field algebras). The full programme now
comprises 4,542 pages across three volumes, verified by
120K+ independent computational tests.
CY-A at $d = 3$ is the single point where the programme
exec
/bin/zsh -lc "rg -n \"genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|Theorem~D is unconditional|Theorem D is unconditional|uses the Lagrangian decomposition|genus expansion of Theorem~D|Theorem~D uses the Lagrangian decomposition|Theorem~D uses|the scalar formula '"\\\\mathrm\\{obs\\}_g = \\\\kappa\\\\cdot\\\\lambda_g holds at all genera because|all genera because the\" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:genus-$0$ data alone|genus-$0$ data of|restricted to genus~$0$|Theorem~D is unconditional|Theorem D is unconditional|uses the Lagrangian decomposition|genus expansion of Theorem~D|Theorem~D uses the Lagrangian decomposition|Theorem~D uses|the scalar formula \mathrm\{obs\}_g = \kappa\cdot\lambda_g holds at all genera because|all genera because the)
                                                                                                                                                                                                                                                                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "genus-$0$ data alone" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "restricted to genus~$0$" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "uses the Lagrangian decomposition" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "genus-$0$ data of" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Theorem~D is unconditional" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 exited 1 in 50ms:

 exited 1 in 50ms:

 exited 1 in 51ms:

 succeeded in 50ms:
chapters/theory/introduction.tex:2499: Theorem~D is unconditional.
chapters/frame/preface.tex:3105:(Theorem~D is unconditional there) and requires the interaction of
exec
/bin/zsh -lc 'rg -n -F "Theorem~D uses the Lagrangian decomposition" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "genus expansion of Theorem~D" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "holds at all genera because the" standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/five_theorems_modular_koszul.tex:1302:is vacuous and the genus expansion of Theorem~D is
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
 succeeded in 51ms:
chapters/frame/preface.tex:3072:scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
 exited 1 in 51ms:


thinking
**Exploring command strings**

I'm thinking about some interesting fixed strings that involve the dollar sign, especially in the context of shell expansion. It seems like if I use double quotes, it might expand to the script name. So, I guess I really need single quotes instead. Anyway, I need to focus on searching for "genus-0 data" without any dollar signs. I might just use regex with single quotes for that search.
codex
The theorem-scope audit is stable now. I’m applying the edits in two batches: core chapter surfaces first, then the standalone summaries and routing prose that still imply an all-genera or C-to-D dependency that the live proof no longer uses.
exec
/bin/zsh -lc "rg -n 'genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~D|genus-universality|family-index|all genera' standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/survey_modular_koszul_duality.tex standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'determined by the genus-\\"'$0'"\\"'$|determined already at genus~'"\\"'$0'"\\"'$|determined by genus-'"\\"'$0'"\\"'$'"' standalone/*.tex chapters/theory/introduction.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections2_4.tex:246:genus-$0$ data alone: the leading coefficient of the OPE,
standalone/programme_summary_sections2_4.tex:443:genus-$0$ data of\/~$\cA$. The generating function is
standalone/programme_summary.tex:820:genus-$0$ data alone: the leading coefficient of the OPE,
standalone/programme_summary.tex:1018:genus-$0$ data of\/~$\cA$. The generating function is
standalone/survey_modular_koszul_duality_v2.tex:1797:restricted to genus~$0$).
 succeeded in 50ms:
standalone/shadow_towers.tex:1097:The algebraic depth is determined by genus-$0$ OPE data
standalone/shadow_towers_v3.tex:2938:The algebraic depth is determined by genus-$0$ OPE data
 succeeded in 50ms:
standalone/five_theorems_modular_koszul.tex:96:standard landscape at all genera.
standalone/five_theorems_modular_koszul.tex:103:Theorem~D identifies the genus expansion: on the
standalone/five_theorems_modular_koszul.tex:106:\textup{(UNIFORM-WEIGHT)} at all genera, with generating
standalone/five_theorems_modular_koszul.tex:545:\subsection{From genus $0$ to all genera}
standalone/five_theorems_modular_koszul.tex:757: inversion is unconditional at all genera.
standalone/five_theorems_modular_koszul.tex:811:unconditional at all genera: the curvature
standalone/five_theorems_modular_koszul.tex:978:\label{thm:genus-universality}
standalone/five_theorems_modular_koszul.tex:1116:\begin{example}[Heisenberg at all genera]\label{ex:thmD-heis}
standalone/five_theorems_modular_koszul.tex:1146:Theorem~D identifies a universal genus expansion governed by
standalone/five_theorems_modular_koszul.tex:1302:is vacuous and the genus expansion of Theorem~D is
standalone/five_theorems_modular_koszul.tex:1321:complementary. The genus expansion of Theorem~D uses the
standalone/five_theorems_modular_koszul.tex:1342:Theorem~D cannot distinguish the universal scalar
standalone/five_theorems_modular_koszul.tex:1378:Without Theorem~D, the coefficient ring of the genus tower
standalone/five_theorems_modular_koszul.tex:1390:$\ChirHoch^*(\cA)$. Theorem~D demonstrates that the
standalone/five_theorems_modular_koszul.tex:1400:and the coefficient ring is polynomial. Without Theorem~D's
standalone/five_theorems_modular_koszul.tex:1418:$\kappa$ (which is computed in Theorem~D). The resolution is
standalone/five_theorems_modular_koszul.tex:1433:in~A and identified in~B. Theorem~D uses the Lagrangian
standalone/five_theorems_modular_koszul.tex:1810:B & $\Omega(\barB(\cH_k)) \simeq \cH_k$, all genera
standalone/programme_summary_sections2_4.tex:171:generator (or more generally with all generators of the
standalone/programme_summary_sections2_4.tex:175:\begin{equation}\label{eq:genus-universality}
exec
/bin/zsh -lc "rg -n 'restricted to genus|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|Theorem~D is unconditional|uniform-weight; multi-weight'"' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Reviewing theorem summaries**

I’m not finding exact matches, which makes me think there might be a mistake in the summary. I might need to patch the `standalone/programme_summary` theorem list at the top. There could be a short summary of Theorem D earlier without that genus1 clause. I should check around line 70 and maybe look at line 2232 to investigate further. Let’s get into the details to clear this up!
exec
/bin/zsh -lc "sed -n '2228,2238p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '72,92p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6428,6442p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,648p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '92,110p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The propagator itself is always weight-$1$ at the edge
level ($d\log E$ has conformal weight~$1$); the mixing
enters through the vertex structure constants.

For uniform-weight algebras (all generators of the same
conformal weight), $\delta F_g^{\mathrm{cross}} = 0$
at all genera and the scalar universality
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ holds
without correction. For multi-weight algebras, the
full genus expansion is
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}
 succeeded in 50ms:

\date{\today}

\begin{abstract}
We survey the modular Koszul duality programme for chiral
algebras on algebraic curves. The bar construction of a
chiral algebra produces a factorization coalgebra whose
differential encodes operator product singularities and
whose curvature at genus~$g \ge 1$ is controlled by a
single scalar, the modular characteristic~$\kappa$.
Five theorems describe the resulting structure: bar-cobar
adjunction with Verdier intertwining~(A), bar-cobar
inversion on the Koszul locus~(B), complementarity
decomposition with shifted-symplectic Lagrangian
geometry~(C), the genus expansion
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
the Hirzebruch $\hat{A}$-class~(D), and polynomial
chiral Hochschild cohomology~(H). All five are projections
of a single universal Maurer--Cartan element~$\Theta_\cA$
in the modular convolution algebra. The shadow obstruction
 succeeded in 51ms:
 \]

\item \emph{Verdier intertwining.}
 Verdier duality on $\Ran(X)$ intertwines the bar construction
 of $\cA$ with the bar construction of $\cA^!$:
 \[
 \mathbb{D}_{\Ran}\, \barB_X(\cA)
 \;\simeq\;
 \cA^!_\infty,
 succeeded in 51ms:
Lagrangian self-intersection
$\mathfrak S = \cL \times_\cM \cL$ in a $(-2)$-shifted
symplectic stack. Every theorem is a face of that geometry:
Theorem~A is the groupoid comodule-module adjunction for
$\mathfrak S$; Theorem~B (bar-cobar inversion) reconstructs
the Lagrangian from its clean self-intersection; Theorem~C
(complementarity) is two Lagrangians whose intersection
carries a $(-1)$-shifted symplectic structure; Theorem~D is
the Kodaira--Spencer class; Theorem~H (Hochschild polynomial
growth) is the HKR theorem for the Lagrangian embedding.

\subsection*{10.9.\enspace Factorization-primary hierarchy}

$\SCchtop$ is a \emph{local model}: the formal completion of a
factorisation structure at collision points. The global truth
 succeeded in 51ms:
dual $\cA^!_\infty$.
Theorem~B proves bar-cobar inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on the
Koszul locus: unconditionally at genus $0$ and on the
standard landscape at all genera.
Theorem~C decomposes the genus-$g$ ambient complex into
Verdier-Lagrangian complements
$Q_g(\cA) \oplus Q_g(\cA^!) \cong
H^*(\Mbar_g, \cZ_\cA)$, with the Koszul complementarity
sum $\kappa(\cA) + \kappa(\cA^!)$ family-dependent: $0$ for
Kac--Moody and free fields, $13$ for Virasoro.
Theorem~D identifies the genus expansion: on the
uniform-weight lane,
$\obs_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)} at all genera, with generating
function the $\Ahat$-genus; at genus $1$ the scalar
formula is unconditional for every family.
Theorem~H proves that chiral Hochschild cohomology is
concentrated in degrees $\{0,1,2\}$ with a polynomial

thinking
**Examining programme summary**

I'm considering whether the programme summary should mention genus 1 unconditional. Since the user is specifically searching for Theorem D, it makes sense to focus on that. The current summary mentions uniform-weight but lacks genus-1, which is okay. However, to align with the new status, I might want to add something about the genus-1 scalar clause being universal for every family. I'll also check the preface for correctness and target the concordance for any stale references. It's time to search!
exec
/bin/zsh -lc "rg -n 'Theorem~D is unconditional|Theorem D is unconditional|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|uses the Lagrangian decomposition|genus expansion of Theorem~D|family-index.*input to Theorem~'"\\\\ref\\{thm:genus-universality\\}' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Corollary~\\\\ref\\{cor:kappa-additivity\\}|thm:universal-generating-function|thm:anomaly-koszul' chapters/connections/concordance.tex chapters/frame/preface.tex chapters/theory/introduction.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
standalone/introduction_full_survey.tex:2200:(Theorem~\ref{thm:universal-generating-function};
standalone/introduction_full_survey.tex:4733:(Theorem~\ref{thm:universal-generating-function}) are consequences
chapters/theory/introduction.tex:639: \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
chapters/theory/introduction.tex:1923:(Theorem~\ref{thm:universal-generating-function}) are consequences
chapters/connections/concordance.tex:6029:expansion (Theorem~\ref{thm:universal-generating-function})
chapters/connections/concordance.tex:6264:Theorem~\ref{thm:universal-generating-function}
chapters/connections/concordance.tex:6294:(Corollary~\ref{cor:kappa-additivity}), which in turn follows
standalone/theorem_index.tex:1407:theorem & \detokenize{thm:universal-generating-function} & \detokenize{Universal generating function} & \texttt{ProvedHere} & \detokenize{chapters/examples/genus_expansions.tex:1914}\\
standalone/theorem_index.tex:2120:theorem & \detokenize{thm:anomaly-koszul} & \detokenize{Anomaly cancellation as Koszul constraint} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1869}\\
standalone/survey_modular_koszul_duality.tex:4264:(Theorem~\ref{thm:universal-generating-function}).

thinking
**Inspecting introduction lines**

I’m considering whether I need to patch the introduction line 1923 or the introduction_full_survey. It seems the universal generating function consequences might benefit from a qualifier. I should inspect the search results since the user is looking for a specific introduction, not the full survey. However, the standalone introduction_full_survey might need checking to see if it's stale. I’ll need to make sure everything is up to date and relevant.
exec
/bin/zsh -lc "sed -n '2194,2204p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1917,1928p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
give the architecture; the standard landscape (Part~\ref{part:standard-landscape},
Table~\ref{tab:master-invariants}) tests it. The shared discriminant
$\Delta(x) = 1 - 2x - 3x^2$
(Theorem~\ref{thm:ds-bar-gf-discriminant}) and the universal
generating function
$\sum_{g \geq 1} F_g x^{2g} = \kappa \cdot (\hat{A}\text{-genus})$ (uniform-weight)
(Theorem~\ref{thm:universal-generating-function}) are consequences
of the proved scalar and spectral layers.
The results, taken together, form three concentric rings of decreasing
logical certainty.

\emph{Ring~1: the proved modular Koszul core.}
 succeeded in 52ms:
$\hat{A}$-genus $(x/2)/\sinh(x/2)$ from the
Atiyah--Singer index theorem; the positivity
$\lambda_g^{\mathrm{FP}} > 0$ reflects the Hodge index theorem
on~$\overline{\mathcal{M}}_g$.
For a free fermion, the formula yields the spin partition function;
for the Virasoro algebra, the one-loop string amplitude
(Theorem~\ref{thm:universal-generating-function};
equation~\eqref{eq:ahat-universality-preface}).

\subsection{The spectral discriminant}
\label{subsec:spectral-discriminant-intro}
exec
/bin/zsh -lc "sed -n '4728,4738p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4258,4268p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Table~\ref{tab:master-invariants}). The shared discriminant
$\Delta(x) = 1 - 2x - 3x^2$
(Theorem~\ref{thm:ds-bar-gf-discriminant}) and the universal
generating function
$\sum_{g \geq 1} F_g x^{2g} = \kappa \cdot (\hat{A}\text{-genus})$ (uniform-weight)
(Theorem~\ref{thm:universal-generating-function}) are consequences
of the proved scalar and spectral layers.


\section{Beyond the five theorems: three concentric rings}
\label{subsec:three-concentric-rings}
 succeeded in 52ms:
\kappa\Bigl(\frac{x/2}{\sin(x/2)} - 1\Bigr).
\end{equation}
The Taylor coefficients $\lambda_g^{\mathrm{FP}}$ are the
Faber--Pandharipande evaluations of the Hodge class: $\lambda_1^{\mathrm{FP}} = 1/24$,
$\lambda_2^{\mathrm{FP}} = 7/5760$,
$\lambda_3^{\mathrm{FP}} = 31/967680$
(Theorem~\ref{thm:universal-generating-function}).
The series converges:
$|F_g|\sim 2|\kappa|/(2\pi)^{2g}$
(exponential decay), in contrast to the bosonic string where
$F_g\sim(2g{-}2)!$ from the noncompactness of~$\mathbf{R}^d$.
exec
/bin/zsh -lc "sed -n '892,905p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}\label{eq:pref-curvature}
d_{\mathrm{fib}}^{2}\;=\;\kappa(\cA)\cdot\omega_g,
\end{equation}
where $\omega_g$ is the Arakelov $(1,1)$-form on the fibre of the
universal curve $\pi\colon\mathcal C_g\to\overline{\mathcal M}_g$, and
$\kappa(\cA)\in\Bbbk$ is the \emph{modular characteristic}, determined
entirely by the leading OPE singularity. The class $\omega_g$ lives on
the fibre $\Sigma_g$, not on the moduli space $\overline{\cM}_g$; its
pushforward $\pi_*\omega_g=c_1(\mathbb E)=\lambda_1$ lands in
$H^2(\overline{\cM}_g)$.

Two conventions coexist. The bar differential $d_{\mathrm{bar}}^2=0$
\emph{always}, at every genus: the bar construction is a dg coalgebra
by definition. The fiberwise differential $d_{\mathrm{fib}}^2=\kappa\cdot\omega_g$
exec
/bin/zsh -lc "sed -n '1525,1535p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2338,2350p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~D is|genus-\\"'$1'"\\"'$ clause|genus-'"\\"'$1'"\\"'$ specialization|unconditional for every family|multi-weight.*g '"\\\\ge 2|cross-channel correction' standalone/five_theorems_modular_koszul.tex standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Section 7: Multi-weight
% ================================================================
\section{Multi-weight structure and cross-channel
corrections}\label{sec:multi-weight}

The scalar formula $\obs_g = \kappa\cdot\lambda_g$ holds at
all genera for uniform-weight algebras.
The forced question: does it hold for multi-weight algebras,
where generators have different conformal weights?
The answer is no. At genus~$1$ the formula remains exact
(unconditionally), but at genus~$\ge 2$ a cross-channel
 succeeded in 51ms:
in the modular convolution algebra~$\gAmod$.
The existence of~$\Theta_\cA$ is encoded by the bar-cobar adjunction:
Theorem~A constructs the arena in which~$\Theta_\cA$ lives.
Bar-cobar inversion proves that~$\Theta_\cA$ is a complete invariant:
Theorem~B recovers~$\cA$ from~$\Theta_\cA$.
Verdier duality decomposes~$\Theta_\cA$ into complementary halves:
Theorem~C splits the genus tower into Lagrangian summands.
The leading coefficient of~$\Theta_\cA$ is the modular characteristic:
Theorem~D extracts the scalar $\kappa(\cA)$ with $\hat A$-genus generating function.
The coefficient ring of~$\Theta_\cA$ is the chiral Hochschild complex:
Theorem~H identifies the deformation ring.

The finite-order projections of~$\Theta_\cA$ form an obstruction tower
 succeeded in 51ms:
standalone/programme_summary_sections2_4.tex:233:multi-weight algebras at $g \ge 2$, the correction is
standalone/programme_summary_sections2_4.tex:453:single number. Theorem~D is the all-genera identity on the
standalone/programme_summary.tex:807:multi-weight algebras at $g \ge 2$, the correction is
standalone/programme_summary.tex:1028:single number. Theorem~D is the all-genera identity on the
standalone/introduction_full_survey.tex:777:\emph{fails} at $g \geq 2$: a nonzero cross-channel correction
standalone/introduction_full_survey.tex:1620: free energy receives a cross-channel correction
standalone/introduction_full_survey.tex:2099:formula fails at $g \geq 2$: a cross-channel correction from
standalone/introduction_full_survey.tex:2108:genus-$2$ cross-channel correction
standalone/introduction_full_survey.tex:2119:The cross-channel correction $\delta F_2 = (c{+}204)/(16c)$ is
standalone/introduction_full_survey.tex:2125:The gravitational cross-channel correction has a
standalone/introduction_full_survey.tex:2141:\item \textbf{Universality.} The cohomological identity $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ and the Faber--Pandharipande free-energy formula hold at all genera for uniform-weight algebras (Theorem~\ref{thm:genus-universality}). For multi-weight algebras (e.g.\ $\mathcal{W}_N$, $N \geq 3$), the scalar formula fails at $g \geq 2$: a nonzero cross-channel correction appears (Theorem~\ref{thm:multi-weight-genus-expansion}). The scalar $\kappa$ is determined by the genus-$1$ value alone: the clutching maps of stable curves propagate the genus-$1$ curvature to all genera via the modular operad structure.
standalone/five_theorems_modular_koszul.tex:108:formula is unconditional for every family.
standalone/five_theorems_modular_koszul.tex:1302:is vacuous and the genus expansion of Theorem~D is
standalone/five_theorems_modular_koszul.tex:1667:No cross-channel correction: $\delta F_g^{\mathrm{cross}} = 0$
standalone/five_theorems_modular_koszul.tex:1831:genus expansion acquires cross-channel corrections for multi-weight
standalone/five_theorems_modular_koszul.tex:2265:cross-channel correction $\delta F_g^{\mathrm{cross}}$
standalone/survey_modular_koszul_duality_v2.tex:1077:\emph{fails}: a cross-channel correction from mixed-propagator
standalone/survey_modular_koszul_duality_v2.tex:1085:\textsc{(all-weight, with cross-channel correction)}.
standalone/survey_modular_koszul_duality_v2.tex:4471:(all-weight, with cross-channel correction.)
standalone/survey_modular_koszul_duality_v2.tex:5915:\textsc{(all-weight, with cross-channel correction)}.
exec
/bin/zsh -lc "sed -n '1456,1470p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $P(t) = 1 + t^2$ (Virasoro) does not determine
 $\kappa = c/2$; it constrains $\dim \ChirHoch^2 = 1$
 (the space where $\kappa$ lives has dimension~$1$) but
 not the value.

\item \emph{D does not imply C.} The formula
 $\obs_g = \kappa \cdot \lambda_g$ could hold
 without a Lagrangian decomposition: one could imagine
 a non-decomposable ambient complex whose scalar
 projection still factors through $\kappa$. Theorem~C
 is stronger; it provides the \emph{reason} for the
 factorization.

\item \emph{C does not imply B.} The Lagrangian
 decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is

thinking
**Considering theorem modifications**

I’m thinking that I could prove kappa additivity and then reference the second sentence to focus on the scalar lane. That sounds good! I wonder if I could patch the theorem with a remark or maybe a corollary statement. I’ll consider adding line breaks and revisions to `chapters/theory/introduction.tex`, `preface.tex`, and possibly `standalone/five_theorems_modular_koszul.tex` for routing properties and remarks. This could improve clarity a lot!
codex
I’ve hit one local theorem surface that is more delicate than the routing fix: `thm:anomaly-koszul` still states `d_{\mathrm{bar}}^2 = 0`, which conflicts with the repo-wide bar/fiberwise differential discipline. I’m checking the local notation now so I can fix the dependency direction without silently preserving a notation-level falsehood.
exec
/bin/zsh -lc "sed -n '1848,1898p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:anomaly-koszul\\}|d_\\{\\\\mathrm\\{bar\\}\\}\\"'^2|d_'"\\{\\\\mathrm\\{fib\\}\\}\\"'^2|uncurved'"' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Getzler--Kapranov \cite{GeK98}), and our identification
$\barB^{\mathrm{full}} \simeq \mathrm{FT}$
(Theorem~\ref{thm:prism-higher-genus}) extends this to Koszul
chiral algebras. The gap at higher genus is the passage from
complex curves to real $1$-manifolds: our propagators are
holomorphic, while Kontsevich's are real. Comparing requires an
analytic continuation argument from holomorphic to topological
Feynman transforms.
The correct bridge between holomorphic and topological frameworks is Chern--Simons gauge equivalence, not merely restriction from complex curves to $S^1$: Cattaneo--Mnev~\cite{CattaneoMnev10} establish that configuration space integrals on $3$-manifolds produce Vassiliev invariants via BV integration, and the comparison map involves the CS partition function (not a pointwise restriction of propagators).

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
The conjecture asserts that the dg Lie algebras controlling
holomorphic (chiral bar) and topological (Kontsevich integral)
deformation problems are quasi-isomorphic.
(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
\end{remark}

\subsection{Anomaly cancellation and Koszul structure}
\label{subsec:anomaly-koszul}
\index{anomaly!Koszul-theoretic}
 succeeded in 51ms:
712:fiberwise curvature $d_{\mathrm{fib}}^2$ on the bar complex of a
922:the curvature $d_{\mathrm{fib}}^2 = \kappa(\mathcal{A})
1870:\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
1878:\item The total bar complex is uncurved
1879: ($d_{\mathrm{bar}}^2 = 0$) if and only if
1896:uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
2198:Hodge pages are paired. The strongest uncurved form occurs on the
2200:$\Theta_\cA^{\min} = 0$ and the bar complex is uncurved.
2312:mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
2756: Anomaly cancellation implies uncurved duality
exec
/bin/zsh -lc "rg -n 'anomaly-koszul|uncurved \\(\\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$'"\\)|d_\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/introduction_full_survey.tex:5364:$d_{\mathrm{bar}}^2 = 0$
chapters/theory/introduction.tex:2642:$d_{\mathrm{bar}}^2 = 0$
standalone/theorem_index.tex:2120:theorem & \detokenize{thm:anomaly-koszul} & \detokenize{Anomaly cancellation as Koszul constraint} & \texttt{ProvedHere} & \detokenize{chapters/connections/editorial_constitution.tex:1869}\\
standalone/e1_primacy_ordered_bar.tex:422:The ordered bar differential satisfies $d_{\mathrm{bar}}^2 = 0$.
standalone/e1_primacy_ordered_bar.tex:493:$\overline{\FM}_3(\CC)$ gives $d_{\mathrm{bar}}^2 = 0$: the three
standalone/chiral_chern_weil.tex:1233:differential satisfies $d_{\mathrm{bar}}^2 = 0$. On a

thinking
**Inspecting theorem references**

I’ve spotted references in the introduction and standalone/introduction_full_survey concerning the theorem anomaly-Koszul and the condition d_bar^2=0. I think I need to explore the context of these references to understand how they might relate. This could help clarify or fix the statement in item (ii) more broadly. So, I'll search specifically around intro section 2642 to gather relevant insights.
exec
/bin/zsh -lc "sed -n '2634,2648p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5358,5370p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2748,2762p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2298,2318p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\subsection{Ambient category}
\label{subsec:ambient-category}

All $\mathcal{D}$-modules are holonomic. The cobar
construction is the Verdier dual of the bar complex
(Definition~\ref{def:geom-cobar-intrinsic}), so
$d_{\mathrm{cobar}}^2 = 0$ follows from
$d_{\mathrm{bar}}^2 = 0$
(Corollary~\ref{cor:cobar-nilpotence-verdier}).
Grading is cohomological ($|d| = +1$); see
Appendix~\ref{app:signs}.
\index{grading convention!cohomological}
All chiral algebras are augmented
($\varepsilon\colon \cA \to \omega_X$,
 succeeded in 50ms:
\label{subsec:ambient-category}

All $\mathcal{D}$-modules are holonomic. The cobar
construction is the Verdier dual of the bar complex
(Definition~\ref{def:geom-cobar-intrinsic}), so
$d_{\mathrm{cobar}}^2 = 0$ follows from
$d_{\mathrm{bar}}^2 = 0$
(Corollary~\ref{cor:cobar-nilpotence-verdier}).
Grading is cohomological ($|d| = +1$); see
Appendix~\ref{app:signs}.
\index{grading convention!cohomological}
All chiral algebras are augmented
($\varepsilon\colon \cA \to \omega_X$,
 succeeded in 52ms:
Each entry gives the label, a brief description,
and the section where it appears.

\smallskip
\noindent\textbf{Algebraic structure.}

\begin{itemize}[nosep]
\item Conjecture~\ref{conj:anomaly-cancellation}:
 Anomaly cancellation implies uncurved duality
 (\S\ref{sec:first-complete-proof}).
\item Conjecture~\ref{conj:brst-cohomology}:
 Heuristic BRST/bar comparison, general genus
 (\S\ref{sec:first-complete-proof}).
\item Conjecture~\ref{conj:cobar-physical}:
 Cobar elements as on-shell propagator templates
 succeeded in 52ms:
as common foundation, but diverge in application: Programme~I
computes $\mathsf{E}_n$-operadic Koszul duals via configuration
space integrals on $n$-manifolds, while Programme~II specializes
from complex curves to real circles, extracting knot invariants via
the Kontsevich integral. At $n = 3$, the two programmes converge:
the $\mathsf{E}_3$-bar complex on a $3$-manifold computes
perturbative Chern--Simons invariants, and the restriction to
configuration spaces of circles in $S^3$ produces precisely the
Vassiliev weight systems of Programme~II
(Proposition~\ref{prop:vassiliev-genus0}).

The anomaly cancellation programme
(\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
physical condition for consistent quantization
(Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
the curvature $m_0 = \kappa \cdot \mathbf{1}$ plays the role of
the cosmological constant: the bar-cobar adjunction
codex
I found a second-order theorem-surface issue under AP228: the anomaly theorem still says `d_{\mathrm{bar}}^2 = 0`, but the actual curvature condition is fiberwise. I’m correcting that statement and the one downstream prose reference that repeats it, rather than leaving a notation-level contradiction in place.
exec
/bin/zsh -lc "rg -n 'd_\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0|d_'"\\{\\\\mathrm\\{fib\\}\\}\\"'^2 = 0|kappa_'"\\{\\\\mathrm\\{tot\\}\\} = 0|anomaly cancellation programme' chapters/connections/editorial_constitution.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{thm:anomaly-koszul\\}|anomaly cancellation as Koszul constraint' chapters/theory/introduction.tex chapters/frame/preface.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/e1_primacy_ordered_bar.tex:422:The ordered bar differential satisfies $d_{\mathrm{bar}}^2 = 0$.
standalone/e1_primacy_ordered_bar.tex:493:$\overline{\FM}_3(\CC)$ gives $d_{\mathrm{bar}}^2 = 0$: the three
standalone/introduction_full_survey.tex:5364:$d_{\mathrm{bar}}^2 = 0$
standalone/analytic_sewing.tex:2542:quasi-isomorphism: $d_{\mathrm{fib}}^2 = 0$ and the harmonic
chapters/theory/introduction.tex:2642:$d_{\mathrm{bar}}^2 = 0$
chapters/connections/editorial_constitution.tex:1879: ($d_{\mathrm{bar}}^2 = 0$) if and only if
chapters/connections/editorial_constitution.tex:1884: $\kappa_{\mathrm{tot}} = 0$ precisely at $c = 26$.
chapters/connections/editorial_constitution.tex:1896:uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
chapters/connections/editorial_constitution.tex:1905:The condition $\kappa_{\mathrm{tot}} = 0$
chapters/connections/editorial_constitution.tex:1935: $\kappa_{\mathrm{tot}} = 0$ holds at
chapters/connections/editorial_constitution.tex:2309:The anomaly cancellation programme
chapters/connections/editorial_constitution.tex:2311:the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
chapters/connections/editorial_constitution.tex:2312:mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
standalone/chiral_chern_weil.tex:1233:differential satisfies $d_{\mathrm{bar}}^2 = 0$. On a
 exited 1 in 50ms:

exec
/bin/zsh -lc "sed -n '1900,1940p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa_{\mathrm{tot}} = c/2 - 13 = 0$ at $c = 26$.
\end{proof}

\begin{theorem}[Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0};
\ClaimStatusProvedHere]\label{thm:anomaly-physical-genus0}
The condition $\kappa_{\mathrm{tot}} = 0$
\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul})} is equivalent,
at genus~$0$, to the BRST anomaly cancellation
$c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 0$. The quasi-isomorphism
$\Phi \colon (\cA_{\mathrm{tot}}^{\mathrm{rel}}, Q_{\mathrm{BRST}})
\xrightarrow{\sim} (\barB^{\mathrm{ch}}_0(\cA_{\mathrm{tot}}),
d_{\mathrm{bar}})$ of Theorem~\textup{\ref{thm:brst-bar-genus0}}
identifies both anomaly cancellation conditions.
\end{theorem}

\begin{proof}
This is Corollary~\ref{cor:anomaly-physical-genus0}.
\end{proof}

\begin{theorem}[Physical anomaly cancellation for affine Kac--Moody algebras;
exec
/bin/zsh -lc "sed -n '2192,2204p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(underlying complexes:
$\mathbb{D}(\barB^{(g)}(\cA)) \simeq (\cA^!)^{(g)}_\infty$, factorization \emph{algebra}, not coalgebra).
For self-dual algebras ($\cA \simeq \cA^!$), this gives an internal
involution on the deformation package and hence a symmetric chiral
Hodge diamond. Self-duality alone does \emph{not} force
$\Theta_\cA$ or $\kappa(\cA)$ to vanish; it only constrains how the
Hodge pages are paired. The strongest uncurved form occurs on the
scalar-critical locus $\kappa = 0$, where
$\Theta_\cA^{\min} = 0$ and the bar complex is uncurved.
\end{remark}

\begin{remark}[Computability of the weight filtration]\label{rem:weight-filtration-computable}
The weight filtration on $H^*(\overline{C}_n(X))$ that enters the genus spectral sequence $E_2^{p,q}$ is explicitly computable by combinatorial methods. Bibby--Gadish~\cite{BG24} establish effective algorithms for computing the mixed Hodge structure on configuration space cohomology via intersection lattice data. For our chiral Hodge numbers $h^{p,q}_g(\cA)$, this means the $E_2$ page can in principle be computed from the combinatorial data of the Orlik--Solomon algebra (for genus~$0$) and the augmented OS algebra (for genus~$g \geq 1$), without needing the full geometric machinery of mixed Hodge modules.



thinking
**Clarifying theorems and routing**

I'm exploring how Theorem D employs the bar-intrinsic scalar trace of Theta_A, along with genus-1 curvature normalization and clutching/GRR propagation to determine the scalar shadow. Theorem C offers a complementary perspective via Verdier polarization, but it's not the main input here. 

The route is: bar-intrinsic MC element leads to adjunction, inversion, and scalar trace, establishing genus universality. We should also consider refining Theorem D's section in the file to clarify that D follows after C.
thinking
**Revising dependency implications**

I'm considering a modification that clarifies complementarity without implying dependency. Maybe I can rephrase: “Complementarity provides an ambient polarization, but the scalar projection of the bar tower is intrinsic and needs genus identification.” 

I could also say, “Theorem D identifies a universal genus expansion governed by one scalar.” That feels like it might work. 

Additionally, I should look at file `standalone/survey_modular_koszul_duality_v2`, particularly line 643, and see if the summary there should be more detailed.
thinking
**Inspecting context for clarity**

I'm considering whether line 3178/3189, which states that "the cross-channel correction vanishes at all genera," needs more context, possibly related to uniform-weight. I want to dive into that section to see if there's anything worth highlighting or clarifying. It feels important to ensure everything is clear for whoever is reviewing this. Let's take a closer look to better understand the implications or reasoning behind that statement.
exec
/bin/zsh -lc "sed -n '3170,3193p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$c_{bc}(\lambda) = 1 - 3(2\lambda{-}1)^2$ and
$c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$
satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
ghost cancellation). The complementarity sum
$\kappa(\beta\gamma) + \kappa(bc) = 0$: the free-field
sum rule.

The cross-channel correction vanishes at all genera:
$\delta F_g^{\mathrm{cross}}(\beta\gamma_\lambda) = 0$ for
all~$g \ge 1$ and all~$\lambda$
(Remark~\ref{rem:betagamma-cross-channel-vanishing}). Two
independent mechanisms force this: the single shadow channel
(one-dimensional cyclic cohomology) leaves no room for
mixed-channel assignments, and the off-diagonal Zamolodchikov
metric kills the propagator cross-term. The scalar formula
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ is exact at all
genera without the uniform-weight hypothesis: a special case of
the general principle that free-field algebras have vanishing
cross-channel correction at all genera

thinking
**Planning a patch application**

I think I need to approach this by using one patch with manageable hunks. I want to draft carefully, especially inspecting the exact snippets around the programme_summary sections before applying the patch. I believe we have enough to work with. It’s important to craft a patch for the first batch of core files and maybe some standalone ones. I’ll aim for the first batch of four or five files to keep it manageable, ensuring hunks match to avoid previous issues.
codex
I’m applying the chapter-file edits now. This batch is only the live theorem surfaces: `cor:kappa-additivity`, `thm:universal-generating-function`, the anomaly theorem wording/proof, and the stale introduction/preface phrases.

thinking
**Inspections and patching**

It looks like the patch failed completely, so I need to inspect the snippet around that later line to find out the exact issue. Using smaller patches might work better. I should start with the core subset while excluding that later line. I also need to check if any other files have changed, but it seems like they haven't. I'll take a closer look at the exact text around the km line, especially line breaks, which might be causing problems.
exec
/bin/zsh -lc "sed -n '1930,1944p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \textup{(}Theorem~\textup{\ref{thm:bar-semi-infinite-km})}.
\item The anomaly duality $\kappa + \kappa' = 0$ holds for
 affine Kac--Moody algebras under Feigin--Frenkel duality
 \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
 The matter-ghost anomaly cancellation
 $\kappa_{\mathrm{tot}} = 0$ holds at
 $c = c_{\mathrm{crit}}$.
\item At genus~$0$, the algebraic Kac--Moody package relevant to
 a Chern--Simons comparison is in place:
 classical Maurer--Cartan = flatness,
 $\barB(\widehat{\fg}_k) \simeq
 C^{\infty/2+\bullet}(\widehat{\fg}_k, V_k)$, and the dual
 curvature coefficient satisfies $\kappa + \kappa' = 0$
 \textup{(}Theorem~\textup{\ref{thm:cs-koszul-km})}.
\end{enumerate}
codex
The first multi-file patch bounced on one hunk in `editorial_constitution.tex`. I’m splitting it into smaller patches now so nothing else gets blocked behind that one local mismatch.
file update
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
@@ -3071,3 +3071,4 @@
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
@@ -3104,3 +3105,3 @@
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2498,3 +2498,3 @@
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex
@@ -5985,3 +5985,23 @@
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
M /Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
@@ -1917,4 +1917,5 @@
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
@@ -1928,3 +1929,22 @@
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M chapters/theory/higher_genus_foundations.tex
M chapters/examples/genus_expansions.tex
M chapters/theory/introduction.tex
M chapters/frame/preface.tex
file update:
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.

file update:
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.

file update:
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.


thinking
**Troubleshooting processes**

I’m realizing that I’m still facing issues because nothing has changed. I need to consider whether there are extra spaces causing the problem. My plan is to patch the first half separately and then handle the second part with the correct context, making sure to account for any indent spaces. Hopefully, this approach will lead to a solution! I’m eager to see what works.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
@@ -1877,4 +1877,4 @@
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
@@ -1891,7 +1891,8 @@
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
@@ -2311,3 +2312,3 @@
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M chapters/connections/editorial_constitution.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..99c252836917c106257fae25b12ea781745aaa3e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -2309,7 +2310,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..99c252836917c106257fae25b12ea781745aaa3e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -2309,7 +2310,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
@@ -1935,3 +1935,4 @@
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M chapters/connections/editorial_constitution.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.


thinking
**Evaluating theorem clarity**

I’m thinking that Theorem C offers a stronger perspective—it provides a complementary interpretation of the factorization, but it doesn't give the necessary proof that Theorem D does. I should check the theorem summary at line 103 to see if it’s alright. Also, I might need to inspect any other outdated lines in the five_theorems section, particularly around line 1418, where `kappa` is mentioned as computed in Theorem D.
codex
I’m moving to the standalone propagation now. This batch is summary-only: theorem D blurbs, the `genus-0 data alone` phrasing, and the stale equivalence line in the survey summary.
file update
M /Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex
@@ -86,4 +86,5 @@
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
@@ -819,4 +820,4 @@
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
@@ -1016,4 +1017,5 @@
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
@@ -1022,3 +1024,5 @@
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
M /Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex
@@ -245,4 +245,4 @@
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
@@ -441,4 +441,5 @@
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
@@ -447,3 +448,5 @@
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
M /Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex
@@ -642,5 +642,8 @@
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
@@ -1795,4 +1798,5 @@
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
apply_patch(auto_approved=true) exited 0 in 60ms:
Success. Updated the following files:
M standalone/programme_summary.tex
M standalone/programme_summary_sections2_4.tex
M standalone/survey_modular_koszul_duality_v2.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Patching and inspecting summaries**

I need to patch five_theorems and possibly work on the programme_summary abstract. After that, I might patch `standalone/programme_summary.tex` for theorem D summary—though I’m not fully convinced I need to. Then, I’ll inspect the current contexts after the patch, not necessarily, but it might help ensure precise anchors. I’ll be careful to use small patches with exact current snippets. Let’s focus on getting it right!
file update
M /Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex
@@ -972,5 +972,5 @@
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
@@ -1298,7 +1298,7 @@
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
@@ -1320,8 +1320,6 @@
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
@@ -1337,8 +1335,8 @@
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
@@ -1353,5 +1351,4 @@
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
@@ -1360,7 +1357,7 @@
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
@@ -1432,15 +1429,21 @@
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
@@ -1465,4 +1468,5 @@
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
apply_patch(auto_approved=true) exited 0 in 70ms:
Success. Updated the following files:
M standalone/five_theorems_modular_koszul.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

codex
The main propagation edits are in. I’m doing a hostile grep pass now for the old phrases and dependency language so I can either clear the remaining stragglers or mark them as truly out of scope.
exec
/bin/zsh -lc "rg -n 'Theorem~D is unconditional|Theorem D is unconditional|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|uses the Lagrangian decomposition|genus expansion of Theorem~D|Theorem~D uses the Lagrangian decomposition'"' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:2499: the genus-$1$ clause of Theorem~D is unconditional.
chapters/frame/preface.tex:3106:(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
exec
/bin/zsh -lc "rg -n 'cor:kappa-additivity|thm:universal-generating-function|thm:anomaly-koszul|d_\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0|d_'"\\{\\\\mathrm\\{fib\\}\\}\\"'^2 = 0|genus-'"\\"'$1'"\\"'$ clause of Theorem~D|proved uniform-weight lane|cross-channel correction'"' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections2_4.tex:450:free energy acquires the explicit cross-channel correction
standalone/five_theorems_modular_koszul.tex:1671:No cross-channel correction: $\delta F_g^{\mathrm{cross}} = 0$
standalone/five_theorems_modular_koszul.tex:1835:genus expansion acquires cross-channel corrections for multi-weight
standalone/five_theorems_modular_koszul.tex:2269:cross-channel correction $\delta F_g^{\mathrm{cross}}$
standalone/programme_summary.tex:1026:free energy acquires the explicit cross-channel correction
standalone/survey_modular_koszul_duality_v2.tex:644:proved uniform-weight lane,
standalone/survey_modular_koszul_duality_v2.tex:647:Multi-weight $g\ge 2$ requires the cross-channel correction
standalone/survey_modular_koszul_duality_v2.tex:1080:\emph{fails}: a cross-channel correction from mixed-propagator
standalone/survey_modular_koszul_duality_v2.tex:1088:\textsc{(all-weight, with cross-channel correction)}.
standalone/survey_modular_koszul_duality_v2.tex:1801:$g \ge 2$ with explicit cross-channel correction).
standalone/survey_modular_koszul_duality_v2.tex:4475:(all-weight, with cross-channel correction.)
standalone/survey_modular_koszul_duality_v2.tex:5919:\textsc{(all-weight, with cross-channel correction)}.
standalone/survey_modular_koszul_duality_v2.tex:6999:cross-channel correction
standalone/survey_modular_koszul_duality_v2.tex:7768:admits an explicit cross-channel correction:
standalone/survey_modular_koszul_duality_v2.tex:7776:cross-channel correction covers principal $\cW_N$:
chapters/connections/editorial_constitution.tex:243:all-genera scalar package only on the proved uniform-weight lane.
chapters/connections/editorial_constitution.tex:1870:\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
chapters/connections/editorial_constitution.tex:1877: \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
chapters/connections/editorial_constitution.tex:1879: ($d_{\mathrm{fib}}^2 = 0$) if and only if
chapters/connections/editorial_constitution.tex:1889:Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Considering fix procedures**

Okay, if the user wants to "fix every issue in scope," I need to either provide a fix or state that no edits are needed. I should probably run `rg -n` on the files changed for any AP violations, or maybe grep for `d_{\mathrm{bar}}^2 = 0` specifically in the editorial_constitution theorem area to ensure there’s nothing leftover. I need to inspect the changed snippets and think about using sed or rg for this.
codex
The stale phrases are gone. I’m re-reading the exact edited blocks now, because a few of these are theorem/proof surfaces and I want the final state checked in context before metadata regeneration.
exec
/bin/zsh -lc "sed -n '1914,1955p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5975,6000p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
\index{obstruction coefficient!additivity}
For Koszul chiral algebras $\mathcal{A}$, $\mathcal{B}$ such that $\mathcal{A} \otimes \mathcal{B}$ is Koszul:
\begin{equation}\label{eq:kappa-additivity}
\kappa(\mathcal{A} \otimes \mathcal{B}) = \kappa(\mathcal{A}) + \kappa(\mathcal{B}).
\end{equation}
In particular, on the proved scalar lane,
$\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ for all $g \geq 1$.
\end{corollary}

\begin{proof}
The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
is the sum of the singular parts of $\mathcal{A}$ and
$\mathcal{B}$, since the tensor factors act on disjoint sets of
fields. The genus-$1$ curvature is therefore additive, so the
genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
\[
\kappa(\mathcal{A} \otimes \mathcal{B})
\;=\;
\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
 succeeded in 52ms:

\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
\index{genus expansion!universal generating function}
\index{obstruction coefficient!generating function}
For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
uniform-weight scalar lane, with obstruction coefficient
$\kappa = \kappa(\mathcal{A})$:
\begin{equation}\label{eq:universal-generating-function}
\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
\end{equation}
with radius of convergence $|x| = 2\pi$, independent of $\mathcal{A}$.
For arbitrary modular Koszul algebras, the genus-$1$ coefficient
still satisfies $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
\end{theorem}

\begin{proof}
On the proved uniform-weight scalar lane,
Theorem~\ref{thm:genus-universality}(iii) gives
$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
\[
exec
/bin/zsh -lc "sed -n '814,826p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2308,2318p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1870,1900p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
% ====================================================================
\subsection{The modular characteristic}
\label{ssec:kappa}
% ====================================================================

The modular characteristic $\kappa(\cA)$ is the single
scalar controlling the genus tower. It is computed from
the leading OPE singularity and fixed universally by the
genus-$1$ curvature extracted through the bar construction.

\begin{table}[ht]
\centering
\caption{Modular characteristic for the standard families}
 succeeded in 53ms:
\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
\index{anomaly cancellation!Koszul constraint}
For the matter-ghost system
$\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The obstruction coefficient is additive:
 $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
 \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
\item The total fiberwise bar differential is uncurved
 ($d_{\mathrm{fib}}^2 = 0$) if and only if
 $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
\item For the Virasoro matter-ghost system,
 $\kappa(\mathrm{Vir}_c) = c/2$ and
 $\kappa(\mathrm{ghost}) = c_{\mathrm{ghost}}/2 = -13$, so
 $\kappa_{\mathrm{tot}} = 0$ precisely at $c = 26$.
\end{enumerate}
\end{theorem}

\begin{proof}
Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 succeeded in 53ms:
Vassiliev weight systems of Programme~II
(Proposition~\ref{prop:vassiliev-genus0}).

The anomaly cancellation programme
(\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
physical condition for consistent quantization
(Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
the curvature $m_0 = \kappa \cdot \mathbf{1}$ plays the role of
exec
/bin/zsh -lc "sed -n '640,650p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,252p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1007,1031p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1294,1468p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1794,1803p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '432,454p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '970,1010p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ====================================================================
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar fixed by the genus-$1$
curvature and already visible in the leading OPE singularity
of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure. At $g \ge 2$ for multi-weight algebras, the full
free energy acquires the explicit cross-channel correction
 succeeded in 52ms:
\subsection{The modular characteristic}
\label{ssec:kappa}
% ====================================================================

The modular characteristic $\kappa(\cA)$ is the single
scalar controlling the genus tower. It is computed from
the leading OPE singularity and fixed universally by the
genus-$1$ curvature extracted through the bar construction.

\begin{table}[ht]
\centering
\caption{Modular characteristic for the standard families}
\label{tab:kappa}
 succeeded in 52ms:
where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.

\medskip
\noindent\textbf{Theorem D} (modular characteristic). On the
proved uniform-weight lane,
$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
For every family, the genus-$1$ specialization is unconditional.
Multi-weight $g\ge 2$ requires the cross-channel correction
$\delta F_g^{\mathrm{cross}}$.

\medskip
 succeeded in 51ms:
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
extensions are Theorem~B. Equivalences
(iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
Equivalence (vii) is Theorem~D (uniform-weight at all genera;
genus~$1$ unconditional for all families; multi-weight
$g \ge 2$ with explicit cross-channel correction).

\subsection*{3.4.\enspace Homotopy chiral algebras}
 succeeded in 51ms:
on $\overline{\FM}_n(X)$, and the Verdier intertwining uses
the Poincar\'{e}--Verdier duality on $\Ran(X)$.

\subsection{B establishes faithfulness}

\begin{proposition}[B is necessary for C and strict-dual identification]
\label{prop:B-necessary}
Without Theorem~B, the Lagrangian decomposition of Theorem~C
is vacuous and the relation between the homotopy dual and the
strict Koszul dual is ungrounded.
\end{proposition}

\begin{proof}
Theorem~A constructs the homotopy Koszul dual
$\cA^!_\infty$, but the construction produces a
factorization algebra that a priori differs from $\cA^!$.
Theorem~B proves that bar-cobar inversion is faithful:
$\barB$ is injective on quasi-isomorphism classes. This
identifies $\cA$ and $\cA^!$ as the two canonical algebras
recoverable from the bar coalgebra, and establishes that
 succeeded in 51ms:
\subsection{Theorem D: the modular characteristic}
\label{ssec:thm-d}
% ====================================================================

\begin{theorem}[D]\label{thm:D}
For a uniform-weight modular Koszul chiral algebra\/~$\cA$,
the genus-$g$ obstruction class satisfies
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
\textup{(UNIFORM-WEIGHT)}
for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
additive, duality-constrained scalar fixed by the genus-$1$
curvature and already visible in the leading OPE singularity
of\/~$\cA$. The generating function is
the Hirzebruch $\hat{A}$-class
\textup{(}\eqref{eq:ahat-generating}\textup{)}.
At genus\/~$1$, the identity is unconditional: it holds
for all modular Koszul algebras regardless of weight
structure. At $g \ge 2$ for multi-weight algebras, the full
free energy acquires the explicit cross-channel correction
$\delta F_g^{\mathrm{cross}}$.
 succeeded in 51ms:

\subsection{Statement}

Complementarity supplies an ambient polarization of the genus tower,
but the scalar projection $\kappa$ is already bar-intrinsic and must
still be identified genus by genus.

\begin{theorem}[Theorem D: genus universality]
\label{thm:genus-universality}
Let $\cA$ be a chirally Koszul chiral algebra with modular
characteristic $\kappa(\cA)$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Genus $1$ (unconditional).}
 The genus-$1$ obstruction class is
 \[
 \obs_1(\cA) = \kappa(\cA) \cdot \lambda_1
 \in H^*(\Mbar_{1,1}),
 \]
 and the genus-$1$ free energy is
 $F_1(\cA) = \kappa(\cA)/24$.
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

exec
/bin/zsh -lc "sed -n '1468,1476p' standalone/five_theorems_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 projection still factors through $\kappa$. Theorem~C
 is stronger; it provides a complementary ambient
 interpretation of the factorization, but not the
 load-bearing proof of Theorem~D.

\item \emph{C does not imply B.} The Lagrangian
 decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
 meaningful even if bar-cobar inversion fails; one
 could have a Lagrangian complement indexed by a
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Considering patches and revisions**

I’m thinking about needing a patch for `chapters/connections/editorial_constitution.tex` because the phrase “total fiberwise bar differential is uncurved” sounds awkward. It might be better to say “the total fiberwise bar complex is uncurved” and reference `d_fib^2=0`.  

Then there's `chapters/examples/genus_expansions.tex`, where there's a remark regarding the all-genera generating function, and the genus-1 clause seems fine. I might also check `chapters/connections/concordance.tex` for theorem D—if it’s correct, no changes are necessary.  

I'll run a search on stale phrases across the repo with better-targeted regex.
codex
The edited blocks read cleanly in context. I’m doing one final grep for the exact stale strings that triggered this pass, then I’ll regenerate metadata so the theorem index and registry line references catch up.
exec
/bin/zsh -lc "rg -n 'genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|genus expansion of Theorem~D|uses the Lagrangian decomposition|Theorem~D is unconditional|Theorem D is unconditional|d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0.*Theorem~'"\\\\ref\\{thm:anomaly-koszul\\}|mathematical condition \\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$'"' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/editorial_constitution.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/frame/preface.tex:3106:(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
chapters/theory/introduction.tex:2499: the genus-$1$ clause of Theorem~D is unconditional.
exec
/bin/zsh -lc 'python3 scripts/generate_metadata.py' in /Users/raeez/chiral-bar-cobar succeeded in 222ms:
Generating metadata for chiral-bar-cobar monograph...
  Root: /Users/raeez/chiral-bar-cobar
  Active files (in main.tex): 90
  All .tex files: 104

  Extracted 3112 tagged claims from 104 files

Writing metadata to /Users/raeez/chiral-bar-cobar/metadata/
  claims.jsonl: 3112 claims
  census.json: PH=2367 PE=414 CJ=289 H=27 CD=12 O=3 total=3112
  dependency_graph.dot: 3112 nodes, 2008 edges
  label_index.json: 11124 labels
  theorem_registry.md: 2367 proved claims indexed
  verified_formulas.jsonl: 34 formulas

Done. Run 'make metadata' to regenerate.
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Clarifying grep usage**

I’m noticing that the first grep is still picking up the new phrase because the pattern "TheoremD is unconditional" matches. I need to ensure that any stale exact phrases are removed, though it seems it's not exact since there's an additional clause before. Maybe that’s okay? I should consider a more precise grep for unwanted full lines, perhaps using a fixed string, but it may still match a substring. I’ll check for other stale patterns and maybe look at `git diff` for any changes.
codex
Metadata regenerated cleanly. I’m doing a final diff/grep pass now to confirm only intended files moved and to verify there isn’t a leftover theorem-scope phrase hiding in the regenerated registry or summaries.
exec
/bin/zsh -lc "rg -n 'Theorem~D is unconditional\\.|Theorem D is unconditional\\.|genus expansion of Theorem~D is|uses the Lagrangian decomposition from~C to extract the scalar shadow|restricted to genus~\\"'$0'"\\"'$|genus-'"\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of'"' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/editorial_constitution.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/connections/editorial_constitution.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/theory/introduction.tex chapters/frame/preface.tex standalone/programme_summary.tex standalone/programme_summary_sections2_4.tex standalone/survey_modular_koszul_duality_v2.tex standalone/five_theorems_modular_koszul.tex metadata/theorem_registry.md | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --stat' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/introduction.tex:2499: the genus-$1$ clause of Theorem~D is unconditional.
 succeeded in 53ms:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d02..773d1fe 100644
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@ $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@ $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
 succeeded in 52ms:
 chapters/connections/editorial_constitution.tex |    18 +-
 chapters/examples/genus_expansions.tex          |    26 +-
 chapters/frame/preface.tex                      |     5 +-
 chapters/theory/higher_genus_foundations.tex    |    22 +-
 chapters/theory/introduction.tex                |     2 +-
 metadata/census.json                            |    12 +-
 metadata/claims.jsonl                           |  3170 +++----
 metadata/dependency_graph.dot                   |   113 +-
 metadata/label_index.json                       | 10224 +++++++++++-----------
 metadata/theorem_registry.md                    |  2577 +++---
 standalone/five_theorems_modular_koszul.tex     |    78 +-
 standalone/programme_summary.tex                |    18 +-
 standalone/programme_summary_sections2_4.tex    |    13 +-
 standalone/survey_modular_koszul_duality_v2.tex |    14 +-
 14 files changed, 8134 insertions(+), 8158 deletions(-)
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Planning file operations**

I'm considering the need to grep before and after editing files across three volumes to update duplicates or pending notes related to collisions. I can use exec_command with rg in the directories /chiral-bar-cobar-vol2 and /calabi-yau-quantum-groups, ensuring I'm in a read-only accessible space. The filesystem sandbox likely allows reading files without modification, so I'll go ahead and execute the grep command across those directories. It seems like reading will work well!
codex
I’ve finished the Vol I edits. I’m doing the required cross-volume grep now on Vol II and Vol III for the same theorem-status phrases, so I can confirm there’s no untouched duplicate surface that still advertises the old universality story.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem D|genus-universality|family-index|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|Theorem~D is unconditional|Theorem D is unconditional|d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0|d_'"\\{\\\\mathrm\\{fib\\}\\}\\"'^2 = 0|cross-channel correction'"' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/connections/editorial_constitution.tex
 M chapters/examples/genus_expansions.tex
 M chapters/frame/preface.tex
 M chapters/theory/higher_genus_foundations.tex
 M chapters/theory/introduction.tex
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/dependency_graph.dot
 M metadata/label_index.json
 M metadata/theorem_registry.md
 M standalone/five_theorems_modular_koszul.tex
 M standalone/programme_summary.tex
 M standalone/programme_summary_sections2_4.tex
 M standalone/survey_modular_koszul_duality_v2.tex
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3112:the genus expansion receives cross-channel corrections. The formula
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3127: cross-channel correction is nonzero.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3135:Does the cross-channel correction have an enumerative interpretation
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3196: the cross-channel correction have an integer expansion in BPS
/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:86:**The physics**: The genus expansion of a multi-weight chiral algebra (like W_3, which has generators T of weight 2 and W of weight 3) receives cross-channel corrections from mixed-propagator graphs: graphs where different edges carry different propagator types (T-channel vs W-channel). These corrections are ABSENT for uniform-weight algebras (Heisenberg, Virasoro) and grow to DOMINATE the scalar part at high genus (ratio ~24 at genus 4). This is the quantitative vindication of E_1 primacy: the modular shadow (kappa, the scalar) is an exponentially lossy compression of the full quantum group data.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:531:% For W-algebras: kappa + kappa' = rho*K (Theorem D).
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:86:**The physics**: The genus expansion of a multi-weight chiral algebra (like W_3, which has generators T of weight 2 and W of weight 3) receives cross-channel corrections from mixed-propagator graphs: graphs where different edges carry different propagator types (T-channel vs W-channel). These corrections are ABSENT for uniform-weight algebras (Heisenberg, Virasoro) and grow to DOMINATE the scalar part at high genus (ratio ~24 at genus 4). This is the quantitative vindication of E_1 primacy: the modular shadow (kappa, the scalar) is an exponentially lossy compression of the full quantum group data.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:33:\phantomsection\label{thm:genus-universality}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2206: genera \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$; Vol~I)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2645:at each genus \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2799:receives cross-channel corrections $\delta F_g^{\mathrm{cross}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2813:$g = 1$ but receives multi-weight cross-channel corrections
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3592: $F_g = \kappa_{\mathrm{ch}}\,\lambda_g^{\mathrm{FP}}$ \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4170: (Theorem~\ref{thm:genus-universality}),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4361:\quad \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4680:$F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$, all-weight with cross-channel correction $\delta F_g^{\mathrm{cross}}$) and what it
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5219: \item At genus~$g \geq 2$: $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}} = 2 \cdot \lambda_g^{\mathrm{FP}}$ (all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$) captures the tautological class contribution, while the full genus-$g$ GW invariant receives additional contributions from higher BPS states $n_h^g$ with $g \leq h$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:6:% Theorem D (modular characteristic), Theorem C (complementarity),
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:7:% thm:anomaly-koszul, cor:kappa-additivity, thm:genus-universality,
/Users/raeez/chiral-bar-cobar-vol2/main.tex:632:\phantomsection\label{V1-thm:genus-universality}%
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Reviewing compute libraries**

I'm thinking about the compute libraries from Volume 2, but I'm not sure if that was specifically asked for. There's a note in a document about Theorem D, which relates obs_g to kappa and lambda_g, but lacks qualifiers. I wonder if some of the README files might be outdated based on the audit notes. I'll need to check to see if anything needs to be updated or clarified!
codex
The Vol I pass is complete. I found one genuine cross-volume collision surface I can’t edit from this sandbox: Vol II still repeats the old anomaly wording in `chapters/connections/bv_brst.tex`. I’m pinning the exact lines now so the blocked propagation note is precise rather than vague.
exec
/bin/zsh -lc "sed -n '320,336p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'By Theorem~\\\\ref\\{thm:anomaly-koszul\\}, \\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$|ensures '"\\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$|d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0.*kappa_'"\\{\\\\mathrm\\{tot\\}\\}|Theorem D.*genus-1|Theorem D.*uniform-weight|Theorem D.*cross-channel correction|Theorem D.*all genera' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
At genus~$1$, the $\hat{A}$-genus gives $F_1 = \kappa(\cA)/24$
\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
\end{remark}

\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
\index{anomaly!curvature identification}
By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
\end{remark}

\section{Gauge fixing and BRST}

\subsection{BRST from BV}

 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:330:By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:479:The condition $Q_{\mathrm{BRST}}^2 = 0$ is the BRST instance of the nilpotence-periodicity correspondence (Remark~\ref{rem:nilpotence-periodicity}): $\kappa_{\mathrm{tot}} = 0$ ensures $d_{\mathrm{bar}}^2 = 0$ on the genus-$0$ bar complex, so the bar differential is a genuine differential. When $\kappa_{\mathrm{tot}} \neq 0$, the curvature term $Q_{\mathrm{BRST}}^2 = \frac{c-26}{12}\,c_0 \neq 0$ obstructs nilpotence.
exec
/bin/zsh -lc "sed -n '472,486p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\cA_{\mathrm{tot}}^{\mathrm{rel}} = \ker(b_0) \cap \ker(L_0^{\mathrm{tot}})$
if and only if $c = 26$.
\end{lemma}

\begin{remark}[BRST nilpotence and the bar construction]
\label{rem:brst-nilpotence-periodicity}
\index{nilpotence-periodicity correspondence!BRST instance}
The condition $Q_{\mathrm{BRST}}^2 = 0$ is the BRST instance of the nilpotence-periodicity correspondence (Remark~\ref{rem:nilpotence-periodicity}): $\kappa_{\mathrm{tot}} = 0$ ensures $d_{\mathrm{bar}}^2 = 0$ on the genus-$0$ bar complex, so the bar differential is a genuine differential. When $\kappa_{\mathrm{tot}} \neq 0$, the curvature term $Q_{\mathrm{BRST}}^2 = \frac{c-26}{12}\,c_0 \neq 0$ obstructs nilpotence.
\end{remark}

The \emph{semi-infinite cohomology} $H^{\infty/2+\bullet}(\cA)$
is the cohomology of $(\cA_{\mathrm{tot}}, Q_{\mathrm{BRST}})$, graded
by ghost number. For the bosonic string ($\cA = \mathcal{H}^{26}$,
$c = 26$), this computes the physical state space.

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Considering verification options**

I'm thinking about whether I should run a targeted LaTeX build since the user asked me to verify no new violations. Alternatively, I could just run a targeted grep. But then again, the surface build might not be necessary. However, since changes involve TeX, maybe running `python3 scripts/verify_claims.py` wouldn’t be ideal. I might consider running a `make metadata` equivalent, just like we did before. It’s worth weighing these options!
codex
I’m down to final hygiene checks: diff sanity and whitespace/patch integrity. After that I’ll close with what is fixed in Vol I and what remains blocked outside the writable roots.
exec
/bin/zsh -lc 'git diff --check' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd_\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0.*Theorem~'"\\\\ref\\{thm:anomaly-koszul\\}|By Theorem~\\\\ref\\{thm:anomaly-koszul\\}, \\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$|Theorem~D is unconditional'"\\.|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|uses the Lagrangian decomposition from~C to extract the scalar shadow|genus expansion of Theorem~D is'"' chapters/connections/editorial_constitution.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 52ms:
chapters/theory/introduction.tex:2499: the genus-$1$ clause of Theorem~D is unconditional.
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..5c7e67a395721cdc26ba4cc0a61a8fdf81babf0a
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,7 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..10b75a0dd70b022032743cd9fb55e4cfa1a59c2e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,7 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ clause of Theorem~D is unconditional.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Improving wording**

I’m thinking that by avoiding the grep match, I could enhance the overall clarity or effectiveness of the wording in my output. This seems like a good approach, so I’m planning to implement this change now. Let’s go ahead and make the necessary adjustments! I’m curious to see how this will improve the results. It might really help in making things clearer for the users.
codex
One stale grep is still firing because the replacement phrase still contains the literal substring `Theorem~D is unconditional`. I’m changing those two lines to a different wording so the final pass is clean and unambiguous.
file update
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
@@ -3105,3 +3105,4 @@
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(the genus-$1$ clause of Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ scalar clause of Theorem~D holds there without
+additional hypotheses) and requires the interaction of
 at least two distinct boundary strata.
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2498,3 +2498,4 @@
  Seven-face verification transported to genus~$1$, where
- the genus-$1$ clause of Theorem~D is unconditional.
+ the genus-$1$ scalar clause of Theorem~D holds without
+ additional hypotheses.
 \end{enumerate}
apply_patch(auto_approved=true) exited 0 in 78ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
M chapters/frame/preface.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..fb465730cd1b9cf570ce66a86fd2c2157fa38ec4
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,8 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ scalar clause of Theorem~D holds there without
+additional hypotheses) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..19fb336b252c28b01791b845cd6e2b8686bd6014
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,8 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ scalar clause of Theorem~D holds without
+ additional hypotheses.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..fb465730cd1b9cf570ce66a86fd2c2157fa38ec4
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,8 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ scalar clause of Theorem~D holds there without
+additional hypotheses) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..19fb336b252c28b01791b845cd6e2b8686bd6014
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,8 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ scalar clause of Theorem~D holds without
+ additional hypotheses.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Assessing metadata and theorem registry**

I need to rerun grep and possibly regenerate metadata because line numbers have changed slightly. The introduction and preface don't claim lines, so maybe there's no theorem registry needed. However, if the theorem registry line references changed due to modified files, I need to consider that. Since we modified theorem files earlier, I might rerun grep and check for differences with git diff. It seems the introduction and preface won't affect metadata. Good to clarify!
exec
/bin/zsh -lc 'git diff --check' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "sed -n '2496,2502p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3102,3108p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~D is unconditional\\.|genus-\\"'$0'"\\"'$ data alone|genus-'"\\"'$0'"\\"'$ data of|restricted to genus~'"\\"'$0'"\\"'$|uses the Lagrangian decomposition from~C to extract the scalar shadow|genus expansion of Theorem~D is|d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0.*Theorem~'"\\\\ref\\{thm:anomaly-koszul\\}|By Theorem~\\\\ref\\{thm:anomaly-koszul\\}, \\"'$d_'"\\{\\\\mathrm\\{bar\\}\\}\\"'^2 = 0'"\\"'$'"' chapters/connections/editorial_constitution.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (Ch.~\ref{ch:genus1-seven-faces}).
 Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
 Seven-face verification transported to genus~$1$, where
 the genus-$1$ scalar clause of Theorem~D holds without
 additional hypotheses.
\end{enumerate}

 succeeded in 52ms:
identically for any algebra whose generators share a single
conformal weight (the uniform-weight locus), but is nonzero
whenever the conformal weights are distinct. Multi-weight is a
genuine genus-$2$ phenomenon: it is invisible at genus~$1$
(the genus-$1$ scalar clause of Theorem~D holds there without
additional hypotheses) and requires the interaction of
at least two distinct boundary strata.
 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..fb465730cd1b9cf570ce66a86fd2c2157fa38ec4
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,8 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ scalar clause of Theorem~D holds there without
+additional hypotheses) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..19fb336b252c28b01791b845cd6e2b8686bd6014
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,8 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ scalar clause of Theorem~D holds without
+ additional hypotheses.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 


thinking
**Structuring file content**

I need to ensure that I don’t have any nested bullets, maybe just two flat bullets under FIXED and BLOCKED, or I could use short paragraphs. Since the content is list-shaped, bullets might actually be okay. I’ll keep it within 50-70 lines and try crafting it with bold headers. It’s also important to know the absolute paths, and I might include file links with optional line numbers for key files while keeping some grouped in prose for compactness.
codex
**FIXED**

Vol I is aligned. I updated the live theorem surfaces in [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5975), [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1915), and [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1870), then propagated the narrowed Theorem D scope through [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2496), [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3069), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:814), [programme_summary_sections2_4.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:240), [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:643), and [five_theorems_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:1294). `cor:kappa-additivity` now routes through genus~1 only; `thm:universal-generating-function` is scoped to the proved uniform-weight lane with the genus-1 clause separated; `thm:anomaly-koszul` now uses `d_{\mathrm{fib}}^2 = 0` and the genus-1 curvature direction. The stale `C -> D` dependency prose in the standalone five-theorems file is removed.

[concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:55) was already consistent with the repaired Theorem D status, so it needed verification but no content change.

Verification: I regenerated metadata with `python3 scripts/generate_metadata.py`, ran targeted grep for the old AP228/AP230 phrases and theorem-status drift, and ran `git diff --check`. Those passed in Vol I.

**BLOCKED**

Cross-volume propagation is blocked by sandbox write limits outside `/Users/raeez/chiral-bar-cobar`. I could verify the remaining live collisions but not edit them:
- [bv_brst.tex](</Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:330>) and [bv_brst.tex](</Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:479>) in Vol II still repeat the old anomaly wording with `d_{\mathrm{bar}}^2 = 0`.
- [bar_cobar_bridge.tex](</Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221>) in Vol III still gives a compressed Theorem D summary that should be expanded to the genus-1/all-genera split if you want full cross-volume parity.
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 4c68d029f09375bdc6fed4039ed78930be26877d..773d1fe1e6ea0bebdc902de5b615134335074672
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -1875,8 +1875,8 @@
 \item The obstruction coefficient is additive:
  $\kappa(\cA_{\mathrm{tot}}) = \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})$
  \textup{(}Corollary~\textup{\ref{cor:kappa-additivity})}.
-\item The total bar complex is uncurved
- ($d_{\mathrm{bar}}^2 = 0$) if and only if
+\item The total fiberwise bar differential is uncurved
+ ($d_{\mathrm{fib}}^2 = 0$) if and only if
  $\kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}}) = 0$.
 \item For the Virasoro matter-ghost system,
  $\kappa(\mathrm{Vir}_c) = c/2$ and
@@ -1889,11 +1889,12 @@
 Part (i) is Corollary~\ref{cor:kappa-additivity}: the singular OPE
 of the tensor product is the sum of the individual singular OPEs
 (the fields act on disjoint sectors), so the genus-$1$ curvature
-is additive. Part~(ii) follows from
+is additive. Part~(ii) follows from the genus-$1$ curvature identity
 $\dfib^{\,2} = \kappa \cdot \omega_1 \cdot \mathrm{id}$
-(Theorem~\ref{thm:genus-universality},
-Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
-uncurved if and only if $\kappa_{\mathrm{tot}} = 0$. Part (iii)
+(the genus-$1$ clause of Theorem~\ref{thm:genus-universality},
+Convention~\ref{conv:higher-genus-differentials}): the total
+fiberwise bar differential is uncurved if and only if
+$\kappa_{\mathrm{tot}} = 0$. Part (iii)
 is the computation $\kappa(\mathrm{Vir}_c) = c/2$
 (Computation~\ref{comp:virasoro-curvature}) combined with
 $c_{\mathrm{ghost}} = -26$, so
@@ -1932,7 +1933,8 @@
  affine Kac--Moody algebras under Feigin--Frenkel duality
  \textup{(}Corollary~\textup{\ref{cor:anomaly-duality-km})}.
  The matter-ghost anomaly cancellation
- $\kappa_{\mathrm{tot}} = 0$ holds at
+ $\kappa_{\mathrm{tot}} = 0$, hence $d_{\mathrm{fib}}^2 = 0$,
+ holds at
  $c = c_{\mathrm{crit}}$.
 \item At genus~$0$, the algebraic Kac--Moody package relevant to
  a Chern--Simons comparison is in place:
@@ -2309,7 +2311,7 @@
 The anomaly cancellation programme
 (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of
 the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the
-mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the
+mathematical condition $d_{\mathrm{fib}}^2 = 0$ and the
 physical condition for consistent quantization
 (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the
 AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d..a6d6dfd911ed4c0b52ee65e4381f605474b302ff
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -1915,8 +1915,9 @@
 \begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 \index{genus expansion!universal generating function}
 \index{obstruction coefficient!generating function}
-For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
-weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
+For any modular Koszul chiral algebra $\mathcal{A}$ on the proved
+uniform-weight scalar lane, with obstruction coefficient
+$\kappa = \kappa(\mathcal{A})$:
 \begin{equation}\label{eq:universal-generating-function}
 \sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
 \end{equation}
@@ -1926,7 +1927,26 @@
 \end{theorem}
 
 \begin{proof}
-By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
+On the proved uniform-weight scalar lane,
+Theorem~\ref{thm:genus-universality}(iii) gives
+$F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$, where
+\[
+\lambda_g^{\mathrm{FP}}
+\;=\;
+\frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
+\]
+The proof of Proposition~\ref{prop:complementarity-genus-series}
+shows that
+\[
+\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
+\;=\;
+\frac{x/2}{\sin(x/2)} - 1.
+\]
+Multiplying by $\kappa$ gives
+\eqref{eq:universal-generating-function}. The radius is $2\pi$
+(the first zero of $\sin(x/2)$). For arbitrary modular Koszul
+algebras, the unconditional genus-$1$ clause is the $x^2$
+coefficient $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
 \end{proof}
 
 \begin{remark}\label{rem:universal-generating-specializations}
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280..fb465730cd1b9cf570ce66a86fd2c2157fa38ec4
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -3069,7 +3069,8 @@
 \subsection*{Multi-weight: the cross-channel correction}
 
 The Virasoro algebra has a single generator of weight~$2$. The
-scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds at all genera because the
+scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds on the
+proved uniform-weight scalar lane at all genera because the
 propagator weight~$1$ couples to a single Hodge bundle
 $\mathbb{E}_1$. The question forced by the depth classification
 is whether the scalar formula survives the passage to multiple
@@ -3102,7 +3103,8 @@
 conformal weight (the uniform-weight locus), but is nonzero
 whenever the conformal weights are distinct. Multi-weight is a
 genuine genus-$2$ phenomenon: it is invisible at genus~$1$
-(Theorem~D is unconditional there) and requires the interaction of
+(the genus-$1$ scalar clause of Theorem~D holds there without
+additional hypotheses) and requires the interaction of
 at least two distinct boundary strata.
 
 \subsection*{Drinfeld--Sokolov reduction and the depth escalator}
diff --git a/chapters/theory/higher_genus_foundations.tex b/chapters/theory/higher_genus_foundations.tex
index d2c45bbcdb6f9a2279cccbc0a6ee971971d3a75c..978e4cd5aa19d39d888724500797b0afc2912960
--- a/chapters/theory/higher_genus_foundations.tex
+++ b/chapters/theory/higher_genus_foundations.tex
@@ -5983,7 +5983,27 @@
 \end{corollary}
 
 \begin{proof}
-The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
+The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$
+is the sum of the singular parts of $\mathcal{A}$ and
+$\mathcal{B}$, since the tensor factors act on disjoint sets of
+fields. The genus-$1$ curvature is therefore additive, so the
+genus-$1$ clause of Theorem~\ref{thm:genus-universality} gives
+\[
+\kappa(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+\kappa(\mathcal{A}) + \kappa(\mathcal{B}).
+\]
+On the proved scalar lane, applying
+\eqref{eq:genus-universality} to this identity yields
+\[
+\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B})
+\;=\;
+(\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g
+\;=\;
+\mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})
+\]
+for all $g \geq 1$.
+\end{proof}
 
 \begin{example}
 For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 09413d565658e9d71f63d7dd7327bf183c8a1ea7..19fb336b252c28b01791b845cd6e2b8686bd6014
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2496,7 +2496,8 @@
  (Ch.~\ref{ch:genus1-seven-faces}).
  Elliptic $r$-matrix, KZB connection, Belavin, elliptic Gaudin.
  Seven-face verification transported to genus~$1$, where
- Theorem~D is unconditional.
+ the genus-$1$ scalar clause of Theorem~D holds without
+ additional hypotheses.
 \end{enumerate}
 
 \textbf{Part~\ref{part:v1-frontier}: The Frontier}.
diff --git a/standalone/five_theorems_modular_koszul.tex b/standalone/five_theorems_modular_koszul.tex
index a1472c3d347d419f9f264d5b3d727017009d7899..59270f8688e8f23c99c9ad2a5236371bdf3a9f42
--- a/standalone/five_theorems_modular_koszul.tex
+++ b/standalone/five_theorems_modular_koszul.tex
@@ -970,9 +970,9 @@
 
 \subsection{Statement}
 
-The Lagrangian decomposition of Theorem~C separates $\cA$ from
-$\cA^!$ on moduli space, but does not identify what the scalar
-projection $\kappa$ governs at each genus.
+Complementarity supplies an ambient polarization of the genus tower,
+but the scalar projection $\kappa$ is already bar-intrinsic and must
+still be identified genus by genus.
 
 \begin{theorem}[Theorem D: genus universality]
 \label{thm:genus-universality}
@@ -1296,11 +1296,11 @@
 
 \subsection{B establishes faithfulness}
 
-\begin{proposition}[B is necessary for C--H]
+\begin{proposition}[B is necessary for C and strict-dual identification]
 \label{prop:B-necessary}
 Without Theorem~B, the Lagrangian decomposition of Theorem~C
-is vacuous and the genus expansion of Theorem~D is
-ungrounded.
+is vacuous and the relation between the homotopy dual and the
+strict Koszul dual is ungrounded.
 \end{proposition}
 
 \begin{proof}
@@ -1318,12 +1318,10 @@
 $Q_g(\cA) \oplus Q_g(\cA^!)$ in Theorem~C involves an
 object $\cA^!_\infty$ whose relation to the strict dual
 $\cA^!$ is uncontrolled: the summands may not be
-complementary. The genus expansion of Theorem~D uses the
-Lagrangian decomposition to force the scalar factorization
-$\obs_g = \kappa \cdot \lambda_g$; without the correct
-identification of $\cA^!$, the constraint
-$\kappa + \kappa' = K$ that anchors the genus tower is
-meaningless.
+complementary. Theorem~D is bar-intrinsic and does not use
+this identification to produce the scalar genus tower, but the
+strict-dual interpretation of complementarity and the
+downstream duality package do require it.
 \end{proof}
 
 The geometric input is the \emph{PBW filtration}: the
@@ -1335,12 +1333,12 @@
 
 \subsection{C provides the polarization}
 
-\begin{proposition}[C is necessary for D--H]
+\begin{proposition}[C is necessary for the ambient polarization package]
 \label{prop:C-necessary}
 Without Theorem~C, the genus tower has no canonical
-factorization into $\cA$ and $\cA^!$ contributions, and
-Theorem~D cannot distinguish the universal scalar
-$\kappa$ from family-dependent corrections.
+factorization into $\cA$ and $\cA^!$ contributions, and the
+complementarity interpretation of the scalar genus tower is
+unavailable.
 \end{proposition}
 
 \begin{proof}
@@ -1351,18 +1349,17 @@
 $\mathbf{C}_g(\cA) = R\Gamma(\Mbar_g, \cZ_\cA)$ receives
 contributions from both $\cA$ and its dual. Without the
 Lagrangian decomposition, these contributions are entangled:
-one cannot extract the universal part $\kappa \cdot \lambda_g$
-because the cohomology of $\Mbar_g$ carries mixed classes
-from both sides.
+one loses the canonical ambient polarization into $\cA$ and
+$\cA^!$ sectors.
 
 Theorem~C provides the polarization: the Verdier involution
 decomposes $\mathbf{C}_g$ into eigenspaces, and the scalar
 projection of this decomposition yields the complementarity
-constraint $\kappa + \kappa' = K$. This constraint is the
-input to the genus universality argument: the fact that the
-scalar shadow factors through $\kappa$ alone, at every genus,
-is a consequence of the polarization being Lagrangian (each
-summand carries half the information).
+constraint $\kappa + \kappa' = K$. Theorem~D still extracts the
+universal scalar shadow bar-intrinsically from the genus-$1$
+curvature together with clutching/GRR propagation; Theorem~C
+explains how that scalar sits inside the ambient complex and
+how duality constrains it.
 \end{proof}
 
 The geometric input is the \emph{Verdier involution}: the
@@ -1430,19 +1427,25 @@
 and the Verdier functor on $\Ran(X)$. Theorem~B uses the
 PBW filtration at genus~$0$. Theorem~C uses the Verdier
 involution on $\Mbar_g$ applied to the objects constructed
-in~A and identified in~B. Theorem~D uses the Lagrangian
-decomposition from~C to extract the scalar shadow $\kappa$,
-which was already present in the definition of $\Theta_\cA$
-but not yet identified as universal. Theorem~H uses the
-concentration result from Koszul duality (Theorem~B) to
-bound the coderivation complex.
+in~A and identified in~B. Theorem~D uses the bar-intrinsic
+scalar trace of $\Theta_\cA$, the genus-$1$ curvature
+normalization, and the clutching/GRR propagation to identify
+the scalar shadow $\kappa$, which was already present in the
+definition of $\Theta_\cA$ but not yet identified as
+universal. Theorem~C gives a complementary ambient
+interpretation of the same scalar, but is not the load-bearing
+input to Theorem~D. Theorem~H uses the concentration result
+from Koszul duality (Theorem~B) together with the scalar
+package of Theorem~D to bound the coderivation complex.
 
 The routing is: bar-intrinsic MC element (definition)
-$\to$ adjunction/intertwining (A) $\to$ inversion (B)
-$\to$ polarization (C) $\to$ scalar extraction (D)
-$\to$ coefficient ring (H). Each step uses results from
-the previous step and new geometric input; no step
-requires a result proved later.
+$\to$ adjunction/intertwining (A), then two downstream
+branches. One branch is inversion (B) $\to$ Verdier
+polarization (C). The other is scalar trace
+$+$ genus-$1$ curvature $+$ clutching/GRR
+$\to$ scalar extraction (D). Theorem~H reads the coefficient
+ring against these outputs. No step requires a result proved
+later.
 \end{remark}
 
 \subsection{Independence of converses}
@@ -1463,8 +1466,9 @@
  without a Lagrangian decomposition: one could imagine
  a non-decomposable ambient complex whose scalar
  projection still factors through $\kappa$. Theorem~C
- is stronger; it provides the \emph{reason} for the
- factorization.
+ is stronger; it provides a complementary ambient
+ interpretation of the factorization, but not the
+ load-bearing proof of Theorem~D.
 
 \item \emph{C does not imply B.} The Lagrangian
  decomposition $Q_g(\cA) \oplus Q_g(\cA^!)$ is
diff --git a/standalone/programme_summary.tex b/standalone/programme_summary.tex
index 3102669d44cc66dee8dd6193ad5099c063b7d231..0c47672f3eee55fe31b49cd85f43efe042342178
--- a/standalone/programme_summary.tex
+++ b/standalone/programme_summary.tex
@@ -84,8 +84,9 @@
 inversion on the Koszul locus~(B), complementarity
 decomposition with shifted-symplectic Lagrangian
 geometry~(C), the genus expansion
-$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (uniform-weight) governed by
-the Hirzebruch $\hat{A}$-class~(D), and polynomial
+$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
+uniform-weight lane, with genus~$1$ universal for every
+family, governed by the Hirzebruch $\hat{A}$-class~(D), and polynomial
 chiral Hochschild cohomology~(H). All five are projections
 of a single universal Maurer--Cartan element~$\Theta_\cA$
 in the modular convolution algebra. The shadow obstruction
@@ -817,8 +818,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -1014,13 +1015,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/programme_summary_sections2_4.tex b/standalone/programme_summary_sections2_4.tex
index b1d11f7e5fd9d746327afa89ab0432dea47d15b8..921c461b8069ceff1bc2f00c29eead06ca4f5676
--- a/standalone/programme_summary_sections2_4.tex
+++ b/standalone/programme_summary_sections2_4.tex
@@ -243,8 +243,8 @@
 
 The modular characteristic $\kappa(\cA)$ is the single
 scalar controlling the genus tower. It is computed from
-genus-$0$ data alone: the leading coefficient of the OPE,
-extracted through the bar construction.
+the leading OPE singularity and fixed universally by the
+genus-$1$ curvature extracted through the bar construction.
 
 \begin{table}[ht]
 \centering
@@ -439,13 +439,16 @@
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(UNIFORM-WEIGHT)}
 for all\/ $g \ge 1$, where $\kappa(\cA)$ is a universal,
-additive, duality-constrained scalar determined by the
-genus-$0$ data of\/~$\cA$. The generating function is
+additive, duality-constrained scalar fixed by the genus-$1$
+curvature and already visible in the leading OPE singularity
+of\/~$\cA$. The generating function is
 the Hirzebruch $\hat{A}$-class
 \textup{(}\eqref{eq:ahat-generating}\textup{)}.
 At genus\/~$1$, the identity is unconditional: it holds
 for all modular Koszul algebras regardless of weight
-structure.
+structure. At $g \ge 2$ for multi-weight algebras, the full
+free energy acquires the explicit cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 \end{theorem}
 
 The universality is the point: no matter how complicated
diff --git a/standalone/survey_modular_koszul_duality_v2.tex b/standalone/survey_modular_koszul_duality_v2.tex
index d22685a4c4d9c8b7ef5549a8a85897ca10d21294..3d85546a20064d41a06cdcd6255ba9bd27010299
--- a/standalone/survey_modular_koszul_duality_v2.tex
+++ b/standalone/survey_modular_koszul_duality_v2.tex
@@ -640,9 +640,12 @@
 where $K=0$ for Kac--Moody and free fields, $K=13$ for Virasoro.
 
 \medskip
-\noindent\textbf{Theorem D} (modular characteristic). For uniform
-weight, $\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ . Multi-weight $g\ge 2$ requires the cross-channel
-correction $\delta F_g^{\mathrm{cross}}$.
+\noindent\textbf{Theorem D} (modular characteristic). On the
+proved uniform-weight lane,
+$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ at all genera.
+For every family, the genus-$1$ specialization is unconditional.
+Multi-weight $g\ge 2$ requires the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$.
 
 \medskip
 \noindent\textbf{Theorem H} (chiral Hochschild).
@@ -1793,8 +1796,9 @@
 classical (Priddy, Beilinson--Ginzburg--Soergel); their chiral
 extensions are Theorem~B. Equivalences
 (iv)$\Leftrightarrow$(v)$\Leftrightarrow$(vi) are Theorem~H.
-Equivalence (vii) is Theorem~D (uniform-weight; multi-weight
-restricted to genus~$0$).
+Equivalence (vii) is Theorem~D (uniform-weight at all genera;
+genus~$1$ unconditional for all families; multi-weight
+$g \ge 2$ with explicit cross-channel correction).
 
 \subsection*{3.4.\enspace Homotopy chiral algebras}
 

tokens used
376,256
